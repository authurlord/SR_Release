#!/usr/bin/env python3
"""Materialize EvoSchema virtual-current catalogs as physical SQLite databases.

EvoSchema releases relation-changing mappings without rewritten database files.
This utility applies the released current snapshot and the project's structural
storage translation once, before an external authors-code method runs.  The
result contains only the current physical schema and values; mapping/lineage and
gold SQL are not copied into the baseline input directory.
"""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
from pathlib import Path
import shutil
import sqlite3
from typing import Any

from finsemguard.e2e.evoschema import TableSchema, read_sqlite_snapshot
from finsemguard.e2e.evolution_relations import (
    RelationEvolutionMapping,
    _relation_select_sql,
    snapshot_to_json,
)


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    return [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]


def quote(identifier: str) -> str:
    return '"' + str(identifier).replace('"', '""') + '"'


def comparable_snapshot(snapshot: Any) -> dict[str, Any]:
    """Return a semantic schema view insensitive to catalog/FK row order."""

    value = snapshot_to_json(snapshot)
    for table in value["tables"]:
        table["foreign_keys"] = sorted(
            table["foreign_keys"],
            key=lambda edge: (
                edge["source_column"],
                edge["target_table"],
                edge["target_column"],
            ),
        )
    value["tables"] = sorted(
        value["tables"], key=lambda table: (table["name"].casefold(), table["name"])
    )
    return value


def create_table_sql(
    table: TableSchema, *, enforce_primary_key: bool = True
) -> str:
    primary = [
        column.name
        for column in sorted(
            table.columns,
            key=lambda column: column.primary_key_ordinal or 10**9,
        )
        if enforce_primary_key and column.primary_key_ordinal > 0
    ]
    definitions: list[str] = []
    for column in table.columns:
        suffix = " NOT NULL" if column.not_null else ""
        if len(primary) == 1 and column.name == primary[0]:
            suffix += " PRIMARY KEY"
        definitions.append(
            f"{quote(column.name)} {column.declared_type or 'TEXT'}{suffix}"
        )
    if len(primary) > 1:
        definitions.append(
            "PRIMARY KEY (" + ", ".join(quote(name) for name in primary) + ")"
        )
    definitions.extend(
        f"FOREIGN KEY ({quote(edge.source_column)}) REFERENCES "
        f"{quote(edge.target_table)} ({quote(edge.target_column)})"
        for edge in table.foreign_keys
    )
    return f"CREATE TABLE {quote(table.name)} (" + ", ".join(definitions) + ")"


def stage_satisfies_primary_key(
    connection: sqlite3.Connection, stage: str, table: TableSchema
) -> bool:
    primary = [
        column.name
        for column in sorted(
            table.columns,
            key=lambda column: column.primary_key_ordinal or 10**9,
        )
        if column.primary_key_ordinal > 0
    ]
    if not primary:
        return True
    null_predicate = " OR ".join(f"{quote(name)} IS NULL" for name in primary)
    if connection.execute(
        f"SELECT 1 FROM {quote(stage)} WHERE {null_predicate} LIMIT 1"
    ).fetchone():
        return False
    names = ", ".join(quote(name) for name in primary)
    return (
        connection.execute(
            f"SELECT 1 FROM {quote(stage)} GROUP BY {names} "
            "HAVING COUNT(*) > 1 LIMIT 1"
        ).fetchone()
        is None
    )


def relax_primary_keys(
    snapshot: Any, table_names: set[str]
) -> dict[str, Any]:
    value = comparable_snapshot(snapshot)
    folded = {name.casefold() for name in table_names}
    for table in value["tables"]:
        if table["name"].casefold() not in folded:
            continue
        for column in table["columns"]:
            column["primary_key"] = False
            column["primary_key_ordinal"] = 0
    return value


