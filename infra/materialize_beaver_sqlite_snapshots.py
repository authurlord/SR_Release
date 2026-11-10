#!/usr/bin/env python3
"""Materialize BEAVER MySQL databases as SQLite inputs for SQLite-only authors code.

The export is a storage/dialect compatibility layer: it copies the current tables,
columns, declared primary/foreign keys, and values without adding descriptions or
SchemaRecovery evidence.  Formal scoring remains on the original MySQL databases.
"""

from __future__ import annotations

import argparse
from datetime import date, datetime, time
from decimal import Decimal
import os
from pathlib import Path
import sqlite3
from typing import Any


def quote(identifier: str) -> str:
    return '"' + str(identifier).replace('"', '""') + '"'


def sqlite_type(mysql_type: str) -> str:
    value = mysql_type.casefold()
    if any(token in value for token in ("int", "bit", "bool")):
        return "INTEGER"
    if any(token in value for token in ("real", "float", "double")):
        return "REAL"
    if any(token in value for token in ("decimal", "numeric")):
        return "NUMERIC"
    if any(token in value for token in ("blob", "binary")):
        return "BLOB"
    return "TEXT"


def sqlite_value(value: Any) -> Any:
    if isinstance(value, Decimal):
        return str(value)
    if isinstance(value, (datetime, date, time)):
        return value.isoformat(sep=" ") if isinstance(value, datetime) else value.isoformat()
    if isinstance(value, (str, bytes, int, float)) or value is None:
        return value
    return str(value)


def fetch_schema(connection: Any, database: str) -> tuple[list[str], dict[str, list[dict[str, Any]]], dict[str, list[dict[str, str]]]]:
    def normalized(row: dict[str, Any]) -> dict[str, Any]:
        return {str(key).casefold(): value for key, value in row.items()}

    cursor = connection.cursor(dictionary=True)
    cursor.execute(
        "SELECT table_name FROM information_schema.tables "
        "WHERE table_schema=%s ORDER BY table_name",
        (database,),
    )
    tables = [str(normalized(row)["table_name"]) for row in cursor.fetchall()]
    cursor.execute(
        "SELECT table_name,column_name,column_type,is_nullable,column_key,ordinal_position "
        "FROM information_schema.columns WHERE table_schema=%s "
        "ORDER BY table_name,ordinal_position",
        (database,),
    )
    columns: dict[str, list[dict[str, Any]]] = {table: [] for table in tables}
    for raw_row in cursor.fetchall():
        row = normalized(raw_row)
        columns[str(row["table_name"])].append(
            {
                "name": str(row["column_name"]),
                "type": str(row["column_type"]),
                "nullable": str(row["is_nullable"]).upper() == "YES",
                "primary": str(row["column_key"]).upper() == "PRI",
                "ordinal": int(row["ordinal_position"]),
            }
        )
    cursor.execute(
        "SELECT table_name,column_name,referenced_table_name,referenced_column_name "
        "FROM information_schema.key_column_usage "
        "WHERE table_schema=%s AND referenced_table_name IS NOT NULL "
        "ORDER BY table_name,ordinal_position",
        (database,),
    )
    foreign_keys: dict[str, list[dict[str, str]]] = {table: [] for table in tables}
    for raw_row in cursor.fetchall():
        row = normalized(raw_row)
        foreign_keys[str(row["table_name"])].append(
            {
                "column": str(row["column_name"]),
                "target_table": str(row["referenced_table_name"]),
                "target_column": str(row["referenced_column_name"]),
            }
        )
    cursor.close()
    return tables, columns, foreign_keys


