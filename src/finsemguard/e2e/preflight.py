from __future__ import annotations

import argparse
import hashlib
import json
import socket
import sqlite3
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Iterable


DR_SPIDER_SETS = (
    "DB_DBcontent_equivalence",
    "DB_schema_abbreviation",
    "DB_schema_synonym",
    "NLQ_column_attribute",
    "NLQ_column_carrier",
    "NLQ_column_synonym",
    "NLQ_column_value",
    "NLQ_keyword_carrier",
    "NLQ_keyword_synonym",
    "NLQ_multitype",
    "NLQ_others",
    "NLQ_value_synonym",
    "SQL_DB_number",
    "SQL_DB_text",
    "SQL_NonDB_number",
    "SQL_comparison",
    "SQL_sort_order",
)


def _load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _load_jsonl(path: Path) -> list[dict[str, Any]]:
    with path.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def _sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def _fingerprint(paths: Iterable[Path], base: Path) -> dict[str, Any]:
    files = sorted({path.resolve() for path in paths if path.is_file()})
    inventory = [
        {
            "path": str(path.relative_to(base.resolve())),
            "bytes": path.stat().st_size,
            "sha256": _sha256(path),
        }
        for path in files
    ]
    canonical = json.dumps(
        inventory, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    ).encode()
    return {
        "file_count": len(inventory),
        "total_bytes": sum(row["bytes"] for row in inventory),
        "inventory_sha256": hashlib.sha256(canonical).hexdigest(),
        "files": inventory,
    }


def _git_head(path: Path) -> str | None:
    head = path / ".git" / "HEAD"
    if not head.exists():
        return None
    value = head.read_text(encoding="utf-8").strip()
    if value.startswith("ref: "):
        ref = path / ".git" / value.removeprefix("ref: ")
        if ref.exists():
            return ref.read_text(encoding="utf-8").strip()
        packed = path / ".git" / "packed-refs"
        if packed.exists():
            suffix = value.removeprefix("ref: ")
            for line in packed.read_text(encoding="utf-8").splitlines():
                if line and not line.startswith(("#", "^")):
                    commit, name = line.split(" ", 1)
                    if name == suffix:
                        return commit
        return None
    return value


def _port_open(host: str, port: int) -> bool:
    try:
        with socket.create_connection((host, port), timeout=0.5):
            return True
    except OSError:
        return False


def _livesql_gold_present(rows: list[dict[str, Any]]) -> bool:
    return bool(rows) and all(
        isinstance(row.get("sol_sql"), str)
        and bool(row["sol_sql"].strip())
        and isinstance(row.get("test_cases"), list)
        for row in rows
    )


def _credential_configured(path: Path) -> bool:
    if not path.is_file():
        return False
    value = _load_json(path)
    return isinstance(value, dict) and bool(value) and all(bool(item) for item in value.values())


def _livesqlbench(root: Path, code_root: Path, postgres_ready: bool) -> dict[str, Any]:
    questions = root / "livesqlbench_data.jsonl"
    rows = _load_jsonl(questions) if questions.is_file() else []
    database_ids = sorted({str(row.get("selected_database", "")) for row in rows})
    schema_files = [root / db_id / f"{db_id}_schema.txt" for db_id in database_ids]
    dump_root = root / "postgre_table_dumps_full"
    dump_files = list(dump_root.rglob("*.sql")) if dump_root.is_dir() else []
    evaluator = code_root / "evaluation" / "src" / "evaluation.py"
    ids = [str(row.get("instance_id")) for row in rows]
    checks = {
        "rows_600": len(rows) == 600,
        "unique_ids": len(ids) == len(set(ids)),
        "database_count_22": len(database_ids) == 22,
        "schema_for_every_database": all(path.is_file() for path in schema_files),
        "gold_and_test_cases_present": _livesql_gold_present(rows),
        "database_dumps_present": len(dump_files) > 200,
        "official_evaluator_present": evaluator.is_file(),
    }
    return {
        "id": "livesqlbench_base_full_v1",
        "upstream_split": "full_release_normal_questions",
        "rows": len(rows),
        "database_count": len(database_ids),
        "asset_ready": all(checks.values()),
        "runtime_ready": all(checks.values()) and postgres_ready,
        "checks": checks,
        "runtime": {"postgresql_reachable": postgres_ready},
        "upstream_commit": _git_head(root),
        "evaluator_commit": _git_head(code_root),
        "fingerprint": _fingerprint(
            [questions, evaluator, *schema_files, *dump_files], root.parent
        ),
    }


