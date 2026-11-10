#!/usr/bin/env python3
"""Run the native BIRD scorer with the frozen no-deadline default."""
from __future__ import annotations

import argparse
from pathlib import Path
import sys
from types import SimpleNamespace

ROOT = Path(__file__).resolve().parents[1]
sys.path[:0] = [str(ROOT / "src"), str(ROOT / "infra")]
import evaluate_bird_external as native


class PaperScoreParser(argparse.ArgumentParser):
    def add_argument(self, *names, **options):
        if "--timeout-seconds" in names:
            options["default"] = None
            options["help"] = "SQL deadline in seconds; omitted uses the frozen no-deadline protocol"
        return super().add_argument(*names, **options)


def main() -> None:
    # Adapt only the native CLI default. Its execution, comparison and outputs
    # are retained, including execute_rows(timeout_seconds=None).
    native.argparse = SimpleNamespace(
        ArgumentParser=PaperScoreParser, ArgumentTypeError=argparse.ArgumentTypeError
    )
    native.main()


if __name__ == "__main__":
    main()
