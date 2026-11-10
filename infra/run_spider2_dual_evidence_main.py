#!/usr/bin/env python3
"""Run the performance-first SchemaRecovery main on Spider 2.0 SQLite.

Every example follows one fixed three-stage compiler trajectory: ground the
current physical schema, compile a role-complete connected relational program,
then realize that program as SQLite. Two target-isolated query-time proposals
are fallible program evidence; neither is a fixed backbone or an answer key.
The runner never reads gold SQL, evaluator results, or per-example routing
rules.
"""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
from pathlib import Path
import re
import sqlite3
import threading
import time
from typing import Any

import sqlglot
from sqlglot import exp

from finsemguard.agent.llm import VLLMClient
from finsemguard.e2e.direct_raw_evidence_sql import extract_sql
from finsemguard.e2e.livesqlbench_runner import _write_atomic


METHOD_ID = "schema_recovery_bounded_set_refine_spider2_v9"

GROUNDING_SYSTEM = """You are the physical grounding stage of SchemaRecovery.
Inspect the question, complete current SQLite schema, declared keys, bounded
current values, released documentation, and two fallible proposal programs.
Recover only physical facts needed by the question; do not write SQL.

Check table/column roles, composite join identities, exact stored values and
date formats, identifier direction in containment or symmetric relations, and
whether each proposal clause is supported by current physical evidence. A
successful execution preview proves only physical executability, not semantic
correctness; an interrupted preview is a concrete efficiency risk. When the
question explicitly defines a metric from base facts, bind those base facts and
all of their identity keys. Do not prefer a convenience or derived relation
merely because its name resembles the requested metric. Prefer declared/current
evidence over plausible names. Do not invent descriptions or expose any
evaluator information.

Return one compact JSON object with exactly these keys: relevant_tables,
role_bindings, join_contracts, value_bindings, source_contracts,
proposal_support, physical_ambiguities. `relevant_tables` must be a JSON list
of current table names. Keep the object below 650 words."""

PROGRAM_SYSTEM = """You are the role-first connected relational-program
compiler of SchemaRecovery. Use the physical grounding plus the question to
compile the program before SQL is written. The supplied proposal programs are
fallible evidence, not answers.

First lock the requested output representation and final row grain. Then list
filters, entity grain, metric numerator/denominator, time scope, and ranking
cardinality. Finally build an ordered sequence of relational stages whose joins
are supported by the physical grounding. Preserve supported proposal clauses;
replace a clause only when the question, grounding, released documentation, or
current value evidence supplies a concrete contradiction.

Avoid fan-out: independent one-to-many additive facts or symmetric roles must
be normalized to a common grain before combination. Join composite facts on all
shared identity dimensions. In a directed containment relation (parent, child,
multiplicity), roots never occur as children, leaves never occur as parents,
path multiplicities multiply, and aggregation occurs at the requested root or
entity grain. For cumulative state, aggregate events through each measurement
time per entity before applying an entity-level floor and final sum. Aggregate
at the requested month/year/category/entity grain before changes, extrema, or
windows. Partition a window only when the ranking/change is explicitly within
each entity/group. If a question asks for a global top N and merely requests a
year/category as output, do not partition by that output field. Ordering does
not imply LIMIT; only explicit top/bottom or singular wording does. Equal-width
N-bucket plans must put the global maximum in the last bucket and never create
an N+1 endpoint bucket.

Compile a set-based efficiency contract together with semantics: scan each
large base relation once where possible; generate repeated periods/offsets as a
small relation and join once; use conditional aggregation instead of repeated
correlated EXISTS or scalar subqueries; compute reusable aggregates once in a
linear CTE chain. Reject a physically equivalent plan whose proposal preview
was interrupted when a bounded, set-based relation plan is available.
When a metric needs both a fine-grain threshold and a coarser total, aggregate
the raw fact once at the fine grain and roll that result up; never rescan the
raw fact. Pre-deduplicate exclusion keys and use one anti-join instead of a
correlated NOT EXISTS per fact row. Do not join every day in a dense calendar
merely to test whether an interval contains a yearly/monthly boundary; generate
only the requested boundaries and range-join them once.

After the stages are fixed, realize them once as a draft SQLite query. Return
one compact JSON object with exactly these keys: outputs, hidden_metrics,
filters, base_grain, stages, final_grain, metric_contract, time_contract,
ranking_and_cardinality, efficiency_contract, proposal_decisions,
unresolved_risks, draft_sql. Each item in `stages` must state input relations,
join keys, operation, group grain, and produced fields. `draft_sql` must contain
one read-only SQLite query without a Markdown fence. Keep the object below 1150
words."""

