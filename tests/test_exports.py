from __future__ import annotations

import json
import shutil
import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

from scripts.render_exports import ATOM_NAMESPACE, check_outputs, load_manifest, rendered_outputs


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
            "atom.xml": self.root / "atom.xml",
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

    def test_invalid_publication_date_fails(self) -> None:
        for invalid_date in ("2026-7-30", "2026-02-30"):
            with self.subTest(publication_date=invalid_date):
                path = self.root / "publications.json"
                data = json.loads(path.read_text(encoding="utf-8"))
                data["papers"][0]["publication_date"] = invalid_date
                path.write_text(json.dumps(data), encoding="utf-8")
                with self.assertRaisesRegex(ValueError, "valid YYYY-MM-DD date"):
                    load_manifest(path)

    def test_non_hermes_canonical_page_fails(self) -> None:
        path = self.root / "publications.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["papers"][0]["canonical_page"] = "https://example.com/paper"
        path.write_text(json.dumps(data), encoding="utf-8")
        with self.assertRaisesRegex(ValueError, "unsupported canonical paper page"):
            load_manifest(path)

    def test_atom_namespace_fields_and_order(self) -> None:
        data = load_manifest(self.root / "publications.json")
        root = ET.fromstring(rendered_outputs(data)["atom.xml"])
        atom = {"atom": ATOM_NAMESPACE}

        self.assertEqual(root.tag, f"{{{ATOM_NAMESPACE}}}feed")
        self.assertEqual(
            root.findtext("atom:title", namespaces=atom),
            "Hermes Labs Research Publications",
        )
        self.assertEqual(
            root.findtext("atom:id", namespaces=atom),
            "https://hermes-labs.ai/atom.xml",
        )
        self.assertEqual(
            root.findtext("atom:updated", namespaces=atom),
            "2026-08-06T00:00:00Z",
        )
        self.assertEqual(
            [
                (link.get("rel"), link.get("href"))
                for link in root.findall("atom:link", atom)
            ],
            [
                ("self", "https://hermes-labs.ai/atom.xml"),
                ("alternate", "https://hermes-labs.ai/research"),
            ],
        )

        entries = root.findall("atom:entry", atom)
        expected_papers = sorted(
            data["papers"],
            key=lambda paper: (
                -int(paper["publication_date"].replace("-", "")),
                paper["slug"],
            ),
        )
        self.assertEqual(
            [entry.findtext("atom:title", namespaces=atom) for entry in entries],
            [paper["title"] for paper in expected_papers],
        )
        for entry, paper in zip(entries, expected_papers, strict=True):
            doi_url = f"https://doi.org/{paper['doi']}"
            timestamp = paper["publication_date"] + "T00:00:00Z"
            self.assertEqual(entry.findtext("atom:id", namespaces=atom), doi_url)
            self.assertEqual(
                [link.attrib for link in entry.findall("atom:link", atom)],
                [
                    {"rel": "alternate", "href": paper["canonical_page"]},
                    {"rel": "related", "href": doi_url},
                ],
            )
            self.assertEqual(
                entry.findtext("atom:summary", namespaces=atom),
                paper["evidence_role"],
            )
            self.assertEqual(
                entry.findtext("atom:author/atom:name", namespaces=atom),
                data["author"]["name"],
            )
            self.assertEqual(
                entry.findtext("atom:author/atom:uri", namespaces=atom),
                data["author"]["orcid"],
            )
            self.assertEqual(entry.findtext("atom:published", namespaces=atom), timestamp)
            self.assertEqual(entry.findtext("atom:updated", namespaces=atom), timestamp)

    def test_atom_is_deterministic_across_manifest_order(self) -> None:
        data = load_manifest(self.root / "publications.json")
        expected = rendered_outputs(data)["atom.xml"]
        data["papers"].reverse()
        self.assertEqual(rendered_outputs(data)["atom.xml"], expected)

    def test_jsonld_license_derives_from_manifest(self) -> None:
        data = load_manifest(self.root / "publications.json")
        data["papers"][0]["license"] = "CC0-1.0"
        jsonld = json.loads(rendered_outputs(data)["publications.jsonld"])
        self.assertEqual(
            jsonld["itemListElement"][0]["item"]["license"],
            "https://creativecommons.org/publicdomain/zero/1.0/",
        )

    def test_bibtex_does_not_relabel_unknown_publication_type(self) -> None:
        data = load_manifest(self.root / "publications.json")
        data["papers"][0]["publication_type"] = "report"
        bibtex = rendered_outputs(data)["CITATION.bib"]
        first_record = bibtex.split("\n\n", 1)[0]
        self.assertIn("note         = {report}", first_record)
        self.assertNotIn("note         = {Preprint}", first_record)


if __name__ == "__main__":
    unittest.main()
