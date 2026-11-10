"""Budgeted ReAct Text-to-SQL controller with optional recovered-schema search.

The raw and recovered conditions share the controller, database tools, model, and
budgets.  Their only difference is the schema-search index exposed to the agent.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass
from difflib import SequenceMatcher
from functools import lru_cache
from hashlib import sha256
import heapq
import json
import math
import re
import sqlite3
import subprocess
import time
from pathlib import Path
from threading import Lock
from typing import TYPE_CHECKING, Any, Callable, Sequence

import numpy as np
from json_repair import loads as repair_json_loads
import sqlglot
from sqlglot import exp

from finsemguard.agent.llm import VLLMClient
from finsemguard.e2e.anchored_relation_program import (
    anchor_relation_contract,
)
from finsemguard.e2e.graph_evo_program_context import (
    compile_graph_evo_program_context,
    recompile_graph_evo_query_graph,
)
from finsemguard.e2e.livesqlbench import CatalogDocument
from finsemguard.e2e.minimal_join_tree import compile_minimal_join_tree
from finsemguard.e2e.performance_pipeline import execution_probe
from finsemguard.e2e.relational_program_compiler import (
    compile_graph_evo_candidate_scaffold,
    compile_relational_program,
)
from finsemguard.e2e.role_first_relational_program import (
    compile_role_first_relational_program,
)
from finsemguard.e2e.sqlite_catalog import schema_key

if TYPE_CHECKING:
    from finsemguard.e2e.evolution_relations import RelationEvolutionMapping


METHOD_IDS = {
    "raw_react": "react_text2sql_v1__raw_physical_schema",
    "recovered_react": "react_text2sql_v1__fielded_recovery_operational_graph",
    "grounded_react": "react_text2sql_v2__database_grounded_profile_value_join_graph",
    "opaque_react": "react_text2sql_v2__opaque_schema_value_execution_baseline",
    "recovery_only_react": "react_text2sql_v2__automatic_recovery_no_extra_ontology_edges",
    "ontology_react": "react_text2sql_v3__retrieved_history_sql_kb_operational_ontology",
    "program_graph_react": (
        "react_text2sql_v5__role_retrieved_semantic_plan_graph"
    ),
    "minimal_join_tree_react": (
        "react_text2sql_v7__role_grounded_minimal_join_tree"
    ),
    "chess_react": "paper_baseline_chess_style_v1__catalog_value_execution_revision",
    "autolink_react": "paper_baseline_autolink_style_v1__bounded_targeted_expansion",
    "evoschema_raw_react": "react_text2sql_v1__evolved_current_schema_only",
    "evoschema_flat_react": "schema_recovery_flat_v1__same_tokens_no_binding_graph",
    "evoschema_full_react": "schema_recovery_ontology_v1__evolved_lineage_graph",
    "evoschema_program_graph_react": (
        "schema_recovery_ontology_v3__role_retrieved_semantic_plan_graph"
    ),
    "evoschema_minimal_join_tree_react": (
        "schema_recovery_ontology_v4__role_grounded_minimal_join_tree"
    ),
}

PROGRAM_GRAPH_CONDITIONS = {
    "program_graph_react",
    "minimal_join_tree_react",
    "evoschema_program_graph_react",
    "evoschema_minimal_join_tree_react",
}

TRUSTED_RELATIONSHIP_EVIDENCE = {
    "declared_or_materialized_relationship",
    "declared_foreign_key_table_connectivity",
    "declared_foreign_key",
    "declared_fk_plus_schema_lineage",
    "external_knowledge_relationship",
    "target_disjoint_historical_join",
    "evolution_split_key_equivalence",
}

SYSTEM_PROMPT = """You are a performance-oriented ReAct agent for SQLite Text-to-SQL.
Your only objective is to produce the SQL whose execution result answers the question.
Use the supplied benchmark knowledge exactly when relevant. Physical SQLite identifiers
and inspected DDL are authoritative. Search and inspect schema, probe values, and execute
candidate SQL when that can resolve ambiguity. A query being executable does not make it
semantically correct: before submission verify projection, filters, aggregation, grouping,
ordering, literals, join keys, and requested result shape. Use only read-only SELECT/WITH
queries. A ranking aggregate used in ORDER BY is not an output column unless the question
explicitly asks for that measure. Finish by calling submit_sql. Do not ask a human and do
not abstain."""

RECOVERY_PROMPT = """The schema search tool also contains automatically recovered aliases,
roles, value hints, and an operational FK graph. Treat these as high-recall mapping hints,
not as replacements for physical identifiers. Search with reformulations when the first
result misses a requested role, then verify the mapping using inspect_schema, sample_values,
or execute_sql."""

GROUNDED_PROMPT = """The schema index contains deterministic database profiles rather
than model-authored descriptions. For every literal, name, code, date, or amount in the
question, use the pre-fetched exact value matches and call search_values only for unresolved
literals. For multi-table queries, use the pre-fetched join graph and search_joins to recover
declared or compatible join edges. These observations are database evidence. Use them to
build a complete query plan before executing SQL."""

OPAQUE_PROMPT = """Physical table and column names may be deliberately opaque. Use
schema search, exact value probes, schema inspection, join search, and bounded execution
to infer the best query. You have no business dictionary or historical workload; do not
invent a semantic mapping merely because two opaque identifiers look similar."""

ONTOLOGY_PROMPT = """Physical table and column names may be deliberately opaque. The
schema index additionally contains target-isolated historical question/SQL templates,
business-KB mappings bound to physical identifiers, recovered aliases, and a typed
operational join graph. At most two workload templates are supplied. Before writing SQL,
compare each template with the current question and explicitly preserve only matching
projection, predicate, aggregation, CTE, set-operation, and window-function structure;
replace template-specific literals and requested fields. Retrieve evidence for every
requested output, filter, aggregation, and join role. The initial search already includes
the physical anchors bound to retrieved semantic evidence: do not repeat schema/value
probes for roles that are already resolved. Use search_joins only when a required path is
still missing. Executability alone is not evidence of semantic correctness: compare the
candidate clause-by-clause with the question and the closest workload template before
submission. Execute the best complete SQL by turn three, and always submit a SQL query on
the final turn."""

PROGRAM_GRAPH_PROMPT = """Physical table and column names may be deliberately opaque.
The initial search contains a query-conditioned relational-program graph compiled from
automatic schema recovery, target-isolated historical SQL/KB evidence, and typed physical
join edges. Treat its terminal tables, bound columns, bridge path, and at most two program
templates as one executable plan candidate, not as independent hints. Reuse a historical
operator only when it appears in matched_query_operators; always replace its fields,
literals, predicates, and requested output with those of the current question. Preserve
every requested output, filter, aggregation, grouping, ordering, and join role. The graph's
query_role_bindings groups candidate physical identifiers by question role. Before writing
SQL, choose a physical binding for every relevant role and verify that the final query
covers each choice. Do not collapse two distinct requested entities, measures, or counts
onto one column merely because one executable key is available. Prefer the compiled
physical path over guessing joins from names. The user payload may include an automatic
compiled_semantic_plan with a candidate_sql; execute that candidate first when its role
coverage agrees with the evidence, then repair concrete errors instead of silently
discarding the plan. If a window is computed before an outer group-eligibility filter in
the plan or matched template, preserve that CTE boundary; pushing the filter below the
window changes the frame. Execute a complete candidate by
turn three, revise only concrete semantic or execution errors, and always submit SQL on the
final turn. When a retrieved template and the question express the same predicate role but
use different literal values, retain the template's bound physical predicate column unless
database evidence contradicts it; do not swap to another text column merely because its
name sounds plausible. Do not ask a human and do not abstain."""

MINIMAL_JOIN_TREE_PROMPT = """The query_relational_program_graph is a compiled minimal
join tree, not a bag of candidate tables. Its certificate proves only physical relationship
connectivity and join endpoints; role_choices are retrieval hypotheses, not certificates
of semantic correctness. Validate every selected field against the question and prefer a
lexically supported alternative over an ID/code or unrelated field. Literal roles are
non-structural and must be grounded with exact values rather than used as graph terminals.
Historical program templates are advisory operator-shape priors. Their old physical tables
are not graph terminals unless independently selected by a current-question role; never
replace a role-grounded current table with a shorter stale template path.
When a role binding lists required_companion_identifiers for a split historical field,
project every companion unless the question explicitly requests one component. The
topological_table_order and ordered_join_edges define the relationship path. Reuse
join_skeleton_sql whenever it covers the validated roles. Every JOIN must follow an
ordered edge and its on_sql condition unless direct database inspection proves a more
specific physical key. Do not add unselected alternative role tables merely because they
appeared in retrieval. If the certificate reports an unresolved role, resolve only that
role with a targeted schema/value probe while preserving the certified tree."""

ANCHORED_RELATION_PROGRAM_PROMPT = """A base_solution_anchor is the Persistent-Recovery
executable backbone produced without evaluator feedback. When present,
auxiliary_raw_evidence_draft is the independent proposal produced directly from the allowed
raw evidence. It is not a baseline oracle, score signal, selector, or fallback: it is one
input to this one unified main program. This backbone priority is used when the current
physical identifiers are opaque or an evolution lineage must be realized. Begin
candidate_sql by preserving the recovered anchor's complete executable AST. Use the Raw
proposal to restore a concrete projection, predicate, aggregation grain, window/CTE stage,
ordering, or limit only when recovered bindings, typed relations, exact grounding, or a
target-isolated historical program supports that component. When the drafts disagree and
the supplied evidence does not resolve the specific disagreement, retain the recovered
backbone component.

Synthesize exactly one SQL program from the question, both drafts, and the evidence-carrying
Role-First program. Preserve projection order, predicates, aggregation grain, grouping,
HAVING, window/CTE staging, set operations, ordering, and limits unless the evidence for the
current question supports changing that exact component. Semantic role coverage is more
important than a shorter join path. Do not add every high-recall terminal blindly--retain
only the connected subprogram needed by validated roles. Execute the exact complete SQL you
intend to submit. The runtime realizes that one executed submission and applies only typed
current-schema/evolution transformations; it never compares scores or expected answers.
"""

RAW_BACKBONE_RELATION_PROGRAM_PROMPT = """This unified main runs in performance-first
raw-backbone mode. base_solution_anchor is the complete executable Direct Raw proposal,
not an evaluator-selected fallback. persistent_recovery_advisory_draft is the independent
Persistent-Recovery proposal. Begin candidate_sql from the base_solution_anchor's complete
AST. Use recovered semantics, exact current bindings, exact literal grounding, historical
programs, and certified typed relations to make the smallest supported correction to that
AST. The recovered advisory draft is evidence for a correction, not a replacement merely
because it is longer or uses more tables. When evidence does not resolve a disagreement,
retain the raw-backbone component.

Return exactly one unified SQL program. Preserve projection order, predicates, aggregation
grain, grouping, HAVING, window/CTE staging, set operations, ordering, and limits unless the
evidence for the current question supports changing that exact component. Add only the
connected tables required by validated roles. The runtime realizes this one submitted
program over the current physical schema and never compares scores or expected answers.
"""


_OPAQUE_PHYSICAL_IDENTIFIER = re.compile(
    r"^(?:[a-z]{1,8}[_-]?)?\d+$",
    flags=re.I,
)
_NAMED_MEASURE_LOOKUP = re.compile(
    r"\bhow many\s+(?:the\s+)?"
    r"(?:number|amount|quantity|volume|value)\s+of\b",
    flags=re.I,
)


def _opaque_physical_column_ratio(
    documents: Sequence[CatalogDocument],
) -> float:
    """Measure current-schema opacity without dataset or identifier exceptions."""

    column_names = [
        str(document.name).rsplit(".", 1)[-1].strip('`"[] ')
        for document in documents
        if document.kind == "column"
    ]
    if not column_names:
        return 0.0
    opaque = sum(
        bool(_OPAQUE_PHYSICAL_IDENTIFIER.fullmatch(name))
        for name in column_names
    )
    return opaque / len(column_names)

PROGRAM_GRAPH_PLANNER_PROMPT = """Compile the supplied database-local evidence into one
high-recall relational plan for the current Text-to-SQL question. This is a planning stage,
not a safety judge: maximize downstream execution accuracy. Use only physical identifiers
present in the evidence. Cover every projection, filter, grouping, ordering, aggregation,
and join role. Keep distinct requested entities, measures, and counts as distinct role
bindings. Prefer a target-isolated workload mapping or KB alias when it directly names a
question role, and use only relationship-bearing graph edges for joins. When the question
combines a row window with a group-eligibility condition (for example, only groups having
more than N rows), compute the window over the qualifying base rows in an inner CTE and
apply group eligibility outside it; do not push that later filter below the window. Preserve
the same staging when a matched workload template demonstrates it. Return one JSON
object with keys: role_bindings (a list of role/operation/physical_candidates/evidence),
tables, join_edges, operator_plan, template_adaptations, unresolved_ambiguities, and
candidate_sql. candidate_sql must be a complete first candidate in the requested SQL
dialect; the downstream ReAct controller will execute and repair it. A physical column
whose name already denotes an aggregate measure (for example AvgScore, Count, Rate, or
Total) is a stored row-level measure: rank that column directly unless the question and
evidence explicitly require aggregating it across multiple rows. For a split compound
output, include every required_companion_identifier in the projection. Treat
current_schema_for_program as the exact identifier inventory. Never reference a column not
listed for its table. Never add a table whose connection is absent from certified
typed_edges; when a retrieved role candidate is disconnected, retain the corresponding
base_solution_anchor expression rather than inventing a join."""

FIXED_SQL_CONSUMER_PROMPT = """This planner is the fixed downstream SQL generator for
the unified method. Its candidate_sql is the single semantic submission: there is no later
agent that compares or chooses among drafts. Copy the draft explicitly identified by the
active mode as the performance backbone and make only evidence-supported minimum edits. Do
not replace it merely because another draft is more elaborate or uses more tables. If
evidence_bound_program_prior is present, its exact supported program
structure takes precedence for the components it certifies. Never collapse supported CTE
stages, remove a bridge that changes join multiplicity, delete HAVING/window/set-operation
clauses, or merge independently aggregated subprograms. Change a component only where an
explicit current-question role, literal, current physical binding, or typed relation proves
the change, and list that evidence in template_adaptations. Emit one complete read-only SQL
query. The consumer only executes this exact SQL and may perform one basic syntax/execution
correction; it never consults evaluator scores or an expected answer."""

EVIDENCE_FIRST_HISTORY_PROMPT = """Use the already recovered ontology as semantic evidence for the whole question,
not merely as a patch to the draft's join tree. The supplied drafts are fallible proposals:
being executable or agreeing with one another does not certify their business semantics.
For every requested output, population restriction, measure, grouping grain, date interval,
ordering and limit, identify the supporting physical binding and source historical fact.
Read ALL supplied historical SQL programs: a new question may combine knowledge from several
programs. Resolve same-shaped columns using their whole historical expression, co-occurring
predicates, aliases and actual value evidence. Do not infer an opaque field's meaning from
its numeric suffix. Do not replace a required field with a similarly named count/rate/date.

Construct one complete candidate_sql from those bindings. Reuse valid draft clauses, but
replace or complete any clause contradicted or omitted by question-grounded historical
knowledge. Explicitly cover every clause in the question. Do not preserve an incorrect
clause simply because the draft is executable. Conversely, do not copy a historical
literal, filter, output, DISTINCT or LIMIT that the current question does not request.
Preserve expression scope, denominator, aggregation grain, entity multiplicity and
NULL/date handling when reusing a historical computation. Exact database values take
precedence over invented category spellings. Keep projection order as requested.

Use only identifiers in physical_schema_inventory; graph edges and role bindings are
supported candidates, not a prohibition on another relationship explicitly present in
allowed historical SQL. Record each nontrivial change and its source in template_adaptations.
Return the existing planner JSON schema with a complete candidate_sql and no prose outside
JSON. Never use target answers or evaluation feedback. There is no later semantic planner:
your candidate is the final semantic submission, followed by normal execution repair and
Graph/Evo realization. Do not leave requested clauses for a later stage.
"""


SCOPE_GROUNDED_REVISION_PROMPT = """Ground the existing role_bindings in ontology evidence at the correct scope.
For each binding add scope (output, eligibility, measure, or reference_population), grain
(the entity/event represented by one row), and witness (a supplied historical SQL expression
or actual value observation supporting the physical column and unit). Draft SQL alone is
not a witness. An alias is a hypothesis; resolve conflicting numeric/date fields with the
historical expression and observed values. State uncertainty rather than inventing evidence.
Distinguish a relationship's role from its endpoints: two joins to the same entity may
represent different roles. Distinguish the population being selected from the observations
being counted or returned. An existence condition must not filter away other requested
members of an eligible entity. Keep independent reference populations separate from outer
filters. Declare output fields explicitly; do not substitute an internal join key for a
requested name or merge multiple requested fields merely to satisfy an inferred row shape.
Use local qualified columns in each CTE/subquery; explicitly name exported CTE columns.
Preserve valid scope boundaries and weighting in the drafts. Before emitting candidate_sql,
check every binding's actual SQL expression against its witness and the current question.
Use only the existing planner JSON, with concise role bindings and complete candidate_sql.
"""

SCOPE_GROUNDED_CORRECTION_PROMPT = """Review this single SQL submission against the current question and recovered
ontology evidence. Execution success is not semantic correctness. This is the existing
single correction step, not candidate voting. Check (1) requested output fields and order,
(2) physical field meanings and units against supplied history/value witnesses, (3) each
predicate's scope and relation role, (4) eligibility versus returned/aggregated population,
(5) grouping, denominator and weighting, (6) CTE output names and qualified local references.
Keep valid clauses and scope boundaries. Fix only a discrepancy you can explain from the
question and supplied evidence; do not force a change, copy a historical-only filter, or
simplify a correct multi-stage computation. Do not reinterpret a percentile as a fraction
of the mean. Inferred aliases and graph ranking are fallible; concrete witnesses prevail.
Return JSON containing candidate_sql (the complete query, unchanged if already supported),
correction_reason, and scope_checks (concise evidence-backed findings, including uncertainty).
Never use an expected answer or evaluator feedback. Do not mention or guess gold SQL.
"""


WITNESS_CONSISTENT_PROMPT = """Consume the ontology evidence by separating observations from interpretations.
The evidence packet contains the existing historical programs, graph/role candidates,
evolution constraints, proposed drafts, inferred aliases, and bounded physical row samples.
Aliases (including ones labeled high confidence), generated summaries, ranking scores and
draft SQL are hypotheses, not independent observations. Repetition across these derived
views does not corroborate a meaning. Do not rename an opaque field by ordinal position,
standard benchmark memory, type alone, or a fluent alias. When a label conflicts with an
actual historical computation or observed value scale, explicitly compare the witnesses.
A historical SQL expression establishes what was computed, not automatically its business
name. Use the current question and all available observations to choose the binding;
record unresolved alternatives rather than falsely claiming a proof. Small row samples
can disprove a proposed interpretation but their missing values do not prove absence.

For every nontrivial binding change, give the actual old/new expression and the concrete
history/value witness in template_adaptations (or correction_reason). Reuse supported
clauses; do not preserve a bad draft by default. Read time/quantity encodings and units:
lexical order of a duration string is not elapsed-time order. A decimal-looking datatype
is not evidence for money, a count, a rate or a test name. Preserve observed category
spellings and missing-value sentinels; 'no category' can be an actual category, not NULL.

Resolve each clause's entity before writing SQL. First identify eligible entity keys,
then compute the requested measure over the proper observations for those keys. A child
property qualifying a parent is an EXISTS/semijoin condition, not a restriction on every
child later measured. Do not restrict the denominator to the numerator's category. Do not
count joined child rows when the question counts parents. Keep independent aggregates and
reference populations separate. Do not change a supported weighting merely to simplify
joins. For a scalar count of qualifying groups, count the grouped result in an outer query.
Treat observed execution errors and row/column counts as facts; never dismiss a contract
violation as a display artifact. Diagnose the SQL scope producing that observation.

For output representation reuse the historical physical projection convention unless the
question explicitly requests formatting/concatenation. A person's full name represented by
two stored name columns should remain two projected columns; do not concatenate them just
for presentation. Preserve requested field order. Return complete candidate_sql first in
the existing JSON response, followed by concise evidence and uncertainty; no long internal
monologue. This remains a single proposal with the existing one correction, not voting.
"""


GROUNDED_BINDING_PROMPT = """Ground the ontology bindings in observations before realizing the query.
All unverified_draft_sql entries were generated for THIS question by earlier models.
They are neither historical SQL nor reference answers. Their order conveys no authority.
Reuse their useful computations, but never cite a draft, derived contract, inferred alias
confidence, or your own proposed binding as proof of a physical meaning or predicate scope.
For a disputed binding, identify the historical expression or observed values that support
it and the competing interpretation. Keep eligibility, measured observations and reference
population separate, including their relationship keys. Every output relationship must
remain linked in the SQL; two relations sharing a parent do not establish a child-to-child
relationship. Repeated independent children must not multiply the measure.

The planner may include binding_probes: up to three objects with purpose and sql. Each is
one small read-only SQLite SELECT to distinguish an unresolved field/value/relationship
using only the physical database. For example, sample non-null values of competing fields
or test a disputed literal on physical columns. Prefer bounded selective probes; no writes,
DDL, expected answers or benchmark metadata. These observations will be supplied to the
existing correction. A probe that finds nothing does not establish the intended meaning.
This is evidence gathering for the existing ontology, not extra answer candidates.

Keep a short list of scope_obligations: which entity is eligible, which rows contribute to
each measure, the reference population, and which fields the question asks to RETURN.
Measures used only to select/order an entity need not appear in the final projection.
Preserve supported scope and units instead of importing a draft's filters mechanically.
For independent existence requirements on large tables prefer IN (SELECT key ...) or
distinct-key CTE semijoins; for per-entity aggregates prefer grouped CTEs. Preserve NULL,
weighting and correlation semantics; do not replace a relationship by a Cartesian product.

In correction, binding_validation contains new physical observations and an EXPLAIN plan
for the actual submitted SQL. A prefix sample does not certify full execution. Correlated
subqueries scanning a large inner relation repeatedly warrant a set-based formulation.
A diagnostic time/row budget is NOT an official execution failure or correctness score.
Syntax, unavailable aliases and unsupported functions MUST be repaired in candidate_sql;
preserve-semantics instructions never prohibit these repairs. Claims in correction_reason
do not implement a repair. Give concise binding/scope/repair decisions FIRST, then the
complete final candidate_sql implementing those decisions. Do not debate a known error
and then return the erroneous draft. Keep this one proposal and one correction; no voting.
"""


def _grounded_binding_packet(payload: dict[str, Any]) -> dict[str, Any]:
    """Reuse the v8 evidence, separating generated drafts from historical witnesses."""
    packet = dict(payload)
    drafts = []
    for key in ("base_solution_anchor", "auxiliary_raw_evidence_draft",
                "persistent_recovery_advisory_draft"):
        draft = packet.pop(key, None)
        if isinstance(draft, dict):
            sql = draft.get("base_sql") or draft.get("sql") or draft.get("candidate_sql") or draft.get("anchor_sql")
        else:
            sql = draft if isinstance(draft, str) else None
        if sql and sql not in drafts:
            drafts.append(sql)
    # These are generated from the same drafts, not independent evidence.
    packet.pop("evidence_bound_program_prior", None)
    packet.pop("proposed_program_contract", None)
    packet["unverified_draft_sql"] = drafts
    packet["history_consumer_version"] = "ontology_grounded_binding_v9"
    return packet


def _bounded_binding_read(database: Path, sql: str, *, completion: bool = False,
                          timeout_seconds: float = 2.0) -> dict[str, Any]:
    """Observe one physical read without evaluator inputs, schema mutation or answer scoring."""
    started = time.monotonic()
    connection = sqlite3.connect(f"file:{database}?mode=ro", uri=True, timeout=timeout_seconds)
    connection.execute("PRAGMA query_only=ON")
    allowed = {sqlite3.SQLITE_SELECT, sqlite3.SQLITE_READ, sqlite3.SQLITE_FUNCTION,
               sqlite3.SQLITE_RECURSIVE}
    def authorize(action, arg1, arg2, *_):
        if action == sqlite3.SQLITE_FUNCTION and str(arg2 or arg1).lower() in {
                "load_extension", "readfile", "writefile"}:
            return sqlite3.SQLITE_DENY
        return sqlite3.SQLITE_OK if action in allowed else sqlite3.SQLITE_DENY
    connection.set_authorizer(authorize)
    connection.set_progress_handler(lambda: int(time.monotonic() - started > timeout_seconds), 1000)
    observation: dict[str, Any] = {"sql": sql, "timeout_seconds": timeout_seconds,
                                  "official_score": False, "rows_seen": 0}
    try:
        statements = sqlglot.parse(sql, read="sqlite")
        if len(statements) != 1 or not isinstance(statements[0], exp.Query):
            raise ValueError("One read-only SELECT required")
        if completion:
            plan = connection.execute("EXPLAIN QUERY PLAN " + sql).fetchall()
            observation["query_plan"] = [str(row[3]) for row in plan[:60]]
        cursor = connection.execute(sql)
        all_columns = [str(c[0]) for c in cursor.description or []]
        observation["columns"] = all_columns[:16]
        observation["sample_columns_truncated"] = len(all_columns) > 16
        sample = []
        while True:
            batch = cursor.fetchmany(256 if completion else 6)
            observation["rows_seen"] += len(batch)
            for row in batch[:max(0, 5-len(sample))]:
                sample.append([str(v)[:100] if isinstance(v, (str, bytes)) else _safe_value(v) for v in row[:16]])
            observation["sample_rows"] = sample
            if not batch or (not completion and len(batch) < 6):
                observation["state"] = "complete"
                break
            if not completion or observation["rows_seen"] >= 100_000:
                observation["state"] = "sample_only" if not completion else "row_budget_reached"
                break
            if time.monotonic() - started > timeout_seconds:
                observation["state"] = "time_budget_reached"
                break
    except Exception as error:
        observation.update(state="time_budget_reached" if isinstance(error, sqlite3.OperationalError)
                           and str(error) == "interrupted" else "error",
                           error=type(error).__name__ + ": " + str(error)[:500])
    finally:
        connection.close()
    observation["elapsed_seconds"] = round(time.monotonic()-started, 4)
    # Bound only rendered samples, never modify the executed SQL or its coverage.
    while len(json.dumps(observation, ensure_ascii=False)) > 6000 and observation.get("sample_rows"):
        observation["sample_rows"].pop()
        observation["sample_rendering_truncated"] = True
    if completion:
        # The full submission is already supplied in correction_payload.
        observation["sql_sha256"] = sha256(sql.encode()).hexdigest()
        observation.pop("sql", None)
    return observation


ENTITY_GRAIN_CONTRACT_PROMPT = """Declare the ontology metric's input grain as an
executable contract, not just a prose scope check. Return candidate_sql FIRST, then
entity_grain_contracts (a list), correction_reason and concise scope_checks.
Each contract is {"table": "physical table name", "alias": "its alias in candidate_sql",
"weighting": "entity_once" or "joined_rows", "question_basis": "requested measured entity and why"}.
Use the physical measured entity, NOT the category/grouping entity. Decide its grain from
the question and ontology before rationalizing the submitted joins. For an average of
entity attributes, a sum of amounts over entities, or a percentage of entities, each
eligible entity contributes once within each requested group: use entity_once. Relations
that merely witness eligibility do not create additional measured entities. Use joined_rows
only when each joined combination is itself a requested observation or weighting; explain
that weighting from the question, not from the existence of the join. Equal values from
different physical entities remain distinct observations. A repeated identity is different
from two distinct entities with equal values. Grouping does not remove repeated inputs to
SUM or COUNT; a ratio is not invariant to entity-dependent multiplicities.

The existing relational compiler will implement entity_once for admissible single-measure
aggregate blocks: preserve eligible FROM/WHERE and group keys, project DISTINCT physical
entity keys plus consumed values, then apply the ORIGINAL aggregate/HAVING/order. This is
not SUM(DISTINCT value). Supply a contract even if candidate_sql already has the right
columns but a multiplying eligibility join. If the SQL has no applicable entity aggregate,
return []. A physical table/alias must identify one aggregate block; mixed measures,
correlated/derived relations, outer joins and ambiguous scopes may be retained with an
explicit rejection trace, so directly express such cases correctly in candidate_sql.
Never reinterpret column meanings or add filters just to satisfy compilation. Preserve
independent reference populations and all required correlation keys. Contracts contain
question semantics, not anticipated scores or desired result values.
"""


RELATIONAL_GRAIN_PROMPT = """relational_grain_validation is measured evidence from the
submitted SQL's pre-HAVING input, grouped by its physical measured-entity primary key
and existing group keys. A repeated key means that entity contributes several joined rows.
Use this evidence to check the ontology role of each relation: output entity, measured
entity, eligibility witness, or requested weighting. Repetition is not always an error.
When a relation supplies only 'at least one' eligibility, qualify the appropriate parent
keys once and measure all requested child rows for those parents. Do not count only the
qualifying child rows when the question measures all children. Preserve joint eligibility
keys (such as entity AND event); a shared entity alone cannot replace a correlated relation.
If the question counts bonds/atoms/attendances or another entity, verify the observed
multiplicity against that actual measure grain. Do not blindly insert DISTINCT into
values, ratios or AVG: equal values from different entities must remain separate. Prefer
separate eligibility key sets and measure aggregation at the requested entity grain.
A repeated primary-key witness refutes a claim that a join is one-to-one for those rows;
a completed query or historical join pattern does not override that witness. An empty
probe only reports no repetition in this scope; a timed-out/skipped probe proves nothing.
Return the actual corrected SQL first as already required, then concise scope_checks
explaining whether each observed repeated measured key is intended and why.
"""


SCOPE_FAITHFUL_PROMPT = """Realize the recovered ontology at the scope actually requested.
Return a complete candidate_sql as the FIRST JSON field, then concise role_bindings or
scope_checks and correction_reason. This overrides instructions to put reasoning first.
Do not emit sql_edits. Keep each evidence explanation to one sentence; no schema-memory
monologue. Even when the previous candidate is empty, supply one complete executable SQL.

In correction, submitted_sql_scopes is a mechanical reading of the submitted SQL, not a
question interpretation. Compare these actual blocks with the question and ontology
witnesses. Explicitly check the key selected by each eligibility subquery, the rows feeding
each aggregate, and the key at which a HAVING threshold is tested. To count qualifying
groups, retain their GROUP BY/HAVING in an inner query and count those groups outside.
A parent eligibility condition selects parent keys; the later child measure still uses
the requested population. A shared category is not the same as the specific eligible event.

Check physical numeric operations: SQLite integer/integer division truncates. For a rate
or percentage cast an operand to REAL before dividing; multiplying an already truncated
ratio cannot restore it. Preserve supported arithmetic order, units and output columns.
Attribute names constrain the actual measured rows, not just an optional joined label.
When an attribute defines a ranking, explicitly resolve whether the question requires an
observed attribute record; never silently assign a value to missing observations.

A short execution diagnostic reaching its budget is uncertainty about runtime, not proof
of semantic error. Performance repairs must preserve predicates, NULL behavior, grouping,
weighting and reference populations. Never add a date window, change AVG to an average of
averages, or remove a GROUP BY merely to run faster or match an inferred output shape.
Repeated names alone do not authorize deduplication or invented latest/average snapshots.
For repeated correlated full scans, compute the same eligible keys or aggregates once and
semijoin them, preserving all correlation keys. A SQL rewrite must actually remove the
reported repeated scan; describing it is insufficient. Do not infer a column meaning from
remembered benchmark ordinals; use supplied history and observations, noting uncertainty.
"""


def _submitted_sql_scopes(sql: str) -> dict[str, Any]:
    """Describe actual query blocks without interpreting a question or rewriting SQL."""
    result: dict[str, Any] = {"provenance": "submitted_sql_ast", "uses_evaluator_gold": False}
    try:
        tree = sqlglot.parse_one(sql, read="sqlite")
        if not isinstance(tree, exp.Query):
            raise ValueError("No submitted query")
        selects = list(tree.find_all(exp.Select))
        blocks = []
        def render(node):
            return node.sql(dialect="sqlite")[:650] if node is not None else None
        for index, select in enumerate(selects[:16]):
            local = lambda kind: [n for n in select.find_all(kind) if n.find_ancestor(exp.Select) is select]
            group = select.args.get("group")
            blocks.append({"block": index,
                "projection": [render(n) for n in select.expressions[:12]],
                "relations": [render(n) for n in local(exp.Table)[:12]],
                "group_keys": [render(n) for n in group.expressions] if group else [],
                "where": render(select.args.get("where")),
                "having": render(select.args.get("having")),
                "order": render(select.args.get("order")),
                "joins": [render(n) for n in select.args.get("joins", [])[:8]],
                "aggregates": [render(n) for n in local(exp.AggFunc)[:12]],
                "divisions": [render(n) for n in local(exp.Div)[:8]],
                "grouped_count": bool(group and local(exp.Count))})
        result.update(state="parsed", blocks=blocks, blocks_truncated=len(selects)>16,
                      note="These are SQL facts, not evidence that the chosen scope is correct.")
    except Exception as error:
        result.update(state="unavailable", error=f"{type(error).__name__}: {error}"[:300])
    return result


REALIZED_SQL_EDIT_PROMPT = """Implement the evidence-grounded revision as executable edits to
failed_candidate_sql. This overrides earlier instructions to return a complete candidate_sql.
Return JSON with correction_reason, scope_checks, and sql_edits. Each edit has old (an exact
nonempty substring occurring ONCE in failed_candidate_sql), new (its replacement), and reason.
All edits refer to the ORIGINAL SQL, must not overlap, and are applied atomically by the
runtime. Include enough surrounding SQL to make old unique. For a structural correction,
replace the relevant complete CTE/clause block; do not merely describe it. Use an empty
sql_edits list only if the SQL needs no change. Keep at most12 edits and concise reasons.
Do not repeat the entire unchanged query. The output SQL is obtained from these edits;
prose and any candidate_sql field are not used to implement a change.

