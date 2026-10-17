# Research brief (for every research agent)

Project: **Generative Reality Inspire** — a bilingual (English / Simplified Chinese) gallery at
generative.reality.design that surveys **generative immersive technology**: the models, products, APIs, research demos,
studies and devices with which situations can be *generated* and *entered*. Made by Reality Design Lab as idea material
for researchers, designers and students, and as the living survey behind a research agenda on **generative immersion for
behavioral science** (how generated, adaptive situations could be used to study and train human behavior).
Today is **2026-10-17**. Working dir: `/Users/amber/Projects/HoloKit/HoloKit2/generative-reality-inspire`.

Read first: `data/SCHEMA.md` (JSON format, language rule), `data/taxonomy.json` (fields / subs / outputs (`modalities`) /
inputs / timings / access / lenses / kinds / collections / disciplines) and `plan/AGENTS.md` (which batch owns what, canonical creator ids).

## The stance (from the agenda)
A *generative immersive world* is an interactive environment in which generative models create or revise behaviorally
relevant aspects of a situation, people encounter it through immersive interfaces (screen, headset VR, AR/MR), and their
actions have consequences within a coherent, evolving context. Three complementary technical routes lead there:
1. **video generation** (synthesising audiovisual events; watched, not acted in),
2. **dynamic 3D / 4D representations** (Gaussian splatting, 4D reconstruction and generation; navigable, but not by itself interactive),
3. **action-conditioned world models** (Genie-like; respond to actions in real time, with limited persistence and control),
plus the layers that make a situation social and responsive: **virtual humans** (full-duplex audio-visual conversation),
**speech and sound**, **agents**, **3D assets**, **generative XR** applications, and the **behavioral research and training
traditions** that use immersive situations (VR Milgram, bystander studies, virtual burglary, virtual patients, presence theory).
Distinguish developer-reported capabilities from demonstrated, independently tested ones. Do not inflate: a 60-second
browser demo is not a deployed VR research platform.

The site's facets mirror the agenda's framework:
- **Output** (`modalities`) × **Input** (`inputs`): e.g. text → flat video; speech + face video → speech + avatar (audio-visual × audio-visual).
- **Timing** (`timing`): pre-generated / turn-based / real-time / full-duplex / scripted.
- **Capability lenses** (`lenses`): situational reach, perceptual realism, behavioral plausibility, temporal responsiveness,
  reactivity, adaptation, situation diversity, authoring accessibility, co-creation & agency, persistence, experimental control.
- **Access** (`access`): open weights, public API, product, waitlist / preview, research only — "can a lab actually use it, and pin a version?"

## Inclusion rule
- IN: models, products, APIs, open-source tools, research demos, datasets / benchmarks and devices that **generate or
  reconstruct immersive situations or their parts** (video, worlds, 3D / 4D scenes, assets, avatars, voices, sound, agents),
  and the **experiences and studies** that put them (or their non-generative predecessors) in front of people.
- Salience over volume: milestone releases (first of a kind, state of the art when released, widely used, open-weight
  landmark, best-paper, top of a public arena) and the 2025–2026 frontier. For each major lab: its milestone versions as
  separate works when each had its own launch and video (e.g. Genie, Genie 2, Genie 3, Project Genie), not every point release.
- Historical precursors are welcome when they anchor a lineage (NeRF 2020, GameNGen 2024, Make-A-Video 2022, Wav2Lip 2020),
  but the weight is on 2023–2026.
- OUT: generic image generators with no immersive / 3D / temporal angle; marketing wrappers around someone else's model;
  benchmarks nobody uses; rumours. If a product is announced but unreleased, include it only with an official source and say
  so ("announced, waitlist only as of October 2026").
- Global coverage: Chinese labs (Kuaishou Kling, ByteDance Seed, Tencent Hunyuan, Alibaba Wan, MiniMax, Shengshu Vidu,
  Skywork, StepFun, Zhipu, SenseTime…) are central to this field — include them, with their Chinese names in `name_zh`.

## Every work
- Bilingual text; correct classification (`field`, `sub`, `modalities` 1–3, `inputs` 0–3, `timing`, `access` 1–3,
  `lenses` 1–3, `kind`); `year` and, for 2023+, `date` (announcement date, ISO).
