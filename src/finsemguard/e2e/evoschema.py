"""Executable virtual schemas for the EvoSchema rename benchmark.

The public EvoSchema repository contains evolved catalogs and revised SQL, but
not the physically rewritten SQLite databases used by the paper.  Pure table
and column renames are bijections, so they can be evaluated exactly against the
original BIRD database by translating *current* identifiers back to storage
identifiers at the database boundary.  The translation is deliberately hidden
from the agent and rejects legacy identifiers that no longer exist in the
evolved catalog.
"""

from __future__ import annotations

from dataclasses import dataclass
import json
from pathlib import Path
import re
import sqlite3
import time
from typing import Any, Iterable

import sqlglot
from sqlglot import exp
from sqlglot.optimizer.scope import traverse_scope

from finsemguard.e2e.livesqlbench import CatalogDocument
from finsemguard.e2e.react_text2sql import SchemaSearchIndex, SQLiteAgentTools, _safe_value


def _quote(identifier: str) -> str:
    return '"' + identifier.replace('"', '""') + '"'


def _case_lookup(values: Iterable[str]) -> dict[str, str]:
    output: dict[str, str] = {}
    for value in values:
        key = value.casefold()
        if key in output and output[key] != value:
            raise ValueError(f"case-insensitive identifier collision: {value}")
        output[key] = value
    return output


@dataclass(frozen=True)
class ColumnSchema:
    name: str
    declared_type: str
    not_null: bool = False
    primary_key: bool = False
    # SQLite reports the 1-based position of a column in a PRIMARY KEY through
    # PRAGMA table_info.  Keeping only a boolean loses the distinction between a
    # genuinely unique single-column key and one component of a composite key.
    # Relation-changing evolution must retain that distinction because copied
    # composite-key components are not independently cardinality preserving.
    primary_key_ordinal: int = 0


@dataclass(frozen=True)
class ForeignKeySchema:
    source_column: str
    target_table: str
    target_column: str


@dataclass(frozen=True)
class TableSchema:
    name: str
    columns: tuple[ColumnSchema, ...]
    foreign_keys: tuple[ForeignKeySchema, ...] = ()


@dataclass(frozen=True)
class SchemaSnapshot:
    tables: tuple[TableSchema, ...]

    @property
    def by_name(self) -> dict[str, TableSchema]:
        return {table.name: table for table in self.tables}


@dataclass
class EvoSchemaMapping:
    """A bijective old-to-current identifier mapping."""

    table_old_to_new: dict[str, str]
    column_old_to_new: dict[str, dict[str, str]]

    def __post_init__(self) -> None:
        _case_lookup(self.table_old_to_new)
        _case_lookup(self.table_old_to_new.values())
        for table, mapping in self.column_old_to_new.items():
            if not table:
                raise ValueError("column mapping requires an old table name")
            _case_lookup(mapping)
            _case_lookup(mapping.values())

    def current_table(self, old_table: str) -> str:
        key = old_table.casefold()
        for old, new in self.table_old_to_new.items():
            if old.casefold() == key:
                return new
        return old_table

    def old_table(self, current_table: str) -> str:
        key = current_table.casefold()
        for old, new in self.table_old_to_new.items():
            if new.casefold() == key:
                return old
        return current_table

    def current_column(self, old_table: str, old_column: str) -> str:
        key = old_column.casefold()
        table_mapping = next(
            (
                value
                for table, value in self.column_old_to_new.items()
                if table.casefold() == old_table.casefold()
            ),
            {},
        )
        for old, new in table_mapping.items():
            if old.casefold() == key:
                return new
        return old_column

    def old_column(self, current_table: str, current_column: str) -> str:
        old_table = self.old_table(current_table)
        key = current_column.casefold()
        table_mapping = next(
            (
                value
                for table, value in self.column_old_to_new.items()
                if table.casefold() == old_table.casefold()
            ),
            {},
        )
        for old, new in table_mapping.items():
            if new.casefold() == key:
                return old
        return current_column

    def to_json(self) -> dict[str, Any]:
        return {
            "table_old_to_new": dict(sorted(self.table_old_to_new.items())),
            "column_old_to_new": {
                table: dict(sorted(mapping.items()))
                for table, mapping in sorted(self.column_old_to_new.items())
            },
        }

    @classmethod
    def from_json(cls, value: dict[str, Any]) -> "EvoSchemaMapping":
        return cls(
            table_old_to_new={
                str(old): str(new)
                for old, new in dict(value.get("table_old_to_new") or {}).items()
            },
            column_old_to_new={
                str(table): {
                    str(old): str(new)
                    for old, new in dict(mapping).items()
                }
                for table, mapping in dict(value.get("column_old_to_new") or {}).items()
            },
        )


