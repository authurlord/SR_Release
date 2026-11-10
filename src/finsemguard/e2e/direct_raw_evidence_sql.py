"""Direct raw-evidence Text-to-SQL baseline with no discovery tools.

This module is intentionally independent from :mod:`react_text2sql`.  The model
sees only a question, a deterministic rendering of the raw physical schema, and
target-isolated raw historical question/SQL pairs.  It receives no recovered
labels, values, inferred relations, semantic retrieval, graph, lineage, or tool
surface.  One second generation is permitted only after a parser/database error;
the feedback contains the error string and never result rows.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from hashlib import sha256
import json
import math
from pathlib import Path
import re
import sqlite3
from typing import Any, Callable, Iterable, Protocol

import sqlglot
from sqlglot import exp

from finsemguard.retrieval.bm25 import BM25Index


METHOD_ID = "baseline_direct_raw_evidence_v1"
CONSUMER_ID = "direct_generator_one_error_only_repair_v1"

SYSTEM_PROMPT = """You generate one executable {dialect} SQL query.

You are given:
1. a user question,
2. a raw physical database schema whose identifiers may be abbreviated,
   opaque, or evolved,
3. raw historical question-SQL examples.

The historical examples are unprocessed evidence. They may use different
wording or older identifiers. Use only identifiers present in the current
physical schema.

Return one SQL query and no explanation."""

REPAIR_PROMPT = """The SQL failed with the following parser or database error:

{error}

