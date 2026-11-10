from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from functools import lru_cache
import hashlib
import json
import os
from pathlib import Path
import threading
import time
from typing import Any

import numpy as np

from finsemguard.agent.llm import VLLMClient
from finsemguard.e2e.livesqlbench import CatalogDocument, evidence_closure, load_catalog
from finsemguard.retrieval.bm25 import tokenize


METHOD_ID = "evidence_bounded_semantic_subgraph_shared_sql_agent_v2"
SELECTION_TOOL = "select_semantic_subgraph"
SELECTION_MAX_ITEMS = 32
SELECTOR_SYSTEM = """You compile a compact semantic subgraph for Text-to-SQL.
Select the smallest sufficient set of opaque handles covering every projection, filter,
calculation, grouping, ordering, JSON path, external rule and PK/FK join path required by
the question. Use only handles in the candidate manifest. Prefer recall over speculative
semantics, but do not pad the context. Call select_semantic_subgraph exactly once."""

SQL_SYSTEM = """You are the shared deterministic PostgreSQL Data Agent used for every
compared context compiler. Use only the supplied semantic subgraph and documentation.
Never invent a table, column, JSON path, relationship, literal meaning, or business rule.
Return one JSON object with exactly decision, sql, clarification, and answer. decision is
answer, clarify, or abstain. When answerable, sql is exactly one PostgreSQL statement and
contains no markdown. Preserve requested rounding, ordering, aliases and scalar/table
shape. For a Query task, generate a read-only SELECT/WITH query. For a Management task,
generate the requested single statement but do not assume it has already executed. If
essential evidence is missing or conflicting, clarify or abstain and set sql to null."""


def _canonical_hash(value: Any) -> str:
    encoded = json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode()
    return hashlib.sha256(encoded).hexdigest()


def _file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


@lru_cache(maxsize=8)
def _embedding_model_inventory_sha256(model_path_text: str) -> str:
    model_path = Path(model_path_text).resolve()
    if not (model_path / "config.json").is_file():
        raise FileNotFoundError(
            f"embedding model config is missing: {model_path / 'config.json'}"
        )
    files = [
        path
        for path in sorted(model_path.rglob("*"))
        if path.is_file()
        and not any(
            part in {".git", ".cache", "__pycache__"}
            for part in path.relative_to(model_path).parts
        )
    ]
    weight_files = [
        path
        for path in files
        if path.suffix in {".safetensors", ".bin"}
    ]
    if not weight_files:
        raise ValueError("embedding model inventory contains no weight file")
    inventory = [
        {
            "path": path.relative_to(model_path).as_posix(),
            "bytes": path.stat().st_size,
            "sha256": _file_sha256(path),
        }
        for path in files
    ]
    return _canonical_hash(inventory)


def _validate_embedding_model_for_run(model_path: Path, output: Path) -> str:
    inventory_sha256 = _embedding_model_inventory_sha256(
        str(model_path.resolve())
    )
    identity_path = output.parent / "RUN_IDENTITY.json"
    if not identity_path.is_file():
        return inventory_sha256
    identity = json.loads(identity_path.read_text(encoding="utf-8"))
    expected = identity.get("identity", {}).get("retrieval", {})
    if expected and (
        Path(str(expected.get("embedder_path", ""))).resolve()
        != model_path.resolve()
        or expected.get("embedder_inventory_sha256")
        != inventory_sha256
    ):
        raise RuntimeError(
            "embedding model path/inventory differs from immutable run identity"
        )
    return inventory_sha256


def _load_jsonl(path: Path) -> list[dict[str, Any]]:
    with path.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def _validate_resume_rows(
    rows: list[dict[str, Any]], *, expected_method_id: str = METHOD_ID
) -> None:
    stale_methods = {
        str(row.get("method_id"))
        for row in rows
        if row.get("method_id") != expected_method_id
    }
    if stale_methods:
        raise ValueError(
            "resume artifact uses an incompatible method contract: "
            f"{sorted(stale_methods)}"
        )


def _rrf(*rankings: list[str], constant: int = 60) -> list[str]:
    scores: dict[str, float] = {}
    best: dict[str, int] = {}
    for ranking in rankings:
        for rank, candidate_id in enumerate(ranking):
            scores[candidate_id] = scores.get(candidate_id, 0.0) + 1.0 / (constant + rank + 1)
            best[candidate_id] = min(best.get(candidate_id, rank), rank)
    return sorted(scores, key=lambda item: (-scores[item], best[item], item))


