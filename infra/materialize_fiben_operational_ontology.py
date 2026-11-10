#!/usr/bin/env python3
"""Materialize physical FIBEN manifests and train-only operational ontology assets."""

from __future__ import annotations

import argparse
from hashlib import sha256
import json
from pathlib import Path
import re
import sqlite3
from typing import Any


FOREIGN_KEY_RE = re.compile(
    r"^ALTER\s+TABLE\s+(?P<source_table>[A-Za-z0-9_]+)\s+"
    r"ADD\s+CONSTRAINT\s+(?P<constraint>[A-Za-z0-9_]+)\s+"
    r"FOREIGN\s+KEY\s+\((?P<source_column>[A-Za-z0-9_]+)\)\s+"
    r"REFERENCES\s+(?P<target_table>[A-Za-z0-9_]+)\s+"
    r"\((?P<target_column>[A-Za-z0-9_]+)\)",
    re.IGNORECASE,
)
BASE_WORDS = {
    "account", "accounts", "accrued", "amount", "and", "applicable",
    "asset", "average", "balance", "by", "cash", "classification",
    "code", "contract", "corporation", "country", "currency", "date",
    "debt", "description", "email", "entity", "expense", "facilitated",
    "fair", "financial", "fiscal", "for", "from", "has", "holding",
    "id", "income", "instrument", "is", "last", "legal", "liability",
    "listed", "loss", "market", "metric", "monetary", "name", "number",
    "of", "owned", "owner", "payable", "period", "person", "phone",
    "provided", "refers", "report", "revenue", "security", "service",
    "stock", "symbol", "ticker", "to", "traded", "transaction", "type",
    "value", "year",
}


def _load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line]


