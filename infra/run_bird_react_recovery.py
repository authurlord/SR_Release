#!/usr/bin/env python3
"""Run budget-matched raw and recovered-schema ReAct on a BIRD dev subset."""

from __future__ import annotations

import argparse
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, as_completed, wait
from hashlib import sha256
import json
import os
from pathlib import Path
from threading import Lock
import time
from typing import Any

import httpx
import numpy as np

from finsemguard.agent.llm import VLLMClient
from finsemguard.config import load_config
from finsemguard.e2e.livesqlbench import CatalogDocument
from finsemguard.e2e.livesqlbench_runner import _load_jsonl, _write_atomic
from finsemguard.e2e.performance_pipeline import _database_path
from finsemguard.e2e.react_text2sql import (
    SchemaSearchIndex,
    build_grounded_profile_documents,
    build_recovery_documents,
    run_react_text2sql,
)
from finsemguard.e2e.sqlite_catalog import load_catalog


EMBEDDING_MODEL_ID = "BAAI/bge-m3"


class _OpenAIEmbeddingBackend:
    """Minimal deterministic adapter for a vLLM pooling endpoint."""

    def __init__(self, *, base_url: str, model: str) -> None:
        self.base_url = base_url.rstrip("/")
        self.model = model
        self.concurrency = int(
            os.environ.get("SCHEMARECOVERY_EMBEDDING_CONCURRENCY", "8")
        )
        if self.concurrency < 1 or self.concurrency > 64:
            raise ValueError(
                "SCHEMARECOVERY_EMBEDDING_CONCURRENCY must be in [1, 64]"
            )
        self.client = httpx.Client(
            timeout=180.0,
            trust_env=False,
            limits=httpx.Limits(
                max_connections=self.concurrency * 2,
                max_keepalive_connections=self.concurrency,
            ),
        )
        response = self.client.get(f"{self.base_url}/models")
        response.raise_for_status()
        served = {
            str(value.get("id") or "")
            for value in response.json().get("data") or []
        }
        if model not in served:
            raise RuntimeError(
                f"required embedding model {model!r} is absent from {served!r}"
            )

    def _encode_batch(
        self, batch: list[str], *, offset: int, max_length: int
    ) -> tuple[int, list[list[float]]]:
        last_error: Exception | None = None
        for attempt in range(4):
            try:
                response = self.client.post(
                    f"{self.base_url}/embeddings",
                    json={
                        "model": self.model,
                        "input": batch,
                        "encoding_format": "float",
                        "truncate_prompt_tokens": max_length,
                    },
                )
                response.raise_for_status()
                values = sorted(
                    response.json().get("data") or [],
                    key=lambda value: int(value["index"]),
                )
                if len(values) != len(batch):
                    raise RuntimeError(
                        "embedding endpoint returned an incomplete batch"
                    )
                return offset, [value["embedding"] for value in values]
            except (httpx.HTTPError, KeyError, TypeError, RuntimeError) as error:
                last_error = error
                if attempt < 3:
                    time.sleep(1.0 * (attempt + 1))
        raise RuntimeError(
            f"remote BGE-M3 embedding failed at offset {offset}"
        ) from last_error

    def _encode(
        self, texts: list[str], *, batch_size: int, max_length: int
    ) -> dict[str, np.ndarray]:
        batches = [
            (offset, texts[offset : offset + batch_size])
            for offset in range(0, len(texts), batch_size)
        ]
        rows_by_offset: dict[int, list[list[float]]] = {}
        completed_rows = 0
        next_batch = 0
        with ThreadPoolExecutor(max_workers=self.concurrency) as executor:
            pending: dict[Any, tuple[int, int]] = {}

            def submit_one() -> None:
                nonlocal next_batch
                offset, batch = batches[next_batch]
                future = executor.submit(
                    self._encode_batch,
                    batch,
                    offset=offset,
                    max_length=max_length,
                )
                pending[future] = (offset, len(batch))
                next_batch += 1

            while next_batch < min(len(batches), self.concurrency * 2):
                submit_one()
            while pending:
                done, _ = wait(
                    pending,
                    timeout=1.0,
                    return_when=FIRST_COMPLETED,
                )
                if not done:
                    continue
                for future in done:
                    _, row_count = pending.pop(future)
                    offset, vectors = future.result()
                    rows_by_offset[offset] = vectors
                    completed_rows += row_count
                    if (
                        completed_rows == len(texts)
                        or completed_rows // 1000
                        != (completed_rows - row_count) // 1000
                    ):
                        print(
                            f"[bge-remote-poll] encoded={completed_rows}/{len(texts)} "
                            f"concurrency={self.concurrency}",
                            flush=True,
                        )
                    if next_batch < len(batches):
                        submit_one()
        ordered = [
            vector
            for offset, _ in batches
            for vector in rows_by_offset[offset]
        ]
        return {"dense_vecs": np.asarray(ordered, dtype=np.float32)}

    def encode(
        self, texts: list[str], *, batch_size: int, max_length: int
    ) -> dict[str, np.ndarray]:
        return self._encode(texts, batch_size=batch_size, max_length=max_length)

    def encode_queries(
        self, texts: list[str], *, batch_size: int, max_length: int
    ) -> dict[str, np.ndarray]:
        return self._encode(texts, batch_size=batch_size, max_length=max_length)


