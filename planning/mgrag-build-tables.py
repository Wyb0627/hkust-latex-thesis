from pathlib import Path
import re,json
s=Path('planning/extracted/mgrag-active.tex.txt').read_text()
blocks={re.search(r'\\label\{([^}]+)\}',m[0]).group(1):m[0] for m in re.finditer(r'\\begin\{table\}.*?\\end\{table\}',s,re.S)}
root=Path('chapter/tables'); root.mkdir(exist_ok=True)
clean=lambda x:x.strip().replace(r'\uline',r'\underline')
def body(key):
 b=blocks[key]; b=b.split(r'\begin{tabular}',1)[1].split('\n',1)[1].split(r'\end{tabular}',1)[0]
 return b

def write_long(name,cols,caption,header,rows):
 if name=='matching':
  rows=re.sub(r'\\(?:textbf|underline)\{([^{}]*)\}',lambda m:m[1] if re.fullmatch(r'[\d.,/\s+\-]+',m[1]) else m[0],rows)
  caption=caption.replace('Original decimal precision and highlighting are preserved.','')
 # Compact tables remain on one page; longer evidence matrices retain longtable pagination.
 if name in {'datasets','inverse'}:
  text = r'\begin{table}[!htbp]'+'\n'+r'\centering\small'+'\n'+r'\setlength{\tabcolsep}{3pt}'+'\n'+r'\caption{'+caption+'}'+r'\label{tab:mgrag:'+name+'}'+'\n'+r'\begin{tabular}{'+cols+'}\n'+r'\toprule'+'\n'+header+r'\\'+'\n'+r'\midrule'+'\n'+rows+'\n'+r'\bottomrule'+'\n'+r'\end{tabular}'+'\n'+r'\end{table}'+'\n'
  (root/('mgrag-'+name+'.tex')).write_text(text)
  return
 text = r'\begin{longtable}{'+cols+'}\n'+r'\caption{'+caption+'}'+r'\label{tab:mgrag:'+name+'}'+r'\\'+'\n'+r'\toprule'+'\n'+header+r'\\'+'\n'+r'\midrule\endfirsthead'+'\n'+r'\multicolumn{'+str(len(cols.replace('|','')))+r'}{c}{\tablename\ \thetable\ (continued)}\\'+'\n'+r'\toprule'+'\n'+header+r'\\'+'\n'+r'\midrule\endhead'+'\n'+r'\bottomrule\endfoot'+'\n'+rows+'\n'+r'\end{longtable}'+'\n'
 (root/('mgrag-'+name+'.tex')).write_text('{\\small\n\\setlength{\\tabcolsep}{3pt}\n'+text+'}\n')

# Dataset table, all rows copied exactly except typographic dash.
b=body('tab:dataset_statistic'); b=b.split(r'\midrule',1)[1].split(r'\bottomrule',1)[0].strip().replace('1-2','1--2').replace('2-5','2--5').replace('2-4','2--4').replace('1-6','1--6').replace('3-4','3--4').replace('2-6','2--6').replace('2-3','2--3')
write_long('datasets','lccccccc','Evaluation datasets, reproduced from published Table 3, p.~2488~\\cite{mgrag-paper}. T and I denote textual and image query modalities. The columns comprise MMQA and six MRAMG subsets.','Statistic & MMQA & Wiki & Wit & Recipe & Arxiv & Manual & Web',b)

b=body('tab:main_exp'); b=b.split(r'\midrule',1)[1].split(r'\bottomrule',1)[0]
# Expand original dataset multirows into explicit entries for safe pagination.
current=''; rows=[]; parsed_main=[]
for line in b.splitlines():
 if '&' not in line:continue
 line=clean(line)
 m=re.match(r'\\multirow\{4\}\{\*\}\{([^}]+)\}',line)
 if m:current=m.group(1);line=line[m.end():]
 elif line.startswith('&'):line=line[1:];line=' & '+line # keep delimiter to dataset below
 cells=[x.strip() for x in line.replace('\\\\','').split('&')]
 if m: cells=cells[1:]
 elif cells[0]=='':cells=cells[1:]
 rows.append(current+' & '+' & '.join(cells)+r' \\')
 parsed_main.append([current]+cells)
write_long('main','llrrrrrr','Answer quality with Qwen2.5-VL-7B-Instruct, reproduced from published Table 4, p.~2489~\\cite{mgrag-paper}. Vanilla., R1., Graph., Light., and Hippo. denote VanillaRAG, R1-Searcher, GraphRAG, LightRAG, and HippoRAG2. A dash means that the experiment exceeded three days; it is not a zero score. Bold and underlining retain the publication\'s highlighting.','Dataset & Metric & Vanilla. & R1. & Graph. & Light. & Hippo. & MGRAG','\n'.join(rows))

