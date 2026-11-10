"""Executable relation-changing schema evolution over immutable SQLite storage.

EvoSchema publishes evolved schemas and revised SQL, but not rewritten database
files.  This module represents split/merge lineage explicitly and compiles an
evolved query back to the immutable source database.  The compiler is structural:
it consumes only previous/current schemas and released evolution mappings, never a
question, gold answer, or correctness label.

Table splits are many-current-to-one-source views.  Table merges are one-current-
to-many-source views joined through an unambiguous declared source foreign key.
Column changes use derived current-schema views and preserve current output shape
by default.  An explicit legacy mode is available only for adapter diagnostics
that enforce the invariant

    Exec(reverse_map(evolved_gold)) == Exec(original_gold)

and reject released rows whose mapping is incomplete or inconsistent.
"""

from __future__ import annotations

import ast
from dataclasses import dataclass
from hashlib import sha256
import json
from pathlib import Path
import re
import sqlite3
import time
from typing import Any, Iterable

import sqlglot
from sqlglot import exp
from sqlglot.optimizer.scope import traverse_scope

from finsemguard.e2e.evoschema import (
    ColumnSchema,
    ForeignKeySchema,
    SchemaSnapshot,
    TableSchema,
)
from finsemguard.e2e.livesqlbench import CatalogDocument
from finsemguard.e2e.react_text2sql import (
    SQLiteAgentTools,
    SchemaSearchIndex,
    _safe_value,
)


def _quote(identifier: str) -> str:
    return '"' + str(identifier).replace('"', '""') + '"'


def _clean_identifier(value: Any) -> str:
    text = str(value or "").strip()
    while len(text) >= 2 and (
        (text[0], text[-1]) in {("'", "'"), ('"', '"'), ("`", "`")}
        or (text[0], text[-1]) == ("[", "]")
    ):
        text = text[1:-1].strip()
    return text


def _case_lookup(values: Iterable[str]) -> dict[str, str]:
    output: dict[str, str] = {}
    for value in values:
        key = str(value).casefold()
        if key in output and output[key] != value:
            raise ValueError(f"case-insensitive identifier collision: {value}")
        output[key] = str(value)
    return output


def _resolve(lookup: dict[str, str], value: Any, *, kind: str) -> str:
    cleaned = _clean_identifier(value)
    resolved = lookup.get(cleaned.casefold())
    if resolved is None:
        raise ValueError(f"unknown {kind}: {cleaned}")
    return resolved


def _split_mapping_values(value: Any) -> list[str]:
    """Normalize the inconsistent quoted/comma-separated official mappings."""

    values = value if isinstance(value, list) else [value]
    output: list[str] = []
    for item in values:
        text = str(item or "").strip()
        if text.startswith("[") and text.endswith("]"):
            try:
                parsed = ast.literal_eval(text)
            except (SyntaxError, ValueError):
                parsed = None
            if isinstance(parsed, (list, tuple)):
                output.extend(_split_mapping_values(list(parsed)))
                continue
        # Some released rows encode two names as one list item, for example
        # ``["WebsiteProtocol, WebsiteDomain"]``.
        parts = re.split(r"\s*,\s*", text)
        output.extend(
            cleaned
            for part in parts
            if (cleaned := _clean_identifier(part))
        )
    return list(dict.fromkeys(output))


def _released_columns(value: dict[str, Any]) -> list[str]:
    """Read the official column list, falling back to its permissive DDL."""

    released = list(value.get("columns") or [])
    if released:
        output: list[str] = []
        for item in released:
            text = str(item or "").strip()
            foreign_key = re.match(r"foreign\s+key\s*\(([^)]+)\)", text, re.I)
            if foreign_key:
                text = foreign_key.group(1)
            cleaned = _clean_identifier(text)
            if cleaned:
                output.append(cleaned)
        return list(dict.fromkeys(output))

    ddl = str(value.get("ddl") or "").strip()
    opening = ddl.find("(")
    closing = ddl.rfind(")")
    if opening < 0 or closing <= opening:
        return []
    body = ddl[opening + 1 : closing]
    chunks: list[str] = []
    start = 0
    depth = 0
    for index, character in enumerate(body):
        if character == "(":
            depth += 1
        elif character == ")":
            depth = max(0, depth - 1)
        elif character == "," and depth == 0:
            chunks.append(body[start:index])
            start = index + 1
    chunks.append(body[start:])

    type_pattern = re.compile(
        r"\s+(?:bigint|boolean|date|datetime|decimal(?:\([^)]*\))?|double|"
        r"float|int|integer|numeric(?:\([^)]*\))?|real|text|timestamp|"
        r"varchar(?:\([^)]*\))?)\b.*$",
        re.I,
    )
    output = []
    for chunk in chunks:
        text = chunk.strip()
        foreign_key = re.match(r"foreign\s+key\s*\(([^)]+)\)", text, re.I)
        if foreign_key:
            name = foreign_key.group(1)
        else:
            name = type_pattern.sub("", text).strip()
        cleaned = _clean_identifier(name)
        if cleaned:
            output.append(cleaned)
    return list(dict.fromkeys(output))


@dataclass(frozen=True)
class SourceColumn:
    table: str
    column: str

    def to_json(self) -> dict[str, str]:
        return {"table": self.table, "column": self.column}

    @classmethod
    def from_json(cls, value: dict[str, Any]) -> "SourceColumn":
        return cls(str(value["table"]), str(value["column"]))


@dataclass(frozen=True)
class SourceJoin:
    left_table: str
    left_column: str
    right_table: str
    right_column: str
    evidence_type: str = "declared_foreign_key"

    def to_json(self) -> dict[str, str]:
        return {
            "left_table": self.left_table,
            "left_column": self.left_column,
            "right_table": self.right_table,
            "right_column": self.right_column,
            "evidence_type": self.evidence_type,
        }

    @classmethod
    def from_json(cls, value: dict[str, Any]) -> "SourceJoin":
        return cls(
            left_table=str(value["left_table"]),
            left_column=str(value["left_column"]),
            right_table=str(value["right_table"]),
            right_column=str(value["right_column"]),
            evidence_type=str(value.get("evidence_type") or "declared_foreign_key"),
        )


class NoDeclaredSourceJoinError(ValueError):
    """The source tables have no declared cross-table relationship."""


class AmbiguousSourceJoinError(ValueError):
    """The source tables have multiple role-distinct declared relationships."""


def snapshot_to_json(snapshot: SchemaSnapshot) -> dict[str, Any]:
    return {
        "tables": [
            {
                "name": table.name,
                "columns": [
                    {
                        "name": column.name,
                        "declared_type": column.declared_type,
                        "not_null": column.not_null,
                        "primary_key": column.primary_key,
                        "primary_key_ordinal": column.primary_key_ordinal,
                    }
                    for column in table.columns
                ],
                "foreign_keys": [
                    {
                        "source_column": edge.source_column,
                        "target_table": edge.target_table,
                        "target_column": edge.target_column,
                    }
                    for edge in table.foreign_keys
                ],
            }
            for table in snapshot.tables
        ]
    }


def snapshot_from_json(value: dict[str, Any]) -> SchemaSnapshot:
    return SchemaSnapshot(
        tuple(
            TableSchema(
                name=str(table["name"]),
                columns=tuple(
                    ColumnSchema(
                        name=str(column["name"]),
                        declared_type=str(column.get("declared_type") or "unknown"),
                        not_null=bool(column.get("not_null")),
                        primary_key=bool(column.get("primary_key")),
                        primary_key_ordinal=int(
                            column.get("primary_key_ordinal")
                            or (1 if column.get("primary_key") else 0)
                        ),
                    )
                    for column in table.get("columns") or []
                ),
                foreign_keys=tuple(
                    ForeignKeySchema(
                        source_column=str(edge["source_column"]),
                        target_table=str(edge["target_table"]),
                        target_column=str(edge["target_column"]),
                    )
                    for edge in table.get("foreign_keys") or []
                ),
            )
            for table in value.get("tables") or []
        )
    )


@dataclass
class RelationEvolutionMapping:
    """Lineage needed to expose and execute one evolved current schema."""

    evolution_type: str
    current_snapshot: SchemaSnapshot
    table_sources: dict[str, tuple[str, ...]]
    column_sources: dict[str, dict[str, tuple[SourceColumn, ...]]]
    source_joins: dict[str, tuple[SourceJoin, ...]]
    column_operations: dict[str, dict[str, str]]
    relationship_edges: tuple[dict[str, Any], ...] = ()

    def to_json(self) -> dict[str, Any]:
        return {
            "evolution_type": self.evolution_type,
            "current_snapshot": snapshot_to_json(self.current_snapshot),
            "table_sources": {
                table: list(sources)
                for table, sources in sorted(self.table_sources.items())
            },
            "column_sources": {
                table: {
                    column: [source.to_json() for source in sources]
                    for column, sources in sorted(columns.items())
                }
                for table, columns in sorted(self.column_sources.items())
            },
            "source_joins": {
                table: [edge.to_json() for edge in edges]
                for table, edges in sorted(self.source_joins.items())
            },
            "column_operations": {
                table: dict(sorted(columns.items()))
                for table, columns in sorted(self.column_operations.items())
            },
            "relationship_edges": [dict(edge) for edge in self.relationship_edges],
        }

    @classmethod
    def from_json(cls, value: dict[str, Any]) -> "RelationEvolutionMapping":
        return cls(
            evolution_type=str(value["evolution_type"]),
            current_snapshot=snapshot_from_json(dict(value["current_snapshot"])),
            table_sources={
                str(table): tuple(str(source) for source in sources)
                for table, sources in dict(value.get("table_sources") or {}).items()
            },
            column_sources={
                str(table): {
                    str(column): tuple(
                        SourceColumn.from_json(dict(source)) for source in sources
                    )
                    for column, sources in dict(columns).items()
                }
                for table, columns in dict(value.get("column_sources") or {}).items()
            },
            source_joins={
                str(table): tuple(SourceJoin.from_json(dict(edge)) for edge in edges)
                for table, edges in dict(value.get("source_joins") or {}).items()
            },
            column_operations={
                str(table): {
                    str(column): str(operation)
                    for column, operation in dict(columns).items()
                }
                for table, columns in dict(
                    value.get("column_operations") or {}
                ).items()
            },
            relationship_edges=tuple(
                dict(edge) for edge in value.get("relationship_edges") or []
            ),
        )

    @property
    def relationship_encoding_changed(self) -> bool:
        return self.evolution_type in {"table_split", "table_merge"}