def read_sqlite_snapshot(database: Path) -> SchemaSnapshot:
    database = database.resolve()
    connection = sqlite3.connect(f"file:{database}?mode=ro", uri=True)
    try:
        names = [
            str(row[0])
            for row in connection.execute(
                "SELECT name FROM sqlite_master WHERE type='table' "
                "AND name NOT LIKE 'sqlite_%' ORDER BY name"
            )
        ]
        # Read columns first because SQLite permits ``REFERENCES parent`` with
        # an omitted target column.  PRAGMA then reports NULL in ``to``; the
        # semantic endpoint is the corresponding parent primary-key column,
        # not a physical column literally named "None".
        table_info = {
            table: list(
                connection.execute(f"PRAGMA table_info({_quote(table)})")
            )
            for table in names
        }
        primary_keys = {
            table: [
                str(row[1])
                for row in sorted(table_info[table], key=lambda value: int(value[5]))
                if int(row[5]) > 0
            ]
            for table in names
        }
        tables: list[TableSchema] = []
        for table in names:
            columns = tuple(
                ColumnSchema(
                    name=str(row[1]),
                    declared_type=str(row[2] or "unknown"),
                    not_null=bool(row[3]),
                    primary_key=bool(row[5]),
                    primary_key_ordinal=int(row[5] or 0),
                )
                for row in table_info[table]
            )
            foreign_keys_list: list[ForeignKeySchema] = []
            for row in connection.execute(
                f"PRAGMA foreign_key_list({_quote(table)})"
            ):
                target_table = str(row[2])
                if row[4] is None:
                    target_primary_keys = primary_keys.get(target_table, [])
                    sequence = int(row[1])
                    if sequence >= len(target_primary_keys):
                        raise ValueError(
                            "implicit SQLite foreign-key target has no matching "
                            f"primary key: {table}.{row[3]} -> {target_table}"
                        )
                    target_column = target_primary_keys[sequence]
                else:
                    target_column = str(row[4])
                foreign_keys_list.append(
                    ForeignKeySchema(
                        source_column=str(row[3]),
                        target_table=target_table,
                        target_column=target_column,
                    )
                )
            foreign_keys = tuple(dict.fromkeys(foreign_keys_list))
            tables.append(TableSchema(table, columns, foreign_keys))
    finally:
        connection.close()
    return SchemaSnapshot(tuple(tables))


def evolve_snapshot(
    previous: SchemaSnapshot, mapping: EvoSchemaMapping
) -> SchemaSnapshot:
    tables: list[TableSchema] = []
    for table in previous.tables:
        current_table = mapping.current_table(table.name)
        columns = tuple(
            ColumnSchema(
                mapping.current_column(table.name, column.name),
                column.declared_type,
                column.not_null,
                column.primary_key,
                column.primary_key_ordinal,
            )
            for column in table.columns
        )
        foreign_keys = tuple(
            ForeignKeySchema(
                mapping.current_column(table.name, edge.source_column),
                mapping.current_table(edge.target_table),
                mapping.current_column(edge.target_table, edge.target_column),
            )
            for edge in table.foreign_keys
        )
        tables.append(TableSchema(current_table, columns, foreign_keys))
    _case_lookup(table.name for table in tables)
    return SchemaSnapshot(tuple(sorted(tables, key=lambda row: row.name.casefold())))


