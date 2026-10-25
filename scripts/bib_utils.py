"""Small brace-aware reader for this project's ordinary BibTeX entries."""
import re,unicodedata

def end_value(s,i):
 if s[i]=='{':
  level=1;j=i+1
  while j<len(s) and level:
   if s[j]=='{' and s[j-1]!='\\':level+=1
   if s[j]=='}' and s[j-1]!='\\':level-=1
   j+=1
  return s[i+1:j-1],j
 if s[i]=='"':
  j=i+1
  while j<len(s) and not(s[j]=='"' and s[j-1]!='\\'):j+=1
  return s[i+1:j],j+1
 m=re.match(r'[^,\n}]+',s[i:]);return m[0].strip(),i+len(m[0])

def parse(s):
 entries=[]
 for m in re.finditer(r'@(\w+)\s*\{\s*([^,\s]+)\s*,',s):
  typ,key=m[1].lower(),m[2]; i=m.end(); fields={}
  while i<len(s):
   while i<len(s) and s[i] in ' \t\n\r,':i+=1
   if i>=len(s) or s[i]=='}':break
   f=re.match(r'(\w+)\s*=\s*',s[i:])
   if not f:raise ValueError((key,s[i:i+80]))
   i+=f.end();v,i=end_value(s,i);fields[f[1].lower()]=v
  entries.append({'type':typ,'key':key,'fields':fields})
 return entries

def dump(e):
 return '@'+e['type']+'{'+e['key']+',\n'+''.join('  '+k+'={'+v+'},\n' for k,v in e['fields'].items())+'}\n'

def norm(s):
 s=unicodedata.normalize('NFKD',s).lower()
 return ''.join(c for c in s if c.isalnum())