def _replace_tables(
    previous: SchemaSnapshot,
    *,
    removed: set[str],
    added: list[TableSchema],
    target_rebindings: dict[tuple[str, str], tuple[str, str]],
) -> SchemaSnapshot:
    """Replace changed tables and rebind only exact old target columns.

    A table-level rebinding is unsound when incoming foreign keys target
    different role-bearing keys.  If no exact, cardinality-safe rebinding is
    supplied, the historical FK is omitted from the current catalog rather
    than being rewritten to an arbitrary column and falsely certified.
    """

    removed_cf = {value.casefold() for value in removed}
    output: list[TableSchema] = []
    for table in previous.tables:
        if table.name.casefold() in removed_cf:
            continue
        foreign_keys: list[ForeignKeySchema] = []
        for edge in table.foreign_keys:
            rebound = target_rebindings.get(
                (edge.target_table.casefold(), edge.target_column.casefold())
            )
            if rebound is None:
                if edge.target_table.casefold() in removed_cf:
                    continue
                foreign_keys.append(edge)
            else:
                foreign_keys.append(
                    ForeignKeySchema(edge.source_column, rebound[0], rebound[1])
                )
        output.append(TableSchema(table.name, table.columns, tuple(foreign_keys)))
    output.extend(added)
    _case_lookup(table.name for table in output)
    return SchemaSnapshot(tuple(sorted(output, key=lambda row: row.name.casefold())))


def build_table_split_mapping(
    row: dict[str, Any], previous: SchemaSnapshot
) -> RelationEvolutionMapping:
    released = dict(row.get("old_new_table_column_mapping") or {})
    if len(released) != 1:
        raise ValueError("table split requires exactly one source table mapping")
    previous_tables = _case_lookup(table.name for table in previous.tables)
    old_supplied, new_values = next(iter(released.items()))
    old_table = _resolve(previous_tables, old_supplied, kind="source table")
    source = previous.by_name[old_table]
    source_primary_key = tuple(
        column.name
        for column in sorted(
            source.columns,
            key=lambda value: value.primary_key_ordinal or 10**9,
        )
        if column.primary_key_ordinal > 0
    )
    # A copied component of a composite key is not independently unique.  The
    # current graph represents one-column join edges, so only a genuine
    # single-column source key can be promoted to a cardinality certificate.
    single_source_primary_key = (
        source_primary_key[0] if len(source_primary_key) == 1 else None
    )
    source_columns = _case_lookup(column.name for column in source.columns)
    relevant = dict(row.get("new_relevant_table") or {})
    relevant_lookup = _case_lookup(relevant)
    new_tables = [
        _resolve(relevant_lookup, value, kind="split table")
        for value in _split_mapping_values(new_values)
    ]
    if len(new_tables) < 2:
        raise ValueError("table split must create at least two current tables")

    added: list[TableSchema] = []
    table_sources: dict[str, tuple[str, ...]] = {}
    column_sources: dict[str, dict[str, tuple[SourceColumn, ...]]] = {}
    primary_targets: dict[str, list[tuple[str, str]]] = {}
    shared_targets: dict[str, list[tuple[str, str]]] = {}
    for new_table in new_tables:
        names = _released_columns(dict(relevant[new_table]))
        if not names:
            raise ValueError(f"split table has no released columns: {new_table}")
        columns: list[ColumnSchema] = []
        sources: dict[str, tuple[SourceColumn, ...]] = {}
        for supplied in names:
            old_column = _resolve(source_columns, supplied, kind="source column")
            original = next(
                column for column in source.columns if column.name == old_column
            )
            columns.append(
                ColumnSchema(
                    name=supplied,
                    declared_type=original.declared_type,
                    not_null=original.not_null,
                    primary_key=(
                        single_source_primary_key is not None
                        and old_column.casefold()
                        == single_source_primary_key.casefold()
                    ),
                    primary_key_ordinal=(
                        1
                        if single_source_primary_key is not None
                        and old_column.casefold()
                        == single_source_primary_key.casefold()
                        else 0
                    ),
                )
            )
            sources[supplied] = (SourceColumn(old_table, old_column),)
            shared_targets.setdefault(old_column, []).append(
                (new_table, supplied)
            )
            if (
                single_source_primary_key is not None
                and old_column.casefold() == single_source_primary_key.casefold()
            ):
                primary_targets.setdefault(old_column, []).append(
                    (new_table, supplied)
                )
        present = {column.name.casefold() for column in columns}
        foreign_keys = tuple(
            ForeignKeySchema(
                source_column=edge.source_column,
                target_table=edge.target_table,
                target_column=edge.target_column,
            )
            for edge in source.foreign_keys
            if edge.source_column.casefold() in present
            and edge.target_table.casefold() != old_table.casefold()
        )
        added.append(TableSchema(new_table, tuple(columns), foreign_keys))
        table_sources[new_table] = (old_table,)
        column_sources[new_table] = sources

    relationship_columns = primary_targets or {
        column: targets
        for column, targets in shared_targets.items()
        if len(set(targets)) >= 2
    }
    target_rebindings: dict[tuple[str, str], tuple[str, str]] = {}
    for old_column, targets in relationship_columns.items():
        if targets:
            target_rebindings[
                (old_table.casefold(), old_column.casefold())
            ] = targets[0]
    # Incoming relations may reference a retained source column that is present
    # in only one split relation and therefore does not participate in the
    # split-to-split relationship edge.  Preserve that exact endpoint too.
    for old_column, targets in shared_targets.items():
        unique_targets = list(dict.fromkeys(targets))
        if unique_targets:
            target_rebindings.setdefault(
                (old_table.casefold(), old_column.casefold()),
                unique_targets[0],
            )
    current = _replace_tables(
        previous,
        removed={old_table},
        added=added,
        target_rebindings=target_rebindings,
    )
    relationship_edges: list[dict[str, Any]] = []
    for old_column, targets in sorted(relationship_columns.items()):
        targets = list(dict.fromkeys(targets))
        for index, left in enumerate(targets):
            for right in targets[index + 1 :]:
                primary_backed = old_column in primary_targets
                relationship_edges.append(
                    {
                        "left": f"{left[0]}.{left[1]}",
                        "right": f"{right[0]}.{right[1]}",
                        # A copied source primary key is an equality-preserving
                        # relationship by construction.  A non-key column shared
                        # by released split tables is useful evidence, but it is
                        # not a uniqueness/cardinality guarantee and must not be
                        # ranked as strongly as the copied key.
                        "score": 1.0 if primary_backed else 0.7,
                        "evidence_types": [
                            (
                                "evolution_split_key_equivalence"
                                if primary_backed
                                else "released_split_shared_column"
                            ),
                            "relationship_encoding_change",
                        ],
                        "provenance_ids": [
                            f"table_split::{old_table}::{left}::{right}::{old_column}"
                        ],
                    }
                )
    if not relationship_edges:
        raise ValueError("table split has no shared relationship column")
    return RelationEvolutionMapping(
        evolution_type="table_split",
        current_snapshot=current,
        table_sources=table_sources,
        column_sources=column_sources,
        source_joins={},
        column_operations={},
        relationship_edges=tuple(relationship_edges),
    )


def _source_join(
    source_tables: tuple[str, ...], previous: SchemaSnapshot
) -> SourceJoin:
    if len(source_tables) != 2:
        raise ValueError("released table merge must contain exactly two source tables")
    source_set = {value.casefold() for value in source_tables}
    candidates: list[SourceJoin] = []
    for table in previous.tables:
        if table.name.casefold() not in source_set:
            continue
        for edge in table.foreign_keys:
            if edge.target_table.casefold() not in source_set:
                continue
            if edge.target_table.casefold() == table.name.casefold():
                # A self-reference does not connect the two tables being merged.
                continue
            candidates.append(
                SourceJoin(
                    left_table=table.name,
                    left_column=edge.source_column,
                    right_table=edge.target_table,
                    right_column=edge.target_column,
                )
            )
    candidates = list(dict.fromkeys(candidates))
    if not candidates:
        raise NoDeclaredSourceJoinError(
            "merged source tables have no declared cross-table relationship"
        )
    candidates.sort(
        key=lambda edge: (
            edge.left_table.casefold(),
            edge.left_column.casefold(),
            edge.right_table.casefold(),
            edge.right_column.casefold(),
        )
    )
    if len(candidates) != 1:
        rendered = ", ".join(
            f"{edge.left_table}.{edge.left_column}="
            f"{edge.right_table}.{edge.right_column}"
            for edge in candidates
        )
        raise AmbiguousSourceJoinError(
            "merged source tables have role-distinct declared relationships: "
            + rendered
        )
    return candidates[0]


