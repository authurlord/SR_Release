"""Semantic method identities for the active SchemaRecovery research line.

Historical result directories retain their immutable numeric suffixes.  New code,
reports, and handoffs use capability-bearing identifiers so a reader can understand
the method without reconstructing the experiment chronology.
"""

from __future__ import annotations


ANCHORED_RECOVERY_ONTOLOGY_PROGRAM_GRAPH = (
    "schema_recovery_ontology__anchored_program_graph"
)
CARDINALITY_AWARE_RELATION_REPAIR = (
    "schema_recovery_ontology__cardinality_aware_relation_repair"
)
EVOLUTION_AWARE_RELATION_REPAIR = (
    "schema_recovery_ontology__evolution_aware_relation_repair"
)
EVOLUTION_AWARE_RELATIONAL_PROGRAM_GRAPH = (
    "schema_recovery_ontology__evolution_aware_relational_program_graph"
)
EVOLUTION_AWARE_RELATIONAL_PROGRAM_COMPILER = (
    "schema_recovery_ontology__evolution_aware_relational_program_compiler"
)
GRAPH_EVO_SEMANTIC_PROGRAM_MAIN = "graph_evo_semantic_program_main_v1"


LEGACY_METHOD_ALIASES = {
    "react_text2sql_v6__anchored_relational_program_graph": (
        ANCHORED_RECOVERY_ONTOLOGY_PROGRAM_GRAPH
    ),
    "react_text2sql_v8__anchored_cardinality_aware_minimal_join_tree": (
        CARDINALITY_AWARE_RELATION_REPAIR
    ),
}


def canonical_method_id(method_id: str) -> str:
    """Return the semantic identity while preserving unknown historical IDs."""

    return LEGACY_METHOD_ALIASES.get(method_id, method_id)
