"""Markdown catalog of the gallery for AI assistants (llms.txt convention).

catalog_md(data, lang) -> every field and sub-category with its works, then every creator.
llms_txt(data)         -> short index pointing to the full files.
"""
SITE = "https://immersive.reality.design"

T = {
    "en": {
        "title": "Generative Immersive Reality Inspire — catalog",
        "intro": ("A catalog of generative immersive technology: the models, products, APIs, research demos, studies and devices with which situations can be generated and entered. Fields: video generation, interactive virtual humans, speech and spatial audio, interactive world models, 3D scene and world generation, 3D assets and motion, capture / reconstruction / 4D, agents and simulated societies, generative XR experiences, immersive behavioral research and training, and platforms / APIs / delivery. Each entry lists its idea, how it works, its input, output, timing (pre-generated, turn-based, real-time, full-duplex, scripted) and access (open weights, API, product, waitlist, research), and links to its video, paper and official page. Compiled by Reality Design Lab as the living survey behind a research agenda on generative immersion for behavioral science. Capabilities are as reported by their developers."),
        "how": "How an AI assistant should use this file",
        "how_items": [
            "Ground ideas in the specific entries below and name the entry and creator you draw on.",
            "Cite papers with the DOI / arXiv / URL given here; do not invent references.",
            "Combine inputs, outputs, timing and access across entries to propose systems and studies.",
            "Treat capabilities as developer-reported and check the official page; do not invent details not stated here.",
        ],
        "creators": "Labs & creators", "orgs": "Resources & links: people, institutions and websites", "idea": "Idea", "what": "What it is", "method": "How it works",
        "paper": "Paper", "video": "Video", "images": "Images", "page": "Project page", "code": "Code",
        "modalities": "Output", "inputs": "Input", "timing": "Timing", "access": "Access", "specs": "Specs", "api": "API docs",
        "kind": "Type", "known": "Known for", "lenses": "Capability", "exhibited": "Recognition",
    },
    "zh": {
        "title": "Generative Immersive Reality Inspire — 目录",
        "intro": ("生成式沉浸技术目录：可以用来生成并进入情境的模型、产品、API、研究演示、研究与设备。领域包括：视频生成、交互式虚拟人、语音与空间音频、交互式世界模型、三维场景与世界生成、三维资产与动作、捕捉/重建与 4D、智能体与模拟社会、生成式扩展现实体验、沉浸式行为研究与训练，以及平台/API/交付。每个条目都列出核心想法、实现方式、输入、输出、时序（预先生成、回合制、实时、全双工、脚本驱动）与获取方式（开源权重、API、产品、候补、仅研究），并附视频、论文和官方页面链接。由 Reality Design Lab 整理，是一项面向行为科学的生成式沉浸研究议程背后持续更新的综述。技术能力以开发者公布为准。"),
        "how": "AI 助手应如何使用这个文件",
        "how_items": [
            "提出想法时，以下面的具体条目为依据，并说明借鉴的是哪个条目、哪位创作者。",
            "引用论文时使用这里给出的 DOI、arXiv 或链接，不要编造参考文献。",
            "组合不同条目的输入、输出、时序与获取方式，提出系统与研究方案。",
            "技术能力以开发者公布为准，请查看官方页面；不要编造这里没有写到的细节。",
        ],
        "creators": "机构与创作者", "orgs": "资源与链接：人物、机构与网站", "idea": "核心想法", "what": "内容", "method": "实现方式",
        "paper": "论文", "video": "视频", "images": "图片", "page": "项目主页", "code": "代码",
        "modalities": "输出", "inputs": "输入", "timing": "时序", "access": "获取方式", "specs": "参数", "api": "API 文档",
        "kind": "类型", "known": "代表作", "lenses": "能力维度", "exhibited": "获奖与认可",
    },
}


def _yr(y: int, zh: bool) -> str:
    """Years before the common era (Zhuangzi, Mencius) read as 300 BCE / 公元前300."""
    return (f"公元前{-y}" if zh else f"{-y} BCE") if y < 0 else str(y)


def _label(pairs: list, key: str, zh: bool) -> str:
    row = next((p for p in pairs if p[0] == key), None)
    return (row[2] if zh else row[1]) if row else key


