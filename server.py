#!/usr/bin/env python3
"""Serve the SR review UI and loopback file/run API; model calls start on POST /api/runs."""
import argparse
import base64
import hashlib
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
import json
import os
from pathlib import Path
import re
import shutil
import sqlite3
import sys
from threading import Lock, Thread
import time
from urllib.parse import parse_qs, urlparse
import uuid

ROOT = Path(__file__).resolve().parent
PROJECTS = {}
RUNS = {}
LOCK = Lock()
BUSY = set()
OPTIONS = None


def load_native(release):
    for path in [str(release / "src"), str(release / "infra")]:
        if path not in sys.path:
            sys.path.insert(0, path)
    import native_adapter
    return native_adapter


def import_project(payload):
    adapter = load_native(OPTIONS.release)
    identity = uuid.uuid4().hex
    context = str(payload.get("database_id") or "external")
    if not re.fullmatch(r"[A-Za-z0-9_-]{1,80}", context):
        raise ValueError("database_id uses 1–80 letters, digits, underscore or hyphen")
    history_text = str(payload.get("history_text") or "")
    question_text = str(payload.get("questions_text") or "")
    paths = payload.get("paths") or {}
    if not isinstance(paths, dict):
        raise ValueError("paths must be an object")
    for key, destination in [("history", "history"), ("questions", "questions")]:
        if paths.get(key):
            value = Path(paths[key]).expanduser().read_text()
            if destination == "history":
                history_text = value
            else:
                question_text = value
    histories = adapter.read_rows(history_text, "history", context)
    questions = adapter.read_rows(question_text, "questions", context)
    if not histories:
        raise ValueError("provide a nonempty SQL-only history file")
    directory = OPTIONS.runtime / identity
    directory.mkdir(parents=True)
    database = directory / "database.sqlite"
    try:
        if paths.get("database"):
            source = Path(paths["database"]).expanduser().resolve()
            connection = sqlite3.connect(source.as_uri() + "?mode=ro", uri=True)
            output = sqlite3.connect(database)
            try:
                connection.backup(output)
            finally:
                connection.close()
                output.close()
        elif payload.get("database_base64"):
            raw = base64.b64decode(payload["database_base64"], validate=True)
            if not raw.startswith(b"SQLite format 3\x00"):
                raise ValueError("database upload must be a SQLite file")
            database.write_bytes(raw)
        else:
            raise ValueError("provide database_base64 or paths.database")
        adapter.physical_catalog(database, context)
        project = {"id": identity, "database_id": context, "directory": str(directory), "history": histories,
                   "questions": questions, "database_sha256": hashlib.sha256(database.read_bytes()).hexdigest()}
        adapter.json_write(directory / "project.json", project)
        with LOCK:
            PROJECTS[identity] = project
        return {"project_id": identity, "database_id": context, "history_count": len(histories),
                "question_count": len(questions), "database_sha256": project["database_sha256"]}
    except Exception:
        shutil.rmtree(directory)
        raise


def start_run(payload):
    adapter = load_native(OPTIONS.release)
    project_id = str(payload.get("project_id") or "")
    if project_id not in PROJECTS:
        raise ValueError("import a project first")
    action = payload.get("action", "build")
    if action not in {"build", "construct", "query", "update"}:
        raise ValueError("action must be build, construct, query or update")
    settings = payload.get("settings") or {}
    if action in {"construct", "query"}:
        adapter.validate_settings(settings, query=action == "query")
    if action != "build":
        if not (Path(PROJECTS[project_id]["directory"]) / "built.json").exists():
            raise ValueError("build the imported ontology first")
    if action == "query" and not PROJECTS[project_id]["questions"]:
        raise ValueError("import at least one question before running queries")
    identity = uuid.uuid4().hex
    directory = Path(PROJECTS[project_id]["directory"])
    secrets = [os.environ.get(settings.get("api_key_env", "SR_DEMO_API_KEY"), "")]

    def redact(value):
        if isinstance(value, str):
            for secret in secrets:
                if secret:
                    value = value.replace(secret, "[redacted]")
            return value
        if isinstance(value, dict):
            return {k: redact(v) for k, v in value.items()}
        if isinstance(value, list):
            return [redact(v) for v in value]
        return value

    def emit(kind, message, data):
        with LOCK:
            run = RUNS[identity]
            event = redact({"index": len(run["events"]), "time": time.time(), "type": kind, "message": message, "data": data})
            run["events"].append(event)
            run["message"] = message
            with (directory / (identity + ".events.jsonl")).open("a") as handle:
                handle.write(json.dumps(event, ensure_ascii=False) + "\n")

    def worker():
        try:
            emit("status", "Started " + action, {"native_release": str(OPTIONS.release)})
            if action == "build":
                result = adapter.build_project(PROJECTS[project_id], emit)
            elif action == "construct":
                result = adapter.construct_project(PROJECTS[project_id], settings, payload.get("family") or {}, emit)
            elif action == "update":
                result = adapter.update_project(PROJECTS[project_id], payload, emit)
            else:
                result = adapter.run_queries(PROJECTS[project_id], settings, emit)
            with LOCK:
                RUNS[identity]["result"] = redact(result)
                RUNS[identity]["status"] = "completed"
            emit("status", "Completed " + action, {})
        except Exception as error:
            with LOCK:
                RUNS[identity]["status"] = "failed"
                RUNS[identity]["error"] = redact(type(error).__name__ + ": " + str(error))
            emit("error", "Run failed", {"error": RUNS[identity]["error"]})
        finally:
            with LOCK:
                BUSY.discard(project_id)

    with LOCK:
        if project_id in BUSY:
            raise ValueError("this project already has a running task")
        BUSY.add(project_id)
        RUNS[identity] = {"id": identity, "project_id": project_id, "action": action,
                          "status": "running", "message": "Queued", "events": [], "result": None}
    Thread(target=worker, daemon=True).start()
    return {"run_id": identity, "status": "running"}