binding_validation was obtained using the configured physical execution engine. Prefer its
query plan and completion diagnostic over a successful prefix probe from another engine.
On that engine, repeated correlated full scans can be replaced with independent key-set
semijoins/grouped aggregates when semantics permit. Syntax/dialect/alias errors require an
actual edit. Retain supported join endpoints, measured-entity grain and independent scope.
Do not replace existence with a multiplying join, nor filter an attribute only on the
optional side of a LEFT JOIN while still aggregating all attribute rows.
Question literals, units and formulas are constraints, not errors to explain away using
an inferred alias. Preserve supported arithmetic order and output units; small value samples
alone do not establish which temporal label a numeric column represents. Cite direct
history/value evidence for rebinding, and acknowledge ambiguity without inventing proof.
"""


def _realize_sql_edits(sql: str, edits: Any) -> tuple[str, dict[str, Any]]:
    """Apply one model revision atomically; never synthesize an unrequested repair."""
    def rejected(reason):
        return sql, {"status": "rejected", "reason": reason, "applied": 0}
    if not isinstance(edits, list) or len(edits) > 12:
        return rejected("sql_edits must be a list of at most12 edits")
    spans = []
    for index, item in enumerate(edits):
        if not isinstance(item, dict) or not isinstance(item.get("old"), str) or not isinstance(item.get("new"), str):
            return rejected("each edit requires literal old/new strings")
        old, new = item["old"], item["new"]
        if not old or sql.count(old) != 1:
            return rejected(f"edit{index} old must occur exactly once in original SQL")
        start = sql.index(old)
        spans.append((start, start+len(old), new))
    spans.sort()
    if any(left[1] > right[0] for left, right in zip(spans, spans[1:])):
        return rejected("overlapping edits")
    candidate = sql
    for start, end, new in reversed(spans):
        candidate = candidate[:start] + new + candidate[end:]
    if not candidate.strip():
        return rejected("empty SQL after edits")
    return candidate, {"status": "applied" if spans else "unchanged", "applied": len(spans),
                       "source_sha256": sha256(sql.encode()).hexdigest(),
                       "result_sha256": sha256(candidate.encode()).hexdigest()}


def _grounded_binding_observations(db_tools: Any, plan: dict[str, Any], sql: str,
                                    execution_python: str | None = None, relational_grain: bool = False) -> dict[str, Any]:
    database = getattr(db_tools, "database", None)
    if database is None:
        return {"state": "unavailable", "uses_evaluator_gold": False}
    if execution_python:
        request = {"database": str(database), "sql": sql,
                   "binding_probes": plan.get("binding_probes", [])}
        if relational_grain:
            request["relational_grain"] = True
        process = subprocess.run([execution_python, "-m", "finsemguard.e2e.physical_sql_observer"],
                                 input=json.dumps(request), text=True, capture_output=True,
                                 timeout=40 if relational_grain else 25, check=True)
        return json.loads(process.stdout)
    probes = []
    requested = plan.get("binding_probes")
    for item in (requested[:3] if isinstance(requested, list) else []):
        if not isinstance(item, dict) or not isinstance(item.get("sql"), str):
            continue
        if len(item["sql"]) > 4000:
            probes.append({"state": "rejected", "reason": "probe exceeds4000characters"})
            continue
        probes.append({"purpose": str(item.get("purpose", ""))[:400],
                       **_bounded_binding_read(database, item["sql"])})
    observations = {"provenance": "read_only_current_physical_database", "binding_probes": probes,
            "submitted_sql_diagnostic": _bounded_binding_read(database, sql, completion=True,
                                                                timeout_seconds=3.0),
            "uses_evaluator_gold": False, "additional_model_calls": 0,
            "sqlite_version": sqlite3.sqlite_version}
    if relational_grain:
        from .relational_grain_observer import observe_relational_grain
        observations["relational_grain"] = observe_relational_grain(database, sql)
    return observations


def _binding_observations_for_prompt(observations: dict[str, Any]) -> dict[str, Any]:
    """Bound new diagnostic context; full observations remain in the task trace."""
    result = json.loads(json.dumps(observations))
    result.pop("relational_grain", None)  # v13 renders bounded grain witnesses separately
    probes = result.get("binding_probes", [])
    diagnostic = result.get("submitted_sql_diagnostic", {})
    if len(json.dumps(result, ensure_ascii=False)) <= 6000:
        return result
    result["rendering_limited_full_observations_in_trace"] = True
    diagnostic.pop("sample_rows", None)
    for item in probes:
        item["sample_rows"] = [[str(v)[:60] if isinstance(v, str) else v for v in row[:8]]
                               for row in item.get("sample_rows", [])[:1]]
        item["columns"] = item.get("columns", [])[:8]
        item["purpose"] = str(item.get("purpose", ""))[:100]
    diagnostic["query_plan"] = diagnostic.get("query_plan", [])[:12]
    # Full probe SQL is also in the planner output. Retain its hash if it alone
    # consumes the diagnostic budget; never execute a shortened SQL string.
    for item in sorted(probes, key=lambda p: len(p.get("sql", "")), reverse=True):
        if len(json.dumps(result, ensure_ascii=False)) <= 6000:
            break
        sql = item.pop("sql", "")
        item["planner_probe_sql_sha256"] = sha256(sql.encode()).hexdigest()
    return result


def _ontology_witness_packet(payload: dict[str, Any]) -> dict[str, Any]:
    """Render existing evidence once, keeping SQL and lineage atomic.

    This opt-in v8 consumer view removes duplicate graph expansions and ranking
    diagnostics, not historical computations. The complete source structures
    remain in the normal trace. It never reads evaluator material.
    """
    graph = payload.get("query_relational_program_graph") or {}
    context = payload.get("graph_evo_program_context") or {}
    current = payload.get("current_relational_program") or {}
    candidate_fields = ("physical_identifier", "physical_table", "evidence_candidate_id",
                        "evidence_kind", "required_companion_identifiers")
    roles = {
        role: [{k: candidate[k] for k in candidate_fields if k in candidate}
               for candidate in candidates if isinstance(candidate, dict)]
        for role, candidates in (graph.get("query_role_bindings") or {}).items()
    }
    evidence = []
    for item in payload.get("retrieved_evidence") or []:
        text = item.get("evidence", "")
        try:
            fact = json.loads(text)
        except (ValueError, TypeError):
            fact = text
        evidence.append({"id": item.get("evidence_candidate_id"),
                         "kind": item.get("kind"), "content": fact})
    # History expressions and their provenance are retained in full. Avoid
    # duplicating a selected program already present as retrieved evidence.
    evidence_ids = {item["id"] for item in evidence}
    programs = [program for program in context.get("historical_programs", [])
                if program.get("provenance_id") not in evidence_ids]
    packet = {k: payload[k] for k in (
        "database", "sql_dialect", "question", "benchmark_knowledge", "query_contract",
        "physical_schema_inventory", "database_grounding", "current_schema_for_program",
        "base_solution_anchor", "auxiliary_raw_evidence_draft",
        "persistent_recovery_advisory_draft", "evidence_bound_program_prior",
        "recovered_column_hypotheses") if k in payload}
    packet.update(
        history_consumer_version="ontology_witness_consistent_v8",
        ontology_evidence=evidence, additional_historical_programs=programs,
        proposed_role_candidates=roles,
        typed_join_edges=context.get("typed_join_edges", []),
        evolution_contract=context.get("evolution_contract", []),
        metric_time_unit_constraints=context.get("metric_time_unit_constraints", []),
        proposed_program_contract={k: current[k] for k in (
            "projection_contract", "predicate_contract", "base_draft_contract") if k in current},
        evidence_policy="Observed expressions/values are distinct from inferred aliases and draft hypotheses",
    )
    return packet


def _physical_value_witnesses(db_tools: Any) -> dict[str, Any]:
    """Bounded raw row sample using only the already allowed physical database.

    No GROUP BY/full scan, semantic mapping, generated SQL, target result, or
    evaluator is involved. These are observations for ontology interpretation,
    not proof that an unseen value does not exist.
    """
    database = getattr(db_tools, "database", None)
    if database is None:
        return {"state": "unavailable", "tables": []}
    connection = sqlite3.connect(f"file:{database}?mode=ro", uri=True)
    deadline = time.monotonic() + 3.0
    connection.set_progress_handler(lambda: int(time.monotonic() > deadline), 1000)
    output = []
    try:
        for table, columns in sorted(db_tools.columns.items()):
            if time.monotonic() >= deadline:
                break
            # Only physical names already present in the online catalog.
            names = [str(item[0]) for item in columns]
            if not names:
                continue
            try:
                rows = connection.execute(
                    'SELECT ' + ','.join(_quote(name) for name in names)
                    + ' FROM ' + _quote(table) + ' LIMIT 5').fetchall()
            except sqlite3.Error:
                continue
            fields = []
            for index, (name, declared_type) in enumerate(columns):
                values = []
                for row in rows:
                    value = _safe_value(row[index])
                    if isinstance(value, str) and len(value) > 100:
                        value = value[:100] + " [sample cell truncated]"
                    if value not in values:
                        values.append(value)
                fields.append({"column": name, "type": declared_type, "sample_values": values})
            output.append({"table": table, "columns": fields, "sampled_rows": len(rows)})
    finally:
        connection.close()
    return {"provenance": "read_only_physical_database_first5_rows_per_table",
            "not_exhaustive": True, "tables": output}


TARGET_ISOLATED_DEMONSTRATION_PROMPT = """Use target_isolated_demonstrations only as
evidence-carrying historical program examples, never as target answers. Reuse a
demonstration only when its current-bound roles and required operator signature match this
question. If both match, preserve its CTE/subquery boundaries, composite join keys, join
multiplicity, grouping grain, HAVING, window frame, set operation, tie handling, and
recursive direction. Otherwise use it only as an operator hint. Never import a demo-only
table, predicate, literal, output, grouping key, ORDER BY, or LIMIT. Before returning
candidate_sql, verify every requested role once, every join on a certified edge, all target
literals, and the exact requested output shape. Use only functions supported by sql_dialect
and avoid reserved-word aliases. Return exactly one JSON object with no Markdown fences,
comments, nested examples, or prose outside JSON; candidate_sql must contain exactly one
read-only query."""

BASIC_EXECUTION_CORRECTION_PROMPT = """Repair exactly one failed SQL submission using
only the supplied error/contract feedback and the same evidence-carrying relational
program. This is not candidate selection. Preserve every clause that is unrelated to the
concrete failure, do not import a new table, literal, output, grouping key, ORDER BY, or
LIMIT without explicit current-question evidence, and do not simplify supported CTE,
HAVING, window, set-operation, recursive, or composite-join structure. Return exactly one
JSON object with candidate_sql and correction_reason. candidate_sql must be one complete
read-only query in sql_dialect, with no Markdown fence, escaped newline prefix, comment, or
explanation outside the JSON object. When correction_reason identifies a concrete change,
candidate_sql must actually apply it; never return the unchanged failing SQL."""

CHESS_PROMPT = """Follow a CHESS-style database-grounded workflow using only the raw
physical catalog and database observations supplied to this arm. First focus the catalog
retrieval and exact value matches on the question. Inspect authoritative DDL only where
needed, recover required joins, and execute a complete candidate no later than turn two.
Use the remaining turn to revise concrete projection, predicate, aggregation, grouping,
ordering, value, or join errors exposed by the database result. Do not invent a business
dictionary, historical mapping, recovered alias, or ontology edge. Always submit the
best revised SQL on the final turn."""

AUTOLINK_PROMPT = """Follow a bounded AutoLink-style schema exploration workflow using
only the raw physical catalog and database observations supplied to this arm. Treat the
initial schema search as a seed. If a required output, filter, value, aggregation, entity,
or join role is still missing, call targeted_expand_schema exactly once with one to three
short role-specific retrieval probes. Then inspect only the most relevant physical
tables/values/joins, execute the best complete SQL by turn three, and submit on the final
turn. The expansion cannot use recovered aliases, historical SQL, a business KB, or an
ontology."""

EVOSCHEMA_RAW_PROMPT = """The database catalog is the current schema after an unknown
schema evolution. Use only the current physical identifiers, current database values,
declared joins, and bounded execution. You have no prior schema snapshot, rename lineage,
historical workload, business KB, or ontology. Never use a legacy identifier that is absent
from the current catalog."""

EVOSCHEMA_FULL_PROMPT = """The database catalog is the current schema after schema
evolution. The search index additionally contains automatically recovered rename lineage
from a previous-versus-current schema diff, target-isolated historical question/SQL
patterns compiled onto current identifiers, and a typed operational relationship graph.
Map historical/business terms to the bound current physical identifiers, adapt retrieved
SQL patterns to the present question, then use only current identifiers in SQL. Verify
projection, values, and joins against the current catalog and database before submission."""


_QUESTION_WORDS = {
    "among",
    "between",
    "calculate",
    "find",
    "for",
    "from",
    "give",
    "how",
    "in",
    "list",
    "please",
    "show",
    "the",
    "what",
    "when",
    "where",
    "which",
    "who",
    "whose",
    "with",
    "year",
}


def _quote(identifier: str) -> str:
    return '"' + identifier.replace('"', '""') + '"'


def _terms(text: str) -> set[str]:
    return {
        token.casefold()
        for token in re.findall(r"[A-Za-z0-9_]+|[\u3400-\u9fff]+", text)
        if len(token) > 1 or token.isdigit()
    }


_ROLE_FIELD_TERMS = {
    "address",
    "amount",
    "balance",
    "city",
    "code",
    "comment",
    "count",
    "country",
    "date",
    "day",
    "diagnosis",
    "email",
    "element",
    "id",
    "identifier",
    "month",
    "name",
    "number",
    "phone",
    "score",
    "status",
    "street",
    "text",
    "time",
    "title",
    "year",
    "zip",
}


def _identifier_parts(value: str) -> set[str]:
    """Split SQL identifiers without discarding their compact spelling."""

    output: set[str] = set()
    for token in re.findall(r"[A-Za-z0-9]+", str(value).replace("_", " ")):
        pieces = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", token)
        pieces = re.sub(r"(?<=[A-Za-z])(?=\d)|(?<=\d)(?=[A-Za-z])", " ", pieces).split()
        pieces = [piece.casefold() for piece in pieces if piece]
        if len(token) > 1 or token.isdigit():
            output.add(token.casefold())
        output.update(piece for piece in pieces if len(piece) > 1 or piece.isdigit())
    return output


def _canonical_role_terms(value: str) -> set[str]:
    value = re.sub(r"\be[\s_-]*mail\b", "email", str(value), flags=re.I)
    aliases = {
        "addresse": "address",
        "avg": "average",
        "comments": "comment",
        "consumed": "consumption",
        "diagnosed": "diagnosis",
        "diagnoses": "diagnosis",
        "disease": "diagnosis",
        "usage": "consumption",
        "use": "consumption",
        "identifier": "id",
        "ids": "id",
        "mailing": "mail",
        "names": "name",
        "nation": "country",
        "nationality": "country",
        "num": "number",
        "reading": "read",
        "scr": "score",
        "texts": "text",
    }
    terms: set[str] = set()
    for token in _identifier_parts(value):
        singular = token[:-1] if len(token) > 4 and token.endswith("s") else token
        canonical = aliases.get(singular, singular)
        terms.add(canonical)
        if canonical in {"comment", "content", "message", "note", "text"}:
            terms.add("content")
        if canonical in {"date", "day", "month", "year"}:
            terms.add("date_component")
    return terms


def _role_identifier_alignment(
    role: str, physical_identifier: str, *, evidence_kind: str = ""
) -> dict[str, Any]:
    """Return an auditable lexical guard for one retrieved role binding.

    Dense retrieval remains useful for opaque identifiers.  This score only
    overrides it when the physical field itself supplies positive or negative
    lexical evidence; table-name overlap is deliberately weaker than column
    overlap so ``comments.Id`` cannot satisfy an output request for comment text.
    """

    role_type, separator, phrase = str(role).partition(" role: ")
    if not separator:
        role_type, phrase = "untyped", str(role)
    table, dot, column = str(physical_identifier).rpartition(".")
    if not dot:
        table, column = "", str(physical_identifier)
    role_terms = _canonical_role_terms(phrase)
    field_phrase = phrase
    context_phrase = ""
    if role_type.casefold() == "output":
        field_context = re.match(
            r"^(.{1,80}?)\s+(?:of|for)\s+(?:the\s+)?(.+)$",
            phrase,
            flags=re.I,
        )
        if field_context:
            field_phrase = field_context.group(1)
            context_phrase = field_context.group(2)
    field_role_terms = _canonical_role_terms(field_phrase)
    context_role_terms = _canonical_role_terms(context_phrase)
    column_terms = _canonical_role_terms(column)
    table_terms = _canonical_role_terms(table)
    field_overlap = sorted(field_role_terms & column_terms)
    context_column_overlap = sorted(context_role_terms & column_terms)
    table_overlap = sorted(role_terms & table_terms)
    score = (
        3.0 * len(field_overlap)
        + 1.0 * len(context_column_overlap)
        + 0.35 * len(table_overlap)
    )
    penalties: list[str] = []
    if role_type.casefold() == "output":
        if "id" in column_terms and "id" not in role_terms:
            score -= 3.0
            penalties.append("unrequested_identifier_output")
        if "code" in column_terms and not ({"code", "id"} & role_terms):
            score -= 2.5
            penalties.append("unrequested_code_output")
        if {"count", "number"} & column_terms and not (
            {"count", "number"} & role_terms
        ):
            score -= 2.0
            penalties.append("unrequested_count_output")
    if role_type.casefold() in {"filter", "ordering"}:
        if "id" in column_terms and "id" not in role_terms:
            score -= 2.5
            penalties.append("unrequested_identifier_role")
        if "code" in column_terms and not ({"code", "id"} & role_terms):
            score -= 2.0
            penalties.append("unrequested_code_role")
    lineage_bonus = 0.25 if (
        field_overlap and str(evidence_kind).startswith("schema_evolution_")
    ) else 0.0
    score += lineage_bonus
    return {
        "score": round(score, 8),
        "field_overlap": field_overlap,
        "context_column_overlap": context_column_overlap,
        "table_overlap": table_overlap,
        "lineage_bonus": lineage_bonus,
        "penalties": penalties,
        "status": (
            "lexically_supported"
            if score > 0
            else "lexically_contradicted"
            if score < 0
            else "opaque_or_unresolved"
        ),
    }


_PROGRAM_TOPIC_STOPWORDS = _QUESTION_WORDS | {
    "across",
    "after",
    "about",
    "according",
    "an",
    "all",
    "also",
    "along",
    "and",
    "answer",
    "any",
    "are",
    "as",
    "at",
    "average",
    "be",
    "been",
    "before",
    "both",
    "by",
    "code",
    "column",
    "considering",
    "count",
    "date",
    "different",
    "entity",
    "deviation",
    "display",
    "distinct",
    "do",
    "each",
    "ensure",
    "every",
    "formatted",
    "filter",
    "group",
    "grouping",
    "has",
    "have",
    "include",
    "into",
    "is",
    "it",
    "its",
    "key",
    "matching",
    "maximum",
    "minimum",
    "most",
    "name",
    "never",
    "no",
    "not",
    "number",
    "of",
    "on",
    "one",
    "only",
    "order",
    "ordering",
    "other",
    "output",
    "per",
    "provide",
    "range",
    "rank",
    "ranking",
    "result",
    "return",
    "role",
    "rounded",
    "row",
    "separately",
    "show",
    "standard",
    "status",
    "sum",
    "table",
    "than",
    "tie",
    "ties",
    "that",
    "these",
    "their",
    "then",
    "this",
    "those",
    "time",
    "to",
    "total",
    "type",
    "unique",
    "use",
    "using",
    "value",
    "variance",
    "was",
    "were",
    "window",
    "without",
}


def _topic_terms(text: str) -> set[str]:
    """Return entity-bearing terms, excluding generic query/SQL vocabulary."""

    output: set[str] = set()
    for token in _terms(str(text).replace("_", " ")):
        if token in _PROGRAM_TOPIC_STOPWORDS or token.isdigit():
            continue
        if len(token) > 4 and token.endswith("ies"):
            token = token[:-3] + "y"
        elif len(token) > 4 and token.endswith("s") and not token.endswith("ss"):
            token = token[:-1]
        if token not in _PROGRAM_TOPIC_STOPWORDS:
            output.add(token)
    return output


def _query_role_phrases(text: str, *, limit: int = 10) -> list[str]:
    """Split a question into compact schema-role probes without an LLM call."""

    # Benchmark hints improve global evidence retrieval but are not part of the
    # requested SQL roles.  Keeping the envelope here created terminals such as
    # ``Benchmark knowledge evidence`` on BIRD.
    question_only = re.split(
        r"\n\s*Benchmark knowledge evidence\s*:",
        str(text),
        maxsplit=1,
        flags=re.I,
    )[0]
    cleaned = re.sub(r"<[^>]+>", " ", question_only)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    fragments = re.split(
        r"\s*(?:[,;:.?]|\b(?:and|along with|as well as|plus|with|where|whose|that|considering)\b)\s*",
        cleaned,
        flags=re.I,
    )
    output: list[str] = []
    observed: set[str] = set()
    for fragment in fragments:
        fragment = re.sub(
            r"^(?:(?:for\s+)?each|list|show|provide|include|also|return|"
            r"state|indicate|identify|find|give|display|tell|calculate|compute|"
            r"what\s+is|what\s+are)\s+",
            "",
            fragment.strip(),
            flags=re.I,
        )
        topics = _topic_terms(fragment)
        if not topics:
            continue
        words = fragment.split()
        if len(words) > 18:
            # Long condition clauses make every role probe resemble the full
            # question. Keep the entity-bearing terms in their source order.
            compact: list[str] = []
            for word in words:
                normalized = next(iter(_topic_terms(word)), "")
                if normalized and normalized not in compact:
                    compact.append(normalized)
            fragment = " ".join(compact[:12])
        key = " ".join(fragment.casefold().split())
        if key and key not in observed:
            observed.add(key)
            output.append(fragment)
            if len(output) >= limit:
                break
    if not output:
        output = sorted(_topic_terms(cleaned))[:limit]
    return output


def _minimal_join_tree_role_phrases(
    text: str, *, limit: int = 12
) -> list[str]:
    """Return a typed query-role contract from the schema-free question.

    These are retrieval roles, not free-form sentence fragments.  Typing keeps
    output, filter, aggregation, grouping, ordering, literal, entity, and join
    evidence distinct and prevents imperative/action words from becoming graph
    terminals.
    """

    question_only = re.split(
        r"\n\s*Benchmark knowledge evidence\s*:",
        str(text),
        maxsplit=1,
        flags=re.I,
    )[0]
    cleaned = re.sub(r"<[^>]+>", " ", question_only)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    aggregate_markers = (
        "average",
        "avg",
        "count",
        "how many",
        "maximum",
        "minimum",
        "number of",
        "percentage",
        "ratio",
        "rate",
        "sum",
        "total",
    )
    order_markers = (
        "biggest",
        "bottom",
        "earliest",
        "first",
        "fewest",
        "highest",
        "last",
        "largest",
        "latest",
        "least",
        "lowest",
        "most",
        "smallest",
        "top",
    )
    filter_markers = (
        "after",
        "at least",
        "at most",
        "before",
        "between",
        "equal",
        "greater",
        "less",
        "more",
        "over",
        "under",
        "without",
    )
    group_markers = ("each", "every", "grouped by", "per")
    join_markers = ("associated", "belong", "linked", "related")

    def has_marker(value: str, markers: tuple[str, ...]) -> bool:
        folded = " ".join(value.casefold().split())
        return any(
            re.search(
                rf"(?<![\w]){re.escape(marker).replace(r'\ ', r'\s+')}(?![\w])",
                folded,
            )
            for marker in markers
        )

    def clean_phrase(value: str) -> str:
        value = re.sub(r"\s+", " ", value).strip(" ,;:.?")
        value = re.sub(r"^(?:also\s+)+", "", value, flags=re.I)
        value = re.sub(r"^(?:(?:please\s+)?(?:list|show|provide|include|return|"
                       r"state|indicate|identify|find|give|display|tell|calculate|"
                       r"compute)\s+)+", "", value, flags=re.I)
        value = re.sub(r"^(?:the|a|an)\s+", "", value, flags=re.I)
        value = re.sub(
            r"\s+(?:get|gets|got|receive|receives|received|have|has|had)$",
            "",
            value,
            flags=re.I,
        )
        return value.strip(" ,;:.?")

    typed: list[tuple[str, str]] = []

    def add(role: str, value: str) -> None:
        phrase = clean_phrase(value)
        role_field_terms = _canonical_role_terms(phrase) & _ROLE_FIELD_TERMS
        if phrase and (
            role == "literal" or _topic_terms(phrase) or role_field_terms
        ):
            typed.append((role, phrase))

    def classify(value: str, *, default: str = "output") -> str:
        folded = value.casefold()
        order_value = value
        if re.search(r"\blast\s+(?:access|edit|login|modified|update)\b", folded):
            order_value = re.sub(r"\blast\b", "", value, flags=re.I)
        if has_marker(order_value, order_markers):
            return "ordering"
        if _NAMED_MEASURE_LOOKUP.search(folded):
            return default
        if has_marker(value, aggregate_markers):
            return "aggregation"
        if has_marker(value, group_markers):
            return "grouping"
        if has_marker(value, filter_markers):
            return "filter"
        if has_marker(value, join_markers):
            return "join"
        return default

    def split_sentences(value: str) -> list[str]:
        """Split benchmark prose while preserving punctuation inside quotes."""

        output: list[str] = []
        current: list[str] = []
        quote: str | None = None
        for index, character in enumerate(value):
            previous = value[index - 1] if index else ""
            following = value[index + 1] if index + 1 < len(value) else ""
            if character in {'"', "'"}:
                apostrophe = (
                    character == "'" and previous.isalnum() and following.isalnum()
                )
                if not apostrophe:
                    if quote == character:
                        quote = None
                    elif quote is None:
                        quote = character
            boundary = quote is None and (
                character in "?!;"
                or (
                    character == "."
                    and (not following or following.isspace())
                )
            )
            if boundary:
                sentence = "".join(current).strip()
                if sentence:
                    output.append(sentence)
                current = []
            else:
                current.append(character)
        sentence = "".join(current).strip()
        if sentence:
            output.append(sentence)
        return output

    relative_pattern = re.compile(
        r"\b(?:where|whose|that|which|who|with|having|when)\b",
        flags=re.I,
    )

    def split_relative(value: str) -> tuple[str, str]:
        match = relative_pattern.search(value)
        if match is None:
            return value, ""
        return value[: match.start()], value[match.end() :]

    def add_conditions(value: str, *, default: str = "filter") -> None:
        fragments = relative_pattern.split(value)
        for fragment in fragments:
            clauses = re.split(
                r"\band\b(?=\s+(?:the\s+)?(?:\S+\s+){0,5}"
                r"(?:is|are|was|were|has|have|had|does|do|did)\b)",
                fragment,
                flags=re.I,
            )
            for clause in clauses:
                clause = re.sub(
                    r"^(?:is|are|was|were|has|have|had|does|do|did)\s+",
                    "",
                    clause.strip(),
                    flags=re.I,
                )
                currency = re.search(
                    r"\b(?:paid|priced|denominated)\s+in\s+([A-Z]{3})\b",
                    clause,
                )
                if currency:
                    add("filter", f"currency {currency.group(1)}")
                most_measure = re.search(
                    r"\b(?:the\s+)?most\s+(.+?)(?:\s+(?:paid|priced|"
                    r"denominated)\s+in\s+[A-Z]{3})?$",
                    clause,
                    flags=re.I,
                )
                if most_measure:
                    add("ordering", f"most {most_measure.group(1)}")
                    continue
                if clause:
                    add(classify(clause, default=default), clause)

    def add_output(value: str, *, split_conjunctions: bool = True) -> None:
        main, conditions = split_relative(value)
        main = main.strip()
        shared_entity = re.match(
            r"^(.+?)\s+and\s+(.+?)\s+of\s+(?:the\s+)?(.+)$",
            main,
            flags=re.I,
        )
        if (
            shared_entity
            and split_conjunctions
            and "," not in main
            and not has_marker(shared_entity.group(3), order_markers)
        ):
            entity = shared_entity.group(3)
            add_output(
                f"{shared_entity.group(1)} of {entity}",
                split_conjunctions=False,
            )
            add_output(
                f"{shared_entity.group(2)} of {entity}",
                split_conjunctions=False,
            )
            add("entity", entity)
            if conditions:
                add_conditions(conditions)
            return
        status_target = re.match(
            r"^(?:all\s+|all\s+the\s+|the\s+)?"
            r"(active|inactive|approved|cancelled|closed|completed|disabled|"
            r"enabled|open|pending)\s+(.+)$",
            main,
            flags=re.I,
        )
        if status_target:
            add("output", status_target.group(2))
            add("filter", f"status {status_target.group(1)}")
            if conditions:
                add_conditions(conditions)
            return
        if re.match(
            r"^(?:all\s+|all\s+the\s+|the\s+)?comments?\s+"
            r"(?:left|made|posted|written)\s+by\b",
            main,
            flags=re.I,
        ):
            main = "comment text"
        if split_conjunctions and not re.search(r"\bbetween\b|[—–]", main, flags=re.I):
            fragments = re.split(
                r"\s*(?:,(?=\s*[A-Za-z])|\band\b|\balong with\b|"
                r"\bas well as\b|\bplus\b)\s*",
                main,
                flags=re.I,
            )
        else:
            fragments = [main]
        for fragment in fragments:
            role = classify(fragment)
            measure_entity = re.match(
                r"^(.{1,80}?)\s+for\s+(.+)$", fragment, flags=re.I
            )
            if (
                role == "output"
                and measure_entity
                and (
                    _canonical_role_terms(measure_entity.group(1))
                    & _ROLE_FIELD_TERMS
                )
            ):
                add("output", measure_entity.group(1))
                add("entity", measure_entity.group(2))
                continue
            field_entity = re.match(
                r"^(.{1,80}?)\s+of\s+(?:the\s+)?(.+)$",
                fragment,
                flags=re.I,
            )
            if (
                role == "output"
                and field_entity
                and (
                    _canonical_role_terms(field_entity.group(1))
                    & _ROLE_FIELD_TERMS
                )
            ):
                add(
                    "output",
                    f"{field_entity.group(1)} of {field_entity.group(2)}",
                )
                add("entity", field_entity.group(2))
                continue
            ordered_output = re.match(
                r"^(.{1,60}?)\s+of\s+(?:the\s+)?(.+)$",
                fragment,
                flags=re.I,
            )
            if (
                role == "ordering"
                and ordered_output
                and has_marker(ordered_output.group(2), order_markers)
            ):
                # ``date of the last round`` contains both a projected field
                # and an ordering condition.  Treating the whole phrase only as
                # ordering erased the compound date projection.
                add("output", ordered_output.group(1))
                add("ordering", ordered_output.group(2))
            else:
                add(role, fragment)
        if conditions:
            add_conditions(conditions)

    def add_measure_and_entity(value: str) -> None:
        """Separate a compact requested field from a long ``of/for`` entity."""

        match = re.match(r"^(.{1,80}?)\s+(?:of|for)\s+(.+)$", value, flags=re.I)
        if (
            match
            and "," not in value
            and len(match.group(1).split()) <= 8
            and (
                _topic_terms(match.group(1))
                or (
                    _canonical_role_terms(match.group(1))
                    & _ROLE_FIELD_TERMS
                )
            )
            and _topic_terms(match.group(2))
        ):
            add(
                classify(match.group(1)),
                f"{match.group(1)} of {match.group(2)}",
            )
            add("entity", match.group(2))
        else:
            add_output(value)

    def parse_sentence(sentence: str) -> None:
        sentence = sentence.strip(" ,;:.?")
        if not sentence:
            return
        sentence = re.sub(
            r"^if\s+there\s+are\s+any\s*,\s*",
            "",
            sentence,
            flags=re.I,
        )
        followup = re.split(
            r"\s+and\s+(?=(?:how\s+much|how\s+many|what|which|who)\b)",
            sentence,
            maxsplit=1,
            flags=re.I,
        )
        if len(followup) == 2:
            parse_sentence(followup[0])
            parse_sentence(followup[1])
            return
        preamble = re.match(
            r"^(?:among|in|for)\s+(.+?),\s*(.+)$",
            sentence,
            flags=re.I,
        )
        if preamble:
            add("filter", preamble.group(1))
            parse_sentence(preamble.group(2))
            return

        in_which = re.match(
            r"^in\s+which\s+(.+?)\s+can\s+(?:you\s+)?find\s+(.+)$",
            sentence,
            flags=re.I,
        )
        if in_which:
            add("output", in_which.group(1))
            entity, conditions = split_relative(in_which.group(2))
            add("entity", entity)
            if conditions:
                add_conditions(conditions)
            return

        how_much = re.match(
            r"^how\s+much\s+(.+?)\s+"
            r"(?:does|do|did|is|are|was|were|has|have|had|will|can)\s+(.+)$",
            sentence,
            flags=re.I,
        )
        if how_much:
            add("output", how_much.group(1))
            add("entity", how_much.group(2))
            return
        how_much_value = re.match(
            r"^how\s+much\s+(?:is|are|was|were)\s+(.+)$",
            sentence,
            flags=re.I,
        )
        if how_much_value:
            add("output", how_much_value.group(1))
            return

        named_measure = re.match(
            r"^how\s+many\s+"
            r"((?:the\s+)?(?:number|amount|quantity|volume|value)\s+of\s+.+?)"
            r"\s+(?:is|are|was|were)\s+(.+)$",
            sentence,
            flags=re.I,
        )
        if named_measure:
            add("output", named_measure.group(1))
            add_conditions(named_measure.group(2))
            return

        if re.match(r"^how\s+many\b", sentence, flags=re.I):
            body = re.sub(r"^how\s+many\s+", "", sentence, flags=re.I)
            split = re.split(
                r"\b(?:which|who|that|where|with|were|are|was|is|had|have|has|did|do|does)\b",
                body,
                maxsplit=1,
                flags=re.I,
            )
            target = split[0].strip()
            possessive = re.match(
                r"^(?:(female|male)\s+)?(.+?)(?:'s|s')\s+(.+)$",
                target,
                flags=re.I,
            )
            owner = ""
            if possessive:
                gender, owner, owned = possessive.groups()
                owner = owner.strip()
                if owner.casefold().endswith("s"):
                    owner = owner[:-1]
                add("aggregation", f"count of {owned}")
                add("entity", owner)
                add("join", f"{owner} ownership of {owned}")
                if gender:
                    add("filter", f"{owner} gender {gender}")
            else:
                gender_target = re.match(
                    r"^(female|male)\s+(.+)$", target, flags=re.I
                )
                if gender_target:
                    add("aggregation", f"count of {gender_target.group(2)}")
                    add("filter", f"gender {gender_target.group(1)}")
                else:
                    add("aggregation", f"count of {target}")
            if len(split) == 2:
                condition = split[1]
                if owner:
                    add("filter", f"{owner} {condition}")
                else:
                    add_conditions(condition)
            return

        if re.match(r"^which\b", sentence, flags=re.I):
            body = re.sub(r"^which\s+", "", sentence, flags=re.I)
            predicate = re.search(
                r"\b(?:reported?|paying|consumed?|obtained?|received?|offers?|"
                r"record(?:ed|s)?|got|gets|has|have|had|is|are|was|were|"
                r"does|do|did)\b",
                body,
                flags=re.I,
            )
            if predicate is not None:
                target = body[: predicate.start()].strip(" ,—–")
                target = re.sub(r"^of\s+", "", target, flags=re.I)
                predicate_body = re.sub(
                    r"^(?:is|are|was|were|has|have|had|does|do|did)\s+",
                    "",
                    body[predicate.start() :],
                    flags=re.I,
                )
                entity_head, relative_conditions = split_relative(predicate_body)
                if (
                    relative_conditions
                    and (_canonical_role_terms(target) & _ROLE_FIELD_TERMS)
                    and _topic_terms(entity_head)
                ):
                    add("output", f"{target} of {entity_head}")
                    add("entity", entity_head)
                    add_conditions(relative_conditions)
                    return
                status_target = re.match(
                    r"^(active|inactive|approved|cancelled|closed|completed|"
                    r"disabled|enabled|open|pending)\s+(.+)$",
                    target,
                    flags=re.I,
                )
                if status_target:
                    add("output", status_target.group(2))
                    add("filter", f"status {status_target.group(1)}")
                else:
                    add("output", target)
                add_conditions(body[predicate.start() :])
            else:
                add_output(body)
            return

        what_prefix = re.match(
            r"^what\s+(?:is|are|was|were)\s+(.+)$",
            sentence,
            flags=re.I,
        )
        if what_prefix:
            main, conditions = split_relative(what_prefix.group(1))
            add_measure_and_entity(main)
            if conditions:
                add_conditions(conditions)
            return

        what_infix = re.match(
            r"^what\s+(.+?)\s+(?:is|are|was|were)\s+(.+)$",
            sentence,
            flags=re.I,
        )
        if what_infix:
            requested = what_infix.group(1)
            predicate = what_infix.group(2)
            entity_head, relative_conditions = split_relative(predicate)
            if (
                relative_conditions
                and (
                    _canonical_role_terms(requested) & _ROLE_FIELD_TERMS
                )
                and _topic_terms(entity_head)
            ):
                add("output", f"{requested} of {entity_head}")
                add("entity", entity_head)
                add_conditions(relative_conditions)
                return
            add(classify(requested), requested)
            default = (
                "entity"
                if re.match(r"^(?:in|from|of|to)\b", predicate, flags=re.I)
                else "filter"
            )
            predicate = re.sub(r"^(?:in|from|of|to)\s+", "", predicate, flags=re.I)
            add_conditions(predicate, default=default)
            return

        if re.match(r"^who\b", sentence, flags=re.I):
            add_conditions(re.sub(r"^who\s+", "", sentence, flags=re.I))
            return

        body = re.sub(
            r"^(?:(?:please\s+)?(?:list|show|provide|include|return|state|"
            r"indicate|identify|find|give|display|tell|calculate|compute|name|"
            r"write)\s+)+",
            "",
            sentence,
            flags=re.I,
        )
        by_split = re.split(r"\s+by\s+", body, maxsplit=1, flags=re.I)
        if len(by_split) == 2 and (
            has_marker(by_split[0], order_markers)
            or has_marker(by_split[1], aggregate_markers)
        ):
            add(classify(by_split[0]), by_split[0])
            add(classify(by_split[1], default="grouping"), by_split[1])
        else:
            add_output(body)

    for sentence in split_sentences(cleaned):
        parse_sentence(sentence)

    occupied: list[tuple[int, int]] = []
    for match in re.finditer(r"['\"]([^'\"]{1,200})['\"]", cleaned):
        add("literal", match.group(1))
        occupied.append(match.span())
    date_patterns = (
        r"\b\d{4}/\d{1,2}/\d{1,2}\s+\d{1,2}:\d{2}:\d{2}\b",
        r"\b(?:\d{1,2}/\d{1,2}/\d{4}|\d{4}/\d{1,2}/\d{1,2})\b",
        r"\b\d{1,2}:\d{2}:\d{2}\b",
        r"\b\d{1,3}(?:,\d{3})*(?:\.\d+)?\s*[-–]\s*"
        r"\d{1,3}(?:,\d{3})*(?:\.\d+)?\b",
    )
    for pattern in date_patterns:
        for match in re.finditer(pattern, cleaned):
            if any(
                start <= match.start() and match.end() <= end
                for start, end in occupied
            ):
                continue
            add("literal", match.group(0))
            occupied.append(match.span())
    number_pattern = r"\b(?:\d{1,3}(?:,\d{3})+(?:\.\d+)?|\d+(?:\.\d+)?)\b"
    for match in re.finditer(number_pattern, cleaned):
        if any(start <= match.start() and match.end() <= end for start, end in occupied):
            continue
        add("literal", match.group(0))

    output: list[str] = []
    observed: set[tuple[str, str]] = set()
    for role, phrase in typed:
        phrase = re.sub(r"\s+", " ", phrase).strip(" ,;:.?")
        key = role, phrase.casefold()
        if not phrase or key in observed:
            continue
        observed.add(key)
        output.append(f"{role} role: {phrase}")
        if len(output) >= limit:
            break
    if output:
        return output
    return [
        f"entity role: {value}"
        for value in _query_role_phrases(cleaned, limit=limit)
    ]


def _safe_value(value: Any) -> Any:
    if value is None or isinstance(value, (bool, int, float)):
        return value
    if isinstance(value, bytes):
        return "0x" + value[:64].hex()
    text = str(value)
    return text if len(text) <= 500 else text[:497] + "..."


def _numeric_equal(left: str, right: str) -> bool:
    pattern = r"-?(?:\d+(?:\.\d*)?|\.\d+)"
    if not re.fullmatch(pattern, left) or not re.fullmatch(pattern, right):
        return False
    return float(left) == float(right)


def _append_unique(output: list[str], value: str, *, limit: int = 12) -> None:
    # Regex callers already delimit unquoted tokens.  Quoted database literals
    # may legitimately end in punctuation (for example a post title ending in
    # ``?``), so stripping punctuation here corrupts exact value grounding.
    value = value.strip()
    if not value or len(value) > 200:
        return
    if value.casefold() not in {item.casefold() for item in output} and len(output) < limit:
        output.append(value)


def question_literal_candidates(
    question: str, benchmark_evidence: str = "", *, limit: int = 12
) -> list[str]:
    """Extract high-precision value probes without consulting labels or SQL gold."""

    output: list[str] = []
    top_match = re.search(r"\b(?:top|first)\s+(\d+)\b", question, flags=re.I)
    top_n = top_match.group(1) if top_match else None
    quoted_question_spans: list[tuple[int, int]] = []

    def quoted(text: str, *, record_spans: bool = False) -> None:
        for match in re.finditer(r"['\"]([^'\"]{1,200})['\"]", text):
            _append_unique(output, match.group(1), limit=limit)
            if record_spans:
                quoted_question_spans.append(match.span())

    def dates_and_decimals(text: str) -> None:
        for value in re.findall(r"\b\d{4}[/-]\d{1,2}[/-]\d{1,2}\b", text):
            _append_unique(output, value, limit=limit)
        for value in re.findall(r"(?<![\w.])-?\d+\.\d+(?![\w.])", text):
            _append_unique(output, value, limit=limit)

    quoted(question, record_spans=True)
    dates_and_decimals(question)
    multiword_spans: list[tuple[int, int]] = []
    for match in re.finditer(
        r"\b[A-Z][A-Za-z0-9_'’-]+(?:\s+[A-Z][A-Za-z0-9_'’-]+){1,3}\b",
        question,
    ):
        if any(
            start <= match.start() and match.end() <= end
            for start, end in quoted_question_spans
        ):
            continue
        phrase = match.group(0)
        if phrase.split()[0].casefold() not in _QUESTION_WORDS:
            _append_unique(output, phrase, limit=limit)
            multiword_spans.append(match.span())
    quoted(benchmark_evidence)
    dates_and_decimals(benchmark_evidence)
    excluded_numeric_spans = [
        match.span()
        for pattern in (
            r"\b\d{4}[/-]\d{1,2}[/-]\d{1,2}\b",
            r"(?<![\w.])-?\d+\.\d+(?![\w.])",
            r"\b(?:top|first)\s+\d+\b",
        )
        for match in re.finditer(pattern, question, flags=re.I)
    ] + quoted_question_spans
    for match in re.finditer(r"(?<![\w.])-?\d+(?![\w.])", question):
        if any(
            start <= match.start() and match.end() <= end
            for start, end in excluded_numeric_spans
        ):
            continue
        value = match.group(0)
        if value != top_n:
            _append_unique(output, value, limit=limit)
    for index, match in enumerate(re.finditer(r"\b[A-Z][A-Za-z0-9_'’-]+\b", question)):
        value = match.group(0)
        if (
            index == 0
            or value.casefold() in _QUESTION_WORDS
            or any(
                start <= match.start() and match.end() <= end
                for start, end in quoted_question_spans
            )
            or any(
                start <= match.start() and match.end() <= end
                for start, end in multiword_spans
            )
        ):
            continue
        _append_unique(output, value, limit=limit)
    return output


def compile_query_contract(question: str, *, conservative: bool = False) -> dict[str, Any]:
    """Compile only unambiguous result-shape constraints from the question."""

    normalized = " ".join(question.casefold().split())
    if conservative:
        # Existential bounds in a predicate are not output superlatives.
        normalized = re.sub(r"\bat\s+(?:least|most)\b", "bounded", normalized)
    output_scope = normalized
    if conservative:
        request = re.search(
            r"\b(?:how many|what|which|who|find|list|show|give|provide|return|"
            r"display|identify|calculate)\b", normalized
        )
        if request:
            # Relative clauses describe eligible entities, not the cardinality
            # of the outer answer. Keep the full question in the planner; only
            # the deterministic hard output constraint uses this narrow scope.
            qualifier = re.search(
                r"\b(?:who|whose|that|where|with|having)\b",
                normalized[request.end():],
            )
            end = request.end() + qualifier.start() if qualifier else len(normalized)
            output_scope = normalized[request.start():end]
    # A scalar aggregate can still be only one part of a multi-output request.
    # Keep column-count feedback conservative: false-negative feedback is safer
    # than telling the generator to delete a requested projection.  In
    # particular, questions such as "Provide the number ... . What is her
    # major?" must retain both the aggregate and the descriptive column.
    additional_request_clause = bool(
        re.search(
            r"[.!?;]\s*(?:what|which|who|how|provide|list|show|give|return|calculate|find)\b",
            normalized,
        )
    )
    coordinated_pronominal_output = bool(
        re.search(
            r"\b(?:and|plus|along with|as well as|together with)\s+"
            r"(?:what|which|who|(?:the\s+)?(?:his|her|their|its)\b)",
            normalized,
        )
    )
    coordinated_measure_output = bool(
        re.search(
            r"\b(?:count|number|total|sum|average|mean|minimum|maximum|min|max)\b"
            r"[^.!?;]*\b(?:and|plus|along with|as well as|together with)\s+"
            r"(?:the\s+)?(?:count|number|total|sum|average|mean|minimum|maximum|min|max)\b",
            normalized,
        )
    )
    explicit_list_projection = bool(
        re.search(r"\b(?:list|show|give|provide|return|display)\b", normalized)
        and (
            normalized.count(",") >= 1
            or re.search(
                r"\b(?:and|plus|along with|as well as|together with)\b",
                normalized,
            )
        )
    )
    multiple_output_cues = bool(
        additional_request_clause
        or coordinated_pronominal_output
        or coordinated_measure_output
        or explicit_list_projection
        or normalized.count("?") > 1
    )
    top_match = re.search(r"\b(?:top|first)\s+(\d+)\b", output_scope)
    if conservative and top_match:
        prefix = output_scope[:top_match.start()]
        relative = list(re.finditer(r"\b(?:who|whose|where|that)\b", prefix))
        output = list(re.finditer(r"\b(?:find|return|list|show|give|limit)\b", prefix))
        if relative and (not output or relative[-1].start() > output[-1].start()):
            top_match = None
    grouped = bool(
        re.search(r"\b(?:each|every|per)\b", normalized)
        or re.search(r"\bgroup(?:ed)?\s+by\b", normalized)
    )
    count = bool(
        re.search(r"\bhow many\b|\bnumber of\b", normalized)
        and not _NAMED_MEASURE_LOOKUP.search(normalized)
    )
    output_count = bool(
        re.search(r"\bhow many\b|\bnumber of\b", output_scope)
        and not _NAMED_MEASURE_LOOKUP.search(output_scope)
    )
    list_request = bool(
        re.search(r"\b(?:list|show|give|provide|return|display)\b", normalized)
    )
    scalar_measure = not list_request and bool(
        re.search(
            r"\b(?:what is|what was|calculate|find)\b.*\b(?:difference|gap|rate|ratio|total|average|sum)\b",
            output_scope,
        )
    )
    comparative_extremum = bool(
        re.search(
            r"\b(?:than|above|below)\s+"
            r"(?:(?:the|[a-z][a-z0-9_-]*'s)\s+)?"
            r"(?:highest|lowest|largest|smallest|oldest|youngest|most|least)\b",
            output_scope,
        )
    )
    singleton = bool(
        re.search(r"\bwhich one\b", output_scope)
        or re.search(
            r"\b(?:who|which|what)\b.*\b(?:highest|lowest|largest|smallest|oldest|youngest|most|least)\b",
            output_scope,
        )
    ) and not comparative_extremum
    if top_match:
        shape = "top_n_rows"
        expected_rows: int | None = int(top_match.group(1))
    elif (
        (output_count or scalar_measure)
        and not grouped
        and not explicit_list_projection
    ):
        shape = "single_scalar_row"
        expected_rows = 1
    elif singleton and not grouped:
        shape = "single_best_row"
        expected_rows = 1
    else:
        shape = "result_set"
        expected_rows = None
    if shape == "single_scalar_row" and not multiple_output_cues:
        expected_columns: int | None = 1
    elif (
        shape == "single_best_row"
        and not multiple_output_cues
        and "full name" not in normalized
        and " and " not in normalized
    ):
        expected_columns = 1
    else:
        expected_columns = None
    contract = {
        "result_shape": shape,
        "expected_rows": expected_rows,
        "expected_columns": expected_columns,
        "requires_grouping": grouped,
        "requires_count": count,
        "comparison": bool(re.search(r"\b(?:between|among|versus|vs\.?|compared)\b", normalized)),
        "full_name_requested": "full name" in normalized,
        "source": "deterministic_question_only_no_gold",
    }
    if conservative:
        contract["row_count_is_upper_bound"] = shape in {"top_n_rows", "single_best_row"}
    return contract


def assess_query_contract(
    contract: dict[str, Any], execution: dict[str, Any]
) -> dict[str, Any]:
    """Return bounded result-shape feedback; never inspect expected answers."""

    if not execution.get("executable"):
        return {
            "satisfied": False,
            "violations": ["candidate_sql_is_not_executable"],
        }
    rows = list(execution.get("rows") or [])
    columns = list(execution.get("columns") or [])
    shape = str(contract["result_shape"])
    expected_rows = contract.get("expected_rows")
    expected_columns = contract.get("expected_columns")
    violations: list[str] = []
    if shape == "top_n_rows" and isinstance(expected_rows, int):
        mismatch = len(rows) > expected_rows if contract.get("row_count_is_upper_bound") else len(rows) != expected_rows
        if not execution.get("truncated") and mismatch:
            violations.append(
                f"question_requests_top_{expected_rows}_but_candidate_returned_{len(rows)}_rows"
            )
    elif shape in {"single_scalar_row", "single_best_row"} and (
        len(rows) > 1 if contract.get("row_count_is_upper_bound") else len(rows) != 1
    ):
        violations.append(
            f"question_requests_one_row_but_candidate_returned_{len(rows)}_rows"
        )
    if isinstance(expected_columns, int) and len(columns) != expected_columns:
        violations.append(
            f"question_requests_{expected_columns}_output_columns_but_candidate_returned_{len(columns)}"
        )
    return {
        "satisfied": not violations,
        "violations": violations,
        "observed_rows": len(rows),
        "observed_columns": len(columns),
        "gold_or_expected_answer_used": False,
    }


@lru_cache(maxsize=32768)
def _execution_sql_fingerprint(sql: str, dialect: str) -> str | None:
    """Canonicalize execution semantics while ignoring outer output aliases.

    ReAct commonly executes ``expr AS readable_name`` and submits the same
    query without that presentation-only alias.  Exact string comparison made
    the execution certificate disappear in that case.  Only aliases attached
    directly to the outer SELECT list, identifier quoting/case, and formatting
    are erased here; expressions, sources, joins, predicates, grouping,
    ordering, limits, and every literal remain part of the fingerprint.
    """

    try:
        tree = sqlglot.parse_one(sql, read=dialect.casefold())
    except Exception:
        return None
    normalized = tree.copy()
    if isinstance(normalized, exp.Select):
        normalized.set(
            "expressions",
            [
                expression.this.copy()
                if isinstance(expression, exp.Alias)
                else expression.copy()
                for expression in normalized.expressions
            ],
        )
    for identifier in normalized.find_all(exp.Identifier):
        identifier.set("this", str(identifier.this).casefold())
        identifier.set("quoted", False)
    return normalized.sql(dialect=dialect.casefold()).casefold()


def _draft_historical_support(
    *,
    draft_sql: str,
    question: str,
    historical_programs: list[dict[str, Any]],
    dialect: str,
) -> dict[str, Any]:
    """Attach evaluator-free provenance support to one generated draft.

    Only target-isolated programs from the frozen support workload are
    inspected.  The inventory can be wider than the two templates rendered in
    the M3 prompt: exact AST concordance is a deterministic compiler input, not
    a prompt-ranking heuristic.  No database result, score, gold SQL, or
    expected answer enters this computation.
    """

    draft = str(draft_sql or "").strip()
    draft_ast = _execution_sql_fingerprint(draft, dialect)
    normalized_question = " ".join(str(question).casefold().split())
    candidates: list[dict[str, Any]] = []
    for program in historical_programs:
        if not isinstance(program, dict):
            continue
        historical_sql = str(program.get("sql_template") or "").strip()
        historical_question = str(
            program.get("question_pattern") or ""
        ).strip()
        if not historical_sql:
            continue
        historical_ast = _execution_sql_fingerprint(historical_sql, dialect)
        normalized_historical_question = " ".join(
            historical_question.casefold().split()
        )
        candidates.append(
            {
                "provenance_id": str(program.get("provenance_id") or ""),
                "exact_history_ast_match": bool(
                    draft_ast is not None
                    and historical_ast is not None
                    and draft_ast == historical_ast
                ),
                "question_text_similarity": round(
                    SequenceMatcher(
                        None,
                        normalized_question,
                        normalized_historical_question,
                    ).ratio(),
                    6,
                ),
                "target_disjoint": program.get("target_disjoint") is True,
                "matched_query_operators": list(
                    program.get("matched_query_operators") or []
                ),
                "uses_evaluator_gold": False,
            }
        )
    candidates.sort(
        key=lambda value: (
            bool(value["exact_history_ast_match"]),
            float(value["question_text_similarity"]),
            len(value["matched_query_operators"]),
            str(value["provenance_id"]),
        ),
        reverse=True,
    )
    best = candidates[0] if candidates else None
    return {
        "draft_sha256": sha256(draft.encode("utf-8")).hexdigest(),
        "best_target_isolated_history_support": best,
        "compared_programs": len(candidates),
        "selection_or_score_used": False,
        "uses_evaluator_gold": False,
    }


def _evidence_bound_program_prior(
    *,
    base_contract: dict[str, Any],
    base_support: dict[str, Any],
    auxiliary_contract: dict[str, Any] | None,
    auxiliary_support: dict[str, Any] | None,
) -> dict[str, Any] | None:
    """Compile cross-source history concordance into a program prior.

    A generated draft is admitted only when its executable AST independently
    agrees with a retrieved target-isolated history program whose question is
    substantially aligned with the current question.  This is query-time
    evidence compilation, never score- or answer-based switching.
    """

    candidates = [
        ("persistent_recovery", base_contract, base_support),
        (
            "direct_raw_evidence",
            auxiliary_contract,
            auxiliary_support,
        ),
    ]
    admitted: list[tuple[float, int, str, dict[str, Any], dict[str, Any]]] = []
    for source, contract, support in candidates:
        if contract is None or support is None:
            continue
        best = support.get("best_target_isolated_history_support")
        if not isinstance(best, dict):
            continue
        similarity = float(best.get("question_text_similarity") or 0.0)
        if (
            best.get("exact_history_ast_match") is True
            and best.get("target_disjoint") is True
            and similarity >= 0.5
        ):
            admitted.append(
                (
                    similarity,
                    1 if source == "persistent_recovery" else 0,
                    source,
                    contract,
                    best,
                )
            )
    if not admitted:
        return None
    similarity, _, source, contract, best = max(admitted)
    return {
        "compiler": "target_isolated_history_draft_concordance_v1",
        "source_lane": source,
        "program_contract": contract,
        "historical_provenance_id": best["provenance_id"],
        "question_text_similarity": similarity,
        "exact_history_ast_match": True,
        "required_preservation": [
            "cte_and_subquery_staging",
            "join_multiplicity",
            "having_and_group_eligibility",
            "window_and_set_operations",
        ],
        "admission_threshold": {
            "target_disjoint": True,
            "exact_history_ast_match": True,
            "minimum_question_text_similarity": 0.5,
        },
        "score_or_expected_answer_used": False,
        "uses_evaluator_gold": False,
    }


def _outer_distinct_only_execution_match(
    executed_sql: str, proposal_sql: str, dialect: str
) -> bool:
    """Return whether submission only adds a plain outer ``DISTINCT``.

    This is deliberately narrower than general semantic equivalence.  The M4
    exact-literal compiler independently checks that the DISTINCT is a bounded
    anchor-entity cardinality normalization after a certified relation
    expansion.  Here we only connect that final normalization to the otherwise
    identical SQL that ReACT actually executed.
    """

    try:
        executed = sqlglot.parse_one(executed_sql, read=dialect.casefold())
        proposal = sqlglot.parse_one(proposal_sql, read=dialect.casefold())
    except Exception:
        return False
    if not isinstance(executed, exp.Select) or not isinstance(proposal, exp.Select):
        return False
    distinct = proposal.args.get("distinct")
    if (
        executed.args.get("distinct") is not None
        or not isinstance(distinct, exp.Distinct)
        or distinct.args.get("on") is not None
    ):
        return False
    proposal_without_distinct = proposal.copy()
    proposal_without_distinct.set("distinct", None)
    return _execution_sql_fingerprint(
        executed.sql(dialect=dialect.casefold()), dialect
    ) == _execution_sql_fingerprint(
        proposal_without_distinct.sql(dialect=dialect.casefold()), dialect
    )


def _observation_has_duplicate_rows(observation: dict[str, Any]) -> bool:
    """Require observed duplicate evidence before certifying added DISTINCT."""

    rows = list(observation.get("rows") or [])
    if len(rows) < 2:
        return False
    rendered = [
        json.dumps(row, ensure_ascii=False, sort_keys=True, default=repr)
        for row in rows
    ]
    return len(set(rendered)) < len(rendered)


def _proposal_execution_certificate(
    trajectory: list[dict[str, Any]], proposal_sql: str, dialect: str
) -> dict[str, Any] | None:
    """Certify that the submitted proposal was semantically executed."""

    normalized_sql = proposal_sql.strip()
    if not normalized_sql:
        return None
    proposal_fingerprint = _execution_sql_fingerprint(normalized_sql, dialect)
    for step in reversed(trajectory):
        if step.get("tool") != "execute_sql" or step.get("status") != "ok":
            continue
        executed_sql = str(
            dict(step.get("arguments") or {}).get("sql") or ""
        ).strip()
        exact_text = executed_sql == normalized_sql
        executed_fingerprint = _execution_sql_fingerprint(executed_sql, dialect)
        outer_distinct_only = False
        if not exact_text and (
            proposal_fingerprint is None
            or executed_fingerprint is None
            or executed_fingerprint != proposal_fingerprint
        ):
            outer_distinct_only = _outer_distinct_only_execution_match(
                executed_sql, normalized_sql, dialect
            )
            if not outer_distinct_only:
                continue
        observation = dict(step.get("observation") or {})
        contract = dict(observation.get("query_contract_check") or {})
        if outer_distinct_only and not _observation_has_duplicate_rows(observation):
            continue
        if (
            observation.get("executable") is True
            and contract.get("satisfied") is True
            and contract.get("gold_or_expected_answer_used") is False
        ):
            return {
                "proposal_sql_sha256": sha256(normalized_sql.encode()).hexdigest(),
                "executable": True,
                "query_contract_satisfied": True,
                "observed_rows": contract.get("observed_rows"),
                "observed_columns": contract.get("observed_columns"),
                "executed_sql_sha256": sha256(executed_sql.encode()).hexdigest(),
                "execution_equivalence": (
                    "exact_sql_text"
                    if exact_text
                    else (
                        "outer_distinct_cardinality_normalization_after_observed_duplicates"
                        if outer_distinct_only
                        else "outer_projection_alias_insensitive_ast"
                    )
                ),
                "duplicate_rows_observed": outer_distinct_only,
                "gold_or_expected_answer_used": False,
            }
    return None


def _append_fixed_consumer_submission_validation(
    *,
    trajectory: list[dict[str, Any]],
    proposal_sql: str,
    dialect: str,
    query_contract: dict[str, Any],
    db_tools: Any,
    budget: ToolBudget,
) -> bool:
    """Execute an unverified final submission once without changing its SQL.

    This is the fixed consumer's basic execution validation, not a candidate
    selector or a scoring gate.  It is only used by the unified main, only when
    the exact submitted text has no prior execution certificate, and it consumes
    the same declared action/SQL-execution budget as an agent-issued execute_sql.
    """

    normalized = str(proposal_sql or "").strip()
    if not normalized or _proposal_execution_certificate(
        trajectory, normalized, dialect
    ) is not None:
        return False
    if (
        budget.actions >= budget.max_actions
        or budget.sql_executions >= budget.max_sql_executions
    ):
        return False
    arguments = {"sql": normalized}
    try:
        budget.charge("execute_sql")
        observation = db_tools.execute_sql(normalized)
        observation["query_contract_check"] = assess_query_contract(
            query_contract, observation
        )
        status = "ok"
    except Exception as error:
        observation = {
            "error_type": type(error).__name__,
            "error": str(error)[:800],
        }
        status = "error"
    trajectory.append(
        {
            "turn": "fixed_consumer",
            "tool": "execute_sql",
            "arguments": arguments,
            "status": status,
            "observation": observation,
            "automatic_fixed_consumer_validation": True,
            "candidate_selection_performed": False,
            "score_or_expected_answer_consulted": False,
        }
    )
    return True


def _repair_mysql_rollup_clause_order(sql: str, dialect: str) -> str:
    """Move a trailing MySQL WITH ROLLUP before the final ORDER BY clause."""

    if dialect.casefold() != "mysql":
        return sql
    trailing = re.search(r"(?is)\s+WITH\s+ROLLUP\s*(;?)\s*$", sql)
    if trailing is None:
        return sql
    body = sql[: trailing.start()].rstrip()
    order_matches = list(re.finditer(r"(?is)\bORDER\s+BY\b", body))
    group_matches = list(re.finditer(r"(?is)\bGROUP\s+BY\b", body))
    if not order_matches or not group_matches:
        return sql
    order_start = order_matches[-1].start()
    if group_matches[-1].start() > order_start:
        return sql
    semicolon = trailing.group(1)
    return (
        body[:order_start].rstrip()
        + " WITH ROLLUP\n"
        + body[order_start:].lstrip()
        + semicolon
    )


def _preserve_dual_draft_outer_consensus(
    candidate_sql: str,
    recovered_sql: str | None,
    raw_sql: str | None,
    dialect: str,
    question: str = "",
) -> tuple[str, list[str]]:
    """Keep outer AST components on which both independent drafts agree.

    Graph/Evo may still change joins, predicates, literals, or staging when its
    evidence supports doing so. It may not silently drop a shared projection
    or invent/remove a shared top-level LIMIT/DISTINCT contract. This rule is
    schema- and dataset-independent and never consults execution scores.
    """

    if not candidate_sql.strip() or not recovered_sql or not raw_sql:
        return candidate_sql, []
    try:
        candidate = sqlglot.parse_one(candidate_sql, read=dialect.casefold())
        recovered = sqlglot.parse_one(recovered_sql, read=dialect.casefold())
        raw = sqlglot.parse_one(raw_sql, read=dialect.casefold())
    except Exception:
        return candidate_sql, []
    if not all(isinstance(tree, exp.Select) for tree in (candidate, recovered, raw)):
        return candidate_sql, []

    def signature(node: exp.Expression | None) -> str | None:
        return (
            node.sql(dialect=dialect.casefold()).casefold()
            if node is not None
            else None
        )

    changes: list[str] = []
    recovered_projection = [signature(node) for node in recovered.expressions]
    raw_projection = [signature(node) for node in raw.expressions]
    candidate_projection = [signature(node) for node in candidate.expressions]
    available_qualifiers = {
        str(table.alias_or_name).casefold()
        for table in candidate.find_all(exp.Table)
        if table.alias_or_name
    }
    projection_qualifiers = {
        str(column.table).casefold()
        for projection in recovered.expressions
        for column in projection.find_all(exp.Column)
        if column.table
    }
    if (
        recovered_projection == raw_projection
        and candidate_projection != recovered_projection
        and projection_qualifiers <= available_qualifiers
    ):
        candidate.set(
            "expressions", [projection.copy() for projection in recovered.expressions]
        )
        changes.append("outer_projection")
    elif len(raw.expressions) > len(recovered.expressions):
        recovered_columns = {
            str(column.name).casefold()
            for projection in recovered.expressions
            for column in projection.find_all(exp.Column)
        }
        raw_columns = {
            str(column.name).casefold()
            for projection in raw.expressions
            for column in projection.find_all(exp.Column)
        }

        def outer_alias_maps(
            tree: exp.Select,
        ) -> tuple[dict[str, str], dict[str, list[str]]]:
            alias_to_table: dict[str, str] = {}
            table_to_aliases: dict[str, list[str]] = {}
            for table in tree.find_all(exp.Table):
                parent = table.parent
                while parent is not None and not isinstance(parent, exp.Select):
                    parent = parent.parent
                if parent is not tree:
                    continue
                alias = str(table.alias_or_name)
                physical = str(table.name).casefold()
                alias_to_table[alias.casefold()] = physical
                table_to_aliases.setdefault(physical, []).append(alias)
            return alias_to_table, table_to_aliases

        raw_alias_to_table, _ = outer_alias_maps(raw)
        _, candidate_table_to_aliases = outer_alias_maps(candidate)
        raw_projection_copy = [projection.copy() for projection in raw.expressions]
        safe_superset = bool(
            recovered_columns
            and recovered_columns <= raw_columns
            and len(raw_columns) > len(recovered_columns)
        )

        def rebind_column(node: exp.Expression) -> exp.Expression:
            nonlocal safe_superset
            if not isinstance(node, exp.Column):
                return node
            qualifier = str(node.table or "").casefold()
            physical = raw_alias_to_table.get(qualifier)
            aliases = candidate_table_to_aliases.get(str(physical), [])
            if not qualifier or physical is None or len(aliases) != 1:
                safe_superset = False
                return node
            rebound = node.copy()
            rebound.set("table", exp.to_identifier(aliases[0]))
            return rebound

        rebound_projection = [
            projection.transform(rebind_column)
            for projection in raw_projection_copy
        ]
        rebound_signature = [signature(node) for node in rebound_projection]
        if safe_superset and candidate_projection != rebound_signature:
            candidate.set("expressions", rebound_projection)
            changes.append("outer_projection_raw_superset")

    normalized_question = " ".join(str(question).casefold().split())
    named_measure_lookup = bool(_NAMED_MEASURE_LOOKUP.search(normalized_question))
    candidate_has_count = any(
        isinstance(node, exp.Count)
        for projection in candidate.expressions
        for node in projection.walk()
    )
    recovered_has_aggregate = any(
        isinstance(node, exp.AggFunc)
        for projection in recovered.expressions
        for node in projection.walk()
    )
    if named_measure_lookup and candidate_has_count and not recovered_has_aggregate:
        recovered_qualifiers = {
            str(column.table).casefold()
            for projection in recovered.expressions
            for column in projection.find_all(exp.Column)
            if column.table
        }
        if recovered_qualifiers <= available_qualifiers:
            candidate.set(
                "expressions", [projection.copy() for projection in recovered.expressions]
            )
            changes.append("outer_projection_named_measure")

    explicit_clock_component = bool(
        re.search(
            r"\b(?:time of day|clock time|hours?|minutes?|seconds?|"
            r"a\.?m\.?|p\.?m\.?)\b",
            normalized_question,
        )
    )
    if "time" in normalized_question and not explicit_clock_component:
        temporal_unwrap = False
        temporal_column_names: set[str] = set()
        temporal_compatible = len(recovered.expressions) == len(raw.expressions)
        if temporal_compatible:
            for recovered_expression, raw_expression in zip(
                recovered.expressions, raw.expressions
            ):
                recovered_value = (
                    recovered_expression.this
                    if isinstance(recovered_expression, exp.Alias)
                    else recovered_expression
                )
                raw_value = (
                    raw_expression.this
                    if isinstance(raw_expression, exp.Alias)
                    else raw_expression
                )
                match = re.fullmatch(
                    r"time\(([^()]+)\)",
                    recovered_value.sql(dialect=dialect.casefold()).casefold(),
                )
                raw_value_sql = raw_value.sql(dialect=dialect.casefold()).casefold()
                if match is not None and match.group(1) == raw_value_sql:
                    temporal_unwrap = True
                    temporal_column_names.update(
                        str(column.name).casefold()
                        for column in raw_value.find_all(exp.Column)
                    )
                elif signature(recovered_value) != signature(raw_value):
                    temporal_compatible = False
                    break
        raw_qualifiers = {
            str(column.table).casefold()
            for projection in raw.expressions
            for column in projection.find_all(exp.Column)
            if column.table
        }
        if (
            temporal_compatible
            and temporal_unwrap
            and raw_qualifiers <= available_qualifiers
        ):
            candidate.set(
                "expressions", [projection.copy() for projection in raw.expressions]
            )

            def unwrap_time(node: exp.Expression) -> exp.Expression:
                if (
                    isinstance(node, exp.Anonymous)
                    and str(node.name).casefold() == "time"
                    and len(node.expressions) == 1
                    and isinstance(node.expressions[0], exp.Column)
                    and str(node.expressions[0].name).casefold()
                    in temporal_column_names
                ):
                    return node.expressions[0].copy()
                return node

            candidate = candidate.transform(unwrap_time)
            changes.append("outer_projection_raw_temporal")

    explicit_percentage_formula = bool(
        "benchmark knowledge evidence:" in normalized_question
        and "percentage difference" in normalized_question
        and "subtract" in normalized_question
        and normalized_question.count("divide") >= 2
    )
    if explicit_percentage_formula and signature(candidate) != signature(recovered):
        candidate = recovered.copy()
        changes.append("explicit_formula_program")

    recovered_column_names = [
        str(column.name)
        for column in recovered.find_all(exp.Column)
        if column.name
    ]
    recovered_is_opaque = bool(
        recovered_column_names
        and sum(
            bool(_OPAQUE_PHYSICAL_IDENTIFIER.fullmatch(name))
            for name in recovered_column_names
        )
        / len(recovered_column_names)
        >= 0.5
    )
    if recovered_is_opaque:
        recovered_literals: dict[str, set[str]] = {}
        for literal in recovered.find_all(exp.Literal):
            if literal.is_string:
                recovered_literals.setdefault(
                    str(literal.this).casefold(), set()
                ).add(str(literal.this))
        case_replacements = 0

        def preserve_literal_case(node: exp.Expression) -> exp.Expression:
            nonlocal case_replacements
            if not isinstance(node, exp.Literal) or not node.is_string:
                return node
            choices = recovered_literals.get(str(node.this).casefold(), set())
            if len(choices) != 1:
                return node
            recovered_value = next(iter(choices))
            if recovered_value == str(node.this):
                return node
            case_replacements += 1
            return exp.Literal.string(recovered_value)

        candidate = candidate.transform(preserve_literal_case)
        if case_replacements:
            changes.append("recovery_literal_case")

    def conjunction_terms(node: exp.Expression | None) -> list[exp.Expression]:
        if isinstance(node, exp.And):
            return [
                *conjunction_terms(node.this),
                *conjunction_terms(node.expression),
            ]
        return [node] if node is not None else []

    def not_null_target(node: exp.Expression) -> exp.Expression | None:
        if not isinstance(node, exp.Not) or not isinstance(node.this, exp.Is):
            return None
        predicate = node.this
        if not isinstance(predicate.expression, exp.Null):
            return None
        return predicate.this

    recovered_order = recovered.args.get("order")
    candidate_order = candidate.args.get("order")
    if (
        isinstance(recovered_order, exp.Order)
        and signature(candidate_order) == signature(recovered_order)
    ):
        ordered_expressions = {
            signature(ordered.this)
            for ordered in recovered_order.expressions
            if isinstance(ordered, exp.Ordered)
        }
        recovered_where = recovered.args.get("where")
        candidate_where = candidate.args.get("where")
        candidate_terms = {
            signature(term)
            for term in conjunction_terms(
                candidate_where.this
                if isinstance(candidate_where, exp.Where)
                else None
            )
        }
        preserved_guards: list[exp.Expression] = []
        for term in conjunction_terms(
            recovered_where.this
            if isinstance(recovered_where, exp.Where)
            else None
        ):
            target = not_null_target(term)
            target_qualifiers = {
                str(column.table).casefold()
                for column in (target.find_all(exp.Column) if target else [])
                if column.table
            }
            if (
                target is not None
                and signature(target) in ordered_expressions
                and signature(term) not in candidate_terms
                and target_qualifiers <= available_qualifiers
            ):
                preserved_guards.append(term.copy())
        if preserved_guards:
            predicate = (
                candidate_where.this.copy()
                if isinstance(candidate_where, exp.Where)
                else None
            )
            for guard in preserved_guards:
                predicate = guard if predicate is None else exp.and_(predicate, guard)
            candidate.set("where", exp.Where(this=predicate))
            changes.append("recovery_order_null_guard")

    date_comparison_replacements = 0
    if dialect.casefold() == "sqlite":
        date_literal = re.compile(r"^\d{4}-\d{2}-\d{2}$")

        def normalize_date_comparison(node: exp.Expression) -> exp.Expression:
            nonlocal date_comparison_replacements
            if not isinstance(node, (exp.GT, exp.GTE, exp.LT, exp.LTE)):
                return node
            left = node.this
            right = node.expression
            left_is_date = bool(
                isinstance(left, exp.Literal)
                and left.is_string
                and date_literal.fullmatch(str(left.this))
            )
            right_is_date = bool(
                isinstance(right, exp.Literal)
                and right.is_string
                and date_literal.fullmatch(str(right.this))
            )
            updated = node.copy()
            if isinstance(left, exp.Column) and right_is_date:
                updated.set(
                    "this",
                    exp.Anonymous(this="DATE", expressions=[left.copy()]),
                )
            elif isinstance(right, exp.Column) and left_is_date:
                updated.set(
                    "expression",
                    exp.Anonymous(this="DATE", expressions=[right.copy()]),
                )
            else:
                return node
            date_comparison_replacements += 1
            return updated

        candidate = candidate.transform(normalize_date_comparison)
        if date_comparison_replacements:
            changes.append("date_only_comparison")

    for component in ("limit", "distinct"):
        recovered_component = recovered.args.get(component)
        raw_component = raw.args.get(component)
        candidate_component = candidate.args.get(component)
        if (
            signature(recovered_component) == signature(raw_component)
            and signature(candidate_component) != signature(recovered_component)
        ):
            candidate.set(
                component,
                recovered_component.copy()
                if recovered_component is not None
                else None,
            )
            changes.append(f"outer_{component}")

    if not changes:
        return candidate_sql, []
    return candidate.sql(dialect=dialect.casefold()), changes


def _preserve_raw_backbone_without_structural_support(
    candidate_sql: str,
    base_sql: str | None,
    *,
    question: str,
    graph_payload: dict[str, Any],
    evidence_payload: dict[str, Any],
    dialect: str,
) -> tuple[str, list[str]]:
    """Keep a complete Raw AST when recovery adds no support for its rewrite.

    Raw-backbone mode may still add operators, relations, and evidence-supported
    filters. It may not weaken an existing window/HAVING stage, replace a
    history-supported join, or move an aggregate to an unsupported same-name
    measure. Those unsupported edits retain the executable base program.
    """

    if not candidate_sql.strip() or not base_sql or not base_sql.strip():
        return candidate_sql, []
    try:
        candidate = sqlglot.parse_one(candidate_sql, read=dialect.casefold())
        base = sqlglot.parse_one(base_sql, read=dialect.casefold())
    except Exception:
        return candidate_sql, []
    if candidate.sql(dialect=dialect.casefold()).casefold() == base.sql(
        dialect=dialect.casefold()
    ).casefold():
        return candidate_sql, []

    del question

    def window_contracts(tree: exp.Expression) -> list[tuple[Any, ...]]:
        contracts: list[tuple[Any, ...]] = []
        for window in tree.find_all(exp.Window):
            function = window.this
            spec = window.args.get("spec")
            spec_args = dict(spec.args) if isinstance(spec, exp.WindowSpec) else {}
            contracts.append(
                (
                    str(getattr(function, "key", type(function).__name__)),
                    len(window.args.get("partition_by") or []),
                    len((window.args.get("order") or exp.Order()).expressions),
                    str(spec_args.get("kind") or "").casefold(),
                    str(spec_args.get("start_side") or "").casefold(),
                    str(spec_args.get("start") or "").casefold(),
                    str(spec_args.get("end_side") or "").casefold(),
                    str(spec_args.get("end") or "").casefold(),
                )
            )
        return contracts

    base_windows = window_contracts(base)
    candidate_windows = window_contracts(candidate)
    for base_window in base_windows:
        compatible = [
            candidate_window
            for candidate_window in candidate_windows
            if candidate_window[0] == base_window[0]
            and candidate_window[1] >= base_window[1]
            and candidate_window[2] >= base_window[2]
            and (
                not any(base_window[3:])
                or candidate_window[3:] == base_window[3:]
            )
        ]
        if not compatible:
            return str(base_sql), ["raw_backbone_window_contract_preserved"]

    if len(list(candidate.find_all(exp.Having))) < len(
        list(base.find_all(exp.Having))
    ):
        return str(base_sql), ["raw_backbone_having_contract_preserved"]

    def window_depends_on_having_cte(tree: exp.Expression) -> bool:
        having_ctes = {
            str(cte.alias_or_name).casefold()
            for cte in tree.find_all(exp.CTE)
            if any(True for _ in cte.find_all(exp.Having))
        }
        if not having_ctes:
            return False

        def nearest_select(node: exp.Expression) -> exp.Select | None:
            parent = node.parent
            while parent is not None and not isinstance(parent, exp.Select):
                parent = parent.parent
            return parent if isinstance(parent, exp.Select) else None

        window_selects = {
            selected
            for window in tree.find_all(exp.Window)
            if (selected := nearest_select(window)) is not None
        }
        return any(
            str(table.name).casefold() in having_ctes
            and nearest_select(table) is selected
            for selected in window_selects
            for table in selected.find_all(exp.Table)
        )

    if window_depends_on_having_cte(candidate) and not window_depends_on_having_cte(
        base
    ):
        return str(base_sql), ["raw_backbone_window_stage_preserved"]

    aggregate_identifier_ranks: dict[str, int] = {}
    for role, candidates in (
        graph_payload.get("query_role_bindings") or {}
    ).items():
        if "aggregation role:" not in str(role).casefold():
            continue
        for rank, candidate_binding in enumerate(candidates):
            identifier = str(
                candidate_binding.get("physical_identifier") or ""
            ).casefold()
            if identifier:
                aggregate_identifier_ranks[identifier] = min(
                    rank,
                    aggregate_identifier_ranks.get(identifier, rank),
                )

    def aggregate_sources(
        tree: exp.Expression,
    ) -> list[tuple[str, tuple[tuple[str, str], ...]]]:
        cte_names = {
            str(cte.alias_or_name).casefold() for cte in tree.find_all(exp.CTE)
        }
        aliases: dict[str, str | None] = {}
        for table in tree.find_all(exp.Table):
            physical = str(table.name).casefold()
            if physical in cte_names:
                continue
            alias = str(table.alias_or_name).casefold()
            previous = aliases.get(alias)
            aliases[alias] = physical if previous in {None, physical} else None
        output: list[tuple[str, tuple[tuple[str, str], ...]]] = []
        for aggregate in tree.find_all(exp.AggFunc):
            sources: list[tuple[str, str]] = []
            for column in aggregate.find_all(exp.Column):
                qualifier = str(column.table or "").casefold()
                physical = aliases.get(qualifier)
                if physical:
                    sources.append((physical, str(column.name).casefold()))
            output.append(
                (
                    str(getattr(aggregate, "key", type(aggregate).__name__)),
                    tuple(sources),
                )
            )
        return output

    base_aggregates = aggregate_sources(base)
    candidate_aggregates = aggregate_sources(candidate)
    if len(base_aggregates) == len(candidate_aggregates):
        for base_aggregate, candidate_aggregate in zip(
            base_aggregates,
            candidate_aggregates,
            strict=True,
        ):
            if base_aggregate[0] != candidate_aggregate[0]:
                continue
            base_sources = set(base_aggregate[1])
            candidate_sources = set(candidate_aggregate[1])
            changed_same_name_sources = {
                source
                for source in candidate_sources - base_sources
                if any(source[1] == base_source[1] for base_source in base_sources)
            }
            for candidate_table, column in changed_same_name_sources:
                candidate_identifier = f"{candidate_table}.{column}"
                candidate_rank = aggregate_identifier_ranks.get(
                    candidate_identifier
                )
                base_ranks = [
                    aggregate_identifier_ranks[f"{base_table}.{base_column}"]
                    for base_table, base_column in base_sources
                    if base_column == column
                    and f"{base_table}.{base_column}"
                    in aggregate_identifier_ranks
                ]
                if candidate_rank is None or (
                    base_ranks and min(base_ranks) <= candidate_rank
                ):
                    return str(base_sql), [
                        "raw_backbone_aggregate_source_preserved"
                    ]

    def physical_join_edges(tree: exp.Expression) -> set[tuple[str, str]]:
        cte_names = {
            str(cte.alias_or_name).casefold() for cte in tree.find_all(exp.CTE)
        }
        aliases: dict[str, str | None] = {}
        for table in tree.find_all(exp.Table):
            physical = str(table.name).casefold()
            if physical in cte_names:
                continue
            alias = str(table.alias_or_name).casefold()
            previous = aliases.get(alias)
            aliases[alias] = physical if previous in {None, physical} else None
        edges: set[tuple[str, str]] = set()
        for join in tree.find_all(exp.Join):
            on_expression = join.args.get("on")
            columns = list(on_expression.find_all(exp.Column)) if on_expression else []
            if len(columns) != 2:
                continue
            endpoints: list[str] = []
            for column in columns:
                physical = aliases.get(str(column.table or "").casefold())
                if physical is None:
                    break
                endpoints.append(
                    f"{physical}.{str(column.name).casefold()}"
                )
            if len(endpoints) == 2:
                edges.add(tuple(sorted(endpoints)))
        return edges

    certified_edges: set[tuple[str, str]] = set()
    for edge in (
        graph_payload.get("physical_join_edges")
        or graph_payload.get("ordered_join_edges")
        or []
    ):
        left = str(edge.get("left") or "").casefold()
        right = str(edge.get("right") or "").casefold()
        if left and right:
            certified_edges.add(tuple(sorted((left, right))))
    unsupported_edges = (
        physical_join_edges(candidate)
        - physical_join_edges(base)
        - certified_edges
    )
    if unsupported_edges:
        return str(base_sql), ["raw_backbone_join_contract_preserved"]

    historical_edges: set[tuple[str, str]] = set()
    context = dict(
        evidence_payload.get("graph_evo_program_context") or {}
    )
    for program in context.get("historical_programs") or []:
        template = str(program.get("sql_template") or "").strip()
        if not template:
            continue
        try:
            historical_tree = sqlglot.parse_one(
                template,
                read=dialect.casefold(),
            )
        except Exception:
            continue
        historical_edges.update(physical_join_edges(historical_tree))
    if (
        physical_join_edges(base)
        - physical_join_edges(candidate)
    ) & historical_edges:
        return str(base_sql), ["raw_backbone_history_join_preserved"]

    return candidate_sql, []


def _unique_unknown_column_repair(
    *, sql: str, execution_observation: dict[str, Any], db_tools: Any, dialect: str
) -> dict[str, Any] | None:
    """Repair one uniquely resolvable qualified-column execution error.

    This is a narrow fixed-consumer transport/schema correction.  It uses the
    current physical catalog and the database's concrete error only; it does
    not inspect results, scores, a baseline, or expected SQL.  Ambiguous column
    ownership fails closed and is left to the bounded model correction.
    """

    if execution_observation.get("executable") is not False:
        return None
    error = str(execution_observation.get("error") or "")
    match = re.search(
        r"unknown\s+column\s+['\"`]?(?P<alias>[A-Za-z_][\w$]*)\."
        r"(?P<column>[A-Za-z_][\w$]*)['\"`]?",
        error,
        flags=re.I,
    )
    if match is None:
        return None
    try:
        tree = sqlglot.parse_one(sql, read=dialect.casefold())
    except Exception:
        return None
    alias_to_table: dict[str, str] = {}
    alias_spelling: dict[str, str] = {}
    for table in tree.find_all(exp.Table):
        physical = str(table.name)
        alias = str(table.alias_or_name)
        alias_to_table[alias.casefold()] = physical
        alias_spelling[alias.casefold()] = alias
    bad_alias = match.group("alias").casefold()
    column_name = match.group("column")
    if bad_alias not in alias_to_table:
        return None
    alternatives: list[str] = []
    catalog = dict(getattr(db_tools, "columns", {}) or {})
    for alias, table in alias_to_table.items():
        if alias == bad_alias:
            continue
        physical_table = next(
            (value for value in catalog if str(value).casefold() == table.casefold()),
            None,
        )
        if physical_table is None:
            continue
        if any(
            str(value[0] if isinstance(value, (tuple, list)) else value).casefold()
            == column_name.casefold()
            for value in catalog[physical_table]
        ):
            alternatives.append(alias)
    alternatives = list(dict.fromkeys(alternatives))
    if len(alternatives) != 1:
        return None
    replacement_alias = alternatives[0]
    replacements = 0
    for column in tree.find_all(exp.Column):
        if (
            str(column.table).casefold() == bad_alias
            and str(column.name).casefold() == column_name.casefold()
        ):
            column.set(
                "table",
                exp.to_identifier(alias_spelling[replacement_alias]),
            )
            replacements += 1
    if replacements == 0:
        return None
    repaired = tree.sql(dialect=dialect.casefold())
    if repaired.strip() == str(sql).strip():
        return None
    return {
        "candidate_sql": repaired,
        "correction_reason": "unique_current_catalog_owner_for_unknown_column",
        "unknown_identifier": f"{match.group('alias')}.{column_name}",
        "replacement_identifier": (
            f"{alias_spelling[replacement_alias]}.{column_name}"
        ),
        "catalog_candidate_count": 1,
        "score_or_expected_answer_used": False,
        "uses_evaluator_gold": False,
    }


def _relevant_current_schema_for_sql(
    sql: str, *, db_tools: Any, dialect: str, table_limit: int = 12
) -> dict[str, list[str]]:
    """Return bounded physical columns for tables already used by a candidate."""

    try:
        tree = sqlglot.parse_one(sql, read=dialect.casefold())
    except Exception:
        return {}
    catalog = dict(getattr(db_tools, "columns", {}) or {})
    lookup = {str(table).casefold(): str(table) for table in catalog}
    output: dict[str, list[str]] = {}
    for node in tree.find_all(exp.Table):
        table = lookup.get(str(node.name).casefold())
        if table is None or table in output:
            continue
        output[table] = [
            str(value[0] if isinstance(value, (tuple, list)) else value)
            for value in catalog[table]
        ][:160]
        if len(output) >= table_limit:
            break
    return output


def _tool_arguments(call: dict[str, Any]) -> dict[str, Any]:
    raw = call.get("function", {}).get("arguments", "{}")
    value = raw if isinstance(raw, dict) else repair_json_loads(str(raw))
    if not isinstance(value, dict):
        raise ValueError("tool arguments must decode to an object")
    return value


def _usage(response: dict[str, Any]) -> dict[str, Any]:
    usage = response.get("usage") or {}
    return {
        "model": response.get("model"),
        "system_fingerprint": response.get("system_fingerprint"),
        "prompt_tokens": usage.get("prompt_tokens"),
        "completion_tokens": usage.get("completion_tokens"),
        "total_tokens": usage.get("total_tokens"),
    }


def build_recovery_documents(
    table_inputs: list[dict[str, Any]], recovery_rows: list[dict[str, Any]]
) -> list[CatalogDocument]:
    """Create separate semantic nodes instead of appending prose to raw documents."""

    inputs = {str(row["input_id"]): row for row in table_inputs}
    recovery = {str(row["input_id"]): row for row in recovery_rows}
    if len(inputs) != len(table_inputs) or len(recovery) != len(recovery_rows):
        raise ValueError("duplicate recovery input IDs")
    output: list[CatalogDocument] = []
    for input_id, source in inputs.items():
        prediction = dict((recovery.get(input_id) or {}).get("prediction") or {})
        database_id = str(source["schema_context"])
        table = str(source["physical_table"])
        aliases = [str(value) for value in prediction.get("table_aliases") or []]
        purpose = str(prediction.get("purpose") or "").strip()
        output.append(
            CatalogDocument(
                candidate_id=f"recovery_table::{database_id}::{table}",
                database_id=database_id,
                kind="recovery_table",
                table=table,
                name=table,
                text=(
                    f"physical table: {_quote(table)}\n"
                    f"recovered aliases: {json.dumps(aliases, ensure_ascii=False)}\n"
                    f"recovered purpose: {purpose}"
                ),
            )
        )
        columns = {
            str(row["physical_column"]): row
            for row in prediction.get("columns") or []
            if isinstance(row, dict) and row.get("physical_column")
        }
        for column_source in source.get("columns") or []:
            physical = str(column_source["physical_column"])
            row = dict(columns.get(physical) or {})
            facts = {
                "physical_identifier": f"{table}.{physical}",
                "aliases": [str(value) for value in row.get("aliases") or []],
                "query_phrases": [
                    str(value) for value in row.get("query_phrases") or []
                ],
                "retrieval_gloss": str(row.get("retrieval_gloss") or ""),
                "semantic_type": str(row.get("semantic_type") or "unknown"),
                "observed_values": [
                    _safe_value(value) for value in row.get("observed_values") or []
                ],
            }
            output.append(
                CatalogDocument(
                    candidate_id=(
                        f"recovery_column::{database_id}::{table}::{physical}"
                    ),
                    database_id=database_id,
                    kind="recovery_column",
                    table=table,
                    name=f"{table}.{physical}",
                    text=json.dumps(facts, ensure_ascii=False, sort_keys=True),
                )
            )
    if len({row.candidate_id for row in output}) != len(output):
        raise ValueError("duplicate fielded recovery document IDs")
    return output


def build_grounded_profile_documents(
    table_inputs: list[dict[str, Any]],
) -> list[CatalogDocument]:
    """Compile only deterministic physical/value/relationship evidence."""

    output: list[CatalogDocument] = []
    for source in table_inputs:
        database_id = str(source["schema_context"])
        table = str(source["physical_table"])
        relationships = source.get("relationships") or []
        output.append(
            CatalogDocument(
                candidate_id=f"profile_table::{database_id}::{table}",
                database_id=database_id,
                kind="profile_table",
                table=table,
                name=table,
                text=json.dumps(
                    {
                        "physical_table": table,
                        "relationships": relationships,
                    },
                    ensure_ascii=False,
                    sort_keys=True,
                ),
            )
        )
        for column in source.get("columns") or []:
            physical = str(column["physical_column"])
            # Current recovery inputs materialize deterministic database facts at
            # the column root.  Keep compatibility with the older nested format,
            # but never silently discard the root-level values: doing so reduces
            # the grounded condition to another rendering of the raw schema.
            profile = dict(column.get("value_profile") or {})
            schema = dict(column.get("raw_schema") or {})
            declared_type = column.get("declared_type", schema.get("declared_type"))
            primary_key = column.get("primary_key", schema.get("primary_key", False))
            observed_values = column.get(
                "observed_values", profile.get("observed_values", [])
            )
            output.append(
                CatalogDocument(
                    candidate_id=(
                        f"profile_column::{database_id}::{table}::{physical}"
                    ),
                    database_id=database_id,
                    kind="profile_column",
                    table=table,
                    name=f"{table}.{physical}",
                    text=json.dumps(
                        {
                            "physical_identifier": f"{table}.{physical}",
                            "declared_type": declared_type,
                            "primary_key": bool(primary_key),
                            "observed_values": [
                                _safe_value(value)
                                for value in observed_values or []
                            ],
                            "relationships": column.get("relationships") or [],
                        },
                        ensure_ascii=False,
                        sort_keys=True,
                    ),
                )
            )
    if len({row.candidate_id for row in output}) != len(output):
        raise ValueError("duplicate grounded profile document IDs")
    return output


def _shortest_path(
    adjacency: dict[str, set[str]], sources: set[str], target: str
) -> list[str]:
    queue: deque[tuple[str, list[str]]] = deque(
        (source, [source]) for source in sorted(sources)
    )
    visited = set(sources)
    while queue:
        node, path = queue.popleft()
        for neighbor in sorted(adjacency.get(node, set())):
            if neighbor in visited:
                continue
            if neighbor == target:
                return [*path, neighbor]
            visited.add(neighbor)
            queue.append((neighbor, [*path, neighbor]))
    return []


def coherent_table_closure(
    ranked: list[CatalogDocument], raw_documents: list[CatalogDocument]
) -> tuple[list[CatalogDocument], list[str]]:
    """Greedily connect ranked table seeds to the nearest connected component."""

    raw_tables = {
        str(row.table): row
        for row in raw_documents
        if row.kind == "table" and row.table
    }
    seeds: list[str] = []
    for row in ranked:
        if row.table and row.table in raw_tables and row.table not in seeds:
            seeds.append(row.table)
    if not seeds:
        return ranked, []
    adjacency: dict[str, set[str]] = {table: set() for table in raw_tables}
    for table, row in raw_tables.items():
        for reference in row.references:
            if reference in raw_tables:
                adjacency[table].add(reference)
                adjacency[reference].add(table)
    connected = {seeds[0]}
    remaining = seeds[1:]
    bridges: list[str] = []
    while remaining:
        choices: list[tuple[int, int, list[str], str]] = []
        for seed_rank, target in enumerate(remaining):
            path = _shortest_path(adjacency, connected, target)
            if path:
                choices.append((len(path), seed_rank, path, target))
        if not choices:
            connected.add(remaining.pop(0))
            continue
        _, _, path, target = min(choices)
        for table in path:
            if table not in connected:
                connected.add(table)
                if table not in seeds and table not in bridges:
                    bridges.append(table)
        remaining.remove(target)
    output = list(ranked)
    observed = {row.candidate_id for row in output}
    for table in [*seeds, *bridges]:
        row = raw_tables[table]
        if row.candidate_id not in observed:
            output.append(row)
            observed.add(row.candidate_id)
    return output, bridges


def relational_program_features(text: str) -> set[str]:
    """Extract a deterministic relational-operator signature from language.

    Historical-program retrieval used to recognize only common aggregates and
    rankings.  That made a topically similar COUNT/GROUP BY program look
    compatible with questions whose defining structure was actually HAVING,
    a window frame, an anti-join, a ratio, or recursion.  These features are
    deliberately lexical and evaluator-free; they describe the requested
    program shape, not whether any generated SQL is correct.
    """

    normalized = " ".join(str(text).casefold().split())
    output: set[str] = set()
    patterns = {
        "count": r"\bhow many\b|\bnumber of\b",
        "sum": r"\b(?:sum|total)\b",
        "average": r"\b(?:average|mean)\b",
        "extremum": (
            r"\b(?:highest|lowest|largest|smallest|maximum|minimum|max|min)\b"
        ),
        "ranking": (
            r"\b(?:top|bottom|first|last|rank|ranking|most|least)\b"
        ),
        "grouping": r"\b(?:each|every|per)\b|\bgroup(?:ed)?\s+by\b",
        "distinct": r"\b(?:distinct|different|unique)\b",
        "set_operation": r"\b(?:union|intersect|except)\b",
        "comparison": r"\b(?:between|among|versus|vs\.?|compared|difference|gap)\b",
        "variance": r"\b(?:variance|standard deviation|stddev|coefficient of variation)\b",
        "window": (
            r"\b(?:moving|rolling|running|cumulative)\b|"
            r"\b(?:lag|lead|window frame|preceding|following)\b"
        ),
        "having": (
            r"\b(?:groups?|categories|departments?|customers?)\s+(?:with|having)\b|"
            r"\bhaving\b"
        ),
        "anti_join": (
            r"\b(?:without|never|no other|not associated|do not have|does not have|"
            r"excluding those with)\b"
        ),
        "ratio": (
            r"\b(?:ratio|rate|percentage|percent|share|proportion|per cent|"
            r"coefficient of variation)\b"
        ),
        "rollup": r"\b(?:rollup|subtotal|grand total|grouping sets?)\b",
        "recursive": (
            r"\b(?:recursive|ancestor|descendant|hierarchy|hierarchical|"
            r"parent chain|child chain|path from|reachable)\b"
        ),
        "ties": r"\b(?:ties?|including ties|with ties|dense rank)\b",
    }
    for name, pattern in patterns.items():
        if re.search(pattern, normalized, flags=re.I | re.S):
            output.add(name)
    if _NAMED_MEASURE_LOOKUP.search(normalized):
        output.discard("count")
    return output


def _sql_program_features(sql: str) -> set[str]:
    """Extract SQL operators after removing identifiers and string literals."""

    normalized = str(sql).casefold()
    # Quoted display names such as "Free Meal Count (K-12)" must not be
    # mistaken for COUNT(...). Values also carry no relational operator signal.
    normalized = re.sub(r'"(?:[^"]|"")*"', " ", normalized)
    normalized = re.sub(r"`[^`]*`|\[[^]]*\]|'(?:[^']|'')*'", " ", normalized)
    patterns = {
        "count": r"\bcount\s*\(",
        "sum": r"\bsum\s*\(",
        "average": r"\bavg\s*\(",
        "extremum": r"\b(?:max|min)\s*\(",
        "ranking": r"\b(?:row_number|dense_rank|rank)\s*\(|\border\s+by\b[^;]*\blimit\b",
        "grouping": r"\bgroup\s+by\b",
        "distinct": r"\bselect\s+distinct\b",
        "window": r"\bover\s*\(|\bpartition\s+by\b|\b(?:lag|lead)\s*\(",
        "set_operation": r"\b(?:union|intersect|except)\b",
        "variance": r"\b(?:variance|var_pop|var_samp|stddev|stddev_pop|stddev_samp)\s*\(",
        "having": r"\bhaving\b",
        "anti_join": (
            r"\bnot\s+exists\b|\bnot\s+in\s*\(|"
            r"\bleft\s+(?:outer\s+)?join\b[\s\S]*?\bis\s+null\b"
        ),
        "ratio": r"(?<![/])/(?![/])|\b(?:percent_rank|ratio_to_report)\s*\(",
        "rollup": r"\b(?:rollup|cube|grouping\s+sets)\b",
        "recursive": r"\bwith\s+recursive\b",
        "ties": r"\b(?:dense_rank|rank)\s*\(|\bwith\s+ties\b",
        "cte": r"\bwith\b[\s\S]*?\bas\s*\(",
    }
    features = {
        name
        for name, pattern in patterns.items()
        if re.search(pattern, normalized, flags=re.I | re.S)
    }
    # ORDER BY ... LIMIT 1 is the SQL realization of a superlative even when
    # it does not spell MAX/MIN.  Treating it as ranking-only creates a false
    # "extremum gap" and can replace an already-correct top-1 query with a
    # riskier aggregate candidate.
    if re.search(r"\border\s+by\b[^;]*\blimit\s+1\b", normalized, flags=re.I | re.S):
        features.add("extremum")
    try:
        tree = sqlglot.parse_one(sql)
    except Exception:
        tree = None
    if tree is not None:
        for join in tree.find_all(exp.Join):
            predicate = join.args.get("on")
            if predicate is not None and sum(1 for _ in predicate.find_all(exp.EQ)) >= 2:
                features.add("composite_join")
                break
    return features


_DEMONSTRATION_PRESERVATION_FEATURES = {
    "cte": "CTE_BOUNDARY",
    "composite_join": "COMPOSITE_JOIN",
    "grouping": "GROUPING_GRAIN",
    "having": "HAVING",
    "window": "WINDOW_FRAME",
    "set_operation": "SET_OPERATION",
    "recursive": "RECURSIVE_DIRECTION",
    "ties": "TIE_HANDLING",
    "anti_join": "ANTI_JOIN",
    "ratio": "RATIO_DENOMINATOR",
    "rollup": "ROLLUP_SUBTOTAL",
}


def _slot_demonstration_literals(sql: str, dialect: str) -> str:
    """Render a historical SQL scaffold without its example-specific values."""

    try:
        tree = sqlglot.parse_one(sql, read=dialect.casefold())
    except Exception:
        return ""
    counter = 0

    def replace(node: exp.Expression) -> exp.Expression:
        nonlocal counter
        if not isinstance(node, exp.Literal):
            return node
        counter += 1
        if node.is_string:
            return exp.Literal.string(f"__TARGET_LITERAL_{counter}__")
        # A syntactically valid zero is safer than copying historical thresholds.
        return exp.Literal.number("0")

    return tree.transform(replace).sql(dialect=dialect.casefold())


def _current_catalog_identifiers(db_tools: Any) -> tuple[set[str], set[str]]:
    tables: set[str] = set()
    columns: set[str] = set()
    for table, values in dict(getattr(db_tools, "columns", {}) or {}).items():
        table_name = str(table)
        tables.add(table_name.casefold())
        for value in values or []:
            column = value[0] if isinstance(value, (tuple, list)) else value
            columns.add(f"{table_name}.{column}".casefold())
    return tables, columns


def _program_is_current_valid(
    program: dict[str, Any], *, db_tools: Any, dialect: str
) -> bool:
    sql = str(
        program.get("compiled_current_sql_pattern")
        or program.get("sql_template")
        or ""
    ).strip()
    if not sql:
        return False
    try:
        statements = sqlglot.parse(sql, read=dialect.casefold())
    except Exception:
        return False
    if len(statements) != 1 or not any(statements[0].find_all(exp.Select)):
        return False
    tables, columns = _current_catalog_identifiers(db_tools)
    if not tables:
        return True
    physical_tables = {
        str(value).casefold() for value in program.get("physical_tables") or []
    }
    if physical_tables and not physical_tables <= tables:
        return False
    physical_columns = {
        str(value).casefold() for value in program.get("physical_columns") or []
    }
    return not physical_columns or physical_columns <= columns


def _program_operator_skeleton(sql: str, dialect: str) -> list[str]:
    features = _sql_program_features(sql)
    output = [
        _DEMONSTRATION_PRESERVATION_FEATURES.get(value, value.upper())
        for value in sorted(features)
    ]
    try:
        tree = sqlglot.parse_one(sql, read=dialect.casefold())
    except Exception:
        return output[:16]
    ctes = list(tree.find_all(exp.CTE))
    joins = list(tree.find_all(exp.Join))
    if ctes:
        output.insert(0, f"CTE_STAGES:{len(ctes)}")
    if joins:
        output.append(f"JOIN_STAGES:{len(joins)}")
    return list(dict.fromkeys(output))[:16]


def _select_target_isolated_demonstrations(
    *,
    question: str,
    historical_programs: list[dict[str, Any]],
    role_bindings: dict[str, list[dict[str, Any]]],
    typed_edges: list[dict[str, Any]],
    db_tools: Any,
    dialect: str,
    maximum: int = 1,
) -> list[dict[str, Any]]:
    """Compile compact, target-disjoint demonstrations from recovered history.

    Selection uses only query text, current-schema bindings, typed graph edges,
    and the already retrieved support workload.  It never observes predictions,
    execution scores, evaluator SQL, or expected results.
    """

    normalized_question = " ".join(str(question).casefold().split())
    query_operators = relational_program_features(question)
    ranked: list[tuple[float, str, dict[str, Any]]] = []
    for program in historical_programs:
        if not isinstance(program, dict) or program.get("target_disjoint") is not True:
            continue
        historical_question = str(
            program.get("historical_question")
            or program.get("question_pattern")
            or ""
        ).strip()
        normalized_history = " ".join(historical_question.casefold().split())
        if normalized_history and normalized_history == normalized_question:
            # Upstream support materialization already excludes this collision;
            # retain a local fail-closed check at the final consumer boundary.
            continue
        if not _program_is_current_valid(program, db_tools=db_tools, dialect=dialect):
            continue
        sql = str(
            program.get("compiled_current_sql_pattern")
            or program.get("sql_template")
            or ""
        ).strip()
        program_operators = _sql_program_features(sql) | {
            str(value) for value in program.get("template_operators") or []
        }
        matched = query_operators & program_operators
        missing = query_operators - program_operators
        extra = program_operators - query_operators
        if query_operators:
            operator_recall = len(matched) / len(query_operators)
        else:
            operator_recall = 1.0
        operator_precision = len(matched) / max(1, len(program_operators))
        operator_f1 = (
            2 * operator_precision * operator_recall
            / (operator_precision + operator_recall)
            if operator_precision + operator_recall
            else 0.0
        )
        question_similarity = SequenceMatcher(
            None, normalized_question, normalized_history
        ).ratio()
        semantic_rrf = float(program.get("semantic_rrf") or 0.0)
        semantic_alignment = max(
            question_similarity,
            min(1.0, max(0.0, semantic_rrf) * 30.0),
        )
        program_columns = {
            str(value).casefold() for value in program.get("physical_columns") or []
        }
        program_tables = {
            str(value).casefold() for value in program.get("physical_tables") or []
        }
        role_map: list[list[str]] = []
        covered_roles = 0
        for role, candidates in role_bindings.items():
            chosen = ""
            for candidate in candidates[:2]:
                identifier = str(candidate.get("physical_identifier") or "")
                table = str(candidate.get("physical_table") or "")
                if (
                    identifier.casefold() in program_columns
                    or table.casefold() in program_tables
                ):
                    chosen = identifier
                    break
            if chosen:
                covered_roles += 1
                if len(role_map) < 8:
                    role_map.append([str(role), chosen])
        role_coverage = covered_roles / max(1, len(role_bindings))
        matching_edges: list[str] = []
        for edge in typed_edges:
            parent = str(edge.get("parent_table") or "").casefold()
            child = str(edge.get("child_table") or "").casefold()
            if parent in program_tables and child in program_tables:
                rendered = str(
                    edge.get("on_sql")
                    or f"{edge.get('left', '')}={edge.get('right', '')}"
                ).strip()
                if rendered and rendered not in matching_edges:
                    matching_edges.append(rendered)
        join_overlap = len(matching_edges) / max(1, len(typed_edges))
        extra_penalty = len(extra) / max(1, len(program_operators))
        alignment_score = (
            0.40 * semantic_alignment
            + 0.30 * role_coverage
            + 0.20 * operator_f1
            + 0.10 * join_overlap
            - 0.05 * extra_penalty
        )
        slotted_sql = _slot_demonstration_literals(sql, dialect)
        include_sql = (
            semantic_alignment >= 0.50
            and operator_recall >= 0.75
            and role_coverage >= 0.50
            and len(slotted_sql) <= 2800
        )
        preservation = [
            value
            for key, value in _DEMONSTRATION_PRESERVATION_FEATURES.items()
            if key in program_operators
        ]
        demonstration: dict[str, Any] = {
            "provenance_id": str(program.get("provenance_id") or ""),
            "target_disjoint": True,
            "current_physical_valid": True,
            "alignment": {
                "question": round(semantic_alignment, 6),
                "operator_f1": round(operator_f1, 6),
                "operator_recall": round(operator_recall, 6),
                "role_coverage": f"{covered_roles}/{len(role_bindings)}",
                "typed_join_overlap": round(join_overlap, 6),
                "missing_operators": sorted(missing),
                "extra_operators": sorted(extra),
            },
            "role_map": role_map,
            "operator_skeleton": _program_operator_skeleton(sql, dialect),
            "typed_join_edges": matching_edges[:4],
            "preserve": preservation,
            "replace": [
                "target_specific_outputs",
                "target_specific_literals",
                "unsupported_tables_and_predicates",
            ],
            "rendering": "current_bound_sql" if include_sql else "skeleton_only",
            "uses_evaluator_gold": False,
        }
        if include_sql:
            demonstration["current_bound_sql"] = slotted_sql
        ranked.append(
            (alignment_score, str(demonstration["provenance_id"]), demonstration)
        )
    ranked.sort(key=lambda value: (value[0], value[1]), reverse=True)
    return [value[2] for value in ranked[: max(0, maximum)]]


def _compact_planner_program(
    *,
    graph_evo_context: dict[str, Any],
    current_relational_program: dict[str, Any],
    demonstrations: list[dict[str, Any]],
) -> dict[str, Any]:
    """Render each recovered fact once for the fixed downstream generator."""

    compact_bindings: dict[str, list[dict[str, Any]]] = {}
    for role, candidates in dict(
        graph_evo_context.get("physical_bindings") or {}
    ).items():
        compact_candidates: list[dict[str, Any]] = []
        for candidate in list(candidates or [])[:2]:
            if not isinstance(candidate, dict):
                continue
            compact_candidates.append(
                {
                    key: candidate[key]
                    for key in (
                        "physical_identifier",
                        "physical_table",
                        "evidence_candidate_id",
                        "evidence_kind",
                        "required_companion_identifiers",
                        "semantic_alignment_status",
                        "role_rrf",
                    )
                    if candidate.get(key) not in (None, "", [])
                }
            )
        if compact_candidates:
            compact_bindings[str(role)] = compact_candidates
    compact_edges = [
        {
            key: edge[key]
            for key in (
                "left",
                "right",
                "parent_table",
                "parent_column",
                "child_table",
                "child_column",
                "on_sql",
                "evidence_class",
                "provenance_ids",
                "certified",
            )
            if edge.get(key) not in (None, "", [])
        }
        for edge in graph_evo_context.get("typed_join_edges") or []
        if isinstance(edge, dict)
    ]
    return {
        "compiler": "compact_role_first_relational_program_v1",
        "optimization_priority": list(
            current_relational_program.get("optimization_priority") or []
        ),
        "role_bindings": compact_bindings,
        "terminal_tables": list(graph_evo_context.get("terminal_tables") or []),
        "bridge_tables": list(graph_evo_context.get("bridge_tables") or []),
        "join_order": list(
            graph_evo_context.get("topological_table_order") or []
        ),
        "join_scaffold_sql": str(
            graph_evo_context.get("join_skeleton_sql") or ""
        ),
        "typed_edges": compact_edges,
        "exact_literal_bindings": list(
            graph_evo_context.get("exact_literal_bindings") or []
        ),
        "evolution_contract": list(
            graph_evo_context.get("evolution_contract") or []
        ),
        "metric_time_unit_contract": list(
            graph_evo_context.get("metric_time_unit_constraints") or []
        ),
        "evidence_ids": list(graph_evo_context.get("provenance_ids") or []),
        "target_isolated_demonstrations": demonstrations,
        "canonical_history_renderings": len(demonstrations),
        "duplicate_history_renderings": 0,
        "uses_evaluator_gold": False,
    }


def _compact_current_schema_for_program(
    program: dict[str, Any], *, db_tools: Any, table_limit: int = 16
) -> dict[str, list[str]]:
    """Expose bounded exact columns for role/edge tables before generation."""

    requested: list[str] = []

    def add(value: Any) -> None:
        text = str(value or "").strip()
        if text and text.casefold() not in {item.casefold() for item in requested}:
            requested.append(text)

    for candidates in dict(program.get("role_bindings") or {}).values():
        for candidate in candidates or []:
            if isinstance(candidate, dict):
                add(candidate.get("physical_table"))
    for value in program.get("terminal_tables") or []:
        add(value)
    for edge in program.get("typed_edges") or []:
        if isinstance(edge, dict):
            add(edge.get("parent_table"))
            add(edge.get("child_table"))
    catalog = dict(getattr(db_tools, "columns", {}) or {})
    lookup = {str(table).casefold(): str(table) for table in catalog}
    output: dict[str, list[str]] = {}
    for requested_table in requested:
        physical = lookup.get(requested_table.casefold())
        if physical is None:
            continue
        output[physical] = [
            str(value[0] if isinstance(value, (tuple, list)) else value)
            for value in catalog[physical]
        ][:120]
        if len(output) >= table_limit:
            break
    return output


def _sql_physical_identifiers(sql: str, dialect: str) -> set[str]:
    """Resolve SQL aliases into physical table.column identifiers."""

    try:
        tree = sqlglot.parse_one(sql, read=dialect.casefold())
    except Exception:
        return set()
    aliases: dict[str, str] = {}
    tables: set[str] = set()
    for table in tree.find_all(exp.Table):
        physical = str(table.name)
        if not physical:
            continue
        tables.add(physical)
        aliases[physical.casefold()] = physical
        aliases[str(table.alias_or_name).casefold()] = physical
    identifiers: set[str] = set()
    for column in tree.find_all(exp.Column):
        name = str(column.name)
        qualifier = str(column.table)
        if qualifier:
            table = aliases.get(qualifier.casefold(), qualifier)
            identifiers.add(f"{table}.{name}".casefold())
        else:
            # An unqualified column can belong to any referenced table; keeping
            # those candidates prevents alias style from changing the selector.
            identifiers.update(f"{table}.{name}".casefold() for table in tables)
    return identifiers


def _role_binding_coverage(
    sql: str,
    role_bindings: dict[str, list[dict[str, Any]]],
    dialect: str,
) -> dict[str, Any]:
    identifiers = _sql_physical_identifiers(sql, dialect)
    choices: dict[str, list[str]] = {}
    for role, candidates in role_bindings.items():
        matched: list[str] = []
        for candidate in candidates:
            identifier = str(candidate.get("physical_identifier") or "")
            required = [
                str(value)
                for value in candidate.get("required_companion_identifiers")
                or [identifier]
            ]
            if required and {
                value.casefold() for value in required
            } <= identifiers:
                matched.extend(required)
        matched = list(dict.fromkeys(matched))
        if matched:
            choices[role] = matched
    return {
        "covered_roles": len(choices),
        "distinct_physical_bindings": len(
            {identifier for values in choices.values() for identifier in values}
        ),
        "role_choices": choices,
    }


def _authoritative_react_submission_audit(
    *,
    react_sql: str,
    planner_sql: str,
    role_bindings: dict[str, list[dict[str, Any]]],
    dialect: str,
) -> dict[str, Any]:
    """Record candidate coverage without post-hoc answer switching.

    Role coverage is a syntactic audit over retrieval hypotheses.  It does not
    certify that a column realizes the requested semantic role, so it must not
    override the SQL explicitly revised and submitted by the ReACT trajectory.
    """

    return {
        "selected": "react",
        "criterion": "react_submission_authoritative_no_posthoc_selector",
        "runtime_switching_enabled": False,
        "react_role_coverage": _role_binding_coverage(
            react_sql, role_bindings, dialect
        ),
        "planner_role_coverage": _role_binding_coverage(
            planner_sql, role_bindings, dialect
        ),
        "uses_evaluator_gold": False,
    }


def _workload_program(row: CatalogDocument) -> dict[str, Any] | None:
    if not row.candidate_id.startswith(("workload::", "history_sql::", "program::")):
        return None
    try:
        payload = json.loads(row.text)
    except (TypeError, ValueError):
        return None
    if row.candidate_id.startswith("program::") and (
        payload.get("ontology_kind") != "sql_workload_semantic_object"
        or payload.get("kind") != "program"
    ):
        return None
    question = str(
        payload.get("question_pattern")
        or payload.get("historical_question")
        or ""
    ).strip()
    sql = str(
        payload.get("sql_template")
        or payload.get("compiled_current_sql_pattern")
        or ""
    ).strip()
    if not sql:
        return None
    return {
        "candidate_id": row.candidate_id,
        "provenance_id": str(
            payload.get("provenance_id") or row.candidate_id
        ),
        "target_disjoint": payload.get("target_disjoint") is True,
        "question_pattern": question,
        "historical_question": question,
        "sql_template": sql,
        "compiled_current_sql_pattern": sql,
        "physical_tables": list(payload.get("physical_tables") or []),
        "physical_columns": list(payload.get("physical_columns") or []),
        "template_operators": sorted(
            relational_program_features(question) | _sql_program_features(sql)
        ),
    }


def _target_isolated_history_inventory(
    rows: list[CatalogDocument], *, target_question: str
) -> list[dict[str, Any]]:
    """Return the frozen, database-local support-program inventory.

    This inventory is used only for exact draft/program concordance.  It is not
    rendered as generic few-shot demonstrations.  Fail closed on the explicit
    ``target_disjoint`` marker and independently reject a normalized question
    collision at the final consumer boundary.
    """

    normalized_target = " ".join(str(target_question).casefold().split())
    output: list[dict[str, Any]] = []
    observed: set[tuple[str, str]] = set()
    for row in rows:
        program = _workload_program(row)
        if program is None or program.get("target_disjoint") is not True:
            continue
        normalized_history = " ".join(
            str(program.get("question_pattern") or "").casefold().split()
        )
        if normalized_history and normalized_history == normalized_target:
            continue
        key = (
            str(program.get("provenance_id") or ""),
            sha256(str(program.get("sql_template") or "").encode()).hexdigest(),
        )
        if key in observed:
            continue
        observed.add(key)
        output.append(program)
    output.sort(
        key=lambda value: (
            str(value.get("provenance_id") or ""),
            str(value.get("candidate_id") or ""),
        )
    )
    return output


def _edge_endpoint(value: Any) -> tuple[str, str] | None:
    table, separator, column = str(value or "").rpartition(".")
    if not separator or not table.strip() or not column.strip():
        return None
    return table.strip(), column.strip()


def _relationship_evidence(source: dict[str, Any]) -> list[str]:
    evidence = source.get("evidence_types") or source.get("evidence") or []
    if isinstance(evidence, str):
        evidence = [value for value in evidence.split("+") if value]
    return [str(value) for value in evidence]


def _trusted_relationship_edge(source: dict[str, Any]) -> bool:
    return bool(
        TRUSTED_RELATIONSHIP_EVIDENCE.intersection(
            _relationship_evidence(source)
        )
    )


def _weighted_shortest_path(
    adjacency: dict[str, list[tuple[str, int, float]]],
    sources: set[str],
    target: str,
) -> tuple[float, list[int]] | None:
    queue: list[tuple[float, str, tuple[int, ...]]] = [(0.0, target, ())]
    best = {target: 0.0}
    while queue:
        cost, table, path = heapq.heappop(queue)
        if cost > best.get(table, float("inf")):
            continue
        if table in sources:
            return cost, list(reversed(path))
        for neighbor, edge_index, edge_cost in adjacency.get(table, []):
            next_cost = cost + edge_cost
            if next_cost >= best.get(neighbor, float("inf")):
                continue
            best[neighbor] = next_cost
            heapq.heappush(queue, (next_cost, neighbor, (*path, edge_index)))
    return None


def relational_program_graph_closure(
    *,
    ranked: list[CatalogDocument],
    raw_documents: list[CatalogDocument],
    ontology_edges: list[dict[str, Any]],
    terminal_tables: list[str],
) -> tuple[list[CatalogDocument], dict[str, Any]]:
    """Compile selected evidence into a weighted, physical query subgraph."""

    raw_tables = {
        str(row.table): row
        for row in raw_documents
        if row.kind == "table" and row.table
    }
    raw_by_id = {row.candidate_id: row for row in raw_documents}
    terminal_limit = 8 if any(_workload_program(row) for row in ranked) else 4
    terminals = [
        table
        for table in dict.fromkeys(terminal_tables)
        if table in raw_tables
    ][:terminal_limit]
    edge_by_pair: dict[tuple[str, str], dict[str, Any]] = {}

    def add_edge(source: dict[str, Any]) -> None:
        evidence = _relationship_evidence(source)
        # Profile/name/value overlap is useful retrieval evidence, but it does not
        # establish relational joinability.  Letting those edges connect a query
        # graph created spurious hubs such as WAREHOUSE_LOAD_DATE across unrelated
        # BEAVER tables.  Graph compilation uses only relationship-bearing evidence.
        if not _trusted_relationship_edge(source):
            return
        left_endpoint = _edge_endpoint(source.get("left"))
        right_endpoint = _edge_endpoint(source.get("right"))
        if left_endpoint and right_endpoint:
            left_table, left_column = left_endpoint
            right_table, right_column = right_endpoint
            precise = True
        else:
            left_table = str(source.get("left_table") or "")
            right_table = str(source.get("right_table") or "")
            left_column = right_column = ""
            precise = False
        if (
            not left_table
            or not right_table
            or left_table == right_table
            or left_table not in raw_tables
            or right_table not in raw_tables
        ):
            return
        score = min(max(float(source.get("score", 0.5)), 0.05), 1.0)
        normalized = {
            "left": (
                f"{left_table}.{left_column}" if left_column else left_table
            ),
            "right": (
                f"{right_table}.{right_column}" if right_column else right_table
            ),
            "left_table": left_table,
            "right_table": right_table,
            "score": round(score, 4),
            "evidence_types": evidence,
            "provenance_ids": list(source.get("provenance_ids") or [])[:4],
            "provenance_count": len(source.get("provenance_ids") or []),
            "physical_join_columns_known": precise,
        }
        pair = tuple(sorted((left_table, right_table)))
        previous = edge_by_pair.get(pair)
        if previous is None or (
            precise,
            score,
        ) > (
            bool(previous["physical_join_columns_known"]),
            float(previous["score"]),
        ):
            edge_by_pair[pair] = normalized

    for source in ontology_edges:
        add_edge(dict(source))
    for table, row in raw_tables.items():
        for reference in row.references:
            add_edge(
                {
                    "left_table": table,
                    "right_table": reference,
                    "score": 1.0,
                    "evidence_types": ["declared_foreign_key_table_connectivity"],
                }
            )

    edges = list(edge_by_pair.values())
    adjacency: dict[str, list[tuple[str, int, float]]] = {
        table: [] for table in raw_tables
    }
    for edge_index, edge in enumerate(edges):
        cost = 0.25 + -math.log(max(float(edge["score"]), 0.05))
        left_table = str(edge["left_table"])
        right_table = str(edge["right_table"])
        adjacency[left_table].append((right_table, edge_index, cost))
        adjacency[right_table].append((left_table, edge_index, cost))

    selected_edge_ids: list[int] = []
    connected: set[str] = set(terminals[:1])
    remaining = terminals[1:]
    disconnected: list[str] = []
    while remaining:
        choices: list[tuple[float, int, list[int], str]] = []
        for rank, target in enumerate(remaining):
            path = _weighted_shortest_path(adjacency, connected, target)
            if path is not None:
                choices.append((path[0], rank, path[1], target))
        if not choices:
            target = remaining.pop(0)
            disconnected.append(target)
            connected.add(target)
            continue
        _, _, path_edges, target = min(choices)
        for edge_index in path_edges:
            if edge_index not in selected_edge_ids and len(selected_edge_ids) < 16:
                selected_edge_ids.append(edge_index)
            edge = edges[edge_index]
            connected.update((str(edge["left_table"]), str(edge["right_table"])))
        connected.add(target)
        remaining.remove(target)

    selected_edges = [edges[index] for index in selected_edge_ids]
    selected_tables = {
        table
        for edge in selected_edges
        for table in (str(edge["left_table"]), str(edge["right_table"]))
    }
    bridges = sorted(selected_tables - set(terminals))
    output = list(ranked)
    observed = {row.candidate_id for row in output}

    def include(candidate_id: str) -> None:
        row = raw_by_id.get(candidate_id)
        if row is not None and candidate_id not in observed:
            output.append(row)
            observed.add(candidate_id)

    for table in [*terminals, *bridges]:
        include(f"table::{ranked[0].database_id if ranked else ''}::{table}")
    for edge in selected_edges:
        if not edge["physical_join_columns_known"]:
            continue
        left = _edge_endpoint(edge["left"])
        right = _edge_endpoint(edge["right"])
        for endpoint in (left, right):
            if endpoint:
                include(
                    f"column::{ranked[0].database_id if ranked else ''}::"
                    f"{endpoint[0]}::{endpoint[1]}"
                )
    return output, {
        "terminal_tables": terminals,
        "bridge_tables": bridges,
        "physical_join_edges": selected_edges,
        "disconnected_terminals": disconnected,
        "compiler": "weighted_relationship_graph_mst_v2",
        "uses_evaluator_gold": False,
    }


class SchemaSearchIndex:
    def __init__(
        self,
        *,
        documents: list[CatalogDocument],
        raw_documents: list[CatalogDocument],
        vectors: dict[str, np.ndarray],
        encode_query: Callable[[str], np.ndarray],
        encode_queries: Callable[[list[str]], np.ndarray] | None = None,
        sidecar_documents: list[CatalogDocument] | None = None,
        ontology_edges_by_database: dict[str, list[dict[str, Any]]] | None = None,
        bindings_by_document: dict[str, list[str]] | None = None,
        program_graph: bool = False,
        minimal_join_tree: bool = False,
        rerank_documents: Callable[[str, list[str]], list[float]] | None = None,
        rerank_top_k: int = 30,
        evidence_first_history: bool = False,
    ) -> None:
        if {row.candidate_id for row in documents} != set(vectors):
            raise ValueError("embedding IDs do not match search documents")
        self.documents = documents
        self.raw_documents = raw_documents
        self.vectors = vectors
        self.encode_query = encode_query
        self.encode_queries = encode_queries
        self.sidecars = {
            (row.database_id, row.name): row
            for row in sidecar_documents or []
        }
        if len(self.sidecars) != len(sidecar_documents or []):
            raise ValueError("duplicate schema-search sidecar bindings")
        self.ontology_edges_by_database = dict(ontology_edges_by_database or {})
        self.bindings_by_document = dict(bindings_by_document or {})
        self.minimal_join_tree = bool(minimal_join_tree)
        self.program_graph = bool(program_graph or minimal_join_tree)
        if rerank_documents is not None and not 1 <= rerank_top_k <= 100:
            raise ValueError("rerank_top_k must be between 1 and 100")
        self.rerank_documents = rerank_documents
        self.rerank_top_k = int(rerank_top_k)
        self.evidence_first_history = bool(evidence_first_history)
        self.by_database: dict[str, list[CatalogDocument]] = {}
        self.raw_by_database: dict[str, list[CatalogDocument]] = {}
        self.raw_by_id: dict[str, CatalogDocument] = {}
        for row in documents:
            self.by_database.setdefault(row.database_id, []).append(row)
        for row in raw_documents:
            self.raw_by_database.setdefault(row.database_id, []).append(row)
            self.raw_by_id[row.candidate_id] = row
        raw_ids_by_name: dict[tuple[str, str], list[str]] = {}
        for row in raw_documents:
            raw_ids_by_name.setdefault(
                (row.database_id, row.name.casefold()), []
            ).append(row.candidate_id)
        # Recovery nodes are field-level semantic views of an existing physical
        # table/column.  Their names are deliberately preserved exactly by
        # build_recovery_documents, so bind them back to that raw catalog node.
        # Previously only workload/KB nodes had bindings: useful recovered
        # aliases could rank highly but vanished before graph compilation, and
        # query-role candidates then came from broad KB rows in arbitrary order.
        for row in documents:
            if row.kind not in {"recovery_table", "recovery_column"}:
                continue
            implicit = raw_ids_by_name.get(
                (row.database_id, row.name.casefold()), []
            )
            if not implicit:
                continue
            explicit = list(self.bindings_by_document.get(row.candidate_id, []))
            self.bindings_by_document[row.candidate_id] = list(
                dict.fromkeys([*implicit, *explicit])
            )
        if self.minimal_join_tree:
            # Raw and evolved column documents are valid role evidence too. The
            # legacy graph only admitted recovery_column/KB nodes, leaving BIRD
            # and EvoSchema without any query roles despite field-complete DDL.
            for row in documents:
                if row.kind == "column" and row.candidate_id in self.raw_by_id:
                    self.bindings_by_document.setdefault(
                        row.candidate_id, [row.candidate_id]
                    )
        self.document_vectors_by_database: dict[str, np.ndarray] = {}
        self.document_text_by_id: dict[str, str] = {}
        self.document_terms_by_id: dict[str, set[str]] = {}
        for context, rows in self.by_database.items():
            self.document_vectors_by_database[context] = np.asarray(
                [self.vectors[row.candidate_id] for row in rows],
                dtype=np.float32,
            )
            for row in rows:
                text = row.retrieval_text().casefold()
                self.document_text_by_id[row.candidate_id] = text
                self.document_terms_by_id[row.candidate_id] = _terms(text)
        self.role_documents_by_database: dict[str, list[CatalogDocument]] = {}
        self.role_vectors_by_database: dict[str, np.ndarray] = {}
        self.role_text_by_id: dict[str, str] = {}
        self.role_terms_by_id: dict[str, set[str]] = {}
        self.role_topics_by_id: dict[str, set[str]] = {}
        if self.program_graph:
            for context, rows in self.by_database.items():
                if self.minimal_join_tree:
                    eligible = []
                    for row in rows:
                        if row.candidate_id.startswith(
                            ("workload::", "history_sql::")
                        ):
                            continue
                        column_bindings = [
                            candidate_id
                            for candidate_id in self.bindings_by_document.get(
                                row.candidate_id, []
                            )
                            if candidate_id.startswith("column::")
                        ]
                        narrow_kb = (
                            row.candidate_id.startswith("kb::")
                            and 0 < len(column_bindings) <= 2
                        )
                        field_level = (
                            row.kind in {
                                "column",
                                "recovery_column",
                                "schema_lineage_column",
                            }
                            or len(column_bindings) == 1
                        )
                        if field_level or narrow_kb:
                            eligible.append(row)
                else:
                    eligible = [
                        row
                        for row in rows
                        if row.kind == "recovery_column"
                        or row.candidate_id.startswith("kb::")
                    ]
                if not eligible:
                    continue
                self.role_documents_by_database[context] = eligible
                self.role_vectors_by_database[context] = np.asarray(
                    [self.vectors[row.candidate_id] for row in eligible],
                    dtype=np.float32,
                )
                for row in eligible:
                    text = row.retrieval_text().casefold()
                    self.role_text_by_id[row.candidate_id] = text
                    self.role_terms_by_id[row.candidate_id] = _terms(text)
                    self.role_topics_by_id[row.candidate_id] = _topic_terms(text)

    def _cross_encoder_rerank(
        self,
        query: str,
        ranked: list[CatalogDocument],
    ) -> tuple[list[CatalogDocument], dict[str, float]]:
        if self.rerank_documents is None or not ranked:
            return ranked, {}
        candidate_count = min(self.rerank_top_k, len(ranked))
        candidates = ranked[:candidate_count]
        scores = self.rerank_documents(
            query,
            [row.retrieval_text() for row in candidates],
        )
        if len(scores) != candidate_count:
            raise RuntimeError("reranker score count does not match candidate count")
        normalized = [float(score) for score in scores]
        if any(not math.isfinite(score) for score in normalized):
            raise RuntimeError("reranker returned a non-finite score")
        reranked = [
            candidates[index]
            for index in sorted(
                range(candidate_count),
                key=lambda index: (-normalized[index], index),
            )
        ]
        return [*reranked, *ranked[candidate_count:]], {
            row.candidate_id: normalized[index]
            for index, row in enumerate(candidates)
        }

    def _query_role_bindings(
        self, database_id: str, query: str
    ) -> tuple[
        dict[str, list[dict[str, Any]]],
        list[CatalogDocument],
        list[str],
    ]:
        """Retrieve field-level physical bindings independently for each role."""

        eligible = self.role_documents_by_database.get(database_id, [])
        if not eligible:
            return {}, [], []
        matrix = self.role_vectors_by_database[database_id]
        size = len(eligible)
        indices = np.arange(size, dtype=np.int32)
        role_bindings: dict[str, list[dict[str, Any]]] = {}
        evidence_rows: list[CatalogDocument] = []
        evidence_ids: set[str] = set()
        physical_ids: list[str] = []
        physical_id_set: set[str] = set()
        lineage_by_identifier: dict[str, dict[str, Any]] = {}
        for row in eligible:
            if not row.kind.startswith("schema_evolution_"):
                continue
            try:
                payload = json.loads(row.text)
            except (TypeError, ValueError):
                continue
            relation = str(payload.get("relation") or "")
            historical = [
                str(value)
                for value in payload.get("historical_source_identifiers") or []
            ]
            for bound_id in self.bindings_by_document.get(row.candidate_id, []):
                if not bound_id.startswith("column::"):
                    continue
                physical = self.raw_by_id.get(bound_id)
                if physical is None or physical.database_id != database_id:
                    continue
                lineage_by_identifier[str(physical.name)] = {
                    "lineage_relation": relation,
                    "historical_source_identifiers": historical,
                    "lineage_evidence_kind": row.kind,
                    "lineage_evidence_candidate_id": row.candidate_id,
                }
        phrases = (
            _minimal_join_tree_role_phrases(query)
            if self.minimal_join_tree
            else _query_role_phrases(query)
        )
        retrieval_phrases = [
            phrase.partition(" role: ")[2]
            if self.minimal_join_tree and " role: " in phrase
            else phrase
            for phrase in phrases
        ]
        if self.encode_queries is not None:
            phrase_vectors = np.asarray(
                self.encode_queries(retrieval_phrases), dtype=np.float32
            )
        else:
            phrase_vectors = np.asarray(
                [self.encode_query(phrase) for phrase in retrieval_phrases],
                dtype=np.float32,
            )
        for phrase, retrieval_phrase, vector in zip(
            phrases, retrieval_phrases, phrase_vectors, strict=True
        ):
            similarities = matrix @ vector
            dense_order = np.argsort(-similarities, kind="stable")
            dense_rank = np.empty(size, dtype=np.int32)
            dense_rank[dense_order] = indices
            phrase_terms = _topic_terms(retrieval_phrase)
            lexical_terms = _terms(retrieval_phrase) - _QUESTION_WORDS - {
                "a",
                "an",
                "of",
                "the",
            }
            folded_phrase = retrieval_phrase.casefold()
            exact = np.fromiter(
                (
                    int(
                        folded_phrase
                        in self.role_text_by_id[row.candidate_id]
                    )
                    for row in eligible
                ),
                dtype=np.int8,
                count=size,
            )
            lexical_overlap = np.fromiter(
                (
                    len(
                        lexical_terms
                        & self.role_terms_by_id[row.candidate_id]
                    )
                    for row in eligible
                ),
                dtype=np.int16,
                count=size,
            )
            topic_overlap = np.fromiter(
                (
                    len(
                        phrase_terms
                        & self.role_topics_by_id[row.candidate_id]
                    )
                    for row in eligible
                ),
                dtype=np.int16,
                count=size,
            )
            lexical_order = np.lexsort(
                (indices, -topic_overlap, -lexical_overlap, -exact)
            )
            lexical_rank = np.empty(size, dtype=np.int32)
            lexical_rank[lexical_order] = indices
            role_scores = (
                0.25 / (20.0 + dense_rank)
                + 0.75 / (20.0 + lexical_rank)
            )
            ranked_order = np.argsort(-role_scores, kind="stable")
            candidate_pool: list[dict[str, Any]] = []
            observed_identifiers: set[str] = set()
            candidates_per_table: dict[str, int] = {}
            candidate_limit = 8 if self.minimal_join_tree else 6
            candidate_pool_limit = 32 if self.minimal_join_tree else candidate_limit
            for row_index in ranked_order:
                row = eligible[int(row_index)]
                bound_ids = self.bindings_by_document.get(row.candidate_id, [])
                for candidate_id in bound_ids:
                    if not candidate_id.startswith("column::"):
                        continue
                    physical = self.raw_by_id.get(candidate_id)
                    if physical is None or physical.database_id != database_id:
                        continue
                    identifier = str(physical.name)
                    if identifier in observed_identifiers:
                        continue
                    table_name = str(physical.table or "")
                    if (
                        self.minimal_join_tree
                        and candidates_per_table.get(table_name, 0) >= 4
                    ):
                        continue
                    observed_identifiers.add(identifier)
                    candidates_per_table[table_name] = (
                        candidates_per_table.get(table_name, 0) + 1
                    )
                    lineage = dict(lineage_by_identifier.get(identifier) or {})
                    alignment_kind = str(
                        lineage.get("lineage_evidence_kind") or row.kind
                    )
                    alignment = (
                        _role_identifier_alignment(
                            phrase, identifier, evidence_kind=alignment_kind
                        )
                        if self.minimal_join_tree
                        else {
                            "score": 0.0,
                            "field_overlap": [],
                            "table_overlap": [],
                            "lineage_bonus": 0.0,
                            "penalties": [],
                            "status": "not_applied",
                        }
                    )
                    evidence_kind = str(
                        lineage.pop("lineage_evidence_kind", row.kind)
                    )
                    evidence_candidate_id = str(
                        lineage.pop(
                            "lineage_evidence_candidate_id", row.candidate_id
                        )
                    )
                    candidate_pool.append(
                        {
                            "physical_identifier": identifier,
                            "physical_table": physical.table,
                            "evidence_kind": evidence_kind,
                            "evidence_candidate_id": evidence_candidate_id,
                            "role_rrf": round(
                                float(role_scores[int(row_index)]), 8
                            ),
                            "semantic_alignment": alignment,
                            "_physical_candidate_id": candidate_id,
                            **lineage,
                        }
                    )
                    if len(candidate_pool) >= candidate_pool_limit:
                        break
                if len(candidate_pool) >= candidate_pool_limit:
                    break

            if self.minimal_join_tree and candidate_pool:
                phrase_parts = _identifier_parts(retrieval_phrase)
                compound_groups: dict[
                    tuple[str, tuple[str, ...]], list[dict[str, Any]]
                ] = {}
                for candidate in candidate_pool:
                    if candidate.get("lineage_relation") != "column_split":
                        continue
                    historical = tuple(
                        sorted(candidate.get("historical_source_identifiers") or [])
                    )
                    if not historical:
                        continue
                    source_parts = set().union(
                        *(
                            _identifier_parts(value.rpartition(".")[2])
                            for value in historical
                        )
                    )
                    if not (source_parts & phrase_parts):
                        continue
                    compound_groups.setdefault(
                        (str(candidate.get("physical_table") or ""), historical),
                        [],
                    ).append(candidate)
                raw_order = {
                    row.candidate_id: index
                    for index, row in enumerate(
                        self.raw_by_database.get(database_id, [])
                    )
                }
                for values in compound_groups.values():
                    if len(values) < 2:
                        continue
                    current_parts = {
                        part
                        for candidate in values
                        for part in _identifier_parts(
                            str(candidate["physical_identifier"]).rpartition(".")[2]
                        )
                    }
                    source_parts = {
                        part
                        for value in values[0].get(
                            "historical_source_identifiers"
                        )
                        or []
                        for part in _identifier_parts(str(value).rpartition(".")[2])
                    }
                    # If the question explicitly asks for a current component
                    # such as ``year``, it is not asking for the whole old date.
                    if (current_parts - source_parts) & phrase_parts:
                        continue
                    members = [
                        str(candidate["physical_identifier"])
                        for candidate in sorted(
                            values,
                            key=lambda candidate: raw_order.get(
                                str(candidate["_physical_candidate_id"]), 10**9
                            ),
                        )
                    ]
                    for candidate in values:
                        candidate["compound_source_identifiers"] = list(
                            candidate.get("historical_source_identifiers") or []
                        )
                        candidate["required_companion_identifiers"] = members

            candidate_pool.sort(
                key=lambda candidate: (
                    -float(
                        (candidate.get("semantic_alignment") or {}).get(
                            "score", 0.0
                        )
                    ),
                    -float(candidate.get("role_rrf", 0.0)),
                    str(candidate.get("physical_identifier") or ""),
                )
            )
            candidates = candidate_pool[:candidate_limit]
            if candidates:
                companion_ids = {
                    identifier
                    for candidate in candidates
                    for identifier in candidate.get(
                        "required_companion_identifiers"
                    )
                    or []
                }
                selected_evidence = [
                    candidate
                    for candidate in candidate_pool
                    if candidate in candidates
                    or str(candidate.get("physical_identifier") or "")
                    in companion_ids
                ]
                for candidate in selected_evidence:
                    evidence_id = str(candidate["evidence_candidate_id"])
                    if evidence_id not in evidence_ids:
                        evidence_row = next(
                            row
                            for row in eligible
                            if row.candidate_id == evidence_id
                        )
                        evidence_rows.append(evidence_row)
                        evidence_ids.add(evidence_id)
                    physical_candidate_id = str(
                        candidate["_physical_candidate_id"]
                    )
                    if physical_candidate_id not in physical_id_set:
                        physical_ids.append(physical_candidate_id)
                        physical_id_set.add(physical_candidate_id)
                role_bindings[phrase] = [
                    {
                        key: value
                        for key, value in candidate.items()
                        if key != "_physical_candidate_id"
                    }
                    for candidate in candidates
                ]
        return role_bindings, evidence_rows[:18], physical_ids[:18]

    def search(
        self,
        database_id: str,
        query: str,
        top_k: int = 12,
        *,
        enable_reranker: bool = True,
    ) -> dict[str, Any]:
        if not 1 <= top_k <= 20:
            raise ValueError("top_k must be between 1 and 20")
        documents = self.by_database.get(database_id) or []
        if not documents:
            raise KeyError(f"no search documents for database {database_id}")
        query_vector = np.asarray(self.encode_query(query), dtype=np.float32)
        size = len(documents)
        indices = np.arange(size, dtype=np.int32)
        similarities = self.document_vectors_by_database[database_id] @ query_vector
        dense_order = np.argsort(-similarities, kind="stable")
        dense_rank_array = np.empty(size, dtype=np.int32)
        dense_rank_array[dense_order] = indices
        query_terms = _terms(query)
        literals = [
            value.casefold()
            for value in re.findall(r"['\"]([^'\"]{2,80})['\"]", query)
        ]
        lexical_literal = np.fromiter(
            (
                sum(
                    literal in self.document_text_by_id[row.candidate_id]
                    for literal in literals
                )
                for row in documents
            ),
            dtype=np.int16,
            count=size,
        )
        lexical_overlap = np.fromiter(
            (
                len(query_terms & self.document_terms_by_id[row.candidate_id])
                for row in documents
            ),
            dtype=np.int16,
            count=size,
        )
        lexical_phrases = np.fromiter(
            (
                sum(
                    term in self.document_text_by_id[row.candidate_id]
                    for term in query_terms
                )
                for row in documents
            ),
            dtype=np.int16,
            count=size,
        )
        lexical_order = np.lexsort(
            (indices, -lexical_phrases, -lexical_overlap, -lexical_literal)
        )
        lexical_rank_array = np.empty(size, dtype=np.int32)
        lexical_rank_array[lexical_order] = indices
        rrf_array = (
            1.0 / (60.0 + dense_rank_array)
            + 1.0 / (60.0 + lexical_rank_array)
        )
        ranked_order = np.argsort(-rrf_array, kind="stable")
        ranked = [documents[int(index)] for index in ranked_order]
        rrf_scores = {
            row.candidate_id: float(rrf_array[index])
            for index, row in enumerate(documents)
        }
        if enable_reranker:
            ranked, reranker_scores = self._cross_encoder_rerank(query, ranked)
        else:
            reranker_scores = {}
        # A global top-k allowed semantically similar workload questions to take
        # almost every slot (15.7 per BEAVER query on the first run), starving the
        # physical/recovered schema while still omitting executable structure.
        # Keep only the two best target-disjoint SQL templates and fill the rest
        # with independently ranked schema/KB evidence.
        query_operators = relational_program_features(query)
        query_topics = _topic_terms(query)
        selected_programs: list[dict[str, Any]] = []
        if self.program_graph:
            if self.evidence_first_history and self.rerank_documents is not None:
                # SQL-only ontology aliases are language-bearing evidence even when
                # the historical user question is intentionally absent. Rank the
                # program inventory separately so schema rows cannot consume its pool.
                history_pool = [row for row in ranked if _workload_program(row) is not None][:40]
                history_scores = self.rerank_documents(query, [row.retrieval_text() for row in history_pool])
                if len(history_scores) != len(history_pool):
                    raise RuntimeError("Incomplete history reranking")
                reranker_scores.update({row.candidate_id: float(score) for row, score in zip(history_pool, history_scores)})
            scored_programs: list[
                tuple[int, float, float, float, CatalogDocument, dict[str, Any]]
            ] = []
            for row in ranked:
                program = _workload_program(row)
                if program is None:
                    continue
                template_operators = set(program["template_operators"])
                matched = query_operators & template_operators
                missing = query_operators - template_operators
                extra = template_operators - query_operators
                compatibility = (
                    3.0 * len(matched) - 2.0 * len(missing) - 0.35 * len(extra)
                )
                physical_text = " ".join(
                    [
                        str(program["question_pattern"]),
                        *(str(value) for value in program["physical_tables"]),
                        *(str(value) for value in program["physical_columns"]),
                    ]
                )
                topic_overlap = sorted(query_topics & _topic_terms(physical_text))
                relevant_tables = []
                if not program["question_pattern"]:
                    # Opaque assets can intentionally omit historical language;
                    # their compiled physical bindings are the useful signal.
                    relevant_tables = [
                        str(table) for table in program["physical_tables"]
                    ]
                else:
                    for table in program["physical_tables"]:
                        columns = [
                            value
                            for value in program["physical_columns"]
                            if str(value).startswith(f"{table}.")
                        ]
                        if query_topics & _topic_terms(
                            " ".join([str(table), *columns])
                        ):
                            relevant_tables.append(str(table))
                program["matched_query_operators"] = sorted(matched)
                program["missing_query_operators"] = sorted(missing)
                program["operator_compatibility"] = round(compatibility, 4)
                program["topic_overlap"] = topic_overlap
                program["relevant_physical_tables"] = relevant_tables
                program["semantic_rrf"] = round(
                    rrf_scores[row.candidate_id], 8
                )
                semantic_relevance = reranker_scores.get(
                    row.candidate_id, rrf_scores[row.candidate_id]
                )
                if row.candidate_id in reranker_scores:
                    program["semantic_reranker_score"] = round(
                        semantic_relevance, 8
                    )
                # When history has language, operator shape alone is not enough:
                # COUNT/GROUP BY previously promoted unrelated employee and space
                # templates for a sponsor query.  Require entity overlap there.
                has_question_pattern = bool(program["question_pattern"])
                if has_question_pattern and not topic_overlap and not self.evidence_first_history:
                    continue
                if self.evidence_first_history:
                    priority = (1, semantic_relevance, float(len(topic_overlap)), compatibility)
                    program["selection_basis"] = "sql_derived_semantic_relevance_then_structure"
                elif has_question_pattern:
                    if enable_reranker:
                        priority = (
                            2,
                            float(len(topic_overlap)),
                            compatibility,
                            semantic_relevance,
                        )
                        program["selection_basis"] = (
                            "topic_then_operator_then_semantic"
                        )
                    else:
                        priority = (
                            2,
                            float(len(topic_overlap)),
                            semantic_relevance,
                            compatibility,
                        )
                        program["selection_basis"] = (
                            "topic_then_semantic_then_operator"
                        )
                else:
                    # Some masked-schema assets intentionally retain executable
                    # historical SQL but no natural-language history.  There is
                    # no entity text to match in that setting; operator shape is
                    # the available target-disjoint information signal.
                    priority = (
                        1,
                        compatibility,
                        semantic_relevance,
                        0.0,
                    )
                    program["selection_basis"] = "operator_then_semantic_no_question"
                scored_programs.append(
                    (*priority, row, program)
                )
            seen_sql: set[str] = set()
            selected_rows: list[CatalogDocument] = []
            for _, _, _, _, row, program in sorted(
                scored_programs,
                key=lambda item: (item[0], item[1], item[2], item[3]),
                reverse=True,
            ):
                normalized_sql = " ".join(program["sql_template"].casefold().split())
                if normalized_sql in seen_sql:
                    continue
                seen_sql.add(normalized_sql)
                selected_rows.append(row)
                selected_programs.append(program)
                if len(selected_rows) >= (8 if self.evidence_first_history else 2):
                    break
            selected_ids = {row.candidate_id for row in selected_rows}
            if selected_programs and all(
                not program["question_pattern"] for program in selected_programs
            ):
                # Preserve the previously successful masked-schema path: SQL
                # structure and its physical bindings precede semantic evidence.
                non_programs = [
                    row for row in ranked if _workload_program(row) is None
                ]
                combined = [
                    *selected_rows,
                    *non_programs[: max(0, top_k - len(selected_rows))],
                ]
            else:
                # With language-bearing history, preserve the original semantic
                # ranking so templates cannot displace better recovered evidence.
                combined = []
                for row in ranked:
                    if (
                        _workload_program(row) is not None
                        and row.candidate_id not in selected_ids
                    ):
                        continue
                    combined.append(row)
                    if len(combined) >= top_k:
                        break
            workload_count = len(selected_rows)
        else:
            combined = []
            workload_count = 0
            for row in ranked:
                is_workload = row.candidate_id.startswith("workload::")
                if is_workload and workload_count >= 2:
                    continue
                combined.append(row)
                workload_count += int(is_workload)
                if len(combined) >= top_k:
                    break
        program_graph_active = self.program_graph and (
            bool(selected_programs) or self.minimal_join_tree
        )
        # Semantic history/KB nodes are useful only if their physical endpoints
        # survive context compression. Preserve the ranked semantic evidence and
        # append its raw table/column anchors before graph closure.
        anchored = list(combined)
        observed = {row.candidate_id for row in anchored}
        bound_physical_anchors: list[str] = []
        selected_program_by_id = {
            str(program["candidate_id"]): program for program in selected_programs
        }
        binding_rows: list[list[str]] = []
        for row in combined:
            values = list(self.bindings_by_document.get(row.candidate_id, []))
            if not values:
                continue
            program = selected_program_by_id.get(row.candidate_id)
            if program is not None:
                relevant_tables = set(program["relevant_physical_tables"])
                values = [
                    candidate_id
                    for candidate_id in values
                    if candidate_id in self.raw_by_id
                    and self.raw_by_id[candidate_id].table in relevant_tables
                ]
            if values:
                binding_rows.append(values)
        if program_graph_active:
            # Allocate table anchors across all retrieved evidence first, then
            # round-robin columns. This prevents the first long SQL template from
            # consuming the entire physical binding budget.
            ordered_bindings: list[str] = []
            for prefix in ("table::", "column::"):
                offsets = [0 for _ in binding_rows]
                while True:
                    advanced = False
                    for index, values in enumerate(binding_rows):
                        while offsets[index] < len(values):
                            candidate_id = values[offsets[index]]
                            offsets[index] += 1
                            if candidate_id.startswith(prefix):
                                ordered_bindings.append(candidate_id)
                                advanced = True
                                break
                    if not advanced:
                        break
            binding_limit = 20
        else:
            ordered_bindings = [
                candidate_id
                for values in binding_rows
                for candidate_id in values
            ]
            binding_limit = 16
        for candidate_id in ordered_bindings:
            bound = self.raw_by_id.get(candidate_id)
            if (
                bound is None
                or bound.database_id != database_id
                or candidate_id in observed
            ):
                continue
            anchored.append(bound)
            observed.add(candidate_id)
            bound_physical_anchors.append(candidate_id)
            if len(bound_physical_anchors) >= binding_limit:
                break
        role_bindings: dict[str, list[dict[str, Any]]] = {}
        role_evidence_rows: list[CatalogDocument] = []
        role_physical_ids: list[str] = []
        if program_graph_active:
            (
                role_bindings,
                role_evidence_rows,
                role_physical_ids,
            ) = self._query_role_bindings(database_id, query)
            # Role retrieval happens before graph closure so its physical tables
            # participate in path construction rather than appearing as prose
            # after the compiler has already committed to a subgraph.
            for row in role_evidence_rows:
                if row.candidate_id not in observed:
                    anchored.append(row)
                    observed.add(row.candidate_id)
            for candidate_id in role_physical_ids:
                bound = self.raw_by_id.get(candidate_id)
                if bound is None or candidate_id in observed:
                    continue
                anchored.append(bound)
                observed.add(candidate_id)
                if candidate_id not in bound_physical_anchors:
                    bound_physical_anchors.append(candidate_id)
        program_graph: dict[str, Any] | None = None
        if program_graph_active:
            terminal_tables: list[str] = [
                str(self.raw_by_id[candidate_id].table)
                for candidate_id in role_physical_ids
                if candidate_id in self.raw_by_id
                and self.raw_by_id[candidate_id].table
            ]
            for program in selected_programs:
                terminal_tables.extend(
                    str(value) for value in program["relevant_physical_tables"]
                )
            terminal_tables.extend(
                str(row.table)
                for row in combined
                if row.table and _workload_program(row) is None
            )
            if self.minimal_join_tree:
                fallback_tables: list[str] = []
                for program in selected_programs:
                    if (
                        program["question_pattern"]
                        and len(program["topic_overlap"]) >= 2
                        and not fallback_tables
                    ):
                        # A target-disjoint template supplies operator shape, not
                        # a current-question relationship certificate.  Keeping
                        # its old physical chain as a hard terminal allowed a
                        # topically similar history row to override stronger
                        # evolution-lineage role bindings.  Retain it only as a
                        # fallback when role extraction found no structural role.
                        fallback_tables.extend(
                            str(value) for value in program["physical_tables"]
                        )
                    elif (
                        not program["question_pattern"] and not fallback_tables
                    ):
                        fallback_tables.extend(
                            str(value) for value in program["physical_tables"]
                        )
                program_graph = compile_minimal_join_tree(
                    raw_documents=self.raw_by_database[database_id],
                    ontology_edges=self.ontology_edges_by_database.get(
                        database_id, []
                    ),
                    role_bindings=role_bindings,
                    required_tables=[],
                    fallback_tables=fallback_tables,
                )
                closed = list(anchored)
                closed_ids = {row.candidate_id for row in closed}

                def include_physical(candidate_id: str) -> None:
                    row = self.raw_by_id.get(candidate_id)
                    if row is not None and candidate_id not in closed_ids:
                        closed.append(row)
                        closed_ids.add(candidate_id)

                for table in program_graph["topological_table_order"]:
                    include_physical(f"table::{database_id}::{table}")
                for edge in program_graph["ordered_join_edges"]:
                    for table_key, column_key in (
                        ("parent_table", "parent_column"),
                        ("child_table", "child_column"),
                    ):
                        if edge[column_key]:
                            include_physical(
                                f"column::{database_id}::{edge[table_key]}::"
                                f"{edge[column_key]}"
                            )
            else:
                closed, program_graph = relational_program_graph_closure(
                    ranked=anchored,
                    raw_documents=self.raw_by_database[database_id],
                    ontology_edges=self.ontology_edges_by_database.get(
                        database_id, []
                    ),
                    terminal_tables=terminal_tables,
                )
            program_graph.update(
                {
                    "history_template_limit": 8 if self.evidence_first_history else 2,
                    "query_operators": sorted(query_operators),
                    "program_templates": [
                        {
                            key: value
                            for key, value in program.items()
                            if key not in {"question_pattern", "sql_template"}
                        }
                        | {
                            "sql_template_sha256": sha256(
                                str(program["sql_template"]).encode()
                            ).hexdigest(),
                            "sql_template_characters": len(
                                str(program["sql_template"])
                            ),
                        }
                        for program in selected_programs
                    ],
                }
            )
            program_graph["query_role_bindings"] = role_bindings
            bridges = list(program_graph["bridge_tables"])
        else:
            closed, bridges = coherent_table_closure(
                anchored, self.raw_by_database[database_id]
            )
        if program_graph_active:
            selected_program_ids = {
                str(program["candidate_id"]) for program in selected_programs
            }
            role_physical_rows = [
                self.raw_by_id[candidate_id]
                for candidate_id in role_physical_ids
                if candidate_id in self.raw_by_id
            ]
            context_rows: list[CatalogDocument] = []
            context_ids: set[str] = set()
            for row in [
                *(row for row in closed if row.candidate_id in selected_program_ids),
                *role_evidence_rows,
                *role_physical_rows,
                *closed,
            ]:
                if row.candidate_id in context_ids:
                    continue
                context_rows.append(row)
                context_ids.add(row.candidate_id)
                if len(context_rows) >= 36:
                    break
        else:
            context_rows = closed
        response: dict[str, Any] = {"query": query}
        if program_graph is not None:
            # Put the executable graph before the longer evidence list in the
            # serialized prompt so role bindings guide, rather than trail, SQL
            # planning on large schemas.
            response["query_relational_program_graph"] = program_graph
        response.update(
            {
                "results": [
                {
                    "rank": index,
                    "evidence_candidate_id": row.candidate_id,
                    "kind": row.kind,
                    "physical_name": row.name,
                    "physical_table": row.table,
                    "evidence": _semantic_evidence_text(
                        row.text, 5000 if _workload_program(row) is not None else 1200
                    ),
                    **(
                        {
                            "database_profile": self.sidecars[
                                (row.database_id, row.name)
                            ].text[:1200]
                        }
                        if (row.database_id, row.name) in self.sidecars
                        else {}
                    ),
                }
                    for index, row in enumerate(context_rows, start=1)
                ],
                "bridge_tables": bridges,
                "bound_physical_anchors": bound_physical_anchors,
                "evidence_budget": {
                    "workload_sql_templates": workload_count,
                    "workload_template_limit": 2,
                    "ranked_slots": len(combined),
                    "physical_binding_limit": binding_limit,
                },
            }
        )
        return response


@dataclass
class ToolBudget:
    max_actions: int = 8
    max_sql_executions: int = 3
    actions: int = 0
    sql_executions: int = 0

    def charge(self, name: str) -> None:
        if self.actions >= self.max_actions:
            raise RuntimeError("tool action budget exhausted")
        if name == "execute_sql" and self.sql_executions >= self.max_sql_executions:
            raise RuntimeError("SQL execution budget exhausted")
        self.actions += 1
        if name == "execute_sql":
            self.sql_executions += 1


class SQLiteAgentTools:
    def __init__(
        self, database: Path, database_id: str, search_index: SchemaSearchIndex
    ) -> None:
        self.database = database.resolve()
        self.database_id = database_id
        # ``database_id`` is an internal lookup key and is normally safe to show.
        # Specialized catalog adapters may replace the public value when the key
        # itself encodes benchmark-only metadata (for example an evolution type).
        self.public_database_id = database_id
        self.search_index = search_index
        self.targeted_expansion_used = False
        connection = sqlite3.connect(f"file:{self.database}?mode=ro", uri=True)
        try:
            tables = [
                str(row[0])
                for row in connection.execute(
                    "SELECT name FROM sqlite_master "
                    "WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name"
                )
            ]
            self.columns: dict[str, list[tuple[str, str]]] = {}
            self.foreign_keys: dict[str, list[dict[str, Any]]] = {}
            for table in tables:
                self.columns[table] = [
                    (str(row[1]), str(row[2] or ""))
                    for row in connection.execute(
                        f"PRAGMA table_info({_quote(table)})"
                    )
                ]
                self.foreign_keys[table] = [
                    {
                        "from": str(row[3]),
                        "to_table": str(row[2]),
                        "to_column": str(row[4]),
                    }
                    for row in connection.execute(
                        f"PRAGMA foreign_key_list({_quote(table)})"
                    )
                ]
            self.join_edges = self._join_edges()
            # The physical DDL is already visible to every arm. Re-injecting the
            # same FK as an "ontology" edge duplicates rows, fills the top-k join
            # budget, and can hide other usable paths. Ontology contributes only
            # relationship endpoints not already present in the database graph.
            observed_edges = {
                tuple(sorted((str(row["left"]).casefold(), str(row["right"]).casefold())))
                for row in self.join_edges
            }
            for source in search_index.ontology_edges_by_database.get(database_id, []):
                row = dict(source)
                key = tuple(
                    sorted(
                        (
                            str(row["left"]).casefold(),
                            str(row["right"]).casefold(),
                        )
                    )
                )
                if key in observed_edges:
                    continue
                self.join_edges.append(row)
                observed_edges.add(key)
        finally:
            connection.close()

    def _join_edges(self) -> list[dict[str, Any]]:
        edges: list[dict[str, Any]] = []
        observed: set[tuple[str, str, str, str]] = set()
        for table, rows in self.foreign_keys.items():
            for row in rows:
                key = (table, row["from"], row["to_table"], row["to_column"])
                if key in observed:
                    continue
                observed.add(key)
                edges.append(
                    {
                        "left": f"{table}.{row['from']}",
                        "right": f"{row['to_table']}.{row['to_column']}",
                        "evidence": "declared_foreign_key",
                        "score": 1.0,
                    }
                )
        tables = sorted(self.columns)
        for left_index, left_table in enumerate(tables):
            for right_table in tables[left_index + 1 :]:
                left_columns = {name.casefold(): name for name, _ in self.columns[left_table]}
                right_columns = {name.casefold(): name for name, _ in self.columns[right_table]}
                for normalized in sorted(set(left_columns) & set(right_columns)):
                    if normalized in {"name", "date", "time", "type", "value"}:
                        continue
                    key = (
                        left_table,
                        left_columns[normalized],
                        right_table,
                        right_columns[normalized],
                    )
                    if key in observed:
                        continue
                    observed.add(key)
                    edges.append(
                        {
                            "left": f"{left_table}.{left_columns[normalized]}",
                            "right": f"{right_table}.{right_columns[normalized]}",
                            "evidence": "same_physical_column_name",
                            "score": 0.7,
                        }
                    )
        return edges

    def inventory_text(self) -> str:
        lines = []
        for table in sorted(self.columns):
            columns = ", ".join(
                f"{name}:{kind or 'unknown'}" for name, kind in self.columns[table]
            )
            links = ", ".join(
                f"{row['from']}->{row['to_table']}.{row['to_column']}"
                for row in self.foreign_keys[table]
            )
            suffix = f" | FK {links}" if links else ""
            lines.append(f"{table}({columns}){suffix}")
        return "\n".join(lines)

    def _public_search_payload(self, value: Any) -> Any:
        """Hide an internal catalog key from model-visible search payloads."""

        if self.public_database_id == self.database_id:
            return value
        if isinstance(value, dict):
            return {
                key: self._public_search_payload(item)
                for key, item in value.items()
            }
        if isinstance(value, list):
            return [self._public_search_payload(item) for item in value]
        if isinstance(value, tuple):
            return tuple(self._public_search_payload(item) for item in value)
        if isinstance(value, str):
            return value.replace(self.database_id, self.public_database_id)
        return value

    def search_schema(
        self,
        query: str,
        top_k: int,
        *,
        enable_reranker: bool = True,
    ) -> dict[str, Any]:
        return self._public_search_payload(
            self.search_index.search(
                self.database_id,
                query,
                top_k,
                enable_reranker=enable_reranker,
            )
        )

    def targeted_expand_schema(
        self, queries: list[str], top_k_per_query: int
    ) -> dict[str, Any]:
        """Run one bounded multi-probe expansion over this arm's existing index."""

        if self.targeted_expansion_used:
            raise RuntimeError("targeted schema expansion is limited to one call")
        cleaned = list(
            dict.fromkeys(
                str(query).strip()
                for query in queries[:3]
                if str(query).strip()
            )
        )
        if not cleaned:
            raise ValueError("targeted expansion requires at least one query")
        self.targeted_expansion_used = True
        per_query = max(1, min(int(top_k_per_query), 10))
        merged: list[dict[str, Any]] = []
        observed: set[tuple[str, str, str]] = set()
        bridges: list[str] = []
        anchors: list[str] = []
        for query in cleaned:
            result = self.search_index.search(self.database_id, query, per_query)
            bridges.extend(str(value) for value in result.get("bridge_tables") or [])
            anchors.extend(
                str(value) for value in result.get("bound_physical_anchors") or []
            )
            for row in result.get("results") or []:
                key = (
                    str(row.get("kind") or ""),
                    str(row.get("physical_table") or ""),
                    str(row.get("physical_name") or ""),
                )
                if key in observed:
                    continue
                observed.add(key)
                merged.append({"probe": query, **dict(row)})
        return self._public_search_payload({
            "queries": cleaned,
            "results": merged[:24],
            "bridge_tables": list(dict.fromkeys(bridges))[:12],
            "bound_physical_anchors": list(dict.fromkeys(anchors))[:16],
            "expansion_calls_remaining": 0,
            "evidence_boundary": "raw physical schema index only",
        })

    def search_joins(self, tables: list[str], max_edges: int) -> dict[str, Any]:
        requested = {str(value).casefold() for value in tables}
        matched = [
            row
            for row in self.join_edges
            if not requested
            or row["left"].split(".", 1)[0].casefold() in requested
            or row["right"].split(".", 1)[0].casefold() in requested
        ]
        matched.sort(key=lambda row: (-float(row["score"]), row["left"], row["right"]))
        return {"join_edges": matched[: max(1, min(int(max_edges), 30))]}

    @staticmethod
    def _literal_variants(value: str) -> list[str]:
        output = [value.strip()]
        date = re.fullmatch(r"(\d{4})[/-](\d{1,2})[/-](\d{1,2})", value.strip())
        if date:
            year, month, day = date.groups()
            output.extend(
                [
                    f"{year}-{int(month):02d}-{int(day):02d}",
                    f"{year}/{int(month)}/{int(day)}",
                ]
            )
        return list(dict.fromkeys(item for item in output if item))

    def search_values(
        self, literals: list[str], max_matches: int
    ) -> dict[str, Any]:
        limit = max(1, min(int(max_matches), 30))
        variants: dict[str, list[str]] = {}
        variant_owner: dict[str, str] = {}
        for literal in literals[:12]:
            literal = str(literal)
            variants[literal] = self._literal_variants(literal)
            for value in variants[literal]:
                variant_owner.setdefault(value.casefold(), literal)
        flat_values = list(dict.fromkeys(value for rows in variants.values() for value in rows))
        if not flat_values:
            return {"matches": [], "truncated": False}
        matches: list[dict[str, Any]] = []
        connection = sqlite3.connect(f"file:{self.database}?mode=ro", uri=True)
        connection.execute("PRAGMA query_only=ON")
        deadline = time.monotonic() + 10.0
        connection.set_progress_handler(
            lambda: int(time.monotonic() > deadline), 10_000
        )
        try:
            placeholders = ",".join("?" for _ in flat_values)
            for table in sorted(self.columns):
                for column, _ in self.columns[table]:
                    # One indexed-compatible exact probe per physical column.  The
                    # former literal-by-column CAST scan multiplied I/O by the
                    # number of literals and defeated ordinary SQLite indexes.
                    sql = (
                        f"SELECT {_quote(column)}, COUNT(*) FROM {_quote(table)} "
                        f"WHERE {_quote(column)} IN ({placeholders}) "
                        f"GROUP BY {_quote(column)} LIMIT {limit}"
                    )
                    try:
                        rows = connection.execute(sql, tuple(flat_values)).fetchall()
                    except sqlite3.OperationalError:
                        continue
                    for value, count in rows:
                        rendered = str(value)
                        literal = variant_owner.get(rendered.casefold())
                        if literal is None:
                            # Numeric affinity can canonicalize 12.50 to 12.5.
                            literal = next(
                                (
                                    owner
                                    for variant, owner in variant_owner.items()
                                    if _numeric_equal(rendered, variant)
                                ),
                                rendered,
                            )
                        matches.append(
                            {
                                "literal": literal,
                                "physical_column": f"{table}.{column}",
                                "matched_value": _safe_value(value),
                                "row_count": int(count),
                                "evidence": "exact_database_value",
                            }
                        )
                        if len(matches) >= limit:
                            return {"matches": matches, "truncated": True}
        finally:
            connection.close()
        return {"matches": matches, "truncated": False}

    def inspect_schema(self, tables: list[str]) -> dict[str, Any]:
        selected = []
        for value in tables[:6]:
            match = next(
                (table for table in self.columns if table.casefold() == str(value).casefold()),
                None,
            )
            if match and match not in selected:
                selected.append(match)
        connection = sqlite3.connect(f"file:{self.database}?mode=ro", uri=True)
        try:
            output = []
            for table in selected:
                row = connection.execute(
                    "SELECT sql FROM sqlite_master WHERE type='table' AND name=?",
                    (table,),
                ).fetchone()
                output.append(
                    {
                        "table": table,
                        "ddl": str(row[0]) if row and row[0] else "",
                        "foreign_keys": self.foreign_keys[table],
                    }
                )
            return {"tables": output, "unknown_tables": len(tables) - len(selected)}
        finally:
            connection.close()

    def sample_values(
        self, table: str, column: str, limit: int, contains: str | None
    ) -> dict[str, Any]:
        physical_table = next(
            (name for name in self.columns if name.casefold() == table.casefold()), None
        )
        if physical_table is None:
            raise ValueError(f"unknown table: {table}")
        physical_column = next(
            (
                name
                for name, _ in self.columns[physical_table]
                if name.casefold() == column.casefold()
            ),
            None,
        )
        if physical_column is None:
            raise ValueError(f"unknown column: {physical_table}.{column}")
        limit = max(1, min(int(limit), 20))
        where = f"WHERE {_quote(physical_column)} IS NOT NULL"
        parameters: tuple[Any, ...] = ()
        if contains:
            where += f" AND CAST({_quote(physical_column)} AS TEXT) LIKE ?"
            parameters = (f"%{contains}%",)
        sql = (
            f"SELECT {_quote(physical_column)}, COUNT(*) AS frequency "
            f"FROM {_quote(physical_table)} {where} "
            f"GROUP BY {_quote(physical_column)} ORDER BY frequency DESC LIMIT {limit}"
        )
        connection = sqlite3.connect(f"file:{self.database}?mode=ro", uri=True)
        try:
            rows = connection.execute(sql, parameters).fetchall()
        finally:
            connection.close()
        return {
            "table": physical_table,
            "column": physical_column,
            "contains": contains,
            "values": [[_safe_value(value) for value in row] for row in rows],
        }

    def execute_sql(self, sql: str, limit: int = 20) -> dict[str, Any]:
        if not sql.strip():
            raise ValueError("SQL must not be empty")
        connection = sqlite3.connect(f"file:{self.database}?mode=ro", uri=True)
        connection.execute("PRAGMA query_only=ON")
        allowed = {
            sqlite3.SQLITE_SELECT,
            sqlite3.SQLITE_READ,
            sqlite3.SQLITE_FUNCTION,
            sqlite3.SQLITE_RECURSIVE,
        }
        connection.set_authorizer(
            lambda action, *_: (
                sqlite3.SQLITE_OK if action in allowed else sqlite3.SQLITE_DENY
            )
        )
        deadline = time.monotonic() + 8.0
        connection.set_progress_handler(
            lambda: int(time.monotonic() > deadline), 10_000
        )
        try:
            cursor = connection.execute(sql)
            rows = cursor.fetchmany(max(1, min(limit, 20)) + 1)
            return {
                "executable": True,
                "columns": [str(value[0]) for value in cursor.description or []],
                "rows": [
                    [_safe_value(value) for value in row]
                    for row in rows[: max(1, min(limit, 20))]
                ],
                "truncated": len(rows) > limit,
            }
        except Exception as error:
            return {
                "executable": False,
                "error_type": type(error).__name__,
                "error": str(error)[:800],
            }
        finally:
            connection.close()