def _sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def _write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    content = "".join(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows)
    if path.exists():
        if path.read_text(encoding="utf-8") != content:
            raise FileExistsError(f"refusing to overwrite different artifact: {path}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(content, encoding="utf-8")
    temporary.replace(path)


def _segment(identifier: str, vocabulary: set[str]) -> str:
    compact = re.sub(r"[^A-Za-z0-9]+", "", identifier).casefold()
    if not compact:
        return identifier.casefold()
    words = sorted((word for word in vocabulary if len(word) > 1), key=lambda x: (-len(x), x))
    best: list[list[str] | None] = [None] * (len(compact) + 1)
    best[0] = []
    for index in range(len(compact)):
        if best[index] is None:
            continue
        for word in words:
            if compact.startswith(word, index):
                target = index + len(word)
                candidate = [*best[index], word]
                if best[target] is None or len(candidate) < len(best[target] or []):
                    best[target] = candidate
    if best[-1]:
        return " ".join(best[-1] or [])
    spaced = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", identifier)
    return re.sub(r"[^A-Za-z0-9]+", " ", spaced).strip().casefold()


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--processed-root", type=Path, required=True)
    parser.add_argument("--ddl", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    args = parser.parse_args()

    questions = _load_jsonl(args.processed_root / "questions.jsonl")
    patterns = _load_jsonl(args.processed_root / "query_patterns.jsonl")
    if any(str(row.get("split_origin")) != "train" for row in patterns):
        raise ValueError("FIBEN query-pattern ontology must be train-only")
    vocabulary = set(BASE_WORDS)
    for pattern in patterns:
        for question in pattern.get("metadata", {}).get("question_examples", []):
            vocabulary.update(re.findall(r"[a-z]{2,}", str(question).casefold()))

    test_rows = [row for row in questions if row["split"] == "test"]
    online = [
        {
            "example_id": row["question_id"],
            "dataset_id": "fiben",
            "database_id": "fiben",
            "database_or_answer_target": "fiben.sqlite",
            "schema_manifest": "fiben.sqlite",
            "upstream_split": f"test:{row['query_type']}",
            "question": row["question"],
            "allowed_docs": [],
            "evaluator_id": "fiben_sqlite_execution",
            "evaluator_version": "fiben-local-v1",
        }
        for row in test_rows
    ]
    evaluator = [
        {
            "example_id": row["question_id"],
            "dataset_id": "fiben",
            "database_id": "fiben",
            "upstream_split": f"test:{row['query_type']}",
            "gold": {
                "sql": row["sql"],
                "query_type": row["query_type"],
                "unique_query_id": row["unique_query_id"],
            },
        }
        for row in test_rows
    ]

    relationships: list[dict[str, Any]] = []
    for line_number, line in enumerate(args.ddl.read_text(encoding="utf-8").splitlines(), start=1):
        match = FOREIGN_KEY_RE.match(line.strip())
        if not match:
            continue
        values = {key: value.upper() for key, value in match.groupdict().items()}
        relationships.append(
            {
                "source": f"{values['source_table']}.{values['source_column']}",
                "target": f"{values['target_table']}.{values['target_column']}",
                "evidence_id": f"fiben.ddl.line.{line_number}.{values['constraint']}",
            }
        )
    relationships_by_table: dict[str, list[dict[str, Any]]] = {}
    for relation in relationships:
        table = relation["source"].split(".", 1)[0]
        relationships_by_table.setdefault(table, []).append(relation)

    database = args.processed_root / "fiben.sqlite"
    connection = sqlite3.connect(f"file:{database.resolve()}?mode=ro", uri=True)
    try:
        table_names = [
            str(row[0])
            for row in connection.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name"
            )
        ]
        table_inputs: list[dict[str, Any]] = []
        recovery_rows: list[dict[str, Any]] = []
        for table in table_names:
            columns = [
                {
                    "physical_column": str(row[1]),
                    "declared_type": str(row[2] or "unknown"),
                    "primary_key": bool(row[5]),
                    "observed_values": [],
                    "history_ids": [],
                }
                for row in connection.execute(f'PRAGMA table_info("{table}")')
            ]
            payload = {
                "format_version": "fiben_operational_ontology_inputs_v1",
                "schema_context": "fiben",
                "db_id": "fiben",
                "physical_table": table,
                "columns": columns,
                "relationships": relationships_by_table.get(table, []),
                "target_disjoint_workload": [],
                "supplied_evidence_ids": [
                    row["evidence_id"] for row in relationships_by_table.get(table, [])
                ],
            }
            payload["input_id"] = "fiben.table." + sha256(
                json.dumps(payload, sort_keys=True, separators=(",", ":")).encode()
            ).hexdigest()[:24]
            table_inputs.append(payload)
            recovery_rows.append(
                {
                    "input_id": payload["input_id"],
                    "schema_context": "fiben",
                    "physical_table": table,
                    "method_id": "fiben_train_vocabulary_decompound_v1",
                    "prediction": {
                        "physical_table": table,
                        "table_aliases": [_segment(table, vocabulary)],
                        "purpose": f"Financial entity: {_segment(table, vocabulary)}",
                        "columns": [
                            {
                                "physical_column": column["physical_column"],
                                "aliases": [_segment(column["physical_column"], vocabulary)],
                                "retrieval_gloss": (
                                    "Physical financial predicate: "
                                    + _segment(column["physical_column"], vocabulary)
                                ),
                                "semantic_type": "identifier" if column["primary_key"] else "unknown",
                                "query_phrases": [_segment(column["physical_column"], vocabulary)],
                                "observed_values": [],
                            }
                            for column in columns
                        ],
                    },
                }
            )
    finally:
        connection.close()

    physical_tables = {row["physical_table"] for row in table_inputs}
    physical_columns = {
        f"{row['physical_table']}.{column['physical_column']}"
        for row in table_inputs
        for column in row["columns"]
    }
    knowledge: list[dict[str, Any]] = []
    for relation in relationships:
        knowledge.append(
            {
                "schema_context": "fiben",
                "source": relation["source"],
                "target": relation["target"],
                "relation": "ddl_foreign_key",
                "description": "FIBEN DDL foreign-key relationship",
                "source_name": "FIBEN.sql",
                "evidence_id": relation["evidence_id"],
                "confidence": 1.0,
            }
        )
    for pattern in patterns:
        metadata = pattern.get("metadata") or {}
        columns = [
            str(value).upper()
            for value in metadata.get("columns") or []
            if str(value).upper() in physical_columns
        ]
        tables = [
            str(value).upper()
            for value in metadata.get("tables") or []
            if str(value).upper() in physical_tables
        ]
        if not columns:
            continue
        questions_for_pattern = [str(value) for value in metadata.get("question_examples") or []]
        knowledge.append(
            {
                "schema_context": "fiben",
                "physical_identifiers": columns,
                "relation": "target_disjoint_train_workload_pattern",
                "aliases": questions_for_pattern,
                "description": (
                    "Train-only Text-to-SQL pattern. Tables: "
                    + ", ".join(tables)
                    + ". Questions: "
                    + " | ".join(questions_for_pattern)
                )[:1800],
                "source_name": "FIBEN train split query pattern",
                "evidence_id": str(pattern["doc_id"]),
                "confidence": 1.0,
            }
        )

    args.output_root.mkdir(parents=True, exist_ok=True)
    paths = {
        "online": args.output_root / "online.jsonl",
        "evaluator": args.output_root / "evaluator_only.jsonl",
        "table_inputs": args.output_root / "table_inputs.jsonl",
        "recovery": args.output_root / "table_recovery.jsonl",
        "knowledge": args.output_root / "knowledge.jsonl",
    }
    for name, rows in (
        ("online", online),
        ("evaluator", evaluator),
        ("table_inputs", table_inputs),
        ("recovery", recovery_rows),
        ("knowledge", knowledge),
    ):
        _write_jsonl(paths[name], rows)
    manifest = {
        "format": "fiben_operational_ontology_assets_v1",
        "test_rows": len(online),
        "tables": len(table_inputs),
        "columns": sum(len(row["columns"]) for row in table_inputs),
        "ddl_relationships": len(relationships),
        "train_pattern_documents": len(knowledge) - len(relationships),
        "baseline_evidence": "physical_sqlite_schema_only",
        "treatment_evidence": "automatic_decompounding_plus_train_patterns_plus_ddl_ontology",
        "evaluator_read_by_online_runner": False,
        "source_sha256": {
            "database": _sha(database),
            "questions": _sha(args.processed_root / "questions.jsonl"),
            "patterns": _sha(args.processed_root / "query_patterns.jsonl"),
            "ddl": _sha(args.ddl),
        },
        "output_sha256": {name: _sha(path) for name, path in paths.items()},
    }
    manifest_path = args.output_root / "MANIFEST.json"
    content = json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if manifest_path.exists() and manifest_path.read_text(encoding="utf-8") != content:
        raise FileExistsError(f"refusing to overwrite different artifact: {manifest_path}")
    if not manifest_path.exists():
        manifest_path.write_text(content, encoding="utf-8")
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