REALIZER_SYSTEM = """You are the bounded AST-safe final refinement stage of
SchemaRecovery. Return exactly one executable, read-only SQLite query and no
explanation.

Follow the explicit draft execution status. If it says COMPLETED, return the
draft SQL exactly without reformatting, elaborating, or reinterpreting it. If it
says FAILED, keep the draft's semantic contract and produce its simplest
set-based equivalent: aggregate a raw fact once and roll up; replace repeated
correlated EXISTS/NOT EXISTS with one deduplicated join or anti-join; generate
only requested time boundaries rather than expanding a dense date range; reuse
each aggregate from one linear CTE. Preserve composite identity keys, output
shape, final grain, filters, metric denominator, global/group ranking scope,
and exact physical values. A timeout is not permission to change semantics.
Use only the supplied question, physical grounding, relational program, draft,
and execution feedback. Return only SQL."""


def _load_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if line.strip():
                rows.append(json.loads(line))
    return rows


def _by_id(path: Path) -> dict[str, dict[str, Any]]:
    output: dict[str, dict[str, Any]] = {}
    for row in _load_jsonl(path):
        example_id = str(row.get("example_id") or row.get("instance_id") or "")
        if not example_id:
            raise ValueError(f"prediction without example_id: {path}")
        if example_id in output:
            raise ValueError(f"duplicate prediction {example_id}: {path}")
        output[example_id] = row
    return output


def _metadata(root: Path) -> dict[str, dict[str, Any]]:
    return {
        str(row["instance_id"]): row
        for row in _load_jsonl(root / "spider2-lite.jsonl")
    }


def _local_map(root: Path) -> dict[str, str]:
    path = root / "resource" / "databases" / "spider2-localdb" / "local-map.jsonl"
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise ValueError("Spider local-map must be an object")
    return {str(key): str(item) for key, item in value.items()}


def _database_path(root: Path, database_id: str) -> Path:
    base = root / "resource" / "databases" / "spider2-localdb"
    direct = base / f"{database_id}.sqlite"
    if direct.is_file():
        return direct
    matches = sorted((root / "resource" / "databases").rglob(f"{database_id}.sqlite"))
    if len(matches) != 1:
        raise FileNotFoundError(f"cannot uniquely resolve SQLite database: {database_id}")
    return matches[0]


def _quote(value: str) -> str:
    return '"' + value.replace('"', '""') + '"'


def _safe_value(value: Any) -> str:
    if isinstance(value, bytes):
        return f"<blob:{len(value)}>"
    return re.sub(r"\s+", " ", repr(value))[:80]


def _proposal_program(sql: str) -> dict[str, Any]:
    if not sql.strip():
        return {"valid": False, "sql": "", "tables": [], "columns": [], "joins": []}
    try:
        clean = extract_sql(sql, dialect="SQLite")
        tree = sqlglot.parse_one(clean, read="sqlite")
    except Exception as error:
        return {
            "valid": False,
            "sql": sql.strip()[:12_000],
            "tables": [],
            "columns": [],
            "joins": [],
            "parse_error": f"{type(error).__name__}: {error}"[:300],
        }
    tables = sorted({node.name for node in tree.find_all(exp.Table) if node.name})
    columns = sorted(
        {
            f"{node.table}.{node.name}" if node.table else node.name
            for node in tree.find_all(exp.Column)
            if node.name
        }
    )
    string_literals = sorted(
        {
            str(node.this)
            for node in tree.find_all(exp.Literal)
            if bool(node.is_string) and str(node.this).strip()
        },
        key=str.casefold,
    )
    joins = []
    for node in tree.find_all(exp.Join):
        relation = node.this.sql(dialect="sqlite") if node.this is not None else ""
        predicate = node.args.get("on")
        joins.append(
            relation
            + (f" ON {predicate.sql(dialect='sqlite')}" if predicate is not None else "")
        )
    return {
        "valid": True,
        "sql": clean[:12_000],
        "tables": tables,
        "columns": columns[:160],
        "string_literals": string_literals[:40],
        "joins": joins[:40],
        "ctes": sum(1 for _ in tree.find_all(exp.CTE)),
        "windows": sum(1 for _ in tree.find_all(exp.Window)),
        "groups": sum(1 for _ in tree.find_all(exp.Group)),
    }


