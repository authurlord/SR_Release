"""Performance-first paired Text-to-SQL pipeline for masked SQLite schemas."""

from __future__ import annotations

from collections import defaultdict, deque
from concurrent.futures import ThreadPoolExecutor, as_completed
from hashlib import sha256
import json
from pathlib import Path
import sqlite3
import threading
import time
from typing import Any

from finsemguard.agent.llm import VLLMClient
from finsemguard.e2e.livesqlbench import CatalogDocument
from finsemguard.e2e.operational_ontology import OperationalOntology
from finsemguard.e2e.livesqlbench_runner import (
    _build_embeddings,
    _canonical_hash,
    _dense_rank,
    _generation_cost_audit,
    _lexical_rank,
    _load_jsonl,
    _normalize_decision,
    _rrf,
    _select,
    _serialize_context,
    _write_atomic,
)
from finsemguard.e2e.sqlite_catalog import load_catalog, schema_key
from finsemguard.e2e.sqlite_runner import _validate_sql
from finsemguard.schema_recovery.performance_recover import (
    compile_performance_overlay,
)


METHOD_IDS = {
    "A0": "rrce_v1__a0_physical_raw_union_retrieval",
    "A5": "rrce_v1__a5_multiview_recovery_union_graph",
    "A6": "rrce_v2__schema_recovery_operational_ontology",
}
SELECTOR_SYSTEM = """You are the recall-oriented schema linker in a Text-to-SQL system.
First infer the question's requested outputs, filters/literals, aggregation, grouping,
ordering, and possible join endpoints. Then select a sufficient set of handles from the
manifest. Recovered aliases are soft mapping hypotheses; physical identifiers and DDL
remain authoritative. Preserve plausible alternatives when a masked name is ambiguous.
Include the tables/columns needed for every role and likely join path. Call
select_semantic_subgraph exactly once. Stay within the provided handles and budget."""

SQL_SYSTEM = """You are a performance-oriented SQLite Text-to-SQL generator. Return one
JSON object with exactly decision, sql, clarification, and answer. Use only physical
tables, columns, keys, values, and mapping hints explicitly supplied in the semantic
subgraph. Entries named performance_recovery_index are soft retrieval aliases; they may
map question wording to the labeled physical identifier, but never replace that physical
identifier in SQL. Always produce the best-supported read-only SQLite SELECT/WITH query
when the physical schema can express the request. Do not abstain merely because an alias
is uncertain. Preserve requested projection, filters, aggregation, grouping, ordering,
and result shape. Set decision to answer and sql to one statement without markdown.
Clarify or abstain only when no supplied physical schema path can express the request."""

REPAIR_SYSTEM = """Repair one SQLite query using only the supplied semantic subgraph and
the bounded parser/executor feedback. Return one JSON object with exactly decision, sql,
clarification, and answer. Produce exactly one read-only SELECT/WITH query without
markdown. Use physical identifiers in SQL; recovered aliases are mapping hints only.
Change only what is necessary to make the best-supported query valid and executable."""


def _documents_by_database(
    documents: list[CatalogDocument],
) -> dict[str, list[CatalogDocument]]:
    output: dict[str, list[CatalogDocument]] = defaultdict(list)
    for document in documents:
        output[document.database_id].append(document)
    return dict(output)


def _take_by_kind(
    ranking: list[str],
    documents: dict[str, CatalogDocument],
    limits: dict[str, int],
) -> list[str]:
    counts: dict[str, int] = defaultdict(int)
    output: list[str] = []
    for candidate_id in ranking:
        kind = documents[candidate_id].kind
        if kind not in limits or counts[kind] >= limits[kind]:
            continue
        output.append(candidate_id)
        counts[kind] += 1
    return output


