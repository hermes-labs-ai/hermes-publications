# Four-paper discovery copy kit

```text
state: PREPARED_COPY_NOT_DEPLOYED
prepared_at: 2026-08-02
public_effect: NONE
```

## Intended use

This is reusable, source-bound copy for an agent preparing a specific owned
Hermes discovery surface: a canonical paper page, the `/proof` collection, or a
paper repository README. It prevents each agent from re-summarizing the papers
and gives the four publications a coherent reader journey.

It is **not** the canonical paper index, a distribution-status snapshot, an
authorization to edit a public surface, or evidence that the copy will increase
views, downloads, citations, or adoption. Before use, verify the exact target
and current paper identity against `../../publications.json`. Public edits,
pushes, and deployments require their own exact authorization.

Use only the components needed for the named surface. Do not deploy this kit in
bulk merely because it exists.

## The Generative Horizon

**Exact title:** *The Generative Horizon: Applied Hermeneutics, Linguistic Attractors, and the Limits of Model Self-Report*
**DOI:** [10.5281/zenodo.21659634](https://doi.org/10.5281/zenodo.21659634)
**Record:** [Zenodo 21659634](https://zenodo.org/records/21659634)
**Canonical page:** [hermes-labs.ai/research/the-generative-horizon](https://hermes-labs.ai/research/the-generative-horizon)

**Discovery snippet**

> Language-model agents interpret and generate through a situated linguistic
> field shaped by instructions, memory, tools, summaries, and corrections. The
> paper turns that condition into concrete requirements for provenance,
> revision, status, and evidential authority.

**Reader / use-case:** An AI systems researcher designing agent memory, model
self-report, reasoning-trace, or interpretability workflows who needs clear
boundaries for when a representation may govern later action.

**CTA:** Read the paper, then use its provenance, status, revision, and
authority questions to review one representation your system currently treats
as evidence.

**Read next:** [*Precise Records, Unstable Meanings*](https://hermes-labs.ai/research/precise-records-unstable-meanings)
— it moves from the conceptual problem of interpretation and authority to an
empirical audit of what operational telemetry can support, without claiming
that either paper validates the other.

## Precise Records, Unstable Meanings

**Exact title:** *Precise Records, Unstable Meanings: Measurement Validity and Unsupported Claims Derived from AI Agent Telemetry*
**DOI:** [10.5281/zenodo.21652317](https://doi.org/10.5281/zenodo.21652317)
**Record:** [Zenodo 21652317](https://zenodo.org/records/21652317)
**Canonical page:** [hermes-labs.ai/research/precise-records-unstable-meanings](https://hermes-labs.ai/research/precise-records-unstable-meanings)

**Discovery snippet**

> Agent logs can be exact and still fail to measure sessions, tasks, outcomes,
> or failure. A twelve-week audit of 41,495 transcript files shows where
> operational telemetry overreaches—and introduces an eight-part gate for
> defensible claims.

**Reader / use-case:** An agent-observability or evaluation lead deciding
whether transcripts, ledger events, anomaly scores, traces, or timestamps
genuinely measure task completion, outcomes, behavior, or failure.

**CTA:** Read the measurement audit and apply the Telemetry-to-Claim Gate before
using one operational metric in evaluation, governance, or system redesign.

**Read next:** [*A Taxonomy of Epistemic Failure Modes in Large Language Models*](https://hermes-labs.ai/research/taxonomy-of-epistemic-failure-modes)
— it broadens the audit lens from unsupported telemetry claims to seven ways
plausible model outputs can distort the epistemic layer around facts.

## The Asymmetric Burden of Proof

**Exact title:** *The Asymmetric Burden of Proof: LLMs Show a Null-Result Asymmetry in a Matched-Vignette Benchmark*
**DOI:** [10.5281/zenodo.18867694](https://doi.org/10.5281/zenodo.18867694)
**Record:** [Zenodo 18867694](https://zenodo.org/records/18867694)
**Canonical page:** [hermes-labs.ai/research/the-asymmetric-burden-of-proof](https://hermes-labs.ai/research/the-asymmetric-burden-of-proof)

**Discovery snippet**

> Across matched scientific studies, three tested LLMs gave less
> conclusion-consistent probability to null findings than equivalent positive
> findings—even when categorical labels looked similar—showing how AI evidence
> systems can quietly underweight high-quality negative evidence.

**Reader / use-case:** A researcher or assurance team evaluating LLM-supported
evidence synthesis, systematic review, safety assessment, or decision support
where negative evidence must receive the same scrutiny as positive evidence.

**CTA:** Read the benchmark before deciding whether label-only monitoring is
sufficient for an LLM workflow that interprets scientific findings.

**Read next:** [*A Taxonomy of Epistemic Failure Modes in Large Language Models*](https://hermes-labs.ai/research/taxonomy-of-epistemic-failure-modes)
— it places null-result asymmetry inside a broader seven-mode map of silent
epistemic failures relevant to deployed systems.

## A Taxonomy of Epistemic Failure Modes

**Exact title:** *A Taxonomy of Epistemic Failure Modes in Large Language Models*
**DOI:** [10.5281/zenodo.19042469](https://doi.org/10.5281/zenodo.19042469)
**Record:** [Zenodo 19042469](https://zenodo.org/records/19042469)
**Canonical page:** [hermes-labs.ai/research/taxonomy-of-epistemic-failure-modes](https://hermes-labs.ai/research/taxonomy-of-epistemic-failure-modes)

**Discovery snippet**

> Drawing on 1,461 controlled experiments, this paper organizes seven silent
> epistemic failure modes in which models can remain factually plausible while
> distorting uncertainty, evidence, source credibility, accountability,
> constraints, causality, or controversy.

**Reader / use-case:** A model-evaluation, governance, compliance,
incident-review, or high-stakes communications team that needs a practical
vocabulary for failures that may remain invisible to factuality and crash-rate
checks.

**CTA:** Read the taxonomy and use its seven modes as an audit checklist for one
LLM-assisted decision or evidence workflow.

**Read next:** [*The Asymmetric Burden of Proof*](https://hermes-labs.ai/research/the-asymmetric-burden-of-proof)
— it provides a matched-vignette benchmark focused on one taxonomy mode,
including probability-level behavior that broad labels can conceal.

## Recommended owned-surface order

1. Canonical paper pages: use the matching snippet, reader/use-case, CTA, and
   one `Read next` link.
2. The Hermes `/proof` collection: use four compact cards, pairing the
   measurement/hermeneutics papers and the benchmark/taxonomy papers.
3. Canonical paper repositories: use a short `For readers` block with the
   snippet, canonical-page CTA, and one cross-paper link.

These are candidate placements, not authorized changes. Their existence does
not supersede a newer distribution snapshot or destination-specific evidence.

## Source boundary

- Canonical identities and paper summaries: `../../publications.json`
- Current partial distribution state: `../20260802T1751-0400-partial/`
- Operational distribution truth: `/Users/rbr_lpci/Documents/oth/distribution/`