def _role_contract(question: str) -> str:
    text = question.casefold()
    roles = []
    if any(token in text for token in ("count", "number of", "how many")):
        roles.append("count/cardinality")
    if any(token in text for token in ("average", "mean", "avg")):
        roles.append("average")
    if any(token in text for token in ("sum", "total")):
        roles.append("sum/total")
    if any(token in text for token in ("percent", "ratio", "rate", "share")):
        roles.append("ratio/percentage")
    if any(token in text for token in ("each ", " per ", " by ", "group")):
        roles.append("grouping grain")
    if any(token in text for token in ("date", "day", "week", "month", "year", "time")):
        roles.append("time")
    if any(token in text for token in ("top ", "highest", "lowest", "most ", "least ", "first ", "last ")):
        roles.append("ordering/ranking; limit only when cardinality is explicit")
    explicit_limit = re.search(r"\b(top|bottom)\s*(\d+)\b", text)
    if explicit_limit is not None:
        roles.append(
            f"explicit cardinality: {explicit_limit.group(1)} "
            f"{explicit_limit.group(2)}"
        )
    elif re.search(r"\b(?:list|show\s+all|for\s+each|report)\b", text):
        roles.append("cardinality: all qualifying rows; ordering alone is not a limit")
    per_group = re.search(
        r"\b(?:for each|per)\s+(year|month|week|day|region|country|category|group|team|customer|product)\b",
        text,
    )
    if per_group is not None:
        roles.append(f"explicit per-group scope: {per_group.group(1)}")
    if "exact number of hours-minutes-seconds" in text or "not calendar days" in text:
        roles.append(
            "elapsed-time unit: exact duration; julianday subtraction is already in days"
        )
    if " exceed" in text:
        roles.append("comparison direction: preserve the grammatical subject as left side")
    return ", ".join(roles) if roles else "projection/filter/join roles from question"


_PROFILE_CACHE: dict[tuple[str, str, str], list[str]] = {}
_PROFILE_CACHE_LOCK = threading.Lock()


def _literal_candidates(
    question: str,
    *proposals: dict[str, Any],
    limit: int = 24,
) -> list[str]:
    values: list[str] = []
    for proposal in proposals:
        values.extend(str(item) for item in proposal.get("string_literals") or [])
    values.extend(
        match.strip()
        for match in re.findall(r"[\"'“”]([^\"'“”]{2,80})[\"'“”]", question)
    )
    values.extend(
        match.strip()
        for match in re.findall(
            r"\b[A-Z][A-Za-z0-9]*(?:\s+[A-Z][A-Za-z0-9]*){1,3}\b",
            question,
        )
    )
    output = []
    seen = set()
    for value in values:
        clean = re.sub(r"\s+", " ", value).strip()
        folded = clean.casefold()
        if (
            folded in seen
            or len(clean) < 3
            or len(clean) > 80
            or re.search(r"[A-Za-z]", clean) is None
        ):
            continue
        seen.add(folded)
        output.append(clean)
        if len(output) >= limit:
            break
    return output


def _profile_column(name: str, declared_type: str) -> bool:
    folded_name = name.casefold()
    folded_type = declared_type.casefold()
    return any(
        token in folded_type for token in ("char", "text", "clob", "date", "time")
    ) or any(
        token in folded_name
        for token in (
            "name",
            "type",
            "status",
            "date",
            "time",
            "country",
            "city",
            "state",
            "region",
            "category",
            "rating",
            "model",
            "gender",
            "cancel",
            "txn_",
        )
    )


def _bounded_fetchall(
    connection: sqlite3.Connection,
    query: str,
    parameters: list[str] | tuple[Any, ...] = (),
    *,
    timeout_seconds: float = 1.0,
) -> list[tuple[Any, ...]]:
    deadline = time.monotonic() + timeout_seconds
    connection.set_progress_handler(
        lambda: int(time.monotonic() >= deadline),
        10_000,
    )
    try:
        return list(connection.execute(query, parameters).fetchall())
    finally:
        connection.set_progress_handler(None, 0)


