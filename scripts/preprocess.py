#!/usr/bin/env python3
"""Extract the released ontology or prepare one dataset's native manifests."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sys
import tarfile

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))

def restore_ontology(output: Path) -> None:
    manifest = json.loads((ROOT / "assets/manifest.json").read_text())
    archive = ROOT / "assets" / manifest["archive"]
    if hashlib.sha256(archive.read_bytes()).hexdigest() != manifest["archive_sha256"]:
        raise ValueError("ontology archive checksum mismatch")
    expected = {entry["path"]: entry for entry in manifest["files"]}
    with tarfile.open(archive) as tar:
        if set(tar.getnames()) != set(expected):
            raise ValueError("ontology archive member mismatch")
        for member in tar.getmembers():
            entry = expected[member.name]
            if not member.isfile() or Path(member.name).is_absolute() or ".." in Path(member.name).parts:
                raise ValueError("invalid ontology member")
            data = tar.extractfile(member).read()
            if len(data) != entry["bytes"] or hashlib.sha256(data).hexdigest() != entry["sha256"]:
                raise ValueError(f"ontology checksum mismatch: {member.name}")
            destination = output / member.name
            if destination.exists() and destination.read_bytes() != data:
                raise FileExistsError(destination)
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(data)
    print(json.dumps({"ontology": str((output / "ontology").resolve()), "files": len(expected)}))

def prepare_manifests(dataset: str, source: Path, output: Path) -> None:
    from finsemguard.e2e import adapters
    loaders = {"kaggledbqa": adapters._kaggledbqa, "dr_spider": adapters._dr_spider, "spider2": adapters._spider2}
    online, evaluator = loaders[dataset](source.resolve())
    ids = [row.example_id for row in online]
    if ids != [row.example_id for row in evaluator] or len(ids) != len(set(ids)):
        raise ValueError("manifest ID mismatch")
    if dataset == "kaggledbqa":
        selected = {row.example_id for row in online if row.upstream_split == "test"}
        online = [row for row in online if row.example_id in selected]
        evaluator = [row for row in evaluator if row.example_id in selected]
    adapters.write_jsonl(output / "online.jsonl", online)
    adapters.write_jsonl(output / "evaluator_only.jsonl", evaluator)
    print(json.dumps({"dataset": dataset, "rows": len(online), "output": str(output.resolve())}))

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="action", required=True)
    ontology = sub.add_parser("ontology")
    ontology.add_argument("--output", type=Path, default=ROOT / "data")
    manifests = sub.add_parser("manifests")
    manifests.add_argument("--dataset", choices=["kaggledbqa", "dr_spider", "spider2"], required=True)
    manifests.add_argument("--source", type=Path, required=True)
    manifests.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    if args.action == "ontology":
        restore_ontology(args.output)
    else:
        prepare_manifests(args.dataset, args.source, args.output)

if __name__ == "__main__":
    main()
