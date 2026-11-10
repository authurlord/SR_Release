"""Compile role-grounded schema evidence into a minimal physical join tree.

The compiler treats physical bindings returned for one query role as alternatives,
not as tables that must all be joined.  It jointly chooses one binding per role and
then uses a bounded joint search to build a small, direction-aware Steiner-tree
approximation over relationship evidence.  The output is an operational certificate
that can be consumed directly by the SQL planner; it never reads evaluator SQL or
labels.
"""

from __future__ import annotations

from dataclasses import dataclass, replace
from hashlib import sha256
import heapq
import json
import math
import re
from typing import Any, Iterable

from finsemguard.e2e.livesqlbench import CatalogDocument


_DECLARED_MARKERS = (
    "declared_or_materialized_relationship",
    "declared_foreign_key",
    "declared_fk",
    "foreign_key",
)
_HISTORY_MARKERS = ("target_disjoint_historical_join", "historical_join")
_KNOWLEDGE_MARKERS = ("external_knowledge_relationship", "knowledge_relationship")
_DERIVED_MARKERS = ("declared_shared_key_equivalence", "derived_equijoin")
_EVOLUTION_KEY_MARKERS = ("evolution_split_key_equivalence",)
_EVOLUTION_SHARED_MARKERS = ("released_split_shared_column",)
_PROFILE_MARKERS = ("profile_value_containment_join",)
_COMPATIBILITY_MARKERS = ("same_physical_column_name", "compatible_join_key")
_CONNECTIVITY_MARKERS = ("declared_foreign_key_table_connectivity",)


def _quote(identifier: str) -> str:
    return '"' + str(identifier).replace('"', '""') + '"'


def _evidence_types(source: dict[str, Any]) -> tuple[str, ...]:
    evidence = source.get("evidence_types") or source.get("evidence") or []
    if isinstance(evidence, str):
        evidence = [value.strip() for value in evidence.split("+") if value.strip()]
    return tuple(dict.fromkeys(str(value) for value in evidence if str(value)))


def _endpoint(value: Any) -> tuple[str, str] | None:
    table, separator, column = str(value or "").rpartition(".")
    if not separator or not table.strip() or not column.strip():
        return None
    return table.strip(), column.strip()


def _has_marker(evidence: Iterable[str], markers: tuple[str, ...]) -> bool:
    folded = tuple(str(value).casefold() for value in evidence)
    return any(marker in value for value in folded for marker in markers)


def _edge_class(evidence: tuple[str, ...], precise: bool) -> tuple[str, float]:
    if _has_marker(evidence, _DECLARED_MARKERS):
        return "declared", 0.10 if precise else 1.45
    if _has_marker(evidence, _HISTORY_MARKERS):
        return "history", 0.28 if precise else 1.70
    if _has_marker(evidence, _KNOWLEDGE_MARKERS):
        return "knowledge", 0.42 if precise else 1.85
    if _has_marker(evidence, _DERIVED_MARKERS):
        # Two child foreign keys referencing the same declared parent key are
        # equality-compatible.  The shortcut is slightly dearer than a direct
        # FK, but cheaper than retaining the parent only to enforce equality.
        return "derived", 0.16 if precise else 1.90
    if _has_marker(evidence, _EVOLUTION_KEY_MARKERS):
        # Both current relations are lossless projections of one immutable
        # source relation and carry the same source key.
        return "evolution_key", 0.18 if precise else 1.90
    if _has_marker(evidence, _EVOLUTION_SHARED_MARKERS):
        # Shared non-key columns survive as a fallback path, but remain dearer
        # than declared/profile-backed joins because multiplicity is unknown.
        return "evolution_shared", 0.92 if precise else 2.05
    if _has_marker(evidence, _PROFILE_MARKERS):
        return "profile", 0.68 if precise else 2.00
    if _has_marker(evidence, _COMPATIBILITY_MARKERS):
        return "compatible", 1.15 if precise else 2.10
    if _has_marker(evidence, _CONNECTIVITY_MARKERS):
        return "connectivity", 2.20
    return "excluded", math.inf


