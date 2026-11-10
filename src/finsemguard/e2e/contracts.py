from __future__ import annotations

from typing import Any

from pydantic import BaseModel, ConfigDict, Field


class DataAgentRecord(BaseModel):
    """Gold-free record that may be consumed by an online Data Agent."""

    model_config = ConfigDict(extra="forbid")

    example_id: str
    dataset_id: str
    upstream_split: str
    database_id: str
    question: str
    allowed_docs: list[str] = Field(default_factory=list)
    schema_manifest: str
    database_or_answer_target: str
    evaluator_id: str
    evaluator_version: str


class EvaluatorTarget(BaseModel):
    """Evaluator-only fields, stored separately from online agent records."""

    model_config = ConfigDict(extra="forbid")

    example_id: str
    dataset_id: str
    gold: dict[str, Any]
