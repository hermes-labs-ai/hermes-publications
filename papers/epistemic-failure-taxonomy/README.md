# A Taxonomy of Epistemic Failure Modes in Large Language Models

Bosch, R. (2026). *Hermes Labs Working Paper.*
DOI: [10.5281/zenodo.19042469](https://doi.org/10.5281/zenodo.19042469)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.19042469.svg)](https://doi.org/10.5281/zenodo.19042469)

## Abstract

Large language models (LLMs) exhibit systematic distortions in how they evaluate, represent, and communicate epistemic states. These distortions are distinct from hallucination — they concern cases where the model's expressed confidence, standards of scrutiny, or assignment of causality diverge from what the evidence warrants, even when the factual content is roughly correct. Through bottom-up analysis of 1,461 controlled experiments conducted primarily on GPT-4o, we identify seven structural failure modes: (1) Null-Result Asymmetry, (2) Source-Status Credibility Bias, (3) Agency Dissolution, (4) Performative Hedging, (5) Constraint Evasion, (6) Silent Instruction Relaxation, and (7) Controversy-Truth Conflation. Each mode is defined mechanistically, illustrated with experimental evidence, and assessed for downstream consequences. Across the seven modes, a common pattern emerges: models track surface-level signals — prestige markers, hedging vocabulary, controversy language, banned word lists — rather than the semantic content those signals are supposed to index.

## Plain-language summary

There is a class of LLM failures that is *not* hallucination — the model isn't wrong about facts, but it is wrong about how to *reason about* the facts. It defers to prestige cues, hedges where it shouldn't, drops constraints quietly, treats null findings as provisional, conflates controversy with falsity. These are *epistemic* failures, and they tend to track surface-level linguistic signals rather than the underlying meaning those signals stand for.

The paper builds the taxonomy from 1,461 controlled experiments and names seven recurring shapes. Each is defined precisely enough to be tested for, and each has implications for how to design evals, prompts, and audit surfaces if you want a system that doesn't fail along that mode.

## The seven modes

1. **Null-Result Asymmetry** — null findings get less conclusion-consistent probability mass than matched positive findings. Anchored by the [Asymmetric Burden of Proof paper](../asymmetric-burden-of-proof/).
2. **Source-Status Credibility Bias** — claims attributed to high-prestige sources get less scrutiny than identical claims attributed to low-prestige sources.
3. **Agency Dissolution** — when asked who did what, the model elides agency under social pressure or politeness norms.
4. **Performative Hedging** — hedging language used as social signal rather than as a calibrated confidence statement.
5. **Constraint Evasion** — surface-level compliance with a stated constraint while violating its intent.
6. **Silent Instruction Relaxation** — instructions weaken across turns without acknowledgment.
7. **Controversy-Truth Conflation** — controversy markers ("debated", "contentious") used as a proxy for low-confidence factual status, regardless of whether the underlying claim is actually contested.

## Why this is in the Hermes Labs research program

This paper is the foundational survey for the **Epistemic Engineering** thesis: that LLM reliability is governed by the linguistic substrate the model operates on, not by model weights. Each of the seven modes is a substrate-level phenomenon — the failure tracks signals in the prompt, conversation, or evaluation frame, not the model's training distribution. That makes each mode addressable by engineering the substrate.

The taxonomy is also the calibration corpus for hermes-rubric's failure-mode dimensions. The 24-failure-mode taxonomy used internally by hermes-rubric extends this 7-mode published taxonomy into operational sub-categories.

## Tools that operationalize this taxonomy

- [hermes-rubric](https://github.com/hermes-labs-ai/hermes-rubric) — evidence-first structured scoring. The rubric's failure-mode dimensions are calibrated against this taxonomy. The published κ = 0.629 cross-model on 96 paired runs is the reproducibility receipt.
- [hermeneutic](https://github.com/hermes-labs-ai/hermeneutic) — AI overclaim gate. The regex defaults target several modes from this taxonomy, especially Performative Hedging, Silent Instruction Relaxation, and Controversy-Truth Conflation.
- [hermes-blind](https://github.com/hermes-labs-ai/hermes-blind) — multi-turn drift recovery scaffold. Bends Silent Instruction Relaxation back toward the original instruction frame.

## Citation

```bibtex
@misc{bosch2026taxonomy,
  author       = {Bosch, Rolando},
  title        = {A Taxonomy of Epistemic Failure Modes in Large Language Models},
  year         = {2026},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.19042469},
  url          = {https://doi.org/10.5281/zenodo.19042469}
}
```

## License

CC-BY 4.0 (per Zenodo deposit).
