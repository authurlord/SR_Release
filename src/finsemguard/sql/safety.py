from __future__ import annotations

import sqlite3
import time
from pathlib import Path
from typing import Any

import sqlglot
from sqlglot import exp


class SQLSafetyError(ValueError):
    pass


DENIED = (
    exp.Insert,
    exp.Update,
    exp.Delete,
    exp.Create,
    exp.Drop,
    exp.Alter,
    exp.Command,
    exp.Merge,
)


def validate_readonly(sql: str, allowed_tables: set[str] | None = None) -> dict[str, Any]:
    statements = sqlglot.parse(sql, read="postgres")
    if len(statements) != 1:
        raise SQLSafetyError("exactly one SQL statement is required")
    tree = statements[0]
    if any(isinstance(node, DENIED) for node in tree.walk()):
        raise SQLSafetyError("mutating or administrative SQL is forbidden")
    if not isinstance(tree, (exp.Select, exp.Union, exp.Intersect, exp.Except)) and tree.find(exp.Select) is None:
        raise SQLSafetyError("only SELECT queries are allowed")
    cte_names = {
        cte.alias_or_name.upper()
        for cte in tree.find_all(exp.CTE)
        if cte.alias_or_name
    }
    tables = {
        table.name.upper()
        for table in tree.find_all(exp.Table)
        if table.name.upper() not in cte_names
    }
    if allowed_tables is not None:
        unknown = tables - {name.upper() for name in allowed_tables}
        if unknown:
            raise SQLSafetyError(f"tables outside allowlist: {sorted(unknown)}")
    return {
        "valid": True,
        "tables": sorted(tables),
        "normalized_sql": tree.sql(dialect="postgres", pretty=False),
    }


def sqlite_tables(database: Path) -> set[str]:
    conn = sqlite3.connect(f"file:{database}?mode=ro", uri=True)
    try:
        return {
            row[0]
            for row in conn.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE '_finsemguard_%'"
            )
        }
    finally:
        conn.close()


def execute_preview(
    database: Path,
    sql: str,
    max_rows: int = 500,
    timeout_seconds: float = 20.0,
) -> dict[str, Any]:
    if max_rows < 1:
        raise ValueError("max_rows must be positive")
    if timeout_seconds <= 0:
        raise ValueError("timeout_seconds must be positive")
    validation = validate_readonly(sql, sqlite_tables(database))
    tree = sqlglot.parse_one(sql, read="postgres")
    sqlite_sql = tree.sql(dialect="sqlite", pretty=False)
    bounded_sql = (
        f"SELECT * FROM ({sqlite_sql}) AS _finsemguard_preview "
        f"LIMIT {max_rows + 1}"
    )

    conn = sqlite3.connect(":memory:", uri=True)
    try:
        uri = f"file:{database.resolve()}?mode=ro"
        escaped = uri.replace("'", "''")
        conn.execute(f"ATTACH DATABASE '{escaped}' AS FIBEN")
        conn.execute("PRAGMA query_only=ON")
        deadline = time.monotonic() + timeout_seconds

        def progress() -> int:
            return int(time.monotonic() > deadline)

        conn.set_progress_handler(progress, 1_000)
        cursor = conn.execute(bounded_sql)
        rows = cursor.fetchmany(max_rows + 1)
        truncated = len(rows) > max_rows
        rows = rows[:max_rows]
        columns = [item[0] for item in cursor.description or []]
        return {
            "columns": columns,
            "rows": rows,
            "row_count": len(rows),
            "truncated": truncated,
            "sqlite_sql": sqlite_sql,
            "bounded_sql": bounded_sql,
            "timeout_seconds": timeout_seconds,
            "validation": validation,
        }
    finally:
        conn.close()
