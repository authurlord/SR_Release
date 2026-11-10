#!/usr/bin/env python3
"""Score several BIRD predictions once and produce a paired baseline comparison."""

from __future__ import annotations

import argparse
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor, as_completed
from hashlib import sha256
import json
import math
from pathlib import Path
import random
from typing import Any

from finsemguard.e2e.livesqlbench_runner import _load_jsonl
from finsemguard.e2e.performance_pipeline import _database_path
from finsemguard.eval.bird import execute_rows, official_ex, wilson_interval


def _sha256(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def _keyed(path: Path) -> dict[str, dict[str, Any]]:
    rows = _load_jsonl(path)
    output = {str(row["example_id"]): row for row in rows}
    if len(output) != len(rows):
        raise ValueError(f"duplicate example_id in {path}")
    return output


def _prediction_arg(value: str) -> tuple[str, Path]:
    label, separator, path = value.partition("=")
    if not separator or not label or not path:
        raise argparse.ArgumentTypeError("prediction must be LABEL=PATH")
    if not label.replace("_", "").replace("-", "").isalnum():
        raise argparse.ArgumentTypeError("prediction label must be alphanumeric")
    return label, Path(path)


def _exact_mcnemar(fixes: int, regressions: int) -> float:
    discordant = fixes + regressions
    if discordant == 0:
        return 1.0
    tail = min(fixes, regressions)
    probability = sum(math.comb(discordant, k) for k in range(tail + 1)) / (
        2**discordant
    )
    return min(1.0, 2 * probability)


def _condition_summary(rows: list[dict[str, Any]], label: str) -> dict[str, Any]:
    scored_rows = [row for row in rows if row["gold_error"] is None]
    correct = sum(bool(row["methods"][label]["official_ex"]) for row in scored_rows)
    by_database: dict[str, Counter[str]] = defaultdict(Counter)
    by_difficulty: dict[str, Counter[str]] = defaultdict(Counter)
    for row in scored_rows:
        value = bool(row["methods"][label]["official_ex"])
        by_database[str(row["database_id"])]["n"] += 1
        by_database[str(row["database_id"])]["correct"] += int(value)
        by_difficulty[str(row["difficulty"])]["n"] += 1
        by_difficulty[str(row["difficulty"])]["correct"] += int(value)

    def render(groups: dict[str, Counter[str]]) -> dict[str, Any]:
        return {
            key: {
                "n": values["n"],
                "correct": values["correct"],
                "execution_accuracy_pct": round(
                    100 * values["correct"] / max(values["n"], 1), 2
                ),
            }
            for key, values in sorted(groups.items())
        }

    return {
        "n": len(scored_rows),
        "total_rows": len(rows),
        "excluded_gold_errors": len(rows) - len(scored_rows),
        "correct": correct,
        "execution_accuracy_pct": round(
            100 * correct / max(len(scored_rows), 1), 2
        ),
        "wilson_95_pct": wilson_interval(correct, len(scored_rows)),
        "prediction_errors": sum(
            row["methods"][label]["error"] is not None for row in scored_rows
        ),
        "by_database": render(by_database),
        "by_difficulty": render(by_difficulty),
    }


def _lean_condition_summary(
    rows: list[dict[str, Any]], label: str
) -> dict[str, Any]:
    """Return only the paper-facing count and denominator.

    This intentionally omits confidence intervals, resampling, subgroup audits,
    and input hashes for fast result iteration.
    """

    scored_rows = [row for row in rows if row["gold_error"] is None]
    correct = sum(bool(row["methods"][label]["official_ex"]) for row in scored_rows)
    return {
        "n": len(scored_rows),
        "total_rows": len(rows),
        "excluded_gold_errors": len(rows) - len(scored_rows),
        "correct": correct,
        "execution_accuracy_pct": round(
            100 * correct / max(len(scored_rows), 1), 2
        ),
        "prediction_errors": sum(
            row["methods"][label]["error"] is not None for row in scored_rows
        ),
    }


def _cluster_bootstrap(
    rows: list[dict[str, Any]], baseline: str, method: str,
    *, samples: int = 10_000, seed: int = 20260808,
) -> dict[str, Any]:
    by_database: dict[str, list[int]] = defaultdict(list)
    for row in rows:
        if row["gold_error"] is not None:
            continue
        by_database[str(row["database_id"])].append(
            int(row["methods"][method]["official_ex"])
            - int(row["methods"][baseline]["official_ex"])
        )
    databases = sorted(by_database)
    rng = random.Random(seed)
    deltas: list[float] = []
    for _ in range(samples):
        selected = [rng.choice(databases) for _ in databases]
        values = [value for database in selected for value in by_database[database]]
        deltas.append(100 * sum(values) / len(values))
    deltas.sort()
    return {
        "unit": "database_id",
        "databases": len(databases),
        "samples": samples,
        "seed": seed,
        "delta_percentage_points_ci95": [
            deltas[int(0.025 * samples)],
            deltas[min(samples - 1, int(0.975 * samples))],
        ],
    }


def _paired_summary(
    rows: list[dict[str, Any]], baseline: str, method: str
) -> dict[str, Any]:
    scored_rows = [row for row in rows if row["gold_error"] is None]
    fixes = regressions = 0
    database_delta: dict[str, Counter[str]] = defaultdict(Counter)
    difficulty_delta: dict[str, Counter[str]] = defaultdict(Counter)
    for row in scored_rows:
        base = bool(row["methods"][baseline]["official_ex"])
        candidate = bool(row["methods"][method]["official_ex"])
        fixes += int(candidate and not base)
        regressions += int(base and not candidate)
        for groups, key in (
            (database_delta, str(row["database_id"])),
            (difficulty_delta, str(row["difficulty"])),
        ):
            groups[key]["n"] += 1
            groups[key]["baseline"] += int(base)
            groups[key]["method"] += int(candidate)

    def render(groups: dict[str, Counter[str]]) -> dict[str, Any]:
        output: dict[str, Any] = {}
        for key, values in sorted(groups.items()):
            delta = values["method"] - values["baseline"]
            output[key] = {
                "n": values["n"],
                "baseline_correct": values["baseline"],
                "method_correct": values["method"],
                "delta_correct": delta,
                "delta_pp": round(100 * delta / max(values["n"], 1), 2),
            }
        return output

    database_rows = render(database_delta)
    return {
        "baseline": baseline,
        "method": method,
        "n": len(scored_rows),
        "total_rows": len(rows),
        "excluded_gold_errors": len(rows) - len(scored_rows),
        "fixes": fixes,
        "regressions": regressions,
        "net_fixes": fixes - regressions,
        "delta_pp": round(
            100 * (fixes - regressions) / max(len(scored_rows), 1), 2
        ),
        "exact_mcnemar_p": _exact_mcnemar(fixes, regressions),
        "database_direction": {
            "improved": sum(row["delta_correct"] > 0 for row in database_rows.values()),
            "tied": sum(row["delta_correct"] == 0 for row in database_rows.values()),
            "worse": sum(row["delta_correct"] < 0 for row in database_rows.values()),
        },
        "by_database": database_rows,
        "by_difficulty": render(difficulty_delta),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-root", type=Path, required=True)
    parser.add_argument("--online", type=Path, required=True)
    parser.add_argument("--evaluator", type=Path, required=True)
    parser.add_argument(
        "--prediction", action="append", type=_prediction_arg, required=True
    )
    parser.add_argument("--baseline-label", required=True)
    parser.add_argument("--method-label", required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument("--timeout-seconds", type=float, default=30.0)
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--example-id", action="append", default=[])
    parser.add_argument(
        "--lean",
        action="store_true",
        help="emit only exact counts/deltas; skip hashes, subgroup audits, and resampling",
    )
    args = parser.parse_args()
    if args.workers < 1:
        raise ValueError("--workers must be positive")

    labels = [label for label, _ in args.prediction]
    if len(set(labels)) != len(labels):
        raise ValueError("prediction labels must be unique")
    if args.baseline_label not in labels or args.method_label not in labels:
        raise ValueError("paired labels must be present in --prediction")
    online_rows = _load_jsonl(args.online)
    if args.example_id:
        selected_ids = set(args.example_id)
        online_rows = [
            row for row in online_rows if str(row["example_id"]) in selected_ids
        ]
        if {str(row["example_id"]) for row in online_rows} != selected_ids:
            raise ValueError("one or more requested example IDs are absent")
    expected = {str(row["example_id"]) for row in online_rows}
    evaluator = {
        key: row for key, row in _keyed(args.evaluator).items() if key in expected
    }
    predictions = {
        label: {
            key: row for key, row in _keyed(path).items() if key in expected
        }
        for label, path in args.prediction
    }
    if set(evaluator) != expected:
        raise ValueError("evaluator sidecar does not match online manifest")
    for label, rows in predictions.items():
        if set(rows) != expected:
            raise ValueError(f"prediction coverage mismatch: {label}")

    def score_one(index: int, online: dict[str, Any]) -> tuple[int, dict[str, Any]]:
        example_id = str(online["example_id"])
        gold = evaluator[example_id]["gold"]
        database = _database_path(args.data_root, online)
        gold_rows = None
        gold_error = None
        try:
            gold_rows = execute_rows(
                database, str(gold["sql"]), timeout_seconds=args.timeout_seconds
            )
        except Exception as error:
            gold_error = f"{type(error).__name__}: {error}"[:1000]
        methods: dict[str, Any] = {}
        local_cache: dict[str, tuple[list[tuple[Any, ...]] | None, str | None]] = {}
        for label in labels:
            prediction = predictions[label][example_id]
            sql = str(prediction.get("sql") or "").strip()
            if sql not in local_cache:
                predicted_rows = None
                predicted_error = None
                try:
                    predicted_rows = execute_rows(
                        database, sql, timeout_seconds=args.timeout_seconds
                    )
                except Exception as error:
                    predicted_error = f"{type(error).__name__}: {error}"[:1000]
                local_cache[sql] = (predicted_rows, predicted_error)
            predicted_rows, predicted_error = local_cache[sql]
            correct = bool(
                gold_rows is not None
                and predicted_rows is not None
                and official_ex(predicted_rows, gold_rows)
            )
            methods[label] = {
                "sql": sql,
                "official_ex": correct,
                "error": predicted_error,
                "result_count": (
                    len(predicted_rows) if predicted_rows is not None else None
                ),
            }
        return index, {
            "example_id": example_id,
            "database_id": str(online["database_id"]),
            "difficulty": str(gold.get("difficulty") or "unknown"),
            "gold_error": gold_error,
            "gold_result_count": len(gold_rows) if gold_rows is not None else None,
            "methods": methods,
        }

    records_by_index: list[dict[str, Any] | None] = [None] * len(online_rows)
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {
            executor.submit(score_one, index, online): index
            for index, online in enumerate(online_rows)
        }
        for completed, future in enumerate(as_completed(futures), start=1):
            index, record = future.result()
            records_by_index[index] = record
            if completed % 20 == 0 or completed == len(online_rows):
                print(f"[bird-score {completed}/{len(online_rows)}]", flush=True)
    records = [row for row in records_by_index if row is not None]
    if len(records) != len(online_rows):
        raise AssertionError("BIRD scorer lost one or more rows")

    args.output_root.mkdir(parents=True, exist_ok=True)
    score_content = "".join(
        json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n" for row in records
    )
    score_path = args.output_root / "paired_scores.jsonl"
    if score_path.exists() and score_path.read_text(encoding="utf-8") != score_content:
        raise FileExistsError(f"refusing to overwrite different scores: {score_path}")
    if not score_path.exists():
        score_path.write_text(score_content, encoding="utf-8")
    if args.lean:
        conditions = {
            label: _lean_condition_summary(records, label) for label in labels
        }
        baseline_correct = int(conditions[args.baseline_label]["correct"])
        method_correct = int(conditions[args.method_label]["correct"])
        denominator = int(conditions[args.method_label]["n"])
        summary = {
            "protocol": "bird_official_ex_set_equality_lean_v1",
            "rows": len(records),
            "scorable_rows": denominator,
            "gold_execution_errors": len(records) - denominator,
            "timeout_seconds": args.timeout_seconds,
            "workers": args.workers,
            "conditions": conditions,
            "comparison": {
                "baseline": args.baseline_label,
                "method": args.method_label,
                "delta_correct": method_correct - baseline_correct,
                "delta_pp": round(
                    100 * (method_correct - baseline_correct)
                    / max(denominator, 1),
                    2,
                ),
            },
        }
    else:
        summary = {
            "protocol": "bird_official_ex_set_equality_paired_v2",
            "rows": len(records),
            "scorable_rows": sum(row["gold_error"] is None for row in records),
            "gold_execution_errors": sum(row["gold_error"] is not None for row in records),
            "timeout_seconds": args.timeout_seconds,
            "workers": args.workers,
            "conditions": {
                label: _condition_summary(records, label) for label in labels
            },
            "paired": _paired_summary(
                records, args.baseline_label, args.method_label
            ),
            "cluster_bootstrap": _cluster_bootstrap(
                records, args.baseline_label, args.method_label
            ),
            "inputs": {
                "online_sha256": _sha256(args.online),
                "evaluator_sha256": _sha256(args.evaluator),
                "predictions_sha256": {
                    label: _sha256(path) for label, path in args.prediction
                },
            },
        }
    summary_content = json.dumps(
        summary, ensure_ascii=False, indent=2, sort_keys=True
    ) + "\n"
    summary_path = args.output_root / "SUMMARY.json"
    if summary_path.exists() and summary_path.read_text(encoding="utf-8") != summary_content:
        raise FileExistsError(f"refusing to overwrite different summary: {summary_path}")
    if not summary_path.exists():
        summary_path.write_text(summary_content, encoding="utf-8")
    print(summary_content)


if __name__ == "__main__":
    main()
