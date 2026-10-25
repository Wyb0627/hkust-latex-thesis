# Independent full-manuscript review, round 2

Closed 2026-10-25. Accepted PDF: `../../thesis.pdf`; SHA-256 `f44abbdbc4bceb3ba9e73fe42b6b032f22d94aa9ceb40068d3e7280707b40905`. This round reviewed the complete manuscript and checked affected source passages against the selected paper versions. It did not run new experiments.

## Review and disposition

- `kglink-gorag.md`: independent methods, experiment controls, shared framing and style review of Chapters3–4; post-integration acceptance included.
- `agrag-mgrag.md`: independent Chapters5–6/source/PDF review; restored Algorithm1 outer loop and controls-table integration accepted.
- `narrative-style.md`: full abstract/Chapters1–8 read, ranked 24-row nine-column audit, necessary caveats, phrase counts and post-integration review.
- Main integrator inspected the affected source/PDF evidence, applied corrections, rechecked the manuscript and actual compiled pages. Agent completion alone was not acceptance.

| Finding | Resolution | Evidence |
|---|---|---|
| Shared argument was diluted by repeated method/evaluation inventories | Introduction now asks which evidence decisions structure controls; Discussion adds error propagation and a cross-study experimental-conditions table; Conclusion starts with findings | `applied-edits.json`, Chapters1/7/8 |
| GORAG model-role summary misassigned statistical keyword extraction to the LM | Table7.1 now states label-description generation and classification | GORAG statistical extraction equations versus label-information/generation stages; reviewer report |
| KGLink implementation description omitted candidate-type cap | Restored up to three candidate types per row from the KG entities in each column, in the candidate-types paragraph | KGLink controlling PDF p9 §IV.B and selected source around line663 |
| KGLink selected-class gain “9.70” had no stated unit | Omitted the number; retained class names, largest-increase criterion and >10-test-sample selection | Source around line874 and controlling PDF p12 both omit a unit. Narrative-audit row11's initial retain suggestion is superseded by this source check |
| AGRAG pseudo-node lifecycle wording exceeded evidence | “Indexing device” changed to “connectivity device”; cost10 and algorithm unchanged | Selected main-method text; no inference about insertion lifecycle |
| MGRAG empty result could imply exhaustive failure; condensed pseudocode missed an outer loop | State failure of the search to find a valid correspondence; restore query-anchor input and loop over eligible evidence counterparts, with anchored mappings and accepted-result aggregation | Publisher p2485 Algorithm1; `mgrag-p2485.txt`; no completeness claim |
| Inherited numeric rank highlighting contradicted values | Removed149 bold/underline numeric marks in three tables, retaining every value, precision, unit and missing marker | `rank-emphasis-changes.json`; no replacement ranking or result calculation |
| Repeated source-preservation assurances, case-versus-aggregate explanations and scope tags | Delete/consolidate; retain metric denominators, timing, model/hardware, source discrepancies and conditional guarantees | 82 exact edit records plus post-integration edits; full nine-column style audit |

## Quantitative delta

| Item | Before | Accepted |
|---|---:|---:|
| PDF pages |137|133|
| Narrative words, Chapters1–8 |30,023|27,843|
| Narrative + headings/captions |31,951|29,785|
| Abstract |261|261|
| Tables |45|46 (new conditions table)|

The 2,180-word narrative reduction is primarily deletion of repetition. Counts now fall below the original working range. Plan §3.3 explicitly permits a shorter complete manuscript and excludes empty expansion; no word-budget compliance is claimed. Exact chapter counts/page ranges: `../CHAPTER_COUNTS.md`.

## Verification and limits

- `invariance-check.json`: all47 original displayed equation/align blocks byte-identical; all22 external result-table ordered numeric streams unchanged. This is an edit-invariance test, not a proof of source mathematics.
- `../qa/final/asset-hash-verification.json`:27 source/target/manifest graphic hashes match. No redraw or replacement experimental image.
- Existing1,765 adopted numeric/missing-value entry audits retained. New conditions-table contents checked against source-specific models, local hardware, supervision and metrics by the integrator and scientific reviewers. No cross-study pooled accuracy or runtime ranking was added.
- Strict final build passed with no unresolved citation/reference, duplicate label, missing glyph/asset, overfull box or Biber warning. Accepted133-page PDF has A4 pages, embedded fonts and no detected body-boundary violations. All-page contact sheets plus detailed changed-page renders inspected; see `../FINAL_QA.md`.
- The full-manuscript style reviewer judged4/10 before and3/10 after (mild; qualitative). Counts in `phrase-counts.json` are flags rather than deletion quotas. Earlier round-one2/10 judgment is historical and was not carried forward as a stronger final claim.
- Source-internal KGLink/GORAG/AGRAG discrepancies, source-specific metric definitions, missing MGRAG fixed b and original224–257ppi portrait instances remain documented. This review did not resolve contradictory proofs, rerun experiments or freshly retrieve FYTGS rules.

Before snapshot: `before-manuscript.tar.gz` and `before-hashes.json` in the full workspace. Applied changes: `applied-edits.json`, `post-integration-edits.json`, `rank-emphasis-changes.json`. The compact deliverable includes text/JSON review evidence; the large before snapshot and rendered images remain in the full workspace.


Fresh package validation passed on 2026-10-25: independent temporary extraction, included reading PDF removed, `make` exit0,133pages, and byte-identical `pdftotext -layout` output. Text SHA-256 `950c9443db7fb1cb9b5a512acb93cd72a74aa3f8b08fe85de21759496b69616c`; compiled-input fingerprint `5c5b3acf6dcfa870e83fe7edfc81c0ef446f97831812cc16de77f55b832f50a1`. Final documentation-only repackaging preserves this tested fingerprint.
