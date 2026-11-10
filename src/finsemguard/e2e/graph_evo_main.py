"""Unified paper main: M0 recovery + M3 Graph/Evo + M4 realization."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Any, Callable

from finsemguard.agent.llm import VLLMClient
from finsemguard.e2e.method_identity import GRAPH_EVO_SEMANTIC_PROGRAM_MAIN
from finsemguard.e2e.react_text2sql import (
    SQLiteAgentTools,
    SchemaSearchIndex,
    run_react_text2sql,
)

if TYPE_CHECKING:
    from finsemguard.e2e.evolution_relations import RelationEvolutionMapping


SUPPORTED_MAIN_CONDITIONS = {
    "minimal_join_tree_react",
    "evoschema_minimal_join_tree_react",
}


def run_graph_evo_semantic_program_main(
    *,
    condition: str,
    row: dict[str, Any],
    client: VLLMClient,
    database: Path,
    search_index: SchemaSearchIndex,
    anchor_sql: str,
    auxiliary_raw_sql: str | None = None,
    max_turns: int = 4,
    max_actions: int = 8,
    max_sql_executions: int = 3,
    initial_schema_top_k: int = 12,
    tools_factory: Callable[
        [Path, str, SchemaSearchIndex], SQLiteAgentTools
    ]
    | None = None,
    sql_dialect: str = "SQLite",
    evolution_mapping: RelationEvolutionMapping | None = None,
    compose_history: bool = False,
    bind_history: bool = False,
    plan_history: bool = False,
    scope_history: bool = False,
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
    lower_eligibility_revision: bool = False,
) -> dict[str, Any]:
    """Run the only unified main without a score gate, selector, or fallback."""

    if lower_eligibility_revision and not entity_grain_revision:
        raise ValueError("Eligibility lowering requires frozen v14 main configuration")
    if condition not in SUPPORTED_MAIN_CONDITIONS:
        raise ValueError(f"unsupported unified-main condition: {condition}")
    if (plan_history or scope_history) and (compose_history or bind_history):
        raise ValueError('contract planning and the older free SQL composer are separate candidates')
    if not str(anchor_sql or "").strip():
        raise ValueError("unified main requires the frozen first-stage anchor SQL")
    result = run_react_text2sql(
        condition=condition,
        row=row,
        client=client,
        database=database,
        search_index=search_index,
        max_turns=max_turns,
        max_actions=max_actions,
        max_sql_executions=max_sql_executions,
        initial_schema_top_k=initial_schema_top_k,
        tools_factory=tools_factory,
        sql_dialect=sql_dialect,
        method_id_override=GRAPH_EVO_SEMANTIC_PROGRAM_MAIN,
        anchor_sql=anchor_sql,
        auxiliary_raw_sql=auxiliary_raw_sql,
        inject_graph_evo_context=True,
        realize_submitted_program=True,
        fixed_sql_consumer=True,
        performance_first_raw_backbone=auxiliary_raw_sql is not None,
        evolution_mapping=evolution_mapping,
        evidence_first_history=evidence_first_history,
        realize_semantic_revision=realize_semantic_revision,
        scope_grounded_revision=scope_grounded_revision,
        witness_consistent_revision=witness_consistent_revision,
        grounded_binding_revision=grounded_binding_revision,
        realized_edit_revision=realized_edit_revision,
        physical_execution_python=physical_execution_python,
        scope_faithful_revision=scope_faithful_revision,
        relational_grain_revision=relational_grain_revision,
        entity_grain_revision=entity_grain_revision,
        semantic_memory=semantic_memory,
        retrieval_snapshot=retrieval_snapshot,
    )
    if compose_history or plan_history or scope_history:
        import copy
        import time
        from types import SimpleNamespace
        from finsemguard.e2e.sql_history_composer import compose_sql_history
        from finsemguard.e2e.sql_contract_plan import plan_sql_history
        from finsemguard.e2e.sql_contract_scope import plan_scoped_sql_history
        composition_started = time.perf_counter()
        factory = tools_factory or SQLiteAgentTools
        tools = factory(database, str(row["database_id"]), search_index)
        reranker = (SimpleNamespace(score=search_index.rerank_documents)
                    if search_index.rerank_documents else None)
        composition_client = copy.copy(client)
        composition_client.max_tokens = 3000 if plan_history or scope_history else 2400
        composer = plan_scoped_sql_history if scope_history else plan_sql_history if plan_history else compose_sql_history
        sql, composition = composer(
            question=str(row["question"]), proposal_sql=result["sql"],
            react=result["react"], documents=search_index.documents,
            tools=tools, client=composition_client, dialect=sql_dialect, reranker=reranker,
        )
        result["sql"] = sql
        result["react"]["sql_history_contract_plan" if plan_history or scope_history else "sql_history_composition"] = composition
        elapsed = time.perf_counter() - composition_started
        result["composition_latency_seconds"] = elapsed
        result["latency_seconds"] = result.get("latency_seconds", 0) + elapsed
        if isinstance(result.get("audit"), dict):
            audit = result["audit"]
            audit.setdefault("usage", []).append(composition["usage"])
            audit["model_calls"] = audit.get("model_calls", 0) + 1
            audit["known_total_tokens"] = audit.get("known_total_tokens", 0) + (composition["usage"].get("total_tokens") or 0)
        if composition["accepted"]:
            result["execution_probe"] = {"executable": True,
                "validation": {"valid": True, "composition_executed": True}}
        if bind_history:
            from finsemguard.e2e.sql_composition_binding import bind_composed_result
            result = bind_composed_result(result, tools, sql_dialect)
    if result.get("method_id") != GRAPH_EVO_SEMANTIC_PROGRAM_MAIN:
        raise RuntimeError("unified main method identity drifted")
    # Expose one semantic method identity at the artifact boundary.  The
    # legacy condition is retained only as an implementation detail so old
    # prompt/index plumbing cannot silently rename the paper method.
    result["method_revision"] = "ontology_entity_grain_v14" if entity_grain_revision else "ontology_relational_grain_v13" if relational_grain_revision else "ontology_scope_faithful_v11" if scope_faithful_revision else "ontology_realized_edits_v10" if realized_edit_revision else "ontology_grounded_binding_v9" if grounded_binding_revision else "ontology_witness_consistent_v8" if witness_consistent_revision else "ontology_scope_grounded_v7" if scope_grounded_revision else "ontology_semantic_revision_v5" if realize_semantic_revision else "ontology_evidence_first_v2" if evidence_first_history else "frozen_v1"
    result["generator_condition"] = condition
    result["asset_condition"] = GRAPH_EVO_SEMANTIC_PROGRAM_MAIN
    if lower_eligibility_revision:
        from .relational_program_compiler import lower_result_eligibility
        result = lower_result_eligibility(result, database)
    if semantic_memory is not None:
        result["method_revision"] = "v17_joint_contract_closure_20261014"
        result["semantic_memory_revision"] = semantic_memory["ontology_revision"]
    return result