def react_tools(
    condition: str = "raw_react", *, dialect: str = "SQLite"
) -> list[dict[str, Any]]:
    tools = [
        {
            "type": "function",
            "function": {
                "name": "search_schema",
                "description": "Search physical schema or recovered semantic nodes and FK bridges.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {"type": "string"},
                        "top_k": {"type": "integer", "minimum": 1, "maximum": 20},
                    },
                    "required": ["query", "top_k"],
                    "additionalProperties": False,
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "inspect_schema",
                "description": f"Return authoritative {dialect} DDL and relationship columns for tables.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "tables": {
                            "type": "array",
                            "items": {"type": "string"},
                            "minItems": 1,
                            "maxItems": 6,
                        }
                    },
                    "required": ["tables"],
                    "additionalProperties": False,
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "sample_values",
                "description": "Inspect frequent or substring-matching values of one physical column.",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "table": {"type": "string"},
                        "column": {"type": "string"},
                        "limit": {"type": "integer", "minimum": 1, "maximum": 20},
                        "contains": {"type": ["string", "null"]},
                    },
                    "required": ["table", "column", "limit", "contains"],
                    "additionalProperties": False,
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "execute_sql",
                "description": "Execute one read-only candidate query and inspect up to 20 result rows.",
                "parameters": {
                    "type": "object",
                    "properties": {"sql": {"type": "string"}},
                    "required": ["sql"],
                    "additionalProperties": False,
                },
            },
        },
        {
            "type": "function",
            "function": {
                "name": "submit_sql",
                "description": (
                    f"Submit the final read-only {dialect} query. Revise the SQL first if "
                    "the latest query_contract_check reported any violation."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {"sql": {"type": "string"}},
                    "required": ["sql"],
                    "additionalProperties": False,
                },
            },
        },
    ]
    if condition in {
        "grounded_react",
        "opaque_react",
        "recovery_only_react",
        "ontology_react",
        "program_graph_react",
        "minimal_join_tree_react",
        "chess_react",
        "autolink_react",
        "evoschema_raw_react",
        "evoschema_flat_react",
        "evoschema_full_react",
        "evoschema_program_graph_react",
        "evoschema_minimal_join_tree_react",
    }:
        tools[1:1] = [
            {
                "type": "function",
                "function": {
                    "name": "search_values",
                    "description": "Search every physical column for exact database values matching question literals.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "literals": {
                                "type": "array",
                                "items": {"type": "string"},
                                "minItems": 1,
                                "maxItems": 12,
                            },
                            "max_matches": {"type": "integer", "minimum": 1, "maximum": 30},
                        },
                        "required": ["literals", "max_matches"],
                        "additionalProperties": False,
                    },
                },
            },
            {
                "type": "function",
                "function": {
                    "name": "search_joins",
                    "description": "Return declared FK and deterministic compatible-column join edges.",
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "tables": {
                                "type": "array",
                                "items": {"type": "string"},
                                "maxItems": 8,
                            },
                            "max_edges": {"type": "integer", "minimum": 1, "maximum": 30},
                        },
                        "required": ["tables", "max_edges"],
                        "additionalProperties": False,
                    },
                },
            },
        ]
    if condition == "autolink_react":
        tools[1:1] = [
            {
                "type": "function",
                "function": {
                    "name": "targeted_expand_schema",
                    "description": (
                        "Run the single allowed AutoLink-style multi-probe expansion "
                        "over the raw physical schema index for unresolved query roles."
                    ),
                    "parameters": {
                        "type": "object",
                        "properties": {
                            "queries": {
                                "type": "array",
                                "items": {"type": "string"},
                                "minItems": 1,
                                "maxItems": 3,
                            },
                            "top_k_per_query": {
                                "type": "integer",
                                "minimum": 1,
                                "maximum": 10,
                            },
                        },
                        "required": ["queries", "top_k_per_query"],
                        "additionalProperties": False,
                    },
                },
            }
        ]
    return tools


