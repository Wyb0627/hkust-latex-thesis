"""Apply individually reviewed prose edits; save evidence and phrase counts."""
from pathlib import Path
import re,json
edits=[
('ch01-introduction.tex','The progression through the chapters introduces new task conditions rather than a sequence of dependent software modules.','The chapters progress through external knowledge, online indexing, connected textual evidence, and query-aware multimodal evidence.','D12','MIXED','The separate implementation scope is already stated in the preceding sentence.'),
('ch02-background.tex','It identifies the object made available to the retrieval computation, rather than assigning a common empirical ranking across their different experiments.','It identifies the evidence object made available to each retrieval computation.','D12','DEFENSIVE','The table describes methods and contains no empirical scores.'),
('ch02-background.tex','The selected table illustrates the result associated with the main discussion of graph reception and qualifier integration; it is not an average over the four datasets.','The selected table illustrates graph reception and qualifier integration on these two datasets.','D12','DEFENSIVE','The caption already identifies the selected dataset columns.'),
('ch04-gorag.tex','The superscript $r$ identifies the current task state; it is not a model layer or a reasoning step within one prediction.','The superscript $r$ identifies the current classification round.','D9','DEFENSIVE','The chapter has already defined rounds; imaginary alternative meanings distract.'),
('ch04-gorag.tex','The graph does not obtain a supervised probability of classification correctness from this formula. Instead, the score determines which lexical units are indexed and how expensive their associations will be in the retrieval structure.','The score determines which lexical units are indexed and how expensive their associations will be in retrieval.','D12','MIXED','The distinction between extraction score and model confidence is already made.'),
('ch04-gorag.tex','Describing every intermediate structure as an exact optimum for the original terminal problem would obscure which vertices are required and which connections have been chosen by the heuristic.','GORAG uses these intermediate structures to construct a heuristic connection among the query terminals.','D1','MIXED','The technical distinction should state the actual operation.'),
('ch04-gorag.tex','The adaptive property concerns candidate selection after the query has been mapped. It does not remove every parameter from the system. Keyword extraction still uses a score and an extraction rule. The language model and its prompts also remain part of the configuration.','Adaptation concerns candidate selection after query mapping. Keyword extraction, the language model, and its prompts remain configured components.','D8','MIXED','A compact positive scope statement preserves the configured parameters.'),
('ch04-gorag.tex','These values show that adapting the retrieval mechanism does not remove the difficulty of later rounds. The relevant empirical observation is the comparison with the other methods under those conditions, rather than a claim that the task\'s accuracy remains constant as labels accumulate.','Accuracy decreases in later rounds as the cumulative label set grows. Comparisons use methods evaluated under the same round and support conditions.','D2','MIXED','The negative hypothetical claim is unnecessary; preserve the measured trend and protocol.'),
('ch05-agrag.tex','The distinction between these roles is necessary for understanding both the method and its ablation. Replacing entity extraction changes the nodes provided to later stages; it does not remove every model-generated component from the graph.','The entity-extraction ablation changes the nodes supplied to subsequent relation extraction and retrieval.','D12','MIXED','Model roles are already named explicitly in the previous sentence.'),
('ch05-agrag.tex','This retains the operator entries given in the main paper, including the nonedge term. It is used with the recurrence and damping value in Equation~\\ref{eq:agrag:propagation}. Its definition is therefore part of the reported influence-scoring configuration, alongside the subsequent passage-node scaling.','Nonadjacent node pairs receive the constant term in this operator. The recurrence uses this matrix with the damping value in Equation~\\ref{eq:agrag:propagation}, followed by passage-node scaling.','D9','MIXED','Explain the defined operator directly; keep the unusual nonedge term explicit.'),
('ch05-agrag.tex','The thesis retains those objects explicitly rather than treating a graph as a cost-free representation.','These objects contribute to the index storage.','D1','DEFENSIVE','No competing claim of cost-free storage has been made.'),
('ch05-agrag.tex','The curves and heatmaps are not converted into additional inferred numerical results.','','D9','DEFENSIVE','An editorial procedure belongs in the verification ledger; the original figure supplies the evidence.'),
('ch06-mgrag.tex','A high-ranked chunk is consequently a candidate for relational extraction; it is not automatically accepted as sufficient evidence.','A high-ranked chunk becomes a candidate for relational extraction and subsequent matching.','D12','MIXED','State the actual stage transition positively.'),
('ch06-mgrag.tex','The method does not train a separate token-importance predictor on the evaluation queries. Its score instead uses the graph and attention information available during processing.','The recomputation score uses graph and attention information available during processing.','D9','DEFENSIVE','An unproposed training alternative distracts from the actual score.'),
('ch06-mgrag.tex','The curves are retained as figures; no numerical points are estimated from their plotted pixels.','','D9','DEFENSIVE','Keep extraction procedure in the source ledger, not the research interpretation.'),
('ch07-discussion.tex','The overall argument draws on the technical role of structure and the corresponding component evidence; it does not require numerical averaging across those outcomes.','The comparison relates each structural operation to its task metrics and component evidence.','D12','DEFENSIVE','Cross-task averaging is not proposed; compare the mechanisms directly.'),
('ch07-discussion.tex','A component that improves answer quality can also add work, while a whole system can achieve a favorable operating point through several interacting choices.','A component that improves answer quality can also increase runtime; the system comparison measures their combined quality and cost.','D10','MIXED','Replace favorable operating point with named measured quantities.'),
]
root=Path('chapter');before='\n'.join(p.read_text() for p in root.glob('ch*.tex'))
rows=[]
for file,old,new,typ,classification,why in edits:
 p=root/file;s=p.read_text()
 if old not in s:
  if new and new in s:continue
  raise SystemExit('Unmatched style edit: '+file+' '+old[:50])
 s=s.replace(old,new,1);p.write_text(s)
 rows.append([file,old,typ,'Minor' if typ=='D9' else 'Major',classification,why,'The explanation may sound like an answer to an objection rather than a description of the study.','Delete' if not new else 'Rewrite',new or '(Deleted)'])
