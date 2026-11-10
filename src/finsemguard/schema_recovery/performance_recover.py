"""Performance-first, table-level multi-view schema recovery.

This path is deliberately different from claim certification.  It keeps several
retrieval-compatible hypotheses, falls back per field rather than per table, and
uses target-disjoint question/SQL workload pairs as automatic supervision.  The
only hard checks protect physical identity and evaluator isolation.
"""

from __future__ import annotations

from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from dataclasses import replace
from hashlib import sha256
import json
from pathlib import Path
import re
import time
from typing import Any

from finsemguard.agent.llm import VLLMClient
from finsemguard.e2e.livesqlbench import CatalogDocument
from finsemguard.schema_recovery.drspider_assets import load_recovery_asset_rows


FORMAT_VERSION = "performance_first_table_recovery_v1"
SYSTEM_PROMPT = """You build a high-recall semantic index for ONE physical database table.
This is offline schema recovery for Text-to-SQL, not question answering.

Use the physical identifiers, types, keys, observed values, and target-disjoint
historical question/SQL pairs in the payload. Historical pairs are the strongest
evidence because their SQL was validated against this exact physical schema. Expand
abbreviations and synonyms, and preserve multiple plausible natural-language surface
forms when evidence is incomplete. Prioritize recall: do not refuse, abstain, or drop a
physical column merely because its meaning is uncertain. Do not rename or modify any
physical identifier.

Return one JSON object with exactly: physical_table, table_aliases, purpose, columns.
columns must contain every supplied physical column exactly once. Each column object
has exactly: physical_column, aliases, retrieval_gloss, semantic_type, query_phrases.
aliases and query_phrases are arrays of concise strings. retrieval_gloss is one short
sentence. semantic_type is one of identifier, category, code, date, currency, count,
ratio, rate, duration, quantity, text, boolean, unknown. Use 2-8 useful aliases where
possible, including singular/plural and common question wording. Output JSON only."""

SEMANTIC_TYPES = {
    "identifier",
    "category",
    "code",
    "date",
    "currency",
    "count",
    "ratio",
    "rate",
    "duration",
    "quantity",
    "text",
    "boolean",
    "unknown",
}
ABBREVIATIONS = {
    "addr": "address",
    "amt": "amount",
    "avg": "average",
    "cnt": "count",
    "code": "code",
    "cust": "customer",
    "dept": "department",
    "desc": "description",
    "dob": "date of birth",
    "doc": "document",
    "dt": "date",
    "emp": "employee",
    "fname": "first name",
    "id": "identifier",
    "lname": "last name",
    "max": "maximum",
    "min": "minimum",
    "mgr": "manager",
    "no": "number",
    "num": "number",
    "qty": "quantity",
    "ref": "reference",
    "src": "source",
    "stu": "student",
    "tel": "telephone",
    "tmp": "template",
    "tot": "total",
    "type": "type",
    "yr": "year",
}


def _canonical_json(value: Any) -> str:
    return json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    )


def _stable_id(prefix: str, value: Any) -> str:
    return f"{prefix}.{sha256(_canonical_json(value).encode()).hexdigest()[:24]}"


