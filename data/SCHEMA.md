# Data schema — Generative Immersive Reality Inspire

Each research batch writes one file: `data/raw/<batch>.json`

```json
{
  "batch": "world-models",
  "creators": [ Creator, ... ],
  "works":    [ Work, ... ],
  "leads":    [ Lead, ... ]
}
```

## Creator (a company, a lab, a studio or a person)
```json
{
  "id": "google-deepmind",                   // kebab-case, unique across all batches
  "name": "Google DeepMind",
  "name_zh": "",                             // optional: Chinese name if it has one (腾讯混元, 快手可灵, 字节跳动 Seed …)
  "kind": "lab",                             // person | lab | studio | company
  "role": "AI research lab of Google",
  "based": "London, UK",
  "bio": "1-2 sentences, English.",
  "why": "Why it matters for generative immersion (1 sentence).",
  "disciplines": ["ml"],                     // 1–2 of taxonomy.disciplines
  "links": { "site": "", "scholar": "", "x": "", "youtube": "", "github": "", "huggingface": "" },
  "role_zh": "…", "bio_zh": "…", "why_zh": "…", "based_zh": "英国伦敦",   // REQUIRED Chinese versions
  "connected_to": ["google"],                // other creator ids (parent company, collaborators, spin-offs)
  "discovered_via": "seed"                   // creator id that led to this one, or "seed"
}
```
Companies and labs are the usual creators of models and products (`openai`, `google-deepmind`, `runway`, `tencent-hunyuan`).
Papers are credited to their first author (a person), with the lab as second creator when it matters.

## Work (one model, product, platform, research demo, study, experience, device, dataset or paper)
```json
{
  "id": "google-deepmind--genie-3",          // <first-creator-id>--<slug>, unique
  "creator_ids": ["google-deepmind"],
  "title": "Genie 3",                        // original name
  "year": 2025,                              // year of first public announcement / release / publication
  "date": "2025-08-05",                      // optional but wanted for 2023+: ISO date (YYYY-MM-DD or YYYY-MM) of the announcement
  "field": "world-models",                   // primary field id (data/taxonomy.json → fields)
  "sub": "general",                          // one sub-category id of that field
  "also": ["agents"],                        // optional: other fields it clearly belongs to
  "modalities": ["frame-stream"],            // OUTPUT: 1-3 from taxonomy.modalities — what the system generates
  "inputs": ["text", "action"],              // INPUT: 0-3 from taxonomy.inputs — what drives it
  "timing": "real-time",                     // ONE of taxonomy.timings: offline | turn-based | real-time | full-duplex | scripted
  "access": ["preview"],                     // 1-3 of taxonomy.access: open | api | product | preview | research
  "lenses": ["reactivity", "persistence"],   // 1-3 from taxonomy.lenses: the capability dimensions it most advances or exposes
  "kind": "model",                           // model | product | platform | open-source | research | study | experience | device | dataset | paper
  "description": "1-2 sentences, English: what it is and what happens.",
  "description_zh": "中文描述（自然流畅，不逐字翻译）",
  "idea_en": "One line: what it changes for generative immersive situations (or what it reveals).",
  "idea_zh": "一句话中文：核心想法",
  "method": "One English sentence: how it works (architecture, training data, pipeline, study design). Mark guesses with 'likely'.",
  "method_zh": "中文：它是怎么做到的。",
  "specs": "720p · 24 fps · consistent for a few minutes",   // optional: language-neutral numbers (resolution, fps, latency, duration, size)
  "keywords": ["world model", "action-conditioned", "autoregressive"],

  "video":  { "url": "https://www.youtube.com/watch?v=…" },  // STRONGLY WANTED: YouTube | Vimeo | X post | direct .mp4/.webm
  "images": ["https://…/hero.jpg"],                         // optional: 1-4 direct image URLs (jpg/png/webp/gif)
  "paper":  { "url": "https://arxiv.org/abs/…", "doi": "", "arxiv": "2408.00000", "venue": "ICML 2024", "title": "…" },
            // optional; title = the paper's own title; REQUIRED when kind = paper
  "source_url": "https://…",                                // official announcement / project page (strongly recommended)
  "api_url": "",                                            // optional: API / developer docs page
  "code_url": "",                                           // optional: repository (GitHub / Hugging Face)
  "collections": ["trend-world-simulators", "ml-conf"],     // optional: collection ids from data/taxonomy.json
  "exhibited": ["CVPR 2025 Best Paper"]                     // optional: awards / key showings (free text) — only if verified
}
```

