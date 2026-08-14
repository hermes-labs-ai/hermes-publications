# Precise Records, Unstable Meanings

**Measurement Validity and Unsupported Claims Derived from AI Agent Telemetry**

Bosch, R. (2026). *Zenodo preprint.*
DOI: [10.5281/zenodo.21652316](https://doi.org/10.5281/zenodo.21652316)

Current version DOI: [10.5281/zenodo.21652317](https://doi.org/10.5281/zenodo.21652317)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21652316.svg)](https://doi.org/10.5281/zenodo.21652316)

Machine-readable metadata: [JSON](../../publications.json) · [JSON-LD](../../publications.jsonld) · [BibTeX](../../CITATION.bib)

## Abstract

Agent systems are increasingly evaluated and modified through operational
telemetry. Yet precise records do not necessarily identify the sessions, tasks,
outcomes, or behaviors named by later metrics. When those interpretations guide
routing, memory, autonomy, evaluation, or redesign, measurement validity becomes
an architectural concern.

We report a naturalistic measurement-validity audit of one coding-agent
orchestration-harness deployment observed over twelve weeks. The frozen corpus
comprised 41,495 transcript files and six auxiliary telemetry streams. Each
candidate claim was examined for producer provenance, analytical unit,
construct, population, observation window, denominator, validation evidence,
and sensitivity to alternative treatments of inter-event gaps.

Across the audited mappings, valid record-level quantities did not support
several broader construct-level interpretations. Transcript-file event spans
produced a file-level distribution but no validated measure of logical-session
or task duration; 46 of 87 files spanning more than eight hours fell below that
threshold after removal of their largest internal gap. Of 28,055 claims-ledger
rows, 27,938 were automatic retrieval-reflex events; the remaining 117
heterogeneous entries did not establish completed tasks or correct outcomes. An
anomaly instrument flagged approximately 65% of scored turns, but without
independent behavioral labels this was an instrument-positive rate, not an
estimate of failure prevalence.

The study provides an empirical account of how record-level measures change at
the claim layer and proposes a Telemetry-to-Claim Gate for documenting producer,
unit, construct, population, window, denominator, validation, and sensitivity
before telemetry is used in evaluation, governance, or system redesign.

## Plain-language summary

Telemetry can be arithmetically precise while its interpretation is unsupported.
A file timestamp can measure the span of a file without measuring a session. A
ledger entry can prove that an instrument wrote a record without proving a task
was completed. A detector can count its own positive outputs without measuring
the prevalence of real failures. Before an operational number guides evaluation,
governance, or redesign, the paper's gate makes the missing evidentiary links
explicit.

## Evidence boundary

The study describes one evolving deployment and does not estimate population
effects beyond it. The empirical paper and its conceptual companion, [The
Generative Horizon](../generative-horizon/), address related but distinct
questions; neither is presented as validating the other.

## Citation

```bibtex
@misc{bosch2026preciserecords,
  author       = {Bosch, Rolando},
  title        = {Precise Records, Unstable Meanings: Measurement Validity and
                  Unsupported Claims Derived from AI Agent Telemetry},
  year         = {2026},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.21652316},
  url          = {https://doi.org/10.5281/zenodo.21652316},
  note         = {Preprint}
}
```

## License

CC-BY 4.0 (per Zenodo deposit).

## Archival repository

The paper, supplementary evidence package, citation metadata, checksums, and
provenance boundary are at
<https://github.com/hermes-labs-ai/precise-records-unstable-meanings>.
