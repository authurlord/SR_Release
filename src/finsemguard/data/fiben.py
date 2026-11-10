from __future__ import annotations

import argparse
import csv
import hashlib
import json
import os
import re
import sqlite3
import subprocess
from collections.abc import Iterable
from pathlib import Path
from typing import Any


CREATE_RE = re.compile(r"^CREATE\s+TABLE\s+([A-Za-z0-9_]+)\s*\(", re.IGNORECASE)


def stable_split(unique_query_id: int) -> str:
    digest = hashlib.sha256(f"fiben:{unique_query_id}".encode()).hexdigest()
    bucket = int(digest[:8], 16) % 100
    if bucket < 70:
        return "train"
    if bucket < 85:
        return "dev"
    return "test"


def create_statements(ddl_path: Path) -> list[str]:
    statements = []
    for line in ddl_path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if CREATE_RE.match(line):
            statements.append(line)
    return statements


def iter_batches(reader: Iterable[list[str]], size: int = 10_000) -> Iterable[list[list[str]]]:
    batch: list[list[str]] = []
    for row in reader:
        batch.append(row)
        if len(batch) >= size:
            yield batch
            batch = []
    if batch:
        yield batch


def build_sqlite(source: Path, csv_root: Path, target: Path) -> dict[str, int]:
    target.parent.mkdir(parents=True, exist_ok=True)
    temp = target.with_suffix(".sqlite.tmp")
    if temp.exists():
        temp.unlink()

    counts: dict[str, int] = {}
    conn = sqlite3.connect(temp)
    try:
        conn.execute("PRAGMA journal_mode=OFF")
        conn.execute("PRAGMA synchronous=OFF")
        conn.execute("PRAGMA foreign_keys=OFF")
        for statement in create_statements(source / "FIBEN.sql"):
            conn.execute(statement)

        tables = (source / "tablelist.txt").read_text(encoding="utf-8").split()
        for table in tables:
            columns = conn.execute(f'PRAGMA table_info("{table}")').fetchall()
            if not columns:
                raise RuntimeError(f"DDL did not create table {table}")
            placeholders = ",".join("?" for _ in columns)
            insert_sql = f'INSERT INTO "{table}" VALUES ({placeholders})'
            csv_path = csv_root / f"{table}.csv"
            inserted = 0
            with csv_path.open("r", encoding="utf-8", newline="") as handle:
                reader = csv.reader(handle)
                for batch in iter_batches(reader):
                    bad = next((row for row in batch if len(row) != len(columns)), None)
                    if bad is not None:
                        raise RuntimeError(
                            f"{table}: CSV width {len(bad)} != DDL width {len(columns)}"
                        )
                    conn.executemany(insert_sql, batch)
                    inserted += len(batch)
            counts[table] = inserted
            conn.commit()

        conn.execute(
            "CREATE TABLE _finsemguard_meta (key TEXT PRIMARY KEY, value TEXT NOT NULL)"
        )
        conn.executemany(
            "INSERT INTO _finsemguard_meta VALUES (?, ?)",
            [
                ("dataset", "FIBEN"),
                ("source", "IBM/fiben-benchmark"),
                ("read_only_expected", "true"),
            ],
        )
        conn.commit()
    finally:
        conn.close()

    os.replace(temp, target)
    return counts


def write_questions(source: Path, target: Path) -> dict[str, int]:
    questions: list[dict[str, Any]] = json.loads(
        (source / "FIBEN_Queries.json").read_text(encoding="utf-8")
    )
    counts = {"train": 0, "dev": 0, "test": 0}
    with target.open("w", encoding="utf-8") as handle:
        for row_id, row in enumerate(questions, start=1):
            split = stable_split(int(row["uniqueQueryID"]))
            counts[split] += 1
            record = {
                "question_id": f"fiben_{row_id:04d}",
                "unique_query_id": int(row["uniqueQueryID"]),
                "question": row["question"].strip(),
                "sql": row["SQL"].strip(),
                "query_type": row["queryType"],
                "is_paraphrased": bool(row["isParaphrased"]),
                "split": split,
            }
            handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    return counts


def build_catalog(database: Path, target: Path) -> dict[str, int]:
    conn = sqlite3.connect(f"file:{database}?mode=ro", uri=True)
    table_count = column_count = 0
    with target.open("w", encoding="utf-8") as handle:
        tables = [
            row[0]
            for row in conn.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE '_finsemguard_%' ORDER BY name"
            )
        ]
        for table in tables:
            columns = conn.execute(f'PRAGMA table_info("{table}")').fetchall()
            row_count = conn.execute(f'SELECT COUNT(*) FROM "{table}"').fetchone()[0]
            table_doc = {
                "doc_id": f"fiben.table.{table.lower()}",
                "kind": "table",
                "dataset": "fiben",
                "split_origin": "schema",
                "name": table,
                "text": f"FIBEN financial table {table}; rows={row_count}; columns="
                + ", ".join(column[1] for column in columns),
                "table": table,
                "column": None,
                "metadata": {"row_count": row_count, "column_count": len(columns)},
            }
            handle.write(json.dumps(table_doc, ensure_ascii=False) + "\n")
            table_count += 1
            for _, name, data_type, not_null, _, pk in columns:
                column_doc = {
                    "doc_id": f"fiben.column.{table.lower()}.{name.lower()}",
                    "kind": "column",
                    "dataset": "fiben",
                    "split_origin": "schema",
                    "name": f"{table}.{name}",
                    "text": f"FIBEN column {table}.{name}; type={data_type}; primary_key={bool(pk)}; not_null={bool(not_null)}",
                    "table": table,
                    "column": name,
                    "metadata": {
                        "data_type": data_type,
                        "primary_key": bool(pk),
                        "not_null": bool(not_null),
                    },
                }
                handle.write(json.dumps(column_doc, ensure_ascii=False) + "\n")
                column_count += 1
    conn.close()
    return {"tables": table_count, "columns": column_count}


def git_revision(source: Path) -> str | None:
    try:
        return subprocess.check_output(
            ["git", "-C", str(source), "rev-parse", "HEAD"], text=True
        ).strip()
    except (subprocess.CalledProcessError, FileNotFoundError):
        return None


def prepare(source: Path, output: Path) -> dict[str, Any]:
    output.mkdir(parents=True, exist_ok=True)
    csv_root = output / "data"
    if not csv_root.is_dir():
        raise FileNotFoundError(
            f"Expected extracted CSV directory at {csv_root}; extract data.zip first"
        )
    database = output / "fiben.sqlite"
    row_counts = build_sqlite(source, csv_root, database)
    split_counts = write_questions(source, output / "questions.jsonl")
    catalog_counts = build_catalog(database, output / "catalog.jsonl")
    manifest = {
        "dataset": "FIBEN",
        "source": "https://github.com/IBM/fiben-benchmark",
        "source_revision": git_revision(source),
        "license": "Apache-2.0",
        "database": str(database),
        "tables": len(row_counts),
        "rows": sum(row_counts.values()),
        "non_empty_tables": sum(count > 0 for count in row_counts.values()),
        "questions": sum(split_counts.values()),
        "splits": split_counts,
        "catalog": catalog_counts,
        "split_policy": "sha256(uniqueQueryID), 70/15/15; paraphrases grouped",
    }
    (output / "manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    return manifest


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    prep = sub.add_parser("prepare")
    prep.add_argument("--source", type=Path, required=True)
    prep.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.command == "prepare":
        print(json.dumps(prepare(args.source.resolve(), args.output.resolve()), indent=2))


if __name__ == "__main__":
    main()

