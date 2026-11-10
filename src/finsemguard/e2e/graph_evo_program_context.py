"""Compile a compact Graph+Evolution program block before SQL generation.

The recovery/ontology search result remains the primary model context.  This
module only compiles its query-conditioned relational constraints into a small,
explicit block so the generator does not have to discover them through a later
tool call.  It never consults predictions, scores, gold SQL, or execution rows.
"""

from __future__ import annotations

from copy import deepcopy
from dataclasses import dataclass
from hashlib import sha256
import json
from typing import Any

import sqlglot
from sqlglot import exp

from finsemguard.e2e.livesqlbench import CatalogDocument
from finsemguard.e2e.minimal_join_tree import compile_minimal_join_tree


CONTEXT_COMPILER_ID = "graph_evo_program_context_v3"


def _canonical_json(value: Any) -> str:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )


def _json_object(value: Any) -> dict[str, Any]:
    if isinstance(value, dict):
        return dict(value)
    try:
        parsed = json.loads(str(value or ""))
    except (TypeError, ValueError, json.JSONDecodeError):
        return {}
    return dict(parsed) if isinstance(parsed, dict) else {}


def _strings(values: Any, *, limit: int = 32) -> list[str]:
    if isinstance(values, (str, int, float)):
        values = [values]
    output: list[str] = []
    for value in values or []:
        text = str(value).strip()
        if text and text not in output:
            output.append(text)
        if len(output) >= limit:
            break
    return output


@dataclass(frozen=True, slots=True)
class GraphEvoProgramContext:
    """The paper-facing M3 context passed directly to the SQL consumer."""

    roles: tuple[str, ...]
    physical_bindings: dict[str, list[dict[str, Any]]]
    terminal_tables: tuple[str, ...]
    bridge_tables: tuple[str, ...]
    topological_table_order: tuple[str, ...]
    join_skeleton_sql: str
    typed_join_edges: tuple[dict[str, Any], ...]
    exact_literal_bindings: tuple[dict[str, Any], ...]
    evolution_contract: tuple[dict[str, Any], ...]
    historical_programs: tuple[dict[str, Any], ...]
    metric_time_unit_constraints: tuple[dict[str, Any], ...]
    provenance_ids: tuple[str, ...]

    def to_prompt_payload(self) -> dict[str, Any]:
        return {
            "compiler": CONTEXT_COMPILER_ID,
            "roles": list(self.roles),
            "physical_bindings": self.physical_bindings,
            "terminal_tables": list(self.terminal_tables),
            "bridge_tables": list(self.bridge_tables),
            "topological_table_order": list(self.topological_table_order),
            "join_skeleton_sql": self.join_skeleton_sql,
            "typed_join_edges": list(self.typed_join_edges),
            "exact_literal_bindings": list(self.exact_literal_bindings),
            "evolution_contract": list(self.evolution_contract),
            "historical_programs": list(self.historical_programs),
            "metric_time_unit_constraints": list(
                self.metric_time_unit_constraints
            ),
            "provenance_ids": list(self.provenance_ids),
            "uses_evaluator_gold": False,
        }

    @property
    def context_sha256(self) -> str:
        return sha256(_canonical_json(self.to_prompt_payload()).encode()).hexdigest()


_BINDING_KEYS = (
    "physical_identifier",
    "physical_table",
    "evidence_candidate_id",
    "evidence_kind",
    "required_companion_identifiers",
    "semantic_alignment",
    "semantic_alignment_status",
    "role_rrf",
)


def _binding(candidate: Any) -> dict[str, Any]:
    source = dict(candidate) if isinstance(candidate, dict) else {}
    output = {
        key: source[key]
        for key in _BINDING_KEYS
        if source.get(key) not in (None, "", [])
    }
    companions = _strings(output.get("required_companion_identifiers"))
    if companions:
        output["required_companion_identifiers"] = companions
    return output


def _physical_bindings(graph: dict[str, Any]) -> dict[str, list[dict[str, Any]]]:
    selected = dict(graph.get("role_choices") or {})
    candidates = dict(graph.get("query_role_bindings") or {})
    roles = list(dict.fromkeys([*selected, *candidates]))
    output: dict[str, list[dict[str, Any]]] = {}
    for role in roles:
        if role in selected:
            choices = [_binding(selected[role])]
        else:
            choices = [
                _binding(value)
                for value in list(candidates.get(role) or [])[:3]
            ]
        choices = [value for value in choices if value.get("physical_identifier")]
        if choices:
            output[str(role)] = choices
    return output


