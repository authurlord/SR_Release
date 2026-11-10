"""Compile an anchor SQL query into an evidence-backed relational program.

The language model may propose relational intent, but it cannot replace any
anchor clause. Two narrow typed extensions may be appended: a graph-certified
explicitly requested output role and a uniquely grounded exact question-literal
predicate. Declared evolution may also expand a historical compound output into
its current fields. This
compiler emits the anchor unchanged when no operator is structurally justified.
The identity result is part of the compiler semantics; it is not a score-based
candidate choice.

Static schemas currently support nine operators:

* graph-certified completion of a unique exact-literal predicate and its
  relationship path, optionally together with graph-bound missing outputs;
* graph-certified completion of a missing requested output role, admitted only
  when the executed proposal preserves every anchor expression and all
  non-relation clauses and uses the exact certified relationship tree;
* proposal-directed outer-to-inner refinement over the exact same certified edge;
* proposal-and-graph-agreed relation-key substitution, admitted only when the
  replacement is grounded by a frozen non-join dependency and propagated through
  that dependency;
* graph-certified relation-key substitution inside named CTE scopes;
* graph-certified exposure of a hidden CTE relation key to an outer join;
* graph-and-proposal-agreed substitution of a complete relation tree while the
  non-relation AST remains exactly frozen;
* certified elimination of a redundant parent-key lookup;
* cardinality-aware minimal relationship-tree compilation.

Evolving schemas use the explicit evolution-lineage compiler, whose only projection
exception is expansion of a historically compound field into its declared current
split columns.
"""

from __future__ import annotations

from decimal import Decimal, InvalidOperation
from hashlib import sha256
import json
from pathlib import Path
import sqlite3
import time
from typing import TYPE_CHECKING, Any

import sqlglot
from sqlglot import exp

from finsemguard.e2e.anchor_join_tree_repair import (
    inspect_sqlite_relationship_catalog,
    repair_anchor_join_tree,
)
from finsemguard.e2e.anchored_relation_program import (
    compose_anchor_relation_program,
)
from finsemguard.e2e.role_first_relational_program import (
    realize_executed_role_first_program,
)

if TYPE_CHECKING:
    from finsemguard.e2e.evolution_relations import RelationEvolutionMapping


COMPILER_ID = "evolution_aware_relational_program_compiler_v15_role_first"


def _sha(value: str) -> str:
    return sha256(value.encode("utf-8")).hexdigest()


def _top_level_select(sql: str, dialect: str) -> exp.Select | None:
    try:
        tree = sqlglot.parse_one(sql, read=dialect.casefold())
    except Exception:
        return None
    return tree if isinstance(tree, exp.Select) else None


def _simple_select(sql: str, dialect: str) -> exp.Select | None:
    tree = _top_level_select(sql, dialect)
    if tree is None or tree.args.get("with_") is not None:
        return None
    if any(node is not tree for node in tree.find_all(exp.Select)):
        return None
    return tree


def _sources(
    tree: exp.Select,
) -> tuple[list[tuple[str, str]], dict[str, str]] | None:
    from_clause = tree.args.get("from_")
    if from_clause is None or not isinstance(from_clause.this, exp.Table):
        return None
    tables: list[exp.Table] = [from_clause.this]
    tables.extend(join.this for join in tree.args.get("joins") or [])
    if any(not isinstance(table, exp.Table) for table in tables):
        return None
    ordered: list[tuple[str, str]] = []
    aliases: dict[str, str] = {}
    seen_tables: set[str] = set()
    for table in tables:
        assert isinstance(table, exp.Table)
        name = str(table.name)
        alias = str(table.alias_or_name)
        if not name or not alias:
            return None
        name_cf = name.casefold()
        alias_cf = alias.casefold()
        if name_cf in seen_tables or alias_cf in aliases:
            return None
        seen_tables.add(name_cf)
        aliases[alias_cf] = name
        ordered.append((name_cf, alias_cf))
    return ordered, aliases


def _join_condition_fingerprint(
    join: exp.Join, aliases: dict[str, str], dialect: str
) -> str | None:
    """Canonicalize one ON clause using physical table names, not aliases."""

    on = join.args.get("on")
    if on is None:
        return None
    normalized = on.copy()
    for column in normalized.find_all(exp.Column):
        qualifier = str(column.table).casefold()
        if qualifier not in aliases:
            return None
        column.set("table", exp.to_identifier(aliases[qualifier].casefold()))
        # Quoting is a serialization choice, not relation identity.  Anchors
        # and proposals often come from different SQL renderers (x.id versus
        # X.\"ID\"); retaining the original quoted flag made equal edges compare
        # unequal and silently disabled otherwise valid typed operators.
        column.set("this", exp.to_identifier(str(column.name).casefold()))
    return normalized.sql(dialect=dialect.casefold()).casefold()


def _conjuncts(node: exp.Expression) -> list[exp.Expression]:
    if isinstance(node, exp.And):
        return [*_conjuncts(node.this), *_conjuncts(node.expression)]
    return [node]


def _join_edge_signatures(
    join: exp.Join, aliases: dict[str, str]
) -> set[tuple[str, str, str, str]] | None:
    """Return physical equality edges local to one JOIN clause."""

    on = join.args.get("on")
    if on is None:
        return None
    output: set[tuple[str, str, str, str]] = set()
    for equality in _conjuncts(on):
        if not isinstance(equality, exp.EQ):
            return None
        left, right = equality.this, equality.expression
        if not isinstance(left, exp.Column) or not isinstance(right, exp.Column):
            # A deterministic column-to-literal constraint can coexist with the
            # physical equality edge (for example, role='OWNER').  It is copied
            # unchanged and compared through the full ON fingerprint above.
            if isinstance(left, exp.Column) != isinstance(right, exp.Column):
                continue
            return None
        left_alias = str(left.table).casefold()
        right_alias = str(right.table).casefold()
        if left_alias not in aliases or right_alias not in aliases:
            return None
        first = (aliases[left_alias].casefold(), str(left.name).casefold())
        second = (aliases[right_alias].casefold(), str(right.name).casefold())
        if second < first:
            first, second = second, first
        output.add((first[0], first[1], second[0], second[1]))
    return output or None


def _join_endpoint_pairs(
    join: exp.Join, aliases: dict[str, str]
) -> list[tuple[tuple[str, str], tuple[str, str]]] | None:
    """Return physical column pairs while retaining endpoint direction."""

    on = join.args.get("on")
    if on is None:
        return None
    output: list[tuple[tuple[str, str], tuple[str, str]]] = []
    for equality in _conjuncts(on):
        if not isinstance(equality, exp.EQ):
            return None
        left, right = equality.this, equality.expression
        if not isinstance(left, exp.Column) or not isinstance(right, exp.Column):
            if isinstance(left, exp.Column) != isinstance(right, exp.Column):
                continue
            return None
        left_alias = str(left.table).casefold()
        right_alias = str(right.table).casefold()
        if left_alias not in aliases or right_alias not in aliases:
            return None
        output.append(
            (
                (aliases[left_alias].casefold(), str(left.name).casefold()),
                (aliases[right_alias].casefold(), str(right.name).casefold()),
            )
        )
    return output or None


def _edge_signature(
    pair: tuple[tuple[str, str], tuple[str, str]],
) -> tuple[str, str, str, str]:
    first, second = pair
    if second < first:
        first, second = second, first
    return first[0], first[1], second[0], second[1]


def _catalog_edge_signatures(
    database: Path,
    *,
    database_id: str,
    tables: list[str],
    table_old_to_new: dict[str, str] | None,
    column_old_to_new: dict[str, dict[str, str]] | None,
) -> set[tuple[str, str, str, str]]:
    catalog = inspect_sqlite_relationship_catalog(
        database,
        database_id=database_id,
        table_old_to_new=table_old_to_new,
        column_old_to_new=column_old_to_new,
        compatibility_tables=tables,
    )
    output: set[tuple[str, str, str, str]] = set()
    for edge in catalog.edges:
        try:
            left_table, left_column = str(edge["left"]).rsplit(".", 1)
            right_table, right_column = str(edge["right"]).rsplit(".", 1)
        except (KeyError, ValueError):
            continue
        first = (left_table.casefold(), left_column.casefold())
        second = (right_table.casefold(), right_column.casefold())
        if second < first:
            first, second = second, first
        output.add((first[0], first[1], second[0], second[1]))
    return output


def _provided_edge_signatures(
    edges: list[dict[str, Any]],
) -> set[tuple[str, str, str, str]]:
    output: set[tuple[str, str, str, str]] = set()
    for edge in edges:
        try:
            left_table, left_column = str(edge["left"]).rsplit(".", 1)
            right_table, right_column = str(edge["right"]).rsplit(".", 1)
        except (KeyError, ValueError):
            continue
        first = (left_table.casefold(), left_column.casefold())
        second = (right_table.casefold(), right_column.casefold())
        if second < first:
            first, second = second, first
        output.add((first[0], first[1], second[0], second[1]))
    return output


def _strong_query_edge_signatures(
    edges: list[dict[str, Any]],
) -> set[tuple[str, str, str, str]]:
    """Return edges strong enough for graph-directed compilation by themselves."""

    trusted_evidence = {
        "declared_foreign_key",
        "declared_or_materialized_relationship",
        "external_knowledge_relationship",
    }
    strong: list[dict[str, Any]] = []
    for edge in edges:
        evidence = {str(value) for value in edge.get("evidence_types") or []}
        explicitly_certified = edge.get("certified") is True
        known_with_evidence = (
            edge.get("physical_join_columns_known") is True
            and bool(evidence & trusted_evidence)
        )
        if explicitly_certified or known_with_evidence:
            strong.append(edge)
    return _provided_edge_signatures(strong)


def _normalized_identifier_ast_sql(
    tree: exp.Expression, dialect: str
) -> str:
    """Serialize an AST with identifier quoting/case removed from identity."""

    normalized = tree.copy()
    for identifier in normalized.find_all(exp.Identifier):
        identifier.set("this", str(identifier.this).casefold())
        identifier.set("quoted", False)
    return normalized.sql(dialect=dialect.casefold()).casefold()


def _direct_projection_column(
    expression: exp.Expression,
) -> exp.Column | None:
    candidate = expression.this if isinstance(expression, exp.Alias) else expression
    if not isinstance(candidate, exp.Column) or str(candidate.name) == "*":
        return None
    return candidate


def _execution_certificate_matches(
    proposal_sql: str, proposal_execution: dict[str, Any] | None
) -> bool:
    return bool(
        proposal_execution
        and proposal_execution.get("executable") is True
        and proposal_execution.get("query_contract_satisfied") is True
        and proposal_execution.get("gold_or_expected_answer_used") is False
        and str(proposal_execution.get("proposal_sql_sha256") or "")
        == _sha(proposal_sql.strip())
    )


def _literal_values_equal(sql_literal: exp.Literal, candidate: Any) -> bool:
    rendered = str(sql_literal.this)
    if sql_literal.is_string:
        return rendered == str(candidate)
    try:
        return Decimal(rendered) == Decimal(str(candidate))
    except (InvalidOperation, ValueError):
        return rendered == str(candidate)


