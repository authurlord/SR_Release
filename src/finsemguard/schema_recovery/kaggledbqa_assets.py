"""Gold-blind KaggleDBQA recovery assets for the released test split.

KaggleDBQA's released ``KaggleDBQA_tables.json`` mixes physical SQLite
identifiers with human-written semantic labels, descriptions, value enums, and
database overviews.  This module projects that file immediately onto the
physical Spider fields and never copies the released semantic fields into a
recovery prompt.

The released few-shot SQL is usable as historical workload evidence, but the
benchmark has no official semantic-cluster IDs.  To guard against the most
direct train/test leakage, :func:`materialize_kaggledbqa_safe_history` removes
every few-shot query whose literal-masked, normalized SQL AST also occurs in
the complete released test split.  The boundary is intentionally named
``AST-template-disjoint`` rather than ``cluster-disjoint``.
"""

from __future__ import annotations

from collections import defaultdict
from hashlib import sha256
import json
from pathlib import Path
import sqlite3
from typing import Any

import sqlglot
from sqlglot import exp

from finsemguard.schema_recovery.drspider_assets import (
    FORBIDDEN_SCHEMA_FIELDS,
    _canonical_json,
    _column_id,
    _contains_forbidden_key,
    _database_path,
    _history_by_column,
    _load_jsonl,
    _load_physical_schema,
    _physical_schema_maps,
    _sha256_file,
    _stable_id,
    _validate_sqlite_physical_schema,
    _value_profile,
    _write_immutable,
)


FORMAT_VERSION = "kaggledbqa_gold_blind_recovery_assets_v1"
HISTORY_PROTOCOL = "kaggledbqa_ast_template_disjoint_sql_history_v1"
EXPECTED_DATABASES = {
    "GeoNuclearData",
    "GreaterManchesterCrime",
    "Pesticide",
    "StudentMathScore",
    "TheHistoryofBaseball",
    "USWildFires",
    "WhatCDHipHop",
    "WorldSoccerDataBase",
}


def _literal_masked_ast(sql: str) -> str:
    """Return a stable SQLite AST template, masking only literal values."""

    statements = sqlglot.parse(sql, read="sqlite")
    if len(statements) != 1 or statements[0] is None:
        raise ValueError("history/test SQL must contain exactly one statement")
    tree = statements[0].copy()
    for node in list(tree.walk()):
        if isinstance(node, (exp.Literal, exp.Boolean, exp.Null)):
            node.replace(exp.Placeholder())
    return tree.sql(dialect="sqlite", normalize=True, pretty=False)


def _template_sha256(sql: str) -> str:
    return sha256(_literal_masked_ast(sql).encode("utf-8")).hexdigest()


def _released_split_files(
    data_root: Path, suffix: str
) -> dict[str, Path]:
    files = {
        path.stem[: -len(suffix)]: path
        for path in sorted((data_root / "examples").glob(f"*{suffix}.json"))
    }
    if set(files) != EXPECTED_DATABASES:
        raise ValueError(
            f"unexpected KaggleDBQA {suffix} database set: "
            f"{sorted(set(files) ^ EXPECTED_DATABASES)}"
        )
    return files


