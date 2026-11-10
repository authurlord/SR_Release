"""Cardinality-aware, deterministic JOIN repair for an existing SQL anchor.

The SQL generator has usually already chosen the right output, filter, and
aggregation columns.  Regenerating the whole query from another rendering of the
same evidence needlessly loses those decisions.  This module instead extracts the
tables used outside JOIN clauses, compiles their smallest relationship-backed tree,
and replaces only FROM/JOIN.  A narrow percentage-of-entities normalization handles
row multiplication introduced by a many-side join.
"""

from __future__ import annotations

from collections import defaultdict, deque
from dataclasses import dataclass
from pathlib import Path
import re
import sqlite3
import time
from typing import Any

import sqlglot
from sqlglot import exp

from finsemguard.e2e.livesqlbench import CatalogDocument
from finsemguard.e2e.minimal_join_tree import compile_minimal_join_tree


def _quote(identifier: str) -> str:
    return '"' + str(identifier).replace('"', '""') + '"'


@dataclass(frozen=True)
class SQLiteRelationshipCatalog:
    documents: tuple[CatalogDocument, ...]
    edges: tuple[dict[str, Any], ...]
    unique_columns: dict[str, frozenset[str]]
    primary_keys: dict[str, tuple[str, ...]]


def inspect_sqlite_relationship_catalog(
    database: Path,
    *,
    database_id: str,
    table_old_to_new: dict[str, str] | None = None,
    column_old_to_new: dict[str, dict[str, str]] | None = None,
    compatibility_tables: list[str] | None = None,
) -> SQLiteRelationshipCatalog:
    """Read only keys/FKs and derive equality shortcuts over a shared parent key."""

    table_map = {str(key): str(value) for key, value in (table_old_to_new or {}).items()}
    column_map = {
        str(table): {str(key): str(value) for key, value in values.items()}
        for table, values in (column_old_to_new or {}).items()
    }

    def mapped_table(table: str) -> str:
        return table_map.get(table, table)

    def mapped_column(table: str, column: str) -> str:
        return column_map.get(table, {}).get(column, column)

    connection = sqlite3.connect(f"file:{database.resolve()}?mode=ro", uri=True)
    try:
        original_tables = [
            str(row[0])
            for row in connection.execute(
                "SELECT name FROM sqlite_master WHERE type='table' "
                "AND name NOT LIKE 'sqlite_%' ORDER BY name"
            )
        ]
        documents: list[CatalogDocument] = []
        edges: list[dict[str, Any]] = []
        unique_columns: dict[str, set[str]] = defaultdict(set)
        primary_keys: dict[str, tuple[str, ...]] = {}
        foreign_keys: list[tuple[str, str, str, str, str]] = []
        columns_by_original_table: dict[str, list[tuple[str, str]]] = {}
        for original_table in original_tables:
            table = mapped_table(original_table)
            columns = list(
                connection.execute(f"PRAGMA table_info({_quote(original_table)})")
            )
            columns_by_original_table[original_table] = [
                (str(row[1]), str(row[2] or "").casefold()) for row in columns
            ]
            primary = [str(row[1]) for row in columns if int(row[5] or 0) > 0]
            primary_keys[table] = tuple(
                mapped_column(original_table, column) for column in primary
            )
            if len(primary) == 1:
                unique_columns[table].add(mapped_column(original_table, primary[0]))
            for index_row in connection.execute(
                f"PRAGMA index_list({_quote(original_table)})"
            ):
                if not bool(index_row[2]):
                    continue
                index_name = str(index_row[1])
                indexed = [
                    str(row[2])
                    for row in connection.execute(
                        f"PRAGMA index_info({_quote(index_name)})"
                    )
                    if row[2] is not None
                ]
                if len(indexed) == 1:
                    unique_columns[table].add(
                        mapped_column(original_table, indexed[0])
                    )

            table_foreign_keys = list(
                connection.execute(
                    f"PRAGMA foreign_key_list({_quote(original_table)})"
                )
            )
            references: list[str] = []
            fk_by_column: dict[str, tuple[str, str]] = {}
            for row in table_foreign_keys:
                parent_original = str(row[2])
                child_original = str(row[3])
                parent_column_original = str(row[4])
                child_column = mapped_column(original_table, child_original)
                parent_table = mapped_table(parent_original)
                parent_column = mapped_column(
                    parent_original, parent_column_original
                )
                references.append(parent_table)
                fk_by_column[child_original] = (parent_table, parent_column)
                provenance = (
                    f"sqlite_fk::{database_id}::{table}.{child_column}::"
                    f"{parent_table}.{parent_column}"
                )
                edges.append(
                    {
                        "left": f"{table}.{child_column}",
                        "right": f"{parent_table}.{parent_column}",
                        "score": 1.0,
                        "evidence_types": ["declared_foreign_key"],
                        "provenance_ids": [provenance],
                    }
                )
                foreign_keys.append(
                    (
                        table,
                        child_column,
                        parent_table,
                        parent_column,
                        provenance,
                    )
                )

            lines: list[str] = []
            for row in columns:
                original_column = str(row[1])
                column = mapped_column(original_table, original_column)
                annotations: list[str] = []
                if int(row[5] or 0) > 0:
                    annotations.append("PRIMARY KEY")
                if original_column in fk_by_column:
                    parent_table, parent_column = fk_by_column[original_column]
                    annotations.append(
                        f"REFERENCES {_quote(parent_table)}({_quote(parent_column)})"
                    )
                suffix = f" -- {'; '.join(annotations)}" if annotations else ""
                lines.append(f"  {_quote(column)} {row[2] or 'unknown'}{suffix}")
            documents.append(
                CatalogDocument(
                    candidate_id=f"table::{database_id}::{table}",
                    database_id=database_id,
                    kind="table",
                    table=table,
                    name=table,
                    text="\n".join(
                        [
                            f"CREATE TABLE {_quote(table)} (",
                            *lines,
                            ");",
                        ]
                    ),
                    references=tuple(dict.fromkeys(references)),
                )
            )

        requested = {
            str(table).casefold() for table in compatibility_tables or []
        }
        compatible_original_tables = [
            table
            for table in original_tables
            if mapped_table(table).casefold() in requested
        ]
        sample_cache: dict[tuple[str, str], set[tuple[str, str]]] = {}

        def samples(table: str, column: str) -> set[tuple[str, str]]:
            key = table, column
            if key not in sample_cache:
                values = connection.execute(
                    f"SELECT DISTINCT {_quote(column)} FROM {_quote(table)} "
                    f"WHERE {_quote(column)} IS NOT NULL LIMIT 1024"
                )
                sample_cache[key] = {
                    (type(row[0]).__name__, str(row[0])) for row in values
                }
            return sample_cache[key]

        for left_index, left_original in enumerate(compatible_original_tables):
            for right_original in compatible_original_tables[left_index + 1 :]:
                for left_column_original, left_type in columns_by_original_table[
                    left_original
                ]:
                    if not any(
                        marker in left_type
                        for marker in ("text", "char", "clob", "varchar")
                    ):
                        continue
                    left_values = samples(left_original, left_column_original)
                    if len(left_values) < 8:
                        continue
                    for right_column_original, right_type in columns_by_original_table[
                        right_original
                    ]:
                        if not any(
                            marker in right_type
                            for marker in ("text", "char", "clob", "varchar")
                        ):
                            continue
                        right_values = samples(right_original, right_column_original)
                        if len(right_values) < 8:
                            continue
                        overlap = len(left_values & right_values)
                        containment = overlap / min(
                            len(left_values), len(right_values)
                        )
                        if overlap < 8 or containment < 0.98:
                            continue
                        left_table = mapped_table(left_original)
                        right_table = mapped_table(right_original)
                        left_column = mapped_column(
                            left_original, left_column_original
                        )
                        right_column = mapped_column(
                            right_original, right_column_original
                        )
                        edges.append(
                            {
                                "left": f"{left_table}.{left_column}",
                                "right": f"{right_table}.{right_column}",
                                "score": round(containment, 6),
                                "evidence_types": [
                                    "profile_value_containment_join",
                                    "compatible_join_key",
                                ],
                                "provenance_ids": [
                                    "profile_containment::"
                                    f"{database_id}::{left_table}.{left_column}::"
                                    f"{right_table}.{right_column}::"
                                    f"overlap={overlap}::coefficient={containment:.6f}"
                                ],
                            }
                        )
    finally:
        connection.close()

    # If A.fk -> P.pk and B.fk -> P.pk, A.fk = B.fk is a valid equality
    # shortcut.  It avoids retaining P solely as an equality bridge and captures
    # common benchmark queries that join sibling fact/detail tables directly.
    by_parent: dict[tuple[str, str], list[tuple[str, str, str]]] = defaultdict(list)
    for child_table, child_column, parent_table, parent_column, provenance in foreign_keys:
        by_parent[(parent_table, parent_column)].append(
            (child_table, child_column, provenance)
        )
    for (parent_table, parent_column), children in by_parent.items():
        for index, left in enumerate(children):
            for right in children[index + 1 :]:
                if left[0] == right[0]:
                    continue
                edges.append(
                    {
                        "left": f"{left[0]}.{left[1]}",
                        "right": f"{right[0]}.{right[1]}",
                        "score": 1.0,
                        "evidence_types": [
                            "declared_shared_key_equivalence",
                            "derived_equijoin",
                        ],
                        "provenance_ids": [
                            left[2],
                            right[2],
                            f"shared_parent::{parent_table}.{parent_column}",
                        ],
                    }
                )
    return SQLiteRelationshipCatalog(
        documents=tuple(documents),
        edges=tuple(edges),
        unique_columns={
            table: frozenset(values) for table, values in unique_columns.items()
        },
        primary_keys=primary_keys,
    )


