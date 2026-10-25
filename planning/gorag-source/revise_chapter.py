from pathlib import Path
p=Path('chapter/ch04-gorag.tex');s=p.read_text()
a=s.index('The selected source first computes a minimum spanning tree')
b=s.index('Once the expanded structure',a)
s=s[:a]+'''GORAG uses a greedy terminal-connecting procedure based on Mehlhorn's algorithm~\\cite{gorag-mehlhorn1988faster}. The mapped keywords serve as terminals. An auxiliary graph $H$ represents connections between terminals, with edge weights given by path costs. A minimum spanning tree of $H$ selects a collection of terminal connections. Expanding these connections into their underlying paths produces the graph structure used for candidate selection. The language model then receives the labels encountered in this structure.

The auxiliary tree and the returned structure have different vertex sets. The auxiliary tree expresses connections among the terminals. Their expanded paths can also contain keyword and label nodes that were not terminals. These intermediate nodes provide the connection between the query's lexical evidence and the candidate classes. The terminal set changes from query to query, while the costs reflect the graph accumulated at the current round.

The retrieval procedure favors a connected explanation of the mapped keywords over independently selecting a fixed number of labels for each keyword. A label may be included because it connects several terms, and an additional keyword node may connect terms that have no direct edge. The returned structure can therefore express joint evidence that would be lost if each terminal were treated as an independent lookup. Its label intersection is the compact output used by classification.
% G1: author directed main-text precedence over conflicting appendix pseudocode. This operational account follows main-text terminal/auxiliary-tree/path-expansion steps. No new ratio or corrected proof is asserted.

'''+s[b:]
s=s.replace('The selected research source calculates','GORAG calculates').replace('the selected source reports','GORAG reports')
s=s.replace('Its exact factors determine','These factors determine')
# Add original unmodified figures at appropriate places.
insert='''
\\begin{figure}[tbp]
\\centering
\\includegraphics[width=0.9\\linewidth]{figures/gorag/DFSTC_task.pdf}
\\caption{Two rounds of the dynamic classification task. New abuse categories extend the available labels. Reproduced from Figure 1 of GORAG~\\cite{gorag-paper}.}
\\label{fig:gorag:task}
\\end{figure}

'''
s=s.replace('\\subsection{Rounds and information availability}',insert+'\\subsection{Rounds and information availability}')
insert='''
\\begin{figure}[tbp]
\\centering
\\includegraphics[width=\\linewidth]{figures/gorag/GORAG_pipeline_example_new.pdf}
\\caption{GORAG's offline indexing, query-dependent retrieval, classification, and online update. New query keywords are associated with the predicted class after classification. Reproduced from Figure 2 of GORAG~\\cite{gorag-paper}.}
\\label{fig:gorag:pipeline}
\\end{figure}

'''
s=s.replace('\\subsection{Keyword extraction and correlation scores}',insert+'\\subsection{Keyword extraction and correlation scores}')
insert='''
\\begin{figure}[tbp]
\\centering
\\begin{minipage}{0.48\\linewidth}\\centering
\\includegraphics[width=\\linewidth]{figures/gorag/runtime_wos.pdf}\\par (a) WOS.
\\end{minipage}\\hfill
\\begin{minipage}{0.48\\linewidth}\\centering
\\includegraphics[width=\\linewidth]{figures/gorag/runtime_cad.pdf}\\par (b) CAD.
\\end{minipage}
\\caption{Total time in minutes for the one-shot four-round experiments with Qwen2.5-7B. The original R1--R4 legend in panel (b) applies to both panels. Reproduced from Figure 3 of GORAG~\\cite{gorag-paper}.}
\\label{fig:gorag:runtime}
\\end{figure}

'''
s=s.replace('\\section{Zero-shot and Round Generalization}',insert+'\\section{Zero-shot and Round Generalization}')
insert='''
\\begin{figure}[tbp]
\\centering
\\begin{minipage}{0.48\\linewidth}\\centering
\\includegraphics[width=\\linewidth]{figures/gorag/wos_4_round_1.pdf}\\par (a) One-shot.
\\end{minipage}\\hfill
\\begin{minipage}{0.48\\linewidth}\\centering
\\includegraphics[width=\\linewidth]{figures/gorag/wos_4_round_5.pdf}\\par (b) Five-shot.
\\end{minipage}
\\caption{WOS classification across the reported round splits. Points 1--4 use the four-round split, 5--6 the six-round split, and 7--8 the eight-round split. The legend in panel (b) applies to both panels. Reproduced from Figure 4 of GORAG~\\cite{gorag-paper}.}
\\label{fig:gorag:rounds}
\\end{figure}

\\subsection{A retrieved classification case}
\\label{sec:gorag:case}

Figure~\\ref{fig:gorag:case} reproduces a contextual-abuse example from the original study. The query contains the terms highlighted in red. These terms map to keyword nodes, and the selected connecting structure passes through an insult label. The classifier outputs the abuse category shown in the figure. This example exposes the relationship between the extracted query evidence, the intermediate label node, and the final classification.

The useful property of the example is that candidate selection has a visible provenance. The label is connected to more than one term in the indexed representation. The displayed nonterminal neighbor also shows that a keyword neighborhood can contain more information than the connection chosen for the current text. Selecting a structure distinguishes the evidence used to connect the query terms from other associations present around the same label.

This case illustrates the operation of retrieval for one text. The accuracy tables quantify the decisions over the test collections, and the ablation table measures the contribution of changing specific pipeline components. These evidence types answer different questions. The example explains how a candidate appears in the classifier's input, while the aggregate results measure whether the resulting predictions match the required classes across the evaluation data.

\\begin{figure}[tbp]
\\centering
\\includegraphics[width=0.75\\linewidth]{figures/gorag/new_case.pdf}
\\caption{A contextual-abuse example and its selected graph connections. The offensive text is retained as part of the original dataset illustration. Reproduced from Figure 5 of GORAG~\\cite{gorag-paper}.}
\\label{fig:gorag:case}
\\end{figure}

'''
s=s.replace('\\section{Discussion and Chapter Summary}',insert+'\\section{Discussion and Chapter Summary}')
# Add computational organization from undisputed construction expression.
insert='''
\\subsection{Computational organization}
\\label{sec:gorag:computation}

The graph separates work performed at a label update from work performed for each query. Offline indexing processes the supplied texts, creates or updates keyword associations, generates label information when available, and merges the round's graph. The cross-round label bridges introduce interactions between the newly indexed and earlier label regions. In the source's abstract operation count, construction is expressed as
\\begin{equation}
O\\!\\left(|\\mathcal{Y}^r||\\mathcal{Y}^{r-1}|+|\\mathcal{V}_{\\mathrm{new}}^r||\\mathcal{D}^r|\\right).
\\label{eq:gorag:constructioncost}
\\end{equation}
The two terms account for label merging and keyword--text processing. This count treats the associated text-processing and graph operations at the granularity used in that analysis. The number of tokens processed by a language-model call depends on the prompt and generated output, so the empirical token study supplies a separate measurement of model-facing work.

Per-query processing maps the extracted terms to the existing graph, obtains a connecting structure, builds the classification prompt, and inserts new terms after prediction. The index state can therefore grow during one round as well as between label rounds. Graph memory and prompt length measure different consequences of that growth. A larger stored index can provide more candidate associations while a query still receives only the labels selected by its own retrieval structure. The resource experiments report these two quantities separately.

'''
s=s.replace('\\section{Experimental Design}',insert+'\\section{Experimental Design}')
s=s.replace('% Working chapter, 2026-10-24. Publisher PDF comparison PENDING.','% Working chapter, 2026-10-24. Author-confirmed publication-equivalent arXiv v4 compared; see evidence ledger.')
p.write_text(s)