@dataclass(frozen=True)
class PhysicalJoinEdge:
    left_table: str
    left_column: str
    right_table: str
    right_column: str
    score: float
    evidence_types: tuple[str, ...]
    provenance_ids: tuple[str, ...]
    evidence_class: str
    cost: float

    @property
    def precise(self) -> bool:
        return bool(self.left_column and self.right_column)

    @property
    def signature(self) -> tuple[str, str, str, str]:
        left = (self.left_table, self.left_column)
        right = (self.right_table, self.right_column)
        first, second = (left, right) if left <= right else (right, left)
        return first[0], first[1], second[0], second[1]

    @property
    def table_pair(self) -> tuple[str, str]:
        return tuple(sorted((self.left_table, self.right_table)))  # type: ignore[return-value]


@dataclass(frozen=True)
class RoleCandidate:
    role: str
    physical_identifier: str
    table: str
    score: float
    rank: int
    evidence_kind: str
    evidence_candidate_id: str
    semantic_alignment: float
    semantic_alignment_status: str
    required_companion_identifiers: tuple[str, ...]


@dataclass(frozen=True)
class _TreeCandidate:
    root: str
    role_choices: tuple[RoleCandidate, ...]
    unresolved_roles: tuple[str, ...]
    edge_ids: tuple[int, ...]
    objective: tuple[Any, ...]


def _ddl_edges(raw_tables: dict[str, CatalogDocument]) -> list[dict[str, Any]]:
    """Recover precise FK endpoints from common CREATE TABLE spellings."""

    identifier = r'(?:"([^"]+)"|`([^`]+)`|\[([^]]+)\]|([A-Za-z_][\w$]*))'
    pattern = re.compile(
        rf"FOREIGN\s+KEY\s*\(([^)]+)\)\s*REFERENCES\s+{identifier}\s*\(([^)]+)\)",
        flags=re.I | re.S,
    )

    def names(value: str) -> list[str]:
        output = []
        for item in value.split(","):
            cleaned = item.strip().strip('"`[] ')
            if cleaned:
                output.append(cleaned)
        return output

    output: list[dict[str, Any]] = []
    for table, row in raw_tables.items():
        for match in pattern.finditer(str(row.text)):
            target = next(
                (value for value in match.groups()[1:5] if value is not None), ""
            )
            left_columns = names(match.group(1))
            right_columns = names(match.group(6))
            if target not in raw_tables or len(left_columns) != len(right_columns):
                continue
            for left_column, right_column in zip(
                left_columns, right_columns, strict=True
            ):
                output.append(
                    {
                        "left": f"{table}.{left_column}",
                        "right": f"{target}.{right_column}",
                        "score": 1.0,
                        "evidence_types": ["declared_foreign_key_from_catalog_ddl"],
                        "provenance_ids": [row.candidate_id],
                    }
                )
    return output