def _lexical_rank(question: str, documents: list[CatalogDocument]) -> list[str]:
    query_tokens = set(tokenize(question))
    scored = []
    for index, document in enumerate(documents):
        tokens = set(tokenize(document.retrieval_text()))
        overlap = len(query_tokens & tokens)
        score = overlap / max(1, len(query_tokens | tokens))
        scored.append((score, overlap, -index, document.candidate_id))
    return [row[-1] for row in sorted(scored, reverse=True)]


def _dense_rank(
    query_vector: np.ndarray,
    documents: list[CatalogDocument],
    vector_by_id: dict[str, np.ndarray],
) -> list[str]:
    matrix = np.asarray([vector_by_id[row.candidate_id] for row in documents])
    scores = matrix @ query_vector
    return [documents[int(index)].candidate_id for index in np.argsort(-scores)]


def _candidate_pool(
    ranking: list[str], all_documents: dict[str, CatalogDocument]
) -> list[CatalogDocument]:
    limits = {"table": 16, "column": 48, "knowledge": 12}
    counts = {kind: 0 for kind in limits}
    output = []
    for candidate_id in ranking:
        document = all_documents[candidate_id]
        if counts[document.kind] >= limits[document.kind]:
            continue
        output.append(document)
        counts[document.kind] += 1
        if all(counts[kind] >= limit for kind, limit in limits.items()):
            break
    return output


def _selection_tool(
    handles: list[str], *, max_items: int = SELECTION_MAX_ITEMS
) -> list[dict[str, Any]]:
    if max_items < 1:
        raise ValueError("selector max_items must be positive")
    return [
        {
            "type": "function",
            "function": {
                "name": SELECTION_TOOL,
                "description": "Select opaque evidence handles for the semantic subgraph.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "handles": {
                            "type": "array",
                            "items": {"type": "string", "enum": handles},
                            "minItems": 1,
                            "maxItems": max_items,
                        }
                    },
                    "required": ["handles"],
                    "additionalProperties": False,
                },
            },
        }
    ]


def _usage(response: dict[str, Any]) -> dict[str, Any]:
    usage = response.get("usage", {})
    return {
        "prompt_tokens": usage.get("prompt_tokens"),
        "completion_tokens": usage.get("completion_tokens"),
        "total_tokens": usage.get("total_tokens"),
    }


def _usage_total(*usage_rows: dict[str, Any] | None) -> tuple[int, int]:
    """Return known tokens and the number of calls without returned usage."""

    known = 0
    missing = 0
    for usage in usage_rows:
        value = usage.get("total_tokens") if isinstance(usage, dict) else None
        if isinstance(value, int) and value >= 0:
            known += value
        else:
            missing += 1
    return known, missing


def _attach_generation_failure(
    error: Exception,
    *,
    model_calls: int,
    usage_rows: list[dict[str, Any] | None],
    started: float,
) -> None:
    known_tokens, missing = _usage_total(*usage_rows)
    error.audit = {  # type: ignore[attr-defined]
        "model_calls": model_calls,
        "total_model_calls": model_calls,
        "known_total_tokens": known_tokens,
        "token_audits_missing": missing,
        "total_tokens": known_tokens if missing == 0 else None,
    }
    error.latency_seconds = round(  # type: ignore[attr-defined]
        time.perf_counter() - started, 6
    )


def _generation_cost_audit(
    usage_rows: list[dict[str, Any] | None],
) -> dict[str, Any]:
    known_tokens, missing = _usage_total(*usage_rows)
    return {
        "model_calls": len(usage_rows),
        "total_model_calls": len(usage_rows),
        "known_total_tokens": known_tokens,
        "token_audits_missing": missing,
        "total_tokens": known_tokens if missing == 0 else None,
    }


