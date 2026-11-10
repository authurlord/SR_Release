"""Gold-blind Dr.Spider recovery assets for a frozen online subset.

This module deliberately has no evaluator-manifest input.  It projects released
schema rows onto physical ``*_original`` identifiers, types, primary/foreign keys,
and optionally profiles values from the exact SQLite target selected online.
Historical evidence is SQL-only: natural-language history questions are never
copied into the benchmark or a recovery prompt.

The resulting JSONL follows :mod:`finsemguard.schema_recovery.recover`'s benchmark
contract.  Every non-``sqlite_*`` user column is materialized; eligibility never
depends on the current question or gold SQL.
"""

from __future__ import annotations

from collections import defaultdict
from dataclasses import replace
from hashlib import sha256
import json
from pathlib import Path
import sqlite3
from typing import Any, Iterable

import sqlglot
from sqlglot import exp

from finsemguard.e2e.livesqlbench import CatalogDocument
from finsemguard.schema_recovery.recover import (
    RecoveredSemantics,
    evidence_ids,
)


FORMAT_VERSION = "drspider_gold_blind_recovery_assets_v1"
FORBIDDEN_SCHEMA_FIELDS = {
    "table_names",
    "column_names",
    "column_descriptions",
    "column_names_manually_normalized_alternative",
}
FORBIDDEN_BENCHMARK_KEYS = {
    "question",
    "gold_sql",
    "gold",
    "answer",
    "evaluator",
    "evaluator_only",
}


def _canonical_json(value: Any) -> str:
    return json.dumps(
        value,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    )


def _stable_id(prefix: str, value: Any) -> str:
    digest = sha256(_canonical_json(value).encode("utf-8")).hexdigest()[:24]
    return f"{prefix}.{digest}"


def _sha256_file(path: Path) -> str:
    digest = sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    if not all(isinstance(row, dict) for row in rows):
        raise ValueError(f"{path} contains a non-object JSONL row")
    return rows


def _quote(identifier: str) -> str:
    return '"' + identifier.replace('"', '""') + '"'


def _database_path(data_root: Path, online_row: dict[str, Any]) -> Path:
    target = data_root / str(online_row["database_or_answer_target"])
    if target.is_file():
        return target.resolve()
    candidate = target / f"{online_row['database_id']}.sqlite"
    if not candidate.is_file():
        raise FileNotFoundError(
            f"SQLite database not found for {online_row['database_id']}: "
            f"{candidate}"
        )
    return candidate.resolve()


def _schema_projection(schema: dict[str, Any]) -> dict[str, Any]:
    """Project immediately onto fields allowed to enter recovery evidence."""

    required = {
        "db_id",
        "table_names_original",
        "column_names_original",
        "column_types",
        "primary_keys",
        "foreign_keys",
    }
    missing = sorted(required - set(schema))
    if missing:
        raise ValueError(f"schema row is missing physical fields: {missing}")
    return {field: schema[field] for field in sorted(required)}


def _load_physical_schema(
    data_root: Path, relative_manifest: str, database_id: str
) -> tuple[dict[str, Any], Path]:
    path = (data_root / relative_manifest).resolve()
    rows = json.loads(path.read_text(encoding="utf-8"))
    matching = [
        row for row in rows if str(row.get("db_id")) == database_id
    ]
    if len(matching) != 1:
        raise ValueError(
            f"expected one schema row for {database_id} in {path}, "
            f"found {len(matching)}"
        )
    return _schema_projection(matching[0]), path


def _schema_context_key(online_row: dict[str, Any]) -> str:
    return (
        f"{online_row['schema_manifest']}::"
        f"{online_row['database_id']}"
    )


def _column_id(
    schema_context: str, table: str, column: str
) -> str:
    return f"column::{schema_context}::{table}::{column}"


