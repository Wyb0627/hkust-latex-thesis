"""Apply reviewed literature additions with exact before/after provenance."""
from pathlib import Path
import json
out=Path(__file__).resolve().parent
edits=[]
def replace(file,before,after,reason):
    p=Path(file);s=p.read_text();assert s.count(before)==1,(file,before[:80])
    p.write_text(s.replace(before,after,1))
    edits.append(dict(file=file,before=before,after=after,reason=reason))
def after(file,anchor,addition,reason):replace(file,anchor,anchor+'\n\n'+addition,reason)

f='chapter/ch01-introduction.tex'
replace(f, 'Language models utilize information in tables, text, and images to make predictions and respond to queries. ',
    'Language models utilize information in tables, text, and images to make predictions and respond to queries. Table pre-training and visual instruction tuning have extended their applications beyond plain text~\\cite{lit-deng2022turl,lit-liu2023llava}. ',
    'Ground the opening in representative table and multimodal pre-training work.')
replace(f, 'For question answering, several facts may need to be combined to answer the query.',
    'For question answering, several facts may need to be combined to answer the query~\\cite{lit-trivedi2022interleaving}.',
    'Support multi-step evidence requirements with IRCoT.')
replace(f, 'make them searchable when selecting information for a language model.',
    'make them searchable when selecting information for a language model~\\cite{lit-zhang2024knowgpt}.',
    'Ground graph-supported knowledge selection in KnowGPT.')
replace(f, "Hence, we explore using a large language model's semantic capabilities with a graph constructed from task data.",
    "Few-shot prompting shows that a language model can adapt its predictions through input examples~\\cite{lit-brown2020language}, while meta-learning studies adaptation from limited supervision~\\cite{lit-finn2017model}. These approaches motivate us to explore using a large language model's semantic capabilities with a graph constructed from task data.",
    'Explain the learning-to-retrieval transition through two established adaptation approaches without equating their mechanisms.')
replace(f, 'Different questions about the same image can require different visual details~\\cite{bg-stacked-attention}.',
    'Different questions about the same image can require different visual details~\\cite{bg-stacked-attention,lit-antol2015vqa}. Instruction-aware visual extraction further makes the selected features depend on the requested task~\\cite{lit-dai2023instructblip}.',
    'Support question-dependent visual evidence and distinguish instruction-aware features from graph extraction.')
replace(f, "The selected structure also guides the reuse and selective recomputation of the LLM's key-value (KV) cache when the evidence is processed for answering.",
    "The selected structure also guides the reuse and selective recomputation of the LLM's key-value (KV) cache when the evidence is processed for answering. Attention-based cache retention provides related approaches to limiting context-processing resources~\\cite{lit-zhang2023h2o,lit-liu2023scissorhands}.",
    'Place graph-aware recomputation in relation to cache-retention literature without presenting them as the same operation.')

f='chapter/ch02-background.tex'
after(f,
    'A model accessing this graph can retrieve relations associated with a mentioned entity, including information absent from its immediate input.',
    '''Knowledge-graph embedding models learn vector representations for predicting missing relations. TransE represents a relation as a translation between entity embeddings, while TransH applies translation after projection onto a relation-specific hyperplane~\\cite{lit-bordes2013translating,lit-wang2014knowledge}. These models make different assumptions about how one relation can connect multiple entities.

Other scoring functions capture different relational patterns. ComplEx uses complex-valued factorization to model symmetric and antisymmetric relations, and SimplE uses paired head and tail representations with inverse relations~\\cite{lit-trouillon2016complex,lit-kazemi2018simple}. ConvE introduces convolutional interactions for link prediction~\\cite{lit-dettmers2018convolutional}. Their embedding scores predict graph facts; later retrieval stages must still decide which facts are useful for a language-model task.''',
    'Explain relational representation choices underlying the hyper-relational study and distinguish link prediction from retrieval.')
after(f,
    'The edge type determines how a connection should be interpreted, whether it represents a fact, lexical similarity, or a keyword--label association.',
    '''Graph encoders can also learn how to aggregate neighborhood information. GraphSAGE samples and aggregates node features to generate representations for previously unseen nodes~\\cite{lit-hamilton2017inductive}. This inductive computation differs from storing a separately trained embedding for every indexed entity. The choice affects how an encoder can receive information when a graph grows.''',
    'Introduce the neighborhood-learning mechanism relevant to graph reception and changing graphs.')
