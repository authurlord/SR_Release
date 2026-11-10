"""Compile and realize an evidence-carrying, role-first relational program.

The previous Graph+Evo path rendered a high-recall graph but then froze every
clause of a first-stage SQL draft.  Consequently the graph could be present in
the prompt and consumed by M4 while still being unable to correct a wrong
``FROM``/``JOIN`` program.  This module makes the query-time method object
explicit.  Semantic roles and their physical evidence are retained first,
relationship connectivity is retained second, and path cost is only metadata.

The module never reads evaluator SQL, labels, scores, or expected results.  A
submitted SQL program is realized only after the ordinary read-only execution
tool has executed that exact AST and the question-derived result-shape contract
has passed.  This is structural admission of the method's one submitted output,
not selection between candidates.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import json
from typing import Any

import sqlglot
from sqlglot import exp

from finsemguard.e2e.anchored_relation_program import (
    compose_anchor_relation_program,
)


ROLE_FIRST_COMPILER_ID = "role_first_connected_relational_program_v1"
ROLE_FIRST_REALIZER_ID = "executed_role_first_program_realizer_v1"


def _canonical_json(value: Any) -> str:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )


def _sha(value: str) -> str:
    return sha256(value.encode("utf-8")).hexdigest()


def _strings(values: Any, *, limit: int = 128) -> tuple[str, ...]:
    if isinstance(values, (str, int, float)):
        values = [values]
    output: list[str] = []
    for value in values or []:
        text = str(value).strip()
        if text and text not in output:
            output.append(text)
        if len(output) >= limit:
            break
    return tuple(output)


def _quote(identifier: str, dialect: str) -> str:
    return exp.to_identifier(str(identifier), quoted=True).sql(
        dialect=dialect.casefold()
    )


def _edge_endpoint(edge: dict[str, Any], side: str) -> tuple[str, str] | None:
    table = str(edge.get(f"{side}_table") or "").strip()
    column = str(edge.get(f"{side}_column") or "").strip()
    if table and column:
        return table, column
    value = str(edge.get(side) or "")
    table, separator, column = value.rpartition(".")
    if separator and table and column:
        return table, column
    return None


def _render_join_scaffold(
    table_order: tuple[str, ...],
    edges: tuple[dict[str, Any], ...],
    *,
    dialect: str,
) -> str:
    if not table_order:
        return ""
    edge_by_child = {
        str(edge.get("child_table") or "").casefold(): edge
        for edge in edges
        if edge.get("child_table")
    }
    lines = [f"FROM {_quote(table_order[0], dialect)}"]
    observed = {table_order[0].casefold()}
    for table in table_order[1:]:
        edge = edge_by_child.get(table.casefold())
        if edge is None:
            return ""
        parent = _edge_endpoint(edge, "parent")
        child = _edge_endpoint(edge, "child")
        if parent is None or child is None:
            return ""
        if parent[0].casefold() not in observed or child[0].casefold() != table.casefold():
            return ""
        lines.append(
            "JOIN "
            + _quote(child[0], dialect)
            + " ON "
            + f"{_quote(parent[0], dialect)}.{_quote(parent[1], dialect)}"
            + " = "
            + f"{_quote(child[0], dialect)}.{_quote(child[1], dialect)}"
        )
        observed.add(table.casefold())
    return "\n".join(lines)


def _anchor_contract(anchor_sql: str, dialect: str) -> dict[str, Any]:
    try:
        tree = sqlglot.parse_one(anchor_sql, read=dialect.casefold())
    except Exception:
        return {
            "parseable": False,
            "tables": [],
            "projections": [],
            "predicates": [],
        }
    select = tree if isinstance(tree, exp.Select) else next(tree.find_all(exp.Select), None)
    projections = (
        [value.sql(dialect=dialect.casefold()) for value in select.expressions]
        if select is not None
        else []
    )
    predicates = [
        value.this.sql(dialect=dialect.casefold())
        for value in tree.find_all(exp.Where)
    ]
    predicates.extend(
        value.this.sql(dialect=dialect.casefold())
        for value in tree.find_all(exp.Having)
    )
    return {
        "parseable": True,
        "tables": list(
            dict.fromkeys(str(value.name) for value in tree.find_all(exp.Table))
        ),
        "projections": projections,
        "predicates": predicates,
    }


@dataclass(frozen=True, slots=True)
class RelationalProgram:
    role_bindings: dict[str, list[dict[str, Any]]]
    terminal_tables: tuple[str, ...]
    bridge_tables: tuple[str, ...]
    typed_edges: tuple[dict[str, Any], ...]
    join_order: tuple[str, ...]
    join_scaffold_sql: str
    projection_contract: tuple[dict[str, Any], ...]
    predicate_contract: tuple[dict[str, Any], ...]
    evolution_contract: tuple[dict[str, Any], ...]
    historical_programs: tuple[dict[str, Any], ...]
    metric_time_unit_contract: tuple[dict[str, Any], ...]
    evidence_ids: tuple[str, ...]
    anchor_contract: dict[str, Any]

    def to_prompt_payload(self) -> dict[str, Any]:
        payload = {
            "compiler": ROLE_FIRST_COMPILER_ID,
            "optimization_priority": [
                "semantic_and_evidence_support",
                "required_role_coverage",
                "current_physical_validity",
                "typed_relation_connectivity",
                "minimum_program_cost",
            ],
            "role_bindings": self.role_bindings,
            "terminal_tables": list(self.terminal_tables),
            "bridge_tables": list(self.bridge_tables),
            "typed_edges": list(self.typed_edges),
            "join_order": list(self.join_order),
            "join_scaffold_sql": self.join_scaffold_sql,
            "projection_contract": list(self.projection_contract),
            "predicate_contract": list(self.predicate_contract),
            "evolution_contract": list(self.evolution_contract),
            "historical_programs": list(self.historical_programs),
            "metric_time_unit_contract": list(self.metric_time_unit_contract),
            "evidence_ids": list(self.evidence_ids),
            "base_draft_contract": self.anchor_contract,
            "uses_evaluator_gold": False,
        }
        payload["program_sha256"] = _sha(_canonical_json(payload))
        return payload


def compile_role_first_relational_program(
    *,
    graph_evo_context: dict[str, Any],
    anchor_sql: str,
    dialect: str,
) -> RelationalProgram:
    """Convert the M3 context into the paper-facing query program."""

    if graph_evo_context.get("uses_evaluator_gold") is not False:
        raise ValueError("role-first compilation requires a gold-free M3 context")
    bindings = {
        str(role): [dict(value) for value in values if isinstance(value, dict)]
        for role, values in dict(
            graph_evo_context.get("physical_bindings") or {}
        ).items()
    }
    edges = tuple(
        dict(value)
        for value in graph_evo_context.get("typed_join_edges") or []
        if isinstance(value, dict)
    )
    trusted_classes = {"declared", "history", "knowledge", "evolution_key"}
    trusted_edges = tuple(
        edge
        for edge in edges
        if edge.get("certified") is True
        and edge.get("physical_join_columns_known") is True
        and str(edge.get("evidence_class") or "").casefold() in trusted_classes
    )
    order = _strings(graph_evo_context.get("topological_table_order"))
    if not order:
        for edge in trusted_edges:
            for key in ("parent_table", "child_table"):
                value = str(edge.get(key) or "").strip()
                if value and value not in order:
                    order = (*order, value)
    scaffold = _render_join_scaffold(order, trusted_edges, dialect=dialect)

    projection: list[dict[str, Any]] = []
    predicate: list[dict[str, Any]] = []
    for role, choices in bindings.items():
        contract = {"role": role, "physical_candidates": choices}
        kind = role.partition(" role:")[0].casefold()
        if kind in {"filter", "literal", "join"}:
            predicate.append(contract)
        else:
            projection.append(contract)
    for binding in graph_evo_context.get("exact_literal_bindings") or []:
        if isinstance(binding, dict):
            predicate.append(
                {
                    "role": f"exact literal: {binding.get('literal')}",
                    "physical_candidates": [dict(binding)],
                }
            )

    evidence = list(_strings(graph_evo_context.get("provenance_ids")))
    for edge in trusted_edges:
        for value in _strings(edge.get("provenance_ids")):
            if value not in evidence:
                evidence.append(value)
    return RelationalProgram(
        role_bindings=bindings,
        terminal_tables=_strings(graph_evo_context.get("terminal_tables")),
        bridge_tables=_strings(graph_evo_context.get("bridge_tables")),
        typed_edges=trusted_edges,
        join_order=order,
        join_scaffold_sql=scaffold,
        projection_contract=tuple(projection),
        predicate_contract=tuple(predicate),
        evolution_contract=tuple(
            dict(value)
            for value in graph_evo_context.get("evolution_contract") or []
            if isinstance(value, dict)
        ),
        historical_programs=tuple(
            dict(value)
            for value in graph_evo_context.get("historical_programs") or []
            if isinstance(value, dict)
        ),
        metric_time_unit_contract=tuple(
            dict(value)
            for value in graph_evo_context.get("metric_time_unit_constraints") or []
            if isinstance(value, dict)
        ),
        evidence_ids=tuple(evidence),
        anchor_contract=_anchor_contract(anchor_sql, dialect),
    )


def _ast_inventory(sql: str, dialect: str) -> dict[str, Any] | None:
    try:
        tree = sqlglot.parse_one(sql, read=dialect.casefold())
    except Exception:
        return None
    return {
        "tables": list(
            dict.fromkeys(str(value.name) for value in tree.find_all(exp.Table))
        ),
        "columns": list(
            dict.fromkeys(
                (
                    f"{value.table}.{value.name}"
                    if value.table
                    else str(value.name)
                )
                for value in tree.find_all(exp.Column)
            )
        ),
        "selects": len(list(tree.find_all(exp.Select))),
        "joins": len(list(tree.find_all(exp.Join))),
        "ctes": len(list(tree.find_all(exp.CTE))),
        "set_operations": sum(
            isinstance(value, (exp.Union, exp.Intersect, exp.Except))
            for value in tree.walk()
        ),
        "windows": len(list(tree.find_all(exp.Window))),
        "groupings": len(list(tree.find_all(exp.Group))),
        "havings": len(list(tree.find_all(exp.Having))),
        "orderings": len(list(tree.find_all(exp.Order))),
    }


def _edge_signature(
    left_table: str,
    left_column: str,
    right_table: str,
    right_column: str,
) -> tuple[str, str, str, str]:
    left = (left_table.casefold(), left_column.casefold())
    right = (right_table.casefold(), right_column.casefold())
    if right < left:
        left, right = right, left
    return left[0], left[1], right[0], right[1]


def _certified_graph_relation_program(
    graph_evo_context: dict[str, Any],
) -> tuple[set[tuple[str, str, str, str]], set[str]] | None:
    """Return the exact certified relation tree exposed by M3.

    M4 may use only physical edges with explicit certification and provenance.
    An empty or incomplete edge set is not authority to replace an existing
    relation program.
    """

    signatures: set[tuple[str, str, str, str]] = set()
    tables: set[str] = set()
    trusted_classes = {"declared", "history", "knowledge", "evolution_key"}
    edges = [
        dict(value)
        for value in graph_evo_context.get("typed_join_edges") or []
        if isinstance(value, dict)
    ]
    if not edges:
        return None
    provenance_ids = {
        str(value) for value in graph_evo_context.get("provenance_ids") or []
    }
    for edge in edges:
        left = _edge_endpoint(edge, "left")
        right = _edge_endpoint(edge, "right")
        edge_provenance = {
            str(value) for value in edge.get("provenance_ids") or []
        }
        if (
            left is None
            or right is None
            or edge.get("certified") is not True
            or edge.get("physical_join_columns_known") is not True
            or str(edge.get("evidence_class") or "").casefold()
            not in trusted_classes
            or not edge_provenance
            or not edge_provenance <= provenance_ids
        ):
            return None
        signatures.add(_edge_signature(*left, *right))
        tables.update((left[0].casefold(), right[0].casefold()))
    if len(tables) != len(signatures) + 1:
        return None
    return signatures, tables


def _submitted_relation_program(
    sql: str, dialect: str
) -> tuple[set[tuple[str, str, str, str]], set[str]] | None:
    """Extract one pure inner-equijoin tree from the submitted SQL."""

    try:
        tree = sqlglot.parse_one(sql, read=dialect.casefold())
    except Exception:
        return None
    if not isinstance(tree, exp.Select):
        return None
    sources: list[exp.Table] = []
    from_clause = tree.args.get("from_")
    if from_clause is None or not isinstance(from_clause.this, exp.Table):
        return None
    sources.append(from_clause.this)
    joins = list(tree.args.get("joins") or [])
    if not joins:
        return None
    for join in joins:
        if not isinstance(join.this, exp.Table):
            return None
        if (
            str(join.args.get("side") or "").casefold()
            or str(join.args.get("kind") or "").casefold() not in {"", "inner"}
        ):
            return None
        sources.append(join.this)
    aliases = {
        str(source.alias_or_name).casefold(): str(source.name).casefold()
        for source in sources
    }
    if len(aliases) != len(sources):
        return None
    signatures: set[tuple[str, str, str, str]] = set()
    for join in joins:
        on = join.args.get("on")
        if on is None:
            return None
        predicates = list(on.flatten()) if isinstance(on, exp.And) else [on]
        for predicate in predicates:
            if not isinstance(predicate, exp.EQ):
                return None
            left = predicate.this
            right = predicate.expression
            if not isinstance(left, exp.Column) or not isinstance(right, exp.Column):
                return None
            left_alias = str(left.table).casefold()
            right_alias = str(right.table).casefold()
            if (
                not left_alias
                or not right_alias
                or left_alias == right_alias
                or left_alias not in aliases
                or right_alias not in aliases
            ):
                return None
            signatures.add(
                _edge_signature(
                    aliases[left_alias],
                    str(left.name),
                    aliases[right_alias],
                    str(right.name),
                )
            )
    tables = {str(source.name).casefold() for source in sources}
    if len(tables) != len(signatures) + 1:
        return None
    return signatures, tables


def _normalized_non_relation_program(
    sql: str,
    dialect: str,
    *,
    alias_map: dict[str, str] | None = None,
) -> str | None:
    """Return the clause program outside top-level FROM/JOIN.

    Alias spelling and identifier quoting are transport details.  Literals,
    projections, predicates, grouping, ordering, windows, and nested-query
    structure remain exact.  A relation proposal is admissible here only when
    the model independently preserves that Raw program; evidence-bound output
    and literal additions are handled by the narrower downstream operators.
    """

    try:
        tree = sqlglot.parse_one(sql, read=dialect.casefold())
    except Exception:
        return None
    if not isinstance(tree, exp.Select):
        return None
    normalized = tree.copy()
    normalized.set("from_", None)
    normalized.set("joins", [])
    aliases = {
        str(key).casefold(): str(value) for key, value in (alias_map or {}).items()
    }
    for column in normalized.find_all(exp.Column):
        qualifier = str(column.table or "").casefold()
        if qualifier and qualifier in aliases:
            column.set("table", exp.to_identifier(aliases[qualifier]))
    for identifier in normalized.find_all(exp.Identifier):
        identifier.set("this", str(identifier.this).casefold())
        identifier.set("quoted", False)
    return normalized.sql(dialect=dialect.casefold()).casefold()


def realize_executed_role_first_program(
    *,
    anchor_sql: str,
    proposal_sql: str,
    graph_evo_context: dict[str, Any],
    proposal_execution: dict[str, Any] | None,
    dialect: str,
) -> dict[str, Any]:
    """Realize the one submitted, executed program without score selection."""

    identity = {
        "operator": ROLE_FIRST_REALIZER_ID,
        "applied": False,
        "reason": "submitted_program_not_structurally_admitted",
        "sql": anchor_sql,
        "uses_evaluator_gold": False,
    }
    if graph_evo_context.get("uses_evaluator_gold") is not False:
        return {**identity, "reason": "graph_context_does_not_exclude_gold"}
    normalized = str(proposal_sql or "").strip()
    if not normalized:
        return {**identity, "reason": "missing_submitted_program"}
    proposal_inventory = _ast_inventory(normalized, dialect)
    anchor_inventory = _ast_inventory(anchor_sql, dialect)
    if proposal_inventory is None:
        return {**identity, "reason": "submitted_program_is_not_parseable"}
    execution = dict(proposal_execution or {})
    if (
        execution.get("executable") is not True
        or execution.get("query_contract_satisfied") is not True
        or execution.get("gold_or_expected_answer_used") is not False
    ):
        return {**identity, "reason": "missing_exact_execution_certificate"}
    if execution.get("proposal_sql_sha256") != _sha(normalized):
        return {**identity, "reason": "execution_certificate_sql_mismatch"}

    program = compile_role_first_relational_program(
        graph_evo_context=graph_evo_context,
        anchor_sql=anchor_sql,
        dialect=dialect,
    ).to_prompt_payload()
    submitted_changed = [
        key
        for key in (
            "tables",
            "columns",
            "selects",
            "joins",
            "ctes",
            "set_operations",
            "windows",
            "groupings",
            "havings",
            "orderings",
        )
        if (anchor_inventory or {}).get(key) != proposal_inventory.get(key)
    ]
    graph_relation = _certified_graph_relation_program(graph_evo_context)
    submitted_relation = _submitted_relation_program(normalized, dialect)
    if graph_relation is None:
        return {
            **identity,
            "reason": "missing_complete_certified_graph_relation_program",
            "program_sha256": program["program_sha256"],
            "submitted_ast_dimensions_ignored": submitted_changed,
        }
    if submitted_relation != graph_relation:
        return {
            **identity,
            "reason": "submitted_relation_program_differs_from_certified_graph",
            "program_sha256": program["program_sha256"],
            "submitted_ast_dimensions_ignored": submitted_changed,
        }
    anchor_tables = {
        str(value).casefold() for value in (anchor_inventory or {}).get("tables") or []
    }
    graph_tables = set(graph_relation[1])
    added_tables = graph_tables - anchor_tables
    terminal_tables = {
        str(value).casefold()
        for value in graph_evo_context.get("terminal_tables") or []
    }
    bridge_tables = {
        str(value).casefold()
        for value in graph_evo_context.get("bridge_tables") or []
    }
    if (
        added_tables
        and terminal_tables
        and terminal_tables <= anchor_tables
        and added_tables <= bridge_tables
    ):
        return {
            **identity,
            "reason": "raw_relation_already_covers_terminals_bridge_not_required",
            "program_sha256": program["program_sha256"],
            "submitted_ast_dimensions_ignored": submitted_changed,
            "added_bridge_tables": sorted(added_tables),
        }
    composition = compose_anchor_relation_program(
        anchor_sql=anchor_sql,
        candidate_sql=normalized,
        dialect=dialect,
    )
    realized_sql = str(composition.get("sql") or anchor_sql)
    if composition.get("applied") is not True:
        return {
            **identity,
            "reason": str(
                composition.get("reason")
                or "certified_relation_program_was_identity"
            ),
            "program_sha256": program["program_sha256"],
            "submitted_ast_dimensions_ignored": submitted_changed,
            "relation_composition": {
                key: value for key, value in composition.items() if key != "sql"
            },
        }
    anchor_non_relation = _normalized_non_relation_program(anchor_sql, dialect)
    submitted_non_relation = _normalized_non_relation_program(
        normalized,
        dialect,
        alias_map=dict(composition.get("alias_map") or {}),
    )
    if (
        anchor_non_relation is None
        or submitted_non_relation is None
        or anchor_non_relation != submitted_non_relation
    ):
        return {
            **identity,
            "reason": "submitted_non_relation_program_lacks_raw_consensus",
            "program_sha256": program["program_sha256"],
            "submitted_ast_dimensions_ignored": submitted_changed,
            "relation_composition": {
                key: value for key, value in composition.items() if key != "sql"
            },
        }
    realized_inventory = _ast_inventory(realized_sql, dialect) or {}
    anchor_inventory = anchor_inventory or {}
    changed = [
        key
        for key in (
            "tables",
            "columns",
            "selects",
            "joins",
            "ctes",
            "set_operations",
            "windows",
            "groupings",
            "havings",
            "orderings",
        )
        if anchor_inventory.get(key) != realized_inventory.get(key)
    ]
    return {
        "operator": ROLE_FIRST_REALIZER_ID,
        "applied": True,
        "reason": "certified_relation_program_composed_into_raw_backbone",
        "sql": realized_sql,
        "program_sha256": program["program_sha256"],
        "anchor_inventory": anchor_inventory,
        "submitted_inventory": proposal_inventory,
        "realized_inventory": realized_inventory,
        "changed_ast_dimensions": changed,
        "submitted_ast_dimensions_ignored": sorted(
            set(submitted_changed) - set(changed)
        ),
        "relation_composition": {
            key: value for key, value in composition.items() if key != "sql"
        },
        "non_relation_ast_preserved": True,
        "execution_certificate": execution,
        "score_or_expected_answer_consulted": False,
        "candidate_selection_performed": False,
        "uses_evaluator_gold": False,
    }
