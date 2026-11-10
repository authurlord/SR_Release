"""BEAVER v3 MySQL adapter and physical catalog utilities.

The adapter keeps evaluator-only fields out of inference.  It exposes the same
bounded ReAct surface as the SQLite path, while normalizing BEAVER's released
upper-case SQL identifiers to the case-sensitive Linux MySQL dump.
"""

from __future__ import annotations

from collections import defaultdict
import json
import re
import time
from typing import Any

import sqlglot
from sqlglot import exp

from finsemguard.e2e.livesqlbench import CatalogDocument
from finsemguard.e2e.react_text2sql import SchemaSearchIndex


GENERIC_JOIN_COLUMNS = {
    "created_at",
    "date",
    "deleted_at",
    "id",
    "name",
    "status",
    "time",
    "type",
    "updated_at",
    "value",
}


def _quote(identifier: str) -> str:
    return "`" + identifier.replace("`", "``") + "`"


def _safe_value(value: Any) -> Any:
    if value is None or isinstance(value, (bool, int, float)):
        return value
    if isinstance(value, bytes):
        return "0x" + value[:64].hex()
    text = str(value)
    return text if len(text) <= 500 else text[:497] + "..."


def canonicalize_mysql_sql(sql: str, table_names: list[str]) -> str:
    """Map table identifiers case-insensitively onto the physical dump names."""

    lookup = {name.casefold(): name for name in table_names}
    try:
        statements = sqlglot.parse(sql, read="mysql")
        if len(statements) != 1:
            raise ValueError("exactly one SQL statement is required")
        tree = statements[0]
        for table in tree.find_all(exp.Table):
            physical = lookup.get(str(table.name).casefold())
            if physical is not None:
                table.set("this", exp.to_identifier(physical, quoted=True))
        return tree.sql(dialect="mysql")
    except Exception:
        output = sql
        for folded, physical in sorted(lookup.items(), key=lambda row: -len(row[0])):
            output = re.sub(
                rf"(?<![A-Za-z0-9_$]){re.escape(folded)}(?![A-Za-z0-9_$])",
                _quote(physical),
                output,
                flags=re.IGNORECASE,
            )
        return output


def _read_only_select(sql: str) -> None:
    statements = sqlglot.parse(sql, read="mysql")
    if len(statements) != 1:
        raise ValueError("exactly one SQL statement is required")
    tree = statements[0]
    forbidden_names = (
        "Alter",
        "Command",
        "Copy",
        "Create",
        "Delete",
        "Drop",
        "Insert",
        "Merge",
        "Transaction",
        "TruncateTable",
        "Update",
        "Use",
    )
    forbidden = tuple(
        value
        for name in forbidden_names
        if (value := getattr(exp, name, None)) is not None
    )
    if forbidden and any(tree.find_all(*forbidden)):
        raise ValueError("only read-only SELECT/WITH queries are allowed")
    if not any(tree.find_all(exp.Select)):
        raise ValueError("query must contain SELECT")


def build_beaver_catalog_documents(
    table_inputs: list[dict[str, Any]],
) -> list[CatalogDocument]:
    """Build physical-only table and field documents from released metadata."""

    output: list[CatalogDocument] = []
    for source in table_inputs:
        database_id = str(source["schema_context"])
        table = str(source["physical_table"])
        lines: list[str] = []
        for column in source.get("columns") or []:
            name = str(column["physical_column"])
            declared = str(column.get("declared_type") or "unknown")
            examples = [_safe_value(value) for value in column.get("observed_values") or []]
            example_text = (
                "\nreleased example values: "
                + json.dumps(examples[:3], ensure_ascii=False)
                if examples
                else ""
            )
            output.append(
                CatalogDocument(
                    candidate_id=f"column::{database_id}::{table}::{name}",
                    database_id=database_id,
                    kind="column",
                    table=table,
                    name=f"{table}.{name}",
                    text=(
                        f"physical MySQL identifier: {_quote(table)}.{_quote(name)}\n"
                        f"declared type: {declared}{example_text}"
                    ),
                )
            )
            suffix = (
                " -- released examples: "
                + json.dumps(examples[:3], ensure_ascii=False)
                if examples
                else ""
            )
            lines.append(f"  {_quote(name)} {declared}{suffix}")
        output.append(
            CatalogDocument(
                candidate_id=f"table::{database_id}::{table}",
                database_id=database_id,
                kind="table",
                table=table,
                name=table,
                text="\n".join(
                    [
                        f"physical MySQL table: {_quote(table)}",
                        f"CREATE TABLE {_quote(table)} (",
                        ",\n".join(lines),
                        ");",
                    ]
                ),
            )
        )
    ids = [row.candidate_id for row in output]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate BEAVER catalog document IDs")
    return output


