from __future__ import annotations

import math
from typing import Any

import httpx


class VLLMRerankerClient:
    """Fail-closed client for vLLM's native cross-encoder rerank endpoint."""

    def __init__(
        self,
        *,
        base_url: str,
        model: str = "bge-reranker-v2-m3",
        timeout_seconds: float = 120.0,
    ) -> None:
        normalized = base_url.rstrip("/")
        if normalized.endswith("/v1"):
            normalized = normalized[: -len("/v1")]
        if not normalized:
            raise ValueError("reranker base URL must not be empty")
        if not model.strip():
            raise ValueError("reranker model must not be empty")
        if timeout_seconds <= 0:
            raise ValueError("reranker timeout must be positive")
        self.base_url = normalized
        self.model = model.strip()
        self.timeout_seconds = float(timeout_seconds)

    def healthy(self) -> bool:
        try:
            response = httpx.get(
                f"{self.base_url}/v1/models",
                timeout=3.0,
                trust_env=False,
            )
            response.raise_for_status()
            payload = response.json()
        except (httpx.HTTPError, ValueError):
            return False
        served = {
            str(row.get("id") or "")
            for row in payload.get("data", [])
            if isinstance(row, dict)
        }
        return self.model in served

    def score(self, query: str, documents: list[str]) -> list[float]:
        if not documents:
            return []
        if not query.strip():
            raise ValueError("reranker query must not be empty")
        if any(not isinstance(document, str) or not document.strip() for document in documents):
            raise ValueError("reranker documents must be nonempty strings")
        response = httpx.post(
            f"{self.base_url}/rerank",
            json={
                "model": self.model,
                "query": query,
                "documents": documents,
                "top_n": len(documents),
            },
            timeout=self.timeout_seconds,
            trust_env=False,
        )
        response.raise_for_status()
        payload: dict[str, Any] = response.json()
        results = payload.get("results")
        if not isinstance(results, list) or len(results) != len(documents):
            raise RuntimeError("reranker returned an incomplete result set")
        scores: list[float | None] = [None] * len(documents)
        for result in results:
            if not isinstance(result, dict):
                raise RuntimeError("reranker result must be an object")
            index = result.get("index")
            score = result.get("relevance_score")
            if not isinstance(index, int) or not 0 <= index < len(documents):
                raise RuntimeError("reranker returned an invalid document index")
            if scores[index] is not None:
                raise RuntimeError("reranker returned a duplicate document index")
            if not isinstance(score, (int, float)) or not math.isfinite(float(score)):
                raise RuntimeError("reranker returned a non-finite score")
            scores[index] = float(score)
        if any(score is None for score in scores):
            raise RuntimeError("reranker omitted a document index")
        return [float(score) for score in scores]
