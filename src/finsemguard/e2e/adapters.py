from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Iterable

from finsemguard.e2e.contracts import DataAgentRecord, EvaluatorTarget
from finsemguard.e2e.preflight import DR_SPIDER_SETS


def _json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def _jsonl(path: Path) -> list[dict[str, Any]]:
    with path.open(encoding="utf-8") as handle:
        return [json.loads(line) for line in handle if line.strip()]


def _relative(path: Path, root: Path) -> str:
    return str(path.resolve().relative_to(root.resolve()))


def _live_sql_bench(root: Path) -> tuple[list[DataAgentRecord], list[EvaluatorTarget]]:
    rows = _jsonl(root / "livesqlbench_data.jsonl")
    online = []
    evaluator = []
    for row in rows:
        db_id = str(row["selected_database"])
        db_root = root / db_id
        instance_id = str(row["instance_id"])
        docs = sorted(
            _relative(path, root)
            for path in db_root.iterdir()
            if path.is_file() and ("meaning" in path.name or "kb" in path.name)
        )
        schema = db_root / f"{db_id}_schema.txt"
        online.append(
            DataAgentRecord(
                example_id=instance_id,
                dataset_id="livesqlbench_base_full_v1",
                upstream_split="full_release_normal_questions",
                database_id=db_id,
                question=str(row["normal_query"]),
                allowed_docs=docs,
                schema_manifest=_relative(schema, root),
                database_or_answer_target=f"postgresql://127.0.0.1:55432/{db_id}",
                evaluator_id="livesqlbench_official_test_cases",
                evaluator_version="e15cd221267e06fabfaf6a3d4a69308280ce9a7c",
            )
        )
        evaluator.append(
            EvaluatorTarget(
                example_id=instance_id,
                dataset_id="livesqlbench_base_full_v1",
                gold={
                    "sol_sql": row.get("sol_sql"),
                    "test_cases": row.get("test_cases", []),
                    "conditions": row.get("conditions", {}),
                    "preprocess_sql": row.get("preprocess_sql", []),
                    "clean_up_sqls": row.get("clean_up_sqls", []),
                    "category": row.get("category", "Query"),
                },
            )
        )
    return online, evaluator


def _spider2(root: Path) -> tuple[list[DataAgentRecord], list[EvaluatorTarget]]:
    lite = root / "spider2-lite"
    rows = _jsonl(lite / "spider2-lite.jsonl")
    online = []
    evaluator = []
    for row in rows:
        instance_id = str(row["instance_id"])
        db_id = str(row["db"])
        docs = []
        external = row.get("external_knowledge")
        if isinstance(external, list):
            docs = [str(item) for item in external]
        elif external:
            docs = [str(external)]
        online.append(
            DataAgentRecord(
                example_id=instance_id,
                dataset_id="spider2_lite",
                upstream_split="full_release",
                database_id=db_id,
                question=str(row["question"]),
                allowed_docs=docs,
                schema_manifest="spider2-lite/resource/databases",
                database_or_answer_target=f"spider2://{instance_id}/{db_id}",
                evaluator_id="spider2_lite_self_evaluation",
                evaluator_version="01a4c67c1e3f6ab9032716b050a927abbb245f65",
            )
        )
        evaluator.append(
            EvaluatorTarget(
                example_id=instance_id,
                dataset_id="spider2_lite",
                gold={"official_exec_result_id": instance_id},
            )
        )
    return online, evaluator


def _dr_spider(root: Path) -> tuple[list[DataAgentRecord], list[EvaluatorTarget]]:
    data = root / "data"
    online = []
    evaluator = []
    for test_set in DR_SPIDER_SETS:
        folder = data / test_set
        rows = _json(folder / "questions_post_perturbation.json")
        gold_lines = (folder / "gold_post_perturbation.sql").read_text(
            encoding="utf-8"
        ).splitlines()
        if len(rows) != len(gold_lines):
            raise ValueError(f"Dr.Spider gold/question mismatch: {test_set}")
        db_perturbation = test_set.startswith("DB_")
        schema = (
            folder / "tables_post_perturbation.json"
            if db_perturbation
            else data / "Spider-dev" / "tables.json"
        )
        for index, (row, gold_line) in enumerate(zip(rows, gold_lines, strict=True)):
            db_id = str(row["db_id"])
            example_id = f"{test_set}:{index:05d}"
            db_root = (
                folder / "database_post_perturbation"
                if db_perturbation
                else data / "Spider-dev" / "databases"
            )
            online.append(
                DataAgentRecord(
                    example_id=example_id,
                    dataset_id="dr_spider",
                    upstream_split=f"{test_set}:post_perturbation",
                    database_id=db_id,
                    question=str(row["question"]),
                    allowed_docs=[],
                    schema_manifest=_relative(schema, root),
                    database_or_answer_target=_relative(db_root / db_id, root),
                    evaluator_id="test_suite_sql_eval",
                    evaluator_version="e97acc546ecbee8fa27fa8dbf025ef61493a876c",
                )
            )
            evaluator.append(
                EvaluatorTarget(
                    example_id=example_id,
                    dataset_id="dr_spider",
                    gold={"gold_line": gold_line, "q_id_spider_dev": row.get("q_id_spider_dev")},
                )
            )
    return online, evaluator