def _sha256_file(path: Path) -> str:
    digest = sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _write_immutable(path: Path, content: str) -> None:
    if path.exists():
        if path.read_text(encoding="utf-8") != content:
            raise FileExistsError(f"refusing to mutate frozen artifact: {path}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(content, encoding="utf-8")
    temporary.replace(path)


def _surface_forms(identifier: str) -> list[str]:
    spaced = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", identifier)
    spaced = re.sub(r"[^A-Za-z0-9]+", " ", spaced).strip().lower()
    if not spaced:
        return []
    tokens = spaced.split()
    expanded = " ".join(ABBREVIATIONS.get(token, token) for token in tokens)
    forms = [spaced]
    if expanded.casefold() != spaced.casefold():
        forms.append(expanded)
    return forms


def _bounded_strings(value: Any, *, limit: int = 8, max_chars: int = 100) -> list[str]:
    values = value if isinstance(value, list) else [value]
    output: list[str] = []
    seen: set[str] = set()
    for item in values:
        text = re.sub(r"\s+", " ", str(item or "")).strip()[:max_chars]
        folded = text.casefold()
        if not text or folded in seen:
            continue
        seen.add(folded)
        output.append(text)
        if len(output) >= limit:
            break
    return output


def _history_cover(
    history: dict[str, dict[str, Any]], max_examples: int
) -> list[dict[str, Any]]:
    """Greedy deterministic set cover over table columns, then stable fill."""

    remaining = dict(history)
    uncovered = {
        column
        for row in remaining.values()
        for column in row["physical_columns"]
    }
    selected: list[dict[str, Any]] = []
    while remaining and len(selected) < max_examples:
        ranked = sorted(
            remaining.values(),
            key=lambda row: (
                -len(set(row["physical_columns"]) & uncovered),
                -len(row["physical_columns"]),
                str(row["history_id"]),
            ),
        )
        choice = ranked[0]
        selected.append(choice)
        uncovered -= set(choice["physical_columns"])
        remaining.pop(str(choice["history_id"]))
    return selected


def materialize_table_recovery_inputs(
    *,
    column_benchmark: Path,
    historical_sql_kb: Path,
    online_manifest: Path,
    output: Path,
    manifest_output: Path,
    max_workload_examples: int = 12,
) -> dict[str, Any]:
    if max_workload_examples < 1:
        raise ValueError("max_workload_examples must be positive")
    columns = load_recovery_asset_rows(column_benchmark)
    history_rows = load_recovery_asset_rows(historical_sql_kb)
    online_rows = load_recovery_asset_rows(online_manifest)
    history_by_id = {str(row["history_id"]): row for row in history_rows}
    if len(history_by_id) != len(history_rows):
        raise ValueError("historical SQL KB contains duplicate history_id")
    target_ids = {str(row["example_id"]) for row in online_rows}
    target_questions = {
        str(row.get("question", "")).strip().casefold()
        for row in online_rows
        if str(row.get("question", "")).strip()
    }
    if target_ids & set(history_by_id):
        raise ValueError("historical workload overlaps target example IDs")

    grouped: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    for row in columns:
        grouped[(str(row["schema_context"]), str(row["table"]))].append(row)

    table_rows: list[dict[str, Any]] = []
    excluded_question_collisions = 0
    for (schema_context, table), rows in sorted(grouped.items()):
        workload: dict[str, dict[str, Any]] = {}
        relationships: dict[str, dict[str, Any]] = {}
        column_payloads: list[dict[str, Any]] = []
        for row in sorted(rows, key=lambda item: str(item["column"])):
            evidence = row["evidence"]
            for relation in evidence.get("relationships", []):
                relationships[str(relation["evidence_id"])] = relation
            column_history_ids: list[str] = []
            for use in evidence.get("history_sql", []):
                history_id = str(use["history_id"])
                source = history_by_id.get(history_id)
                if source is None or str(source.get("sql", "")).strip() != str(
                    use.get("sql", "")
                ).strip():
                    raise ValueError(
                        f"validated history cannot be joined exactly: {history_id}"
                    )
                question = str(source.get("question", "")).strip()
                # Some public workloads release validated train SQL without the
                # corresponding NL question.  The SQL still carries physical role
                # and join evidence; retain it as a target-disjoint structural
                # pattern instead of discarding the entire history row.
                if question and question.casefold() in target_questions:
                    excluded_question_collisions += 1
                    continue
                entry = workload.setdefault(
                    history_id,
                    {
                        "evidence_id": str(use["evidence_id"]),
                        "history_id": history_id,
                        "question": question,
                        "sql": str(use["sql"]),
                        "physical_columns": [],
                    },
                )
                physical_column = str(row["column"])
                if physical_column not in entry["physical_columns"]:
                    entry["physical_columns"].append(physical_column)
                column_history_ids.append(history_id)
            raw_schema = evidence["raw_schema"]
            value_profile = evidence.get("value_profile", {})
            column_payloads.append(
                {
                    "physical_column": str(row["column"]),
                    "declared_type": str(raw_schema.get("declared_type", "unknown")),
                    "primary_key": bool(raw_schema.get("primary_key", False)),
                    "observed_values": list(value_profile.get("observed_values", [])),
                    "history_ids": sorted(set(column_history_ids)),
                }
            )
        selected_history = _history_cover(workload, max_workload_examples)
        supplied_ids = sorted(
            {
                str(value["evidence_id"])
                for row in rows
                for key in ("raw_schema", "value_profile")
                for value in [row["evidence"].get(key, {})]
                if value.get("evidence_id")
            }
            | set(relationships)
            | {str(row["evidence_id"]) for row in selected_history}
        )
        payload = {
            "format_version": FORMAT_VERSION,
            "schema_context": schema_context,
            "db_id": str(rows[0]["db_id"]),
            "physical_table": table,
            "columns": column_payloads,
            "relationships": [relationships[key] for key in sorted(relationships)],
            "target_disjoint_workload": selected_history,
            "supplied_evidence_ids": supplied_ids,
        }
        payload["input_id"] = _stable_id("table_recovery", payload)
        table_rows.append(payload)

    serialized = "".join(
        json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n"
        for row in table_rows
    )
    manifest = {
        "format_version": FORMAT_VERSION,
        "table_inputs": len(table_rows),
        "columns": sum(len(row["columns"]) for row in table_rows),
        "contexts": len({row["schema_context"] for row in table_rows}),
        "workload_examples": sum(
            len(row["target_disjoint_workload"]) for row in table_rows
        ),
        "tables_without_workload": sum(
            not row["target_disjoint_workload"] for row in table_rows
        ),
        "excluded_exact_target_question_collisions": excluded_question_collisions,
        "target_example_id_overlap": 0,
        "selection_uses_evaluator_manifest": False,
        "released_semantic_fields_consumed": False,
        "source_sha256": {
            "column_benchmark": _sha256_file(column_benchmark),
            "historical_sql_kb": _sha256_file(historical_sql_kb),
            "online_manifest": _sha256_file(online_manifest),
        },
        "output_sha256": sha256(serialized.encode()).hexdigest(),
    }
    _write_immutable(output, serialized)
    _write_immutable(
        manifest_output,
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
    )
    return manifest


def build_recovery_prompt(row: dict[str, Any]) -> tuple[str, str]:
    # BEAVER contains very long compositional SQL.  Passing twelve full queries can
    # exceed a 49k model context before generation starts, while the recovery task
    # only needs the question wording, referenced fields, and a bounded SQL pattern.
    # The unabridged rows remain in the frozen input and operational ontology; this
    # bound applies only to the table-level LLM prompt.
    workload = []
    for history in (row.get("target_disjoint_workload") or [])[:8]:
        workload.append(
            {
                "evidence_id": history.get("evidence_id"),
                "history_id": history.get("history_id"),
                "question": str(history.get("question") or "")[:1200],
                "sql_pattern": str(history.get("sql") or "")[:4500],
                "physical_columns": list(history.get("physical_columns") or []),
            }
        )
    payload = {
        "task": "build_high_recall_table_semantic_index",
        "schema_context": row["schema_context"],
        "physical_table": row["physical_table"],
        "columns": [
            {
                "physical_column": column["physical_column"],
                "declared_type": column.get("declared_type", "unknown"),
                "primary_key": bool(column.get("primary_key", False)),
                "observed_values": list(column.get("observed_values") or [])[:5],
            }
            for column in row["columns"]
        ],
        "relationships": list(row.get("relationships") or [])[:64],
        "target_disjoint_workload": workload,
    }
    while len(_canonical_json(payload)) > 36000 and workload:
        workload.pop()
    return SYSTEM_PROMPT, json.dumps(payload, ensure_ascii=False, indent=2)


def normalize_prediction(row: dict[str, Any], payload: dict[str, Any]) -> dict[str, Any]:
    table = str(row["physical_table"])
    expected = {str(item["physical_column"]): item for item in row["columns"]}
    predicted_columns: dict[str, dict[str, Any]] = {}
    raw_columns = payload.get("columns", [])
    if isinstance(raw_columns, list):
        for candidate in raw_columns:
            if not isinstance(candidate, dict):
                continue
            physical = str(candidate.get("physical_column", "")).strip()
            if physical not in expected or physical in predicted_columns:
                continue
            aliases = _bounded_strings(candidate.get("aliases", []))
            aliases = _bounded_strings([*_surface_forms(physical), *aliases])
            gloss = re.sub(
                r"\s+", " ", str(candidate.get("retrieval_gloss", ""))
            ).strip()[:300]
            semantic_type = str(candidate.get("semantic_type", "unknown")).lower()
            if semantic_type not in SEMANTIC_TYPES:
                semantic_type = "unknown"
            predicted_columns[physical] = {
                "physical_column": physical,
                "aliases": aliases,
                "retrieval_gloss": gloss,
                "semantic_type": semantic_type,
                "query_phrases": _bounded_strings(
                    candidate.get("query_phrases", []), max_chars=140
                ),
                "observed_values": expected[physical].get("observed_values", [])[:5],
                "source": "llm_plus_deterministic_surface_forms",
            }
    missing = []
    normalized_columns = []
    for physical in expected:
        prediction = predicted_columns.get(physical)
        if prediction is None:
            missing.append(physical)
            prediction = {
                "physical_column": physical,
                "aliases": _surface_forms(physical),
                "retrieval_gloss": "",
                "semantic_type": "unknown",
                "query_phrases": [],
                "observed_values": expected[physical].get("observed_values", [])[:5],
                "source": "deterministic_surface_form_fallback",
            }
        normalized_columns.append(prediction)
    table_aliases = _bounded_strings(
        [*_surface_forms(table), *(
            payload.get("table_aliases", [])
            if isinstance(payload.get("table_aliases", []), list)
            else [payload.get("table_aliases", "")]
        )]
    )
    purpose = re.sub(r"\s+", " ", str(payload.get("purpose", ""))).strip()[:400]
    return {
        "physical_table": table,
        "table_name_matched": str(payload.get("physical_table", "")) == table,
        "table_aliases": table_aliases,
        "purpose": purpose,
        "columns": normalized_columns,
        "llm_columns": len(predicted_columns),
        "fallback_columns": missing,
    }


def recover_one(client: VLLMClient, row: dict[str, Any]) -> dict[str, Any]:
    system, user = build_recovery_prompt(row)
    started = time.perf_counter()
    payload, usage = client.chat_json_with_metadata(system, user)
    return {
        "input_id": row["input_id"],
        "schema_context": row["schema_context"],
        "physical_table": row["physical_table"],
        "prediction": normalize_prediction(row, payload),
        "usage": usage,
        "prompt_sha256": sha256(
            _canonical_json({"system": system, "user": user}).encode()
        ).hexdigest(),
        "latency_seconds": round(time.perf_counter() - started, 6),
    }


def recover_tables(
    *,
    client: VLLMClient,
    input_path: Path,
    output: Path,
    concurrency: int = 4,
    resume: bool = False,
) -> list[dict[str, Any]]:
    if concurrency < 1:
        raise ValueError("concurrency must be positive")
    rows = load_recovery_asset_rows(input_path)
    existing = (
        load_recovery_asset_rows(output) if resume and output.is_file() else []
    )
    if output.exists() and not resume:
        raise FileExistsError(f"refusing to overwrite recovery output: {output}")
    existing_by_id = {str(row["input_id"]): row for row in existing}
    unknown = sorted(set(existing_by_id) - {str(row["input_id"]) for row in rows})
    if unknown:
        raise ValueError(f"resume output contains unknown input IDs: {unknown[:5]}")
    by_id = {
        input_id: row
        for input_id, row in existing_by_id.items()
        if "prediction" in row
    }
    pending = [row for row in rows if str(row["input_id"]) not in by_id]
    output.parent.mkdir(parents=True, exist_ok=True)

    def run(row: dict[str, Any]) -> dict[str, Any]:
        try:
            return recover_one(client, row)
        except Exception as error:
            return {
                "input_id": row["input_id"],
                "schema_context": row["schema_context"],
                "physical_table": row["physical_table"],
                "error_type": type(error).__name__,
                "error": str(error)[:1000],
            }

    mode = "a" if output.exists() else "w"
    with output.open(mode, encoding="utf-8") as handle:
        with ThreadPoolExecutor(max_workers=concurrency) as executor:
            for index, (source, result) in enumerate(
                zip(pending, executor.map(run, pending), strict=True), start=1
            ):
                by_id[str(source["input_id"])] = result
                handle.write(json.dumps(result, ensure_ascii=False) + "\n")
                handle.flush()
                print(
                    f"[table-recovery {index}/{len(pending)}] "
                    f"{source['schema_context']}::{source['physical_table']} "
                    f"status={'error' if 'error' in result else 'ok'}",
                    flush=True,
                )
    ordered = [by_id[str(row["input_id"])] for row in rows]
    temporary = output.with_suffix(output.suffix + ".tmp")
    temporary.write_text(
        "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in ordered),
        encoding="utf-8",
    )
    temporary.replace(output)
    return ordered


def compile_performance_overlay(
    *,
    base_documents: list[CatalogDocument],
    table_inputs: list[dict[str, Any]],
    recovery_rows: list[dict[str, Any]],
) -> tuple[list[CatalogDocument], dict[str, Any]]:
    """Compile every structurally valid hypothesis; never gate on confidence."""

    input_by_id = {str(row["input_id"]): row for row in table_inputs}
    recovery_by_id = {str(row["input_id"]): row for row in recovery_rows}
    if len(input_by_id) != len(table_inputs) or len(recovery_by_id) != len(recovery_rows):
        raise ValueError("duplicate table recovery input/result IDs")
    unknown = sorted(set(recovery_by_id) - set(input_by_id))
    if unknown:
        raise ValueError(f"unknown table recovery result IDs: {unknown[:5]}")
    expansion_by_table: dict[tuple[str, str], dict[str, Any]] = {}
    error_tables = 0
    for input_id, source in input_by_id.items():
        result = recovery_by_id.get(input_id)
        if not result or "prediction" not in result:
            error_tables += 1
            normalized = normalize_prediction(source, {})
        else:
            normalized = normalize_prediction(source, result["prediction"])
        expansion_by_table[
            (str(source["schema_context"]), str(source["physical_table"]))
        ] = normalized

    output: list[CatalogDocument] = []
    expanded_columns = 0
    for document in base_documents:
        key = (document.database_id, str(document.table or ""))
        expansion = expansion_by_table.get(key)
        text = document.text
        if expansion is not None and document.kind == "table":
            compact = {
                "aliases": expansion["table_aliases"],
                "purpose": expansion["purpose"],
                "columns": {
                    column["physical_column"]: {
                        "aliases": column["aliases"],
                        "gloss": column["retrieval_gloss"],
                        "type": column["semantic_type"],
                        "query_phrases": column["query_phrases"],
                        "observed_values": column["observed_values"],
                    }
                    for column in expansion["columns"]
                },
            }
            text += "\nperformance_recovery_index: " + _canonical_json(compact)
        elif expansion is not None and document.kind == "column":
            physical = document.name.split(".", 1)[-1]
            match = next(
                (
                    row
                    for row in expansion["columns"]
                    if row["physical_column"] == physical
                ),
                None,
            )
            if match is not None:
                text += "\nperformance_recovery_index: " + _canonical_json(match)
                expanded_columns += 1
        output.append(replace(document, text=text))
    signature = lambda rows: [
        (row.candidate_id, row.database_id, row.kind, row.table, row.name, row.references)
        for row in rows
    ]
    if signature(output) != signature(base_documents):
        raise AssertionError("performance overlay changed physical catalog identity")
    return output, {
        "method": FORMAT_VERSION,
        "confidence_gate": False,
        "semantic_withdrawal": False,
        "per_field_fallback": True,
        "table_inputs": len(table_inputs),
        "recovery_results": len(recovery_rows),
        "error_or_missing_tables": error_tables,
        "expanded_column_documents": expanded_columns,
        "candidate_ids_unchanged": True,
        "physical_graph_unchanged": True,
    }
