from __future__ import annotations

import argparse
import hashlib
import json
import re
import statistics
from collections import defaultdict
from pathlib import Path
from typing import Any

from finsemguard.retrieval.bm25 import tokenize


TABLE_HEADER = re.compile(r"^###Table full name:\s*(.+?)\s*$", re.IGNORECASE)
SIMILAR_TABLES = re.compile(
    r"\*\*Some other tables have the similar structure:\s*\[(.*?)\]\*\*",
    re.IGNORECASE,
)
COLUMN_LINE = re.compile(r"^\s{4}([^\s].*?)\s+\(Type:", re.MULTILINE)


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def normalize_table(identifier: str) -> str:
    return (
        identifier.strip()
        .strip("`\"")
        .replace("`", "")
        .replace('"', "")
        .casefold()
    )


def parse_autolink_prompt(text: str) -> tuple[set[str], int]:
    """Recover tables (including compressed siblings) from a released prompt."""
    tables: set[str] = set()
    current: str | None = None
    for line in text.splitlines():
        header = TABLE_HEADER.match(line)
        if header:
            current = header.group(1).strip()
            tables.add(normalize_table(current))
            continue
        siblings = SIMILAR_TABLES.search(line)
        if siblings and current:
            prefix = current.rsplit(".", 1)[0]
            for name in siblings.group(1).split(","):
                clean_name = name.strip().strip("`\"'")
                if clean_name:
                    tables.add(normalize_table(f"{prefix}.{clean_name}"))
    return tables, len(COLUMN_LINE.findall(text))


def compact_schema_tokens(text: str) -> int:
    """Count a schema-only serialization with samples and documents removed."""
    compact: list[str] = []
    current: str | None = None
    for line in text.splitlines():
        header = TABLE_HEADER.match(line)
        if header:
            current = normalize_table(header.group(1))
            compact.append(current)
            continue
        siblings = SIMILAR_TABLES.search(line)
        if siblings and current:
            compact.append("similar tables " + siblings.group(1))
            continue
        column = COLUMN_LINE.match(line)
        if not column or current is None:
            continue
        stripped = line.strip()
        name, remainder = stripped.split(" (Type:", 1)
        column_type = remainder.split(";", 1)[0].strip()
        description = ""
        if "Description:" in remainder:
            description = remainder.rsplit("Description:", 1)[1].rstrip(")").strip()
        compact.append(f"{current}.{name} {column_type} {description}".strip())
    return len(tokenize("\n".join(compact)))


def schema_size_by_database(schema_root: Path) -> dict[tuple[str, str], dict[str, int]]:
    output: dict[tuple[str, str], dict[str, int]] = {}
    for dialect_dir in sorted(path for path in schema_root.iterdir() if path.is_dir()):
        dialect = dialect_dir.name
        for database_dir in sorted(path for path in dialect_dir.iterdir() if path.is_dir()):
            tables = columns = full_schema_tokens = 0
            for path in database_dir.rglob("*.json"):
                try:
                    row = json.loads(path.read_text(encoding="utf-8"))
                except (json.JSONDecodeError, UnicodeDecodeError):
                    continue
                if not isinstance(row, dict) or "table_name" not in row:
                    continue
                tables += 1
                names = row.get("nested_column_names") or row.get("column_names") or []
                types = row.get("nested_column_types") or row.get("column_types") or []
                descriptions = row.get("description") or []
                columns += len(names)
                schema_text = [
                    str(row.get("table_fullname") or row.get("table_name") or "")
                ]
                schema_text.extend(
                    " ".join(
                        str(value)
                        for value in (
                            name,
                            types[index] if index < len(types) else "",
                            descriptions[index] if index < len(descriptions) else "",
                        )
                        if value
                    )
                    for index, name in enumerate(names)
                )
                full_schema_tokens += len(tokenize("\n".join(schema_text)))
            payload = {
                "candidate_tables": tables,
                "candidate_columns": columns,
                "full_schema_tokens": full_schema_tokens,
            }
            output[(dialect, database_dir.name.casefold())] = payload
            normalized_name = re.sub(
                r"[^a-z0-9]", "", database_dir.name.casefold()
            )
            output[(dialect, normalized_name)] = payload
    return output


def schema_family_closure(schema_root: Path) -> dict[str, frozenset[str]]:
    """Map every table to its exact name/type schema-equivalence family."""
    output: dict[str, frozenset[str]] = {}
    for database_dir in sorted(
        path
        for dialect_dir in schema_root.iterdir()
        if dialect_dir.is_dir()
        for path in dialect_dir.iterdir()
        if path.is_dir()
    ):
        groups: dict[tuple[tuple[str, str], ...], set[str]] = defaultdict(set)
        for path in database_dir.rglob("*.json"):
            try:
                row = json.loads(path.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, UnicodeDecodeError):
                continue
            if not isinstance(row, dict) or "table_name" not in row:
                continue
            names = row.get("nested_column_names") or row.get("column_names") or []
            types = row.get("nested_column_types") or row.get("column_types") or []
            signature = tuple(
                (
                    str(name).casefold(),
                    str(types[index] if index < len(types) else "").casefold(),
                )
                for index, name in enumerate(names)
            )
            table = normalize_table(
                str(row.get("table_fullname") or row["table_name"])
            )
            if "." not in table:
                continue
            groups[signature].add(table)
        for members in groups.values():
            family = frozenset(members)
            for table in members:
                output[table] = family
    return output