def _top_physical_values(
    connection: sqlite3.Connection,
    database: Path,
    table: str,
    column: str,
) -> list[str]:
    key = (str(database.resolve()), table.casefold(), column.casefold())
    with _PROFILE_CACHE_LOCK:
        cached = _PROFILE_CACHE.get(key)
    if cached is not None:
        return cached
    quoted_table = _quote(table)
    quoted_column = _quote(column)
    try:
        rows = _bounded_fetchall(
            connection,
            f"SELECT {quoted_column}, COUNT(*) AS frequency "
            f"FROM {quoted_table} WHERE {quoted_column} IS NOT NULL "
            f"GROUP BY {quoted_column} "
            f"ORDER BY frequency DESC, CAST({quoted_column} AS TEXT) LIMIT 6",
        )
        values = [_safe_value(row[0]) for row in rows]
    except sqlite3.Error:
        values = []
    with _PROFILE_CACHE_LOCK:
        _PROFILE_CACHE[key] = values
    return values


def _matching_physical_values(
    connection: sqlite3.Connection,
    table: str,
    column: str,
    candidates: list[str],
) -> list[str]:
    if not candidates:
        return []
    quoted_table = _quote(table)
    quoted_column = _quote(column)
    text_expression = f"LOWER(CAST({quoted_column} AS TEXT))"
    normalized_expression = text_expression
    for character in (" ", "-", "_", "/", "."):
        normalized_expression = f"REPLACE({normalized_expression}, '{character}', '')"
    clauses = []
    parameters: list[str] = []
    for candidate in candidates[:12]:
        folded = candidate.casefold()
        normalized = re.sub(r"[\s\-_/\.]", "", folded)
        clauses.append(
            f"({text_expression} LIKE ? OR {normalized_expression} = ?)"
        )
        parameters.extend((f"%{folded}%", normalized))
    try:
        rows = _bounded_fetchall(
            connection,
            f"SELECT {quoted_column}, COUNT(*) AS frequency FROM {quoted_table} "
            f"WHERE {quoted_column} IS NOT NULL AND ({' OR '.join(clauses)}) "
            f"GROUP BY {quoted_column} ORDER BY frequency DESC LIMIT 8",
            parameters,
        )
        return [_safe_value(row[0]) for row in rows]
    except sqlite3.Error:
        return []


def _schema_context(
    database: Path,
    focus_tables: set[str],
    literal_candidates: list[str],
    max_chars: int,
) -> str:
    connection = sqlite3.connect(f"file:{database.resolve()}?mode=ro", uri=True)
    try:
        names = [
            str(row[0])
            for row in connection.execute(
                "SELECT name FROM sqlite_master WHERE type IN ('table','view') "
                "AND name NOT LIKE 'sqlite_%' ORDER BY name COLLATE NOCASE"
            )
        ]
        focus_folded = {name.casefold() for name in focus_tables}
        names.sort(key=lambda name: (name.casefold() not in focus_folded, name.casefold()))
        blocks = ["[Current physical SQLite schema; focus tables are listed first]"]
        for table in names:
            quoted = _quote(table)
            try:
                columns = list(connection.execute(f"PRAGMA table_info({quoted})"))
            except sqlite3.Error:
                continue
            if not columns:
                continue
            column_text = ", ".join(
                f"{_quote(str(row[1]))} {str(row[2] or 'UNKNOWN')}"
                + (" PK" if row[5] else "")
                for row in columns
            )
            foreign_keys = list(connection.execute(f"PRAGMA foreign_key_list({quoted})"))
            fk_text = "; ".join(
                f"{_quote(str(row[3]))} -> {_quote(str(row[2]))}.{_quote(str(row[4]))}"
                for row in foreign_keys
                if row[3] and row[4]
            )
            lines = [f"TABLE {_quote(table)} ({column_text})"]
            if fk_text:
                lines.append(f"  DECLARED FK: {fk_text}")
            if table.casefold() in focus_folded:
                try:
                    sample = connection.execute(f"SELECT * FROM {quoted} LIMIT 1").fetchone()
                except sqlite3.Error:
                    sample = None
                if sample is not None:
                    pairs = [
                        f"{_quote(str(columns[index][1]))}={_safe_value(value)}"
                        for index, value in enumerate(sample[: min(12, len(columns))])
                    ]
                    lines.append("  BOUNDED CURRENT VALUE ROW: " + ", ".join(pairs))
                profiled = 0
                profiles = []
                matches = []
                for column in columns:
                    column_name = str(column[1])
                    declared_type = str(column[2] or "")
                    if not _profile_column(column_name, declared_type):
                        continue
                    top_values = _top_physical_values(
                        connection,
                        database,
                        table,
                        column_name,
                    )
                    if top_values:
                        profiles.append(
                            f"{_quote(column_name)}=[{', '.join(top_values)}]"
                        )
                    matched_values = _matching_physical_values(
                        connection,
                        table,
                        column_name,
                        literal_candidates,
                    )
                    if matched_values:
                        matches.append(
                            f"{_quote(column_name)}=[{', '.join(matched_values)}]"
                        )
                    profiled += 1
                    if profiled >= 12:
                        break
                if profiles:
                    lines.append("  CURRENT VALUE PROFILE: " + "; ".join(profiles))
                if matches:
                    lines.append(
                        "  QUESTION/PROPOSAL LITERAL MATCHES: " + "; ".join(matches)
                    )
            candidate = "\n".join([*blocks, *lines])
            if len(candidate) > max_chars:
                blocks.append("[remaining non-focus tables omitted by fixed context budget]")
                break
            blocks.extend(lines)
        return "\n".join(blocks)
    finally:
        connection.close()


