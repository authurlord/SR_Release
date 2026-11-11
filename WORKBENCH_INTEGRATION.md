# Workbench archive integration

The current workbench layout and stylesheet are retained. `dist/archive-adapter.js` binds its dataset, database, Construct, Answer, Update, and inspector components to saved files.

| Dataset | DB/schema entries | Questions |
| --- | ---: | ---: |
| BIRD-History | 11 | 1393 |
| BIRD-Dev | 11 | 1534 |
| BIRD-Mini | 11 | 300 |
| KaggleDBQA | 8 | 185 |
| FIBEN | 1 | 52 |
| EvoSchema | 295 | 295 |
| BEAVER | 3 | 500 |
| Spider 2.0-Lite | 30 | 135 |
| Total | 370 | 4394 |

Navigation starts with successful saved questions. The result filter also exposes all questions, failures, and unscored records. SQL, official score status, tool observations, retrieval context, model usage, and saved execution rows remain attached to each question's archive file.

Construct replays the saved source contributions, recovered names, semantic objects, column families, and join evidence. Update replays available maintenance events and their before/after names and dependency closure. Chinese and English schema guides load per DB. A DB without a saved update event shows an empty update view.

Archive navigation loads the index once, then loads the selected DB and question on demand. Late responses from a previous selection cannot overwrite the current selection.

```sh
python3 scripts/build_workbench_index.py
node tests/workbench_archive.cjs
```

The branch is `feat/full-archive-integration`; the saved visual baseline is commit `8ed9633` on `main`. Data directories remain local alongside the tracked source files. This integration uses CPU and saved JSON; it makes no model calls or database queries. The existing native local API remains a separate service on port 8765; this archive adapter does not start live runs.
