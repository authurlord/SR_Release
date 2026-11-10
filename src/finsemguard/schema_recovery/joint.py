"""Opt-in family reconstruction: model proposals, deterministic feasibility.

Original SQL, physical identities and the legacy per-column path are immutable.
Domain implications are explicitly conditional on the proposed relation; observed
support containment alone never supplies a business label.
"""
from __future__ import annotations

from collections import Counter
from hashlib import sha256
from itertools import permutations
import json
import math
from pathlib import Path
import re
import sqlite3
from typing import Any, Protocol

from finsemguard.ontology_discovery.workload_semantics import extract_sql_evidence


def digest(value: Any) -> str:
    return sha256(json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":")).encode()).hexdigest()


def file_hash(path: Path) -> str:
    h = sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def quote(identifier: str) -> str:
    return '"' + identifier.replace('"', '""') + '"'


def value_format(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, (int, float)):
        return "numeric"
    if isinstance(value, bytes):
        return "blob"
    if value == "":
        return "empty"
    if re.fullmatch(r"\d+:\d{2}\.\d{3}", str(value)):
        return "lap_time"
    if re.fullmatch(r"[-+]?\d+(?:\.\d+)?", str(value)):
        return "numeric_text"
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}(?:[ T].*)?", str(value)):
        return "iso_date"
    return "text"


def profile_table(database: Path, context: str, table: str, columns: list[str], *,
                  empty_is_null: bool = True, database_sha256: str | None = None,
                  include_pairs: bool = True) -> dict:
    """Ordinary SQLite aggregates; distinct value frequencies retain format tails.

    Open immutable read-only snapshots. No UDFs, temporary writes or sampling.
    Pair counts are restricted to a preselected family, never the whole schema.
    """
    dbhash = database_sha256 or file_hash(database)
    conn = sqlite3.connect(database.resolve().as_uri() + "?mode=ro&immutable=1", uri=True)
    conn.execute("PRAGMA query_only=ON")
    try:
        types = {r[1]: r[2] for r in conn.execute(f"PRAGMA table_info({quote(table)})")}
        if not columns or len(columns) != len(set(columns)) or not set(columns) <= types.keys():
            raise ValueError("family must contain distinct existing columns")
        expressions = {c: f"NULLIF({quote(c)}, '')" if empty_is_null else quote(c) for c in columns}
        n = conn.execute(f"SELECT COUNT(*) FROM {quote(table)}").fetchone()[0]
        profiles = {}
        queries = []
        for c in columns:
            e = expressions[c]
            query = f"SELECT COUNT({e}), COUNT(DISTINCT {e}), MIN({e}), MAX({e}) FROM {quote(table)}"
            present, distinct, low, high = conn.execute(query).fetchone()
            queries.append(query)
            formats, storage = Counter(), Counter()
            frequency_sql = f"SELECT {e}, TYPEOF({e}), COUNT(*) FROM {quote(table)} GROUP BY {e}, TYPEOF({e})"
            queries.append(frequency_sql)
            for val, typ, count in conn.execute(frequency_sql):
                formats[value_format(val)] += count
                storage[typ] += count
            dominant = max((k for k in formats if k not in {"null", "empty"}), key=lambda k: formats[k], default="unknown")
            profiles[c] = {"declared_type": types[c], "non_null": present, "distinct": distinct,
                "min": low if not isinstance(low, bytes) else low.hex(),
                "max": high if not isinstance(high, bytes) else high.hex(),
                "format_counts": dict(formats), "storage_counts": dict(storage), "dominant_format": dominant}
        pairs = []
        for a in columns if include_pairs else []:
            for b in columns:
                if a == b:
                    continue
                query = f"SELECT COUNT(*) FROM {quote(table)} WHERE {expressions[a]} IS NOT NULL AND {expressions[b]} IS NULL"
                queries.append(query)
                pairs.append({"present": a, "absent": b, "count": conn.execute(query).fetchone()[0]})
        result = {"schema_context": context, "table": table, "columns": sorted(columns),
            "family_id": "family::" + digest([context, table, sorted(columns)])[:24],
            "database_sha256": dbhash, "empty_strings_normalized_to_null": empty_is_null,
            "row_count": n, "profiles": profiles, "support_differences": pairs, "queries": queries}
        # Snapshot identity and evidence content are different. An unrelated
        # table update must not invalidate this family's unchanged observations.
        result["profile_revision"] = digest({k: v for k, v in result.items() if k != "database_sha256"})
        return result
    finally:
        conn.close()