def dual_view_candidate_pool(
    *,
    question: str,
    raw_documents: list[CatalogDocument],
    semantic_documents: list[CatalogDocument],
    raw_vectors: dict[str, Any],
    semantic_vectors: dict[str, Any],
    query_vector: Any,
) -> tuple[list[CatalogDocument], dict[str, Any]]:
    """Union raw anchors with semantic candidates; semantic IDs may enter top-k."""

    raw_by_id = {row.candidate_id: row for row in raw_documents}
    semantic_by_id = {row.candidate_id: row for row in semantic_documents}
    if not set(raw_by_id).issubset(semantic_by_id):
        missing = sorted(set(raw_by_id) - set(semantic_by_id))[:5]
        raise ValueError(
            "semantic view is missing physical candidate IDs: " + ", ".join(missing)
        )
    raw_ranking = _rrf(
        _dense_rank(query_vector, raw_documents, raw_vectors),
        _lexical_rank(question, raw_documents),
    )
    semantic_ranking = _rrf(
        _dense_rank(query_vector, semantic_documents, semantic_vectors),
        _lexical_rank(question, semantic_documents),
    )
    final_limits = {"table": 16, "column": 56, "knowledge": 8}
    guaranteed_raw = _take_by_kind(
        raw_ranking,
        raw_by_id,
        {"table": 8, "column": 20, "knowledge": 4},
    )
    guaranteed_semantic = _take_by_kind(
        semantic_ranking,
        semantic_by_id,
        {"table": 12, "column": 40, "knowledge": 6},
    )
    fused = _rrf(semantic_ranking, raw_ranking)
    ordered_ids: list[str] = []
    for sequence in (guaranteed_raw, guaranteed_semantic, fused):
        for candidate_id in sequence:
            if candidate_id not in ordered_ids:
                ordered_ids.append(candidate_id)
    selected_ids = _take_by_kind(ordered_ids, semantic_by_id, final_limits)

    # Make table-first and column-first retrieval additive: parent tables and
    # declared FK neighbors enter the manifest even if they ranked below top-k.
    selected = set(selected_ids)
    for candidate_id in list(selected_ids):
        document = semantic_by_id[candidate_id]
        if document.table:
            table_id = f"table::{document.database_id}::{document.table}"
            if table_id in semantic_by_id:
                selected.add(table_id)
    for candidate_id in list(selected):
        document = semantic_by_id[candidate_id]
        if document.kind != "table":
            continue
        for reference in document.references:
            reference_id = f"table::{document.database_id}::{reference}"
            if reference_id in semantic_by_id:
                selected.add(reference_id)
    order = {candidate_id: index for index, candidate_id in enumerate(ordered_ids)}
    candidates = sorted(
        (semantic_by_id[candidate_id] for candidate_id in selected),
        key=lambda row: (order.get(row.candidate_id, 10**9), row.candidate_id),
    )
    raw_top = set(guaranteed_raw)
    semantic_only = [
        candidate_id for candidate_id in selected_ids if candidate_id not in raw_top
    ]
    return candidates, {
        "raw_ranking_top_ids": raw_ranking[:20],
        "semantic_ranking_top_ids": semantic_ranking[:20],
        "semantic_nonanchor_entries": semantic_only,
        "semantic_nonanchor_entry_count": len(semantic_only),
    }


def _shortest_path(
    adjacency: dict[str, set[str]], start: str, goal: str
) -> list[str]:
    if start == goal:
        return [start]
    queue: deque[tuple[str, list[str]]] = deque([(start, [start])])
    visited = {start}
    while queue:
        node, path = queue.popleft()
        for neighbor in sorted(adjacency.get(node, set())):
            if neighbor in visited:
                continue
            if neighbor == goal:
                return [*path, neighbor]
            visited.add(neighbor)
            queue.append((neighbor, [*path, neighbor]))
    return []