def _merge_generation_retry_cost(
    row: dict[str, Any], prior: dict[str, Any] | None
) -> dict[str, Any]:
    retry_history = [
        *(
            prior.get("retry_history", [])
            if isinstance(prior, dict)
            else []
        )
    ]
    if isinstance(prior, dict):
        retry_history.append(
            {
                "status": "error",
                "error_type": prior.get("error_type"),
                "error": prior.get("error"),
                "audit": prior.get("audit", {}),
                "latency_seconds": prior.get("latency_seconds", 0.0),
            }
        )
    if retry_history:
        row["retry_history"] = retry_history
    attempts = [*retry_history, row]
    audit = dict(row.get("audit", {}))
    total_model_calls = sum(
        int(item.get("audit", {}).get("model_calls") or 0)
        for item in attempts
    )
    token_audits_missing = sum(
        int(item.get("audit", {}).get("token_audits_missing") or 0)
        for item in attempts
    )
    known_total_tokens = sum(
        int(item.get("audit", {}).get("known_total_tokens") or 0)
        for item in attempts
    )
    audit.update(
        {
            "total_model_calls": total_model_calls,
            "known_total_tokens": known_total_tokens,
            "token_audits_missing": token_audits_missing,
        }
    )
    if token_audits_missing == 0:
        audit["total_tokens"] = known_total_tokens
    else:
        audit["total_tokens"] = None
    row["audit"] = audit
    row["total_latency_seconds"] = round(
        sum(float(item.get("latency_seconds") or 0.0) for item in attempts),
        6,
    )
    return row


def _select(
    client: VLLMClient,
    question: str,
    candidates: list[CatalogDocument],
    *,
    system_prompt: str = SELECTOR_SYSTEM,
    max_items: int = SELECTION_MAX_ITEMS,
) -> tuple[list[str], dict[str, Any], str]:
    if max_items < 1:
        raise ValueError("selector max_items must be positive")
    if not candidates:
        raise ValueError("selector candidate manifest is empty")
    candidate_ids = [row.candidate_id for row in candidates]
    if len(candidate_ids) != len(set(candidate_ids)):
        raise ValueError("selector candidate manifest contains duplicate IDs")
    handle_to_id = {f"S{index:04d}": row.candidate_id for index, row in enumerate(candidates)}
    manifest = "\n".join(
        f"{handle}: {row.kind} | {row.name} | {row.text[:900]}"
        for handle, row in zip(handle_to_id, candidates, strict=True)
    )
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"Question:\n{question}\n\nCandidate manifest:\n{manifest}"},
    ]
    tools = _selection_tool(list(handle_to_id), max_items=max_items)
    # This request exposes exactly one function. Use the portable forced-tool
    # form so vLLM 0.25.1 reports ``finish_reason=tool_calls`` instead of the
    # non-standard ``stop`` produced for a named-function tool choice.
    tool_choice = "required"
    prompt_hash = _canonical_hash(
        {
            "messages": messages,
            "tools": tools,
            "tool_choice": tool_choice,
        }
    )
    started = time.perf_counter()
    response: dict[str, Any] | None = None
    try:
        response = client.chat_tools(
            messages,
            tools,
            tool_choice=tool_choice,
        )
        choices = response.get("choices")
        if not isinstance(choices, list) or len(choices) != 1:
            raise ValueError("selector response must contain exactly one choice")
        choice = choices[0]
        if not isinstance(choice, dict):
            raise ValueError("selector choice must be an object")
        message = choice.get("message")
        if not isinstance(message, dict):
            raise ValueError("selector response message must be an object")
        calls = message.get("tool_calls")
        if not isinstance(calls, list) or len(calls) != 1:
            raise ValueError("selector must return exactly one tool call")
        call = calls[0]
        if not isinstance(call, dict):
            raise ValueError("selector tool call must be an object")
        function = call.get("function")
        if (
            not isinstance(function, dict)
            or function.get("name") != SELECTION_TOOL
        ):
            raise ValueError("selector returned an unexpected tool name")
        arguments = function.get("arguments", {})
        if isinstance(arguments, str):
            try:
                arguments = json.loads(arguments)
            except json.JSONDecodeError as error:
                raise ValueError(
                    "selector tool arguments are not valid JSON"
                ) from error
        if not isinstance(arguments, dict):
            raise ValueError("selector tool arguments must be an object")
        if set(arguments) != {"handles"}:
            raise ValueError("selector tool arguments must contain only handles")
        handles = arguments["handles"]
        if not isinstance(handles, list):
            raise ValueError("selector handles must be an array")
        if not 1 <= len(handles) <= max_items:
            raise ValueError(
                f"selector handles must contain 1..{max_items} items"
            )
        invalid = [
            handle
            for handle in handles
            if not isinstance(handle, str) or handle not in handle_to_id
        ]
        if invalid:
            raise ValueError(
                f"selector returned {len(invalid)} handle(s) outside the candidate enum"
            )
    except Exception as error:
        _attach_generation_failure(
            error,
            model_calls=1,
            usage_rows=[_usage(response) if response is not None else None],
            started=started,
        )
        raise
    selected: list[str] = []
    for handle in handles:
        candidate_id = handle_to_id[handle]
        if candidate_id not in selected:
            selected.append(candidate_id)
    return selected, _usage(response), prompt_hash