def _top_level_sources(tree: exp.Select) -> tuple[dict[str, str], dict[str, exp.Table]]:
    sources: list[exp.Expression] = []
    from_clause = tree.args.get("from_")
    if from_clause is not None and from_clause.this is not None:
        sources.append(from_clause.this)
    sources.extend(join.this for join in tree.args.get("joins") or [])
    if not sources or any(not isinstance(source, exp.Table) for source in sources):
        return {}, {}
    aliases: dict[str, str] = {}
    nodes: dict[str, exp.Table] = {}
    for source in sources:
        assert isinstance(source, exp.Table)
        table = str(source.name)
        alias = str(source.alias_or_name)
        if not table or not alias or alias.casefold() in aliases:
            return {}, {}
        aliases[alias.casefold()] = table
        nodes[table.casefold()] = source
    if len(nodes) != len(sources):
        # Self joins require alias-specific terminals; the current compiler is
        # table-level and deliberately leaves them untouched.
        return {}, {}
    return aliases, nodes


def _nearest_select(node: exp.Expression) -> exp.Select | None:
    parent = node.parent
    while parent is not None:
        if isinstance(parent, exp.Select):
            return parent
        parent = parent.parent
    return None


def _inside_join(node: exp.Expression, root: exp.Select) -> bool:
    parent = node.parent
    while parent is not None and parent is not root:
        if isinstance(parent, exp.Join):
            return True
        parent = parent.parent
    return False