def _compile_graph_exact_literal_program_completion(
    *,
    anchor_sql: str,
    proposal_sql: str,
    dialect: str,
    graph_evo_context: dict[str, Any] | None,
    proposal_execution: dict[str, Any] | None,
) -> dict[str, Any]:
    """Append only unique exact-literal filters over the exact M3 tree.

    The proposal must retain every anchor projection and predicate, may append
    only graph-bound direct output columns, and may append only equality
    predicates whose value and current physical column were uniquely matched by
    the deterministic database probe embedded in the exact Graph+Evo context.
    """

    identity: dict[str, Any] = {
        "operator": "graph_certified_exact_literal_program_completion",
        "applied": False,
        "reason": "exact_literal_program_completion_not_applicable",
        "sql": anchor_sql,
        "uses_evaluator_gold": False,
    }
    if graph_evo_context is None:
        return {**identity, "reason": "missing_graph_evo_context"}
    if not _execution_certificate_matches(proposal_sql, proposal_execution):
        return {**identity, "reason": "missing_or_invalid_proposal_execution_certificate"}

    anchor = _simple_select(anchor_sql, dialect)
    proposal = _simple_select(proposal_sql, dialect)
    if anchor is None or proposal is None:
        return {**identity, "reason": "exact_literal_requires_simple_selects"}
    anchor_sources = _sources(anchor)
    proposal_sources = _sources(proposal)
    if anchor_sources is None or proposal_sources is None:
        return {**identity, "reason": "exact_literal_has_unsupported_sources"}
    anchor_order, anchor_aliases = anchor_sources
    proposal_order, proposal_aliases = proposal_sources
    anchor_tables = {table for table, _alias in anchor_order}
    proposal_tables = {table for table, _alias in proposal_order}
    if not anchor_tables.issubset(proposal_tables):
        return {**identity, "reason": "proposal_removes_anchor_table"}
    anchor_alias_by_table = {table: alias for table, alias in anchor_order}
    proposal_alias_by_table = {table: alias for table, alias in proposal_order}
    if any(
        anchor_alias_by_table[table] != proposal_alias_by_table[table]
        for table in anchor_tables
    ):
        return {**identity, "reason": "proposal_changes_anchor_table_alias"}

    anchor_expressions = list(anchor.expressions)
    proposal_expressions = list(proposal.expressions)
    if len(proposal_expressions) < len(anchor_expressions):
        return {**identity, "reason": "proposal_removes_anchor_projection"}
    for anchor_expression, proposal_expression in zip(
        anchor_expressions, proposal_expressions, strict=False
    ):
        if _normalized_identifier_ast_sql(
            anchor_expression, dialect
        ) != _normalized_identifier_ast_sql(proposal_expression, dialect):
            return {**identity, "reason": "proposal_changes_anchor_projection"}

    provenance_ids = {
        str(value) for value in graph_evo_context.get("provenance_ids") or []
    }
    output_bindings: dict[str, dict[str, str]] = {}
    for role, candidates in dict(
        graph_evo_context.get("physical_bindings") or {}
    ).items():
        if not str(role).casefold().startswith("output role:"):
            continue
        for candidate in candidates or []:
            identifier = str(candidate.get("physical_identifier") or "").casefold()
            evidence_id = str(candidate.get("evidence_candidate_id") or "")
            if (
                identifier
                and evidence_id in provenance_ids
                and str(candidate.get("semantic_alignment_status") or "")
                == "lexically_supported"
            ):
                output_bindings[identifier] = {
                    "role": str(role),
                    "evidence_candidate_id": evidence_id,
                }
    added_projections: list[dict[str, str]] = []
    seen_outputs: set[str] = set()
    for expression in proposal_expressions[len(anchor_expressions) :]:
        column = _direct_projection_column(expression)
        if column is None:
            return {**identity, "reason": "added_projection_is_not_direct_column"}
        qualifier = str(column.table).casefold()
        if not qualifier or qualifier not in proposal_aliases:
            return {**identity, "reason": "added_projection_is_not_physically_bound"}
        identifier = f"{proposal_aliases[qualifier]}.{column.name}".casefold()
        binding = output_bindings.get(identifier)
        if binding is None:
            return {**identity, "reason": "added_projection_has_no_output_role_binding"}
        if identifier in seen_outputs:
            return {**identity, "reason": "duplicate_role_projection"}
        seen_outputs.add(identifier)
        added_projections.append({"physical_identifier": identifier, **binding})

    anchor_shell = anchor.copy()
    anchor_shell.set("expressions", [])
    anchor_shell.set("from_", None)
    anchor_shell.set("joins", [])
    anchor_shell.set("where", None)
    proposal_shell = proposal.copy()
    proposal_shell.set("expressions", [])
    proposal_shell.set("from_", None)
    proposal_shell.set("joins", [])
    proposal_shell.set("where", None)
    cardinality_normalization: str | None = None
    anchor_distinct = anchor.args.get("distinct")
    proposal_distinct = proposal.args.get("distinct")
    if anchor_distinct is None and proposal_distinct is not None:
        anchor_projection_columns = [
            _direct_projection_column(expression)
            for expression in anchor_expressions
        ]
        projected_anchor_tables = {
            anchor_aliases.get(str(column.table).casefold(), "").casefold()
            for column in anchor_projection_columns
            if column is not None and column.table
        }
        distinct_is_relation_cardinality_normalization = bool(
            len(proposal_expressions) == len(anchor_expressions)
            and len(anchor_tables) == 1
            and len(proposal_tables) > len(anchor_tables)
            and anchor_projection_columns
            and all(column is not None for column in anchor_projection_columns)
            and projected_anchor_tables == anchor_tables
            and not any(
                expression.find(exp.AggFunc) is not None
                or expression.find(exp.Window) is not None
                for expression in anchor_expressions
            )
            and all(
                anchor.args.get(key) is None
                for key in (
                    "group",
                    "having",
                    "qualify",
                    "order",
                    "limit",
                    "offset",
                )
            )
        )
        if distinct_is_relation_cardinality_normalization:
            proposal_shell.set("distinct", None)
            cardinality_normalization = (
                "distinct_anchor_entity_after_certified_relation_expansion"
            )
    if _normalized_identifier_ast_sql(
        anchor_shell, dialect
    ) != _normalized_identifier_ast_sql(proposal_shell, dialect):
        return {**identity, "reason": "proposal_changes_frozen_nonrelation_ast"}

    anchor_where = anchor.args.get("where")
    proposal_where = proposal.args.get("where")
    anchor_conjuncts = (
        _conjuncts(anchor_where.this) if isinstance(anchor_where, exp.Where) else []
    )
    proposal_conjuncts = (
        _conjuncts(proposal_where.this) if isinstance(proposal_where, exp.Where) else []
    )
    remaining = list(proposal_conjuncts)
    for anchor_conjunct in anchor_conjuncts:
        fingerprint = _normalized_identifier_ast_sql(anchor_conjunct, dialect)
        match_index = next(
            (
                index
                for index, candidate in enumerate(remaining)
                if _normalized_identifier_ast_sql(candidate, dialect) == fingerprint
            ),
            None,
        )
        if match_index is None:
            return {**identity, "reason": "proposal_removes_or_changes_anchor_predicate"}
        remaining.pop(match_index)
    if not remaining:
        return {**identity, "reason": "proposal_adds_no_exact_literal_predicate"}

    allowed_evidence = {
        "exact_database_value",
        "current_database_value",
        "exact_storage_value_through_lineage",
        "derived_current_value_through_lineage",
    }
    exact_bindings: dict[str, list[dict[str, Any]]] = {}
    for value in graph_evo_context.get("exact_literal_bindings") or []:
        binding = dict(value) if isinstance(value, dict) else {}
        identifier = str(binding.get("physical_identifier") or "").casefold()
        provenance_id = str(binding.get("provenance_id") or "")
        if (
            identifier
            and binding.get("binding_status") == "unique_exact_current_value"
            and binding.get("uses_evaluator_gold") is False
            and int(binding.get("row_count") or 0) > 0
            and str(binding.get("evidence") or "") in allowed_evidence
            and provenance_id in provenance_ids
        ):
            exact_bindings.setdefault(identifier, []).append(binding)

    added_predicates: list[dict[str, Any]] = []
    seen_predicates: set[tuple[str, str]] = set()
    for conjunct in remaining:
        if not isinstance(conjunct, exp.EQ):
            return {**identity, "reason": "added_predicate_is_not_exact_equality"}
        left, right = conjunct.this, conjunct.expression
        if isinstance(left, exp.Literal) and isinstance(right, exp.Column):
            literal, column = left, right
        elif isinstance(left, exp.Column) and isinstance(right, exp.Literal):
            column, literal = left, right
        else:
            return {**identity, "reason": "added_predicate_is_not_column_literal_equality"}
        qualifier = str(column.table).casefold()
        if not qualifier or qualifier not in proposal_aliases:
            return {**identity, "reason": "added_predicate_column_is_not_physically_bound"}
        identifier = f"{proposal_aliases[qualifier]}.{column.name}".casefold()
        binding = next(
            (
                candidate
                for candidate in exact_bindings.get(identifier, [])
                if _literal_values_equal(literal, candidate.get("matched_value"))
                or _literal_values_equal(literal, candidate.get("literal"))
            ),
            None,
        )
        if binding is None:
            return {**identity, "reason": "added_predicate_has_no_unique_exact_binding"}
        signature = (identifier, str(literal.this))
        if signature in seen_predicates:
            return {**identity, "reason": "duplicate_exact_literal_predicate"}
        seen_predicates.add(signature)
        added_predicates.append(
            {
                "physical_identifier": identifier,
                "literal": binding.get("literal"),
                "matched_value": binding.get("matched_value"),
                "row_count": binding.get("row_count"),
                "evidence": binding.get("evidence"),
                "provenance_id": binding.get("provenance_id"),
            }
        )

    typed_edges = [
        dict(value)
        for value in graph_evo_context.get("typed_join_edges") or []
        if isinstance(value, dict)
    ]
    trusted_classes = {"declared", "history", "knowledge"}
    if any(
        edge.get("certified") is not True
        or edge.get("physical_join_columns_known") is not True
        or str(edge.get("evidence_class") or "").casefold() not in trusted_classes
        for edge in typed_edges
    ):
        return {**identity, "reason": "exact_literal_graph_not_strongly_certified"}
    graph_signatures = _strong_query_edge_signatures(typed_edges)
    proposal_signatures = _strict_inner_join_signatures(proposal, proposal_aliases) or set()
    anchor_signatures = _strict_inner_join_signatures(anchor, anchor_aliases) or set()
    if anchor_signatures - proposal_signatures:
        return {**identity, "reason": "proposal_removes_anchor_relation"}
    if proposal_signatures != graph_signatures:
        return {
            **identity,
            "reason": "proposal_relation_tree_differs_from_graph",
            "proposal_edge_signatures": [
                list(value) for value in sorted(proposal_signatures)
            ],
            "graph_edge_signatures": [
                list(value) for value in sorted(graph_signatures)
            ],
        }
    graph_tables = {
        table
        for signature in graph_signatures
        for table in (signature[0], signature[2])
    }
    if graph_signatures:
        if graph_tables != proposal_tables or len(proposal_tables) != len(graph_signatures) + 1:
            return {**identity, "reason": "exact_literal_graph_is_not_complete_tree"}
    elif len(proposal_tables) != 1:
        return {**identity, "reason": "exact_literal_missing_relation_tree"}

    sql = proposal.sql(dialect=dialect.casefold())
    return {
        "operator": "graph_certified_exact_literal_program_completion",
        "applied": True,
        "reason": "executed_proposal_appends_unique_exact_literal_program",
        "sql": sql,
        "added_predicates": added_predicates,
        "added_projections": added_projections,
        "added_tables": sorted(proposal_tables - anchor_tables),
        "edge_signatures": [list(value) for value in sorted(graph_signatures)],
        "anchor_clauses_preserved": True,
        "cardinality_normalization": cardinality_normalization,
        "proposal_execution_sha256": _sha(proposal_sql.strip()),
        "uses_evaluator_gold": False,
    }


def _sql_covers_graph_exact_literals(
    sql: str, graph_evo_context: dict[str, Any] | None, dialect: str
) -> bool:
    """Return whether every M3 exact-literal terminal is already a SQL filter."""

    bindings = [
        dict(value)
        for value in (graph_evo_context or {}).get("exact_literal_bindings") or []
        if isinstance(value, dict)
        and value.get("binding_status") == "unique_exact_current_value"
        and value.get("uses_evaluator_gold") is False
    ]
    if not bindings:
        return True
    tree = _simple_select(sql, dialect)
    sources = _sources(tree) if tree is not None else None
    if tree is None or sources is None:
        return False
    _order, aliases = sources
    where = tree.args.get("where")
    if not isinstance(where, exp.Where):
        return False
    covered: set[str] = set()
    for conjunct in _conjuncts(where.this):
        if not isinstance(conjunct, exp.EQ):
            continue
        left, right = conjunct.this, conjunct.expression
        if isinstance(left, exp.Literal) and isinstance(right, exp.Column):
            literal, column = left, right
        elif isinstance(left, exp.Column) and isinstance(right, exp.Literal):
            column, literal = left, right
        else:
            continue
        qualifier = str(column.table).casefold()
        if qualifier not in aliases:
            continue
        identifier = f"{aliases[qualifier]}.{column.name}".casefold()
        for binding in bindings:
            if identifier != str(binding.get("physical_identifier") or "").casefold():
                continue
            if _literal_values_equal(
                literal, binding.get("matched_value")
            ) or _literal_values_equal(literal, binding.get("literal")):
                covered.add(str(binding.get("provenance_id") or identifier))
    required = {
        str(binding.get("provenance_id") or binding.get("physical_identifier") or "")
        for binding in bindings
    }
    return bool(required) and required <= covered