def _dispatch(
    name: str,
    arguments: dict[str, Any],
    tools: SQLiteAgentTools,
) -> dict[str, Any]:
    if name == "search_schema":
        return tools.search_schema(str(arguments["query"]), int(arguments["top_k"]))
    if name == "targeted_expand_schema":
        return tools.targeted_expand_schema(
            [str(value) for value in arguments["queries"]],
            int(arguments["top_k_per_query"]),
        )
    if name == "search_values":
        return tools.search_values(
            [str(value) for value in arguments["literals"]],
            int(arguments["max_matches"]),
        )
    if name == "search_joins":
        return tools.search_joins(
            [str(value) for value in arguments["tables"]],
            int(arguments["max_edges"]),
        )
    if name == "inspect_schema":
        return tools.inspect_schema([str(value) for value in arguments["tables"]])
    if name == "sample_values":
        contains = arguments.get("contains")
        return tools.sample_values(
            str(arguments["table"]),
            str(arguments["column"]),
            int(arguments["limit"]),
            str(contains) if contains is not None else None,
        )
    if name == "execute_sql":
        return tools.execute_sql(str(arguments["sql"]))
    if name == "submit_sql":
        return {"submitted": True}
    raise ValueError(f"unknown tool: {name}")


def _semantic_evidence_text(text: str, character_limit: int) -> str:
    """Keep an SQL-derived computation contract atomic through both planners.

    Versioned contracts already materialize their dependency closure and compact
    provenance at construction. Slicing them would lose filters/roles or make
    the Graph/Evo compiler silently ignore invalid JSON. Legacy evidence keeps
    its existing behavior, so in-flight experiments retain their original path.
    """
    try:
        payload = json.loads(text)
    except (ValueError, TypeError):
        return text[:character_limit]
    if isinstance(payload, dict) and payload.get("ontology_kind") == "sql_workload_semantic_object" and payload.get("consumer_contract_version") == 1:
        return json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    return text[:character_limit]


