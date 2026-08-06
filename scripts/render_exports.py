#!/usr/bin/env python3
"""Render deterministic scholarly discovery exports from publications.json."""

from __future__ import annotations

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "publications.json"
OUTPUTS = {
    "CITATION.bib": ROOT / "CITATION.bib",
    "atom.xml": ROOT / "atom.xml",
    "publications.jsonld": ROOT / "publications.jsonld",
}
ATOM_NAMESPACE = "http://www.w3.org/2005/Atom"
ATOM_FEED_URL = "https://hermes-labs.ai/atom.xml"
RESEARCH_URL = "https://hermes-labs.ai/research"
REQUIRED_PAPER_FIELDS = {
    "slug",
    "title",
    "short_title",
    "title_aliases",
    "citation_family_name",
    "doi",
    "publication_date",
    "publication_type",
    "license",
    "evidence_role",
    "citation_key",
    "canonical_page",
    "archive_repository",
}
PUBLICATION_TYPE_LABELS = {
    "preprint": "Preprint",
    "workingpaper": "Working paper",
    "technicalnote": "Technical note",
}

ET.register_namespace("", ATOM_NAMESPACE)


def atom_tag(name: str) -> str:
    return f"{{{ATOM_NAMESPACE}}}{name}"


def license_reference(identifier: str) -> str:
    normalized = identifier.lower()
    if normalized == "cc0-1.0":
        return "https://creativecommons.org/publicdomain/zero/1.0/"
    creative_commons = re.fullmatch(
        r"cc-(?P<terms>by(?:-[a-z]+)*)-(?P<version>\d+\.\d+)",
        normalized,
    )
    if creative_commons:
        return (
            "https://creativecommons.org/licenses/"
            f"{creative_commons.group('terms')}/{creative_commons.group('version')}/"
        )
    return identifier


def load_manifest(path: Path = MANIFEST) -> dict:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data.get("schema") != "hermes.publications/v1":
        raise ValueError("unsupported or missing publications schema")
    papers = data.get("papers")
    if not isinstance(papers, list) or not papers:
        raise ValueError("papers must be a non-empty list")

    seen_slugs: set[str] = set()
    seen_dois: set[str] = set()
    seen_keys: set[str] = set()
    for position, paper in enumerate(papers, start=1):
        missing = REQUIRED_PAPER_FIELDS - set(paper)
        if missing:
            raise ValueError(f"paper {position} missing fields: {sorted(missing)}")
        if not isinstance(paper["title_aliases"], list):
            raise ValueError(f"paper {position} title_aliases must be a list")
        publication_date = paper["publication_date"]
        if not isinstance(publication_date, str) or not re.fullmatch(
            r"\d{4}-\d{2}-\d{2}", publication_date
        ):
            raise ValueError(
                f"paper {position} publication_date must be a valid YYYY-MM-DD date: "
                f"{publication_date!r}"
            )
        try:
            date.fromisoformat(publication_date)
        except ValueError as exc:
            raise ValueError(
                f"paper {position} publication_date must be a valid YYYY-MM-DD date: "
                f"{publication_date!r}"
            ) from exc
        for field, seen in (
            ("slug", seen_slugs),
            ("doi", seen_dois),
            ("citation_key", seen_keys),
        ):
            value = paper[field]
            if value in seen:
                raise ValueError(f"duplicate {field}: {value}")
            seen.add(value)
        if not paper["doi"].startswith("10.5281/zenodo."):
            raise ValueError(f"unsupported DOI authority: {paper['doi']}")
        if not paper["canonical_page"].startswith(
            "https://hermes-labs.ai/research/"
        ):
            raise ValueError(
                f"unsupported canonical paper page: {paper['canonical_page']}"
            )
    return data


def render_bibtex(data: dict) -> str:
    author = data["author"]["name"]
    blocks: list[str] = []
    for paper in data["papers"]:
        publication_type = paper["publication_type"]
        note = PUBLICATION_TYPE_LABELS.get(publication_type, publication_type)
        title = paper["title"]
        blocks.append(
            "\n".join(
                [
                    f"@misc{{{paper['citation_key']},",
                    f"  author       = {{{author}}},",
                    f"  title        = {{{title}}},",
                    f"  year         = {{{paper['publication_date'][:4]}}},",
                    "  publisher    = {Zenodo},",
                    f"  doi          = {{{paper['doi']}}},",
                    f"  url          = {{https://doi.org/{paper['doi']}}},",
                    f"  note         = {{{note}}}",
                    "}",
                ]
            )
        )
    return "\n\n".join(blocks) + "\n"