after(f,
    'Generative language models produce an answer sequence conditioned on the query and supplied context.',
    '''Pre-training objectives shape how these representations are learned. XLNet uses a permutation-based autoregressive objective to capture context beyond a fixed left-to-right factorization~\\cite{lit-yang2019xlnet}. T5 formulates diverse language tasks through a shared text-to-text interface and studies pre-training objectives and transfer learning~\\cite{lit-raffel2020exploring}. These objectives determine the model's initial capabilities, while the downstream task determines the additional supervision and evidence it receives.''',
    'Expand the language-model background with established objectives and task interfaces.')
after(f,
    'Surrounding columns and external facts can help determine the intended type.',
    '''WebTables demonstrated that relational tables extracted from the Web form a large collection of small databases and that corpus-wide schema statistics support table search and schema applications~\\cite{lit-cafarella2008webtables}. This setting motivates methods that recover semantics from cell values, surrounding columns, and other tables when a target table has limited metadata.''',
    'Ground the table-understanding problem in its database setting.')
after(f,
    'Self-attention lets a column representation depend on values in other columns, subject to the input-length limit.',
    '''Table pre-training can encode additional structural information. TURL learns contextual representations of relational tables through self-supervised pre-training~\\cite{lit-deng2022turl}. TAPAS augments a language model with table-aware inputs and learns to answer questions through cell selection and aggregation~\\cite{lit-herzig2020tapas}. TableFormer introduces learned attention biases for table structure and table--text alignment while addressing sensitivity to row and column order~\\cite{lit-yang2022tableformer}. These designs show how serialization, structural biases, and pre-training tasks affect the table information available to a predictor.''',
    'Compare three distinct table-pre-training mechanisms rather than append citations to Doduo.')
after(f,
    'Their retrieval units and preparation costs differ accordingly.',
    '''ColNet combines knowledge-base-derived supervision with convolutional representations of cell and column semantics~\\cite{lit-chen2019colnet}. TCN models contextual information within and across Web tables through a table convolutional network~\\cite{lit-wang2021tcn}. Together with RECA, these approaches illustrate different uses of external context, from knowledge-base concepts to relationships among tables. KGLink instead selects graph-derived descriptions for an encoder that learns the target annotation vocabulary.''',
    'Relate knowledge-base and cross-table context to KGLink without adding unsupported performance comparisons.')
after(f,
    'Their coverage determines which ambiguities they can resolve.',
    '''\\section{Few-shot Adaptation and Evolving Label Sets}
\\label{sec:background:fewshot}

Few-shot learning studies prediction from limited labeled examples, often using experience from related tasks to support adaptation~\\cite{lit-wang2020generalizing}. The support set provides examples of the current classes, while the query set tests the resulting decisions. A method must specify which information is learned beforehand and which information becomes available for a new task.

Metric-based methods organize support information in a learned representation space. Matching Networks use an attention-based prediction over support examples, while Prototypical Networks compare query representations with class prototypes~\\cite{lit-vinyals2016matching,lit-snell2017prototypical}. Relation Networks learn a comparison function between examples~\\cite{lit-sung2018learning}. Model-agnostic meta-learning instead learns an initialization that supports adaptation through a small number of gradient updates~\\cite{lit-finn2017model}. The learned metric, comparison function, and initialization provide different mechanisms for using a small support set.

An expanding label set adds the need to retain earlier categories. Dynamic Few-Shot Visual Learning studies recognizing novel categories while preserving base categories, and Attention Attractor Networks regularize the addition of new classifier weights in incremental few-shot learning~\\cite{lit-gidaris2018dynamic,lit-ren2019incremental}. These visual-learning settings establish related adaptation problems; incremental few-shot text classification introduces successive rounds of text labels and limited examples~\\cite{gorag-xia-etal-2021-incremental}.

Large language models introduce another adaptation interface. GPT-3 demonstrates prediction from task descriptions and examples supplied in the prompt, without gradient updates for the demonstrated task~\\cite{lit-brown2020language}. GORAG uses a language model for this prediction role, but maintains keyword--label associations in an external graph. Its online updates change which label evidence is retrieved for subsequent queries.''',
    'Add the missing shared background for GORAG, distinguishing metric learning, gradient adaptation, incremental categories, and in-context prediction.')