def infer_schema_lineage(
    previous: SchemaSnapshot, current: SchemaSnapshot
) -> EvoSchemaMapping:
    """Infer rename lineage using names, ordered types, and table signatures.

    This is the evidence available to the method: a prior schema snapshot and
    the current catalog.  No benchmark mapping, question, or gold SQL is read.
    """

    old_by_cf = {table.name.casefold(): table for table in previous.tables}
    new_by_cf = {table.name.casefold(): table for table in current.tables}
    matches: dict[str, str] = {
        old.name: new_by_cf[key].name for key, old in old_by_cf.items() if key in new_by_cf
    }
    removed = [table for key, table in old_by_cf.items() if key not in new_by_cf]
    added = [table for key, table in new_by_cf.items() if key not in old_by_cf]

    def signature(table: TableSchema, *, include_names: bool) -> tuple[Any, ...]:
        return tuple(
            (
                column.name.casefold() if include_names else "",
                column.declared_type.casefold(),
                column.primary_key_ordinal,
            )
            for column in table.columns
        )

    unmatched_added = {table.name for table in added}
    for old in removed:
        exact = [
            new
            for new in added
            if new.name in unmatched_added
            and signature(old, include_names=True) == signature(new, include_names=True)
        ]
        candidates = exact or [
            new
            for new in added
            if new.name in unmatched_added
            and signature(old, include_names=False) == signature(new, include_names=False)
        ]
        if len(candidates) == 1:
            matches[old.name] = candidates[0].name
            unmatched_added.remove(candidates[0].name)

    table_mapping = {
        old: new for old, new in matches.items() if old.casefold() != new.casefold()
    }
    column_mapping: dict[str, dict[str, str]] = {}
    current_by_name = current.by_name
    previous_by_name = previous.by_name
    for old_table, new_table in matches.items():
        old_columns = previous_by_name[old_table].columns
        new_columns = current_by_name[new_table].columns
        if len(old_columns) != len(new_columns):
            continue
        if any(
            old.declared_type.casefold() != new.declared_type.casefold()
            for old, new in zip(old_columns, new_columns, strict=True)
        ):
            continue
        changed = {
            old.name: new.name
            for old, new in zip(old_columns, new_columns, strict=True)
            if old.name.casefold() != new.name.casefold()
        }
        if changed:
            column_mapping[old_table] = changed
    return EvoSchemaMapping(table_mapping, column_mapping)


def build_catalog_documents(
    snapshot: SchemaSnapshot, context_id: str
) -> list[CatalogDocument]:
    output: list[CatalogDocument] = []
    for table in snapshot.tables:
        fk_by_column = {edge.source_column: edge for edge in table.foreign_keys}
        lines: list[str] = []
        for column in table.columns:
            annotations: list[str] = []
            if column.primary_key:
                annotations.append("PRIMARY KEY")
            if column.not_null:
                annotations.append("NOT NULL")
            edge = fk_by_column.get(column.name)
            if edge:
                annotations.append(
                    f"REFERENCES {_quote(edge.target_table)}({_quote(edge.target_column)})"
                )
            suffix = f" -- {'; '.join(annotations)}" if annotations else ""
            lines.append(
                f"  {_quote(column.name)} {column.declared_type or 'unknown'}{suffix}"
            )
            output.append(
                CatalogDocument(
                    candidate_id=(
                        f"column::{context_id}::{table.name}::{column.name}"
                    ),
                    database_id=context_id,
                    kind="column",
                    table=table.name,
                    name=f"{table.name}.{column.name}",
                    text=(
                        f"current physical SQLite identifier: {_quote(table.name)}."
                        f"{_quote(column.name)}\n"
                        f"type: {column.declared_type or 'unknown'}"
                    ),
                )
            )
        output.append(
            CatalogDocument(
                candidate_id=f"table::{context_id}::{table.name}",
                database_id=context_id,
                kind="table",
                table=table.name,
                name=table.name,
                text="\n".join(
                    [
                        f"current physical SQLite table: {_quote(table.name)}",
                        f"CREATE TABLE {_quote(table.name)} (",
                        *lines,
                        ");",
                    ]
                ),
                references=tuple(
                    dict.fromkeys(edge.target_table for edge in table.foreign_keys)
                ),
            )
        )
    if len({row.candidate_id for row in output}) != len(output):
        raise ValueError(f"duplicate evolved catalog IDs for {context_id}")
    return output


