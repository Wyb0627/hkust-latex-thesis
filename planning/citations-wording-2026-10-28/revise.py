"""Apply exact, logged prose edits against the author's saved working copy."""
from pathlib import Path
import json

out = Path(__file__).resolve().parent
edits = []

def change(file, before, after, reason):
    p = Path(file)
    text = p.read_text()
    assert text.count(before) == 1, (file, before[:100], text.count(before))
    p.write_text(text.replace(before, after, 1))
    edits.append(dict(file=file, before=before, after=after, reason=reason))

f = 'chapter/ch01-introduction.tex'
change(f, 'across sources \\cite{}.', 'across sources~\\cite{bg-reca,bg-mmqa}.', 'C1: missing table context and evidence distributed across modalities.')
change(f, 'Hence, selecting relevant evidences and preserving their connections are crucial real-world problems \\cite{}.', 'Hence, selecting relevant evidence and preserving the relationships among facts are crucial real-world problems~\\cite{bg-hipporag}.', 'C2: relational retrieval; evidence is uncountable.')
change(f, 'current task \\cite{}.', 'current task~\\cite{bg-reca,bg-dpr}.', 'C3: task-relevant external context in annotation and QA.')
change(f, 'several facts may need to be jointed before they can answer the query.', 'several facts may need to be combined to answer the query.', 'Correct the verb while retaining the author\'s direct phrasing.')
change(f, 'make them available for search when selecting information for a language model.', 'make them searchable when selecting information for a language model.', 'Keep the author\'s emphasis on search in a shorter construction.')
change(f, 'These types may also differ from the annotation needs.', 'These graph types may also differ from the labels required by the annotation task.', 'Make the type-to-label mismatch explicit.')
change(f, 'new labels arrive with few examples, the system needs another way to obtain and use knowledge \\cite{}.', 'new labels arrive with few examples~\\cite{gorag-xia-etal-2021-incremental}, the system needs another way to obtain and use knowledge.', 'C4: place the incremental few-shot citation on the condition it supports.')
change(f, 'As a result, we propose GORAG for dynamic few-shot text classification task. GORAG constructs weighted keyword-label relations,', 'To support this setting, we propose GORAG for dynamic few-shot text classification. GORAG constructs weighted keyword--label relations,', 'Connect the task to the method, correct the article construction, and retain relation typography.')
change(f, 'The model needs facts that jointly support an answer, and a summary can require several complementary information items \\cite{}.', 'The model needs facts that jointly support an answer~\\cite{bg-hipporag}, and a summary can require several complementary facts~\\cite{bg-graphrag}.', 'C5: separate multi-hop QA from summarization coverage.')
change(f, 'On the other hand, multimodal question answering introduces a further requirement for task-related graph construction and retrieval \\cite{}. Relevant facts can be distributed across text and images, and the visual details needed from an image depend on the question \\cite{}. \nIn this scenario, different queries may need different visual evidences given the same image, and a relation stated directly in that query may also correspond to several relations in the evidence. \n', 'On the other hand, multimodal question answering requires joint reasoning over evidence from text and images~\\cite{bg-mmqa}. Different questions about the same image can require different visual details~\\cite{bg-stacked-attention}. A relation stated directly in a question may also correspond to several relations in the evidence.\n', 'C6/C7: cross-modal reasoning and question-guided visual selection; combine repeated visual-evidence sentences.')
change(f, "reuse of the LLM's KV cache", 'reuse and selective recomputation of the LLM\'s key-value (KV) cache', 'Define KV at first use in the chapter and retain both operations.')
change(f, 'contributions corresponding to the research questions.', 'contributions that address the research questions.', 'Use the author\'s problem-to-solution phrasing.')