def _physical_schema_maps(
    schema: dict[str, Any],
) -> tuple[
    list[dict[str, Any]],
    dict[str, dict[str, str]],
    list[dict[str, str]],
]:
    tables = [str(value) for value in schema["table_names_original"]]
    types = [str(value) for value in schema["column_types"]]
    primary_keys = {int(value) for value in schema["primary_keys"]}
    columns: list[dict[str, Any]] = []
    indexed: dict[int, tuple[str, str]] = {}
    table_columns: dict[str, dict[str, str]] = defaultdict(dict)
    for index, item in enumerate(schema["column_names_original"]):
        owner, raw_column = int(item[0]), str(item[1])
        if owner < 0 or raw_column == "*":
            continue
        table = tables[owner]
        if table.casefold().startswith("sqlite_"):
            continue
        column = raw_column
        indexed[index] = (table, column)
        folded_table = table.casefold()
        folded_column = column.casefold()
        if folded_column in table_columns[folded_table]:
            raise ValueError(f"duplicate physical column {table}.{column}")
        table_columns[folded_table][folded_column] = column
        columns.append(
            {
                "index": index,
                "table": table,
                "column": column,
                "declared_type": types[index] if index < len(types) else "",
                "primary_key": index in primary_keys,
            }
        )
    relationships: list[dict[str, str]] = []
    for source_index, target_index in schema["foreign_keys"]:
        source = indexed.get(int(source_index))
        target = indexed.get(int(target_index))
        if source is None or target is None:
            continue
        relationships.append(
            {
                "source": f"{source[0]}.{source[1]}",
                "target": f"{target[0]}.{target[1]}",
            }
        )
    relationships.sort(key=lambda row: (row["source"], row["target"]))
    return columns, dict(table_columns), relationships


def _validate_sqlite_physical_schema(
    connection: sqlite3.Connection,
    columns: list[dict[str, Any]],
) -> None:
    actual_tables = {
        str(row[0]).casefold(): str(row[0])
        for row in connection.execute(
            "SELECT name FROM sqlite_master "
            "WHERE type='table' AND name NOT LIKE 'sqlite_%'"
        )
    }
    actual_columns: dict[str, set[str]] = {}
    for folded_table, physical_table in actual_tables.items():
        actual_columns[folded_table] = {
            str(row[1]).casefold()
            for row in connection.execute(
                f"PRAGMA table_info({_quote(physical_table)})"
            )
        }
    for column in columns:
        table_key = str(column["table"]).casefold()
        column_key = str(column["column"]).casefold()
        if table_key not in actual_tables:
            raise ValueError(
                f"schema manifest table is absent from SQLite: {column['table']}"
            )
        if column_key not in actual_columns[table_key]:
            raise ValueError(
                "schema manifest column is absent from SQLite: "
                f"{column['table']}.{column['column']}"
            )


def _json_safe_value(value: Any) -> Any:
    if isinstance(value, bytes):
        return f"bytes:{value.hex()[:200]}"
    if isinstance(value, str):
        return value[:200]
    if value is None or isinstance(value, (bool, int, float)):
        return value
    return str(value)[:200]


def _value_profile(
    connection: sqlite3.Connection,
    *,
    table: str,
    column: str,
    sample_limit: int,
) -> dict[str, Any]:
    rows = connection.execute(
        f"SELECT DISTINCT {_quote(column)} FROM {_quote(table)} "
        f"WHERE {_quote(column)} IS NOT NULL LIMIT {sample_limit + 1}"
    ).fetchall()
    observed = [_json_safe_value(row[0]) for row in rows]
    return {
        "enabled": True,
        "observed_values": observed[:sample_limit],
        "low_cardinality": len(observed) <= sample_limit,
        "profile_truncated": len(observed) > sample_limit,
    }


def _column_roles(column: exp.Column) -> list[str]:
    roles = []
    for label, expression_type in (
        ("filter", exp.Where),
        ("join", exp.Join),
        ("group", exp.Group),
        ("order", exp.Order),
        ("projection", exp.Select),
        ("aggregation", exp.AggFunc),
    ):
        if column.find_ancestor(expression_type) is not None:
            roles.append(label)
    return roles