def _typed_edges(graph: dict[str, Any]) -> tuple[dict[str, Any], ...]:
    keys = (
        "step",
        "left",
        "right",
        "parent_table",
        "parent_column",
        "child_table",
        "child_column",
        "on_sql",
        "evidence_class",
        "evidence_types",
        "provenance_ids",
        "certified",
        "physical_join_columns_known",
    )
    output: list[dict[str, Any]] = []
    for source in (
        graph.get("ordered_join_edges")
        or graph.get("physical_join_edges")
        or []
    ):
        if not isinstance(source, dict):
            continue
        edge = {
            key: source[key]
            for key in keys
            if source.get(key) not in (None, "", [])
        }
        if edge:
            output.append(edge)
    return tuple(output)


def _anchor_physical_tables(
    anchor_sql: str | None,
    *,
    raw_documents: list[CatalogDocument],
    dialect: str,
) -> list[str]:
    """Recover only physical tables already referenced by the frozen anchor."""

    if not anchor_sql:
        return []
    canonical = {
        str(row.table).casefold(): str(row.table)
        for row in raw_documents
        if row.table
    }
    try:
        tree = sqlglot.parse_one(anchor_sql, read=dialect.casefold())
    except Exception:
        return []
    output: list[str] = []
    for table in tree.find_all(exp.Table):
        physical = canonical.get(str(table.name).casefold())
        if physical and physical not in output:
            output.append(physical)
    return output


def _unique_exact_literal_bindings(
    exact_value_matches: dict[str, Any] | None,
    *,
    raw_documents: list[CatalogDocument],
) -> list[dict[str, Any]]:
    """Promote only complete, unique exact-value probes to graph terminals.

    Exact database matches are strong column evidence only when the bounded
    scan completed and one question literal maps to exactly one current
    physical column.  Ambiguous or truncated matches remain available to the
    SQL consumer in its ordinary grounding payload, but cannot certify an M3
    terminal or an M4 predicate transformation.
    """

    payload = dict(exact_value_matches or {})
    if payload.get("truncated") is True:
        return []
    canonical_tables = {
        str(row.table).casefold(): str(row.table)
        for row in raw_documents
        if row.table
    }
    by_literal: dict[str, dict[str, dict[str, Any]]] = {}
    for source in payload.get("matches") or []:
        if not isinstance(source, dict) or int(source.get("row_count") or 0) <= 0:
            continue
        physical_identifier = str(source.get("physical_column") or "").strip()
        table, separator, column = physical_identifier.rpartition(".")
        canonical_table = canonical_tables.get(table.casefold())
        literal = str(source.get("literal") or "")
        if not separator or not canonical_table or not column or not literal:
            continue
        canonical_identifier = f"{canonical_table}.{column}"
        by_literal.setdefault(literal, {})[
            canonical_identifier.casefold()
        ] = {
            "literal": literal,
            "matched_value": source.get("matched_value"),
            "physical_identifier": canonical_identifier,
            "physical_table": canonical_table,
            "row_count": int(source["row_count"]),
            "evidence": str(source.get("evidence") or "exact_database_value"),
        }

    output: list[dict[str, Any]] = []
    for literal, candidates in by_literal.items():
        if len(candidates) != 1:
            continue
        binding = next(iter(candidates.values()))
        provenance_basis = _canonical_json(binding)
        output.append(
            {
                **binding,
                "binding_status": "unique_exact_current_value",
                "provenance_id": (
                    "exact_value::" + sha256(provenance_basis.encode()).hexdigest()
                ),
                "uses_evaluator_gold": False,
            }
        )
    return output


