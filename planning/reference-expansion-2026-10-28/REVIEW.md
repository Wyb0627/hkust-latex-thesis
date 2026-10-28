# 引用扩充与写作复核记录

日期：2026-10-28（Asia/Shanghai）。主文件 `main.tex`，阅读稿 `thesis.pdf`。本轮在上一轮七处空引用补全和全文措辞修改的基础上，完成用户要求的独立论文总量超过 120 篇。

## 实际引用数量

| 口径 | 扩充前 | 扩充后 |
|---|---:|---:|
| 正文实际引用的去重条目 | 73 | **129** |
| 独立研究论文，保守计数 | 67 | **123** |
| ch01 实际引用的不同作品 | 12 | **22** |
| ch02 实际引用的不同作品 | 27 | **84** |

Biber 生成的 `main.bbl` 中实际排印 129 个条目，PDF 最后一项编号为 [129]。计数根据正文引用以及合并时的 DOI、规范化题名和 key alias 去重，不把相同作品的不同引用键重复计数。数据库共有 131 个去重条目，另有 31 个旧键别名；两条未在正文引用的记录不计入上述数量。章节之间重复引用同一论文时，全篇只计一次。

以下六条保留在正文/参考文献中，但不计入独立研究论文数：

| 引用键 | 不计入原因 |
|---|---|
| `agrag-tfidf` | Encyclopedia entry, not a research paper |
| `agrag-ragas2024` | Software repository; the separate RAGAs paper is counted |
| `agrag-fastgraphrag` | Software repository |
| `kglink-hassanzadeh_oktie_2019_3518539` | Dataset release |
| `mgrag-tech-report` | Supplementary report for the already counted MGRAG paper |
| `mgrag-nanographrag` | Software repository |

因此，目标按 **123 篇独立论文** 达成，而非仅通过软件、数据或重复报告达到条目数量。

## 文献选择与正文修改

新增 **56 篇**，其中 **36 篇**来自作者既有论文 bib，**20 篇**通过外部检索补充。检索了 KGLink、AGRAG/GORAG、MGRAG、CIKM 超关系图、GFM、KBLink、CoT survey、NIPS 及 NER 等 11 个原始文献库；候选及原始路径保存在 `local-candidates.json`，最终选择在 `shortlist.json`。

新增会议论文 50 篇，均采用 CCF A 类会议的正式全文记录（包括两篇 PVLDB 归档论文）；另有 6 篇 JMLR、TACL、ACM Computing Surveys 期刊论文。新增文献没有依赖未发表预印本，因此无需通过引用量门槛放行。已有参考文献未按本轮新增标准删除。