f = 'chapter/ch02-background.tex'
change(f, "The distinction makes the external collection an explicit part of the prediction system. Changing its contents or its selection rule changes the context received by the generator even when the generator's parameters stay fixed.", "The external collection supplies evidence at prediction time. Updating the collection or its retrieval rule changes the generator's context even when its parameters stay fixed.", 'Replace abstract metadiscourse with the operation and its consequence.')
change(f, 'The resulting context is then a selected relational object with a serialization for the language model.', 'The selected nodes and relationships are then serialized as context for the language model.', 'Name the concrete retrieval output.')
change(f, 'A graph result must be converted into model input.', 'The retrieved graph must be converted into model input.', 'Use the defined evidence object.')
change(f, 'Wider graph reception and qualifier integration consequently concern complementary parts of the architecture.', 'Graph reception supplies wider context, while qualifier integration preserves information within each fact.', 'Explain how the two components complement each other.')

f = 'chapter/ch03-kglink.tex'
change(f, 'Retrieving a factually relevant graph type is consequently insufficient to determine the required output label.', 'A factually relevant graph type alone may therefore leave the required output label ambiguous.', 'Connect the type example to its annotation difficulty.')
change(f, 'We address missing context and type granularity through separate steps.', 'To address these two difficulties, KGLink combines graph processing with supervised representation learning.', 'Extend the author\'s explicit problem-to-method transition.')
change(f, 'BM25 to score the relation between the mention\'s words and indexed entity labels', 'BM25 to score lexical matches between the mention\'s words and indexed entity labels', 'Distinguish lexical retrieval from a graph relation.')
change(f, 'This arrangement supplies supervision about the label\'s meaning in context.', 'The paired inputs teach the encoder how the label relates to the table context.', 'Replace an abstract subject with the training inputs and their role.')
change(f, "These measurements locate KGLink's annotation results within the costs of the evaluated implementations. Its use of external retrieval and a second training objective carries computation beyond the table encoder alone.", "These results show the cost of KGLink's graph-augmented annotation. External retrieval and the auxiliary training objective add computation beyond the table encoder alone.", 'State what the runtime comparison explains.')
change(f, 'compares annotation accuracy without retrieved KG evidence. It obtains', 'compares annotation accuracy without retrieved KG evidence. KGLink obtains', 'Correct an unclear pronoun referring to a table rather than KGLink.')

f = 'chapter/ch04-gorag.tex'
change(f, 'We represent keywords and labels in a weighted graph.', 'To select labels jointly from the query keywords, we represent keywords and labels in a weighted graph.', 'Link the candidate-selection difficulty to the graph design.')
change(f, 'The representation places label alternatives inside the same structure that stores their lexical associations.', 'Label nodes make candidate classes directly accessible through their keyword associations.', 'Explain the operational purpose of label nodes.')
change(f, 'The complement converts a larger correlation score into a smaller contribution to connection cost.', 'Subtracting the correlation score from one gives stronger keyword associations lower connection costs.', 'Explain the weighting operation directly without changing the equation.')
change(f, 'The partition prevents the retrieval operation from treating an unindexed term as if it already had a known label neighborhood.', 'This partition restricts current retrieval to keywords with indexed label associations.', 'State the information available for retrieval directly.')
change(f, 'The offline ablation shows the contribution of expanding the index beyond the support sample.', 'Disabling online insertion lowers accuracy, showing the contribution of expanding the index beyond the support sample.', 'State the observed result before its interpretation.')