- **A video is the default, not a bonus.** The gallery must show each technology working. Find, in this order:
  1. the official launch / demo video on the creator's YouTube channel (or Vimeo),
  2. the official launch post on X with a video (`https://x.com/<account>/status/<id>`; check_media confirms it has video),
  3. a direct `.mp4` / `.webm` from the official project page or CDN (github.io project pages, storage.googleapis.com,
     cdn.openai.com, website-files CDNs…). Look in the raw HTML: `curl -sL -A "Mozilla/5.0" <page> | grep -oE 'https?://[^"'"'"' ]+\.(mp4|webm)[^"'"'"' ]*' | sort -u`,
  4. a conference talk / paper video (SIGGRAPH, CVPR, CHI YouTube channels) or a reputable third-party demo (last resort; note it in `keywords`: "third-party video").
  YouTube search without the API: `curl -sL -A "Mozilla/5.0" "https://www.youtube.com/results?search_query=<q>" | grep -oE '"videoId":"[^"]{11}"' | sort -u | head`
  then confirm title + channel with `python3 tools/check_media.py https://www.youtube.com/watch?v=<id>` (it prints title and author).
  The video must show THIS work (check the title / author). Each video may be used by only one work.
- **images**: 1–2 (og:image of the official page, a hero image, or an arXiv project-page teaser). YouTube thumbnails are added automatically.
- **paper**: arXiv id (`paper.arxiv`) or DOI, with venue and the paper's own title. Technical reports count.
- `source_url` (official announcement or project page), `api_url` (developer docs, when an API exists), `code_url` (repo / Hugging Face for open models).
- `specs`: the headline numbers when published (resolution, fps, clip length, latency, parameters, consistency horizon).
- Verify every link with `python3 tools/check_media.py` before writing it: videos and images (`<url>`), DOIs (`--doi`),
  arXiv ids (`--arxiv`). Keep only `"ok": true`. Check that a DOI's / arXiv id's returned title really is the work.
- `collections`: add a `trend-*` id when the work is a clear signal of that trend (see taxonomy → collections, type trend);
  add a venue id (`siggraph`, `cvpr`, `iccv-eccv`, `ml-conf`, `chi`, `uist`, `ieee-vr`) when the paper appeared there;
  add `agenda-core` for the works listed below.

