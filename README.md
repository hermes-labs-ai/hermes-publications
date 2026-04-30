# Hermes Labs — Publications

Research publications from Hermes Labs on **epistemic engineering**, the study and engineering of how language models reason, hedge, and represent evidence. Each paper here is published, citable, and DOI-anchored on Zenodo.

---

## Why this exists

Hermes Labs is a reliability research lab for autonomous AI agents. Two old questions from philosophy sit underneath the work:

- **Epistemology** is the study of how we know what is true. For an autonomous agent, the question becomes operational: when the model produces a claim, does it track reality, and how confidently? Hallucination, miscalibrated hedging, source-status credibility bias, and null-result asymmetry are all *epistemic* failures — failures of the agent to know what it knows.

- **Hermeneutics** is the study of how meaning is interpreted and communicated. For an autonomous agent, the question becomes: when an instruction, a context window, or a tool description is read by the model, what does the model take that to mean — and does that meaning survive across turns, tools, and hand-offs? Silent instruction relaxation, multi-turn drift, and constraint evasion are all *hermeneutic* failures — failures of meaning to be preserved.

Both questions are language questions.

The Hermes Labs position is that **the model is the substrate** — the trained system, the parameters, the capability ceiling — and **language is the operations layer**: the prompts, scaffolds, evals, contexts, memory layers, and audit surfaces that run on top of the substrate. The substrate can be changed (fine-tuning, distillation, RLHF), but for most teams, most of the time, it's fixed; the operations layer is the lever. That's where deployed reliability is won or lost, and the operations layer is made of language.

We call this discipline **Epistemic Engineering**: engineering an autonomous agent's epistemic and hermeneutic behavior — its calibration, its evidence handling, its preservation of meaning — at the language operations layer. Hermes Labs publications focus on **applied epistemology and hermeneutics** in this sense: empirical studies of how agents fail epistemically and hermeneutically, and the linguistic infrastructure that closes those failures.

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
