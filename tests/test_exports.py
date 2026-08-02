from __future__ import annotations

import json
import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.render_exports import check_outputs, load_manifest, rendered_outputs


class PublicationExportTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name) / "repo"
        source = Path(__file__).resolve().parents[1]
        shutil.copytree(source, self.root, ignore=shutil.ignore_patterns(".git", "__pycache__"))

    def tearDown(self) -> None:
        self.tempdir.cleanup()

    def outputs(self) -> dict[str, Path]:
        return {
            "CITATION.bib": self.root / "CITATION.bib",
            "publications.jsonld": self.root / "publications.jsonld",
        }

    def test_generated_exports_are_current(self) -> None:
        data = load_manifest(self.root / "publications.json")
        self.assertEqual(check_outputs(rendered_outputs(data), self.outputs()), [])

    def test_stale_export_fails(self) -> None:
        data = load_manifest(self.root / "publications.json")
        path = self.root / "CITATION.bib"
        path.write_text(path.read_text(encoding="utf-8") + "\n% stale\n", encoding="utf-8")
        self.assertIn("stale generated export: CITATION.bib", check_outputs(rendered_outputs(data), self.outputs()))

    def test_duplicate_identity_fails(self) -> None:
        path = self.root / "publications.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["papers"][1]["doi"] = data["papers"][0]["doi"]
        path.write_text(json.dumps(data), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "duplicate doi"):
            load_manifest(path)


if __name__ == "__main__":
    unittest.main()