def render_jsonld(data: dict) -> str:
    author = data["author"]
    items = []
    for position, paper in enumerate(data["papers"], start=1):
        doi_url = f"https://doi.org/{paper['doi']}"
        items.append(
            {
                "@type": "ListItem",
                "position": position,
                "item": {
                    "@type": "ScholarlyArticle",
                    "@id": doi_url,
                    "name": paper["title"],
                    "datePublished": paper["publication_date"],
                    "author": {
                        "@type": "Person",
                        "name": author["name"],
                        "identifier": author["orcid"],
                    },
                    "publisher": {"@type": "Organization", "name": "Zenodo"},
                    "license": license_reference(paper["license"]),
                    "url": doi_url,
                    "sameAs": paper["archive_repository"],
                    "description": paper["evidence_role"],
                },
            }
        )
    document = {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": "Hermes Labs Research Publications",
        "url": "https://github.com/hermes-labs-ai/hermes-publications",
        "numberOfItems": len(items),
        "itemListElement": items,
    }
    return json.dumps(document, indent=2, ensure_ascii=False) + "\n"


def render_atom(data: dict) -> str:
    root = ET.Element(atom_tag("feed"))
    ET.SubElement(root, atom_tag("title")).text = "Hermes Labs Research Publications"
    ET.SubElement(root, atom_tag("id")).text = ATOM_FEED_URL
    ET.SubElement(root, atom_tag("link"), {"rel": "self", "href": ATOM_FEED_URL})
    ET.SubElement(root, atom_tag("link"), {"rel": "alternate", "href": RESEARCH_URL})

    papers = sorted(data["papers"], key=lambda paper: paper["slug"])
    papers.sort(key=lambda paper: paper["publication_date"], reverse=True)
    updated = max(paper["publication_date"] for paper in papers) + "T00:00:00Z"
    ET.SubElement(root, atom_tag("updated")).text = updated

    author = data["author"]
    for paper in papers:
        doi_url = f"https://doi.org/{paper['doi']}"
        timestamp = paper["publication_date"] + "T00:00:00Z"
        entry = ET.SubElement(root, atom_tag("entry"))
        ET.SubElement(entry, atom_tag("title")).text = paper["title"]
        ET.SubElement(entry, atom_tag("id")).text = doi_url
        ET.SubElement(
            entry,
            atom_tag("link"),
            {"rel": "alternate", "href": paper["canonical_page"]},
        )
        ET.SubElement(entry, atom_tag("link"), {"rel": "related", "href": doi_url})
        ET.SubElement(entry, atom_tag("summary")).text = paper["evidence_role"]
        entry_author = ET.SubElement(entry, atom_tag("author"))
        ET.SubElement(entry_author, atom_tag("name")).text = author["name"]
        ET.SubElement(entry_author, atom_tag("uri")).text = author["orcid"]
        ET.SubElement(entry, atom_tag("published")).text = timestamp
        ET.SubElement(entry, atom_tag("updated")).text = timestamp

    ET.indent(root, space="  ")
    # ET.tostring's auto-generated XML declaration casing for the encoding
    # attribute ('UTF-8' vs 'utf-8') differs by Python version, which made
    # this export flip depending on which interpreter last ran it. Build the
    # declaration explicitly so the output is identical on every Python.
    body = ET.tostring(root, encoding="unicode", xml_declaration=False)
    return "<?xml version='1.0' encoding='utf-8'?>\n" + body + "\n"


def rendered_outputs(data: dict) -> dict[str, str]:
    return {
        "CITATION.bib": render_bibtex(data),
        "atom.xml": render_atom(data),
        "publications.jsonld": render_jsonld(data),
    }


def check_outputs(rendered: dict[str, str], outputs: dict[str, Path] = OUTPUTS) -> list[str]:
    errors: list[str] = []
    for name, expected in rendered.items():
        path = outputs[name]
        if not path.is_file():
            errors.append(f"missing generated export: {name}")
        elif path.read_text(encoding="utf-8") != expected:
            errors.append(f"stale generated export: {name}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="fail instead of rewriting stale exports")
    args = parser.parse_args()

    try:
        data = load_manifest()
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1
    rendered = rendered_outputs(data)

    if args.check:
        errors = check_outputs(rendered)
        if errors:
            for error in errors:
                print(f"FAIL: {error}", file=sys.stderr)
            return 1
        print(f"PASS: {len(rendered)} generated scholarly exports are current")
        return 0

    for name, content in rendered.items():
        OUTPUTS[name].write_text(content, encoding="utf-8")
        print(f"WROTE: {name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