def _spider2(root: Path) -> dict[str, Any]:
    lite = root / "spider2-lite"
    questions = lite / "spider2-lite.jsonl"
    rows = _load_jsonl(questions) if questions.is_file() else []
    ids = [str(row.get("instance_id")) for row in rows]
    evaluation = lite / "evaluation_suite"
    evaluator_files = [evaluation / "evaluate.py", evaluation / "evaluate_utils.py"]
    credentials = {
        "bigquery": _credential_configured(evaluation / "bigquery_credential.json"),
        "snowflake": _credential_configured(evaluation / "snowflake_credential.json"),
    }
    schema_files = list((lite / "resource" / "databases").rglob("DDL.csv"))
    gold_files = list((evaluation / "gold").rglob("*"))
    gold_files = [path for path in gold_files if path.is_file()]
    checks = {
        "rows_547": len(rows) == 547,
        "unique_ids": len(ids) == len(set(ids)),
        "official_evaluator_present": all(path.is_file() for path in evaluator_files),
        "schema_resources_present": bool(schema_files),
        "self_evaluation_answers_present": bool(gold_files),
        "backend_credentials_configured": all(credentials.values()),
    }
    return {
        "id": "spider2_lite",
        "upstream_split": "full_release",
        "rows": len(rows),
        "database_count": len({str(row.get("db")) for row in rows}),
        "asset_ready": all(checks.values()),
        "runtime_ready": all(checks.values()),
        "checks": checks,
        "runtime": {"credentials_configured": credentials},
        "upstream_commit": _git_head(root),
        "fingerprint": _fingerprint(
            [questions, *evaluator_files, *schema_files, *gold_files], root.parent
        ),
    }


def _dr_spider(root: Path, evaluator_root: Path) -> dict[str, Any]:
    data = root / "data"
    question_files = [data / name / "questions_post_perturbation.json" for name in DR_SPIDER_SETS]
    gold_files = [data / name / "gold_post_perturbation.sql" for name in DR_SPIDER_SETS]
    counts = {
        name: len(_load_json(path)) if path.is_file() else 0
        for name, path in zip(DR_SPIDER_SETS, question_files, strict=True)
    }
    sqlite_files = list(data.rglob("*.sqlite"))
    evaluator_files = [evaluator_root / "evaluation.py", evaluator_root / "exec_eval.py"]
    checks = {
        "all_17_sets_present": all(path.is_file() for path in question_files),
        "gold_for_all_17_sets": all(path.is_file() for path in gold_files),
        "sqlite_databases_present": bool(sqlite_files),
        "official_evaluator_present": all(path.is_file() for path in evaluator_files),
    }
    return {
        "id": "dr_spider",
        "upstream_split": "all_17_perturbation_test_sets_post_perturbation",
        "rows": sum(counts.values()),
        "released_test_sets": len(DR_SPIDER_SETS),
        "rows_by_test_set": counts,
        "asset_ready": all(checks.values()),
        "runtime_ready": all(checks.values()),
        "checks": checks,
        "upstream_commit": _git_head(root),
        "evaluator_commit": _git_head(evaluator_root),
        "fingerprint": _fingerprint(
            [*question_files, *gold_files, *sqlite_files, *evaluator_files], root.parent
        ),
    }


def _kaggledbqa(root: Path, evaluator_root: Path) -> dict[str, Any]:
    examples = root / "examples"
    full_files = sorted(
        path
        for path in examples.glob("*.json")
        if not path.stem.endswith(("_test", "_fewshot"))
    )
    test_files = sorted(examples.glob("*_test.json"))
    fewshot_files = sorted(examples.glob("*_fewshot.json"))
    full_rows = sum(len(_load_json(path)) for path in full_files)
    test_rows = sum(len(_load_json(path)) for path in test_files)
    fewshot_rows = sum(len(_load_json(path)) for path in fewshot_files)
    schema = root / "KaggleDBQA_tables.json"
    schemas = _load_json(schema) if schema.is_file() else []
    db_ids = [str(row["db_id"]) for row in schemas]
    sqlite_files = list((root / "databases").rglob("*.sqlite"))
    evaluator_files = [evaluator_root / "evaluation.py", evaluator_root / "exec_eval.py"]
    checks = {
        "complete_release_rows_272": full_rows == 272,
        "official_plain_test_rows_185": test_rows == 185,
        "fewshot_rows_87": fewshot_rows == 87,
        "database_count_8": len(db_ids) == 8 and len(sqlite_files) == 8,
        "official_schema_present": schema.is_file(),
        "execution_evaluator_present": all(path.is_file() for path in evaluator_files),
    }
    return {
        "id": "kaggledbqa",
        "upstream_split": "complete_release",
        "rows": full_rows,
        "official_plain_test_rows": test_rows,
        "fewshot_rows": fewshot_rows,
        "database_count": len(db_ids),
        "asset_ready": all(checks.values()),
        "runtime_ready": all(checks.values()),
        "checks": checks,
        "upstream_commit": _git_head(root),
        "evaluator_commit": _git_head(evaluator_root),
        "fingerprint": _fingerprint(
            [*full_files, *test_files, *fewshot_files, schema, *sqlite_files, *evaluator_files],
            root.parent,
        ),
    }


