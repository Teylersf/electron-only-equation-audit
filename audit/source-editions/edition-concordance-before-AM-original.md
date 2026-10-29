# Source 10 identity and edition concordance

## Verified identity

The supplied file is **byte-identical to official arXiv:2407.06020v2**, not yet verified against the journal version of record. It has 19 pages and a printed date of 11 March 2025; arXiv records v2 submission on 10 March 2025 at 04:08:15 UTC. The original v1 was submitted 8 July 2024 at 15:09:04 UTC and has seven pages. Both PDFs and both author-source archives were retrieved normally from arXiv.

The authentic final publication is **Electron-Only Magnetic Reconnection and Inverse Magnetic-Energy Transfer at Subion Scales**, by Zhuo Liu, Caio Silva, Lucio M. Milanese, Muni Zhou, Noah R. Mandell and Nuno F. Loureiro, *Physical Review Letters* **134**(15),155201. DOI [10.1103/PhysRevLett.134.155201](https://doi.org/10.1103/PhysRevLett.134.155201). The official publication is dated 15 April 2025; the issue is dated 18 April. APS records received9 July2024 and accepted14 March2025. This identity uses official APS and Crossref records; the current arXiv abstract page itself has no journal-reference field.

## Frozen retrieved bytes

| File | Bytes | PDF pages | SHA-256 |
|---|---:|---:|---|
| `supplied.pdf` | 2,913,430 | 19 | `e482988aa241494c52cc6071317fbd6f3a1c084173f045f2bfc03ba0ade26cd8` |
| `arxiv-v2.pdf` | 2,913,430 | 19 | `e482988aa241494c52cc6071317fbd6f3a1c084173f045f2bfc03ba0ade26cd8` |
| `arxiv-v1.pdf` | 710,338 | 7 | `2466c733c1b731def2e6f2cf963af5ad8e428eca1e80b3b6fdbe491419113d09` |
| `arxiv-v2-source.tar` | 7,457,932 | — | `dcb3becc8d69928088b22cef4b03b877d297bdbcbae46b64efa22b2705965d47` |
| `arxiv-v1-source.tar` | 1,132,377 | — | `56351ec0d7867eb95cdc90994e265ee7fd4674fa67e05f00be4971a797646ea4` |

The source archives were safely extracted under `arxiv-source-v1/` and `arxiv-source-v2/`. Their per-member SHA-256 inventories are preserved. These are author TeX/figure archives, not executable simulation-code releases.

## Observed v1 to v2 changes

This is a descriptive edition comparison, not a finding that either edition is wrong. Exact differences are in `arxiv-v1-v2-main-source.diff`.

- The title adds “magnetic”; the abstract removes its low-beta parenthetical. The main low-beta fluid-model description remains.
- Strong separation signs in the island-ordering description become single inequalities. New footnote38 explains the formal ordering and practical scale ratio; v2 explicitly states simulation ratios at most20 and discusses agreement without large separation. See v2`main.tex`126–129,174 and189.
- Numerical descriptions add the role of hyperdiffusion against unbounded thinning and confirmation of current-sheet widths. Figure1 parameter captions change. See v1line177 and v2lines166,181–190.
- The printed3D parameter changes from rho_i=2.0 to1.0 while d_e=.04 stays fixed (v1line228, v2line235). No claim about unobserved executable histories is inferred.
- V2 adds more explicit forward/inverse-transfer, non-isothermal and non-volume-filling qualifications, plus supplemental diagnostics. Its described kinetic-to-MHD crossover shifts from approximately.2 to.1 tau_A. See v2lines249–278.
- V2 adds AppendixA on the reconnection-rate derivation (source305–367; PDFpp5–6) and embeds ten supplemental pages. The19-page package comprises main textpp1–5, appendixpp5–6, referencespp6–9 and supplementpp10–19. V1 has no supplemental PDF embedded in its seven-page PDF or six-member source archive; this does not establish that no supplement existed elsewhere.

## Current final-edition access limit

One ordinary request to the [official final PDF](https://journals.aps.org/prl/pdf/10.1103/PhysRevLett.134.155201) returned HTTP403 challenge HTML, not a PDF. It was not retried. Root then inspected the normal Chrome publisher page: security verification resolved automatically, but the final full text requires subscription authorization; the supplement is also marked subscription-required. The access limit is therefore **subscription authorization**, not an outstanding human challenge. This UI fact is explicitly root-reported, separately corroborated by accessible official page metadata, rather than an independently performed browser read by this preflight agent.

APS openly supplies [Download Accepted Manuscript](https://link.aps.org/accepted/10.1103/PhysRevLett.134.155201). One ordinary request to that public link also returned403 HTML, so no accepted-manuscript PDF was obtained. An accepted manuscript must be distinguished from the final VOR even if a later legitimate download succeeds. No alternate-route bypass, credential, purchase or source-author contact was used. Neither final-versus-v2 scientific identity nor difference is presently verified.

## Root reading cache

- Complete primary text: `supplied-full-text.txt`; numbered pages:`supplied-page-01.txt` through`supplied-page-19.txt`. These use default pypdf extraction.
- Layout-mode copies are retained as `*-layout.txt`. Layout extraction omitted most rotated embedded supplement text; the primary complete text fixes that omission. Each complete page is nonempty. Separate embedded supplemental PDF/text files are also available.
- All19 supplied pages rendered at130dpi as `supplied-page-01.png` through`supplied-page-19.png`, plus `supplied-contact-sheet.png`. V1 also has seven numbered page texts/renders.
- All19-page thumbnail overview and full-size identity/supplement-opening pages1 and10 were inspected; this is not a full scientific audit. Poppler emitted display-font alias warnings; sample identity pages are legible.
- `arxiv-equation-environments.json` preserves exact author-TeX display environments with line numbers/labels (eight in v1,16in v2). The supplemental material was submitted as PDFs, so its full source TeX is not claimed available.

## Corrections and availability

The independently prepared `correction-and-deposit-check.json` records an empty Crossref relation and no update-to/updated-by fields. Three bounded primary-context searches identified no target-specific correction or authenticated target-linked code/data deposit. This is not exhaustive and does not establish absence, particularly while final text is restricted. The arXiv text cites numerical codeGX and its method papers; the inspected source archives contain manuscripts/figures, not run decks or raw simulation diagnostics.

Zenodo14919784 belongs to a different CommunicationsPhysics paper, DOI10.1038/s42005-025-02034-z; it must not be attributed to this PRL.

No scientific correctness verdict, new manuscript/program, publication, queue advance, Git change, access-guide change or private-catalogue change was made.
