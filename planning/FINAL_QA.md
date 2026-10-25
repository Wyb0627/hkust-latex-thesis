# Final integrated thesis QA — 2026-10-25, review round 2

Accepted artifact: `thesis.pdf`; entry `main.tex`; SHA-256 `f44abbdbc4bceb3ba9e73fe42b6b032f22d94aa9ceb40068d3e7280707b40905`. **133 pages**: preliminary i–xiv, body1–114, References115–119. Chapters1–8 contain **27,843 narrative words**, **29,785 including headings/captions**; abstract261words. Detailed ranges/counts: `CHAPTER_COUNTS.md`. Original working word range is not met after removing2,180 narrative words of repetition; plan §3.3 permits a shorter complete manuscript without filler.

## Compilation and structure

Final strict `make` (XeLaTeX/Biber/latexmk, shell escape disabled) passed after the last paragraph-pagination changes; current build log is `qa/build-current.txt`, also `review-round2/build.txt`. No unresolved reference/citation, duplicate label, missing asset/glyph or overfull box. Biber is warning/error-free. Three vendor notices remain: directory-qualified class name, unused UTF8 option, and siunitx/physics compatibility. Underfull paragraph diagnostics were checked visually.

All eight chapters and abstract are explicit local inputs. Front matter order: Title → Abstract → Authorization → Signature → Acknowledgments → TOC → LOF → LOT → body → References. Actual contents lists, bookmark destinations and Roman/Arabic numbering were checked. No old MPhil example identities or invented officials occur. Bibliography deduplication yields74 distinct works with31 aliases from105 fragment entries.

There are **46 table labels**,21 figure environments,47 displayed equation/align blocks, and one algorithm environment plus the explained greedy path procedure. The additional table is the cross-study experimental-conditions matrix; no new result table or experiment was introduced.

## Method and evidence changes

Three independent full/scientific review reports and integration decisions are in `review-round2/REVIEW_SUMMARY.md`. Scientific fixes restore the KGLink candidate-type cap; correct GORAG's model role; avoid unsupported AGRAG pseudo-node lifecycle wording; and restore MGRAG publisher Algorithm1's anchor-counterpart loop. Search-failure wording preserves greedy incompleteness. Unitless KGLink9.70 is omitted, not converted to a guessed unit. Necessary source-specific formulas and interpretation caveats remain.

All47 original displayed formula blocks are byte-identical to the before snapshot. All22 external result-table files preserve ordered numeric tokens, including units/precision/missing markers by source audits. Incorrect inherited numeric rank emphasis was removed from three tables (149 marks), with no value change. All27 graphic source/target/manifest hashes match. Existing1,765-entry adopted-table source audits remain applicable. The new conditions table was checked separately against each study's source controls. See `EVIDENCE_SUMMARY.md`, individual chapter ledgers and `review-round2/invariance-check.json`.

## Geometry, fonts and graphics

| Check | Current133-page PDF |
|---|---|
| Geometry | Every page A4,595.28×841.89 PDF points; no rotation |
| Body type | TeX Gyre Termes11.955 PDF points (=12 TeX points); XITS Math |
| Margins |25mm class setting; no extracted body glyphs outside the checked approximate25mm boundary, excluding centered page numbers |
| Line spacing |20.66 PDF-point median body baseline; class linespread1.43 is its documented Word-style1.5 setting |
| Fonts |95 font resources, all embedded; some original Type3 figure fonts fully embedded rather than subset;18 resources lack Unicode maps, with visible glyphs retained |
| Raster quality | Original illustrative220×293 portrait instances in MGRAG figures at224–257ppi (physical97/105); source-resolution limit retained. Main raster diagrams exceed300ppi |
| Image identity |27 original copied research files, matching hashes; vector labels/plots preserved; no redraw or artificial upsampling |
| Content | All133 pages contain content; unencrypted; no PDF JavaScript detected |

Machine records: `qa/final/pdf-preflight.json`, `typography-summary.json`, `pdffonts.txt`, `pdfimages.txt`, `asset-hash-verification.json`. This is not PDF/A or tagged-PDF certification. A strict300ppi minimum for every embedded portrait would require an original higher-resolution figure; resampling would not create detail.

## Actual visual inspection

The revised PDF was rendered to seven all-page contact sheets. The main integrator inspected all133 pages at overview scale and reinspected changed algorithm/table/paragraph pages in detailed renders. Earlier independent chapter PDF reports retain their own historical hashes; they are not misrepresented as a fresh inspection of133 pages. Current preflight/contact sheets were regenerated after the final pagination edits.

Detailed round-two renders in `review-round2/` include the Introduction contribution table (physical21/printed7), MGRAG Algorithm1 (physical102/printed88), AGRAG efficiency/ablation tables (physical86/88), and Discussion roles/controls tables (physical120/122, printed106/108). The expanded algorithm fits with its nesting and input visible. Table7.1 model roles and Table7.2 condition rows remain readable. Final `final-discussion-120.png` and `accepted-discussion-121.png`/`122.png` were checked after paragraph controls and a shortened transition removed a one-line continuation around floats.

No clipping, overlap, missing material, illegible numerical table entries or broken continuation headers was found in the inspected output. Long MGRAG tables repeat their headers/dataset identifiers. Original graphic labels remain readable at page scale; small portrait detail is limited as disclosed above. Float-only KGLink illustration pages are clean, with intentional whitespace. TOC/LOF/LOT, front matter, references and chapter transitions remain present after repagination.

## Portable package and remaining items

Current bundle: `deliverables/thesis-project-2026-10-25.zip`; previous October24 bundle retained. Fresh extraction/build verification is recorded in `qa/final/package-build-verification.json` and `package-build.txt`. The final ZIP/PDF checksums are outside the ZIP in `deliverables/SHA256SUMS`; `deliverables/package-manifest.json` gives per-file hashes. Documentation-only repackaging must preserve the tested compiled-input fingerprint.

The remaining author/institutional items are unchanged: department-head identity, real signature dates/signatures, title-page i display clarification, and missing fixed MGRAG b metadata. See `AUTHOR_ACTIONS.md`. FYTGS returned403 on October24; no fresh October25 policy retrieval is claimed. Format review uses the local official PhD sample, the existing current-requirements review and October24 Library guidance. No experiment reproduction, corrected proof, signed submission, iThenticate result or institutional approval is asserted.


Fresh package validation passed on 2026-10-25: independent temporary extraction, included reading PDF removed, `make` exit0,133pages, and byte-identical `pdftotext -layout` output. Text SHA-256 `950c9443db7fb1cb9b5a512acb93cd72a74aa3f8b08fe85de21759496b69616c`; compiled-input fingerprint `5c5b3acf6dcfa870e83fe7edfc81c0ef446f97831812cc16de77f55b832f50a1`. Final documentation-only repackaging preserves this tested fingerprint.