def build_lineage_ontology_documents(
    *,
    previous: SchemaSnapshot,
    current: SchemaSnapshot,
    lineage: EvoSchemaMapping,
    context_id: str,
) -> tuple[list[CatalogDocument], dict[str, list[str]], list[dict[str, Any]]]:
    """Compile schema-diff lineage and typed FK relations for retrieval."""

    output: list[CatalogDocument] = []
    bindings: dict[str, list[str]] = {}

    def add(document: CatalogDocument, physical_ids: list[str]) -> None:
        output.append(document)
        bindings[document.candidate_id] = physical_ids

    for old_table, new_table in sorted(lineage.table_old_to_new.items()):
        candidate_id = f"lineage_table::{context_id}::{new_table}"
        add(
            CatalogDocument(
                candidate_id=candidate_id,
                database_id=context_id,
                kind="schema_lineage_table",
                table=new_table,
                name=new_table,
                text=json.dumps(
                    {
                        "current_physical_table": new_table,
                        "historical_identifier": old_table,
                        "relation": "renamed_from",
                        "evidence": "automatic_previous_current_schema_diff",
                    },
                    ensure_ascii=False,
                    sort_keys=True,
                ),
            ),
            [f"table::{context_id}::{new_table}"],
        )
    for old_table, mapping in sorted(lineage.column_old_to_new.items()):
        new_table = lineage.current_table(old_table)
        for old_column, new_column in sorted(mapping.items()):
            candidate_id = (
                f"lineage_column::{context_id}::{new_table}::{new_column}"
            )
            add(
                CatalogDocument(
                    candidate_id=candidate_id,
                    database_id=context_id,
                    kind="schema_lineage_column",
                    table=new_table,
                    name=f"{new_table}.{new_column}",
                    text=json.dumps(
                        {
                            "current_physical_identifier": f"{new_table}.{new_column}",
                            "historical_identifier": f"{old_table}.{old_column}",
                            "relation": "renamed_from",
                            "evidence": "automatic_previous_current_schema_diff",
                        },
                        ensure_ascii=False,
                        sort_keys=True,
                    ),
                ),
                [
                    f"table::{context_id}::{new_table}",
                    f"column::{context_id}::{new_table}::{new_column}",
                ],
            )

    old_by_current = {
        lineage.current_table(table.name): table.name for table in previous.tables
    }
    ontology_edges: list[dict[str, Any]] = []
    for table in current.tables:
        old_table = old_by_current.get(table.name, table.name)
        for edge in table.foreign_keys:
            old_target = lineage.old_table(edge.target_table)
            old_source_column = lineage.old_column(table.name, edge.source_column)
            old_target_column = lineage.old_column(
                edge.target_table, edge.target_column
            )
            left = f"{table.name}.{edge.source_column}"
            right = f"{edge.target_table}.{edge.target_column}"
            candidate_id = (
                f"ontology_fk::{context_id}::{table.name}::{edge.source_column}::"
                f"{edge.target_table}::{edge.target_column}"
            )
            add(
                CatalogDocument(
                    candidate_id=candidate_id,
                    database_id=context_id,
                    kind="ontology_relation",
                    table=table.name,
                    name=f"{left} -> {right}",
                    text=json.dumps(
                        {
                            "relation": "foreign_key_join",
                            "current_left": left,
                            "current_right": right,
                            "historical_left": f"{old_table}.{old_source_column}",
                            "historical_right": f"{old_target}.{old_target_column}",
                            "evidence": "declared_fk_plus_schema_lineage",
                        },
                        ensure_ascii=False,
                        sort_keys=True,
                    ),
                    references=(edge.target_table,),
                ),
                [
                    f"table::{context_id}::{table.name}",
                    f"column::{context_id}::{table.name}::{edge.source_column}",
                    f"table::{context_id}::{edge.target_table}",
                    f"column::{context_id}::{edge.target_table}::{edge.target_column}",
                ],
            )
            ontology_edges.append(
                {
                    "left": left,
                    "right": right,
                    "evidence": "declared_fk_plus_schema_lineage",
                    "provenance_ids": [candidate_id],
                    "score": 1.0,
                }
            )
    return output, bindings, ontology_edges


def _current_schema_sets(
    snapshot: SchemaSnapshot,
) -> tuple[dict[str, str], dict[str, dict[str, str]]]:
    tables = _case_lookup(table.name for table in snapshot.tables)
    columns = {
        table.name: _case_lookup(column.name for column in table.columns)
        for table in snapshot.tables
    }
    return tables, columns