## agenda-core (works the research agenda cites — the owning batch must add each one with `"collections": ["agenda-core", …]`)
behavioral: Blascovich et al. 2002 *Immersive virtual environment technology as a methodological tool for social psychology*
(Psychological Inquiry 13(2)); Pan & Hamilton 2018 (doi 10.1111/bjop.12290); Slater 2009 place illusion & plausibility
(doi 10.1098/rstb.2009.0138); Yee & Bailenson 2007 Proteus effect (doi 10.1111/j.1468-2958.2007.00299.x); Hamstra et al. 2014
fidelity in simulation (doi 10.1097/ACM.0000000000000130); Kenny et al. 2007 *Building Interactive Virtual Humans for Training
Environments* (I/ITSEC); Ning et al. 2026 GenAI meets XR systematic review (doi 10.1080/10447318.2025.2565392, arXiv 2511.03282);
Brunswik 1955 representative design (doi 10.1037/h0047470); Steuer 1992 (doi 10.1111/j.1460-2466.1992.tb00812.x); Slater et al.
2006 virtual Milgram (doi 10.1371/journal.pone.0000039); van Gelder et al. 2017 virtual burglary (doi 10.1177/0022427816663997);
van Gelder 2023 VR for criminologists (doi 10.1086/726691); Slater et al. 2013 bystander (doi 10.1371/journal.pone.0052766);
Slater & Sanchez-Vives 2016 (doi 10.3389/frobt.2016.00074); Ericsson et al. 1993 deliberate practice (doi 10.1037/0033-295X.100.3.363);
Makransky & Petersen 2021 CAMIL (doi 10.1007/s10648-020-09586-2); DeVault et al. 2014 SimSensei Kiosk (AAMAS);
CLiVR 2025 (arXiv 2510.19031); Barker et al. 2026 VR + LLM team training in the operating room (arXiv 2601.13406).
video: Veo 3.1 (Google DeepMind).
spatial-4d: 3D Gaussian Splatting (Kerbl et al. 2023, doi 10.1145/3592433); 4D Gaussian Splatting (Wu et al. CVPR 2024);
DreamGaussian4D (arXiv 2312.17142); CAT4D (CVPR 2025); BulletGen (arXiv 2506.18601).
world-models: Genie (Bruce et al. ICML 2024); Genie 2 (2024-12-04); Genie 3 (2025-08-05); Project Genie (Google Labs) and its
Street View grounding (2026-05-19).
genxr: Social Conjuring (arXiv 2410.00274); CinemaWorld (Ihara et al. 2026, arXiv 2603.08060); Editing Reality: in-situ
co-creation with generative AI in MR (Weng et al. DIS '26, doi 10.1145/3800645.3813087); Generative Enactments (Hu 2026) — add
only if a public version (arXiv / DOI / project page) exists, otherwise list as a lead.

## Writing
- `description`: 1–2 concrete sentences: what it is and what a person sees / does / gets.
- `idea_en`: the one-line takeaway for someone building generated situations (e.g. "Turns a single photo into a world you can walk
  for a minute, but the world forgets what it showed you once it is out of view").
- `method`: architecture / pipeline / study design in one sentence.
- State status as of October 2026 when it matters (open weights, API, waitlist, discontinued).
- Chinese natural, not word-for-word. Established terms: 世界模型, 高斯泼溅 (Gaussian splatting), 神经辐射场 (NeRF), 全双工,
  文生视频, 图生视频, 数字人 / 虚拟人, 体积视频, 临场感 (presence), 具身 (embodiment), 智能体 (agent).
- Plain, precise language. No hype ("groundbreaking", "revolutionary", "stunning", "game-changing", "unprecedented").
  Developer claims are reported as claims ("DeepMind reports…").

## Output
- One file `data/raw/<your-batch>.json` (`"batch": "<your-batch>"`), creators + works + leads; split into `<your-batch>-2.json` if > ~60 works.
- Chinese titles: `data/title_zh/<your-batch>.json` (only where a Chinese title adds something: official Chinese names, translated paper titles).
- Creators get `disciplines` (1–2) and `name_zh` when they have one. Use the canonical ids in `plan/AGENTS.md`; before creating
  any other creator, `grep -ril "<name>" data/raw/` — parallel agents write too; reuse ids. Ids: kebab-case ASCII.
  Work id: `<first-creator-id>--<short-slug>`.
- Run `python3 tools/validate.py data/raw/<file>.json` until it prints ✓.
- `leads`: works you found but did not add (for the next round), with a link.

## Search
- **WebSearch is capped at about 200 calls for ALL agents together: use at most 14.** Prefer direct sources:
  official blogs / newsrooms, `curl` of project pages, arXiv API (`curl -s "https://export.arxiv.org/api/query?search_query=all:%22world%20model%22&sortBy=submittedDate&max_results=50"`),
  Hugging Face API (`curl -s "https://huggingface.co/api/models?search=<q>&sort=downloads&limit=20"`), GitHub search API
  (`curl -s "https://api.github.com/search/repositories?q=<q>&sort=stars"`), YouTube search scrape (above), WebFetch, and
  sparingly `curl -s -A "Mozilla/5.0" "https://html.duckduckgo.com/html/?q=<query>"`.
- For "what was released recently" questions, a Perplexity call through OpenRouter is allowed (max 6 per agent):
  `curl -s https://openrouter.ai/api/v1/chat/completions -H "Authorization: Bearer $OPENROUTER_API_KEY" -H "Content-Type: application/json" -d '{"model":"perplexity/sonar","messages":[{"role":"user","content":"<question>"}]}'`
  Treat its answers as leads; verify every fact on an official page.
- Never put the user's email (or any personal email) in an API request — no `mailto=` for Crossref / OpenAlex; accept rate limits.
- Do NOT use the Chrome browser tools. Scratch files: `temp/<your-batch>/` only.
- Do NOT touch files outside `data/raw/<your-batch>*.json`, `data/title_zh/<your-batch>.json` and `temp/<your-batch>/`.

## Report back (short)
File(s) written; number of creators and works by sub-category and kind; how many have video / images / paper; works without
video and why; notable 2026 developments you found; top leads.