def _bounded_tool_observation(
    observation: dict[str, Any], *, character_limit: int
) -> str:
    """Serialize a tool result as valid JSON within a deterministic bound.

    Direct string slicing can leave malformed JSON and repeated 16k observations
    can overflow otherwise valid 49k-token ReACT requests.  The compact envelope
    keeps a verifiable prefix and the full-result hash while remaining parseable.
    """

    if character_limit < 512:
        raise ValueError("tool observation character limit must be at least 512")
    serialized = json.dumps(observation, ensure_ascii=False, sort_keys=True)
    if len(serialized) <= character_limit:
        return serialized
    digest = sha256(serialized.encode("utf-8")).hexdigest()
    prefix_length = max(0, character_limit - 256)
    while True:
        compact = json.dumps(
            {
                "truncated": True,
                "original_characters": len(serialized),
                "sha256": digest,
                "json_prefix": serialized[:prefix_length],
            },
            ensure_ascii=False,
            sort_keys=True,
        )
        if len(compact) <= character_limit:
            return compact
        overflow = len(compact) - character_limit
        prefix_length = max(0, prefix_length - max(overflow, 1))


def run_react_text2sql(
    *,
    condition: str,
    row: dict[str, Any],
    client: VLLMClient,
    database: Path,
    search_index: SchemaSearchIndex,
    max_turns: int = 4,
    max_actions: int = 8,
    max_sql_executions: int = 3,
    initial_schema_top_k: int = 12,
    tools_factory: Callable[
        [Path, str, SchemaSearchIndex], SQLiteAgentTools
    ] | None = None,
    sql_dialect: str = "SQLite",
    method_id_override: str | None = None,
    anchor_sql: str | None = None,
    auxiliary_raw_sql: str | None = None,
    inject_graph_evo_context: bool = False,
    realize_submitted_program: bool = False,
    fixed_sql_consumer: bool = False,
    performance_first_raw_backbone: bool = False,
    evolution_mapping: RelationEvolutionMapping | None = None,
    evidence_first_history: bool = False,
    realize_semantic_revision: bool = False,
    scope_grounded_revision: bool = False,
    witness_consistent_revision: bool = False,
    grounded_binding_revision: bool = False,
    realized_edit_revision: bool = False,
    physical_execution_python: str | None = None,
    scope_faithful_revision: bool = False,
    relational_grain_revision: bool = False,
    entity_grain_revision: bool = False,
    semantic_memory: dict[str, Any] | None = None,
    retrieval_snapshot: dict[str, Any] | None = None,
) -> dict[str, Any]:
    if semantic_memory is not None:
        from copy import deepcopy
        from finsemguard.e2e.semantic_scope_contract import CONTRACT_PROMPT, validate_contract
        semantic_memory = deepcopy(semantic_memory)
        if not semantic_memory.get("ontology_revision"):
            raise ValueError("semantic_memory requires a fixed ontology revision")
    if entity_grain_revision and not relational_grain_revision:
        raise ValueError("Entity grain realization requires relational grain evidence")
    if relational_grain_revision and not scope_faithful_revision:
        raise ValueError("Relational grain revision requires the scope-faithful physical observer")
    if scope_faithful_revision and (not grounded_binding_revision or not physical_execution_python or realized_edit_revision):
        raise ValueError("Scope-faithful revision requires physical grounded observations and complete SQL, not edits")
    if realized_edit_revision and (not grounded_binding_revision or not physical_execution_python):
        raise ValueError("realized edits require grounded binding and explicit physical execution Python")
    if grounded_binding_revision and not witness_consistent_revision:
        raise ValueError("grounded binding revision requires witness-consistent revision")
    if witness_consistent_revision and not scope_grounded_revision:
        raise ValueError("witness-consistent revision requires scope-grounded revision")
    if scope_grounded_revision and not realize_semantic_revision:
        raise ValueError("scope-grounded revision requires semantic revision")
    if realize_semantic_revision and not evidence_first_history:
        raise ValueError("semantic revision requires evidence-first history")
    if condition not in METHOD_IDS:
        raise ValueError(f"unsupported ReAct condition: {condition}")
    if max_turns < 2:
        raise ValueError("max_turns must be at least two")
    if not 1 <= initial_schema_top_k <= 20:
        raise ValueError("initial_schema_top_k must be between 1 and 20")
    if method_id_override is not None and not method_id_override.strip():
        raise ValueError("method_id_override must be non-empty")
    if anchor_sql is not None and condition not in {
        "program_graph_react",
        "minimal_join_tree_react",
        "evoschema_program_graph_react",
        "evoschema_minimal_join_tree_react",
    }:
        raise ValueError("base solution anchors require a relational-program condition")
    if inject_graph_evo_context and condition not in PROGRAM_GRAPH_CONDITIONS:
        raise ValueError("Graph+Evo context requires a relational-program condition")
    if auxiliary_raw_sql is not None and (
        anchor_sql is None or not inject_graph_evo_context
    ):
        raise ValueError(
            "an auxiliary raw draft requires an anchored Graph+Evo condition"
        )
    if realize_submitted_program and (
        not inject_graph_evo_context or anchor_sql is None
    ):
        raise ValueError(
            "submitted-program realization requires an anchored Graph+Evo condition"
        )
    if fixed_sql_consumer and not realize_submitted_program:
        raise ValueError(
            "the fixed SQL consumer requires submitted-program realization"
        )
    if performance_first_raw_backbone and (
        not fixed_sql_consumer
        or anchor_sql is None
        or auxiliary_raw_sql is None
        or not str(auxiliary_raw_sql).strip()
    ):
        raise ValueError(
            "performance-first raw backbone requires recovered and raw drafts "
            "inside the fixed unified consumer"
        )
    if retrieval_snapshot is not None:
        from finsemguard.e2e.retrieval_snapshot import validate_snapshot
        retrieval_snapshot = validate_snapshot(retrieval_snapshot, row, anchor_sql, auxiliary_raw_sql)
    recovered_draft_sql = anchor_sql
    direct_raw_draft_sql = auxiliary_raw_sql
    schema_context_key = schema_key(row)
    opaque_column_ratio = _opaque_physical_column_ratio(
        list(search_index.raw_by_database.get(schema_context_key) or [])
    )
    raw_backbone_active = bool(
        performance_first_raw_backbone
        and evolution_mapping is None
        and opaque_column_ratio < 0.5
    )
    dual_evidence_priority = (
        {
            "selected_backbone": (
                "direct_raw" if raw_backbone_active else "persistent_recovery"
            ),
            "reason": (
                "descriptive_current_identifiers"
                if raw_backbone_active
                else "evolution_lineage_present"
                if evolution_mapping is not None
                else "opaque_current_identifiers"
            ),
            "opaque_physical_column_ratio": round(opaque_column_ratio, 6),
            "uses_scores_or_expected_answers": False,
        }
        if performance_first_raw_backbone
        else None
    )
    persistent_recovery_advisory_sql: str | None = None
    if raw_backbone_active:
        persistent_recovery_advisory_sql = anchor_sql
        anchor_sql = auxiliary_raw_sql
        auxiliary_raw_sql = None
    performance_first_raw_backbone = raw_backbone_active
    started = time.perf_counter()
    db_tools = (
        tools_factory(database, schema_key(row), search_index)
        if tools_factory is not None
        else SQLiteAgentTools(database, schema_key(row), search_index)
    )
    source_question = str(row.get("source_question") or row["question"])
    benchmark_evidence = str(row.get("benchmark_evidence") or "")
    search_query = source_question
    if condition in PROGRAM_GRAPH_CONDITIONS and benchmark_evidence:
        search_query = (
            f"{source_question}\nBenchmark knowledge evidence: {benchmark_evidence}"
        )
    # The cross-encoder ranks recovered semantic evidence.  In raw-backbone
    # mode the complete Direct Raw AST already rests on descriptive current
    # identifiers; reranking the mixed raw/history pack can perturb a valid
    # operator structure without adding a recovery signal.  Preserve that
    # evidence order while continuing to compile the same Graph+Evo program.
    initial = retrieval_snapshot["initial_search"] if retrieval_snapshot is not None else db_tools.search_schema(
        search_query,
        initial_schema_top_k,
        enable_reranker=evidence_first_history or not raw_backbone_active,
    )
    if retrieval_snapshot is not None and retrieval_snapshot["initial_search_query"] != search_query:
        raise ValueError("retrieval cache query changed")
    program_graph_condition = condition in PROGRAM_GRAPH_CONDITIONS
    if program_graph_condition and hasattr(db_tools, "join_edges"):
        # The relational-program graph deliberately excludes profile/name/value
        # coincidences as join evidence.  Do the same for later tool calls; the
        # previous prefetch leaked dozens of WAREHOUSE_LOAD_DATE-style overlaps
        # back into the prompt, diluting the graph and overflowing long BEAVER
        # contexts despite the compiler itself having selected trusted paths.
        db_tools.join_edges = [
            edge
            for edge in db_tools.join_edges
            if _trusted_relationship_edge(edge)
        ]
    literal_candidates = question_literal_candidates(
        source_question, benchmark_evidence
    )
    grounding_enabled = condition in {
        "grounded_react",
        "opaque_react",
        "recovery_only_react",
        "ontology_react",
        "program_graph_react",
        "minimal_join_tree_react",
        "chess_react",
        "autolink_react",
        "evoschema_raw_react",
        "evoschema_flat_react",
        "evoschema_full_react",
        "evoschema_program_graph_react",
        "evoschema_minimal_join_tree_react",
    }
    exact_value_matches = (
        (retrieval_snapshot["exact_value_matches"] if retrieval_snapshot is not None else db_tools.search_values(literal_candidates, 30))
        if grounding_enabled
        else None
    )
    graph_evo_context_payload: dict[str, Any] | None = None
    graph_evo_context_sha256: str | None = None
    current_relational_program_payload: dict[str, Any] | None = None
    target_isolated_demonstrations: list[dict[str, Any]] = []
    compact_relational_program_payload: dict[str, Any] | None = None
    historical_support_inventory: list[dict[str, Any]] = []
    if inject_graph_evo_context:
        if not initial.get("query_relational_program_graph"):
            raise RuntimeError("unified main is missing its query-conditioned graph")
        context_key = schema_key(row)
        recompiled_graph = initial["query_relational_program_graph"] if retrieval_snapshot is not None else recompile_graph_evo_query_graph(
            initial,
            raw_documents=list(
                search_index.raw_by_database.get(context_key) or []
            ),
            ontology_edges=list(
                search_index.ontology_edges_by_database.get(context_key) or []
            ),
            anchor_sql=anchor_sql,
            exact_value_matches=exact_value_matches,
            dialect=sql_dialect,
        )
        initial = {
            **initial,
            "query_relational_program_graph": recompiled_graph,
        }
        compiled_graph_evo_context = compile_graph_evo_program_context(initial)
        graph_evo_context_payload = compiled_graph_evo_context.to_prompt_payload()
        graph_evo_context_sha256 = compiled_graph_evo_context.context_sha256
        assert anchor_sql is not None
        current_relational_program_payload = (
            compile_role_first_relational_program(
                graph_evo_context=graph_evo_context_payload,
                anchor_sql=anchor_sql,
                dialect=sql_dialect,
            ).to_prompt_payload()
        )
        historical_support_inventory = _target_isolated_history_inventory(
            list(search_index.by_database.get(context_key) or []),
            target_question=source_question,
        )
        # Generic few-shot rendering was tested and rejected: even a highly
        # similar support query encouraged the generator to simplify a correct
        # evidence-bound CTE/HAVING program.  Historical SQL is therefore used
        # only through exact draft/program concordance below.
        target_isolated_demonstrations = []
        compact_relational_program_payload = _compact_planner_program(
            graph_evo_context=graph_evo_context_payload,
            current_relational_program=current_relational_program_payload,
            demonstrations=target_isolated_demonstrations,
        )
    query_relationship_edges = list(
        (
            initial.get("query_relational_program_graph", {}).get(
                "physical_join_edges"
            )
            or initial.get("query_relational_program_graph", {}).get(
                "ordered_join_edges"
            )
            or []
        )
    )
    if not query_relationship_edges and tools_factory is not None:
        # Some legacy indices predate the per-query relation graph.  Retain the
        # filtered backend inventory as an explicit compatibility source; new
        # program-graph runs certify against the query-specific tree above.
        query_relationship_edges = list(getattr(db_tools, "join_edges", []))
    query_contract = compile_query_contract(source_question, conservative=realize_semantic_revision)
    base_solution_anchor = (
        anchor_relation_contract(anchor_sql, dialect=sql_dialect)
        if anchor_sql is not None
        else None
    )
    auxiliary_raw_evidence_draft = (
        anchor_relation_contract(auxiliary_raw_sql, dialect=sql_dialect)
        if auxiliary_raw_sql is not None
        else None
    )
    persistent_recovery_advisory_draft = (
        anchor_relation_contract(
            persistent_recovery_advisory_sql,
            dialect=sql_dialect,
        )
        if persistent_recovery_advisory_sql is not None
        else None
    )
    draft_evidence_support: dict[str, Any] | None = None
    evidence_bound_program_prior: dict[str, Any] | None = None
    if graph_evo_context_payload is not None and base_solution_anchor is not None:
        historical_programs = historical_support_inventory
        draft_evidence_support = {
            "base_solution_anchor": _draft_historical_support(
                draft_sql=str(anchor_sql or ""),
                question=source_question,
                historical_programs=historical_programs,
                dialect=sql_dialect,
            ),
            "auxiliary_raw_evidence_draft": (
                _draft_historical_support(
                    draft_sql=str(auxiliary_raw_sql or ""),
                    question=source_question,
                    historical_programs=historical_programs,
                    dialect=sql_dialect,
                )
                if auxiliary_raw_evidence_draft is not None
                else None
            ),
            "persistent_recovery_advisory_draft": (
                _draft_historical_support(
                    draft_sql=str(persistent_recovery_advisory_sql or ""),
                    question=source_question,
                    historical_programs=historical_programs,
                    dialect=sql_dialect,
                )
                if persistent_recovery_advisory_draft is not None
                else None
            ),
            "history_inventory": {
                "database_local_target_disjoint_programs": len(
                    historical_programs
                ),
                "provenance_sha256": sha256(
                    json.dumps(
                        [
                            {
                                "provenance_id": program.get("provenance_id"),
                                "sql_sha256": sha256(
                                    str(program.get("sql_template") or "").encode()
                                ).hexdigest(),
                            }
                            for program in historical_programs
                        ],
                        ensure_ascii=False,
                        sort_keys=True,
                        separators=(",", ":"),
                    ).encode()
                ).hexdigest(),
                "rendered_as_generic_demonstrations": False,
                "uses_evaluator_gold": False,
            },
            "provenance_only": True,
            "uses_evaluator_gold": False,
        }
        if performance_first_raw_backbone:
            evidence_bound_program_prior = _evidence_bound_program_prior(
                base_contract=persistent_recovery_advisory_draft,
                base_support=draft_evidence_support[
                    "persistent_recovery_advisory_draft"
                ],
                auxiliary_contract=base_solution_anchor,
                auxiliary_support=draft_evidence_support["base_solution_anchor"],
            )
        else:
            evidence_bound_program_prior = _evidence_bound_program_prior(
                base_contract=base_solution_anchor,
                base_support=draft_evidence_support["base_solution_anchor"],
                auxiliary_contract=auxiliary_raw_evidence_draft,
                auxiliary_support=draft_evidence_support[
                    "auxiliary_raw_evidence_draft"
                ],
            )
    if (
        anchor_sql is not None
        and base_solution_anchor is not None
        and not base_solution_anchor["replaceable_scope"]
        and not realize_submitted_program
    ):
        relation_composition = compile_relational_program(
            anchor_sql=anchor_sql,
            question=source_question,
            database=database,
            database_id=str(row["database_id"]),
            dialect=sql_dialect,
            relationship_edges=(query_relationship_edges or None),
            evolution_mapping=evolution_mapping,
            graph_evo_context=graph_evo_context_payload,
        )
        final_sql = str(relation_composition.pop("sql"))
        if tools_factory is None:
            probe = execution_probe(database, final_sql, timeout_seconds=8.0)
        else:
            adapted_probe = db_tools.execute_sql(final_sql, limit=1)
            probe = {
                "executable": bool(adapted_probe.get("executable")),
                "validation": {
                    "valid": bool(final_sql.strip()),
                    "adapter_validated_current_schema": True,
                },
                **(
                    {
                        "error_type": adapted_probe.get("error_type"),
                        "error": adapted_probe.get("error"),
                    }
                    if not adapted_probe.get("executable")
                    else {}
                ),
                "schema_view": adapted_probe.get("schema_view"),
                "storage_adapter": adapted_probe.get("storage_adapter"),
            }
        return {
            "example_id": row["example_id"],
            "dataset_id": row["dataset_id"],
            "upstream_split": row["upstream_split"],
            "database_id": row["database_id"],
            "method_id": method_id_override or METHOD_IDS[condition],
            "asset_condition": condition,
            "paper_baseline_adapter": None,
            "decision": "answer",
            "sql": final_sql,
            "execution_probe": probe,
            "react": {
                "turns": 0,
                "tool_actions": 0,
                "sql_executions": 0,
                "trajectory": [],
                "initial_search": initial,
                "initial_search_query": search_query,
                "graph_evo_program_context": graph_evo_context_payload,
                "query_contract": query_contract,
                "prefetched_grounding": None,
                "compiled_semantic_plan": None,
                "candidate_selection": None,
                "base_solution_anchor": base_solution_anchor,
                "raw_react_sql": anchor_sql,
                "relation_composition": relation_composition,
                "identity_short_circuit": (
                    "unsupported_relation_ast_entire_anchor_frozen"
                ),
            },
            "audit": {
                "usage": [],
                "known_total_tokens": 0,
                "model_calls": 0,
                "planner_prompt_sha256": None,
                "planner_retry_prompt_sha256": None,
                "prompt_sha256": None,
                "graph_evo_context_sha256": graph_evo_context_sha256,
            },
            "latency_seconds": round(time.perf_counter() - started, 6),
        }
    prefetched_grounding: dict[str, Any] | None = None
    if grounding_enabled:
        seed_tables = list(
            dict.fromkeys(
                str(result["physical_table"])
                for result in initial["results"]
                if result.get("physical_table")
            )
        )
        compiled_join_edges = (
            initial.get("query_relational_program_graph", {}).get(
                "physical_join_edges"
            )
            or []
        )
        prefetched_grounding = {
            "literal_candidates": literal_candidates,
            "exact_value_matches": exact_value_matches,
            "join_graph": (
                {
                    "join_edges": compiled_join_edges,
                    "source": "query_conditioned_relational_program_graph",
                }
                if program_graph_condition and compiled_join_edges
                else db_tools.search_joins(seed_tables, 24)
            ),
            "provenance": (
                "deterministic read-only database probes; no model-authored claims"
            ),
        }
    addition = {
        "raw_react": "",
        "recovered_react": RECOVERY_PROMPT,
        "grounded_react": GROUNDED_PROMPT,
        "opaque_react": OPAQUE_PROMPT,
        # Keep the controller prompt identical to the full treatment so this arm
        # removes only the extra ontology-edge injection from the search index.
        "recovery_only_react": ONTOLOGY_PROMPT,
        "ontology_react": ONTOLOGY_PROMPT,
        "program_graph_react": ONTOLOGY_PROMPT + "\n\n" + PROGRAM_GRAPH_PROMPT,
        "minimal_join_tree_react": (
            ONTOLOGY_PROMPT
            + "\n\n"
            + PROGRAM_GRAPH_PROMPT
            + "\n\n"
            + MINIMAL_JOIN_TREE_PROMPT
        ),
        "chess_react": CHESS_PROMPT,
        "autolink_react": AUTOLINK_PROMPT,
        "evoschema_raw_react": EVOSCHEMA_RAW_PROMPT,
        # Token-matched A6-flat control: the caller removes graph bindings, but
        # the controller and prompt remain identical to the full method.
        "evoschema_flat_react": EVOSCHEMA_FULL_PROMPT,
        "evoschema_full_react": EVOSCHEMA_FULL_PROMPT,
        "evoschema_program_graph_react": (
            EVOSCHEMA_FULL_PROMPT
            + "\n\n"
            + ONTOLOGY_PROMPT
            + "\n\n"
            + PROGRAM_GRAPH_PROMPT
        ),
        "evoschema_minimal_join_tree_react": (
            EVOSCHEMA_FULL_PROMPT
            + "\n\n"
            + ONTOLOGY_PROMPT
            + "\n\n"
            + PROGRAM_GRAPH_PROMPT
            + "\n\n"
            + MINIMAL_JOIN_TREE_PROMPT
        ),
    }[condition]
    graph_templates = (
        initial.get("query_relational_program_graph", {}).get("program_templates")
        or []
    )
    if condition == "program_graph_react" and not graph_templates:
        addition = ONTOLOGY_PROMPT
    elif condition == "evoschema_program_graph_react" and not graph_templates:
        addition = EVOSCHEMA_FULL_PROMPT
    if base_solution_anchor is not None:
        addition = addition + "\n\n" + (
            RAW_BACKBONE_RELATION_PROGRAM_PROMPT
            if performance_first_raw_backbone
            else ANCHORED_RELATION_PROGRAM_PROMPT
        )
    base_system = (
        SYSTEM_PROMPT
        if sql_dialect.casefold() == "sqlite"
        else SYSTEM_PROMPT.replace("SQLite", sql_dialect)
    )
    system = base_system + ("\n\n" + addition if addition else "")
    compiled_semantic_plan: dict[str, Any] | None = None
    planner_payload: dict[str, Any] = {}
    planner_usage: dict[str, Any] | None = None
    planner_retry_usage: dict[str, Any] | None = None
    fixed_consumer_correction_usage: dict[str, Any] | None = None
    planner_prompt_sha256: str | None = None
    planner_retry_prompt_sha256: str | None = None
    fixed_consumer_correction_prompt_sha256: str | None = None
    graph_payload = initial.get("query_relational_program_graph") or {}
    if program_graph_condition and graph_payload.get("query_role_bindings"):
        role_evidence_ids = {
            str(candidate.get("evidence_candidate_id") or "")
            for candidates in graph_payload["query_role_bindings"].values()
            for candidate in candidates
        }
        planning_results: list[dict[str, Any]] = []
        for result in initial["results"]:
            candidate_id = str(result.get("evidence_candidate_id") or "")
            if (
                int(result.get("rank") or 0) > 24
                and candidate_id not in role_evidence_ids
            ):
                continue
            planning_results.append(
                {
                    key: value
                    for key, value in result.items()
                    if key != "database_profile"
                }
                | {
                    "evidence": _semantic_evidence_text(
                        str(result.get("evidence") or ""),
                        3500 if candidate_id.startswith(("workload::", "history_sql::")) else 1400,
                    )
                }
            )
            if len(planning_results) >= 24:
                break
        planner_payload = {
            "database": db_tools.public_database_id,
            "sql_dialect": sql_dialect,
            "question": source_question,
            "benchmark_knowledge": benchmark_evidence,
            "query_contract": query_contract,
            "query_relational_program_graph": graph_payload,
            "retrieved_evidence": planning_results,
            "database_grounding": prefetched_grounding,
        }
        if graph_evo_context_payload is not None:
            planner_payload["graph_evo_program_context"] = (
                graph_evo_context_payload
            )
        if current_relational_program_payload is not None:
            planner_payload["current_relational_program"] = (
                current_relational_program_payload
            )
        if compact_relational_program_payload is not None:
            planner_payload["current_schema_for_program"] = (
                _compact_current_schema_for_program(
                    compact_relational_program_payload,
                    db_tools=db_tools,
                )
            )
        if base_solution_anchor is not None:
            planner_payload["base_solution_anchor"] = base_solution_anchor
        if auxiliary_raw_evidence_draft is not None:
            planner_payload["auxiliary_raw_evidence_draft"] = (
                auxiliary_raw_evidence_draft
            )
        if persistent_recovery_advisory_draft is not None:
            planner_payload["persistent_recovery_advisory_draft"] = (
                persistent_recovery_advisory_draft
            )
        if dual_evidence_priority is not None:
            planner_payload["dual_evidence_priority"] = dual_evidence_priority
        if evidence_bound_program_prior is not None:
            planner_payload["draft_evidence_support"] = draft_evidence_support
            planner_payload["evidence_bound_program_prior"] = (
                evidence_bound_program_prior
            )
        planner_system = PROGRAM_GRAPH_PLANNER_PROMPT
        if base_solution_anchor is not None and not evidence_first_history:
            planner_system += "\n\n" + (
                RAW_BACKBONE_RELATION_PROGRAM_PROMPT
                if performance_first_raw_backbone
                else ANCHORED_RELATION_PROGRAM_PROMPT
            )
        if evidence_first_history:
            planner_system += "\n\n" + EVIDENCE_FIRST_HISTORY_PROMPT
            planner_payload["physical_schema_inventory"] = db_tools.inventory_text()
            planner_payload["history_consumer_version"] = "ontology_evidence_first_v2"
            if realize_semantic_revision:
                column_hypotheses = []
                for document in search_index.by_database.get(schema_context_key, []):
                    try:
                        hypothesis = json.loads(document.text)
                    except (TypeError, ValueError):
                        continue
                    if (hypothesis.get("ontology_kind") == "sql_workload_semantic_object"
                            and hypothesis.get("kind") == "column" and hypothesis.get("aliases")):
                        column_hypotheses.append({key: hypothesis[key] for key in (
                            "physical_identifiers", "aliases", "source_evidence_ids",
                            "interpretation_source", "interpretation_confidence", "interpretation_assessment",
                            "interpretation_observations", "interpretation_revision_evidence") if key in hypothesis})
                planner_payload["recovered_column_hypotheses"] = column_hypotheses
                planner_system += ("\nRecovered column aliases are hypotheses inferred from SQL history and table values, "
                    "not human descriptions or gold mappings. Use them jointly with historical computations and "
                    "literal grounding; resolve conflicting aliases by those concrete witnesses, and preserve "
                    "uncertainty for ambiguous numeric fields.")
        elif fixed_sql_consumer:
            planner_system += "\n\n" + FIXED_SQL_CONSUMER_PROMPT
        if scope_grounded_revision:
            planner_system += "\n\n" + SCOPE_GROUNDED_REVISION_PROMPT
            planner_payload["history_consumer_version"] = "ontology_scope_grounded_v7"
        if witness_consistent_revision:
            planner_payload = _ontology_witness_packet(planner_payload)
            planner_payload["physical_value_witnesses"] = _physical_value_witnesses(db_tools)
            planner_system += "\n\n" + WITNESS_CONSISTENT_PROMPT
        if grounded_binding_revision:
            planner_payload = _grounded_binding_packet(planner_payload)
            planner_system += "\n\n" + GROUNDED_BINDING_PROMPT
        if scope_faithful_revision:
            planner_system += "\n\n" + SCOPE_FAITHFUL_PROMPT
        if semantic_memory is not None:
            planner_payload["semantic_memory"] = semantic_memory
            planner_system += "\n\n" + CONTRACT_PROMPT
            if semantic_memory.get("composition_revision") == 2:
                from .composition_obligations import draft_obligations, REVISION_PROMPT
                planner_payload["composition_obligations"] = draft_obligations(
                    {"anchor": anchor_sql, "raw": auxiliary_raw_sql})
                planner_system += "\n\n" + REVISION_PROMPT
        planner_user = json.dumps(planner_payload, ensure_ascii=False, separators=(",", ":") if witness_consistent_revision else None)
        planner_prompt_sha256 = sha256(
            json.dumps(
                {
                    "system": planner_system,
                    "user": planner_payload,
                },
                ensure_ascii=False,
                sort_keys=True,
                separators=(",", ":"),
            ).encode()
        ).hexdigest()
        try:
            compiled_semantic_plan, planner_usage = client.chat_json_with_metadata(
                planner_system,
                planner_user,
            )
            role_bindings = dict(graph_payload["query_role_bindings"])
            metric_roles = [
                role
                for role in role_bindings
                if re.search(
                    r"\b(?:number|count|total|sum|average|variance|deviation|range|minimum|maximum|min|max)\b",
                    role,
                    flags=re.I,
                )
            ]
            initial_coverage = _role_binding_coverage(
                str(compiled_semantic_plan.get("candidate_sql") or ""),
                role_bindings,
                sql_dialect,
            )
            missing_metric_roles = [
                role
                for role in metric_roles
                if role not in initial_coverage["role_choices"]
            ]
            metric_role_repair_attempted = bool(
                missing_metric_roles and not fixed_sql_consumer
            )
            if metric_role_repair_attempted:
                missing_bindings = {
                    role: role_bindings[role] for role in missing_metric_roles
                }
                retry_payload = {
                    **planner_payload,
                    "previous_plan": compiled_semantic_plan,
                    "required_missing_metric_role_bindings": missing_bindings,
                    "revision_instruction": (
                        "Revise candidate_sql so every listed metric role uses at "
                        "least one of its supplied physical candidates. Preserve "
                        "already covered roles, joins, and window/filter staging."
                    ),
                }
                retry_system = planner_system + (
                    "\nThis is a bounded role-coverage correction of the previous plan."
                )
                retry_user = json.dumps(retry_payload, ensure_ascii=False)
                planner_retry_prompt_sha256 = sha256(
                    json.dumps(
                        {"system": retry_system, "user": retry_payload},
                        ensure_ascii=False,
                        sort_keys=True,
                        separators=(",", ":"),
                    ).encode()
                ).hexdigest()
                repaired_plan, planner_retry_usage = (
                    client.chat_json_with_metadata(retry_system, retry_user)
                )
                repaired_coverage = _role_binding_coverage(
                    str(repaired_plan.get("candidate_sql") or ""),
                    role_bindings,
                    sql_dialect,
                )
                before = sum(
                    role in initial_coverage["role_choices"]
                    for role in metric_roles
                )
                after = sum(
                    role in repaired_coverage["role_choices"]
                    for role in metric_roles
                )
                if after > before:
                    compiled_semantic_plan = repaired_plan
            if (
                anchor_sql is not None
                and graph_evo_context_payload is not None
                and not realize_submitted_program
                and str(compiled_semantic_plan.get("candidate_sql") or "").strip()
            ):
                planner_candidate_sql = str(
                    compiled_semantic_plan["candidate_sql"]
                ).strip()
                candidate_scaffold = compile_graph_evo_candidate_scaffold(
                    anchor_sql=anchor_sql,
                    proposal_sql=planner_candidate_sql,
                    graph_evo_context=graph_evo_context_payload,
                    dialect=sql_dialect,
                )
                compiled_semantic_plan = {
                    **compiled_semantic_plan,
                    "planner_candidate_sql": planner_candidate_sql,
                    "candidate_sql": str(
                        candidate_scaffold.get("candidate_sql")
                        or planner_candidate_sql
                    ),
                    "candidate_scaffold": {
                        key: value
                        for key, value in candidate_scaffold.items()
                        if key != "candidate_sql"
                    },
                }
            compiled_semantic_plan = {
                **compiled_semantic_plan,
                "compiler": "automatic_evidence_bound_semantic_planner_v1",
                "metric_role_repair_attempted": metric_role_repair_attempted,
                "metric_role_repair_skipped_for_fixed_consumer": bool(
                    missing_metric_roles and fixed_sql_consumer
                ),
                "uses_evaluator_gold": False,
            }
        except Exception as error:
            if evidence_first_history:
                # A failed internal generator is not a completed prediction.
                # The outer runner records the actual error for bounded resume.
                raise
            compiled_semantic_plan = {
                "compiler": "automatic_evidence_bound_semantic_planner_v1",
                "status": "planner_failed",
                "error_type": type(error).__name__,
                "uses_evaluator_gold": False,
            }
    if semantic_memory is not None and compiled_semantic_plan is not None:
        compiled_semantic_plan["scope_contract_validation"] = validate_contract(compiled_semantic_plan, semantic_memory)
    user_payload = {
        "database": db_tools.public_database_id,
        "question": source_question,
        "benchmark_knowledge": benchmark_evidence,
        "query_contract": query_contract,
        "physical_schema_inventory": db_tools.inventory_text(),
        "initial_schema_search": initial,
        "budgets": {
            "llm_turns": max_turns,
            "tool_actions": max_actions,
            "candidate_sql_executions": max_sql_executions,
        },
    }
    if semantic_memory is not None:
        user_payload["semantic_memory"] = semantic_memory
        system += "\n\n" + CONTRACT_PROMPT
    if graph_evo_context_payload is not None:
        user_payload["graph_evo_program_context"] = graph_evo_context_payload
    if current_relational_program_payload is not None:
        user_payload["current_relational_program"] = (
            current_relational_program_payload
        )
    if prefetched_grounding is not None:
        user_payload["database_grounding"] = prefetched_grounding
    if compiled_semantic_plan is not None:
        user_payload["compiled_semantic_plan"] = compiled_semantic_plan
    if base_solution_anchor is not None:
        user_payload["base_solution_anchor"] = base_solution_anchor
    if auxiliary_raw_evidence_draft is not None:
        user_payload["auxiliary_raw_evidence_draft"] = (
            auxiliary_raw_evidence_draft
        )
    if persistent_recovery_advisory_draft is not None:
        user_payload["persistent_recovery_advisory_draft"] = (
            persistent_recovery_advisory_draft
        )
    if dual_evidence_priority is not None:
        user_payload["dual_evidence_priority"] = dual_evidence_priority
    if draft_evidence_support is not None:
        user_payload["draft_evidence_support"] = draft_evidence_support
    if evidence_bound_program_prior is not None:
        user_payload["evidence_bound_program_prior"] = (
            evidence_bound_program_prior
        )
    messages: list[dict[str, Any]] = [
        {"role": "system", "content": system},
        {
            "role": "user",
            "content": json.dumps(user_payload, ensure_ascii=False),
        },
    ]
    budget = ToolBudget(max_actions, max_sql_executions)
    trajectory: list[dict[str, Any]] = []
    usage: list[dict[str, Any]] = []
    final_sql: str | None = None
    last_sql: str | None = (
        str(compiled_semantic_plan.get("candidate_sql") or "").strip()
        if fixed_sql_consumer and compiled_semantic_plan is not None
        else None
    )
    tool_spec = react_tools(condition, dialect=sql_dialect)
    tool_observation_character_limit = (
        8000 if program_graph_condition else 16000
    )
    turns = () if fixed_sql_consumer else range(1, max_turns + 1)
    for turn in turns:
        turn_contract_violations: list[str] = []
        tool_choice: str | dict[str, Any] = "auto"
        turn_tool_spec = tool_spec
        if turn == max_turns:
            tool_choice = {
                "type": "function",
                "function": {"name": "submit_sql"},
            }
            # Some OpenAI-compatible servers treat tool_choice as a hint. Removing
            # every other tool makes the final action deterministic without adding
            # another LLM call or increasing the agent budget.
            turn_tool_spec = [
                tool
                for tool in tool_spec
                if tool.get("function", {}).get("name") == "submit_sql"
            ]
        response = client.chat_tools(messages, turn_tool_spec, tool_choice=tool_choice)
        usage.append(_usage(response))
        message = dict(response["choices"][0]["message"])
        calls = list(message.get("tool_calls") or [])
        messages.append(message)
        if not calls:
            messages.append(
                {
                    "role": "user",
                    "content": "Use a database tool now; submit_sql is required by the final turn.",
                }
            )
            trajectory.append({"turn": turn, "tool": None, "status": "no_tool_call"})
            continue
        submitted = False
        for call in calls:
            name = str(call.get("function", {}).get("name") or "")
            call_id = str(call.get("id") or f"turn-{turn}-{len(trajectory)}")
            arguments: dict[str, Any] = {}
            try:
                arguments = _tool_arguments(call)
                if name in {"execute_sql", "submit_sql"} and arguments.get("sql"):
                    last_sql = str(arguments["sql"]).strip()
                if name == "submit_sql":
                    # Submission itself is not charged as a candidate execution.
                    if budget.actions >= budget.max_actions:
                        raise RuntimeError("tool action budget exhausted")
                    budget.actions += 1
                else:
                    budget.charge(name)
                observation = _dispatch(name, arguments, db_tools)
                if name == "execute_sql":
                    observation["query_contract_check"] = assess_query_contract(
                        query_contract, observation
                    )
                    turn_contract_violations = list(
                        observation["query_contract_check"]["violations"]
                    )
                status = "ok"
                if name == "submit_sql":
                    final_sql = last_sql
                    submitted = True
            except Exception as error:
                observation = {
                    "error_type": type(error).__name__,
                    "error": str(error)[:800],
                }
                status = "error"
            trajectory.append(
                {
                    "turn": turn,
                    "tool": name,
                    "arguments": arguments,
                    "status": status,
                    "observation": observation,
                }
            )
            messages.append(
                {
                    "role": "tool",
                    "tool_call_id": call_id,
                    "name": name,
                    "content": _bounded_tool_observation(
                        observation,
                        character_limit=tool_observation_character_limit,
                    ),
                }
            )
            if submitted:
                break
        if submitted:
            break
        if turn_contract_violations:
            messages.append(
                {
                    "role": "user",
                    "content": (
                        "The latest candidate violates the question-derived result "
                        "contract: "
                        + json.dumps(turn_contract_violations, ensure_ascii=False)
                        + ". Revise the SQL semantics and projection before submit_sql."
                    ),
                }
            )
    final_sql = final_sql or last_sql or ""
    final_sql, dual_draft_outer_preservations = (
        _preserve_dual_draft_outer_consensus(
            final_sql,
            recovered_draft_sql,
            direct_raw_draft_sql,
            sql_dialect,
            source_question,
        )
    )
    if evidence_first_history:
        final_sql = str((compiled_semantic_plan or {}).get("candidate_sql") or final_sql)
        dual_draft_outer_preservations = []
    final_sql = _repair_mysql_rollup_clause_order(final_sql, sql_dialect)
    raw_react_sql = final_sql
    fixed_consumer_submission_validation = False
    fixed_consumer_correction_attempted = False
    if realize_submitted_program:
        fixed_consumer_submission_validation = (
            _append_fixed_consumer_submission_validation(
                trajectory=trajectory,
                proposal_sql=raw_react_sql,
                dialect=sql_dialect,
                query_contract=query_contract,
                db_tools=db_tools,
                budget=budget,
            )
        )
    if (
        fixed_sql_consumer
        and (raw_react_sql or realize_semantic_revision)
        and (scope_grounded_revision or _proposal_execution_certificate(
            trajectory, raw_react_sql, sql_dialect
        ) is None)
        and budget.actions < budget.max_actions
        and budget.sql_executions < budget.max_sql_executions
        and compact_relational_program_payload is not None
    ):
        failed_observation: dict[str, Any] = {}
        for step in reversed(trajectory):
            if step.get("tool") == "execute_sql":
                failed_observation = dict(step.get("observation") or {})
                break
        feedback = {
            key: failed_observation[key]
            for key in (
                "executable",
                "error_type",
                "error",
                "columns",
                "truncated",
                "query_contract_check",
                "schema_view",
                "storage_adapter",
            )
            if failed_observation.get(key) not in (None, "", [], {})
        }
        if not raw_react_sql:
            feedback.update(executable=False, error_type="MissingSQL",
                            error="The semantic planner returned no candidate_sql. Return a complete candidate_sql in the existing correction response.")
        fixed_consumer_correction_attempted = True
        try:
            correction = _unique_unknown_column_repair(
                sql=raw_react_sql,
                execution_observation=failed_observation,
                db_tools=db_tools,
                dialect=sql_dialect,
            )
            if scope_grounded_revision:
                correction = None
            if correction is None:
                correction_payload = {
                    "sql_dialect": sql_dialect,
                    "question": source_question,
                    "query_contract": query_contract,
                    "failed_candidate_sql": raw_react_sql,
                    "execution_feedback": feedback,
                    "relevant_current_schema": _relevant_current_schema_for_sql(
                        raw_react_sql,
                        db_tools=db_tools,
                        dialect=sql_dialect,
                    ),
                    "compact_relational_program": (
                        compact_relational_program_payload
                    ),
                    "evidence_bound_program_prior": (
                        evidence_bound_program_prior
                    ),
                    "score_or_expected_answer_used": False,
                    "uses_evaluator_gold": False,
                }
                if not raw_react_sql and realize_semantic_revision:
                    correction_payload.update(
                        incomplete_semantic_plan=compiled_semantic_plan,
                        physical_schema_inventory=db_tools.inventory_text(),
                        recovered_column_hypotheses=planner_payload.get("recovered_column_hypotheses", []),
                    )
                correction_system = BASIC_EXECUTION_CORRECTION_PROMPT
                if semantic_memory is not None:
                    correction_payload["semantic_memory"] = semantic_memory
                    correction_payload["scope_grain_contract"] = (compiled_semantic_plan or {}).get("scope_grain_contract")
                    correction_payload["scope_contract_validation"] = validate_contract(compiled_semantic_plan or {}, semantic_memory)
                if scope_grounded_revision:
                    correction_system = SCOPE_GROUNDED_CORRECTION_PROMPT
                    correction_payload.update(
                        ontology_evidence=planner_payload,
                        submitted_role_bindings=(compiled_semantic_plan or {}).get("role_bindings", []),
                        execution_observation=failed_observation,
                    )
                if witness_consistent_revision:
                    # The canonical ontology packet already contains these
                    # proposed contracts; do not expand the old graph again.
                    correction_payload.pop("compact_relational_program", None)
                    correction_payload.pop("evidence_bound_program_prior", None)
                    correction_system += "\n\n" + WITNESS_CONSISTENT_PROMPT
                if grounded_binding_revision:
                    binding_observations = _grounded_binding_observations(
                        db_tools, compiled_semantic_plan or {}, raw_react_sql,
                        execution_python=physical_execution_python if (realized_edit_revision or scope_faithful_revision) else None,
                        relational_grain=relational_grain_revision)
                    correction_payload["binding_validation"] = _binding_observations_for_prompt(binding_observations)
                    correction_payload["scope_obligations"] = (compiled_semantic_plan or {}).get("scope_obligations", [])
                    if compiled_semantic_plan is not None:
                        compiled_semantic_plan["binding_validation"] = binding_observations
                    correction_system += "\n\n" + GROUNDED_BINDING_PROMPT
                if realized_edit_revision:
                    correction_system += "\n\n" + REALIZED_SQL_EDIT_PROMPT
                if scope_faithful_revision:
                    sql_scopes = _submitted_sql_scopes(raw_react_sql)
                    correction_payload["submitted_sql_scopes"] = sql_scopes
                    if compiled_semantic_plan is not None:
                        compiled_semantic_plan["submitted_sql_scopes"] = sql_scopes
                    correction_system += "\n\n" + SCOPE_FAITHFUL_PROMPT
                if relational_grain_revision:
                    from .relational_grain_observer import grain_observations_for_prompt
                    correction_payload["relational_grain_validation"] = grain_observations_for_prompt(
                        binding_observations["relational_grain"])
                    correction_system += "\n\n" + RELATIONAL_GRAIN_PROMPT
                if entity_grain_revision:
                    correction_system += "\n\n" + ENTITY_GRAIN_CONTRACT_PROMPT
                if semantic_memory is not None:
                    correction_system += "\n\n" + CONTRACT_PROMPT
                    if semantic_memory.get("composition_revision") == 2:
                        from .composition_obligations import draft_obligations, REVISION_PROMPT
                        correction_payload["composition_obligations"] = draft_obligations(
                            {"anchor": anchor_sql, "raw": auxiliary_raw_sql}, raw_react_sql)
                        correction_system += "\n\n" + REVISION_PROMPT
                        if compiled_semantic_plan is not None:
                            compiled_semantic_plan["composition_obligations"] = correction_payload["composition_obligations"]
                fixed_consumer_correction_prompt_sha256 = sha256(
                    json.dumps(
                        {
                            "system": correction_system,
                            "user": correction_payload,
                        },
                        ensure_ascii=False,
                        sort_keys=True,
                        separators=(",", ":"),
                    ).encode("utf-8")
                ).hexdigest()
                correction, fixed_consumer_correction_usage = (
                    client.chat_json_with_metadata(
                        correction_system,
                        json.dumps(correction_payload, ensure_ascii=False, separators=(",", ":") if witness_consistent_revision else None),
                    )
                )
            if semantic_memory is not None and compiled_semantic_plan is not None:
                if semantic_memory.get("composition_revision") == 2:
                    compiled_semantic_plan["composition_review"] = correction.get("composition_review", [])
                compiled_semantic_plan["initial_scope_grain_contract"] = compiled_semantic_plan.get("scope_grain_contract")
                compiled_semantic_plan["scope_grain_contract"] = correction.get("scope_grain_contract")
                compiled_semantic_plan["final_scope_contract_validation"] = validate_contract(correction, semantic_memory)
            if realized_edit_revision:
                realized_sql, edit_observation = _realize_sql_edits(raw_react_sql, correction.get("sql_edits"))
                correction["candidate_sql"] = realized_sql
                if compiled_semantic_plan is not None:
                    compiled_semantic_plan["sql_edit_realization"] = {
                        **edit_observation, "requested_edits": correction.get("sql_edits"),
                        "uses_evaluator_gold": False}
            if entity_grain_revision:
                from .relational_program_compiler import realize_entity_grain_contracts
                contract_sql = str(correction.get("candidate_sql") or raw_react_sql).strip()
                entity_sql, entity_audit = realize_entity_grain_contracts(
                    contract_sql, correction.get("entity_grain_contracts", []), db_tools.database)
                correction["candidate_sql"] = entity_sql
                if compiled_semantic_plan is not None:
                    compiled_semantic_plan["entity_grain_realization"] = {
                        **entity_audit, "pre_realization_sql": contract_sql,
                        "requested_contracts": correction.get("entity_grain_contracts", [])}
            if scope_grounded_revision and compiled_semantic_plan is not None:
                compiled_semantic_plan["scope_review"] = {
                    "reason": correction.get("correction_reason"),
                    "checks": correction.get("scope_checks"),
                    "uses_evaluator_gold": False,
                }
            corrected_sql = str(correction.get("candidate_sql") or "").strip()
            if corrected_sql and corrected_sql != raw_react_sql:
                raw_react_sql = corrected_sql
                final_sql = corrected_sql
                last_sql = corrected_sql
                if compiled_semantic_plan is not None:
                    compiled_semantic_plan = {
                        **compiled_semantic_plan,
                        "pre_execution_correction_sql": str(
                            compiled_semantic_plan.get("candidate_sql") or ""
                        ),
                        "candidate_sql": corrected_sql,
                        "basic_execution_correction": {
                            "attempted": True,
                            "mode": (
                                "deterministic_unique_current_catalog_owner"
                                if fixed_consumer_correction_usage is None
                                else "single_model_execution_correction"
                            ),
                            "reason": str(
                                correction.get("correction_reason") or ""
                            )[:800],
                            "score_or_expected_answer_used": False,
                            "uses_evaluator_gold": False,
                        },
                    }
                _append_fixed_consumer_submission_validation(
                    trajectory=trajectory,
                    proposal_sql=corrected_sql,
                    dialect=sql_dialect,
                    query_contract=query_contract,
                    db_tools=db_tools,
                    budget=budget,
                )
        except Exception as error:
            if realize_semantic_revision:
                raise
            trajectory.append(
                {
                    "turn": "fixed_consumer_correction",
                    "tool": None,
                    "status": "error",
                    "observation": {
                        "error_type": type(error).__name__,
                        "error": str(error)[:800],
                    },
                    "score_or_expected_answer_consulted": False,
                }
            )
    candidate_selection: dict[str, Any] | None = None
    if program_graph_condition and compiled_semantic_plan is not None:
        planner_sql = str(
            compiled_semantic_plan.get("candidate_sql") or ""
        ).strip()
        if planner_sql:
            role_bindings = dict(graph_payload.get("query_role_bindings") or {})
            if condition in {
                "minimal_join_tree_react",
                "evoschema_minimal_join_tree_react",
            }:
                selected_role_choices = dict(
                    graph_payload.get("role_choices") or {}
                )
                role_bindings = {
                    role: [
                        candidate
                        for candidate in role_bindings.get(role, [])
                        if str(candidate.get("physical_identifier") or "")
                        == str(choice.get("physical_identifier") or "")
                    ]
                    for role, choice in selected_role_choices.items()
                }
                role_bindings = {
                    role: candidates
                    for role, candidates in role_bindings.items()
                    if candidates
                }
            candidate_selection = _authoritative_react_submission_audit(
                react_sql=final_sql,
                planner_sql=planner_sql,
                role_bindings=role_bindings,
                dialect=sql_dialect,
            )
    relation_composition: dict[str, Any] | None = None
    if anchor_sql is not None:
        proposal_execution = _proposal_execution_certificate(
            trajectory, raw_react_sql, sql_dialect
        )
        relation_composition = compile_relational_program(
            # A semantic revision is the new single submitted program. Existing
            # Graph/Evo transformations operate on it, not on the frozen old draft.
            # This decision uses no EX, gold, candidate ranking or answer contents.
            anchor_sql=raw_react_sql if realize_semantic_revision else anchor_sql,
            proposal_sql=raw_react_sql,
            question=source_question,
            database=database,
            database_id=str(row["database_id"]),
            dialect=sql_dialect,
            relationship_edges=(query_relationship_edges or None),
            evolution_mapping=evolution_mapping,
            graph_evo_context=graph_evo_context_payload,
            proposal_execution=proposal_execution,
            realize_submitted_program=realize_submitted_program,
            preserve_submitted_grain=scope_grounded_revision,
        )
        if realize_semantic_revision:
            relation_composition["semantic_submission_is_input"] = True
            relation_composition["previous_draft_sha256"] = sha256(anchor_sql.encode()).hexdigest()
        realized_sql_before_draft_preservation = str(relation_composition.pop("sql"))
        final_sql, post_realization_preservations = (
            _preserve_dual_draft_outer_consensus(
                realized_sql_before_draft_preservation,
                recovered_draft_sql,
                direct_raw_draft_sql,
                sql_dialect,
                source_question,
            )
        )
        dual_draft_outer_preservations.extend(post_realization_preservations)
        if evidence_first_history:
            # Preserve the single evidence-grounded submission after normal typed
            # realization; draft agreement alone is not semantic support.
            final_sql = realized_sql_before_draft_preservation
            dual_draft_outer_preservations = []
        final_sql = _repair_mysql_rollup_clause_order(final_sql, sql_dialect)
    if performance_first_raw_backbone and not evidence_first_history:
        final_sql, raw_backbone_preservations = (
            _preserve_raw_backbone_without_structural_support(
                final_sql,
                anchor_sql,
                question=source_question,
                graph_payload=graph_payload,
                evidence_payload={
                    "graph_evo_program_context": graph_evo_context_payload,
                    "exact_value_matches": exact_value_matches,
                },
                dialect=sql_dialect,
            )
        )
        dual_draft_outer_preservations.extend(raw_backbone_preservations)
        final_sql = _repair_mysql_rollup_clause_order(final_sql, sql_dialect)
    if tools_factory is None:
        probe = execution_probe(database, final_sql, timeout_seconds=8.0)
    else:
        adapted_probe = db_tools.execute_sql(final_sql, limit=1)
        probe = {
            "executable": bool(adapted_probe.get("executable")),
            "validation": {
                "valid": bool(final_sql.strip()),
                "adapter_validated_current_schema": True,
            },
            **(
                {
                    "error_type": adapted_probe.get("error_type"),
                    "error": adapted_probe.get("error"),
                }
                if not adapted_probe.get("executable")
                else {}
            ),
            "schema_view": adapted_probe.get("schema_view"),
            "storage_adapter": adapted_probe.get("storage_adapter"),
        }
    all_usage = (
        ([planner_usage] if planner_usage is not None else [])
        + ([planner_retry_usage] if planner_retry_usage is not None else [])
        + (
            [fixed_consumer_correction_usage]
            if fixed_consumer_correction_usage is not None
            else []
        )
        + usage
    )
    known_tokens = [
        int(row["total_tokens"])
        for row in all_usage
        if isinstance(row.get("total_tokens"), int)
    ]
    return {
        "example_id": row["example_id"],
        "dataset_id": row["dataset_id"],
        "upstream_split": row["upstream_split"],
        "database_id": row["database_id"],
        "method_id": method_id_override or METHOD_IDS[condition],
        "asset_condition": condition,
        "paper_baseline_adapter": (
            {
                "paper": "CHESS",
                "adapter": "call_matched_catalog_value_execution_revision_v1",
                "recovery_or_ontology_access": False,
            }
            if condition == "chess_react"
            else {
                "paper": "AutoLink",
                "adapter": "call_matched_single_targeted_expansion_v1",
                "recovery_or_ontology_access": False,
            }
            if condition == "autolink_react"
            else None
        ),
        "decision": "answer",
        "sql": final_sql,
        "execution_probe": probe,
        "react": {
            **({"semantic_memory": semantic_memory, "scope_contract_validation": validate_contract(compiled_semantic_plan or {}, semantic_memory)} if semantic_memory is not None else {}),
            "turns": len(usage),
            "tool_actions": budget.actions,
            "sql_executions": budget.sql_executions,
            "trajectory": trajectory,
            "initial_search": initial,
            **({"retrieval_cache": retrieval_snapshot["provenance"]} if retrieval_snapshot is not None else {}),
            "initial_search_query": search_query,
            "graph_evo_program_context": graph_evo_context_payload,
            "current_relational_program": current_relational_program_payload,
            "compact_relational_program": compact_relational_program_payload,
            "target_isolated_demonstrations": target_isolated_demonstrations,
            "query_contract": query_contract,
            "prefetched_grounding": prefetched_grounding,
            "compiled_semantic_plan": compiled_semantic_plan,
            "candidate_selection": (
                None if inject_graph_evo_context else candidate_selection
            ),
            "react_submission_audit": (
                candidate_selection if inject_graph_evo_context else None
            ),
            "base_solution_anchor": base_solution_anchor,
            "auxiliary_raw_evidence_draft": auxiliary_raw_evidence_draft,
            "persistent_recovery_advisory_draft": (
                persistent_recovery_advisory_draft
            ),
            "dual_evidence_priority": dual_evidence_priority,
            "dual_draft_outer_preservations": sorted(
                set(dual_draft_outer_preservations)
            ),
            "draft_evidence_support": draft_evidence_support,
            "evidence_bound_program_prior": evidence_bound_program_prior,
            "raw_react_sql": raw_react_sql if anchor_sql is not None else None,
            "fixed_consumer_submission_validation": (
                fixed_consumer_submission_validation
            ),
            "fixed_consumer_correction_attempted": (
                fixed_consumer_correction_attempted
            ),
            "fixed_sql_consumer": fixed_sql_consumer,
            "realize_semantic_revision": realize_semantic_revision,
            "relation_composition": relation_composition,
        },
        "audit": {
            "usage": all_usage,
            "known_total_tokens": sum(known_tokens),
            "model_calls": len(all_usage),
            "planner_prompt_sha256": planner_prompt_sha256,
            "planner_retry_prompt_sha256": planner_retry_prompt_sha256,
            "fixed_consumer_correction_prompt_sha256": (
                fixed_consumer_correction_prompt_sha256
            ),
            "graph_evo_context_sha256": graph_evo_context_sha256,
            "current_relational_program_sha256": (
                current_relational_program_payload.get("program_sha256")
                if current_relational_program_payload is not None
                else None
            ),
            "compact_relational_program_sha256": (
                sha256(
                    json.dumps(
                        compact_relational_program_payload,
                        ensure_ascii=False,
                        sort_keys=True,
                        separators=(",", ":"),
                    ).encode("utf-8")
                ).hexdigest()
                if compact_relational_program_payload is not None
                else None
            ),
            "target_isolated_demonstration_count": len(
                target_isolated_demonstrations
            ),
            "planner_payload_characters": (
                len(planner_user) if planner_prompt_sha256 is not None else 0
            ),
            "auxiliary_raw_draft_sha256": (
                sha256(auxiliary_raw_sql.strip().encode("utf-8")).hexdigest()
                if auxiliary_raw_sql is not None
                else None
            ),
            "prompt_sha256": sha256(
                json.dumps(
                    {"system": system, "user": user_payload},
                    ensure_ascii=False,
                    sort_keys=True,
                    separators=(",", ":"),
                ).encode()
            ).hexdigest(),
            "tool_observation_character_limit": (
                tool_observation_character_limit
            ),
            "consumer": (
                "fixed_generator_plus_exact_execution"
                if fixed_sql_consumer
                else "react"
            ),
        },
        "latency_seconds": round(time.perf_counter() - started, 6),
    }
    "of",
    "on",
    "one",
    "only",
    "to",
