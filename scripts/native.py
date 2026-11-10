#!/usr/bin/env python3
"""Run a bundled native entry point from this checkout."""
from __future__ import annotations

import argparse
import os
from pathlib import Path
import runpy
import sys

ROOT = Path(__file__).resolve().parents[1]
ENTRYPOINTS = {
    "sqlite": "infra/run_ontology_react.py",
    "beaver": "infra/run_beaver_full.py",
    "evoschema": "infra/run_evoschema_main.py",
    "spider2": "infra/run_spider2_dual_evidence_main.py",
    "spider2-react": "infra/run_spider2_react.py",
    "beaver-snapshot": "infra/materialize_beaver_sqlite_snapshots.py",
    "evoschema-snapshot": "infra/materialize_evoschema_current_sqlite.py",
    "fiben-ontology": "infra/materialize_fiben_operational_ontology.py",
    "kaggledbqa-inputs": "infra/materialize_kaggledbqa_recovery_assets.py",
    "kaggledbqa-ontology": "infra/materialize_kaggledbqa_operational_ontology.py",
    "drspider-inputs": "infra/materialize_drspider_recovery_assets.py",
    "bird-prepare": "src/finsemguard/data/bird.py",
    "bird-ontology": "infra/a100/build_bird_history_semantics.py",
    "fiben-prepare": "src/finsemguard/data/fiben.py",
    "raw": "infra/run_direct_raw_evidence_baseline.py",
    "bird-score": "infra/evaluate_bird_external.py",
}

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("entrypoint", choices=sorted(ENTRYPOINTS))
    parser.add_argument("arguments", nargs=argparse.REMAINDER)
    args = parser.parse_args()
    sys.path[:0] = [str(ROOT / "src"), str(ROOT / "infra")]
    os.environ["PYTHONPATH"] = str(ROOT / "src") + os.pathsep + os.environ.get("PYTHONPATH", "")
    sys.argv = [str(ROOT / ENTRYPOINTS[args.entrypoint]), *args.arguments]
    runpy.run_path(sys.argv[0], run_name="__main__")

if __name__ == "__main__":
    main()