def _allowed_docs(root: Path, row: dict[str, Any], meta: dict[str, Any]) -> str:
    raw_paths: list[str] = []
    for value in (row.get("allowed_docs"), meta.get("external_knowledge")):
        if isinstance(value, str) and value:
            raw_paths.append(value)
        elif isinstance(value, list):
            raw_paths.extend(str(item) for item in value if item)
    document_root = (root / "resource" / "documents").resolve()
    blocks = []
    remaining = 24_000
    for relative in dict.fromkeys(raw_paths):
        path = (document_root / relative).resolve()
        if document_root not in path.parents or not path.is_file() or remaining <= 0:
            continue
        content = path.read_text(encoding="utf-8", errors="replace")[:remaining]
        blocks.append(f"--- {relative} ---\n{content}")
        remaining -= len(content)
    return "\n\n".join(blocks) if blocks else "(none released for this question)"


def _compile_check(database: Path, sql: str) -> dict[str, Any]:
    try:
        clean = extract_sql(sql, dialect="SQLite")
        connection = sqlite3.connect(f"file:{database.resolve()}?mode=ro", uri=True)
        try:
            connection.execute("EXPLAIN QUERY PLAN " + clean).fetchall()
        finally:
            connection.close()
        return {"ok": True, "sql": clean, "error": ""}
    except Exception as error:
        return {
            "ok": False,
            "sql": "",
            "error": f"{type(error).__name__}: {error}"[:800],
        }


def _execution_preview(
    database: Path,
    sql: str,
    *,
    max_rows: int = 3,
    timeout_seconds: float = 5.0,
) -> dict[str, Any]:
    """Execute a bounded read-only preview without using scorer information."""

    compiled = _compile_check(database, sql)
    if not compiled["ok"]:
        return {
            "ok": False,
            "compile_ok": False,
            "columns": [],
            "sample_rows": [],
            "error": compiled["error"],
        }
    connection = sqlite3.connect(f"file:{database.resolve()}?mode=ro", uri=True)
    deadline = time.monotonic() + timeout_seconds
    connection.set_progress_handler(
        lambda: int(time.monotonic() >= deadline),
        10_000,
    )
    try:
        cursor = connection.execute(str(compiled["sql"]))
        columns = [str(item[0]) for item in (cursor.description or [])]
        rows = cursor.fetchmany(max_rows)
        return {
            "ok": True,
            "compile_ok": True,
            "columns": columns[:80],
            "sample_rows": [
                [_safe_value(value) for value in row[:80]] for row in rows
            ],
            "rows_returned_in_preview": len(rows),
            "error": "",
        }
    except Exception as error:
        return {
            "ok": False,
            "compile_ok": True,
            "columns": [],
            "sample_rows": [],
            "error": f"{type(error).__name__}: {error}"[:800],
        }
    finally:
        connection.set_progress_handler(None, 0)
        connection.close()


def _proposal_block(label: str, proposal: dict[str, Any]) -> str:
    return f"""[{label}; fallible target-isolated hypothesis]
valid={proposal['valid']}
current_schema_compile_ok={proposal.get('compile_ok', False)}
compile_error={proposal.get('compile_error') or '(none)'}
tables={proposal['tables']}
columns={proposal['columns']}
joins={proposal['joins']}
string_literals={proposal.get('string_literals', [])}
program_shape=CTEs:{proposal.get('ctes', 0)}, windows:{proposal.get('windows', 0)}, groups:{proposal.get('groups', 0)}
bounded_execution_preview={json.dumps(proposal.get('execution_preview') or {}, ensure_ascii=False, sort_keys=True)}
SQL:
{proposal['sql'] or '(unavailable)'}"""


