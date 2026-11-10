# SchemaRecovery: Building and Maintaining Database Semantic Layers from SQL Histories

[English](README.md) | [简体中文](README.zh-CN.md)

## 数据集

| 数据集 | 官方页面 |
|---|---|
| BIRD-History | [BIRD](https://bird-bench.github.io/) SQL 历史划分 |
| BIRD Dev | [BIRD](https://bird-bench.github.io/) |
| BIRD Mini-Dev | [BIRD Mini-Dev](https://github.com/bird-bench/mini_dev) |
| KaggleDBQA | [KaggleDBQA](https://github.com/Chia-Hsuan-Lee/KaggleDBQA) |
| FIBEN | [IBM FIBEN benchmark](https://github.com/IBM/fiben-benchmark) |
| EvoSchema | [EvoSchema](https://github.com/zhangtianshu/EvoSchema) |
| BEAVER | [BEAVER benchmark](https://beaverbench.github.io/) |
| Spider2 | [Spider 2.0](https://spider2-sql.github.io/) |

## 数据集预处理

使用 Linux 和 Python 3.13：

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pip install -e . --no-deps
# 本地 BGE-M3 编码：
pip install -r requirements-retrieval.txt
# BEAVER MySQL 工具：
pip install -r requirements-mysql.txt
```

Conda 环境：`conda env create -f environment.yml`。

数据包保存实验使用的实际屏蔽版本：

| 数据包 | 内容 | 字节数 | 位置 |
|---|---|---:|---|
| `bird_masked.tar.gz` | 11 个库及 BIRD-History、Dev、Mini-Dev 输入 | 386,516,161 | 夸克：`/quark/SchemaRecovery/SR_Release/databases/` |
| [kaggledbqa_masked.tar.gz](assets/databases/kaggledbqa_masked.tar.gz) | 8 个屏蔽库 | 99,210,635 | 仓库内 |
| `fiben_masked.tar.gz` | 1 个屏蔽库 | 202,146,216 | 夸克：`/quark/SchemaRecovery/SR_Release/databases/` |
| [intermediates_masked.tar.gz](assets/databases/intermediates_masked.tar.gz) | 上游 Raw/Anchor SQL 与构建输入 | 1,673,705 | 仓库内 |

文件清单和归档校验值见 [assets/databases](assets/databases)。

在路径配置中填写 BGE 模型目录、生成端点和重排序端点，然后复用保存的 Raw/Anchor SQL 与恢复的 ontology，运行 BIRD-History Main 和原生评分：

```bash
cp configs/reproduce.bird-history.example.json configs/bird-history.local.json
bash scripts/reproduce.sh --dataset bird-history \
  --data-root data/extracted --data-archive /path/to/bird_masked.tar.gz \
  --paths configs/bird-history.local.json
```

脚本校验归档和文件哈希，解包 ontology 与中间输入，重定位数据库及 schema 路径，然后运行 Main，并按冻结的无 SQL 时限协议调用原生 BIRD 评分器。`--score-timeout-seconds 120` 可指定 120 秒评分时限，结果写入 `outputs/bird-history/scores/SUMMARY.json`。

重新生成 Raw 和 Anchor，再运行 Main 与评分：

```bash
bash scripts/reproduce.sh --dataset bird-history --data-root data/extracted \
  --paths configs/bird-history.local.json --stages fresh-drafts \
  --output-root outputs/bird-history-fresh
```

`fresh-drafts` 分别使用包内原始 Anchor ontology 和 v17 Main ontology。Raw/Anchor/Main 的输出预算分别为 2,048/2,048/6,144 tokens；Anchor 与 Main 保持 4 turns、8 actions、3 次 SQL 执行。`--dry-run` 准备并校验输入、打印各阶段命令；`--resume` 接续生成；`--stages score` 对已有运行评分。可用 `SR_PYTHON` 指定 Python 解释器。

单独解包 BIRD-History ontology：

```bash
python scripts/preprocess.py ontology --output data
```

输出包括 `data/ontology/{table_inputs.jsonl,table_recovery.jsonl,semantic_memory.json}`、`data/ontology/semantic_layer/state.json` 和 `data/ontology/construct/` 下的联合解释记录，校验值见 `assets/manifest.json`。

从准备好的 1,534 条 SQL-only 历史构建 BIRD-History 语义层：

```bash
python scripts/native.py bird-ontology \
  --history /path/to/bird-history/history_sql_only.jsonl \
  --output-root data/bird-history-ontology
```

为 BIRD Dev 或 Mini-Dev 准备 catalog 与问题记录，传入对应划分的 JSON 和 schema 文件：

```bash
python scripts/native.py bird-prepare \
  --dev-source /path/to/bird/dev.json \
  --dev-schemas /path/to/bird/dev_tables.json \
  --database-root /path/to/bird/dev_databases \
  --output data/bird-dev
```

准备 KaggleDBQA 官方 test 划分和 Spider2 online 清单：

```bash
python scripts/preprocess.py manifests --dataset kaggledbqa \
  --source /path/to/KaggleDBQA --output data/kaggledbqa
python scripts/preprocess.py manifests --dataset spider2 \
  --source /path/to/Spider2 --output data/spider2
```

FIBEN：先把上游 CSV 归档解包到 `data/fiben/data/`，再运行：

```bash
python scripts/native.py fiben-prepare prepare \
  --source /path/to/fiben-benchmark --output data/fiben
```

EvoSchema 和 BEAVER 物理快照转换：

```bash
python scripts/native.py evoschema-snapshot \
  --online /path/to/evoschema/online.jsonl \
  --runtime /path/to/evoschema/runtime.jsonl \
  --repo-root /path/to/source-data --output-root data/evoschema
python scripts/native.py beaver-snapshot \
  --mysql-host 127.0.0.1 --mysql-port 3306 --mysql-user root \
  --output-root data/beaver
```

BEAVER 转换和运行器从环境变量 `BEAVER_MYSQL_PASSWORD` 读取密码。
`fiben-ontology`、`kaggledbqa-inputs`、`kaggledbqa-ontology` 和 `drspider-inputs` 提供原生恢复输入构建入口，可用 `python scripts/native.py ENTRY --help` 查看参数。

## 数据集路径

| 数据集 | 输入布局 | 原生加载器 / 入口 |
|---|---|---|
| BIRD-History | 准备好的 `online.jsonl`；匹配的屏蔽版 `dev_tables.json` and `dev_databases/<db>/<db>.sqlite`; `data/ontology/`; program-graph 与 Raw 草稿 | `sqlite --dataset-id bird` |
| BIRD Dev | 划分后的 `online.jsonl`, `dev_tables.json`, `dev_databases/<db>/<db>.sqlite`, 恢复的 table inputs | `sqlite --dataset-id bird` |
| BIRD Mini-Dev | Mini 划分 `online.jsonl`、匹配的 tables 和 SQLite 数据库, 恢复的 table inputs | `sqlite --dataset-id bird` |
| KaggleDBQA | `examples/`, `KaggleDBQA_tables.json`, `databases/`; 生成的 `online.jsonl` 与 恢复的 table inputs | `sqlite --dataset-id kaggledbqa` |
| FIBEN | 准备好的 `fiben.sqlite`, `questions.jsonl`, `catalog.jsonl`; online 清单和 ontology | `sqlite --dataset-id fiben` |
| EvoSchema | `online.jsonl`, `runtime.jsonl`, 原始 BIRD 数据库位于 `data/processed/bird_full_dev/dev_databases/` | `evoschema` / `evoschema-snapshot` |
| BEAVER | Online manifest, 恢复的 table inputs and knowledge JSONL; MySQL databases `dw`, `nova`, `neutron` | `beaver` / `beaver-snapshot` |
| Spider2 | `spider2-lite/spider2-lite.jsonl`, `spider2-lite/resource/databases/`; 准备好的清单与 direct/recovery 草稿 | `spider2` / `spider2-react` |

SQLite online 清单中的 `database_or_answer_target` 指向数据库文件或其父目录，`schema_manifest` 指向物理 schema JSON；行内相对路径以 `--data-root` 为基准。

复制 `configs/paths.example.json` 为 `configs/paths.json`，填写数据集、online 清单、ontology、模型、草稿与输出路径。该配置中的相对路径以仓库根目录为基准：

```bash
cp configs/paths.example.json configs/paths.json
python scripts/run_v17.py --paths configs/paths.json --print-command
python scripts/run_v17.py --paths configs/paths.json
```

v17 r05 入口使用 4 turns、8 actions、3 次 SQL 执行、最多 6,144 个输出 tokens。`--resume` 从配置的输出目录接续运行。其他原生数据集参数：

```bash
python scripts/native.py sqlite --help
python scripts/native.py beaver --help
python scripts/native.py evoschema --help
python scripts/native.py spider2 --help
```

## 模型

| 用途 | 模型 | Hugging Face | ModelScope |
|---|---|---|---|
| 主要生成模型 | Qwen3.8-27B-FP8 | [发布页](https://huggingface.co/Qwen/Qwen3.8-27B-FP8) | [发布页](https://modelscope.cn/models/Qwen/Qwen3.8-27B-FP8) |
| 跨模型实验 | Qwen3.5-4B | [发布页](https://huggingface.co/Qwen/Qwen3.5-4B) | [发布页](https://modelscope.cn/models/Qwen/Qwen3.5-4B) |
| 跨模型实验 | Qwen3.5-9B | [发布页](https://huggingface.co/Qwen/Qwen3.5-9B) | [发布页](https://modelscope.cn/models/Qwen/Qwen3.5-9B) |
| 跨模型实验 | Qwen3.6-35B-A3B-FP8 | [发布页](https://huggingface.co/Qwen/Qwen3.6-35B-A3B-FP8) | [发布页](https://modelscope.cn/models/Qwen/Qwen3.6-35B-A3B-FP8) |
| 跨模型实验 | DeepSeek-V4.1-Flash-1017 | [发布页](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash-1017) | [发布页](https://modelscope.cn/models/deepseek-ai/DeepSeek-V4.1-Flash-1017) |
| 向量编码 | BGE-M3 | [发布页](https://huggingface.co/BAAI/bge-m3) | [发布页](https://modelscope.cn/models/BAAI/bge-m3) |
| 重排序 | BGE-reranker-v2-m3 | [发布页](https://huggingface.co/BAAI/bge-reranker-v2-m3) | [发布页](https://modelscope.cn/models/BAAI/bge-reranker-v2-m3) |

`SCHEMARECOVERY_LLM_MODEL_PATH` 指向本地生成模型，`SCHEMARECOVERY_LLM_MODEL` 设置服务模型名，默认 `qwen3.8-27b-fp8`。`configs/paths.json` 中的 `embedding_model` 和 `reranker_base_url` 分别指定向量模型目录与重排序端点。

生成使用 OpenAI-compatible 端点，通过 `SCHEMARECOVERY_LLM_BASE_URL` 设置地址。需要认证时，在环境变量 `SCHEMARECOVERY_LLM_API_KEY` 中设置凭据；可用设置见 `.env.example`。生成配置位于 `configs/v17.yaml`；独立的 vLLM 0.30.0 服务环境依赖位于 `requirements-vllm.txt`。

`embedding_cache` 指定生成的 BGE-M3 缓存路径。可通过 `SCHEMARECOVERY_EMBEDDING_BASE_URL` 和 `SCHEMARECOVERY_EMBEDDING_MODEL=bge-m3` 使用已有的 BGE 服务。

## 代码树

```text
assets/
  ontology-v17-r05.tar.gz       Recovered ontology and semantic memory
  manifest.json                Ontology file checksums
configs/
  paths.example.json           Dataset and resource paths
  v17.yaml                     Generation configuration
scripts/
  preprocess.py                Ontology extraction and dataset manifests
  reproduce.sh                 Masked-data Main or Raw/Anchor/Main + scoring
  reproduce.py                 Package checks and native stage orchestration
  score_bird.py                Native scorer with the frozen no-deadline default
  run_v17.py                   Path-configured native v17 entry
  native.py                    Native dataset and preprocessing entry points
infra/
  run_ontology_react.py         SQLite v17 pipeline
  run_direct_raw_evidence_baseline.py  Direct Raw draft
  evaluate_bird_external.py     Native BIRD scoring
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
