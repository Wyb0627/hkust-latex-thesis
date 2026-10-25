"""Apply the independently reviewed round-two manuscript corrections once."""
from pathlib import Path
import json,re
texts={p:p.read_text() for p in Path('chapter').glob('ch*.tex')};changes=[]
def replace(file,old,new,kind='redundancy',evidence='Independent full-manuscript review'):
 p=Path('chapter')/file;s=texts[p]
 if s.count(old)!=1:raise ValueError((file,s.count(old),old[:100]))
 texts[p]=s.replace(old,new,1);changes.append({'file':str(p),'kind':kind,'before':old,'after':new,'evidence':evidence})
def para(file,prefix,new='',kind='redundancy',evidence='Independent full-manuscript review'):
 p=Path('chapter')/file;s=texts[p];start=s.index(prefix);end=s.find('\n\n',start)
 if end<0:end=len(s)
 replace(file,s[start:end],new,kind,evidence)
# Introduction: one research argument, with experiment details beside the actual evidence.
f='ch01-introduction.tex'
replace(f,'A language model often receives a question together with a collection of text, table cells, or images.','Language-model pipelines use text, table cells, and images as evidence for prediction or generation.')
para(f,'These problems connect through the interface between evidence and prediction.','The common question is how explicit relationships should constrain the evidence used for a task. KGLink selects descriptions for a supervised representation; GORAG selects labels from an evolving index; AGRAG selects connected facts and source context; and MGRAG matches query relations and allocates computation over the selected evidence. Across these studies, the thesis examines where structure is obtained, when it is adapted, and which downstream decision it controls.','shared-thread')
replace(f,"This distinction is relevant to the title's use of \\emph{language models}. The thesis includes both a supervised encoder-based annotation method and retrieval-augmented generation systems.","The thesis therefore includes supervised encoder-based annotation and retrieval-augmented generation.")
replace(f,'An existing knowledge graph precedes online task indexing in the presentation; connected textual evidence precedes query-aware multimodal matching. ','')
for prefix in ['They also determine the interpretation of an ablation.','This focus on interfaces separates several quantities that can otherwise be conflated.','The distinction is especially useful for comparing the studies.']:para(f,prefix)
replace(f,'The contribution statements describe the technical changes; the research chapters retain their measured results and conditions.','')
for old in [' The contribution is evaluated through column annotation, component ablations, and cases with different graph coverage.',' The evaluation measures accuracy across rounds and shot conditions together with resource costs.',' Its evaluation separates tasks requiring isolated facts, multiple facts, summaries, flexible generation, and labels, and tests the effects of its component choices.',' The experiments examine multimodal answer quality, matching alternatives, construction and retrieval ablations, and serving costs.']:replace(f,old,'')
# Background: remove a third catalogue of the same four contributions.
f='ch02-background.tex';para(f,'The term structural augmentation in this thesis covers these explicit uses of relationships.')
# KGLink: exact source cap, concise integration, no unit inferred for the original 9.70.
f='ch03-kglink.tex'
replace(f,'and long tables are split by columns','and wide tables are split by columns','precision','KGLink source implementation divides tables with more than eight columns')
replace(f,'The experimental implementation retrieves at most ten entities per cell mention.','The experimental implementation retrieves at most ten entities per cell mention. From the KG entities in each column, it generates up to three candidate types per row, as specified in the original implementation.','method-condition','KGLink controlling PDF p.9 §IV.B; original KGLink.tex:663 (source says per row)')
replace(f,'Its effect is an empirical question because the score measures linkage rather than the semantic diversity of the selected values. ','')
para(f,'The repeated classification positions retain the association between an output vector and its target column.',"Each column's \\texttt{[CLS]} position produces a contextual vector using the serialized columns. Candidate-type text precedes the corresponding cell values, allowing both to interact with neighboring columns through self-attention. KGLink separately encodes the feature sequence into a column-specific vector and combines it with the contextual column vector through the composition function $\\phi$. The resulting representation is mapped into the dataset's classification space.")
para(f,'The processed column includes candidate-type information as well as retained cell values.')
replace(f,'The order of the two distributions follows the published expression. ','')
replace(f,' The experiment evaluates the trained models on the selected missing-linkage subset.','')
para(f,"KGLink's graph stage supplies additional evidence when retrieval succeeds,")
para(f,'The qualitative analysis examines classes whose accuracy changes when the representation-generation task is added.','Among SemTab classes with more than ten test samples, Athlete, Protein, and Film have the three largest reported accuracy increases when the representation-generation task is added.','ambiguous-source-quantity','Controlling PDF p.12 §V.D and KGLink.tex:874 both give 9.70 with no unit; omit that quantity rather than invent percent/percentage points')
replace(f,"The qualitative cases explain the kind of mismatch targeted by the method, while the task-removal ablation measures its aggregate effect under the reported protocol.",'')
# GORAG: keep support/query protocol and actual graph operations; remove repeated admonitions.
f='ch04-gorag.tex'
replace(f,"The associated label is the model's prediction, which introduces an important distinction between supervised initialization and subsequent online expansion. The system receives true labels for the few-shot support examples; it does not receive the true label of a query before predicting that query. This information boundary defines the interpretation of the online evaluation.","The predicted label associates the newly observed keywords with a class for subsequent retrieval. Support examples initialize the graph using their supplied labels.")
replace(f,"Maintaining these statistics does not provide the query's correct class. ",'')
replace(f,'Individual support documents are used to construct this representation; they are not defined as a third category of exemplar nodes in the graph.','Support documents contribute keyword--label associations to this representation.')
replace(f,"The graph does not encode a fixed rule that every occurrence of a keyword implies the same class.",'')
replace(f,'Consequently, a retrieved path should be interpreted as an operation on the constructed index, with these distinct edge semantics, rather than as a sequence of independently observed real-world relations.','A retrieved path can therefore combine observed keyword associations with label bridges introduced during merging.')
for prefix in ['The distinction between terminals and intermediate nodes is central.','The auxiliary tree and the returned structure have different vertex sets.','The retrieval procedure favors a connected explanation of the mapped keywords over independently selecting a fixed number of labels for each keyword.']:para(f,prefix)
para(f,'This expression makes the retrieval output explicit.','Representative keywords and label descriptions are added to the classification prompt for the labels selected by this intersection.')
para(f,'Adaptation concerns candidate selection after query mapping.')
para(f,'The prediction precedes the update.',"The prediction precedes insertion, so a new keyword's association can affect later queries but not the prediction that created it. Incorrect predicted labels can propagate through those associations. The offline ablation suppresses online expansion, measuring its contribution relative to an index that receives no such query-dependent additions.")
para(f,'This distinction also determines what an evaluation result measures.')
replace(f,'Comparing the fourth-round ten-shot score to the first-round one-shot score would mix these conditions.','')
replace(f,'Comparisons use methods evaluated under the same round and support conditions.','')
para(f,'The results establish different patterns on different datasets.','WOS improves with additional support in the displayed rounds, whereas IFS-Rel is non-monotonic across support sizes and CAD loses accuracy as labels accumulate.')
para(f,'The full-method row of this ablation table differs from the full-method row of the main WOS table.',"The publication gives different full-method values in the main and ablation WOS tables without explaining their provenance. Component comparisons here use the full-method row from the ablation table.",'source-boundary','GORAG controlling PDF main Table2 vs ablation Table3; no run/seed reconciliation established')
replace(f,' It does not measure a classifier with no external label information.','')
para(f,'The zero-shot result also illustrates why support size is not the only determinant of graph content.')
para(f,'This construction lets the study display behavior at later rounds while retaining a sufficient test collection in each split.')
para(f,'This case illustrates the operation of retrieval for one text.')
para(f,'The online component changes the source of that evidence.',"The offline ablation shows the contribution of expanding the index beyond the support sample. Because these additions carry predicted labels, the method couples current classification with the evidence available to later queries.")
# AGRAG: distinguish an operational connection from an unspecified indexing order.
f='ch05-agrag.tex'
replace(f,'It is a qualitative account of evidence selection; quantitative evaluation is provided separately in Section~\\ref{sec:agrag:experiments}.','')
replace(f,'The pseudo connection is an indexing device','The pseudo connection is a connectivity device','lifecycle-precision','AGRAG selected main method introduces pseudo node after query-dependent scoring; no fixed insertion order inferred')
replace(f,'a high-cost indexing connection','a high-cost connectivity connection','lifecycle-precision')
replace(f,' Equations~\\ref{eq:agrag:extraction-score}--\\ref{eq:agrag:entities} preserve the source formulation.','')
replace(f,'These expressions retain the distinct roles assigned to the candidate score and subgraph quantity in the method. This describes the paper\'s expansion rule separately from the initial tree construction.','The candidate ratio therefore ranks possible additions using their assigned node scores, while the current subgraph is evaluated by Equation~\\ref{eq:agrag:mcmi-objective}.')
para(f,'This case also distinguishes structural inclusion from answer generation.')
replace(f,"The graph records relationships in the indexed evidence; the generated answer remains the language model's response conditioned on that evidence.",'')
para(f,'These distinctions explain why multiple metrics are retained.')
for old in [' The reported improvements concern this protocol and corpus.',' Each column retains the metric and query collection of its corresponding task.',' This is why the chapter retains both faithfulness and coverage rather than summarizing the ablation as uniform improvement.',' It measures the downstream consequence of that replacement; the aggregate scores alone do not identify every intermediate graph error.']:replace(f,old,'')
replace(f,"AGRAG's efficiency therefore needs to be read together with the task results and the individual cost components. AGRAG reduces indexing time in these comparisons while its query totals remain above HippoRAG2 on Novel and Medical.",'')
# MGRAG: semantic failure is search failure, not an infeasibility certificate.
f='ch06-mgrag.tex'
replace(f,'The matcher returns an empty result when no valid correspondence exists in its current graph.','The matcher returns an empty result when its search finds no valid correspondence in the current graph.','algorithm-precision','Publisher Algorithm1 empty result set; greedy Algorithm2 may miss an otherwise feasible path')
for old in [' These facts are the content of the published illustrative example.','The objective and constraints follow the published formulation. ','It preserves the incremental operation described in the published construction procedure.']:replace(f,old,'')
replace(f,'\\REQUIRE Query graph $\\mathcal{QG}_q$, evidence graph $\\mathcal{KG}_q$, threshold $\\theta$','\\REQUIRE Query graph $\\mathcal{QG}_q$, query anchor $\\gamma$, evidence graph $\\mathcal{KG}_q$, threshold $\\theta$','algorithm-loop','Publisher PDF p.2485 Algorithm1 inputs anchor and loops over threshold-qualified evidence counterparts')
replace(f,'\\STATE Select an anchor correspondence and enumerate candidate mappings\n\\FOR{each candidate mapping $I$}','\\FOR{each $v\\in\\mathcal V_q$ with $\\cos(\\mathbf h_v,\\mathbf h_\\gamma)>\\theta$}\n\\STATE Enumerate candidate mappings consistent with $I(\\gamma)=v$\n\\FOR{each candidate mapping $I$}','algorithm-loop','Publisher PDF Algorithm1 lines2–4')
replace(f,'\\ENDFOR\n\\STATE Return the highest-scoring result, or $\\varnothing$ if $\\mathcal R$ is empty','\\ENDFOR\n\\ENDFOR\n\\STATE Return the highest-scoring result, or $\\varnothing$ if $\\mathcal R$ is empty','algorithm-loop','Publisher PDF Algorithm1 collects all counterpart results before maximum selection')
replace(f,'An anchor limits the subsequent search to mappings consistent with its correspondence.','For the selected query anchor, Algorithm~\\ref{alg:mgrag:matching} considers each evidence counterpart exceeding the threshold and enumerates mappings consistent with that correspondence.','algorithm-loop')
para(f,'{\\clubpenalty=10000\nThe construction and matching substitutions supply a second level of comparison.', 'Component substitutions evaluate graph construction, semantic matching, and cache policy within MGRAG. Inverse ablations add matching and recomputation to other retrieval systems.')
para(f,'The comparisons have four roles.')
replace(f,' The reported gains vary with the dataset and metric.','')
replace(f,'The margins are therefore uneven. The table supports a consistent advantage for the full matching choice across the reported metric rows, with the magnitude determined by dataset and metric.','MGRAG leads the displayed metric rows, with smaller MMQA and Web accuracy margins than the Wiki accuracy margin.')
para(f,'The matching experiment measures downstream answers after each substitution.')
replace(f,' The hop-specific values retain the measured trade-off for each question group.','')
replace(f,'Reporting both values preserves the contribution of the cache policy without assuming that every application of recomputation reduces total runtime. ','')
para(f,'The result also depends on the retrieval pipeline paired with the cache.','Section~\\ref{sec:mgrag:ablations} compares these component additions within the HippoRAG2 and VanillaRAG pipelines.')
replace(f,'The end-to-end measurement is retained separately from the listed module times. The original totals and their reported precision are preserved.','The listed module times do not sum to the reported end-to-end total; the publication does not reconcile the difference in this breakdown.','cost-accounting','Publisher Table5 MMQA KGC193.0/Match0.14/QA8.9/E2E248.1; no explanation invented')
# Discussion: correct the LM role and add one concrete cross-study controls matrix.
f='ch07-discussion.tex'
replace(f,'Keyword extraction and classification','Label-description generation and classification','model-role','GORAG PDF Eq2 statistical TF-IDF; Eq11/12 model-generated label information/classification')
replace(f,'Table~\\ref{tab:discussion:roles} records these roles without requiring the studies to share an implementation. ','')
para(f,'This variation explains why the thesis retains task-specific metrics.',r'''Table~\ref{tab:discussion:controls} brings the main experimental conditions into the comparison. KGLink evaluates a trained encoder, whereas the other studies evaluate generative pipelines with different backbones. Even when a dataset name recurs, its supervision and update protocol can change: GORAG's WOS and IFS-Rel experiments accumulate labels and predicted-keyword associations over rounds, while AGRAG indexes one training passage per label for its classification setting. These experiments answer different questions about the use of structure.

\begin{table}[tbp]
\centering\small
\caption{Main experimental conditions across the four studies. Hardware denotes the reported local setup; GORAG's IFS-Rel generation uses the GPT-4o service. Full task-specific controls appear in the corresponding research chapters.}
\label{tab:discussion:controls}
\begin{tabular}{>{\raggedright\arraybackslash}p{0.11\textwidth}>{\raggedright\arraybackslash}p{0.26\textwidth}>{\raggedright\arraybackslash}p{0.28\textwidth}>{\raggedright\arraybackslash}p{0.23\textwidth}}
\toprule
Study & Main model and hardware & Supervision and evidence state & Reported outcome\\
\midrule
KGLink & BERT; Tesla V100 & 7:1:2 labeled-column split; external KG; three-run averages & Annotation accuracy and weighted F1 on a percentage scale\\
GORAG & Qwen2.5-7B on CAD/WOS; GPT-4o on IFS-Rel; A100 40 GB & 1/5/10 support texts per label; cumulative labels; prediction-dependent index updates & Exact-label accuracy by round and support size\\
AGRAG & Qwen2.5-14B-Instruct; A100 80 GB & Fixed corpus graph; query-conditioned scores and subgraph; one training passage per label for classification & Task-specific QA assessment/overlap, coverage, faithfulness, and classification metrics\\
MGRAG & Qwen2.5-VL-7B-Instruct; A100 40 GB & Query-specific multimodal graph; semantic matching; selective KV recomputation & Answer quality, TTFT, and complete-system/module costs\\
\bottomrule
\end{tabular}
\end{table}

A shared metric label can also conceal a different assessment rule. GORAG's accuracy requires the predicted class to match the gold label. AGRAG's QA accuracy uses model judgments scored 0, 0.5, or 1, while its classification accuracy uses label correctness. Its source-defined ROUGE-L quantity divides longest-common-subsequence length by generated-answer length. MGRAG reports answer accuracy alongside semantic similarity and lexical overlap. The synthesis therefore relates structural mechanisms to their corresponding measurements; it does not pool these scores into a single cross-task accuracy.''','experimental-consistency','Sources independently checked in round2 scientific reviews; no common model/protocol inferred')
start=texts[Path('chapter')/f].index('\\section{Choosing the Unit of Adaptation}');end=texts[Path('chapter')/f].index('\\section{Limitations and Open Questions}',start)
old=texts[Path('chapter')/f][start:end]
replace(f,old,r'''\section{Error Propagation Across Structural Decisions}
\label{sec:discussion:unit}
The location of a structural decision affects how an error can propagate. An incorrect KGLink entity link changes the descriptions offered to the encoder for a table. In GORAG, an incorrect predicted label can become an association available to later queries. AGRAG reuses a corpus graph, so an extracted relation can influence several query-specific selections. MGRAG constructs a new graph for each query, but a mistaken accepted match can end construction before later chunks are examined. These consequences follow from the lifecycles of the four evidence structures.

They identify different targets for feedback. Entity disambiguation concerns the link from a cell to external knowledge. Online correction concerns an association already inserted into an index. Relation verification concerns the connection from graph content to source passages. Matching diagnosis concerns entity alignment, relation semantics, and the path search. Evaluating feedback at those stages would connect an observed answer or classification error to the structural decision that made the evidence available. Chapter~\ref{ch:conclusion} develops this direction while retaining the sequence in which feedback becomes available.

''','shared-thread','Cross-chapter synthesis from operational evidence lifecycles; prospective feedback is not presented as an experiment')
# Conclusion: findings first, with no invented general guarantee.
f='ch08-conclusion.tex'
para(f,'The first research question concerned the combination of external knowledge and table representations.',"KGLink's component comparisons show benefits from graph-derived evidence and contextual type-representation training. Its no-linkage subset also shows continued annotation through the table encoder when retrieved KG evidence is absent. External descriptions enter a supervised mapping to the annotation vocabulary, with cross-column filtering determining which descriptions are available.",'conclusion-inference')
para(f,'The second research question concerned retrieval under evolving few-shot supervision.',"GORAG's offline ablation shows the contribution of expanding the keyword--label index with earlier predictions under its round protocol. Additional support and cumulative label growth have dataset-dependent effects, including non-monotonic results on IFS-Rel. The study makes evidence maintenance part of dynamic classification: current decisions shape associations available to later candidate retrieval.",'conclusion-inference')
para(f,'The third question concerned the organization of evidence for textual generation.',"AGRAG's ablations distinguish answer coverage from support for the claims actually generated. Removing hybrid passages can retain a high faithfulness score while reducing coverage; replacing the expanded subgraph with its initial tree affects tasks differently. Connected graph facts and passage context therefore serve complementary evidence needs in the evaluated generation tasks.",'conclusion-inference')
para(f,'The fourth question concerned semantic correspondence and computation over multimodal evidence.',"MGRAG's construction and matching comparisons support query-dependent extraction and semantic paths for the evaluated multimodal questions. Its cache comparisons show that the selected graph can also inform token-state recomputation. Component additions improve answer quality with runtime changes that depend on the host pipeline, extending structural evidence use into context processing.",'conclusion-inference')
# Commit only after every exact-match operation succeeds.
for p,s in texts.items():
 s=re.sub(r'\n{3,}','\n\n',s);p.write_text(s)
Path('planning/review-round2/applied-edits.json').write_text(json.dumps(changes,indent=2))
print(len(changes),'reviewed manuscript edits applied')
