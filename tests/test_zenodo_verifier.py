from __future__ import annotations

import unittest

from scripts.render_exports import load_manifest
from scripts.verify_zenodo import compare


class ZenodoVerifierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        data = load_manifest()
        cls.paper = data["papers"][0]
        cls.orcid = data["author"]["orcid"].rsplit("/", 1)[-1]

    def record(self) -> dict:
        return {
            "doi": self.paper["version_doi"],
            "conceptdoi": self.paper["doi"],
            "metadata": {
                "title": self.paper["title"],
                "publication_date": self.paper["publication_date"],
                "resource_type": {"subtype": self.paper["publication_type"]},
                "license": {"id": "cc-by-4.0"},
                "creators": [{"orcid": self.orcid}],
            },
        }

    def test_matching_record_passes(self) -> None:
        self.assertEqual(compare(self.paper, self.record(), self.orcid), [])

    def test_title_drift_fails(self) -> None:
        record = self.record()
        record["metadata"]["title"] = "Different title"
        self.assertTrue(
            any("title expected" in error for error in compare(self.paper, record, self.orcid))
        )

    def test_concept_doi_drift_fails(self) -> None:
        record = self.record()
        record["conceptdoi"] = "10.5281/zenodo.1"
        self.assertTrue(any("concept_doi expected" in error for error in compare(self.paper, record, self.orcid)))


if __name__ == "__main__":
    unittest.main()
