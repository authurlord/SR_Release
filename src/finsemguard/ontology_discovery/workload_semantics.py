"""Incremental semantic-layer construction from SQL logs alone.

No schema catalogue, column descriptions, NL questions, values, or answers are
required. SQL scopes supply structural evidence; aliases supply semantic hints.
Hints are not promoted to verified business definitions. Contributions belong
to log records, so correcting/retracting a record also updates dependent assets.
"""

from __future__ import annotations

import argparse
from collections import defaultdict
from copy import deepcopy
from hashlib import sha256
import json
from pathlib import Path
from typing import Any

import sqlglot
from sqlglot import exp
from sqlglot.optimizer.scope import Scope, traverse_scope

from finsemguard.e2e.livesqlbench import CatalogDocument
from finsemguard.ontology_discovery.sql_scope_contracts import ScopeContract


def _key(value: Any) -> str:
    return sha256(json.dumps(value, sort_keys=True, ensure_ascii=False).encode()).hexdigest()[:24]


def _bindings(tree: exp.Expression) -> list[str]:
    return sorted({f"{c.table}.{c.name}" for c in tree.find_all(exp.Column) if c.table and not c.is_star})


class _Unresolved(ValueError):
    pass


def extract_sql_evidence(sql: str, context: str, dialect: str = "sqlite") -> dict[str, Any]:
    """Resolve CTE/subquery outputs before learning roles and expressions.

    Ambiguous unqualified columns are retained as unresolved observations. Without
    a catalogue, selecting one of several possible source tables would fabricate
    a mapping. Full programs remain available even when a fragment is unresolved.
    """
    statements = sqlglot.parse(sql, read=dialect)
    if len(statements) != 1 or not isinstance(statements[0], exp.Query):
        raise ValueError("one historical SELECT/UNION query is required per log record")
    tree = statements[0]
    scopes = list(traverse_scope(tree))
    facts: dict[str, dict[str, Any]] = {}
    unresolved: set[str] = set()
    seen_columns: dict[str, set[str]] = defaultdict(set)
    exports: dict[int, dict[str, exp.Expression | None]] = {}
    active_tables: list[str] = []
    upstream_scopes: list[str] = []
    staged_execution = False
    scope_contract: ScopeContract | None = None

    def scope_tables(source: Scope | exp.Expression, visited: frozenset[int] = frozenset()) -> set[str]:
        if isinstance(source, exp.Table):
            return {".".join(p.name for p in source.parts)}
        if not isinstance(source, Scope) or id(source) in visited:
            return set()
        return set().union(*(scope_tables(s, visited | {id(source)}) for _, s in source.selected_sources.values()))

    def add(kind: str, expression: exp.Expression, *, role: str = "", alias: str = "",
            grain: list[str] | None = None, row_context: str = "",
            source_expression: exp.Expression | None = None) -> str:
        physical = _bindings(expression)
        definition = {"schema_context": context, "kind": kind,
                      "expression": expression.sql(dialect=dialect),
                      "physical_identifiers": physical,
                      "physical_tables": sorted({c.table for c in expression.find_all(exp.Column) if c.table})
                          if kind == "column" else active_tables}
        if kind != "column":
            definition.update(grain=grain or [], row_context=row_context,
                              upstream_scopes=upstream_scopes,
                              requires_staged_execution=staged_execution)
            if staged_execution and source_expression is not None:
                # Aggregate/window outputs are values of an upstream relation,
                # not scalar macros that may be flattened into SUM(SUM(...)).
                definition["expression"] = source_expression.sql(dialect=dialect)
        execution_contract = None
        if kind in {"metric", "binding"} and scope_contract is not None and source_expression is not None:
            try:
                execution_contract = scope_contract.computation(source_expression)
            except ValueError:
                pass
        identity_definition = definition
        if execution_contract is not None:
            identity_definition = {"schema_context": context, "kind": kind,
                "computation": execution_contract["formula"], "scope": scope_contract.context}
        identity = "semantic::" + _key(identity_definition)
        definition["consumer_contract_version"] = 1
        if execution_contract is not None:
            definition["execution_contract"] = execution_contract
        fact = facts.setdefault(identity, {"id": identity, **definition, "roles": [], "aliases": []})
        if role and role not in fact["roles"]:
            fact["roles"].append(role)
        if alias and alias not in fact["aliases"]:
            fact["aliases"].append(alias)
        for column in expression.find_all(exp.Column):
            if column.table and not column.is_star:
                seen_columns[column.table].add(column.name)
                if kind != "column":
                    add("column", column, role=role)
        return identity

    for scope in scopes:
        active_tables = sorted(scope_tables(scope))
        sources = {name.casefold(): source for name, (_, source) in scope.selected_sources.items()}
        ancestors: dict[int, Scope] = {}

        def collect_upstream(current: Scope) -> None:
            for _, source in current.selected_sources.values():
                if isinstance(source, Scope) and id(source) not in ancestors:
                    ancestors[id(source)] = source
                    collect_upstream(source)

        collect_upstream(scope)
        upstream_scopes = sorted({s.expression.sql(dialect=dialect) for s in ancestors.values()})
        staged_execution = any(s.expression.find(exp.AggFunc, exp.Window) is not None
            or any(s.expression.args.get(k) is not None for k in ("distinct", "limit", "offset", "group"))
            for s in ancestors.values())
        for source in sources.values():
            if isinstance(source, exp.Table):
                # Keep qualified table identities, not only their leaf name.
                seen_columns[".".join(p.name for p in source.parts)]

        def resolve(expression: exp.Expression, *, output_aliases: bool = False) -> exp.Expression:
            if any(isinstance(n, (exp.Subquery, exp.Select)) for n in expression.walk()):
                raise _Unresolved("nested query expression")

            def replace(node: exp.Expression) -> exp.Expression:
                if not isinstance(node, exp.Column):
                    return node
                if node.is_star:
                    raise _Unresolved("wildcard needs a catalogue")
                if output_aliases and not node.table and node.name.casefold() in resolved_outputs:
                    value = resolved_outputs[node.name.casefold()]
                    if value is None:
                        raise _Unresolved("ambiguous output alias")
                    return value.copy()
                source = sources.get(node.table.casefold()) if node.table else None
                if not node.table:
                    candidates = [s for s in sources.values() if isinstance(s, exp.Table)
                                  or node.name.casefold() in exports.get(id(s), {})]
                    if len(candidates) != 1:
                        raise _Unresolved(f"ambiguous column: {node.sql()}")
                    source = candidates[0]
                if isinstance(source, exp.Table):
                    table = ".".join(p.name for p in source.parts)
                    return exp.column(node.name, table=table, quoted=True)
                if isinstance(source, Scope):
                    value = exports.get(id(source), {}).get(node.name.casefold())
                    if value is not None:
                        return value.copy()
                raise _Unresolved(f"unresolved source: {node.sql()}")

            return expression.copy().transform(replace)

        if not isinstance(scope.expression, exp.Select):
            # UNION output may have multiple physical origins; retain each branch
            # and the complete program without assigning the union a false field.
            exports[id(scope)] = {}
            unresolved.add("set-operation output lineage requires multiple alternatives")
            continue
        select = scope.expression
        try:
            scope_contract = ScopeContract(scope, dialect)
        except ValueError:
            scope_contract = None
        # The relational scope is part of a metric's identity. Identical SUMs at
        # different grains, filters, or join multiplicities must not be merged.
        row_context = select.sql(dialect=dialect)
        resolved_outputs: dict[str, exp.Expression | None] = {}
        for projection in select.expressions:
            expression = projection.this if isinstance(projection, exp.Alias) else projection
            try:
                resolved = resolve(expression)
                if isinstance(resolved, exp.Star):
                    raise _Unresolved("wildcard needs a catalogue")
            except _Unresolved as error:
                unresolved.add(str(error))
                resolved = None
            name = projection.alias_or_name.casefold()
            if name:
                # Duplicate output names do not provide unambiguous lineage.
                resolved_outputs[name] = None if name in resolved_outputs else resolved

        exports[id(scope)] = resolved_outputs
        grain: list[str] = []
        group = select.args.get("group")
        for item in group.expressions if group else []:
            try:
                if isinstance(item, exp.Literal) and item.is_int:
                    position = int(item.this)
                    if not 1 <= position <= len(select.expressions):
                        raise _Unresolved("invalid positional grouping")
                    projection = select.expressions[position - 1]
                    value = resolved_outputs.get(projection.alias_or_name.casefold())
                    if value is None:
                        raise _Unresolved("unresolved positional grouping")
                elif isinstance(item, exp.Column) and not item.table and item.name.casefold() in resolved_outputs:
                    value = resolved_outputs[item.name.casefold()]
                    if value is None:
                        raise _Unresolved("unresolved grouping alias")
                else:
                    value = resolve(item)
                grain.append(value.sql(dialect=dialect))
                add("grouping", value, role="group", row_context=row_context)
            except (_Unresolved, IndexError) as error:
                unresolved.add(str(error))
                grain.append("unresolved:" + item.sql(dialect=dialect))

        for projection in select.expressions:
            expression = projection.this if isinstance(projection, exp.Alias) else projection
            try:
                resolved = resolve(expression)
                if isinstance(resolved, exp.Star):
                    continue
            except _Unresolved:
                continue
            kind = "metric" if resolved.find(exp.AggFunc, exp.Window) else "binding"
            add(kind, resolved, role="output", alias=projection.alias, grain=grain,
                row_context=row_context, source_expression=expression)
            # A computed alias describes its expression, not every operand.
            if isinstance(resolved, exp.Column):
                add("column", resolved, role="output", alias=projection.alias)
            for aggregate in resolved.find_all(exp.AggFunc):
                for column in aggregate.find_all(exp.Column):
                    add("column", column, role="aggregate")

        for key, role in (("where", "filter"), ("having", "having"), ("qualify", "qualify"), ("order", "order")):
            clause = select.args.get(key)
            if clause is None:
                continue
            items = clause.expressions if isinstance(clause, exp.Order) else [clause.this]
            for item in items:
                try:
                    # SQL output aliases in ORDER BY resolve to their expression.
                    value = resolve(item, output_aliases=role == "order")
                    add("ordering" if role == "order" else "predicate", value,
                        role=role, grain=grain, row_context=row_context)
                except _Unresolved as error:
                    unresolved.add(str(error))
        for join in select.args.get("joins") or []:
            if join.args.get("using"):
                unresolved.add("USING join requires explicit endpoint lineage")
            if join.args.get("on") is None:
                continue
            try:
                predicate = resolve(join.args["on"])
                add("relationship", predicate, role="join", row_context=row_context)
            except _Unresolved as error:
                unresolved.add(str(error))

    program = {"id": "program::" + _key([context, dialect, tree.sql(dialect=dialect)]),
               "consumer_contract_version": 1,
               "schema_context": context, "kind": "program", "expression": tree.sql(dialect=dialect),
               "physical_tables": sorted(seen_columns),
               "physical_identifiers": sorted(f"{t}.{c}" for t, cs in seen_columns.items() for c in cs),
               "depends_on": sorted(facts), "roles": [], "aliases": []}
    for fact in facts.values():
        if fact["kind"] != "column":
            fact["depends_on"] = sorted(f["id"] for f in facts.values()
                if f["kind"] == "column" and set(f["physical_identifiers"]) <= set(fact["physical_identifiers"]))
        if fact["kind"] in {"metric", "binding"}:
            source_contexts = {fact.get("row_context"), *fact.get("upstream_scopes", [])}
            fact["depends_on"] = sorted(set(fact["depends_on"]) | {
                f["id"] for f in facts.values()
                if f["kind"] in {"grouping", "predicate", "relationship"}
                and f.get("row_context") in source_contexts})
    facts[program["id"]] = program
    return {"facts": list(facts.values()), "tables": {t: sorted(cs) for t, cs in seen_columns.items()},
            "unresolved": sorted(unresolved)}