def materialize_kaggledbqa_safe_history(
    *,
    data_root: Path,
    output: Path,
    manifest_output: Path,
) -> dict[str, Any]:
    """Freeze SQL-only few-shot history after complete-test AST exclusion.

    Test SQL is read only by this boundary-building step and is used only to
    construct the exclusion set.  No test SQL, question, or semantic schema
    field is copied to the history artifact.
    """

    fewshot_files = _released_split_files(data_root, "_fewshot")
    test_files = _released_split_files(data_root, "_test")
    test_templates: dict[str, set[str]] = {}
    test_rows = 0
    for database_id, path in sorted(test_files.items()):
        rows = json.loads(path.read_text(encoding="utf-8"))
        test_rows += len(rows)
        test_templates[database_id] = {
            _template_sha256(str(row["query"])) for row in rows
        }

    retained: list[dict[str, Any]] = []
    excluded: dict[str, int] = defaultdict(int)
    fewshot_rows = 0
    for database_id, path in sorted(fewshot_files.items()):
        rows = json.loads(path.read_text(encoding="utf-8"))
        fewshot_rows += len(rows)
        for index, row in enumerate(rows):
            sql = str(row["query"]).strip()
            template = _template_sha256(sql)
            if template in test_templates[database_id]:
                excluded[database_id] += 1
                continue
            retained.append(
                {
                    "history_id": (
                        f"kaggledbqa:fewshot:{database_id}:{index:03d}"
                    ),
                    "database_id": database_id,
                    "sql": sql,
                    "source_split": "fewshot",
                    "ast_template_sha256": template,
                }
            )

    retained.sort(key=lambda row: str(row["history_id"]))
    retained_templates = {
        (str(row["database_id"]), str(row["ast_template_sha256"]))
        for row in retained
    }
    heldout_templates = {
        (database_id, template)
        for database_id, templates in test_templates.items()
        for template in templates
    }
    overlap = retained_templates & heldout_templates
    if overlap:
        raise AssertionError("test AST template leaked into historical SQL")
    serialized = "".join(
        json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n"
        for row in retained
    )
    if any(
        key in serialized
        for key in (
            '"question"',
            '"column_descriptions"',
            '"db_overview"',
            '"value_enums"',
        )
    ):
        raise AssertionError("question or released semantic field leaked into history")

    output_sha256 = sha256(serialized.encode("utf-8")).hexdigest()
    source_sha256 = {
        "fewshot": {
            database_id: _sha256_file(path)
            for database_id, path in sorted(fewshot_files.items())
        },
        "test_exclusion_only": {
            database_id: _sha256_file(path)
            for database_id, path in sorted(test_files.items())
        },
    }
    manifest = {
        "protocol": HISTORY_PROTOCOL,
        "claim_boundary": (
            "Released few-shot SQL only, after literal-masked normalized-AST "
            "template exclusion against the complete released test split. "
            "KaggleDBQA has no official semantic-cluster IDs, so this is not "
            "claimed to prove semantic-cluster disjointness."
        ),
        "history": str(output.resolve()),
        "fewshot_rows": fewshot_rows,
        "test_rows_used_for_exclusion_only": test_rows,
        "retained_rows": len(retained),
        "excluded_rows": sum(excluded.values()),
        "excluded_rows_by_database": dict(sorted(excluded.items())),
        "retained_ast_template_test_overlap": 0,
        "output_sha256": output_sha256,
        "source_sha256": source_sha256,
        "leakage_assertions": {
            "history_source_split": "fewshot",
            "test_sql_read_for_exclusion_only": True,
            "test_sql_copied": False,
            "question_field_consumed": False,
            "question_field_copied": False,
            "released_semantic_schema_consumed": False,
            "released_semantic_schema_copied": False,
            "official_semantic_cluster_ids_available": False,
            "ast_template_disjoint": True,
        },
    }
    _write_immutable(output, serialized)
    _write_immutable(
        manifest_output,
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True)
        + "\n",
    )
    return manifest

