"""Opt-in forward-impact maintenance around the existing source-keyed layer.

`depends_on` stores upstream identities on a dependent object. The public edge
orientation is upstream -> dependent. No recovery callback sees skipped objects.
"""
from __future__ import annotations
from collections import defaultdict, deque
from copy import deepcopy
from typing import Callable, Any

from finsemguard.ontology_discovery.workload_semantics import WorkloadSemanticLayer
from finsemguard.schema_recovery.joint import digest


def forward_closure(seeds: set[str], *object_sets: list[dict]) -> set[str]:
    outgoing: dict[str, set[str]] = defaultdict(set)
    for objects in object_sets:
        for obj in objects:
            for upstream in obj.get("depends_on", []):
                outgoing[upstream].add(obj["id"])
    seen, pending = set(seeds), deque(sorted(seeds))
    while pending:
        for dependent in outgoing[pending.popleft()]:
            if dependent not in seen:
                seen.add(dependent)
                pending.append(dependent)
    return seen


def update_objects(previous: list[dict], structural: list[dict], *,
                   previous_structural: list[dict] | None = None,
                   interpretations: dict[str, dict] | None = None,
                   lineage: dict[str, str] | None = None,
                   profile_revisions: dict[str, str] | None = None,
                   previous_profile_revisions: dict[str, str] | None = None,
                   recovery: Callable[[str, list[dict]], dict[str, dict]] | None = None) -> tuple[list[dict], dict]:
    """Apply an explicit delta and validate only its forward closure.

    Source assertions retain original physical_identifiers. `binding` separately
    records current physical realizations. Callback returns auxiliary semantic
    attributes, not source IDs or identity rewrites. Lineage-only events do not
    invoke recovery. Profile changes seed every member sharing that family.
    """
    old = {o["id"]: o for o in previous}
    base = {o["id"]: o for o in (previous_structural if previous_structural is not None else previous)}
    new = {o["id"]: o for o in structural}
    interpretations, lineage = interpretations or {}, lineage or {}
    profiles, old_profiles = profile_revisions or {}, previous_profile_revisions or {}
    source_delta = {k for k in base.keys() | new.keys() if base.get(k) != new.get(k)}
    semantic_delta = {k for k, changes in interpretations.items()
                      if k in old and any(old[k].get(field) != value for field, value in changes.items())}
    changed_profiles = {k for k in profiles.keys() | old_profiles.keys() if profiles.get(k) != old_profiles.get(k)}
    profile_delta = {k for k, o in old.items() if o.get("family_id") in changed_profiles}
    binding_delta = {k for k, o in old.items() if set(o.get("binding", o.get("physical_identifiers", []))) & lineage.keys()}
    seeds = source_delta | semantic_delta | profile_delta | binding_delta
    touched_families = {o.get("family_id") for k, o in old.items() if k in seeds and o.get("family_id")}
    family_members = {k for k, o in old.items() if o.get("family_id") in touched_families}
    seeds |= family_members
    affected = forward_closure(seeds, previous, structural)
    output = {}
    for k in sorted(old.keys() | new.keys()):
        if k not in affected:
            output[k] = deepcopy(old[k])
            continue
        if k not in new:
            continue  # Last active source removed this structural assertion.
        obj = {**deepcopy(old.get(k, {})), **deepcopy(new[k])}
        obj.update(deepcopy(interpretations.get(k, {})))
        bindings = obj.get("binding", obj.get("physical_identifiers", []))
        obj["binding"] = [lineage.get(b, b) for b in bindings]
        family = obj.get("family_id")
        if family in changed_profiles:
            obj["profile_revision"] = profiles.get(family)
        output[k] = obj
    # Count only actual callback invocations, with one invocation per affected
    # family; caller may implement the bounded Propose/Choose call sequence.
    calls = []
    families: dict[str, list[dict]] = defaultdict(list)
    recover_seeds = source_delta | profile_delta
    recovery_families = {old[k].get("family_id") for k in recover_seeds & old.keys() if old[k].get("family_id")}
    recover_seeds |= {k for k, o in old.items() if o.get("family_id") in recovery_families}
    if recovery is not None:
        for k in sorted(affected & output.keys()):
            o = output[k]
            if o.get("kind") == "column" and k in recover_seeds:
                families[o.get("family_id", k)].append(o)
        for family, members in sorted(families.items()):
            # A family is atomic: all member interpretations are reconciled.
            siblings = [o for o in output.values() if o.get("family_id", o["id"]) == family]
            if not {o["id"] for o in siblings} <= affected:
                raise ValueError("family membership edges must connect all members before recovery")
            changes = recovery(family, deepcopy(siblings))
            calls.append({"family_id": family, "object_ids": [o["id"] for o in siblings]})
            if not set(changes) <= {o["id"] for o in siblings}:
                raise ValueError("recovery attempted to mutate an unrelated object")
            for k, attrs in changes.items():
                if set(attrs) & {"id", "physical_identifiers", "evidence_ids", "depends_on", "binding"}:
                    raise ValueError("recovery may not rewrite identity, bindings or provenance")
                output[k].update(deepcopy(attrs))
    skipped = sorted(old.keys() - affected)
    assert all(output[k] == old[k] for k in skipped)
    diff = [{"id": k, "before": old.get(k), "after": output.get(k)}
            for k in sorted(affected) if old.get(k) != output.get(k)]
    receipt = {"delta_ids": sorted(seeds), "affected_ids": sorted(affected), "skipped_ids": skipped,
        "delta_size": len(seeds), "affected_size": len(affected), "unchanged_object_count": len(skipped),
        "changed_profile_families": sorted(changed_profiles), "recovery_invocations": calls,
        "recovery_invocation_count": len(calls), "ontology_diff": diff,
        "before_hash": digest(previous), "after_hash": digest([output[k] for k in sorted(output)])}
    return [output[k] for k in sorted(output)], receipt


def update_layer(layer: WorkloadSemanticLayer, interpreted_objects: list[dict], rows: list[dict], *,
                 retract: tuple[tuple[str, str], ...] = (), **kwargs: Any) -> tuple[list[dict], dict]:
    previous = layer.objects()
    source_receipt = layer.update(rows, retract=retract)
    result, receipt = update_objects(interpreted_objects, layer.objects(), previous_structural=previous, **kwargs)
    receipt["source_update"] = source_receipt
    return result, receipt
