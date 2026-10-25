# Thesis writing progress and handoff

Updated: 2026-10-25 (Asia/Shanghai). **Independent whole-manuscript review round 2 is complete and integrated.** Complete eight-chapter English manuscript is ready for author/supervisor review; signature and institutional items remain with the author. This record supersedes earlier checkpoint counts and hashes.

## Entry, template and delivery

- Title: **Structural Augmented Reasoning for Language Models**; author Yubo Wang.
- Build: `make`; entry `main.tex`; output `thesis.pdf` (also `main.pdf`). XeLaTeX + Biber + latexmk, shell escape disabled. Ordinary compilation uses project-local inputs.
- Template: HKFoggyU v0.11.6, release commit `1a9230d`, under `template/hkust-thesis-v0.11.6/`. The release's older internal class version is preserved. Original MPhil example: `legacy/mars-2010/`.
- Current PDF: **133 pages** (14 front matter, 114 body, 5 references); **27,843 narrative words**, **29,785 with headings/captions**, **261-word abstract**. SHA-256 `f44abbdbc4bceb3ba9e73fe42b6b032f22d94aa9ceb40068d3e7280707b40905`. Exact counts/ranges: `CHAPTER_COUNTS.md`.
- Review removed 2,180 narrative words of repeated explanation. Counts are below the original 30,000–38,000 working range; plan §3.3 allows a complete shorter thesis and forbids empty expansion. The original budget has not been relabeled as met.
- Current portable source/PDF archive: `deliverables/thesis-project-2026-10-25.zip`; prior October24 archive retained. Package test evidence: `qa/final/package-build-verification.json`.

## Chapter state

| Chapter | File | State |
|---|---|---|
| 1 | `chapter/ch01-introduction.tex` | Complete; independently reviewed; 2,489 narrative words, 8 pages |
| 2 | `chapter/ch02-background.tex` | Complete; independently reviewed; 3,892 narrative words, 12 pages |
| 3 | `chapter/ch03-kglink.tex` | Complete; independently reviewed; 4,337 narrative words, 19 pages |
| 4 | `chapter/ch04-gorag.tex` | Complete; independently reviewed; 4,162 narrative words, 17 pages |
| 5 | `chapter/ch05-agrag.tex` | Complete; independently reviewed; 4,568 narrative words, 22 pages |
| 6 | `chapter/ch06-mgrag.tex` | Complete; independently reviewed; 5,763 narrative words, 26 pages |
| 7 | `chapter/ch07-discussion.tex` | Complete; independently reviewed; 1,907 narrative words, 7 pages |
| 8 | `chapter/ch08-conclusion.tex` | Complete; independently reviewed; 725 narrative words, 3 pages |

Front matter: `chapter/front-abstract.tex`, `chapter/front-acknowledgements.tex`; metadata in `main.tex`. CIKM HyperKG/FormerGNN remains the separate Background §2.6 (about960 words), unchanged this round. MGRAG retains query-aware construction, semantic path matching and graph-aware context recomputation. CMI-Mem and ClinicalAgents are excluded from core contributions. The four studies have separate implementations and protocols.

## Latest review and evidence

Three independent reviews and integration dispositions are under `review-round2/`; start at `review-round2/REVIEW_SUMMARY.md`. The common argument now concerns the evidence decisions controlled by explicit relationships. A new Discussion conditions table distinguishes models, hardware, supervision, evolving/fixed/query-dependent evidence and metrics. The error-propagation section adds synthesis instead of another component inventory.

Source checks corrected KGLink's three-candidate-type per-row implementation description, GORAG's model-role cell, AGRAG pseudo-node wording, and MGRAG's anchor-counterpart loop/search-failure description. Unitless KGLink “9.70” was omitted rather than assigned an unreported unit. Inherited incorrect numerical rank emphasis was removed from three tables; all values remain literal. See `EVIDENCE_SUMMARY.md` and `verification-*.md`.

All 47 original displayed formula blocks are byte-identical to the pre-review manuscript; all 22 external result-table files retain ordered numeric tokens; all 27 original graphic source/target/manifest hashes match. The earlier 1,765 adopted numeric/missing-value entry audits remain valid; the new conditions table was checked separately. Bibliography: 105 fragment entries →74 works with31 aliases; no unresolved citations.

MGRAG is checked against the publisher PDF. KGLink/GORAG/HyperKG PDFs are author-confirmed publication-equivalent arXiv versions, not direct publisher downloads. **AGRAG uses the author-selected complete local ICDE2026.pdf**, retained at `published/agrag-local-complete.pdf`; its incomplete arXiv is not the authority for absent main tables. Main-text precedence for KGLink/GORAG/AGRAG conflicts is author-confirmed. Contradictory supplementary guarantees are not asserted. MGRAG's fixed experimental b remains unreported.

## Confirmed author information

December2026 submission; tentative27November2026 defense; Prof.Lei Chen, Chair Professor, supervisor. The approved personal contribution statement says the author led the research with discussions/collaboration by Dr.Haoyang Li, Dr.Hao Xin and Dr.Shimin Di. A brief acknowledgment draft is authorized; individual unconfirmed tasks are not allocated.

## Latest compilation and PDF inspection

Final strict `make` passed; no unresolved reference/citation, duplicate label, missing asset/glyph, overfull box or Biber warning. All133 pages were inspected in regenerated contact sheets, with detailed reinspection of changed algorithm, table, introduction and discussion pages. Final pagination controls were inspected after the last build. `FINAL_QA.md` identifies accepted hash, font/geometry checks and source-resolution limits. Original portrait instances remain224–257ppi. No research figure was redrawn or upsampled. The paper-level style postpass is3/10 (mild), with necessary scientific caveats preserved; `STYLE_AUDIT.md` links the full nine-column audit and before/after counts.

## Directly executable next steps

1. Obtain the exact department-head name/title and real signature dates/signatures; update `main.tex` from confirmed information. The tentative defense date is not a signature date.
2. Clarify the official sample's conflicting title-page i instructions with FYTGS/CSE. Current output counts/displays i following the visible sample. FYTGS retrieval returned403 on October24; no fresh October25 policy verification is claimed.
3. If original MGRAG run configurations/logs become available, resolve fixed experimental b; do not infer it from a code default.
4. Author/supervisor review can proceed on this PDF. Refine personal acknowledgments and arrange departmental/iThenticate steps; see `AUTHOR_ACTIONS.md`.
5. After manuscript changes run `make`, `make counts`, `scripts/inspect_thesis_pdf.py` with pypdf/pdfplumber/Pillow, `scripts/report_thesis_counts.py`, and inspect affected pages. Refresh final QA/hash and source package. Review snapshot scripts require `review-round2/before-manuscript.tar.gz`, retained in the full workspace.

No parallel edit ownership remains. No session change is necessary. Historical chapter/round-one reports retain their own snapshot counts and do not certify this newer PDF by themselves.

Final portable-package test: fresh extraction and `make` passed (exit0,133pages), with identical extracted text to the accepted PDF. Final documentation updates preserve the tested compilation-input fingerprint; see `qa/final/package-build-verification.json`.
