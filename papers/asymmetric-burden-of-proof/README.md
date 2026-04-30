# The Asymmetric Burden of Proof

**LLMs Show a Null-Result Asymmetry in a Matched-Vignette Benchmark**

Bosch, R. (2026). *Hermes Labs Working Paper.*
DOI: [10.5281/zenodo.18867694](https://doi.org/10.5281/zenodo.18867694)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.18867694.svg)](https://doi.org/10.5281/zenodo.18867694)

## Abstract

We report matched-pair experiments testing whether large language models apply symmetric evidential standards to positive and null scientific claims. Three models (GPT-4o, GPT-5.2 Thinking, Claude Haiku 4.5) evaluated fictional scientific vignettes in which evidence quality was held constant while only the conclusion direction was reversed. Across all six model-format conditions, models allocated less conclusion-consistent probability mass to null claims than to matched positive claims (gaps of 19.6–56.7 percentage points; all bootstrap 95% CIs excluding zero). The asymmetry was directionally consistent in 23 of 24 pair-condition cells and persisted even when discrete classification labels collapsed entirely, surfacing through probability allocation rather than categorical commitment. We characterize this as an asymmetric burden of proof: models treat non-detection as more provisional than matched detection claims, with implications for evidence synthesis, safety assessment, and decision-support pipelines that rely on LLM-generated confidence scores.

## Plain-language summary

If you ask three frontier LLMs to evaluate two scientific vignettes that are identical except one concludes "we found an effect" and the other concludes "we found no effect," the models systematically credit the positive conclusion more than the null one. This holds even when the underlying evidence quality is held constant. The gap is large (up to 56.7 percentage points), it appears in 23 of 24 pair-condition cells, and it shows up in probability allocation even when the categorical labels are forced to be the same.

This matters anywhere LLMs are used to summarize evidence, score safety claims, or rank confidence: the model is not neutral about which direction the evidence points. Null results — the kind that often anchor safety assessments — get a quieter hearing than they should.

## Why this is in the Hermes Labs research program

The asymmetric-burden finding is one of the seven structural failure modes catalogued in the [Taxonomy paper](../epistemic-failure-taxonomy/) (mode 1: Null-Result Asymmetry). The two papers are best read together: this one is the matched-vignette experimental anchor, the Taxonomy is the broader bottom-up survey that places it among six related modes.

This is also the empirical foundation for the **Epistemic Engineering** thesis: the asymmetry is a property of how the model interprets the linguistic frame of a claim, not of its underlying world model. Different framings of the same evidence yield different confidence outputs. That makes confidence outputs *substrate phenomena* — engineerable.

## Tools that operationalize this finding

- [hermes-rubric](https://github.com/hermes-labs-ai/hermes-rubric) — evidence-first structured scoring. The rubric forces explicit evidence citations before any number is produced, and its hedge mechanism is calibrated against modes including Null-Result Asymmetry. Cohen's κ = 0.629 cross-model on 96 paired runs.
- [hermeneutic](https://github.com/hermes-labs-ai/hermeneutic) — AI overclaim gate. Catches drift in outgoing assistant drafts, including the completion-with-quantifier pattern that surfaces this asymmetry in operational pipelines.

## Citation

```bibtex
@misc{bosch2026asymmetric,
  author       = {Bosch, Rolando},
  title        = {The Asymmetric Burden of Proof: LLMs Show a Null-Result
                  Asymmetry in a Matched-Vignette Benchmark},
  year         = {2026},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.18867694},
  url          = {https://doi.org/10.5281/zenodo.18867694}
}
```

## License

CC-BY 4.0 (per Zenodo deposit).
