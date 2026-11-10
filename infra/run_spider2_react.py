#!/usr/bin/env python3
"""Spider 2.0-Lite M0-M4 Live LLM Generation Pipeline."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
import json
import os
from pathlib import Path
import sqlite3
import time
from typing import Any

import sqlglot

from finsemguard.agent.llm import VLLMClient
from finsemguard.e2e.livesqlbench_runner import _write_atomic


SYSTEM_PROMPT = """You are an expert SQL Data Agent specializing in complex real-world data warehouses (SQLite/DuckDB).
Your task is to generate precise, valid SQLite statements that accurately satisfy the business question based on the inspected schema and documentation.
Always return your final answer in a single JSON block."""

SPIDER2_PROMPT_TEMPLATE = """[Database ID]: {database_id}
[Question]: {question}

[Allowed Documentation & Business Rules]:
{allowed_docs}

[Inspected Physical Schema & Foreign Key Graph]:
{probe_context}

[Instructions]:
1. Carefully analyze the question requirements, metrics, and grouping dimensions.
2. Select the exact table and column names from the Inspected Physical Schema above.
3. When external business rules or definitions (e.g. RFM model, Haversine formula, CLV formulas) are provided, follow their exact segmentations, formulas, and conditions.
4. For date arithmetic, use SQLite DATE(...), STRFTIME(...), or JULIANDAY(...).
5. For ratios or percentages, use safe floating-point division CAST(... AS REAL) or multiplying by 1.0.
6. Output ONLY a valid JSON object:
   {{"decision": "answer", "sql": "SELECT ...", "explanation": "..."}}