def graph_complete_context(
    selected_ids: list[str],
    candidates: list[CatalogDocument],
    all_documents: dict[str, CatalogDocument],
) -> tuple[list[CatalogDocument], list[str]]:
    """Add parents and undirected shortest FK bridges between selected tables."""

    selected = {
        candidate_id for candidate_id in selected_ids if candidate_id in all_documents
    }
    table_ids: set[str] = set()
    database_ids = {
        all_documents[candidate_id].database_id for candidate_id in selected
    }
    if len(database_ids) > 1:
        raise ValueError("one query selected documents from multiple schema contexts")
    for candidate_id in list(selected):
        document = all_documents[candidate_id]
        if document.kind == "table":
            table_ids.add(candidate_id)
        elif document.table:
            table_id = f"table::{document.database_id}::{document.table}"
            if table_id in all_documents:
                selected.add(table_id)
                table_ids.add(table_id)
    adjacency: dict[str, set[str]] = defaultdict(set)
    for candidate_id, document in all_documents.items():
        if document.kind != "table" or document.database_id not in database_ids:
            continue
        for reference in document.references:
            target = f"table::{document.database_id}::{reference}"
            if target in all_documents:
                adjacency[candidate_id].add(target)
                adjacency[target].add(candidate_id)
    bridges: set[str] = set()
    ordered_tables = sorted(table_ids)
    if ordered_tables:
        root = ordered_tables[0]
        for target in ordered_tables[1:]:
            path = _shortest_path(adjacency, root, target)
            for table_id in path:
                if table_id not in selected:
                    bridges.add(table_id)
                    selected.add(table_id)
    candidate_order = {
        document.candidate_id: index for index, document in enumerate(candidates)
    }
    closed = sorted(
        (all_documents[candidate_id] for candidate_id in selected),
        key=lambda row: (
            candidate_order.get(row.candidate_id, 10**9),
            row.candidate_id,
        ),
    )
    return closed, sorted(bridges)


def _database_path(data_root: Path, row: dict[str, Any]) -> Path:
    target = data_root / str(row["database_or_answer_target"])
    if target.is_file():
        return target.resolve()
    candidate = target / f"{row['database_id']}.sqlite"
    if not candidate.is_file():
        raise FileNotFoundError(f"SQLite database not found: {candidate}")
    return candidate.resolve()


def execution_probe(
    database: Path, sql: str | None, timeout_seconds: float = 5.0
) -> dict[str, Any]:
    validation = _validate_sql(sql)
    if not validation.get("valid") or not sql:
        return {"executable": False, "validation": validation}
    connection = sqlite3.connect(f"file:{database}?mode=ro", uri=True)
    deadline = time.monotonic() + timeout_seconds
    connection.set_progress_handler(
        lambda: 1 if time.monotonic() > deadline else 0, 1000
    )
    try:
        cursor = connection.execute(sql)
        cursor.fetchone()
        return {"executable": True, "validation": validation}
    except Exception as error:
        return {
            "executable": False,
            "validation": validation,
            "error_type": type(error).__name__,
            "error": str(error)[:500],
        }
    finally:
        connection.close()


def _prediction_sql(prediction: dict[str, Any]) -> tuple[str | None, str]:
    sql = prediction.get("sql")
    sql = str(sql).strip() if sql else None
    decision = _normalize_decision(
        prediction.get("decision"), sql, prediction.get("clarification")
    )
    return sql, decision


