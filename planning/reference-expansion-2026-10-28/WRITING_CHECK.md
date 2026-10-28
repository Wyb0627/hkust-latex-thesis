# Writing check under the author's updated instructions

2026-10-28. Scope: manually review the newly expanded ch01/ch02 paragraphs, Abstract, Discussion and Conclusion, and scan all eight narrative chapters for defensive stock phrases and sentence punctuation. This complements the preceding full-manuscript wording pass in `../citations-wording-2026-10-28/`.

The audit uses `academic-defensive-writing-auditor`. Scientific protocol conditions are retained when they determine what the method or reported result means. No additional manuscript changes were needed after the final compilation.

| Location | Original | Type | Severity | Necessary caveat? | Why it feels defensive | Likely reviewer reaction | Recommended action | Rewrite |
|---|---|---|---|---|---|---|---|---|
| ch02, retrieval | The generated document guides retrieval; the retrieved source documents supply the evidence used downstream. | CLEAN | None | Technical distinction | Explains the different roles of generated queries and source evidence. | Clarifies HyDE without inventing provenance. | Retain. | Unchanged. |
| ch02, few-shot adaptation | These visual-learning settings establish related adaptation problems; incremental few-shot text classification introduces successive rounds of text labels and limited examples. | NECESSARY_CAVEAT | None | Yes | Identifies the domain and protocol difference in cited work. | Avoids presenting visual-learning studies as text experiments. | Retain. | Unchanged. |
| ch07, evaluation | Its source-defined ROUGE-L quantity divides longest-common-subsequence length by generated-answer length. | NECESSARY_CAVEAT | None | Yes | States the actual source metric. | Prevents confusion with alternative ROUGE-L conventions. | Retain. | Unchanged. |
| ch07, limitations | GORAG starts from sparse support data and can retain errors through prediction-derived updates. | NECESSARY_CAVEAT | None | Yes | Gives a concrete error-propagation mechanism. | Scientifically useful limitation. | Retain once in this limitations discussion. | Unchanged. |
| ch08, feedback | An online correction becomes available after the original prediction, and an answer assessment can guide only subsequent retrieval. | NECESSARY_CAVEAT | None | Yes | Specifies information availability. | Makes the future evaluation protocol interpretable. | Retain. | Unchanged. |

## Paper-level defensive-writing score

**1/10**, qualitative editorial assessment. No critical or major defensive passages were identified in the current review. The Abstract and Introduction motivate the methods through data and task requirements. Discussion states protocol differences directly; Conclusion describes the implemented progression. Necessary metric, timing and coverage conditions remain concise.

## Highest-priority removals

No additional deletion was justified in the current expanded paragraphs. The preceding author-led wording pass already removed repeated explanations and abstract editorial wording. The expansion adds named methods and the technical distinctions needed to connect them to the thesis, without calling the evidence comprehensive, fair or sufficient.

## Necessary caveats to preserve

- Existing-graph coverage and the annotation label vocabulary constrain KGLink's input and supervised predictor.
- GORAG's cumulative index uses the information available at each prediction, including prediction-derived associations.
- AGRAG's coverage and faithfulness measure different aspects of an answer; its source metric definition remains explicit.
- MGRAG's extraction, caption ranking and accepted matches affect what can enter retrieval and cache processing.
- Source-internal theory and unreported experimental recomputation settings remain recorded rather than being replaced by invented claims.

## Repeated phrase audit

Counts below use the abstract and eight chapter files, excluding LaTeX comments. “while” and “however” are context indicators, not automatic violations; inspected occurrences express model, evidence or protocol differences.

| Pattern | Occurrences |
|---|---:|
| we do not claim | 0 |
| to ensure fairness | 0 |
| it should be noted | 0 |
| taken together | 0 |
| preliminary | 0 |
| promising / encouraging / compelling | 0 |
| em dash / LaTeX triple hyphen | 0 |
| while | 87 |
| however | 3 |

No sentence-level em dash or `---` appears in these narrative files. The retained colons belong to RQ headings and the original titles of KGLink, GORAG, AGRAG and MGRAG; the source comments do not print. Mathematical ranges and LaTeX double hyphens used for relations or names are not sentence-level em dashes.