for key,name,cols,header,caption in [
 ('tab:efficiency_MGRAG','breakdown','lrrrrr','Dataset & Queries & KGC & Match & QA & E2E','Module costs reproduced from published Table 5, p.~2489~\\cite{mgrag-paper}. Time is in minutes. KGC, QA, and E2E cells retain the published time/token pairs for graph construction, answering, and end-to-end processing. Match denotes matching time. Token counts and E2E totals are preserved as reported.'),
 ('tab:system_comp','cache','lrrrrrr','System & SIM. & ACC. & ROG. & BLEU & TTFT & Time','Cache-system comparison on MMQA, reproduced from published Table 6, p.~2489~\\cite{mgrag-paper}. V. and H. identify VanillaRAG and HippoRAG2 retrieval pipelines. TTFT is in seconds and total time is in hours.'),
 ('tab:abl_exp','ablation','lrrrrr','Model & SIM. & ACC. & ROG. & BLEU & Time','MMQA component ablations, reproduced from published Table 9, p.~2490~\\cite{mgrag-paper}. Time is in hours.'),
 ('tab:inv_abl','inverse','lrrrrr','Model & SIM. & ACC. & ROG. & BLEU & Time','MMQA inverse ablations, reproduced from published Table 10, p.~2491~\\cite{mgrag-paper}. PSGM and GKV denote path-based semantic graph matching and graph-aware KV recomputation. Time is in hours.')]:
 b=body(key)
 b=re.split(r'\\(?:midrule|hline)',b,maxsplit=1)[1].split(r'\bottomrule',1)[0]
 b=clean(b).replace('\\hline','\\midrule')
 if name=='ablation': b=b.replace('MGRAG w.o. GM','Without graph matching').replace('MGRAG w. MM Encoder','With CLIP encoder').replace('Vanilla MGRAG w. k=5','Vanilla MGRAG, $k=5$')
 write_long(name,cols,caption,header,b)

# Transpose every Table 7 method cell into rows so values remain legible.
b=body('tab:gm_experiment').split(r'\midrule',1)[1].split(r'\bottomrule',1)[0]
methods=['O.IE','STAT','VF2','ISMAGS','SM','VJ','RRWM','IPFP','BGE','SLOT','FGW','MGRAG']
datasets={};current=''
for line in b.splitlines():
 if '&' not in line:continue
 line=clean(line)
 m=re.match(r'\\multirow\{4\}\{\*\}\{([^}]+)\}',line)
 if m:current=m.group(1);line=line[m.end():]
 cells=[x.strip() for x in line.replace('\\\\','').split('&')][1:]
 datasets.setdefault(current,[]).append(cells)
rows=[]; parsed_match=[]
for ds,metrics in datasets.items():
 assert len(metrics)==4,(ds,len(metrics))
 for j,method in enumerate(methods):
  vals=[m[j+1] for m in metrics]
  rows.append(ds+' & '+method+' & '+' & '.join(vals)+r' \\')
  parsed_match.append([ds,method]+vals)
 rows.append(r'\midrule')
write_long('matching','llrrrr','Graph-construction and graph-matching substitutions, transposed from published Table 7, p.~2490~\\cite{mgrag-paper}. All twelve method columns and all four metric values per dataset are retained. O.IE and STAT replace graph construction; the other alternatives replace matching. The shared backbone is Qwen2.5-VL-7B-Instruct. Original decimal precision and highlighting are preserved.','Dataset & Method & SIM. & ACC. & ROG. & BLEU','\n'.join(rows))
# Hop table split method groups vertically, retaining 6 original rows and all 8 outputs.
b=body('tab:hop_performance')
b=re.split(r'\\hline',b,maxsplit=1)[1].split(r'\bottomrule',1)[0]
rows=[]
for line in b.splitlines():
 if '&' not in line:continue
 cs=[clean(x) for x in line.replace('\\\\','').split('&')]
 assert len(cs)==10,cs
 rows += [cs[0]+' & '+cs[1]+' & VanillaRAG & '+' & '.join(cs[2:6])+r' \\',cs[0]+' & '+cs[1]+' & MGRAG & '+' & '.join(cs[6:])+r' \\']
write_long('hops','lrlrrrr','Results by query hop count, reorganized from published Table 8, p.~2490~\\cite{mgrag-paper}. Time is in minutes, as reported. Each original row is shown as two method rows, with the query count repeated.','Hops & Queries & Method & Time & ACC. & ROG. & BLEU','\n'.join(rows))
Path('planning/mgrag-table-cells.json').write_text(json.dumps({'main':parsed_main,'matching':parsed_match},indent=2)+'\n')
print('main',len(parsed_main),'matching',len(parsed_match))
