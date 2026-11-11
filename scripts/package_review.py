#!/usr/bin/env python3
"""Package the reviewed app with an explicit public-file allowlist."""
import argparse
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    files = [ROOT / name for name in ["README.md", "README.zh-CN.md", "server.py", "native_adapter.py", "requirements-demo.txt", "THIRD_PARTY_PASCAL_LICENSE", "REVIEW_RECEIPT.json"]]
    files += [path for path in (ROOT / "dist").rglob("*") if path.is_file()]
    files += [path for path in (ROOT / "scripts").glob("*.py") if path.is_file()]
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(args.output, "w", ZIP_DEFLATED) as archive:
        for path in files:
            archive.write(path, "SR_Demo_Review/" + str(path.relative_to(ROOT)))
    print(f"Packaged {len(files)} allowlisted files to {args.output}")


if __name__ == "__main__":
    main()