def _serialize_context(documents: list[CatalogDocument], budget_tokens: int = 24576) -> str:
    budget_chars = budget_tokens * 4
    chunks = []
    used = 0
    for document in documents:
        chunk = document.compact_text()
        remaining = budget_chars - used
        if remaining <= 0:
            break
        if len(chunk) > remaining:
            chunks.append(chunk[:remaining])
            used += remaining
            break
        chunks.append(chunk)
        used += len(chunk)
    return "\n\n".join(chunks)


def _build_embeddings(
    documents: list[CatalogDocument],
    questions: list[dict[str, Any]],
    model_path: Path,
    cache: Path,
    device: str = "cpu",
) -> tuple[dict[str, np.ndarray], dict[str, np.ndarray], str]:
    doc_ids = [row.candidate_id for row in documents]
    question_ids = [str(row["example_id"]) for row in questions]
    model_inventory_sha256 = _embedding_model_inventory_sha256(
        str(model_path.resolve())
    )
    fingerprint = _canonical_hash(
        {
            "documents": [(row.candidate_id, row.retrieval_text()) for row in documents],
            "questions": [(row["example_id"], row["question"]) for row in questions],
            "model": str(model_path.resolve()),
            "model_inventory_sha256": model_inventory_sha256,
        }
    )
    if cache.is_file():
        payload = np.load(cache, allow_pickle=False)
        if str(payload["fingerprint"].item()) == fingerprint:
            doc_vectors = payload["doc_vectors"]
            question_vectors = payload["question_vectors"]
            return (
                dict(zip(doc_ids, doc_vectors, strict=True)),
                dict(zip(question_ids, question_vectors, strict=True)),
                fingerprint,
            )
    from FlagEmbedding import BGEM3FlagModel

    model = BGEM3FlagModel(
        str(model_path),
        use_fp16=device != "cpu",
        devices=device,
        trust_remote_code=False,
    )
    doc_vectors = np.asarray(
        model.encode(
            [row.retrieval_text() for row in documents], batch_size=16, max_length=512
        )["dense_vecs"]
    )
    question_vectors = np.asarray(
        model.encode_queries(
            [str(row["question"]) for row in questions], batch_size=16, max_length=512
        )["dense_vecs"]
    )
    cache.parent.mkdir(parents=True, exist_ok=True)
    np.savez_compressed(
        cache,
        fingerprint=np.asarray(fingerprint),
        doc_vectors=doc_vectors,
        question_vectors=question_vectors,
    )
    return (
        dict(zip(doc_ids, doc_vectors, strict=True)),
        dict(zip(question_ids, question_vectors, strict=True)),
        fingerprint,
    )


def _validate_sql(sql: str | None, category: str) -> dict[str, Any]:
    if not sql:
        return {"valid": False, "reason": "missing_sql"}
    try:
        import sqlglot

        statements = sqlglot.parse(sql, read="postgres")
        if len(statements) != 1:
            return {"valid": False, "reason": "multiple_statements"}
        if category == "Query" and statements[0].key not in {"select", "union", "intersect", "except"}:
            return {"valid": False, "reason": "query_track_non_readonly", "expression": statements[0].key}
        return {"valid": True, "expression": statements[0].key}
    except Exception as error:
        return {"valid": False, "reason": type(error).__name__, "detail": str(error)[:500]}


