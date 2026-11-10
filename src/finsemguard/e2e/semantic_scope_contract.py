"""Query-local semantic memory and explicit eligibility/measure obligations."""
from copy import deepcopy
from typing import Any

from pydantic import BaseModel, Field, ValidationError

from finsemguard.schema_recovery.joint import digest


class Eligibility(BaseModel):
    predicate: str
    input_relation: str
    scope: str
    correlation_keys: list[str]
    source_ids: list[str] = Field(default_factory=list)


class Measure(BaseModel):
    expression: str
    input_relation: str
    scope: str
    aggregation_grain: list[str]
    correlation_keys: list[str]
    eligibility_application: str
    multiplicity_argument: str
    source_ids: list[str] = Field(default_factory=list)


class ScopeGrainContract(BaseModel):
    target_entity: str
    entity_keys: list[str]
    eligibility: list[Eligibility]
    measures: list[Measure]
    selected_bindings: dict[str, str]
    unresolved_choices: list[dict[str, Any]] = Field(default_factory=list)


CONTRACT_PROMPT = """V17 response schema extension: include scope_grain_contract as a required
top-level JSON object alongside candidate_sql and the existing response fields.
This applies to both initial plans and correction responses, even when SQL is unchanged.
Return the complete contract, not a prose summary or null. Required fields:
target_entity (string), entity_keys (list), selected_bindings (role -> physical identifier),
unresolved_choices (list), eligibility (list of {predicate,input_relation,scope,
correlation_keys,source_ids}), measures (list of {expression,input_relation,scope,
aggregation_grain,correlation_keys,eligibility_application,multiplicity_argument,source_ids}).
entity_keys, correlation_keys, aggregation_grain and source_ids are arrays of strings.
unresolved_choices is an array of objects (use [] if none), not strings.
source_ids cite actual historical program IDs (bird_dev:* from the supplied evidence),
not semantic::* or program::* asset IDs. Use [] when no historical source supports a clause.
State which predicates select eligible entities and which restrict measure rows.
A measure must be computed at its own grain before a one-to-many eligibility join,
or use a semijoin/EXISTS so rows are not duplicated. Explain the structural reason.
Resolve uncertain roles with the available evidence and bounded read-only probes.
Do not silently discard uncertainty or let an eligibility-only filter narrow a
measure's scope. This is one query-local plan, not a persistent ontology update.
Semantic memory is a fixed revision. Existing supported SQL rewrites remain bounded;
no generic rewrite is guaranteed to repair an incorrect scope or aggregate grain."""


def query_memory(revision: str, families: list[dict], *, selected_source_ids: list[str] | None = None) -> dict:
    if not revision:
        raise ValueError("a fixed semantic memory revision is required")
    records = []
    for family in families:
        if selected_source_ids is not None and not set(family.get("source_ids", [])) & set(selected_source_ids):
            continue
        last = family.get("attempts", [{}])[-1]
        records.append({"family_id": family["family_id"], "table": family["table"],
            "schema_context": family["schema_context"], "status": family["status"],
            "selected_assignment": family.get("selected_assignment"), "roles": last.get("proposal", {}).get("roles", []),
            "remaining_alternatives": last.get("feasible_assignments", []),
            "constraint_ids": [c["constraint_id"] for c in last.get("constraints", [])],
            "profile_revision": family["profile_revision"], "source_ids": family["source_ids"]})
    state = {"ontology_revision": revision, "families": deepcopy(records)}
    state["memory_hash"] = digest(state)
    return state


def validate_contract(plan: dict, memory: dict) -> dict:
    """Validate explicit representation and provenance, not semantic correctness."""
    try:
        value = ScopeGrainContract.model_validate(plan.get("scope_grain_contract", {})).model_dump()
    except ValidationError as error:
        return {"valid_representation": False, "errors": error.errors(include_url=False), "semantic_correctness": "not_determined"}
    sources = {s for f in memory.get("families", []) for s in f.get("source_ids", [])}
    sources.update(memory.get("additional_source_ids", []))
    cited = {s for item in value["eligibility"] + value["measures"] for s in item["source_ids"]}
    unknown = sorted(cited - sources)
    return {"valid_representation": not unknown, "unknown_source_ids": unknown,
        "contract": value, "semantic_correctness": "requires_observations_and_evaluation"}
