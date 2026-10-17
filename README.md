# Generative Immersive Reality Inspire

**https://immersive.reality.design**

Worlds generated while you act in them. A bilingual (English / 中文) survey of **generative immersive technology**: the models, products, APIs, research demos, studies and devices with which situations can be generated and entered. Every entry is shown on video and lists what it takes as **input**, what it generates (**output**), its **timing** (pre-generated, turn-based, real-time, full-duplex, scripted) and its **access** (open weights, public API, product, waitlist, research only). Built by [Reality Design Lab](https://reality.design) as the living survey behind a research agenda on generative immersion for behavioral science. Sibling of [Reality Design Inspire (AR)](https://augmented.reality.design), [Somatic Reality Inspire](https://somatic.reality.design) and [Machinic Reality Inspire](https://machinic.reality.design).

## What's inside

- **Atlas**: eleven fields and their sub-categories, the five timing modes and eleven capability dimensions.
- **Trends**: where the field is heading as of October 2026, each trend backed by dated releases.
- **Eleven fields**:
  - Video Generation: frontier and open-weight models, control and editing, real-time and long video, panoramic / stereo / spatial video.
  - Interactive Virtual Humans: real-time conversational video (full-duplex audio-visual), audio-driven portraits, photoreal 3D avatars, listening and nonverbal behaviour.
  - Speech, Sound & Spatial Audio: full-duplex speech, expressive voice, sound and music, spatial audio.
  - Interactive World Models: general world models (Genie-like), neural game engines, world models for robots and driving, memory and consistency.
  - 3D Scene & World Generation: explorable 3D worlds, panoramas, layout and procedural scenes, photos to spatial scenes.
  - 3D Assets, Characters & Motion.
  - Capture, Reconstruction & 4D: NeRF and Gaussian splatting, feed-forward reconstruction, dynamic 4D, generative 4D, volumetric video, capture tools.
  - Agents & Simulated Societies: generative agents, agents in 3D worlds, NPC platforms.
  - Generative XR Experiences: in-situ co-creation, restyling reality, generative film and enactment, platform features.
  - Immersive Behavioral Research & Training: presence theory, VR social psychology, criminology, simulation training, clinical VR, generative AI in studies.
  - Platforms, APIs & Delivery: model APIs, real-time agent stacks, engines, devices, datasets and benchmarks.
- **All entries**: filter by field, timing, input, output, access, capability, type, collection and era; full-text search.
- **Resources & Links**: the researchers, founders and artists of the field, and its labs, companies, conferences, journals, newsletters and leaderboards.
- **Papers**, **Labs & creators**, **Starred** (export as `SKILL.md`, `README.md` or a reading list).

The capability dimensions (situational reach, perceptual realism, behavioral plausibility, temporal responsiveness, reactivity, adaptation, situation diversity, authoring accessibility, co-creation & agency, persistence, experimental control) come from the research agenda's framework for comparing generative worlds. Capabilities are as reported by their developers unless stated otherwise.

## For AI assistants

- [`llms.txt`](llms.txt): index
- [`catalog.md`](catalog.md) / [`catalog.zh.md`](catalog.zh.md): full catalog in English / Chinese
- [`data/entries.json`](data/entries.json): raw data

## Maintain it with AI

Open this folder in [Claude Code](https://claude.com/claude-code) and run:

```text
/add-work https://www.tavus.io/griffin
/add-work World Labs Atlas, Meshy 7
/add-work https://arxiv.org/abs/2603.08060
```

`/add-work` (in [`.claude/commands/`](.claude/commands/)) researches the model, product, lab or paper, adds every salient generative immersive work in both languages with a verified video, image and paper links, rebuilds and publishes. The inclusion rule and research rules are in [`data/RESEARCH_BRIEF.md`](data/RESEARCH_BRIEF.md), the data format in [`data/SCHEMA.md`](data/SCHEMA.md), the Resources tab brief in [`data/RESOURCES_BRIEF.md`](data/RESOURCES_BRIEF.md).

| Script | Purpose |
|---|---|
| `python3 tools/check_media.py <url>…` / `--doi` / `--arxiv` / `--og <page>` | Check videos, images, DOIs and arXiv ids; list image candidates on a page |
| `python3 tools/validate.py data/raw/<file>.json` (or `--all`) | Check a batch: bilingual fields, taxonomy ids (field, sub, output, input, timing, access, capability), duplicates |
| `python3 tools/validate_orgs.py --all` | Check the Resources & Links records |
| `python3 tools/build_data.py [--recheck]` | Merge batches, verify every link, write `data/entries.*`, catalogs and `llms.txt` |
| `python3 tools/audit_titles.py` | List same-title works across batches (possible duplicates) |
| `tools/publish.sh "<message>"` | Validate all, rebuild, refuse on errors or unexpected removals, commit and push |

## Run locally

```bash
./serve.sh   # rebuilds data/ and serves http://localhost:8937
```

## Data layout

| Path | Contents |
|---|---|
| `data/taxonomy.json` | Fields and sub-categories, outputs (`modalities`), inputs, timings, access, capability lenses, types, collections and trends, disciplines, resource types |
| `data/raw/*.json` | Research batches: creators, works, leads |
| `data/orgs/*.json` | Resources & Links: people, institutions and websites |
| `data/title_zh/*.json` | Chinese titles of works |
| `data/collections/*.json` | Extra members of a collection or trend (lists of work ids) |
| `data/entries.json`, `data/entries.js`, `data/entries-detail.js` | Built dataset used by the site |
| `data/media_cache.json`, `data/dropped.json` | Link-check results; dead links and DOI / arXiv title mismatches |
| `data/leads.json` | Works and people found but not yet added |

## Credits

Images and videos are linked from the labs, companies and publishers and remain theirs. To suggest a correction or an addition, please open an issue.