def compile_graph_evo_candidate_scaffold(
    *,
    anchor_sql: str,
    proposal_sql: str,
    graph_evo_context: dict[str, Any],
    dialect: str,
) -> dict[str, Any]:
    """Build the unexecuted ReACT seed from M0 clauses and the exact M3 tree.

    This is deliberately not a final-output certificate.  It mechanically
    restores every anchor clause after installing the planner's certified
    relation tree, then appends only graph-bound direct outputs and unique
    exact-literal predicates.  ReACT must still execute the result and M4 must
    independently certify the submitted SQL before any extension is retained.
    """

    result: dict[str, Any] = {
        "candidate_sql": proposal_sql,
        "applied": False,
        "compiler": "graph_evo_unexecuted_candidate_scaffold_v1",
        "reason": "candidate_scaffold_not_applicable",
        "final_output_authorized": False,
        "uses_evaluator_gold": False,
    }
    if graph_evo_context.get("uses_evaluator_gold") is not False:
        return {**result, "reason": "graph_context_does_not_exclude_gold"}
    proposal = _simple_select(proposal_sql, dialect)
    proposal_sources = _sources(proposal) if proposal is not None else None
    if proposal is None or proposal_sources is None:
        return {**result, "reason": "planner_proposal_is_not_simple_select"}
    _proposal_order, proposal_aliases = proposal_sources

    typed_edges = [
        dict(value)
        for value in graph_evo_context.get("typed_join_edges") or []
        if isinstance(value, dict)
    ]
    trusted_classes = {"declared", "history", "knowledge"}
    if any(
        edge.get("certified") is not True
        or edge.get("physical_join_columns_known") is not True
        or str(edge.get("evidence_class") or "").casefold() not in trusted_classes
        for edge in typed_edges
    ):
        return {**result, "reason": "planner_relation_graph_not_strongly_certified"}
    graph_signatures = _strong_query_edge_signatures(typed_edges)
    proposal_signatures = _strict_inner_join_signatures(proposal, proposal_aliases) or set()
    proposal_tables = {str(value).casefold() for value in proposal_aliases.values()}
    if proposal_signatures != graph_signatures:
        return {**result, "reason": "planner_relation_tree_differs_from_graph"}
    if graph_signatures:
        graph_tables = {
            table
            for signature in graph_signatures
            for table in (signature[0], signature[2])
        }
        if graph_tables != proposal_tables or len(proposal_tables) != len(graph_signatures) + 1:
            return {**result, "reason": "planner_graph_is_not_complete_tree"}
    elif len(proposal_tables) != 1:
        return {**result, "reason": "planner_graph_missing_relation_tree"}

    composition = compose_anchor_relation_program(
        anchor_sql=anchor_sql,
        candidate_sql=proposal_sql,
        dialect=dialect,
    )
    scaffold_sql = str(composition.get("sql") or anchor_sql)
    if composition.get("applied") is not True:
        return {
            **result,
            "reason": str(composition.get("reason") or "anchor_composition_failed"),
        }
    scaffold = _simple_select(scaffold_sql, dialect)
    scaffold_sources = _sources(scaffold) if scaffold is not None else None
    if scaffold is None or scaffold_sources is None:
        return {**result, "reason": "composed_scaffold_is_not_simple_select"}
    scaffold_order, scaffold_aliases = scaffold_sources
    scaffold_alias_by_table = {
        table: alias for table, alias in scaffold_order
    }

    provenance_ids = {
        str(value) for value in graph_evo_context.get("provenance_ids") or []
    }
    output_bindings: dict[str, dict[str, str]] = {}
    for role, candidates in dict(
        graph_evo_context.get("physical_bindings") or {}
    ).items():
        if not str(role).casefold().startswith("output role:"):
            continue
        for candidate in candidates or []:
            identifier = str(candidate.get("physical_identifier") or "").casefold()
            evidence_id = str(candidate.get("evidence_candidate_id") or "")
            if (
                identifier
                and evidence_id in provenance_ids
                and str(candidate.get("semantic_alignment_status") or "")
                == "lexically_supported"
            ):
                output_bindings[identifier] = {
                    "role": str(role),
                    "evidence_candidate_id": evidence_id,
                }

    existing_outputs: set[str] = set()
    for expression in scaffold.expressions:
        column = _direct_projection_column(expression)
        if column is None:
            continue
        qualifier = str(column.table).casefold()
        if qualifier in scaffold_aliases:
            existing_outputs.add(
                f"{scaffold_aliases[qualifier]}.{column.name}".casefold()
            )
    added_projections: list[dict[str, str]] = []
    for expression in proposal.expressions:
        column = _direct_projection_column(expression)
        if column is None:
            continue
        qualifier = str(column.table).casefold()
        if qualifier not in proposal_aliases:
            continue
        identifier = f"{proposal_aliases[qualifier]}.{column.name}".casefold()
        binding = output_bindings.get(identifier)
        table = str(proposal_aliases[qualifier]).casefold()
        target_alias = scaffold_alias_by_table.get(table)
        if binding is None or target_alias is None or identifier in existing_outputs:
            continue
        projected: exp.Expression = exp.column(str(column.name), table=target_alias)
        if isinstance(expression, exp.Alias) and expression.alias:
            projected = exp.alias_(projected, str(expression.alias))
        scaffold.append("expressions", projected)
        existing_outputs.add(identifier)
        added_projections.append({"physical_identifier": identifier, **binding})

    exact_bindings = [
        dict(value)
        for value in graph_evo_context.get("exact_literal_bindings") or []
        if isinstance(value, dict)
        and value.get("binding_status") == "unique_exact_current_value"
        and value.get("uses_evaluator_gold") is False
        and str(value.get("provenance_id") or "") in provenance_ids
    ]

    def binding_is_present(binding: dict[str, Any]) -> bool:
        where = scaffold.args.get("where")
        if not isinstance(where, exp.Where):
            return False
        for conjunct in _conjuncts(where.this):
            if not isinstance(conjunct, exp.EQ):
                continue
            left, right = conjunct.this, conjunct.expression
            if isinstance(left, exp.Literal) and isinstance(right, exp.Column):
                literal, column = left, right
            elif isinstance(left, exp.Column) and isinstance(right, exp.Literal):
                column, literal = left, right
            else:
                continue
            qualifier = str(column.table).casefold()
            if qualifier not in scaffold_aliases:
                continue
            identifier = f"{scaffold_aliases[qualifier]}.{column.name}".casefold()
            if identifier != str(binding.get("physical_identifier") or "").casefold():
                continue
            if _literal_values_equal(
                literal, binding.get("matched_value")
            ) or _literal_values_equal(literal, binding.get("literal")):
                return True
        return False

    added_predicates: list[dict[str, Any]] = []
    for binding in exact_bindings:
        if binding_is_present(binding):
            continue
        identifier = str(binding.get("physical_identifier") or "")
        table, separator, column = identifier.rpartition(".")
        target_alias = scaffold_alias_by_table.get(table.casefold())
        if not separator or not target_alias or not column:
            return {**result, "reason": "exact_literal_table_missing_from_scaffold"}
        matched_value = binding.get("matched_value")
        literal = (
            exp.Literal.number(str(matched_value))
            if isinstance(matched_value, (int, float))
            and not isinstance(matched_value, bool)
            else exp.Literal.string(str(matched_value))
        )
        predicate = exp.EQ(
            this=exp.column(column, table=target_alias),
            expression=literal,
        )
        where = scaffold.args.get("where")
        if isinstance(where, exp.Where):
            scaffold.set(
                "where",
                exp.Where(this=exp.and_(where.this.copy(), predicate)),
            )
        else:
            scaffold.set("where", exp.Where(this=predicate))
        added_predicates.append(
            {
                "physical_identifier": identifier.casefold(),
                "literal": binding.get("literal"),
                "matched_value": matched_value,
                "provenance_id": binding.get("provenance_id"),
            }
        )

    candidate_sql = scaffold.sql(dialect=dialect.casefold())
    if not _sql_covers_graph_exact_literals(
        candidate_sql, graph_evo_context, dialect
    ):
        return {**result, "reason": "candidate_scaffold_misses_exact_literal"}
    return {
        "candidate_sql": candidate_sql,
        "applied": True,
        "compiler": "graph_evo_unexecuted_candidate_scaffold_v1",
        "reason": "anchor_preserved_graph_extensions_compiled_for_execution",
        "added_projections": added_projections,
        "added_predicates": added_predicates,
        "relation_composition": {
            key: value for key, value in composition.items() if key != "sql"
        },
        "graph_edge_signatures": [
            list(value) for value in sorted(graph_signatures)
        ],
        "final_output_authorized": False,
        "requires_react_execution_and_m4_certificate": True,
        "uses_evaluator_gold": False,
    }


def _compile_graph_role_projection_completion(
    *,
    anchor_sql: str,
    proposal_sql: str,
    dialect: str,
    graph_evo_context: dict[str, Any] | None,
    proposal_execution: dict[str, Any] | None,
) -> dict[str, Any]:
    """Add only graph-bound output columns and their certified relation path.

    This is an AST operator, not a candidate selector.  The proposal must have
    been executed successfully by the fixed consumer, must have satisfied the
    question-only result-shape contract, and must retain every anchor projection
    in order.  All predicates, grouping, ordering, limits, and other clauses are
    byte-independent AST identities.  Additional projections must be direct
    columns bound to explicit ``output role:`` nodes in the exact Graph+Evo
    context, and the proposal relation tree must equal that context's strongly
    certified tree.
    """

    identity: dict[str, Any] = {
        "operator": "graph_certified_role_projection_completion",
        "applied": False,
        "reason": "role_projection_completion_not_applicable",
        "sql": anchor_sql,
        "uses_evaluator_gold": False,
    }
    if graph_evo_context is None:
        return {**identity, "reason": "missing_graph_evo_context"}
    if not proposal_execution:
        return {**identity, "reason": "missing_proposal_execution_certificate"}
    expected_execution_sha = _sha(proposal_sql.strip())
    if (
        proposal_execution.get("executable") is not True
        or proposal_execution.get("query_contract_satisfied") is not True
        or proposal_execution.get("gold_or_expected_answer_used") is not False
        or str(proposal_execution.get("proposal_sql_sha256") or "")
        != expected_execution_sha
    ):
        return {**identity, "reason": "proposal_execution_not_certified"}

    anchor = _simple_select(anchor_sql, dialect)
    proposal = _simple_select(proposal_sql, dialect)
    if anchor is None or proposal is None:
        return {**identity, "reason": "role_projection_requires_simple_selects"}
    anchor_sources = _sources(anchor)
    proposal_sources = _sources(proposal)
    if anchor_sources is None or proposal_sources is None:
        return {**identity, "reason": "role_projection_has_unsupported_sources"}
    anchor_order, anchor_aliases = anchor_sources
    proposal_order, proposal_aliases = proposal_sources
    anchor_tables = {table for table, _alias in anchor_order}
    proposal_tables = {table for table, _alias in proposal_order}
    if not anchor_tables.issubset(proposal_tables):
        return {**identity, "reason": "proposal_removes_anchor_table"}
    anchor_alias_by_table = {table: alias for table, alias in anchor_order}
    proposal_alias_by_table = {table: alias for table, alias in proposal_order}
    if any(
        anchor_alias_by_table[table] != proposal_alias_by_table[table]
        for table in anchor_tables
    ):
        return {**identity, "reason": "proposal_changes_anchor_table_alias"}

    anchor_expressions = list(anchor.expressions)
    proposal_expressions = list(proposal.expressions)
    if len(proposal_expressions) <= len(anchor_expressions):
        return {**identity, "reason": "proposal_adds_no_projection"}
    for anchor_expression, proposal_expression in zip(
        anchor_expressions, proposal_expressions, strict=False
    ):
        if _normalized_identifier_ast_sql(
            anchor_expression, dialect
        ) != _normalized_identifier_ast_sql(proposal_expression, dialect):
            return {**identity, "reason": "proposal_changes_anchor_projection"}

    anchor_shell = anchor.copy()
    anchor_shell.set("expressions", [])
    anchor_shell.set("from_", None)
    anchor_shell.set("joins", [])
    proposal_shell = proposal.copy()
    proposal_shell.set("expressions", [])
    proposal_shell.set("from_", None)
    proposal_shell.set("joins", [])
    if _normalized_identifier_ast_sql(
        anchor_shell, dialect
    ) != _normalized_identifier_ast_sql(proposal_shell, dialect):
        return {**identity, "reason": "proposal_changes_frozen_nonrelation_ast"}

    typed_edges = [
        dict(value)
        for value in graph_evo_context.get("typed_join_edges") or []
        if isinstance(value, dict)
    ]
    trusted_classes = {"declared", "history", "knowledge"}
    if any(
        edge.get("certified") is not True
        or edge.get("physical_join_columns_known") is not True
        or str(edge.get("evidence_class") or "").casefold()
        not in trusted_classes
        for edge in typed_edges
    ):
        return {**identity, "reason": "role_projection_graph_not_strongly_certified"}
    graph_signatures = _strong_query_edge_signatures(typed_edges)
    proposal_signatures = (
        _strict_inner_join_signatures(proposal, proposal_aliases) or set()
    )
    anchor_signatures = (
        _strict_inner_join_signatures(anchor, anchor_aliases) or set()
    )
    if anchor_signatures - proposal_signatures:
        return {**identity, "reason": "proposal_removes_anchor_relation"}
    if proposal_signatures != graph_signatures:
        return {
            **identity,
            "reason": "proposal_relation_tree_differs_from_graph",
            "proposal_edge_signatures": [
                list(value) for value in sorted(proposal_signatures)
            ],
            "graph_edge_signatures": [
                list(value) for value in sorted(graph_signatures)
            ],
        }
    if graph_signatures:
        graph_tables = {
            table
            for signature in graph_signatures
            for table in (signature[0], signature[2])
        }
        if (
            graph_tables != proposal_tables
            or len(proposal_tables) != len(graph_signatures) + 1
        ):
            return {**identity, "reason": "role_projection_graph_is_not_complete_tree"}
    elif len(proposal_tables) != 1:
        return {**identity, "reason": "role_projection_missing_relation_tree"}

    provenance_ids = {
        str(value) for value in graph_evo_context.get("provenance_ids") or []
    }
    output_bindings: dict[str, dict[str, str]] = {}
    for role, candidates in dict(
        graph_evo_context.get("physical_bindings") or {}
    ).items():
        if not str(role).casefold().startswith("output role:"):
            continue
        for candidate in candidates or []:
            physical_identifier = str(
                candidate.get("physical_identifier") or ""
            ).casefold()
            evidence_id = str(candidate.get("evidence_candidate_id") or "")
            if (
                physical_identifier
                and evidence_id
                and evidence_id in provenance_ids
                and str(candidate.get("semantic_alignment_status") or "")
                == "lexically_supported"
            ):
                output_bindings[physical_identifier] = {
                    "role": str(role),
                    "evidence_candidate_id": evidence_id,
                }

    additions: list[dict[str, str]] = []
    seen_physical: set[str] = set()
    for expression in proposal_expressions[len(anchor_expressions) :]:
        column = _direct_projection_column(expression)
        if column is None:
            return {**identity, "reason": "added_projection_is_not_direct_column"}
        qualifier = str(column.table).casefold()
        if not qualifier or qualifier not in proposal_aliases:
            return {**identity, "reason": "added_projection_is_not_physically_bound"}
        physical_identifier = (
            f"{proposal_aliases[qualifier]}.{column.name}".casefold()
        )
        if physical_identifier not in output_bindings:
            return {**identity, "reason": "added_projection_has_no_output_role_binding"}
        if physical_identifier in seen_physical:
            return {**identity, "reason": "duplicate_role_projection"}
        seen_physical.add(physical_identifier)
        additions.append(
            {
                "physical_identifier": physical_identifier,
                **output_bindings[physical_identifier],
            }
        )

    sql = proposal.sql(dialect=dialect.casefold())
    return {
        "operator": "graph_certified_role_projection_completion",
        "applied": True,
        "reason": "executed_proposal_completes_graph_bound_output_roles",
        "sql": sql,
        "added_projections": additions,
        "added_tables": sorted(proposal_tables - anchor_tables),
        "edge_signatures": [list(value) for value in sorted(graph_signatures)],
        "anchor_projection_count": len(anchor_expressions),
        "compiled_projection_count": len(proposal_expressions),
        "anchor_nonrelation_ast_frozen": True,
        "proposal_execution_sha256": expected_execution_sha,
        "uses_evaluator_gold": False,
    }


def _strict_inner_join_signatures(
    tree: exp.Select,
    aliases: dict[str, str],
) -> set[tuple[str, str, str, str]] | None:
    """Extract a pure inner equijoin tree with no hidden ON-clause predicates."""

    output: set[tuple[str, str, str, str]] = set()
    joins = list(tree.args.get("joins") or [])
    if not joins:
        return None
    for join in joins:
        if (
            str(join.args.get("side") or "").casefold()
            or str(join.args.get("kind") or "").casefold() not in {"", "inner"}
        ):
            return None
        on = join.args.get("on")
        if on is None:
            return None
        for conjunct in _conjuncts(on):
            if not isinstance(conjunct, exp.EQ):
                return None
            left, right = conjunct.this, conjunct.expression
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
            output.add(
                _edge_signature(
                    (
                        (
                            aliases[left_alias].casefold(),
                            str(left.name).casefold(),
                        ),
                        (
                            aliases[right_alias].casefold(),
                            str(right.name).casefold(),
                        ),
                    )
                )
            )
    return output or None


def _nonjoin_columns_are_bound(
    tree: exp.Select, aliases: dict[str, str]
) -> bool:
    """Reject relation-tree changes that alter unqualified-name resolution."""

    for column in tree.find_all(exp.Column):
        if _inside_join(column, tree):
            continue
        if str(column.name) == "*":
            qualifier = str(column.table).casefold()
            if qualifier and qualifier not in aliases:
                return False
            continue
        qualifier = str(column.table).casefold()
        if not qualifier or qualifier not in aliases:
            return False
    return True