Rules:
- Every work needs **at least one** of `video`, `images`, `paper`. This gallery exists to SHOW the technology:
  every model, product, demo and experience should have a **video** (official launch / demo video, or the project page's mp4).
  Paper-only is acceptable only for theory papers, reviews and older studies with no recorded footage.
- `paper.doi` is checked against Crossref and `paper.arxiv` against arXiv at build time: use the real id, never a guess.
- Images: direct URLs to image files (`og:image` of the project page is usually best). Must return `image/*`.
- Videos: prefer the creator's own upload (official YouTube channel, official X account, project-page mp4).
- `timing` describes the generation as experienced: a video model is `offline`; a chatbot avatar replying after you finish
  speaking is `turn-based`; Genie 3 is `real-time`; a model that talks while listening and handles interruption is `full-duplex`;
  a classic hand-authored VR experiment is `scripted`.

Verify media before writing (all must print `"ok": true`):
```
python3 tools/check_media.py <video-or-image-url> ...
python3 tools/check_media.py --doi 10.1145/3592433
python3 tools/check_media.py --arxiv 2408.14837
python3 tools/check_media.py --og <project-page-url>      # lists og:image / twitter:image / large <img> candidates
```

## Collections
A collection is a named set of works. Defined in `data/taxonomy.json` → `collections` (`id, type, en, zh, desc_en, desc_zh, url`).
`type`: `trend` | `survey` | `venue` | `exhibition` | `award` | `archive`.
- `trend-*` collections are the **Trends** tab: tag a work with a trend id when it is a clear signal of that trend.
- `agenda-core`: the works cited by the generative-immersion research agenda (list in `data/RESEARCH_BRIEF.md`).
- venues: `siggraph`, `cvpr`, `iccv-eccv`, `ml-conf`, `chi`, `uist`, `ieee-vr` — the work's paper was published there.
A work joins by listing the id in its `collections`, or by adding its id to `data/collections/<collection-id>.json` (a JSON list).

## Chinese titles (`data/title_zh/<name>.json`)
`{ "<work-id>": {"zh": "可灵", "src": "original|established|translated|keep"} }` — shown as the main title in the Chinese
interface. Model and product names are usually kept (`Genie 3`, `Sora 2`, `Marble`); use the official Chinese name when it exists
(可灵 Kling, 海螺 Hailuo, 混元 Hunyuan, 即梦 Dreamina, 通义万相 Wan); translate descriptive paper titles.

## Extra media (`data/media/<name>.json`)
`{ "<work-id>": { "images": ["https://…"], "video": { "url": "https://…" } } }` — images are appended (max 4), a video is used only when the work has none.

## Resource (`data/orgs/<batch>.json` → `{ "batch": "...", "orgs": [ Resource, ... ] }`)
The **Resources & Links** tab lists key PEOPLE (researchers, founders & builders, artists) and INSTITUTIONS & WEBSITES
(AI labs & companies, academic labs, conferences, journals, newsletters & media, communities, leaderboards).
`type` is one of `taxonomy.org_types` (the 6th column says `person` or `org`).
```json
{
  "id": "person--mel-slater",                         // kebab-case, unique across data/orgs; people: "person--<name>"
  "name": "Mel Slater",
  "name_zh": "",
  "type": "researcher",                              // researcher | builder | artist | ai-lab | academic-lab | conference | journal | media | community | leaderboard
  "themes": ["presence", "behavioral-research"],     // 1–4 of taxonomy.org_themes
  "fields": ["behavioral"],                          // 0–3 related gallery fields
  "description": "1–2 sentences, English: who they are / what it does, and why it matters here.",
  "description_zh": "中文：是谁 / 做什么，为什么重要。",
  "known_for": ["Place illusion and plausibility (2009)", "A Virtual Reprise of the Milgram Experiments (2006)"],
  "url": "https://…",                                // REQUIRED, must load
  "links": [ { "label": "Google Scholar", "url": "https://scholar.google.com/…" } ],
  "image": "https://…/og.jpg",                       // optional (check_media ok)
  "based": "Barcelona, ES", "based_zh": "西班牙巴塞罗那",
  "born": 1950, "founded": 2010,                     // optional integers
  "people": [],                                      // institutions: optional key people
  "creator_id": "mel-slater",                        // optional: matching creator id in the works data
  "found_via": "https://…"
}
```
Validate with `python3 tools/validate_orgs.py data/orgs/<file>.json` (or `--all`).

## Lead (found but not added in this batch)
```json
{ "name": "…", "why": "…", "link": "…", "found_via": "creator id", "status": "open" }   // open | no_media | off_topic | duplicate
```

## Language rule
Every user-facing text exists in BOTH languages, never mixed inside one field (proper nouns — model, product, company,
people names — stay in the original).
English fields: description, idea_en, method, role, bio, why, based. Chinese fields: description_zh, idea_zh, method_zh, role_zh, bio_zh, why_zh, based_zh.
`specs` is language-neutral (numbers and units).
Run `python3 tools/validate.py data/raw/<file>.json` before building.
