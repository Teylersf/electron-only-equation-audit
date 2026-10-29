# Equation consistency in electron-only reconnection manuscripts

**Taylor Kalin** — independent researcher; [taylorkalin.com](https://taylorkalin.com), [ORCID 0009-0003-9000-9315](https://orcid.org/0009-0003-9000-9315).

Version 1.0.0 is a public GitHub preprint:

- [Complete seven-page PDF](https://github.com/Teylersf/electron-only-equation-audit/releases/download/v1.0.0/main.pdf)
- [Complete manuscript](paper/manuscript.md)
- [All-page mathematical, citation and visual review](submissions/final-pages-and-citation-review.json)
- [Current publication status](submissions/publication-status.json)
- [Verified software archive — DOI 10.5281/zenodo.23784871](https://doi.org/10.5281/zenodo.23784871)
- [Anonymous software, archive and registry verification](submissions/zenodo-code-v1.0.0.json)

This computational audit checks displayed equations in Liu et al., *Electron-only magnetic reconnection and inverse magnetic-energy transfer at sub-ion scales*, arXiv:2407.06020v2, and its inspected publisher accepted manuscript. It contains original exact synthetic controls and independent review records. The accepted manuscript is an authentic CHORUS copy, **not the uninspected journal version of record**. Supplementary findings concern the supplement embedded in arXiv v2.

The controls isolate the main-to-Appendix continuity sign, a missing dimensional pressure coefficient, the density coefficient in the stated quadratic invariant, and collisionless Gaussian/Hermite projection signs. They retain positive checks of the source's reconnection-rate and conditional decay scalings. Recognizable transcription errors are a plausible explanation. These results do not determine the equations actually advanced by GX or invalidate the source's numerical curves.

- [Computational methods and scope](COMPUTATIONAL_METHODS.md)
- [Reproduction instructions](REPRODUCIBILITY.md)
- [Exact results](data/equation-controls.json)
- [Periodic energy ledger](data/periodic-energy-controls.csv)
- [Linear sign controls](data/linear-symbol-controls.csv)
- [Retained rate controls](data/retained-rate-controls.csv)
- [Retained conditional exponents](data/conditional-exponents.csv)

![Exact synthetic energy and linear-sign controls](figures/energy-and-wave-controls.png)

![Collisionless Gaussian/Hermite controls](figures/hermite-projection-controls.png)

The figures are explanatory synthetic calculations, not source simulation outputs. The complete comment credits the established KREHM/ERMHD theory and preserves the reconnection-rate and conditional decay controls. It does not identify the equations actually advanced by the source solver, revise its numerical curves, or claim that the uninspected journal version contains these displayed defects.

The [immutable computational snapshot](https://github.com/Teylersf/electron-only-equation-audit/tree/83583b1524778b8bb4e5c78482ae7f4f104856cc) contains exactly 55 files at commit `83583b1524778b8bb4e5c78482ae7f4f104856cc`, distinct tree `7bf82539dd5224ec9328dc94848b2a62dc6b4029`. The software DOI archives those exact bytes; it is not a manuscript DOI or journal acceptance. This release adds the manuscript, build inputs, operational verification and publication links. This README is the sole administrative change among the original computational files; the archived README and scientific/code/source-copy bytes remain unchanged at the immutable snapshot.

GitHub publication is a preprint release. Formal venue decisions and any later preprint-host records are tracked separately in the publication-status file. AI-assisted internal review is not external human peer review. No source-author correspondence or original simulation rerun is claimed.

Code is licensed under [MIT](LICENSE-CODE). Original explanatory text and figures are licensed under [CC BY 4.0](LICENSE-MANUSCRIPT). Source scientific ideas remain attributed to their original authors; source PDFs and credentials are excluded.