def _compile_relation_tree_substitution(
    *,
    anchor_sql: str,
    proposal_sql: str,
    dialect: str,
    relationship_edges: list[dict[str, Any]] | None,
) -> dict[str, Any]:
    """Replace only FROM/JOIN when graph and proposal encode the same full tree.

    This operator is intentionally stricter than accepting a generated SQL query:
    the graph must provide a complete, strongly certified physical tree; the
    proposal must reproduce every graph edge and no other edge.  The final query
    is constructed from the anchor AST, so generated projection/filter/aggregate
    drift is ignored rather than copied; a postcondition verifies that grafting
    the relation tree did not alter any anchor non-relation node.
    """

    identity: dict[str, Any] = {
        "operator": "certified_relation_tree_substitution",
        "applied": False,
        "reason": "relation_tree_substitution_not_applicable",
        "sql": anchor_sql,
        "uses_evaluator_gold": False,
    }
    if not relationship_edges:
        return {**identity, "reason": "query_relationship_program_has_no_edges"}
    anchor = _simple_select(anchor_sql, dialect)
    proposal = _simple_select(proposal_sql, dialect)
    if anchor is None or proposal is None:
        return {**identity, "reason": "relation_tree_requires_simple_selects"}
    anchor_sources = _sources(anchor)
    proposal_sources = _sources(proposal)
    if anchor_sources is None or proposal_sources is None:
        return {**identity, "reason": "relation_tree_has_unsupported_sources"}
    anchor_order, anchor_aliases = anchor_sources
    proposal_order, proposal_aliases = proposal_sources
    anchor_tables = {table for table, _alias in anchor_order}
    proposal_tables = {table for table, _alias in proposal_order}
    if anchor_tables == proposal_tables:
        return {**identity, "reason": "relation_tree_table_program_unchanged"}

    trusted_classes = {"declared", "history", "knowledge"}
    if any(
        edge.get("certified") is not True
        or edge.get("physical_join_columns_known") is not True
        or str(edge.get("evidence_class") or "").casefold()
        not in trusted_classes
        for edge in relationship_edges
    ):
        return {**identity, "reason": "relation_tree_graph_not_strongly_certified"}
    graph_signatures = _provided_edge_signatures(relationship_edges)
    strong_signatures = _strong_query_edge_signatures(relationship_edges)
    graph_tables = {
        table
        for signature in graph_signatures
        for table in (signature[0], signature[2])
    }
    if (
        not graph_signatures
        or graph_signatures != strong_signatures
        or graph_tables != proposal_tables
        or len(proposal_order) != len(graph_signatures) + 1
    ):
        return {**identity, "reason": "relation_tree_graph_is_not_complete"}
    proposal_signatures = _strict_inner_join_signatures(
        proposal, proposal_aliases
    )
    if proposal_signatures != graph_signatures:
        return {
            **identity,
            "reason": "proposal_and_graph_relation_trees_disagree",
            "proposal_edge_signatures": [
                list(value) for value in sorted(proposal_signatures or set())
            ],
            "graph_edge_signatures": [
                list(value) for value in sorted(graph_signatures)
            ],
        }

    anchor_alias_by_table = {
        table: alias for table, alias in anchor_order
    }
    proposal_alias_by_table = {
        table: alias for table, alias in proposal_order
    }
    shared_tables = anchor_tables & proposal_tables
    if any(
        anchor_alias_by_table[table] != proposal_alias_by_table[table]
        for table in shared_tables
    ):
        return {**identity, "reason": "relation_tree_changes_shared_table_alias"}
    shared_aliases = set(anchor_aliases) & set(proposal_aliases)
    if any(
        anchor_aliases[alias].casefold()
        != proposal_aliases[alias].casefold()
        for alias in shared_aliases
    ):
        # A qualified frozen expression such as COUNT(r.old_key) would remain
        # syntactically bound after ``r`` was silently reassigned to a different
        # physical table, but could become invalid or change meaning.  Physical
        # alias identity is therefore part of the frozen non-relation contract;
        # cross-table rebinding needs an explicit lineage operator.
        return {**identity, "reason": "relation_tree_retargets_anchor_alias"}
    if not _nonjoin_columns_are_bound(anchor, proposal_aliases):
        return {**identity, "reason": "relation_tree_changes_column_resolution"}

    anchor_nonrelation = anchor.copy()
    anchor_nonrelation.set("from_", None)
    anchor_nonrelation.set("joins", [])

    compiled = anchor.copy()
    compiled.set("from_", proposal.args["from_"].copy())
    compiled.set(
        "joins", [join.copy() for join in proposal.args.get("joins") or []]
    )
    compiled_sources = _sources(compiled)
    if compiled_sources is None:
        return {**identity, "reason": "compiled_relation_tree_is_invalid"}
    compiled_signatures = _strict_inner_join_signatures(
        compiled, compiled_sources[1]
    )
    if compiled_signatures != graph_signatures:
        return {**identity, "reason": "compiled_relation_tree_validation_failed"}
    compiled_nonrelation = compiled.copy()
    compiled_nonrelation.set("from_", None)
    compiled_nonrelation.set("joins", [])
    if _normalized_identifier_ast_sql(
        compiled_nonrelation, dialect
    ) != _normalized_identifier_ast_sql(anchor_nonrelation, dialect):
        return {**identity, "reason": "compiled_nonrelation_ast_changed"}

    sql = compiled.sql(dialect=dialect.casefold())
    return {
        "operator": "certified_relation_tree_substitution",
        "applied": True,
        "reason": "proposal_and_query_graph_agree_on_complete_relation_tree",
        "sql": sql,
        "removed_tables": sorted(anchor_tables - proposal_tables),
        "added_tables": sorted(proposal_tables - anchor_tables),
        "shared_tables": sorted(shared_tables),
        "edge_signatures": [list(value) for value in sorted(graph_signatures)],
        "external_projection_frozen": True,
        "nonrelation_ast_frozen": True,
        "proposal_nonrelation_ignored": True,
        "uses_evaluator_gold": False,
    }


def _table_pair(
    signature: tuple[str, str, str, str],
) -> tuple[str, str]:
    return tuple(sorted((signature[0], signature[2])))


def _inside_join(node: exp.Expression, root: exp.Select) -> bool:
    parent = node.parent
    while parent is not None and parent is not root:
        if isinstance(parent, exp.Join):
            return True
        parent = parent.parent
    return False


def _sqlite_probe(database: Path, sql: str, timeout_seconds: float) -> bool:
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


def _compile_redundant_parent_lookup(
    *,
    sql: str,
    database: Path,
    database_id: str,
    dialect: str,
    timeout_seconds: float,
) -> dict[str, Any]:
    """Eliminate a two-table FK parent used only through the equality key.

    The operator substitutes the child FK for the equal parent key, adds an
    explicit non-null predicate, and requires a database-local no-orphan probe.
    It therefore preserves the inner join's row semantics without relying on an
    evaluator answer.
    """

    identity: dict[str, Any] = {
        "operator": "certified_redundant_parent_lookup",
        "applied": False,
        "reason": "lookup_elimination_not_applicable",
        "sql": sql,
        "uses_evaluator_gold": False,
    }
    tree = _simple_select(sql, dialect)
    if tree is None:
        return {**identity, "reason": "lookup_requires_simple_select"}
    source_info = _sources(tree)
    joins = list(tree.args.get("joins") or [])
    if source_info is None or len(joins) != 1:
        return {**identity, "reason": "lookup_requires_two_tables"}
    ordered, aliases = source_info
    join = joins[0]
    if (
        str(join.args.get("side") or "").casefold()
        or str(join.args.get("kind") or "").casefold() not in {"", "inner"}
    ):
        return {**identity, "reason": "lookup_requires_inner_join"}
    on = join.args.get("on")
    if not isinstance(on, exp.EQ):
        return {**identity, "reason": "lookup_requires_single_equality"}
    left, right = on.this, on.expression
    if not isinstance(left, exp.Column) or not isinstance(right, exp.Column):
        return {**identity, "reason": "lookup_requires_column_equality"}
    left_alias = str(left.table).casefold()
    right_alias = str(right.table).casefold()
    if left_alias not in aliases or right_alias not in aliases:
        return {**identity, "reason": "lookup_has_unresolved_alias"}
    endpoints = {
        (aliases[left_alias].casefold(), str(left.name).casefold()): (
            left_alias,
            str(left.name),
        ),
        (aliases[right_alias].casefold(), str(right.name).casefold()): (
            right_alias,
            str(right.name),
        ),
    }
    if len(endpoints) != 2:
        return {**identity, "reason": "lookup_self_join_unsupported"}

    catalog = inspect_sqlite_relationship_catalog(
        database,
        database_id=database_id,
    )
    declared_directions: set[
        tuple[tuple[str, str], tuple[str, str]]
    ] = set()
    for edge in catalog.edges:
        if "declared_foreign_key" not in set(edge.get("evidence_types") or []):
            continue
        try:
            child_table, child_column = str(edge["left"]).rsplit(".", 1)
            parent_table, parent_column = str(edge["right"]).rsplit(".", 1)
        except (KeyError, ValueError):
            continue
        declared_directions.add(
            (
                (child_table.casefold(), child_column.casefold()),
                (parent_table.casefold(), parent_column.casefold()),
            )
        )
    direction = next(
        (
            value
            for value in declared_directions
            if value[0] in endpoints and value[1] in endpoints
        ),
        None,
    )
    if direction is None:
        return {**identity, "reason": "lookup_edge_not_declared_fk"}
    kept_key, removed_key = direction
    removed_table, removed_column_cf = removed_key
    kept_table, kept_column_cf = kept_key
    normalized_unique_columns = {
        table.casefold(): {column.casefold() for column in columns}
        for table, columns in catalog.unique_columns.items()
    }
    if removed_column_cf not in normalized_unique_columns.get(removed_table, set()):
        return {**identity, "reason": "lookup_parent_key_not_unique"}
    kept_alias, kept_column = endpoints[kept_key]
    removed_alias, _removed_column = endpoints[removed_key]

    referenced_removed: list[exp.Column] = []
    for column in tree.find_all(exp.Column):
        if _inside_join(column, tree):
            continue
        qualifier = str(column.table).casefold()
        if not qualifier:
            return {**identity, "reason": "lookup_has_unqualified_column"}
        if qualifier != removed_alias:
            continue
        if str(column.name).casefold() != removed_column_cf:
            return {**identity, "reason": "lookup_parent_has_nonkey_semantics"}
        referenced_removed.append(column)
    # A parent that contributes no clause at all is commonly an intentional
    # existence constraint.  Require an explicit equal-key use to keep the
    # transformation semantically observable and conservative.
    if not referenced_removed:
        return {**identity, "reason": "lookup_parent_key_not_referenced"}

    original_tables = {
        table.name.casefold(): table for table in tree.find_all(exp.Table)
    }
    kept_node = original_tables.get(kept_table)
    if kept_node is None:
        return {**identity, "reason": "lookup_kept_source_missing"}
    compiled = tree.copy()
    for column in list(compiled.find_all(exp.Column)):
        if _inside_join(column, compiled):
            continue
        if str(column.table).casefold() == removed_alias:
            column.set("table", exp.to_identifier(kept_alias))
            column.set("this", exp.to_identifier(kept_column))
    compiled.set("from_", exp.From(this=kept_node.copy()))
    compiled.set("joins", [])
    nonnull = exp.Not(
        this=exp.Is(
            this=exp.column(kept_column, table=kept_alias),
            expression=exp.Null(),
        )
    )
    existing_where = compiled.args.get("where")
    if existing_where is None:
        compiled.set("where", exp.Where(this=nonnull))
    else:
        compiled.set(
            "where",
            exp.Where(this=exp.and_(existing_where.this.copy(), nonnull)),
        )

    child_table_sql = '"' + kept_table.replace('"', '""') + '"'
    parent_table_sql = '"' + removed_table.replace('"', '""') + '"'
    child_column_sql = '"' + kept_column.replace('"', '""') + '"'
    parent_column = endpoints[removed_key][1]
    parent_column_sql = '"' + parent_column.replace('"', '""') + '"'
    orphan_probe = (
        f"SELECT 1 FROM {child_table_sql} AS child LEFT JOIN {parent_table_sql} "
        f"AS parent ON child.{child_column_sql}=parent.{parent_column_sql} "
        f"WHERE child.{child_column_sql} IS NOT NULL "
        f"AND parent.{parent_column_sql} IS NULL LIMIT 1"
    )
    connection = sqlite3.connect(f"file:{database.resolve()}?mode=ro", uri=True)
    deadline = time.monotonic() + timeout_seconds
    connection.set_progress_handler(
        lambda: int(time.monotonic() > deadline), 1000
    )
    try:
        orphan = connection.execute(orphan_probe).fetchone()
    except Exception:
        return {**identity, "reason": "lookup_orphan_probe_failed"}
    finally:
        connection.close()
    if orphan is not None:
        return {**identity, "reason": "lookup_fk_has_observed_orphan"}
    compiled_sql = compiled.sql(dialect=dialect.casefold())
    if not _sqlite_probe(database, compiled_sql, timeout_seconds):
        return {**identity, "reason": "lookup_compilation_not_executable"}
    return {
        "operator": "certified_redundant_parent_lookup",
        "applied": True,
        "reason": "declared_fk_unique_parent_no_orphans_key_substitution",
        "sql": compiled_sql,
        "kept_child": f"{kept_table}.{kept_column}",
        "eliminated_parent": f"{removed_table}.{parent_column}",
        "rewritten_key_references": len(referenced_removed),
        "uses_evaluator_gold": False,
    }