def _validated_history(
    history_path: Path, history_manifest_path: Path
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    rows = _load_jsonl(history_path)
    manifest = json.loads(history_manifest_path.read_text(encoding="utf-8"))
    if manifest.get("protocol") != HISTORY_PROTOCOL:
        raise ValueError("historical SQL manifest has the wrong protocol")
    if str(manifest.get("output_sha256")) != _sha256_file(history_path):
        raise ValueError("historical SQL manifest hash does not match history")
    if int(manifest.get("retained_rows", -1)) != len(rows):
        raise ValueError("historical SQL manifest row count does not match history")
    assertions = manifest.get("leakage_assertions", {})
    required = {
        "test_sql_copied": False,
        "question_field_copied": False,
        "released_semantic_schema_copied": False,
        "ast_template_disjoint": True,
    }
    if any(assertions.get(key) != value for key, value in required.items()):
        raise ValueError("historical SQL manifest does not satisfy leakage boundary")
    if int(manifest.get("retained_ast_template_test_overlap", -1)) != 0:
        raise ValueError("historical SQL is not test-AST-template-disjoint")
    if any(str(row.get("source_split")) != "fewshot" for row in rows):
        raise ValueError("historical SQL contains a non-fewshot row")
    if any("question" in row for row in rows):
        raise ValueError("historical SQL contains natural-language questions")
    return rows, manifest


def materialize_kaggledbqa_recovery_assets(
    *,
    online_manifest: Path,
    data_root: Path,
    historical_sql_kb: Path,
    historical_sql_kb_manifest: Path,
    benchmark_output: Path,
    manifest_output: Path,
    values_on: bool = True,
    value_sample_limit: int = 5,
    max_history_per_column: int = 8,
) -> dict[str, Any]:
    """Freeze all-column physical recovery inputs for KaggleDBQA test."""

    if value_sample_limit < 1 or max_history_per_column < 1:
        raise ValueError("sample/history limits must be positive")
    online_rows = _load_jsonl(online_manifest)
    history_rows, history_manifest = _validated_history(
        historical_sql_kb, historical_sql_kb_manifest
    )
    if not online_rows:
        raise ValueError("online manifest is empty")
    if any(str(row.get("dataset_id")) != "kaggledbqa" for row in online_rows):
        raise ValueError("online manifest must contain only kaggledbqa rows")
    if any(str(row.get("upstream_split")) != "test" for row in online_rows):
        raise ValueError("automatic KaggleDBQA recovery accepts test rows only")
    selected_example_ids = {str(row["example_id"]) for row in online_rows}
    if len(selected_example_ids) != len(online_rows):
        raise ValueError("online manifest contains duplicate example_id")

    contexts: dict[str, dict[str, Any]] = {}
    for row in online_rows:
        database_id = str(row["database_id"])
        physical_target = str(_database_path(data_root, row))
        projected = {
            "schema_manifest": str(row["schema_manifest"]),
            "database_id": database_id,
            "database_or_answer_target": str(
                row["database_or_answer_target"]
            ),
            "sqlite_path": physical_target,
        }
        prior = contexts.setdefault(database_id, projected)
        if prior != projected:
            raise ValueError(
                f"one KaggleDBQA database maps to multiple targets: {database_id}"
            )

    records: list[dict[str, Any]] = []
    context_audits: list[dict[str, Any]] = []
    schema_source_hashes: dict[str, str] = {}
    sqlite_source_hashes: dict[str, str] = {}
    for schema_context, context in sorted(contexts.items()):
        schema, schema_path = _load_physical_schema(
            data_root,
            context["schema_manifest"],
            context["database_id"],
        )
        columns, table_columns, relationships = _physical_schema_maps(schema)
        database = Path(context["sqlite_path"])
        connection = sqlite3.connect(
            f"file:{database.resolve()}?mode=ro", uri=True
        )
        try:
            _validate_sqlite_physical_schema(connection, columns)
            history, history_audit = _history_by_column(
                history_rows,
                database_id=context["database_id"],
                schema_context=schema_context,
                table_columns=table_columns,
                selected_example_ids=selected_example_ids,
                max_per_column=max_history_per_column,
            )
            for column in columns:
                table = str(column["table"])
                name = str(column["column"])
                column_key = (table.casefold(), name.casefold())
                column_identifier = _column_id(schema_context, table, name)
                related = [
                    relationship
                    for relationship in relationships
                    if relationship["source"].casefold()
                    == f"{table}.{name}".casefold()
                    or relationship["target"].casefold()
                    == f"{table}.{name}".casefold()
                ]
                if values_on:
                    value_profile = _value_profile(
                        connection,
                        table=table,
                        column=name,
                        sample_limit=value_sample_limit,
                    )
                else:
                    value_profile = {
                        "enabled": False,
                        "observed_values": [],
                        "low_cardinality": None,
                        "profile_truncated": None,
                    }
                value_profile = {
                    "evidence_id": _stable_id(
                        "value_profile", column_identifier
                    ),
                    **value_profile,
                }
                raw_schema = {
                    "evidence_id": _stable_id(
                        "raw_schema", column_identifier
                    ),
                    "schema_context": schema_context,
                    "table": table,
                    "column": name,
                    "declared_type": str(column["declared_type"]),
                    "primary_key": bool(column["primary_key"]),
                }
                relationship_evidence = [
                    {
                        "evidence_id": _stable_id(
                            "relationship",
                            {
                                "schema_context": schema_context,
                                **relationship,
                            },
                        ),
                        **relationship,
                    }
                    for relationship in related
                ]
                records.append(
                    {
                        "column_id": column_identifier,
                        "dataset": "kaggledbqa",
                        "db_id": context["database_id"],
                        "schema_context": schema_context,
                        "table": table,
                        "column": name,
                        "ambiguity_tags": ["unassessed_all_user_columns"],
                        "is_ambiguous": True,
                        "evidence": {
                            "raw_schema": raw_schema,
                            "relationships": relationship_evidence,
                            "value_profile": value_profile,
                            "history_sql": history.get(column_key, []),
                            "workload_history": [],
                        },
                    }
                )
        finally:
            connection.close()
        schema_source_hashes[str(schema_path)] = _sha256_file(schema_path)
        sqlite_source_hashes[str(database)] = _sha256_file(database)
        context_audits.append(
            {
                "schema_context": schema_context,
                "database_id": context["database_id"],
                "columns": len(columns),
                **history_audit,
            }
        )

    records.sort(key=lambda row: str(row["column_id"]))
    if len({row["column_id"] for row in records}) != len(records):
        raise ValueError("duplicate recovery column_id")
    if any(_contains_forbidden_key(row) for row in records):
        raise AssertionError("gold/question/evaluator key leaked into benchmark")
    serialized_records = "".join(
        json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n"
        for row in records
    )
    online_questions = [
        str(row["question"])
        for row in online_rows
        if str(row.get("question", "")).strip()
    ]
    if any(question in serialized_records for question in online_questions):
        raise AssertionError("online question text leaked into benchmark")

    benchmark_sha256 = sha256(serialized_records.encode("utf-8")).hexdigest()
    freeze_material = {
        "format_version": FORMAT_VERSION,
        "online_manifest_sha256": _sha256_file(online_manifest),
        "historical_sql_kb_sha256": _sha256_file(historical_sql_kb),
        "historical_sql_kb_manifest_sha256": _sha256_file(
            historical_sql_kb_manifest
        ),
        "schema_source_sha256": schema_source_hashes,
        "sqlite_source_sha256": sqlite_source_hashes,
        "column_ids": [row["column_id"] for row in records],
        "values_on": values_on,
        "value_sample_limit": value_sample_limit,
        "max_history_per_column": max_history_per_column,
        "benchmark_sha256": benchmark_sha256,
    }
    manifest = {
        "format_version": FORMAT_VERSION,
        "freeze_id": sha256(
            _canonical_json(freeze_material).encode("utf-8")
        ).hexdigest(),
        "claim_boundary": (
            "Automatic, gold-blind recovery input for released KaggleDBQA "
            "test questions. Released semantic labels/descriptions/overview/"
            "enums and evaluator gold are excluded. Historical SQL is released "
            "few-shot SQL with complete-test AST-template exclusion."
        ),
        "benchmark": str(benchmark_output.resolve()),
        "columns": len(records),
        "contexts": len(contexts),
        "online_test_rows": len(online_rows),
        "values_on": values_on,
        "context_audits": context_audits,
        "history_boundary": {
            "protocol": history_manifest["protocol"],
            "retained_rows": history_manifest["retained_rows"],
            "excluded_rows": history_manifest["excluded_rows"],
            "retained_ast_template_test_overlap": 0,
            "official_semantic_cluster_ids_available": False,
        },
        "source_sha256": {
            "online_manifest": _sha256_file(online_manifest),
            "historical_sql_kb": _sha256_file(historical_sql_kb),
            "historical_sql_kb_manifest": _sha256_file(
                historical_sql_kb_manifest
            ),
            "schema_manifests": schema_source_hashes,
            "sqlite_databases": sqlite_source_hashes,
        },
        "benchmark_sha256": benchmark_sha256,
        "leakage_assertions": {
            "evaluator_sidecar_read": False,
            "released_semantic_fields_consumed": False,
            "forbidden_schema_fields": sorted(
                FORBIDDEN_SCHEMA_FIELDS
                | {"db_overview", "value_enums"}
            ),
            "all_non_sqlite_user_columns_materialized": True,
            "column_selection_uses_question_or_gold": False,
            "online_question_text_copied": False,
            "history_question_text_copied": False,
            "history_sql_exact_physical_validation": True,
            "history_source_split": "fewshot",
            "test_ast_template_overlap": False,
            "semantic_cluster_disjointness_claimed": False,
        },
    }
    _write_immutable(benchmark_output, serialized_records)
    _write_immutable(
        manifest_output,
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True)
        + "\n",
    )
    return manifest
