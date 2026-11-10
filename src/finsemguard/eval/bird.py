from __future__ import annotations

import argparse
import hashlib
import json
import math
import sqlite3
import statistics
import time
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

import sqlglot
from sqlglot import exp

from finsemguard.agent.bird_demo import run_benchmark
from finsemguard.config import load_config, project_path
from finsemguard.data.bird import database_path


def sql_objects(sql: str) -> tuple[set[str], set[str]]:
    tree = sqlglot.parse_one(sql, read="sqlite")
    tables = {table.name.lower() for table in tree.find_all(exp.Table)}
    columns = {column.name.lower() for column in tree.find_all(exp.Column)}
    return tables, columns


def execute_rows(
    database: Path, sql: str, timeout_seconds: float | None = 20.0
) -> list[tuple[Any, ...]]:
    """Execute BIRD SQL verbatim in a read-only SQLite connection.

    BIRD gold SQL uses valid SQLite identifiers that ``sqlglot`` cannot always
    parse (for example, backtick-quoted columns containing spaces or hyphens).
    The official metric executes SQLite SQL directly, so evaluator safety is
    enforced by SQLite's read-only mode and authorizer instead of an AST parser.
    """

    if not sql.strip():
        raise ValueError("SQL must not be empty")
    if timeout_seconds is not None and timeout_seconds <= 0:
        raise ValueError("timeout_seconds must be positive")
    # None explicitly disables the evaluator deadline. Query-local probe budgets
    # and legacy evaluation configurations retain their existing limits.
    deadline = None if timeout_seconds is None else time.monotonic() + timeout_seconds
    connection = sqlite3.connect(f"file:{database.resolve()}?mode=ro", uri=True)
    connection.execute("PRAGMA query_only=ON")

    allowed_actions = {
        sqlite3.SQLITE_SELECT,
        sqlite3.SQLITE_READ,
        sqlite3.SQLITE_FUNCTION,
        sqlite3.SQLITE_RECURSIVE,
    }

    def authorize(
        action: int,
        _arg1: str | None,
        _arg2: str | None,
        _database_name: str | None,
        _trigger_name: str | None,
    ) -> int:
        return sqlite3.SQLITE_OK if action in allowed_actions else sqlite3.SQLITE_DENY

    connection.set_authorizer(authorize)

    def progress() -> int:
        return int(deadline is not None and time.monotonic() > deadline)

    if deadline is not None:
        connection.set_progress_handler(progress, 10_000)
    try:
        return connection.execute(sql).fetchall()
    finally:
        connection.close()


def official_ex(predicted_rows: list[tuple[Any, ...]], gold_rows: list[tuple[Any, ...]]) -> bool:
    """Match the official BIRD Mini-Dev EX implementation (set equality)."""
    return set(predicted_rows) == set(gold_rows)


def wilson_interval(successes: int, total: int, z: float = 1.96) -> list[float]:
    if total == 0:
        return [0.0, 0.0]
    p = successes / total
    denominator = 1 + z * z / total
    center = (p + z * z / (2 * total)) / denominator
    margin = z * math.sqrt((p * (1 - p) + z * z / (4 * total)) / total) / denominator
    return [round(100 * max(0.0, center - margin), 2), round(100 * min(1.0, center + margin), 2)]


def percentile(values: list[float], probability: float) -> float:
    if not values:
        return 0.0
    ordered = sorted(values)
    index = math.ceil(probability * len(ordered)) - 1
    return round(ordered[max(index, 0)], 3)


def select_rows(source: Path, db_id: str, limit: int) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = json.loads(source.read_text(encoding="utf-8"))
    return [row for row in rows if row["db_id"] == db_id][:limit]


def retrieval_objects(retrieval: list[dict[str, Any]]) -> tuple[set[str], set[str]]:
    tables: set[str] = set()
    columns: set[str] = set()
    for item in retrieval:
        parts = item["name"].split(".")
        if item["kind"] == "table" and len(parts) >= 2:
            tables.add(parts[-1].lower())
        elif item["kind"] == "column" and len(parts) >= 3:
            tables.add(parts[-2].lower())
            columns.add(parts[-1].lower())
        elif item["kind"] == "relationship":
            text = item["text"].lower()
            for side in text.split(":", 1)[-1].split("->"):
                if "." in side:
                    table, column = side.strip().split(".", 1)
                    tables.add(table)
                    columns.add(column)
    return tables, columns


def evaluate_one(row: dict[str, Any], database: Path) -> dict[str, Any]:
    started = time.perf_counter()
    trace = run_benchmark(
        row["question"],
        row["db_id"],
        row.get("evidence", ""),
    )
    latency = time.perf_counter() - started
    gold_tables, gold_columns = sql_objects(row["SQL"])
    retrieved_tables, retrieved_columns = retrieval_objects(trace.retrieval)

    gold_rows: list[tuple[Any, ...]] | None = None
    predicted_rows: list[tuple[Any, ...]] | None = None
    gold_error = predicted_error = None
    try:
        gold_rows = execute_rows(database, row["SQL"])
    except Exception as error:
        gold_error = f"{type(error).__name__}: {error}"
    if trace.decision.value == "answer" and trace.sql:
        try:
            predicted_rows = execute_rows(database, trace.sql)
        except Exception as error:
            predicted_error = f"{type(error).__name__}: {error}"
    correct = bool(
        gold_rows is not None
        and predicted_rows is not None
        and official_ex(predicted_rows, gold_rows)
    )
    return {
        "question_id": row["question_id"],
        "db_id": row["db_id"],
        "difficulty": row.get("difficulty"),
        "question": row["question"],
        "benchmark_evidence": row.get("evidence", ""),
        "gold_sql": row["SQL"],
        "decision": trace.decision.value,
        "predicted_sql": trace.sql,
        "validator": trace.validator,
        "clarification": trace.clarification,
        "evidence_ids": (
            trace.semantic_plan.evidence_ids if trace.semantic_plan is not None else []
        ),
        "gold_tables": sorted(gold_tables),
        "gold_columns": sorted(gold_columns),
        "retrieved_tables": sorted(retrieved_tables),
        "retrieved_columns": sorted(retrieved_columns),
        "table_recall": len(gold_tables & retrieved_tables) / max(len(gold_tables), 1),
        "column_recall": len(gold_columns & retrieved_columns) / max(len(gold_columns), 1),
        "official_ex": correct,
        "gold_result_count": len(gold_rows) if gold_rows is not None else None,
        "predicted_result_count": len(predicted_rows) if predicted_rows is not None else None,
        "gold_error": gold_error,
        "predicted_error": predicted_error,
        "latency_seconds": round(latency, 3),
    }