def _evidence_prompt(
    *,
    row: dict[str, Any],
    database_id: str,
    direct: dict[str, Any],
    recovery: dict[str, Any],
    schema: str,
    docs: str,
) -> str:
    return f"""Database: {database_id}
Question: {row['question']}

Query-role contract: {_role_contract(str(row['question']))}

{_proposal_block('Direct Raw proposal', direct)}

{_proposal_block('Recovered-evidence proposal', recovery)}

[Released documentation / business rules]
{docs}

{schema}"""


def _grounding_prompt(evidence: str) -> str:
    return f"""{evidence}

Ground the physical roles and relation keys now. Return only the required JSON
object."""


def _program_prompt(evidence: str, grounding: dict[str, Any]) -> str:
    grounding_text = json.dumps(grounding, ensure_ascii=False, sort_keys=True)
    return f"""{evidence}

[Controlling current-schema physical grounding]
{grounding_text}

Compile the ordered role-complete connected relational program now. Return only
the required JSON object."""


def _realization_prompt(
    question: str,
    grounding: dict[str, Any],
    program: dict[str, Any],
    draft_sql: str,
    preview: dict[str, Any],
) -> str:
    grounding_text = json.dumps(grounding, ensure_ascii=False, sort_keys=True)
    program_text = json.dumps(
        {key: value for key, value in program.items() if key != "draft_sql"},
        ensure_ascii=False,
        sort_keys=True,
    )
    preview_text = json.dumps(preview, ensure_ascii=False, sort_keys=True)
    execution_status = (
        "COMPLETED: return the draft exactly"
        if preview.get("ok")
        else "FAILED: produce the simplest set-based equivalent"
    )
    return f"""Question: {question}

[Controlling current-schema physical grounding]
{grounding_text}

[Controlling ordered relational program]
{program_text}

[Draft SQLite]
{draft_sql or '(missing or unparseable)'}

[Bounded read-only draft execution feedback]
{preview_text}

[Mandatory refinement action]
{execution_status}

Perform the bounded AST-safe final refinement. Return only SQL."""


def _grounded_focus_tables(
    database: Path,
    grounding: dict[str, Any],
) -> set[str]:
    raw = grounding.get("relevant_tables")
    if not isinstance(raw, list):
        return set()
    connection = sqlite3.connect(f"file:{database.resolve()}?mode=ro", uri=True)
    try:
        current = {
            str(row[0]).casefold(): str(row[0])
            for row in connection.execute(
                "SELECT name FROM sqlite_master WHERE type IN ('table','view') "
                "AND name NOT LIKE 'sqlite_%'"
            )
        }
    finally:
        connection.close()
    output = set()
    for value in raw:
        name = str(value).strip().strip('`"[]')
        resolved = current.get(name.casefold())
        if resolved is not None:
            output.add(resolved)
    return output


