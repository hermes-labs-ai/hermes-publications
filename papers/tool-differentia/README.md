# Tool Differentia

**Relational Static Analysis for AI Agent Tool Descriptions**

Bosch, R. (2026). *Zenodo technical note.*
DOI: [10.5281/zenodo.21817243](https://doi.org/10.5281/zenodo.21817243)
Current version DOI: [10.5281/zenodo.21820025](https://doi.org/10.5281/zenodo.21820025)

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.21817243.svg)](https://doi.org/10.5281/zenodo.21817243)

Machine-readable metadata: [JSON](../../publications.json) · [JSON-LD](../../publications.jsonld) · [BibTeX](../../CITATION.bib)

## Abstract

Tool definitions are commonly validated one at a time, although an agent
selects tools from a set of alternatives. Consequently, two descriptions may
each be syntactically valid and individually accurate while jointly failing
to explain why one tool should be selected instead of the other. This note
calls the missing distinguishing information a **tool differentia**. It
defines tool differentia as a set-relative property and presents H1.6, a
deterministic static analysis implemented in LintLang. H1.6 extracts
meaning-bearing terms from tool names and descriptions, normalizes selected
synonyms, and compares tool pairs within one parsed input. It reports mutual
nondistinction when neither member carries a distinguishing analyzed term and
directional domination when one member contributes none beyond those of the
other. The method requires no model calls and is suitable for local and
continuous-integration use.

## Plain-language summary

Two tool descriptions can each be individually well-written and still fail to
tell an agent — or a human reviewer — why it should pick one over the other.
Tool Differentia is a cheap, deterministic check that flags exactly that gap
before runtime, without calling a model. It is a narrow, bounded primitive:
it identifies an authored absence, not a guarantee about what a model will
actually select at runtime.

## Evidence boundary

The current synonym model is English-specific, and the detector only compares
definitions extracted from one parsed input — it does not infer which files,
servers, or tool groups are presented together at runtime. A missing
differentia does not demonstrate that a model will select the wrong tool; it
identifies an authored absence under the analysis model. The note does not
claim to validate H1.6's effect on actual model tool-selection behavior.

## Citation

```bibtex
@misc{bosch2026tooldifferentia,
  author       = {Bosch, Rolando},
  title        = {Tool Differentia: Relational Static Analysis for AI Agent
                  Tool Descriptions},
  year         = {2026},
  publisher    = {Zenodo},
  doi          = {10.5281/zenodo.21817243},
  url          = {https://doi.org/10.5281/zenodo.21817243},
  note         = {Technical note}
}
```

## License

CC-BY 4.0 (per Zenodo deposit).

## Tool that operationalizes this note

[LintLang](https://github.com/hermes-labs-ai/lintlang) implements H1.6, the
reference behavior described here, as of release `v0.3.8`.
