"""Thin, local-file adapter over the released SchemaRecovery modules."""
import json
import os
from pathlib import Path
import re
import sqlite3
import sys
from urllib.parse import urlparse


def json_write(path, value):
    Path(path).write_text(json.dumps(value, ensure_ascii=False, indent=2))


def read_rows(text, kind, context):
    """Accept a JSON array, JSONL, or SQL-only history / one-question-per-line."""
    text = text.strip()
    if not text:
        return []
    if text.startswith("["):
        rows = json.loads(text)
    elif text.startswith("{"):
        rows = [json.loads(line) for line in text.splitlines() if line.strip()]
    elif kind == "history":
        import sqlglot
        rows = [{"sql": statement.sql(dialect="sqlite")} for statement in sqlglot.parse(text, read="sqlite") if statement]
    else:
        rows = [{"question": line} for line in text.splitlines() if line.strip()]
    if not isinstance(rows, list):
        raise ValueError(kind + " must be an array or JSONL")
    normalized = []
    for index, row in enumerate(rows):
        if isinstance(row, str):
            row = {"sql" if kind == "history" else "question": row}
        if not isinstance(row, dict):
            raise ValueError(kind + " rows must be objects")
        field = "sql" if kind == "history" else "question"
        if not isinstance(row.get(field), str) or not row[field].strip():
            raise ValueError(f"{kind} row {index + 1}: {field} is required")
        row_context = str(row.get("schema_context") or row.get("database_id") or context)
        if row_context != context:
            raise ValueError("each import contains one database_id; historical schema_context must match it")
        if kind == "history":
            # SQL-only boundary: extra question/answer/score fields never enter construction.
            normalized.append({"history_id": str(row.get("history_id") or f"external:{index + 1}"),
                               "schema_context": context, "sql": row["sql"], "dialect": "sqlite"})
        else:
            normalized.append({"example_id": str(row.get("example_id") or f"external:{index + 1}"),
                               "dataset_id": "external_sqlite", "database_id": context,
                               "question": row["question"],
                               **{key: row[key] for key in ("anchor_sql", "raw_sql") if row.get(key)}})
    identity = "history_id" if kind == "history" else "example_id"
    if len({row[identity] for row in normalized}) != len(normalized):
        raise ValueError("duplicate " + identity)
    return normalized


def physical_catalog(database, context):
    from finsemguard.e2e.livesqlbench import CatalogDocument
    from finsemguard.schema_recovery.joint import quote
    connection = sqlite3.connect(Path(database).resolve().as_uri() + "?mode=ro&immutable=1", uri=True)
    connection.execute("PRAGMA query_only=ON")
    inputs, documents = [], []
    try:
        tables = list(connection.execute("SELECT name, sql FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name"))
        if not tables:
            raise ValueError("SQLite file contains no user tables")
        for table, ddl in tables:
            columns = []
            fks = list(connection.execute(f"PRAGMA foreign_key_list({quote(table)})"))
            relationships = [{"source": f"{table}.{r[3]}", "target": f"{r[2]}.{r[4]}", "evidence_id": f"sqlite_fk::{context}::{table}::{r[0]}"} for r in fks if r[4]]
            for _, name, typ, _, _, pk in connection.execute(f"PRAGMA table_info({quote(table)})"):
                columns.append({"physical_column": name, "declared_type": typ, "primary_key": bool(pk), "observed_values": []})
                documents.append(CatalogDocument(f"column::{context}::{table}::{name}", context, "column", table, f"{table}.{name}",
                                                 f'physical SQLite identifier: {quote(table)}.{quote(name)}\ntype: {typ or "unknown"}'))
            documents.append(CatalogDocument(f"table::{context}::{table}", context, "table", table, table, ddl or "", tuple(sorted({r[2] for r in fks}))))
            inputs.append({"input_id": f"external_catalog::{context}::{table}", "schema_context": context,
                           "physical_table": table, "schema_source": "uploaded_sqlite", "catalogue_complete": True,
                           "columns": columns, "relationships": relationships, "target_disjoint_workload": []})
    finally:
        connection.close()
    return inputs, documents


