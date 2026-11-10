"""Anchor-preserving repair for explicit relation and column evolution.

The repair consumes only the frozen anchor SQL, the user question, the current
catalog, and released/automatically recovered schema lineage.  It never reads a
gold query or execution label.  Two narrow transformations are currently allowed:

* replace a non-certified join between copied table-split relations with the
  smallest current, relationship-certified join tree; and
* restore a complete split-column projection when the question requests the
  historical compound field rather than one named component.

Every predicate, grouping, ordering, limit, and operator outside FROM/JOIN and an
explicit split projection is fingerprinted before and after repair.
"""

from __future__ import annotations

from hashlib import sha256
import json
from pathlib import Path
import re
import sqlite3
import time
from typing import Any

import sqlglot
from sqlglot import exp

from finsemguard.e2e.anchor_join_tree_repair import (
    _canonical_edge_signature,
    _old_join_edges,
    _replace_join_tree,
    _top_level_sources,
)
from finsemguard.e2e.evolution_relations import (
    RelationEvolutionMapping,
    build_evolution_documents,
    reverse_map_evolved_sql,
)
from finsemguard.e2e.minimal_join_tree import compile_minimal_join_tree


def _sha(value: str) -> str:
    return sha256(value.encode()).hexdigest()


def _nearest_select(node: exp.Expression) -> exp.Select | None:
    parent = node.parent
    while parent is not None:
        if isinstance(parent, exp.Select):
            return parent
        parent = parent.parent
    return None


def _preserved_clause_fingerprint(tree: exp.Select, dialect: str) -> str:
    copy = tree.copy()
    copy.set("from_", None)
    copy.set("joins", [])
    # Projections have their own explicit audit because split-column restoration
    # is the only permitted non-relation edit.
    copy.set("expressions", [])
    return _sha(copy.sql(dialect=dialect))


def _projection_fingerprint(tree: exp.Select, dialect: str) -> str:
    return _sha(
        json.dumps(
            [value.sql(dialect=dialect) for value in tree.expressions],
            ensure_ascii=False,
            separators=(",", ":"),
        )
    )


def _adapter_probe(
    database: Path,
    sql: str,
    mapping: RelationEvolutionMapping,
    timeout_seconds: float,
) -> dict[str, Any]:
    try:
        reverse = reverse_map_evolved_sql(sql, mapping=mapping)
    except Exception as error:
        return {
            "executable": False,
            "error_type": type(error).__name__,
            "error": str(error)[:500],
        }
    connection = sqlite3.connect(f"file:{database.resolve()}?mode=ro", uri=True)
    deadline = time.monotonic() + timeout_seconds
    connection.set_progress_handler(
        lambda: int(time.monotonic() > deadline), 1000
    )
    try:
        connection.execute(reverse).fetchone()
        return {"executable": True, "reverse_sql_sha256": _sha(reverse)}
    except Exception as error:
        return {
            "executable": False,
            "error_type": type(error).__name__,
            "error": str(error)[:500],
            "reverse_sql_sha256": _sha(reverse),
        }
    finally:
        connection.close()


def _question_mentions(value: str, question: str) -> bool:
    phrase = " ".join(re.findall(r"[a-z0-9]+", value.casefold()))
    normalized = " ".join(re.findall(r"[a-z0-9]+", question.casefold()))
    return bool(phrase and re.search(rf"\b{re.escape(phrase)}s?\b", normalized))


def _expand_compound_split_projections(
    tree: exp.Select,
    *,
    question: str,
    mapping: RelationEvolutionMapping,
) -> list[dict[str, Any]]:
    aliases, _nodes = _top_level_sources(tree)
    if not aliases:
        return []
    table_lookup = {
        table.name.casefold(): table.name for table in mapping.current_snapshot.tables
    }
    direct_tables = list(dict.fromkeys(aliases.values()))
    transformations: list[dict[str, Any]] = []
    expressions = list(tree.expressions)
    for current_table, operations in mapping.column_operations.items():
        split_columns = [
            column for column, operation in operations.items() if operation == "split"
        ]
        groups: dict[tuple[str, str], list[str]] = {}
        for current_column in split_columns:
            sources = mapping.column_sources[current_table][current_column]
            if len(sources) == 1:
                source = sources[0]
                groups.setdefault(
                    (source.table.casefold(), source.column.casefold()), []
                ).append(current_column)
        schema_order = {
            column.name: index
            for index, column in enumerate(
                mapping.current_snapshot.by_name[current_table].columns
            )
        }
        for (_source_table, source_column), siblings in groups.items():
            if len(siblings) < 2 or not _question_mentions(source_column, question):
                continue
            if any(_question_mentions(sibling, question) for sibling in siblings):
                # "year" or "domain" asks for a component, not the compound.
                continue
            matched: list[tuple[int, exp.Column, str]] = []
            for index, projection in enumerate(expressions):
                node = projection.this if isinstance(projection, exp.Alias) else projection
                if not isinstance(node, exp.Column) or isinstance(projection, exp.Alias):
                    continue
                qualifier = str(node.table or "")
                if qualifier:
                    supplied_table = aliases.get(qualifier.casefold())
                else:
                    supplied_table = direct_tables[0] if len(direct_tables) == 1 else None
                resolved = table_lookup.get(str(supplied_table or "").casefold())
                if resolved != current_table or not any(
                    node.name.casefold() == sibling.casefold() for sibling in siblings
                ):
                    continue
                matched.append((index, node, qualifier))
            if not matched:
                continue
            present = {node.name.casefold() for _index, node, _alias in matched}
            ordered = sorted(siblings, key=lambda value: schema_order[value])
            missing = [value for value in ordered if value.casefold() not in present]
            if not missing:
                continue
            insertion = max(index for index, _node, _alias in matched) + 1
            qualifier = matched[0][2]
            additions = [
                exp.column(column, table=qualifier or None, quoted=True)
                for column in missing
            ]
            expressions[insertion:insertion] = additions
            transformations.append(
                {
                    "kind": "complete_compound_split_projection",
                    "current_table": current_table,
                    "historical_compound_column": source_column,
                    "present_components": sorted(present),
                    "added_components": missing,
                }
            )
    if transformations:
        tree.set("expressions", expressions)
    return transformations


