"""Compose a generated relation program into an existing SQL solution.

The graph/planner branch is responsible for proposing a typed physical program.
It cannot silently re-decide anything already established by the base solution.
Separate M4 operators may append a missing question-explicit output or a unique
exact-literal predicate, but only while retaining every anchor clause.  This
module records that boundary; the compiler enforces it by AST construction
rather than by choosing between scored candidates.
"""

from __future__ import annotations

from collections import defaultdict
from hashlib import sha256
from typing import Any

import sqlglot
from sqlglot import exp


def _sha(value: str) -> str:
    return sha256(value.encode()).hexdigest()


def _parse_select(sql: str, dialect: str) -> exp.Select:
    tree = sqlglot.parse_one(sql, read=dialect.casefold())
    if not isinstance(tree, exp.Select):
        raise ValueError("top-level SQL is not a SELECT")
    return tree


def _top_level_sources(tree: exp.Select) -> list[exp.Table]:
    sources: list[exp.Expression] = []
    from_clause = tree.args.get("from_")
    if from_clause is not None and from_clause.this is not None:
        sources.append(from_clause.this)
    sources.extend(join.this for join in tree.args.get("joins") or [])
    if not sources or any(not isinstance(source, exp.Table) for source in sources):
        raise ValueError("relation program contains a non-table source")
    return [source for source in sources if isinstance(source, exp.Table)]


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


def _required_anchor_aliases(tree: exp.Select) -> set[str]:
    """Return top-level sources referenced outside the replaceable join clauses."""

    required: set[str] = set()
    for column in tree.find_all(exp.Column):
        if _nearest_select(column) is not tree or _inside_join(column, tree):
            continue
        if column.table:
            required.add(str(column.table).casefold())
    return required


def _non_relation_sql(tree: exp.Select, dialect: str) -> str:
    copy = tree.copy()
    copy.set("from_", None)
    copy.set("joins", [])
    return copy.sql(dialect=dialect.casefold())


def _relation_sql(tree: exp.Select, dialect: str) -> str:
    relation = exp.select("1")
    from_clause = tree.args.get("from_")
    relation.set("from_", from_clause.copy() if from_clause is not None else None)
    relation.set("joins", [join.copy() for join in tree.args.get("joins") or []])
    return relation.sql(dialect=dialect.casefold())


def _set_table_alias(table: exp.Table, alias: str) -> None:
    if alias.casefold() == str(table.name).casefold():
        table.set("alias", None)
    else:
        table.set(
            "alias",
            exp.TableAlias(this=exp.Identifier(this=alias, quoted=True)),
        )


def _normalized_candidate_relations(
    anchor: exp.Select,
    candidate: exp.Select,
) -> tuple[exp.From, list[exp.Join], dict[str, str]]:
    """Copy candidate relations while retaining anchor aliases for shared tables."""

    anchor_sources = _top_level_sources(anchor)
    candidate_sources = _top_level_sources(candidate)
    anchor_by_table: dict[str, list[str]] = defaultdict(list)
    for source in anchor_sources:
        anchor_by_table[str(source.name).casefold()].append(str(source.alias_or_name))

    candidate_occurrence: dict[str, int] = defaultdict(int)
    used_aliases: set[str] = set()
    alias_map: dict[str, str] = {}
    assigned_aliases: list[str] = []
    for source in candidate_sources:
        table_key = str(source.name).casefold()
        old_alias = str(source.alias_or_name)
        occurrence = candidate_occurrence[table_key]
        candidate_occurrence[table_key] += 1
        anchor_aliases = anchor_by_table.get(table_key, [])
        if old_alias.casefold() in {
            value.casefold() for value in anchor_aliases
        }:
            new_alias = old_alias
        elif occurrence < len(anchor_aliases):
            new_alias = anchor_aliases[occurrence]
        else:
            new_alias = old_alias
        base = new_alias
        suffix = 2
        while new_alias.casefold() in used_aliases:
            new_alias = f"{base}_{suffix}"
            suffix += 1
        used_aliases.add(new_alias.casefold())
        alias_map[old_alias.casefold()] = new_alias
        # A qualified reference may use the physical table name even when the
        # source has an alias.  Normalize it only when that key is unambiguous.
        alias_map.setdefault(table_key, new_alias)
        assigned_aliases.append(new_alias)

    from_clause = candidate.args.get("from_")
    if from_clause is None:
        raise ValueError("candidate relation program has no FROM clause")
    copied_from = from_clause.copy()
    copied_joins = [join.copy() for join in candidate.args.get("joins") or []]
    copied_sources: list[exp.Table] = []
    if isinstance(copied_from.this, exp.Table):
        copied_sources.append(copied_from.this)
    for join in copied_joins:
        if not isinstance(join.this, exp.Table):
            raise ValueError("candidate relation program contains a non-table JOIN")
        copied_sources.append(join.this)
    if len(copied_sources) != len(assigned_aliases):
        raise ValueError("candidate relation source count changed during copy")
    for source, alias in zip(copied_sources, assigned_aliases, strict=True):
        _set_table_alias(source, alias)

    for expression in [copied_from, *copied_joins]:
        for column in expression.find_all(exp.Column):
            qualifier = str(column.table or "").casefold()
            if qualifier and qualifier in alias_map:
                column.set(
                    "table",
                    exp.Identifier(this=alias_map[qualifier], quoted=True),
                )
    return copied_from, copied_joins, alias_map


