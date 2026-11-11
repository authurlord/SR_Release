#!/usr/bin/env python3
"""Project three saved v17 records into browser assets without inference."""
import argparse
import gzip
import hashlib
import json
from pathlib import Path
import sys
import tarfile

ROOT = Path(__file__).resolve().parents[1]


def dump(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, separators=(",", ":")))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--release", type=Path, default=ROOT.parent / "SR_Release")
    parser.add_argument("--anchor", type=Path, default=ROOT.parent / "SchemaRecovery-r05-anchor-20261016/repro/v17_r05")
    args = parser.parse_args()
    sys.path.insert(0, str(args.release / "src"))
    from finsemguard.e2e.operational_ontology import OperationalOntology
    from finsemguard.ontology_discovery.workload_semantics import WorkloadSemanticLayer
    from finsemguard.ontology_discovery.dependency_update import update_objects, update_layer
    from copy import deepcopy

    archive = args.release / "assets/ontology-v17-r05.tar.gz"
    with tarfile.open(archive) as bundle:
        state = json.load(bundle.extractfile("ontology/semantic_layer/state.json"))
        inputs = [json.loads(line) for line in bundle.extractfile("ontology/table_inputs.jsonl")]
        recovery = [json.loads(line) for line in bundle.extractfile("ontology/table_recovery.jsonl")]
        constructs = [json.load(bundle.extractfile("ontology/construct/" + name)) for name in
                      ["f1_joint_interpretation.json", "district_joint_interpretation.json"]]
    ids = {"bird_history:1113", "bird_history:177", "bird_history:417"}
    with gzip.open(args.anchor / "predictions.jsonl.gz", "rt") as handle:
        predictions = {row["example_id"]: row for row in map(json.loads, handle) if row["example_id"] in ids}
    if set(predictions) != ids:
        raise ValueError("missing selected saved prediction")
    provenance = {
        "archive": "v17 r05 · recovered saved run",
        "prediction_source": "repro/v17_r05/predictions.jsonl.gz",
        "prediction_sha256": hashlib.sha256((args.anchor / "predictions.jsonl.gz").read_bytes()).hexdigest(),
        "ontology_source": "assets/ontology-v17-r05.tar.gz",
        "ontology_sha256": hashlib.sha256(archive.read_bytes()).hexdigest(),
        "source_commit": "03fc25e3a472891f50056df1cc79b1557c7549f8",
        "export": "Selected saved JSON fields, unchanged SQL and observed result rows",
    }
    titles = {
        "bird_history:1113": "Qualifying stages & driver grain",
        "bird_history:177": "Eligibility & monthly consumption",
        "bird_history:417": "Ranking population & filter order",
    }
    catalog = []
    for identity in ["bird_history:1113", "bird_history:177", "bird_history:417"]:
        prediction = predictions[identity]
        context = prediction["database_id"]
        records = {key: row for key, row in state["records"].items() if row["schema_context"] == context}
        layer = WorkloadSemanticLayer(records, state["revision"])
        selected_inputs = [row for row in inputs if row["schema_context"] == context]
        ontology = layer.augment_ontology(OperationalOntology.from_recovery_inputs(selected_inputs, []))
        objects = layer.objects()
        data = {
            "id": identity, "title": titles[identity], "database": context,
            "question": prediction["react"]["initial_search_query"],
            "origin": "archive", "provenance": provenance,
            "ontology": {
                "revision": state["revision"],
                "sources": [{"evidence_id": "sql_log::" + key, **row} for key, row in records.items()],
                "objects": objects,
                "tables": selected_inputs,
                "recovery": [row for row in recovery if row["input_id"] in {r["input_id"] for r in selected_inputs}],
                "edges": [edge.as_dict() for edge in ontology.edges],
                "construct": [row for row in constructs if row["schema_context"] == context],
            },
            "prediction": prediction,
        }
        filename = identity.replace(":", "-") + ".json"
        dump(ROOT / "dist/data" / filename, data)
        catalog.append({k: data[k] for k in ["id", "title", "database", "question", "origin"]} |
                       {"path": "data/" + filename, "source_count": len(records), "object_count": len(objects)})
    databases = []
    for context in sorted({row["schema_context"] for row in state["records"].values()}):
        records = {key: row for key, row in state["records"].items() if row["schema_context"] == context}
        layer = WorkloadSemanticLayer(records, state["revision"])
        objects = layer.objects()
        tables = [row for row in inputs if row["schema_context"] == context]
        ontology = layer.augment_ontology(OperationalOntology.from_recovery_inputs(tables, []))
        events = []
        for obj in objects:
            prior = obj.get("superseded_alias_hypotheses")
            if obj["kind"] != "column" or not prior or prior == obj.get("aliases"):
                continue
            previous = deepcopy(objects)
            next(row for row in previous if row["id"] == obj["id"])["aliases"] = list(prior)
            after, receipt = update_objects(previous, previous, interpretations={obj["id"]: {"aliases": obj["aliases"]}})
            events.append({"title": "Recorded alias revision · " + ", ".join(obj["physical_identifiers"]),
                           "event_type": "saved_alias_revision_replayed_on_copy", "method": "dependency_update.update_objects",
                           "source": "Archived superseded_alias_hypotheses → archived aliases",
                           "model_calls": 0, "receipt": receipt,
                           "column_changes": [{"physical_identifiers": obj["physical_identifiers"], "before": prior, "after": obj["aliases"]}]})
            if len(events) == 3:
                break
        if not events:
            key, source = next(iter(records.items()))
            after, receipt = update_layer(WorkloadSemanticLayer(deepcopy(records), state["revision"]), objects, [],
                                           retract=((context, source["history_id"]),))
            after_by_id = {row["id"]: row for row in after}
            changes = [{"physical_identifiers": obj["physical_identifiers"], "before": obj.get("aliases", []),
                        "after": after_by_id.get(obj["id"], {}).get("aliases", []),
                        "status": "updated" if obj["id"] in after_by_id else "removed"}
                       for obj in objects if obj["kind"] == "column" and obj != after_by_id.get(obj["id"])]
            events.append({"title": "Source withdrawal preview · " + source["history_id"],
                           "event_type": "source_withdrawal_preview_on_copy", "method": "dependency_update.update_layer",
                           "source": "Review event: withdraw this archived SQL source on a copied ontology",
                           "model_calls": 0, "receipt": receipt, "column_changes": changes,
                           "source_sql": source["sql"], "source_id": source["history_id"]})
        data = {"database": context, "provenance": provenance,
                "ontology": {"revision": layer.revision,
                             "sources": [{"evidence_id": "sql_log::" + key, **row} for key, row in records.items()],
                             "objects": objects, "tables": tables,
                             "recovery": [row for row in recovery if row["input_id"] in {r["input_id"] for r in tables}],
                             "edges": [edge.as_dict() for edge in ontology.edges],
                             "construct": [row for row in constructs if row["schema_context"] == context]},
                "maintenance": events,
                "cases": [row for row in catalog if row["database"] == context]}
        dump(ROOT / "dist/data" / (context + ".json"), data)
        databases.append({"id": context, "path": "data/" + context + ".json", "sources": len(records),
                          "objects": len(objects), "columns": sum(len(row["columns"]) for row in tables), "cases": data["cases"]})
    dump(ROOT / "dist/data/catalog.json", {"format": "sr-demo-catalog-v1", "cases": catalog, "databases": databases, "provenance": provenance})
    dump(ROOT / "dist/data/construct-district.json", constructs[1])
    dump(ROOT / "dist/data/manifest.json", provenance)
    print(json.dumps({"cases": len(catalog), "sources": [r["source_count"] for r in catalog], "output": str(ROOT / "dist/data")}))


if __name__ == "__main__":
    main()