def normalize_join_edges(
    *,
    raw_documents: list[CatalogDocument],
    ontology_edges: list[dict[str, Any]],
) -> tuple[dict[str, CatalogDocument], list[PhysicalJoinEdge]]:
    raw_tables = {
        str(row.table): row
        for row in raw_documents
        if row.kind == "table" and row.table
    }
    sources = [*ontology_edges, *_ddl_edges(raw_tables)]
    for table, row in raw_tables.items():
        for target in row.references:
            sources.append(
                {
                    "left_table": table,
                    "right_table": target,
                    "score": 1.0,
                    "evidence_types": [
                        "declared_foreign_key_table_connectivity"
                    ],
                    "provenance_ids": [row.candidate_id],
                }
            )

    merged: dict[tuple[str, str, str, str], dict[str, Any]] = {}
    for source in sources:
        evidence = _evidence_types(source)
        left_endpoint = _endpoint(source.get("left"))
        right_endpoint = _endpoint(source.get("right"))
        if left_endpoint and right_endpoint:
            left_table, left_column = left_endpoint
            right_table, right_column = right_endpoint
        else:
            left_table = str(source.get("left_table") or "")
            right_table = str(source.get("right_table") or "")
            left_column = right_column = ""
        if (
            not left_table
            or not right_table
            or left_table == right_table
            or left_table not in raw_tables
            or right_table not in raw_tables
        ):
            continue
        precise = bool(left_column and right_column)
        evidence_class, base_cost = _edge_class(evidence, precise)
        if not math.isfinite(base_cost):
            continue
        score = min(max(float(source.get("score", 0.5)), 0.05), 1.0)
        left = (left_table, left_column)
        right = (right_table, right_column)
        first, second = (left, right) if left <= right else (right, left)
        signature = first[0], first[1], second[0], second[1]
        previous = merged.get(signature)
        provenance = tuple(
            dict.fromkeys(str(value) for value in source.get("provenance_ids") or [])
        )
        if previous is None:
            merged[signature] = {
                "left_table": left_table,
                "left_column": left_column,
                "right_table": right_table,
                "right_column": right_column,
                "score": score,
                "evidence_types": evidence,
                "provenance_ids": provenance,
                "evidence_class": evidence_class,
                "base_cost": base_cost,
            }
            continue
        previous["score"] = max(float(previous["score"]), score)
        previous["evidence_types"] = tuple(
            dict.fromkeys([*previous["evidence_types"], *evidence])
        )
        previous["provenance_ids"] = tuple(
            dict.fromkeys([*previous["provenance_ids"], *provenance])
        )
        merged_class, merged_base = _edge_class(
            previous["evidence_types"], precise
        )
        previous["evidence_class"] = merged_class
        previous["base_cost"] = merged_base

    # A precise relationship dominates table-only connectivity for the same pair,
    # while multiple precise key alternatives remain available to the optimizer.
    precise_pairs = {
        tuple(sorted((value["left_table"], value["right_table"])))
        for value in merged.values()
        if value["left_column"] and value["right_column"]
    }
    edges: list[PhysicalJoinEdge] = []
    for value in merged.values():
        pair = tuple(sorted((value["left_table"], value["right_table"])))
        if not value["left_column"] and pair in precise_pairs:
            continue
        score = float(value["score"])
        cost = float(value["base_cost"]) + 0.18 * -math.log(score)
        edges.append(
            PhysicalJoinEdge(
                left_table=str(value["left_table"]),
                left_column=str(value["left_column"]),
                right_table=str(value["right_table"]),
                right_column=str(value["right_column"]),
                score=score,
                evidence_types=tuple(value["evidence_types"]),
                provenance_ids=tuple(value["provenance_ids"]),
                evidence_class=str(value["evidence_class"]),
                cost=cost,
            )
        )
    edges.sort(key=lambda edge: (edge.cost, edge.signature, edge.evidence_types))
    return raw_tables, edges


def _adjacency(
    tables: Iterable[str], edges: list[PhysicalJoinEdge]
) -> dict[str, list[tuple[str, int, float]]]:
    output: dict[str, list[tuple[str, int, float]]] = {
        table: [] for table in tables
    }
    for index, edge in enumerate(edges):
        output[edge.left_table].append((edge.right_table, index, edge.cost))
        output[edge.right_table].append((edge.left_table, index, edge.cost))
    for values in output.values():
        values.sort(key=lambda value: (value[2], value[0], value[1]))
    return output


def _identifier_tokens(value: str) -> set[str]:
    expanded = re.sub(r"([a-z0-9])([A-Z])", r"\1 \2", str(value))
    return {
        token
        for token in re.findall(r"[a-z0-9]+", expanded.casefold())
        if token not in {"id", "ids", "api", "key", "fk", "pk"}
    }


def _relationship_role_tokens(roles: Iterable[str]) -> set[str]:
    tokens = set().union(*(_identifier_tokens(role) for role in roles))
    # Small relation-role aliases make explicit wording comparable with common
    # FK names without inventing an entity or measure binding.
    if tokens & {"created", "create", "posted", "post", "author"}:
        tokens.add("owner")
    if tokens & {"edited", "edit", "editor"}:
        tokens.add("editor")
    return tokens


def _condition_parallel_edges_on_roles(
    edges: list[PhysicalJoinEdge],
    role_bindings: dict[str, list[dict[str, Any]]],
) -> list[PhysicalJoinEdge]:
    """Break multi-FK table-pair ties with explicit query relation words.

    Declared FKs certify endpoints, not which role-distinct FK the question
    requests.  The adjustment is applied only among parallel precise edges and
    only when their identifiers have different overlap with question roles.
    """

    role_tokens = _relationship_role_tokens(role_bindings)
    by_pair: dict[tuple[str, str], list[int]] = {}
    for index, edge in enumerate(edges):
        if edge.precise:
            by_pair.setdefault(edge.table_pair, []).append(index)
    output = list(edges)
    for indices in by_pair.values():
        if len(indices) < 2:
            continue
        overlaps = {
            index: len(
                role_tokens
                & (
                    _identifier_tokens(edges[index].left_column)
                    | _identifier_tokens(edges[index].right_column)
                )
            )
            for index in indices
        }
        best = max(overlaps.values(), default=0)
        worst = min(overlaps.values(), default=0)
        if best <= worst:
            continue
        for index in indices:
            regret = best - overlaps[index]
            if regret:
                output[index] = replace(
                    edges[index],
                    cost=edges[index].cost + 0.12 * regret,
                )
    output.sort(key=lambda edge: (edge.cost, edge.signature, edge.evidence_types))
    return output


