# Continuation protocol for agents

Use this protocol when extending Hermes Labs paper-distribution knowledge.

## Before adding anything

1. Verify the current repository path, branch, SHA, dirty state, and ownership.
2. Read [`../SNAPSHOT.md`](SNAPSHOT.md), [`STATUS.md`](STATUS.md), and
   [`EVIDENCE.md`](EVIDENCE.md).
3. Read the current operational handoff under
   `/Users/rbr_lpci/Documents/oth/distribution/` and check
   `/Users/rbr_lpci/.config/hermes/supersession-pointers.json`.
4. Confirm that no newer receipt or public readback already answers the proposed
   question.
5. Revalidate only the narrow open item being advanced. Do not restart the
   30-source channel inventory without a materially new research question.

## Evidence classes

- `CONFIRMED_LOCAL` — directly supported by an exact local artifact, field,
  commit, or hash.
- `CONFIRMED_PUBLIC_READBACK` — directly observed at an exact URL with retrieval
  time and result.
- `OWNER_STATED` — an owner instruction or authorization; not independent proof.
- `INFERRED` — an interpretation derived from evidence; never present it as a
  fact.
- `UNKNOWN` or `UNEVALUATED` — not checked, unavailable, blocked, rate-limited,
  or insufficiently reconciled.

## Add one finding

Record this minimum payload:

```text
finding_id:
statement:
evidence_class:
exact_source:
captured_at_utc:
scope_limit:
supersedes: NONE | <finding_id>
public_effect: NONE
next_condition:
```

Local evidence needs an absolute path plus a field, commit, or SHA when useful.
Public evidence needs the exact URL, retrieval timestamp, and literal readback.
A DOI or URL by itself is a pointer, not proof of current state.

## Preserve history

- Do not edit an old timestamped snapshot to make it look current.
- When material evidence changes, create a newer sibling snapshot with
  `SNAPSHOT.md`, `STATUS.md`, and `EVIDENCE.md`, then update
  `distribution/README.md` to point to it.
- State the exact older finding that is superseded and why.
- If evidence conflicts without resolution, retain both observations and mark
  the conclusion `UNKNOWN` or `UNEVALUATED`.

## Public-effect boundary

Default to `public_effect: NONE`. Local research, drafting, validation, code,
and review do not authorize sending, posting, submitting, pushing, deploying,
publishing, changing a profile, or creating a release.

A future public action requires:

1. exact target;
2. exact content, commit, or payload;
3. explicit owner authorization for that exact effect; and
4. one post-action public readback.

## End each continuation

End with exactly one:

- `NEXT: <single bounded read-only or local action>`
- `WAITING: <external dependency and last checked time>`
- `PARKED: <exact owner action required>`
- `NO_NEXT_ACTION: <reason>`
