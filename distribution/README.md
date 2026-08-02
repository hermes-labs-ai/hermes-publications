# Paper distribution workspace

This folder gives agents a small, evidence-bound entry point into Hermes Labs
paper-distribution work.

It is deliberately **not** the complete or canonical distribution state. Each
snapshot records only what one agent or agent group established by its cutoff
time. Older snapshots remain historical evidence; newer evidence may supersede
them.

## Current snapshot

- [2026-08-02 18:42 EDT local website integration](20260802T1842-0400-atom-site-local/SNAPSHOT.md)
- [Website integration status](20260802T1842-0400-atom-site-local/STATUS.md)
- [Website integration evidence](20260802T1842-0400-atom-site-local/EVIDENCE.md)

Prior snapshots:

- [2026-08-02 18:18 EDT local Atom implementation](20260802T1818-0400-atom-local/SNAPSHOT.md)
- [Local implementation status](20260802T1818-0400-atom-local/STATUS.md)
- [Local implementation evidence](20260802T1818-0400-atom-local/EVIDENCE.md)
- [Continuation protocol](20260802T1751-0400-partial/CONTINUE.md)

- [2026-08-02 17:51 EDT partial distribution reconstruction](20260802T1751-0400-partial/SNAPSHOT.md)

## Prepared copy assets

- [Four-paper discovery copy kit](assets/four-paper-discovery-kit-20260802.md)
  — reusable snippets, reader/use-cases, calls to action, and cross-paper links
  for a specifically authorized owned surface. State:
  `PREPARED_COPY_NOT_DEPLOYED`; public effect: `NONE`.

## Authority order

When sources disagree, use this order:

1. Current public readback for the exact DOI, URL, or external record.
2. Canonical publication identity in [`../publications.json`](../publications.json)
   and the corresponding Zenodo DOI record.
3. Current operational receipts and handoffs under
   `/Users/rbr_lpci/Documents/oth/distribution/`.
4. The newest timestamped snapshot in this folder.
5. Older snapshots and inherited notes, which are leads rather than current
   truth until revalidated.

Also check `/Users/rbr_lpci/.config/hermes/supersession-pointers.json` before
using a load-bearing Hermes claim.

## Boundaries

- Do not copy PDFs, manuscripts, generated citation exports, dashboards, owner
  cards, or full operational receipts into this folder.
- Do not silently rewrite an older snapshot. Add a newer timestamped snapshot
  and state what it supersedes.
- Preserve `UNKNOWN`, `WAITING`, `HOLD`, `UNEVALUATED`, and `NOT_ESTIMABLE`
  until exact evidence resolves them.
- Local research and preparation do not authorize a push, deployment, post,
  email, submission, profile change, or other public effect.