def infer_sqlite_source_join(
    database: Path,
    *,
    source_tables: tuple[str, ...],
    previous: SchemaSnapshot,
    sample_limit: int = 1024,
) -> SourceJoin:
    """Infer a target-independent merge relation from keys and stored values."""

    try:
        return _source_join(source_tables, previous)
    except NoDeclaredSourceJoinError:
        pass
    if len(source_tables) != 2:
        raise ValueError("profile relation inference requires two source tables")
    left_table, right_table = source_tables
    left_schema = previous.by_name[left_table]
    right_schema = previous.by_name[right_table]

    def joinish(column: ColumnSchema) -> bool:
        normalized = re.sub(r"[^a-z0-9]", "", column.name.casefold())
        return column.primary_key or any(
            marker in normalized for marker in ("id", "key", "code", "uuid")
        )

    left_columns = [column for column in left_schema.columns if joinish(column)]
    right_columns = [column for column in right_schema.columns if joinish(column)]
    connection = sqlite3.connect(f"file:{database.resolve()}?mode=ro", uri=True)
    sample_cache: dict[tuple[str, str], set[tuple[str, str]]] = {}

    def samples(table: str, column: str) -> set[tuple[str, str]]:
        key = table, column
        if key not in sample_cache:
            rows = connection.execute(
                f"SELECT DISTINCT {_quote(column)} FROM {_quote(table)} "
                f"WHERE {_quote(column)} IS NOT NULL LIMIT {int(sample_limit)}"
            )
            sample_cache[key] = {
                (type(row[0]).__name__, str(row[0])) for row in rows
            }
        return sample_cache[key]

    candidates: list[tuple[tuple[Any, ...], SourceJoin]] = []
    try:
        for left in left_columns:
            left_values = samples(left_table, left.name)
            if len(left_values) < 2:
                continue
            left_normalized = re.sub(r"[^a-z0-9]", "", left.name.casefold())
            for right in right_columns:
                right_values = samples(right_table, right.name)
                if len(right_values) < 2:
                    continue
                overlap = len(left_values & right_values)
                containment = overlap / min(len(left_values), len(right_values))
                if overlap < min(8, len(left_values), len(right_values)):
                    continue
                if containment < 0.98:
                    continue
                right_normalized = re.sub(
                    r"[^a-z0-9]", "", right.name.casefold()
                )
                name_affinity = (
                    2
                    if left_normalized == right_normalized
                    else int(
                        left_normalized in right_normalized
                        or right_normalized in left_normalized
                    )
                )
                objective = (
                    -name_affinity,
                    -int(left.primary_key or right.primary_key),
                    -round(containment, 8),
                    -overlap,
                    left.name.casefold(),
                    right.name.casefold(),
                )
                candidates.append(
                    (
                        objective,
                        SourceJoin(
                            left_table=left_table,
                            left_column=left.name,
                            right_table=right_table,
                            right_column=right.name,
                            evidence_type="profile_value_containment_join",
                        ),
                    )
                )
    finally:
        connection.close()
    if not candidates:
        raise ValueError("merged source tables have no recoverable relationship")
    return min(candidates, key=lambda value: value[0])[1]


def _deduplicated_column_mapping(
    row: dict[str, Any], source_tables: tuple[str, ...], previous: SchemaSnapshot
) -> dict[str, SourceColumn]:
    table_lookup = _case_lookup(source_tables)
    source_columns = {
        table: _case_lookup(column.name for column in previous.by_name[table].columns)
        for table in source_tables
    }
    output: dict[str, SourceColumn] = {}
    released = dict(
        row.get("deduplicate_new_column_to_old_table_old_table_mapping") or {}
    )
    for current_values, source in released.items():
        current_names = _split_mapping_values(current_values)
        old_tables = _split_mapping_values(dict(source).get("old_table"))
        old_columns = _split_mapping_values(dict(source).get("old_column"))
        if not (
            len(current_names) == len(old_tables) == len(old_columns)
        ):
            # Some released rows concatenate several mappings into one malformed
            # string.  They are allowed to fall back to unambiguous name matching;
            # otherwise the row is rejected later.
            continue
        for current, old_table_value, old_column_value in zip(
            current_names, old_tables, old_columns, strict=True
        ):
            old_table = _resolve(table_lookup, old_table_value, kind="merge source table")
            old_column = _resolve(
                source_columns[old_table], old_column_value, kind="merge source column"
            )
            output[current.casefold()] = SourceColumn(old_table, old_column)
    return output


def build_table_merge_mapping(
    row: dict[str, Any],
    previous: SchemaSnapshot,
    *,
    source_join: SourceJoin | None = None,
) -> RelationEvolutionMapping:
    released = dict(row.get("old_new_table_mapping") or {})
    if len(released) != 2:
        raise ValueError("table merge requires exactly two source tables")
    previous_tables = _case_lookup(table.name for table in previous.tables)
    pairs = [
        (
            _resolve(previous_tables, old, kind="merge source table"),
            _clean_identifier(new),
        )
        for old, new in released.items()
    ]
    current_names = {new.casefold(): new for _, new in pairs}
    if len(current_names) != 1:
        raise ValueError("source tables do not map to one merged table")
    current_table = next(iter(current_names.values()))
    source_tables = tuple(old for old, _ in pairs)
    join = source_join or _source_join(source_tables, previous)
    relevant = dict(row.get("new_relevant_table") or {})
    relevant_name = _resolve(
        _case_lookup(relevant), current_table, kind="merged current table"
    )
    current_table = relevant_name
    released_columns = _released_columns(dict(relevant[current_table]))
    if not released_columns:
        raise ValueError("merged table has no released column list")
    explicit = _deduplicated_column_mapping(row, source_tables, previous)
    source_column_lookups = {
        table: _case_lookup(column.name for column in previous.by_name[table].columns)
        for table in source_tables
    }
    join_endpoints = {
        (join.left_table.casefold(), join.left_column.casefold()),
        (join.right_table.casefold(), join.right_column.casefold()),
    }
    primary_name = _clean_identifier(row.get("new_table_primary_key"))
    columns: list[ColumnSchema] = []
    columns_to_sources: dict[str, tuple[SourceColumn, ...]] = {}
    source_to_current: dict[tuple[str, str], str] = {}
    for current_column in released_columns:
        selected = explicit.get(current_column.casefold())
        candidates: list[SourceColumn] = []
        for table in source_tables:
            old = source_column_lookups[table].get(current_column.casefold())
            if old is not None:
                candidates.append(SourceColumn(table, old))
        if selected is None and len(candidates) == 1:
            selected = candidates[0]
        if (
            selected is None
            and candidates
            and primary_name
            and current_column.casefold() == primary_name.casefold()
        ):
            by_table = {candidate.table: candidate for candidate in candidates}
            selected = next(
                (
                    by_table[table]
                    for table in source_tables
                    if table in by_table
                ),
                None,
            )
        if selected is None and candidates:
            endpoint_candidates = [
                candidate
                for candidate in candidates
                if (candidate.table.casefold(), candidate.column.casefold())
                in join_endpoints
            ]
            if len(endpoint_candidates) == len(candidates):
                # Both names identify the same joined key value.
                selected = sorted(
                    endpoint_candidates,
                    key=lambda value: (value.table.casefold(), value.column.casefold()),
                )[0]
        if selected is None:
            raise ValueError(f"ambiguous merged column lineage: {current_column}")
        original = next(
            column
            for column in previous.by_name[selected.table].columns
            if column.name == selected.column
        )
        columns.append(
            ColumnSchema(
                name=current_column,
                declared_type=original.declared_type,
                not_null=original.not_null,
                primary_key=(
                    bool(primary_name)
                    and current_column.casefold() == primary_name.casefold()
                ),
                primary_key_ordinal=(
                    1
                    if bool(primary_name)
                    and current_column.casefold() == primary_name.casefold()
                    else 0
                ),
            )
        )
        columns_to_sources[current_column] = (selected,)
        source_to_current[(selected.table.casefold(), selected.column.casefold())] = (
            current_column
        )

    foreign_keys: list[ForeignKeySchema] = []
    source_set = {value.casefold() for value in source_tables}
    for source_table in source_tables:
        for edge in previous.by_name[source_table].foreign_keys:
            if edge.target_table.casefold() in source_set:
                continue
            current_column = source_to_current.get(
                (source_table.casefold(), edge.source_column.casefold())
            )
            if current_column:
                foreign_keys.append(
                    ForeignKeySchema(
                        current_column, edge.target_table, edge.target_column
                    )
                )
    added = [TableSchema(current_table, tuple(columns), tuple(foreign_keys))]
    # The two source-join endpoints represent the same value in the materialized
    # merge.  Propagate a missing endpoint lineage through that declared equality,
    # while never replacing an explicit released mapping.
    left_key = (join.left_table.casefold(), join.left_column.casefold())
    right_key = (join.right_table.casefold(), join.right_column.casefold())
    if left_key in source_to_current and right_key not in source_to_current:
        current_column = source_to_current[left_key]
        source_to_current[right_key] = current_column
        columns_to_sources[current_column] = tuple(
            dict.fromkeys(
                [
                    *columns_to_sources[current_column],
                    SourceColumn(join.right_table, join.right_column),
                ]
            )
        )
    elif right_key in source_to_current and left_key not in source_to_current:
        current_column = source_to_current[right_key]
        source_to_current[left_key] = current_column
        columns_to_sources[current_column] = tuple(
            dict.fromkeys(
                [
                    *columns_to_sources[current_column],
                    SourceColumn(join.left_table, join.left_column),
                ]
            )
        )

    # Merging can turn a formerly unique entity key into a repeated column.  An
    # incoming FK remains cardinality-safe only when its exact source target maps
    # to a declared primary key of the merged relation.  Other historical edges
    # are intentionally not emitted as current declared FKs.
    current_primary_columns = {
        column.name.casefold() for column in columns if column.primary_key
    }
    target_rebindings: dict[tuple[str, str], tuple[str, str]] = {
        source: (current_table, current_column)
        for source, current_column in source_to_current.items()
        if current_column.casefold() in current_primary_columns
    }
    current = _replace_tables(
        previous,
        removed=set(source_tables),
        added=added,
        target_rebindings=target_rebindings,
    )
    # The source relationship explains how the merged current view is
    # materialized, but its endpoints no longer exist in the current catalog.
    # Exposing it as an operational current join edge makes the graph silently
    # drop or misbind it.  Lineage documents retain the source join explicitly;
    # current relationship_edges contain only executable current endpoints.
    return RelationEvolutionMapping(
        evolution_type="table_merge",
        current_snapshot=current,
        table_sources={current_table: source_tables},
        column_sources={current_table: columns_to_sources},
        source_joins={current_table: (join,)},
        column_operations={},
        relationship_edges=(),
    )