def _canonical_hash(value: Any) -> str:
    return sha256(
        json.dumps(
            value,
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode()
    ).hexdigest()


def _write_json(path: Path, value: dict[str, Any]) -> None:
    content = json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if path.exists():
        if path.read_text(encoding="utf-8") != content:
            raise FileExistsError(f"refusing to overwrite different artifact: {path}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(content, encoding="utf-8")
    temporary.replace(path)


def _stable_subset(
    rows: list[dict[str, Any]], *, difficulty: str, size: int
) -> list[dict[str, Any]]:
    selected = (
        list(rows)
        if difficulty.casefold() == "all"
        else [row for row in rows if str(row.get("difficulty")) == difficulty]
    )
    groups: dict[tuple[str, str], list[dict[str, Any]]] = {}
    for row in selected:
        key = (str(row.get("difficulty") or "unknown"), str(row["database_id"]))
        groups.setdefault(key, []).append(row)
    for values in groups.values():
        values.sort(key=lambda row: sha256(str(row["example_id"]).encode()).digest())
    by_difficulty: dict[str, list[dict[str, Any]]] = {}
    for level in sorted({key[0] for key in groups}):
        level_rows: list[dict[str, Any]] = []
        database_ids = sorted(
            (key[1] for key in groups if key[0] == level),
            key=lambda database_id: sha256(
                f"{level}::{database_id}".encode()
            ).digest(),
        )
        offset = 0
        while True:
            progressed = False
            for database_id in database_ids:
                values = groups[(level, database_id)]
                if offset < len(values):
                    level_rows.append(values[offset])
                    progressed = True
            if not progressed:
                break
            offset += 1
        by_difficulty[level] = level_rows
    output: list[dict[str, Any]] = []
    levels = sorted(by_difficulty)
    offset = 0
    while len(output) < min(size, len(selected)):
        progressed = False
        for level in levels:
            values = by_difficulty[level]
            if offset < len(values):
                output.append(values[offset])
                progressed = True
                if len(output) >= size:
                    break
        if not progressed:
            break
        offset += 1
    return output


class BGEEncoder:
    def __init__(
        self,
        *,
        model_path: Path,
        documents: list[CatalogDocument],
        cache_path: Path,
        batch_size: int,
        seed_cache_paths: list[Path] | None = None,
    ) -> None:
        resolved = model_path.resolve()
        if resolved.name.casefold() != "bge-m3":
            raise ValueError("embedding model must be BAAI/bge-m3; MiniLM is forbidden")
        required = {
            "config.json",
            "pytorch_model.bin",
            "colbert_linear.pt",
            "sparse_linear.pt",
            "sentencepiece.bpe.model",
        }
        missing = sorted(name for name in required if not (resolved / name).is_file())
        if missing:
            raise FileNotFoundError(f"incomplete BGE-M3 model: {missing}")
        self.model_path = resolved
        self.batch_size = int(batch_size)
        self.lock = Lock()
        self.query_cache: dict[str, np.ndarray] = {}
        embedding_base_url = os.environ.get(
            "SCHEMARECOVERY_EMBEDDING_BASE_URL", ""
        ).strip()
        embedding_model = os.environ.get(
            "SCHEMARECOVERY_EMBEDDING_MODEL", "bge-m3"
        ).strip()
        self.backend = (
            "vllm_openai_pooling_v1"
            if embedding_base_url
            else "flagembedding_cpu_v1"
        )
        ids = [row.candidate_id for row in documents]
        texts = [row.retrieval_text() for row in documents]
        fingerprint = _canonical_hash(
            {
                "model_id": EMBEDDING_MODEL_ID,
                "model_path": str(resolved),
                "documents": list(zip(ids, texts, strict=True)),
                **(
                    {
                        "embedding_backend": self.backend,
                        "served_model": embedding_model,
                    }
                    if embedding_base_url
                    else {}
                ),
            }
        )
        vectors: np.ndarray | None = None
        if cache_path.is_file():
            cached = np.load(cache_path, allow_pickle=False)
            if (
                str(cached["fingerprint"].item()) == fingerprint
                and cached["document_ids"].tolist() == ids
            ):
                vectors = np.asarray(cached["vectors"], dtype=np.float32)
            else:
                raise FileExistsError(
                    f"refusing to overwrite incompatible embedding cache: {cache_path}"
                )
        if embedding_base_url:
            self.model = _OpenAIEmbeddingBackend(
                base_url=embedding_base_url,
                model=embedding_model,
            )
        else:
            from FlagEmbedding import BGEM3FlagModel

            self.model = BGEM3FlagModel(
                str(resolved),
                use_fp16=False,
                devices="cpu",
                trust_remote_code=False,
            )
        if vectors is None:
            # Content-addressed embedding IDs allow unchanged documents to be
            # reused safely when only a small evidence lane changes.  Generic
            # caller-provided IDs are deliberately excluded because the same ID
            # could otherwise hide modified text.
            reusable: dict[str, np.ndarray] = {}
            current_ids = set(ids)
            for seed_path in seed_cache_paths or []:
                if not seed_path.is_file():
                    continue
                seed = np.load(seed_path, allow_pickle=False)
                if embedding_base_url and (
                    "embedding_backend" not in seed.files
                    or str(seed["embedding_backend"].item()) != self.backend
                ):
                    continue
                seed_ids = seed["document_ids"].tolist()
                seed_vectors = np.asarray(seed["vectors"], dtype=np.float32)
                for candidate_id, vector in zip(seed_ids, seed_vectors, strict=True):
                    if (
                        candidate_id in current_ids
                        and str(candidate_id).startswith("embedding_text::")
                    ):
                        reusable[str(candidate_id)] = vector
            missing = [index for index, candidate_id in enumerate(ids) if candidate_id not in reusable]
            encoded: dict[int, np.ndarray] = {}
            if missing:
                fresh = np.asarray(
                    self.model.encode(
                        [texts[index] for index in missing],
                        batch_size=batch_size,
                        max_length=512,
                    )["dense_vecs"],
                    dtype=np.float32,
                )
                fresh = self._normalize(fresh)
                encoded = dict(zip(missing, fresh, strict=True))
            vectors = np.asarray(
                [
                    reusable[candidate_id]
                    if candidate_id in reusable
                    else encoded[index]
                    for index, candidate_id in enumerate(ids)
                ],
                dtype=np.float32,
            )
            vectors = self._normalize(vectors)
            print(
                f"[bge-cache] reused={len(ids) - len(missing)} "
                f"encoded={len(missing)} total={len(ids)}",
                flush=True,
            )
            cache_path.parent.mkdir(parents=True, exist_ok=True)
            np.savez_compressed(
                cache_path,
                fingerprint=np.asarray(fingerprint),
                embedding_backend=np.asarray(self.backend),
                document_ids=np.asarray(ids),
                vectors=vectors,
            )
        self.vectors = {
            candidate_id: vector
            for candidate_id, vector in zip(ids, vectors, strict=True)
        }
        self.fingerprint = fingerprint

    @staticmethod
    def _normalize(vectors: np.ndarray) -> np.ndarray:
        denominator = np.linalg.norm(vectors, axis=-1, keepdims=True)
        return vectors / np.maximum(denominator, 1e-12)

    def encode_query(self, text: str) -> np.ndarray:
        return self.encode_queries([text])[0]

    def encode_queries(self, texts: list[str]) -> np.ndarray:
        """Encode a query batch under one model lock and cache every row."""

        with self.lock:
            missing = list(
                dict.fromkeys(text for text in texts if text not in self.query_cache)
            )
            if missing:
                vectors = np.asarray(
                    self.model.encode_queries(
                        missing,
                        batch_size=min(self.batch_size, len(missing)),
                        max_length=512,
                    )["dense_vecs"],
                    dtype=np.float32,
                )
                vectors = self._normalize(vectors)
                self.query_cache.update(dict(zip(missing, vectors, strict=True)))
            return np.asarray(
                [self.query_cache[text] for text in texts], dtype=np.float32
            )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-root", type=Path, required=True)
    parser.add_argument("--online", type=Path, required=True)
    parser.add_argument("--table-inputs", type=Path, required=True)
    parser.add_argument("--recovery", type=Path, required=True)
    parser.add_argument("--embedding-model", type=Path, required=True)
    parser.add_argument("--embedding-cache", type=Path, required=True)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument(
        "--condition",
        action="append",
        choices=["raw_react", "recovered_react", "grounded_react"],
        default=[],
    )
    parser.add_argument("--difficulty", default="challenging")
    parser.add_argument("--subset-size", type=int, default=64)
    parser.add_argument("--example-id", action="append", default=[])
    parser.add_argument("--concurrency", type=int, default=4)
    parser.add_argument("--embedding-batch-size", type=int, default=32)
    parser.add_argument("--max-turns", type=int, default=4)
    parser.add_argument("--max-actions", type=int, default=8)
    parser.add_argument("--max-sql-executions", type=int, default=3)
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()
    if args.subset_size < 1 or args.concurrency < 1:
        raise ValueError("subset size and concurrency must be positive")
    conditions = args.condition or ["raw_react", "recovered_react"]
    all_rows = _load_jsonl(args.online)
    if args.example_id:
        requested = set(args.example_id)
        rows = [row for row in all_rows if str(row["example_id"]) in requested]
        if {str(row["example_id"]) for row in rows} != requested:
            raise ValueError("one or more example IDs are absent")
    else:
        rows = _stable_subset(
            all_rows, difficulty=args.difficulty, size=args.subset_size
        )
    if not rows:
        raise ValueError("selected subset is empty")
    args.output_root.mkdir(parents=True, exist_ok=True)
    subset_path = args.output_root / "SUBSET.jsonl"
    subset_content = "".join(
        json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows
    )
    if subset_path.exists() and subset_path.read_text(encoding="utf-8") != subset_content:
        raise FileExistsError("refusing to change frozen subset")
    if not subset_path.exists():
        subset_path.write_text(subset_content, encoding="utf-8")

    raw_documents = load_catalog(
        "bird", args.data_root, rows, bird_schema_view="physical"
    )
    requested_databases = {str(row["database_id"]) for row in rows}
    table_inputs = [
        row
        for row in _load_jsonl(args.table_inputs)
        if str(row["schema_context"]) in requested_databases
    ]
    recovery_rows = [
        row
        for row in _load_jsonl(args.recovery)
        if str(row["schema_context"]) in requested_databases
    ]
    recovery_documents = (
        build_recovery_documents(table_inputs, recovery_rows)
        if "recovered_react" in conditions
        else []
    )
    grounded_documents = build_grounded_profile_documents(table_inputs)
    # Grounded profiles are identifier-bound sidecars, not retrieval candidates.
    # Embedding them alongside physical schema would make them compete for top-k
    # slots and confound evidence enrichment with a changed candidate ranking.
    all_documents = [*raw_documents, *recovery_documents]
    encoder = BGEEncoder(
        model_path=args.embedding_model,
        documents=all_documents,
        cache_path=args.embedding_cache,
        batch_size=args.embedding_batch_size,
    )
    raw_ids = {row.candidate_id for row in raw_documents}
    raw_index = SchemaSearchIndex(
        documents=raw_documents,
        raw_documents=raw_documents,
        vectors={key: value for key, value in encoder.vectors.items() if key in raw_ids},
        encode_query=encoder.encode_query,
    )
    recovered_index = SchemaSearchIndex(
        documents=[*raw_documents, *recovery_documents],
        raw_documents=raw_documents,
        vectors={
            row.candidate_id: encoder.vectors[row.candidate_id]
            for row in [*raw_documents, *recovery_documents]
        },
        encode_query=encoder.encode_query,
    )
    grounded_index = SchemaSearchIndex(
        documents=raw_documents,
        raw_documents=raw_documents,
        vectors={key: value for key, value in encoder.vectors.items() if key in raw_ids},
        encode_query=encoder.encode_query,
        sidecar_documents=grounded_documents,
    )
    indices = {
        "raw_react": raw_index,
        "recovered_react": recovered_index,
        "grounded_react": grounded_index,
    }
    client = VLLMClient(dict(load_config(args.config)["llm"]))
    if not client.healthy():
        raise RuntimeError(f"required exact LLM is unavailable at {client.base_url}")

    paths = {condition: args.output_root / f"{condition}.jsonl" for condition in conditions}
    if not args.resume and any(path.exists() for path in paths.values()):
        raise FileExistsError("output exists; use --resume or a new output root")
    completed: dict[str, dict[str, dict[str, Any]]] = {}
    for condition, path in paths.items():
        prior = _load_jsonl(path) if args.resume and path.is_file() else []
        completed[condition] = {
            str(row["example_id"]): row for row in prior if row.get("status") != "error"
        }
    lock = Lock()

    def run(row: dict[str, Any]) -> dict[str, dict[str, Any]]:
        example_id = str(row["example_id"])
        order = list(conditions)
        if sha256(example_id.encode()).digest()[0] % 2:
            order.reverse()
        output: dict[str, dict[str, Any]] = {}
        for condition in order:
            if example_id in completed[condition]:
                continue
            output[condition] = run_react_text2sql(
                condition=condition,
                row=row,
                client=client,
                database=_database_path(args.data_root, row),
                search_index=indices[condition],
                max_turns=args.max_turns,
                max_actions=args.max_actions,
                max_sql_executions=args.max_sql_executions,
            )
        return output

    pending = [
        row
        for row in rows
        if any(str(row["example_id"]) not in completed[value] for value in conditions)
    ]
    with ThreadPoolExecutor(max_workers=args.concurrency) as executor:
        futures = {executor.submit(run, row): row for row in pending}
        for index, future in enumerate(as_completed(futures), start=1):
            results = future.result()
            with lock:
                for condition, result in results.items():
                    completed[condition][str(result["example_id"])] = result
                    with paths[condition].open("a", encoding="utf-8") as handle:
                        handle.write(json.dumps(result, ensure_ascii=False) + "\n")
                        handle.flush()
            if index % 5 == 0 or index == len(futures):
                print(f"[react {index}/{len(futures)}]", flush=True)
    ordered: dict[str, list[dict[str, Any]]] = {}
    for condition, path in paths.items():
        ordered[condition] = [
            completed[condition][str(row["example_id"])] for row in rows
        ]
        _write_atomic(path, ordered[condition])
    summary = {
        "protocol": "bird_budget_matched_react_recovery_dev_v1",
        "rows": len(rows),
        "conditions": conditions,
        "subset_sha256": sha256(subset_path.read_bytes()).hexdigest(),
        "selection": {
            "gold_used": False,
            "difficulty": args.difficulty if not args.example_id else None,
            "strategy": "difficulty-and-database-stratified stable hash round-robin",
        },
        "model": {
            "requested": client.model,
            "require_exact": client.require_exact_model,
            "thinking": client.thinking,
        },
        "embedding": {
            "model_id": EMBEDDING_MODEL_ID,
            "device": "cpu",
            "fingerprint": encoder.fingerprint,
            "minilm_used": False,
        },
        "budgets": {
            "max_turns": args.max_turns,
            "max_actions": args.max_actions,
            "max_sql_executions": args.max_sql_executions,
            "token_budget": client.token_budget_status(),
        },
        "usage": {
            condition: {
                "model_calls": sum(
                    int(row["audit"]["model_calls"]) for row in values
                ),
                "known_total_tokens": sum(
                    int(row["audit"]["known_total_tokens"]) for row in values
                ),
                "mean_turns": round(
                    sum(int(row["react"]["turns"]) for row in values)
                    / len(values),
                    3,
                ),
            }
            for condition, values in ordered.items()
        },
        "evaluator_manifest_read": False,
    }
    _write_json(args.output_root / "GENERATION_SUMMARY.json", summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