def recompile_graph_evo_query_graph(
    initial_search: dict[str, Any],
    *,
    raw_documents: list[CatalogDocument],
    ontology_edges: list[dict[str, Any]],
    anchor_sql: str | None,
    exact_value_matches: dict[str, Any] | None,
    dialect: str,
) -> dict[str, Any]:
    """Recompile M3 after anchor and exact-literal evidence are available.

    The first schema-search graph is intentionally high recall.  The unified
    main then performs one deterministic compilation pass before generation:
    anchor-referenced physical tables are mandatory terminals, unique exact
    current-value matches are mandatory filter terminals, and an unresolved
    output retrieval is not allowed to displace an output table already fixed
    by the anchor.  No prediction, score, expected answer, or gold SQL enters
    this pass.
    """

    source_graph = deepcopy(
        dict(initial_search.get("query_relational_program_graph") or {})
    )
    if not source_graph or not raw_documents:
        return source_graph
    anchor_tables = _anchor_physical_tables(
        anchor_sql,
        raw_documents=raw_documents,
        dialect=dialect,
    )
    exact_bindings = _unique_exact_literal_bindings(
        exact_value_matches,
        raw_documents=raw_documents,
    )
    exact_tables = [
        str(binding["physical_table"]) for binding in exact_bindings
    ]

    source_bindings = deepcopy(dict(source_graph.get("query_role_bindings") or {}))
    role_bindings: dict[str, list[dict[str, Any]]] = {}
    suppressed_roles: list[str] = []
    for role, values in source_bindings.items():
        candidates = [dict(value) for value in values or [] if isinstance(value, dict)]
        supported = [
            value
            for value in candidates
            if str(
                dict(value.get("semantic_alignment") or {}).get("status") or ""
            )
            == "lexically_supported"
        ]
        if supported:
            # A positive physical-field witness dominates opaque alternatives;
            # retaining the latter can make a shorter but unrelated table win.
            role_bindings[str(role)] = supported
        elif str(role).casefold().startswith("output role:") and anchor_tables:
            suppressed_roles.append(str(role))
        elif candidates:
            # Opaque-schema recovery can legitimately have no lexical signal.
            # Preserve those hypotheses when the anchor does not already fix
            # the requested output relation.
            role_bindings[str(role)] = candidates

    compiled = compile_minimal_join_tree(
        raw_documents=raw_documents,
        ontology_edges=ontology_edges,
        role_bindings=role_bindings,
        required_tables=list(dict.fromkeys([*anchor_tables, *exact_tables])),
        fallback_tables=list(source_graph.get("template_advisory_tables") or []),
    )
    for key in ("query_operators", "program_templates", "history_template_limit"):
        if key in source_graph:
            compiled[key] = deepcopy(source_graph[key])
    compiled["query_role_bindings"] = role_bindings
    compiled["anchor_required_tables"] = anchor_tables
    compiled["exact_literal_required_tables"] = exact_tables
    compiled["exact_literal_bindings"] = exact_bindings
    compiled["suppressed_unresolved_output_roles"] = suppressed_roles
    if suppressed_roles:
        compiled["unresolved_roles"] = list(
            dict.fromkeys([*compiled.get("unresolved_roles", []), *suppressed_roles])
        )
        compiled["certificate"]["all_roles_connected"] = False
    compiled["certificate"]["graph_evo_recompile"] = {
        "anchor_tables_are_required_terminals": bool(anchor_tables),
        "unique_exact_literals_are_required_terminals": bool(exact_bindings),
        "suppressed_unresolved_output_roles": suppressed_roles,
        "uses_evaluator_gold": False,
    }
    compiled["uses_evaluator_gold"] = False
    return compiled


def _result_inventory(
    initial_search: dict[str, Any],
) -> tuple[list[dict[str, Any]], dict[str, dict[str, Any]]]:
    rows = [
        dict(value)
        for value in initial_search.get("results") or []
        if isinstance(value, dict)
    ]
    return rows, {
        str(row.get("evidence_candidate_id") or ""): row
        for row in rows
        if row.get("evidence_candidate_id")
    }


def _evolution_contracts(
    rows: list[dict[str, Any]],
    selected_ids: set[str],
    selected_identifiers: set[str],
) -> tuple[dict[str, Any], ...]:
    output: list[dict[str, Any]] = []
    allowed = (
        "relation",
        "current_physical_identifier",
        "historical_source_identifiers",
        "current_table",
        "historical_source_tables",
        "source_table",
        "target_table",
        "key_lineage",
    )
    for row in rows:
        kind = str(row.get("kind") or "")
        candidate_id = str(row.get("evidence_candidate_id") or "")
        physical_name = str(row.get("physical_name") or "")
        if not (
            kind.startswith("schema_evolution_")
            or kind == "schema_lineage_column"
        ):
            continue
        if candidate_id not in selected_ids and physical_name not in selected_identifiers:
            continue
        evidence = _json_object(row.get("evidence"))
        contract = {
            key: evidence[key]
            for key in allowed
            if evidence.get(key) not in (None, "", [], {})
        }
        contract["provenance_id"] = candidate_id
        contract["evidence_kind"] = kind
        if contract not in output:
            output.append(contract)
        if len(output) >= 16:
            break
    return tuple(output)


def _historical_programs(
    graph: dict[str, Any], by_id: dict[str, dict[str, Any]]
) -> tuple[dict[str, Any], ...]:
    output: list[dict[str, Any]] = []
    evidence_keys = (
        "historical_question",
        "question_pattern",
        "compiled_current_sql_pattern",
        "sql_template",
        "current_lineage_bindings",
        "physical_tables",
        "physical_columns",
        "provenance",
        "provenance_id",
        "target_disjoint",
    )
    template_keys = (
        "matched_query_operators",
        "missing_query_operators",
        "template_operators",
        "relevant_physical_tables",
        "selection_basis",
        "semantic_rrf",
        "operator_compatibility",
        "topic_overlap",
    )
    for template in list(graph.get("program_templates") or [])[:max(2, min(8, int(graph.get("history_template_limit", 2))))]:
        if not isinstance(template, dict):
            continue
        candidate_id = str(template.get("candidate_id") or "")
        evidence = _json_object(by_id.get(candidate_id, {}).get("evidence"))
        program: dict[str, Any] = {"provenance_id": candidate_id}
        program.update(
            {
                key: evidence[key]
                for key in evidence_keys
                if evidence.get(key) not in (None, "", [], {})
            }
        )
        program.update(
            {
                key: template[key]
                for key in template_keys
                if template.get(key) not in (None, "", [], {})
            }
        )
        if candidate_id and len(program) > 1:
            output.append(program)
    return tuple(output)