Return one corrected {dialect} SQL query using only identifiers from the
provided raw physical schema. Do not explain."""


class TextGenerationClient(Protocol):
    model: str

    def chat_text_with_metadata(
        self, system: str, user: str
    ) -> tuple[str, dict[str, Any]]: ...


@dataclass(frozen=True)
class RawColumn:
    name: str
    declared_type: str = "unknown"
    primary_key: bool = False


@dataclass(frozen=True)
class RawForeignKey:
    source_table: str
    source_column: str
    target_table: str
    target_column: str


@dataclass(frozen=True)
class RawTable:
    name: str
    columns: tuple[RawColumn, ...]


@dataclass(frozen=True)
class RawPhysicalSchema:
    tables: tuple[RawTable, ...]
    foreign_keys: tuple[RawForeignKey, ...] = ()

    def __post_init__(self) -> None:
        names = [table.name.casefold() for table in self.tables]
        if len(names) != len(set(names)):
            raise ValueError("raw physical schema contains duplicate tables")
        for table in self.tables:
            columns = [column.name.casefold() for column in table.columns]
            if len(columns) != len(set(columns)):
                raise ValueError(f"raw table contains duplicate columns: {table.name}")


@dataclass(frozen=True)
class RawHistoryExample:
    history_id: str
    question: str
    sql: str


@dataclass(frozen=True)
class DirectRawEvidenceConfig:
    history_max_examples: int = 12
    history_max_tokens: int = 8192
    schema_max_tokens: int = 20000
    max_generation_calls: int = 2
    max_repairs: int = 1
    max_output_tokens: int = 2048

    def __post_init__(self) -> None:
        if self.history_max_examples < 0:
            raise ValueError("history_max_examples must be nonnegative")
        if self.history_max_tokens < 0 or self.schema_max_tokens < 1:
            raise ValueError("schema/history token budgets are invalid")
        if self.max_generation_calls != 2 or self.max_repairs != 1:
            raise ValueError(
                "Direct Raw-Evidence baseline is frozen to one generation plus "
                "at most one error-only repair"
            )
        if self.max_output_tokens != 2048:
            raise ValueError("Direct Raw-Evidence max_output_tokens is frozen to 2048")


def _canonical_json(value: Any) -> str:
    return json.dumps(
        value, ensure_ascii=False, sort_keys=True, separators=(",", ":")
    )


def _sha(value: Any) -> str:
    text = value if isinstance(value, str) else _canonical_json(value)
    return sha256(text.encode("utf-8")).hexdigest()


def _estimated_tokens(text: str) -> int:
    """Deterministic tokenizer-free estimate recorded in every prediction.

    Four UTF-8 bytes per token tracks the model prompt budget closely enough for
    packing while remaining stable on machines that do not host the tokenizer.
    The exact serialized prompt is preserved and hashed for later re-tokenization.
    """

    return int(math.ceil(len(text.encode("utf-8")) / 4))


def _clean(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


def _endpoint(value: Any) -> tuple[str, str] | None:
    table, separator, column = str(value or "").rpartition(".")
    if not separator or not table.strip() or not column.strip():
        return None
    return table.strip(), column.strip()


def raw_schema_from_table_inputs(
    rows: Iterable[dict[str, Any]],
    *,
    schema_context: str,
    declared_relationship: Callable[[dict[str, Any]], bool] | None = None,
) -> RawPhysicalSchema:
    """Extract only physical names, types, PKs, and certified declared FKs.

    Values, history IDs, descriptions, recovered fields, and generic relation
    hypotheses in the input rows are deliberately ignored.  A relationship is
    included only when the caller explicitly certifies it as physically declared.
    """

    tables: dict[str, RawTable] = {}
    foreign_keys: dict[tuple[str, str, str, str], RawForeignKey] = {}
    for source in rows:
        context = str(source.get("schema_context") or source.get("db_id") or "")
        if context != schema_context:
            continue
        table_name = str(source.get("physical_table") or "").strip()
        if not table_name:
            raise ValueError("table input lacks physical_table")
        columns = tuple(
            RawColumn(
                name=str(column.get("physical_column") or "").strip(),
                declared_type=str(column.get("declared_type") or "unknown").strip(),
                primary_key=bool(column.get("primary_key")),
            )
            for column in source.get("columns") or []
        )
        if not columns or any(not column.name for column in columns):
            raise ValueError(f"table input lacks physical columns: {table_name}")
        key = table_name.casefold()
        table = RawTable(table_name, columns)
        previous = tables.get(key)
        if previous is not None and previous != table:
            raise ValueError(f"conflicting raw table definitions: {table_name}")
        tables[key] = table
        for relation in source.get("relationships") or []:
            if declared_relationship is None or not declared_relationship(relation):
                continue
            left = _endpoint(relation.get("source") or relation.get("left"))
            right = _endpoint(relation.get("target") or relation.get("right"))
            if left is None or right is None:
                continue
            value = RawForeignKey(left[0], left[1], right[0], right[1])
            signature = tuple(part.casefold() for part in asdict(value).values())
            foreign_keys[signature] = value
    if not tables:
        raise ValueError(f"no raw table inputs for schema context: {schema_context}")
    return RawPhysicalSchema(
        tables=tuple(sorted(tables.values(), key=lambda table: table.name.casefold())),
        foreign_keys=tuple(
            sorted(
                foreign_keys.values(),
                key=lambda edge: (
                    edge.source_table.casefold(),
                    edge.source_column.casefold(),
                    edge.target_table.casefold(),
                    edge.target_column.casefold(),
                ),
            )
        ),
    )


def raw_schema_from_snapshot(snapshot: dict[str, Any]) -> RawPhysicalSchema:
    """Extract the current physical view from a schema snapshot JSON object."""

    tables: list[RawTable] = []
    foreign_keys: list[RawForeignKey] = []
    for source in snapshot.get("tables") or []:
        table_name = str(source.get("name") or "").strip()
        columns = tuple(
            RawColumn(
                name=str(column.get("name") or "").strip(),
                declared_type=str(column.get("declared_type") or "unknown").strip(),
                primary_key=bool(column.get("primary_key")),
            )
            for column in source.get("columns") or []
        )
        if not table_name or not columns or any(not column.name for column in columns):
            raise ValueError("invalid current physical schema snapshot")
        tables.append(RawTable(table_name, columns))
        for edge in source.get("foreign_keys") or []:
            foreign_keys.append(
                RawForeignKey(
                    table_name,
                    str(edge.get("source_column") or "").strip(),
                    str(edge.get("target_table") or "").strip(),
                    str(edge.get("target_column") or "").strip(),
                )
            )
    return RawPhysicalSchema(tuple(tables), tuple(foreign_keys))


def raw_schema_from_sqlite_database(database: Path) -> RawPhysicalSchema:
    """Read only the physical SQLite catalog; never inspect table values."""

    connection = sqlite3.connect(f"file:{database.resolve()}?mode=ro", uri=True)
    try:
        objects = [
            (str(row[0]), str(row[1]))
            for row in connection.execute(
                "SELECT name, type FROM sqlite_master "
                "WHERE type IN ('table', 'view') AND name NOT LIKE 'sqlite_%' "
                "ORDER BY name COLLATE NOCASE"
            )
        ]
        tables: list[RawTable] = []
        foreign_keys: list[RawForeignKey] = []
        for table_name, object_type in objects:
            quoted = '"' + table_name.replace('"', '""') + '"'
            try:
                columns = tuple(
                    RawColumn(
                        name=str(row[1]),
                        declared_type=str(row[2] or "unknown"),
                        primary_key=bool(row[5]),
                    )
                    for row in connection.execute(f"PRAGMA table_info({quoted})")
                )
            except sqlite3.OperationalError:
                # Some released Spider 2.0 SQLite databases contain stale views
                # whose referenced columns no longer exist. Such a view has no
                # usable physical schema; retain every readable table/view and
                # skip only the invalid view without inspecting any row values.
                if object_type == "view":
                    continue
                raise
            if not columns:
                if object_type == "view":
                    continue
                raise ValueError(f"SQLite catalog table has no columns: {table_name}")
            tables.append(RawTable(table_name, columns))
            for row in connection.execute(f"PRAGMA foreign_key_list({quoted})"):
                source_column = str(row[3] or "").strip()
                target_column = str(row[4] or "").strip()
                if not source_column or not target_column:
                    continue
                foreign_keys.append(
                    RawForeignKey(
                        source_table=table_name,
                        source_column=source_column,
                        target_table=str(row[2]),
                        target_column=target_column,
                    )
                )
    finally:
        connection.close()
    if not tables:
        raise ValueError(f"SQLite database has no physical tables: {database}")
    return RawPhysicalSchema(tuple(tables), tuple(foreign_keys))


def raw_history_from_table_inputs(
    rows: Iterable[dict[str, Any]], *, schema_context: str
) -> list[RawHistoryExample]:
    """Deduplicate complete raw NL-SQL pairs without reading semantic fields."""

    output: dict[str, RawHistoryExample] = {}
    for source in rows:
        context = str(source.get("schema_context") or source.get("db_id") or "")
        if context != schema_context:
            continue
        for row in source.get("target_disjoint_workload") or []:
            history_id = str(row.get("history_id") or row.get("evidence_id") or "")
            question = str(row.get("question") or "").strip()
            sql = str(row.get("sql") or row.get("SQL") or "").strip()
            # The headline baseline is raw NL-SQL, not SQL-only program mining.
            if not history_id or not question or not sql:
                continue
            value = RawHistoryExample(history_id, question, sql)
            previous = output.get(history_id)
            if previous is not None and previous != value:
                raise ValueError(f"conflicting historical pair: {history_id}")
            output[history_id] = value
    return sorted(output.values(), key=lambda row: row.history_id)


def raw_history_from_rows(
    rows: Iterable[dict[str, Any]],
    *,
    schema_context: str,
    context_key: str = "db_id",
    question_key: str = "question",
    sql_key: str = "SQL",
    id_key: str = "question_id",
) -> list[RawHistoryExample]:
    output: dict[str, RawHistoryExample] = {}
    for row in rows:
        if str(row.get(context_key) or "") != schema_context:
            continue
        raw_history_id = row.get(id_key)
        history_id = "" if raw_history_id is None else str(raw_history_id)
        question = str(row.get(question_key) or "").strip()
        sql = str(row.get(sql_key) or "").strip()
        if not history_id or not question or not sql:
            continue
        value = RawHistoryExample(history_id, question, sql)
        previous = output.get(history_id)
        if previous is not None and previous != value:
            raise ValueError(f"conflicting historical pair: {history_id}")
        output[history_id] = value
    return sorted(output.values(), key=lambda value: value.history_id)


def _quote_identifier(value: str, dialect: str) -> str:
    if dialect.casefold() == "mysql":
        return "`" + value.replace("`", "``") + "`"
    return '"' + value.replace('"', '""') + '"'


def _table_line(table: RawTable, dialect: str, *, include_types: bool) -> str:
    columns: list[str] = []
    for column in table.columns:
        text = _quote_identifier(column.name, dialect)
        if include_types:
            text += ":" + (column.declared_type or "unknown")
            if column.primary_key:
                text += " PK"
        columns.append(text)
    return f"{_quote_identifier(table.name, dialect)}({', '.join(columns)});"


def pack_raw_schema(
    schema: RawPhysicalSchema,
    *,
    question: str,
    dialect: str,
    max_tokens: int,
) -> tuple[str, dict[str, Any]]:
    full_lines = [
        _table_line(table, dialect, include_types=True) for table in schema.tables
    ]
    full_lines.extend(
        "FK("
        + f"{_quote_identifier(edge.source_table, dialect)}."
        + f"{_quote_identifier(edge.source_column, dialect)} -> "
        + f"{_quote_identifier(edge.target_table, dialect)}."
        + f"{_quote_identifier(edge.target_column, dialect)})"
        for edge in schema.foreign_keys
    )
    full = "\n".join(full_lines)
    mode = "complete_raw_schema"
    selected_tables = [table.name for table in schema.tables]
    omitted_tables: list[str] = []
    if _estimated_tokens(full) <= max_tokens:
        packed = full
    else:
        identifiers_only = "\n".join(
            _table_line(table, dialect, include_types=False)
            for table in schema.tables
        )
        mode = "all_identifiers_without_types_or_keys"
        if _estimated_tokens(identifiers_only) <= max_tokens:
            packed = identifiers_only
        else:
            mode = "raw_identifier_lexical_selection"
            inventory = "Tables: " + ", ".join(
                _quote_identifier(table.name, dialect) for table in schema.tables
            )
            documents = [
                {
                    "name": table.name,
                    "text": " ".join(
                        [table.name, *(column.name for column in table.columns)]
                    ),
                    "table": table.name,
                }
                for table in schema.tables
            ]
            ranked = BM25Index(documents).search(question, top_k=len(documents))
            ranked_names = [str(row["document"]["table"]) for row in ranked]
            ranked_names.extend(
                table.name
                for table in schema.tables
                if table.name not in ranked_names
            )
            by_name = {table.name: table for table in schema.tables}
            lines = [inventory]
            selected_tables = []
            for name in ranked_names:
                line = _table_line(by_name[name], dialect, include_types=True)
                candidate = "\n".join([*lines, line])
                if _estimated_tokens(candidate) > max_tokens:
                    continue
                lines.append(line)
                selected_tables.append(name)
            packed = "\n".join(lines)
            omitted_tables = [
                table.name for table in schema.tables if table.name not in selected_tables
            ]
    return packed, {
        "mode": mode,
        "truncated": mode != "complete_raw_schema",
        "table_count": len(schema.tables),
        "column_count": sum(len(table.columns) for table in schema.tables),
        "declared_foreign_key_count": len(schema.foreign_keys),
        "selected_tables": selected_tables,
        "omitted_tables": omitted_tables,
        "estimated_tokens": _estimated_tokens(packed),
        "budget_tokens": max_tokens,
        "selection_features": (
            "raw_identifier_BM25_only"
            if mode == "raw_identifier_lexical_selection"
            else "none"
        ),
    }


def _history_block(row: RawHistoryExample) -> str:
    return (
        f"Historical Example [{row.history_id}]\n"
        f"Historical Question:\n{row.question}\n"
        f"Historical SQL:\n{row.sql}"
    )


def pack_raw_history(
    history: Iterable[RawHistoryExample],
    *,
    question: str,
    target_example_id: str,
    max_examples: int,
    max_tokens: int,
) -> tuple[str, dict[str, Any]]:
    target_question = _clean(question).casefold()
    eligible: dict[str, RawHistoryExample] = {}
    excluded_target_ids = excluded_target_questions = incomplete = 0
    for row in history:
        if not row.history_id or not row.question.strip() or not row.sql.strip():
            incomplete += 1
            continue
        if row.history_id == target_example_id:
            excluded_target_ids += 1
            continue
        if _clean(row.question).casefold() == target_question:
            excluded_target_questions += 1
            continue
        previous = eligible.get(row.history_id)
        if previous is not None and previous != row:
            raise ValueError(f"conflicting historical pair: {row.history_id}")
        eligible[row.history_id] = row
    stable = sorted(eligible.values(), key=lambda row: row.history_id)
    all_text = "\n\n".join(_history_block(row) for row in stable)
    if len(stable) <= max_examples and _estimated_tokens(all_text) <= max_tokens:
        ranked = stable
        selection = "all_stable_id"
    else:
        documents = [
            {"name": row.history_id, "text": row.question, "history_id": row.history_id}
            for row in stable
        ]
        matches = BM25Index(documents).search(question, top_k=len(documents))
        ranked_ids = [str(match["document"]["history_id"]) for match in matches]
        ranked_ids.extend(row.history_id for row in stable if row.history_id not in ranked_ids)
        by_id = {row.history_id: row for row in stable}
        ranked = [by_id[history_id] for history_id in ranked_ids]
        selection = "raw_question_BM25"
    selected: list[RawHistoryExample] = []
    blocks: list[str] = []
    oversized_examples = 0
    for row in ranked:
        if len(selected) >= max_examples:
            break
        block = _history_block(row)
        candidate = "\n\n".join([*blocks, block])
        if _estimated_tokens(candidate) > max_tokens:
            oversized_examples += 1
            continue
        selected.append(row)
        blocks.append(block)
    packed = "\n\n".join(blocks) if blocks else "(none available)"
    return packed, {
        "selection": selection,
        "corpus_examples": len(stable),
        "selected_examples": len(selected),
        "selected_history_ids": [row.history_id for row in selected],
        "estimated_tokens": _estimated_tokens(packed),
        "budget_tokens": max_tokens,
        "max_examples": max_examples,
        "excluded_target_ids": excluded_target_ids,
        "excluded_target_questions": excluded_target_questions,
        "excluded_incomplete_pairs": incomplete,
        "unpacked_over_budget": oversized_examples,
        "ranking_fields": ["raw_historical_question"],
    }


def _read_only_sql(sql: str, dialect: str) -> str:
    statements = sqlglot.parse(sql, read=dialect.casefold())
    if len(statements) != 1:
        raise ValueError("exactly one SQL statement is required")
    tree = statements[0]
    forbidden = tuple(
        value
        for name in (
            "Alter",
            "Command",
            "Copy",
            "Create",
            "Delete",
            "Drop",
            "Insert",
            "Merge",
            "Transaction",
            "TruncateTable",
            "Update",
            "Use",
        )
        if (value := getattr(exp, name, None)) is not None
    )
    if forbidden and any(tree.find_all(*forbidden)):
        raise ValueError("only read-only SELECT/WITH SQL is allowed")
    if not isinstance(tree, (exp.Select, exp.Union, exp.Intersect, exp.Except)) and not any(
        tree.find_all(exp.Select)
    ):
        raise ValueError("SQL must contain a SELECT query")
    return sql.strip().rstrip(";").strip()


def extract_sql(content: str, *, dialect: str) -> str:
    text = str(content or "").strip()
    if not text:
        raise ValueError("model returned empty SQL")
    fenced = [
        match.group(1).strip()
        for match in re.finditer(
            r"```(?:sql)?\s*(.*?)```", text, flags=re.IGNORECASE | re.DOTALL
        )
        if match.group(1).strip()
    ]
    sql_starter = re.compile(
        r"\b(?:SELECT|WITH|INSERT|UPDATE|DELETE|DROP|CREATE|ALTER|MERGE|TRUNCATE)\b",
        re.IGNORECASE,
    )
    # Never make a multi-statement response appear safe by silently keeping its
    # first statement.  Explanatory prose after a semicolon is still allowed.
    if any(sql_starter.search(suffix) for suffix in text.split(";")[1:]):
        raise ValueError("multiple SQL statements are not allowed")
    if sum(bool(sql_starter.search(block)) for block in fenced) > 1:
        raise ValueError("multiple SQL code blocks are not allowed")

    candidates: list[str] = list(fenced)
    candidates.append(text)
    starts = [match.start() for match in re.finditer(r"\b(?:SELECT|WITH)\b", text, re.I)]
    candidates.extend(text[start:].strip() for start in starts)
    observed: set[str] = set()
    errors: list[str] = []
    for source in candidates:
        source = source.strip().strip("`").strip()
        variants = [source]
        if ";" in source:
            variants.insert(0, source.split(";", 1)[0])
        lines = source.splitlines()
        variants.extend("\n".join(lines[:end]) for end in range(len(lines) - 1, 0, -1))
        for candidate in variants:
            candidate = candidate.strip()
            if not candidate or candidate in observed:
                continue
            observed.add(candidate)
            try:
                return _read_only_sql(candidate, dialect)
            except Exception as error:  # retain only short parser diagnostics
                errors.append(str(error)[:240])
    raise ValueError("SQL parse error: " + (errors[-1] if errors else "no SELECT found"))


def _sanitize_check(value: dict[str, Any]) -> dict[str, Any]:
    ok = bool(value.get("ok") or value.get("executable"))
    error_type = str(value.get("error_type") or "")[:120]
    error = str(value.get("error") or "")[:800]
    return {"ok": ok, "error_type": error_type, "error": error}


def _prompt(
    *, question: str, schema_text: str, history_text: str, dialect: str
) -> str:
    return (
        f"SQL dialect: {dialect}\n\n"
        f"User question:\n{question}\n\n"
        f"Raw current physical schema:\n{schema_text}\n\n"
        f"Raw historical question-SQL examples:\n{history_text}\n"
    )


def run_direct_raw_evidence_sql(
    *,
    row: dict[str, Any],
    client: TextGenerationClient,
    schema: RawPhysicalSchema,
    history: Iterable[RawHistoryExample],
    error_only_check: Callable[[str], dict[str, Any]],
    dialect: str = "SQLite",
    config: DirectRawEvidenceConfig | None = None,
    source_sha256: str | None = None,
    config_sha256: str | None = None,
) -> dict[str, Any]:
    """Generate SQL directly and optionally perform one error-only repair."""

    active = config or DirectRawEvidenceConfig()
    question = str(row.get("source_question") or row.get("question") or "").strip()
    if not question:
        raise ValueError("online row lacks a question")
    example_id = str(row.get("example_id") or "")
    if not example_id:
        raise ValueError("online row lacks example_id")
    history_target_id = str(row.get("history_target_id") or example_id)
    schema_text, schema_audit = pack_raw_schema(
        schema,
        question=question,
        dialect=dialect,
        max_tokens=active.schema_max_tokens,
    )
    history_text, history_audit = pack_raw_history(
        history,
        question=question,
        target_example_id=history_target_id,
        max_examples=active.history_max_examples,
        max_tokens=active.history_max_tokens,
    )
    system = SYSTEM_PROMPT.format(dialect=dialect)
    user = _prompt(
        question=question,
        schema_text=schema_text,
        history_text=history_text,
        dialect=dialect,
    )
    generations: list[dict[str, Any]] = []
    content, usage = client.chat_text_with_metadata(system, user)
    generations.append({"kind": "initial", "usage": usage})
    sql = ""
    check = {"ok": False, "error_type": "SQLParseError", "error": ""}
    try:
        sql = extract_sql(content, dialect=dialect)
        check = _sanitize_check(error_only_check(sql))
    except Exception as error:
        check = {
            "ok": False,
            "error_type": type(error).__name__,
            "error": str(error)[:800],
        }

    repair_used = False
    repair_prompt_sha256: str | None = None
    initial_sql = sql
    if not check["ok"]:
        repair_used = True
        error_text = f"{check['error_type']}: {check['error']}".strip(": ")
        repair_system = REPAIR_PROMPT.format(error=error_text, dialect=dialect)
        repair_user = (
            user
            + "\nFailed SQL:\n"
            + (sql or str(content).strip())[:8000]
            + "\n\nError-only feedback:\n"
            + error_text
        )
        repair_prompt_sha256 = _sha(
            {"system": repair_system, "user": repair_user}
        )
        repaired_content, repair_usage = client.chat_text_with_metadata(
            repair_system, repair_user
        )
        generations.append({"kind": "error_only_repair", "usage": repair_usage})
        try:
            sql = extract_sql(repaired_content, dialect=dialect)
            check = _sanitize_check(error_only_check(sql))
        except Exception as error:
            sql = ""
            check = {
                "ok": False,
                "error_type": type(error).__name__,
                "error": str(error)[:800],
            }

    if len(generations) > active.max_generation_calls:
        raise AssertionError("direct baseline exceeded its generation-call budget")
    module_sha = sha256(Path(__file__).read_bytes()).hexdigest()
    config_payload = asdict(active)
    raw_schema_payload = {
        "tables": [
            {
                "name": table.name,
                "columns": [asdict(column) for column in table.columns],
            }
            for table in schema.tables
        ],
        "foreign_keys": [asdict(edge) for edge in schema.foreign_keys],
    }
    known_tokens = [
        int(value)
        for generation in generations
        for value in [dict(generation.get("usage") or {}).get("total_tokens")]
        if isinstance(value, int)
    ]
    return {
        "example_id": example_id,
        "dataset_id": row.get("dataset_id"),
        "upstream_split": row.get("upstream_split"),
        "database_id": row.get("database_id"),
        "method_id": METHOD_ID,
        "consumer_id": CONSUMER_ID,
        "model": client.model,
        "decision": "answer",
        "sql": sql,
        "status": "ok" if check["ok"] else "invalid_sql",
        "source_sha256": source_sha256 or module_sha,
        "module_sha256": module_sha,
        "config_sha256": config_sha256 or _sha(config_payload),
        "prompt_sha256": _sha({"system": system, "user": user}),
        "repair_prompt_sha256": repair_prompt_sha256,
        "raw_schema_sha256": _sha(raw_schema_payload),
        "raw_history_pack_sha256": _sha(history_text),
        "graph_evo_context_sha256": None,
        "tools_exposed": [],
        "generation_calls": len(generations),
        "repair_used": repair_used,
        "initial_sql": initial_sql,
        "final_sql": sql,
        "error_only_check": check,
        "input_boundary": {
            "question": True,
            "raw_physical_schema": True,
            "raw_historical_nl_sql": True,
            "values": False,
            "recovered_semantics": False,
            "inferred_relations": False,
            "graph": False,
            "lineage": False,
            "schema_or_value_tools": False,
        },
        "schema_pack": schema_audit,
        "history_pack": history_audit,
        "audit": {
            "usage": generations,
            "known_total_tokens": sum(known_tokens),
            "model_calls": len(generations),
            "max_generation_calls": active.max_generation_calls,
            "max_repairs": active.max_repairs,
            "tools": [],
            "token_estimator": "ceil(utf8_bytes/4); exact prompt preserved by hash",
            "error_feedback_contains_result_rows": False,
        },
    }