patterns=['reported','rather than','does not','do not','not claim','it should be noted','we emphasize','for a fair comparison','together,','taken together','within the evaluated','instead of','important','robust','promising']
after='\n'.join(p.read_text() for p in root.glob('ch*.tex'))
counts={x:{'before':len(re.findall(re.escape(x),before,re.I)),'after':len(re.findall(re.escape(x),after,re.I))} for x in patterns}
Path('planning/qa/style-phrase-counts.json').write_text(json.dumps(counts,indent=2))
def safe(s):return s.replace('|','\\|').replace('\n',' ')
head='''# Whole-manuscript defensive-writing audit — 2026-10-24

Applied the academic-defensive-writing-auditor skill after source verification. Scope: abstract, Introduction and contribution statements, all four research chapters, common Background, Discussion and Conclusion. Earlier chapter audits remain supporting records. The edits below do not change results, formulas, protocols or evidence strength.

| Location | Original | Type | Severity | Necessary caveat? | Why it feels defensive | Likely reviewer reaction | Recommended action | Rewrite |
|---|---|---|---|---|---|---|---|---|
'''
text=head+''.join('| '+' | '.join(map(safe,r))+' |\n' for r in rows)
text+='''
## Paper-level defensive-writing score

Before this integration pass: 4/10 (mild, concentrated in repeated evidence-boundary explanations). After the listed edits: 2/10. This is a qualitative editorial judgment, not an automated quality metric. Some `reported` constructions remain because they distinguish original measurements and source-level formulations from thesis synthesis.

## Highest-priority removals

1. Remove editorial assurances about not inferring figure pixels from research prose.
2. State the scope of adaptive retrieval directly, without arguing that other parameters still exist.
3. Replace hypothetical incorrect interpretations of the Steiner procedure with its actual heuristic operation.
4. Describe the propagation operator directly, retaining its unusual nonedge term.
5. Remove the duplicate introduction statement about chapter publication sources.
6. Replace promotional cost-language with measured quality and runtime quantities.

## Necessary caveats to preserve

- GORAG online updates use predictions rather than query gold labels; the zero-shot initialization and stitched round-generalization plot have different information/partition conditions.
- KGLink's SemTab MTab accuracy and missing weighted-F1 require the task-definition boundary; graph coverage affects no-linkage cases.
- AGRAG's ROUGE-L denominator and model-assessed ACC are the source-specific metrics; main and ablation efficiency measurements remain separate. Statistical entity selection coexists with model-extracted relations.
- The initial tree's source approximation statement does not establish a guarantee for the expanded sum objective. The propagation operator is retained as defined, without an invented normalization.
- MGRAG's greedy path search can miss valid paths. Its threshold condition is conditional on an accepted match. The numerical fixed recomputation budget is unreported in the selected experimental tables.
- Missing MGRAG entries mean experiments exceeded three days. Module times and end-to-end times are separate original measurements.
- Hardware, backbones, support size, query counts and per-task metrics remain attached to their results.

## Repeated phrase audit

Counts are literal case-insensitive occurrences in chapter source prose, including captions/comments. They flag constructions for review, not an instruction to remove every occurrence.

| Construction | Before | After |
|---|---:|---:|
'''
for k,v in counts.items():text+=f"| {k} | {v['before']} | {v['after']} |\n"
text+='\nNo reviewer-facing prebuttal was found in the abstract or contribution bullets. Remaining negative sentences were reviewed for metric definitions, algorithm conditions, missing values or experimental boundaries. Source inconsistency details are held in the verification records rather than expanded into a thesis-wide disclaimer.\n'
Path('planning/STYLE_AUDIT.md').write_text(text)
print(len(rows),'edits applied')