def run_condition(
    *,
    condition: str,
    row: dict[str, Any],
    client: VLLMClient,
    data_root: Path,
    raw_documents: list[CatalogDocument],
    semantic_documents: list[CatalogDocument],
    raw_vectors: dict[str, Any],
    semantic_vectors: dict[str, Any],
    query_vector: Any,
    enable_repair: bool = True,
    ontology: OperationalOntology | None = None,
) -> dict[str, Any]:
    if condition not in METHOD_IDS:
        raise ValueError(f"unknown performance condition: {condition}")
    if condition == "A6" and ontology is None:
        raise ValueError("A6 requires an operational ontology")
    started = time.perf_counter()
    question = str(row["question"])
    all_documents = {document.candidate_id: document for document in semantic_documents}
    candidates, retrieval_audit = dual_view_candidate_pool(
        question=question,
        raw_documents=raw_documents,
        semantic_documents=semantic_documents,
        raw_vectors=raw_vectors,
        semantic_vectors=semantic_vectors,
        query_vector=query_vector,
    )
    retrieved_evidence_ids: list[str] = []
    prebound_ids: list[str] = []
    if ontology is not None:
        candidates, retrieved_evidence_ids, prebound_ids = (
            ontology.prebind_retrieved_evidence(
                context=schema_key(row),
                candidates=candidates,
                all_documents=all_documents,
            )
        )
    selected, selector_usage, selector_hash = _select(
        client,
        question,
        candidates,
        system_prompt=SELECTOR_SYSTEM,
        max_items=40,
    )
    ontology_audit: dict[str, Any] | None = None
    if ontology is None:
        closed, bridge_ids = graph_complete_context(
            selected, candidates, all_documents
        )
    else:
        closed, ontology_expansion = ontology.expand_documents(
            context=schema_key(row),
            selected_ids=list(dict.fromkeys([*selected, *retrieved_evidence_ids])),
            all_documents=all_documents,
        )
        bridge_ids = [
            f"table::{schema_key(row)}::{table}"
            for table in ontology_expansion.bridge_tables
        ]
        ontology_audit = ontology_expansion.audit()
    context = _serialize_context(closed, budget_tokens=16384)
    user_payload = {
        "dataset": row["dataset_id"],
        "database": row["database_id"],
        "upstream_split": row["upstream_split"],
        "question": question,
        "semantic_subgraph": context,
    }
    prediction, sql_usage = client.chat_json_with_metadata(
        SQL_SYSTEM, json.dumps(user_payload, ensure_ascii=False)
    )
    initial_sql, decision = _prediction_sql(prediction)
    database = _database_path(data_root, row)
    initial_probe = execution_probe(database, initial_sql)
    final_sql = initial_sql
    final_prediction = prediction
    final_probe = initial_probe
    repair_usage: dict[str, Any] | None = None
    repair_hash: str | None = None
    if enable_repair and not initial_probe["executable"]:
        repair_payload = {
            **user_payload,
            "failed_sql": initial_sql,
            "feedback": {
                key: value
                for key, value in initial_probe.items()
                if key in {"validation", "error_type", "error"}
            },
        }
        repaired, repair_usage = client.chat_json_with_metadata(
            REPAIR_SYSTEM, json.dumps(repair_payload, ensure_ascii=False)
        )
        repaired_sql, repaired_decision = _prediction_sql(repaired)
        repaired_probe = execution_probe(database, repaired_sql)
        repair_hash = _canonical_hash(
            {"system": REPAIR_SYSTEM, "user": repair_payload}
        )
        if repaired_probe["executable"]:
            final_sql = repaired_sql
            decision = repaired_decision
            final_prediction = repaired
            final_probe = repaired_probe
    usage_rows = [selector_usage, sql_usage]
    if repair_usage is not None:
        usage_rows.append(repair_usage)
    generation_cost = _generation_cost_audit(usage_rows)
    return {
        "example_id": row["example_id"],
        "dataset_id": row["dataset_id"],
        "upstream_split": row["upstream_split"],
        "database_id": row["database_id"],
        "method_id": METHOD_IDS[condition],
        "asset_condition": condition,
        "decision": decision,
        "sql": final_sql,
        "clarification": final_prediction.get("clarification"),
        "answer": final_prediction.get("answer"),
        "validation": _validate_sql(final_sql),
        "execution_probe": final_probe,
        "pre_repair": {
            "sql": initial_sql,
            "decision": _prediction_sql(prediction)[1],
            "execution_probe": initial_probe,
        },
        "repair_attempted": repair_usage is not None,
        "repair_adopted": final_sql != initial_sql,
        "context": {
            "candidate_count": len(candidates),
            "selected_ids": selected,
            "closed_ids": [document.candidate_id for document in closed],
            "bridge_ids": bridge_ids,
            "serialized_chars": len(context),
            "serialized_token_estimate": (len(context) + 3) // 4,
            "ontology": ontology_audit,
            "retrieved_evidence_ids": retrieved_evidence_ids,
            "prebound_ids": prebound_ids,
            **retrieval_audit,
        },
        "audit": {
            **generation_cost,
            "selector_usage": selector_usage,
            "sql_usage": sql_usage,
            "repair_usage": repair_usage,
            "prompt_sha256": {
                "selector": selector_hash,
                "sql_agent": _canonical_hash(
                    {"system": SQL_SYSTEM, "user": user_payload}
                ),
                "repair": repair_hash,
            },
        },
        "latency_seconds": round(time.perf_counter() - started, 6),
    }


