#!/usr/bin/env python3
"""Compare publications.json identities with their canonical Zenodo records."""

from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request

if __package__:
    from .render_exports import load_manifest
else:
    from render_exports import load_manifest


API_ROOT = "https://zenodo.org/api/records"


def fetch_record(doi: str, timeout: float) -> dict:
    record_id = doi.rsplit(".", 1)[-1]
    request = urllib.request.Request(
        f"{API_ROOT}/{record_id}",
        headers={"User-Agent": "hermes-publications-verify/1"},
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return json.loads(response.read().decode("utf-8"))


def compare(paper: dict, record: dict, author_orcid: str) -> list[str]:
    metadata = record.get("metadata", {})
    creators = metadata.get("creators", [])
    observed_orcids = {creator.get("orcid") for creator in creators}
    expected = {
        "doi": paper["doi"],
        "title": paper["title"],
        "publication_date": paper["publication_date"],
        "publication_type": paper["publication_type"],
        "license": paper["license"].lower(),
        "orcid": author_orcid,
    }
    observed = {
        "doi": record.get("doi"),
        "title": metadata.get("title"),
        "publication_date": metadata.get("publication_date"),
        "publication_type": (metadata.get("resource_type") or {}).get("subtype"),
        "license": (metadata.get("license") or {}).get("id", "").lower(),
        "orcid": expected["orcid"] if expected["orcid"] in observed_orcids else None,
    }
    return [
        f"{paper['slug']}: {field} expected {value!r}, got {observed[field]!r}"
        for field, value in expected.items()
        if observed[field] != value
    ]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--timeout", type=float, default=15.0)
    args = parser.parse_args()

    try:
        data = load_manifest()
    except (OSError, ValueError, json.JSONDecodeError) as exc:
        print(f"FAIL: {exc}", file=sys.stderr)
        return 1

    errors: list[str] = []
    author_orcid = data["author"]["orcid"].rsplit("/", 1)[-1]
    for paper in data["papers"]:
        try:
            record = fetch_record(paper["doi"], args.timeout)
        except (OSError, UnicodeError, urllib.error.URLError, json.JSONDecodeError) as exc:
            errors.append(f"{paper['slug']}: Zenodo lookup failed: {exc}")
            continue
        errors.extend(compare(paper, record, author_orcid))

    if errors:
        for error in errors:
            print(f"FAIL: {error}", file=sys.stderr)
        return 1
    print(f"PASS: {len(data['papers'])} manifest identities match canonical Zenodo records")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
