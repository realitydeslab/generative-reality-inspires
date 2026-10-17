/* Generative Immersive Reality Inspire — language-aware field access and Markdown export (SKILL.md / README.md / reading list). */
(() => {
  "use strict";
  const SITE = "https://immersive.reality.design";

  const text = {
    work(w, lang) {
      const zh = lang === "zh";
      return { description: zh ? w.description_zh : w.description, idea: zh ? w.idea_zh : w.idea_en, method: zh ? w.method_zh : w.method };
    },
    creator(c, lang) {
      const zh = lang === "zh";
      return { role: zh ? c.role_zh : c.role, bio: zh ? c.bio_zh : c.bio, why: zh ? c.why_zh : c.why, based: zh ? c.based_zh : c.based };
    },
  };

  const L = {
    en: {
      skillDesc: (n) => `${n} entries I starred in Generative Immersive Reality Inspire (${SITE}): generative immersive technology — video generation, interactive world models, 3D and 4D scenes, full-duplex virtual humans, speech, agents, generative XR and immersive behavioral research. Each entry lists what it is, its idea, how it works, its input, output, timing and access, and links to its paper, video and official page. Use it when designing generated or adaptive immersive situations, choosing models and APIs for a prototype or study, or writing about generative immersion.`,
      skillTitle: "Generative immersion: my starred entries",
      source: (d, n) => `Source: ${SITE} · exported ${d} · ${n} works.`,
      howTitle: "How to use this skill",
      how: [
        "Start from these entries and name the entry and creator you build on.",
        "Combine inputs, outputs and timing across entries to propose systems (e.g. a world model for the setting plus a full-duplex avatar for the person).",
        "Treat capabilities as developer-reported; check the official page before relying on them, and note access (open weights, API, waitlist).",
        "Cite papers only with the DOI / arXiv / URL listed here; do not invent references or details.",
      ],
      field: "Field", modalities: "Output", inputs: "Input", timing: "Timing", access: "Access", idea: "Idea", what: "What it is", method: "How it works", specs: "Specs",
      paper: "Paper", video: "Video", page: "Official page", api: "API docs",
      readmeTitle: "My picks from Generative Immersive Reality Inspire",
      readmeIntro: (n) => `${n} entries I starred on ${SITE}. For an AI assistant, load the companion SKILL.md.`,
      listTitle: "Reading list — Generative Immersive Reality Inspire",
    },
    zh: {
      skillDesc: (n) => `我在 Generative Immersive Reality Inspire（${SITE}）收藏的 ${n} 个条目：生成式沉浸技术，包括视频生成、交互式世界模型、三维与 4D 场景、全双工虚拟人、语音、智能体、生成式扩展现实与沉浸式行为研究。每个条目包括：内容、核心想法、实现方式、输入、输出、时序与获取方式，以及论文、视频和官方页面链接。在设计生成式或自适应的沉浸情境、为原型或研究挑选模型与 API、撰写生成式沉浸相关文章时使用。`,
      skillTitle: "生成式沉浸：我的收藏",
      source: (d, n) => `来源：${SITE} · 导出于 ${d} · 共 ${n} 件作品。`,
      howTitle: "如何使用这个 skill",
      how: [
        "从这些条目出发，并说明借鉴的是哪个条目、哪位创作者。",
        "组合不同条目的输入、输出与时序来提出系统方案（例如用世界模型生成场景，再用全双工虚拟人扮演角色）。",
        "技术能力以开发者公布为准；依赖之前先查看官方页面，并注意获取方式（开源权重、API、候补名单）。",
        "引用论文时只使用这里列出的 DOI、arXiv 或链接，不要编造参考文献或细节。",
      ],
      field: "领域", modalities: "输出", inputs: "输入", timing: "时序", access: "获取方式", idea: "核心想法", what: "内容", method: "实现方式", specs: "参数",
      paper: "论文", video: "视频", page: "官方页面", api: "API 文档",
      readmeTitle: "我在 Generative Immersive Reality Inspire 的收藏",
      readmeIntro: (n) => `我在 ${SITE} 收藏的 ${n} 个条目。给 AI 助手使用时，请加载配套的 SKILL.md。`,
      listTitle: "阅读清单 — Generative Immersive Reality Inspire",
    },
  };

  const label = (pairs, k, zh) => { const r = pairs.find((p) => p[0] === k); return r ? (zh ? r[2] : r[1]) : k; };
  const fieldName = (data, id, zh) => { const f = data.taxonomy.fields.find((x) => x.id === id); return f ? (zh ? f.zh : f.en) : id; };
  const subName = (data, w, zh) => {
    const f = data.taxonomy.fields.find((x) => x.id === w.field);
    const s = f && f.subs.find((x) => x.id === w.sub);
    return s ? (zh ? s.zh : s.en) : "";
  };
  const names = (w, data) => w.creator_ids.map((id) => (data.creators.find((c) => c.id === id) || {}).name || id).join(", ");

  function block(w, data, lang) {
    const s = L[lang], zh = lang === "zh", t = text.work(w, lang);
    const p = w.paper || {};
    return [
      `### ${zh && w.title_zh && w.title_zh !== w.title ? `${w.title_zh}（${w.title}）` : w.title} — ${names(w, data)}${w.year ? ` (${w.year < 0 ? (zh ? `公元前${-w.year}` : `${-w.year} BCE`) : w.year})` : ""}`,
      `- ${s.field}: ${fieldName(data, w.field, zh)} / ${subName(data, w, zh)}`,
      (w.inputs || []).length ? `- ${s.inputs}: ${w.inputs.map((o) => label(data.taxonomy.inputs || [], o, zh)).join(", ")}` : "",
      `- ${s.modalities}: ${(w.modalities || []).map((o) => label(data.taxonomy.modalities, o, zh)).join(", ")}`,
      w.timing ? `- ${s.timing}: ${label(data.taxonomy.timings || [], w.timing, zh)}` : "",
      (w.access || []).length ? `- ${s.access}: ${w.access.map((o) => label(data.taxonomy.access || [], o, zh)).join(", ")}` : "",
      t.idea ? `- ${s.idea}: ${t.idea}` : "",
      t.description ? `- ${s.what}: ${t.description}` : "",
      t.method ? `- ${s.method}: ${t.method}` : "",
      w.specs ? `- ${s.specs}: ${w.specs}` : "",
      p.url ? `- ${s.paper}: ${p.url}${p.venue ? ` (${p.venue})` : ""}` : "",
      w.video && w.video.url ? `- ${s.video}: ${w.video.url}` : "",
      w.source_url ? `- ${s.page}: ${w.source_url}` : "",
      w.api_url ? `- ${s.api}: ${w.api_url}` : "",
    ].filter(Boolean).join("\n");
  }
  const today = () => new Date().toISOString().slice(0, 10);

  function skillMd(list, data, lang) {
    const s = L[lang];
    return [
      "---", "name: generative-immersion-inspiration", `description: ${s.skillDesc(list.length)}`, "---", "",
      `# ${s.skillTitle}`, "", s.source(today(), list.length), "", `## ${s.howTitle}`, "",
      ...s.how.map((x) => `- ${x}`), "", ...list.map((w) => block(w, data, lang) + "\n"),
    ].join("\n");
  }
  function readmeMd(list, data, lang) {
    const s = L[lang];
    return [`# ${s.readmeTitle}`, "", s.readmeIntro(list.length), "", ...list.map((w) => block(w, data, lang) + "\n")].join("\n");
  }
  function readingList(list, data, lang) {
    const s = L[lang];
    const rows = list.filter((w) => w.paper && w.paper.url).sort((a, b) => (a.year || 0) - (b.year || 0))
      .map((w) => `- ${names(w, data)} (${w.year ? (w.year < 0 ? `${-w.year} BCE` : w.year) : "n.d."}). *${w.title}*.${w.paper.venue ? ` ${w.paper.venue}.` : ""} ${w.paper.doi ? `https://doi.org/${w.paper.doi}` : w.paper.url}`);
    return [`# ${s.listTitle}`, "", s.source(today(), rows.length), "", ...rows, ""].join("\n");
  }

  window.MthText = text;
  window.MthExport = { skillMd, readmeMd, readingList };
})();