"""


def _probe_sqlite_tables(sqlite_path: Path) -> str:
    """M0 dynamic probe: inspect all schemas, foreign keys, and distinct sample values."""
    if not sqlite_path.is_file():
        return ""
    
    probe_lines = ["[M0 Schema & Value Probe Insights]:"]
    try:
        conn = sqlite3.connect(f"file:{sqlite_path}?mode=ro", uri=True)
        cursor = conn.cursor()
        
        # Get all table names
        all_tables = [
            r[0] for r in cursor.execute(
                "SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%';"
            ).fetchall()
        ]
        
        for t in all_tables:
            cols = cursor.execute(f"PRAGMA table_info('{t}');").fetchall()
            col_specs = [f"{c[1]} ({c[2]})" for c in cols]
            
            # Foreign keys
            fks = cursor.execute(f"PRAGMA foreign_key_list('{t}');").fetchall()
            fk_strs = [f"{fk[3]} -> {fk[2]}.{fk[4]}" for fk in fks]
            fk_info = f" | Foreign Keys: {', '.join(fk_strs)}" if fk_strs else ""
            
            probe_lines.append(f"Table '{t}' [{', '.join(col_specs)}]{fk_info}")
            
            # Sample row
            try:
                sample_row = cursor.execute(f"SELECT * FROM '{t}' LIMIT 1;").fetchone()
                if sample_row:
                    samples = [f"{cols[i][1]}={repr(sample_row[i])[:25]}" for i in range(min(len(cols), 5))]
                    probe_lines.append(f"  Sample values: {', '.join(samples)}")
            except Exception:
                pass
        conn.close()
    except Exception as e:
        probe_lines.append(f"Probe notice: {e}")
        
    return "\n".join(probe_lines)


def process_spider2_question(
    row: dict[str, Any],
    spider2_root: Path,
    client: VLLMClient,
    local_map: dict[str, str],
    metadata_map: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    instance_id = row.get("example_id") or row.get("instance_id")
    meta = metadata_map.get(instance_id, {})
    question = row.get("question") or meta.get("question")
    
    # 1. Database identification from local_map or metadata
    db_name = local_map.get(instance_id) or meta.get("db") or row.get("database_id")
    
    # 2. External Knowledge & Allowed Documentation
    ext_doc = meta.get("external_knowledge") or row.get("external_knowledge")
    allowed_docs_text = ""
    if ext_doc:
        doc_path = spider2_root / "resource" / "documents" / ext_doc
        if doc_path.is_file():
            allowed_docs_text = f"\n--- {ext_doc} ---\n" + doc_path.read_text(encoding="utf-8", errors="replace")[:16000]
            
    if not allowed_docs_text:
        allowed_docs_text = "None provided."
        
    # 3. M0 Dynamic Probe on Local SQLite DB
    sqlite_base = spider2_root / "resource" / "databases" / "spider2-localdb"
    sqlite_path = sqlite_base / f"{db_name}.sqlite"
    if not sqlite_path.is_file():
        matches = list((spider2_root / "resource" / "databases").rglob(f"{db_name}.sqlite"))
        if matches:
            sqlite_path = matches[0]
            
    probe_context = _probe_sqlite_tables(sqlite_path)
    
    prompt = SPIDER2_PROMPT_TEMPLATE.format(
        database_id=db_name,
        question=question,
        allowed_docs=allowed_docs_text,
        probe_context=probe_context,
    )
    
    # 4. Live Multi-turn LLM Inference
    raw_response, _ = client.chat_text_with_metadata(
        system=SYSTEM_PROMPT,
        user=prompt,
    )
    
    # 5. Parse SQL
    pred_sql = ""
    decision = "answer"
    try:
        content = raw_response.strip()
        if "```json" in content:
            json_str = content.split("```json")[1].split("```")[0].strip()
            parsed = json.loads(json_str)
            pred_sql = parsed.get("sql") or ""
        elif "```sql" in content:
            pred_sql = content.split("```sql")[1].split("```")[0].strip()
        elif "{" in content and "}" in content:
            json_start = content.find("{")
            json_end = content.rfind("}") + 1
            parsed = json.loads(content[json_start:json_end])
            pred_sql = parsed.get("sql") or ""
        else:
            pred_sql = content
    except Exception:
        pred_sql = content
        
    clean_sql = pred_sql
    if pred_sql:
        try:
            parsed_expr = sqlglot.parse_one(pred_sql, read="sqlite")
            clean_sql = parsed_expr.sql(dialect="sqlite")
        except Exception:
            clean_sql = pred_sql.strip("`").strip()
            
    return {
        "example_id": instance_id,
        "instance_id": instance_id,
        "dataset_id": "spider2_lite",
        "database_id": db_name,
        "question": question,
        "raw_sql": pred_sql,
        "sql": clean_sql,
        "decision": decision,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--spider2-root", type=Path, default=Path("/data/workspace/yanmy/datasets/Spider2_official/spider2-lite"))
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--vllm-base-url", type=str, default="http://127.0.0.1:18000/v1")
    parser.add_argument("--model-name", type=str, default="qwen3.8-27b-fp8")
    parser.add_argument("--subset-size", type=int, default=None)
    parser.add_argument("--workers", type=int, default=8)
    args = parser.parse_args()
    
    # Load metadata
    metadata_map = {}
    meta_path = args.spider2_root / "spider2-lite.jsonl"
    if meta_path.is_file():
        with open(meta_path) as f:
            for line in f:
                if line.strip():
                    item = json.loads(line)
                    metadata_map[item["instance_id"]] = item
                    
    # Load manifest
    rows = []
    with open(args.manifest) as f:
        for line in f:
            if line.strip():
                rows.append(json.loads(line))
    if args.subset_size:
        rows = rows[:args.subset_size]
        
    print(f"Loaded {len(rows)} Spider 2.0-Lite instances to evaluate.")
    
    # Load local-map
    local_map_file = args.spider2_root / "resource" / "databases" / "spider2-localdb" / "local-map.jsonl"
    local_map = {}
    if local_map_file.is_file():
        with open(local_map_file) as f:
            local_map = json.loads(f.read())
            
    client = VLLMClient({
        "base_url": args.vllm_base_url,
        "api_key": "EMPTY",
        "model": args.model_name,
        "temperature": 0.0,
        "top_p": 1.0,
        "max_output_tokens": 2048,
        "request_timeout_seconds": 120.0,
        "compatibility": "vllm"
    })
    
    args.output.parent.mkdir(parents=True, exist_ok=True)
    results = []
    
    print(f"Starting live LLM generation with {args.workers} workers...")
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {
            pool.submit(
                process_spider2_question,
                row,
                args.spider2_root,
                client,
                local_map,
                metadata_map,
            ): (row.get("example_id") or row.get("instance_id"))
            for row in rows
        }
        for future in as_completed(futures):
            eid = futures[future]
            try:
                res = future.result()
                results.append(res)
                print(f"[{len(results)}/{len(rows)}] Completed {eid}: {res['sql'][:60]}...")
            except Exception as e:
                print(f"Error processing {eid}: {e}")
                results.append({
                    "example_id": eid,
                    "instance_id": eid,
                    "dataset_id": "spider2_lite",
                    "sql": "",
                    "decision": "error",
                    "error": str(e)
                })
                
    _write_atomic(args.output, results)
    print(f"SUCCESS! Written {len(results)} predictions to {args.output}")

if __name__ == "__main__":
    main()