def _run_one(
    row: dict[str, Any],
    *,
    root: Path,
    clients: tuple[VLLMClient, VLLMClient, VLLMClient],
    metadata: dict[str, dict[str, Any]],
    local_map: dict[str, str],
    direct_rows: dict[str, dict[str, Any]],
    recovery_rows: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    grounding_client, program_client, realizer_client = clients
    example_id = str(row["example_id"])
    meta = metadata.get(example_id, {})
    database_id = local_map.get(example_id) or str(meta.get("db") or row["database_id"])
    database = _database_path(root, database_id)
    direct = _proposal_program(str(direct_rows[example_id].get("sql") or ""))
    recovery = _proposal_program(str(recovery_rows[example_id].get("sql") or ""))
    for proposal in (direct, recovery):
        compiled = _compile_check(database, str(proposal.get("sql") or ""))
        proposal["compile_ok"] = bool(compiled["ok"])
        proposal["compile_error"] = compiled["error"] or None
        proposal["execution_preview"] = _execution_preview(
            database,
            str(proposal.get("sql") or ""),
            max_rows=2,
            timeout_seconds=3.0,
        )
    focus_tables = set(direct["tables"]) | set(recovery["tables"])
    literal_candidates = _literal_candidates(
        str(row["question"]),
        direct,
        recovery,
    )
    initial_schema = _schema_context(
        database,
        focus_tables,
        literal_candidates,
        max_chars=96_000,
    )
    docs = _allowed_docs(root, row, meta)
    evidence = _evidence_prompt(
        row=row,
        database_id=database_id,
        direct=direct,
        recovery=recovery,
        schema=initial_schema,
        docs=docs,
    )
    grounding, grounding_usage = grounding_client.chat_json_with_metadata(
        GROUNDING_SYSTEM,
        _grounding_prompt(evidence),
    )
    grounded_tables = _grounded_focus_tables(database, grounding)
    expanded_focus_tables = focus_tables | grounded_tables
    expanded_schema = _schema_context(
        database,
        expanded_focus_tables,
        literal_candidates,
        max_chars=96_000,
    )
    expanded_evidence = _evidence_prompt(
        row=row,
        database_id=database_id,
        direct=direct,
        recovery=recovery,
        schema=expanded_schema,
        docs=docs,
    )
    program, program_usage = program_client.chat_json_with_metadata(
        PROGRAM_SYSTEM,
        _program_prompt(expanded_evidence, grounding),
    )
    draft_content = str(program.get("draft_sql") or "")
    draft = _compile_check(database, draft_content)
    draft_sql = str(draft.get("sql") or draft_content)[:16_000]
    draft_preview = _execution_preview(
        database,
        draft_sql,
        max_rows=3,
        timeout_seconds=5.0,
    )
    realization_content, realization_usage = realizer_client.chat_text_with_metadata(
        REALIZER_SYSTEM,
        _realization_prompt(
            str(row["question"]),
            grounding,
            program,
            draft_sql,
            draft_preview,
        ),
    )
    realized = _compile_check(database, realization_content)

    if realized["ok"]:
        final = realized
        realization_source = "ground_program_draft_refine"
    elif draft["ok"]:
        final = draft
        realization_source = "draft_ast_safe"
    elif direct["compile_ok"]:
        final = _compile_check(database, str(direct["sql"]))
        realization_source = "direct_ast_safe"
    else:
        final = _compile_check(database, str(recovery["sql"]))
        realization_source = "recovery_ast_safe"
    return {
        "example_id": example_id,
        "instance_id": example_id,
        "dataset_id": "spider2_lite",
        "database_id": database_id,
        "question": row["question"],
        "method_id": METHOD_ID,
        "decision": "answer" if final["sql"] else "error",
        "sql": final["sql"],
        "error": final["error"] or None,
        "repair_used": bool(
            realized["ok"]
            and re.sub(r"\s+", " ", draft_sql).strip().rstrip(";").casefold()
            != re.sub(r"\s+", " ", str(realized["sql"])).strip().rstrip(";").casefold()
        ),
        "model_calls": 3,
        "usage": {
            "physical_grounding": grounding_usage,
            "relational_program": program_usage,
            "realization": realization_usage,
        },
        "program": {
            "backbone_policy": "physical_grounding_then_role_complete_program",
            "physical_grounding": grounding,
            "relational_program": program,
            "direct_valid": direct["valid"],
            "recovery_valid": recovery["valid"],
            "direct_compile_ok": direct["compile_ok"],
            "recovery_compile_ok": recovery["compile_ok"],
            "proposal_focus_table_count": len(focus_tables),
            "grounded_focus_table_count": len(grounded_tables),
            "expanded_focus_table_count": len(expanded_focus_tables),
            "literal_candidate_count": len(literal_candidates),
            "released_documentation": docs != "(none released for this question)",
            "draft_compile_ok": draft["ok"],
            "draft_execution_ok": draft_preview["ok"],
            "draft_execution_error": draft_preview["error"] or None,
            "realized_compile_ok": realized["ok"],
            "realization_source": realization_source,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--direct-predictions", type=Path, required=True)
    parser.add_argument("--recovery-predictions", type=Path, required=True)
    parser.add_argument(
        "--spider2-root",
        type=Path,
        default=Path("/data/workspace/yanmy/datasets/Spider2_official/spider2-lite"),
    )
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument(
        "--base-url",
        action="append",
        dest="base_urls",
        help=(
            "OpenAI-compatible endpoint; repeat to distribute complete examples "
            "round-robin across endpoints"
        ),
    )
    parser.add_argument("--model", default="qwen3.8-27b-fp8")
    parser.add_argument(
        "--generation-endpoint",
        help="Human-readable runtime location recorded in RUN_SUMMARY.json",
    )
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument(
        "--thinking",
        choices=("enabled", "disabled"),
        default="disabled",
    )
    parser.add_argument("--limit", type=int)
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()

    rows = _load_jsonl(args.manifest)
    if args.limit is not None:
        rows = rows[: args.limit]
    direct_rows = _by_id(args.direct_predictions)
    recovery_rows = _by_id(args.recovery_predictions)
    ids = {str(row["example_id"]) for row in rows}
    for name, proposals in (("Direct", direct_rows), ("Recovery", recovery_rows)):
        missing = sorted(ids - set(proposals))
        if missing:
            raise ValueError(f"{name} proposals missing {len(missing)} rows: {missing[:5]}")

    base_urls = args.base_urls or ["http://127.0.0.1:18023/v1"]
    def make_client(base_url: str, max_output_tokens: int) -> VLLMClient:
        return VLLMClient(
            {
                "base_url": base_url,
                "api_key": "EMPTY",
                "model": args.model,
                "temperature": 0.0,
                "top_p": 1.0,
                "max_output_tokens": max_output_tokens,
                "request_timeout_seconds": 600.0,
                "compatibility": "vllm",
                "thinking": args.thinking,
            }
        )

    client_sets = [
        (
            make_client(base_url, 3072),
            make_client(base_url, 4096),
            make_client(base_url, 4096),
        )
        for base_url in base_urls
    ]
    unavailable = [
        client_set[0].base_url
        for client_set in client_sets
        if not client_set[0].healthy()
    ]
    if unavailable:
        raise RuntimeError(f"Qwen endpoints are unavailable: {unavailable}")

    metadata = _metadata(args.spider2_root)
    local_map = _local_map(args.spider2_root)
    completed = _by_id(args.output) if args.resume and args.output.is_file() else {}
    pending = [row for row in rows if str(row["example_id"]) not in completed]
    lock = threading.Lock()
    args.output.parent.mkdir(parents=True, exist_ok=True)

    def run(index: int, row: dict[str, Any]) -> dict[str, Any]:
        clients = client_sets[index % len(client_sets)]
        endpoint = clients[0].base_url
        try:
            result = _run_one(
                row,
                root=args.spider2_root,
                clients=clients,
                metadata=metadata,
                local_map=local_map,
                direct_rows=direct_rows,
                recovery_rows=recovery_rows,
            )
            result["generation_endpoint"] = endpoint
            return result
        except Exception as error:
            example_id = str(row["example_id"])
            return {
                "example_id": example_id,
                "instance_id": example_id,
                "dataset_id": "spider2_lite",
                "database_id": row.get("database_id"),
                "question": row.get("question"),
                "method_id": METHOD_ID,
                "decision": "error",
                "sql": "",
                "error": f"{type(error).__name__}: {error}"[:1000],
                "generation_endpoint": endpoint,
            }

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {
            executor.submit(run, index, row): str(row["example_id"])
            for index, row in enumerate(pending)
        }
        for count, future in enumerate(as_completed(futures), start=1):
            result = future.result()
            with lock:
                completed[str(result["example_id"])] = result
                ordered = [
                    completed[str(row["example_id"])]
                    for row in rows
                    if str(row["example_id"]) in completed
                ]
                _write_atomic(args.output, ordered)
            print(
                f"[{count}/{len(pending)}] {result['example_id']} "
                f"decision={result['decision']} "
                f"source={result.get('program', {}).get('realization_source', 'error')}",
                flush=True,
            )

    ordered = [completed[str(row["example_id"])] for row in rows]
    _write_atomic(args.output, ordered)
    summary = {
        "method_id": METHOD_ID,
        "rows": len(ordered),
        "errors": sum(not row.get("sql") for row in ordered),
        "fixed_model_calls_per_example": 3,
        "grounding_max_output_tokens": 3072,
        "program_and_draft_max_output_tokens": 4096,
        "sql_stage_max_output_tokens": 4096,
        "model": args.model,
        "thinking": args.thinking,
        "generation_endpoint": args.generation_endpoint or base_urls,
        "input_boundary": (
            "question + Direct Raw proposal + evidence-informed proposal + "
            "current schema/FK/physical value profiles + bounded proposal "
            "execution previews + released documentation"
        ),
        "output_contract": "one executable read-only SQLite query per example",
        "trajectory": (
            "current-schema physical grounding -> role-first connected relational "
            "program plus draft SQL -> bounded-execution AST-safe refinement"
        ),
        "gold_or_scorer_access": "none",
    }
    args.output.with_name("RUN_SUMMARY.json").write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    main()