def _shortest_path(
    adjacency: dict[str, list[tuple[str, int, float]]],
    source: str,
    target: str,
) -> tuple[float, tuple[int, ...]] | None:
    if source == target:
        return 0.0, ()
    queue: list[tuple[float, int, str, tuple[int, ...]]] = [
        (0.0, 0, source, ())
    ]
    best: dict[str, tuple[float, int]] = {source: (0.0, 0)}
    while queue:
        cost, hops, table, path = heapq.heappop(queue)
        if (cost, hops) > best.get(table, (math.inf, 10**9)):
            continue
        if table == target:
            return cost, path
        for neighbor, edge_id, edge_cost in adjacency.get(table, []):
            candidate = (cost + edge_cost, hops + 1)
            if candidate >= best.get(neighbor, (math.inf, 10**9)):
                continue
            best[neighbor] = candidate
            heapq.heappush(
                queue, (candidate[0], candidate[1], neighbor, (*path, edge_id))
            )
    return None


class _UnionFind:
    def __init__(self, values: Iterable[str]) -> None:
        self.parent = {value: value for value in values}

    def find(self, value: str) -> str:
        parent = self.parent[value]
        if parent != value:
            self.parent[value] = self.find(parent)
        return self.parent[value]

    def union(self, left: str, right: str) -> bool:
        left_root = self.find(left)
        right_root = self.find(right)
        if left_root == right_root:
            return False
        self.parent[right_root] = left_root
        return True


def _metric_tree(
    terminals: list[str],
    adjacency: dict[str, list[tuple[str, int, float]]],
    edges: list[PhysicalJoinEdge],
    *,
    path_cache: dict[
        tuple[str, str], tuple[float, tuple[int, ...]] | None
    ] | None = None,
) -> tuple[tuple[int, ...], tuple[str, ...]]:
    unique = list(dict.fromkeys(terminals))
    if len(unique) <= 1:
        return (), ()
    closure: list[tuple[float, str, str, tuple[int, ...]]] = []
    disconnected: list[str] = []
    for index, left in enumerate(unique):
        for right in unique[index + 1 :]:
            key = tuple(sorted((left, right)))
            if path_cache is not None and key in path_cache:
                path = path_cache[key]
            else:
                path = _shortest_path(adjacency, left, right)
                if path_cache is not None:
                    path_cache[key] = path
            if path is not None:
                closure.append((path[0], left, right, path[1]))
    terminal_union = _UnionFind(unique)
    selected: list[int] = []
    for _, left, right, path in sorted(closure):
        if not terminal_union.union(left, right):
            continue
        selected.extend(path)
    root_component = terminal_union.find(unique[0])
    disconnected = [
        table for table in unique[1:] if terminal_union.find(table) != root_component
    ]

    involved_tables = set(unique)
    for edge_id in selected:
        involved_tables.update(
            (edges[edge_id].left_table, edges[edge_id].right_table)
        )
    tree_union = _UnionFind(involved_tables)
    tree_edges: list[int] = []
    for edge_id in sorted(set(selected), key=lambda value: (edges[value].cost, value)):
        edge = edges[edge_id]
        if tree_union.union(edge.left_table, edge.right_table):
            tree_edges.append(edge_id)

    # Remove bridge leaves. They cannot lie on a path between required terminals.
    required = set(unique)
    changed = True
    while changed:
        changed = False
        degree: dict[str, int] = {}
        for edge_id in tree_edges:
            edge = edges[edge_id]
            degree[edge.left_table] = degree.get(edge.left_table, 0) + 1
            degree[edge.right_table] = degree.get(edge.right_table, 0) + 1
        leaves = {table for table, value in degree.items() if value == 1 and table not in required}
        if leaves:
            tree_edges = [
                edge_id
                for edge_id in tree_edges
                if edges[edge_id].left_table not in leaves
                and edges[edge_id].right_table not in leaves
            ]
            changed = True
    return tuple(tree_edges), tuple(disconnected)