def build_project(project, emit):
    from finsemguard.ontology_discovery.workload_semantics import WorkloadSemanticLayer
    from finsemguard.e2e.operational_ontology import OperationalOntology
    root, context = Path(project["directory"]), project["database_id"]
    emit("stage", "Read physical SQLite catalogue", {})
    inputs, _ = physical_catalog(root / "database.sqlite", context)
    histories = project["history"]
    emit("stage", "Extract SQL-only semantic objects", {"history_count": len(histories)})
    layer = WorkloadSemanticLayer()
    update = layer.update(histories)
    history_inputs, recovery, _ = layer.export_assets()
    by_table = {row["physical_table"]: row for row in history_inputs}
    recovery_by_table = {row["prediction"]["physical_table"]: row for row in recovery}
    for table in inputs:
        history_table = by_table.get(table["physical_table"], {})
        table["target_disjoint_workload"] = history_table.get("target_disjoint_workload", [])
        row = recovery_by_table.get(table["physical_table"])
        if row:
            row["input_id"] = table["input_id"]
    layer.save(root / "semantic-state.json")
    ontology = layer.augment_ontology(OperationalOntology.from_recovery_inputs(inputs, []))
    json_write(root / "inputs.json", inputs)
    json_write(root / "recovery.json", recovery)
    result = {"id": project["id"], "origin": "local", "title": "Imported SQLite ontology", "database": context,
              "question": project["questions"][0]["question"] if project["questions"] else "SQL history ontology",
              "provenance": {"archive": "Local file import", "database_sha256": project["database_sha256"],
                             "native_package": "finsemguard", "construction": "WorkloadSemanticLayer.update + OperationalOntology"},
              "ontology": {"revision": layer.revision, "sources": [{"evidence_id": "sql_log::" + key, **row} for key, row in layer.records.items()],
                           "objects": layer.objects(), "tables": inputs, "recovery": recovery,
                           "edges": [edge.as_dict() for edge in ontology.edges], "construct": []},
              "prediction": None}
    json_write(root / "built.json", result)
    emit("ontology", "Ontology ready", {**update, "tables": len(inputs), "edges": len(ontology.edges)})
    return result


def validate_settings(settings, *, query=False):
    required = ["base_url", "model"] + (["embedding_base_url", "embedding_model", "reranker_base_url", "reranker_model"] if query else [])
    for key in required:
        if not isinstance(settings.get(key), str) or not settings[key].strip():
            raise ValueError(key + " is required")
    for key in required:
        if key.endswith("url"):
            parsed = urlparse(settings[key])
            if parsed.scheme not in {"http", "https"} or not parsed.hostname or parsed.username or parsed.password:
                raise ValueError(key + " requires an http(s) URL without credentials")
    for key in ["api_key_env"]:
        name = settings.get(key, "SR_DEMO_API_KEY")
        if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", name):
            raise ValueError("invalid credential environment variable name")
    if any("key" in key.casefold() and key != "api_key_env" for key in settings):
        raise ValueError("set model credentials in the server environment; send api_key_env only")
    if settings.get("embedding_model", "bge-m3").casefold() not in {"bge-m3", "baai/bge-m3"}:
        raise ValueError("the native SR retrieval adapter requires BGE-M3")


def model_client(settings, emit):
    from finsemguard.agent.llm import VLLMClient

    class ObservedClient(VLLMClient):
        def _post_chat_completion(self, request):
            emit("model_request", "Model call", {"model": self.model, "request": request})
            response = super()._post_chat_completion(request)
            emit("model_response", "Model response", {"model": response.get("model"), "usage": response.get("usage"), "choices": response.get("choices")})
            return response

    return ObservedClient({"base_url": settings["base_url"], "model": settings["model"],
                           "api_key": os.environ.get(settings.get("api_key_env", "SR_DEMO_API_KEY"), ""),
                           "max_output_tokens": 6144, "request_timeout_seconds": 600, "temperature": 0,
                           "compatibility": settings.get("compatibility", "vllm"), "require_exact_model": True})


def construct_project(project, settings, family, emit):
    from finsemguard.schema_recovery.joint import profile_table, assertions_for_family, reconstruct_family
    validate_settings(settings)
    root = Path(project["directory"])
    result = json.loads((root / "built.json").read_text())
    table, columns = family.get("table"), family.get("columns")
    known = {row["physical_table"]: {column["physical_column"] for column in row["columns"]} for row in result["ontology"]["tables"]}
    if table not in known or not isinstance(columns, list) or not 2 <= len(columns) <= 8 or not set(columns) <= known[table]:
        raise ValueError("select one existing table and 2–8 distinct physical columns")
    emit("stage", "Profile selected column family", {"table": table, "columns": columns})
    profile = profile_table(root / "database.sqlite", project["database_id"], table, columns)
    assertions = assertions_for_family(project["history"], project["database_id"], table, columns)
    if not assertions:
        raise ValueError("selected family has no SQL history evidence")
    emit("profile", "Read-only family observations", profile)
    record = reconstruct_family(profile, assertions, model_client(settings, emit))
    result["ontology"]["construct"] = [r for r in result["ontology"]["construct"] if r["family_id"] != record["family_id"]] + [record]
    json_write(root / "built.json", result)
    emit("construct", "Family interpretation saved", record)
    return result