def _outer_to_inner_from_proposal(
    *,
    anchor_sql: str,
    proposal_sql: str,
    database: Path,
    database_id: str,
    dialect: str,
    table_old_to_new: dict[str, str] | None,
    column_old_to_new: dict[str, dict[str, str]] | None,
    relationship_edges: list[dict[str, Any]] | None,
) -> dict[str, Any]:
    """Apply only outer-to-inner changes over an otherwise identical join graph."""

    identity: dict[str, Any] = {
        "operator": "proposal_directed_join_modality",
        "applied": False,
        "reason": "proposal_not_applicable",
        "sql": anchor_sql,
        "uses_evaluator_gold": False,
    }
    # This operator touches only the top-level JOIN modalities.  CTEs and nested
    # SELECTs remain byte-for-byte represented by the anchor AST and therefore do
    # not make an otherwise typed top-level relation program unsupported.
    anchor = _top_level_select(anchor_sql, dialect)
    proposal = _top_level_select(proposal_sql, dialect)
    if anchor is None or proposal is None:
        return {**identity, "reason": "proposal_or_anchor_not_simple_select"}
    anchor_sources = _sources(anchor)
    proposal_sources = _sources(proposal)
    if anchor_sources is None or proposal_sources is None:
        return {**identity, "reason": "unsupported_sources"}
    anchor_order, anchor_aliases = anchor_sources
    proposal_order, proposal_aliases = proposal_sources
    if [table for table, _ in anchor_order] != [table for table, _ in proposal_order]:
        return {**identity, "reason": "proposal_changes_table_program"}
    anchor_joins = list(anchor.args.get("joins") or [])
    proposal_joins = list(proposal.args.get("joins") or [])
    if len(anchor_joins) != len(proposal_joins):
        return {**identity, "reason": "proposal_changes_join_count"}
    anchor_conditions = [
        _join_condition_fingerprint(join, anchor_aliases, dialect)
        for join in anchor_joins
    ]
    proposal_conditions = [
        _join_condition_fingerprint(join, proposal_aliases, dialect)
        for join in proposal_joins
    ]
    if anchor_conditions != proposal_conditions:
        return {**identity, "reason": "proposal_changes_join_edges"}
    changed_indices: list[int] = []
    changed_tables: list[str] = []
    changed_edges: set[tuple[str, str, str, str]] = set()
    for index, (old_join, proposed_join) in enumerate(
        zip(anchor_joins, proposal_joins, strict=True)
    ):
        old_side = str(old_join.args.get("side") or "").casefold()
        old_kind = str(old_join.args.get("kind") or "").casefold()
        proposed_side = str(proposed_join.args.get("side") or "").casefold()
        proposed_kind = str(proposed_join.args.get("kind") or "").casefold()
        old_inner = old_side == "" and old_kind in {"", "inner"}
        proposed_inner = proposed_side == "" and proposed_kind in {"", "inner"}
        if (old_side, old_kind) == (proposed_side, proposed_kind):
            continue
        if old_inner or not proposed_inner or old_side not in {"left", "right", "full"}:
            return {**identity, "reason": "proposal_contains_unsupported_modality_change"}
        local_edges = _join_edge_signatures(old_join, anchor_aliases)
        if not local_edges:
            return {**identity, "reason": "changed_join_has_no_physical_equality_edge"}
        changed_indices.append(index)
        changed_tables.append(anchor_order[index + 1][0])
        changed_edges.update(local_edges)
    if not changed_indices:
        return {**identity, "reason": "join_modality_unchanged"}

    if relationship_edges is not None:
        certified = _provided_edge_signatures(relationship_edges)
        certificate_source = "query_relationship_program"
    elif dialect.casefold() == "sqlite":
        certified = _catalog_edge_signatures(
            database,
            database_id=database_id,
            tables=[table for table, _ in anchor_order],
            table_old_to_new=table_old_to_new,
            column_old_to_new=column_old_to_new,
        )
        certificate_source = "sqlite_relationship_catalog"
    else:
        # A non-SQLite adapter must pass its own relationship program.  Never
        # reinterpret a placeholder filesystem path as a SQLite catalog.
        certified = set()
        certificate_source = "missing_backend_relationship_program"
    # Unchanged joins are part of the frozen anchor and do not need to be
    # re-certified.  Requiring the entire pre-existing tree here incorrectly
    # suppressed a locally proven modality edit whenever an unrelated legacy
    # edge lacked ontology evidence.
    if not changed_edges <= certified:
        return {
            **identity,
            "reason": "changed_join_edges_not_relationship_certified",
            "edge_signatures": [list(value) for value in sorted(changed_edges)],
            "relationship_certificate_source": certificate_source,
        }

    compiled = anchor.copy()
    compiled_joins = list(compiled.args.get("joins") or [])
    for index in changed_indices:
        compiled_joins[index].set("side", None)
        compiled_joins[index].set("kind", "INNER")
    compiled.set("joins", compiled_joins)
    sql = compiled.sql(dialect=dialect.casefold())
    return {
        "operator": "proposal_directed_join_modality",
        "applied": True,
        "reason": "certified_outer_to_inner_refinement",
        "sql": sql,
        "refined_tables": changed_tables,
        "edge_signatures": [list(value) for value in sorted(changed_edges)],
        "relationship_certificate_source": certificate_source,
        "uses_evaluator_gold": False,
    }


def _compile_relation_key_substitution(
    *,
    anchor_sql: str,
    proposal_sql: str,
    dialect: str,
    relationship_edges: list[dict[str, Any]] | None,
) -> dict[str, Any]:
    """Propagate a query-graph-selected replacement key through the anchor.

    The replacement must be both strongly certified by the query relationship
    program and restated by the proposal.  It must additionally participate in
    a frozen, non-join anchor clause (for example, a predicate or grouping key).
    That third structural witness matters because the proposal is generated from
    the same retrieved graph and is therefore not statistically independent of
    it: graph/proposal agreement alone can merely repeat one noisy edge.  No
    proposal predicate, projection, table, or modality is copied.
    """

    identity: dict[str, Any] = {
        "operator": "certified_relation_key_substitution",
        "applied": False,
        "reason": "relation_key_substitution_not_applicable",
        "sql": anchor_sql,
        "uses_evaluator_gold": False,
    }
    if relationship_edges is None:
        return {**identity, "reason": "query_relationship_program_not_provided"}
    certified = _strong_query_edge_signatures(relationship_edges)
    if not certified:
        return {
            **identity,
            "reason": "query_relationship_program_has_no_strong_edges",
        }
    anchor = _simple_select(anchor_sql, dialect)
    if anchor is None:
        return {**identity, "reason": "key_substitution_requires_simple_anchor"}
    anchor_sources = _sources(anchor)
    if anchor_sources is None:
        return {**identity, "reason": "key_substitution_has_unsupported_anchor_sources"}
    _anchor_order, anchor_aliases = anchor_sources
    anchor_joins = list(anchor.args.get("joins") or [])

    graph_by_table_pair: dict[
        tuple[str, str], set[tuple[str, str, str, str]]
    ] = {}
    for signature in certified:
        graph_by_table_pair.setdefault(_table_pair(signature), set()).add(signature)
    proposal_by_table_pair: dict[
        tuple[str, str], list[
            tuple[tuple[str, str, str, str], tuple[str, str]]
        ]
    ] = {}
    proposal = _simple_select(proposal_sql, dialect)
    if proposal is not None:
        proposal_sources = _sources(proposal)
        if proposal_sources is not None:
            _proposal_order, proposal_aliases = proposal_sources
            for proposal_join in proposal.args.get("joins") or []:
                pairs = _join_endpoint_pairs(proposal_join, proposal_aliases)
                if pairs is None or len(pairs) != 1:
                    continue
                signature = _edge_signature(pairs[0])
                modality = (
                    str(proposal_join.args.get("side") or "").casefold(),
                    str(proposal_join.args.get("kind") or "").casefold(),
                )
                proposal_by_table_pair.setdefault(
                    _table_pair(signature), []
                ).append((signature, modality))

    replacements: dict[tuple[str, str], str] = {}
    changed_edges: list[dict[str, Any]] = []
    ignored_proposal_modality_changes = 0
    proposal_disagreement = False
    for anchor_join in anchor_joins:
        anchor_modality = (
            str(anchor_join.args.get("side") or "").casefold(),
            str(anchor_join.args.get("kind") or "").casefold(),
        )
        anchor_pairs = _join_endpoint_pairs(anchor_join, anchor_aliases)
        if anchor_pairs is None or len(anchor_pairs) != 1:
            continue
        anchor_pair = anchor_pairs[0]
        anchor_signature = _edge_signature(anchor_pair)
        candidates = graph_by_table_pair.get(_table_pair(anchor_signature), set())
        if len(candidates) > 1:
            return {
                **identity,
                "reason": "relation_key_is_ambiguous_in_query_program",
                "anchor_edge_signature": list(anchor_signature),
                "candidate_edge_signatures": [
                    list(value) for value in sorted(candidates)
                ],
            }
        if not candidates:
            continue
        replacement_signature = next(iter(candidates))
        if anchor_signature == replacement_signature:
            continue

        proposal_matches = [
            modality
            for signature, modality in proposal_by_table_pair.get(
                _table_pair(anchor_signature), []
            )
            if signature == replacement_signature
        ]
        proposal_agrees = bool(proposal_matches)
        if not proposal_agrees:
            proposal_disagreement = True
            continue
        ignored_proposal_modality_changes += sum(
            modality != anchor_modality for modality in proposal_matches
        )

        anchor_by_table = {table: column for table, column in anchor_pair}
        replacement_by_table = {
            replacement_signature[0]: replacement_signature[1],
            replacement_signature[2]: replacement_signature[3],
        }
        if set(anchor_by_table) != set(replacement_by_table):
            return {**identity, "reason": "query_graph_changes_joined_tables"}
        local_replacements: dict[tuple[str, str], str] = {}
        for table in sorted(anchor_by_table):
            old_column = anchor_by_table[table]
            new_column = replacement_by_table[table]
            if old_column != new_column:
                local_replacements[(table, old_column)] = new_column
        if not local_replacements:
            return {**identity, "reason": "relation_key_has_no_column_substitution"}
        for key, value in local_replacements.items():
            previous = replacements.get(key)
            if previous is not None and previous != value:
                return {**identity, "reason": "relation_key_substitution_is_ambiguous"}
            replacements[key] = value
        changed_edges.append(
            {
                "anchor": list(anchor_signature),
                "replacement": list(replacement_signature),
                "proposal_agrees": proposal_agrees,
            }
        )
    if not replacements:
        return {
            **identity,
            "reason": (
                "proposal_does_not_confirm_relation_key"
                if proposal_disagreement
                else "relation_keys_unchanged"
            ),
        }

    # Keep the externally visible output binding frozen.  The current operator
    # supports relation keys used by JOIN/predicate/group/order logic; a projected
    # physical key needs a separate, explicit output-lineage certificate.
    for expression in anchor.expressions:
        for column in expression.find_all(exp.Column):
            qualifier = str(column.table).casefold()
            if qualifier not in anchor_aliases:
                if any(
                    old_column == str(column.name).casefold()
                    for _table, old_column in replacements
                ):
                    return {
                        **identity,
                        "reason": "projected_relation_key_is_unqualified",
                    }
                continue
            key = (
                anchor_aliases[qualifier].casefold(),
                str(column.name).casefold(),
            )
            if key in replacements:
                return {**identity, "reason": "projected_relation_key_requires_lineage"}

    # A proposal is conditioned on the retrieved relation graph, so agreement
    # between those two representations is not an independent certificate.  A
    # bare JOIN-key swap can therefore replace a correct anchor edge with a
    # plausible but semantically different historical key.  Require at least one
    # occurrence of the old key in a *frozen non-join clause* of the anchor.  The
    # compiler then propagates a key already tied to query semantics (WHERE,
    # GROUP BY, HAVING, ORDER BY, QUALIFY, etc.) instead of authoring an isolated
    # relation edge.  Evolution-only key changes remain handled by the explicit
    # lineage operator below.
    frozen_nonjoin_occurrences = 0
    for argument_name, argument in anchor.args.items():
        if argument_name in {"expressions", "from_", "joins", "with_"}:
            continue
        values = argument if isinstance(argument, list) else [argument]
        for value in values:
            if not isinstance(value, exp.Expression):
                continue
            columns = (
                [value]
                if isinstance(value, exp.Column)
                else list(value.find_all(exp.Column))
            )
            for column in columns:
                qualifier = str(column.table).casefold()
                if qualifier not in anchor_aliases:
                    continue
                key = (
                    anchor_aliases[qualifier].casefold(),
                    str(column.name).casefold(),
                )
                frozen_nonjoin_occurrences += int(key in replacements)
    if frozen_nonjoin_occurrences == 0:
        return {
            **identity,
            "reason": "replacement_key_lacks_frozen_nonjoin_dependency",
            "changed_edges": changed_edges,
        }

    compiled = anchor.copy()
    rewritten_occurrences = 0
    for column in compiled.find_all(exp.Column):
        qualifier = str(column.table).casefold()
        if qualifier not in anchor_aliases:
            continue
        key = (
            anchor_aliases[qualifier].casefold(),
            str(column.name).casefold(),
        )
        replacement = replacements.get(key)
        if replacement is None:
            continue
        column.set("this", exp.to_identifier(replacement))
        rewritten_occurrences += 1
    if rewritten_occurrences == 0:
        return {**identity, "reason": "relation_key_occurrence_not_found"}

    compiled_joins = list(compiled.args.get("joins") or [])
    compiled_signatures = {
        _edge_signature(pair)
        for join in compiled_joins
        for pair in (_join_endpoint_pairs(join, anchor_aliases) or [])
    }
    required_signatures = {
        tuple(edge["replacement"]) for edge in changed_edges
    }
    if not required_signatures <= compiled_signatures:
        return {**identity, "reason": "relation_key_substitution_validation_failed"}
    anchor_signatures = {
        _edge_signature(pair)
        for join in anchor_joins
        for pair in (_join_endpoint_pairs(join, anchor_aliases) or [])
    }
    unapproved_new_signatures = (
        compiled_signatures - anchor_signatures - certified
    )
    if unapproved_new_signatures:
        return {
            **identity,
            "reason": "relation_key_substitution_changes_uncertified_edge",
            "unapproved_edge_signatures": [
                list(value) for value in sorted(unapproved_new_signatures)
            ],
        }
    sql = compiled.sql(dialect=dialect.casefold())
    return {
        "operator": "certified_relation_key_substitution",
        "applied": True,
        "reason": "proposal_and_query_graph_agree_on_replacement_key",
        "sql": sql,
        "replacements": [
            {
                "table": table,
                "old_column": old_column,
                "new_column": new_column,
            }
            for (table, old_column), new_column in sorted(replacements.items())
        ],
        "changed_edges": changed_edges,
        "rewritten_occurrences": rewritten_occurrences,
        "frozen_nonjoin_occurrences": frozen_nonjoin_occurrences,
        "ignored_proposal_modality_changes": (
            ignored_proposal_modality_changes
        ),
        "proposal_agrees_with_all_replacements": True,
        "relationship_certificate_source": "query_relationship_program",
        "uses_evaluator_gold": False,
    }


def _cte_definitions(tree: exp.Select) -> dict[str, exp.Select] | None:
    with_clause = tree.args.get("with_")
    if with_clause is None:
        return None
    definitions: dict[str, exp.Select] = {}
    for cte in with_clause.expressions:
        if not isinstance(cte, exp.CTE) or not isinstance(cte.this, exp.Select):
            return None
        name = str(cte.alias_or_name).casefold()
        if not name or name in definitions:
            return None
        definitions[name] = cte.this
    return definitions or None


