#!/usr/bin/env python3
"""Run the EvoSchema Full method against call-matched external baselines."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from hashlib import sha256
import json
from pathlib import Path
import re
from threading import Lock
from typing import Any

import sqlglot
from sqlglot import exp

from finsemguard.agent.llm import VLLMClient
from finsemguard.config import load_config
from finsemguard.e2e.evoschema import (
    EvoSchemaMapping,
    EvoSchemaSQLiteAgentTools,
    build_catalog_documents,
    build_lineage_ontology_documents,
    evolve_snapshot,
    infer_schema_lineage,
    read_sqlite_snapshot,
    translate_storage_sql_to_current,
)
from finsemguard.e2e.evolution_relations import (
    EvolutionSQLiteAgentTools,
    RelationEvolutionMapping,
)
from finsemguard.e2e.livesqlbench import CatalogDocument
from finsemguard.e2e.livesqlbench_runner import _load_jsonl, _write_atomic
from finsemguard.e2e.performance_pipeline import _database_path
from finsemguard.e2e.react_text2sql import (
    METHOD_IDS,
    SchemaSearchIndex,
    _minimal_join_tree_role_phrases,
    _query_role_phrases,
    run_react_text2sql,
)
from run_bird_react_recovery import BGEEncoder


EXTERNAL_BASELINE_CONDITIONS = (
    "evoschema_raw_react",
    "chess_react",
    "autolink_react",
)
DEFAULT_CONDITIONS = (
    *EXTERNAL_BASELINE_CONDITIONS,
    "evoschema_full_react",
)
ABLATION_CONDITIONS = ("evoschema_flat_react",)
PROGRAM_GRAPH_CONDITIONS = (
    "evoschema_program_graph_react",
    "evoschema_minimal_join_tree_react",
)
SUPPORTED_CONDITIONS = (
    *DEFAULT_CONDITIONS,
    *ABLATION_CONDITIONS,
    *PROGRAM_GRAPH_CONDITIONS,
)
EVOSCHEMA_DATASET_IDS = {"evoschema", "evoschema_relation_change"}


def _generation_protocol(conditions: tuple[str, ...]) -> str:
    if conditions == DEFAULT_CONDITIONS:
        return "evoschema_external_baseline_main_comparison_v1"
    if conditions and set(conditions) <= set(EXTERNAL_BASELINE_CONDITIONS):
        return "evoschema_external_baseline_reproduction_v1"
    if set(conditions) & set(ABLATION_CONDITIONS):
        return "evoschema_post_main_ablation_v1"
    return "evoschema_relational_program_development_v1"


def _external_baseline_only(conditions: tuple[str, ...]) -> bool:
    return bool(conditions) and set(conditions) <= set(
        EXTERNAL_BASELINE_CONDITIONS
    )


def _evoschema_dataset_id(rows: list[dict[str, Any]]) -> str:
    dataset_ids = {str(row.get("dataset_id") or "") for row in rows}
    if len(dataset_ids) != 1 or not dataset_ids <= EVOSCHEMA_DATASET_IDS:
        raise ValueError(
            "online manifest must be one homogeneous EvoSchema scope: "
            "evoschema or evoschema_relation_change"
        )
    return next(iter(dataset_ids))


def _runtime_mapping_and_current(
    *,
    dataset_id: str,
    runtime_mapping: dict[str, Any],
    previous: Any,
) -> tuple[Any, Any]:
    """Deserialize the runtime adapter that matches the frozen asset family.

    Relation-changing EvoSchema assets carry non-bijective table/column lineage
    plus an explicit current snapshot.  Treating that payload as the older
    rename-only ``EvoSchemaMapping`` silently produces an empty mapping and
    exposes the historical schema to the model.  Keep the two formats explicit.
    """

    if dataset_id == "evoschema_relation_change":
        mapping = RelationEvolutionMapping.from_json(runtime_mapping)
        return mapping, mapping.current_snapshot
    if dataset_id == "evoschema":
        mapping = EvoSchemaMapping.from_json(runtime_mapping)
        return mapping, evolve_snapshot(previous, mapping)
    raise ValueError(f"unsupported EvoSchema dataset_id: {dataset_id}")


def _normalized_text(value: str) -> str:
    return " ".join(re.findall(r"[\w]+", value.casefold()))


def _sql_bindings(
    sql: str, *, context_id: str, current: Any
) -> list[str]:
    tree = sqlglot.parse_one(sql, read="sqlite")
    table_names = {table.name.casefold(): table.name for table in current.tables}
    columns = {
        table.name: {column.name.casefold(): column.name for column in table.columns}
        for table in current.tables
    }
    aliases: dict[str, str] = {}
    referenced: list[str] = []
    output: list[str] = []
    for node in tree.find_all(exp.Table):
        current_table = table_names.get(node.name.casefold())
        if current_table is None:
            continue
        aliases[str(node.alias or current_table).casefold()] = current_table
        aliases[current_table.casefold()] = current_table
        referenced.append(current_table)
        output.append(f"table::{context_id}::{current_table}")
    for node in tree.find_all(exp.Column):
        if node.name == "*":
            continue
        qualifier = str(node.table or "")
        if qualifier and qualifier.casefold() in aliases:
            candidates = [aliases[qualifier.casefold()]]
        else:
            candidates = [
                table
                for table in dict.fromkeys(referenced)
                if node.name.casefold() in columns[table]
            ]
        if len(candidates) == 1:
            table = candidates[0]
            column = columns[table].get(node.name.casefold())
            if column:
                output.append(f"column::{context_id}::{table}::{column}")
    return list(dict.fromkeys(output))


def _history_documents(
    *,
    bird_rows: list[dict[str, Any]],
    target: dict[str, Any],
    previous: Any,
    current: Any,
    mapping: EvoSchemaMapping,
    context_id: str,
) -> tuple[list[CatalogDocument], dict[str, list[str]]]:
    target_id = int(target["official_train_idx"])
    target_question = _normalized_text(str(target["question"]))
    target_sql = _normalized_text(str(bird_rows[target_id]["SQL"]))
    source_database_id = str(target["source_database_id"])
    documents: list[CatalogDocument] = []
    bindings: dict[str, list[str]] = {}
    for row in bird_rows:
        if str(row["db_id"]) != source_database_id:
            continue
        question = str(row["question"])
        historical_sql = str(row["SQL"])
        if (
            int(row["question_id"]) == target_id
            or _normalized_text(question) == target_question
            or _normalized_text(historical_sql) == target_sql
        ):
            continue
        try:
            compiled_sql = translate_storage_sql_to_current(
                historical_sql, mapping=mapping, previous=previous
            )
            physical_ids = _sql_bindings(
                compiled_sql, context_id=context_id, current=current
            )
        except Exception:
            continue
        candidate_id = f"history_sql::{context_id}::{row['question_id']}"
        document = CatalogDocument(
            candidate_id=candidate_id,
            database_id=context_id,
            kind="history_sql",
            table=None,
            name=f"historical question: {question}",
            text=json.dumps(
                {
                    "historical_question": question,
                    "compiled_current_sql_pattern": compiled_sql,
                    "provenance": "target_isolated_prior_BIRD_workload",
                    "instruction": "adapt the pattern; do not copy target-specific literals",
                },
                ensure_ascii=False,
                sort_keys=True,
            ),
        )
        documents.append(document)
        bindings[candidate_id] = physical_ids
    return documents, bindings


def _deduplicated_encoder(
    *,
    documents: list[CatalogDocument],
    model_path: Path,
    cache_path: Path,
    batch_size: int,
    seed_cache_paths: list[Path] | None = None,
) -> tuple[BGEEncoder, dict[str, Any], int]:
    representatives: list[CatalogDocument] = []
    representative_by_text: dict[str, str] = {}
    representative_by_candidate: dict[str, str] = {}
    for document in documents:
        text = document.retrieval_text()
        representative_id = representative_by_text.get(text)
        if representative_id is None:
            representative_id = f"embedding_text::{sha256(text.encode()).hexdigest()}"
            representative_by_text[text] = representative_id
            representatives.append(
                CatalogDocument(
                    candidate_id=representative_id,
                    database_id="embedding-deduplicated",
                    kind=document.kind,
                    table=None,
                    name=document.name,
                    text=document.text,
                )
            )
        representative_by_candidate[document.candidate_id] = representative_id
    encoder = BGEEncoder(
        model_path=model_path,
        documents=representatives,
        cache_path=cache_path,
        batch_size=batch_size,
        seed_cache_paths=seed_cache_paths,
    )
    vectors = {
        candidate_id: encoder.vectors[representative_id]
        for candidate_id, representative_id in representative_by_candidate.items()
    }
    return encoder, vectors, len(representatives)


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


def _write_latest_json(path: Path, value: dict[str, Any]) -> None:
    """Atomically replace a mutable resume summary, never a prediction."""

    content = json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(content, encoding="utf-8")
    temporary.replace(path)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo-root", type=Path, default=Path("."))
    parser.add_argument("--online", type=Path, required=True)
    parser.add_argument("--runtime", type=Path, required=True)
    parser.add_argument("--embedding-model", type=Path, required=True)
    parser.add_argument("--embedding-cache", type=Path, required=True)
    parser.add_argument(
        "--embedding-seed-cache", type=Path, action="append", default=[]
    )
    parser.add_argument("--config", type=Path, required=True)
    parser.add_argument("--audit-log", type=Path)
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument("--concurrency", type=int, default=4)
    parser.add_argument("--embedding-batch-size", type=int, default=32)
    parser.add_argument("--max-turns", type=int, default=4)
    parser.add_argument("--max-actions", type=int, default=8)
    parser.add_argument("--max-sql-executions", type=int, default=3)
    parser.add_argument("--example-id", action="append", default=[])
    parser.add_argument(
        "--condition", action="append", choices=SUPPORTED_CONDITIONS
    )
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()
    if args.concurrency < 1:
        raise ValueError("concurrency must be positive")
    conditions = tuple(args.condition or DEFAULT_CONDITIONS)
    if len(set(conditions)) != len(conditions):
        raise ValueError("duplicate condition")
    external_baseline_only = _external_baseline_only(conditions)

    repo_root = args.repo_root.resolve()
    # Raw/CHESS/AutoLink reproduction must not even open the historical target
    # workload.  These adapters use only the evolved current catalog and runtime
    # database tools; lineage/history assets are built solely for conditions that
    # explicitly require them.
    bird_rows = (
        []
        if external_baseline_only
        else json.loads(
            (repo_root / "data/raw/bird_full_dev/dev.json").read_text(
                encoding="utf-8"
            )
        )
    )
    all_rows = _load_jsonl(args.online)
    dataset_id = _evoschema_dataset_id(all_rows)
    relation_change_assets = dataset_id == "evoschema_relation_change"
    if relation_change_assets and not external_baseline_only:
        raise ValueError(
            "relation-changing assets require the dedicated evolution-aware "
            "main runner; this runner supports them only for current-catalog "
            "external baseline reproduction"
        )
    if args.example_id:
        requested = set(args.example_id)
        rows = [row for row in all_rows if str(row["example_id"]) in requested]
        if {str(row["example_id"]) for row in rows} != requested:
            raise ValueError("one or more requested example IDs are absent")
    else:
        rows = all_rows
    runtime_rows = {str(row["example_id"]): row for row in _load_jsonl(args.runtime)}
    expected = {str(row["example_id"]) for row in all_rows}
    if set(runtime_rows) != expected:
        raise ValueError("runtime sidecar does not match online manifest")

    args.output_root.mkdir(parents=True, exist_ok=True)
    subset_path = args.output_root / "SUBSET.jsonl"
    subset_content = "".join(
        json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows
    )
    if subset_path.exists() and subset_path.read_text(encoding="utf-8") != subset_content:
        raise FileExistsError("refusing to change frozen EvoSchema subset")
    if not subset_path.exists():
        subset_path.write_text(subset_content, encoding="utf-8")

    snapshots_by_database: dict[str, Any] = {}
    mappings: dict[str, Any] = {}
    current_snapshots: dict[str, Any] = {}
    raw_documents = []
    full_extra_documents = []
    bindings: dict[str, list[str]] = {}
    ontology_edges: dict[str, list[dict[str, Any]]] = {}
    for row in all_rows:
        example_id = str(row["example_id"])
        context_id = str(row["database_id"])
        source_database_id = str(row["source_database_id"])
        database = _database_path(repo_root, row)
        previous = snapshots_by_database.get(source_database_id)
        if previous is None:
            previous = read_sqlite_snapshot(database)
            snapshots_by_database[source_database_id] = previous
        mapping, current = _runtime_mapping_and_current(
            dataset_id=dataset_id,
            runtime_mapping=dict(runtime_rows[example_id]["mapping"]),
            previous=previous,
        )
        mappings[example_id] = mapping
        current_snapshots[example_id] = current
        context_raw = build_catalog_documents(current, context_id)
        raw_documents.extend(context_raw)
        if not external_baseline_only:
            inferred = infer_schema_lineage(previous, current)
            if evolve_snapshot(previous, inferred) != current:
                raise ValueError(f"automatic lineage is incomplete: {example_id}")
            extra, context_bindings, context_edges = (
                build_lineage_ontology_documents(
                    previous=previous,
                    current=current,
                    lineage=inferred,
                    context_id=context_id,
                )
            )
            history, history_bindings = _history_documents(
                bird_rows=bird_rows,
                target=row,
                previous=previous,
                current=current,
                mapping=inferred,
                context_id=context_id,
            )
            full_extra_documents.extend([*extra, *history])
            bindings.update(context_bindings)
            bindings.update(history_bindings)
            ontology_edges[context_id] = context_edges

    full_documents = [*raw_documents, *full_extra_documents]
    encoder, vectors, unique_embedding_texts = _deduplicated_encoder(
        documents=full_documents,
        model_path=args.embedding_model,
        cache_path=args.embedding_cache,
        batch_size=args.embedding_batch_size,
        seed_cache_paths=args.embedding_seed_cache,
    )
    if set(PROGRAM_GRAPH_CONDITIONS) & set(conditions):
        query_texts = list(
            dict.fromkeys(str(row["question"]) for row in rows)
        )
        role_phrase_texts = list(
            dict.fromkeys(
                phrase
                for row in rows
                for phrase in (
                    _minimal_join_tree_role_phrases(str(row["question"]))
                    if "evoschema_minimal_join_tree_react" in conditions
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
        vectors={key: value for key, value in vectors.items() if key in raw_ids},
        encode_query=encoder.encode_query,
    )
    full_index = SchemaSearchIndex(
        documents=full_documents,
        raw_documents=raw_documents,
        vectors={row.candidate_id: vectors[row.candidate_id] for row in full_documents},
        encode_query=encoder.encode_query,
        ontology_edges_by_database=ontology_edges,
        bindings_by_document=bindings,
    )
    program_graph_index = SchemaSearchIndex(
        documents=full_documents,
        raw_documents=raw_documents,
        vectors={row.candidate_id: vectors[row.candidate_id] for row in full_documents},
        encode_query=encoder.encode_query,
        encode_queries=encoder.encode_queries,
        ontology_edges_by_database=ontology_edges,
        bindings_by_document=bindings,
        program_graph=True,
    )
    minimal_join_tree_index = SchemaSearchIndex(
        documents=full_documents,
        raw_documents=raw_documents,
        vectors={row.candidate_id: vectors[row.candidate_id] for row in full_documents},
        encode_query=encoder.encode_query,
        encode_queries=encoder.encode_queries,
        ontology_edges_by_database=ontology_edges,
        bindings_by_document=bindings,
        minimal_join_tree=True,
    )
    flat_index = SchemaSearchIndex(
        documents=full_documents,
        raw_documents=raw_documents,
        vectors={row.candidate_id: vectors[row.candidate_id] for row in full_documents},
        encode_query=encoder.encode_query,
    )
    indices = {
        "evoschema_raw_react": raw_index,
        "chess_react": raw_index,
        "autolink_react": raw_index,
        "evoschema_flat_react": flat_index,
        "evoschema_full_react": full_index,
        "evoschema_program_graph_react": program_graph_index,
        "evoschema_minimal_join_tree_react": minimal_join_tree_index,
    }

    llm_config = dict(load_config(args.config)["llm"])
    if args.audit_log is not None:
        llm_config["audit_log_path"] = str(args.audit_log)
    client = VLLMClient(llm_config)
    if not client.healthy():
        raise RuntimeError(f"required exact LLM is unavailable at {client.base_url}")
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
            str(row["example_id"]): row
            for row in prior
            if row.get("status") != "error"
        }
    lock = Lock()

    def run(row: dict[str, Any]) -> dict[str, dict[str, Any]]:
        example_id = str(row["example_id"])
        offset = sha256(f"arm-order-v1::{example_id}".encode()).digest()[0] % len(conditions)
        order = [*conditions[offset:], *conditions[:offset]]
        output: dict[str, dict[str, Any]] = {}
        mapping = mappings[example_id]
        current = current_snapshots[example_id]

        def tools_factory(database: Path, database_id: str, search_index: SchemaSearchIndex):
            if relation_change_assets:
                if not isinstance(mapping, RelationEvolutionMapping):
                    raise TypeError("relation-change runtime mapping type mismatch")
                return EvolutionSQLiteAgentTools(
                    database,
                    database_id,
                    search_index,
                    mapping=mapping,
                    expose_evolution_evidence=False,
                )
            if not isinstance(mapping, EvoSchemaMapping):
                raise TypeError("rename-only runtime mapping type mismatch")
            return EvoSchemaSQLiteAgentTools(
                database,
                database_id,
                search_index,
                mapping=mapping,
                current_snapshot=current,
            )

        for condition in order:
            if example_id in completed[condition]:
                continue
            try:
                output[condition] = run_react_text2sql(
                    condition=condition,
                    row=row,
                    client=client,
                    database=_database_path(repo_root, row),
                    search_index=indices[condition],
                    max_turns=args.max_turns,
                    max_actions=args.max_actions,
                    max_sql_executions=args.max_sql_executions,
                    tools_factory=tools_factory,
                )
            except Exception as error:
                output[condition] = {
                    "example_id": example_id,
                    "dataset_id": row["dataset_id"],
                    "database_id": row["database_id"],
                    "source_database_id": row["source_database_id"],
                    "upstream_split": row["upstream_split"],
                    "method_id": METHOD_IDS[condition],
                    "asset_condition": condition,
                    "status": "error",
                    "error_type": type(error).__name__,
                    "error": str(error)[:1000],
                    "sql": "",
                }
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
            print(f"[evoschema-main {count}/{len(futures)}]", flush=True)

    ordered: dict[str, list[dict[str, Any]]] = {}
    for condition, path in paths.items():
        ordered[condition] = [
            completed[condition][str(row["example_id"])] for row in rows
        ]
        _write_atomic(path, ordered[condition])
    summary = {
        "protocol": _generation_protocol(conditions),
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
            "audit_log_path": (
                str(client.audit_log_path) if client.audit_log_path else None
            ),
        },
        "embedding": {
            "model_id": "BAAI/bge-m3",
            "device": "cpu",
            "minilm_used": False,
            "fingerprint": encoder.fingerprint,
            "documents": len(full_documents),
            "unique_retrieval_texts": unique_embedding_texts,
        },
        "evidence_boundary": {
            "raw_chess_autolink": (
                "current evolved catalog + current values/FKs/execution only; no old "
                "snapshot, lineage, history, KB, or ontology"
            ),
            "full": (
                "same current evidence + automatic previous/current schema-diff lineage "
                "+ target-isolated historical SQL compiled to current identifiers + "
                "typed operational FK ontology"
            ),
            "flat": (
                "the same lineage/history/ontology retrieval documents and prompt as "
                "full, with semantic-to-physical bindings and injected ontology edges "
                "removed"
            ),
            "runtime_adapter": (
                "structural evolution reverse compiler exposes the relation-changing "
                "current schema over immutable storage and rejects legacy identifiers; "
                "it is not included in prompts or retrieval"
                if relation_change_assets
                else "hidden identifier bijection emulates the evolved SQLite database "
                "and rejects legacy identifiers; it is not included in prompts or retrieval"
            ),
            "evaluator_manifest_read": False,
            "target_workload_sql_read": not external_baseline_only,
        },
        "external_baseline_scope": {
            "chess_react": "method-faithful call-matched adapter, not authors' code",
            "autolink_react": "method-faithful call-matched adapter, not authors' code",
        },
        "budgets": {
            "max_turns": args.max_turns,
            "max_actions": args.max_actions,
            "max_sql_executions": args.max_sql_executions,
            "token_budget": client.token_budget_status(),
        },
    }
    name = "GENERATION_SUMMARY_RESUMED.json" if args.resume else "GENERATION_SUMMARY.json"
    if args.resume:
        _write_latest_json(args.output_root / name, summary)
    else:
        _write_json(args.output_root / name, summary)
    print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