after(f,
    "Updating the collection or its retrieval rule changes the generator's context even when its parameters stay fixed.",
    '''Retrieval can also participate in model training. REALM trains a language model with a latent knowledge retriever, RETRO conditions generation on chunks retrieved from a large text collection, and Atlas studies few-shot knowledge-intensive tasks with a pre-trained retrieval-augmented model~\\cite{lit-guu2020retrieval,lit-borgeaud2022improving,lit-izacard2023atlas}. These systems make the retrieval source part of the model's information supply, while differing in their training objectives and task adaptation.''',
    'Situate inference-time evidence selection relative to retrieval-augmented model training.')
after(f,
    'The two representations provide different signals, so hybrid retrieval can select context using both lexical overlap and embedding similarity.',
    '''Retrieval need not compress each passage into a single vector. ColBERT independently encodes query and passage tokens, then uses a late-interaction operation to score fine-grained matches~\\cite{lit-khattab2020colbert}. HyDE addresses retrieval without relevance labels by generating a hypothetical document and encoding it as a search representation~\\cite{lit-gao2023hyde}. The generated document guides retrieval; the retrieved source documents supply the evidence used downstream. These methods change the representation used to find context without requiring a graph index.''',
    'Compare token-level retrieval and hypothetical-document query representations with the existing dense/sparse discussion.')
after(f,
    'An answer improvement can arise from selecting better evidence, organizing the context, or using it more effectively.',
    '''Question-answering benchmarks expose different evidence requirements. Natural Questions contains naturally occurring search queries with long and short answer annotations on Wikipedia pages, while TriviaQA pairs trivia questions with independently gathered evidence documents~\\cite{lit-kwiatkowski2019natural,lit-joshi2017triviaqa}. These collections help distinguish locating supporting text from reading or generating an answer from it.

Complex questions can require retrieval to change as reasoning proceeds. IRCoT interleaves retrieval with generated intermediate reasoning steps, using those steps to search for further evidence~\\cite{lit-trivedi2022interleaving}. This iterative approach obtains additional context through successive retrieval decisions. Graph-based retrieval instead makes extracted relationships available within the index, where several supporting facts can be selected through connected paths or propagation.''',
    'Ground evaluation and multi-step retrieval in benchmark definitions and IRCoT, without implying those benchmarks were added to thesis experiments.')
after(f,
    'The retrieval budget therefore affects the information available to the generator even when the corpus and model remain fixed.',
    '''A larger context window does not ensure that all supplied evidence is used equally well. Lost in the Middle shows that answer performance can depend strongly on where relevant information occurs in a long input~\\cite{lit-liu2024lost}. Evidence selection and organization therefore remain relevant even when the model can accept additional passages.''',
    'Support the motivation for evidence organization with a published long-context analysis.')
after(f,
    'Its retrieval modes select specific entity information and broader relational or conceptual information.',
    '''KnowGPT studies knowledge-graph-based prompting by extracting useful knowledge and constructing context-aware prompts~\\cite{lit-zhang2024knowgpt}. It makes graph knowledge available through the prompt supplied to a language model. This connects the retrieval decision to how the selected information is presented, complementing methods that rank nodes, return source passages, or summarize graph communities.''',
    'Broaden graph-based retrieval with knowledge-selection and prompt-construction work.')