def _role_groups(
    role_bindings: dict[str, list[dict[str, Any]]],
    raw_tables: set[str],
    *,
    limit_per_role: int = 4,
) -> list[tuple[str, list[RoleCandidate]]]:
    groups: list[tuple[str, list[RoleCandidate]]] = []
    for role, values in role_bindings.items():
        # Literal values are grounded through exact database probes.  Treating
        # an ungrounded number/string embedding as a structural graph terminal
        # previously certified mappings such as ``1999 -> circuitId``.
        if str(role).casefold().startswith("literal role:"):
            continue
        candidates: list[RoleCandidate] = []
        observed_tables: set[str] = set()
        values = [
            value
            for value in values
            if float(
                (value.get("semantic_alignment") or {}).get("score", 0.0)
            )
            >= 0
        ]
        ranked = sorted(
            values,
            key=lambda value: (
                -float(
                    (value.get("semantic_alignment") or {}).get(
                        "score", 0.0
                    )
                ),
                -float(value.get("role_rrf", 0.0)),
                str(value.get("physical_identifier") or ""),
            ),
        )
        for rank, value in enumerate(ranked):
            table = str(value.get("physical_table") or "")
            identifier = str(value.get("physical_identifier") or "")
            if table not in raw_tables or table in observed_tables or not identifier:
                continue
            observed_tables.add(table)
            candidates.append(
                RoleCandidate(
                    role=str(role),
                    physical_identifier=identifier,
                    table=table,
                    score=float(value.get("role_rrf", 0.0)),
                    rank=rank,
                    evidence_kind=str(value.get("evidence_kind") or ""),
                    evidence_candidate_id=str(
                        value.get("evidence_candidate_id") or ""
                    ),
                    semantic_alignment=float(
                        (value.get("semantic_alignment") or {}).get(
                            "score", 0.0
                        )
                    ),
                    semantic_alignment_status=str(
                        (value.get("semantic_alignment") or {}).get(
                            "status", "opaque_or_unresolved"
                        )
                    ),
                    required_companion_identifiers=tuple(
                        str(identifier)
                        for identifier in value.get(
                            "required_companion_identifiers"
                        )
                        or []
                    ),
                )
            )
            if len(candidates) >= limit_per_role:
                break
        if candidates:
            groups.append((str(role), candidates))
    return groups[:8]