def _metric_constraints(
    rows: list[dict[str, Any]], selected_ids: set[str]
) -> tuple[dict[str, Any], ...]:
    output: list[dict[str, Any]] = []
    contract_keys = (
        "metric_contract",
        "time_contract",
        "unit_contract",
        "metric",
        "formula",
        "unit",
        "currency",
        "time_grain",
        "period",
        "scale",
        "aggregation",
    )
    for row in rows:
        candidate_id = str(row.get("evidence_candidate_id") or "")
        if candidate_id not in selected_ids and str(row.get("kind") or "") != "knowledge":
            continue
        evidence = _json_object(row.get("evidence"))
        contract = {
            key: evidence[key]
            for key in contract_keys
            if evidence.get(key) not in (None, "", [], {}, "unknown")
        }
        if not contract:
            continue
        for key in ("physical_identifiers", "aliases", "description"):
            if evidence.get(key) not in (None, "", [], {}):
                contract[key] = evidence[key]
        contract["provenance_id"] = candidate_id
        output.append(contract)
        if len(output) >= 8:
            break
    return tuple(output)


def compile_graph_evo_program_context(
    initial_search: dict[str, Any],
) -> GraphEvoProgramContext:
    """Compile only query-time retrieved assets into a deterministic M3 block."""

    graph = dict(initial_search.get("query_relational_program_graph") or {})
    bindings = _physical_bindings(graph)
    rows, by_id = _result_inventory(initial_search)
    selected_ids = {
        str(choice.get("evidence_candidate_id") or "")
        for choices in bindings.values()
        for choice in choices
        if choice.get("evidence_candidate_id")
    }
    selected_identifiers = {
        str(choice.get("physical_identifier") or "")
        for choices in bindings.values()
        for choice in choices
        if choice.get("physical_identifier")
    }
    for choices in bindings.values():
        for choice in choices:
            selected_identifiers.update(
                _strings(choice.get("required_companion_identifiers"))
            )
    historical = _historical_programs(graph, by_id)
    history_ids = {
        str(value.get("provenance_id") or "")
        for value in historical
        if value.get("provenance_id")
    }
    edges = _typed_edges(graph)
    exact_literals = tuple(
        dict(value)
        for value in graph.get("exact_literal_bindings") or []
        if isinstance(value, dict)
        and value.get("binding_status") == "unique_exact_current_value"
        and value.get("uses_evaluator_gold") is False
    )
    evolution = _evolution_contracts(
        rows,
        selected_ids=selected_ids,
        selected_identifiers=selected_identifiers,
    )
    metrics = _metric_constraints(rows, selected_ids)
    provenance = list(dict.fromkeys([*selected_ids, *history_ids]))
    for edge in edges:
        provenance.extend(_strings(edge.get("provenance_ids")))
    provenance.extend(
        str(value.get("provenance_id"))
        for value in exact_literals
        if value.get("provenance_id")
    )
    provenance.extend(
        str(value.get("provenance_id"))
        for value in [*evolution, *metrics]
        if value.get("provenance_id")
    )
    terminals = _strings(
        graph.get("terminal_tables") or graph.get("topological_table_order")
    )
    terminals.extend(
        str(choice["physical_table"])
        for choices in bindings.values()
        for choice in choices
        if choice.get("physical_table")
        and str(choice["physical_table"]) not in terminals
    )
    return GraphEvoProgramContext(
        roles=tuple(bindings),
        physical_bindings=bindings,
        terminal_tables=tuple(terminals),
        bridge_tables=tuple(_strings(graph.get("bridge_tables"))),
        topological_table_order=tuple(
            _strings(graph.get("topological_table_order"))
        ),
        join_skeleton_sql=str(graph.get("join_skeleton_sql") or ""),
        typed_join_edges=edges,
        exact_literal_bindings=exact_literals,
        evolution_contract=evolution,
        historical_programs=historical,
        metric_time_unit_constraints=metrics,
        provenance_ids=tuple(_strings(provenance, limit=128)),
    )