after(f,
    'AGRAG uses this combination for text, and MGRAG retains source chunks containing the original images.',
    '''\\subsection{Reasoning structures and source evidence}

Explicit structure also appears in generated reasoning. Chain-of-thought prompting supplies intermediate reasoning demonstrations, and Zero-shot-CoT uses a reasoning instruction without task-specific demonstrations~\\cite{lit-wei2022chain,lit-kojima2022large}. Plan-and-Solve prompting first develops a plan and then carries out its subtasks~\\cite{lit-wang2023plan}. These approaches organize how a model produces intermediate steps.

Tree of Thoughts searches over alternative intermediate thoughts, while Graph of Thoughts allows dependencies and combinations among generated information units~\\cite{lit-yao2024tree,lit-besta2024graph}. Their nodes represent model-generated reasoning states. In an evidence graph, nodes and edges instead describe information extracted or indexed from task data. Combining a reasoning structure with retrieved facts therefore requires tracking the source of each information item.

The NLGraph study evaluates graph problems expressed in natural language and finds that language-model performance depends on problem complexity and graph presentation~\\cite{lit-wang2023can}. This motivates specifying which structural operations are performed by graph algorithms and which decisions are left to a language model. In our retrieval pipelines, graph construction and selection define the evidence passed to the final predictor.''',
    'Compare generated reasoning structures with evidence graphs, then ground the division of graph/model operations in NLGraph.')
after(f,
    'Retrieval must therefore consider both the relevance of individual objects and the relationship connecting them to the question.',
    '''The VQA task asks for an answer to a natural-language question about an image, making visual relevance depend on the question~\\cite{lit-antol2015vqa}. MultiModalQA extends the evidence requirement to reasoning across source modalities. The distinction matters for retrieval because a visually informative image can still lack the particular detail or relationship requested by the question.

Vision--language pre-training supplies several ways to align the modalities. ViLBERT uses interacting visual and textual streams, while BLIP combines understanding and generation objectives with caption bootstrapping~\\cite{lit-lu2019vilbert,lit-li2022blip}. BLIP-2 connects frozen image and language models through a trainable querying component~\\cite{lit-li2023blip2}. These architectures determine how visual content becomes accessible to language-based prediction.

Flamingo supports few-shot prediction with interleaved visual and textual inputs~\\cite{lit-alayrac2022flamingo}. LLaVA studies visual instruction tuning, and InstructBLIP introduces instruction-aware visual feature extraction~\\cite{lit-liu2023llava,lit-dai2023instructblip}. Such models can condition their processing on a task instruction, but a retrieval pipeline must additionally identify which source objects contain the supporting evidence. MGRAG uses query-aware graph construction to organize relationships among those objects.''',
    'Explain visual questioning, multimodal pre-training, frozen-model bridges, and instruction-conditioned visual processing before MGRAG retrieval.')
after(f,
    'It is a separate decision from choosing which evidence belongs in the context.',
    '''Attention computation, cache retention, and cache recomputation address different costs. FlashAttention reduces memory traffic through an IO-aware implementation of exact attention~\\cite{lit-dao2022flashattention}. H2O retains a combination of recent and heavily attended tokens, while Scissorhands exploits persistent token importance to compress the KV cache~\\cite{lit-zhang2023h2o,lit-liu2023scissorhands}. These retention policies decide which states remain available; selective recomputation decides which available states to refresh when the context changes.''',
    'Distinguish exact-attention implementation, state retention, and recomputation rather than conflate their efficiency claims.')
after(f,
    'StarE retains the semantic roles of qualifiers and triples in message passing and introduces WD50K for hyper-relational link prediction~\\cite{bg-stare}.',
    '''Related work represents facts with more than two participating entities in several ways. NaLP models the relatedness among role--value pairs, GETD extends tensor decomposition to n-ary relational knowledge bases, and RAM learns role-aware representations~\\cite{lit-guan2019link,lit-liu2020generalizing,lit-liu2021role}. These representations expose the roles occupied by entities within a fact.

NeuInfer represents a primary triple together with auxiliary attribute--value descriptions and studies inference from complete or partial facts~\\cite{lit-guan2020neuinfer}. HAHE combines global hypergraph structure with local sequential representations of hyper-relational facts~\\cite{lit-luo2023hahe}. These designs motivate examining both information within a fact and information received from the wider graph, the two aspects studied below.''',
    'Add relevant n-ary and hyper-relational representation work while keeping their encodings distinct.')

(out/'edits.json').write_text(json.dumps(edits,indent=2,ensure_ascii=False))
print('Applied',len(edits),'reviewed literature additions/replacements in Chapters 1 and 2.')
