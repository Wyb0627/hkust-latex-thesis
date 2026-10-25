# KGLink defensive-writing audit

Audited 2026-10-24 after method/source checking. Scope: chapter/ch03-kglink.tex, not the complete thesis. The table records actual working-draft phrases revised during this pass. Technical caveats about the evaluation protocol remain.

| Location | Original | Type | Severity | Necessary caveat? | Why it feels defensive | Likely reviewer reaction | Recommended action | Rewrite |
|---|---|---|---|---|---|---|---|---|
| Linking limit | “It does not imply that the first lexical match is the correct entity.” | D12 | Minor | DEFENSIVE | Answers an unraised interpretation rather than explaining the next operation | Reader wants the selection rule | Delete and state processing | “Graph-based filtering and row ranking select among the retrieved evidence before it reaches the annotation model.” |
| Row selection | “Its measurements should be interpreted as the effect of the reported procedure, rather than an isolated estimate of the effect of removing arbitrary rows.” | D12 | Major | MIXED | Excessively instructs interpretation of a simple intervention | Reader may perceive anticipatory defense | Keep intervention in one sentence | “The row-selection experiment evaluates this coupled selection mechanism.” |
| Two KG pathways | “They provide evidence about the reported architecture under its selection rules, rather than a general claim that every additional graph neighbor improves annotation.” | D2, D12 | Major | DEFENSIVE | Disclaims a universal claim absent from the text | Distracts from the ablation | Delete universal non-claim | “The experimental ablations examine the two pathways through specific model variants.” |
| Representation protocol | “This distinction is part of the information protocol and is necessary for interpreting the result.” | D1 | Minor | MIXED | Tells the reader that the protocol matters instead of stating it | Reader wants label availability | State training/evaluation distinction directly | “Training uses the true-type and masked inputs, while evaluation uses the masked input.” |
| Encoder substitution | “It does not isolate an architectural change to candidate extraction.” | D12 | Minor | DEFENSIVE | Adds an unnecessary non-claim after defining the changed encoder | Repeats the experimental scope | Delete | “The architecture uses the same graph-processing design with a different encoder in this experiment.” |
| Runtime missing entry | “This missing entry is retained in the original image and is not assigned a zero time.” | D9, D12 | Minor | DEFENSIVE | Describes transcription procedure inside scientific prose | Reader expects the entry itself | State the measurement status | “The chart labels MTab's inference entry as N/A.” |
| Data efficiency | “The auxiliary objective can only be interpreted relative to those training proportions and the shared evaluation data.” | D12 | Minor | MIXED | Over-signals a protocol already given | Unnecessary caution | Describe controlled comparison | “The experiment measures data efficiency by varying available supervision against a fixed evaluation set.” |

## Paper-level defensive-writing score

**1/10 for this chapter only.** A thesis-level score requires the full manuscript. Residual boundaries state input limits, task labels, model substitutions, or data availability and affect interpretation.

## Highest-priority removals

1. Deleted the universal non-claim about every graph neighbor improving performance.
2. Replaced interpretive instructions about row selection with its actual coupled intervention.
3. Consolidated the training/evaluation label-availability explanation.
4. Removed bookkeeping about missing runtime values from scientific prose.
5. Removed a repeated non-claim about encoder substitution.
6. Replaced the data-efficiency warning with the fixed-test-set protocol.

## Necessary caveats to preserve

- SemTab excludes the multi-label second round, and VizNet uses the selected multi-column subset.
- Training includes ground-truth type inputs; inference includes only the masked input.
- No-KG evaluation requires the entire table to lack linkages.
- MTab's weighted F1 entries are unreported, and its VizNet labels are translated to KG entities.
- Main configuration uses BERT; DeBERTa is a separate encoder experiment.
- The encoder's token/column limits constrain the effective table view.
- Runtime measurements use the reported VizNet implementation/hardware and separate training from inference.

## Repeated phrase audit

Machine counts of actual source phrases after this pass are saved in `planning/kglink-style-counts.json`. The chapter has no occurrences of “we emphasize,” “it should be noted,” “for a fair comparison,” “we do not claim,” “together, these,” “robust,” “comprehensive,” or “promising.” “Reported” is retained for inherited published measurements and can be reduced during whole-thesis editing where the publication provenance is already clear.