class BeaverMySQLAgentTools:
    """Read-only MySQL tools with a metadata-backed high-recall value probe."""

    def __init__(
        self,
        database_id: str,
        search_index: SchemaSearchIndex,
        *,
        connection_config: dict[str, Any],
        table_inputs: list[dict[str, Any]],
        query_timeout_ms: int = 8000,
    ) -> None:
        self.database_id = database_id
        # BEAVER has no hidden storage/current adapter: its public and
        # physical database identifiers are the same.  Keep the common tool
        # protocol used by the unified planner explicit.
        self.public_database_id = database_id
        self.search_index = search_index
        self.connection_config = {**connection_config, "database": database_id}
        self.query_timeout_ms = int(query_timeout_ms)
        self.targeted_expansion_used = False
        self.columns: dict[str, list[tuple[str, str]]] = {}
        self.examples: dict[tuple[str, str], list[Any]] = {}
        for row in table_inputs:
            if str(row["schema_context"]) != database_id:
                continue
            table = str(row["physical_table"])
            self.columns[table] = []
            for column in row.get("columns") or []:
                name = str(column["physical_column"])
                self.columns[table].append(
                    (name, str(column.get("declared_type") or "unknown"))
                )
                self.examples[(table, name)] = list(column.get("observed_values") or [])
        self._table_lookup = {name.casefold(): name for name in self.columns}
        self._recent_tables: list[str] = []
        self.join_edges = self._same_name_join_edges()
        observed = {
            tuple(
                sorted(
                    (str(row["left"]).casefold(), str(row["right"]).casefold())
                )
            ): index
            for index, row in enumerate(self.join_edges)
        }
        for source in search_index.ontology_edges_by_database.get(database_id, []):
            row = dict(source)
            key = tuple(
                sorted((str(row["left"]).casefold(), str(row["right"]).casefold()))
            )
            if key in observed:
                # A same-name heuristic is constructed before ontology edges.
                # Do not let endpoint de-duplication discard the stronger
                # declared/history evidence needed by the typed compiler.
                existing = self.join_edges[observed[key]]

                def evidence(value: dict[str, Any]) -> list[str]:
                    raw = value.get("evidence_types") or value.get("evidence") or []
                    if isinstance(raw, str):
                        raw = [part for part in raw.split("+") if part]
                    return [str(part) for part in raw]

                merged = {**existing, **row}
                merged["evidence_types"] = list(
                    dict.fromkeys([*evidence(existing), *evidence(row)])
                )
                merged["provenance_ids"] = list(
                    dict.fromkeys(
                        [
                            *list(existing.get("provenance_ids") or []),
                            *list(row.get("provenance_ids") or []),
                        ]
                    )
                )
                merged["score"] = max(
                    float(existing.get("score") or 0.0),
                    float(row.get("score") or 0.0),
                )
                self.join_edges[observed[key]] = merged
                continue
            self.join_edges.append(row)
            observed[key] = len(self.join_edges) - 1

    def _connect(self):
        import mysql.connector

        connection = mysql.connector.connect(
            **self.connection_config, connection_timeout=10
        )
        # MySQL 8.0.19's TempTable engine can segfault on the nested
        # CTE/window/aggregate queries common in BEAVER.  MEMORY is a
        # semantics-preserving internal temporary-table backend and keeps one
        # model-authored SELECT from taking down the shared evaluator process.
        cursor = connection.cursor()
        try:
            cursor.execute("SET SESSION internal_tmp_mem_storage_engine=MEMORY")
        finally:
            cursor.close()
        return connection

    def _same_name_join_edges(self) -> list[dict[str, Any]]:
        by_column: dict[str, list[tuple[str, str]]] = defaultdict(list)
        for table, columns in self.columns.items():
            for column, _ in columns:
                normalized = re.sub(r"[^a-z0-9]+", "_", column.casefold()).strip("_")
                if normalized and normalized not in GENERIC_JOIN_COLUMNS:
                    by_column[normalized].append((table, column))
        output: list[dict[str, Any]] = []
        for endpoints in by_column.values():
            if len(endpoints) > 12:
                continue
            for index, left in enumerate(endpoints):
                for right in endpoints[index + 1 :]:
                    if left[0] == right[0]:
                        continue
                    output.append(
                        {
                            "left": f"{left[0]}.{left[1]}",
                            "right": f"{right[0]}.{right[1]}",
                            "evidence": "same_physical_column_name",
                            "score": 0.7,
                        }
                    )
        return output

    def inventory_text(self) -> str:
        # Full DDL for a 175-table database wastes the context budget and bypasses
        # retrieval.  The table inventory is complete; retrieved/inspected DDL is
        # field-complete for the selected tables.
        return "\n".join(
            f"{table} ({len(self.columns[table])} columns)" for table in sorted(self.columns)
        )

    def search_schema(
        self,
        query: str,
        top_k: int,
        *,
        enable_reranker: bool = True,
    ) -> dict[str, Any]:
        result = self.search_index.search(
            self.database_id,
            query,
            top_k,
            enable_reranker=enable_reranker,
        )
        recent: list[str] = []
        for row in result.get("results") or []:
            table = str(row.get("physical_table") or "")
            if table and table in self.columns and table not in recent:
                recent.append(table)
        self._recent_tables = recent[:12]
        return result

    def targeted_expand_schema(
        self, queries: list[str], top_k_per_query: int
    ) -> dict[str, Any]:
        if self.targeted_expansion_used:
            raise RuntimeError("targeted schema expansion is limited to one call")
        cleaned = list(dict.fromkeys(str(value).strip() for value in queries[:3] if str(value).strip()))
        if not cleaned:
            raise ValueError("targeted expansion requires at least one query")
        self.targeted_expansion_used = True
        merged: list[dict[str, Any]] = []
        observed: set[tuple[str, str, str]] = set()
        bridges: list[str] = []
        anchors: list[str] = []
        for query in cleaned:
            result = self.search_schema(query, max(1, min(int(top_k_per_query), 10)))
            bridges.extend(str(value) for value in result.get("bridge_tables") or [])
            anchors.extend(str(value) for value in result.get("bound_physical_anchors") or [])
            for row in result.get("results") or []:
                key = (
                    str(row.get("kind") or ""),
                    str(row.get("physical_table") or ""),
                    str(row.get("physical_name") or ""),
                )
                if key not in observed:
                    observed.add(key)
                    merged.append({"probe": query, **dict(row)})
        return {
            "queries": cleaned,
            "results": merged[:24],
            "bridge_tables": list(dict.fromkeys(bridges))[:12],
            "bound_physical_anchors": list(dict.fromkeys(anchors))[:16],
            "expansion_calls_remaining": 0,
            "evidence_boundary": "this arm's existing schema index only",
        }

    def search_joins(self, tables: list[str], max_edges: int) -> dict[str, Any]:
        requested = {str(value).casefold() for value in tables}
        matched = [
            row
            for row in self.join_edges
            if not requested
            or str(row["left"]).split(".", 1)[0].casefold() in requested
            or str(row["right"]).split(".", 1)[0].casefold() in requested
        ]
        matched.sort(key=lambda row: (-float(row["score"]), str(row["left"]), str(row["right"])))
        return {"join_edges": matched[: max(1, min(int(max_edges), 30))]}

    def search_values(self, literals: list[str], max_matches: int) -> dict[str, Any]:
        limit = max(1, min(int(max_matches), 30))
        lookup = {str(value).strip().casefold(): str(value) for value in literals[:12] if str(value).strip()}
        matches: list[dict[str, Any]] = []
        for (table, column), values in sorted(self.examples.items()):
            for value in values:
                owner = lookup.get(str(value).strip().casefold())
                if owner is None:
                    continue
                matches.append(
                    {
                        "literal": owner,
                        "physical_column": f"{table}.{column}",
                        "matched_value": _safe_value(value),
                        "evidence": "released_table_example_exact_match",
                    }
                )
                if len(matches) >= limit:
                    return {"matches": matches, "truncated": True}
        return {"matches": matches, "truncated": False}

    def inspect_schema(self, tables: list[str]) -> dict[str, Any]:
        selected: list[str] = []
        for value in tables[:6]:
            match = self._table_lookup.get(str(value).casefold())
            if match and match not in selected:
                selected.append(match)
        connection = self._connect()
        try:
            cursor = connection.cursor()
            output = []
            for table in selected:
                cursor.execute(f"SHOW CREATE TABLE {_quote(table)}")
                row = cursor.fetchone()
                output.append(
                    {
                        "table": table,
                        "ddl": str(row[1]) if row and len(row) > 1 else "",
                        "relationship_edges": [
                            edge
                            for edge in self.join_edges
                            if str(edge["left"]).split(".", 1)[0] == table
                            or str(edge["right"]).split(".", 1)[0] == table
                        ][:20],
                    }
                )
            cursor.close()
            return {"tables": output, "unknown_tables": len(tables) - len(selected)}
        finally:
            connection.close()

    def sample_values(
        self, table: str, column: str, limit: int, contains: str | None
    ) -> dict[str, Any]:
        physical_table = self._table_lookup.get(table.casefold())
        if physical_table is None:
            raise ValueError(f"unknown table: {table}")
        physical_column = next(
            (name for name, _ in self.columns[physical_table] if name.casefold() == column.casefold()),
            None,
        )
        if physical_column is None:
            raise ValueError(f"unknown column: {physical_table}.{column}")
        limit = max(1, min(int(limit), 20))
        where = f"WHERE {_quote(physical_column)} IS NOT NULL"
        parameters: tuple[Any, ...] = ()
        if contains:
            where += f" AND CAST({_quote(physical_column)} AS CHAR) LIKE %s"
            parameters = (f"%{contains}%",)
        sql = (
            f"SELECT {_quote(physical_column)}, COUNT(*) AS frequency "
            f"FROM {_quote(physical_table)} {where} GROUP BY {_quote(physical_column)} "
            f"ORDER BY frequency DESC LIMIT {limit}"
        )
        connection = self._connect()
        try:
            cursor = connection.cursor()
            cursor.execute(f"SET SESSION MAX_EXECUTION_TIME={self.query_timeout_ms}")
            cursor.execute(sql, parameters)
            rows = cursor.fetchall()
            cursor.close()
        finally:
            connection.close()
        return {
            "table": physical_table,
            "column": physical_column,
            "contains": contains,
            "values": [[_safe_value(value) for value in row] for row in rows],
        }

    def execute_sql(self, sql: str, limit: int = 20) -> dict[str, Any]:
        if not sql.strip():
            raise ValueError("SQL must not be empty")
        normalized = canonicalize_mysql_sql(sql, list(self.columns))
        try:
            _read_only_select(normalized)
        except Exception as error:
            return {
                "executable": False,
                "error_type": type(error).__name__,
                "error": str(error)[:800],
                "storage_adapter": "beaver_mysql_case_normalization_v1",
            }
        connection = self._connect()
        cursor = None
        started = time.perf_counter()
        try:
            cursor = connection.cursor()
            cursor.execute(f"SET SESSION MAX_EXECUTION_TIME={self.query_timeout_ms}")
            cursor.execute(normalized)
            cap = max(1, min(int(limit), 20))
            rows = cursor.fetchmany(cap + 1)
            return {
                "executable": True,
                "columns": [str(value[0]) for value in cursor.description or []],
                "rows": [[_safe_value(value) for value in row] for row in rows[:cap]],
                "truncated": len(rows) > cap,
                "normalized_sql": normalized,
                "storage_adapter": "beaver_mysql_case_normalization_v1",
                "latency_seconds": round(time.perf_counter() - started, 6),
            }
        except Exception as error:
            return {
                "executable": False,
                "error_type": type(error).__name__,
                "error": str(error)[:800],
                "normalized_sql": normalized,
                "storage_adapter": "beaver_mysql_case_normalization_v1",
            }
        finally:
            try:
                if cursor is not None:
                    cursor.close()
            except Exception:
                pass
            connection.close()