def materialize_one(
    row: dict[str, Any],
    runtime: dict[str, Any],
    *,
    repo_root: Path,
    output_root: Path,
) -> dict[str, Any]:
    example_id = str(row["example_id"])
    source_database_id = str(row["source_database_id"])
    source = (
        repo_root
        / "data/processed/bird_full_dev/dev_databases"
        / source_database_id
        / f"{source_database_id}.sqlite"
    ).resolve()
    target_dir = output_root / example_id
    target = target_dir / f"{example_id}.sqlite"
    if target.is_file():
        return {"example_id": example_id, "status": "existing"}
    target_dir.mkdir(parents=True, exist_ok=True)
    temporary = target.with_suffix(target.suffix + ".partial")
    if temporary.exists():
        temporary.unlink()
    shutil.copy2(source, temporary)
    mapping = RelationEvolutionMapping.from_json(dict(runtime["mapping"]))
    source_snapshot = read_sqlite_snapshot(temporary)
    source_by_name = {table.name.casefold(): table for table in source_snapshot.tables}
    current_by_name = {
        table.name.casefold(): table for table in mapping.current_snapshot.tables
    }
    rebuild = {
        table.name
        for table in mapping.current_snapshot.tables
        if source_by_name.get(table.name.casefold()) != table
        or table.name in mapping.table_sources
    }
    removed = {
        table.name
        for table in source_snapshot.tables
        if table.name.casefold() not in current_by_name
    }
    connection = sqlite3.connect(temporary)
    relaxed_primary_keys: set[str] = set()
    try:
        connection.execute("PRAGMA foreign_keys=OFF")
        stage_names: dict[str, str] = {}
        for index, table_name in enumerate(sorted(rebuild), start=1):
            table = mapping.current_snapshot.by_name[table_name]
            stage = f"__schema_recovery_current_stage_{index:04d}"
            stage_names[table_name] = stage
            if table_name in mapping.table_sources:
                select_sql = _relation_select_sql(table_name, mapping)
            else:
                select_sql = (
                    "SELECT "
                    + ", ".join(quote(column.name) for column in table.columns)
                    + f" FROM {quote(table_name)}"
                )
            connection.execute(
                f"CREATE TABLE {quote(stage)} AS "
                f"SELECT {', '.join(quote(column.name) for column in table.columns)} "
                f"FROM ({select_sql})"
            )
        for view_name, in connection.execute(
            "SELECT name FROM sqlite_master WHERE type='view' ORDER BY name"
        ).fetchall():
            connection.execute(f"DROP VIEW {quote(str(view_name))}")
        for table_name in sorted(removed | rebuild):
            exists = connection.execute(
                "SELECT 1 FROM sqlite_master WHERE type='table' AND lower(name)=lower(?)",
                (table_name,),
            ).fetchone()
            if exists:
                connection.execute(f"DROP TABLE {quote(table_name)}")
        for table_name in sorted(rebuild):
            table = mapping.current_snapshot.by_name[table_name]
            enforce_primary_key = stage_satisfies_primary_key(
                connection, stage_names[table_name], table
            )
            if not enforce_primary_key:
                relaxed_primary_keys.add(table_name)
            connection.execute(
                create_table_sql(table, enforce_primary_key=enforce_primary_key)
            )
            names = ", ".join(quote(column.name) for column in table.columns)
            connection.execute(
                f"INSERT INTO {quote(table_name)} ({names}) "
                f"SELECT {names} FROM {quote(stage_names[table_name])}"
            )
            connection.execute(f"DROP TABLE {quote(stage_names[table_name])}")
        connection.commit()
        connection.execute("PRAGMA optimize")
        connection.commit()
    finally:
        connection.close()
    actual = read_sqlite_snapshot(temporary)
    expected = relax_primary_keys(mapping.current_snapshot, relaxed_primary_keys)
    if comparable_snapshot(actual) != expected:
        raise ValueError(f"materialized current schema differs for {example_id}")
    temporary.replace(target)
    return {
        "example_id": example_id,
        "source_database_id": source_database_id,
        "status": "materialized",
        "rebuilt_tables": len(rebuild),
        "removed_tables": len(removed),
        "relaxed_primary_keys": len(relaxed_primary_keys),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--online", type=Path, required=True)
    parser.add_argument("--runtime", type=Path, required=True)
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument("--workers", type=int, default=2)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--example-id", action="append", default=[])
    args = parser.parse_args()
    online = load_jsonl(args.online)
    if args.example_id:
        selected = set(args.example_id)
        online = [row for row in online if str(row["example_id"]) in selected]
        found = {str(row["example_id"]) for row in online}
        if found != selected:
            raise ValueError(f"unknown example IDs: {sorted(selected - found)}")
    if args.limit is not None:
        online = online[: args.limit]
    runtime = {str(row["example_id"]): row for row in load_jsonl(args.runtime)}
    missing = [row["example_id"] for row in online if str(row["example_id"]) not in runtime]
    if missing:
        raise ValueError(f"runtime mappings missing: {missing[:5]}")
    results = []
    with ThreadPoolExecutor(max_workers=max(1, args.workers)) as pool:
        futures = {
            pool.submit(
                materialize_one,
                row,
                runtime[str(row["example_id"])],
                repo_root=args.repo_root.resolve(),
                output_root=args.output_root,
            ): str(row["example_id"])
            for row in online
        }
        for index, future in enumerate(as_completed(futures), start=1):
            result = future.result()
            results.append(result)
            print(
                f"[evoschema-current {index}/{len(futures)}] "
                f"{result['example_id']} {result['status']}",
                flush=True,
            )
    print(
        json.dumps(
            {
                "rows": len(results),
                "materialized": sum(row["status"] == "materialized" for row in results),
                "existing": sum(row["status"] == "existing" for row in results),
                "relaxed_primary_keys": sum(
                    int(row.get("relaxed_primary_keys") or 0) for row in results
                ),
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
