#!/usr/bin/env python3
"""Verify that every canonical paper is represented on every repository surface."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
PAPERS = {
    "asymmetric-burden-of-proof": (
        "The Asymmetric Burden of Proof: LLMs Show a Null-Result Asymmetry in a Matched-Vignette Benchmark",
        "10.5281/zenodo.18867694",
    ),
    "epistemic-failure-taxonomy": (
        "A Taxonomy of Epistemic Failure Modes in Large Language Models",
        "10.5281/zenodo.19042469",
    ),
    "precise-records-unstable-meanings": (
        "Precise Records, Unstable Meanings: Measurement Validity and Unsupported Claims Derived from AI Agent Telemetry",
        "10.5281/zenodo.21652317",
    ),
    "generative-horizon": (
        "The Generative Horizon: Applied Hermeneutics, Linguistic Attractors, and the Limits of Model Self-Report",
        "10.5281/zenodo.21659634",
    ),
}
DOI_PATTERN = re.compile(r"10\.5281/zenodo\.\d+")
MARKDOWN_LINK_PATTERN = re.compile(r"\[[^]]*]\(([^)]+)\)")


def dois(text: str) -> set[str]:
    return set(DOI_PATTERN.findall(text))


def check_relative_links(path: Path, text: str) -> list[str]:
    errors: list[str] = []
    for raw_target in MARKDOWN_LINK_PATTERN.findall(text):
        target = raw_target.split("#", 1)[0]
        if not target or ":" in target or target.startswith("/"):
            continue
        resolved = (path.parent / unquote(target)).resolve()
        if not resolved.exists():
            errors.append(f"{path.relative_to(ROOT)}: missing relative link target {target}")
    return errors


def check() -> list[str]:
    errors: list[str] = []
    expected_slugs = set(PAPERS)
    expected_dois = {doi for _, doi in PAPERS.values()}

    actual_slugs = {path.name for path in (ROOT / "papers").iterdir() if path.is_dir()}
    if actual_slugs != expected_slugs:
        errors.append(
            f"paper folder set differs: expected {sorted(expected_slugs)}, got {sorted(actual_slugs)}"
        )

    top_readme = (ROOT / "README.md").read_text(encoding="utf-8")
    llms = (ROOT / "llms.txt").read_text(encoding="utf-8")
    top_cff = (ROOT / "CITATION.cff").read_text(encoding="utf-8")
    zenodo = json.loads((ROOT / ".zenodo.json").read_text(encoding="utf-8"))

    for slug, (title, doi) in PAPERS.items():
        folder = ROOT / "papers" / slug
        readme_path = folder / "README.md"
        cff_path = folder / "CITATION.cff"
        for path in (readme_path, cff_path):
            if not path.is_file():
                errors.append(f"missing required file: {path.relative_to(ROOT)}")
        if not readme_path.is_file() or not cff_path.is_file():
            continue

        paper_readme = readme_path.read_text(encoding="utf-8")
        paper_cff = cff_path.read_text(encoding="utf-8")
        for surface_name, surface in (
            ("README.md", top_readme),
            ("llms.txt", llms),
            (str(readme_path.relative_to(ROOT)), paper_readme),
            (str(cff_path.relative_to(ROOT)), paper_cff),
        ):
            if doi not in surface:
                errors.append(f"{surface_name}: missing DOI {doi}")
        if title not in paper_cff:
            errors.append(f"{cff_path.relative_to(ROOT)}: missing canonical title")
        if f"papers/{slug}/" not in top_readme or f"papers/{slug}/" not in llms:
            errors.append(f"top-level indices do not both link paper folder: {slug}")

        errors.extend(check_relative_links(readme_path, paper_readme))

    if dois(top_cff) != expected_dois:
        errors.append(
            f"CITATION.cff DOI set differs: expected {sorted(expected_dois)}, got {sorted(dois(top_cff))}"
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

    errors.extend(check_relative_links(ROOT / "README.md", top_readme))
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
