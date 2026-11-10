from __future__ import annotations

import argparse
import hashlib
import json
import re
import statistics
import time
from collections import defaultdict
from pathlib import Path
from typing import Any

from finsemguard.baselines.autolink_spider2 import (
    dialect_for_instance,
    normalize_table,
    scale_bucket,
)
from finsemguard.retrieval.bm25 import BM25Index, tokenize


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def align_gold_ids(
    questions: dict[str, dict[str, Any]], gold_rows: list[dict[str, Any]]
) -> tuple[dict[str, list[str]], dict[str, str]]:
    gold = {row["instance_id"]: row["gold_tables"] for row in gold_rows}
    remaps: dict[str, str] = {}
    for gold_id in sorted(set(gold) - set(questions)):
        corrected = f"sf_{gold_id}"
        if corrected in questions and corrected not in gold:
            gold[corrected] = gold.pop(gold_id)
            remaps[corrected] = gold_id
    if set(gold) != set(questions):
        raise ValueError("Spider2 questions and gold-table IDs differ")
    return gold, remaps


def table_text(row: dict[str, Any]) -> str:
    names = row.get("nested_column_names") or row.get("column_names") or []
    types = row.get("nested_column_types") or row.get("column_types") or []
    descriptions = row.get("description") or []
    columns = []
    for index, name in enumerate(names):
        column_type = types[index] if index < len(types) else ""
        description = descriptions[index] if index < len(descriptions) else ""
        columns.append(f"{name} {column_type} {description}".strip())
    return "\n".join(
        [
            str(row.get("table_fullname") or row.get("table_name") or ""),
            str(row.get("table_name") or ""),
            *columns,
        ]
    )


def schema_signature(row: dict[str, Any]) -> tuple[tuple[str, str], ...]:
    names = row.get("nested_column_names") or row.get("column_names") or []
    types = row.get("nested_column_types") or row.get("column_types") or []
    return tuple(
        (
            str(name).casefold(),
            str(types[index] if index < len(types) else "").casefold(),
        )
        for index, name in enumerate(names)
    )


def load_database(database_dir: Path) -> dict[str, Any]:
    tables: list[dict[str, Any]] = []
    for path in sorted(database_dir.rglob("*.json")):
        try:
            row = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue
        if not isinstance(row, dict) or "table_name" not in row:
            continue
        table_id = normalize_table(
            str(row.get("table_fullname") or row["table_name"])
        )
        text = table_text(row)
        names = row.get("nested_column_names") or row.get("column_names") or []
        tables.append(
            {
                "table_id": table_id,
                "name": table_id,
                "text": text,
                "columns": len(names),
                "signature": schema_signature(row),
            }
        )
    groups: dict[tuple[tuple[str, str], ...], list[dict[str, Any]]] = defaultdict(list)
    for table in tables:
        groups[table["signature"]].append(table)
    family_documents = []
    for index, members in enumerate(groups.values()):
        representative = members[0]
        sibling_names = " ".join(member["table_id"] for member in members)
        family_documents.append(
            {
                "family_id": f"family_{index}",
                "name": " ".join(member["table_id"] for member in members),
                "table_ids": [member["table_id"] for member in members],
                "columns": representative["columns"],
                "text": representative["text"] + "\nSimilar tables: " + sibling_names,
            }
        )
    return {
        "tables": tables,
        "families": family_documents,
        "table_index": BM25Index(tables),
        "family_index": BM25Index(family_documents),
        "candidate_tables": len(tables),
        "candidate_columns": sum(table["columns"] for table in tables),
        "full_schema_tokens": sum(len(tokenize(table["text"])) for table in tables),
    }


def retrieve(
    query: str, database: dict[str, Any], table_budget: int, family: bool
) -> tuple[list[str], int, int]:
    if family:
        documents = database["families"]
        ranking = database["family_index"].search(query, top_k=len(documents))
        selected = [hit["document"] for hit in ranking[:table_budget]]
        tables = [table for row in selected for table in row["table_ids"]]
        tokens = sum(len(tokenize(row["text"])) for row in selected)
        columns = sum(row["columns"] for row in selected)
        return tables, tokens, columns
    documents = database["tables"]
    ranking = database["table_index"].search(query, top_k=len(documents))
    selected = [hit["document"] for hit in ranking[:table_budget]]
    return (
        [row["table_id"] for row in selected],
        sum(len(tokenize(row["text"])) for row in selected),
        sum(row["columns"] for row in selected),
    )


def external_knowledge(question: dict[str, Any], documents_dir: Path) -> str:
    value = question.get("external_knowledge")
    if not value:
        return ""
    names = value if isinstance(value, list) else [value]
    text = []
    for name in names:
        path = documents_dir / str(name)
        if path.is_file():
            text.append(path.read_text(encoding="utf-8", errors="replace"))
    return "\n".join(text)


def resolve_database_directory(dialect_root: Path, database_name: str) -> Path:
    directories = [path for path in dialect_root.iterdir() if path.is_dir()]
    exact = {path.name.casefold(): path for path in directories}
    key = database_name.casefold()
    if key in exact:
        return exact[key]
    normalized_key = re.sub(r"[^a-z0-9]", "", key)
    normalized = [
        path
        for path in directories
        if re.sub(r"[^a-z0-9]", "", path.name.casefold()) == normalized_key
    ]
    if len(normalized) == 1:
        return normalized[0]
    raise ValueError(
        f"schema directory not found or ambiguous for {(dialect_root.name, database_name)}"
    )