def _validated_sql_usage(
    sql: str,
    table_columns: dict[str, dict[str, str]],
) -> dict[tuple[str, str], set[str]] | None:
    """Return exact physical references, or ``None`` for any uncertainty.

    Strict rejection is intentional.  A history statement that cannot be resolved
    against the exact physical context is weaker than no evidence and is dropped.
    """

    try:
        statements = sqlglot.parse(sql, read="sqlite")
    except Exception:
        return None
    if len(statements) != 1 or statements[0] is None:
        return None
    tree = statements[0]
    aliases: dict[str, str] = {}
    query_tables: set[str] = set()
    for table in tree.find_all(exp.Table):
        physical = table.name.casefold()
        if physical not in table_columns:
            return None
        alias = table.alias_or_name.casefold()
        aliases[alias] = physical
        aliases[physical] = physical
        query_tables.add(physical)
    if not query_tables:
        return None
    usage: dict[tuple[str, str], set[str]] = defaultdict(set)
    for column in tree.find_all(exp.Column):
        if column.name == "*":
            continue
        folded_column = column.name.casefold()
        if column.table:
            table = aliases.get(column.table.casefold())
            if table is None:
                return None
            candidates = [table]
        else:
            candidates = [
                table
                for table in query_tables
                if folded_column in table_columns[table]
            ]
        if len(candidates) != 1:
            return None
        table = candidates[0]
        if folded_column not in table_columns[table]:
            return None
        physical_column = table_columns[table][folded_column]
        usage[(table, physical_column.casefold())].update(
            _column_roles(column)
        )
    return dict(usage)


def _history_by_column(
    history_rows: list[dict[str, Any]],
    *,
    database_id: str,
    schema_context: str,
    table_columns: dict[str, dict[str, str]],
    selected_example_ids: set[str],
    max_per_column: int,
) -> tuple[dict[tuple[str, str], list[dict[str, Any]]], dict[str, int]]:
    selected = [
        row
        for row in history_rows
        if str(row.get("database_id")) == database_id
    ]
    overlapping = sorted(
        {
            str(row.get("history_id"))
            for row in selected
            if str(row.get("history_id")) in selected_example_ids
        }
    )
    if overlapping:
        raise AssertionError(
            "historical SQL is not holdout-disjoint: "
            + ", ".join(overlapping[:5])
        )
    output: dict[tuple[str, str], list[dict[str, Any]]] = defaultdict(list)
    accepted = 0
    dropped = 0
    for row in sorted(
        selected,
        key=lambda item: (
            str(item.get("history_id", "")),
            str(item.get("sql", "")),
        ),
    ):
        history_id = str(row.get("history_id", "")).strip()
        sql = str(row.get("sql", "")).strip()
        if not history_id or not sql:
            dropped += 1
            continue
        usage = _validated_sql_usage(sql, table_columns)
        if usage is None:
            dropped += 1
            continue
        accepted += 1
        stable_evidence_id = _stable_id(
            "history_sql",
            {
                "schema_context": schema_context,
                "history_id": history_id,
                "sql": sql,
            },
        )
        for (folded_table, folded_column), roles in usage.items():
            physical_column = table_columns[folded_table][folded_column]
            output[(folded_table, physical_column.casefold())].append(
                {
                    "evidence_id": stable_evidence_id,
                    "history_id": history_id,
                    "roles": sorted(roles),
                    "sql": sql,
                }
            )
    bounded = {
        key: rows[:max_per_column]
        for key, rows in output.items()
    }
    return bounded, {
        "available_exact_database_rows": len(selected),
        "accepted_validated_sql_rows": accepted,
        "dropped_unvalidated_sql_rows": dropped,
    }


def _contains_forbidden_key(value: Any, *, root: bool = True) -> bool:
    if isinstance(value, dict):
        keys = {str(key).casefold() for key in value}
        if keys & FORBIDDEN_BENCHMARK_KEYS or (root and "target" in keys):
            return True
        return any(
            _contains_forbidden_key(item, root=False)
            for item in value.values()
        )
    if isinstance(value, list):
        return any(
            _contains_forbidden_key(item, root=False) for item in value
        )
    return False


def _write_immutable(path: Path, content: str) -> None:
    if path.exists():
        if path.read_text(encoding="utf-8") != content:
            raise FileExistsError(
                f"refusing to mutate frozen recovery asset: {path}"
            )
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(content, encoding="utf-8")
    temporary.replace(path)