def build_column_change_mapping(
    row: dict[str, Any], previous: SchemaSnapshot
) -> RelationEvolutionMapping:
    operation = str(row.get("split_or_merge") or "").casefold()
    if operation not in {"split", "merge"}:
        raise ValueError(f"unsupported column evolution: {operation}")
    changes = row.get("column_changes")
    relevant_values = dict(row.get("new_relevant_table") or {})
    relevant_lookup = _case_lookup(relevant_values)
    previous_lookup = _case_lookup(previous.by_name)
    specs: list[tuple[TableSchema, str, list[str], list[str]]] = []

    if isinstance(changes, dict) and len(changes) == 1:
        left, right = next(iter(changes.items()))
        if operation == "split":
            released_old = [_clean_identifier(left)]
            released_current = _split_mapping_values(right)
        else:
            released_current = [_clean_identifier(left)]
            released_old = _split_mapping_values(right)
        if not released_current or not released_old:
            raise ValueError("empty column evolution mapping")
        for supplied_table, current_value in relevant_values.items():
            old_name = previous_lookup.get(str(supplied_table).casefold())
            if old_name is None:
                continue
            old_table = previous.by_name[old_name]
            old_lookup = _case_lookup(column.name for column in old_table.columns)
            if not all(value.casefold() in old_lookup for value in released_old):
                continue
            released_names = {
                value.casefold() for value in _released_columns(dict(current_value))
            }
            if released_names and not all(
                value.casefold() in released_names for value in released_current
            ):
                continue
            resolved_old = [
                _resolve(old_lookup, value, kind="changed source column")
                for value in released_old
            ]
            current_table = relevant_lookup[str(supplied_table).casefold()]
            specs.append(
                (old_table, current_table, resolved_old, list(released_current))
            )
    else:
        # The released student_club merge rows contain an empty mapping.  Infer
        # only a uniquely determined schema diff: multiple removed columns to one
        # added column (or its exact split inverse).
        for supplied_table, current_value in relevant_values.items():
            old_name = previous_lookup.get(str(supplied_table).casefold())
            if old_name is None:
                continue
            old_table = previous.by_name[old_name]
            released_names = _released_columns(dict(current_value))
            if not released_names:
                continue
            old_names = [column.name for column in old_table.columns]
            old_lookup = _case_lookup(old_names)
            current_lookup = _case_lookup(released_names)
            removed = [
                name for name in old_names if name.casefold() not in current_lookup
            ]
            added = [
                name for name in released_names if name.casefold() not in old_lookup
            ]
            valid = (
                len(removed) == 1 and len(added) >= 2
                if operation == "split"
                else len(removed) >= 2 and len(added) == 1
            )
            if valid:
                specs.append(
                    (
                        old_table,
                        relevant_lookup[str(supplied_table).casefold()],
                        removed,
                        added,
                    )
                )
    if not specs:
        raise ValueError("column lineage is not recoverable from released schema diff")

    added_tables: list[TableSchema] = []
    removed_tables: set[str] = set()
    target_rebindings: dict[tuple[str, str], tuple[str, str]] = {}
    table_sources: dict[str, tuple[str, ...]] = {}
    columns_by_table: dict[str, dict[str, tuple[SourceColumn, ...]]] = {}
    operations_by_table: dict[str, dict[str, str]] = {}
    lineage_edges: list[dict[str, Any]] = []
    for old_table, current_table, resolved_old, current_columns in specs:
        removed = {value.casefold() for value in resolved_old}
        retained = [
            column
            for column in old_table.columns
            if column.name.casefold() not in removed
        ]
        source_example = next(
            column for column in old_table.columns if column.name == resolved_old[0]
        )
        added_columns = [
            ColumnSchema(
                name=name,
                declared_type=source_example.declared_type,
                not_null=source_example.not_null,
                primary_key=False,
                primary_key_ordinal=0,
            )
            for name in current_columns
        ]
        changed_names = {name.casefold() for name in current_columns}
        columns: list[ColumnSchema] = []
        inserted = False
        for column in old_table.columns:
            if column.name.casefold() in removed:
                if not inserted:
                    columns.extend(added_columns)
                    inserted = True
                continue
            if column.name.casefold() not in changed_names:
                columns.append(column)
        if not inserted:
            columns.extend(added_columns)

        column_sources: dict[str, tuple[SourceColumn, ...]] = {
            column.name: (SourceColumn(old_table.name, column.name),)
            for column in retained
        }
        column_operations: dict[str, str] = {}
        if operation == "split":
            source = SourceColumn(old_table.name, resolved_old[0])
            for current_column in current_columns:
                column_sources[current_column] = (source,)
                column_operations[current_column] = "split"
        else:
            column_sources[current_columns[0]] = tuple(
                SourceColumn(old_table.name, value) for value in resolved_old
            )
            column_operations[current_columns[0]] = "merge"

        changed_fk_columns = {
            edge.source_column.casefold() for edge in old_table.foreign_keys
        } & removed
        if changed_fk_columns:
            raise ValueError("column change rewrites a declared foreign key")
        added_tables.append(
            TableSchema(current_table, tuple(columns), old_table.foreign_keys)
        )
        removed_tables.add(old_table.name)
        # Retained columns keep exact incoming relationship endpoints.  Changed
        # split/merge values are not equality-preserving FK targets and are not
        # rebound without a dedicated relationship encoding.
        for current_column, sources in column_sources.items():
            if current_column in column_operations:
                continue
            for source in sources:
                target_rebindings[
                    (source.table.casefold(), source.column.casefold())
                ] = (current_table, current_column)
        table_sources[current_table] = (old_table.name,)
        columns_by_table[current_table] = column_sources
        operations_by_table[current_table] = column_operations
        for current_column, sources in column_sources.items():
            if current_column not in column_operations:
                continue
            for source in sources:
                lineage_edges.append(
                    {
                        "left": f"{old_table.name}.{source.column}",
                        "right": f"{current_table}.{current_column}",
                        "score": 1.0,
                        "evidence_types": [
                            f"evolution_column_{operation}_lineage"
                        ],
                        "provenance_ids": [
                            f"column_{operation}::{old_table.name}::{source.column}::"
                            f"{current_table}.{current_column}"
                        ],
                    }
                )
    current = _replace_tables(
        previous,
        removed=removed_tables,
        added=added_tables,
        target_rebindings=target_rebindings,
    )
    return RelationEvolutionMapping(
        evolution_type=f"column_{operation}",
        current_snapshot=current,
        table_sources=table_sources,
        column_sources=columns_by_table,
        source_joins={},
        column_operations=operations_by_table,
        relationship_edges=tuple(lineage_edges),
    )


def _current_schema_sets(
    snapshot: SchemaSnapshot,
) -> tuple[dict[str, str], dict[str, dict[str, str]]]:
    tables = _case_lookup(table.name for table in snapshot.tables)
    columns = {
        table.name: _case_lookup(column.name for column in table.columns)
        for table in snapshot.tables
    }
    return tables, columns


def _validate_current_identifiers(
    tree: exp.Expression, snapshot: SchemaSnapshot
) -> None:
    tables, columns = _current_schema_sets(snapshot)
    cte_names = {
        str(cte.alias_or_name).casefold() for cte in tree.find_all(exp.CTE)
    }
    for scope in traverse_scope(tree):
        aliases: dict[str, str] = {}
        local_tables: list[str] = []
        for table in scope.tables:
            if table.name.casefold() in cte_names:
                continue
            current = tables.get(table.name.casefold())
            if current is None:
                raise ValueError(f"table is absent from evolved schema: {table.name}")
            alias = str(table.alias_or_name)
            aliases[alias.casefold()] = current
            aliases[current.casefold()] = current
            local_tables.append(current)
        for column in scope.columns:
            if column.name == "*":
                continue
            qualifier = str(column.table or "")
            if qualifier:
                table = aliases.get(qualifier.casefold())
                # A projected column of a CTE/derived relation is outside the
                # physical current-schema namespace.
                if table is None:
                    continue
                if column.name.casefold() not in columns[table]:
                    raise ValueError(
                        f"column is absent from evolved schema: {table}.{column.name}"
                    )
                continue
            matches = [
                table
                for table in local_tables
                if column.name.casefold() in columns[table]
            ]
            if not matches and local_tables:
                # It can still be a SELECT alias used by ORDER/GROUP.  SQLite
                # performs the final validation after the structural rewrite.
                continue


def _hidden_name(table: str, sources: tuple[SourceColumn, ...], index: int) -> str:
    basis = json.dumps(
        [table, *[(source.table, source.column) for source in sources]],
        separators=(",", ":"),
        ensure_ascii=False,
    )
    return f"__evo_source_{sha256(basis.encode()).hexdigest()[:12]}_{index}"


def _identifier_tokens(value: str) -> tuple[str, ...]:
    """Tokenize snake_case, spaced, and CamelCase released identifiers."""

    separated = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1 \2", str(value))
    separated = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", separated)
    return tuple(re.findall(r"[a-z0-9]+", separated.casefold()))


def _split_expression_kind(
    current_column: str, sibling_columns: Iterable[str]
) -> str | None:
    tokens = set(_identifier_tokens(current_column))
    sibling_tokens = {
        token
        for sibling in sibling_columns
        for token in _identifier_tokens(sibling)
    }
    if "year" in tokens:
        return "iso_year"
    if "month" in tokens:
        return "iso_month"
    if "day" in tokens:
        return "iso_day"
    if "time" in tokens:
        return "iso_time"
    if "local" in tokens and {"email", "domain"} & sibling_tokens:
        return "email_local"
    if "domain" in tokens and {"email", "local"} & sibling_tokens:
        return "email_domain"
    if "protocol" in tokens:
        return "url_protocol"
    if "domain" in tokens and "protocol" in sibling_tokens:
        return "url_domain"
    return None


