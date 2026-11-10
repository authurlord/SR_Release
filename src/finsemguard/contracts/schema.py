from __future__ import annotations

from enum import StrEnum
from typing import Any, Literal

from pydantic import BaseModel, Field, field_validator


class AgentDecision(StrEnum):
    ANSWER = "answer"
    CLARIFY = "clarify"
    ABSTAIN = "abstain"


class EvidenceDocument(BaseModel):
    doc_id: str
    kind: Literal["table", "column", "query_pattern", "metric", "relationship"]
    dataset: str = "fiben"
    split_origin: str = "schema"
    name: str
    text: str
    table: str | None = None
    column: str | None = None
    metadata: dict[str, Any] = Field(default_factory=dict)


class SemanticPlan(BaseModel):
    intent: str
    measures: list[str] = Field(default_factory=list)
    dimensions: list[str] = Field(default_factory=list)
    filters: list[dict[str, Any]] = Field(default_factory=list)
    time_range: dict[str, Any] | None = None
    grain: list[str] = Field(default_factory=list)
    join_path: list[str] = Field(default_factory=list)
    evidence_ids: list[str] = Field(default_factory=list)
    assumptions: list[str] = Field(default_factory=list)
    missing_slots: list[str] = Field(default_factory=list)
    risk_flags: list[str] = Field(default_factory=list)

    @field_validator(
        "measures",
        "dimensions",
        "grain",
        "join_path",
        "evidence_ids",
        "assumptions",
        "missing_slots",
        "risk_flags",
        mode="before",
    )
    @classmethod
    def normalize_list_fields(cls, value: Any) -> list[Any]:
        if value is None:
            return []
        return value if isinstance(value, list) else [value]

    @field_validator("filters", mode="before")
    @classmethod
    def normalize_filters(cls, value: Any) -> list[dict[str, Any]]:
        if value is None:
            return []
        values = value if isinstance(value, list) else [value]
        return [item if isinstance(item, dict) else {"expression": str(item)} for item in values]

    @field_validator("time_range", mode="before")
    @classmethod
    def normalize_time_range(cls, value: Any) -> dict[str, Any] | None:
        if value is None or isinstance(value, dict):
            return value
        return {"description": str(value)}


class AgentTrace(BaseModel):
    question: str
    decision: AgentDecision
    retrieval: list[dict[str, Any]] = Field(default_factory=list)
    semantic_plan: SemanticPlan | None = None
    sql: str | None = None
    validator: dict[str, Any] = Field(default_factory=dict)
    preview: dict[str, Any] = Field(default_factory=dict)
    clarification: str | None = None
    answer: str | None = None
    model: str | None = None
