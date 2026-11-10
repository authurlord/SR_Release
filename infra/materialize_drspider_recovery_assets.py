#!/usr/bin/env python3
"""Freeze gold-blind automatic recovery inputs for a Dr.Spider online subset."""

from __future__ import annotations

import argparse
import json
from pathlib import Path

from finsemguard.schema_recovery.drspider_assets import (
    materialize_drspider_recovery_assets,
)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--online-manifest", type=Path, required=True)
    parser.add_argument("--data-root", type=Path, required=True)
    parser.add_argument("--historical-sql-kb", type=Path, required=True)
    parser.add_argument("--output-root", type=Path, required=True)
    parser.add_argument("--values-off", action="store_true")
    parser.add_argument("--value-sample-limit", type=int, default=5)
    parser.add_argument("--max-history-per-column", type=int, default=8)
    args = parser.parse_args()

    manifest = materialize_drspider_recovery_assets(
        online_manifest=args.online_manifest,
        data_root=args.data_root,
        historical_sql_kb=args.historical_sql_kb,
        benchmark_output=args.output_root / "columns.jsonl",
        manifest_output=args.output_root / "MANIFEST.json",
        values_on=not args.values_off,
        value_sample_limit=args.value_sample_limit,
        max_history_per_column=args.max_history_per_column,
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
