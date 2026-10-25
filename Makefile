.PHONY: all clean counts
all: thesis.pdf

BIB_FRAGMENTS := $(wildcard bibliography/*.bib)
THESIS_INPUTS := $(wildcard chapter/*.tex chapter/tables/*.tex figures/*/*) template/hkust-thesis-v0.11.6/hkustthesis.cls

thesis-references.bib: $(BIB_FRAGMENTS) scripts/merge_bibliography.py scripts/bib_utils.py
	python3 scripts/merge_bibliography.py

thesis.pdf: main.tex Makefile scripts/build_thesis.py $(THESIS_INPUTS) thesis-references.bib
	python3 scripts/build_thesis.py

counts:
	mkdir -p planning/qa
	texcount -inc -sub=chapter main.tex > planning/qa/texcount.txt

clean:
	latexmk -c main.tex
