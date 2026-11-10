from __future__ import annotations

import argparse
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
import time
from pathlib import Path
from typing import Any, Literal

from pydantic import BaseModel, ConfigDict, Field, field_validator

from finsemguard.agent.llm import VLLMClient
from finsemguard.config import load_config


EvidenceProfile = Literal[
    "raw",
    "raw_values",
    "raw_sql",
    "raw_workload",
    "full_sql",
    "full",
]
PROFILE_PARTS: dict[EvidenceProfile, tuple[str, ...]] = {
    "raw": ("raw_schema", "relationships"),
    "raw_values": ("raw_schema", "relationships", "value_profile"),
    "raw_sql": ("raw_schema", "relationships", "history_sql"),
    "raw_workload": ("raw_schema", "relationships", "workload_history"),
    "full_sql": ("raw_schema", "relationships", "value_profile", "history_sql"),
    "full": ("raw_schema", "relationships", "value_profile", "workload_history"),
}


class RecoveredSemantics(BaseModel):
    model_config = ConfigDict(extra="ignore")

    canonical_name: str
    description: str
    semantic_type: Literal[
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
        "unknown",
    ] = "unknown"
    value_meanings: dict[str, str] = Field(default_factory=dict)
    unit: str | None = None
    date_format: str | None = None
    temporal_scope: str | None = None
    confidence: float = Field(ge=0.0, le=1.0)
    evidence_ids: list[str] = Field(default_factory=list)
    uncertainties: list[str] = Field(default_factory=list)

    @field_validator("semantic_type", mode="before")
    @classmethod
    def normalize_semantic_type(cls, value: Any) -> Any:
        aliases = {
            "number": "quantity",
            "numeric": "quantity",
            "integer": "quantity",
            "float": "quantity",
            "rank": "quantity",
            "ordinal": "quantity",
            "score": "quantity",
            "rating": "quantity",
            "percentage": "rate",
            "datetime": "date",
            "timestamp": "date",
            "time": "date",
            "boolean": "category",
            "categorical": "category",
            "string": "text",
            "id": "identifier",
        }
        return aliases.get(str(value).strip().lower(), value)

    @field_validator("value_meanings", mode="before")
    @classmethod
    def normalize_value_meanings(cls, value: Any) -> dict[str, str]:
        if not value:
            return {}
        if isinstance(value, dict):
            return {str(key): str(item) for key, item in value.items()}
        if isinstance(value, list):
            result = {}
            for item in value:
                if isinstance(item, dict) and "value" in item and "meaning" in item:
                    result[str(item["value"])] = str(item["meaning"])
            return result
        return {}

    @field_validator("evidence_ids", "uncertainties", mode="before")
    @classmethod
    def normalize_lists(cls, value: Any) -> list[str]:
        if value is None:
            return []
        values = value if isinstance(value, list) else [value]
        return [str(item) for item in values]


SYSTEM_PROMPT = """You recover the semantics of ONE ambiguous database column.
This is schema recovery, not question answering and not SQL generation.

Use only the supplied raw schema, relationships, observed values, and historical SQL.
Historical SQL contains no natural-language questions. Treat it as behavioral evidence,
not as an infallible definition. Never invent a code meaning, unit, date format, or year.
When evidence is insufficient, use null/unknown, lower confidence, and state the gap in
uncertainties. Cite only supplied evidence_id values.

Return one JSON object with exactly these semantic fields:
canonical_name, description, semantic_type, value_meanings, unit, date_format,
temporal_scope, confidence, evidence_ids, uncertainties.
semantic_type must be one of identifier, category, code, date, currency, count, ratio,
rate, duration, quantity, text, unknown. confidence is between 0 and 1.
Keep description under 60 words, value_meanings to at most 8 observed mappings, and
uncertainties to at most 5 concise items so that the JSON object remains bounded.
"""


def select_evidence(record: dict[str, Any], profile: EvidenceProfile) -> dict[str, Any]:
    """Copy only allowed evidence; never copy target-derived labels or targets."""
    evidence = record["evidence"]
    return {name: evidence[name] for name in PROFILE_PARTS[profile]}


def evidence_ids(value: Any) -> set[str]:
    result: set[str] = set()
    if isinstance(value, dict):
        if "evidence_id" in value:
            result.add(str(value["evidence_id"]))
        for item in value.values():
            result.update(evidence_ids(item))
    elif isinstance(value, list):
        for item in value:
            result.update(evidence_ids(item))
    return result


def build_prompt(
    record: dict[str, Any], profile: EvidenceProfile
) -> tuple[str, str, set[str]]:
    selected = select_evidence(record, profile)
    payload = {
        "task": "recover_column_semantics",
        "profile": profile,
        "column_id": record["column_id"],
        "evidence": selected,
    }
    return (
        SYSTEM_PROMPT,
        json.dumps(payload, ensure_ascii=False, indent=2),
        evidence_ids(selected),
    )