def _choose_tree(
    *,
    groups: list[tuple[str, list[RoleCandidate]]],
    required_tables: list[str],
    fallback_tables: list[str],
    raw_tables: set[str],
    edges: list[PhysicalJoinEdge],
) -> tuple[_TreeCandidate, dict[str, Any]]:
    """Jointly choose role alternatives and their shared relationship tree.

    The previous implementation fixed a root and independently selected the
    nearest candidate for every role.  That optimizes a sum of root distances,
    not the cost of the *shared* tree, and can therefore erase the graph method's
    central interaction.  This search expands assignments role by role, first
    preserves the strongest explicit lexical binding available for every role,
    then scores the shared metric-closure tree among semantically tied choices.
    A shorter tree must never erase positive field-level role evidence.
    """

    adjacency = _adjacency(raw_tables, edges)
    component_by_table: dict[str, int] = {}
    components: list[list[str]] = []
    for seed in sorted(raw_tables):
        if seed in component_by_table:
            continue
        component_id = len(components)
        queue = [seed]
        component_by_table[seed] = component_id
        values: list[str] = []
        while queue:
            table = queue.pop(0)
            values.append(table)
            for neighbor, _, _ in adjacency.get(table, []):
                if neighbor in component_by_table:
                    continue
                component_by_table[neighbor] = component_id
                queue.append(neighbor)
        components.append(sorted(values))

    relevant_tables = list(
        dict.fromkeys(
            [
                candidate.table
                for _, candidates in groups
                for candidate in candidates
            ]
            + list(required_tables)
            + list(fallback_tables)
        )
    )
    component_ids = list(
        dict.fromkeys(
            component_by_table[table]
            for table in relevant_tables
            if table in component_by_table
        )
    )
    if not component_ids:
        empty = _TreeCandidate(
            "", (), tuple(role for role, _ in groups), (), (10**9,)
        )
        return empty, {
            "strategy": "semantic_first_bounded_joint_role_binding_steiner_v3",
            "beam_width": 512,
            "evaluated_assignments": 0,
            "pruned_assignments": 0,
            "components_considered": 0,
        }

    beam_width = 512
    evaluated = 0
    pruned = 0
    best: _TreeCandidate | None = None
    for component_id in component_ids:
        component = set(components[component_id])
        required_here = [table for table in required_tables if table in component]
        required_elsewhere = [
            table for table in required_tables if table not in component
        ]
        fallback_here = [table for table in fallback_tables if table in component]
        reachable_groups: list[tuple[str, list[RoleCandidate]]] = []
        unresolved_roles: list[str] = []
        for role, candidates in groups:
            reachable = [candidate for candidate in candidates if candidate.table in component]
            if reachable:
                reachable_groups.append((role, reachable))
            else:
                unresolved_roles.append(role)

        best_semantic_alignment = {
            role: max(candidate.semantic_alignment for candidate in candidates)
            for role, candidates in reachable_groups
        }

        def semantic_regret(
            choices: tuple[RoleCandidate, ...],
        ) -> tuple[int, float]:
            regrets = [
                max(
                    0.0,
                    best_semantic_alignment[choice.role]
                    - choice.semantic_alignment,
                )
                for choice in choices
            ]
            return (
                sum(regret > 1e-9 for regret in regrets),
                round(sum(regrets), 8),
            )

        path_cache: dict[
            tuple[str, str], tuple[float, tuple[int, ...]] | None
        ] = {}
        tree_cache: dict[
            tuple[str, ...], tuple[tuple[int, ...], tuple[str, ...]]
        ] = {}

        def tree_for(tables: list[str]) -> tuple[tuple[int, ...], tuple[str, ...]]:
            key = tuple(sorted(set(tables)))
            if key not in tree_cache:
                tree_cache[key] = _metric_tree(
                    list(key), adjacency, edges, path_cache=path_cache
                )
            return tree_cache[key]

        def state_key(choices: tuple[RoleCandidate, ...]) -> tuple[Any, ...]:
            terminals = [*required_here, *[choice.table for choice in choices]]
            edge_ids, disconnected = tree_for(terminals)
            selected_edges = [edges[index] for index in edge_ids]
            terminal_set = set(terminals)
            selected_tables = terminal_set | {
                table
                for edge in selected_edges
                for table in (edge.left_table, edge.right_table)
            }
            suboptimal_roles, alignment_regret = semantic_regret(choices)
            return (
                len(disconnected),
                suboptimal_roles,
                alignment_regret,
                sum(not edge.precise for edge in selected_edges),
                sum(edge.evidence_class == "compatible" for edge in selected_edges),
                round(
                    sum(edge.cost for edge in selected_edges)
                    + 0.18 * sum(choice.rank for choice in choices),
                    8,
                ),
                len(selected_tables - terminal_set),
                sum(choice.rank for choice in choices),
                len(selected_edges),
                tuple(choice.table for choice in choices),
                tuple(choice.physical_identifier for choice in choices),
            )

        frontier: list[tuple[RoleCandidate, ...]] = [()]
        for _, options in reachable_groups:
            expanded = [
                (*state, option)
                for state in frontier
                for option in options
            ]
            evaluated += len(expanded)
            # A table tuple uniquely identifies the candidate for each role
            # because _role_groups retains at most one field per role/table.
            deduplicated: dict[tuple[str, ...], tuple[RoleCandidate, ...]] = {}
            for state in expanded:
                key = tuple(choice.table for choice in state)
                previous = deduplicated.get(key)
                if previous is None or state_key(state) < state_key(previous):
                    deduplicated[key] = state
            ranked = sorted(deduplicated.values(), key=state_key)
            if len(ranked) > beam_width:
                pruned += len(ranked) - beam_width
            frontier = ranked[:beam_width]

        if not frontier:
            frontier = [()]
        for choices in frontier:
            terminals = [*required_here, *[choice.table for choice in choices]]
            if not groups:
                terminals.extend(fallback_here)
            terminals = list(dict.fromkeys(terminals))
            if not terminals:
                continue
            edge_ids, disconnected = tree_for(terminals)
            selected_edges = [edges[index] for index in edge_ids]
            selected_tables = set(terminals) | {
                table
                for edge in selected_edges
                for table in (edge.left_table, edge.right_table)
            }
            root_priority = [
                *required_here,
                *[choice.table for choice in choices],
                *fallback_here,
            ]
            root = next(value for value in root_priority if value in component)
            unresolved = [
                *unresolved_roles,
                *required_elsewhere,
                *disconnected,
            ]
            suboptimal_roles, alignment_regret = semantic_regret(choices)
            role_penalty = 0.18 * sum(choice.rank for choice in choices)
            objective = (
                len(unresolved),
                suboptimal_roles,
                alignment_regret,
                sum(not edge.precise for edge in selected_edges),
                sum(edge.evidence_class == "compatible" for edge in selected_edges),
                round(sum(edge.cost for edge in selected_edges) + role_penalty, 8),
                len(selected_tables - set(terminals)),
                sum(choice.rank for choice in choices),
                len(selected_edges),
                root,
                tuple(choice.physical_identifier for choice in choices),
            )
            candidate = _TreeCandidate(
                root=root,
                role_choices=choices,
                unresolved_roles=tuple(unresolved),
                edge_ids=edge_ids,
                objective=objective,
            )
            if best is None or candidate.objective < best.objective:
                best = candidate
    assert best is not None
    return best, {
        "strategy": "semantic_first_bounded_joint_role_binding_steiner_v3",
        "beam_width": beam_width,
        "evaluated_assignments": evaluated,
        "pruned_assignments": pruned,
        "components_considered": len(component_ids),
    }


