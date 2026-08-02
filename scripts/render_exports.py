#!/usr/bin/env python3
"""Render deterministic scholarly discovery exports from publications.json."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "publications.json"
OUTPUTS = {
    "CITATION.bib": ROOT / "CITATION.bib",
    "publications.jsonld": ROOT / "publications.jsonld",
}
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
    "archive_repository",
}


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
    return data


def render_bibtex(data: dict) -> str:
    author = data["author"]["name"]
    blocks: list[str] = []
    for paper in data["papers"]:
        note = "Working paper" if paper["publication_type"] == "workingpaper" else "Preprint"
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
                    "license": "https://creativecommons.org/licenses/by/4.0/",
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


def rendered_outputs(data: dict) -> dict[str, str]:
    return {
        "CITATION.bib": render_bibtex(data),
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