class WorkloadSemanticLayer:
    """Persistent source contributions, consolidated into reusable semantic objects."""

    def __init__(self, records: dict[str, Any] | None = None, revision: int = 0):
        self.records = deepcopy(records or {})
        self.revision = revision

    @classmethod
    def load(cls, path: Path) -> "WorkloadSemanticLayer":
        payload = json.loads(path.read_text())
        if payload.get("format") != "sql_workload_semantic_layer_v1":
            raise ValueError("unsupported workload semantic layer")
        return cls(payload["records"], payload["revision"])

    def save(self, path: Path) -> None:
        path.parent.mkdir(parents=True, exist_ok=True)
        temporary = path.with_suffix(path.suffix + ".tmp")
        temporary.write_text(json.dumps({"format": "sql_workload_semantic_layer_v1",
            "revision": self.revision, "records": self.records}, ensure_ascii=False, indent=2) + "\n")
        temporary.replace(path)

    def update(self, rows: list[dict[str, Any]], *, retract: tuple[tuple[str, str], ...] = ()) -> dict[str, Any]:
        """Upsert only SQL/source identity; ignore question, answer, score and gloss.

        context must distinguish incompatible physical schema versions when logs
        span migrations. A log correction reuses (context, history_id). Independent
        observations use different IDs; equal aliases never imply equal concepts.
        """
        previous = {r["id"]: r for r in self.objects()}
        candidate = deepcopy(self.records)
        changed = 0
        for context, history_id in retract:
            changed += candidate.pop(_key([context, history_id]), None) is not None
        batch: set[str] = set()
        for row in rows:
            context = str(row.get("schema_context") or row.get("database_id") or "").strip()
            history_id = str(row.get("history_id") or "").strip()
            sql = str(row.get("sql") or "").strip()
            if not context or not history_id or not sql:
                raise ValueError("history_id, schema_context/database_id and sql are required")
            key = _key([context, history_id])
            if key in batch:
                raise ValueError("duplicate log identity in one update")
            batch.add(key)
            source = {"schema_context": context, "history_id": history_id, "sql": sql,
                      "dialect": str(row.get("dialect") or "sqlite"), "extractor_version": 3}
            if key in candidate and all(candidate[key].get(k) == v for k, v in source.items()):
                continue
            candidate[key] = {**source, **extract_sql_evidence(sql, context, source["dialect"])}
            changed += 1
        self.records = candidate
        self.revision += bool(changed)
        current = {r["id"]: r for r in self.objects()}
        return {"revision": self.revision, "changed_logs": changed, "objects": len(current),
                "added_objects": sorted(current.keys() - previous.keys()),
                "removed_objects": sorted(previous.keys() - current.keys()),
                "updated_objects": sorted(k for k in current.keys() & previous.keys() if current[k] != previous[k])}

    def objects(self) -> list[dict[str, Any]]:
        merged: dict[str, dict[str, Any]] = {}
        for source_key, record in sorted(self.records.items()):
            for fact in record["facts"]:
                item = merged.setdefault(fact["id"], {**deepcopy(fact), "evidence_ids": [], "roles": [], "aliases": []})
                item["evidence_ids"].append("sql_log::" + source_key)
                for key in ("roles", "aliases"):
                    item[key] = sorted(set(item[key]) | set(fact.get(key, [])))
                if "depends_on" in fact:
                    item["depends_on"] = sorted(set(item.get("depends_on", [])) | set(fact["depends_on"]))
        return [merged[key] for key in sorted(merged)]

    def export_assets(self) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[CatalogDocument]]:
        """Adapt the SQL-only layer to the existing recovery/ontology consumer.

        The inferred catalogue is a workload footprint, not a verified current
        schema. Types, keys, cardinalities and unseen columns remain unknown.
        """
        tables: dict[tuple[str, str], set[str]] = defaultdict(set)
        for record in self.records.values():
            for table, columns in record["tables"].items():
                tables[record["schema_context"], table].update(columns)
        objects = self.objects()
        by_id = {o["id"]: o for o in objects}
        columns = {(o["schema_context"], o["physical_identifiers"][0]): o for o in objects if o["kind"] == "column"}
        inputs, recovery, documents = [], [], []
        for (context, table), names in sorted(tables.items()):
            input_id = "sql_catalog::" + _key([context, table])
            histories = [{"history_id": r["history_id"], "evidence_id": "sql_log::" + k,
                          "sql": r["sql"], "question": "", "physical_columns": r["tables"][table]}
                         for k, r in sorted(self.records.items())
                         if r["schema_context"] == context and table in r["tables"]]
            inputs.append({"input_id": input_id, "schema_context": context, "physical_table": table,
                           "schema_source": "historical_sql_observation", "catalogue_complete": False,
                           "columns": [{"physical_column": c, "declared_type": "unknown", "primary_key": False,
                                        "observed_values": []} for c in sorted(names)],
                           "relationships": [], "target_disjoint_workload": histories})
            prediction = {"physical_table": table, "table_aliases": [], "purpose": "", "columns": []}
            for name in sorted(names):
                fact = columns.get((context, f"{table}.{name}"), {})
                prediction["columns"].append({"physical_column": name, "aliases": fact.get("aliases", []),
                    "query_phrases": fact.get("roles", []), "semantic_type": "unknown",
                    "retrieval_gloss": "Historical SQL roles: " + ", ".join(fact.get("roles", [])),
                    "source": "sql_log_structural_evidence"})
            recovery.append({"input_id": input_id, "prediction": prediction})
        for item in objects:
            payload = {"ontology_kind": "sql_workload_semantic_object", **item,
                       "semantic_status": "observed_expression_and_alias_hints",
                       "schema_status": "historical_not_current_verified"}
            if item["kind"] == "program":
                payload.update(sql_template=item["expression"],
                               physical_columns=item["physical_identifiers"],
                               provenance="historical_sql_log",
                               historical_question="")
            if item["kind"] == "metric":
                payload["metric_contract"] = {
                    "formula": item["expression"], "grain": item.get("grain", []),
                    "row_context": item.get("row_context", ""),
                    "upstream_scopes": item.get("upstream_scopes", []),
                    "requires_staged_execution": item.get("requires_staged_execution", False),
                    "depends_on": item.get("depends_on", []),
                }
            if item.get("consumer_contract_version") == 1:
                # Materialize meaning for the consumer, not opaque dependency
                # hashes followed by a character-truncated JSON dump. The full
                # source graph/provenance remains in the persistent layer.
                required, visited = set(), set()

                def collect(identity: str) -> None:
                    if identity in visited:
                        return
                    visited.add(identity)
                    obj = by_id[identity]
                    required.update(obj["physical_identifiers"])
                    for dependency in obj.get("depends_on", []):
                        collect(dependency)

                collect(item["id"])
                payload = {k: payload[k] for k in (
                    "ontology_kind", "id", "schema_context", "kind", "aliases", "roles",
                    "physical_tables", "semantic_status", "schema_status", "consumer_contract_version")}
                payload.update(physical_identifiers=sorted(required),
                    supporting_sql_logs=len(item["evidence_ids"]),
                    source_evidence_ids=item["evidence_ids"][:3])
                if item["kind"] == "program":
                    payload.update(sql_template=item["expression"], provenance="historical_sql_log",
                                   physical_columns=sorted(required), historical_question="")
                elif item["kind"] in {"metric", "binding"}:
                    contract = deepcopy(item.get("execution_contract"))
                    if contract is None:
                        contract = {"formula": item["expression"], "grain": item.get("grain", []),
                            "scope_sql": item.get("row_context", ""),
                            "upstream_scopes": item.get("upstream_scopes", []),
                            "requires_staged_execution": item.get("requires_staged_execution", False)}
                    payload["metric_contract" if item["kind"] == "metric" else "binding_contract"] = contract
                else:
                    payload["expression"] = item["expression"]
                    if item["kind"] != "column":
                        payload.update(scope_sql=item.get("row_context", ""),
                                       upstream_scopes=item.get("upstream_scopes", []))
            if "interpretation_confidence" in item:
                for interpretation_key in ("interpretation_source", "interpretation_confidence", "interpretation_history_ids", "interpretation_revision_evidence"):
                    if interpretation_key in item:
                        payload[interpretation_key] = item[interpretation_key]
                if item.get("interpretation_revision_evidence"):
                    for interpretation_key in ("interpretation_assessment", "interpretation_observations"):
                        if interpretation_key in item:
                            payload[interpretation_key] = item[interpretation_key]
            for auxiliary_key in ("family_id", "family_status", "profile_revision", "candidate_interpretations",
                                  "hard_constraint_ids", "proposed_domain_relations", "interpretation_history_ids",
                                  "interpretation_source", "interpretation_description", "binding"):
                if "family_id" in item and auxiliary_key in item:
                    payload[auxiliary_key] = item[auxiliary_key]
            documents.append(CatalogDocument(candidate_id=item["id"], database_id=item["schema_context"],
                kind="knowledge", table=None, name=" ".join([item["kind"], *item["aliases"], *item["roles"]]),
                text=json.dumps(payload, ensure_ascii=False, sort_keys=True)))
        return inputs, recovery, documents

    def augment_ontology(self, ontology: Any) -> Any:
        """Expose learned assets through the existing query-time ontology path.

        Binding to an available current catalogue is optional at construction and
        mandatory here: historical observations are not proof of current schema.
        Relations are observed joins, never inferred PK/FK/cardinality claims.
        """
        from finsemguard.e2e.operational_ontology import OperationalOntology, OntologyEdge

        objects = {o["id"]: o for o in self.objects()}
        _, _, documents = self.export_assets()
        refresh = not self.records or any(r.get("extractor_version", 0) >= 3 for r in self.records.values())
        old_owned = set()
        if refresh:
            for d in ontology.evidence_documents:
                try:
                    if json.loads(d.text).get("ontology_kind") == "sql_workload_semantic_object":
                        old_owned.add(d.candidate_id)
                except (ValueError, AttributeError):
                    pass
        existing = {d.candidate_id: d for d in ontology.evidence_documents if d.candidate_id not in old_owned}
        bindings = {k: v for k, v in ontology.document_bindings.items() if k not in old_owned}
        edges = [e for e in ontology.edges if not (refresh and e.evidence_types == ("sql_workload_observed_join",))]
        observed_edges: dict[tuple[str, str, str], dict[str, Any]] = {}

        def closure(item: dict[str, Any], visited: set[str]) -> list[dict[str, Any]]:
            if item["id"] in visited:
                return []
            visited.add(item["id"])
            return [item, *(x for k in item.get("depends_on", []) for x in closure(objects[k], visited))]

        for document in documents:
            item = objects[document.candidate_id]
            dependencies = closure(item, set())
            context = item["schema_context"]
            inventory = ontology.inventory.get(context, {})
            required = {p for d in dependencies for p in d["physical_identifiers"]}
            tables = {t for d in dependencies for t in d.get("physical_tables", [])}
            known = {f"{t}.{c}" for t, columns in inventory.items() for c in columns}
            if not tables or not tables <= set(inventory) or not required <= known:
                continue
            existing[document.candidate_id] = document
            bindings[document.candidate_id] = tuple(sorted(
                {f"table::{context}::{t}" for t in tables}
                | {f"column::{context}::{p.rsplit('.', 1)[0]}::{p.rsplit('.', 1)[1]}" for p in required}))
            # Retain the full ON predicate in the semantic object; only an exact
            # equality predicate is exposed as a simple join edge.
            if item["kind"] == "relationship":
                predicate = sqlglot.parse_one(item["expression"])
                if isinstance(predicate, exp.EQ) and isinstance(predicate.left, exp.Column) and isinstance(predicate.right, exp.Column):
                    left, right = predicate.left, predicate.right
                    if left.table != right.table:
                        if refresh:
                            a, b = sorted(((left.table, left.name), (right.table, right.name)))
                            key = (context, str(a), str(b))
                            edge = observed_edges.setdefault(key, {"left": a, "right": b, "evidence": set()})
                            edge["evidence"].update(item["evidence_ids"])
                        else:
                            edges.append(OntologyEdge(context, left.table, left.name, right.table, right.name,
                                0.95, ("sql_workload_observed_join",), tuple(item["evidence_ids"])))
        for (context, _, _), edge in sorted(observed_edges.items()):
            edges.append(OntologyEdge(context, *edge["left"], *edge["right"], 0.95,
                ("sql_workload_observed_join",), tuple(sorted(edge["evidence"]))))
        return OperationalOntology(edges, ontology.inventory, list(existing.values()), bindings)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--history", type=Path, required=True, help="JSONL: history_id, schema_context, sql; optional dialect")
    parser.add_argument("--state", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--retract", action="append", nargs=2, default=[], metavar=("CONTEXT", "HISTORY_ID"))
    args = parser.parse_args()
    layer = WorkloadSemanticLayer.load(args.state) if args.state.exists() else WorkloadSemanticLayer()
    rows = [json.loads(line) for line in args.history.read_text().splitlines() if line.strip()]
    summary = layer.update(rows, retract=tuple(tuple(pair) for pair in args.retract))
    layer.save(args.state)
    inputs, recovery, documents = layer.export_assets()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    for name, values in (("table_inputs.jsonl", inputs), ("table_recovery.jsonl", recovery),
                         ("semantic_objects.jsonl", layer.objects()),
                         ("semantic_documents.jsonl", [vars(d) for d in documents])):
        (args.output_dir / name).write_text("".join(json.dumps(v, ensure_ascii=False) + "\n" for v in values))
    compact = {k: v for k, v in summary.items() if k not in {"added_objects", "removed_objects", "updated_objects"}}
    compact.update(history_records=len(layer.records), observed_tables=len(inputs),
        unresolved_records=sum(bool(r["unresolved"]) for r in layer.records.values()),
        added_objects=len(summary["added_objects"]), removed_objects=len(summary["removed_objects"]),
        updated_objects=len(summary["updated_objects"]))
    (args.output_dir / "BUILD_SUMMARY.json").write_text(json.dumps(compact, indent=2) + "\n")
    print(json.dumps(compact, indent=2))


if __name__ == "__main__":
    main()