def _essential_tables(
    tree: exp.Select, aliases: dict[str, str]
) -> tuple[list[str], dict[str, str]]:
    tables: list[str] = []
    essential_aliases: dict[str, str] = {}
    for column in tree.find_all(exp.Column):
        if _nearest_select(column) is not tree or _inside_join(column, tree):
            continue
        qualifier = str(column.table).casefold()
        if qualifier:
            table = aliases.get(qualifier)
            if table is None:
                continue
            essential_aliases[table.casefold()] = str(column.table)
        elif len(aliases) == 1:
            table = next(iter(aliases.values()))
            essential_aliases[table.casefold()] = next(iter(aliases))
        else:
            continue
        if table not in tables:
            tables.append(table)
    return tables, essential_aliases


def _percentage_entity_alias(tree: exp.Select, question: str) -> str | None:
    if not re.search(r"\b(?:percentage|percent|proportion|rate)\b", question, re.I):
        return None
    aliases: set[str] = set()
    for case in tree.find_all(exp.Case):
        if _nearest_select(case) is not tree:
            continue
        parent = case.parent
        if not isinstance(parent, exp.Sum):
            continue
        aliases.update(
            str(column.table).casefold()
            for column in case.find_all(exp.Column)
            if column.table
        )
    return next(iter(aliases)) if len(aliases) == 1 else None