def run_paired_study(
    *,
    rows: list[dict[str, Any]],
    client: VLLMClient,
    data_root: Path,
    raw_documents: list[CatalogDocument],
    recovered_documents: list[CatalogDocument],
    raw_vectors: dict[str, Any],
    recovered_vectors: dict[str, Any],
    query_vectors: dict[str, Any],
    output_root: Path,
    concurrency: int = 4,
    resume: bool = False,
) -> dict[str, list[dict[str, Any]]]:
    if concurrency < 1:
        raise ValueError("concurrency must be positive")
    output_root.mkdir(parents=True, exist_ok=True)
    paths = {
        "A0": output_root / "A0_physical_raw.jsonl",
        "A5": output_root / "A5_recovered_union_graph.jsonl",
    }
    if not resume and any(path.exists() for path in paths.values()):
        raise FileExistsError("paired output exists; use --resume or a new output root")
    completed: dict[str, dict[str, dict[str, Any]]] = {}
    for condition, path in paths.items():
        prior = _load_jsonl(path) if resume and path.is_file() else []
        completed[condition] = {
            str(row["example_id"]): row
            for row in prior
            if row.get("status") != "error"
        }
    raw_by_db = _documents_by_database(raw_documents)
    recovered_by_db = _documents_by_database(recovered_documents)
    lock = threading.Lock()

    def run_row(row: dict[str, Any]) -> dict[str, dict[str, Any]]:
        example_id = str(row["example_id"])
        key = schema_key(row)
        order = ["A0", "A5"]
        if sha256(example_id.encode()).digest()[0] % 2:
            order.reverse()
        results: dict[str, dict[str, Any]] = {}
        for condition in order:
            if example_id in completed[condition]:
                continue
            try:
                semantic_docs = raw_by_db[key] if condition == "A0" else recovered_by_db[key]
                semantic_vectors = raw_vectors if condition == "A0" else recovered_vectors
                results[condition] = run_condition(
                    condition=condition,
                    row=row,
                    client=client,
                    data_root=data_root,
                    raw_documents=raw_by_db[key],
                    semantic_documents=semantic_docs,
                    raw_vectors=raw_vectors,
                    semantic_vectors=semantic_vectors,
                    query_vector=query_vectors[example_id],
                )
            except Exception as error:
                results[condition] = {
                    "example_id": example_id,
                    "dataset_id": row["dataset_id"],
                    "upstream_split": row["upstream_split"],
                    "database_id": row["database_id"],
                    "method_id": METHOD_IDS[condition],
                    "asset_condition": condition,
                    "status": "error",
                    "error_type": type(error).__name__,
                    "error": str(error)[:1000],
                }
        return results

    pending = [
        row
        for row in rows
        if any(str(row["example_id"]) not in completed[condition] for condition in paths)
    ]
    with ThreadPoolExecutor(max_workers=concurrency) as executor:
        futures = {executor.submit(run_row, row): row for row in pending}
        for index, future in enumerate(as_completed(futures), start=1):
            row_results = future.result()
            with lock:
                for condition, result in row_results.items():
                    completed[condition][str(result["example_id"])] = result
                    with paths[condition].open("a", encoding="utf-8") as handle:
                        handle.write(json.dumps(result, ensure_ascii=False) + "\n")
            print(
                f"[paired {index}/{len(futures)}] {futures[future]['example_id']} "
                + " ".join(
                    f"{condition}={'error' if result.get('status') == 'error' else 'ok'}"
                    for condition, result in sorted(row_results.items())
                ),
                flush=True,
            )
    ordered: dict[str, list[dict[str, Any]]] = {}
    for condition, path in paths.items():
        ordered[condition] = [
            completed[condition][str(row["example_id"])] for row in rows
        ]
        _write_atomic(path, ordered[condition])
    return ordered
