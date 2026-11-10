from __future__ import annotations

import os
from pathlib import Path
from typing import Any

import yaml


PROJECT_ROOT = Path(__file__).resolve().parents[2]
ENV_OVERRIDES = {
    "SCHEMARECOVERY_LLM_BASE_URL": ("llm", "base_url"),
    "SCHEMARECOVERY_LLM_API_KEY": ("llm", "api_key"),
    "SCHEMARECOVERY_LLM_MODEL": ("llm", "model"),
    "SCHEMARECOVERY_LLM_MODEL_PATH": ("llm", "model_path"),
    "SCHEMARECOVERY_LLM_AUDIT_LOG": ("llm", "audit_log_path"),
    "SCHEMARECOVERY_BGE_M3_PATH": ("retrieval", "bge_m3_path"),
    "SCHEMARECOVERY_RERANKER_PATH": ("retrieval", "reranker_path"),
    "SCHEMARECOVERY_BIRD_DATABASE_ROOT": ("paths", "bird_dev_databases"),
}


def load_config(path: str | Path | None = None) -> dict[str, Any]:
    config_path = Path(path) if path else PROJECT_ROOT / "configs" / "base.yaml"
    if not config_path.is_absolute():
        config_path = PROJECT_ROOT / config_path
    data = yaml.safe_load(config_path.read_text(encoding="utf-8"))
    for environment_name, (section, key) in ENV_OVERRIDES.items():
        if value := os.environ.get(environment_name):
            data.setdefault(section, {})[key] = value
    return data


def project_path(value: str | Path) -> Path:
    path = Path(value)
    return path if path.is_absolute() else PROJECT_ROOT / path
