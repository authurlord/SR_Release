# SchemaRecovery 交互审阅 Demo

[English](README.md)

本地审阅版复用 PASCAL 的三栏布局和样式。先选择 benchmark 与数据库，在中栏展开 Schema、SQL 表别名及已有业务口径，再点击 **Run**，逐步查看存档来源如何形成恢复列名、语义对象、关系与联合恢复 family。Text-to-SQL 按数据库选择问题，回放检索证据、绑定上下文、模型调用记录、SQL 和执行结果。

当前包含 8 个 benchmark、370 个相互独立的 dataset/schema 条目、全部 4,394 条固定题集的真实保存主结果（含失败记录）。每个数据库都有独立的英文、中文 Schema 解释：370 份双语 JSON 缓存、740 份可下载 Markdown 文档。点击 **Schema explanation / Business semantics** 填入当前数据库的解释；右上角中英文切换读取离线缓存。

## 打开静态回放

```bash
cd /data/workspace/yanmy/SR_Demo_Review
python3 -m http.server 8766 --bind 127.0.0.1 --directory dist
```

访问 `http://127.0.0.1:8766/`。`dist/` 是完整静态站点。Run 从空的派生视图开始，按已保存来源贡献的前缀依次展示恢复列名、objects、edges 与 coupled family；支持 1×、4×、Instant、Next step 和 Stop。速度控制的是浏览器回放节奏。

增量维护 Run 依次展示来源变化、直接受影响对象、前向依赖闭包、名称变化与未受影响列。已有别名修订使用存档中的旧假设与最终别名，在副本上运行原生 `dependency_update`；来源撤回预览有独立事件类型。相应 receipt 和 before/after 对象已保存到数据文件。

## 启动本地文件 API

把此目录与已准备的 `SR_Release` 并列放置，或通过 `--release /path/to/SR_Release` 指定原生包。

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements-demo.txt
.venv/bin/python server.py --port 8765
```

访问 `http://127.0.0.1:8765/`，同一界面同时具备文件导入和运行 API。服务默认仅绑定本机；`--port 0` 自动选择空闲端口，8787、8788 留给共享 dashboard。独立静态前端连接 API 时，服务端加上精确来源，例如 `--allow-origin http://127.0.0.1:8766`，在 Local API 中填写 `http://127.0.0.1:8765`。

SQLite 可以上传文件，也可以选择 API 主机上的现有路径。主机路径导入通过 SQLite backup 创建一致副本。SQL 历史、问题、项目副本与任务事件写入此目录的 `.runtime/`。

历史输入支持 JSONL / JSON 数组，字段为 `history_id`、`sql`、可选 `schema_context`；也支持包含 SELECT 的 `.sql` 文件。问题支持 JSONL / JSON 数组，字段为 `question`、可选 `example_id`、`anchor_sql`、`raw_sql`；纯文本按一行一题。每次导入对应一个数据库、一个物理 schema context；输入中的 context 必须与数据库 ID 一致。历史输入中额外的 question、answer、score 字段不会进入 SQL-only 构建。

`dist/fixtures/` 提供明确标记为 synthetic 的小型测试文件：`history.jsonl` 把 `t1.c2` 解释为 `revenue`，`update.jsonl` 将同一个来源修订为 `net_revenue`。执行导入、Build、增量更新后，可查看真实原生名称变化与未受影响对象保留收据。

## 对外部文件执行 Construct 与问答

启动前在 API 主机环境中设置模型凭据：

```bash
export SR_DEMO_API_KEY='your-model-key'
.venv/bin/python server.py --port 8765
```

前端只传环境变量名称，后端读取实际 key；key 不进入前端响应和任务产物。在 Local API 填写生成服务 base URL、实际 served model、OpenAI-compatible / DeepSeek 协议、BGE-M3 embedding 服务和 BGE reranker 服务。

**Build ontology** 调用 `WorkloadSemanticLayer.update`，导出 SQL 语义层，并用 `OperationalOntology` 绑定上传数据库的真实物理目录，不需要模型。**Apply native incremental update** 调用 `dependency_update.update_layer`，应用 SQL 来源修订或撤回。**Run native Construct** 对选定的 2–8 列读取物理 profile，调用原生 `reconstruct_family`，保存角色提案、约束和可行赋值。**Run questions** 复用原生远程 BGE-M3 与 reranker adapter，生成缺少的 program-graph / opaque-schema draft，再以物理 observer 和 query-local semantic memory 调用 `run_graph_evo_semantic_program_main`。