def create_table(
    sqlite_connection: sqlite3.Connection,
    table: str,
    columns: list[dict[str, Any]],
    foreign_keys: list[dict[str, str]],
) -> None:
    primary = [column["name"] for column in columns if column["primary"]]
    definitions = []
    for column in columns:
        suffix = " NOT NULL" if not column["nullable"] else ""
        if len(primary) == 1 and column["name"] == primary[0]:
            suffix += " PRIMARY KEY"
        definitions.append(
            f"{quote(column['name'])} {sqlite_type(column['type'])}{suffix}"
        )
    if len(primary) > 1:
        definitions.append("PRIMARY KEY (" + ", ".join(quote(item) for item in primary) + ")")
    for edge in foreign_keys:
        definitions.append(
            f"FOREIGN KEY ({quote(edge['column'])}) REFERENCES "
            f"{quote(edge['target_table'])} ({quote(edge['target_column'])})"
        )
    sqlite_connection.execute(
        f"CREATE TABLE {quote(table)} (" + ", ".join(definitions) + ")"
    )


def export_database(
    mysql_connection: Any,
    database: str,
    target: Path,
    batch_size: int,
) -> None:
    if target.is_file():
        print(f"[beaver-sqlite {database}] already complete", flush=True)
        return
    target.parent.mkdir(parents=True, exist_ok=True)
    temporary = target.with_suffix(target.suffix + ".partial")
    if temporary.exists():
        temporary.unlink()
    tables, columns, foreign_keys = fetch_schema(mysql_connection, database)
    sqlite_connection = sqlite3.connect(temporary)
    try:
        sqlite_connection.execute("PRAGMA journal_mode=OFF")
        sqlite_connection.execute("PRAGMA synchronous=OFF")
        sqlite_connection.execute("PRAGMA foreign_keys=OFF")
        for table in tables:
            if not columns.get(table):
                continue
            create_table(sqlite_connection, table, columns[table], foreign_keys[table])
        sqlite_connection.commit()
        for index, table in enumerate(tables, start=1):
            table_columns = columns.get(table) or []
            if not table_columns:
                continue
            names = [column["name"] for column in table_columns]
            mysql_cursor = mysql_connection.cursor(buffered=False)
            mysql_cursor.execute(
                f"SELECT {', '.join('`' + name.replace('`', '``') + '`' for name in names)} "
                f"FROM `{database.replace('`', '``')}`.`{table.replace('`', '``')}`"
            )
            placeholders = ",".join("?" for _ in names)
            insert_sql = (
                f"INSERT INTO {quote(table)} ("
                + ",".join(quote(name) for name in names)
                + f") VALUES ({placeholders})"
            )
            copied = 0
            while True:
                rows = mysql_cursor.fetchmany(batch_size)
                if not rows:
                    break
                sqlite_connection.executemany(
                    insert_sql,
                    [tuple(sqlite_value(value) for value in row) for row in rows],
                )
                copied += len(rows)
                sqlite_connection.commit()
            mysql_cursor.close()
            print(
                f"[beaver-sqlite {database} {index}/{len(tables)}] "
                f"{table} rows={copied}",
                flush=True,
            )
        sqlite_connection.execute("PRAGMA optimize")
        sqlite_connection.commit()
    finally:
        sqlite_connection.close()
    temporary.replace(target)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument("--database", action="append", default=[])
    parser.add_argument("--mysql-host", default="127.0.0.1")
    parser.add_argument("--mysql-port", type=int, default=3306)
    parser.add_argument("--mysql-user", default="root")
    parser.add_argument("--mysql-password-env", default="BEAVER_MYSQL_PASSWORD")
    parser.add_argument("--batch-size", type=int, default=2000)
    args = parser.parse_args()
    databases = args.database or ["dw", "nova", "neutron"]
    password = os.environ.get(args.mysql_password_env)
    if password is None:
        raise RuntimeError(f"missing environment variable: {args.mysql_password_env}")
    import mysql.connector

    connection = mysql.connector.connect(
        host=args.mysql_host,
        port=args.mysql_port,
        user=args.mysql_user,
        password=password,
        connection_timeout=10,
    )
    try:
        for database in databases:
            export_database(
                connection,
                database,
                args.output_root / database / f"{database}.sqlite",
                args.batch_size,
            )
    finally:
        connection.close()


if __name__ == "__main__":
    main()