def _count_entity_alias(
    tree: exp.Select, question: str, aliases: dict[str, str]
) -> str | None:
    if not re.search(r"\b(?:how many|number of|count of)\b", question, re.I):
        return None
    counts = [
        node
        for node in tree.find_all(exp.Count)
        if _nearest_select(node) is tree
    ]
    if len(counts) != 1:
        return None
    counted = counts[0].this
    if isinstance(counted, exp.Column) and counted.table:
        alias = str(counted.table).casefold()
        if alias in aliases and _table_mentioned(question, aliases[alias]):
            return alias
    from_clause = tree.args.get("from_")
    if from_clause is None or not isinstance(from_clause.this, exp.Table):
        return None
    alias = str(from_clause.this.alias_or_name).casefold()
    if alias in aliases and _table_mentioned(question, aliases[alias]):
        return alias
    return None


def _table_mentioned(question: str, table: str) -> bool:
    query_tokens = set(re.findall(r"[a-z0-9]+", question.casefold()))
    table_tokens = re.findall(r"[a-z0-9]+", table.replace("_", " ").casefold())
    for token in table_tokens:
        variants = {
            token,
            token.removesuffix("s"),
            token if token.endswith("s") else f"{token}s",
        }
        if variants & query_tokens:
            return True
    return False


def _canonical_edge_signature(edge: dict[str, str]) -> tuple[str, str, str, str]:
    left = (edge["left_table"].casefold(), edge["left_column"].casefold())
    right = (edge["right_table"].casefold(), edge["right_column"].casefold())
    first, second = (left, right) if left <= right else (right, left)
    return first[0], first[1], second[0], second[1]


def _old_join_edges(
    tree: exp.Select, aliases: dict[str, str]
) -> list[dict[str, str]]:
    output: list[dict[str, str]] = []
    for join in tree.args.get("joins") or []:
        for equality in (join.args.get("on") or exp.Null()).find_all(exp.EQ):
            if not isinstance(equality.this, exp.Column) or not isinstance(
                equality.expression, exp.Column
            ):
                continue
            left, right = equality.this, equality.expression
            left_alias = str(left.table).casefold()
            right_alias = str(right.table).casefold()
            if left_alias not in aliases or right_alias not in aliases:
                continue
            output.append(
                {
                    "left_alias": left_alias,
                    "left_table": aliases[left_alias],
                    "left_column": str(left.name),
                    "right_alias": right_alias,
                    "right_table": aliases[right_alias],
                    "right_column": str(right.name),
                }
            )
    return output


def _expansion_count(
    *,
    start: str,
    edges: list[dict[str, str]],
    unique_columns: dict[str, frozenset[str]],
    alias_graph: bool,
) -> int | None:
    adjacency: dict[str, list[tuple[str, str, str]]] = defaultdict(list)
    for edge in edges:
        left = edge["left_alias"] if alias_graph else edge["left_table"].casefold()
        right = edge["right_alias"] if alias_graph else edge["right_table"].casefold()
        adjacency[left].append((right, edge["right_table"], edge["right_column"]))
        adjacency[right].append((left, edge["left_table"], edge["left_column"]))
    if start not in adjacency:
        return None
    queue: deque[str] = deque([start])
    visited = {start}
    expansions = 0
    while queue:
        node = queue.popleft()
        for neighbor, neighbor_table, neighbor_column in adjacency.get(node, []):
            if neighbor in visited:
                continue
            visited.add(neighbor)
            queue.append(neighbor)
            if neighbor_column not in unique_columns.get(neighbor_table, frozenset()):
                expansions += 1
    return expansions


