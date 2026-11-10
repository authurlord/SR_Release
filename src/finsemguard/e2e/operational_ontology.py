"""Database-local operational ontology for query-time schema compilation.

The ontology is intentionally narrower than a business ontology.  It contains typed
physical nodes and evidence-bearing relationship edges that can change schema
retrieval, bridge-table restoration, or SQL join planning.  It never reads evaluator
gold and does not use an LLM judge.
"""

from __future__ import annotations

from dataclasses import dataclass
from hashlib import sha256
import heapq
import json
import math
import re
from typing import Any, Iterable

import sqlglot
from sqlglot import exp

from finsemguard.e2e.livesqlbench import CatalogDocument


GENERIC_COMPATIBILITY_COLUMNS = {
    "date",
    "id",
    "name",
    "status",
    "time",
    "type",
    "value",
}


def _endpoint(value: str) -> tuple[str, str] | None:
    table, separator, column = str(value).rpartition(".")
    if not separator or not table.strip() or not column.strip():
        return None
    if column.strip().casefold() in {"none", "null", "?"}:
        return None
    return table.strip(), column.strip()


def _normalized_name(value: str) -> str:
    spaced = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "_", value)
    return re.sub(r"[^a-z0-9]+", "_", spaced.casefold()).strip("_")


def _value_key(value: Any) -> tuple[str, Any]:
    if value is None:
        return "null", None
    if isinstance(value, bool):
        return "number", int(value)
    if isinstance(value, (int, float)):
        return "number", round(float(value), 8)
    return "text", str(value).strip().casefold()


@dataclass(frozen=True)
class OntologyEdge:
    context: str
    left_table: str
    left_column: str
    right_table: str
    right_column: str
    score: float
    evidence_types: tuple[str, ...]
    provenance_ids: tuple[str, ...]

    @property
    def left(self) -> str:
        return f"{self.left_table}.{self.left_column}"

    @property
    def right(self) -> str:
        return f"{self.right_table}.{self.right_column}"

    @property
    def table_pair(self) -> tuple[str, str]:
        return tuple(sorted((self.left_table, self.right_table)))  # type: ignore[return-value]

    def as_dict(self) -> dict[str, Any]:
        return {
            "left": self.left,
            "right": self.right,
            "score": round(self.score, 4),
            "evidence_types": list(self.evidence_types),
            "provenance_ids": list(self.provenance_ids),
        }


@dataclass(frozen=True)
class OntologyExpansion:
    context: str
    terminal_tables: tuple[str, ...]
    bridge_tables: tuple[str, ...]
    edges: tuple[OntologyEdge, ...]

    def audit(self) -> dict[str, Any]:
        return {
            "context": self.context,
            "terminal_tables": list(self.terminal_tables),
            "bridge_tables": list(self.bridge_tables),
            "edges": [edge.as_dict() for edge in self.edges],
            "edge_count": len(self.edges),
            "uses_evaluator_gold": False,
        }


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


