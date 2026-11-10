from __future__ import annotations

import json
from pathlib import Path
import sqlite3
from typing import Any, Iterable, Literal

from finsemguard.e2e.livesqlbench import CatalogDocument


def _quote(identifier: str) -> str:
    return '"' + identifier.replace('"', '""') + '"'


def schema_key(row: dict[str, Any]) -> str:
    dataset_id = str(row["dataset_id"])
    database_id = str(row["database_id"])
    if dataset_id == "dr_spider":
        return f"{row['schema_manifest']}::{database_id}"
    return database_id


def _spider_documents(
    schema_key_value: str,
    schema: dict[str, Any],
    *,
    include_column_documents: bool,
    schema_view: Literal["released", "physical"] = "released",
) -> list[CatalogDocument]:
    if schema_view not in {"released", "physical"}:
        raise ValueError(f"unsupported Spider schema view: {schema_view}")
    physical_tables = [str(value) for value in schema["table_names_original"]]
    physical_columns = schema["column_names_original"]
    if schema_view == "released":
        semantic_tables = [
            str(value) for value in schema.get("table_names", physical_tables)
        ]
        semantic_columns = schema.get("column_names", physical_columns)
        alternative_columns = schema.get(
            "column_names_manually_normalized_alternative", []
        )
        descriptions = schema.get("column_descriptions", [])
    else:
        # The physical view deliberately never reads released semantic labels,
        # normalized alternatives, or descriptions.  It is the gold-blind base
        # catalog onto which automatic recovery predictions may be compiled.
        semantic_tables = physical_tables
        semantic_columns = physical_columns
        alternative_columns = []
        descriptions = []
    types = schema.get("column_types", [])
    primary_keys: set[int] = set()
    for value in schema.get("primary_keys", []):
        if isinstance(value, list):
            primary_keys.update(int(item) for item in value)
        else:
            primary_keys.add(int(value))
    foreign_keys = {int(source): int(target) for source, target in schema.get("foreign_keys", [])}
    output: list[CatalogDocument] = []
    for table_index, physical_table in enumerate(physical_tables):
        column_lines: list[str] = []
        references: list[str] = []
        table_columns: list[tuple[int, str, str, str, str, str]] = []
        for column_index, (owner, physical_column) in enumerate(physical_columns):
            if int(owner) != table_index:
                continue
            semantic_column = str(semantic_columns[column_index][1])
            alternative = (
                str(alternative_columns[column_index][1])
                if column_index < len(alternative_columns)
                else ""
            )
            description = (
                str(descriptions[column_index]) if column_index < len(descriptions) else ""
            )
            column_type = str(types[column_index]) if column_index < len(types) else ""
            table_columns.append(
                (
                    column_index,
                    str(physical_column),
                    semantic_column,
                    alternative,
                    description,
                    column_type,
                )
            )
        for column_index, physical_column, semantic_column, alternative, description, column_type in table_columns:
            annotations = []
            if semantic_column.casefold() != physical_column.casefold():
                annotations.append(f"semantic label: {semantic_column}")
            if alternative and alternative.casefold() not in {
                semantic_column.casefold(),
                physical_column.casefold(),
            }:
                annotations.append(f"normalized label: {alternative}")
            if description and description != "*":
                annotations.append(f"description: {description}")
            if column_index in primary_keys:
                annotations.append("PRIMARY KEY")
            target_index = foreign_keys.get(column_index)
            if target_index is not None:
                target_owner, target_column = physical_columns[target_index]
                target_table = physical_tables[int(target_owner)]
                annotations.append(
                    f"REFERENCES {_quote(target_table)}({_quote(str(target_column))})"
                )
                references.append(target_table)
            suffix = f" -- {'; '.join(annotations)}" if annotations else ""
            column_lines.append(
                f"  {_quote(physical_column)} {column_type or 'unknown'}{suffix}"
            )
            if include_column_documents:
                facts = [
                    f"physical SQLite identifier: {_quote(physical_table)}.{_quote(physical_column)}",
                    f"type: {column_type or 'unknown'}",
                ]
                if schema_view == "released" and semantic_column:
                    facts.append(f"semantic label: {semantic_column}")
                if alternative:
                    facts.append(f"normalized label: {alternative}")
                if description and description != "*":
                    facts.append(f"description: {description}")
                output.append(
                    CatalogDocument(
                        candidate_id=(
                            f"column::{schema_key_value}::{physical_table}::{physical_column}"
                        ),
                        database_id=schema_key_value,
                        kind="column",
                        table=physical_table,
                        name=f"{physical_table}.{physical_column}",
                        text="\n".join(facts),
                    )
                )
        semantic_table = semantic_tables[table_index]
        heading = f"physical SQLite table: {_quote(physical_table)}"
        if semantic_table.casefold() != physical_table.casefold():
            heading += f"; semantic label: {semantic_table}"
        table_text = "\n".join(
            [heading, f"CREATE TABLE {_quote(physical_table)} (", *column_lines, ");"]
        )
        output.append(
            CatalogDocument(
                candidate_id=f"table::{schema_key_value}::{physical_table}",
                database_id=schema_key_value,
                kind="table",
                table=physical_table,
                name=physical_table,
                text=table_text,
                references=tuple(dict.fromkeys(references)),
            )
        )
    return output