def update_project(project, payload, emit):
    from finsemguard.ontology_discovery.workload_semantics import WorkloadSemanticLayer
    from finsemguard.ontology_discovery.dependency_update import update_layer
    from finsemguard.e2e.operational_ontology import OperationalOntology
    root, context = Path(project["directory"]), project["database_id"]
    result = json.loads((root / "built.json").read_text())
    layer = WorkloadSemanticLayer.load(root / "semantic-state.json")
    rows = read_rows(str(payload.get("history_text") or ""), "history", context)
    retract = tuple((context, str(identity)) for identity in payload.get("retract_history_ids", []))
    if not rows and not retract:
        raise ValueError("provide changed SQL history rows or retract_history_ids")
    previous = result["ontology"]["objects"]
    emit("stage", "Apply source delta and forward dependency closure", {"upserts": len(rows), "retractions": len(retract)})
    objects, receipt = update_layer(layer, previous, rows, retract=retract)
    layer.save(root / "semantic-state.json")
    history_inputs, recovery, _ = layer.export_assets()
    inputs, _ = physical_catalog(root / "database.sqlite", context)
    by_table = {row["physical_table"]: row for row in history_inputs}
    for table in inputs:
        table["target_disjoint_workload"] = by_table.get(table["physical_table"], {}).get("target_disjoint_workload", [])
    id_by_table = {row["physical_table"]: row["input_id"] for row in inputs}
    for row in recovery:
        if row["prediction"]["physical_table"] in id_by_table:
            row["input_id"] = id_by_table[row["prediction"]["physical_table"]]
    ontology = layer.augment_ontology(OperationalOntology.from_recovery_inputs(inputs, []))
    old_by_id = {row["id"]: row for row in previous}
    new_by_id = {row["id"]: row for row in objects}
    column_changes = [{"physical_identifiers": row["physical_identifiers"],
                       "before": old_by_id.get(identity, {}).get("aliases", []),
                       "after": new_by_id.get(identity, {}).get("aliases", []),
                       "status": "added" if identity not in old_by_id else "removed" if identity not in new_by_id else "updated"}
                      for identity in sorted(old_by_id.keys() | new_by_id.keys())
                      if (row := new_by_id.get(identity, old_by_id.get(identity)))["kind"] == "column"
                      and old_by_id.get(identity) != new_by_id.get(identity)]
    event = {"title": "Local SQL source update", "event_type": "local_source_update", "source": "User supplied SQL history delta",
             "method": "dependency_update.update_layer", "model_calls": 0, "receipt": receipt, "column_changes": column_changes}
    result["maintenance"] = [*result.get("maintenance", []), event]
    result["ontology"].update({"revision": layer.revision, "objects": objects, "tables": inputs, "recovery": recovery,
         "sources": [{"evidence_id": "sql_log::" + key, **row} for key, row in layer.records.items()], "edges": [edge.as_dict() for edge in ontology.edges]})
    project["history"] = [{key: row[key] for key in ("history_id", "schema_context", "sql", "dialect")} for row in layer.records.values()]
    json_write(root / "project.json", project)
    json_write(root / "built.json", result)
    json_write(root / "inputs.json", inputs)
    json_write(root / "recovery.json", recovery)
    emit("maintenance", "Incremental update completed", event)
    return result


