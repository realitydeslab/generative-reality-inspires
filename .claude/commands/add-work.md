---
description: Research one or more models, products, APIs, papers, labs or companies for Generative Immersive Reality Inspire, add their salient generative immersive works (bilingual, classified, each with a video), rebuild the site and catalogs, and publish.
argument-hint: <model, product, lab, company, project URL or paper arXiv/DOI> [, another …] [--no-push]
---

# Add to Generative Immersive Reality Inspire

Input: `$ARGUMENTS` — one or more models, products, APIs, labs / companies, research projects (URL) or papers (arXiv / DOI), comma-separated. `--no-push` = build and preview locally, do not commit or publish.

The gallery surveys generative immersive technology: video generation, virtual humans, speech and spatial audio, interactive world models, 3D / 4D scenes, assets, agents, generative XR, immersive behavioral research and the platforms that deliver them. Generic image generators with no immersive, 3D or temporal angle are OUT.
Read `data/SCHEMA.md`, `data/taxonomy.json` and `data/RESEARCH_BRIEF.md` (stance, inclusion rule, video-finding steps) first.

## Steps

1. **Sync.** `git pull --ff-only`.
2. **Identify.** Resolve each input to a creator (company, lab or first author). `grep -i "<name>" data/creators_index.txt` — if it exists, reuse the id and add only missing works. Several inputs → one subagent each, in parallel, each writing its own file.
3. **Research the salient works**: official announcement, project page, paper, and — required — a **video** that shows it working (official YouTube / X post / project-page mp4; see the brief). Record `date`, `specs`, `timing`, `access`, `inputs` → `modalities` (output), `api_url`, `code_url`, and the status as of today.
   Verify with `python3 tools/check_media.py <url>…`, `--doi <doi>`, `--arxiv <id>`, `--og <page>`. Keep only `"ok": true`; check that a paper id's title is the right paper.
4. **Write** `data/raw/add-<creator-id>.json` (creators with `disciplines` and `name_zh` if any; works with field / sub / modalities / inputs / timing / access / lenses / kind; English + Chinese text; leads). Add `trend-*` collection ids where the work is a clear signal of a trend.
   People or institutions for **Resources & Links**: `data/orgs/add-<creator-id>.json` (see SCHEMA → Resource) with `creator_id`.
   Chinese titles: `data/title_zh/add-<creator-id>.json`.
5. **Validate.** `python3 tools/validate.py data/raw/add-<creator-id>.json` (and `python3 tools/validate_orgs.py --all`) until ✓.
6. **Build.** `python3 tools/build_data.py`. Check `data/dropped.json` (dead media, DOI / arXiv title mismatches) and fix what is yours.
7. **Preview** (optional): `./serve.sh`, open `http://localhost:8937/#view=works&q=<name>`.
8. **Check duplicates**: `python3 tools/audit_titles.py` — resolve any same-title works that are yours.
9. **Publish** (skip with `--no-push`): `tools/publish.sh "feat(data): add <name> (<n> works)"`
   It validates every batch, rebuilds, refuses to publish if validation fails or works disappeared, then commits and pushes.
   GitHub Pages redeploys https://immersive.reality.design in about a minute.
10. **Report**: what was added (counts per field), notable works, what was left out and why, new leads, live URL.