def materialize_drspider_recovery_assets(
    *,
    online_manifest: Path,
    data_root: Path,
    historical_sql_kb: Path,
    benchmark_output: Path,
    manifest_output: Path,
    values_on: bool = True,
    value_sample_limit: int = 5,
    max_history_per_column: int = 8,
) -> dict[str, Any]:
    """Freeze a gold-blind, all-column recovery benchmark and its manifest."""

    if value_sample_limit < 1 or max_history_per_column < 1:
        raise ValueError("sample/history limits must be positive")
    online_rows = _load_jsonl(online_manifest)
    history_rows = _load_jsonl(historical_sql_kb)
    if not online_rows:
        raise ValueError("online manifest is empty")
    if any(str(row.get("dataset_id")) != "dr_spider" for row in online_rows):
        raise ValueError("online manifest must contain only dr_spider rows")
    selected_example_ids = {str(row["example_id"]) for row in online_rows}
    if len(selected_example_ids) != len(online_rows):
        raise ValueError("online manifest contains duplicate example_id")

    contexts: dict[str, dict[str, Any]] = {}
    for row in online_rows:
        context_key = _schema_context_key(row)
        physical_target = str(_database_path(data_root, row))
        projected = {
            "schema_manifest": str(row["schema_manifest"]),
            "database_id": str(row["database_id"]),
            "database_or_answer_target": str(
                row["database_or_answer_target"]
            ),
            "sqlite_path": physical_target,
        }
        prior = contexts.setdefault(context_key, projected)
        if prior != projected:
            raise ValueError(
                f"one physical schema context maps to multiple targets: "
                f"{context_key}"
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
                column_identifier = _column_id(
                    schema_context, table, name
                )
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
                        "dataset": "dr_spider",
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
    history_questions = [
        str(row["question"])
        for row in history_rows
        if str(row.get("question", "")).strip()
    ]
    leaked_questions = [
        question
        for question in online_questions + history_questions
        if question in serialized_records
    ]
    if leaked_questions:
        raise AssertionError("natural-language question text leaked into benchmark")

    benchmark_sha256 = sha256(serialized_records.encode("utf-8")).hexdigest()
    freeze_material = {
        "format_version": FORMAT_VERSION,
        "online_manifest_sha256": _sha256_file(online_manifest),
        "historical_sql_kb_sha256": _sha256_file(historical_sql_kb),
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
            "This artifact is an automatic, gold-blind recovery input only. "
            "It does not use released semantic labels or evaluator data."
        ),
        "benchmark": str(benchmark_output.resolve()),
        "columns": len(records),
        "contexts": len(contexts),
        "values_on": values_on,
        "context_audits": context_audits,
        "source_sha256": {
            "online_manifest": _sha256_file(online_manifest),
            "historical_sql_kb": _sha256_file(historical_sql_kb),
            "schema_manifests": schema_source_hashes,
            "sqlite_databases": sqlite_source_hashes,
        },
        "benchmark_sha256": benchmark_sha256,
        "leakage_assertions": {
            "evaluator_sidecar_read": False,
            "released_semantic_fields_consumed": False,
            "forbidden_schema_fields": sorted(FORBIDDEN_SCHEMA_FIELDS),
            "all_non_sqlite_user_columns_materialized": True,
            "column_selection_uses_question_or_gold": False,
            "online_question_text_copied": False,
            "history_question_text_copied": False,
            "history_sql_exact_physical_validation": True,
            "holdout_history_id_overlap": False,
        },
    }
    serialized_manifest = (
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True)
        + "\n"
    )
    _write_immutable(benchmark_output, serialized_records)
    _write_immutable(manifest_output, serialized_manifest)
    return manifest


def _catalog_signature(
    documents: Iterable[CatalogDocument],
) -> list[tuple[Any, ...]]:
    return [
        (
            row.candidate_id,
            row.database_id,
            row.kind,
            row.table,
            row.name,
            row.references,
        )
        for row in documents
    ]


def _is_physical_only_catalog(documents: Iterable[CatalogDocument]) -> bool:
    forbidden = ("semantic label:", "normalized label:", "description:")
    return not any(
        marker in document.text.casefold()
        for document in documents
        for marker in forbidden
    )


