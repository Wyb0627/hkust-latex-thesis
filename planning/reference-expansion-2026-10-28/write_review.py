from pathlib import Path
import collections, hashlib, json, re, shutil
root=Path(__file__).resolve().parents[2]
out=Path(__file__).resolve().parent
ledger=json.loads((out/'reference-ledger.json').read_text())
checks=json.loads((out/'source-checks.json').read_text())
pre=json.loads((out/'pdf-qa/pdf-preflight.json').read_text())
counts=json.loads((out/'pdf-qa/chapter-counts.json').read_text())
scholar=json.loads((out/'scholar-crosscheck-index.json').read_text())
assert hashlib.sha256((root/'main.pdf').read_bytes()).hexdigest()==pre['pdf_sha256']
assert (root/'main.pdf').read_bytes()==(root/'thesis.pdf').read_bytes()
assert len(re.findall(r'\\entry\{',(root/'main.bbl').read_text()))==129
fonts=(out/'pdf-qa/pdffonts.txt').read_text().splitlines()[2:]
assert len(fonts)==95 and all(x.split()[-5]=='yes' for x in fonts)
qa=dict(status='PASS',pdf_sha256=pre['pdf_sha256'],pages=pre['pages'],embedded_fonts=len(fonts),bbl_printed_entries=129,independent_papers=123,all_pages_rendered=True,contact_sheets_reviewed=7,detailed_pages_reviewed=[15,26,31,117,125],original_figure_margin_flags=pre['text_outside_approx_25mm_body'])
(out/'final-validation.json').write_text(json.dumps(qa,indent=2))
shutil.copy2(out/'texcount.txt',root/'planning/qa/texcount.txt')
text='''# 引用扩充与写作复核记录

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
'''
for key,reason in checks['excluded_from_paper_count'].items():text+=f'| `{key}` | {reason} |\n'
text+='''
因此，目标按 **123 篇独立论文** 达成，而非仅通过软件、数据或重复报告达到条目数量。

## 文献选择与正文修改

新增 **56 篇**，其中 **36 篇**来自作者既有论文 bib，**20 篇**通过外部检索补充。检索了 KGLink、AGRAG/GORAG、MGRAG、CIKM 超关系图、GFM、KBLink、CoT survey、NIPS 及 NER 等 11 个原始文献库；候选及原始路径保存在 `local-candidates.json`，最终选择在 `shortlist.json`。

新增会议论文 50 篇，均采用 CCF A 类会议的正式全文记录（包括两篇 PVLDB 归档论文）；另有 6 篇 JMLR、TACL、ACM Computing Surveys 期刊论文。新增文献没有依赖未发表预印本，因此无需通过引用量门槛放行。已有参考文献未按本轮新增标准删除。

官方目录依据：[CCF 人工智能类](https://www.ccf.org.cn/Academic_Evaluation/AI/)、[数据库/数据挖掘/内容检索类 A 类会议](https://www.ccf.org.cn/Academic_Evaluation/DM_CS/zgjsjxhtjgjxshy/al/)、[WWW 官方目录条目](https://www.ccf.org.cn/Academic_Evaluation/Cross_Compre_Emerging/zgjsjxhtjgjxshy/al/2017-04-25/592216.shtml)、[CCF 分类说明](https://www.ccf.org.cn/Academic_Evaluation/By_category/)。按 full/regular paper 口径处理，未将 Findings 或 workshop 当作主会全文。

| 会刊 | 新增篇数 |
|---|---:|
'''
for venue,n in collections.Counter(x['venue'] for x in ledger).most_common():text+=f'| {venue} | {n} |\n'
text+='''
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
'''
for r in ledger:
 src='外部检索' if r['original_source']=='external-primary-search' else '/'.join(Path(r['original_source']).parts[-2:])
 locs=', '.join(f"[{Path(v['file']).stem}:{v['line']}](../../{v['file']}#L{v['line']})" for v in r['locations'])
 title=r['title'].replace('|',r'\|')
 text+=f"| `{r['key']}` | [{title}]({r['primary_url']}) | {r['venue']} {r['year']} | `{src}` | {locs} |\n"
text+=f'''
## 写作规范复核

按作者最新规范复查新增段落，并扫描摘要及八章。结合 `academic-defensive-writing-auditor` 检查 reviewer-facing 辩解、重复非主张、空泛总结和宣传措辞。未检出常见“we do not claim / to ensure fairness / it should be noted / taken together”等表达；叙述文件中未检出句中 em dash 或 LaTeX `---`。冒号限于研究问题标题、原论文题名及不排印的注释，没有新增句中冒号。已有必要条件涉及索引状态、标签信息、图覆盖、指标语义及未报告的重计算预算，保留其科学作用。详见 `WRITING_CHECK.md`。

上一轮全文 44 处措辞修改和七处空引用的详细记录继续保存在 `../citations-wording-2026-10-28/REVIEW.md`。本轮仅扩充 ch01/ch02；摘要与 ch03–ch08 相对本轮开始时逐字节一致。原有非空引用、标签、数学、算法、图表及表格数据均保留，只新增一个少样本学习节标签。

## 编译与 PDF 检查

通过 `latex-paper-en` 技能的 `compile.py` 清理后以 XeLaTeX、latexmk、Biber 重建，禁用 shell escape。最终日志 `compile-final.log`。无未定义引用、缺字、重复标签/目标、overfull box 或 LaTeX 错误；Biber 无警告或错误。

`main.pdf` 与 `thesis.pdf` 完全一致，SHA-256：`{pre['pdf_sha256']}`。

PDF 共 **125 页**，包含 14 页前置、102 页正文、9 页参考文献。95 项字体均嵌入，全部页面有文本、无旋转。125 页全部渲染并检查七张联系表，另放大检查物理页 15、26、31、117、125。没有观察到新增截断、重叠或引用排版错误。四处近似页边距标记来自原有嵌入图片的坐标标签，现位于印刷页 36、50、51、94，与前次四处来源相同且没有裁切。

正文叙述 {counts['total_narrative_words']:,} 英文词，含标题/图表题注 {counts['total_non_cell_words']:,} 词；摘要仍为 213 词。页码和逐章计数在 `../CHAPTER_COUNTS.md`。自动检查汇总见 `source-checks.json`、`final-validation.json` 和 `pdf-qa/pdf-preflight.json`。
'''
(out/'REVIEW.md').write_text(text)
print('Review and final validation written.')
