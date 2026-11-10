from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
import sqlite3
from collections import Counter
from pathlib import Path
from typing import Any, Iterable


FINANCE_TERMS = re.compile(
    r"financial|finance|debit|credit|bank|loan|retail|sales?|market|coin|insurance",
    re.IGNORECASE,
)


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def identifier(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", value.lower()).strip("_")


def flatten(values: Iterable[Any]) -> set[int]:
    result: set[int] = set()
    for value in values:
        if isinstance(value, list):
            result.update(int(item) for item in value)
        else:
            result.add(int(value))
    return result


def database_path(root: Path | None, db_id: str) -> Path | None:
    if root is None:
        return None
    candidates = [root / db_id / f"{db_id}.sqlite", root / f"{db_id}.sqlite"]
    return next((path for path in candidates if path.is_file()), None)


def column_descriptions(sqlite_path: Path | None) -> dict[tuple[str, str], dict[str, str]]:
    descriptions: dict[tuple[str, str], dict[str, str]] = {}
    if sqlite_path is None:
        return descriptions
    description_root = sqlite_path.parent / "database_description"
    if not description_root.is_dir():
        return descriptions
    for path in description_root.glob("*.csv"):
        # BIRD description files mix UTF-8 and Windows-1252 bytes. Keep raw
        # files untouched and replace only undecodable description glyphs.
        with path.open("r", encoding="utf-8-sig", errors="replace", newline="") as handle:
            for row in csv.DictReader(handle):
                original = (row.get("original_column_name") or "").strip()
                if not original:
                    continue
                descriptions[(path.stem.lower(), original.lower())] = {
                    key: (value or "").strip()
                    for key, value in row.items()
                    if key and value and value.strip()
                }
    return descriptions


def quote_identifier(value: str) -> str:
    return '"' + value.replace('"', '""') + '"'


def profile_column(
    connection: sqlite3.Connection | None,
    table: str,
    column: str,
    *,
    distinct_limit: int = 21,
) -> dict[str, Any]:
    if connection is None:
        return {}
    table_sql = quote_identifier(table)
    column_sql = quote_identifier(column)
    try:
        rows = connection.execute(
            f"SELECT DISTINCT {column_sql} FROM {table_sql} "
            f"WHERE {column_sql} IS NOT NULL LIMIT ?",
            (distinct_limit,),
        ).fetchall()
    except sqlite3.Error:
        return {}
    values: list[Any] = []
    for (value,) in rows[:20]:
        if isinstance(value, bytes):
            rendered: Any = f"<bytes:{len(value)}>"
        elif isinstance(value, str) and len(value) > 100:
            rendered = value[:97] + "..."
        else:
            rendered = value
        values.append(rendered)
    return {
        "observed_values": values if len(rows) <= 20 else values[:5],
        "low_cardinality": len(rows) <= 20,
        "profile_truncated": len(rows) > 20,
    }


def schema_documents(
    schema: dict[str, Any],
    *,
    split_origin: str,
    database_root: Path | None,
    profile_values: bool = False,
) -> list[dict[str, Any]]:
    db_id = schema["db_id"]
    tables_original = schema["table_names_original"]
    tables_logical = schema.get("table_names", tables_original)
    columns_original = schema["column_names_original"]
    columns_logical = schema.get("column_names", columns_original)
    column_types = schema.get("column_types", ["unknown"] * len(columns_original))
    primary_keys = flatten(schema.get("primary_keys", []))
    sqlite_path = database_path(database_root, db_id)
    descriptions = column_descriptions(sqlite_path)
    profile_connection = None
    if profile_values and sqlite_path is not None:
        profile_connection = sqlite3.connect(
            f"file:{sqlite_path.resolve()}?mode=ro", uri=True
        )

    per_table: dict[int, list[int]] = {index: [] for index in range(len(tables_original))}
    for column_index, (table_index, _) in enumerate(columns_original):
        if table_index >= 0:
            per_table[int(table_index)].append(column_index)

    documents: list[dict[str, Any]] = []
    for table_index, table in enumerate(tables_original):
        logical = tables_logical[table_index]
        column_indexes = per_table[table_index]
        column_names = [columns_original[index][1] for index in column_indexes]
        documents.append(
            {
                "doc_id": f"bird.{identifier(db_id)}.table.{identifier(table)}",
                "kind": "table",
                "dataset": "bird",
                "split_origin": split_origin,
                "name": f"{db_id}.{table}",
                "text": (
                    f"BIRD database {db_id}; table {table}; semantic name {logical}; "
                    f"columns: {', '.join(column_names)}"
                ),
                "table": table,
                "column": None,
                "metadata": {
                    "db_id": db_id,
                    "logical_name": logical,
                    "column_count": len(column_indexes),
                    "executable": sqlite_path is not None,
                },
            }
        )
        for column_index in column_indexes:
            _, column = columns_original[column_index]
            logical_column = columns_logical[column_index][1]
            data_type = column_types[column_index]
            description = descriptions.get((table.lower(), column.lower()), {})
            semantic_description = description.get("column_description", "")
            value_description = description.get("value_description", "")
            value_profile = profile_column(profile_connection, table, column)
            observed_values = value_profile.get("observed_values", [])
            documents.append(
                {
                    "doc_id": (
                        f"bird.{identifier(db_id)}.column."
                        f"{identifier(table)}.{identifier(column)}"
                    ),
                    "kind": "column",
                    "dataset": "bird",
                    "split_origin": split_origin,
                    "name": f"{db_id}.{table}.{column}",
                    "text": (
                        f"BIRD column {db_id}.{table}.{column}; semantic name "
                        f"{logical_column}; type={data_type}; "
                        f"primary_key={column_index in primary_keys}; "
                        f"description={semantic_description}; documented_values={value_description}; "
                        f"observed_values={json.dumps(observed_values, ensure_ascii=False)}"
                    ),
                    "table": table,
                    "column": column,
                    "metadata": {
                        "db_id": db_id,
                        "logical_name": logical_column,
                        "data_type": data_type,
                        "primary_key": column_index in primary_keys,
                        "description": semantic_description,
                        "value_description": value_description,
                        **value_profile,
                        "executable": sqlite_path is not None,
                    },
                }
            )

    for source_index, target_index in schema.get("foreign_keys", []):
        source_table_index, source_column = columns_original[source_index]
        target_table_index, target_column = columns_original[target_index]
        source_table = tables_original[source_table_index]
        target_table = tables_original[target_table_index]
        relation_name = f"{source_table}.{source_column} -> {target_table}.{target_column}"
        documents.append(
            {
                "doc_id": (
                    f"bird.{identifier(db_id)}.relationship."
                    f"{identifier(source_table)}_{identifier(source_column)}__"
                    f"{identifier(target_table)}_{identifier(target_column)}"
                ),
                "kind": "relationship",
                "dataset": "bird",
                "split_origin": split_origin,
                "name": f"{db_id}.{relation_name}",
                "text": f"BIRD foreign-key relationship in {db_id}: {relation_name}",
                "table": source_table,
                "column": source_column,
                "metadata": {
                    "db_id": db_id,
                    "source_table": source_table,
                    "source_column": source_column,
                    "target_table": target_table,
                    "target_column": target_column,
                    "executable": sqlite_path is not None,
                },
            }
        )
    if profile_connection is not None:
        profile_connection.close()
    return documents


def write_questions(source: Path, target: Path, split: str) -> dict[str, Any]:
    rows: list[dict[str, Any]] = json.loads(source.read_text(encoding="utf-8"))
    db_counts: Counter[str] = Counter()
    difficulty_counts: Counter[str] = Counter()
    with target.open("w", encoding="utf-8") as handle:
        for index, row in enumerate(rows):
            db_id = row["db_id"]
            db_counts[db_id] += 1
            if difficulty := row.get("difficulty"):
                difficulty_counts[difficulty] += 1
            record = {
                "question_id": f"bird_{split}_{row.get('question_id', index)}",
                "source_question_id": row.get("question_id", index),
                "db_id": db_id,
                "question": row["question"].strip(),
                "evidence": row.get("evidence", "").strip(),
                "sql": (row.get("SQL") or row.get("sql") or "").strip(),
                "difficulty": row.get("difficulty"),
                "split": split,
            }
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    return {
        "questions": len(rows),
        "databases": len(db_counts),
        "by_database": dict(sorted(db_counts.items())),
        "by_difficulty": dict(sorted(difficulty_counts.items())),
        "finance_questions": sum(
            count for db_id, count in db_counts.items() if FINANCE_TERMS.search(db_id)
        ),
    }


def prepare(
    dev_source: Path,
    dev_schemas: Path,
    database_root: Path,
    output: Path,
    train_source: Path | None = None,
    train_schemas: Path | None = None,
    train_database_root: Path | None = None,
) -> dict[str, Any]:
    output.mkdir(parents=True, exist_ok=True)
    dev_schema_rows: list[dict[str, Any]] = json.loads(dev_schemas.read_text(encoding="utf-8"))
    train_schema_rows: list[dict[str, Any]] = []
    if train_schemas and train_schemas.exists():
        train_schema_rows = json.loads(train_schemas.read_text(encoding="utf-8"))

    dev_stats = write_questions(dev_source, output / "dev_questions.jsonl", "dev")
    train_stats: dict[str, Any] | None = None
    if train_source and train_source.exists():
        train_stats = write_questions(train_source, output / "train_questions.jsonl", "train")

    documents: list[dict[str, Any]] = []
    for schema in dev_schema_rows:
        documents.extend(
            schema_documents(
                schema,
                split_origin="dev_schema",
                database_root=database_root,
                profile_values=bool(FINANCE_TERMS.search(schema["db_id"])),
            )
        )
    for schema in train_schema_rows:
        documents.extend(
            schema_documents(
                schema,
                split_origin="train_schema",
                database_root=train_database_root,
                profile_values=bool(FINANCE_TERMS.search(schema["db_id"])),
            )
        )
    with (output / "catalog.jsonl").open("w", encoding="utf-8") as handle:
        for document in documents:
            handle.write(json.dumps(document, ensure_ascii=False) + "\n")

    dev_sqlite_files = [
        path
        for schema in dev_schema_rows
        if (path := database_path(database_root, schema["db_id"])) is not None
    ]
    train_sqlite_files = [
        path
        for schema in train_schema_rows
        if (path := database_path(train_database_root, schema["db_id"])) is not None
    ]
    sqlite_files = dev_sqlite_files + train_sqlite_files
    selected_train_ids = {path.stem for path in train_sqlite_files}
    selected_train_questions = sum(
        count
        for db_id, count in (train_stats or {}).get("by_database", {}).items()
        if db_id in selected_train_ids
    )
    for path in sqlite_files:
        connection = sqlite3.connect(f"file:{path.resolve()}?mode=ro", uri=True)
        try:
            connection.execute("SELECT 1").fetchone()
        finally:
            connection.close()

    source_files = [dev_source, dev_schemas]
    if train_source and train_source.exists():
        source_files.append(train_source)
    if train_schemas and train_schemas.exists():
        source_files.append(train_schemas)
    manifest = {
        "dataset": "BIRD-SQL",
        "mirror": "ModelScope: wangzhaocheng/bird-bench",
        "upstream": "https://bird-bench.github.io/",
        "license": "See upstream BIRD dataset terms",
        "source_sha256": {path.name: file_sha256(path) for path in source_files},
        "questions": {
            "total": dev_stats["questions"] + (train_stats or {}).get("questions", 0),
            "dev": dev_stats,
            "train": train_stats,
        },
        "schemas": {
            "databases": len(dev_schema_rows) + len(train_schema_rows),
            "dev_databases": len(dev_schema_rows),
            "train_databases": len(train_schema_rows),
            "catalog_documents": len(documents),
            "value_profile_policy": (
                "Finance-like executable DBs; all values for <=20 distinct, otherwise 5 samples"
            ),
        },
        "executable": {
            "databases": len(sqlite_files),
            "dev_databases": len(dev_sqlite_files),
            "selected_train_databases": len(train_sqlite_files),
            "selected_train_database_ids": sorted(selected_train_ids),
            "questions": dev_stats["questions"] + selected_train_questions,
            "selected_train_questions": selected_train_questions,
            "sqlite_bytes": sum(path.stat().st_size for path in sqlite_files),
            "dev_database_root": str(database_root.resolve()),
            "train_database_root": (
                str(train_database_root.resolve()) if train_database_root else None
            ),
        },
        "leakage_policy": (
            "Dev SQL is retained only for evaluation. Retrieval workload patterns must be mined "
            "from train_questions.jsonl only."
        ),
    }
    (output / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dev-source", type=Path, required=True)
    parser.add_argument("--dev-schemas", type=Path, required=True)
    parser.add_argument("--database-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--train-source", type=Path)
    parser.add_argument("--train-schemas", type=Path)
    parser.add_argument("--train-database-root", type=Path)
    args = parser.parse_args()
    print(
        json.dumps(
            prepare(
                args.dev_source,
                args.dev_schemas,
                args.database_root,
                args.output,
                args.train_source,
                args.train_schemas,
                args.train_database_root,
            ),
            ensure_ascii=False,
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
