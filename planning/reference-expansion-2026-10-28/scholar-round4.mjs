const fs = await import("node:fs/promises");
const task = await taskSpace(3); const page = task.page("p1");
const titles = ["Neuinfer: Knowledge inference on n-ary facts", "Knowledge graph embedding by translating on hyperplanes", "Convolutional 2d knowledge graph embeddings", "HAHE: Hierarchical Attention for Hyper-Relational Knowledge Graphs in Global and Local Level", "Complex embeddings for simple link prediction", "Inductive representation learning on large graphs", "Can language models solve graph problems in natural language?", "Large language models are zero-shot reasoners"];
const rows=[];
for (const title of titles) {
 await page.goto("https://scholar.google.com/scholar?q="+encodeURIComponent('"'+title+'"'));
 const data=await page.evaluate(()=>({text:document.body.innerText, results:[...document.querySelectorAll("h3")].map(h=>({title:h.innerText, text:h.parentElement.innerText, links:[...h.parentElement.querySelectorAll("a")].map(a=>({text:a.innerText,href:a.href}))}))}));
 rows.push({title,url:await page.url(),...data});
 console.log(JSON.stringify({title,firstResult:data.results[0]?.title,citedBy:data.results[0]?.text.match(/Cited by [0-9,]+/)?.[0],blocked:/unusual traffic|not a robot|recaptcha/i.test(data.text)}));
 if (/unusual traffic|not a robot|recaptcha/i.test(data.text)) break;
}
await fs.writeFile("/Users/ybwang/Library/CloudStorage/OneDrive-HKUSTConnect/paper/thesis/hkust-latex-thesis/planning/reference-expansion-2026-10-28/scholar-round4.json",JSON.stringify(rows,null,2));