def load_rows(path: Path, ambiguous_only: bool) -> list[dict[str, Any]]:
    rows = [
        json.loads(line)
        for line in path.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    if ambiguous_only:
        rows = [row for row in rows if row["is_ambiguous"]]
    return rows


def stratified_rows(
    rows: list[dict[str, Any]], per_db_limit: int, seed: int = 42
) -> list[dict[str, Any]]:
    by_database: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        by_database[row["db_id"]].append(row)
    selected = []
    for db_id in sorted(by_database):
        ranked = sorted(
            by_database[db_id],
            key=lambda row: hashlib.sha256(
                f"{seed}:{row['column_id']}".encode()
            ).hexdigest(),
        )
        selected.extend(ranked[:per_db_limit])
    return selected


def recover_one(
    client: VLLMClient, record: dict[str, Any], profile: EvidenceProfile
) -> dict[str, Any]:
    system, user, supplied_ids = build_prompt(record, profile)
    started = time.perf_counter()
    payload, usage = client.chat_json_with_metadata(system, user)
    prediction = RecoveredSemantics.model_validate(payload)
    return {
        "column_id": record["column_id"],
        "profile": profile,
        "prediction": prediction.model_dump(mode="json"),
        "supplied_evidence_ids": sorted(supplied_ids),
        "usage": usage,
        "latency_seconds": round(time.perf_counter() - started, 3),
    }


def recover_or_error(
    client: VLLMClient, record: dict[str, Any], profile: EvidenceProfile
) -> dict[str, Any]:
    try:
        return recover_one(client, record, profile)
    except Exception as error:
        return {
            "column_id": record["column_id"],
            "profile": profile,
            "error": f"{type(error).__name__}: {error}",
        }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--benchmark", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--profile", choices=sorted(PROFILE_PARTS), required=True)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--per-db-limit", type=int)
    parser.add_argument("--include-controls", action="store_true")
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--retry-errors", action="store_true")
    parser.add_argument("--concurrency", type=int, default=1)
    parser.add_argument("--config", default="configs/base.yaml")
    args = parser.parse_args()

    if args.resume and args.retry_errors:
        raise ValueError("--resume and --retry-errors are mutually exclusive")
    if args.concurrency < 1:
        raise ValueError("--concurrency must be positive")

    profile: EvidenceProfile = args.profile
    rows = load_rows(args.benchmark, ambiguous_only=not args.include_controls)
    if args.limit is not None and args.per_db_limit is not None:
        raise ValueError("--limit and --per-db-limit are mutually exclusive")
    if args.per_db_limit is not None:
        rows = stratified_rows(rows, args.per_db_limit)
    if args.limit is not None:
        rows = rows[: args.limit]
    if not rows:
        raise ValueError("no benchmark rows selected")

    config = load_config(args.config)
    client = VLLMClient(config["llm"])
    if not client.healthy():
        raise RuntimeError(f"vLLM is unavailable at {client.base_url}")

    args.output.parent.mkdir(parents=True, exist_ok=True)
    if args.retry_errors:
        if not args.output.exists():
            raise ValueError("--retry-errors requires an existing output")
        existing = [
            json.loads(line)
            for line in args.output.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        if [row["column_id"] for row in existing] != [
            row["column_id"] for row in rows
        ] or any(row.get("profile") != profile for row in existing):
            raise ValueError("existing results do not match task ordering")
        failures = [
            (index, row)
            for index, (row, result) in enumerate(zip(rows, existing, strict=True))
            if "prediction" not in result
        ]
        with ThreadPoolExecutor(max_workers=args.concurrency) as executor:
            results = executor.map(
                lambda task: recover_or_error(client, task[1], profile), failures
            )
            for retry_index, ((index, row), result) in enumerate(
                zip(failures, results, strict=True), start=1
            ):
                existing[index] = result
                print(
                    f"[retry {retry_index:02d}/{len(failures)}] "
                    f"{row['column_id']} profile={profile} "
                    f"status={'ok' if 'prediction' in result else 'error'}",
                    flush=True,
                )
        temporary = args.output.with_suffix(args.output.suffix + ".tmp")
        temporary.write_text(
            "".join(json.dumps(row, ensure_ascii=False) + "\n" for row in existing),
            encoding="utf-8",
        )
        temporary.replace(args.output)
        errors = [row for row in existing if "prediction" not in row]
        if errors:
            raise ValueError(f"recovery results contain {len(errors)} errors")
        return

    completed: list[dict[str, Any]] = []
    if args.resume and args.output.exists():
        completed = [
            json.loads(line)
            for line in args.output.read_text(encoding="utf-8").splitlines()
            if line.strip()
        ]
        expected = [row["column_id"] for row in rows[: len(completed)]]
        actual = [row["column_id"] for row in completed]
        if actual != expected or any(row.get("profile") != profile for row in completed):
            raise ValueError("existing results are not a matching prefix")

    mode = "a" if completed else "w"
    pending = rows[len(completed) :]
    with args.output.open(mode, encoding="utf-8") as handle:
        with ThreadPoolExecutor(max_workers=args.concurrency) as executor:
            results = executor.map(
                lambda row: recover_or_error(client, row, profile), pending
            )
            for index, (row, result) in enumerate(
                zip(pending, results, strict=True), start=len(completed) + 1
            ):
                handle.write(json.dumps(result, ensure_ascii=False) + "\n")
                handle.flush()
                status = "ok" if "prediction" in result else "error"
                print(
                    f"[{index:02d}/{len(rows)}] {row['column_id']} "
                    f"profile={profile} status={status} "
                    f"latency={result.get('latency_seconds', 0):.3f}s",
                    flush=True,
                )

    selection_hash = hashlib.sha256(
        json.dumps([row["column_id"] for row in rows]).encode()
    ).hexdigest()
    print(
        json.dumps(
            {
                "task": "schema_recovery",
                "profile": profile,
                "selected": len(rows),
                "selection_sha256": selection_hash,
                "output": str(args.output),
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
