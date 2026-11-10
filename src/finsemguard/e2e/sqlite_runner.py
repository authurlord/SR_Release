from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
import os
from pathlib import Path
import threading
import time
from typing import Any

from finsemguard.agent.llm import VLLMClient
from finsemguard.e2e.livesqlbench import CatalogDocument, evidence_closure
from finsemguard.e2e.livesqlbench_runner import (
    METHOD_ID,
    _attach_generation_failure,
    _build_embeddings,
    _candidate_pool,
    _canonical_hash,
    _dense_rank,
    _lexical_rank,
    _load_jsonl,
    _generation_cost_audit,
    _merge_generation_retry_cost,
    _normalize_decision,
    _rrf,
    _select,
    _serialize_context,
    _validate_embedding_model_for_run,
    _validate_resume_rows,
    _write_atomic,
)
from finsemguard.e2e.sqlite_catalog import load_catalog, schema_key


SQL_SYSTEM = """You are the shared deterministic SQLite Data Agent used for every
compared context compiler. Use only the supplied semantic subgraph. Never invent a
table, column, relationship, literal meaning, or business rule. Physical identifiers
are explicitly labeled and must be quoted when needed. Obvious spelling errors and
direct lexical or semantic matches from a question phrase to a supplied column label
are bounded evidence, not invented semantics. A released sample row may establish
column roles but is not the complete table. Return one JSON object with exactly
decision, sql, clarification, and answer. decision is answer, clarify, or abstain.
When answerable, sql is exactly one read-only SQLite SELECT/WITH statement and contains
no markdown. Preserve requested aggregation, ordering, aliases and result shape. If
essential evidence is missing or conflicting, clarify or abstain and set sql to null."""


def _validate_sql(sql: str | None) -> dict[str, Any]:
    if not sql:
        return {"valid": False, "reason": "missing_sql"}
    try:
        import sqlglot

        statements = sqlglot.parse(sql, read="sqlite")
        if len(statements) != 1:
            return {"valid": False, "reason": "multiple_statements"}
        if statements[0].key not in {"select", "union", "intersect", "except"}:
            return {
                "valid": False,
                "reason": "query_track_non_readonly",
                "expression": statements[0].key,
            }
        return {"valid": True, "expression": statements[0].key}
    except Exception as error:
        return {
            "valid": False,
            "reason": type(error).__name__,
            "detail": str(error)[:500],
        }


def _run_one(
    row: dict[str, Any],
    client: VLLMClient,
    docs_by_database: dict[str, list[CatalogDocument]],
    all_documents: dict[str, CatalogDocument],
    vector_by_id: dict[str, Any],
    query_vector: Any,
) -> dict[str, Any]:
    started = time.perf_counter()
    database_key = schema_key(row)
    question = str(row["question"])
    documents = docs_by_database[database_key]
    ranking = _rrf(
        _dense_rank(query_vector, documents, vector_by_id),
        _lexical_rank(question, documents),
    )
    candidates = _candidate_pool(ranking, all_documents)
    selected, selector_usage, selector_hash = _select(client, question, candidates)
    sql_call_started = False
    sql_usage: dict[str, Any] | None = None
    try:
        closed = evidence_closure(selected, candidates, all_documents)
        context = _serialize_context(closed)
        user_payload = {
            "dataset": row["dataset_id"],
            "database": row["database_id"],
            "upstream_split": row["upstream_split"],
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
        "database_id": row["database_id"],
        "method_id": METHOD_ID,
        "decision": decision,
        "sql": sql,
        "clarification": prediction.get("clarification"),
        "answer": prediction.get("answer"),
        "validation": _validate_sql(sql),
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
                "sql_agent": _canonical_hash(
                    {"system": SQL_SYSTEM, "user": user_payload}
                ),
            },
        },
        "latency_seconds": round(time.perf_counter() - started, 6),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--dataset-id", choices=("dr_spider", "kaggledbqa", "llmsql"), required=True
    )
    parser.add_argument("--data-root", type=Path, required=True)
    parser.add_argument("--online-manifest", type=Path, required=True)
    parser.add_argument("--embedding-model", type=Path, required=True)
    parser.add_argument("--embedding-cache", type=Path, required=True)
    parser.add_argument("--embedding-device", default="cpu")
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
    if any(str(row["dataset_id"]) != args.dataset_id for row in full_rows):
        raise ValueError("online manifest dataset does not match --dataset-id")
    rows = full_rows if args.limit is None else full_rows[: args.limit]
    _validate_embedding_model_for_run(args.embedding_model, args.output)
    documents = load_catalog(args.dataset_id, args.data_root, full_rows)
    all_documents = {row.candidate_id: row for row in documents}
    docs_by_database: dict[str, list[CatalogDocument]] = {}
    for document in documents:
        docs_by_database.setdefault(document.database_id, []).append(document)
    missing_keys = sorted(
        {schema_key(row) for row in full_rows} - set(docs_by_database)
    )
    if missing_keys:
        raise ValueError(f"manifest schemas missing from catalog: {missing_keys[:5]}")
    vector_by_id, query_vectors, embedding_hash = _build_embeddings(
        documents,
        full_rows,
        args.embedding_model,
        args.embedding_cache,
        device=args.embedding_device,
    )
    if args.build_embeddings_only:
        print(
            json.dumps(
                {
                    "dataset_id": args.dataset_id,
                    "documents": len(vector_by_id),
                    "questions": len(query_vectors),
                    "databases": len(docs_by_database),
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
            return _run_one(
                row,
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
                "upstream_split": row["upstream_split"],
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
            result = future.result()
            example_id = futures[future]
            result = _merge_generation_retry_cost(
                result, prior_errors.get(example_id)
            )
            with lock:
                by_id[example_id] = result
                with args.output.open("a", encoding="utf-8") as handle:
                    handle.write(json.dumps(result, ensure_ascii=False) + "\n")
            print(
                f"[{completed_count}/{len(pending)}] {example_id} "
                f"status={'error' if result.get('status') == 'error' else 'ok'}",
                flush=True,
            )
    ordered = [by_id[str(row["example_id"])] for row in rows]
    _write_atomic(args.output, ordered)
    summary = {
        "method_id": METHOD_ID,
        "dataset_id": args.dataset_id,
        "rows": len(ordered),
        "errors": sum(row.get("status") == "error" for row in ordered),
        "valid_sql": sum(
            row.get("validation", {}).get("valid") is True for row in ordered
        ),
        "decisions": {
            decision: sum(row.get("decision") == decision for row in ordered)
            for decision in ("answer", "clarify", "abstain")
        },
        "protocol": {
            "client_concurrency": args.concurrency,
            "gold_access": "none; online manifest and released schemas only",
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