def apply_schema_family_closure(
    predicted: set[str], families: dict[str, frozenset[str]]
) -> tuple[set[str], set[str]]:
    expanded = set(predicted)
    for table in predicted:
        expanded.update(families.get(table, ()))
    return expanded, expanded - predicted


def lineage_stem(table: str) -> str:
    prefix, separator, name = table.rpartition(".")
    if not separator:
        prefix = ""
    stem = re.sub(
        r"(?:_r\d+(?:_v\d+)?|_v\d+|_?\d{4,8})$", "", name, flags=re.IGNORECASE
    )
    return f"{prefix}.{stem}" if prefix else stem


def schema_lineage_closure(schema_root: Path) -> dict[str, frozenset[str]]:
    groups: dict[str, set[str]] = defaultdict(set)
    for path in schema_root.rglob("*.json"):
        try:
            row = json.loads(path.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, UnicodeDecodeError):
            continue
        if not isinstance(row, dict) or "table_name" not in row:
            continue
        table = normalize_table(str(row.get("table_fullname") or row["table_name"]))
        if "." not in table:
            continue
        stem = lineage_stem(table)
        if stem != table:
            groups[stem].add(table)
    output: dict[str, frozenset[str]] = {}
    for members in groups.values():
        lineage = frozenset(members)
        for table in members:
            output[table] = lineage
    return output


def dialect_for_instance(instance_id: str) -> str:
    if instance_id.startswith("local"):
        return "sqlite"
    if instance_id.startswith("sf"):
        return "snowflake"
    return "bigquery"


def scale_bucket(columns: int | None) -> str:
    if columns is None:
        return "unknown"
    if columns <= 100:
        return "le100"
    if columns <= 500:
        return "101_500"
    if columns <= 1000:
        return "501_1000"
    if columns <= 3000:
        return "1001_3000"
    return "gt3000"