def _split_join_repair(
    tree: exp.Select,
    *,
    mapping: RelationEvolutionMapping,
) -> tuple[exp.Select | None, dict[str, Any] | None]:
    if mapping.evolution_type != "table_split":
        return None, None
    aliases, original_nodes = _top_level_sources(tree)
    if not aliases:
        return None, None
    current_tables = {
        table.name.casefold(): table.name for table in mapping.current_snapshot.tables
    }
    required_tables = list(dict.fromkeys(aliases.values()))
    if any(table.casefold() not in current_tables for table in required_tables):
        return None, None
    changed_tables = {
        table.casefold()
        for table, sources in mapping.table_sources.items()
        if len(sources) == 1 and table.casefold() != sources[0].casefold()
    }
    used_changed = [
        table for table in required_tables if table.casefold() in changed_tables
    ]
    if len(used_changed) < 2:
        return None, None

    certified_split_signatures: set[tuple[str, str, str, str]] = set()
    for edge in mapping.relationship_edges:
        evidence = [str(value) for value in edge.get("evidence_types") or []]
        if "evolution_split_key_equivalence" not in evidence:
            continue
        left_table, separator, left_column = str(edge.get("left") or "").rpartition(
            "."
        )
        right_table, right_separator, right_column = str(
            edge.get("right") or ""
        ).rpartition(".")
        if not separator or not right_separator:
            continue
        certified_split_signatures.add(
            _canonical_edge_signature(
                {
                    "left_table": left_table,
                    "left_column": left_column,
                    "right_table": right_table,
                    "right_column": right_column,
                }
            )
        )
    if not certified_split_signatures:
        return None, {"reason": "no_certified_split_key"}

    def connects_changed(
        signatures: set[tuple[str, str, str, str]],
    ) -> bool:
        required = {value.casefold() for value in used_changed}
        adjacency: dict[str, set[str]] = {value: set() for value in required}
        for signature in signatures:
            left_table, right_table = signature[0], signature[2]
            if left_table in required and right_table in required:
                adjacency[left_table].add(right_table)
                adjacency[right_table].add(left_table)
        visited = {next(iter(required))}
        frontier = list(visited)
        while frontier:
            table = frontier.pop()
            for neighbor in adjacency[table] - visited:
                visited.add(neighbor)
                frontier.append(neighbor)
        return visited == required

    old_edges = _old_join_edges(tree, aliases)
    old_signatures = {_canonical_edge_signature(edge) for edge in old_edges}
    old_certified_split = old_signatures & certified_split_signatures
    if connects_changed(old_certified_split):
        return None, {"reason": "split_join_already_certified"}

    raw_and_lineage, _bindings, ontology_edges = build_evolution_documents(
        mapping, "evolution-repair"
    )
    raw_documents = [
        row for row in raw_and_lineage if row.kind in {"table", "column"}
    ]
    graph = compile_minimal_join_tree(
        raw_documents=raw_documents,
        ontology_edges=ontology_edges,
        role_bindings={},
        required_tables=required_tables,
    )
    certificate = dict(graph.get("certificate") or {})
    if (
        graph.get("unresolved_roles")
        or not certificate.get("all_join_columns_known")
        or not certificate.get("all_edges_relationship_certified")
        or set(graph.get("topological_table_order") or []) != set(required_tables)
    ):
        return None, {"reason": "uncertified_current_join_tree", "graph": graph}

    new_edges = [
        {
            "left_table": str(edge["parent_table"]),
            "left_column": str(edge["parent_column"]),
            "right_table": str(edge["child_table"]),
            "right_column": str(edge["child_column"]),
        }
        for edge in graph.get("ordered_join_edges") or []
    ]
    new_signatures = {_canonical_edge_signature(edge) for edge in new_edges}
    changed_cf = {value.casefold() for value in used_changed}

    def touches_split(signature: tuple[str, str, str, str]) -> bool:
        return signature[0] in changed_cf and signature[2] in changed_cf

    old_split = {value for value in old_signatures if touches_split(value)}
    new_split = {value for value in new_signatures if touches_split(value)}
    new_certified_split = new_split & certified_split_signatures
    if not connects_changed(new_certified_split):
        return None, {
            "reason": "compiled_tree_omits_certified_split_key",
            "graph": graph,
        }
    repaired = tree.copy()
    _replace_join_tree(repaired, graph, original_nodes, aliases)
    return (
        repaired,
        {
            "kind": "replace_table_split_join_with_certified_current_tree",
            "old_split_join_signatures": [list(value) for value in sorted(old_split)],
            "new_split_join_signatures": [list(value) for value in sorted(new_split)],
            "graph": graph,
        },
    )