官方目录依据：[CCF 人工智能类](https://www.ccf.org.cn/Academic_Evaluation/AI/)、[数据库/数据挖掘/内容检索类 A 类会议](https://www.ccf.org.cn/Academic_Evaluation/DM_CS/zgjsjxhtjgjxshy/al/)、[WWW 官方目录条目](https://www.ccf.org.cn/Academic_Evaluation/Cross_Compre_Emerging/zgjsjxhtjgjxshy/al/2017-04-25/592216.shtml)、[CCF 分类说明](https://www.ccf.org.cn/Academic_Evaluation/By_category/)。按 full/regular paper 口径处理，未将 Findings 或 workshop 当作主会全文。

| 会刊 | 新增篇数 |
|---|---:|
| NeurIPS | 21 |
| ACL | 8 |
| ICML | 6 |
| AAAI | 4 |
| WWW | 4 |
| TACL | 3 |
| CVPR | 3 |
| VLDB | 2 |
| JMLR | 2 |
| CSUR | 1 |
| SIGIR | 1 |
| ICCV | 1 |

ch01 补充表格预训练、视觉指令微调、多跳检索、图知识提示、少样本适应以及注意力缓存保留的依据。ch02 增补以下脉络，并在新段落中设置引用位置：

- 知识图谱嵌入及图邻域编码，区分关系评分与任务证据选择。
- 表格预训练、表格问答和外部语义信息，连接 KGLink 的问题设置。
- 新增“Few-shot Adaptation and Evolving Label Sets”一节，说明度量学习、元学习、类别增量学习和上下文学习的差别。
- 检索参与预训练、细粒度检索、零样本检索、问答数据集、交替检索推理和长上下文证据位置。
- 区分生成的推理结构与有来源的证据图。
- 多模态预训练、视觉指令微调及知识型视觉问答。
- 区分注意力计算、KV 保留和重计算；补充 n-ary 与 hyper-relational 事实表示。

这些介绍不新增实验或声称复现了被引方法。每条新增引用的具体句子保存在 `reference-ledger.json` 的 `locations.paragraph` 中；`edits.json` 和 `manuscript.diff` 记录精确差异。

## 真实性、元数据和 Google Scholar 交叉核查

56 篇均取得官方论文集、出版平台、期刊网站或出版商提交的 Crossref 元数据；原始响应保存在 `primary-records/`，抓取状态和解析结果保存在 `primary-verification.json`。核对题名、作者、正式年份、会刊，以及可获得的卷期、页码、DOI。新增 bib 由这些正式记录重建，原始 bib 只用于候选和来源追踪。

修正了原 bib 中的若干版本差异：TURL 使用原始 PVLDB 论文而非 SIGMOD Record 转载；GPT-3 使用 NeurIPS 2020 正式论文；Tree of Thoughts 使用 NeurIPS 2023，IRCoT 使用 ACL 2023 长文，HAHE 使用 ACL 2023 长文，替代旧键所暗示的年份或预印本身份。原 key 中的年份不是最终发表年份的依据。

Google Scholar 经浏览器取得 27 个成功检索快照，其中 24 个对应最终新增论文；另有 REALM 的早期交互检索。保存的查询索引为 `scholar-crosscheck-index.json`，原始快照为 `scholar-round1.json` 至 `scholar-round5.json`。Scholar 随后触发“Please show you're not a robot”，已停止继续检索并交还浏览器，没有绕过验证。**没有声称 56 篇全部完成 Scholar 核查**；正式发表身份和最终 bib 以官方记录为准。

未采用的两个具体候选：

- LLMLingua-2：原库会议信息不准确，正式记录属于 Findings，未按 CCF A 主会全文加入。
- Improving Hyper-relational Knowledge Graph Completion：检索时仍为预印本，Scholar 显示 69 次引用，未满足用户的未发表论文门槛，因此未加入。

一次 Python HTTPS 探查遭遇本机证书链错误，记录于 `python-tls-probe.json`；改用具有正常系统信任链的 curl 获取相同官方资源，未关闭 TLS 验证。AAAI 压缩响应解析问题通过正常解压后重新抓取解决，没有将失败抓取作为核查成功。浏览器提示 EgoLite 有更新，本轮没有升级或更改用户浏览器环境。

## 新增引用逐条索引

“原库”列给出作者 bib 文件的末级路径；完整绝对路径、原键、官方记录原文件和引用整段文字均在 `reference-ledger.json` 中。

| 新键 | 论文 | 正式会刊/年份 | 原库或外部 | 正文位置 |
|---|---|---|---|---|
| `lit-deng2022turl` | [TURL: table understanding through representation learning](https://api.crossref.org/works/10.14778/3430915.3430921) | VLDB 2020 | `KGLink_ICDE_revision/KGLink.bib` | [ch01-introduction:4](../../chapter/ch01-introduction.tex#L4), [ch02-background:42](../../chapter/ch02-background.tex#L42) |
| `lit-cafarella2008webtables` | [WebTables: exploring the power of tables on the web](https://api.crossref.org/works/10.14778/1453856.1453916) | VLDB 2008 | `KGLink_ICDE_revision/KGLink.bib` | [ch02-background:36](../../chapter/ch02-background.tex#L36) |
| `lit-chen2019colnet` | [ColNet: Embedding the Semantics of Web Tables for Column Type Prediction](https://ojs.aaai.org/index.php/AAAI/article/view/3765) | AAAI 2019 | `KGLink_ICDE_revision/KGLink.bib` | [ch02-background:46](../../chapter/ch02-background.tex#L46) |
| `lit-wang2021tcn` | [TCN: Table Convolutional Network for Web Table Interpretation](https://api.crossref.org/works/10.1145/3442381.3450090) | WWW 2021 | `KGLink_ICDE_revision/KGLink.bib` | [ch02-background:46](../../chapter/ch02-background.tex#L46) |
| `lit-raffel2020exploring` | [Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer](https://jmlr.org/papers/v21/20-074.html) | JMLR 2020 | `KGLink_ICDE_revision/KGLink.bib` | [ch02-background:25](../../chapter/ch02-background.tex#L25) |
| `lit-wang2020generalizing` | [Generalizing from a Few Examples: A Survey on Few-shot Learning](https://api.crossref.org/works/10.1145/3386252) | CSUR 2020 | `WWW/GraphRAG_FSCIL.bib` | [ch02-background:55](../../chapter/ch02-background.tex#L55) |
| `lit-wei2022chain` | [Chain-of-Thought Prompting Elicits Reasoning in Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2022/hash/9d5609613524ecf4f15af0f7b31abca4-Abstract-Conference.html) | NeurIPS 2022 | `WWW/GraphRAG_FSCIL.bib` | [ch02-background:134](../../chapter/ch02-background.tex#L134) |
| `lit-brown2020language` | [Language Models are Few-Shot Learners](https://proceedings.neurips.cc/paper_files/paper/2020/hash/1457c0d6bfcb4967418bfb8ac142f64a-Abstract.html) | NeurIPS 2020 | `WWW/GraphRAG_FSCIL.bib` | [ch01-introduction:14](../../chapter/ch01-introduction.tex#L14), [ch02-background:61](../../chapter/ch02-background.tex#L61) |
| `lit-liu2024lost` | [Lost in the Middle: How Language Models Use Long Contexts](https://aclanthology.org/2024.tacl-1.9/) | TACL 2024 | `WWW/GraphRAG_FSCIL.bib` | [ch02-background:88](../../chapter/ch02-background.tex#L88) |
| `lit-finn2017model` | [Model-Agnostic Meta-Learning for Fast Adaptation of Deep Networks](https://proceedings.mlr.press/v70/finn17a.html) | ICML 2017 | `WWW/GraphRAG_FSCIL.bib` | [ch01-introduction:14](../../chapter/ch01-introduction.tex#L14), [ch02-background:57](../../chapter/ch02-background.tex#L57) |
| `lit-gidaris2018dynamic` | [Dynamic Few-Shot Visual Learning Without Forgetting](https://openaccess.thecvf.com/content_cvpr_2018/html/Gidaris_Dynamic_Few-Shot_Visual_CVPR_2018_paper.html) | CVPR 2018 | `WWW/GraphRAG_FSCIL.bib` | [ch02-background:59](../../chapter/ch02-background.tex#L59) |
| `lit-ren2019incremental` | [Incremental Few-Shot Learning with Attention Attractor Networks](https://proceedings.neurips.cc/paper_files/paper/2019/hash/e833e042f509c996b1b25324d56659fb-Abstract.html) | NeurIPS 2019 | `WWW/GraphRAG_FSCIL.bib` | [ch02-background:59](../../chapter/ch02-background.tex#L59) |
| `lit-zhang2024knowgpt` | [KnowGPT: Knowledge Graph based Prompting for Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2024/hash/0b8705a611ed1ce19cdb759031078705-Abstract-Conference.html) | NeurIPS 2024 | `WWW/GraphRAG_FSCIL.bib` | [ch01-introduction:10](../../chapter/ch01-introduction.tex#L10), [ch02-background:103](../../chapter/ch02-background.tex#L103) |
| `lit-yang2019xlnet` | [XLNet: Generalized Autoregressive Pretraining for Language Understanding](https://proceedings.neurips.cc/paper_files/paper/2019/hash/dc6a7e655d7e5840e66733e9ee67cc69-Abstract.html) | NeurIPS 2019 | `WWW/GraphRAG_FSCIL.bib` | [ch02-background:25](../../chapter/ch02-background.tex#L25) |
| `lit-borgeaud2022improving` | [Improving Language Models by Retrieving from Trillions of Tokens](https://proceedings.mlr.press/v162/borgeaud22a.html) | ICML 2022 | `pvldbstyle-master/anyrag.bib` | [ch02-background:68](../../chapter/ch02-background.tex#L68) |
| `lit-zhang2023h2o` | [H2O: Heavy-Hitter Oracle for Efficient Generative Inference of Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2023/hash/6ceefa7b15572587b78ecfcebb2827f8-Abstract-Conference.html) | NeurIPS 2023 | `pvldbstyle-master/anyrag.bib` | [ch01-introduction:18](../../chapter/ch01-introduction.tex#L18), [ch02-background:157](../../chapter/ch02-background.tex#L157) |
| `lit-liu2021role` | [Role-Aware Modeling for N-ary Relational Knowledge Bases](https://api.crossref.org/works/10.1145/3442381.3449874) | WWW 2021 | `CIKM_FormerGNN/reference.bib` | [ch02-background:178](../../chapter/ch02-background.tex#L178) |
| `lit-guan2019link` | [Link Prediction on N-ary Relational Data](https://api.crossref.org/works/10.1145/3308558.3313414) | WWW 2019 | `CIKM_FormerGNN/reference.bib` | [ch02-background:178](../../chapter/ch02-background.tex#L178) |
| `lit-liu2020generalizing` | [Generalizing Tensor Decomposition for N-ary Relational Knowledge Bases](https://api.crossref.org/works/10.1145/3366423.3380188) | WWW 2020 | `CIKM_FormerGNN/reference.bib` | [ch02-background:178](../../chapter/ch02-background.tex#L178) |
| `lit-kazemi2018simple` | [SimplE Embedding for Link Prediction in Knowledge Graphs](https://proceedings.neurips.cc/paper_files/paper/2018/hash/b2ab001909a8a6f04b51920306046ce5-Abstract.html) | NeurIPS 2018 | `CIKM_FormerGNN/reference.bib` | [ch02-background:15](../../chapter/ch02-background.tex#L15) |
| `lit-guan2020neuinfer` | [NeuInfer: Knowledge Inference on N-ary Facts](https://aclanthology.org/2020.acl-main.546/) | ACL 2020 | `CIKM_FormerGNN/reference.bib` | [ch02-background:180](../../chapter/ch02-background.tex#L180) |
| `lit-wang2014knowledge` | [Knowledge Graph Embedding by Translating on Hyperplanes](https://ojs.aaai.org/index.php/AAAI/article/view/8870) | AAAI 2014 | `CIKM_FormerGNN/reference.bib` | [ch02-background:13](../../chapter/ch02-background.tex#L13) |
| `lit-bordes2013translating` | [Translating Embeddings for Modeling Multi-relational Data](https://proceedings.neurips.cc/paper_files/paper/2013/hash/1cecc7a77928ca8133fa24680a88d2f9-Abstract.html) | NeurIPS 2013 | `CIKM_FormerGNN/reference.bib` | [ch02-background:13](../../chapter/ch02-background.tex#L13) |
| `lit-dettmers2018convolutional` | [Convolutional 2D Knowledge Graph Embeddings](https://ojs.aaai.org/index.php/AAAI/article/view/11573) | AAAI 2018 | `CIKM_FormerGNN/reference.bib` | [ch02-background:15](../../chapter/ch02-background.tex#L15) |
| `lit-luo2023hahe` | [HAHE: Hierarchical Attention for Hyper-Relational Knowledge Graphs in Global and Local Level](https://aclanthology.org/2023.acl-long.450/) | ACL 2023 | `CIKM_FormerGNN/reference.bib` | [ch02-background:180](../../chapter/ch02-background.tex#L180) |
| `lit-trouillon2016complex` | [Complex Embeddings for Simple Link Prediction](https://proceedings.mlr.press/v48/trouillon16.html) | ICML 2016 | `CIKM_FormerGNN/reference.bib` | [ch02-background:15](../../chapter/ch02-background.tex#L15) |
| `lit-hamilton2017inductive` | [Inductive Representation Learning on Large Graphs](https://proceedings.neurips.cc/paper_files/paper/2017/hash/5dd9db5e033da9c6fb5ba83c7a7ebea9-Abstract.html) | NeurIPS 2017 | `GFM4Graph/GFM.bib` | [ch02-background:21](../../chapter/ch02-background.tex#L21) |
| `lit-wang2023can` | [Can Language Models Solve Graph Problems in Natural Language?](https://proceedings.neurips.cc/paper_files/paper/2023/hash/622afc4edf2824a1b6aaf5afe153fa93-Abstract-Conference.html) | NeurIPS 2023 | `GFM4Graph/GFM.bib` | [ch02-background:138](../../chapter/ch02-background.tex#L138) |
| `lit-kojima2022large` | [Large Language Models are Zero-Shot Reasoners](https://proceedings.neurips.cc/paper_files/paper/2022/hash/8bb0d291acd4acf06ef112099c16f326-Abstract-Conference.html) | NeurIPS 2022 | `CoT Survey/sample-base.bib` | [ch02-background:134](../../chapter/ch02-background.tex#L134) |
| `lit-wang2023plan` | [Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](https://aclanthology.org/2023.acl-long.147/) | ACL 2023 | `CoT Survey/sample-base.bib` | [ch02-background:134](../../chapter/ch02-background.tex#L134) |
| `lit-yao2024tree` | [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://proceedings.neurips.cc/paper_files/paper/2023/hash/271db9922b8d1f4dd7aaef84ed5ac703-Abstract-Conference.html) | NeurIPS 2023 | `CoT Survey/sample-base.bib` | [ch02-background:136](../../chapter/ch02-background.tex#L136) |
| `lit-besta2024graph` | [Graph of Thoughts: Solving Elaborate Problems with Large Language Models](https://ojs.aaai.org/index.php/AAAI/article/view/29720) | AAAI 2024 | `CoT Survey/sample-base.bib` | [ch02-background:136](../../chapter/ch02-background.tex#L136) |
| `lit-guu2020retrieval` | [Retrieval Augmented Language Model Pre-Training](https://proceedings.mlr.press/v119/guu20a.html) | ICML 2020 | `LLM_NER/entity.bib` | [ch02-background:68](../../chapter/ch02-background.tex#L68) |
| `lit-izacard2023atlas` | [Atlas: Few-shot Learning with Retrieval Augmented Language Models](https://jmlr.org/papers/v24/23-0037.html) | JMLR 2023 | `LLM_NER/entity.bib` | [ch02-background:68](../../chapter/ch02-background.tex#L68) |
| `lit-trivedi2022interleaving` | [Interleaving Retrieval with Chain-of-Thought Reasoning for Knowledge-Intensive Multi-Step Questions](https://aclanthology.org/2023.acl-long.557/) | ACL 2023 | `LLM_NER/entity.bib` | [ch01-introduction:10](../../chapter/ch01-introduction.tex#L10), [ch02-background:82](../../chapter/ch02-background.tex#L82) |
| `lit-liu2023llava` | [Visual Instruction Tuning](https://proceedings.neurips.cc/paper_files/paper/2023/hash/6dcf277ea32ce3288914faf369fe6de0-Abstract-Conference.html) | NeurIPS 2023 | `LLM_NER/entity.bib` | [ch01-introduction:4](../../chapter/ch01-introduction.tex#L4), [ch02-background:149](../../chapter/ch02-background.tex#L149) |
| `lit-snell2017prototypical` | [Prototypical Networks for Few-shot Learning](https://proceedings.neurips.cc/paper_files/paper/2017/hash/cb8da6767461f2812ae4290eac7cbc42-Abstract.html) | NeurIPS 2017 | `外部检索` | [ch02-background:57](../../chapter/ch02-background.tex#L57) |
| `lit-vinyals2016matching` | [Matching Networks for One Shot Learning](https://proceedings.neurips.cc/paper_files/paper/2016/hash/90e1357833654983612fb05e3ec9148c-Abstract.html) | NeurIPS 2016 | `外部检索` | [ch02-background:57](../../chapter/ch02-background.tex#L57) |
| `lit-sung2018learning` | [Learning to Compare: Relation Network for Few-Shot Learning](https://openaccess.thecvf.com/content_cvpr_2018/html/Sung_Learning_to_Compare_CVPR_2018_paper.html) | CVPR 2018 | `外部检索` | [ch02-background:57](../../chapter/ch02-background.tex#L57) |
| `lit-khattab2020colbert` | [ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT](https://api.crossref.org/works/10.1145/3397271.3401075) | SIGIR 2020 | `外部检索` | [ch02-background:74](../../chapter/ch02-background.tex#L74) |
| `lit-gao2023hyde` | [Precise Zero-Shot Dense Retrieval without Relevance Labels](https://aclanthology.org/2023.acl-long.99/) | ACL 2023 | `外部检索` | [ch02-background:74](../../chapter/ch02-background.tex#L74) |
| `lit-dao2022flashattention` | [FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness](https://proceedings.neurips.cc/paper_files/paper/2022/hash/67d57c32e20fd0a7a302cb81d36e40d5-Abstract-Conference.html) | NeurIPS 2022 | `外部检索` | [ch02-background:157](../../chapter/ch02-background.tex#L157) |
| `lit-liu2023scissorhands` | [Scissorhands: Exploiting the Persistence of Importance Hypothesis for LLM KV Cache Compression at Test Time](https://proceedings.neurips.cc/paper_files/paper/2023/hash/a452a7c6c463e4ae8fbdc614c6e983e6-Abstract-Conference.html) | NeurIPS 2023 | `外部检索` | [ch01-introduction:18](../../chapter/ch01-introduction.tex#L18), [ch02-background:157](../../chapter/ch02-background.tex#L157) |
| `lit-antol2015vqa` | [VQA: Visual Question Answering](https://openaccess.thecvf.com/content_iccv_2015/html/Antol_VQA_Visual_Question_ICCV_2015_paper.html) | ICCV 2015 | `外部检索` | [ch01-introduction:18](../../chapter/ch01-introduction.tex#L18), [ch02-background:145](../../chapter/ch02-background.tex#L145) |
| `lit-li2022blip` | [BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation](https://proceedings.mlr.press/v162/li22n.html) | ICML 2022 | `外部检索` | [ch02-background:147](../../chapter/ch02-background.tex#L147) |
| `lit-li2023blip2` | [BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models](https://proceedings.mlr.press/v202/li23q.html) | ICML 2023 | `外部检索` | [ch02-background:147](../../chapter/ch02-background.tex#L147) |
| `lit-alayrac2022flamingo` | [Flamingo: a Visual Language Model for Few-Shot Learning](https://proceedings.neurips.cc/paper_files/paper/2022/hash/960a172bc7fbf0177ccccbb411a7d800-Abstract-Conference.html) | NeurIPS 2022 | `外部检索` | [ch02-background:149](../../chapter/ch02-background.tex#L149) |
| `lit-lu2019vilbert` | [ViLBERT: Pretraining Task-Agnostic Visiolinguistic Representations for Vision-and-Language Tasks](https://proceedings.neurips.cc/paper_files/paper/2019/hash/c74d97b01eae257e44aa9d5bade97baf-Abstract.html) | NeurIPS 2019 | `外部检索` | [ch02-background:147](../../chapter/ch02-background.tex#L147) |
| `lit-dai2023instructblip` | [InstructBLIP: Towards General-purpose Vision-Language Models with Instruction Tuning](https://proceedings.neurips.cc/paper_files/paper/2023/hash/9a6a435e75419a836fe47ab6793623e6-Abstract-Conference.html) | NeurIPS 2023 | `外部检索` | [ch01-introduction:18](../../chapter/ch01-introduction.tex#L18), [ch02-background:149](../../chapter/ch02-background.tex#L149) |
| `lit-kwiatkowski2019natural` | [Natural Questions: A Benchmark for Question Answering Research](https://aclanthology.org/Q19-1026/) | TACL 2019 | `外部检索` | [ch02-background:80](../../chapter/ch02-background.tex#L80) |
| `lit-joshi2017triviaqa` | [TriviaQA: A Large Scale Distantly Supervised Challenge Dataset for Reading Comprehension](https://aclanthology.org/P17-1147/) | ACL 2017 | `外部检索` | [ch02-background:80](../../chapter/ch02-background.tex#L80) |
| `lit-herzig2020tapas` | [TaPas: Weakly Supervised Table Parsing via Pre-training](https://aclanthology.org/2020.acl-main.398/) | ACL 2020 | `外部检索` | [ch02-background:42](../../chapter/ch02-background.tex#L42) |
| `lit-yang2022tableformer` | [TableFormer: Robust Transformer Modeling for Table-Text Encoding](https://aclanthology.org/2022.acl-long.40/) | ACL 2022 | `外部检索` | [ch02-background:42](../../chapter/ch02-background.tex#L42) |
| `lit-trivedi2022musique` | [MuSiQue: Multihop Questions via Single-hop Question Composition](https://aclanthology.org/2022.tacl-1.31/) | TACL 2022 | `外部检索` | [ch02-background:80](../../chapter/ch02-background.tex#L80) |
| `lit-marino2019okvqa` | [OK-VQA: A Visual Question Answering Benchmark Requiring External Knowledge](https://openaccess.thecvf.com/content_CVPR_2019/html/Marino_OK-VQA_A_Visual_Question_Answering_Benchmark_Requiring_External_Knowledge_CVPR_2019_paper.html) | CVPR 2019 | `外部检索` | [ch02-background:145](../../chapter/ch02-background.tex#L145) |
| `lit-ouyang2022training` | [Training language models to follow instructions with human feedback](https://proceedings.neurips.cc/paper_files/paper/2022/hash/b1efde53be364a73914f58805a001731-Abstract-Conference.html) | NeurIPS 2022 | `外部检索` | [ch02-background:27](../../chapter/ch02-background.tex#L27) |

## 写作规范复核

按作者最新规范复查新增段落，并扫描摘要及八章。结合 `academic-defensive-writing-auditor` 检查 reviewer-facing 辩解、重复非主张、空泛总结和宣传措辞。未检出常见“we do not claim / to ensure fairness / it should be noted / taken together”等表达；叙述文件中未检出句中 em dash 或 LaTeX `---`。冒号限于研究问题标题、原论文题名及不排印的注释，没有新增句中冒号。已有必要条件涉及索引状态、标签信息、图覆盖、指标语义及未报告的重计算预算，保留其科学作用。详见 `WRITING_CHECK.md`。

上一轮全文 44 处措辞修改和七处空引用的详细记录继续保存在 `../citations-wording-2026-10-28/REVIEW.md`。本轮仅扩充 ch01/ch02；摘要与 ch03–ch08 相对本轮开始时逐字节一致。原有非空引用、标签、数学、算法、图表及表格数据均保留，只新增一个少样本学习节标签。

## 编译与 PDF 检查

通过 `latex-paper-en` 技能的 `compile.py` 清理后以 XeLaTeX、latexmk、Biber 重建，禁用 shell escape。最终日志 `compile-final.log`。无未定义引用、缺字、重复标签/目标、overfull box 或 LaTeX 错误；Biber 无警告或错误。

`main.pdf` 与 `thesis.pdf` 完全一致，SHA-256：`6e2a743fe4d42b94340c4958dc000e39840978c057727eb86f7c91bfc980dbb5`。

PDF 共 **125 页**，包含 14 页前置、102 页正文、9 页参考文献。95 项字体均嵌入，全部页面有文本、无旋转。125 页全部渲染并检查七张联系表，另放大检查物理页 15、26、31、117、125。没有观察到新增截断、重叠或引用排版错误。四处近似页边距标记来自原有嵌入图片的坐标标签，现位于印刷页 36、50、51、94，与前次四处来源相同且没有裁切。

正文叙述 22,182 英文词，含标题/图表题注 24,124 词；摘要仍为 213 词。页码和逐章计数在 `../CHAPTER_COUNTS.md`。自动检查汇总见 `source-checks.json`、`final-validation.json` 和 `pdf-qa/pdf-preflight.json`。