def _table_expression(table: str, original: exp.Table | None) -> exp.Table:
    if original is not None:
        return original.copy()
    return exp.Table(this=exp.Identifier(this=table, quoted=True))


def _replace_join_tree(
    tree: exp.Select,
    graph: dict[str, Any],
    original_nodes: dict[str, exp.Table],
    aliases: dict[str, str],
) -> None:
    alias_by_table = {
        table.casefold(): alias for alias, table in aliases.items()
    }

    def alias_for(table: str) -> str:
        return alias_by_table.get(table.casefold(), table)

    order = [str(value) for value in graph.get("topological_table_order") or []]
    if not order:
        raise ValueError("compiled tree has no table order")
    root = order[0]
    tree.set(
        "from_",
        exp.From(
            this=_table_expression(root, original_nodes.get(root.casefold()))
        ),
    )
    joins: list[exp.Join] = []
    for edge in graph.get("ordered_join_edges") or []:
        parent_table = str(edge["parent_table"])
        child_table = str(edge["child_table"])
        parent_column = str(edge["parent_column"])
        child_column = str(edge["child_column"])
        joins.append(
            exp.Join(
                this=_table_expression(
                    child_table, original_nodes.get(child_table.casefold())
                ),
                on=exp.EQ(
                    this=exp.column(
                        parent_column, table=alias_for(parent_table), quoted=True
                    ),
                    expression=exp.column(
                        child_column, table=alias_for(child_table), quoted=True
                    ),
                ),
            )
        )
    tree.set("joins", joins)


def _normalize_distinct_entity_percentage(
    tree: exp.Select, *, entity_alias: str, entity_primary_key: str
) -> bool:
    sums = [
        node
        for node in tree.find_all(exp.Sum)
        if _nearest_select(node) is tree and isinstance(node.this, exp.Case)
    ]
    counts = [
        node
        for node in tree.find_all(exp.Count)
        if _nearest_select(node) is tree
    ]
    if len(sums) != 1 or len(counts) != 1:
        return False
    case = sums[0].this.copy()
    assert isinstance(case, exp.Case)
    ifs = list(case.args.get("ifs") or [])
    if len(ifs) != 1:
        return False
    entity_column = exp.column(
        entity_primary_key, table=entity_alias, quoted=True
    )
    ifs[0].set("true", entity_column.copy())
    case.set("default", exp.Null())
    numerator = exp.Count(this=exp.Distinct(expressions=[case]))
    denominator = exp.Count(
        this=exp.Distinct(expressions=[entity_column.copy()])
    )
    sums[0].replace(numerator)
    counts[0].replace(denominator)
    return True


def _normalize_distinct_entity_count(
    tree: exp.Select, *, entity_alias: str, entity_primary_key: str
) -> bool:
    counts = [
        node
        for node in tree.find_all(exp.Count)
        if _nearest_select(node) is tree
    ]
    if len(counts) != 1:
        return False
    if isinstance(counts[0].this, exp.Distinct):
        return True
    counts[0].replace(
        exp.Count(
            this=exp.Distinct(
                expressions=[
                    exp.column(
                        entity_primary_key, table=entity_alias, quoted=True
                    )
                ]
            )
        )
    )
    return True


def _executable(database: Path, sql: str, timeout_seconds: float) -> bool:
    connection = sqlite3.connect(f"file:{database.resolve()}?mode=ro", uri=True)
    deadline = time.monotonic() + timeout_seconds
    connection.set_progress_handler(
        lambda: int(time.monotonic() > deadline), 1000
    )
    try:
        connection.execute(sql).fetchone()
        return True
    except Exception:
        return False
    finally:
        connection.close()


