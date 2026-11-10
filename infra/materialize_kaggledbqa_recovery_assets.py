#!/usr/bin/env python3
"""Freeze safe few-shot SQL and gold-blind KaggleDBQA recovery inputs."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from finsemguard.schema_recovery.kaggledbqa_assets import (
    materialize_kaggledbqa_recovery_assets,
    materialize_kaggledbqa_safe_history,
)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--online-test-manifest", type=Path, required=True)
    parser.add_argument("--data-root", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument("--values-off", action="store_true")
    parser.add_argument("--value-sample-limit", type=int, default=5)
    parser.add_argument("--max-history-per-column", type=int, default=8)
    args = parser.parse_args()

    history = args.output_root / "history" / "fewshot_ast_disjoint.jsonl"
    history_manifest = history.with_suffix(history.suffix + ".manifest.json")
    materialize_kaggledbqa_safe_history(
        data_root=args.data_root,
        output=history,
        manifest_output=history_manifest,
    )
    manifest = materialize_kaggledbqa_recovery_assets(
        online_manifest=args.online_test_manifest,
        data_root=args.data_root,
        historical_sql_kb=history,
        historical_sql_kb_manifest=history_manifest,
        benchmark_output=args.output_root / "columns.jsonl",
        manifest_output=args.output_root / "MANIFEST.json",
        values_on=not args.values_off,
        value_sample_limit=args.value_sample_limit,
        max_history_per_column=args.max_history_per_column,
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