def _normalize_decision(
    value: Any, sql: str | None, clarification: Any
) -> str:
    decision = str(value or "").strip().lower()
    if decision in {"answer", "clarify", "abstain"}:
        return decision
    if sql:
        return "answer"
    if clarification:
        return "clarify"
    return "abstain"


def _run_one(
    row: dict[str, Any],
    category: str,
    client: VLLMClient,
    docs_by_database: dict[str, list[CatalogDocument]],
    all_documents: dict[str, CatalogDocument],
    vector_by_id: dict[str, np.ndarray],
    query_vector: np.ndarray,
) -> dict[str, Any]:
    started = time.perf_counter()
    database_id = str(row["database_id"])
    question = str(row["question"])
    documents = docs_by_database[database_id]
    lexical = _lexical_rank(question, documents)
    dense = _dense_rank(query_vector, documents, vector_by_id)
    ranking = _rrf(dense, lexical)
    candidates = _candidate_pool(ranking, all_documents)
    selected, selector_usage, selector_hash = _select(client, question, candidates)
    sql_call_started = False
    sql_usage: dict[str, Any] | None = None
    try:
        closed = evidence_closure(selected, candidates, all_documents)
        context = _serialize_context(closed)
        user_payload = {
            "dataset": row["dataset_id"],
            "database": database_id,
            "category": category,
            "question": question,
            "semantic_subgraph": context,
        }
        sql_call_started = True
        prediction, sql_usage = client.chat_json_with_metadata(
            SQL_SYSTEM, json.dumps(user_payload, ensure_ascii=False)
        )
        sql = prediction.get("sql")
        sql = str(sql).strip() if sql else None
        decision = _normalize_decision(
            prediction.get("decision"), sql, prediction.get("clarification")
        )
        validation = _validate_sql(sql, category)
    except Exception as error:
        usage_rows: list[dict[str, Any] | None] = [selector_usage]
        if sql_call_started:
            usage_rows.append(sql_usage)
        _attach_generation_failure(
            error,
            model_calls=len(usage_rows),
            usage_rows=usage_rows,
            started=started,
        )
        raise
    generation_cost = _generation_cost_audit([selector_usage, sql_usage])
    return {
        "example_id": row["example_id"],
        "dataset_id": row["dataset_id"],
        "upstream_split": row["upstream_split"],
        "database_id": database_id,
        "method_id": METHOD_ID,
        "decision": decision,
        "sql": sql,
        "clarification": prediction.get("clarification"),
        "answer": prediction.get("answer"),
        "validation": validation,
        "context": {
            "candidate_count": len(candidates),
            "selected_ids": selected,
            "closed_ids": [document.candidate_id for document in closed],
            "serialized_chars": len(context),
            "serialized_token_estimate": (len(context) + 3) // 4,
        },
        "audit": {
            **generation_cost,
            "selector_usage": selector_usage,
            "sql_usage": sql_usage,
            "prompt_sha256": {
                "selector": selector_hash,
                "sql_agent": _canonical_hash({"system": SQL_SYSTEM, "user": user_payload}),
            },
        },
        "latency_seconds": round(time.perf_counter() - started, 6),
    }


