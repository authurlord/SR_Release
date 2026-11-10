#!/usr/bin/env python3
"""Adapt frozen KaggleDBQA recovery and released KB into RRCE ontology assets."""

from __future__ import annotations

import argparse
from collections import defaultdict
from hashlib import sha256
import json
from pathlib import Path
import re
from typing import Any

from finsemguard.e2e.livesqlbench_runner import _load_jsonl
from finsemguard.schema_recovery.performance_recover import (
    SEMANTIC_TYPES,
    materialize_table_recovery_inputs,
)


def _sha(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def _write_immutable(path: Path, rows: list[dict[str, Any]]) -> None:
    content = "".join(
        json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in rows
    )
    if path.exists():
        if path.read_text(encoding="utf-8") != content:
            raise FileExistsError(f"refusing to overwrite different artifact: {path}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(content, encoding="utf-8")
    temporary.replace(path)


def _surface(value: str) -> str:
    value = re.sub(r"(?<=[a-z0-9])(?=[A-Z])", " ", value)
    return re.sub(r"[^A-Za-z0-9]+", " ", value).strip().lower()


def _unique(values: list[Any], limit: int = 8) -> list[str]:
    output: list[str] = []
    seen: set[str] = set()
    for value in values:
        text = re.sub(r"\s+", " ", str(value or "")).strip()
        if not text or text == "*" or text.casefold() in seen:
            continue
        seen.add(text.casefold())
        output.append(text[:160])
        if len(output) >= limit:
            break
    return output


def _semantic_type(value: Any) -> str:
    normalized = str(value or "unknown").strip().casefold()
    mapping = {
        "datetime": "date",
        "number": "quantity",
        "numeric": "quantity",
        "categorical": "category",
        "string": "text",
    }
    normalized = mapping.get(normalized, normalized)
    return normalized if normalized in SEMANTIC_TYPES else "unknown"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--column-inputs", type=Path, required=True)
    parser.add_argument("--historical-sql", type=Path, required=True)
    parser.add_argument("--online", type=Path, required=True)
    parser.add_argument("--column-recovery", type=Path, required=True)
    parser.add_argument("--schema-manifest", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    args = parser.parse_args()

    table_inputs_path = args.output_root / "table_inputs.jsonl"
    table_inputs_manifest = args.output_root / "TABLE_INPUTS_MANIFEST.json"
    materialize_table_recovery_inputs(
        column_benchmark=args.column_inputs,
        historical_sql_kb=args.historical_sql,
        online_manifest=args.online,
        output=table_inputs_path,
        manifest_output=table_inputs_manifest,
        max_workload_examples=12,
    )
    table_inputs = _load_jsonl(table_inputs_path)
    column_recovery = {
        str(row["column_id"]): dict(row.get("prediction") or {})
        for row in _load_jsonl(args.column_recovery)
    }
    column_sources = {
        str(row["column_id"]): row for row in _load_jsonl(args.column_inputs)
    }
    if len(column_recovery) != len(_load_jsonl(args.column_recovery)):
        raise ValueError("duplicate column recovery IDs")

    recovery_rows: list[dict[str, Any]] = []
    for table_input in table_inputs:
        context = str(table_input["schema_context"])
        table = str(table_input["physical_table"])
        columns = []
        for source in table_input["columns"]:
            physical = str(source["physical_column"])
            column_id = f"column::{context}::{table}::{physical}"
            prediction = dict(column_recovery.get(column_id) or {})
            canonical = str(prediction.get("canonical_name") or "")
            description = str(prediction.get("description") or "").strip()
            aliases = _unique([_surface(physical), canonical])
            columns.append(
                {
                    "physical_column": physical,
                    "aliases": aliases,
                    "retrieval_gloss": description[:300],
                    "semantic_type": _semantic_type(
                        prediction.get("semantic_type")
                    ),
                    "query_phrases": _unique([canonical, description], limit=4),
                    "observed_values": list(source.get("observed_values") or [])[:5],
                }
            )
        recovery_rows.append(
            {
                "input_id": table_input["input_id"],
                "schema_context": context,
                "physical_table": table,
                "method_id": "kaggledbqa_frozen_column_recovery_to_rrce_v1",
                "prediction": {
                    "physical_table": table,
                    "table_aliases": _unique([_surface(table)]),
                    "purpose": "",
                    "columns": columns,
                },
            }
        )

    schemas = json.loads(args.schema_manifest.read_text(encoding="utf-8"))
    knowledge_rows: list[dict[str, Any]] = []
    for schema in schemas:
        context = str(schema["db_id"])
        physical_tables = [str(value) for value in schema["table_names_original"]]
        semantic_tables = [str(value) for value in schema.get("table_names") or physical_tables]
        physical_columns = schema["column_names_original"]
        semantic_columns = schema.get("column_names") or physical_columns
        normalized_columns = schema.get(
            "column_names_manually_normalized_alternative"
        ) or []
        descriptions = schema.get("column_descriptions") or []
        for index, (owner, physical_column) in enumerate(physical_columns):
            if int(owner) < 0:
                continue
            table = physical_tables[int(owner)]
            semantic = str(semantic_columns[index][1])
            normalized = (
                str(normalized_columns[index][1])
                if index < len(normalized_columns)
                else ""
            )
            description = str(descriptions[index]) if index < len(descriptions) else ""
            aliases = _unique(
                [semantic_tables[int(owner)], semantic, normalized, _surface(physical_column)]
            )
            if not aliases and not description.strip("*"):
                continue
            evidence_id = "kaggledbqa_kb." + sha256(
                f"{context}\0{table}\0{physical_column}\0{description}".encode()
            ).hexdigest()[:24]
            knowledge_rows.append(
                {
                    "schema_context": context,
                    "physical_identifier": f"{table}.{physical_column}",
                    "relation": "released_schema_semantic_mapping",
                    "aliases": aliases,
                    "semantic_type": "unknown",
                    "description": "" if description == "*" else description,
                    "source_name": "KaggleDBQA_released_schema_KB",
                    "evidence_id": evidence_id,
                    "confidence": 1.0,
                }
            )

    recovery_path = args.output_root / "table_recovery.jsonl"
    knowledge_path = args.output_root / "knowledge.jsonl"
    _write_immutable(recovery_path, recovery_rows)
    _write_immutable(knowledge_path, knowledge_rows)
    manifest = {
        "format": "kaggledbqa_operational_ontology_assets_v1",
        "table_inputs": len(table_inputs),
        "columns": sum(len(row["columns"]) for row in table_inputs),
        "table_recovery_rows": len(recovery_rows),
        "knowledge_rows": len(knowledge_rows),
        "sql_only_workload_patterns": sum(
            not str(history.get("question") or "").strip()
            for row in table_inputs
            for history in row.get("target_disjoint_workload") or []
        ),
        "evaluator_manifest_read": False,
        "baseline_kb_access": False,
        "treatment_kb_access": True,
        "sources": {
            "column_inputs": _sha(args.column_inputs),
            "historical_sql": _sha(args.historical_sql),
            "online": _sha(args.online),
            "column_recovery": _sha(args.column_recovery),
            "schema_manifest": _sha(args.schema_manifest),
        },
        "outputs": {
            "table_inputs": _sha(table_inputs_path),
            "table_recovery": _sha(recovery_path),
            "knowledge": _sha(knowledge_path),
        },
    }
    manifest_path = args.output_root / "MANIFEST.json"
    content = json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    if manifest_path.exists() and manifest_path.read_text(encoding="utf-8") != content:
        raise FileExistsError(f"refusing to overwrite different artifact: {manifest_path}")
    if not manifest_path.exists():
        manifest_path.write_text(content, encoding="utf-8")
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
