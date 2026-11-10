from __future__ import annotations

import argparse
import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Callable


TOKEN_RE = re.compile(r"[A-Za-z]+|\d+|[\u4e00-\u9fff]")
PREFIXES = ("HAS", "IS", "OF", "BY", "TO", "FROM", "AND", "WITH", "DATE", "VALUE", "AMOUNT", "NAME", "ID")


def tokenize(text: str) -> list[str]:
    text = text.replace("_", " ").replace(".", " ")
    tokens = [match.group(0).lower() for match in TOKEN_RE.finditer(text)]
    expanded = list(tokens)
    for token in tokens:
        upper = token.upper()
        for prefix in PREFIXES:
            if upper.startswith(prefix) and len(upper) > len(prefix) + 2:
                expanded.extend([prefix.lower(), upper[len(prefix) :].lower()])
    return expanded


class BM25Index:
    def __init__(self, documents: list[dict[str, Any]], k1: float = 1.5, b: float = 0.75):
        self.documents = documents
        self.k1 = k1
        self.b = b
        self.tokens = [tokenize(f"{doc['name']} {doc['text']}") for doc in documents]
        self.lengths = [len(tokens) for tokens in self.tokens]
        self.avgdl = sum(self.lengths) / max(len(self.lengths), 1)
        self.term_frequencies = [Counter(tokens) for tokens in self.tokens]
        document_frequency: Counter[str] = Counter()
        for tokens in self.tokens:
            document_frequency.update(set(tokens))
        n = max(len(documents), 1)
        self.idf = {
            term: math.log(1 + (n - count + 0.5) / (count + 0.5))
            for term, count in document_frequency.items()
        }

    def search(
        self,
        query: str,
        top_k: int = 20,
        document_filter: Callable[[dict[str, Any]], bool] | None = None,
    ) -> list[dict[str, Any]]:
        query_terms = tokenize(query)
        scores = []
        for index, frequencies in enumerate(self.term_frequencies):
            if document_filter is not None and not document_filter(self.documents[index]):
                continue
            score = 0.0
            dl = self.lengths[index]
            for term in query_terms:
                frequency = frequencies.get(term, 0)
                if not frequency:
                    continue
                numerator = frequency * (self.k1 + 1)
                denominator = frequency + self.k1 * (1 - self.b + self.b * dl / max(self.avgdl, 1))
                score += self.idf.get(term, 0.0) * numerator / denominator
            if score > 0:
                scores.append((score, index))
        scores.sort(reverse=True)
        return [
            {"score": round(score, 6), "document": self.documents[index]}
            for score, index in scores[:top_k]
        ]

    def save(self, path: Path) -> None:
        path.write_text(
            json.dumps({"version": 1, "documents": self.documents}, ensure_ascii=False),
            encoding="utf-8",
        )

    @classmethod
    def load(cls, path: Path) -> "BM25Index":
        data = json.loads(path.read_text(encoding="utf-8"))
        return cls(data["documents"])


def load_jsonl(paths: list[Path]) -> list[dict[str, Any]]:
    documents = []
    for path in paths:
        if not path.exists():
            continue
        documents.extend(json.loads(line) for line in path.read_text(encoding="utf-8").splitlines())
    return documents


def main() -> None:
    parser = argparse.ArgumentParser()
    sub = parser.add_subparsers(dest="command", required=True)
    build = sub.add_parser("build")
    build.add_argument("--catalog", type=Path, required=True)
    build.add_argument("--patterns", type=Path, required=True)
    build.add_argument("--output", type=Path, required=True)
    search = sub.add_parser("search")
    search.add_argument("--index", type=Path, required=True)
    search.add_argument("--query", required=True)
    search.add_argument("--top-k", type=int, default=10)
    args = parser.parse_args()
    if args.command == "build":
        documents = load_jsonl([args.catalog, args.patterns])
        BM25Index(documents).save(args.output)
        print(json.dumps({"documents": len(documents), "output": str(args.output)}, indent=2))
    else:
        print(json.dumps(BM25Index.load(args.index).search(args.query, args.top_k), indent=2))


if __name__ == "__main__":
    main()
