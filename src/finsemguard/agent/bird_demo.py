from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from finsemguard.agent.llm import VLLMClient
from finsemguard.config import load_config, project_path
from finsemguard.contracts import AgentDecision, AgentTrace, SemanticPlan
from finsemguard.data.bird import database_path
from finsemguard.retrieval.bm25 import BM25Index
from finsemguard.sql import execute_preview


SYSTEM_PROMPT = """You are a selective financial Text-to-SQL planner for one BIRD SQLite database.
Use only the supplied evidence and never invent a table, column, relationship, or literal meaning.
The benchmark_hint is a trusted expert annotation: apply every explicit column/value mapping in it
without asking the user to reconfirm it. The database name is context, not a SQL schema name; use
bare SQLite table names and never prefix a table with the database id.
Return one JSON object with decision (answer|clarify|abstain), semantic_plan, sql,
clarification, and answer. semantic_plan must contain intent, measures, dimensions,
filters, time_range, grain, join_path, evidence_ids, assumptions, missing_slots, and risk_flags.
SQL must be a single read-only SQLite SELECT. If essential evidence is absent or conflicting,
clarify or abstain and set sql to null. Do not clarify when the full supplied schema and trusted
hint already make the query answerable. Do not include markdown or hidden reasoning."""


_INDEX: BM25Index | None = None


def load_question(path: Path, question_id: str) -> dict[str, Any]:
    for line in path.read_text(encoding="utf-8").splitlines():
        row = json.loads(line)
        if row["question_id"] == question_id or str(row["source_question_id"]) == question_id:
            return row
    raise KeyError(f"BIRD question not found: {question_id}")


def _run(
    question: str,
    db_id: str,
    *,
    trusted_benchmark_hint: str = "",
    config_path: str | Path | None = None,
) -> AgentTrace:
    global _INDEX
    config = load_config(config_path)
    if _INDEX is None:
        _INDEX = BM25Index.load(project_path(config["paths"]["bird_bm25_index"]))
    ranked = _INDEX.search(
        question,
        top_k=int(config["retrieval"]["top_k"]),
        document_filter=lambda document: document.get("metadata", {}).get("db_id") == db_id,
    )
    # BIRD dev databases are narrow: financial has 71 schema/relationship
    # documents (~3K tokens). Keep the relevant ranking first, then append the
    # complete schema instead of pruning a required column. Query patterns stay
    # retrieval-only so train databases still have a bounded context.
    retrieved = list(ranked)
    seen = {item["document"]["doc_id"] for item in retrieved}
    for document in _INDEX.documents:
        if document.get("metadata", {}).get("db_id") != db_id:
            continue
        if document["kind"] == "query_pattern" or document["doc_id"] in seen:
            continue
        retrieved.append({"score": 0.0, "document": document})
        seen.add(document["doc_id"])
    compact = [
        {
            "doc_id": item["document"]["doc_id"],
            "kind": item["document"]["kind"],
            "name": item["document"]["name"],
            "text": item["document"]["text"],
            "score": item["score"],
            "split_origin": item["document"]["split_origin"],
        }
        for item in retrieved
    ]
    llm = VLLMClient(config["llm"])
    if not llm.healthy():
        return AgentTrace(
            question=question,
            decision=AgentDecision.ABSTAIN,
            retrieval=compact,
            answer="Local vLLM is unavailable; retrieval evidence is ready.",
            validator={"valid": False, "reason": "llm_unavailable"},
            model=config["llm"]["model"],
        )

    payload = llm.chat_json(
        SYSTEM_PROMPT,
        json.dumps(
            {
                "database": db_id,
                "question": question,
                "benchmark_hint": trusted_benchmark_hint,
                "evidence": compact,
            },
            ensure_ascii=False,
        ),
    )
    try:
        decision = AgentDecision(payload.get("decision", "abstain"))
    except ValueError:
        decision = AgentDecision.ABSTAIN
    plan_data = payload.get("semantic_plan")
    plan = SemanticPlan.model_validate(plan_data) if plan_data else None
    sql = payload.get("sql")
    validator: dict[str, Any] = {}
    preview: dict[str, Any] = {}
    db_root = project_path(config["paths"]["bird_dev_databases"])
    sqlite_path = database_path(db_root, db_id)
    if decision == AgentDecision.ANSWER and sql:
        if sqlite_path is None:
            decision = AgentDecision.ABSTAIN
            validator = {"valid": False, "reason": "database_unavailable", "db_id": db_id}
        else:
            try:
                preview = execute_preview(
                    sqlite_path,
                    sql,
                    int(config["sql"]["max_rows"]),
                    float(config["sql"]["timeout_seconds"]),
                )
                validator = preview.pop("validation")
            except Exception as error:
                decision = AgentDecision.ABSTAIN
                validator = {
                    "valid": False,
                    "reason": type(error).__name__,
                    "detail": str(error),
                }
                preview = {}
    return AgentTrace(
        question=question,
        decision=decision,
        retrieval=compact,
        semantic_plan=plan,
        sql=sql,
        validator=validator,
        preview=preview,
        clarification=payload.get("clarification"),
        answer=payload.get("answer"),
        model=config["llm"]["model"],
    )


def run(
    question: str,
    db_id: str,
    *,
    config_path: str | Path | None = None,
) -> AgentTrace:
    """Public demo entry point: callers cannot inject trusted annotations."""
    return _run(question, db_id, config_path=config_path)


def run_benchmark(
    question: str,
    db_id: str,
    benchmark_hint: str,
    *,
    config_path: str | Path | None = None,
) -> AgentTrace:
    """Evaluation-only entry point for dataset-owned benchmark annotations."""
    return _run(
        question,
        db_id,
        trusted_benchmark_hint=benchmark_hint,
        config_path=config_path,
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--question-id", default="bird_dev_90")
    parser.add_argument("--question")
    parser.add_argument("--db-id")
    parser.add_argument("--config")
    args = parser.parse_args()
    config = load_config(args.config)
    if args.question:
        if not args.db_id:
            parser.error("--db-id is required with --question")
        question, db_id, evidence_hint = args.question, args.db_id, ""
    else:
        record = load_question(
            project_path(config["paths"]["bird_dev_questions"]), args.question_id
        )
        question, db_id, evidence_hint = (
            record["question"],
            record["db_id"],
            record.get("evidence", ""),
        )
    trace = (
        run_benchmark(question, db_id, evidence_hint, config_path=args.config)
        if evidence_hint
        else run(question, db_id, config_path=args.config)
    )
    print(trace.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