def _orient_tree(
    root: str,
    edge_ids: tuple[int, ...],
    edges: list[PhysicalJoinEdge],
) -> tuple[list[str], list[dict[str, Any]]]:
    if not root:
        return [], []
    adjacency: dict[str, list[tuple[str, int]]] = {}
    for edge_id in edge_ids:
        edge = edges[edge_id]
        adjacency.setdefault(edge.left_table, []).append((edge.right_table, edge_id))
        adjacency.setdefault(edge.right_table, []).append((edge.left_table, edge_id))
    table_order = [root]
    ordered_edges: list[dict[str, Any]] = []
    queue = [root]
    visited = {root}
    while queue:
        parent = queue.pop(0)
        for child, edge_id in sorted(adjacency.get(parent, [])):
            if child in visited:
                continue
            visited.add(child)
            queue.append(child)
            table_order.append(child)
            edge = edges[edge_id]
            if edge.left_table == parent:
                parent_column, child_column = edge.left_column, edge.right_column
                traversal = "left_to_right"
            else:
                parent_column, child_column = edge.right_column, edge.left_column
                traversal = "right_to_left"
            on_sql = ""
            if edge.precise:
                on_sql = (
                    f"{_quote(parent)}.{_quote(parent_column)} = "
                    f"{_quote(child)}.{_quote(child_column)}"
                )
            ordered_edges.append(
                {
                    "step": len(ordered_edges) + 1,
                    "parent_table": parent,
                    "child_table": child,
                    "parent_column": parent_column,
                    "child_column": child_column,
                    "left": (
                        f"{edge.left_table}.{edge.left_column}"
                        if edge.left_column
                        else edge.left_table
                    ),
                    "right": (
                        f"{edge.right_table}.{edge.right_column}"
                        if edge.right_column
                        else edge.right_table
                    ),
                    "on_sql": on_sql,
                    "traversal": traversal,
                    "score": round(edge.score, 4),
                    "cost": round(edge.cost, 4),
                    "evidence_class": edge.evidence_class,
                    "evidence_types": list(edge.evidence_types),
                    "provenance_ids": list(edge.provenance_ids[:6]),
                    "physical_join_columns_known": edge.precise,
                    "certified": edge.precise
                    and edge.evidence_class
                    in {
                        "declared",
                        "evolution_key",
                    },
                }
            )
    return table_order, ordered_edges


