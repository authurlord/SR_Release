from __future__ import annotations

import json
import hashlib
import re
from pathlib import Path
from typing import Any

from finsemguard.baselines.autolink_spider2 import dialect_for_instance
from finsemguard.e2e.livesqlbench import CatalogDocument
from finsemguard.schema_linking.spider2_table_scale import resolve_database_directory


COLUMN_CHUNK_SIZE = 24


def _values(row: dict[str, Any], primary: str, fallback: str) -> list[Any]:
    value = row.get(primary) or row.get(fallback) or []
    return value if isinstance(value, list) else []


def table_document(
    dialect: str, database_id: str, row: dict[str, Any]
) -> CatalogDocument:
    table = str(row.get("table_fullname") or row["table_name"])
    names = _values(row, "nested_column_names", "column_names")
    types = _values(row, "nested_column_types", "column_types")
    descriptions = _values(row, "description", "descriptions")
    columns = []
    for index, raw_name in enumerate(names):
        name = str(raw_name)
        column_type = str(types[index]) if index < len(types) else ""
        description = str(descriptions[index]) if index < len(descriptions) else ""
        columns.append(
            " ".join(value for value in (name, column_type, description) if value).strip()
        )
    visible = columns[:COLUMN_CHUNK_SIZE]
    suffix = (
        f"\n{len(columns) - len(visible)} more columns are available through column chunks."
        if len(columns) > len(visible)
        else ""
    )
    text = f"{dialect} table {table}\ncolumns:\n" + "\n".join(visible) + suffix
    key = f"{dialect}::{database_id}"
    return CatalogDocument(
        candidate_id=f"table::{key}::{table}",
        database_id=key,
        kind="table",
        table=table,
        name=table,
        text=text,
    )


def column_chunk_documents(
    dialect: str,
    database_id: str,
    row: dict[str, Any],
    *,
    physical_table: str | None = None,
    id_variant: str = "",
) -> list[CatalogDocument]:
    table = physical_table or str(row.get("table_fullname") or row["table_name"])
    names = _values(row, "nested_column_names", "column_names")
    types = _values(row, "nested_column_types", "column_types")
    descriptions = _values(row, "description", "descriptions")
    columns = []
    for index, raw_name in enumerate(names):
        values = [
            str(raw_name),
            str(types[index]) if index < len(types) else "",
            str(descriptions[index]) if index < len(descriptions) else "",
        ]
        columns.append(" ".join(value for value in values if value).strip())
    key = f"{dialect}::{database_id}"
    variant = f"::{id_variant}" if id_variant else ""
    output = []
    for start in range(0, len(columns), COLUMN_CHUNK_SIZE):
        chunk_index = start // COLUMN_CHUNK_SIZE
        chunk = columns[start : start + COLUMN_CHUNK_SIZE]
        output.append(
            CatalogDocument(
                candidate_id=(
                    f"column::{key}::{table}{variant}::chunk-{chunk_index:04d}"
                ),
                database_id=key,
                kind="column",
                table=table,
                name=f"{table} columns {start + 1}-{start + len(chunk)}",
                text=(
                    f"{dialect} physical table {table}\n"
                    f"column block {start + 1}-{start + len(chunk)}:\n"
                    + "\n".join(chunk)
                ),
            )
        )
    return output


def _schema_signature(row: dict[str, Any]) -> tuple[tuple[str, str], ...]:
    names = _values(row, "nested_column_names", "column_names")
    types = _values(row, "nested_column_types", "column_types")
    return tuple(
        (
            str(name).casefold(),
            str(types[index] if index < len(types) else "").casefold(),
        )
        for index, name in enumerate(names)
    )


def _wildcard_pattern(rows: list[dict[str, Any]]) -> str | None:
    names = [str(row.get("table_fullname") or row["table_name"]) for row in rows]
    matches = [re.fullmatch(r"(.+?)(\d{6,8})", name) for name in names]
    if not all(matches):
        return None
    prefixes = {match.group(1) for match in matches if match is not None}
    return f"{prefixes.pop()}*" if len(prefixes) == 1 else None


def family_document(
    dialect: str,
    database_id: str,
    rows: list[dict[str, Any]],
    wildcard: str,
) -> CatalogDocument:
    representative = table_document(dialect, database_id, rows[0])
    signature_id = hashlib.sha256(
        repr(_schema_signature(rows[0])).encode("utf-8")
    ).hexdigest()[:12]
    members = sorted(
        str(row.get("table_fullname") or row["table_name"]) for row in rows
    )
    text = "\n".join(
        [
            f"{dialect} physical schema family with {len(members)} identically typed tables",
            f"wildcard table pattern: {wildcard}",
            "The wildcard denotes only the released physical member tables in this family.",
            f"first member: {members[0]}",
            f"last member: {members[-1]}",
            representative.text,
        ]
    )
    key = f"{dialect}::{database_id}"
    return CatalogDocument(
        candidate_id=f"family::{key}::{wildcard}::{signature_id}",
        database_id=key,
        kind="table",
        table=wildcard,
        name=f"{wildcard} schema-variant-{signature_id}",
        text=text,
    )


def family_documents(
    dialect: str,
    database_id: str,
    rows: list[dict[str, Any]],
    wildcard: str,
) -> list[CatalogDocument]:
    table = family_document(dialect, database_id, rows, wildcard)
    signature_id = table.candidate_id.rsplit("::", 1)[-1]
    return [
        table,
        *column_chunk_documents(
            dialect,
            database_id,
            rows[0],
            physical_table=wildcard,
            id_variant=signature_id,
        ),
    ]


def load_catalog(root: Path, questions: list[dict[str, Any]]) -> list[CatalogDocument]:
    database_root = root / "resource" / "databases"
    requested = {
        (dialect_for_instance(str(row["example_id"])), str(row["database_id"]))
        for row in questions
    }
    output: list[CatalogDocument] = []
    for dialect, database_id in sorted(requested):
        database_dir = resolve_database_directory(database_root / dialect, database_id)
        table_rows: list[dict[str, Any]] = []
        for path in sorted(database_dir.rglob("*.json")):
            try:
                row = json.loads(path.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, UnicodeDecodeError):
                continue
            if isinstance(row, dict) and "table_name" in row:
                table_rows.append(row)
        groups: dict[tuple[tuple[str, str], ...], list[dict[str, Any]]] = {}
        for row in table_rows:
            groups.setdefault(_schema_signature(row), []).append(row)
        for rows in groups.values():
            wildcard = _wildcard_pattern(rows)
            if len(rows) > 1 and wildcard is not None:
                output.extend(family_documents(dialect, database_id, rows, wildcard))
            else:
                for row in rows:
                    output.append(table_document(dialect, database_id, row))
                    output.extend(column_chunk_documents(dialect, database_id, row))
    if not output:
        raise ValueError(f"no Spider2 catalog documents found under {root}")
    return output


def load_allowed_document(root: Path, relative_path: str) -> str:
    path = (root / "resource" / "documents" / relative_path).resolve()
    document_root = (root / "resource" / "documents").resolve()
    if document_root not in path.parents or not path.is_file():
        raise ValueError(f"invalid Spider2 allowed document: {relative_path}")
    return path.read_text(encoding="utf-8", errors="replace")
