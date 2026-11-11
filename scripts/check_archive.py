#!/usr/bin/env python3
"""Check exported archives and cached guides without executing SQL or model requests."""
import gzip
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
D = ROOT / "dist"


def load(path):
    return json.loads(path.read_text())


def main():
    catalog = load(D / "data/catalog.json")
    groups = catalog["datasets"]
    assert len(groups) == 8
    cases = []
    guides = []
    schema_keys = set()
    for group in groups:
        assert group["databases"]
        for entry in group["databases"]:
            schema = load(D / entry["path"])
            key = (group["id"], schema["database"])
            assert key not in schema_keys
            schema_keys.add(key)
            assert schema["ontology"]["tables"]
            guide = load(D / entry["explanations"])
            assert guide["dataset"] == group["id"]
            assert guide["database"] == schema["database"]
            for language in ["en", "zh"]:
                content = guide["documents"][language]
                assert len(content["html"]) > 200
                assert (D / content["markdown"]).is_file()
            guides.append(guide)
            for case_info in schema["cases"]:
                case = load(D / case_info["path"])
                assert case["database"] == schema["database"]
                p = case["prediction"]
                assert p["example_id"] == case["id"]
                assert "sql" in p
                trace = case.get("saved_native_trace") or p
                assert isinstance(trace, dict)
                assert isinstance(trace.get("react", {}), dict)
                assert isinstance(case_info.get("trace_available"), bool)
                cases.append(case)
    assert len(schema_keys) == 370
    assert len(cases) == 4394
    assert len({(case["dataset"], case["id"]) for case in cases}) == 4394
    coverage = load(D / "data/full-result-coverage.json")
    for group, receipt in zip(groups, coverage, strict=True):
        ids = [case["id"] for entry in group["databases"] for case in entry["cases"]]
        assert len(ids) == len(set(ids)) == receipt["fixed_questions"] == receipt["indexed_questions"]
        import hashlib
        assert hashlib.sha256(json.dumps(sorted(ids)).encode()).hexdigest() == receipt["ids_sha256"]
    originals = {}
    source = ROOT.parent / "SchemaRecovery-r05-anchor-20261016/repro/v17_r05/predictions.jsonl.gz"
    with gzip.open(source, "rt") as handle:
        for row in map(json.loads, handle):
            if row["example_id"] in {"bird_history:1113", "bird_history:177", "bird_history:417"}:
                originals[row["example_id"]] = row
    for case in cases:
        if case["id"] in originals:
            assert case["prediction"] == originals[case["id"]]
    # The exported native alias revision receipts retain exact skipped counts.
    history = next(g for g in groups if g["id"] == "BIRD-History")
    for entry in history["databases"]:
        schema = load(D / entry["path"])
        for event in schema["maintenance"]:
            receipt = event["receipt"]
            assert len(receipt["skipped_ids"]) == receipt["unchanged_object_count"]
            assert event["model_calls"] == 0
    print(json.dumps({"datasets": 8, "schema_entries": 370, "query_traces": 4394,
                      "bilingual_guides": len(guides), "markdown_documents": len(guides) * 2,
                      "history_native_records_equal": len(originals), "new_model_requests": 0}))


if __name__ == "__main__":
    main()
