#!/usr/bin/env python3
"""Verify that every canonical paper is represented on every repository surface."""

from __future__ import annotations

import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]


@dataclass(frozen=True)
class Paper:
    title: str
    label: str
    label_aliases: tuple[str, ...]
    doi: str
    family_name: str


PAPERS = {
    "asymmetric-burden-of-proof": Paper(
        title="The Asymmetric Burden of Proof: LLMs Show a Null-Result Asymmetry in a Matched-Vignette Benchmark",
        label="The Asymmetric Burden of Proof",
        label_aliases=(),
        doi="10.5281/zenodo.18867694",
        family_name="Bosch Rodriguez",
    ),
    "epistemic-failure-taxonomy": Paper(
        title="A Taxonomy of Epistemic Failure Modes in Large Language Models",
        label="A Taxonomy of Epistemic Failure Modes in Large Language Models",
        label_aliases=("A Taxonomy of Epistemic Failure Modes in LLMs",),
        doi="10.5281/zenodo.19042469",
        family_name="Bosch Rodriguez",
    ),
    "precise-records-unstable-meanings": Paper(
        title="Precise Records, Unstable Meanings: Measurement Validity and Unsupported Claims Derived from AI Agent Telemetry",
        label="Precise Records, Unstable Meanings",
        label_aliases=(),
        doi="10.5281/zenodo.21652317",
        family_name="Bosch",
    ),
    "generative-horizon": Paper(
        title="The Generative Horizon: Applied Hermeneutics, Linguistic Attractors, and the Limits of Model Self-Report",
        label="The Generative Horizon",
        label_aliases=(),
        doi="10.5281/zenodo.21659634",
        family_name="Bosch",
    ),
}
DOI_PATTERN = re.compile(r"10\.5281/zenodo\.\d+")
MARKDOWN_LINK_PATTERN = re.compile(r"\[[^]]*]\(([^)]+)\)")


def dois(text: str) -> set[str]:
    return set(DOI_PATTERN.findall(text))


def check_relative_links(root: Path, path: Path, text: str) -> list[str]:
    errors: list[str] = []
    for raw_target in MARKDOWN_LINK_PATTERN.findall(text):
        target = raw_target.split("#", 1)[0]
        if not target or ":" in target or target.startswith("/"):
            continue
        resolved = (path.parent / unquote(target)).resolve()
        if not resolved.exists():
            errors.append(f"{path.relative_to(root)}: missing relative link target {target}")
    return errors


def publication_section(text: str, labels: tuple[str, ...]) -> str | None:
    for label in labels:
        pattern = re.compile(
            rf"^### (?:\d+\.\s+)?{re.escape(label)}(?: \(2026\))?\s*$\n(?P<body>.*?)(?=^### |\Z)",
            re.MULTILINE | re.DOTALL,
        )
        match = pattern.search(text)
        if match:
            return match.group("body")
    return None


def citation_references(text: str) -> dict[str, tuple[str, str, str]]:
    references = text.split("\nreferences:\n", 1)
    if len(references) != 2:
        return {}
    blocks = re.split(r"(?=^  - type: article\s*$)", references[1], flags=re.MULTILINE)
    parsed: dict[str, tuple[str, str, str]] = {}
    for block in blocks:
        title = re.search(r'^    title: "([^"]+)"\s*$', block, re.MULTILINE)
        doi = re.search(r'^    doi: "([^"]+)"\s*$', block, re.MULTILINE)
        family = re.search(r'^      - family-names: "([^"]+)"\s*$', block, re.MULTILINE)
        given = re.search(r'^        given-names: "([^"]+)"\s*$', block, re.MULTILINE)
        if title and doi and family and given:
            parsed[doi.group(1)] = (title.group(1), family.group(1), given.group(1))
    return parsed


def check(root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    expected_slugs = set(PAPERS)
    expected_dois = {paper.doi for paper in PAPERS.values()}

    actual_slugs = {path.name for path in (root / "papers").iterdir() if path.is_dir()}
    if actual_slugs != expected_slugs:
        errors.append(
            f"paper folder set differs: expected {sorted(expected_slugs)}, got {sorted(actual_slugs)}"
        )

    top_readme = (root / "README.md").read_text(encoding="utf-8")
    llms = (root / "llms.txt").read_text(encoding="utf-8")
    top_cff = (root / "CITATION.cff").read_text(encoding="utf-8")
    zenodo = json.loads((root / ".zenodo.json").read_text(encoding="utf-8"))

    for slug, paper in PAPERS.items():
        folder = root / "papers" / slug
        readme_path = folder / "README.md"
        cff_path = folder / "CITATION.cff"
        for path in (readme_path, cff_path):
            if not path.is_file():
                errors.append(f"missing required file: {path.relative_to(root)}")
        if not readme_path.is_file() or not cff_path.is_file():
            continue

        paper_readme = readme_path.read_text(encoding="utf-8")
        paper_cff = cff_path.read_text(encoding="utf-8")
        for surface_name, surface in (
            (str(readme_path.relative_to(root)), paper_readme),
            (str(cff_path.relative_to(root)), paper_cff),
        ):
            if paper.doi not in surface:
                errors.append(f"{surface_name}: missing DOI {paper.doi}")
        if paper.title not in paper_cff:
            errors.append(f"{cff_path.relative_to(root)}: missing canonical title")

        for surface_name, surface in (("README.md", top_readme), ("llms.txt", llms)):
            section = publication_section(surface, (paper.label, *paper.label_aliases))
            if section is None:
                errors.append(f"{surface_name}: missing publication section for {paper.label}")
                continue
            if dois(section) != {paper.doi} or f"papers/{slug}/" not in section:
                errors.append(
                    f"{surface_name}: {paper.label} section does not bind DOI {paper.doi} to {slug}"
                )

        errors.extend(check_relative_links(root, readme_path, paper_readme))

    references = citation_references(top_cff)
    if set(references) != expected_dois:
        errors.append(
            f"CITATION.cff DOI set differs: expected {sorted(expected_dois)}, got {sorted(references)}"
        )
    for paper in PAPERS.values():
        expected_reference = (paper.title, paper.family_name, "Rolando")
        if references.get(paper.doi) != expected_reference:
            errors.append(
                f"CITATION.cff: DOI {paper.doi} is not bound to {expected_reference}"
            )

    zenodo_dois = {
        item.get("identifier")
        for item in zenodo.get("related_identifiers", [])
        if item.get("scheme") == "doi"
    }
    if zenodo_dois != expected_dois:
        errors.append(
            f".zenodo.json DOI set differs: expected {sorted(expected_dois)}, got {sorted(zenodo_dois)}"
        )

    errors.extend(check_relative_links(root, root / "README.md", top_readme))
    return errors


def main() -> int:
    errors = check()
    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print(f"PASS: {len(PAPERS)} papers agree across folders, indices, and citation metadata")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
