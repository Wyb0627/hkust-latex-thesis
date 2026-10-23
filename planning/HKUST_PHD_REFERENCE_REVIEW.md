# HKUST CSE PhD 模板与示例补充评估

核查日期 2026-10-23。本次补充服务于 [THESIS_WRITING_PLAN.md](../THESIS_WRITING_PLAN.md)，没有更换项目模板、生成 thesis 正文或制作答辩 slides。

建议采用三类材料各司其职。**格式以 FYTGS 官方说明和 PhD sample 为准，LaTeX 底稿优先评估 HKFoggyU 的当前发布版，内容组织参考真实 CSE 博士论文。** 本地示例确为 MPhil，但其类文件也支持 PhD，不能仅凭示例学位判断整个类文件不可用。

## 1. 官方要求与 CSE 指导

| 资源 | 本次核查范围 | 用于本项目的结论 |
|---|---|---|
| [FYTGS Guidelines on Thesis Preparation](https://fytgs.hkust.edu.hk/academics/Academic-Regulations-and-Requirements/Handbook-for-Research-Postgraduate-Studies/guidelines-thesis-preparation) | 当前网页全文，包括原创性、组成、格式与提交流程 | 博士论文要形成完整论证；内容由 TSC 指导。网页未规定统一全篇词数。旧存档论文不能代替现行格式要求 |
| [官方 PhD sample](https://fytgs.hkust.edu.hk/system/files/thesis_sample_page_phd.pdf) | 已完整下载 8 页，读取文字并查看封面、摘要、正文说明页 | 明确使用 Doctor of Philosophy；摘要紧接封面；A4、统一页边距及各前置页可直接对照 |
| [Raymond Wong PG Guideline](https://home.cse.ust.hk/~raywong/PGGuideline/#defensePreparation) | 模板、博士论文示例与答辩指导段落 | 提供可追溯的 CSE PhD 源码；特别提醒 2025-02-03 起摘要位置调整。课题组的安排不自动成为全系规则 |
| [CSE Research Guides for PG Students](https://cse.hkust.edu.hk/pg/research/guides/) | 页面栏目与外链目录 | 可继续阅读 Dissertation 和 Thesis Defense 栏目。它是资源导航，所链接的校外文章不是 HKUST 格式政策 |
| [CSE Thesis Defense Tips](https://cse.hkust.edu.hk/ct/pg/defense.html) | 页面全文 | 准备 proposal 中的难题、解释缩写、让图表准确对应论点、为事实与假设准备来源，并进行演练 |
| [Library E-thesis Guide](https://libguides.hkust.edu.hk/e-thesis) | 提交与 PDF 核验入口 | 成稿阶段使用官方 PDF preflight，核对字体嵌入、图像和单文件提交 |

官方 sample 的本地副本为 [hkust-official-phd-sample.pdf](references/hkust-official-phd-sample.pdf)。它的目录页采用示意章名和示意页码，不能当作一篇真实博士论文来估计篇幅。

有一处官方材料内部不一致需要保留记录。sample 第 1 页实际显示罗马数字 i，第 6 页说明却写 “i is not shown on the title page”；当前网页要求从标题页开始编号。可以确定标题页计为 i，但最终是否显示该数字应在格式定稿时向 FYTGS／系内提交负责人核实。不要为了迁就某个旧模板而把冲突抹掉。

## 2. LaTeX 模板候选

| 候选 | 身份与已核实情况 | 建议用途 |
|---|---|---|
| [HKFoggyU/hkust-thesis](https://github.com/HKFoggyU/hkust-thesis)，[v0.11.6](https://github.com/HKFoggyU/hkust-thesis/releases/tag/v0.11.6) | 社区维护的 HKUST 通用 PhD／MPhil 模板。本次核查 release、README、主文件与类实现源码；2026-09-23 发布 v0.11.6。主文件实际配置为 PhD，前置页顺序已更新 | **优先评估的底稿**。固定发布版，先编译本项目小样；本次没有执行其编译，也未验证完整输出 |
| [Raymond Wong 提供的 Yu Peng 模板 ZIP](https://home.cse.ust.hk/~raywong/PGGuideline/defense/Thesis-Template.zip) | 真实 CSE PhD 源码。正确入口为 `Thesis/GracePhDThesis.tex`，对应 Yu Peng 2012 博士论文 | 优先学习多工作整合与章节组织。格式年代较早，不直接作为现行提交版 |
| [fcyu/HKUST_PhD_MPhil_thesis_Latex](https://github.com/fcyu/HKUST_PhD_MPhil_thesis_Latex) | 已读 `thesis.tex` 和 `thesis.sty`，有 PhD 配置，使用 report／自定义样式及 BibTeX 路线，示例信息来自其他学科 | 轻量实现的对照候选；实际前置页仍把摘要放在列表之后，需要更新 |
| [onlytailei/HKUST_latex_thesis_2019](https://github.com/onlytailei/HKUST_latex_thesis_2019) | README 与文件列表表明是 ECE 的 PhD／MPhil 模板；未做源码全审和编译 | 历史排版参考，不是 CSE 专用现行模板 |
| [UsmanMaqbool/hkust-phd-mphil-thesis](https://github.com/UsmanMaqbool/hkust-phd-mphil-thesis) | ECE 2021 示例，含签字页处理；本次仅核查项目说明 | 如需比较签字页实现可参考，不能把 ECE 委员会展示要求直接搬到 CSE |
| [AI-Huang/HKUST_PhD_MPhil_Thesis_LaTeX](https://github.com/AI-Huang/HKUST_PhD_MPhil_Thesis_LaTeX) | 作者个人 MPhil 改版，说明中承认部分版式未完全一致 | 不列为优先方案 |
| [Cheedoong/hkust-latex-thesis](https://github.com/Cheedoong/hkust-latex-thesis) 与当前本地项目 | 当前示例为 Wenbin Fang 的 2010 MPhil，类文件提供 PhD 选项；`slides/Makefile` 也明确产生 MPhil slides | 保留为可恢复的旧底稿与兼容性对照，不继续用其 49 页示例推算 PhD 篇幅 |

不要把 HKUST (Guangzhou) 的模板视为本项目可直接采用的清水湾校区格式。也不要把名称含 PhD 的社区仓库标为学校官方模板。

### HKFoggyU 的具体采用条件

本次核对的 [v0.11.6 主文件](https://github.com/HKFoggyU/hkust-thesis/blob/v0.11.6/mythesis.tex) 实际依次调用封面、摘要、授权页和签字页。文件上方仍有一段未更新的旧顺序注释，后续 agent 应以实际调用及生成 PDF 为准。[类源码](https://github.com/HKFoggyU/hkust-thesis/blob/v0.11.6/hkustthesis.dtx) 的变更记录包含 2025-02-03 的摘要位置修改，以及 2026-09-23 的 iThenticate 字符问题修复。

项目 README 提醒 Overleaf 副本落后于 GitHub。应从发布页获取固定版本，记录版本及文件哈希；不把搜索结果中任意同名 Overleaf 副本当作当前发布版。

这个方案使用 XeLaTeX、biblatex 和 Biber。当前项目及论文源稿的 BibTeX 命令、旧字体宏包、数学宏包和算法环境不能整体叠加进去。建议小样包含完整前置页、一个真实研究节、一张原图、一张宽表、公式、算法、引用和附录。核对 A4、12 pt、边距、行距、编号和字体后再决定迁移。字体与行距应检查输出，不能仅把某个 `linespread` 数值认作合规证明。

模板中的人物、机构、日期是示例值；委员会展示选项涉及院系差异。正式 CSE 信息由作者提供，并与当年的提交要求核对。

### Yu Peng 压缩包的入口陷阱

`Thesis/GracePhDThesis.tex` 和对应 PDF 才是本次确认的 **Understanding and Utilizing User Preferences**。包中的 `Thesis/Thesis.tex` 是 proposal，嵌套目录还包含其他旧论文，不能根据文件名最短或最通用就选择入口。已单独保留 [正确的 PhD PDF](references/yu-peng-2012-phd.pdf)，没有把整个历史工程导入本项目。

## 3. 完整 CSE PhD 论文的组织与篇幅

“总页数”是 PDF 物理页数；正文、参考文献起始页是文中印刷页码，两者不能混算。此处检查用于内容组织，不代表逐项验证这些论文的研究结论。

| 作者与论文 | 总页数与正文边界 | 观察及可借鉴之处 |
|---|---|---|
| Yu Peng，2012，*Understanding and Utilizing User Preferences*。[源码包](https://home.cse.ust.hk/~raywong/PGGuideline/defense/Thesis-Template.zip) | 167 页；结论从 127 开始，References 从 130 开始，证明附录从 141 开始 | Introduction 和 Related Work 后有三个研究章。引言先解释理解与利用偏好的共同问题，研究章各自完成定义、方法与实验 |
| Cheng Long，2015，*On Boosting Spatial Computations for Location-Based Services*。[PDF](https://home.cse.ust.hk/~raywong/PGGuideline/defense/Thesis-ChengLONG.pdf) | 216 页；正文至 177，References 从 178 开始 | 四个研究章围绕统一主题组织，长证明与算法细节放附录。沿用前次核查记录 |
| Wangze Ni，2023，*On Efficient Transaction Anonymization Methods in Blockchain*。[PDF](https://repository.hkust.edu.hk/ir/bitstream/1783.1-140999/1/991013248656403412.pdf) | 150 页；References 从 125 开始 | 导师 Lei Chen。共同背景后有三个研究章，问题、理论和实验各自完整。沿用前次核查记录 |
| Tianqing Fang，2024，*Commonsense Knowledge Base Population and Reasoning for Inferential Knowledge*。[PDF](https://tqfang.github.io/files/Tianqing_Ph_D__thesis.pdf) | 155 页；结论从 102 开始，Bibliography 从 105 开始，附录从 136 开始 | 与知识结构、语言模型和推理方向较接近。按知识获取、评估／学习、下游推理展开；第 6 章仅占印刷页 81–85，章节长度取决于论证职责 |

本次新增的 Yu Peng、Tianqing Fang PDF 已下载并核查封面、目录与相关组织说明。Fang 的本地副本见 [tianqing-fang-2024-phd.pdf](references/tianqing-fang-2024-phd.pdf)。它们均使用 2025 年调整之前的摘要顺序，因此只用于内容参考。

这四个样本的 PDF 总页数为 150、155、167、216，正文规模也不同。它们支持“共同问题加多个研究章”的组织方式，但不是随机样本，不足以给出 CSE 博士论文的统计主流词数。保留本项目 **33,500 英文词、30,000–38,000 工作区间、总页数初估 155–200** 的预算，性质仍是写作建议。

另找到 [Zihao Wang 的 Querying Neural Graph Databases](https://researchportal.hkust.edu.hk/en/studentTheses/querying-neural-graph-databases/)（CSE PhD，2025）。本次只核查官方元数据和摘要，没有获取可核查全文，因此不把它列入页数统计或章节结构证据。

## 4. 答辩 slides 与 thesis 模板分开选择

本轮没有找到能够确认是 **HKUST CSE 官方 PhD final defense 专用** 的公开 PowerPoint／Beamer 模板。以下资源可参考视觉样式，不构成全系规定。

| 资源 | 已确认的定位 | 使用边界 |
|---|---|---|
| [ArthurHowardMorris/HKUST_Beamer_Template](https://github.com/ArthurHowardMorris/HKUST_Beamer_Template) | 通用 HKUST Beamer，README 说明校色和标志来源 | 可作为简洁 slides 主题候选；README 也提示标志分辨率问题，需要看最终投影效果 |
| [Boyang Zhang 的 HKUST Beamer 模板](https://www.overleaf.com/latex/templates/hkust-beamer-template/wsjnrdpyhmfn) | 学术报告／授课用途，公开模板页可见源码 | 可参考配色与版式；并非 CSE 博士答辩内容模板 |
| [HKFoggyU/HKUST-MPhil-defense-template](https://github.com/HKFoggyU/HKUST-MPhil-defense-template) | 仓库明确标注个人 MPhil defense 备份，使用 XeLaTeX／Biber | 可以借鉴样式，不能将它误报为已找到的 PhD 答辩示例。它与上面的通用 thesis 仓库是两个项目 |

PhD slides 的核心是支撑整体研究贡献。四篇论文不宜各讲一场完整 conference talk 后拼接。写 thesis 时应积累每章的“问题、技术增量、决定性证据、适用条件”，将共同背景集中讲，证明细节与完整表格留作后备材料。这里仅作未来答辩准备建议，本轮不创建 slides。

Raymond Wong 页面给出的博士 presentation 时长建议属于其指导语境。实际答辩时长、语言和安排以作者导师、CSE 当次通知为准，不据此给全系规定一个固定时长。

## 5. 已落实到 writing plan 的补充

1. 明确本地示例／slides 是 MPhil，而类文件同时支持 PhD；加入当前模板候选及小样验证步骤。
2. 把官方 PhD sample 从“未成功获取”更新为“已获取并检查”，补充 A4 与标题页编号冲突记录。
3. 扩充 CSE PhD 样本，保持词数预算为建议；章节长度按实际贡献与证据分配。
4. 加强共同研究问题和章节职责说明。KGLink、GORAG、AGRAG、MGRAG 的顺序与题目保持作者已确认的版本。CIKM 工作保持可识别的短节。
5. 增加跨章“研究问题—技术贡献—已发表证据”表和每章事实核验要求，为 thesis 综合讨论和以后答辩共用。
6. 根据现行 FYTGS 指南，纳入答辩前至少四周提交 draft 和 iThenticate 报告的时间约束；实际日期待作者确认。

## 6. 核查范围与复用记录

本轮没有编译外部模板，也没有做五篇作者论文出版 PDF 的逐格数据比对。下载失败或不完整的其他 thesis 文件未进入本地参考集合，也不计入样本统计。

保存的三份 PDF 合计约 3.5 MB，文件来源、字节数和 SHA-256 见 [references/manifest.json](references/manifest.json)。社区模板保留在线入口和选用建议，尚未复制为项目依赖。后续 agent 应先阅读主计划，再使用本文件选取适合的参考，不按资源数量增加 thesis 的背景篇幅。
