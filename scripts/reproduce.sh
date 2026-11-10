#!/usr/bin/env bash
set -euo pipefail
SR_REPO_ROOT="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/.." && pwd)"
export PYTHONPATH="${SR_REPO_ROOT}/src${PYTHONPATH:+:${PYTHONPATH}}"
exec "${SR_PYTHON:-python}" "${SR_REPO_ROOT}/scripts/reproduce.py" "$@"
