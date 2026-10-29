# Source editions and review scope

The source is Liu, Silva, Milanese, Zhou, Mandell and Loureiro, “Electron-only magnetic reconnection and inverse magnetic-energy transfer at sub-ion scales.” The supplied nineteen-page file is byte-identical to [arXiv:2407.06020v2](https://arxiv.org/abs/2407.06020v2), submitted 10 March 2025 and internally dated 11 March 2025. Its first nine pages comprise the main article, Appendix A and references; PDF pages 10–19 contain the ten-page supplement. All nineteen supplied pages were read.

The independently established journal publication is *Electron-Only Magnetic Reconnection and Inverse Magnetic-Energy Transfer at Subion Scales*, Physical Review Letters 134(15), 155201, [DOI 10.1103/PhysRevLett.134.155201](https://doi.org/10.1103/PhysRevLett.134.155201). APS gives 15 April 2025 as online publication and 18 April as the issue date. Journal identity does not establish that a preprint or accepted manuscript is byte-identical to the version of record.

## Verified retrieved editions

| Edition | Bytes | PDF pages | SHA-256 |
|---|---:|---:|---|
| Supplied / official arXiv v2 | 2,913,430 | 19 | e482988aa241494c52cc6071317fbd6f3a1c084173f045f2bfc03ba0ade26cd8 |
| Official arXiv v1 | 710,338 | 7 | 2466c733c1b731def2e6f2cf963af5ad8e428eca1e80b3b6fdbe491419113d09 |
| Publisher-hosted accepted manuscript | 757,810 | 10 | 71c9216d20334427fdc84570c72b600c82c7009721f03837787f8d5a74eadd83 |

The [openly publisher-linked accepted manuscript](https://link.aps.org/accepted/10.1103/PhysRevLett.134.155201) has a CHORUS cover and nine article pages internally dated 19 March 2025. The cover is PDF page 1; printed article page 1 is PDF page 2. It contains no supplement. The original downloaded file and cached copy were independently compared. The edition reviewer and parent read all ten pages; the separate derivation reviewer inspected the relevant main/Appendix pages directly without claiming an additional full AM reading.

The subscription journal version of record and its final supplement were not retrieved. Publisher access now requires subscription authorization; the earlier raw-request security responses are historical access observations, not evidence that the openly supplied AM is a VOR. No access bypass or private subscription credential was used.

## Descriptive edition changes

The v1-to-v2 comparison records added applicability/ordering qualifications, a changed printed three-dimensional simulation parameter, additional numerical and cascade discussion, Appendix A and the embedded supplement. These are edition facts, not inferred executable histories. The AM retains the relevant main model, rate/scaling expressions and Appendix, while changing the date, figure placement, references and caption details. Its Figure 1 caption fixes the v2 decimal typo and adds approximation signs.

The exact historical [edition concordance](audit/source-editions/edition-concordance-original.md), [preflight record](audit/source-editions/source-editions-preflight-original.json), source inventories, extraction metadata and receipt copies preserve these distinctions. Earlier records explicitly labeled “before AM” describe the earlier access state. They are retained byte-exactly rather than silently rewritten.

## Finding locators and identity limits

| Check | Supplied v2 location | Accepted-manuscript check | Limit |
|---|---|---|---|
| Main continuity sign versus the stated 2D reduction | Main Eq. (1), PDF p.1; Appendix (A1), PDF p.5 | Printed pp.1,5 / PDF pp.2,6 | Verified in these two editions; no VOR claim |
| Main pressure-gradient coefficient versus Appendix | Main Eq. (2), PDF p.1; Appendix (A2), PDF p.5 | Printed pp.1,5 / PDF pp.2,6 | Printed dimensional/main-Appendix inconsistency |
| Density-energy coefficient and ion-entropy comparison | Supplement Eq. (12), PDF p.17; explanation p.18 | Supplement absent | v2 supplement only; diagnostic implementation unknown |
| Collisionless Hermite projection | Supplement Eqs. (9),(11), PDF p.15 | Supplement absent | v2 supplement only; collision-functional convention excluded |
| Ion-beta dimensional definition | After supplement Eq. (2), PDF p.12 | Supplement absent | Unit/normalization declaration issue; no hidden-code inference |
| Combined parallel Ohm term | Supplement Eq. (4), PDF p.14 | Supplement absent | v2 supplement only; not a rejection of the nonlinear shell diagnostic |

The full original [independent derivation review](audit/independent-derivation-review/independent-derivation-review-original.md) gives the calculations, positive controls and strongest benign interpretations. The most plausible interpretation is display/transcription or normalization defects: Appendix A already provides the consistent core coefficients and signs. The established KREHM model is prior work. The reconnection-rate calculation and conditional energy-decay/critical-balance exponents remain supported under the source's assumptions.

## Independent program and provenance

The [original independent program](audit/independent-derivation-review/verify_equation_consistency.py) uses exact rational arithmetic and periodic Fourier coefficients. It imports no producer, other verifier or simulation code. It was copied byte-exactly and run both in a clean directory containing only the program and at its packaged location with CPython 3.13.7. Both results match the original receipt byte for byte. See [copy-and-portability.json](audit/independent-derivation-review/copy-and-portability.json).

The program checks the literal continuity sign, wave symbols, local free-energy derivatives, Gaussian/Hermite moments, dimensions, and retained rate/ERMHD algebra. Source hashes in its output are recorded identities, not claims that source PDFs were present and rehashed during an offline reproduction. The true copy/run distinction and all original hashes are preserved.

No third-party source PDF, page image, full article text, complete author manuscript TeX or source archive is bundled here. Source metadata, archive-member inventories and a compact extraction of the main display environments identify external evidence; cache basenames in original receipts are not runtime dependencies. Mathematical expressions remain attributed to their source; third-party works retain their rights.

## Primary-model credit and convention checks

The separate [primary-theory verification](audit/primary-reference-review/primary-theory-verification.md) and its [metadata/provenance](audit/primary-reference-review/primary-theory-verification.json) are preserved byte-exactly. The checker read the relevant model, energy and Hermite sections of Zocco and Schekochihin, *Reduced fluid-kinetic equations for low-frequency dynamics, magnetic reconnection, and electron heating in low-beta plasmas*, Physics of Plasmas 18, 102309 (2011), [DOI 10.1063/1.3628639](https://doi.org/10.1063/1.3628639). It did not claim a full reading of the later tearing appendices.

That primary model supplies the consistent density-continuity minus sign, dimensional Ohm coefficient, half-weighted density energy and collisionless Hermite hierarchy. Its summary equation for a polarization variable can legitimately have a positive parallel derivative because that dependent variable is the negative of the density perturbation. Comparing signs without converting the variable would manufacture a disagreement.

The checker also read the relevant parameter/convention and ERMHD sections of Schekochihin et al., *Astrophysical gyrokinetics: kinetic and fluid turbulent cascades in magnetized weakly collisional plasmas*, Astrophysical Journal Supplement Series 182, 310 (2009), [DOI 10.1088/0067-0049/182/1/310](https://doi.org/10.1088/0067-0049/182/1/310). Its flux function has the opposite sign to the target vector potential; applying that conversion preserves the target's positive two-dimensional ERMHD density bracket and the low-beta rate limit. This was a bounded section read, not a full 67-page audit or a fresh publisher-VOR byte comparison.

The [GX framework identification](audit/primary-reference-review/GX-framework-identification.json) establishes the public solver framework and its published method reference, JPP 90(4), 905900402 (2024), [DOI 10.1017/S0022377824000631](https://doi.org/10.1017/S0022377824000631). It does not identify a commit, branch, run deck or diagnostic implementation used for the target study. The consistency comment's contribution is edition-specific reproducibility checks; it does not claim ownership of the established KREHM/ERMHD model or standard Gaussian/conservation identities.

## Availability and boundaries

Bounded registry and title/DOI searches found no target-specific correction or authenticated target-linked run-deck/raw-data deposit. This is not an exhaustive absence claim. The author archives contain manuscripts and figures, not a source-specific simulation release. GX and its method papers are cited by the article; generic code availability does not establish the exact implementation or diagnostics behind this study.

The source discloses its isothermal approximation, scale-ordering limitations, hyperdiffusion, the order-unity-beta extension's missing microscopic flux-breaking closure, and volume-filling assumptions. Those limitations receive explicit credit. No original simulation, observed reconnection/decay law, VOR expression, final journal supplement, code implementation or plotted energy diagnostic is rejected by this evidence package.