def discover_families(database: Path, context: str, table: str, active_columns: set[str], *,
                      max_active_columns: int = 8) -> list[dict]:
    """Group compatible declared types and dominant formats, retaining outliers.

    Profile cheap single-column statistics first. Inactive columns remain in the
    family catalogue but do not trigger quadratic pair scans or model calls.
    Large active families are explicitly deferred rather than treated as solved.
    """
    con = sqlite3.connect(database.resolve().as_uri() + "?mode=ro&immutable=1", uri=True)
    try:
        columns = [r[1] for r in con.execute(f"PRAGMA table_info({quote(table)})")]
    finally:
        con.close()
    cheap = profile_table(database, context, table, columns, include_pairs=False)
    groups = {}
    for column, p in cheap["profiles"].items():
        key = (p["declared_type"].upper(), p["dominant_format"])
        groups.setdefault(key, []).append(column)
    result = []
    for key, members in sorted(groups.items()):
        if len(members) < 2:
            continue
        active = sorted(set(members) & active_columns)
        record = {"family_id": "family::" + digest([context, table, sorted(members)])[:24],
            "schema_context": context, "table": table, "columns": members, "active_columns": active,
            "declared_type": key[0], "dominant_format": key[1],
            "single_column_profiles": {c: cheap["profiles"][c] for c in members},
            "pair_profile_deferred": len(active) > max_active_columns,
            "pruning_policy": "historically referenced columns; defer oversized active families",
            "database_sha256": cheap["database_sha256"]}
        if active and len(active) <= max_active_columns:
            record["active_profile"] = profile_table(database, context, table, active, database_sha256=cheap["database_sha256"])
        result.append(record)
    return result


def assertions_for_family(histories: list[dict], context: str, table: str, columns: list[str]) -> list[dict]:
    physical = {f"{table}.{c}" for c in columns}
    result = []
    for source in histories:
        if str(source.get("schema_context") or source.get("database_id")) != context:
            continue
        extracted = extract_sql_evidence(source["sql"], context, source.get("dialect", "sqlite"))
        for fact in extracted["facts"]:
            if physical.intersection(fact["physical_identifiers"]):
                result.append({**fact, "source_ids": [source["history_id"]], "source_sql": source["sql"],
                    "unresolved_references": extracted["unresolved"],
                    "cross_family_physical_identifiers": sorted(set(fact["physical_identifiers"]) - physical)})
    return result


PROPOSE_PROMPT = """Propose semantic roles for one family of masked physical columns using only
the supplied historical SQL and read-only profiles. Do not equate a column's order in
the input with semantic order. Propose roles, NOT a physical assignment. Distinct
roles have unique ids. Return JSON {roles:[{id,description,source_ids,year:null|integer}],
domain_relations:[{kind:'support_subset',subset_role,superset_role,strict:boolean,
description,source_ids}], soft_evidence:[{description,source_ids}]}.
Propose a finite role vocabulary sufficient for an injective assignment to the family.
For staged participation, state the relevant domain convention as support_subset
(participation in the later stage implies participation in the earlier stage). Its
orientation is subset -> superset, and strict=true requires fewer present rows.
Do not assert an arbitrary ordering just from numeric magnitudes or identifier suffixes.
For year-bearing roles, year must be a literal justified by source SQL, otherwise null.
Every source_id must be supplied. Domain relations are hypotheses, not database facts.
No target questions, answers, or unmasked gold labels are available. If evidence cannot
name a role, use a distinct unknown role rather than inventing a business meaning.
Do not use a remembered unmasked benchmark schema as evidence. A numerical magnitude
alone cannot distinguish population, salary, or a different numeric quantity. In this
case use an unknown measure role and state the remaining conceptual alternatives in
its description. Year literals may identify a year without identifying the measured
business quantity. Preserve this distinction. Stage-order domain conventions are
allowed when explicitly stated and tested against participation support."""