def translate_current_sql_to_storage(
    sql: str,
    *,
    mapping: EvoSchemaMapping,
    current: SchemaSnapshot,
) -> str:
    """Validate current identifiers and translate only identifiers, never literals."""

    if not sql.strip():
        raise ValueError("SQL must not be empty")
    tree = sqlglot.parse_one(sql, read="sqlite")
    current_tables, current_columns = _current_schema_sets(current)
    cte_names = {
        str(cte.alias_or_name).casefold() for cte in tree.find_all(exp.CTE)
    }
    qualifier_to_current: dict[str, str] = {}
    scope_tables_by_column: dict[int, list[str]] = {}
    for scope in traverse_scope(tree):
        local_tables = [
            current_tables[table.name.casefold()]
            for table in scope.tables
            if table.name.casefold() in current_tables
        ]
        for column in scope.columns:
            scope_tables_by_column.setdefault(id(column), local_tables)
    table_nodes: list[tuple[exp.Table, str, str | None]] = []
    referenced: list[str] = []
    for table in tree.find_all(exp.Table):
        supplied = table.name
        if supplied.casefold() in cte_names:
            continue
        current_name = current_tables.get(supplied.casefold())
        if current_name is None:
            raise ValueError(f"table is absent from evolved schema: {supplied}")
        alias = str(table.alias or "") or None
        qualifier_to_current[(alias or current_name).casefold()] = current_name
        qualifier_to_current[current_name.casefold()] = current_name
        referenced.append(current_name)
        table_nodes.append((table, current_name, alias))

    for column in tree.find_all(exp.Column):
        name = column.name
        if name == "*":
            continue
        qualifier = str(column.table or "")
        current_table = (
            qualifier_to_current.get(qualifier.casefold()) if qualifier else None
        )
        if current_table:
            known = current_columns[current_table]
            if name.casefold() not in known:
                raise ValueError(
                    f"column is absent from evolved schema: {current_table}.{name}"
                )
            storage_name = mapping.old_column(current_table, known[name.casefold()])
            column.set("this", exp.to_identifier(storage_name, quoted=True))
            if qualifier and qualifier.casefold() == current_table.casefold():
                storage_table = mapping.old_table(current_table)
                column.set("table", exp.to_identifier(storage_table, quoted=True))
            continue

        candidates: list[tuple[str, str]] = []
        # A derived-table/CTE consumer has no local physical table even though
        # its projected columns still inherit the underlying renamed physical
        # identifiers. Fall back to the statement's base tables only for that
        # empty-local-scope case. Nested scopes with a real local table keep
        # their own table set, which prevents outer-table renames leaking into
        # an unrelated subquery.
        scoped_tables = scope_tables_by_column.get(id(column)) or referenced
        for table_name in dict.fromkeys(scoped_tables):
            known = current_columns[table_name]
            if name.casefold() in known:
                candidates.append(
                    (
                        table_name,
                        mapping.old_column(table_name, known[name.casefold()]),
                    )
                )
        if not candidates:
            renamed_legacy = {
                old.casefold()
                for values in mapping.column_old_to_new.values()
                for old in values
            }
            if name.casefold() in renamed_legacy:
                raise ValueError(f"legacy column is absent from evolved schema: {name}")
            # It may be a CTE/output alias. SQLite will validate it after translation.
            continue
        storage_names = {value.casefold(): value for _, value in candidates}
        if len(storage_names) == 1:
            column.set("this", exp.to_identifier(next(iter(storage_names.values())), quoted=True))

    for table, current_name, _alias in table_nodes:
        table.set("this", exp.to_identifier(mapping.old_table(current_name), quoted=True))
    return tree.sql(dialect="sqlite")


