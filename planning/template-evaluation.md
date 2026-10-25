# Template evaluation — 2026-10-24

## Decision for integration

Adopt **HKFoggyU/hkust-thesis v0.11.6**, pinned to release commit `1a9230d`, using the unmodified generated class in `template/hkust-thesis-v0.11.6/hkustthesis.cls`. This is a community template. The actual PDF, rather than its stale structure comment, has been checked. No changes were made to the old `main.tex`, `ustthesis.cls`, or MPhil sample PDF by this task.

The isolated entry is `template-smoke.tex`; output `template-smoke.pdf` has 13 pages. It exercises full front matter, a real MGRAG method passage, original published vector overview, an eight-column dataset table, the published cache-score expression, an algorithmic workflow, a theorem environment, numeric citation, bibliography and appendix. It is a layout test rather than a chapter draft. Front-matter names/dates were deliberately placeholders at creation and should now be replaced in the thesis entry using author-confirmed data.

## Reproducible acquisition and build

Release: https://github.com/HKFoggyU/hkust-thesis/releases/tag/v0.11.6

The release metadata was retrieved successfully. Raw GitHub and binary release ZIP downloads stalled; files were instead retrieved from the GitHub contents API with `ref=v0.11.6`, preserving the same pinned source version. The class was extracted by running `xetex -interaction=nonstopmode -halt-on-error hkustthesis.dtx` in its vendor directory. SHA-256 hashes and the MGRAG image provenance are in `planning/template-manifest.json`. The original LPPL license is retained.

From the project root:

```sh
latexmk -xelatex -interaction=nonstopmode -halt-on-error -latexoption=-no-shell-escape template-smoke.tex
```

A complete first build can also run XeLaTeX, Biber, and XeLaTeX until the bibliography and references converge. A second Biber pass was required because this class enables citation and page trackers. The final latexmk build completed successfully, with no undefined citations/references, duplicate labels, or overfull boxes. Logs are in `template/qa/`; the final compilation log is `template-smoke.log`.

## Measurements and visual QA

| Check | Output evidence | Result |
|---|---|---|
| Paper | `pdfinfo`: 595.28 × 841.89 PDF points | A4 |
| Base text size | PDF text extraction: 11.955 PDF points = 12 TeX points | 12 pt |
| Margins | Class geometry: horizontal and vertical 25 mm; body x extents 70.866–524.422 PDF points | Equal 25 mm margins |
| Body spacing | Consecutive body text baselines differ by about 20.66 PDF points, corresponding to 20.74 TeX points | Class uses `linespread=1.43`, documented by upstream as Word 1.5 spacing |
| Fonts | TeX Gyre Termes body, XITS Math; original figure retains its original fonts | All fonts embedded, all subset embedded |
| Pagination | Physical pages 1–8 show i–viii; first body page shows 1; references and appendix continue Arabic numbering | Correct sequence |
| Front matter | Title → Abstract → Authorization → Signature → Acknowledgments → TOC → LOF → LOT | Correct actual PDF order |
| Figure | Original MGRAG Figure 2, p.2484, copied byte-for-byte | Legible vector output; no redraw |
| Table | Published MGRAG Table 3, p.2488, 7 dataset columns, every numerical cell checked against PDF extraction | Fits with `\small` and 3pt tabcolsep, no scaling needed |
| Formula/algorithm | Unicode math and existing `algorithm`/`algorithmic` environments compile | Compatible |
| References | IEEE numeric compressed style; Biber 2.19 | Resolved |

All 13 pages were rendered at low resolution for a contact-sheet inspection; the body pages were additionally rendered at 96 dpi. The inspected final pages show no clipping, overlap, missing glyphs, or table overflow. Page 10 contains two floats with whitespace between them; this is acceptable in the short test, and full chapters should place floats near their discussion. Underfull horizontal-box diagnostics arise in the authorization text's explicit line breaks. Their rendered lines are visually acceptable. The class-name warning comes from loading the class with a directory path; its declared name is `hkustthesis`. The unused `UTF8` option and siunitx/physics message are inherited upstream diagnostics, not failed content.

## Integration API and package compatibility

Use:

```tex
\documentclass[customlatinfont=gyre,displaycommittee=false,blankpage=false]{template/hkust-thesis-v0.11.6/hkustthesis}
\hkustsetup{info={degree={phd},title={...},author={Yubo Wang},school={School of Engineering},department={Department of Computer Science and Engineering},program={Computer Science and Engineering},major={},supervisor={...},co-supervisor={},submit-month={...},submit-date={...},defend-date={...},depthead={...},reviewer={},reviewerdept={},reviewerext={},city={Hong Kong}}}
\addbibresource{thesis-references.bib}
```

Then `\frontmatter\maketitle`, `abstract` environment, `\authorization`, `\signaturepage`, `acknowledgements` environment, `\tableofcontents\listoffigures\listoftables`, `\mainmatter`, chapter inputs, `\printbibliography[heading=bibintoc,title=References]`, `\appendix`, appendix inputs.

The class already loads amsmath, amsthm, mathtools, thmtools, unicode-math, graphicx, subcaption, wrapfig, tikz, booktabs, multirow, multicol, listings, algorithm, algorithmic, enumitem, hyperref, cleveref, biblatex, physics, siunitx and others. Do not reload incompatible font packages, natbib, a second algorithm implementation, or legacy `subfigure`. Use `\cite`, `\textcite`, or `\parencite`; if chapter sources retain `\citep`/`\citet`, define deliberate biblatex-compatible wrappers in the shared preamble. Set chapter-specific theorem environments and ensure labels are namespaced.

`customlatinfont=gyre` is an explicit reproducibility choice among the template's built-in supported fonts, not an undocumented fallback. It avoids operating-system-specific Times New Roman variants. The original figure fonts are left unchanged.

## Open checks

1. The current FYTGS guideline URL returned HTTP 403 through both web and curl on 2026-10-24. This run therefore checked the official local eight-page PhD sample and the prior day's documented official requirements; it does **not** claim a successful fresh retrieval of the guideline webpage. Recheck at final submission.
2. The local official sample visibly displays i on its title page, while page 6 says i is not shown. The smoke counts and displays i following the visible sample; final display requires FYTGS/CSE confirmation. Counting title as i is preserved either way.
3. Author-confirmed submission month, dates, supervisor/head information must be inserted in the actual thesis entry. Signature date and department head remain distinct unknown fields. The draft cannot certify completion or substitute signatures.
4. The source dataset-table caption says “7 sub dataset of the MRAMG benchmark”; the actual published dataset paragraph and columns show six MRAMG subsets plus MMQA. No values were altered. This discrepancy is recorded for the main source audit.
5. The original MGRAG Figure 2 has small labels, although legible at full thesis text width. Final chapter QA should inspect the figure at 100% and, if necessary, place it on a landscape page while preserving its original bytes.
