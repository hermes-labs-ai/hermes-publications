# hermes-publications is a DOI-anchored research index

hermes-publications is a DOI-anchored index of Hermes Labs research on AI
reliability, applied epistemology and hermeneutics, and measurement validity.
Each paper here is published, citable, and DOI-anchored on Zenodo.

Read the complete public collection at [hermes-labs.ai/research](https://hermes-labs.ai/research).

---

## Why this exists

Hermes Labs treats AI reliability not as a math problem, but as a language problem. The name derives from the Greek messenger god Hermes — the root of hermeneutics, the study of interpretation. Two old questions from philosophy sit underneath the work:

- **Epistemology** — how we know what is true. For an autonomous agent it's operational: when a model produces a claim, does it track reality, and how confidently? Hallucination, miscalibrated hedging, source-credibility bias, and null-result asymmetry are *epistemic* failures — the agent failing to know what it knows.

- **Hermeneutics** — how meaning is interpreted and communicated. For an autonomous agent it's operational: when a model reads an instruction, context window, or tool description, what does it take it to mean — and does that meaning survive across turns, tools, and hand-offs? Silent instruction relaxation, multi-turn drift, and constraint evasion are *hermeneutic* failures — meaning failing to be preserved.

Both are language questions.

The Hermes Labs position: **the model is the substrate** — the trained system, the parameters, the capability ceiling. But **language is the operations layer** — the prompts, scaffolds, evals, memory layers, and audit surfaces running on top. The substrate is changeable in principle (fine-tuning, distillation, RLHF) and fixed in deployment. The operations layer is the lever — where deployed reliability is won or lost, and it's made of language.

We call the discipline **Epistemic Engineering**: engineering an autonomous agent's epistemic and hermeneutic behavior — calibration, evidence handling, preservation of meaning — at the language operations layer. Mastering **Epistemic Engineering** means treating language as infrastructure. Hermes Labs publications focus on **applied epistemology and hermeneutics** in this sense: empirical studies of how agents fail epistemically and hermeneutically, and the **linguistic infrastructure** that closes those failures.

---

## Publications

### 1. The Asymmetric Burden of Proof
**LLMs Show a Null-Result Asymmetry in a Matched-Vignette Benchmark**
Bosch, R. (2026). DOI: [10.5281/zenodo.18867694](https://doi.org/10.5281/zenodo.18867694)

Matched-pair experiments testing whether three frontier LLMs (GPT-4o, GPT-5.2 Thinking, Claude Haiku 4.5) apply symmetric evidential standards to positive and null scientific claims. Across all six model-format conditions, models allocated less conclusion-consistent probability mass to null claims than to matched positive claims (gaps of 19.6–56.7 percentage points; all bootstrap 95% CIs excluding zero). Directionally consistent in 23 of 24 pair-condition cells. The asymmetry persists even when categorical labels collapse, surfacing through probability allocation. Implications for evidence synthesis, safety assessment, and decision-support pipelines that rely on LLM-generated confidence scores.

[`papers/asymmetric-burden-of-proof/`](papers/asymmetric-burden-of-proof/)

Paper-specific archival repository:
[hermes-labs-ai/the-asymmetric-burden-of-proof](https://github.com/hermes-labs-ai/the-asymmetric-burden-of-proof)

### 2. A Taxonomy of Epistemic Failure Modes in Large Language Models
Bosch, R. (2026). DOI: [10.5281/zenodo.19042469](https://doi.org/10.5281/zenodo.19042469)

Bottom-up analysis of 1,461 controlled experiments identifies seven structural failure modes distinct from hallucination: (1) Null-Result Asymmetry, (2) Source-Status Credibility Bias, (3) Agency Dissolution, (4) Performative Hedging, (5) Constraint Evasion, (6) Silent Instruction Relaxation, and (7) Controversy-Truth Conflation. Each mode is defined mechanistically, illustrated with experimental evidence, and assessed for downstream consequences. A common pattern emerges: models track surface-level signals — prestige markers, hedging vocabulary, controversy language, banned word lists — rather than the semantic content those signals are supposed to index.

[`papers/epistemic-failure-taxonomy/`](papers/epistemic-failure-taxonomy/)

Paper-specific archival repository:
[hermes-labs-ai/taxonomy-of-epistemic-failure-modes](https://github.com/hermes-labs-ai/taxonomy-of-epistemic-failure-modes)

### 3. Precise Records, Unstable Meanings
**Measurement Validity and Unsupported Claims Derived from AI Agent Telemetry**
Bosch, R. (2026). DOI: [10.5281/zenodo.21652317](https://doi.org/10.5281/zenodo.21652317)

A naturalistic twelve-week audit asks what operational telemetry can actually
support us in claiming about sessions, tasks, outcomes, behavior, and failure.
The paper separates valid record-level measurements from unsupported
construct-level interpretations and introduces a Telemetry-to-Claim Gate for
provenance, analytical unit, construct, population, window, denominator,
validation, and sensitivity. It does not turn file spans, ledger entries, or
detector-positive rates into task duration, successful outcomes, or failure
prevalence without independent evidence.

[`papers/precise-records-unstable-meanings/`](papers/precise-records-unstable-meanings/)

Paper-specific archival repository:
[hermes-labs-ai/precise-records-unstable-meanings](https://github.com/hermes-labs-ai/precise-records-unstable-meanings)

### 4. The Generative Horizon
**Applied Hermeneutics, Linguistic Attractors, and the Limits of Model Self-Report**
Bosch, R. (2026). DOI: [10.5281/zenodo.21659634](https://doi.org/10.5281/zenodo.21659634)

A conceptual paper on how a represented linguistic situation becomes operative
in the same computation that produces a language model's next representation.
It distinguishes the present generative horizon from recursive interpretive
conditioning across retained outputs, and translates applied hermeneutics into
requirements for provenance, status, revision, and authority. It does not
attribute an inner observer, privileged access, or phenomenal awareness to
language models.

[`papers/generative-horizon/`](papers/generative-horizon/)

Paper-specific archival repository:
[hermes-labs-ai/the-generative-horizon](https://github.com/hermes-labs-ai/the-generative-horizon)

### 5. Behavioral Canarying for Prompt Injection
**Powerless Model Probes with Explicit Coverage Semantics**
Bosch, R. (2026). DOI: [10.5281/zenodo.21818565](https://doi.org/10.5281/zenodo.21818565)

A technical note describing behavioral canarying: deliberately exposing a
powerless language model to untrusted input and treating its response as
pre-execution evidence, with routing disposition kept explicitly separate
from inspection coverage so a fail-open route can never be read as a clean
measurement. Reports no aggregate detection or false-positive rate for the
current release.

[`papers/behavioral-canarying/`](papers/behavioral-canarying/)

Operationalizing tool repository:
[hermes-labs-ai/little-canary](https://github.com/hermes-labs-ai/little-canary)

### 6. Tool Differentia
**Relational Static Analysis for AI Agent Tool Descriptions**
Bosch, R. (2026). DOI: [10.5281/zenodo.21817244](https://doi.org/10.5281/zenodo.21817244)

A deterministic, pre-runtime static analysis (LintLang H1.6) that flags when
two individually valid tool definitions jointly fail to provide distinguishing
information for an agent to select between them. Makes no model or network
calls; a clean result does not establish runtime selection correctness.

[`papers/tool-differentia/`](papers/tool-differentia/)

Operationalizing tool repository:
[hermes-labs-ai/lintlang](https://github.com/hermes-labs-ai/lintlang)

---

## How to cite

Each paper folder contains a `CITATION.cff` and a citation block in its README. The canonical home for each paper is the Zenodo DOI; this repository aggregates metadata, plain-language summaries, and pointers to the tools that operationalize the findings.

## Machine-readable reuse

- [`publications.json`](publications.json) is the single structured identity
  source for the publication program: title, DOI, date, evidence role, license,
  citation key, folder slug, and archival repository.
- [`publications.jsonld`](publications.jsonld) exposes the same identities as a
  Schema.org `ItemList` of `ScholarlyArticle` records for search and answer
  engines.
- [`CITATION.bib`](CITATION.bib) is the generated aggregate BibTeX export.
- [`atom.xml`](atom.xml) is the deterministic Atom 1.0 publication feed,
  ordered newest-first for feed readers and scholarly discovery agents.

Regenerate the derived exports with `python3 scripts/render_exports.py`; CI
fails when any generated file is stale.

Before a release-facing update, run `python3 scripts/verify_zenodo.py` for a
bounded live comparison of every manifest title, DOI, date, license, and author
ORCID against the canonical Zenodo API records.

## Tools that operationalize this research

The findings here drive the open-source reliability infrastructure published under [hermes-labs-ai](https://github.com/hermes-labs-ai). Cross-references appear in each paper folder.

## Author

Rolando (Roli) Bosch · Hermes Labs · [hermes-labs.ai](https://hermes-labs.ai) · roli@hermes-labs.ai

## License

Paper texts are governed by the Zenodo deposit license for each work (CC-BY 4.0). Repository scaffolding (this README, llms.txt, AGENTS.md, per-paper READMEs) is MIT.