def _split_expression(
    source_sql: str,
    *,
    current_column: str,
    sibling_columns: Iterable[str],
) -> str:
    kind = _split_expression_kind(current_column, sibling_columns)
    if kind == "iso_year":
        return f"strftime('%Y', {source_sql})"
    if kind == "iso_month":
        return f"strftime('%m', {source_sql})"
    if kind == "iso_day":
        return f"strftime('%d', {source_sql})"
    if kind == "iso_time":
        return f"strftime('%H:%M:%S', {source_sql})"
    if kind == "email_local":
        return (
            f"CASE WHEN instr({source_sql}, '@') > 0 "
            f"THEN substr({source_sql}, 1, instr({source_sql}, '@') - 1) "
            f"ELSE {source_sql} END"
        )
    if kind == "email_domain":
        return (
            f"CASE WHEN instr({source_sql}, '@') > 0 "
            f"THEN substr({source_sql}, instr({source_sql}, '@') + 1) "
            f"ELSE {source_sql} END"
        )
    if kind == "url_protocol":
        return (
            f"CASE WHEN instr({source_sql}, '://') > 0 "
            f"THEN substr({source_sql}, 1, instr({source_sql}, '://') - 1) "
            f"ELSE '' END"
        )
    if kind == "url_domain":
        return (
            f"CASE WHEN instr({source_sql}, '://') > 0 "
            f"THEN substr({source_sql}, instr({source_sql}, '://') + 3) "
            f"ELSE {source_sql} END"
        )
    # Unknown released encodings cannot be reconstructed faithfully from the
    # immutable source database.  The fallback keeps execution available for
    # diagnostics, but callers must mark the virtual semantics unsupported.
    return source_sql


def _merge_expression(sources: list[str], source_names: list[str]) -> str:
    separator = "-" if {"year", "month", "day"} <= {
        value.casefold() for value in source_names
    } else " "
    parts = [f"COALESCE(CAST({source} AS TEXT), '')" for source in sources]
    return "TRIM(" + f" || '{separator}' || ".join(parts) + ")"


def virtual_semantics_report(
    mapping: RelationEvolutionMapping,
    *,
    previous_snapshot: SchemaSnapshot | None = None,
) -> dict[str, Any]:
    """Describe whether the immutable-storage view has defensible current semantics.

    This is deliberately stricter than executability.  Unsupported split encodings,
    composite-key table splits, and role-ambiguous table merges may execute but are
    not safe evidence about current-schema execution accuracy.
    """

    unsupported: list[dict[str, Any]] = []
    if mapping.evolution_type == "column_split":
        for table, operations in mapping.column_operations.items():
            groups: dict[tuple[str, str], list[str]] = {}
            for column, operation in operations.items():
                if operation != "split":
                    continue
                sources = mapping.column_sources[table][column]
                if len(sources) != 1:
                    unsupported.append(
                        {"table": table, "column": column, "reason": "non_unary_split"}
                    )
                    continue
                source = sources[0]
                groups.setdefault((source.table, source.column), []).append(column)
            for (_source_table, _source_column), siblings in groups.items():
                for column in siblings:
                    if _split_expression_kind(column, siblings) is None:
                        unsupported.append(
                            {
                                "table": table,
                                "column": column,
                                "reason": "unsupported_split_encoding",
                            }
                        )
    elif mapping.evolution_type == "column_merge":
        for table, operations in mapping.column_operations.items():
            for column, operation in operations.items():
                if operation != "merge":
                    continue
                source_names = [
                    source.column for source in mapping.column_sources[table][column]
                ]
                if {value.casefold() for value in source_names} != {
                    "year",
                    "month",
                    "day",
                }:
                    unsupported.append(
                        {
                            "table": table,
                            "column": column,
                            "reason": "unspecified_merge_serialization",
                        }
                    )
    elif mapping.evolution_type == "table_split":
        evolution_keys = [
            edge
            for edge in mapping.relationship_edges
            if "evolution_split_key_equivalence"
            in set(edge.get("evidence_types") or [])
        ]
        if not evolution_keys:
            unsupported.append({"reason": "no_single_column_split_key_certificate"})
        if previous_snapshot is not None:
            for source_table in sorted(
                {
                    source
                    for sources in mapping.table_sources.values()
                    for source in sources
                }
            ):
                source = previous_snapshot.by_name.get(source_table)
                if source is None:
                    unsupported.append(
                        {"table": source_table, "reason": "missing_source_table"}
                    )
                    continue
                primary_key = [
                    column.name
                    for column in source.columns
                    if column.primary_key_ordinal > 0
                ]
                if len(primary_key) != 1:
                    unsupported.append(
                        {
                            "table": source_table,
                            "reason": "composite_or_missing_source_primary_key",
                            "primary_key": primary_key,
                        }
                    )
    elif mapping.evolution_type == "table_merge":
        for current_table, source_tables in mapping.table_sources.items():
            joins = mapping.source_joins.get(current_table, ())
            if len(joins) != 1 or joins[0].evidence_type != "declared_foreign_key":
                unsupported.append(
                    {
                        "table": current_table,
                        "reason": "non_unique_or_inferred_source_join",
                    }
                )
                continue
            if previous_snapshot is not None:
                try:
                    declared = _source_join(source_tables, previous_snapshot)
                except (NoDeclaredSourceJoinError, AmbiguousSourceJoinError) as error:
                    unsupported.append(
                        {
                            "table": current_table,
                            "reason": type(error).__name__,
                        }
                    )
                else:
                    if declared != joins[0]:
                        unsupported.append(
                            {
                                "table": current_table,
                                "reason": "source_join_mismatch",
                            }
                        )
    return {
        "certified": not unsupported,
        "evolution_type": mapping.evolution_type,
        "unsupported": unsupported,
    }


def _relation_select_sql(
    current_table: str, mapping: RelationEvolutionMapping
) -> str:
    sources = mapping.table_sources[current_table]
    aliases = {table: f"__evo_s{index}" for index, table in enumerate(sources)}
    current = mapping.current_snapshot.by_name[current_table]
    operations = mapping.column_operations.get(current_table, {})
    by_source_group: dict[tuple[str, str], list[str]] = {}
    for column, column_sources in mapping.column_sources[current_table].items():
        if operations.get(column) == "split" and len(column_sources) == 1:
            source = column_sources[0]
            by_source_group.setdefault((source.table, source.column), []).append(column)

    projections: list[str] = []
    hidden_seen: set[str] = set()
    for column in current.columns:
        column_sources = mapping.column_sources[current_table].get(column.name)
        if not column_sources:
            raise ValueError(
                f"current column has no storage lineage: {current_table}.{column.name}"
            )
        source_sql = [
            f"{_quote(aliases[source.table])}.{_quote(source.column)}"
            for source in column_sources
        ]
        operation = operations.get(column.name)
        if operation == "merge":
            expression = _merge_expression(
                source_sql, [source.column for source in column_sources]
            )
        elif operation == "split":
            source = column_sources[0]
            expression = _split_expression(
                source_sql[0],
                current_column=column.name,
                sibling_columns=by_source_group[(source.table, source.column)],
            )
        else:
            expression = source_sql[0]
        projections.append(f"{expression} AS {_quote(column.name)}")
        if operation in {"split", "merge"}:
            for index, item in enumerate(source_sql):
                hidden = _hidden_name(current_table, column_sources, index)
                if hidden in hidden_seen:
                    continue
                hidden_seen.add(hidden)
                projections.append(f"{item} AS {_quote(hidden)}")

    first = sources[0]
    from_sql = f"FROM {_quote(first)} AS {_quote(aliases[first])}"
    visited = {first}
    joins_sql: list[str] = []
    pending = list(mapping.source_joins.get(current_table, ()))
    while pending:
        progressed = False
        for edge in list(pending):
            if edge.left_table in visited and edge.right_table not in visited:
                parent, child = edge.left_table, edge.right_table
                parent_column, child_column = edge.left_column, edge.right_column
            elif edge.right_table in visited and edge.left_table not in visited:
                parent, child = edge.right_table, edge.left_table
                parent_column, child_column = edge.right_column, edge.left_column
            else:
                continue
            joins_sql.append(
                f"JOIN {_quote(child)} AS {_quote(aliases[child])} ON "
                f"{_quote(aliases[parent])}.{_quote(parent_column)} = "
                f"{_quote(aliases[child])}.{_quote(child_column)}"
            )
            visited.add(child)
            pending.remove(edge)
            progressed = True
        if not progressed:
            raise ValueError(f"source joins do not connect current table: {current_table}")
    if visited != set(sources):
        raise ValueError(f"source relation is disconnected: {current_table}")
    return "\n".join(
        ["SELECT " + ",\n  ".join(projections), from_sql, *joins_sql]
    )


def _direct_aliases(select: exp.Select) -> dict[str, str]:
    sources: list[exp.Expression] = []
    from_clause = select.args.get("from_")
    if from_clause is not None and from_clause.this is not None:
        sources.append(from_clause.this)
    sources.extend(join.this for join in select.args.get("joins") or [])
    output: dict[str, str] = {}
    for source in sources:
        if not isinstance(source, exp.Table):
            continue
        output[str(source.alias_or_name).casefold()] = str(source.name)
        output[str(source.name).casefold()] = str(source.name)
    return output


def _restore_projection_shape(
    tree: exp.Expression, mapping: RelationEvolutionMapping
) -> None:
    """Return changed top-level fields in the immutable source result shape."""

    current_lookup = _case_lookup(mapping.current_snapshot.by_name)
    for select in list(tree.find_all(exp.Select)):
        aliases = _direct_aliases(select)
        if not aliases:
            continue
        output: list[exp.Expression] = []
        emitted_split_groups: set[tuple[str, str, str]] = set()
        for projection in select.expressions:
            column = projection
            if isinstance(projection, exp.Alias):
                column = projection.this
            if not isinstance(column, exp.Column):
                output.append(projection)
                continue
            qualifier = str(column.table or "")
            if qualifier:
                supplied_table = aliases.get(qualifier.casefold())
            else:
                direct_tables = list(dict.fromkeys(aliases.values()))
                supplied_table = direct_tables[0] if len(direct_tables) == 1 else None
            if supplied_table is None:
                output.append(projection)
                continue
            current_table = current_lookup.get(supplied_table.casefold())
            if current_table is None:
                output.append(projection)
                continue
            columns = mapping.column_sources.get(current_table, {})
            current_column = next(
                (
                    name
                    for name in columns
                    if name.casefold() == column.name.casefold()
                ),
                None,
            )
            operation = mapping.column_operations.get(current_table, {}).get(
                current_column or ""
            )
            if operation not in {"split", "merge"} or current_column is None:
                output.append(projection)
                continue
            if isinstance(projection, exp.Alias):
                raise ValueError("aliased changed-column projection is unsupported")
            sources = columns[current_column]
            rendered_qualifier = qualifier or supplied_table
            if operation == "split":
                source = sources[0]
                group = (
                    current_table.casefold(),
                    source.table.casefold(),
                    source.column.casefold(),
                )
                if group in emitted_split_groups:
                    continue
                emitted_split_groups.add(group)
                hidden = _hidden_name(current_table, sources, 0)
                output.append(
                    exp.column(hidden, table=rendered_qualifier, quoted=True)
                )
            else:
                output.extend(
                    exp.column(
                        _hidden_name(current_table, sources, index),
                        table=rendered_qualifier,
                        quoted=True,
                    )
                    for index, _source in enumerate(sources)
                )
        select.set("expressions", output)