class OperationalOntology:
    """Typed, provenance-bearing physical relationship graph."""

    def __init__(
        self,
        edges: list[OntologyEdge],
        inventory: dict[str, Any],
        evidence_documents: list[CatalogDocument] | None = None,
        document_bindings: dict[str, tuple[str, ...]] | None = None,
    ) -> None:
        self.edges = tuple(edges)
        self.inventory = inventory
        self.evidence_documents = tuple(evidence_documents or [])
        self.document_bindings = dict(document_bindings or {})
        evidence_ids = [row.candidate_id for row in self.evidence_documents]
        if len(set(evidence_ids)) != len(evidence_ids):
            raise ValueError("duplicate operational ontology evidence document IDs")
        self.by_context: dict[str, list[OntologyEdge]] = {}
        for edge in self.edges:
            self.by_context.setdefault(edge.context, []).append(edge)

    @staticmethod
    def _canonical_edge(
        left: tuple[str, str], right: tuple[str, str]
    ) -> tuple[tuple[str, str], tuple[str, str]]:
        return (left, right) if left <= right else (right, left)

    @classmethod
    def from_recovery_inputs(
        cls,
        table_inputs: list[dict[str, Any]],
        knowledge_rows: list[dict[str, Any]] | None = None,
        *,
        sql_dialect: str = "sqlite",
    ) -> "OperationalOntology":
        inventory: dict[str, dict[str, dict[str, dict[str, Any]]]] = {}
        rows_by_context: dict[str, list[dict[str, Any]]] = {}
        for row in table_inputs:
            context = str(row["schema_context"])
            table = str(row["physical_table"])
            rows_by_context.setdefault(context, []).append(row)
            tables = inventory.setdefault(context, {})
            if table in tables:
                raise ValueError(f"duplicate ontology table input: {context}::{table}")
            tables[table] = {
                str(column["physical_column"]): {
                    "declared_type": str(column.get("declared_type") or "unknown"),
                    "primary_key": bool(column.get("primary_key", False)),
                    "observed_values": list(column.get("observed_values") or []),
                }
                for column in row.get("columns") or []
            }

        merged: dict[
            tuple[str, tuple[str, str], tuple[str, str]], dict[str, Any]
        ] = {}
        evidence_documents: list[CatalogDocument] = []
        document_bindings: dict[str, tuple[str, ...]] = {}

        def add(
            context: str,
            left: tuple[str, str],
            right: tuple[str, str],
            score: float,
            evidence_type: str,
            provenance_id: str,
        ) -> None:
            if left[0] == right[0] or left[0] not in inventory.get(context, {}):
                return
            if right[0] not in inventory.get(context, {}):
                return
            left_columns = inventory[context][left[0]]
            right_columns = inventory[context][right[0]]
            if left[1] not in left_columns or right[1] not in right_columns:
                return
            canonical_left, canonical_right = cls._canonical_edge(left, right)
            key = (context, canonical_left, canonical_right)
            item = merged.setdefault(
                key,
                {
                    "score": 0.0,
                    "evidence_types": set(),
                    "provenance_ids": set(),
                },
            )
            item["score"] = max(float(item["score"]), min(max(score, 0.0), 1.0))
            item["evidence_types"].add(evidence_type)
            if provenance_id:
                item["provenance_ids"].add(provenance_id)

        for context, rows in rows_by_context.items():
            for row in rows:
                for relation in row.get("relationships") or []:
                    left = _endpoint(str(relation.get("source") or ""))
                    right = _endpoint(str(relation.get("target") or ""))
                    if left and right:
                        add(
                            context,
                            left,
                            right,
                            1.0,
                            "declared_or_materialized_relationship",
                            str(relation.get("evidence_id") or ""),
                        )

            # The same target-disjoint history row is attached to every physical
            # table it touched.  Preserve those per-table column bindings instead
            # of keeping only the first copy, and expose the actual SQL structure
            # to the downstream agent.  The previous representation retained up
            # to dozens of similar questions but discarded the one artifact that
            # can transfer CTE/window/UNION structure: the historical SQL itself.
            histories: dict[str, dict[str, Any]] = {}
            for row in rows:
                source_table = str(row["physical_table"])
                for history in row.get("target_disjoint_workload") or []:
                    history_id = str(history.get("history_id"))
                    item = histories.setdefault(
                        history_id,
                        {"history": history, "physical_columns": set()},
                    )
                    for column in history.get("physical_columns") or []:
                        physical_column = str(column)
                        if physical_column in inventory[context][source_table]:
                            item["physical_columns"].add(
                                f"{source_table}.{physical_column}"
                            )
            for history_id, history_item in histories.items():
                history = dict(history_item["history"])
                sql = str(history.get("sql") or "").strip()
                if not sql:
                    continue
                try:
                    tree = sqlglot.parse_one(sql, read=sql_dialect)
                except Exception:
                    continue
                aliases: dict[str, str] = {}
                for table_node in tree.find_all(exp.Table):
                    physical = str(table_node.name)
                    if physical not in inventory.get(context, {}):
                        # sqlglot also exposes references to CTE names as Table
                        # nodes.  They are query-local aliases, not physical
                        # schema anchors, and previously polluted retrieval.
                        continue
                    aliases[physical.casefold()] = physical
                    alias = str(table_node.alias_or_name)
                    aliases[alias.casefold()] = physical
                physical_tables = tuple(sorted(set(aliases.values())))
                physical_columns: set[str] = set(history_item["physical_columns"])
                for column_node in tree.find_all(exp.Column):
                    physical_table = aliases.get(str(column_node.table).casefold())
                    physical_column = str(column_node.name)
                    if (
                        physical_table in inventory.get(context, {})
                        and physical_column in inventory[context][physical_table]
                    ):
                        physical_columns.add(
                            f"{physical_table}.{physical_column}"
                        )
                for equality in tree.find_all(exp.EQ):
                    left_node = equality.left
                    right_node = equality.right
                    if not isinstance(left_node, exp.Column) or not isinstance(
                        right_node, exp.Column
                    ):
                        continue
                    left_table = aliases.get(str(left_node.table).casefold())
                    right_table = aliases.get(str(right_node.table).casefold())
                    if not left_table or not right_table:
                        continue
                    add(
                        context,
                        (left_table, str(left_node.name)),
                        (right_table, str(right_node.name)),
                        0.95,
                        "target_disjoint_historical_join",
                        str(history.get("evidence_id") or history_id),
                    )
                history_payload = {
                    "ontology_kind": "target_disjoint_workload_pattern",
                    "question_pattern": str(history.get("question") or "").strip(),
                    "sql_template": sql,
                    "physical_tables": list(physical_tables),
                    "physical_columns": sorted(physical_columns),
                    "provenance_id": str(
                        history.get("evidence_id") or history_id
                    ),
                    "target_disjoint": True,
                }
                # Keep question and SQL first: BGE embeds the leading question,
                # while the prompt receives the transferable SQL immediately
                # after it.  This is intentionally not key-sorted.
                rendered = json.dumps(history_payload, ensure_ascii=False)
                digest = sha256(
                    f"{context}\0{history_id}\0{rendered}".encode()
                ).hexdigest()[:20]
                candidate_id = f"workload::{context}::{digest}"
                bound_ids = [
                    f"table::{context}::{table}" for table in physical_tables
                ]
                bound_ids.extend(
                    f"column::{context}::{identifier.rsplit('.', 1)[0]}::"
                    f"{identifier.rsplit('.', 1)[1]}"
                    for identifier in sorted(physical_columns)
                )
                evidence_documents.append(
                    CatalogDocument(
                        candidate_id=candidate_id,
                        database_id=context,
                        kind="knowledge",
                        table=(physical_tables[0] if len(physical_tables) == 1 else None),
                        name="target-disjoint workload pattern",
                        text=rendered,
                    )
                )
                document_bindings[candidate_id] = tuple(dict.fromkeys(bound_ids))

            tables = inventory[context]
            table_names = sorted(tables)
            for left_index, left_table in enumerate(table_names):
                for right_table in table_names[left_index + 1 :]:
                    left_by_name = {
                        _normalized_name(column): column for column in tables[left_table]
                    }
                    right_by_name = {
                        _normalized_name(column): column for column in tables[right_table]
                    }
                    for normalized in sorted(set(left_by_name) & set(right_by_name)):
                        if normalized in GENERIC_COMPATIBILITY_COLUMNS:
                            continue
                        left_column = left_by_name[normalized]
                        right_column = right_by_name[normalized]
                        left_profile = tables[left_table][left_column]
                        right_profile = tables[right_table][right_column]
                        left_values = {
                            _value_key(value)
                            for value in left_profile["observed_values"]
                            if value is not None
                        }
                        right_values = {
                            _value_key(value)
                            for value in right_profile["observed_values"]
                            if value is not None
                        }
                        if not left_values or not right_values:
                            continue
                        overlap = len(left_values & right_values) / min(
                            len(left_values), len(right_values)
                        )
                        if overlap < 0.6:
                            continue
                        score = min(
                            0.85,
                            0.55
                            + 0.2 * overlap
                            + 0.1
                            * bool(
                                left_profile["primary_key"]
                                or right_profile["primary_key"]
                            ),
                        )
                        add(
                            context,
                            (left_table, left_column),
                            (right_table, right_column),
                            score,
                            "profile_name_value_compatibility",
                            "deterministic_profile_overlap",
                        )

        # External KB rows are deliberately interpreted through a small allowlist.
        # Unknown keys (including any evaluator-only material) never enter prompts.
        for index, raw in enumerate(knowledge_rows or []):
            context = str(raw.get("schema_context") or "").strip()
            if context not in inventory:
                continue
            source = _endpoint(str(raw.get("source") or ""))
            target = _endpoint(str(raw.get("target") or ""))
            physical = _endpoint(str(raw.get("physical_identifier") or ""))
            physical_many = [
                endpoint
                for endpoint in (
                    _endpoint(str(value))
                    for value in raw.get("physical_identifiers") or []
                )
                if endpoint is not None
            ]
            confidence = float(raw.get("confidence", 0.9))
            evidence_id = str(raw.get("evidence_id") or f"kb.{index}")
            if source and target:
                add(
                    context,
                    source,
                    target,
                    confidence,
                    "external_knowledge_relationship",
                    evidence_id,
                )
            endpoints = [
                endpoint
                for endpoint in (physical, source, target, *physical_many)
                if endpoint
            ]
            valid_endpoints = [
                endpoint
                for endpoint in endpoints
                if endpoint[0] in inventory[context]
                and endpoint[1] in inventory[context][endpoint[0]]
            ]
            if not valid_endpoints:
                continue
            payload = {
                "ontology_kind": "external_target_isolated_knowledge",
                "physical_identifiers": [
                    f"{table}.{column}" for table, column in valid_endpoints
                ],
                "relation": str(raw.get("relation") or "semantic_mapping"),
                "aliases": [str(value) for value in raw.get("aliases") or []],
                "semantic_type": str(raw.get("semantic_type") or "unknown"),
                "unit": str(raw.get("unit") or ""),
                "formula": str(raw.get("formula") or ""),
                "description": str(raw.get("description") or ""),
                "source_name": str(raw.get("source_name") or "external_kb"),
                "provenance_id": evidence_id,
                "confidence": min(max(confidence, 0.0), 1.0),
                "target_disjoint": True,
            }
            rendered = json.dumps(payload, ensure_ascii=False, sort_keys=True)
            digest = sha256(f"{context}\0{evidence_id}\0{rendered}".encode()).hexdigest()[:20]
            candidate_id = f"kb::{context}::{digest}"
            tables = tuple(dict.fromkeys(table for table, _ in valid_endpoints))
            evidence_documents.append(
                CatalogDocument(
                    candidate_id=candidate_id,
                    database_id=context,
                    kind="knowledge",
                    table=tables[0] if len(tables) == 1 else None,
                    name="external operational ontology assertion",
                    text=rendered,
                )
            )
            document_bindings[candidate_id] = tuple(
                dict.fromkeys(
                    [f"table::{context}::{table}" for table in tables]
                    + [
                        f"column::{context}::{table}::{column}"
                        for table, column in valid_endpoints
                    ]
                )
            )

        edges = [
            OntologyEdge(
                context=context,
                left_table=left[0],
                left_column=left[1],
                right_table=right[0],
                right_column=right[1],
                score=float(item["score"]),
                evidence_types=tuple(sorted(item["evidence_types"])),
                provenance_ids=tuple(sorted(item["provenance_ids"])),
            )
            for (context, left, right), item in sorted(merged.items())
        ]
        return cls(edges, inventory, evidence_documents, document_bindings)

    def augment_documents(
        self, documents: list[CatalogDocument]
    ) -> list[CatalogDocument]:
        """Add searchable workload/KB evidence without changing physical documents."""

        output = list(documents)
        observed = {row.candidate_id for row in output}
        for row in self.evidence_documents:
            if row.candidate_id in observed:
                raise ValueError(
                    f"ontology evidence collides with catalog ID: {row.candidate_id}"
                )
            output.append(row)
            observed.add(row.candidate_id)
        return output

    def prebind_retrieved_evidence(
        self,
        *,
        context: str,
        candidates: list[CatalogDocument],
        all_documents: dict[str, CatalogDocument],
        evidence_limit: int = 2,
        bound_limit: int = 32,
    ) -> tuple[list[CatalogDocument], list[str], list[str]]:
        """Expand top retrieved workload/KB nodes before LLM schema selection.

        Retrieval has already ranked these evidence nodes for the question.  Making
        their physical bindings visible before top-k schema compression prevents the
        selector from seeing a useful historical pattern while silently dropping the
        opaque columns that pattern names.
        """

        if evidence_limit < 0 or bound_limit < 0:
            raise ValueError("prebinding limits must be nonnegative")
        evidence_ids = [
            row.candidate_id
            for row in candidates
            if row.database_id == context
            and row.candidate_id in self.document_bindings
        ][:evidence_limit]
        bound_ids: list[str] = []
        for evidence_id in evidence_ids:
            for candidate_id in self.document_bindings[evidence_id]:
                if candidate_id not in bound_ids and candidate_id in all_documents:
                    bound_ids.append(candidate_id)
                    if len(bound_ids) >= bound_limit:
                        break
            if len(bound_ids) >= bound_limit:
                break
        output = list(candidates)
        observed = {row.candidate_id for row in output}
        for candidate_id in bound_ids:
            if candidate_id not in observed:
                output.append(all_documents[candidate_id])
                observed.add(candidate_id)
        return output, evidence_ids, bound_ids

    @staticmethod
    def _edge_cost(edge: OntologyEdge) -> float:
        # Every hop has a cost; stronger evidence is preferred without allowing a
        # long chain of weak similarities to beat a short declared relationship.
        return 0.25 + -math.log(max(edge.score, 0.05))

    def _shortest_path(
        self,
        context: str,
        start: str,
        goal: str,
    ) -> tuple[float, list[OntologyEdge]] | None:
        adjacency: dict[str, list[tuple[str, OntologyEdge]]] = {}
        for edge in self.by_context.get(context, []):
            adjacency.setdefault(edge.left_table, []).append((edge.right_table, edge))
            adjacency.setdefault(edge.right_table, []).append((edge.left_table, edge))
        queue: list[tuple[float, str, tuple[int, ...]]] = [(0.0, start, ())]
        best = {start: 0.0}
        edge_list = self.by_context.get(context, [])
        edge_index = {id(edge): index for index, edge in enumerate(edge_list)}
        while queue:
            cost, table, path_indices = heapq.heappop(queue)
            if cost > best.get(table, float("inf")):
                continue
            if table == goal:
                return cost, [edge_list[index] for index in path_indices]
            for neighbor, edge in adjacency.get(table, []):
                next_cost = cost + self._edge_cost(edge)
                if next_cost >= best.get(neighbor, float("inf")):
                    continue
                best[neighbor] = next_cost
                heapq.heappush(
                    queue,
                    (next_cost, neighbor, (*path_indices, edge_index[id(edge)])),
                )
        return None

    def connect(self, context: str, terminal_tables: Iterable[str]) -> OntologyExpansion:
        terminals = tuple(dict.fromkeys(str(value) for value in terminal_tables))
        if len(terminals) < 2:
            return OntologyExpansion(context, terminals, (), ())
        paths: list[tuple[float, str, str, list[OntologyEdge]]] = []
        for left_index, left in enumerate(terminals):
            for right in terminals[left_index + 1 :]:
                path = self._shortest_path(context, left, right)
                if path is not None:
                    paths.append((path[0], left, right, path[1]))
        union = _UnionFind(terminals)
        selected_edges: list[OntologyEdge] = []
        for _, left, right, path in sorted(paths, key=lambda row: (row[0], row[1], row[2])):
            if not union.union(left, right):
                continue
            for edge in path:
                if edge not in selected_edges:
                    selected_edges.append(edge)
        selected_tables = {
            table
            for edge in selected_edges
            for table in (edge.left_table, edge.right_table)
        }
        bridges = tuple(sorted(selected_tables - set(terminals)))
        return OntologyExpansion(context, terminals, bridges, tuple(selected_edges))

    def expand_documents(
        self,
        *,
        context: str,
        selected_ids: list[str],
        all_documents: dict[str, CatalogDocument],
    ) -> tuple[list[CatalogDocument], OntologyExpansion]:
        selected = [
            all_documents[candidate_id]
            for candidate_id in selected_ids
            if candidate_id in all_documents
        ]
        observed = {document.candidate_id for document in selected}

        def include(candidate_id: str) -> None:
            if candidate_id in all_documents and candidate_id not in observed:
                selected.append(all_documents[candidate_id])
                observed.add(candidate_id)

        # A selected history/KB assertion deterministically restores the physical
        # entities it names before graph connection. This is the actual information
        # path; it is not another same-model self-verification pass.
        for candidate_id in selected_ids:
            for bound_id in self.document_bindings.get(candidate_id, ()):
                include(bound_id)
        terminal_tables = []
        for document in selected:
            table = document.table if document.kind != "table" else document.name
            if table and table not in terminal_tables:
                terminal_tables.append(str(table))
        expansion = self.connect(context, terminal_tables)
        output = list(selected)
        observed = {document.candidate_id for document in output}

        def include(candidate_id: str) -> None:
            if candidate_id in all_documents and candidate_id not in observed:
                output.append(all_documents[candidate_id])
                observed.add(candidate_id)

        for table in expansion.bridge_tables:
            include(f"table::{context}::{table}")
        for edge in expansion.edges:
            include(f"table::{context}::{edge.left_table}")
            include(f"table::{context}::{edge.right_table}")
            include(f"column::{context}::{edge.left_table}::{edge.left_column}")
            include(f"column::{context}::{edge.right_table}::{edge.right_column}")
        if expansion.edges:
            payload = {
                "ontology_kind": "query_operational_relationship_subgraph",
                "physical_join_edges": [edge.as_dict() for edge in expansion.edges],
                "bridge_tables": list(expansion.bridge_tables),
                "semantics": (
                    "Edges are database-local evidence for join planning; use physical "
                    "identifiers exactly and do not invent unstated business relations."
                ),
            }
            rendered = json.dumps(payload, ensure_ascii=False, sort_keys=True)
            digest = sha256(rendered.encode()).hexdigest()[:20]
            output.append(
                CatalogDocument(
                    candidate_id=f"ontology::{context}::{digest}",
                    database_id=context,
                    kind="knowledge",
                    table=None,
                    name="operational ontology join subgraph",
                    text=rendered,
                )
            )
        return output, expansion

    def manifest(self) -> dict[str, Any]:
        evidence_counts: dict[str, int] = {}
        for edge in self.edges:
            for evidence_type in edge.evidence_types:
                evidence_counts[evidence_type] = evidence_counts.get(evidence_type, 0) + 1
        payload = {
            "format": "query_operational_ontology_v1",
            "contexts": len(self.inventory),
            "tables": sum(len(tables) for tables in self.inventory.values()),
            "columns": sum(
                len(columns)
                for tables in self.inventory.values()
                for columns in tables.values()
            ),
            "edges": len(self.edges),
            "evidence_documents": len(self.evidence_documents),
            "workload_documents": sum(
                row.candidate_id.startswith("workload::")
                for row in self.evidence_documents
            ),
            "external_kb_documents": sum(
                row.candidate_id.startswith("kb::")
                for row in self.evidence_documents
            ),
            "evidence_counts": dict(sorted(evidence_counts.items())),
            "uses_evaluator_gold": False,
        }
        payload["sha256"] = sha256(
            json.dumps(
                {
                    "edges": [
                        edge.as_dict() | {"context": edge.context}
                        for edge in self.edges
                    ],
                    "evidence_documents": [
                        {
                            "candidate_id": row.candidate_id,
                            "database_id": row.database_id,
                            "name": row.name,
                            "text": row.text,
                            "bindings": list(
                                self.document_bindings.get(row.candidate_id, ())
                            ),
                        }
                        for row in self.evidence_documents
                    ],
                },
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
            ).encode()
        ).hexdigest()
        return payload