def _llmsql(root: Path, code_root: Path) -> dict[str, Any]:
    questions = root / "test_questions.jsonl"
    rows = _load_jsonl(questions) if questions.is_file() else []
    ids = [str(row.get("question_id")) for row in rows]
    database = root / "sqlite_tables.db"
    table_count = 0
    if database.is_file():
        with sqlite3.connect(database) as connection:
            table_count = int(
                connection.execute(
                    "SELECT count(*) FROM sqlite_master WHERE type='table'"
                ).fetchone()[0]
            )
    evaluator_files = [
        code_root / "llmsql" / "evaluation" / "evaluate.py",
        code_root / "llmsql" / "utils" / "evaluation_utils.py",
    ]
    checks = {
        "official_test_rows_15834": len(rows) == 15834,
        "unique_ids": len(ids) == len(set(ids)),
        "sqlite_table_count_25609": table_count == 25609,
        "gold_sql_present": all(bool(row.get("sql")) for row in rows),
        "official_evaluator_present": all(path.is_file() for path in evaluator_files),
    }
    return {
        "id": "llmsql",
        "upstream_split": "test",
        "rows": len(rows),
        "database_count": table_count,
        "asset_ready": all(checks.values()),
        "runtime_ready": all(checks.values()),
        "checks": checks,
        "upstream_commit": _git_head(root),
        "evaluator_commit": _git_head(code_root),
        "fingerprint": _fingerprint(
            [questions, database, *evaluator_files], root.parent
        ),
    }


def build_preflight_manifest(
    dataset_root: Path,
    spider2_root: Path,
    *,
    postgres_host: str = "127.0.0.1",
    postgres_port: int = 55432,
) -> dict[str, Any]:
    postgres_ready = _port_open(postgres_host, postgres_port)
    evaluator_root = dataset_root / "test-suite-sql-eval"
    datasets = [
        _livesqlbench(
            dataset_root / "LiveSQLBench_data",
            dataset_root / "LiveSQLBench_code",
            postgres_ready,
        ),
        _spider2(spider2_root),
        _dr_spider(dataset_root / "DrSpider", evaluator_root),
        _kaggledbqa(dataset_root / "KaggleDBQA", evaluator_root),
        _llmsql(dataset_root / "LLMSQL_data", dataset_root / "LLMSQL_code"),
    ]
    return {
        "experiment_id": "e2e_5dataset_4090_24h_v1",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "split_policy": "preserve upstream labels; no dev/test relabeling",
        "hardware_policy": {
            "gpu": "2xRTX4090",
            "h200_allowed": False,
            "kv_cache_dtype": "fp8_e4m3",
            "client_concurrency": 8,
            "minimum_client_concurrency": 5,
            "enforce_eager": False,
        },
        "datasets": datasets,
        "asset_ready_count": sum(bool(row["asset_ready"]) for row in datasets),
        "runtime_ready_count": sum(bool(row["runtime_ready"]) for row in datasets),
        "asset_gate": "PASS" if all(row["asset_ready"] for row in datasets) else "NO_GO",
        "runtime_gate": "PASS" if all(row["runtime_ready"] for row in datasets) else "NO_GO",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset-root", type=Path, required=True)
    parser.add_argument("--spider2-root", type=Path, required=True)
    parser.add_argument("--postgres-host", default="127.0.0.1")
    parser.add_argument("--postgres-port", type=int, default=55432)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    manifest = build_preflight_manifest(
        args.dataset_root,
        args.spider2_root,
        postgres_host=args.postgres_host,
        postgres_port=args.postgres_port,
    )
    args.output.parent.mkdir(parents=True, exist_ok=True)
    temporary = args.output.with_suffix(args.output.suffix + ".tmp")
    temporary.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    temporary.replace(args.output)
    print(json.dumps({
        "output": str(args.output),
        "asset_gate": manifest["asset_gate"],
        "runtime_gate": manifest["runtime_gate"],
        "asset_ready_count": manifest["asset_ready_count"],
        "runtime_ready_count": manifest["runtime_ready_count"],
    }, ensure_ascii=False))


if __name__ == "__main__":
    main()
