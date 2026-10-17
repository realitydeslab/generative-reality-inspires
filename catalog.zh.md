# Generative Immersive Reality Inspire — 目录

生成式沉浸技术目录：可以用来生成并进入情境的模型、产品、API、研究演示、研究与设备。领域包括：视频生成、交互式虚拟人、语音与空间音频、交互式世界模型、三维场景与世界生成、三维资产与动作、捕捉/重建与 4D、智能体与模拟社会、生成式扩展现实体验、沉浸式行为研究与训练，以及平台/API/交付。每个条目都列出核心想法、实现方式、输入、输出、时序（预先生成、回合制、实时、全双工、脚本驱动）与获取方式（开源权重、API、产品、候补、仅研究），并附视频、论文和官方页面链接。由 Reality Design Lab 整理，是一项面向行为科学的生成式沉浸研究议程背后持续更新的综述。技术能力以开发者公布为准。

https://immersive.reality.design · 2026-10-17 · 318 个机构与创作者 · 508 个条目

## AI 助手应如何使用这个文件

- 提出想法时，以下面的具体条目为依据，并说明借鉴的是哪个条目、哪位创作者。
- 引用论文时使用这里给出的 DOI、arXiv 或链接，不要编造参考文献。
- 组合不同条目的输入、输出、时序与获取方式，提出系统与研究方案。
- 技术能力以开发者公布为准，请查看官方页面；不要编造这里没有写到的细节。

## 视频生成

根据文字、图像和参考素材合成视听事件的模型。这是制作情境素材最快的路径，但视频只能观看，不能在其中行动。

### 前沿文生 / 图生视频

闭源旗舰模型（Sora、Veo、可灵、Runway、Luma、海螺、Seedance……），许多已能同时生成声音。

#### 可灵 4.0（Kling 4.0） — 快手 / 可灵 (2026-09-28)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 产品 / 应用
- 输入: 文字提示, 图像, 视频 → 输出: 平面视频, 语音 / 声音, 音效、音乐与空间音频
- 核心想法: 30 秒的长镜头可以在一个连续镜头里容纳一段完整的短互动（接近、交流、反应）。
- 内容: 可灵 4.0 于 2026-09-28 推出（Flash 版先向高阶订阅用户开放），单次生成延长到约 30 秒，支持关键帧控制和立体声；据报道于 2026-10-16 全面推出，截至 2026 年 10 月中旬已在 kling.ai 上线。
- 实现方式: 可灵新一代模型；据报道每段最多可用 10 张关键帧图像并输出最高 4K；架构未公开。
- 参数: ~30 s per generation · up to 10 keyframes · up to 4K (reported)
- 能力维度: 持久性, 实验控制, 感知真实感
- 视频: https://www.youtube.com/watch?v=nlM7kL3kv_Y
- 项目主页: https://kling.ai/

#### 通义万相 3.0（Wan 3.0） — 阿里通义 (2026-08-06)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 候补 / 抢先体验, 公开 API
- 输入: 文字提示, 图像, 视频 → 输出: 平面视频, 语音 / 声音, 音效、音乐与空间音频
- 核心想法: 就连最重要的开源视频团队也开始把最新旗舰闭源，开源的 Wan 模型因此落后一代。
- 内容: 通义万相 Wan 3.0 于 2026-08-06 在阿里云开启公测；与开源的 Wan 2.1、2.2 不同，它闭源、仅提供 API，可在一个提示中同时接收文本、图像、视频和音频。此前 Wan 2.5（2025 年 9 月）和 Wan 2.6（2025 年 12 月）已加入原生音频与参考角色功能。
- 实现方式: 通过阿里云百炼提供服务的多模态音视频生成模型；截至 2026 年 10 月，架构与权重均未公开。
- 参数: up to 30 s · 1080p (reported)
- 能力维度: 持久性, 创作可及性, 实验控制
- 视频: https://www.youtube.com/watch?v=dC5pu8zL2p8
- 图片: https://img.alicdn.com/imgextra/i1/O1CN01WlNesT1EWvfm8mzKw_!!6000000000360-2-tps-600-315.png
- 项目主页: https://wan.video/
- API 文档: https://www.alibabacloud.com/help/en/model-studio/

#### Gemini Omni — 谷歌 DeepMind (2026-05-19)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 产品 / 应用, 公开 API
- 输入: 文字提示, 图像, 视频 → 输出: 平面视频, 语音 / 声音, 音效、音乐与空间音频
- 核心想法: 生成与编辑合并为一场对话：情境可以逐镜修改（“让旁观者转过身”），而不必整段重新抽卡。
- 内容: Google 在 2026-05-19 I/O 上发布的 Veo 系列后继。首个模型 Gemini Omni Flash 可接受文本、图像、音频与视频的任意组合，生成带声音的视频或通过对话修改视频，已上线 Gemini 应用、Flow、YouTube Shorts 与 Google Vids；在 Gemini API 中于 2026-06-30 进入预览，2026-08-27 以 gemini-omni-1.1-flash 正式发布（GA）。
- 实现方式: 原生多模态的 Gemini 系列生成模型，可接收最长约 3 秒的参考视频以及图像和音频；DeepMind 称其在编辑以及文生、图生、参考生成视频的人工评测中领先。
- 参数: 360p / 720p · 1080p and 4K via upscaling · up to 3 s video reference · API GA 2026-08-27
- 能力维度: 实验控制, 共创与能动性, 创作可及性
- 视频: https://www.youtube.com/watch?v=KUyRq7szZsM
- 项目主页: https://deepmind.google/models/gemini-omni/
- API 文档: https://ai.google.dev/gemini-api/docs/video

#### Seedance 2.0 — 字节跳动 Seed (2026-02-12)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 产品 / 应用, 公开 API
- 输入: 文字提示, 图像, 视频 → 输出: 平面视频, 语音 / 声音, 音效、音乐与空间音频
- 核心想法: 在一个提示中同时给出音频、动作和镜头参考，带来导演级的控制，也让肖像授权成为必须的设计要求。
- 内容: Seedance 2.0（2026-02-12 在字节跳动的即梦与豆包中公开上线，4 月经 BytePlus 面向全球）可根据文本、图像、音频和视频参考的任意组合联合生成音视频。据媒体报道，字节跳动在发布后不久暂停了真人参考素材上传；Seedance 2.5（2026-07-30）把单次生成延长到 30 秒。
- 实现方式: 统一的多模态音视频联合生成架构，接受文本、图像、音频与视频输入（据 Seedance 2.0 技术报告）。
- 参数: 4–15 s · joint audio-video · Seedance 2.5: up to 30 s
- 能力维度: 感知真实感, 实验控制, 情境可达性
- 论文: https://arxiv.org/abs/2604.14148 (arXiv 2026)
- 视频: https://www.youtube.com/watch?v=l89woJ0jidw
- 项目主页: https://seed.bytedance.com/en/seedance2_0

#### 可灵 3.0（Kling 3.0） — 快手 / 可灵 (2026-02-04)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 产品 / 应用, 公开 API
- 输入: 文字提示, 图像, 视频 → 输出: 平面视频, 语音 / 声音, 音效、音乐与空间音频
- 核心想法: 可以指定谁在何时说话，多人短对话场景因此可以用作刺激材料。
- 内容: 可灵 3.0（2026-02-04）可生成最长 15 秒的多镜头序列，带原生音频和多语种、口型同步的对白，用户可指定由谁说话；“Omni”版本可用参考视频和图像保持角色一致。
- 实现方式: 沿用 Kling-Omni 架构，加入音视频联合生成与分镜式多镜头规划（据快手新闻稿）。
- 参数: up to 15 s · multi-shot · speech in EN / ZH / JA / KO / ES
- 能力维度: 行为似真性, 创作可及性, 感知真实感
- 视频: https://www.youtube.com/watch?v=XD_7FNPhZQY
- 项目主页: https://kling.ai/
- API 文档: https://app.klingai.com/global/dev

#### Vidu Q3 — 生数科技（Vidu） (2026-02-02)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 产品 / 应用, 公开 API
- 输入: 文字提示, 图像 → 输出: 平面视频, 语音 / 声音, 音效、音乐与空间音频
- 核心想法: 体现了国内团队的迭代速度：不到两年推出四代 Vidu，每代都新增参考生成或音频能力。
- 内容: Vidu Q3（2026 年 2 月初）是生数科技的音视频模型，可生成带同步语音和声音的片段，参考生视频的一致性较强。生数科技于 2024 年 4 月与清华大学推出 Vidu 系列，是国内首个 Sora 级模型；2026 年 10 月 Vidu Q4 处于预览阶段。
- 实现方式: 基于清华提出的 U-ViT 扩散 Transformer，扩展到音视频联合生成；Q3 细节未公开。
- 能力维度: 创作可及性, 持久性
- 视频: https://www.youtube.com/watch?v=QQloL2IW8kA
- 项目主页: https://www.vidu.com/
- API 文档: https://platform.vidu.com/

#### Gen-4.5 — Runway (2025-12-01)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 产品 / 应用, 公开 API
- 输入: 文字提示, 图像 → 输出: 平面视频
- 核心想法: 前沿模型竞争的重点从分辨率转向身体与物体的物理合理性。
- 内容: Gen-4.5（2025-12-01）提升了动作质量、物体的重量感与提示遵循；Runway 称其发布时以 1247 Elo 位列 Artificial Analysis 文生视频榜首。图生视频功能于 2026 年初推出。
- 实现方式: Runway 新一代视频扩散模型，在 NVIDIA Hopper 与 Blackwell GPU 上训练；细节未公开。
- 参数: #1 Artificial Analysis T2V at launch · 1,247 Elo (Runway claim)
- 能力维度: 行为似真性, 感知真实感
- 视频: https://www.youtube.com/watch?v=ei2PsDpPbB4
- 图片: https://d3phaj0sisr2ct.cloudfront.net/site/images/research/gen/launch-post/card-gen-4.5.png
- 项目主页: https://runwayml.com/research/introducing-runway-gen-4.5
- API 文档: https://docs.dev.runwayml.com/

#### Veo 3.1 — 谷歌 DeepMind (2025-10-15)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 公开 API, 产品 / 应用
- 输入: 文字提示, 图像 → 输出: 平面视频, 语音 / 声音, 音效、音乐与空间音频
- 核心想法: 参考图和首尾帧让研究者能在多个片段中固定同一角色与场景，是迈向可控刺激材料集的第一步。
- 内容: Veo 3.1（2025-10-15）在 Veo 3 基础上带来更丰富的原生音频和更好的提示遵循，并在 Flow 与 Gemini API 中提供“素材生成视频”（参考图）、首尾帧过渡，以及延展到一分钟以上的场景扩展。
- 实现方式: Veo 3 的后继版本，支持参考图条件、首尾帧插值，以及从上一段最后一秒接着生成的片段延展。
- 参数: 8 s per clip · extend to 60 s+ · 720p / 1080p · native audio
- 能力维度: 实验控制, 感知真实感, 创作可及性
- 视频: https://www.youtube.com/watch?v=I06Ef8alr2Y
- 图片: https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Veo3.1_Social_v3.width-1300.png
- 项目主页: https://blog.google/innovation-and-ai/products/veo-updates-flow/
- API 文档: https://ai.google.dev/gemini-api/docs/video

#### Sora 2 — OpenAI (2025-09-30)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 文字提示, 图像, 视频 → 输出: 平面视频, 语音 / 声音, 音效、音乐与空间音频
- 核心想法: 经授权的肖像插入把视频模型变成了社交媒介；而它在数月内下线，也提醒需要稳定模型版本的研究注意风险。
- 内容: OpenAI 的第二代视频模型，2025-09-30 随一款社交 iOS 应用发布，可生成带同步对白和音效的片段，并能插入经过验证用户的“客串”（cameo）形象。该应用于 2026-04-26 关闭，API 于 2026-09-24 停止。
- 实现方式: 音视频联合生成；OpenAI 称物理合理性有所提升（投篮不中会反弹，而不是瞬移进篮筐），并能遵循多镜头指令；架构未公开。
- 参数: synchronized audio · cameos · app 2025-09-30 → closed 2026-04-26
- 能力维度: 感知真实感, 行为似真性, 共创与能动性
- 视频: https://www.youtube.com/watch?v=lEcg6AJ6DVY
- 图片: https://images.ctfassets.net/kftzwdyauwt9/1Q8NDmnyavsoPAKDlWpW18/a1f595376097668d1772c9cac40fc8ee/16_x_9____1_.png?w=1600&h=900&fit=fill
- 项目主页: https://openai.com/index/sora-2/

#### Ray3 — Luma AI (2025-09-18)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 产品 / 应用, 公开 API
- 输入: 文字提示, 图像, 视频 → 输出: 平面视频
- 核心想法: 会自我审阅草稿的模型，预示着在呈现之前先按规格检查场景的生成闭环。
- 内容: Ray3（2025-09-18）是 Luma 的“推理型”视频模型，会评估并修正自己的草稿，并能导出 16 位 HDR 以接入影视流程；Ray3.14（2026-01-26）改为原生 1080p，Ray3.2（2026-06-09）支持每段最多 16 个关键帧。
- 实现方式: Luma 称其在视频扩散模型之上加入多模态推理阶段来规划与评估生成结果，并针对 HDR 输出进行训练。
- 参数: 16-bit HDR · draft mode · Ray3.2: up to 16 keyframes
- 能力维度: 感知真实感, 实验控制
- 视频: https://www.youtube.com/watch?v=z2UIcD2xvsA
- 图片: https://cdn.sanity.io/images/2ylxvaa2/production/3f83440c074f2a5e161d1975975cafeb73a81a78-1920x1080.png?rect=0,36,1920,1008&w=1200&h=630&fm=jpg
- 项目主页: https://lumalabs.ai/ray
- API 文档: https://docs.lumalabs.ai/

#### Marey — Moonvalley (2025-07-08)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 产品 / 应用
- 输入: 文字提示, 图像, 视频 → 输出: 平面视频
- 核心想法: 仅用授权数据训练，回应了机构使用生成素材前必须面对的数据来源问题。
- 内容: Moonvalley 的 Marey（2025 年 7 月公开上线）只用授权素材训练，面向影视创作者，提供镜头路径重设、姿态迁移等镜头与动作控制。
- 实现方式: Moonvalley 称其基于商业授权视频训练，并与动画工作室 Asteria 共同开发。
- 参数: 1080p · 24 fps
- 能力维度: 实验控制, 创作可及性
- 视频: https://www.youtube.com/watch?v=YbhQnzYAIjM
- 项目主页: https://www.moonvalley.com/

#### 海螺 02（Hailuo 02） — 稀宇科技 MiniMax（海螺 AI） (2025-06-18)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 产品 / 应用, 公开 API
- 输入: 文字提示, 图像 → 输出: 平面视频
- 核心想法: 可信的全身动作，是以身体行为作为刺激的情境的前提。
- 内容: MiniMax 的海螺 02（2025-06-18）可生成原生 1080p 片段，以体操、杂技等复杂全身动作著称。
- 实现方式: MiniMax 称其采用 NCR（噪声感知计算重分配）架构，训练与推理效率约提升 2.5 倍，参数量为海螺 01 的 3 倍、训练数据为 4 倍。
- 参数: 1080p · 6 s / 768p · 10 s
- 能力维度: 行为似真性, 感知真实感
- 视频: https://www.youtube.com/watch?v=J18idUz87LA
- 项目主页: https://www.minimax.io/news/minimax-hailuo-02
- API 文档: https://platform.minimax.io/docs

#### Midjourney Video V1 — Midjourney (2025-06-18)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 产品 / 应用
- 输入: 图像, 文字提示 → 输出: 平面视频
- 核心想法: Midjourney 把它定位为从审美导向的图像模型迈向实时开放世界模拟的一步。
- 内容: Midjourney 首个视频模型（2025-06-18）可把任意 Midjourney 图像做成 5 秒动画，可延展到约 21 秒，运动方式可自动生成或由提示指定。
- 实现方式: 提供“低/高”两档运动强度的图生视频模型；架构未公开。
- 参数: 480p · 5 s, extendable to ~21 s
- 能力维度: 创作可及性, 情境多样性
- 视频: https://www.youtube.com/watch?v=E9PvSeIO5NY
- 项目主页: https://updates.midjourney.com/introducing-our-v1-video-model/

#### Seedance 1.0 — 字节跳动 Seed (2025-06-11)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 产品 / 应用, 公开 API
- 输入: 文字提示, 图像 → 输出: 平面视频
- 核心想法: 一次生成即可完成多镜头叙事（切换、反打、特写）。
- 内容: 字节跳动 Seed 的 Seedance 1.0（2025-06-11）可生成 1080p 多镜头片段，切镜后主体保持一致；字节跳动称其发布后在 Artificial Analysis 文生与图生视频竞技场排名第一。
- 实现方式: 据技术报告：采用时空解耦层的扩散 Transformer，结合多源数据筛选、RLHF，以及约 10 倍加速的蒸馏推理方案。
- 参数: 1080p · 5–10 s · multi-shot
- 能力维度: 持久性, 感知真实感, 创作可及性
- 论文: https://arxiv.org/abs/2506.09113 (arXiv 2025)
- 视频: https://www.youtube.com/watch?v=F7wNbB0_uyk
- 项目主页: https://seed.bytedance.com/en/seedance

#### Veo 3 — 谷歌 DeepMind (2025-05-20)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 公开 API, 产品 / 应用
- 输入: 文字提示, 图像 → 输出: 平面视频, 语音 / 声音, 音效、音乐与空间音频
- 核心想法: 声音与口型同步的语音随画面一起生成，生成场景因此能承载社交互动，而不只是一段画面。
- 内容: Veo 3（2025-05-20 Google I/O）可一次生成视频及对白、音效和环境声，使生成场景里“会说话的角色”变得普遍；DeepMind 2025 年 9 月的论文称它能零样本完成感知与物理类任务。
- 实现方式: 音视频联合扩散模型；论文《Video models are zero-shot learners and reasoners》仅靠提示就用 62 类任务对其进行测试。
- 参数: 8 s · 720p / 1080p · native audio
- 能力维度: 感知真实感, 情境可达性, 行为似真性
- 论文: https://arxiv.org/abs/2509.20328 (arXiv 2025)
- 视频: https://www.youtube.com/watch?v=QYnJ3qJ5qJQ
- 图片: https://storage.googleapis.com/gweb-uniblog-publish-prod/images/5.20v2_SS_1920x1080.width-1300.png
- 项目主页: https://blog.google/innovation-and-ai/products/generative-media-models-io-2025/
- API 文档: https://ai.google.dev/gemini-api/docs/video

#### Gen-4 — Runway (2025-03-31)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 产品 / 应用, 公开 API
- 输入: 文字提示, 图像 → 输出: 平面视频
- 核心想法: 跨镜头保持身份一致，是把零散片段变成有固定角色的情境的关键。
- 内容: Gen-4（2025-03-31）只需一张参考图即可在多个镜头间保持角色、物体与场景一致，同一个人可以出现在不同光照和场景中。
- 实现方式: 带视觉参考（References）条件的图生视频扩散模型，用参考图约束身份与风格；架构未公开。
- 参数: 5 / 10 s · 720p
- 能力维度: 持久性, 实验控制, 创作可及性
- 视频: https://www.youtube.com/watch?v=uRkfzKYFOxc
- 图片: https://d3phaj0sisr2ct.cloudfront.net/site/content/images/card_gen4post.jpg
- 项目主页: https://runwayml.com/research/introducing-runway-gen-4
- API 文档: https://docs.dev.runwayml.com/

#### Veo 2 — 谷歌 DeepMind (2024-12-16)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 公开 API, 产品 / 应用
- 输入: 文字提示, 图像 → 输出: 平面视频
- 核心想法: 镜头类型和运镜成为可靠的提示参数，适合需要特定视角的情境素材。
- 内容: 第二代 Veo（2024-12-16），物理表现与镜头控制更好，最高可输出 4K；DeepMind 称其在发布时的人类偏好对比中优于 Sora Turbo、可灵与 MiniMax。后来开放于 Gemini API、Gemini 应用与 YouTube Shorts。
- 实现方式: 基于扩散的视频模型，强化了对物理、人体运动与电影摄影的建模；细节未公开。
- 参数: up to 4K · 8 s clips (API)
- 能力维度: 感知真实感, 实验控制, 行为似真性
- 视频: https://www.youtube.com/watch?v=PEUcCF-jVCI
- 图片: https://storage.googleapis.com/gweb-uniblog-publish-prod/images/12-16-24_GenMedia_16x9.width-1300.png
- 项目主页: https://blog.google/innovation-and-ai/models-and-research/google-labs/video-image-generation-update-december-2024/
- API 文档: https://ai.google.dev/gemini-api/docs/video

#### Movie Gen — Meta (2024-10-04)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 文字提示, 图像 → 输出: 平面视频, 音效、音乐与空间音频
- 核心想法: 把个性化、编辑和声音放进同一个系统，并发布了同代最详细的公开技术报告之一。
- 内容: Meta 的 Movie Gen（2024-10-04）是一套研究模型，可生成 16 秒 1080p 视频，用一张人物照片做个性化，用文字编辑视频，并配上同步音效和音乐；未作为独立产品发布。
- 实现方式: 300 亿参数、以流匹配训练的视频 Transformer，外加 130 亿参数的音频模型，详见 92 页技术报告。
- 参数: 30B video · 13B audio · 16 s · 16 fps · 1080p (upsampled)
- 能力维度: 感知真实感, 实验控制, 创作可及性
- 论文: https://arxiv.org/abs/2410.13720 (arXiv 2024)
- 视频: https://www.youtube.com/watch?v=FHSSx4dUs7E
- 项目主页: https://ai.meta.com/research/movie-gen/

#### Gen-3 Alpha — Runway (2024-06-17)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 产品 / 应用, 公开 API
- 输入: 文字提示, 图像, 视频 → 输出: 平面视频
- 核心想法: 明确把商用视频生成定义为世界建模，Runway 后来把这条路线延续到交互式 GWM 模型中。
- 内容: Gen-3 Alpha（2024-06-17）是 Runway 在新的大规模多模态训练设施上训练的第一个模型，人物表情丰富，时间维度的控制更细；Runway 把它定位为迈向“通用世界模型”的一步。
- 实现方式: 在视频与图像上联合训练的扩散模型，使用描述详细、时间上密集的字幕。
- 参数: 10 s · 1280×768
- 能力维度: 感知真实感, 实验控制
- 视频: https://www.youtube.com/watch?v=nByslCkykj8
- 图片: https://d3phaj0sisr2ct.cloudfront.net/site/blog/images/research-001.jpg
- 项目主页: https://runwayml.com/research/introducing-gen-3-alpha
- API 文档: https://docs.dev.runwayml.com/

#### Dream Machine — Luma AI (2024-06-12)
- 类型: 产品 / 应用 · 时序: 预先生成 · 获取方式: 产品 / 应用, 公开 API
- 输入: 文字提示, 图像 → 输出: 平面视频
- 核心想法: 2024 年年中的免费公开访问，让学生当天下午就能上手测试视频生成。
- 内容: Luma 的 Dream Machine（2024-06-12）让高质量的文生/图生视频模型可以在网页上免费试用，约两分钟生成 120 帧片段，是最早向所有人开放的 Sora 级工具之一。
- 实现方式: 直接在视频上训练的 Transformer 视频扩散模型（Luma Ray1）。
- 参数: 5 s · 120 frames
- 能力维度: 创作可及性, 情境多样性
- 视频: https://www.youtube.com/watch?v=Zb3tffmBPRE
- 图片: https://cdn.sanity.io/images/2ylxvaa2/production/b31d99c8312ed2f74080e118e9d58bf6b2b6e953-1200x630.png?w=1200&h=630&fm=jpg
- 项目主页: https://lumalabs.ai/dream-machine
- API 文档: https://docs.lumalabs.ai/

#### 可灵（Kling） — 快手 / 可灵 (2024-06-06)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 产品 / 应用, 公开 API
- 输入: 文字提示, 图像 → 输出: 平面视频
- 核心想法: 表明一家中国短视频平台能比 OpenAI 早数月把前沿视频生成交到数百万用户手中。
- 内容: 快手首个可灵模型（2024-06-06）是第一个公众能用上的 Sora 级文生视频模型，官方称可生成最长两分钟、1080p、30 fps 的视频；2024 年 7 月面向全球开放。
- 实现方式: 快手称其采用扩散 Transformer、3D VAE 与三维时空注意力，并基于快手规模的视频数据训练。
- 参数: up to 2 min · 1080p · 30 fps (claimed)
- 能力维度: 感知真实感, 持久性, 创作可及性
- 视频: https://www.youtube.com/watch?v=BKNAXS0keoQ
- 项目主页: https://kling.ai/
- API 文档: https://app.klingai.com/global/dev

#### Veo — 谷歌 DeepMind (2024-05-14)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 候补 / 抢先体验
- 输入: 文字提示, 图像, 视频 → 输出: 平面视频
- 核心想法: 把电影语言当作控制接口：用摄影师的术语来指挥一个镜头。
- 内容: Google DeepMind 首个 Veo 模型，于 2024-05-14 Google I/O 发布，可生成超过一分钟的 1080p 片段，并理解“延时”“航拍”等电影术语；最初只通过 VideoFX 向部分创作者开放。
- 实现方式: 以文本、图像或视频为条件的潜空间扩散 Transformer；DeepMind 称其建立在 GQN、Phenaki、WALT、VideoPoet 与 Lumiere 等工作之上。
- 参数: 1080p · > 60 s (claimed)
- 能力维度: 感知真实感, 实验控制
- 视频: https://www.youtube.com/watch?v=dKAVFLB75xs
- 图片: https://storage.googleapis.com/gweb-uniblog-publish-prod/images/IO24_Gen_Media_Header_1.width-1300.png
- 项目主页: https://blog.google/innovation-and-ai/products/google-generative-ai-veo-imagen-3/

#### Sora — OpenAI (2024-02-15)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 文字提示, 图像, 视频 → 输出: 平面视频
- 核心想法: 让“视频模型即世界模拟器”成为整个领域的叙事：一分钟长镜头基本保持物体与空间一致，但人无法在其中行动。
- 内容: OpenAI 的首个文生视频模型，2024 年 2 月以预览形式发布，展示了长达一分钟、场景与镜头运动保持连贯的 1080p 镜头，2024 年 12 月作为产品上线。OpenAI 已于 2026-04-26 关闭 Sora 应用，并于 2026-09-24 停止 API。
- 实现方式: 在压缩视频潜空间的时空块（spacetime patches）上训练扩散 Transformer，训练数据为不同时长、分辨率与画幅的视频和图像。
- 参数: up to 60 s · up to 1080p (Feb 2024 preview)
- 能力维度: 感知真实感, 持久性, 情境多样性
- 论文: https://openai.com/index/video-generation-models-as-world-simulators/ (OpenAI technical report 2024)
- 视频: https://www.youtube.com/watch?v=HK6y8DAPN_0
- 图片: https://images.ctfassets.net/kftzwdyauwt9/8264d3d7-922c-4343-dde924eae75b/c9f68101050dc2a6caaac2f434c0da5e/paper-airplanes.jpg?w=1600&h=900&fit=fill
- 项目主页: https://openai.com/index/sora/

#### Lumiere — 谷歌 (2024-01-23)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 文字提示, 图像 → 输出: 平面视频
- 核心想法: 对需要在物理上看起来连续的运动而言，整体的时间一致性胜过拼接关键帧。
- 内容: Google Research 的 Lumiere（2024-01-23）一次性生成整段时长，而不是先生成关键帧再插帧，因此运动更连贯；演示包括风格化生成、动态照片（cinemagraph）和视频修补。
- 实现方式: 在预训练文生图扩散模型上构建的时空 U-Net（STUNet），在空间和时间两个维度同时下采样。
- 参数: 80 frames · 16 fps · 5 s
- 能力维度: 行为似真性, 实验控制
- 论文: https://arxiv.org/abs/2401.12945 (SIGGRAPH Asia 2024)
- 视频: https://www.youtube.com/watch?v=f9ThAzZs32M
- 图片: https://lumiere-video.github.io/images/lumiere_frame_poster.jpg
- 项目主页: https://lumiere-video.github.io/

#### Pika 1.0 — Pika (2023-11-28)
- 类型: 产品 / 应用 · 时序: 预先生成 · 获取方式: 产品 / 应用
- 输入: 文字提示, 图像, 视频 → 输出: 平面视频
- 核心想法: 较早表明推动生成视频大众化的是好玩的编辑功能，而不只是画质。
- 内容: Pika 1.0（2023-11-28）把起家于 Discord 的 Pika 机器人变成网页上的“想法生成视频”平台，提供文生视频、让图片动起来，以及局部修改、画面扩展等视频内编辑。
- 实现方式: 自研视频扩散模型；后续 Pika 2.x 加入了 Pikaffects 特效和场景素材组合等功能。
- 能力维度: 创作可及性, 共创与能动性
- 视频: https://www.youtube.com/watch?v=6b10jGNNbXQ
- 图片: https://pika.art/brand/opengraph.png
- 项目主页: https://pika.art/

#### Gen-2 — Runway (2023-03-20)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 产品 / 应用
- 输入: 文字提示, 图像 → 输出: 平面视频
- 核心想法: 在视频生成达到照片级真实之前两年，就把“用提示生成片段”交到了非工程师手中。
- 内容: Runway 的 Gen-2（2023-03-20）是首个商用文生视频模型，可在面向影视创作者的网页编辑器中把一句提示或一张图变成 4 秒短片。
- 实现方式: 潜空间视频扩散模型，在 Runway Gen-1（结构与内容引导）的基础上加入文本和图像条件。
- 参数: 4 s clips (at launch)
- 能力维度: 创作可及性, 情境多样性
- 视频: https://www.youtube.com/watch?v=trXPfpV5iRQ
- 图片: https://runway-static-assets.s3.amazonaws.com/site/images/news/Researchhub_014.jpg
- 项目主页: https://runwayml.com/research/gen-2

#### Imagen Video — 谷歌 (2022)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 文字提示 → 输出: 平面视频
- 核心想法: 级联扩散证明了高分辨率可以实现，代价是串联七个模型。
- 内容: Google Research 的 Imagen Video（2022-10-05）可从文字生成 5.3 秒、1280×768、24 fps 的片段，是当时保真度最高的文生视频结果，但从未公开发布。
- 实现方式: 由七个视频扩散模型组成的级联（基础模型加 3 个空间超分和 3 个时间超分阶段），以 T5-XXL 文本编码为条件。
- 参数: 1280×768 · 24 fps · 128 frames
- 能力维度: 感知真实感
- 论文: https://arxiv.org/abs/2210.02303 (arXiv 2022)
- 视频: https://imagen.research.google/video/videos/leaves.mp4
- 图片: https://imagen.research.google/video/leaves.png
- 项目主页: https://imagen.research.google/video/

#### Make-A-Video — Meta (2022)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 文字提示, 图像 → 输出: 平面视频
- 核心想法: 证明可以从无标注视频中学习运动、从带字幕的图像中学习外观，这一配方被后来许多模型沿用。
- 内容: Meta AI 的 Make-A-Video（2022-09-29）是最早的文生视频系统之一，可生成低分辨率短片（如泰迪熊画肖像），且不需要成对的文本-视频数据。
- 实现方式: 在文生图扩散模型上加入时空卷积与注意力层，并配合插帧与超分辨率。
- 参数: 16 frames · up to 768×768
- 能力维度: 情境多样性
- 论文: https://arxiv.org/abs/2209.14792 (ICLR 2023)
- 图片: https://makeavideo.studio/assets/A_teddy_bear_painting_a_portrait-sm.gif
- 项目主页: https://makeavideo.studio/

### 开源权重视频模型

Wan、HunyuanVideo、LTX、CogVideoX、Mochi、Open-Sora 等可以本地运行、锁定版本并检查的模型。

#### MiniMax H3 — 稀宇科技 MiniMax（海螺 AI） (2026-07-31)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码, 公开 API, 产品 / 应用
- 输入: 文字提示, 图像, 视频 → 输出: 平面视频, 语音 / 声音, 音效、音乐与空间音频
- 核心想法: 可下载权重的旗舰级音视频模型，让实验室能锁定刺激材料背后的确切模型版本。
- 内容: MiniMax H3（2026-07-31）可根据文本、图像、视频和音频上下文生成最长 15 秒、2K 分辨率并带原生立体声的视频，也能按指令编辑视频；少见的是，MiniMax 把这款旗舰模型的权重发布在了 Hugging Face 上。
- 实现方式: MiniMax 称其采用上下文全模态表征（Contextual Omni Representation），包括 H3-VAE、H3-Omni Transformer，以及用于编辑的上下文再生成。
- 参数: up to 15 s · 2K · native stereo audio
- 能力维度: 创作可及性, 实验控制, 感知真实感
- 视频: https://filecdn.minimax.chat/public/h3-en-v2-video-001-1785473639588.mp4
- 图片: https://file.cdn.minimax.io/public/3df321d9-42bd-4be0-ac58-71f22377a11f.png
- 项目主页: https://www.minimax.io/blog/minimax-h3
- API 文档: https://platform.minimax.io/docs
- 代码: https://huggingface.co/MiniMaxAI/MiniMax-H3

#### 混元视频 1.5（HunyuanVideo 1.5） — 腾讯混元 (2025-11-20)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 文字提示, 图像 → 输出: 平面视频
- 核心想法: 开源模型的竞争转向“每个参数的质量”；实验室不需要集群就能运行。
- 内容: HunyuanVideo 1.5（2025-11-20）是 83 亿参数的轻量开源模型，可生成 720p 视频（配合超分辨率阶段可达 1080p），能在消费级显卡上运行。
- 实现方式: 采用选择性滑动分块注意力（SSTA）的 DiT，配字形感知的中英文本编码和视频超分辨率网络。
- 参数: 8.3B · 720p → 1080p SR
- 能力维度: 创作可及性, 实验控制
- 论文: https://arxiv.org/abs/2511.18870 (arXiv 2025)
- 视频: https://github.com/user-attachments/assets/d45ec78e-ea40-47f1-8d4d-f4d9a0682e2d
- 项目主页: https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5
- 代码: https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5

#### LTX-2 — Lightricks (2025-10-23)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码, 公开 API, 产品 / 应用
- 输入: 文字提示, 图像 → 输出: 平面视频, 语音 / 声音, 音效、音乐与空间音频
- 核心想法: 可锁定版本、达到生产级分辨率的开源音视频生成，并提供用于定制控制的 LoRA 接口。
- 内容: Lightricks 的 LTX-2（2025-10-23 发布，权重随后开放）可生成同步的音频与视频，最高 4K、50 fps；LTX-2.5 于 2026 年 8 月推出，是 220 亿参数的开源模型，配有一系列控制 LoRA。
- 实现方式: 非对称双流 Transformer，通过跨模态注意力联合生成音频与视频（据 LTX-2 论文）。
- 参数: up to 4K · up to 50 fps · up to 20 s · synchronized audio
- 能力维度: 感知真实感, 时间响应性, 创作可及性
- 论文: https://arxiv.org/abs/2601.03233 (arXiv 2026)
- 视频: https://www.youtube.com/watch?v=KRJW3yXwJdY
- 图片: https://cdn.prod.website-files.com/68872d15af29880764eac4aa/695b91d18b612de840f4786e_ltx-2-mode-open-graph.jpg
- 项目主页: https://ltx.io/model/ltx-2
- 代码: https://github.com/Lightricks/LTX-2

#### Ovi — Character.AI (2025-09-30)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 文字提示, 图像 → 输出: 平面视频, 语音 / 声音, 音效、音乐与空间音频
- 核心想法: 开源的音视频联合生成，让实验室无需闭源 API 就能研究口型同步的语音刺激。
- 内容: Character.AI 的 Ovi（2025-09-30）是一个开源模型，可一次生成 5 秒 720p 视频及其音频（语音、音效、音乐），是最早回应 Veo 3 式“会说话片段”的开源权重模型之一。
- 实现方式: 双主干设计：结构相同的音频与视频扩散 Transformer（视频分支由 Wan 2.2 初始化），逐块通过双向交叉注意力融合。
- 参数: 11B · 5 s · 720p · 24 fps
- 能力维度: 行为似真性, 感知真实感
- 论文: https://arxiv.org/abs/2510.01284 (arXiv 2025)
- 视频: https://aaxwaz.github.io/Ovi/assets/final_ovi_trailer.mp4
- 图片: https://aaxwaz.github.io/Ovi/assets/robot_red_eye.png
- 项目主页: https://aaxwaz.github.io/Ovi/
- 代码: https://github.com/character-ai/Ovi

#### 通义万相 2.2（Wan 2.2） — 阿里通义 (2025-07-28)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码, 公开 API
- 输入: 文字提示, 图像 → 输出: 平面视频
- 核心想法: 光线、镜头、构图等美学参数，在开源模型中变成明确且可复现的旋钮。
- 内容: 通义万相 Wan 2.2（2025-07-28）是首个开源的混合专家（MoE）视频模型，提供光照、色彩与构图等电影美学控制，其 50 亿参数版本可在单张消费级显卡上生成 720p 视频。
- 实现方式: 双专家 MoE 扩散模型（高噪声专家负责布局，低噪声专家负责细节；总参数 270 亿、激活 140 亿），另有高压缩比的 TI2V-5B 模型。
- 参数: A14B MoE · TI2V-5B · 720p · 24 fps
- 能力维度: 感知真实感, 实验控制, 创作可及性
- 视频: https://www.youtube.com/watch?v=ktDogWm7Hac
- 项目主页: https://wan.video/
- 代码: https://github.com/Wan-Video/Wan2.2

#### 通义万相 2.1（Wan 2.1） — 阿里通义 (2025-02-25)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码, 公开 API
- 输入: 文字提示, 图像, 视频 → 输出: 平面视频
- 核心想法: 2025 年的实时与控制研究大多以它为基础，因此不同实验室的结果可以相互迁移。
- 内容: 阿里巴巴的通义万相 Wan 2.1（2025-02-25 以 Apache 2.0 开源）提供 140 亿和 13 亿参数的文生/图生视频模型，小模型约需 8 GB 显存。它成为 VACE、Self Forcing、Krea Realtime 等众多研究与社区模型的基础。
- 实现方式: 以流匹配训练的扩散 Transformer，配合新的因果 3D VAE（Wan-VAE），可编码任意长度的 1080p 视频。
- 参数: 14B / 1.3B · 480p / 720p · 1.3B on 8.19 GB VRAM
- 能力维度: 创作可及性, 实验控制, 情境多样性
- 论文: https://arxiv.org/abs/2503.20314 (arXiv 2025)
- 视频: https://www.youtube.com/watch?v=2CObXv_CLyY
- 项目主页: https://wan.video/
- 代码: https://github.com/Wan-Video/Wan2.1

#### 阶跃 Step-Video-T2V（Step-Video-T2V） — 阶跃星辰 (2025-02-17)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 文字提示 → 输出: 平面视频
- 核心想法: 把开源模型规模推到 300 亿参数，并记录了视频扩散规模化的实际瓶颈。
- 内容: 阶跃星辰的 Step-Video-T2V（2025-02-17）是 300 亿参数的开源文生视频模型，可根据中文或英文提示生成最多 204 帧。
- 实现方式: 采用三维全注意力的 DiT，配深度压缩视频 VAE（空间 16×16、时间 8 倍），并用 Video-DPO 做偏好优化。
- 参数: 30B · 204 frames · 544×992
- 能力维度: 持久性, 感知真实感
- 论文: https://arxiv.org/abs/2502.10248 (arXiv 2025)
- 视频: https://github.com/user-attachments/assets/9274b351-595d-41fb-aba3-f58e6e91603a
- 项目主页: https://github.com/stepfun-ai/Step-Video-T2V
- 代码: https://github.com/stepfun-ai/Step-Video-T2V

#### 混元视频 HunyuanVideo（HunyuanVideo） — 腾讯混元 (2024-12-03)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码, 产品 / 应用
- 输入: 文字提示 → 输出: 平面视频
- 核心想法: 一度缩小了开源与闭源视频模型的质量差距，并带动了大量 LoRA 与控制适配器生态。
- 内容: 腾讯的 HunyuanVideo（2024-12-03）发布时是参数规模最大的开源视频模型（130 亿）；腾讯称其在专业人工评测中优于 Runway Gen-3 和 Luma 1.6。
- 实现方式: 从双流到单流的扩散 Transformer，配 3D 因果 VAE，并用多模态大语言模型作为文本编码器。
- 参数: 13B · 720p · 129 frames
- 能力维度: 感知真实感, 实验控制
- 论文: https://arxiv.org/abs/2412.03603 (arXiv 2024)
- 视频: https://github.com/user-attachments/assets/22440764-0d7e-438e-a44d-d0dad1006d3d
- 项目主页: https://github.com/Tencent-Hunyuan/HunyuanVideo
- 代码: https://github.com/Tencent-Hunyuan/HunyuanVideo

#### LTX-Video — Lightricks (2024-11-22)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码, 产品 / 应用
- 输入: 文字提示, 图像 → 输出: 平面视频
- 核心想法: 生成快于实时，是场景能对参与者作出反应的任何闭环的前提。
- 内容: Lightricks 的 LTX-Video（2024-11-22）是首个生成速度快于播放速度的开源视频模型：在 H100 上约 4 秒生成 5 秒 768×512 视频。13B 版本于 2025 年 5 月推出。
- 实现方式: 采用高压缩比 VAE（1:192）的 DiT，VAE 解码器同时完成最后一步去噪。
- 参数: 2B / 13B · 768×512 · 24 fps · faster than real time on H100
- 能力维度: 时间响应性, 创作可及性
- 论文: https://arxiv.org/abs/2501.00103 (arXiv 2024)
- 视频: https://www.youtube.com/watch?v=7ZMxtMyUD_U
- 项目主页: https://github.com/Lightricks/LTX-Video
- 代码: https://github.com/Lightricks/LTX-Video

#### Mochi 1 — Genmo (2024-10-22)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 文字提示 → 输出: 平面视频
- 核心想法: 宽松的许可使其成为学术微调与评测中常用的基础模型。
- 内容: Genmo 的 Mochi 1（2024-10-22）是 100 亿参数、Apache 2.0 许可的开源文生视频模型，运动质量与提示遵循在当时表现较强。
- 实现方式: 非对称扩散 Transformer（AsymmDiT），视频 VAE 压缩 128 倍，只用一个 T5-XXL 文本编码器。
- 参数: 10B · 480p · 30 fps · 5.4 s
- 能力维度: 行为似真性, 实验控制
- 视频: https://cdn.genmo.dev/results/mochi-launch.mp4
- 图片: https://www.genmo.ai/media/social/mochi1.png
- 项目主页: https://www.genmo.ai/blog/mochi-1-a-new-sota-in-open-text-to-video
- 代码: https://github.com/genmoai/mochi

#### CogVideoX（清影）（CogVideoX） — 智谱 (2024-08-06)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码, 产品 / 应用
- 输入: 文字提示, 图像 → 输出: 平面视频
- 核心想法: 证明开源模型能在单张消费级显卡上运行，并能被实验室按自身场景微调。
- 内容: 智谱的 CogVideoX（2024-08-06 开源）是国内实验室首个表现强劲的开源文生视频模型，可生成 6 秒 720×480 视频，也是智谱“清影”产品的底座。
- 实现方式: 带 3D 因果 VAE 的扩散 Transformer，用带专家自适应 LayerNorm 的“专家 Transformer”融合文本与视频 token。
- 参数: 2B / 5B · 6 s · 720×480 · 8 fps
- 能力维度: 创作可及性, 实验控制
- 论文: https://arxiv.org/abs/2408.06072 (ICLR 2025)
- 视频: https://github.com/user-attachments/assets/cf5953ea-96d3-48fd-9907-c4708752c714
- 项目主页: https://github.com/zai-org/CogVideo
- 代码: https://github.com/zai-org/CogVideo

#### Stable Video Diffusion — Stability AI (2023-11-21)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像 → 输出: 平面视频
- 核心想法: 为研究者提供了可微调的视频先验，后来许多三维、四维生成方法都从 SVD 权重起步。
- 内容: Stable Video Diffusion（2023-11-21）是首个被广泛使用的开源图生视频模型，可把一张静态图变成 14 或 25 帧短片，也被用作多视角三维生成的基础模型。
- 实现方式: 在 Stable Diffusion 2.1 上加入时间层的潜空间视频扩散模型，分三阶段训练：图像预训练、精选视频预训练和高质量微调。
- 参数: 576×1024 · 14 / 25 frames · 3–30 fps
- 能力维度: 创作可及性, 实验控制
- 论文: https://arxiv.org/abs/2311.15127 (arXiv 2023)
- 图片: https://static1.squarespace.com/static/6213c340453c3f502425776e/62f2452bc121595f4d87c713/655c90f932dda45e84c36b21/1728899860281/SVD+blog+cover+image.jpg?format=1500w
- 项目主页: https://stability.ai/news/stable-video-diffusion-open-ai-video-model
- 代码: https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt

### 控制、编辑与角色

镜头路径、动作迁移、参考角色、视频到视频编辑与表演驱动的动画。

#### 可灵 O1（Kling O1） — 快手 / 可灵 (2025-12-01)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 产品 / 应用, 公开 API
- 输入: 文字提示, 图像, 视频 → 输出: 平面视频
- 核心想法: 一个模型同时负责“拍摄”和“剪辑”，场景可以按指令迭代，而角色保持不变。
- 内容: 可灵 O1（2025-12-01）号称首个统一视频模型，在一个多模态提示中同时完成生成、基于参考的创作和视频编辑（替换主体、改变风格、更换镜头）。
- 实现方式: 多模态视觉-语言主干驱动扩散视频生成器，详见 Kling-Omni 技术报告。
- 能力维度: 实验控制, 共创与能动性, 创作可及性
- 论文: https://arxiv.org/abs/2512.16776 (arXiv 2025)
- 视频: https://www.youtube.com/watch?v=V_oiFFTpxHs
- 项目主页: https://kling.ai/
- API 文档: https://app.klingai.com/global/dev

#### 通义万相 Wan-Animate（Wan-Animate） — 阿里通义 (2025-09-17)
- 类型: 开源工具 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像, 视频 → 输出: 平面视频, 虚拟人（脸 / 身体）
- 核心想法: 开源的表演迁移：任何录下的演员表演，都能在实验室自己的 GPU 上驱动任意角色。
- 内容: Wan-Animate（2025 年 9 月）可用驱动视频中的身体动作与面部表情来驱动一张角色图，或把视频中的人替换成该角色并匹配场景光照；权重以 Wan2.2-Animate-14B 开源。
- 实现方式: 基于 Wan 2.2，用骨架信号控制身体动作，用隐式面部特征控制表情，并用重光照 LoRA 完成角色替换。
- 参数: 14B
- 能力维度: 行为似真性, 实验控制
- 论文: https://arxiv.org/abs/2509.14055 (arXiv 2025)
- 视频: https://humanaigc.github.io/wan-animate/content/aa/rep_shots.mp4
- 图片: https://humanaigc.github.io/wan-animate/content/aa/arch.png
- 项目主页: https://humanaigc.github.io/wan-animate/
- 代码: https://huggingface.co/Wan-AI/Wan2.2-Animate-14B

#### Runway Aleph — Runway (2025-07-25)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 产品 / 应用, 公开 API
- 输入: 视频, 文字提示, 图像 → 输出: 平面视频
- 核心想法: 按指令编辑真实视频，研究者可以只改变一个因素（光照、道具、天气），而录制场景的其余部分保持不变。
- 内容: Aleph（2025-07-25）是 Runway 的上下文视频编辑模型：给定已有画面，它能增删物体，改变光照、天气或季节，转换风格，或为同一场景生成新的机位；Aleph 2.0 于 2026-05-21 发布。
- 实现方式: 以输入视频加文本或图像指令为条件的上下文视频模型；架构未公开。
- 能力维度: 实验控制, 共创与能动性, 创作可及性
- 视频: https://www.youtube.com/watch?v=KUHx-2uz_qI
- 图片: https://d3phaj0sisr2ct.cloudfront.net/site/content/images/rw-card-aleph.jpg
- 项目主页: https://runwayml.com/research/introducing-runway-aleph
- API 文档: https://docs.dev.runwayml.com/

#### Act-Two — Runway (2025-07-15)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 产品 / 应用, 公开 API
- 输入: 视频, 图像 → 输出: 平面视频, 虚拟人（脸 / 身体）
- 核心想法: 人的表演录像成为控制信号：只需演一遍，就能把同一段行为套到许多不同角色身上。
- 内容: Act-Two（2025-07-15）可把演员录制的表演（面部、头部、身体与手部）迁移到任意角色图像或视频上，是只驱动面部的 Act-One（2024 年 10 月）的后继。
- 实现方式: 以驱动视频与角色参考为输入的表演驱动视频生成；架构未公开。
- 能力维度: 实验控制, 行为似真性, 创作可及性
- 视频: https://www.youtube.com/watch?v=JW8PHlFD7HM
- 项目主页: https://runwayml.com/research
- API 文档: https://docs.dev.runwayml.com/

#### ReCamMaster — Jianhong Bai, 快手 / 可灵 (2025-03-14)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 视频, 镜头路径 / 位姿 → 输出: 平面视频
- 核心想法: 从新角度“重拍”已录下的事件，是不经三维采集就迈向自由视点视频的一步。
- 内容: ReCamMaster（2025-03-14，浙江大学与快手可灵团队）可沿新的镜头轨迹重新渲染已有视频，从不同视角呈现同一动态场景。
- 实现方式: 在帧维度拼接源视频，以此条件化预训练文生视频模型；训练数据是用虚幻引擎 5 渲染的多机位同步数据集。
- 能力维度: 实验控制, 情境可达性
- 论文: https://arxiv.org/abs/2503.11647 (arXiv 2025)
- 视频: https://jianhongbai.github.io/ReCamMaster/videos/ReCamMaster/TEASER_compressed.mp4
- 图片: https://jianhongbai.github.io/ReCamMaster/pics/fig_pipe.png
- 项目主页: https://jianhongbai.github.io/ReCamMaster/
- 代码: https://github.com/KwaiVGI/ReCamMaster

#### VACE — 阿里通义 (2025-03-10)
- 类型: 开源工具 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 视频, 图像, 文字提示 → 输出: 平面视频
- 核心想法: 在一个开源模型中组合姿态、深度、遮罩与参考条件，实验室可以对生成刺激进行细粒度、可复现的控制。
- 内容: VACE（论文 2025-03-10；2025 年 5 月基于 Wan 2.1 开源权重）是阿里巴巴的一体化模型，涵盖参考生视频、视频到视频和遮罩编辑：用同一个网络移动、替换、扩展或驱动片段中的任意对象。
- 实现方式: 用视频条件单元（VCU）把文本、帧和遮罩打包成统一输入，经上下文适配器（Context Adapter）注入扩散 Transformer。
- 参数: 1.3B / 14B (Wan 2.1-based)
- 能力维度: 实验控制, 创作可及性
- 论文: https://arxiv.org/abs/2503.07598 (ICCV 2025)
- 视频: https://ali-vilab.github.io/VACE-Page/assets/videos/SwapAnything_1.mp4
- 项目主页: https://ali-vilab.github.io/VACE-Page/
- 代码: https://github.com/ali-vilab/VACE

### 实时与长视频

因果、自回归与蒸馏模型：实时流式生成视频，或持续生成数分钟。

#### Vidu S1 — 生数科技（Vidu） (2026-07-03)
- 类型: 模型 · 时序: 实时流式 · 获取方式: 产品 / 应用
- 输入: 语音与音频, 文字提示, 图像 → 输出: 交互式帧流, 语音 / 声音
- 核心想法: 跟得上对话节奏的视频生成，把视频模型带进了虚拟人的轮流对话循环。
- 内容: Vidu S1（2026-07-03）是生数科技的实时交互视频模型：你对它说话时，生成的角色或场景会在毫秒级作出回应，可用于“会说话的宠物”、游戏陪伴等场景。
- 实现方式: 以流式语音输入为条件的实时视频生成；架构未公开。
- 能力维度: 时间响应性, 反应性, 行为似真性
- 视频: https://www.youtube.com/watch?v=jaPLmykNk0I
- 项目主页: https://www.vidu.com/

#### Helios — Shenghai Yuan (2026-03-04)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 文字提示, 图像 → 输出: 交互式帧流
- 核心想法: 实时不再意味着只能用 13 亿参数的小模型：质量与响应速度不必二选一。
- 内容: Helios（北京大学与字节跳动，2026 年 3 月）是 140 亿参数的开源模型，可在单张 H100 上实时生成分钟级视频，表明大规模实时模型在速度上也能追平小模型。
- 实现方式: 自回归视频扩散，结合长时稳定性与高效推理技术（据 Helios 论文）。
- 参数: 14B · real-time on 1 H100 · minute-scale (reported)
- 能力维度: 时间响应性, 持久性, 感知真实感
- 论文: https://arxiv.org/abs/2603.04379 (arXiv 2026)
- 视频: https://www.youtube.com/watch?v=vd_AgHtOUFQ
- 图片: https://pku-yuangroup.github.io/Helios-Page/figures/highlight_speed_v2.png
- 项目主页: https://pku-yuangroup.github.io/Helios-Page/
- 代码: https://github.com/PKU-YuanGroup/Helios

#### Lucy 2 — Decart (2026-01-26)
- 类型: 模型 · 时序: 实时流式 · 获取方式: 公开 API, 产品 / 应用
- 输入: 视频, 文字提示, 图像 → 输出: 交互式帧流
- 核心想法: 基于参考图对人的实时画面进行变换，是构建生成式混合现实实验条件的基本模块。
- 内容: Decart 的 Lucy 2（2026-01-26）能以 1080p、30 fps、近乎零延迟编辑实时视频流，依据文本和参考图完成角色替换、换装、植入商品乃至整体环境变换；Lucy 2.5（2026-07-16）提升了时间稳定性。
- 实现方式: 在 MirageLSD 与 Lucy Edit 基础上构建的实时“世界变换”视频模型；Decart 称其无需深度图或三维信息即可学到物理一致性。
- 参数: 1080p · 30 fps · near-zero latency (claimed)
- 能力维度: 时间响应性, 反应性, 共创与能动性
- 视频: https://www.youtube.com/watch?v=N82RN4dPKaM
- 图片: https://cdn.prod.website-files.com/69a974f0b1fffb03644ecf2c/6a4d10c78242cf13741618a1_lucy-og.jpg
- 项目主页: https://decart.ai/publications/lucy-2-introducing-sota-video-generation-in-realtime

#### Krea Realtime 14B — Krea (2025-10-15)
- 类型: 模型 · 时序: 实时流式 · 获取方式: 开源权重 / 代码, 产品 / 应用
- 输入: 文字提示, 视频 → 输出: 交互式帧流
- 核心想法: 140 亿参数规模的实时生成表明，交互性不再必须以小而粗糙的模型为代价。
- 内容: Krea Realtime 14B（2025-10-15）是从 Wan 2.1 14B 蒸馏而来的开源文生视频模型，在单张 B200 上约 11 fps 流式生成，用户可在生成过程中更换提示或重绘画面风格。
- 实现方式: 用 Self Forcing 把 140 亿参数的双向模型蒸馏为自回归模型，并用 KV 缓存重算与注意力偏置抑制误差累积。
- 参数: 14B · ~11 fps on 1 B200 · ~1 s to first frame
- 能力维度: 时间响应性, 共创与能动性
- 视频: https://s.krea.ai/krea-rt-video-blog/prompt_003.mp4
- 图片: https://s.krea.ai/krea_realtime_14b_cover.webp
- 项目主页: https://www.krea.ai/blog/krea-realtime-14b
- 代码: https://huggingface.co/krea/krea-realtime-video

#### LongLive — Shuai Yang, 英伟达 (2025-09-26)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 文字提示 → 输出: 交互式帧流
- 核心想法: 一个正在进行、听指令就能改变的场景，是可导演情境的核心。
- 内容: LongLive（NVIDIA、MIT、港科大（广州）等，2025 年 9 月）可实时生成最长 4 分钟的视频，用户能在生成过程中随时输入新提示，画面会平滑过渡。
- 实现方式: 帧级自回归模型，切换提示时重建 KV 缓存，采用流式长视频微调和带帧汇聚（frame sink）的短窗口注意力。
- 参数: 1.3B · 20.7 fps (H100) · up to 240 s
- 能力维度: 时间响应性, 适应性, 持久性
- 论文: https://arxiv.org/abs/2509.22622 (ICLR 2026)
- 视频: https://www.youtube.com/watch?v=CO1QC7BNvig
- 图片: https://nvlabs.github.io/LongLive/assets/streaming_long.jpg
- 项目主页: https://nvlabs.github.io/LongLive/
- 代码: https://github.com/NVlabs/LongLive

#### MirageLSD — Decart (2025-07-17)
- 类型: 模型 · 时序: 实时流式 · 获取方式: 产品 / 应用, 公开 API
- 输入: 视频, 文字提示 → 输出: 交互式帧流
- 核心想法: 对现实世界实时“换皮”，是通向混合现实情境最直接的生成路径，前提是转换保持稳定。
- 内容: Decart 的 MirageLSD（2025-07-17）可按提示把任意实时摄像头、游戏或视频画面实时转换成另一种风格或世界（Decart 称延迟低于 40 毫秒、24 fps）；以网页演示和手机应用形式发布，后由 Lucy 2 接替。
- 实现方式: 实时流扩散（Live-Stream Diffusion）：逐帧因果视频扩散模型，借助扩散强制与历史增强抵抗误差累积，并使用定制 GPU 内核。
- 参数: 24 fps · < 40 ms latency (claimed)
- 能力维度: 时间响应性, 反应性, 共创与能动性
- 视频: https://cdn.prod.website-files.com/6874f65b561c843511ee5b85%2F68791e9e65a7de52792e9cdf_mirage-transcode.mp4
- 图片: https://cdn.prod.website-files.com/6875c2f7957701899283e82a/68793def662cebbb07fd8940_image.png
- 项目主页: https://web.archive.org/web/20250801/https://decart.ai/publications/mirage

#### Seaweed APT2 — 字节跳动 Seed (2025-06-11)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入: 文字提示, 图像, 镜头路径 / 位姿 → 输出: 交互式帧流
- 核心想法: 每帧只需一次网络前向，视频便能像游戏引擎一样响应输入，至少能持续一分钟。
- 内容: 字节跳动 Seed 的 Seaweed APT2（2025 年 6 月）在单张 H100 上以 24 fps 流式生成 736×416 视频，最长约一分钟，可通过镜头运动实时操控，其虚拟人演示中还能由人体姿态驱动。
- 实现方式: 自回归对抗后训练（AAPT）：把预训练视频扩散模型改造为每次网络前向生成一个潜帧，并在长序列上以学生强制方式进行对抗训练。
- 参数: 8B · 24 fps · 736×416 · up to 1,440 frames (1 min)
- 能力维度: 时间响应性, 反应性, 持久性
- 论文: https://arxiv.org/abs/2506.09350 (arXiv 2025)
- 视频: https://cdn.seaweed-apt.com/apt2/highres/man-helmet.mp4
- 图片: https://cdn.seaweed-apt.com/apt2/misc/teaser.jpg
- 项目主页: https://seaweed-apt.com/2

#### Self Forcing — Xun Huang, Adobe (2025-06-09)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 文字提示 → 输出: 交互式帧流
- 核心想法: 成为 LongLive、Krea Realtime 等实时视频模型常用的训练方法。
- 内容: Self Forcing（Adobe Research 与 UT Austin，2025 年 6 月）让自回归视频模型在自身的生成结果上训练，弥合训练与推理的差距，在单张 H100 上以约 17 fps、亚秒级延迟流式生成视频。
- 实现方式: 训练时就用 KV 缓存进行自回归展开，以整段视频级的分布匹配损失优化，并用滚动 KV 缓存外推更长视频。
- 参数: 1.3B · ~17 fps · < 1 s latency (H100)
- 能力维度: 时间响应性, 持久性
- 论文: https://arxiv.org/abs/2506.08009 (arXiv 2025)
- 视频: https://github.com/user-attachments/assets/7548c2db-fe03-4ba8-8dd3-52d2c6160739
- 图片: https://self-forcing.github.io/static/teaser.jpg
- 项目主页: https://self-forcing.github.io/
- 代码: https://github.com/guandeh17/Self-Forcing

#### MAGI-1 — Sand AI (2025-04-21)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 文字提示, 图像, 视频 → 输出: 平面视频
- 核心想法: 分块自回归让人能逐秒控制场景如何展开。
- 内容: Sand AI 的 MAGI-1（2025-04-21）是 240 亿参数的开源自回归视频模型，逐块生成视频，支持流式输出、无限延展和逐块更换提示。
- 实现方式: 以 24 帧为一块进行自回归去噪，越靠后的块噪声越高、前面的块逐步细化，配合基于 Transformer 的 VAE。
- 参数: 24B (4.5B distilled) · 24-frame chunks
- 能力维度: 持久性, 实验控制
- 论文: https://arxiv.org/abs/2505.13211 (arXiv 2025)
- 视频: https://www.youtube.com/watch?v=RauucR3jmo0
- 图片: https://repository-images.githubusercontent.com/970023948/34ab6cc2-a578-4398-8f10-be2bffa59fa4
- 项目主页: https://github.com/SandAI-org/MAGI-1
- 代码: https://github.com/SandAI-org/MAGI-1

#### SkyReels-V2 — 昆仑万维 Skywork (2025-04-21)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 文字提示, 图像 → 输出: 平面视频
- 核心想法: 扩散强制（diffusion forcing）把片段模型变成连续讲故事的模型，但时长到数分钟时漂移仍会累积。
- 内容: 昆仑万维 Skywork 的 SkyReels-V2（2025 年 4 月）是开源的“无限时长电影”模型，可在保持镜头一致的同时不断延展视频，训练时使用了电影语法标注。
- 实现方式: 采用扩散强制框架（每个 token 噪声水平不同），用多模态字幕模型 SkyCaptioner 标注镜头语言，并用强化学习提升运动质量。
- 参数: 1.3B / 14B · 540p / 720p · unlimited length
- 能力维度: 持久性, 创作可及性
- 论文: https://arxiv.org/abs/2504.13074 (arXiv 2025)
- 视频: https://github.com/user-attachments/assets/f6f9f9a7-5d5f-433c-9d73-d8d593b7ad25
- 项目主页: https://github.com/SkyworkAI/SkyReels-V2
- 代码: https://github.com/SkyworkAI/SkyReels-V2

#### FramePack — 张吕敏 (2025-04-17)
- 类型: 开源工具 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像, 文字提示 → 输出: 平面视频
- 核心想法: 无论视频多长，显存占用都恒定，普通硬件也能生成长镜头。
- 内容: FramePack（斯坦福的张吕敏与 Maneesh Agrawala，2025 年 4 月）把历史帧压缩进固定大小的上下文，从而在 6 GB 显存的笔记本 GPU 上生成 1–2 分钟的图生视频。
- 实现方式: 下一帧段预测，配合渐进式上下文打包（越早的帧分到越少的 token）和防漂移的双向采样，以 HunyuanVideo 为主干。
- 参数: 13B · 30 fps · 60–120 s · 6 GB VRAM
- 能力维度: 持久性, 创作可及性
- 论文: https://arxiv.org/abs/2504.12626 (arXiv 2025)
- 视频: https://lllyasviel.github.io/frame_pack_gitpage/long/250415_173937_297_5230_451.mp4
- 图片: https://lllyasviel.github.io/frame_pack_gitpage/img/sample.png
- 项目主页: https://lllyasviel.github.io/frame_pack_gitpage/
- 代码: https://github.com/lllyasviel/FramePack

#### CausVid — Tianwei Yin, Adobe (2024-12-10)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 文字提示, 图像 → 输出: 交互式帧流
- 核心想法: 按下生成就开始播放的视频，是离线片段与可实时操控视频流之间的转折点。
- 内容: CausVid（MIT 与 Adobe，2024 年 12 月）把缓慢的双向视频扩散模型转换为因果模型，在单张 GPU 上约 1.3 秒后即可开始以约 9 fps 流式输出画面。
- 实现方式: 用分布匹配蒸馏，把双向教师模型蒸馏成 4 步、块因果注意力并带 KV 缓存的自回归学生模型。
- 参数: 9.4 fps streaming · ~1.3 s first-frame latency
- 能力维度: 时间响应性, 持久性
- 论文: https://arxiv.org/abs/2412.07772 (CVPR 2025)
- 视频: https://www.youtube.com/watch?v=nXAT18XuEKc
- 项目主页: https://causvid.github.io/
- 代码: https://github.com/tianweiy/CausVid

#### StreamDiffusion — Akio Kodaira (2023-12-19)
- 类型: 开源工具 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 视频, 文字提示 → 输出: 交互式帧流
- 核心想法: 对实时摄像头画面逐帧扩散，是第一个能在当下改变人所见画面的实用方案。
- 内容: StreamDiffusion（2023-12-19）可用 Stable Diffusion 实时重绘摄像头或屏幕画面，在单张 RTX 4090 上最高约 90 fps，成为许多 TouchDesigner 与现场表演装置的引擎；StreamDiffusionV2（2025 年 11 月）把它扩展到视频扩散模型。
- 实现方式: 围绕 SD-Turbo、LCM 等少步模型的流水线级优化：去噪步的流式批处理、残差无分类器引导、随机相似度过滤。
- 参数: up to 91 fps img2img on RTX 4090 (reported)
- 能力维度: 时间响应性, 反应性
- 论文: https://arxiv.org/abs/2312.12491 (arXiv 2023)
- 视频: https://www.youtube.com/watch?v=I9Eq4LoB7Wk
- 图片: https://raw.githubusercontent.com/cumulo-autumn/StreamDiffusion/main/assets/demo_07.gif
- 项目主页: https://github.com/cumulo-autumn/StreamDiffusion
- 代码: https://github.com/cumulo-autumn/StreamDiffusion

#### Phenaki — 谷歌 (2022)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 文字提示 → 输出: 平面视频
- 核心想法: 首次勾勒出由故事驱动、可切换提示的视频流，这一想法后来被 LongLive 等实时模型做成了交互式。
- 内容: Phenaki（Google，2022-10-05）可根据随时间变化的一串提示生成可变长度、最长数分钟的视频，例如逐镜讲述一个故事。
- 实现方式: 用 C-ViViT 把视频压缩为离散 token，再由以文本为条件的双向掩码 Transformer 在时间维度上自回归生成。
- 参数: variable length · minutes (prompt sequences)
- 能力维度: 持久性, 适应性
- 论文: https://arxiv.org/abs/2210.02399 (ICLR 2023)
- 视频: https://www.youtube.com/watch?v=Uf_xSjL0Bh8
- 项目主页: https://phenaki.github.io/

### 全景、立体与空间视频

面向头显的 360°、立体与空间视频生成，以及 2D 转 3D。

#### 360Anything：无需几何的图像与视频 360° 提升（360Anything） — Ziyi Wu, 谷歌 DeepMind (2026-01-22)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 图像, 视频 → 输出: 360° / 立体视频, 图像 / 全景图
- 核心想法: 任何生成片段，哪怕是世界模型的推演画面，都可以事后“包裹”到观看者四周。
- 内容: 360Anything（Google DeepMind 与多伦多大学，ECCV 2026）无需相机标定，就能把任意透视图像或视频（包括 Genie 3 世界模型的画面）提升为无缝的 360° 全景。
- 实现方式: 无需几何先验的扩散 Transformer，从数据中学习透视输入在全景中的位置，不依赖显式的相机内外参。
- 能力维度: 情境可达性, 情境多样性
- 论文: https://arxiv.org/abs/2601.16192 (ECCV 2026)
- 视频: https://360anything.github.io/videos/video_360_viewer/genie_3_concat.mp4
- 图片: https://360anything.github.io/imgs/image_360_viewer/lighthouse_ours.png
- 项目主页: https://360anything.github.io/

#### StereoPilot — Guibao Shen, 快手 / 可灵 (2025-12-18)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 视频 → 输出: 360° / 立体视频
- 核心想法: 快速且区分立体格式的转换，让实验室无需重新渲染就能把生成场景投放到不同头显上。
- 内容: StereoPilot（港科大（广州）与快手可灵团队，2025 年 12 月）借助生成式视频先验，一次高效推理即可把单目视频转换为平行式或会聚式两种立体格式。
- 实现方式: 基于视频生成主干的统一前馈式立体转换，在涵盖平行与会聚两种立体格式的数据集上训练。
- 能力维度: 情境可达性, 感知真实感
- 论文: https://arxiv.org/abs/2512.16915 (arXiv 2025)
- 视频: https://hit-perfect.github.io/StereoPilot/Video_Intro/StereoPilot.mp4
- 图片: https://hit-perfect.github.io/StereoPilot/Figs/PacificRim.gif
- 项目主页: https://hit-perfect.github.io/StereoPilot/
- 代码: https://github.com/KlingTeam/StereoPilot

#### Imagine360：从透视锚点生成沉浸式 360 视频（Imagine360） — Jing Tan (2024-12-04)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 视频 → 输出: 360° / 立体视频
- 核心想法: 把手机拍下的事件画面变成参与者可以环顾的环绕素材。
- 内容: Imagine360（香港中文大学与上海人工智能实验室，NeurIPS 2025）可把普通透视视频扩展成完整的 360° 视频，在保留原有运动的同时补全画框之外的周边环境。
- 实现方式: 透视/全景双分支扩散，配合对跖遮罩（antipodal mask）与仰角感知设计，在全景视频上训练。
- 能力维度: 情境可达性, 感知真实感
- 论文: https://arxiv.org/abs/2412.03552 (NeurIPS 2025)
- 视频: https://www.youtube.com/watch?v=gRGo4B41GXY
- 项目主页: https://ys-imtech.github.io/projects/Imagine360/
- 代码: https://github.com/YS-IMTech/Imagine360

#### StereoCrafter：单目视频生成长时高保真立体 3D（StereoCrafter） — Sijie Zhao, 腾讯 ARC 实验室 (2024-09-11)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 视频 → 输出: 360° / 立体视频
- 核心想法: 任何现有或生成的片段都能转成立体视频，是从平面刺激走向头显刺激成本最低的路径。
- 内容: StereoCrafter（腾讯 ARC 实验室，2024 年 9 月）可把普通 2D 视频转换为长时、高保真的立体 3D 视频，供 Apple Vision Pro 等头显观看，并用视频扩散模型补全视差暴露出的遮挡区域。
- 实现方式: 先基于深度做前向变换得到第二视角，再用在大规模立体视频上训练的扩散修补模型填补空洞。
- 能力维度: 情境可达性, 感知真实感
- 论文: https://arxiv.org/abs/2409.07447 (arXiv 2024)
- 视频: https://github.com/stereocrafter/stereocrafter.github.io/releases/download/V0.0.1/camel_sbs.mp4
- 项目主页: https://stereocrafter.github.io/
- 代码: https://github.com/TencentARC/StereoCrafter

#### 360DVD：可控全景视频生成（360DVD） — Qian Wang (2024-01-12)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 文字提示 → 输出: 360° / 立体视频
- 核心想法: 最早能生成可环顾四周的环绕视频（而不是一个画框）的方法之一。
- 内容: 360DVD（北京大学，CVPR 2024）可从文字生成 360° 等距柱状全景视频，并可加入运动条件，供 VR 头显观看。
- 实现方式: 在预训练文生视频模型上加入轻量的 360-Adapter 及针对 360° 的增强技术，使用 WEB360 全景视频数据集训练。
- 参数: equirectangular · 512×1024
- 能力维度: 情境可达性, 情境多样性
- 论文: https://arxiv.org/abs/2401.06578 (CVPR 2024)
- 视频: https://akaneqwq.github.io/360DVD/static/videos/01-vr.mp4
- 图片: https://akaneqwq.github.io/360DVD/static/images/framework.webp
- 项目主页: https://akaneqwq.github.io/360DVD/
- 代码: https://github.com/akaneqwq/360DVD

## 交互式虚拟人

为对话实时生成的脸和身体：边听边说的视频虚拟人、音频驱动的人像、照片级三维化身，以及非语言行为模型。

### 实时对话视频

以视频形式呈现的全双工视听智能体：Tavus、HeyGen、D-ID、Character.AI、Anam、Hedra 等。

#### Griffin 人类交互模型（Griffin） — Tavus (2026-10-01)
- 类型: 模型 · 时序: 全双工 · 获取方式: 候补 / 抢先体验
- 输入: 视频, 语音与音频 → 输出: 虚拟人（脸 / 身体）, 语音 / 声音, 对话 / 文本
- 核心想法: 第一个边说边听、可被打断、会在对方说话时点头的商用虚拟人，让面对面的时机本身成为可生成、可研究的变量。
- 内容: Griffin 是一个面向视频通话的全双工视频到视频模型：它同时看和听对方，每隔不到一秒判断该说话、停顿、附和还是让出话轮，并从一张参考图像实时生成语音和 720p 画面中人物的每一个像素。Tavus 报告称，在一分钟的通话中有 48% 的参与者认为对方是真人；截至 2026 年 10 月，Griffin-Lite 仅以研究预览形式向部分测试者开放。
- 实现方式: 一个连续对话模型以亚秒间隔读取输入的音视频并输出文本和控制信号；随后由流式自回归扩散语音生成器（基于 48 kHz 连续编解码器）和经 DMD2、teacher forcing 与 Self-Forcing 蒸馏的少步因果视频 DiT 渲染回应。
- 参数: 720p · real time · 0.43 s avg audio-to-video latency (H100) · 48% judged human in 1-min calls · VideoFDB generation 3.83 (human 3.92)
- 能力维度: 时间响应性, 行为似真性, 感知真实感
- 视频: https://www.youtube.com/watch?v=lHw6yoyPkpo
- 图片: https://cdn.prod.website-files.com/68c8e57d6e512b9573db146f/6abe6c84125e80a50a54a217_Griffin%20OG%20v3%20%E2%80%94%2003%20Split%20%C2%B7%20Type%20Left.jpg
- 项目主页: https://www.tavus.io/griffin
- API 文档: https://docs.tavus.io

#### Sessions 交互虚拟人会话（Sessions (Interactive Avatars)） — Synthesia (2026-10-01)
- 类型: 产品 / 应用 · 时序: 回合制 · 获取方式: 产品 / 应用, 公开 API
- 输入: 语音与音频 → 输出: 虚拟人（脸 / 身体）, 语音 / 声音, 对话 / 文本
- 核心想法: 主流培训厂商开始销售与会回应的虚拟人进行可打分的角色扮演，这正是模拟训练中“刻意练习”循环的企业级版本。
- 内容: Sessions 是 Synthesia 用于与实时虚拟人双向对话的平台：Roleplay Sessions（2026 年 7 月首发）让员工与会“反驳”的虚拟人演练销售、辅导或客服对话，结束后由 AI 打分并反馈；Survey Sessions 把问卷变成口头访谈。Interactive Avatars API 向开发者开放同一套虚拟人。
- 实现方式: 很可能是级联方案（语音识别、大模型情境提示、语音合成和 Synthesia 的实时虚拟人渲染器），另有一个大模型教练对对话记录评分。
- 能力维度: 情境可达性, 创作可及性, 适应性
- 视频: https://www.youtube.com/watch?v=vcYBbtFejmg
- 图片: https://cdn.prod.website-files.com/65e89895c5a4b8d764c0d70e/6abd354ed0f78074501e8826_GTM_Sessions_Blog-Header_V1.png
- 项目主页: https://www.synthesia.io/post/sessions-interactive-avatar-platform
- API 文档: https://www.synthesia.io/features/avatars/interactive-avatars

#### Gemini 3.8 Live 实时虚拟人（Live Avatar）（Gemini 3.8 Live with Live Avatar） — 谷歌 DeepMind (2026-09-24)
- 类型: 产品 / 应用 · 时序: 回合制 · 获取方式: 产品 / 应用, 公开 API
- 输入: 语音与音频, 视频, 图像 → 输出: 虚拟人（脸 / 身体）, 语音 / 声音, 对话 / 文本
- 核心想法: 前沿实验室的虚拟人在发布时就内置了溯源标识：生成的每一帧画面和每一句话都带水印，这对需要披露“对话者是合成的”研究很重要。
- 内容: Live Avatar 把 Google 的 Gemini 3.8 Live 对话模型与近实时视频生成结合起来，让企业智能体以一个会说话的角色出现：它能看到和听到用户，在 97 种语言间（可在对话中途切换）保持口型同步，并在后台调用工具时继续对话。它已在 Gemini Enterprise 中提供预设虚拟人；用参考图像定制虚拟人仅向白名单企业开放，所有音频和视频都带有 SynthID 水印。
- 实现方式: Gemini 3.8 Live 原生音频对话（音视频输入、语音输出）与低延迟流式视频生成器原生耦合；轮流发言由 Live 模型处理，像 Live API 一样支持打断（Google 的描述是“流畅的轮流发言”，而非重叠说话）。
- 参数: 97 languages · near-real-time streaming video · SynthID in audio and video
- 能力维度: 时间响应性, 感知真实感, 实验控制
- 视频: https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/GLA-Video_3_compression.mp4
- 图片: https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Slide_16_9_-_37.width-1300.png
- 项目主页: https://deepmind.google/blog/introducing-gemini-38-live-with-live-avatar/
- API 文档: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/live-api

#### 角色世界模型 CWM-1（Character World Model-1 (CWM-1)） — LemonSlice (2026-09-23)
- 类型: 模型 · 时序: 实时流式 · 获取方式: 产品 / 应用, 公开 API
- 输入: 语音与音频, 图像, 文字提示 → 输出: 虚拟人（脸 / 身体）, 交互式帧流
- 核心想法: 把虚拟人看作以角色为中心的小型世界模型，肢体语言和与物体的互动都是生成出来的，而不是靠绑定动画。
- 内容: CWM-1 只需任意角色（真人、动漫、动物）的一张图像，就能生成整个实时视频通话画面：脸、身体、手、头发和周围环境；其情绪引擎会触发耸肩、前倾、拿起手机等动作。它接替了 2025 年 12 月发布的 LemonSlice-2（一个在单 GPU 上以 20 fps 运行的 20B 因果模型）。
- 实现方式: 一个因果、少步的视频扩散 Transformer，以音频、提示词以及独立情绪引擎（读取对话内容）预测的动作/情绪状态为条件。
- 参数: LemonSlice-2: 20B params · 20 fps on 1 GPU · 471 ms p99 latency (platform)
- 能力维度: 行为似真性, 实验控制, 情境多样性
- 视频: https://lemonslice.com/cwm-1/header/header-1.webm
- 图片: https://lemonslice.com/cwm-1/launch.webp
- 项目主页: https://lemonslice.com/cwm-1
- API 文档: https://lemonslice.com/docs

#### AVTR-1：实时交互虚拟人开源方案（AVTR-1） — Avaturn Live (2026-09-19)
- 类型: 开源工具 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 语音与音频, 图像 → 输出: 虚拟人（脸 / 身体）, 动作 / 动画
- 核心想法: 为实时虚拟人的底层管线提供开放、可测量的参照，还给出一个检验倾听者动作是否真的依赖对方说话的指标（R-DGG）。
- 内容: AVTR-1 是一个开源的实时虚拟人对话方案：一个小型动作生成器同时听用户和语音智能体的声音，再由渲染器和服务后端把结果变成同步的音视频流，并能处理打断。模型权重、渲染器和后端均按各组件的许可证发布。
- 实现方式: 一个 1.53 亿参数的自回归流匹配动作生成器，以双方音频为条件，配合自蒸馏的流式音频编码器，并对用户可感知的延迟给出解析上界。
- 参数: 153M-param motion model · real time on data-center and consumer GPUs
- 能力维度: 时间响应性, 实验控制
- 论文: https://arxiv.org/abs/2609.22913 (arXiv 2026)
- 视频: https://avaturn-live.github.io/avtr-1-projectpage/media/pair_V00_S2019_I00001095.mp4
- 图片: https://avtr-1.avaturn.live/media/og-preview.png
- 项目主页: https://avaturn-live.github.io/avtr-1-projectpage/
- 代码: https://github.com/avaturn-live/avtr-1

#### FacePlex：全双工对话虚拟人（FacePlex） — Habin Lim (2026-06-29)
- 类型: 研究演示 · 时序: 全双工 · 获取方式: 仅限研究
- 输入: 语音与音频, 文字提示 → 输出: 虚拟人（脸 / 身体）, 语音 / 声音
- 核心想法: 说明全双工的脸需要预判自己将要说的话，而不只是跟着语音动。
- 内容: FacePlex 在用户说话的同时逐 token 地联合生成对话虚拟人的语音和面部动作，在对应音频发出之前就准备好口型，并加入与对话内容相关的非语言反应，最后用高斯泼溅渲染。
- 实现方式: 一个统一的流式框架，把语音 token、面部动作 token 和高斯泼溅渲染放在同一条时间线上，基于全双工语音对话模型构建。
- 参数: 122 ms end-to-end avatar interaction latency
- 能力维度: 时间响应性, 行为似真性
- 论文: https://arxiv.org/abs/2606.30145 (arXiv 2026)
- 视频: https://hahminlew.github.io/faceplex/static/videos/compare_offline/session_1.mp4
- 图片: https://hahminlew.github.io/faceplex/static/images/main_figure.png
- 项目主页: https://hahminlew.github.io/faceplex

#### Wan-Streamer：面向实时交互的端到端基础模型（Wan-Streamer） — 阿里通义 (2026-06-24)
- 类型: 模型 · 时序: 全双工 · 获取方式: 仅限研究
- 输入: 视频, 语音与音频, 文字提示 → 输出: 虚拟人（脸 / 身体）, 语音 / 声音, 对话 / 文本
- 核心想法: 把整条级联压缩进一个流式模型，时机、轮流发言和表情都在一起学习，而不是拼接起来。
- 内容: Wan-Streamer 是一个端到端模型，在同一个 Transformer 中同时完成听、看、思考、说话和视频回应，不依赖单独的语音识别、大模型、语音合成或虚拟人模块。0.3 版（2026 年 7 月）加入“世界设定 + 事件流”的视频预训练以支持自由行为；演示展示了实时的全双工视频对话。
- 实现方式: 在单个 Transformer 中交错排列视觉、音频与文本的输入和输出 token，配合块因果注意力以及因果编码器与解码器，实现增量式流式生成。
- 参数: 640×368 · 25 fps · ~200 ms model-side latency
- 能力维度: 时间响应性, 反应性, 行为似真性
- 论文: https://arxiv.org/abs/2606.25041 (arXiv 2026)
- 视频: https://wan-streamer.com/v0.1/assets/video/realtime.mp4
- 图片: https://wan-streamer.com/v0.1/assets/img/agent-chat-poster.jpg https://wan-streamer.com/v0.1/assets/img/framework.png
- 项目主页: https://wan-streamer.com

#### CARA-4 — Anam (2026-05-12)
- 类型: 模型 · 时序: 回合制 · 获取方式: 公开 API, 产品 / 应用
- 输入: 语音与音频, 图像, 文字提示 → 输出: 虚拟人（脸 / 身体）
- 核心想法: 可导演的表演（痛苦的病人与沉着的教练）让虚拟人的情绪成为可以写下来的实验条件。
- 内容: CARA-4 是 Anam 的实时虚拟人扩散模型：只需一张照片即可以 25 fps 渲染横屏（1152×768）或竖屏（768×1152）的对话人脸；Director Notes 让开发者设定虚拟人的表演方式（温和、痛苦、愤怒等），并允许大模型在一次回复中途改变表演方向。
- 实现方式: 一个实时生成每个像素的扩散模型，以语音和文本表演提示为条件，运行在对话引擎中；从用户说完到虚拟人回应的中位延迟低于 1 秒。
- 参数: 1152×768 / 768×1152 · 25 fps · <1 s median response latency
- 能力维度: 感知真实感, 实验控制, 行为似真性
- 视频: https://framerusercontent.com/assets/89hAkOrdOYdbEcy5VV2WX2NS6uk.mp4
- 图片: https://framerusercontent.com/assets/cyASyHEg6g3WK5dCwQoOyyVbFZU.png
- 项目主页: https://anam.ai/research
- API 文档: https://anam.ai/docs/introduction/models

#### LPM 1.0 大型表演模型（LPM 1.0 (Large Performance Model)） — Ailing Zeng (2026-04-09)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入: 语音与音频, 图像, 文字提示 → 输出: 虚拟人（脸 / 身体）, 平面视频
- 核心想法: 把表现力、实时速度和长时身份一致性视为同一个“表演三难”，游戏 NPC 和直播角色必须同时解决。
- 内容: LPM 1.0 是一个用于对话角色表演的视频模型：给定一张角色图像，它会根据用户的音频生成倾听画面，根据合成语音生成说话画面，并可用文本提示控制动作；它实时运行、时长不受限，同时保持身份稳定。作者还提出了交互式角色表演基准 LPM-Bench。
- 实现方式: 在说话-倾听配对的人物视频和身份参考上训练 17B 扩散 Transformer，再蒸馏为因果流式生成器（Online LPM）。
- 参数: 17B base · real-time streaming · infinite length
- 能力维度: 行为似真性, 持久性, 实验控制
- 论文: https://arxiv.org/abs/2604.07823 (arXiv 2026)
- 视频: https://pub-4e149c2dec59455a88c79783cc4985c8.r2.dev/videos/hero-demo.mp4
- 项目主页: https://large-performance-model.github.io

#### V4 Expressive 可视化智能体（V4 Expressive Visual Agents） — D-ID (2026-03-16)
- 类型: 产品 / 应用 · 时序: 回合制 · 获取方式: 产品 / 应用, 公开 API
- 输入: 语音与音频, 文字提示 → 输出: 虚拟人（脸 / 身体）, 语音 / 声音, 对话 / 文本
- 核心想法: 与情绪匹配的表情已成为商用智能体的标配，但它跟随的是智能体自己的文本，而不是用户的行为。
- 内容: D-ID 的 V4 Expressive 可视化智能体是实时对话虚拟人，表情会跟随所说内容的情绪基调；只需一段真人短视频即可生成，可部署到网站或通过 API 调用，企业还可自行托管。
- 实现方式: 级联智能体（知识库、大模型、语音合成）驱动 D-ID 的 V4 虚拟人视频模型，该模型以生成语音的情绪为条件控制面部表情。
- 能力维度: 感知真实感, 创作可及性
- 视频: https://www.youtube.com/watch?v=-WhLtR1no0M
- 项目主页: https://www.d-id.com/introducing-v4-expressive-avatars/
- API 文档: https://docs.d-id.com

#### Phoenix-4 — Tavus (2026-02-18)
- 类型: 模型 · 时序: 实时流式 · 获取方式: 公开 API, 产品 / 应用
- 输入: 语音与音频, 文字提示 → 输出: 虚拟人（脸 / 身体）
- 核心想法: 让“倾听时的脸”而不只是说话的嘴，成为实时渲染器的可控输出。
- 内容: Phoenix-4 能实时渲染真人的全脸视频复刻，可显式控制情绪，并在用户说话时呈现主动倾听的表情；它是 Tavus 对话视频接口的“脸”。Phoenix-4.5（2026-09-09）加入上半身动作和零样本身份，音频到视频延迟约 134 ms。
- 实现方式: 音频特征编码器和行为模型驱动一个在对话视频上训练的实时全脸渲染网络，以情绪和倾听状态作为条件；它与 Sparrow（轮流发言）和 Raven（感知）组成级联系统协同工作。
- 参数: 1080p · 40 fps (Phoenix-4) · ~134 ms audio-to-video (Phoenix-4.5)
- 能力维度: 感知真实感, 行为似真性
- 视频: https://www.youtube.com/watch?v=FDxfK2xisoE
- 图片: https://cdn.prod.website-files.com/68c8e57d6e512b9573db147f/6993c0e122a8c8cbd131d6ac_Herop44.avif
- 项目主页: https://www.tavus.io/blog/phoenix-4-real-time-human-rendering-with-emotional-intelligence
- API 文档: https://docs.tavus.io

#### LiveAvatar 实时虚拟人（LiveAvatar (Interactive Avatar)） — HeyGen (2025-11)
- 类型: 平台 / API · 时序: 回合制 · 获取方式: 公开 API, 产品 / 应用
- 输入: 语音与音频, 文字提示 → 输出: 虚拟人（脸 / 身体）, 语音 / 声音
- 核心想法: 实时虚拟人便宜到可以给每个语音智能体配一张脸，问题从“能不能渲染”转向“行为像不像”。
- 内容: LiveAvatar 是 HeyGen 的实时虚拟人流式 API，接替了此前的 Interactive Avatar：一个由图像或两分钟视频克隆而来的半身或全身 1080p 虚拟人，通过 WebRTC 说出语音智能体的回复。HeyGen 称首帧中位时间低于 300 ms，大批量时约每分钟 0.01 美元。
- 实现方式: 仅负责虚拟人渲染，通过 LiveKit/WebRTC 推流；驱动它的可以是 HeyGen 托管的语音识别-大模型-语音合成流程，也可以是开发者自己的语音智能体。
- 参数: 1080p · <300 ms median time to first frame · unlimited concurrency
- 能力维度: 创作可及性, 时间响应性
- 视频: https://www.youtube.com/watch?v=4hVvW4tHFJY
- 图片: https://www.liveavatar.com/og-image-fb.jpg
- 项目主页: https://www.liveavatar.com/
- API 文档: https://docs.liveavatar.com
- 代码: https://github.com/heygen-com/liveavatar-web-sdk

#### Tavus 对话视频接口（CVI）（Conversational Video Interface (Phoenix-2)） — Tavus (2024-08-15)
- 类型: 平台 / API · 时序: 回合制 · 获取方式: 公开 API, 产品 / 应用
- 输入: 语音与音频, 视频 → 输出: 虚拟人（脸 / 身体）, 语音 / 声音, 对话 / 文本
- 核心想法: 把语音识别、大模型、语音合成和渲染出的人脸打包成一个 API，让“会说话的视频人”变成实验室可以按分钟租用的东西。
- 内容: Tavus 的对话视频接口（CVI）把真人的视频复刻放进实时通话中回答口头提问；它于 2024 年 8 月与 Phoenix-2 渲染模型一同发布，Tavus 称这一步突破了实时门槛。截至 2026 年 10 月，CVI 中的“PAL”可配置人设、面孔、声音、目标、护栏、知识库和记忆，可运行于完整的 Tavus 流程、Echo 模式，或接入 LiveKit、Pipecat、Agora。
- 实现方式: 级联流程：语音转文字、大语言模型、文字转语音，再由 Phoenix-2 音频驱动的人脸渲染器生成画面（很可能是用一段短训练视频为每个复刻拟合、带三维先验的说话头模型），通过 WebRTC 流式传输并支持打断。
- 能力维度: 时间响应性, 创作可及性
- 视频: https://www.youtube.com/watch?v=OZthIm5W-yQ
- 项目主页: https://www.tavus.io/blog/introducing-the-evolution-of-conversational-video-interface-now-with-emotional-intelligence
- API 文档: https://docs.tavus.io

### 音频驱动的说话人像与全身

由一张图像加语音生成脸部与全身动画：VASA-1、EMO、OmniHuman、Hallo、LivePortrait……

#### SoulX-FlashTalk — Soul AI Lab (2025-12-29)
- 类型: 模型 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 图像, 语音与音频 → 输出: 虚拟人（脸 / 身体）, 交互式帧流
- 核心想法: 一家社交应用公司开源的实时虚拟人，2026 年被商用全双工系统用作对比基线。
- 内容: SoulX-FlashTalk 用一个 14B 模型流式生成高保真的音频驱动虚拟人，启动时间不到一秒，帧率达到实时，时长不受限；权重已发布在 Hugging Face。
- 实现方式: 自校正双向蒸馏（在片段内保留双向注意力），配合多步回溯自校正机制，以及混合序列并行和并行 VAE 解码。
- 参数: 14B params · 32 fps · 0.87 s start-up latency
- 能力维度: 时间响应性, 持久性
- 论文: https://arxiv.org/abs/2512.23379 (arXiv 2025)
- 视频: https://github.com/Soul-AILab/Soul-AILab.github.io/raw/refs/heads/main/soulx-livetalk/static/videos/teaser_1_n_0129.mp4
- 项目主页: https://soul-ailab.github.io/soulx-flashtalk/
- 代码: https://github.com/Soul-AILab/SoulX-FlashTalk

#### Live Avatar：无限时长实时流式虚拟人（Live Avatar） — 阿里巴巴夸克 (2025-12-04)
- 类型: 模型 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 图像, 语音与音频 → 输出: 虚拟人（脸 / 身体）, 交互式帧流
- 核心想法: 说明只要把去噪步骤分摊到多块 GPU 上，前沿规模的视频模型也能作为实时虚拟人运行。
- 内容: Live Avatar 用一个 14B 扩散模型实时流式生成音频驱动的虚拟人，可连续生成数小时（超过 10000 秒）而身份不漂移；演示展示了与语音智能体的实时互动。
- 实现方式: 两阶段地把双向模型蒸馏为因果、少步的流式模型，加上长时防漂移策略，以及时间步强制流水线并行（每块 GPU 负责一个去噪时间步）。
- 参数: 14B params · 45 fps · 1.21 s time to first frame on 5× H800 · >10,000 s stable
- 能力维度: 时间响应性, 持久性
- 论文: https://arxiv.org/abs/2512.04677 (arXiv 2025)
- 视频: https://www.youtube.com/watch?v=_KwHex65wCU
- 项目主页: https://liveavatar.github.io/
- 代码: https://github.com/Alibaba-Quark/LiveAvatar

#### MIDAS：实时自回归多模态交互数字人（MIDAS） — 快手 / 可灵 (2025-08-26)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入: 语音与音频, 文字提示, 图像 → 输出: 虚拟人（脸 / 身体）, 交互式帧流
- 核心想法: 用大语言模型骨干充当流式虚拟人的动作规划器，新的控制信号可以像新 token 一样加入。
- 内容: 快手可灵团队的 MIDAS 是一个实时流式数字人，以音频、姿态和文本为控制信号自回归地生成视频，演示了双人双工对话和多语言说话。
- 实现方式: 稍加修改的大语言模型接收多模态条件编码并引导扩散头；配合最高 64 倍压缩的深度压缩自编码器，并使用约 2 万小时对话视频训练。
- 参数: ~20,000 h training dialogue · up to 64× latent compression
- 能力维度: 时间响应性, 实验控制
- 论文: https://arxiv.org/abs/2508.19320 (arXiv 2025)
- 视频: https://chenmingthu.github.io/milm/static/videos/dia_duplex.mp4
- 图片: https://chenmingthu.github.io/milm/static/images/dialog.png
- 项目主页: https://chenmingthu.github.io/milm/

#### OmniHuman-1.5 — 字节跳动 Seed (2025-08-26)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 公开 API, 产品 / 应用
- 输入: 图像, 语音与音频, 文字提示 → 输出: 虚拟人（脸 / 身体）, 平面视频
- 核心想法: 加入一个“深思”式规划器，让生成的人根据话语内容行动，这是从唇形同步走向行为的一步。
- 内容: OmniHuman-1.5 可生成一个或多个角色、长达一分钟的视频，人物的手势和表情跟随语音的含义和情绪而不只是节奏，并可用文本提示引导；可通过 BytePlus 和即梦使用。
- 实现方式: 双系统设计：多模态大模型对音频、图像和文本进行推理以规划高层动作，再由带有“伪末帧”身份设计的多模态 DiT 渲染视频。
- 能力维度: 行为似真性, 实验控制
- 论文: https://arxiv.org/abs/2508.19209 (arXiv 2025)
- 视频: https://www.youtube.com/watch?v=zjrcDKe2dlI
- 项目主页: https://omnihuman-lab.github.io/v1_5/

#### InfiniteTalk — 美团 (2025-08-19)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 视频, 图像, 语音与音频 → 输出: 虚拟人（脸 / 身体）, 平面视频
- 核心想法: 开源的长时音频驱动视频模型，后来许多实时系统都拿它做对比或在其基础上构建。
- 内容: InfiniteTalk 能为人物配上新的语音并驱动其动作，时长不受限，嘴唇、头部、姿态和表情一起变化并保持身份，输入可以是一段源视频或一张图像。
- 实现方式: 在基于 Wan 的视频扩散模型上做稀疏帧视频配音，以选定的参考帧为条件，使全身动作在分段之间都跟随音频。
- 能力维度: 持久性, 感知真实感
- 论文: https://arxiv.org/abs/2508.14033 (arXiv 2025)
- 视频: https://meigen-ai.github.io/InfiniteTalk/videos/0.mp4
- 图片: https://meigen-ai.github.io/InfiniteTalk/images/0.png
- 项目主页: https://meigen-ai.github.io/InfiniteTalk/
- 代码: https://github.com/MeiGen-AI/InfiniteTalk

#### TalkingMachines：实时 FaceTime 式音频驱动视频（TalkingMachines） — Character.AI (2025-06-03)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入: 图像, 语音与音频 → 输出: 虚拟人（脸 / 身体）, 交互式帧流
- 核心想法: 展示了 2026 年多数实时虚拟人采用的做法：把大型双向视频模型蒸馏成因果、少步的流式生成器。
- 内容: TalkingMachines 把预训练的图生视频模型改造成实时的音频驱动角色动画器，与音频大模型配合实现 FaceTime 式通话，可流式生成不限时长且不漂移的视频。
- 实现方式: 由先进的图生视频模型改造而来的 18B 音频条件 DiT，经非对称蒸馏得到稀疏因果的自回归学生模型，并把 DiT 与 VAE 解码拆分到不同 GPU 上。
- 参数: 18B params · real-time streaming
- 能力维度: 时间响应性, 感知真实感
- 论文: https://arxiv.org/abs/2506.03099 (arXiv 2025)
- 视频: https://aaxwaz.github.io/TalkingMachines/assets/videos/albert_2.mp4
- 项目主页: https://aaxwaz.github.io/TalkingMachines/

#### 混元 HunyuanVideo-Avatar（HunyuanVideo-Avatar） — 腾讯混元 (2025-05-26)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像, 语音与音频 → 输出: 虚拟人（脸 / 身体）, 平面视频
- 核心想法: 多角色音频驱动场景的开源权重，从单个说话头像迈向一个小型生成的社交情境。
- 内容: HunyuanVideo-Avatar 可根据音频驱动场景中的一个或多个角色，情绪可取自参考图像，不同角色由各自的音频驱动，例如两人相声对话。
- 实现方式: 基于 HunyuanVideo 的多模态 DiT，配有角色图像注入模块、音频情绪模块，以及按人脸区域为每个角色分配音频的人脸感知音频适配器。
- 能力维度: 情境多样性, 行为似真性
- 论文: https://arxiv.org/abs/2505.20156 (arXiv 2025)
- 视频: https://hunyuanvideo-avatar.github.io/static/%E5%8F%8C%E4%BA%BA/%E9%BB%91%E7%99%BD%E7%9B%B8%E5%A3%B0-2.mp4
- 项目主页: https://hunyuanvideo-avatar.github.io/
- 代码: https://github.com/Tencent-Hunyuan/HunyuanVideo-Avatar

#### AvatarFX — Character.AI (2025-04-22)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 产品 / 应用
- 输入: 图像, 文字提示, 语音与音频 → 输出: 虚拟人（脸 / 身体）, 平面视频
- 核心想法: 把会动的脸带进大众陪伴聊天平台，也带来了随之而来的安全问题（未成年人、冒充）。
- 内容: AvatarFX 让 Character.AI 用户在应用内把角色图像变成该角色用选定声音说话、唱歌或表达情绪的视频，适用于人类、动物和风格化角色。
- 实现方式: 据 Character.AI 的发布说明，是一个带音频条件的 DiT 扩散视频模型（架构细节未公开）。
- 能力维度: 创作可及性, 情境多样性
- 视频: https://www.youtube.com/watch?v=LEPaWVbRJ1E
- 项目主页: https://character.ai

#### Character-3 — Hedra (2025-03-12)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 产品 / 应用, 公开 API
- 输入: 图像, 语音与音频, 文字提示 → 输出: 虚拟人（脸 / 身体）, 平面视频
- 核心想法: 让音频驱动的角色视频成为大规模使用的创作工具，也适用于非人类和风格化角色。
- 内容: Character-3 能把任意角色图像（照片、插画、三维渲染）根据音频和设定情绪与肢体动作的文本提示，变成说话或唱歌的视频，在 Hedra Studio 应用中使用。
- 实现方式: 一个同时以图像、文本和音频为条件的“全模态”视频模型（架构未公开）。
- 能力维度: 创作可及性, 感知真实感
- 视频: https://www.youtube.com/watch?v=2IcwhZZGJUs
- 项目主页: https://www.hedra.com/
- API 文档: https://www.hedra.com/docs

#### OmniHuman-1 — 字节跳动 Seed (2025-02-03)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 产品 / 应用, 仅限研究
- 输入: 图像, 语音与音频, 视频 → 输出: 虚拟人（脸 / 身体）, 平面视频
- 核心想法: 用一个模型在混合条件（文本、音频、姿态）上扩大训练规模，让音频驱动视频从头部扩展到全身。
- 内容: OmniHuman-1 只需一张图像（头像、半身或全身，真人或卡通）加一段音频，就能生成此人说话、唱歌或做手势的视频，包括手部和手持物体；字节跳动后来在即梦 / Dreamina 中上线了它。
- 实现方式: 视频 DiT 模型，采用“全条件”训练策略，混合较弱（文本、音频）和较强（姿态）的条件，使更多训练数据可被利用。
- 能力维度: 感知真实感, 情境多样性
- 论文: https://arxiv.org/abs/2502.01061 (ICCV 2025)
- 视频: https://www.youtube.com/watch?v=1NU8NzvAxEg
- 项目主页: https://omnihuman-lab.github.io/

#### Loopy — 字节跳动 Seed (2024-09-04)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 图像, 语音与音频 → 输出: 虚拟人（脸 / 身体）, 平面视频
- 核心想法: 长时间的时间上下文让非语言动作从音频中自然产生，而不是来自循环播放的模板。
- 内容: Loopy 仅凭音频驱动人像，叹气、眉毛动作和头部运动都跟随语音的节奏和情绪，不需要空间动作模板。
- 实现方式: 视频扩散模型，配有片段间与片段内的时间模块，以及音频到隐变量的模块，以建模长期动作依赖。
- 能力维度: 感知真实感, 行为似真性
- 论文: https://arxiv.org/abs/2409.02634 (ICLR 2025 (Oral))
- 视频: https://loopyavatar.github.io/video/diverse_1.mp4
- 项目主页: https://loopyavatar.github.io/

#### LivePortrait — 快手 / 可灵 (2024-07-03)
- 类型: 开源工具 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 图像, 视频 → 输出: 虚拟人（脸 / 身体）, 平面视频
- 核心想法: 一个快速、可控的开源表情迁移工具，成为用真人表演操控生成人脸的默认方式。
- 内容: LivePortrait 能把驱动视频中的表情和头部姿态迁移到一张静态人像上（后续版本也支持动物），每帧约 13 ms，并可显式控制眼睛和嘴唇的开合，再无缝拼回原图。
- 实现方式: 基于隐式关键点（非扩散）的动画框架，训练数据扩展到约 6900 万帧，并配有小型 MLP 拼接模块和眼部/唇部重定向模块。
- 参数: 12.8 ms per frame on RTX 4090
- 能力维度: 实验控制, 创作可及性
- 论文: https://arxiv.org/abs/2407.03168 (arXiv 2024)
- 视频: https://liveportrait.github.io/src/video/all_cross_opt.mp4
- 图片: https://liveportrait.github.io/src/img/live-portrait.png
- 项目主页: https://liveportrait.github.io/
- 代码: https://github.com/KlingAIResearch/LivePortrait

#### VASA-1：实时生成的逼真说话人脸（VASA-1） — 微软 (2024-04-16)
- 类型: 模型 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入: 图像, 语音与音频 → 输出: 虚拟人（脸 / 身体）, 平面视频
- 核心想法: 证明了一张照片就能变成实时对话的人脸，也说明了开发者为何因冒充风险而不公开它。
- 内容: VASA-1 只需一张人像照片和一段语音，就能生成唇形同步、带细微表情和自然头部动作的逼真说话人脸，可在线以 512×512、最高 40 fps 生成。微软没有公开发布它；2025 年微软称在 Copilot Labs 的 Copilot Portraits 中用 VASA-1 驱动风格化的面孔。
- 实现方式: 扩散 Transformer 在从视频中学到的解耦人脸隐空间里生成整体面部动态和头部动作，再由解码器根据隐编码渲染画面。
- 参数: 512×512 · up to 40 fps online · negligible starting latency
- 能力维度: 感知真实感, 时间响应性
- 论文: https://arxiv.org/abs/2404.10667 (NeurIPS 2024 (Oral))
- 视频: https://vasavatar.github.io/VASA-1/video/realtime_demo.mp4
- 项目主页: https://www.microsoft.com/en-us/research/project/vasa-1/

#### EMO：让人像活起来（EMO (Emote Portrait Alive)） — 阿里通义 (2024-02-27)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 图像, 语音与音频 → 输出: 虚拟人（脸 / 身体）, 平面视频
- 核心想法: 让说话头像从只动嘴的唇形同步，进化到由音频直接驱动的整张脸的情绪表演。
- 内容: EMO 能让一张人像随任意音频说话或唱歌，表情和头部动作丰富，中间不经过三维人脸模型或面部关键点。
- 实现方式: 音频到视频的扩散模型（以 Stable Diffusion 为骨干，结合 ReferenceNet 身份特征、音频交叉注意力以及速度和人脸区域控制），在 250 多小时的说话视频上训练。
- 能力维度: 感知真实感, 行为似真性
- 论文: https://arxiv.org/abs/2402.17485 (arXiv 2024)
- 视频: https://humanaigc.github.io/emote-portrait-alive/content/video/%E8%B5%AB%E6%9C%AC16_9.mp4
- 图片: https://humanaigc.github.io/emote-portrait-alive/content/images/framework/intro.png
- 项目主页: https://humanaigc.github.io/emote-portrait-alive/

#### Wav2Lip 唇形同步（Wav2Lip） — K R Prajwal (2020-08-23)
- 类型: 开源工具 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 语音与音频, 视频 → 输出: 平面视频, 虚拟人（脸 / 身体）
- 核心想法: 这一谱系的前身：一旦唇形能跟随任何声音，人脸就能与合成语音配对；它的唇形同步指标（LSE-C/D）在 2026 年仍被用来给虚拟人打分。
- 内容: Wav2Lip 能把任意视频中说话人的唇形重新对齐到一段新的音频上，适用于任何身份和语言，无需针对说话人训练。
- 实现方式: 基于 GAN 的唇形生成器，训练时用一个冻结的、预训练好的唇形同步专家判别器（SyncNet）惩罚不同步的口型。
- 能力维度: 感知真实感, 创作可及性
- 论文: https://arxiv.org/abs/2008.10010 (ACM Multimedia 2020)
- 视频: https://www.youtube.com/watch?v=0fXaDCZNOJc
- 项目主页: https://github.com/Rudrabha/Wav2Lip
- 代码: https://github.com/Rudrabha/Wav2Lip

### 照片级三维化身

Codec Avatars、高斯头部与全身化身、MetaHuman、Personas、NVIDIA ACE：可驱动的 XR 三维人物。

#### 大规模 Codec Avatars（LCA）（Large-scale Codec Avatars (LCA)） — Junxuan Li, Meta (2026-04-02)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入: 图像, 视频 → 输出: 虚拟人（脸 / 身体）, 高斯泼溅 / 辐射场
- 核心想法: 把基础模型的做法（在一百万段真实视频上预训练，再用影棚数据后训练）用于三维化身，让人群多样性不再受限于采集。
- 内容: LCA 只需一次前向推理就能为几乎任何人生成高保真的全身三维化身，具备细致的面部表情和手指级控制，并能泛化到不同发型、服装和人群。
- 实现方式: 先在一百万段真实场景视频上预训练前馈高斯化身模型以获得外观与几何先验，再在精选多视角数据上后训练以提升表现力和保真度。
- 参数: 1M pretraining videos · full body · feed-forward
- 能力维度: 情境多样性, 感知真实感, 实验控制
- 论文: https://arxiv.org/abs/2604.02320 (CVPR 2026)
- 视频: https://www.youtube.com/watch?v=eqFz2GFPIkE
- 项目主页: https://junxuan-li.github.io/lca

#### Audio2Face-3D 语音驱动面部动画（Audio2Face-3D） — 英伟达 (2025-09-24)
- 类型: 开源工具 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 语音与音频 → 输出: 动作 / 动画, 虚拟人（脸 / 身体）
- 核心想法: 为游戏引擎 NPC 和 XR 智能体提供开放、可检视的“语音到面部”层，可与大模型和语音合成并行运行。
- 内容: Audio2Face-3D 可根据语音音频实时为绑定好的三维角色生成唇形同步和面部表情；NVIDIA 于 2025 年 9 月开源了模型、SDK 和训练框架，并提供 Unreal Engine 与 Maya 插件。
- 实现方式: 神经网络（回归与扩散两种版本）把音频特征映射为面部 blendshape 或顶点动画以及情绪，属于 NVIDIA ACE 的一部分。
- 能力维度: 时间响应性, 创作可及性
- 论文: https://arxiv.org/abs/2508.16401 (arXiv 2025)
- 视频: https://www.youtube.com/watch?v=-l8kjQUTfQk
- 图片: https://developer-blogs.nvidia.com/wp-content/uploads/2025/09/NVIDIA-Open-Source-Audio2Face-video-500x282.gif
- 项目主页: https://developer.nvidia.com/blog/nvidia-open-sources-audio2face-animation-model/
- 代码: https://github.com/NVIDIA/Audio2Face-3D

#### Persona 数字分身（visionOS 26）（Personas (visionOS 26)） — 苹果 (2025-06-09)
- 类型: 产品 / 应用 · 时序: 实时流式 · 获取方式: 产品 / 应用
- 输入: 多视角拍摄 / 扫描, 身体、面部与视线追踪 → 输出: 虚拟人（脸 / 身体）
- 核心想法: 多数 XR 用户真正接触到的第一个照片级自我化身，因此是具身远程临场研究的现实基线。
- 内容: Persona 是 Apple Vision Pro 佩戴者的三维形象：用头显快速扫描面部生成，在 FaceTime 和共享空间应用中由头显的眼部、面部和手部追踪实时驱动；visionOS 26 重新打造了 Persona，头发、皮肤、睫毛和侧脸更逼真。
- 实现方式: 由头显前置摄像头在设备端重建（Apple 在 visionOS 26 中称使用了“体积渲染”和机器学习），并由内部的眼部和面部摄像头驱动。
- 能力维度: 感知真实感, 时间响应性
- 视频: https://www.youtube.com/watch?v=81bsjbTN88g
- 项目主页: https://www.apple.com/os/visionos/

#### LAM 大型化身模型（LAM (Large Avatar Model)） — 阿里通义 (2025-02-25)
- 类型: 模型 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 图像, 语音与音频 → 输出: 虚拟人（脸 / 身体）, 高斯泼溅 / 辐射场
- 核心想法: 单图生成、成本低到能在浏览器里运行的三维头部，让具身智能体无需 GPU 推流也能部署。
- 内容: LAM 只需一张照片、一次前向推理就能生成可驱动的三维高斯头部，可在手机和 WebGL 中实时运行；阿里巴巴还把它与音频驱动动画结合用于聊天虚拟人。
- 实现方式: 以 FLAME 规范点为查询、与多尺度图像特征交互的 Transformer 预测规范空间中的高斯属性，再用标准线性混合蒙皮和修正 blendshape 驱动。
- 能力维度: 创作可及性, 时间响应性
- 论文: https://arxiv.org/abs/2502.17796 (arXiv 2025)
- 视频: https://www.youtube.com/watch?v=FrfE3RYSKhk
- 项目主页: https://aigc3d.github.io/projects/LAM/
- 代码: https://github.com/aigc3d/LAM

#### URAvatar：通用可重光照高斯化身（URAvatar） — Junxuan Li, Meta (2024-10-31)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入: 视频, 多视角拍摄 / 扫描 → 输出: 虚拟人（脸 / 身体）, 高斯泼溅 / 辐射场
- 核心想法: 把 Codec Avatar 的质量从采集影棚带到手机上，这一步让研究可以使用参与者自己的脸。
- 内容: URAvatar 只需一次手机扫描就能生成可重光照、可驱动的照片级头部化身；它利用从数百名影棚采集者身上学到的通用先验，并能在新光照下实时渲染。
- 实现方式: 在多视角、多光照采集数据上训练通用的可重光照高斯化身先验；手机扫描通过逆向渲染对先验进行拟合与微调。
- 能力维度: 创作可及性, 感知真实感
- 论文: https://arxiv.org/abs/2410.24223 (SIGGRAPH Asia 2024)
- 视频: https://junxuan-li.github.io/urgca-website/static/videos/ica-driving-video_crop.mp4
- 图片: https://junxuan-li.github.io/urgca-website/static/images/overview.png
- 项目主页: https://junxuan-li.github.io/urgca-website/

#### 可重光照高斯 Codec Avatars（Relightable Gaussian Codec Avatars） — Shunsuke Saito, Meta (2023-12-06)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入: 多视角拍摄 / 扫描, 身体、面部与视线追踪 → 输出: 虚拟人（脸 / 身体）, 高斯泼溅 / 辐射场
- 核心想法: 光照一致是可信度的一部分：无视房间光线的脸看起来就像贴上去的。
- 内容: 可重光照高斯 Codec Avatars 能在任意光照下实时渲染可驱动的三维头部，包括单根发丝、皮肤毛孔和眼睛反光，使化身与所处场景的光照一致。
- 实现方式: 把三维高斯附着在可变形头部模型上，学习辐射传输（漫反射球谐与球面高斯镜面反射），再加上显式的眼睛模型，在光场舞台多视角采集数据上训练。
- 能力维度: 感知真实感
- 论文: https://arxiv.org/abs/2312.03704 (CVPR 2024 (Oral))
- 视频: https://shunsukesaito.github.io/rgca/static/videos/full_video.mp4
- 图片: https://shunsukesaito.github.io/rgca/static/images/overview.png
- 项目主页: https://shunsukesaito.github.io/rgca/

#### GaussianAvatars：绑定三维高斯的照片级头部化身（GaussianAvatars） — Shenhan Qian (2023-12-04)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 多视角拍摄 / 扫描, 身体、面部与视线追踪 → 输出: 虚拟人（脸 / 身体）, 高斯泼溅 / 辐射场
- 核心想法: 把高斯绑定到标准人脸模型上，让高斯化身可以用游戏和追踪器已在使用的参数来驱动。
- 内容: GaussianAvatars 把三维高斯绑定到 FLAME 人脸网格上，从多视角视频中构建照片级三维头部，可用新的表情和姿态重新驱动，并能从任意视角实时渲染。
- 实现方式: 三维高斯挂接在 FLAME 网格三角形上并随之运动，致密化时继承绑定关系，在多视角视频上与 FLAME 参数联合优化。
- 能力维度: 感知真实感, 实验控制
- 论文: https://arxiv.org/abs/2312.02069 (CVPR 2024)
- 视频: https://www.youtube.com/watch?v=lVEY78RwU_I
- 项目主页: https://shenhanqian.github.io/gaussian-avatars
- 代码: https://github.com/ShenhanQian/GaussianAvatars

#### MetaHuman Animator — Epic Games (2023-06-15)
- 类型: 产品 / 应用 · 时序: 预先生成 · 获取方式: 产品 / 应用
- 输入: 视频, 身体、面部与视线追踪 → 输出: 动作 / 动画, 虚拟人（脸 / 身体）
- 核心想法: 人人可用的表演捕捉，一条“人工制作但基于真实录制”的可信虚拟人行为路线。
- 内容: MetaHuman Animator 能在几分钟内把用 iPhone 或立体头戴相机拍摄的演员表演，转换为任意 MetaHuman 上的高保真面部动画；后续版本支持仅用网络摄像头或仅用音频生成动画，Unreal Engine 5.8（2026）又加入了用单个网络摄像头或手机摄像头对单名演员做无标记身体捕捉的功能。
- 实现方式: 4D 求解器先用少量帧拟合出该演员的 MetaHuman 身份，再追踪采集的视频与深度，把表演迁移到标准面部绑定上。
- 能力维度: 感知真实感, 创作可及性
- 视频: https://www.youtube.com/watch?v=bIGnx2jvrbg
- 项目主页: https://www.metahuman.com/

#### MetaHuman Creator — Epic Games (2021-02-10)
- 类型: 产品 / 应用 · 时序: 实时流式 · 获取方式: 产品 / 应用
- 输入: 场景规格、代码与规则, 多视角拍摄 / 扫描 → 输出: 虚拟人（脸 / 身体）, 网格 / 三维资产
- 核心想法: 非生成式的基线：人工制作、完整绑定、可控，每个参数都能记录；在可控性上，生成式虚拟人仍难以企及。
- 内容: MetaHuman Creator 让任何人通过混合扫描人脸并调整皮肤、头发和体型，在几分钟内设计出逼真且完整绑定的数字人，可直接在 Unreal Engine 中驱动；自 Unreal Engine 5.6（2025）起，它在引擎内运行并接受网格或扫描输入。
- 实现方式: 在扫描人脸与身体数据库（来自 3Lateral 和 Cubic Motion）上做参数化混合，配有标准面部绑定和用于实时渲染的多级细节（LOD）。
- 能力维度: 创作可及性, 感知真实感, 实验控制
- 视频: https://www.youtube.com/watch?v=OeUBATSJSr0
- 项目主页: https://www.metahuman.com/

#### Codec Avatars 照片级远程临场化身（Codec Avatars） — Meta (2019-03)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入: 身体、面部与视线追踪, 多视角拍摄 / 扫描 → 输出: 虚拟人（脸 / 身体）
- 核心想法: 确立了后来的高斯化身、手机扫描化身和前馈化身所追赶的目标：像编解码器一样编码、传输、解码一张脸的远程临场。
- 内容: Codec Avatars 是 Meta 为真人打造的照片级三维化身：在多相机影棚中采集，由 VR 头显内部的摄像头实时驱动，让戴着头显的两个人能看到对方的三维面孔。最著名的公开演示是 2023 年 Lex Fridman 与扎克伯格完全通过 Codec Avatars 进行的访谈。
- 实现方式: 深度外观模型（变分自编码器）从影棚采集数据中学习个人专属的面部几何与视角相关纹理的隐编码；头显摄像头实时回归该编码，再由解码器渲染。
- 能力维度: 感知真实感, 时间响应性
- 论文: https://doi.org/10.1145/3197517.3201401 (ACM TOG (SIGGRAPH 2018))
- 视频: https://www.youtube.com/watch?v=MVYrJJNdrEg
- 项目主页: https://tech.facebook.com/reality-labs/2019/3/codec-avatars-facebook-reality-labs/

### 倾听、手势与双人互动行为

建模两人之间的回应信号、视线、手势与轮流发言。

#### Sparrow-2 轮流发言模型（Sparrow-2） — Tavus (2026-08-27)
- 类型: 模型 · 时序: 回合制 · 获取方式: 公开 API
- 输入: 语音与音频 → 输出: 智能体行为与动作
- 核心想法: 对话时机如今是有专门基准的可测量模型输出，这让回应延迟成为实验可以设定的变量。
- 内容: Sparrow-2 是 Tavus 的轮流发言模型：它每 10 ms 判断一次语音或视频智能体应该听、等还是说，能区分思考中的停顿与话轮结束，也能区分真正的打断与背景噪声。Tavus 称它在 TurnBench 基准上的话轮结束检测（召回率 92.4%）和打断检测（召回率 97.4%）均排名第一。
- 实现方式: 一个基于整体音频场景（说话意图、韵律、环境）的流式声学-语义模型，取代静音计时与 VAD 端点检测；前代为 Sparrow-0（2025）和 Sparrow-1（2026 年 1 月）。
- 参数: 10 ms decision frame · TurnBench end-of-turn recall 92.4% · interruption recall 97.4%
- 能力维度: 时间响应性, 行为似真性
- 视频: https://www.youtube.com/watch?v=E7MjlfJQkJM
- 图片: https://cdn.prod.website-files.com/68c8e57d6e512b9573db147f/6a8ff14fd7938137631903b7_download%20(2).avif
- 项目主页: https://www.tavus.io/blog/sparrow-2
- API 文档: https://docs.tavus.io

#### VideoFDB 全双工视听对话基准（VideoFDB） — 英伟达 (2026-05-28)
- 类型: 数据集 / 基准 · 时序: 全双工 · 获取方式: 开源权重 / 代码
- 输入: 视频, 语音与音频 → 输出: 对话 / 文本, 虚拟人（脸 / 身体）
- 核心想法: 为全双工虚拟人提供带有人类参照分数的共同标尺，让各家厂商的说法可以相互比较。
- 内容: VideoFDB 是第一个评测全双工“视听到视听”对话智能体的基准：包含来自真实视频通话、由专家标注的 237 段双人片段，覆盖 11 种非语言互动动态；分别对感知（智能体能否读懂当下）和生成（能否以恰当的语音、视线和表情回应）打分，并设有公开排行榜。
- 实现方式: 从自然视频通话中截取片段，按区分感知与生成行为的分类体系标注，再由基于评分细则的语言模型评审，从流畅度、情绪匹配、非语言契合度和时机等维度打分。
- 参数: 237 clips · 11 nonverbal dynamics · human reference 3.92
- 能力维度: 时间响应性, 实验控制
- 论文: https://arxiv.org/abs/2605.30256 (arXiv 2026)
- 图片: https://research.nvidia.com/labs/amri/projects/video-fdb/og/videofdb-sunburst.png
- 项目主页: https://research.nvidia.com/labs/amri/projects/video-fdb/
- 代码: https://huggingface.co/datasets/nvidia/video-full-duplex-benchmark

#### Raven-1 多模态感知模型（Raven-1） — Tavus (2026-02-10)
- 类型: 模型 · 时序: 实时流式 · 获取方式: 公开 API
- 输入: 视频, 语音与音频 → 输出: 对话 / 文本, 智能体行为与动作
- 核心想法: 对人的感知成为一个可单独替换的模型，其输出可以记录下来，作为智能体“看到了什么”的日志。
- 内容: Raven-1 是 Tavus 用于实时对话的多模态感知模型：它把用户的语气、面部表情、视线、姿态和迟疑融合成持续更新的自然语言描述供智能体的大模型读取，于是语气平淡的“还行”和愉快的“还行”会得到不同的回应。
- 实现方式: 统一的视听融合，输出大模型可读的描述而非情绪标签，并滚动更新，使上下文的滞后不超过约 300 ms。
- 参数: audio descriptions <100 ms · context ≤300 ms stale · pipeline <600 ms
- 能力维度: 反应性, 时间响应性
- 视频: https://www.youtube.com/watch?v=GH9-EmgtABw
- 图片: https://cdn.prod.website-files.com/68c8e57d6e512b9573db147f/698ac479d3b6b3e85ef6cb96_processed-image%20(97).avif
- 项目主页: https://www.tavus.io/blog/raven-1-bringing-emotional-intelligence-to-artificial-intelligence
- API 文档: https://docs.tavus.io

#### Avatar Forcing：实时交互头部虚拟人（Avatar Forcing） — Taekyung Ki (2026-01-02)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 语音与音频, 视频, 图像 → 输出: 虚拟人（脸 / 身体）
- 核心想法: 以用户的动作（而不只是音频）为条件，让人像虚拟人能对参与者不说话时的行为作出反应。
- 内容: Avatar Forcing 驱动的头部虚拟人能实时回应用户的声音和可见行为（说话、点头、笑声）以及它自己的语音，在单个 GPU 上延迟约 500 ms。
- 实现方式: 在动作隐空间上做 diffusion forcing，以因果方式实时接收用户音频与动作等多模态条件；并用去掉用户条件的样本作为负例做偏好优化。
- 参数: ~500 ms latency · single H100 (14 GB) · 6.8× faster than baseline
- 能力维度: 反应性, 时间响应性
- 论文: https://arxiv.org/abs/2601.00664 (CVPR 2026)
- 视频: https://www.youtube.com/watch?v=TARPGnJ8GW4
- 项目主页: https://taekyungki.github.io/AvatarForcing/
- 代码: https://github.com/TaekyungKi/AvatarForcing

#### Seamless Interaction 双人互动数据集与模型（Seamless Interaction） — Meta (2025-06-27)
- 类型: 数据集 / 基准 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 语音与音频, 视频 → 输出: 动作 / 动画, 虚拟人（脸 / 身体）
- 核心想法: 开放的大规模双人互动数据是全双工虚拟人训练和评测的基础；2026 年的 GENEA 手势生成挑战赛就建立在它之上。
- 内容: Seamless Interaction 是 Meta FAIR 发布的数据集，包含 4000 多名参与者超过 4000 小时的面对面对话，并附带双人动作模型：根据双方音频和对方的视觉行为生成说话者的面部表情与手势，可用于二维视频或三维 Codec Avatars。
- 实现方式: 多机位录制自然对话与即兴表演的双人会话；基于扩散的视听双人动作模型可控制情绪与表现力，也可由大模型生成的语音驱动。
- 参数: 4,000+ hours · 4,000+ participants
- 能力维度: 行为似真性, 情境多样性, 实验控制
- 论文: https://arxiv.org/abs/2506.22554 (arXiv 2025)
- 图片: https://raw.githubusercontent.com/facebookresearch/seamless_interaction/main/assets/banner.gif
- 项目主页: https://ai.meta.com/research/seamless-interaction/
- 代码: https://github.com/facebookresearch/seamless_interaction

#### INFP：双人对话中的交互式头部生成（INFP） — 字节跳动 Seed (2024-12-05)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 语音与音频, 图像 → 输出: 虚拟人（脸 / 身体）
- 核心想法: 去掉了多数说话头像需要的“现在说 / 现在听”手动切换，这是自然轮流发言的前提。
- 内容: INFP 根据对话双方的音频驱动一张人像，在说话和倾听之间自动切换，在对方说话时呈现点头、视线和表情等反应。
- 实现方式: 第一阶段从真实对话视频中学习低维动作隐空间（头部模仿）；第二阶段用去噪模型把双轨音频映射到这些隐变量；训练数据为新构建的双人对话数据集 DyConv。
- 能力维度: 行为似真性, 时间响应性
- 论文: https://arxiv.org/abs/2412.04037 (CVPR 2025)
- 视频: https://www.youtube.com/watch?v=6exuYJ393LI
- 图片: https://grisoon.github.io/INFP/static/images/task-v3.png
- 项目主页: https://grisoon.github.io/INFP/

#### Audio2Photoreal：从音频到照片级对话化身（Audio2Photoreal） — Evonne Ng, Meta (2024-01-03)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 语音与音频 → 输出: 虚拟人（脸 / 身体）, 动作 / 动画
- 核心想法: 说明照片级渲染会暴露火柴人看不出的细微手势错误，所以行为与外观必须一起评估。
- 内容: Audio2Photoreal 把两人对话的音频转换成照片级三维化身的面部、身体和手势动作（包括倾听时的行为），并用 Meta 的 Codec Avatars 渲染。
- 实现方式: 先由 VQ-Transformer 预测引导姿态，再由扩散模型补全身体动作，另一个以音频为条件的扩散模型生成面部编码；训练数据为新采集的多视角对话数据集。
- 能力维度: 行为似真性, 感知真实感
- 论文: https://arxiv.org/abs/2401.01885 (arXiv 2024)
- 视频: https://www.youtube.com/watch?v=Y0GMaMtUynQ
- 项目主页: https://people.eecs.berkeley.edu/~evonne_ng/projects/audio2photoreal/
- 代码: https://github.com/facebookresearch/audio2photoreal

#### 学会倾听：非确定性双人面部动作建模（Learning to Listen） — Evonne Ng (2022-04-18)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 语音与音频, 视频 → 输出: 动作 / 动画, 虚拟人（脸 / 身体）
- 核心想法: 把倾听当作一种非确定的、可生成的行为，补上了对话虚拟人缺失的另一半。
- 内容: Learning to Listen 根据说话者的话语、声音和面部，生成倾听者的面部反应（点头、微笑、皱眉），并能为同一段发言生成多种合理的倾听反应。
- 实现方式: 用 VQ-VAE 码本表示倾听者动作，再用 Transformer 根据说话者的多模态输入自回归地预测倾听者编码，训练数据为真实场景中的双人访谈视频。
- 能力维度: 行为似真性, 情境多样性
- 论文: https://arxiv.org/abs/2204.08451 (CVPR 2022)
- 视频: https://www.youtube.com/watch?v=3CSlKZ5T6DU
- 项目主页: https://evonneng.github.io/learning2listen/
- 代码: https://github.com/evonneng/learning2listen

## 语音、声音与空间音频

视听沉浸中“听”的一半：可以被打断的全双工语音模型、富有表现力的声音、生成的音效与音乐，以及空间音频。

### 全双工语音与语音智能体

边说边听的语音到语音模型：Moshi、Sesame、GPT realtime、Gemini Live、Hume EVI……

#### Gemini 3.8 Live — 谷歌 DeepMind (2026-09-15)
- 类型: 模型 · 时序: 回合制 · 获取方式: 公开 API
- 输入: 语音与音频, 视频, 文字提示 → 输出: 语音 / 声音, 对话 / 文本
- 核心想法: 说话时在后台推理，缩小了“反应快”和“想得深”之间的差距，适合需要一边保持回应、一边处理复杂情境逻辑的角色。
- 内容: 两款用于 Live API 的音频到音频模型，自 2026 年 9 月 15 日起正式可用：Gemini 3.8 Live 面向低延迟对话，Gemini 3.8 Live Extended Thinking 能在对话进行中于后台推理。谷歌重点介绍了异步函数调用与主动音频，即智能体只在相关时才开口。
- 实现方式: 音频到音频的 Gemini 模型，支持交错推理与默认异步函数调用，接替 2026 年 3 月的 gemini-3.1-flash-live-preview。
- 能力维度: 时间响应性, 反应性
- 视频: https://storage.googleapis.com/gdm-deepmind-com-prod-public/media/SeC1i4kt5pDKGMWX/gemini-audio__demo__multi-tasking.webm
- 项目主页: https://deepmind.google/models/gemini-audio/
- API 文档: https://ai.google.dev/gemini-api/docs/live

#### SeedRealtime 视听全双工大模型（SeedRealtime） — 字节跳动 Seed (2026-08-05)
- 类型: 模型 · 时序: 全双工 · 获取方式: 产品 / 应用
- 输入: 语音与音频, 视频 → 输出: 语音 / 声音, 对话 / 文本
- 核心想法: 在已部署的产品中实现主动、抗干扰的对话时机：系统根据看到和听到的内容决定何时开口，而不是依据静音。
- 内容: 字节跳动 Seed 的原生视听全双工模型：能同时看、听、说，在合适的时机插话或停顿，并能忽略旁人闲聊和背景噪音。Seed 报告称，人工评测中它的对话节奏问题比级联系统减少一半，并已全量大规模上线。
- 实现方式: 统一架构原生融合连续的音频、视频与文本流，并对用户的对话状态建模，取代外部的语音活动检测器。
- 能力维度: 时间响应性, 反应性
- 视频: https://lf3-static.bytednsdoc.com/obj/eden-cn/lapzild-tss/ljhwZthlaukjlkulzlp/user-upload/4xfa4msff67ew.mp4
- 项目主页: https://seed.bytedance.com/en/blog/seedrealtime-audio-visual-full-duplex-llm-released-toward-omni-modal-natural-interaction

#### GPT-Live — OpenAI (2026-07-08)
- 类型: 模型 · 时序: 全双工 · 获取方式: 产品 / 应用, 公开 API
- 输入: 语音与音频 → 输出: 语音 / 声音, 对话 / 文本
- 核心想法: OpenAI 自己告别了回合制语音：主流的 ChatGPT 语音如今会重叠发言、会附和，全双工的对话节奏不再只是研究原型的特性。
- 内容: 一个全双工语音模型，现在驱动 ChatGPT 语音：它边说边听，会用“嗯哼”“对”表示在听，也能在用户思考时保持安静。较难的请求会在后台交给前沿模型（发布时为 GPT-5.5）处理，对话不中断。GPT-Live-1 于 2026 年 9 月 10 日在 API 中正式可用，GPT-Live-1.1（2026 年 10 月 15 日）为 ChatGPT 增加了新声音和口音。
- 实现方式: 全双工架构：在生成输出的同时持续处理输入，并把推理任务委托给后台模型。
- 参数: GPT-Live-1 and GPT-Live-1 mini · ChatGPT · API GA 2026-09-10 (v1/live/sessions)
- 能力维度: 时间响应性, 行为似真性
- 视频: https://www.youtube.com/watch?v=EAN5Cj347PY
- 图片: https://images.ctfassets.net/kftzwdyauwt9/54glGpDpS58mKdx6Y3GobW/6ea5121851a36b8cf0505a96be2de994/bidi-art-card_16_9__1_.png?w=1600&h=900&fit=fill
- 项目主页: https://openai.com/index/introducing-gpt-live/
- API 文档: https://developers.openai.com/api/docs/changelog

#### GPT-Realtime-2 — OpenAI (2026-05-07)
- 类型: 模型 · 时序: 回合制 · 获取方式: 公开 API
- 输入: 语音与音频, 文字提示 → 输出: 语音 / 声音, 对话 / 文本
- 核心想法: 能在对话中推理并采取行动的语音智能体，让多步骤角色扮演情境（调度员、办事员、谈判对手）可以在电话中实现。
- 内容: OpenAI 第一个具备 GPT-5 级推理能力的语音模型，同时发布 GPT-Realtime-Translate（70 多种输入语言到 13 种输出语言的实时翻译）和 GPT-Realtime-Whisper（流式转写）。它会先说一句“我查一下”之类的过渡语，可以并行调用多个工具，并在处理任务时继续对话。GPT-Realtime-2.1 及 2.1 mini（2026 年 7 月 6 日）改进了字母数字识别、噪声处理和被打断时的表现。
- 实现方式: 在 Realtime API 中提供的语音到语音模型，可调节推理强度，支持过渡语与并行工具调用；对话仍按轮次切分。
- 参数: +15.2% Big Bench Audio vs GPT-Realtime-1.5 (OpenAI)
- 能力维度: 时间响应性, 反应性
- 视频: https://www.youtube.com/watch?v=JOu8v6CBjkE
- 图片: https://images.ctfassets.net/kftzwdyauwt9/CtzMayHtxIkcMPAo8BpqJ/966285cf3802995841337122190ec2fd/OAI_GPT-Realtime-2_Art_Card_16x9.png.png?w=1600&h=900&fit=fill
- 项目主页: https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/
- API 文档: https://platform.openai.com/docs/guides/realtime

#### Hibiki-Zero 同声传译模型（Hibiki-Zero） — Kyutai (2026-02-12)
- 类型: 模型 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 语音与音频 → 输出: 语音 / 声音
- 核心想法: 带声音迁移的实时传译让跨语言相遇可以被布置出来：参与者能以短而自然的延迟，用自己的语言听到外语对话者的话。
- 内容: 一个同声传译式的语音到语音翻译模型：听法语、西班牙语、葡萄牙语或德语，在对方还在说话时就用对方自己的声音说出英文译文。它是 Hibiki（2025 年 2 月）的后续，不再需要逐词对齐的训练数据。
- 实现方式: 一个 3B 的仅解码器多流 Transformer，基于 12.5 Hz 的 Mimi 音频标记，联合建模源语音与目标语音，并自适应调整延迟以积累恰好足够的上下文，训练时无需词级对齐。
- 参数: 3B · 12.5 Hz · FR/ES/PT/DE → EN · CC BY-NC-SA 4.0
- 能力维度: 时间响应性, 情境可达性
- 论文: https://arxiv.org/abs/2602.11072 (arXiv 2026)
- 视频: https://github.com/user-attachments/assets/d533ec45-8d5e-4e41-886a-0b2d198be6f3
- 图片: https://opengraph.githubassets.com/645106f5c200b440e2f106671ceaf13e48ac82c921672b8db6c2724e1a6ddc6e/kyutai-labs/hibiki-zero
- 项目主页: https://kyutai.org/blog/2026-02-12-hibiki-zero/
- 代码: https://github.com/kyutai-labs/hibiki-zero

#### MiniCPM-o 4.5 — 面壁智能 OpenBMB (2026-02-03)
- 类型: 模型 · 时序: 全双工 · 获取方式: 开源权重 / 代码
- 输入: 语音与音频, 视频 → 输出: 语音 / 声音, 对话 / 文本
- 核心想法: 体量小到单张 GPU 即可运行的全双工视听对话，让头显情境中的对话者可以离线、锁定版本地运行。
- 内容: 一个 9B 的开源全模态模型，能看实时摄像头画面，同时听和说，发现情况时还能主动开口。它可以通过 llama.cpp、Ollama 和 vLLM 在本地运行，并用一小段参考音频克隆声音。
- 实现方式: 由 SigLIP2 视觉编码器、Whisper-medium 音频编码器、CosyVoice2 语音解码器和 Qwen3-8B 主干端到端组装而成，持续处理音视频输入，并同时输出文本与语音流，二者互不阻塞。
- 参数: 9B · full-duplex audio + video · local inference (llama.cpp-omni)
- 能力维度: 时间响应性, 反应性
- 论文: https://arxiv.org/abs/2604.27393 (Technical report (arXiv 2026))
- 视频: https://www.youtube.com/watch?v=6UzC-O1Q-1U
- 图片: https://opengraph.githubassets.com/32a28717382bef321452043efe551d5e3b48d955488f80e319b7355cba3a43eb/OpenBMB/MiniCPM-V
- 项目主页: https://github.com/OpenBMB/MiniCPM-V
- 代码: https://huggingface.co/openbmb/MiniCPM-o-4_5

#### PersonaPlex — 英伟达 (2026-01-15)
- 类型: 模型 · 时序: 全双工 · 获取方式: 开源权重 / 代码
- 输入: 语音与音频, 文字提示 → 输出: 语音 / 声音, 对话 / 文本
- 核心想法: 消除了“可配置角色”与“全双工自然度”之间的取舍，这正是行为研究中按脚本行事的实验助手所需要的。
- 内容: 一个开源的全双工对话模型：开发者可以选择声音，并用文字提示定义任意角色（客服、宇航员、奇幻人物），同时保留 Moshi 式的打断、附和与对话节奏。
- 实现方式: 基于 Moshi 的 7B 双流架构，使用语音加文本的混合系统提示；在由大模型补写角色描述的 Fisher 对话以及合成对话上微调。
- 参数: 7B · Moshi architecture · open weights
- 能力维度: 行为似真性, 实验控制
- 论文: https://research.nvidia.com/labs/adlr/files/personaplex/personaplex_preprint.pdf (Preprint 2026)
- 视频: https://research.nvidia.com/labs/adlr/files/personaplex/personaplex-intro.mp4
- 图片: https://opengraph.githubassets.com/b3ed03a6cecaddba122da6989b7312f8f08ca56a739ca320f413dca7aaff6350/NVIDIA/personaplex
- 项目主页: https://research.nvidia.com/labs/adlr/personaplex/
- 代码: https://github.com/NVIDIA/personaplex

#### 通义千问 Qwen3-Omni（Qwen3-Omni） — 阿里通义 (2025-09-22)
- 类型: 模型 · 时序: 回合制 · 获取方式: 开源权重 / 代码, 公开 API
- 输入: 语音与音频, 视频, 图像 → 输出: 语音 / 声音, 对话 / 文本
- 核心想法: 一个实验室可以自行部署的开源模型，能听、能看参与者并用语音回应，是闭源实时 API 的自托管替代方案。
- 内容: 一个开源权重、原生全模态的模型，接收文本、图像、音频和视频，并以流式文本和自然语音回答。阿里巴巴报告它在 36 项音频与视听基准中的 32 项上达到开源最佳，支持 119 种文本语言、19 种语音输入语言和 10 种语音输出语言。
- 实现方式: 混合专家的 Thinker–Talker 架构（总参数 30B，激活 3B），采用 AuT 音频编码器，并用多码本 Talker 流式生成语音。
- 参数: 30B-A3B MoE · 234 ms theoretical first-packet latency (Qwen) · 119 / 19 / 10 languages
- 能力维度: 时间响应性, 情境多样性
- 论文: https://arxiv.org/abs/2509.17765 (Technical report (arXiv 2025))
- 视频: https://www.youtube.com/watch?v=_zdOrPju4_g
- 图片: https://opengraph.githubassets.com/d43656f30182aae86d2489ca2e28f8912ccf78430f4743f461ca6c3166c2c752/QwenLM/Qwen3-Omni
- 项目主页: https://github.com/QwenLM/Qwen3-Omni
- 代码: https://github.com/QwenLM/Qwen3-Omni

#### gpt-realtime — OpenAI (2025-08-28)
- 类型: 模型 · 时序: 回合制 · 获取方式: 公开 API
- 输入: 语音与音频, 图像, 文字提示 → 输出: 语音 / 声音, 对话 / 文本
- 核心想法: 让可被指令控制、会调用工具的语音智能体成为现成 API：情境作者可以在系统提示里定义一个电话中的角色。
- 内容: OpenAI 面向 Realtime API 的生产级语音到语音模型，同时推出远程 MCP 工具、图像输入与 SIP 电话呼叫。它能遵循“说快一点、带点同理心”这类语气指令，在一句话中切换语言，并新增 Cedar 与 Marin 两种声音。
- 实现方式: 单一的语音到语音模型，通过 WebRTC、WebSocket 或 SIP 提供；轮次由服务器端或语义语音活动检测切分，支持用户插话打断。
- 参数: Big Bench Audio 82.8% vs 65.6% for the Dec 2024 model (OpenAI)
- 能力维度: 时间响应性, 实验控制
- 视频: https://www.youtube.com/watch?v=nfBbmtMJhX0
- 图片: https://images.ctfassets.net/kftzwdyauwt9/16qATUOZ1GSdE7JHHr0qFG/47b074ae6486a3d8f9ad14adb7812d13/RealtimeAPI_Blog_Open_Graphic_Image__1200x630_.png?w=1600&h=900&fit=fill
- 项目主页: https://openai.com/index/introducing-gpt-realtime/
- API 文档: https://platform.openai.com/docs/guides/realtime

#### 阶跃星辰 Step-Audio 2（Step-Audio 2） — 阶跃星辰 (2025-07-22)
- 类型: 模型 · 时序: 回合制 · 获取方式: 开源权重 / 代码, 公开 API
- 输入: 语音与音频 → 输出: 语音 / 声音, 对话 / 文本
- 核心想法: 不仅理解说了什么，还能读出是怎么说的，这是虚拟对话者对参与者的紧张或犹豫做出反应的前提。
- 内容: 阶跃星辰的端到端音频语言模型，用于口语对话：能捕捉情绪等副语言线索，按口头要求切换音色，并能在对话中联网搜索。阶跃星辰报告其在 LibriSpeech、MMAU 和 URO-Bench 上达到最佳；较小的 Step-Audio 2 mini 开源权重。
- 实现方式: 音频编码器加大模型，生成交错的文本与离散音频标记；训练中使用面向推理的强化学习，以及包含音频检索的检索增强生成。
- 能力维度: 感知真实感, 适应性
- 论文: https://arxiv.org/abs/2507.16632 (Technical report (arXiv 2025))
- 视频: https://www.youtube.com/watch?v=AAsl0pwbKME
- 图片: https://opengraph.githubassets.com/b3e3c4a9bb21755a2be0af80a3424e5bb4422426ffe5ea35b27cd073fdc1bd7e/stepfun-ai/Step-Audio2
- 项目主页: https://github.com/stepfun-ai/Step-Audio2
- 代码: https://github.com/stepfun-ai/Step-Audio2

#### EVI 3 — Hume AI (2025-05-29)
- 类型: 模型 · 时序: 回合制 · 获取方式: 公开 API, 产品 / 应用
- 输入: 语音与音频, 文字提示 → 输出: 语音 / 声音, 对话 / 文本
- 核心想法: 通过提示设计、带情绪表达的声音，让一项研究可以低成本地“选角”出许多不同的虚拟角色。
- 内容: Hume 的第三代共情语音接口，一个语音-语言模型：能在一秒内根据文字提示生成新的声音和性格，并用它对话。在 Hume 的盲测比较中，它在同理心、表现力、自然度、被打断时的表现和响应速度上的评分高于 GPT-4o。
- 实现方式: 单一的语音到语音语言模型，流式接收用户语音并同时生成语音与语言，说话时还能调用推理模型与网络搜索。
- 能力维度: 感知真实感, 适应性
- 视频: https://www.youtube.com/watch?v=SyO7sRtkcRE
- 图片: https://cdn.sanity.io/images/xqnc2for/production/282c4a42cdd49007a55031f3e06a2f880373f9bf-2160x2160.png?rect=0,513,2160,1134&w=1200&h=630
- 项目主页: https://www.hume.ai/blog/introducing-evi-3
- API 文档: https://dev.hume.ai/docs/speech-to-speech-evi/overview

#### Unmute — Kyutai (2025-05-22)
- 类型: 开源工具 · 时序: 回合制 · 获取方式: 开源权重 / 代码, 产品 / 应用
- 输入: 语音与音频, 文字提示 → 输出: 语音 / 声音, 对话 / 文本
- 核心想法: 给研究者一个可以接入任意大模型和角色设定的语音前端，代价是采用轮流发言，而不是 Moshi 那样的重叠对话。
- 内容: 一个模块化的语音层，让任何文本大模型都能听会说：它把 Kyutai 的流式语音识别、流式语音合成与语义轮次检测组合在一起。在 unmute.sh 上，人们可以和它交谈、打断它，并选择声音与性格。
- 实现方式: 级联结构：带语义语音活动检测的流式语音识别、任意文本大模型，以及在回复写完之前就开始说话的流式语音合成；2025 年 7 月开源。
- 能力维度: 时间响应性, 创作可及性
- 视频: https://www.youtube.com/watch?v=sRUaYQyX2vw
- 图片: https://opengraph.githubassets.com/871275284d27de66853e8b7ea8593ad83e38d94d709d5974ea8ca7996a1291dc/kyutai-labs/unmute
- 项目主页: https://kyutai.org/blog/2025-05-22-unmute/
- 代码: https://github.com/kyutai-labs/unmute

#### Amazon Nova Sonic — Amazon (2025-04-08)
- 类型: 模型 · 时序: 回合制 · 获取方式: 公开 API
- 输入: 语音与音频 → 输出: 语音 / 声音, 对话 / 文本
- 核心想法: 把会调用工具的语音到语音智能体带进企业云，对受数据治理要求限制、只能使用 AWS 的机构很有意义。
- 内容: Amazon Bedrock 上的语音到语音基础模型，双向流式对话，能根据说话人的语气调整表达，也能处理用户插话。Nova 2 Sonic 于 2025 年 12 月推出。
- 实现方式: 统一的语音理解与生成模型，通过 Bedrock 的双向流式 API 提供，支持插话打断。
- 能力维度: 时间响应性, 实验控制
- 视频: https://www.youtube.com/watch?v=68HjtdRYkUI
- 图片: https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2024/11/20/Bedrock-Nova-feat-img-1260x630.png
- 项目主页: https://aws.amazon.com/blogs/aws/introducing-amazon-nova-sonic-human-like-voice-conversations-for-generative-ai-applications/
- API 文档: https://docs.aws.amazon.com/nova/latest/userguide/speech.html

#### Sesame 对话语音模型 CSM（Maya 与 Miles）（Sesame CSM (Maya & Miles)） — Sesame (2025-02-27)
- 类型: 模型 · 时序: 回合制 · 获取方式: 产品 / 应用, 开源权重 / 代码
- 输入: 语音与音频, 文字提示 → 输出: 语音 / 声音, 对话 / 文本
- 核心想法: 瞄准“声音临场感”：决定语调的不只是文本，还有此前的对话上下文，而这正是让虚拟对话者显得“在场”的线索。
- 内容: Sesame 的对话语音模型，通过语音伴侣 Maya 与 Miles 展示：它们会停顿、发笑、变换语气、自我纠正，许多听众难以分辨是否真人。1B 规模的 CSM 于 2025 年 3 月开源权重；2026 年 Sesame 已在 iOS 与 Android 应用中提供其智能体，并宣布了眼镜产品。
- 实现方式: 两个基于交错文本与音频标记的自回归 Transformer：主干根据对话历史预测第一层 RVQ 码本，小型解码器预测其余各层；训练数据约一百万小时，以英语为主。
- 参数: Tiny 1B · Small 3B · Medium 8B backbones · CSM-1B open (Apache 2.0)
- 能力维度: 感知真实感, 行为似真性
- 视频: https://www.youtube.com/watch?v=i1BoLH1r2lU
- 图片: https://www.sesame.com/assets/images/og/sesame.jpg
- 项目主页: https://www.sesame.com/research/crossing_the_uncanny_valley_of_voice
- 代码: https://github.com/SesameAILabs/csm

#### Gemini 原生音频（Live API）（Gemini native audio (Live API)） — 谷歌 DeepMind (2024-12-11)
- 类型: 模型 · 时序: 回合制 · 获取方式: 公开 API, 产品 / 应用
- 输入: 语音与音频, 视频, 文字提示 → 输出: 语音 / 声音, 对话 / 文本
- 核心想法: 让语音智能体在说话的同时看到参与者摄像头里的画面，这正是头显情境需要的视听输入。
- 内容: Gemini 2.0 推出原生音频输出和多模态 Live API，可进行语音加摄像头的流式对话；Gemini 2.5 Flash 原生音频（2025 年 5 月起预览，9 月与 12 月更新）加入了情感对话与主动音频。
- 实现方式: 原生多模态的 Gemini 模型，接收流式音频与视频并直接输出音频标记，通过双向 WebSocket 提供，带语音活动检测与插话打断。
- 能力维度: 时间响应性, 反应性
- 视频: https://www.youtube.com/watch?v=qE673AY-WEI
- 图片: https://ai.google.dev/static/site-assets/images/share-gemini-api-2026-07.png
- 项目主页: https://ai.google.dev/gemini-api/docs/live
- API 文档: https://ai.google.dev/gemini-api/docs/live

#### Moshi — Kyutai (2024-07-03)
- 类型: 模型 · 时序: 全双工 · 获取方式: 开源权重 / 代码
- 输入: 语音与音频 → 输出: 语音 / 声音, 对话 / 文本
- 核心想法: 第一个公开发布的全双工语音模型：实验室可以运行、锁定版本并检查一个像人一样会重叠说话、而不是等待沉默的对话伙伴。
- 内容: 一个开源的语音-文本基础模型，能边听边说，因此可以被打断、主动插话并实时附和。Kyutai 在 2024 年 7 月现场演示，并于 2024 年 9 月发布权重、代码与论文。
- 实现方式: 在 7B 的 Helium 文本大模型上增加用户与模型两路并行音频流，由流式 Mimi 编解码器以 12.5 Hz 编码，并加入时间对齐的文本“内心独白”。
- 参数: 7B · Mimi codec 12.5 Hz · 160 ms theoretical / ~200 ms practical latency
- 能力维度: 时间响应性, 行为似真性
- 论文: https://arxiv.org/abs/2410.00037 (Technical report (arXiv 2024))
- 视频: https://www.youtube.com/watch?v=hm2IJSKcYvo
- 图片: https://opengraph.githubassets.com/c8a1dcee9d391167fc1993e466ce1b5b2a2da00e30da3e390021a0478eea6fbb/kyutai-labs/moshi
- 项目主页: https://kyutai.org/blog/2024-09-18-moshi-release/
- 代码: https://github.com/kyutai-labs/moshi

#### GPT-4o 语音（高级语音模式）（GPT-4o voice (Advanced Voice Mode)） — OpenAI (2024-05-13)
- 类型: 模型 · 时序: 回合制 · 获取方式: 产品 / 应用, 公开 API
- 输入: 语音与音频, 视频 → 输出: 语音 / 声音, 对话 / 文本
- 核心想法: 把“语音识别—大模型—语音合成”的级联压缩为一个模型，使副语言线索得以保留；但 OpenAI 后来自己也称其为回合制，因为它要等用户停下来。
- 内容: OpenAI 在 ChatGPT 中的第一个端到端音频模型：能听出语气，用带情绪、笑声甚至歌唱的声音回答，被打断时会停下；OpenAI 报告平均响应时间为 320 毫秒。2024 年 5 月现场演示，同年晚些时候以“高级语音模式”进入 ChatGPT，并于 2024 年 10 月通过 Realtime API 测试版向开发者开放。
- 实现方式: 一个在文本、视觉和音频上端到端训练的多模态 Transformer；轮次结束由语音活动检测根据静音判断。
- 参数: 232 ms min / 320 ms avg audio response (OpenAI)
- 能力维度: 时间响应性, 感知真实感
- 视频: https://www.youtube.com/watch?v=1uM8jhcqDP0
- 项目主页: https://openai.com/index/hello-gpt-4o/

#### dGSLM（生成式口语对话语言模型）（dGSLM (Generative Spoken Dialogue Language Modeling)） — Tu Anh Nguyen, Meta (2022-03-30)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码, 仅限研究
- 输入: 语音与音频 → 输出: 语音 / 声音
- 核心想法: 证明了轮流说话、重叠发言和“嗯嗯”这类附和可以直接从双声道原始音频中学到，是全双工语音智能体在概念上的前身。
- 内容: 一个不依赖文本的模型，直接从音频生成双声道口语对话，包括两位说话人之间的重叠发言、笑声和附和语。给它一段真实对话的开头，它会以音频形式同时续写双方。
- 实现方式: 为每个说话人的声道提取离散 HuBERT 单元，用带交叉注意力的双塔 Transformer 建模，在约 2000 小时的 Fisher 电话对话上训练。
- 参数: 2 audio channels · ~2,000 h training audio
- 能力维度: 行为似真性, 时间响应性
- 论文: https://arxiv.org/abs/2203.16502 (TACL 2023)
- 图片: https://speechbot.github.io/dgslm/figure.png
- 项目主页: https://speechbot.github.io/dgslm/
- 代码: https://github.com/facebookresearch/fairseq/tree/main/examples/textless_nlp/dgslm

### 富表现力语音与声音克隆

带情绪、节奏与音色设计的语音合成；用几秒音频克隆声音。

#### Eleven v4 — ElevenLabs (2026-09-28)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 公开 API, 产品 / 应用
- 输入: 文字提示 → 输出: 语音 / 声音
- 核心想法: 一次生成里同时包含表演指示和行内声音提示，模糊了“一句台词”和“一个小型声音场景”之间的界线。
- 内容: ElevenLabs 2026 年的新一代语音合成：新架构、面向低延迟智能体的 Turbo 版本、同一声音跨多种语言，以及更稳定的声音克隆。ElevenLabs 表示，它比 v3 更准确地遵循 [laughs]、[said angrily in French accent] 这类行内指示，甚至 [light rain] 这样的声音提示。
- 实现方式: 新的语音合成架构（未公开），另有用于实时场景的 Turbo 模型；遵循音频标签与表演指示提示。
- 参数: v4 + v4 Turbo
- 能力维度: 感知真实感, 创作可及性
- 视频: https://www.youtube.com/watch?v=th_tXR2QQ6U
- 图片: https://eleven-public-cdn.elevenlabs.io/payloadcms/3o2hqbr4pb7-1920x1080.webp
- 项目主页: https://elevenlabs.io/blog/eleven-v4
- API 文档: https://elevenlabs.io/docs

#### TADA — Hume AI (2026-03-10)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 文字提示, 语音与音频 → 输出: 语音 / 声音
- 核心想法: 文本忠实度有保证对实验很重要：一个从不漏词、不多词的刺激声音，才是可控的刺激。
- 内容: Hume 开源的语音-语言模型，让文本与音频一一对齐，因此从结构上就不会漏词或凭空多出词。Hume 报告其实时率为 0.09，比同级别的大模型语音合成快五倍以上。
- 实现方式: 基于 Llama 的 1B（英语）与 3B（多语言）模型，配合每秒仅 2–3 帧的音频分词器，实现文本与声学的双重对齐。
- 参数: 1B / 3B · RTF 0.09 · 2-3 tokens per second of audio
- 能力维度: 实验控制, 时间响应性
- 论文: https://arxiv.org/abs/2602.23068 (arXiv 2026)
- 视频: https://www.youtube.com/watch?v=eT5c_nsAO_Q
- 图片: https://cdn.sanity.io/images/xqnc2for/production/05620681ef774dc41236f42520a269829e11851a-4800x2520.png?w=1200&h=630
- 项目主页: https://www.hume.ai/blog/opensource-tada
- 代码: https://github.com/HumeAI/tada

#### Eleven v3 — ElevenLabs (2025-06)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 公开 API, 产品 / 应用
- 输入: 文字提示 → 输出: 语音 / 声音
- 核心想法: 把剧本变成有打断、有情绪的表演场景，降低录制多样化有声刺激材料的成本。
- 内容: ElevenLabs 发布时表现力最强的语音合成模型，可用 [whispers]、[sighs]、[excited] 等行内音频标签来“导戏”，并能以 70 多种语言生成多人对话。2025 年 6 月以 alpha 版发布，2026 年 2 月 2 日正式可用。
- 实现方式: 一种新的语音合成架构（细节未公开），根据文本上下文和方括号音频标签控制情绪、语气与非语言声音。
- 参数: 70+ languages · multi-speaker dialogue
- 能力维度: 感知真实感, 创作可及性
- 视频: https://www.youtube.com/watch?v=zv_IoWIO5Ek
- 图片: https://eleven-public-cdn.elevenlabs.io/payloadcms/xffpzuby3yb-cover.webp
- 项目主页: https://elevenlabs.io/blog/eleven-v3
- API 文档: https://elevenlabs.io/docs

#### IndexTTS2 — 哔哩哔哩 (2025-06-23)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 文字提示, 语音与音频 → 输出: 语音 / 声音
- 核心想法: 时长控制让生成的语音准确落在指定时间点上；当语音必须与生成视频或预设的 VR 事件同步时，这一点必不可少。
- 内容: 哔哩哔哩 Index 团队的开源零样本语音合成模型：用一小段样本克隆声音，情绪与音色可分别控制，还能精确指定输出时长，正好满足配音所需。它的演示为电影和动画片段重新配音，涵盖中文与英文。
- 实现方式: 自回归的文本到语义 Transformer，通过显式的标记数量控制时长，并解耦说话人与情绪提示；之后接语义到梅尔谱模型和声码器。
- 能力维度: 实验控制, 感知真实感
- 论文: https://arxiv.org/abs/2506.21619 (arXiv 2025)
- 视频: https://index-tts.github.io/index-tts2.github.io/ex6/Let_the_Bullets_Fly_1.mp4
- 项目主页: https://index-tts.github.io/index-tts2.github.io/
- 代码: https://github.com/index-tts/index-tts

#### Octave — Hume AI (2025-02-26)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 公开 API, 产品 / 应用
- 输入: 文字提示 → 输出: 语音 / 声音
- 核心想法: 用描述来设计声音，实验者可以直接指定角色（“一位紧张的年轻急救员”），而不必在现成声音库里翻找。
- 内容: Hume 基于大模型的语音合成：能从剧本中推断台词该怎么说（低声说出秘密、得意地高喊），并能根据文字描述创造新的声音。之后的 Octave 2 扩展到更多语言。
- 实现方式: 一个经训练能理解并合成语音的语音-语言模型，根据文本、表演指示和上下文预测语调、节奏与音色。
- 能力维度: 感知真实感, 创作可及性
- 视频: https://www.youtube.com/watch?v=rKcgsg0HBlY
- 图片: https://cdn.sanity.io/images/xqnc2for/production/9b31d5726693ff81fd8347008940845ea7824338-1080x1080.png?rect=0,257,1080,567&w=1200&h=630
- 项目主页: https://www.hume.ai/blog/octave-the-first-text-to-speech-model-that-understands-what-its-saying
- API 文档: https://dev.hume.ai/docs/text-to-speech-tts/overview

### 音效、音乐与视频配音

生成拟音、环境声、音乐，以及与视频同步的配乐。

#### Seed Audio 1.0 音频创作模型（Seed Audio 1.0） — 字节跳动 Seed (2026-07-20)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 公开 API
- 输入: 文字提示 → 输出: 音效、音乐与空间音频, 语音 / 声音
- 核心想法: 生成的是整个声音场景，而不是零散的片段，更接近人们在沉浸情境中真实听到的样子。
- 内容: 字节跳动 Seed 的场景级音频创作模型，用一个提示同时生成语音、音效、环境声与背景质感，让一句台词连同房间混响、脚步声和警报声一起出现。可通过 BytePlus 使用。
- 实现方式: 统一的生成框架，联合建模同一场景中的语音、音效与环境声（架构未公开）。
- 能力维度: 创作可及性, 感知真实感
- 视频: https://lf3-static.bytednsdoc.com/obj/eden-cn/lapzild-tss/ljhwZthlaukjlkulzlp/user-upload/4xfa4mrsklaag.mp4
- 项目主页: https://seed.bytedance.com/en/blog/from-speech-to-audio-creation-introducing-the-seed-audio-1-0-audio-creation-model

#### Suno v5.5 — Suno (2026-03-26)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 产品 / 应用
- 输入: 文字提示, 语音与音频 → 输出: 音效、音乐与空间音频
- 核心想法: 个人声音与风格模型，让音乐生成从千篇一律的曲目走向个人自己的声音身份。
- 内容: Suno 歌曲生成器的 2026 年版本，新增 Voices（用你自己录制的声音演唱）、按创作者作品定制的模型，以及个人口味画像。它是 Suno v5（2025 年 9 月）的后续版本。
- 实现方式: 专有的歌曲生成模型（可能是基于音频标记的 Transformer），具备声音克隆与按用户定制模型的功能。
- 能力维度: 创作可及性, 共创与能动性
- 视频: https://www.youtube.com/watch?v=eVlFcpX1VGA
- 图片: https://suno.com/blog/v5-5/opengraph-image?4a0be6b3238f1ddc
- 项目主页: https://suno.com/blog/v5-5

#### Lyria 3 — 谷歌 DeepMind (2026-02-18)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 产品 / 应用, 公开 API
- 输入: 文字提示, 图像 → 输出: 音效、音乐与空间音频
- 核心想法: 从图像生成音乐，让配乐可以从场景的外观中推导出来，使音乐与场景保持一致。
- 内容: Google DeepMind 2026 年带人声的音乐模型，2026 年 2 月 18 日在 Gemini 应用中上线，随后推出生成完整歌曲的 Lyria 3 Pro（2026 年 3 月 25 日）和 Lyria 3.5（2026 年 9 月 3 日正式可用）。它接受文字和图像提示，所有输出都带 SynthID 水印。
- 实现方式: 带人声的生成式音乐模型（架构未公开），提供 30 秒片段与完整歌曲两种版本；输出带 SynthID 水印。
- 参数: 48 kHz stereo (Lyria 3 API) · 44.1 kHz stereo (Lyria 3.5)
- 能力维度: 创作可及性, 感知真实感
- 视频: https://www.youtube.com/watch?v=Op8X8RmiE98
- 图片: https://storage.googleapis.com/gweb-uniblog-publish-prod/images/0217_KeywordHeaderFinalc.width-1300.png
- 项目主页: https://blog.google/innovation-and-ai/products/gemini-app/lyria-3
- API 文档: https://ai.google.dev/gemini-api/docs/music-generation

#### Stable Audio 2.5 — Stability AI (2025-09-10)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 公开 API, 产品 / 应用
- 输入: 文字提示 → 输出: 音效、音乐与空间音频
- 核心想法: 快速的声音设计加上开源的同系列模型，使其成为可锁定版本、可复现的刺激材料制作方案。
- 内容: Stability AI 面向企业的音乐与声音设计模型；Stability 称其能在一块 GPU 上用不到两秒生成最长三分钟的曲目，并支持音频修补。开源的 Stable Audio Open（2024）和 Stable Audio 3 系列（2026 年 5 月，在 Hugging Face 上提供小型与中型的音乐与音效模型）为实验室提供了可下载的替代方案。
- 实现方式: 潜空间扩散 Transformer，采用对抗式相对-对比（ARC）后训练以实现少步采样，训练数据经过授权。
- 参数: up to 3 min of audio in < 2 s (Stability)
- 能力维度: 创作可及性, 实验控制
- 视频: https://www.youtube.com/watch?v=zlldXbV72SM
- 图片: http://static1.squarespace.com/static/6213c340453c3f502425776e/62f2452bc121595f4d87c713/68af30c1f7616137793f399f/1765490304733/StableAudio2.5_Thumbnail_1x1_v5+%281%29.png?format=1500w
- 项目主页: https://stability.ai/news/stability-ai-introduces-stable-audio-25-the-first-audio-model-built-for-enterprise-sound-production-at-scale
- 代码: https://huggingface.co/stabilityai/stable-audio-3-medium

#### 混元 HunyuanVideo-Foley 视频拟音（HunyuanVideo-Foley） — 腾讯混元 (2025-08)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 视频, 文字提示 → 输出: 音效、音乐与空间音频
- 核心想法: 在文字要求与画面内容之间取得平衡，声音设计师可以用提示来引导一个场景的拟音。
- 内容: 腾讯混元的开源“文本+视频到音频”模型，生成与画面匹配的高保真拟音和环境声。它的演示页在相同片段上与 MMAudio、FoleyCrafter 和 ThinkSound 并排对比。
- 实现方式: 多模态扩散 Transformer，采用音视频联合注意力与文本交叉注意力，并与自监督音频特征做表征对齐，在大规模自动筛选的数据集上训练。
- 能力维度: 感知真实感, 实验控制
- 论文: https://arxiv.org/abs/2508.16930 (arXiv 2025)
- 视频: https://texttoaudio-train-1258344703.cos.ap-guangzhou.myqcloud.com/hunyuanvideo-foley_demo/demo_show/1-1.mp4
- 图片: https://opengraph.githubassets.com/4837e51d5700901b7328e37eca87975e75c4648e45fdbd4bfb31c6d00d89539f/Tencent-Hunyuan/HunyuanVideo-Foley
- 项目主页: https://szczesnys.github.io/hunyuanvideo-foley/
- 代码: https://github.com/Tencent-Hunyuan/HunyuanVideo-Foley

#### Eleven Music — ElevenLabs (2025-08-05)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 公开 API, 产品 / 应用
- 输入: 文字提示 → 输出: 音效、音乐与空间音频
- 核心想法: 经授权、可编辑的音乐生成，降低了随研究一同发表的刺激材料的版权风险。
- 内容: ElevenLabs 的音乐模型，可根据提示生成录音室品质、带或不带人声的歌曲，支持按段落编辑和多语言歌词；ElevenLabs 表示，通过与音乐版权方的授权合作，它可用于商业用途。之后推出了 Music v2 和 Music v2.5（2026 年 9 月 11 日）。
- 实现方式: 文本到音乐模型，可在结构层面控制段落、歌词与风格（架构未公开）。
- 能力维度: 创作可及性, 实验控制
- 视频: https://www.youtube.com/watch?v=VDwTSuKbrg8
- 图片: https://eleven-public-cdn.elevenlabs.io/payloadcms/qoyke7g9a6g-image%20(44).webp
- 项目主页: https://elevenlabs.io/blog/eleven-music-is-here
- API 文档: https://elevenlabs.io/docs

#### Lyria RealTime — 谷歌 DeepMind (2025-05)
- 类型: 模型 · 时序: 实时流式 · 获取方式: 公开 API, 产品 / 应用
- 输入: 文字提示 → 输出: 音效、音乐与空间音频
- 核心想法: 自适应配乐：音乐随情境的展开而变化，而不是从歌单里挑一首。
- 内容: 一个持续输出音乐流的模型，人们可以通过混合、调整文字提示的权重来实时引导音乐走向；它用于 MusicFX DJ，并在 Gemini API 中提供。其开源对应版本 Magenta RealTime 可在本地运行。
- 实现方式: 逐段生成音乐，以前面的音频以及可变、带权重的文字提示为条件（细节大多未公开；开源的 Magenta RealTime 很可能采用相同的流式方案）。
- 能力维度: 时间响应性, 共创与能动性
- 视频: https://storage.googleapis.com/gdm-deepmind-com-prod-public/media/media/lyria_realtime_header.mp4
- 项目主页: https://deepmind.google/models/lyria/lyria-realtime/
- API 文档: https://ai.google.dev/gemini-api/docs/music-generation

#### MMAudio — Ho Kei Cheng (2024-12)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 视频, 文字提示 → 输出: 音效、音乐与空间音频
- 核心想法: 快速、开源的拟音能力，让生成流程可以为每段视频配上可信的声音，但它不生成可懂的语音或有结构的音乐。
- 内容: 一个开源的视频配音模型，为无声视频添加同步的音效与环境声；作者报告最小的模型约 1.2 秒即可为 8 秒视频生成音频。它已成为被广泛使用的开源拟音基线。
- 实现方式: 基于流匹配的多模态 Transformer，在视频-音频与大规模文本-音频数据上联合训练，并用同步模块将音频与视频帧特征对齐。
- 参数: 157M-1.03B parameters · 8 s audio in ~1.2 s (small model, authors)
- 能力维度: 感知真实感, 情境多样性
- 论文: https://arxiv.org/abs/2412.15322 (CVPR 2025)
- 视频: https://www.youtube.com/watch?v=YElewUT2M4M
- 图片: https://opengraph.githubassets.com/9338427bbd0a4344c8597ed9e14235a566d9f7d523bd22ebe5ebc26f20250eaa/hkchengrex/MMAudio
- 项目主页: https://hkchengrex.github.io/MMAudio
- 代码: https://github.com/hkchengrex/MMAudio

#### V2A（视频生成音频）（V2A (video-to-audio)） — 谷歌 DeepMind (2024-06-17)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 视频, 文字提示 → 输出: 音效、音乐与空间音频, 语音 / 声音
- 核心想法: 逐帧跟随画面的声音，把一段无声的生成视频变成视听事件。
- 内容: Google DeepMind 的视频配音研究：为无声视频生成配乐、音效甚至对白，并可用可选的正向与反向文字提示来引导。
- 实现方式: 扩散模型以编码后的视频帧和文本为条件，从噪声中逐步生成音频；训练时使用 AI 生成的声音标注与对白文本；输出带 SynthID 水印。
- 能力维度: 感知真实感, 创作可及性
- 视频: https://www.youtube.com/watch?v=9Q0-t8D9XFI
- 项目主页: https://deepmind.google/discover/blog/generating-audio-for-video/

### 空间与全景声音频

在三维空间中定位与渲染的声音，为头显生成或升混。

#### ViSAGe：视频生成空间音频（ViSAGe） — Jaeyeon Kim (2025-06-13)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码, 仅限研究
- 输入: 视频, 镜头路径 / 位姿 → 输出: 音效、音乐与空间音频
- 核心想法: 可随头部追踪变化的视频空间声音：从立体声配乐迈向属于头显中三维场景的音频。
- 内容: 根据一段无声的视野视频及其镜头方向生成一阶全景声，使听者转头时声源仍停留在画面中对应的位置。作者还发布了 YT-Ambigen 数据集，包含约 10.2 万段带全景声的 YouTube 片段。
- 实现方式: 基于神经编解码器的自回归模型，以 CLIP 视频特征、分块能量图和镜头方向为条件生成全景声各声道，并提出了新的空间音频评测指标。
- 参数: first-order ambisonics (4 channels)
- 能力维度: 感知真实感, 实验控制
- 论文: https://arxiv.org/abs/2506.12199 (ICLR 2025)
- 视频: https://www.youtube.com/watch?v=awUvswKbNyQ
- 项目主页: https://jaeyeonkim99.github.io/visage/

#### OmniAudio：从 360° 视频生成空间音频（OmniAudio） — Huadai Liu (2025-04-21)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码, 仅限研究
- 输入: 视频 → 输出: 音效、音乐与空间音频
- 核心想法: 与生成的 360° 视频天然配合：让一段被观看的全景画面变成一个在听觉上也有空间感的地方。
- 内容: 根据 360° 视频生成一阶全景声，使全景片段的声景在各个方向上都与观看者周围的画面一致。作者构建了 Sphere360 数据集，包含 10.3 万多段带空间音频的真实 360° 片段。
- 实现方式: 先在空间与非空间音频上做自监督流匹配预训练，再用全景视频与视野视频特征的双分支进行条件生成。
- 参数: first-order ambisonics · Sphere360 103K clips
- 能力维度: 感知真实感, 情境可达性
- 论文: https://arxiv.org/abs/2504.14906 (ICML 2025)
- 视频: https://www.youtube.com/watch?v=Bg1xqWy0ugs
- 图片: https://opengraph.githubassets.com/a2469ea8c177f6d51c3aaafca025bf2971cf0717b6912d3d141e00bc591ac654/liuhuadai/OmniAudio
- 项目主页: https://github.com/liuhuadai/OmniAudio
- 代码: https://github.com/liuhuadai/OmniAudio

#### Both Ears Wide Open：语言驱动的空间音频生成（Both Ears Wide Open (BEWO)） — Peiwen Sun (2024-10-14)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码, 仅限研究
- 输入: 文字提示, 图像 → 输出: 音效、音乐与空间音频
- 核心想法: 用文字控制声音的位置与移动，作者无需声音引擎就能为 VR 场景编排空间线索。
- 内容: 根据文字描述生成双耳空间音频，按描述放置并移动声源（例如左边一只狗在叫，然后跑到右边），也接受图像提示。作者发布了约一百万对“文本—空间音频”的 BEWO-1M 数据集。
- 实现方式: SpatialSonic：单阶段潜空间扩散模型，由具备空间感知的文本与图像编码器以及方位角状态条件引导，在 BEWO-1M 上训练。
- 参数: binaural stereo · BEWO-1M dataset
- 能力维度: 实验控制, 创作可及性
- 论文: https://arxiv.org/abs/2410.10676 (ICLR 2025)
- 图片: https://peiwensun2000.github.io/bewo/static/I2A_audios/image_001.jpg
- 项目主页: https://peiwensun2000.github.io/bewo/
- 代码: https://github.com/PeiwenSun2000/Both-Ears-Wide-Open

#### Sounding Bodies：由身体姿态与音频建模人体三维空间声音（Sounding Bodies） — Xudong Xu, Meta (2023-11-01)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码, 仅限研究
- 输入: 身体、面部与视线追踪, 语音与音频 → 输出: 音效、音乐与空间音频
- 核心想法: 空间上正确的身体声音，才让“同在”的虚拟化身听起来真的同在；这个模型把它与被追踪的姿态联系起来。
- 内容: 根据头显麦克风音频和被追踪的身体姿态，渲染人体发出的完整三维声场（说话、脚步、拍手、打响指），让虚拟人从任何听音位置听起来都正确。与 Meta Reality Labs Research 合作完成。
- 实现方式: 神经网络把头戴麦克风信号与三维身体姿态映射为身体周围的声场，训练数据来自大型球形麦克风阵列录制的多视角采集。
- 能力维度: 感知真实感, 行为似真性
- 论文: https://arxiv.org/abs/2311.06285 (NeurIPS 2023)
- 图片: https://opengraph.githubassets.com/041b4f76c06e31a7107b494fd5503ebe36ad06f5021380c741bc640d600a9a6c/facebookresearch/SoundingBodies
- 项目主页: https://github.com/facebookresearch/SoundingBodies
- 代码: https://github.com/facebookresearch/SoundingBodies

## 交互式世界模型

以动作为条件的模型：根据键盘、手柄或智能体的输入生成世界的下一刻，例如 Genie 及其同类。已经可以“玩”，但持久性、可控性与头显支持仍是未解问题。

### 通用世界模型

由文字或一张图像生成可交互的世界：Genie 3、Project Genie、GWM-1、Mirage、Odyssey、Matrix-Game、Hunyuan-GameCraft……

#### Agora-2：多智能体世界模型（Agora-2） — Odyssey (2026-09)
- 类型: 模型 · 时序: 实时流式 · 获取方式: 候补 / 抢先体验
- 输入: 键盘与手柄动作 → 输出: 交互式帧流, 智能体行为与动作
- 核心想法: 共享的生成世界是社会情境的前提；Agora-2 展示了它的可行性，但目前局限于一款游戏的画面世界。
- 内容: 一个可游玩的多智能体世界模型研究预览：最多 20 名人类与 AI 智能体实时共处于同一个生成世界，每个人的动作都会改变其他人看到的画面；训练数据来自《暗黑破坏神 II》的游戏录像。
- 实现方式: 以配对了观察、动作与游戏状态的《暗黑破坏神 II》录像训练的世界模型，根据多名参与者的同时动作预测共享状态；相较 Agora-1（2026 年 5 月）参与人数增加 5 倍，并支持多个环境。
- 参数: up to 20 participants · real-time (developer-reported)
- 能力维度: 共创与能动性, 持久性, 行为似真性
- 视频: https://framerusercontent.com/assets/ZfcIM6TLKcPbbzfURMa87Lo6ww.mp4
- 图片: https://framerusercontent.com/assets/G8pOTIjyosApbiNbN1y31BVpbM.jpeg
- 项目主页: https://odyssey.ml/introducing-agora-2
- API 文档: https://agora.odyssey.systems

#### PixVerse R2（爱诗科技）（PixVerse R2） — 爱诗科技 PixVerse (2026-09-22)
- 类型: 模型 · 时序: 实时流式 · 获取方式: 产品 / 应用
- 输入: 键盘与手柄动作, 文字提示, 语音与音频 → 输出: 交互式帧流, 音效、音乐与空间音频
- 核心想法: 让后果在运行中的世界里延续，再加上语音输入，使世界模型向审讯、访谈这类交互情境靠近。
- 内容: 一个用于连续音视频交互的实时世界模型：用户用 WASD 移动，用提示改变天气或召来车辆，也可以说话或添加参考素材，而这些改变的后果会延续下去；PixVerse 自己的演示中包括实时审问一名 AI 嫌疑人。
- 实现方式: 在 PixVerse 音视频模型之上，把不同速率的移动、提示、音频与参考输入融合进同一个连续生成循环。
- 能力维度: 反应性, 持久性, 共创与能动性
- 视频: https://www.youtube.com/watch?v=PEGqOLcdVIs
- 图片: https://media.pixverse.ai/asset/blog/pixverse-r2-real-time-omni-world-model-cover-v5.webp
- 项目主页: https://pixverse.ai/en/model/pixverse-r2

#### GWM Worlds 2 — Runway (2026-09-03)
- 类型: 模型 · 时序: 实时流式 · 获取方式: 候补 / 抢先体验
- 输入: 文字提示, 镜头路径 / 位姿, 图像 → 输出: 交互式帧流, 音效、音乐与空间音频
- 核心想法: 把“持续存在的东西”（场景、角色、规则）与“发生的事”（带时间戳的事件）分开，这与实验者编排情境的方式非常接近。
- 内容: 一个可游玩世界模型的研究预览，同时流式生成画面与声音；一个人扮演角色，另一个人可以用发给任何对象的文字动作“导演”场景，比如挥剑、说一句话，或让房间进水。
- 实现方式: 基于 Runway 的音视频生成模型，由“WorldPrompt”驱动：包含场景、角色与规则的创世提示、首帧、带时间戳的自由文本动作流，以及逐帧镜头输入。
- 参数: 720p · 24 fps · 48 kHz audio · no preset session length (developer-reported)
- 能力维度: 共创与能动性, 实验控制, 反应性
- 视频: https://www.youtube.com/watch?v=pmjyB-lc4KQ
- 图片: https://d3phaj0sisr2ct.cloudfront.net/site/research/gwm-worlds-2/images/gwm-worlds-2-card.webp
- 项目主页: https://runway.com/research/introducing-gwm-worlds-2

#### LingBot-World 2.0（蚂蚁灵波）（LingBot-World 2.0） — 蚂蚁灵波科技 (2026-07-08)
- 类型: 开源工具 · 时序: 实时流式 · 获取方式: 开源权重 / 代码, 产品 / 应用
- 输入: 文字提示, 键盘与手柄动作, 图像 → 输出: 交互式帧流, 智能体行为与动作
- 核心想法: 把世界模型与两个大模型智能体搭配：一个负责行动、一个负责导演，这一模式可以直接对应实验中的“同谋者”与“实验者”角色。
- 内容: 第二代 LingBot 世界模型（又名 LingBot-World-Infinity），灵波科技称其为首个可交互一小时的世界模型：交互时长不设上限，支持攻击、射箭、施法等动作和文字驱动的事件，并配有智能体框架：“驾驶员”智能体负责游玩，“导演”智能体负责添加场景元素。
- 实现方式: 通过因果预训练实现无上限的推演，蒸馏出实时版本，并加入智能体框架：驾驶员智能体规划角色行为，导演智能体随场景推进合成新的环境元素。
- 参数: 720p · 60 fps real-time variant · hour-long sessions (developer-reported)
- 能力维度: 持久性, 反应性, 共创与能动性
- 论文: https://arxiv.org/abs/2607.07534 (arXiv 2026)
- 视频: https://www.youtube.com/watch?v=78l_RW_f12c
- 图片: https://raw.githubusercontent.com/Robbyant/lingbot-world-v2/main/assets/teaser.png
- 项目主页: https://technology.robbyant.com/lingbot-world-v2
- API 文档: https://www.reactor.inc/lingbot-world-v2
- 代码: https://github.com/Robbyant/lingbot-world-v2

#### Project Genie：街景锚定（Project Genie: Street View grounding） — 谷歌 DeepMind, 谷歌 (2026-05-19)
- 类型: 产品 / 应用 · 时序: 实时流式 · 获取方式: 产品 / 应用, 候补 / 抢先体验
- 输入: 图像, 文字提示, 键盘与手柄动作 → 输出: 交互式帧流
- 核心想法: 让生成的世界锚定在一条真实的街道上，使基于具体地点的情境成为可能；但它只是带风格化的起点，随着移动会逐渐偏离。
- 内容: 2026 年 I/O 大会上的更新，让 Project Genie 可以从真实地点出发：用户在地图上为美国某处放置图钉，选择“海洋世界”或“黑白电影”等风格并描述角色，Genie 便基于街景图像生成世界；同日向全球 Google AI Ultra 订阅用户开放。
- 实现方式: 通过谷歌的 Maps Imagery Grounding 调取街景图像作为开场画面的条件，之后由 Genie 3 根据用户动作实时延续世界。
- 参数: U.S. places at launch · global Google AI Ultra rollout (developer-reported)
- 能力维度: 情境可达性, 感知真实感, 创作可及性
- 视频: https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/GeoGenie_hero_small_kA4AQO6.mp4
- 图片: https://storage.googleapis.com/gweb-uniblog-publish-prod/images/projectgenie-social.width-1300.png
- 项目主页: https://blog.google/innovation-and-ai/models-and-research/google-deepmind/project-genie-expands/
- API 文档: https://labs.google/projectgenie

#### Waypoint-1.5 — Overworld (2026-04-09)
- 类型: 开源工具 · 时序: 实时流式 · 获取方式: 开源权重 / 代码, 产品 / 应用
- 输入: 文字提示, 图像, 键盘与手柄动作 → 输出: 交互式帧流
- 核心想法: 让世界模型跑在消费级硬件上：实验室可以离线运行、记录会话，并避开云端延迟。
- 内容: 一个开源权重的实时世界模型，可在游戏电脑上本地运行或通过串流使用，把一段提示或一张图像变成可探索的第一人称世界；它是 Waypoint-1（2026 年 1 月）的后继，2026 年 10 月 Waypoint 2 正在分批邀请开发者内测。
- 实现方式: 实时扩散世界模型，配有把用户输入改写为种子图像、合成视频与对齐操控信号的提示流程；分为 720p 与 360p 两档，可本地运行或串流。
- 参数: up to 720p · 60 fps · 1B parameters · consumer GPUs (developer-reported)
- 能力维度: 时间响应性, 创作可及性
- 视频: https://www.youtube.com/watch?v=W2vDzB4KvxU
- 图片: https://over.world/blog/waypoint-1-5/og.jpg
- 项目主页: https://over.world/blog/waypoint-1-5
- 代码: https://huggingface.co/Overworld/Waypoint-1.5-1B

#### Project Genie — 谷歌 DeepMind, 谷歌 (2026-01-29)
- 类型: 产品 / 应用 · 时序: 实时流式 · 获取方式: 产品 / 应用, 候补 / 抢先体验
- 输入: 文字提示, 图像, 键盘与手柄动作 → 输出: 交互式帧流
- 核心想法: 首次把实时世界模型交到付费用户手中：创作一个世界只需一句话加一张图，但体验一分钟就会结束。
- 内容: Google Labs 推出的网页原型，由 Genie 3、Nano Banana Pro 与 Gemini 驱动：Google AI Ultra 订阅用户用文字和图像勾勒世界与角色，以第一或第三人称探索，可改编他人的世界并下载视频；每次体验限时 60 秒。
- 实现方式: Nano Banana Pro 生成可编辑的预览图（“世界草图”），Gemini 可能负责理解提示，随后由 Genie 3 根据用户的移动与镜头输入实时生成前方的路。
- 参数: 60 s per generation · U.S. Google AI Ultra, 18+ at launch (developer-reported)
- 能力维度: 创作可及性, 时间响应性, 共创与能动性
- 视频: https://www.youtube.com/watch?v=YxkGdX4WIBE
- 图片: https://storage.googleapis.com/gweb-uniblog-publish-prod/images/genie-3__project-genie__hero-film_social-shar.width-1300.jpg
- 项目主页: https://blog.google/innovation-and-ai/models-and-research/google-deepmind/project-genie/
- API 文档: https://labs.google/projectgenie

#### LingBot-World（蚂蚁灵波）（LingBot-World） — 蚂蚁灵波科技 (2026-01-28)
- 类型: 开源工具 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 图像, 文字提示, 键盘与手柄动作 → 输出: 交互式帧流
- 核心想法: 来自中国实验室的开源分钟级世界模型，比 Project Genie 早一天发布，缩小了开源与闭源世界模型之间的差距。
- 内容: 蚂蚁集团灵波科技推出的开源世界模拟器，可在分钟级交互中保持写实、科学与卡通等不同风格世界的一致性，响应延迟低于一秒；可在 Reactor 平台在线试用。
- 实现方式: 由大型视频生成骨干派生、再经后训练获得动作条件、长期记忆与低延迟流式能力的世界模型；后续版本加入了快速版与动作版。
- 参数: 16 fps · < 1 s latency · minute-level horizon (developer-reported)
- 能力维度: 持久性, 时间响应性, 情境多样性
- 论文: https://arxiv.org/abs/2601.20540 (arXiv 2026)
- 视频: https://www.youtube.com/watch?v=Hg_giTANYks
- 图片: https://raw.githubusercontent.com/Robbyant/lingbot-world/main/assets/teaser.png
- 项目主页: https://technology.robbyant.com/lingbot-world
- 代码: https://github.com/Robbyant/lingbot-world

#### PixVerse R1（爱诗科技）（PixVerse R1） — 爱诗科技 PixVerse (2026-01-12)
- 类型: 模型 · 时序: 实时流式 · 获取方式: 产品 / 应用, 公开 API
- 输入: 文字提示, 图像 → 输出: 交互式帧流, 音效、音乐与空间音频
- 核心想法: 一款消费级视频应用被重新定义为实时世界：从“片段”转向“会话”，但代价是缺少游戏级的操控。
- 内容: PixVerse 的首个实时世界模型：持续生成一个带声音的实时场景，观看者用提示引导它，而不必等待成片；后续更新为合作伙伴开放 720p API，并加入共享世界与个性化虚拟形象。
- 实现方式: PixVerse 称其由三部分组成：原生多模态基础模型“Omni”、用于连续流式生成的自回归记忆，以及降低采样成本、实现低延迟的“即时响应引擎”。
- 参数: 1080p research claim · 720p via partner API (developer-reported)
- 能力维度: 时间响应性, 持久性
- 视频: https://media.pixverse.ai/asset/media/Fig/PixVerse-R1-demo-0.mp4
- 图片: https://media.pixverse.ai/asset/media/realtimecover.png
- 项目主页: https://pixverse.ai/en/blog/pixverse-r1-next-generation-real-time-world-model

#### 混元世界 1.5（WorldPlay）（HY-World 1.5 (WorldPlay)） — 腾讯混元 (2025-12-17)
- 类型: 开源工具 · 时序: 实时流式 · 获取方式: 开源权重 / 代码, 产品 / 应用
- 输入: 图像, 文字提示, 键盘与手柄动作 → 输出: 交互式帧流
- 核心想法: 在开源模型中同时做到实时交互与长期几何记忆，使“持久性”可以被研究，而不只是听厂商宣称。
- 内容: 开源的实时交互世界模型：从一张图像或一段文字流式生成可漫游的世界，用户回到原处时几何结构保持一致；后续版本加入了轻量的 5B 版本、训练代码以及强化学习后训练方法 WorldCompass。
- 实现方式: 基于 HunyuanVideo 的 8B 自回归视频模型，采用双重动作表示、按几何关系重新挑选历史帧的“重构上下文记忆”，以及用于实时提速的上下文强制蒸馏。
- 参数: 24 fps · 720p · real-time (developer-reported)
- 能力维度: 持久性, 时间响应性
- 论文: https://arxiv.org/abs/2512.14614 (arXiv 2025)
- 视频: https://github.com/user-attachments/assets/9fd12b40-41ab-4201-8667-8b333db1123d
- 图片: https://raw.githubusercontent.com/Tencent-Hunyuan/HY-WorldPlay/main/assets/teaser.webp
- 项目主页: https://3d-models.hunyuan.tencent.com/world/
- 代码: https://github.com/Tencent-Hunyuan/HY-WorldPlay

#### GWM-1 — Runway (2025-12-11)
- 类型: 模型 · 时序: 实时流式 · 获取方式: 候补 / 抢先体验, 公开 API
- 输入: 键盘与手柄动作, 镜头路径 / 位姿, 语音与音频 → 输出: 交互式帧流, 虚拟人（脸 / 身体）
- 核心想法: 同一个视频骨干同时服务于场景、人物与机器人，预示着用一个模型承载整个情境的可能，尽管各变体目前仍是独立模型。
- 内容: Runway 的首个通用世界模型系列，以三个后训练变体发布：用于可探索环境的 GWM Worlds、用于对话角色的 GWM Avatars，以及以机器人动作为条件生成视频的 GWM Robotics，并提供机器人 SDK。
- 实现方式: 基于 Gen-4.5 的自回归模型，逐帧生成，以镜头位姿、机器人指令或音频为条件。
- 参数: 720p · up to 2 min (developer-reported)
- 能力维度: 时间响应性, 反应性, 情境可达性
- 视频: https://www.youtube.com/watch?v=aevPpq4PIhE
- 图片: https://d3phaj0sisr2ct.cloudfront.net/site/images/research/gwm/gwm-card-01.png
- 项目主页: https://runwayml.com/research/introducing-runway-gwm-1
- API 文档: https://docs.dev.runwayml.com/

#### Odyssey-2 — Odyssey (2025-10-27)
- 类型: 模型 · 时序: 实时流式 · 获取方式: 产品 / 应用, 公开 API
- 输入: 文字提示, 图像 → 输出: 交互式帧流
- 核心想法: 让视频像聊天一样运作：边打字边引导画面，降低了创作门槛，但与游戏操控相比，文字指令较为粗略。
- 内容: 一个世界模型：输入提示几秒后便开始流式生成视频，观看者继续输入指令，画面随之改变，单次可持续数分钟，可在网页应用中体验；它是 Odyssey-1（2025 年 5 月）的后继，之后以 Odyssey-2 Pro 的形式开放 API。
- 实现方式: 因果自回归视频模型，根据此前的画面与当前文字生成每一帧，每 50 毫秒产出一帧。
- 参数: 20 fps · 50 ms per frame · multi-minute streams (developer-reported)
- 能力维度: 时间响应性, 共创与能动性, 创作可及性
- 视频: https://framerusercontent.com/assets/1RxJjsLhuFccE8n3TwpMnC8cNE.mp4
- 图片: https://framerusercontent.com/assets/iGnprsv1qq41yOKpOnTDNQNBrRs.jpg
- 项目主页: https://odyssey.ml/introducing-odyssey-2
- API 文档: https://developer.odyssey.ml

#### RTFM — World Labs (2025-10-16)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 候补 / 抢先体验
- 输入: 图像, 镜头路径 / 位姿 → 输出: 交互式帧流
- 核心想法: 把学习得到的模型当作带空间记忆的渲染器，是一条无需构建显式三维也能获得持久世界的路线。
- 内容: “实时帧模型”的研究预览：在浏览器中边走边渲染由单张图像生成的世界，包含反射、光泽与阴影；World Labs 称它只需一张 H100，且世界“永远不会被遗忘”。
- 实现方式: 端到端的逐帧自回归扩散 Transformer，存储的每一帧都带有三维位姿；通过调取附近帧作为上下文（“上下文轮换”）保持世界一致。
- 参数: 1× H100 · interactive frame rate (developer-reported)
- 能力维度: 持久性, 感知真实感, 时间响应性
- 视频: https://wlt-ai-cdn.art/videos/2025-10-15-v3/matchmove-icegleam.mp4
- 图片: https://www.worldlabs.ai/api/opengraph-image?imageUrl=/images/rtfm-thumbnail-glass.png&title=RTFM:%20A%20Real-Time%20Frame%20Model
- 项目主页: https://www.worldlabs.ai/blog/rtfm
- API 文档: https://rtfm.worldlabs.ai/

#### Mirage 2 — Dynamics Lab (2025-08-21)
- 类型: 模型 · 时序: 实时流式 · 获取方式: 候补 / 抢先体验
- 输入: 图像, 文字提示, 键盘与手柄动作 → 输出: 交互式帧流
- 核心想法: 在 2025 年展示了任何人都能走进自己的图片，但媒体实测发现操控松散、场景时有突变。
- 内容: 一款“生成式世界引擎”：把任意上传的图像（从照片到儿童画）变成可在浏览器中用 WASD 键游玩的世界，并允许玩家在游玩中用文字修改世界；2026 年 10 月核查时在线演示已下线。
- 实现方式: 据报道是一个基于 Transformer 的自回归扩散模型，根据图像与文字提示流式生成画面，并支持实时文字编辑。
- 参数: > 10 min sessions · ~200 ms latency · single GPU (developer-reported, via press)
- 能力维度: 创作可及性, 共创与能动性, 时间响应性
- 视频: https://www.youtube.com/watch?v=Ps55y7NPgTs
- 项目主页: https://www.gigazine.net/gsc_news/en/20250825-ai-generative-world-mirage-2

#### 混元 GameCraft（Hunyuan-GameCraft） — 腾讯混元 (2025-08-14)
- 类型: 开源工具 · 时序: 回合制 · 获取方式: 开源权重 / 代码
- 输入: 图像, 文字提示, 键盘与手柄动作 → 输出: 交互式帧流
- 核心想法: 让以动作为条件的视频达到 3A 游戏级画质，但每段动作是逐段生成的，而不是实时流式输出。
- 内容: 一个开源权重模型，把一张图像和一段文字变成以键盘鼠标操控的高动态游戏画面，并在长动作序列中保持场景一致；论文发布于 2025 年 6 月，权重于 2025 年 8 月开源。
- 实现方式: 基于 HunyuanVideo：把键盘鼠标输入统一到连续的镜头动作空间，用混合历史条件实现自回归延展，并通过蒸馏提速；训练数据为来自 100 多款 3A 游戏的逾百万段游戏录像。
- 能力维度: 反应性, 持久性, 感知真实感
- 论文: https://arxiv.org/abs/2506.17201 (arXiv 2025)
- 视频: https://hunyuan-gamecraft.github.io/assets/videos/main.mp4
- 图片: https://hunyuan-gamecraft.github.io/assets/images/pipeline.png
- 项目主页: https://hunyuan-gamecraft.github.io/
- 代码: https://github.com/Tencent-Hunyuan/Hunyuan-GameCraft-1.0

#### Matrix-Game 2.0（昆仑万维）（Matrix-Game 2.0） — 昆仑万维 Skywork (2025-08-12)
- 类型: 开源工具 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 图像, 键盘与手柄动作 → 输出: 交互式帧流
- 核心想法: 第一个被广泛使用的开源实时世界模型：实验室可以下载、运行并固定版本。
- 内容: 一个开源权重的世界模型，可从单张图像出发，以键盘鼠标操控，流式生成长达数分钟的交互视频，场景包括类 Minecraft、城市驾驶与 GTA 风格。
- 实现方式: 经蒸馏的少步因果扩散模型，用于自回归流式生成，配有动作注入模块，训练数据约为 1200 小时的虚幻引擎与 GTA5 交互数据。
- 参数: 25 fps · minute-level video (developer-reported)
- 能力维度: 时间响应性, 反应性
- 论文: https://arxiv.org/abs/2508.13009 (arXiv 2025)
- 视频: https://matrix-game-v2.github.io/static/videos/matrix-game2.mp4
- 图片: https://matrix-game-v2.github.io/static/imgs/architecture.png
- 项目主页: https://matrix-game-v2.github.io/
- 代码: https://github.com/SkyworkAI/Matrix-Game

#### Yan（腾讯）（Yan） — 腾讯 (2025-08-12)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入: 图像, 文字提示, 键盘与手柄动作 → 输出: 交互式帧流
- 核心想法: 把一个世界拆分为模拟、生成与实时编辑三部分；对需要在运行中修改情境的人来说，这是很有用的拆解方式。
- 内容: 一个由三部分组成的交互式视频框架：Yan-Sim 根据玩家输入以 1080p、60 fps 模拟游戏世界，Yan-Gen 根据文字和图像生成新的交互世界，Yan-Edit 允许玩家在游玩时用文字修改结构与风格。
- 实现方式: 采用高压缩、低延迟的 3D-VAE 与基于 KV 缓存的移位窗口去噪实现实时模拟，并配有为流式生成而蒸馏的多模态扩散生成器，以及把机制与画面渲染分离以便编辑的混合模型。
- 参数: 1080p · 60 fps (developer-reported)
- 能力维度: 感知真实感, 时间响应性, 共创与能动性
- 论文: https://arxiv.org/abs/2508.08601 (arXiv 2025)
- 视频: https://greatx3.github.io/Yan/videos_compressed/teaser.mp4
- 图片: https://greatx3.github.io/Yan/images/architecture/yan_sim.png
- 项目主页: https://greatx3.github.io/Yan/

#### Genie 3 — 谷歌 DeepMind (2025-08-05)
- 类型: 模型 · 时序: 实时流式 · 获取方式: 候补 / 抢先体验, 产品 / 应用
- 输入: 文字提示, 键盘与手柄动作 → 输出: 交互式帧流
- 核心想法: 第一个实时的通用世界模型：情境可以用文字描述后直接走进去，但只能持续几分钟而非几小时，而且人只能操控一个化身。
- 内容: 一个通用世界模型：根据文字提示生成可漫游的世界并实时流式输出；DeepMind 称其分辨率为 720p、帧率 24 fps，一致性可维持数分钟，还支持在体验中途改变天气或加入物体的“可提示世界事件”。
- 实现方式: 逐帧自回归生成，并关注此前的整条轨迹，使回到原处时场景保持一致，而无需显式三维表示；在大规模视频上训练。
- 参数: 720p · 24 fps · consistent for a few minutes · promptable world events (developer-reported)
- 能力维度: 时间响应性, 持久性, 情境可达性
- 视频: https://www.youtube.com/watch?v=PDKhUknuQDg
- 图片: https://lh3.googleusercontent.com/MZsGi3QroEY4lNLxrQVBVpn_5NZDXMCKwXs8nStlzGvjS7p76pP-FjyyO-hrYuBhERc60C5-KosmVJFfITEYN7wx_cV94Wju48IyYRwQ39_DtRDU=w1200-h630-n-nu-rw
- 项目主页: https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/

#### Genie 2 — 谷歌 DeepMind (2024-12-04)
- 类型: 模型 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 图像, 文字提示, 键盘与手柄动作 → 输出: 交互式帧流
- 核心想法: 把世界模型从二维游戏推进到丰富、具立体感的场景，但只能短时运行，且不是实时的。
- 内容: 一个基础世界模型：把一张提示图像变成看起来立体、可用键盘鼠标游玩的世界，包含物理、光照、NPC 与物体交互；DeepMind 称其一致性最长可维持约一分钟。
- 实现方式: 在视频帧潜空间上进行自回归扩散、以键盘鼠标动作为条件的模型，在大规模视频数据上训练；提示图像由 Imagen 3 生成。
- 参数: 10–20 s typical · up to ~1 min consistency (developer-reported)
- 能力维度: 情境多样性, 持久性, 情境可达性
- 视频: https://storage.googleapis.com/gdm-deepmind-com-prod-public/media/media/genie2_zoom_v6.mp4
- 图片: https://lh3.googleusercontent.com/NtYWmA3waHr1wi5OrNVdxndoSe4iS7Kui6GU4p8HvpFN_YrsbDcGudAgi4Nl-rN1geHpA4Czl0yXO6TQ73n8Q39oMmhDj_vbQ3rWNYE9EVLJcqm2=w1200-h630-n-nu-rw
- 项目主页: https://deepmind.google/discover/blog/genie-2-a-large-scale-foundation-world-model/

#### Genie — 谷歌 DeepMind (2024-02-23)
- 类型: 模型 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 图像, 键盘与手柄动作 → 输出: 交互式帧流
- 核心想法: 证明了操控方式可以从无标注视频中学出来，于是任何一张图片都能变成一个拥有少量“自发现动作”的世界。
- 内容: 一个 110 亿参数的模型，能把一张图像、草图或照片变成可游玩的二维平台游戏；它从网络游戏视频中学习，完全不需要动作标注。
- 实现方式: 由时空视频分词器、在帧间推断 8 个离散动作的潜在动作模型和自回归动力学模型组成，训练数据是从约 20 万小时网络视频中筛选出的 3 万小时二维平台游戏画面。
- 参数: 11B parameters · 8 latent actions · ~1 fps (developer-reported)
- 能力维度: 反应性, 情境多样性
- 获奖与认可: ICML 2024 Best Paper
- 论文: https://arxiv.org/abs/2402.15391 (ICML 2024)
- 视频: https://www.youtube.com/watch?v=DSVsnCDTyfc
- 项目主页: https://sites.google.com/view/genie-2024/home

### 神经游戏引擎

由神经网络逐帧渲染的游戏：GameNGen、DIAMOND、Oasis、Muse / WHAM、WHAMM……

#### Matrix-Game 4.0（昆仑万维）（Matrix-Game 4.0） — 昆仑万维 Skywork (2026-10-15)
- 类型: 开源工具 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 键盘与手柄动作, 文字提示, 场景规格、代码与规则 → 输出: 交互式帧流
- 核心想法: 把状态与规则交还给引擎，只让模型负责外观，从而找回持久性与实验控制。
- 内容: 一次开源发布：游戏逻辑、物理与玩家输入都留在真正的游戏引擎中，因果视频模型只负责把引擎输出的低多边形画面变成精细画面；附带三款可玩游戏（中世纪城堡、古埃及、城市赛车）的权重与源代码。
- 实现方式: 流式神经渲染：少步因果视频模型以可执行引擎输出的低多边形 RGB 画面和文字提示为条件，逐段渲染后续画面。
- 参数: 864×480 · up to 67 fps on RTX 5080 (developer-reported)
- 能力维度: 实验控制, 持久性, 感知真实感
- 视频: https://matrix-game-v4-0.github.io/page/assets/prompt/egypt06.mp4
- 图片: https://matrix-game-v4-0.github.io/page/assets/fig/overview_en.png
- 项目主页: https://matrix-game-v4-0.github.io/page/
- 代码: https://github.com/SkyworkAI/Matrix-Game

#### MIRA：多人交互世界模型（MIRA） — General Intuition, Kyutai (2026-07-06)
- 类型: 开源工具 · 时序: 实时流式 · 获取方式: 开源权重 / 代码, 产品 / 应用
- 输入: 键盘与手柄动作 → 输出: 交互式帧流, 智能体行为与动作
- 核心想法: 多人共享同一个生成情境并看到彼此的动作，背后没有任何游戏引擎；开发者称它可以无限运行而不发散。
- 内容: 一个开源的《火箭联盟》多人世界模型：四名玩家在浏览器中进行 2 对 2 比赛，每人看到的生成画面都保持一致，帧率 20 fps；加速槽、进球与撞毁全部由模型自行追踪；“自动驾驶”模式还能让模型替缺席的玩家上场。
- 实现方式: 以 6 亿参数的视频表征编解码器为基础的 50 亿参数扩散 Transformer，在机器人对局录像上以“动作随机丢弃”方式训练，并以四名玩家的输入为条件；由 General Intuition 与 Kyutai 联合 Epic Games 开发。
- 参数: 4 players · 20 fps · 576p split across players · 5B + 600M parameters (developer-reported)
- 能力维度: 共创与能动性, 持久性, 时间响应性
- 视频: https://mira-wm.com/media/hero-v2.mp4
- 项目主页: https://mira-wm.com/blog-post/
- 代码: https://github.com/mira-wm/mira

#### Dreamer 4：在可扩展世界模型中训练智能体（Dreamer 4） — Danijar Hafner, 谷歌 DeepMind (2025-09-29)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入: 键盘与手柄动作 → 输出: 交互式帧流, 智能体行为与动作
- 核心想法: 一个精确到足以训练智能体完成长任务的世界模型，而这恰恰也是把它当作可信测试平台所需的特性。
- 内容: 一个仅凭离线视频就学会在 Minecraft 中获得钻石的智能体：它在学到的世界模型里练习，而这个世界模型也能在单张 GPU 上实时供人类玩家游玩。
- 实现方式: 由因果分词器与高效 Transformer 动力学模型组成，采用“捷径强制”目标训练；智能体在想象推演上通过强化学习进行学习。
- 参数: real-time on 1 GPU (developer-reported)
- 能力维度: 反应性, 行为似真性
- 论文: https://arxiv.org/abs/2509.24527 (arXiv 2025)
- 视频: https://www.youtube.com/watch?v=oDlBtTcX0g0
- 项目主页: https://danijar.com/project/dreamer4/

#### WHAMM — 微软 (2025-04-04)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 产品 / 应用, 仅限研究
- 输入: 键盘与手柄动作 → 输出: 交互式帧流
- 核心想法: 展示了复刻一个关卡所需的数据少得惊人，也展示了这种复刻的记忆有多短暂。
- 内容: 在 Copilot Labs 中推出的《雷神之锤 II》关卡实时 AI 版本，根据手柄输入以 640×360 生成画面；微软指出，物体离开视野约一秒后就会被遗忘，延迟也较明显；项目页面现将其称为 WHAM-RT。
- 实现方式: MaskGIT 式的世界与人类动作模型，可并行生成图像 token；训练数据仅为一周经过精选的《雷神之锤 II》游玩录像，上下文长度为 0.9 秒（9 帧）。
- 参数: 640×360 · 10+ fps · 0.9 s context (developer-reported)
- 能力维度: 时间响应性, 反应性
- 视频: https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/vid1_square.mp4
- 图片: https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/whamm_overview.png
- 项目主页: https://www.microsoft.com/en-us/research/articles/whamm-real-time-world-modelling-of-interactive-environments/

#### Muse（世界与人类动作模型 WHAM）（Muse (WHAM)） — 微软 (2025-02-19)
- 类型: 模型 · 时序: 回合制 · 获取方式: 开源权重 / 代码, 仅限研究
- 输入: 图像, 键盘与手柄动作 → 输出: 交互式帧流, 智能体行为与动作
- 核心想法: 它不仅模拟世界，也模拟玩家的动作，因此能预测人接下来可能做什么，而不仅是会看到什么。
- 内容: 一个“世界与人类动作模型”，用 Xbox 游戏《Bleeding Edge》约七年的人类游玩数据训练，可生成游戏画面、手柄动作或两者，一致性可维持长达两分钟；权重与 WHAM Demonstrator 工具已向研究者开放；2026 年 9 月 23 日，微软把 WHAM 团队与技术并入 Microsoft AI 产品部门。
- 实现方式: 16 亿参数的 Transformer，交替预测图像 token 与手柄动作 token，在超过 10 亿帧 300×180 分辨率的画面与手柄动作（相当于 7 年以上的游玩时长）上训练，与 Ninja Theory 合作开发。
- 参数: 1.6B parameters · 300×180 · up to 2 min consistency (developer-reported)
- 能力维度: 持久性, 创作可及性, 情境多样性
- 论文: https://doi.org/10.1038/s41586-025-08600-3 (Nature 2025)
- 视频: https://www.microsoft.com/en-us/research/wp-content/uploads/2025/02/BE-Play-Session-edited.mp4
- 图片: https://www.microsoft.com/en-us/research/wp-content/uploads/2025/02/WHAM-TWLIFB-1200x627-1.jpg
- 项目主页: https://www.microsoft.com/en-us/research/blog/introducing-muse-our-first-generative-ai-model-designed-for-gameplay-ideation/
- 代码: https://huggingface.co/microsoft/wham

#### GameFactory：用生成式交互视频创造新游戏（GameFactory） — Jiwen Yu, 快手 / 可灵 (2025-01-14)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 开源权重 / 代码, 仅限研究
- 输入: 文字提示, 键盘与手柄动作 → 输出: 平面视频
- 核心想法: 把“怎么移动”与“世界长什么样”分开，正是这一点让实验室无需新的游戏数据就能编排新情境。
- 内容: 一种把新游戏当作交互视频来创作的方法：把在 Minecraft 中学到的动作控制迁移到由文字生成的开放场景，玩家可以在训练数据中从未出现过的世界里行走、环顾。
- 实现方式: 在预训练视频扩散模型上加入风格解耦 LoRA，以及在 GF-Minecraft 数据集上训练的独立动作控制模块，并以自回归方式延展为长视频。
- 能力维度: 情境多样性, 创作可及性, 实验控制
- 论文: https://arxiv.org/abs/2501.08325 (ICCV 2025 (Highlight))
- 视频: https://yujiwen.github.io/gamefactory/videos/gallery/1.mp4
- 图片: https://yujiwen.github.io/gamefactory/static/assets/layout.jpg
- 项目主页: https://yujiwen.github.io/gamefactory/
- 代码: https://github.com/KwaiVGI/GameFactory

#### Oasis — Decart, Etched (2024-10-31)
- 类型: 模型 · 时序: 实时流式 · 获取方式: 开源权重 / 代码, 产品 / 应用
- 输入: 键盘与手柄动作 → 输出: 交互式帧流
- 核心想法: 第一个被大规模试玩的实时 AI 游戏世界，也暴露出缺少锚定的世界会多么迅速地忘记你身后的东西。
- 内容: 一个类 Minecraft 的开放世界，根据键盘鼠标输入逐帧生成，可在浏览器中以约 20 fps 游玩；代码与 5 亿参数的模型权重随在线演示（使用更大的模型）一同开源。
- 实现方式: 由 ViT 自编码器与扩散 Transformer 根据历史帧与动作自回归生成每一帧，采用 Diffusion Forcing 训练；Etched 计划用其 Sohu 芯片支撑更高分辨率。
- 参数: ~20 fps · 500M open weights (developer-reported)
- 能力维度: 时间响应性, 反应性
- 视频: https://oasis-model.github.io/wide1.mp4
- 图片: https://oasis-model.github.io/1.webp
- 项目主页: https://oasis-model.github.io/
- 代码: https://github.com/etched-ai/open-oasis

#### GameNGen：扩散模型即实时游戏引擎（GameNGen） — 谷歌, 谷歌 DeepMind (2024-08-27)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入: 键盘与手柄动作 → 输出: 交互式帧流
- 核心想法: 证明了用神经网络实时渲染一整款游戏是可行的，但仅限于模型已“背熟”规则的那一款游戏。
- 内容: 第一个完全由神经模型驱动的游戏引擎：在单个 TPU 上以约 20 fps 交互式运行《毁灭战士》；开发者报告，人类评审区分生成片段与真实游戏的准确率仅略高于随机。
- 实现方式: 先由强化学习智能体录制游玩数据，再把 Stable Diffusion v1.4 在历史帧与动作上微调以预测下一帧，并对上下文加噪以防止漂移。
- 参数: ~20 fps · single TPU · PSNR 29.4 (developer-reported)
- 能力维度: 时间响应性, 感知真实感
- 论文: https://arxiv.org/abs/2408.14837 (ICLR 2025)
- 视频: https://www.youtube.com/watch?v=O3616ZFGpqw
- 图片: https://gamengen.github.io/static/images/embed_image.png
- 项目主页: https://gamengen.github.io/

#### DIAMOND：扩散世界模型（DIAMOND） — Eloi Alonso (2024-05-20)
- 类型: 开源工具 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 键盘与手柄动作 → 输出: 交互式帧流, 智能体行为与动作
- 核心想法: 画面细节对智能体很重要，而一个开源的小型扩散模型就足以构成可玩的三维游戏世界。
- 内容: 一个扩散世界模型：在想象中训练 Atari 智能体；作为演示，它还把《反恐精英：全球攻势》的游戏录像变成可在消费级显卡上游玩的 Dust II 地图。
- 实现方式: 以历史帧与动作为条件的 EDM 式扩散模型，既充当强化学习环境，又在 CS:GO 演示中作为带上采样器的两阶段生成器。
- 参数: Atari 100k mean HNS 1.46 · CS:GO playable at ~10 fps on RTX 3090 (developer-reported)
- 能力维度: 感知真实感, 反应性
- 论文: https://arxiv.org/abs/2405.12399 (NeurIPS 2024 (Spotlight))
- 视频: https://x.com/EloiAlonso1/status/1793916382779982120
- 图片: https://diamond-wm.github.io/static/gifs/half_diamond.gif
- 项目主页: https://diamond-wm.github.io/
- 代码: https://github.com/eloialonso/diamond

#### GameGAN — Seung Wook Kim, 英伟达 (2020-05-22)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 开源权重 / 代码, 仅限研究
- 输入: 键盘与手柄动作 → 输出: 交互式帧流
- 核心想法: 第一个被广泛展示的神经游戏引擎：游戏的规则与画面都可以从游玩数据中学出来。
- 内容: 一个生成模型，仅凭 5 万局游戏录像（画面与按键）就学会重建可玩的《吃豆人》，完全不接触游戏引擎；英伟达在该游戏 40 周年之际发布了它。
- 实现方式: 由动力学引擎、保持迷宫一致的外部记忆模块，以及把静态背景与运动角色分开的渲染引擎组成的 GAN。
- 能力维度: 反应性, 持久性
- 论文: https://arxiv.org/abs/2005.12126 (CVPR 2020)
- 视频: https://www.youtube.com/watch?v=BYt6r8z6pUY
- 项目主页: https://nv-tlabs.github.io/gameGAN/
- 代码: https://github.com/nv-tlabs/GameGAN_code

#### 世界模型（World Models）（World Models） — David Ha (2018-03-27)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 开源权重 / 代码, 仅限研究
- 输入: 键盘与手柄动作 → 输出: 交互式帧流, 智能体行为与动作
- 核心想法: 这条谱系从这里开始：学习得到的模拟器可以替代真实环境，而它的缺陷也可能被身处其中的行动者利用。
- 内容: 一篇交互式论文：智能体先学会赛车游戏和 VizDoom 的压缩模型，然后完全在自己生成的“梦境”中训练，再把学到的策略迁回真实游戏；读者可以在浏览器里进入这个梦境游玩。
- 实现方式: 用 VAE 压缩画面，用混合密度 RNN 根据动作预测下一潜在状态，再在 RNN 的推演中用 CMA-ES 进化一个小型控制器。
- 能力维度: 反应性
- 论文: https://arxiv.org/abs/1803.10122 (NeurIPS 2018 (as 'Recurrent World Models Facilitate Policy Evolution'))
- 视频: https://www.youtube.com/watch?v=HzA8LRqhujk
- 图片: https://worldmodels.github.io/assets/world_models_card_both.png
- 项目主页: https://worldmodels.github.io/
- 代码: https://github.com/hardmaru/WorldModelsExperiments

### 面向机器人与驾驶的世界模型

预测世界如何回应智能体的物理 AI 模拟器：Cosmos、GAIA、V-JEPA 2、UniSim……

#### Odyssey-3 — Odyssey (2026-09-15)
- 类型: 模型 · 时序: 实时流式 · 获取方式: 产品 / 应用, 公开 API
- 输入: 文字提示, 键盘与手柄动作, 视频 → 输出: 交互式帧流, 智能体行为与动作
- 核心想法: 同一个世界模型既是模拟器又是控制器，这意味着同一个模型可以同时扮演环境和其中的智能体。
- 内容: Odyssey 的第三代基础世界模型；公司称，它既能生成交互世界，也能借助用数小时数据训练的小型动作解码器，控制机械臂、人形机器人、汽车、无人机和游戏角色。
- 实现方式: 在大量视觉观察数据上训练的自回归扩散 Transformer；针对具体任务的动作解码器把其内部表征转换为控制信号。
- 参数: few to tens of hours of task data per embodiment (developer-reported)
- 能力维度: 适应性, 情境可达性, 行为似真性
- 视频: https://framerusercontent.com/assets/J2EGlzwE6xA1NPIEdgwQypDfz1A.mp4
- 图片: https://framerusercontent.com/assets/JU7BjLegfmzvfZ2iaaZ0CIAWWag.jpg
- 项目主页: https://odyssey.ml/introducing-odyssey-3
- API 文档: https://developer.odyssey.ml

#### GAIA-4 — Wayve (2026-08-03)
- 类型: 模型 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 视频, 键盘与手柄动作, 场景规格、代码与规则 → 输出: 平面视频
- 核心想法: 闭环且锚定在真实记录上：反事实只改变由智能体决定所引起的部分，是做“如果……会怎样”测试的干净设计。
- 内容: 第四代 GAIA 世界模型，让 Wayve 的 AI 驾驶员参与闭环：一段真实行驶记录成为仿真的起点，每一次刹车或转向决定都会改变摄像头看到的画面，工程师因此可以测试从未发生过的未来。
- 实现方式: 多模态世界模型，以驾驶模型的动作为条件重新模拟传感器输入，同时让底层场景与原始记录保持一致，作为确定性的基线。
- 能力维度: 反应性, 实验控制, 情境可达性
- 视频: https://wayve.ai/wp-content/uploads/2026/07/GAIA-4-Trimmed-1.mp4
- 图片: https://wayve.ai/wp-content/uploads/2026/07/GAIA-4-Hero-Image.jpg
- 项目主页: https://wayve.ai/thinking/gaia-4/

#### Oasis 3 — Decart (2026-06-10)
- 类型: 模型 · 时序: 实时流式 · 获取方式: 公开 API
- 输入: 文字提示, 键盘与手柄动作 → 输出: 交互式帧流
- 核心想法: 罕见的长尾事件变成可以通过提示调用、直接驶入的场景，而不必在真实道路上苦等。
- 内容: Decart 面向物理 AI 的交互式世界模型，先从自动驾驶入手：根据一句提示生成多样、逼真的驾驶环境，并实时响应车辆的动作；发布当天即可通过 API 使用。
- 实现方式: 运行在 Decart 优化推理栈（DOS）上的实时生成式世界模型，以提示与车辆控制为条件，用于闭环机器人训练。
- 能力维度: 情境可达性, 时间响应性, 情境多样性
- 视频: https://www.youtube.com/watch?v=yeGmjZ8Nr1A
- 图片: https://cdn.prod.website-files.com/69ac78b058a3b8e6de5d1387/6a297d526275636705fa5eb5_oaasis.jpg
- 项目主页: https://decart.ai/publications/introducing-oasis-3-first-interactive-world-model-for-physical-ai
- API 文档: https://platform.decart.ai/

#### Cosmos 3 — 英伟达 (2026-05-31)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码, 公开 API
- 输入: 文字提示, 视频, 键盘与手柄动作 → 输出: 平面视频, 智能体行为与动作, 音效、音乐与空间音频
- 核心想法: 先推理情境、再进行模拟，这一步让生成的结果可以对照解释加以核查。
- 内容: 在 GTC 台北发布的开源“全能模型”：先理解场景，再生成视频与环境声，还能输出关节角度、夹爪位置等机器人动作数据，让一个模型同时负责描述、模拟与行动。
- 实现方式: 混合 Transformer 架构：推理模块先解读场景，生成模块再输出符合物理的视频、音频与数值动作；可后训练为世界-动作模型。
- 能力维度: 情境可达性, 行为似真性, 实验控制
- 视频: https://www.youtube.com/watch?v=q7Hj3J9SOXw
- 图片: https://blogs.nvidia.com/wp-content/uploads/2026/05/Featured-image.png
- 项目主页: https://blogs.nvidia.com/blog/cosmos-3-physical-ai-open-world-foundation-model/
- 代码: https://github.com/nvidia-cosmos

#### Waymo 世界模型（Waymo World Model） — Waymo, 谷歌 DeepMind (2026-02-06)
- 类型: 模型 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入: 文字提示, 键盘与手柄动作, 场景规格、代码与规则 → 输出: 平面视频, 动态三维 / 4D
- 核心想法: 通用世界模型的知识在用某一领域的传感器数据后训练之后，就能迁移到这个安全攸关的领域；其他高风险模拟也可以遵循这一模式。
- 内容: 一个基于 Genie 3 的驾驶模拟器，同时生成摄像头与激光雷达数据，可通过语言提示、驾驶输入和场景布局控制，用来演练龙卷风、路上出现大象或车辆逆行等罕见事件。
- 实现方式: 在 Waymo 驾驶数据上对 Genie 3 进行后训练，使其输出多传感器二维视频与三维激光雷达点云；当仿真偏离记录的事件时，改用高效的实时版本。
- 参数: camera + lidar output (developer-reported)
- 能力维度: 情境可达性, 实验控制, 感知真实感
- 视频: https://storage.googleapis.com/waymo-prod-cdn/uploads/bd1e232de236794e89f6daa89b594b93-topline_video_close_loop_sim_cropped.webm
- 图片: https://lh3.googleusercontent.com/pcL3e60qMHH67WyyOeA1d-8Tjx2B4kwe90bpyvAyWOgf8Clb40mPxyjhpSAaH1ZsJzvtOxhU-eMYvfy5G_YYPYyGvRmRYlLHxOs
- 项目主页: https://waymo.com/blog/2026/02/the-waymo-world-model-a-new-frontier-for-autonomous-driving-simulation

#### V-JEPA 2 — Meta (2025-06-11)
- 类型: 模型 · 时序: 回合制 · 获取方式: 开源权重 / 代码
- 输入: 视频, 图像 → 输出: 智能体行为与动作
- 核心想法: 世界模型不一定要渲染像素才有用；预测抽象的后果就足以支撑规划。
- 内容: 一个自监督视频世界模型，在学到的表征空间而不是像素空间中做预测；Meta 称，其动作条件版本能让机械臂在从未见过的实验室中零样本规划抓取放置任务。
- 实现方式: 联合嵌入预测架构，先在超过 100 万小时的网络视频与图像上预训练，再以 V-JEPA 2-AC 的形式在 DROID 数据集中不足 62 小时的无标注机器人视频上后训练，用于模型预测控制。
- 参数: 1.2B parameters · 1M+ hours of video · < 62 h robot data (developer-reported)
- 能力维度: 行为似真性, 适应性
- 论文: https://arxiv.org/abs/2506.09985 (arXiv 2025)
- 视频: https://about.fb.com/wp-content/uploads/2025/06/01_VJEPA2.mp4
- 图片: https://about.fb.com/wp-content/uploads/2025/06/VJEPA-2-Launch_Header-Cover_Social-Share.png?w=1200
- 项目主页: https://about.fb.com/news/2025/06/our-new-model-helps-ai-think-before-it-acts/
- 代码: https://github.com/facebookresearch/vjepa2

#### GAIA-2 — Wayve (2025-03-26)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 场景规格、代码与规则, 视频, 文字提示 → 输出: 平面视频
- 核心想法: 罕见且危险的交通情境可以用参数指定、按需生成，为情境可控的研究提供了范本。
- 内容: 一个生成式驾驶世界模型：根据自车运动、其他交通参与者、天气、时间与道路布局等结构化输入，生成一致的多摄像头驾驶视频，覆盖英国、美国与德国的道路；它是 GAIA-1（2023）的后继。
- 实现方式: 潜空间扩散世界模型，配有专用视频分词器和丰富的结构化条件（自车动力学、交通参与者配置、环境、道路语义），并可接入外部驾驶模型的嵌入。
- 参数: multi-camera · UK / US / Germany data (developer-reported)
- 能力维度: 情境可达性, 实验控制, 情境多样性
- 论文: https://arxiv.org/abs/2503.20523 (Technical report 2025)
- 视频: https://www.youtube.com/watch?v=bwTzVU1ib1I
- 图片: https://wayve.ai/wp-content/uploads/2025/03/Wayve-GAIA-2-Hero-Blog-Image.jpg
- 项目主页: https://wayve.ai/thinking/gaia-2/

#### Cosmos — 英伟达 (2025-01-06)
- 类型: 平台 / API · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 文字提示, 图像, 视频 → 输出: 平面视频
- 核心想法: 采用宽松许可的开源世界模型，实验室可以针对自己的环境微调，是机器人与驾驶仿真的默认基座。
- 内容: 在 CES 2025 上发布的面向物理 AI 的开放“世界基础模型”平台：包括视频分词器、数据筛选流程，以及生成物理上合理视频的扩散与自回归模型，用于训练机器人和自动驾驶；后续又加入 Predict、Transfer 与 Reason 系列模型。
- 实现方式: 扩散与自回归 Transformer 模型，在从 2000 万小时视频中筛选出的约 1 亿个片段上预训练，配有安全防护与针对镜头控制、机器人和驾驶的后训练方法。
- 参数: 4B–14B parameters · 20M hours of source video (developer-reported)
- 能力维度: 情境可达性, 情境多样性
- 论文: https://arxiv.org/abs/2501.03575 (arXiv 2025)
- 视频: https://www.youtube.com/watch?v=9Uch931cDx8
- 图片: https://www.nvidia.com/content/dam/en-zz/Solutions/ai/cosmos/nvidia-cosmos-og.jpg
- 项目主页: https://www.nvidia.com/en-us/ai/cosmos/
- 代码: https://github.com/nvidia-cosmos

#### 导航世界模型（Navigation World Models） — Amir Bar, Meta (2024-12-04)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 开源权重 / 代码
- 输入: 图像, 键盘与手柄动作 → 输出: 平面视频, 智能体行为与动作
- 核心想法: 把世界模型当作规划时的想象力，并且可以在规划时临时加入约束。
- 内容: 一个可控视频模型，能想象智能体沿某条候选路线会看到什么；机器人因此可以通过模拟轨迹、检查是否到达目标来规划路线，甚至能从单张图像出发在陌生环境中规划。
- 实现方式: 10 亿参数的条件扩散 Transformer（CDiT），在人类与机器人的第一人称视频上训练，以历史帧与导航动作为条件。
- 参数: 1B parameters (developer-reported)
- 能力维度: 实验控制, 反应性
- 获奖与认可: CVPR 2025 Best Paper Honorable Mention
- 论文: https://arxiv.org/abs/2412.03572 (CVPR 2025)
- 视频: https://www.amirbar.net/nwm/assets/known_environments/recon_ours_1_1080p.mp4
- 图片: https://www.amirbar.net/nwm/assets/nwm.png
- 项目主页: https://www.amirbar.net/nwm/
- 代码: https://github.com/facebookresearch/nwm

#### 1X 世界模型（1X World Model） — 1X Technologies (2024-09-17)
- 类型: 模型 · 时序: 回合制 · 获取方式: 开源权重 / 代码, 仅限研究
- 输入: 视频, 键盘与手柄动作 → 输出: 平面视频
- 核心想法: 把世界模型当作评估工具：先在想象中比较不同策略，再拿到真机上运行。
- 内容: 1X 为其人形机器人打造的学习型模拟器：从同一组起始画面出发，根据不同的动作方案想象多种未来，涵盖衣物、门、抽屉等刚性、可形变与带关节的物体；1X 还发布了数据集和公开挑战赛。
- 实现方式: 以 1X 自有机器人日志训练的动作条件视频预测模型，采用视频分词，并提供公开的 1xgpt 基线。
- 能力维度: 实验控制, 反应性
- 视频: https://www.youtube.com/watch?v=xPX6dDRYbV4
- 图片: https://cdn.sanity.io/images/qka6yvsc/production/1da42dae7a0f986a38880cd979a570e0fba70ddd-2048x1080.png?fit=max&auto=format
- 项目主页: https://www.1x.tech/discover/1x-world-model
- 代码: https://github.com/1x-technologies/1xgpt

#### UniSim：可交互的真实世界模拟器（UniSim） — Sherry Yang, 谷歌 DeepMind (2023-10)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 文字提示, 图像, 键盘与手柄动作 → 输出: 平面视频
- 核心想法: 把视频生成重新定义为真实世界交互的模拟器，这是从“视频模型”迈向“世界模型”的概念性一步。
- 内容: 一个“通用模拟器”：预测一个人或机器人执行文字描述的动作（如“切胡萝卜”“打开抽屉”）之后，摄像头会看到什么，从而让规划器和强化学习策略先在模拟中训练，再部署到真实机器人上。
- 实现方式: 以历史帧及文字或底层动作为条件的视频扩散模型，在精心组合的图像、视频、机器人与导航数据上训练，并通过自回归推演实现长时交互。
- 能力维度: 情境可达性, 反应性
- 获奖与认可: ICLR 2024 Outstanding Paper Award
- 论文: https://arxiv.org/abs/2310.06114 (ICLR 2024)
- 视频: https://universal-simulator.github.io/unisim/materials/cut_carrot-final.mp4
- 图片: https://universal-simulator.github.io/unisim/materials/unisim.png
- 项目主页: https://universal-simulator.github.io/unisim/

### 记忆、一致性与控制

让生成的世界保持连贯的研究：空间记忆、长上下文、可提示事件与状态。

#### WorldTrace：视频世界模型的可寻址记忆（WorldTrace） — Xindi Wu, 英伟达 (2026-08-07)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入: 键盘与手柄动作, 镜头路径 / 位姿 → 输出: 交互式帧流
- 核心想法: 指出世界模型遗忘的原因在于位置编码超出训练范围，并在不重新训练的情况下加以修复，让现有模型能运行更长的会话。
- 内容: 一种无需重新训练的修补方法，针对会话超出训练长度后就开始遗忘的交互视频世界模型：让模型压缩后的记忆仍可被准确寻址，使长时推演保持平滑，并能回想起曾经到过的场景。
- 实现方式: 把 KV 缓存压缩到固定、处于训练分布内的槽位，并用规范化键写入，避免把相位不兼容的 RoPE 平均在一起；两个变体分别面向平滑推演（Field）与场景回想（Landmark）。
- 能力维度: 持久性, 实验控制
- 论文: https://arxiv.org/abs/2608.07408 (NeurIPS 2026)
- 视频: https://research.nvidia.com/labs/sil/projects/WorldTrace/videos/teaser/worldtrace_panel_rotate90.mp4
- 图片: https://research.nvidia.com/labs/sil/projects/WorldTrace/figures/og-card.png
- 项目主页: https://research.nvidia.com/labs/sil/projects/WorldTrace/

#### Matrix-Game 3.0（昆仑万维）（Matrix-Game 3.0） — 昆仑万维 Skywork (2026-03-27)
- 类型: 开源工具 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 图像, 键盘与手柄动作, 镜头路径 / 位姿 → 输出: 交互式帧流
- 核心想法: 在开源模型中同时实现记忆与实时速度，但硬件成本（8 张 GPU）仍限制了实验室的使用。
- 内容: 一个开源权重、带记忆增强的交互世界模型：实时流式输出 720p 视频，并按相机位置调取相关历史帧，使长时会话中的场景保持一致；昆仑万维于 2026 年 8 月推出后续版本 Matrix-Game 3.5（块记忆）。
- 实现方式: 在 Matrix-Game 2.0 基础上构建的 50 亿参数自回归扩散模型，采用基于 GPU 的相机感知记忆检索、少步采样、INT8 量化、蒸馏和轻量 VAE。
- 参数: 720p · up to 40 fps · 5B parameters · 8 GPUs (developer-reported)
- 能力维度: 持久性, 时间响应性
- 论文: https://arxiv.org/abs/2604.08995 (arXiv 2026)
- 视频: https://matrix-game-v3.github.io/static/videos/teaser.mp4
- 图片: https://matrix-game-v3.github.io/static/imgs/mg3_overview.png
- 项目主页: https://matrix-game-v3.github.io/
- 代码: https://github.com/SkyworkAI/Matrix-Game

#### 具备长期空间记忆的视频世界模型（Video World Models with Long-term Spatial Memory） — Tong Wu (2025-06-05)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 镜头路径 / 位姿, 图像 → 输出: 平面视频, 三维场景 / 世界
- 核心想法: 把显式三维存储与生成模型结合：几何负责必须持久的部分，生成负责可以变化的部分。
- 内容: 一个视频世界模型：在保留近期画面与关键帧的同时，把静态场景的三维点云作为长期记忆，使长时间镜头移动后重访的地方看起来依然一致。
- 实现方式: 以几何为基础的三部分记忆：记录静态内容的点云空间记忆、记录近期画面的工作记忆和记录关键帧的情景记忆，共同作为视频扩散模型的条件。
- 能力维度: 持久性, 实验控制
- 论文: https://arxiv.org/abs/2506.05284 (arXiv 2025)
- 视频: https://spmem.github.io/static/videos/wm-demo.mp4
- 图片: https://spmem.github.io/static/images/teaser.jpg
- 项目主页: https://spmem.github.io/

#### 以上下文为记忆（Context-as-Memory）（Context-as-Memory） — Jiwen Yu, 快手 / 可灵 (2025-06-03)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 镜头路径 / 位姿, 图像 → 输出: 平面视频
- 核心想法: 按视野重叠做简单检索，效果胜过把过去压缩起来，而且记忆可以逐帧检查。
- 内容: 一种让长时交互视频中的生成场景保持一致的方法：把此前生成的所有画面都当作记忆，只调取与下一视角视野重叠的那些画面。
- 实现方式: 把历史帧拼接为视频扩散模型的上下文，并用记忆检索模块按相机视野重叠挑选帧，以限制计算量。
- 能力维度: 持久性
- 论文: https://arxiv.org/abs/2506.03141 (SIGGRAPH Asia 2025)
- 视频: https://www.youtube.com/watch?v=6Ye6wWupWD4
- 图片: https://context-as-memory.github.io/pics/framework.jpg
- 项目主页: https://context-as-memory.github.io/

#### WorldMem：带记忆的长期一致世界模拟（WorldMem） — Zeqi Xiao (2025-04-16)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 开源权重 / 代码
- 输入: 键盘与手柄动作, 图像 → 输出: 交互式帧流
- 核心想法: 持久性可以被工程化：把看到的内容连同位置和时间一起存下来，需要时去查，而不是指望模型自己记得。
- 内容: 一个带显式记忆库的世界模型：当 Minecraft 玩家回头看向先前建造或见过的地方时，模型会调取存储的画面及其位姿，一致地重新生成该处，包括随时间发生的变化。
- 实现方式: 存储带有相机位姿与时间戳的历史帧的记忆库，由视频扩散模型中的记忆注意力模块读取。
- 能力维度: 持久性
- 论文: https://arxiv.org/abs/2504.12369 (arXiv 2025)
- 视频: https://xizaoqu.github.io/worldmem/resources/cover.mp4
- 图片: https://xizaoqu.github.io/worldmem/resources/success_044.png
- 项目主页: https://xizaoqu.github.io/worldmem/
- 代码: https://github.com/xizaoqu/WorldMem

#### 扩散强制（Diffusion Forcing）（Diffusion Forcing） — Boyuan Chen (2024-07-01)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 键盘与手柄动作, 视频 → 输出: 平面视频
- 核心想法: 长时间、稳定的推演首先是训练问题，然后才是记忆问题；这一方法解决了很大一部分漂移。
- 内容: 一种训练方法：为每一帧分配各自的噪声水平，使视频模型能远超训练长度稳定地向前推演，并能被引导朝向目标；许多后来的实时世界模型都以它为基础。
- 实现方式: 序列扩散中每个 token 以独立采样的噪声水平去噪，把下一 token 预测与全序列扩散结合起来，并支持对未来 token 的引导。
- 能力维度: 持久性, 实验控制
- 论文: https://arxiv.org/abs/2407.01392 (NeurIPS 2024)
- 视频: https://www.youtube.com/watch?v=CNgwS8B7UvE
- 图片: https://boyuan.space/diffusion-forcing/static/images/teaser.png
- 项目主页: https://boyuan.space/diffusion-forcing/
- 代码: https://github.com/buoyancy99/diffusion-forcing

## 三维场景与世界生成

带有显式几何（高斯泼溅、网格、全景图）的生成环境：可以戴着头显走进去、编辑并保存。持久性由表示方式本身保证。

### 可探索的三维世界

由文字或图像生成可漫游的三维世界：Marble、Atlas、HunyuanWorld、WonderWorld、Lyra、Voyager……

#### Atlas — World Labs (2026-09-01)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 候补 / 抢先体验
- 输入: 图像, 镜头路径 / 位姿, 视频 → 输出: 平面视频, 高斯泼溅 / 辐射场, 图像 / 全景图
- 核心想法: 同一个模型既能想象也能重建：给它的现场照片越多，它编造的就越少，“真实与想象”的比例变成研究可以设定的一个旋钮。
- 内容: World Labs 的“全模态”世界模型，从零开始在文本、图像、视频和三维数据上预训练：给定一到几张参考图和手工设计的镜头路径，可生成最长一分钟的 1440p 视频；能用一张到一百多张照片重建真实地点，并输出点云或高斯泼溅。截至 2026 年 10 月仅开放抢先体验；World Labs 表示它将驱动未来版本的 Marble。
- 实现方式: 多模态自回归扩散 Transformer 把每张输入图像放在共享空间上下文中的三维位置上，再以像素级精确的相机几何为条件生成新画面与深度图；深度被融合成点云，并补全为三维高斯泼溅。
- 参数: up to 60 s video at 1440p · 1–6 reference images for generation · reconstruction from 1 to 100+ images · point cloud / 3DGS output
- 能力维度: 持久性, 实验控制, 感知真实感
- 视频: https://www.youtube.com/watch?v=hzvXRHBInx0
- 图片: https://www.worldlabs.ai/images/atlas-og.jpg
- 项目主页: https://www.worldlabs.ai/blog/atlas

#### Echo-2 — SpAItial (2026-04)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 产品 / 应用
- 输入: 图像, 文字提示 → 输出: 高斯泼溅 / 辐射场, 三维场景 / 世界
- 核心想法: 世界生成正在变成一次“工具调用”：智能体可以在对话中途请求、编辑并交付一个三维场所。
- 内容: SpAItial 的第二代世界模型，根据文字或图像生成可实时漫游、在任何设备浏览器中运行的三维场景；2026 年 6 月又推出 Claude 插件和托管 MCP 服务器，可在对话中生成与编辑世界。
- 实现方式: 每个提示词生成一个空间上持久的三维场景，而不是一串画面；SpAItial 称其在 WorldScore 基准上优于 Marble 1.1（公司自述，未经独立验证）。
- 能力维度: 持久性, 创作可及性
- 视频: https://www.youtube.com/watch?v=2CIoyGoGHZs
- 图片: https://spaitial.ai/og-image-default.png
- 项目主页: https://www.spaitial.ai/

#### 混元世界模型 2.0（HY-World 2.0）（HY-World 2.0） — 腾讯混元 (2026-04-16)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码, 产品 / 应用
- 输入: 文字提示, 图像, 视频 → 输出: 高斯泼溅 / 辐射场, 网格 / 三维资产, 三维场景 / 世界
- 核心想法: 腾讯明确把它与视频世界模型对照：把世界一次性建成资产、此后渲染几乎零成本，而不是为一个会消失的世界逐帧付费。
- 内容: 腾讯第二代开源世界模型：把文字或单张图像扩展为可漫游的三维高斯泼溅或网格世界，也能把多视角照片或视频重建为三维，输出可直接导入 Blender、Unity、虚幻引擎和 Isaac Sim。权重于 2026 年 4–5 月陆续开源，7 月发布 HY World 2.1 更新，可在腾讯的网页产品中使用。
- 实现方式: 共四个阶段：HY-Pano 2.0（约 800 亿参数）生成全景图，WorldNav 规划镜头轨迹，WorldStereo 2.0（约 170 亿参数）借助关键帧视图与几何记忆扩展世界，最后由能前馈预测深度、法线、相机、点云和 3DGS 的 WorldMirror 2.0 合成完整世界。
- 参数: HY-Pano 2.0 ~80B · WorldStereo 2.0 ~17B · 3DGS / mesh output
- 能力维度: 持久性, 实验控制, 创作可及性
- 论文: https://arxiv.org/abs/2604.14268 (Technical report 2026)
- 视频: https://github.com/user-attachments/assets/b56f4750-25c9-48fb-83ff-d58526711463
- 图片: https://raw.githubusercontent.com/Tencent-Hunyuan/HY-World-2.0/main/assets/teaser.png
- 项目主页: https://github.com/Tencent-Hunyuan/HY-World-2.0
- 代码: https://github.com/Tencent-Hunyuan/HY-World-2.0

#### Lyra 2.0 — 英伟达 (2026-04-15)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像, 镜头路径 / 位姿 → 输出: 高斯泼溅 / 辐射场, 网格 / 三维资产, 平面视频
- 核心想法: 它针对长距离生成漫游的两大问题——走出上下文后忘掉去过的地方、外观逐渐漂移——而这两点恰恰也是破坏参与者“稳定场所感”的原因。
- 内容: NVIDIA 面向大场景的开源 Lyra 后继版本：生成可以回头、重访已到过地点的长距离镜头漫游视频，并把它提升为可导出为泼溅或网格的持久三维世界，例如用作 Isaac Sim 中的机器人训练场景。2026 年 7 月发布了图形界面与训练代码。
- 实现方式: 保留逐帧三维几何，只用于检索相关的历史帧并与目标视角建立稠密对应（应对空间遗忘）；用模型自身退化输出构成的“自增强历史”训练视频模型（应对漂移）；再用得到的长轨迹微调前馈式重建，输出三维高斯与网格。
- 参数: long-horizon walkthroughs with revisits · 3DGS and mesh export
- 能力维度: 持久性, 情境可达性
- 论文: https://arxiv.org/abs/2604.13036 (SIGGRAPH Asia 2026 (accepted))
- 视频: https://nv-tlabs.github.io/Project-Lyra/assets/teaser.mp4
- 图片: https://nv-tlabs.github.io/Project-Lyra/assets/method_v2.png
- 项目主页: https://nv-tlabs.github.io/Project-Lyra/
- 代码: https://github.com/nv-tlabs/lyra

#### Echo — SpAItial (2025-12)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 候补 / 抢先体验
- 输入: 图像, 文字提示 → 输出: 高斯泼溅 / 辐射场, 三维场景 / 世界
- 核心想法: 又一家来自慕尼黑三维视觉圈的公司开始提供持久的泼溅世界，研究者不必绑定单一厂商的格式。
- 内容: SpAItial 的第一个世界模型：把一张图像或一句简短文字变成具有真实尺度的三维高斯泼溅环境，可在网页浏览器中实时自由探索。
- 实现方式: SpAItial 称其先推断出统一的、具有真实尺度的几何与外观场景表示，每一帧画面和深度图都由它渲染，再用三维高斯泼溅显示；架构未公开。
- 能力维度: 持久性, 感知真实感
- 视频: https://www.youtube.com/watch?v=mlkRiJfuARw
- 项目主页: https://www.spaitial.ai/

#### Marble — World Labs (2025-11-12)
- 类型: 产品 / 应用 · 时序: 预先生成 · 获取方式: 产品 / 应用, 公开 API
- 输入: 文字提示, 图像, 视频 → 输出: 高斯泼溅 / 辐射场, 网格 / 三维资产, 三维场景 / 世界
- 核心想法: 研究者可以用一句提示词或几张照片搭出整个场景，之后为每位参与者保存、版本化并重新加载完全相同的世界。
- 内容: World Labs 的世界生成产品：文字、一张或多张照片、一段视频或粗略的三维布局，都能变成持久的三维世界，可以编辑、扩展、与其他世界拼接，并导出为高斯泼溅、网格或视频。2025 年 9 月 16 日开放测试，11 月 12 日全面上线；2026 年推出 Marble 1.1 与可生成更大世界的 1.1 Plus，并于 2026 年 1 月 21 日通过 World API 向开发者开放。
- 实现方式: 专有的多模态世界模型根据输入生成三维高斯泼溅世界（可另行提取网格）；布局编辑器 Chisel 把粗略的三维结构与视觉风格分开控制；世界通过 World Labs 开源的 Spark 渲染器在网页、手机和 VR 中显示。
- 参数: text / image / multi-image / video / 3D layout in · Gaussian splats, mesh or video out · Marble 1.1 Plus for larger worlds
- 能力维度: 创作可及性, 持久性, 感知真实感
- 视频: https://www.youtube.com/watch?v=UslQB4LUueI
- 图片: https://www.worldlabs.ai/images/nov12-thumbnail.jpg
- 项目主页: https://www.worldlabs.ai/blog/marble-world-model
- API 文档: https://docs.worldlabs.ai/api

#### FlashWorld — Xinyang Li, 腾讯混元 (2025-10-16)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 文字提示, 图像 → 输出: 高斯泼溅 / 辐射场, 三维场景 / 世界
- 核心想法: 当生成一个世界只需几秒而不是几分钟，就可以在两次试验之间重新生成场景，或为研究批量采样。
- 内容: 开源模型：在单张 GPU 上约 5–10 秒即可由一张图像或一句文字生成三维高斯泼溅场景，并提供网页演示查看结果。
- 实现方式: 基于视频扩散先验的多视角扩散模型先在“多视角图像”和“直接输出三维高斯”两种模式下预训练，再通过跨模式蒸馏，让快速的三维输出模式达到多视角模式的画质。
- 参数: 5–10 s per scene on one GPU · authors report 10–100× faster than prior work
- 能力维度: 时间响应性, 情境多样性, 创作可及性
- 论文: https://arxiv.org/abs/2510.13678 (ICLR 2026 (oral))
- 视频: https://www.youtube.com/watch?v=nUIiCj8J6B4
- 图片: https://imlixinyang.github.io/FlashWorld-Project-Page/static/images/teaser.png
- 项目主页: https://imlixinyang.github.io/FlashWorld-Project-Page/
- 代码: https://github.com/imlixinyang/FlashWorld

#### Lyra — 英伟达 (2025-09-23)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 文字提示, 图像, 视频 → 输出: 高斯泼溅 / 辐射场, 动态三维 / 4D
- 核心想法: 视频模型内部已有的三维知识可以直接读出为场景，完全不需要多视角训练数据。
- 内容: NVIDIA 的开源模型：一次前向推理就能把单张图像（或用于动态场景的一段视频）变成显式的三维高斯泼溅场景，可直接实时渲染或放进 Isaac Sim 等仿真环境。
- 实现方式: 自蒸馏：在可控镜头的视频扩散模型（基于 Cosmos 的 GEN3C）的 RGB 解码器旁增加一个 3DGS 解码器，只用模型自己合成的数据训练，使其渲染结果与解码视频一致。
- 参数: single image → 3DGS · video → dynamic 3DGS · feed-forward
- 能力维度: 持久性, 情境可达性
- 论文: https://arxiv.org/abs/2509.19296 (ICLR 2026)
- 视频: https://research.nvidia.com/labs/toronto-ai/lyra/assets/videos/teaser/teaser.mp4
- 图片: https://research.nvidia.com/labs/toronto-ai/lyra/assets/images/isaac/apartment_1.png
- 项目主页: https://research.nvidia.com/labs/toronto-ai/lyra/
- 代码: https://github.com/nv-tlabs/lyra

#### 混元世界模型 Voyager（HunyuanWorld-Voyager） — 腾讯混元 (2025-09-02)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像, 镜头路径 / 位姿 → 输出: 平面视频, 三维场景 / 世界
- 核心想法: 每一帧都同时生成深度，意味着世界边走边建，而不必事后再用运动恢复结构去还原。
- 内容: 开源视频扩散模型：给定一张图像和用户绘制的镜头路径，同时生成对齐的 RGB 与深度视频，因此每一步“行走”同时也是一份可直接重建为场景的三维点云。
- 实现方式: 世界一致的视频扩散模型以先前点云构成的世界缓存（带点剔除）为条件，联合去噪 RGB 与深度，并通过自回归与平滑采样延伸到长距离探索；训练数据来自可扩展的数据引擎，包含估计了相机与深度的真实视频和虚幻引擎视频。
- 参数: RGB-D video along a user camera path · direct point-cloud reconstruction
- 能力维度: 持久性, 实验控制
- 论文: https://arxiv.org/abs/2506.04225 (ACM TOG (SIGGRAPH Asia 2025))
- 视频: https://github.com/user-attachments/assets/2eb844c9-30ba-4770-8066-189c123affee
- 图片: https://raw.githubusercontent.com/Tencent-Hunyuan/HunyuanWorld-Voyager/main/assets/teaser.png
- 项目主页: https://github.com/Tencent-Hunyuan/HunyuanWorld-Voyager
- 代码: https://github.com/Tencent-Hunyuan/HunyuanWorld-Voyager

#### Matrix-3D — 昆仑万维 Skywork (2025-08-12)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 文字提示, 图像, 镜头路径 / 位姿 → 输出: 360° / 立体视频, 高斯泼溅 / 辐射场, 三维场景 / 世界
- 核心想法: 生成全景视频而不是正前方视频，消除了观看者身后的空白，让世界不再像单面布景。
- 内容: 开源框架：把文字或图像变成全方位可探索的三维世界——先沿选定轨迹生成 360° 全景视频，再把视频重建为三维高斯泼溅场景。
- 实现方式: 以场景网格渲染为条件、受轨迹引导的全景视频扩散模型生成行走画面，再由前馈式大型全景重建模型或优化流程提升为三维；训练使用合成数据集 Matrix-Pano。
- 参数: 360° panoramic video → 3DGS · 5B low-VRAM mode (12 GB)
- 能力维度: 持久性, 情境可达性
- 论文: https://arxiv.org/abs/2508.08086 (Technical report 2025)
- 视频: https://www.youtube.com/watch?v=cOmIVyade-c
- 图片: https://matrix-3d.github.io/static/images/fig2.png
- 项目主页: https://matrix-3d.github.io/
- 代码: https://github.com/SkyworkAI/Matrix-3D

#### 混元3D世界模型 1.0（HunyuanWorld 1.0） — 腾讯混元 (2025-07-26)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码, 产品 / 应用
- 输入: 文字提示, 图像 → 输出: 网格 / 三维资产, 图像 / 全景图, 三维场景 / 世界
- 核心想法: 先生成全景的路线一次给出完整的 360° 环绕，并以普通 CG 流程能直接打开的网格形式输出，代价是可行走范围有限。
- 内容: 腾讯开源权重的世界生成模型：先把文字或图像变成 360° 全景图，再分解成分层的三维网格（天空、背景、可分离的物体），可在浏览器、头显或游戏引擎中探索。2025 年 8 月推出的量化 lite 版可在 RTX 4090 等消费级显卡上运行。
- 实现方式: 全景扩散模型（PanoDiT）先生成 360° 的世界代理图，再按语义分层，借助深度估计与补全提升为三维，最终导出为物体可分离的分层网格。
- 参数: 360° panorama proxy · layered mesh export · lite version on consumer GPUs
- 能力维度: 持久性, 创作可及性, 情境多样性
- 论文: https://arxiv.org/abs/2507.21809 (Technical report 2025)
- 视频: https://github.com/user-attachments/assets/747b3e41-df9c-4cd2-b1d1-c0dce63f63ef
- 图片: https://raw.githubusercontent.com/Tencent-Hunyuan/HunyuanWorld-1.0/main/assets/teaser.png
- 项目主页: https://3d-models.hunyuan.tencent.com/world/
- 代码: https://github.com/Tencent-Hunyuan/HunyuanWorld-1.0

#### 大世界模型演示（Generating Worlds）（Large World Model demo (Generating Worlds)） — World Labs (2024-12-02)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 图像 → 输出: 三维场景 / 世界, 高斯泼溅 / 辐射场
- 核心想法: 生成的世界第一次成为可以反复回到的“地方”，而不是播完即止的片段；不过这批早期世界范围较小、边界有限。
- 内容: World Labs 的首次公开成果：把一张图像变成可以在浏览器中实时探索的三维场景，并可交互地加入景深、滑动变焦等镜头效果。
- 实现方式: 一个未公开细节的生成模型把单张图像提升为显式三维表示，在浏览器端实时渲染；World Labs 称之为迈向“大世界模型”的第一步。
- 参数: single image in · real-time browser rendering
- 能力维度: 持久性, 感知真实感
- 视频: https://wlt-ai-cdn.art/videos/banner_video.mp4
- 图片: https://www.worldlabs.ai/images/generating-worlds-nologo.jpg
- 项目主页: https://www.worldlabs.ai/blog/generating-worlds

#### WonderWorld — Hong-Xing (Koven) Yu (2024-06-13)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 开源权重 / 代码
- 输入: 图像, 文字提示, 镜头路径 / 位姿 → 输出: 高斯泼溅 / 辐射场, 三维场景 / 世界
- 核心想法: 生成快到能及时回应用户的请求，参与者就成了这个世界的共同作者。
- 内容: 从一张图像开始，用户移动镜头并输入那里应该出现什么；WonderWorld 在十秒内生成相连的新三维场景，让世界一块一块地被交互式搭建出来。
- 实现方式: 快速分层高斯面元（FLAGS）直接由前景、背景和天空三层的估计几何初始化，避免缓慢的逐场景优化，并用引导式深度扩散让新场景在几何上与旧场景衔接。
- 参数: < 10 s per new scene on one A6000 GPU (authors)
- 能力维度: 时间响应性, 共创与能动性, 创作可及性
- 论文: https://arxiv.org/abs/2406.09394 (CVPR 2025)
- 视频: https://kovenyu.com/wonderworld/interactive_converted_60fps_trimmed_cropped/cathedral_2_interactive_compressed_60fps_trimmed_cropped.mp4
- 图片: https://kovenyu.com/wonderworld/complete/venice.jpg
- 项目主页: https://kovenyu.com/wonderworld/
- 代码: https://github.com/KovenYu/WonderWorld

#### WonderJourney — Hong-Xing (Koven) Yu (2023-12-06)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 文字提示, 图像 → 输出: 三维场景 / 世界, 平面视频
- 核心想法: 让语言模型来写“接下来是什么”，场景生成就变成了无尽的旅行；不过每一步都只是一小块依赖视角的三维片段。
- 内容: WonderJourney 从任意一张图像或一段文字出发，生成一长串彼此相连的三维场景，例如从一幅画飞入群山或诗中的风景，并渲染成一段连续的镜头旅程。
- 实现方式: 语言模型提出下一个场景的描述，文生图模型配合深度估计构建点云场景，再由视觉语言模型检查结果，镜头才继续前进。
- 能力维度: 情境多样性, 情境可达性
- 论文: https://arxiv.org/abs/2312.03884 (CVPR 2024)
- 视频: https://www.youtube.com/watch?v=2X8TU3KwZ-c
- 项目主页: https://kovenyu.com/wonderjourney/
- 代码: https://github.com/KovenYu/WonderJourney

#### LucidDreamer — Jaeyoung Chung (2023-11-22)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 文字提示, 图像 → 输出: 高斯泼溅 / 辐射场, 三维场景 / 世界
- 核心想法: 图像补全加深度估计就足以从一句提示词“长出”连贯的泼溅场景，后来许多世界生成器都在完善这套做法。
- 内容: 根据一句文字或一张图像生成整片三维高斯泼溅场景（而不只是一个物体），风格不限：方法是反复想象新视角，再把它们拼进同一个点云。
- 实现方式: “做梦”阶段交替进行：用 Stable Diffusion 补全移动后的视角，再用单目深度把它提升进共享点云；“对齐”阶段合并点云，并以此初始化三维高斯泼溅的优化。
- 能力维度: 情境多样性, 感知真实感
- 获奖与认可: IEEE TVCG 2025 Best Paper Runner-Up
- 论文: https://arxiv.org/abs/2311.13384 (IEEE TVCG 2025)
- 视频: https://github.com/user-attachments/assets/35004aaa-dffc-4133-b15a-05224e68b91e
- 项目主页: https://luciddreamer-cvlab.github.io/
- 代码: https://github.com/luciddreamer-cvlab/LucidDreamer

#### CityDreamer — Haozhe Xie (2023-09-01)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 镜头路径 / 位姿 → 输出: 三维场景 / 世界, 平面视频
- 核心想法: 人群、交通、迷路这类情境都发生在城市尺度；CityDreamer 表明在这个尺度上可以把生成的布局与外观分开控制。
- 内容: 生成无边界的三维城市——街道布局、建筑与背景——可以用连贯的镜头飞越其中，训练数据为 Google Earth 影像与 OpenStreetMap 布局。
- 实现方式: 无边界布局生成器先输出语义图与高度图；再由分别负责建筑（逐实例）和背景的神经场生成器渲染，并以紧凑的鸟瞰图场景表示组合起来。
- 能力维度: 情境可达性, 情境多样性
- 论文: https://arxiv.org/abs/2309.00610 (CVPR 2024)
- 视频: https://www.youtube.com/watch?v=te4zinLTYz0
- 图片: https://www.infinitescript.com/projects/CityDreamer/CityDreamer-Thumbnail.webp
- 项目主页: https://www.infinitescript.com/project/city-dreamer/
- 代码: https://github.com/hzxie/CityDreamer

#### Text2Room：用文生图模型生成带纹理的房间网格（Text2Room） — Lukas Höllein (2023-03-21)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 文字提示 → 输出: 网格 / 三维资产, 三维场景 / 世界
- 核心想法: 它是早期的证明：二维图像模型加上深度估计，就能布置出一个可以走进去的完整房间。
- 内容: Text2Room 根据一句文字搭建出完整的、带纹理的三维房间网格，可以在其中走动：方法是用图像模型逐个视角“画”出整个房间。
- 实现方式: 沿选定的镜头轨迹进行以文字为条件的迭代补全，结合单目深度估计与深度对齐，把每个新视角融合进同一个网格；第二轮再从更多视角补洞。
- 能力维度: 创作可及性, 持久性
- 论文: https://arxiv.org/abs/2303.11989 (ICCV 2023 (oral))
- 视频: https://www.youtube.com/watch?v=fjRnFL91EZc
- 图片: https://lukashoel.github.io/text-to-room/static/images/teaser-min.jpg
- 项目主页: https://lukashoel.github.io/text-to-room/
- 代码: https://github.com/lukasHoel/text2room

#### Infinite Nature：从单张图像无限生成自然风景（Infinite Nature） — Andrew Liu, 谷歌 (2020)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像, 镜头路径 / 位姿 → 输出: 平面视频, 图像 / 全景图
- 核心想法: 可探索世界这一脉的源头：它展示了从一张图像生成无尽的新地形，也暴露了没有持久三维记忆时世界会如何崩坏。
- 内容: Infinite Nature 从一张风景照片出发，生成任意长度的“无人机飞入画面”视频，镜头前进时不断创造新的海岸线与山峦。
- 实现方式: “渲染—修补—重复”：把当前画面及其视差变换到下一个相机位姿，再由网络补全和修饰，训练数据为航拍自然视频。
- 能力维度: 情境多样性, 情境可达性
- 论文: https://arxiv.org/abs/2012.09855 (ICCV 2021 (oral))
- 视频: https://www.youtube.com/watch?v=oXUf6anNAtc
- 图片: https://infinite-nature.github.io/teaser.png
- 项目主页: https://infinite-nature.github.io/
- 代码: https://github.com/google-research/google-research/tree/master/infinite_nature

### 360° 全景与天空盒

用于 VR 的等距柱状全景与天空盒，常是生成场景的第一层。

#### LayerPano3D — Shuai Yang (2024-08-23)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 文字提示 → 输出: 高斯泼溅 / 辐射场, 图像 / 全景图
- 核心想法: 把全景图分层，是增加视差与去遮挡效果的低成本办法，而这正是 360° 图像在头显中“像一个地方”的关键。
- 内容: 根据文字生成 360° 全景图，并按深度拆成多个图层再转成三维高斯，观看者可以走动一小段距离，看到被物体遮挡的内容显现出来。
- 实现方式: 先合成文字引导的锚点视图并拼成高分辨率全景图，再按深度分解为多层全景并补全被遮挡内容，每一层都优化为三维高斯。
- 能力维度: 感知真实感, 持久性
- 论文: https://arxiv.org/abs/2408.13252 (SIGGRAPH 2025)
- 视频: https://www.youtube.com/watch?v=lpNs5JwaJoA
- 项目主页: https://ys-imtech.github.io/projects/LayerPano3D/
- 代码: https://github.com/YS-IMTech/LayerPano3D

#### DreamScene360 — Shijie Zhou (2024-04-10)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 文字提示 → 输出: 高斯泼溅 / 辐射场, 图像 / 全景图
- 核心想法: 全景图是 VR 场景方便的第一层：在构建任何三维内容之前就先确定了整个环绕环境。
- 内容: 把一句文字变成完整的 360° 三维场景：先生成全景图，再提升为高斯泼溅，可以从任意方向观看，并允许小范围移动。
- 实现方式: 先用 GPT-4V 自我修正循环优化提示词，再用二维扩散模型生成全景图，以单目深度初始化全景三维高斯，并在合成的虚拟视角上施加语义与几何正则以补全未见区域。
- 能力维度: 创作可及性, 持久性
- 论文: https://arxiv.org/abs/2404.06903 (ECCV 2024)
- 视频: https://www.youtube.com/watch?v=6rMIQfe7b24
- 图片: https://raw.githubusercontent.com/ShijieZhou-UCLA/DreamScene360/main/assets/teaser_v6.png
- 项目主页: https://dreamscene360.github.io/
- 代码: https://github.com/ShijieZhou-UCLA/DreamScene360

#### Skybox AI — Blockade Labs (2023)
- 类型: 产品 / 应用 · 时序: 预先生成 · 获取方式: 产品 / 应用, 公开 API
- 输入: 文字提示, 草图与手势, 图像 → 输出: 图像 / 全景图
- 核心想法: 这是让参与者置身于生成环境中最快的办法，但天空盒始终只是背景：其中的任何东西都无法触及或移动。
- 内容: 网页工具与 API：根据提示词或粗略草图生成 360° 等距柱状天空盒，提供风格包、对已有 360° 照片的重混、HDRI 光照导出，以及基于深度的“世界网格”导出，可用于游戏引擎和 VR。
- 实现方式: 专为无缝等距柱状输出训练的专有扩散模型（Model 3 及之后版本）；通过深度估计把全景图变成一个简单的包围网格。
- 能力维度: 创作可及性, 情境多样性
- 视频: https://www.youtube.com/watch?v=eKO49j-ibaA
- 图片: https://static.wixstatic.com/media/8d6639_b2ee76a88e224659804c1ef09c7bc5da~mv2.jpg
- 项目主页: https://www.blockadelabs.com/
- API 文档: https://api-documentation.blockadelabs.com/api/

#### MVDiffusion — Shitao Tang (2023-07-03)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 文字提示, 图像 → 输出: 图像 / 全景图
- 核心想法: 把全景图视为多个必须彼此一致的视角，而不是一张宽幅图像，从而消除了接缝和首尾相接处的漂移。
- 内容: 通过一次性生成八张相互重叠且彼此一致的透视视图，根据文字合成无缝的 360° 全景图；同样的思路也能一致地为扫描的房间网格上色。
- 实现方式: 在预训练的 Stable Diffusion 中插入对应关系感知的注意力层，使各视图中像素对应的位置共享特征，所有视图并行去噪。
- 能力维度: 感知真实感, 持久性
- 论文: https://arxiv.org/abs/2307.01097 (NeurIPS 2023 (spotlight))
- 视频: https://mvdiffusion.github.io/pics/panorama/1_h264.mp4
- 图片: https://mvdiffusion.github.io/assets/images/teaser_v2.gif
- 项目主页: https://mvdiffusion.github.io/
- 代码: https://github.com/Tangshitao/MVDiffusion

#### Text2Light — Zhaoxi Chen (2022)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 文字提示 → 输出: 图像 / 全景图
- 核心想法: 生成的环境还能为场景提供光照，让虚拟人物和物体看起来真的身处其中。
- 内容: 根据文字描述生成高分辨率的 HDR 360° 全景图，既可作为沉浸式背景，也可作为三维场景渲染时基于物理的光照。
- 实现方式: 零样本两阶段流程：先借助 CLIP 引导与分层码本生成文字驱动的低分辨率 LDR 全景图，再由结构感知的超分辨率网络放大并提升为 HDR。
- 能力维度: 感知真实感, 创作可及性
- 论文: https://arxiv.org/abs/2209.09898 (ACM TOG (SIGGRAPH Asia 2022))
- 视频: https://www.youtube.com/watch?v=XDx6tOHigPE
- 图片: https://frozenburning.github.io/projects/text2light/img/teaser.jpg
- 项目主页: https://frozenburning.github.io/projects/text2light/
- 代码: https://github.com/FrozenBurning/Text2Light

### 布局、程序化与代码生成场景

由语言模型、程序化规则或代码拼装的场景：Holodeck、Infinigen、场景图。

#### WorldClaw：智能体驱动的大规模开放世界生成（WorldClaw） — 腾讯混元 (2026-08-07)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 文字提示 → 输出: 网格 / 三维资产, 三维场景 / 世界
- 核心想法: 会规划、会搭建、还会检查渲染结果的智能体，可以把生成规模从一个房间扩展到一片地景，同时让每个物体都保持可编辑。
- 内容: 腾讯混元的智能体系统：把一句开放式提示词变成大尺度、可探索的开放世界三维场景，包含地形、分区和可编辑的实例级资产。
- 实现方式: 规划智能体先写出结构化规格（分区、地形、资产、材质、空间关系）；由分区感知的高度场和语义布局构成地形，细节区域以地形为条件生成组合并重建为带纹理的网格，最后由基于渲染的智能体修正地形、物体与接触关系。
- 能力维度: 情境可达性, 创作可及性, 实验控制
- 论文: https://arxiv.org/abs/2608.05248 (arXiv 2026)
- 视频: https://tencent-hunyuan.github.io/Hunyuan3D-WorldClaw/media/worldclaw-teaser.mp4
- 图片: https://tencent-hunyuan.github.io/Hunyuan3D-WorldClaw/assets/worldclaw-share.jpg
- 项目主页: https://tencent-hunyuan.github.io/Hunyuan3D-WorldClaw/
- 代码: https://github.com/Tencent-Hunyuan/Hunyuan3D-WorldClaw

#### SAGE — 英伟达 (2026-02-10)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 文字提示 → 输出: 三维场景 / 世界, 网格 / 三维资产
- 核心想法: 根据任务描述生成情境、再用评审器检查，这正是研究中既要变化多样又要保证有效的情境所需要的循环。
- 内容: 给定“拿起碗放到桌上”这样的具身任务，SAGE 的智能体会为之生成一个物理上有效、可直接仿真的房间，并不断修正直到通过自身的检查；NVIDIA 公开了代码和 SAGE-10k 场景数据集。
- 实现方式: 语言模型智能体把布局生成器、物体组合生成器（包括 TRELLIS 资产）与语义合理性、视觉真实感和物理稳定性评审器结合起来，反复迭代，直到场景符合意图并能在 Isaac Sim 中稳定加载。
- 参数: SAGE-10k dataset · Isaac Sim / Isaac Lab
- 能力维度: 情境可达性, 情境多样性, 行为似真性
- 论文: https://arxiv.org/abs/2602.10116 (arXiv 2026)
- 视频: https://research.nvidia.com/labs/cosmos-lab/sage/assets/video-sage.mp4
- 图片: https://research.nvidia.com/labs/cosmos-lab/sage/assets/images/teaser.png
- 项目主页: https://research.nvidia.com/labs/cosmos-lab/sage/
- 代码: https://github.com/NVlabs/sage

#### WorldGen — Meta (2025-11-20)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 文字提示 → 输出: 网格 / 三维资产, 三维场景 / 世界
- 核心想法: 可行走性优先：先规划布局和导航网格，再决定外观，所以这个世界首先是一个“关卡”，而不只是一幅画面。
- 内容: Meta Reality Labs 的研究系统：把一句文字变成可行走、完整贴图的三维世界（报道称最大约 50 × 50 米），自带导航网格，可直接在 Unity 或虚幻引擎中探索或编辑。截至 2026 年 10 月仍仅限研究。
- 实现方式: 由语言模型推理布局并程序化生成白盒，得到考虑导航网格的场景规划；再生成参考图像，经图生三维重建出场景，最后进行按物体的分解、增强与贴图。
- 参数: scenes up to ~50 × 50 m (reported) · navmesh · Unity / Unreal export
- 能力维度: 创作可及性, 情境可达性, 持久性
- 论文: https://arxiv.org/abs/2511.16825 (CVPR 2026)
- 视频: https://www.youtube.com/watch?v=mzuyLODsUTM
- 图片: https://arxiv.org/html/2511.16825v1/x1.png
- 项目主页: https://www.meta.com/blog/worldgen-3d-world-generation-reality-labs-generative-ai-research/

#### BlenderMCP — Siddharth Ahuja (2025-03)
- 类型: 开源工具 · 时序: 回合制 · 获取方式: 开源权重 / 代码
- 输入: 文字提示, 图像 → 输出: 三维场景 / 世界, 网格 / 三维资产
- 核心想法: 在专业工具中通过对话搭建场景：语言模型写代码，人保留文件。
- 内容: 开源插件与 Model Context Protocol 服务器，让 Claude 等语言模型可以查看并编辑正在运行的 Blender 场景：创建和摆放物体、应用材质、调用 Poly Haven 资产以及三维生成服务。
- 实现方式: Blender 插件开启一个套接字服务；MCP 服务器把场景查看、物体创建、Python 执行、资产搜索等功能暴露为工具，由语言模型逐轮调用。
- 能力维度: 创作可及性, 共创与能动性
- 视频: https://www.youtube.com/watch?v=DqgKuLYUv00
- 项目主页: https://github.com/ahujasid/blender-mcp
- 代码: https://github.com/ahujasid/blender-mcp

#### Holodeck — Yue Yang, Allen Institute for AI (Ai2) (2023-12-14)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 文字提示 → 输出: 三维场景 / 世界, 网格 / 三维资产
- 核心想法: 语言模型把场景写成约束，因此每个生成的房间都是一份可检查的规格说明，可以记录、变化和重建。
- 内容: 输入“一位养猫研究者的一室一厅公寓”这样的提示，Holodeck 就会在 AI2-THOR 中搭建完整的、可交互的多房间环境，包括平面图、材质、门窗和摆放好的家具，具身智能体可以在其中导航。
- 实现方式: GPT-4 提出平面图、材质和带空间关系约束的物体清单；从 Objaverse 检索资产，再由约束求解器优化布局，最后载入 AI2-THOR 模拟器。
- 能力维度: 创作可及性, 情境多样性, 实验控制
- 论文: https://arxiv.org/abs/2312.09067 (CVPR 2024)
- 视频: https://www.youtube.com/watch?v=Pk5BcEqqPoU
- 图片: https://yueyang1996.github.io/holodeck/static/images/floorplan_customizability.jpg
- 项目主页: https://yueyang1996.github.io/holodeck/
- 代码: https://github.com/allenai/Holodeck

#### Infinigen — Alexander Raistrick, Princeton Vision & Learning Lab (2023-06-15)
- 类型: 开源工具 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 场景规格、代码与规则 → 输出: 三维场景 / 世界, 网格 / 三维资产
- 核心想法: 程序化生成能给出学习式生成器做不到的东西：场景的每个参数都已知、可设种子、可复现。
- 内容: 开源的程序化生成器，完全在 Blender 中用代码创造无限多的照片级自然世界——地形、植物、动物和天气，并附带深度、分割和几何的精确真值。Infinigen Indoors（CVPR 2024）把它扩展到布置好的室内房间，随后又加入可铰接、可用于仿真的资产（2025）和 ProcFunc 抽象（2026）。
- 实现方式: 从几何到材质，每个资产都由随机化的数学规则生成（不依赖外部资产），再通过基于约束的摆放组成场景，并用 Blender 路径追踪渲染。
- 参数: fully procedural · no external assets · ground-truth depth, normals, segmentation
- 能力维度: 情境多样性, 实验控制, 感知真实感
- 论文: https://arxiv.org/abs/2306.09310 (CVPR 2023)
- 视频: https://www.youtube.com/watch?v=6tgspeI-GHY
- 图片: https://infinigen.org/img/social_card.png
- 项目主页: https://infinigen.org/
- 代码: https://github.com/princeton-vl/infinigen

#### LayoutGPT — Weixi Feng (2023-05-24)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 文字提示 → 输出: 三维场景 / 世界
- 核心想法: 以文字写成的布局是生成场景中最可控的一层：在渲染之前就能阅读、编辑和比对。
- 内容: 表明只懂文字的语言模型，在类似 CSS 的示例提示下，就能写出带数值的布局：为图像给出包围框，为三维室内房间给出物体的位置与尺寸。
- 实现方式: 用检索到的示例，以类似 CSS 的格式进行上下文学习，让 GPT-3.5/4 输出布局，再用于驱动布局到图像的模型，或在 3D-FRONT 房间中摆放家具。
- 能力维度: 实验控制, 创作可及性
- 论文: https://arxiv.org/abs/2305.15393 (NeurIPS 2023)
- 视频: https://layoutgpt.github.io/static/videos/merged_scenes.mp4
- 图片: https://layoutgpt.github.io/static/images/3d_qualitative.png
- 项目主页: https://layoutgpt.github.io/
- 代码: https://github.com/weixi-feng/LayoutGPT

### 从照片到空间场景

把一张照片变成有深度与视差的三维场景：空间场景、单目深度、单图高斯泼溅。

#### Hyper3D WorldGen — 影眸科技 (2026-09-09)
- 类型: 产品 / 应用 · 时序: 预先生成 · 获取方式: 产品 / 应用
- 输入: 图像 → 输出: 网格 / 三维资产, 高斯泼溅 / 辐射场, 三维场景 / 世界
- 核心想法: 物体自带物理属性，一张房间照片因此能变成可交互的场景，而不是一块背景板。
- 内容: Hyper3D 的场景生成产品：把一张照片变成由独立、可编辑物体组成的三维场景——物体由 Rodin 生成网格，并估计碰撞几何、质量和摩擦——背景则用高斯泼溅呈现，面向机器人仿真、影视、游戏和空间计算。
- 实现方式: 在 CAST 的基础上，自动检测物体或由用户框选，补全三维形状，借助接触、支撑与悬挂的关系图估计位姿、尺度与物理属性并完成摆放，背景则重建为三维高斯泼溅。
- 能力维度: 行为似真性, 创作可及性, 持久性
- 视频: https://www.youtube.com/watch?v=-rhncMVVtGM
- 图片: https://storage.deemos.dev/features/worldgen/introBg.webp
- 项目主页: https://hyper3d.ai/features/worldgen

#### SHARP — 苹果 (2025-12-11)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像 → 输出: 高斯泼溅 / 辐射场
- 核心想法: 一秒之内从一张照片得到带真实尺度的泼溅，让“走进这张照片”便宜到可以对每张刺激图都这样做，不过只适用于小幅度的头部移动。
- 内容: Apple 的开源模型：在普通 GPU 上不到一秒就把一张照片转换成具有真实尺度的三维高斯表示，随后可实时渲染出照片级的邻近视角。
- 实现方式: 单个前馈网络从一张图像直接回归具有绝对尺度的三维高斯参数；作者报告其 LPIPS 比此前最佳模型低 25–34%，DISTS 低 21–43%，合成时间缩短三个数量级。
- 参数: < 1 s per image on a standard GPU · metric-scale 3DGS · real-time rendering
- 能力维度: 时间响应性, 感知真实感
- 论文: https://arxiv.org/abs/2512.10685 (ICLR 2026)
- 视频: https://www.youtube.com/watch?v=pSQSsXqQlcY
- 图片: https://apple-aiml-research.github.io/ml-sharp/teaser.jpg
- 项目主页: https://apple-aiml-research.github.io/ml-sharp/
- 代码: https://github.com/apple/ml-sharp

#### 空间场景（visionOS 26）（Spatial Scenes (visionOS 26)） — 苹果 (2025-06-09)
- 类型: 产品 / 应用 · 时序: 预先生成 · 获取方式: 产品 / 应用, 公开 API
- 输入: 图像 → 输出: 三维场景 / 世界, 图像 / 全景图
- 核心想法: 照片转三维已成为头显系统的默认功能，个人照片因此成为沉浸式研究中现成的、熟悉的真实场所来源。
- 内容: visionOS 26 的功能：把任意二维照片变成带深度、可从多个角度观看的空间场景，在 Apple Vision Pro 上可以凑近、环顾（iOS 26 锁定屏幕上则呈现为视差效果）；开发者可使用 Spatial Scene API；visionOS 27（2026 年 6 月）把它扩展到全景照片，并可设为个人“环境”。
- 实现方式: Apple 称其使用“新的生成式 AI 算法与计算深度”推断几何并补全去遮挡区域，以生成多个视角；模型未公开（Apple 的 SHARP 研究针对的是同一任务）。
- 能力维度: 感知真实感, 创作可及性
- 视频: https://www.apple.com/newsroom/videos/2025/autoplay/06/visionos-26-introduces-powerful-new-spatial-experiences-for-apple-vision-pro/apple-wwdc25-visionos-26-spatial-scenes-photos-app/large_2x.mp4
- 图片: https://www.apple.com/newsroom/images/2025/06/visionos-26-introduces-powerful-new-spatial-experiences-for-apple-vision-pro/tile/Apple-WWDC25-visionOS-26-hero-250609-lp.jpg.og.jpg
- 项目主页: https://www.apple.com/newsroom/2025/06/visionos-26-introduces-powerful-new-spatial-experiences-for-apple-vision-pro/

#### Bolt3D — Stanislaw Szymanowicz, 谷歌 (2025-03-18)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 图像, 多视角拍摄 / 扫描 → 输出: 高斯泼溅 / 辐射场, 三维场景 / 世界
- 核心想法: 直接采样三维表示，而不是先生成图像再重建，才让场景生成缩短到几秒。
- 内容: 从一张或几张图像出发，在单张 GPU 上不到七秒就生成三维高斯泼溅场景，无需逐场景优化。
- 实现方式: 基于二维扩散架构的潜空间扩散模型，直接输出类似 Splatter Image 的三维高斯与几何；训练数据是一个预先做过稠密重建的大规模多视角数据集。
- 参数: < 7 s per scene on one GPU · up to 300× lower inference cost than optimisation-based methods (authors)
- 能力维度: 时间响应性, 感知真实感
- 论文: https://arxiv.org/abs/2503.14445 (ICCV 2025)
- 视频: https://szymanowiczs.github.io/bolt3d/videos/single_vs_2_view.mp4
- 图片: https://szymanowiczs.github.io/bolt3d/img/rep_img.png
- 项目主页: https://szymanowiczs.github.io/bolt3d

#### Stable Virtual Camera — Stability AI (2025-03-18)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像, 多视角拍摄 / 扫描, 镜头路径 / 位姿 → 输出: 平面视频, 图像 / 全景图
- 核心想法: 仅凭几张照片就能沿精确的镜头路径“拍摄”一个场景，完全不必先建三维，适合制作标准化的刺激视频。
- 内容: Stability AI 的开源视图合成模型：给定一张或多张照片以及任意目标镜头路径（环绕、螺旋、滑动变焦等），即可生成三维一致的新视角和最长约半分钟、首尾闭合的流畅视频。
- 实现方式: 13 亿参数的多视角扩散模型，以输入视图和目标相机射线为条件，长轨迹采用两轮程序化采样，不需要三维蒸馏。
- 参数: 1.3B parameters · 576p · videos up to ~30 s
- 能力维度: 实验控制, 感知真实感
- 论文: https://arxiv.org/abs/2503.14489 (arXiv 2025)
- 视频: https://stable-virtual-camera.github.io/assets/task_overview.mp4
- 图片: https://stable-virtual-camera.github.io/img/seva.png
- 项目主页: https://stable-virtual-camera.github.io/
- 代码: https://github.com/Stability-AI/stable-virtual-camera

#### GEN3C — Xuanchi Ren, 英伟达 (2025-03-05)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像, 视频, 镜头路径 / 位姿 → 输出: 平面视频
- 核心想法: 在视频生成器之下保留一个显式三维缓存是一条折中路线：画面达到视频级质量，而镜头回来时世界仍在原处。
- 内容: 一个能精确控制镜头的视频模型：从一张或几张图像（或一段视频）出发，渲染与三维内容保持一致的新镜头轨迹，并提供绘制镜头路径的图形界面；基于 NVIDIA Cosmos，于 2025 年 6 月开源。
- 实现方式: 由输入预测的深度被反投影成点云三维缓存；沿用户镜头路径渲染该缓存，再以渲染结果为条件驱动视频扩散模型补洞并修正瑕疵。
- 能力维度: 实验控制, 持久性
- 论文: https://arxiv.org/abs/2503.03751 (CVPR 2025 (highlight))
- 视频: https://github.com/nv-tlabs/gen3c_website/raw/main/assets/cosmos/compressed/gui_demo.mp4
- 图片: https://research.nvidia.com/labs/toronto-ai/GEN3C/assets/cosmos/composed_single_view/grid_1_thumbnail.png
- 项目主页: https://research.nvidia.com/labs/toronto-ai/GEN3C/
- 代码: https://github.com/nv-tlabs/GEN3C

#### CAST — Kaixin Yao, 影眸科技 (2025-02-18)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 图像 → 输出: 网格 / 三维资产, 三维场景 / 世界
- 核心想法: 照片变成了一组彼此正确放置、相互接触的物体，这是场景里任何东西能被拿起或推动的前提。
- 内容: 把一张 RGB 照片重建为由独立、完整的物体网格组成的三维场景，物体之间的接触与支撑关系在物理上一致，因此可以逐个物体地编辑或仿真。
- 实现方式: 先做物体级分割与相对深度估计，再由考虑遮挡的生成模型生成每个物体的完整几何；位姿对齐模型负责摆放，物理感知的修正步骤借助关系图消除穿插与悬空。
- 能力维度: 持久性, 行为似真性, 实验控制
- 获奖与认可: SIGGRAPH 2025 Best Paper Award
- 论文: https://arxiv.org/abs/2502.12894 (ACM TOG (SIGGRAPH 2025))
- 视频: https://www.youtube.com/watch?v=xKnVOjs5go4
- 项目主页: https://sites.google.com/view/cast4

#### Wonderland — Hanwen Liang, Snap Inc. (2024-12-16)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 图像, 镜头路径 / 位姿 → 输出: 高斯泼溅 / 辐射场, 三维场景 / 世界
- 核心想法: 可控镜头视频模型的压缩潜变量本身就编码了多视角场景，直接从中读出三维可以省去解码与优化。
- 内容: Wonderland 从一张图像出发，以前馈方式重建大范围的三维高斯泼溅场景，连照片之外很远的背景区域也一并生成。
- 实现方式: 可控镜头的视频扩散模型沿指定轨迹生成潜变量；在该潜空间上渐进训练的大型重建模型预测出三维高斯。
- 能力维度: 感知真实感, 情境可达性
- 论文: https://arxiv.org/abs/2412.12091 (arXiv 2024)
- 视频: https://snap-research.github.io/wonderland/3d_autoregressive/00c5252d5_final.mp4
- 图片: https://snap-research.github.io/wonderland/teaser-final.png
- 项目主页: https://snap-research.github.io/wonderland/

#### MoGe — 微软 (2024-10-24)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像 → 输出: 图像 / 全景图, 三维场景 / 世界
- 核心想法: 预测点图而不是深度图，一步就能得到照片可用的三维布局，连相机参数也一并给出。
- 内容: 微软的开源模型，一次前向即可恢复任意照片的三维点图（几何及相机视场角）；MoGe-2（2025 年 7 月）加入真实尺度和更锐利的细节，MoGe-3（2026 年 8 月）进一步提升点图几何的精细度。
- 实现方式: ViT 模型预测仿射不变的点图，训练时使用稳健的最优对齐求解器和多尺度局部几何损失；后续版本加入真实尺度预测。
- 能力维度: 感知真实感, 实验控制
- 论文: https://arxiv.org/abs/2410.19115 (CVPR 2025 (oral))
- 视频: https://wangrc.site/MoGePage/static/videos/teaser/teaser_crf28.mp4
- 图片: https://raw.githubusercontent.com/microsoft/MoGe/main/assets/overview_simplified.png
- 项目主页: https://wangrc.site/MoGePage/
- 代码: https://github.com/microsoft/MoGe

#### Depth Pro — 苹果 (2024-10-02)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像 → 输出: 图像 / 全景图
- 核心想法: 从任意照片得到真实尺度的深度，是从图像走向几何最便宜的一步；多数照片转场景流程都从这里开始。
- 内容: Apple 的开源单目深度模型：不需要相机内参，在不到一秒内从一张照片预测出边缘锐利、具有真实尺度的深度图。
- 实现方式: 多尺度视觉 Transformer 编码器，结合真实与合成数据的训练课程，预测真实尺度深度，并直接从图像估计焦距。
- 参数: 2.25-megapixel depth map in 0.3 s on a standard GPU (authors)
- 能力维度: 感知真实感, 时间响应性
- 论文: https://arxiv.org/abs/2410.02073 (ICLR 2025)
- 视频: https://www.youtube.com/watch?v=no5yJje_mos
- 图片: https://raw.githubusercontent.com/apple/ml-depth-pro/main/data/depth-pro-teaser.jpg
- 项目主页: https://github.com/apple/ml-depth-pro
- 代码: https://github.com/apple/ml-depth-pro

#### Depth Anything V2 — Lihe Yang, 字节跳动 Seed (2024-06-14)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像, 视频 → 输出: 图像 / 全景图
- 核心想法: 任意图像的可靠深度，是许多“生成”三维场景之下看不见的一层：深度上的错误会变成世界里的错误。
- 内容: 开源单目深度模型（参数规模约从 2500 万到 13 亿），能为任意图像估计细致的相对深度，被广泛集成进三维照片、二维转三维视频和场景生成工具；它是 Depth Anything（2024 年 1 月）的后续版本。
- 实现方式: 只在精确的合成深度标签上训练的教师模型，为约 6200 万张真实图像生成伪标签，再用这些数据训练较小的学生模型（DINOv2 编码器加 DPT 解码头）。
- 参数: Small 25M · Base 98M · Large 335M · Giant 1.3B
- 能力维度: 感知真实感, 情境多样性
- 论文: https://arxiv.org/abs/2406.09414 (NeurIPS 2024)
- 视频: https://www.youtube.com/watch?v=zna5PrtDUFE
- 图片: https://depth-anything-v2.github.io/static/images/teaser.png
- 项目主页: https://depth-anything-v2.github.io/
- 代码: https://github.com/DepthAnything/Depth-Anything-V2

#### CAT3D — Ruiqi Gao, 谷歌 DeepMind (2024-05-16)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 图像, 多视角拍摄 / 扫描, 文字提示 → 输出: 三维场景 / 世界, 图像 / 全景图
- 核心想法: 多视角扩散补上了相机从未拍到的部分，这就是一张随手拍的照片如今能变成可漫游场所的原因。
- 内容: 从任意数量的照片（甚至一张图片或文生图的结果）出发，先想象出大量彼此一致的新视角，再加以重建，约一分钟即可得到完整的三维场景。
- 实现方式: 以输入视图和目标相机位姿为条件的多视角潜空间扩散模型，生成大量一致的新视角图像，再交给稳健的 NeRF 重建。
- 参数: about 1 min per scene (authors)
- 能力维度: 感知真实感, 创作可及性
- 论文: https://arxiv.org/abs/2405.10314 (NeurIPS 2024 (oral))
- 视频: https://cat3d.github.io/videos/teaser/cat_compress.mp4
- 图片: https://cat3d.github.io/img/rep_img.jpeg
- 项目主页: https://cat3d.github.io/

#### 基于上下文感知分层深度补全的三维摄影（3D Photography using Context-aware Layered Depth Inpainting） — Meng-Li Shih (2020)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像 → 输出: 图像 / 全景图, 平面视频
- 核心想法: 今天“空间场景”的源头：一张照片加上补全的隐藏图层，就已经能带来令人信服的纵深感。
- 内容: 把一张 RGB-D 照片（深度来自手机或深度估计）变成具有真实视差的“三维照片”，并合成前景物体背后被遮挡的颜色与深度，让镜头可以小幅移动。
- 实现方式: 先把照片转换为分层深度图像，再由学习得到的颜色与深度补全网络，在深度不连续处局部填补被遮挡区域，最后以网格形式渲染。
- 能力维度: 感知真实感
- 论文: https://arxiv.org/abs/2004.04727 (CVPR 2020)
- 视频: https://www.youtube.com/watch?v=D0JObXCfxv0
- 项目主页: https://shihmengli.github.io/3D-Photo-Inpainting/
- 代码: https://github.com/vt-vl-lab/3d-photo-inpainting

## 三维资产、角色与动作

按需生成的物体、角色与动画：一个被设计出来的情境里的道具与演员。

### 文生 / 图生三维

由提示词或照片生成网格与贴图：Meshy、Tripo、Rodin、Hunyuan3D、TRELLIS、SAM 3D……

#### Meshy 7 — Meshy (2026-08-12)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 产品 / 应用, 公开 API
- 输入: 图像, 文字提示 → 输出: 网格 / 三维资产
- 核心想法: 当明显的失败已不多见，三维生成的竞争就落在对参考图的忠实度和表面细节上，这在生成的道具必须对应某个真实物体时尤其重要。Meshy 称 Meshy 7 和 7.1 在其自建基准上领先，但这些并非独立测试。
- 内容: Meshy 针对“几何对齐”（生成形状与输入图像的吻合程度）调优的图生三维模型，并随模型发布了自建的对齐基准；2026 年 9 月 10 日的 Meshy 7.1 更新加入 Ultra 4K 模式，几何分辨率达 4096³，原始网格最多 8000 万个三角面。
- 实现方式: 专有的图生三维基础模型；7.1 把体素几何表示和生成主干从 2048³ 扩展到 4096³，并加入高精度网格提取与简化。
- 参数: 7.1 Ultra 4K: 4096³ geometry · up to 80M raw triangles
- 能力维度: 感知真实感, 创作可及性
- 视频: https://www.youtube.com/watch?v=FYl0ng2haZ8
- 图片: https://cdn.meshy.ai/landing-assets/blog/meshy-7/meshy-7-cover.webp https://cdn.meshy.ai/landing-assets/blog/meshy-7.1-launch/meshy-7-1-launch-cover-v2.webp
- 项目主页: https://www.meshy.ai/blog/meshy-7-image-to-3d-geometry-alignment
- API 文档: https://docs.meshy.ai/

#### Meshy 3D 智能体（Meshy 3D Agent） — Meshy (2026-05-29)
- 类型: 产品 / 应用 · 时序: 回合制 · 获取方式: 产品 / 应用
- 输入: 文字提示, 图像, 草图与手势 → 输出: 网格 / 三维资产, 对话 / 文本
- 核心想法: 把资产生成从单个提示框变成能规划、能迭代的对话，研究者也可以用这种方式“说”出情境所需的道具。
- 内容: Meshy 内置的对话式智能体：用户描述想法或上传照片、草图，智能体会提出方向、批量生成概念图，把选中的方案变成可下载的三维模型，还能通过对话为角色绑定和制作动画。
- 实现方式: 由大语言模型驱动的智能体，在一次对话中调度 Meshy 的图像生成、图生三维、贴图、绑定和动画工具；Meshy 还通过 MCP 服务器把这些工具开放给外部智能体。
- 能力维度: 创作可及性, 共创与能动性
- 视频: https://www.youtube.com/watch?v=YwnwaCpRNGE
- 图片: https://cdn.meshy.ai/landing-assets/blog/meshy-3d-agent/meshy-3d-agent-cover-new.webp
- 项目主页: https://www.meshy.ai/blog/meshy-3d-agent
- API 文档: https://www.meshy.ai/mcp

#### Rodin Gen-2.5 — 影眸科技 (2026-05-19)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 产品 / 应用, 公开 API
- 输入: 图像, 文字提示 → 输出: 网格 / 三维资产
- 核心想法: 给三维生成加入类似大语言模型的速度—质量调节，适合需要大量廉价背景道具和少数精细焦点物体的情境。
- 内容: Rodin Gen-2.5 可生成最多 1000 万面的网格，并允许用户调节自适应的“思考强度”，用时间换细节：从约 4 秒的草稿到耗时更长的主角级资产；同时提供原生三维贴图、单次最多 10 个结果以及手动部件拆分。
- 实现方式: 专有模型；影眸科技称其对几何和贴图采用自适应的推理时计算（“思考强度”）和原生三维贴图生成，并沿用 Gen-2 的部件式流程。
- 参数: up to 10M polygons · 1M-poly mesh in ~4 s (developer claims)
- 能力维度: 感知真实感, 实验控制
- 视频: https://www.youtube.com/watch?v=ymTb7eKc9ng
- 图片: https://storage.deemos.dev/assets/og-banner.png
- 项目主页: https://x.com/DeemosTech/status/2056744290689441833
- API 文档: https://docs.hyper3d.ai/

#### TripoSplat — VAST 光影焕像 (2026-05-07)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像 → 输出: 高斯泼溅 / 辐射场
- 核心想法: 以高斯泼溅形式生成的资产，可以直接放进真实场所的高斯泼溅扫描中，缩小了实拍环境与生成道具之间的差距。
- 内容: VAST 的开源模型，把单张图像生成为三维高斯而非网格，并学习高斯的分布密度，让基元集中在几何复杂的区域；同时发布了代码、权重和 ComfyUI 工作流。
- 实现方式: 密度采样高斯（DeG）：高斯中心从八叉树上的可学习概率密度中采样，用可微的渲染贡献梯度训练，再在 DeG 表示上训练潜扩散模型。
- 参数: MIT licence · variable-resolution decoding
- 能力维度: 感知真实感, 创作可及性
- 论文: https://arxiv.org/abs/2605.16355 (SIGGRAPH 2026 (Conference Papers))
- 视频: https://cdn-blog.holymolly.ai/media/production/triposplat-kv.mp4
- 图片: https://cdn-blog.holymolly.ai/media/production/Splat-kv-new.webp
- 项目主页: https://www.tripo3d.ai/research/triposplat
- 代码: https://github.com/VAST-AI-Research/TripoSplat

#### Seed3D 2.0 — 字节跳动 Seed (2026-04-23)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 公开 API
- 输入: 图像, 视频, 文字提示 → 输出: 网格 / 三维资产, 三维场景 / 世界
- 核心想法: 可动结构的输出（能拉开的抽屉、能转动的门）让生成的道具变成人或机器人可以操作的东西。
- 内容: 第二代 Seed3D，重点提升几何精度与材质质量；新增部件级分割与补全、以 URDF 格式导出带关节信息的可动资产（可用于 Isaac Sim 等仿真器），以及由图像、视频或文字进行场景组合。通过字节跳动火山引擎方舟平台提供。
- 实现方式: 由粗到细的两阶段几何生成，加上统一的混合专家（MoE）PBR 材质模型，并引入视觉语言先验以在未知光照下分解材质（据字节跳动 Seed 博客）。
- 能力维度: 感知真实感, 行为似真性
- 视频: https://lf3-static.bytednsdoc.com/obj/eden-cn/lapzild-tss/ljhwZthlaukjlkulzlp/user-upload/1vx23mnwp9xif.mp4
- 图片: https://lf3-static.bytednsdoc.com/obj/eden-cn/lapzild-tss/ljhwZthlaukjlkulzlp/user-upload/4og2ymo6oe71o.jpeg
- 项目主页: https://seed.bytedance.com/en/seed3d_2_0

#### Cube 4D 生成（Cube 4D generation） — Roblox (2026-02-04)
- 类型: 模型 · 时序: 回合制 · 获取方式: 候补 / 抢先体验, 产品 / 应用
- 输入: 文字提示 → 输出: 网格 / 三维资产, 智能体行为与动作
- 核心想法: 由参与者在游玩过程中生成、并遵守世界规则的物体：为“让身处生成情境中的人创造真正能用的东西”提供了具体范例。Roblox 称在一款游戏的早期测试中已生成超过 16 万个物体。
- 内容: Roblox 上“4D 生成”的测试版：玩家在游戏中输入提示词，就能得到一个可用的物体，例如可以坐进去开的车；做法是 Cube 按“模式”（schema）生成各个部件，再由 Roblox 为部件附加行为。
- 实现方式: Car-5（车身加四个车轮）、Body-1（任意单一网格）等模式规定物体所需的命名网格部件；Cube 生成这些部件，再由脚本行为让它们在体验中运转。
- 参数: beta schemas: Car-5, Body-1 · 160K+ objects in early access
- 能力维度: 共创与能动性, 行为似真性, 反应性
- 视频: https://www.youtube.com/watch?v=8y9k6AsPY6w
- 图片: https://cms-media.roblox.com/assets/63a0216d-5e83-1ba0-9156-5cb411951612.webp
- 项目主页: https://corp.roblox.com/newsroom/2026/02/accelerating-creation-powered-roblox-cube-foundation-model

#### ShapeR — Meta (2026-01-16)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 视频, 多视角拍摄 / 扫描 → 输出: 网格 / 三维资产
- 核心想法: 从“一张干净的产品照”到“戴着眼镜在真实房间走一圈”：能处理人们在现场随手拍下的杂乱素材的物体生成。
- 内容: 从随手拍摄的视频（例如 Aria 眼镜录制的画面）中，为每个检测到的物体利用 SLAM 点、带位姿的视图和自动生成的描述，生成具有真实尺度的三维形状；并附带一个包含 7 个真实场景、178 个物体的基准。
- 实现方式: 用视觉惯性 SLAM、三维检测和视觉语言模型描述提取每个物体的条件；再由以组合式数据增强和“物体到场景”课程训练的整流流 Transformer 生成各个形状。
- 参数: benchmark: 178 objects · 7 scenes
- 能力维度: 情境可达性, 感知真实感
- 论文: https://arxiv.org/abs/2601.11514 (arXiv preprint)
- 视频: https://www.youtube.com/watch?v=EbY30KAA55I
- 图片: https://facebookresearch.github.io/ShapeR/images/panel1.png
- 项目主页: https://facebookresearch.github.io/ShapeR/
- 代码: https://github.com/facebookresearch/ShapeR

#### TRELLIS.2 — 微软 (2025-12)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像 → 输出: 网格 / 三维资产
- 核心想法: 原生支持布料、树叶、内部结构等薄、开放和嵌套的表面，消除了生成道具常像封闭塑料壳的一个原因。
- 内容: TRELLIS 的后继：40 亿参数的图生三维模型，基于稀疏体素结构 O-Voxel，可同时编码任意拓扑（开放、非流形和完全封闭的表面）与 PBR 材质属性。
- 实现方式: 基于 O-Voxel 的稀疏压缩 VAE 提供紧凑的潜空间；在公开三维数据集上训练的大型流匹配 Transformer（40 亿参数）生成几何与材质。
- 参数: 4B parameters · MIT licence
- 能力维度: 感知真实感, 创作可及性
- 论文: https://arxiv.org/abs/2512.14692 (Technical report)
- 视频: https://microsoft.github.io/TRELLIS.2/assets/trellis2.mp4
- 图片: https://microsoft.github.io/TRELLIS.2/assets/method/overview.jpg
- 项目主页: https://microsoft.github.io/TRELLIS.2/
- 代码: https://github.com/microsoft/TRELLIS.2

#### SAM 3D（物体与人体）（SAM 3D (Objects and Body)） — Meta (2025-11-19)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像 → 输出: 网格 / 三维资产, 虚拟人（脸 / 身体）
- 核心想法: 把资产生成扎根于真实照片：任何一张房间或人物的快照，都能成为重建该情境所需的三维道具和人体的来源。
- 内容: Meta 的一对开源模型，可把普通照片中的东西“抬升”为三维：SAM 3D Objects 即使在杂乱或遮挡情况下也能重建选中物体的几何、贴图和摆放位置；SAM 3D Body 恢复包括手脚在内的全身人体网格，可用遮罩或关键点进行提示。
- 实现方式: Objects：在人与模型协同标注的数据上进行多阶段训练（先合成数据预训练，再与真实世界对齐）；Body：基于新的参数化网格 Momentum Human Rig（MHR）的编码器—解码器。
- 参数: ≥5:1 human-preference win rate on real-world objects (Meta)
- 能力维度: 创作可及性, 感知真实感
- 论文: https://arxiv.org/abs/2511.16624 (Technical report)
- 视频: https://www.youtube.com/watch?v=B7PZuM55ayc
- 图片: https://raw.githubusercontent.com/facebookresearch/sam-3d-objects/main/doc/intro.png
- 项目主页: https://ai.meta.com/sam3d/
- 代码: https://github.com/facebookresearch/sam-3d-objects

#### Seed3D 1.0 — 字节跳动 Seed (2025-10-22)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 图像 → 输出: 网格 / 三维资产, 三维场景 / 世界
- 核心想法: 把生成资产当作训练环境而不是美术素材：检验标准是智能体能否在物理仿真器中与之交互。
- 内容: 字节跳动 Seed 面向仿真的图生三维基础模型：生成几何准确、贴图对齐并带 PBR 材质的资产，可直接放入物理引擎用于机器人操作训练，也能组装成完整场景。
- 实现方式: 先用扩散 Transformer 生成几何，再进行多视角贴图与 PBR 材质合成；单个物体再被组装成用于仿真的场景。
- 能力维度: 感知真实感, 情境可达性
- 论文: https://arxiv.org/abs/2510.19944 (Technical report)
- 视频: https://lf3-static.bytednsdoc.com/obj/eden-cn/lapzild-tss/ljhwZthlaukjlkulzlp/user-upload/1vx23mh0jdhl0.mp4
- 图片: https://lf3-static.bytednsdoc.com/obj/eden-cn/lapzild-tss/ljhwZthlaukjlkulzlp/user-upload/1vx23mh0jdet6.jpg
- 项目主页: https://seed.bytedance.com/en/seed3d

#### Rodin Gen-2 — 影眸科技 (2025-09-24)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 产品 / 应用, 公开 API
- 输入: 图像, 文字提示 → 输出: 网格 / 三维资产
- 核心想法: 部件感知的生成把一整块几何拆成门、轮子、四肢等可分离的部分，便于之后做动画或交互。
- 内容: 影眸科技（Hyper3D）的第二代 Rodin 三维生成模型，官方称网格质量是 Gen-1.5 的四倍，并能按部件递归构建模型（“BANG to Parts”），让生成的物体可拆分为可编辑的组件。
- 实现方式: 延续 CLAY 路线的专有原生三维扩散模型，结合 BANG（生成式爆炸视图动力学）进行部件分解。
- 参数: 4× mesh quality vs Gen-1.5 (developer claim)
- 能力维度: 创作可及性, 实验控制
- 视频: https://www.youtube.com/watch?v=1VLCf5_lCug
- 项目主页: https://hyper3d.ai/
- API 文档: https://docs.hyper3d.ai/

#### 混元3D 3.0（Hunyuan3D 3.0） — 腾讯混元 (2025-09-16)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 产品 / 应用, 公开 API
- 输入: 图像, 文字提示, 草图与手势 → 输出: 网格 / 三维资产
- 核心想法: 体现了中国团队的一种模式：先开源权重（2.x），再推出通过云 API 和一体化工作台销售的闭源旗舰（3.x）。
- 内容: 腾讯面向生产资产的闭源旗舰模型，官方称精度是此前版本的三倍、几何分辨率达 1536³；它驱动混元3D 引擎（2025 年 11 月 26 日面向全球上线并开放腾讯云 API）以及 HY 3D Studio，后者把生成、重拓扑、UV、贴图、绑定和动画串成一条流程。
- 实现方式: 专有模型；腾讯称其采用 36 亿体素的高分辨率几何表示，支持图像、多视角和草图条件，很可能是混元3D-DiT 形状模型的放大版后继。
- 参数: 1536³ geometry · 3.6B voxels (Tencent claims)
- 能力维度: 感知真实感, 创作可及性
- 视频: https://x.com/TencentHunyuan/status/1967873084960260470
- 图片: https://www.tencent.com/wp-content/uploads/2025/11/f126e13e424fb6903c0891c383ecb495.jpg
- 项目主页: https://www.tencent.com/en-us/articles/2202235.html

#### Tripo 3.0 — VAST 光影焕像 (2025-08-20)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 产品 / 应用, 公开 API
- 输入: 图像, 文字提示 → 输出: 网格 / 三维资产
- 核心想法: 与 Meshy、Rodin、混元3D 并列的主要商用图生三维服务之一，也是与同一团队开源研究联系最紧密的一个。
- 内容: VAST 的第三代 Tripo 模型，几何更锐利并提供 Ultra 模式，可在 Tripo Studio 和 Tripo API 中使用；之后 Tripo 又推出 H3.1 高清模型（2026 年 5 月）和 P2.0 角色模型。
- 实现方式: 专有模型；VAST 已发表的研究（TripoSG 整流流形状模型）表明其可能是基于三维形状潜空间的大型整流流 Transformer，但 3.0 的架构未公开。
- 能力维度: 感知真实感, 创作可及性
- 视频: https://www.youtube.com/watch?v=uRZPf-2VmGs
- 图片: https://cdn-blog.holymolly.ai/media/production/Tripo3D_og-1.webp
- 项目主页: https://www.tripo3d.ai/
- API 文档: https://platform.tripo3d.ai/docs

#### Cube 3D — Roblox (2025-03-17)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码, 产品 / 应用
- 输入: 文字提示 → 输出: 网格 / 三维资产
- 核心想法: 把三维形状当作语言模型能读写的词元，朝着一个能为游戏平台生成物体、场景、绑定和脚本的统一模型迈出一步。
- 内容: Roblox Cube 三维基础模型首个开源部分：文字生成形状，可在 Roblox Studio 中使用，也能通过游戏内 API 调用，让创作者和他们的游戏都能由提示词生成网格。
- 实现方式: 三维形状分词器把网格转成离散词元；自回归 Transformer 由文字生成形状词元并解码回网格，同一套词元还支持形状转文字以及借助大语言模型的文字生成场景。
- 能力维度: 创作可及性, 情境多样性
- 论文: https://arxiv.org/abs/2503.15475 (Technical report)
- 视频: https://www.youtube.com/watch?v=85PNb99CT68
- 图片: https://raw.githubusercontent.com/Roblox/cube/main/resources/teaser.png
- 项目主页: https://corp.roblox.com/newsroom/2025/03/introducing-roblox-cube
- 代码: https://github.com/Roblox/cube

#### 混元3D 2.0（Hunyuan3D 2.0） — 腾讯混元 (2025-01-21)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码, 产品 / 应用
- 输入: 图像, 文字提示 → 输出: 网格 / 三维资产
- 核心想法: 社区和许多中国应用所依赖的开源权重模型；腾讯称截至 2025 年 11 月，其开源三维模型在 Hugging Face 的下载量已超过 300 万。
- 内容: 腾讯开源权重的两阶段三维资产系统：混元3D-DiT 由图像生成形状，混元3D-Paint 负责上贴图；同时提供 Blender 插件和网页工作台，2025 年 6 月的混元3D 2.1 又开源了 PBR 材质。
- 实现方式: 基于流的扩散 Transformer 在形状 VAE 潜空间中生成与条件图像对齐的几何，随后多视角扩散贴图模型为生成或手工制作的网格上色。
- 能力维度: 创作可及性, 感知真实感
- 论文: https://arxiv.org/abs/2501.12202 (Technical report)
- 视频: https://github.com/user-attachments/assets/a2cbc5b8-be22-49d7-b1c3-7aa2b20ba460
- 图片: https://raw.githubusercontent.com/Tencent-Hunyuan/Hunyuan3D-2/main/assets/images/teaser.jpg
- 项目主页: https://3d.hunyuan.tencent.com/
- 代码: https://github.com/Tencent-Hunyuan/Hunyuan3D-2

#### TRELLIS — 微软 (2024-12-02)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像, 文字提示 → 输出: 网格 / 三维资产, 高斯泼溅 / 辐射场
- 核心想法: 一个潜变量、多种输出格式：同一个生成物体既可做游戏网格，也可做照片级场景里的高斯泼溅，局部还能重新生成而不必从头来过。
- 内容: 微软开源的三维生成模型，基于结构化潜变量（SLAT）表示，可解码为网格、三维高斯或辐射场；可由图像或文字生成资产，并支持局部三维编辑。
- 实现方式: 携带多视角 DINOv2 特征的稀疏三维体素网格被编码为结构化潜变量，再由最多 20 亿参数、在 50 万个资产上训练的整流流 Transformer 生成。
- 参数: up to 2B parameters · 500K training assets · MIT licence
- 能力维度: 创作可及性, 情境多样性
- 论文: https://arxiv.org/abs/2412.01506 (CVPR 2025)
- 视频: https://microsoft.github.io/TRELLIS/assets/teaser.mp4
- 图片: https://microsoft.github.io/TRELLIS/assets/pipeline.png
- 项目主页: https://microsoft.github.io/TRELLIS/
- 代码: https://github.com/microsoft/TRELLIS

#### Meshy-4 — Meshy (2024-08-22)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 产品 / 应用, 公开 API
- 输入: 文字提示, 图像 → 输出: 网格 / 三维资产
- 核心想法: 标志着商用三维生成从“远看还行”转向几何细节足以用作游戏道具。
- 内容: Meshy 第四代模型，重做了文生三维和图生三维的几何质量，硬表面造型更干净，并采用两步式文生三维流程：先出无贴图预览，再上贴图。
- 实现方式: 专有三维生成模型（架构未公开）；文生三维拆成快速预览网格阶段和单独的 PBR 贴图阶段。
- 能力维度: 创作可及性, 感知真实感
- 视频: https://www.youtube.com/watch?v=AH58ABQbXd8
- 图片: https://cdn.meshy.ai/landing-assets/blog/meshy-4-break-grounds/cover.png
- 项目主页: https://www.meshy.ai/blog/meshy-4-break-grounds
- API 文档: https://docs.meshy.ai/

#### Stable Fast 3D (SF3D) — Stability AI (2024-08-01)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码, 公开 API
- 输入: 图像 → 输出: 网格 / 三维资产
- 核心想法: 亚秒级、可重新打光的网格，使在体验进行中生成道具成为可能，而不必放在前期制作阶段。
- 内容: Stability AI 的单图生网格模型，约 0.5 秒返回已展开 UV、带贴图并预测了材质参数的网格，贴图中的光照已被去除，可重新打光。
- 实现方式: 专门为网格输出训练的大型重建 Transformer，带快速 UV 展开、材质与法线贴图预测以及去光照步骤。
- 参数: ~0.5 s per mesh
- 能力维度: 时间响应性, 创作可及性
- 论文: https://arxiv.org/abs/2408.00653 (Technical report)
- 视频: https://www.youtube.com/watch?v=uT96UCBSBko
- 项目主页: https://stability.ai/news/introducing-stable-fast-3d
- 代码: https://github.com/Stability-AI/stable-fast-3d

#### Meta 3D Gen (AssetGen) — Meta (2024-07-02)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 文字提示 → 输出: 网格 / 三维资产
- 核心想法: 真正让生成资产在 VR 场景自身光照下显得可信的，是基于物理的材质，而不是烘焙进去的颜色。
- 内容: Meta 的文生三维流程，结合 3D AssetGen（由文字生成带 PBR 材质的网格）与 3D TextureGen（贴图与重新贴图），Meta 称可在一分钟内生成一个资产。
- 实现方式: AssetGen 先生成带着色与反照率通道的多视角图像，用大型重建模型重建有向距离场和 PBR 材质，再在 UV 空间细化贴图。
- 参数: <1 min per asset (Meta claim)
- 能力维度: 感知真实感, 创作可及性
- 论文: https://arxiv.org/abs/2407.02445 (Technical report)
- 视频: https://www.youtube.com/watch?v=xY_2jAEcBa0
- 图片: https://assetgen.github.io/static/teaser/teaser.jpg
- 项目主页: https://assetgen.github.io/

#### CLAY（Rodin Gen-1）（CLAY (Rodin Gen-1)） — Longwen Zhang, 影眸科技 (2024-05-30)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 文字提示, 图像, 多视角拍摄 / 扫描 → 输出: 网格 / 三维资产
- 核心想法: 主张直接用原生三维数据训练，而不是从二维模型蒸馏，这成为生产级资产的主流做法（混元3D、TRELLIS、TripoSG）。
- 内容: 影眸科技 Rodin Gen-1 背后的原生三维生成模型：直接在三维几何上训练的潜扩散 Transformer，可由文字、图像或体素、包围盒、点云等三维控制生成网格与 PBR 材质。
- 实现方式: 基于神经场几何的多分辨率 VAE，加上简洁的潜扩散 Transformer，在大规模精选三维数据上分阶段训练；PBR 材质由单独的多视角扩散模型生成。
- 能力维度: 创作可及性, 实验控制
- 论文: https://arxiv.org/abs/2406.13897 (ACM TOG (SIGGRAPH 2024))
- 视频: https://www.youtube.com/watch?v=YcKFp4U2Voo
- 项目主页: https://sites.google.com/view/clay-3dlm

#### TripoSR — VAST 光影焕像, Stability AI (2024-03-04)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像 → 输出: 网格 / 三维资产
- 核心想法: 速度快、许可宽松（MIT），可直接嵌入其他工具，成为按需插入道具的基础组件。
- 内容: Stability AI 与 Tripo AI 联合发布的开源权重图生三维模型，在 NVIDIA A100 上不到半秒即可由单张图像重建带贴图的网格。
- 实现方式: LRM 式 Transformer 将 DINO 图像特征映射为三平面 NeRF，并改进了数据筛选、模型设计和训练，最后用 Marching Cubes 提取网格。
- 参数: <0.5 s per object on A100 · MIT licence
- 能力维度: 时间响应性, 创作可及性
- 论文: https://arxiv.org/abs/2403.02151 (Technical report)
- 视频: https://www.youtube.com/watch?v=il0THDcRaDY
- 图片: https://raw.githubusercontent.com/VAST-AI-Research/TripoSR/main/figures/teaser800.gif
- 项目主页: https://stability.ai/news/triposr-3d-generation
- 代码: https://github.com/VAST-AI-Research/TripoSR

#### Genie（Luma 文生三维）（Genie (Luma)） — Luma AI (2024-01-09)
- 类型: 产品 / 应用 · 时序: 预先生成 · 获取方式: 产品 / 应用
- 输入: 文字提示 → 输出: 网格 / 三维资产
- 核心想法: 让文生三维变成以秒计的大众操作；此后 Luma 把重心转向视频模型，Genie 的独立页面如今已跳转到其主站。
- 内容: Luma 的文生三维工具：输入提示词，几秒内返回多个候选三维模型，可选其一细化为质量更高的带贴图网格并下载，可在浏览器或 Discord 中使用。
- 实现方式: 专有的前馈式三维生成模型（架构未公开），分为快速草稿阶段和单独的细化阶段。
- 参数: drafts in <10 s (developer claim)
- 能力维度: 创作可及性, 情境多样性
- 视频: https://www.youtube.com/watch?v=5rW98mMdP6I
- 项目主页: https://lumalabs.ai/genie

#### LRM：大型重建模型（LRM: Large Reconstruction Model） — Yicong Hong, Adobe (2023-11-08)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 图像 → 输出: 高斯泼溅 / 辐射场, 网格 / 三维资产
- 核心想法: 用一次前馈推理取代逐物体优化，把图生三维从数小时缩短到数秒；TripoSR、InstantMesh 和多数生产流程都沿用了这一模板。
- 内容: 一个 5 亿参数的 Transformer，约 5 秒即可从单张图像预测物体的三平面 NeRF，训练数据为来自 Objaverse 和 MVImgNet 的约一百万个物体。
- 实现方式: 在图像到三平面的 Transformer 解码器中，可学习的三平面词元对 DINO 图像特征做交叉注意力，并用多视角数据上的渲染损失端到端训练。
- 参数: 500M parameters · ~5 s per object · ~1M training objects
- 能力维度: 创作可及性, 时间响应性
- 论文: https://arxiv.org/abs/2311.04400 (ICLR 2024)
- 视频: https://www.youtube.com/watch?v=RD-UhM1kBVY
- 项目主页: https://research.adobe.com/publication/lrm-large-reconstruction-model-for-single-image-to-3d/

#### DreamGaussian — Jiaxiang Tang (2023-09-28)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像, 文字提示 → 输出: 高斯泼溅 / 辐射场, 网格 / 三维资产
- 核心想法: 把高斯泼溅引入生成任务，将基于优化的图生 / 文生三维从数小时缩短到几分钟，是资产模型走向显式三维表示的一步。
- 内容: 通过分数蒸馏优化三维高斯，再提取网格并细化 UV 贴图，约两分钟即可由一张图像（或一句文字提示）生成带贴图的网格。
- 实现方式: 在 SDS 指导下（图像用 Zero-1-to-3，文字用 Stable Diffusion）逐步加密三维高斯，随后提取网格并在 UV 空间细化贴图。
- 参数: ~2 min per image-to-3D asset
- 能力维度: 创作可及性, 时间响应性
- 论文: https://arxiv.org/abs/2309.16653 (ICLR 2024 (Oral))
- 视频: https://dreamgaussian.github.io/videos/text-to-image-to-3d.mp4
- 项目主页: https://dreamgaussian.github.io/
- 代码: https://github.com/dreamgaussian/dreamgaussian

#### Zero-1-to-3 — Ruoshi Liu (2023-03-20)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像, 镜头路径 / 位姿 → 输出: 图像 / 全景图, 网格 / 三维资产
- 核心想法: 把二维图像模型变成可控视角的物体渲染器，从此一张照片成为三维资产生成的默认输入。
- 内容: 微调 Stable Diffusion，使其根据一张照片和相对相机旋转，生成同一物体在新视角下的图像；这些视图再通过分数蒸馏提升为三维模型。
- 实现方式: 以输入图像和相对相机位姿为条件的潜扩散模型，在 Objaverse 物体渲染图上微调；再用分数蒸馏把结果重建为神经场。
- 能力维度: 创作可及性, 感知真实感
- 论文: https://arxiv.org/abs/2303.11328 (ICCV 2023)
- 视频: https://www.youtube.com/watch?v=H5dVW5yOfPY
- 图片: https://zero123.cs.columbia.edu/assets/teaser.png
- 项目主页: https://zero123.cs.columbia.edu/
- 代码: https://github.com/cvlab-columbia/zero123

#### DreamFusion — Ben Poole, 谷歌 (2022-09-29)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 文字提示 → 输出: 高斯泼溅 / 辐射场, 网格 / 三维资产
- 核心想法: 证明了无需任何三维训练数据就能从二维图像模型中“提取”出三维物体，是文生三维路线的起点，代价是每个物体都要缓慢优化。
- 内容: 谷歌研究院的文生三维方法：以冻结的二维文生图扩散模型（Imagen）作为唯一指导，从零优化一个神经辐射场（NeRF）；输入一句提示词，经过较长的逐物体优化后得到可重新打光的三维物体。
- 实现方式: 分数蒸馏采样（SDS）：从随机视角渲染随机初始化的 NeRF，用 Imagen 去噪损失的梯度更新它，并加入着色项以促使形成真实几何。
- 参数: per-prompt NeRF optimization · Imagen 64×64 prior
- 能力维度: 创作可及性, 情境多样性
- 获奖与认可: ICLR 2023 Outstanding Paper Award
- 论文: https://arxiv.org/abs/2209.14988 (ICLR 2023)
- 视频: https://dreamfusion-cdn.ajayj.com/dreamfusion_overview.mp4
- 图片: https://dreamfusion3d.github.io/assets/images/dreamfusion_samples.png
- 项目主页: https://dreamfusion3d.github.io/

### 角色、绑定与动画

带骨骼的生成角色、自动绑定与可直接用于引擎的动画。

#### Tripo P2.0 — VAST 光影焕像 (2026-09-06)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 产品 / 应用, 公开 API
- 输入: 图像, 文字提示 → 输出: 网格 / 三维资产, 动作 / 动画
- 核心想法: 布线合理的四边形拓扑，是生成角色在运动时能正确变形的前提；P2.0 针对的正是“雕像”与“演员”之间的差距。
- 内容: Tripo 的角色模型，可由图像或提示词生成带干净四边形拓扑、可直接做动画的角色；2026 年 9 月 6 日发布预览，10 月 1 日正式上线。
- 实现方式: 专有模型；VAST 尚未公开其架构。
- 能力维度: 创作可及性, 感知真实感
- 视频: https://www.youtube.com/watch?v=g4ozFeSBPfo
- 项目主页: https://www.tripo3d.ai/
- API 文档: https://platform.tripo3d.ai/docs

#### Puppeteer — Chaoyue Song, 字节跳动 Seed (2025-08-14)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入:  → 输出: 网格 / 三维资产, 动作 / 动画
- 核心想法: 补上了从静态生成模型到动画资产之间的一步，而且适用于任何类别的物体，而不只是有标准骨架的角色。
- 内容: 为任意三维模型绑定并制作动画：自回归 Transformer 预测骨架，注意力网络预测蒙皮权重，再由优化阶段生成稳定、高保真的动画。
- 实现方式: 骨架生成采用基于关节的分词、层级排序与随机扰动；蒙皮采用感知拓扑的关节注意力；动画由可微的基于优化的流程生成。
- 能力维度: 创作可及性, 感知真实感
- 论文: https://arxiv.org/abs/2508.10898 (NeurIPS 2025 (Spotlight))
- 视频: https://www.youtube.com/watch?v=DnKx803JHyI
- 图片: https://chaoyuesong.github.io/Puppeteer/static/images/method/method.png
- 项目主页: https://chaoyuesong.github.io/Puppeteer/
- 代码: https://github.com/Seed3D/Puppeteer

#### UniRig — Jia-Peng Zhang, VAST 光影焕像 (2025-04-16)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入:  → 输出: 网格 / 三维资产
- 核心想法: 一个模型适用于各种生物——当生成器产出的不再只是人形角色时，这一点很关键。
- 内容: 清华大学与 VAST 合作的统一自动绑定模型，可为人类、动物以及骨架结构差异很大的其他角色生成拓扑正确的骨架和蒙皮权重。
- 实现方式: 采用“骨架树分词”的自回归 Transformer 生成骨骼层级，骨骼—点交叉注意力模块预测蒙皮权重；在包含 1.4 万多个已绑定模型的 Rig-XL 上训练。
- 参数: Rig-XL: 14K+ rigged models
- 能力维度: 创作可及性, 情境多样性
- 论文: https://arxiv.org/abs/2504.12451 (ACM TOG (SIGGRAPH 2025))
- 视频: https://zjp-shadow.github.io/works/UniRig/static/videos/teaser-720p.mp4
- 图片: https://zjp-shadow.github.io/works/UniRig/static/images/result.webp
- 项目主页: https://zjp-shadow.github.io/works/UniRig/
- 代码: https://github.com/VAST-AI-Research/UniRig

#### Make-It-Animatable — Zhiyang Guo (2024-11-27)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入:  → 输出: 网格 / 三维资产, 动作 / 动画
- 核心想法: 亚秒级绑定意味着在体验中生成的角色可以马上动起来。
- 内容: 无论输入姿态如何，都能在一秒内预测混合权重、骨骼和姿态变换，让任意三维人形模型（网格或高斯泼溅）可以直接做动画。
- 实现方式: 基于粒子的形状自编码器，以由粗到细、感知结构的方式，相对标准人形骨架预测蒙皮权重、骨骼位置和姿态到静止姿态的变换。
- 参数: <1 s per character
- 能力维度: 创作可及性, 时间响应性
- 论文: https://arxiv.org/abs/2411.18197 (CVPR 2025)
- 视频: https://www.youtube.com/watch?v=mH6L9r_28LA
- 图片: https://jasongzy.github.io/Make-It-Animatable/static/images/teaser.jpg
- 项目主页: https://jasongzy.github.io/Make-It-Animatable/
- 代码: https://github.com/jasongzy/Make-It-Animatable

#### Meshy 自动绑定与动画（Meshy auto-rigging and animation） — Meshy (2024-07-04)
- 类型: 产品 / 应用 · 时序: 预先生成 · 获取方式: 产品 / 应用, 公开 API
- 输入:  → 输出: 网格 / 三维资产, 动作 / 动画
- 核心想法: 把道具变成演员的商用默认方案：生成的角色一键就能成为会动的群演，只是动作来自固定预设库而非生成。
- 内容: Meshy 的绑定与动画工具：上传或生成的人形、四足角色可在几秒内自动绑定，并从 600 多个动作预设（走路循环、待机、跳跃、攻击等）中选择动画，再导出到游戏引擎。
- 实现方式: 为人形和四足网格自动拟合骨架和蒙皮，再把 Meshy 动画库中动捕风格的预设重定向到角色上。
- 参数: 600+ motion presets
- 能力维度: 创作可及性
- 视频: https://www.youtube.com/watch?v=DRYu_M76qoM
- 图片: https://cdn.meshy.ai/landing-assets/og-images/animation_og.webp
- 项目主页: https://www.meshy.ai/features/ai-animation-generator
- API 文档: https://docs.meshy.ai/

#### Animate Anything（万物动画）（Animate Anything） — Anything World (2023-09-28)
- 类型: 产品 / 应用 · 时序: 预先生成 · 获取方式: 产品 / 应用
- 输入:  → 输出: 网格 / 三维资产, 动作 / 动画
- 核心想法: 把自动绑定扩展到人形之外，让场景中的动物和机械也能动起来。
- 内容: Anything World 的服务：自动为上传的三维模型（包括动物、交通工具和其他非人形物体）绑定并制作动画，返回可直接用于引擎的动画资产。
- 实现方式: 专有系统；很可能先识别模型类别，再放置对应类别的骨架、计算蒙皮，并套用相应的动画集。
- 能力维度: 创作可及性, 情境多样性
- 视频: https://www.youtube.com/watch?v=EVKFVvIu3FQ
- 图片: https://cdn.prod.website-files.com/6101e033eba551a09cbbe91c/64f342ce3a3dc9a3448a5e91_autoRigg_home_small_2.png
- 项目主页: https://anything.world/

#### RigNet — Zhan Xu (2020-05-01)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入:  → 输出: 网格 / 三维资产
- 核心想法: “先生成角色、再让它动起来”且无需绑定师这一路线的起点。
- 内容: 一个神经网络，可为任意关节角色网格预测骨架和蒙皮权重，是首个适用于人形之外多样形体的学习式自动绑定方法。
- 实现方式: 在网格上运行的图神经网络先预测关节位置，再通过对学习到的边概率求最小生成树得到骨骼连接，最后预测蒙皮权重；训练数据为约 2700 个已绑定角色。
- 能力维度: 创作可及性
- 论文: https://arxiv.org/abs/2005.00559 (ACM TOG (SIGGRAPH 2020))
- 视频: https://www.youtube.com/watch?v=J90VETgWIDg
- 图片: https://zhan-xu.github.io/rig-net/teaser.png
- 项目主页: https://zhan-xu.github.io/rig-net/
- 代码: https://github.com/zhan-xu/RigNet

### 人体动作生成

由文字或音频生成身体、手部与交互动作的模型。

#### ARDY — Kaifeng Zhao, 英伟达 (2026-07-09)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 文字提示, 场景规格、代码与规则 → 输出: 动作 / 动画
- 核心想法: 把文生动作从离线片段推进到实时、可操控的身体——当参与者在场景中途改变情境时，生成的虚拟人正需要这种能力。
- 内容: 英伟达与苏黎世联邦理工学院的流式动作生成模型，可实时生成三维人体动作，并能随时接收新的文字提示和运动学约束：根轨迹、路径点、全身关键帧和稀疏关节目标。
- 实现方式: 基于混合表示（显式根节点特征加潜在身体嵌入）的两阶段自回归 Transformer 去噪器，支持可变长度的历史上下文和长时程约束条件，在大规模动捕语料上训练。
- 能力维度: 时间响应性, 实验控制, 反应性
- 论文: https://arxiv.org/abs/2607.08741 (ACM TOG (SIGGRAPH 2026))
- 视频: https://research.nvidia.com/labs/sil/projects/ardy/assets/videos/ardy_siggraph_video_cam_ready.mp4
- 图片: https://raw.githubusercontent.com/nv-tlabs/ardy/main/assets/banner.png
- 项目主页: https://research.nvidia.com/labs/sil/projects/ardy/
- 代码: https://github.com/nv-tlabs/ardy

#### 混元 HY-Motion 1.0（HY-Motion 1.0） — 腾讯混元 (2025-12-30)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 文字提示 → 输出: 动作 / 动画
- 核心想法: 规模化来到了动作生成：更多数据和更大模型显著提升了对提示的遵循，缩小了身体动作与文生视频之间的差距。
- 内容: 腾讯开源权重的十亿参数文生动作模型，可由自然语言提示生成用于角色动画的三维人体动作，覆盖 200 多个动作类别，并发布了 Lite 版本和 Hugging Face 演示。
- 实现方式: 基于流匹配的扩散 Transformer，先在 3000 多小时动作数据上预训练，再用 400 小时精选数据微调，最后用人类反馈与奖励模型做强化学习对齐。
- 参数: 1B parameters · 3,000+ h pretraining · 200+ motion categories
- 能力维度: 情境多样性, 实验控制
- 论文: https://arxiv.org/abs/2512.23464 (Technical report)
- 视频: https://x.com/TencentHunyuan/status/2005916817987100708
- 图片: https://huggingface.co/tencent/HY-Motion-1.0/resolve/main/assets/teaser.jpg
- 项目主页: https://hunyuan.tencent.com/motion
- 代码: https://github.com/Tencent-Hunyuan/HY-Motion-1.0

#### Meta Motivo — Meta (2024-12)
- 类型: 模型 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 身体、面部与视线追踪, 场景规格、代码与规则 → 输出: 动作 / 动画, 智能体行为与动作
- 核心想法: 一个用目标来“提示”而不必按任务重训的预训练身体控制器：有望成为实验者可以随时设定行为的虚拟身体。
- 内容: Meta FAIR 面向物理仿真人形的行为基础模型：无需再训练，就能在测试时追踪一段动作、到达目标姿态或优化指定的奖励，并提供交互式网页演示。
- 实现方式: 带条件策略正则化的前向—后向表示（FB-CPR）：在状态、动作与奖励共享的潜空间中进行无监督强化学习，并向无标注动捕数据正则化；在 MuJoCo 中的 SMPL 人形上训练。
- 能力维度: 反应性, 适应性
- 论文: https://arxiv.org/abs/2504.11054 (ICLR 2025)
- 视频: https://metamotivo.metademolab.com/assets/demo_1080p-ccfbbf9f.mp4
- 图片: https://metamotivo.metademolab.com/bg_share.png
- 项目主页: https://metamotivo.metademolab.com/
- 代码: https://github.com/facebookresearch/metamotivo

#### MaskedMimic — Chen Tessler, 英伟达 (2024-09-22)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 文字提示, 身体、面部与视线追踪 → 输出: 动作 / 动画, 智能体行为与动作
- 核心想法: 会对推挤、地形和物体作出反应、并能按情境设计者设定的任意约束来操控的物理仿真角色，比运动学动画片段更接近真正“会表演”的演员。
- 内容: 一个用于仿真人形的统一物理控制器，可根据任意不完整的描述（稀疏关键帧、VR 头部与手部追踪、文字或要交互的物体）补全全身动作，并在物理仿真器中运行。
- 实现方式: 动作补全：把动作追踪教师策略蒸馏为以掩码动作描述为输入的条件 VAE 策略，在 NVIDIA Isaac Gym 中用大规模动捕数据训练；代码在 ProtoMotions 中开源。
- 能力维度: 反应性, 实验控制, 行为似真性
- 论文: https://arxiv.org/abs/2409.14393 (ACM TOG (SIGGRAPH Asia 2024))
- 视频: https://www.youtube.com/watch?v=rePVn1xDWlo
- 图片: https://research.nvidia.com/labs/par/projects/maskedmimic/assets/teaser.jpg
- 项目主页: https://research.nvidia.com/labs/par/projects/maskedmimic/
- 代码: https://github.com/NVlabs/ProtoMotions

#### SayMotion — DeepMotion (2023-12-08)
- 类型: 产品 / 应用 · 时序: 预先生成 · 获取方式: 产品 / 应用
- 输入: 文字提示, 视频 → 输出: 动作 / 动画
- 核心想法: 较早的商业实例：动画师用打字代替动作捕捉，适合快速为生成角色排出动作草稿。
- 内容: DeepMotion 的文生三维动画工具：用文字描述动作即可得到三维角色动画，可继续细化、循环，或与从普通视频中捕捉的动作组合，再导出为常见三维格式。
- 实现方式: 专有的文生动作模型，很可能结合了 DeepMotion 的无标记视频动作捕捉（Animate 3D）。
- 能力维度: 创作可及性
- 视频: https://www.youtube.com/watch?v=6b2Lk3A_dzI
- 项目主页: https://www.deepmotion.com/saymotion

#### MoMask — Chuan Guo (2023-11-29)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 文字提示 → 输出: 动作 / 动画
- 核心想法: 离散的掩码生成让动作质量大幅提升，至今仍是文字驱动身体的强力开源基线。
- 内容: 把动作表示为分层残差词元、并用掩码 Transformer 生成的文生动作模型，在 HumanML3D 上的保真度高于扩散基线，并支持时间维度上的补全。
- 实现方式: 残差 VQ-VAE 把动作量化为基础层和若干残差层；掩码 Transformer 由文字预测基础层词元，残差 Transformer 补全更细的层。
- 参数: HumanML3D FID 0.045 (authors)
- 能力维度: 感知真实感, 实验控制
- 论文: https://arxiv.org/abs/2312.00063 (CVPR 2024)
- 视频: https://www.youtube.com/watch?v=T5Wqxs37vg0
- 项目主页: https://ericguo5513.github.io/momask/
- 代码: https://github.com/EricGuo5513/momask-codes

#### MotionGPT — Biao Jiang (2023-06-26)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 开源权重 / 代码
- 输入: 文字提示 → 输出: 动作 / 动画, 对话 / 文本
- 核心想法: 让身体动作和语言处在同一个词元序列中，后来的对话智能体由此可以用一个模型同时说话和动作。
- 内容: 把人体动作当作一门外语：先把动作分词，再让语言模型在文字与动作混合的词元上训练，于是一个模型就能由文字生成动作、为动作写描述，以及预测或补间动作。
- 实现方式: VQ-VAE 动作分词器，加上在动作—语言语料上预训练、并在基于提示的动作任务上做指令微调的 T5 语言模型。
- 能力维度: 创作可及性, 实验控制
- 论文: https://arxiv.org/abs/2306.14795 (NeurIPS 2023)
- 视频: https://www.youtube.com/watch?v=AH_q9P5dQ-c
- 项目主页: https://motion-gpt.github.io/
- 代码: https://github.com/OpenMotionLab/MotionGPT

#### EDGE — Jonathan Tseng (2022-11-19)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 语音与音频 → 输出: 动作 / 动画
- 核心想法: 可加编辑约束的音频驱动身体生成：音乐（进而语音或声音）驱动身体，同时可以固定选定的姿态。
- 内容: 用扩散模型由音乐生成舞蹈编排，并提供按关节约束、补间和任意长度续写等编辑控制。
- 实现方式: 以 Jukebox 音乐嵌入为条件的 Transformer 扩散模型，加入足部接触一致性损失并提出新的物理足部接触评分；在 AIST++ 上训练。
- 能力维度: 感知真实感, 实验控制
- 论文: https://arxiv.org/abs/2211.10658 (CVPR 2023)
- 视频: https://edge-dance.github.io/assets/media/gallery1.mp4
- 图片: https://edge-dance.github.io/assets/media/cover.png
- 项目主页: https://edge-dance.github.io/
- 代码: https://github.com/Stanford-TML/EDGE

#### MDM：人体动作扩散模型（MDM: Human Motion Diffusion Model） — Guy Tevet (2022-09-29)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 文字提示 → 输出: 动作 / 动画
- 核心想法: 把扩散模型带入动作生成并让其可编辑：可以固定关键帧或部分身体，其余部分由模型生成——这是对生成身体的一种基本实验控制。
- 内容: 由文字或动作标签生成人体动作的扩散模型，无需重新训练即可完成补间、身体部位补全等编辑。
- 实现方式: 在姿态序列上运行的 Transformer 编码器扩散模型，直接预测干净样本而非噪声，从而可以加入足部接触和速度等几何损失；以 CLIP 编码文字条件；在 HumanML3D 和 KIT-ML 上训练。
- 能力维度: 情境多样性, 实验控制
- 论文: https://arxiv.org/abs/2209.14916 (ICLR 2023)
- 视频: https://www.youtube.com/watch?v=rVkIDj5wgjs
- 图片: https://guytevet.github.io/mdm-page/static/figures/mdm_arch.png
- 项目主页: https://guytevet.github.io/mdm-page/
- 代码: https://github.com/GuyTevet/motion-diffusion-model

#### HumanML3D — Chuan Guo (2022-06)
- 类型: 数据集 / 基准 · 获取方式: 开源权重 / 代码
- 输入: 文字提示 → 输出: 动作 / 动画
- 核心想法: 2022 年以来几乎所有文生动作模型都在它上面训练和评测，因此它的覆盖范围（以日常单人动作为主，社交互动很少）决定了生成身体能做什么。
- 内容: 包含 14,616 段人体动作与 44,970 条文字描述的数据集（共 28.59 小时，来自 AMASS 和 HumanAct12），并附带一个文生动作基线模型；是文生动作的标准基准。
- 实现方式: 对 AMASS 和 HumanAct12 动作片段进行众包文字标注，并提供一个先由文字预测动作长度、再生成动作的时序 VAE。
- 参数: 14,616 motions · 44,970 descriptions · 28.59 h
- 能力维度: 情境多样性, 实验控制
- 论文: https://openaccess.thecvf.com/content/CVPR2022/html/Guo_Generating_Diverse_and_Natural_3D_Human_Motions_From_Text_CVPR_2022_paper.html (CVPR 2022)
- 视频: https://www.youtube.com/watch?v=085mBtMeZpg
- 图片: https://ericguo5513.github.io/text-to-motion/model.png
- 项目主页: https://ericguo5513.github.io/text-to-motion/
- 代码: https://github.com/EricGuo5513/HumanML3D

## 捕捉、重建与 4D

把真实世界变成可漫游的三维与四维（三维加时间）：辐射场与高斯泼溅、几秒内完成的前馈式重建、动态场景、生成式 4D 与体积视频。

### NeRF 与高斯泼溅

让照片级、实时的新视角渲染成为可能的表示方法。

#### 3DGUT — Qi Wu, 英伟达 (2024-12-17)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 多视角拍摄 / 扫描 → 输出: 高斯泼溅 / 辐射场
- 核心想法: 去掉了必须使用理想针孔相机拍摄的前提，让更多真实素材可以变成场景。
- 内容: 3DGUT 保留了泼溅光栅化的速度，同时支持鱼眼镜头、卷帘快门等畸变相机，使机器人、汽车和头显拍摄的素材可以直接用于重建。
- 实现方式: 用无迹变换把每个高斯的 sigma 点通过精确相机模型投影，而不是对其线性化，并与 3DGRT 共用以实现混合渲染。
- 能力维度: 情境可达性, 感知真实感
- 论文: https://arxiv.org/abs/2412.12507 (CVPR 2025)
- 视频: https://research.nvidia.com/labs/toronto-ai/3DGUT/res/3DGUT_ready_compressed.mp4
- 图片: https://research.nvidia.com/labs/toronto-ai/3DGUT/res/teaser.jpg
- 项目主页: https://research.nvidia.com/labs/toronto-ai/3DGUT/
- 代码: https://github.com/nv-tlabs/3dgrut

#### 3D 高斯光线追踪（3DGRT）（3D Gaussian Ray Tracing (3DGRT)） — Nicolas Moenne-Loccoz, 英伟达 (2024-07-09)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 多视角拍摄 / 扫描 → 输出: 高斯泼溅 / 辐射场
- 核心想法: 让捕捉的场景可以与插入的物体和光照效果混合，这是光栅化泼溅做不到的。
- 内容: NVIDIA 的 3DGRT 用光线追踪而不是光栅化来渲染高斯粒子，使捕捉场景中可以出现反射、折射、阴影以及鱼眼或广角相机。
- 实现方式: 每个高斯被包裹在硬件加速的 BVH 中的包围网格里，沿每条光线按深度顺序分块处理命中。
- 能力维度: 感知真实感
- 论文: https://arxiv.org/abs/2407.07090 (SIGGRAPH Asia 2024 (ACM TOG))
- 视频: https://gaussiantracer.github.io/res/3dgrt_supplementary_video.mp4
- 图片: https://gaussiantracer.github.io/res/method_figure.jpg
- 项目主页: https://gaussiantracer.github.io/
- 代码: https://github.com/nv-tlabs/3dgrut

#### 面向超大数据集的层级 3D 高斯（Hierarchical 3D Gaussians for Very Large Datasets） — Bernhard Kerbl, Inria GraphDeco (2024-06-17)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 多视角拍摄 / 扫描 → 输出: 高斯泼溅 / 辐射场, 三维场景 / 世界
- 核心想法: 说明捕捉的场景可以从一个房间扩展到一个街区，同时保持实时观看。
- 内容: 一种高斯的细节层次结构，使由数万张照片构成的街区级捕捉可以实时渲染，并在移动时平滑地切换细节。
- 实现方式: 场景被切分成独立训练的块，合并成一棵高斯树，渲染时为每个视角选取树上的一个切面。
- 参数: tens of thousands of photos · kilometre-scale trajectories · level of detail
- 能力维度: 情境可达性, 持久性
- 论文: https://arxiv.org/abs/2406.12080 (SIGGRAPH 2024 (ACM TOG))
- 视频: https://www.youtube.com/watch?v=p-mb2TzVJZk
- 项目主页: https://repo-sam.inria.fr/fungraph/hierarchical-3d-gaussians/
- 代码: https://github.com/graphdeco-inria/hierarchical-3d-gaussians

#### 2D 高斯泼溅（2D Gaussian Splatting） — Binbin Huang (2024-03-26)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 多视角拍摄 / 扫描 → 输出: 高斯泼溅 / 辐射场, 网格 / 三维资产
- 核心想法: 让捕捉的场景拥有可以碰撞的几何，这是可交互情境所需要的。
- 内容: 2D 高斯泼溅用有朝向的扁平圆盘替代三维高斯团块，使一次捕捉既能得到照片级视图，也能得到准确的表面和干净的网格。
- 实现方式: 使用光线与面元求交的面元表示，配合深度畸变与法线一致性损失逐场景优化，再用 TSDF 融合提取网格。
- 能力维度: 持久性, 实验控制
- 论文: https://arxiv.org/abs/2403.17888 (SIGGRAPH 2024)
- 视频: https://www.youtube.com/watch?v=oaHCtB6yiKU
- 项目主页: https://surfsplatting.github.io/
- 代码: https://github.com/hbb1/2d-gaussian-splatting

#### SMERF — Daniel Duckworth, 谷歌 DeepMind (2023-12-12)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 多视角拍摄 / 扫描 → 输出: 高斯泼溅 / 辐射场, 三维场景 / 世界
- 核心想法: 说明一个大型捕捉场景无需专用 GPU，也能在浏览器标签页中被探索。
- 内容: SMERF 把房屋大小的辐射场流式加载到网页浏览器，在笔记本和手机上实时渲染，质量接近其所蒸馏自的、较慢的 Zip-NeRF。
- 实现方式: 场景被划分为按相机位置加载的独立 MERF 子模型，通过从 Zip-NeRF 教师模型蒸馏得到。
- 能力维度: 情境可达性, 时间响应性
- 论文: https://arxiv.org/abs/2312.07541 (SIGGRAPH 2024 (ACM TOG))
- 视频: https://www.youtube.com/watch?v=zhO8iUBpnCc
- 图片: https://smerf-3d.github.io/assets/img/merf/social.jpg
- 项目主页: https://smerf-3d.github.io/

#### Mip-Splatting — Zehao Yu (2023-11-27)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 多视角拍摄 / 扫描 → 输出: 高斯泼溅 / 辐射场
- 核心想法: 对头显很重要，因为人在头显里靠近和后退的幅度远大于拍摄相机。
- 内容: Mip-Splatting 消除了高斯泼溅场景在放大或缩小（相对于拍摄尺度）时出现的闪烁与细线伪影。
- 实现方式: 三维平滑滤波器依据训练视角的采样率限制高斯尺寸，二维 Mip 滤波器替代屏幕空间膨胀。
- 能力维度: 感知真实感
- 获奖与认可: CVPR 2024 Best Student Paper
- 论文: https://arxiv.org/abs/2311.16493 (CVPR 2024)
- 视频: https://www.youtube.com/watch?v=D389imzYO04
- 图片: https://niujinshuchong.github.io/mip-splatting/resources/teaser.png
- 项目主页: https://niujinshuchong.github.io/mip-splatting/
- 代码: https://github.com/autonomousvision/mip-splatting

#### 3D 高斯泼溅（3D Gaussian Splatting） — Bernhard Kerbl, Inria GraphDeco (2023-08-08)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 多视角拍摄 / 扫描 → 输出: 高斯泼溅 / 辐射场
- 核心想法: 让照片级的捕捉场景快到足以在头显中使用，而且它的显式基元可以被编辑、流式传输，之后还能随时间运动。
- 内容: 3D 高斯泼溅把拍摄的场景表示为数以百万计的彩色半透明三维高斯，用光栅化而不是光线步进来渲染，以实时帧率得到照片级的新视角。
- 实现方式: 高斯从运动恢复结构得到的点云初始化，通过基于图块的可微光栅化器优化，并自适应地增删高斯。
- 参数: ≥30 fps at 1080p · per-scene training in tens of minutes (paper)
- 能力维度: 感知真实感, 时间响应性, 持久性
- 论文: https://arxiv.org/abs/2308.04079 (SIGGRAPH 2023 (ACM TOG))
- 视频: https://www.youtube.com/watch?v=T_kXY43VZnk
- 项目主页: https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/
- 代码: https://github.com/graphdeco-inria/gaussian-splatting

#### Instant NGP 即时神经图形基元（Instant Neural Graphics Primitives (Instant NeRF)） — Thomas Müller, 英伟达 (2022)
- 类型: 开源工具 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 多视角拍摄 / 扫描 → 输出: 高斯泼溅 / 辐射场
- 核心想法: 让捕捉辐射场的体验更像拍照，而不像跑一个批处理任务。
- 内容: NVIDIA 的 instant-ngp 能在几秒到几分钟内用少量照片训练出 NeRF，并允许在训练过程中就用交互式查看器在结果里穿行。
- 实现方式: 用多分辨率哈希表存储可训练特征向量，替代了大部分多层感知机，并通过完全融合的 CUDA 内核在单张 GPU 上训练与渲染。
- 参数: NeRF training in seconds; 1920×1080 rendering in tens of milliseconds (paper)
- 能力维度: 时间响应性, 创作可及性
- 获奖与认可: SIGGRAPH 2022 Best Paper Award
- 论文: https://arxiv.org/abs/2201.05989 (SIGGRAPH 2022 (ACM TOG))
- 视频: https://www.youtube.com/watch?v=DJ2hcC1orc4
- 图片: https://nvlabs.github.io/instant-ngp/assets/twitter.jpg
- 项目主页: https://nvlabs.github.io/instant-ngp/
- 代码: https://github.com/NVlabs/instant-ngp

#### Mip-NeRF 360 — Jonathan T. Barron, 谷歌 (2022)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 多视角拍摄 / 扫描 → 输出: 高斯泼溅 / 辐射场
- 核心想法: 定义了一次完整绕行拍摄的真实场景应达到的效果，包括远处背景。
- 内容: Mip-NeRF 360 把抗锯齿 NeRF 扩展到绕物体一周拍摄的无界真实场景，并发布了一个九场景数据集，后来成为高斯泼溅方法的标准测试。
- 实现方式: 非线性场景收缩把无界空间映射进有界球体，在线提议网络蒸馏密度以指导采样，畸变正则项抑制漂浮伪影。
- 能力维度: 感知真实感, 情境可达性
- 论文: https://arxiv.org/abs/2111.12077 (CVPR 2022)
- 视频: https://www.youtube.com/watch?v=zBSH-k9GbV4
- 图片: https://jonbarron.info/mipnerf360/img/gardenvase.jpg
- 项目主页: https://jonbarron.info/mipnerf360/
- 代码: https://github.com/google-research/multinerf

#### NeRF 神经辐射场（NeRF） — Ben Mildenhall, Matthew Tancik, Jonathan T. Barron (2020)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 多视角拍摄 / 扫描 → 输出: 高斯泼溅 / 辐射场
- 核心想法: 从这里开始，一组照片变成了可以环顾的地方，代价是每个场景要训练一天、渲染也很慢。
- 内容: 神经辐射场把场景表示为一个小型神经网络：给定任意位置和视角，它返回颜色与密度，因此只需大约一百张照片，就能为拍摄的物体或房间渲染出照片级的新视角。
- 实现方式: 带位置编码的多层感知机把五维坐标映射为辐射与密度，通过可微体渲染与带位姿照片对比，逐场景训练。
- 参数: ~100 posed photos · per-scene training about 1–2 days on one V100 (paper)
- 能力维度: 感知真实感, 持久性
- 获奖与认可: ECCV 2020 Best Paper Honorable Mention
- 论文: https://arxiv.org/abs/2003.08934 (ECCV 2020)
- 视频: https://www.youtube.com/watch?v=JuH79E8rdKc
- 图片: https://cdn.prod.website-files.com/51e0d73d83d06baa7a00000f/5e700ef6067b43821ed52768_pipeline_website-01.png
- 项目主页: https://www.matthewtancik.com/nerf
- 代码: https://github.com/bmild/nerf

### 前馈式重建

一次网络前向就从图像得到几何或高斯泼溅：DUSt3R、VGGT、AnySplat……

#### VGGT-Ω — Jianyuan Wang, Meta (2026-05-14)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像, 视频 → 输出: 三维场景 / 世界, 动态三维 / 4D
- 核心想法: 作者报告重建质量随模型与数据规模可预测地提升，这意味着前馈式三维会像语言模型那样持续进步。
- 内容: VGGT-Ω 是 VGGT 在 2026 年的后续版本：一个更大的前馈式重建模型，同时处理静态与动态场景，另有文本对齐版本和公开的 Hugging Face 演示。
- 实现方式: 简化后的 VGGT：单一多任务稠密预测头、加入寄存器标记、去掉高分辨率卷积层，并借助支持动态场景的标注流程与自监督在更大规模上训练。
- 参数: ~1B parameters · 256–512 px checkpoints · gated weights on Hugging Face
- 能力维度: 时间响应性, 情境多样性
- 论文: https://arxiv.org/abs/2605.15195 (CVPR 2026)
- 视频: https://vggt-omega.github.io/assets/demos/transmission_video.mp4
- 项目主页: https://vggt-omega.github.io/
- 代码: https://github.com/facebookresearch/vggt-omega

#### LingBot-Map 流式三维重建（LingBot-Map） — 蚂蚁灵波科技 (2026-04-15)
- 类型: 模型 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 视频 → 输出: 三维场景 / 世界
- 核心想法: 能跟上行走相机速度的前馈式重建，正是实时映射人周围环境所需要的。
- 内容: LingBot-Map 是蚂蚁集团灵波科技（Robbyant）发布的开源流式三维重建模型，可将实时视频流以约每秒 20 帧的速度转换为相机位姿与点云。
- 实现方式: 几何上下文 Transformer 在注意力中结合锚点上下文、位姿参考窗口与轨迹记忆，在保持流式状态紧凑的同时抑制漂移。
- 参数: ~20 fps at 518×378 (paper)
- 能力维度: 时间响应性, 持久性
- 论文: https://arxiv.org/abs/2604.14141 (arXiv 2026)
- 视频: https://www.youtube.com/watch?v=dChg10XY4aM
- 图片: https://mdn.alipayobjects.com/huamei_u94ywh/afts/img/fkaZRp3UjWwAAAAAgBAAAAgADkxfAQFr/original.png
- 项目主页: https://technology.robbyant.com/lingbot-map
- 代码: https://github.com/Robbyant/lingbot-map

#### Depth Anything 3 — 字节跳动 Seed, Haotong Lin (2025-11-13)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像, 视频 → 输出: 三维场景 / 世界, 高斯泼溅 / 辐射场
- 核心想法: 把单目深度、多视角重建和前馈式泼溅合并到一个开源模型中。
- 内容: 字节跳动 Seed 的 Depth Anything 3 可从一张图像或任意数量的视角预测一致的深度与相机射线，并能输出用于新视角渲染的三维高斯场景。
- 实现方式: 一个普通的 DINOv2 Transformer 加跨视角注意力，预测“深度-射线”表示，在合成与真实数据上以师生方式训练，并附加高斯预测头用于渲染。
- 能力维度: 创作可及性, 情境多样性
- 论文: https://arxiv.org/abs/2511.10647 (arXiv 2025)
- 视频: https://depth-anything-3.github.io/assets/teaser_compress.mp4
- 图片: https://depth-anything-3.github.io/assets/teaser.png
- 项目主页: https://depth-anything-3.github.io/
- 代码: https://github.com/ByteDance-Seed/Depth-Anything-3

#### MapAnything — Nikhil Keetha, Meta (2025-09-16)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像, 多视角拍摄 / 扫描, 镜头路径 / 位姿 → 输出: 三维场景 / 世界
- 核心想法: 公制尺度和可选的传感器输入让重建可测量，当捕捉的房间被用作实验场景时这一点很重要。
- 内容: MapAnything 是 Meta 与卡内基梅隆大学推出的单一模型，可将图像（可选地加上已知内参、位姿或深度）转换为公制尺度的三维几何与相机。
- 实现方式: 多视角 Transformer 使用因式分解的场景表示（逐视角射线方向、沿射线深度、位姿和全局公制尺度），在多种数据集与输入配置上训练。
- 能力维度: 实验控制, 创作可及性
- 论文: https://arxiv.org/abs/2509.13414 (3DV 2026)
- 视频: https://map-anything.github.io/static/MapAnything_Teaser.mp4
- 图片: https://map-anything.github.io/static/MapAnything_Geometric_Inp.png
- 项目主页: https://map-anything.github.io/
- 代码: https://github.com/facebookresearch/map-anything

#### AnySplat — Lihan Jiang (2025-05-29)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像 → 输出: 高斯泼溅 / 辐射场, 三维场景 / 世界
- 核心想法: 去掉了让泼溅捕捉变慢的逐场景训练步骤，使一段走拍几乎可以立刻变得可探索。
- 内容: AnySplat 把一组无位姿、未标定的照片，在几秒的一次前向中变成完整的三维高斯泼溅场景，并同时给出相机位姿。
- 实现方式: 类似 VGGT 的几何 Transformer 预测高斯、内参与外参，可微体素化合并逐像素高斯，并用渲染与蒸馏损失训练。
- 能力维度: 创作可及性, 时间响应性
- 论文: https://arxiv.org/abs/2505.23716 (SIGGRAPH Asia 2025 (ACM TOG))
- 视频: https://city-super.github.io/anysplat/static/videos/teaser_video.mp4
- 图片: https://city-super.github.io/anysplat/static/images/teaser.png
- 项目主页: https://city-super.github.io/anysplat/
- 代码: https://github.com/InternRobotics/AnySplat

#### VGGT — Jianyuan Wang, Meta (2025-03-14)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像, 视频 → 输出: 三维场景 / 世界
- 核心想法: 让一次网络前向成为把照片或视频变成三维场景的默认第一步。
- 内容: VGGT（视觉几何基础 Transformer）输入一张到数百张图像，在约一秒的单次前向中预测出所有相机、深度图、点图和点轨迹。
- 实现方式: 一个 12 亿参数的 Transformer 在 DINO 图块标记上交替进行帧内与全局注意力，并解码出相机、深度、点图与追踪等预测头，在大量三维数据集上训练。
- 参数: 1.2B parameters · up to hundreds of views · under 1 s per scene (paper)
- 能力维度: 时间响应性, 创作可及性
- 获奖与认可: CVPR 2025 Best Paper Award
- 论文: https://arxiv.org/abs/2503.11651 (CVPR 2025)
- 视频: https://vgg-t.github.io/resources/teaser_video_v3_compressed_short.mp4
- 图片: https://vgg-t.github.io/resources/architecture_v4.png
- 项目主页: https://vgg-t.github.io/
- 代码: https://github.com/facebookresearch/vggt

#### CUT3R — Qianqian Wang (2025-01-21)
- 类型: 模型 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 视频, 图像 → 输出: 三维场景 / 世界, 动态三维 / 4D
- 核心想法: 随移动不断累积世界的状态，比批量重建更接近头显感知房间的方式。
- 内容: CUT3R 从图像流在线重建场景：每来一帧就更新一个持续的内部状态，并逐帧输出相机位姿和公制点图，也能处理运动内容。
- 实现方式: 循环 Transformer 让每张图像与一组可学习的状态标记交互并回写，也能从未见过的视角查询该状态。
- 能力维度: 持久性, 时间响应性
- 论文: https://arxiv.org/abs/2501.12387 (CVPR 2025)
- 视频: https://cut3r.github.io/static/videos/cut3r_factory.mp4
- 项目主页: https://cut3r.github.io/
- 代码: https://github.com/CUT3R/CUT3R

#### MASt3R — Vincent Leroy, NAVER LABS Europe (2024-06-14)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像 → 输出: 三维场景 / 世界
- 核心想法: 让点图模型成为 SLAM 与运动恢复结构系统的前端。
- 内容: MASt3R 在 DUSt3R 的基础上加入稠密特征匹配和公制尺度，使图像对能给出可靠的对应关系，用于建图、定位和大规模重建。
- 实现方式: 第二个预测头输出用匹配损失训练的局部描述子，快速互近邻匹配器在公制点图之上寻找对应关系。
- 能力维度: 创作可及性, 实验控制
- 论文: https://arxiv.org/abs/2406.09756 (ECCV 2024)
- 视频: https://www.youtube.com/watch?v=AWu5z2O9H3s
- 图片: https://github.com/naver/mast3r/raw/main/assets/mast3r.jpg
- 项目主页: https://europe.naverlabs.com/blog/mast3r-matching-and-stereo-3d-reconstruction/
- 代码: https://github.com/naver/mast3r

#### DUSt3R — Shuzhe Wang, NAVER LABS Europe (2023-12-21)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像 → 输出: 三维场景 / 世界
- 核心想法: 开启了从脆弱的摄影测量转向“用手头任意照片就能重建”的模型。
- 内容: DUSt3R 输入两张相机未知的照片，直接为每个像素回归一个三维点，于是深度、相机位姿和点云都来自同一个网络，而不再需要运动恢复结构流程。
- 实现方式: 以跨视角补全预训练的 ViT 编码器-解码器，在第一台相机坐标系中输出两张图像的点图；全局对齐步骤合并多个视角。
- 能力维度: 创作可及性, 时间响应性
- 论文: https://arxiv.org/abs/2312.14132 (CVPR 2024)
- 视频: https://www.youtube.com/watch?v=kI7wCEAFFb0
- 图片: https://github.com/naver/dust3r/raw/main/assets/dust3r.jpg
- 项目主页: https://europe.naverlabs.com/research/publications/dust3r-geometric-3d-vision-made-easy/
- 代码: https://github.com/naver/dust3r

#### pixelSplat — David Charatan (2023-12-19)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像 → 输出: 高斯泼溅 / 辐射场
- 核心想法: 早期迹象之一：泼溅场景可以直接由网络输出，而不必经过一次训练。
- 内容: pixelSplat 只用两张照片、一次网络前向就预测出三维高斯场景，无需逐场景优化，并能渲染两者之间的新视角。
- 实现方式: 对极 Transformer 编码图像对，并对逐像素的深度分布进行可微采样来放置高斯。
- 能力维度: 时间响应性, 创作可及性
- 论文: https://arxiv.org/abs/2312.12337 (CVPR 2024)
- 视频: https://davidcharatan.com/pixelsplat/static/videos/teaser.mp4
- 图片: https://pixelsplat.github.io/static/images/banner.png
- 项目主页: https://davidcharatan.com/pixelsplat/
- 代码: https://github.com/dcharatan/pixelsplat

### 动态 4D 场景

在空间与时间上重建的运动场景：4D 高斯、时空泼溅、4D 视频。

#### FreeTimeGS — Yifan Wang, 浙江大学三维视觉组 (2025-06-05)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 多视角拍摄 / 扫描, 视频 → 输出: 动态三维 / 4D, 高斯泼溅 / 辐射场
- 核心想法: 4DV.ai 4D 视频背后的已发表方法，把一篇 CVPR 论文直接连接到一种制作媒介。
- 内容: FreeTimeGS 允许高斯在任意时间、任意位置出现并带有各自的运动，从多相机阵列重建快速复杂的动作，实现实时自由视角回放。
- 实现方式: 每个高斯具有时间中心、基于速度的运动函数与时间不透明度，并通过 4D 正则化避免对单帧过拟合。
- 能力维度: 感知真实感, 时间响应性
- 论文: https://arxiv.org/abs/2506.05348 (CVPR 2025)
- 视频: https://zju3dv.github.io/freetimegs/demo/demo_f1.mp4
- 图片: https://zju3dv.github.io/freetimegs/img/teaser.jpg
- 项目主页: https://zju3dv.github.io/freetimegs/

#### Stereo4D — Linyi Jin, 谷歌 DeepMind (2024-12-12)
- 类型: 数据集 / 基准 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 视频 → 输出: 动态三维 / 4D
- 核心想法: 大规模的真实三维运动，正是让 4D 生成模型生成合理运动所缺少的训练信号。
- 内容: Stereo4D 从互联网 VR180 立体视频中挖掘数据，构建了一个包含真实世界场景及其稠密三维点轨迹（即物体真实运动方式）的大型数据集。
- 实现方式: 把立体深度、相机位姿与二维轨迹融合并过滤为世界坐标系下的三维轨迹，并以此训练 DUSt3R 变体（DynaDUSt3R）来预测运动。
- 能力维度: 情境多样性, 行为似真性
- 论文: https://arxiv.org/abs/2412.09621 (CVPR 2025)
- 视频: https://stereo4d.github.io/static/videos/pipeline/vr180s-v2_compressed.mp4
- 图片: https://stereo4d.github.io/stereo4d_teaser.jpg
- 项目主页: https://stereo4d.github.io/

#### MegaSaM — Zhengqi Li, 谷歌 DeepMind (2024-12-05)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 视频 → 输出: 动态三维 / 4D, 三维场景 / 世界
- 核心想法: 可靠的相机与深度估计，是任何 4D 捕捉或视频转世界流程首先需要的。
- 内容: MegaSaM 能从随手拍摄的动态视频中估计准确的相机路径与一致的深度，包括相机几乎不动的手持素材，而这些正是传统 SLAM 与运动恢复结构失效的地方。
- 实现方式: 将 DROID-SLAM 风格的可微 SLAM 与单目深度先验和考虑不确定性的优化相结合，再细化为一致的视频深度。
- 能力维度: 情境可达性, 实验控制
- 获奖与认可: CVPR 2025 Best Paper Honorable Mention
- 论文: https://arxiv.org/abs/2412.04463 (CVPR 2025)
- 视频: https://www.youtube.com/watch?v=swigYTCdoiw
- 项目主页: https://mega-sam.github.io/
- 代码: https://github.com/mega-sam/mega-sam

#### BTimer — Hanxue Liang, 英伟达 (2024-12-04)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 视频 → 输出: 动态三维 / 4D, 高斯泼溅 / 辐射场
- 核心想法: 把 VGGT 类模型的前馈速度带到运动场景中，并能直接用于生成的视频。
- 内容: NVIDIA 的 BTimer 只需一次前向，就能为单目视频中的任意时刻重建完整的三维高斯快照，为运动场景提供子弹时间视角，也适用于视频生成模型的片段。
- 实现方式: Transformer 输入上下文帧与目标时间戳，输出该时刻的像素对齐高斯，采用静态与动态数据的课程式训练。
- 能力维度: 时间响应性, 创作可及性
- 论文: https://arxiv.org/abs/2412.03526 (arXiv 2024)
- 视频: https://research.nvidia.com/labs/toronto-ai/bullet-timer/davis_results/tennis_demo.mp4
- 图片: https://research.nvidia.com/labs/toronto-ai/bullet-timer/figures/teaser.png
- 项目主页: https://research.nvidia.com/labs/toronto-ai/bullet-timer/

#### MonST3R — Junyi Zhang (2024-10-04)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 视频 → 输出: 动态三维 / 4D, 三维场景 / 世界
- 核心想法: 说明前馈式几何不必假设世界是静止的。
- 内容: MonST3R 把 DUSt3R 式点图扩展到有运动的视频，直接从单目片段估计逐帧几何、相机轨迹与运动物体掩码。
- 实现方式: 在少量合成动态数据集的混合上微调 DUSt3R，使其预测逐时间步点图，再在时间窗口上做轻量的全局优化。
- 能力维度: 时间响应性, 情境可达性
- 论文: https://arxiv.org/abs/2410.03825 (ICLR 2025)
- 视频: https://monst3r-project.github.io/files/teaser_vid_v2_lowres.mp4
- 图片: https://monst3r-project.github.io/files/teaser_monst3r.png
- 项目主页: https://monst3r-project.github.io/
- 代码: https://github.com/Junyi42/monst3r

#### Shape of Motion：单视频 4D 重建（Shape of Motion） — Qianqian Wang (2024-07-18)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 视频 → 输出: 动态三维 / 4D, 高斯泼溅 / 辐射场
- 核心想法: 把 4D 捕捉从相机阵列推向任何人手头已有的素材，同时如实暴露未拍到区域的局限。
- 内容: Shape of Motion 把一段随手拍摄的运动场景手机视频重建为带完整三维轨迹的 4D 高斯，使事件可以从新角度回放。
- 实现方式: 场景运动由一小组共享的 SE(3) 运动基表示，并借助基础模型提供的单目深度与二维轨迹先验进行拟合。
- 能力维度: 情境可达性, 持久性
- 论文: https://arxiv.org/abs/2407.13764 (ICCV 2025)
- 视频: https://shape-of-motion.github.io/static/videos/swing.mp4
- 图片: https://shape-of-motion.github.io/static/images/open_graph.png
- 项目主页: https://shape-of-motion.github.io/
- 代码: https://github.com/vye16/shape-of-motion

#### 时空高斯（Spacetime Gaussians） — Zhan Li (2023-12-28)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 多视角拍摄 / 扫描, 视频 → 输出: 动态三维 / 4D, 高斯泼溅 / 辐射场
- 核心想法: 随时间出现与消失的高斯，比让一组固定高斯变形更能处理火焰、烟雾与遮挡。
- 内容: Spacetime Gaussian Feature Splatting 为每个高斯赋予各自的存续时间、运动与旋转曲线，可实时以极高分辨率回放多视角录制。
- 实现方式: 每个高斯具有时间不透明度、多项式运动与旋转，并结合由小型多层感知机解码的神经泼溅特征，在覆盖不足的区域引导采样新高斯。
- 参数: 8K at 60 fps on RTX 4090, lite model (paper)
- 能力维度: 感知真实感, 时间响应性
- 论文: https://arxiv.org/abs/2312.16812 (CVPR 2024)
- 视频: https://www.youtube.com/watch?v=_7deTUDRlns
- 图片: https://oppo-us-research.github.io/SpacetimeGaussians-website/static/images/methodv2.png
- 项目主页: https://oppo-us-research.github.io/SpacetimeGaussians-website/
- 代码: https://github.com/oppo-us-research/SpacetimeGaussians

#### 4D 高斯泼溅（4DGS）（4D Gaussian Splatting (4DGS)） — 吴官骏 (2023-10-12)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 视频, 多视角拍摄 / 扫描 → 输出: 动态三维 / 4D, 高斯泼溅 / 辐射场
- 核心想法: 把录下来的事件（而不仅是地点）当作观众可以绕着走的东西，这项工作是参照点。
- 内容: 4D 高斯泼溅把运动场景表示为一组三维高斯加上一个学习得到的形变场，使录制的动态场景能以自由视角实时回放。
- 实现方式: HexPlane 时空编码器为一个小型多层感知机提供特征，预测每个时间戳下每个高斯的位置、旋转与尺度偏移。
- 参数: 82 fps at 800×800 on RTX 3090 (paper, synthetic scenes)
- 能力维度: 感知真实感, 时间响应性
- 论文: https://arxiv.org/abs/2310.08528 (CVPR 2024)
- 视频: https://www.youtube.com/watch?v=_wRbq8KnaVg
- 图片: https://guanjunwu.github.io/4dgs/static/images/pipeline_00.jpg
- 项目主页: https://guanjunwu.github.io/4dgs/
- 代码: https://github.com/hustvl/4DGaussians

#### 动态 3D 高斯（Dynamic 3D Gaussians） — Jonathon Luiten (2023-08-18)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 多视角拍摄 / 扫描, 视频 → 输出: 动态三维 / 4D, 高斯泼溅 / 辐射场
- 核心想法: 追踪随重建一起得到，因此捕捉到的运动可以用来驱动其他内容或与之比较。
- 内容: Dynamic 3D Gaussians 把多相机录制的人物抛接、运动等片段重建为随时间移动的高斯，在从新视角渲染的同时，每个点在整段序列中都被追踪。
- 实现方式: 高斯保持颜色、尺寸与不透明度不变，只在每个时间步移动和旋转，并用局部刚性、旋转相似性与等距约束进行正则。
- 参数: 27-camera studio captures · dense 6-DoF tracking
- 能力维度: 持久性, 实验控制
- 论文: https://arxiv.org/abs/2308.09713 (3DV 2024)
- 视频: https://dynamic3dgaussians.github.io/vid_assets/0/juggle.mp4
- 项目主页: https://dynamic3dgaussians.github.io/
- 代码: https://github.com/JonathonLuiten/Dynamic3DGaussians

#### 神经三维视频合成（DyNeRF）（Neural 3D Video Synthesis (DyNeRF)） — Tianye Li, Meta (2021)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 多视角拍摄 / 扫描, 视频 → 输出: 动态三维 / 4D
- 核心想法: 它的多视角厨房录制成了此后所有 4D 高斯方法共用的衡量标准。
- 内容: Meta Reality Labs 的 DyNeRF 把多相机录制的短视频（人在做饭，有火焰与移动的手）重建为辐射场，可以从新的视角、在新的时刻回放。
- 实现方式: 以每帧一个紧凑可学习隐编码为条件的 NeRF，在约 20 台同步相机上用分层关键帧采样与光线重要性采样训练。
- 能力维度: 感知真实感, 实验控制
- 论文: https://arxiv.org/abs/2103.02597 (CVPR 2022)
- 视频: https://neural-3d-video.github.io/resources/video.mp4
- 项目主页: https://neural-3d-video.github.io/
- 代码: https://github.com/facebookresearch/Neural_3D_Video

### 生成式 4D

借助视频先验生成或补全的动态三维内容：DreamGaussian4D、CAT4D、BulletGen、SV4D……

#### 4DNeX — Zhaoxi Chen (2025-08-18)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像 → 输出: 动态三维 / 4D, 平面视频
- 核心想法: 无需逐场景优化的图像到 4D，是通过改造开源视频模型实现的。
- 内容: 4DNeX 只需一次前向，就能从单张图像生成动态三维点云场景，让一张静态照片变成可以从新角度观看的短暂运动场景。
- 实现方式: 微调预训练视频扩散模型，使其联合输出 RGB 与 XYZ 点图序列，在大规模精选 4D 数据集（4DNeX-10M）上训练。
- 能力维度: 创作可及性, 情境多样性
- 论文: https://arxiv.org/abs/2508.13154 (arXiv 2025)
- 视频: https://www.youtube.com/watch?v=jaXNU1-0zgk
- 项目主页: https://4dnex.github.io/
- 代码: https://github.com/3DTopia/4DNeX

#### BulletGen — Denis Rozumny, Jonathon Luiten, Meta (2025-06-23)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 视频 → 输出: 动态三维 / 4D, 高斯泼溅 / 辐射场
- 核心想法: 把生成当作重建中的修补工具：保留拍到的运动，同时填补空缺。
- 内容: Meta 的 BulletGen 在定格的子弹时间时刻生成相机从未看到的视角，并用它们监督重建，从而改进随手单目视频的 4D 高斯重建。
- 实现方式: 在单个定格时间步上，把扩散视频模型与当前 4D 高斯场景对齐，生成的帧作为监督加入迭代优化，同时改善二维/三维追踪。
- 能力维度: 情境可达性, 感知真实感
- 论文: https://arxiv.org/abs/2506.18601 (CVPR 2026 Workshop (4D World Models))
- 图片: https://arxiv.org/html/2506.18601v2/imgs/teaser/skating/v1_our.png https://arxiv.org/html/2506.18601v2/x1.png
- 项目主页: https://arxiv.org/abs/2506.18601

#### SV4D 2.0 — Stability AI (2025-03-20)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 视频 → 输出: 动态三维 / 4D, 平面视频
- 核心想法: 说明开放权重的物体级 4D 路线正走向可用的动画资产。
- 内容: SV4D 2.0 改进了 Stability AI 的视频到 4D 模型，生成的多视角视频更清晰、更一致，在大幅运动下也更稳定，并可被优化为 4D 资产。
- 实现方式: 融合三维注意力与帧注意力且不再依赖参考多视角，使用更多更干净的动画训练数据，并采用由 3D 到 4D 的渐进训练来提升一致性，输出再经两阶段 4D 优化细化。
- 能力维度: 感知真实感, 持久性
- 论文: https://arxiv.org/abs/2503.16396 (arXiv 2025)
- 视频: https://www.youtube.com/watch?v=dtqj-s50ynU
- 项目主页: https://sv4d20.github.io/
- 代码: https://github.com/Stability-AI/generative-models

#### CAT4D — Rundi Wu, 谷歌 DeepMind (2024-11-27)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 视频 → 输出: 动态三维 / 4D, 高斯泼溅 / 辐射场
- 核心想法: 生成补足了单个相机看不到的部分，这正是一段随手视频能变成可漫游时刻的途径。
- 内容: Google DeepMind 的 CAT4D 先用多视角视频扩散模型生成缺失的相机视角，再把单目动态场景视频变成 4D 高斯场景。
- 实现方式: 在静态、动态与合成数据混合上训练的多视角视频扩散模型，可在指定时间采样新视角，交替采样策略保证一致性，然后拟合 4D 高斯。
- 能力维度: 情境可达性, 持久性
- 论文: https://arxiv.org/abs/2411.18613 (CVPR 2025)
- 视频: https://cat-4d.github.io/videos/howitworks_cat4d.mp4
- 图片: https://cat-4d.github.io/img/rep_img.jpg
- 项目主页: https://cat-4d.github.io/

#### Stable Video 4D（SV4D）（Stable Video 4D (SV4D)） — Stability AI (2024-07-24)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 视频 → 输出: 动态三维 / 4D, 平面视频
- 核心想法: 一个开放权重的多视角视频模型，实验室可以本地运行并锁定版本，用于物体级 4D 内容。
- 内容: Stability AI 的 SV4D 输入一段物体视频，生成围绕该物体的、彼此一致的新视角视频，再据此拟合动态三维表示。
- 实现方式: 在 Stable Video Diffusion 上加入视角注意力与帧注意力，联合去噪“视角 × 帧”网格，输出用于监督动态 NeRF。
- 能力维度: 创作可及性, 情境多样性
- 论文: https://arxiv.org/abs/2407.17470 (arXiv 2024)
- 视频: https://www.youtube.com/watch?v=RBP8vdAWTgk
- 项目主页: https://sv4d.github.io/
- 代码: https://github.com/Stability-AI/generative-models

#### L4GM — Jiawei Ren, 英伟达 (2024-06-14)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 视频 → 输出: 动态三维 / 4D, 高斯泼溅 / 辐射场
- 核心想法: 把 4D 物体生成变成一次前向，快到可以嵌入交互式工具之中。
- 内容: NVIDIA 的 L4GM（大型 4D 高斯重建模型）能在约一秒内把物体的单视角视频变成带动画的三维高斯物体。
- 实现方式: 在多视角 LGM 骨干上加入时间自注意力，用 Objaverse 动画物体的渲染数据训练，并配合插帧模型提高帧率。
- 参数: about 1 s per video (paper)
- 能力维度: 时间响应性, 创作可及性
- 论文: https://arxiv.org/abs/2406.10324 (NeurIPS 2024)
- 视频: https://research.nvidia.com/labs/toronto-ai/l4gm/assets/4d_scenes/regular_assets/w_interp_000000.mp4
- 图片: https://research.nvidia.com/labs/toronto-ai/l4gm/assets/figures/framework_largertext.png
- 项目主页: https://research.nvidia.com/labs/toronto-ai/l4gm/
- 代码: https://github.com/nv-tlabs/L4GM-official

#### 4Real — Heng Yu, Snap Inc. (2024-06-11)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 文字提示 → 输出: 动态三维 / 4D, 高斯泼溅 / 辐射场
- 核心想法: 把文本到 4D 从白底上的物体推进到完整场景。
- 内容: Snap Research 与卡内基梅隆大学的 4Real 可根据文字提示生成带背景的照片级动态场景，可从一定角度范围观看，而不是孤立的卡通式物体。
- 实现方式: 文生视频模型先生成参考视频和定格环绕视频，由环绕视频构建标准三维高斯场景，再通过分数蒸馏使其变形以匹配参考视频。
- 能力维度: 感知真实感, 情境多样性
- 论文: https://arxiv.org/abs/2406.07472 (NeurIPS 2024)
- 视频: https://snap-research.github.io/4Real/resources/teaser-1080p.mp4
- 图片: https://snap-research.github.io/4Real/resources/racoon_sync.gif
- 项目主页: https://snap-research.github.io/4Real/

#### DreamGaussian4D — Jiawei Ren (2023-12-28)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像, 视频 → 输出: 动态三维 / 4D, 高斯泼溅 / 辐射场, 网格 / 三维资产
- 核心想法: 把 4D 物体生成缩短到几分钟，并变成游戏引擎能加载的格式。
- 内容: DreamGaussian4D 以参考视频驱动，由单张图像生成的三维高斯物体动起来，并导出为带动画的网格，耗时几分钟而非几小时。
- 实现方式: DreamGaussianHD 生成的静态高斯物体由 HexPlane 形变网络变形，以拟合图生视频得到的驱动片段，再通过视频到视频的纹理优化细化。
- 能力维度: 创作可及性, 时间响应性
- 论文: https://arxiv.org/abs/2312.17142 (arXiv 2023)
- 视频: https://jiawei-ren.github.io/projects/dreamgaussian4d/videos/teaser.mp4
- 项目主页: https://jiawei-ren.github.io/projects/dreamgaussian4d/
- 代码: https://github.com/jiawei-ren/dreamgaussian4d

#### MAV3D 文本生成 4D 动态场景（MAV3D (Make-A-Video3D)） — Uriel Singer, Meta (2023-01-26)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 文字提示, 图像 → 输出: 动态三维 / 4D
- 核心想法: 第一个文本到 4D 系统，确立了“从视频模型借用运动”的范式。
- 内容: Meta 的 MAV3D 仅凭文字提示就能生成短小的动态三维场景（例如可从任意角度观看的动画柯基），方法是蒸馏一个文生视频模型。
- 实现方式: 用 Make-A-Video 的分数蒸馏优化一个 HexPlane 动态 NeRF，采用由静态到动态的训练日程并进行超分辨率微调。
- 能力维度: 创作可及性, 情境多样性
- 论文: https://arxiv.org/abs/2301.11280 (ICML 2023)
- 视频: https://make-a-video3d.github.io/assets/rotating_grid.mp4
- 图片: https://make-a-video3d.github.io/assets/images/teaser.png
- 项目主页: https://make-a-video3d.github.io/

### 体积视频与远程临场

以三维形式捕捉并传输或回放的人：Beam、体积视频工作室、高斯视频。

#### Gracia 体积高斯视频（Gracia） — Gracia (2025)
- 类型: 产品 / 应用 · 时序: 预先生成 · 获取方式: 产品 / 应用
- 输入: 多视角拍摄 / 扫描, 视频 → 输出: 动态三维 / 4D, 高斯泼溅 / 辐射场
- 核心想法: 最早把流式高斯视频送进消费级头显的服务之一（据 Radiancefields.com 报道，2026 年 3 月首次实现 4DGS 流式传输，6 月推出免费的 Apple Vision Pro 应用），因此也能看出文件大小和带宽在哪里限制了可展示的内容。
- 内容: Gracia 把表演者和场景捕捉为 4D 高斯泼溅视频，并流式传输到 Quest、Pico、Apple Vision Pro、桌面和浏览器上的应用中，观众可以绕着录下的时刻走动。
- 实现方式: 多相机捕捉被重建为逐帧泼溅序列，并编码为关键帧加运动增量以便流式传输（据 Radiancefields.com 介绍）；提供 Unity、Unreal 插件与 WebGPU 播放。
- 能力维度: 感知真实感, 情境可达性
- 视频: https://www.youtube.com/watch?v=m3ti-mJu0tI
- 图片: https://gracia.ai/images/open-graph/hub.jpg
- 项目主页: https://gracia.ai/

#### VoluMe — Martin de La Gorce, 微软 (2025-07-28)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入: 视频 → 输出: 虚拟人（脸 / 身体）, 高斯泼溅 / 辐射场
- 核心想法: 无需相机阵列的三维视频通话，代价是看不到的一侧是预测出来的，而不是拍到的。
- 内容: 微软研究院的 VoluMe 把普通单路网络摄像头画面实时转换为人物的三维高斯重建，使常规视频通话可以从略有不同的角度以三维方式观看。
- 实现方式: 网络以输入帧为条件逐帧预测三维高斯，训练目标是使重建与输入视角完全一致并保持时间稳定。
- 能力维度: 时间响应性, 感知真实感
- 论文: https://arxiv.org/abs/2507.21311 (ICCV 2025)
- 视频: https://www.youtube.com/watch?v=xgh46cf4_fw
- 图片: https://www.microsoft.com/en-us/research/wp-content/uploads/2025/07/volume_banner.jpg
- 项目主页: https://www.microsoft.com/en-us/research/publication/volume/

#### 4DV.ai 4D 高斯视频（4DV.ai 4D Gaussian Video） — 4DV.ai (2025-06)
- 类型: 平台 / API · 时序: 预先生成 · 获取方式: 候补 / 抢先体验
- 输入: 多视角拍摄 / 扫描, 视频 → 输出: 动态三维 / 4D, 高斯泼溅 / 辐射场
- 核心想法: 把 4D 视频当作一种独立媒介：录下的事件变成观众可以站在其中的地方，但目前只能在拍摄棚里完成捕捉。
- 内容: 4DV.ai 用多相机阵列录制场景，并转换为 4D 高斯泼溅视频，可在网页、Quest 或 Vision Pro 查看器中播放，观众可以暂停、环绕并在动作中移动；该公司在 SIGGRAPH 2025 Real-Time Live 上做了现场演示，并在 SIGGRAPH 2026 与 Dell、Radiancefields.com 合作首映了一部 11.5 分钟、全部由 4DGS 构成的影片。
- 实现方式: 基于 FreeTimeGS 的研究路线：高斯随时间被连续追踪，而不是逐帧重建，公司称这能减少闪烁并容忍相机不同步。
- 参数: 70-camera 4K PTZ rig shown at NAB 2026 with OBSBOT · 30–60 Mbps finished stream (reported)
- 能力维度: 感知真实感, 情境可达性
- 获奖与认可: SIGGRAPH 2025 Real-Time Live! Best in Show (as reported by Radiancefields.com); Venice Immersive 2026: three 4DGS projects (per 4DV.ai)
- 论文: https://arxiv.org/abs/2506.05348 (CVPR 2025)
- 视频: https://www.youtube.com/watch?v=M01_By5h8lQ
- 图片: https://framerusercontent.com/images/1JJc7VhziLkne1hdBiux2vfYo.webp
- 项目主页: https://www.4dv.ai/viewer/rocket?nowheel

#### Google Beam 三维视频通话（Google Beam） — 谷歌 (2025-05-20)
- 类型: 产品 / 应用 · 时序: 实时流式 · 获取方式: 产品 / 应用
- 输入: 多视角拍摄 / 扫描, 语音与音频, 身体、面部与视线追踪 → 输出: 虚拟人（脸 / 身体）, 动态三维 / 4D
- 核心想法: 体积式远程临场已经是可以买到的产品，但据报道每台约 2.5 万美元，并且只支持一对一通话。
- 内容: Google Beam 是 Project Starline 的商用后继：AI 模型把多路二维相机画面转换为远端人物的三维渲染，在光场显示屏上呈现，内置于 HP Dimension 显示设备出售。
- 实现方式: Google 称其使用六相机阵列与 AI 体积视频模型，在三维光场显示屏上以 60 帧/秒和毫米级头部追踪进行渲染。
- 参数: 6 cameras · 60 fps · 65-inch light-field display (HP Dimension) · 1:1 calls · ~$25,000 per unit (reported)
- 能力维度: 感知真实感, 时间响应性
- 视频: https://www.youtube.com/watch?v=NGPyOHKWLFQ
- 图片: https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Google_Beam_hero.width-1300.png
- 项目主页: https://blog.google/innovation-and-ai/technology/research/google-beam-expansion/
- API 文档: https://beam.google/

#### 时间高斯层级（长时体积视频）（Temporal Gaussian Hierarchy (Long Volumetric Video)） — 徐震, 浙江大学三维视觉组 (2024-12)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 多视角拍摄 / 扫描, 视频 → 输出: 动态三维 / 4D, 高斯泼溅 / 辐射场
- 核心想法: 长度决定了一个片段能否成为让人停留其中的场景；这项工作打破了早期 4D 高斯只能持续几秒的限制。
- 内容: 浙江大学的这一方法把几分钟长的多相机人物录制存为一个跨时间段共享的高斯层级结构，使长时体积视频可以实时回放而不耗尽显存。
- 实现方式: 时间树把每个高斯分配到它所需要的时间段范围：静态区域在长时间段内共享，动态区域使用短暂存在的高斯；外观采用轻量的基于高斯的模型。
- 能力维度: 持久性, 感知真实感
- 论文: https://arxiv.org/abs/2412.09608 (SIGGRAPH Asia 2024 (ACM TOG))
- 视频: https://www.youtube.com/watch?v=y7e0YRNNmXw
- 图片: https://zju3dv.github.io/longvolcap/img/teaser.jpg
- 项目主页: https://zju3dv.github.io/longvolcap/

#### Project Starline — 谷歌 (2021-05-18)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入: 多视角拍摄 / 扫描, 语音与音频, 身体、面部与视线追踪 → 输出: 虚拟人（脸 / 身体）, 动态三维 / 4D
- 核心想法: 真人尺寸的眼神接触与深度线索，并经过用户测试，使它成为远程社交临场感的参照。
- 内容: Google 的 Project Starline 原型是一个通话隔间：两个人隔着光场显示屏交谈，彼此以真人大小的三维形象出现，实时捕捉并传输。
- 实现方式: 多台彩色与深度相机接入实时融合与压缩流程，头部追踪的裸眼立体显示屏配合空间音频渲染远端的人。
- 能力维度: 感知真实感, 时间响应性
- 论文: https://doi.org/10.1145/3478513.3480490 (SIGGRAPH Asia 2021 (ACM TOG))
- 视频: https://www.youtube.com/watch?v=Q13CishCKXY
- 图片: https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Blog_HERO.width-1300.png
- 项目主页: https://blog.google/technology/research/project-starline/

#### HoloSuite 体积视频套件（HoloSuite (HoloEdit / HoloStream)） — Arcturus (2020)
- 类型: 产品 / 应用 · 时序: 预先生成 · 获取方式: 产品 / 应用
- 输入: 多视角拍摄 / 扫描, 视频 → 输出: 动态三维 / 4D, 虚拟人（脸 / 身体）
- 核心想法: 体积捕捉在被放进一段体验之前，需要的正是这样的编辑与交付层。
- 内容: Arcturus HoloSuite 是一套制作工具，用于编辑、压缩体积视频中的人物，并将其流式传输到游戏、AR 与网页播放器中；该公司后来转向基于高斯泼溅的体育赛事回放。
- 实现方式: 对捕捉得到的网格序列进行清理、重定时、重定向（例如头部朝向），并编码为自适应码流，提供 Unity 与 Unreal 插件。
- 能力维度: 创作可及性, 实验控制
- 视频: https://www.youtube.com/watch?v=T0CjAilUtbM
- 项目主页: https://arcturus.studio/

#### 高质量可流式自由视角视频（High-Quality Streamable Free-Viewpoint Video） — Alvaro Collet, 微软 (2015)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 多视角拍摄 / 扫描 → 输出: 动态三维 / 4D, 虚拟人（脸 / 身体）
- 核心想法: 这是高斯视频出现之前的影棚体积视频流程，也是评价高斯视频时的基线。
- 内容: 微软的捕捉舞台系统用一圈同步相机录制表演者，并把他们转换为可流式传输的带纹理三维网格，用于 AR、VR 或电影。
- 实现方式: 多视角 RGB 与红外立体得到点云，再经网格化、为时间一致性进行追踪、纹理映射并压缩以便流式传输。
- 能力维度: 感知真实感, 持久性
- 论文: https://doi.org/10.1145/2766945 (SIGGRAPH 2015 (ACM TOG))
- 视频: https://www.youtube.com/watch?v=_ljYpdGJdoo

### 捕捉应用与泼溅工具

手机与头显捕捉、训练和查看工具：Luma、Polycam、Scaniverse、Postshot、Hyperscape、SuperSplat……

#### Meta Horizon Hyperscape 空间捕捉（Meta Horizon Hyperscape Capture） — Meta (2025-09-17)
- 类型: 产品 / 应用 · 时序: 预先生成 · 获取方式: 产品 / 应用, 候补 / 抢先体验
- 输入: 透视画面与实时环境, 多视角拍摄 / 扫描 → 输出: 高斯泼溅 / 辐射场, 三维场景 / 世界
- 核心想法: 由头显本身完成捕捉，让任何房间都能变成可重返的 VR 场景；但复制品是静态的，处理在 Meta 服务器上进行，而 2026 年移除分享功能也说明测试版平台可能在研究进行中迅速改变。
- 内容: Hyperscape Capture 让 Meta Quest 3 或 3S 用户戴着头显环顾房间几分钟即可完成扫描，随后 Meta 的服务器构建一个照片级的高斯泼溅复制品，可在头显中重新进入。Meta 于 2025 年 11 月 20 日加入链接分享（每个实例最多 8 人），又在 2026 年 5 月 12 日移除了分享功能；如今世界只能在 Capture（Beta）应用中“仅查看”。
- 实现方式: 在一次完成的引导式扫描中由头显相机录制；云端处理（据 Meta 帮助页最长 8 小时）生成高斯泼溅，现由 Capture 应用在设备端渲染。
- 参数: Quest 3 / 3S · scan in minutes · processing up to 8 h (Meta help page)
- 能力维度: 情境可达性, 创作可及性
- 视频: https://www.youtube.com/watch?v=zJ4pjwIPiRk
- 项目主页: https://www.meta.com/help/quest/1088536553019177/

#### Spark — World Labs (2025-06-02)
- 类型: 开源工具 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 场景规格、代码与规则 → 输出: 高斯泼溅 / 辐射场, 三维场景 / 世界
- 核心想法: 让捕捉或生成的泼溅世界可以包上网页交互，这是把它们呈现给研究参与者的最省成本的途径。
- 内容: Spark 是 World Labs 面向 three.js 的开源高斯泼溅渲染器；Spark 2.0（2026 年 4 月）可把超过 1 亿个泼溅的世界流式加载进普通网页。
- 实现方式: 一个 three.js 渲染器，具备 GPU 排序、细节层次与流式加载，并支持可编程的逐泼溅效果用于编辑与动画。
- 参数: 100M+ splats streamed in the browser (Spark 2.0)
- 能力维度: 创作可及性, 情境可达性
- 视频: https://www.youtube.com/watch?v=BpzKZnV0MQc
- 图片: https://sparkjs.dev/static/images/logo-hero.png
- 项目主页: https://sparkjs.dev/
- 代码: https://github.com/sparkjsdev/spark

#### Postshot — Jawset (2024)
- 类型: 产品 / 应用 · 时序: 预先生成 · 获取方式: 产品 / 应用
- 输入: 视频, 多视角拍摄 / 扫描 → 输出: 高斯泼溅 / 辐射场, 三维场景 / 世界
- 核心想法: 本地训练让实验室能掌控数据与版本，这是云端捕捉应用做不到的。
- 内容: Jawset Postshot 是一款 Windows 桌面应用，在本地 NVIDIA GPU 上从视频或照片训练高斯泼溅与辐射场，提供实时预览、编辑以及 After Effects 和 Unreal 插件。
- 实现方式: 相机追踪与泼溅优化都在本地运行，并提供渐进式预览；当前版本线为 v1.1（2026 年 5 月）。
- 能力维度: 创作可及性, 实验控制
- 视频: https://www.youtube.com/watch?v=u-EOH3NRFSU
- 项目主页: https://www.jawset.com/

#### Varjo Teleport（Teleport by Varjo） — Varjo (2024-06-18)
- 类型: 产品 / 应用 · 时序: 预先生成 · 获取方式: 产品 / 应用
- 输入: 视频, 多视角拍摄 / 扫描 → 输出: 高斯泼溅 / 辐射场, 三维场景 / 世界
- 核心想法: 把真实场地的捕捉与专业 XR 培训和可视化连接起来。
- 内容: Teleport 是 Varjo 的云服务，把真实地点的手机扫描或 360° 相机素材转换为高斯泼溅场景，可在网页、VR 头显或游戏引擎中探索。
- 实现方式: 上传的素材在云端重建为泼溅，后续版本加入了大范围捕捉与 360° 视频自动转换。
- 能力维度: 情境可达性, 创作可及性
- 视频: https://www.youtube.com/watch?v=15GCm6NlIj4
- 图片: https://cdn.prod.website-files.com/6708c29d4750b8ec6dcacff9/674083c9edee9798111729ae_Teleport%20OG.png
- 项目主页: https://get.teleport.varjo.com/

#### Scaniverse — Niantic Spatial (2024-03-20)
- 类型: 产品 / 应用 · 时序: 预先生成 · 获取方式: 产品 / 应用
- 输入: 视频, 多视角拍摄 / 扫描 → 输出: 高斯泼溅 / 辐射场
- 核心想法: 在设备端处理让原始素材留在本地，在捕捉真实空间时这可能关系到伦理审查。
- 内容: Scaniverse 直接在手机上训练高斯泼溅，绕物体或地点走一圈，几分钟内就能得到可查看的泼溅，无需上传；2026 年它已成为 Niantic Spatial 捕捉服务的一部分。
- 实现方式: 手机视频与 ARKit/ARCore 位姿输入设备端的高斯优化，扫描结果可共享到 Niantic Spatial 的地图与重建服务。
- 能力维度: 创作可及性, 时间响应性
- 视频: https://www.youtube.com/watch?v=Arrr6ezwJ_4
- 项目主页: https://www.nianticspatial.com/products/capture

#### SuperSplat — PlayCanvas (2023-10)
- 类型: 开源工具 · 时序: 预先生成 · 获取方式: 开源权重 / 代码, 产品 / 应用
- 输入: 多视角拍摄 / 扫描 → 输出: 高斯泼溅 / 辐射场
- 核心想法: 捕捉得到的泼溅通常在这里被清理与分享，因此它是大多数捕捉流程的一部分。
- 内容: SuperSplat 是 PlayCanvas 推出的免费开源浏览器高斯泼溅编辑器及托管网站，用于清理、裁剪、合并和发布泼溅场景；3.0 版（2026 年 9 月）基于 WebGPU 重建。
- 实现方式: 基于 PlayCanvas 引擎的网页应用，用选择工具编辑 PLY/SOG 泼溅，并导出供查看器与引擎使用的压缩格式。
- 能力维度: 创作可及性, 实验控制
- 视频: https://www.youtube.com/watch?v=7B0KdoJCUK8
- 图片: https://superspl.at/header.webp
- 项目主页: https://superspl.at/
- 代码: https://github.com/playcanvas/supersplat

#### Polycam 高斯泼溅（Polycam Gaussian Splatting） — Polycam (2023-09-28)
- 类型: 产品 / 应用 · 时序: 预先生成 · 获取方式: 产品 / 应用
- 输入: 多视角拍摄 / 扫描, 视频 → 输出: 高斯泼溅 / 辐射场, 网格 / 三维资产
- 核心想法: 把泼溅捕捉放进人们已经在用的摄影测量与 LiDAR 扫描应用里。
- 内容: Polycam 是一款广泛使用的手机与网页三维扫描应用，加入了高斯泼溅处理，上传的照片或视频会变成可在浏览器中高帧率观看的泼溅场景。
- 实现方式: 照片或视频在云端处理为三维高斯，同时提供网格与点云输出，支持浏览器内编辑和导出。
- 能力维度: 创作可及性
- 视频: https://www.youtube.com/watch?v=m2j8EF6N2G8
- 项目主页: https://poly.cam/tools/gaussian-splatting

#### Luma 三维捕捉（Luma 3D Capture） — Luma AI (2022)
- 类型: 产品 / 应用 · 时序: 预先生成 · 获取方式: 产品 / 应用
- 输入: 视频, 多视角拍摄 / 扫描 → 输出: 高斯泼溅 / 辐射场, 三维场景 / 世界
- 核心想法: 在大多数人听说 NeRF 之前，就把辐射场捕捉带到了普通手机上。
- 内容: Luma 的手机应用引导用户拍摄物体或地点，并返回 NeRF 结果，后来改为可嵌入网页或导出到游戏引擎的高斯泼溅“交互场景”。
- 实现方式: 引导式拍摄界面采集围绕主体的视频，由云端重建训练 NeRF 或三维高斯场景，并提供网格与 Unreal 等工具的导出。
- 能力维度: 创作可及性
- 视频: https://www.youtube.com/watch?v=JXb_a3ZIGnI
- 项目主页: https://lumalabs.ai/

#### Nerfstudio — Matthew Tancik (2022)
- 类型: 开源工具 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 多视角拍摄 / 扫描, 视频 → 输出: 高斯泼溅 / 辐射场
- 核心想法: 共享、有版本的代码库，让重建中的各种选择可以在不同实验室之间被报告和复现。
- 内容: Nerfstudio 是一个开源框架与网页查看器，可用自己的捕捉数据训练并比较辐射场与高斯泼溅（通过 gsplat）。
- 实现方式: 模块化的 PyTorch 组件（数据解析、采样器、场、渲染器），内置 Nerfacto 与 Splatfacto 方法和浏览器查看器。
- 能力维度: 实验控制, 创作可及性
- 论文: https://arxiv.org/abs/2302.04264 (SIGGRAPH 2023)
- 视频: https://www.youtube.com/watch?v=nSFsugarWzk
- 图片: https://assets.nerf.studio/opg.png
- 项目主页: https://docs.nerf.studio/
- 代码: https://github.com/nerfstudio-project/nerfstudio

## 智能体与模拟社会

由语言模型驱动、在世界中记忆、计划与行动的角色与群体：生成情境里“社会”的一面。

### 生成式智能体与社会模拟

带记忆与反思的可信智能体，从 Smallville 到整个人群的模拟。

#### Simile — Simile, Joon Sung Park (2026-02-12)
- 类型: 平台 / API · 时序: 回合制 · 获取方式: 产品 / 应用
- 输入: 文字提示 → 输出: 对话 / 文本, 智能体行为与动作
- 核心想法: 人群模拟已经成为产品；它的准确性声明，正是行为研究者把这类“数字孪生”当作被试之前必须检验的内容。
- 内容: 一个商业平台，用访谈与问卷数据构建的智能体，模拟真实客户群体对产品发布、价格调整或营销活动的反应，延续斯坦福 1,000 人研究的思路。
- 实现方式: 很可能沿用以访谈为基础人设的生成式智能体架构，并通过比较模拟回答与留出的真人回答分布来验证；Simile 披露了与企业（如 CVS Health）的合作研究，但未公开完整模型细节。
- 能力维度: 情境多样性, 情境可达性, 行为似真性
- 视频: https://www.youtube.com/watch?v=_7FuglsjhbM
- 图片: https://cdn.sanity.io/images/bz52j8pw/production/2b12507f79346d8ce26c4e362188d12e57e13414-1200x630.png?rect=0,2,1200,627&w=1200&h=627&fit=crop&auto=format
- 项目主页: https://www.simile.com/

#### AgentSociety — 清华大学 FIB 实验室 (2025-02-12)
- 类型: 开源工具 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 场景规格、代码与规则, 文字提示 → 输出: 智能体行为与动作, 对话 / 文本
- 核心想法: 把智能体人群当作实验室，先行试验那些在真人身上不道德或无法实施的干预。
- 内容: 一个模拟器：让一万多个 LLM 智能体在建模的城市中拥有工作、住所、出行与社会关系，再在其上开展社会实验，包括极化、煽动性信息传播、全民基本收入与飓风冲击。
- 实现方式: 具备需求、情绪与记忆的 LLM 智能体在城市环境（出行、经济、社交网络）中行动，运行于分布式模拟引擎之上；作者报告约 500 万次智能体之间及与环境的交互，并与真人研究结论对比。
- 参数: 10,000+ agents · ~5 million interactions
- 能力维度: 情境可达性, 实验控制, 情境多样性
- 论文: https://arxiv.org/abs/2502.08691 (arXiv)
- 视频: https://www.youtube.com/watch?v=Oww_rbKvM0U
- 图片: https://opengraph.githubassets.com/2adbf7870edfc463bf6e2fc58ee3d5f0698af94621dca4e2ac4df3208861b60b/tsinghua-fib-lab/AgentSociety
- 项目主页: https://agentsociety.readthedocs.io/
- 代码: https://github.com/tsinghua-fib-lab/AgentSociety

#### OASIS — CAMEL-AI (2024-11-18)
- 类型: 开源工具 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 场景规格、代码与规则 → 输出: 智能体行为与动作, 对话 / 文本
- 核心想法: 可以先在模拟人群中测试推荐算法或谣言会如何改变群体，再考虑在真实用户身上尝试。
- 内容: 一个社交媒体模拟器：多达一百万个 LLM 智能体在带推荐流的类 X、类 Reddit 平台上关注、发帖、评论与转发，用来复现信息扩散、群体极化与从众效应。
- 实现方式: 基于 CAMEL 框架的智能体在动态社交图上通过统一的动作空间行动；环境服务器与基于兴趣或热度的推荐系统决定每个智能体看到的内容，并借助并行的大语言模型推理扩展到超大规模人群。
- 参数: up to 1,000,000 agents
- 能力维度: 情境可达性, 情境多样性, 实验控制
- 论文: https://arxiv.org/abs/2411.11581 (arXiv)
- 视频: https://www.youtube.com/watch?v=wjLHrdZ1Smk
- 图片: https://raw.githubusercontent.com/camel-ai/oasis/main/assets/banner.png
- 项目主页: https://github.com/camel-ai/oasis
- 代码: https://github.com/camel-ai/oasis

#### 1,000 人的生成式智能体模拟（Generative Agent Simulations of 1,000 People） — Joon Sung Park (2024-11-15)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 仅限研究, 开源权重 / 代码
- 输入: 语音与音频, 文字提示 → 输出: 对话 / 文本, 智能体行为与动作
- 核心想法: 以真实个体自己的话（而非人口统计标签）为基础的智能体，能在未见过的问题上替代这个人作答；这是从 Smallville 走向行为研究中参与者“数字孪生”的桥梁。
- 内容: 斯坦福研究者对 1,052 名美国人各做了两小时访谈，把每份访谈记录变成一个智能体，让它像本人一样回答问卷、人格测验与经济博弈。评估标准是参与者本人两周后再次作答的一致性。
- 实现方式: 由 AI 访谈员按 American Voices Project 提纲进行半结构化访谈；将完整访谈记录放入大语言模型上下文，构建每个人的智能体，并在综合社会调查（GSS）题目、大五人格、经济博弈与复现实验上评估，以参与者本人两周重测一致性作归一化。
- 参数: 1,052 participants · 2-hour interviews · 83–86% of test-retest consistency on GSS
- 能力维度: 行为似真性, 实验控制, 情境多样性
- 论文: https://arxiv.org/abs/2411.10109 (arXiv)
- 视频: https://www.youtube.com/watch?v=6EIkeKruJaI
- 图片: https://raw.githubusercontent.com/StanfordHCI/genagents/main/static_dir/cover3.png
- 项目主页: https://arxiv.org/abs/2411.10109
- 代码: https://github.com/StanfordHCI/genagents

#### Project Sid — Altera (Fundamental Research Labs) (2024-10-31)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入:  → 输出: 智能体行为与动作, 对话 / 文本
- 核心想法: 规模改变了问题：数百个智能体共处一个持续世界时，可以观察制度与文化如何形成或瓦解。
- 内容: 多达 1,000 多个 LLM 智能体在同一个 Minecraft 服务器里共同生活数小时：它们自发分工成农民、守卫等角色，投票修改税法，还把一种戏仿宗教在彼此之间传播。
- 实现方式: PIANO 架构让多个模块（记忆、行动、对话、社会感知、目标）并发运行，再由认知控制器实时保持智能体言行一致；以“文明基准”评估社会表现，如分工、规则遵守与文化传播。
- 参数: 10–1,000+ agents · Minecraft
- 能力维度: 行为似真性, 持久性, 情境多样性
- 论文: https://arxiv.org/abs/2411.00114 (arXiv)
- 视频: https://www.youtube.com/watch?v=2tbaCn0Kl90
- 图片: https://raw.githubusercontent.com/altera-al/project-sid/main/visual_abstract.png
- 项目主页: https://github.com/altera-al/project-sid
- 代码: https://github.com/altera-al/project-sid

#### Concordia — 谷歌 DeepMind (2023-12-06)
- 类型: 开源工具 · 时序: 回合制 · 获取方式: 开源权重 / 代码
- 输入: 文字提示, 场景规格、代码与规则 → 输出: 对话 / 文本, 智能体行为与动作
- 核心想法: 把“谁在行动”与“世界判定发生了什么”分开，让社会科学研究者能在一个地方设定、记录和审查模拟情境的规则。
- 内容: 一个开源的 Python 生成式智能体建模库：研究者编写角色与情境，再由一个“游戏主持人”（Game Master）智能体叙述角色行动的后果，类似桌面角色扮演游戏。
- 实现方式: 智能体由可组合的 LLM 组件（记忆、观察、计划、身份）构成；游戏主持人把自由文本行动裁定为基于物理、社会或数字状态的事件；2.0 版重构了组件体系，NeurIPS 2024 的 Concordia Contest 用它研究合作行为。
- 能力维度: 实验控制, 创作可及性, 行为似真性
- 论文: https://arxiv.org/abs/2312.03664 (arXiv)
- 视频: https://www.youtube.com/watch?v=2FO5g65mu2I
- 图片: https://opengraph.githubassets.com/4de00716ff808a0096aa35431807b2a0ef1508212df30727e4812f407badf203/google-deepmind/concordia
- 项目主页: https://github.com/google-deepmind/concordia
- 代码: https://github.com/google-deepmind/concordia

#### AI Town — 安德森·霍洛维茨 (2023-08)
- 类型: 开源工具 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 文字提示 → 输出: 智能体行为与动作, 对话 / 文本
- 核心想法: 把生成式智能体论文变成一个模板，人们可以复刻它来搭建自己的模拟社群与游戏。
- 内容: 一个可部署、MIT 许可的浏览器小镇：LLM 角色四处走动、主动搭话并记住对话；访客也可以作为一个角色加入，与居民聊天。
- 实现方式: 基于 Convex 响应式数据库的 TypeScript 游戏循环保存世界状态、智能体记忆与向量嵌入，并调用托管或本地大语言模型（OpenAI、Together 或 Ollama）生成对话与记忆摘要。
- 能力维度: 创作可及性, 共创与能动性
- 视频: https://www.youtube.com/watch?v=UoJjeyQR66s
- 图片: https://opengraph.githubassets.com/475a5f833a271707e21592833533372def75afb692ea2a116bc756cff677f406/a16z-infra/ai-town
- 项目主页: https://www.convex.dev/ai-town
- 代码: https://github.com/a16z-infra/ai-town

#### 生成式智能体（Smallville 小镇）（Generative Agents (Smallville)） — Joon Sung Park (2023-04-07)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 开源权重 / 代码, 仅限研究
- 输入: 文字提示 → 输出: 智能体行为与动作, 对话 / 文本
- 核心想法: 在大语言模型之上加入记忆、反思与计划，就足以让一个小社会在没有脚本的情况下跨越数天彼此协调。
- 内容: 25 个由大语言模型驱动的角色生活在像素风小镇 Smallville：起床、工作、闲聊、形成看法，并记得彼此。研究者只给一个角色设定“想办情人节派对”的念头，其他角色便自发传播邀请、互相约会，并在约定时间到场。
- 实现方式: 每个智能体保存一条自然语言记忆流；按时间近度、重要性与相关性检索记忆，输入 GPT-3.5 生成反思与分层的日程计划，再由沙盒游戏引擎转化为移动与对话；可信度由人类评估者与消融版本对比打分。
- 参数: 25 agents · 2 game days · GPT-3.5-turbo
- 能力维度: 行为似真性, 持久性, 共创与能动性
- 论文: https://arxiv.org/abs/2304.03442 (UIST 2023)
- 视频: https://www.youtube.com/watch?v=ZdoU9vI2yCg
- 图片: https://raw.githubusercontent.com/joonspk-research/generative_agents/main/cover.png
- 项目主页: https://github.com/joonspk-research/generative_agents
- 代码: https://github.com/joonspk-research/generative_agents

### 在三维世界中行动的智能体

在游戏与生成世界中感知并行动的智能体：Voyager、SIMA、玩游戏的智能体。

#### NitroGen — 英伟达 (2026-01-04)
- 类型: 模型 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 视频 → 输出: 智能体行为与动作
- 核心想法: 互联网游戏视频成为智能体的训练数据，正如它是视频世界模型的训练数据一样。
- 内容: 一个开放的游戏智能体视觉-动作基础模型，在 1,000 多款游戏、共 4 万小时的公开游戏视频上训练，能直接从画面游玩三维动作游戏、二维平台跳跃游戏和程序生成的世界。
- 实现方式: 从游戏视频画面中的手柄输入叠加层自动提取玩家动作，再以大规模行为克隆训练统一的视觉-动作模型；英伟达报告其在未见过的游戏上比从零训练最多提升 52%（相对值）。
- 参数: 40,000 h video · 1,000+ games
- 能力维度: 情境多样性, 反应性
- 论文: https://arxiv.org/abs/2601.02427 (arXiv)
- 视频: https://nitrogen.minedojo.org/assets/videos/banner.mp4
- 图片: https://nitrogen.minedojo.org/assets/images/nitrogen_overview.webp
- 项目主页: https://nitrogen.minedojo.org/
- 代码: https://github.com/MineDojo/NitroGen

#### SIMA 2 — 谷歌 DeepMind (2025-11-13)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 候补 / 抢先体验
- 输入: 文字提示, 图像, 视频 → 输出: 智能体行为与动作, 对话 / 文本
- 核心想法: 首次公开把通用智能体与世界模型配对：Genie 3 生成世界，SIMA 2 在其中行动，并在不需要新人类数据的情况下自我提升。
- 内容: 基于 Gemini 的游戏伙伴：能推理目标、与玩家交谈，理解多种语言的文字、表情符号或图像形式的指令，并把技能带到从未见过的游戏中，包括 Genie 3 即时生成的三维世界。
- 实现方式: 在人类游戏数据与 Gemini 标注数据上微调的 Gemini 基础模型，把屏幕画面与指令映射为键鼠动作；在自我提升循环中，由 Gemini 提出任务并估计奖励，智能体自身的轨迹用于训练下一代版本。
- 能力维度: 反应性, 适应性, 共创与能动性
- 论文: https://arxiv.org/abs/2512.04797 (arXiv)
- 视频: https://www.youtube.com/watch?v=Zphax4f6Rls
- 图片: https://lh3.googleusercontent.com/A5vgACWjzxaEanLkjrZSNlQDjI0SEZ4tKJqE2EtboljSRIkcbEVv4JA2H7a-BEYNoWK097hNdthFdB6h537DUVvFbAUwhWUFSzzA0E0ndr6zMC8tMA=w1200-h630-n-nu-rw
- 项目主页: https://deepmind.google/blog/sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds/

#### Lumine — 字节跳动 Seed, Weihao Tan (2025-11-12)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入: 视频, 文字提示 → 输出: 智能体行为与动作
- 核心想法: 能在商业开放世界中实时、连续游玩数小时，意味着智能体可以在三维世界里成为长期陪伴者或测试玩家。
- 内容: 一个视觉语言智能体，能实时游玩《原神》，以接近人类的效率完成五小时的蒙德主线剧情；无需微调，还能完成《鸣潮》中 100 分钟的任务以及《崩坏：星穹铁道》第一章。
- 实现方式: 一个视觉语言模型按课程式训练：1,731 小时人类游戏录像（动作基元）、200 小时指令跟随数据与 15 小时推理数据，以 5 Hz 读取画面，输出 30 Hz 的键鼠动作块，并只在需要时调用推理。
- 参数: 5 Hz perception · 30 Hz actions · 5-hour storyline
- 能力维度: 反应性, 持久性
- 论文: https://arxiv.org/abs/2511.08892 (arXiv)
- 视频: https://www.youtube.com/watch?v=aNmR8PhN-m8
- 图片: https://img.alicdn.com/imgextra/i4/2042484851/O1CN01jUnyzn1lhoQ0yKvbC_!!2042484851.jpg
- 项目主页: https://www.lumine-ai.org/

#### Game-TARS — 字节跳动 Seed (2025-10-27)
- 类型: 模型 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入: 视频, 文字提示 → 输出: 智能体行为与动作
- 核心想法: 所有游戏共用一个动作空间，让智能体训练可以像语言模型预训练一样扩展。
- 内容: 一个通过原生键鼠输入操控任意游戏的通用游戏智能体；字节跳动称其在开放世界 Minecraft 任务上的成功率约为此前最佳模型的两倍，在未见过的网页三维游戏中接近新手玩家的泛化水平。
- 实现方式: 在操作系统、网页与游戏领域超过 5,000 亿 token 的多模态轨迹上持续预训练，用衰减式持续损失缓解因果混淆，并采用只在关键步骤推理的稀疏思考策略。
- 参数: 500B+ training tokens
- 能力维度: 反应性, 情境多样性
- 论文: https://arxiv.org/abs/2510.23691 (arXiv)
- 视频: https://lf3-static.bytednsdoc.com/obj/eden-cn/eojfrzeh7vhouloj/seed-tars/game-tars-unseen.mp4
- 图片: https://lf3-static.bytednsdoc.com/obj/eden-cn/eojfrzeh7vhouloj/seed-tars/game-tars-hero.png
- 项目主页: https://seed-tars.com/game-tars/

#### SIMA — 谷歌 DeepMind (2024-03-13)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入: 文字提示, 视频 → 输出: 智能体行为与动作
- 核心想法: 采用与人相同的“像素输入、键鼠输出”接口，因此一个智能体无需 API 就能进入任何游戏，包括生成的世界。
- 内容: “可扩展、可指令、多世界”智能体：观看屏幕画面并按键操作，在《无人深空》《英灵神殿》《拆迁》等九款商业游戏和四个研究环境中执行“砍倒那棵树”“打开地图”之类的语言指令。
- 实现方式: 预训练的图像与视频编码器加上文本编码器，输入一个 Transformer 策略，在带指令标注的人类游戏录像上做行为克隆训练；共评估约 600 个时长约 10 秒的基础技能。
- 参数: 9 games + 4 research environments · ~600 skills
- 能力维度: 反应性, 情境多样性
- 论文: https://arxiv.org/abs/2404.10179 (arXiv)
- 视频: https://storage.googleapis.com/gdm-deepmind-com-prod-public/media/media/Compressed-Fig_2_Sima_1.mp4
- 图片: https://lh3.googleusercontent.com/he4kR35RBqPtN9SQ4qMzZjlZJFY9ocs14rJls1ELrNoNoF7MzbF6U-dDBtvNxnI2a6PY_xhHdgQT61BMCpph94Vu4h1mT9fTORPajOwYeS2ypulXSQ=w1200-h630-n-nu-rw
- 项目主页: https://deepmind.google/blog/sima-generalist-ai-agent-for-3d-virtual-environments/

#### Cradle — Weihao Tan, 北京智源人工智能研究院 (2024-03-05)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 开源权重 / 代码
- 输入: 视频, 文字提示 → 输出: 智能体行为与动作
- 核心想法: 证明通用智能体可以通过与玩家相同的屏幕进入商业三维游戏，代价是速度远低于实时。
- 内容: 一个框架，让多模态大语言模型只凭截图和键鼠输出就能完成《荒野大镖客：救赎 2》的主线任务，并可迁移到《星露谷物语》《城市：天际线》和日常软件。
- 实现方式: 由 GPT-4V / GPT-4o 模型循环执行信息收集、自我反思、任务推断、技能整理、动作规划与记忆，编写并复用发出键鼠事件的技能代码。
- 能力维度: 反应性, 适应性
- 论文: https://arxiv.org/abs/2403.03186 (arXiv)
- 视频: https://www.youtube.com/watch?v=ay5gBqzPcDE
- 图片: https://baai-agents.github.io/Cradle/images/cradle-banner.png
- 项目主页: https://baai-agents.github.io/Cradle/
- 代码: https://github.com/BAAI-Agents/Cradle

#### Voyager — Guanzhi Wang, 英伟达 (2023-05-25)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 开源权重 / 代码
- 输入: 文字提示 → 输出: 智能体行为与动作
- 核心想法: 把学到的东西存成代码的智能体，能在开放世界里持续成长；后来的 NPC 与世界智能体系统也沿用了这一模式。
- 内容: 一个无需人工干预、自己玩 Minecraft 的 GPT-4 智能体：它自行提出下一个目标，编写 JavaScript 代码去完成，并把有效代码存为可复用技能，从徒手砍树一路做到挖出钻石。
- 实现方式: 由自动课程、结合环境反馈与执行报错和自我验证的迭代提示循环，以及向量索引的技能库，通过 Mineflayer API 驱动 GPT-4；作者报告获取的独特物品数为此前方法的 3.3 倍，科技树进度最快提升 15.3 倍。
- 能力维度: 适应性, 持久性
- 论文: https://arxiv.org/abs/2305.16291 (arXiv)
- 视频: https://voyager.minedojo.org/assets/videos/gallery/diamond.mp4
- 图片: https://voyager.minedojo.org/assets/images/components.png
- 项目主页: https://voyager.minedojo.org/
- 代码: https://github.com/MineDojo/Voyager

#### XLand：开放式学习智能体（XLand: Open-Ended Learning Agents） — 谷歌 DeepMind (2021)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入:  → 输出: 智能体行为与动作
- 核心想法: SIMA 与“生成世界中的智能体”的先声：通用性来自在生成的情境空间中训练，而不是单一的人工任务。
- 内容: 在 XLand（一个由程序生成的三维世界与多人游戏构成的宇宙）中训练的智能体，学会了尝试、合作、利用物体等通用行为，随后无需再训练就能玩捉迷藏、夺旗等未见过的游戏。
- 实现方式: 采用基于种群的深度强化学习，并以动态课程按每个智能体当前能力生成世界、目标与同伴，在留出的任务上进行零样本评估。
- 能力维度: 情境多样性, 适应性
- 论文: https://arxiv.org/abs/2107.12808 (arXiv)
- 视频: https://www.youtube.com/watch?v=lTmL7jwFfdw
- 项目主页: https://deepmind.google/blog/generally-capable-agents-emerge-from-open-ended-play/

#### 多智能体捉迷藏（Multi-Agent Hide and Seek） — OpenAI (2019)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码, 仅限研究
- 输入:  → 输出: 智能体行为与动作
- 核心想法: “世界中的智能体”的先声：仅靠对抗，就产生了一连串没人设计过的策略。
- 内容: 在三维物理世界中通过强化学习训练的躲藏者与寻找者队伍，在数亿局游戏中自己学会用箱子搭堡垒、用坡道翻墙，甚至利用物理引擎漏洞。
- 实现方式: 在 MuJoCo 环境中，用 PPO 与以实体为中心的注意力策略进行多智能体自我博弈；识别出六个阶段的涌现策略，并与内在动机基线对比。
- 能力维度: 行为似真性, 反应性
- 论文: https://arxiv.org/abs/1909.07528 (ICLR 2020)
- 视频: https://www.youtube.com/watch?v=kopoLzvh5jY
- 项目主页: https://openai.com/index/emergent-tool-use/
- 代码: https://github.com/openai/multi-agent-emergence-environments

### NPC 与角色平台

游戏与 XR 中对话角色的引擎：Inworld、Convai、ACE，以及已上线游戏中的 AI NPC。

#### 《全面战争：法老》AI 顾问（NVIDIA ACE 演示）（Total War: PHARAOH AI advisor (NVIDIA ACE demo)） — 英伟达 (2026-01-05)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 语音与音频, 文字提示 → 输出: 语音 / 声音, 对话 / 文本
- 核心想法: 一个在游戏内辅导玩家的 NPC，这一模式可以直接迁移到训练模拟中的导师角色。
- 内容: CES 2026 上的技术演示：为 Creative Assembly 的策略游戏《全面战争：法老》加入一位会说话的顾问；玩家询问游戏系统和当前战局，顾问用语音回答。
- 实现方式: 英伟达 ACE 在本地 RTX GPU 上运行语音识别、基于游戏数据与当前游戏状态的小语言模型，以及语音合成。
- 能力维度: 适应性, 时间响应性
- 视频: https://www.youtube.com/watch?v=6es-Zvh5bu4
- 图片: https://www.nvidia.com/content/dam/en-zz/Solutions/geforce/news/ces-2026-nvidia-geforce-rtx-announcements/ces-2026-nvidia-geforce-rtx-announcements-ogimage.jpg
- 项目主页: https://www.nvidia.com/en-us/geforce/news/ces-2026-nvidia-geforce-rtx-announcements/

#### Teammates（育碧 AI 队友实验）（Teammates） — 育碧 (2025-11-21)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 候补 / 抢先体验
- 输入: 语音与音频 → 输出: 对话 / 文本, 语音 / 声音, 智能体行为与动作
- 核心想法: 把生成式 NPC 从“聊天”推进到“协同行动”：在实时战斗情境中，自然语音成为指挥队友的操作方式。
- 内容: 一个可游玩的第一人称射击关卡：玩家用语音向两名 AI 队友 Pablo 与 Sofia，以及游戏内助手 Jaspar 下达指令；Jaspar 能标记敌人、讲解背景故事、调整设置或暂停游戏。该实验曾向数百名玩家开放测试。
- 实现方式: 基于育碧 Snowdrop 引擎；语音被转写后，与游戏状态上下文一起交给大语言模型层（据报道为 Google Gemini 与内部中间件）理解，由其选择小队行为并生成配音回复。
- 能力维度: 反应性, 时间响应性, 共创与能动性
- 视频: https://www.youtube.com/watch?v=y6uBzRpqT3w
- 图片: https://staticctf.ubisoft.com/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/5YY8eeQIZh8QolUZwzJOhF/8a826f0cfcca1a41dda148c808096435/Ubisoft_Teammates_XP_Sofia_and_Pablo.jpg
- 项目主页: https://news.ubisoft.com/en-us/article/3mWlITIuWuu0MoVuR6o8ps/ubisoft-reveals-teammates--an-ai-experiment-to-change-the-game

#### Whispers from the Star — Anuttacon (2025-08-14)
- 类型: 产品 / 应用 · 时序: 回合制 · 获取方式: 产品 / 应用
- 输入: 语音与音频, 文字提示 → 输出: 语音 / 声音, 对话 / 文本, 虚拟人（脸 / 身体）
- 核心想法: 一整款商业游戏建立在单个 LLM 角色与开放语音对话之上，检验一段关系能否撑起完整体验。
- 内容: 一款互动科幻故事：玩家通过通讯器与困在外星球的宇航员 Stella 交谈，帮助她活下去；没有对话选项，她接下来做什么取决于玩家说了什么。
- 实现方式: 很可能是专有的大语言模型管线：语音识别、Stella 的人设与剧情状态模型、合成语音以及渲染的角色动画；Anuttacon 未公开技术细节。
- 能力维度: 时间响应性, 共创与能动性, 行为似真性
- 视频: https://www.youtube.com/watch?v=3hnIPdVZK1A
- 图片: https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/3730100/f4c10b5b4ad08b6e879bb53ffa12f5123cca760e/header.jpg?t=1764897761
- 项目主页: https://store.steampowered.com/app/3730100/

#### 《堡垒之夜》AI 达斯·维达（AI Darth Vader in Fortnite） — Epic Games (2025-05-16)
- 类型: 产品 / 应用 · 时序: 回合制 · 获取方式: 产品 / 应用
- 输入: 语音与音频 → 输出: 语音 / 声音, 对话 / 文本, 智能体行为与动作
- 核心想法: 迄今规模最大的授权 LLM 角色公开测试，也清楚表明：角色的声音与人设在上线前必须有护栏。
- 内容: Fortnite 玩家可以招募达斯·维达加入小队，并用麦克风与他交谈；他以合成的 James Earl Jones 声音回答。上线数小时内就有玩家诱导他说脏话，Epic 随即修补。这项技术随后以 Persona 装置开放给创作者，后更名为 Conversations，并于 2026-04-16 作为 UEFN 实验功能推出（尚不能发布作品）。
- 实现方式: 按键说话的语音交给带有维达人设提示的 Google Gemini 2.0 Flash，文字回复再由 ElevenLabs Flash v2.5 以模仿 Jones 的声音合成（Jones 生前于 2022 年把声音权利授予迪士尼）；据报道 Conversations 使用 Gemini 3.1 Flash-Lite 与 ElevenLabs。
- 能力维度: 时间响应性, 反应性, 创作可及性
- 视频: https://www.youtube.com/watch?v=M7spbUI40NQ
- 项目主页: https://www.fortnite.com/news/bring-npcs-to-life-with-ai-powered-conversations

#### 《永劫无间》AI 队友（NARAKA: BLADEPOINT AI Teammate） — 网易游戏, 英伟达 (2025-01-06)
- 类型: 产品 / 应用 · 时序: 实时流式 · 获取方式: 产品 / 应用
- 输入:  → 输出: 智能体行为与动作
- 核心想法: 最早在大型中国动作游戏中上线的 LLM 队友之一，运行在玩家的 GPU 上而不是服务器上。
- 内容: 自 2025 年 3 月 27 日起，网易《永劫无间》手游 PC 版（国服）玩家可以在自由训练中邀请一名本地运行的 AI 队友：它与玩家并肩作战、寻找玩家需要的物品、交换装备，并建议解锁哪些技能。
- 实现方式: 很可能由本地 GeForce RTX GPU 上运行的英伟达 ACE 小语言模型选择高层行动与建议，再由游戏自身的战斗 AI 执行具体操作；网易未公开模型细节。
- 能力维度: 反应性, 适应性
- 视频: https://www.youtube.com/watch?v=I65tiaHQuFk
- 图片: https://www.nvidia.com/content/dam/en-zz/Solutions/geforce/news/nvidia-ace-naraka-bladepoint-inzoi-launch-this-month/nvidia-ace-inzoi-naraka-bladepoint-mobile-pc-version-launch-this-month-ogimage.jpg
- 项目主页: https://www.nvidia.com/en-us/geforce/news/nvidia-ace-naraka-bladepoint-inzoi-launch-this-month/

#### PUBG Ally（AI 队友）（PUBG Ally） — 魁匠团, 英伟达 (2025-01-06)
- 类型: 产品 / 应用 · 时序: 实时流式 · 获取方式: 候补 / 抢先体验
- 输入: 语音与音频 → 输出: 智能体行为与动作, 对话 / 文本, 语音 / 声音
- 核心想法: 一个在快节奏竞技游戏中既能说话又能行动的队友，运行在玩家自己的 GPU 上，而不是云端。
- 内容: 《绝地求生》中可语音交流的 AI 队友：用游戏术语报点、分享物资、驾驶载具并与玩家并肩作战。魁匠团称之为“可共玩角色”（CPC）；在 CES 2025 与 GDC 2026 展示后，计划于 2026 年夏季通过 PUBG 街机模式测试版上线。
- 实现方式: 最初通过英伟达 ACE 使用 Mistral-NeMo-Minitron-8B 小语言模型展示；随后魁匠团从“行为树 + 小模型”的工作流，转向在蒸馏后的本地 Nemotron 模型上运行的自主工具调用智能体循环，并加入长期记忆（CES 2026 宣布）。
- 能力维度: 反应性, 时间响应性, 适应性
- 视频: https://www.youtube.com/watch?v=ukV-ZUJ1mTo
- 图片: https://www.nvidia.com/content/dam/en-zz/Solutions/geforce/news/nvidia-ace-autonomous-ai-companions-pubg-naraka-bladepoint/nvidia-ace-autonomous-ai-companions-ogimage.jpg
- 项目主页: https://www.krafton.ai/blog/pubg_ally_nemotron/

#### inZOI Smart Zoi — 魁匠团, 英伟达 (2025-01-06)
- 类型: 产品 / 应用 · 时序: 实时流式 · 获取方式: 产品 / 应用
- 输入: 文字提示 → 输出: 智能体行为与动作, 对话 / 文本
- 核心想法: 大众市场游戏中整座由 LLM 驱动居民构成的模拟小镇，并在本地运行，接近一个可玩的 Smallville。
- 内容: 在魁匠团的人生模拟游戏 inZOI 中，Smart Zoi 让城市里的每个居民依照自己的人生目标行动、对周围事件作出反应，并根据当天经历调整第二天的日程，而不是等待玩家指令；玩家可以实时查看 Smart Zoi 的内心想法并加以引导。这一实验性设置随游戏于 2025 年 3 月在 Steam 抢先体验上线，需要 GeForce RTX GPU。
- 实现方式: 通过英伟达 ACE 在本地运行的 5 亿参数 Mistral-NeMo-Minitron 小语言模型，依据目标、记忆与反思，从游戏动作集中为每个 Zoi 选择下一步行动，再由游戏模拟系统执行并呈现动画。
- 参数: 0.5B-parameter SLM · on-device · GeForce RTX
- 能力维度: 行为似真性, 情境多样性, 反应性
- 视频: https://www.youtube.com/watch?v=Pk9z1upOj3U
- 图片: https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/2456740/89acee5c3d965af802002617d6c130e5e03bd240/header.jpg?t=1792094410
- 项目主页: https://www.nvidia.com/en-us/geforce/news/nvidia-ace-naraka-bladepoint-inzoi-launch-this-month/

#### Covert Protocol — 英伟达, Inworld AI (2024-03-19)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 语音与音频 → 输出: 对话 / 文本, 语音 / 声音, 虚拟人（脸 / 身体）
- 核心想法: 让对话本身成为玩法：推进剧情靠的是社交能力，而不是对话树选项。
- 内容: GDC 2024 上的技术演示：玩家扮演酒店里的私家侦探，必须通过对话从 AI 驱动的角色口中套出信息；角色透露什么取决于对话走向，因此每次游玩都不同。
- 实现方式: Inworld 角色引擎负责每个角色的人设、目标与知识，英伟达 ACE 提供 Riva 语音识别与 Audio2Face 面部动画；场景基于 Unreal Engine 构建。
- 能力维度: 反应性, 行为似真性
- 视频: https://www.youtube.com/watch?v=uryeFhnNzEs
- 图片: https://www.nvidia.com/content/dam/en-zz/Solutions/geforce/news/nvidia-ace-gdc-gtc-2024-ai-character-game-and-app-demo-videos/nvidia-ace-covert-protocol-ogimage.jpg
- 项目主页: https://www.nvidia.com/en-us/geforce/news/nvidia-ace-gdc-gtc-2024-ai-character-game-and-app-demo-videos/

#### NEO NPC — 育碧, Inworld AI, 英伟达 (2024-03-19)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 语音与音频, 文字提示 → 输出: 对话 / 文本, 语音 / 声音, 虚拟人（脸 / 身体）
- 核心想法: 重新定义了游戏编剧的工作：不再逐句写台词，而是写出“这个人”，再检验模型如何演绎他。
- 内容: 育碧巴黎工作室在 GDC 2024 展示的原型：玩家可以自由说话，与 Bloom、Iron 等角色谈判和制定计划，而角色始终保持叙事总监写下的背景设定。
- 实现方式: Inworld 基于大语言模型的角色引擎依据编写的背景与护栏生成对话，英伟达 Audio2Face 驱动面部动画，演员的表演捕捉决定每个角色的表现幅度。
- 能力维度: 行为似真性, 创作可及性
- 视频: https://www.youtube.com/watch?v=TxrYI6Aoav0
- 图片: https://staticctf.ubisoft.com/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/3NWrkKkT1Bxy1f7VUsyH2q/30eb696cebe4ff5ce9efffd52ec303b1/UN-Ubisoft-New-Generative-AI-Prototype-960x540.jpg
- 项目主页: https://news.ubisoft.com/en-us/article/5qXdxhshJBXoanFZApdG3L/how-ubisofts-new-generative-ai-prototype-changes-the-narrative-for-npcs

#### Convai — Convai (2023)
- 类型: 平台 / API · 时序: 回合制 · 获取方式: 公开 API, 产品 / 应用
- 输入: 语音与音频, 文字提示 → 输出: 对话 / 文本, 语音 / 声音, 智能体行为与动作
- 核心想法: 从一份书面角色设定直达三维或 XR 场景中具身 NPC 的现成路径，无需自建语音与动作管线。
- 内容: 一个用于构建角色的平台：角色能进行语音对话、感知周围环境，并执行取物、引导玩家等动作；提供 Unreal Engine、Unity 与网页三维插件，也用于 VR 训练场景。
- 实现方式: 在网页后台配置角色（背景、知识库、声音、动作）；引擎把语音识别、带动作选择的大语言模型回复、语音合成与口型同步流式传给游戏客户端，并支持 NPC 之间的对话与实时游戏状态上下文。
- 能力维度: 创作可及性, 反应性, 时间响应性
- 视频: https://www.youtube.com/watch?v=q3Th60XdhSs
- 图片: https://cdn.prod.website-files.com/66f6655083b0f778e338eebf/66fba91c8dc2a2d8413cf159_openGraph.jpg
- 项目主页: https://convai.com/
- API 文档: https://docs.convai.com/

#### Suck Up! — Proxima (2023-12)
- 类型: 产品 / 应用 · 时序: 回合制 · 获取方式: 产品 / 应用
- 输入: 语音与音频, 文字提示 → 输出: 对话 / 文本, 语音 / 声音, 智能体行为与动作
- 核心想法: 把说服 LLM 角色作为全部玩法，也展示了玩家如何试探并突破角色提示词。
- 内容: 一款喜剧游戏：玩家扮演吸血鬼，借助伪装和即兴谎言说服由 AI 驱动的镇民开门；每位居民都有自己的性格，并对玩家说的话作出反应。2025 年 10 月登陆 Steam。
- 实现方式: 很可能为每个角色调用云端大语言模型，结合人设提示与游戏状态上下文（伪装、时间、此前的拜访），配合语音输入识别与合成回复；开发者未公开细节。
- 能力维度: 反应性, 共创与能动性
- 视频: https://www.youtube.com/watch?v=JkObwtlXtC4
- 图片: https://cdn.prod.website-files.com/6642c397a9d95685228ac4f3/6644f0c6bc2113e41247eb9e_Suck%20Up!.png
- 项目主页: https://www.playsuckup.com/

#### NVIDIA ACE 游戏演示：Kairos（NVIDIA ACE for Games: Kairos demo） — 英伟达, Convai (2023-05-28)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 语音与音频 → 输出: 对话 / 文本, 语音 / 声音, 虚拟人（脸 / 身体）
- 核心想法: 确立了“语音输入、语音加面部输出”游戏角色模板的演示：语音识别、带人设的大语言模型、语音合成与音频驱动面部动画串成一个循环。
- 内容: 在光线追踪的 Unreal Engine 5 拉面店里，玩家开口与店主 Jin 交谈，他用语音回答并带有口型同步的面部动画，且始终符合自己的背景设定。在 Computex 2023 主题演讲中展示。
- 实现方式: Convai 的角色平台基于英伟达 ACE 模块运行：Riva 语音识别与合成、注入 Jin 背景故事并带护栏的 NeMo 语言模型，以及根据合成语音生成面部动画的 Audio2Face。
- 能力维度: 时间响应性, 感知真实感, 行为似真性
- 视频: https://www.youtube.com/watch?v=5R8xZb6J3r0
- 图片: https://iprsoftwaremedia.com/219/files/20234/646ec444b3aed34ea82f0ed7_nvidia-ace-for-games/nvidia-ace-for-games_b71f46a0-fffd-445d-984b-b531c995ecfb-prv.jpg?v=b71f46a0-fffd-445d-984b-b531c995ecfb
- 项目主页: https://nvidianews.nvidia.com/news/nvidia-ace-for-games-sparks-life-into-virtual-characters-with-generative-ai

## 生成式扩展现实体验

发生在头显与眼镜里的生成：混合现实中的现场共创、实时重绘的现实、生成式电影与演绎，以及 XR 平台已经上线的生成功能。

### MR / VR 中的现场共创

通过说话、草图或手势，把内容放进身边的空间：Editing Reality、LLMR、Social Conjuring……

#### 编辑现实：混合现实中与生成式 AI 的现场共创（Editing Reality） — Suibi Che-Chuan Weng, Ryo Suzuki (2026-06-12)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 语音与音频, 草图与手势, 透视画面与实时环境 → 输出: 网格 / 三维资产, 三维场景 / 世界
- 核心想法: 把生成当作可以在现场一轮轮塑造的材料，而不是在屏幕上敲下的一次性指令。
- 内容: 一个在真实房间里与生成式 AI 共同创作的混合现实系统：通过说话、画草图和直接抓取，人可以就地生成、修改、擦除和重新贴图锚定在身边的虚拟物体与重建物体。
- 实现方式: 设计研究（Research through Design）：结合语音、草图、直接操作与生成式三维和纹理模型迭代开发系统，并通过形成性工作坊与专家评审，提炼现场共创的设计框架。
- 能力维度: 共创与能动性, 创作可及性
- 论文: https://doi.org/10.1145/3800645.3813087 (DIS 2026)
- 视频: https://www.youtube.com/watch?v=PzxpJLmMLwk
- 项目主页: https://ryosuzuki.org/editing-reality

#### Prop-Chromeleon — Haoyu Wang (2026-05-01)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 文字提示, 透视画面与实时环境 → 输出: 网格 / 三维资产
- 核心想法: 把生成约束在真实物体的形状之内，任何家居物品都能成为生成内容的被动触觉道具。
- 内容: 手握一个水瓶，输入“魔法灯笼”，系统就生成一个贴合水瓶形状的虚拟灯笼并锚定在它上面，让你看到的与摸到的一致。
- 实现方式: 生成流程在扫描道具的几何约束下，根据文字提示生成三维资产并锚定在道具上；生成实验评估形状相似度与提示忠实度，用户研究则与静态道具比较真实感和乐趣。
- 能力维度: 感知真实感, 创作可及性
- 论文: https://arxiv.org/abs/2605.00804 (DIS 2026)
- 视频: https://www.youtube.com/watch?v=IKRM-_YxGpM
- 图片: https://arxiv.org/html/2605.00804v2/figures/teaser.png
- 项目主页: https://arxiv.org/abs/2605.00804

#### Vibe Coding XR — Ruofei Du, 谷歌 (2026-03-25)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 开源权重 / 代码, 仅限研究
- 输入: 文字提示 → 输出: 智能体行为与动作, 三维场景 / 世界
- 核心想法: 为语言模型提供描述用户、房间与智能体的精简词汇，让一句话就能产出可运行的 XR 原型。
- 内容: 像“做一朵会对我的手作出反应的蒲公英”这样的提示词，会直接变成一个具备物理效果的混合现实应用，先在桌面的模拟房间里测试，再部署到头显。
- 实现方式: Gemini 基于 XR Blocks 的语义化“现实模型” WebXR API 生成代码；先在桌面模拟现实中循环测试，再部署到头显，并用 60 条提示组成的 VCXR60 与自动评估流程测量一次成功率。
- 参数: VCXR60: 60 prompts
- 能力维度: 创作可及性
- 论文: https://arxiv.org/abs/2603.24591 (arXiv 2026)
- 视频: https://www.youtube.com/watch?v=nknCzIxHHzw
- 图片: https://arxiv.org/html/2603.24591v2/vcxr_samples.png
- 项目主页: https://xrblocks.github.io/
- 代码: https://github.com/google/xrblocks

#### NeXus Print 共创沙盒（NeXus Print） — Ars Electronica Futurelab (2025-09)
- 类型: 体验 / 艺术作品 · 时序: 回合制
- 输入: 文字提示, 草图与手势 → 输出: 网格 / 三维资产, 三维场景 / 世界
- 核心想法: 多人现场生成的公众版、节展规模的实践，被定位为集体头脑风暴与重新构想公共空间的工具。
- 内容: 多人戴上 Meta Quest 3 进入同一个 XR 空间，用简单的文字提示和手势生成三维物体与环境，一起搭建或重新想象一个世界。
- 实现方式: 在共享的 Quest 3 会话中，把手势交互与文字生成三维物体和环境结合起来（与大日本印刷合作开发）。
- 参数: Meta Quest 3 · multi-user
- 能力维度: 共创与能动性, 创作可及性
- 获奖与认可: Open Futurelab, Ars Electronica Festival 2025
- 视频: https://www.youtube.com/watch?v=HH4xfM-XL2Q
- 图片: https://ars.electronica.art/futurelab/files/2025/10/ars-electronica-2025-20cbettinagangl_4932x3288-1-2000x1000.jpg
- 项目主页: https://ars.electronica.art/futurelab/en/nexus-print/

#### 把孩子的画变成可玩的 XR 世界（Drawings into playable XR worlds） — Stijn Spanhove (2025-08-28)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入: 图像, 键盘与手柄动作 → 输出: 交互式帧流
- 核心想法: 动作条件世界模型流式进入 AR 眼镜的早期信号，唯一的创作步骤只是一幅画。
- 内容: 孩子画的一幅画被输入 Mirage 2 世界模型，在 Snap Spectacles 上于观者眼前展开为一个可以玩的世界。
- 实现方式: 概念验证：把画作为起始图像发送给 Dynamics Lab 的 Mirage 2 交互式世界模型，在 Spectacles 上显示生成的帧流，并把输入回传给模型。
- 能力维度: 共创与能动性, 反应性
- 视频: https://x.com/stspanho/status/1961138591934947462
- 项目主页: https://x.com/stspanho/status/1961138591934947462

#### Capybara — Lei Zhang (2025-08-11)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 文字提示, 身体、面部与视线追踪, 透视画面与实时环境 → 输出: 网格 / 三维资产, 动作 / 动画, 智能体行为与动作
- 核心想法: 让孩子成为 AI 驱动 AR 的作者，而不只是观众。
- 内容: 孩子们用文生三维 AI 创造三维角色和配饰，通过自动绑骨和自己的身体动作让它们动起来，再编程设定角色如何回应摄像头识别到的真实物体。
- 实现方式: AR 可视化编程环境结合文生三维、自动绑骨、身体追踪和基于视觉的物体识别（作为可编程触发器）；在美国和阿根廷对 20 名儿童开展用户研究。
- 参数: user studies with 20 children (US, Argentina)
- 能力维度: 创作可及性, 共创与能动性
- 论文: https://arxiv.org/abs/2508.08467 (UIST 2025)
- 视频: https://www.youtube.com/watch?v=paJP8B8btVk
- 图片: https://arxiv.org/html/2508.08467v2/Figures/Teaser_Figure_V20.png
- 项目主页: https://arxiv.org/abs/2508.08467

#### EchoLadder — Zhuangze Hou (2025-08-04)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 语音与音频 → 输出: 三维场景 / 世界
- 核心想法: 把生成拆成可逆、渐进的建议，让人持续掌舵场景，而不是被动接受 AI 的一次性结果。
- 内容: VR 设计者可以用任意抽象程度的口头指令（“更温馨一点”“在沙发旁放盏灯”）提出要求，系统给出具体的场景修改，并可一键应用、重做或撤回。
- 实现方式: 大型视觉语言模型读取当前 VR 场景与口头指令，通过渐进式设计流程给出具体编辑建议；做了消融实验，以及与无建议基线对比的用户研究。
- 能力维度: 创作可及性, 实验控制
- 论文: https://arxiv.org/abs/2508.02173 (UIST 2025)
- 视频: https://www.youtube.com/watch?v=mSZTSsDLjRE
- 图片: https://arxiv.org/html/2508.02173v1/Pic_table/Teaser.png
- 项目主页: https://arxiv.org/abs/2508.02173

#### ImaginateAR — Jaewook Lee, Niantic Spatial (2025-04-30)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 语音与音频, 透视画面与实时环境 → 输出: 网格 / 三维资产, 三维场景 / 世界
- 核心想法: 把对真实地点预先计算的场景理解与快速三维生成结合，让任何人都能在任何地方用说话来创作 AR。
- 内容: 在户外，人说一句“一条在篝火旁享受的龙”，手机 AR 应用就生成三维资产并把它们布置在真实的公园或街道里，之后还可以手动调整。
- 实现方式: 移动 AR 工具结合离线构建的户外场景图、快速文生三维资产流程与基于大语言模型的布局推理；做了技术评估与三阶段用户研究（N=20）。
- 参数: mobile AR · user study N=20
- 能力维度: 创作可及性, 情境可达性
- 论文: https://arxiv.org/abs/2504.21360 (UIST 2025)
- 视频: https://www.youtube.com/watch?v=G9mH1HKSPkg
- 图片: https://nianticspatial.github.io/imaginatear/resources/social_card.png
- 项目主页: https://nianticspatial.github.io/imaginatear/

#### 会说话的日常物件：AI 驱动的 AR 角色（AI-Powered Talking Characters on Everyday Objects） — Nozomu Iwai, Preferred Networks (2025-04-25)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 语音与音频, 透视画面与实时环境 → 输出: 对话 / 文本, 语音 / 声音, 虚拟人（脸 / 身体）
- 核心想法: 把生成角色扎根于真实物体及其周边环境，让对话指向真实存在的东西。
- 内容: 透过 AR 头显或手机，水壶、植物或椅子会长出动画面孔，拥有与自身用途相符的性格，和你聊起这个房间，并在周围发生变化时作出反应。
- 实现方式: 语言、视觉与语音模型为每个识别出的物体赋予性格，并根据其功能与场景变化生成对话；在 HoloLens 2 和安卓手机上做了初步评估。
- 能力维度: 行为似真性, 反应性
- 论文: https://doi.org/10.1145/3706599.3719978 (CHI 2025 Extended Abstracts)
- 视频: https://www.youtube.com/watch?v=RkRc7TRDPDQ
- 项目主页: https://doi.org/10.1145/3706599.3719978

#### Sketch2Terrain — Tianyi Xiao (2025-04-25)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入: 草图与手势 → 输出: 网格 / 三维资产, 三维场景 / 世界
- 核心想法: 从草图实时生成地形，让非专业者能把记忆中的地貌表达出来，也为研究者提供统一的数据采集环境。
- 内容: 人在 AR 中徒手画几笔三维线条，生成模型就实时把它们变成带有山丘与山谷的完整地形。
- 实现方式: 以徒手 AR 笔画为条件，生成式地形模型实时输出高程网格；被试间研究（N=36）将其与传统草图地图比较。
- 参数: between-subjects study N=36
- 能力维度: 创作可及性, 时间响应性, 实验控制
- 论文: https://doi.org/10.1145/3706598.3713467 (CHI 2025)
- 视频: https://www.youtube.com/watch?v=DPvd_EmxzVg
- 项目主页: https://doi.org/10.1145/3706598.3713467

#### Figmin XR 的 AI 创作工具（Figmin XR AI creation tools） — Figmin XR (2024)
- 类型: 产品 / 应用 · 时序: 回合制 · 获取方式: 产品 / 应用
- 输入: 文字提示 → 输出: 网格 / 三维资产, 智能体行为与动作
- 核心想法: 一款消费级头显应用：生成的资产与生成的行为都直接落在你所站立的空间里。
- 内容: 在混合现实创作应用 Figmin XR 中，用户可以通过内置浏览器里的 Luma Genie 用文字生成三维模型并放进房间，后来还能让语言模型编写脚本，让物体变得可交互。
- 实现方式: 把 Luma Genie 的文生三维结果导入为场景物体，并由大语言模型（2025 年包括 GPT-5）基于 Figmin XR 的脚本 API 编写代码。
- 能力维度: 创作可及性
- 视频: https://www.youtube.com/watch?v=PFY1mk4gzjs
- 项目主页: https://figmin.com

#### Dreamcrafter — Cyrus Vachha (2024-10-13)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 语音与音频, 文字提示 → 输出: 高斯泼溅 / 辐射场, 网格 / 三维资产
- 核心想法: 在高延迟生成期间用代理表示顶替，即使模型很慢，沉浸式编辑也能保持流畅。
- 内容: 一个用于捕捉场景（NeRF 与高斯泼溅）的 VR 编辑器：可以用语音或直接操作添加、重绘物体，并在较慢的生成完成前借助快速预览继续工作。
- 实现方式: 模块化 VR 架构接入二维、三维与辐射场编辑等生成模型，混合自然语言与直接操作两种控制方式，并在慢速操作时显示代理表示。
- 能力维度: 创作可及性, 感知真实感
- 论文: https://arxiv.org/abs/2512.20129 (CHI 2025)
- 视频: https://www.youtube.com/watch?v=47r0uMhrokE
- 项目主页: https://dream-crafter.github.io/

#### Thing2Reality — Erzhen Hu, 谷歌 (2024-10-09)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 图像, 视频 → 输出: 高斯泼溅 / 辐射场, 图像 / 全景图
- 核心想法: 把共享的二维内容当场变成三维，让远程讨论具有空间性：人们可以指向物体的某个部位，而不只是一张图。
- 内容: 在 XR 通话中，参与者从视频画面里“抓取”一张二维图片或一个实物，它就在大家之间变成三维物体，可以移动、旋转并指着讨论。
- 实现方式: 把分割出的二维内容先生成条件多视图渲染，再用图像到三维生成得到三维高斯，并在多人 XR 会话中共享；用户研究测量了讨论效率。
- 能力维度: 共创与能动性, 时间响应性
- 论文: https://arxiv.org/abs/2410.07119 (UIST 2025)
- 视频: https://www.youtube.com/watch?v=sKrq77cOtC4
- 图片: https://arxiv.org/html/2410.07119v1/teaserfigure.png
- 项目主页: https://arxiv.org/abs/2410.07119

#### 社交召唤：多人与 AI 实时协作搭建虚拟三维世界（Social Conjuring） — Amina Kobenova, 微软 (2024-09-30)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 文字提示 → 输出: 三维场景 / 世界, 网格 / 三维资产
- 核心想法: 表明“用提示词召唤世界”会变成一种社交行为：生成什么，取决于房间里还有谁。
- 内容: 多人同处一个虚拟世界，在运行中通过向 AI 发出提示共同搭建和修改它；AI 一边放置、调整物体，大家一边交谈并回应彼此的请求。
- 实现方式: Social Conjurer 框架把大语言模型驱动的三维场景生成，与社交互动、工具操作和空间推理结合起来，支持多人实时共创，并通过初步用户研究（N=12）评估。
- 参数: multi-user · preliminary study N=12
- 能力维度: 共创与能动性, 创作可及性
- 论文: https://arxiv.org/abs/2410.00274 (arXiv 2024)
- 图片: https://arxiv.org/html/2410.00274v2/images/teaser.png https://arxiv.org/html/2410.00274v2/images/scene_examples/zoo-cropped.png
- 项目主页: https://arxiv.org/abs/2410.00274

#### SpaceBlender — Nels Numan, 微软 (2024-09-20)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 图像, 文字提示 → 输出: 三维场景 / 世界
- 核心想法: 用每个人的真实环境生成会面空间能带来熟悉感，但生成出的杂乱细节也可能分散对任务的注意。
- 内容: 每位参与者提供自己房间的照片，SpaceBlender 把它们拼接成一个生成的 VR 空间，异地协作者在彼此熟悉的环境中会面。
- 实现方式: 通过深度估计把二维照片抬升为网格，再在几何先验和自适应提示引导下，用扩散模型补全空间、对齐拼接；被试内研究（N=20，两两一组）将其与普通 VR 房间及一个场景生成基线比较。
- 参数: within-subjects study N=20
- 能力维度: 感知真实感, 创作可及性
- 论文: https://arxiv.org/abs/2409.13926 (UIST 2024)
- 视频: https://www.youtube.com/watch?v=2rTTyjNl-a0
- 图片: https://arxiv.org/html/2409.13926v1/fig1-July24.png
- 项目主页: https://arxiv.org/abs/2409.13926

#### VRCopilot — Lei Zhang (2024-08-18)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 语音与音频, 草图与手势 → 输出: 三维场景 / 世界, 网格 / 三维资产
- 核心想法: 发现“搭好脚手架再生成”（人画线框、AI 填充）比完全自动生成更能保住人的能动感。
- 内容: 在 VR 中，人与生成模型一起布置房间：可以边说边指来要家具，也可以先画线框让 AI 填充，或者让它直接排好整个场景。
- 实现方式: 混合主导系统把预训练的三维布局与物体生成模型，与语音加指点的多模态输入和线框中间表示结合；用户研究比较了手动、脚手架式和自动三种创作方式。
- 能力维度: 创作可及性, 共创与能动性
- 论文: https://arxiv.org/abs/2408.09382 (UIST 2024)
- 视频: https://www.youtube.com/watch?v=95xd8oF3Rik
- 图片: https://arxiv.org/html/2408.09382v1/Figures/teaser.png
- 项目主页: https://arxiv.org/abs/2408.09382

#### MagicItem — Ryutaro Kurai (2024-06-19)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 文字提示 → 输出: 智能体行为与动作
- 核心想法: 最早在真实运营的元宇宙中、而非实验室里，由普通用户实际测试的大语言模型行为创作工具之一。
- 内容: 在商业社交 VR 平台 Cluster 中，没有编程基础的用户只需描述物体该做什么，大语言模型就会写出让它照此行动的 Cluster Script。
- 实现方式: 用 Cluster Script API 提示大语言模型，从自然语言生成物体行为，集成进平台后在线上与 63 名普通用户一起评估。
- 参数: online study with 63 platform users
- 能力维度: 创作可及性, 反应性
- 论文: https://arxiv.org/abs/2406.13242 (IEEE Access 2025)
- 视频: https://www.youtube.com/watch?v=ZKf5RkQkV_g
- 图片: https://arxiv.org/html/2406.13242v1/teaser.png
- 项目主页: https://arxiv.org/abs/2406.13242

#### Video2MR — Keiichi Ihara, Ryo Suzuki (2024-05-28)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 视频 → 输出: 动作 / 动画, 虚拟人（脸 / 身体）
- 核心想法: 任何二维视频都能变成可以绕着看的具身示范，是一种低成本的情境化教学来源。
- 内容: 把网上的运动或健身视频变成混合现实教练：视频里的人变成你房间中的三维虚拟人，并带有姿态差异高亮、运动轨迹、速度控制和位置调整。
- 实现方式: 从单目视频中提取三维人体动作，重定向到放置在混合现实中的虚拟人身上，并自动生成可视化增强。
- 能力维度: 情境可达性, 创作可及性
- 论文: https://arxiv.org/abs/2405.18565 (IUI 2025)
- 视频: https://www.youtube.com/watch?v=f1L-2US25PU
- 图片: https://arxiv.org/html/2405.18565v1/figures/teaser.jpg
- 项目主页: https://ryosuzuki.org/video2mr

#### LLMR — Fernanda De La Torre, 微软 (2023-09-21)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 文字提示, 语音与音频 → 输出: 三维场景 / 世界, 智能体行为与动作
- 核心想法: 让沉浸世界的行为（而不只是外观）变成可以用日常语言提出的要求。
- 内容: 输入或说出“用旋转的立方体做一个计时器”或“为色盲用户重新配色”，LLMR 就会编写、检查并运行 Unity 代码，直接改变正在运行的混合现实世界。
- 实现方式: 在 Unity 中编排多个 GPT-4 模块，分别负责场景理解、任务规划、代码生成、自我调试与记忆；作者报告其平均错误率比直接使用 GPT-4 低 4 倍，并做了可用性研究（N=11）。
- 参数: Unity · 4x lower error rate vs GPT-4 (reported) · N=11
- 能力维度: 创作可及性, 反应性
- 论文: https://arxiv.org/abs/2309.12276 (CHI 2024)
- 视频: https://www.youtube.com/watch?v=j44JJtp272k
- 图片: https://arxiv.org/html/2309.12276v3/Figures/Final/teaser.png
- 项目主页: https://arxiv.org/abs/2309.12276

### 实时重绘现实

扩散模型与视频到视频模型，在你观看时重绘透视画面或摄像头画面。

#### Spectacles 上的实时 AI 风格迁移（Real-time AI style transfer on Spectacles） — Alessio Grancini (2026-07-28)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入: 透视画面与实时环境 → 输出: 交互式帧流
- 核心想法: 在透视式眼镜上，重绘需要决定增强什么、在哪里增强，而不只是给整个画面加滤镜。
- 内容: 一项实验把 Snap Spectacles 接入 Decart 的实时视频模型，再把改造后的摄像头画面按真实尺度投回佩戴者视野，让街景实时呈现另一种风格。
- 实现方式: Spectacles 摄像头画面经 WebRTC 发送到 Decart 的实时视频到视频 API，返回的画面在镜头中按真实尺度渲染；这个原型借助智能体编程循环在一天内完成。
- 能力维度: 时间响应性
- 视频: https://x.com/alessiograncini/status/2082150582467387856
- 项目主页: https://x.com/alessiograncini/status/2082150582467387856

#### 身体甲骨文翻译器（Body Oracle Translator） — Danlin Huang, Botao 'Amber' Hu, Reality Design Lab (2026-03)
- 类型: 体验 / 艺术作品 · 时序: 实时流式
- 输入: 身体、面部与视线追踪 → 输出: 图像 / 全景图
- 核心想法: 重绘的对象是人而不是房间：镜头把身体改写成另一种文字，营造一个可以共享的“另类当下”。
- 内容: 透过手持混合现实镜头，人们看到彼此的姿态和动作被实时“翻译”成受甲骨文启发的、由 AI 生成的思辨文字。
- 实现方式: 姿态追踪数据输入一个把身体骨架映射为甲骨文风格字形的图像生成模型（基于 Body Oracle），字形叠加在手持 MR 画面中的人物身上。
- 能力维度: 反应性, 共创与能动性
- 获奖与认可: IEEE VR 2026 XR Gallery
- 视频: https://www.youtube.com/watch?v=GXeLSfZnXAQ
- 项目主页: https://reality.design/project/body-oracle

#### Roomify — Xueyang Wang (2026-03-05)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 文字提示, 透视画面与实时环境 → 输出: 三维场景 / 世界
- 核心想法: 保留房间的功能布局、只改换风格，可以在不丢失空间感知的前提下获得临场感。
- 内容: 把你的真实房间变成主题化的虚拟环境，例如林中小屋或宇宙飞船，其中每张沙发、桌子和每面墙都留在真实的位置，设计者可以在 MR 中编辑、在 VR 中预览。
- 实现方式: 通过现场三维场景理解、AI 空间推理与风格感知生成，把每件陈设替换为几何与功能相匹配的主题对应物；分别对 18 名 VR 用户和 8 名设计专业人员开展研究。
- 参数: presence +63% vs passthrough, +26% vs fully virtual (reported, N=18)
- 能力维度: 感知真实感, 情境多样性
- 论文: https://arxiv.org/abs/2603.04917 (CHI 2026)
- 视频: https://www.youtube.com/watch?v=zPEOMXafHVA
- 图片: https://arxiv.org/html/2603.04917v1/teaser.png
- 项目主页: https://arxiv.org/abs/2603.04917

#### 用实时 AI 视频重绘 XR 房间（Real-time AI video restyling an XR room） — Stijn Spanhove (2025-10-21)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入: 文字提示, 透视画面与实时环境 → 输出: 交互式帧流
- 核心想法: 揭示实时重绘的一条舒适性约束：生成画面的变化必须足够缓慢，才不会与佩戴者的运动冲突。
- 内容: 在 XR 中看到的房间被实时视频模型重绘，先是“现代宜家风格”，再变成“工业风阁楼”；为避免眩晕，画面更新被刻意放慢同步。
- 实现方式: 把渲染出的 XR 画面送入实时视频到视频模型，再以较低的更新频率把重绘结果混合回场景。
- 能力维度: 时间响应性, 情境多样性
- 视频: https://x.com/stspanho/status/1980751025930661934
- 项目主页: https://x.com/stspanho/status/1980751025930661934

#### Decart XR — Decart, Roberto Coviello (2025-10-04)
- 类型: 开源工具 · 时序: 实时流式 · 获取方式: 开源权重 / 代码, 产品 / 应用
- 输入: 语音与音频, 透视画面与实时环境 → 输出: 交互式帧流
- 核心想法: 实时视频到视频模型能把任何房间变成按提示选择的世界，但你看到的东西不再与你摸到的一致。
- 内容: 在 Meta Quest 上，佩戴者说出一个提示，就能看到自己房间的透视画面被实时视频模型当场改造；该应用在 SideQuest 上免费提供，并且开源。
- 实现方式: 通过 QuestCameraKit 获取透视摄像头画面，流式发送到 Decart 的实时视频到视频模型（很可能是经由 WebRTC 的 MirageLSD），再把重绘后的画面渲染回头显。
- 能力维度: 时间响应性, 情境多样性
- 视频: https://x.com/DecartAI/status/1974534910623859128
- 项目主页: https://github.com/DecartAI/Decart-XR
- API 文档: https://decart.ai
- 代码: https://github.com/DecartAI/Decart-XR

#### 混合现实 + 扩散模型透视原型（MR + Diffusion passthrough prototype） — Hugues Bruyère (2025-03-16)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入: 透视画面与实时环境, 文字提示 → 输出: 图像 / 全景图
- 核心想法: Meta 在 2025 年开放透视摄像头 API 之后最早的扩散模型叠加透视演示之一。
- 内容: 一个 Quest 混合现实原型读取透视摄像头画面，用扩散模型生成的图像替换房间的部分区域，佩戴者环顾四周时这些图像保持在原位。
- 实现方式: 把 Meta 透视摄像头 API 获取的画面送入图像扩散模型，再把生成结果重新投射到房间中对应的表面上。
- 能力维度: 时间响应性, 感知真实感
- 视频: https://x.com/smallfly/status/1901403937321750862
- 项目主页: https://x.com/smallfly/status/1901403937321750862

#### Snap 端侧实时生成式 AR 模型（Real-time on-device generative AR model） — Snap Inc. (2024-06-18)
- 类型: 模型 · 时序: 实时流式 · 获取方式: 候补 / 抢先体验
- 输入: 文字提示, 透视画面与实时环境 → 输出: 交互式帧流
- 核心想法: 把对实时摄像头画面的重绘，从云端搬到人手中的设备上。
- 内容: Snap 预览了一个图像扩散模型：小到能在手机上运行、快到能按文字提示实时重绘摄像头画面，用于 AR 镜头，同时发布了 Lens Studio 5.0 的生成工具。
- 实现方式: 一个为端侧推理优化的紧凑型文本条件图像扩散模型实时重绘摄像头画面；Snap 表示使用该模型的镜头会先面向用户上线，之后再开放给创作者。
- 能力维度: 时间响应性, 创作可及性
- 获奖与认可: AWE USA 2024
- 视频: https://www.youtube.com/watch?v=zqHNq2ML_5Q
- 项目主页: https://techcrunch.com/2024/06/18/snap-previews-its-real-time-image-model-that-can-generate-ar-experiences/

#### DreamSpace — Bangbang Yang (2023-10-19)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 文字提示, 多视角拍摄 / 扫描 → 输出: 三维场景 / 世界, 图像 / 全景图
- 核心想法: 重绘的是真实房间的外观而不是替换其几何，生成的世界保留了身体早已熟悉的布局。
- 内容: 输入“梵高”或“赛博朋克”等风格，扫描好的房间就会被整体重新贴图，墙面、地板与家具的纹理彼此连贯，戴上 VR 头显即可走进其中。
- 实现方式: 先从房间中心用由粗到细的扩散模型和双重纹理对齐生成风格化 360° 全景纹理，再通过图像修补和隐式模仿网络，把纹理传播到网格其余部分及被遮挡区域。
- 能力维度: 感知真实感, 情境多样性
- 论文: https://arxiv.org/abs/2310.13119 (IEEE VR 2024)
- 视频: https://www.youtube.com/watch?v=Ni5kXdj7cfw
- 项目主页: https://ybbbbt.com/publication/dreamspace/

### 生成式电影、戏剧与演绎

围绕观众生成或延展的故事、电影与情境。

#### 生成式演绎（Generative Enactments） — Botao 'Amber' Hu, Reality Design Lab (2026)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 文字提示 → 输出: 平面视频
- 核心想法: 借助快速、廉价的视频生成，让人预演那些不安全、不合伦理或尚无法布置的情境，并提供研究者可以设定和比较的配置。
- 内容: 参与者在一个情境中行动，并收到由 AI 生成的第一人称后果视频（短暂等待后返回，或实时流式反应），从而看到情境随自己的行为展开。
- 实现方式: 用一张配置表规定研究者、参与者与 AI 系统如何提出、生成、质疑和修改不同路径；以家用机器人的注意分配（对抗式、回合制）、旁观者干预（选择式）和实习教师后果预演（实时流式）三个案例说明，并报告实现与试用证据。
- 能力维度: 情境可达性, 反应性, 实验控制
- 图片: https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/e24f1e2a-3433-4a17-a6d6-3cdd234543f0/robot-archetype-06-care-or-control/public
- 项目主页: https://amber.botao.hu/project/generative-enactments

#### CinemaWorld：用生成式 AR 延展电影（CinemaWorld） — Keiichi Ihara, Ryo Suzuki (2026-03-09)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 视频, 透视画面与实时环境 → 输出: 三维场景 / 世界
- 核心想法: 无需为每个镜头手工制作 AR，就能把一部固定的电影自动延伸到观者的物理空间。
- 内容: 在播放二维电影的同时，观者在 Meta Quest 3 中看到自己的房间里出现与镜头同步的生成三维内容：粒子特效、环绕物体、纹理覆盖、角色驱动的效果与灯光。
- 实现方式: 先用多模态大语言模型预处理电影、提取关键特征，再用生成式 AI 制作动态三维增强并嵌入房间空间；通过 100 段片段的技术评估、用户研究（N=12）与电影创作者访谈（N=8）评估。
- 参数: Meta Quest 3 · 100 clips · N=12 · 8 experts
- 能力维度: 感知真实感, 创作可及性
- 论文: https://arxiv.org/abs/2603.08060 (UIST 2026)
- 视频: https://ryosuzuki.org/static/video/cinemaworld.mp4
- 图片: https://arxiv.org/html/2603.08060v1/figures/teaser_ver1.1.jpg
- 项目主页: https://ryosuzuki.org/cinemaworld

#### 走进 AI 生成的电影场景（Step inside an AI-generated movie scene） — Stijn Spanhove (2025-12-29)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 视频, 图像 → 输出: 高斯泼溅 / 辐射场, 动作 / 动画
- 核心想法: 完全用现成的生成工具拼出可走进的电影场景，预示电影可以变成可探索的情境。
- 内容: 一个浏览器 WebXR 概念验证（在 Apple Vision Pro 上录制）让观者走进《黑客帝国》的道场，在运动中的生成角色之间瞬移，还能向场景里的 AI 智能体提问。
- 实现方式: 环境由 World Labs 从原片素材生成高斯泼溅，角色用 Tripo 从图像转换为绑骨三维模型，动作来自 AI 动作捕捉，场景里嵌入一个回答问题的 AI 智能体。
- 能力维度: 感知真实感, 创作可及性
- 视频: https://x.com/stspanho/status/2005626245166313514
- 项目主页: https://x.com/stspanho/status/2005626245166313514

#### 人生故事 × World Labs（Life Stories × World Labs） — Liquid City (2025-11)
- 类型: 体验 / 艺术作品 · 时序: 预先生成
- 输入: 语音与音频 → 输出: 高斯泼溅 / 辐射场, 图像 / 全景图
- 核心想法: 一段口述回忆变成可以走进去的地方，这是从口述史通往沉浸情境的一条路径。
- 内容: Liquid City 的 AI 采访者收集一段真实回忆，先把它变成文字描述，再变成图像，最后用 World Labs 的 Marble 生成可漫游的三维高斯泼溅世界，例如《Night Lake》。
- 实现方式: 流程：AI 采访，大语言模型撰写场景描述，图像生成，再用 World Labs Marble 从图像生成高斯泼溅世界。
- 能力维度: 情境可达性, 创作可及性
- 视频: https://www.youtube.com/watch?v=w5fp-otQhQU
- 图片: https://lifestory.liquid.city/img/life-stories-banner.png https://lifestory.liquid.city/img/lifestories-demo.png
- 项目主页: https://lifestory.liquid.city/

#### Storycaster — Naisha Agarwal, 微软 (2025-10-26)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 语音与音频, 透视画面与实时环境 → 输出: 图像 / 全景图, 音效、音乐与空间音频, 对话 / 文本
- 核心想法: 生成式 CAVE 让人在周围故事不断变化时，仍能感知真实房间与彼此。
- 内容: 投影房间变成故事空间：叙述者智能体引导参与者，参与者用语音共同创作场景，墙面投出生成的图像，并配有生成的环境音与对白；房间里的真实物品也能变成故事中的对应物。
- 实现方式: 通过实时摄像头画面与柱面投影增强墙面；图像、音频、对白生成器，对真实物品的物体级编辑，以及大语言模型叙述者共同回应语音指令；对 13 名参与者开展研究。
- 参数: room-scale projection · study n=13
- 能力维度: 共创与能动性, 感知真实感
- 论文: https://arxiv.org/abs/2510.22857 (CHI 2026)
- 视频: https://www.youtube.com/watch?v=ckCtta27LJQ
- 图片: https://arxiv.org/html/2510.22857v2/Figure1.png
- 项目主页: https://arxiv.org/abs/2510.22857

#### 叠加在真实房间里的生成式 AI 地震演练（Generative-AI earthquake rehearsal overlaid on a real room） — Tomoki Itamiya (2025-04-23)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 图像 → 输出: 360° / 立体视频
- 核心想法: 把危险事件“搬进”人们真正需要应对的那个房间，并可调节严重程度、反复回放。
- 内容: 仅凭一张真实房间的照片，生成视频模型就制作出天花板面板掉落的地震情境；视频被转为空间视频，在 Apple Vision Pro 中叠加到同一个房间，并可倒放和慢放。
- 实现方式: 以房间照片做图生视频，调整天花板面板掉落的程度，再转为与实体房间对齐的立体空间视频。
- 能力维度: 情境可达性, 实验控制
- 视频: https://x.com/t_itamiya/status/1914896389152133364
- 项目主页: https://x.com/t_itamiya/status/1914896389152133364

#### Tulpamancer — Light in the Head (2023-08)
- 类型: 体验 / 艺术作品 · 时序: 预先生成
- 输入: 文字提示 → 输出: 三维场景 / 世界, 对话 / 文本
- 核心想法: 根据一个人的回答生成的私人 VR 旅程，只做一次，看完即弃。
- 内容: 观众先在一台旧电脑终端前回答关于自己人生的问题，再戴上 VR 头显，由自己的“图帕”带领穿过专门生成的场景，回望过去、设想未来；每件作品在观看后即被删除。
- 实现方式: 机器学习流程（很可能结合语言与图像生成）在佩戴头显之前，把每位参与者的回答变成一系列虚拟场景与旁白。
- 能力维度: 适应性, 情境多样性
- 获奖与认可: Venice Immersive 2023
- 视频: https://www.youtube.com/watch?v=nBYuZiTI8gA
- 图片: https://static.labiennale.org/files/styles/seo_thumbnail/public/cinema/2023/Schede_film/970x647/Ve_Immersive/dacosta-niederhauser.jpg?itok=FJNGWYE9
- 项目主页: https://www.labiennale.org/en/cinema/2023/venice-immersive/tulpamancer

#### Agence 动态电影（Agence） — Transitional Forms (2020)
- 类型: 体验 / 艺术作品 · 时序: 实时流式
- 输入: 键盘与手柄动作 → 输出: 智能体行为与动作
- 核心想法: 早期先例：故事里的角色是训练出来的智能体而不是动画，所以观众的干预会带来后果。
- 内容: 一部短篇“动态电影”：小星球上的小生物由 AI 智能体驱动；观众可以旁观，也可以伸手改变它们的世界，每次故事走向都不同。
- 实现方式: 角色在游戏引擎构建的电影中实时运行强化学习策略，观众的交互会改变它们的环境（与加拿大国家电影局联合制作）。
- 能力维度: 行为似真性, 共创与能动性
- 获奖与认可: BFI London Film Festival 2020
- 视频: https://vimeo.com/426287032
- 项目主页: https://www.transforms.ai/agence

### XR 平台中的生成功能

头显与眼镜已经推出的功能：空间场景、空间捕捉、生成式镜头、AI 世界编辑器。

#### Android XR 自动空间化（Android XR auto-spatialization） — 谷歌, 三星 (2026-04-07)
- 类型: 产品 / 应用 · 时序: 实时流式 · 获取方式: 产品 / 应用
- 输入: 视频, 图像 → 输出: 360° / 立体视频, 图像 / 全景图
- 核心想法: 系统级的二维转三维意味着，任何平面内容在头显里都能成为立体内容，靠的是生成而不是拍摄。
- 内容: Android XR 在三星 Galaxy XR 头显上推出的实验功能：一键把几乎任何应用、游戏、网站、图像或视频（包括 YouTube 视频和二维游戏）变成三维体验。
- 实现方式: 很可能是在系统合成器层面对每帧做单目深度估计并合成立体视图；在“设置”的 Labs 页面中开启。
- 能力维度: 感知真实感
- 视频: https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/Auto_Spatialization.mp4
- 图片: https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Final_Hero_Image.width-1300.png
- 项目主页: https://blog.google/products-and-platforms/platforms/android/android-xr-immersive-features-update-april-2026/

#### XR Blocks — 谷歌 (2025-09-29)
- 类型: 开源工具 · 时序: 回合制 · 获取方式: 开源权重 / 代码
- 输入: 文字提示, 语音与音频, 透视画面与实时环境 → 输出: 智能体行为与动作
- 核心想法: 降低把感知、渲染与生成模型连在一起的成本，而这正是大多数 AI + XR 原型卡住的环节。
- 内容: 谷歌开源的 WebXR 框架，提供用户、世界、同伴、界面、上下文与智能体等即插即用模块，让 AI + XR 原型（Gemini 助手、场景理解）可以在 Chrome 和 Android XR 头显上运行。
- 实现方式: 基于 WebXR、three.js、TensorFlow 与 Gemini 的模块化架构，附带模板、示例与演示，也是 Vibe Coding XR 的基础。
- 能力维度: 创作可及性, 实验控制
- 论文: https://arxiv.org/abs/2509.25504 (arXiv 2025)
- 视频: https://www.youtube.com/watch?v=75QJHTsAoB8
- 图片: https://arxiv.org/html/2509.25504v1/teaser.png
- 项目主页: https://xrblocks.github.io/
- API 文档: https://xrblocks.github.io/docs/
- 代码: https://github.com/google/xrblocks

#### Meta Horizon Studio 生成式 AI 工具（Meta Horizon Studio generative AI tools） — Meta (2025-09-17)
- 类型: 平台 / API · 时序: 回合制 · 获取方式: 产品 / 应用, 候补 / 抢先体验
- 输入: 文字提示 → 输出: 网格 / 三维资产, 图像 / 全景图, 音效、音乐与空间音频
- 核心想法: 把“提示生成资产”和“提示生成代码”放进一个大型社交 VR 平台的主要创作工具中。
- 内容: Meta 面向 Horizon 的世界搭建编辑器，让创作者在全新的 Horizon Engine 之上，用文字提示生成网格、纹理、TypeScript、音频和天空盒，并宣布将推出串联这些工具的智能体助手。
- 实现方式: 把文生三维、纹理、代码、音频与天空盒生成器集成进编辑器，由 Horizon Engine 渲染结果；2026 年 9 月，Meta 把 Horizon Studio 调整为在浏览器中以智能体方式创作手机游戏的工具，处于抢先体验阶段。
- 能力维度: 创作可及性
- 视频: https://www.youtube.com/watch?v=viXoK-MJRls
- 项目主页: https://www.meta.com/blog/connect-2025-day-one-keynote-ai-glasses-ray-ban-display-neural-band-metaverse-news/
- API 文档: https://developers.meta.com/horizon-worlds/

#### Spectacles AI 更新与 Snap3D（Spectacles AI release with Snap3D） — Snap Inc. (2025-06-10)
- 类型: 平台 / API · 时序: 回合制 · 获取方式: 公开 API, 产品 / 应用
- 输入: 文字提示, 语音与音频 → 输出: 网格 / 三维资产
- 核心想法: 让文生三维成为 AR 眼镜应用的标准构件，镜头可以生成开发者从未建模过的物体。
- 内容: Spectacles 系统更新加入 Snap3D API，可在镜头内按需生成三维物体，同时接入 OpenAI 与 Gemini，并改进语音识别，用于多模态 AI 镜头。
- 实现方式: 把云端文生三维作为 Lens Studio API 提供，在 Spectacles 镜头运行时调用，并配合托管的大语言模型与语音识别服务。
- 能力维度: 创作可及性
- 视频: https://www.youtube.com/watch?v=qpi1JTnPwgs
- 项目主页: https://investor.snap.com/news/news-details/2025/Snap-to-Launch-New-Lightweight-Immersive-Specs-in-2026/default.aspx
- API 文档: https://developers.snap.com/spectacles

#### visionOS 2：二维照片转空间照片（visionOS 2 spatial photos from 2D images） — 苹果 (2024-06-10)
- 类型: 产品 / 应用 · 时序: 回合制 · 获取方式: 产品 / 应用
- 输入: 图像 → 输出: 图像 / 全景图
- 核心想法: 让生成的深度成为在头显中重温个人回忆的默认方式；visionOS 26 随后把它扩展为“空间场景”。
- 内容: 在 visionOS 2 中，Apple Vision Pro 用户可以把图库里的任意二维照片转成带深度的空间照片，在头显中鲜活呈现。
- 实现方式: Apple 表示 visionOS 用先进的机器学习把二维图像转化为立体空间照片，做法很可能是单目深度估计加带修补的视图合成。
- 能力维度: 感知真实感
- 视频: https://www.apple.com/newsroom/videos/videos-2024/autoplay/2024/visionos-2-spatial-photos/large_2x.mp4
- 图片: https://www.apple.com/newsroom/images/2024/06/visionos-2-brings-new-spatial-computing-experiences-to-apple-vision-pro/tile/Apple-WWDC24-visionOS-2-spatial-photos-240610-lp.jpg.og.jpg?202608191902
- 项目主页: https://www.apple.com/newsroom/2024/06/visionos-2-brings-new-spatial-computing-experiences-to-apple-vision-pro/

## 沉浸式行为研究与训练

这些情境被用在哪里：社会心理学与犯罪学中的 VR 实验、有虚拟人和虚拟病人参与的模拟训练、临床 VR、临场感理论，以及首批把生成式 AI 带入沉浸式研究的工作。

### 临场感、似真性与方法论

人为何会对虚拟情境作出反应，以及如何设计与验证这些情境：Slater、Steuer、Blascovich、Brunswik……

#### 把虚拟现实误当作现实：一项实验研究（Confusing virtual reality with reality – An experimental study） — Michael Wiesing, Mel Slater (2025-05-13)
- 类型: 行为研究 · 时序: 脚本 / 规则驱动
- 输入: 身体、面部与视线追踪, 语音与音频 → 输出: 人工制作的 VR 情境, 虚拟人（脸 / 身体）
- 核心想法: 当虚拟情境与物理现实高度吻合时，人们会把虚拟中的“事实”带回现实世界；随着生成世界越来越照片级逼真，这一安全与伦理问题会愈发突出。
- 内容: 49 名参与者在一间真实房间的虚拟副本中与一位虚拟实验员互动。20% 的人没有确认现实中是否有椅子就坐了下去；一周后在真实房间里，45% 的人以为虚拟实验员放进抽屉的平板电脑就在那里。
- 实现方式: 以虚拟实验员开展实验，结合行为指标（是否坐下、一周后对物品位置的预期）与内隐态度测验，并用贝叶斯统计分析。
- 参数: N=49 · follow-up after 1 week
- 能力维度: 感知真实感, 行为似真性
- 论文: https://doi.org/10.1016/j.isci.2025.112655 (iScience (2025))
- 视频: https://www.youtube.com/watch?v=pM279hO8n5s

#### 沉浸式学习的认知情感模型（CAMIL）（The Cognitive Affective Model of Immersive Learning (CAMIL): a Theoretical Research-Based Model of Learning in Immersive Virtual Reality） — Guido Makransky (2021)
- 类型: 论文 / 综述
- 输入: 身体、面部与视线追踪, 键盘与手柄动作 → 输出: 人工制作的 VR 情境
- 核心想法: 临场感更强并不自动意味着学得更好：生成的训练情境只有当其真实感与交互性服务于学习目标、而非让学习者超载时才有帮助。
- 内容: 解释沉浸式 VR 学习的理论模型：临场感与能动性两种特性，通过兴趣、自我效能、具身化、认知负荷等六个情感与认知因素影响学习。
- 实现方式: Makransky 与 Petersen 把沉浸式学习的实证研究整合为一个可检验的因果模型。
- 能力维度: 感知真实感, 共创与能动性
- 论文: https://doi.org/10.1007/s10648-020-09586-2 (Educational Psychology Review 33 (2021))

#### 为何以及如何用虚拟现实研究人类社会互动：探索新研究版图的挑战（Why and how to use virtual reality to study human social interaction: The challenges of exploring a new research landscape） — Sylvia Xueni Pan (2018)
- 类型: 论文 / 综述
- 输入: 身体、面部与视线追踪, 语音与音频 → 输出: 人工制作的 VR 情境, 虚拟人（脸 / 身体）
- 核心想法: 虚拟互动对象以牺牲双向真实感为代价，换来精确、可重复的社会刺激；这正是由大语言模型驱动的角色如今试图弥合的缺口。
- 内容: 发表于 British Journal of Psychology 的综述，讨论如何用 VR 研究面对面的社会互动：虚拟角色让研究者能控制什么，以及当互动对象不是真人时会失去什么。
- 实现方式: 与 Antonia Hamilton 合作的叙述性综述，涵盖 VR 社会互动范式中的角色真实感、互动回路与效度问题。
- 能力维度: 实验控制, 行为似真性
- 论文: https://doi.org/10.1111/bjop.12290 (British Journal of Psychology (2018))
- 视频: https://www.youtube.com/watch?v=rh6e-mW_y5E

#### 用沉浸式虚拟现实改善我们的生活（Enhancing Our Lives with Immersive Virtual Reality） — Mel Slater (2016)
- 类型: 论文 / 综述
- 输入: 身体、面部与视线追踪 → 输出: 人工制作的 VR 情境, 虚拟人（脸 / 身体）
- 核心想法: VR 的价值在于现实中不可能、危险或不合伦理的情境——包括进入另一具身体——而生成技术可能大幅降低构建这些情境的成本。
- 内容: 发表于 Frontiers in Robotics and AI 的长篇综述，回顾沉浸式 VR 在神经科学、心理学、临床治疗、训练、教育与娱乐中的应用，概括其独特能力，并提出伦理上的提醒。
- 实现方式: 与 Maria V. Sanchez-Vives 合作的叙述性综述，围绕临场感、身体拥有感与应用领域展开。
- 能力维度: 情境可达性, 感知真实感
- 论文: https://doi.org/10.3389/frobt.2016.00074 (Frontiers in Robotics and AI 3 (2016))

#### 地点错觉与似真错觉可在沉浸式虚拟环境中引发真实行为（Place illusion and plausibility can lead to realistic behaviour in immersive virtual environments） — Mel Slater (2009)
- 类型: 论文 / 综述
- 输入: 身体、面部与视线追踪 → 输出: 人工制作的 VR 情境
- 核心想法: 渲染质量换来地点错觉；似真错觉则来自会回应你且可信的事件——这正是生成式智能体与世界模型必须提供的。
- 内容: 理论论文，把临场感拆分为“地点错觉”（身处其中之感，由感觉运动的一致性决定）与“似真错觉”（觉得正在发生的事是真的），并论证二者结合才会引发真实的行为反应。
- 实现方式: 基于以往临场感实验的概念分析，把“沉浸”定义为系统所支持的有效感觉运动动作的集合。
- 能力维度: 感知真实感, 行为似真性
- 论文: https://doi.org/10.1098/rstb.2009.0138 (Philosophical Transactions of the Royal Society B (2009))
- 视频: https://www.youtube.com/watch?v=WSLyfBscA9E

#### 沉浸式虚拟环境技术：社会心理学的方法论工具（Immersive Virtual Environment Technology as a Methodological Tool for Social Psychology） — Jim Blascovich (2002)
- 类型: 论文 / 综述
- 输入: 身体、面部与视线追踪 → 输出: 人工制作的 VR 情境, 虚拟人（脸 / 身体）
- 核心想法: 这一领域的奠基主张：VR 缓解了实验控制与真实感之间的取舍；生成式情境只有保住这种可控性，才算保住了这一方法。
- 内容: 发表于 Psychological Inquiry 的靶文章，提出把沉浸式虚拟环境作为社会心理学研究方法：实验者可以让每位参与者面对同样逼真的情境，精确复现实验，并用虚拟人代替实验助手。
- 实现方式: 概念性靶文章，回顾早期沉浸式 VR 研究，阐述这一方法的优势与局限，同期附有同行评论。
- 能力维度: 实验控制, 情境可达性
- 论文: https://doi.org/10.1207/S15327965PLI1302_01 (Psychological Inquiry 13(2))

#### 定义虚拟现实：决定远程临场感的维度（Defining Virtual Reality: Dimensions Determining Telepresence） — Jonathan Steuer (1992)
- 类型: 论文 / 综述
- 输入:  → 输出: 人工制作的 VR 情境
- 核心想法: 生动性与交互性仍是评判生成系统的两条轴线：生成的世界有多丰富，回应得有多快、多广。
- 内容: 发表于 Journal of Communication 的论文，以“远程临场”这种体验而非硬件来定义虚拟现实，并提出决定它的两个技术维度：生动性（感官信息的广度与深度）与交互性（用户控制的速度、范围与映射）。
- 实现方式: 概念性论文，按生动性与交互性两个维度对媒介技术进行分类。
- 能力维度: 感知真实感, 反应性
- 论文: https://doi.org/10.1111/j.1460-2466.1992.tb00812.x (Journal of Communication 42(4))

#### 功能心理学中的代表性设计与概率理论（Representative design and probabilistic theory in a functional psychology） — Egon Brunswik (1955)
- 类型: 论文 / 综述
- 输入:  → 输出: 人工制作的 VR 情境
- 核心想法: 代表性设计为生成式情境提供了方法论依据：与其手工搭建一个场景，不如生成大量按生态学原则抽样的变体。
- 内容: 发表于 Psychological Review 的经典论文，主张心理学应像抽样被试那样，认真地从人们真实生活的环境中抽样刺激情境，而不是在人为布置中孤立单一变量。
- 实现方式: 在 Brunswik 的概率功能主义（透镜模型）框架内的理论论证，对比系统设计与代表性设计两种实验思路。
- 能力维度: 情境多样性, 实验控制
- 论文: https://doi.org/10.1037/h0047470 (Psychological Review 62(3))

### 社会心理学 VR 实验

在沉浸式情境中研究服从、旁观者、具身与社会互动。

#### 在虚拟现实中以性骚扰受害者视角具身体验，可降低随后米尔格拉姆服从情境中的行动从众（An Embodied Perspective as a Victim of Sexual Harassment in Virtual Reality Reduces Action Conformity in a Later Milgram Obedience Scenario） — Solène Neyret, Mel Slater (2020)
- 类型: 行为研究 · 时序: 脚本 / 规则驱动
- 输入: 身体、面部与视线追踪 → 输出: 人工制作的 VR 情境, 虚拟人（脸 / 身体）
- 核心想法: 情境可以串联：一次具身体验会改变下一个情境中的行为，因此一组生成的场景序列本身就是一种实验操纵。
- 内容: 60 名男性在虚拟酒吧中目睹一群男性对一名女性的性骚扰，有人只以群体成员之一的身份在场，有人还以受害女性的身体体验了这一幕；后者在随后的米尔格拉姆式情境中更少随群体行动。
- 实现方式: 三组各 20 人（仅作为群体成员、还以女性身体体验、只经历空酒吧的对照组），随后在群体压力下完成虚拟米尔格拉姆任务。
- 参数: N=60 (3 × 20)
- 能力维度: 情境可达性, 实验控制
- 论文: https://doi.org/10.1038/s41598-020-62932-w (Scientific Reports 10 (2020))
- 视频: https://www.youtube.com/watch?v=D6QcTSB6_t0

#### 建立长期共情：传统换位思考与虚拟现实换位思考的大规模比较（Building long-term empathy: A large-scale comparison of traditional and virtual reality perspective-taking） — Fernanda Herrera, Jeremy Bailenson (2018)
- 类型: 行为研究 · 时序: 脚本 / 规则驱动
- 输入: 身体、面部与视线追踪, 键盘与手柄动作 → 输出: 人工制作的 VR 情境
- 核心想法: 具身的换位思考可以延续到体验结束之后；检验生成的共情情境，应看长期追踪，而不是体验后的即时评分。
- 内容: 两项实验把 VR 体验《Becoming Homeless》（经历失业、失去住所）与传统换位思考任务相比较；在八周内，VR 组对无家可归者的态度更积极、更持久，也更愿意签署支持可负担住房的请愿书。
- 实现方式: 大样本实验，比较 VR、叙事式换位思考与对照条件（研究二另比较桌面与头显），在八周内测量态度量表与签署请愿这一行为指标。
- 参数: follow-up over 8 weeks
- 能力维度: 情境可达性, 实验控制
- 论文: https://doi.org/10.1371/journal.pone.0204494 (PLOS ONE 13(10))
- 视频: https://www.youtube.com/watch?v=OK2yJIcAhDE

#### 米尔格拉姆服从实验 VR 复现中参与者对“学习者”的关切（Participant concerns for the Learner in a Virtual Reality replication of the Milgram obedience study） — Mar Gonzalez-Franco, Mel Slater (2018)
- 类型: 行为研究 · 时序: 脚本 / 规则驱动
- 输入: 语音与音频, 身体、面部与视线追踪 → 输出: 人工制作的 VR 情境, 虚拟人（脸 / 身体）
- 核心想法: 在虚拟复现中记录细粒度行为，可以检验原范式只能争论的理论（此处为“代理状态”）。
- 内容: 40 名参与者经历了 VR 版米尔格拉姆范式；与 20 名对照者相比，他们在朗读测试题时会刻意加重正确选项来帮助虚拟学习者——这说明他们关心受害者，而非单纯服从。
- 实现方式: VR 复现实验，对参与者朗读词对的语音进行声学分析，并与未经历模拟的对照组比较。
- 参数: N=40 VR + 20 controls
- 能力维度: 行为似真性, 实验控制
- 论文: https://doi.org/10.1371/journal.pone.0209704 (PLOS ONE 13(12))
- 视频: https://www.youtube.com/watch?v=83zBvG1e7uA

#### 沉浸式虚拟环境中旁观者对暴力事件的反应（Bystander Responses to a Violent Incident in an Immersive Virtual Environment） — Mel Slater (2013)
- 类型: 行为研究 · 时序: 脚本 / 规则驱动
- 输入: 身体、面部与视线追踪, 语音与音频 → 输出: 人工制作的 VR 情境, 虚拟人（脸 / 身体）
- 核心想法: 无法真实布置的暴力场景被变成可控的 2×2 实验——为生成大量危险社会场景的变体提供了样板。
- 内容: 40 名男性阿森纳球迷在虚拟酒吧中目睹一场争执升级为暴力；当受害者也是阿森纳球迷时，他们更常出手干预，支持了用社会认同解释旁观者行为的观点。
- 实现方式: 双因素组间设计（受害者为同群体 vs. 外群体 × 受害者是否望向参与者），使用真人大小的虚拟角色，并根据录像编码干预行为。
- 参数: N=40 · 2×2 between-groups
- 能力维度: 情境可达性, 行为似真性
- 论文: https://doi.org/10.1371/journal.pone.0052766 (PLoS ONE 8(1): e52766)
- 视频: https://www.youtube.com/watch?v=m6kBQk0DCFM

#### 进入黑人化身的皮肤可降低内隐种族偏见（Putting yourself in the skin of a black avatar reduces implicit racial bias） — Tabitha Peck, Mel Slater (2013)
- 类型: 行为研究 · 时序: 脚本 / 规则驱动
- 输入: 身体、面部与视线追踪 → 输出: 虚拟人（脸 / 身体）, 人工制作的 VR 情境
- 核心想法: 对另一种身份的全身拥有感能可测地改变态度——对任何使用生成化身的研究而言，这都是一种强效且有伦理分量的操纵。
- 内容: 肤色较浅的参与者被赋予一具随自己动作而动的深肤色虚拟身体后，其内隐种族偏见低于其他身体条件下的参与者。
- 实现方式: 组间具身实验，使用全身动作捕捉与虚拟镜子，在体验前后施测内隐联想测验。
- 能力维度: 实验控制, 情境可达性
- 论文: https://doi.org/10.1016/j.concog.2013.04.016 (Consciousness and Cognition 22(3))
- 视频: https://www.youtube.com/watch?v=HliN3iOX090

#### 以年龄增长后的“未来自我”形象提升储蓄行为（Increasing Saving Behavior Through Age-Progressed Renderings of the Future Self） — Hal Hershfield, Jeremy Bailenson (2011)
- 类型: 行为研究 · 时序: 脚本 / 规则驱动
- 输入: 身体、面部与视线追踪 → 输出: 虚拟人（脸 / 身体）, 人工制作的 VR 情境
- 核心想法: 一个来自另一时间点的“生成的自己”就能改变真实的经济决策——这是把合成面孔用作行为干预的早期案例。
- 内容: 在虚拟镜子中（后续研究中也在屏幕上）见到自己“变老”化身的参与者，比看到当前年龄化身的人，向假想的退休账户投入了更多钱。
- 实现方式: 与斯坦福 VHIL 合作的系列实验，使用经年龄变形的三维化身，测量假想储蓄的分配。
- 能力维度: 情境可达性, 实验控制
- 论文: https://doi.org/10.1509/jmkr.48.spl.s23 (Journal of Marketing Research 48 (SPL))
- 视频: https://www.youtube.com/watch?v=ixwValjzqRg

#### 普罗透斯效应：变换后的自我呈现对行为的影响（The Proteus Effect: The Effect of Transformed Self-Representation on Behavior） — Nick Yee, Jeremy Bailenson (2007)
- 类型: 行为研究 · 时序: 脚本 / 规则驱动
- 输入: 身体、面部与视线追踪 → 输出: 虚拟人（脸 / 身体）, 人工制作的 VR 情境
- 核心想法: 你被赋予的身体本身就是实验变量：生成的化身改变的不只是外观，还有行为。
- 内容: 两项 VR 实验：被分配到更有吸引力化身的参与者与实验助手站得更近、自我披露更多；被分配到更高化身的参与者在谈判中表现得更自信——与他人如何看待他们无关。
- 实现方式: 使用头显的被试间实验，分别操纵化身吸引力（研究一）与身高（研究二），测量人际距离、自我披露与谈判结果。
- 能力维度: 实验控制, 感知真实感
- 论文: https://doi.org/10.1111/j.1468-2958.2007.00299.x (Human Communication Research 33(3))
- 视频: https://www.youtube.com/watch?v=nuOphOwjIDM

#### 米尔格拉姆服从实验的虚拟重现（A Virtual Reprise of the Stanley Milgram Obedience Experiments） — Mel Slater (2006)
- 类型: 行为研究 · 时序: 脚本 / 规则驱动
- 输入: 身体、面部与视线追踪, 语音与音频 → 输出: 人工制作的 VR 情境, 虚拟人（脸 / 身体）
- 核心想法: 证明人们会把极端的虚拟社会情境当真来反应：原本因伦理而无法开展的范式由此可以研究，也意味着生成的情境同样需要伦理审查。
- 内容: 参与者对一位女性虚拟“学习者”进行词语联想测试，并在她答错时施以“电击”，她会出声抗议。能看见、听见她的参与者出现了应激反应，有些人中途退出——尽管所有人都知道她不是真人。
- 实现方式: 组间实验（能看见并听见学习者 vs. 仅文字交互），在类 CAVE 投影系统中按米尔格拉姆的程序进行，测量皮肤电、心率与行为指标。
- 能力维度: 情境可达性, 实验控制
- 论文: https://doi.org/10.1371/journal.pone.0000039 (PLoS ONE 1(1): e39)
- 视频: https://www.youtube.com/watch?v=RjUNg3pkEag

#### 面对三种虚拟听众时的公开演讲焦虑实验（An Experiment on Public Speaking Anxiety in Response to Three Different Types of Virtual Audience） — David-Paul Pertaub, Mel Slater (2002)
- 类型: 行为研究 · 时序: 脚本 / 规则驱动
- 输入: 语音与音频, 身体、面部与视线追踪 → 输出: 人工制作的 VR 情境, 虚拟人（脸 / 身体）
- 核心想法: 只要表现出评判意味，即便是低保真的虚拟角色也会引发社会威胁感——此后所有虚拟听众训练系统都以此为基础。
- 内容: 参与者向八名虚拟男性听众做五分钟演讲，听众或保持中性，或表现友善，或显出厌倦与敌意；尽管演讲者知道听众是虚拟的，负面听众仍引发了焦虑。
- 实现方式: 在伦敦大学学院进行的组间实验（中性、积极、消极听众），测量自评焦虑与演讲自信。
- 参数: 5-min talk · 8 virtual audience members · 3 conditions
- 能力维度: 行为似真性, 实验控制
- 论文: https://doi.org/10.1162/105474602317343668 (Presence: Teleoperators and Virtual Environments 11(1))
- 视频: https://www.youtube.com/watch?v=rqvdb4gttyU

### 犯罪学与极端情境

入室盗窃、攻击、威胁与紧急情况：无法真实布置的情境。

#### 用虚拟现实考察警察在协同出警互动中的决策（Using Virtual Reality to Examine Officer Decision-Making in Police Co-Response Interactions） — Connor Powelson (2025-07-21)
- 类型: 行为研究 · 时序: 脚本 / 规则驱动
- 输入: 身体、面部与视线追踪, 语音与音频 → 输出: 人工制作的 VR 情境
- 核心想法: VR 加出声思维，把罕见的高风险遭遇转化为可检视的决策数据；在此基础上很容易生成当事人行为的不同变体。
- 内容: 警察在 VR 中与一名临床医生“协同出警”处理精神健康危机警情，并边做边出声思考，揭示了他们如何决定医生站在哪里、共享哪些信息、谁承担什么角色。
- 实现方式: 质性研究，结合 VR 模拟、出声思维与对警员及协同出警人员的半结构化访谈。
- 能力维度: 情境可达性
- 论文: https://doi.org/10.1007/s12103-025-09831-w (American Journal of Criminal Justice (2025))
- 图片: https://media.springernature.com/m685/springer-static/image/art%3A10.1007%2Fs12103-025-09831-w/MediaObjects/12103_2025_9831_Fig1_HTML.png

#### 虚拟入室盗窃项目——宾夕法尼亚（VBPP）：面向犯罪学研究的开放获取虚拟现实环境（Introducing The Virtual Burglary Project – Pennsylvania (VBPP): An Open Access Virtual Reality Environment for Criminology Research） — Patrick McClanahan (2025-03-27)
- 类型: 开源工具 · 时序: 脚本 / 规则驱动 · 获取方式: 开源权重 / 代码
- 输入: 身体、面部与视线追踪, 键盘与手柄动作 → 输出: 人工制作的 VR 情境, 三维场景 / 世界
- 核心想法: 共享、开放的虚拟刺激材料让不同实验室能运行同一情境——生成式情境同样需要这样的复现基础设施。
- 内容: 该论文公开了虚拟入室盗窃项目宾夕法尼亚分支的两个开放获取虚拟街区，用于研究与盗窃相关的行为、情绪与认知，其他犯罪学者也可直接复用。
- 实现方式: 介绍两个 VR 街区及其可调整的要素与数据记录方式，并给出研究问题示例；该项目曾在美国监狱中开展 VR 盗窃任务。
- 能力维度: 实验控制, 创作可及性
- 论文: https://doi.org/10.21428/cb6ab371.f1f780ee (CrimRxiv (2025))
- 视频: https://www.youtube.com/watch?v=2BST0F-Nq_8

#### 写给犯罪学家的虚拟现实：一份路线图（Virtual Reality for Criminologists: A Road Map） — Jean-Louis van Gelder (2023-08-08)
- 类型: 论文 / 综述
- 输入:  → 输出: 人工制作的 VR 情境
- 核心想法: 犯罪学之所以需要 VR，是因为它能在违法或不安全、无法真实创设的情境中观察行为——而生成工具恰好能让这类情境的变化成本更低。
- 内容: 发表于 Crime and Justice 的长文，回顾犯罪相关情境中的 VR 研究及相关领域成果，阐述这项技术的特点、局限与伦理挑战，并认为 VR 可能成为“犯罪学的培养皿”。
- 实现方式: 综述与研究议程，涵盖 VR 犯罪学的生态效度、理论检验、伦理与实际设计选择。
- 能力维度: 情境可达性, 实验控制
- 论文: https://doi.org/10.1086/726691 (Crime and Justice 52 (2023))

#### 在“工作”中学习：用虚拟环境研究入室盗窃者的专长（Learning on the job: Studying expertise in residential burglars using virtual environments） — Claire Nee, Jean-Louis van Gelder (2019)
- 类型: 行为研究 · 时序: 脚本 / 规则驱动
- 输入: 身体、面部与视线追踪, 键盘与手柄动作 → 输出: 人工制作的 VR 情境
- 核心想法: 以专家行为来检验虚拟场景（盗窃犯的行为像盗窃犯）——任何生成的犯罪情境都应达到这一标准。
- 内容: 56 名在押入室盗窃犯、50 名其他罪犯和 55 名非罪犯各自在虚拟街区中完成一次模拟盗窃；入室盗窃犯侦察街区、搜索房屋的方式体现出专业技能。
- 实现方式: 准实验，比较三组人在虚拟盗窃中的路线、时间分配与目标选择，并以认知专长理论解释。
- 参数: N=161 (56 burglars · 50 other offenders · 55 non-offenders)
- 能力维度: 情境可达性, 实验控制
- 论文: https://doi.org/10.1111/1745-9125.12210 (Criminology 57(3))
- 视频: https://www.youtube.com/watch?v=82XkiXi7uQE

#### 在虚拟现实中让施暴者成为受害者：家庭暴力中视角转换的影响（Offenders become the victim in virtual reality: impact of changing perspective in domestic violence） — Sofia Seinfeld, Mel Slater (2018)
- 类型: 行为研究 · 时序: 脚本 / 规则驱动
- 输入: 身体、面部与视线追踪 → 输出: 虚拟人（脸 / 身体）, 人工制作的 VR 情境
- 核心想法: 让罪犯换位进入受害者的身体，是只有 VR 才能布置的干预；生成技术可以按个案定制施暴者、场景与台词。
- 内容: 男性家暴罪犯和无暴力史的对照者被赋予一具女性虚拟身体，同时一名虚拟男性对“她”进行言语虐待；体验之后，罪犯识别女性面孔中恐惧情绪的能力有所提高。
- 实现方式: 通过头显与动作捕捉诱发全身拥有错觉，并在虚拟施暴场景前后施测情绪识别。
- 能力维度: 情境可达性, 实验控制
- 论文: https://doi.org/10.1038/s41598-018-19987-7 (Scientific Reports 8 (2018))
- 视频: https://www.youtube.com/watch?v=l4R9aJIKzRI

#### 虚拟入室盗窃：探索用虚拟现实研究“进行中”的盗窃（Virtual Burglary: Exploring the Potential of Virtual Reality to Study Burglary in Action） — Jean-Louis van Gelder (2017)
- 类型: 行为研究 · 时序: 脚本 / 规则驱动
- 输入: 身体、面部与视线追踪, 键盘与手柄动作 → 输出: 人工制作的 VR 情境
- 核心想法: 犯罪从自我报告变成了可观察、可记录的行为——生成环境有望把这种情境可达性扩展到更多罪行与场景。
- 内容: 77 名男性本科生戴着头显在虚拟街区中行走，并被要求入室盗窃其中一户；系统记录了他们的路线、偷走的物品和心率，同时操纵是否响起警报以及他们对被抓概率的认知。
- 实现方式: 可自由走动的 VR 盗窃任务，实验操纵警报与感知风险，记录行为日志与心率，并测量自我控制、感觉寻求等个体特质。
- 参数: N=77
- 能力维度: 情境可达性, 实验控制
- 论文: https://doi.org/10.1177/0022427816663997 (Journal of Research in Crime and Delinquency 54(1))
- 视频: https://www.youtube.com/watch?v=uAiuTmkKejY
- 项目主页: https://csl.mpg.de/en/projects/virtual-burglary-project

#### 沉浸式虚拟环境中高压疏散时的人群行为（Crowd behaviour during high-stress evacuations in an immersive virtual environment） — Mehdi Moussaïd (2016)
- 类型: 行为研究 · 时序: 脚本 / 规则驱动
- 输入: 键盘与手柄动作 → 输出: 人工制作的 VR 情境, 智能体行为与动作
- 核心想法: 多人虚拟环境让人群紧急情况可以被实验研究；生成的建筑布局与险情可以把这类测试扩展到远不止一栋建筑。
- 内容: 多组真实参与者在共享的三维虚拟建筑中各自操控一个化身；常规疏散时重现了已知的人群模式，高压疏散条件则展示了人群移动在压力下如何变化。
- 实现方式: 联网的多人实验，把虚拟人群模式与真实世界观察相比较，并加入高压疏散条件。
- 能力维度: 情境可达性, 实验控制
- 论文: https://doi.org/10.1098/rsif.2016.0414 (Journal of the Royal Society Interface 13(122))
- 视频: https://www.youtube.com/watch?v=pqH7pPmM28c

### 模拟训练与虚拟人

用于练习沟通与判断的虚拟病人、访谈者与队友。

#### Talespin CoPilot Designer — Talespin (2021)
- 类型: 产品 / 应用 · 时序: 预先生成 · 获取方式: 产品 / 应用
- 输入: 文字提示 → 输出: 虚拟人（脸 / 身体）, 对话 / 文本, 人工制作的 VR 情境
- 核心想法: 生成式 AI 最早以创作辅助的身份进入 VR 训练：先起草由人审阅的分支对话，之后才去实时驱动角色。
- 内容: 无代码工具，用于搭建含虚拟人、分支对话与反馈的 VR 软技能模拟；到 2023 年已加入用于起草内容的生成式 AI。Talespin 官网现已跳转至 Cornerstone 的沉浸式学习平台，后者宣传与 AI 驱动的虚拟人进行角色扮演。
- 实现方式: 基于流程编辑器编写分支对话并驱动动画虚拟人，后加入生成式内容工具，可在头显与桌面端交付。
- 能力维度: 创作可及性, 行为似真性
- 视频: https://www.youtube.com/watch?v=qOFuXWC67-c
- 项目主页: https://www.cornerstoneondemand.com/platform/immersive-learning/

#### Bodyswaps — Bodyswaps (2019)
- 类型: 产品 / 应用 · 时序: 回合制 · 获取方式: 产品 / 应用
- 输入: 语音与音频, 身体、面部与视线追踪 → 输出: 虚拟人（脸 / 身体）, 对话 / 文本, 语音 / 声音
- 核心想法: 商业培训已从分支脚本转向开放式 AI 角色扮演与自动评分；这种评分是否有效，是尚待研究的问题。
- 内容: 在 VR 与浏览器中进行的软技能训练：学习者与 AI 化身进行角色扮演对话（例如护士与病人交谈），之后获得完整对话记录，以及 AI 教练就说话内容与方式给出的反馈。
- 实现方式: 以语音输入与 AI 化身对话（很可能基于大语言模型），支持 VR 头显、桌面与移动端，并自动分析说话内容以及眼神交流等非语言线索。
- 能力维度: 反应性, 适应性
- 视频: https://www.youtube.com/watch?v=XtsHXFwbbCU
- 项目主页: https://bodyswaps.co/

#### SHOTPROS：面向压力下警务决策的 VR 训练（SHOTPROS: VR training for police decision-making under stress） — SHOTPROS (2019)
- 类型: 研究演示 · 时序: 脚本 / 规则驱动 · 获取方式: 仅限研究
- 输入: 身体、面部与视线追踪, 键盘与手柄动作, 语音与音频 → 输出: 人工制作的 VR 情境
- 核心想法: 压力成为可由教官调高调低的训练参数——这正是自适应生成可以接入的位置。
- 内容: 欧盟“地平线 2020”项目：警务机构、心理学家与 VR 开发者共同构建并实地测试 VR 情境，用于训练警员在压力下的决策与行动，配有生理监测与教官控制。
- 实现方式: 历时三年，收集警务教官需求、开展人因研究并在多国实地试验，成果由 Zechner 等人（2023）总结为工具与指南。
- 能力维度: 情境可达性, 实验控制
- 论文: https://doi.org/10.3390/mti7020014 (Multimodal Technologies and Interaction 7(2))
- 视频: https://www.youtube.com/watch?v=MXJHzBUbdgU
- 项目主页: https://shotpros.eu/

#### Axon VR Training — Axon (2018)
- 类型: 产品 / 应用 · 时序: 脚本 / 规则驱动 · 获取方式: 产品 / 应用
- 输入: 身体、面部与视线追踪, 键盘与手柄动作 → 输出: 人工制作的 VR 情境, 360° / 立体视频
- 核心想法: 降级处置训练如今已在警局规模上通过头显进行；Axon 称部分情境可实时调整，这一说法值得与脚本分支方案对照检验。
- 内容: TASER 与执法记录仪制造商 Axon 推出的警务 VR 训练：2018 年 10 月以一个关于精神分裂症的 360° 共情情境起步，2019 年又加入自闭症与自杀相关情境；如今警员从共情与危机应对模块开始，逐步进阶到降级处置、战术决策，以及使用仿真 TASER 和手枪的模拟训练。
- 实现方式: 在一体机头显上运行的实拍与 CG 编写情境，配有可追踪的仿真武器与教官控制；“自适应”为开发方的说法。
- 能力维度: 情境可达性, 适应性
- 视频: https://www.youtube.com/watch?v=PA8DoNYwCz4
- 项目主页: https://www.axon.com/products/vr

#### Strivr — Strivr (2015)
- 类型: 产品 / 应用 · 时序: 脚本 / 规则驱动 · 获取方式: 产品 / 应用
- 输入: 身体、面部与视线追踪 → 输出: 360° / 立体视频, 人工制作的 VR 情境
- 核心想法: 实拍的 360° 情境把 VR 演练带给了庞大的零售员工群体；这家公司的下一步，是让 AI 透过眼镜观察真实工作。
- 内容: 源自斯坦福 VHIL 的企业 VR 培训：员工借助 360° 视频与交互模块演练购物高峰、难缠顾客等情境，沃尔玛在其培训学院中部署了它。截至 2026 年，其官网主推基于智能眼镜的 AI 质检，同时仍提供 VR 平台。
- 实现方式: 以实拍 360° 视频和人工编写的交互情境在一体机头显上交付，并对受训者的反应进行数据分析。
- 能力维度: 感知真实感, 情境可达性
- 视频: https://www.youtube.com/watch?v=0s4OBHV0WH4
- 项目主页: https://www.strivr.com/

#### Mursion — Mursion (2014)
- 类型: 产品 / 应用 · 时序: 实时流式 · 获取方式: 产品 / 应用
- 输入: 语音与音频, 身体、面部与视线追踪 → 输出: 虚拟人（脸 / 身体）, 对话 / 文本, 语音 / 声音
- 核心想法: 人在回路的虚拟人展示了大规模下“全面反应性”是什么样子；大语言模型智能体正是以这条“绿野仙踪”基线来衡量的。
- 内容: 一个让员工与教师和化身演练艰难对话的模拟平台：经过训练的模拟专员实时为化身配音并操控其行为；截至 2026 年，Mursion 把自己定位为 AI 驱动的技能提升平台。
- 实现方式: 由受过训练的真人操作员按情境指引实时操控化身（声音、表情、行为）并配合教练反馈；公司如今也宣传 AI 驱动的模拟。
- 能力维度: 反应性, 适应性
- 视频: https://www.youtube.com/watch?v=yRD4Hbn3EUM
- 项目主页: https://www.mursion.com/

#### 重新审视模拟训练中的保真度（Reconsidering Fidelity in Simulation-Based Training） — Stanley J. Hamstra (2014)
- 类型: 论文 / 综述
- 输入:  → 输出: 人工制作的 VR 情境
- 核心想法: 生成的真实感本身不是目标：训练情境需要的是对任务有意义的线索——这比照片级真实更便宜，也更容易检验。
- 内容: 发表于 Academic Medicine 的评论文章，主张用“物理相似性”与“功能任务一致性”取代笼统的“保真度”，并指出推动学习的是投入度以及与任务的对应，而非表面真实感。
- 实现方式: Hamstra、Brydges、Hatala、Zendejas 与 Cook 对模拟训练文献的概念分析。
- 能力维度: 感知真实感, 行为似真性
- 论文: https://doi.org/10.1097/ACM.0000000000000130 (Academic Medicine 89(3))

#### 自闭症谱系障碍成人的虚拟现实求职面试训练（Virtual Reality Job Interview Training in Adults with Autism Spectrum Disorder） — Matthew J. Smith (2014)
- 类型: 行为研究 · 时序: 脚本 / 规则驱动
- 输入: 语音与音频 → 输出: 虚拟人（脸 / 身体）, 对话 / 文本, 语音 / 声音
- 核心想法: 分级难度加上与虚拟面试官的无限次重复，在分支脚本时代就已奏效；生成技术解除的是编写上限，而不是对试验验证的需要。
- 内容: 虚拟现实求职面试训练（VR-JIT）的随机试验：自闭症成年人反复与虚拟招聘经理“Molly Porter”面试，难度可逐级提高并附带反馈；与对照组相比，受训者的模拟面试表现有所提升。
- 实现方式: 对 SIMmersion 分支对话模拟器的随机对照疗效试验，在训练前后以模拟面试评估。
- 能力维度: 适应性, 反应性
- 论文: https://doi.org/10.1007/s10803-014-2113-y (Journal of Autism and Developmental Disorders 44)
- 视频: https://www.youtube.com/watch?v=Uz-hfR1Hulo

#### 为训练环境构建交互式虚拟人（Building Interactive Virtual Humans for Training Environments） — Patrick Kenny, 南加州大学创意技术研究所 (2007)
- 类型: 论文 / 综述 · 时序: 脚本 / 规则驱动
- 输入: 语音与音频, 身体、面部与视线追踪 → 输出: 虚拟人（脸 / 身体）, 对话 / 文本, 智能体行为与动作
- 核心想法: 大语言模型之前的蓝图：训练用虚拟人的每个模块都需手工构建与编写——这正是生成模型如今省去的成本，也是它们可能削弱的可控性。
- 内容: USC ICT 在 I/ITSEC 发表的论文，介绍训练用交互式虚拟人的架构：语音识别、语言理解、对话管理、情绪建模、非语言行为生成与渲染，并以 ICT 的谈判训练与虚拟病人系统为例。
- 实现方式: 对 ICT 集成式虚拟人架构及其训练应用背后的内容编写工作的系统性介绍。
- 能力维度: 行为似真性, 创作可及性
- 论文: https://openalex.org/W2151904280 (I/ITSEC 2007)

#### 虚拟人体验用于人际技能教育的效度（The validity of a virtual human experience for interpersonal skills education） — Kyle Johnsen (2007)
- 类型: 行为研究 · 时序: 脚本 / 规则驱动
- 输入: 语音与音频, 身体、面部与视线追踪 → 输出: 虚拟人（脸 / 身体）, 对话 / 文本
- 核心想法: 以真实考试作为效度标准——这正是多数大语言模型虚拟病人论文至今仍跳过的一步。
- 内容: 33 名二年级医学生在“虚拟客观结构化临床考试”（VOSCE）中问诊一位真人大小的虚拟病人并接受问诊技能评分，其成绩与面对真人标准化病人的考试成绩进行了比较。
- 实现方式: 作为医学院课程要求的一部分，比较学生面对投影的真人大小虚拟人（语音识别对话）与面对真人标准化病人时的问诊表现。
- 参数: N=33 medical students
- 能力维度: 行为似真性, 实验控制
- 论文: https://doi.org/10.1145/1240624.1240784 (CHI 2007)

#### 虚拟标准化病人（Justin、Justina）（Virtual Standardized Patients (Justin, Justina)） — 南加州大学创意技术研究所, Albert "Skip" Rizzo (2007)
- 类型: 研究演示 · 时序: 脚本 / 规则驱动 · 获取方式: 仅限研究
- 输入: 语音与音频 → 输出: 虚拟人（脸 / 身体）, 对话 / 文本
- 核心想法: 永不疲倦、从不走样的标准化病人：大语言模型驱动的病人正是以牺牲这种一致性换取应答广度。
- 内容: USC ICT 开发的真人大小虚拟病人，例如患有品行障碍的青少年、遭受性侵后患 PTSD 的年轻女性；受训临床人员直接开口问诊，病人从预先编写的台词中作答，由语言理解模块挑选。
- 实现方式: 把受训者的提问统计分类到预先编写的应答集合中，以 ICT 的虚拟人技术驱动动画，并由精神科住院医师与社会工作专业学生参与评估。
- 能力维度: 行为似真性, 反应性
- 论文: https://doi.org/10.20385/1860-2037/8.2011.3 (Journal of Virtual Reality and Broadcasting 8 (2011))
- 视频: https://www.youtube.com/watch?v=PPbcl8Z-8Ec

#### 刻意练习在获得专家级表现中的作用（The role of deliberate practice in the acquisition of expert performance） — K. Anders Ericsson (1993)
- 类型: 论文 / 综述
- 输入:  → 输出: 人工制作的 VR 情境
- 核心想法: 训练的价值来自大量有针对性、带反馈、处在能力边缘的重复——这正是自适应生成情境可以规模化提供的。
- 内容: 发表于 Psychological Review 的论文，表明顶尖音乐家与水平较低的同侪的主要差别在于累计的刻意练习时长——即有明确目标、伴随即时反馈与重复、专门用于提升表现的费力练习。
- 实现方式: 理论框架，加上对柏林一所音乐学院小提琴与钢琴学生的回溯性日记与访谈研究。
- 能力维度: 适应性, 情境多样性
- 论文: https://doi.org/10.1037/0033-295X.100.3.363 (Psychological Review 100(3))

### 临床与治疗 VR

在虚拟情境中进行的暴露治疗、辅导与心理治疗。

#### 以不可察觉的变化消除焦虑：针对公开演讲恐惧的单次暴露疗法范式可行性研究（Desensitizing Anxiety Through Imperceptible Change: Feasibility Study on a Paradigm for Single-Session Exposure Therapy for Fear of Public Speaking） — Domna Banakou, Mel Slater (2024-07-22)
- 类型: 行为研究 · 时序: 脚本 / 规则驱动
- 输入: 语音与音频, 身体、面部与视线追踪 → 输出: 人工制作的 VR 情境, 虚拟人（脸 / 身体）
- 核心想法: 一个持续且在意识阈限以下变化的情境，可以把整套暴露阶梯压缩进一次治疗——这种控制只有生成式或程序化场景才能做到。
- 内容: 害怕公开演讲的人与一位虚拟治疗师交谈，在一次治疗过程中，这位治疗师以几乎察觉不到的变化逐渐变成了一整群听众；一周后在虚拟舞台上演讲时，这一次治疗降低焦虑的效果至少与五次常规暴露治疗相当。
- 实现方式: 三组可行性研究（单次“不可察觉变化”组 n=16、五次暴露组 n=14、日常对话对照组 n=15），一周后进行 VR 演讲测试，并以贝叶斯模型分析。
- 参数: N=45 · 3 arms · test after 1 week
- 能力维度: 适应性, 实验控制
- 论文: https://doi.org/10.2196/52212 (JMIR Formative Research 8 (2024))
- 视频: https://www.youtube.com/watch?v=QFvJMPmdsDE

#### gameChange：用自动化虚拟现实疗法治疗精神病患者的广场回避与痛苦（多中心随机对照试验）（Automated virtual reality therapy to treat agoraphobic avoidance and distress in patients with psychosis (gameChange): a multicentre, parallel-group, single-blind, randomised, controlled trial in England with mediation and moderation analyses） — Daniel Freeman (2022)
- 类型: 行为研究 · 时序: 脚本 / 规则驱动
- 输入: 身体、面部与视线追踪 → 输出: 人工制作的 VR 情境, 虚拟人（脸 / 身体）, 语音 / 声音
- 核心想法: 当情境与教练都实现自动化后，治疗无需治疗师在场即可进行；这一试验标准正是生成式疗法需要达到的。
- 内容: 在英格兰九个 NHS 机构开展的多中心随机试验：自动化 VR 疗法 gameChange 由一位虚拟教练引导精神病患者，按难度分级进入他们回避的日常情境（如咖啡馆、公交车、商店）；疗法减少了回避与痛苦，对重度广场恐惧者效果最明显。
- 实现方式: 单盲随机对照试验（gameChange 加常规护理 vs. 仅常规护理），由预先录制的虚拟教练引导分级 VR 暴露，并进行中介与调节分析。
- 参数: 9 NHS trusts · single-blind RCT
- 能力维度: 情境可达性, 适应性
- 论文: https://doi.org/10.1016/S2215-0366(22)00060-8 (The Lancet Psychiatry 9(5))
- 视频: https://www.youtube.com/watch?v=AdMLfdPBb60
- 项目主页: https://gamechangevr.com/

#### RelieVRx — AppliedVR (2021)
- 类型: 产品 / 应用 · 时序: 脚本 / 规则驱动 · 获取方式: 产品 / 应用
- 输入: 身体、面部与视线追踪 → 输出: 人工制作的 VR 情境, 音效、音乐与空间音频
- 核心想法: 脚本化 VR 已成为受监管的医疗器械；任何生成式或自适应的后继者都要跨过同样的证据门槛。
- 内容: 用于慢性下背痛的处方型居家 VR 项目，通过每日简短课程教授呼吸、放松、注意力转移等疼痛管理技巧；2021 年获美国 FDA De Novo 授权。
- 实现方式: 基于认知行为疗法与正念的预制模块，在家中通过一体机头显交付，并在与假 VR 对照的随机试验中接受评估。
- 能力维度: 适应性, 情境可达性
- 视频: https://www.youtube.com/watch?v=iDM1vHLlH9Q
- 项目主页: https://www.relievrx.com/

#### AVATAR 疗法治疗精神病患者的言语性幻听：单盲随机对照试验（AVATAR therapy for auditory verbal hallucinations in people with psychosis: a single-blind, randomised controlled trial） — Tom Craig (2018)
- 类型: 行为研究 · 时序: 实时流式
- 输入: 语音与音频 → 输出: 虚拟人（脸 / 身体）, 语音 / 声音
- 核心想法: 为患者的“折磨者”定制、由真人配音的化身，是虚拟人的一种临床用途；大语言模型可以让它规模化，但绝不能让它失控偏离。
- 内容: 受迫害性幻听困扰的人为自己听到的主要“声音”创建一张数字面孔和一种声音，然后与它对话；治疗师通过变声器以化身的身份说话，并让它逐渐变得不那么敌意。与支持性咨询相比，幻听的严重程度有所下降。
- 实现方式: 单盲随机对照试验，比较 AVATAR 疗法（由 Julian Leff 于 2008 年提出）与支持性咨询；化身依患者描述制作，由治疗师实时配音。规模更大的 AVATAR2 试验于 2024 年发表。
- 能力维度: 反应性, 适应性
- 论文: https://doi.org/10.1016/S2215-0366(17)30427-3 (The Lancet Psychiatry 5(1))
- 视频: https://www.youtube.com/watch?v=4Gmp9IILUx4

#### 用沉浸式虚拟现实进行自动化心理治疗以治疗恐高：单盲平行组随机对照试验（Automated psychological therapy using immersive virtual reality for treatment of fear of heights: a single-blind, parallel-group, randomised controlled trial） — Daniel Freeman (2018)
- 类型: 行为研究 · 时序: 脚本 / 规则驱动
- 输入: 身体、面部与视线追踪 → 输出: 人工制作的 VR 情境, 虚拟人（脸 / 身体）, 语音 / 声音
- 核心想法: 早期的严格证据：全自动的虚拟教练也能实施心理治疗，为 VR 中由大语言模型引导的治疗开了先例。
- 内容: 随机试验：恐高的成年人在两周内接受约六次、每次 30 分钟的 VR 治疗，全程由一位动画虚拟教练引导，无需治疗师在场；与常规护理相比，恐高程度明显下降。
- 实现方式: 单盲随机对照试验：在消费级头显上进行自动化认知 VR 治疗（虚拟教练由演员的动作与声音捕捉驱动），对照为常规护理，以恐高解释问卷为结局指标。
- 参数: ~6 × 30-min sessions over 2 weeks
- 能力维度: 适应性, 情境可达性
- 论文: https://doi.org/10.1016/S2215-0366(18)30226-8 (The Lancet Psychiatry 5(8))
- 视频: https://www.youtube.com/watch?v=yDJArJ40FGc

#### 以西格蒙德·弗洛伊德身份进行的自我对话：一种用于自我咨询的虚拟身体拥有范式（Conversations between self and self as Sigmund Freud—A virtual body ownership paradigm for self counselling） — Sofia Adelaide Osimo, Mel Slater (2015)
- 类型: 行为研究 · 时序: 脚本 / 规则驱动
- 输入: 语音与音频, 身体、面部与视线追踪 → 输出: 虚拟人（脸 / 身体）, 人工制作的 VR 情境, 语音 / 声音
- 核心想法: 咨询者可以是换了身体的参与者本人——后续研究在此基础上加入了推动自我对话的 AI 智能体。
- 内容: 参与者先向一位虚拟咨询者讲述个人困扰，再换到咨询者的身体里回答自己，并听到经变声处理的自己的声音；与以“另一个自己”的身体提供建议相比，化身为西格蒙德·弗洛伊德时心情改善更明显。
- 实现方式: 具身实验，使用全身追踪，在参与者化身与咨询者化身之间切换第一人称视角并进行变声，比较弗洛伊德身体与“自我复制”身体两种条件。
- 能力维度: 共创与能动性, 情境可达性
- 论文: https://doi.org/10.1038/srep13899 (Scientific Reports 5 (2015))
- 视频: https://www.youtube.com/watch?v=sn-UNGcbi2Q

#### “它只是台计算机”：虚拟人提高人们的自我披露意愿（It's only a computer: Virtual humans increase willingness to disclose） — Gale Lucas, 南加州大学创意技术研究所 (2014)
- 类型: 行为研究 · 时序: 脚本 / 规则驱动
- 输入: 语音与音频, 身体、面部与视线追踪 → 输出: 虚拟人（脸 / 身体）, 对话 / 文本
- 核心想法: 相信没有真人在看会让人更坦诚——因此告诉参与者对面的 AI 是什么，本身就是需要控制的变量。
- 内容: 接受 SimSensei 虚拟人访谈的人，若相信对方是全自动的，比相信有人在后台操控时，对自我暴露的顾虑更少、印象管理更少，也更坦然地流露悲伤。
- 实现方式: 2×2 设计，交叉操纵“告知”（计算机 vs. 真人操作）与“实际控制方式”（自动 vs. 绿野仙踪），测量自我暴露顾虑、印象管理与编码后的情绪表达。
- 能力维度: 行为似真性, 实验控制
- 论文: https://doi.org/10.1016/j.chb.2014.04.043 (Computers in Human Behavior 37)

#### SimSensei Kiosk：用于医疗决策支持的虚拟人访谈者（SimSensei Kiosk: a virtual human interviewer for healthcare decision support） — David DeVault, 南加州大学创意技术研究所 (2014)
- 类型: 研究演示 · 时序: 脚本 / 规则驱动 · 获取方式: 仅限研究
- 输入: 语音与音频, 视频, 身体、面部与视线追踪 → 输出: 虚拟人（脸 / 身体）, 对话 / 文本, 语音 / 声音
- 核心想法: 经过三轮开发：从面对面访谈数据，到“绿野仙踪”原型，再到全自动——生成式访谈者仍然需要走这条方法路线。
- 内容: 虚拟人访谈者“Ellie”询问受访者的生活与身心状况，同时 MultiSense 模块追踪面部、视线、姿态与语音；她会给出倾听反馈并追问，系统据此提取抑郁、焦虑与 PTSD 的指标。
- 实现方式: 先分析真人访谈，再做由两名操作员选择话语与手势的“绿野仙踪”原型，最后实现具备多模态感知、基于规则的对话策略与预编写话语的全自动系统。
- 能力维度: 时间响应性, 反应性
- 论文: https://doi.org/10.65109/mxiv3169 (AAMAS 2014)
- 视频: https://www.youtube.com/watch?v=ejczMs6b1Q4

#### SnowWorld：虚拟现实作为医疗操作中急性烧伤疼痛的非药物辅助镇痛（Virtual Reality as an Adjunctive Non-pharmacologic Analgesic for Acute Burn Pain During Medical Procedures） — Hunter Hoffman (2011)
- 类型: 论文 / 综述 · 时序: 脚本 / 规则驱动
- 输入: 身体、面部与视线追踪, 键盘与手柄动作 → 输出: 人工制作的 VR 情境
- 核心想法: 沉浸本身就像一种剂量：被虚拟世界吸引走的注意力，就是从疼痛那里拿走的注意力，因此沉浸越强，效果可能越强。
- 内容: 关于 SnowWorld 的综述：在这个华盛顿大学开发的 VR 世界里，烧伤患者在换药时向雪人和企鹅扔雪球；患者报告沉浸期间操作疼痛降低 35%–50%，功能磁共振成像也显示与疼痛相关的脑活动下降。
- 实现方式: 回顾 Hoffman 团队的临床与实验室研究，包括可用于水疗换药的防水头显与机械臂支架头显。
- 参数: 35-50% less procedural pain (patient reports)
- 能力维度: 感知真实感, 情境可达性
- 论文: https://doi.org/10.1007/s12160-010-9248-7 (Annals of Behavioral Medicine 41(2))
- 视频: https://www.youtube.com/watch?v=Nh4K_dZ7LvQ

#### Bravemind — Albert "Skip" Rizzo, 南加州大学创意技术研究所 (2005)
- 类型: 研究演示 · 时序: 脚本 / 规则驱动 · 获取方式: 仅限研究
- 输入: 身体、面部与视线追踪, 键盘与手柄动作 → 输出: 人工制作的 VR 情境, 音效、音乐与空间音频
- 核心想法: 由临床医生实时调整刺激，是最早的自适应沉浸情境；生成技术能扩大每位医生可调用的场景库。
- 内容: 针对战争相关 PTSD 的 VR 暴露疗法，脱胎于“Virtual Iraq”：临床医生把患者带入可定制的伊拉克和阿富汗场景，随着患者讲述创伤，逐步加入声音、气味、爆炸与震动。
- 实现方式: 以头显实施延长暴露疗法，配有供临床医生控制刺激出现的面板和多感官装置，并经开放试验与随机试验评估。
- 能力维度: 情境可达性, 适应性
- 论文: https://doi.org/10.1080/20008198.2017.1414560 (European Journal of Psychotraumatology 8 (2017))
- 视频: https://www.youtube.com/watch?v=LRL0TzrNtVc
- 项目主页: https://ict.usc.edu/research/projects/bravemind-virtual-reality-exposure-therapy/

#### 计算机生成（虚拟现实）分级暴露治疗恐高症的疗效（Effectiveness of computer-generated (virtual reality) graded exposure in the treatment of acrophobia） — Barbara Olasov Rothbaum (1995)
- 类型: 行为研究 · 时序: 脚本 / 规则驱动
- 输入: 身体、面部与视线追踪 → 输出: 人工制作的 VR 情境
- 核心想法: 分级暴露只需要一组可信的情境阶梯——这就是 1995 年的图形也能奏效的原因，而生成技术的贡献在于广度与个性化。
- 内容: VR 暴露疗法的早期对照研究：恐高的大学生戴上头显，在逐渐升高的位置乘坐虚拟玻璃电梯、走过桥梁、站上阳台，与候补组相比焦虑和回避都有所减轻。
- 实现方式: 埃默里大学与佐治亚理工学院的 Rothbaum、Hodges 等人进行的对照比较：分级 VR 暴露 vs. 候补对照，测量焦虑、回避与态度。
- 能力维度: 情境可达性, 适应性
- 论文: https://doi.org/10.1176/ajp.152.4.626 (American Journal of Psychiatry 152(4))

### 沉浸式研究中的生成式 AI

把语言模型智能体、生成情境或世界模型用于研究与训练的研究和综述。

#### 当生成式人工智能遇上扩展现实：一项系统综述（When Generative Artificial Intelligence Meets Extended Reality: A Systematic Review） — Xinyu Ning (2026)
- 类型: 论文 / 综述
- 输入: 文字提示, 语音与音频 → 输出: 三维场景 / 世界, 虚拟人（脸 / 身体）, 对话 / 文本
- 核心想法: 这一领域年轻且规模不大：三年的工作只有 26 篇论文——生成式沉浸研究的方法论仍是一片有待开拓的领域。
- 内容: 按 PRISMA 流程筛选出 26 篇 2023–2025 年将生成式 AI 与 XR 结合的文章，总结其应用领域与关键技术实现，并指出研究空白。
- 实现方式: 遵循 PRISMA 的系统综述，包括数据库检索、筛选与对纳入文章的主题分析。
- 能力维度: 创作可及性, 情境多样性
- 论文: https://doi.org/10.1080/10447318.2025.2565392 (International Journal of Human-Computer Interaction (2026; online 2025-09-30))

#### 与港海豹一起 VR 潜水可增强海洋联结感，而对话式 AI 对护海参与的影响取决于此前与海豹的接触经历（VR scuba diving with harbor seals increases ocean connectedness, and the effect of conversational AI on pro-environmental engagement depends on prior experience with seals） — Gustav Bøg Petersen, Jeremy Bailenson (2026-09-07)
- 类型: 行为研究 · 时序: 回合制
- 输入: 语音与音频 → 输出: 人工制作的 VR 情境, 虚拟人（脸 / 身体）, 对话 / 文本
- 核心想法: 配对对照解决了研究生成式对话的核心难题：每个对照者看到的正是某位实验组参与者得到的内容，从而分离出“互动”本身的效应。
- 内容: 在 OceanSpeak 中，参与者在 VR 里潜水，并与一只 AI 驱动的港海豹谈论海洋酸化与过度捕捞。一项预注册研究（N=106）采用“配对对照”设计：对照组看到完全相同的内容，包括另一位参与者与 AI 的对话，但自己不能开口。
- 实现方式: 与斯坦福虚拟人交互实验室合作的预注册被试间实验，以配对回放 AI 对话作为对照；结局指标包括海洋联结感、对海豹的共情、护海行为与知识。
- 参数: N=106 (53 + 53 yoked controls)
- 能力维度: 实验控制, 反应性
- 论文: https://doi.org/10.1016/j.cexr.2026.100181 (Computers & Education: X Reality (2026))

#### CoEmpaTeam：在虚拟现实中用大语言模型化身与动态角色扮演提升认知共情（CoEmpaTeam: Enhancing Cognitive Empathy using LLM-based Avatars and Dynamic Role Play in Virtual Reality） — Dehui Kong (2026-04-13)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 语音与音频, 身体、面部与视线追踪 → 输出: 虚拟人（脸 / 身体）, 对话 / 文本, 语音 / 声音
- 核心想法: 性格成为大语言模型角色可控且经预先验证的参数——朝着把生成的人物视为“经过校准的刺激”迈出了一步。
- 内容: 用于训练认知共情的 VR 系统：用户与三个性格迥异、由大语言模型驱动的化身协作，并通过角色互换从他人视角体验情境；化身性格在线上实验（n=90）中得到验证，系统在实验室研究（n=32）中接受了评估。
- 实现方式: 以提示词设定性格的大语言模型化身，先进行技术评估与线上性格感知验证，再开展关于认知共情结果的实验室实验。
- 参数: online N=90 · lab N=32
- 能力维度: 行为似真性, 情境多样性
- 论文: https://doi.org/10.1145/3772318.3790389 (CHI 2026)
- 视频: https://www.youtube.com/watch?v=ODzQGc8KNZI

#### 扩展现实与 AI 可能把我们带向何方：社交虚拟现实中冒充与 AI 伪造的伦理问题（Where extended reality and AI may take us: Ethical issues of impersonation and AI fakes in social virtual reality） — Ramon Oliva, Mel Slater (2026-04-02)
- 类型: 行为研究 · 时序: 回合制
- 输入: 语音与音频, 身体、面部与视线追踪 → 输出: 虚拟人（脸 / 身体）, 对话 / 文本, 语音 / 声音
- 核心想法: 相貌相似的化身加上大语言模型智能体，让“身份”本身变得可以操纵——使用生成人物的研究需要专属的告知与同意规则。
- 内容: IEEE VR 2025 大会上，一场小组讨论在社交 VR 中进行，每位嘉宾都使用与本人相貌相似的化身；中途两位嘉宾互换化身并假扮对方，另有一个由大语言模型控制的艾伦·图灵化身参与讨论。在填写问卷的 100 名观众中，约 40 人没有察觉这次互换。
- 实现方式: 在现场会议小组讨论中开展的实地研究，画面投影给观众，会后以问卷调查观众是否察觉互换以及如何看待 AI 嘉宾。
- 参数: ~100 audience survey responses
- 能力维度: 感知真实感, 行为似真性
- 论文: https://doi.org/10.1371/journal.pone.0340829 (PLOS ONE (2026))
- 图片: https://journals.plos.org/plosone/article/figure/image?id=10.1371/journal.pone.0340829.g001&size=large

#### 人工智能用于虚拟现实暴露疗法（VRET）：一项系统综述（Artificial intelligence (AI) for virtual reality exposure therapy (VRET): A systematic review） — Kamilla Bergsnev (2026-03-26)
- 类型: 论文 / 综述
- 输入: 身体、面部与视线追踪, 语音与音频 → 输出: 人工制作的 VR 情境
- 核心想法: 自适应暴露——根据患者当下状态调整所恐惧的情境——是最接近实时生成的临床用例，而其证据基础仍然有限。
- 内容: 按 PRISMA 流程纳入截至 2025 年 11 月发表的 23 篇同行评审文章，系统梳理如何用人工智能让 VR 暴露疗法更贴合患者与治疗师的需要。
- 实现方式: 遵循 PRISMA 的系统综述，检索 PsycINFO、Web of Science、Google Scholar、EMBASE、CINAHL 与 MEDLINE，从 377 条记录中纳入 23 篇。
- 参数: 23 of 377 records
- 能力维度: 适应性, 实验控制
- 论文: https://doi.org/10.1038/s41398-026-03936-4 (Translational Psychiatry (2026))

#### 融合虚拟现实与大语言模型，用于手术室团队非技术技能的训练与评估（Integrating Virtual Reality and Large Language Models for Team-Based Non-Technical Skills Training and Evaluation in the Operating Room） — Jacob Barker (2026-01-19)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 语音与音频, 身体、面部与视线追踪 → 输出: 人工制作的 VR 情境, 对话 / 文本
- 核心想法: 这里的大语言模型是测量工具而非情境本身：对团队行为进行自动化、结构化的编码，是在增强而非削弱实验控制。
- 内容: VORTeX 是一个多人 VR 手术室，外科团队在其中处理腹腔镜手术中的紧急情况（气胸、腹腔内出血）；随后由大语言模型依据 NOTSS 框架对团队对话进行分类，并绘制谁在主导、谁在整合信息的互动网络。
- 实现方式: 多人 VR 模拟并录制团队语音；依据 NOTSS 设计的结构化提示词对行为分类并构建有向沟通图；在 SAGES 2024 上由 12 名外科专业人员试用。
- 参数: pilot N=12 · 2 emergency scenarios
- 能力维度: 实验控制, 行为似真性
- 论文: https://doi.org/10.1038/s44484-026-00009-3 (npj Digital Surgery (2026))
- 图片: https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs44484-026-00009-3/MediaObjects/44484_2026_9_Fig1_HTML.png

#### CLiVR：配有 AI 病人的虚拟现实对话式学习系统（CLiVR: Conversational Learning System in Virtual Reality with AI-Powered Patients） — Akilan Amithasagaran (2025-10-21)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 语音与音频 → 输出: 虚拟人（脸 / 身体）, 对话 / 文本, 语音 / 声音
- 核心想法: 从结构化数据库中抽样病例，让大语言模型病人既有多样性，又能把握“变的是什么”——这是对可控性问题的一个务实回答。
- 内容: 基于 Meta Quest 3 的系统，医学受训者可与由大语言模型驱动的虚拟病人进行语音对话；每个病例都从“综合征—症状”数据库动态生成，情感分析对受训者的语气给出反馈。13 位医学院教师评价其易用且逼真。
- 实现方式: Unity 应用，结合语音处理、以生成病例为条件的大语言模型与三维化身；以专家用户研究（n=13）评估易用性、真实感与教学价值。
- 参数: Meta Quest 3 · expert study N=13
- 能力维度: 情境多样性, 反应性
- 论文: https://arxiv.org/abs/2510.19031 (arXiv (2025))
- 图片: https://arxiv.org/html/2510.19031v1/Images/vr-combined.png

#### 面向 VR 具身对话智能体的低延迟大语言模型多模态对话系统（A Latency-Optimized LLM-based Multimodal Dialogue System for Embodied Conversational Agents in VR） — Konstantin W. Kühlem (2025-09-16)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 语音与音频 → 输出: 虚拟人（脸 / 身体）, 对话 / 文本, 语音 / 声音
- 核心想法: 轮流发言的延迟是大语言模型角色最先破坏似真性的地方，因此为延迟做工程优化本身就是实验装置的一部分。
- 内容: 为 VR 博物馆中由大语言模型驱动的具身导览员设计的对话系统，缩短其响应延迟；导览员以语音和手势帮助参观者了解艺术品与艺术家。
- 实现方式: 针对端到端延迟优化的多模态智能体管线（语音识别、大语言模型、语音合成、手势），很可能通过各环节并行重叠来实现；关于参与度的后续研究发表于 IEEE AIxVR 2026。
- 能力维度: 时间响应性
- 论文: https://doi.org/10.1145/3717511.3749287 (IVA 2025)
- 视频: https://www.youtube.com/watch?v=kfjh-9yDeQQ

#### Inceptor：在虚拟现实中自动生成社会情境（Inceptor: Automated Generation of Social Scenarios in Virtual Reality） — Dan Pollak, Doron Friedman (2025-09-16)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 文字提示, 场景规格、代码与规则 → 输出: 人工制作的 VR 情境, 虚拟人（脸 / 身体）, 动作 / 动画
- 核心想法: 在实时大语言模型对话之前，批量生成接近人工制作水准的简短社会场景，已经让训练受益。
- 内容: 一条把文字情境描述转化为带动画虚拟角色的社会 VR 片段的流水线；在一个心理健康韧性训练项目中，它在短时间内生成了 32 个片段、总时长超过两小时，作者还测试了用大语言模型为角色挑选动画。
- 实现方式: 从脚本到多角色 VR 场景的自动化创作流程，已用于实际部署的韧性训练项目；作者称将以开源形式发布。
- 参数: 32 episodes · >2 h of content
- 能力维度: 创作可及性, 情境多样性
- 论文: https://doi.org/10.1145/3717511.3747061 (IVA 2025)
- 视频: https://www.youtube.com/watch?v=uUfgWLcIdaY

#### Milo：面向扩展现实的开源大语言模型虚拟人平台（Milo: an LLM-based virtual human open-source platform for extended reality） — Alon Shoa, Doron Friedman (2025-06-05)
- 类型: 开源工具 · 时序: 回合制 · 获取方式: 开源权重 / 代码
- 输入: 语音与音频, 身体、面部与视线追踪 → 输出: 虚拟人（脸 / 身体）, 对话 / 文本, 语音 / 声音
- 核心想法: 开放、由实验室掌控的虚拟人技术栈对研究很重要：一项研究可以锁定它实际使用的提示词、模型与行为管线。
- 内容: 开源系统，可把由大语言模型驱动的虚拟人接入 VR 与 AR 应用；论文展示了它作为单个对话智能体、多人 VR 会议参与者、VR 自我对话助手以及 AR 现场活动参与者的用法。
- 实现方式: 把语音识别、大语言模型、语音合成与化身动画集成到 XR 平台中的架构，并总结了多次部署的经验。
- 能力维度: 创作可及性, 反应性
- 论文: https://doi.org/10.3389/frvir.2025.1555173 (Frontiers in Virtual Reality 6 (2025))
- 图片: https://www.frontiersin.org/files/Articles/1555173/frvir-06-1555173-HTML/image_m/frvir-06-1555173-g001.jpg
- 代码: https://github.com/Advanced-Reality-Lab/Milo

#### AI 增强的虚拟现实自我对话用于心理咨询：一项形成性质性研究（AI-Enhanced Virtual Reality Self-Talk for Psychological Counseling: Formative Qualitative Study） — Moreah Zisquit, Doron Friedman, Mel Slater (2025-02-10)
- 类型: 行为研究 · 时序: 回合制
- 输入: 语音与音频, 身体、面部与视线追踪 → 输出: 虚拟人（脸 / 身体）, 对话 / 文本, 语音 / 声音
- 核心想法: 大语言模型不是取代治疗师，而是推动当事人自己的思考——这是生成式智能体在临床 VR 中风险较低的角色。
- 内容: 在 VR 具身自我对话（参与者在自己的化身与咨询者化身之间切换）中加入一个 AI 智能体，在参与者卡住时介入引导；一项形成性质性研究探讨了参与者如何体验这种帮助。
- 实现方式: 形成性质性研究，在 AI 辅助的 VR 自我对话后进行访谈，由赖克曼大学先进现实实验室与 Mel Slater 合作完成。
- 能力维度: 共创与能动性, 反应性
- 论文: https://doi.org/10.2196/67782 (JMIR Formative Research 9 (2025))

#### 探索用虚拟现实中的大语言模型聊天机器人训练自闭症人士的职场沟通技能（Exploring the Use of Large Language Model-Driven Chatbots in Virtual Reality to Train Autistic Individuals in Job Communication Skills） — Ziming Li (2024-05-11)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 语音与音频, 文字提示 → 输出: 虚拟人（脸 / 身体）, 对话 / 文本, 语音 / 声音
- 核心想法: 提示词取代了分支脚本，于是由辅导员而非开发者来编写情境——这是去掉了创作瓶颈的 VR-JIT 思路。
- 内容: 一款 VR 应用：自闭症受训者通过语音与 GPT-3.5 Turbo 驱动的化身练习与顾客对话，就业辅导员则通过撰写文字提示来创建训练情境；初步研究有三名受训者和两名就业辅导员参与。
- 实现方式: 为 VR 化身串联语音转文字、大语言模型生成回复与文字转语音，并进行初步可用性研究；罗切斯特理工学院团队随后把这条研究线扩展到与环境关联的角色扮演。
- 参数: 3 trainees · 2 job coaches
- 能力维度: 创作可及性, 反应性
- 论文: https://doi.org/10.1145/3613905.3651996 (CHI EA 2024)
- 视频: https://www.youtube.com/watch?v=p5zcxrxM8BQ

## 平台、API 与交付

构建与交付所需的一切：模型 API 与推理平台、实时智能体技术栈、引擎与泼溅渲染器、头显与显示设备，以及这个领域用来衡量自己的数据集与基准。

### 模型 API 与推理平台

开发者调用视频、三维、世界与虚拟人模型的地方：官方 API 以及 fal、Replicate 等托管平台。

#### World API — World Labs (2026-01-21)
- 类型: 平台 / API · 时序: 预先生成 · 获取方式: 公开 API
- 输入: 文字提示, 图像, 视频 → 输出: 高斯泼溅 / 辐射场, 三维场景 / 世界
- 核心想法: 把“搭建房间”变成一次返回显式三维世界的 API 调用：实验室可以生成同一场景的多种变体，再让每位被试面对完全相同的版本。
- 内容: World Labs 为 Marble 世界模型开放的公开 API：输入文字、一张或多张图片、360° 全景图或一段视频，就能得到可在浏览器中渲染、也可导出到其他工具的可漫游三维世界。World Labs 介绍的用例包括把二维电影变成可探索的空间（Escape.ai），以及为 Isaac Sim、MuJoCo 等机器人仿真器生成环境。
- 实现方式: 异步的世界生成请求调用 Marble，把输入提升为三维高斯泼溅场景，并可导出网格。
- 参数: inputs: text, image, multi-image, 360° panorama, video · output: Gaussian splats + mesh · launched 2026-01-21
- 能力维度: 创作可及性, 持久性, 情境可达性
- 视频: https://wlt-ai-cdn.art/videos/marble_labs/world-api.mp4
- 图片: https://www.worldlabs.ai/api/opengraph-image?imageUrl=/images/world-api.jpg&title=Announcing%20the%20World%20API
- 项目主页: https://www.worldlabs.ai/blog/announcing-the-world-api
- API 文档: https://docs.worldlabs.ai

#### Decart API Platform — Decart (2025)
- 类型: 平台 / API · 时序: 实时流式 · 获取方式: 公开 API
- 输入: 视频, 文字提示, 键盘与手柄动作 → 输出: 交互式帧流, 平面视频
- 核心想法: 按秒出售的实时生成，让“被生成式改写的实时环境”成了实验室可以租用、而不必自己训练的东西。
- 内容: Decart 的 API 提供实时生成视频流：Lucy 2.5 通过 WebRTC 实时编辑或重绘摄像头画面（替换人物、物体或背景），Oasis 3 Preview 世界模型则通过 gRPC 根据驾驶动作返回相机画面。按实际生成时长计费，截至 2026 年 10 月，720p 每秒 0.01–0.04 美元。
- 实现方式: 通过 WebRTC（Lucy）与 gRPC（Oasis）会话连接 Decart 托管的自回归视频模型，提供 JavaScript 与 Python SDK；Decart 称其模型运行在 AWS Trainium 3 上。
- 参数: Lucy 2.5: 720p, $0.02/s ($0.04/s fast mode) · Lucy Restyle 2: $0.01/s · Oasis 3 Preview: $0.02/s
- 能力维度: 时间响应性, 反应性
- 视频: https://www.youtube.com/watch?v=GXTOeJlDS9o
- 图片: https://cdn.prod.website-files.com/69a974f0b1fffb03644ecf2c/69b94eac7c2b44111d02c52d_og.jpg
- 项目主页: https://platform.decart.ai
- API 文档: https://docs.platform.decart.ai

#### OpenAI 视频 API（Sora 2）（OpenAI Videos API (Sora 2)） — OpenAI (2025-10-06)
- 类型: 平台 / API · 时序: 预先生成 · 获取方式: 公开 API
- 输入: 文字提示, 图像, 视频 → 输出: 平面视频, 音效、音乐与空间音频
- 核心想法: 可以通过 API 调用、按快照锁定版本的前沿视频模型，直到厂商将其撤下：依赖托管生成器的研究，可能在某个确定日期失去刺激材料的来源。
- 内容: OpenAI 的 v1/videos 接口通过公开 API 提供 Sora 2 与 Sora 2 Pro，开发者可以生成、改写、延长和编辑带同步声音的视频片段。OpenAI 已于 2026-09-24 从 API 中下线 Videos API 及全部 Sora 2 快照，没有替代接口。
- 实现方式: 异步 REST 任务（POST /v1/videos），由 OpenAI 的 Sora 2 模型渲染（架构未公开，很可能与第一代 Sora 一样是扩散 Transformer）；2026 年 3 月加入角色参考、视频延长、编辑与 Batch API 支持。
- 参数: sora-2 / sora-2-pro · up to 20 s · 1080p on sora-2-pro ($0.70/s) · launched 2025-10-06 · removed 2026-09-24
- 能力维度: 创作可及性, 实验控制
- 视频: https://www.youtube.com/watch?v=hS1YqcewH0c
- 项目主页: https://developers.openai.com/api/docs/deprecations
- API 文档: https://developers.openai.com/api/docs/guides/video-generation

#### Gemini API 视频生成（Veo / Omni）（Gemini API video generation (Veo, Omni)） — 谷歌, 谷歌 DeepMind (2025-04-09)
- 类型: 平台 / API · 时序: 预先生成 · 获取方式: 公开 API
- 输入: 文字提示, 图像, 视频 → 输出: 平面视频, 音效、音乐与空间音频
- 核心想法: 对实验室来说最完整的托管视频技术栈：模型 ID 可以锁定，从预览到正式发布的生命周期可以追踪，下线通知也会提前告诉你某个刺激生成模型何时停用。
- 内容: Google 的 Gemini API 与 Vertex AI（2026 年文档中称 Gemini Enterprise Agent Platform）以带版本号的接口提供 DeepMind 视频模型：2025 年 4 月起提供 Veo 2，之后是带原生音频的 Veo 3 与 3.1，2026 年 1 月起支持 4K 输出，2026 年 3 月推出 Veo 3.1 Lite。2026 年 Google 又加入了可对话式生成与编辑视频的 Gemini Omni Flash（2026-06-30 预览，2026-08-27 正式发布）。
- 实现方式: 通过长时运行的预测操作调用 veo-3.1-generate-preview、gemini-omni-1.1-flash 等模型 ID；Google 会给 Veo 输出加上 SynthID 水印。
- 参数: Veo 3.1: 4 / 6 / 8 s · 720p–4K · native audio · Omni Flash: 360p–4K, extend, first + last frame
- 能力维度: 创作可及性, 实验控制
- 视频: https://www.youtube.com/watch?v=Co-97Ht5vAY
- 图片: https://ai.google.dev/static/site-assets/images/share-gemini-api-2026-07.png
- 项目主页: https://ai.google.dev/gemini-api/docs/changelog
- API 文档: https://ai.google.dev/gemini-api/docs/video

#### 可灵 AI 开放平台 API（Kling AI API (KlingAI Open Platform)） — 快手 / 可灵 (2024)
- 类型: 平台 / API · 时序: 预先生成 · 获取方式: 公开 API
- 输入: 文字提示, 图像, 视频 → 输出: 平面视频, 图像 / 全景图
- 核心想法: 让中国的前沿视频模型拥有与 Veo、Ray 同类的版本化 API，跨机构比较刺激材料时不必再通过消费级应用。
- 内容: 快手的可灵 AI 开放平台为开发者提供可灵视频与图像模型的 API，附有各模型的参考文档与计费单价。与 fal 等转售平台一起，它是中国前沿视频模型进入全球第三方应用的主要途径之一。
- 实现方式: 以访问密钥签名的异步 REST 任务（文生视频、图生视频、视频延长），结果以托管视频链接返回。
- 参数: API since 2024 · v1.5 1080p professional mode and video extension added 2024-11
- 能力维度: 创作可及性, 感知真实感
- 视频: https://www.youtube.com/watch?v=mT5aHJxnqx0
- 项目主页: https://app.klingai.com/global/dev/document-api/quickStart/productIntroduction/overview
- API 文档: https://app.klingai.com/global/dev/document-api/quickStart/productIntroduction/overview

#### Luma API (Ray) — Luma AI (2024)
- 类型: 平台 / API · 时序: 预先生成 · 获取方式: 公开 API
- 输入: 文字提示, 图像, 视频 → 输出: 平面视频, 图像 / 全景图
- 核心想法: 通过 API 实现关键帧级控制，视频模型才成为实验者可以逐个镜头编排的工具。
- 内容: Luma 的 API 向开发者提供 Ray 视频模型与 Photon 图像模型。Ray3.2 API（2026-06-09）开放了模型的全部控制项：单个片段最多 16 个关键帧、表演追踪、HDR 生成与 EXR 导出。
- 实现方式: 在 Luma 的 Ray 视频模型上运行异步生成任务，支持多关键帧条件、视频到视频与重新构图等接口。
- 参数: Ray3.2 API (2026-06-09) · up to 16 keyframes per clip · HDR · EXR export
- 能力维度: 实验控制, 创作可及性
- 视频: https://www.youtube.com/watch?v=YawXSpOlzgw
- 图片: https://cdn.sanity.io/images/2ylxvaa2/production/ff7469d468f6f7e447ccb4a50276f1cb03c6664d-1200x630.jpg?w=1200&h=630&fm=jpg
- 项目主页: https://lumalabs.ai/api
- API 文档: https://docs.lumalabs.ai

#### Runway API (Runway Dev) — Runway (2024-09)
- 类型: 平台 / API · 时序: 预先生成 · 获取方式: 公开 API
- 输入: 文字提示, 图像, 视频 → 输出: 平面视频, 虚拟人（脸 / 身体）, 音效、音乐与空间音频
- 核心想法: 一次接入就能同时覆盖预渲染片段与实时对话角色，研究可以在离线刺激与实时刺激之间切换，而不必更换供应商。
- 内容: Runway 的开发者平台通过一个 API 提供自家及其他机构的视频、图像与音频模型，并配有模型路由、可复用工作流和实时对话角色“Characters”。2026 年 5 月，Runway 举办了首届线上 API 黑客松，主题是实时视频智能体。
- 实现方式: 带 SDK 的 REST 任务 API；路由器按成本、延迟或质量偏好为每个请求选择模型，Characters 以实时流方式输出（很可能基于 WebRTC）。
- 参数: launched 2024-09 · credit-based billing · model router · real-time Characters
- 能力维度: 创作可及性, 时间响应性
- 视频: https://www.youtube.com/watch?v=rV81E4TntkI
- 图片: https://d3phaj0sisr2ct.cloudfront.net/devportal/og-image-v4.jpg
- 项目主页: https://runwayml.com/api
- API 文档: https://docs.dev.runwayml.com/

#### fal — fal (2023)
- 类型: 平台 / API · 时序: 预先生成 · 获取方式: 公开 API
- 输入: 文字提示, 图像, 视频 → 输出: 平面视频, 网格 / 三维资产, 音效、音乐与空间音频
- 核心想法: 实验室只需改一个参数就能更换刺激生成流程背后的模型，比较模型的成本很低，但可复现性也因此取决于第三方平台的模型目录。
- 内容: 生成式媒体推理平台：一个 API 和 SDK 即可调用来自多家机构的 1,000 多个图像、视频、音频与三维模型（可灵、Seedance、MiniMax、FLUX 以及开源权重模型），也可以用 Serverless GPU 部署自己的模型。截至 2026 年 10 月，fal 称其开发者超过 150 万。
- 实现方式: 在 H100、H200、B200 集群的优化推理之上，提供排队与流式的 HTTP / WebSocket 接口；自定义模型以 Serverless 应用形式部署。
- 参数: 1,000+ models · billed per output · serverless and dedicated GPUs
- 能力维度: 创作可及性, 时间响应性
- 视频: https://www.youtube.com/watch?v=fcBfGnpUKjI
- 图片: https://fal.ai/og-thumbnail.webp
- 项目主页: https://fal.ai
- API 文档: https://docs.fal.ai
- 代码: https://github.com/fal-ai/fal

#### 火山方舟 / BytePlus ModelArk（Volcano Engine Ark / BytePlus ModelArk） — 火山引擎 (2023-06-28)
- 类型: 平台 / API · 时序: 预先生成 · 获取方式: 公开 API
- 输入: 文字提示, 图像 → 输出: 平面视频, 对话 / 文本
- 核心想法: 调用字节跳动 Seedance 模型的官方途径；当研究需要一个可签约、稳定的接口时，企业级条款很关键。
- 内容: 字节跳动的模型即服务平台（国内为火山方舟，海外为 BytePlus ModelArk）通过 API 提供豆包大语言模型与 Seedance 视频模型。2025 年 BytePlus 在 ModelArk 上为 Seedance 1.0 Pro 加入首尾帧控制，2026 年又上架 Seedance 2.0 与 2.5。
- 实现方式: 托管推理接口，提供 REST API、模型版本与配额管理；视频任务异步执行，返回托管的 MP4 文件。
- 参数: launched 2023-06-28 (China) · Seedance 1.0 Pro first/last-frame control (2025) · Seedance 2.0 / 2.5 (2026)
- 能力维度: 创作可及性, 实验控制
- 视频: https://www.youtube.com/watch?v=pBUvj5USz1Y
- 项目主页: https://www.volcengine.com/product/ark
- API 文档: https://docs.byteplus.com/en/docs/ModelArk

#### Replicate — Replicate (2021)
- 类型: 平台 / API · 时序: 预先生成 · 获取方式: 公开 API, 开源权重 / 代码
- 输入: 文字提示, 图像, 视频 → 输出: 平面视频, 网格 / 三维资产, 图像 / 全景图
- 核心想法: 每个模型都有版本 ID，在这里锁定研究所用的确切生成器相对容易。
- 内容: 通过一个 API 运行数千个开源与闭源模型，每个模型都以版本 ID 调用；开发者也可以用开源的 Cog 容器格式打包并发布自己的模型。Replicate 于 2025-11-17 宣布并入 Cloudflare，品牌与 API 保持不变。
- 实现方式: 以 Cog 容器打包的模型运行在 Replicate 的 GPU 集群上；每次预测都是一个按模型版本寻址的 HTTP 任务。
- 参数: thousands of models · per-second GPU or per-output billing · joining Cloudflare (announced 2025-11-17)
- 能力维度: 实验控制, 创作可及性
- 视频: https://www.youtube.com/watch?v=VmYYcGtbF8E
- 图片: https://replicate.com/blog/replicate-cloudflare.png
- 项目主页: https://replicate.com/blog/replicate-cloudflare
- API 文档: https://replicate.com/docs
- 代码: https://github.com/replicate/cog

### 实时媒体与智能体技术栈

承载全双工交互的 WebRTC、语音智能体与流媒体框架。

#### 声网对话式 AI 引擎（Agora Conversational AI Engine） — 声网 (2025-04)
- 类型: 平台 / API · 时序: 全双工 · 获取方式: 公开 API
- 输入: 语音与音频, 文字提示 → 输出: 语音 / 声音, 对话 / 文本, 虚拟人（脸 / 身体）
- 核心想法: 一旦虚拟人走出实验室，网络层面的稳定性（丢包、嘈杂环境）与模型延迟同样重要。
- 内容: 一项托管服务，把语音智能体放进声网的实时频道：开发者自选大语言模型与语音合成，声网负责在其全球网络上传输音频，并处理降噪、打断与话轮。同一频道还能接入合作厂商的数字人形象。
- 实现方式: 通过 REST 调用启动智能体，它加入声网 SD-RTN 频道，在托管流水线中运行语音识别、大语言模型与语音合成（或语音到语音模型），再把语音推回频道。
- 参数: launched 2025 · bring-your-own LLM and TTS · Agora SD-RTN global network
- 能力维度: 时间响应性, 反应性
- 视频: https://www.youtube.com/watch?v=B0nacrYT5bU
- 图片: https://cdn.prod.website-files.com/661e75fc70756be16764754b/6a5f42861fc82c4cd5e27a2f_Products%20_%20Conversational%20AI%20Engine.png
- 项目主页: https://www.agora.io/en/products/conversational-ai-engine/
- API 文档: https://docs.agora.io/en/conversational-ai/overview/product-overview

#### Gemini Live API — 谷歌, 谷歌 DeepMind (2024-12-11)
- 类型: 平台 / API · 时序: 全双工 · 获取方式: 公开 API
- 输入: 语音与音频, 视频, 文字提示 → 输出: 语音 / 声音, 对话 / 文本
- 核心想法: 它在说话的同时也在看画面，因此不仅能回应被试说了什么，还能回应被试在镜头前做了什么。
- 内容: Google 面向“语音 + 视觉”智能体的双向流式 API：应用通过 WebSocket 把麦克风音频与摄像头或屏幕画面实时传给 Gemini，并收到可被用户打断的语音回复。它于 2024 年 12 月随 Gemini 2.0 以 Multimodal Live API 之名推出；自 2026-09-15 起，默认模型为 Gemini 3.8 Live 与 Gemini 3.8 Live Extended Thinking，支持异步函数调用与主动音频。
- 实现方式: 与原生音频到音频 Gemini 模型建立有状态 WebSocket 会话，支持语音活动检测、会话恢复、上下文压缩与工具调用；临时令牌允许浏览器直接连接。
- 参数: audio + video in · audio out · GA models gemini-3.8-live and gemini-3.8-live-extended-thinking (2026-09-15)
- 能力维度: 时间响应性, 反应性
- 视频: https://www.youtube.com/watch?v=3CyW24Pkz4o
- 项目主页: https://ai.google.dev/gemini-api/docs/live-api
- API 文档: https://ai.google.dev/gemini-api/docs/live-api

#### OpenAI Realtime API 与 GPT-Live（OpenAI Realtime API and GPT-Live） — OpenAI (2024-10-01)
- 类型: 平台 / API · 时序: 全双工 · 获取方式: 公开 API
- 输入: 语音与音频, 文字提示, 图像 → 输出: 语音 / 声音, 对话 / 文本
- 核心想法: 把维持对话的声音与决定角色行为的推理分开，这正是一个反应灵敏的虚拟实验同谋所需要的架构。
- 内容: OpenAI 的低延迟语音到语音接口，支持 WebRTC、WebSocket 或 SIP：2024 年 DevDay 推出测试版，2025-08-28 随 gpt-realtime 正式发布，之后有 gpt-realtime-2（2026-05-07）与 2.1（2026-07-06）。2026-09-10，OpenAI 正式发布 GPT-Live 1：一个全双工语音层，在后台模型或智能体调用工具时仍能继续对话（称为“委托”）。
- 实现方式: 持久会话把音频持续送入并取出原生音频模型；服务器端语音活动检测负责话轮与打断，函数调用或委托给后台的任务在语音继续时并行执行。
- 参数: WebRTC / WebSocket / SIP · beta 2024-10-01 · GA 2025-08-28 · beta interface removed 2026-05-12 · GPT-Live 1 GA 2026-09-10
- 能力维度: 时间响应性, 反应性
- 视频: https://www.youtube.com/watch?v=qGS9Ghnq1RU
- 项目主页: https://developers.openai.com/api/docs/guides/realtime
- API 文档: https://developers.openai.com/api/docs/guides/live

#### TEN Framework — 声网 (2024-06)
- 类型: 开源工具 · 时序: 全双工 · 获取方式: 开源权重 / 代码
- 输入: 语音与音频, 视频, 文字提示 → 输出: 语音 / 声音, 对话 / 文本, 虚拟人（脸 / 身体）
- 核心想法: 开源的话轮检测与语音活动检测模型很重要，因为虚拟人何时开口，本身就是一个实验变量。
- 内容: 由声网及社区支持的开源框架，用于构建实时多模态对话智能体。它提供 TEN Agent 示例、自研的语音活动检测与话轮检测模型，以及 RTC 与 WebSocket 传输连接器；最新版本为 0.11.73（2026-09-22）。
- 实现方式: 由 C++、Go、Python 或 Node.js 编写的扩展组成图，在同一运行时内以低开销交换音频、视频与数据消息。
- 参数: ~11.2k GitHub stars (Oct 2026) · TEN VAD and TEN Turn Detection models · RTC and WebSocket
- 能力维度: 时间响应性, 实验控制
- 视频: https://www.youtube.com/watch?v=yYg07CbPZfg
- 图片: https://opengraph.githubassets.com/1/TEN-framework/ten-framework
- 项目主页: https://theten.ai/
- 代码: https://github.com/TEN-framework/ten-framework

#### Pipecat — Daily (2024-05)
- 类型: 开源工具 · 时序: 全双工 · 获取方式: 开源权重 / 代码, 公开 API
- 输入: 语音与音频, 视频, 文字提示 → 输出: 语音 / 声音, 对话 / 文本, 虚拟人（脸 / 身体）
- 核心想法: 帧级流水线让对话刺激的每个环节都清晰可见、可替换；当研究需要报告每一部分由哪个模型生成时，这一点很有用。
- 内容: 由 Daily 维护的开源 Python 框架，用于搭建语音与多模态智能体：数据帧依次流经语音、大语言模型、视频与虚拟人等服务。Pipecat Flows 提供结构化的对话图，Pipecat Cloud 负责托管。Pipecat 1.0 于 2026-04-14 发布，1.12 于 2026-09-26 发布。
- 实现方式: 由处理器组成的异步流水线，通过 Daily WebRTC、WebSocket 或电话等传输层交换音频、视频、文本与控制帧；Flows 负责描述对话状态与转移。
- 参数: ~16.6k GitHub stars (Oct 2026) · v1.0.0 on 2026-04-14 · v1.12.0 on 2026-09-26
- 能力维度: 时间响应性, 实验控制
- 视频: https://www.youtube.com/watch?v=tAQW319_h-s
- 图片: https://opengraph.githubassets.com/1/pipecat-ai/pipecat
- 项目主页: https://docs.pipecat.ai/getting-started/introduction
- API 文档: https://docs.pipecat.ai
- 代码: https://github.com/pipecat-ai/pipecat

#### LiveKit Agents — LiveKit (2023-11)
- 类型: 开源工具 · 时序: 全双工 · 获取方式: 开源权重 / 代码, 公开 API
- 输入: 语音与音频, 视频, 文字提示 → 输出: 语音 / 声音, 对话 / 文本, 虚拟人（脸 / 身体）
- 核心想法: 这套底层管线让研究者可以更换虚拟人的声音、模型或形象，同时保持同样的房间、日志与时序行为。
- 内容: 开源的实时语音、视频与物理 AI 智能体框架，智能体以参与者身份加入 LiveKit WebRTC 房间。它把语音识别、大语言模型、语音合成（或语音到语音模型）以及虚拟人服务串进同一会话，并提供话轮检测、打断处理、电话接入与评测工具；1.0 版于 2025-04-10 发布，1.8.8 版于 2026-10-15 发布，LiveKit Cloud 负责托管部署。
- 实现方式: Python 与 Node.js 工作进程通过 WebRTC 连接 LiveKit 媒体服务器；每段对话由插件流水线（语音识别、大语言模型、语音合成、语音活动检测与 Transformer 话轮检测模型）或实时模型处理。
- 参数: ~14.8k GitHub stars (Oct 2026) · 1.0 on 2025-04-10 · 1.8.8 on 2026-10-15
- 能力维度: 时间响应性, 实验控制
- 视频: https://www.youtube.com/watch?v=OZG0oZKctgw
- 图片: https://livekit.com/opengraph-image.png?opengraph-image.10qgazecccxaz.png
- 项目主页: https://docs.livekit.io/agents/
- API 文档: https://docs.livekit.io/agents/
- 代码: https://github.com/livekit/agents

### 引擎、运行时与查看器

把生成内容呈现给人的游戏引擎、WebXR 与泼溅渲染器。

#### Roblox Build 与 AI 创作工具（Roblox Build and AI creation tools） — Roblox (2026-09-11)
- 类型: 平台 / API · 时序: 回合制 · 获取方式: 产品 / 应用, 候补 / 抢先体验
- 输入: 文字提示, 图像 → 输出: 三维场景 / 世界, 网格 / 三维资产, 智能体行为与动作
- 核心想法: 在一个每季度 290 亿小时游玩时长的平台上用提示词做游戏，意味着生成的情境能大规模触达玩家：它既是工具，也是招募被试、提升生态效度的渠道。
- 内容: 在 RDC 2026（2026-09-11）上，Roblox 介绍了建在引擎之上的“AI 创作层”：Build 是 Roblox 应用里的一个标签页，任何人都能用提示词做游戏（新西兰内测期间已发布约 9,000 款，现扩展到塞尔维亚和新加坡）；Scene Generator 将于 2026 年晚些时候推出，可把文字提示加参考图变成可在 Studio 中继续编辑的功能性布局。它们与 Studio 的 Assistant 以及开源的 Cube 3D 模型并列。
- 实现方式: 大语言模型智能体与生成式三维模型（Cube）很可能在 Roblox 引擎与云服务中生成 Luau 脚本、资源与布局；游戏可即时发布到 Roblox 的多人在线基础设施上。
- 参数: Build alpha: ~9,000 games by 2026-09-01; 71% of Build creators had never used Studio · Scene Generator: later 2026
- 能力维度: 创作可及性, 共创与能动性
- 视频: https://www.youtube.com/watch?v=AD3I2Vw7l5M
- 图片: https://cms-media.roblox.com/assets/ced9560d-5aa5-42d3-b5d8-8e70abeac00c.png
- 项目主页: https://corp.roblox.com/newsroom/2026/09/rdc-2026-the-world-needs-more-play

#### glTF 高斯泼溅扩展（KHR_gaussian_splatting）（glTF Gaussian Splatting extension (KHR_gaussian_splatting)） — The Khronos Group (2026-02-03)
- 类型: 平台 / API · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入:  → 输出: 高斯泼溅 / 辐射场
- 核心想法: 有了共享的文件格式，生成的世界才能原封不动地从生成它的模型，转到运行研究的任意引擎中。
- 内容: Khronos 的一项扩展，把三维高斯泼溅（位置、旋转、缩放、不透明度与球谐颜色）存为 glTF 2.0 网格图元，为引擎与查看器提供共同的基础格式。Khronos 于 2026-02-03 发布候选版本征求业界意见；截至 2026 年 10 月，规范已标记为完成并获批准，压缩则留给后续扩展。
- 实现方式: 在 glTF 网格图元上为高斯参数增加逐点属性，并规定渲染模型，使泼溅场景可以沿用标准 glTF 工具链。
- 参数: release candidate 2026-02-03 · ratified (status as of Oct 2026) · glTF 2.0 · uncompressed baseline
- 能力维度: 实验控制, 创作可及性
- 视频: https://www.youtube.com/watch?v=EEFIxtBRRBo
- 图片: https://www.khronos.org/assets/uploads/apis/gltf-Square.png
- 项目主页: https://www.khronos.org/news/press/gltf-gaussian-splatting-press-release
- 代码: https://github.com/KhronosGroup/glTF/tree/main/extensions/2.0/Khronos/KHR_gaussian_splatting

#### Immersive Web SDK（沉浸式网页 SDK）（Immersive Web SDK (IWSDK)） — Meta (2025)
- 类型: 开源工具 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 场景规格、代码与规则, 身体、面部与视线追踪 → 输出: 三维场景 / 世界
- 核心想法: XR 场景可由智能体直接操作，意味着大语言模型不仅能为研究环境写代码，还能从头到尾搭建并测试它。
- 内容: Meta 基于 Three.js 的开源 WebXR 应用框架：实体组件运行时，内置抓取交互、移动、空间音频、物理、场景理解与类 HTML 语法的空间界面，并配有 Spatial Editor。截至 2026 年 10 月，其官网称之为“AI 原生”：编程智能体可以截图、发送手柄输入、检查正在运行的 XR 场景并调试。
- 实现方式: 实体组件架构之下的 Three.js 渲染器，用 UIKitML 编写空间界面，并提供供智能体检查场景、模拟输入的工具接口。
- 参数: v1.0.1 · Three.js-based · Spatial Editor
- 能力维度: 创作可及性
- 视频: https://www.youtube.com/watch?v=d1PwLkvgP7A
- 图片: https://opengraph.githubassets.com/1/facebook/immersive-web-sdk
- 项目主页: https://iwsdk.dev/
- 代码: https://github.com/facebook/immersive-web-sdk

#### Unity AI 工具（Unity AI tools (Unity AI)） — Unity (2025-08)
- 类型: 平台 / API · 时序: 回合制 · 获取方式: 产品 / 应用, 候补 / 抢先体验
- 输入: 文字提示, 图像, 场景规格、代码与规则 → 输出: 三维场景 / 世界, 网格 / 三维资产
- 核心想法: 当智能体可以直接修改场景图时，情境脚本与它的三维实现就能在同一段对话中一起修改。
- 内容: Unity 为自家引擎提供的 AI 工具：能读取当前场景并执行编辑器操作的智能体助手、AI 网关、MCP 服务器与命令行工具，以及面向 Claude Code、Codex 和 Grok 的官方插件。Unity AI 公开测试于 2026-05-04 向所有 Unity 6 及以上版本开发者开放；此后 Unity 不再使用“Unity AI”这一品牌名，并于 2026-10-07 宣布推出无需写代码、用提示词做游戏的 Unity Spark（封闭测试）。
- 实现方式: 一个掌握 Unity 专用工具与项目上下文（场景层级、组件、资源）的大语言模型智能体发出编辑器指令；外部智能体通过 Unity CLI 以 MCP 接入。
- 参数: Unity 6+ · CLI, MCP server and plugins free · in-editor assistant in Pro / Enterprise / Industry, $10/month for Personal after trial · open beta 2026-05-04
- 能力维度: 创作可及性
- 视频: https://www.youtube.com/watch?v=pHRZm2BwNQc
- 图片: https://cdn.sanity.io/images/fuvbjjlp/production/b55d23a7301a66deab7adb111442c13cb6510919-3840x2160.png
- 项目主页: https://unity.com/products/ai

#### NVIDIA Omniverse NuRec 神经重建（NVIDIA Omniverse NuRec） — 英伟达 (2025-06)
- 类型: 平台 / API · 时序: 预先生成 · 获取方式: 产品 / 应用
- 输入: 多视角拍摄 / 扫描, 视频 → 输出: 高斯泼溅 / 辐射场, 三维场景 / 世界
- 核心想法: 从真实地点到可控仿真的一条路径：把场地重建一次，再让生成模型改变条件，而几何结构保持不变。
- 内容: NVIDIA 面向 Omniverse 的神经重建库：把相机与激光雷达采集的数据重建为以 OpenUSD 打包的三维高斯泼溅场景，并在仿真器（Isaac Sim、CARLA、AlpaSim）中渲染。NVIDIA 还把 NuRec 与 Cosmos 世界模型配合使用，为重建场景生成各种变化。
- 实现方式: 从多传感器记录中进行高斯泼溅重建（据 NVIDIA 介绍基于开源 gsplat），并通过 NCore 数据标准连同轨迹导出为 OpenUSD。
- 参数: OpenUSD output · camera + lidar input · integrations: Isaac Sim, CARLA, AlpaSim
- 能力维度: 感知真实感, 情境可达性, 实验控制
- 视频: https://www.youtube.com/watch?v=e3dfXj6ATA0
- 项目主页: https://developer.nvidia.com/omniverse/nurec

#### Android XR SDK (Jetpack XR) — 谷歌 (2024-12-12)
- 类型: 平台 / API · 时序: 实时流式 · 获取方式: 候补 / 抢先体验
- 输入: 身体、面部与视线追踪, 透视画面与实时环境, 语音与音频 → 输出: 三维场景 / 世界
- 核心想法: 同一套 Android 工具链覆盖头显与眼镜，研究应用可以从完全沉浸一路延伸到抬头显示的叠加界面。
- 内容: Google 面向 Android XR 应用的 SDK，覆盖头显（Galaxy XR）、有线 XR 眼镜（XREAL AURA）与 AI 眼镜：包括 Jetpack Compose for XR、SceneCore、ARCore for Jetpack XR（带语义标签的平面与物体追踪），以及 Unity、OpenXR 与 WebXR 的开发路径。截至 2026 年 10 月，它处于开发者预览第 4 版。
- 实现方式: 基于 OpenXR 感知栈的 Kotlin Jetpack 库，设备上的应用还可调用 Gemini API。
- 参数: Developer Preview 4 (2026) · targets Galaxy XR, XREAL AURA, AI glasses · Unity / OpenXR / WebXR
- 能力维度: 创作可及性, 情境可达性
- 视频: https://www.youtube.com/watch?v=otzSN5pSNZk
- 项目主页: https://developer.android.com/develop/xr
- API 文档: https://developer.android.com/develop/xr/jetpack-xr-sdk

#### Meta Spatial SDK — Meta (2024-09-25)
- 类型: 平台 / API · 时序: 实时流式 · 获取方式: 产品 / 应用
- 输入: 身体、面部与视线追踪, 透视画面与实时环境, 场景规格、代码与规则 → 输出: 三维场景 / 世界
- 核心想法: 把开发一款混合现实研究应用的成本降到与 Android 应用相当，还能访问头显摄像头，让 AI 读取被试所处的环境。
- 内容: Meta 推出的 Kotlin / Android 框架，无需游戏引擎即可开发 Quest 上的 Horizon OS 应用：在一个实体组件运行时中整合二维 Android 面板、三维 glTF 内容、混合现实场景理解与透视摄像头访问，并配有桌面端 Spatial Editor。移动开发者可以借此为现有应用加入混合现实功能，包括读取透视摄像头画面的 AI。
- 实现方式: 实体组件系统场景图，配合基于物理的渲染器、Android Activity 生命周期以及 Horizon OS 混合现实 API（场景、锚点、透视摄像头）。
- 参数: Kotlin / Android · Quest 3 and 3S · Spatial Editor · announced 2024-09-25
- 能力维度: 创作可及性, 情境可达性
- 视频: https://www.youtube.com/watch?v=6aKbrPp09jo
- 图片: https://opengraph.githubassets.com/1/meta-quest/Meta-Spatial-SDK-Samples
- 项目主页: https://github.com/meta-quest/Meta-Spatial-SDK-Samples
- 代码: https://github.com/meta-quest/Meta-Spatial-SDK-Samples

#### Unreal Engine 5 — Epic Games (2022-04-05)
- 类型: 平台 / API · 时序: 实时流式 · 获取方式: 产品 / 应用
- 输入: 场景规格、代码与规则, 视频 → 输出: 三维场景 / 世界, 虚拟人（脸 / 身体）, 动作 / 动画
- 核心想法: 为生成内容提供照片级、可确定复现的运行环境：生成层可以放在 MetaHuman 与脚本里，时序与日志则由引擎精确保证。
- 内容: Epic 的实时引擎，许多高保真 VR 研究与虚拟制片舞台都用它，具备 Nanite 几何、Lumen 光照与 MetaHuman 数字人。Unreal Engine 5.8（2026-06-23）加入了可生成数百人群的 MetaHuman Collections、用网络摄像头即可完成的全身无标记 MetaHuman 动捕、以 MIT 许可开源的 OpenRigLogic，以及一个实验性 MCP 插件，让任意大语言模型都能查看并操控编辑器。
- 实现方式: C++ 引擎，配有 Blueprint 可视化脚本；Nanite 虚拟化几何与 Lumen 全局光照实时渲染，MetaHuman 工具为扫描或生成的角色绑定骨骼并驱动动画。
- 参数: UE 5.0 released 2022-04-05 · UE 5.8 released 2026-06-23 · free, 5% royalty above $1M gross for games
- 能力维度: 感知真实感, 创作可及性, 实验控制
- 视频: https://www.youtube.com/watch?v=ExFF5gXVhDU
- 图片: https://cms-assets.unrealengine.com/AiKUh5PQCTaOFnmJDZJBfz/resize=width:1200/cmqhyducc6qq007n7n99x5sjf
- 项目主页: https://www.unrealengine.com/en-US/news/unreal-engine-5-8-is-now-available

#### WebXR 设备 API（WebXR Device API） — W3C Immersive Web Working Group (2019)
- 类型: 平台 / API · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 身体、面部与视线追踪, 透视画面与实时环境, 键盘与手柄动作 → 输出: 三维场景 / 世界, 360° / 立体视频
- 核心想法: 生成场景门槛最低的交付方式：一个能在头显中打开的网址，这也让远程与大样本 XR 研究变得可行。
- 内容: W3C 的网页标准，让网页可以在头显和手机上开启沉浸式 VR 与 AR 会话，提供位姿追踪、手柄与手势输入，以及用于命中测试、锚点和深度的 AR 模块。Chromium 系浏览器（包括 Meta Quest 浏览器与 Android XR 上的 Chrome）以及 visionOS 上的 Safari 都已实现；核心规范为 W3C 候选推荐草案，最新版本日期为 2026-06-09。
- 实现方式: 一个 JavaScript API，逐帧提供观察者与输入设备的位姿，以及可供渲染的 XR 兼容 WebGL / WebGPU 图层；功能模块补充 AR 能力。
- 参数: W3C Candidate Recommendation Draft (2026-06-09) · editors from Google and Meta
- 能力维度: 情境可达性, 创作可及性
- 视频: https://www.youtube.com/watch?v=C3XDHjam-eI
- 图片: https://opengraph.githubassets.com/1/immersive-web/webxr
- 项目主页: https://www.w3.org/TR/webxr/
- API 文档: https://www.w3.org/TR/webxr/
- 代码: https://github.com/immersive-web/webxr

#### PlayCanvas Engine — PlayCanvas (2014)
- 类型: 开源工具 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 场景规格、代码与规则 → 输出: 高斯泼溅 / 辐射场, 三维场景 / 世界
- 核心想法: 生成的世界可以以链接形式交付：被试在电脑或头显浏览器中直接打开泼溅场景，无需安装任何东西。
- 内容: 以 MIT 许可开源的网页图形运行时（WebGL、WebGPU、WebXR、glTF），已成为浏览器中渲染高斯泼溅的主要引擎之一；隶属 Snap 的 PlayCanvas 还开发了 SuperSplat 编辑器。引擎 2.20 版（2026 年 6 月）加入了泼溅重打光、软阴影与景深、数十亿泼溅点场景的流式加载，以及基于 WebGPU 的 WebXR。
- 实现方式: JavaScript / TypeScript 引擎，采用实体组件系统，带有在 GPU 上排序并光栅化高斯的泼溅渲染器，并支持 WebXR 会话。
- 参数: MIT · ~17k GitHub stars (Oct 2026) · v2.20 (2026-06) · billions of splats via streaming (PlayCanvas claim)
- 能力维度: 感知真实感, 创作可及性
- 视频: https://www.youtube.com/watch?v=gsLkNo-PBF4
- 图片: https://playcanvas.com/assets/images/og/playcanvas.png
- 项目主页: https://playcanvas.com
- 代码: https://github.com/playcanvas/engine

#### Babylon.js — 微软 (2013)
- 类型: 开源工具 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 场景规格、代码与规则 → 输出: 三维场景 / 世界, 高斯泼溅 / 辐射场
- 核心想法: 另一款成熟的开源网页引擎，可交付泼溅与 WebXR 内容；当研究需要在浏览器中呈现三维内容、又不想绑定单一厂商时很有用。
- 内容: 微软以 Apache-2.0 许可开源的网页 JavaScript 渲染与游戏引擎，支持 WebXR、WebGPU 与高斯泼溅。Babylon.js 9.0 于 2026-03-26 发布。
- 实现方式: TypeScript 引擎，带节点式材质编辑器、物理、WebXR 体验辅助工具与泼溅渲染器，运行于 WebGL2 或 WebGPU。
- 参数: Apache-2.0 · ~26k GitHub stars (Oct 2026) · v9.0 (2026-03-26)
- 能力维度: 创作可及性, 感知真实感
- 视频: https://www.youtube.com/watch?v=Th9mD_D5DrQ
- 图片: https://www.babylonjs.com/assets/videos/newGaussianSplat.jpg
- 项目主页: https://www.babylonjs.com
- API 文档: https://doc.babylonjs.com
- 代码: https://github.com/BabylonJS/Babylon.js

### 头显、眼镜与显示设备

生成世界最终运行的硬件。

#### Steam Frame — Valve (2025-11-12)
- 类型: 设备 · 获取方式: 产品 / 应用
- 输入: 身体、面部与视线追踪, 键盘与手柄动作 → 输出: 三维场景 / 世界, 人工制作的 VR 情境
- 核心想法: 无线 PC 串流让头显可以显示由台式机 GPU 生成的世界；在实时世界模型仍需工作站或数据中心硬件的阶段，这一点很重要。
- 内容: Valve 的一体式、以串流为主的 VR 头显，2025-11-12 发布，2026 年 9 月开售（256 GB 版 1,059 美元，1 TB 版 1,299 美元）。它在骁龙 8 Gen 3 上运行 SteamOS，并通过眼动追踪注视点串流无线传输 PC VR 画面；它本身不带生成式功能，但能把 PC 渲染的世界送到无线头显上。
- 实现方式: 骁龙 8 Gen 3 与 16 GB LPDDR5X 内存，单眼 2160×2160 LCD，由内向外追踪与眼动追踪，并配有专用无线适配器用于 PC 串流。
- 参数: 2160×2160 LCD per eye · 72–144 Hz · Snapdragon 8 Gen 3 · 16 GB · $1,059 / $1,299
- 能力维度: 感知真实感
- 视频: https://www.youtube.com/watch?v=OmKrKTwtukE
- 图片: https://clan.fastly.steamstatic.com/images/45479024/41ac1feaa13a1396844a31be91beb068eb2e509f.jpg
- 项目主页: https://store.steampowered.com/sale/steamframe

#### Samsung Galaxy XR — 三星, 谷歌 (2025-10-21)
- 类型: 设备 · 获取方式: 产品 / 应用
- 输入: 语音与音频, 身体、面部与视线追踪, 透视画面与实时环境 → 输出: 三维场景 / 世界, 360° / 立体视频
- 核心想法: 首款由操作系统默认把平面媒体生成为空间内容的大众市场头显。
- 内容: 首款 Android XR 头显，由三星与 Google、高通合作打造，2025-10-21 上市，售价 1,799.99 美元。它内置能看到佩戴者所见画面的多模态助手 Gemini、把二维照片和视频转成三维的媒体自动空间化功能，以及沉浸式 Google 地图。
- 实现方式: 骁龙 XR2+ Gen 2，配 micro-OLED 显示屏、眼动与手势追踪，以及外置电池。
- 参数: Snapdragon XR2+ Gen 2 · micro-OLED, 3,552×3,840 per eye · $1,799.99 · launched 2025-10-21 (US, Korea)
- 能力维度: 感知真实感, 情境可达性
- 视频: https://www.youtube.com/watch?v=MPwZscUoly4
- 项目主页: https://www.samsung.com/us/xr/galaxy-xr/galaxy-xr/
- API 文档: https://developer.android.com/develop/xr

#### Apple Vision Pro (M5) — 苹果 (2025-10-15)
- 类型: 设备 · 获取方式: 产品 / 应用
- 输入: 身体、面部与视线追踪, 语音与音频, 透视画面与实时环境 → 输出: 360° / 立体视频, 三维场景 / 世界, 虚拟人（脸 / 身体）
- 核心想法: 展示生成场景与视频保真度最高的主流设备，内置眼动与手势追踪，但价格限制了实验室的采购数量。
- 内容: Apple 的混合现实头显，2025-10-15 升级为 M5 芯片，刷新率最高 120 Hz，配 Dual Knit 头带，售价 3,499 美元。在生成内容方面，它搭载 visionOS 26 的空间场景（用生成式深度让二维照片可被探索）、用于视频通话的 Persona、180° / 360° 与广角视频播放，以及 Apple Immersive 视频。
- 实现方式: 双 micro-OLED 显示屏（共 2,300 万像素），由 M5 与 R1 传感芯片驱动，支持眼动、手势与空间追踪。
- 参数: M5 + R1 · micro-OLED, 23M pixels total · up to 120 Hz · $3,499 · on sale 2025-10-22
- 能力维度: 感知真实感, 情境可达性
- 视频: https://www.apple.com/newsroom/videos/2025/autoplay/10/apple-vision-pro-immersive-experience/large_2x.mp4
- 图片: https://www.apple.com/newsroom/images/2025/10/apple-vision-pro-upgraded-with-the-m5-chip-and-dual-knit-band/tile/Apple-Vision-Pro-hero-251015-lp.jpg.og.jpg?202608191813
- 项目主页: https://www.apple.com/newsroom/2025/10/apple-vision-pro-upgraded-with-the-m5-chip-and-dual-knit-band/
- API 文档: https://developer.apple.com/visionos/

#### Meta Ray-Ban Display — Meta (2025-09-17)
- 类型: 设备 · 获取方式: 产品 / 应用
- 输入: 语音与音频, 身体、面部与视线追踪, 透视画面与实时环境 → 输出: 对话 / 文本, 图像 / 全景图
- 核心想法: 在日常活动中显示生成文字与图像的抬头通道：它不是沉浸式显示，却随时可用。
- 内容: Meta 首款内置显示屏的消费级眼镜：Ray-Ban 镜框中带一块单眼全彩镜片内显示，由 Meta Neural Band 肌电腕带操控，售价 799 美元。在生成内容方面，它可以在佩戴者视野中显示带图像的 Meta AI 回答、实时字幕与翻译，以及导航。
- 实现方式: 右侧镜片内置投影与波导，镜框上有摄像头与麦克风，腕带通过表面肌电解码手指手势。
- 参数: monocular in-lens display, 600×600 px · $799 incl. Neural Band · US launch 2025-09-30
- 能力维度: 情境可达性, 时间响应性
- 视频: https://www.youtube.com/watch?v=hrj4NQuE93M
- 图片: https://about.fb.com/wp-content/uploads/2025/09/Meta-Ray-Ban-Display_Social-Share.jpg?w=1200
- 项目主页: https://about.fb.com/news/2025/09/meta-ray-ban-display-ai-glasses-emg-wristband/

#### SPECS（Snap 消费级 AR 眼镜）（SPECS (Snap consumer AR glasses)） — Snap Inc. (2025-06-10)
- 类型: 设备 · 获取方式: 候补 / 抢先体验
- 输入: 语音与音频, 身体、面部与视线追踪, 透视画面与实时环境 → 输出: 三维场景 / 世界, 对话 / 文本
- 核心想法: 无需连线的 AR 眼镜，把生成内容放进佩戴者的真实环境；出品方已经在手机端大规模运行生成式滤镜。
- 内容: Snap 面向消费者的一体式光学透视 AR 眼镜，2025-06-10 宣布将于 2026 年推出，并在 2026-09-16 的 SPECS 发布会上正式亮相：预订价 2,195 美元（带蜂窝网络充电盒套装 2,395 美元），2026 年秋季晚些时候在美国、英国和法国发货。它运行 SPECS OS 与 Lens Studio 开发的应用（包括生成式 AI 滤镜），并搭载横跨 iPhone、Mac 与眼镜的预判式 AI 服务 SPECS Intelligence。
- 实现方式: 计算单元集成在眼镜上，无需外接计算盒，采用光学透视波导显示，支持手势与语音输入；以 Lens Studio 为创作工具，并调用云端 AI 服务。
- 参数: pre-order $2,195 (from 2026-09-16) · ships fall 2026 (US, UK, France) · standalone, no puck
- 能力维度: 情境可达性, 反应性
- 视频: https://www.youtube.com/watch?v=_RHEDU7neds
- 项目主页: https://investor.snap.com/news/news-details/2026/SPECS-Make-Computing-More-Human-with-New-Experiences-Partnerships-and-SPECS-Intelligence/default.aspx
- API 文档: https://developers.snap.com/spectacles/home

#### XREAL AURA — XREAL, 谷歌 (2025-05-20)
- 类型: 设备 · 获取方式: 候补 / 抢先体验
- 输入: 身体、面部与视线追踪, 透视画面与实时环境, 语音与音频 → 输出: 三维场景 / 世界, 360° / 立体视频
- 核心想法: 把完整的 Android XR 应用带到眼镜级重量的硬件上，让混合现实刺激能以人们愿意在公共场合佩戴的形态走出实验室。
- 内容: 与 Google 合作开发的光学透视 Android XR 眼镜（原名 Project Aura），配骁龙计算盒，并由 Gemini 提供辅助。截至 2026 年 10 月处于预约阶段，预计 2026 年秋季在美国、加拿大、日本和韩国上市，标价 1,279 美元（12 GB / 256 GB）或 1,499 美元（16 GB / 512 GB）。
- 实现方式: 骁龙（Reality Elite）计算盒加上眼镜内的 X1S 空间协处理器，驱动 70° 光学透视显示。
- 参数: 70° FOV · Sony micro-OLED 1920×1200 per eye · 95 g · 3 ms motion-to-photon · listed $1,279 / $1,499
- 能力维度: 情境可达性
- 视频: https://www.youtube.com/watch?v=qIQ7Qga61QI
- 图片: https://resource.xreal.com/www-xreal-com/images/aura/AuraPic_Mobile.webp
- 项目主页: https://www.xreal.com/aura
- API 文档: https://developer.android.com/develop/xr

#### Meta Quest 3 / Quest 3S — Meta (2023-06-01)
- 类型: 设备 · 获取方式: 产品 / 应用
- 输入: 身体、面部与视线追踪, 透视画面与实时环境, 键盘与手柄动作 → 输出: 三维场景 / 世界, 人工制作的 VR 情境
- 核心想法: VR 研究默认的交付设备：价格低到可以批量部署，摄像头访问又能让生成内容回应被试所在的真实房间。
- 内容: Meta 的一体式混合现实头显：Quest 3（2023-06-01 发布，2023-10-10 上市，售价 499 美元）与更便宜的 Quest 3S（2024-09-25，起价 299.99 美元），均采用骁龙 XR2 Gen 2 与彩色透视。它们在 VR 研究实验室中使用广泛；Horizon OS 允许应用访问透视摄像头以运行 AI，并支持 Meta 的 Hyperscape 照片级场景采集。
- 实现方式: 骁龙 XR2 Gen 2，具备由内向外追踪、手势追踪与彩色透视；Quest 3 采用 pancake 透镜并配有深度传感器，Quest 3S 采用菲涅耳透镜。
- 参数: Quest 3: 2064×2208 per eye, $499 at launch · Quest 3S: 1832×1920 per eye, from $299.99
- 能力维度: 情境可达性
- 视频: https://www.youtube.com/watch?v=Exu7r2vZpcw
- 项目主页: https://about.fb.com/news/2023/09/meet-meta-quest-3-mixed-reality-headset/

### 数据集与基准

这些模型学习所用的数据，以及比较它们的测试。

#### Arena 视频竞技场（Arena Video Arena (LMArena)） — Arena (formerly LMArena) (2026-01-21)
- 类型: 数据集 / 基准 · 获取方式: 产品 / 应用
- 输入: 文字提示, 图像 → 输出: 平面视频
- 核心想法: 人类两两偏好是衡量感知真实感最接近的公开指标，但它奖励的是惊艳的短片，而不是长时间交互中的一致性。
- 内容: Arena 的众包视频生成排行榜：访客输入提示词，并排观看两个匿名模型生成的片段并投票，票数汇总为文生视频与图生视频的评分。它于 2026 年 1 月在 lmarena.ai 上线；此后公司已由 LMArena 更名为 Arena（arena.ai）。
- 实现方式: 公众用户的盲测两两比较，用 Bradley-Terry 模型汇总为带置信区间的评分。
- 参数: text-to-video and image-to-video leaderboards · blind pairwise votes
- 能力维度: 感知真实感, 实验控制
- 视频: https://www.youtube.com/watch?v=6Z1z6ztfx60
- 项目主页: https://arena.ai

#### WorldScore — Haoyi Duan (2025-04-01)
- 类型: 数据集 / 基准 · 获取方式: 开源权重 / 代码
- 输入: 文字提示, 图像, 镜头路径 / 位姿 → 输出: 三维场景 / 世界, 平面视频, 动态三维 / 4D
- 核心想法: 把视频模型与显式三维生成器放在同一把尺子上比较镜头控制与一致性；在选择通往可探索世界的技术路线时，正需要这种比较。
- 内容: 斯坦福提出的世界生成统一基准，让三维场景生成器、4D 生成器与视频模型在同一任务上接受评测：按布局与镜头轨迹指令生成一连串场景。它在 3,000 个测试样例上从可控性、质量与动态三方面打分，并维护公开排行榜；论文评测了 19 个模型。
- 实现方式: 把世界生成拆解为带显式镜头轨迹布局的“下一个场景”任务，由自动指标评估镜头与物体控制、内容对齐、三维与光度一致性、风格、主观质量与运动。
- 参数: 3,000 test examples · 19 models evaluated · ICCV 2025
- 能力维度: 持久性, 实验控制
- 论文: https://arxiv.org/abs/2504.00983 (ICCV 2025)
- 视频: https://haoyi-duan.github.io/WorldScore/assets/videos/overview.mp4
- 图片: https://haoyi-duan.github.io/WorldScore/assets/images/overview/dataset_overview.jpg
- 项目主页: https://haoyi-duan.github.io/WorldScore/
- 代码: https://github.com/haoyi-duan/WorldScore

#### VBench-2.0 — Dian Zheng, Ziqi Huang (2025-03-27)
- 类型: 数据集 / 基准 · 获取方式: 开源权重 / 代码
- 输入: 文字提示 → 输出: 平面视频
- 核心想法: 它追问生成的事件是否符合物理与常识，而这正决定了一个生成情境在行为上是否可信。
- 内容: VBench 的后续基准，检验的是“内在可信度”而非表面画质：18 个维度分为人物保真、可控性、创造力、物理与常识五类，由视觉语言模型、大语言模型与异常检测器打分。
- 实现方式: 按维度设计的提示集，由视觉语言模型 / 大语言模型评审与专用检测器评估，并与人类标注对照检验一致性。
- 参数: 18 dimensions in 5 categories · arXiv 2025-03
- 能力维度: 行为似真性, 实验控制
- 论文: https://arxiv.org/abs/2503.21755 (arXiv 2025)
- 视频: https://www.youtube.com/watch?v=kJrzKy9tgAc
- 图片: https://vchitect.github.io/VBench-2.0-project/assets/vbench/images/figures/fig_paper_teaser.jpg
- 项目主页: https://vchitect.github.io/VBench-2.0-project/
- 代码: https://github.com/Vchitect/VBench

#### Artificial Analysis 视频竞技场（Artificial Analysis Video Arena） — Artificial Analysis (2024)
- 类型: 数据集 / 基准 · 获取方式: 产品 / 应用
- 输入: 文字提示, 图像, 视频 → 输出: 平面视频
- 核心想法: 把质量评分与各服务商的价格和延迟放在一起，这正是实验室选择托管生成器时要权衡的三个数字。
- 内容: 独立评测公司 Artificial Analysis 运营的视频模型盲投竞技场，分设文生视频、图生视频与视频编辑排行榜，并附有各 API 服务商的价格与速度对比。视频模型厂商发布新模型时常引用它的排名。
- 实现方式: 对同一提示生成的片段进行人类两两偏好投票，汇总为 Elo 式评分，并给出各服务商实测的生成时间与标价。
- 参数: text-to-video · image-to-video · video editing · online since at least 2024-10
- 能力维度: 感知真实感, 实验控制
- 图片: https://artificialanalysis.ai/opengraph-image.png?ab13fbb533329573
- 项目主页: https://artificialanalysis.ai/text-to-video/arena

#### 3D 竞技场（3D Arena）（3D Arena） — Dylan Ebert (2024-06)
- 类型: 数据集 / 基准 · 获取方式: 开源权重 / 代码
- 输入: 图像 → 输出: 网格 / 三维资产, 高斯泼溅 / 辐射场
- 核心想法: 规模最大的生成三维资产公开人类评判，可用来决定场景道具该信任哪个生成器。
- 内容: Hugging Face 上的一个开放 Space：人们对比同一张输入图片生成的两个匿名图生三维结果（网格或高斯泼溅）并投票。2025 年的论文报告，自 2024 年 6 月上线以来，共有 8,096 名用户为 19 个模型投出 123,243 票，结果显示人们更偏好高斯泼溅与带纹理的输出。
- 实现方式: 在网页三维查看器中，以 100 个提示的 iso3d 数据集进行两两偏好投票，配合统计学作弊检测，汇总为 Elo 评分。
- 参数: 123,243 votes · 8,096 users · 19 models · iso3d: 100 prompts
- 能力维度: 感知真实感, 实验控制
- 论文: https://arxiv.org/abs/2506.18787 (arXiv 2025)
- 图片: https://cdn-thumbnails.huggingface.co/social-thumbnails/spaces/3d-arena/3d-arena.png
- 项目主页: https://huggingface.co/spaces/dylanebert/3d-arena

#### DL3DV-10K — Lu Ling (2023-12-26)
- 类型: 数据集 / 基准 · 获取方式: 开源权重 / 代码
- 输入: 多视角拍摄 / 扫描, 视频 → 输出: 三维场景 / 世界
- 核心想法: 这种规模的真实场景多样性，才让重建模型与世界模型能泛化到少数基准房间之外。
- 内容: 包含 10,510 段视频（5,120 万帧）的数据集，覆盖 65 类地点的真实室内外场景，反射、透明与光照条件各异，用于训练和评测新视角合成与三维重建。它已成为前馈式重建与镜头可控视频模型的标准训练数据之一。
- 实现方式: 用手机与无人机拍摄视频，以运动恢复结构估计相机位姿，按场景复杂度标注，并划出新视角合成的评测子集。
- 参数: 10,510 videos · 51.2M frames · 65 location types · CVPR 2024
- 能力维度: 情境多样性, 感知真实感
- 论文: https://arxiv.org/abs/2312.16256 (CVPR 2024)
- 视频: https://dl3dv-10k.github.io/DL3DV-10K/assets/img/teaser1080-2x.mp4
- 图片: https://dl3dv-10k.github.io/DL3DV-10K/assets/img/Scene_Category_by_secondary_POI.png
- 项目主页: https://dl3dv-10k.github.io/DL3DV-10K/
- 代码: https://github.com/DL3DV-10K/Dataset

#### VBench — Ziqi Huang (2023-11-29)
- 类型: 数据集 / 基准 · 获取方式: 开源权重 / 代码
- 输入: 文字提示, 图像 → 输出: 平面视频
- 核心想法: 把“视频质量”拆成可以分别测量的维度；不过时间平滑度得分高，也可能是在奖励几乎不动的视频。
- 内容: 一套视频生成评测基准，从主体一致性、运动平滑度、时间闪烁、动态程度、空间关系等 16 个维度为文生视频模型打分，每个维度都有专门的提示集与自动评估器，并以人类偏好标注加以校验。许多视频模型发布时都会引用它的公开排行榜；VBench++（2024）又加入了图生视频与可信度测试。
- 实现方式: 按维度设计的提示集，由基于预训练视觉模型的自动指标打分（特征相似度、光流、检测器、美学预测器），并用逐维度的人类偏好标注加以验证。
- 参数: 16 dimensions · CVPR 2024 Highlight · VBench++ arXiv 2411.13503
- 能力维度: 实验控制, 感知真实感
- 论文: https://arxiv.org/abs/2311.17982 (CVPR 2024)
- 视频: https://www.youtube.com/watch?v=7IhCC8Qqn8Y
- 图片: https://vchitect.github.io/VBench-project/assets/vbench/images/dim_results/fig_teaser_new.jpg
- 项目主页: https://vchitect.github.io/VBench-project/
- 代码: https://github.com/Vchitect/VBench

#### Objaverse-XL — Matt Deitke (2023-07-11)
- 类型: 数据集 / 基准 · 获取方式: 开源权重 / 代码
- 输入:  → 输出: 网格 / 三维资产
- 核心想法: 为生成世界提供道具的资产生成器，对物体的理解很大程度上来自这一语料，也继承了它的偏差与参差不齐的授权。
- 内容: 艾伦人工智能研究所从公开来源收集的开放数据集，包含 1,000 多万个去重的三维物体（手工建模物体、摄影测量扫描以及历史文物的专业扫描）。它是图生三维与多视角扩散模型的主要预训练语料之一；论文用其中超过 1 亿张渲染图训练了 Zero123-XL。
- 实现方式: 爬取并去重公开三维资源库，附带元数据与渲染脚本；每个物体的授权各不相同。
- 参数: 10M+ objects · NeurIPS 2023 Datasets and Benchmarks
- 能力维度: 情境多样性
- 论文: https://arxiv.org/abs/2307.05663 (NeurIPS 2023 Datasets and Benchmarks)
- 视频: https://objaverse.allenai.org/objaverse-xl/image-to-3d.mp4
- 图片: https://objaverse.allenai.org/objaverse-xl/objaverse-xl.jpg
- 项目主页: https://objaverse.allenai.org/
- 代码: https://github.com/allenai/objaverse-xl

#### RealEstate10K — Tinghui Zhou (2018)
- 类型: 数据集 / 基准 · 获取方式: 开源权重 / 代码
- 输入: 镜头路径 / 位姿, 视频 → 输出: 三维场景 / 世界, 平面视频
- 核心想法: 普通的看房视频加上恢复出的镜头路径，让新视角合成与镜头可控视频模型学会了人在室内移动时空间如何展开。
- 内容: 约 8 万段 YouTube 房产看房视频片段、约 1,000 万帧的相机轨迹数据集，由 Google 随 Stereo Magnification 论文发布。它成为新视角合成、以及后来镜头可控视频生成的标准测试集。
- 实现方式: 对看房视频进行 SLAM 与光束法平差，恢复逐帧相机内参与位姿；数据集提供位姿与视频 ID，不包含视频本身。
- 参数: ~10M frames · ~80K clips · SIGGRAPH 2018
- 能力维度: 情境多样性, 实验控制
- 论文: https://arxiv.org/abs/1805.09817 (SIGGRAPH 2018 (ACM TOG))
- 图片: https://tinghuiz.github.io/projects/mpi/images/teaser.png
- 项目主页: https://google.github.io/realestate10k/

## 资源与链接：人物、机构与网站

### 研究者

- **Albert "Skip" Rizzo** (美国洛杉矶) — 南加州大学创意技术研究所（ICT）医疗虚拟现实主任，主导了用于创伤后应激障碍的 Bravemind VR 暴露疗法，以及用于临床培训的虚拟标准化病人。 代表作: Bravemind / Virtual Iraq (2005–); SimCoach (2011); Virtual standardized patients. https://ict.usc.edu/about-us/leadership/research-leadership/albert-skip-rizzo/
- **Aleksander Holynski** (美国纽约) — 哥伦比亚大学教授，同时在 Google DeepMind 领导生成式三维与世界模型团队；InstructPix2Pix、CAT3D 与 CAT4D 的共同作者，这些方法用多视角扩散把少量图像变成三维与四维场景。 代表作: CAT3D (NeurIPS 2024); CAT4D (CVPR 2025); InstructPix2Pix (CVPR 2023). https://holynski.org/
- **Alexandre Défossez** (法国巴黎) — Kyutai 创始成员、首席探索官（Chief Exploration Officer）；Moshi 的主要作者，此前在 Meta 主导了 EnCodec 音频编解码器、Demucs 音源分离与 MusicGen。 代表作: Moshi (2024); EnCodec (2022); MusicGen (NeurIPS 2023); Demucs (2019). https://ai.honu.io/
- **Angjoo Kanazawa** (美国伯克利) — 加州大学伯克利分校副教授，领导 Kanazawa AI Research（KAIR）实验室；其团队开发了众多高斯泼溅项目所依赖的开源工具（Nerfstudio、gsplat），以及从随手拍视频中进行人物与场景 4D 重建的方法。她曾担任 Luma AI 与 Wonder Dynamics 的顾问。 代表作: Nerfstudio (SIGGRAPH 2023); gsplat (2024); Shape of Motion (2024); Plenoxels (CVPR 2022). https://people.eecs.berkeley.edu/~kanazawa/
- **Antonia Hamilton** (英国伦敦) — 伦敦大学学院认知神经科学研究所社会神经科学教授，借助动作捕捉与虚拟角色研究面对面互动中的模仿、注视与非语言协调。 代表作: Why and how to use virtual reality to study human social interaction (with Pan, 2018); Social neuroscience of mimicry. https://antoniahamilton.com/
- **Ashley Edwards** — Google DeepMind 高级研究科学家，研究强化学习与基础世界模型。她早期关于仅从观察中学习潜在动作的工作，是 Genie 潜在动作模型的基础，使世界模型可以用无标注视频训练。 代表作: Imitating Latent Policies from Observation (ICML 2019); Genie (ICML 2024, co-first author). https://ashedwards.github.io/
- **Ben Mildenhall** (美国旧金山) — World Labs 联合创始人，NeRF 第一作者；这篇 2020 年的论文开启了神经辐射场视角合成的时代。2021 至 2023 年他在 Google Research 任研究科学家。 代表作: NeRF (ECCV 2020); Mip-NeRF 360 (CVPR 2022); DreamFusion (ICLR 2023). https://bmild.github.io/
- **Bernhard Kerbl** (丹麦哥本哈根) — 3D 高斯泼溅（3DGS）第一作者：该方法让照片级辐射场可以实时渲染，引发了高斯泼溅热潮。他现任哥本哈根大学终身轨助理教授，并在维也纳工业大学担任项目首席研究员。 代表作: 3D Gaussian Splatting for Real-Time Radiance Field Rendering (SIGGRAPH 2023 Best Paper); A Hierarchical 3D Gaussian Representation for Real-Time Rendering of Very Large Datasets (SIGGRAPH 2024). https://snosixtyboo.github.io/
- **Bill Peebles** (美国旧金山) — OpenAI 研究科学家、Sora 负责人，扩散 Transformer（DiT）的共同作者；DiT 是当今多数视频模型采用的架构。OpenAI 于 2026 年 4 月关闭 Sora 应用、9 月关闭其 API，Sora 转为面向世界模拟的研究项目。 代表作: Scalable Diffusion Models with Transformers (DiT, ICCV 2023); Sora (2024); Sora 2 (2025). https://www.wpeebles.com/
- **Botao 'Amber' Hu / 胡博涛** — 设计师与研究者，主持现实设计实验室（Reality Design Lab），在中国美术学院教授混合现实设计；开源 HoloKit 头显及本图库的创作者。 代表作: HoloKit (open-source MR headset); EchoVision; Generative Immersive Reality Inspire (2026). https://amber.botao.hu/
- **Christoph Lassner** (美国旧金山) — World Labs 联合创始人，此前在 Epic Games 与 Meta Reality Labs Research 领导研究团队，研究可交互的辐射场重建与渲染以及三维人体模型。 代表作: Keep it SMPL / SMPLify (ECCV 2016); Pulsar: Efficient Sphere-based Neural Rendering (CVPR 2021). https://christophlassner.de/
- **Daniel Freeman** (英国牛津) — 牛津大学临床心理学教授，用 VR 研究和治疗偏执；他的 gameChange 试验检验了由虚拟教练引导的自动化 VR 疗法对精神病患者的效果。 代表作: gameChange automated VR therapy trial (Lancet Psychiatry, 2022); Automated VR treatment for fear of heights (Lancet Psychiatry, 2018). https://en.wikipedia.org/wiki/Daniel_Freeman_(psychologist)
- **Eloi Alonso** — General Intuition 联合创始人，DIAMOND 第一作者：这个开源扩散世界模型完全在“想象”中训练 Atari 智能体，并生成了可玩的 Counter-Strike 地图。他在日内瓦大学 François Fleuret 组完成博士学业。 代表作: DIAMOND: Diffusion for World Modeling (NeurIPS 2024 Spotlight); IRIS: Transformers are Sample-Efficient World Models (ICLR 2023). https://eloialonso.github.io/
- **Fei-Fei Li / 李飞飞** (美国斯坦福 / 旧金山, 1976–) — 斯坦福大学教授，ImageNet 的创建者，空间智能公司 World Labs 的联合创始人兼首席执行官（推出 Marble）；她主张语言模型之后的下一步是能生成并推理三维世界的模型。 代表作: ImageNet (CVPR 2009); World Labs Marble (2025); From Words to Worlds: Spatial Intelligence (essay, 2025). https://profiles.stanford.edu/fei-fei-li
- **George Drettakis** (法国索菲亚-安提波利斯) — 法国国家信息与自动化研究院（Inria）索菲亚-安提波利斯中心 GraphDeco 组负责人，3D 高斯泼溅的通讯作者；他数十年的基于图像的渲染研究为该方法奠定了基础。 代表作: 3D Gaussian Splatting (SIGGRAPH 2023); Deep Blending for Free-Viewpoint Image-Based Rendering (SIGGRAPH Asia 2018). https://www-sop.inria.fr/members/George.Drettakis/
- **Gordon Wetzstein** (美国斯坦福) — 斯坦福大学教授，领导计算成像实验室，研究横跨三维感知生成模型、神经渲染以及面向 AR / VR 的全息近眼显示。 代表作: EG3D (CVPR 2022); Holographic glasses for virtual reality (SIGGRAPH 2022); SIREN (NeurIPS 2020). https://stanford.edu/~gordonwz/
- **Guido Makransky** (丹麦哥本哈根) — 哥本哈根大学教育心理学教授；他提出的 CAMIL 模型解释了沉浸式 VR 何时有助于学习，他的实验还发现临场感更强有时反而学得更少。 代表作: CAMIL: Cognitive Affective Model of Immersive Learning (Educational Psychology Review, 2021); Adding immersive VR to a science lab simulation causes more presence but less learning (2019). https://researchprofiles.ku.dk/en/persons/guido-makransky/
- **Hao Li / 黎顥** (阿联酋阿布扎比 / 美国洛杉矶, 1981–) — Pinscreen 联合创始人兼首席执行官、穆罕默德·本·扎耶德人工智能大学（MBZUAI）计算机视觉教授并主持元宇宙中心；他开发即时照片级虚拟形象，也经常就深度伪造问题发声。 代表作: paGAN (SIGGRAPH Asia 2018); Pinscreen avatars; Realistic Dynamic Facial Textures from a Single Image using GANs (ICCV 2017). https://en.wikipedia.org/wiki/Hao_Li
- **Ioannis Patras** (英国伦敦) — 伦敦玛丽女王大学计算机视觉与人体感知教授、Tavus 研究负责人；他是 Griffin（2026）的共同作者，这是一个实时“人类交互模型”，Tavus 报告称 48% 的研究参与者把它当成了真人。 代表作: Griffin human interaction model (Tavus, 2026); Facial expression and affect analysis. https://www.qmul.ac.uk/eecs/people/profiles/patrasioannis.html
- **Jack Parker-Holder** (英国伦敦) — Google DeepMind 研究总监，负责扩展世界模型；共同主导了 Genie、Genie 2 与 Genie 3，这些模型能把一段提示变成可以在其中行动的环境。他同时是 UCL DARK 的荣誉讲师。 代表作: Genie: Generative Interactive Environments (ICML 2024); Genie 2 (2024); Genie 3 (2025). https://jparkerholder.github.io/
- **Jake Bruce** (英国伦敦) — Google DeepMind 伦敦研究科学家，Genie 第一作者。这个 110 亿参数的模型在没有动作标注的情况下，从互联网游戏视频中学会了生成可玩的 2D 世界；他也参与了 Genie 3。 代表作: Genie: Generative Interactive Environments (ICML 2024 Best Paper); Genie 3 (2025). https://jakebruce.ca/
- **Jaron Lanier** (美国伯克利, 1960–) — 虚拟现实先驱，1985 年创立首家销售 VR 头显与数据手套的公司 VPL Research，现任职于微软；他在著作中倡导“数据尊严”，反对把人当作 AI 的燃料。 代表作: VPL Research DataGlove and EyePhone (1980s); Dawn of the New Everything (2017); Who Owns the Future? (2013). https://www.jaronlanier.com/
- **Jean-Louis van Gelder** (德国弗莱堡) — 弗莱堡马克斯·普朗克犯罪、安全与法律研究所所长，把 VR 引入犯罪学研究，最著名的是让入室盗窃者在虚拟街区中行走的研究。 代表作: Virtual Burglary (Journal of Research in Crime and Delinquency, 2017); Virtual Reality for Criminologists (Crime and Justice, 2023). https://csl.mpg.de/en/jean-louis-van-gelder
- **Jeremy Bailenson** (美国斯坦福) — 斯坦福大学虚拟人交互实验室（VHIL）创始主任；他关于“普罗透斯效应”与“变换的社会互动”的研究揭示了化身如何改变使用它的人。 代表作: The Proteus Effect (Human Communication Research, 2007); Transformed Social Interaction (2004); Experience on Demand (2018). https://vhil.stanford.edu/people/jeremy-bailenson
- **Jim Blascovich** (美国圣塔芭芭拉) — 加州大学圣塔芭芭拉分校心理学杰出荣休教授；他 2002 年的论文把沉浸式虚拟环境确立为社会心理学的方法工具，在实验控制与日常真实性之间取得平衡。 代表作: Immersive virtual environment technology as a methodological tool for social psychology (Psychological Inquiry, 2002); Infinite Reality (with Bailenson, 2011). https://psych.ucsb.edu/people/emeriti/jim-blascovich
- **Jon Barron** (美国旧金山) — Google DeepMind 旧金山首席研究科学家，带领一个主要研究 NeRF 的小团队；NeRF 及 Mip-NeRF、Zip-NeRF 系列的共同作者，也参与了 DreamFusion、CAT3D 等生成式三维工作。 代表作: Mip-NeRF (ICCV 2021); Zip-NeRF (ICCV 2023); CAT3D (NeurIPS 2024). https://jonbarron.info/
- **Jonathan Gratch** (美国洛杉矶) — 南加州大学创意技术研究所教授，主持情感计算组；他为虚拟人构建情绪计算模型，并研究人们为何更愿意向虚拟人吐露心声。 代表作: EMA: a process model of appraisal dynamics (2009); It's only a computer: virtual humans increase willingness to disclose (2014); SimSensei Kiosk (AAMAS 2014). https://people.ict.usc.edu/~gratch/
- **Joon Sung Park** (美国帕洛阿尔托) — 提出“生成式智能体”（由 25 个大模型角色组成的 Smallville 小镇）的计算机科学家，后又根据访谈模拟了 1,052 位真实个体；他现在经营 Simile，一家在帕洛阿尔托提供群体规模行为模拟的公司。 代表作: Generative Agents (UIST 2023 Best Paper); Generative Agent Simulations of 1,000 People (2024); Social Simulacra (UIST 2022). https://www.joonsungpark.com/
- **Justin Johnson** (美国旧金山) — World Labs 联合创始人、密歇根大学教员；以风格迁移的感知损失、CLEVR 推理基准和由场景图生成图像等工作著称。 代表作: Perceptual Losses for Real-Time Style Transfer (ECCV 2016); CLEVR (CVPR 2017); Image Generation from Scene Graphs (CVPR 2018). https://www.worldlabs.ai/about
- **Linxi "Jim" Fan / 范麟熙** (美国圣克拉拉) — NVIDIA 高级研究科学家、AI 智能体负责人（GEAR 实验室）；他的 Minecraft 智能体 MineDojo 与 Voyager 展示了大模型驱动的智能体在游戏世界里学习开放式技能。 代表作: Voyager (2023); MineDojo (NeurIPS 2022 Outstanding Paper); Eureka (ICLR 2024). https://jimfan.me/
- **Louis-Philippe Morency** (美国匹兹堡) — 卡内基梅隆大学 Leonardo 副教授，主持 MultiComp 实验室；他参与打造了 SimSensei——一个通过读取非语言线索筛查心理困扰的虚拟访谈者，并研究社会行为的多模态模型。 代表作: SimSensei Kiosk (AAMAS 2014); Multimodal Machine Learning: A Survey and Taxonomy (TPAMI 2019). https://www.cs.cmu.edu/~morency/
- **Mar Gonzalez-Franco** — 神经科学家与计算机科学家，在 Google 管理人机交互与智能眼镜方向的团队，主导了 Android XR 的输入与交互体验；此前在微软研究院主持化身具身研究，并开放了 Rocketbox 虚拟人库。 代表作: The Rocketbox Library (Frontiers in VR 2020); Avatar Embodiment questionnaire (Frontiers 2018); Android XR input and interaction. https://margonzalezfranco.github.io/
- **Maria V. Sanchez-Vives** (西班牙巴塞罗那) — 巴塞罗那 IDIBAPS 研究所的 ICREA 研究教授，领导系统神经科学组，长期与 Event Lab 的 Mel Slater 合作；她研究临场感、身体拥有感，以及虚拟身体如何改变行为。 代表作: From presence to consciousness through virtual reality (Nat. Rev. Neurosci., 2005); Enhancing Our Lives with Immersive Virtual Reality (Frontiers in Robotics and AI, 2016). https://ca.wikipedia.org/wiki/Mavi_S%C3%A1nchez-Vives
- **Matthias Nießner** (德国慕尼黑, 1986–) — 慕尼黑工业大学教授，领导视觉计算与人工智能实验室，Synthesia 联合创始人；其团队在人脸重演与高斯化身方面的工作，同时推动了深度伪造检测与可驱动三维头像。 代表作: Face2Face (CVPR 2016); ScanNet (CVPR 2017); GaussianAvatars (CVPR 2024). https://niessnerlab.org/
- **Mel Slater** (西班牙巴塞罗那) — 在巴塞罗那大学领导 Event Lab 的虚拟现实研究者；他提出的“位置错觉与合理性错觉”定义了临场感，他的虚拟米尔格拉姆实验与旁观者研究表明，人们会对虚拟他人做出真实反应。 代表作: Place illusion and plausibility (Phil. Trans. R. Soc. B, 2009); A Virtual Reprise of the Stanley Milgram Obedience Experiments (PLoS ONE, 2006); Bystander responses to a violent incident in an immersive virtual environment (PLoS ONE, 2013). https://www.ub.edu/eventlab/EventLab/
- **Michael Bernstein** (美国斯坦福) — 斯坦福大学计算机科学教授（人机交互组），《Generative Agents》与《Social Simulacra》的通讯作者；他研究如何使用（以及如何误用）模拟的人来为社会系统做原型。 代表作: Generative Agents (UIST 2023); Social Simulacra (UIST 2022); Generative Agent Simulations of 1,000 People (2024). https://hci.stanford.edu/msb/
- **Michael J. Black** (德国图宾根) — 马克斯·普朗克智能系统研究所感知系统部门创始所长、Meshcapade 联合创始人；他的 SMPL 人体模型是大多数三维人体生成与动作研究的通用骨架。 代表作: SMPL (SIGGRAPH Asia 2015); SMPL-X (CVPR 2019); AMASS (ICCV 2019). https://en.wikipedia.org/wiki/Michael_J._Black
- **Neil Zeghidour** (法国巴黎) — 巴黎实验室 Kyutai 联合创始人、其语音衍生公司 Gradium（2025 年 12 月成立）的首席执行官；SoundStream、AudioLM 与 Moshi 的共同作者，Moshi 是首个开源的全双工语音模型，可以边听边说。 代表作: SoundStream (2021); AudioLM (2022); Moshi (2024). https://scholar.google.com/citations?user=fiJamZ0AAAAJ
- **Noah Snavely** (美国纽约) — 康奈尔科技校区教授、Google DeepMind 研究员，研究从 Photo Tourism（2006）一直到 RealEstate10K 相机轨迹数据集与随手视频的 4D 重建；如今多数相机可控视频与场景模型都用这些数据训练。 代表作: Photo Tourism (SIGGRAPH 2006); Stereo Magnification / RealEstate10K (SIGGRAPH 2018); MegaSaM (CVPR 2025). https://www.cs.cornell.edu/~snavely/
- **Percy Liang** (美国斯坦福) — 斯坦福大学教授、基础模型研究中心（CRFM）主任；《Generative Agents》与“1000 人模拟”的共同作者，也主持了 HELM 评测框架。 代表作: HELM (2022); Generative Agents (UIST 2023); On the Opportunities and Risks of Foundation Models (2021). https://cs.stanford.edu/~pliang/
- **Ruiqi Gao** — Google DeepMind 研究科学家，研究生成模型；CAT3D 第一作者，该方法可在约一分钟内由一张或几张图像生成三维场景。 代表作: CAT3D: Create Anything in 3D with Multi-View Diffusion Models (NeurIPS 2024); Understanding Diffusion Objectives as the ELBO (NeurIPS 2023). https://ruiqigao.github.io/
- **Ryo Suzuki** (美国博尔德) — 科罗拉多大学博尔德分校（ATLAS 研究所）助理教授，此前任教于卡尔加里大学，领导可编程现实实验室（Programmable Reality Lab）；其团队开发用 AI 从物理世界生成交互内容的 AR 系统。 代表作: RealitySketch (UIST 2020); Augmented Physics (UIST 2024); RealityCanvas (UIST 2023). https://ryosuzuki.org/
- **Shlomi Fruchter** — Google DeepMind 研究总监，曾参与领导 Veo 与 Imagen 3，并合著 GameNGen：一个无需游戏引擎、实时运行 DOOM 的扩散模型。 代表作: GameNGen: Diffusion Models Are Real-Time Game Engines (ICLR 2025); Veo (2024); Imagen 3 (2024). https://shlomifruchter.github.io/
- **Sylvia Xueni Pan** (英国伦敦) — 伦敦大学金史密斯学院虚拟现实教授，共同主持该校虚拟与增强现实硕士项目；她用虚拟角色研究社会互动，并训练医生应对棘手病人。 代表作: Why and how to use virtual reality to study human social interaction (British Journal of Psychology, 2018); GPs' responses to patient demand for antibiotics in VR (2016). https://www.panxueni.com/
- **Thomas Müller** — instant-ngp 与 tiny-cuda-nn 的作者；其多分辨率哈希编码把 NeRF 训练从数小时缩短到数秒。他曾任 NVIDIA 首席研究科学家，现为独立研究者。 代表作: Instant Neural Graphics Primitives (SIGGRAPH 2022 Best Paper); tiny-cuda-nn (2021). https://tom94.net/
- **Tim Brooks** (美国旧金山) — 在 Meta 超级智能实验室（Meta Superintelligence Labs）领导媒体生成（Muse Image 与 Muse Video 模型）。此前他在 Google DeepMind 领导全模态模型团队，并在 OpenAI 共同领导 Sora；在伯克利读博期间提出了 InstructPix2Pix。 代表作: Sora: Video generation models as world simulators (2024); InstructPix2Pix (CVPR 2023); Generating Long Videos of Dynamic Scenes (NeurIPS 2022). https://timothybrooks.com/
- **Tim Rocktäschel** (英国伦敦) — 伦敦大学学院（UCL）人工智能教授，Recursive 联合创始人兼首席科学家；此前领导 Google DeepMind 的开放式学习（Open-Endedness）团队，Genie 即出自该团队。他主张智能体持续学习需要开放式环境，而不是固定数据集。 代表作: Genie (ICML 2024); Open-Endedness is Essential for Artificial Superhuman Intelligence (ICML 2024); The NetHack Learning Environment (NeurIPS 2020). https://rockt.ai/
- **Vincent Sitzmann** (美国马萨诸塞州剑桥) — MIT CSAIL 副教授，领导场景表示组（Scene Representation Group），研究神经场景表示，以及能在时间上保持三维结构与记忆的视频世界模型。 代表作: SIREN (NeurIPS 2020); Scene Representation Networks (NeurIPS 2019); Diffusion Forcing (NeurIPS 2024). https://www.vincentsitzmann.com/
- **Yann LeCun** (美国纽约 / 法国巴黎, 1960–) — 图灵奖得主、纽约大学教授，2025 年 12 月离开 Meta 首席 AI 科学家职位，联合创办 Advanced Machine Intelligence（AMI）Labs。他主张智能体需要预测式世界模型（JEPA），而非逐像素生成。 代表作: A Path Towards Autonomous Machine Intelligence (2022); I-JEPA (2023); V-JEPA 2 (2025). https://en.wikipedia.org/wiki/Yann_LeCun
- **Yaser Sheikh** (美国匹兹堡) — 创立了 Meta 匹兹堡 Reality Labs 实验室，2015 至 2025 年任 Meta 副总裁期间主导发明了 Codec Avatars（实时照片级远程临场化身）。现为卡内基梅隆大学顾问教授，并创办了一家尚未公开的 AI 公司。 代表作: Codec Avatars (2019–2025); OpenPose (CVPR 2017); Panoptic Studio (ICCV 2015). https://www.cs.cmu.edu/~yaser/
- **Zhu Jun / 朱军** (中国北京) — 清华大学计算机系教授，生数科技首席科学家。其团队提出的 U-ViT 架构是 Vidu 的基础；Vidu 于 2024 年 4 月发布，团队称其为继 Sora 之后首个 Sora 级视频生成模型。 代表作: U-ViT: All are Worth Words (CVPR 2023); Vidu (2024); ProlificDreamer (NeurIPS 2023). https://ml.cs.tsinghua.edu.cn/~jun/index.shtml
- **Ziwei Liu / 刘子纬** (新加坡) — 南洋理工大学副教授（MMLab@NTU、S-Lab），其团队构建了被广泛使用的视频生成评测基准 VBench，并发布了多个开源三维与虚拟人生成模型。 代表作: VBench (CVPR 2024); LGM: Large Multi-View Gaussian Model (ECCV 2024); DeepFashion (CVPR 2016). https://liuziwei7.github.io/

### 创始人与建造者

- **Amit Jain** (美国旧金山) — Luma AI 联合创始人兼首席执行官；Luma 从 NeRF 拍摄应用起步，推出 Dream Machine 与 Ray 系列视频模型，如今把使命描述为“通用物理 AI”。 代表作: Luma NeRF capture app (2022); Dream Machine (2024); Ray3 (2025). https://x.com/gravicle
- **Brendan Iribe** (美国旧金山, 1979–) — Oculus 联合创始人，后又联合创办语音伴侣公司 Sesame；其对话语音模型（CSM，2025）让 AI 声音能像人一样停顿、发笑和打断。Sesame 也在开发智能眼镜。 代表作: Oculus Rift (2012–2016); Sesame CSM / Maya and Miles (2025). https://en.wikipedia.org/wiki/Brendan_Iribe
- **Cristóbal Valenzuela** (美国纽约, 1989–) — Runway 联合创始人兼首席执行官；Runway 把视频生成从研究带进电影制作工具（Gen-1 至 Gen-4.5），并在 2025 年转向通用世界模型。 代表作: Runway Gen-2 (2023); Gen-4 (2025); GWM-1 world model (2025). https://en.wikipedia.org/wiki/Crist%C3%B3bal_Valenzuela
- **Dean Leitersdorf** (美国旧金山 / 以色列特拉维夫) — Decart 联合创始人兼首席执行官，公司开发实时生成视频：与 Etched 合作的可玩类 Minecraft 世界模型 Oasis，以及实时视频风格转换 MirageLSD。 代表作: Oasis (2024); MirageLSD (2025). https://x.com/dleitersdorf
- **Ethan (Yuanming) Hu / 胡渊鸣** — Meshy 创始人兼首席执行官，Meshy 是文本 / 图像生成三维资产的工具；此前他在 MIT 读博期间创造了面向图形学的 Taichi 编程语言。 代表作: Taichi (SIGGRAPH Asia 2019); Meshy (2023–); DiffTaichi (ICLR 2020). https://yuanming.taichi.graphics/
- **Hassaan Raza** (美国旧金山) — Tavus 联合创始人兼首席执行官；Tavus 的对话式视频接口把感知、轮流发言与人脸模型组合在一起，并于 2026 年 10 月推出被其称为“人类交互模型”的 Griffin。 代表作: Tavus CVI (2024); Phoenix / Raven / Sparrow models; Griffin (2026). https://www.tavus.io/griffin
- **Joshua Xu** (美国洛杉矶) — HeyGen 联合创始人兼首席执行官；HeyGen 是虚拟人视频平台，其交互式虚拟人把说话人像生成带入实时对话。 代表作: HeyGen avatar video (2020–); HeyGen Interactive Avatar / LiveAvatar. https://x.com/joshua_xu_
- **Mati Staniszewski** (英国伦敦, 1995–) — ElevenLabs 联合创始人兼首席执行官；其富有表现力的文本转语音、声音克隆与智能体平台，成为许多生成角色默认的声音层。 代表作: ElevenLabs TTS (2023); Eleven v3 (2025); ElevenLabs Agents platform. https://en.wikipedia.org/wiki/Mati_Staniszewski
- **Oliver Cameron** (美国旧金山) — Odyssey 联合创始人兼首席执行官，公司开发可流式输出交互视频的基础世界模型；此前他在 Voyage 与 Cruise 从事自动驾驶。 代表作: Odyssey interactive video (2025); Voyage self-driving (2017–2021). https://x.com/olivercameron
- **Victor Riparbelli** (英国伦敦) — Synthesia 联合创始人兼首席执行官，该虚拟人视频公司由他与研究者 Lourdes Agapito、Matthias Nießner 等共同创立；它较早倡导合成人物的知情同意规则。 代表作: Synthesia avatars (2017–); Synthesia Expressive Avatars (2024). https://x.com/vriparbelli
- **Yan Junjie / 闫俊杰** (中国上海, 1989–) — MiniMax 联合创始人兼首席执行官；这家上海公司推出了海螺（Hailuo）视频模型与 Speech 系列语音合成模型。 代表作: Hailuo Video-01 (2024); Hailuo 02 (2025); MiniMax Speech-02 (2025). https://en.wikipedia.org/wiki/Yan_Junjie

### 艺术家与导演

- **Hsin-Chien Huang / 黄心健** (中国台湾台北, 1966–) — 台湾新媒体艺术家，其 VR 作品（包括与 Laurie Anderson 合作的《To the Moon》以及《Bodyless》）是威尼斯等影展上沉浸式叙事的代表作。 代表作: La Camera Insabbiata / Chalkroom (with Laurie Anderson, Venice 2017); To the Moon (2018); Bodyless (2019). https://hsinchienhuang.com/
- **Ian Cheng** (美国纽约, 1984–) — 创作“实时模拟”的艺术家：开放式的虚拟生态，其中的智能体无剧本地持续行动和变化，是生成式智能体世界在艺术领域的对应物。 代表作: Emissaries trilogy (2015–2017); BOB (Bag of Beliefs) (2018–2019); Life After BOB (2021). https://iancheng.com/
- **Keiichi Matsuda** (英国伦敦) — 设计师与电影人，短片《Hyper-Reality》描绘了一座被增强现实广告与助手智能体淹没的城市；他之后的工作为日常混合现实设计 AI 智能体。 代表作: Hyper-Reality (2016); Merger (2018). http://km.cx/
- **Nonny de la Peña** (美国洛杉矶) — 记者与电影人，被誉为“沉浸式新闻”的开创者；Emblematic Group 创始人，其 VR 作品如《Hunger in Los Angeles》让观众亲身置于重建的真实事件之中。 代表作: Hunger in Los Angeles (Sundance 2012); Project Syria (2014); Immersive Journalism (Presence, 2010). https://en.wikipedia.org/wiki/Nonny_de_la_Pe%C3%B1a
- **Paul Trillo** (美国洛杉矶) — 编剧兼导演，最早受邀用 Sora 创作影片的创作者之一，包括 2024 年为 Washed Out 的《The Hardest Part》制作的音乐录影带，整部片由一次穿过生成场景的无尽推镜构成。 代表作: The Hardest Part (Washed Out, made with Sora, 2024). https://paultrillo.com/
- **Refik Anadol** (美国洛杉矶, 1985–) — 媒体艺术家，其工作室把大规模数据转化为沉浸式、房间尺度的生成作品；“大自然模型”（Large Nature Model）与洛杉矶 Dataland 美术馆把 AI 生成的自然变成人们可以走进去的环境。 代表作: Unsupervised (MoMA, 2022); Large Nature Model (2024); Dataland (Los Angeles). https://refikanadol.com/

### AI 实验室与公司

- **AI at Meta (FAIR & Superintelligence Labs)** (美国门洛帕克) — Meta 的人工智能研究部门，发布了 V-JEPA 2 世界模型、刻画双人面对面行为的 Seamless Interaction 数据集与模型，以及 SAM 3D；其研究主页现以 2026 年的 Muse 系列模型为首。 https://ai.meta.com/research/
- **Alibaba Tongyi Wan / 阿里通义万相** (中国杭州) — 阿里巴巴通义实验室的视频模型系列；Wan 2.1 与 2.2 以开源权重发布，成为开源视频研究与微调的常用底座。 https://wan.video/
- **ByteDance Seed / 字节跳动 Seed** (中国北京) — 字节跳动 2023 年成立的基础模型团队，推出了 Seedance 视频模型、音频驱动人体动画 OmniHuman 以及 Seed3D。 https://seed.bytedance.com/en/
- **Decart** (美国旧金山 / 以色列特拉维夫) — 实时生成视频实验室：Oasis（2024）是一款类 Minecraft 游戏的可玩世界模型，MirageLSD（2025）能对实时摄像头画面进行实时风格转换。 https://decart.ai/
- **ElevenLabs** (英国伦敦 / 美国纽约) — 语音 AI 公司，其文本转语音、声音克隆、音效、音乐与对话智能体平台，为许多生成角色与虚拟人提供声音。 https://elevenlabs.io/
- **General Intuition** — 由 DIAMOND 作者 Eloi Alonso 联合创立的世界模型实验室，利用大量游戏录像训练智能体与世界模型，自称“在空间与时间中行动的前沿实验室”。 https://www.generalintuition.com/
- **Google DeepMind** (英国伦敦) — Google 的人工智能实验室，也是本图库中里程碑作品最多的来源：Genie 世界模型（Genie 1 至 3）、能原生生成声音的 Veo 视频模型、CAT3D 以及 SIMA 游戏智能体。 https://deepmind.google/
- **Gradium** (法国巴黎) — 2025 年 12 月从 Kyutai 分拆出的巴黎语音 AI 公司，由 Neil Zeghidour 领导；它把 Moshi 一脉的研究转化为面向智能体的实时语音 API（低延迟语音合成、转写、实时翻译与声音克隆）。 https://gradium.ai/
- **Hume AI** (美国纽约) — 以情绪科学为基础的语音 AI 公司，推出共情语音接口 EVI 与 Octave 语音合成；现在也提供 600 多个维度的表情测量，用于评估语音智能体，也可用于研究中的情感编码。 https://www.hume.ai/
- **Kling AI (Kuaishou) / 可灵 AI（快手）** (中国北京) — 快手的视频生成产品，于 2024 年 6 月上线，此后快速迭代多个可灵版本，多次位居公开视频竞技场榜首或前列。 https://kling.ai/
- **Kyutai** (法国巴黎) — 巴黎的非营利开放科学 AI 实验室，发布了首个开源全双工语音模型 Moshi，以及实时语音翻译 Hibiki 与语音系统 Unmute；其语音技术于 2025 年分拆为 Gradium 公司。 https://kyutai.org/
- **Luma AI** (美国旧金山) — 从手机上的 NeRF 与高斯泼溅捕捉起步，之后发布 Dream Machine 与 Ray 系列视频模型；其网站现在主推面向创意工作的 AI 智能体。 https://lumalabs.ai/
- **Meta Reality Labs Research** (美国雷德蒙德 / 匹兹堡) — Meta 的 AR / VR 研究部门，Codec Avatars（照片级远程临场化身）、基于高斯泼溅的 Hyperscape 房间捕捉以及 Aria 科研眼镜都出自这里。 https://tech.facebook.com/reality-labs/
- **Microsoft Research** (美国雷德蒙德) — 微软的研究机构，推出了由一张照片生成逼真说话人脸的 VASA-1、与 Xbox 合作的 Muse（WHAM）游戏世界模型，以及被大量 VR 研究使用的开源 Rocketbox 虚拟人库。 https://www.microsoft.com/en-us/research/
- **MiniMax / MiniMax（稀宇科技）** (中国上海) — 上海人工智能公司，旗下海螺（Hailuo）视频模型与 Speech 语音合成模型在公开视频与语音竞技场中名列前茅。 https://www.minimax.io/
- **Mursion** (美国旧金山) — 沉浸式模拟公司，员工可以与会“顶嘴”的虚拟人练习棘手对话；它起初由真人模拟专家为虚拟人配音和操控，如今主推 AI 驱动的技能提升平台。 https://www.mursion.com/
- **NVIDIA Spatial Intelligence Lab** (加拿大多伦多) — NVIDIA 研究感知、建模并与物理世界交互的 AI 的实验室（原多伦多 AI 实验室），推出了 GEN3C、Lyra 等三维一致的视频与世界生成方法，以及 3DGUT 渲染器。 https://research.nvidia.com/labs/sil/
- **OpenAI** (美国旧金山) — 推出了 Sora（2024，把视频模型定位为“世界模拟器”）和能同步生成声音的 Sora 2（2025），以及 gpt-realtime 语音到语音 API。2026 年 4 月关闭 Sora 应用、9 月关闭 Sora API，团队转向世界模拟研究。 https://openai.com/
- **Runway** (美国纽约) — 纽约公司，把视频生成变成电影制作工具（Gen-1 至 Gen-4.5、Act-Two、Aleph），并于 2025 年 12 月推出通用世界模型 GWM-1；它还主办 AI 电影节（AIF）。 https://runway.com/
- **Shanghai AI Laboratory / 上海人工智能实验室** (中国上海) — 2020 年成立的国家支持的研究机构，发布开源模型与评测基准，包括与南洋理工 S-Lab 合作、支撑 VBench 排行榜的 Vchitect 视频生成项目。 https://www.shlab.org.cn/
- **Shengshu Technology (Vidu) / 生数科技** (中国北京) — 源自清华大学的北京公司，推出 Vidu 视频模型（2024 年 4 月首发），以“参考生视频”保持角色一致性见长。 https://www.vidu.com/
- **Simile** (美国帕洛阿尔托) — 由“生成式智能体”作者 Joon Sung Park 创立的帕洛阿尔托公司，提供关于顾客、员工或人群如何回应变化的模拟服务；2026 年宣布完成 2 亿美元 B 轮融资，估值 20 亿美元。 https://www.simile.com/
- **Tencent Hunyuan / 腾讯混元** (中国深圳) — 腾讯的基础模型团队，是该领域最活跃的开源权重来源之一：HunyuanVideo、Hunyuan3D、HunyuanWorld 以及游戏视频模型 GameCraft。 https://hunyuan.tencent.com/
- **World Labs** (美国旧金山) — 由李飞飞、Justin Johnson、Ben Mildenhall 与 Christoph Lassner 创立的空间智能公司；其产品 Marble 能由文字、图像、视频和三维布局生成持久、可编辑的三维世界。 https://www.worldlabs.ai/

### 高校实验室

- **Event Lab (Universitat de Barcelona)** (西班牙巴塞罗那) — Mel Slater 在巴塞罗那领导的“神经科学与技术中的虚拟环境”实验室，以身体拥有感、具身以及人们对虚拟他人反应的研究著称。 https://www.ub.edu/eventlab/EventLab/
- **Inria GraphDeco** (法国索菲亚-安提波利斯) — George Drettakis 在 Inria 索菲亚-安提波利斯中心的图形学研究组，3D 高斯泼溅在此诞生（SIGGRAPH 2023 最佳论文）并开源发布。 https://team.inria.fr/graphdeco/
- **Max Planck Institute for the Study of Crime, Security and Law / 马克斯·普朗克犯罪、安全与法律研究所** (德国弗莱堡) — 位于弗莱堡的研究所，其犯罪学部门由 Jean-Louis van Gelder 领导，用虚拟现实在接近真实的条件下研究犯罪、受害与决策。 https://csl.mpg.de/en
- **MMLab@NTU / S-Lab** (新加坡) — 南洋理工大学多媒体实验室（吕健勤、刘子纬），大量开源视频、三维与虚拟人生成模型以及 VBench 评测基准的来源。 https://www.mmlab-ntu.com/
- **Reality Design Lab / 现实设计实验室** — 胡博涛（Botao “Amber” Hu）的设计研究实验室，研究混合现实与生成式沉浸体验，开发开源 HoloKit 工具包；本图库 Generative Immersive Reality Inspire 即由其制作。 https://reality.design/
- **Stanford Virtual Human Interaction Lab (VHIL)** (美国斯坦福) — Jeremy Bailenson 的实验室，研究 VR 与化身会对人产生什么影响，从普罗透斯效应到“Zoom 疲劳”与大规模 VR 课程。 https://vhil.stanford.edu/
- **Stanford Vision and Learning Lab (SVL)** (美国斯坦福) — 斯坦福大学由李飞飞、吴佳俊等人组成的实验室，构建具身智能体的模拟环境与基准（BEHAVIOR、OmniGibson），以及 WorldScore 等世界生成评测。 https://svl.stanford.edu/
- **UCL Virtual Environments and Computer Graphics (VECG)** (英国伦敦) — 伦敦大学学院计算机系研究组，临场感研究在 1990–2000 年代的大量奠基工作在此完成，包括 Slater 的虚拟米尔格拉姆实验（2006）与以阿森纳球迷为对象的旁观者研究（2013）；至今仍研究 VR、协同虚拟环境与图形学。 http://vecg.cs.ucl.ac.uk/
- **USC Institute for Creative Technologies** (美国洛杉矶) — 由美国陆军资助的南加州大学研究中心，二十多年来为训练与治疗构建交互式虚拟人，包括 Bravemind VR 暴露疗法与 SimSensei 虚拟访谈者。 https://ict.usc.edu/

### 会议与研讨会

- **ACM CHI** — ACM 人机交互大会，规模最大的人机交互会议，生成式 XR 系统、大模型智能体研究与 VR 用户研究在此发表。 https://chi2027.acm.org/
- **ACM IVA (Intelligent Virtual Agents)** — ACM 智能虚拟智能体会议：关注具身对话角色、非语言行为生成，以及它们在训练、健康与研究中的应用。 https://iva.acm.org/
- **ACM SIGGRAPH & SIGGRAPH Asia** — 最重要的计算机图形学会议，NeRF 时代的渲染、3D 高斯泼溅、虚拟人与动作生成论文在此发表，并设有沉浸式展区与 Real-Time Live 实时演示。 https://s2026.siggraph.org/
- **ACM UIST** — ACM 用户界面软件与技术研讨会，《Generative Agents》于 2023 年在此获最佳论文，许多 AR 创作与人机协同 AI 系统在此首次发表。 https://uist.acm.org/
- **AIF (Runway AI Festival)** — Runway 主办的年度节展，2023 年以“AI 电影节”名义创办，放映使用生成式视频工具制作的短片。 https://aif.runwayml.com/
- **CVPR** — IEEE/CVF 计算机视觉与模式识别会议，规模最大的视觉会议，视频生成、三维 / 四维重建与世界生成论文和研讨会的主要阵地。 https://cvpr.thecvf.com/
- **I/ITSEC** (美国奥兰多) — 奥兰多举办的跨军种 / 产业训练、模拟与教育会议，军事与工业模拟训练领域规模最大的会议，ICT 的虚拟人训练系统曾在此发表。 https://www.iitsec.org/
- **ICCV & ECCV** — 国际计算机视觉大会与欧洲计算机视觉会议，隔年交替举办（ICCV 奇数年，ECCV 偶数年）；NeRF 发表于 ECCV 2020，DiT 发表于 ICCV 2023。 https://iccv.thecvf.com/
- **ICLR** — 国际学习表征会议，采用 OpenReview 公开评审；GameNGen 以及许多视频与世界模型论文发表于此。 https://iclr.cc/
- **IEEE ISMAR** — IEEE 混合与增强现实国际研讨会，AR / MR 研究的主要会议，生成式与大模型驱动的 XR 论文日益增多。 https://ismar.net/
- **IEEE VR** — IEEE 虚拟现实与三维用户界面会议，VR 系统、临场感与具身研究的主要会议；其论文发表于 IEEE TVCG。 https://ieeevr.org/
- **NeurIPS** — 神经信息处理系统大会，大量世界模型、扩散模型与智能体研究在此发表，并设有数据集与基准赛道。 https://neurips.cc/
- **Venice Immersive** (意大利威尼斯) — 威尼斯国际电影节的沉浸式单元，自 2017 年起是 VR、MR 与沉浸式作品最重要的展映与竞赛平台。 https://www.labiennale.org/en/cinema/2026/venice-immersive

### 期刊

- **ACM Transactions on Graphics (TOG)** — 最重要的图形学期刊，刊载 SIGGRAPH 与 SIGGRAPH Asia 的技术论文，包括 3D 高斯泼溅与 instant-ngp。 https://en.wikipedia.org/wiki/ACM_Transactions_on_Graphics
- **Computers in Human Behavior** — 爱思唯尔出版的计算机使用心理学期刊，常发表关于虚拟人、化身以及 VR 对行为影响的研究。 https://en.wikipedia.org/wiki/Computers_in_Human_Behavior
- **Frontiers in Virtual Reality** — 2020 年创刊的开放获取期刊，涵盖 VR / AR 技术及其在心理学、健康与训练中的应用。 https://www.frontiersin.org/journals/virtual-reality
- **IEEE Transactions on Visualization and Computer Graphics (TVCG)** — IEEE 期刊，刊载 IEEE VR 与 ISMAR 的期刊论文，是 VR 系统与感知研究的主要存档渠道。 https://www.computer.org/csdl/journal/tg
- **PRESENCE: Virtual and Augmented Reality** — 麻省理工学院出版社期刊，1992 年以 Presence: Teleoperators and Virtual Environments 之名创刊，临场感理论、沉浸式新闻与大量早期 VR 行为研究在此发表。 https://en.wikipedia.org/wiki/Presence:_Teleoperators_%26_Virtual_Environments

### 通讯、播客与媒体

- **80 Level** — 面向游戏与三维美术从业者的行业网站，追踪生成式三维、高斯泼溅与实时工具进入生产流程的进展。 https://80.lv/
- **Bilawal Sidhu** — 内容创作者，曾任 Google 地图 / AR 产品经理；其 YouTube 与社交账号演示并讲解三维捕捉、高斯泼溅与生成视频。 https://www.youtube.com/@bilawalsidhu
- **Radiance Fields** — 专注辐射场的新闻网站与通讯：高斯泼溅、NeRF，以及基于它们的捕捉工具与平台。 https://radiancefields.com/
- **Road to VR** — 老牌 XR 新闻网站，报道头显、平台与沉浸式软件，包括 Quest、Vision Pro 与 Android XR 上的生成式功能。 https://roadtovr.com/
- **Two Minute Papers** — Károly Zsolnai-Fehér 的 YouTube 频道，用短视频讲解图形学与 AI 新论文；快速看到视频生成、高斯泼溅与模拟新成果实际运行效果的途径。 https://www.youtube.com/@TwoMinutePapers
- **UploadVR** — XR 新闻网站，报道 VR 与 AR 硬件、应用与平台变化，常对新的沉浸式功能进行上手测试。 https://www.uploadvr.com/
- **Voices of VR Podcast** — Kent Bye 主持的播客，以一千多期访谈记录 XR 的口述历史，受访者包括沉浸式艺术家、研究者与开发者，也涉及 XR 伦理与 AI。 https://voicesofvr.com/

### 社区与目录

- **Awesome 3D Gaussian Splatting** — MrNeRF 维护、持续更新的高斯泼溅论文、代码与工具清单，按主题分类，从压缩到虚拟人与 4D。 https://github.com/MrNeRF/awesome-3D-gaussian-splatting
- **Awesome Talking Head Generation** — GitHub 上的说话人像与音频驱动人像生成论文、数据集与代码精选清单。 https://github.com/harlanhong/awesome-talking-head-generation
- **Awesome Video Diffusion** — 新加坡国立大学 Show Lab 维护的视频扩散论文与代码清单，从文生视频到编辑、控制与长视频。 https://github.com/showlab/Awesome-Video-Diffusion
- **Awesome World Models** — GitHub 上的世界模型论文精选清单，涵盖游戏、具身智能、自动驾驶与视频生成。 https://github.com/knightnemo/Awesome-World-Models
- **C2PA (Content Credentials)** — 内容来源与真实性联盟（C2PA），维护开放的“内容凭证”（Content Credentials）标准；多家视频与图像生成服务会在输出中附加该凭证，标明内容由 AI 生成。 https://c2pa.org/
- **Hugging Face Daily Papers** — Hugging Face 上每日更新、按投票排序的 arXiv 新论文列表，由 AK（@_akhaliq）发起，并关联模型、数据集与演示 Space；追踪生成视频、三维与世界模型新发布最快的途径。 https://huggingface.co/papers
- **Hugging Face Spaces** — 开源模型的在线演示平台，许多视频、三维、虚拟人与语音模型在发布当天即可在浏览器中试用。 https://huggingface.co/spaces

### 排行榜与竞技场

- **3D Arena** — Hugging Face 上的竞技场，用户在成对的生成三维模型之间投票，为图生三维模型排名。 https://huggingface.co/spaces/3d-arena/3d-arena
- **Arena (formerly LMArena)** — 从 Chatbot Arena 与 LMArena 发展而来的众包投票模型排名网站；除文本模型外，也对文生视频、图生视频与图像模型排名。 https://arena.ai/
- **Artificial Analysis Speech Arena** — 盲测人类偏好竞技场，对文本转语音模型与声音进行排名，并比较价格与延迟。 https://artificialanalysis.ai/text-to-speech/arena
- **Artificial Analysis Video Arena** — 盲测两两比较的人类偏好竞技场，为文生视频与图生视频模型（含声音与不含声音）给出 Elo 排名，并附价格与速度数据。 https://artificialanalysis.ai/video/arena
- **TTS Arena** — Hugging Face 社区竞技场，听众在两段文本转语音输出之间投票，覆盖开源与商业声音。 https://huggingface.co/spaces/TTS-AGI/TTS-Arena-V2
- **VBench Leaderboard** — VBench 排行榜，从主体一致性、运动平滑度、物理合理性等 16 个维度为视频生成模型打分。 https://huggingface.co/spaces/Vchitect/VBench_Leaderboard
- **WorldScore** — 斯坦福推出的世界生成统一评测基准与排行榜，从可控性、质量与动态性比较三维场景生成、四维生成与视频模型。 https://haoyi-duan.github.io/WorldScore/

## 机构与创作者

- **Google DeepMind** (32) — 谷歌旗下的人工智能研究实验室. 谷歌的人工智能实验室（Gemini、Genie、Veo）。其 SIMA 项目训练能在商业三维游戏中听从语言指令的智能体，SIMA 2 还进入了 Genie 3 生成的世界；它也维护用于生成式社会模拟的 Concordia 库。 https://deepmind.google
- **Meta** (29) — Meta AI 研究院 / FAIR / Reality Labs 现实实验室. Meta 的 AI 研究（FAIR）与 Reality Labs 团队；在三维资产方面发布了 Meta 3D Gen、SAM 3D Objects 与 Body、ShapeR 以及 Meta Motivo 人形模型。 https://ai.meta.com
- **NVIDIA** (29) — GPU 与人工智能计算公司. GPU 厂商，并推出 ACE：一套面向游戏角色的语音、语言与面部动画模型；其研究团队还开发了 Voyager 与 NitroGen 等游戏智能体。 https://research.nvidia.com
- **Google** (21) — 谷歌研究院、Google Labs 与 Google AR. 谷歌在 DeepMind 之外的研究与产品团队；谷歌研究院发表了 DreamFusion，这篇 2022 年的论文开启了借助二维扩散模型的文生三维路线。 https://research.google
- **ByteDance Seed** (16) — 字节跳动的基础模型研究团队. 构建字节跳动基础模型（豆包、Seedance、UI-TARS）的研究团队；2025 年发布游戏智能体 Game-TARS 与 Lumine。 https://seed.bytedance.com
- **Mel Slater** (14) — 虚拟现实研究者，巴塞罗那大学 EventLab 联合主任. 从计算机科学转向临场感研究，提出“地点错觉”与“似真错觉”，主持了虚拟米尔格拉姆、旁观者与身体拥有感等一系列实验。
- **Tencent Hunyuan** (14) — 腾讯的基础模型团队. 腾讯混元团队发布覆盖文本、图像、视频、三维（混元3D 1.0 至 3.x、HY 3D Studio）和动作（HY-Motion）的开源与闭源模型。 https://hunyuan.tencent.com
- **Microsoft** (13) — 微软研究院. 微软研究院发布了 TRELLIS（2024）和 TRELLIS.2（2025），两者都是基于结构化三维潜变量、采用 MIT 许可的三维生成模型。 https://www.microsoft.com/research
- **Kuaishou** (11) — 短视频公司（可灵团队）. 快手开发可灵视频模型并开源了 LivePortrait，其可灵团队还发布了实时自回归数字人模型 MIDAS。 https://www.kuaishou.com
- **Alibaba Tongyi (Qwen)** (9) — 阿里巴巴通义实验室与 Qwen 团队. 阿里巴巴通义实验室开发千问 Qwen 系列、万相 Wan 视频模型以及 Fun-Audio / CosyVoice 语音模型，其中许多以开源权重发布。 https://wan.video
- **OpenAI** (9) — 人工智能研究与产品公司. GPT、Sora 与实时语音模型的开发者；2019 年的多智能体捉迷藏研究展示了智能体在三维物理世界中自发学会使用工具。 https://openai.com
- **Runway** (9) — AI 视频公司. Gen 与 Aleph 视频模型的开发者，也做世界模型研究（GWM-1）；同时提供应用与开发者 API。 https://runwayml.com
- **Stability AI** (7) — 开源生成模型公司. Stable Diffusion 的开发公司，也发布了开源三维模型：TripoSR（与 Tripo AI 合作）、Stable Fast 3D、SPAR3D 和 Stable Video 3D。 https://stability.ai
- **Apple** (6) — 消费科技公司. Apple Vision Pro 会为佩戴者生成 Persona：一个由面部扫描重建、由头显传感器驱动的三维化身。 https://machinelearning.apple.com
- **Decart** (6) — 构建实时生成视频与世界模型的 AI 实验室. 初创公司，推出实时生成的类 Minecraft 世界 Oasis 与实时视频到视频模型 MirageLSD，并通过 API 提供。 https://decart.ai
- **World Labs** (6) — 空间智能公司. 由李飞飞等人创立，开发 Marble 世界模型与 Spark 泼溅渲染器。 https://www.worldlabs.ai
- **Deemos (Hyper3D Rodin)** (5) — Hyper3D Rodin 背后的三维生成公司. 源自上海科技大学的公司，开发 Rodin 系列三维生成模型（Gen-1 基于 CLAY 研究模型，之后有 Gen-1.5、Gen-2、Gen-2.5）和 ChatAvatar 人脸生成，通过 hyper3d.ai 和 API 提供服务。 https://hyper3d.ai
- **Luma AI** (5) — 生成式 AI 公司（三维拍摄、视频）. 以 NeRF 拍摄应用和 Genie 文生三维起家，之后把重心转向视频生成（Dream Machine、Ray 系列模型）。 https://lumalabs.ai
- **Skywork (Kunlun Tech)** (5) — 昆仑万维旗下人工智能业务. 昆仑万维的人工智能业务，开源 SkyReels 视频模型与 Matrix 世界模型。 https://www.skywork.ai
- **Snap Inc.** (5) — 相机公司；Snapchat、Lens Studio 与 Spectacles / SPECS AR 眼镜. Snapchat 镜头（每天使用数十亿次）的开发者，也推出独立 AR 眼镜：面向开发者的 Spectacles（2024）与消费级 SPECS（2026）。 https://research.snap.com
- **Tavus** (5) — 实时对话视频 AI 公司. Tavus 开发面对面 AI 对话所需的模型：Phoenix（渲染）、Raven（感知）、Sparrow（轮流发言），以及 2026 年 10 月发布的统一全双工视频到视频模型 Griffin。其对话视频接口（CVI）API 和面向个人用户的 PALs 都基于这些模型。 https://www.tavus.io
- **Tripo AI (VAST)** (5) — 三维生成公司（VAST）. VAST 开发 Tripo 三维生成模型与 Tripo Studio，并发布 TripoSR（与 Stability AI 合作）、TripoSG、UniRig、TripoSplat 等开源研究。 https://www.tripo3d.ai/
- **USC Institute for Creative Technologies** (5) — 南加州大学下属的大学附属研究中心. 1999 年在美国陆军资助下成立，把人工智能、图形与叙事结合用于训练和健康；虚拟人工具包、SimSensei 与 Bravemind 均出自这里。 https://ict.usc.edu/
- **Epic Games** (4) — 游戏开发商与引擎厂商（Fortnite、Unreal Engine）. Fortnite 与 Unreal Engine 的开发商；2025 年在 Fortnite 中上线可语音对话的 AI 达斯·维达，随后以 Persona 装置（后更名 Conversations）向创作者开放这项技术。 https://www.unrealengine.com
- **Jeremy Bailenson** (4) — 斯坦福大学虚拟人交互实验室（VHIL）创始主任. 传播学学者，研究化身、虚拟身体与沉浸式媒体如何改变态度与行为，从“普罗透斯效应”到大规模 VR 实地研究。 https://vhil.stanford.edu/
- **Kyutai** (4) — 非营利开放科学 AI 实验室. Kyutai 是位于巴黎的非营利研究实验室，由 Iliad、CMA CGM 与 Schmidt Sciences 资助，语音模型均公开发布。 https://kyutai.org
- **Meshy** (4) — AI 三维生成公司. Meshy 的开发公司，提供文生三维、图生三维、AI 贴图、自动绑定与动画的网页、应用和 API；模型从 Meshy-1（2023 年）迭代到 Meshy 7.1（2026 年 9 月）。 https://www.meshy.ai/
- **Adobe** (3) — 创意软件公司（Adobe 研究院）. Photoshop 和 Substance 3D 的开发商；Adobe 研究院参与了 LRM，这是首个用于单张图像三维重建的大型重建模型。 https://research.adobe.com
- **Character.AI** (3) — 面向大众的 AI 角色平台. Character.AI 运营一个大型 AI 角色聊天平台，并开发视频模型（AvatarFX、TalkingMachines）为角色配上面孔。 https://character.ai
- **Doron Friedman** (3) — 赖克曼大学先进现实实验室负责人. 研究虚拟人、远程临场与面向心理健康的 VR；其实验室开发由大语言模型驱动的虚拟人和自动化情境生成流程。
- **ElevenLabs** (3) — AI 音频公司. ElevenLabs 开发语音合成、声音克隆、对话智能体、音效与音乐模型，在媒体制作中被广泛使用。 https://elevenlabs.io
- **Hume AI** (3) — 语音 AI、表达测量与评测公司. Hume AI 开发共情语音接口 EVI、Octave 语音合成模型以及开源的 TADA 模型；2026 年其主打表达测量 API（50 多种语言、600 多个表达维度），以及用于评测真实场景语音 AI 的工具与基准，包括 RW-Voice-EQ Bench。 https://www.hume.ai
- **Jean-Louis van Gelder** (3) — 马克斯·普朗克犯罪、安全与法律研究所所长；莱顿大学教授. 犯罪学家与心理学家，用 VR 研究犯罪决策（虚拟入室盗窃项目）和“未来自我”干预。 https://csl.mpg.de/en
- **Joon Sung Park** (3) — 人机交互研究者，Simile 联合创始人兼 CEO. 斯坦福大学计算机科学博士，2023 年以 Smallville 论文提出生成式智能体，随后用 1,052 名美国人的两小时访谈构建个体智能体。与 Michael Bernstein、Percy Liang 共同创办 Simile。
- **Odyssey** (3) — 世界模型 AI 实验室. 由 Oliver Cameron 与 Jeff Hawke 于 2023 年创立的 AI 实验室，致力于通用世界模型，先后发布 Odyssey-1、-2、-3、多智能体 Agora 系列模型及 API。 https://odyssey.ml
- **Robbyant** (3) — 蚂蚁集团具身智能公司. 蚂蚁集团旗下的具身智能公司，发布面向机器人与空间感知的开源 LingBot 系列模型。 https://technology.robbyant.com
- **Roblox** (3) — 在线游戏平台. 用户在此搭建并游玩各类体验的平台；其基础 AI 团队开发了部分开源的 Cube 三维基础模型，以及在游戏内使用的三维与 4D 生成功能。 https://corp.roblox.com
- **Ryo Suzuki** (3) — 科罗拉多大学博尔德分校 ATLAS 研究所与计算机系助理教授，Programmable Reality Lab 负责人. 人机交互研究者，研究 AR/VR、实体界面与 AI 的交叉；实验室的“生成式 AR”方向希望把物理世界变成生成式 AI 的画布。 https://ryosuzuki.org
- **Stijn Spanhove** (3) — In The Pocket 公司 XR 开发者；Snap Spectacles 创作者. 持续发布把 AR 眼镜、Vision Pro 与生成模型结合起来的短小概念验证。
- **Agora** (2) — 实时互动平台. 运营面向音视频 SDK 的全球实时网络，推出对话式 AI 引擎，并支持开源 TEN Framework。 https://www.agora.io
- **Albert "Skip" Rizzo** (2) — 南加州大学创意技术研究所医学虚拟现实部门主任. 临床心理学家，开发了用于 PTSD 暴露疗法的 Virtual Iraq/Afghanistan 与 Bravemind，并主持虚拟病人研究。
- **Bernhard Kerbl** (2) — Inria / 维也纳工业大学研究者. 3D 高斯泼溅（SIGGRAPH 2023）共同第一作者，也是其超大场景层级版本的第一作者。
- **Botao 'Amber' Hu** (2) — 牛津大学研究者；Reality Design Lab 创始人；HoloKit 发明者. 设计师与研究者（清华大学本科、斯坦福大学人工智能硕士），主持 Reality Design Lab 在具身与社交混合现实、思辨设计和生成式未来构想方面的研究；实验室作品曾在 SIGGRAPH、CHI、TEI 与 Ars Electronica 展出。 https://reality.design
- **Chuan Guo** (2) — 人体动作生成研究者. 研究者（阿尔伯塔大学，后进入业界），创建了 HumanML3D 数据集（CVPR 2022）和 MoMask（CVPR 2024）。 https://ericguo5513.github.io/
- **Convai** (2) — 面向游戏与 XR 角色的对话式 AI 平台. 为 Unreal Engine、Unity 与网页三维场景提供能说话、感知和行动的角色引擎与插件；2023 年与英伟达用 ACE 合作制作了 Kairos 演示。 https://convai.com/
- **Daniel Freeman** (2) — 牛津大学临床心理学教授. 主持牛津大学针对恐高、偏执以及精神病患者广场回避（gameChange）的自动化 VR 治疗研究。 https://gamechangevr.com/
- **Evonne Ng** (2) — 双人互动行为与手势生成研究者. Evonne Ng（加州大学伯克利分校，后加入 Meta）主导了 Learning to Listen（CVPR 2022）和 Audio2Photoreal（2024），建模对话中倾听者的脸和身体如何回应。 https://evonneng.github.io
- **Hong-Xing (Koven) Yu** (2) — 斯坦福大学研究者. 斯坦福大学吴佳俊组的计算机视觉研究者，WonderJourney 与 WonderWorld 的第一作者。 https://kovenyu.com
- **Inria GraphDeco** (2) — Inria 图形学研究组. 由 George Drettakis 领导的 Inria 蔚蓝海岸大学研究组，3D 高斯泼溅及其层级扩展的出处。 https://team.inria.fr/graphdeco/
- **Inworld AI** (2) — 实时 AI 公司，前身是游戏 AI 角色引擎. 2021 年成立，最初为游戏 AI 角色打造引擎，育碧 NEO NPC 与英伟达 Covert Protocol 演示都使用了它。到 2026 年，它主要推广实时语音模型（TTS、STT、语音到语音）以及面向消费级 AI 应用的运行时。 https://inworld.ai/
- **Jianyuan Wang** (2) — 牛津 VGG / Meta AI 研究者. VGGT（CVPR 2025 最佳论文）与 VGGT-Ω（CVPR 2026 Oral）第一作者，牛津视觉几何组与 Meta 的合作工作。
- **Jiawei Ren** (2) — 南洋理工大学 S-Lab / NVIDIA 研究者. DreamGaussian4D 与 L4GM（NeurIPS 2024，与 NVIDIA 合作）的第一作者。
- **Jiwen Yu** (2) — 香港大学研究者. 香港大学博士研究者，与快手可灵团队合作研究交互式视频生成。 https://yujiwen.github.io
- **Jonathan T. Barron** (2) — Google DeepMind 研究科学家. Google 研究者，mip-NeRF、mip-NeRF 360、Zip-NeRF 等工作以及多项辐射场质量基准的作者。
- **Jonathon Luiten** (2) — Meta 研究者. Dynamic 3D Gaussians（3DV 2024）第一作者，在 Meta 参与了 BulletGen。
- **Junxuan Li** (2) — Meta Codec Avatars 实验室研究科学家. Junxuan Li 是 URAvatar（SIGGRAPH Asia 2024）和大规模 Codec Avatars（CVPR 2026）的第一作者。 https://junxuan-li.github.io
- **KRAFTON** (2) — 电子游戏发行商. 韩国游戏公司，发行《绝地求生》与 inZOI；与英伟达 ACE 合作推出运行在本地小语言模型上的“可共玩角色”（CPC）。 https://www.krafton.com/
- **Keiichi Ihara** (2) — Programmable Reality Lab（科罗拉多大学博尔德分校）与筑波大学博士生. 人机交互研究者，构建把电影、教学视频等二维媒介转化为空间内容的混合现实系统。
- **Lei Zhang** (2) — 人机交互研究者（密歇根大学博士，现任职于新泽西理工学院）. 研究沉浸式创作中的人机共创，从 VRCopilot（密歇根大学）到 Capybara（与普林斯顿 HCI 实验室合作）。
- **Lightricks** (2) — 创意应用公司，LTX 模型开发者. Facetune 与 LTX Studio 的开发者，发布开源的 LTX-Video、LTX-2 与 LTX-2.5 模型。 https://ltx.io
- **Matthew Tancik** (2) — 研究者，Nerfstudio 联合创建者. NeRF 合著者，在伯克利主导了 Nerfstudio，后加入 Luma AI。
- **MiniMax** (2) — 大模型公司（海螺 AI）. 海螺视频模型、MiniMax 语言模型与语音模型的开发者；2026 年 7 月以开源权重发布 H3 视频模型。 https://www.minimax.io
- **NAVER LABS Europe** (2) — NAVER 的欧洲研究院. 韩国 NAVER 公司位于格勒诺布尔的研究中心，DUSt3R / MASt3R 系列三维基础模型的出处。 https://europe.naverlabs.com/
- **Niantic Spatial** (2) — 从 Niantic 独立出来的地理空间 AI 公司. 在 Niantic 于 2025 年出售游戏业务后，专注大型地理空间模型、视觉定位与 AR 地图。 https://www.nianticspatial.com/
- **PixVerse** (2) — AI 视频公司（爱诗科技）. 总部位于北京的 PixVerse 视频生成器与应用的开发者，由爱诗科技打造；2026 年推出实时世界模型 R1 与 R2。 https://pixverse.ai
- **PlayCanvas** (2) — 网页图形引擎公司（Snap 旗下）. 开发开源 PlayCanvas 引擎与 SuperSplat 高斯泼溅编辑器。 https://playcanvas.com/
- **Qianqian Wang** (2) — 加州大学伯克利分校研究者. 伯克利研究者，Shape of Motion 与 CUT3R 第一作者。
- **Reality Design Lab** (2) — 由 Botao 'Amber' Hu 主持的混合现实独立设计研究实验室. 以“设计新现实”为宗旨，创作混合现实艺术作品，开发开源工具（HoloKit、HoloMask、Unity 版 MultipeerConnectivity），并开展教学项目；作品曾在 SIGGRAPH、CHI、IEEE VR 与 Ars Electronica 展出。 https://reality.design
- **Samsung Electronics** (2) — 电子公司；Galaxy XR 头显制造商. 与谷歌、高通共同开发 Android XR，并于 2025 年 10 月推出 Galaxy XR 头显。 https://www.samsung.com
- **Shengshu Technology (Vidu)** (2) — 源自清华大学的视频生成公司. 由清华大学研究者创立；2024 年 4 月发布 Vidu，此后推出 Q 系列与实时 S 系列模型。 https://www.vidu.com
- **SpAItial** (2) — 三维世界模型初创公司（Echo）. 由慕尼黑工业大学教授 Matthias Niessner 联合创立的初创公司，研发空间基础模型；2025 年获 1300 万美元种子轮融资，先后发布 Echo（2025 年 12 月）和 Echo-2（2026 年 4 月）。 https://www.spaitial.ai
- **StepFun** (2) — 中国基础模型公司. 阶跃星辰开发 Step 系列语言、多模态与音频模型，并开源了其中多款。 https://www.stepfun.com
- **Ubisoft** (2) — 电子游戏发行商. 《刺客信条》《全境封锁》的法国发行商；其巴黎团队在 2024 年展示 NEO NPC 原型，2025 年推出可游玩的 Teammates 实验。 https://www.ubisoft.com/
- **Wayve** (2) — 具身智能自动驾驶公司. 总部位于伦敦的公司，开发端到端驾驶模型，并自 2023 年起推出 GAIA 系列生成式驾驶世界模型。 https://wayve.ai
- **Weihao Tan** (2) — 人工智能研究者，游戏智能体方向. Cradle（2024）与 Lumine（2025，字节跳动 Seed）的第一作者：前者通过截图和键鼠输出游玩《荒野大镖客 2》，后者能实时完成数小时的《原神》任务。
- **ZJU3DV** (2) — 浙江大学三维视觉组. 浙江大学 CAD&CG 国家重点实验室周晓巍、彭思达团队，长期研究动态人体与场景捕捉。 https://zju3dv.github.io/
- **Zhaoxi Chen** (2) — 南洋理工大学 S-Lab 博士研究者. 前馈式图像到 4D 模型 4DNeX 的第一作者。 https://frozenburning.github.io
- **Ziqi Huang** (2) — 南洋理工大学 S-Lab 研究者. 在刘子纬课题组研究视频生成及其评测，VBench 与 VBench++ 的第一作者。 https://ziqihuangg.github.io
- **1X Technologies** (1) — 人形机器人公司. 挪威与美国背景的人形机器人公司，产品包括 EVE 与 NEO。 https://www.1x.tech
- **4DV.ai** (1) — 4D 高斯视频创业公司. 基于高斯泼溅开发 4D 视频拍摄、播放与编辑工具的创业公司，CEO 孙佳明是 FreeTimeGS 的合著者。据 Radiancefields.com 报道，其 Infinite Studio 演示获得 SIGGRAPH 2025 Real-Time Live 最佳展示奖。 https://www.4dv.ai
- **Ailing Zeng** (1) — 人体动作与角色生成研究者. Ailing Zeng 是 LPM 1.0（2026）的第一作者和共同负责人，这是一个面向实时对话的 17B 视频角色表演模型。 https://large-performance-model.github.io
- **Akilan Amithasagaran** (1) — CLiVR（2025）第一作者. 与医学教育合作者一起开发了 CLiVR——一个基于 Meta Quest 3、由大语言模型驱动的虚拟病人系统。
- **Akio Kodaira** (1) — 实时扩散流水线开发者. StreamDiffusion 的主要作者，与 UC Berkeley 等研究者合作完成。
- **Alessio Grancini** (1) — AR 工程师；Snap Spectacles 开发者关系. AR 工程师（曾任职 Magic Leap），制作并讲解 Spectacles 实验项目。 https://www.alessiograncini.com
- **Alexander Raistrick** (1) — 普林斯顿视觉与学习实验室研究者. 普林斯顿大学邓嘉组的博士研究者，Infinigen、Infinigen Indoors 与 ProcFunc 的第一作者。 https://infinigen.org
- **Alibaba Quark** (1) — 阿里巴巴夸克 / 千问应用研究团队. 阿里巴巴千问应用事业群的夸克团队与中国科学技术大学合作发布了 14B 流式虚拟人模型 Live Avatar。
- **Allen Institute for AI (Ai2)** (1) — 非营利 AI 研究机构. 非营利研究机构，开发了 AI2-THOR、ProcTHOR、Objaverse 与 Holodeck。 https://allenai.org
- **Alon Shoa** (1) — 赖克曼大学先进现实实验室研究员. 开源 XR 大语言模型虚拟人平台 Milo 的开发者。
- **Altera (Fundamental Research Labs)** (1) — AI 智能体初创公司. 构建自主数字人的初创公司；2024 年推出 Project Sid，在 Minecraft 中模拟 10 到 1,000 多个 LLM 智能体。其 YouTube 频道现名 Fundamental Research Labs。
- **Alvaro Collet** (1) — 微软研究者（2015）. 《High-Quality Streamable Free-Viewpoint Video》（SIGGRAPH 2015）第一作者，该系统是微软混合现实捕捉工作室的基础。
- **Amazon** (1) — 亚马逊（AWS 与 Amazon AGI）. 亚马逊开发 Nova 系列基础模型，在 AWS Bedrock 上提供服务。 https://aws.amazon.com/ai/generative-ai/nova/
- **Amina Kobenova** (1) — 人机交互研究者；与微软合作者完成 Social Conjuring 的第一作者. 研究虚拟世界中借助生成式 AI 的多人社交创作；合作者包括 Judith Amores 与 Jaron Lanier。
- **Amir Bar** (1) — Meta FAIR 研究员，导航世界模型第一作者. 计算机视觉研究者（Meta FAIR、特拉维夫大学），研究视觉预测与世界模型。 https://www.amirbar.net
- **Anam** (1) — 实时交互虚拟人公司. Anam 开发 CARA 系列实时虚拟人扩散模型，并提供面对面 AI 智能体的 API。 https://anam.ai
- **Andreessen Horowitz (a16z)** (1) — 风险投资机构（a16z 基础设施团队）. 风险投资机构，其基础设施团队于 2023 年与 Convex 合作发布 AI Town：一个 MIT 许可、可在浏览器中运行的 LLM 角色小镇起步套件。 https://a16z.com/
- **Andrew Liu** (1) — Google Research 研究者. Infinite Nature（ICCV 2021）的第一作者，与 Noah Snavely、Angjoo Kanazawa 等在 Google Research 合作。
- **Anuttacon** (1) — AI 游戏工作室. 由米哈游联合创始人蔡浩宇创办的 AI 原生游戏工作室；2025 年发布《Whispers from the Star》。 https://www.anuttacon.com/
- **Anything World** (1) — AI 绑定与动画公司. 为任意三维模型（包括动物和交通工具）提供自动绑定与动画的公司，提供网页应用和游戏引擎插件。 https://anything.world/
- **AppliedVR** (1) — 数字疗法公司. RelieVRx 的开发商，这是一款经美国 FDA De Novo 途径授权、用于慢性下背痛的居家 VR 项目。 https://www.appliedvr.io/
- **Arcturus** (1) — 体积视频软件公司. HoloSuite 的开发者，这套工具用于编辑、压缩与流式传输体积视频，后来转向基于高斯泼溅的体育回放。 https://arcturus.studio/
- **Arena (formerly LMArena)** (1) — 众包 AI 评测平台. 源自加州大学伯克利分校的 LMSYS Chatbot Arena，运营文本、视觉、图像与视频模型的公开盲投排行榜。 https://arena.ai
- **Ars Electronica Futurelab** (1) — Ars Electronica 的艺术与科技研究实验室. 处于艺术、技术与社会交叉点的跨学科实验室，以 Deep Space 8K 及与产业伙伴的合作闻名。 https://ars.electronica.art/futurelab/en/
- **Artificial Analysis** (1) — 独立 AI 基准评测公司. 跨服务商评测模型的质量、价格与速度，并运营图像与视频盲投竞技场。 https://artificialanalysis.ai
- **Avaturn Live** (1) — 实时交互虚拟人公司. Avaturn Live 开发实时交互虚拟人，发布了包含模型权重、渲染器和服务后端的开源方案 AVTR-1。 https://avaturn.live
- **Axon** (1) — 公共安全科技公司（TASER 电击器、执法记录仪）. TASER 电击武器与警用执法记录仪的制造商，也为警员提供 VR 训练。 https://www.axon.com/products/vr
- **Bangbang Yang** (1) — 字节跳动 PICO 混合现实团队研究者. 研究面向 XR 的神经渲染与场景编辑。 https://ybbbbt.com/
- **Barbara Olasov Rothbaum** (1) — 埃默里大学精神病学教授. 临床心理学家，她 1995 年的试验是最早的虚拟现实暴露疗法对照研究之一。
- **Beijing Academy of Artificial Intelligence (BAAI)** (1) — 非营利人工智能研究机构. 位于北京的非营利研究机构；其智能体团队发布了 Cradle，一个在商业游戏与软件中测试的通用计算机控制框架。 https://www.baai.ac.cn/
- **Ben Mildenhall** (1) — 研究者，World Labs 联合创始人. NeRF（2020）第一作者，后在 Google Research 工作，现为 World Labs 联合创始人。
- **Ben Poole** (1) — 谷歌研究科学家. 谷歌研究员，DreamFusion 第一作者，该论文提出了用于文生三维的分数蒸馏采样（SDS）。
- **Biao Jiang** (1) — 复旦大学研究者. 复旦大学研究者，与腾讯合作的 MotionGPT（NeurIPS 2023）第一作者。
- **Binbin Huang** (1) — 上海科技大学研究者. 2D 高斯泼溅（SIGGRAPH 2024）第一作者。
- **Blockade Labs** (1) — Skybox AI 的开发者. 开发 Skybox AI 的初创公司：一个生成 360° 等距柱状天空盒与环境的网页工具和 API。 https://www.blockadelabs.com
- **Bodyswaps** (1) — 软技能培训公司. 为学生和员工打造在 VR 与浏览器中进行的 AI 化身角色扮演，并提供自动反馈。 https://bodyswaps.co/
- **Boyuan Chen** (1) — 麻省理工学院研究者，Diffusion Forcing 第一作者. 麻省理工学院的博士研究者，研究视频世界模型与机器人学习。 https://boyuan.space
- **CAMEL-AI** (1) — 开源多智能体研究社区. CAMEL 多智能体框架与 OASIS 背后的开源社区；OASIS 是可容纳一百万个 LLM 智能体的社交媒体模拟器。 https://www.camel-ai.org/
- **Chaoyue Song** (1) — 南洋理工大学博士研究者. 南洋理工大学研究者，与字节跳动 Seed 合作的 Puppeteer（NeurIPS 2025 亮点论文）和 MagicArticulate 第一作者。 https://chaoyuesong.github.io/
- **Chen Tessler** (1) — 英伟达研究科学家. 英伟达研究科学家，研究基于物理的角色控制；MaskedMimic（SIGGRAPH Asia 2024）第一作者，并维护 ProtoMotions。
- **Claire Nee** (1) — 朴次茅斯大学司法心理学教授. 研究入室盗窃者的专业技能与决策，共同领导虚拟入室盗窃项目。
- **Connor Powelson** (1) — 刑事司法研究者. 2025 年一项关于警察在精神健康协同出警中如何决策的 VR 出声思维研究的第一作者。
- **Cyrus Vachha** (1) — 加州大学伯克利分校电子工程与计算机系研究者. 研究沉浸式三维创作与辐射场（NeRF、高斯泼溅），与 Björn Hartmann 合作。
- **D-ID** (1) — 数字人与可视化 AI 智能体公司. D-ID 能让照片中的人脸动起来，并提供实时的可视化 AI 智能体；2026 年推出面向交互与脚本场景的 V4 Expressive 虚拟人。 https://www.d-id.com
- **Daily** (1) — WebRTC 音视频基础设施公司. 提供实时视频 API，维护开源智能体框架 Pipecat 与 Pipecat Cloud。 https://www.daily.co
- **Dan Pollak** (1) — 赖克曼大学先进现实实验室研究员. Inceptor 的第一作者，该流程可为心理健康训练生成社会 VR 片段。
- **Daniel Duckworth** (1) — Google DeepMind 研究工程师. Google 研究者，SMERF 第一作者，这是一种可在浏览器中流式加载大场景的辐射场。
- **Danijar Hafner** (1) — 研究科学家，Dreamer 系列智能体作者. Google DeepMind 研究科学家，以 Dreamer 系列世界模型智能体闻名。 https://danijar.com
- **Danlin Huang** (1) — 设计研究者，中国美术学院创新设计学院. 与 Reality Design Lab 合作创作以身体为中心的思辨混合现实作品，如 Body Oracle 与 FungiSync。
- **David Charatan** (1) — 麻省理工学院博士研究者. 麻省理工学院研究者，pixelSplat（CVPR 2024）第一作者。
- **David DeVault** (1) — 南加州大学创意技术研究所自然语言对话研究者. 主持 SimSensei Kiosk 虚拟人访谈者项目。
- **David Ha** (1) — 研究者，《World Models》（2018）第一作者. 机器学习研究者，时任职于 Google Brain，后联合创立 Sakana AI；与 Jürgen Schmidhuber 合著《World Models》。 https://worldmodels.github.io
- **David-Paul Pertaub** (1) — 伦敦大学学院研究者（2002 年）. 2002 年与 Mel Slater、Chris Barker 合作的虚拟听众演讲实验的第一作者。
- **DeepMotion** (1) — AI 动作捕捉与动画公司. 以基于视频的无标记动作捕捉（Animate 3D）和文生三维动画工具 SayMotion 著称。 https://www.deepmotion.com/
- **Dehui Kong** (1) — 卡尔斯鲁厄理工学院研究员. CoEmpaTeam（CHI 2026）的第一作者，这是一个用大语言模型化身训练认知共情的 VR 系统。
- **Denis Rozumny** (1) — Meta 研究者. Meta 研究者，BulletGen 第一作者。
- **Dian Zheng** (1) — 上海人工智能实验室、中山大学研究者. VBench-2.0 的第一作者，该基准检验生成视频在物理与常识上的可信度。
- **Domna Banakou** (1) — 虚拟具身研究者（巴塞罗那大学 EventLab）. 研究虚拟身体与场景的渐进变化如何改变知觉、态度与焦虑。
- **Dylan Ebert** (1) — Hugging Face 机器学习工程师. 在 Hugging Face 从事三维机器学习，3D Arena 的创建者。
- **Dynamics Lab** (1) — 生成式游戏引擎初创公司. 推出 Mirage（2025 年 7 月）与 Mirage 2（2025 年 8 月）这两款可在浏览器中游玩的生成式世界引擎的初创公司；2026 年 10 月核查时，其网站与发布帖均已下线。
- **Egon Brunswik** (1) — 心理学家，加州大学伯克利分校（1903–1955）. 出生于匈牙利的心理学家，提出概率功能主义与“透镜模型”，主张实验应像抽样被试一样认真地抽样情境。
- **Eloi Alonso** (1) — 研究者，DIAMOND 第一作者. 日内瓦大学的机器学习研究者，研究用于强化学习的扩散世界模型。
- **Erzhen Hu** (1) — 弗吉尼亚大学计算机系博士研究者. 研究 XR 通信，与 Google XR 合作者完成 Thing2Reality 的第一作者。
- **Etched** (1) — AI 芯片公司. 设计 Transformer 专用推理芯片 Sohu 的初创公司，与 Decart 合作开发了 Oasis。 https://www.etched.com
- **Fernanda De La Torre** (1) — 麻省理工学院脑与认知科学系研究者；与微软合作的 LLMR 第一作者. 主导 LLMR：微软用语言模型创建与修改交互式混合现实世界的框架。
- **Fernanda Herrera** (1) — 斯坦福虚拟人交互实验室研究员. 主导了比较 VR 与传统换位思考的大规模《Becoming Homeless》研究。
- **Figmin XR** (1) — 混合现实创作应用 Figmin XR 背后的独立团队. 开发 Figmin XR：一款跨平台（Quest、Vision Pro、HoloLens）的应用，用于搭建和分享混合现实场景、玩具与可编程物体。 https://figmin.com
- **Gale Lucas** (1) — 南加州大学创意技术研究所研究员. 社会心理学家，发现人们在相信虚拟人由计算机控制时会披露更多。
- **General Intuition** (1) — 研究在时空中行动的智能体的 AI 实验室. 从游戏片段平台 Medal 分拆出来的 AI 实验室，利用大规模游戏视频档案训练智能体与世界模型。 https://generalintuition.com
- **Genmo** (1) — 开源视频模型初创公司. 发布了 100 亿参数、Apache 2.0 许可的开源文生视频模型 Mochi 1。 https://www.genmo.ai
- **Gracia** (1) — 体积高斯视频公司. 将 4D 高斯泼溅视频流式传输到 Quest、Pico、Apple Vision Pro、桌面与浏览器的公司，2026 年起把重点表述为面向物理 AI 的世界重建模型。 https://gracia.ai/
- **Guanjun Wu** (1) — 华中科技大学研究者. 《4D Gaussian Splatting for Real-Time Dynamic Scene Rendering》（CVPR 2024）第一作者。
- **Guanzhi Wang** (1) — 人工智能研究者（加州理工学院、英伟达）. 加州理工学院博士研究者，与英伟达合作；Voyager（2023）的第一作者，该智能体通过编写并保存代码技能来探索 Minecraft。
- **Guibao Shen** (1) — 立体转换研究者. 香港科技大学（广州）研究者，StereoPilot 第一作者，该工作在快手可灵团队实习期间完成。
- **Guido Makransky** (1) — 哥本哈根大学教育心理学教授. 研究沉浸式 VR 中的学习，合作提出 CAMIL 模型，解释临场感与能动性何时促进、何时妨碍学习。
- **Gustav Bøg Petersen** (1) — 与斯坦福虚拟人交互实验室合作的研究者. 研究 VR 中的学习与环境态度，OceanSpeak 对话式 AI 研究的第一作者。
- **Guy Tevet** (1) — 特拉维夫大学研究者. 特拉维夫大学研究者（与 Amit Bermano、Daniel Cohen-Or 合作），人体动作扩散模型 MDM（ICLR 2023）第一作者。 https://guytevet.github.io/
- **Habin Lim** (1) — 高丽大学研究者. Habin Lim 是 FacePlex（2026）的共同第一作者。该模型来自高丽大学与 Klleon，可全双工地生成语音与面部动作，并用高斯泼溅渲染。 https://hahminlew.github.io/faceplex
- **Hal Hershfield** (1) — 加州大学洛杉矶分校安德森管理学院市场营销与行为决策教授. 研究“未来自我”心理学；与斯坦福 VHIL 合作发现，见到自己变老的化身会增加储蓄。
- **Hanwen Liang** (1) — 多伦多大学研究者. 多伦多大学的博士研究者，与 Snap Research 合作完成 Wonderland 并任第一作者。
- **Hanxue Liang** (1) — 剑桥大学 / NVIDIA 研究者. NVIDIA 前馈式子弹时间重建模型 BTimer 的第一作者。
- **Haotong Lin** (1) — 字节跳动 Seed / 浙江大学研究者. Depth Anything 3 第一作者。
- **Haoyi Duan** (1) — 斯坦福大学研究者. 与吴佳俊、李飞飞合作，WorldScore 的第一作者。 https://haoyi-duan.github.io
- **Haoyu Wang** (1) — 伦敦帝国理工学院戴森设计工程学院研究者. 研究混合现实中的触觉与生成式 AI，与多伦多大学 Dynamic Graphics Project 合作者共同完成 Prop-Chromeleon。
- **Haozhe Xie** (1) — 南洋理工大学 S-Lab 研究者. 南洋理工大学刘子纬 S-Lab 的研究者，CityDreamer 与 CityDreamer4D 的第一作者。 https://www.infinitescript.com
- **Hedra** (1) — 生成式角色视频公司. Hedra 开发音频驱动的角色视频模型（Character-3）和制作会说话角色的工作室。 https://www.hedra.com
- **Heng Yu** (1) — 卡内基梅隆大学博士研究者. 4Real（NeurIPS 2024）第一作者，与 Snap Research 合作完成。
- **HeyGen** (1) — AI 视频虚拟人平台. HeyGen 提供 AI 虚拟人视频制作，并通过 LiveAvatar 提供实时虚拟人流式 API。 https://www.heygen.com
- **Ho Kei Cheng** (1) — 计算机视觉研究者（伊利诺伊大学厄巴纳-香槟分校）. Ho Kei（Rex）Cheng 以视频目标分割（XMem、Cutie）以及与 Sony AI 合作开发的 MMAudio 视频配音模型而知名。 https://hkchengrex.com
- **Huadai Liu** (1) — 音频生成研究者（浙江大学）. Huadai Liu 在浙江大学研究文本、视频与空间音频的生成。
- **Hugues Bruyère** (1) — Dpt.（蒙特利尔）合伙人与创新负责人. 创意技术专家，用实时生成模型制作交互装置与混合现实体验原型。
- **Hunter Hoffman** (1) — 华盛顿大学研究科学家. 与 David Patterson 合作开发 SnowWorld，在烧伤换药时分散患者对疼痛的注意。
- **Jacob Barker** (1) — VORTeX（2026）第一作者. 开发用于训练和评估外科团队协作的“虚拟手术室团队体验”（VORTeX）。
- **Jaewook Lee** (1) — 华盛顿大学 Makeability Lab 博士研究者. 研究 AI 驱动的增强现实，与 Niantic Spatial 合作主导 ImaginateAR。
- **Jaeyeon Kim** (1) — 视听学习研究者（首尔大学）. Jaeyeon Kim 在首尔大学视觉与学习实验室研究视听生成。 https://jaeyeonkim99.github.io/visage/
- **Jaeyoung Chung** (1) — 首尔国立大学计算机视觉实验室研究者. 首尔国立大学 Kyoung Mu Lee 实验室的研究者，LucidDreamer 的共同第一作者。
- **Jawset** (1) — Postshot 开发商. 开发 Postshot 的小型软件公司，Postshot 是在本地 GPU 上训练和编辑辐射场与高斯泼溅的桌面应用。 https://www.jawset.com/
- **Jia-Peng Zhang** (1) — 清华大学研究者. 清华大学研究者，与 VAST 合作的 UniRig（SIGGRAPH 2025）第一作者。 https://zjp-shadow.github.io/
- **Jianhong Bai** (1) — 镜头可控视频研究者. 浙江大学研究者，与快手可灵团队合作完成 ReCamMaster。 https://jianhongbai.github.io/
- **Jiaxiang Tang** (1) — 北京大学博士研究者. 北京大学研究者，DreamGaussian（ICLR 2024 口头报告）第一作者，是较早把三维高斯泼溅用于生成的工作。 https://me.kiui.moe/
- **Jim Blascovich** (1) — 社会心理学家，加州大学圣塔芭芭拉分校. 共同创办加州大学圣塔芭芭拉分校的虚拟环境与行为研究中心，倡导把沉浸式 VR 作为社会心理学的研究方法。
- **Jing Tan** (1) — 沉浸式视频生成研究者. 香港中文大学研究者，Imagine360 第一作者。
- **Jonathan Steuer** (1) — 传播学研究者（1992 年时在斯坦福大学）. 1992 年发表论文，以“远程临场”体验及其两个决定因素——生动性与交互性——来定义虚拟现实。
- **Jonathan Tseng** (1) — 斯坦福大学研究者. 斯坦福大学研究者（与 C. Karen Liu 合作），由音乐生成可编辑舞蹈的 EDGE（CVPR 2023）第一作者。 https://edge-dance.github.io/
- **Junyi Zhang** (1) — 加州大学伯克利分校博士研究者. MonST3R（ICLR 2025）第一作者。
- **K R Prajwal** (1) — 唇形同步与语音驱动视频研究者. K R Prajwal 当时在印度海得拉巴国际信息技术学院（IIIT Hyderabad），是 Wav2Lip（ACM Multimedia 2020）的第一作者。
- **K. Anders Ericsson** (1) — 心理学家，佛罗里达州立大学（1947–2020）. 瑞典心理学家，开创了专家表现研究，并界定了“刻意练习”的概念。
- **Kaifeng Zhao** (1) — 苏黎世联邦理工学院博士研究者. 苏黎世联邦理工学院研究者（与 Siyu Tang 合作），在英伟达完成的 ARDY（SIGGRAPH 2026）第一作者。 https://research.nvidia.com/labs/sil/projects/ardy/
- **Kaixin Yao** (1) — 上海科技大学与影眸科技研究者. CAST（SIGGRAPH 2025 最佳论文）的第一作者，该工作由上海科技大学与影眸科技完成。
- **Kamilla Bergsnev** (1) — 2026 年一篇关于 AI 用于 VR 暴露疗法的系统综述的第一作者. 系统梳理了人工智能如何被用来定制 VR 暴露疗法的研究者。
- **Konstantin W. Kühlem** (1) — 亚琛工业大学视觉计算研究所研究员. VR 中具身对话智能体低延迟大语言模型对话系统（IVA 2025）的第一作者。
- **Krea** (1) — 实时创意 AI 工具公司. 以实时图像生成著称的创意工具公司；2025 年 10 月发布开源的 Krea Realtime 14B 视频模型。 https://www.krea.ai
- **Kyle Johnsen** (1) — 计算机科学家（佛罗里达大学，后任职于佐治亚大学）. 与 Benjamin Lok 团队合作构建并验证了用于医学问诊训练的真人大小虚拟病人。
- **LemonSlice** (1) — 交互式虚拟人模型公司. LemonSlice 开发用于交互式虚拟人的实时视频扩散模型（2025 年的 LemonSlice-2、2026 年的 Character World Model-1），可从一张图像驱动任意角色。 https://lemonslice.com
- **Light in the Head** (1) — Marc Da Costa 与 Matthew Niederhauser 的工作室. 使用机器学习、VR 与装置创作的艺术家二人组，也是 Sensorium 的联合创始人。
- **Lihan Jiang** (1) — 中国科学技术大学 / 上海人工智能实验室研究者. AnySplat（SIGGRAPH Asia 2025）第一作者。
- **Lihe Yang** (1) — 香港大学研究者. 香港大学赵恒爽组的博士研究者，与字节跳动（TikTok）合作的 Depth Anything 与 Depth Anything V2 的第一作者。 https://liheyoung.github.io
- **Linyi Jin** (1) — 密歇根大学 / Google DeepMind 博士研究者. Stereo4D（CVPR 2025）第一作者，与 Google DeepMind 合作，利用互联网 VR180 视频构建。
- **Liquid City** (1) — 由 Keiichi Matsuda 创立的设计工作室. 由设计师、电影人 Keiichi Matsuda（Hyper-Reality、Merger）领导的工作室，设计 AR、AI 智能体与空间界面。 https://www.liquid.city
- **LiveKit** (1) — 实时音视频基础设施公司. 开发开源 WebRTC 媒体服务器、LiveKit Agents 框架与 LiveKit Cloud。 https://livekit.io
- **Longwen Zhang** (1) — 上海科技大学 / 影眸科技研究者. CLAY（SIGGRAPH 2024）第一作者，该原生三维生成模型后来成为 Rodin Gen-1。
- **Lu Ling** (1) — 普渡大学研究者. DL3DV-10K 的第一作者，这是一个面向三维视觉的大型真实场景视频数据集。 https://dl3dv-10k.github.io/DL3DV-10K/
- **Lukas Höllein** (1) — 慕尼黑工业大学研究者. 慕尼黑工业大学 Matthias Niessner 视觉计算与 AI 实验室的博士研究者，Text2Room 的第一作者。 https://lukashoel.github.io
- **Lvmin Zhang** (1) — 可控生成研究者. 斯坦福博士研究者，ControlNet、IC-Light 与 FramePack 的作者。
- **Mar Gonzalez-Franco** (1) — XR 研究科学家（Google；曾任职于微软研究院）. 从事化身、具身与社交 XR 研究的神经科学家与工程师，主导了米尔格拉姆范式的 VR 复现研究。
- **Martin de La Gorce** (1) — 微软研究者. 微软研究者，VoluMe（2025）第一作者。
- **Matt Deitke** (1) — AI 研究者（Objaverse、Objaverse-XL）. 在艾伦人工智能研究所主导了 Objaverse 与 Objaverse-XL 三维数据集。 https://mattdeitke.com
- **Matthew J. Smith** (1) — 社会工作研究者（西北大学，后任职于密歇根大学）. 以虚拟面试官 Molly Porter 为核心的虚拟现实求职面试训练试验的第一作者。
- **Mehdi Moussaïd** (1) — 马克斯·普朗克人类发展研究所研究科学家. 研究人群行为与集体动力学，包括让真实参与者在共享虚拟环境中进行人群疏散实验。
- **Meituan** (1) — 科技公司（MeiGen / LongCat 团队）. 美团的 MeiGen 团队发布了 MultiTalk 和 InfiniteTalk，这是用于音频驱动说话视频与配音的开源模型。 https://www.meituan.com
- **Meng-Li Shih** (1) — 研究者（弗吉尼亚理工，后至华盛顿大学）. 《3D Photography using Context-aware Layered Depth Inpainting》（CVPR 2020）的第一作者，合作者包括黄嘉斌与 Johannes Kopf。 https://shihmengli.github.io
- **Michael Wiesing** (1) — 巴塞罗那大学 EventLab 研究员. 研究 VR 体验如何延续到物理现实中的信念与行动。
- **Midjourney** (1) — 独立图像与视频生成实验室. 自筹资金的实验室，以审美导向的图像模型著称；2025 年 6 月发布首个视频模型。 https://www.midjourney.com
- **Moonvalley** (1) — 面向影视创作者的视频生成公司. 与工作室 Asteria 一同开发只用授权素材训练的视频模型 Marey。 https://www.moonvalley.com
- **Moreah Zisquit** (1) — 赖克曼大学研究员. 2025 年一项在 VR 自我对话咨询中加入 AI 智能体的形成性研究的第一作者。
- **Mursion** (1) — 沉浸式模拟训练公司. 源于“人在回路”教学模拟器的研究；由受过训练的模拟专员实时为化身配音并操控其行为，公司如今主打 AI 驱动的模拟。 https://www.mursion.com/
- **Naisha Agarwal** (1) — 加州大学洛杉矶分校研究者；微软研究院合作者. 与微软研究院的 Judith Amores、Andrew D. Wilson 合作主导 Storycaster。
- **Nels Numan** (1) — 伦敦大学学院博士研究者；微软研究院合作者. 研究协作式混合现实与远程临场，SpaceBlender 第一作者，也是 XR Blocks 的合作者。
- **NetEase Games** (1) — 电子游戏开发商与发行商. 中国游戏公司，旗下有《逆水寒》《蛋仔派对》《永劫无间》；2023 年在《逆水寒》手游中上线 LLM 驱动的 NPC，2025 年在《永劫无间》手游 PC 版中上线基于英伟达 ACE、本地运行的 AI 队友。 https://www.neteasegames.com/
- **Nick Yee** (1) — 化身与网络游戏研究者（斯坦福 VHIL；后联合创办 Quantic Foundry）. 在斯坦福读博期间与 Jeremy Bailenson 一起提出“普罗透斯效应”，之后大规模研究玩家动机。
- **Nicolas Moenne-Loccoz** (1) — NVIDIA 研究者. NVIDIA 研究者，3D Gaussian Ray Tracing（3DGRT）第一作者。
- **Nikhil Keetha** (1) — 卡内基梅隆大学 / Meta 博士研究者. MapAnything 第一作者，这是 Meta 与卡内基梅隆大学合作的公制三维重建模型。
- **Nozomu Iwai** (1) — Preferred Networks 研究者. Preferred Networks 研究者，与 Fabrice Matulic 合作完成 AR 会说话物件研究（CHI 2025 扩展摘要）的第一作者。
- **OpenBMB** (1) — 面壁智能与清华 NLP 实验室的开源模型社区. OpenBMB 是 MiniCPM 系列模型背后的开源项目，由面壁智能与清华大学自然语言处理实验室主导。 https://www.openbmb.cn
- **Overworld** (1) — 开源世界模型初创公司. 发布可在消费级显卡本地运行的开源实时扩散世界模型（Waypoint）及开源客户端 Biome 的初创公司。 https://over.world
- **Patrick Kenny** (1) — 南加州大学创意技术研究所研究员（2000 年代）. 在 USC ICT 主持虚拟人与虚拟病人项目，包括 2007 年 I/ITSEC 上关于构建训练用交互式虚拟人的综述。
- **Patrick McClanahan** (1) — 犯罪学研究者，宾夕法尼亚虚拟入室盗窃项目（马克斯·普朗克犯罪、安全与法律研究所）. 主导虚拟入室盗窃项目的宾夕法尼亚分支，把 VR 盗窃任务带进美国监狱，并以开放获取方式公开了虚拟街区。
- **Peiwen Sun** (1) — 空间音频生成研究者（香港科技大学）. Peiwen Sun 在香港科技大学研究语言驱动的音频生成。 https://peiwensun2000.github.io/bewo/
- **Pika** (1) — 面向大众的视频生成初创公司. 2023 年由斯坦福博士生创立，以 Pika 1.0 和趣味化编辑特效著称。 https://pika.art
- **Polycam** (1) — 三维捕捉应用公司. 一款覆盖 LiDAR、摄影测量与高斯泼溅的手机、网页与无人机三维捕捉应用的开发商。 https://poly.cam/
- **Preferred Networks** (1) — 日本人工智能公司. 总部位于东京的 AI 公司，开发深度学习模型与 AI 芯片，并开展包括 AR 与角色交互在内的应用研究。 https://www.preferred.jp/en/
- **Princeton Vision & Learning Lab** (1) — 普林斯顿大学邓嘉的计算机视觉实验室. 由邓嘉领导的高校实验室，开发了 Infinigen 程序化世界生成器。 https://pvl.cs.princeton.edu
- **Proxima** (1) — 独立游戏工作室. 《Suck Up!》背后的小型工作室；在这款喜剧游戏里，玩家要说服由 AI 驱动的镇民让吸血鬼进门。 https://www.playsuckup.com/
- **Qi Wu** (1) — NVIDIA 研究者. NVIDIA 研究者，3DGUT（CVPR 2025）第一作者。
- **Qian Wang** (1) — 全景视频生成研究者. 北京大学深圳研究生院研究者，360DVD 第一作者。
- **Ramon Oliva** (1) — 巴塞罗那大学 EventLab 研究员. 与 Mel Slater 团队开发 VR 系统并开展社交 VR 研究，包括 2026 年关于会议小组讨论中化身互换与大语言模型驱动的艾伦·图灵的研究。
- **Replicate** (1) — 模型托管平台（并入 Cloudflare）. 以带版本号的 HTTP 接口运行开源与闭源模型，Cog 容器格式的创建者。 https://replicate.com
- **Roberto Coviello** (1) — XR 与 AI 工程师；QuestCameraKit 作者. 维护 QuestCameraKit：基于 Meta Quest 透视摄像头 API 的开源示例集。 https://xrdevrob.com
- **Ruiqi Gao** (1) — Google DeepMind 研究科学家. Google DeepMind 的生成模型研究者，CAT3D 与 CAT4D 的共同第一作者。
- **Rundi Wu** (1) — 哥伦比亚大学 / Google DeepMind 博士研究者. CAT4D（CVPR 2025）第一作者，在 Google DeepMind 完成。
- **Ruofei Du** (1) — Google XR 交互感知与图形负责人. 研究面向 XR 的交互图形与 AI，主导 XR Blocks，参与 Thing2Reality 与 Sensible Agent。 https://duruofei.com
- **Ruoshi Liu** (1) — 哥伦比亚大学博士研究者. 哥伦比亚大学研究者（Carl Vondrick 实验室，与丰田研究院合作），Zero-1-to-3 第一作者。 https://ruoshiliu.github.io/
- **Ryutaro Kurai** (1) — Cluster 公司研究者（Cluster Metaverse Lab）. 日本社交 VR 平台 Cluster 的研究者，为平台用户开发基于大语言模型的创作工具。
- **SHOTPROS** (1) — 欧盟“地平线 2020”VR 警务训练研究项目（2019–2022）. 由警务机构、大学与企业组成的联合体，研究压力下的决策与行动，并构建了一套 VR 训练框架。 https://shotpros.eu/
- **Sand AI** (1) — 视频生成初创公司. 2025 年 4 月开源了 240 亿参数的自回归视频模型 MAGI-1。 https://sand.ai
- **Sesame** (1) — 语音 AI 与硬件公司. Sesame 由 Oculus 联合创始人 Brendan Iribe 参与创立，开发对话式语音智能体与对话语音模型 CSM，并已宣布眼镜产品。 https://www.sesame.com
- **Seung Wook Kim** (1) — 英伟达研究员，GameGAN 第一作者. 英伟达多伦多 AI 实验室研究员，研究游戏与驾驶的神经模拟。
- **Shenghai Yuan** (1) — 实时视频生成研究者. 北京大学研究者（袁粒课题组，与字节跳动合作），Helios 第一作者。
- **Shenhan Qian** (1) — 慕尼黑工业大学博士研究者. Shenhan Qian 在慕尼黑工业大学 Matthias Niessner 组，是 GaussianAvatars（CVPR 2024）的第一作者。 https://shenhanqian.github.io
- **Sherry Yang** (1) — 研究者，UniSim 第一作者. 研究者（发表 UniSim 时任职于 Google DeepMind 与加州大学伯克利分校），研究把视频模型用作真实世界模拟器。
- **Shijie Zhou** (1) — 加州大学洛杉矶分校研究者. 加州大学洛杉矶分校 Achuta Kadambi 实验室的博士研究者，DreamScene360 的第一作者。
- **Shitao Tang** (1) — 西蒙菲莎大学研究者. 西蒙菲莎大学 Yasutaka Furukawa 组的博士研究者，MVDiffusion 的第一作者。
- **Shuai Yang** (1) — 长视频生成研究者. 就职于 NVIDIA 与香港科技大学（广州）的研究者，LongLive 第一作者。
- **Shuai Yang** (1) — 上海交通大学与上海人工智能实验室研究者. LayerPano3D（SIGGRAPH 2025）的第一作者，合作者来自香港中文大学、斯坦福与南洋理工。
- **Shunsuke Saito** (1) — Meta Codec Avatars 实验室研究科学家. Shunsuke Saito 在 Meta 主导高斯 Codec Avatars 研究，包括可重光照高斯 Codec Avatars（CVPR 2024）和大规模 Codec Avatars（CVPR 2026）。 https://shunsukesaito.github.io
- **Shuzhe Wang** (1) — 阿尔托大学 / NAVER LABS Europe 研究者. DUSt3R（CVPR 2024）第一作者，该工作在 NAVER LABS Europe 完成。
- **Siddharth Ahuja** (1) — BlenderMCP 开发者. 独立开发者，发布了开源的 BlenderMCP：连接语言模型与 Blender 的 Model Context Protocol 桥接工具。
- **Sijie Zhao** (1) — 立体视频生成研究者. 腾讯研究者，StereoCrafter 共同第一作者。
- **Simile** (1) — 人类行为模拟公司. 由 Joon Sung Park、Michael Bernstein 与 Percy Liang 创办，把生成式智能体研究做成对客户与人群的模拟。2026 年 2 月公开亮相。 https://www.simile.com/
- **Sofia Adelaide Osimo** (1) — 虚拟具身研究者（巴塞罗那大学 EventLab）. 2015 年“自我咨询”研究的第一作者：参与者在自己的身体与西格蒙德·弗洛伊德的身体之间切换。
- **Sofia Seinfeld** (1) — 虚拟具身研究者（巴塞罗那大学 EventLab）. 让家暴罪犯“进入”受害者身体的那项研究的第一作者。
- **Solène Neyret** (1) — 巴塞罗那大学 EventLab 研究员. 研究 VR 中的具身换位思考如何改变从众行为与群体中的伤害行为。
- **Soul AI Lab** (1) — 社交应用 Soul 的 AI 实验室. Soul AI Lab 是社交平台 Soul 的研究部门，开源了 14B 实时流式虚拟人模型 SoulX-FlashTalk。
- **Stanislaw Szymanowicz** (1) — 牛津大学视觉几何组研究者. 牛津大学视觉几何组的博士研究者（Splatter Image、Flash3D），与 Google 合作完成 Bolt3D 并任第一作者。 https://szymanowiczs.github.io
- **Stanley J. Hamstra** (1) — 医学教育研究者（渥太华大学；美国毕业后医学教育认证委员会）. 研究基于模拟的训练，2014 年重新审视模拟“保真度”一文的第一作者。
- **Strivr** (1) — 沉浸式培训公司. 2015 年从斯坦福 VHIL 衍生，先用 360° VR 训练运动员，后把 VR 培训推广到沃尔玛等企业；截至 2026 年主推基于智能眼镜的 AI 质检。 https://www.strivr.com/
- **Suibi Che-Chuan Weng** (1) — 科罗拉多大学博尔德分校 ATLAS 研究所人机交互研究者. 研究创意混合现实与生成式 AI，Editing Reality（DIS 2026）第一作者。
- **Suno** (1) — AI 音乐公司. Suno 打造了被广泛使用的歌曲生成器，能根据提示写出并演唱完整歌曲。 https://suno.com
- **Sylvia Xueni Pan** (1) — 伦敦大学金史密斯学院虚拟社会互动研究者. 研究人与虚拟角色的社会互动，与 Antonia Hamilton 合写了用 VR 研究社会互动的经典综述。
- **Synthesia** (1) — 企业级 AI 视频与虚拟人平台. Synthesia 为企业培训和内部沟通制作 AI 虚拟人视频，2026 年加入实时交互虚拟人和用于角色扮演与访谈的 Sessions 平台。 https://www.synthesia.io
- **Tabitha Peck** (1) — 戴维森学院计算机科学家. 研究虚拟具身与化身效应，2013 年与 Mel Slater 团队合作的“黑人化身与内隐偏见”研究的第一作者。
- **Taekyung Ki** (1) — 韩国科学技术院（KAIST）博士研究者. Taekyung Ki 是 Avatar Forcing（CVPR 2026）的第一作者，该模型是能对用户声音与动作作出反应的实时交互头部虚拟人。 https://taekyungki.github.io
- **Talespin** (1) — 沉浸式软技能培训公司，现已并入 Cornerstone. 开发带虚拟人的 VR 软技能模拟和无代码创作工具 CoPilot Designer；talespin.com 现已跳转至 Cornerstone 的沉浸式学习平台。 https://www.cornerstoneondemand.com/platform/immersive-learning/
- **Tencent** (1) — 中国科技与游戏公司. 总部位于深圳的互联网与游戏公司；除混元外，其多个研究团队也发表交互式视频方面的工作。 https://www.tencent.com
- **Tencent ARC Lab** (1) — 腾讯 PCG 应用研究中心. 腾讯从事视觉生成与编辑研究的实验室，成果包括 StereoCrafter 与 Rolling Forcing。 https://arc.tencent.com
- **The Khronos Group** (1) — 图形与空间计算标准联盟. 制定 glTF、OpenXR、Vulkan 与 WebGL 的开放行业联盟。 https://www.khronos.org
- **Thomas Müller** (1) — NVIDIA 研究者. NVIDIA 研究者，Instant Neural Graphics Primitives（instant-ngp）第一作者。
- **Tianwei Yin** (1) — 快速生成模型研究者. MIT 博士研究者，DMD 蒸馏与 CausVid 的第一作者。
- **Tianye Li** (1) — Meta Reality Labs 研究者. Neural 3D Video Synthesis（DyNeRF，CVPR 2022）第一作者，该工作在 Meta Reality Labs Research 完成。
- **Tianyi Xiao** (1) — 苏黎世联邦理工学院制图与地理信息研究所研究者. 研究空间认知、草图地图与增强现实。
- **Tinghui Zhou** (1) — 计算机视觉研究者（加州大学伯克利分校博士）. Stereo Magnification（SIGGRAPH 2018）的第一作者，该论文提出了多平面图像表示与 RealEstate10K 数据集。 https://tinghuiz.github.io
- **Tom Craig** (1) — 伦敦国王学院社会精神病学教授. 主持 AVATAR 疗法试验：幻听者与由治疗师配音、代表其“迫害者”的化身对话。
- **Tomoki Itamiya** (1) — 爱知工科大学教授. 开发 AR 与 VR 防灾教育工具，例如叠加在真实房间与街道上的洪水和地震模拟。
- **Tong Wu** (1) — 斯坦福大学研究者. 斯坦福大学 Gordon Wetzstein 组的研究者，研究具备三维感知的视频生成。
- **Transitional Forms** (1) — 由 Pietro Gagliano 创立的 AI 娱乐工作室. 围绕实时 AI 智能体创作故事与游戏的工作室，作品从与加拿大国家电影局合作的动态电影 Agence，到多智能体故事模拟。 https://www.transforms.ai
- **Tsinghua University FIB Lab** (1) — 清华大学电子工程系研究实验室. 由李勇领导的实验室，研究城市科学与大语言模型智能体；2025 年发布 AgentSociety 模拟器。
- **Tu Anh Nguyen** (1) — 语音研究者（Meta AI / ENS–Inria）. Tu Anh Nguyen 在 Meta AI 与巴黎认知机器学习团队从事无文本口语语言建模研究。
- **Unity** (1) — 游戏引擎公司. Unity 引擎的开发者，大量 XR 与移动游戏以及许多 VR 研究实验室都在用它。 https://unity.com
- **Uriel Singer** (1) — Meta AI 研究科学家. Meta 研究者，Make-A-Video 与 MAV3D（文本到 4D，2023）的第一作者。
- **Valve** (1) — 游戏公司、Steam 运营方. 运营 Steam，生产 Index、Steam Deck 与 Steam Frame 头显。 https://store.steampowered.com
- **Varjo** (1) — XR 头显与重建公司. 芬兰高分辨率 XR 头显厂商，推出了 Teleport 云服务，把手机或相机素材转换为高斯泼溅场景。 https://varjo.com/
- **Vincent Leroy** (1) — NAVER LABS Europe 研究者. NAVER LABS Europe 研究者，MASt3R（ECCV 2024）第一作者。
- **Volcano Engine (BytePlus)** (1) — 字节跳动旗下云平台. 字节跳动的云服务与模型即服务业务，海外品牌为 BytePlus。 https://www.volcengine.com
- **W3C Immersive Web Working Group** (1) — 网页标准组织. 万维网联盟（W3C）中负责制定 WebXR 设备 API 及其模块的工作组。 https://www.w3.org/immersive-web/
- **Waymo** (1) — Alphabet 旗下的自动驾驶公司. Alphabet 旗下的自动驾驶公司，在多座美国城市运营无人驾驶网约车。 https://waymo.com
- **Weixi Feng** (1) — 加州大学圣巴巴拉分校研究者. 加州大学圣巴巴拉分校王威廉组的博士研究者，LayoutGPT 的第一作者。 https://weixi-feng.github.io
- **XREAL** (1) — AR 眼镜公司. 中国显示眼镜厂商（原名 Nreal），与 Google 合作开发 Android XR 眼镜 XREAL AURA。 https://www.xreal.com
- **Xindi Wu** (1) — 普林斯顿大学与英伟达研究者. 普林斯顿大学博士研究者，与英伟达合作研究视频世界模型的记忆机制。
- **Xinyang Li** (1) — 厦门大学 MAC 实验室博士研究者. FlashWorld 的第一作者，该工作与腾讯混元合作完成。
- **Xinyu Ning** (1) — 生成式 AI 与 XR 系统综述的第一作者（Lik-Hang Lee 团队）. 梳理了 2023–2025 年生成式 AI 与扩展现实结合研究的研究者。
- **Xuanchi Ren** (1) — NVIDIA 研究科学家. NVIDIA 多伦多 AI 实验室研究者，GEN3C 的第一作者，Lyra 的合作者。 https://xuanchiren.com
- **Xudong Xu** (1) — 视听学习研究者. Xudong Xu 研究视听学习与三维感知生成；Sounding Bodies 与 Meta Reality Labs Research 合作完成。
- **Xueyang Wang** (1) — 清华大学研究者. 研究跨现实创作与空间锚定的生成，Roomify（CHI 2026）第一作者。
- **Xun Huang** (1) — 生成式视频研究者. 研究科学家（Self Forcing 发表时任职于 Adobe Research），以 AdaIN 风格迁移和实时视频扩散研究著称。
- **Yicong Hong** (1) — Adobe 研究院研究科学家. Adobe 研究院研究员，《LRM：用于单张图像三维重建的大型重建模型》（ICLR 2024）第一作者。
- **Yifan Wang** (1) — 浙江大学研究者. 浙江大学三维视觉组研究者，FreeTimeGS（CVPR 2025）第一作者。
- **Yue Yang** (1) — 宾夕法尼亚大学研究者. 宾夕法尼亚大学的博士研究者，与艾伦人工智能研究所合作主导了 Holodeck。 https://yueyang1996.github.io
- **Zehao Yu** (1) — 图宾根大学研究者. Andreas Geiger 团队的博士研究者，Mip-Splatting 第一作者。
- **Zeqi Xiao** (1) — 研究者，WorldMem 第一作者. 南洋理工大学 S-Lab 研究者，研究一致的视频世界模拟。 https://xizaoqu.github.io
- **Zhan Li** (1) — 波特兰州立大学 / OPPO 美国研究院研究者. Spacetime Gaussian Feature Splatting（CVPR 2024）第一作者。
- **Zhan Xu** (1) — 研究者（马萨诸塞大学阿默斯特分校，后加入 Adobe）. RigNet（SIGGRAPH 2020）第一作者，该工作完成于马萨诸塞大学阿默斯特分校 Evangelos Kalogerakis 团队。 https://zhan-xu.github.io/
- **Zhen Xu** (1) — 浙江大学研究者. 浙江大学三维视觉组研究者，EasyVolcap 的作者，《Representing Long Volumetric Video with Temporal Gaussian Hierarchy》（SIGGRAPH Asia 2024）第一作者。
- **Zhengqi Li** (1) — Google DeepMind 研究科学家. 研究动态场景重建的 Google 研究者，MegaSaM（CVPR 2025）第一作者。
- **Zhipu AI** (1) — 源自清华大学的大模型公司. GLM 语言模型及开源 CogVideoX 视频模型（“清影”产品底座）的开发者。 https://www.zhipuai.cn
- **Zhiyang Guo** (1) — 中国科学技术大学博士研究者. Make-It-Animatable（CVPR 2025）第一作者，可在一秒内为人形网格和高斯泼溅完成绑定。 https://jasongzy.github.io/
- **Zhuangze Hou** (1) — 香港城市大学创意媒体学院研究者. 研究虚拟现实中由 AI 辅助的空间设计，EchoLadder（UIST 2025）第一作者。
- **Ziming Li** (1) — 罗切斯特理工学院研究员. Roshan Peiris 实验室中面向自闭症人士的大语言模型 VR 职场沟通训练研究（CHI EA 2024）的第一作者。
- **Ziyi Wu** (1) — 生成式三维与视频研究者. 多伦多大学博士研究者；360Anything 第一作者，该工作在 Google DeepMind 完成。
- **bilibili** (1) — 中国视频平台（Index 团队）. 哔哩哔哩是中国视频社区，其 Index 团队开发开源的 IndexTTS 语音模型。 https://www.bilibili.com
- **fal** (1) — 生成式媒体推理平台. 通过一个 API 托管 1,000 多个图像、视频、音频与三维模型，并提供 Serverless GPU。 https://fal.ai
