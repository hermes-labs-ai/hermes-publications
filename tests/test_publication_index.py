from __future__ import annotations

import shutil
import tempfile
import unittest
from pathlib import Path

from scripts.check_publications import ROOT, check


class PublicationIndexTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name) / "repo"
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns(".git", "__pycache__"))

    def tearDown(self) -> None:
        self.tempdir.cleanup()

    def test_current_index_passes(self) -> None:
        self.assertEqual(check(self.root), [])

    def test_swapped_readme_dois_fail(self) -> None:
        path = self.root / "README.md"
        text = path.read_text(encoding="utf-8")
        first = "10.5281/zenodo.21652317"
        second = "10.5281/zenodo.21659634"
        text = text.replace(first, "SWAP_DOI", 1).replace(second, first, 1).replace("SWAP_DOI", second, 1)
        path.write_text(text, encoding="utf-8")
        self.assertTrue(any("does not bind DOI" in error for error in check(self.root)))

    def test_swapped_citation_titles_fail(self) -> None:
        path = self.root / "CITATION.cff"
        text = path.read_text(encoding="utf-8")
        first = "Precise Records, Unstable Meanings: Measurement Validity and Unsupported Claims Derived from AI Agent Telemetry"
        second = "The Generative Horizon: Applied Hermeneutics, Linguistic Attractors, and the Limits of Model Self-Report"
        text = text.replace(first, "SWAP_TITLE", 1).replace(second, first, 1).replace("SWAP_TITLE", second, 1)
        path.write_text(text, encoding="utf-8")
        self.assertTrue(any("is not bound" in error for error in check(self.root)))


if __name__ == "__main__":
    unittest.main()
