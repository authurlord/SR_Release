"""Outcome-free reuse of a frozen, already materialized retrieval boundary."""
from copy import deepcopy
from finsemguard.schema_recovery.joint import digest


def input_identity(row, anchor_sql, raw_sql):
    return digest({"example_id": row["example_id"], "database_id": row["database_id"],
        "question": str(row.get("source_question") or row["question"]),
        "evidence": str(row.get("benchmark_evidence") or ""),
        "anchor_sql": anchor_sql, "raw_sql": raw_sql})


def validate_snapshot(snapshot, row, anchor_sql, raw_sql):
    if set(snapshot) - {"example_id", "input_identity", "initial_search_query", "initial_search", "exact_value_matches", "provenance"}:
        raise ValueError("retrieval cache contains non-retrieval fields")
    if snapshot["input_identity"] != input_identity(row, anchor_sql, raw_sql):
        raise ValueError("retrieval cache input mismatch")
    if snapshot["example_id"] != row["example_id"]:
        raise ValueError("retrieval cache identity mismatch")
    return deepcopy(snapshot)
