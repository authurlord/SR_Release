#!/usr/bin/env python3
"""Run schema recovery + operational ontology on a frozen BEAVER v3 view."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from hashlib import sha256
import json
import os
from pathlib import Path
from threading import Lock
from typing import Any

import numpy as np

from finsemguard.agent.llm import VLLMClient
from finsemguard.config import load_config
from finsemguard.e2e.beaver import BeaverMySQLAgentTools, build_beaver_catalog_documents
from finsemguard.e2e.graph_evo_main import (
    run_graph_evo_semantic_program_main,
)
from finsemguard.e2e.livesqlbench import CatalogDocument
from finsemguard.e2e.livesqlbench_runner import _load_jsonl, _write_atomic
from finsemguard.e2e.method_identity import (
    EVOLUTION_AWARE_RELATIONAL_PROGRAM_COMPILER,
    GRAPH_EVO_SEMANTIC_PROGRAM_MAIN,
)
from finsemguard.e2e.operational_ontology import OperationalOntology
from finsemguard.e2e.react_text2sql import (
    METHOD_IDS,
    SchemaSearchIndex,
    _minimal_join_tree_role_phrases,
    _query_role_phrases,
    build_recovery_documents,
    run_react_text2sql,
)
from finsemguard.retrieval.reranker import VLLMRerankerClient
from run_bird_react_recovery import BGEEncoder


SUPPORTED_CONDITIONS = (
    "ontology_react",
    "program_graph_react",
    "minimal_join_tree_react",
    "opaque_react",
    "chess_react",
    "autolink_react",
    GRAPH_EVO_SEMANTIC_PROGRAM_MAIN,
)
RELATIONAL_PROGRAM_CONDITIONS = {
    "program_graph_react",
    "minimal_join_tree_react",
    GRAPH_EVO_SEMANTIC_PROGRAM_MAIN,
}


def _declared_method_id(condition: str, *, anchored: bool) -> str:
    if condition == GRAPH_EVO_SEMANTIC_PROGRAM_MAIN:
        return GRAPH_EVO_SEMANTIC_PROGRAM_MAIN
    if anchored:
        return EVOLUTION_AWARE_RELATIONAL_PROGRAM_COMPILER
    return METHOD_IDS[condition]


def _write_json(path: Path, value: Any) -> None:
    content = json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if path.exists():
        if path.read_text(encoding="utf-8") != content:
            raise FileExistsError(f"refusing to overwrite different artifact: {path}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(content, encoding="utf-8")
    temporary.replace(path)


def _write_latest_json(path: Path, value: Any) -> None:
    """Atomically replace a mutable progress summary, never a prediction."""

    content = json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(content, encoding="utf-8")
    temporary.replace(path)


def _strip_lean_metadata(value: Any) -> Any:
    """Remove audit/checksum metadata while retaining method outputs and traces."""

    if isinstance(value, dict):
        return {
            key: _strip_lean_metadata(item)
            for key, item in value.items()
            if "audit" not in key.casefold()
            and "sha256" not in key.casefold()
            and "hash" not in key.casefold()
            and "fingerprint" not in key.casefold()
        }
    if isinstance(value, list):
        return [_strip_lean_metadata(item) for item in value]
    return value


def _deduplicated_encoder(
    *,
    documents: list[CatalogDocument],
    model_path: Path,
    cache_path: Path,
    batch_size: int,
    seed_cache_paths: list[Path] | None = None,
) -> tuple[BGEEncoder, dict[str, np.ndarray], int]:
    representatives: list[CatalogDocument] = []
    representative_by_text: dict[str, str] = {}
    representative_by_candidate: dict[str, str] = {}
    for document in documents:
        text = document.retrieval_text()
        representative_id = representative_by_text.get(text)
        if representative_id is None:
            representative_id = f"embedding_text::{sha256(text.encode()).hexdigest()}"
            representative_by_text[text] = representative_id
            representatives.append(
                CatalogDocument(
                    candidate_id=representative_id,
                    database_id="embedding-deduplicated",
                    kind=document.kind,
                    table=None,
                    name=document.name,
                    text=document.text,
                )
            )
        representative_by_candidate[document.candidate_id] = representative_id
    encoder = BGEEncoder(
        model_path=model_path,
        documents=representatives,
        cache_path=cache_path,
        batch_size=batch_size,
        seed_cache_paths=seed_cache_paths,
    )
    vectors = {
        candidate_id: encoder.vectors[representative_id]
        for candidate_id, representative_id in representative_by_candidate.items()
    }
    return encoder, vectors, len(representatives)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--online", type=Path, required=True)
    parser.add_argument("--table-inputs", type=Path, required=True)
    parser.add_argument("--recovery", type=Path, required=True)
    parser.add_argument("--knowledge", type=Path, required=True)
    parser.add_argument("--embedding-model", type=Path, required=True)
    parser.add_argument("--embedding-cache", type=Path, required=True)
    parser.add_argument(
        "--query-cache",
        type=Path,
        help="Persistent BGE vectors for the frozen question and role-phrase set.",
    )
    parser.add_argument("--embedding-seed-cache", type=Path, action="append", default=[])
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument(
        "--llm-base-url",
        action="append",
        default=[],
        help=(
            "OpenAI-compatible generation endpoint. Repeat to distribute rows "
            "deterministically across identical model servers."
        ),
    )
    parser.add_argument(
        "--audit-log",
        type=Path,
        help="Override the config audit-log path for this immutable run.",
    )
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument(
        "--lean",
        action="store_true",
        help=(
            "Write only the prediction and compact run metadata: disable API "
            "audit logging and omit artifact checksums from summaries."
        ),
    )
    parser.add_argument("--retrieval-output-root", type=Path)
    parser.add_argument("--concurrency", type=int, default=4)
    parser.add_argument("--embedding-batch-size", type=int, default=32)
    parser.add_argument("--reranker-base-url")
    parser.add_argument(
        "--reranker-model", default="bge-reranker-v2-m3"
    )
    parser.add_argument("--reranker-top-k", type=int, default=30)
    parser.add_argument("--reranker-timeout-seconds", type=float, default=120.0)
    parser.add_argument("--max-turns", type=int, default=4)
    parser.add_argument("--max-actions", type=int, default=8)
    parser.add_argument("--max-sql-executions", type=int, default=3)
    parser.add_argument("--initial-schema-top-k", type=int, default=20)
    parser.add_argument("--mysql-host", default="127.0.0.1")
    parser.add_argument("--mysql-port", type=int, default=3306)
    parser.add_argument("--mysql-user", default="root")
    parser.add_argument("--mysql-password-env", default="BEAVER_MYSQL_PASSWORD")
    parser.add_argument("--example-id", action="append", default=[])
    parser.add_argument("--subset-size", type=int)
    parser.add_argument("--seed-predictions", type=Path, action="append", default=[])
    parser.add_argument(
        "--anchor-predictions",
        type=Path,
        help=(
            "Frozen Persistent-Recovery SQL used as the primary evidence draft."
        ),
    )
    parser.add_argument(
        "--auxiliary-raw-predictions",
        type=Path,
        help=(
            "Frozen Direct Raw-Evidence SQL exposed only as an unscored auxiliary "
            "draft to the unified Graph+Evo main."
        ),
    )
    parser.add_argument(
        "--condition", action="append", choices=SUPPORTED_CONDITIONS
    )
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()
    if args.concurrency < 1:
        raise ValueError("concurrency must be positive")
    conditions = tuple(args.condition or ("ontology_react",))
    if len(set(conditions)) != len(conditions):
        raise ValueError("duplicate condition")
    if args.reranker_base_url is not None and conditions != (
        GRAPH_EVO_SEMANTIC_PROGRAM_MAIN,
    ):
        raise ValueError("the cross-encoder reranker is reserved for the unified main")
    if args.reranker_base_url is not None and not 1 <= args.reranker_top_k <= 100:
        raise ValueError("reranker top-k must be between 1 and 100")
    if args.anchor_predictions is not None and any(
        condition not in RELATIONAL_PROGRAM_CONDITIONS for condition in conditions
    ):
        raise ValueError(
            "anchor predictions require a relational-program condition"
        )
    if (
        GRAPH_EVO_SEMANTIC_PROGRAM_MAIN in conditions
        and args.anchor_predictions is None
    ):
        raise ValueError("the unified Graph+Evo main requires --anchor-predictions")
    if args.auxiliary_raw_predictions is not None and (
        GRAPH_EVO_SEMANTIC_PROGRAM_MAIN not in conditions
        or args.anchor_predictions is None
    ):
        raise ValueError(
            "auxiliary raw predictions require the anchored unified Graph+Evo main"
        )
    password = os.environ.get(args.mysql_password_env)
    if password is None:
        raise RuntimeError(f"missing MySQL password environment variable: {args.mysql_password_env}")
    connection_config = {
        "host": args.mysql_host,
        "port": args.mysql_port,
        "user": args.mysql_user,
        "password": password,
    }

    all_rows = _load_jsonl(args.online)
    if {str(row["dataset_id"]) for row in all_rows} != {"beaver_v3"}:
        raise ValueError("online manifest must contain only BEAVER v3 rows")
    if args.example_id and args.subset_size is not None:
        raise ValueError("--example-id and --subset-size are mutually exclusive")
    if args.subset_size is not None and args.subset_size < 1:
        raise ValueError("--subset-size must be positive")
    if args.example_id:
        requested = set(args.example_id)
        rows = [row for row in all_rows if str(row["example_id"]) in requested]
        if {str(row["example_id"]) for row in rows} != requested:
            raise ValueError("one or more requested example IDs are absent")
    elif args.subset_size is not None:
        rows = all_rows[: args.subset_size]
    else:
        rows = all_rows
    anchor_by_id: dict[str, str] = {}
    if args.anchor_predictions is not None:
        anchor_rows = _load_jsonl(args.anchor_predictions)
        for anchor in anchor_rows:
            example_id = str(anchor.get("example_id") or "")
            sql = str(anchor.get("sql") or "").strip()
            if not example_id or not sql or example_id in anchor_by_id:
                raise ValueError("anchor predictions contain an invalid or duplicate row")
            anchor_by_id[example_id] = sql
        missing = sorted(
            str(row["example_id"])
            for row in rows
            if str(row["example_id"]) not in anchor_by_id
        )
        if missing:
            raise ValueError(f"anchor predictions miss {len(missing)} selected rows")
    auxiliary_raw_by_id: dict[str, str] = {}
    if args.auxiliary_raw_predictions is not None:
        auxiliary_rows = _load_jsonl(args.auxiliary_raw_predictions)
        for auxiliary in auxiliary_rows:
            example_id = str(auxiliary.get("example_id") or "")
            sql = str(auxiliary.get("sql") or "").strip()
            if not example_id or not sql or example_id in auxiliary_raw_by_id:
                raise ValueError(
                    "auxiliary raw predictions contain an invalid or duplicate row"
                )
            auxiliary_raw_by_id[example_id] = sql
        missing = sorted(
            str(row["example_id"])
            for row in rows
            if str(row["example_id"]) not in auxiliary_raw_by_id
        )
        if missing:
            raise ValueError(
                f"auxiliary raw predictions miss {len(missing)} selected rows"
            )
    forbidden = {
        "sql",
        "tables",
        "join_keys",
        "column_mapping",
        "domain_knowledge",
        "sub_questions",
        "sub_sqls",
        "gold",
    }
    contamination = sorted(
        (str(row["example_id"]), sorted(forbidden & set(row)))
        for row in all_rows
        if forbidden & set(row)
    )
    if contamination:
        raise ValueError(f"online view contains evaluator fields: {contamination[:3]}")

    table_inputs = _load_jsonl(args.table_inputs)
    recovery_rows = _load_jsonl(args.recovery)
    knowledge_rows = _load_jsonl(args.knowledge)
    if len(recovery_rows) != len(table_inputs) or any(
        "prediction" not in row for row in recovery_rows
    ):
        raise ValueError("table recovery is incomplete")
    raw_documents = build_beaver_catalog_documents(table_inputs)
    recovery_documents = build_recovery_documents(table_inputs, recovery_rows)
    ontology = OperationalOntology.from_recovery_inputs(
        table_inputs,
        knowledge_rows,
        sql_dialect="mysql",
    )
    full_documents = ontology.augment_documents(
        [*raw_documents, *recovery_documents]
    )
    encoder, vectors, unique_embedding_texts = _deduplicated_encoder(
        documents=full_documents,
        model_path=args.embedding_model,
        cache_path=args.embedding_cache,
        batch_size=args.embedding_batch_size,
        seed_cache_paths=args.embedding_seed_cache,
    )
    question_texts = list(dict.fromkeys(str(row["question"]) for row in all_rows))
    role_phrase_texts: list[str] = []
    if RELATIONAL_PROGRAM_CONDITIONS & set(conditions):
        role_phrase_texts = list(
            dict.fromkeys(
                phrase
                for row in all_rows
                for condition in conditions
                if condition in RELATIONAL_PROGRAM_CONDITIONS
                for phrase in (
                    _minimal_join_tree_role_phrases(str(row["question"]))
                    if condition
                    in {"minimal_join_tree_react", GRAPH_EVO_SEMANTIC_PROGRAM_MAIN}
                    else _query_role_phrases(str(row["question"]))
                )
            )
        )
    all_query_texts = list(dict.fromkeys([*question_texts, *role_phrase_texts]))
    query_fingerprint = sha256(
        json.dumps(
            {
                "embedding_fingerprint": encoder.fingerprint,
                "texts": all_query_texts,
            },
            ensure_ascii=False,
            sort_keys=True,
            separators=(",", ":"),
        ).encode()
    ).hexdigest()
    query_matrix: np.ndarray | None = None
    if args.query_cache is not None and args.query_cache.is_file():
        cached_queries = np.load(args.query_cache, allow_pickle=False)
        if (
            str(cached_queries["fingerprint"].item()) != query_fingerprint
            or cached_queries["texts"].tolist() != all_query_texts
        ):
            raise FileExistsError(
                f"refusing incompatible BGE query cache: {args.query_cache}"
            )
        query_matrix = np.asarray(cached_queries["vectors"], dtype=np.float32)
    if query_matrix is None:
        query_matrix = encoder.encode_queries(all_query_texts)
        if args.query_cache is not None:
            args.query_cache.parent.mkdir(parents=True, exist_ok=True)
            temporary = args.query_cache.with_suffix(args.query_cache.suffix + ".tmp")
            with temporary.open("wb") as handle:
                np.savez_compressed(
                    handle,
                    fingerprint=np.asarray(query_fingerprint),
                    texts=np.asarray(all_query_texts),
                    vectors=query_matrix,
                )
            temporary.replace(args.query_cache)
    encoder.query_cache.update(
        dict(zip(all_query_texts, query_matrix, strict=True))
    )
    query_vectors = {
        text: encoder.query_cache[text] for text in question_texts
    }
    print(
        f"[bge-query-cache] questions={len(question_texts)} "
        f"role_phrases={len(role_phrase_texts)} persistent={args.query_cache is not None}",
        flush=True,
    )

    def encode_query(text: str) -> np.ndarray:
        if text in query_vectors:
            return query_vectors[text]
        return encoder.encode_query(text)
    reranker: VLLMRerankerClient | None = None
    if args.reranker_base_url is not None:
        reranker = VLLMRerankerClient(
            base_url=args.reranker_base_url,
            model=args.reranker_model,
            timeout_seconds=args.reranker_timeout_seconds,
        )
        if not reranker.healthy():
            raise RuntimeError("required exact main-method reranker is unavailable")
    ontology_edges: dict[str, list[dict[str, Any]]] = {}
    for edge in ontology.edges:
        ontology_edges.setdefault(edge.context, []).append(edge.as_dict())
    full_index = SchemaSearchIndex(
        documents=full_documents,
        raw_documents=raw_documents,
        vectors=vectors,
        encode_query=encode_query,
        encode_queries=encoder.encode_queries,
        ontology_edges_by_database=ontology_edges,
        bindings_by_document={
            key: list(values) for key, values in ontology.document_bindings.items()
        },
    )
    program_graph_index = SchemaSearchIndex(
        documents=full_documents,
        raw_documents=raw_documents,
        vectors=vectors,
        encode_query=encode_query,
        encode_queries=encoder.encode_queries,
        ontology_edges_by_database=ontology_edges,
        bindings_by_document={
            key: list(values) for key, values in ontology.document_bindings.items()
        },
        program_graph=True,
    )
    minimal_join_tree_index = SchemaSearchIndex(
        documents=full_documents,
        raw_documents=raw_documents,
        vectors=vectors,
        encode_query=encode_query,
        encode_queries=encoder.encode_queries,
        ontology_edges_by_database=ontology_edges,
        bindings_by_document={
            key: list(values) for key, values in ontology.document_bindings.items()
        },
        minimal_join_tree=True,
        rerank_documents=reranker.score if reranker is not None else None,
        rerank_top_k=args.reranker_top_k,
    )
    raw_ids = {row.candidate_id for row in raw_documents}
    raw_index = SchemaSearchIndex(
        documents=raw_documents,
        raw_documents=raw_documents,
        vectors={key: value for key, value in vectors.items() if key in raw_ids},
        encode_query=encode_query,
    )
    raw_tables = [row for row in raw_documents if row.kind == "table"]
    table_index = SchemaSearchIndex(
        documents=raw_tables,
        raw_documents=raw_tables,
        vectors={row.candidate_id: vectors[row.candidate_id] for row in raw_tables},
        encode_query=encode_query,
    )
    indices = {
        "ontology_react": full_index,
        "program_graph_react": program_graph_index,
        "minimal_join_tree_react": minimal_join_tree_index,
        "opaque_react": raw_index,
        "chess_react": raw_index,
        "autolink_react": raw_index,
        GRAPH_EVO_SEMANTIC_PROGRAM_MAIN: minimal_join_tree_index,
    }

    if args.retrieval_output_root is not None:
        by_database: dict[str, dict[str, list[str]]] = {}
        for row in all_rows:
            database = str(row["database_id"])
            result = table_index.search(database, str(row["question"]), 15)
            tables = list(
                dict.fromkeys(
                    str(value["physical_table"])
                    for value in result["results"]
                    if value.get("physical_table")
                )
            )
            by_database.setdefault(database, {})[str(row["example_id"])] = tables[:15]
        for database, value in by_database.items():
            _write_json(args.retrieval_output_root / f"retrieved_tables_{database}.json", value)

    llm_config = dict(load_config(args.config)["llm"])
    if args.lean:
        llm_config.pop("audit_log_path", None)
    endpoint_urls = list(
        dict.fromkeys(
            str(value).rstrip("/")
            for value in (args.llm_base_url or [llm_config["base_url"]])
        )
    )
    clients: list[VLLMClient] = []
    for endpoint_index, endpoint_url in enumerate(endpoint_urls):
        endpoint_config = {**llm_config, "base_url": endpoint_url}
        if args.audit_log is not None:
            audit_path = args.audit_log
            if len(endpoint_urls) > 1:
                audit_path = audit_path.with_name(
                    f"{audit_path.stem}.endpoint{endpoint_index}{audit_path.suffix}"
                )
            endpoint_config["audit_log_path"] = str(audit_path)
        endpoint_client = VLLMClient(endpoint_config)
        if not endpoint_client.healthy():
            raise RuntimeError(
                f"required exact LLM is unavailable at {endpoint_client.base_url}"
            )
        clients.append(endpoint_client)
    client = clients[0]
    args.output_root.mkdir(parents=True, exist_ok=True)
    paths = {
        condition: args.output_root / f"{condition}.jsonl"
        for condition in conditions
    }
    if not args.resume and any(path.exists() for path in paths.values()):
        raise FileExistsError("output exists; use --resume or a new output root")
    completed: dict[str, dict[str, dict[str, Any]]] = {}
    for condition, path in paths.items():
        prior = _load_jsonl(path) if args.resume and path.is_file() else []
        completed[condition] = {
            str(row["example_id"]): (
                _strip_lean_metadata(row) if args.lean else row
            )
            for row in prior
            if row.get("status") != "error"
        }
    eligible_ids = {str(row["example_id"]) for row in rows}
    for seed_path in args.seed_predictions:
        for seed in _load_jsonl(seed_path):
            example_id = str(seed["example_id"])
            if example_id not in eligible_ids or seed.get("status") == "error":
                continue
            condition = str(seed.get("asset_condition") or "")
            if condition not in completed or seed.get("method_id") != _declared_method_id(
                condition,
                anchored=args.anchor_predictions is not None,
            ):
                raise ValueError(
                    f"seed prediction uses a different method for {example_id}: "
                    f"{seed.get('method_id')}"
                )
            completed[condition].setdefault(example_id, seed)
    for condition, path in paths.items():
        if completed[condition] and not path.exists():
            _write_atomic(
                path,
                [
                    completed[condition][str(row["example_id"])]
                    for row in rows
                    if str(row["example_id"]) in completed[condition]
                ],
            )
    lock = Lock()

    def run(row: dict[str, Any]) -> dict[str, dict[str, Any]]:
        example_id = str(row["example_id"])
        selected_client = clients[
            int.from_bytes(
                sha256(f"beaver-llm-endpoint-v1::{example_id}".encode()).digest()[:8],
                "big",
            )
            % len(clients)
        ]

        def tools_factory(_database: Path, database_id: str, search_index: SchemaSearchIndex):
            return BeaverMySQLAgentTools(
                database_id,
                search_index,
                connection_config=connection_config,
                table_inputs=table_inputs,
            )

        offset = sha256(f"beaver-arm-v1::{example_id}".encode()).digest()[0] % len(conditions)
        order = [*conditions[offset:], *conditions[:offset]]
        output: dict[str, dict[str, Any]] = {}
        for condition in order:
            if example_id in completed[condition]:
                continue
            try:
                if condition == GRAPH_EVO_SEMANTIC_PROGRAM_MAIN:
                    output[condition] = run_graph_evo_semantic_program_main(
                        condition="minimal_join_tree_react",
                        row=row,
                        client=selected_client,
                        database=Path("."),
                        search_index=indices[condition],
                        anchor_sql=anchor_by_id[example_id],
                        auxiliary_raw_sql=(
                            auxiliary_raw_by_id[example_id]
                            if args.auxiliary_raw_predictions is not None
                            else None
                        ),
                        max_turns=args.max_turns,
                        max_actions=args.max_actions,
                        max_sql_executions=args.max_sql_executions,
                        initial_schema_top_k=args.initial_schema_top_k,
                        tools_factory=tools_factory,
                        sql_dialect="MySQL",
                    )
                else:
                    output[condition] = run_react_text2sql(
                        condition=condition,
                        row=row,
                        client=selected_client,
                        database=Path("."),
                        search_index=indices[condition],
                        max_turns=args.max_turns,
                        max_actions=args.max_actions,
                        max_sql_executions=args.max_sql_executions,
                        initial_schema_top_k=args.initial_schema_top_k,
                        tools_factory=tools_factory,
                        sql_dialect="MySQL",
                        method_id_override=(
                            EVOLUTION_AWARE_RELATIONAL_PROGRAM_COMPILER
                            if args.anchor_predictions is not None
                            else None
                        ),
                        anchor_sql=(
                            anchor_by_id[example_id]
                            if args.anchor_predictions is not None
                            else None
                        ),
                    )
            except Exception as error:
                output[condition] = {
                    "example_id": example_id,
                    "dataset_id": row["dataset_id"],
                    "database_id": row["database_id"],
                    "upstream_split": row["upstream_split"],
                    "method_id": _declared_method_id(
                        condition,
                        anchored=args.anchor_predictions is not None,
                    ),
                    "asset_condition": condition,
                    "status": "error",
                    "error_type": type(error).__name__,
                    "error": str(error)[:1000],
                    "sql": "",
                }
            if args.lean:
                output[condition] = _strip_lean_metadata(output[condition])
        return output

    pending = [
        row
        for row in rows
        if any(str(row["example_id"]) not in completed[c] for c in conditions)
    ]
    with ThreadPoolExecutor(max_workers=args.concurrency) as executor:
        futures = {executor.submit(run, row): row for row in pending}
        for count, future in enumerate(as_completed(futures), start=1):
            generated = future.result()
            with lock:
                for condition, result in generated.items():
                    completed[condition][str(result["example_id"])] = result
                    with paths[condition].open("a", encoding="utf-8") as handle:
                        handle.write(json.dumps(result, ensure_ascii=False) + "\n")
                        handle.flush()
            print(
                f"[beaver-full {count}/{len(futures)}] "
                f"{futures[future]['example_id']} arms={','.join(generated)}",
                flush=True,
            )
    ordered: dict[str, list[dict[str, Any]]] = {}
    for condition, path in paths.items():
        ordered[condition] = [
            completed[condition][str(row["example_id"])] for row in rows
        ]
        _write_atomic(path, ordered[condition])
    summary = {
        "protocol": "beaver_v3_external_baselines_and_program_graph_v1",
        "rows": len(rows),
        "conditions": list(conditions),
        "errors": {
            condition: sum(row.get("status") == "error" for row in values)
            for condition, values in ordered.items()
        },
        "model": {
            "requested": client.model,
            "require_exact": client.require_exact_model,
            "thinking": client.thinking,
            "endpoints": [value.base_url for value in clients],
            "routing": "sha256(example_id)_mod_endpoint_count_v1",
        },
        "embedding": {
            "model_id": "BAAI/bge-m3",
            "backend": encoder.backend,
            "device": (
                "smart01_cuda1_http"
                if encoder.backend == "vllm_openai_pooling_v1"
                else "cpu"
            ),
            "minilm_used": False,
            "fingerprint": encoder.fingerprint,
            "documents": len(full_documents),
            "unique_retrieval_texts": unique_embedding_texts,
            "query_fingerprint": query_fingerprint,
            "query_cache_path": str(args.query_cache) if args.query_cache else None,
            "query_texts": len(all_query_texts),
        },
        "main_reranker": (
            {
                "model_id": reranker.model,
                "candidate_top_k": args.reranker_top_k,
                "scope": "unified_graph_evo_main_only",
            }
            if reranker is not None
            else None
        ),
        "ontology": ontology.manifest(),
        "evidence_boundary": {
            "target_annotations_in_online_view": False,
            "support": (
                "released physical schema/examples plus target-subset-disjoint historical "
                "question/SQL and aggregated historical mappings/KB"
            ),
            "evaluator_manifest_read_during_generation": False,
            "raw_chess_autolink": (
                "released physical schema/examples + read-only database tools only; "
                "no recovery, historical SQL, KB, or ontology"
            ),
        },
        "base_solution_anchor": (
            {
                "path": str(args.anchor_predictions),
                "rows": len(anchor_by_id),
                "uses_evaluator_gold": False,
            }
            if args.anchor_predictions is not None
            else None
        ),
        "auxiliary_raw_evidence_draft": (
            {
                "path": str(args.auxiliary_raw_predictions),
                "rows": len(auxiliary_raw_by_id),
                "uses_evaluator_gold": False,
                "runtime_score_selection": False,
            }
            if args.auxiliary_raw_predictions is not None
            else None
        ),
        "budgets": {
            "max_turns": args.max_turns,
            "max_actions": args.max_actions,
            "max_sql_executions": args.max_sql_executions,
            "initial_schema_top_k": args.initial_schema_top_k,
            "token_budget": [
                {
                    "endpoint": value.base_url,
                    **value.token_budget_status(),
                }
                for value in clients
            ],
        },
    }
    ontology_manifest = ontology.manifest()
    if args.lean:
        summary["embedding"].pop("fingerprint", None)
        summary["embedding"].pop("query_fingerprint", None)
        summary["ontology"].pop("sha256", None)
        ontology_manifest.pop("sha256", None)
        if len(clients) == 1:
            summary["model"]["routing"] = "single_endpoint"
    if args.resume:
        # A resume replaces explicit error rows in the frozen prediction stream.
        # Preserve the first-pass summary and publish one atomic latest-resume
        # summary so repeated infrastructure retries cannot fail merely because
        # the remaining error count changed.
        _write_latest_json(
            args.output_root / "GENERATION_SUMMARY_RESUMED.json", summary
        )
    else:
        _write_json(args.output_root / "GENERATION_SUMMARY.json", summary)
    _write_json(args.output_root / "ONTOLOGY_MANIFEST.json", ontology_manifest)
    print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
