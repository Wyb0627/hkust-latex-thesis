const fs = await import("node:fs/promises");
const task = await taskSpace(3); const page = task.page("p1");
const titles = ["Matching Networks for One Shot Learning", "Learning to Compare: Relation Network for Few-Shot Learning", "ColBERT: Efficient and Effective Passage Search via Contextualized Late Interaction over BERT", "Precise Zero-Shot Dense Retrieval without Relevance Labels", "FlashAttention: Fast and Memory-Efficient Exact Attention with IO-Awareness", "Scissorhands: Exploiting the Persistence of Importance Hypothesis for LLM KV Cache Compression at Test Time", "VQA: Visual Question Answering", "BLIP: Bootstrapping Language-Image Pre-training for Unified Vision-Language Understanding and Generation"];
const rows=[];
for (const title of titles) {
 await page.goto("https://scholar.google.com/scholar?q="+encodeURIComponent('"'+title+'"'));
 const data=await page.evaluate(()=>({text:document.body.innerText, results:[...document.querySelectorAll("h3")].map(h=>({title:h.innerText, text:h.parentElement.innerText, links:[...h.parentElement.querySelectorAll("a")].map(a=>({text:a.innerText,href:a.href}))}))}));
 rows.push({title,url:await page.url(),...data});
 console.log(JSON.stringify({title,firstResult:data.results[0]?.title,citedBy:data.results[0]?.text.match(/Cited by [0-9,]+/)?.[0],blocked:/unusual traffic|not a robot|recaptcha/i.test(data.text)}));
 if (/unusual traffic|not a robot|recaptcha/i.test(data.text)) break;
}
await fs.writeFile("/Users/ybwang/Library/CloudStorage/OneDrive-HKUSTConnect/paper/thesis/hkust-latex-thesis/planning/reference-expansion-2026-10-28/scholar-round6.json",JSON.stringify(rows,null,2));
