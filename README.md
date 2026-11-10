# Schema Recovery

## Dataset preprocessing

Use Python 3.13 on Linux:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e . --no-deps
# Local BGE-M3 encoding:
pip install -r requirements-retrieval.txt
# BEAVER MySQL tools:
pip install -r requirements-mysql.txt
```

The equivalent Conda environment is `conda env create -f environment.yml`.

Extract the recovered BIRD-History ontology:

```bash
python scripts/preprocess.py ontology --output data
```

This writes `data/ontology/{table_inputs.jsonl,table_recovery.jsonl,semantic_memory.json}`,
`data/ontology/semantic_layer/state.json`, and the joint interpretation records in
`data/ontology/construct/`. File checksums are in `assets/manifest.json`.

Construct the SQL-only BIRD-History semantic layer from the prepared 1,534-record history:

```bash
python scripts/native.py bird-ontology \
  --history /path/to/bird-history/history_sql_only.jsonl \
  --output-root data/bird-history-ontology
```

Prepare BIRD Dev or Mini-Dev catalogs and question records using the corresponding
split JSON and schema files:

```bash
python scripts/native.py bird-prepare \
  --dev-source /path/to/bird/dev.json \
  --dev-schemas /path/to/bird/dev_tables.json \
  --database-root /path/to/bird/dev_databases \
  --output data/bird-dev
```

Prepare the released KaggleDBQA test partition and Spider2 online manifests:

```bash
python scripts/preprocess.py manifests --dataset kaggledbqa \
  --source /path/to/KaggleDBQA --output data/kaggledbqa
python scripts/preprocess.py manifests --dataset spider2 \
  --source /path/to/Spider2 --output data/spider2
```

FIBEN: extract the upstream CSV archive into `data/fiben/data/`, then run:

```bash
python scripts/native.py fiben-prepare prepare \
  --source /path/to/fiben-benchmark --output data/fiben
```

EvoSchema and BEAVER physical snapshot conversion:

```bash
python scripts/native.py evoschema-snapshot \
  --online /path/to/evoschema/online.jsonl \
  --runtime /path/to/evoschema/runtime.jsonl \
  --repo-root /path/to/source-data --output-root data/evoschema
python scripts/native.py beaver-snapshot \
  --mysql-host 127.0.0.1 --mysql-port 3306 --mysql-user root \
  --output-root data/beaver
```

Set `BEAVER_MYSQL_PASSWORD` in the environment for the BEAVER conversion and runner.
The `fiben-ontology`, `kaggledbqa-inputs`, `kaggledbqa-ontology`, and `drspider-inputs`
entries expose the native recovery input builders; use `python scripts/native.py ENTRY --help`
for their input arguments.

## Dataset paths

| Dataset | Input layout | Native loader / entry |
|---|---|---|
| BIRD-History | Prepared `online.jsonl`; matching masked `dev_tables.json` and `dev_databases/<db>/<db>.sqlite`; `data/ontology/`; program-graph and raw drafts | `sqlite --dataset-id bird` |
| BIRD Dev | Split `online.jsonl`, `dev_tables.json`, `dev_databases/<db>/<db>.sqlite`, recovered table inputs | `sqlite --dataset-id bird` |
| BIRD Mini-Dev | Mini split `online.jsonl`, matching tables and SQLite databases, recovered table inputs | `sqlite --dataset-id bird` |
| KaggleDBQA | `examples/`, `KaggleDBQA_tables.json`, `databases/`; generated `online.jsonl` and recovered table inputs | `sqlite --dataset-id kaggledbqa` |
| FIBEN | Prepared `fiben.sqlite`, `questions.jsonl`, `catalog.jsonl`; online manifest and ontology | `sqlite --dataset-id fiben` |
| EvoSchema | `online.jsonl`, `runtime.jsonl`, source BIRD databases below `data/processed/bird_full_dev/dev_databases/` | `evoschema` / `evoschema-snapshot` |
| BEAVER | Online manifest, recovered table inputs and knowledge JSONL; MySQL databases `dw`, `nova`, `neutron` | `beaver` / `beaver-snapshot` |
| Spider2 | `spider2-lite/spider2-lite.jsonl`, `spider2-lite/resource/databases/`; prepared manifest and direct/recovery drafts | `spider2` / `spider2-react` |

For SQLite manifests, `database_or_answer_target` points to the database file or
its parent directory, and `schema_manifest` points to the physical schema JSON.
Relative resource paths in each row resolve against `--data-root`.

Copy `configs/paths.example.json` to `configs/paths.json` and set the dataset,
online manifest, ontology, model, draft, and output paths. Relative paths in this
configuration resolve against the repository root.

```bash
cp configs/paths.example.json configs/paths.json
python scripts/run_v17.py --paths configs/paths.json --print-command
python scripts/run_v17.py --paths configs/paths.json
```

The v17 r05 entry uses 4 turns, 8 actions, 3 SQL executions, and 6,144 maximum
output tokens. `--resume` continues from the configured output directory.
Additional native dataset arguments are available through:

```bash
python scripts/native.py sqlite --help
python scripts/native.py beaver --help
python scripts/native.py evoschema --help
python scripts/native.py spider2 --help
```

## Model paths

| Role | Checkpoint / served name | Configuration |
|---|---|---|
| Generation | `Qwen3.8-27B-FP8` / `qwen3.8-27b-fp8` | `SCHEMARECOVERY_LLM_MODEL_PATH`, `SCHEMARECOVERY_LLM_MODEL`, `SCHEMARECOVERY_LLM_BASE_URL` |
| Embedding | `BAAI/bge-m3` | `embedding_model` in `configs/paths.json` |
| Reranking | `BAAI/bge-reranker-v2-m3` / `bge-reranker-v2-m3` | `reranker_base_url` in `configs/paths.json` |

Generation uses an OpenAI-compatible endpoint. Set `SCHEMARECOVERY_LLM_API_KEY`
in the environment when the endpoint requires authentication. `.env.example`
lists the available environment settings. Generation settings are in
`configs/v17.yaml`; vLLM 0.30.0 serving dependencies are in
`requirements-vllm.txt` for a separate environment.

`embedding_model` is the local BGE-M3 checkpoint directory. `embedding_cache`
is generated at the configured path. An existing BGE endpoint can be selected
through `SCHEMARECOVERY_EMBEDDING_BASE_URL` and
`SCHEMARECOVERY_EMBEDDING_MODEL=bge-m3`.

## Code tree

```text
assets/
  ontology-v17-r05.tar.gz       Recovered ontology and semantic memory
  manifest.json                Ontology file checksums
configs/
  paths.example.json           Dataset and resource paths
  v17.yaml                     Generation configuration
scripts/
  preprocess.py                Ontology extraction and dataset manifests
  run_v17.py                   Path-configured native v17 entry
  native.py                    Native dataset and preprocessing entry points
infra/
  run_ontology_react.py         SQLite v17 pipeline
  run_beaver_full.py            MySQL tools and BEAVER pipeline
  run_evoschema_main.py         Evolution-aware schema pipeline
  run_spider2_*.py              Spider2 tools and pipeline
  materialize_*.py              Dataset and recovery input preparation
src/finsemguard/
  agent/                       Model client
  data/                        BIRD and FIBEN preparation
  schema_recovery/             Joint interpretation and recovery
  ontology_discovery/          Workload semantics and dependency updates
  e2e/                         Retrieval, contracts, compilation and SQL tools
  retrieval/                   Reranker client
source_manifest.json           Native source file checksums
requirements*.txt              Runtime and optional environments
environment.yml               Conda environment
pyproject.toml                Python package
```