def compile_recovery_catalog_overlay(
    *,
    base_documents: list[CatalogDocument],
    benchmark_rows: list[dict[str, Any]],
    recovery_rows: list[dict[str, Any]],
    minimum_confidence: float = 0.6,
) -> tuple[list[CatalogDocument], dict[str, Any]]:
    """Add supported recovery semantics without changing physical catalog identity.

    Errors, low confidence, malformed predictions, and unsupported evidence citations
    all fail closed to the unchanged raw document.  The returned audit makes every
    fallback count visible.
    """

    if not 0.0 <= minimum_confidence <= 1.0:
        raise ValueError("minimum_confidence must be between zero and one")
    if not _is_physical_only_catalog(base_documents):
        raise ValueError(
            "automatic recovery overlay requires a physical-only base catalog"
        )
    benchmark_by_id = {
        str(row["column_id"]): row for row in benchmark_rows
    }
    if len(benchmark_by_id) != len(benchmark_rows):
        raise ValueError("benchmark contains duplicate column_id")
    recovery_by_id = {
        str(row["column_id"]): row for row in recovery_rows
    }
    if len(recovery_by_id) != len(recovery_rows):
        raise ValueError("recovery output contains duplicate column_id")
    unknown = sorted(set(recovery_by_id) - set(benchmark_by_id))
    if unknown:
        raise ValueError(
            f"recovery output contains unknown column IDs: {unknown[:5]}"
        )
    base_ids = {row.candidate_id for row in base_documents}
    missing = sorted(set(benchmark_by_id) - base_ids)
    if missing:
        raise ValueError(
            f"physical catalog is missing benchmark columns: {missing[:5]}"
        )

    accepted: dict[str, dict[str, Any]] = {}
    fallback_reasons: dict[str, int] = defaultdict(int)
    for column_id, benchmark in sorted(benchmark_by_id.items()):
        result = recovery_by_id.get(column_id)
        if result is None:
            fallback_reasons["missing_prediction"] += 1
            continue
        if "error" in result or "prediction" not in result:
            fallback_reasons["recovery_error"] += 1
            continue
        benchmark_ids = evidence_ids(benchmark["evidence"])
        supplied_ids = {
            str(value)
            for value in result.get("supplied_evidence_ids", [])
        }
        try:
            prediction = RecoveredSemantics.model_validate(
                result["prediction"]
            )
        except Exception:
            fallback_reasons["invalid_prediction"] += 1
            continue
        cited_ids = set(prediction.evidence_ids)
        if not supplied_ids <= benchmark_ids or not cited_ids <= supplied_ids:
            fallback_reasons["unsupported_evidence"] += 1
            continue
        if prediction.confidence < minimum_confidence:
            fallback_reasons["low_confidence"] += 1
            continue
        if not prediction.canonical_name.strip() or not prediction.description.strip():
            fallback_reasons["empty_semantics"] += 1
            continue
        accepted[column_id] = {
            "canonical_name": prediction.canonical_name.strip(),
            "description": prediction.description.strip(),
            "semantic_type": prediction.semantic_type,
            "confidence": prediction.confidence,
            "evidence_ids": sorted(cited_ids),
        }

    table_annotations: dict[
        tuple[str, str], list[tuple[str, dict[str, Any]]]
    ] = defaultdict(list)
    for column_id, annotation in accepted.items():
        benchmark = benchmark_by_id[column_id]
        table_annotations[
            (str(benchmark["schema_context"]), str(benchmark["table"]))
        ].append((str(benchmark["column"]), annotation))

    output: list[CatalogDocument] = []
    for document in base_documents:
        annotation = accepted.get(document.candidate_id)
        text = document.text
        if document.kind == "column" and annotation is not None:
            text += (
                "\nautomatic_recovery: "
                + _canonical_json(annotation)
            )
        elif document.kind == "table" and document.table:
            entries = table_annotations.get(
                (document.database_id, document.table), []
            )
            if entries:
                lines = [
                    "automatic_recovery_overlays:",
                    *[
                        f"  {_quote(column)}: {_canonical_json(annotation)}"
                        for column, annotation in sorted(entries)
                    ],
                ]
                text += "\n" + "\n".join(lines)
        output.append(replace(document, text=text))
    if _catalog_signature(output) != _catalog_signature(base_documents):
        raise AssertionError("recovery overlay changed physical catalog identity")
    audit = {
        "claim": "automatic_gold_blind_schema_recovery",
        "minimum_confidence": minimum_confidence,
        "benchmark_columns": len(benchmark_rows),
        "recovery_rows": len(recovery_rows),
        "accepted_columns": len(accepted),
        "raw_fallback_columns": len(benchmark_rows) - len(accepted),
        "fallback_reasons": dict(sorted(fallback_reasons.items())),
        "candidate_ids_unchanged": True,
        "physical_graph_unchanged": True,
        "prediction_evidence_subset_enforced": True,
    }
    return output, audit


def load_recovery_asset_rows(path: Path) -> list[dict[str, Any]]:
    """Public JSONL loader for the materializer/compiler CLI boundary."""

    return _load_jsonl(path)