def mean(rows: list[dict[str, Any]], key: str) -> float | None:
    values = [float(row[key]) for row in rows if row.get(key) is not None]
    return round(statistics.fmean(values), 6) if values else None


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--questions", type=Path, required=True)
    parser.add_argument("--gold-tables", type=Path, required=True)
    parser.add_argument("--linking-results", type=Path, required=True)
    parser.add_argument("--schema-root", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--upstream-commit", required=True)
    parser.add_argument("--family-closure", action="store_true")
    parser.add_argument("--lineage-closure", action="store_true")
    args = parser.parse_args()

    questions = {
        row["instance_id"]: row
        for row in (
            json.loads(line)
            for line in args.questions.read_text(encoding="utf-8").splitlines()
            if line.strip()
        )
    }
    gold = {
        row["instance_id"]: row["gold_tables"]
        for row in (
            json.loads(line)
            for line in args.gold_tables.read_text(encoding="utf-8").splitlines()
            if line.strip()
        )
    }
    id_remaps: dict[str, str] = {}
    for gold_id in sorted(set(gold) - set(questions)):
        corrected_id = f"sf_{gold_id}"
        if corrected_id in questions and corrected_id not in gold:
            gold[corrected_id] = gold.pop(gold_id)
            id_remaps[corrected_id] = gold_id
    if set(questions) != set(gold):
        raise ValueError("Spider2 questions and gold-table IDs differ")
    sizes = schema_size_by_database(args.schema_root)
    families = schema_family_closure(args.schema_root) if args.family_closure else {}
    lineages = (
        schema_lineage_closure(args.schema_root) if args.lineage_closure else {}
    )
    rows: list[dict[str, Any]] = []
    missing_outputs: list[str] = []
    for instance_id, question in questions.items():
        result_id = instance_id
        path = args.linking_results / f"{result_id}.txt"
        if not path.exists() and instance_id in id_remaps:
            result_id = id_remaps[instance_id]
            path = args.linking_results / f"{result_id}.txt"
        if not path.exists():
            missing_outputs.append(instance_id)
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        predicted, predicted_columns = parse_autolink_prompt(text)
        closure_added: set[str] = set()
        if args.family_closure:
            predicted, closure_added = apply_schema_family_closure(predicted, families)
        if args.lineage_closure:
            predicted, lineage_added = apply_schema_family_closure(predicted, lineages)
            closure_added.update(lineage_added)
        expected = {normalize_table(table) for table in gold[instance_id]}
        database_key = (
            dialect_for_instance(instance_id),
            str(question["db"]).casefold(),
        )
        size = sizes.get(database_key)
        if size is None:
            size = sizes.get(
                (database_key[0], re.sub(r"[^a-z0-9]", "", database_key[1])), {}
            )
        matched = predicted & expected
        released_prompt_tokens = len(tokenize(text))
        compact_tokens = compact_schema_tokens(text)
        closure_name_tokens = sum(len(tokenize(table)) for table in closure_added)
        total_input_tokens = compact_tokens + closure_name_tokens
        full_schema_tokens = size.get("full_schema_tokens")
        rows.append(
            {
                "instance_id": instance_id,
                "released_result_id": result_id,
                "db": question["db"],
                "dialect": database_key[0],
                "scale_bucket": scale_bucket(size.get("candidate_columns")),
                **size,
                "gold_tables": sorted(expected),
                "predicted_tables": sorted(predicted),
                "family_closure_added_tables": sorted(closure_added),
                "metrics": {
                    "table_recall": len(matched) / len(expected),
                    "table_strict_recall": float(expected <= predicted),
                    "selected_tables": len(predicted),
                    "selected_columns": predicted_columns,
                    "released_prompt_tokens": released_prompt_tokens,
                    "compact_schema_tokens": compact_tokens,
                    "closure_name_tokens": closure_name_tokens,
                    "total_input_tokens": total_input_tokens,
                    "context_compression": (
                        1.0 - total_input_tokens / full_schema_tokens
                        if full_schema_tokens
                        else None
                    ),
                },
            }
        )

    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(
        "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows),
        encoding="utf-8",
    )
    flattened = [
        {**row, **row["metrics"]}
        for row in rows
    ]
    bucket_summary = {}
    for bucket in ("le100", "101_500", "501_1000", "1001_3000", "gt3000", "unknown"):
        selected = [row for row in flattened if row["scale_bucket"] == bucket]
        if selected:
            bucket_summary[bucket] = {
                "rows": len(selected),
                "table_recall": mean(selected, "table_recall"),
                "table_strict_recall": mean(selected, "table_strict_recall"),
                "selected_tables": mean(selected, "selected_tables"),
                "selected_columns": mean(selected, "selected_columns"),
                "released_prompt_tokens": mean(selected, "released_prompt_tokens"),
                "compact_schema_tokens": mean(selected, "compact_schema_tokens"),
                "closure_name_tokens": mean(selected, "closure_name_tokens"),
                "total_input_tokens": mean(selected, "total_input_tokens"),
                "context_compression": mean(selected, "context_compression"),
            }
    summary = {
        "protocol": {
            "task": "Spider 2.0-Lite released gold-table schema-linking audit",
            "method": (
                "AutoLink released outputs plus deterministic closure"
                if args.family_closure or args.lineage_closure
                else "AutoLink authors-released linking outputs"
            ),
            "upstream_commit": args.upstream_commit,
            "oracle_tables_note": "gold tables are used for scoring only",
            "metric_scope": "table recall; this is not full table-plus-column SRR",
            "family_closure": args.family_closure,
            "lineage_closure": args.lineage_closure,
            "family_closure_rule": (
                "expand a selected table only to tables in the same database with "
                "an exactly identical ordered nested column-name/type signature"
                if args.family_closure
                else None
            ),
            "lineage_closure_rule": (
                "expand only within one dataset when a selected table shares the "
                "same identifier after removing a terminal date/year or rN/vN "
                "version suffix"
                if args.lineage_closure
                else None
            ),
        },
        "inputs_sha256": {
            "questions": file_sha256(args.questions),
            "gold_tables": file_sha256(args.gold_tables),
        },
        "dataset_rows": len(questions),
        "evaluated_rows": len(rows),
        "coverage": round(len(rows) / len(questions), 6),
        "missing_output_ids": sorted(missing_outputs),
        "official_gold_id_remaps": id_remaps,
        "metrics": {
            "table_recall": mean(flattened, "table_recall"),
            "table_strict_recall": mean(flattened, "table_strict_recall"),
            "selected_tables": mean(flattened, "selected_tables"),
            "selected_columns": mean(flattened, "selected_columns"),
            "released_prompt_tokens": mean(flattened, "released_prompt_tokens"),
            "compact_schema_tokens": mean(flattened, "compact_schema_tokens"),
            "closure_name_tokens": mean(flattened, "closure_name_tokens"),
            "total_input_tokens": mean(flattened, "total_input_tokens"),
            "context_compression": mean(flattened, "context_compression"),
        },
        "by_scale_bucket": bucket_summary,
    }
    summary_path = args.output.with_suffix(".summary.json")
    summary_path.write_text(
        json.dumps(summary, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
