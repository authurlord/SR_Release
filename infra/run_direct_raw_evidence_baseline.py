#!/usr/bin/env python3
"""Run the frozen Direct Raw-Evidence baseline without ReACT or search tools."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from hashlib import sha256
import json
import os
from pathlib import Path
import sqlite3
from threading import Lock
import time
from typing import Any, Callable

from finsemguard.agent.llm import VLLMClient
from finsemguard.config import load_config
from finsemguard.e2e.direct_raw_evidence_sql import (
    METHOD_ID,
    DirectRawEvidenceConfig,
    RawHistoryExample,
    RawPhysicalSchema,
    raw_history_from_rows,
    raw_history_from_table_inputs,
    raw_schema_from_snapshot,
    raw_schema_from_sqlite_database,
    raw_schema_from_table_inputs,
    run_direct_raw_evidence_sql,
)
from finsemguard.e2e.evolution_relations import (
    RelationEvolutionMapping,
    reverse_map_evolved_sql,
)


DATASETS = {
    "fiben",
    "kaggledbqa",
    "bird",
    "spider2",
    "evoschema",
    "beaver",
}
KAGGLE_RAW_HISTORY_PROTOCOL = "kaggledbqa_direct_raw_history_pool_v1"


def _strip_lean_metadata(value: Any) -> Any:
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


def _load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def _atomic_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    content = "".join(
        json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows
    )
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(content, encoding="utf-8")
    temporary.replace(path)


def _atomic_json(path: Path, value: dict[str, Any]) -> None:
    content = json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(content, encoding="utf-8")
    temporary.replace(path)


def _database_path(data_root: Path, row: dict[str, Any]) -> Path:
    target_spec = str(row["database_or_answer_target"])
    if target_spec.startswith("spider2://"):
        candidate = data_root / f"{row['database_id']}.sqlite"
        if not candidate.is_file():
            raise FileNotFoundError(f"Spider2 SQLite database not found: {candidate}")
        return candidate.resolve()
    target = data_root / target_spec
    if target.is_file():
        return target.resolve()
    candidate = target / f"{row['database_id']}.sqlite"
    if not candidate.is_file():
        raise FileNotFoundError(f"SQLite database not found: {candidate}")
    return candidate.resolve()


def _resume_completed(row: dict[str, Any], *, retry_invalid_sql: bool = False) -> bool:
    if row.get('method_id') != METHOD_ID or row.get('status') == 'error':
        return False
    if retry_invalid_sql:
        return (row.get('status') != 'invalid_sql' and bool(str(row.get('sql') or '').strip())
                and row.get('error_only_check', {}).get('ok') is not False)
    return True


def _sqlite_error_only_check(
    database: Path, *, translated_sql: Callable[[str], str] | None = None
) -> Callable[[str], dict[str, Any]]:
    def check(sql: str) -> dict[str, Any]:
        started = time.monotonic()
        connection = sqlite3.connect(f"file:{database}?mode=ro", uri=True)
        connection.set_progress_handler(
            lambda: 1 if time.monotonic() - started > 8.0 else 0,
            1000,
        )
        try:
            physical_sql = translated_sql(sql) if translated_sql is not None else sql
            cursor = connection.execute("EXPLAIN QUERY PLAN " + physical_sql)
            cursor.close()
            return {"ok": True, "error_type": "", "error": ""}
        except Exception as error:
            return {
                "ok": False,
                "error_type": type(error).__name__,
                "error": str(error)[:800],
            }
        finally:
            connection.close()

    return check


def _mysql_error_only_check(
    *, connection_config: dict[str, Any], database_id: str
) -> Callable[[str], dict[str, Any]]:
    def check(sql: str) -> dict[str, Any]:
        connection = None
        cursor = None
        try:
            import mysql.connector

            connection = mysql.connector.connect(
                **connection_config,
                database=database_id,
                connection_timeout=15,
            )
            cursor = connection.cursor(buffered=True)
            cursor.execute("EXPLAIN " + sql)
            # The plan rows are deliberately discarded and never reach the model.
            cursor.fetchall()
            return {"ok": True, "error_type": "", "error": ""}
        except Exception as error:
            return {
                "ok": False,
                "error_type": type(error).__name__,
                "error": str(error)[:800],
            }
        finally:
            if cursor is not None:
                cursor.close()
            if connection is not None:
                connection.close()

    return check


def _select_rows(
    rows: list[dict[str, Any]], requested: list[str], subset_size: int | None
) -> list[dict[str, Any]]:
    if requested and subset_size is not None:
        raise ValueError("--example-id and --subset-size are mutually exclusive")
    if requested:
        requested_set = set(requested)
        output = [row for row in rows if str(row["example_id"]) in requested_set]
        if {str(row["example_id"]) for row in output} != requested_set:
            raise ValueError("one or more requested example IDs are absent")
        return output
    if subset_size is not None:
        if subset_size < 1:
            raise ValueError("--subset-size must be positive")
        return rows[:subset_size]
    return rows


def _validate_kaggledbqa_history_support(
    *,
    history_path: Path,
    audit_path: Path,
    online_rows: list[dict[str, Any]],
) -> dict[str, Any]:
    rows = _load_jsonl(history_path)
    audit = json.loads(audit_path.read_text(encoding="utf-8"))
    if audit.get("protocol") != KAGGLE_RAW_HISTORY_PROTOCOL:
        raise ValueError("KaggleDBQA raw history has the wrong protocol")
    digest = sha256(history_path.read_bytes()).hexdigest()
    if digest != str(audit.get("pool_sha256") or ""):
        raise ValueError("KaggleDBQA raw history pool hash mismatch")
    if len(rows) != int(audit.get("rows", -1)):
        raise ValueError("KaggleDBQA raw history pool row count mismatch")
    if not rows:
        raise ValueError("KaggleDBQA raw history pool is empty")
    if any(set(row) != {"history_id", "database_id", "question", "sql"} for row in rows):
        raise ValueError("KaggleDBQA raw history exposes fields outside raw NL-SQL")
    history_ids = [str(row.get("history_id") or "") for row in rows]
    if any(not value for value in history_ids) or len(history_ids) != len(set(history_ids)):
        raise ValueError("KaggleDBQA raw history IDs are empty or duplicated")
    if any(
        not str(row.get(field) or "").strip()
        for row in rows
        for field in ("database_id", "question", "sql")
    ):
        raise ValueError("KaggleDBQA raw history contains incomplete NL-SQL")
    target_overlap = dict(audit.get("target_overlap") or {})
    if int(target_overlap.get("history_id", -1)) != 0 or int(
        target_overlap.get("normalized_question", -1)
    ) != 0:
        raise ValueError("KaggleDBQA raw history failed target-overlap audit")
    if int(target_overlap.get("upstream_retained_ast_template_test_overlap", -1)) != 0:
        raise ValueError("KaggleDBQA raw history failed upstream AST isolation")
    question_hashes = dict(audit.get("question_sha256") or {})
    sql_hashes = dict(audit.get("sql_sha256") or {})
    for row in rows:
        history_id = str(row["history_id"])
        if question_hashes.get(history_id) != sha256(
            str(row["question"]).encode("utf-8")
        ).hexdigest():
            raise ValueError(f"KaggleDBQA question hash mismatch: {history_id}")
        if sql_hashes.get(history_id) != sha256(
            str(row["sql"]).encode("utf-8")
        ).hexdigest():
            raise ValueError(f"KaggleDBQA SQL hash mismatch: {history_id}")
    target_ids = {str(row.get("example_id") or "") for row in online_rows}
    if target_ids & set(history_ids):
        raise ValueError("KaggleDBQA raw history contains a target example ID")
    return audit


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset", choices=sorted(DATASETS), required=True)
    parser.add_argument("--online", type=Path, required=True)
    parser.add_argument("--data-root", type=Path)
    parser.add_argument("--table-inputs", type=Path)
    parser.add_argument("--runtime", type=Path)
    parser.add_argument("--history-support", type=Path)
    parser.add_argument("--history-support-audit", type=Path)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument(
        "--llm-base-url",
        action="append",
        default=[],
        help=(
            "OpenAI-compatible generation endpoint. Repeat to route distinct "
            "rows deterministically across identical model servers."
        ),
    )
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument(
        "--lean",
        action="store_true",
        help="Omit API logs and checksum/audit metadata from active outputs.",
    )
    parser.add_argument("--concurrency", type=int, default=32)
    parser.add_argument("--example-id", action="append", default=[])
    parser.add_argument("--subset-size", type=int)
    parser.add_argument("--resume", action="store_true")
    parser.add_argument('--retry-invalid-sql', action='store_true',
                        help='On resume, regenerate invalid/empty SQL drafts; preserve completed valid rows.')
    parser.add_argument("--mysql-host", default="127.0.0.1")
    parser.add_argument("--mysql-port", type=int, default=3306)
    parser.add_argument("--mysql-user", default="root")
    parser.add_argument("--mysql-password-env", default="BEAVER_MYSQL_PASSWORD")
    args = parser.parse_args()
    if args.concurrency < 1:
        raise ValueError("concurrency must be positive")
    if args.dataset in {"fiben", "kaggledbqa", "bird", "spider2"} and args.data_root is None:
        raise ValueError("static SQLite datasets require --data-root")
    if args.dataset == "beaver" and args.table_inputs is None:
        raise ValueError("BEAVER requires --table-inputs")
    if args.dataset == "kaggledbqa" and (
        args.history_support is None or args.history_support_audit is None
    ):
        raise ValueError(
            "KaggleDBQA requires --history-support and --history-support-audit"
        )
    if args.dataset == "evoschema" and (
        args.runtime is None
        or args.history_support is None
        or args.history_support_audit is None
        or args.data_root is None
    ):
        raise ValueError(
            "EvoSchema requires --runtime, --history-support, "
            "--history-support-audit, and --data-root"
        )

    all_rows = _load_jsonl(args.online)
    rows = _select_rows(all_rows, args.example_id, args.subset_size)
    if len({str(row["example_id"]) for row in rows}) != len(rows):
        raise ValueError("online manifest contains duplicate example IDs")
    args.output_root.mkdir(parents=True, exist_ok=True)
    subset_path = args.output_root / "SUBSET.jsonl"
    subset_content = "".join(
        json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows
    )
    if subset_path.exists() and subset_path.read_text(encoding="utf-8") != subset_content:
        raise FileExistsError("refusing to change the frozen baseline subset")
    if not subset_path.exists():
        subset_path.write_text(subset_content, encoding="utf-8")

    table_inputs = _load_jsonl(args.table_inputs) if args.table_inputs else []
    runtime_rows = _load_jsonl(args.runtime) if args.runtime else []
    runtime = {str(row["example_id"]): row for row in runtime_rows}
    history_support = (
        _load_jsonl(args.history_support) if args.history_support else []
    )
    history_audit: dict[str, Any] | None = None
    if args.dataset == "evoschema" and set(runtime) != {
        str(row["example_id"]) for row in all_rows
    }:
        raise ValueError("EvoSchema runtime does not exactly match online rows")
    if args.dataset == "evoschema":
        history_audit = json.loads(
            args.history_support_audit.read_text(encoding="utf-8")
        )
        if sha256(args.history_support.read_bytes()).hexdigest() != str(
            history_audit.get("support_sha256") or ""
        ):
            raise ValueError("EvoSchema history support hash failed isolation audit")
        required_collision_checks = {
            "target_id",
            "normalized_question",
            "normalized_sql",
            "literal_stripped_ast_skeleton",
        }
        if not required_collision_checks <= set(
            history_audit.get("collision_checks") or []
        ):
            raise ValueError("EvoSchema history support lacks collision checks")
    elif args.dataset == "kaggledbqa":
        assert args.history_support is not None
        assert args.history_support_audit is not None
        history_audit = _validate_kaggledbqa_history_support(
            history_path=args.history_support,
            audit_path=args.history_support_audit,
            online_rows=all_rows,
        )

    config_file_sha = (
        "" if args.lean else sha256(args.config.read_bytes()).hexdigest()
    )
    llm_config = dict(load_config(args.config)["llm"])
    if float(llm_config.get("temperature", 0.0)) != 0.0:
        raise ValueError("Direct Raw-Evidence baseline requires temperature 0")
    if int(llm_config.get("max_output_tokens", 2048)) != 2048:
        raise ValueError("Direct Raw-Evidence baseline requires 2048 output tokens")
    base_urls = list(args.llm_base_url) or [str(llm_config["base_url"])]
    clients: list[VLLMClient] = []
    for index, base_url in enumerate(base_urls):
        endpoint_config = dict(llm_config)
        endpoint_config["base_url"] = base_url
        if args.lean:
            endpoint_config.pop("audit_log_path", None)
        else:
            endpoint_config["audit_log_path"] = str(
                args.output_root / f"api_audit.endpoint{index}.jsonl"
            )
        client = VLLMClient(endpoint_config)
        if not client.healthy():
            raise RuntimeError(
                f"required exact LLM is unavailable at {client.base_url}"
            )
        clients.append(client)

    source_paths = [
        Path(__file__),
        Path(__file__).parents[1]
        / "src/finsemguard/e2e/direct_raw_evidence_sql.py",
    ]
    source_sha = (
        ""
        if args.lean
        else sha256(
            "".join(
                sha256(path.read_bytes()).hexdigest() for path in source_paths
            ).encode()
        ).hexdigest()
    )
    frozen_config = DirectRawEvidenceConfig()
    mysql_config: dict[str, Any] | None = None
    if args.dataset == "beaver":
        password = os.environ.get(args.mysql_password_env)
        if password is None:
            raise RuntimeError(
                f"missing MySQL password environment variable: {args.mysql_password_env}"
            )
        mysql_config = {
            "host": args.mysql_host,
            "port": args.mysql_port,
            "user": args.mysql_user,
            "password": password,
        }

    schema_cache: dict[str, RawPhysicalSchema] = {}
    history_cache: dict[str, list[RawHistoryExample]] = {}
    mappings: dict[str, RelationEvolutionMapping] = {}
    databases: dict[str, Path] = {}
    for row in rows:
        example_id = str(row["example_id"])
        database_id = str(row["database_id"])
        if args.dataset == "evoschema":
            runtime_row = runtime[example_id]
            mapping = RelationEvolutionMapping.from_json(
                dict(runtime_row["mapping"])
            )
            mappings[example_id] = mapping
            schema_cache[example_id] = raw_schema_from_snapshot(
                dict(runtime_row["mapping"]["current_snapshot"])
            )
            source_database_id = str(row["source_database_id"])
            history_cache[example_id] = raw_history_from_rows(
                history_support,
                schema_context=source_database_id,
            )
            databases[example_id] = _database_path(args.data_root, row)
        elif args.dataset == "beaver":
            if database_id not in schema_cache:
                schema_cache[database_id] = raw_schema_from_table_inputs(
                    table_inputs,
                    schema_context=database_id,
                    # BEAVER relation observations are history-derived, not
                    # physically declared FK constraints.
                    declared_relationship=lambda _row: False,
                )
                history_cache[database_id] = raw_history_from_table_inputs(
                    table_inputs, schema_context=database_id
                )
        else:
            database = _database_path(args.data_root, row)
            databases[example_id] = database
            cache_key = database_id if table_inputs else str(database)
            if cache_key not in schema_cache:
                schema_cache[cache_key] = (
                    raw_schema_from_table_inputs(
                        table_inputs,
                        schema_context=database_id,
                        # These static sidecars are built directly from released
                        # DDL/schema-manifest foreign-key declarations.
                        declared_relationship=lambda relation: str(
                            relation.get("evidence_id") or ""
                        ).startswith(("fiben.ddl.", "relationship.")),
                    )
                    if table_inputs
                    else raw_schema_from_sqlite_database(database)
                )
            if database_id not in history_cache:
                if args.dataset == "kaggledbqa":
                    history_cache[database_id] = raw_history_from_rows(
                        history_support,
                        schema_context=database_id,
                        context_key="database_id",
                        question_key="question",
                        sql_key="sql",
                        id_key="history_id",
                    )
                else:
                    history_cache[database_id] = raw_history_from_table_inputs(
                        table_inputs, schema_context=database_id
                    )

    output_path = args.output_root / "predictions.jsonl"
    previous = _load_jsonl(output_path) if args.resume and output_path.exists() else []
    if output_path.exists() and not args.resume:
        raise FileExistsError(f"prediction output exists: {output_path}")
    completed = {
        str(row["example_id"]): row
        for row in previous
        if _resume_completed(row, retry_invalid_sql=args.retry_invalid_sql)
    }
    row_order = {str(row["example_id"]): index for index, row in enumerate(rows)}
    results = dict(completed)
    write_lock = Lock()

    def generate(source_row: dict[str, Any]) -> dict[str, Any]:
        example_id = str(source_row["example_id"])
        database_id = str(source_row["database_id"])
        row = dict(source_row)
        client = clients[row_order[example_id] % len(clients)]
        try:
            if args.dataset == "evoschema":
                mapping = mappings[example_id]
                row["history_target_id"] = str(source_row["official_train_idx"])
                schema = schema_cache[example_id]
                history = history_cache[example_id]

                def translate(sql: str) -> str:
                    return reverse_map_evolved_sql(
                        sql,
                        mapping=mapping,
                        preserve_current_projection=True,
                    )

                check = _sqlite_error_only_check(
                    databases[example_id], translated_sql=translate
                )
                dialect = "SQLite"
            elif args.dataset == "beaver":
                assert mysql_config is not None
                schema = schema_cache[database_id]
                history = history_cache[database_id]
                check = _mysql_error_only_check(
                    connection_config=mysql_config,
                    database_id=database_id,
                )
                dialect = "MySQL"
            else:
                database = databases[example_id]
                schema = schema_cache[
                    database_id if table_inputs else str(database)
                ]
                history = history_cache.get(database_id, [])
                check = _sqlite_error_only_check(database)
                dialect = "SQLite"
            result = run_direct_raw_evidence_sql(
                row=row,
                client=client,
                schema=schema,
                history=history,
                error_only_check=check,
                dialect=dialect,
                config=frozen_config,
                source_sha256=source_sha,
                config_sha256=config_file_sha,
            )
            return _strip_lean_metadata(result) if args.lean else result
        except Exception as error:
            result = {
                "example_id": example_id,
                "dataset_id": source_row.get("dataset_id"),
                "database_id": database_id,
                "method_id": METHOD_ID,
                "status": "error",
                "error_type": type(error).__name__,
                "error": str(error)[:1000],
                "sql": "",
                "graph_evo_context_sha256": None,
                "tools_exposed": [],
            }
            return _strip_lean_metadata(result) if args.lean else result

    pending = [
        row for row in rows if str(row["example_id"]) not in completed
    ]
    with ThreadPoolExecutor(max_workers=args.concurrency) as executor:
        futures = {executor.submit(generate, row): row for row in pending}
        for future in as_completed(futures):
            result = future.result()
            with write_lock:
                results[str(result["example_id"])] = result
                ordered = sorted(
                    results.values(),
                    key=lambda value: row_order[str(value["example_id"])],
                )
                _atomic_jsonl(output_path, ordered)
                if len(results) % 25 == 0 or len(results) == len(rows):
                    print(
                        f"[direct-raw {len(results)}/{len(rows)}]",
                        flush=True,
                    )

    final = sorted(
        results.values(), key=lambda value: row_order[str(value["example_id"])]
    )
    manifest = {
        "method_id": METHOD_ID,
        "dataset": args.dataset,
        "examples": len(rows),
        "completed": sum(row.get("status") != "error" for row in final),
        "errors": sum(row.get("status") == "error" for row in final),
        "invalid_sql": sum(row.get("status") == "invalid_sql" for row in final),
        "generation_calls": sum(int(row.get("generation_calls") or 0) for row in final),
        "generation_endpoints": len(clients),
        "tools_exposed": [],
        "source_sha256": source_sha,
        "config_sha256": config_file_sha,
        "input_sha256": sha256(args.online.read_bytes()).hexdigest(),
        "predictions_sha256": sha256(output_path.read_bytes()).hexdigest(),
        "raw_history_pool": (
            {
                "path": str(args.history_support),
                "sha256": sha256(args.history_support.read_bytes()).hexdigest(),
                "audit_path": str(args.history_support_audit),
                "audit_sha256": sha256(
                    args.history_support_audit.read_bytes()
                ).hexdigest(),
                "protocol": (history_audit or {}).get("protocol"),
                "corpus_examples": len(history_support),
                "by_database": {
                    database_id: len(examples)
                    for database_id, examples in sorted(history_cache.items())
                    if args.dataset == "kaggledbqa"
                },
            }
            if args.history_support is not None
            and args.history_support_audit is not None
            else None
        ),
        "input_boundary": (
            "question + raw current physical schema + target-isolated raw NL-SQL"
        ),
        "forbidden_capabilities": [
            "react",
            "schema_search",
            "value_search",
            "join_search",
            "semantic_retrieval",
            "recovered_descriptions",
            "inferred_relations",
            "graph",
            "lineage",
            "selector",
            "fallback",
        ],
    }
    if args.lean:
        manifest = _strip_lean_metadata(manifest)
    _atomic_json(args.output_root / "RUN_MANIFEST.json", manifest)
    print(json.dumps(manifest, ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