def reverse_map_evolved_sql(
    sql: str,
    *,
    mapping: RelationEvolutionMapping,
    dialect: str = "sqlite",
    preserve_current_projection: bool = True,
) -> str:
    """Compile current identifiers and relations onto immutable source storage.

    Current output shape is preserved by default.  Setting
    ``preserve_current_projection=False`` is a legacy adapter diagnostic that
    reconstructs historical source columns; it must never be used to score
    current-schema predictions against evolved gold.
    """

    if not sql.strip():
        raise ValueError("SQL must not be empty")
    tree = sqlglot.parse_one(sql, read=dialect)
    _validate_current_identifiers(tree, mapping.current_snapshot)
    if not preserve_current_projection:
        _restore_projection_shape(tree, mapping)
    current_lookup = _case_lookup(mapping.current_snapshot.by_name)
    table_nodes = [
        table
        for table in tree.find_all(exp.Table)
        if table.name.casefold() in current_lookup
        and current_lookup[table.name.casefold()] in mapping.table_sources
    ]
    for table in table_nodes:
        current_table = current_lookup[table.name.casefold()]
        sources = mapping.table_sources[current_table]
        operations = mapping.column_operations.get(current_table, {})
        explicit_alias = str(table.alias or "")
        alias = explicit_alias or current_table
        direct_split = (
            len(sources) == 1
            and not operations
            and current_table.casefold() != sources[0].casefold()
        )
        if direct_split:
            replacement = exp.Table(
                this=exp.to_identifier(sources[0], quoted=True),
                alias=exp.TableAlias(this=exp.to_identifier(alias, quoted=True)),
            )
        else:
            relation = sqlglot.parse_one(
                _relation_select_sql(current_table, mapping), read="sqlite"
            )
            replacement = exp.Subquery(
                this=relation,
                alias=exp.TableAlias(this=exp.to_identifier(alias, quoted=True)),
            )
        table.replace(replacement)
    return tree.sql(dialect=dialect)


def _source_column_targets(
    mapping: RelationEvolutionMapping,
    source_table: str,
    source_column: str,
) -> list[tuple[str, str]]:
    output: list[tuple[str, str]] = []
    for current_table, columns in mapping.column_sources.items():
        for current_column, sources in columns.items():
            if any(
                source.table.casefold() == source_table.casefold()
                and source.column.casefold() == source_column.casefold()
                for source in sources
            ):
                output.append((current_table, current_column))
    if output:
        return list(dict.fromkeys(output))
    current_table = next(
        (
            table
            for table in mapping.current_snapshot.tables
            if table.name.casefold() == source_table.casefold()
        ),
        None,
    )
    if current_table is not None:
        current_column = next(
            (
                column.name
                for column in current_table.columns
                if column.name.casefold() == source_column.casefold()
            ),
            None,
        )
        if current_column is not None:
            return [(current_table.name, current_column)]
    return []


def _source_table_targets(
    mapping: RelationEvolutionMapping, source_table: str
) -> list[str]:
    output = [
        current_table
        for current_table, sources in mapping.table_sources.items()
        if any(source.casefold() == source_table.casefold() for source in sources)
    ]
    if output:
        return output
    current = next(
        (
            table.name
            for table in mapping.current_snapshot.tables
            if table.name.casefold() == source_table.casefold()
        ),
        None,
    )
    return [current] if current else []


def _split_program_join(
    *,
    mapping: RelationEvolutionMapping,
    left_table: str,
    left_alias: str,
    right_table: str,
    right_alias: str,
) -> exp.Join:
    def endpoint(value: Any) -> tuple[str, str] | None:
        table, separator, column = str(value or "").rpartition(".")
        if not separator or not table or not column:
            return None
        return table, column

    candidates = []
    for edge in mapping.relationship_edges:
        if "evolution_split_key_equivalence" not in set(
            edge.get("evidence_types") or []
        ):
            continue
        left_endpoint = endpoint(edge.get("left"))
        right_endpoint = endpoint(edge.get("right"))
        if left_endpoint is None or right_endpoint is None:
            continue
        endpoint_tables = {
            left_endpoint[0].casefold(),
            right_endpoint[0].casefold(),
        }
        if endpoint_tables != {left_table.casefold(), right_table.casefold()}:
            continue
        candidates.append((left_endpoint, right_endpoint))
    if len(candidates) != 1:
        raise ValueError(
            "historical program requires one certified split-key relation between "
            f"{left_table} and {right_table}"
        )
    left_endpoint, right_endpoint = candidates[0]
    endpoint_alias = {
        left_table.casefold(): left_alias,
        right_table.casefold(): right_alias,
    }
    condition = exp.EQ(
        this=exp.column(
            left_endpoint[1],
            table=endpoint_alias[left_endpoint[0].casefold()],
            quoted=True,
        ),
        expression=exp.column(
            right_endpoint[1],
            table=endpoint_alias[right_endpoint[0].casefold()],
            quoted=True,
        ),
    )
    return exp.Join(
        this=exp.Table(
            this=exp.to_identifier(right_table, quoted=True),
            alias=exp.TableAlias(this=exp.to_identifier(right_alias, quoted=True)),
        ),
        on=condition,
    )