def repair_evolution_aware_relation(
    *,
    sql: str,
    question: str,
    database: Path,
    mapping: RelationEvolutionMapping,
    dialect: str = "sqlite",
    timeout_seconds: float = 5.0,
) -> dict[str, Any]:
    """Return a deterministic repair decision and a non-gold audit certificate."""

    # ``run_react_text2sql`` exposes human-readable dialect labels (for
    # example ``SQLite``), while sqlglot's registry is case-sensitive.  Keep
    # the public API permissive and normalize once before every parse/render
    # operation.  Without this, the production EvoSchema path silently
    # returned ``parse_error:ValueError`` for every example even though the
    # SQL itself was valid.
    dialect_name = dialect.casefold()

    base: dict[str, Any] = {
        "selected": "anchor",
        "reason": "not_applicable",
        "sql": sql,
        "uses_evaluator_gold": False,
        "evolution_type": mapping.evolution_type,
    }
    try:
        parsed = sqlglot.parse_one(sql, read=dialect_name)
    except Exception as error:
        return {**base, "reason": f"parse_error:{type(error).__name__}"}
    if not isinstance(parsed, exp.Select) or parsed.args.get("with_") is not None:
        return {**base, "reason": "non_simple_select"}
    if any(node is not parsed for node in parsed.find_all(exp.Select)):
        return {**base, "reason": "nested_select"}
    joins = list(parsed.args.get("joins") or [])
    if any(
        str(join.args.get("side") or "").casefold() not in {""}
        or str(join.args.get("kind") or "").casefold() not in {"", "inner"}
        for join in joins
    ):
        return {**base, "reason": "non_inner_join"}

    before_probe = _adapter_probe(database, sql, mapping, timeout_seconds)
    before_clause = _preserved_clause_fingerprint(parsed, dialect_name)
    before_projection = _projection_fingerprint(parsed, dialect_name)
    working = parsed.copy()
    transformations = _expand_compound_split_projections(
        working,
        question=question,
        mapping=mapping,
    )
    join_repaired, join_audit = _split_join_repair(working, mapping=mapping)
    if join_repaired is not None:
        working = join_repaired
        assert join_audit is not None
        transformations.append(join_audit)
    if not transformations:
        return {
            **base,
            "reason": str((join_audit or {}).get("reason") or "not_applicable"),
            "anchor_probe": before_probe,
            **({"join_audit": join_audit} if join_audit else {}),
        }

    after_clause = _preserved_clause_fingerprint(working, dialect_name)
    if after_clause != before_clause:
        return {
            **base,
            "reason": "preserved_clause_fingerprint_changed",
            "transformations": transformations,
        }
    repaired_sql = working.sql(dialect=dialect_name)
    after_probe = _adapter_probe(database, repaired_sql, mapping, timeout_seconds)
    if not after_probe.get("executable"):
        return {
            **base,
            "reason": "repair_not_executable",
            "anchor_probe": before_probe,
            "repair_probe": after_probe,
            "transformations": transformations,
        }
    return {
        "selected": "evolution_aware_relation_repair",
        "reason": "+".join(str(value["kind"]) for value in transformations),
        "sql": repaired_sql,
        "uses_evaluator_gold": False,
        "evolution_type": mapping.evolution_type,
        "anchor_probe": before_probe,
        "repair_probe": after_probe,
        "transformations": transformations,
        "audit": {
            "preserved_clause_sha256_before": before_clause,
            "preserved_clause_sha256_after": after_clause,
            "preserved_clause_unchanged": before_clause == after_clause,
            "projection_sha256_before": before_projection,
            "projection_sha256_after": _projection_fingerprint(
                working, dialect_name
            ),
            "anchor_sql_sha256": _sha(sql),
            "repaired_sql_sha256": _sha(repaired_sql),
        },
    }