def summarize(
    records: list[dict[str, Any]], selection_hash: str, profile: str
) -> dict[str, Any]:
    total = len(records)
    answered = sum(record["decision"] == "answer" for record in records)
    clarifications = sum(record["decision"] == "clarify" for record in records)
    abstentions = sum(record["decision"] == "abstain" for record in records)
    valid_sql = sum(record["validator"].get("valid") is True for record in records)
    correct = sum(record["official_ex"] for record in records)
    silent_errors = sum(
        record["decision"] == "answer"
        and record["validator"].get("valid") is True
        and not record["official_ex"]
        for record in records
    )
    latencies = [float(record["latency_seconds"]) for record in records]
    difficulty: defaultdict[str, Counter[str]] = defaultdict(Counter)
    for record in records:
        bucket = difficulty[record.get("difficulty") or "unknown"]
        bucket["n"] += 1
        bucket["correct"] += int(record["official_ex"])
        bucket["answered"] += int(record["decision"] == "answer")

    return {
        "protocol": {
            "dataset": "BIRD Mini-Dev SQLite financial subset",
            "profile": profile,
            "selection": "first N financial rows in official Mini-Dev order",
            "selection_sha256": selection_hash,
            "metric": "official BIRD EX-style set equality",
            "temperature": 0.0,
        },
        "n": total,
        "execution_accuracy_pct": round(100 * correct / max(total, 1), 2),
        "execution_accuracy_wilson_95_pct": wilson_interval(correct, total),
        "correct": correct,
        "coverage_pct": round(100 * answered / max(total, 1), 2),
        "answered": answered,
        "answered_accuracy_pct": round(100 * correct / max(answered, 1), 2),
        "clarifications": clarifications,
        "abstentions": abstentions,
        "valid_sql_rate_pct": round(100 * valid_sql / max(total, 1), 2),
        "silent_semantic_error_rate_pct": round(100 * silent_errors / max(answered, 1), 2),
        "silent_semantic_errors": silent_errors,
        "mean_table_recall_pct": round(
            100 * statistics.fmean(record["table_recall"] for record in records), 2
        ),
        "mean_column_recall_pct": round(
            100 * statistics.fmean(record["column_recall"] for record in records), 2
        ),
        "latency_seconds": {
            "mean": round(statistics.fmean(latencies), 3) if latencies else 0.0,
            "p50": percentile(latencies, 0.50),
            "p95": percentile(latencies, 0.95),
            "total": round(sum(latencies), 3),
        },
        "by_difficulty": {
            name: {
                "n": counts["n"],
                "execution_accuracy_pct": round(
                    100 * counts["correct"] / max(counts["n"], 1), 2
                ),
                "coverage_pct": round(100 * counts["answered"] / max(counts["n"], 1), 2),
            }
            for name, counts in sorted(difficulty.items())
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--source", type=Path, default=Path("data/raw/bird_mini_dev/mini_dev_sqlite.json")
    )
    parser.add_argument("--db-id", default="financial")
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--profile", default="full_enriched_schema_typed_plan_guarded_v1")
    parser.add_argument("--seed-results", type=Path)
    parser.add_argument("--config", default="configs/base.yaml")
    args = parser.parse_args()

    config = load_config(args.config)
    rows = select_rows(args.source, args.db_id, args.limit)
    if len(rows) != args.limit:
        raise ValueError(f"requested {args.limit} rows, found {len(rows)}")
    selection_hash = hashlib.sha256(
        json.dumps([row["question_id"] for row in rows]).encode()
    ).hexdigest()
    database = database_path(
        project_path(config["paths"]["bird_dev_databases"]), args.db_id
    )
    if database is None:
        raise FileNotFoundError(f"database not found: {args.db_id}")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    records: list[dict[str, Any]] = []
    if args.seed_results:
        records = [
            json.loads(line)
            for line in args.seed_results.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        expected_ids = [row["question_id"] for row in rows[: len(records)]]
        actual_ids = [record["question_id"] for record in records]
        if actual_ids != expected_ids:
            raise ValueError("seed results are not a prefix of the selected evaluation rows")
    with args.output.open("w", encoding="utf-8") as handle:
        for record in records:
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
        handle.flush()
        for index, row in enumerate(rows[len(records) :], start=len(records) + 1):
            record = evaluate_one(row, database)
            records.append(record)
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
            handle.flush()
            print(
                f"[{index:02d}/{len(rows)}] q={row['question_id']} "
                f"decision={record['decision']} ex={int(record['official_ex'])} "
                f"latency={record['latency_seconds']:.3f}s",
                flush=True,
            )
    summary = summarize(records, selection_hash, args.profile)
    summary_path = args.output.with_suffix(".summary.json")
    summary_path.write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
