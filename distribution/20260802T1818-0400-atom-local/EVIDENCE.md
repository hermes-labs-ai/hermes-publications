# Evidence ledger — local Atom implementation

| ID | Observation | Class | Exact source | Status / scope limit |
|---|---|---|---|---|
| E-012 | A deterministic Atom 1.0 feed is generated from the four-paper manifest. DOI URLs remain stable entry IDs and `related` links; `alternate` links point to human-readable Hermes research pages. | `CONFIRMED_LOCAL` | `scripts/render_exports.py`; `atom.xml` SHA-256 `b4012e349550ad3396d2c76726dfc72280cf6e3252b11e03a46fcfeafd38026b` | Local working tree only; no public endpoint claim. Supersedes only the local-generation part of E-010. Landing-page links are ordinary feed semantics, not Crossref optimization. |
| E-013 | Export checks, publication consistency, unit tests, XML parsing, and whitespace checks passed. | `CONFIRMED_LOCAL` | `python3 scripts/render_exports.py --check`; `python3 scripts/check_publications.py`; `python3 -m unittest discover -s tests`; `xmllint --noout atom.xml`; `git diff --check` | 3 exports current; 4 papers consistent; 14 tests. Local verification only. |
| E-014 | An agent-oriented four-paper discovery copy kit is prepared with explicit non-deployment boundaries. | `CONFIRMED_LOCAL` | `distribution/assets/four-paper-discovery-kit-20260802.md`; SHA-256 `935c6fda509d229075a24af712528aa2460144e792f6b3fb7955b1b7f16b186c` | Prepared copy, not approval, live state, or effect evidence. |
| E-015 | The Precise Records snippet's `41,495 transcript files` statement was traced to the canonical paper source during independent read-only support. | `CONFIRMED_LOCAL_SOURCE_TRACE` | Canonical Precise Records source referenced by `publications.json`; coordination task `019fc43b-bd63-75e1-86c1-ec93918abd0b` | Source trace only; not a new paper result. |
| E-016 | The earlier Crossref Event Data follow-on rationale is obsolete and retracted. Crossref states that Event Data was sunset and unavailable from 2026-04-23. | `CONFIRMED_EXTERNAL_SUPERSESSION` | Crossref, “Strengthening support for data citations—and saying goodbye to Event Data,” https://www.production.crossref.org/blog/strengthening-support-for-data-citations-and-saying-goodbye-to-event-data/; coordination correction from task `019fc43b-bd63-75e1-86c1-ec93918abd0b` | No Event Data optimization, onboarding request, compatibility claim, or expected ingestion effect remains licensed. |

## Supersession

- E-012 supersedes E-010 only for whether a local Atom generator/export exists.
- E-010 remains current at its cutoff for the missing public endpoint.
- E-014 does not alter any distribution-channel state.
- E-016 supersedes and retracts the earlier coordination suggestion to optimize
  the Atom feed or request onboarding for Crossref Event Data.

PARKED: no public effect is licensed by this ledger.