def mean(rows: list[dict[str, Any]], key: str) -> float | None:
    values = [float(row[key]) for row in rows if row.get(key) is not None]
    return round(statistics.fmean(values), 6) if values else None


def summarize(rows: list[dict[str, Any]]) -> dict[str, Any]:
    output: dict[str, Any] = {}
    for method in sorted({row["method"] for row in rows}):
        method_rows = [row for row in rows if row["method"] == method]
        by_bucket = {}
        for bucket in ("le100", "101_500", "501_1000", "1001_3000", "gt3000"):
            selected = [row for row in method_rows if row["scale_bucket"] == bucket]
            if selected:
                by_bucket[bucket] = {
                    "rows": len(selected),
                    "table_recall": mean(selected, "table_recall"),
                    "table_strict_recall": mean(selected, "table_strict_recall"),
                    "selected_tables": mean(selected, "selected_tables"),
                    "selected_columns": mean(selected, "selected_columns"),
                    "context_tokens": mean(selected, "context_tokens"),
                    "context_compression": mean(selected, "context_compression"),
                    "latency_seconds": mean(selected, "latency_seconds"),
                }
        output[method] = {
            "rows": len(method_rows),
            "table_recall": mean(method_rows, "table_recall"),
            "table_strict_recall": mean(method_rows, "table_strict_recall"),
            "selected_tables": mean(method_rows, "selected_tables"),
            "selected_columns": mean(method_rows, "selected_columns"),
            "context_tokens": mean(method_rows, "context_tokens"),
            "context_compression": mean(method_rows, "context_compression"),
            "latency_seconds": mean(method_rows, "latency_seconds"),
            "by_scale_bucket": by_bucket,
        }
    return output


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--questions", type=Path, required=True)
    parser.add_argument("--gold-tables", type=Path, required=True)
    parser.add_argument("--schema-root", type=Path, required=True)
    parser.add_argument("--documents-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--table-budget", type=int, default=10)
    parser.add_argument("--limit", type=int)
    args = parser.parse_args()

    questions = {row["instance_id"]: row for row in load_jsonl(args.questions)}
    gold, id_remaps = align_gold_ids(questions, load_jsonl(args.gold_tables))
    selected_questions = list(questions.values())
    if args.limit is not None:
        selected_questions = selected_questions[: args.limit]

    database_cache: dict[tuple[str, str], dict[str, Any]] = {}
    rows: list[dict[str, Any]] = []
    for question in selected_questions:
        instance_id = question["instance_id"]
        dialect = dialect_for_instance(instance_id)
        database_name = str(question["db"])
        key = (dialect, database_name.casefold())
        if key not in database_cache:
            dialect_root = args.schema_root / dialect
            database_cache[key] = load_database(
                resolve_database_directory(dialect_root, database_name)
            )
        database = database_cache[key]
        query = str(question["question"])
        knowledge = external_knowledge(question, args.documents_dir)
        if knowledge:
            query += "\nExternal knowledge:\n" + knowledge
        expected = {normalize_table(table) for table in gold[instance_id]}
        for method, family in (
            ("bm25_table_raw", False),
            ("evidence_family_bm25", True),
        ):
            started = time.perf_counter()
            predicted, context_tokens, selected_columns = retrieve(
                query, database, args.table_budget, family
            )
            predicted_set = set(predicted)
            matched = predicted_set & expected
            full_tokens = database["full_schema_tokens"]
            rows.append(
                {
                    "instance_id": instance_id,
                    "db": database_name,
                    "dialect": dialect,
                    "method": method,
                    "table_budget": args.table_budget,
                    "scale_bucket": scale_bucket(database["candidate_columns"]),
                    "candidate_tables": database["candidate_tables"],
                    "candidate_columns": database["candidate_columns"],
                    "gold_tables": sorted(expected),
                    "predicted_tables": predicted,
                    "table_recall": len(matched) / len(expected),
                    "table_strict_recall": float(expected <= predicted_set),
                    "selected_tables": len(predicted_set),
                    "selected_columns": selected_columns,
                    "full_schema_tokens": full_tokens,
                    "context_tokens": context_tokens,
                    "context_compression": (
                        1.0 - context_tokens / full_tokens if full_tokens else 0.0
                    ),
                    "model_calls": 0,
                    "model_tokens": 0,
                    "latency_seconds": round(time.perf_counter() - started, 6),
                }
            )
        print(f"[{len(rows) // 2:03d}/{len(selected_questions)}] {instance_id}", flush=True)

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows),
        encoding="utf-8",
    )
    summary = {
        "protocol": {
            "task": "Spider 2.0-Lite large-schema table retrieval",
            "query": "question plus released external knowledge when available",
            "gold_isolation": "official gold tables are used only after retrieval",
            "methods": {
                "bm25_table_raw": "existing lexical retrieval baseline",
                "evidence_family_bm25": (
                    "schema-signature family compression followed by lexical "
                    "prototype retrieval and lossless sibling expansion"
                ),
            },
            "table_group_budget": args.table_budget,
            "metric_scope": "table recall; column gold is unavailable for all 547 rows",
        },
        "inputs_sha256": {
            "questions": file_sha256(args.questions),
            "gold_tables": file_sha256(args.gold_tables),
        },
        "official_gold_id_remaps": id_remaps,
        "executed_questions": len(selected_questions),
        "metrics": summarize(rows),
    }
    args.output.with_suffix(".summary.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
