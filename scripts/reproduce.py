#!/usr/bin/env python3
"""Prepare the released masked BIRD inputs, run native stages, and score SQL."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tarfile

import yaml

from preprocess import restore_ontology
from run_v17 import build_command

ROOT = Path(__file__).resolve().parents[1]


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def resolve(value: str | Path) -> Path:
    path = Path(value).expanduser()
    return path.resolve() if path.is_absolute() else (ROOT / path).resolve()


def write_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n")


def read_rows(path: Path) -> list[dict]:
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def extract_package(archive: Path, destination: Path, package: str) -> None:
    receipt_path = ROOT / "assets/databases" / f"{package}.receipt.json"
    receipt = json.loads(receipt_path.read_text())
    if archive.stat().st_size != receipt["size_bytes"] or sha256(archive) != receipt["sha256"]:
        raise ValueError(f"archive checksum mismatch: {archive}")
    destination.mkdir(parents=True, exist_ok=True)
    with tarfile.open(archive) as source:
        for member in source:
            target = (destination / member.name).resolve()
            if not target.is_relative_to(destination.resolve()) or not member.name.startswith(package + "/"):
                raise ValueError(f"invalid archive path: {member.name}")
            if member.isdir():
                target.mkdir(parents=True, exist_ok=True)
                continue
            if not member.isfile():
                raise ValueError(f"invalid archive member: {member.name}")
            if target.exists():
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            temporary = target.with_name(target.name + ".extracting")
            with source.extractfile(member) as stream, temporary.open("wb") as output:
                shutil.copyfileobj(stream, output)
            temporary.replace(target)


def verify_package(folder: Path, package: str) -> dict:
    manifest = json.loads((folder / "PACKAGE_MANIFEST.json").read_text())
    reference = json.loads((ROOT / "assets/databases" / f"{package}.manifest.json").read_text())
    if manifest != reference:
        raise ValueError(f"package manifest differs from release: {package}")
    for entry in [*manifest.get("files", []), *manifest.get("generated_files", [])]:
        target = (folder / entry["archive_path"]).resolve()
        if not target.is_relative_to(folder.resolve()):
            raise ValueError(f"invalid package path: {target}")
        expected_size = entry.get("size_bytes", entry.get("bytes"))
        if not target.is_file() or (expected_size is not None and target.stat().st_size != expected_size):
            raise ValueError(f"missing or mismatched package file: {target}")
        if sha256(target) != entry["sha256"]:
            raise ValueError(f"package file checksum mismatch: {target}")
    return manifest


def relocate_online(package: Path, destination: Path) -> list[dict]:
    rows = read_rows(package / "model_input/bird_history_online.jsonl")
    ids = [str(row["example_id"]) for row in rows]
    if len(rows) != 1393 or len(ids) != len(set(ids)):
        raise ValueError("BIRD-History requires the released 1393 unique example IDs")
    for row in rows:
        db = str(row["database_id"])
        database = package / f"data/processed/bird_full_dev/dev_databases/{db}/{db}.sqlite"
        if not database.is_file() or not database.resolve().is_relative_to(package.resolve()):
            raise FileNotFoundError(database)
        row["database_or_answer_target"] = str(database.relative_to(package))
        row["schema_manifest"] = str((package / "model_input/masked_schema.json").resolve())
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text("".join(json.dumps(row, ensure_ascii=False) + "\n" for row in rows))
    return rows


def check_drafts(path: Path, ids: set[str]) -> None:
    rows = read_rows(path)
    found = [str(row["example_id"]) for row in rows]
    if len(found) != len(set(found)) or set(found) != ids:
        raise ValueError(f"draft coverage mismatch: {path}")
    if any(not str(row.get("sql") or "").strip() for row in rows):
        raise ValueError(f"draft contains empty SQL: {path}")


def stage_commands(config: dict, package: Path, intermediates: Path, work: Path, online: Path,
                   population: int, stages: str, resume: bool,
                   score_timeout_seconds: float | None = None) -> list[tuple[str, list[str]]]:
    llm = yaml.safe_load((ROOT / "configs/v17.yaml").read_text())
    llm["llm"]["api_key"] = ""
    for source_key, target_key in (("llm_base_url", "base_url"), ("model", "model")):
        if config.get(source_key):
            llm["llm"][target_key] = config[source_key]
    llm["llm"]["max_output_tokens"] = 6144
    main_config = work / "inputs/main.yaml"
    main_config.write_text(yaml.safe_dump(llm, sort_keys=False))
    llm["llm"]["max_output_tokens"] = 2048
    draft_config = work / "inputs/drafts.yaml"
    draft_config.write_text(yaml.safe_dump(llm, sort_keys=False))
    native = [sys.executable, str(ROOT / "scripts/native.py")]
    raw = intermediates / "bird_history/raw.jsonl"
    anchor = intermediates / "bird_history/anchor.jsonl"
    if stages == "score" and (work / "raw/predictions.jsonl").is_file():
        raw = work / "raw/predictions.jsonl"
    commands = []
    if stages == "fresh-drafts":
        raw = work / "raw/predictions.jsonl"
        anchor = work / "anchor/program_graph_react.jsonl"
        commands.append(("Raw", [*native, "raw", "--dataset", "bird", "--online", str(online),
            "--data-root", str(package), "--config", str(draft_config), "--output-root", str(work / "raw"),
            "--concurrency", "12", "--lean", "--retry-invalid-sql"]))
        original = intermediates / "bird_history/anchor_ontology"
        commands.append(("Anchor", [*native, "sqlite", "--dataset-id", "bird", "--online", str(online),
            "--data-root", str(package), "--table-inputs", str(original / "table_inputs.jsonl"),
            "--recovery", str(original / "table_recovery.jsonl"), "--workload-semantic-state", str(original / "semantic_layer/state.json"),
            "--embedding-model", str(resolve(config["embedding_model"])), "--embedding-cache", str(work / "cache/anchor.npz"),
            "--embedding-batch-size", "16", "--config", str(draft_config), "--subset-size", str(population),
            "--concurrency", "16", "--max-turns", "4", "--max-actions", "8", "--max-sql-executions", "3",
            "--lean", "--output-root", str(work / "anchor"), "--condition", "program_graph_react"]))
    if stages != "score":
        ontology = work / "inputs/ontology"
        main = dict(dataset_id="bird", data_root=str(package), online=str(online),
            table_inputs=str(ontology / "table_inputs.jsonl"), recovery=str(ontology / "table_recovery.jsonl"),
            workload_semantic_state=str(ontology / "semantic_layer/state.json"), semantic_memory=str(ontology / "semantic_memory.json"),
            anchor_predictions=str(anchor), auxiliary_raw_predictions=str(raw),
            embedding_model=str(resolve(config["embedding_model"])), embedding_cache=str(work / "cache/main.npz"),
            config=str(main_config), output_root=str(work / "main"), subset_size=population,
            concurrency=config.get("concurrency", 8), reranker_base_url=config["reranker_base_url"])
        commands.append(("Main", build_command(main)))
    if resume:
        for _, command in commands:
            command.append("--resume")
    score = [sys.executable, str(ROOT / "scripts/score_bird.py"), "--data-root", str(package), "--online", str(online),
        "--evaluator", str(package / "evaluator_only/bird_history_gold.jsonl"),
        "--prediction", f"raw_draft={raw}", "--prediction", f"main={work / 'main/graph_evo_semantic_program_main_v1.jsonl'}",
        "--baseline-label", "raw_draft", "--method-label", "main", "--output-root", str(work / "scores"),
        "--workers", "8", "--lean"]
    if score_timeout_seconds is not None:
        score += ["--timeout-seconds", str(score_timeout_seconds)]
    commands.append(("Score", score))
    return commands


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dataset", choices=["bird-history"], required=True)
    parser.add_argument("--data-root", type=Path, required=True)
    parser.add_argument("--data-archive", type=Path)
    parser.add_argument("--paths", type=Path, required=True)
    parser.add_argument("--intermediates-root", type=Path)
    parser.add_argument("--output-root", type=Path)
    parser.add_argument("--stages", choices=["main", "fresh-drafts", "score"], default="main")
    parser.add_argument("--score-timeout-seconds", type=float,
                        help="Optional scoring SQL deadline; default matches the frozen no-deadline run")
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if args.score_timeout_seconds is not None and args.score_timeout_seconds <= 0:
        parser.error("--score-timeout-seconds must be positive")
    config = json.loads(args.paths.read_text())
    if not config.get("embedding_model") or not config.get("reranker_base_url"):
        raise ValueError("paths configuration requires embedding_model and reranker_base_url")
    work = resolve(args.output_root or config.get("output_root", "outputs/bird-history"))
    (work / "inputs").mkdir(parents=True, exist_ok=True)
    data_root = args.data_root.expanduser().resolve()
    if args.data_archive:
        extract_package(args.data_archive.resolve(), data_root, "bird_masked")
    package = data_root / "bird_masked" if (data_root / "bird_masked").is_dir() else data_root
    verify_package(package, "bird_masked")
    if args.intermediates_root:
        intermediates = args.intermediates_root.expanduser().resolve()
        if (intermediates / "intermediates_masked").is_dir():
            intermediates /= "intermediates_masked"
    else:
        extract_package(ROOT / "assets/databases/intermediates_masked.tar.gz", work / "inputs", "intermediates_masked")
        intermediates = work / "inputs/intermediates_masked"
    verify_package(intermediates, "intermediates_masked")
    restore_ontology(work / "inputs")
    online = work / "inputs/online.jsonl"
    rows = relocate_online(package, online)
    ids = {str(row["example_id"]) for row in rows}
    if {str(row["example_id"]) for row in read_rows(package / "evaluator_only/bird_history_gold.jsonl")} != ids:
        raise ValueError("BIRD-History scoring IDs differ from online IDs")
    if args.stages == "main":
        for draft in ["raw.jsonl", "anchor.jsonl"]:
            check_drafts(intermediates / "bird_history" / draft, ids)
    commands = stage_commands(config, package, intermediates, work, online, len(rows), args.stages,
                              args.resume, args.score_timeout_seconds)
    write_json(work / "COMMANDS.json", {label: command for label, command in commands})
    if args.dry_run:
        print(json.dumps({label: command for label, command in commands}, indent=2))
        return
    if args.stages != "score" and not resolve(config["embedding_model"]).is_dir():
        raise FileNotFoundError(resolve(config["embedding_model"]))
    environment = os.environ.copy()
    environment["PYTHONPATH"] = str(ROOT / "src") + os.pathsep + environment.get("PYTHONPATH", "")
    for label, command in commands:
        print(f"[{label}]", flush=True)
        subprocess.run(command, check=True, cwd=ROOT, env=environment)
    print(f"Scores: {work / 'scores/SUMMARY.json'}")


if __name__ == "__main__":
    main()
