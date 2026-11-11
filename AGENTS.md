# Demo development

- Keep `main` as the saved interface baseline. Make changes on a feature branch; the current integration branch is `feat/full-archive-integration`.
- Preserve the workbench's visual layout and stylesheet. Implement archive bindings in `dist/archive-adapter.js`.
- Saved experiment data under `dist/data`, `dist/history-sql`, and `dist/explanations` stays in place and is not rewritten or rescored by this demo work.
- Rebuild navigation with `python3 scripts/build_workbench_index.py`; run `node tests/workbench_archive.cjs` for archive integration checks.
- Keep local runtime, credentials, environment directories, and review state out of Git.
- Do not publish or push this demo without the user's approval.
