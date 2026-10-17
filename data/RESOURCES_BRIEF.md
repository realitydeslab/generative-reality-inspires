# Resources & Links brief (for the resources research agent)

The gallery at generative.reality.design has a **Resources & Links** tab: the key PEOPLE of generative immersive technology
(researchers, founders & builders, artists & directors) and the INSTITUTIONS & WEBSITES where the field happens (AI labs &
companies, academic labs, conferences & workshops, journals, newsletters / podcasts / media, communities & directories,
leaderboards & arenas). Working dir: `/Users/amber/Projects/HoloKit/HoloKit2/generative-reality-inspire`. Today is 2026-10-17.

Read first: `data/SCHEMA.md` → section **Resource**, `data/taxonomy.json` → `org_types`, `org_themes`, `fields`,
and `data/RESEARCH_BRIEF.md` → project stance (generative immersion for behavioral science).

## Goal: complete for the key figures, selective beyond them (target 90–130 records)
- People (researchers): the authors behind the landmark models and methods — world models (Jack Parker-Holder, Tim Rocktäschel,
  Ashley Edwards, Jake Bruce — Genie; Dani Valevski — GameNGen; Eloi Alonso — DIAMOND), video (Tim Brooks, Bill Peebles — Sora),
  3D / 4D (Ben Mildenhall, Jon Barron, Bernhard Kerbl, George Drettakis, Angjoo Kanazawa, Jonathon Luiten, Ruiqi Gao, Aleksander Holynski,
  Shubham Tulsiani, Noah Snavely, Gordon Wetzstein, Hao Su, Jiaming Sun? verify), world generation (Fei-Fei Li, Justin Johnson,
  Christoph Lassner), virtual humans (Yaser Sheikh, Michael Black, Hao Li), speech (Neil Zeghidour, Alexandre Défossez),
  agents (Joon Sung Park, Michael Bernstein, Percy Liang, Linxi "Jim" Fan), HCI / XR (Ryo Suzuki, Jaron Lanier, Eric Paulos? verify fit),
  and the behavioral-science side: Mel Slater, Maria V. Sanchez-Vives, Sylvia Xueni Pan, Antonia Hamilton, Jeremy Bailenson,
  Jim Blascovich, Jean-Louis van Gelder, Albert "Skip" Rizzo, Jonathan Gratch, Daniel Freeman, Guido Makransky, Ioannis Patras.
- People (builders): founders who define products (Cristóbal Valenzuela — Runway, Amit Jain — Luma, Hassan Raza — Tavus,
  Joshua Xu — HeyGen, Mati Staniszewski — ElevenLabs, Ethan Hu — Meshy, Dean Leitersdorf — Decart, Oliver Cameron — Odyssey, …).
- People (artists & directors) using generative + immersive media, sparingly and only when salient.
- Institutions: AI labs & companies (one record per relevant unit: "Google DeepMind", "Meta Reality Labs Research", "NVIDIA Research
  — Toronto AI Lab"…, plus Chinese labs: Tencent Hunyuan, ByteDance Seed, Kuaishou Kling, Alibaba Tongyi Wan, Shanghai AI Lab),
  academic labs (UCL VECG / Slater, Event Lab Barcelona, Stanford VHIL, USC ICT, Max Planck Institute for the Study of Crime NSCR?
  verify Van Gelder's institute, Inria GraphDeco, Berkeley KAIR / Kanazawa, Stanford SVL, CMU, MIT Media Lab, Calgary Suzuki lab…),
  conferences (SIGGRAPH, CVPR, ICCV, ECCV, NeurIPS, ICLR, CHI, UIST, IEEE VR, ISMAR, AAMAS / IVA), journals (Presence, Computers
  in Human Behavior, Frontiers in Virtual Reality, IEEE TVCG, ACM TOG), media (newsletters, podcasts, YouTube channels that track
  the field, e.g. Two Minute Papers, Radiance Fields, Bilawal Sidhu, 80.lv; check), communities & directories (awesome lists:
  awesome-3D-gaussian-splatting, awesome-world-models, Hugging Face spaces), leaderboards (Artificial Analysis Video Arena,
  VBench, WorldScore, 3D Arena, LMArena video).
- One record per person / institution. `url` must load (`python3 tools/check_media.py --og <url>` also returns image candidates).
  People: personal / lab page; else Google Scholar or Wikipedia; add up to 4 `links`.
- Bilingual `description` / `description_zh` (1–2 concrete sentences). `name_zh` for people and institutions with a Chinese name.
  `known_for`: 2–4 key works for people.
- `creator_id`: if the person / org exists as a creator in the works data (`grep -ril "<name>" data/raw/`), put its id. Works agents
  run in parallel: do a final grep pass right before you finish. Canonical creator ids are listed in `plan/AGENTS.md`.

## Output
- Your file only: `data/orgs/resources.json` (`{"batch": "resources", "orgs": [...]}`); split into `resources-2.json` if large.
- Ids: people `person--<kebab-name>`, institutions `<kebab-name>`.
- Validate: `python3 tools/validate_orgs.py data/orgs/<file>.json` until ✓.
- Search: WebSearch is capped for ALL agents together — use at most 12 calls. Prefer WebFetch, curl, Wikipedia API, lab pages,
  conference sites; sparingly `curl -s -A "Mozilla/5.0" "https://html.duckduckgo.com/html/?q=<query>"`.
- Never put the user's email (or any personal email) in an API request — no `mailto=`.
- No Chrome browser tools. Scratch: `temp/resources/`.

## Report back (short)
File(s), number of records by type and theme, notable gaps, leads.