def translate_storage_sql_to_current(
    sql: str,
    *,
    mapping: EvoSchemaMapping,
    previous: SchemaSnapshot,
) -> str:
    """Compile a target-isolated historical SQL pattern onto current identifiers."""

    if not sql.strip():
        raise ValueError("SQL must not be empty")
    tree = sqlglot.parse_one(sql, read="sqlite")
    old_tables, old_columns = _current_schema_sets(previous)
    cte_names = {
        str(cte.alias_or_name).casefold() for cte in tree.find_all(exp.CTE)
    }
    qualifier_to_old: dict[str, str] = {}
    scope_tables_by_column: dict[int, list[str]] = {}
    for scope in traverse_scope(tree):
        local_tables = [
            old_tables[table.name.casefold()]
            for table in scope.tables
            if table.name.casefold() in old_tables
        ]
        for column in scope.columns:
            scope_tables_by_column.setdefault(id(column), local_tables)
    table_nodes: list[tuple[exp.Table, str, str | None]] = []
    referenced: list[str] = []
    for table in tree.find_all(exp.Table):
        supplied = table.name
        if supplied.casefold() in cte_names:
            continue
        old_name = old_tables.get(supplied.casefold())
        if old_name is None:
            raise ValueError(f"table is absent from historical schema: {supplied}")
        alias = str(table.alias or "") or None
        qualifier_to_old[(alias or old_name).casefold()] = old_name
        qualifier_to_old[old_name.casefold()] = old_name
        referenced.append(old_name)
        table_nodes.append((table, old_name, alias))

    for column in tree.find_all(exp.Column):
        name = column.name
        if name == "*":
            continue
        qualifier = str(column.table or "")
        old_table = qualifier_to_old.get(qualifier.casefold()) if qualifier else None
        if old_table:
            known = old_columns[old_table]
            if name.casefold() not in known:
                # Qualified derived-table columns are validated by SQLite later.
                continue
            current_name = mapping.current_column(old_table, known[name.casefold()])
            column.set("this", exp.to_identifier(current_name, quoted=True))
            if qualifier and qualifier.casefold() == old_table.casefold():
                column.set(
                    "table",
                    exp.to_identifier(mapping.current_table(old_table), quoted=True),
                )
            continue
        candidates: list[tuple[str, str]] = []
        scoped_tables = scope_tables_by_column.get(id(column), referenced)
        for table_name in dict.fromkeys(scoped_tables):
            known = old_columns[table_name]
            if name.casefold() in known:
                candidates.append(
                    (
                        table_name,
                        mapping.current_column(table_name, known[name.casefold()]),
                    )
                )
        current_names = {value.casefold(): value for _, value in candidates}
        if len(current_names) == 1:
            column.set("this", exp.to_identifier(next(iter(current_names.values())), quoted=True))

    for table, old_name, _alias in table_nodes:
        table.set("this", exp.to_identifier(mapping.current_table(old_name), quoted=True))
    return tree.sql(dialect="sqlite")


