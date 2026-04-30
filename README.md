# Hermes Labs — Publications

Research publications from Hermes Labs on **epistemic engineering**, the study and engineering of how language models reason, hedge, and represent evidence. Each paper here is published, citable, and DOI-anchored on Zenodo.

---

## Why this exists

Hermes Labs is named for Hermes, the Greek messenger god — patron of communication and interpretation, the herald who carries meaning between worlds. The thread to the work: **hermeneutics**, the theory of interpretation that takes its name from Hermes, is the philosophical anchor for an AI infrastructure company whose substrate is linguistic.

The thesis: **language sets capability.** The neural model is the ceiling, not the source. Reliability, interpretation, and epistemic discipline are properties of the linguistic infrastructure that wraps the model — the prompts, scaffolds, evals, memory layers, and audit surfaces. Hermes Labs publications study and engineer that substrate.

Two framings are repeated across this work:

- **Epistemic Engineering** — the foundational thesis. Language dictates capability and intelligence; the model is the ceiling, the linguistic substrate is the source of behavior. Reliability is an engineering problem of linguistic infrastructure, not weight tuning.
- **Hermeneutic Engineering** — the operational corollary. Where Epistemic Engineering names the *what* (language as substrate of reasoning), Hermeneutic Engineering names the *how* (designing interpretive scaffolds, evidence-first evaluation, structured drift recovery, and audit trails so meaning is preserved across an autonomous-agent pipeline).

---

## Publications

### 1. The Asymmetric Burden of Proof
**LLMs Show a Null-Result Asymmetry in a Matched-Vignette Benchmark**
Bosch, R. (2026). DOI: [10.5281/zenodo.18867694](https://doi.org/10.5281/zenodo.18867694)

Matched-pair experiments testing whether three frontier LLMs (GPT-4o, GPT-5.2 Thinking, Claude Haiku 4.5) apply symmetric evidential standards to positive and null scientific claims. Across all six model-format conditions, models allocated less conclusion-consistent probability mass to null claims than to matched positive claims (gaps of 19.6–56.7 percentage points; all bootstrap 95% CIs excluding zero). Directionally consistent in 23 of 24 pair-condition cells. The asymmetry persists even when categorical labels collapse, surfacing through probability allocation. Implications for evidence synthesis, safety assessment, and decision-support pipelines that rely on LLM-generated confidence scores.

[`papers/asymmetric-burden-of-proof/`](papers/asymmetric-burden-of-proof/)

### 2. A Taxonomy of Epistemic Failure Modes in Large Language Models
Bosch, R. (2026). DOI: [10.5281/zenodo.19042469](https://doi.org/10.5281/zenodo.19042469)

Bottom-up analysis of 1,461 controlled experiments identifies seven structural failure modes distinct from hallucination: (1) Null-Result Asymmetry, (2) Source-Status Credibility Bias, (3) Agency Dissolution, (4) Performative Hedging, (5) Constraint Evasion, (6) Silent Instruction Relaxation, and (7) Controversy-Truth Conflation. Each mode is defined mechanistically, illustrated with experimental evidence, and assessed for downstream consequences. A common pattern emerges: models track surface-level signals — prestige markers, hedging vocabulary, controversy language, banned word lists — rather than the semantic content those signals are supposed to index.

[`papers/epistemic-failure-taxonomy/`](papers/epistemic-failure-taxonomy/)

---

## How to cite

Each paper folder contains a `CITATION.cff` and a citation block in its README. The canonical home for each paper is the Zenodo DOI; this repository aggregates metadata, plain-language summaries, and pointers to the tools that operationalize the findings.

## Tools that operationalize this research

The findings here drive the open-source reliability infrastructure published under [hermes-labs-ai](https://github.com/hermes-labs-ai). Cross-references appear in each paper folder.

## Author

Rolando (Roli) Bosch · Hermes Labs · [hermes-labs.ai](https://hermes-labs.ai) · rbosch@lpci.ai

## License

Paper texts are governed by the Zenodo deposit license for each work (CC-BY 4.0). Repository scaffolding (this README, llms.txt, AGENTS.md, per-paper READMEs) is MIT.
