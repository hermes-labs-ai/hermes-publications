# Behavioral Canarying for Prompt Injection

**Powerless Model Probes with Explicit Coverage Semantics**

Bosch, R. (2026). *Zenodo technical note.*
DOI: [10.5281/zenodo.21818564](https://doi.org/10.5281/zenodo.21818564)
Current version DOI: [10.5281/zenodo.21820059](https://doi.org/10.5281/zenodo.21820059)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21818564.svg)](https://doi.org/10.5281/zenodo.21818564)

Machine-readable metadata: [JSON](../../publications.json) · [JSON-LD](../../publications.jsonld) · [BibTeX](../../CITATION.bib)

## Abstract

Prompt-injection defenses commonly classify untrusted text before it reaches an
agent, inspect a production model's output after generation, or isolate
untrusted content inside a restricted model. This note describes a
complementary pre-execution pattern: deliberately expose a powerless language
model to the untrusted input, observe the resulting response for evidence of
behavioral compromise, and route the original input according to that evidence
before an authority-bearing agent acts. The probe is sacrificial in a limited
engineering sense — it has no application tools, credentials, output
execution, or automatic path by which its free-form response gains downstream
authority.

The central contribution is not merely the auxiliary model. It is an
evidence-preserving interface that separates **routing disposition** from
**inspection coverage**, so a fail-open route taken because inspection failed
can never be conflated with a route taken because inspection ran and found
nothing. The note presents the architecture implemented in Little Canary,
distinguishes it from input classifiers, canary-token systems, and quarantined
task models, and specifies the evidence required for future performance
claims.

## Plain-language summary

Most prompt-injection defenses ask "what does this input look like?" This note
asks a different question: what does this input *do* to a small, powerless
model deliberately exposed to it? Little Canary treats that model's response
as evidence, not as an authority — and, critically, it keeps track of whether
that evidence was actually collected. A system can still fail open for
availability reasons, but it must say so explicitly rather than let "allowed
to proceed" be read as "inspected and clean."

## Evidence boundary

This note does not claim universal detection, formal security, aggregate
accuracy for the current release, or invention of the general
sacrificial-canary concept. It documents implementation evidence (state
fields, verdict semantics, failure-mode handling) and names the closest
located prior art (Sibylline Software's canary-agent design) rather than
claiming novelty over it. It reports no numeric detection or false-positive
rate for the current release; historical benchmark artifacts are retained for
regression work but are not represented as a performance certificate.

## Citation

```bibtex
@misc{bosch2026behavioralcanarying,
  author       = {Bosch, Rolando},
  title        = {Behavioral Canarying for Prompt Injection: Powerless Model
                  Probes with Explicit Coverage Semantics},
  year         = {2026},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.21818564},
  url          = {https://doi.org/10.5281/zenodo.21818564},
  note         = {Technical note}
}
```

## License

CC-BY 4.0 (per Zenodo deposit).

## Tool that operationalizes this note

[Little Canary](https://github.com/hermes-labs-ai/little-canary) is the
open-source reference implementation of the architecture described here.
