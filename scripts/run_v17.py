#!/usr/bin/env python3
"""Resolve local paths and launch the native v17 r05 SQLite method."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import runpy
import sys

ROOT = Path(__file__).resolve().parents[1]
PATH_KEYS = (
    "data_root", "online", "table_inputs", "recovery", "workload_semantic_state",
    "semantic_memory", "anchor_predictions", "auxiliary_raw_predictions",
    "embedding_model", "embedding_cache", "retrieval_cache", "config", "output_root",
)
REVISION_FLAGS = (
    "evidence-first-history", "realize-semantic-revision", "scope-grounded-revision",
    "witness-consistent-revision", "grounded-binding-revision", "scope-faithful-revision",
    "relational-grain-revision", "entity-grain-revision", "lower-eligibility-revision",
)

def build_command(config: dict) -> list[str]:
    command = [sys.executable, str(ROOT / "infra/run_ontology_react.py")]
    command += ["--dataset-id", config["dataset_id"]]
    required = ("data_root", "online", "table_inputs", "recovery", "embedding_model", "embedding_cache", "config", "output_root")
    for key in required:
        if not config.get(key):
            raise ValueError(f"missing required path: {key}")
    for key in PATH_KEYS:
        if config.get(key):
            path = Path(config[key]).expanduser()
            if not path.is_absolute():
                path = ROOT / path
            command += ["--" + key.replace("_", "-"), str(path.resolve())]
    command += ["--condition", "graph_evo_semantic_program_main_v1"]
    command += ["--max-turns", "4", "--max-actions", "8", "--max-sql-executions", "3"]
    command += ["--physical-execution-python", sys.executable]
    command += ["--embedding-batch-size", "16", "--reranker-top-k", "30", "--reranker-timeout-seconds", "600"]
    command += ["--subset-size", str(config.get("subset_size", 1393)), "--concurrency", str(config.get("concurrency", 8))]
    if config.get("reranker_base_url"):
        command += ["--reranker-base-url", config["reranker_base_url"]]
    command += ["--" + flag for flag in REVISION_FLAGS]
    return command

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--paths", type=Path, required=True)
    parser.add_argument("--print-command", action="store_true")
    parser.add_argument("--resume", action="store_true")
    args = parser.parse_args()
    command = build_command(json.loads(args.paths.read_text()))
    if args.resume:
        command += ["--resume"]
    if args.print_command:
        print(json.dumps(command, indent=2))
        return
    sys.path[:0] = [str(ROOT / "src"), str(ROOT / "infra")]
    # Child SQL observers inherit the same installed package or explicit source path.
    import os
    os.environ["PYTHONPATH"] = str(ROOT / "src") + os.pathsep + os.environ.get("PYTHONPATH", "")
    sys.argv = command[1:]
    runpy.run_path(command[1], run_name="__main__")

if __name__ == "__main__":
    main()