def repair_anchor_join_tree(
    *,
    sql: str,
    question: str,
    database: Path,
    database_id: str,
    dialect: str = "sqlite",
    table_old_to_new: dict[str, str] | None = None,
    column_old_to_new: dict[str, dict[str, str]] | None = None,
    timeout_seconds: float = 5.0,
) -> dict[str, Any]:
    """Return an anchor-preserving repair decision and its structural certificate."""

    decision: dict[str, Any] = {
        "selected": "anchor",
        "reason": "not_applicable",
        "sql": sql,
        "uses_evaluator_gold": False,
    }
    try:
        tree = sqlglot.parse_one(sql, read=dialect.casefold())
    except Exception as error:
        return {**decision, "reason": f"parse_error:{type(error).__name__}"}
    if not isinstance(tree, exp.Select) or tree.args.get("with_") is not None:
        return {**decision, "reason": "non_simple_select"}
    if any(node is not tree for node in tree.find_all(exp.Select)):
        return {**decision, "reason": "nested_select"}
    joins = list(tree.args.get("joins") or [])
    if not joins or any(
        str(join.args.get("side") or "").casefold() not in {""}
        or str(join.args.get("kind") or "").casefold() not in {"", "inner"}
        for join in joins
    ):
        return {**decision, "reason": "non_inner_or_no_join"}
    aliases, original_nodes = _top_level_sources(tree)
    if not aliases:
        return {**decision, "reason": "unsupported_sources"}
    essential_tables, _ = _essential_tables(tree, aliases)
    if len(essential_tables) < 2:
        return {**decision, "reason": "fewer_than_two_essential_tables"}
    entity_alias = _percentage_entity_alias(tree, question)
    entity_mode = "percentage"
    if entity_alias is None:
        entity_alias = _count_entity_alias(tree, question, aliases)
        entity_mode = "count"
    if entity_alias is None or entity_alias not in aliases:
        return {**decision, "reason": "not_supported_entity_aggregate"}

    catalog = inspect_sqlite_relationship_catalog(
        database,
        database_id=database_id,
        table_old_to_new=table_old_to_new,
        column_old_to_new=column_old_to_new,
        compatibility_tables=(essential_tables if entity_mode == "count" else []),
    )
    entity_table = aliases[entity_alias]
    entity_keys = list(catalog.primary_keys.get(entity_table, ()))
    if not entity_keys:
        entity_keys = sorted(catalog.unique_columns.get(entity_table, frozenset()))
    if len(entity_keys) != 1:
        return {**decision, "reason": "entity_key_not_unique"}
    graph = compile_minimal_join_tree(
        raw_documents=list(catalog.documents),
        ontology_edges=list(catalog.edges),
        role_bindings={},
        # Orient the tree from the entity whose multiplicity is being guarded.
        # This is operationally clearer than allowing SQLGlot traversal order to
        # choose the root, and keeps aggregate aliases stable during replacement.
        required_tables=list(dict.fromkeys([entity_table, *essential_tables])),
    )
    certificate = graph.get("certificate") or {}
    graph_edges = list(graph.get("ordered_join_edges") or [])
    supported_edge_classes = {
        "declared",
        "evolution_key",
        # These remain explicitly *uncertified* in the graph certificate.  The
        # repair's query-grounding checks below are the additional acceptance
        # condition for a logical shared-parent shortcut or empirical profile
        # containment relation.
        "derived",
        "profile",
    }
    if (
        graph.get("unresolved_roles")
        or not certificate.get("all_join_columns_known")
        or any(
            str(edge.get("evidence_class") or "") not in supported_edge_classes
            for edge in graph_edges
        )
    ):
        return {**decision, "reason": "join_tree_not_certified", "graph": graph}
    new_edges = [
        {
            "left_table": str(edge["parent_table"]),
            "left_column": str(edge["parent_column"]),
            "right_table": str(edge["child_table"]),
            "right_column": str(edge["child_column"]),
        }
        for edge in graph.get("ordered_join_edges") or []
    ]
    old_edges = _old_join_edges(tree, aliases)
    old_expansion = _expansion_count(
        start=entity_alias,
        edges=old_edges,
        unique_columns=catalog.unique_columns,
        alias_graph=True,
    )
    new_expansion = _expansion_count(
        start=entity_table.casefold(),
        edges=new_edges,
        unique_columns=catalog.unique_columns,
        alias_graph=False,
    )
    diagnostics = {
        "essential_tables": essential_tables,
        "entity_table": entity_table,
        "entity_primary_key": entity_keys[0],
        "entity_mode": entity_mode,
        "old_join_count": len(joins),
        "new_join_count": len(new_edges),
        "old_expanding_edges": old_expansion,
        "new_expanding_edges": new_expansion,
        "old_table_count": len(original_nodes),
        "new_table_count": len(graph.get("topological_table_order") or []),
        "graph": graph,
    }
    if (
        old_expansion is None
        or new_expansion is None
        or new_expansion > old_expansion
        or len(new_edges) > len(joins)
    ):
        return {**decision, "reason": "no_cardinality_improvement", **diagnostics}

    # A key swap over the same table topology is not a join-tree improvement:
    # schemas commonly expose several FKs to the same dimension (eye/skin/hair
    # colour), and relationship structure alone cannot choose their semantic role.
    if diagnostics["new_table_count"] >= diagnostics["old_table_count"]:
        return {**decision, "reason": "join_topology_not_reduced", **diagnostics}

    if new_expansion == old_expansion:
        profile_edges = [
            edge
            for edge in graph.get("ordered_join_edges") or []
            if edge.get("evidence_class") == "profile"
        ]
        profile_query_grounded = bool(profile_edges) and all(
            _table_mentioned(question, str(edge[side]))
            for edge in profile_edges
            for side in ("parent_table", "child_table")
        )
        shared_parent_tables = {
            provenance.split("::", 1)[1].rsplit(".", 1)[0]
            for edge in graph.get("ordered_join_edges") or []
            if edge.get("evidence_class") == "derived"
            for provenance in edge.get("provenance_ids") or []
            if str(provenance).startswith("shared_parent::")
        }
        diagnostics["shared_parent_tables"] = sorted(shared_parent_tables)
        diagnostics["profile_edges_query_grounded"] = profile_query_grounded
        # Co-membership on a shared parent is meaningful only when that parent
        # is itself part of the requested semantics (atoms and bonds *in the same
        # molecule*).  It must not turn co-location in a district into a direct
        # customer-account relationship.
        if not profile_query_grounded and (
            not shared_parent_tables
            or not any(
                _table_mentioned(question, table)
                for table in shared_parent_tables
            )
        ):
            return {
                **decision,
                "reason": "shared_parent_not_query_grounded",
                **diagnostics,
            }

    original_signature = {_canonical_edge_signature(edge) for edge in old_edges}
    new_signature = {_canonical_edge_signature(edge) for edge in new_edges}
    if original_signature == new_signature and len(joins) == len(new_edges):
        return {**decision, "reason": "join_tree_unchanged", **diagnostics}

    repaired = tree.copy()
    _replace_join_tree(repaired, graph, original_nodes, aliases)
    distinct_normalized = False
    if new_expansion > 0:
        if entity_mode == "percentage":
            distinct_normalized = _normalize_distinct_entity_percentage(
                repaired,
                entity_alias=entity_alias,
                entity_primary_key=entity_keys[0],
            )
        else:
            distinct_normalized = _normalize_distinct_entity_count(
                repaired,
                entity_alias=entity_alias,
                entity_primary_key=entity_keys[0],
            )
        if not distinct_normalized:
            return {
                **decision,
                "reason": "multiplicity_requires_unsupported_aggregate_rewrite",
                **diagnostics,
            }
    repaired_sql = repaired.sql(dialect=dialect.casefold())
    if not _executable(database, repaired_sql, timeout_seconds):
        return {**decision, "reason": "repair_not_executable", **diagnostics}
    return {
        "selected": "anchor_join_tree_repair",
        "reason": (
            f"cardinality_preserving_{entity_mode}_minimal_join_tree_with_distinct_entity"
            if distinct_normalized
            else f"cardinality_preserving_{entity_mode}_minimal_join_tree"
        ),
        "sql": repaired_sql,
        "uses_evaluator_gold": False,
        "distinct_entity_normalized": distinct_normalized,
        **diagnostics,
    }