用户点击 Construct 或 Run questions 后，后端访问已配置的服务。任务流会给出进度、模型 request/response、usage、轨迹和结果。新结果以 Local API 来源标记，在同一 ontology / query 界面查看。

## API 路由

| 路由 | 功能 |
|---|---|
| `GET /api/health` | 可用操作与原生包配置 |
| `POST /api/import` | 导入文件 / 主机路径，返回 `project_id` |
| `POST /api/runs` | 启动 `build`、`update`、`construct`、`query`，返回 `run_id` |
| `GET /api/runs/{id}` | 状态、当前进度 |
| `GET /api/runs/{id}/events?after=0` | 有序事件、下一个 offset |
| `GET /api/runs/{id}/result` | 最终结果或错误 |

导入 JSON：`database_id`、`database_base64`、`history_text`、`questions_text`；或者 `paths.database`、`paths.history`、`paths.questions`。运行 JSON：`project_id`、`action`、`settings`。Construct 增加 `family: {table, columns}`；update 增加 `history_text` 与 `retract_history_ids`。设置字段为 `base_url`、`model`、`api_key_env`、`compatibility`、`embedding_base_url`、`embedding_model`、`reranker_base_url`、`reranker_model`。

## 来源与验证

`dist/data/` 保留原始来源标识与方法元数据，界面统一显示 SR。BIRD-History 取自冻结复现存档；其他 benchmark 使用各自固定的已保存主方法输入、ontology 与 prediction 题集。BIRD-History / Dev / Mini、KaggleDBQA、FIBEN、EvoSchema、BEAVER、Spider2-Lite 分别索引 1393 / 1534 / 300 / 185 / 52 / 295 / 500 / 135 题。原 18 个样例另存样例目录，总题量使用完整固定题集。每题独立 JSON 在选择时才加载；缺失轨迹和空 SQL 保留已保存状态。EvoSchema、Spider2 保留原协议的物理名称；已有恢复别名按存档显示。导出保持各问题的 SQL 和执行观察内容。

```bash
.venv/bin/python -m unittest discover -s tests -p 'test_*.py' -v
node --check dist/app.js
node --check dist/replay-enhancements.js
```

离线 API 验证覆盖 synthetic SQLite 导入、原生构建、增量别名修订、未受影响对象逐项保留、来源边界与错误输入。DOM 验证覆盖 8 个 benchmark 的原生查询步骤、Schema/KB 折叠块、构建前缀、维护 Run 和双语解释缓存。真实生成与检索服务由用户发起运行时配置。

需要重建存档时，依次运行 `scripts/export_archive.py`、`scripts/export_multibench.py`、`scripts/export_full_results.py`、`scripts/build_explanations.py`、`scripts/export_history_sql.py`；脚本来源路径指向现有本地研究存档。本审阅目录独立于方法发布仓库。

PASCAL 布局与 CSS 来自 `authurlord/PASCAL_Release` 的 `gh-pages`，commit 为 `fef13e41d01a02d0e6f3632b91795e973a5c306f`，原许可保留在 [THIRD_PARTY_PASCAL_LICENSE](THIRD_PARTY_PASCAL_LICENSE)。

审阅包通过明确的文件白名单收录应用、静态资产、说明文档和导出脚本；本地会话状态、运行时上传、虚拟环境和 QA 依赖均由打包白名单与 `.gitignore` 排除。

每个数据库的 **History SQL / 可查看的历史SQL** 折叠块展示存档中可查看的历史 SQL、原始 ID、已有来源元数据，并支持搜索、每页 20 条、逐条展开，以及恢复列名、连接和业务口径的证据联动。构建回放会高亮当前 SQL 来源。当前未包含历史 SQL 文本的存档显示「可查看的历史SQL：0条」「当前存档未包含历史SQL文本」。

左栏 **Result / 结果** 筛选默认选择 **成功**，也可切换为全部、失败、未评分。状态取自与提交 SQL 或冻结 prediction 产物匹配的已有正式逐题评分；未评分题仍保留在完整存档中。外部 API 新运行结果在没有正式评价时显示为未评分。