def _compile_cte_relation_key_substitution(
    *,
    anchor_sql: str,
    proposal_sql: str,
    dialect: str,
    relationship_edges: list[dict[str, Any]] | None,
) -> dict[str, Any]:
    """Apply the typed relation-key operator inside matching named CTEs.

    The top-level relation-key operator deliberately accepts only a single
    SELECT scope.  Treating every WITH query as an indivisible unsupported AST
    therefore discarded otherwise local, graph-certified key repairs.  This
    operator pairs CTEs by their declared name and invokes the same conservative
    compiler independently inside each simple SELECT definition.  It never
    copies a proposal expression: the returned query is the anchor tree with
    only certified physical key occurrences rewritten inside those scopes.
    """

    identity: dict[str, Any] = {
        "operator": "graph_certified_cte_relation_key_substitution",
        "applied": False,
        "reason": "cte_relation_key_substitution_not_applicable",
        "sql": anchor_sql,
        "uses_evaluator_gold": False,
    }
    if relationship_edges is None:
        return {**identity, "reason": "query_relationship_program_not_provided"}
    anchor = _top_level_select(anchor_sql, dialect)
    proposal = _top_level_select(proposal_sql, dialect)
    if anchor is None or proposal is None:
        return {**identity, "reason": "cte_key_substitution_requires_top_level_select"}
    anchor_ctes = _cte_definitions(anchor)
    proposal_ctes = _cte_definitions(proposal)
    if anchor_ctes is None or proposal_ctes is None:
        return {**identity, "reason": "cte_key_substitution_requires_ctes"}
    if set(anchor_ctes) != set(proposal_ctes):
        return {**identity, "reason": "proposal_changes_cte_program"}

    compiled = anchor.copy()
    compiled_ctes = _cte_definitions(compiled)
    assert compiled_ctes is not None
    scope_certificates: list[dict[str, Any]] = []
    transformations: list[dict[str, Any]] = []
    for cte_name in anchor_ctes:
        result = _compile_relation_key_substitution(
            anchor_sql=anchor_ctes[cte_name].sql(dialect=dialect.casefold()),
            proposal_sql=proposal_ctes[cte_name].sql(dialect=dialect.casefold()),
            dialect=dialect,
            relationship_edges=relationship_edges,
        )
        scope_sql = str(result.pop("sql"))
        scope_certificates.append({"cte": cte_name, **result})
        if not result["applied"]:
            continue
        replacement = _simple_select(scope_sql, dialect)
        if replacement is None:
            return {
                **identity,
                "reason": "compiled_cte_key_substitution_is_invalid",
                "scope_certificates": scope_certificates,
            }
        compiled_ctes[cte_name].replace(replacement)
        transformations.append(
            {
                "cte": cte_name,
                "reason": result["reason"],
                "replacements": result["replacements"],
                "changed_edges": result["changed_edges"],
                "rewritten_occurrences": result["rewritten_occurrences"],
                "frozen_nonjoin_occurrences": result[
                    "frozen_nonjoin_occurrences"
                ],
                "ignored_proposal_modality_changes": result[
                    "ignored_proposal_modality_changes"
                ],
            }
        )
    if not transformations:
        return {
            **identity,
            "reason": "no_certified_cte_relation_key_substitution",
            "scope_certificates": scope_certificates,
        }

    # Only WITH definitions may differ.  This is redundant with construction,
    # but makes the frozen outer query contract an explicit checked invariant.
    anchor_outer = anchor.copy()
    anchor_outer.set("with_", None)
    compiled_outer = compiled.copy()
    compiled_outer.set("with_", None)
    if _normalized_identifier_ast_sql(
        anchor_outer, dialect
    ) != _normalized_identifier_ast_sql(compiled_outer, dialect):
        return {
            **identity,
            "reason": "cte_key_substitution_changes_outer_query",
            "scope_certificates": scope_certificates,
        }

    return {
        "operator": "graph_certified_cte_relation_key_substitution",
        "applied": True,
        "reason": "named_cte_scopes_contain_certified_relation_key_substitutions",
        "sql": compiled.sql(dialect=dialect.casefold()),
        "cte_transformations": transformations,
        "scope_certificates": scope_certificates,
        "external_projection_frozen": True,
        "outer_query_contract_frozen": True,
        "uses_evaluator_gold": False,
    }


def _direct_cte_projection_lineage(
    cte: exp.Select,
    projected_name: str,
) -> tuple[str, str] | None:
    """Resolve one CTE output to a direct physical table-column reference."""

    matches = [
        expression
        for expression in cte.expressions
        if str(expression.alias_or_name).casefold() == projected_name.casefold()
    ]
    if len(matches) != 1:
        return None
    expression = matches[0]
    value = expression.this if isinstance(expression, exp.Alias) else expression
    if not isinstance(value, exp.Column) or value.is_star:
        return None
    source_info = _sources(cte)
    if source_info is None:
        return None
    _ordered, aliases = source_info
    qualifier = str(value.table).casefold()
    if qualifier not in aliases:
        return None
    return aliases[qualifier].casefold(), str(value.name).casefold()


def _top_level_projects_wildcard(tree: exp.Select) -> bool:
    for expression in tree.expressions:
        value = expression.this if isinstance(expression, exp.Alias) else expression
        if isinstance(value, exp.Star):
            return True
        if isinstance(value, exp.Column) and value.is_star:
            return True
    return False


def _compile_cte_relation_key_exposure(
    *,
    anchor_sql: str,
    proposal_sql: str,
    dialect: str,
    relationship_edges: list[dict[str, Any]] | None,
) -> dict[str, Any]:
    """Expose one hidden CTE key solely to repair an outer relation edge.

    The proposal is used as a typed relation-intent witness, not as replacement
    SQL.  The only accepted proposal delta is one direct physical column added
    to a CTE projection plus one top-level equality endpoint changed to that
    hidden output.  The resulting physical edge must be the unique strong edge
    for its table pair in the query relationship program.  External projection
    shape and every non-relation clause remain frozen.
    """

    identity: dict[str, Any] = {
        "operator": "graph_certified_cte_relation_key_exposure",
        "applied": False,
        "reason": "cte_relation_key_exposure_not_applicable",
        "sql": anchor_sql,
        "uses_evaluator_gold": False,
    }
    if relationship_edges is None:
        return {**identity, "reason": "query_relationship_program_not_provided"}
    anchor = _top_level_select(anchor_sql, dialect)
    proposal = _top_level_select(proposal_sql, dialect)
    if anchor is None or proposal is None:
        return {**identity, "reason": "cte_exposure_requires_top_level_select"}
    anchor_ctes = _cte_definitions(anchor)
    proposal_ctes = _cte_definitions(proposal)
    if anchor_ctes is None or proposal_ctes is None:
        return {**identity, "reason": "cte_exposure_requires_ctes"}
    if set(anchor_ctes) != set(proposal_ctes):
        return {**identity, "reason": "proposal_changes_cte_program"}
    if _top_level_projects_wildcard(anchor):
        return {**identity, "reason": "cte_exposure_would_leak_through_wildcard"}

    anchor_sources = _sources(anchor)
    proposal_sources = _sources(proposal)
    if anchor_sources is None or proposal_sources is None:
        return {**identity, "reason": "cte_exposure_has_unsupported_sources"}
    anchor_order, anchor_aliases = anchor_sources
    proposal_order, proposal_aliases = proposal_sources
    if anchor_order != proposal_order:
        return {**identity, "reason": "proposal_changes_top_level_cte_sources"}
    if any(table not in anchor_ctes for table, _alias in anchor_order):
        return {**identity, "reason": "top_level_source_is_not_local_cte"}

    anchor_joins = list(anchor.args.get("joins") or [])
    proposal_joins = list(proposal.args.get("joins") or [])
    if len(anchor_joins) != len(proposal_joins):
        return {**identity, "reason": "proposal_changes_join_count"}
    changed_join_indices: list[int] = []
    for index, (anchor_join, proposal_join) in enumerate(
        zip(anchor_joins, proposal_joins, strict=True)
    ):
        anchor_on = anchor_join.args.get("on")
        proposal_on = proposal_join.args.get("on")
        anchor_on_sql = anchor_on.sql(dialect=dialect.casefold()) if anchor_on else ""
        proposal_on_sql = (
            proposal_on.sql(dialect=dialect.casefold()) if proposal_on else ""
        )
        if anchor_on_sql != proposal_on_sql:
            changed_join_indices.append(index)
    if len(changed_join_indices) != 1:
        return {**identity, "reason": "cte_exposure_requires_one_changed_join"}
    join_index = changed_join_indices[0]
    anchor_join = anchor_joins[join_index]
    proposal_join = proposal_joins[join_index]
    anchor_modality = (
        str(anchor_join.args.get("side") or "").casefold(),
        str(anchor_join.args.get("kind") or "").casefold(),
    )
    proposal_modality = (
        str(proposal_join.args.get("side") or "").casefold(),
        str(proposal_join.args.get("kind") or "").casefold(),
    )
    if anchor_modality != proposal_modality:
        return {**identity, "reason": "proposal_changes_cte_join_modality"}
    anchor_pairs = _join_endpoint_pairs(anchor_join, anchor_aliases)
    proposal_pairs = _join_endpoint_pairs(proposal_join, proposal_aliases)
    if anchor_pairs is None or proposal_pairs is None:
        return {**identity, "reason": "cte_exposure_requires_column_equality"}
    if len(anchor_pairs) != 1 or len(proposal_pairs) != 1:
        return {**identity, "reason": "cte_exposure_requires_single_equality"}
    anchor_by_cte = dict(anchor_pairs[0])
    proposal_by_cte = dict(proposal_pairs[0])
    if set(anchor_by_cte) != set(proposal_by_cte):
        return {**identity, "reason": "proposal_changes_joined_ctes"}
    changed_ctes = [
        cte
        for cte in anchor_by_cte
        if anchor_by_cte[cte] != proposal_by_cte[cte]
    ]
    if len(changed_ctes) != 1:
        return {**identity, "reason": "cte_exposure_requires_one_changed_endpoint"}
    changed_cte = changed_ctes[0]
    stable_cte = next(cte for cte in anchor_by_cte if cte != changed_cte)
    old_output = anchor_by_cte[changed_cte]
    new_output = proposal_by_cte[changed_cte]
    if _direct_cte_projection_lineage(anchor_ctes[changed_cte], new_output):
        return {**identity, "reason": "replacement_key_already_exposed_by_anchor"}

    anchor_projection_sql = [
        expression.sql(dialect=dialect.casefold())
        for expression in anchor_ctes[changed_cte].expressions
    ]
    proposal_projection_sql = [
        expression.sql(dialect=dialect.casefold())
        for expression in proposal_ctes[changed_cte].expressions
    ]
    removable_indices: list[int] = []
    for index, expression in enumerate(proposal_ctes[changed_cte].expressions):
        if str(expression.alias_or_name).casefold() != new_output:
            continue
        reduced = proposal_projection_sql[:index] + proposal_projection_sql[index + 1 :]
        if reduced == anchor_projection_sql:
            removable_indices.append(index)
    if len(removable_indices) != 1:
        return {**identity, "reason": "proposal_does_not_add_exactly_one_cte_key"}
    added_index = removable_indices[0]
    added_projection = proposal_ctes[changed_cte].expressions[added_index]

    stable_lineage = _direct_cte_projection_lineage(
        anchor_ctes[stable_cte], anchor_by_cte[stable_cte]
    )
    replacement_lineage = _direct_cte_projection_lineage(
        proposal_ctes[changed_cte], new_output
    )
    if stable_lineage is None or replacement_lineage is None:
        return {**identity, "reason": "cte_key_has_no_direct_physical_lineage"}
    replacement_signature = _edge_signature(
        (stable_lineage, replacement_lineage)
    )
    strong = _strong_query_edge_signatures(relationship_edges)
    same_table_pair = {
        signature
        for signature in strong
        if _table_pair(signature) == _table_pair(replacement_signature)
    }
    if same_table_pair != {replacement_signature}:
        return {
            **identity,
            "reason": "cte_physical_edge_not_uniquely_graph_certified",
            "replacement_edge_signature": list(replacement_signature),
            "candidate_edge_signatures": [
                list(value) for value in sorted(same_table_pair)
            ],
        }

    # Prove that the proposal contains no additional edits.  Revert the one
    # relation-key exposure and the one equality endpoint, then require complete
    # normalized AST equality with the anchor.
    reverted = proposal.copy()
    reverted_ctes = _cte_definitions(reverted)
    assert reverted_ctes is not None
    reverted_cte = reverted_ctes[changed_cte]
    reverted_cte.set(
        "expressions",
        [
            expression
            for index, expression in enumerate(reverted_cte.expressions)
            if index != added_index
        ],
    )
    reverted_joins = list(reverted.args.get("joins") or [])
    reverted_joins[join_index].set("on", anchor_join.args["on"].copy())
    reverted.set("joins", reverted_joins)
    if reverted.sql(dialect=dialect.casefold()) != anchor.sql(
        dialect=dialect.casefold()
    ):
        return {**identity, "reason": "proposal_contains_non_relation_drift"}

    compiled = anchor.copy()
    compiled_ctes = _cte_definitions(compiled)
    assert compiled_ctes is not None
    compiled_ctes[changed_cte].append("expressions", added_projection.copy())
    compiled_joins = list(compiled.args.get("joins") or [])
    compiled_joins[join_index].set("on", proposal_join.args["on"].copy())
    compiled.set("joins", compiled_joins)
    sql = compiled.sql(dialect=dialect.casefold())
    return {
        "operator": "graph_certified_cte_relation_key_exposure",
        "applied": True,
        "reason": "proposal_and_graph_expose_hidden_cte_relation_key",
        "sql": sql,
        "cte": changed_cte,
        "old_output": old_output,
        "new_output": new_output,
        "physical_column": ".".join(replacement_lineage),
        "replacement_edge_signature": list(replacement_signature),
        "external_projection_frozen": True,
        "uses_evaluator_gold": False,
    }


