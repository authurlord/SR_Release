#!/usr/bin/env python3
"""Build the static GitHub Pages site from the saved workbench archive."""
import argparse
import json
import shutil
import subprocess
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    output = args.output.resolve()
    source = ROOT / "dist"
    if output == source or source in output.parents:
        parser.error("output must be outside dist")
    if output.exists() and any(output.iterdir()):
        parser.error("output directory must be empty")
    output.mkdir(parents=True, exist_ok=True)
    counts = Counter()
    files = []
    roots = [source / x for x in ["index.html", "archive-adapter.js", "archive-index.json", "LICENSE-PASCAL.txt", "vendor", "data", "explanations", "history-sql"]]
    for item in roots:
        paths = item.rglob("*") if item.is_dir() else [item]
        for path in paths:
            if not path.is_file():
                continue
            relative = path.relative_to(source)
            dest = output / relative
            dest.parent.mkdir(parents=True, exist_ok=True)
            if path.suffix == ".json":
                # Minify whitespace while retaining all saved fields and values.
                data = json.loads(path.read_text())
                dest.write_text(json.dumps(data, ensure_ascii=False, separators=(",", ":"), allow_nan=False) + "\n")
            else:
                shutil.copy2(path, dest)
            counts[relative.parts[0]] += dest.stat().st_size
            files.append(relative.as_posix())
    html = (output / "index.html").read_text()
    html = html.replace("https://www.gstatic.com/antigravity/web/dev/tailwindcss.min.js", "vendor/tailwindcss.min.js")
    (output / "index.html").write_text(html)
    (output / ".nojekyll").write_text("")
    index = json.loads((output / "archive-index.json").read_text())
    status = Counter()
    for group in index["datasets"]:
        for db in group["databases"]:
            for case in db["cases"]:
                if not (output / case["path"]).is_file():
                    raise FileNotFoundError(case["path"])
                status[case["result_status"] or "unknown"] += 1
    total = sum(p.stat().st_size for p in output.rglob("*") if p.is_file())
    if total >= 1_000_000_000:
        raise ValueError("Site exceeds the GitHub Pages size limit")
    manifest = {
        "source_commit": subprocess.check_output(["git", "rev-parse", "HEAD"], cwd=ROOT, text=True).strip(),
        "datasets": len(index["datasets"]), "databases": index["database_count"],
        "questions": index["question_count"], "default_result_filter": "success",
        "result_counts": dict(status), "bytes": total, "file_count": len(files) + 1,
    }
    (output / "PUBLICATION_MANIFEST.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(manifest, ensure_ascii=False))


if __name__ == "__main__":
    main()