CHOOSE_PROMPT = """Choose among the supplied feasible injective role assignments using only
the recorded SQL evidence. Return JSON {assignment: {column:role_id}|null,
assignment_index: integer|null, reason:string,
source_ids:[...]}. Null means undetermined. Do not invent constraints or candidates.
If assignments are encoded as a decision DAG, start at root and traverse one edge
per column in column_order. Edges map role IDs to the next node; node 0 accepts.
Return the complete assignment, which will be checked against the feasible set.
If remaining alternatives are indistinguishable from the evidence, return null."""


def compact_assertions(assertions: list[dict]) -> dict:
    """Lossless source/SQL interning, preserving each original assertion exactly.

    Shared assertion bodies retain all their contributing source IDs. SQL and
    repeated expression/scope strings are referenced, never abbreviated.
    """
    strings: dict[str, str] = {}
    lookup: dict[str, str] = {}
    def intern(value):
        if isinstance(value, str) and len(value) > 80:
            if value not in lookup:
                key = f'text_{len(lookup)}'; lookup[value] = key; strings[key] = value
            return {'text_ref': lookup[value]}
        if isinstance(value, list): return [intern(v) for v in value]
        if isinstance(value, dict): return {k:intern(v) for k,v in value.items()}
        return value
    return {'encoding': 'replace each {text_ref:id} with strings[id]; no evidence omitted',
            'strings': strings, 'assertions': [intern(a) for a in assertions]}


def assignment_dag(assignments: list[dict]) -> dict:
    """Canonical reduced decision DAG for an explicit finite set, not a score.

    Identical suffix subtrees share a node. This reduces a seven-role permutation
    family from 5,040 repeated dictionaries to 128 states, with no lost choices.
    """
    if not assignments: raise ValueError('empty feasible set')
    columns = sorted(assignments[0])
    if any(sorted(a) != columns for a in assignments): raise ValueError('inconsistent assignment columns')
    nodes: dict[str, dict] = {'0': {'accept': True}}
    interned = {}
    def build(rows, depth):
        if depth == len(columns): return '0'
        groups = {}
        for row in rows: groups.setdefault(row[columns[depth]], []).append(row)
        edges = {role:build(group, depth+1) for role,group in sorted(groups.items())}
        key = (depth,tuple(edges.items()))
        if key not in interned:
            node_id = str(len(nodes));interned[key] = node_id
            nodes[node_id] = {'column':columns[depth],'edges':edges}
        return interned[key]
    root = build(assignments,0)
    return {'column_order':columns,'root':root,'nodes':nodes,'assignment_count':len(assignments)}


class RecoveryModel(Protocol):
    def chat_json_with_metadata(self, system: str, user: str) -> tuple[dict, dict]: ...


def validate_proposal(proposal: dict, source_ids: set[str]) -> None:
    roles = proposal.get("roles", [])
    ids = [r["id"] for r in roles]
    if not ids or len(set(ids)) != len(ids):
        raise ValueError("proposal roles must have unique nonempty identities")
    for entry in [*roles, *proposal.get("domain_relations", []), *proposal.get("soft_evidence", [])]:
        if not set(entry.get("source_ids", [])) <= source_ids:
            raise ValueError("proposal cites evidence outside the provided history")
    for relation in proposal.get("domain_relations", []):
        if relation["kind"] != "support_subset":
            raise ValueError("unsupported domain predicate")
        if relation["subset_role"] not in ids or relation["superset_role"] not in ids:
            raise ValueError("domain predicate references unknown roles")