def anchor_relation_contract(sql: str, *, dialect: str = "sqlite") -> dict[str, Any]:
    """Return the compact, evaluator-free contract exposed to the planner."""

    immutable_scope = [
        "projection_and_order",
        "predicates_and_literals",
        "aggregation_grouping_having",
        "ordering_limit_distinct",
        "cte_set_operation_and_nested_query_semantics",
    ]
    try:
        tree = _parse_select(sql, dialect)
        sources = _top_level_sources(tree)
        non_relation_fingerprint = _sha(_non_relation_sql(tree, dialect))
    except Exception as error:
        # Complex/unsupported anchors are valid base solutions.  Their typed
        # relation program is the identity element: freeze the entire query
        # instead of turning a parser limitation into a missing prediction.
        return {
            "base_sql": sql,
            "immutable_scope": ["entire_query"],
            "replaceable_scope": [],
            "appendable_scope": [],
            "top_level_sources": [],
            "non_relation_fingerprint": _sha(sql),
            "contract_status": "identity_unsupported_relation_program",
            "parser_error_type": type(error).__name__,
            "uses_evaluator_gold": False,
        }
    return {
        "base_sql": sql,
        "immutable_scope": immutable_scope,
        "replaceable_scope": ["top_level_from", "top_level_joins"],
        "appendable_scope": [
            "graph_bound_question_explicit_output_role",
            "unique_exact_question_literal_predicate",
        ],
        "top_level_sources": [
            {
                "table": str(source.name),
                "alias": str(source.alias_or_name),
            }
            for source in sources
        ],
        "non_relation_fingerprint": non_relation_fingerprint,
        "contract_status": "typed_relation_program",
        "uses_evaluator_gold": False,
    }


def compose_anchor_relation_program(
    *,
    anchor_sql: str,
    candidate_sql: str,
    dialect: str = "sqlite",
) -> dict[str, Any]:
    """Install candidate FROM/JOIN into the base AST and preserve everything else.

    Returning the unchanged anchor for an unsupported or incomplete relation
    proposal is the identity element of the relation transformation, not a
    score-aware fallback: no execution label or alternative correctness estimate
    is consulted.
    """

    result: dict[str, Any] = {
        "sql": anchor_sql,
        "applied": False,
        "reason": "identity_relation_program",
        "uses_evaluator_gold": False,
    }
    try:
        anchor = _parse_select(anchor_sql, dialect)
        candidate = _parse_select(candidate_sql, dialect)
        anchor_sources = _top_level_sources(anchor)
        candidate_sources = _top_level_sources(candidate)
    except Exception as error:
        return {
            **result,
            "reason": f"identity_unsupported_relation:{type(error).__name__}",
        }

    anchor_alias_table = {
        str(source.alias_or_name).casefold(): str(source.name).casefold()
        for source in anchor_sources
    }
    candidate_tables = {str(source.name).casefold() for source in candidate_sources}
    missing_required = sorted(
        alias
        for alias in _required_anchor_aliases(anchor)
        if anchor_alias_table.get(alias) not in candidate_tables
    )
    if missing_required:
        return {
            **result,
            "reason": "identity_candidate_missing_required_anchor_source",
            "missing_required_aliases": missing_required,
        }

    try:
        copied_from, copied_joins, alias_map = _normalized_candidate_relations(
            anchor, candidate
        )
        composed = anchor.copy()
        composed.set("from_", copied_from)
        composed.set("joins", copied_joins)
        before_non_relation = _non_relation_sql(anchor, dialect)
        after_non_relation = _non_relation_sql(composed, dialect)
        if before_non_relation != after_non_relation:
            raise AssertionError("non-relation contract changed during composition")
        sql = composed.sql(dialect=dialect.casefold())
        anchor_relation = _relation_sql(anchor, dialect)
        composed_relation = _relation_sql(composed, dialect)
    except Exception as error:
        return {
            **result,
            "reason": f"identity_relation_composition_error:{type(error).__name__}",
        }

    return {
        **result,
        "sql": sql,
        "applied": composed_relation != anchor_relation,
        "reason": (
            "candidate_relation_program_composed"
            if composed_relation != anchor_relation
            else "identity_equivalent_relation_program"
        ),
        "alias_map": alias_map,
        "anchor_non_relation_fingerprint": _sha(before_non_relation),
        "anchor_relation_fingerprint": _sha(anchor_relation),
        "candidate_relation_fingerprint": _sha(_relation_sql(candidate, dialect)),
        "composed_relation_fingerprint": _sha(composed_relation),
    }