f = 'chapter/ch05-agrag.tex'
change(f, 'We propose AGRAG to select connected evidence using query relevance and graph influence.', 'To address these evidence requirements, we propose AGRAG to select connected facts using query relevance and graph influence.', 'Extend the author\'s task-requirement-to-method transition.')
change(f, 'The original example in Figure~\\ref{fig:agrag:example} illustrates this distinction. The example motivates expansion beyond an initial terminal-connecting structure.', 'Figure~\\ref{fig:agrag:example} illustrates why evidence retrieval may need to expand beyond an initial terminal-connecting structure.', 'Combine repeated references to the same motivating example.')
change(f, 'A passage contributes contextual evidence to graph retrieval without being reduced to a single isolated fact.', 'Passage nodes retain context shared by several extracted facts.', 'Give the passage node a concrete role.')
change(f, 'The running example in Figure~\\ref{fig:agrag:example} makes the difference between connecting anchors and collecting an answer visible.', 'The running example in Figure~\\ref{fig:agrag:example} shows why connecting the query anchors may leave required answer facts outside the retrieved structure.', 'State the unresolved evidence requirement explicitly.')
change(f, 'This comparison shows lower index preparation time alongside a higher reported query total for AGRAG.', 'AGRAG reduces indexing time in both corpora but takes longer to process their queries.', 'State the measured quality-cost comparison directly.')

f = 'chapter/ch06-mgrag.tex'
change(f, 'We construct query-related graphs and match their paths to the relationships requested by the question.', 'To meet these requirements, we construct query-related graphs and match their paths to the relationships requested by the question.', 'Link multimodal requirements to construction and matching.')
change(f, 'The second decision concerns what constitutes a match.', 'The second challenge is matching the relations requested by the query to those expressed by the evidence.', 'Make the matching problem parallel to the extraction challenge.')
change(f, 'The third decision concerns the cost of processing retrieved evidence.', 'The third challenge is reducing repeated computation when processing retrieved evidence.', 'Identify the computation problem before introducing cache reuse.')
change(f, 'This detail matters because the ranking representation expresses the image through language, whereas the later extraction and answering stages can use its visual content.', 'Ranking therefore depends on the caption, while extraction and answering can use the original image.', 'Remove editorial metadiscourse and name the available evidence.')
change(f, 'These comparisons expose answer-quality and time changes under several compositions of retrieval and caching.', 'These comparisons measure how combining retrieval and caching changes answer quality and processing time.', 'Replace abstract nominal phrasing with the measured behavior.')
change(f, 'Actual module costs provide the complementary evidence about where runtime is spent.', 'Module-level runtime measurements show where the computation is spent.', 'State the purpose of the runtime breakdown directly.')

f = 'chapter/ch07-discussion.tex'
change(f, "This separates obtaining external information from learning the output vocabulary, but both the available graph and the annotated training set determine the method's application.", "The method therefore depends on both the coverage of the external graph and the labeled data available for learning the annotation vocabulary.", 'Connect the limitations to the transition toward task-driven retrieval.')
change(f, 'MGRAG investigates another requirement of evidence retrieval.', 'For multimodal retrieval, MGRAG addresses the additional need to select and match evidence for each question.', 'Keep the multimodal branch explicit in the cross-chapter synthesis.')
change(f, 'The location of a structural decision affects how an error can propagate.', 'Errors propagate differently depending on where structure enters the pipeline.', 'Introduce the following concrete error examples directly.')

f = 'chapter/ch08-conclusion.tex'
change(f, 'We then studied the evidence requirements of question answering and generation. AGRAG constructs', 'We then extended task-driven retrieval to the connected facts needed for question answering and generation. AGRAG constructs', 'State how AGRAG extends the classification research direction.')
change(f, 'For multimodal question answering, we proposed MGRAG to construct query-specific graphs and match requested relations to semantic paths.', 'To support answers that combine text and image evidence, we proposed MGRAG to construct query-specific graphs and match requested relations to semantic paths.', 'State the multimodal requirement before the proposed method.')

f = 'chapter/front-abstract.tex'
change(f, 'We further study evidence requirements beyond classification. AGRAG selects', 'We then extend retrieval beyond candidate labels to facts that support an answer. AGRAG selects', 'Make the transition beyond classification concrete in the abstract.')

(out / 'edits.json').write_text(json.dumps(edits, indent=2, ensure_ascii=False))
print(f'Applied {len(edits)} exact replacements in {len({e["file"] for e in edits})} files.')