def derive_constraints(profile: dict, assertions: list[dict], proposal: dict) -> list[dict]:
    import sqlglot
    from sqlglot import exp
    constraints = []
    def add(kind: str, origin: str, sources: list[str], **payload: Any) -> None:
        value = {"kind": kind, "origin": origin, "source_ids": sorted(set(sources)),
            "profile_revision": profile["profile_revision"], **payload}
        value["constraint_id"] = "constraint::" + digest(value)[:24]
        constraints.append(value)
    for pair in profile["support_differences"]:
        add("observed_support_difference", "database_observation", [], **pair)
    for relation in proposal.get("domain_relations", []):
        add("role_support_subset", "proposed_domain_relation_and_database_observation", relation.get("source_ids", []),
            subset_role=relation["subset_role"], superset_role=relation["superset_role"],
            strict=bool(relation.get("strict", False)), description=relation.get("description", ""))
    # SQL IIF(compare(a,b),'year_a','year_b') directly associates the displayed
    # year with the corresponding comparison operand. Preserve the full source.
    seen = set()
    for assertion in assertions:
        sql = assertion["source_sql"]
        if (sql, tuple(assertion["source_ids"])) in seen:
            continue
        seen.add((sql, tuple(assertion["source_ids"])))
        tree = sqlglot.parse_one(sql, read="sqlite")
        for node in tree.find_all(exp.If):
            cond, yes, no = node.this, node.args.get("true"), node.args.get("false")
            if not isinstance(cond, (exp.GT, exp.LT)) or not isinstance(yes, exp.Literal) or not isinstance(no, exp.Literal):
                continue
            if not re.fullmatch(r"(?:19|20)\d{2}", str(yes.this)) or not re.fullmatch(r"(?:19|20)\d{2}", str(no.this)):
                continue
            left, right = list(cond.left.find_all(exp.Column)), list(cond.right.find_all(exp.Column))
            if len(left) != 1 or len(right) != 1:
                continue
            if not {left[0].name, right[0].name} <= set(profile["columns"]):
                continue
            # Alias resolution is taken from extracted physical references, not
            # guessed across ambiguous joins that reuse the same column names.
            physical = {f'{profile["table"]}.{left[0].name}', f'{profile["table"]}.{right[0].name}'}
            if not physical <= set(assertion["physical_identifiers"]):
                continue
            for col, year in ((left[0].name, int(yes.this)), (right[0].name, int(no.this))):
                add("role_year_literal", "sql_branch_literal", assertion["source_ids"], column=col, year=year,
                    expression=node.sql(dialect="sqlite"), interpretation="displayed branch label corresponds to comparison operand")
    for assertion in assertions:
        if assertion["kind"] not in {"column", "program"}:
            add("retained_sql_use", "historical_sql", assertion["source_ids"], expression=assertion["expression"],
                physical_identifiers=assertion["physical_identifiers"], scope=assertion.get("row_context"),
                cross_family_physical_identifiers=assertion["cross_family_physical_identifiers"])
    return constraints


def feasible_assignments(profile: dict, proposal: dict, constraints: list[dict], *, budget: int = 10000) -> dict:
    if budget < 1:
        raise ValueError("enumeration budget must be positive")
    columns, roles = profile["columns"], proposal["roles"]
    by_role = {r["id"]: r for r in roles}
    differences = {(r["present"], r["absent"]): r["count"] for r in profile["support_differences"]}
    total = math.perm(len(roles), len(columns)) if len(roles) >= len(columns) else 0
    excluded, feasible = [], []
    tested = 0
    for values in permutations(by_role, len(columns)):
        if tested >= budget:
            break
        tested += 1
        assignment = dict(zip(columns, values))
        inverse = {v: k for k, v in assignment.items()}
        violated = []
        for c in constraints:
            if c["kind"] == "role_support_subset":
                sub, sup = inverse.get(c["subset_role"]), inverse.get(c["superset_role"])
                if sub is None or sup is None:
                    continue
                bad = differences[(sub, sup)] != 0
                if c["strict"]:
                    bad |= profile["profiles"][sub]["non_null"] >= profile["profiles"][sup]["non_null"]
                if bad:
                    violated.append(c["constraint_id"])
            elif c["kind"] == "role_year_literal":
                if by_role[assignment[c["column"]]].get("year") != c["year"]:
                    violated.append(c["constraint_id"])
        if violated:
            excluded.append({"assignment": assignment, "violated_constraint_ids": violated})
        else:
            feasible.append(assignment)
    return {"initial_assignment_count": total, "tested": tested, "enumeration_truncated": tested < total,
        "feasible_assignments": feasible, "excluded_assignments": excluded}


