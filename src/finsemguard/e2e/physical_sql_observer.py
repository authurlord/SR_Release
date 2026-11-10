"""Physical query observations in a configured SQLite runtime; no evaluator interface."""
import json
from pathlib import Path
import sys
from types import SimpleNamespace

from finsemguard.e2e.react_text2sql import _grounded_binding_observations


def main():
    request = json.load(sys.stdin)
    if set(request) not in ({"database", "sql", "binding_probes"},
                            {"database", "sql", "binding_probes", "relational_grain"}):
        raise ValueError("Only physical database, submitted SQL and probes are accepted")
    result = _grounded_binding_observations(
        SimpleNamespace(database=Path(request["database"])),
        {"binding_probes": request["binding_probes"]}, request["sql"],
        relational_grain=request.get("relational_grain", False) is True)
    json.dump(result, sys.stdout, ensure_ascii=False)


if __name__ == "__main__":
    main()
