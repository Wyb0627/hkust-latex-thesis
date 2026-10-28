const fs = await import("node:fs/promises");
const task = await taskSpace(3); const page = task.page("p1");
const titles = ["BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models", "Flamingo: a Visual Language Model for Few-Shot Learning", "ViLBERT: Pretraining Task-Agnostic Visiolinguistic Representations for Vision-and-Language Tasks", "InstructBLIP: Towards General-purpose Vision-Language Models with Instruction Tuning", "Natural Questions: A Benchmark for Question Answering Research", "TriviaQA: A Large Scale Distantly Supervised Challenge Dataset for Reading Comprehension", "TAPAS: Weakly Supervised Table Parsing via Pre-training", "TableFormer: Robust Transformer Modeling for Table-Text Encoding"];
const rows=[];
for (const title of titles) {
 await page.goto("https://scholar.google.com/scholar?q="+encodeURIComponent('"'+title+'"'));
 const data=await page.evaluate(()=>({text:document.body.innerText, results:[...document.querySelectorAll("h3")].map(h=>({title:h.innerText, text:h.parentElement.innerText, links:[...h.parentElement.querySelectorAll("a")].map(a=>({text:a.innerText,href:a.href}))}))}));
 rows.push({title,url:await page.url(),...data});
 console.log(JSON.stringify({title,firstResult:data.results[0]?.title,citedBy:data.results[0]?.text.match(/Cited by [0-9,]+/)?.[0],blocked:/unusual traffic|not a robot|recaptcha/i.test(data.text)}));
 if (/unusual traffic|not a robot|recaptcha/i.test(data.text)) break;
}
await fs.writeFile("/Users/ybwang/Library/CloudStorage/OneDrive-HKUSTConnect/paper/thesis/hkust-latex-thesis/planning/reference-expansion-2026-10-28/scholar-round7.json",JSON.stringify(rows,null,2));