def compile_relational_program(
    *,
    anchor_sql: str,
    question: str,
    database: Path,
    database_id: str,
    proposal_sql: str | None = None,
    evolution_mapping: RelationEvolutionMapping | None = None,
    dialect: str = "sqlite",
    table_old_to_new: dict[str, str] | None = None,
    column_old_to_new: dict[str, dict[str, str]] | None = None,
    relationship_edges: list[dict[str, Any]] | None = None,
    graph_evo_context: dict[str, Any] | None = None,
    proposal_execution: dict[str, Any] | None = None,
    realize_submitted_program: bool = False,
    preserve_submitted_grain: bool = False,
    timeout_seconds: float = 5.0,
) -> dict[str, Any]:
    """Compile one anchor into the method's relational-program representation."""

    graph_evo_context_sha256: str | None = None
    if graph_evo_context is not None:
        if graph_evo_context.get("uses_evaluator_gold") is not False:
            raise ValueError("Graph+Evo context must explicitly exclude evaluator gold")
        graph_evo_context_sha256 = sha256(
            json.dumps(
                graph_evo_context,
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
            ).encode()
        ).hexdigest()
        # M4 consumes exactly the query-conditioned typed edges shown to the
        # generator.  This prevents a hidden, wider relation inventory from
        # changing the compiled SQL after generation.
        relationship_edges = [
            dict(value)
            for value in graph_evo_context.get("typed_join_edges") or []
            if isinstance(value, dict)
        ]

    working_sql = anchor_sql
    transformations: list[dict[str, Any]] = []
    certificates: list[dict[str, Any]] = []
    if realize_submitted_program:
        if graph_evo_context is None:
            raise ValueError(
                "role-first submitted-program realization requires Graph+Evo context"
            )
        realization = realize_executed_role_first_program(
            anchor_sql=anchor_sql,
            proposal_sql=str(proposal_sql or ""),
            graph_evo_context=graph_evo_context,
            proposal_execution=proposal_execution,
            dialect=dialect,
        )
        realized_sql = str(realization.pop("sql"))
        certificates.append(realization)
        if realization["applied"]:
            working_sql = realized_sql
            transformations.append(
                {
                    "operator": realization["operator"],
                    "reason": realization["reason"],
                    "program_sha256": realization["program_sha256"],
                    "changed_ast_dimensions": realization[
                        "changed_ast_dimensions"
                    ],
                    "candidate_selection_performed": False,
                    "score_or_expected_answer_consulted": False,
                }
            )
    exact_literal_program_admitted = _sql_covers_graph_exact_literals(
        working_sql, graph_evo_context, dialect
    )

    if proposal_sql and graph_evo_context is not None:
        exact_literal_completion = _compile_graph_exact_literal_program_completion(
            anchor_sql=working_sql,
            proposal_sql=proposal_sql,
            dialect=dialect,
            graph_evo_context=graph_evo_context,
            proposal_execution=proposal_execution,
        )
        exact_literal_sql = str(exact_literal_completion.pop("sql"))
        certificates.append(exact_literal_completion)
        if exact_literal_completion["applied"]:
            working_sql = exact_literal_sql
            exact_literal_program_admitted = True
            transformations.append(
                {
                    "operator": exact_literal_completion["operator"],
                    "reason": exact_literal_completion["reason"],
                    "added_predicates": exact_literal_completion[
                        "added_predicates"
                    ],
                    "added_projections": exact_literal_completion[
                        "added_projections"
                    ],
                    "added_tables": exact_literal_completion["added_tables"],
                    "edge_signatures": exact_literal_completion[
                        "edge_signatures"
                    ],
                    "anchor_clauses_preserved": exact_literal_completion[
                        "anchor_clauses_preserved"
                    ],
                    "cardinality_normalization": exact_literal_completion.get(
                        "cardinality_normalization"
                    ),
                }
            )

        projection_completion = _compile_graph_role_projection_completion(
            anchor_sql=working_sql,
            proposal_sql=proposal_sql,
            dialect=dialect,
            graph_evo_context=graph_evo_context,
            proposal_execution=proposal_execution,
        )
        projection_completion_sql = str(projection_completion.pop("sql"))
        certificates.append(projection_completion)
        if projection_completion["applied"]:
            working_sql = projection_completion_sql
            transformations.append(
                {
                    "operator": projection_completion["operator"],
                    "reason": projection_completion["reason"],
                    "added_projections": projection_completion[
                        "added_projections"
                    ],
                    "added_tables": projection_completion["added_tables"],
                    "edge_signatures": projection_completion[
                        "edge_signatures"
                    ],
                    "anchor_nonrelation_ast_frozen": projection_completion[
                        "anchor_nonrelation_ast_frozen"
                    ],
                }
            )

    if proposal_sql and evolution_mapping is None and exact_literal_program_admitted:
        proposal = _outer_to_inner_from_proposal(
            anchor_sql=working_sql,
            proposal_sql=proposal_sql,
            database=database,
            database_id=database_id,
            dialect=dialect,
            table_old_to_new=table_old_to_new,
            column_old_to_new=column_old_to_new,
            relationship_edges=relationship_edges,
        )
        proposal_sql_out = str(proposal.pop("sql"))
        certificates.append(proposal)
        if proposal["applied"]:
            working_sql = proposal_sql_out
            transformations.append(
                {
                    "operator": proposal["operator"],
                    "reason": proposal["reason"],
                    "refined_tables": proposal.get("refined_tables") or [],
                }
            )

        cte_key_substitution = _compile_cte_relation_key_substitution(
            anchor_sql=working_sql,
            proposal_sql=proposal_sql,
            dialect=dialect,
            relationship_edges=relationship_edges,
        )
        cte_key_substitution_sql = str(cte_key_substitution.pop("sql"))
        certificates.append(cte_key_substitution)
        if cte_key_substitution["applied"]:
            working_sql = cte_key_substitution_sql
            transformations.append(
                {
                    "operator": cte_key_substitution["operator"],
                    "reason": cte_key_substitution["reason"],
                    "cte_transformations": cte_key_substitution[
                        "cte_transformations"
                    ],
                    "external_projection_frozen": cte_key_substitution[
                        "external_projection_frozen"
                    ],
                    "outer_query_contract_frozen": cte_key_substitution[
                        "outer_query_contract_frozen"
                    ],
                }
            )

        working_tree = _top_level_select(working_sql, dialect)
        if working_tree is not None and working_tree.args.get("with_") is not None:
            cte_exposure = _compile_cte_relation_key_exposure(
                anchor_sql=working_sql,
                proposal_sql=proposal_sql,
                dialect=dialect,
                relationship_edges=relationship_edges,
            )
            cte_exposure_sql = str(cte_exposure.pop("sql"))
            certificates.append(cte_exposure)
            if cte_exposure["applied"]:
                working_sql = cte_exposure_sql
                transformations.append(
                    {
                        "operator": cte_exposure["operator"],
                        "reason": cte_exposure["reason"],
                        "cte": cte_exposure["cte"],
                        "old_output": cte_exposure["old_output"],
                        "new_output": cte_exposure["new_output"],
                        "physical_column": cte_exposure["physical_column"],
                        "replacement_edge_signature": cte_exposure[
                            "replacement_edge_signature"
                        ],
                        "external_projection_frozen": cte_exposure[
                            "external_projection_frozen"
                        ],
                    }
                )

        relation_tree = _compile_relation_tree_substitution(
            anchor_sql=working_sql,
            proposal_sql=proposal_sql,
            dialect=dialect,
            relationship_edges=relationship_edges,
        )
        relation_tree_sql = str(relation_tree.pop("sql"))
        certificates.append(relation_tree)
        if relation_tree["applied"]:
            working_sql = relation_tree_sql
            transformations.append(
                {
                    "operator": relation_tree["operator"],
                    "reason": relation_tree["reason"],
                    "removed_tables": relation_tree["removed_tables"],
                    "added_tables": relation_tree["added_tables"],
                    "shared_tables": relation_tree["shared_tables"],
                    "edge_signatures": relation_tree["edge_signatures"],
                    "external_projection_frozen": relation_tree[
                        "external_projection_frozen"
                    ],
                    "nonrelation_ast_frozen": relation_tree[
                        "nonrelation_ast_frozen"
                    ],
                    "proposal_nonrelation_ignored": relation_tree[
                        "proposal_nonrelation_ignored"
                    ],
                }
            )

        key_substitution = _compile_relation_key_substitution(
            anchor_sql=working_sql,
            proposal_sql=proposal_sql,
            dialect=dialect,
            relationship_edges=relationship_edges,
        )
        key_substitution_sql = str(key_substitution.pop("sql"))
        certificates.append(key_substitution)
        if key_substitution["applied"]:
            working_sql = key_substitution_sql
            transformations.append(
                {
                    "operator": key_substitution["operator"],
                    "reason": key_substitution["reason"],
                    "replacements": key_substitution["replacements"],
                    "changed_edges": key_substitution["changed_edges"],
                    "rewritten_occurrences": key_substitution[
                        "rewritten_occurrences"
                    ],
                    "frozen_nonjoin_occurrences": key_substitution[
                        "frozen_nonjoin_occurrences"
                    ],
                    "ignored_proposal_modality_changes": key_substitution[
                        "ignored_proposal_modality_changes"
                    ],
                }
            )

    elif proposal_sql and evolution_mapping is None:
        certificates.append(
            {
                "operator": "proposal_relation_program_admission",
                "applied": False,
                "reason": "graph_exact_literal_terminal_not_fulfilled",
                "uses_evaluator_gold": False,
            }
        )

    if evolution_mapping is None and dialect.casefold() == "sqlite":
        lookup = _compile_redundant_parent_lookup(
            sql=working_sql,
            database=database,
            database_id=database_id,
            dialect=dialect,
            timeout_seconds=timeout_seconds,
        )
        lookup_sql = str(lookup.pop("sql"))
        certificates.append(lookup)
        if lookup["applied"]:
            working_sql = lookup_sql
            transformations.append(
                {
                    "operator": lookup["operator"],
                    "reason": lookup["reason"],
                    "kept_child": lookup["kept_child"],
                    "eliminated_parent": lookup["eliminated_parent"],
                    "rewritten_key_references": lookup[
                        "rewritten_key_references"
                    ],
                }
            )

    if evolution_mapping is not None:
        # Lazy import avoids the evoschema tools -> react controller dependency
        # cycle while keeping the static compiler usable inside that controller.
        from finsemguard.e2e.evolution_aware_relation_repair import (
            repair_evolution_aware_relation,
        )

        evolution = repair_evolution_aware_relation(
            sql=working_sql,
            question=question,
            database=database,
            mapping=evolution_mapping,
            dialect=dialect,
            timeout_seconds=timeout_seconds,
        )
        evolution_sql = str(evolution.pop("sql"))
        transformed = evolution.pop("selected", "") == "evolution_aware_relation_repair"
        certificates.append(
            {
                "operator": "evolution_lineage",
                "applied": transformed,
                **evolution,
            }
        )
        if transformed:
            working_sql = evolution_sql
            for transformation in evolution.get("transformations") or []:
                graph = dict(transformation.get("graph") or {})
                transformations.append(
                    {
                        "operator": "evolution_lineage",
                        "kind": transformation.get("kind"),
                        "old_split_join_signatures": transformation.get(
                            "old_split_join_signatures"
                        )
                        or [],
                        "new_split_join_signatures": transformation.get(
                            "new_split_join_signatures"
                        )
                        or [],
                        "join_tree_sha256": dict(
                            graph.get("certificate") or {}
                        ).get("join_tree_sha256"),
                    }
                )
    elif preserve_submitted_grain:
        # Query-bound scopes define measure weighting. A shorter physical tree
        # and COUNT(DISTINCT key) are not a proof of equivalent population/grain.
        # Keep Graph/Evo binding, lineage and certified relation repairs above.
        certificates.append({
            "operator": "cardinality_aware_minimal_relation_tree",
            "applied": False,
            "reason": "submitted_scope_and_measure_grain_preserved",
            "uses_evaluator_gold": False,
        })
    elif dialect.casefold() == "sqlite":
        cardinality = repair_anchor_join_tree(
            sql=working_sql,
            question=question,
            database=database,
            database_id=database_id,
            dialect=dialect,
            table_old_to_new=table_old_to_new,
            column_old_to_new=column_old_to_new,
            timeout_seconds=timeout_seconds,
        )
        cardinality_sql = str(cardinality.pop("sql"))
        transformed = cardinality.pop("selected", "") == "anchor_join_tree_repair"
        certificates.append(
            {
                "operator": "cardinality_aware_minimal_relation_tree",
                "applied": transformed,
                **cardinality,
            }
        )
        if transformed:
            working_sql = cardinality_sql
            transformations.append(
                {
                    "operator": "cardinality_aware_minimal_relation_tree",
                    "reason": cardinality["reason"],
                    "entity_mode": cardinality.get("entity_mode"),
                    "distinct_entity_normalized": bool(
                        cardinality.get("distinct_entity_normalized")
                    ),
                }
            )
    else:
        certificates.append(
            {
                "operator": "cardinality_aware_minimal_relation_tree",
                "applied": False,
                "reason": "backend_has_no_cardinality_catalog_adapter",
                "dialect": dialect.casefold(),
                "uses_evaluator_gold": False,
            }
        )

    return {
        "sql": working_sql,
        "compiler_id": COMPILER_ID,
        "status": "transformed" if transformations else "identity",
        "transformations": transformations,
        "certificates": certificates,
        "anchor_sql_sha256": _sha(anchor_sql),
        "compiled_sql_sha256": _sha(working_sql),
        "graph_evo_context_sha256": graph_evo_context_sha256,
        "graph_evo_context_consumed": graph_evo_context is not None,
        "uses_evaluator_gold": False,
    }


