# Security Policy

## Scope

hermes-publications is a metadata and citation index: JSON, JSON-LD, BibTeX,
and Atom export files, per-paper Markdown, and small Python scripts
(`scripts/render_exports.py`, `scripts/verify_zenodo.py`,
`scripts/check_publications.py`) that regenerate and check those exports
against the canonical Zenodo records. It has no running service, no user
input surface, and no network listener.

## Reporting a Vulnerability

If you find a security issue in the generation or verification scripts, or a
supply-chain concern in this repository, please report it responsibly.

**Do not open a public issue for security vulnerabilities.**

Instead, email us at: **roli@hermes-labs.ai**

Include:
- A description of the issue.
- Steps to reproduce it.
- Any relevant logs or output.

## Response Timeline

- **Acknowledgment**: within 48 hours of your report.
- **Assessment**: within 7 days we will confirm the issue and outline next steps.
- **Fix**: we aim to land a fix within 30 days of confirmation.

There is no uptime or availability SLA: this repository is a data index, not
a running service.

## Supported Versions

Security fixes are applied to the latest commit on the default branch only.

Thank you for helping keep this index trustworthy.