def _work(w: dict, lang: str, names: dict, tax: dict) -> str:
    s, zh = T[lang], lang == "zh"
    who = ", ".join(names.get(c, c) for c in w["creator_ids"])
    p = w.get("paper") or {}
    lines = [
        f"#### {(w['title_zh'] + '（' + w['title'] + '）') if zh and w.get('title_zh') and w['title_zh'] != w['title'] else w['title']} — {who}" + (f" ({w.get('date') or _yr(w['year'], zh)})" if w.get("year") else ""),
        f"- {s['kind']}: {_label(tax['kinds'], w.get('kind', ''), zh)}"
        + (f" · {s['timing']}: {_label(tax.get('timings', []), w['timing'], zh)}" if w.get("timing") else "")
        + (f" · {s['access']}: " + ", ".join(_label(tax.get("access", []), a, zh) for a in w["access"]) if w.get("access") else ""),
        f"- {s['inputs']}: " + ", ".join(_label(tax.get("inputs", []), o, zh) for o in w.get("inputs", [])) + " → "
        + f"{s['modalities']}: " + ", ".join(_label(tax["modalities"], o, zh) for o in w.get("modalities", [])),
        f"- {s['idea']}: {w.get('idea_zh' if zh else 'idea_en', '')}",
        f"- {s['what']}: {w.get('description_zh' if zh else 'description', '')}",
        f"- {s['method']}: {w.get('method_zh' if zh else 'method', '')}",
        f"- {s['specs']}: {w['specs']}" if w.get("specs") else "",
        f"- {s['lenses']}: " + ", ".join(_label(tax.get("lenses", []), x, zh) for x in w["lenses"]) if w.get("lenses") else "",
        f"- {s['exhibited']}: {'; '.join(w['exhibited'])}" if w.get("exhibited") else "",
        f"- {s['paper']}: {p['url']}" + (f" ({p['venue']})" if p.get("venue") else "") if p.get("url") else "",
        f"- {s['video']}: {w['video']['url']}" if w.get("video") else "",
        f"- {s['images']}: {' '.join(w['images'])}" if w.get("images") else "",
        f"- {s['page']}: {w['source_url']}" if w.get("source_url") else "",
        f"- {s['api']}: {w['api_url']}" if w.get("api_url") else "",
        f"- {s['code']}: {w['code_url']}" if w.get("code_url") else "",
    ]
    return "\n".join(x for x in lines if x)


def catalog_md(data: dict, lang: str) -> str:
    s, zh = T[lang], lang == "zh"
    tax = data["taxonomy"]
    names = {c["id"]: (c.get("name_zh") if zh and c.get("name_zh") else c["name"]) for c in data["creators"]}
    counts = (f"{len(data['creators'])} 个机构与创作者 · {len(data['works'])} 个条目" if zh
              else f"{len(data['creators'])} labs & creators · {len(data['works'])} entries")
    out = [f"# {s['title']}", "", s["intro"], "", f"{SITE} · {data['generated']} · {counts}", "", f"## {s['how']}", ""]
    out += [f"- {x}" for x in s["how_items"]] + [""]
    for f in tax["fields"]:
        fw = [w for w in data["works"] if w["field"] == f["id"]]
        if not fw:
            continue
        out += [f"## {f['zh'] if zh else f['en']}", "", f["desc_zh" if zh else "desc_en"], ""]
        for sub in f["subs"]:
            sw = [w for w in fw if w.get("sub") == sub["id"]]
            if not sw:
                continue
            out += [f"### {sub['zh'] if zh else sub['en']}", "", sub["desc_zh" if zh else "desc_en"], ""]
            out += ["\n\n".join(_work(w, lang, names, tax) for w in sw), ""]
    orgs = data.get("orgs") or []
    if orgs:
        out += [f"## {s['orgs']}", ""]
        for ot in tax.get("org_types", []):
            group = [o for o in orgs if o.get("type") == ot[0]]
            if not group:
                continue
            out += [f"### {ot[2] if zh else ot[1]}", ""]
            for o in group:
                desc = o.get("description_zh" if zh else "description", "")
                based = o.get("based_zh" if zh else "based", "")
                name = o["name"] + (f" / {o['name_zh']}" if o.get("name_zh") and o["name_zh"] != o["name"] else "")
                life = f"{o['born']}–{o.get('died', '')}" if o.get("born") else ""
                meta = ", ".join(x for x in (based, life) if x)
                known = f" {s['known']}: {'; '.join(o['known_for'])}." if o.get("known_for") else ""
                out.append(f"- **{name}**" + (f" ({meta})" if meta else "") + f" — {desc}{known} {o['url']}")
            out.append("")
    out += [f"## {s['creators']}", ""]
    for c in sorted(data["creators"], key=lambda c: (-c.get("work_count", 0), c["name"])):
        role = c.get("role_zh" if zh else "role", "")
        bio = c.get("bio_zh" if zh else "bio", "")
        site = (c.get("links") or {}).get("site", "")
        out.append(f"- **{c['name']}** ({c.get('work_count', 0)}) — {role}. {bio}" + (f" {site}" if site else ""))
    return "\n".join(out).rstrip() + "\n"


def llms_txt(data: dict) -> str:
    fields = ", ".join(f"{f['en']} ({sum(w['field'] == f['id'] for w in data['works'])})" for f in data["taxonomy"]["fields"])
    return "\n".join([
        "# Generative Immersive Reality Inspire",
        "",
        f"> {T['en']['intro']}",
        "",
        f"{len(data['creators'])} labs & creators, {len(data['works'])} entries ({fields}), "
        f"{sum(bool(w.get('paper')) for w in data['works'])} with papers, {len(data.get('orgs') or [])} people, institutions & websites, updated {data['generated']}. "
        "Bilingual (English / Simplified Chinese).",
        "",
        "## Full catalog",
        "",
        f"- [English catalog]({SITE}/catalog.md): every field and sub-category with all entries, then all labs & creators",
        f"- [Chinese catalog]({SITE}/catalog.zh.md): 中文版完整目录",
        f"- [Raw data (JSON)]({SITE}/data/entries.json)",
        "",
        "## Website",
        "",
        f"- [{SITE}]({SITE}): videos and images, paper links, trends, filters by field, input, output, timing, access, capability and type, starring and SKILL.md export",
        "",
    ])