def realize_entity_grain_contracts(sql: str, contracts: Any, database: Path) -> tuple[str, dict[str, Any]]:
    """Realize explicit ontology measure grain, separate from the frozen anchor compiler.

    Only the opt-in v14 consumer calls this. Entity identity survives the DISTINCT
    projection, so equal-valued measurements from different entities are retained.
    The contract is a model interpretation, not a correctness certificate.
    """
    audit: dict[str, Any] = {"version": "ontology_entity_grain_v14", "contracts": [],
        "source_sha256": _sha(sql), "uses_evaluator_gold": False,
        "contract_is_model_interpretation": True}
    if not isinstance(contracts, list) or len(contracts) > 8:
        return sql, {**audit, "status": "rejected", "reason": "expected at most8 typed contracts"}
    if not contracts:
        return sql, {**audit, "status": "not_requested", "applied": 0}
    try:
        statements = sqlglot.parse(sql, read="sqlite")
        if len(statements) != 1 or not isinstance(statements[0], exp.Query):
            raise ValueError("one query required")
        tree = statements[0]
        with sqlite3.connect(f"file:{database}?mode=ro", uri=True, timeout=2) as conn:
            conn.execute("PRAGMA query_only=ON")
            started = time.monotonic()
            conn.set_progress_handler(lambda: int(time.monotonic()-started > 3), 1000)
            schema = {}
            for (table,) in conn.execute("SELECT name FROM sqlite_master WHERE type='table'"):
                quoted = '"'+table.replace('"','""')+'"'
                cols = conn.execute(f"PRAGMA table_info({quoted})").fetchall()
                schema[table.lower()] = {"columns": {c[1].lower(): c[1] for c in cols},
                    "keys": [c[1] for c in sorted(cols,key=lambda c:c[5]) if c[5]], "quoted": quoted}
            for contract in contracts:
                item: dict[str, Any] = {"requested": contract, "status": "rejected"}
                audit["contracts"].append(item)
                try:
                    if not isinstance(contract, dict) or not all(isinstance(contract.get(k), str) and contract[k].strip()
                        for k in ("table", "alias", "weighting", "question_basis")):
                        raise ValueError("table, alias, weighting and question_basis required")
                    if contract["weighting"] == "joined_rows":
                        item.update(status="retained", reason="explicit joined-row weighting")
                        continue
                    if contract["weighting"] != "entity_once":
                        raise ValueError("unknown weighting")
                    def local(node, kind):
                        return [n for n in node.find_all(kind) if n.find_ancestor(exp.Select) is node]
                    def relations(node):
                        f = node.args.get("from_")
                        return ([f.this] if f else []) + [j.this for j in node.args.get("joins", [])]
                    candidates = [s for s in tree.find_all(exp.Select) if local(s, exp.AggFunc) and
                        any(isinstance(t, exp.Table) and t.name.lower()==contract["table"].lower() and
                            t.alias_or_name.lower()==contract["alias"].lower() for t in relations(s))]
                    if len(candidates) != 1:
                        raise ValueError("aggregate relation scope absent or ambiguous")
                    select = candidates[0]
                    sources = relations(select)
                    ctes = {c.alias_or_name.lower() for c in tree.find_all(exp.CTE)}
                    if any(not isinstance(t, exp.Table) or t.name.lower() not in schema or
                           t.name.lower() in ctes for t in sources):
                        raise ValueError("derived relation not supported")
                    if any(j.args.get("side") or str(j.args.get("kind", "")).upper() not in ("", "INNER", "CROSS")
                           for j in select.args.get("joins", [])):
                        raise ValueError("outer/semi/anti join requires separate semantics")
                    if local(select, exp.Window) or any(isinstance(n, exp.Star) for n in select.expressions):
                        raise ValueError("window or star projection not supported")
                    alias_map = {t.alias_or_name.lower(): t for t in sources}
                    if len(alias_map) != len(sources):
                        raise ValueError("duplicate relation alias")
                    measured_alias = contract["alias"].lower()
                    source = alias_map[measured_alias]
                    info = schema[source.name.lower()]
                    if not info["keys"]:
                        raise ValueError("no physical primary key")
                    condition = ' OR '.join('"'+k.replace('"','""')+'" IS NULL' for k in info['keys'])
                    if conn.execute(f"SELECT 1 FROM {info['quoted']} WHERE {condition} LIMIT 1").fetchone():
                        raise ValueError("nullable physical identity")
                    def resolve(col):
                        aliases = [col.table.lower()] if col.table else [a for a,t in alias_map.items()
                            if col.name.lower() in schema[t.name.lower()]["columns"]]
                        if len(aliases)!=1 or aliases[0] not in alias_map or col.name.lower() not in schema[alias_map[aliases[0]].name.lower()]["columns"]:
                            raise ValueError("ambiguous or correlated physical column")
                        return aliases[0], col.name.lower()
                    # Preserve correlated predicates only when their outer dependency is
                    # inside this same block. External correlation is not compiled here.
                    for col in local(select, exp.Column):
                        if col.table and col.table.lower() not in alias_map:
                            raise ValueError("external correlation")
                    group = select.args.get("group")
                    group_cols = list(group.expressions) if group else []
                    if any(not isinstance(g, exp.Column) for g in group_cols):
                        raise ValueError("group expression/ordinal not supported")
                    group_ids = {resolve(g) for g in group_cols}
                    clause_keys = ("expressions", "group", "having", "order")
                    consumers = list(select.expressions) + [select.args[k] for k in clause_keys[1:] if select.args.get(k)]
                    if any(n.find(exp.Select) is not None for n in consumers):
                        raise ValueError("scalar subquery in aggregate consumer")
                    projection_aliases = {n.alias.lower() for n in select.expressions if isinstance(n,exp.Alias)}
                    required = {}
                    for clause in consumers:
                        for col in clause.find_all(exp.Column):
                            if not col.table and col.name.lower() in projection_aliases and clause not in select.expressions:
                                continue  # ORDER/HAVING output aliases stay in the outer query.
                            identity = resolve(col)
                            agg = col.find_ancestor(exp.AggFunc)
                            if agg is not None and agg.find_ancestor(exp.Select) is select:
                                if identity[0] != measured_alias:
                                    raise ValueError("aggregate uses another relation; mixed measure scope")
                            elif identity not in group_ids:
                                raise ValueError("non-aggregate output must be an explicit group key")
                            required.setdefault(identity,col.copy())
                    # A primary key is retained even if it was never projected or counted.
                    for key in info["keys"]:
                        required.setdefault((measured_alias,key.lower()),exp.column(key,table=source.alias_or_name,quoted=True))
                    aliases = {identity:f"__grain_value_{i}" for i,identity in enumerate(required)}
                    inner = select.copy()
                    inner.set("expressions",[exp.alias_(col.copy(),aliases[identity],quoted=True) for identity,col in required.items()])
                    for key in ("group","having","order","limit","offset","qualify","windows","with_"):
                        inner.set(key,None)
                    inner.set("distinct",exp.Distinct())
                    outer = select.copy()
                    for key in ("joins","where"):
                        outer.set(key,None)
                    inner_alias = "__ontology_entity_grain"
                    outer.set("from_",exp.From(this=inner.subquery(inner_alias)))
                    def replace_column(node):
                        if not isinstance(node,exp.Column):
                            return node
                        if not node.table and node.name.lower() in projection_aliases:
                            try: identity=resolve(node)
                            except ValueError: return node
                        else: identity=resolve(node)
                        if identity not in aliases:
                            return node
                        return exp.column(aliases[identity],table=inner_alias,quoted=True)
                    outer.set("expressions",[n.transform(replace_column) for n in select.expressions])
                    for key in ("group","having","order"):
                        if select.args.get(key):outer.set(key,select.args[key].transform(replace_column))
                    # Preserve implicit output names for downstream CTE/subquery consumers.
                    for original,new in zip(select.expressions,outer.expressions):
                        if isinstance(original,exp.Column):
                            new.replace(exp.alias_(new.copy(),original.name,quoted=True))
                    if select is tree: tree=outer
                    else: select.replace(outer)
                    item.update(status="applied", physical_primary_key=info["keys"],
                        group_keys=[c.sql(dialect="sqlite") for c in group_cols],
                        realization="distinct physical entity identity and group values before unchanged aggregation")
                except Exception as error:
                    item["reason"] = f"{type(error).__name__}: {error}"[:300]
        applied = sum(i['status']=='applied' for i in audit['contracts'])
        candidate = tree.sql(dialect="sqlite") if applied else sql
        # Validate syntax only. EX/gold do not select between candidate and original.
        if applied: sqlglot.parse_one(candidate,read="sqlite")
        audit.update(status="applied" if applied else "retained",applied=applied,result_sha256=_sha(candidate))
        return candidate,audit
    except Exception as error:
        return sql,{**audit,"status":"rejected","applied":0,"reason":f"{type(error).__name__}: {error}"[:300]}


def lower_integer_key_eligibility(sql: str, database: Path) -> tuple[str, dict[str, Any]]:
    """Lower positive conjunctive EXISTS to key membership without model/evaluator input.

    Integer affinity on both correlation columns and no declared COLLATE avoid
    changing SQLite comparison affinity/collation when exchanging operand sides.
    NULL equality is preserved as row eligibility, not as a projected Boolean.
    """
    audit: dict[str, Any] = {"version": "ontology_keyset_eligibility_v15", "rules": [],
        "source_sha256": _sha(sql), "uses_evaluator_gold": False, "additional_model_calls": 0}
    try:
        parsed = sqlglot.parse(sql, read="sqlite")
        if len(parsed)!=1 or not isinstance(parsed[0],exp.Query):
            raise ValueError("one query required")
        tree=parsed[0]
        with sqlite3.connect(f"file:{database}?mode=ro",uri=True) as conn:
            catalog={}
            for name,ddl in conn.execute("SELECT name,sql FROM sqlite_master WHERE type='table'"):
                quoted='"'+name.replace('"','""')+'"'
                catalog[name.lower()]={'types':{c[1].lower():str(c[2]).upper() for c in conn.execute(f'PRAGMA table_info({quoted})')},
                    'collation': 'COLLATE' in str(ddl).upper()}
        ctes={c.alias_or_name.lower() for c in tree.find_all(exp.CTE)}
        def relation_map(select):
            f=select.args.get('from_');nodes=([f.this] if f else [])+[j.this for j in select.args.get('joins',[])]
            if not nodes or any(not isinstance(t,exp.Table) or t.name.lower() not in catalog or t.name.lower() in ctes for t in nodes):
                raise ValueError('nonphysical or derived relation')
            result={t.alias_or_name.lower():t.name.lower() for t in nodes}
            if len(result)!=len(nodes):raise ValueError('ambiguous alias')
            return result
        def conjuncts(node):
            if isinstance(node,exp.Paren):return conjuncts(node.this)
            return conjuncts(node.this)+conjuncts(node.expression) if isinstance(node,exp.And) else [node]
        for exists in list(tree.find_all(exp.Exists)):
            rule={'status':'retained','source_exists_sha256':_sha(exists.sql(dialect='sqlite'))};audit['rules'].append(rule)
            try:
                parent=exists.parent
                while isinstance(parent,(exp.And,exp.Paren)):parent=parent.parent
                if not isinstance(parent,exp.Where):raise ValueError('not positive conjunctive WHERE eligibility')
                outer=parent.parent;inner=exists.this
                if not isinstance(outer,exp.Select) or not isinstance(inner,exp.Select):raise ValueError('unsupported query block')
                if len(list(inner.find_all(exp.Select)))!=1 or inner.find(exp.AggFunc) or inner.find(exp.Window):
                    raise ValueError('nested or aggregate existence')
                if any(inner.args.get(k) is not None for k in ('limit','offset','group','having','qualify','with_')):
                    raise ValueError('existence cardinality modifier')
                if any(isinstance(n,exp.Func) and (n.sql_name().lower() in {'rand','random','randomblob','changes','last_insert_rowid'} or
                       isinstance(n,exp.Anonymous)) for n in inner.walk()):
                    raise ValueError('volatile or unrecognized function')
                outer_map=relation_map(outer);inner_map=relation_map(inner)
                if set(outer_map)&set(inner_map):raise ValueError('shadowed aliases')
                where=inner.args.get('where')
                if where is None:raise ValueError('uncorrelated EXISTS')
                pairs=[];residual=[]
                for term in conjuncts(where.this):
                    cols=list(term.find_all(exp.Column))
                    if any(not c.table for c in cols):raise ValueError('unqualified column')
                    outside=[c for c in cols if c.table.lower() not in inner_map]
                    if not outside:residual.append(term.copy());continue
                    if not isinstance(term,exp.EQ) or not isinstance(term.this,exp.Column) or not isinstance(term.expression,exp.Column):
                        raise ValueError('non-equality correlation')
                    left,right=term.this,term.expression
                    if left.table.lower() in outer_map and right.table.lower() in inner_map:left,right=right,left
                    if left.table.lower() not in inner_map or right.table.lower() not in outer_map:
                        raise ValueError('correlation outside immediate scope')
                    for col,mapping in ((left,inner_map),(right,outer_map)):
                        info=catalog[mapping[col.table.lower()]]
                        if info['collation'] or 'INT' not in info['types'].get(col.name.lower(),''):
                            raise ValueError('requires integer keys with default collation')
                    pairs.append((left.copy(),right.copy()))
                if not pairs:raise ValueError('no qualified equality correlation')
                lowered=inner.copy();lowered.set('expressions',[a for a,b in pairs]);lowered.set('order',None)
                lowered.set('where',exp.Where(this=exp.and_(*residual)) if residual else None)
                # Includes ON clauses: no unresolved outer dependency may remain.
                if any(not c.table or c.table.lower() not in inner_map for c in lowered.find_all(exp.Column)):
                    raise ValueError('residual correlation')
                keys=[b for a,b in pairs]
                lhs=keys[0] if len(keys)==1 else exp.Tuple(expressions=keys)
                replacement=exp.In(this=lhs,query=lowered.subquery())
                exists.replace(replacement)
                rule.update(status='applied',correlation_keys=[{'inner':a.sql(dialect='sqlite'),'outer':b.sql(dialect='sqlite')} for a,b in pairs],
                    local_predicates=[t.sql(dialect='sqlite') for t in residual],
                    realization='positive WHERE membership in independent integer key set')
            except ValueError as error:rule['reason']=str(error)
        applied=sum(r['status']=='applied' for r in audit['rules'])
        result=tree.sql(dialect='sqlite') if applied else sql
        audit.update(status='applied' if applied else 'retained',applied=applied,result_sha256=_sha(result))
        return result,audit
    except Exception as error:
        return sql,{**audit,'status':'retained','applied':0,'reason':f'{type(error).__name__}: {error}'[:300]}


def lower_result_eligibility(result: dict[str, Any], database: Path) -> dict[str, Any]:
    """The same final transformation is used by generation and frozen-output reuse."""
    sql,audit=lower_integer_key_eligibility(str(result.get('sql') or ''),database)
    result.setdefault('react',{})['eligibility_lowering']={**audit,'pre_lowering_sql':result.get('sql')}
    if audit.get('applied'):
        result['react']['pre_lowering_execution_probe']=result.get('execution_probe')
        result['execution_probe']={'executable':None,'state':'not_executed_after_deterministic_lowering',
            'official_score':False,'sql_sha256':_sha(sql)}
    result['sql']=sql
    result['method_revision']='ontology_keyset_eligibility_v15'
    return result
