# PhD Thesis Writing Plan

**Structural Augmented Reasoning for Language Models**

作者 Yubo Wang。计划核查日期为 2026 年 10 月 23 日，已补充第二轮 HKUST CSE PhD 模板、完整论文与答辩资源检索。本计划面向后续撰写 agent，以中文说明写作任务，thesis 正文使用英文。本次交付是写作与证据组织计划，没有改写现有 thesis 正文或更换模板。

## 1. 已确认的写作决策

以下决定来自作者本次会话，后续 agent 不需要重复询问。

1. 保留 proposal 原题目 **Structural Augmented Reasoning for Language Models**，包括其现有英文措辞。未经作者允许，不改成其他题目。
2. 覆盖五篇已接收的一作论文。四篇核心工作为 KGLink、GORAG、AGRAG、MGRAG。CIKM 2025 的超关系知识图谱研究保留独立且可识别的介绍，但无需作为第五个核心研究章节。
3. MGRAG 必须进入主线。重点是面向多模态证据的查询感知图构建、路径语义子图匹配，以及图结构对上下文计算的作用。
4. CMI-Mem 和 ClinicalAgents 不构成主线，不写入核心贡献列表，不设专章。若收尾讨论确有需要，可合计用一小段说明后续研究联系；也可不提。CMI-Mem 在个人主页上仍标为 In Submission，ClinicalAgents 为非一作工作。
5. 可以选择各论文目录中的最新研究稿。正式出版 PDF 是数据、结果、方法版本与结论的最终校核依据，源文件用于复用公式、表格和原图。修改时间不能替代出版核对。
6. 论文中的研究图片沿用原论文原图，表格忠实于原论文数据。不得生成替代实验图、猜测缺失数字、补造实验或把计划中的研究写成已完成成果。
7. 遇到影响方法、数字、理论结论、作者贡献或范围的歧义，向作者确认。可以继续撰写不受影响的部分，但不能自行决定争议内容。

## 2. 输入材料与证据优先级

### 2.1 本机路径

| 用途 | 路径 |
|---|---|
| Thesis 项目根目录 | `/Users/ybwang/Library/CloudStorage/OneDrive-HKUSTConnect/paper/thesis/hkust-latex-thesis` |
| 博士期间论文源文件总目录 | `/Users/ybwang/Library/CloudStorage/OneDrive-HKUSTConnect/paper` |
| Proposal | `proposal/Structural Augmented Reasoning for Language Models Yubo Thesis Proposal.pdf`，相对 thesis 项目根目录 |
| 现有主文件与类文件 | 项目根目录下的 `main.tex`、`ustthesis.cls`、`ustthesis_Department2ProgramOffice.cls` |
| 现有示例章节 | 项目根目录下的 `chapter/` |
| 当前示例 PDF | 项目根目录下的 `thesis.pdf` |
| 文风审计 skill | `/Users/ybwang/.codex/skills/academic-defensive-writing-auditor/SKILL.md` |

已生成的配套文件均位于本项目 `planning/`。

- [SOURCE_MAP.md](planning/SOURCE_MAP.md) 给出每篇论文的绝对入口路径、实际输入文件、图片位置和表格标签与行号。
- [asset_inventory.tsv](planning/asset_inventory.tsv) 包含 40 个图片引用与 37 个表格位置。图片带 SHA-256，方便复制后校验。这里统计的是源稿引用，不代表最终 thesis 应采用的数量。
- [source_roots.json](planning/source_roots.json) 是机器可读的五篇论文入口。
- [HKUST_PHD_REFERENCE_REVIEW.md](planning/HKUST_PHD_REFERENCE_REVIEW.md) 区分官方规范、社区模板、真实 CSE PhD 论文与答辩 slides，记录核查深度及选用建议。
- [references/README.md](planning/references/README.md) 索引本次保留的官方 PhD sample、Yu Peng 2012 与 Tianqing Fang 2024 博士论文；同目录的 `manifest.json` 记录来源和 SHA-256。

清单已检查图片存在性，排除了普通行尾注释与 `comment` 环境。它不是完整的 TeX 编译器，所有条目仍需与实际出版 PDF 对照。清单没有宣称图表数字已经逐格验证。

### 2.2 选定的源稿入口

以下路径相对论文总目录。所有绝对路径见 SOURCE_MAP。

| 工作 | 本地入口 | 版本选择与在 thesis 中的位置 |
|---|---|---|
| KGLink，ICDE 2024 | `KGLink/KGLink_ICDE_revision/KGLink.tex` | 当前找到的该项目研究稿入口，2024-06-01 修改。第 3 章 |
| Understanding the Embedding Models on Hyper-relational Knowledge Graph，CIKM 2025 | `CIKM_FormerGNN/CIKM2025_CR_new.tex` | 根目录版本比模板子目录副本稍新，入口内容相同；实际内容由 `main.tex` 和 `appendix.tex` 输入。第 2.6 节及可选精简附录 |
| GORAG，WWW 2026 | `AGRAG_GORAG/WWW/WWW_CR/GORAG_WWW.tex` | 2026-01-31 camera-ready 目录，比外层 WWW 入口更新。第 4 章 |
| AGRAG，ICDE 2026 | `AGRAG_GORAG/ICDE2026.tex` | 与 `arXIV_cr/ICDE2026.tex` 修改时间相同；已检查主用 section 副本一致。选根目录为唯一搬运入口。第 5 章 |
| MGRAG，VLDB 2026 | `VLDB_MGRAG/pvldbstyle-master/anyrag_vldb26.tex` | 2026-05-27 修改；更晚的 poster 文件不是论文版本。第 6 章 |

AGRAG 的当前入口实际使用 `section/sec-*_sigmod.tex`。这些文件名来自投稿历史，不能因为带有 `sigmod` 就改用旁边同名但无后缀的旧内容。GORAG 必须从其 WWW_CR 自己的 `section/` 与 `figures/` 读取，不能从 AGRAG 共用目录拼装。

### 2.3 在线来源

写作时再次检查网页是否更新。以下来源本次已定位。