class EvoSchemaSQLiteAgentTools(SQLiteAgentTools):
    """Expose an evolved catalog while executing against immutable BIRD storage."""

    def __init__(
        self,
        database: Path,
        database_id: str,
        search_index: SchemaSearchIndex,
        *,
        mapping: EvoSchemaMapping,
        current_snapshot: SchemaSnapshot,
    ) -> None:
        self.mapping = mapping
        self.current_snapshot = current_snapshot
        super().__init__(database, database_id, search_index)
        self.columns = {
            table.name: [
                (column.name, column.declared_type) for column in table.columns
            ]
            for table in current_snapshot.tables
        }
        self.foreign_keys = {
            table.name: [
                {
                    "from": edge.source_column,
                    "to_table": edge.target_table,
                    "to_column": edge.target_column,
                }
                for edge in table.foreign_keys
            ]
            for table in current_snapshot.tables
        }
        self.join_edges = self._join_edges()
        observed = {
            tuple(sorted((row["left"].casefold(), row["right"].casefold())))
            for row in self.join_edges
        }
        for source in search_index.ontology_edges_by_database.get(database_id, []):
            row = dict(source)
            key = tuple(sorted((str(row["left"]).casefold(), str(row["right"]).casefold())))
            if key not in observed:
                self.join_edges.append(row)
                observed.add(key)

    def _storage_identifiers(self, table: str, column: str) -> tuple[str, str]:
        current_tables, current_columns = _current_schema_sets(self.current_snapshot)
        current_table = current_tables.get(table.casefold())
        if current_table is None:
            raise ValueError(f"unknown evolved table: {table}")
        current_column = current_columns[current_table].get(column.casefold())
        if current_column is None:
            raise ValueError(f"unknown evolved column: {current_table}.{column}")
        return (
            self.mapping.old_table(current_table),
            self.mapping.old_column(current_table, current_column),
        )

    def inspect_schema(self, tables: list[str]) -> dict[str, Any]:
        requested = {str(value).casefold() for value in tables[:6]}
        output = []
        for table in self.current_snapshot.tables:
            if table.name.casefold() not in requested:
                continue
            lines = [
                f"  {_quote(column.name)} {column.declared_type or 'unknown'}"
                for column in table.columns
            ]
            output.append(
                {
                    "table": table.name,
                    "ddl": "\n".join(
                        [f"CREATE TABLE {_quote(table.name)} (", *lines, ");"]
                    ),
                    "foreign_keys": self.foreign_keys[table.name],
                }
            )
        return {"tables": output, "schema_view": "evolved_current_catalog"}

    def search_values(
        self, literals: list[str], max_matches: int
    ) -> dict[str, Any]:
        limit = max(1, min(int(max_matches), 30))
        variants: dict[str, list[str]] = {}
        variant_owner: dict[str, str] = {}
        for literal in literals[:12]:
            rendered = str(literal)
            variants[rendered] = self._literal_variants(rendered)
            for value in variants[rendered]:
                variant_owner.setdefault(value.casefold(), rendered)
        flat = list(dict.fromkeys(value for rows in variants.values() for value in rows))
        if not flat:
            return {"matches": [], "truncated": False}
        matches: list[dict[str, Any]] = []
        connection = sqlite3.connect(f"file:{self.database}?mode=ro", uri=True)
        connection.execute("PRAGMA query_only=ON")
        deadline = time.monotonic() + 10.0
        connection.set_progress_handler(lambda: int(time.monotonic() > deadline), 10_000)
        try:
            placeholders = ",".join("?" for _ in flat)
            for table in sorted(self.columns):
                for column, _kind in self.columns[table]:
                    old_table, old_column = self._storage_identifiers(table, column)
                    query = (
                        f"SELECT {_quote(old_column)}, COUNT(*) FROM {_quote(old_table)} "
                        f"WHERE {_quote(old_column)} IN ({placeholders}) "
                        f"GROUP BY {_quote(old_column)} LIMIT {limit}"
                    )
                    try:
                        rows = connection.execute(query, tuple(flat)).fetchall()
                    except sqlite3.OperationalError:
                        continue
                    for value, count in rows:
                        rendered = str(value)
                        owner = variant_owner.get(rendered.casefold(), rendered)
                        matches.append(
                            {
                                "literal": owner,
                                "physical_column": f"{table}.{column}",
                                "matched_value": _safe_value(value),
                                "row_count": int(count),
                                "evidence": "exact_database_value",
                            }
                        )
                        if len(matches) >= limit:
                            return {"matches": matches, "truncated": True}
        finally:
            connection.close()
        return {"matches": matches, "truncated": False}

    def sample_values(
        self,
        table: str,
        column: str,
        limit: int = 8,
        contains: str | None = None,
    ) -> dict[str, Any]:
        current_table = next(
            (value for value in self.columns if value.casefold() == table.casefold()),
            None,
        )
        if current_table is None:
            raise ValueError(f"unknown evolved table: {table}")
        current_column = next(
            (
                value
                for value, _kind in self.columns[current_table]
                if value.casefold() == column.casefold()
            ),
            None,
        )
        if current_column is None:
            raise ValueError(f"unknown evolved column: {current_table}.{column}")
        old_table, old_column = self._storage_identifiers(
            current_table, current_column
        )
        limit = max(1, min(int(limit), 20))
        where = f"WHERE {_quote(old_column)} IS NOT NULL"
        parameters: tuple[Any, ...] = ()
        if contains:
            where += f" AND CAST({_quote(old_column)} AS TEXT) LIKE ?"
            parameters = (f"%{contains}%",)
        query = (
            f"SELECT {_quote(old_column)}, COUNT(*) AS frequency "
            f"FROM {_quote(old_table)} {where} GROUP BY {_quote(old_column)} "
            f"ORDER BY frequency DESC LIMIT {limit}"
        )
        connection = sqlite3.connect(f"file:{self.database}?mode=ro", uri=True)
        try:
            rows = connection.execute(query, parameters).fetchall()
        finally:
            connection.close()
        return {
            "table": current_table,
            "column": current_column,
            "contains": contains,
            "values": [[_safe_value(value) for value in row] for row in rows],
        }

    def execute_sql(self, sql: str, limit: int = 20) -> dict[str, Any]:
        try:
            translated = translate_current_sql_to_storage(
                sql, mapping=self.mapping, current=self.current_snapshot
            )
        except Exception as error:
            return {
                "executable": False,
                "error_type": type(error).__name__,
                "error": str(error)[:800],
                "schema_view": "evolved_current_catalog",
            }
        output = super().execute_sql(translated, limit=limit)
        output["schema_view"] = "evolved_current_catalog"
        output["storage_adapter"] = "identifier_bijection_hidden_from_agent"
        return output
