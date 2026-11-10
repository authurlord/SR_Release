#!/usr/bin/env python3
"""Run budget-matched opaque-schema ReACT with and without history/KB ontology."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from hashlib import sha256
import json
from pathlib import Path
from threading import Lock
from typing import Any

from finsemguard.agent.llm import VLLMClient
from finsemguard.config import load_config
from finsemguard.e2e.graph_evo_main import (
    run_graph_evo_semantic_program_main,
)
from finsemguard.e2e.livesqlbench_runner import _load_jsonl, _write_atomic
from finsemguard.e2e.method_identity import (
    EVOLUTION_AWARE_RELATIONAL_PROGRAM_COMPILER,
    GRAPH_EVO_SEMANTIC_PROGRAM_MAIN,
)
from finsemguard.e2e.operational_ontology import OperationalOntology
from finsemguard.e2e.performance_pipeline import _database_path
from finsemguard.e2e.react_text2sql import (
    METHOD_IDS,
    SchemaSearchIndex,
    _minimal_join_tree_role_phrases,
    _query_role_phrases,
    build_recovery_documents,
    run_react_text2sql,
)
from finsemguard.e2e.sqlite_catalog import load_catalog
from finsemguard.retrieval.reranker import VLLMRerankerClient
from run_bird_react_recovery import BGEEncoder


DEFAULT_CONDITIONS = ("opaque_react", "ontology_react")
SUPPORTED_CONDITIONS = (
    "opaque_react",
    "recovery_only_react",
    "ontology_react",
    "program_graph_react",
    "minimal_join_tree_react",
    "chess_react",
    "autolink_react",
    GRAPH_EVO_SEMANTIC_PROGRAM_MAIN,
)

BASE_ANCHORED_RELATIONAL_PROGRAM_METHOD_ID = (
    EVOLUTION_AWARE_RELATIONAL_PROGRAM_COMPILER
)
RELATIONAL_PROGRAM_CONDITIONS = {
    "program_graph_react",
    "minimal_join_tree_react",
    GRAPH_EVO_SEMANTIC_PROGRAM_MAIN,
}


def _declared_method_id(condition: str, *, anchored: bool) -> str:
    if condition == GRAPH_EVO_SEMANTIC_PROGRAM_MAIN:
        return GRAPH_EVO_SEMANTIC_PROGRAM_MAIN
    if anchored:
        return BASE_ANCHORED_RELATIONAL_PROGRAM_METHOD_ID
    return METHOD_IDS[condition]


def _write_json(path: Path, value: dict[str, Any]) -> None:
    content = json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if path.exists():
        if path.read_text(encoding="utf-8") != content:
            raise FileExistsError(f"refusing to overwrite different artifact: {path}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(content, encoding="utf-8")
    temporary.replace(path)


def _strip_lean_metadata(value: Any) -> Any:
    """Remove bulky audit/checksum fields from active prediction artifacts."""

    if isinstance(value, dict):
        return {
            key: _strip_lean_metadata(item)
            for key, item in value.items()
            if "sha256" not in key.casefold()
            and "hash" not in key.casefold()
            and "fingerprint" not in key.casefold()
            and "audit" not in key.casefold()
        }
    if isinstance(value, list):
        return [_strip_lean_metadata(item) for item in value]
    return value


def _select(
    rows: list[dict[str, Any]], example_ids: list[str], subset_size: int
) -> list[dict[str, Any]]:
    if example_ids:
        requested = set(example_ids)
        selected = [row for row in rows if str(row["example_id"]) in requested]
        if {str(row["example_id"]) for row in selected} != requested:
            raise ValueError("one or more requested example IDs are absent")
        return selected
    return sorted(
        rows,
        key=lambda row: sha256(
            f"ontology-react-pilot-v1:{row['example_id']}".encode()
        ).digest(),
    )[:subset_size]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset-id", choices=["fiben", "bird", "kaggledbqa", "dr_spider"], required=True)
    parser.add_argument("--data-root", type=Path, required=True)
    parser.add_argument("--online", type=Path, required=True)
    parser.add_argument("--table-inputs", type=Path, required=True)
    parser.add_argument("--recovery", type=Path, required=True)
    parser.add_argument("--knowledge", type=Path)
    parser.add_argument("--workload-semantic-state", type=Path,
                        help="Persistent SQL-only semantic layer for the main method")
    parser.add_argument("--compose-history", action="store_true",
                        help="Compose SQL-derived computations into the main submission")
    parser.add_argument("--bind-history", action="store_true",
                        help="Compose and realize history computations against physical value domains")
    parser.add_argument("--plan-history", action="store_true",
                        help="Compile a structured history-contract stage plan after the existing main")
    parser.add_argument("--scope-history", action="store_true",
                        help="Instantiate history roles, predicates and grain before stage composition")
    parser.add_argument("--embedding-model", type=Path, required=True)
    parser.add_argument("--embedding-cache", type=Path, required=True)
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument(
        "--llm-base-url",
        action="append",
        default=[],
        help=(
            "OpenAI-compatible generation endpoint. Repeat to distribute rows "
            "round-robin across identical model servers."
        ),
    )
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument(
        "--lean",
        action="store_true",
        help=(
            "Disable API audit logging and omit checksum/audit fields from the "
            "active prediction artifacts."
        ),
    )
    parser.add_argument("--subset-size", type=int, default=10)
    parser.add_argument("--example-id", action="append", default=[])
    parser.add_argument("--concurrency", type=int, default=4)
    parser.add_argument("--embedding-batch-size", type=int, default=32)
    parser.add_argument("--reranker-base-url")
    parser.add_argument(
        "--reranker-model", default="bge-reranker-v2-m3"
    )
    parser.add_argument("--reranker-top-k", type=int, default=30)
    parser.add_argument("--reranker-timeout-seconds", type=float, default=120.0)
    parser.add_argument("--max-turns", type=int, default=4)
    parser.add_argument("--max-actions", type=int, default=8)
    parser.add_argument("--max-sql-executions", type=int, default=3)
    parser.add_argument(
        "--condition",
        action="append",
        choices=SUPPORTED_CONDITIONS,
        help="Run only the selected arm; repeat for multiple arms.",
    )
    parser.add_argument(
        "--seed-output-root",
        type=Path,
        help="Reuse a completed prediction subset without repeating model calls.",
    )
    parser.add_argument(
        "--anchor-predictions",
        type=Path,
        help=(
            "Frozen first-stage base predictions. With a relational-program arm, "
            "their non-relation SQL clauses become the mandatory AST contract."
        ),
    )
    parser.add_argument(
        "--auxiliary-raw-predictions",
        type=Path,
        help=(
            "Frozen Direct Raw-Evidence SQL used as an independent draft inside "
            "the unified Graph+Evo main; schema properties determine backbone priority."
        ),
    )
    parser.add_argument("--evidence-first-history", action="store_true")
    parser.add_argument("--realize-semantic-revision", action="store_true")
    parser.add_argument("--scope-grounded-revision", action="store_true")
    parser.add_argument("--witness-consistent-revision", action="store_true")
    parser.add_argument("--grounded-binding-revision", action="store_true")
    parser.add_argument("--realized-edit-revision", action="store_true")
    parser.add_argument("--scope-faithful-revision", action="store_true")
    parser.add_argument("--relational-grain-revision", action="store_true")
    parser.add_argument("--entity-grain-revision", action="store_true")
    parser.add_argument("--lower-eligibility-revision", action="store_true")
    parser.add_argument("--retrieval-cache", type=Path, help="Frozen outcome-free query retrieval snapshots")
    parser.add_argument("--semantic-memory", type=Path, help="V17 fixed revision query memory by database; absent preserves V15")
    parser.add_argument("--physical-execution-python")
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()
    if args.subset_size < 1 or args.concurrency < 1:
        raise ValueError("subset size and concurrency must be positive")
    conditions = tuple(args.condition or DEFAULT_CONDITIONS)
    if args.workload_semantic_state and conditions not in {
        (GRAPH_EVO_SEMANTIC_PROGRAM_MAIN,), ("program_graph_react",)
    }:
        raise ValueError("workload semantic state is reserved for the unified main and its program-graph draft stage")
    if len(set(conditions)) != len(conditions):
        raise ValueError("duplicate condition")
    if args.reranker_base_url is not None and conditions != (
        GRAPH_EVO_SEMANTIC_PROGRAM_MAIN,
    ):
        raise ValueError("the cross-encoder reranker is reserved for the unified main")
    if args.reranker_base_url is not None and not 1 <= args.reranker_top_k <= 100:
        raise ValueError("reranker top-k must be between 1 and 100")
    if args.anchor_predictions is not None and any(
        condition not in RELATIONAL_PROGRAM_CONDITIONS for condition in conditions
    ):
        raise ValueError(
            "anchor predictions may only be used with relational-program conditions"
        )
    if (
        GRAPH_EVO_SEMANTIC_PROGRAM_MAIN in conditions
        and args.anchor_predictions is None
    ):
        raise ValueError("the unified Graph+Evo main requires --anchor-predictions")
    if args.auxiliary_raw_predictions is not None and (
        conditions != (GRAPH_EVO_SEMANTIC_PROGRAM_MAIN,)
        or args.anchor_predictions is None
    ):
        raise ValueError(
            "auxiliary raw predictions require the unified Graph+Evo main alone"
        )

    memory_by_database = json.loads(args.semantic_memory.read_text()) if args.semantic_memory else {}
    retrieval_by_id = {r["example_id"]: r for r in _load_jsonl(args.retrieval_cache)} if args.retrieval_cache else {}
    all_rows = _load_jsonl(args.online)
    if {str(row["dataset_id"]) for row in all_rows} != {args.dataset_id}:
        raise ValueError("dataset ID does not match online manifest")
    rows = _select(all_rows, args.example_id, args.subset_size)
    anchor_by_id: dict[str, str] = {}
    if args.anchor_predictions is not None:
        anchor_rows = _load_jsonl(args.anchor_predictions)
        for anchor_row in anchor_rows:
            example_id = str(anchor_row.get("example_id") or "")
            sql = str(anchor_row.get("sql") or "").strip()
            if not example_id or not sql:
                raise ValueError("anchor predictions contain an empty ID or SQL")
            if example_id in anchor_by_id:
                raise ValueError(f"duplicate anchor prediction: {example_id}")
            anchor_by_id[example_id] = sql
        missing_anchors = sorted(
            str(row["example_id"])
            for row in rows
            if str(row["example_id"]) not in anchor_by_id
        )
        if missing_anchors:
            raise ValueError(
                f"anchor predictions miss {len(missing_anchors)} selected examples"
            )
    auxiliary_raw_by_id: dict[str, str] = {}
    if args.auxiliary_raw_predictions is not None:
        for auxiliary_row in _load_jsonl(args.auxiliary_raw_predictions):
            example_id = str(auxiliary_row.get("example_id") or "")
            sql = str(auxiliary_row.get("sql") or "").strip()
            if not example_id or not sql or example_id in auxiliary_raw_by_id:
                raise ValueError(
                    "auxiliary raw predictions contain an invalid or duplicate row"
                )
            auxiliary_raw_by_id[example_id] = sql
        missing_raw = sorted(
            str(row["example_id"])
            for row in rows
            if str(row["example_id"]) not in auxiliary_raw_by_id
        )
        if missing_raw:
            raise ValueError(
                f"auxiliary raw predictions miss {len(missing_raw)} selected examples"
            )
    if args.semantic_memory and not {str(r["database_id"]) for r in rows} <= memory_by_database.keys():
        raise ValueError("semantic memory missing database")
    if args.retrieval_cache and not {str(r["example_id"]) for r in rows} <= retrieval_by_id.keys():
        raise ValueError("retrieval cache missing target")
    args.output_root.mkdir(parents=True, exist_ok=True)
    subset_path = args.output_root / "SUBSET.jsonl"
    subset_content = "".join(
        json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows
    )
    if subset_path.exists() and subset_path.read_text(encoding="utf-8") != subset_content:
        raise FileExistsError("refusing to change frozen subset")
    if not subset_path.exists():
        subset_path.write_text(subset_content, encoding="utf-8")

    if args.retrieval_cache:
        from finsemguard.schema_recovery.joint import file_hash
        cache_manifest = json.loads(args.retrieval_cache.with_suffix(".manifest.json").read_text())
        if file_hash(args.retrieval_cache) != cache_manifest["cache_sha256"]:
            raise ValueError("retrieval cache content changed")
        for key, path in [("table_inputs.jsonl", args.table_inputs), ("table_recovery.jsonl", args.recovery), ("semantic_layer/state.json", args.workload_semantic_state)]:
            if path is None or file_hash(path) != cache_manifest["assets"][key]:
                raise ValueError("retrieval asset mismatch: " + key)
    table_inputs = _load_jsonl(args.table_inputs)
    recovery_rows = _load_jsonl(args.recovery)
    knowledge_rows = _load_jsonl(args.knowledge) if args.knowledge else []
    raw_documents = load_catalog(
        args.dataset_id,
        args.data_root,
        all_rows,
        spider_schema_view="physical",
        kaggledbqa_schema_view="physical",
        bird_schema_view="physical",
    )
    recovery_documents = build_recovery_documents(table_inputs, recovery_rows)
    ontology = OperationalOntology.from_recovery_inputs(
        table_inputs, knowledge_rows=knowledge_rows
    )
    if args.workload_semantic_state:
        from finsemguard.ontology_discovery.workload_semantics import WorkloadSemanticLayer

        ontology = WorkloadSemanticLayer.load(args.workload_semantic_state).augment_ontology(ontology)
    treatment_documents = ontology.augment_documents(
        [*raw_documents, *recovery_documents]
    )
    encoder = BGEEncoder(
        model_path=args.embedding_model,
        documents=treatment_documents,
        cache_path=args.embedding_cache,
        batch_size=args.embedding_batch_size,
    )
    if RELATIONAL_PROGRAM_CONDITIONS & set(conditions) and not args.retrieval_cache:
        query_texts = list(
            dict.fromkeys(str(row["question"]) for row in rows)
        )
        role_phrase_texts = list(
            dict.fromkeys(
                phrase
                for row in rows
                for phrase in (
                    _minimal_join_tree_role_phrases(str(row["question"]))
                    if (
                        "minimal_join_tree_react" in conditions
                        or GRAPH_EVO_SEMANTIC_PROGRAM_MAIN in conditions
                    )
                    else _query_role_phrases(str(row["question"]))
                )
            )
        )
        encoder.encode_queries([*query_texts, *role_phrase_texts])
        print(
            f"[bge-query-cache] questions={len(query_texts)} "
            f"role_phrases={len(role_phrase_texts)}",
            flush=True,
        )
    raw_ids = {row.candidate_id for row in raw_documents}
    raw_index = SchemaSearchIndex(
        documents=raw_documents,
        raw_documents=raw_documents,
        vectors={key: value for key, value in encoder.vectors.items() if key in raw_ids},
        encode_query=encoder.encode_query,
    )
    ontology_edges: dict[str, list[dict[str, Any]]] = {}
    for edge in ontology.edges:
        ontology_edges.setdefault(edge.context, []).append(
            {
                "left": edge.left,
                "right": edge.right,
                "evidence": "+".join(edge.evidence_types),
                "provenance_ids": list(edge.provenance_ids),
                "score": edge.score,
            }
        )
    raw_by_name = {
        (row.database_id, row.name): row.candidate_id for row in raw_documents
    }
    bindings_by_document = {
        candidate_id: list(bound_ids)
        for candidate_id, bound_ids in ontology.document_bindings.items()
    }
    for row in recovery_documents:
        raw_id = raw_by_name.get((row.database_id, row.name))
        if raw_id:
            bindings_by_document.setdefault(row.candidate_id, []).append(raw_id)
    reranker: VLLMRerankerClient | None = None
    if args.reranker_base_url is not None:
        reranker = VLLMRerankerClient(
            base_url=args.reranker_base_url,
            model=args.reranker_model,
            timeout_seconds=args.reranker_timeout_seconds,
        )
        if not reranker.healthy():
            raise RuntimeError("required exact main-method reranker is unavailable")
    treatment_index = SchemaSearchIndex(
        documents=treatment_documents,
        raw_documents=raw_documents,
        vectors={row.candidate_id: encoder.vectors[row.candidate_id] for row in treatment_documents},
        encode_query=encoder.encode_query,
        ontology_edges_by_database=ontology_edges,
        bindings_by_document=bindings_by_document,
    )
    program_graph_index = SchemaSearchIndex(
        documents=treatment_documents,
        raw_documents=raw_documents,
        vectors={
            row.candidate_id: encoder.vectors[row.candidate_id]
            for row in treatment_documents
        },
        encode_query=encoder.encode_query,
        encode_queries=encoder.encode_queries,
        ontology_edges_by_database=ontology_edges,
        bindings_by_document=bindings_by_document,
        program_graph=True,
    )
    minimal_join_tree_index = SchemaSearchIndex(
        documents=treatment_documents,
        raw_documents=raw_documents,
        vectors={
            row.candidate_id: encoder.vectors[row.candidate_id]
            for row in treatment_documents
        },
        encode_query=encoder.encode_query,
        encode_queries=encoder.encode_queries,
        ontology_edges_by_database=ontology_edges,
        bindings_by_document=bindings_by_document,
        minimal_join_tree=True,
        rerank_documents=reranker.score if reranker is not None else None,
        rerank_top_k=args.reranker_top_k,
        evidence_first_history=args.evidence_first_history,
    )
    recovery_only_documents = [*raw_documents, *recovery_documents]
    recovery_only_index = SchemaSearchIndex(
        documents=recovery_only_documents,
        raw_documents=raw_documents,
        vectors={
            row.candidate_id: encoder.vectors[row.candidate_id]
            for row in recovery_only_documents
        },
        encode_query=encoder.encode_query,
        bindings_by_document=bindings_by_document,
    )
    indices = {
        "opaque_react": raw_index,
        "recovery_only_react": recovery_only_index,
        "ontology_react": treatment_index,
        "program_graph_react": program_graph_index,
        "minimal_join_tree_react": minimal_join_tree_index,
        "chess_react": raw_index,
        "autolink_react": raw_index,
        GRAPH_EVO_SEMANTIC_PROGRAM_MAIN: minimal_join_tree_index,
    }

    llm_config = dict(load_config(args.config)["llm"])
    if args.lean:
        llm_config.pop("audit_log_path", None)
    endpoint_urls = list(
        dict.fromkeys(
            str(value).rstrip("/")
            for value in (args.llm_base_url or [llm_config["base_url"]])
        )
    )
    clients: list[VLLMClient] = []
    for endpoint_url in endpoint_urls:
        endpoint_client = VLLMClient({**llm_config, "base_url": endpoint_url})
        if not endpoint_client.healthy():
            raise RuntimeError(
                f"required exact LLM is unavailable at {endpoint_client.base_url}"
            )
        clients.append(endpoint_client)
    client = clients[0]
    client_by_id = {
        str(row["example_id"]): clients[index % len(clients)]
        for index, row in enumerate(rows)
    }
    paths = {
        condition: args.output_root / f"{condition}.jsonl"
        for condition in conditions
    }
    if not args.resume and any(path.exists() for path in paths.values()):
        raise FileExistsError("output exists; use --resume or a new output root")
    completed: dict[str, dict[str, dict[str, Any]]] = {}
    for condition, path in paths.items():
        prior = _load_jsonl(path) if args.resume and path.is_file() else []
        completed[condition] = {
            str(row["example_id"]): (
                _strip_lean_metadata(row) if args.lean else row
            )
            for row in prior
            if row.get("status") != "error"
        }
    if args.seed_output_root:
        seed = {
            condition: _load_jsonl(args.seed_output_root / f"{condition}.jsonl")
            for condition in conditions
        }
        seed_ids = {str(row["example_id"]) for row in seed[conditions[0]]}
        if not seed_ids or any(
            {str(row["example_id"]) for row in seed[condition]} != seed_ids
            for condition in conditions
        ):
            raise ValueError("seed outputs have empty or inconsistent coverage")
        expected_ids = {str(row["example_id"]) for row in rows}
        if not seed_ids.issubset(expected_ids):
            raise ValueError("seed outputs are outside the requested scope")
        for condition in conditions:
            by_id = {str(row["example_id"]): row for row in seed[condition]}
            overlap = set(completed[condition]) & seed_ids
            if overlap:
                raise ValueError(f"seed/resume overlap for {condition}")
            completed[condition].update(by_id)
    lock = Lock()

    def run(row: dict[str, Any]) -> dict[str, dict[str, Any]]:
        example_id = str(row["example_id"])
        selected_client = client_by_id[example_id]
        order = list(conditions)
        if sha256(example_id.encode()).digest()[0] % 2:
            order.reverse()
        output: dict[str, dict[str, Any]] = {}
        for condition in order:
            if example_id in completed[condition]:
                continue
            try:
                if condition == GRAPH_EVO_SEMANTIC_PROGRAM_MAIN:
                    output[condition] = run_graph_evo_semantic_program_main(
                        compose_history=args.compose_history or args.bind_history,
                        bind_history=args.bind_history,
                        plan_history=args.plan_history,
                        scope_history=args.scope_history,
                        evidence_first_history=args.evidence_first_history,
                        realize_semantic_revision=args.realize_semantic_revision,
                        scope_grounded_revision=args.scope_grounded_revision,
                        witness_consistent_revision=args.witness_consistent_revision,
                        grounded_binding_revision=args.grounded_binding_revision,
                        realized_edit_revision=args.realized_edit_revision,
                        physical_execution_python=args.physical_execution_python,
                        scope_faithful_revision=args.scope_faithful_revision,
                        relational_grain_revision=args.relational_grain_revision,
                        entity_grain_revision=args.entity_grain_revision,
                        lower_eligibility_revision=args.lower_eligibility_revision,
                        semantic_memory=memory_by_database.get(str(row["database_id"])),
                        retrieval_snapshot=retrieval_by_id.get(example_id),
                        condition="minimal_join_tree_react",
                        row=row,
                        client=selected_client,
                        database=_database_path(args.data_root, row),
                        search_index=indices[condition],
                        anchor_sql=anchor_by_id[example_id],
                        auxiliary_raw_sql=(
                            auxiliary_raw_by_id[example_id]
                            if args.auxiliary_raw_predictions is not None
                            else None
                        ),
                        max_turns=args.max_turns,
                        max_actions=args.max_actions,
                        max_sql_executions=args.max_sql_executions,
                    )
                else:
                    output[condition] = run_react_text2sql(
                        condition=condition,
                        row=row,
                        client=selected_client,
                        database=_database_path(args.data_root, row),
                        search_index=indices[condition],
                        max_turns=args.max_turns,
                        max_actions=args.max_actions,
                        max_sql_executions=args.max_sql_executions,
                        method_id_override=(
                            BASE_ANCHORED_RELATIONAL_PROGRAM_METHOD_ID
                            if args.anchor_predictions is not None
                            else None
                        ),
                        anchor_sql=(
                            anchor_by_id[example_id]
                            if args.anchor_predictions is not None
                            else None
                        ),
                    )
            except Exception as error:
                output[condition] = {
                    "example_id": example_id,
                    "dataset_id": row["dataset_id"],
                    "database_id": row["database_id"],
                    "upstream_split": row["upstream_split"],
                    "method_id": _declared_method_id(
                        condition,
                        anchored=args.anchor_predictions is not None,
                    ),
                    "asset_condition": condition,
                    "status": "error",
                    "error_type": type(error).__name__,
                    "error": str(error)[:1000],
                    "sql": "",
                }
            if args.lean:
                output[condition] = _strip_lean_metadata(output[condition])
        return output

    pending = [
        row
        for row in rows
        if any(str(row["example_id"]) not in completed[c] for c in conditions)
    ]
    with ThreadPoolExecutor(max_workers=args.concurrency) as executor:
        futures = {executor.submit(run, row): row for row in pending}
        for count, future in enumerate(as_completed(futures), start=1):
            generated = future.result()
            with lock:
                for condition, result in generated.items():
                    completed[condition][str(result["example_id"])] = result
                    with paths[condition].open("a", encoding="utf-8") as handle:
                        handle.write(json.dumps(result, ensure_ascii=False) + "\n")
                        handle.flush()
            print(f"[ontology-react {count}/{len(futures)}]", flush=True)

    ordered: dict[str, list[dict[str, Any]]] = {}
    for condition, path in paths.items():
        ordered[condition] = [
            completed[condition][str(row["example_id"])] for row in rows
        ]
        _write_atomic(path, ordered[condition])
    summary = {
        "protocol": "budget_matched_react_conditions_v2",
        "dataset_id": args.dataset_id,
        "rows": len(rows),
        "conditions": list(conditions),
        "errors": {
            condition: sum(row.get("status") == "error" for row in values)
            for condition, values in ordered.items()
        },
        "model": {
            "requested": client.model,
            "require_exact": client.require_exact_model,
            "thinking": client.thinking,
        },
        "embedding": {
            "model_id": "BAAI/bge-m3",
            "backend": encoder.backend,
            "minilm_used": False,
        },
        "main_reranker": (
            {
                "model_id": reranker.model,
                "candidate_top_k": args.reranker_top_k,
                "scope": "unified_graph_evo_main_only",
            }
            if reranker is not None
            else None
        ),
        "ontology": ontology.manifest(),
        "evidence_boundary": {
            "baseline": "opaque schema + values + execution",
            "treatment_additional": (
                "automatic recovery mappings; ontology_react additionally injects "
                "operational ontology edges"
            ),
            "paper_baselines": {
                "chess_react": (
                    "raw physical catalog + values + execution/revision; no recovery, "
                    "history, KB, or ontology"
                ),
                "autolink_react": (
                    "raw physical catalog + one bounded targeted expansion + values + "
                    "execution; no recovery, history, KB, or ontology"
                ),
            },
            "evaluator_manifest_read": False,
        },
        "seed_output_root": str(args.seed_output_root) if args.seed_output_root else None,
        "base_solution_anchor": (
            {
                "path": str(args.anchor_predictions),
                "rows": len(anchor_by_id),
                "method_id": (
                    GRAPH_EVO_SEMANTIC_PROGRAM_MAIN
                    if GRAPH_EVO_SEMANTIC_PROGRAM_MAIN in conditions
                    else BASE_ANCHORED_RELATIONAL_PROGRAM_METHOD_ID
                ),
                "uses_evaluator_gold": False,
            }
            if args.anchor_predictions is not None
            else None
        ),
        "auxiliary_raw_evidence_draft": (
            {
                "path": str(args.auxiliary_raw_predictions),
                "rows": len(auxiliary_raw_by_id),
                "consumer": "schema_property_evidence_priority",
            }
            if args.auxiliary_raw_predictions is not None
            else None
        ),
        "generation_endpoints": len(clients),
        "budgets": {
            "max_turns": args.max_turns,
            "max_actions": args.max_actions,
            "max_sql_executions": args.max_sql_executions,
            "token_budget": client.token_budget_status(),
        },
    }
    summary_name = (
        "GENERATION_SUMMARY_RESUMED.json" if args.resume else "GENERATION_SUMMARY.json"
    )
    if not args.lean:
        summary["embedding"]["fingerprint"] = encoder.fingerprint
        if summary["base_solution_anchor"] is not None:
            summary["base_solution_anchor"]["sha256"] = sha256(
                args.anchor_predictions.read_bytes()
            ).hexdigest()
    written_summary = _strip_lean_metadata(summary) if args.lean else summary
    _write_json(args.output_root / summary_name, written_summary)
    print(json.dumps(written_summary, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