def compile_minimal_join_tree(
    *,
    raw_documents: list[CatalogDocument],
    ontology_edges: list[dict[str, Any]],
    role_bindings: dict[str, list[dict[str, Any]]],
    required_tables: list[str] | None = None,
    fallback_tables: list[str] | None = None,
) -> dict[str, Any]:
    """Return a deterministic role assignment and physical join-tree certificate."""

    raw_tables, edges = normalize_join_edges(
        raw_documents=raw_documents, ontology_edges=ontology_edges
    )
    edges = _condition_parallel_edges_on_roles(edges, role_bindings)
    rejected_semantic_roles = [
        role
        for role, values in role_bindings.items()
        if not str(role).casefold().startswith("literal role:")
        and values
        and all(
            float(
                (value.get("semantic_alignment") or {}).get("score", 0.0)
            )
            < 0
            for value in values
        )
    ]
    groups = _role_groups(role_bindings, set(raw_tables))
    fallback = list(
        dict.fromkeys(
            table for table in fallback_tables or [] if table in raw_tables
        )
    )[:8]
    required = list(
        dict.fromkeys(
            table for table in required_tables or [] if table in raw_tables
        )
    )[:12]
    chosen, optimizer = _choose_tree(
        groups=groups,
        required_tables=required,
        fallback_tables=fallback,
        raw_tables=set(raw_tables),
        edges=edges,
    )
    table_order, ordered_edges = _orient_tree(chosen.root, chosen.edge_ids, edges)
    chosen_tables = list(dict.fromkeys(choice.table for choice in chosen.role_choices))
    terminal_tables = list(
        dict.fromkeys([*chosen_tables, *required] or fallback)
    )
    terminal_set = set(terminal_tables)
    bridge_tables = [table for table in table_order if table not in terminal_set]
    unresolved = list(
        dict.fromkeys([*chosen.unresolved_roles, *rejected_semantic_roles])
    )
    precise = all(edge["physical_join_columns_known"] for edge in ordered_edges)
    certified = all(edge["certified"] for edge in ordered_edges)
    join_skeleton = ""
    if table_order and precise and len(ordered_edges) == len(table_order) - 1:
        lines = [f"FROM {_quote(table_order[0])}"]
        lines.extend(
            f"JOIN {_quote(edge['child_table'])} ON {edge['on_sql']}"
            for edge in ordered_edges
        )
        join_skeleton = "\n".join(lines)

    role_choices = {
        choice.role: {
            "physical_identifier": choice.physical_identifier,
            "physical_table": choice.table,
            "role_rrf": round(choice.score, 8),
            "candidate_rank": choice.rank,
            "evidence_kind": choice.evidence_kind,
            "evidence_candidate_id": choice.evidence_candidate_id,
            "semantic_alignment": round(choice.semantic_alignment, 8),
            "semantic_alignment_status": choice.semantic_alignment_status,
            "required_companion_identifiers": list(
                choice.required_companion_identifiers
            ),
        }
        for choice in chosen.role_choices
    }
    non_structural_roles = [
        role
        for role in role_bindings
        if str(role).casefold().startswith("literal role:")
    ]
    certificate_basis = {
        "root": chosen.root,
        "role_choices": role_choices,
        "table_order": table_order,
        "ordered_edges": ordered_edges,
        "unresolved": unresolved,
    }
    return {
        "compiler": "role_grounded_minimal_join_tree_v3",
        "root_table": chosen.root or None,
        "terminal_role_count": len(groups),
        "covered_role_count": len(role_choices),
        "role_choices": role_choices,
        "non_structural_roles": non_structural_roles,
        "terminal_tables": terminal_tables,
        "template_required_tables": required,
        "template_advisory_tables": fallback,
        "bridge_tables": bridge_tables,
        "topological_table_order": table_order,
        "ordered_join_edges": ordered_edges,
        # Compatibility with the existing grounding/planner payload.
        "physical_join_edges": ordered_edges,
        "join_skeleton_sql": join_skeleton,
        "unresolved_roles": unresolved,
        "disconnected_terminals": [
            value for value in unresolved if value in raw_tables
        ],
        "certificate": {
            "all_roles_connected": not unresolved,
            "all_selected_roles_not_lexically_contradicted": all(
                choice.semantic_alignment >= 0
                for choice in chosen.role_choices
            ),
            "semantic_role_bindings_logically_certified": False,
            "role_binding_scope": (
                "retrieval hypotheses; certificate covers relationship "
                "connectivity and physical join endpoints only"
            ),
            "optimization_priority": (
                "connected_role_coverage_then_explicit_semantic_alignment_"
                "then_minimal_relationship_tree"
            ),
            "all_join_columns_known": precise,
            "all_edges_relationship_certified": certified,
            "minimal_nonterminal_leaves": True,
            "objective": list(chosen.objective),
            "optimizer": optimizer,
            "join_tree_sha256": sha256(
                json.dumps(
                    certificate_basis,
                    ensure_ascii=False,
                    sort_keys=True,
                    separators=(",", ":"),
                ).encode()
            ).hexdigest(),
        },
        "edge_inventory": {
            "relationship_edges": len(edges),
            "precise_edges": sum(edge.precise for edge in edges),
            "alternative_key_pairs": sum(
                count > 1
                for count in {
                    pair: sum(edge.table_pair == pair for edge in edges)
                    for pair in {edge.table_pair for edge in edges}
                }.values()
            ),
        },
        "uses_evaluator_gold": False,
    }