class Handler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(ROOT / "dist"), **kwargs)

    def log_message(self, fmt, *args):
        # Paths are enough for local review; request bodies and headers stay out of logs.
        return

    def origin_allowed(self):
        origin = self.headers.get("Origin")
        if not origin:
            return True
        expected = "http://" + self.headers.get("Host", "")
        return origin == expected or origin in OPTIONS.allow_origin

    def end_headers(self):
        origin = self.headers.get("Origin")
        if origin and self.origin_allowed():
            self.send_header("Access-Control-Allow-Origin", origin)
            self.send_header("Vary", "Origin")
        self.send_header("X-Content-Type-Options", "nosniff")
        super().end_headers()

    def json_response(self, status, value):
        body = json.dumps(value, ensure_ascii=False).encode()
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_OPTIONS(self):
        if not self.origin_allowed():
            return self.json_response(403, {"error": "origin is not enabled; start server with --allow-origin"})
        self.send_response(204)
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Access-Control-Allow-Headers", "Content-Type")
        self.end_headers()

    def do_GET(self):
        url = urlparse(self.path)
        if url.path == "/api/health":
            return self.json_response(200, {"service": "schema-recovery-local-api", "version": 1,
                "release": str(OPTIONS.release), "operations": ["import", "build", "update", "construct", "query"],
                "credential_source": "server environment", "active_runs": sum(r["status"] == "running" for r in RUNS.values())})
        if url.path.startswith("/api/runs/"):
            parts = url.path.strip("/").split("/")
            if len(parts) < 3:
                return self.json_response(404, {"error": "unknown run"})
            with LOCK:
                run = RUNS.get(parts[2])
                if run is None:
                    return self.json_response(404, {"error": "unknown run"})
                if len(parts) == 4 and parts[3] == "events":
                    try:
                        after = max(0, int(parse_qs(url.query).get("after", ["0"])[0]))
                    except ValueError:
                        return self.json_response(400, {"error": "after must be an integer"})
                    value = {"events": list(run["events"][after:]), "next": len(run["events"]), "status": run["status"]}
                elif len(parts) == 4 and parts[3] == "result":
                    value = {"status": run["status"], "result": run["result"], "error": run.get("error")}
                elif len(parts) == 3:
                    value = {key: value for key, value in run.items() if key not in {"events", "result"}}
                    value["event_count"] = len(run["events"])
                else:
                    return self.json_response(404, {"error": "unknown API route"})
            return self.json_response(200, value)
        if url.path.startswith("/api/"):
            return self.json_response(404, {"error": "unknown API route"})
        return super().do_GET()

    def do_POST(self):
        if not self.origin_allowed():
            return self.json_response(403, {"error": "origin is not enabled; start server with --allow-origin"})
        if self.headers.get_content_type() != "application/json":
            return self.json_response(415, {"error": "Content-Type must be application/json"})
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if not 0 < length <= OPTIONS.max_upload_mb * 1024 * 1024:
                return self.json_response(413, {"error": "payload exceeds configured upload size"})
            payload = json.loads(self.rfile.read(length))
            if not isinstance(payload, dict):
                raise ValueError("JSON request must be an object")
            if self.path == "/api/import":
                return self.json_response(201, import_project(payload))
            if self.path == "/api/runs":
                return self.json_response(202, start_run(payload))
            return self.json_response(404, {"error": "unknown API route"})
        except (ValueError, KeyError, OSError, sqlite3.Error, ImportError) as error:
            self.json_response(400, {"error": type(error).__name__ + ": " + str(error)})


def main():
    global OPTIONS
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--host", default="127.0.0.1", choices=["127.0.0.1", "localhost", "::1"])
    parser.add_argument("--port", type=int, default=8765, help="use 0 for an OS-selected free port")
    parser.add_argument("--release", type=Path, default=ROOT.parent / "SR_Release")
    parser.add_argument("--runtime", type=Path, default=ROOT / ".runtime")
    parser.add_argument("--allow-origin", action="append", default=[], help="enable a reviewed static frontend origin")
    parser.add_argument("--max-upload-mb", type=int, default=128)
    OPTIONS = parser.parse_args()
    if OPTIONS.port in {8787, 8788}:
        parser.error("8787/8788 are reserved for the shared dashboard")
    OPTIONS.release = OPTIONS.release.resolve()
    OPTIONS.runtime = OPTIONS.runtime.resolve()
    if not (OPTIONS.release / "src/finsemguard").is_dir():
        parser.error("--release must point to the prepared SR release package")
    load_native(OPTIONS.release)
    OPTIONS.runtime.mkdir(parents=True, exist_ok=True)
    server = ThreadingHTTPServer((OPTIONS.host, OPTIONS.port), Handler)
    print(f"SR review UI + local API: http://{OPTIONS.host}:{server.server_port}", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