def _write_atomic(path: Path, rows: list[dict[str, Any]]) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    with temporary.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(json.dumps(row, ensure_ascii=False) + "\n")
    temporary.replace(path)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-root", type=Path, required=True)
    parser.add_argument("--online-manifest", type=Path, required=True)
    parser.add_argument("--source-data", type=Path, required=True)
    parser.add_argument("--embedding-model", type=Path, required=True)
    parser.add_argument("--embedding-cache", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--base-url", default="http://127.0.0.1:18000/v1")
    parser.add_argument("--model", default="qwen3.6-35b")
    parser.add_argument("--api-key-env", default="SCHEMARECOVERY_LLM_API_KEY")
    parser.add_argument("--concurrency", type=int, default=8)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--build-embeddings-only", action="store_true")
    args = parser.parse_args()
    if args.concurrency <= 4:
        raise ValueError("the frozen 4090 run requires client concurrency > 4")
    full_rows = _load_jsonl(args.online_manifest)
    source_by_id = {str(row["instance_id"]): row for row in _load_jsonl(args.source_data)}
    rows = full_rows if args.limit is None else full_rows[: args.limit]
    _validate_embedding_model_for_run(args.embedding_model, args.output)
    documents = load_catalog(args.data_root)
    all_documents = {row.candidate_id: row for row in documents}
    docs_by_database: dict[str, list[CatalogDocument]] = {}
    for document in documents:
        docs_by_database.setdefault(document.database_id, []).append(document)
    vector_by_id, query_vectors, embedding_hash = _build_embeddings(
        documents, full_rows, args.embedding_model, args.embedding_cache
    )
    if args.build_embeddings_only:
        print(
            json.dumps(
                {
                    "documents": len(vector_by_id),
                    "questions": len(query_vectors),
                    "embedding_input_sha256": embedding_hash,
                    "cache": str(args.embedding_cache),
                },
                ensure_ascii=False,
            )
        )
        return
    api_key = os.environ.get(args.api_key_env)
    if not api_key:
        raise ValueError(f"API key environment variable is unset: {args.api_key_env}")
    client = VLLMClient(
        {
            "base_url": args.base_url,
            "api_key": api_key,
            "model": args.model,
            "temperature": 0.0,
            "top_p": 1.0,
            "max_output_tokens": 2048,
        }
    )
    if not client.healthy():
        raise RuntimeError(f"vLLM is unavailable at {client.base_url}")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    completed = _load_jsonl(args.output) if args.resume and args.output.is_file() else []
    _validate_resume_rows(completed)
    prior_errors = {
        str(row["example_id"]): row
        for row in completed
        if row.get("status") == "error"
    }
    by_id = {
        str(row["example_id"]): row
        for row in completed
        if row.get("status") != "error"
    }
    pending = [row for row in rows if str(row["example_id"]) not in by_id]
    lock = threading.Lock()

    def run(row: dict[str, Any]) -> dict[str, Any]:
        example_id = str(row["example_id"])
        started = time.perf_counter()
        try:
            source = source_by_id[example_id]
            return _run_one(
                row,
                str(source.get("category", "Query")),
                client,
                docs_by_database,
                all_documents,
                vector_by_id,
                query_vectors[example_id],
            )
        except Exception as error:
            audit = getattr(
                error,
                "audit",
                {
                    "model_calls": 0,
                    "total_model_calls": 0,
                    "known_total_tokens": 0,
                    "token_audits_missing": 0,
                    "total_tokens": 0,
                },
            )
            return {
                "example_id": example_id,
                "dataset_id": row["dataset_id"],
                "database_id": row["database_id"],
                "method_id": METHOD_ID,
                "status": "error",
                "error_type": type(error).__name__,
                "error": str(error)[:1000],
                "audit": audit,
                "latency_seconds": float(
                    getattr(
                        error,
                        "latency_seconds",
                        time.perf_counter() - started,
                    )
                ),
            }

    with ThreadPoolExecutor(max_workers=args.concurrency) as executor:
        futures = {executor.submit(run, row): str(row["example_id"]) for row in pending}
        for completed_count, future in enumerate(as_completed(futures), start=1):
            row = future.result()
            example_id = futures[future]
            row = _merge_generation_retry_cost(
                row, prior_errors.get(example_id)
            )
            with lock:
                by_id[example_id] = row
                with args.output.open("a", encoding="utf-8") as handle:
                    handle.write(json.dumps(row, ensure_ascii=False) + "\n")
            print(
                f"[{completed_count}/{len(pending)}] {example_id} "
                f"status={'error' if row.get('status') == 'error' else 'ok'}",
                flush=True,
            )
    ordered = [by_id[str(row["example_id"])] for row in rows]
    _write_atomic(args.output, ordered)
    summary = {
        "method_id": METHOD_ID,
        "rows": len(ordered),
        "errors": sum(row.get("status") == "error" for row in ordered),
        "valid_sql": sum(row.get("validation", {}).get("valid") is True for row in ordered),
        "decisions": {
            decision: sum(row.get("decision") == decision for row in ordered)
            for decision in ("answer", "clarify", "abstain")
        },
        "protocol": {
            "client_concurrency": args.concurrency,
            "gold_access": "none; online manifest only",
            "model": args.model,
            "embedding_model": str(args.embedding_model.resolve()),
            "embedding_input_sha256": embedding_hash,
            "max_context_tokens": 24576,
            "model_calls_per_successful_row": 2,
        },
    }
    args.output.with_suffix(".summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
