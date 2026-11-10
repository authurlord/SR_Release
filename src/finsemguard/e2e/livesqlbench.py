from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any


CREATE_TABLE_RE = re.compile(
    r'"?CREATE"?\s+TABLE\s+"?([^"\s(]+)"?\s*\((.*?)\)\s*;',
    re.IGNORECASE | re.DOTALL,
)


@dataclass(frozen=True)
class CatalogDocument:
    candidate_id: str
    database_id: str
    kind: str
    table: str | None
    name: str
    text: str
    references: tuple[str, ...] = ()

    def retrieval_text(self) -> str:
        return f"{self.name}\n{self.text}"

    def compact_text(self) -> str:
        return f"[{self.candidate_id}] {self.kind} {self.name}\n{self.text}"


def parse_schema_tables(database_id: str, text: str) -> list[CatalogDocument]:
    output = []
    for match in CREATE_TABLE_RE.finditer(text):
        table = match.group(1)
        body = match.group(2).strip()
        # Several official Base-Full schema manifests intentionally quote SQL
        # keywords as noisy identifiers. The PostgreSQL dumps use ordinary
        # constraints, so normalize only these keyword spellings in context.
        body = re.sub(r'"(PRIMARY|FOREIGN)"\s+KEY', r'\1 KEY', body, flags=re.I)
        ddl = f'CREATE TABLE "{table}" (\n{body}\n);'
        references = tuple(
            dict.fromkeys(
                re.findall(
                    r'REFERENCES\s+"?([^"\s(]+)"?', body, flags=re.IGNORECASE
                )
            )
        )
        output.append(
            CatalogDocument(
                candidate_id=f"table::{database_id}::{table}",
                database_id=database_id,
                kind="table",
                table=table,
                name=table,
                text=ddl,
                references=references,
            )
        )
    return output


def load_catalog(root: Path) -> list[CatalogDocument]:
    output: list[CatalogDocument] = []
    for schema_path in sorted(root.glob("*/*_schema.txt")):
        database_id = schema_path.parent.name
        output.extend(
            parse_schema_tables(database_id, schema_path.read_text(encoding="utf-8"))
        )
        meaning_path = schema_path.parent / f"{database_id}_column_meaning_base.json"
        meanings = json.loads(meaning_path.read_text(encoding="utf-8"))
        for raw_id, description in meanings.items():
            parts = str(raw_id).split("|", 2)
            if len(parts) != 3:
                raise ValueError(f"invalid LiveSQLBench column ID: {raw_id}")
            _, table, column = parts
            output.append(
                CatalogDocument(
                    candidate_id=f"column::{database_id}::{table}::{column}",
                    database_id=database_id,
                    kind="column",
                    table=table,
                    name=f"{table}.{column}",
                    text=str(description),
                )
            )
        kb_path = schema_path.parent / f"{database_id}_kb.jsonl"
        with kb_path.open(encoding="utf-8") as handle:
            for line in handle:
                if not line.strip():
                    continue
                row: dict[str, Any] = json.loads(line)
                knowledge_id = str(row.get("id", len(output)))
                name = str(row.get("knowledge", knowledge_id))
                fields = [
                    str(row[key])
                    for key in ("description", "definition")
                    if row.get(key)
                ]
                output.append(
                    CatalogDocument(
                        candidate_id=f"knowledge::{database_id}::{knowledge_id}",
                        database_id=database_id,
                        kind="knowledge",
                        table=None,
                        name=name,
                        text="\n".join(fields),
                    )
                )
    if not output:
        raise ValueError(f"no LiveSQLBench catalog documents found under {root}")
    return output


def evidence_closure(
    selected_ids: list[str],
    candidates: list[CatalogDocument],
    all_documents: dict[str, CatalogDocument],
) -> list[CatalogDocument]:
    selected = {candidate_id for candidate_id in selected_ids if candidate_id in all_documents}
    table_ids = []
    for candidate_id in list(selected):
        document = all_documents[candidate_id]
        if document.table:
            table_id = f"table::{document.database_id}::{document.table}"
            if table_id in all_documents and table_id not in selected:
                selected.add(table_id)
            if table_id in all_documents:
                table_ids.append(table_id)
    while table_ids:
        table_id = table_ids.pop()
        document = all_documents[table_id]
        for reference in document.references:
            reference_id = f"table::{document.database_id}::{reference}"
            if reference_id in all_documents and reference_id not in selected:
                selected.add(reference_id)
                table_ids.append(reference_id)
    order = {document.candidate_id: index for index, document in enumerate(candidates)}
    return sorted(
        (all_documents[candidate_id] for candidate_id in selected),
        key=lambda document: (order.get(document.candidate_id, 10**9), document.candidate_id),
    )
