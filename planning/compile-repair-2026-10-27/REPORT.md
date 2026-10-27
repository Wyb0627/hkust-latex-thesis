# Compilation environment diagnosis and repair

Date: 2026-10-27. Requested outcome: diagnose missing programs, repair compilation and update the thesis PDF.

## Findings

- The system programs are present and usable: active TeX Live 2023, latexmk 4.79, XeLaTeX and Biber 2.19 under `/Library/TeX/texbin`. `latex-doctor.json` reports `existing-usable`, no missing required tools and a passed TeX Live smoke test. No TeX installation or upgrade was needed.
- The app compiler uses an independent process environment. Its Tectonic fallback inherits a restricted PATH without the TeX detector’s augmented MacTeX path. This explains how its external-tool lookup can report Biber missing while terminal Biber works. The built-in retry still records that error.
- The bundled desktop helper defaults to pdfLaTeX, and the app invocation inspected locally does not specify an engine. A direct helper reproduction fails with `unicode-math` requiring XeLaTeX/LuaLaTeX. The project has always required XeLaTeX. This reproduced engine mismatch is distinct from the app’s recorded TeX Live exit -6; the precise cause of that abort remains unresolved.
- A direct helper run with XeLaTeX also encountered output-directory bibliography-state handling. No bibliography backend was substituted. The ordinary project XeLaTeX/Biber chain succeeds.

## Repair and validation

`scripts/build_thesis.py` now resolves latexmk, XeLaTeX and Biber before compilation. If PATH omits a required tool, it adds the existing active `/Library/TeX/texbin` directory for this process, prints the resolved paths and fails explicitly if any program is still missing. It anchors execution to the project directory and retains the original XeLaTeX/Biber chain with shell escape disabled. No system-wide settings or signed app files were changed.

An explicit Biber pass succeeded. After removing only latexmk’s generated dependency database, a full XeLaTeX rebuild through the repaired script succeeded with PATH deliberately restricted to `/usr/bin:/bin`. Final checks passed for references/citations, characters, labels, overflow and Biber diagnostics. This was a real rebuild, not only an up-to-date check. Evidence: `biber-rebuild.txt`, `repaired-build.txt`, and `terminal-build.txt`.

Updated outputs: `main.pdf` and `thesis.pdf`, 115 pages. SHA-256: `2e0fa332ed7ffd94111d25b45640d4fcf60e24baa97b90d277ae13c9f3941a87`. PDF inspection, font embedding, geometry and visual checks are summarized in `../FINAL_QA.md`; current page ranges are in `../CHAPTER_COUNTS.md`. Manuscript text, bibliography, equations, tables, figures and experimental data were not modified during this repair.

## Remaining app issue

The existing editor was kept open. Its independent preview still fails in the built-in retry, preserved as `built-in-retry.json`. The project build and exported PDF are repaired; the app’s preview is not. Continue using `make` from the project root or `python3 scripts/build_thesis.py` for the current local installation. Restarting or patching the application was not attempted.