def translate_source_program_to_current(
    sql: str,
    *,
    mapping: RelationEvolutionMapping,
    dialect: str = "sqlite",
) -> str:
    """Conservatively rebind a simple historical SQL program to current lineage.

    The translation preserves operators and literals, collapses an unambiguous
    table merge, expands a single-key table split, and expands a compound column
    projection.  Ambiguous filters, self joins, composite split relations, and
    nested queries are rejected rather than exposed to the generator as stale SQL.
    """

    tree = sqlglot.parse_one(sql, read=dialect)
    if not isinstance(tree, exp.Select) or tree.args.get("with_") is not None:
        raise ValueError("historical program must be one simple SELECT")
    if any(node is not tree for node in tree.find_all(exp.Select)):
        raise ValueError("nested historical programs are unsupported")
    from_clause = tree.args.get("from_")
    if from_clause is None or not isinstance(from_clause.this, exp.Table):
        raise ValueError("historical program has no direct source table")
    joins = list(tree.args.get("joins") or [])
    if any(not isinstance(join.this, exp.Table) for join in joins):
        raise ValueError("historical program contains a derived table")

    source_records: list[dict[str, Any]] = []
    for table, join in [(from_clause.this, None), *((join.this, join) for join in joins)]:
        source_table = str(table.name)
        alias = str(table.alias_or_name)
        if any(record["alias"].casefold() == alias.casefold() for record in source_records):
            raise ValueError("duplicate historical table alias")
        targets = _source_table_targets(mapping, source_table)
        if not targets:
            raise ValueError(f"historical table has no current lineage: {source_table}")
        source_records.append(
            {
                "table": source_table,
                "alias": alias,
                "node": table,
                "join": join,
                "table_targets": targets,
                "required": [],
            }
        )
    record_by_alias = {
        record["alias"].casefold(): record for record in source_records
    }
    record_by_table: dict[str, list[dict[str, Any]]] = {}
    for record in source_records:
        record_by_table.setdefault(record["table"].casefold(), []).append(record)

    direct_projection: dict[int, exp.Expression] = {}
    for projection in tree.expressions:
        node = projection.this if isinstance(projection, exp.Alias) else projection
        if isinstance(node, exp.Column):
            direct_projection[id(node)] = projection

    column_plans: dict[int, dict[str, Any]] = {}
    for column in list(tree.find_all(exp.Column)):
        if column.name == "*":
            continue
        qualifier = str(column.table or "")
        if qualifier:
            record = record_by_alias.get(qualifier.casefold())
            if record is None:
                raise ValueError(f"unknown historical qualifier: {qualifier}")
        else:
            candidates = [
                record
                for record in source_records
                if _source_column_targets(mapping, record["table"], str(column.name))
            ]
            if len(candidates) != 1:
                raise ValueError(f"ambiguous historical column: {column.name}")
            record = candidates[0]
        targets = _source_column_targets(
            mapping, record["table"], str(column.name)
        )
        if not targets:
            raise ValueError(
                f"historical column has no current lineage: "
                f"{record['table']}.{column.name}"
            )
        target_tables = list(dict.fromkeys(table for table, _column in targets))
        for target_table in target_tables:
            if target_table not in record["required"]:
                record["required"].append(target_table)
        same_table_split = len(targets) > 1 and len(target_tables) == 1
        if same_table_split and id(column) not in direct_projection:
            raise ValueError(
                "a split historical column is only safe as a direct projection"
            )
        column_plans[id(column)] = {
            "node": column,
            "record": record,
            "targets": targets,
            "same_table_split": same_table_split,
        }

    for record in source_records:
        if not record["required"]:
            record["required"].append(record["table_targets"][0])
        if len(record_by_table[record["table"].casefold()]) > 1:
            raise ValueError("historical self joins are not conservatively translatable")

    alias_for: dict[tuple[str, str], str] = {}
    merged_alias: dict[str, str] = {}
    for record in source_records:
        base_alias = record["alias"]
        for offset, current_table in enumerate(record["required"]):
            key = current_table.casefold()
            is_merge = len(mapping.table_sources.get(current_table, ())) > 1
            if is_merge and key in merged_alias:
                alias = merged_alias[key]
            else:
                alias = base_alias if offset == 0 else f"{base_alias}__evo{offset + 1}"
                if is_merge:
                    merged_alias[key] = alias
            alias_for[(record["alias"].casefold(), key)] = alias

    expanded_projection: dict[int, list[exp.Expression]] = {}
    for plan in column_plans.values():
        column = plan["node"]
        record = plan["record"]
        targets = plan["targets"]
        if plan["same_table_split"]:
            projection = direct_projection[id(column)]
            if isinstance(projection, exp.Alias):
                raise ValueError("aliased split historical projection is unsupported")
            expanded_projection[id(projection)] = [
                exp.column(
                    target_column,
                    table=alias_for[
                        (record["alias"].casefold(), target_table.casefold())
                    ],
                    quoted=True,
                )
                for target_table, target_column in targets
            ]
            continue
        if len(targets) == 1:
            target_table, target_column = targets[0]
        else:
            # A copied table-split key can bind to any required split table; use
            # the root copy so all references remain coherent.
            root_table = record["required"][0]
            target_table, target_column = next(
                (
                    target
                    for target in targets
                    if target[0].casefold() == root_table.casefold()
                ),
                targets[0],
            )
        column.set("this", exp.to_identifier(target_column, quoted=True))
        column.set(
            "table",
            exp.to_identifier(
                alias_for[(record["alias"].casefold(), target_table.casefold())],
                quoted=True,
            ),
        )

    if expanded_projection:
        new_expressions: list[exp.Expression] = []
        for projection in tree.expressions:
            new_expressions.extend(expanded_projection.get(id(projection), [projection]))
        tree.set("expressions", new_expressions)

    emitted_current: set[str] = set()
    base_record = source_records[0]
    base_table = base_record["required"][0]
    base_alias = alias_for[(base_record["alias"].casefold(), base_table.casefold())]
    from_clause.set(
        "this",
        exp.Table(
            this=exp.to_identifier(base_table, quoted=True),
            alias=exp.TableAlias(this=exp.to_identifier(base_alias, quoted=True)),
        ),
    )
    emitted_current.add(base_table.casefold())
    new_joins: list[exp.Join] = []

    def append_split_expansion(record: dict[str, Any], root_table: str) -> None:
        connected = {root_table.casefold()}
        pending = list(record["required"])
        pending.remove(root_table)
        while pending:
            progressed = False
            for current_table in list(pending):
                for connected_table_cf in list(connected):
                    connected_table = next(
                        value
                        for value in record["required"]
                        if value.casefold() == connected_table_cf
                    )
                    try:
                        join = _split_program_join(
                            mapping=mapping,
                            left_table=connected_table,
                            left_alias=alias_for[
                                (
                                    record["alias"].casefold(),
                                    connected_table.casefold(),
                                )
                            ],
                            right_table=current_table,
                            right_alias=alias_for[
                                (record["alias"].casefold(), current_table.casefold())
                            ],
                        )
                    except ValueError:
                        continue
                    new_joins.append(join)
                    connected.add(current_table.casefold())
                    emitted_current.add(current_table.casefold())
                    pending.remove(current_table)
                    progressed = True
                    break
                if progressed:
                    break
            if not progressed:
                raise ValueError("required split tables are not key-connected")

    append_split_expansion(base_record, base_table)
    for record in source_records[1:]:
        root_table = record["required"][0]
        root_key = root_table.casefold()
        is_collapsed_merge = root_key in emitted_current and len(
            mapping.table_sources.get(root_table, ())
        ) > 1
        if is_collapsed_merge:
            continue
        original_join = record["join"]
        assert isinstance(original_join, exp.Join)
        alias = alias_for[(record["alias"].casefold(), root_key)]
        rewritten = original_join.copy()
        rewritten.set(
            "this",
            exp.Table(
                this=exp.to_identifier(root_table, quoted=True),
                alias=exp.TableAlias(this=exp.to_identifier(alias, quoted=True)),
            ),
        )
        new_joins.append(rewritten)
        emitted_current.add(root_key)
        append_split_expansion(record, root_table)
    tree.set("joins", new_joins)

    # Multiple historical projections can collapse onto one merged current
    # column.  Remove exact duplicate output expressions without touching more
    # complex expressions or aliases.
    deduplicated: list[exp.Expression] = []
    seen_direct: set[str] = set()
    for projection in tree.expressions:
        if isinstance(projection, exp.Column):
            signature = projection.sql(dialect=dialect).casefold()
            if signature in seen_direct:
                continue
            seen_direct.add(signature)
        deduplicated.append(projection)
    tree.set("expressions", deduplicated)
    return tree.sql(dialect=dialect)


def build_evolution_documents(
    mapping: RelationEvolutionMapping, context_id: str
) -> tuple[list[CatalogDocument], dict[str, list[str]], list[dict[str, Any]]]:
    """Compile current catalog, typed lineage documents, bindings, and edges."""

    output: list[CatalogDocument] = []
    bindings: dict[str, list[str]] = {}
    operational_edges: list[dict[str, Any]] = []
    for table in mapping.current_snapshot.tables:
        fk_by_column = {
            edge.source_column.casefold(): edge for edge in table.foreign_keys
        }
        lines = []
        for column in table.columns:
            annotations: list[str] = []
            if column.primary_key:
                annotations.append("PRIMARY KEY")
            foreign_key = fk_by_column.get(column.name.casefold())
            if foreign_key is not None:
                annotations.append(
                    f"REFERENCES {_quote(foreign_key.target_table)}"
                    f"({_quote(foreign_key.target_column)})"
                )
            suffix = f" -- {'; '.join(annotations)}" if annotations else ""
            lines.append(
                f"  {_quote(column.name)} {column.declared_type or 'unknown'}{suffix}"
            )
            output.append(
                CatalogDocument(
                    candidate_id=f"column::{context_id}::{table.name}::{column.name}",
                    database_id=context_id,
                    kind="column",
                    table=table.name,
                    name=f"{table.name}.{column.name}",
                    text=(
                        f"current physical SQLite identifier: {_quote(table.name)}."
                        f"{_quote(column.name)}\ntype: {column.declared_type or 'unknown'}"
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
                    [f"CREATE TABLE {_quote(table.name)} (", *lines, ");"]
                ),
                references=tuple(
                    dict.fromkeys(edge.target_table for edge in table.foreign_keys)
                ),
            )
        )
        for edge in table.foreign_keys:
            operational_edges.append(
                {
                    "left": f"{table.name}.{edge.source_column}",
                    "right": f"{edge.target_table}.{edge.target_column}",
                    "score": 1.0,
                    "evidence_types": ["declared_foreign_key"],
                    "provenance_ids": [
                        f"current_fk::{context_id}::{table.name}."
                        f"{edge.source_column}::{edge.target_table}."
                        f"{edge.target_column}"
                    ],
                }
            )

    for current_table, source_tables in sorted(mapping.table_sources.items()):
        if (current_table,) == source_tables and not mapping.column_operations.get(
            current_table
        ):
            continue
        candidate_id = f"evolution_table::{context_id}::{current_table}"
        current_lineage = {
            current_column: [
                f"{source.table}.{source.column}" for source in sources
            ]
            for current_column, sources in sorted(
                mapping.column_sources.get(current_table, {}).items()
            )
        }
        output.append(
            CatalogDocument(
                candidate_id=candidate_id,
                database_id=context_id,
                kind="schema_evolution_table_lineage",
                table=current_table,
                name=current_table,
                text=json.dumps(
                    {
                        "current_physical_table": current_table,
                        "historical_source_tables": list(source_tables),
                        "historical_source_joins": [
                            edge.to_json()
                            for edge in mapping.source_joins.get(current_table, ())
                        ],
                        "current_column_lineage": current_lineage,
                        "relation": mapping.evolution_type,
                        "evidence": "released_schema_mapping",
                    },
                    ensure_ascii=False,
                    sort_keys=True,
                ),
            )
        )
        bindings[candidate_id] = [f"table::{context_id}::{current_table}"]

        # Table split/merge can rename or deduplicate individual columns even
        # though it is not a column-operation benchmark row.  Emit one typed
        # binding per current column so retrieval does not have to infer those
        # rebindings from a large table-level JSON blob.
        for current_column, sources in sorted(
            mapping.column_sources.get(current_table, {}).items()
        ):
            lineage_id = (
                f"evolution_relation_column::{context_id}::{current_table}::"
                f"{current_column}"
            )
            output.append(
                CatalogDocument(
                    candidate_id=lineage_id,
                    database_id=context_id,
                    kind="schema_evolution_relation_column_lineage",
                    table=current_table,
                    name=f"{current_table}.{current_column}",
                    text=json.dumps(
                        {
                            "current_physical_identifier": (
                                f"{current_table}.{current_column}"
                            ),
                            "historical_source_identifiers": [
                                f"{source.table}.{source.column}"
                                for source in sources
                            ],
                            "relation": mapping.evolution_type,
                            "evidence": "released_schema_mapping",
                        },
                        ensure_ascii=False,
                        sort_keys=True,
                    ),
                )
            )
            bindings[lineage_id] = [
                f"table::{context_id}::{current_table}",
                f"column::{context_id}::{current_table}::{current_column}",
            ]

    for current_table, operations in sorted(mapping.column_operations.items()):
        for current_column, operation in sorted(operations.items()):
            sources = mapping.column_sources[current_table][current_column]
            candidate_id = (
                f"evolution_column::{context_id}::{current_table}::{current_column}"
            )
            output.append(
                CatalogDocument(
                    candidate_id=candidate_id,
                    database_id=context_id,
                    kind="schema_evolution_column_lineage",
                    table=current_table,
                    name=f"{current_table}.{current_column}",
                    text=json.dumps(
                        {
                            "current_physical_identifier": (
                                f"{current_table}.{current_column}"
                            ),
                            "historical_source_identifiers": [
                                f"{source.table}.{source.column}" for source in sources
                            ],
                            "relation": f"column_{operation}",
                            "evidence": "released_schema_mapping",
                        },
                        ensure_ascii=False,
                        sort_keys=True,
                    ),
                )
            )
            bindings[candidate_id] = [
                f"table::{context_id}::{current_table}",
                f"column::{context_id}::{current_table}::{current_column}",
            ]
    edge_by_signature: dict[tuple[str, str], dict[str, Any]] = {}
    for edge in [*operational_edges, *mapping.relationship_edges]:
        signature = tuple(
            sorted((str(edge.get("left") or ""), str(edge.get("right") or "")))
        )
        previous = edge_by_signature.get(signature)
        if previous is None:
            edge_by_signature[signature] = dict(edge)
            continue
        previous["score"] = max(
            float(previous.get("score") or 0.0),
            float(edge.get("score") or 0.0),
        )
        previous["evidence_types"] = list(
            dict.fromkeys(
                [
                    *previous.get("evidence_types", []),
                    *edge.get("evidence_types", []),
                ]
            )
        )
        previous["provenance_ids"] = list(
            dict.fromkeys(
                [
                    *previous.get("provenance_ids", []),
                    *edge.get("provenance_ids", []),
                ]
            )
        )
    return output, bindings, list(edge_by_signature.values())


