"""Offline API integration: synthetic files, native parsing/update, no model or retrieval calls."""
import base64
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import time
import unittest
from urllib.error import HTTPError
from urllib.request import Request, urlopen, build_opener, ProxyHandler

ROOT = Path(__file__).resolve().parents[1]
HTTP = build_opener(ProxyHandler({}))


class APITest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.runtime = tempfile.TemporaryDirectory(dir=ROOT)
        cls.server = subprocess.Popen([sys.executable, str(ROOT / "server.py"), "--port", "0", "--runtime", cls.runtime.name], stdout=subprocess.PIPE, text=True)
        cls.base = cls.server.stdout.readline().strip().split()[-1]

    @classmethod
    def tearDownClass(cls):
        cls.server.terminate()
        cls.server.wait(timeout=5)
        cls.server.stdout.close()
        cls.runtime.cleanup()

    def request(self, path, payload=None, origin=None):
        headers = {"Content-Type": "application/json"}
        if origin:
            headers["Origin"] = origin
        req = Request(self.base + path, data=json.dumps(payload).encode() if payload is not None else None, headers=headers)
        with HTTP.open(req, timeout=5) as response:
            return response.status, json.load(response)

    def wait(self, identity):
        for _ in range(120):
            _, run = self.request("/api/runs/" + identity)
            if run["status"] != "running":
                _, result = self.request("/api/runs/" + identity + "/result")
                return run, result
            time.sleep(.05)
        self.fail("run timed out")

    def test_import_build_incremental_update(self):
        fixture = ROOT / "dist/fixtures"
        _, imported = self.request("/api/import", {"database_id": "fixture", "database_base64": base64.b64encode((fixture / "fixture.sqlite").read_bytes()).decode(), "history_text": (fixture / "history.jsonl").read_text(), "questions_text": (fixture / "questions.jsonl").read_text()})
        self.assertEqual(imported["history_count"], 3)
        _, start = self.request("/api/runs", {"project_id": imported["project_id"], "action": "build"})
        run, result = self.wait(start["run_id"])
        self.assertEqual(run["status"], "completed", result)
        before = result["result"]
        revenue = next(row for row in before["ontology"]["objects"] if row["kind"] == "column" and "t1.c2" in row["physical_identifiers"])
        self.assertIn("revenue", revenue["aliases"])
        self.assertTrue(before["ontology"]["edges"])
        _, start = self.request("/api/runs", {"project_id": imported["project_id"], "action": "update", "history_text": (fixture / "update.jsonl").read_text()})
        run, result = self.wait(start["run_id"])
        self.assertEqual(run["status"], "completed", result)
        after = result["result"]
        revenue = next(row for row in after["ontology"]["objects"] if row["kind"] == "column" and "t1.c2" in row["physical_identifiers"])
        self.assertIn("net_revenue", revenue["aliases"])
        self.assertNotIn("revenue", revenue["aliases"])
        receipt = after["maintenance"][-1]["receipt"]
        self.assertGreater(receipt["unchanged_object_count"], 0)
        skipped = set(receipt["skipped_ids"])
        old = {row["id"]: row for row in before["ontology"]["objects"]}
        new = {row["id"]: row for row in after["ontology"]["objects"]}
        self.assertTrue(all(old[key] == new[key] for key in skipped))
        _, events = self.request("/api/runs/" + start["run_id"] + "/events")
        self.assertTrue(any(e["type"] == "maintenance" for e in events["events"]))
        self.assertFalse(any(e["type"].startswith("model_") for e in events["events"]))

    def test_input_errors_and_origin(self):
        with self.assertRaises(HTTPError) as caught:
            self.request("/api/import", {"database_base64": "aW52YWxpZA==", "history_text": "SELECT c1 FROM t1"})
        self.assertEqual(caught.exception.code, 400)
        with self.assertRaises(HTTPError) as caught:
            self.request("/api/runs", {"action": "build"}, origin="https://unconfigured.example")
        self.assertEqual(caught.exception.code, 403)
        with self.assertRaises(HTTPError) as caught:
            self.request("/api/runs", {"project_id": "absent", "action": "query"})
        self.assertEqual(caught.exception.code, 400)

    def test_sql_only_boundary(self):
        sys.path[:0] = [str(ROOT), str(ROOT.parent / "SR_Release/src")]
        from native_adapter import read_rows, validate_settings
        rows = read_rows('{"sql":"SELECT c1 FROM t1", "question":"secret target", "answer":"not input", "score":1}', "history", "fixture")
        self.assertEqual(set(rows[0]), {"history_id", "schema_context", "sql", "dialect"})
        with self.assertRaises(ValueError):
            validate_settings({"base_url": "http://localhost/v1", "model": "test", "api_key": "never-save"})
        self.assertEqual(len(read_rows("SELECT c1 FROM t1; SELECT c2 FROM t1;", "history", "fixture")), 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