def _jsonl(path: Path) -> Iterable[dict[str, Any]]:
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                yield json.loads(line)


def load_dr_spider_catalog(
    root: Path,
    online_rows: list[dict[str, Any]],
    *,
    schema_view: Literal["released", "physical"] = "released",
) -> list[CatalogDocument]:
    requested: dict[str, set[str]] = {}
    for row in online_rows:
        requested.setdefault(str(row["schema_manifest"]), set()).add(
            str(row["database_id"])
        )
    output: list[CatalogDocument] = []
    for relative_path, database_ids in sorted(requested.items()):
        schema_rows = json.loads((root / relative_path).read_text(encoding="utf-8"))
        schema_by_id = {str(row["db_id"]): row for row in schema_rows}
        for database_id in sorted(database_ids):
            output.extend(
                _spider_documents(
                    f"{relative_path}::{database_id}",
                    schema_by_id[database_id],
                    include_column_documents=True,
                    schema_view=schema_view,
                )
            )
    return output


def load_kaggledbqa_catalog(
    root: Path,
    online_rows: list[dict[str, Any]],
    *,
    schema_view: Literal["released", "physical"] = "released",
) -> list[CatalogDocument]:
    schemas = json.loads((root / "KaggleDBQA_tables.json").read_text(encoding="utf-8"))
    requested = {str(row["database_id"]) for row in online_rows}
    output: list[CatalogDocument] = []
    for schema in schemas:
        database_id = str(schema["db_id"])
        if database_id not in requested:
            continue
        overview = str(schema.get("db_overview") or "").strip()
        documents = _spider_documents(
            database_id,
            schema,
            include_column_documents=True,
            schema_view=schema_view,
        )
        if schema_view == "released" and overview:
            documents.append(
                CatalogDocument(
                    candidate_id=f"knowledge::{database_id}::overview",
                    database_id=database_id,
                    kind="knowledge",
                    table=None,
                    name=f"{database_id} overview",
                    text=overview,
                )
            )
        output.extend(documents)
    return output


def load_bird_catalog(
    root: Path,
    online_rows: list[dict[str, Any]],
    *,
    schema_view: Literal["released", "physical"] = "physical",
) -> list[CatalogDocument]:
    requested: dict[str, set[str]] = {}
    for row in online_rows:
        relative = str(row.get("schema_manifest") or "data/raw/bird_full_dev/dev_tables.json")
        requested.setdefault(relative, set()).add(str(row["database_id"]))
    output: list[CatalogDocument] = []
    for relative, database_ids in sorted(requested.items()):
        schema_rows = json.loads((root / relative).read_text(encoding="utf-8"))
        schema_by_id = {str(row["db_id"]): row for row in schema_rows}
        for database_id in sorted(database_ids):
            if database_id not in schema_by_id:
                raise KeyError(f"BIRD schema not found: {database_id}")
            output.extend(
                _spider_documents(
                    database_id,
                    schema_by_id[database_id],
                    include_column_documents=True,
                    schema_view=schema_view,
                )
            )
    return output


def load_llmsql_catalog(root: Path) -> list[CatalogDocument]:
    output: list[CatalogDocument] = []
    for row in _jsonl(root / "tables.jsonl"):
        table_id = str(row["table_id"])
        headers = [str(value) for value in row["header"]]
        types = [str(value) for value in row.get("types", [])]
        rows = row.get("rows", [])
        sample_row = rows[0] if isinstance(rows, list) and rows else []
        columns = [
            f"  {_quote(header)} {types[index] if index < len(types) else 'text'}"
            for index, header in enumerate(headers)
        ]
        metadata = [
            f"physical SQLite table: {_quote(table_id)}",
            f"page title: {row.get('page_title', '')}",
            f"section title: {row.get('section_title', '')}",
            f"caption: {row.get('caption', '')}",
            (
                "official released sample row (aligned to the columns above): "
                + json.dumps(sample_row, ensure_ascii=False)
            ),
            f"CREATE TABLE {_quote(table_id)} (",
            *columns,
            ");",
        ]
        output.append(
            CatalogDocument(
                candidate_id=f"table::{table_id}::{table_id}",
                database_id=table_id,
                kind="table",
                table=table_id,
                name=table_id,
                text="\n".join(metadata),
            )
        )
    return output