class EvolutionSQLiteAgentTools(SQLiteAgentTools):
    """Expose a relation-changing current catalog over immutable SQLite storage."""

    def __init__(
        self,
        database: Path,
        database_id: str,
        search_index: SchemaSearchIndex,
        *,
        mapping: RelationEvolutionMapping,
        expose_evolution_evidence: bool = True,
    ) -> None:
        self.evolution_mapping = mapping
        self.expose_evolution_evidence = bool(expose_evolution_evidence)
        super().__init__(database, database_id, search_index)
        if not self.expose_evolution_evidence:
            # Relation-change assets use an internal key such as
            # ``evoschema::column_merge::...``.  That key is needed to select the
            # immutable runtime mapping, but exposing it in prompts or candidate
            # IDs tells a current-catalog baseline which evolution occurred.
            self.public_database_id = "current_catalog"
        self.columns = {
            table.name: [
                (column.name, column.declared_type) for column in table.columns
            ]
            for table in mapping.current_snapshot.tables
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
            for table in mapping.current_snapshot.tables
        }
        self.join_edges = self._join_edges()
        observed = {
            tuple(
                sorted(
                    (str(edge["left"]).casefold(), str(edge["right"]).casefold())
                )
            )
            for edge in self.join_edges
        }
        extra_relationship_evidence = (
            [
                *mapping.relationship_edges,
                *search_index.ontology_edges_by_database.get(database_id, []),
            ]
            if self.expose_evolution_evidence
            else []
        )
        for source in extra_relationship_evidence:
            edge = dict(source)
            key = tuple(
                sorted(
                    (str(edge["left"]).casefold(), str(edge["right"]).casefold())
                )
            )
            if key in observed:
                continue
            evidence = edge.get("evidence") or edge.get("evidence_types") or []
            if isinstance(evidence, list):
                edge.setdefault("evidence", "+".join(str(value) for value in evidence))
            edge.setdefault("score", 1.0)
            self.join_edges.append(edge)
            observed.add(key)

    def _public_search_payload(self, value: Any) -> Any:
        published = super()._public_search_payload(value)
        if self.expose_evolution_evidence or not isinstance(published, dict):
            return published
        # The current-only baseline contract is stronger than merely removing
        # graph edges: even if a caller accidentally supplies a lineage-enriched
        # index, only ordinary current table/column catalog rows may reach the
        # model.  Keep a small explicit allow-list instead of trying to enumerate
        # every possible historical/evolution metadata field.
        if "results" not in published:
            return published
        safe_results = []
        allowed = {
            "rank",
            "probe",
            "evidence_candidate_id",
            "kind",
            "physical_name",
            "physical_table",
            "evidence",
        }
        for source in published.get("results") or []:
            row = dict(source)
            if str(row.get("kind") or "") not in {"table", "column"}:
                continue
            safe_results.append(
                {key: row[key] for key in allowed if key in row}
            )
        output = {
            key: item
            for key, item in published.items()
            if key
            in {
                "query",
                "queries",
                "results",
                "bridge_tables",
                "bound_physical_anchors",
                "evidence_budget",
                "expansion_calls_remaining",
                "evidence_boundary",
            }
        }
        output["results"] = safe_results
        output["bridge_tables"] = []
        output["bound_physical_anchors"] = []
        return output

    def _direct_source(self, table: str, column: str) -> SourceColumn | None:
        current_table = next(
            (
                name
                for name in self.columns
                if name.casefold() == str(table).casefold()
            ),
            None,
        )
        if current_table is None:
            return None
        current_column = next(
            (
                name
                for name, _kind in self.columns[current_table]
                if name.casefold() == str(column).casefold()
            ),
            None,
        )
        if current_column is None:
            return None
        sources = self.evolution_mapping.column_sources.get(
            current_table, {}
        ).get(current_column)
        operation = self.evolution_mapping.column_operations.get(
            current_table, {}
        ).get(current_column)
        if sources is None:
            return SourceColumn(current_table, current_column)
        if len(sources) != 1 or operation in {"split", "merge"}:
            return None
        return sources[0]

    def _value_relation(
        self, table: str, column: str
    ) -> tuple[str, str, str] | None:
        """Return FROM SQL, value SQL, and provenance for a current column."""

        source = self._direct_source(table, column)
        if source is not None:
            return (
                f"FROM {_quote(source.table)}",
                _quote(source.column),
                (
                    "exact_storage_value_through_lineage"
                    if self.expose_evolution_evidence
                    else "current_database_value"
                ),
            )
        current_table = next(
            (
                name
                for name in self.columns
                if name.casefold() == str(table).casefold()
            ),
            None,
        )
        if current_table is None or current_table not in self.evolution_mapping.table_sources:
            return None
        current_column = next(
            (
                name
                for name, _kind in self.columns[current_table]
                if name.casefold() == str(column).casefold()
            ),
            None,
        )
        if current_column is None:
            return None
        relation = _relation_select_sql(current_table, self.evolution_mapping)
        alias = "__evo_values"
        return (
            f"FROM ({relation}) AS {_quote(alias)}",
            f"{_quote(alias)}.{_quote(current_column)}",
            (
                "derived_current_value_through_lineage"
                if self.expose_evolution_evidence
                else "current_database_value"
            ),
        )

    def inspect_schema(self, tables: list[str]) -> dict[str, Any]:
        requested = {str(value).casefold() for value in tables[:6]}
        output = []
        for table in self.evolution_mapping.current_snapshot.tables:
            if table.name.casefold() not in requested:
                continue
            fk_by_column = {
                edge.source_column.casefold(): edge for edge in table.foreign_keys
            }
            lines = []
            for column in table.columns:
                annotations = []
                if column.primary_key:
                    annotations.append("PRIMARY KEY")
                edge = fk_by_column.get(column.name.casefold())
                if edge is not None:
                    annotations.append(
                        f"REFERENCES {_quote(edge.target_table)}"
                        f"({_quote(edge.target_column)})"
                    )
                suffix = f" -- {'; '.join(annotations)}" if annotations else ""
                lines.append(
                    f"  {_quote(column.name)} "
                    f"{column.declared_type or 'unknown'}{suffix}"
                )
            item = {
                "table": table.name,
                "ddl": "\n".join(
                    [f"CREATE TABLE {_quote(table.name)} (", *lines, ");"]
                ),
                "foreign_keys": self.foreign_keys[table.name],
            }
            if self.expose_evolution_evidence:
                item["evolution_type"] = self.evolution_mapping.evolution_type
            output.append(item)
        return {
            "tables": output,
            "unknown_tables": len(tables) - len(output),
            "schema_view": (
                "relation_changing_current_catalog"
                if self.expose_evolution_evidence
                else "current_catalog"
            ),
        }

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
        connection.set_progress_handler(
            lambda: int(time.monotonic() > deadline), 10_000
        )
        try:
            placeholders = ",".join("?" for _ in flat)
            for table in sorted(self.columns):
                for column, _kind in self.columns[table]:
                    relation = self._value_relation(table, column)
                    if relation is None:
                        continue
                    from_sql, value_sql, evidence = relation
                    query = (
                        f"SELECT {value_sql}, COUNT(*) {from_sql} "
                        f"WHERE {value_sql} IN ({placeholders}) "
                        f"GROUP BY {value_sql} LIMIT {limit}"
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
                                "evidence": evidence,
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
        relation = self._value_relation(table, column)
        if relation is None:
            return {
                "table": table,
                "column": column,
                "contains": contains,
                "values": [],
                "reason": "current_column_has_no_executable_value_lineage",
            }
        from_sql, value_sql, evidence = relation
        limit = max(1, min(int(limit), 20))
        where = f"WHERE {value_sql} IS NOT NULL"
        parameters: tuple[Any, ...] = ()
        if contains:
            where += f" AND CAST({value_sql} AS TEXT) LIKE ?"
            parameters = (f"%{contains}%",)
        query = (
            f"SELECT {value_sql}, COUNT(*) AS frequency {from_sql} {where} "
            f"GROUP BY {value_sql} "
            f"ORDER BY frequency DESC LIMIT {limit}"
        )
        connection = sqlite3.connect(f"file:{self.database}?mode=ro", uri=True)
        try:
            rows = connection.execute(query, parameters).fetchall()
        finally:
            connection.close()
        return {
            "table": table,
            "column": column,
            "contains": contains,
            "values": [[_safe_value(value) for value in row] for row in rows],
            "value_evidence": evidence,
        }

    def execute_sql(self, sql: str, limit: int = 20) -> dict[str, Any]:
        try:
            translated = reverse_map_evolved_sql(
                sql,
                mapping=self.evolution_mapping,
            )
        except Exception as error:
            return {
                "executable": False,
                "error_type": type(error).__name__,
                "error": str(error)[:800],
                "schema_view": (
                    "relation_changing_current_catalog"
                    if self.expose_evolution_evidence
                    else "current_catalog"
                ),
            }
        output = super().execute_sql(translated, limit=limit)
        output["schema_view"] = (
            "relation_changing_current_catalog"
            if self.expose_evolution_evidence
            else "current_catalog"
        )
        if self.expose_evolution_evidence:
            output["storage_adapter"] = "structural_evolution_reverse_compiler_v1"
        return output
