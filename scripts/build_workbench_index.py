#!/usr/bin/env python3
"""Build the workbench's small navigation index from the saved demo archive."""
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "dist"


def main():
    catalog = json.loads((ROOT / "data/catalog.json").read_text())
    result = {"datasets": [], "question_count": 0, "database_count": 0}
    for group in catalog["datasets"]:
        dataset = {"id": group["id"], "label": group.get("label", group["id"]), "databases": []}
        for entry in group["databases"]:
            source = json.loads((ROOT / entry["path"]).read_text())
            ontology = source.get("ontology", {})
            cases = []
            for case in entry["cases"]:
                path = ROOT / case["path"]
                if not path.is_file():
                    raise FileNotFoundError(path)
                cases.append({k: case.get(k) for k in (
                    "id", "question", "path", "result_status", "official_score", "evaluation_reason"
                )})
            dataset["databases"].append({
                "id": entry["id"], "path": entry["path"], "cases": cases,
                "table_count": len(ontology.get("tables", [])),
                "column_count": sum(len(t.get("columns", [])) for t in ontology.get("tables", [])),
                "object_count": len(ontology.get("objects", [])),
                "source_count": len(ontology.get("sources", [])),
                "history_sql_count": source.get("history_sql_count", 0),
                "update_count": len(source.get("maintenance", [])),
                "result_counts": dict(Counter(c["result_status"] or "unknown" for c in cases)),
            })
        dataset["question_count"] = sum(len(d["cases"]) for d in dataset["databases"])
        result["datasets"].append(dataset)
        result["database_count"] += len(dataset["databases"])
        result["question_count"] += dataset["question_count"]
    assert result["question_count"] == catalog["total_questions"]
    (ROOT / "archive-index.json").write_text(json.dumps(result, ensure_ascii=False, separators=(",", ":")) + "\n")
    print(json.dumps({k: v for k, v in result.items() if k != "datasets"}))


if __name__ == "__main__":
    main()