| 来源 | 链接与用途 |
|---|---|
| 作者主页 | [Yubo Wang](https://ywangnx.student.ust.hk/)，核对论文范围、作者顺序与接收状态；范围已获作者确认 |
| 学校现行要求 | [FYTGS Guidelines on Thesis Preparation](https://fytgs.hkust.edu.hk/academics/Academic-Regulations-and-Requirements/Handbook-for-Research-Postgraduate-Studies/guidelines-thesis-preparation)，格式与整体性要求的首要来源 |
| 官方博士示例页 | [PhD sample pages](https://fytgs.hkust.edu.hk/system/files/thesis_sample_page_phd.pdf)，第二轮已成功获取 8 页并核对文字、封面、摘要及正文说明页；[本地副本](planning/references/hkust-official-phd-sample.pdf) |
| 图书馆提交说明 | [HKUST Electronic Theses Database](https://libguides.hkust.edu.hk/e-thesis)，最终 PDF 与提交校验 |
| CSE 教授指导 | [Raymond Wong PG Guideline](https://home.cse.ust.hk/~raywong/PGGuideline/#defensePreparation)，提供模板与 Cheng Long 博士论文示例；其中课题组安排不自动适用于本作者 |
| CSE 写作与答辩指导 | [Research Guides](https://cse.hkust.edu.hk/pg/research/guides/) 和 [Thesis Defense Tips](https://cse.hkust.edu.hk/ct/pg/defense.html)，用于论证与演讲准备，不是版式规定 |
| 当前模板候选 | [HKFoggyU/hkust-thesis v0.11.6](https://github.com/HKFoggyU/hkust-thesis/releases/tag/v0.11.6)，社区通用 PhD／MPhil 模板；已检查入口及类源码，尚未编译验证 |
| KGLink 出版记录 | [IEEE document 10597678](https://ieeexplore.ieee.org/document/10597678)；[作者公开稿](https://arxiv.org/abs/2406.00318) |
| HyperKG 出版记录 | [ACM DOI 10.1145/3746252.3761370](https://dl.acm.org/doi/10.1145/3746252.3761370)；[作者公开稿](https://arxiv.org/abs/2508.03280) |
| GORAG 出版记录 | [ACM DOI 10.1145/3774904.3793011](https://dl.acm.org/doi/abs/10.1145/3774904.3793011)；[作者公开稿](https://arxiv.org/abs/2501.02844) |
| AGRAG 出版记录 | [IEEE document 11629443](https://ieeexplore.ieee.org/abstract/document/11629443)；[作者公开稿](https://arxiv.org/abs/2511.05549) |
| MGRAG 出版 PDF | [PVLDB 19(9), 2480–2493](https://www.vldb.org/pvldb/vol19/p2480-wang.pdf)，DOI `10.14778/3819518.3819565`；已阅读其首页、摘要并对照本地方法组织 |

本次没有完成五篇论文的出版 PDF 与源稿的全量逐字、逐数字比对。后续搬运前必须完成此步骤。若出版 PDF 暂时无法获取，可以先建立章节结构；对于尚未对照的数字明确保留内部待核验状态，不把预印本当成已核实的出版版本。

优先级按问题分别处理。

- 研究范围、题目、写作偏好以作者确认为准。
- 学校格式以提交时有效的 FYTGS 要求为准。
- 研究事实以正式论文为准；如果正式论文、代码和最新源文件冲突，列出具体差异给作者，不默默改正或拼接。
- Proposal 提供研究方向和叙事背景，不是最终数据或方法的权威来源。
- 旧 thesis 示例仅提供内容组织参考。

## 3. 模板与篇幅判断

### 3.1 当前模板可以借鉴什么

当前 `main.tex` 是 Wenbin Fang 的 **Mars: Accelerating MapReduce with Graphics Processors**。它设置 `\degree{\MPhil}`，答辩日期为 2010-06-25。现有 PDF 共 49 页，正文到第 36 页，随后是参考文献。

配套 `slides/Makefile` 也明确生成 MPhil slides。另一方面，`main.tex` 有注释掉的 `\degree{\PhD}`，`ustthesis.cls` 实现了 PhD 选项。因此准确判断是“当前内容示例和 slides 为 MPhil，类文件支持两种学位”。切换学位字段仍不足以解决现行前置页顺序、纸张和行距问题。

其内容顺序为 Introduction、Preliminaries and Related Work、Design、Single-Machine Implementations、Multi-machine Implementations、Experimental Evaluation、Conclusion。值得保留的是先交代问题与背景，再解释方法、实现和证据的顺序。它围绕单一系统组织，不能直接作为四项独立研究工作的章节目录，也不能用它估计 PhD thesis 长度。

本 thesis 应采用“共同背景 + 四个相对完整的研究章节 + 跨章节讨论”的形式。各研究章保留本身的设置、结果与分析，避免把四篇不同任务的实验全部塞进一个总实验章。

### 3.2 已核查的 CSE PhD 示例

| 示例 | 已观察到的篇幅与组织 | 对本 thesis 的启发 |
|---|---|---|
| Yu Peng，*Understanding and Utilizing User Preferences*，2012 | [Raymond Wong 提供的源码包](https://home.cse.ust.hk/~raywong/PGGuideline/defense/Thesis-Template.zip)，[本地 PDF](planning/references/yu-peng-2012-phd.pdf) 共 167 页。共同引言与 Related Work 后为三个研究章，结论从印刷页 127、References 从 130 开始 | 先建立共同研究对象，再将不同问题展开为完整研究章节；正确源码入口是 `Thesis/GracePhDThesis.tex`，同包 `Thesis/Thesis.tex` 是 proposal |
| Cheng Long，*On Boosting Spatial Computations for Location-Based Services*，2015 | [完整 PDF](https://home.cse.ust.hk/~raywong/PGGuideline/defense/Thesis-ChengLONG.pdf) 共 216 页。Introduction 后为四个研究章节，正文结论在印刷页 177，References 从 178 开始，另有理论与算法附录 | 同一主线可以由多个自包含的问题章节展开，详细证明放附录 |
| Wangze Ni，*On Efficient Transaction Anonymization Methods in Blockchain*，2023，导师 Lei Chen | [完整 PDF](https://repository.hkust.edu.hk/ir/bitstream/1783.1-140999/1/991013248656403412.pdf) 共 150 页。Introduction、Background 后为三个研究章节，参考文献从印刷页 125 开始 | 共同背景与研究章节分开，每章具有问题、方法、理论及实验链条 |
| Tianqing Fang，*Commonsense Knowledge Base Population and Reasoning for Inferential Knowledge*，2024 | [完整 PDF](https://tqfang.github.io/files/Tianqing_Ph_D__thesis.pdf)，[本地副本](planning/references/tianqing-fang-2024-phd.pdf) 共 155 页。知识获取、benchmark、学习方法与推理相互连接；结论从印刷页 102、Bibliography 从 105 开始 | 主题与本 thesis 接近，适合参考如何把知识结构与语言模型任务串联。各章可承担不同职责，第 6 章只占印刷页 81–85，不必把每项工作扩成同等长度 |

上述四篇均已查看全文 PDF 的相关部分，重点为封面、目录、篇幅及组织，不表示逐项验证其研究结果。它们不是全系统计，不能据此声称 HKUST CSE 存在某个固定平均字数。现行公开准备指南未列出全篇博士论文的统一字数下限或上限，内容要求由 TSC 指导。篇幅预算因此是针对本项目的建议，需要导师最终认可。

旧论文的章节组织与格式要分开借鉴。例如 Tianqing Fang 2024 的摘要仍在目录列表之后，不能照搬到 2025 年调整后的提交版本。官方 sample 的示意目录也不能计入真实 thesis 篇幅样本。

### 3.3 建议字数预算

正文先以 **约 34,000 英文词**为目标，可接受工作区间 **30,000–38,000 词**。四个核心研究章占正文约三分之二以上。附录额外约 3,000–5,000 词，按实际需要安排。

| 部分 | 目标英文词数 | 建议范围 |
|---|---:|---:|
| 1 Introduction | 3,000 | 2,500–3,500 |
| 2 Background and Related Work，含 CIKM 工作精简介绍 | 4,500 | 4,000–5,000 |
| 3 KGLink | 5,000 | 4,500–5,500 |
| 4 GORAG | 5,500 | 5,000–6,000 |
| 5 AGRAG | 6,000 | 5,500–6,500 |
| 6 MGRAG | 6,500 | 6,000–7,000 |
| 7 Discussion | 2,000 | 1,500–2,500 |
| 8 Conclusion and Future Directions | 1,000 | 800–1,200 |
| **正文合计** | **33,500** | **约 30,000–38,000** |

初步排版预算为正文约 125–160 页，连同前置页、参考文献与必要附录约 155–200 页。页数只是规划估计，受公式、原图与表格尺寸影响，不能与字数作固定换算。若全文充分且更短，不扩写空泛背景来凑数；若超出预算，先删重复相关工作和结果复述。

统计时分别报告正文 prose、标题与图表说明、参考文献、附录。以 TeXcount 或同等明确口径的工具计数，并保存命令与输出。不要把 LaTeX 命令、BibTeX 条目和表格数字当成正文词数。

### 3.4 排版迁移必须处理的事项

根据本次核查的 [FYTGS 指南](https://fytgs.hkust.edu.hk/academics/Academic-Regulations-and-Requirements/Handbook-for-Research-Postgraduate-Studies/guidelines-thesis-preparation)，正式 thesis 使用以下顺序。

**Title page → Abstract → Authorization → Signature → Acknowledgments → Table of contents → Lists of figures and tables → Body → Bibliography → Appendices。**

摘要不得超过 300 英文词；建议写成 250–290 词。使用 A4，常规字体为 12 pt，正文为 1.5 倍行距，四边边距一致，25 mm 至不超过 30 mm。前置页从标题页 i 开始使用小写罗马数字，正文第一章从 1 开始，页码位于页底中央。图表应靠近说明它们的正文。最终 thesis 文件为单个未加密、嵌入字体的 PDF。

标题页页码有一处待核实细节。官方 sample 的封面显示 i，但第 6 页文字说标题页不显示 i；现行网页又要求从标题页开始编号。先保留标题页计为 i 的计数规则，最终显示方式在格式定稿时向 FYTGS／系内提交负责人核实，记录答复。这个冲突不影响正文撰写。

现有类文件把标题、授权和签字页合在 `\maketitle` 流程中。正式修改时要调整生成顺序，不能只把 `\input{chapter/sec-abstract}` 移到 `\maketitle` 后便认定已经合规。现有 PDF 检测为 Letter 尺寸，类文件还有历史双倍行距设置，须结合官方 sample 实测纸张、字号、边距及行距，不继承旧注释中的说明。不要直接保留旧作者、旧日期、旧系主任、旧签字文字和 proposal 的答辩日期。

### 3.5 模板选用与小样核验

优先评估 [HKFoggyU/hkust-thesis v0.11.6](https://github.com/HKFoggyU/hkust-thesis/releases/tag/v0.11.6)，以官方 PhD sample 校核最终输出。它是社区维护的通用模板，不是 CSE 官方专用模板。当前发布于 2026-09-23；实际主文件支持 PhD，并已把摘要放到封面之后。README 明确提醒 Overleaf 副本落后于 GitHub，应固定发布版，不直接使用任意同名副本。

迁移前保留当前底稿，并在独立小样中加入完整前置页、一个真实研究节、原图、宽表、公式、算法、引用和附录。新候选使用 XeLaTeX、biblatex／Biber，需检查旧 BibTeX 引用命令、字体、数学及算法宏包兼容性。核验实际 PDF 后再确定采用。当前回合只给出候选优先级，没有完成编译试验或模板迁移。

如果保留当前类文件，则显式修正第 3.4 节的格式问题并完成同样的小样核验。候选模板的示例人物、院系、日期及委员会名单都不能作为作者信息。更多备选与源码入口陷阱见 [参考评估](planning/HKUST_PHD_REFERENCE_REVIEW.md)。

## 4. 整篇论文的论证主线

### 4.1 核心问题

论文讨论语言模型如何使用显式结构组织与选择外部证据，支持表格理解、动态分类、文本问答与多模态问答。共同对象是“模型接收什么证据、证据之间如何连接、这些连接如何影响检索和上下文计算”。

可用的英文中心陈述草案如下。后续根据核实后的结果再定稿。

> This thesis studies how explicit knowledge structures can organize and select evidence for language models. It develops methods for knowledge-enriched table understanding, adaptive retrieval under evolving labels, connected evidence selection for textual queries, and semantic matching over multimodal evidence.

“Reasoning”在这里应通过具体任务与操作解释，包括类型判定、标签推断、证据路径组织和跨模态关系匹配。每章用其原始任务和指标检验效果。不能把检索路径直接等同于模型内部思维过程，也不能用任务效果推出通用推理能力提高。

### 4.2 四个研究问题及相互关系

| 研究问题 | 工作 | 结构怎样参与计算 | 对下一章的连接 |
|---|---|---|---|
| RQ1. 如何把 KG 的外部知识与 PLM 的表格表征结合，处理类型粒度和表内上下文不足？ | KGLink | 实体链接、跨列邻域、候选类型、结构信息增强的表征学习 | 从已有 KG 提供知识，转向任务数据中不断形成的证据关系 |
| RQ2. 当标签与样本随轮次变化时，如何维护结构并为当前文本检索相关标签证据？ | GORAG | 加权关键词—标签关系、连接式候选标签选择、在线索引 | 从分类任务中特定的标签结构，转向一般文本查询的证据子图 |
| RQ3. 如何在文本图中兼顾证据影响力与连接成本，为生成提供相关且连贯的证据？ | AGRAG | 图构建、PPR 影响分数、MCMI 子图与混合检索 | 文本证据的连接仍不足以解决跨模态、语义表达不同的查询匹配 |
| RQ4. 如何针对多模态查询逐步构建证据图，允许路径层面的语义匹配，并让结构参与上下文重计算？ | MGRAG | 查询感知的增量建图、路径语义子图匹配、图感知 KV 重计算 | 汇总结构在表示、检索和上下文服务中的作用 |

这些是共同研究问题下的四种方法，不应写成已经实现的单一端到端系统。不要暗示 MGRAG 调用了 AGRAG 的 MCMI，或 AGRAG 直接复用了 GORAG 的完整图结构，除非代码和正式论文确实支持。

### 4.3 MGRAG 的写作重心

第 6 章以“如何使检索证据在语义和关系上覆盖多模态查询”为问题开端。先解释 query graph 与 evidence graph，再解释一个查询路径为何可能对应数据图中的不同拓扑和多个事实。接着介绍按需建图及停止条件，最后说明结构信息怎样进入 KV 重计算分数。

方法与解释部分建议约 60% 用于查询感知建图和路径匹配，约 20% 用于缓存机制，其余用于整体流程、接口和复杂度。实验部分同时保留检索与缓存证据，不能为了靠近题目而删除缓存贡献。

原稿中缓存操作是**选择性重计算**，需准确说明复用与重计算的对象、预算、图特征和 attention 项。不要写成没有依据的长期记忆、cache eviction 或统一的跨查询记忆系统。

### 4.4 CIKM 工作的位置

在第 2 章设置 **Structural Information in Hyper-relational Knowledge Graphs** 小节，约 900–1,400 词，明确标注这是作者已发表的研究。

内容包含研究问题、分解 HKG 后的信息保留、qualifier capture 与 graph reception 两个分析角度、FormerGNN 的设计响应及一项代表性证据。与主线的联系是结构表示会保留或丢失任务相关信息。它没有直接评估语言模型，因此不将其写成语言模型增强效果的实验证据，也不声称四个主线系统使用了 FormerGNN。

可在附录保留 1,000–1,500 词的设置和结果细节。是否使用附录由正文完整性决定，不把整篇 CIKM 论文作为附录复制进去。正文的 publication-to-chapter 表列出五篇工作；核心贡献列表只组织四条主线。篇幅差异以叙事相关性说明，不在 thesis 中讨论会议等级。

### 4.5 从多篇论文形成一篇博士论文

参考 Yu Peng 的共同问题组织和 Tianqing Fang 的知识到推理的章节连接，引言需要明确四个工作的不同职责。本文可以从结构补充表格知识，推进到动态标签证据维护，再到连接式文本证据选择，最后到多模态查询的语义匹配与上下文计算。这是对已完成研究的组织方式，不要求这些系统具有代码或算法上的继承关系。

在第 1 章形成“研究问题—技术贡献—证据位置”表，在第 7 章回到相同问题做综合分析。每一行至少指向对应章的方法小节和已经发表的实验／定理。CIKM 小节作为结构信息保留的相关研究单独标注，避免读者把作者自己的工作误认成一般背景知识。

每个研究章开头说明本章要回答的问题及输入条件，结尾说明该章已经回答的部分与下一章新增的任务条件。不要为了连接章节凭空增加跨系统实验。论文之间已有设置不同，就按各自条件讨论；统一的是研究问题和术语的解释。

## 5. 逐章写作任务

### Chapter 1 — Introduction

**本章目的**是让读者先理解共同问题，再理解四个工作的必要性。建议结构如下。

1. **Motivation**。用论文已有例子说明外部证据不足、关系被平坦检索忽略、标签变化和跨模态匹配的问题。不要从泛泛的 AI 历史写起。
2. **Research Scope and Structural Augmentation**。说明 KG、任务图、证据子图和查询图在本文中的含义。区分 PLM 与生成式 LLM，解释 KGLink 与后续 RAG 工作的联系。
3. **Research Questions**。按 RQ1–RQ4 展开，每个问题包含具体输入、困难与方法目标。
4. **Contributions**。每条给出一个实际技术增量及其证据类别，不罗列宣传形容词。具体提升数字待原表核实后再加入，不把异构指标合成一个总提升。
5. **Publications and Thesis Organization**。列出五篇论文与章节对应关系，给出每个研究章的来源引用。

建议放一张文字型研究问题对照表。若后续希望新增 thesis 总览图，先向作者确认是否允许原创概念图；默认不新增生图，使用表格与原论文图片即可完成叙事。

### Chapter 2 — Background and Related Work

**本章目的**是提供共用概念与有组织的文献比较，不是五篇论文 related work 的拼接。

建议小节为 Knowledge Graphs and Language Models、Knowledge-enhanced Table Understanding、Retrieval-augmented Generation、Graph-based Evidence Retrieval、Multimodal Retrieval and Context Serving、Structural Information in Hyper-relational Knowledge Graphs、Summary of Research Questions。

相关工作按“证据表示、索引更新、检索单元、连接约束、查询依赖、多模态支持、计算复用”比较。表格中的每个判断应有原始文献支持，不依据论文名称猜测功能。动态 few-shot 的细节留给第 4 章，多模态缓存细节留给第 6 章。

CIKM 小节需要引用其正式论文，并用 `figures/decomp_new.pdf` 或 `figures/QAAgg_new.pdf` 中最直接的一张图解释信息保留问题。可选 `tab:decomp` 或 `tab:formergnn` 的代表性结果，保留数据集、指标和模型条件。不要为简短介绍复制全部消融。

优先使用五篇原论文已引用的文献，并核验 bibliographic metadata。可以更新必要的后续工作，但按时间区分“论文提出时的比较”与“thesis 写作时的讨论”，不把后来方法写成当年的已评估 baseline。

### Chapter 3 — Knowledge-enriched Table Understanding with KGLink

**章节论点**是 KG 结构可提供表内缺失的知识，并通过任务相关的表示学习支持类型判断。

建议小节顺序为 Motivation and Task、Problem Formulation、KG-derived Candidate Types、Language Model Integration、Complexity、Experimental Evaluation、Discussion and Chapter Summary。

方法必须回到源论文展开实体匹配、跨列的一跳邻域过滤、overlapping score、linking quality、候选类型生成、序列化、辅助表示任务与分类目标。尤其检查 DMLM 和候选类型表示生成的具体关系。不要把 proposal 中“hierarchy-constrained selection”“learned aggregation”或“理论保证”等概括直接当作已经实现的算法模块。

证据安排先介绍 SemTab 与 VizNet 的实际子集、类型数、划分、指标和 baseline，再给主要结果，随后解释 KG 信息、辅助任务、过滤、参数与数据效率的证据。原论文没有支持的因果归因不补写。

优先原图为 `figures/tg_issue_small.pdf`、`figures/DL_NotWell_small.pdf`、`figures/kglink_new_overview.png`、`figures/KG_part.pdf` 以及 `overlap`、`dmlm` 对应的原图。源表重点为 `tab:resource`、`tab:performance`、`tab:abl_performance`、`tab:no_ct` 和 `tab:filter`。正文选择能支撑本章论点的结果，其余放附录或省略。

结尾用一段说明固定表格任务和已有 KG 的知识增强过程，为下一章动态任务图引入问题，不写成 KGLink 的失败清单。

### Chapter 4 — Adaptive Graph Retrieval for Dynamic Classification with GORAG

**章节论点**是显式维护关键词与标签的关系，可以适应动态 few-shot 分类中的证据选择和索引更新。

建议小节为 Dynamic Few-shot Classification、Weighted Graph Indexing、Adaptive Candidate Label Retrieval、Classification and Online Indexing、Algorithmic Properties、Experiments、Discussion and Chapter Summary。

清楚说明轮次、标签集合、shot 数、当前可见训练信息以及测试文本进入在线索引的时机。区分真实标签与模型预测标签，准确呈现在线更新。重点解释图中节点与边的实际含义，不沿用 proposal 中未经核实的 exemplar-node 描述。

检索部分按正式论文的优化问题、算法和证明说明 terminal nodes、辅助图、树构造以及候选标签。源稿混用了 MST 与 Steiner tree 表述，须核对后统一说明。不能把需要连接 terminal nodes 的问题直接写成普通 MST 可精确求解，也不能凭写作需要自行更换算法。

实验以 WWW camera-ready 的 CAD、WOS、IFS-Rel 为主，区分主要 accuracy、补充 recall、hallucination rate 等指标。核对 4／6／8 轮与 few-shot／zero-shot 设置。旧目录或注释中的 Reuters 表格不可因看起来完整就搬入正文。

优先图为 `DFSTC_task`、`GORAG_pipeline_example_new`、`runtime_wos`、`runtime_cad`、`wos_4_round_1`、`wos_4_round_5`、`new_case`。主表为 `tab:data_stat`、`tab:main_exp`、`tab:memory_cost`、`tab:token_cost`、`tab:exp_abl`、`tab:0_shot`。图与表的实际扩展名见 SOURCE_MAP。

结尾连接到 AGRAG 的问题是从“哪些标签与当前文本相关”转向“哪些互相关联的事实足以支持开放式回答”。不把两项工作写成同一套在线更新机制。

### Chapter 5 — Connected Evidence Selection for Language Models with AGRAG

**章节论点**是从相关节点进一步组织成有连接结构的证据，能更明确地表达检索内容与查询之间的关系。

建议小节为 Motivation and Task、Graph Construction、Influence-aware Evidence Selection、MCMI Formulation and Algorithm、Hybrid Retrieval、Theoretical Analysis、Experiments、Discussion and Chapter Summary。

按正式论文交代统计式实体抽取具体替代了哪个步骤，区分实体抽取和其他可能仍依赖语言模型的处理。不要写“整个建图过程不使用 LLM”或“消除了全部 hallucination”，除非原论文精确支持。

方法解释 query-to-graph mapping、PPR influence、edge cost、连接要求、MCMI 目标、初始树与后续边扩展，以及图与文本 chunk 如何共同进入生成上下文。给出一个原论文已有案例帮助读者理解环或其他结构的意义。

理论只报告实际定理。源稿中概述的“2-approximation”与详细定理的适用范围需要特别检查。当前详细文本将该保证指向 MCST 构造阶段，并对后续 MCMI 阶段描述单调增益与终止条件。不要把局部阶段的保证扩展为整个 MCMI 优化问题的全局近似保证。若出版稿仍有冲突，先报告作者。

实验区分 Novel、Medical 上的四类任务与 WOS、IFS-REL 的分类任务。按任务解释 ACC、REC、ROUGE-L 等指标；同名 ACC 在分类与生成任务中可能有不同评估协议。主模型、GPT-4o／其他模型补充实验、低资源实验不能合并为同一设置。

优先图为 `AGRAG_pipeline.pdf`、`GERAG_example.pdf`、`heatmap_novel.pdf`、`heatmap_medical.pdf`、`case_light_ner`、`case_mcmi`。主表为 `tab:main_exp`、`tab:data_stat`、`tab:efficiency`、`tab:gpt_exp`、`tab:abl_exp`；低资源与分项耗时表可按需要进入附录。表格采用入口实际编译的版本，避免注释区重复表。

章节结尾引出多模态证据与语义表达差异。不能说 AGRAG 已解决多模态查询，也不为未开展的实验写解释性辩护。

### Chapter 6 — Semantic Graph Matching for Multimodal Reasoning with MGRAG

**章节论点**是查询相关的证据结构需要在语义层面匹配，图结构还可以用于决定哪些上下文计算值得重新执行。

建议小节为 Multimodal Evidence and Query Requirements、Framework Overview、Coarse-grained Ranking、Query-aware Graph Construction、Path-based Semantic Subgraph Matching、Graph-aware KV Recomputation、Complexity、Experiments、Discussion and Chapter Summary。

方法写作必须回答以下问题。

1. 文本、图像和图像 caption 如何进入粗排？避免把 caption-based representation 改写成直接联合视觉 embedding。
2. 查询图中实体、关系和未知量 placeholder 分别是什么？
3. 从排序后的 chunk 逐步建图时，哪些内容因查询而被选择？匹配成功、迭代预算和未成功情况如何决定停止？
4. 路径语义匹配允许何种对应，优化对象与贪心策略是什么？NP-hardness 与算法性质分别对应哪个问题？
5. 生成阶段接收哪些原始 chunk、图序列与查询内容？
6. KV 分数如何结合 query attention、graph-sequence attention 和 graph features？重计算比例、层级与缓存复用对象是什么？

实验保留七个实际使用的数据集，即 MMQA 与 MRAMG 的 Arxiv、Manual、Web、Wiki、Wit、Recipe 六个子集。源稿个别 caption 写成“7 sub datasets”，不得直接沿用该文字造成七与八的混淆，应按出版表的实际列与作者确认处理。记录 Qwen2.5-VL-7B-Instruct 的准确模型名称和模型设置。

先给 QA 效果，再通过 graph construction／matching ablation 解释结构作用，然后给缓存质量—成本结果及端到端分项成本。保留 subgraph matching baselines、KV baselines 与 inverse ablations 的区分，原图或原表没有支持的“跨模态推理能力”概括不补写。

优先图为 `motivation.pdf`、`pipeline_new`、`query_graph`、`graph_based_cache.pdf` 及两张匹配参数曲线。主表为 `tab:dataset_statistic`、`tab:main_exp`、`tab:gm_experiment`、`tab:hop_performance`、`tab:system_comp`、`tab:efficiency_MGRAG`、`tab:abl_exp`、`tab:inv_abl`。`tab:human_eval` 仅按其实际抽样范围介绍，不推成所有场景的建图质量保证。

本章必须同时服务 thesis 主线与论文原贡献，不能因叙事需要弱化、替换或虚构原方法。完整保留支撑缓存结论所需的质量、token、耗时与重计算条件。

### Chapter 7 — Discussion

本章提供 thesis 层面的综合分析，不要求新增实验。按以下主题写约 2,000 词。

- **Where Structure Enters the Pipeline**。比较结构在类型表示、候选标签检索、证据子图、语义匹配与上下文重计算中的位置。
- **Static and Query-dependent Structures**。讨论已有 KG、在线维护图、文本证据图、按需多模态图各自对应的任务条件。
- **Evidence Quality and Computational Cost**。用各章已报告的结果说明权衡，不跨任务平均 accuracy，也不把不同硬件或 backbone 的时间数字直接排名。
- **Information Preservation**。将 CIKM 的结构信息保留观察与主线的设计问题联系起来，标明这是综合讨论，不能声称有跨论文的因果实验。
- **Limitations and Open Questions**。集中写真正影响解释的条件，例如 KG coverage、在线预测误差、生成式评估、图抽取质量与任务迁移。每个限制说明影响哪个结论，避免反复写未宣称事项。

推荐一张无新增数字的比较表，列出每项工作的输入、结构来源、检索对象、更新方式、模型角色和主要评估任务。所有格子均可追溯到原论文。

### Chapter 8 — Conclusion and Future Directions

先按 RQ1–RQ4 总结实际获得的认识，不把五个摘要压缩后串起来。未来方向可以围绕查询适应的结构维护、跨模态结构质量及反馈驱动的证据更新展开，明确是研究方向。

CMI-Mem 如需提及，应作为后续探索的例子，并说明当前状态；ClinicalAgents 如需提及，应说明合作工作属性。两者不出现为本 thesis 已验证的核心贡献。删除 proposal 中已过时的 2026–2028 计划表、项目进度风险说明和“预期结果”。

### Front matter 与附录

摘要在所有研究章完成后写，采用“研究问题 → 四项技术响应 → 经核实的主要认识”结构，控制在 300 词以内。致谢由作者提供实际对象与经历，agent 不生成虚构的私人关系、感谢理由或委员会贡献。

附录按必要性安排，候选内容为完整证明、伪代码、参数与数据集划分、补充结果和 prompt。CIKM 工作可有精简补充说明。正文必须保留理解主要结论所需的算法、关键条件和结果，不能把核心证据全部移到附录。

## 6. 原图、表格与引用的搬运规范

### 6.1 图片

正式搬运前先给每个采用条目补上 `published_figure_number`、`published_page`、`target_chapter`、`target_path` 和 `verified_by`。建议目标目录为 `figures/kglink/`、`figures/gorag/`、`figures/agrag/`、`figures/mgrag/`、`figures/hyperkg/`，保留原文件名并避免跨论文重名覆盖。

直接复制原始 PDF／PNG 等资源并校验 SHA-256。优先论文原有矢量版本，不将整张图截图后当作原图。只调整 LaTeX 展示宽度与浮动位置，不修改坐标、曲线、图例、色彩或图内数字。原稿中仅通过 TeX 拼接的 subfigure 保留全部子图和对应含义。

图注可以重写以适应 thesis 的自包含阅读，但不得改变原图所比较的对象和设置。图中旧章节号或旧符号若造成矛盾，向作者提出具体修改请求，不能静默重画。

本计划没有预先把所有候选图片复制到项目。应在选定正文图表并完成出版核对后复制，避免把旧稿素材误认为最终图表。现有清单保证后续 agent 可以直接定位。

### 6.2 表格

保留原始行列、数字、小数位、单位、统计符号、粗体语义、缺失值标记和 caption 对实验条件的说明。允许为单栏 thesis 拆分宽表或调整排版；拆分时重复列头、标注来源，确保所有数据可回到原表。

不得把 `-` 变成 0，不能推算未报告的标准差、显著性或新指标。MGRAG 表中的长时间未完成标记尤其不能改写成模型分数为零。不要从曲线像素估计值后填成新结果表。

每张表建立逐单元格核验记录，至少包含出版表号、源 TeX 行号、数据集、模型版本、实验条件、目标表号与核验状态。若需要叙述相对提升，明确比较对象及计算方式；百分比与百分点区分。没有必要时直接引用原始分数，减少派生数字。

### 6.3 公式、理论与引用

各章可统一通用符号，但保持原公式语义。跨章同一字母含义不同时，使用局部符号表或显式下标，不能为统一记号而改变定义。

引用合并时以 DOI／标题／作者检查重复，不因 BibTeX key 相同而覆盖不同文献。统一参考文献风格，保留每章的来源声明。章节可写 “This chapter is based on …” 并引用正式论文；作者个人贡献说明由作者提供，不能从第一作者身份推测所有分工。

## 7. 文风与防御性写作审计

撰写 agent 应读取 `/Users/ybwang/.codex/skills/academic-defensive-writing-auditor/SKILL.md`，先写准确内容，再做审计。采取“技术事实或结果 → 证据 → 必要的适用条件”的顺序。

正文使用直接的主谓结构，少用冒号引出长串枚举，少用破折号插入补充说明，避免反复用三项排比和空泛收尾。论文正式名称、数学符号、算法名称和确有必要的列表不机械禁用标点。

特别避免以下写法。

- 每段以 “We emphasize that” 或 “It should be noted that” 开始。
- 反复解释“不声称”“不意味着”“不是为了证明”。
- 用 “For a fair comparison” 代替实验设置本身。
- 无诊断证据便解释较低分数的原因。
- 将 “robust”“comprehensive”“promising” 等评价词当成结果。
- 每节结尾添加没有新信息的 “Together, these results demonstrate”。

保留会改变结果解释的必要条件，如数据集子集、label availability、评估模型、硬件、知识覆盖范围、理论假设与计算预算。不要为了去掉防御性语气而删除必要条件或加强主张。

以下是针对已读材料的初步审计示例，帮助后续 agent 理解处理方式，不是整篇 thesis 的评分。

| Location | Original | Type | Severity | Necessary caveat? | Why it feels defensive | Likely reviewer reaction | Recommended action | Rewrite |
|---|---|---|---|---|---|---|---|---|
| KGLink 原稿数据集段 | “It's important to note that each web table in this dataset contains multiple columns.” | D1 | Minor | MIXED | 多列表格是协议事实，无需强调式前缀 | 想直接看到所用子集 | 删除前缀，保留事实 | “Each table in the selected subset contains multiple columns.” |
| Proposal 贡献汇总 | “Taken together, the four contributions form a coherent research arc.” | D11 | Minor | DEFENSIVE | 该句宣告连贯性，未说明技术联系 | 更需要实际联系而非自我评价 | 用结构参与计算的位置概括联系 | “The four studies examine how graph structure supplies knowledge, selects evidence, and guides context processing.” |
| Thesis 待写结果讨论 | 没有已完成正文 | — | — | — | 不虚构原文或审计发现 | — | 正文完成后再逐句审计 | — |

**Paper-level defensive-writing score** 暂不评全篇。以上局部示例不能代表尚未撰写的 thesis。

**Highest-priority removals** 是 proposal 的预期成果与时间线风险辩护、原论文里的空间限制说明、反复宣称比较公平、没有证据的结果归因，以及重复的综合总结句。

**Necessary caveats to preserve** 包括任务与指标定义、在线信息可见性、LLM 评估方式、近似保证的实际条件、缓存预算与硬件条件。

**Repeated phrase audit** 在完整初稿后统计 D1–D14 可疑短语、冒号和破折号的分布，逐处判断，不设置机械的删词配额。正式审计报告按 skill 的完整九列表格返回，并附全篇评分、优先修改、保留条件和重复短语计数。

## 8. 建议执行顺序与交付约定

### 阶段 A — 固定来源与搭建骨架

读取本计划、SOURCE_MAP、proposal 和五篇选定源稿；获取正式出版 PDF，建立图表与论文版本核对记录。先解决会影响整体方法叙述的版本问题，其他章节可继续。

先阅读 `planning/HKUST_PHD_REFERENCE_REVIEW.md` 并完成第 3.5 节的小样核验，比较优先候选与修复当前类文件的实际成本，再固定模板及版本。保留可恢复的旧示例。创建章节骨架与 bibliography 合并草稿，核对前置页顺序、纸张、字号、页码和行距。此阶段不需要新增实验。

### 阶段 B — 撰写研究章

顺序建议为 KGLink → GORAG → AGRAG → MGRAG。每章先做“论点—来源—图表”映射，再写方法与实验，最后写该章引言和小结。完成一章后核查其全部数字、公式、图表和引用，不把事实核查推迟到全篇末尾。

每章交付包括章节 TeX、已采用的原图、经核验的表格、引用增量与简短核验记录。记录中保留该章“研究问题—技术贡献—关键证据”的对应关系，供全文讨论与未来答辩复用。遇到歧义写入内部记录并向作者提出具体问题，不让 `TODO` 混入看似完成的最终 PDF。

### 阶段 C — 形成整体论证

撰写第 2 章与 CIKM 精简介绍，再写第 1、7、8 章，最后写摘要。统一定义、章间连接、研究问题与贡献表。删去各章重复背景和重复的 related work，保留研究章可独立理解所需的信息。

### 阶段 D — 全文审阅与交付

依次进行来源核验、逻辑一致性检查、防御性语言审计、英文编辑和 PDF 视觉检查。检查所有原图的字号、裁切、清晰度和图表分页，修复未定义引用、重复标签、缺失图片和溢出。所有检查基于最终 PDF 与对应源码，不能只检查较早构建。

最后交付可编译的 LaTeX 项目、单一 PDF、分章词数与页数、已核验素材清单，以及仍需作者决定的具体事项。未解决的方法或数字冲突应保持可见，不以“写作完成”掩盖。

### 建议章节文件

继续使用当前项目的 `chapter/` 结构即可。建议新文件为 `ch01-introduction.tex`、`ch02-background.tex`、`ch03-kglink.tex`、`ch04-gorag.tex`、`ch05-agrag.tex`、`ch06-mgrag.tex`、`ch07-discussion.tex`、`ch08-conclusion.tex`。前置页与附录分开维护。新 label 使用 `ch:`、`sec:kglink:`、`fig:gorag:`、`tab:mgrag:` 等前缀，避免原论文都使用 `tab:main_exp` 产生冲突。

本次为规划工作，不要求新建 CHANGELOG、METHODS 或 FUTURE_WORK。后续实施遵循项目已有文档结构，不为满足流程而创建多余文件。

## 9. 需要作者输入的事项与触发条件

已经确认的题目、五篇论文范围、四篇主线和最新版本选择，不再重复询问。以下内容在实际需要时确认。

| 事项 | 何时需要 | 当前处理 |
|---|---|---|
| 最终提交月份、答辩日期、签字页人员与正式职衔 | 制作正式 front matter 前 | 不沿用旧模板或 proposal 日期，不填猜测值 |
| 致谢内容与合作贡献分工 | 写致谢与个人贡献说明前 | 向作者索取真实信息 |
| 正式论文、最新源稿、公式或代码不一致 | 相应段落或表格定稿前 | 给出两处原文和具体冲突，请作者裁定 |
| 导师对篇幅或章节有不同要求 | 初稿组织阶段 | 当前 33,500 词为规划目标，按导师要求调整 |
| 标题页 i 是否显示 | 最终格式核验时 | 官方 sample 图示与文字不一致，由 FYTGS／系内提交负责人确认；不影响研究章写作 |
| 新增原创总览图、重绘原图或新增实验 | 动手之前 | 当前计划未包含这些工作 |

本计划已经足以启动来源核对和正文撰写。未知的 front matter 资料不阻碍研究章工作。

## 10. 可直接交给下一个 agent 的启动指令

> 请在 `/Users/ybwang/Library/CloudStorage/OneDrive-HKUSTConnect/paper/thesis/hkust-latex-thesis` 中撰写英文 PhD thesis。先完整阅读 `THESIS_WRITING_PLAN.md`、`planning/HKUST_PHD_REFERENCE_REVIEW.md`、`planning/SOURCE_MAP.md` 和 `planning/source_roots.json`，再阅读 proposal 与各论文实际输入的源文件。题目固定为 **Structural Augmented Reasoning for Language Models**。四个核心研究章依次为 KGLink、GORAG、AGRAG、MGRAG。CIKM 2025 的超关系知识图谱工作在背景章节中作明确但精简的介绍，必要时补充附录。CMI-Mem 和 ClinicalAgents 不进入核心贡献。
>
> 作者已允许选择各入口的最新研究稿，正式出版 PDF 是方法、数字与结论的最终核对依据。使用计划指定入口，不从旧投稿目录、注释表格、审稿回复或海报混取内容。开始搬运前完成相应源文件与出版图表核对。研究图片复制原图并校验，表格不得改数据或补造数据。不要补造实验、理论保证或作者贡献。
>
> 先按第 3.5 节完成模板小样核验，优先评估 HKFoggyU v0.11.6，格式以现行 FYTGS 要求和本地官方 PhD sample 为准，摘要紧接标题页。旧 CSE PhD 论文用于内容组织参考。按约 33,500 英文词组织正文，具体分配和章节职责见计划。优先完成四个研究章，再写共同背景、引言、讨论、结论和摘要。MGRAG 以查询感知建图与路径语义匹配接入主线，缓存保留为结构参与上下文计算的贡献。不同方法之间建立问题联系，不虚构算法依赖或统一系统。
>
> 使用 `/Users/ybwang/.codex/skills/academic-defensive-writing-auditor/SKILL.md` 审计文风，少用冒号、破折号、免责声明与模板化总结句，保留真正影响科学解释的条件。遇到方法、公式、版本或数据冲突，给出具体证据向作者确认，同时推进无冲突的部分。完成后交付源码、PDF、词数、素材核验清单和未决事项。

## 11. 为答辩保留的材料与时间约束

### 11.1 写作时积累答辩材料

本轮检索没有找到可确认的官方 CSE PhD final defense 专用公开 slides 模板。通用 HKUST Beamer 和个人 MPhil slides 的链接及边界见 [参考评估第 4 节](planning/HKUST_PHD_REFERENCE_REVIEW.md#4-答辩-slides-与-thesis-模板分开选择)。以后可以选择其中的视觉样式，内容按博士论文的共同问题与贡献组织。

参照 [CSE Thesis Defense Tips](https://cse.hkust.edu.hk/ct/pg/defense.html)，撰写过程中保留以下材料，暂不制作 slides。

- 每个 RQ 的简洁回答、一项具体技术增量、最直接的原图／原表／定理，以及结论适用的实验或理论条件。
- Proposal 中曾被询问的问题及回答证据。当前 proposal PDF 不等于答辩问答记录，历史问题需作者提供。
- 理论假设、完整数据表、补充消融与模型／硬件设置的后备材料位置。
- 一张 thesis 层面的研究问题与贡献对照表，支持解释四项工作为何属于同一研究方向。

正式答辩内容应重新组织，集中讲共同背景，给 MGRAG 的结构匹配与上下文计算保留足够解释空间。报告时长与 slides 数量待导师和当次通知确认，不把某位教授的课题组建议作为全系要求。

### 11.2 以答辩日倒排

现行 [FYTGS 指南 F 节](https://fytgs.hkust.edu.hk/academics/Academic-Regulations-and-Requirements/Handbook-for-Research-Postgraduate-Studies/guidelines-thesis-preparation) 要求，送审 thesis 及 draft 的 iThenticate 报告在答辩前至少四周提交系里。写作排期必须为导师阅读、事实核验和格式修订留出更早的时间；具体日期在作者确定答辩日后填写。

答辩后按要求完成修订及相关 originality check，再取得签字。当前流程将已签署的 Signature／Authorization 页合成一个 PDF 单独上传，最终 thesis 为另一个 PDF，无需把扫描签字页替换进 thesis 正文文件。提交前再次核对当时有效流程，并运行图书馆 PDF preflight。

以上只是把官方提交节点纳入写作安排。本计划不预填答辩日期、签字人员，也不代替系里当次通知。
