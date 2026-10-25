"""Produce readable source extracts without changing research files; not a TeX interpreter."""
import json,re,hashlib
from pathlib import Path
roots=json.loads(Path('planning/source_roots.json').read_text())
for name,entry in roots.items():
    seen=set(); chunks=[]
    def visit(p):
        p=p.resolve()
        if p in seen:return
        seen.add(p)
        raw=p.read_text()
        s=re.sub(r'\\begin\{comment\}.*?\\end\{comment\}','',raw,flags=re.S)
        lines=[]
        for n,line in enumerate(s.splitlines(),1):
            line=re.sub(r'(?<!\\)%.*','',line).strip()
            if line: lines.append(line)
        text='\n'.join(lines)
        chunks.append(f'\n===== {p} SHA256 {hashlib.sha256(raw.encode()).hexdigest()} =====\n'+text)
        for inc in re.findall(r'\\(?:input|include)\{([^}]+)\}',text):
            q=Path(entry).parent/inc
            if not q.suffix:q=q.with_suffix('.tex')
            if q.exists():visit(q)
    visit(Path(entry))
    Path(f'planning/extracted/{name.lower()}-active.tex.txt').write_text('\n'.join(chunks))
    print(name,len(seen),'files',sum(len(c.split()) for c in chunks),'whitespace tokens')