def load_fiben_catalog(root: Path, online_rows: list[dict[str, Any]]) -> list[CatalogDocument]:
    """Build a physical-only catalog from the local FIBEN SQLite database."""

    if {str(row["database_id"]) for row in online_rows} != {"fiben"}:
        raise ValueError("FIBEN online rows must use database_id=fiben")
    database = root / "fiben.sqlite"
    if not database.is_file():
        raise FileNotFoundError(f"FIBEN SQLite database not found: {database}")
    connection = sqlite3.connect(f"file:{database.resolve()}?mode=ro", uri=True)
    try:
        tables = [
            str(row[0])
            for row in connection.execute(
                "SELECT name FROM sqlite_master WHERE type='table' "
                "AND name NOT LIKE 'sqlite_%' ORDER BY name"
            )
        ]
        output: list[CatalogDocument] = []
        for table in tables:
            columns = [
                {
                    "name": str(row[1]),
                    "type": str(row[2] or "unknown"),
                    "not_null": bool(row[3]),
                    "primary_key": bool(row[5]),
                }
                for row in connection.execute(f"PRAGMA table_info({_quote(table)})")
            ]
            foreign_keys = [
                {
                    "from": str(row[3]),
                    "to_table": str(row[2]),
                    "to_column": str(row[4]),
                }
                for row in connection.execute(
                    f"PRAGMA foreign_key_list({_quote(table)})"
                )
            ]
            references = tuple(
                dict.fromkeys(row["to_table"] for row in foreign_keys)
            )
            fk_by_column = {row["from"]: row for row in foreign_keys}
            lines = []
            for column in columns:
                annotations = []
                if column["primary_key"]:
                    annotations.append("PRIMARY KEY")
                if column["not_null"]:
                    annotations.append("NOT NULL")
                fk = fk_by_column.get(column["name"])
                if fk:
                    annotations.append(
                        f"REFERENCES {_quote(fk['to_table'])}({_quote(fk['to_column'])})"
                    )
                suffix = f" -- {'; '.join(annotations)}" if annotations else ""
                lines.append(
                    f"  {_quote(column['name'])} {column['type']}{suffix}"
                )
                output.append(
                    CatalogDocument(
                        candidate_id=f"column::fiben::{table}::{column['name']}",
                        database_id="fiben",
                        kind="column",
                        table=table,
                        name=f"{table}.{column['name']}",
                        text=(
                            f"physical SQLite identifier: {_quote(table)}."
                            f"{_quote(column['name'])}\n"
                            f"type: {column['type']}\n"
                            f"primary key: {column['primary_key']}"
                        ),
                    )
                )
            output.append(
                CatalogDocument(
                    candidate_id=f"table::fiben::{table}",
                    database_id="fiben",
                    kind="table",
                    table=table,
                    name=table,
                    text="\n".join(
                        [
                            f"physical SQLite table: {_quote(table)}",
                            f"CREATE TABLE {_quote(table)} (",
                            *lines,
                            ");",
                        ]
                    ),
                    references=references,
                )
            )
    finally:
        connection.close()
    return output


def load_catalog(
    dataset_id: str,
    root: Path,
    online_rows: list[dict[str, Any]],
    *,
    spider_schema_view: Literal["released", "physical"] = "released",
    kaggledbqa_schema_view: Literal["released", "physical"] = "released",
    bird_schema_view: Literal["released", "physical"] = "physical",
) -> list[CatalogDocument]:
    if dataset_id == "dr_spider":
        output = load_dr_spider_catalog(
            root,
            online_rows,
            schema_view=spider_schema_view,
        )
    elif dataset_id == "kaggledbqa":
        output = load_kaggledbqa_catalog(
            root,
            online_rows,
            schema_view=kaggledbqa_schema_view,
        )
    elif dataset_id == "bird":
        output = load_bird_catalog(
            root,
            online_rows,
            schema_view=bird_schema_view,
        )
    elif dataset_id == "llmsql":
        output = load_llmsql_catalog(root)
    elif dataset_id == "fiben":
        output = load_fiben_catalog(root, online_rows)
    else:
        raise ValueError(f"unsupported SQLite benchmark: {dataset_id}")
    if not output:
        raise ValueError(f"no catalog documents found for {dataset_id} under {root}")
    if len({row.candidate_id for row in output}) != len(output):
        raise ValueError(f"duplicate catalog document IDs for {dataset_id}")
    return output