def run_queries(project, settings, emit):
    from finsemguard.e2e.graph_evo_main import run_graph_evo_semantic_program_main
    from finsemguard.e2e.react_text2sql import SchemaSearchIndex, build_recovery_documents, run_react_text2sql
    from finsemguard.e2e.operational_ontology import OperationalOntology
    from finsemguard.ontology_discovery.workload_semantics import WorkloadSemanticLayer
    from finsemguard.retrieval.reranker import VLLMRerankerClient
    from run_bird_react_recovery import _OpenAIEmbeddingBackend, BGEEncoder
    validate_settings(settings, query=True)
    if not project["questions"]:
        raise ValueError("questions file is empty")
    root, context = Path(project["directory"]), project["database_id"]
    built = json.loads((root / "built.json").read_text())
    inputs = built["ontology"]["tables"]
    recovery = json.loads((root / "recovery.json").read_text())
    layer = WorkloadSemanticLayer.load(root / "semantic-state.json")
    ontology = layer.augment_ontology(OperationalOntology.from_recovery_inputs(inputs, []))
    _, raw = physical_catalog(root / "database.sqlite", context)
    recovery_docs = build_recovery_documents(inputs, recovery)
    documents = ontology.augment_documents([*raw, *recovery_docs])
    emit("stage", "Encode evidence with native remote BGE-M3 adapter", {"documents": len(documents), "model": settings["embedding_model"]})
    backend = _OpenAIEmbeddingBackend(base_url=settings["embedding_base_url"], model=settings["embedding_model"])
    vectors_array = BGEEncoder._normalize(backend.encode([row.retrieval_text() for row in documents], batch_size=32, max_length=512)["dense_vecs"])
    vectors = {row.candidate_id: vector for row, vector in zip(documents, vectors_array, strict=True)}
    query_cache = {}

    def encode_queries(texts):
        missing = list(dict.fromkeys(text for text in texts if text not in query_cache))
        if missing:
            values = BGEEncoder._normalize(backend.encode_queries(missing, batch_size=32, max_length=512)["dense_vecs"])
            query_cache.update(zip(missing, values, strict=True))
        import numpy as np
        return np.asarray([query_cache[text] for text in texts])

    reranker = VLLMRerankerClient(base_url=settings["reranker_base_url"], model=settings["reranker_model"], timeout_seconds=600)
    if not reranker.healthy():
        raise RuntimeError("configured reranker is unavailable or serves a different model")
    common = {"documents": documents, "raw_documents": raw, "vectors": vectors,
              "encode_query": lambda text: encode_queries([text])[0], "encode_queries": encode_queries,
              "ontology_edges_by_database": {context: [{"left": edge.left, "right": edge.right,
                    "evidence": "+".join(edge.evidence_types), "provenance_ids": list(edge.provenance_ids), "score": edge.score} for edge in ontology.edges]},
              "bindings_by_document": {key: list(value) for key, value in ontology.document_bindings.items()}}
    main_index = SchemaSearchIndex(**common, minimal_join_tree=True, evidence_first_history=True,
                                  rerank_documents=reranker.score, rerank_top_k=30)
    draft_index = SchemaSearchIndex(**common, program_graph=True)
    raw_index = SchemaSearchIndex(documents=raw, raw_documents=raw, vectors={row.candidate_id: vectors[row.candidate_id] for row in raw},
                                 encode_query=common["encode_query"], encode_queries=encode_queries)
    client = model_client(settings, emit)
    from finsemguard.e2e.semantic_scope_contract import query_memory
    memory = query_memory(f"external-sql-history-{layer.revision}", built["ontology"]["construct"])
    memory["additional_source_ids"] = [row["history_id"] for row in project["history"]]
    memory["composition_revision"] = 2
    results = []
    for index, row in enumerate(project["questions"]):
        emit("stage", f"Question {index + 1}/{len(project['questions'])}", {"question": row["question"], "example_id": row["example_id"]})
        anchor = row.get("anchor_sql")
        if not anchor:
            emit("stage", "Generate native program-graph draft", {})
            draft = run_react_text2sql(condition="program_graph_react", row=row, client=client, database=root / "database.sqlite", search_index=draft_index)
            anchor = draft["sql"]
            emit("draft", "Program-graph draft", draft)
        raw_sql = row.get("raw_sql")
        if not raw_sql:
            emit("stage", "Generate native opaque-schema draft", {})
            draft = run_react_text2sql(condition="opaque_react", row=row, client=client, database=root / "database.sqlite", search_index=raw_index)
            raw_sql = draft["sql"]
            emit("draft", "Opaque-schema draft", draft)
        emit("stage", "Run native graph/evolution semantic program", {})
        prediction = run_graph_evo_semantic_program_main(
            condition="minimal_join_tree_react", row=row, client=client, database=root / "database.sqlite",
            search_index=main_index, anchor_sql=anchor, auxiliary_raw_sql=raw_sql,
            evidence_first_history=True, realize_semantic_revision=True, scope_grounded_revision=True,
            witness_consistent_revision=True, grounded_binding_revision=True, scope_faithful_revision=True,
            relational_grain_revision=True, entity_grain_revision=True, lower_eligibility_revision=True,
            physical_execution_python=sys.executable, semantic_memory=memory)
        case = {**built, "id": row["example_id"], "title": row["question"][:64], "question": row["question"], "prediction": prediction,
                "provenance": {**built["provenance"], "archive": "Local API run", "generation_model": settings["model"],
                               "embedding_model": settings["embedding_model"], "reranker_model": settings["reranker_model"]}}
        results.append(case)
        emit("result", "Question completed", {"example_id": row["example_id"], "sql": prediction.get("sql")})
        json_write(root / "query-results.json", results)
    return {"cases": results}