def reconstruct_family(profile: dict, assertions: list[dict], model: RecoveryModel, *, enumeration_budget: int = 10000) -> dict:
    sources = {s for a in assertions for s in a["source_ids"]}
    calls, attempts = [], []
    evidence = compact_assertions(assertions)
    payload = {"profile": profile, "evidence": evidence}
    selected = None
    status = "undetermined"
    for attempt in range(2):
        proposal, usage = model.chat_json_with_metadata(PROPOSE_PROMPT, json.dumps(payload, ensure_ascii=False, separators=(',', ':')))
        calls.append({"type": "Propose", "usage": usage, "request_hash": digest(payload), "response": proposal})
        try:
            validate_proposal(proposal, sources)
        except (ValueError, KeyError, TypeError) as error:
            attempts.append({'proposal':proposal, 'validation_error':str(error),
                'constraints':[], 'initial_assignment_count':0, 'tested':0,
                'enumeration_truncated':False, 'feasible_assignments':[], 'excluded_assignments':[]})
            status = 'invalid_proposal'
            payload = {**payload, 'previous_proposal':proposal,
                'validation_error':str(error), 'permitted_history_source_ids':sorted(sources),
                'correction_instruction':'Use historical source IDs, not column IDs. Correct the invalid proposal within this final proposal attempt.'}
            continue
        status = 'undetermined'
        constraints = derive_constraints(profile, assertions, proposal)
        feasible = feasible_assignments(profile, proposal, constraints, budget=enumeration_budget)
        attempts.append({"proposal": proposal, "constraints": constraints, **feasible})
        if feasible["enumeration_truncated"]:
            break  # Never claim uniqueness from a searched prefix.
        alternatives = feasible["feasible_assignments"]
        if len(alternatives) == 1:
            selected, status = alternatives[0], "resolved_structurally"
            break
        if len(alternatives) > 1:
            choice_payload = {"proposal": proposal, "evidence": evidence}
            if len(alternatives) <= 64:
                choice_payload['assignments'] = alternatives
            else:
                choice_payload['assignment_dag'] = assignment_dag(alternatives)
            choice, usage = model.chat_json_with_metadata(CHOOSE_PROMPT, json.dumps(choice_payload, ensure_ascii=False, separators=(',', ':')))
            calls.append({"type": "Choose", "usage": usage, "request_hash": digest(choice_payload), "response": choice})
            if not set(choice.get("source_ids", [])) <= sources:
                raise ValueError("choice cites unseen evidence")
            index = choice.get("assignment_index")
            assignment = choice.get('assignment')
            if isinstance(assignment, dict) and assignment in alternatives:
                selected, status = assignment, 'chosen_with_alternatives'
            elif isinstance(index, int) and not isinstance(index, bool) and 0 <= index < len(alternatives):
                selected, status = alternatives[index], "chosen_with_alternatives"
            break
        payload = {**payload, "previous_proposal": proposal, "violations": feasible["excluded_assignments"]}
    return {"family_id": profile["family_id"], "profile_revision": profile["profile_revision"],
        "schema_context": profile["schema_context"], "table": profile["table"],
        "status": status, "selected_assignment": selected, "source_ids": sorted(sources),
        "attempts": attempts, "model_calls": calls, "model_call_count": len(calls)}
