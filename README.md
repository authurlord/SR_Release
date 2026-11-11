# SchemaRecovery interactive review demo

[中文说明](README.zh-CN.md)

This local review build reuses PASCAL's three-column browser layout and stylesheet. Choose a benchmark, open a database, inspect its collapsible schema and business definitions, then click **Run** to follow ontology construction from saved source contributions. The Text-to-SQL tab replays each selected question's retrieval, bound context, recorded model usage, SQL and execution observations.

The prepared archive covers 8 benchmarks, 370 separate dataset/schema entries and all 4,394 fixed saved main results, including saved failures. Each database has its own English and Chinese schema guide: 370 cached JSON guides and 740 downloadable Markdown documents. **Schema explanation**, **Business semantics** and the language switch load these prepared files.

## Open the static archive

```bash
cd /data/workspace/yanmy/SR_Demo_Review
python3 -m http.server 8766 --bind 127.0.0.1 --directory dist
```

Open `http://127.0.0.1:8766/`. The `dist/` directory is a complete static site. Its Run controls advance through saved artifact contributions; 1×, 4× and Instant control browser playback. Next step and Stop support manual inspection. Construction starts with an empty derived view and progressively reveals recovered columns, objects, edges and coupled families.

Maintenance Run displays the selected source event, seed set, forward dependency closure, changed aliases and preserved columns. Recorded alias hypotheses and final aliases are replayed on copies using native `dependency_update`; source-withdrawal previews are identified by their event type. Their receipts and before/after objects are included in the archive.

## Start the local file API

Place this directory next to the prepared `SR_Release` package, or pass `--release /path/to/SR_Release`.

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements-demo.txt
.venv/bin/python server.py --port 8765
```

Open `http://127.0.0.1:8765/` for the same frontend with its API. The service binds to loopback. `--port 0` selects a free port; 8787 and 8788 remain reserved for the shared dashboard. To connect a separately served static frontend, pass its exact origin with `--allow-origin http://127.0.0.1:8766`, then enter `http://127.0.0.1:8765` under Local API.

Import an uploaded SQLite file or specify an existing database path on the API host. Supply SQL-only history and optional questions. Host-path imports use SQLite backup to copy a consistent snapshot. Working files and events are written under this directory's `.runtime/`.

History accepts JSONL / a JSON array with `history_id`, `sql` and optional `schema_context`, or a `.sql` file containing SELECT statements. Questions accept JSONL / a JSON array with `question`, optional `example_id`, `anchor_sql`, `raw_sql`, or one question per text line. Each import contains one database and one physical schema context. The database ID must match any supplied context. Extra question, answer and score fields are excluded from SQL history construction.

The downloadable files under `dist/fixtures/` are explicitly synthetic test inputs. `history.jsonl` names `t1.c2` as `revenue`; `update.jsonl` corrects the same source to `net_revenue`. Import, Build and Apply incremental update expose the resulting alias change and native preservation receipt.

## Run Construct or answer external questions

Set the generation credential in the server environment before startup:

```bash
export SR_DEMO_API_KEY='your-model-key'
.venv/bin/python server.py --port 8765
```

The browser sends the environment variable's name. Model keys are read by the backend and excluded from frontend responses and task artifacts. Configure the generation base URL, exact served model, OpenAI-compatible / DeepSeek profile, BGE-M3 embedding service and BGE reranker service in Local API.

**Build ontology** calls `WorkloadSemanticLayer.update`, exports the SQL semantic layer and binds it to the uploaded physical catalogue through `OperationalOntology`. It requires no model service. **Apply native incremental update** calls `dependency_update.update_layer` for changed or retracted SQL sources. **Run native Construct** reads the selected 2–8 column family, calls native `reconstruct_family` and saves proposals, constraints and feasible assignments. **Run questions** uses the native remote BGE-M3 and reranker adapters; generates missing program-graph and opaque-schema drafts; then calls `run_graph_evo_semantic_program_main` with the physical observer and query-local semantic memory.

User-started Construct and question runs make calls to the configured services. The task stream exposes progress, model request/response payloads, usage, traces and results. New results open in the same ontology and query explorer with Local API source labels.

## API routes

| Route | Function |
|---|---|
| `GET /api/health` | Available operations and configured package |
| `POST /api/import` | Import files / host paths; return `project_id` |
| `POST /api/runs` | Start `build`, `update`, `construct` or `query`; return `run_id` |
| `GET /api/runs/{id}` | Status and progress message |
| `GET /api/runs/{id}/events?after=0` | Ordered events and next offset |
| `GET /api/runs/{id}/result` | Final result or recorded error |

Import JSON fields: `database_id`, `database_base64`, `history_text`, `questions_text`; alternatively `paths.database`, `paths.history`, `paths.questions`. Run JSON fields: `project_id`, `action`, `settings`; Construct adds `family: {table, columns}`; update adds `history_text` and `retract_history_ids`. Settings use `base_url`, `model`, `api_key_env`, `compatibility`, `embedding_base_url`, `embedding_model`, `reranker_base_url`, `reranker_model`.

## Sources and checks

Saved source identifiers and original method metadata remain in `dist/data/`; presentation labels use SR. BIRD-History comes from the frozen reproduction archive. Other benchmark views consume their fixed saved main input, ontology and prediction populations. BIRD-History / Dev / Mini, KaggleDBQA, FIBEN, EvoSchema, BEAVER and Spider2-Lite contain 1393 / 1534 / 300 / 185 / 52 / 295 / 500 / 135 indexed questions. The original 18 examples remain in a separate examples catalogue; total counts use the complete fixed populations. Every question fetches its own JSON only when selected; saved missing traces and empty SQL retain their recorded status. EvoSchema and Spider2 retain their released physical identifiers; recovered aliases are shown when recorded. The export scripts preserve each question's saved SQL and execution observations.

```bash
.venv/bin/python -m unittest discover -s tests -p 'test_*.py' -v
node --check dist/app.js
node --check dist/replay-enhancements.js
```

Offline API checks cover synthetic SQLite import, native construction, incremental alias correction, preservation of unaffected objects, source boundaries and input errors. DOM checks load all 8 benchmarks and their native query steps, schema/KB folds, construction prefixes, maintenance Run and bilingual cached guides. Real generation and retrieval services are configured when starting a user run.

Rebuild saved assets in order with `scripts/export_archive.py`, `scripts/export_multibench.py`, `scripts/export_full_results.py`, `scripts/build_explanations.py`, then `scripts/export_history_sql.py`; their source paths point to the existing local research archives. This review directory is independent of the method release repository.

PASCAL layout/CSS reference: `authurlord/PASCAL_Release`, `gh-pages` commit `fef13e41d01a02d0e6f3632b91795e973a5c306f`. Its notice is retained in [THIRD_PARTY_PASCAL_LICENSE](THIRD_PARTY_PASCAL_LICENSE).

Review packages include only the explicit application, static assets, documentation and export scripts. Local session state, runtime uploads, virtual environments and QA dependencies are excluded by the packaging allowlist and `.gitignore`.

The per-database **History SQL** fold shows available archived historical SQL text, with original IDs, existing metadata, search, 20-row pagination and links to supported recovered columns, joins and business definitions. Construction playback highlights its current SQL contributions. Counts are scoped to the text present in each native source archive.

The **Result / 结果** filter defaults to **Success**. Choose All, Failure or Unscored to browse the remaining saved questions. Status comes from existing official per-question score fields bound to the submitted SQL or frozen prediction artifact. Unscored questions remain in the complete archive, and new local API outputs display as Unscored until an official evaluation is supplied.