def _kaggledbqa(root: Path) -> tuple[list[DataAgentRecord], list[EvaluatorTarget]]:
    examples = root / "examples"
    test_members = {
        (str(row["db_id"]), str(row["question"]), str(row["query"]))
        for path in examples.glob("*_test.json")
        for row in _json(path)
    }
    fewshot_members = {
        (str(row["db_id"]), str(row["question"]), str(row["query"]))
        for path in examples.glob("*_fewshot.json")
        for row in _json(path)
    }
    full_files = sorted(
        path
        for path in examples.glob("*.json")
        if not path.stem.endswith(("_test", "_fewshot"))
    )
    online = []
    evaluator = []
    for path in full_files:
        for index, row in enumerate(_json(path)):
            db_id = str(row["db_id"])
            key = (db_id, str(row["question"]), str(row["query"]))
            if key in test_members:
                split = "test"
            elif key in fewshot_members:
                split = "fewshot"
            else:
                raise ValueError(f"KaggleDBQA row has no released partition: {path}:{index}")
            example_id = f"{db_id}:{index:03d}"
            database = next((root / "databases").rglob(f"{db_id}.sqlite"))
            online.append(
                DataAgentRecord(
                    example_id=example_id,
                    dataset_id="kaggledbqa",
                    upstream_split=split,
                    database_id=db_id,
                    question=str(row["question"]),
                    allowed_docs=[],
                    schema_manifest="KaggleDBQA_tables.json",
                    database_or_answer_target=_relative(database, root),
                    evaluator_id="sqlite_execution_test_suite",
                    evaluator_version="e97acc546ecbee8fa27fa8dbf025ef61493a876c",
                )
            )
            evaluator.append(
                EvaluatorTarget(
                    example_id=example_id,
                    dataset_id="kaggledbqa",
                    gold={"sql": row["query"]},
                )
            )
    return online, evaluator


def _llmsql(root: Path) -> tuple[list[DataAgentRecord], list[EvaluatorTarget]]:
    rows = _jsonl(root / "test_questions.jsonl")
    online = []
    evaluator = []
    for row in rows:
        example_id = str(row["question_id"])
        table_id = str(row["table_id"])
        online.append(
            DataAgentRecord(
                example_id=example_id,
                dataset_id="llmsql",
                upstream_split="test",
                database_id=table_id,
                question=str(row["question"]),
                allowed_docs=[],
                schema_manifest="tables.jsonl",
                database_or_answer_target="sqlite_tables.db",
                evaluator_id="llmsql_official_execution",
                evaluator_version="5d55402a8508e53b038e0327d79ad2410ca33f1c",
            )
        )
        evaluator.append(
            EvaluatorTarget(
                example_id=example_id,
                dataset_id="llmsql",
                gold={"sql": row["sql"], "table_id": table_id},
            )
        )
    return online, evaluator


def load_all_adapters(
    dataset_root: Path, spider2_root: Path
) -> dict[str, tuple[list[DataAgentRecord], list[EvaluatorTarget]]]:
    return {
        "livesqlbench_base_full_v1": _live_sql_bench(dataset_root / "LiveSQLBench_data"),
        "spider2_lite": _spider2(spider2_root),
        "dr_spider": _dr_spider(dataset_root / "DrSpider"),
        "kaggledbqa": _kaggledbqa(dataset_root / "KaggleDBQA"),
        "llmsql": _llmsql(dataset_root / "LLMSQL_data"),
    }


def write_jsonl(path: Path, rows: Iterable[DataAgentRecord | EvaluatorTarget]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    with temporary.open("w", encoding="utf-8") as handle:
        for row in rows:
            handle.write(row.model_dump_json() + "\n")
    temporary.replace(path)
