# Generative Reality Inspire — 目录

生成式沉浸技术目录：可以用来生成并进入情境的模型、产品、API、研究演示、研究与设备。领域包括：视频生成、交互式虚拟人、语音与空间音频、交互式世界模型、三维场景与世界生成、三维资产与动作、捕捉/重建与 4D、智能体与模拟社会、生成式扩展现实体验、沉浸式行为研究与训练，以及平台/API/交付。每个条目都列出核心想法、实现方式、输入、输出、时序（预先生成、回合制、实时、全双工、脚本驱动）与获取方式（开源权重、API、产品、候补、仅研究），并附视频、论文和官方页面链接。由 Reality Design Lab 整理，是一项面向行为科学的生成式沉浸研究议程背后持续更新的综述。技术能力以开发者公布为准。

https://generative.reality.design · 2026-10-18 · 534 个机构与创作者 · 799 个条目

## AI 助手应如何使用这个文件

- 提出想法时，以下面的具体条目为依据，并说明借鉴的是哪个条目、哪位创作者。
- 引用论文时使用这里给出的 DOI、arXiv 或链接，不要编造参考文献。
- 组合不同条目的输入、输出、时序与获取方式，提出系统与研究方案。
- 技术能力以开发者公布为准，请查看官方页面；不要编造这里没有写到的细节。

## 视频生成

根据文字、图像和参考素材合成视听事件的模型。这是制作情境素材最快的路径，但视频只能观看，不能在其中行动。

### 前沿文生 / 图生视频

闭源旗舰模型（Sora、Veo、可灵、Runway、Luma、海螺、Seedance……），许多已能同时生成声音。

#### Vidu Q4 Preview — 生数科技（Vidu） (2026-10-07)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 候补 / 抢先体验, 产品 / 应用
- 输入: 文字提示, 图像, 语音与音频 → 输出: 平面视频, 语音 / 声音, 音效、音乐与空间音频
- 核心想法: 除了参考图像还有参考音频：情境中的角色可以在多个生成镜头里保持同一张脸和同一种声音。
- 内容: Vidu Q4 Preview（2026-10-07）是生数科技下一代旗舰音视频模型的公开预览版，重点在角色表演：面部表情、肢体动作与声音一同生成，可用最多 15 张参考图和 3 段参考音频来约束，输出 2K 或 4K、10 bit 色深。
- 实现方式: 以多张参考图与多段参考音频为条件的音视频联合生成（架构未公开）。
- 参数: 2K / 4K · 10-bit · up to 15 image + 3 audio references · from $0.014/s (launch price)
- 能力维度: 行为似真性, 感知真实感, 实验控制
- 视频: https://www.youtube.com/watch?v=jJcbxCDRRaw
- 图片: https://mmx.prnewswire.com/media/MS2004200/20261007094159EDT_image_1.jpg?id=OA2992270&p=facebook
- 项目主页: https://www.prnewswire.com/news-releases/vidu-launches-q4-preview-making-flagship-ai-video-creation-accessible-to-everyone-302901266.html
- API 文档: https://platform.vidu.com/

#### 可灵 4.0（Kling 4.0） — 快手 / 可灵 (2026-09-28)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 产品 / 应用
- 输入: 文字提示, 图像, 视频 → 输出: 平面视频, 语音 / 声音, 音效、音乐与空间音频
- 核心想法: 30 秒的长镜头可以在一个连续镜头里容纳一段完整的短互动（接近、交流、反应）。
- 内容: 可灵 4.0 于 2026-09-28 推出（可灵 4.0 Flash 先向部分用户开放），单次生成延长到 30 秒，支持最多 10 个关键帧、1080p 与 4K 下的 10 bit HDR 以及双声道立体声；可灵于 2026-10-16 宣布其已在 kling.ai 全面开放。截至 2026-10-17，尚未公布可灵 4.0 的 API 模型。
- 实现方式: 可灵新一代模型；据报道每段最多可用 10 张关键帧图像并输出最高 4K；架构未公开。
- 参数: 3–30 s per generation · up to 10 keyframes · 720p / 1080p / 4K · 10-bit HDR · stereo audio
- 能力维度: 持久性, 实验控制, 感知真实感
- 视频: https://www.youtube.com/watch?v=nlM7kL3kv_Y
- 项目主页: https://kling.ai/blog/kling-4-vs-3

#### 通义万相 3.0（Wan 3.0） — 阿里通义 (2026-08-06)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 公开 API
- 输入: 文字提示, 图像, 视频 → 输出: 平面视频, 语音 / 声音, 音效、音乐与空间音频
- 核心想法: 就连最重要的开源视频团队也开始把最新旗舰闭源，开源的 Wan 模型因此落后一代。
- 内容: 通义万相 Wan 3.0 于 2026-08-06 在阿里云开启公测，8 月下旬已在百炼正式提供，并自 2026-08-20 起提供更快的 wan3.0-video-prime 版本；与开源的 Wan 2.1、2.2 不同，它闭源、仅提供 API，可在一个提示中同时接收文本、图像、视频和音频。此前 Wan 2.5（2025 年 9 月）和 Wan 2.6（2025 年 12 月）已加入原生音频与参考角色功能。
- 实现方式: 通过阿里云百炼提供服务的多模态音视频生成模型；截至 2026 年 10 月，架构与权重均未公开。
- 参数: up to 30 s · 1080p (reported)
- 能力维度: 持久性, 创作可及性, 实验控制
- 视频: https://www.youtube.com/watch?v=dC5pu8zL2p8
- 图片: https://img.alicdn.com/imgextra/i1/O1CN01WlNesT1EWvfm8mzKw_!!6000000000360-2-tps-600-315.png
- 项目主页: https://wan.video/
- API 文档: https://www.alibabacloud.com/help/en/model-studio/video-generation

#### Grok Imagine Video 1.5 — xAI (SpaceXSI) (2026-06-03)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 产品 / 应用, 公开 API
- 输入: 图像, 文字提示, 语音与音频 → 输出: 平面视频, 音效、音乐与空间音频
- 核心想法: 前沿视频模型同时通过聊天应用和开发者 API 提供：生成速度正与画质一样成为主要指标。
- 内容: Grok Imagine Video 1.5 是 xAI 的图生视频模型，提供于 Grok 应用中，并自 2026-06-03 起以 grok-imagine-video-1.5-preview 进入 xAI API：根据描述运镜、节奏与声音的提示让一张静态画面动起来，最高 720p，每段约 25 秒生成。2026-08-07 又推出支持文字、图像与声音参考、可输出 1080p 的版本。
- 实现方式: 闭源图生视频模型，可用提示控制镜头、运动与声音（架构未公开）。
- 参数: 720p in ~25 s (claimed) · up to 10 s per API call · references version: up to 1080p
- 能力维度: 感知真实感, 创作可及性
- 视频: https://www.youtube.com/watch?v=SIfDV2JjLL4
- 图片: https://media.x.ai/v1/website/grok-imagine-1-5-og-342e9fa3.webp
- 项目主页: https://x.ai/news/grok-imagine-1-5
- API 文档: https://docs.x.ai/docs/guides/video-generations

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

#### HappyHorse — Alibaba Token Hub (ATH) (2026-04-21)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 公开 API
- 输入: 文字提示, 图像, 视频 → 输出: 平面视频, 语音 / 声音, 音效、音乐与空间音频
- 核心想法: 匿名登榜说明前沿变化之快：阿里另一支团队未经发布的模型，在人类偏好评测中胜过了老牌视频模型。
- 内容: HappyHorse 是阿里巴巴的音视频模型，2026 年 4 月先以匿名身份出现在 Artificial Analysis 视频竞技场，据媒体报道一度排名第一，之后阿里巴巴 ATH 集团才认领。HappyHorse 1.0 于 2026-04-21 登陆百炼 API（文生、图生、参考生视频及视频编辑），HappyHorse 1.1 于 2026-06-16 推出；两者都能一次生成最长 15 秒、带声音的 1080p 视频。
- 实现方式: 据社区整理的资料，是一个对文本、图像、视频与音频 token 统一做自注意力的 150 亿参数 Transformer（未经阿里论文证实）。
- 参数: up to 15 s · 1080p · native audio · 1.0 API 2026-04-21 · 1.1 API 2026-06-16
- 能力维度: 感知真实感, 行为似真性
- 视频: https://www.youtube.com/watch?v=65EBGlhn-lQ
- 项目主页: https://www.alibabacloud.com/help/en/model-studio/newly-released-models
- API 文档: https://www.alibabacloud.com/help/en/model-studio/video-generation

#### PixVerse V6 — 爱诗科技 PixVerse (2026-03-30)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 产品 / 应用, 公开 API
- 输入: 文字提示, 图像 → 输出: 平面视频, 音效、音乐与空间音频, 语音 / 声音
- 核心想法: 智能体现在可以在命令行里直接生成带声音的多镜头成片，情境的多个变体无需剪辑即可批量产出。
- 内容: PixVerse V6（2026-03-30）是 PixVerse 应用的旗舰视频模型：一条提示即可生成最长 15 秒、1080p、带原生音频的多镜头短片，并在镜头切换间保持角色情绪一致；它还可以通过命令行工具由编程智能体调用。
- 实现方式: 闭源音视频联合生成模型，支持多镜头规划（架构未公开）。
- 参数: up to 15 s · 1080p · native audio · multi-shot
- 能力维度: 创作可及性, 感知真实感
- 视频: https://www.youtube.com/watch?v=m-qRU0SY8NQ
- 图片: https://media.pixverse.ai/asset/blog/pixverse-v6-launch-press-release-cover-20260330.webp?x-oss-process=style/cover-webp-large
- 项目主页: https://pixverse.ai/en/blog/pixverse-launches-v6-advancing-ai-video-generation
- API 文档: https://platform.pixverse.ai/

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
- 内容: Veo 3.1（2025-10-15）在 Veo 3 基础上带来更丰富的原生音频和更好的提示遵循，并在 Flow 与 Gemini API 中提供“素材生成视频”（参考图）、首尾帧过渡，以及延展到一分钟以上的场景扩展。更便宜的 Veo 3.1 Lite 于 2026-03-31 进入预览；Google 将于 2026-10-22 关闭 Gemini API 中的 Veo 3.1 预览端点，改由 gemini-omni-1.1-flash 取代，而 Vertex AI 上正式版 veo-3.1-generate-001 至少支持到 2026-11-17。
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
- 类型: 模型 · 时序: 预先生成 · 获取方式: 产品 / 应用
- 输入: 文字提示, 图像 → 输出: 平面视频, 语音 / 声音, 音效、音乐与空间音频
- 核心想法: 声音与口型同步的语音随画面一起生成，生成场景因此能承载社交互动，而不只是一段画面。
- 内容: Veo 3（2025-05-20 Google I/O）可一次生成视频及对白、音效和环境声，使生成场景里“会说话的角色”变得普遍；DeepMind 2025 年 9 月的论文称它能零样本完成感知与物理类任务。其 veo-3.0 API 端点已于 2026-06-30 在 Gemini API 与 Vertex AI 上关闭，由 Veo 3.1 取代。
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

#### Firefly 视频模型（Firefly Video Model） — Adobe (2025-02-12)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 产品 / 应用
- 输入: 文字提示, 图像 → 输出: 平面视频
- 核心想法: 训练数据的来源成了产品卖点，这对需要审核刺激材料版权的机构很重要。
- 内容: Adobe 的 Firefly 视频模型（2025-02-12 公开测试）可在 Firefly 网页应用与 Premiere Pro 中根据文字或图像生成视频片段，并提供镜头角度与景别控制；Adobe 称其只用授权与公有领域内容训练，因此“可安全商用”。
- 实现方式: 扩散视频模型，只用 Adobe Stock 等授权内容与公有领域素材训练，从不使用用户内容（据 Adobe；架构未公开）。
- 参数: 1080p (beta, 2025)
- 能力维度: 创作可及性, 实验控制
- 视频: https://www.youtube.com/watch?v=fjk2mMFBpRo
- 图片: https://blog.adobe.com/en/publish/2025/02/12/media_19846d436079bbe9de6505cc71ae92758436e7468.png?width=1200&format=pjpg&optimize=medium
- 项目主页: https://blog.adobe.com/en/publish/2025/02/12/meet-firefly-video-model-ai-powered-creation-with-unparalleled-creative-control

#### Veo 2 — 谷歌 DeepMind (2024-12-16)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 产品 / 应用
- 输入: 文字提示, 图像 → 输出: 平面视频
- 核心想法: 镜头类型和运镜成为可靠的提示参数，适合需要特定视角的情境素材。
- 内容: 第二代 Veo（2024-12-16），物理表现与镜头控制更好，最高可输出 4K；DeepMind 称其在发布时的人类偏好对比中优于 Sora Turbo、可灵与 MiniMax。后来开放于 Gemini API、Gemini 应用与 YouTube Shorts；其 Gemini API 端点（veo-2.0-generate-001）已于 2026-06-30 关闭。
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

#### Kandinsky 6.0 Video — Kandinsky Lab (2026-10-06)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 文字提示, 图像 → 输出: 平面视频, 语音 / 声音, 音效、音乐与空间音频
- 核心想法: MIT 许可的音视频联合权重，让更多人能在本地生成会说话的角色片段，不再局限于以英文和中文为主的模型。
- 内容: Kandinsky 6.0 Video（2026-10-06）是开源的文生 / 图生音视频模型系列，分 Lite（30 亿参数）与 Pro（290 亿参数）两种规模，可生成 5 秒、带同步 44 kHz 音频（含口型同步语音）的片段，并原生理解俄语。代码与权重以 MIT 许可证发布，支持 Diffusers 与 ComfyUI。
- 实现方式: 生成同步视频与音频的扩散 Transformer，经监督微调、强化学习后训练与蒸馏分阶段训练（据技术报告）。
- 参数: Lite 3B · Pro 29B · 5 s clips · 44 kHz audio · MIT licence
- 能力维度: 感知真实感, 实验控制
- 论文: https://arxiv.org/abs/2610.05608 (arXiv 2026)
- 视频: https://kandinskylab.ai/media/img/models/video-promo-v3.mp4
- 图片: https://kandinskylab.ai/img/showreel-poster.jpg
- 项目主页: https://kandinskylab.ai/models/video/
- 代码: https://github.com/kandinskylab/kandinsky-6

#### Video DeltaNet：面向直播式视频生成的混合注意力（VDN-H3）（Video DeltaNet (VDN-H3)） — Haocheng Xi (2026-09-06)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 文字提示, 图像 → 输出: 平面视频, 音效、音乐与空间音频
- 核心想法: 当一个开源音视频模型的渲染速度超过实时，情境片段就可以在两次试验之间按需生成，而不必提前准备。
- 内容: Video DeltaNet（加州大学伯克利分校与 Impossible, Inc.，2026-09-06）是 MiniMax H3 音视频模型的开源混合注意力版本（VDN-H3）：在 8 张 B200 上约 9 秒就能生成一段 14.4 秒、768p 的有声视频，比播放还快，作者称画质几乎无损。权重、训练与推理代码均已开源，社区项目 FreeVideo 在此基础上让 H3 可在 8 GB 显存的显卡上运行。
- 实现方式: 把部分视频到视频的注意力替换为 Video Delta Attention（逐帧更新的双向线性记忆），并保留局部 softmax 注意力（涉及文本和音频的交互仍用 softmax）；通过分阶段的教师对齐引入新分支，再蒸馏到 8 步，用 SGLang Diffusion 部署。
- 参数: 14.4 s · 768p with audio · ~9.0 s end-to-end on 8×B200 (6.9 s denoising) · 8 steps · 14.5× over 50-step dense H3 (developer-reported)
- 能力维度: 时间响应性, 创作可及性
- 论文: https://arxiv.org/abs/2609.20744 (arXiv preprint)
- 视频: https://openvdn.github.io/GeneratedVideos/hf_test_5_vdn_stage_d_step250_8nfe.mp4
- 项目主页: https://openvdn.github.io/
- 代码: https://github.com/OpenVDN/vdn-minimax-h3

#### LTX-2.5 — Lightricks (2026-08-11)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码, 公开 API, 产品 / 应用
- 输入: 文字提示, 图像, 视频 → 输出: 平面视频, 音效、音乐与空间音频
- 核心想法: 可锁定版本、可微调的开源模型已能生成带声音的多镜头场景，实验室可以固定刺激材料生成器的版本，并用自己的素材训练它。
- 内容: LTX-2.5（2026-08-11）是 Lightricks 的 220 亿参数开源权重音视频模型，LTX 将其称为“开放世界模型”：它能一次生成多镜头序列，在镜头切换间保持角色、场景与声音一致，并配套 HDR、Alpha 遮罩、修复、布局到渲染等 IC-LoRA。权重以 LTX 社区许可证发布在 Hugging Face，发布当天即支持 ComfyUI。
- 实现方式: 在 8 倍时间压缩的潜空间中运行的扩散 Transformer，配合新的扩散式视频解码器、Gemma 4 文本编码器与提示增强器，以及按场景复杂度增加高保真关键帧的“Diffusion Fidelity Rendering”（据 LTX）。
- 参数: 22B · open weights · native multi-shot · synchronized audio · 16 GB min VRAM (claimed)
- 能力维度: 实验控制, 感知真实感, 创作可及性
- 视频: https://www.youtube.com/watch?v=ZDfjZae7Da0
- 图片: https://cdn.prod.website-files.com/68c6ddbeb26cbd692adc0291/6a7afda4f4de5e107c04180b_Cover-Newsroom.png
- 项目主页: https://ltx.io/newsroom/introducing-ltx-2-5
- API 文档: https://ltx.io/model/ltx-2-5
- 代码: https://huggingface.co/Lightricks/LTX-2.5

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

#### AnimateDiff：无需专门调优即可让个性化文生图模型动起来（AnimateDiff） — Yuwei Guo (2023-07-10)
- 类型: 开源工具 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 文字提示, 图像 → 输出: 平面视频
- 核心想法: 把运动与外观分开，让任何图像画风都能动起来，这是开源社区自建视频工具的早期信号。
- 内容: AnimateDiff（香港中文大学、上海人工智能实验室与斯坦福，2023 年 7 月；ICLR 2024 spotlight）为 Stable Diffusion 增加一个即插即用的运动模块，让任何社区微调的图像模型都能以自身画风生成短动画，并用 MotionLoRA 控制镜头运动；它成为 ComfyUI 开源视频工具链的常用组件。
- 实现方式: 在视频上训练时间运动模块，并插入冻结的文生图 U-Net；MotionLoRA 只需少量数据即可适配新的运动模式。
- 参数: 16-frame clips (default) · plug-in for Stable Diffusion 1.5
- 能力维度: 创作可及性, 情境多样性
- 论文: https://arxiv.org/abs/2307.04725 (ICLR 2024)
- 视频: https://animatediff.github.io/animations/teaser/ani_01.mp4
- 图片: https://animatediff.github.io/figs/framework.jpg
- 项目主页: https://animatediff.github.io/
- 代码: https://github.com/guoyww/AnimateDiff

### 控制、编辑与角色

镜头路径、动作迁移、参考角色、视频到视频编辑与表演驱动的动画。

#### 4Director：用刚体 3D 几何控制视频世界模型（4Director） — Stability AI (2026-10-01)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像, 镜头路径 / 位姿, 场景规格、代码与规则 → 输出: 平面视频
- 核心想法: 像布置 3D 场景那样安排物体路径和镜头，再得到逼真的视频，这已接近实验者编排一场情境事件的方式。
- 内容: 4Director（Stability AI 与伊利诺伊大学厄巴纳-香槟分校，2026 年 10 月）从一张图像出发“导演”视频：每个物体只重建一次为网格，并按帧施加一个刚体 3D 变换，因此镜头运动、已有物体与新插入的物体都在同一个 3D 空间中控制，物体从新角度看也保持形状。
- 实现方式: 把受控的网格场景渲染为深度视频，再由 Motion Adapter 转换成外观、光照与非刚性运动都视角一致的视频；训练数据为 RealCOD-Rigid，含 20,774 段标注了刚体 3D 场景的视频。
- 参数: RealCOD-Rigid: 20,774 clips
- 能力维度: 实验控制, 持久性
- 论文: https://arxiv.org/abs/2610.02160 (arXiv 2026)
- 视频: https://stability-ai.github.io/4director/assets/4Director-supplementary.mp4
- 图片: https://stability-ai.github.io/4director/assets/feature-hiker.png
- 项目主页: https://stability-ai.github.io/4director/
- 代码: https://github.com/VVeiCao/4Director

#### 4DStreamCtrl：在线 4D 控制的交互式视频生成（4DStreamCtrl） — Shiqian Li, 腾讯混元 (2026-08-26)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入: 图像, 镜头路径 / 位姿, 草图与手势 → 输出: 交互式帧流
- 核心想法: 把镜头、物体运动和深度统一为一种可在生成中途修改的三维控制信号，这正是实验者在生成视频里编排事件所需的闭环控制。
- 内容: 4DStreamCtrl（北京大学与腾讯混元，2026-08-26）在流式生成视频的同时，让用户通过三维点轨迹操控镜头和单个物体：在视频播放中用笔刷就能让球滚动、推动罐子或移动人物。作者报告，它在单张高端显卡上以 480p、20 fps 运行，数百帧内保持连贯，并称其为首个可交互 4D 控制的流式生成器。
- 实现方式: 镜头运动、物体轨迹和深度被统一编码为三维点轨迹，由一个轻量的 Geometric Motion Head 接入预训练视频扩散模型；训练数据是从真实视频中挖掘的 OpenVidHD-Motion3D 轨迹；之后蒸馏成一个四步因果流式学生模型，显存占用不随视频长度增长。
- 参数: 480p · 20 fps on one high-end GPU · 4 denoising steps · hundreds of frames (developer-reported)
- 能力维度: 实验控制, 时间响应性, 反应性
- 论文: https://arxiv.org/abs/2608.25479 (arXiv preprint)
- 视频: https://4dstreamctrl.github.io/videos/demo.mp4
- 项目主页: https://4dstreamctrl.github.io/

#### Vista4D：基于 4D 点云的视频重拍（Vista4D） — Eyeline Labs (Netflix) (2026-04-23)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 视频, 镜头路径 / 位姿 → 输出: 平面视频
- 核心想法: 一次拍摄可以从其他机位观看，录好的情境在事后也能改变视角。
- 内容: Vista4D（Eyeline Labs 与 Netflix，联合哥伦比亚大学、加州大学洛杉矶分校等，CVPR 2026 Highlight）用新的镜头轨迹“重拍”已有视频，同时保持原有动作：输入被提升为 4D 点云，用来保留已拍到的内容并引导镜头，其余部分由模型补全；它还支持场景扩展与重新组合。代码与模型已公开。
- 实现方式: 通过带静态像素分割的 4D 重建得到点云，沿目标镜头路径渲染；视频模型在重建的多视角动态数据上训练，可容忍点云伪影，并据此生成最终视频。
- 能力维度: 实验控制, 感知真实感
- 获奖与认可: CVPR 2026 Highlight
- 论文: https://arxiv.org/abs/2604.21915 (CVPR 2026)
- 视频: https://eyeline-labs.github.io/Vista4D/media/ours_snowboard_back-follow_s52106.mp4
- 图片: https://eyeline-labs.github.io/Vista4D/media/preview.jpg
- 项目主页: https://eyeline-labs.github.io/Vista4D/
- 代码: https://github.com/Eyeline-Labs/Vista4D

#### VerseCrafter：具备 4D 几何控制的动态真实视频世界模型（VerseCrafter） — Sixiao Zheng, 腾讯 ARC 实验室 (2026-01-08)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像, 镜头路径 / 位姿, 场景规格、代码与规则 → 输出: 平面视频
- 核心想法: 谁往哪里走、从哪个视角看，变成可检查的 3D 规格而不是一句提示，这正是布置实验情境所需要的控制。
- 内容: VerseCrafter（复旦大学、香港大学与腾讯 ARC 实验室，CVPR 2026）根据显式的 4D 世界状态生成视频：静态背景点云加上每个物体的 3D 高斯轨迹，因此可以同时指定镜头路径与多个物体的运动，生成结果会照此执行。代码、模型、Blender 插件与 3.5 万段的 VerseControl4D 数据集均已公开。
- 实现方式: 把 4D 几何控制（背景点云与各物体的高斯轨迹）渲染为控制图，作为预训练视频扩散模型的条件；训练数据来自自动构建的真实世界数据集。
- 参数: VerseControl4D: 35K training clips
- 能力维度: 实验控制, 行为似真性
- 论文: https://arxiv.org/abs/2601.05138 (CVPR 2026)
- 视频: https://sixiaozheng.github.io/VerseCrafter_page/assets/pipeline_video_com.mp4
- 图片: https://sixiaozheng.github.io/VerseCrafter_page/assets/framework.png
- 项目主页: https://sixiaozheng.github.io/VerseCrafter_page/
- 代码: https://github.com/TencentARC/VerseCrafter

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
- 内容: Wan-Animate（2025 年 9 月）可用驱动视频中的身体动作与面部表情来驱动一张角色图，或把视频中的人替换成该角色并匹配场景光照；权重以 Wan2.2-Animate-14B 开源。Wan-Animate-2（2026-08-07 开源权重）改用重新设计的扩散 Transformer 直接读取驱动视频。
- 实现方式: 基于 Wan 2.2，用骨架信号控制身体动作，用隐式面部特征控制表情，并用重光照 LoRA 完成角色替换。
- 参数: 14B
- 能力维度: 行为似真性, 实验控制
- 论文: https://arxiv.org/abs/2509.14055 (arXiv 2025)
- 视频: https://humanaigc.github.io/wan-animate/content/aa/rep_shots.mp4
- 图片: https://humanaigc.github.io/wan-animate/content/aa/arch.png
- 项目主页: https://humanaigc.github.io/wan-animate/
- 代码: https://huggingface.co/Wan-AI/Wan2.2-Animate-14B

#### 通义万相 Wan-S2V（Wan-S2V） — 阿里通义 (2025-08-26)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像, 语音与音频, 文字提示 → 输出: 平面视频, 虚拟人（脸 / 身体）
- 核心想法: 由音频驱动、带有肢体语言与运镜的角色，让对话场景走出“说话头像”的画框。
- 内容: Wan-S2V（阿里通义实验室，2025-08-26）把一张静态图和一段音频变成影视风格的角色视频：人物说话、唱歌或表演，带有全身或半身动作与运镜，而不只是一个说话的头像；140 亿参数模型作为 Wan 2.2 的一部分开源。
- 实现方式: 在 Wan 视频模型上加入音频条件，并用文字控制整体场景，另有长视频与口型同步编辑模式。
- 参数: 14B · open weights (Wan2.2-S2V-14B)
- 能力维度: 行为似真性, 感知真实感
- 论文: https://arxiv.org/abs/2508.18621 (arXiv 2025)
- 视频: https://humanaigc.github.io/wan-s2v-webpage/content/v3/video/1-moive_talk.mp4
- 图片: https://humanaigc.github.io/wan-s2v-webpage/content/v3/superman.png
- 项目主页: https://humanaigc.github.io/wan-s2v-webpage/
- 代码: https://huggingface.co/Wan-AI/Wan2.2-S2V-14B

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

#### Vidu S2 — 生数科技（Vidu） (2026-09-10)
- 类型: 模型 · 时序: 实时流式 · 获取方式: 产品 / 应用
- 输入: 语音与音频, 图像, 视频 → 输出: 交互式帧流, 虚拟人（脸 / 身体）, 360° / 立体视频
- 核心想法: 实时生成不再只是一个会回话的角色：同一条视频流还能改写摄像头或头显看到的画面，让视频模型成为覆盖在参与者真实环境之上的实时图层。
- 内容: Vidu S2 是生数科技的第二代实时视频系统：S2-Avatar 根据一张参考图驱动角色边听边答，分辨率提升到 720p，参考图可在生成过程中随时更换，还能执行跳舞等动作；S2-Editing 则在视频播放或摄像头直播时实时改写画面，替换服装、人物或背景。生数还展示了把两种视频流实时转换为左右眼画面、用于 VR 头显和透视画面的效果；截至 2026 年 10 月，vidu.com 提供可试玩的在线演示。
- 实现方式: 延续 Vidu S1 的因果自回归视频扩散路线（基于 TurboDiffusion 与 TurboServe），主干与精修模块分别使用不同噪声水平的历史缓存，再用一步超分 Refiner 把 540p 主干输出提升到 720p；S2-Editing 让每个输出片段以输入的源视频帧为条件，立体视图则在流式管线内部生成。
- 参数: 720p · 25–42 fps real-time (Vidu S1: 540p) · live camera-stream editing · stereo output explored (developer-reported)
- 能力维度: 时间响应性, 反应性, 创作可及性
- 论文: https://arxiv.org/abs/2609.11638 (Technical report (arXiv))
- 视频: https://www.youtube.com/watch?v=h60wG1w0jOY
- 项目主页: https://www.vidu.com/vidu-stream

#### Ring Forcing：自回归视频扩散的精确长时记忆（Ring Forcing） — Bowen Xue (2026-08-27)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 文字提示 → 输出: 平面视频
- 核心想法: 限制数分钟情境视频的是记忆而不是分辨率：生成的房间必须把先前出现过的物体原样还回来，长片段的实验控制正需要这一点。
- 内容: Ring Forcing（斯坦福大学与字节跳动，ECCV 2026）针对自回归长视频中的物体恒存性：一本书、一辆车或一幅画离开画面，最长一分钟后再回到画面时，应当保持原样。作者报告，它能维持数分钟的连贯性，物体重新出现时也比以往的长视频方法更忠实。
- 实现方式: 用正放再倒放的环形训练片段，迫使模型从久远的历史中检索内容；通过历史压缩和时间步组合，在固定序列长度下把有效上下文延伸到数分钟；稀疏 RoPE 让预训练视频先验适配长记忆。
- 参数: re-appearance after gaps of 15–60 s · minutes-long effective history (developer-reported)
- 能力维度: 持久性, 实验控制
- 论文: https://arxiv.org/abs/2608.26794 (ECCV 2026)
- 视频: https://ringforcing.com/media/gallery/adr/extended/gap-60/case-01.mp4
- 图片: https://ringforcing.com/og.png
- 项目主页: https://ringforcing.com

#### 京东 JoyAI-Video-Edit：实时开放式视频编辑（JoyAI-Video-Edit） — 京东 (2026-08-05)
- 类型: 开源工具 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 视频, 文字提示, 图像 → 输出: 交互式帧流
- 核心想法: 开源、可在消费级显卡上运行的摄像头实时改写：参与者在活动时，同一个房间或同一个人就能被换成另一种情境。
- 内容: JoyAI-Video-Edit（京东，2026-08-05）在画面到达时即时编辑实时摄像头流或上传的视频，按文字指令或参考图换装、换背景或改变画风，其余部分保持不变。京东称其在单张 B200 上以约 30 fps 输出 720p，在单张 RTX 5090 上以 24 fps 输出 840x480；权重、代码与浏览器摄像头演示均已公开。
- 实现方式: 160 亿参数多模态扩散 Transformer，配合多模态大模型条件编码器与因果视频 VAE，按块改造为自回归生成，并通过源锚定分布匹配蒸馏到两步。
- 参数: 16B · ~30 fps 720p on 1 B200 · 24 fps 840x480 on RTX 5090 (reported)
- 能力维度: 时间响应性, 反应性, 情境可达性
- 论文: https://arxiv.org/abs/2608.03974 (arXiv 2026)
- 视频: https://github.com/user-attachments/assets/bca232c9-75df-46f9-b366-14cfa2651994
- 图片: https://raw.githubusercontent.com/jd-opensource/JoyAI-Video-Edit/main/assets/live_demo/live_cartoon_group.jpg
- 项目主页: https://github.com/jd-opensource/JoyAI-Video-Edit
- 代码: https://huggingface.co/jdopensource/JoyAI-Video-Edit

#### Visko Orbis 1.0：实时交互长视频“活模型”（Visko Orbis 1.0） — Visko (2026-07-29)
- 类型: 模型 · 时序: 实时流式 · 获取方式: 产品 / 应用
- 输入: 文字提示, 图像, 视频 → 输出: 交互式帧流
- 核心想法: 把生成的场景当作一个持续运行、可随时引导的过程，而不是一次次请求的片段；长时、可调控的实验情境正需要这种框架。
- 内容: Visko Orbis 1.0 是一个“活模型”（Live Model）：用户随时修改提示词时，它仍持续生成视频，每次修改都会在正在播放的视频流中立刻体现。Visko 称它能以 4K、24 fps 实时生成，连续运行一小时也没有明显的色彩或画质漂移。2026 年 9 月 1 日起，visko.ai 对公众开放（需登录）。
- 实现方式: 经过蒸馏的分块因果流式生成器，带有跨块的有界多尺度记忆，并用潜空间世界模型奖励对齐；之后接流式视频超分和优化的 GPU 推理引擎（来自团队技术报告，架构细节有限）。
- 参数: 4K · 24 fps real-time · hour-scale rollouts (developer-reported)
- 能力维度: 时间响应性, 持久性
- 论文: https://arxiv.org/abs/2607.26694 (Technical report (arXiv))
- 视频: https://assets.visko.ai/home/orbis/orbis-720p.webm
- 图片: https://assets.visko.ai/blogs/graphs/introducing-live-models-preview.webp
- 项目主页: https://www.visko.ai/blog/introducing-live-models

#### Vidu S1 — 生数科技（Vidu） (2026-07-03)
- 类型: 模型 · 时序: 实时流式 · 获取方式: 产品 / 应用
- 输入: 语音与音频, 文字提示, 图像 → 输出: 交互式帧流, 语音 / 声音
- 核心想法: 跟得上对话节奏的视频生成，把视频模型带进了虚拟人的轮流对话循环。
- 内容: Vidu S1（2026-07-03）是生数科技的实时交互视频模型：你对它说话时，生成的角色或场景会在毫秒级作出回应，可用于“会说话的宠物”、游戏陪伴等场景。
- 实现方式: 以流式语音输入为条件的实时视频生成；架构未公开。
- 能力维度: 时间响应性, 反应性, 行为似真性
- 视频: https://www.youtube.com/watch?v=jaPLmykNk0I
- 项目主页: https://www.vidu.com/

#### LiveEdit：基于扩散的实时流式视频编辑（LiveEdit） — Xinyu Wang (2026-06-25)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 视频, 文字提示 → 输出: 交互式帧流
- 核心想法: 保留未编辑区域的实时编辑正是透视画面改写所需要的：只改变视野中的一个物体，房间其余部分不会闪烁。
- 内容: LiveEdit（清华大学与港科大，ECCV 2026）按文字指令逐帧编辑实时视频流，只改动指定区域，背景与未编辑部分保持稳定；作者报告其 4 步蒸馏的因果模型可达 12.66 fps。
- 实现方式: 三阶段蒸馏，把双向编辑模型迁移为因果、按块的流式 DiT，并用面向自回归的掩码缓存复用未编辑区域的计算。
- 参数: 12.66 fps · 4-step distilled · causal DiT (reported)
- 能力维度: 时间响应性, 实验控制
- 论文: https://arxiv.org/abs/2606.26740 (ECCV 2026)
- 视频: https://live-edit.github.io/assets/liveedit/teaser.mp4
- 图片: https://live-edit.github.io/assets/liveedit/Framework-v2_page-0001.jpg
- 项目主页: https://live-edit.github.io/
- 代码: https://github.com/cp-cp/LiveEdit

#### SANA-Streaming：实时流式视频编辑（SANA-Streaming） — 英伟达 (2026-05-28)
- 类型: 模型 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 视频, 文字提示 → 输出: 交互式帧流
- 核心想法: 在消费级显卡上做分钟级的视频到视频编辑，使实时改写参与者的摄像头画面或录制好的情境变得可行，原视频的动作就是控制信号。
- 内容: SANA-Streaming（英伟达，2026-05-28）是一个 2B 参数的开源模型，可按文字指令实时编辑直播或录制的视频流，例如改变风格、替换背景或物体；在单张 RTX 5090 上以 1280×704、端到端 24 fps 运行，可处理约一分钟长的视频。权重于 2026 年 6 月发布，训练代码于 7 月发布，Reactor 上有托管演示。
- 实现方式: 混合扩散 Transformer 把线性注意力（gated DeltaNet）模块与部分 softmax 注意力模块结合；训练时加入循环反推正则，从编辑结果反向预测源视频帧；部署时使用融合算子和针对 Blackwell 显卡调优的混合精度量化。
- 参数: 1280×704 · 24 fps end-to-end (DiT 58 fps) on one RTX 5090 · 2B parameters · up to ~1 min
- 能力维度: 时间响应性, 感知真实感, 持久性
- 论文: https://arxiv.org/abs/2605.30409 (arXiv preprint)
- 视频: https://huggingface.co/datasets/Efficient-Large-Model/Sana-assets/resolve/main/Streaming/assets/teaser/sana-streaming-teaser.mp4
- 图片: https://huggingface.co/datasets/Efficient-Large-Model/Sana-assets/resolve/main/Streaming/assets/figures/latency-breakdown.png
- 项目主页: https://nvlabs.github.io/Sana/Streaming/
- 代码: https://github.com/NVlabs/Sana

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

#### Causal Forcing：面向实时交互视频的自回归扩散蒸馏（Causal Forcing） — Hongzhou Zhu (2026-02-02)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 文字提示, 图像 → 输出: 交互式帧流
- 核心想法: 改进的是实时视频学生模型的初始化方式，而不是推理方式，因此在相同的流式算力下能生成更多运动；它已成为交互视频研究常用的起点。
- 内容: Causal Forcing（清华大学，ICML 2026）是一套蒸馏方法和一组开源权重，可把双向视频扩散模型变成用于实时交互视频的少步自回归生成器。作者报告，在相同推理开销下，它在动态程度上比 Self Forcing 高 19.3%，在指令遵循上高 16.7%；后续版本 Causal Forcing++ 又推出了 2 步和 1 步逐帧模型，2026 年的多项长视频方法以它为基础模型。
- 实现方式: 先用自回归教师模型做 ODE 蒸馏来初始化因果学生模型（双向教师的流映射无法被因果学生复现），再沿用 Self Forcing 的 DMD 训练；基于 Wan 1.3B 发布了分块与逐帧两种版本。
- 参数: Wan 1.3B base · 4-step chunk-wise and frame-wise · 2-step and 1-step frame-wise (Causal Forcing++)
- 能力维度: 时间响应性, 感知真实感
- 论文: https://arxiv.org/abs/2602.02214 (ICML 2026)
- 视频: https://thu-ml.github.io/CausalForcing.github.io/videos/demo.mp4
- 项目主页: https://thu-ml.github.io/CausalForcing.github.io/
- 代码: https://github.com/thu-ml/Causal-Forcing

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

#### Self-Forcing++：迈向分钟级高质量视频生成（Self-Forcing++） — Justin Cui, 字节跳动 Seed (2025-10-02)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 文字提示 → 输出: 平面视频
- 核心想法: 分钟级的连贯不再需要分钟级的训练视频，这对必须完整展开一段遭遇的情境很重要。
- 内容: Self-Forcing++（加州大学洛杉矶分校与字节跳动 Seed，2025 年 10 月）把从只能生成短片的教师模型蒸馏而来的少步自回归视频模型延伸到数分钟仍保持连贯：作者报告最长 4 分 15 秒，是基线长度的 50 倍以上，且没有过曝或漂移。截至 2026 年 10 月，代码仓库只有论文与演示，尚未发布代码。
- 实现方式: 让短时长教师模型纠正从学生模型自身长序列中采样的片段（在自生成视频上做分布匹配），且无需重复计算重叠帧。
- 参数: up to 4 min 15 s · 20x beyond teacher horizon (reported)
- 能力维度: 持久性, 感知真实感
- 论文: https://arxiv.org/abs/2510.02283 (arXiv 2025)
- 视频: https://huggingface.co/datasets/self-forcing-plus-plus/website/resolve/main/merged/merged_snow_valley.mp4
- 图片: https://self-forcing-plus-plus.github.io/images/workflow.png
- 项目主页: https://self-forcing-plus-plus.github.io/
- 代码: https://github.com/justincui03/Self-Forcing-Plus-Plus

#### Rolling Forcing：实时自回归长视频扩散（Rolling Forcing） — Kunhao Liu, 腾讯 ARC 实验室 (2025-09-29)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 文字提示 → 输出: 交互式帧流
- 核心想法: 实时与长时长在一个开源模型中兼得：视频流能以交互速率持续数分钟才出现漂移。
- 内容: Rolling Forcing（南洋理工大学与腾讯 ARC 实验室，ICLR 2026）在单张 GPU 上实时流式生成数分钟视频且误差累积很小：它对一个窗口内的多帧以递增噪声水平同时去噪，而不是逐帧生成。
- 实现方式: 在滚动窗口内以递增噪声联合去噪，用注意力汇（attention sink）保留起始帧的键值状态作为全局锚点，并在不重叠窗口上做少步蒸馏。
- 参数: real-time on 1 GPU · multi-minute streams (reported)
- 能力维度: 时间响应性, 持久性
- 论文: https://arxiv.org/abs/2509.25161 (ICLR 2026)
- 视频: https://kunhao-liu.github.io/Rolling_Forcing_Webpage/videos/2min_videos/A%20dynamic%20action%20scene%20in%20a%20modern%20gym%2C%20featuring%20a%20kangaroo%20wearing%20boxing%20gloves%2C%20engaged%20in%20an%20in-0.mp4
- 项目主页: https://kunhao-liu.github.io/Rolling_Forcing_Webpage/
- 代码: https://github.com/TencentARC/RollingForcing

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
- 内容: Sand AI 的 MAGI-1（2025-04-21）是 240 亿参数的开源自回归视频模型，逐块生成视频，支持流式输出、无限延展和逐块更换提示。Sand AI 随后于 2026-08-05 发布 MAGI-2 Preview：开源的 1140 亿参数混合专家模型，每个 token 激活 60 亿参数，可生成带声音的 10 秒片段。
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
- 内容: 昆仑万维 Skywork 的 SkyReels-V2（2025 年 4 月）是开源的“无限时长电影”模型，可在保持镜头一致的同时不断延展视频，训练时使用了电影语法标注。Skywork 于 2026-01-29 以开源权重发布 SkyReels V3，新增多主体参考生视频、音频引导生成与视频到视频生成。
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

#### Pantheon360：用 3D 感知 360° 视频扩散生成数字孪生（Pantheon360） — Ting-Hsuan Chen (2026-05-25)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 多视角拍摄 / 扫描, 镜头路径 / 位姿 → 输出: 360° / 立体视频
- 核心想法: 对真实场所的几次全景拍摄，就能变成可沿任意路径重走的 360° 视频，而且几何是固定的，不会逐帧重新想象。
- 内容: Pantheon360（南加州大学、阳明交通大学、康奈尔大学与博世研究院，CVPR 2026）根据对某个地点的稀疏 360° 拍摄，沿用户自定的任意镜头路径生成 360° 视频：从输入重建的显式 3D 缓存保证几何一致，视频扩散模型负责细化外观，目标是用于仿真的数字孪生。代码标注为即将发布。
- 实现方式: 从稀疏的 360° 输入重建 3D 缓存，沿目标镜头路径渲染作为几何支架，再由 360° 视频扩散模型细化纹理并补全空缺。
- 能力维度: 持久性, 实验控制, 情境可达性
- 论文: https://arxiv.org/abs/2605.25449 (CVPR 2026)
- 视频: https://koi953215.github.io/pantheon360_page/pantheon360_videos/teaser.mp4
- 图片: https://koi953215.github.io/pantheon360_page/pantheon360_img/pipeline.jpg
- 项目主页: https://koi953215.github.io/pantheon360_page/

#### Stereo World Model：相机可控的立体视频生成（Stereo World Model） — Yang-Tian Sun, VAST 光影焕像 (2026-03-18)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像, 镜头路径 / 位姿 → 输出: 360° / 立体视频
- 核心想法: 同时生成双眼画面，使深度与镜头路径保持一致；这是人们在头显里环顾而不是平面观看情境的前提。
- 内容: Stereo World Model（StereoWorld；香港大学、VAST 与字节跳动 Pico，CVPR 2026）沿给定的镜头路径同时生成左右眼视频，而不是先生成平面视频再转成立体。作者报告，它比“先生成再转换”的管线快 3 倍以上，视差也更准确，并可直接用于无需深度估计或补全的双目 VR 渲染；代码和权重均已开源。
- 实现方式: 在预训练视频扩散模型上微调：统一的相机-帧 RoPE 让镜头条件在视角和时间上保持一致；立体感知注意力把完整的 4D 注意力分解为单视角 3D 注意力加沿极线的水平行注意力；全程只用 RGB，不需要深度输入。
- 参数: >3× faster than monocular-then-convert pipelines · +5% viewpoint consistency (developer-reported)
- 能力维度: 感知真实感, 实验控制
- 论文: https://arxiv.org/abs/2603.17375 (CVPR 2026)
- 视频: https://assets.vast-eden.ai/assets/stereo-world/videos/demo.mp4
- 图片: https://assets.vast-eden.ai/assets/stereo-world/images/teaser.jpg
- 项目主页: https://vast-eden.ai/?p=stereo-world
- 代码: https://github.com/VAST-AI-Research/StereoWorld

#### CubeComposer：从透视视频时空自回归生成 4K 360° 视频（CubeComposer） — Lingen Li, 腾讯 ARC 实验室 (2026-03-04)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 视频, 文字提示 → 输出: 360° / 立体视频
- 核心想法: 用一段手机视频得到头显级分辨率的 360° 画面：拍到的一个角度可以变成整个场景的环绕视野。
- 内容: CubeComposer（香港中文大学与腾讯 ARC 实验室，CVPR 2026）把普通透视视频扩展为原生 4K 的 360° 视频：它按空间与时间顺序逐个生成立方体贴图的六个面，而不是把低分辨率全景图放大。代码、权重与 4K360Vid 数据集均已公开。
- 实现方式: 在立方体贴图各面与时间窗口上进行时空自回归视频扩散，配合立方体面上下文管理与稀疏上下文注意力。
- 参数: native 4K · 360° equirectangular / cubemap output
- 能力维度: 感知真实感, 情境可达性
- 论文: https://arxiv.org/abs/2603.04291 (CVPR 2026)
- 视频: https://lg-li.github.io/pub-videos/CubeComposer/li2026cubecomposer-video.mp4
- 图片: https://raw.githubusercontent.com/TencentARC/CubeComposer/main/assets/images/Teaser.jpg
- 项目主页: https://lg-li.github.io/project/cubecomposer
- 代码: https://github.com/TencentARC/CubeComposer

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

#### StereoWorld：几何感知的单目转立体视频生成（StereoWorld） — Ke Xing (2025-12-10)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 视频 → 输出: 360° / 立体视频
- 核心想法: 生成的或已有的平面素材无需立体摄影机，也能以可信的深度在头显中播放。
- 内容: StereoWorld（北京交通大学与 Dzine AI，CVPR 2026）把预训练视频生成模型改造成单目转立体的转换器：输入普通视频，在几何约束监督下生成另一只眼的画面；训练数据是 1100 多万帧按人眼瞳距对齐的蓝光左右格式视频。
- 实现方式: 以单目视频为条件端到端微调视频扩散模型，配合几何感知正则化与时空分块以支持高分辨率。
- 参数: 11M+ stereo training frames (IPD-aligned)
- 能力维度: 感知真实感, 情境可达性
- 论文: https://arxiv.org/abs/2512.09363 (CVPR 2026)
- 视频: https://ke-xing.github.io/StereoWorld/sfsf.mp4
- 图片: https://ke-xing.github.io/StereoWorld/big.png
- 项目主页: https://ke-xing.github.io/StereoWorld/
- 代码: https://github.com/ke-xing/StereoWorldCode

#### Immersity — Leia Inc. (2025-08-13)
- 类型: 产品 / 应用 · 时序: 预先生成 · 获取方式: 产品 / 应用
- 输入: 图像, 视频 → 输出: 360° / 立体视频, 图像 / 全景图
- 核心想法: 消费级的 2D 转 3D 意味着现有的平面素材库可以低成本地以深度形式用于头显研究。
- 内容: Immersity 是 Leia Inc. 的深度 3D 平台：其网页应用把照片、视频和专辑封面转换为可用于社交媒体、广告或 VR 的 3D 内容，同一套“空间 AI”软件也驱动 Leia 提供给设备厂商的 2D/3D 可切换显示屏。Leia 于 2025-08-13 发布 Immersity 平台。
- 实现方式: 对普通图像和视频做单目深度估计与视图合成（“空间 AI”），输出到 3D 显示屏与立体格式（细节未公开）。
- 能力维度: 情境可达性, 创作可及性
- 视频: https://s3.us-east-1.amazonaws.com/static.immersity.ai/videos/HOMEPAGE/Homepage-Reel_Desktop_compressed.mp4
- 图片: https://static.immersity.ai/img/og-image.png
- 项目主页: https://www.immersity.ai/
- API 文档: https://app.immersity.ai

#### S²VG：基于去噪帧矩阵的 3D 立体与空间视频生成（S²VG） — Peng Dai, 谷歌 (2025-08-11)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 文字提示, 视频 → 输出: 360° / 立体视频
- 核心想法: 任何文生视频模型都能通过后处理变成面向头显的立体或空间视频生成器。
- 内容: S²VG（香港大学与 Google，2025 年 8 月）无需训练、也无需相机位姿，就能把现成单目视频生成模型的输出变成 3D 立体视频与空间视频：它用估计的深度把生成视频扭曲到新视点，再在视角与时间上补全空洞。
- 实现方式: 基于深度把画面扭曲成由视点与时间组成的帧矩阵，再在两个维度上用视频模型的去噪过程进行免训练补全。
- 能力维度: 情境可达性, 感知真实感
- 论文: https://arxiv.org/abs/2508.08048 (arXiv 2025)
- 视频: https://daipengwa.github.io/S-2VG_ProjectPage/results1/teaser.mp4
- 图片: https://daipengwa.github.io/S-2VG_ProjectPage/images/astronaut.png
- 项目主页: https://daipengwa.github.io/S-2VG_ProjectPage/

#### Eye2Eye：单目转立体视频合成的简单方法（Eye2Eye） — Michal Geyer, 谷歌 DeepMind (2025-04-30)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 视频 → 输出: 360° / 立体视频
- 核心想法: 用生成先验而非深度图来合成立体画面，避免了在反光或透明表面上破坏临场感的扭曲伪影。
- 内容: Eye2Eye（Google DeepMind 与魏茨曼科学研究所，2025 年 4 月）把一段真实单目视频当作右眼画面，用微调后的文生视频模型生成左眼视频，两者可以用 3D 眼镜或 VR 头显观看；由于跳过了深度估计与扭曲，它能处理玻璃、雪花等反光与半透明物体。
- 实现方式: 以输入视角为条件微调预训练文生视频扩散模型，直接生成另一只眼的视图，不使用显式深度或扭曲。
- 能力维度: 感知真实感
- 论文: https://arxiv.org/abs/2505.00135 (arXiv 2025)
- 视频: https://video-eye2eye.github.io/static/videos/Demo.mp4
- 图片: https://video-eye2eye.github.io/static/images/pipeline.png
- 项目主页: https://video-eye2eye.github.io/

#### VideoPanda：基于多视角注意力的全景视频扩散（VideoPanda） — Kevin Xie, 英伟达 (2025-04-15)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 文字提示, 视频 → 输出: 360° / 立体视频
- 核心想法: 一个拍摄视角或一句话就能变成头显中的环绕场景，相当于文生视频的沉浸版。
- 内容: VideoPanda（NVIDIA 多伦多 AI 实验室，2025 年 4 月）可根据文字提示或一段普通视频生成 360° 视频：它生成各个方向上一致的视图并拼成全景，还能以自回归方式延长成更长的片段。
- 实现方式: 在视频扩散模型中加入多视角注意力层，在纯文字与单视角视频两种条件下联合训练，并对帧与视角随机下采样。
- 能力维度: 情境可达性, 感知真实感
- 论文: https://arxiv.org/abs/2504.11389 (arXiv 2025)
- 视频: https://research.nvidia.com/labs/toronto-ai/VideoPanda/assets_web/release_col_cond_comp/49545422/56_1_samplepanopost2x.mp4
- 图片: https://research.nvidia.com/labs/toronto-ai/VideoPanda/assets_web/comp_to_mvdiffusion/pano/11/pano_fix.png
- 项目主页: https://research.nvidia.com/labs/toronto-ai/VideoPanda/

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

#### VidPanos：从随手摇拍视频生成全景视频（VidPanos） — Jingwei Ma, 谷歌 DeepMind (2024-10-17)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 视频 → 输出: 360° / 立体视频
- 核心想法: 生成式补全填上了摄像机每一刻没有拍到的部分，是从一个拍摄角度走向环绕场景的一步。
- 内容: VidPanos（华盛顿大学与 Google DeepMind，SIGGRAPH Asia 2024）把随手拍的摇镜头视频变成同等长度的全景视频，就像用广角镜头拍摄一样：当前画面外的人和物体仍在运动，而不是像拼接的全景照片那样静止。
- 实现方式: 对全景时空体进行外扩补全：把预训练视频生成模型作为合成系统的一个组件，并绕开其有限的空间与时间上下文。
- 能力维度: 感知真实感, 情境可达性
- 论文: https://arxiv.org/abs/2410.13832 (SIGGRAPH Asia 2024)
- 视频: https://www.youtube.com/watch?v=93HHOnISoqk
- 图片: https://vidpanos.github.io/static/images/real_results/dynibar_thumb.jpg
- 项目主页: https://vidpanos.github.io/

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

#### FlowAct-R2：基于流式多模态参考与主动式智能体规划的交互数字人（FlowAct-R2） — 字节跳动 Seed (2026-09-28)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入: 文字提示, 语音与音频, 图像 → 输出: 虚拟人（脸 / 身体）, 语音 / 声音, 智能体行为与动作
- 核心想法: 让虚拟人从“回答问题”走向“主持一场互动”：人设、议程和可复用技能让生成的人在参与者两次行动之间也能把情境维持下去。
- 内容: FlowAct-R2 可连续数小时流式生成 720p 数字人：无人互动时它按自己的安排行动，观众发言时立即回应；它能在视频通话中聊天、手持并试穿商品进行直播带货、根据弹幕唱歌跳舞，也能处理打断。字节跳动报告称，在视频质量和实时互动的人类偏好评测中明显优于生数科技的 Vidu-S1。
- 实现方式: 一个流式多模态参考扩散 Transformer，由 Seedance 2.0 Mini 参考生视频模型改造而来，采用 diffusion forcing、与视频对齐的 RoPE 和部分加噪的历史帧；再由一个主动式智能体在离线阶段规划人设、议程与技能，在线时调度、打断和恢复各种行为。
- 参数: 720p · hour-level streams · GSB +54.76% video quality / +40.48% real-time interaction vs Vidu-S1 (developer-reported)
- 能力维度: 反应性, 行为似真性, 持久性
- 论文: https://arxiv.org/abs/2609.35728 (arXiv 2026)
- 视频: https://avatar-agent.tos-cn-beijing.volces.com/flowact-r2-project-clean-20260920/static/videos/entertainment_final_danmaku_only/chat4_faststart.mp4
- 项目主页: https://bone-11.github.io/Flowact-R2/

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

#### Muse Realtime Avatar — Meta (2026-09-23)
- 类型: 模型 · 时序: 回合制 · 获取方式: 产品 / 应用
- 输入: 语音与音频, 图像 → 输出: 虚拟人（脸 / 身体）, 语音 / 声音
- 核心想法: 语音和面孔由同一条语音 token 流生成，语气、口型和表情因此同步；任何一张图都能以消费级规模获得一个实时的身体。
- 内容: Muse Realtime Avatar 让 Meta 的 Muse 智能体在视频聊天中有了一张脸：只需一张参考图（照片、插画、动物甚至物件），它就能在 Muse Realtime Voice 说话时实时驱动角色的面部、双手和身体，对话持续多久就生成多久。Meta 称在两到三分钟的实时通话中，评测者更偏好它而不是 Runway Characters 和 HeyGen LiveAvatar；截至 2026 年 10 月，Muse 应用已开放视频聊天。
- 实现方式: 一个音频驱动的扩散 Transformer 读取 Muse Realtime Voice 的语音 token 流、参考素材和最近视频潜变量的滚动窗口，逐段生成短的因果视频块；40 步、三路 CFG 的教师模型通过 self-forcing 与分布匹配蒸馏成无引导的两步学生模型，以 4 比特量化和持久 KV 缓存部署，每一帧都嵌入 Video Seal 水印。
- 参数: 448×768 · 25 fps · ~870 ms from end of user turn to first byte · 2 NFE per chunk (from 120) · 12 sessions per GB200 (developer-reported)
- 能力维度: 时间响应性, 感知真实感, 持久性
- 视频: https://x.com/alexandr_wang/status/2102919552254484765
- 图片: https://research.meta.ai/articles/bringing-your-muse-to-life/images/muse-realtime-avatar-character-introduction-first-frame-v3.webp https://research.meta.ai/articles/bringing-your-muse-to-life/images/muse-realtime-avatar-streaming-architecture-v3.webp
- 项目主页: https://research.meta.ai/blog/bringing-your-muse-to-life

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

#### 开放虚拟人工具包（Virtual Human Toolkit，2026）（Open Virtual Human Toolkit (2026)） — 南加州大学创意技术研究所 (2026-07-23)
- 类型: 开源工具 · 时序: 回合制 · 获取方式: 开源权重 / 代码, 产品 / 应用
- 输入: 语音与音频, 视频 → 输出: 虚拟人（脸 / 身体）, 语音 / 声音, 对话 / 文本
- 核心想法: SimSensei 式虚拟人背后的研究传统被重新打造：实验室可通过一个下拉菜单更换大模型或声音，为敏感研究完全在本地运行，同时保持角色其余部分不变。
- 内容: USC ICT 的 Virtual Human Toolkit 于 2026 年开放发布：这是一个 Unity 项目，用于构建能看见、听见用户并以语音和非语言行为回应的对话式三维角色，可部署到网页、手机、桌面和 Quest。语音识别、大模型、语音合成、感知和非语言行为等每项能力都通过同一个 API 接入，可在 20 多家云端服务或完全本地的方案间切换；它获得 IVA 2026 最佳技术演示奖，可免费用于非商业用途。
- 实现方式: 模块化的 Unity 架构，为音视频感知（如 OpenFace、DeepFace）、语音识别（Whisper、Azure、OpenAI Realtime）、大模型（Claude、GPT、Gemini、Ollama、vLLM）、语音合成（ElevenLabs、Piper、Kokoro）、基于关键词或向量的知识检索，以及 Reallusion 角色上基于规则或模型的非语言行为提供统一的接入 API。
- 参数: 20+ providers · cloud or fully local · Web, iOS, Android, Windows, macOS, Linux, Quest
- 能力维度: 实验控制, 创作可及性, 情境可达性
- 获奖与认可: IVA 2026 Best Technical Demonstration
- 论文: https://doi.org/10.1145/3806774.3832327 (IVA 2026)
- 视频: https://www.youtube.com/watch?v=QU_ItB4p_zc
- 图片: https://vhtoolkitwww.ict.usc.edu/demo/VHToolkit_July2026.png
- 项目主页: https://vhtoolkit.ict.usc.edu
- 代码: https://github.com/USC-ICT/vhtoolkit

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

#### Moshi-Face：把面部生成接入全双工语音对话系统（Moshi-Face） — Jingjing Jiang (2026-06-20)
- 类型: 研究演示 · 时序: 全双工 · 获取方式: 仅限研究
- 输入: 语音与音频, 视频 → 输出: 语音 / 声音, 虚拟人（脸 / 身体）, 动作 / 动画
- 核心想法: 首个公开发表、在全双工对话中既看用户的脸又展示自己面部的模型：可视为 Tavus Griffin 的可检视学术对照。
- 内容: Moshi-Face 为全双工语音模型 Moshi 加上了一张脸：它在说话的同时接收用户的声音和面部动作，并同步生成自己的语音和三维面部动作，从而继承了 Moshi 话语重叠、附和与可被打断的能力，并配上了会动的脸。作者报告其在低延迟下实现了视听对齐，并保持了 Moshi 原有的对话质量。
- 实现方式: 先用 VQ-VAE 面部编解码器把视频中提取的三维头部网格编码成离散的面部 token，再在 Moshi 中加入一个 Face Transformer，与 Moshi 的音频 token 同步、非自回归地预测这些面部 token，并与用户的音频和面部输入流对齐。
- 能力维度: 时间响应性, 反应性
- 论文: https://arxiv.org/abs/2606.21970 (Interspeech 2026)
- 图片: https://arxiv.org/html/2606.21970v1/overall.png https://arxiv.org/html/2606.21970v1/sample.png
- 项目主页: https://arxiv.org/abs/2606.21970

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

#### Runway Characters — Runway (2026-03-09)
- 类型: 平台 / API · 时序: 回合制 · 获取方式: 公开 API, 产品 / 应用
- 输入: 语音与音频, 图像 → 输出: 虚拟人（脸 / 身体）, 语音 / 声音, 对话 / 文本
- 核心想法: 通用世界模型的虚拟人分支，让吉祥物、历史人物或风格化的对话伙伴都能接通视频通话；Meta 2026 年 9 月的评测认为它的举止与 Muse Realtime Avatar 不相上下。
- 内容: Runway Characters 是一个实时视频智能体 API：只需一张参考图、无需微调，就能创建一个对话角色（写实或风格化、人类或非人类），并可配置声音、性格、知识和工具动作；角色在倾听和说话时都会保持面部表情、视线和手势。2026-03-09 向所有 Runway 开发者客户开放，Runway 网页应用中也提供预设角色。
- 实现方式: 基于 Runway GWM-1 世界模型的 GWM Avatars 变体（2025 年 12 月），这是一个以参考图像和智能体语音为条件的自回归视频模型，通过实时 API 提供，并可配置大模型、声音和知识库。
- 能力维度: 创作可及性, 感知真实感, 行为似真性
- 视频: https://www.youtube.com/watch?v=kiwPrAjFGWo
- 图片: https://d3phaj0sisr2ct.cloudfront.net/site/images/news/characters-hero-og.png
- 项目主页: https://runway.com/news/introducing-runway-characters
- API 文档: https://docs.dev.runwayml.com/

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
- 内容: LiveAvatar 是 HeyGen 的实时虚拟人流式 API，接替了此前的 Interactive Avatar：一个由图像或两分钟视频克隆而来的半身或全身 1080p 虚拟人，通过 WebRTC 说出语音智能体的回复。HeyGen 称首帧中位时间低于 300 ms，大批量时约每分钟 0.01 美元。2026 年 6 月，HeyGen 推出用于全天候直播虚拟人的 Avatar Realtime API；2026-09-10，又以 MIT 协议开源了一套参考实现，由 OpenAI 的全双工语音模型 GPT-Live-1 驱动 LiveAvatar。
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

#### FaceGAN：无需蒸馏的单次前向实时说话头像（FaceGAN (No Distillation Needed)） — Yu Han, Meta (2026-10-08)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入: 语音与音频 → 输出: 虚拟人（脸 / 身体）, 动作 / 动画
- 核心想法: 质疑了“实时虚拟人就要蒸馏大型扩散模型”的默认做法：对面部动作而言，一个小型因果 GAN 可能就够了，这降低了在研究中使用及时回应面孔的成本。
- 内容: FaceGAN（Meta Reality Labs，2026-10-08）用流式音频驱动说话头像，每帧只需一次前向计算，随音频到来输出面部表情和头部姿态，再渲染成头像。作者报告，其生成质量与基于扩散模型的说话头像方法相当或更好，并能无限时长生成而不漂移。
- 实现方式: 一个因果、时不变的生成器把音频映射为表情和头部姿态；由于驱动噪声是合成的，可以提前采样噪声的“未来”并对其做非因果整形，从而突破 i.i.d. 噪声驱动的因果生成器在频谱上的限制，同时音频路径保持因果；有界注意力窗口保证长时间生成稳定。
- 参数: 1 network evaluation per frame · unbounded length (developer-reported)
- 能力维度: 时间响应性, 感知真实感
- 论文: https://arxiv.org/abs/2610.11070 (arXiv preprint)
- 视频: https://wojciechzielonka.com/assets/facegan-site/videos/combined/A285_C024.mp4
- 图片: https://wojciechzielonka.com/assets/img/facegan/postimg.jpg https://wojciechzielonka.com/assets/facegan-site/teaser.png
- 项目主页: https://wojciechzielonka.com/facegan/

#### PixReenact：像素条件因果视频扩散的流式头像重演（PixReenact） — Gavriel Habib (2026-10-04)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入: 图像, 视频 → 输出: 虚拟人（脸 / 身体）
- 核心想法: 实时重演让幕后的实验助手或演员即时操纵一张生成的面孔，这是实现可控虚拟对话者的一条“绿野仙踪”式路径。
- 内容: PixReenact（OriginAI 与英伟达，2026-10-04）用实时驱动视频流式地驱动一张参考人像，让一个人的表情和头部动作即时呈现在另一张脸上。作者报告，平均输出延迟约 240 毫秒，五分钟的连续视频流中身份保持稳定，极端转头和遮挡时也是如此。
- 实现方式: 因果视频扩散模型直接以参考帧和驱动帧的 VAE 潜变量为条件，不使用单独的身份或动作编码器；训练采用跨身份伪监督和长程自回放，再分别用冷启动和稳态两个教师蒸馏成 4 步滚动学生模型，每次更新输出 4 帧。
- 参数: 4 NFE · 4 frames per update · ~239 ms mean emission latency · 5-min identity test (developer-reported)
- 能力维度: 时间响应性, 持久性, 实验控制
- 论文: https://arxiv.org/abs/2610.05233 (arXiv preprint)
- 视频: https://gavriel-habib.github.io/pixreenact/static/videos/long_identity_5min.mp4
- 图片: https://gavriel-habib.github.io/pixreenact/static/images/teaser.jpg
- 项目主页: https://gavriel-habib.github.io/pixreenact/

#### Wan-Dancer：分钟级连贯的音乐驱动舞蹈视频生成（Wan-Dancer） — 阿里通义 (2026-07-13)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 语音与音频, 图像 → 输出: 虚拟人（脸 / 身体）, 平面视频
- 核心想法: 先对整首曲子规划关键帧，突破了音频驱动全身视频约 20 秒的时长限制，让生成的表演者能完整演完一首歌而不出现身份或动作漂移。
- 内容: Wan-Dancer（阿里巴巴通义实验室，2026-07-13）根据整首音乐，让参考图中的人物跳舞并生成视频，动作跟随音乐的节奏与结构，覆盖中国古典舞、K-pop、街舞、踢踏舞、拉丁舞等风格，还支持换装和基于关键帧的动作控制。通义称其可稳定生成超过一分钟的 720p、30 fps 视频（项目页展示了 2 分 36 秒的样例）；14B 权重和推理代码以 Apache-2.0 协议开源，Hugging Face 和魔搭上有在线演示。
- 实现方式: 基于 Wan 的分层图生视频扩散管线：全局阶段根据整首音乐规划关键帧，局部阶段细化关键帧之间的动作；通过时间映射 RoPE 适配动态帧率，用光流损失增强动作连续性，并用动作速度控制保留快速动作中的细节。
- 参数: 720p · 30 fps · >1 min per video (up to 2 min 36 s shown) · 14B parameters
- 能力维度: 持久性, 感知真实感, 情境多样性
- 论文: https://arxiv.org/abs/2607.09581 (arXiv preprint)
- 视频: https://cloud.video.taobao.com/vod/tHYQgRwFmx0A4CV0q2Kr6aDEKBe2L_baKNTlkdCgGv0.mp4
- 项目主页: https://humanaigc.github.io/wan-dancer-project/
- 代码: https://github.com/Wan-Video/Wan-Dancer

#### LongCat-Video-Avatar 1.5 — 美团 (2026-05)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 语音与音频, 图像, 文字提示 → 输出: 虚拟人（脸 / 身体）, 平面视频
- 核心想法: 一个可固定版本的开源多人说话场景模型，让实验室可以离线渲染多名虚拟人之间的脚本对话，并保留确切的模型版本。
- 内容: LongCat-Video-Avatar 1.5 是美团以 MIT 协议开源的音频驱动说话视频模型：根据语音和文字提示（可选参考图），生成稳定的长时 480p 或 720p 视频，人物可以是一人或多人，能说话、唱歌或拿取物品，也支持动漫和动物角色，还能续写已有视频。它是 LongCat-Video-Avatar 1.0（2025 年 12 月）的升级版。
- 实现方式: 在 LongCat-Video 基础模型上微调，支持音频+文本生视频、音频+文本+图像生视频以及视频续写，可输入单路或多路音频；美团同时发布了一个人类评测基准：6 类场景共 508 组图像-音频样本，由 770 名众包评测者打分。
- 参数: 480p / 720p · single- or multi-person · MIT licence
- 能力维度: 感知真实感, 持久性, 情境多样性
- 视频: https://meigen-ai.github.io/LongCat-Video-Avatar-1.5-Page/videos/teaser/teaser.mp4
- 项目主页: https://meigen-ai.github.io/LongCat-Video-Avatar-1.5-Page/
- 代码: https://huggingface.co/meituan-longcat/LongCat-Video-Avatar-1.5

#### Archon：面向完整数字人生成的统一多模态模型（Archon） — Chong Bao, 谷歌 (2026-05-28)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 文字提示, 语音与音频, 视频 → 输出: 虚拟人（脸 / 身体）, 语音 / 声音, 对话 / 文本
- 核心想法: 当描述、台词、声音、动作和画面都在同一个模型里，虚拟人只需设定一次，就能在实验要改变的那个通道中修改。
- 内容: Archon 用一个模型完成整个数字人：根据一段文字描述，它可以写出角色台词、念出来、驱动面部和身体动画，并渲染出说话视频；也能以其中任一模态为输入，生成或编辑其余模态（例如改写台词而保留表演）。它在七种同步模态上的 72 项任务中训练。
- 实现方式: 一个原生自回归多模态模型，为描述、台词、语音、动画（身份、表情、姿态）、语义视频、图像和 RGB 视频分别配备分词器；用语义视频重参数化把视频 token 减少 4 倍，配合语义驱动的视频扩散解码器，并以“模态内思考”链处理含糊的跨模态任务。
- 参数: 7 modalities · 72 pre-training tasks · 4× video-token reduction
- 能力维度: 创作可及性, 实验控制, 持久性
- 论文: https://arxiv.org/abs/2605.30311 (CVPR 2026)
- 视频: https://www.youtube.com/watch?v=9h2_L9E2KjE
- 图片: https://zju3dv.github.io/archon/static/framework_cropped.jpg
- 项目主页: https://zju3dv.github.io/archon/

#### Avatar V — HeyGen (2026-04-08)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 产品 / 应用, 公开 API
- 输入: 视频, 文字提示 → 输出: 虚拟人（脸 / 身体）, 平面视频, 语音 / 声音
- 核心想法: 把一个人录下的表演与外观分离，一段短录像就能生成同一身份的多种造型，便于制作受控的讲者变体，也带来冒充风险。
- 内容: Avatar V 是 HeyGen 接替 Avatar IV 的虚拟人模型：只需一段 15 秒的手机录像，就能生成一个人的数字分身，用 177 种以上语言和方言念出任意脚本，并在不同机位、更换服装与场景以及长视频中保持面孔一致。自 2026 年 6 月起，可在网页端和 API 中一次生成长达 30 分钟的连续讲话视频。
- 实现方式: 专有的视频扩散虚拟人模型，用多角度和长时长素材训练，从参考片段建立身份表征，再以流式推理生成新造型和长镜头；HeyGen 未公开架构。
- 参数: 15 s reference clip · up to 30 min continuous video (since June 2026) · 177+ languages and dialects (developer-reported)
- 能力维度: 感知真实感, 持久性, 创作可及性
- 视频: https://www.youtube.com/watch?v=OGbsSuHLuMc
- 图片: https://cdn.sanity.io/images/pdhqcmb1/production/2f2a72c9868deb43e26d3ef8a98f7af938632fa4-5760x3240.png?fit=max&fm=png
- 项目主页: https://www.heygen.com/blog/announcing-avatar-v
- API 文档: https://developers.heygen.com/

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

#### MoCha：迈向电影级说话角色生成（MoCha） — Cong Wei, Meta (2025-03-30)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 语音与音频, 文字提示 → 输出: 虚拟人（脸 / 身体）, 平面视频
- 核心想法: 生成的是社交场景，而不只是说话的人：两个生成的人物你来我往地对话，正是行为研究中剧本化情景片段的素材。
- 内容: MoCha 直接根据语音和文本提示生成电影风格的“说话角色”：不仅是脸，而是画面中的整个角色，包括手势和动作；借助结构化提示，它还能跨镜头编排两个或更多角色之间的轮流对话。
- 实现方式: 一个扩散 Transformer 视频模型，用语音-视频窗口注意力对齐语音与视频 token，在带语音标注和带文本标注的视频上联合训练，并用带角色标签的提示模板实现多角色对话。
- 能力维度: 感知真实感, 行为似真性, 情境多样性
- 论文: https://arxiv.org/abs/2503.23307 (arXiv 2025)
- 视频: https://congwei1230.github.io/MoCha/assets/2p/2p_2clip_2talk/2p_2clip_2talk_woman_man_street_2.mp4
- 项目主页: https://congwei1230.github.io/MoCha/

#### Character-3 — Hedra (2025-03-12)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 产品 / 应用, 公开 API
- 输入: 图像, 语音与音频, 文字提示 → 输出: 虚拟人（脸 / 身体）, 平面视频
- 核心想法: 让音频驱动的角色视频成为大规模使用的创作工具，也适用于非人类和风格化角色。
- 内容: Character-3 能把任意角色图像（照片、插画、三维渲染）根据音频和设定情绪与肢体动作的文本提示，变成说话或唱歌的视频，在 Hedra Studio 应用中使用。2026 年 2 月，Hedra 推出后继模型 Omnia，可从单张图像控制镜头、身体动作和背景，同时推出可一次生成最长五分钟视频的 Avatar 模型，两者均可通过 API 使用。
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

#### Hologram 全息人像（Meta Ray-Ban Display / Meta VR Glasses）（Hologram (Meta Ray-Ban Display / Meta VR Glasses)） — Meta (2026-09-23)
- 类型: 产品 / 应用 · 时序: 实时流式 · 获取方式: 候补 / 抢先体验
- 输入: 语音与音频, 视频 → 输出: 虚拟人（脸 / 身体）
- 核心想法: 即使没有摄像头对着自己的脸，佩戴者仍能“面对面”出现，因为面孔是从语音推断出来的：对方看到的表情是生成的，而不是拍到的。
- 内容: Hologram 是在眼镜上打视频电话时使用的照片级实时人脸：用手机做一次简短的自我采集后，通话对方就能看到你的脸和表情；Meta 称在 Meta Ray-Ban Display 上它完全由你的声音驱动。该功能于 2026-09-23 的 Connect 大会发布，2026 年秋季起在美国通过 WhatsApp 向 Ray-Ban Display 用户抢先开放，并将在 2027 年春季随 Meta VR Glasses 推出。
- 实现方式: 先在 Meta AI 应用中用手机做简短自我采集，建立个人面部模型；再由 hologram 模型根据说话内容和语气推断表情。Meta 尚未公开架构，可能与其 Codec Avatars 研究相关。
- 能力维度: 感知真实感, 时间响应性
- 视频: https://about.fb.com/wp-content/uploads/2026/09/02_Hologram.mp4
- 图片: https://about.fb.com/wp-content/uploads/2026/09/New-Features-for-Meta-Ray-Ban-Display_Header.jpg?w=1200
- 项目主页: https://about.fb.com/news/2026/09/new-features-for-meta-ray-ban-display-navigation-hologram/

#### FiCA：从单张人像前馈即时生成高斯 Codec Avatars（FiCA） — Kim Youwang, Meta (2026-06-23)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入: 图像, 身体、面部与视线追踪 → 输出: 虚拟人（脸 / 身体）, 高斯泼溅 / 辐射场
- 核心想法: 一张自拍在几秒内变成 Codec Avatar 级别的三维头部，把特定面孔放进 XR 场景的成本降到接近于零。
- 内容: FiCA（前馈即时高斯 Codec Avatars）只需一张随手拍的人像照片，约五秒即可生成照片级、可驱动的三维高斯头部化身，随后可实时驱动出新的表情，无需针对每个人做优化。
- 实现方式: 先用微调的 Sapiens 模型把照片展开为不完整的 UV 纹理、法线和几何图，再由 UV 空间扩散模型补全，前馈细化网络增强身份特征，最后由通用 Codec Avatar 先验把网格解码成三维高斯。
- 参数: single image · ~5 s per avatar · real-time animation
- 能力维度: 感知真实感, 创作可及性
- 论文: https://arxiv.org/abs/2606.24232 (arXiv 2026)
- 视频: https://www.youtube.com/watch?v=oIW3ZooWaQw
- 项目主页: https://youwangk.github.io/FiCA.html

#### HumanNOVA：由单张图像快速生成照片级三维人体化身（HumanNOVA） — Hezhen Hu (2026-06-01)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像 → 输出: 虚拟人（脸 / 身体）
- 核心想法: 一秒内把一张照片变成全身三维人物，使按参与者或实验助手定制化身的成本低到可以每次实验都做。
- 内容: HumanNOVA（得克萨斯大学奥斯汀分校，CVPR 2026 Highlight）能在一秒内由一张照片生成一个人的照片级全身三维化身，无需针对每个人做优化。它的训练数据是 10 万个化身，来自给已绑定骨骼的资产摆出大量姿态，以及对多机位拍摄重新拟合；代码和 Colab 演示已公开。
- 实现方式: 把图像和估计出的 SMPL 人体网格编码为紧凑的 token，通过交叉注意力在一次前馈中融合成三平面（triplane）化身；训练集通过给绑定资产套用日常姿态、以及对多机位拍摄做拟合补充视角，扩充到 10 万个资产。
- 参数: <1 s per avatar · single image · 100k training assets
- 能力维度: 创作可及性, 感知真实感
- 获奖与认可: CVPR 2026 Highlight
- 论文: https://arxiv.org/abs/2606.02573 (CVPR 2026 (Highlight))
- 视频: https://www.youtube.com/watch?v=pslYhxFiALE
- 项目主页: https://humannova.github.io
- 代码: https://github.com/HumanNOVA/HumanNOVA

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
- 内容: Audio2Face-3D 可根据语音音频实时为绑定好的三维角色生成唇形同步和面部表情；NVIDIA 于 2025 年 9 月开源了模型、SDK 和训练框架，并提供 Unreal Engine 与 Maya 插件。Audio2Face-3D 微服务 2.0 版（2026 年 3 月）新增基于扩散的 Multi v3.2 模型和可选的舌部 blendshape。
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

#### LHM：数秒内从单张图像重建可动画人体（LHM） — 阿里通义 (2025-03-13)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像, 视频 → 输出: 虚拟人（脸 / 身体）, 高斯泼溅 / 辐射场
- 核心想法: 任何被拍下的人，包括特定的实验助手或参与者本人，都能在几秒内成为场景中的全身三维角色。
- 内容: LHM（大型可动画人体重建模型）能在几秒内把一张全身照片变成可驱动的三维高斯化身，保留服装和面部细节，并可用从视频中提取的动作来驱动。其后继版本 LHM++ 于 2026 年 3 月开源，支持任意数量的视角输入，8 视角输入只需 8 GB 显存。
- 实现方式: 多模态 Transformer 用注意力编码人体位置特征和图像特征，并加入头部特征金字塔以保留面部身份，一次前馈即可预测标准姿态下的三维高斯，再通过基于 SMPL-X 的蒙皮驱动。
- 参数: single image → animatable 3D Gaussian human in seconds · LHM++ (open-sourced 2026-03): any-view input, 8 views on 8 GB GPU
- 能力维度: 创作可及性, 感知真实感
- 论文: https://arxiv.org/abs/2503.10625 (arXiv 2025)
- 视频: https://www.youtube.com/watch?v=tivEpz_yiEo
- 项目主页: https://aigc3d.github.io/projects/LHM/
- 代码: https://github.com/aigc3d/LHM

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
- 内容: MetaHuman Creator 让任何人通过混合扫描人脸并调整皮肤、头发和体型，在几分钟内设计出逼真且完整绑定的数字人，可直接在 Unreal Engine 中驱动；自 Unreal Engine 5.6（2025）起，它在引擎内运行并接受网格或扫描输入。MetaHuman 5.8（2026 年 6 月）可把任意拓扑的全身网格转换为 MetaHuman，支持数百到数千个实时角色的人群，并以 MIT 协议开源 RigLogic 与 DNA 库（OpenRigLogic）。
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

#### ELLSA 2：语音、表情与手势的全双工交互（ELLSA 2） — Siyin Wang, 字节跳动 Seed (2026-10-15)
- 类型: 研究演示 · 时序: 全双工 · 获取方式: 开源权重 / 代码, 仅限研究
- 输入: 语音与音频 → 输出: 语音 / 声音, 动作 / 动画, 对话 / 文本
- 核心想法: 让倾听行为与语音共用同一条全双工时钟，角色在决定接话之前就能用身体对参与者正在说的话作出反应。
- 内容: ELLSA 2 是一个端到端全双工对话模型，能同时听和说，并为三维角色流式生成上半身手势、手部动作和面部表情，包括在不说话时点头、微笑，以及根据对话内容选择有意义的手势。评测采用人工核验的测试集，涵盖附和、话语重叠与打断；截至 2026 年 10 月，已以 Apache 2.0 协议发布数据处理流程、评测代码、测试集和独立的流式手势-表情生成器，完整的联合模型尚未发布。
- 实现方式: 一个属于 SALMONN-omni 系列的全双工语音对话主干，将分开的倾听与说话隐藏状态以及双方的预训练声学特征输入一个自回归分块合成器，每 0.8 秒输出 SMPL-H 上半身、手部、FLAME 表情和口型编码；上下文语义调用与模板引导分别决定何时以及如何做出语义手势，训练数据整理自 Seamless Interaction。
- 参数: gesture/expression codes every 0.8 s · test set 138 clips (67 full-duplex, 71 semantic) · Apache 2.0
- 能力维度: 行为似真性, 时间响应性, 反应性
- 论文: https://arxiv.org/abs/2610.21452 (arXiv 2026)
- 图片: https://raw.githubusercontent.com/bytedance/SALMONN/ELLSA2/code/assets/paper/architecture.png https://arxiv.org/html/2610.21452v1/seg_1.png
- 项目主页: https://github.com/bytedance/SALMONN/tree/ELLSA2
- 代码: https://huggingface.co/tsinghua-ee/ELLSA2

#### GLARE：生成做出恰当反应的倾听头像（GLARE） — Zikai Liao (2026-09-30)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 语音与音频, 图像 → 输出: 虚拟人（脸 / 身体）
- 核心想法: 把倾听行为看作带有时间点的离散、可标注反应，这正是行为编码本来就采用的形式。
- 内容: GLARE 在两人对话中生成倾听者的面部，并决定何时、以何种方式反应：点头、摇头、微笑、大笑、皱眉或表现惊讶。它附带约 147 小时的说话者-倾听者配对视频，含 64,557 条事件级反应标注，以及衡量反应是否恰当（而不只是画面是否逼真）的指标。
- 实现方式: 一个流匹配 Transformer 根据说话者音频驱动参考人像，以 Qwen2-Audio 提取的韵律特征为条件，并在从 RealTalk 与 Seamless Interaction 整理出的片段上用时序反应损失训练。
- 参数: ~147 h paired speaker-listener video · 64,557 reaction annotations · 6 reaction types
- 能力维度: 行为似真性, 反应性, 实验控制
- 论文: https://arxiv.org/abs/2609.40317 (NeurIPS 2026)
- 图片: https://raw.githubusercontent.com/lzk901372/glare/main/overview.png
- 项目主页: https://github.com/lzk901372/glare
- 代码: https://github.com/lzk901372/glare

#### Motion-Omni：端到端联合生成语音与全身动作的语音对话模型（Motion-Omni） — Chengqian Ma (2026-08-28)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 开源权重 / 代码
- 输入: 语音与音频 → 输出: 语音 / 声音, 动作 / 动画, 对话 / 文本
- 核心想法: 当肢体语言出自选择措辞的同一个模型，手势就能表达级联系统无从得知的信息，例如对它自己决定强调的词加以强调。
- 内容: Motion-Omni 是一个语音对话模型：对口头提问，它在用语音作答的同时，从同一组隐藏状态直接生成面部表情以及手部、上半身和下半身动作，因此三维角色的手势与说话内容一同产生，而不是在语音生成完后再由另一个模型补上。模型代码、训练方案和数据已开源；截至 2026 年 10 月，权重仍在准备中。
- 实现方式: 一个基于大语言模型的语音对话模型，语音生成器和动作生成器读取同一组隐藏状态，在语音与动作两个目标上联合训练；作者发现若冻结语音通路，动作就会与语音错位。
- 能力维度: 行为似真性, 时间响应性
- 论文: https://arxiv.org/abs/2609.04250 (arXiv 2026)
- 视频: https://step-out.github.io/Motion-Omni-Page/videos/demo1_feedback_to_interns.mp4
- 图片: https://step-out.github.io/Motion-Omni-Page/assets/architecture.png
- 项目主页: https://step-out.github.io/Motion-Omni-Page/
- 代码: https://github.com/step-out/Motion-Omni

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

#### 倾听重要吗？AI 分身中的附和与点头（Does Listening Matter? Backchanneling and Nodding in an AI Clone） — Koji Inoue (2026-08-20)
- 类型: 行为研究 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 语音与音频 → 输出: 虚拟人（脸 / 身体）, 语音 / 声音, 动作 / 动画
- 核心想法: 证据表明，分身的逼真度也包括它如何倾听：即使声音和内容不变，附和与点头也会改变人们感受到的临场感。
- 内容: 京都大学与 Sony CSL 的一项被试内研究（N=35）：参与者与一位真实研究者的 AI 分身（克隆声音、大模型回复）交谈，对比在其说话时有无实时预测的语言附和与点头。加入倾听行为后，分身被评为更专注、更像在与真人交谈，共在感也更强。
- 实现方式: 采用 AB/BA 平衡的被试内设计，比较有无倾听行为的 AI 分身；倾听行为由基于 Voice Activity Projection 的实时模型驱动，预测附和时机以及点头的时机和运动参数（Kato 等，ICMI 2026）。
- 参数: N=35 · within-subjects
- 能力维度: 行为似真性, 时间响应性
- 论文: https://arxiv.org/abs/2608.19527 (ICMI 2026 (Late-Breaking Results))
- 图片: https://arxiv.org/html/2608.19527v1/interface-crop.png https://arxiv.org/html/2608.19527v1/system-crop.png
- 项目主页: https://arxiv.org/abs/2608.19527
- 代码: https://github.com/MaAI-Kyoto/MaAI

#### STEER：可调控的双人对话头部化身（STEER） — Kartik Teotia (2026-07-26)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 语音与音频, 身体、面部与视线追踪, 文字提示 → 输出: 虚拟人（脸 / 身体）, 动作 / 动画
- 核心想法: 视线和点头成为实验者可以设定和记录的自变量，而不是音频的副产品。
- 内容: STEER 在两人对话中驱动一个三维头部化身，并让使用者调控它如何倾听和反应：注视或回避目光、头部动作的节奏以及情绪都是可同时编辑的显式控制量；它还提供可与真人实时对话的交互界面。
- 实现方式: 一个因果流匹配动作先验，根据对方的动作与音频以及目标人物自己的音频，生成目标人物 61 维 FLAME 状态（表情、下颌、颈部、眼球转动、眼睑）；视线、头部节奏和情绪控制量来自双人对话语料，由新的追踪与标注流程逐帧标注；推理代码已开源。
- 能力维度: 实验控制, 行为似真性, 反应性
- 论文: https://arxiv.org/abs/2607.23840 (SIGGRAPH Asia 2026)
- 视频: https://kartik-teotia.github.io/STEER/assets/videos/hero-control-with-input.mp4
- 图片: https://kartik-teotia.github.io/STEER/assets/images/og.png
- 项目主页: https://kartik-teotia.github.io/STEER/
- 代码: https://github.com/Kartik-Teotia/STEER

#### DyaPlex：面向双人互动的全双工语音-动作模型（DyaPlex） — Koki Nagano, 英伟达 (2026-06-02)
- 类型: 研究演示 · 时序: 全双工 · 获取方式: 仅限研究
- 输入: 语音与音频, 身体、面部与视线追踪 → 输出: 语音 / 声音, 动作 / 动画
- 核心想法: 语音、倾听行为和手势出自同一个能感知对方身体的全双工模型，虚拟对话者因此能在参与者还在说话时点头或模仿其动作。
- 内容: DyaPlex（英伟达与香港科技大学，NeurIPS 2026）是一个流式模型，在听和看对方的同时说话和做动作：它根据对方的语音和身体动作生成智能体自己的语音和身体动作，包括点头之类的视觉回应信号和手势模仿。英伟达展示了用它驱动虚拟智能体和机器人，以及生成合成的双人对话数据。
- 实现方式: 双塔 Transformer 保留一个冻结的全双工语音模型（PersonaPlex，可重叠说话并发出回应信号），再加上一个可训练的因果动作塔，对双方的 RVQ-VAE 动作 token 建模；通过双人 token 交织和时间对齐的语音-动作 RoPE 与语音对齐；在 Meta 的 Seamless Interaction 数据集（4000 小时）上训练。
- 参数: 4,000 h of dyadic training data · streaming, causal · speech + body motion
- 能力维度: 时间响应性, 行为似真性, 反应性
- 论文: https://arxiv.org/abs/2606.03874 (NeurIPS 2026)
- 视频: https://www.youtube.com/watch?v=Ls9l6daowyE
- 项目主页: https://research.nvidia.com/labs/amri/projects/DyaPlex/

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

#### EmbodiedHead：面向对话智能体的实时倾听与说话头像（EmbodiedHead） — Yu Zhang (2026-04-19)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入: 语音与音频, 图像 → 输出: 虚拟人（脸 / 身体）
- 核心想法: “正在倾听”是脸部必须显式表达的状态；否则虚拟人要么跟着用户的话动嘴，要么在对方说话时僵住。
- 内容: EmbodiedHead 为大模型语音智能体提供一个既会说也会听的实时头部虚拟人：用户说话时它闭着嘴做出反应，大模型回复时它对口型说话；两种状态在单路音频流中切换，不需要预知对方接下来会说什么。
- 实现方式: 一个最少四步采样的整流流扩散 Transformer，以参考图、动作幅度和逐帧的倾听/说话状态为条件生成人脸模型系数；流式音频调度器合并用户与大模型的音频作为输入，再由可微渲染器生成画面。
- 能力维度: 时间响应性, 行为似真性
- 论文: https://arxiv.org/abs/2604.17211 (ECCV 2026)
- 视频: https://www.youtube.com/watch?v=rHMcwFDAh-Y
- 项目主页: https://vpx-ecnu.github.io/EmbodiedHead-Website/

#### AgentHands：为 XR 中空间锚定的智能体对话生成交互式手势（AgentHands） — Ziyi Liu, 谷歌, Ruofei Du (2026-04-13)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 语音与音频, 透视画面与实时环境, 身体、面部与视线追踪 → 输出: 动作 / 动画, 语音 / 声音, 对话 / 文本
- 核心想法: 非语言行为可以锚定在参与者所处的真实房间里：智能体说“这个”的那一刻，手势正好落在实物上。
- 内容: AgentHands 是 Google XR 的研究原型：头显中的语音智能体获得一双虚拟手，能随着话语指向、描摹和演示用户身边的真实物体（例如勾勒兰花的气生根，或在高温的 3D 打印机喷嘴上加一道警示光晕）。在一项被试内研究（N=12）中，与台词相同的纯语音条件相比，参与者明显更容易找到所指物体、理解方向和需要做的动作。
- 实现方式: 先借助眼动和场景重建把物体登记为三维包围盒；大模型在回复中插入与触发词绑定的 GestureEvent（惯用手、手势、空间性、时间动态、交互性、视觉效果），头显端解析器依据语音合成的逐词时间戳，从手势库中同步播放这些手部动作。系统设计基于一项面向 XR 与手势专家的形成性研究。
- 参数: N=12 within-subjects · 2 tasks (orchid care, 3D printer) · 6-dimension gesture taxonomy
- 能力维度: 情境可达性, 行为似真性, 反应性
- 论文: https://doi.org/10.1145/3772318.3790938 (CHI 2026)
- 视频: https://storage.googleapis.com/gweb-research2023-media/media/AgentHands1_Demo.mp4
- 图片: https://storage.googleapis.com/gweb-research2023-media/images/HO_previewImage1.width-800.format-jpeg.jpg
- 项目主页: https://research.google/blog/agenthands-generating-interactive-hand-gestures-for-spatially-grounded-agent-conversations-in-xr/

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

#### Grok Voice 3.0 — xAI (SpaceXSI) (2026-10-14)
- 类型: 模型 · 时序: 回合制 · 获取方式: 公开 API, 产品 / 应用
- 输入: 语音与音频 → 输出: 语音 / 声音, 对话 / 文本
- 核心想法: 语音智能体的排名如今同时考察推理、任务完成与轮流发言，而目前的领先者是为解决客服来电而调校的，并非陪伴型产品。
- 内容: xAI 的第三代语音到语音模型，在 Voice Agent API 中按每分钟 0.08 美元提供，已用于特斯拉汽车、Grok Bot 的语音模式和 Starlink 客服热线。xAI 引用 Artificial Analysis 2026 年 10 月 13 日的结果：它在 Speech-to-Speech Index 上排名第一（86.9 分，高于 GPT-Live-1 与 Gemini 3.8 Live），在 Full Duplex Bench 上得分 97%。
- 实现方式: 原生语音到语音模型（架构未公开）；grok-voice-latest 已自动切换到该模型。目前没有公开证据表明它会在用户说话时发出附和，因此按回合制归类。
- 参数: $0.08/min · <1 s latency (developer claim) · AA Speech-to-Speech Index 86.9
- 能力维度: 时间响应性, 反应性
- 图片: https://media.x.ai/v1/website/og-grok-voice-3-0-b281361b.webp
- 项目主页: https://x.ai/news/grok-voice-3

#### D2：由半双工主干构建高能力全双工口语模型（D2 (Dialogue-to-Duplex)） — Cheng-Kuang Chang (2026-10-12)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 语音与音频 → 输出: 语音 / 声音
- 核心想法: 通过给现有主干模型补上双工时序、而不是从头训练双工模型，缩小了“能力强”与“对话流畅”之间的取舍。
- 内容: D2（麻省理工学院 CSAIL 与 MIT-IBM Watson AI Lab，2026-10-12）把能力较强的回合制口语语言模型 Qwen3-Omni 和 LLaMA-Omni 2 转换为边说边听的模型：用户说完时回答，被打断时让出话轮，同时保留大部分问答能力。作者报告 Qwen3-Omni-D2 的轮次交接成功率为 99.2%（521 毫秒），打断处理成功率为 99.5%（403 毫秒）；它不发出回应信号，因此这里归为回合制。
- 实现方式: 先在不需要转写的情况下，把冻结的离线语音编码器蒸馏成块内双向、块间因果的流式编码器；再用对齐的用户与助手音频、延迟的自身音频反馈，以及表示开始和停止的显式控制 token 微调主干，块长 80–160 毫秒。
- 参数: 12.5 Hz updates · 80 ms chunks · VoiceBench 70.1 · turn-taking 99.2% at 521 ms · interruption 99.5% at 403 ms (developer-reported)
- 能力维度: 时间响应性
- 论文: https://arxiv.org/abs/2610.17124 (arXiv preprint)
- 视频: https://d2-duplex-demo.github.io/assets/video/interruption.mp4
- 项目主页: https://d2-duplex-demo.github.io/

#### Gemini 3.8 Live — 谷歌 DeepMind (2026-09-15)
- 类型: 模型 · 时序: 回合制 · 获取方式: 公开 API
- 输入: 语音与音频, 视频, 文字提示 → 输出: 语音 / 声音, 对话 / 文本
- 核心想法: 说话时在后台推理，缩小了“反应快”和“想得深”之间的差距，适合需要一边保持回应、一边处理复杂情境逻辑的角色。
- 内容: 两款用于 Live API 的音频到音频模型，自 2026 年 9 月 15 日起正式可用：Gemini 3.8 Live 面向低延迟对话，Gemini 3.8 Live Extended Thinking 能在对话进行中于后台推理。谷歌重点介绍了异步函数调用与主动音频，即智能体只在相关时才开口。
- 实现方式: 音频到音频的 Gemini 模型，支持交错推理与默认异步函数调用，接替 2026 年 3 月的 gemini-3.1-flash-live-preview。
- 参数: audio $0.005/min in · $0.018/min out (paid tier)
- 能力维度: 时间响应性, 反应性
- 视频: https://storage.googleapis.com/gdm-deepmind-com-prod-public/media/SeC1i4kt5pDKGMWX/gemini-audio__demo__multi-tasking.webm
- 项目主页: https://deepmind.google/models/gemini-audio/
- API 文档: https://ai.google.dev/gemini-api/docs/live

#### Realtime-Venus — 蚂蚁集团 (2026-09-12)
- 类型: 模型 · 时序: 回合制 · 获取方式: 开源权重 / 代码
- 输入: 语音与音频, 视频 → 输出: 语音 / 声音, 对话 / 文本
- 核心想法: 把语音智能体拆成快速的对话前端和较慢的后台委托执行，让虚拟对话者在查资料或推理时仍能及时回应。
- 内容: Realtime-Venus（蚂蚁集团与清华大学，2026-09-12）是两个开源的 9B 对话模型，一个处理语音，一个处理语音加摄像头视频。它们边说边听：用户说“嗯嗯”时继续讲，用户真正打断时停下，能对微波炉提示音之类的声音和画面作出反应，还能把查航班这类较长的任务交给后台智能体，同时对话照常进行。它在倾听时不会主动发出回应信号，因此这里归为回合制；权重和 Android 测试版应用均已公开。
- 实现方式: 两个前端都基于开源的 MiniCPM-o 4.5（9B），在同一条因果时间线上预测交互控制 token、回复文本和委托请求，并用合成的双工、主动发言和任务委托场景做后训练；独立的 Harness 执行委托任务并准备好回复，由前端决定何时说出。
- 参数: 2 × 9B (Omni: audio + video; Audio) · Full-Duplex-Bench v1.5: 75% interruption response, 97% continuation under user backchannels (developer-reported)
- 能力维度: 时间响应性, 反应性
- 论文: https://arxiv.org/abs/2609.13814 (Technical report (arXiv))
- 视频: https://realtime-venus.github.io/assets/demos/microwave.mp4
- 图片: https://realtime-venus.github.io/assets/system-overview.png
- 项目主页: https://realtime-venus.github.io/
- 代码: https://github.com/inclusionAI/Realtime-Venus

#### 阶跃星辰 StepAudio 3 Realtime（StepAudio 3 Realtime） — 阶跃星辰 (2026-09-12)
- 类型: 模型 · 时序: 回合制 · 获取方式: 公开 API, 产品 / 应用
- 输入: 语音与音频 → 输出: 语音 / 声音, 对话 / 文本
- 核心想法: 从双方两路音频中学到的话轮管理，让语音角色能分辨对方是在附和还是在纠正；不过报告没有展示它自己发出附和。
- 内容: 阶跃星辰 2026 年的语音对话模型，围绕“听—说—想—做”的循环构建：听者说“对”“嗯”时它会继续讲，真正被打断时让出话轮，边说边在后台私下推理，并在后台调用工具。阶跃星辰报告其在 Artificial Analysis 的 Full Duplex Bench 上排名第一（总分 98.9）；通过阶跃 Realtime API 和 Voice Studio 提供。
- 实现方式: 混合专家音频语言模型（总参数约 1960 亿、激活 110 亿），以 Step 3.7 Flash 为主干，采用 Qwen3-Omni 的 AuT 音频编码器，用户与模型音频作为两路同步流，并支持边说边想。报告描述了如何处理用户的附和，但没有描述模型自己发出附和，因此按回合制归类。
- 参数: ~196B MoE (11B active) · AA Full Duplex Bench 98.9 (developer-reported)
- 能力维度: 时间响应性, 反应性, 行为似真性
- 论文: https://arxiv.org/abs/2609.14005 (Technical report)
- 视频: https://stepaudiollm.github.io/step-audio-3-realtime/assets/hero.mp4?v=37c74f6a
- 图片: https://arxiv.org/html/2609.14005v3/stepaudio3-realtime-main-results.png
- 项目主页: https://stepaudiollm.github.io/step-audio-3-realtime/
- API 文档: https://platform.stepfun.ai/docs/en/guides/models/stepaudio-3-realtime

#### Gander：多模态双工交互智能体（Gander (Multimodal Duplex Interaction Agent)） — 腾讯混元 (2026-09-08)
- 类型: 模型 · 时序: 回合制 · 获取方式: 开源权重 / 代码
- 输入: 语音与音频, 视频, 文字提示 → 输出: 语音 / 声音, 对话 / 文本
- 核心想法: 与 Realtime-Venus 类似，快速的“小脑”负责对话节奏，较慢的“大脑”负责干活；这种模式让虚拟人在执行长任务时仍能保持社交上的及时回应。
- 内容: Gander（腾讯混元语音团队与浙江大学、上海交通大学，2026-09-08）是一个开源的音视频对话智能体，边说边听：用户简短附和时继续讲，用户明确要求停下时暂停，画面中出现相关内容时主动提醒，还能在对话进行的同时在后台完成编程或工具任务。模型权重、代码和训练数据均已发布；它在倾听时不会主动发出回应信号，因此这里归为回合制。
- 实现方式: 基于 MiniCPM-o 4.5 的流式 Thinker–Talker“小脑”把用户输入和模型输出按块展平为一条 token 流（每块 1 秒，上下文 128 块），通过工具调用与“大脑”智能体协作；训练语料约 270 万条，涵盖语音、音视频、智能体和抗干扰场景。
- 参数: 1 s streaming chunks · 128-chunk context · ~2.7M training samples · MiniCPM-o 4.5 base
- 能力维度: 时间响应性, 反应性
- 论文: https://arxiv.org/abs/2609.08977 (arXiv preprint)
- 视频: https://omni-interaction-gander.github.io/Omni-Interaction-Agent/asset/videos/full-duplex.mp4
- 项目主页: https://omni-interaction-gander.github.io/Omni-Interaction-Agent/
- 代码: https://github.com/Omni-Interaction-Gander/Omni-Interaction-Agent

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
- 实现方式: 全双工架构：在生成输出的同时持续处理输入，并把推理任务委托给后台模型；自 2026 年 7 月 31 日起输出带有 SynthID 水印。
- 参数: GPT-Live-1 and GPT-Live-1 mini · ChatGPT · API GA 2026-09-10 (v1/live/sessions) · $0.05/min billed per second (backend model billed separately)
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

#### 通义千问 Qwen3.5-Omni（Qwen3.5-Omni） — 阿里通义 (2026-03-30)
- 类型: 模型 · 时序: 回合制 · 获取方式: 公开 API, 产品 / 应用
- 输入: 语音与音频, 视频, 文字提示 → 输出: 语音 / 声音, 对话 / 文本
- 核心想法: 开放的 Qwen-Omni 系列在 2026 年转为仅通过 API 提供，基于 Qwen3-Omni 权重开展工作的实验室只能沿用旧模型，或接受托管服务。
- 内容: 阿里巴巴 2026 年的全模态模型，能听语音、看视频并用语音回答，通过 Model Studio（qwen3.5-omni-plus）和 Qwen Chat 提供，没有开放权重。Qwen 重点介绍了语义打断、74 种语言的语音识别、29 种语言的富表现力语音生成，以及“音视频氛围编程”：对着摄像头口头描述，就能生成一个网站或小游戏。
- 实现方式: Thinker-Talker 架构，两部分都采用混合注意力的混合专家结构，训练数据包含超过一亿小时的音视频内容；ARIA 对齐文本与语音单元，使流式语音更稳定。
- 参数: 256k context · 10+ h audio input · 400 s of 720p video at 1 fps
- 能力维度: 反应性, 时间响应性
- 论文: https://arxiv.org/abs/2604.15804 (Technical report)
- 视频: https://www.youtube.com/watch?v=-iTkqXlhLK8
- 项目主页: https://qwen.ai/blog?id=qwen3.5-omni
- API 文档: https://www.alibabacloud.com/help/en/model-studio/qwen-omni

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

#### Gemini 实时语音翻译（Gemini live speech translation） — 谷歌 DeepMind (2025-12-12)
- 类型: 模型 · 时序: 实时流式 · 获取方式: 产品 / 应用, 公开 API
- 输入: 语音与音频 → 输出: 语音 / 声音
- 核心想法: 让没有共同语言的两个人也能留在同一场口语交流中，扩大了能参与语音驱动情境的人群。
- 内容: Gemini 原生音频模型提供的连续语音到语音翻译：戴上耳机，Google 翻译应用（2025 年 12 月起测试）会把身边人说的话转成你的语言，同时保留说话人的语调、节奏和音高，覆盖 70 多种语言、2000 多个语言对。谷歌现在在 AI Studio 中以 Gemini 3.5 Live Translate 的名称向开发者提供该模型。
- 实现方式: 基于 Gemini 2.5 Flash Native Audio（2025 年 12 月更新）的流式音频到音频翻译，保留说话风格并过滤噪声；后续由 Gemini 3.5 Live Translate 接替。
- 参数: 70+ languages · 2,000+ language pairs
- 能力维度: 情境可达性, 时间响应性
- 视频: https://www.youtube.com/watch?v=xdPIwgDriTg
- 图片: https://storage.googleapis.com/gweb-uniblog-publish-prod/images/gemini-audio-flash__keyword_meta__dark.width-1300.png
- 项目主页: https://blog.google/products-and-platforms/products/gemini/gemini-audio-model-updates/

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
- 内容: Hume 的第三代共情语音接口，一个语音-语言模型：能在一秒内根据文字提示生成新的声音和性格，并用它对话。在 Hume 的盲测比较中，它在同理心、表现力、自然度、被打断时的表现和响应速度上的评分高于 GPT-4o。Hume 于 2026 年 10 月 2 日宣布停止提供 EVI 与 TTS API，访问将于 2026 年 11 月 13 日结束。
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
- 内容: Sesame 的对话语音模型，通过语音伴侣 Maya 与 Miles 展示：它们会停顿、发笑、变换语气、自我纠正，许多听众难以分辨是否真人。1B 规模的 CSM 于 2025 年 3 月开源权重；自 2026 年 10 月 6 日起，Sesame 的语音助手在其 iOS 与 Android 应用中向所有人开放，眼镜计划于 2027 年推出。
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

#### Drama 3 多角色语音合成（Drama 3） — Fish Audio (2026-10-13)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码, 公开 API, 产品 / 应用
- 输入: 文字提示, 语音与音频 → 输出: 语音 / 声音
- 核心想法: 整场多声音的戏可以在实验室自己的 GPU 上生成并固定版本，而不必逐句租用封闭的语音 API。
- 内容: 一个面向多角色场景的开源权重语音合成模型：一段脚本最多可包含 16 个带标签的说话人，每个声音都可以用一小段参考音频克隆，并支持 [sighs]、[laughs] 这类行内提示。Fish Audio 于 2026 年 10 月 13 日在 Hugging Face 以其研究许可发布权重，Artificial Analysis 将其预览版列为开源权重语音合成模型第一名。
- 实现方式: 混合专家文本主干（350 亿参数，每个词元激活 30 亿），结合全注意力与线性注意力，配合因果多码本音频解码器（10 个码本）；可用 SGLang-Omni 与 vLLM-Omni 部署。
- 参数: 35B MoE (3B active) · up to 16 speakers · 83 languages (developer claim)
- 能力维度: 感知真实感, 创作可及性, 情境多样性
- 视频: https://www.youtube.com/watch?v=L5IjgBBuCpg
- 项目主页: https://huggingface.co/fishaudio/drama-3
- 代码: https://huggingface.co/fishaudio/drama-3

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

#### Gemini 3.8 Flash 语音合成（Gemini 3.8 Flash TTS） — 谷歌 DeepMind (2026-09-22)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 公开 API
- 输入: 文字提示, 语音与音频 → 输出: 语音 / 声音
- 核心想法: 可以跨会话保存的提示设计声音，让低成本地为一组角色稳定“选角”成为可能，克隆声音时还内置了授权核验。
- 内容: 谷歌的语音合成模型，自 2026 年 9 月 22 日起在 Gemini API 中正式可用：Gemini 3.8 Flash TTS 面向有表演指导的演绎、地方口音和双人对话，Flash-Lite TTS 面向大批量生成和实时智能体流程。新的 Voices 接口可以根据文字提示设计可长期保存的声音，并在验证授权后复刻某个声音；两天后，Hume 的 Real World VoiceEQ 排行榜把 Flash TTS 排在第一位。
- 实现方式: 基于 Gemini 的语音生成（架构未公开），用自然语言指导发声；Flash-Lite 取代 2026 年 4 月的 gemini-3.1-flash-tts-preview。
- 参数: 150+ prebuilt and custom voices · two-speaker dialogue
- 能力维度: 创作可及性, 感知真实感, 情境多样性
- 视频: https://storage.googleapis.com/gdm-deepmind-com-prod-public/media/nqVLpNNIjrfo9GQS/TTSfinal.webm
- 项目主页: https://deepmind.google/models/gemini-audio/
- API 文档: https://ai.google.dev/gemini-api/docs/changelog

#### Realtime TTS-2 实时语音合成（Realtime TTS-2） — Inworld AI (2026-05-05)
- 类型: 模型 · 时序: 回合制 · 获取方式: 公开 API
- 输入: 文字提示, 语音与音频 → 输出: 语音 / 声音
- 核心想法: 根据对方实际的说话语气来调整发声，让脚本化的角色无需逐句标注也能有情绪上的回应。
- 内容: Inworld 面向实时对话的语音合成模型：它能听到前几轮对话的音频，因此同一句话在坏消息之后会更柔和，在玩笑之后会更明快；它还接受用日常英语写的表演指示，例如 [speak tired but warm]。2026 年 5 月 5 日发布，8 月 31 日起正式可用；Inworld 的 Realtime API 把它封装成语音到语音会话，宣传为全双工，但实际上要等用户说完才回应，被打断时停止说话。
- 实现方式: 以前几轮对话音频为上下文的语音合成模型，支持自然语言表演指示标签和用文字描述设计声音；2026 年 8 月 9 日推出的 Flash 版本去掉表演指示以换取更低延迟。
- 参数: TTS-2 ~100 ms · TTS-2 Flash 20 ms time to first audio (server-side P90, developer claim) · 100+ languages
- 能力维度: 行为似真性, 时间响应性, 创作可及性
- 视频: https://www.youtube.com/watch?v=Y82bWkYKOMw
- 项目主页: https://inworld.ai/blog/realtime-tts-2
- API 文档: https://docs.inworld.ai/release-notes/tts

#### Seed Speech 2.0 语音合成与识别（Seed Speech 2.0） — 字节跳动 Seed (2026-03-16)
- 类型: 模型 · 时序: 回合制 · 获取方式: 公开 API
- 输入: 文字提示, 语音与音频 → 输出: 语音 / 声音
- 核心想法: 与 Inworld 的 TTS-2 类似，它让回答的语气取决于对方刚刚说了什么，这是脚本化语音流程原本缺少的线索。
- 内容: 字节跳动 2026 年在 BytePlus 上推出的语音技术组合，包含 TTS 2.0 与 ASR 2.0。TTS 2.0 会把用户的问题和它要说出的回答一起理解，使语气、节奏和停顿契合这次交流；提示词或参考上下文可以设定情绪、语速、音高、音色和风格。BytePlus 报告其朗读数学与科学公式的准确率约为 90%。
- 实现方式: 以对话中的提问和回答文本共同为条件的“问—答”式语音合成，并支持提示词与参考上下文控制（架构未公开）。
- 能力维度: 行为似真性, 创作可及性
- 视频: https://www.youtube.com/watch?v=Rno7SlzOPh8
- 图片: https://sf-bpcms.bytepluscdn.com/obj/byteplus-public-aiso/onebyte/seedspeech-kv-a193a405-a1a1-493f-90c8-986aad92486c.png
- 项目主页: https://www.byteplus.com/en/blog/seed-speech-2-0

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

#### Gradium — Gradium (2025-12-02)
- 类型: 平台 / API · 时序: 回合制 · 获取方式: 公开 API
- 输入: 文字提示, 语音与音频 → 输出: 语音 / 声音
- 核心想法: 做出第一个开源全双工模型的团队，如今出售的是快速的级联组件，这说明了 2026 年生产环境中语音智能体所处的位置。
- 内容: 一家 2025 年由 Kyutai 的 Moshi 研究者（Neil Zeghidour、Alexandre Défossez、Laurent Mazaré、Olivier Teboul）创立的语音 AI 公司，为语音智能体提供流式语音合成、语音识别、实时翻译、声音克隆、提示式声音设计和端侧语音合成。2025 年 12 月以 7000 万美元种子轮亮相，2026 年 7 月扩展到 1 亿美元，并报告语音合成延迟低于 50 毫秒、声音库达 1400 个（2026 年 10 月）。
- 实现方式: 流式语音合成与语音识别模型（很可能源自 Kyutai 的延迟流建模工作），以及提示式声音设计；Gradium 报告在盲听两两比较中，母语者有 72.6% 的情况更偏好其声音而非五家竞品。
- 参数: sub-50 ms TTS latency (developer claim) · 1.4k voices · EN/FR/ES/DE/PT
- 能力维度: 时间响应性, 创作可及性
- 视频: https://www.youtube.com/watch?v=qaaaXWs_bMg
- 图片: https://gradium.ai/assets/og-voice-ai.jpg
- 项目主页: https://gradium.ai

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
- 内容: Hume 基于大模型的语音合成：能从剧本中推断台词该怎么说（低声说出秘密、得意地高喊），并能根据文字描述创造新的声音。之后的 Octave 2 扩展到更多语言。Hume 于 2026 年 10 月 2 日宣布停止提供 EVI 与 TTS API，访问将于 2026 年 11 月 13 日结束。
- 实现方式: 一个经训练能理解并合成语音的语音-语言模型，根据文本、表演指示和上下文预测语调、节奏与音色。
- 能力维度: 感知真实感, 创作可及性
- 视频: https://www.youtube.com/watch?v=rKcgsg0HBlY
- 图片: https://cdn.sanity.io/images/xqnc2for/production/9b31d5726693ff81fd8347008940845ea7824338-1080x1080.png?rect=0,257,1080,567&w=1200&h=630
- 项目主页: https://www.hume.ai/blog/octave-the-first-text-to-speech-model-that-understands-what-its-saying
- API 文档: https://dev.hume.ai/docs/text-to-speech-tts/overview

### 音效、音乐与视频配音

生成拟音、环境声、音乐，以及与视频同步的配乐。

#### Instant Soundtracks 视频即时配乐（Instant Soundtracks） — ElevenLabs (2026-10-15)
- 类型: 产品 / 应用 · 时序: 预先生成 · 获取方式: 产品 / 应用, 公开 API
- 输入: 视频 → 输出: 音效、音乐与空间音频
- 核心想法: 音乐与音效以分开且带时间点的图层返回，而不是一条合成好的音轨，因此可以按实验条件分别修改。
- 内容: ElevenLabs 的一项功能：为上传的视频配上原创音乐，并在模型识别出的时刻放置生成的音效，例如标志出现时的“嗖”声；音效保留在独立的图层上，可以移动或替换。它还能把视频原有的音频作为曲风、速度与配器的参考，自 2026 年 10 月 15 日起在 ElevenCreative、ElevenMusic 和 API 中提供。
- 实现方式: 通过视频分析找出音效时机与情绪变化，驱动 ElevenLabs 的音乐模型（很可能是 Music v2）和音效生成，并对齐到编辑器时间线上的时间点。
- 能力维度: 创作可及性, 感知真实感
- 视频: https://www.youtube.com/watch?v=WtPiZ0ym13k
- 图片: https://eleven-public-cdn.elevenlabs.io/payloadcms/sm49fesxdni-Blog-cover.webp
- 项目主页: https://elevenlabs.io/blog/introducing-instant-soundtracks

#### Mirelo SFX 2.0 视频生成音效（Mirelo SFX 2.0） — Mirelo (2026-10-14)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 公开 API, 产品 / 应用
- 输入: 视频 → 输出: 音效、音乐与空间音频
- 核心想法: 把声音层重新从生成视频中分离出来，研究者可以固定画面，只改变听到的内容。
- 内容: 一个视频生成音效模型，无需重新生成画面就能替换片段的声音：它保留对白，去掉不需要的音乐，生成与动作同步、跨镜头保持一致的音效、拟音和环境声，单个视频最长 10 分钟。2026 年 10 月 14 日在 Mirelo 的工作室和 API 上线，也可在 fal、Runway 等平台使用。
- 实现方式: 以视频为条件的音频生成，包含对白检测与保留、非对白音频去除（架构未公开）；Mirelo 报告了与其他视频生成音效模型及视频模型原生音频的盲听比较。
- 参数: up to 10 min per pass (Studio and API)
- 能力维度: 感知真实感, 实验控制, 创作可及性
- 视频: https://x.com/MireloAI/status/2110360787780800611
- 图片: https://mirelo.ai/marketing/blog/mirelo-sfx-2-0-hero.jpg
- 项目主页: https://mirelo.ai/blog/mirelo-sfx-2-0

#### Soundwich：分层可控音频的视频生成（Soundwich） — Zhuo Ning (2026-09-30)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 文字提示 → 输出: 音效、音乐与空间音频, 平面视频
- 核心想法: 独立音轨让生成的声音从片段的固定属性变成可操纵的实验变量：同一场景可以分别呈现有或没有警笛、人声的版本。
- 内容: Soundwich（西蒙弗雷泽大学与特拉维夫大学，2026-09-30）让现有的音视频联合生成模型输出相互同步、各自可控时间的独立音轨（人声、音乐、音效、环境声），而不是一条混音；这样就能在不重新生成画面的情况下调整某个声音的时间、静音、替换或重新混音。它无需训练，可直接运行在 LTX-2.5、MiniMax H3 等冻结的开源模型上。
- 实现方式: 无需训练的采样方案：为每个声源生成一条音轨，用共享的场景表示在音轨之间传递全局视听上下文，并把每条音轨的跨模态注意力引向它对应的画面声源。
- 能力维度: 实验控制, 创作可及性
- 论文: https://arxiv.org/abs/2610.00691 (arXiv preprint)
- 视频: https://pub-238c8a4431a4476c8eb0f5bd97a3846e.r2.dev/media/demo/20260926/video.mp4
- 项目主页: https://soundwich.avdemo.workers.dev/
- 代码: https://github.com/CodyNing/Soundwich

#### Passing — Ryu Furusawa, 索尼 (2026-09-23)
- 类型: 体验 / 艺术作品 · 时序: 实时流式
- 输入: 视频, 身体、面部与视线追踪 → 输出: 音效、音乐与空间音频, 平面视频
- 核心想法: 把视频生成音频模型当作一位实时“聆听者”，面对它从未见过的画面，并让观众的在场引导它听到什么。
- 内容: 一件影像装置：把一段连续拍摄的单轨列车车窗影像当作时空体重新采样，变成一段没有尽头、不断变化的旅程；摄像头检测屏幕前是否有人，并据此引导画面转换。影像流由索尼的实时视频生成音频模型 SpecMaskFoley 现场配声，为一个不再遵循常规时空的风景“设想”出可能的声音。
- 实现方式: 把帧堆叠成时空体并沿非线性轨迹切片；基于摄像头的在场检测选择片段；实时 SpecMaskFoley 生成同步声景。
- 能力维度: 共创与能动性, 反应性
- 论文: https://arxiv.org/abs/2609.27489 (NeurIPS 2026 Creative AI Track)
- 视频: https://vimeo.com/1188576972
- 图片: https://live.staticflickr.com/65535/55220401637_78df0d4611_b.jpg
- 项目主页: https://ryufurusawa.com/passing

#### 阶跃星辰 StepAudio 3 Gen 全要素音频生成（StepAudio 3 Gen） — 阶跃星辰 (2026-09-11)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 公开 API, 候补 / 抢先体验
- 输入: 文字提示, 语音与音频 → 输出: 语音 / 声音, 音效、音乐与空间音频
- 核心想法: 从生成一句台词走向生成一个声音情境：谁在说话、周围发生了什么、配什么音乐，都用文字一并设定。
- 内容: 一个通用音频模型，能根据一段描述生成完整的声音场景：多个角色以设计好的音色、情绪和方言彼此对话，再加上音效、环境声、背景音乐和演唱，并按指定顺序排在同一条时间线上。阶跃星辰于 2026 年 9 月 11 日以免费预览形式在 API 中发布（stepaudio-3-gen-preview），同时推出 StepAudio 3 TTS 与 Music。
- 实现方式: 在语音、音效与音乐共享的 12.5 Hz RVQ 码空间（16 × 2048）上做离散自回归生成：主干沿时间预测第一层码本，轻量因果 Transformer 补全其余十五层；采用考虑干扰的渐进式预训练，以保留大模型的文本能力。
- 参数: 12.5 Hz tokenizer · 16 × 2048 RVQ · free preview
- 能力维度: 创作可及性, 情境可达性, 情境多样性
- 论文: https://arxiv.org/abs/2609.12945 (Technical report)
- 视频: https://stepaudiollm.github.io/step-audio-3-gen/video/gen-hero-overview.mp4
- 项目主页: https://stepaudiollm.github.io/step-audio-3-gen/
- API 文档: https://platform.stepfun.ai/docs/en/guides/models/stepaudio-3-gen

#### Suno v6 — Suno (2026-09-09)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 产品 / 应用
- 输入: 文字提示, 语音与音频 → 输出: 音效、音乐与空间音频, 语音 / 声音
- 核心想法: 与唱片公司合作训练、而非抓取曲库，成了前沿音乐模型的卖点之一；当生成音乐出现在发表的研究或展出的作品中时，这一点很重要。
- 内容: Suno 2026 年的新一代音乐模型，与华纳音乐、BMG 和 Believe 合作开发；Suno 称其更快、更有表现力、可控性更强，同时对上传的音频和歌词进行未授权使用筛查。2026 年 10 月 1 日，Suno 又推出 Speech（测试版），把人声朗读与背景音乐作为一条音轨同时生成。
- 实现方式: 与唱片公司和版权方合作开发的音乐生成模型（架构未公开），并对上传内容做未授权素材筛查。
- 能力维度: 感知真实感, 创作可及性
- 视频: https://www.youtube.com/watch?v=_lHvWn2SNC4
- 图片: https://suno.com/blog/introducing-v6/opengraph-image?4a0be6b3238f1ddc
- 项目主页: https://suno.com/blog/introducing-v6

#### MiniMax Music 3.0 音乐生成模型（MiniMax Music 3.0） — 稀宇科技 MiniMax（海螺 AI） (2026-08-13)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码, 公开 API
- 输入: 文字提示 → 输出: 音效、音乐与空间音频
- 核心想法: 为实验室提供一个开放、可固定版本、能按段落控制的完整歌曲生成模型，而不是封闭的订阅应用。
- 内容: MiniMax 的开源权重歌曲模型：根据带段落标签的歌词和结构化描述（曲风、BPM、调性、人声、编曲），一次生成最长五分钟、带人声的完整歌曲。权重已发布在 Hugging Face 和 GitHub，也可通过 MiniMax API 调用。
- 实现方式: 混合语言模型：80 亿参数的全局大模型（由 Qwen3-8B 初始化）预测八层 RVQ 中的第一层以把握长程结构，6 亿参数的局部模型预测其余各层，再由 24 亿参数的流匹配解码器结合 Flow-VAE，从两者融合的隐藏状态渲染 32 kHz 音频。
- 参数: 8B global + 0.6B local LM · 2.4B flow matching · up to 5 min · 32 kHz
- 能力维度: 创作可及性, 实验控制, 情境多样性
- 图片: https://file.cdn.minimax.io/public/32b0b01d-d945-4c9d-a8e0-8bb9204737c2.png
- 项目主页: https://www.minimax.io/blog/minimax-music-3-0-next-generation-open-weights-production-ready-versatile-music-model
- 代码: https://huggingface.co/MiniMaxAI/MiniMax-Music3

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

#### ThinkSound：思维链引导的视频配音（ThinkSound） — Huadai Liu, 阿里通义 (2025-06-26)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码, 仅限研究
- 输入: 视频, 文字提示 → 输出: 音效、音乐与空间音频
- 核心想法: 声音设计变成一串可以检查的推理步骤，人可以逐个物体地加以引导。
- 内容: 一个开源的视频生成音频模型，先推理再配声：先为无声片段生成连贯的拟音，再让用户点选某个物体细化它的声音，最后根据文字指令编辑结果；每个阶段都由多模态大模型写出思维链来引导。由阿里通义语音团队连同 AudioCoT 数据集一起发布，论文发表于 NeurIPS 2025。
- 实现方式: 多模态大模型生成关于画面动态与声学环境的思维链描述，用来驱动统一的流匹配音频基础模型，覆盖生成、以物体为中心的细化和基于指令的编辑三个阶段。
- 能力维度: 创作可及性, 实验控制, 感知真实感
- 论文: https://arxiv.org/abs/2506.21448 (NeurIPS 2025)
- 视频: https://raw.githubusercontent.com/ThinkSound-Demo/ThinkSound-Demo.github.io/main/interactive/iter1/_8JGpCc5RI8_000160_stage1.mp4
- 项目主页: https://thinksound-project.github.io/
- 代码: https://github.com/QwenAudio/ThinkSound

#### 可灵 Kling-Foley 视频拟音（Kling-Foley） — 快手 / 可灵 (2025-06-24)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 视频, 文字提示 → 输出: 音效、音乐与空间音频
- 核心想法: 展示了前沿视频团队如何先把声音做成独立、可适应时长的环节，再把音频并入视频模型本身。
- 内容: 快手可灵团队的视频生成音频模型：根据视频和可选的文字提示，生成与画面同步、任意时长的立体声音效与背景音乐。快手随之开源了工业级评测基准 Kling-Audio-Eval，但没有公开模型权重。
- 实现方式: 以文本、视频和逐帧特征联合为条件的多模态流匹配 MMDiT 预测 VAE 隐变量，解码为单声道梅尔谱，经 Mono2Stereo 模块转为立体声后再由声码器合成波形。
- 能力维度: 感知真实感, 情境可达性
- 论文: https://arxiv.org/abs/2506.19774 (arXiv 2025)
- 视频: https://p2-kling.klingai.com/kcdn/cdn-kcdn112595/00.mp4
- 图片: https://klingfoley.github.io/Kling-Foley/static/image/kling.png
- 项目主页: https://klingfoley.github.io/Kling-Foley/
- 代码: https://github.com/klingfoley/Kling-Foley

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

#### SepGen：单一模型中的多音轨音视频分离与生成（SepGen） — Aviad Dahan, 谷歌 (2026-10-08)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 文字提示, 视频 → 输出: 音效、音乐与空间音频, 平面视频
- 核心想法: 空间渲染需要按声源分开的音频：一个人声和声音可分离的生成场景，无论参与者站在哪里都能听得对。
- 内容: SepGen（特拉维夫大学与谷歌，2026-10-08）扩展了一个预训练的音视频生成模型，使其在一次采样中同时输出视频、混音音轨，以及每个带文字描述的声源各自的波形，例如对话中每位说话人一条音轨；在分离模式下，它可以按文字描述拆分已有录音。分离出的声源可以在三维场景中定位和移动，从而渲染空间音频；代码、权重和数据均已开源。
- 实现方式: 微调音视频联合生成模型，使其在混音之外，按每个声源的文字描述额外输出音频流；分离模式下保持输入混音不变，从中提取被描述的声源。
- 能力维度: 实验控制, 感知真实感
- 论文: https://arxiv.org/abs/2610.11361 (arXiv preprint)
- 视频: https://sepgen.github.io/figures/demo.mp4
- 图片: https://sepgen.github.io/figures/og.png
- 项目主页: https://sepgen.github.io/
- 代码: https://github.com/AviadDahan/SepGen

#### WorldSonus：为世界模型配上声音（WorldSonus） — Pengjun Fang (2026-10-06)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 开源权重 / 代码, 仅限研究
- 输入: 视频, 文字提示 → 输出: 音效、音乐与空间音频
- 核心想法: 声音可以和可玩的世界模型同步实时生成，并在体验过程中被改变方向，而不是事后为成片补配。
- 内容: 一个流式视频生成音频模型，目标是为交互式世界模型配上声音：随着画面帧到来，它以 100 毫秒为单位生成立体声，跟随镜头运动与场景布局，并能在生成过程中接受新的声音指令。作者报告其实时率为 0.41，在开放领域的视频生成音频基准上与离线双向模型质量相当；权重以非商用许可发布。
- 实现方式: 对音频片段做因果自回归扩散，用面向音频的字幕流程生成按片段编号调度的提示，并以从立体声与全景声录音中整理出的立体声数据进行监督训练。
- 参数: stereo · 100 ms chunks · RTF 0.41 · CC BY-NC 4.0 weights
- 能力维度: 时间响应性, 感知真实感, 实验控制
- 论文: https://arxiv.org/abs/2610.08760 (arXiv 2026)
- 视频: https://soundreactor-wbench-public-728750562872-20260920.s3.us-east-2.amazonaws.com/demo-v1/overview-ust-l4-smaller-hq-20261007-v1/h264/overview.mp4
- 图片: https://noizai.github.io/WorldSonus/assets/method-overview-v27.png
- 项目主页: https://noizai.github.io/WorldSonus/
- 代码: https://github.com/NoizAI/WorldSonus

#### StereoBind：音视频联合生成中的动态立体声（StereoBind） — Hanmo Chen (2026-09-30)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 文字提示 → 输出: 平面视频, 音效、音乐与空间音频
- 核心想法: 生成视频的原生音频开始带有方向感，这正是头显所需、而单声道配乐缺少的线索。
- 内容: 把音视频联合生成扩展到立体声，让生成的声音随画面中的声源左右移动，作者称之为“动态空间对应”。西安电子科技大学与 vivo 团队还构建了带运动轨迹的立体声音视频数据集 StereoWorld-29K，以及衡量音画空间一致性的 StereoWorldBench。
- 实现方式: 用运动轨迹为音视频联合生成器提供条件：视觉运动绑定建立声源对应，空间轨迹编码器表示声源的绝对位置，残差轨迹 RoPE 刻画相对运动。
- 参数: StereoWorld-29K dataset · StereoWorldBench
- 能力维度: 感知真实感, 实验控制
- 论文: https://arxiv.org/abs/2609.38748 (arXiv 2026)
- 视频: https://vivocameraresearch.github.io/Stereo-Bind-Project/media/case-video.mp4
- 图片: https://vivocameraresearch.github.io/Stereo-Bind-Project/media/teaser.jpg
- 项目主页: https://vivocameraresearch.github.io/Stereo-Bind-Project/

#### Audible World Models：为三维世界生成空间感知的声音（Audible World Models） — Duowen Chen (2026-09-29)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 文字提示 → 输出: 音效、音乐与空间音频
- 核心想法: 把声音放进世界状态而不是渲染出的视频里，访客绕着声源走动时，声源仍待在原处。
- 内容: 一个无需训练的流程，为文本生成的三维世界配上位置固定的声源：先构建世界的全景三维代理，找出发声物体与环境声区域，为每一项合成干声，再按听者的移动渲染其听到的声音。在 80 个生成场景上，作者（佐治亚理工学院与杜比）报告其空间一致性高于以文本、视频和全景图为条件的基线；论文发表于 NeurIPS 2026。
- 实现方式: 全景图转三维代理并做语义分层，按标签合成干声，把声源锚定到重建的几何上，再用几何声学传播做随听者位置变化的渲染。
- 参数: 80 generated scenes evaluated
- 能力维度: 持久性, 感知真实感, 实验控制
- 论文: https://arxiv.org/abs/2609.38444 (NeurIPS 2026)
- 图片: https://arxiv.org/html/2609.38444v1/img/Picture2.png
- 项目主页: https://arxiv.org/abs/2609.38444

#### OmniDream：从任意视频生成沉浸式视听体验（OmniDream） — Zitong Lan (2026-09-28)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 视频 → 输出: 音效、音乐与空间音频, 360° / 立体视频
- 核心想法: 任意一段普通视频都能变成可以环顾、且各个方向听起来都对的场景，无需录制空间音频。
- 内容: 把一段无声、视野狭窄的视频变成 360° 视听场景：在把画面扩展为全景的同时，为每个可见声源单独生成声音，经模拟场景传播后渲染成空间音频，观众转头环顾时声音始终与画面对齐。宾夕法尼亚大学的作者报告，其音画对齐、空间正确性与主观沉浸感均优于基线。
- 实现方式: 无需训练：以物体为中心的音频表示把每个声源的本征声音与场景相关的声学效果分开，从而分别生成声源、用物理方法模拟传播，并渲染为一阶全景声。
- 能力维度: 感知真实感, 情境可达性
- 论文: https://arxiv.org/abs/2609.36295 (arXiv 2026)
- 视频: https://huggingface.co/spaces/CuriousAlien000/spatial-audio-360-demo/resolve/main/media/elephant/elephant_acoustic.mp4
- 图片: https://arxiv.org/html/2609.36295v1/teaser_v2.png
- 项目主页: https://huggingface.co/spaces/CuriousAlien000/spatial-audio-360-demo

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

#### WorldPlay2 — Haiyu Zhang (2026-09-28)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入: 文字提示, 图像, 键盘与手柄动作 → 输出: 交互式帧流
- 核心想法: 在提示中把“世界是什么”“我是谁”“现在发生什么”分开，是在运行中的世界里编排事件的一步。
- 内容: 腾讯混元 WorldPlay（HY-World 1.5）的后续研究，作者多有重合：一个实时世界模型，由键盘与镜头动作以及结构化文字共同驱动，文字分别设定场景、被控角色和定时事件（点燃炉灶、气球升起），并在更长的旅程中保持一致。
- 实现方式: 分解式混合控制（逐帧对齐的动作，加上拆分为场景、实体与事件三个字段的描述），把历史帧压缩为紧凑记忆 token 的可学习压缩器，以及蒸馏为少步自回归学生模型的 “Stable Forcing” 方法。
- 能力维度: 实验控制, 持久性, 反应性
- 论文: https://arxiv.org/abs/2609.35560 (arXiv 2026)
- 视频: https://www.youtube.com/watch?v=_pFzHHslhgc
- 图片: https://worldplay2.github.io/assets/figures/overview.webp
- 项目主页: https://worldplay2.github.io/
- 代码: https://github.com/WorldPlay2/WorldPlay2

#### Agora-2：多智能体世界模型（Agora-2） — Odyssey (2026-09-24)
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

#### Astronex-World 1.0 — Astronex (2026-09-17)
- 类型: 开源工具 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 文字提示, 图像, 键盘与手柄动作 → 输出: 交互式帧流
- 核心想法: 一个小型开源模型用同一个动作接口处理镜头、游戏操控与机器人，便于在不同具身形态下测试同一情境。
- 内容: 一个以 Apache 2.0 协议开源权重的世界模型基座：根据提示或首帧，在镜头轨迹、连续动作和具身标识的条件下预测视频，并接受在推演中指定位置插入的文字事件；其因果版本可在单张 48 GB GPU 上实时流式生成。
- 实现方式: 基于 Wan2.2-TI2V-5B 视频先验，用 PRoPE 编码相机参数，以 64 维动作流调制每一层 Transformer，并提供带跨块 KV 缓存的块因果版本；五个训练阶段均在两张 NVIDIA L20 上完成。
- 参数: 5B parameters · 832×480 · 24 fps on one L20 48 GB (developer-reported)
- 能力维度: 实验控制, 反应性
- 论文: https://arxiv.org/abs/2609.20034 (arXiv 2026)
- 视频: https://world.astronex.com.cn/assets/videos/Astronex_01_720p24.mp4
- 图片: https://world.astronex.com.cn/assets/img/teaser.jpg
- 项目主页: https://world.astronex.com.cn/
- 代码: https://github.com/Astronex-Robotics/Astronex-World

#### Zing-0.5：动作与文字实时联合控制的可玩世界（Zing-0.5） — 涌跃智能 (2026-09-15)
- 类型: 模型 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 键盘与手柄动作, 文字提示, 图像 → 输出: 交互式帧流
- 核心想法: 键盘与文字同时控制，让人能在场景进行中改变事件走向；开发者报告的成本让长时间体验变得便宜。
- 内容: 涌跃智能（Seedleap.ai）推出的开源权重 5B 世界模型：玩家用键盘在生成的世界中行走，同时可以输入文字改变接下来发生的事，且无需重新开始生成；开发者称其以 832×480、24 fps 运行，每分钟流式画面的服务器租用成本约 0.009 美元。
- 实现方式: 把带力度信息的键盘输入与时间对齐的文字指令统一作为条件；在多提示词连续视频上训练的片段级教师模型，通过 DMD 监督块因果学生模型；四步生成配合保留上下文的流式推理，并以基于 SGLang 的 WebSocket 服务部署。
- 参数: 5B · 832×480 · 24 fps · ~US$0.009 per stream-minute (developer-reported) · WBench navigation 81.0
- 能力维度: 共创与能动性, 时间响应性
- 论文: https://arxiv.org/abs/2609.17909 (arXiv 2026)
- 视频: https://cdn.jsdelivr.net/gh/seedleap/zing-world-model@main/assets/case0.mp4
- 项目主页: https://zing.loopit.me/
- 代码: https://github.com/seedleap/zing-world-model

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

#### HelixWorld — Noiz AI (2026-09-03)
- 类型: 开源工具 · 时序: 实时流式 · 获取方式: 开源权重 / 代码, 候补 / 抢先体验
- 输入: 图像, 文字提示, 键盘与手柄动作 → 输出: 交互式帧流, 音效、音乐与空间音频
- 核心想法: 随头部与镜头移动而变化的空间声音正是头显体验所需要的；它是最早直接生成、而不是事后配音的世界模型之一。
- 内容: Noiz AI 与香港科技大学推出的实时世界模型，同时生成视频与随镜头变化的立体声：声场随视角转动，声音随引发它的动作起止；网页预览版可以把上传的照片变成带声音的可进入世界，代码以 Apache 2.0 协议开源。
- 实现方式: 以 6 自由度镜头轨迹和用户动作为条件的双向音视频教师模型，在带有度量级相机位姿的立体声数据集上训练，再蒸馏为因果、低延迟的学生模型。
- 参数: 768×512 · 24 fps · real-time factor 0.77 on one H800 (developer-reported)
- 能力维度: 感知真实感, 时间响应性
- 论文: https://arxiv.org/abs/2609.38123 (arXiv 2026)
- 视频: https://www.youtube.com/watch?v=cSLm_BPwJ2U
- 项目主页: https://helixworld.org/
- 代码: https://github.com/NoizAI/HelixWorld

#### EchoWM：可进入的开源全模态世界模型（EchoWM） — 京东 (2026-08-24)
- 类型: 模型 · 时序: 回合制 · 获取方式: 开源权重 / 代码
- 输入: 键盘与手柄动作, 图像, 文字提示 → 输出: 交互式帧流, 音效、音乐与空间音频, 语音 / 声音
- 核心想法: 声音与画面在世界模型内部一起生成，进入的场景从一开始就有合适的声音，而不是事后再配音。
- 内容: 京东开源的全模态世界模型，属于 JoyAI-Echo 1.5 的一部分：用户以第一或第三人称在场景中移动时，它同时生成 720p 视频以及环境音、音乐与语音，并在长时会话中保持同步。
- 实现方式: 把离散指令与连续位姿统一映射为真实尺度的相对六自由度轨迹；第三人称下相机与角色的运动关系直接从数据中学习；借助专门的数据引擎、渐进式音视频联合训练与自回归后训练，把生成延伸到长时程。
- 参数: 720p · video + ambient sound, music, speech
- 能力维度: 感知真实感, 实验控制
- 论文: https://arxiv.org/abs/2608.23189 (arXiv 2026)
- 视频: https://echovideo.jd.cn/Echo15/wm/assets/optimized/featured/hero-reel.mp4
- 项目主页: https://echo-team-joy-future-academy-jd.github.io/Echo-1.5-Page/wm/
- 代码: https://github.com/jd-opensource/JoyAI-Echo

#### Khora：可按人数扩展的多智能体世界模型（Khora） — RhOS.ai, Ophilus.AI (2026-08-09)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入: 键盘与手柄动作 → 输出: 交互式帧流
- 核心想法: 把“世界里发生了什么”与“每个人看到了什么”分开；一旦共享的社会情境里不止寥寥几人，就需要这种拆分。
- 内容: 一个多智能体世界模型：维护一份共享的世界状态，每名玩家的画面都通过查询这份状态渲染出来，因此推理时可以加入更多观察者而无需重新训练；RhOS.ai 与 Ophilus.AI 在《反恐精英》类地图上展示了它，提供在线演示，并称成本随视角数量大致线性增长。
- 实现方式: 把世界状态的演化与画面渲染解耦，并以与人数无关的渲染机制引入其他智能体的信息，使跨视角一致性来自共享状态，而不是依赖视频生成器内部各观测流之间的稠密注意力。
- 参数: any number of agents at inference · ~linear scaling with views (developer-reported)
- 能力维度: 共创与能动性, 持久性
- 论文: https://arxiv.org/abs/2608.08600 (arXiv 2026)
- 视频: https://rhos.ai/research/khora/assets/videos/HIGHLIGHT1.trimmed.mp4
- 图片: https://rhos.ai/research/khora/assets/images/khora-social-preview.jpg
- 项目主页: https://rhos.ai/research/khora

#### AlayaWorld — Alaya Lab (2026-07-08)
- 类型: 开源工具 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 图像, 文字提示, 镜头路径 / 位姿 → 输出: 交互式帧流
- 核心想法: 开放的不只是权重，还有训练代码与数据，这才让实验室能够用自己的情境重新训练世界模型。
- 内容: 一个可游玩视频世界的开源全栈框架，公开了训练与推理代码、权重以及部分训练数据：15B 自回归模型在屏幕摇杆控制镜头的情况下以 720p、24 fps 流式生成，可随时切换提示，每段可连续生成一分钟以上且无明显漂移。
- 实现方式: 分块自回归视频生成，经 DMD 蒸馏为少步推理；在带漂移的历史上训练，并用“误差库”重新注入累积伪影；v1.1（2026 年 8 月）把基于深度扭曲的空间记忆换成流式三维点缓存渲染器。
- 参数: 720p · 24 fps · 15B parameters · over 1 min per rollout (developer-reported)
- 能力维度: 持久性, 时间响应性
- 论文: https://arxiv.org/abs/2607.06291 (arXiv 2026)
- 视频: https://www.youtube.com/watch?v=n0jIEg7taTI
- 项目主页: https://alaya-lab.github.io/AlayaWorld/
- 代码: https://github.com/AlayaLab/AlayaWorld

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

#### MoWorld — Moxin (2026-07-07)
- 类型: 开源工具 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 图像, 键盘与手柄动作 → 输出: 交互式帧流
- 核心想法: 不依赖 NVIDIA 硬件的实时世界模型，会改变谁能负担得起运行它们，在中国尤其如此。
- 内容: 一个在国产 NPU 上训练和部署的“闪电”交互视频世界模型（代码面向华为昇腾）：Moxin 称其可连续控制生成、最高 50 fps，推理成本为现有世界模型方案的 30%–50%；曾在 2026 年世界人工智能大会展出，并于 2026 年 9 月开源。
- 实现方式: 用三维原生数据引擎生成几何一致的训练片段，配合课程式跨帧预训练、去噪步数蒸馏，以及 NPU 上的混合精度并行推理框架。
- 参数: up to 50 fps on NPUs · 30–50% of reference inference cost (developer-reported)
- 能力维度: 时间响应性
- 论文: https://arxiv.org/abs/2607.06216 (arXiv 2026)
- 视频: https://moxin-tech.github.io/moworld/moworld/videos/0.mp4
- 项目主页: https://moxin-tech.github.io/moworld/
- 代码: https://github.com/Moxin-Tech/moworld_base

#### DreamX-World 1.0 — 高德地图 (2026-06-15)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入: 文字提示, 图像, 键盘与手柄动作 → 输出: 交互式帧流
- 核心想法: 把 2026 年主要的持久性与事件控制技术集于一个模型，是了解通用世界模型现状的一个参照点。
- 内容: 高德（阿里巴巴）的通用交互世界模型：根据文字或图像，在镜头漫游中流式生成写实、游戏或风格化的世界，用户回到原处时保留先前的画面，并能响应提示的事件；截至 2026 年 10 月只公开了技术报告。
- 实现方式: 通过因果强制与 DMD 式蒸馏，把双向视频生成器改造为少步自回归模型；采用 E-PRoPE 相机编码、按相机几何检索记忆、事件指令微调与强化学习对齐；训练数据包括虚幻引擎渲染、游戏录像与真实视频。
- 参数: up to 16 fps on eight RTX 5090 (developer-reported)
- 能力维度: 持久性, 实验控制
- 论文: https://arxiv.org/abs/2606.16993 (arXiv 2026)
- 视频: https://www.youtube.com/watch?v=6IWCQWWgPNU
- 项目主页: https://amap-ml.github.io/DreamX_World/
- 代码: https://github.com/AMAP-ML/DreamX-World

#### MoVerse：基于全景高斯骨架的实时视频世界模型（MoVerse） — Yang Zhou (2026-06-11)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 图像, 镜头路径 / 位姿 → 输出: 交互式帧流, 高斯泼溅 / 辐射场
- 核心想法: 在视频渲染器下面垫一层显式三维骨架，转头再回来时几何保持不变，画面依然逼真。
- 内容: 一个实时世界模型，把一张普通照片变成可以漫游的场景：先补全为 360° 全景，再提升为持久的三维高斯“骨架”，最后沿用户的相机路径渲染出照片级视频；由优酷（阿里巴巴）Orange 3DV 团队推出，作者报告帧率为 8 fps。
- 实现方式: 用拓扑感知的扩散模型把输入扩展为重力对齐的 360° 全景；通过全景几何感知的残差预测，把全景提升为三维高斯骨架；再由以高斯渲染为条件的视频渲染器（双向教师模型蒸馏为因果学生模型）把骨架渲染结果转成视频。
- 参数: 1 image in · 360° panorama → 3D Gaussian scaffold · 8 fps (developer-reported)
- 能力维度: 持久性, 感知真实感
- 论文: https://arxiv.org/abs/2606.13376 (arXiv 2026)
- 视频: https://orange-3dv-team.github.io/MoVerse/assets/videos/moverse.mp4
- 图片: https://orange-3dv-team.github.io/MoVerse/assets/pipeline_overview.png
- 项目主页: https://orange-3dv-team.github.io/MoVerse/
- 代码: https://github.com/Orange-3DV-Team/MoVerse

#### minWM：实时交互视频世界模型全栈开源框架（minWM） — 生数科技（Vidu） (2026-05-28)
- 类型: 开源工具 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 镜头路径 / 位姿, 图像, 文字提示 → 输出: 交互式帧流
- 核心想法: 把实时世界模型的配方变成实验室能在开源骨干模型上复现的流程。
- 内容: 生数科技（Vidu 背后的公司）开源的端到端框架与教程：把现有的文生视频或图生视频模型改造成可控相机、少步自回归、低延迟流式输出的世界模型，并在 Wan2.1-1.3B 与 HunyuanVideo-1.5-8B 上做了演示。
- 实现方式: 先为双向视频扩散模型加入相机控制微调，再套用 Causal Forcing / Causal Forcing++ 流程（自回归扩散训练、因果 ODE 或一致性蒸馏、非对称 DMD），得到少步自回归生成器；也可用于改造 HY-WorldPlay 等现有世界模型。
- 参数: Apache-2.0 · backbones Wan2.1-T2V-1.3B, HunyuanVideo-1.5-TI2V-8B
- 能力维度: 创作可及性, 时间响应性
- 论文: https://arxiv.org/abs/2605.30263 (arXiv 2026)
- 视频: https://github.com/user-attachments/assets/99c25915-7fe7-4a20-a2c4-9d291502fccf
- 项目主页: https://github.com/shengshu-ai/minWM
- 代码: https://github.com/shengshu-ai/minWM

#### Gamma-World (γ-World) — Fangfu Liu, 英伟达 (2026-05-27)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入: 键盘与手柄动作, 图像 → 输出: 交互式帧流
- 核心想法: 社会情境需要多人共享的世界；这个模型增加参与者时无需针对人数重新训练。
- 内容: 一个世界模型：两到四名可独立操控的玩家同时在同一个生成世界中行动，每人看到的共享场景保持一致，应用从多人游戏延伸到真实机器人协作；作者称其能以 24 fps 对动作作出响应。
- 实现方式: “单纯形旋转智能体编码”（把智能体表示为 RoPE 角度空间中正单纯形的顶点，身份无需固定槽位），用可学习枢纽 token 实现线性跨智能体代价的“稀疏枢纽注意力”，以及把扩散教师模型蒸馏为带 KV 缓存的因果学生模型。
- 参数: 2–4 players · 24 fps (developer-reported)
- 能力维度: 共创与能动性, 反应性
- 论文: https://arxiv.org/abs/2605.28816 (arXiv 2026)
- 视频: https://research.nvidia.com/labs/sil/projects/gamma-world/videos/16-all.mp4
- 项目主页: https://research.nvidia.com/labs/sil/projects/gamma-world/

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

#### Starchild-1 — Odyssey (2026-05-17)
- 类型: 模型 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入: 文字提示, 语音与音频, 键盘与手柄动作 → 输出: 交互式帧流, 音效、音乐与空间音频
- 核心想法: 把声音纳入世界模型的交互回路；在许多情境中，人听到的东西（一个声音、一声警报）正是驱动其行为的关键。
- 内容: 一个世界模型的研究预览：用户持续输入文字、语音与动作时，它实时生成同步的声音与画面，场景中的环境声、对话和事件都随之改变。
- 实现方式: 把一个双向音视频基础模型因果蒸馏为自回归世界模型，并用异步 KV 缓存处理长时推演中音频与视频不同的时间尺度（据 Odyssey 技术报告）。
- 能力维度: 感知真实感, 反应性, 时间响应性
- 视频: https://framerusercontent.com/assets/k0v24lxPs3XttPIexzq95yIYE.mp4
- 图片: https://framerusercontent.com/assets/jGMTDQnPXnvR324lQwGegNJDIg.jpg
- 项目主页: https://odyssey.ml/introducing-starchild-1

#### SANA-WM：高效的分钟级世界模型（SANA-WM） — 英伟达 (2026-05-14)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像, 镜头路径 / 位姿, 文字提示 → 输出: 平面视频
- 核心想法: 小到能在一张消费级显卡上运行的模型就能生成一分钟可控相机的世界，让单台实验室机器也能做世界生成。
- 内容: 英伟达开源的 26 亿参数世界模型，原生训练即面向一分钟、720p、沿给定六自由度相机路径运动的视频；英伟达称其画质可与 LingBot-World、HY-WorldPlay 相当而成本低得多：在 64 张 H100 上训练 15 天，每段一分钟视频只需一张 GPU。
- 实现方式: 用混合线性注意力（逐帧 Gated DeltaNet 加 softmax 注意力）处理长上下文，采用双分支相机控制、带长视频精修器的两阶段生成流程，并从约 21.3 万段公开视频中提取真实尺度的六自由度相机位姿作为监督。
- 参数: 2.6B · 720p · 60 s clips · distilled NVFP4 variant denoises a 60 s clip in 34 s on one RTX 5090 (developer-reported)
- 能力维度: 实验控制, 持久性
- 论文: https://arxiv.org/abs/2605.15178 (arXiv 2026)
- 视频: https://huggingface.co/datasets/Efficient-Large-Model/Sana-assets/resolve/main/WM/media/videos/hero_reel_v9.mp4
- 项目主页: https://nvlabs.github.io/Sana/WM/
- 代码: https://github.com/NVlabs/Sana

#### 快乐生蚝（HappyOyster） — Alibaba Token Hub (ATH) (2026-04-16)
- 类型: 产品 / 应用 · 时序: 实时流式 · 获取方式: 候补 / 抢先体验, 公开 API
- 输入: 文字提示, 图像, 键盘与手柄动作 → 输出: 交互式帧流, 音效、音乐与空间音频
- 核心想法: 把世界模型当作现场导演工具：人可以随时介入，也能回溯到某一刻改走另一条分支，更像在运行一个情境，而不是渲染一段视频。
- 内容: 阿里巴巴推出的实时世界模型产品：在“执导”模式中，用户可用文字、语音或图片引导一段持续演进的场景，最长三分钟；在“漫游”（后改为“冒险”）模式中，可以第一或第三人称探索不断延展的世界。2026 年 6 月 17 日的 HappyOyster 1.0 加入了冲刺、跳跃、攻击、骑马或进入载具等动作，并可回溯到关键时刻，让剧情走向另一条分支。
- 实现方式: 一个原生多模态视频模型，在长视频数据上训练，把文字、导航动作和图像作为持续的控制信号，在同一条流中生成音频与视频；架构细节未公开。
- 参数: Directing up to 3 min at 480p / 720p · Wandering up to 1 min at 480p (developer-reported)
- 能力维度: 创作可及性, 共创与能动性, 反应性
- 视频: https://www.youtube.com/watch?v=HQYY3xUl6AY
- 图片: https://alizila.oss-us-west-1.aliyuncs.com/uploads/2026/06/Image1.png https://alizila.oss-us-west-1.aliyuncs.com/uploads/2026/04/HappyOyster.png
- 项目主页: https://www.alizila.com/alibaba-launches-happyoyster-a-world-model-product-for-real-time-immersive-creation-and-interaction/
- API 文档: https://fal.ai/happy-oyster

#### Waypoint-1.5 — Overworld (2026-04-09)
- 类型: 开源工具 · 时序: 实时流式 · 获取方式: 开源权重 / 代码, 产品 / 应用
- 输入: 文字提示, 图像, 键盘与手柄动作 → 输出: 交互式帧流
- 核心想法: 让世界模型跑在消费级硬件上：实验室可以离线运行、记录会话，并避开云端延迟。
- 内容: 一个开源权重的实时世界模型，可在游戏电脑上本地运行或通过串流使用，把一段提示或一张图像变成可探索的第一人称世界；它是 Waypoint-1（2026 年 1 月）的后继，2026 年 10 月 Waypoint 2 正在分批邀请开发者内测。
- 实现方式: 实时扩散世界模型，配有把用户输入改写为种子图像、合成视频与对齐操控信号的提示流程；分为 720p 与 360p 两档，可本地运行或串流。
- 参数: up to 720p · 60 fps · 1B parameters · consumer GPUs (developer-reported)
- 能力维度: 时间响应性, 创作可及性
- 论文: https://arxiv.org/abs/2609.37107 (arXiv 2026)
- 视频: https://www.youtube.com/watch?v=W2vDzB4KvxU
- 图片: https://over.world/blog/waypoint-1-5/og.jpg
- 项目主页: https://over.world/blog/waypoint-1-5
- 代码: https://huggingface.co/Overworld/Waypoint-1.5-1B

#### InSpatio-WorldFM — InSpatio 空间智能 (2026-03)
- 类型: 开源工具 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 图像, 文字提示, 镜头路径 / 位姿 → 输出: 交互式帧流
- 核心想法: 逐帧独立生成、而不是按视频窗口生成，可以降低延迟；当“镜头”就是人的头部时，这一点很重要。
- 内容: 一个开源的实时“帧模型”：镜头移动时独立渲染生成场景的每一帧，并在消费级 GPU 上保持多视角一致；演示中用于生成一致场景的模型属于内部模型，不在开源范围内。
- 实现方式: 用显式三维锚点与隐式空间记忆保证多视角一致；分三阶段把预训练图像扩散模型变成可控帧模型，再通过少步蒸馏变成实时生成器。
- 能力维度: 持久性, 时间响应性
- 论文: https://arxiv.org/abs/2603.11911 (arXiv 2026)
- 视频: https://www.inspatio.com/assets/worldfm-demo.mp4
- 图片: https://www.inspatio.com/assets/worldfm-cover.webp
- 项目主页: https://www.inspatio.com/models/worldfm
- 代码: https://github.com/inspatio/worldfm

#### Generated Reality：手部与相机控制的以人为中心的交互世界模拟（Generated Reality） — Linxi Xie (2026-02-20)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入: 身体、面部与视线追踪, 镜头路径 / 位姿 → 输出: 交互式帧流
- 核心想法: 让身体而不是键盘来控制生成的世界，这正是基于头显的情境所需要的；不过帧率仍远低于舒适 VR 的要求。
- 内容: 一个面向 VR 的视频世界模型，由佩戴者被追踪的头部位姿和关节级手部姿态驱动：在头显中伸手抓取，生成的第一人称场景随之变化，并以约 11 fps 流式传回头显。斯坦福团队的用户研究中，参与者的任务成功率更高，主观控制感也明显强于基线。
- 实现方式: 比较多种扩散 Transformer 条件注入方式，提出适用于三维头部与手部控制的方案（手部采用商用 VR 头显提供的 UmeTrack 表示）；把双向视频扩散教师模型蒸馏为因果自回归模型，向头显流式输出；通过人类被试研究与基线比较任务成功率与主观控制感（项目主页未给出样本量）。
- 参数: ~11 fps on a VR headset · head + joint-level hand pose control (developer-reported)
- 能力维度: 反应性, 时间响应性
- 论文: https://arxiv.org/abs/2602.18422 (CVPR 2026 (Findings))
- 视频: https://codeysun.github.io/generated-reality/static/videos/teaser_final2.mp4
- 图片: https://codeysun.github.io/generated-reality/static/images/pipeline.png
- 项目主页: https://codeysun.github.io/generated-reality/

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
- 内容: 一个世界模型：输入提示几秒后便开始流式生成视频，观看者继续输入指令，画面随之改变，单次可持续数分钟，可在网页应用中体验；它是 Odyssey-1（2025 年 5 月）的后继，之后以 Odyssey-2 Pro 的形式开放 API。2026 年 4 月 21 日推出的 Odyssey-2 Max 规模约为 Odyssey-2 Pro 的三倍，VBench 2 物理得分由 49.67 提升到 58.52（开发者自述）。
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

#### Yume — Xiaofeng Mao, Alaya Lab (2025-07-23)
- 类型: 开源工具 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 图像, 文字提示, 键盘与手柄动作 → 输出: 交互式帧流
- 核心想法: 从真实照片而非游戏画面出发，更接近行为研究常常需要的日常场所。
- 内容: 一个开源交互世界模型，把一张照片变成可用键盘探索的写实世界；作者称 2025 年 7 月的预览版是首个完全开源（数据、训练与推理代码、权重）的真实场景世界模型，2025 年 12 月的 Yume 1.5 又加入了文字触发事件与实时流式生成。
- 实现方式: 把镜头运动量化为键盘动作，用带记忆模块的掩码视频扩散 Transformer 自回归生成；1.5 版本加入统一的上下文压缩与线性注意力，并通过蒸馏实现实时流式生成。
- 能力维度: 感知真实感, 持久性
- 论文: https://arxiv.org/abs/2507.17744 (arXiv 2025)
- 视频: https://www.youtube.com/watch?v=zhkWctq4N1k
- 图片: https://github.com/stdstu12/YUME/raw/main/assets/yume.png
- 项目主页: https://github.com/stdstu12/YUME
- 代码: https://github.com/stdstu12/YUME

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

#### The Matrix：无限时长世界生成（The Matrix） — Ruili Feng, 阿里通义 (2024-12-04)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入: 键盘与手柄动作, 文字提示 → 输出: 交互式帧流
- 核心想法: 表明少量带标注的游戏录像就能教会可迁移到真实场所的操控，而在真实场所录制受控运动往往很难。
- 内容: 一个世界模拟器，以第一或第三人称连续流式生成 720p 视频，可在沙漠、草地、水面与城市中驾驶或行走，单段不间断长达一小时、速度为 16 fps；它在《极限竞速：地平线 5》《赛博朋克 2077》等游戏的少量带动作标注录像以及大量无标注真实画面上训练，能把游戏中的操控迁移到真实场景。
- 实现方式: 带交互控制模块的视频扩散 Transformer，在带标注的 3A 游戏录像与无标注真实视频上训练，以连续流的方式生成无限长度视频（通义实验室与香港大学、滑铁卢大学、Vector Institute 合作）。
- 参数: 720p · 16 fps · hour-long sequences (developer-reported)
- 能力维度: 时间响应性, 情境可达性
- 论文: https://arxiv.org/abs/2412.03568 (arXiv 2024)
- 视频: https://thematrix1999.github.io/videos/cyberpunk_processed_0.mp4
- 图片: https://thematrix1999.github.io/img/thematrix.png
- 项目主页: https://thematrix1999.github.io/

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

#### WorldCast：分布式多人世界模型（WorldCast） — Ziyang Ye, Junchao Huang (2026-10-08)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 键盘与手柄动作 → 输出: 交互式帧流
- 核心想法: 共享的生成世界可以像联网游戏一样扩展：每位参与者在本地渲染，彼此之间只传递状态。
- 内容: 一个面向《反恐精英 2》的分布式多人世界模型：每名玩家的客户端各自生成自己的画面，彼此只交换精简的玩家状态与场景状态，因此增加一名玩家只需多一个客户端，而不必扩大一个联合模型；作者称在 2 到 16 名玩家、每人一张 GPU 的条件下，每个客户端可达 16 fps 以上。
- 实现方式: 每个客户端由一个视频生成器和一个状态模型组成，状态模型根据生成画面与操作输入估计玩家位置；客户端之间交换玩家状态，并把它们投影为与相机对齐的“玩家状态场”，指导其他玩家在何处、以何种样子被画出，同时把彼此的观测复用为共享场景状态。
- 参数: 2–16 players · 16+ fps per client · 1 GPU per client · ~3.5 Mb/s received per client (developer-reported)
- 能力维度: 共创与能动性, 持久性
- 论文: https://arxiv.org/abs/2610.12412 (arXiv 2026)
- 视频: https://ziyang-ye.github.io/WorldCast-Page/assets/media/views/A.mp4
- 图片: https://ziyang-ye.github.io/WorldCast-Page/assets/og.jpg
- 项目主页: https://ziyang-ye.github.io/WorldCast-Page/
- 代码: https://github.com/Ziyang-Ye/WorldCast

#### WanToFight：多人格斗实时生成式游戏引擎（WanToFight） — Li Hu, 阿里通义 (2026-07-14)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入: 键盘与手柄动作 → 输出: 交互式帧流
- 核心想法: 两个人在同一个生成场景里以游戏速度相互对抗：这正是单人世界模型回避的、充满肢体接触的对抗情形。
- 内容: 一个生成式游戏引擎：根据两名玩家各自的键盘输入，逐帧渲染双人对战的《拳皇 97》比赛，招式接触与胜负结果都由神经网络而非游戏代码生成；阿里巴巴通义实验室称其可在单张 RTX 5090 上以 30 fps 跑完整场比赛。
- 实现方式: 基于 Wan-1.3B 视频扩散 Transformer：采用块因果注意力与滚动 KV 缓存的流式自回归生成器；以画面为依据、把每路键盘信号绑定到对应角色的“玩家关联”模块；以及按“从单人到完整对局”课程训练的门控、局部因果键盘注入模块；经四步 DMD 蒸馏的学生模型配合剪枝后的 VAE 解码器实时运行。
- 参数: 2 players · 512×384 · 30 fps on one RTX 5090 (developer-reported)
- 能力维度: 共创与能动性, 时间响应性, 反应性
- 论文: https://arxiv.org/abs/2607.12592 (arXiv 2026)
- 视频: https://humanaigc.github.io/wantofight/content/kof_teaser2.mp4
- 项目主页: https://humanaigc.github.io/wantofight/

#### MIRA：多人交互世界模型（MIRA） — General Intuition, Kyutai (2026-07-06)
- 类型: 开源工具 · 时序: 实时流式 · 获取方式: 开源权重 / 代码, 产品 / 应用
- 输入: 键盘与手柄动作 → 输出: 交互式帧流, 智能体行为与动作
- 核心想法: 多人共享同一个生成情境并看到彼此的动作，背后没有任何游戏引擎；开发者称它可以无限运行而不发散。
- 内容: 一个开源的《火箭联盟》多人世界模型：四名玩家在浏览器中进行 2 对 2 比赛，每人看到的生成画面都保持一致，帧率 20 fps；加速槽、进球与撞毁全部由模型自行追踪；“自动驾驶”模式还能让模型替缺席的玩家上场。
- 实现方式: 以 6 亿参数的视频表征编解码器为基础的 50 亿参数扩散 Transformer，在机器人对局录像上以“动作随机丢弃”方式训练，并以四名玩家的输入为条件；由 General Intuition 与 Kyutai 联合 Epic Games 开发。
- 参数: 4 players · 20 fps · 576p split across players · 5B + 600M parameters (developer-reported)
- 能力维度: 共创与能动性, 持久性, 时间响应性
- 论文: https://arxiv.org/abs/2607.05352 (arXiv 2026)
- 视频: https://mira-wm.com/media/hero-v2.mp4
- 项目主页: https://mira-wm.com/blog-post/
- 代码: https://github.com/mira-wm/mira

#### Solaris：《我的世界》多人视频世界模型（Solaris） — Georgy Savva (2026-02-25)
- 类型: 模型 · 时序: 回合制 · 获取方式: 开源权重 / 代码
- 输入: 键盘与手柄动作 → 输出: 交互式帧流
- 核心想法: 把世界模型从单一观察者变成共享空间：一名玩家建造或走开时，另一名玩家的画面也必须体现出来。
- 内容: 一个视频世界模型：同时为在同一个《我的世界》世界里行动的两名玩家分别生成第一人称画面，并让每人看到的内容与对方的动作保持一致；纽约大学公开了模型权重、评测数据集与多人数据采集引擎。
- 实现方式: 分阶段训练，从单人建模过渡到多人建模，结合双向、因果与 Self Forcing 训练，并提出节省显存的 Checkpointed Self Forcing，以便使用更长时程的教师模型；训练数据是由自动化《我的世界》机器人采集的 1260 万帧同步多人画面。
- 参数: 2 players · Minecraft · 12.6M multiplayer training frames · JAX (TPU training, GPU inference)
- 能力维度: 共创与能动性, 持久性
- 论文: https://arxiv.org/abs/2602.22208 (arXiv 2026)
- 视频: https://solaris-wm.github.io/static/img/banner-collage.mp4
- 图片: https://solaris-wm.github.io/static/img/icons/solaris-socials.png
- 项目主页: https://solaris-wm.github.io/
- 代码: https://github.com/solaris-wm/solaris

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

#### MineWorld — Junliang Guo, 微软 (2025-04-11)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入: 键盘与手柄动作, 图像 → 输出: 交互式帧流
- 核心想法: 提醒人们开源发布也可能被撤回：基于某个世界模型开展研究的实验室，需要保存自己的副本与版本记录。
- 内容: 微软研究院的 Minecraft 实时交互世界模型：根据游戏画面与键鼠动作生成后续场景，速度足以在网页演示中游玩；代码开源，但 Hugging Face 上的模型权重已于 2025 年 5 月下架。
- 实现方式: 一个视觉–动作自回归 Transformer，以交错排列的离散图像 token 与动作 token 为输入，按下一个 token 预测训练，并用并行解码算法一次预测同一帧中空间上冗余的 token。
- 参数: 4–7 fps depending on model size (developer-reported)
- 能力维度: 时间响应性, 反应性
- 论文: https://arxiv.org/abs/2504.08388 (arXiv 2025)
- 视频: https://github.com/user-attachments/assets/2f5b4740-badd-453c-970d-061abd367f82
- 图片: https://github.com/microsoft/mineworld/raw/main/assets/demo.png
- 项目主页: https://aka.ms/mineworld
- 代码: https://github.com/microsoft/mineworld

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

#### GameGen-X — Haoxuan Che (2024-11-01)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 开源权重 / 代码, 仅限研究
- 输入: 文字提示, 键盘与手柄动作 → 输出: 平面视频
- 核心想法: 较早把类游戏情境做成“生成视频 + 片段级控制”的原型，底层没有游戏引擎。
- 内容: 一个扩散 Transformer：先根据文字生成开放世界游戏画面（角色、环境、动作与事件），再让玩家用键盘式操作或新的提示控制后续片段；训练数据 OGameData 包含来自 150 多款游戏的一百多万段视频。
- 实现方式: 两阶段训练：先在 OGameData 上预训练文生视频基础模型，再冻结基础模型，只微调由游戏相关控制专家组成的 InstructNet。
- 参数: 1M+ clips · 150+ games (developer-reported)
- 能力维度: 情境多样性, 创作可及性
- 论文: https://arxiv.org/abs/2411.00769 (arXiv 2024)
- 视频: https://github.com/3a2077/3a2077.github.io/raw/main/videos/OGameGen_PV.mp4
- 项目主页: https://gamegen-x.github.io/
- 代码: https://github.com/GameGen-X/GameGen-X

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
- 内容: Odyssey 的第三代基础世界模型；公司称，它既能生成交互世界，也能借助用数小时数据训练的小型动作解码器，控制机械臂、人形机器人、汽车、无人机和游戏角色。2026 年 10 月 8 日，Odyssey 开放了公开研究预览（分 Pro 与 Flash 两档），并称 Odyssey-3 Pro 在 Physics-IQ Verified 上得分 66.1（开发者自述）。
- 实现方式: 在大量视觉观察数据上训练的自回归扩散 Transformer；针对具体任务的动作解码器把其内部表征转换为控制信号。
- 参数: few to tens of hours of task data per embodiment · Physics-IQ Verified 66.1 for Pro (developer-reported)
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

#### Real-to-Sim-to-Real (R2S2R) engine — World Labs (2026-07-28)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 多视角拍摄 / 扫描, 视频 → 输出: 三维场景 / 世界
- 核心想法: 这正是行为实验室想做的：先忠实重建一个真实情境，再系统地改变它，并检验在副本中的结果能否预测现实中的结果。
- 内容: World Labs 的“真实到仿真再到真实”引擎，来自 2026 年 7 月并入的 SceniX 团队：先采集一个真实的机器人任务，把它重建成外观与物理都相符的交互式仿真，再改变光照、杂物、物体、物理参数与相机视角；World Labs 称，由此训练的操作策略无需任何真实数据，仿真测试也能预测哪些策略会在真机上失败。
- 实现方式: 用生成式世界模型构建空间上连贯的环境，并与按任务对齐的机器人仿真结合；每次重建都通过在仿真与现实中回放同一组开环动作、比较观测与结果来验证。
- 能力维度: 实验控制, 情境多样性, 情境可达性
- 视频: https://wlt-ai-cdn.art/videos/2026-robotics-blog/box-packing-aloha-30x.mp4
- 图片: https://www.worldlabs.ai/api/opengraph-image?imageUrl=/images/scenix/blog-image.jpg&title=Building%20Worlds%20That%20Train%20Robots
- 项目主页: https://www.worldlabs.ai/blog/real-to-sim-to-real

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
- 内容: 在 GTC 台北发布的开源“全能模型”：先理解场景，再生成视频与环境声，还能输出关节角度、夹爪位置等机器人动作数据，让一个模型同时负责描述、模拟与行动。2026 年 7 月 20 日的 SIGGRAPH 2026 上，NVIDIA 开放发布了可在设备端实时运行的 4B 版本 Cosmos 3 Edge。
- 实现方式: 混合 Transformer 架构：推理模块先解读场景，生成模块再输出符合物理的视频、音频与数值动作；可后训练为世界-动作模型。
- 参数: Edge variant 4B · real-time on device (developer-reported)
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

#### GAIA-3 — Wayve (2025-12-02)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 视频, 键盘与手柄动作 → 输出: 平面视频
- 核心想法: “沿轨道运行的世界”：只改变一个行动者、其余一切保持不变，正是把对照实验的逻辑用在生成场景上。
- 内容: 第三代 GAIA 世界模型，用于评估驾驶策略：沿着改变后的自车轨迹重新“驾驶”一段录制场景，其他交通参与者、光照与天气保持原样，从而生成碰撞、险情和 NCAP 式测试案例，还能为不同的相机配置重新渲染同一场景。
- 实现方式: 以真实驾驶序列和参数化的自车轨迹变化为条件的视频世界模型；生成结果与录制的激光雷达扫描对齐以检验一致性，Wayve 称策略在生成测试中的排名与实际道路表现相关。
- 能力维度: 情境可达性, 实验控制, 情境多样性
- 视频: https://wayve.ai/wp-content/uploads/2025/11/Counterfactuals-Scenarios-GAIA-3.mp4
- 图片: https://wayve.ai/wp-content/uploads/2025/12/GAIA3-PR-notice.jpg
- 项目主页: https://wayve.ai/thinking/gaia-3/

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

#### GAIA-1 — Wayve (2023-06)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 视频, 文字提示, 键盘与手柄动作 → 输出: 平面视频
- 核心想法: 较早证明世界模型可以演出无法安全拍摄的危险反事实时刻，这正是“情境可达性”的核心。
- 内容: Wayve 的第一个驾驶生成式世界模型：以几秒真实驾驶视频、文字或自车动作为提示，生成数分钟合理的驾驶视频，能从同一起点设想多种未来，也能被强制做出训练数据中没有的行为，比如驶上人行道。
- 实现方式: 把视频、文字与动作输入映射为离散 token，用自回归 Transformer 做下一个 token 预测，再由视频扩散解码器把预测的 token 还原为画面。
- 能力维度: 情境可达性, 情境多样性
- 论文: https://arxiv.org/abs/2309.17080 (Technical report 2023)
- 视频: https://www.youtube.com/watch?v=3Si-QBUF97E
- 图片: https://wayve.ai/wp-content/uploads/2023/06/GAIA-1-tile_montage_feature.jpg
- 项目主页: https://wayve.ai/thinking/introducing-gaia1/

### 记忆、一致性与控制

让生成的世界保持连贯的研究：空间记忆、长上下文、可提示事件与状态。

#### World-T3：以测试时训练作持久记忆（World-T3） — Junyi Wu, Meta (2026-10-12)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入: 图像, 镜头路径 / 位姿 → 输出: 交互式帧流
- 核心想法: 每帧成本恒定的记忆，正是在生成场所中进行长时实时会话所需要的。
- 内容: 伊利诺伊大学芝加哥分校与 Meta Reality Labs 提出的镜头可控视频世界模型：把看到的内容存入一组在测试时更新的权重，沿原路返回时同一地点保持不变，同时实时生成。
- 实现方式: 测试时训练记忆：用递推最小二乘更新把历史观察整合进专门的参数中，使记忆成本不随推演长度增长。
- 参数: 1280×704 · 20.6 fps on one B200 (developer-reported)
- 能力维度: 持久性, 时间响应性
- 论文: https://arxiv.org/abs/2610.17434 (arXiv 2026)
- 图片: https://adreamwu.github.io/World-T3/static/images/og.jpg https://adreamwu.github.io/World-T3/static/images/teaser.webp
- 项目主页: https://adreamwu.github.io/World-T3/

#### LOCI：流式世界模型的空间线性记忆（LOCI） — Ji Xia, MBZUAI Institute of Foundation Models (2026-09-30)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 键盘与手柄动作, 图像 → 输出: 交互式帧流
- 核心想法: 把对已见画面的精确回忆与固定大小的摘要结合起来，使重访保持忠实，而记忆不会随会话时长膨胀。
- 内容: 一个流式、可控相机的世界模型，采用混合空间记忆：一半 Transformer 模块保留历史帧缓存，另一半使用按相机几何寻址的紧凑循环记忆，因此相机回到原处时画面依旧；作者在单张 H200 上流式运行，并称峰值显存比全注意力低约 30%。
- 实现方式: 交替使用两类模块：一类是带缓存的主注意力；另一类只关注当前片段，并辅以循环线性注意力记忆，其读写都以相机投影几何为条件；循环记忆的读出作为后续带缓存模块的查询输入；由四步蒸馏的学生模型流式生成视频。
- 参数: 864×480 · 4 denoising steps per chunk · 1 H200 · ~30% lower peak memory than full softmax (developer-reported)
- 能力维度: 持久性
- 论文: https://arxiv.org/abs/2609.40222 (arXiv 2026)
- 视频: https://huggingface.co/datasets/sum0214/LOCI-web-media/resolve/main/media/hero.mp4
- 图片: https://huggingface.co/datasets/sum0214/LOCI-web-media/resolve/main/media/hero.jpg
- 项目主页: https://xiaji2021.github.io/LOCI/
- 代码: https://github.com/xiaji2021/LOCI

#### WorldCrafter：隐式三维感知记忆的一致性视频世界模型（WorldCrafter） — Wangbo Yu, 腾讯 ARC 实验室 (2026-09-21)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 开源权重 / 代码
- 输入: 图像, 镜头路径 / 位姿, 文字提示 → 输出: 交互式帧流
- 核心想法: 让下一个视角决定从过去保留什么，是在固定 token 预算内维持世界一致性的低成本办法。
- 内容: 腾讯 ARC 实验室的视频世界模型，其记忆由相机来“查询”：历史画面按照即将请求的视角被压缩成固定数量的 token，从而让重访的地点和环绕镜头保持一致；基础版与蒸馏加速版权重以及 Hugging Face 在线演示均已公开。
- 实现方式: 与视频生成器联合训练的记忆编码器和以位姿为条件的读出模块，把历史观测整合为一组固定数量、针对目标视角的 token（隐式的三维感知记忆）。
- 能力维度: 持久性
- 论文: https://arxiv.org/abs/2609.24984 (arXiv 2026)
- 视频: https://www.youtube.com/watch?v=sg09ftQOl0E
- 项目主页: https://drexubery.github.io/WorldCrafter
- 代码: https://github.com/TencentARC/WorldCrafter

#### SolarWM：长时视频世界模型的开放数据与可扩展训练（SolarWM） — Junchao Huang (2026-09-02)
- 类型: 开源工具 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 镜头路径 / 位姿, 图像, 文字提示 → 输出: 交互式帧流
- 核心想法: 开放且有完整文档的数据与训练流程，让世界模型成为实验室可以复现、可以比较的东西，而不只是下载来用。
- 内容: 一套完全开放、用于构建长时交互世界模型的技术栈：来自十个数据集、带相机标注的 143 万段视频（25 TB），一套统一的训练方法，以及基于 Wan2.2、LTX-2.5 与 MiniMax-H3 的四个 5B 至 33B 参数模型；作者称这些只用五秒片段训练的模型可以实时推演数分钟乃至数小时。
- 实现方式: 可重新配置的多源数据引擎把视频片段转换为统一的逐帧对齐格式（画面、真实尺度的相机几何、文字描述、质量与来源元数据）；“保留骨干原生结构”的适配框架对每个视频骨干模型执行三阶段训练：双向适配、教师强制的自回归初始化，以及分布匹配蒸馏。
- 参数: 1.43M clips · 25 TB · 4 models, 5B–33B (developer-reported)
- 能力维度: 持久性, 实验控制
- 论文: https://arxiv.org/abs/2609.02886 (arXiv 2026)
- 视频: https://media.githubusercontent.com/media/Junchao-cs/SolarWM-Web/main/assets/demo.mp4
- 图片: https://junchao-cs.github.io/SolarWM-Web/assets/images/solar_teaser-cover.png
- 项目主页: https://junchao-cs.github.io/SolarWM-Web/
- 代码: https://github.com/Junchao-cs/SolarWM

#### ReWorld：具备长时记忆的交互世界模型（ReWorld） — Zhifei Chen, Alibaba Token Hub (ATH) (2026-08-24)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 键盘与手柄动作, 图像 → 输出: 交互式帧流
- 核心想法: 只要给记忆设定预算，实时控制与长时记忆就能共存于一个模型：世界记得去过的地方，而开销不会随着漫游距离增长。
- 内容: 一个由键盘和鼠标驱动的交互世界模型：实时流式输出 704×1280 视频，玩家离开后再回来时场景依然一致，靠的是一个按相机位姿索引“地标”、容量有上限的记忆；由香港科技大学（广州）与阿里巴巴 ATH 事业群合作，2026 年 9 月公开了 5B 模型权重。
- 实现方式: 训练时为注意力头设置不同窗口（多数头只看近处，少数全局头看完整历史），并随机路由注意力头、随机丢弃片段；推理时使用有上限的 KV 缓存，配合按位姿索引的地标库；按真实尺度对齐的数据引擎把八类数据源统一到同一动作尺度；在 LoRA 适配器中做 DMD 蒸馏，得到四步实时模式。
- 参数: 704×1280 · real-time, 4 steps · 5B checkpoints (developer-reported)
- 能力维度: 持久性, 时间响应性
- 论文: https://arxiv.org/abs/2608.23565 (arXiv 2026)
- 视频: https://zhifeichen097.github.io/ReWorld/videos/hero_loop.mp4
- 图片: https://zhifeichen097.github.io/ReWorld/videos/hero_loop.jpg
- 项目主页: https://zhifeichen097.github.io/ReWorld/
- 代码: https://github.com/zhifeichen097/ReWorld

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

#### HelloWorld：会社交回应的世界模型角色（HelloWorld） — Liangyang Ouyang, Alaya Lab (2026-08-05)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 开源权重 / 代码
- 输入: 键盘与手柄动作, 图像, 镜头路径 / 位姿 → 输出: 交互式帧流, 虚拟人（脸 / 身体）
- 核心想法: 从“对你视而不见的世界”迈向“会回应你的角色”的第一步，而且视线与时机是被测量的，而不是想当然。
- 内容: 一个让画面中的角色回应观看者的视频世界模型：镜头在场景中移动时，按下一个键，画面里的人就会转向镜头挥手、点头、鞠躬或简短问候，时机与按键对应；同时发布的 HelloWorldBench 从动作准确度、时机与视线方向三方面评分。
- 实现方式: 自蒸馏：用基础视频模型自己合成的、同时包含社交回应与镜头运动的片段来微调它，再用无需训练的时间交叉注意力掩码，把回应限定在按键对应的时间窗内（东京大学与 Alaya Lab 合作）。
- 参数: HelloWorldBench: 400 samples · ActAcc / TimeAcc / GazeDev (developer-reported)
- 能力维度: 行为似真性, 反应性, 实验控制
- 论文: https://arxiv.org/abs/2608.05070 (arXiv 2026)
- 视频: https://www.youtube.com/watch?v=j4scl5Y7gXo
- 图片: https://github.com/AlayaLab/HelloWorld/raw/main/assets/teaser.png
- 项目主页: https://github.com/AlayaLab/HelloWorld
- 代码: https://github.com/AlayaLab/HelloWorld

#### PanoWorld — Haoyuan Li, 影石 Insta360 (2026-07-10)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 开源权重 / 代码
- 输入: 图像, 镜头路径 / 位姿 → 输出: 360° / 立体视频, 交互式帧流
- 核心想法: 原生输出就是完整球面画面的世界模型，是把生成场所放进头显的最短路径。
- 内容: Insta360 研究团队与中国科学院合作的全景（360°）世界模型：随视点移动生成真实场景的 360° 视频，并记住经过的地方；同时发布了模型权重和 World360 数据集（全景无人机实拍与仿真片段）。
- 实现方式: 利用全景图的旋转等变性，把相机轨迹简化为固定朝向下的平移；用“稠密全景射线条件”表示动作，用“几何感知记忆增强”实现长程记忆，分三阶段训练。
- 能力维度: 持久性, 情境可达性
- 论文: https://arxiv.org/abs/2607.09661 (arXiv 2026)
- 视频: https://www.youtube.com/watch?v=KbA3mKTpSCU
- 图片: https://lihaoy-ux.github.io/panoworld-page/res/images/panoworld_teaser.png
- 项目主页: https://lihaoy-ux.github.io/panoworld-page/
- 代码: https://github.com/Insta360-Research-Team/PanoWorld

#### WorldDirector：带持久动态记忆的可控世界模拟器（WorldDirector） — Hanlin Wang (2026-07-02)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 文字提示, 图像, 镜头路径 / 位姿 → 输出: 平面视频
- 核心想法: 把“谁往哪里走”的计划放在像素之外，生成的世界就能记住会动的东西，而不只是静态布景。
- 内容: 一个可控的世界模拟框架：先由语言模型规划运动角色与相机的三维轨迹，再由视频模型渲染出来，因此离开画面的人或动物再次出现时，位置正确、外观不变；由香港科技大学与蚂蚁集团合作，已公开 14B 模型权重。
- 实现方式: 把语义层面的运动编排与画面生成解耦：由大语言模型协调物体三维轨迹与相机运动，再以编排好的轨迹作为条件，驱动 14B 视频生成模型输出 480p 视频。
- 参数: 14B · 480p
- 能力维度: 持久性, 实验控制
- 论文: https://arxiv.org/abs/2607.02517 (arXiv 2026)
- 视频: https://worlddirector.github.io/WorldDirector.mp4
- 项目主页: https://worlddirector.github.io/
- 代码: https://github.com/pPetrichor/WorldDirector

#### MemLearner：学习查询上下文记忆（MemLearner） — Jiwen Yu, 快手 / 可灵 (2026-06-30)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 键盘与手柄动作, 图像 → 输出: 交互式帧流
- 核心想法: 把记忆检索从固定规则变成模型自己学会的能力；一旦场景里有会移动的人和物，这一点就很关键。
- 内容: 一种为视频世界模型学习得到的记忆查询方式：不再按相机视野重叠之类的人工规则调取历史帧，而是用查询 token 决定读取哪些上下文，从而在遮挡和物体移动时保持场景一致（香港大学与快手合作）。
- 实现方式: 用可学习的查询 token 连接已存储的上下文与正在预测的 token，直接利用预训练视频生成模型本身查询记忆，无需另训检索模型。
- 能力维度: 持久性
- 论文: https://arxiv.org/abs/2606.31734 (ECCV 2026)
- 视频: https://yujiwen.github.io/memlearner/video/demo/1.mp4
- 图片: https://yujiwen.github.io/memlearner/static/images/teaser-1.png
- 项目主页: https://yujiwen.github.io/memlearner/

#### Matrix-Game 3.0（昆仑万维）（Matrix-Game 3.0） — 昆仑万维 Skywork (2026-03-27)
- 类型: 开源工具 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 图像, 键盘与手柄动作, 镜头路径 / 位姿 → 输出: 交互式帧流
- 核心想法: 在开源模型中同时实现记忆与实时速度，但硬件成本（8 张 GPU）仍限制了实验室的使用。
- 内容: 一个开源权重、带记忆增强的交互世界模型：实时流式输出 720p 视频，并按相机位置调取相关历史帧，使长时会话中的场景保持一致；2026 年 8 月，与 3.0 团队部分重合的作者以 Riemann Dynamics 名义发布后续版本 Matrix-Game 3.5（块记忆，基于 Wan2.2 的 5B 开源权重）。
- 实现方式: 在 Matrix-Game 2.0 基础上构建的 50 亿参数自回归扩散模型，采用基于 GPU 的相机感知记忆检索、少步采样、INT8 量化、蒸馏和轻量 VAE。
- 参数: 720p · up to 40 fps · 5B parameters · 8 GPUs (developer-reported)
- 能力维度: 持久性, 时间响应性
- 论文: https://arxiv.org/abs/2604.08995 (arXiv 2026)
- 视频: https://matrix-game-v3.github.io/static/videos/teaser.mp4
- 图片: https://matrix-game-v3.github.io/static/imgs/mg3_overview.png
- 项目主页: https://matrix-game-v3.github.io/
- 代码: https://github.com/SkyworkAI/Matrix-Game

#### VMem：面元索引视图记忆（VMem） — Runjia Li (2025-06-23)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 开源权重 / 代码
- 输入: 图像, 镜头路径 / 位姿 → 输出: 交互式帧流
- 核心想法: 按事物所在的位置、而不是看到它的时间来索引记忆，回访就能保持一致，算力只需关注全部历史帧的一小部分。
- 内容: 一个用于视频生成器的记忆模块，可从一张图像出发探索场景：历史视图按其观察到的三维面元（surfel）建立索引，镜头回到某处时，只调取看到过该表面的视图并据此一致地重绘。
- 实现方式: 基于估计几何构建以面元为索引的视图记忆，为相机条件视频扩散模型挑选最相关的历史视图作为上下文。
- 能力维度: 持久性
- 获奖与认可: ICCV 2025 highlight
- 论文: https://arxiv.org/abs/2506.18903 (ICCV 2025)
- 视频: https://v-mem.github.io/img/video-1min-encoded_720p.mp4
- 图片: https://v-mem.github.io/img/vmem_method.webp
- 项目主页: https://v-mem.github.io/
- 代码: https://github.com/runjiali-rl/vmem

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

#### 长上下文状态空间视频世界模型（Long-Context State-Space Video World Models） — Ryan Po (2025-05-26)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 键盘与手柄动作, 图像 → 输出: 交互式帧流
- 核心想法: 记忆不必随会话变长而增长：一个紧凑的循环状态就能以恒定成本记住一个地方。
- 内容: 一个用状态空间层在长时动作条件推演中传递记忆的视频世界模型：智能体在 Memory Maze 或 Minecraft 中重回某处时，看到的与先前一致，又不必对全部历史做注意力计算。
- 实现方式: 在空间分块上做块式状态空间扫描以延长时间记忆，同时用稠密的局部注意力保证相邻帧连贯（斯坦福大学、普林斯顿大学与 Adobe Research）。
- 能力维度: 持久性
- 论文: https://arxiv.org/abs/2505.20171 (arXiv 2025)
- 视频: https://ryanpo.com/ssm_wm/static/videos/ours_mc.mp4
- 图片: https://ryanpo.com/ssm_wm/static/images/architecture.png
- 项目主页: https://ryanpo.com/ssm_wm/

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

#### 历史引导视频扩散（History-Guided Video Diffusion） — Kiwhan Song (2025-02-10)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像, 视频, 镜头路径 / 位姿 → 输出: 平面视频
- 核心想法: 让世界模型可以更强或更弱地依赖过去，在“漂移”与“忠于历史”之间提供一个调节旋钮。
- 内容: 提出 Diffusion Forcing Transformer：一种可以以任意数量历史帧为条件的视频模型；并提出“历史引导”，在采样时加强历史的作用。两者结合可得到长得多的稳定推演，包括从单张图像出发在场景中移动镜头。
- 实现方式: 训练时为每帧设置独立噪声水平（扩散强制）并应用到 Transformer 上，推理时对不同的历史子集与噪声水平做类似无分类器引导的组合。
- 能力维度: 持久性
- 论文: https://arxiv.org/abs/2502.06764 (ICML 2025)
- 视频: https://boyuan.space/history-guidance/static/videos/long_rollout_0.mp4
- 图片: https://boyuan.space/history-guidance/static/images/thumbnail.jpg
- 项目主页: https://boyuan.space/history-guidance/
- 代码: https://github.com/kwsong0113/diffusion-forcing-transformer

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

#### GAE：几何原生自编码器（GAE (Geometry-Native Autoencoder)） — Jiahao Lu, 腾讯 ARC 实验室 (2026-09-21)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像, 文字提示, 镜头路径 / 位姿 → 输出: 平面视频, 三维场景 / 世界
- 核心想法: 在本身就编码几何的潜空间里生成，而不是事后再补几何，是让类视频世界在回头看时仍保持不变的一条路径。
- 内容: 香港科技大学与腾讯 ARC 实验室推出的开源 10 亿参数生成模型：由一张图像和一句提示生成相机可控的多视角视频，每一帧同时可解码为深度、相机位姿和点图，生成的世界因此直接带有一致的三维结构，而不只是像素。
- 实现方式: 把几何基础模型的特征重新参数化为一个紧凑潜空间（几何原生自编码器），它可同时解码出外观、深度、相机与点图；再用标准的条件流匹配模型直接在该潜空间中生成。作者报告，在生成器与训练流程不变的对照中，换用该潜空间后，画质和独立测量的三维一致性都优于只编码外观的潜空间。
- 参数: 1B parameters · image + prompt → multi-view video with depth, cameras and point maps
- 能力维度: 持久性, 感知真实感
- 论文: https://arxiv.org/abs/2609.24981 (arXiv 2026)
- 视频: https://www.youtube.com/watch?v=DpPD85IK-Ko
- 图片: https://jiah-cloud.github.io/GAE.github.io/assets/overview/GAE-teaser-poster.jpg
- 项目主页: https://jiah-cloud.github.io/GAE.github.io/
- 代码: https://github.com/TencentARC/GAE-GeometricAutoEncoder

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

#### SynCity 3000 — Paul Engstler (2026-07-06)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 文字提示, 场景规格、代码与规则 → 输出: 高斯泼溅 / 辐射场, 三维场景 / 世界
- 核心想法: 把物体生成器当作在整幅场景图上滑动的卷积来用，就能得到任意大小、可控制布局的世界，这是一条通向大规模且仍可编辑的生成情境的路线。
- 内容: 只需一句文字提示（可选地再给一个布局），SynCity 3000 就能生成一个大范围、整体连贯的三维高斯泼溅场景（郊区街道、主题乐园、沙漠遗迹、带破冰船的海冰），可以从任意角度探索，也不再有早期 SynCity 那样明显的分块网格。
- 实现方式: 分两步：先根据提示用重叠潜变量窗口上的联合扩散（类似 MultiDiffusion，可加布局约束）生成高分辨率的二等角二维场景模板；再用一个在新合成数据引擎生成的 32 万个程序化场景上微调过的图生三维模型，逐区域把模板转换为三维高斯泼溅，并参考周围上下文保持一致。
- 参数: Text → 3DGS scene of arbitrary size · fine-tuned on 320k synthetic scenes
- 能力维度: 情境多样性, 实验控制
- 论文: https://arxiv.org/abs/2607.05392 (arXiv 2026)
- 视频: https://research.paulengstler.com/syncity-3k/assets/teaser.mp4
- 项目主页: https://research.paulengstler.com/syncity-3k/
- 代码: https://github.com/paulengstler/syncity-3k

#### 高德 ABot-Earth 生成式三维地球（ABot-Earth） — 高德地图 (2026-06-08)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 产品 / 应用, 候补 / 抢先体验
- 输入: 图像, 文字提示 → 输出: 高斯泼溅 / 辐射场, 三维场景 / 世界
- 核心想法: 以卫星影像为生成依据，得到的城市级场景遵循真实地点的布局，研究可以在一条可辨认的街道上布置情境，而无需实地采集。
- 内容: 高德的生成式三维地球模型：以卫星影像为条件生成可漫游的三维高斯泼溅城市街区，每平方公里不到 10 分钟，并以分级细节（LOD）在公开的网页浏览器中流式加载，访客可以在生成的城市、月球和火星之间穿梭。0.5 版技术报告发布于 2026 年 6 月，0.7 版于 2026 年 9 月 10 日上线；截至 2026 年 10 月，用文字或参考图创作自己的 1 平方公里地块仍仅向白名单用户开放。
- 实现方式: 直接在三维高斯泼溅表示上构建的生成模型，用大量真实城市重建数据训练；推理时仅以带地理坐标的卫星影像为条件合成几何与纹理，并打包成分级 LOD，供网页地图引擎实时渲染。
- 参数: < 10 min per km² · 1 km² tiles · hierarchical LOD · web viewer
- 能力维度: 情境可达性, 持久性, 感知真实感
- 论文: https://arxiv.org/abs/2606.09967 (Technical report 2026)
- 视频: https://www.youtube.com/watch?v=Qv64FpsEi2Q
- 图片: https://raw.githubusercontent.com/amap-cvlab/ABot-Earth-0.5/main/src/fig_teaser.jpg
- 项目主页: https://abot-earth.amap.com/

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

#### GaussianGPT — Nicolas von Lützow (2026-03-27)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入:  → 输出: 高斯泼溅 / 辐射场, 三维场景 / 世界
- 核心想法: 逐步搭建场景，让“保留这部分、重新生成其余部分”成为原生操作，这正是有控制地改变一个情境所需要的。
- 内容: 一个像语言模型写文字那样逐个 token 写出三维高斯泼溅房间的 Transformer：同一个模型既能从零生成场景，也能补全残缺场景或向外扩展房间，并用采样温度控制结果的多样程度；代码与检查点已开源。
- 实现方式: 带向量量化的稀疏三维卷积自编码器把高斯基元压缩成离散潜网格；序列化后的 token 由带三维旋转位置编码的因果 Transformer 建模，训练数据为合成室内场景（3D-FRONT、Aria Synthetic Environments）。
- 能力维度: 情境多样性, 实验控制
- 论文: https://arxiv.org/abs/2603.26661 (ECCV 2026 (oral))
- 视频: https://www.youtube.com/watch?v=zVnMHkFzHDg
- 项目主页: https://nicolasvonluetzow.github.io/GaussianGPT/
- 代码: https://github.com/nicolasvonluetzow/GaussianGPT

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

#### Explorer — Odyssey (2024-12-18)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 候补 / 抢先体验
- 输入: 图像 → 输出: 高斯泼溅 / 辐射场, 三维场景 / 世界
- 核心想法: 选择高斯泼溅作为输出，意味着生成的世界可以直接进入影视和游戏工具供人手工修改：放弃实时生成，换来可编辑的资产。
- 内容: Odyssey 的第一个世界模型：约 10 分钟把一张图像变成照片级的三维高斯泼溅世界，艺术家可以在 Unreal、Houdini 或 Blender 中打开并手工修改；Odyssey 还在伦敦 Garden Studios 的虚拟制片棚里测试了这些世界。它通过联系申请提供，而非公开应用；Odyssey 此后转向实时交互的视频世界模型（Odyssey-2、Odyssey-3）。
- 实现方式: 图像到世界的生成模型（架构未公开）输出三维高斯泼溅场景；Odyssey 称平均生成时间约 10 分钟，并在早期实验中加入了雪、水、火等运动元素。
- 参数: ~10 min per world · Gaussian-splat output
- 能力维度: 感知真实感, 创作可及性
- 视频: https://framerusercontent.com/assets/nOPsdj7d3r5UPEOKBgvQiQtqjE.mp4
- 图片: https://framerusercontent.com/assets/RtVCbwsEdQy3SKNwI2I8GB4Mhbk.png
- 项目主页: https://odyssey.world/introducing-explorer

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

#### SceneScape：文本驱动的一致场景生成（SceneScape） — Rafail Fridman (2023-02-02)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 文字提示, 镜头路径 / 位姿 → 输出: 平面视频, 网格 / 三维资产
- 核心想法: 一边用图像模型绘制新视角、一边维护显式网格，是让无限生成的漫游“记得走过哪里”的最早做法之一。
- 内容: SceneScape 由一句文字和一条镜头路径生成穿行于想象场所（洞穴、鬼屋、中世纪铁匠铺）的长视频，边走边构建同一个带纹理的网格，使先前看到的表面保持一致；NeurIPS 2023，代码开源。
- 实现方式: 每一帧先从统一网格渲染，缺失区域由预训练的文生图补全模型填充，再用测试时微调以保持一致的单目深度模型把新内容提升到三维，并融合回网格。
- 能力维度: 持久性, 情境多样性
- 论文: https://arxiv.org/abs/2302.01133 (NeurIPS 2023)
- 视频: https://scenescape.github.io/joined_videos/haunted_house.mp4
- 项目主页: https://scenescape.github.io/
- 代码: https://github.com/RafailFridman/SceneScape

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

#### 地平线 EmbodiedGen V2（EmbodiedGen V2） — 地平线 (2026-07-08)
- 类型: 开源工具 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 文字提示, 图像 → 输出: 三维场景 / 世界, 网格 / 三维资产
- 核心想法: 通过对话来搭建任务环境（用“氛围编程”写场景），降低了为同一情境制作大量变体的成本。
- 内容: 地平线的开源工具包：把文字、图像和自然语言对话变成可直接仿真的资产、按任务生成的房间以及大型多房间场景，可在 Isaac Sim、MuJoCo、Genesis、SAPIEN 和 PyBullet 中加载；第二版（2026 年 7 月）接续 2025 年 6 月的 EmbodiedGen。
- 实现方式: 以统一的“可仿真”表示串起生成资产（含碰撞与可供性数据）、按任务布局、多房间场景生成和有状态的语言模型编程循环；作者报告资产的人工认可率为 96.5%，83.3% 的任务世界无需人工修改即可使用。
- 参数: 96.5% asset acceptance · 83.3% task worlds usable as generated · Isaac Sim / MuJoCo / Genesis / SAPIEN / PyBullet
- 能力维度: 创作可及性, 情境可达性, 情境多样性
- 论文: https://arxiv.org/abs/2607.07459 (Technical report 2026)
- 视频: https://www.youtube.com/watch?v=MIkJJSVM8L4
- 图片: https://horizonrobotics.github.io/EmbodiedGen/assets/img/overview.jpg
- 项目主页: https://horizonrobotics.github.io/EmbodiedGen/
- 代码: https://github.com/HorizonRobotics/EmbodiedGen

#### SimFoundry — 英伟达 (2026-06-26)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 视频 → 输出: 三维场景 / 世界, 网格 / 三维资产, 高斯泼溅 / 辐射场
- 核心想法: 一个真实场景变成一组功能可供性相同、受控变化的变体，作者还表明在这些变体中的评估能预测真实世界的结果：这正是研究希望模拟房间具备的性质。
- 内容: NVIDIA 的 SimFoundry 由一段真实桌面或房间的短视频，在一小时内自动搭建可做物理仿真的场景（高斯泼溅背景加带纹理的物体网格，包括可活动的关节物体），再生成改变物体、布局与任务的“数字表亲”；代码于 2026 年 8 月以 Apache 2.0 许可开源。
- 实现方式: 模块化流程：分割每个物体（SAM 3）、估计深度（Depth Anything 3）与位姿（FoundationPose）、生成带纹理网格（Hunyuan3D-2），再编译成带物理参数、任务建议和保持可供性的变体的 OmniGibson 场景。
- 参数: video → sim scene in < 1 h · sim-vs-real policy evaluation: mean Pearson r = 0.911 (7 tasks, 5 policy architectures)
- 能力维度: 实验控制, 情境可达性, 情境多样性
- 论文: https://arxiv.org/abs/2606.28276 (arXiv 2026)
- 视频: https://research.nvidia.com/labs/gear/simfoundry/videos/Simfoundry_Teaser.mp4
- 项目主页: https://research.nvidia.com/labs/gear/simfoundry/
- 代码: https://github.com/NVlabs/SimFoundry

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

#### SpatialGen：布局引导的三维室内场景生成（SpatialGen） — 群核科技 (2025-08)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 场景规格、代码与规则, 文字提示, 图像 → 输出: 高斯泼溅 / 辐射场, 三维场景 / 世界, 图像 / 全景图
- 核心想法: 固定平面布局和家具包围盒、只让外观随机变化，把实验者控制的部分和模型变化的部分分开了。
- 内容: 群核科技的开源模型：根据语义房间布局加一句文字或一张参考图生成三维室内场景，从多个视点合成彼此一致的颜色、几何与语义视图，再融合为高斯泼溅（3DV 2026）。
- 实现方式: 多视角、多模态扩散模型以三维布局和参考图（需要时由文字生成）为条件，逐视角预测颜色图、场景坐标图和语义图，再优化为三维高斯；训练数据为包含 12,328 个标注场景、57,440 个房间和 470 万张渲染图的合成数据集。
- 参数: training data: 12,328 scenes · 57,440 rooms · 4.7M renderings
- 能力维度: 实验控制, 创作可及性
- 论文: https://arxiv.org/abs/2509.14981 (3DV 2026)
- 视频: https://manycore-research.github.io/SpatialGen/assets/teaser.mp4
- 图片: https://manycore-research.github.io/SpatialGen/static/images/teaser.jpg
- 项目主页: https://manycore-research.github.io/SpatialGen/
- 代码: https://github.com/manycore-research/SpatialGen

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

#### 从一张照片建起罗马：单图生成完整三维场景（Building Rome from a Single Image） — Jiraphon Yenphraphai, Applied Intuition (2026-10-06)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像 → 输出: 网格 / 三维资产, 三维场景 / 世界
- 核心想法: 把物体生成器的形状先验按整场景重新分块使用，就能补出单张照片看不到的部分，让一个真实地点变成可行走、有真实尺度的替身，而且权重开放。
- 内容: 给它一张房间或街道的照片，它就会生成一个完整、带真实尺度的三维场景网格，包括相机没有拍到的表面；在浏览器查看器里可以环绕、行走，并以米为单位测量距离。
- 实现方式: 把以物体为中心的 TRELLIS 2 生成器改造用于场景：随距相机远近增大的自适应分块；把图像特征投到可见表面上，并把体素标为空闲、可见或被遮挡；在相邻分块间复用重叠潜变量的自回归生成；并在以室内为主的训练数据中加入约 4,000 个合成户外场景。Applied Intuition 称其在 Tanks and Temples、ScanNet++ 和野外照片上优于 World Tracing、GenRecon、VolFill 与 Lyra 2.0。
- 参数: Single image → metric scene mesh · indoor and outdoor · ~4,000 synthetic outdoor training scenes
- 能力维度: 感知真实感, 持久性
- 论文: https://arxiv.org/abs/2610.08790 (arXiv 2026)
- 视频: https://build-rome.github.io/assets/media/teaser.mp4
- 图片: https://build-rome.github.io/assets/media/teaser_poster.jpg
- 项目主页: https://build-rome.github.io/
- 代码: https://github.com/Applied-Intuition-Open-Source/BuildRome

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

#### WorldSculpt：由视频生成可组合的世界（WorldSculpt） — Muyao Niu (2026-09-04)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 视频, 多视角拍摄 / 扫描 → 输出: 网格 / 三维资产, 三维场景 / 世界
- 核心想法: 把世界拆成一个个物体，才能逐件编辑：挪动椅子、拿走包，其余一切在不同实验条件间保持不变。
- 内容: WorldSculpt 把一段杂乱房间的视频（附实例掩码与三维包围盒）变成同一坐标系下数百个独立、完整的物体网格；作者还把它用于 Marble 生成的泼溅世界，将其拆成可编辑的物体。代码、模型与基准均已开源。
- 实现方式: 在单物体三维生成先验 Pixal3D 上加入多视角条件通路，使每个物体都能从被遮挡的多个视角补全，并按其三维包围盒放置到共享的世界坐标系中。
- 参数: hundreds of objects per scene · per-object meshes
- 能力维度: 实验控制, 持久性, 创作可及性
- 论文: https://arxiv.org/abs/2609.05416 (arXiv 2026)
- 视频: https://alaya-lab.github.io/WorldSculpt/assets/videos/demo_video.mp4
- 图片: https://alaya-lab.github.io/WorldSculpt/assets/figures/teaser.webp
- 项目主页: https://alaya-lab.github.io/WorldSculpt/
- 代码: https://github.com/AlayaLab/WorldSculpt

#### PixWorld — Sensen Gao, 爱诗科技 PixVerse (2026-07-06)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像, 多视角拍摄 / 扫描, 镜头路径 / 位姿 → 输出: 高斯泼溅 / 辐射场, 三维场景 / 世界
- 核心想法: 当重建与生成是同一个模型时，场景中有多少是拍到的、有多少是想象的，就取决于你提供了多少视角。
- 内容: 一个同时完成重建与生成的开源扩散模型：对给定的视角做重建，对缺失的视角做生成；输入带位姿的图像，单次前向即可输出像素对齐的三维高斯场景。由南洋理工大学与爱诗科技（PixVerse）合作完成。
- 实现方式: 把带位姿的多视角输入分成干净子集（重建）和加噪子集（生成），由双流扩散 Transformer 处理并解码为像素对齐的三维高斯；损失直接定义在渲染图像上的流匹配目标，并加入几何感知损失。
- 能力维度: 持久性, 感知真实感
- 论文: https://arxiv.org/abs/2607.05373 (arXiv 2026)
- 视频: https://sensengao.github.io/PixWorld/static/videos/demo_v32.mp4
- 图片: https://sensengao.github.io/PixWorld/static/images/demo_v32_poster.png
- 项目主页: https://sensengao.github.io/PixWorld/
- 代码: https://github.com/SensenGao/PixWorld

#### Gen3R — Jiaxin Huang (2026-01-07)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像, 多视角拍摄 / 扫描 → 输出: 平面视频, 三维场景 / 世界
- 核心想法: 把生成器与重建模型耦合，每个生成视角都带有可检验的几何，从“看起来合理的画面”向“可测量的空间”迈进一步。
- 内容: Gen3R 由一张或几张图像生成场景：输出 RGB 视频及其三维几何（相机位姿、深度图和全局点云），做法是让视频扩散模型与 VGGT 重建模型共享对齐的潜变量；代码与检查点已开源。
- 实现方式: 在 VGGT 的 token 上训练适配器，得到与预训练视频扩散模型外观潜变量对齐的几何潜变量；两者联合生成，再解码为画面、相机、深度与点云。
- 能力维度: 持久性, 感知真实感
- 论文: https://arxiv.org/abs/2601.04090 (CVPR 2026)
- 视频: https://xdimlab.github.io/Gen3R/static/videos/teaser.mp4
- 图片: https://raw.githubusercontent.com/JaceyHuang/Gen3R/main/assets/teaser.png
- 项目主页: https://xdimlab.github.io/Gen3R/
- 代码: https://github.com/JaceyHuang/Gen3R

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
- 内容: visionOS 26 的功能：把任意二维照片变成带深度、可从多个角度观看的空间场景，在 Apple Vision Pro 上可以凑近、环顾（iOS 26 锁定屏幕上则呈现为视差效果）；开发者可使用 Spatial Scene API。2026 年 6 月 8 日 WWDC 发布、9 月 14 日正式推送的 visionOS 27 进一步让 Vision Pro 用户把全景照片变成空间场景，并设为个人“环境”。
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

#### ViewCrafter — Wangbo Yu (2024-09-03)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像, 镜头路径 / 位姿 → 输出: 平面视频, 高斯泼溅 / 辐射场
- 核心想法: 粗略的三维点告诉视频模型物体在哪里，视频模型补上它们看起来的样子：后来许多世界生成器都采用了这种分工。
- 内容: ViewCrafter 从一张或几张照片出发，用以点云为引导的视频扩散模型沿指定镜头路径生成新视角，再用这些画面拟合三维高斯，使场景可以实时浏览；代码与权重均已开源。
- 实现方式: 先由输入图像重建点云，沿目标轨迹渲染后作为图生视频扩散模型的条件；再通过迭代视角合成与镜头轨迹规划逐步扩大覆盖范围，最后用生成的画面优化三维高斯泼溅。
- 能力维度: 感知真实感, 实验控制
- 论文: https://arxiv.org/abs/2409.02048 (IEEE TPAMI 2025)
- 视频: https://www.youtube.com/watch?v=WGIEmu9eXmU
- 图片: https://drexubery.github.io/ViewCrafter/static/images/room.png
- 项目主页: https://drexubery.github.io/ViewCrafter/
- 代码: https://github.com/Drexubery/ViewCrafter

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

#### Hyper3D 智能体模式（Hyper3D Agentic Mode） — 影眸科技 (2026-10-10)
- 类型: 产品 / 应用 · 时序: 回合制 · 获取方式: 产品 / 应用
- 输入: 文字提示, 图像 → 输出: 网格 / 三维资产, 动作 / 动画
- 核心想法: 继 Meshy 3D 智能体之后，主要的三维资产厂商都在生成器前面加了一个负责规划的智能体：人只需说明意图，步骤由智能体决定。
- 内容: Deemos 旗下 Hyper3D（Rodin）应用中的智能体模式：它理解用户的意图、改写输入并决定建模方式，生成可编辑、尺寸可调的 N 边形（n-gon）模型，面向 CAD、建筑和产品设计，也能为模型添加动画；Deemos 称之为“氛围建模”（vibe modeling）。
- 实现方式: 专有系统；Deemos 称其为一个智能体层，负责优化提示词并在自家 Rodin 生成器之上选择建模路线，具体设计未公开。
- 能力维度: 创作可及性, 共创与能动性
- 视频: https://www.youtube.com/watch?v=heJjHOAUWLU
- 图片: https://storage.deemos.dev/assets/og-banner.png
- 项目主页: https://hyper3d.ai/

#### GATOR：生成式、智能体驱动的三维物体重建（GATOR） — Qirui Wu, 英伟达 (2026-10-08)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 图像 → 输出: 网格 / 三维资产, 三维场景 / 世界
- 核心想法: 生成负责补全相机没拍到的部分，智能体再拿拍到的部分来核对结果，这是从一次快速拍摄到真实房间的可交互副本的一条路径。
- 内容: 英伟达与西蒙菲莎大学的系统：由一张或几张随手拍的照片恢复完整、带纹理的物体资产及其在房间中的位姿，再由智能体在 Blender 中对照照片与渲染结果修补每个网格；组合出的房间被放进物理仿真，与人形机器人一起演示。
- 实现方式: 局部模态混合模块把逐块对齐的 RGB、目标掩码和点图特征结合起来，并通过文本引导的适配器分别控制结构、几何与外观；之后由“编辑—渲染—复查”的图像驱动智能体在每个物体十分钟的预算内进行修补，只有渲染结果与观测相符时才保留修改。
- 参数: 10-minute agentic refinement budget per object
- 能力维度: 持久性, 行为似真性
- 论文: https://arxiv.org/abs/2610.11215 (arXiv 2026)
- 视频: https://research.nvidia.com/labs/lpr/gator/assets/video/gator-overview.mp4
- 图片: https://research.nvidia.com/labs/lpr/gator/assets/social-card.png
- 项目主页: https://research.nvidia.com/labs/lpr/gator/

#### USDCraft 面向仿真的关节三维资产程序化建模（USDCraft） — Chuanrui Zhang, 英伟达 (2026-10-08)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 多视角拍摄 / 扫描, 图像, 文字提示 → 输出: 网格 / 三维资产
- 核心想法: 能打开、滑动、按下的物体以附带物理属性、可编辑的程序形式交付，生成的房间不只是能看，还能动手操作。
- 内容: NVIDIA（与南洋理工大学合作）的研究：由预训练大语言模型根据残缺或有缺陷的扫描网格、一张图像或一段文字，编写并反复修改可执行程序，生成抽屉、烤面包机、钢琴等带关节的物体；输出为带关节和物理属性的 USD 资产，无需手动调整即可载入 Isaac Sim。截至 2026 年 10 月，代码与数据集仍标注为“待发布”。
- 实现方式: “源几何分析”把输入网格转为区分已观测表面与未知空间的度量化文字描述；大语言模型据此编写 USD 程序，每个候选结果再用同样方式重新编码，差异直接指向需要修改的程序；最后借助视觉反馈和物理建模指引完成资产，无需针对任务的训练。
- 参数: output: OpenUSD with joints and physical properties · loads in Isaac Sim
- 能力维度: 行为似真性, 实验控制
- 论文: https://arxiv.org/abs/2610.11322 (arXiv 2026)
- 视频: https://www.youtube.com/watch?v=lNaAm5zc0BM
- 图片: https://xingyoujun.github.io/usdcraft/static/videos/update-20260928/opening.jpg
- 项目主页: https://xingyoujun.github.io/usdcraft/

#### MultiCube 部件级可控的组合式三维生成（MultiCube） — Roblox (2026-08-20)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 文字提示, 场景规格、代码与规则 → 输出: 网格 / 三维资产
- 核心想法: 像关卡设计师那样指定道具——要哪些部件、各放在哪里——而不是寄希望于一句提示词恰好生成正确的结构。
- 内容: Roblox 与卡内基梅隆大学、斯坦福大学合作的研究模型：输入一句文字提示、一份带名称的部件清单以及每个部件的包围盒，就能生成由独立部件网格组成的三维物体；同一布局可以换上不同部件，同一组部件也可以重新摆放。以预印本和项目主页形式发布，截至 2026 年 10 月未公开代码。
- 实现方式: 两阶段扩散：先生成与部件清单和布局一致的整体网格，再一次性拆分为各个部件网格；Part Layout Adapter 独立编码每个部件的名称与包围盒。
- 能力维度: 实验控制, 创作可及性
- 论文: https://arxiv.org/abs/2608.20448 (arXiv 2026)
- 视频: https://multi-cube.github.io/assets/demo.mp4
- 图片: https://multi-cube.github.io/assets/method.jpg
- 项目主页: https://multi-cube.github.io/

#### Hi3D 3.0 (Twinkle3D) — Math Magic (Hi3D) (2026-08-18)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 产品 / 应用
- 输入: 图像, 文字提示 → 输出: 网格 / 三维资产
- 核心想法: 表明商用图生三维的竞争转向几何保真度（复制出来的物体是否有同样的孔洞和刻字），并用公开的并排对比而不是单一分数来展示。
- 内容: 第三代 Hi3D 图生三维模型，基于名为 Twinkle3D 的几何模型；Math Magic 称其几何重建分辨率达 2048³ 体素、纹理最高 8K，重点还原刻字、孔洞、接缝等体现物体特征的细节；2026 年 7 月 23 日发布预告，8 月 18 日上线。
- 实现方式: 专有模型；Math Magic 称其采用了新的 2048³ 体素高精度三维表示和升级的 UV 补全算法，未发表论文。
- 参数: 2048³ voxel geometry · up to 8K PBR textures (developer claims)
- 能力维度: 感知真实感, 创作可及性
- 视频: https://www.youtube.com/watch?v=1_aWAwd3NEk
- 项目主页: https://www.prnewswire.com/news-releases/hi3d-announces-v3-0-for-august-launch-publishes-side-by-side-comparison-of-leading-ai-3d-tools-302838563.html

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

#### 混元3D-Buffalo 1.0（Hunyuan3D-Buffalo 1.0） — 腾讯混元 (2026-08-05)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 文字提示 → 输出: 网格 / 三维资产, 对话 / 文本
- 核心想法: 把“描述、生成、修改、拆分”放进同一个模型，道具可以按指令修改，而不必每次从头重新生成。
- 内容: 腾讯混元3D 的统一模型：能描述一个三维资产、由文字生成资产、按文字指令编辑资产，并按名称提取其中的部件；2026 年 8 月以技术报告和项目主页形式发布，截至 2026 年 10 月代码已预告但尚未公开。
- 实现方式: Hunyuan3D-VLM 为 Hunyuan3D DiT 生成器提供语义、结构与空间条件，编辑和部件生成时还把原始资产一并输入；训练语料共 8700 万条三维样本，其中 1200 万条编辑样本由 Nano3D-v2 生成。
- 参数: 87M training samples: 25M understanding · 50M text-to-3D · 12M editing
- 能力维度: 创作可及性, 实验控制
- 论文: https://arxiv.org/abs/2608.02711 (arXiv 2026 (technical report))
- 视频: https://tencent-hunyuan.github.io/Hunyuan3D-Buffalo1.0/intro.mp4
- 图片: https://tencent-hunyuan.github.io/Hunyuan3D-Buffalo1.0/statics/images/Pipeline.png
- 项目主页: https://tencent-hunyuan.github.io/Hunyuan3D-Buffalo1.0/
- 代码: https://github.com/Tencent-Hunyuan/Hunyuan3D-Buffalo1.0

#### MeshFlow：高效的艺术家风格网格生成（MeshFlow） — Weiyu Li, Meta (2026-06-03)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像 → 输出: 网格 / 三维资产
- 核心想法: 艺术家风格的拓扑过去只能缓慢地逐 token 生成；并行生成让干净、可直接用于游戏的网格便宜到可以按需生产。
- 内容: Meta AI 与香港科技大学的模型，约一秒即可生成艺术家风格的网格（布线干净，而不是扫描式的密集三角面），以输入几何为条件，并可附参考图像；权重以 Meta 非商用研究许可发布。
- 实现方式: 用对比损失训练的 MeshVAE 把连续的顶点位置和离散的连接关系映射到紧凑的连续潜空间，再由流匹配扩散 Transformer 并行去噪；无需坐标量化，计算量随网格规模线性增长。
- 参数: ~1 s per mesh · ~18× faster than autoregressive mesh generation (author claims)
- 能力维度: 创作可及性, 感知真实感
- 获奖与认可: CVPR 2026 Highlight
- 论文: https://arxiv.org/abs/2606.04621 (CVPR 2026 (Highlight))
- 视频: https://mesh-flow.github.io/assets/media/denoise_teaser.mp4
- 图片: https://raw.githubusercontent.com/facebookresearch/meshflow/main/assets/teaser.png
- 项目主页: https://mesh-flow.github.io/
- 代码: https://github.com/facebookresearch/meshflow

#### Meshy 3D 智能体（Meshy 3D Agent） — Meshy (2026-05-29)
- 类型: 产品 / 应用 · 时序: 回合制 · 获取方式: 产品 / 应用
- 输入: 文字提示, 图像, 草图与手势 → 输出: 网格 / 三维资产, 对话 / 文本
- 核心想法: 把资产生成从单个提示框变成能规划、能迭代的对话，研究者也可以用这种方式“说”出情境所需的道具。
- 内容: Meshy 内置的对话式智能体：用户描述想法或上传照片、草图，智能体会提出方向、批量生成概念图，把选中的方案变成可下载的三维模型，还能通过对话为角色绑定和制作动画；2026 年 10 月 14 日起向所有 Meshy 用户开放。
- 实现方式: 由大语言模型驱动的智能体，在一次对话中调度 Meshy 的图像生成、图生三维、贴图、绑定和动画工具；Meshy 还通过 MCP 服务器把这些工具开放给外部智能体。
- 能力维度: 创作可及性, 共创与能动性
- 视频: https://www.youtube.com/watch?v=YwnwaCpRNGE
- 图片: https://cdn.meshy.ai/landing-assets/blog/meshy-3d-agent/meshy-3d-agent-cover-new.webp
- 项目主页: https://www.meshy.ai/blog/meshy-3d-agent
- API 文档: https://www.meshy.ai/mcp

#### CubePart：开放词汇、部件可控的三维生成（CubePart） — Roblox (2026-05-27)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 文字提示, 场景规格、代码与规则 → 输出: 网格 / 三维资产
- 核心想法: 让创作者在生成之前就决定物体由哪些部件组成，需要能开的门、能转的旋翼从一开始就是独立的部件。
- 内容: Roblox 开源的部件可控三维生成模型：给出提示词和一份部件名称列表（例如直升机的机身、旋翼和尾部），它为每个部件生成一个完整网格，组合起来就是整个物体，可直接在游戏里编写脚本或做动画。
- 实现方式: 两阶段生成：先合成整体形状，再按开放词汇的部件清单逐个解码出每个部件的网格；训练数据是用可扩展标注流程构建的大规模部件标注三维数据集。
- 能力维度: 实验控制, 创作可及性, 行为似真性
- 论文: https://arxiv.org/abs/2605.28763 (SIGGRAPH 2026)
- 视频: https://www.youtube.com/watch?v=Afp_jkabSL0
- 图片: https://cubepart.github.io/static/images/social-card.jpg
- 项目主页: https://cubepart.github.io/
- 代码: https://huggingface.co/Roblox/cubepart

#### PhysX-Omni：统一的可仿真物理三维生成（PhysX-Omni） — Ziang Cao (2026-05-20)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像 → 输出: 网格 / 三维资产
- 核心想法: 一个知道自己多大、多重、怎样弯曲或打开的生成物体，在人或机器人触碰它时才能表现得合理。
- 内容: 南洋理工大学的开源模型，可由单张图像生成可直接仿真的物体，覆盖刚体、可变形体和铰接体三类，同时预测几何、绝对尺度、材质、可供性、关节和功能描述；一并发布了 PhysXVerse 数据集和 PhysX-Bench 基准。
- 实现方式: 经微调的 Qwen2.5-VL 视觉语言模型由粗到细地推理整体物理属性和部件级几何，并采用专为视觉语言模型设计、无需压缩即可编码高分辨率三维结构的几何表示。
- 能力维度: 行为似真性, 反应性
- 论文: https://arxiv.org/abs/2605.21572 (arXiv 2026)
- 视频: https://www.youtube.com/watch?v=ZCgj4ffz4yk
- 图片: https://physx-omni.github.io/static/videos/teaser2.png
- 项目主页: https://physx-omni.github.io/
- 代码: https://github.com/physx-omni/PhysX-Omni

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

#### Articraft：规模化生成可活动三维资产的智能体系统（Articraft） — Matt Zhou (2026-05-14)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 文字提示, 图像 → 输出: 网格 / 三维资产, 三维场景 / 世界
- 核心想法: 把物体生成为代码，每个铰链和抽屉都显式可测，于是生成的房间可以在头显里伸手去碰，而不只是看。
- 内容: 剑桥大学与牛津大学的系统：由语言模型根据文字描述（可附参考图）编写搭建程序，生成带部件和关节的可活动物体；作者把这些资产载入 VR 供人亲手操作，也载入仿真器用于机器人操作。
- 实现方式: 大模型智能体在受限的运行框架中，调用一个专用 SDK 编写代码来定义部件、组合几何、设定关节并编写测试；框架验证每个资产并返回结构化反馈，模型无需直接编写 URDF。
- 能力维度: 反应性, 情境多样性, 创作可及性
- 论文: https://arxiv.org/abs/2605.15187 (arXiv 2026)
- 视频: https://articraft3d.github.io/webpage/vr/vr_demo.mp4
- 图片: https://articraft3d.github.io/webpage/teaser.jpg
- 项目主页: https://articraft3d.github.io/
- 代码: https://github.com/articraftresearch/Articraft

#### Pixal3D 像素对齐的图生三维（Pixal3D） — 腾讯 ARC 实验室 (2026-05-11)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像, 多视角拍摄 / 扫描 → 输出: 网格 / 三维资产, 三维场景 / 世界
- 核心想法: 生成的道具终于能和原照片对得上：真实物体乃至一整间屋子的物品，都可以从一张照片重建，而不只是近似。
- 内容: 腾讯 ARC Lab 与清华大学的图生三维模型：不在标准姿态下生成，而是直接按输入照片的视角生成资产，使网格与照片逐像素对齐；它也能接收多视角图像，并可借助模块化流程把一张照片重建为由独立物体组成的场景。代码与权重以 MIT 许可证开放。
- 实现方式: 通过“像素反投影”条件，把多尺度图像特征提升到与视角对齐的三维特征体中，为原生三维潜空间生成器提供明确的像素—三维对应关系；多视角输入时把各视角反投影得到的特征体聚合起来。
- 参数: MIT licence · single- or multi-view input · ComfyUI packaging ≈786k downloads in 30 days (Hugging Face, 2026-10-18)
- 能力维度: 感知真实感, 创作可及性
- 论文: https://arxiv.org/abs/2605.10922 (SIGGRAPH 2026)
- 图片: https://ldyang694.github.io/projects/pixal3d/results/2_mesh.webp
- 项目主页: https://ldyang694.github.io/projects/pixal3d/
- 代码: https://github.com/TencentARC/Pixal3D

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

#### SIMART：把整体网格拆解为可仿真的铰接资产（SIMART） — Chuanrui Zhang, 字节跳动 Seed (2026-03-24)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像, 文字提示 → 输出: 网格 / 三维资产
- 核心想法: 把一个“雕塑般”的生成柜子变成能打开的柜子，这是从“只能看的道具”到“能用的道具”之间的一步。
- 内容: 字节跳动 Seed 与南洋理工大学的模型：输入一个整体网格（例如图生三维模型的输出），把它拆分为部件并预测关节，输出可在物理仿真器中打开的 URDF，让抽屉能拉、盖子能翻；权重以 Apache 2.0 协议开源。
- 实现方式: 稀疏三维 VQ-VAE 把网格编码为比稠密体素少约 70% 的 token；多模态大模型将其与图像和文本输入融合，完成部件定位和关节参数估计，输出 URDF 元数据和分割后的部件。
- 参数: ~70% fewer 3D tokens than dense voxels
- 能力维度: 行为似真性, 反应性
- 论文: https://arxiv.org/abs/2603.23386 (SIGGRAPH 2026)
- 视频: https://www.youtube.com/watch?v=Facqav-LthQ
- 图片: https://simart-mllm.github.io/static/videos/teaser.png
- 项目主页: https://simart-mllm.github.io/
- 代码: https://github.com/ByteDance-Seed/SimArt

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

#### AutoPartGen 自回归三维部件生成（AutoPartGen） — Meta (2025-07-17)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像 → 输出: 网格 / 三维资产
- 核心想法: 物体生成出来时已经拆成交互所需的部件——盖子、把手、门——无需另做分割。
- 内容: Meta AI 与牛津大学视觉几何组（VGG）的模型：根据一张图像、可选的二维部件掩码或已有三维形状，一次生成一个三维部件，逐步搭出物体乃至整个场景，并自行决定部件数量。Meta 于 2026 年 6 月在 Hugging Face 发布了代码和需申请访问的权重。
- 实现方式: 在 3DShape2VecSet 潜空间中自回归生成：每个部件都以已生成的部件以及图像、掩码或三维输入为条件，直到模型判断物体已完整；各部件无需额外优化即可拼合。
- 参数: weights: facebook/autopartgen on Hugging Face (gated) · published 2026-06-09
- 能力维度: 创作可及性, 实验控制
- 论文: https://arxiv.org/abs/2507.13346 (arXiv 2025)
- 视频: https://silent-chen.github.io/AutoPartGen/static/assets/video.mp4
- 图片: https://huggingface.co/datasets/silentchen/AutoPartGen-projectpage-assets/resolve/main/overview.png
- 项目主页: https://silent-chen.github.io/AutoPartGen/
- 代码: https://github.com/facebookresearch/autopartgen

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

#### TripoSG — VAST 光影焕像 (2025-02-10)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像 → 输出: 网格 / 三维资产
- 核心想法: 一个接近商用水准、许可宽松的开源形状生成模型，让实验室可以固定版本并检查生成道具所用的模型。
- 内容: VAST 开源的 15 亿参数图生形状模型，以 MIT 协议发布，另有草图条件版本；可由单张图像生成细节丰富的封闭几何，成为 2025 年三维形状生成常用的开源基线之一。
- 实现方式: 在三维 VAE 潜空间上训练的整流流 Transformer，VAE 采用 SDF、法线和 eikonal 损失训练，并配有一条筛选约 200 万个高质量三维样本的数据管线。
- 参数: 1.5B parameters
- 能力维度: 感知真实感
- 论文: https://arxiv.org/abs/2502.06608 (arXiv 2025)
- 图片: https://raw.githubusercontent.com/VAST-AI-Research/TripoSG/main/assets/doc/triposg_teaser.png
- 项目主页: https://github.com/VAST-AI-Research/TripoSG
- 代码: https://huggingface.co/VAST-AI/TripoSG

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

#### SPAR3D（稳定点感知三维）（SPAR3D (Stable Point Aware 3D)） — Stability AI (2025-01-08)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码, 公开 API
- 输入: 图像 → 输出: 网格 / 三维资产
- 核心想法: 在照片和网格之间加入一个可编辑的中间结果，人可以修正物体被遮住的那一面，而不必全盘接受模型的猜测。
- 内容: Stability AI 的开源单图生成网格模型：先采样物体的点云（用户可以编辑），再在一秒内由点云生成带纹理的网格，包括图像中看不到的背面。
- 实现方式: 点扩散模型先由图像采样稀疏点云，再由以图像和点云为条件的前馈网格化阶段预测几何、纹理与材质；以 Stability AI 社区许可证发布。
- 参数: <1 s per mesh (developer claim)
- 能力维度: 实验控制, 创作可及性
- 论文: https://arxiv.org/abs/2501.04689 (CVPR 2025)
- 视频: https://www.youtube.com/watch?v=mlO3Nc3Nsng
- 图片: https://static1.squarespace.com/static/6213c340453c3f502425776e/62f2452bc121595f4d87c713/677c55948f46f6565bb34016/1736395384697/SPAR3D_Hero+Thumbnail_Blog+1_1.png?format=1500w
- 项目主页: https://stability.ai/news/stable-point-aware-3d
- 代码: https://github.com/Stability-AI/stable-point-aware-3d

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

#### Shap-E（及 Point-E）（Shap-E (and Point-E)） — OpenAI (2023-05-03)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 文字提示, 图像 → 输出: 网格 / 三维资产
- 核心想法: 最早被广泛使用的前馈式文生三维模型：快速、开源但粗糙，是后来原生三维生成模型的比较基线。
- 内容: OpenAI 开源的文生 / 图生三维模型：Point-E（2022 年 12 月）可在单张 GPU 上用一到两分钟生成彩色点云，Shap-E（2023 年 5 月）生成隐式函数，几秒内即可渲染为带纹理的网格或神经辐射场。
- 实现方式: Shap-E 先训练一个编码器，把三维资产映射为隐式函数的参数（可作为网格或 NeRF 渲染），再在这些参数上训练条件扩散模型；Point-E 则把文生图模型与图像到点云的扩散模型串联起来。
- 能力维度: 创作可及性, 情境多样性
- 论文: https://arxiv.org/abs/2305.02463 (arXiv 2023)
- 图片: https://raw.githubusercontent.com/openai/shap-e/main/samples/a_chair_that_looks_like_an_avocado/2.gif https://raw.githubusercontent.com/openai/shap-e/main/samples/a_penguin/1.gif
- 项目主页: https://github.com/openai/shap-e
- 代码: https://github.com/openai/shap-e

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
- 内容: Tripo 的角色模型，可由图像或提示词生成带干净四边形拓扑、可直接做动画的角色；2026 年 9 月 6 日发布预览，10 月 1 日正式上线。2026 年 10 月 Tripo 重做了自动绑定：加入手部骨骼和五种引擎骨骼预设，并可由文字生成 1–10 秒的动作片段，最多串联五段。
- 实现方式: 专有模型；VAST 尚未公开其架构。
- 能力维度: 创作可及性, 感知真实感
- 视频: https://www.youtube.com/watch?v=g4ozFeSBPfo
- 项目主页: https://www.tripo3d.ai/
- API 文档: https://platform.tripo3d.ai/docs

#### UniMate：为任意骨骼生成动画的统一模型（UniMate） — Linzhan Mou (2026-09-04)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 文字提示 → 输出: 动作 / 动画
- 核心想法: 文生动作不再只适用于人：创作者绑定好的任何生物或物体，都可以用文字告诉它做什么。
- 内容: 普林斯顿大学的模型：输入任意已绑定骨骼的三维资产和一段文字提示，就能为其生成动画，无论是人、猫、蛇还是鹰，无需针对每种骨骼单独训练或提供参考动作；还支持动作编辑和中间帧补全，代码、模型和数据集均已公开。
- 实现方式: 拓扑感知的扩散 Transformer，通过基于关节两两关系的图感知注意力偏置等机制把骨骼图结构融入注意力，在多骨骼动作数据集上训练。
- 能力维度: 创作可及性, 情境多样性
- 论文: https://arxiv.org/abs/2609.05415 (SIGGRAPH Asia 2026)
- 视频: https://www.youtube.com/watch?v=xbndC-dEuVw
- 图片: https://linzhanmou.com/unimate/assets/images/og-teaser.jpg
- 项目主页: https://linzhanmou.com/unimate/
- 代码: https://github.com/Friedrich-M/UniMate

#### AniGen：可直接做动画的三维资产生成（AniGen） — Yi-Hua Huang, VAST 光影焕像 (2026-04-09)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像 → 输出: 网格 / 三维资产, 动作 / 动画
- 核心想法: 骨骼绑定与形状一起生成，而不是事后再推断，省去了多数生成角色“动不起来”的那一步。
- 内容: 香港大学与 VAST 的开源模型，可由单张图像生成已绑定的三维资产：网格、关节骨骼和蒙皮权重一起生成，适用于动物、人形和机械，生成后可直接用现成的动作数据驱动。
- 实现方式: 把形状、骨骼和蒙皮表示为同一空间域上相互一致的场（S³ Fields），配合置信度衰减的骨骼场和双重蒙皮特征场，由基于 TRELLIS 式结构化潜空间的两阶段流匹配管线生成。
- 能力维度: 创作可及性, 行为似真性
- 论文: https://arxiv.org/abs/2604.08746 (SIGGRAPH 2026)
- 视频: https://yihua7.github.io/AniGen_web/assets/videos/demo/AniGen_video_h264.mp4
- 图片: https://yihua7.github.io/AniGen_web/assets/images/teaser.png
- 项目主页: https://yihua7.github.io/AniGen_web/
- 代码: https://github.com/VAST-AI-Research/AniGen

#### SkinTokens（TokenRig）：统一自回归骨骼绑定（SkinTokens (TokenRig)） — Jia-Peng Zhang, VAST 光影焕像 (2026-02-04)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入:  → 输出: 网格 / 三维资产
- 核心想法: 骨骼绑定决定了生成角色能不能动起来；现在它变成一次生成就能完成的步骤，还可以用强化学习继续改进。
- 内容: 清华大学与 VAST 推出的 UniRig 后继工作：输入任意三维网格（从动漫角色到四足动物），把骨骼和逐顶点蒙皮权重作为同一个 token 序列一次生成，可直接导入常用动画工具；权重和演示已发布在 Hugging Face。
- 实现方式: 用 FSQ-CVAE 把稀疏的蒙皮权重压缩为离散的 SkinTokens；TokenRig 在同一序列中自回归预测骨骼参数和 SkinTokens，再通过带几何与语义奖励的强化学习阶段改进绑定结果。
- 参数: 98–133% better skinning accuracy, 17–22% better bone prediction than baselines (author claims)
- 能力维度: 创作可及性
- 论文: https://arxiv.org/abs/2602.04805 (ACM TOG 2026)
- 视频: https://zjp-shadow.github.io/works/SkinTokens/static/videos/show.mp4
- 图片: https://zjp-shadow.github.io/works/SkinTokens/static/images/wild.webp
- 项目主页: https://zjp-shadow.github.io/works/SkinTokens/
- 代码: https://github.com/VAST-AI-Research/SkinTokens

#### RigMo：绑定与动作的统一学习（RigMo） — Hao Zhang, Snap Inc. (2026-01-10)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 场景规格、代码与规则 → 输出: 网格 / 三维资产, 动作 / 动画
- 核心想法: 把绑定和动作当作同一个学习问题，为没有标准骨骼的生物和物体做动画提供了一条路。
- 内容: Snap Research 的模型，直接从原始的形变网格序列中同时学习绑定和动作，不需要骨骼标注，把任意运动中的网格变成带显式骨骼、蒙皮权重和动作的可动画资产；代码与数据已宣布即将公开。
- 实现方式: 把逐顶点形变编码为两个潜变量：绑定潜变量解码为高斯骨骼和蒙皮权重，动作潜变量输出随时间变化的 SE(3) 变换；再用 Motion-DiT 在该潜空间中生成动作。
- 能力维度: 创作可及性, 行为似真性
- 论文: https://arxiv.org/abs/2601.06378 (arXiv 2026)
- 视频: https://www.youtube.com/watch?v=0H0lsM3USVM
- 图片: https://rigmo-page.github.io/pdf2png/teaser/teaser-1.png
- 项目主页: https://rigmo-page.github.io/

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

#### AnimaX 借视频先验为任意三维网格生成动画（AnimaX） — Zehuan Huang, VAST 光影焕像 (2025-06-24)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 文字提示 → 输出: 动作 / 动画
- 核心想法: 从视频中学到的运动先验可以用于任意形状的骨骼，生物与道具不需要针对自身结构的动捕库也能动起来。
- 内容: 北京航空航天大学与 VAST（Tripo）的方法：借用视频扩散模型的运动知识，只需一句文字提示，就能以单次前馈在几分钟内为任意带骨骼的三维网格（人形、动物及其他关节物体）生成动画。截至 2026 年 10 月，代码与模型仍标注为“即将发布”。
- 实现方式: 把三维动作表示为多视角、多帧的二维姿态图，以模板渲染图和动作提示为条件，与视频联合生成；再把姿态三角化为三维关节位置，并通过逆向运动学转换为网格动画；训练数据为 16 万条带骨骼的动画序列。
- 参数: trained on 160k rigged sequences · arbitrary skeletons
- 能力维度: 创作可及性, 情境多样性
- 论文: https://arxiv.org/abs/2506.19851 (arXiv 2025)
- 视频: https://anima-x.github.io/assets/teaser.mp4
- 图片: https://anima-x.github.io/assets/overview.png
- 项目主页: https://anima-x.github.io/
- 代码: https://github.com/anima-x/anima-x

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

#### Sonic-AMG 由空间音频流式生成人体动作（Sonic-AMG） — Jingcheng Ni (2026-10-09)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入: 语音与音频 → 输出: 动作 / 动画
- 核心想法: 背景角色能实时对场景中的声音事件做出反应，而紧急情况与旁观者情境恰恰依赖这类线索。
- 内容: 布朗大学（与麻省理工学院、耶鲁大学和香港大学合作）的模型：根据声音的内容和方位，实时流式生成人对声音的全身反应；演示涵盖对来电、咳嗽、火警、飞机和昆虫声音的反应。作者称这是首个从空间音频流式生成动作的模型；代码标注为“即将发布”。
- 实现方式: 把声音内容和相对身体的声源位置编码为两类 token，输入带流匹配头的因果 Transformer，输出动作潜变量；用短程自回放的“排练训练”和“空间反馈”（根据生成的根节点姿态重新计算声源方向）缩小训练与流式推理之间的差距。
- 能力维度: 反应性, 行为似真性, 时间响应性
- 论文: https://arxiv.org/abs/2610.13300 (arXiv 2026)
- 视频: https://jingchengni.com/sonic-amg/assets/videos/fire-alarm-motion.mp4
- 图片: https://jingchengni.com/sonic-amg/assets/figures/teaser.png
- 项目主页: https://jingchengni.com/sonic-amg/

#### FloodDiffusion 2 流式动作生成（FloodDiffusion 2） — Yiyi Cai, Alaya Lab (2026-09-27)
- 类型: 模型 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 文字提示 → 输出: 动作 / 动画
- 核心想法: 角色在动作进行中就能被文字或语音指令改变动作、沿指定路径行进，就像游戏主持人或实验者给演员下提示一样。
- 内容: 流式文本生成动作模型：文字提示变化时（例如从慢跑改为跳跃），三维角色的动作始终连贯不断，新版还能让角色按指定路径和速度移动；权重、数据和 Hugging Face 在线演示均已公开。它是 ShandaAI 东京研究院与东京大学 FloodDiffusion（CVPR 2026）的后续版本，作者报告去噪速度提升约 11 倍，每次更新耗时 2.3 毫秒。
- 实现方式: 针对动作定制的扩散强迫（diffusion forcing）：双向注意力、下三角噪声调度和随时间变化的文字条件；第二版加入支持 KV 缓存推理的部分注意力、由正向运动学导出的损失函数以及根轨迹条件。
- 参数: 2.3 ms per update · 11.3× faster denoising and 4.6× less training compute than v1 · FID 0.053 on HumanML3D (developer figures)
- 能力维度: 时间响应性, 反应性, 实验控制
- 论文: https://arxiv.org/abs/2609.33167 (arXiv 2026)
- 视频: https://alayalab.github.io/FloodDiffusion2/assets/videos/demo-v45-1080p.mp4
- 图片: https://alayalab.github.io/FloodDiffusion2/assets/posters/demo-v45.jpg
- 项目主页: https://alayalab.github.io/FloodDiffusion2/
- 代码: https://github.com/AlayaLab/FloodDiffusion2

#### Kirin 从网络视频学习动物动作生成（Kirin） — Brian Nlong Zhao (2026-09-01)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 文字提示, 图像 → 输出: 动作 / 动画, 网格 / 三维资产
- 核心想法: 狗、马等动物也能靠描述写进场景里，补上了人体动作模型留下的空白。
- 内容: 伊利诺伊大学厄巴纳-香槟分校、宾夕法尼亚大学、斯坦福大学与剑桥大学合作的框架：从网络视频中学习四足动物的动作，再根据一张图像和一句文字生成带骨骼、会动的三维动物；同时发布 AiM3D，作者称这是首个对齐视频、文字与三维动作的大规模四足动物数据集（截至 2026 年 10 月数据集已可下载，代码尚未发布）。
- 实现方式: 从真实动物视频中重建三维动作并配上文字说明，构成 AiM3D；以文字和图像为条件的视觉引导生成模型产生动作，再借现成的图生三维模型得到网格，自动绑定骨骼后施加动作。
- 能力维度: 情境多样性, 创作可及性
- 论文: https://arxiv.org/abs/2609.01823 (ECCV 2026)
- 视频: https://kirin-ani.github.io/video_assets/global_1.mp4
- 图片: https://kirin-ani.github.io/figures/teaser.jpg
- 项目主页: https://kirin-ani.github.io/

#### StreamTalk 流式伴随语音手势生成（StreamTalk） — Xiangyue Zhang, 阿里通义 (2026-08-03)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 语音与音频 → 输出: 动作 / 动画
- 核心想法: 说话的角色可以连续数分钟保持手势同步，不会像开环流式模型那样慢慢滑向怪异的姿势。
- 内容: 通义实验室（阿里巴巴）与东京大学的伴随语音手势模型：随着语音输入逐段生成三维身体与手部动作，速度达 76 fps；每段结束时从该说话人自己的动作库中检索一个合理的关键姿态并朝它修正，从而避免长时间讲话中动作逐渐跑偏。
- 实现方式: “生成—检索—修正”循环：分部位 DiT（手、身体、位移分别建模）先预测粗略片段，再从说话人专属数据库中检索末尾关键姿态，并据此修正片段；训练时用随机锚点遮挡，让模型学会从稀疏的边界姿态恢复完整动作。
- 参数: 76 fps real-time · BEAT2 benchmark
- 能力维度: 时间响应性, 行为似真性
- 论文: https://arxiv.org/abs/2608.01643 (ECCV 2026)
- 视频: https://www.youtube.com/watch?v=tKV3lWD6MDI
- 图片: https://xiangyue-zhang.github.io/assets/img/paper/StreamTalk/teaser.png
- 项目主页: https://xiangyue-zhang.github.io/StreamTalk/
- 代码: https://github.com/Xiangyue-Zhang/StreamTalk

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

#### VideoMDM：用二维监督训练三维人体动作生成（VideoMDM） — Amir Mann (2026-06-11)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 文字提示 → 输出: 动作 / 动画
- 核心想法: 如果动作生成模型能从视频而不是动捕中学习，它能生成的行为种类就不再受限于动捕棚里录过什么。
- 内容: 以色列理工学院与英伟达的研究：只用从普通单目视频中提取的二维姿态，不用任何三维真值，就训练出三维人体动作扩散模型；在 HumanML3D 上几乎追平全三维监督的 MDM，在 Fit3D 和 NBA 视频上学到的动作更受人类评审偏好。
- 实现方式: 用预训练的二维到三维提升模型得到带噪声的三维姿态序列，在三维空间中加噪去噪，再把预测重投影到二维、用深度加权损失与准确的关键点比对来监督，并把常用的三维正则项改造到二维设定。
- 参数: HumanML3D FID 0.88 (vs 0.54 for 3D-supervised MDM)
- 能力维度: 感知真实感, 情境多样性
- 论文: https://arxiv.org/abs/2606.13364 (arXiv 2026)
- 视频: https://videomdm.github.io/hero-figure.mp4
- 图片: https://videomdm.github.io/figures/method.png
- 项目主页: https://videomdm.github.io/
- 代码: https://github.com/Amir-Mann/VideoMDM_release

#### EchoAvatar 音频流实时驱动的角色动画（EchoAvatar） — Bohong Chen (2026-05-27)
- 类型: 模型 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 语音与音频, 文字提示 → 输出: 动作 / 动画, 虚拟人（脸 / 身体）
- 核心想法: 为任何语音智能体配上一副身体：说话时有手势，听到音乐会随之起舞，大语言模型还能下达特定动作。
- 内容: 浙江大学的模型：根据实时输入的语音或音乐以低延迟生成三维角色的全身动作，而且不需要事先告诉它听到的是哪一种；演示中把它接到 ChatGPT、豆包和 ElevenLabs 的语音智能体上，让智能体的声音驱动一个会动的身体，大语言模型还能通过工具调用触发特定动作。代码与预训练模型已公开。
- 实现方式: 统一的流式架构根据持续到来的音频片段合成连续动作；训练时强化动作对音频的依赖，使其无需模式标签即可同时适用于语音和音乐；再用强化学习改进在线生成质量，并通过工具调用接口接受上游大语言模型的语义控制。
- 参数: streaming speech and music input · full-body motion · MIT code and pretrained models
- 能力维度: 时间响应性, 行为似真性
- 论文: https://arxiv.org/abs/2605.28272 (SIGGRAPH 2026)
- 视频: https://www.youtube.com/watch?v=GydR3H6YwBQ
- 图片: https://robinwitch.github.io/EchoAvatar-Page/imgs/demo_pipeline_2.png
- 项目主页: https://robinwitch.github.io/EchoAvatar-Page/
- 代码: https://github.com/RobinWitch/EchoAvatar

#### Kimodo：可控人体动作生成（Kimodo） — 英伟达 (2026-03-16)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 文字提示, 场景规格、代码与规则 → 输出: 动作 / 动画
- 核心想法: 一个可下载、能遵守约束的动作生成模型：作者可以规定角色必须在哪里、做什么，中间的动作由模型合理补全。
- 内容: 英伟达开源的运动学动作扩散模型，用 700 小时光学动捕数据训练，可由文字加上全身关键帧、稀疏关节目标、二维路径点和路径等约束生成三维人体及人形机器人动作；发布了 SOMA、SMPL-X 和宇树 G1 版本以及公开基准，并于 2026 年 10 月更新到 v1.2。
- 实现方式: 基于专门设计的动作表示，两阶段 Transformer 去噪器分别预测根轨迹和身体姿态，在减少动作瑕疵的同时能灵活注入约束；训练数据为 Bones Rigplay 和 BONES-SEED 动捕数据集。
- 参数: 700 h optical mocap · SOMA 77-joint, SMPL-X and Unitree G1 skeletons
- 能力维度: 实验控制, 感知真实感
- 论文: https://research.nvidia.com/labs/sil/projects/kimodo/assets/kimodo_tech_report.pdf (NVIDIA technical report 2026)
- 视频: https://research.nvidia.com/labs/sil/projects/kimodo/assets/videos/teaser.mp4
- 图片: https://research.nvidia.com/labs/sil/projects/kimodo/assets/soma_fullbody_highlight.png
- 项目主页: https://research.nvidia.com/labs/sil/projects/kimodo/
- 代码: https://github.com/nv-tlabs/kimodo

#### FrankenMotion 部位级人体动作生成与组合（FrankenMotion） — Chuqiao Li (2026-01-15)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 文字提示 → 输出: 动作 / 动画
- 核心想法: 可以随时间精细控制各个身体部位，这正是手势、姿态等非语言线索实验所需要的。
- 内容: 图宾根大学与马克斯·普朗克信息学研究所的文本生成动作模型：每个身体部位都有自己带时间安排的文字提示，手臂、腿部和躯干可以分别指挥，并组合出训练中从未见过的动作；训练数据是借助大语言模型标注的 39 小时 Frankenstein 部位级数据集。
- 实现方式: 扩散模型以每个身体部位分层、按时间组织的文字为条件，训练数据中的原子级、异步的部位描述由大语言模型生成。
- 参数: Frankenstein dataset: 39 h with part-level, time-stamped captions
- 能力维度: 实验控制, 创作可及性
- 论文: https://arxiv.org/abs/2601.10909 (CVPR 2026)
- 视频: https://coral79.github.io/frankenmotion/video_results/00997_Ours.mp4
- 图片: https://coral79.github.io/frankenmotion/images/Method.png
- 项目主页: https://coral79.github.io/frankenmotion/
- 代码: https://github.com/Coral79/FrankenMotion-Code

#### Uthana — Uthana (2025)
- 类型: 产品 / 应用 · 时序: 预先生成 · 获取方式: 产品 / 应用, 公开 API
- 输入: 文字提示, 视频 → 输出: 动作 / 动画
- 核心想法: 生成的动作以动画师现有的工作方式交付（直接用在自己角色的骨骼上，可在 Unity、Blender 或 Maya 中使用），这才让它能真正用来为情境中的角色编排动作。
- 内容: 可由文字提示或视频生成可编辑骨骼动画的网页应用与 API，并能把动作重定向到用户自己的角色或人形机器人上；Text-to-Motion 3.0（2026 年 7 月 14 日）能理解关于节奏、姿态和风格的长提示，2026 年 5 月起已接入 Unity AI。
- 实现方式: 专有动作模型，文生动作、视频转动作、行走运动和重定向分别由不同模型完成；Uthana 同时出售棚内动捕数据，这很可能就是其训练数据来源，架构未公开。
- 能力维度: 创作可及性, 感知真实感
- 视频: https://www.youtube.com/watch?v=WHmV8kD-_xo
- 项目主页: https://uthana.com/blog/text-to-motion-30-sets-a-new-bar-for-ai-animation
- API 文档: https://uthana.com/

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

## 捕捉、重建与 4D 生成

可漫游的三维与四维（三维加时间），既可从真实世界捕捉，也可以生成：辐射场与高斯泼溅、几秒内完成的前馈式重建、动态场景、体积视频，以及由文字、图像或视频生成的运动物体、场景与世界。

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

#### InfiniSplat v2 — Yongzhen Hu, 浙江大学三维视觉组 (2026-10-14)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像, 视频, 镜头路径 / 位姿 → 输出: 高斯泼溅 / 辐射场, 三维场景 / 世界
- 核心想法: 前馈式泼溅如今要看它在远离拍摄位置时的效果，而这正是人在 VR 中绕着重建场景走动时最关键的情形。
- 内容: 浙江大学三维视觉组的 InfiniSplat v2 可以从任意数量的照片直接预测三维高斯场景，相机位姿已知或未知均可，目标是在相机远离输入视角时画面依然干净。2026 年 10 月 14 日随论文发布了权重和 Hugging Face 演示。
- 实现方式: 双分支网络冻结预训练的几何分支，单独学习高斯属性，并用不透明度抑制不一致的点；训练时将预测与尺度对齐的真实相机对齐，并对大角度目标视角进行监督。
- 参数: mean LPIPS −25.8%, DISTS −32.9% vs. compared methods (pose-conditioned, 6 datasets; authors)
- 能力维度: 时间响应性, 感知真实感
- 论文: https://arxiv.org/abs/2610.20341 (arXiv 2026)
- 视频: https://huggingface.co/datasets/Edisoneh/InfiniSplat-v2-assets/resolve/8e50354da224daebc35bdd9e99cae947e0c1ea40/assets/demo/infinisplat-v2-demo-v14-preview.mp4
- 图片: https://zju3dv.github.io/InfiniSplat2/assets/demo/cover.png
- 项目主页: https://zju3dv.github.io/InfiniSplat2/
- 代码: https://github.com/zju3dv/InfiniSplat

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

#### 混元 WorldMirror（HunyuanWorld-Mirror (WorldMirror)） — 腾讯混元 (2025-10-22)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像, 视频, 镜头路径 / 位姿 → 输出: 三维场景 / 世界, 高斯泼溅 / 辐射场
- 核心想法: 关于一次拍摄已经知道的信息（头显追踪得到的位姿、手机测得的深度）可以直接输入、让重建更准确，而不必丢弃。
- 内容: WorldMirror 是腾讯混元开源的前馈式重建模型：输入照片或视频帧，一次前向即可预测点云、深度、法线、相机参数与三维高斯，并能把已知的相机位姿、内参或深度作为额外提示输入。WorldMirror 2.0（2026 年 4 月）作为 HY-World 2.0 的重建模块发布；原论文已被 ICML 2026 接收。
- 实现方式: Transformer 将多视角图像与可选的先验标记（相机位姿、内参、深度）一起编码，再由点云、深度、法线、相机与 3DGS 等任务头解码；腾讯报告称加入先验能提升所有任务的表现。
- 参数: one forward pass · outputs points, depth, normals, cameras, 3DGS · exports to COLMAP
- 能力维度: 实验控制, 创作可及性
- 论文: https://arxiv.org/abs/2510.10726 (ICML 2026)
- 视频: https://github.com/user-attachments/assets/146a9a25-5eb7-4400-aa09-5b58e1d10a5e
- 图片: https://raw.githubusercontent.com/Tencent-Hunyuan/HunyuanWorld-Mirror/main/assets/teaser.jpg
- 项目主页: https://3d-models.hunyuan.tencent.com/world/
- 代码: https://github.com/Tencent-Hunyuan/HunyuanWorld-Mirror

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

#### π³ (Pi3) — 上海人工智能实验室 (2025-07-17)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像, 视频 → 输出: 三维场景 / 世界
- 核心想法: 去掉参考视角之后，随手收集、顺序混乱的素材（例如许多人用手机拍下的同一地点）也能更稳定地被重建。
- 内容: π³ 是上海人工智能实验室开源的前馈式模型：把一组无序的照片或视频帧转换为相机位姿与点图，而不把任何一帧当作参考帧，因此结果与输入顺序无关。它被 ICLR 2026 接收，并与 VGGT 一起被后续重建方法用作骨干网络。
- 实现方式: 完全置换等变的 Transformer，不设参考帧标记，为每个视角预测仿射不变的相机位姿与尺度不变的局部点图。
- 参数: BSD-3 code and weights · ~2.2k GitHub stars (Oct 2026)
- 能力维度: 时间响应性, 创作可及性
- 论文: https://arxiv.org/abs/2507.13347 (ICLR 2026)
- 视频: https://yyfz.github.io/pi3/assets/videos/teaser.mp4
- 项目主页: https://yyfz.github.io/pi3/
- 代码: https://github.com/yyfz/Pi3

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

#### 4RC 随时随地条件查询的 4D 重建（4RC） — Yihang Luo (2026-02-10)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 视频 → 输出: 动态三维 / 4D
- 核心想法: 一次前向就把手机拍的动态场景视频变成可查询的 4D 几何，是把真实事件搬进三维重演的一道采集工序。
- 内容: 南洋理工大学 S-Lab（与牛津大学合作）的前馈模型：一次前向即可从单目视频重建动态场景的稠密几何与运动；视频只需编码一次，之后就能在任意时间点查询任一帧的三维几何。代码已公开。
- 实现方式: Transformer 把整段视频编码为紧凑的时空潜变量；条件解码器可按需查询任一帧在任一目标时刻的三维几何与运动，每个视角的 4D 属性被分解为基础几何加随时间变化的相对运动。
- 能力维度: 持久性, 创作可及性
- 论文: https://arxiv.org/abs/2602.10094 (ICML 2026)
- 视频: https://yihangluo.com/projects/4RC/assets/demo_video.mp4
- 图片: https://yihangluo.com/projects/4RC/assets/framework.png
- 项目主页: https://yihangluo.com/projects/4RC/
- 代码: https://github.com/Luo-Yihang/4RC

#### MotionCrafter — Ruijie Zhu, 腾讯 ARC 实验室 (2026-02-09)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 视频 → 输出: 动态三维 / 4D
- 核心想法: 视频生成模型已经学到了物体如何运动；MotionCrafter 用这些知识去测量真实画面中的运动，而不是生成新的画面。
- 内容: MotionCrafter 输入一段普通视频，为每一帧输出稠密的三维点图，以及每个点的三维运动（场景流），全部位于同一个坐标系中。它入选 CVPR 2026 Highlight，代码、权重与在线演示均已公开。
- 实现方式: 4D VAE 把点图与场景流编码为潜变量，再由微调过的视频扩散骨干根据 RGB 视频预测这些潜变量；作者发现强行让它们与 RGB VAE 潜变量对齐反而有害，因此改用新的归一化方式。
- 参数: +38.6% geometry, +25.0% scene flow vs. prior best (authors)
- 能力维度: 持久性
- 获奖与认可: CVPR 2026 Highlight
- 论文: https://arxiv.org/abs/2602.08961 (CVPR 2026)
- 视频: https://www.youtube.com/watch?v=oc0fRoZTyk8
- 项目主页: https://ruijiezhu94.github.io/MotionCrafter_Page/
- 代码: https://github.com/TencentARC/MotionCrafter

#### D4RT — Chuhan Zhang, 谷歌 DeepMind (2025-12-09)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 视频 → 输出: 动态三维 / 4D, 三维场景 / 世界
- 核心想法: 把拍下的情境变成会动的三维记录只需几秒钟，真实事件因此可以实际地成为可回放 4D 场景的素材，而不再只是实验室里的流程。
- 内容: D4RT 是 Google DeepMind 的一个统一模型：输入一段普通视频，就能给出深度、相机轨迹，以及任意像素在任意时刻的三维位置，把运动中的人和物体作为一个连贯的 4D 场景来追踪。它获得了 CVPR 2026 最佳论文奖；截至 2026 年 10 月，代码和权重仍未公开。
- 实现方式: 编码器-解码器 Transformer 先把整段视频压缩为全局场景表示；轻量解码器再以“像素、源时刻、目标时刻、相机坐标系”为查询，返回该点的三维位置，由同一个模型同时得到深度、追踪与相机估计。
- 参数: 1-min video in ~5 s on one TPU chip · 18–300× faster than prior state of the art (DeepMind)
- 能力维度: 时间响应性, 持久性
- 获奖与认可: CVPR 2026 Best Paper
- 论文: https://arxiv.org/abs/2512.08924 (CVPR 2026)
- 视频: https://storage.googleapis.com/gdm-deepmind-com-prod-public/media/media/D4RT_blog_figure-1-light.mp4
- 图片: https://lh3.googleusercontent.com/ozG6v7VcBOV2eYZ8TnGTAe1Z-7EjkNiBPHxdQEG1wy_F5QwRN_4IJ_jJYMNQiOMHEWyNMZg3tmC00bzGQX0IYfXHMVuoQS6OLptEV-H6CUpIOnWOaQ=w1200-h630-n-nu-rw https://storage.googleapis.com/d4rt_assets/D4RT_capabilities_left.gif
- 项目主页: https://deepmind.google/blog/d4rt-teaching-ai-to-see-the-world-in-four-dimensions/

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

### 体积视频与远程临场

以三维形式捕捉并传输或回放的人：Beam、体积视频工作室、高斯视频。

#### PackUV — Aashish Rai (2026-02-26)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 多视角拍摄 / 扫描 → 输出: 动态三维 / 4D, 高斯泼溅 / 辐射场
- 核心想法: 如果 4D 捕捉只是一叠视频文件，现有的流媒体基础设施就能把录下的人和事件送进头显，而不必另建专用播放系统。
- 内容: PackUV 把 4D 高斯体积视频存成一串打包好的 UV 图像图集，使多相机拍摄的内容可以用普通视频编解码器压缩与传输，并在长达 30 分钟的序列中保持一致。它同时发布了 PackUV-2B 数据集：100 段由 50 台以上同步相机拍摄的序列。
- 实现方式: PackUV-GS 直接在每帧的多尺度 UV 图集中拟合高斯参数，并借助光流引导的动态高斯标注与视频关键帧机制，稳定静态区域、处理大幅运动与遮挡变化。
- 参数: sequences up to 30 min · codec-compatible atlases (e.g. FFV1) · PackUV-2B: 100 sequences, 50+ cameras, 2B frames
- 能力维度: 持久性, 感知真实感
- 论文: https://arxiv.org/abs/2602.23040 (CVPR 2026)
- 视频: https://www.youtube.com/watch?v=tY1J1iRzzow
- 项目主页: https://ivl.cs.brown.edu/packuv

#### A$AP Rocky《HELICOPTER》（4D 捕捉音乐录影带）（A$AP Rocky – HELICOPTER (4D-captured music video)） — Evercoast (2026-01-12)
- 类型: 体验 / 艺术作品 · 时序: 预先生成 · 获取方式: 产品 / 应用
- 输入: 多视角拍摄 / 扫描 → 输出: 平面视频, 动态三维 / 4D
- 核心想法: 一部面向大众的作品把 4D 捕捉的人当作可以事后“重拍”的素材，说明 4D 媒体的捕捉环节已从演示走进商业制作。
- 内容: A$AP Rocky《HELICOPTER》的官方音乐录影带（2026 年 1 月）由 Evercoast 多相机系统捕捉为 4D 高斯泼溅的表演者合成到各个场景中；Evercoast 称片中几乎所有人物都是用其平台拍摄并生成的。
- 实现方式: 表演者在同步多相机阵列上拍摄（据 Radiancefields.com 报道为 56 台相机），再用 Evercoast 的软件（很可能是其 Cloudbreak 服务）重建为 4D 高斯泼溅序列，由视效团队沿新的虚拟镜头路径渲染。
- 参数: 56-camera rig (reported) · 4D Gaussian splat performers
- 能力维度: 感知真实感, 创作可及性
- 视频: https://www.youtube.com/watch?v=GTRbualP7-A
- 项目主页: https://evercoast.com/

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
- 内容: Google Beam 是 Project Starline 的商用后继：AI 模型把多路二维相机画面转换为远端人物的三维渲染，在光场显示屏上呈现，内置于 HP Dimension 显示设备出售。Google 于 2026 年 9 月 23 日表示，Beam 设备已通过 18 家渠道合作伙伴向六个国家（美国、加拿大、英国、法国、德国、日本）的客户发货，并自 2026 年 10 月起可在部分 Industrious 共享办公空间预约使用。
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

#### Volinga：Unreal Engine 中的 4D 高斯泼溅（Volinga 4DGS for Unreal Engine） — Volinga (2026-07-21)
- 类型: 产品 / 应用 · 时序: 预先生成 · 获取方式: 产品 / 应用
- 输入: 多视角拍摄 / 扫描 → 输出: 动态三维 / 4D, 高斯泼溅 / 辐射场
- 核心想法: 捕捉到的动态表演可以像其他资产一样在游戏引擎中摆放、打光和安排时序，4D 录像因此能成为人工编排的交互场景中的一个元素。
- 内容: Volinga 在 2026 年 7 月更新了其套件与 Unreal Engine 插件，使 4D 高斯泼溅捕捉能以时间轴资产的形式在 Unreal 中播放：来自 Gracia、Houdini 等工具的逐帧 PLY 序列被打包为一个压缩的 NVOL 文件，由 Unreal 的 Sequencer 驱动，并支持光照交互、裁剪体积与 OCIO 色彩管理。
- 实现方式: Volinga Suite 把成千上万个逐帧 PLY 转换为一个近乎无损的 NVOL 资产；Volinga Renderer 插件（Unreal Engine 5.8，测试版）通过 Sequencer 轨道播放这些帧，每个场景中的 4DGS 资产数量不设上限。
- 参数: Unreal Engine 5.8 · PLY / SPZ / SOG import · NVOL container · free watermarked trial, then subscriptions
- 能力维度: 创作可及性, 实验控制
- 视频: https://www.youtube.com/watch?v=OQwaF0ihjH4
- 项目主页: https://volinga.ai/

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
- 内容: Spark 是 World Labs 面向 three.js 的开源高斯泼溅渲染器；Spark 2.0（2026 年 4 月）可把超过 1 亿个泼溅的世界流式加载进普通网页。2026 年 9 月 28 日，AMD 同意收购 World Labs（预计 2026 年底完成交割）；Spark 仍采用 MIT 许可证。
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

### 4D 物体生成

由文字、单张图像或视频生成会动的三维物体与角色，以动态高斯或变形网格表示：DreamGaussian4D、L4GM、SV4D……

#### 4DAnyone 单目视频生成 4D 人体（4DAnyone） — Yudong Jin, 蚂蚁灵波科技 (2026-08-20)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 视频 → 输出: 动态三维 / 4D, 高斯泼溅 / 辐射场, 虚拟人（脸 / 身体）
- 核心想法: 一台相机即可得到可自由换视角的人物：缺失的视角靠生成而非拍摄，省去了体积视频的多机位采集环节。
- 内容: 4DAnyone 能把一段随手拍摄的人物单目视频（无需标定、无需绑定骨骼）变成可从任意视角回放的 4D 高斯人体。代码与模型以 Apache-2.0 开源。
- 实现方式: 相机可控的视频扩散模型生成数十路一致的新视角视频，采用“参考上下文打包”（固定长度的参考上下文）与“目标上下文路由”（去噪过程中轮换视角分组），再用 4D 高斯泼溅拟合；训练数据混合了游戏引擎数据集 MVGameHuman、光场舞台数据与真实视频。
- 能力维度: 感知真实感, 创作可及性
- 论文: https://arxiv.org/abs/2608.20335 (SIGGRAPH Asia 2026)
- 视频: https://4danyone.github.io/assets/videos/teaser.mp4
- 图片: https://4danyone.github.io/assets/images/social-card.jpg
- 项目主页: https://4danyone.github.io/
- 代码: https://github.com/ant-research/4DAnyone

#### Lift4D 野外单目视频 4D 重建与补全（Lift4D） — Yehonathan Litman (2026-06-22)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 视频 → 输出: 动态三维 / 4D, 高斯泼溅 / 辐射场
- 核心想法: 生成式先验弥补了单个相机所见与完整 4D 物体之间的差距，这是把真实运动物体带进三维场景所需的一步。
- 内容: Lift4D 把一段随手拍摄的形变动物或物体单目视频变成完整的运动三维高斯模型，并补全相机从未拍到的那一侧。
- 实现方式: 通过因果潜变量条件改造单视角三维重建模型，得到时间上一致的逐帧形状，用来初始化可形变三维高斯；再在遮挡感知的优化中对照视频细化，并用视角条件扩散先验补全未见区域。
- 能力维度: 感知真实感, 持久性
- 论文: https://arxiv.org/abs/2606.23688 (SIGGRAPH Asia 2026)
- 视频: https://lift4d.github.io/static/videos/teaser_wide.mp4
- 项目主页: https://lift4d.github.io/
- 代码: https://github.com/yehonathanlitman/Lift4D

#### NeuROK 生成式 4D 神经物体运动学（NeuROK） — Chen Geng (2026-05-28)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 多视角拍摄 / 扫描, 键盘与手柄动作 → 输出: 动态三维 / 4D
- 核心想法: 扫描下来的房间也能“摸得着”：物体被作用时会合理地弯曲、晃动，而不必为每件物体手工搭建物理装置。
- 内容: 斯坦福大学的模型：把静态三维物体（包括用智能手机扫描的物体）变成可交互的 4D 资产，在给定的初始物理条件下产生合理的形变，不需要物理标注，也不对物体类别做结构假设；演示中，扫描得到的办公室和厨房里的物体都能对交互做出反应。
- 实现方式: 在大规模整理的 4D 数据集上训练 Transformer 编码—解码器，学习物体所有可能形变状态的潜空间，以及从潜变量到形变形状的解码器；随后从拉格朗日力学出发，在这一低维潜空间中以常微分方程求解来模拟动力学。
- 能力维度: 行为似真性, 反应性
- 论文: https://arxiv.org/abs/2605.30347 (CVPR 2026)
- 视频: https://chen-geng.com/neurok/static/videos/demos/office2.mp4
- 图片: https://chen-geng.com/neurok/static/og-card.jpg
- 项目主页: https://chen-geng.com/neurok

#### R-DMesh 视频引导的三维动画（R-DMesh） — Zijie Wu, 腾讯混元 (2026-05-13)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 视频 → 输出: 动态三维 / 4D, 网格 / 三维资产
- 核心想法: 视频成为任意三维资产的动作控制手柄：先拍摄或生成动作，再迁移到网格上。
- 内容: 腾讯混元的 R-DMesh 能让用户提供的静态三维网格跟随参考视频中的动作运动，即使网格的初始姿态与视频首帧不一致也能对齐。代码与权重已于 2026 年 5 月发布。
- 实现方式: VAE 把输入分解为基础网格、相对运动轨迹以及一个学习得到的“校正跳变”偏移，先把网格移到视频的起始姿态；再由以预训练视频潜变量为条件的整流流扩散 Transformer 生成运动，训练数据为包含 50 多万条动态网格序列的 Video-RDMesh。
- 能力维度: 创作可及性, 实验控制
- 论文: https://arxiv.org/abs/2605.13838 (SIGGRAPH 2026)
- 视频: https://www.youtube.com/watch?v=xBrMjPnH3_w
- 图片: https://r-dmesh.github.io/assets/pipeline.png
- 项目主页: https://r-dmesh.github.io/
- 代码: https://github.com/Tencent-Hunyuan/R-DMesh

#### ActionMesh 动画三维网格生成（ActionMesh） — Remy Sabathier, Meta (2026-01-22)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 视频, 文字提示, 图像 → 输出: 动态三维 / 4D, 网格 / 三维资产
- 核心想法: 生成的 4D 结果以普通动画网格的形式在大约一分钟内交付，正是游戏引擎与 XR 工具早已在用的格式。
- 内容: Meta 的 ActionMesh 能把一段短视频、一张图像或一句文字（也可以是一个三维网格加一句动作描述）变成拓扑固定的动画三维网格，可以贴图、重定向并导入常规三维软件。代码、权重和 Hugging Face 演示均以 Meta 的许可证公开。
- 实现方式: “时序三维扩散”：在现有三维扩散模型上加入时间轴，生成逐帧形状的同步潜变量，再由时序三维自编码器把它们转换为同一参考网格的形变，得到无需骨骼、拓扑一致的动画。
- 参数: ≈45–75 s per animation on one H100 (developer figures) · 12 GB VRAM low-RAM mode · ActionBench: 128 video–animated point-cloud pairs
- 能力维度: 创作可及性, 时间响应性, 持久性
- 论文: https://arxiv.org/abs/2601.16148 (CVPR 2026)
- 视频: https://www.youtube.com/watch?v=Uc_CL_D8KiU
- 图片: https://remysabathier.github.io/actionmesh/videos/thumbnail/actionmesh.gif
- 项目主页: https://remysabathier.github.io/actionmesh/
- 代码: https://github.com/facebookresearch/actionmesh

#### Motion 3-to-4 由三维动作重建实现 4D 合成（Motion 3-to-4） — Hongyuan Chen (2026-01-20)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 视频 → 输出: 动态三维 / 4D, 网格 / 三维资产
- 核心想法: 把“物体是什么”和“它怎么动”分开，任何一段动作视频都能拿来驱动给定的三维资产。
- 内容: 西湖大学的前馈模型：输入一段运动物体的单目视频（可选再加一个该物体的三维网格），输出动画网格；它只生成或读取一次形状，再逐帧重建顶点运动，因此从任何角度看几何都保持一致。代码已公开。
- 实现方式: 把 4D 合成拆分为静态三维形状生成与动作重建：在标准参考网格上，用紧凑的动作潜变量预测逐帧顶点轨迹，逐帧 Transformer 可处理不同长度的序列。
- 能力维度: 持久性, 创作可及性
- 论文: https://arxiv.org/abs/2601.14253 (CVPR 2026)
- 视频: https://motion3-to-4.github.io/static/videos/animation/fox.mp4
- 图片: https://motion3-to-4.github.io/static/images/motion324.png
- 项目主页: https://motion3-to-4.github.io/
- 代码: https://github.com/Inception3D/Motion324

#### SS4D 基于结构化时空潜变量的原生 4D 生成（SS4D） — Zhibing Li, 上海人工智能实验室 (2025-12-16)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 视频 → 输出: 动态三维 / 4D
- 核心想法: 手机拍下的运动物体视频，经一次模型推理就能变成可从任意角度观看的 4D 资产，不必再为每个物体花数小时优化。
- 内容: 香港中文大学与上海人工智能实验室的原生 4D 生成模型：把一段运动物体的单目视频直接转换为动态三维物体；它直接在 4D 数据上训练，而不是针对每个物体去优化三维或视频模型。代码与权重以 MIT 许可证开放。
- 实现方式: 在预训练的单图生三维生成器上加入结构化时空潜变量：专门的时间层跨帧推理，分解式 4D 卷积与时间下采样压缩长序列，训练策略增强对遮挡的鲁棒性。
- 参数: MIT code and weights
- 能力维度: 持久性, 感知真实感
- 论文: https://arxiv.org/abs/2512.14284 (SIGGRAPH Asia 2025 (ACM TOG))
- 视频: https://lizb6626.github.io/SS4D/static/videos/ss4d_demo_video.mp4
- 图片: https://lizb6626.github.io/SS4D/static/images/overview.png
- 项目主页: https://lizb6626.github.io/SS4D/
- 代码: https://github.com/Lizb6626/SS4D

#### ShapeGen4D 从视频生成高质量 4D 形状（ShapeGen4D） — Jiraphon Yenphraphai, Snap Inc. (2025-10-07)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 视频 → 输出: 动态三维 / 4D, 网格 / 三维资产
- 核心想法: 会拉伸、分裂或合并的物体也能从视频提升为 4D，而这些正是骨骼动画应付不了的情形。
- 内容: Snap Research（与普渡大学、阿卜杜拉国王科技大学合作）的模型：从单目视频端到端生成带纹理的网格序列，能捕捉非刚性运动、体积变化乃至拓扑变化，无需逐帧优化。截至 2026 年 10 月未公开代码。
- 实现方式: 在大型预训练三维生成器上加入覆盖全部帧的时间注意力、时间感知的点采样与 4D 潜变量锚定，以保持几何和纹理一致，并在各帧之间共享噪声以提高稳定性。
- 能力维度: 感知真实感, 持久性
- 论文: https://arxiv.org/abs/2510.06208 (ICLR 2026)
- 视频: https://shapegen4d.github.io/assets/teaser5.mp4
- 图片: https://shapegen4d.github.io/assets/method_v4.jpg
- 项目主页: https://shapegen4d.github.io/

#### 高斯变化场扩散（GVFDiffusion）视频生成 4D（Gaussian Variation Field Diffusion (GVFDiffusion)） — Bowen Zhang, 微软 (2025-07-31)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 视频 → 输出: 动态三维 / 4D, 高斯泼溅 / 辐射场
- 核心想法: 原生 4D 扩散模型：生成发生在压缩后的三维高斯动画空间中，而不是为每个物体蒸馏视频模型。
- 内容: 把一段物体运动的单目视频（例如一个奔跑的角色）变成可从各个方向观看的动画三维高斯物体；也能按照视频为现有三维模型添加动画。
- 实现方式: 4DMesh-to-GS 变化场 VAE 把 Objaverse 动画物体的规范高斯及其逐帧变化编码为紧凑潜变量，再由以输入视频和规范高斯为条件的时序扩散 Transformer 生成这些潜变量。
- 能力维度: 感知真实感, 创作可及性
- 论文: https://arxiv.org/abs/2507.23785 (ICCV 2025)
- 视频: https://www.youtube.com/watch?v=u1SzuKIYAsE
- 图片: https://gvfdiffusion.github.io/static/images/Pipeline.jpg
- 项目主页: https://gvfdiffusion.github.io/
- 代码: https://github.com/ForeverFancy/GVFDiffusion

#### AnimateAnyMesh 文本驱动的网格动画（AnimateAnyMesh） — Zijie Wu (2025-06-11)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 文字提示 → 输出: 动态三维 / 4D, 网格 / 三维资产
- 核心想法: 网格动画变成“输入提示、等几秒”的一步，让生成场景中的动态道具可以低成本地变换。
- 内容: AnimateAnyMesh 能在几秒内根据文字提示为任意三维网格生成动画（例如让一条龙扇动翅膀），无需绑定骨骼，也无需逐物体优化。
- 实现方式: DyMeshVAE 把动态网格序列压缩为潜在轨迹并保留局部拓扑，再由整流流模型根据文字生成这些潜变量；训练数据为 DyMesh 数据集，作者称其包含 400 多万条带文字标注的动态网格序列。
- 参数: a few seconds per animation (developer claim) · arbitrary mesh topology
- 能力维度: 创作可及性, 时间响应性
- 论文: https://arxiv.org/abs/2506.09982 (ICCV 2025)
- 视频: https://www.youtube.com/watch?v=q8xH9B0S4y0
- 图片: https://animateanymesh.github.io/AnimateAnyMesh/img/AnimateAnyMesh.png
- 项目主页: https://animateanymesh.github.io/AnimateAnyMesh/
- 代码: https://github.com/JarrentWu1031/AnimateAnyMesh

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

#### Animate3D 为任意三维模型生成动画（Animate3D） — Yanqin Jiang (2024-07-16)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 文字提示 → 输出: 动态三维 / 4D, 高斯泼溅 / 辐射场
- 核心想法: 把 4D 生成当作给现有资产添加动画的一道工序，而不是从零生成新物体。
- 内容: Animate3D 以现有的静态三维模型和一句文字提示为输入，让模型动起来，并在各个视角下保持外观与形状一致。
- 实现方式: 以静态物体的多视角渲染为条件、在新建的多视角视频数据集 MV-Video 上训练的多视角视频扩散模型（MV-VDM）生成一致的运动；先从这些视频中重建运动，再用 4D 分数蒸馏细化。
- 能力维度: 创作可及性, 持久性
- 论文: https://arxiv.org/abs/2407.11398 (NeurIPS 2024)
- 视频: https://www.youtube.com/watch?v=qkaeeGzLnY8
- 项目主页: https://animate3d.github.io/
- 代码: https://github.com/yanqinJiang/Animate3D

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

#### PhysDreamer 基于物理的三维物体交互（PhysDreamer） — Tianyuan Zhang, Hong-Xing (Koven) Yu (2024-04-19)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 多视角拍摄 / 扫描, 键盘与手柄动作 → 输出: 动态三维 / 4D, 高斯泼溅 / 辐射场
- 核心想法: 把视频模型当作物理属性的来源，使生成的运动成为人的动作的后果，而不是一段固定的片段。
- 内容: PhysDreamer 让一个捕捉得到的三维物体（例如花或盆栽）在被戳、被拉时作出物理响应：它会摇摆、弯曲再弹回，这种动态是从视频生成模型中学来的。
- 实现方式: 先用视频生成模型让静态三维高斯物体的渲染图动起来，再优化空间变化的材料场（杨氏模量），使可微物质点法（MPM）仿真与该视频一致，之后即可仿真新的外力；真实感通过用户研究评估。
- 能力维度: 反应性, 行为似真性
- 论文: https://arxiv.org/abs/2404.13026 (ECCV 2024)
- 视频: https://physdreamer.github.io/assets/videos/teaser_videos/teaser_video_morph.mp4
- 图片: https://physdreamer.github.io/assets/thumbnails/red_rose.png
- 项目主页: https://physdreamer.github.io/
- 代码: https://github.com/a1600012888/PhysDreamer

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

#### Align Your Gaussians 动态高斯文本生成 4D（Align Your Gaussians (AYG)） — Huan Ling, 英伟达 (2023-12-21)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 文字提示 → 输出: 动态三维 / 4D, 高斯泼溅 / 辐射场
- 核心想法: 高斯表示的 4D 内容可以像片段一样组合：分别生成的运动物体可以放进同一个场景。
- 内容: 英伟达的 Align Your Gaussians 把文字提示变成由运动高斯组成的动画三维物体，还能把多段动画串联、组合成包含多个角色的更长场景。
- 实现方式: 以带形变场的动态三维高斯为表示，用文生图、多视角与文生视频模型（VideoLDM）的组合分数蒸馏进行优化，对高斯运动加入正则，并以自回归方式延长序列。
- 能力维度: 创作可及性, 情境多样性
- 论文: https://arxiv.org/abs/2312.13763 (CVPR 2024)
- 视频: https://research.nvidia.com/labs/toronto-ai/AlignYourGaussians/assets/4d_scenes/christmas_composed.mp4
- 图片: https://research.nvidia.com/labs/toronto-ai/AlignYourGaussians/assets/figures/ayg_paper_preview.png
- 项目主页: https://research.nvidia.com/labs/toronto-ai/AlignYourGaussians/

#### 4D-fy 文本生成 4D（4D-fy） — Sherwin Bahmani (2023-11-29)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 文字提示 → 输出: 动态三维 / 4D
- 核心想法: 文本到 4D 需要同时向多个“老师”学习：图像模型管外观，多视角模型管形状，视频模型管运动。
- 内容: 4D-fy 能根据一句文字提示生成一段会动的三维场景（例如一只开车的熊），在播放时可以从任意角度观看。
- 实现方式: 以多分辨率哈希编码的 4D 辐射场为表示，针对每个提示用“混合分数蒸馏”优化，交替使用文生图、三维感知多视角与文生视频扩散模型的梯度。
- 能力维度: 感知真实感, 创作可及性
- 论文: https://arxiv.org/abs/2311.17984 (CVPR 2024)
- 视频: https://sherwinbahmani.github.io/4dfy/data/videos/ours/a_bear_driving_a_car.mp4
- 图片: https://sherwinbahmani.github.io/4dfy/data/method.png
- 项目主页: https://sherwinbahmani.github.io/4dfy/
- 代码: https://github.com/sherwinbahmani/4dfy

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

### 4D 场景与世界生成

借助视频先验生成或补全的运动场景与世界，可随时间推移从新视角观看：CAT4D、4Real、4DNeX、BulletGen……

#### OuroWorld 让三维世界变成循环动态照片（OuroWorld） — You-Zhe Xie, Alaya Lab (2026-10-08)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 多视角拍摄 / 扫描 → 输出: 动态三维 / 4D, 高斯泼溅 / 辐射场
- 核心想法: 让静止的生成世界“活”起来的低成本办法：无缝循环的环境运动给场景加入时间，而不需要完整的世界模型。
- 内容: OuroWorld 以一个静态三维高斯世界（例如由 Marble 或 Lyra 2.0 生成的世界）为输入，让它变成无限循环的三维动态照片：水流动、植物摇曳、光线变化，可从任意位置观看。
- 实现方式: 视觉语言模型推断合理的动态并引导视频模型生成参考视频，再提升并补全为多视角视频；随后拟合一个对不一致具有鲁棒性的周期性 4D 高斯模型，其傅里叶级数形变场保证循环，锚定参考视角的漂移场吸收视角间的不一致。
- 能力维度: 感知真实感, 情境多样性
- 论文: https://arxiv.org/abs/2610.12461 (arXiv 2026)
- 视频: https://www.youtube.com/watch?v=QCJ4u7f3K-8
- 图片: https://ouroworld.userwei.com/og.jpg
- 项目主页: https://ouroworld.userwei.com/
- 代码: https://github.com/youzhe0305/OuroWorld

#### GS-Agent 以生成式仿真构建 4D 物理世界（GS-Agent） — Hongxin Zhang (2026-07-23)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 文字提示 → 输出: 动态三维 / 4D, 三维场景 / 世界
- 核心想法: 它不是去预测世界“看起来”该是什么样，而是搭建一个遵守物理规律、改一个参数就能重跑的世界，这正是实验所需要的。
- 内容: 麻省大学阿默斯特分校与 Genesis AI 的多智能体系统：根据一段文字描述，为物理仿真器编写代码来构建动态三维世界——智能体负责挑选和摆放资产、调整材质、编排运动、设置镜头与灯光，然后运行仿真，让液体、可变形物体与刚体发生符合物理的交互。由于输出是仿真而非像素，每一帧的几何都保持一致；作者将其与 Sora 2 和 Wan 2.2 做了对比。
- 实现方式: 分工不同的大语言模型智能体（资产挑选、材质调整、摆放、运动控制、镜头与灯光）通过代码与物理引擎交互，查看渲染结果的多模态反馈并反复迭代，直到仿真过程符合文字描述。
- 能力维度: 实验控制, 行为似真性, 创作可及性
- 论文: https://arxiv.org/abs/2607.21522 (arXiv 2026)
- 视频: https://umass-embodied-agi.github.io/gs-agent/static/videos/teaser/1_rgb.mp4
- 项目主页: https://umass-embodied-agi.github.io/gs-agent/

#### World from Motion 单目视频的生成式动态高斯重建（World from Motion） — Liyuan Zhu, 英伟达 (2026-07-01)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 视频 → 输出: 动态三维 / 4D, 高斯泼溅 / 辐射场
- 核心想法: 一段手持拍摄的视频就能变成可以绕着走的 4D 场景，看不到的那一面由视频模型补上，而不是留下空洞。
- 内容: NVIDIA 与斯坦福大学的方法：把一段普通的动态场景单目视频（例如街道、商店或舞者）转换为可从新视角渲染的动态三维高斯场景；以初始重建为条件的视频模型负责补全看不到的区域、修正瑕疵，其输出再蒸馏回同一个一致的 4D 表示。项目主页提供了可在浏览器中查看结果的查看器。
- 实现方式: 视频生成器以沿输入与目标相机路径渲染的外观、几何和三维场景运动等稠密像素对齐图为条件；用带有模拟单目重建瑕疵的对齐多视角视频对训练，再把它为新视角生成的画面蒸馏进同一个动态 3DGS。
- 能力维度: 持久性, 感知真实感
- 论文: https://arxiv.org/abs/2607.01202 (NeurIPS 2026)
- 视频: https://research.nvidia.com/labs/amri/projects/world-from-motion/videos_compressed/talk/world_from_motion_talk.mp4
- 图片: https://research.nvidia.com/labs/amri/projects/world-from-motion/thumbnails/og_image.jpg
- 项目主页: https://research.nvidia.com/labs/amri/projects/world-from-motion/

#### InSpatio-World 实时 4D 世界模拟器（InSpatio-World） — InSpatio 空间智能 (2026-04-08)
- 类型: 模型 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 视频, 镜头路径 / 位姿 → 输出: 交互式帧流, 动态三维 / 4D
- 核心想法: 从视频素材实时得到 4D：一次被录下的事件变成可以重新进入、从新位置观看的地方，同时生成始终锚定原视频。
- 内容: InSpatio-World 能把单段参考视频变成可实时漫游的动态场景：人可以一边改变视角，一边暂停、放慢或倒放时间。1.3B 权重（Apache-2.0）与网页演示均已公开。
- 实现方式: 基于 Wan2.1 的时空自回归（STAR）视频模型以参考视频沿用户路径渲染的深度点云为条件，维护参考帧与历史帧的隐式时空缓存，并通过联合分布匹配蒸馏（JDMD）实现实时生成。
- 参数: 1.3B open weights · real-time navigation · first among real-time methods on WorldScore-Dynamic (developer claim)
- 能力维度: 时间响应性, 持久性, 情境可达性
- 论文: https://arxiv.org/abs/2604.07209 (arXiv 2026)
- 视频: https://inspatio.github.io/inspatio-world/static/videos/0311_ar_14B_ema_grid9_0.mp4
- 项目主页: https://inspatio.github.io/inspatio-world/
- 代码: https://github.com/inspatio/inspatio-world

#### NeoVerse 基于真实单目视频的 4D 世界模型（NeoVerse） — Yuxue Yang (2026-01-01)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 视频, 镜头路径 / 位姿 → 输出: 动态三维 / 4D, 平面视频
- 核心想法: 用日常单目视频而非稀缺的多视角采集数据训练 4D 世界模型，扩大了它能处理的场景范围。
- 内容: NeoVerse 能把一段普通单目视频重建为运动的 4D 场景，并沿原视频从未走过的相机路径生成新视频，例如子弹时间镜头。代码与权重以 Apache-2.0 开源。
- 实现方式: 先对输入视频进行无需位姿的前馈式 4D 重建并沿新轨迹渲染，再由训练时在线模拟单目退化模式的视频扩散模型把渲染结果变成干净的新轨迹视频。
- 能力维度: 情境可达性, 持久性
- 获奖与认可: CVPR 2026 Highlight; Best Paper, VideoWorldModel Workshop
- 论文: https://arxiv.org/abs/2601.00393 (CVPR 2026)
- 视频: https://www.youtube.com/watch?v=1k8Ikf8zbZw
- 图片: https://neoverse-4d.github.io/resources/teaser.png
- 项目主页: https://neoverse-4d.github.io/
- 代码: https://github.com/IamCreateAI/NeoVerse

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

#### 4Real-Video-V2 4D 场景生成（4Real-Video-V2） — Chaoyang Wang, Snap Inc. (2025-06-18)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 文字提示, 多视角拍摄 / 扫描 → 输出: 动态三维 / 4D, 高斯泼溅 / 辐射场, 平面视频
- 核心想法: 4Real（2024）与 4Real-Video（CVPR 2025）的后续：无需逐场景优化的 4D 场景生成，从提示直接得到动态高斯。
- 内容: Snap Research 的 4Real-Video-V2 能根据文字提示生成运动场景（也可为捕捉的三维场景或资产添加动画），输出“视角 × 时间”的视频网格，并通过一次前向把每个时间步提升为三维高斯。
- 实现方式: 4D 视频扩散模型采用融合的视角—时间稀疏注意力（token 只关注同一帧、同一时刻或同一视角的 token，不给基础视频模型增加参数）生成网格，再由带高斯头的前馈重建模型恢复相机与逐帧高斯。
- 能力维度: 感知真实感, 持久性
- 论文: https://arxiv.org/abs/2506.18839 (arXiv 2025)
- 视频: https://snap-research.github.io/4Real-Video-V2/supp_demo/4real-video-v2-teaser.mp4
- 项目主页: https://snap-research.github.io/4Real-Video-V2/

#### WonderPlay 由单图与动作生成动态三维场景（WonderPlay） — Zizhang Li, Hong-Xing (Koven) Yu (2025-05-23)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像, 键盘与手柄动作 → 输出: 动态三维 / 4D, 三维场景 / 世界
- 核心想法: 把物理求解器与视频生成器结合，让生成的三维场景有“后果”而不只是运动，更接近一个情境而非一段片段。
- 内容: WonderPlay 能把一张图像变成会对动作作出反应的三维场景：人可以加一阵风、推一下玻璃杯或倒入蜂蜜，场景中的布料、液体、烟雾或刚体随之运动。
- 实现方式: 混合生成式模拟器：物理求解器针对输入动作预测粗略的三维动态，以此为条件让视频生成器生成真实运动，再用生成的视频循环更新动态三维场景。
- 能力维度: 反应性, 行为似真性
- 获奖与认可: ICCV 2025 Highlight
- 论文: https://arxiv.org/abs/2505.18151 (ICCV 2025)
- 视频: https://www.youtube.com/watch?v=vzO4VyBE7T0
- 图片: https://kyleleey.github.io/WonderPlay/assets/teaser/full_scene.jpg
- 项目主页: https://kyleleey.github.io/WonderPlay/
- 代码: https://github.com/kyleleey/WonderPlay

#### Free4D 免训练 4D 场景生成（Free4D） — Tianqi Liu (2025-03-26)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像, 文字提示 → 输出: 动态三维 / 4D, 高斯泼溅 / 辐射场
- 核心想法: 把现有的图生视频与多视角模型蒸馏成一致的 4D 场景，使场景级 4D 不必等待大规模 4D 训练数据。
- 内容: Free4D 能从一张图像或一句文字构建 4D 高斯场景，让静态画面动起来，并可在运动过程中从新视角探索，且无需训练专门模型。
- 实现方式: 先用图生视频模型让图像动起来并初始化粗略的 4D 结构；再通过自适应引导与潜变量替换生成一致的多视角视频，最后以基于调制的细化优化 4D 高斯表示。
- 能力维度: 创作可及性, 持久性
- 论文: https://arxiv.org/abs/2503.20785 (ICCV 2025)
- 视频: https://www.youtube.com/watch?v=GpHnoSczlhA
- 项目主页: https://free4d.github.io
- 代码: https://github.com/TQTQliu/Free4D

#### Aether 几何感知的统一世界模型（Aether） — Haoyi Zhu, 上海人工智能实验室 (2025-03-24)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像, 镜头路径 / 位姿 → 输出: 动态三维 / 4D, 平面视频
- 核心想法: 一个预测结果自带 4D 几何的世界模型，它“想象”出的内容可以在三维中检查和度量，而不只是看像素。
- 内容: 上海人工智能实验室的 Aether 是一个开源世界模型：能把视频重建为带相机轨迹的运动三维几何，根据图像与相机轨迹预测未来视频，并在起始图像与目标图像之间规划路径。
- 实现方式: 对视频扩散模型（CogVideoX）进行后训练，使其联合输出视频、深度与相机射线图，用于重建、动作条件预测与目标条件规划；只使用合成 4D 数据，作者称可零样本迁移到真实视频。
- 能力维度: 实验控制, 行为似真性
- 获奖与认可: ICCV 2025 RIWM workshop Outstanding Paper
- 论文: https://arxiv.org/abs/2503.18945 (ICCV 2025)
- 视频: https://www.youtube.com/watch?v=BGj3BIbZ74A
- 项目主页: https://aether-world.github.io/
- 代码: https://github.com/InternRobotics/Aether

#### CityDreamer4D 无边界 4D 城市生成（CityDreamer4D） — Haozhe Xie (2025-01-15)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 场景规格、代码与规则 → 输出: 动态三维 / 4D, 三维场景 / 世界
- 核心想法: 把城市拆分为静态背景与动态参与者，使车流可以变化而地点保持不变，为街道尺度的生成情境提供了模板。
- 内容: CityDreamer4D 能生成无边界的 4D 城市，包含建筑、道路与行驶中的车流，相机可以在车辆行驶时于其中飞行穿梭。
- 实现方式: 组合式神经场：建筑、道路、背景与车辆实例各有生成器，由鸟瞰布局与交通场景驱动，在 OpenStreetMap、Google Earth 与 CityTopia 数据集上训练。
- 能力维度: 情境可达性, 情境多样性
- 论文: https://arxiv.org/abs/2501.08983 (IEEE TPAMI 2026)
- 视频: https://www.youtube.com/watch?v=PF6W0Nd27Tk
- 图片: https://www.infinitescript.com/projects/CityDreamer4D/CityDreamer4D-Thumbnail.webp
- 项目主页: https://haozhexie.com/project/city-dreamer-4d
- 代码: https://github.com/hzxie/CityDreamer4D

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

#### DimensionX 单图生成三维与 4D 场景（DimensionX） — Wenqiang Sun (2024-11-07)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像 → 输出: 动态三维 / 4D, 高斯泼溅 / 辐射场, 平面视频
- 核心想法: 在同一个视频模型中把“移动相机”与“让时间流逝”分开，就能以较低成本把任意图像变成三维或 4D 场景。
- 内容: DimensionX 能把一张照片变成三维场景（相机移动、时间静止）或 4D 场景（时间流动、可从多个角度观看），并重建为高斯泼溅。
- 实现方式: ST-Director 在 CogVideoX-5B 图生视频模型上训练维度感知的 LoRA，分别控制空间与时间变化；生成的视角集合再被重建为三维或 4D 高斯。
- 能力维度: 创作可及性, 情境多样性
- 论文: https://arxiv.org/abs/2411.04928 (ICCV 2025)
- 视频: https://www.youtube.com/watch?v=ViDQI1HMY2U
- 图片: https://chenshuo20.github.io/DimensionX/DimensionX/images/woman.png
- 项目主页: https://chenshuo20.github.io/DimensionX/
- 代码: https://github.com/wenqsun/DimensionX

#### GenXD 生成任意三维与 4D 场景（GenXD） — Yuyang Zhao, 微软 (2024-11-04)
- 类型: 模型 · 时序: 预先生成 · 获取方式: 开源权重 / 代码
- 输入: 图像, 镜头路径 / 位姿 → 输出: 动态三维 / 4D, 三维场景 / 世界, 平面视频
- 核心想法: 一个模型同时学习静态扫描和日常视频，4D 数据稀缺的问题因此缓解不少。
- 内容: 新加坡国立大学与微软的模型：根据一张或多张图像生成静态三维场景或运动的 4D 场景，输出沿指定镜头路径的视频和一致的多视角画面，可再提升为三维或 4D 高斯表示。它还发布了从视频中挖掘得到的真实世界 4D 场景数据集 CamVid-30K；代码、模型与数据均已公开。
- 实现方式: 数据整理流程从视频中估计相机位姿与物体运动强度，构建 CamVid-30K；多视角—时间模块把相机运动与物体运动解耦，使同一个扩散模型可以同时用三维和 4D 数据训练，掩码潜变量条件则支持任意数量的输入视角。
- 参数: CamVid-30K dataset · Apache-2.0 code
- 能力维度: 情境多样性, 持久性
- 论文: https://arxiv.org/abs/2411.02319 (ICLR 2025)
- 视频: https://gen-x-d.github.io/materials/figures/teaser.mp4
- 图片: https://gen-x-d.github.io/materials/figures/icon.jpg
- 项目主页: https://gen-x-d.github.io/
- 代码: https://github.com/HeliosZhao/GenXD

#### 4DiM 用扩散模型控制空间与时间（4DiM） — Daniel Watson, 谷歌 DeepMind (2024-07-10)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 图像, 镜头路径 / 位姿 → 输出: 动态三维 / 4D, 图像 / 全景图
- 核心想法: 把相机位姿与时间作为同一扩散模型的两个独立控制量，这正是后来的 4D 场景生成器采用的基本接口。
- 内容: Google DeepMind 的 4DiM 能根据一张或几张照片，在任意指定的相机位置与时间点生成真实场景的新视角画面，例如让相机在房间中移动，或为一段视频换一个角度。
- 实现方式: 级联扩散模型以输入图像、相机位姿和时间戳为条件，在带位姿的三维数据、带位姿的视频（4D）与无位姿视频上联合训练，并用单目度量深度把运动恢复结构得到的位姿校准到真实尺度。
- 能力维度: 实验控制, 持久性
- 论文: https://arxiv.org/abs/2407.07860 (ICLR 2025)
- 图片: https://4d-diffusion.github.io/new_samples/banner/table.gif https://4d-diffusion.github.io/new_samples/sv_reangle/hyp.gif
- 项目主页: https://4d-diffusion.github.io

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

## 智能体与模拟社会

由语言模型驱动、在世界中记忆、计划与行动的角色与群体：生成情境里“社会”的一面。

### 生成式智能体与社会模拟

带记忆与反思的可信智能体，从 Smallville 到整个人群的模拟。

#### Emergence World — Emergence AI (2026-05-14)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入: 场景规格、代码与规则, 文字提示 → 输出: 智能体行为与动作, 对话 / 文本
- 核心想法: 持续数周、全程记录的智能体社会，让行为漂移、从众与崩溃变得可以测量；而同一个人设的表现，会随与它共处同一世界的模型不同而改变。
- 内容: 一个持续运行的大语言模型智能体小镇：智能体拥有记忆、日记与人际关系，可使用 120 多种工具，能修订自己的宪章，并受能量经济约束，还接入了纽约实时天气与新闻。在 Emergence AI 的第一项研究中，五个各有 10 名智能体、只在底层模型上不同的世界，在 15 天内走向截然不同的结局：有的世界没有一起犯罪记录，有的多达数百起；第二季（2026 年 9 月）又向其中投放了错误信息与提示注入攻击。
- 实现方式: 与模型无关的多智能体模拟：40 多个地点，每个智能体有情景记忆、反思日记与关系状态三种记忆，三层工具目录，提案需 70% 赞成才通过，能量随时间衰减；多个平行世界从相同条件出发，只改变底层基础模型，并记录每一个动作。
- 参数: 10 agents per world · 40+ locations · 120+ tools · 15–16-day runs · Season 2: 8 worlds, >850,000 LLM calls
- 能力维度: 持久性, 实验控制, 行为似真性
- 论文: https://arxiv.org/abs/2606.08367 (arXiv)
- 视频: https://www.youtube.com/watch?v=fbDd_ph305Q
- 图片: https://images.squarespace-cdn.com/content/69af1b77df627e3fed4f484d/d2931bac-6772-4a44-b382-c21f0b645f82/Emergence-World.jpg
- 项目主页: https://www.emergence.ai/blog/emergence-world-a-laboratory-for-evaluating-long-horizon-agent-autonomy
- 代码: https://github.com/EmergenceAI/Emergence-World

#### Simile — Simile, Joon Sung Park (2026-02-12)
- 类型: 平台 / API · 时序: 回合制 · 获取方式: 产品 / 应用
- 输入: 文字提示 → 输出: 对话 / 文本, 智能体行为与动作
- 核心想法: 人群模拟已经成为产品；它的准确性声明，正是行为研究者把这类“数字孪生”当作被试之前必须检验的内容。
- 内容: 一个商业平台，用访谈与问卷数据构建的智能体，模拟真实客户群体对产品发布、价格调整或营销活动的反应，延续斯坦福 1,000 人研究的思路。2026 年 7 月，Simile 以 20 亿美元投后估值融资逾 2 亿美元，并称已建成人类行为基础模型，以及可预测每次模拟准确度的置信度模型。
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

#### Centaur：人类认知基础模型（Centaur） — Marcel Binz (2024-10-26)
- 类型: 模型 · 时序: 回合制 · 获取方式: 开源权重 / 代码
- 输入: 文字提示 → 输出: 智能体行为与动作
- 核心想法: 一个可用于任何能写成文字的实验的“模拟被试”；它让生成情境的预实验变得廉价，但与群体平均一致，并不等于能代表任何一个具体的人。
- 内容: 一个经过微调、能逐个试次预测人在心理学实验中如何行动的语言模型：只要用自然语言描述实验，它就能像被试一样作出选择。《自然》论文（2025 年 7 月）报告，它对未参与训练的被试的预测优于现有认知模型，并能推广到新的情境设定、任务变化与新领域。
- 实现方式: 在 Psych-101 上用 QLoRA 微调 Llama 3.1 70B；Psych-101 把 160 项实验（6 万多名被试、1,000 多万次选择）的逐试次数据转写成自然语言；评估包括未参与训练的被试、修改后的任务以及与人类神经活动的对齐程度。
- 参数: Llama 3.1 70B + QLoRA · Psych-101: 160 experiments, 60,000+ participants, 10M+ choices
- 能力维度: 行为似真性, 情境可达性, 实验控制
- 论文: https://doi.org/10.1038/s41586-025-09215-4 (Nature 2025)
- 视频: https://www.youtube.com/watch?v=dndPhyJJcTE
- 项目主页: https://www.nature.com/articles/s41586-025-09215-4
- 代码: https://huggingface.co/marcelbinz/Llama-3.1-Centaur-70B

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

#### Gemini 4 Argon 智能体团队通关 Minecraft（A team of Gemini 4 Argon agents beats Minecraft） — 谷歌 DeepMind (2026-10-15)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 文字提示, 场景规格、代码与规则 → 输出: 智能体行为与动作, 对话 / 文本
- 核心想法: 一组智能体已能在游戏世界中跨越数千个相互依赖的步骤、连续一天保持目标一致；不过它们依靠的接口直接告诉它们人类玩家需要亲眼看到的信息。
- 内容: 四个 Gemini 4 Argon 智能体各自通过开源库 Mineflayer 操控一名 Minecraft 玩家，借助游戏内聊天与共享笔记协作，从随机生成的生存世界中赤手空拳起步，在 27 小时 14 分钟后击败末影龙，期间编写了 2,783 个程序、死亡 605 次。Google DeepMind 称这是 AI 智能体首次端到端自主通关 Minecraft。
- 实现方式: 不预设角色、游戏逻辑或技能：智能体自行规划、编写并调试调用 Mineflayer 的程序；Mineflayer 直接提供方块与实体信息以及寻路，而不是画面像素；一个观察者智能体与研究人员通过实时面板查看每个程序、消息与游戏事件。
- 参数: 4 agents · 27 h 14 min · 2,783 programs · ~24,000 model calls · ~1.35B input tokens · ~US$520 at introductory list price
- 能力维度: 持久性, 适应性, 实验控制
- 论文: https://arxiv.org/abs/2610.22319 (arXiv)
- 图片: https://arxiv.org/html/2610.22319v1/overview.png https://arxiv.org/html/2610.22319v1/timeline.png
- 项目主页: https://arxiv.org/abs/2610.22319

#### Player-1 — Mingyu Ouyang, 腾讯 ARC 实验室 (2026-10-14)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 开源权重 / 代码, 仅限研究
- 输入: 图像, 文字提示 → 输出: 智能体行为与动作
- 核心想法: 廉价、可随机化的合成游戏可以代替人工收集的示范，成为智能体学习行动的场所；生成的世界也可以承担同样的角色。
- 内容: 把计算机操作模型变成游戏智能体的训练方法。智能体先在来自 172 款游戏的 6,044 条游戏轨迹上微调，再在 16 个合成的二维与三维训练游戏中通过强化学习练习，随后去完成从未训练过的 Minecraft、ViZDoom 与 GameWorld 任务。
- 实现方式: 以 Qwen3.5 为基础的计算机操作模型（9B 与 35B-A3B）获得扩展的键鼠动作空间（相对指针移动、持续按键、组合动作），先在带指令与推理标注的轨迹上监督微调，再在 Player-1-Gym 中做多环境 PPO 强化学习；奖励直接由游戏状态计算，外观、镜头、场景与操控参数均随机化。
- 参数: Player-1-9B · MineDojo-300 success 10.54% (SFT) → 38.33% (RL), best external baseline 12.63% · 16 synthetic environments
- 能力维度: 情境多样性, 反应性
- 论文: https://arxiv.org/abs/2610.20584 (arXiv)
- 视频: https://player-1-project.github.io/assets/introduction/overview.mp4
- 图片: https://player-1-project.github.io/assets/base_3d_combat_arena.webp
- 项目主页: https://player-1-project.github.io/
- 代码: https://github.com/TencentARC/Player-1

#### PROWL-2 — Odyssey (2026-10-01)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入:  → 输出: 智能体行为与动作
- 核心想法: 在让智能体从生成的世界中学习之前，先检查这个世界：模型推演错的片段不用于训练，而是转去修正模型本身。
- 内容: Odyssey 提出的训练框架：一组智能体在学习得到的世界模型中训练，同时在世界模型预测出错的地方对其进行修复。演示场景包括《星际争霸 II》小队作战（SMACv2）和多台四足机器人的协作任务。
- 实现方式: 智能体在世界模型生成的推演中训练，起始状态按学习潜力排序（无监督环境设计）；一个“开发者”智能体在真实环境中寻找模型预测错误之处；保真度闸门把想象轨迹与记录的真实轨迹对比，保真度低的起始状态先交给世界模型修复，直到模型能正确预测后才重新用于训练。
- 参数: SMACv2 9 scenarios (5v5, 10v10, 10v11) · up to 91% relative gain over the baseline world-model learner · MQE Gate-3 success 29.8% → 70.4%
- 能力维度: 适应性, 情境多样性, 行为似真性
- 论文: https://prowl.odyssey.ml/PROWL-2.pdf (Preprint)
- 视频: https://framerusercontent.com/assets/ZIdJUCh5QSXs3cQHda1vkpy32s.mp4
- 图片: https://framerusercontent.com/assets/n4yXH1c5rgVzfkISH5AOF0HEZUc.jpg
- 项目主页: https://odyssey.ml/introducing-prowl-2

#### GameWorld — Mingyu Ouyang (2026-04-08)
- 类型: 数据集 / 基准 · 时序: 回合制 · 获取方式: 开源权重 / 代码
- 输入: 图像, 文字提示 → 输出: 智能体行为与动作
- 核心想法: 依据游戏状态而不是评审模型来打分，让智能体在世界中的行为可核验、可重复，这正是实验平台所需的特性。
- 内容: 一个包含 34 款网页游戏、170 项任务的基准，用来测试多模态模型作为游戏智能体的能力：既可以作为直接按键、移动鼠标的计算机操作智能体，也可以通过解析后的语义动作空间行动；每项任务都依据游戏自身的状态评分。在 18 组模型与接口的组合中，表现最好的智能体仍远不及人类玩家。
- 实现方式: 游戏在浏览器中运行，提供两种智能体接口：原始键鼠操作与确定性的语义动作解析；结果指标直接从游戏状态读取，并通过多次完整重跑检验基准的稳定性。
- 参数: 34 games · 170 tasks · 18 model-interface pairs
- 能力维度: 实验控制, 反应性
- 论文: https://arxiv.org/abs/2604.07429 (arXiv)
- 视频: https://gameworld-project.github.io/static/figures/GameworldPromoShort.mp4
- 图片: https://gameworld-project.github.io/static/figures/gameworld/teaser-wo-logo-transparent.png
- 项目主页: https://gameworld-project.github.io/

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

#### Mindcraft — Kolby Nottingham (2024-02-17)
- 类型: 开源工具 · 时序: 回合制 · 获取方式: 开源权重 / 代码
- 输入: 文字提示 → 输出: 智能体行为与动作, 对话 / 文本
- 核心想法: 一种低成本、易改造的方式，把会说话、会行动的 AI 玩家放进与人共享的三维世界，几乎是现成的多智能体社会试验平台。
- 内容: 一个开源机器人框架：大语言模型智能体以玩家身份加入 Minecraft 服务器，可以与人交谈，会采矿、合成、建造、战斗与聊天，为新任务自行编写代码，并与其他机器人合作或争执。Emergent Garden 频道中多个模型一起生存的视频让它广为人知；2025 年基于它构建的 MineCollab 基准用于测试协作能力。
- 实现方式: 基于 Mineflayer 机器人库的 Node.js 智能体循环：大语言模型（默认 OpenAI，也支持其他服务商与本地模型）读取聊天与游戏状态，调用内置命令或编写沙箱化的 JavaScript，并记录自身进展；在 MineCollab 中，当智能体必须交流详细计划时，表现最多下降 15%，作者认为沟通是主要瓶颈。
- 能力维度: 共创与能动性, 反应性, 创作可及性
- 论文: https://arxiv.org/abs/2504.17950 (arXiv)
- 视频: https://www.youtube.com/watch?v=NTHWMk5pcYs
- 图片: https://mindcraft-minecollab.github.io/steve.png
- 项目主页: https://kolbynottingham.com/mindcraft/
- 代码: https://github.com/mindcraft-bots/mindcraft

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

#### 视频预训练（VPT）（Video PreTraining (VPT)） — OpenAI (2022-06-23)
- 类型: 模型 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 视频 → 输出: 智能体行为与动作
- 核心想法: 只要用少量标注数据训练模型去推断视频中缺失的操作，互联网视频就能教会智能体行动；NitroGen 等后来的游戏智能体正是放大了这一方法。
- 内容: 一个 Minecraft 智能体：通过观看约 7 万小时无标注的 YouTube 游戏视频，学会以每秒 20 帧、用普通键盘鼠标玩游戏；微调后能制作钻石工具，这一任务熟练玩家约需 20 分钟、约 2.4 万次操作。
- 实现方式: 先用约 2,000 小时外包玩家的游戏记录训练逆动力学模型，为网络视频标注操作；再在这些伪标注视频上预训练大型行为克隆策略，并通过模仿学习与强化学习微调。
- 参数: ~70,000 h of video · 20 Hz keyboard and mouse · diamond pickaxe after RL fine-tuning
- 能力维度: 情境多样性, 反应性
- 论文: https://arxiv.org/abs/2206.11795 (NeurIPS 2022)
- 视频: https://www.youtube.com/watch?v=fJn9B64Znrk
- 项目主页: https://openai.com/index/vpt/
- 代码: https://github.com/openai/Video-Pre-Training

#### MineDojo — Linxi (Jim) Fan, 英伟达 (2022-06-17)
- 类型: 数据集 / 基准 · 时序: 实时流式 · 获取方式: 开源权重 / 代码
- 输入: 文字提示, 视频 → 输出: 智能体行为与动作
- 核心想法: 把一款游戏以及人们发布的相关内容，变成开放式智能体共享的基准；此后的大多数 Minecraft 智能体都在它上面接受评测。
- 内容: 一个 Minecraft 研究框架：在程序化生成的世界中提供数千个以语言描述的开放式任务，并配套由 YouTube 视频、维基页面与 Reddit 帖子组成的互联网规模知识库，以及用作智能体奖励的视频-语言模型 MineCLIP。
- 实现方式: 在 MineRL 之上构建的模拟器套件，包含程序化任务与创造性任务；MineCLIP 在时间对齐的 YouTube 视频与字幕对上做对比学习，评估智能体最近画面与文字目标的匹配程度，作为强化学习的奖励。
- 参数: 3,000+ tasks · 730,000+ YouTube videos · 7,000+ wiki pages · 340,000+ Reddit posts
- 能力维度: 情境多样性, 情境可达性
- 获奖与认可: NeurIPS 2022 Outstanding Paper Award
- 论文: https://arxiv.org/abs/2206.08853 (NeurIPS 2022 Datasets and Benchmarks)
- 视频: https://minedojo.org/videos/pull_video.mp4
- 图片: https://minedojo.org/images/card/youtube.png
- 项目主页: https://minedojo.org/
- 代码: https://github.com/MineDojo/MineDojo

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

#### WorldMind — Zhiyang Deng, 腾讯 (2026-08-18)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入: 键盘与手柄动作 → 输出: 交互式帧流, 智能体行为与动作
- 核心想法: 把生成角色“决定做什么”与“如何被画出来”分开，就得到一个可检查的决策层；实验要控制并记录 NPC 行为，正需要这样的接口。
- 内容: 一个游戏世界模型：首领角色的下一步动作，由从生成画面中重建出的显式游戏状态来决定，而不是隐含在视频生成器里，或由外部直接给定。项目页展示了连续一小时的闭环首领战。
- 实现方式: 四层闭环：理解层从生成画面中构建紧凑状态，决策层规划 NPC 动作，控制层将其转为时间对齐的条件，经蒸馏的视频生成器渲染结果；训练数据为 BOSS-140K，即由智能体自动采集、与游戏内部状态配对的游戏视频。
- 参数: BOSS-140K dataset · 1-hour continuous rollout · two-step distilled generator · preferred over baselines in ~70% of pairwise comparisons
- 能力维度: 行为似真性, 反应性, 实验控制
- 论文: https://arxiv.org/abs/2608.21439 (arXiv)
- 视频: https://teawhite.cn/WorldMind/assets/rollout-1h-6x.mp4
- 图片: https://teawhite.cn/WorldMind/assets/teaser.webp
- 项目主页: https://teawhite.cn/WorldMind/

#### NVIDIA ACE 游戏智能体 SDK（NVIDIA ACE Game Agent SDK） — 英伟达 (2026-06-16)
- 类型: 开源工具 · 时序: 回合制 · 获取方式: 开源权重 / 代码
- 输入: 语音与音频, 文字提示, 场景规格、代码与规则 → 输出: 对话 / 文本, 智能体行为与动作, 语音 / 声音
- 核心想法: PUBG Ally 与《全面战争》顾问所用的 NPC 技术栈，如今成了免费的本地工具包；实验室无需云端费用、也不必担心供应商更换底层模型，就能运行会说话、会行动的角色。
- 内容: 一个开源的 C/C++ 框架，于 Unreal Fest 2026 以测试版发布，用于构建完全在玩家 RTX GPU 上运行的游戏角色：包括保存对话历史并驱动多步工具调用的智能体 API、无状态的对话 API，以及面向游戏自身数据的检索 API。同时推出的 Unreal Engine 5 插件提供本地语音识别、小语言模型与语音合成。
- 实现方式: 针对 RTX 硬件上小模型优化的轻量智能体循环，支持工具调用与语义-词法混合检索；UE5 插件内置 nemo-conformer-ctc-120m 语音识别、GGUF 格式的 Qwen 3.5 4B 模型与 Chatterbox Turbo 350M 语音合成，可通过蓝图或 C++ 调用。
- 参数: C/C++ · on-device (GeForce RTX) · Qwen 3.5 4B SLM · ASR 120M · TTS 350M · beta
- 能力维度: 创作可及性, 时间响应性, 实验控制
- 视频: https://www.youtube.com/watch?v=4syKq_OrbGA
- 图片: https://developer-blogs.nvidia.com/wp-content/uploads/2026/06/ai-game-character.gif
- 项目主页: https://developer.nvidia.com/blog/build-on-device-ai-companions-with-the-nvidia-ace-game-agent-sdk-and-unreal-engine-5-plugins/
- API 文档: https://developer.nvidia.com/ace-for-games
- 代码: https://github.com/NVIDIA/game-agent-sdk

#### Look2React：让 VR NPC 通过视觉引导作出动态反应（Look2React） — Ritik Vatsal (2026-03-31)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 身体、面部与视线追踪, 图像 → 输出: 智能体行为与动作, 对话 / 文本
- 核心想法: 像潜行游戏那样用注视和距离来触发，给角色一双“眼睛”，它们就能回应肢体语言，而且成本低到只在需要时运行。
- 内容: 能对所见作出反应的 VR NPC：当玩家注视并走近 NPC 时，NPC 视角的画面会被送进一个基于视觉的推理模型，由它根据玩家的姿势和当时的情境选择身体姿态和一句台词。
- 实现方式: 以注视和距离触发，截取 NPC 的视角画面送入视觉语言推理模型，由其选择姿态与文本回应；在一款 RPG 中与仿照当代游戏的 NPC 对比（N = 20），玩家与 NPC 的互动更频繁、更多次，报告的社会临场感显著更高。
- 参数: N = 20
- 能力维度: 反应性, 行为似真性
- 论文: https://doi.org/10.1109/TVCG.2026.3679121 (IEEE TVCG 2026 (IEEE VR 2026))
- 视频: https://www.youtube.com/watch?v=GFnAT7k43ME
- 项目主页: https://doi.org/10.1109/TVCG.2026.3679121

#### 与生成式 AI NPC 对话：VR 游戏中玩家与语音智能体的互动（Dialogs with GenAI NPCs） — Nima Zargham (2026-02-02)
- 类型: 行为研究 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 语音与音频 → 输出: 对话 / 文本, 语音 / 声音
- 核心想法: 与 NPC 自由对话让玩家感到沉浸，直到对话出错：77% 的人遇到过语音识别错误，而错误或离题的回答比延迟更常打断游戏。
- 内容: Office Whispers 是一款运行在 Quest 2 上的语音 VR 解谜冒险游戏，玩家通过与四个由 Inworld 驱动的 NPC（经理、维修工、设计师和实习生）自由交谈来解开谜团；研究者对加拿大和荷兰的 48 名玩家进行了问卷与访谈。
- 实现方式: 由 Inworld 提供语音识别、对话记忆和大语言模型回复，并以语音输出；探索性研究，N = 48，使用玩家体验量表（PXI）、自编问卷和半结构化访谈，角色设置有两个互换性别的版本。
- 参数: Quest 2 · 4 NPCs · N = 48
- 能力维度: 行为似真性, 时间响应性
- 论文: https://doi.org/10.1080/10447318.2026.2620647 (International Journal of Human–Computer Interaction, 2026)
- 项目主页: https://doi.org/10.1080/10447318.2026.2620647

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

#### GARP：实时生成式智能体村庄（GARP (Generative Agents Realtime Playground)） — Studio Atelico (2025-01-08)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入: 文字提示 → 输出: 智能体行为与动作, 对话 / 文本
- 核心想法: 生成式智能体小镇不再需要云端预算：在本地运行时，一整个群体可以在游戏或 VR 场景中实时生活。
- 内容: 一个技术演示：村庄里有 20 多个生成式智能体，各有性格、记忆与日程，会建立关系、相互回应；它仿照斯坦福的 Smallville 重新实现，在一块 NVIDIA RTX 3090 上实时运行，而不是依赖缓慢且收费的云端回合。
- 实现方式: Atelico 的本地端引擎运行自研小语言模型，配合认知记忆架构与可热切换的适配器；Atelico 称原版 Smallville 以回合方式运行，每模拟一个游戏日约需 500 美元，而 GARP 在本地运行，没有按次费用。
- 参数: 20+ agents · real-time · one RTX 3090
- 能力维度: 行为似真性, 持久性, 时间响应性
- 视频: https://www.youtube.com/watch?v=xT_vi2maxuM
- 图片: https://atelico.studio/images/og/home.png
- 项目主页: https://atelico.studio

#### 《MIR5》AI 首领 Asterion（MIR5 AI boss Asterion） — Wemade Next, 英伟达 (2025-01-06)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入: 键盘与手柄动作 → 输出: 智能体行为与动作
- 核心想法: 把生成式角色用作对手而不是帮手：一个会适应人习惯的对手，正是自适应训练情境在游戏中的对应物。
- 内容: Wemade Next 为 MMORPG《MIR5》打造的首领角色，在 CES 2025 上展示：它会分析对手玩家的技能、装备与战术，回忆以往的战斗并调整攻击方式，因此同一个首领每次的战斗过程都不相同。截至 2026 年 10 月，尚未确认这一 AI 首领已在正式游戏中上线。
- 实现方式: 为《MIR5》调优、通过 NVIDIA ACE 提供的小语言模型感知战斗情况，把当前队伍与以往战斗对比，并选择首领的下一步动作，而不是按预设套路行动。
- 能力维度: 适应性, 反应性
- 视频: https://www.youtube.com/watch?v=-8XeiZ4djKw
- 项目主页: https://www.nvidia.com/en-us/geforce/news/nvidia-ace-autonomous-ai-companions-pubg-naraka-bladepoint/

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
- 内容: 《绝地求生》中可语音交流的 AI 队友：用游戏术语报点、分享物资、驾驶载具并与玩家并肩作战。魁匠团称之为“可共玩角色”（CPC）；在 CES 2025 与 GDC 2026 展示后，于 2026 年 6 月 17 日至 30 日在 Steam 版 PUBG 街机模式中以“Ally 双排模式”进行了为期两周的公开测试。
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

#### AI People（AI NPC 沙盒游戏）（AI People） — GoodAI (2024-09-19)
- 类型: 产品 / 应用 · 时序: 回合制 · 获取方式: 产品 / 应用
- 输入: 文字提示 → 输出: 智能体行为与动作, 对话 / 文本
- 核心想法: 让玩家自己设定情境与角色，再观察大语言模型角色如何演绎；但云端成本与不明朗的商业模式也可能让这样的世界终止。
- 内容: 一款沙盒游戏：每个角色都是有自己情绪与动机的大语言模型智能体；玩家与他们交谈，创建并分享自定义情境，在约十分钟的游玩中观察故事自然展开。测试版于 2024 年 9 月 19 日开放，月费 10 美元；到 2026 年 10 月，游戏网站已跳转到 GoodAI 首页，现状不明。
- 实现方式: 云端大语言模型根据情境描述与每个角色的记忆，驱动 NPC 的对话、情绪与行动选择，这也是 GoodAI 采用订阅收费的原因；GoodAI 也是 CES 2025 上列出的 NVIDIA ACE 合作方。
- 参数: ~10-minute sessions · US$10/month (alpha)
- 能力维度: 行为似真性, 共创与能动性, 创作可及性
- 视频: https://www.youtube.com/watch?v=3XtqQBt-W0Y
- 图片: https://www.goodai.com/wp-content/uploads/2024/08/AIPeople_Banner_02_ALPHA-1024x576.jpg
- 项目主页: https://www.goodai.com/ai-people-alpha-release-date-announced/

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

#### Mantella（《上古卷轴 V》AI NPC 模组）（Mantella） — Art from the Machine (2023-08-19)
- 类型: 开源工具 · 时序: 回合制 · 获取方式: 开源权重 / 代码
- 输入: 语音与音频 → 输出: 语音 / 声音, 对话 / 文本
- 核心想法: 一个大型手工构建的世界，加上语音识别、大语言模型与声音克隆，就能与其中全部角色进行开放式对话；这为在现成三维世界中搭建对话场景提供了低成本的模板。
- 内容: 一个免费模组：玩家可以直接开口与《上古卷轴 V：天际》（后来也包括《辐射 4》）中的 1,000 多个 NPC 交谈，并听到他们以各自的合成声音回答；角色会记住之前的对话，也能感知游戏中发生的事件。
- 实现方式: 用 Whisper 或 Moonshine 转写语音，由云端或本地大语言模型根据每个 NPC 的人物小传、对话记忆与当前游戏事件生成回复，再用 xVASynth、Piper 或 XTTS 以角色原有的游戏嗓音说出并口型同步。
- 参数: 1,000+ NPCs · Skyrim, Fallout 4
- 能力维度: 反应性, 持久性, 共创与能动性
- 视频: https://www.youtube.com/watch?v=FLmbd48r2Wo
- 图片: https://raw.githubusercontent.com/art-from-the-machine/Mantella/main/img/mantella_trailer.gif
- 项目主页: https://art-from-the-machine.github.io/Mantella/index.html
- 代码: https://github.com/art-from-the-machine/Mantella

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

#### XARA：生成扩展现实实验的多模态智能体系统（XARA） — Tareq Alsaleh (2026-10-15)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 语音与音频, 草图与手势 → 输出: 三维场景 / 世界, 智能体行为与动作
- 核心想法: 面向行为研究者本人的语音式实验场景生成，场景可以保存并作为实验条件反复使用。
- 内容: 交通研究者置身沉浸式 Unity 场景中，用语音下达指令，例如添加车辆、行人或街道设施并设定它们的运动；大语言模型流程据此搭建并保存驾驶、过街或街道设计情境，供行为实验使用。
- 实现方式: 双大语言模型架构先转写语音，再把它转成结构化指令并实时作用于 Unity XR 场景（创建物体、空间操作、动画控制与场景保存），并用手势辅助摆放；论文为系统描述，尚无用户研究。
- 能力维度: 创作可及性, 实验控制, 情境可达性
- 论文: https://arxiv.org/abs/2610.21067 (arXiv 2026)
- 视频: https://www.youtube.com/watch?v=A6PlUJB6QJU
- 图片: https://arxiv.org/html/2610.21067v1/transform5.png
- 项目主页: https://arxiv.org/abs/2610.21067

#### 生成式教程：为现实任务实时生成贴合情境的可视化指导（Generative Tutorial） — Muzhe Wu (2026-09-21)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 透视画面与实时环境 → 输出: 图像 / 全景图, 平面视频
- 核心想法: 指导根据现场画面生成，而不是事先录好的视频；参与者完成得更好，但生成错误会影响他们对指导的信任程度。
- 内容: 一个 AR 原型在用户做手工任务时观察其工作台，并为每一步生成目标图和简短示范视频，画面里是用户自己的工具和材料以及它们当前的状态。
- 实现方式: 先用 15 个现实任务对现有图像与视频生成模型做形成性测试，据此搭建流程：预测前序动作的视觉结果，并根据观察到的工作台生成每一步的图像与视频；24 人的实验室研究将其与预先制作的指导作比较。
- 能力维度: 适应性, 反应性
- 论文: https://arxiv.org/abs/2609.24955 (arXiv 2026)
- 图片: https://arxiv.org/html/2609.24955v1/figures/teaser.png
- 项目主页: https://arxiv.org/abs/2609.24955

#### 混合现实中的视觉生成式 AI 综述（Visual Generative AI in Mixed Reality: A Survey） — Duotun Wang (2026-08-18)
- 类型: 论文 / 综述
- 输入: 文字提示, 透视画面与实时环境 → 输出: 图像 / 全景图, 三维场景 / 世界
- 核心想法: 生成模型与 MR 交互设计在三个方面共同演进：沉浸式可视化、可控生成与合成数据。
- 内容: 一篇综述，考察视觉生成式 AI（二维与三维内容生成以及视觉语言模型）如何被用于 VR 与 AR；基于对 2018–2025 年 102 篇论文的深入审阅，按技术、交互设计与评估方法组织。
- 实现方式: 筛选 2018–2025 年国际会议与期刊发表的论文，再对 102 篇进行深入审阅，按二维与三维视觉内容生成、视觉语言模型集成、交互设计与评估进行编码。
- 能力维度: 创作可及性, 感知真实感
- 论文: https://doi.org/10.1080/10447318.2026.2713822 (International Journal of Human–Computer Interaction, 2026)
- 项目主页: https://doi.org/10.1080/10447318.2026.2713822

#### Generative Proxy：为 AR 眼镜合成用于现实世界交互的代理式界面（Generative Proxy） — Xianhao Carton Liu, Mar Gonzalez-Franco (2026-08-10)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 场景规格、代码与规则, 透视画面与实时环境, 文字提示 → 输出: 三维场景 / 世界
- 核心想法: 佩戴者操作的是房间的生成式抽象，而不是房间本身；现实中哪些部分可被操控、以何种方式操控，由生成器按设备和意图来决定。
- 内容: 在没有大视场显示、也没有手部和眼动追踪的轻量 AR 眼镜上，系统会生成代理界面：为远处、杂乱或被遮挡的真实物体生成虚拟替身，佩戴者用设备有限的输入方式就能操作它们，界面会按场景、任务和设备量身生成。
- 实现方式: 生成过程被表述为基于三类规格（场景、意图、设备能力）的约束合成，先枚举出有效的代理界面；再依据直接操纵理论中的语义距离与动作距离对候选排序，排序结合了基于规则的代价、大语言模型给出的人机工效评分，以及对入围候选的大语言模型一致性检查。原型运行于 Apple Vision Pro、Meta Quest 3、Meta Ray-Ban Display 和 Project Aria，并支持手表、手机与 Neural Band 输入；12 位 XR 开发者与研究者对生成界面给出了正面评价。
- 能力维度: 创作可及性, 适应性
- 论文: https://arxiv.org/abs/2608.08971 (UIST 2026)
- 视频: https://www.youtube.com/watch?v=N1YcwAxcPaQ
- 图片: https://arxiv.org/html/2608.08971v1/figs/Teaser.png
- 项目主页: https://arxiv.org/abs/2608.08971

#### PartInteractor：面向 XR 持续共创的意图驱动、部件感知三维创作（PartInteractor） — Jianan Jiang (2026-08-02)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 语音与音频, 草图与手势, 图像 → 输出: 网格 / 三维资产
- 核心想法: 把生成的物体当作部件层级来处理，一次性的“提示到物体”就变成了可持续的编辑，场景修改无需从头再来。
- 内容: 用户在 XR 头显中用语音描述、画草图或拍照来表达想要的物体；系统把它生成为由若干命名部件组成的三维资产，用户随后可以逐个部件地抓取、替换、换风格或重新生成。
- 实现方式: 由 LLM/VLM 解析器把语音、现场草图或头显拍摄的图像转成候选二维概念图（检索加生成），再用部件感知的图生三维模型生成按语义拆分的资产，在头显中按部件操作；并与整体重新生成的方式作对比评估。
- 能力维度: 创作可及性, 共创与能动性
- 论文: https://arxiv.org/abs/2608.01335 (UIST 2026)
- 视频: https://horizonjohn.github.io/PartInteractor/static/videos/PartInteractor.mp4
- 图片: https://horizonjohn.github.io/PartInteractor/static/images/application.png
- 项目主页: https://horizonjohn.github.io/PartInteractor/
- 代码: https://github.com/SNeC-Lab-PSU/PartInteractor

#### “一语一世界”：生成式 AI 驱动的实时 VR 共创（One Word, One World） — Chen Yang (2026-07-31)
- 类型: 行为研究 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 语音与音频 → 输出: 网格 / 三维资产
- 核心想法: 语音驱动的生成改变的不只是速度，还有谁能参与：对三维经验很少的人，社会临场感与心理安全感提升最明显。
- 内容: 在共享的 VR 空间里，协作者只要说出一个物体，所有人眼前就会同时出现一个占位体，随后被生成的三维资产替换，任何参与者都可以移动和编辑它。一项被试内实验（N = 48）把它与从资产库搭建的方式作了比较。
- 实现方式: 多人 VR 环境中结合语音识别与生成式三维资产创建，提供共享占位体、软锁定、状态同步和作者可视化。被试内设计，N = 48，以资产库为基线：创作产出更高（p < .001），专家评定的设计质量更高（p = .007），社会临场感与心理安全感也更高。
- 参数: N = 48 within-subjects
- 能力维度: 共创与能动性, 创作可及性
- 论文: https://doi.org/10.1007/s10055-026-01434-y (Virtual Reality (Springer), 2026)
- 项目主页: https://link.springer.com/article/10.1007/s10055-026-01434-y

#### 大语言模型辅助沉浸式场景编辑中的虚构现象与感知—现实差距（Confabulations in LLM-Assisted Immersive Scene Editing） — Junlong Chen (2026-07-25)
- 类型: 行为研究 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 语音与音频 → 输出: 三维场景 / 世界
- 核心想法: 在较复杂的场景中，用户只察觉到大约三分之一的虚构，而且错误越多，用户的估计越脱离实际；因此生成场景需要可由机器核验的编辑日志，而不能依赖用户的信任。
- 内容: 24 名非专业用户通过与基于 GPT-5.2 的助手对话来编辑三个 VR 场景（办公室、阁楼和城市）；作者逐轮标注“虚构”现象，即系统错误陈述自己做了什么或场景里有什么，并与用户察觉到的情况对比。
- 实现方式: 语音先转为文字，由规则分类器判别意图，再由 GPT-5.2 对选中的物体执行编辑（Oculus Quest 2）。探索性研究，N = 24：1,612 个交互轮次中有 437 个（27.1%）出现虚构；得出九类分类，空间放置错误最多（299 次）；并提出“感知与现实差距”：感知与实际次数的中位数分别为 2 对 6（办公室）和 4 对 10.5（城市）。
- 参数: N = 24 · 1,612 turns · 27.1% confabulated
- 能力维度: 实验控制, 创作可及性
- 论文: https://arxiv.org/abs/2607.23213 (arXiv preprint (under review), 2026)
- 图片: https://arxiv.org/html/2607.23213v1/figures/city-teaser.png https://arxiv.org/html/2607.23213v1/system-workflow.png
- 项目主页: https://arxiv.org/abs/2607.23213

#### CoGen3D：为虚拟现实生成三维资产的人机协同设计智能体流程（CoGen3D） — Weiwei Jiang (2026-07-04)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 文字提示 → 输出: 网格 / 三维资产, 图像 / 全景图
- 核心想法: 共同设计的资产与更高的投入度和情绪反应的变化相关，但人们仍更喜欢概念图而不是最终的三维模型，这反映出图像到三维之间的质量落差。
- 内容: 智能体先就用户想为 VR 场景添加的物体进行提问，给出概念图供确认，再生成三维资产并放入沉浸式场景；一项 120 人的研究比较了共同设计资产的人和只体验场景的人。
- 实现方式: 分阶段流程：由大语言模型智能体对话式地引出意图，确认概念图，再进行图生三维并直接部署到 Meta Quest 3 上六个情绪基调不同的 VR 场景；60 名设计者与 60 名验证者参与。
- 能力维度: 创作可及性, 共创与能动性
- 论文: https://arxiv.org/abs/2607.03731 (arXiv 2026)
- 图片: https://arxiv.org/html/2607.03731v1/system_design.png
- 项目主页: https://arxiv.org/abs/2607.03731

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

#### 生成式 AI 赋能的 XR：在超能力与风险之间权衡（Empowered XR through Generative AI） — Yiliu Tang (2026-04-13)
- 类型: 论文 / 综述
- 输入: 语音与音频, 透视画面与实时环境 → 输出: 三维场景 / 世界, 对话 / 文本
- 核心想法: 头显里的每一种生成式“超能力”都伴随着对自主性、隐私或透明度的风险，因此生成情境的防护措施必须与能力同步设计。
- 内容: CHI 2026 的一篇综合研究，梳理 135 项近期系统与研究，把大语言模型赋能的 XR 带给人的能力归为“超能力”：内在的（认知与感官增强）和外在的（改变环境与社交情境），并逐一对应其风险。
- 实现方式: 对 135 项 XR 中生成式 AI 的近期工作进行多阶段分析，得出内在与外在超能力及其风险（用户自主、数据安全、伦理透明）的分类，并提出设计准则与研究议程。
- 能力维度: 情境可达性, 实验控制
- 论文: https://doi.org/10.1145/3772318.3791307 (CHI 2026)
- 视频: https://www.youtube.com/watch?v=azB-6roN0no
- 项目主页: https://doi.org/10.1145/3772318.3791307

#### GenerativeSurface：生成式 AI 辅助的混合现实三维概念设计语义支架（GenerativeSurface） — Yichen Chai (2026-03-31)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 文字提示, 草图与手势 → 输出: 网格 / 三维资产
- 核心想法: 生成的曲面是用来在上面画的，而不是成品，这样既保留了人的亲手设计，又解决了面对空白画布无从下手的问题。
- 内容: 在混合现实中，设计师用语言描述一个概念，GenerativeSurface 把它变成可交互的三维曲面，作为在空中画草图的支架，形成“描述、生成、草绘、迭代”的循环。
- 实现方式: 生成式 AI 把自然语言描述转成可编辑的三维曲面，放进 MR 工作空间供空中草绘；在工程概念设计任务中与基本几何体支架和徒手空中草绘作了对比评估。
- 能力维度: 创作可及性, 共创与能动性
- 论文: https://doi.org/10.1109/TVCG.2026.3679098 (IEEE TVCG 2026 (IEEE VR 2026))
- 视频: https://www.youtube.com/watch?v=Emc7e7AvhSA
- 项目主页: https://doi.org/10.1109/TVCG.2026.3679098

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

#### DreamCraft：VR 沉浸式原型的场景级与物体级生成流程（DreamCraft） — Cheng-Chih Tsai (2026-03-21)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 文字提示 → 输出: 三维场景 / 世界, 网格 / 三维资产
- 核心想法: 整场景生成与逐物体生成是两种不同的情境创作方式，这项研究把两者之间的取舍变成设计准则，而不是默认选项。
- 内容: DreamCraft 是一个 VR 原型工具，提供两种生成流程：一次生成整个可漫游的环境，或者用 AI 生成的资产逐个物体地搭建场景；12 位 VR 设计师试用了两种流程。
- 实现方式: VR 系统结合场景级生成（整个环境）与物体级生成（逐步添加资产），很可能由文字或语音提示驱动；12 位 VR 设计师参与的用户研究，从任务完成时间、创意探索和感知认知负荷几方面比较两种流程。
- 参数: N = 12 VR designers
- 能力维度: 创作可及性, 共创与能动性
- 论文: https://doi.org/10.1109/VR67842.2026.00088 (IEEE VR 2026)
- 视频: https://www.youtube.com/watch?v=wmliWuwohqg
- 项目主页: https://doi.org/10.1109/VR67842.2026.00088

#### GenAssist：交互式提示驱动的 XR 程序生成（GenAssist） — Sruti Srinidhi (2026-03-21)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 文字提示 → 输出: 三维场景 / 世界
- 核心想法: 生成的是程序而不是像素，得到的场景行为可以阅读、记录和重跑，这正是实验者对生成情境的要求。
- 内容: 用自然语言描述想要的 XR 程序，GenAssist 就会编写、运行并把它热插入正在运行的场景：放置基本几何体和三维模型、让它们动起来并接上交互，再通过场景里的虚拟相机检查结果、修改代码。
- 实现方式: 检索增强生成把平台文档与示例代码放入大语言模型提示；生成的脚本以热插拔方式运行，并通过闭环从虚拟相机渲染场景、把画面反馈回去修正程序。在 50 条提示的基准上评估（每次运行不到 10 秒，调用次数少于以往系统），并做了 18 人的用户研究（NASA-TLX 36.6）。
- 参数: <10 s per run · 50-prompt benchmark · N = 18
- 能力维度: 创作可及性, 实验控制
- 论文: https://doi.org/10.1109/VR67842.2026.00081 (IEEE VR 2026)
- 视频: https://www.youtube.com/watch?v=nA28_u0hOjU
- 项目主页: https://doi.org/10.1109/VR67842.2026.00081

#### HOICraft：基于视觉语言模型的 VR 部件级手物交互现场创作工具（HOICraft） — Dohui Lee (2026-02-09)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 文字提示, 身体、面部与视线追踪 → 输出: 人工制作的 VR 情境
- 核心想法: 生成的对象可以是世界如何回应双手，而不只是它的外观；大多数生成物体恰恰停留在不可交互的道具阶段。
- 内容: VR 设计师选中一个三维物体并说明意图，HOICraft 用 GPT-4o 判断哪些部件应当可交互，并推荐手部动作如何驱动它们（物理抓取、手势或触碰，操纵或动画），设计师随后在头显里测试和调整。
- 实现方式: GPT-4o 分析物体与设计意图，推荐可交互部件、手物交互属性，以及在五类交互设计（基于物理、手势或接触的操纵或动画）中排好序的手部到行为映射，并以 20 名参与者的偏好数据作为上下文示例。在 Meta Quest 3 上，12 位 VR 交互设计师的试错次数显著少于手动映射（p < .001），SUS 为 81。
- 参数: Meta Quest 3 · N = 12 designers · SUS 81
- 能力维度: 反应性, 创作可及性
- 论文: https://arxiv.org/abs/2602.08219 (CHI 2026)
- 视频: https://www.youtube.com/watch?v=-QvYgTRsOgI
- 项目主页: https://doi.org/10.1145/3772318.3790823

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

#### ShadAR：在增强现实中用提示实时改写视觉（ShadAR） — Yanni Mei (2026-10-14)
- 类型: 研究演示 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入: 文字提示, 透视画面与实时环境 → 输出: 交互式帧流
- 核心想法: 通过提示实时改写人所看到的画面，甚至可以用关于情绪或行为的“目标式”提示，让感知本身成为可生成、可操控的条件。
- 内容: 佩戴者写下希望透视画面发生的变化，比如“把所有人都模糊掉”或“让我笑一笑”，大语言模型随即编写像素着色器，实时作用在摄像头画面中对应的区域上。
- 实现方式: 由大语言模型（论文中为 GPT-5.2）理解提示，目标检测器（YOLO）在透视画面中定位目标，再把生成的着色器注入透视渲染管线；一项由 21 位 HCI 研究者参与的探索性研究梳理了应用领域与提示方式。
- 能力维度: 反应性, 创作可及性
- 论文: https://arxiv.org/abs/2610.19998 (UIST 2026)
- 图片: https://arxiv.org/html/2610.19998v1/teaser.jpeg
- 项目主页: https://arxiv.org/abs/2610.19998

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
- 实现方式: 通过 QuestCameraKit 获取透视摄像头画面，经 WebRTC 流式发送到 Decart 的实时视频到视频模型，再把重绘后的画面渲染回头显；自 2026 年 7 月起，应用中的模型名为 Lucy-Restyle-2（由 Mirage 更名，61 种世界风格）和 Lucy（15 种人物变换）。
- 参数: 720p · 30 fps · <200 ms latency (developer-reported)
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

#### 加拉帕戈斯：最后的伊甸园（Galápagos: The Last Eden） — Atlantic Studios, 谷歌 (2026-09-11)
- 类型: 体验 / 艺术作品 · 时序: 回合制
- 输入: 语音与音频 → 输出: 对话 / 文本, 语音 / 声音
- 核心想法: 把一位能对话的历史人物放进实拍的纪录片世界，让向导回答观众自己的问题，而不是只念固定台词。
- 内容: 一部为 XR 眼镜制作、由 Margot Robbie 旁白的自然历史体验，在 2026 年威尼斯沉浸单元展出：观众走进 16K 三维拍摄的加拉帕戈斯群岛，还可以向一位由 Gemini 驱动的数字达尔文提问。
- 实现方式: 以 16K 立体三维拍摄素材在 Android XR 眼镜上进行空间呈现，其中的达尔文角色对话由 Gemini 生成（据联合制作方 Google 100 Zeros 团队介绍）。
- 参数: 16K 3D capture · XR glasses
- 能力维度: 行为似真性, 情境可达性
- 获奖与认可: Venice Immersive 2026 (83rd Venice International Film Festival)
- 图片: https://static.labiennale.org/files/styles/seo_thumbnail/public/cinema/2026/Schede_film/970x647/Ve_Immersive/galapagos_the_last_eden.jpg?itok=2TXE0uhw
- 项目主页: https://www.labiennale.org/en/cinema/2026/venice-immersive/galapagos-last-eden

#### Nevatars — Andy Serkis, 谷歌 (2026-09-11)
- 类型: 体验 / 艺术作品 · 时序: 回合制
- 输入: 语音与音频, 透视画面与实时环境 → 输出: 虚拟人（脸 / 身体）, 对话 / 文本, 语音 / 声音
- 核心想法: 一部由明星主导的电影节作品，让按剧本塑造的角色以开放对话回应观众，考验一个精心编排的故事能容纳多少即兴。
- 内容: 一部 31 分钟、为 XR 眼镜打造的混合现实动画电影，在 2026 年威尼斯沉浸单元首映：被遗弃的数字角色出现在观众的房间里并与之交谈；Google 称片中充满由 Gemini 驱动的对话与互动时刻。
- 实现方式: 在 Android XR 的透视混合现实中呈现人工制作的动画与表演捕捉，对话段落由 Gemini 和 Vertex AI 驱动（据 Google 介绍）；由 Imaginarium、Boona、Google 100 Zeros 与 3Dar 联合制作。
- 参数: 31 min · XR glasses
- 能力维度: 共创与能动性, 行为似真性
- 获奖与认可: Venice Immersive 2026 (83rd Venice International Film Festival)
- 视频: https://www.youtube.com/watch?v=Es6SDpbiyM8
- 图片: https://static.labiennale.org/files/styles/seo_thumbnail/public/cinema/2026/Schede_film/970x647/Ve_Immersive/nevatars2.jpg?itok=j3wvW8K0
- 项目主页: https://www.labiennale.org/en/cinema/2026/venice-immersive/nevatars

#### MemoryDiorama：把日常照片变成动态三维模型，帮助唤起记忆（MemoryDiorama） — Keiichi Ihara, Ryo Suzuki (2026-04-08)
- 类型: 研究演示 · 时序: 预先生成 · 获取方式: 仅限研究
- 输入: 图像 → 输出: 三维场景 / 世界, 动作 / 动画
- 核心想法: 围绕个人照片生成的情境可以充当记忆线索：参与者回忆起更多细节，这也提示生成式重现可能影响自传体记忆。
- 内容: 在 Meta Quest 3 的混合现实中，把一张日常照片变成会动的三维立体模型，加入从照片推断出的生成物体、人物动作、天气与粒子效果，帮助人回忆照片中的那一刻。
- 实现方式: 基于大语言模型的场景分析从照片中提取地点、物体、光照与氛围，再经三维物体生成、动画与空间排布搭建立体模型；被试内研究（N=18）比较了仅照片、静态模型与 MemoryDiorama 三种条件。
- 能力维度: 感知真实感, 情境可达性
- 论文: https://arxiv.org/abs/2604.06773 (arXiv 2026)
- 图片: https://arxiv.org/html/2604.06773v1/figures/teaser_v1.2.jpg
- 项目主页: https://arxiv.org/abs/2604.06773

#### VR 中的自适应生成音乐：调节沉浸感与表现（Adaptive Generative Music in VR） — Jiayuan Wen (2026-04-01)
- 类型: 行为研究 · 时序: 实时流式 · 获取方式: 仅限研究
- 输入: 键盘与手柄动作 → 输出: 音效、音乐与空间音频
- 核心想法: 生成音乐不只是氛围，而是一种行为操纵：适度的紧张让瞄准更准，过度的紧张则使其变差，因此自适应配乐可以像其他实验因素一样被调节。
- 内容: 在 Meta Quest 3 上的一款 VR 射箭游戏里，配乐由 Google 的 MusicFX DJ 实时生成，并随着玩家 20 支箭逐渐用完分四个阶段变得越来越紧张；一项被试内实验（N = 22）把它与风格相同的固定配乐作了比较。
- 实现方式: Unity 把游戏事件经由 Ubiq-Genie 发送给控制器，控制器用四条预载提示驱动 MusicFX DJ，并在剩余箭数达到阈值时切换（预载避免了按需生成带来的数秒延迟）。被试内设计，N = 22，每种条件射 20 箭；自适应音乐提高了临场感（7 分制 5.32 对 4.27），并呈倒 U 型：第 2 阶段比固定配乐瞄得更准更快，第 4 阶段则更差更慢。
- 参数: Meta Quest 3 · 4 tension phases · N = 22 within-subjects
- 能力维度: 适应性, 时间响应性
- 论文: https://doi.org/10.1109/TVCG.2026.3679907 (IEEE TVCG 2026)
- 视频: https://www.youtube.com/watch?v=GouIKwIllP4
- 项目主页: https://doi.org/10.1109/TVCG.2026.3679907

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

#### PlayWrite：在 XR 中通过“玩”与 AI 共写故事（PlayWrite） — Esen K. Tütüncü, Autodesk Research (2026-03-02)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 草图与手势, 语音与音频 → 输出: 对话 / 文本
- 核心想法: 让在空间中摆弄角色、而不是输入提示，成为故事生成的输入；这种模式可以迁移到“通过演出来编写情境”。
- 内容: 写作者戴上混合现实头显，在桌面上移动小型虚拟角色和道具，并边玩边说出情节；AI 智能体把这些动作解读为故事节拍，以可重新排列的“故事弹珠”呈现，再由大语言模型把排好的序列写成完整叙事。
- 实现方式: 多智能体流程（环境、社交、叙述者与意图帧智能体）把操作、空间关系与语音压缩为“意图帧”，再由大语言模型写成文本；对 13 位写作者进行了用户研究。
- 能力维度: 共创与能动性, 创作可及性
- 论文: https://arxiv.org/abs/2603.02366 (CHI 2026)
- 视频: https://www.youtube.com/watch?v=RHvioD_b2Hc
- 图片: https://arxiv.org/html/2603.02366v1/images/teaser-place-holder.png
- 项目主页: https://arxiv.org/abs/2603.02366

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
- 实现方式: 基于 WebXR、three.js、TensorFlow 与 Gemini 的模块化架构，附带模板、示例与演示，也是 Vibe Coding XR 的基础。截至 2026 年 10 月仍在活跃开发（2026-10-15 发布 v0.23.0），v0.19.0 起加入三维场景编辑器与虚拟形象。
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

#### Meta Horizon Worlds 具身大语言模型 NPC（Meta Horizon Worlds embodied LLM NPCs） — Meta (2025-08-27)
- 类型: 平台 / API · 时序: 回合制 · 获取方式: 产品 / 应用
- 输入: 语音与音频, 场景规格、代码与规则 → 输出: 对话 / 文本, 语音 / 声音
- 核心想法: 把大语言模型角色放进一个大型社交 VR 平台的标准工具箱，预设台词与约束规则成为创作者手中的控制杆。
- 内容: 创作者在 Worlds Desktop Editor 中设定角色的名字、背景故事、性格、约束规则与声音，玩家随后就能在 VR 或手机世界里用语音与这个有形体的 NPC 交谈，回应由预设台词和大语言模型生成的话语混合而成。
- 实现方式: Character Builder 的设定与 TypeScript 提供的世界状态上下文共同约束一个大语言模型（据 UploadVR 报道为 Llama 4），回复由合成语音读出；与文本生成地形的 Environment Generation 同时发布，据报道 2025 年 9 月向所有创作者开放，但只有美国成年用户可以与之对话。
- 能力维度: 创作可及性, 行为似真性
- 视频: https://www.youtube.com/watch?v=FNeR-ESSRnY
- 项目主页: https://developers.meta.com/horizon/blog/environment-generation-embodied-conversational-llm-npcs-genai-tools/
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

#### 走出实验室：基于 VERA 平台的大规模远程 VR 晕动症研究（Beyond the Lab: Large-Scale Remote Cybersickness Research in Virtual Reality Using the VERA Platform） — Matt Gottsacker, Jeremy Bailenson, Tabitha Peck (2026-09-04)
- 类型: 行为研究 · 时序: 脚本 / 规则驱动
- 输入: 身体、面部与视线追踪 → 输出: 人工制作的 VR 情境
- 核心想法: 无人监督的远程 VR 研究能以九倍样本复现实验室结果，但样本是有经验的头显用户，而非普通公众。
- 内容: 由美国国家科学基金会资助的“虚拟体验研究加速器”（VERA）通过 Prolific 招募 263 名参与者，让他们在自己的 Meta Quest 头显上运行标准的晕动症测试平台。结果在方向与时间进程上与已发表的实验室研究（N=30）一致，更大的样本还证实了性别、易感性与预期的影响。
- 实现方式: 通过 VERA 部署 Cybersicker 测试平台的远程版本，在 SSQ、FMS 与症状出现轨迹上，与实验室数据及人口学匹配的远程子样本比较；并对人口学与个体差异因素做回归分析。
- 参数: remote N=263 vs in-lab N=30 · consumer Meta Quest headsets
- 能力维度: 实验控制, 情境多样性
- 论文: https://arxiv.org/abs/2609.26203 (arXiv preprint (2026; under review at IEEE TVCG))
- 视频: https://www.youtube.com/watch?v=KMgAFx1MHmg
- 图片: https://arxiv.org/html/2609.26203v1/figs/CybersickerInCart4.png
- 项目主页: https://arxiv.org/abs/2609.26203

#### 用于心理学、行为与认知研究的沉浸式虚拟现实实验工具箱：范围综述（Toolboxes for creating immersive virtual reality experiments in psychological, behavioral, and cognitive research: A scoping review） — Mehrnaz Hosseinzadeh (2026-07-03)
- 类型: 论文 / 综述
- 输入: 场景规格、代码与规则 → 输出: 人工制作的 VR 情境
- 核心想法: 在“生成”之前，瓶颈是“创作”：这份梳理展示了不会编程的研究者目前已能搭建并控制 VR 实验的多大部分。
- 内容: 一篇范围综述：梳理心理学、行为科学与认知神经科学研究者用来搭建头显实验的软件工具箱，并据此为不会编程的研究者提供选型决策框架。
- 实现方式: 对已发表的 VR 实验工具箱做范围综述，按可用性与应用特征整理成证据地图与决策支持框架。
- 能力维度: 创作可及性, 实验控制
- 论文: https://doi.org/10.1016/j.chbr.2026.101194 (Computers in Human Behavior Reports (2026))

#### 合成具身：虚拟现实与沉浸式环境中 AI 生成身份线索的框架（Synthetic embodiment: a framework for AI-generated identity cues in virtual reality and immersive environments） — Tsehaye Haidemariam (2026-06-29)
- 类型: 论文 / 综述
- 输入: 文字提示 → 输出: 虚拟人（脸 / 身体）, 图像 / 全景图
- 核心想法: 生成式化身可以把身份变成能精细调节的自变量，前提是每个生成刺激都经过感知验证和偏差审查。
- 内容: 一篇假说与理论文章：把化身身份视为一个可控的设计空间（表型、性别呈现、年龄、文化标记、模糊性、交叉性线索），并提出“具身分类偏差”（ECB）模型——身份线索先影响具身强度，再影响社会分类，最终影响偏见、共情与合作等群际结果。可行性演示把设定好的身份变量转化为提示词，交给 ChatGPT、Gemini（Nano Banana Pro）和 Tripo，得到九个初步化身刺激；作者明确说明这些刺激尚未经过验证。
- 实现方式: 概念框架，加上五阶段方法流程（生成、标准化、沉浸式集成、感知验证、公平性审查），以及在三个生成系统上从提示词到化身的示例演示。
- 能力维度: 实验控制, 情境多样性
- 论文: https://doi.org/10.3389/frvir.2026.1860842 (Frontiers in Virtual Reality (2026))
- 图片: https://www.frontiersin.org/files/Articles/1860842/xml-images/frvir-07-1860842-g001.webp
- 项目主页: https://www.frontiersin.org/journals/virtual-reality/articles/10.3389/frvir.2026.1860842/full

#### 当虚拟空间与真实空间一致时，“房间里的大象”会放大不适感（An elephant in the room amplifies discomfort when the virtual reality space matches physical reality） — Michael Wiesing, Mel Slater (2026-05)
- 类型: 行为研究 · 时序: 脚本 / 规则驱动
- 输入: 透视画面与实时环境, 身体、面部与视线追踪 → 输出: 人工制作的 VR 情境
- 核心想法: 把威胁放进参与者自己的房间会让人更难受——对于把内容写进真实环境的生成式 MR，这既是设计问题也是伦理问题。
- 内容: 29 名参与者在三种房间里遇到狼、狗、兔子或松鼠：通过混合现实透视看到的真实实验室、该实验室的 VR 复制品，或一个无关的虚拟客厅；牛顿摆可开可关。一个概率智能体请他们每次只改变一个因素；最令人不适的配置是混合现实中出现狼且牛顿摆在摆动。
- 实现方式: 被试内范式（动物 × 房间 × 牛顿摆）：参与者在概率智能体的提示下在各配置间切换；用马尔可夫转移矩阵对配置的不适程度排序。
- 参数: N=29 · 4 animals × 3 rooms × cradle on/off
- 能力维度: 感知真实感, 实验控制
- 论文: https://doi.org/10.1016/j.isci.2026.115951 (iScience (2026))
- 视频: https://www.youtube.com/watch?v=PdUq-_6ba5s

#### 用生成式 AI 制作高保真 360° 空间图像：作为实验刺激的方法学验证（Leveraging Generative AI for High-Fidelity 360° Spatial Images: Methodological Validation for Use as Experimental Stimuli） — Yoojin Han (2026-04-24)
- 类型: 行为研究 · 时序: 预先生成
- 输入: 文字提示 → 输出: 图像 / 全景图
- 核心想法: 生成的全景可以只改变一个被操纵的因素、其余保持不变，这正是实验所需要的；不过目前的验证依据是专家评分，而不是被试的行为。
- 内容: 一套为环境心理学实验制作受控 360° 刺激材料的流程：先用 Skybox AI（Model 4）生成固定的中庭全景，再用 Gemini 3 Flash Image（Nano Banana 2）以局部重绘方式加入绿植，形成八种布置与密度变体。图像质量指标显示拼接处畸变很少；七位资深专家在 Meta Quest 3 中观看后，对生成刺激的临场感评分高于传统三维建模的对照场景（7 分制 6.14 对 4.40）。
- 实现方式: 三阶段流程（以提示词生成结构、材质与光照固定的基础全景；用 AI 局部重绘在墙面、柱子与栏杆上加入绿植；验证），以 SSIM、LPIPS、BRISQUE、NIQE、MUSIQ、美学评分与 CLIP-IQA 评估，并由七位专家在头显中与传统建模的对照场景比较评分（Wilcoxon 符号秩检验）。
- 参数: 8K equirectangular base · 4K final · 8 variants · 7 expert raters · Meta Quest 3
- 能力维度: 实验控制, 创作可及性, 情境多样性
- 论文: https://doi.org/10.3390/buildings16091679 (Buildings 16(9):1679 (2026))
- 图片: https://pub.mdpi-res.com/buildings/buildings-16-01679/article_deploy/html/images/buildings-16-01679-i010.png https://pub.mdpi-res.com/buildings/buildings-16-01679/article_deploy/html/images/buildings-16-01679-g001.png

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

#### 真实与虚拟环境中疏散行为的社会影响（Social Influence on Evacuation Behavior in Real and Virtual Environments） — Max Kinateder (2016-07-25)
- 类型: 行为研究 · 时序: 脚本 / 规则驱动
- 输入: 身体、面部与视线追踪 → 输出: 人工制作的 VR 情境, 虚拟人（脸 / 身体）
- 核心想法: 真实与虚拟的匹配对照显示了哪些效应能延续（正向社会影响）、哪些会减弱（紧迫感、负向影响）——任何生成的紧急情境都需要这类验证。
- 内容: 火警响起时，150 名参与者要决定是否撤离：独自一人，或身边有一位要么离开、要么留下的旁观者；一半人在真实实验室，另一半在配有虚拟旁观者的、与之匹配的 VR 复制场景中。两种环境中都出现了同样的社会影响，但人们对虚拟火警的反应较弱，留下不走的旁观者在 VR 中的“拖住”作用也较弱。
- 实现方式: 单次试验的被试间实验，设三种旁观者条件，分别在真实实验室与在头戴显示器中呈现的匹配虚拟环境中进行。
- 参数: N=150 · 3 conditions × real / VR
- 能力维度: 实验控制, 情境可达性
- 论文: https://doi.org/10.3389/frobt.2016.00043 (Frontiers in Robotics and AI 3 (2016))
- 图片: https://www.frontiersin.org/files/Articles/204625/xml-images/frobt-03-00043-g001.webp

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

#### 借助虚拟现实与手机应用中的“未来自我”激发面向未来的思考与目标达成：随机对照试验（Stimulating Future-Oriented Thinking and Goal-Achievement Through the Future Self Using Virtual Reality and a Smartphone App: Randomized Controlled Trial） — Jean-Louis van Gelder (2026-03-10)
- 类型: 行为研究 · 时序: 脚本 / 规则驱动
- 输入: 语音与音频, 身体、面部与视线追踪 → 输出: 人工制作的 VR 情境, 虚拟人（脸 / 身体）
- 核心想法: 同一套“未来自我”干预分别用手机和头显实施：VR 显著提高了每周目标达成（d=0.88），但两种形式对未来自我认同的提升大多在六个月后消退。
- 内容: FutureU：大一学生与“十年后的自己”——一个按年龄老化处理的自我化身——见面，方式是手机应用，或三次各约 30 分钟的 VR 会话；在 VR 中，他们轮流化身为现在的自己和未来的自己，并回答自己事先录下的问题。一项三臂随机对照试验（N=321，每组 107 人）在六个月内比较了应用、VR 与目标设定对照组。
- 实现方式: 平行三臂随机对照试验，区组随机化；VR 会话使用由照片生成的全身“未来自我”化身、在现在与未来自我之间切换身体，并由研究者操控的机器人向导引导；用潜变量增长曲线模型分析六个时间点的结局。
- 参数: N=321 · 3 arms × 107 · 3 × 30 min VR · 6-month follow-up
- 能力维度: 适应性, 实验控制
- 论文: https://doi.org/10.2196/84420 (Journal of Medical Internet Research (2026))
- 视频: https://www.youtube.com/watch?v=4s5NDsyt6V4
- 项目主页: https://doi.org/10.2196/84420

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

#### 对虚拟儿童身体的错觉拥有感导致高估物体尺寸并改变内隐态度（Illusory ownership of a virtual child body causes overestimation of object sizes and implicit attitude changes） — Domna Banakou, Mel Slater (2013-07-15)
- 类型: 行为研究 · 时序: 脚本 / 规则驱动
- 输入: 身体、面部与视线追踪 → 输出: 人工制作的 VR 情境, 虚拟人（脸 / 身体）
- 核心想法: 被赋予的身体会改变知觉与内隐态度，而不只是感受——化身的选择本身就是实验变量。
- 内容: 30 名成年人在 VR 中被赋予一个 4 岁儿童的身体，或一个缩小到儿童身高的成人身体，且身体动作同步。两种条件都产生了强烈的身体拥有感，但只有儿童身体让人更高估物体尺寸，并更快地把自己与儿童特质联系起来；第二项实验（n=16）中，动作不同步消除了拥有感错觉及儿童身体特有的效应。
- 实现方式: 组间具身实验：头显第一人称视角配合全身动作捕捉，测量物体尺寸估计与内隐联想测验；第二项实验以视觉-运动不同步作为对照。
- 参数: Exp. 1 N=30 · Exp. 2 n=16
- 能力维度: 感知真实感, 实验控制
- 论文: https://doi.org/10.1073/pnas.1306779110 (PNAS 110(31) (2013))
- 视频: https://www.youtube.com/watch?v=8Oy83OVgbSM

#### 虚拟超级英雄：用虚拟现实中的超能力促进亲社会行为（Virtual Superheroes: Using Superpowers in Virtual Reality to Encourage Prosocial Behavior） — Robin S. Rosenberg, Jeremy Bailenson (2013-01-30)
- 类型: 行为研究 · 时序: 脚本 / 规则驱动
- 输入: 身体、面部与视线追踪 → 输出: 人工制作的 VR 情境
- 核心想法: 在 VR 中被赋予的“能力”——而不只是角色或故事——也能延续到头显之外的助人行为。
- 内容: 参与者要么像超人一样挥动手臂在虚拟城市上空飞行，要么作为乘客坐直升机；任务是寻找一个急需胰岛素的糖尿病儿童，或只是游览城市。之后，无论任务是什么，飞行组都比直升机组更多地帮实验者捡起洒落的笔。
- 实现方式: 2（超人飞行 / 直升机乘客）× 2（救援 / 游览任务）被试间实验，采用全身追踪；之后以安排好的“笔掉在地上”情境测量助人行为。
- 能力维度: 情境可达性, 实验控制
- 论文: https://doi.org/10.1371/journal.pone.0055003 (PLoS ONE 8(1) (2013))
- 图片: https://journals.plos.org/plosone/article/figure/image?size=inline&id=10.1371/journal.pone.0055003.g001

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

#### 沉浸式虚拟环境中的人际距离（Interpersonal Distance in Immersive Virtual Environments） — Jeremy Bailenson, Jim Blascovich (2003)
- 类型: 行为研究 · 时序: 脚本 / 规则驱动
- 输入: 身体、面部与视线追踪 → 输出: 人工制作的 VR 情境, 虚拟人（脸 / 身体）
- 核心想法: 人们会尊重虚拟人的个人空间，这让人际距离成为一种低成本、内隐的指标，用来判断生成的角色是否被当作社会性存在。
- 内容: 参与者在虚拟房间里从虚拟人身边走过，或被虚拟人走近；研究者操纵了性别、注视方式，以及该人物据称由人还是由计算机控制。人们与虚拟人正面保持的距离大于背面，会给保持对视的智能体留出更多空间，而当智能体闯入个人空间时退得最远。
- 实现方式: 两项沉浸式虚拟环境实验，参与者在头部追踪下行走；操纵参与者与虚拟人的性别、注视行为以及“智能体/化身”的说法，通过追踪记录最小距离与路径。
- 能力维度: 行为似真性, 实验控制
- 论文: https://doi.org/10.1177/0146167203029007002 (Personality and Social Psychology Bulletin 29(7) (2003))

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

#### 感知种族与性别对警察用语的影响：来自 VR 模拟的实验证据（The Effect of Perceived Race and Gender on Police Language Use: Experimental Evidence from VR Simulations） — Sandra C. Sandoval, Rashawn Ray (2026-08-05)
- 类型: 行为研究 · 时序: 脚本 / 规则驱动
- 输入: 语音与音频 → 输出: 人工制作的 VR 情境, 对话 / 文本
- 核心想法: 随机分配虚拟人物的身份，让一个 VR 场景变成检验警察逐轮实际话语中偏见的因果实验。
- 内容: 对一组 VR 现场实验的再分析：70 名美国警察在三个场景（住宅、公交站、便利店）中与虚拟角色对话，角色的种族与性别随机分配。多数警察对被呈现为黑人男性的角色说话时更不客气，在已知该角色是嫌疑人时尤其明显。
- 实现方式: 基于 Doan 等人的 VR 实验数据，对 3,897 条警察话语的众包“恭敬程度”评分（0–10）做话语层面的因果分析；用大语言模型提取文本特征、做倾向得分加权，并用大语言模型生成的改写句验证效应估计；论文还贡献了一个标注数据集。
- 参数: 70 officers · 208 scenes · 3,897 utterances
- 能力维度: 实验控制, 情境可达性
- 论文: https://arxiv.org/abs/2608.05050 (arXiv preprint (2026))
- 视频: https://www.youtube.com/watch?v=ZH3XgnpBGHM
- 项目主页: https://arxiv.org/abs/2608.05050

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

#### MAXLab 攻击与旁观者干预情境集（MAXLab_ABISS）（The MAXLab Aggression and Bystander Intervention Scenario Set (MAXLab_ABISS)） — Jean-Louis van Gelder (2024-10-18)
- 类型: 数据集 / 基准 · 时序: 脚本 / 规则驱动 · 获取方式: 仅限研究
- 输入:  → 输出: 360° / 立体视频
- 核心想法: 共享且可模块化的刺激材料，让暴力情境可以跨实验室、跨语言比较——这正是生成式变体需要达到的人工制作基线。
- 内容: 一套以酒吧为场景、可模块化组合的 360° 视频，提供英语、德语和荷兰语版本，让参与者置身于被陌生人羞辱、目睹年轻女性被骚扰或酒吧斗殴等情境，研究者可借此测量与暴力和干预相关的情绪与决策。两个样本（n=101、n=55）显示这些场景能引发预期的情绪。
- 实现方式: 在头显中观看的模块化 360° 视频场景，论文公开了制作过程、技术规格与研究者获取方式；在两个样本中以决策时刻的自评情绪进行验证。
- 参数: 360° video · EN / DE / NL · validation n=101 and n=55
- 能力维度: 实验控制, 情境可达性
- 论文: https://doi.org/10.1007/s11292-024-09645-6 (Journal of Experimental Criminology (2024))
- 视频: https://www.youtube.com/watch?v=T2p8UqTWN84

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

#### 沉浸式 VR 护理模拟中生成式 AI 辅助复盘与教师主导复盘对知识和非技术技能的影响：准实验研究（Comparing the effects of GenAI-assisted and facilitator-led debriefing on knowledge and non-technical skills in immersive virtual reality simulation in nursing education: A quasi-experimental study） — Patrick Pui Kin Kor (2026-07-18)
- 类型: 行为研究 · 时序: 回合制
- 输入:  → 输出: 对话 / 文本, 人工制作的 VR 情境
- 核心想法: 生成式 AI 可以接手复盘而不是情境本身；在随机分组之后“效果相当”是否仍然成立，还有待检验。
- 内容: 在一次沉浸式 VR 医院模拟之后，178 名护理本科生分别接受生成式 AI 工具主导的复盘加 10 分钟教师总结（n = 102），或仅由教师主持的复盘（n = 76）。两组知识得分均有提高（d = 0.79 与 0.72），校正基线后组间无差异，自评非技术技能也无差异。
- 实现方式: 准实验两组前后测设计，按选课分组；前后测采用选择题知识测验，后测加自评非技术技能，并以基线知识为协变量做协方差分析。
- 参数: N=178 (102 + 76) · quasi-experimental · knowledge d=0.79 vs. 0.72
- 能力维度: 实验控制, 适应性
- 论文: https://doi.org/10.1016/j.nedt.2026.107275 (Nurse Education Today (2026))

#### 用于 VR 警务训练的虚拟人：抵抗程度与手段可调的嫌疑人动态模型（Virtual Human for Police Training in Virtual Reality: A Dynamic Model of a Suspect With Modulated Resistance and Means） — Yvain Tisserand (2026-06-01)
- 类型: 行为研究 · 时序: 脚本 / 规则驱动
- 输入: 身体、面部与视线追踪, 语音与音频 → 输出: 虚拟人（脸 / 身体）, 智能体行为与动作, 语音 / 声音
- 核心想法: 两个可解释的“旋钮”就能让受过训练的警察产生可区分的威胁评估——这是大语言模型驱动的嫌疑人日后必须与之比较的可控基线。
- 内容: 一个警务处置场景中的虚拟嫌疑人，其表情、姿态、视线、移动与声音由两个参数驱动：抵抗程度（从服从到攻击）与手段（徒手或扳手）。58 名日内瓦在职警察在 VR 中各自处理了六种“抵抗 × 手段”组合场景；抵抗程度主要改变感知到的危险与意图，手段则改变感知到的能力与机会。
- 实现方式: 基于“相称使用武力”原则的状态机行为模型，用 Unity 开发并在 HTC Vive Pro Eye 上运行；受限语音识别，由教官确认指令；被试内评估，场景顺序平衡，问卷在 VR 内完成。
- 参数: N=58 officers · 6 scenarios within-subjects
- 能力维度: 行为似真性, 实验控制
- 论文: https://doi.org/10.1002/cav.70129 (Computer Animation and Virtual Worlds (CASA XR 2026))

#### 帮助自闭症人士与警察互动的虚拟现实干预：面向自闭症青少年与成人的随机对照临床试验（Virtual Reality Intervention to Empower Autistic People to Interact With Police: A Randomized Controlled Clinical Trial for Autistic Teens and Adults） — Joseph P. McCleery, Floreo (2026-05-06)
- 类型: 行为研究 · 时序: 脚本 / 规则驱动
- 输入: 身体、面部与视线追踪 → 输出: 人工制作的 VR 情境, 虚拟人（脸 / 身体）
- 核心想法: 结局在与真实警察的现场接触中测量——这是多数 VR 训练研究省略的迁移检验；三项结局中只有一项显示出可靠的组间差异。
- 内容: 47 名 12 至 60 岁的自闭症人士被随机分配，接受三次各 45 分钟的 Floreo VR 警察安全模块训练或视频示范训练，然后在与真实警察的现场互动中接受测试。现场互动中的小动作只在 VR 组减少；对“按预期回应”和整体表现，组别 × 时间交互作用不显著，但计划内检验显示 VR 训练后有所改善。
- 实现方式: 平行随机对照试验（Floreo VR 对比 BeSAFE 视频示范），三次训练间隔约九天，在训练前后的真实警察互动中对行为编码；由美国国立卫生研究院资助，与费城儿童医院自闭症研究中心合作。
- 参数: N=47 · ages 12–60 · 3 × 45 min
- 能力维度: 情境可达性, 实验控制
- 论文: https://doi.org/10.1007/s10803-026-07339-8 (Journal of Autism and Developmental Disorders (2026))
- 视频: https://www.youtube.com/watch?v=eFVottnTn-w
- 项目主页: https://floreovr.com/research

#### AI 该先开口吗？混合现实医学训练中主动与被动引导的比较（Should the AI Speak First? Evaluating Proactive vs. Reactive Facilitation in Mixed-Reality Medical Training） — Duo Wang (2026-04-13)
- 类型: 行为研究 · 时序: 回合制
- 输入: 语音与音频 → 输出: 语音 / 声音, 对话 / 文本
- 核心想法: 生成角色何时主动开口本身就是一个设计变量，它取决于任务阶段和认知负荷，而不是一个固定设置。
- 内容: 医学生在混合现实模拟器中练习腰椎穿刺，AI 引导者或主动提供指导与鼓励，或只在被询问时回答（n = 22）。两种方式在学习结果、互动频率和体验评分上没有差异，但访谈和行为记录显示：主动帮助在某些任务阶段受欢迎，在另一些阶段则造成干扰。
- 实现方式: 在 XR 腰椎穿刺模拟器中，以 22 名医学生比较 AI 引导者（可能与该团队的 EmSim 一样基于大语言模型）的主动与被动两个版本；测量学习结果、互动日志、体验评分，并进行行为分析与访谈，最终归纳出 AI 主动性的边界框架。
- 参数: n=22 · proactive vs. reactive · lumbar puncture simulator
- 能力维度: 时间响应性, 适应性
- 论文: https://doi.org/10.1145/3772318.3791910 (CHI 2026)

#### 补充职前护士的病人接诊训练：迈向 AI×VR 方法（Supplementing Patient Encounter Training for Preservice Nurses: Towards an AI×VR Approach） — Yupei Duan (2026-01-26)
- 类型: 行为研究 · 时序: 回合制
- 输入: 语音与音频 → 输出: 虚拟人（脸 / 身体）, 语音 / 声音, 对话 / 文本
- 核心想法: 信心和临场感提高了，考核表现却没有变化；这提醒我们要测量迁移效果，而不只是体验。
- 内容: 职前护士在参加标准化病人考核前，在沉浸式 VR 中与生成式 AI 驱动的虚拟标准化病人练习（使用系统 23 人，对照 34 人）。一次练习就把自我效能从 3.74 提高到 4.11，可用性评分 81.6/100；但考核表现与对照组没有差异，也与临场感和沉浸感无关。
- 实现方式: 混合方法研究，实验组 23 人、对照组 34 人；测量 SUS、前后测自我效能、标准化病人考核得分、投入度与临场感问卷，并进行访谈；作者据此提出限制回复长度、支持可靠插话打断等设计建议。
- 参数: N=57 (23 + 34) · single session · SUS 81.6
- 能力维度: 时间响应性, 实验控制
- 论文: https://doi.org/10.1109/aixvr67263.2026.00020 (IEEE AIxVR 2026)

#### AI 增强的 VR 模拟提升护生共情：自动评分与评分者一致性的随机对照研究（AI-enhanced virtual reality simulation for nursing students' empathy: Automated scoring and inter-rater reliability in a randomised controlled study） — Pao-Ju Chen (2026-01-05)
- 类型: 行为研究 · 时序: 回合制
- 输入:  → 输出: 人工制作的 VR 情境, 对话 / 文本
- 核心想法: 同一个 AI 既能运行情境、又能评分；只要其评分与专家判断一致，评估就不再是反复练习的瓶颈。
- 内容: 护理学生在第一人称 VR 模拟（VR-AI-ECS）中练习产科情境下的共情沟通，系统提供 AI 引导的对话与实时反馈；对照组使用含标准化病人互动的 360° 视频（各 40 人）。VR-AI 组在训练后即刻（d = 0.96）和随访时（d = 0.60）的共情沟通得分更高，AI 评分与教师评分高度一致（ICC = 0.81）。
- 实现方式: 随机对照混合方法试验（40 + 40），比较含 AI 引导对话与反馈的 VR 和含标准化病人的 360° 视频；在三个时间点用共情沟通表现评定量表评估，由 AI 与教师分别评分，采用广义估计方程与组内相关系数分析，并辅以焦点小组访谈。
- 参数: N=80 (40 + 40) · d=0.96 post, d=0.60 follow-up · AI–educator ICC=0.81
- 能力维度: 适应性, 实验控制
- 论文: https://doi.org/10.1016/j.nedt.2025.106968 (Nurse Education Today (2026))

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

#### VR 中 AI 生成的个性化安全之地与传统安全之地想象的比较：随机对照试验（AI-Generated Personalized Visualization of the Safe Place in Virtual Reality vs Traditional Safe Place Imagery: Randomized Controlled Trial） — Franziska Grießenauer (2026-07-24)
- 类型: 行为研究 · 时序: 预先生成
- 输入: 文字提示 → 输出: 图像 / 全景图
- 核心想法: 最早让每位参与者进入由其本人描述生成的世界的随机试验之一；结果是生成的场景并不比想象更有效。
- 内容: 60 名成人先想象一个属于自己的“安全之地”，完成压力任务后放松三分钟：一组在 Meta Quest 3 中进入根据本人描述生成的 360° 全景（n = 30），另一组闭眼想象（n = 30）。两组放松程度同样上升，即时与五天随访均无差异；临场感和对生成场景的满意度不能预测放松效果，而想象的生动程度可以。
- 实现方式: 随机对照试验（30 + 30），含压力诱导；实验组每人的安全之地由 PsyTechVR 平台中的 MindGap AI（与 Stable Diffusion 同类的潜在扩散模型，带 LDM3D 深度扩展）生成为无声的静态 360° 全景；测量放松状态问卷、视觉意象生动性问卷与 IPQ 临场感量表，并进行为期五天的每日在线随访。
- 参数: N=60 (30 + 30) · Meta Quest 3 · 3-min exposure · 5-day follow-up
- 能力维度: 适应性, 情境多样性
- 论文: https://doi.org/10.2196/82647 (JMIR AI 5:e82647 (2026))

#### Refugio — Pau Mora (2026-03-13)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 语音与音频 → 输出: 网格 / 三维资产, 对话 / 文本
- 核心想法: 按需生成平静之地中的物件，让当事人自己设计治疗情境；但每个物件约两分钟的等待，本身也成了体验的一部分。
- 内容: 一款 Meta Quest 3 应用：用户用语音布置一个用于心理治疗的“安全之地”。自托管的 Gemma 3 模型先过滤请求，Sana v1.0 生成候选图像，再由 Zero123++ 与 InstantMesh 把选中的图像变成三维物体，每个约需两分钟。在一项 30 名非临床参与者的单次可行性研究中，可用性很高（SUS 86.3）、工作负荷低；创作过程中效价上升，随后的冥想中唤醒度下降。
- 实现方式: 语音（Wit.ai）→ Gemma 3 过滤请求 → Sana 生成图像 → 用户挑选 → Zero123++ 生成多视角 → InstantMesh 重建网格，运行在本地三 GPU 服务器上；单组研究（N = 30），测量 SUS、NASA-TLX、改编版 RJPQ 与三个时间点的 SAM 评分。
- 参数: ~117 s per object · N=30 · Meta Quest 3 · SUS 86.3
- 能力维度: 共创与能动性, 适应性
- 论文: https://doi.org/10.3389/frvir.2026.1760765 (Frontiers in Virtual Reality (2026))
- 图片: https://www.frontiersin.org/files/Articles/1760765/xml-images/frvir-07-1760765-g003.webp https://www.frontiersin.org/files/Articles/1760765/xml-images/frvir-07-1760765-g001.webp
- 项目主页: https://www.frontiersin.org/journals/virtual-reality/articles/10.3389/frvir.2026.1760765/full

#### 针对精神病痛苦幻听的数字化身疗法：II/III 期 AVATAR2 试验（Digital AVATAR therapy for distressing voices in psychosis: the phase 2/3 AVATAR2 trial） — Philippa Garety (2024-10-28)
- 类型: 行为研究 · 时序: 实时流式
- 输入: 语音与音频 → 输出: 虚拟人（脸 / 身体）, 语音 / 声音
- 核心想法: 内心声音的可控化身可以被直面和改变，但获益在第 28 周已消退——提醒沉浸式治疗试验需要长期随访。
- 内容: 听到痛苦幻听的人与一个数字面孔进行由治疗师引导的对话，这个面孔的声音由治疗师通过实时变声现场发出。在一项有 345 名参与者的多中心 II/III 期试验中，简短版（6 次）和扩展版（12 次）分别叠加常规治疗，都在第 16 周降低了与幻听相关的痛苦，但第 28 周时效果不再显著。
- 实现方式: 多中心、评估者盲法随机试验，比较 AVATAR 简短版和扩展版（均叠加常规治疗）与单纯常规治疗，采用意向性分析；治疗师通过实时变声为化身配音。
- 参数: N=345 · 3 arms · follow-up 16 and 28 weeks
- 能力维度: 反应性, 适应性
- 论文: https://doi.org/10.1038/s41591-024-03252-8 (Nature Medicine (2024))
- 视频: https://www.youtube.com/watch?v=8BwQu8oS8XY

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
- 内容: 用于慢性下背痛的处方型居家 VR 项目，通过每日简短课程教授呼吸、放松、注意力转移等疼痛管理技巧；2021 年获美国 FDA De Novo 授权。此后又获两次 FDA 510(k) 许可（2024 年 12 月；2025 年 8 月，适用于 Pico G3 头显），产品网站截至 2026 年 10 月仍在运行。
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

#### 生成式 AI 辅助的虚拟现实牙科技能训练对学习表现、视觉行为与皮层激活的影响：分层随机对照试验（Effects of Generative AI-Supported Virtual Reality Dental Skill Training on Learning Performance, Visual Behavior, and Cortical Activation Among Dental Students: Stratified Randomized Controlled Trial） — Yuting Wen (2026-10-01)
- 类型: 行为研究 · 时序: 回合制
- 输入: 文字提示, 身体、面部与视线追踪 → 输出: 人工制作的 VR 情境, 对话 / 文本
- 核心想法: 生成式 AI 作为人工制作的模拟器中的导师（而不是模拟器本身），可以在随机设计中与人类教师正面比较。
- 内容: 牙科学生在 VR 模拟器中进行为期七天的操作技能训练，一组只有 ChatGPT 指导、没有人类导师（n=62），另一组由教师现场指导（n=61）。ChatGPT 组的操作技能测试得分更高（77.3 对 67.4，d=0.70）；训练中同时记录了眼动与功能性近红外光谱数据。
- 实现方式: 按理论基线分层的随机对照试验，比较生成式 AI 辅助与教师主导的 VR 牙科训练；研究助理仅出于安全目的审查 AI 输出；结局包括操作考核、眼动追踪、功能性近红外光谱、视觉空间测验与问卷。
- 参数: N=123 (62 + 61) · 7 days · d=0.70
- 能力维度: 适应性, 实验控制
- 论文: https://doi.org/10.2196/90938 (Journal of Medical Internet Research (2026))

#### 倾听与镜像：言语共情与行为模仿对 VR 中具身 AI 智能体社会与共情感知的影响（Listening and Mirroring: The Effects of Verbal Attunement and Behavioral Mimicry on Social and Empathic Perceptions of Embodied AI Agents in VR） — Nathalia Gomez (2026-09-23)
- 类型: 行为研究 · 时序: 回合制
- 输入: 语音与音频, 身体、面部与视线追踪 → 输出: 虚拟人（脸 / 身体）, 语音 / 声音, 对话 / 文本
- 核心想法: 对大语言模型驱动的角色来说，说什么比身体是否模仿你更能左右被感知到的共情。
- 内容: VR 中的具身 AI 咨询师：通过 GPT-4o mini 作答，并能借助 Meta Quest Pro 的追踪模仿用户的面部表情、头部倾斜与姿势。在 2 × 2 被试内研究（N = 20）中，言语上的共情回应提高了被感知的共情，而行为模仿只对“像人程度”有边缘效应，两者的作用也不能简单相加。
- 实现方式: Unity 应用，结合 Deepgram 语音识别与语音合成、经 LiveKit 调用的 GPT-4o mini、Ready Player Me 化身以及 Quest Pro 面部追踪实现模仿；2 × 2 重复测量设计（言语共情 × 行为模仿），N = 20，重复测量方差分析。
- 参数: N=20 · 2×2 within-subjects · Meta Quest Pro
- 能力维度: 行为似真性, 时间响应性
- 论文: https://arxiv.org/abs/2609.27246 (ACM VRST 2026 (arXiv preprint))
- 图片: https://arxiv.org/html/2609.27246v1/Teaser.png https://arxiv.org/html/2609.27246v1/FacialMimicry.png

#### AI 幻觉的信号：为 VR 中的具身对话智能体设计幻觉提示（Signals of AI Hallucination: Designing Hallucination-Aware Cues for Embodied Conversational Agents in VR） — Xiaoran Yang (2026-09-23)
- 类型: 行为研究 · 时序: 回合制
- 输入: 语音与音频 → 输出: 虚拟人（脸 / 身体）, 语音 / 声音, 对话 / 文本
- 核心想法: 生成的角色难免说错话；角色自己如何表达“不确定”，既影响人们能否发现错误，也影响他们有多信任它。
- 内容: 在 VR 中，一个由 GPT-4o 驱动的具身智能体回答问题，并以三种方式之一提示不确定性与来源：手势与姿态、状态图标，或带引用的彩色标注文本。被试内研究（N=24）显示，与无提示相比，三种方式都帮助人们识别出幻觉内容；具身提示提高了信任与沉浸感，文本提示最容易理解。
- 实现方式: 被试内比较具身、图标与文本三种提示和无提示基线，后端采用基于忠实度的幻觉检测；收集幻觉识别日志、信任、沉浸感与任务负荷问卷及访谈。
- 参数: N=24 · 4 conditions within-subjects
- 能力维度: 实验控制, 行为似真性
- 论文: https://arxiv.org/abs/2609.28812 (ISMAR 2026 (IEEE TVCG))
- 图片: https://arxiv.org/html/2609.28812v1/Group49.png

#### 从抓取到表达：面向自闭症人士、基于生成式 AI 并与环境关联的 VR 沟通训练（From Grasping to Speaking: Generative AI-Based Environment-Grounded VR Communication Training for Autistic Individuals） — Ziming Li (2026-09-22)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 语音与音频, 身体、面部与视线追踪 → 输出: 虚拟人（脸 / 身体）, 对话 / 文本, 语音 / 声音
- 核心想法: 让智能体的话语与手头任务相关联，把软技能练习从孤立的聊天变成嵌入工作中的沟通。
- 内容: 这是该团队大语言模型职场沟通训练系统的后续工作：智能体生成的对话与 VR 工作场景以及受训者手上的动作相关联。ASSETS 2026 上的一项探索性研究有 9 名自闭症受训者和 7 名就业辅导员参与，比较了仅对话、对话加物体、对话加物体与抓取三种条件；两类参与者都更喜欢关联程度最高的条件。
- 实现方式: 提示词框架把 VR 物体状态与手部交互事件输入大语言模型智能体；以可用性、工作负荷与偏好为指标，对三种关联条件做探索性的被试内比较。
- 参数: 9 autistic trainees · 7 job coaches · 3 conditions
- 能力维度: 反应性, 行为似真性
- 视频: https://www.youtube.com/watch?v=54krjoYva5Q

#### 与港海豹一起 VR 潜水可增强海洋联结感，而对话式 AI 对护海参与的影响取决于此前与海豹的接触经历（VR scuba diving with harbor seals increases ocean connectedness, and the effect of conversational AI on pro-environmental engagement depends on prior experience with seals） — Gustav Bøg Petersen, Jeremy Bailenson (2026-09-07)
- 类型: 行为研究 · 时序: 回合制
- 输入: 语音与音频 → 输出: 人工制作的 VR 情境, 虚拟人（脸 / 身体）, 对话 / 文本
- 核心想法: 配对对照解决了研究生成式对话的核心难题：每个对照者看到的正是某位实验组参与者得到的内容，从而分离出“互动”本身的效应。
- 内容: 在 OceanSpeak 中，参与者在 VR 里潜水，并与一只 AI 驱动的港海豹谈论海洋酸化与过度捕捞。一项预注册研究（N=106）采用“配对对照”设计：对照组看到完全相同的内容，包括另一位参与者与 AI 的对话，但自己不能开口。
- 实现方式: 与斯坦福虚拟人交互实验室合作的预注册被试间实验，以配对回放 AI 对话作为对照；结局指标包括海洋联结感、对海豹的共情、护海行为与知识。
- 参数: N=106 (53 + 53 yoked controls)
- 能力维度: 实验控制, 反应性
- 论文: https://doi.org/10.1016/j.cexr.2026.100181 (Computers & Education: X Reality (2026))

#### “嘿，AI，你能让我紧张吗？”虚拟社会应激范式中文本转语音与真人语音的比较（Hey AI: Can you trigger me? A comparison of Text-to-Speech synthesis and human speech in a virtual social stress paradigm） — Sarah Roßkopf (2026-08)
- 类型: 行为研究 · 时序: 预先生成
- 输入:  → 输出: 语音 / 声音
- 核心想法: 合成语音同样能传递社会评价威胁，这让虚拟评审可以说出新内容，而不必只回放录音。
- 内容: 虚拟版特里尔社会应激测试（TSST）中，评审委员会分别使用文本转语音或预先录制的真人语音。两种条件都引发了明显的应激反应；两种语音条件下的心率上升在统计上等效，而自评应激与临场感的等效性只得到中等程度的支持。
- 实现方式: 随机对照试验，在 VR-TSST 中比较虚拟委员会使用文本转语音与预录真人语音；测量心率、斜方肌肌电以及自评应激、临场感与情绪，并做等效性检验。
- 参数: RCT · VR-TSST · TTS vs. prerecorded human speech
- 能力维度: 感知真实感, 实验控制
- 论文: https://doi.org/10.1016/j.chbah.2026.100371 (Computers in Human Behavior: Artificial Humans (2026))

#### CyberSelf：在虚拟现实中以具身自我疏离提供情绪支持（CyberSelf: Embodied Self-Distancing for Emotional Support in Virtual Reality） — Bing Li (2026-07-09)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 语音与音频, 视频 → 输出: 虚拟人（脸 / 身体）, 语音 / 声音, 对话 / 文本
- 核心想法: “像自己”的程度变成可调参数：生成的相似性（文本、声音、面孔）可以逐层打开，并分别测量其对情绪调节的作用。
- 内容: 用户在 VR 中与“数字分身”对话：这个化身由约 20 秒的面部视频重建，用其克隆的声音说话，对话由大语言模型驱动。短期研究（n=24）比较了纯文本、文本+声音、文本+声音+外貌三种条件；为期四周的研究（n=12）以压力较大的博士生为对象，检验了反复使用的效果。
- 实现方式: 用 Unreal Engine 5 从短视频重建化身，结合声音克隆、Whisper 语音输入与大语言模型对话；被试内比较三种表征层级，测量问卷与生理指标，并开展为期四周的自我关怀纵向研究。
- 参数: N=36 (24 short-term + 12 four-week) · ~20 s face video + ~19 s voice sample
- 能力维度: 适应性, 感知真实感
- 论文: https://arxiv.org/abs/2608.07521 (arXiv preprint (2026))
- 图片: https://arxiv.org/html/2608.07521v1/teaser.png
- 项目主页: https://arxiv.org/abs/2608.07521

#### 面向 VR 演讲练习的大语言模型教练智能体：设计与评估（Designing and evaluating LLM-driven coaching agents for VR public speaking practice） — Enyao Chang (2026-07-08)
- 类型: 行为研究 · 时序: 回合制
- 输入: 语音与音频, 身体、面部与视线追踪 → 输出: 虚拟人（脸 / 身体）, 语音 / 声音, 对话 / 文本
- 核心想法: 注意力匹配的对照组分离出了大语言模型的贡献：起作用的是量身定制的指导，而不只是“有个会说话的智能体”。
- 内容: 在 VR 礼堂中，具身的虚拟评委在每次演讲后给出口头的、针对表现的指导，内容由文心一言（ERNIE Bot）根据语音识别与视线线索生成。两臂随机研究（N=120）显示：与注意力匹配的通用反馈相比，自适应指导更明显地降低了自评演讲焦虑，差异在一周和一个月随访时仍可见。
- 实现方式: VR 系统集成语音识别、语音合成、视线线索，并以三级结构化提示调用文心一言；60/60 随机用户研究，重复测量状态焦虑与 PRCA 量表，并在一周和一个月后随访。
- 参数: N=120 (60 + 60) · follow-up 1 week and 1 month
- 能力维度: 适应性, 时间响应性
- 论文: https://doi.org/10.3389/fpsyg.2026.1886780 (Frontiers in Psychology (2026))
- 图片: https://www.frontiersin.org/files/Articles/1886780/xml-images/fpsyg-17-1886780-g0001.webp https://www.frontiersin.org/files/Articles/1886780/xml-images/fpsyg-17-1886780-g0002.webp
- 项目主页: https://www.frontiersin.org/journals/psychology/articles/10.3389/fpsyg.2026.1886780/full

#### 探索沉浸式三方协作决策中具身虚拟智能体的调解作用（Exploring Mediation by an Embodied Virtual Agent in Immersive Triadic Collaborative Decision-Making） — Binyang Han (2026-05)
- 类型: 行为研究 · 时序: 回合制
- 输入: 语音与音频 → 输出: 虚拟人（脸 / 身体）, 语音 / 声音, 对话 / 文本
- 核心想法: 大语言模型“队友”在群体中的价值在于它如何塑造社会互动；它的策略是涌现的而非预设的，因此也更难控制。
- 内容: 目标相互冲突的两名用户在 XR 中共同设计一间办公室，由一个大语言模型驱动的智能体进行调解；智能体或有具身形象，或只是无形的声音，并与无智能体条件比较（论文报告 n=24 组）。具身形象提高了共同临场感与感知到的协作质量，但没有提高任务效率；智能体还在未经专门编程的情况下，自发采用了促进式与评估式的调解策略。
- 实现方式: XR 协作研究，操纵智能体是否在场及是否具身，测量共同临场感、协作、偏好与效率，并对照冲突解决模式对智能体的调解策略做质性编码。
- 参数: pairs (n=24 reported) · 3 agent conditions
- 能力维度: 行为似真性, 共创与能动性
- 论文: https://doi.org/10.1109/tvcg.2026.3679103 (IEEE VR 2026 (IEEE TVCG))

#### 生成式 AI 支持的虚拟病人在医疗卫生教育中的应用：系统综述（GenAI-Supported Virtual Patients in Health Care Education: Systematic Review） — Juming Jiang (2026-05-07)
- 类型: 论文 / 综述
- 输入: 文字提示, 语音与音频 → 输出: 对话 / 文本, 语音 / 声音, 虚拟人（脸 / 身体）
- 核心想法: 生成式虚拟病人的证据几乎都来自平面屏幕；沉浸式的对照研究正是空白所在。
- 内容: 一篇系统综述，纳入 15 项评估生成式 AI 虚拟病人的研究（共 645 名参与者），涵盖护理、医学、药学、放射学与急救人员培训。其中 13 项使用 OpenAI 的 GPT 模型，6 项采用三维具身化身，只有 1 项在头戴显示器中呈现病人；多数干预只有一次训练、没有随访，因此作者认为证据在可行性上有希望，但在学习效果上仍属初步。
- 实现方式: 检索 CINAHL、Medline、Embase、Scopus 与 Web of Science 至 2026 年 3 月；两人独立筛选与提取；采用 JBI 质量评价清单；叙述性综合。
- 参数: 15 studies · N=645 · 3 RCTs · 1 HMD study
- 能力维度: 行为似真性, 实验控制
- 论文: https://doi.org/10.2196/82756 (Journal of Medical Internet Research 28:e82756 (2026))

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

#### 社交 VR 中用于缓解外语口语焦虑的大语言模型具身对话智能体（LLM-based Embodied Conversational Agent for Reducing Foreign Language Speaking Anxiety in Social VR） — Mengxu Pan (2026-04-13)
- 类型: 行为研究 · 时序: 回合制
- 输入: 语音与音频 → 输出: 虚拟人（脸 / 身体）, 语音 / 声音, 对话 / 文本
- 核心想法: 一个耐心、不评判的对话伙伴很难长期由真人担任，却容易生成；不过目前的证据仍来自一个没有对照组的小样本。
- 内容: 英语学习者连续五天、每天 30 分钟，在三个社交 VR 场景中与大语言模型驱动的具身智能体进行角色扮演。三天后自评外语焦虑显著下降，口语指标略有提升；学习者认为这得益于智能体不评判的态度、语言支架和情感鼓励。
- 实现方式: 为期五天的混合方法研究（N = 20，无对照组），每天在社交 VR 中与基于大语言模型的具身智能体进行 30 分钟角色扮演；测量外语焦虑量表、口语能力指标并进行访谈。
- 参数: N=20 · 5 days × 30 min · 3 scenarios
- 能力维度: 适应性, 情境可达性
- 论文: https://doi.org/10.1145/3772318.3791068 (CHI 2026)

#### 量化延迟：用会话分析研究虚拟现实中的人与智能体互动（Quantifying Latencies: A Conversation Analysis Approach to Human-Agent Interactions in Virtual Reality） — Raina Cao (2026-04-13)
- 类型: 行为研究 · 时序: 回合制
- 输入: 语音与音频 → 输出: 虚拟人（脸 / 身体）, 语音 / 声音, 对话 / 文本
- 核心想法: 最先打破错觉的是话轮转换，而不是内容；几秒钟的沉默是可以量化的似真性代价。
- 内容: 对社交 VR 中人与大语言模型智能体的口语对话进行会话分析，测量回应时序与修复行为。智能体回应的中位延迟为 4.1 秒，人类说话者为 1.2 秒；作者将其描述为“对话时序漂移”：智能体开口太晚，被打断时又不能很快停下。
- 实现方式: 对社交 VR 中人与智能体的对话进行会话分析编码，测量智能体与人的回应延迟、开口延迟、被打断后的收声延迟以及修复尝试；作者称这是首次在 VR 中对人与智能体的对话延迟进行实证量化。
- 参数: median response latency 4.1 s (agent) vs. 1.2 s (human)
- 能力维度: 时间响应性, 行为似真性
- 论文: https://doi.org/10.1145/3772318.3790947 (CHI 2026)

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

#### 什么让 VR 中的虚拟名人智能体值得信任？风格化与声音的作用（What Makes a Virtual Celebrity Agent Trustworthy in VR? Exploring the Role of Stylization and Voice） — Yang Gao (2026-03)
- 类型: 行为研究 · 时序: 脚本 / 规则驱动
- 输入: 视频 → 输出: 虚拟人（脸 / 身体）, 语音 / 声音
- 核心想法: 同一人物的生成版与手工版可以当作刺激来比较；在这里，外观对信任的影响大于声音是否克隆。
- 内容: 研究者为电视角色 Sheldon Cooper 制作了六个 VR 版本——手工雕刻、AI 重建或非风格化外观，各配克隆声音或合成声音——并与原始视频片段比较。3×2 被试内实验（N=30）显示：外观风格影响信任、真实感、熟悉度与社会临场感；声音类型只影响真实感与熟悉度。
- 实现方式: 3（外观风格）× 2（声音类型）被试内 VR 实验，以视频为基线，测量信任、真实感、熟悉度与社会临场感问卷，并记录人际距离。
- 参数: N=30 · 3×2 within-subjects
- 能力维度: 感知真实感, 实验控制
- 论文: https://doi.org/10.1109/tvcg.2026.3680715 (IEEE VR 2026 (IEEE TVCG))
- 视频: https://www.youtube.com/watch?v=1aSmlWFmQNQ

#### 人工智能用于虚拟现实暴露疗法（VRET）：一项系统综述（Artificial intelligence (AI) for virtual reality exposure therapy (VRET): A systematic review） — Kamilla Bergsnev (2026-03-26)
- 类型: 论文 / 综述
- 输入: 身体、面部与视线追踪, 语音与音频 → 输出: 人工制作的 VR 情境
- 核心想法: 自适应暴露——根据患者当下状态调整所恐惧的情境——是最接近实时生成的临床用例，而其证据基础仍然有限。
- 内容: 按 PRISMA 流程纳入截至 2025 年 11 月发表的 23 篇同行评审文章，系统梳理如何用人工智能让 VR 暴露疗法更贴合患者与治疗师的需要。
- 实现方式: 遵循 PRISMA 的系统综述，检索 PsycINFO、Web of Science、Google Scholar、EMBASE、CINAHL 与 MEDLINE，从 377 条记录中纳入 23 篇。
- 参数: 23 of 377 records
- 能力维度: 适应性, 实验控制
- 论文: https://doi.org/10.1038/s41398-026-03936-4 (Translational Psychiatry (2026))

#### OasisMind — Ruoyu Wen (2026-03-03)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 文字提示 → 输出: 图像 / 全景图, 音效、音乐与空间音频, 对话 / 文本
- 核心想法: 让参与者自己创作情境能提高偏好，却不会提高临场感；当生成世界被用作干预手段时，这种分离值得重视。
- 内容: 一个 AI 辅助的 VR 系统：人们用自然语言描述一个能给自己情绪支持的地方，系统随之生成 360° 环境、相应的环境音景，以及能感知情境的数字陪伴者。在 24 人的研究中，参与者更偏爱自己创造的环境，而不是经过验证的预设放松场景，但满意度与临场感没有差异。
- 实现方式: 由提示词驱动的流程在头显中生成 360° 全景、环境音频和一个（可能由大语言模型驱动的）陪伴者；用户研究（N = 24）比较自建环境与经过验证的预设 VR 场景在偏好、满意度与临场感上的差异。
- 参数: N=24 · generated 360° environment + soundscape + companion
- 能力维度: 共创与能动性, 适应性
- 论文: https://doi.org/10.1145/3742413.3789067 (IUI 2026)
- 视频: https://www.youtube.com/watch?v=zG1x0sNmxZc

#### EmSim：面向执法人员冲突降级训练的 AI 驱动 VR 模拟（EmSim: AI-Driven VR Simulation for De-Escalation Training in Law Enforcement） — Duo Wang (2026-01-26)
- 类型: 研究演示 · 时序: 回合制 · 获取方式: 仅限研究
- 输入: 语音与音频 → 输出: 虚拟人（脸 / 身体）, 语音 / 声音, 对话 / 文本
- 核心想法: 同一场景中大语言模型扮演两个角色：一个扮演情绪激动的人，另一个为学员的话打分并沿升级路径推动场景，让后果取决于所说的话。
- 内容: 警校学员与一位情绪激动的虚拟人（基于 Unreal Engine 数字人、由 Convai 驱动语音对话）自由交谈；GPT-4-turbo 评估器按共情量表为每句话打分，分数决定场景是升级还是缓和，教官仪表盘实时显示这些分数。一项有 14 名学员和 5 名教官参与的试点研究发现了两种策略：谨慎降级与试探边界。
- 实现方式: Unreal Engine 场景配合 Convai 语音对语音角色，由 PC 串流到 Meta Quest 3；GPT-4-turbo 按量表为每句话打分，结果输入升级状态管理器和教官网页仪表盘；混合方法试点，分析行为轨迹与课后访谈。
- 参数: pilot: 14 police trainees · 5 trainers
- 能力维度: 反应性, 情境可达性
- 论文: https://doi.org/10.1109/AIXVR67263.2026.00014 (IEEE AIxVR 2026)

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
- 内容: World Labs 为 Marble 世界模型开放的公开 API：输入文字、一张或多张图片、360° 全景图或一段视频，就能得到可在浏览器中渲染、也可导出到其他工具的可漫游三维世界。World Labs 介绍的用例包括把二维电影变成可探索的空间（Escape.ai），以及为 Isaac Sim、MuJoCo 等机器人仿真器生成环境。2026-09-28，World Labs 签署协议并入 AMD，交易预计于 2026 年底前完成。
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

#### Inworld Unreal AI Runtime — Inworld AI (2025-10-29)
- 类型: 平台 / API · 时序: 回合制 · 获取方式: 产品 / 应用
- 输入: 语音与音频, 文字提示 → 输出: 对话 / 文本, 语音 / 声音, 智能体行为与动作
- 核心想法: NPC 技术栈变成一张可配置、可追踪的流程图：同一个角色流水线可以在不同模型之间切换，每一步都有记录，这正是研究所需要的可检查性。
- 内容: Inworld 面向 Unreal Engine 的插件：用一个 API 密钥统一调用语音识别、大语言模型和语音合成（来自多家提供商的 100 多个模型），配有可视化节点图编辑器来搭建语音到语音的 NPC 对话等流水线，并提供 NPC 与聊天机器人模板，以及内置的日志、链路追踪和成本面板。
- 实现方式: Unreal Engine SDK，通过统一的多提供商 API 和节点图编辑器提供语音识别、大语言模型与语音合成模块，附带模板（包括 Inworld 的 Character Template）以及可观测性与实验工具；同日推出 Unity AI Runtime SDK 抢先体验版。它承接 Inworld 早期的角色引擎；发布文章称后者是公司服务游戏开发者的起点。
- 参数: 100+ models via one API key · Unreal Engine (Unity in early access)
- 能力维度: 创作可及性, 实验控制
- 视频: https://www.youtube.com/watch?v=XvEx7_jhnBc
- 图片: https://static.inworld.ai/public-website-2025/images/content/712fb09391e460fe1ce715a9bd49f9f05ebb30b4-1400x788.jpg
- 项目主页: https://inworld.ai/blog/introducing-unreal-ai-runtime-sdk

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

#### Playground（含 Unity Spark）（Playground (with Unity Spark)） — 谷歌, Unity (2026-10-07)
- 类型: 平台 / API · 时序: 回合制 · 获取方式: 产品 / 应用, 候补 / 抢先体验
- 输入: 文字提示 → 输出: 三维场景 / 世界, 智能体行为与动作
- 核心想法: 从提示词到可玩游戏，发布与排行榜一并内置；这正是研究者快速制作任务变体所需的创作循环，但产出的是轻量浏览器游戏，而不是沉浸式场景。
- 内容: Google 推出的实验性浏览器平台，2026-10-07 起向 18 岁以上用户开放：用文字描述一款游戏即可立刻试玩，想改物理、规则、角色或环境也只需开口，完成后可以发布到社区画廊，带排行榜，部分类型还支持多人游戏。Google 与 Unity 同日宣布，Unity 的零代码游戏制作工具 Unity Spark（基于 Asset Store 美术资源与网页编辑器）将在 2026 年晚些时候接入 Playground；截至 2026 年 10 月，Spark 只开放了候补名单。
- 实现方式: 通过对话界面，由 Google 未具名的 AI 模型根据提示生成并修改游戏；Play Games 账号提供身份与排行榜，Unity Spark 计划补上 Unity 的运行时与美术师制作的资源。
- 参数: browser-based · 18+ · text-prompt creation · leaderboards, multiplayer in select genres · Unity Spark: waitlist, later in 2026
- 能力维度: 创作可及性, 共创与能动性
- 视频: https://www.youtube.com/watch?v=Dxvrvfyicp0
- 图片: https://storage.googleapis.com/gweb-uniblog-publish-prod/images/THUMBNAIL_BLOG.width-1300.png https://cdn.sanity.io/images/fuvbjjlp/production/2d99684e1ccd449afd498dbf61024c79f5ce48d5-1920x1080.png
- 项目主页: https://blog.google/innovation-and-ai/technology/ai/playground-experimental-gaming-platform/

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
- 内容: Unity 为自家引擎提供的 AI 工具：能读取当前场景并执行编辑器操作的智能体助手、AI 网关、MCP 服务器与命令行工具，以及面向 Claude Code、Codex 和 Grok 的官方插件。Unity AI 公开测试于 2026-05-04 向所有 Unity 6 及以上版本开发者开放；此后 Unity 不再使用“Unity AI”这一品牌名，并于 2026-10-07 与 Google 共同宣布无需写代码、用提示词做游戏的 Unity Spark，将在 2026 年晚些时候接入 Google 的 Playground（截至 2026 年 10 月仅开放候补名单）。2026-07-21 公布的 Unity 7 将为编程智能体提供免费的 MCP 服务器，计划 2026 年 12 月进入测试，2027 年第一季度正式发布。
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
- 内容: Epic 的实时引擎，许多高保真 VR 研究与虚拟制片舞台都用它，具备 Nanite 几何、Lumen 光照与 MetaHuman 数字人。Unreal Engine 5.8（2026-06-17）加入了可生成数百人群的 MetaHuman Collections、用网络摄像头即可完成的全身无标记 MetaHuman 动捕、以 MIT 许可开源的 OpenRigLogic，以及一个实验性 MCP 插件，让任意大语言模型都能查看并操控编辑器。
- 实现方式: C++ 引擎，配有 Blueprint 可视化脚本；Nanite 虚拟化几何与 Lumen 全局光照实时渲染，MetaHuman 工具为扫描或生成的角色绑定骨骼并驱动动画。
- 参数: UE 5.0 released 2022-04-05 · UE 5.8 released 2026-06-17 · free, 5% royalty above $1M gross for games
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

#### Meta VR 眼镜（Meta VR Glasses） — Meta (2026-09-23)
- 类型: 设备 · 获取方式: 候补 / 抢先体验
- 输入: 语音与音频, 身体、面部与视线追踪, 透视画面与实时环境 → 输出: 360° / 立体视频, 三维场景 / 世界, 虚拟人（脸 / 身体）
- 核心想法: 把 VR 的重量降到能戴着看完一整部电影、撑过一次长时间体验的程度；对于更长的生成情境，这一点和分辨率同样重要。不过在 2027 年春季之前，它还只是发布，实验室还用不上。
- 内容: Meta 做成眼镜形态的 VR 设备，于 2026-09-23 的 Connect 大会发布：戴在脸上的部分约 100 克，计算、电池与存储放在通过光纤连接的口袋计算盒里；配备 5K Micro-OLED 显示屏（每度 37 像素）、彩色透视，以及眼动、手势与语音操控，Meta 的 AI 智能体直接集成在操作系统中。现有 Quest 应用可以在上面运行，它还新增了照片级真实的“全息影像”视频通话，将于 2027 年春季以 1,299.99 美元开售。
- 实现方式: 分体式设计：眼镜部分只放传感器、Micro-OLED 屏幕与定制的折叠光路（pancake）镜片，经连线接驳的计算盒搭载高通骁龙 Reality Elite，负责计算并内置电池，Meta 称可连续播放视频最长三小时。
- 参数: ~100 g glasses + tethered puck · 5K micro-OLED · 37 ppd · Snapdragon Reality Elite · up to 3 h media playback · $1,299.99 · on sale spring 2027
- 能力维度: 感知真实感, 情境可达性
- 视频: https://www.youtube.com/watch?v=xyD_bmMy5nQ
- 图片: https://about.fb.com/wp-content/uploads/2026/09/Introducing-Meta-VR-Glasses_-A-Cinema-Courtside-Seat-and-Workspace-in-Just-100-GramsIntroducing-Meta-VR-Glasses_-A-Cinema-Courtside-Seat-and-Workspace-in-Just-100-Grams_social.jpg?w=1200
- 项目主页: https://about.fb.com/news/2026/09/introducing-meta-vr-glasses-3d-movies-immersive-live-sports-100-grams/

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
- 内容: Apple 的混合现实头显，2025-10-15 升级为 M5 芯片，刷新率最高 120 Hz，配 Dual Knit 头带，售价 3,499 美元。在生成内容方面，它搭载 visionOS 26 的空间场景（用生成式深度让二维照片可被探索）、用于视频通话的 Persona、180° / 360° 与广角视频播放，以及 Apple Immersive 视频。在 2026-06-08 的 WWDC 上预览、于 2026 年秋季推出的 visionOS 27，可以把全景照片变成空间场景并用作环境（Environments）。
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
- 内容: Meta 首款内置显示屏的消费级眼镜：Ray-Ban 镜框中带一块单眼全彩镜片内显示，由 Meta Neural Band 肌电腕带操控，售价 799 美元。在生成内容方面，它可以在佩戴者视野中显示带图像的 Meta AI 回答、实时字幕与翻译，以及导航。2026-09-23 的 Connect 大会上，Meta 开放了线上订购，新增英国、加拿大、法国、意大利与德国市场，并推出抢先体验的“Hologram”：在 WhatsApp 通话中用语音驱动佩戴者照片级真实的面部形象。
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
- 内容: Snap 面向消费者的一体式光学透视 AR 眼镜，2025-06-10 宣布将于 2026 年推出，2026-06-16 在 AWE 上开放预订（2,195 美元），并在 2026-09-16 的 SPECS 发布会上正式亮相（带蜂窝网络充电盒套装 2,395 美元），2026 年秋季晚些时候在美国、英国和法国发货。它运行 SPECS OS 与 Lens Studio 开发的应用（包括生成式 AI 滤镜），并搭载横跨 iPhone、Mac 与眼镜的预判式 AI 服务 SPECS Intelligence。
- 实现方式: 计算单元集成在眼镜上，无需外接计算盒，采用光学透视波导显示，支持手势与语音输入；以 Lens Studio 为创作工具，并调用云端 AI 服务。
- 参数: 51° FOV · pre-order $2,195 (from 2026-06-16) · ships fall 2026 (US, UK, France) · standalone, no puck
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

#### AA-3D — Artificial Analysis (2026-10-12)
- 类型: 数据集 / 基准 · 获取方式: 产品 / 应用
- 输入: 文字提示 → 输出: 三维场景 / 世界
- 核心想法: 衡量的是通往生成世界的“写代码”路线：由智能体搭建、显式且可编辑的场景，而不是视频模型输出的像素；排名靠前的模型都很早就开始查看自己场景的渲染图。
- 内容: Artificial Analysis 推出的基准，评测 AI 模型搭建交互式三维场景的能力：每个模型作为智能体在离线沙盒里工作（配有 Blender、Rapier 物理引擎、Python、无头浏览器与 CC0 资源库），最长三小时、250 轮，把一份文字需求变成一个 three.js 网页。招募的评审在同一需求生成的两个场景之间盲选；上线时（v1.0），Claude Sonnet 5.5 以 1,194 Elo 居首，与另外三个 Anthropic 和 OpenAI 模型在统计上并列。
- 实现方式: 55 个需求覆盖地标、机械、自然现象、人体、游戏、太空与故事等领域；智能体编写代码、渲染并查看截图后再修改；人工盲选两两投票拟合为带 95% 置信区间的 Elo 分数，并报告每个场景的成本（0.20–32.08 美元）。
- 参数: 55 briefs · 1,000+ scenes · 20+ models · ≤3 h / 250 turns per scene · output: three.js page · Elo from blind votes
- 能力维度: 创作可及性, 感知真实感
- 视频: https://x.com/ArtificialAnlys/status/2109791341802885209
- 图片: https://artificialanalysiscdn.com/article-assets/2026/aa-3d.jpg
- 项目主页: https://artificialanalysis.ai/articles/aa-3d

#### DyaFDB — Sungnyun Kim (2026-10-06)
- 类型: 数据集 / 基准 · 获取方式: 仅限研究
- 输入: 语音与音频 → 输出: 语音 / 声音, 对话 / 文本
- 核心想法: 轮流发言、重叠与打断是两个说话者共同造成的，所以虚拟人必须在会作出反应的对象面前测试；每个模型都会改变对方的表现。
- 内容: DyaFDB 不再让全双工语音模型面对录音或照本宣科的考官，而是让两个模型按分配的角色直接对话，目标或一致或冲突（订会议室、守住秘密），再由外部评审在事后为双方打分。
- 实现方式: 用 80 毫秒步进同步的桥接把两个全双工模型连起来，各自拿到一份私密的角色说明，处在同一情境中；共四类任务（如信息汇集、秘密的攻防），140 个场景、7,560 段录制对话，覆盖 PersonaPlex、MiniCPM-o 与 Raon-SpeechChat 的六种自对与互对组合，由外部评审打分。场景、角色提示与录制规程已宣布将公开。
- 参数: 4 tasks · 140 scenarios · 7,560 conversations · 80 ms lockstep
- 能力维度: 时间响应性, 行为似真性
- 论文: https://arxiv.org/abs/2610.08125 (arXiv 2026)
- 视频: https://dyafdb.github.io/media/dyafdb-promo.mp4
- 图片: https://dyafdb.github.io/og.png
- 项目主页: https://dyafdb.github.io/
- 代码: https://github.com/sungnyun/dyafdb

#### TurnBench — Sesame (2026-08-25)
- 类型: 数据集 / 基准 · 获取方式: 开源权重 / 代码
- 输入: 语音与音频 → 输出: 语音 / 声音
- 核心想法: 人在对方说完前约 151 毫秒（中位数）就开始接话；榜上没有一个系统能做到这一点而不频繁抢话，这限定了生成的对话伙伴能有多自然。
- 内容: 由 Sesame 牵头、联合多位学界作者推出的轮流发言基准：30 小时录音棚录制的双人对话，覆盖六种对话类型，每段由三人独立标注“说完一轮”与“打断”事件，并设公开排行榜，按召回率、误报率与延迟打分。排行榜把专门的话轮检测器与 Tavus Sparrow-2、Gemini 3.1 Live、OpenAI Realtime 和 Moshi 放在一起比较。
- 实现方式: 双声道双人对话录音（154 段对话、106 名演员，Fleiss κ = 0.78），测试集标签不公开；系统输出事件时间点，在误报率不超过 0.15 的约束下评分；另附按同一规范标注的 104 小时训练集；论文发表于 IEEE SLT 2026。
- 参数: 30 h test corpus · 6 conversation types · 104 h training set · metrics: recall, FPR, p50 latency · 14 systems in paper
- 能力维度: 时间响应性, 实验控制
- 论文: https://arxiv.org/abs/2608.25218 (IEEE SLT 2026)
- 图片: https://www.sesame.com/assets/images/blog/turnbench-og.png https://arxiv.org/html/2608.25218v2/figs/scoring-schematic.png
- 项目主页: https://www.sesame.com/blog/turnbench
- 代码: https://github.com/SesameAILabs/turnbench

#### 语音智能体竞技场（Speech Agent Arena） — Artificial Analysis (2026-08-24)
- 类型: 数据集 / 基准 · 获取方式: 产品 / 应用
- 输入: 语音与音频 → 输出: 语音 / 声音, 对话 / 文本
- 核心想法: 人们更愿意交谈的模型，不一定是能把事办成的那个：一个听起来很到位的智能体，可能在工具调用失败后仍声称已经完成。
- 内容: Artificial Analysis 为语音智能体设立的竞技场：经过筛选的付费参与者在同一情境下分别与两个匿名的语音到语音模型或级联系统实时对话（15 个需要调用工具的任务，如点外卖；20 个不需要的任务），再选出更喜欢的一方。上线时，Gemini 3.1 Flash Live 在偏好上领先，Grok Voice 与 GPT-Realtime 系列在任务完成率上领先；它与该公司 2026-06-23 推出的 Speech to Speech Index 互为补充，后者综合了 Big Bench Audio、Full-Duplex-Bench 的一部分与 τ-Voice。
- 实现方式: 参与者分别完成两段实时对话后进行盲选两两投票，拟合为 Elo 分数；另以最终工具调用是否正确来计算任务完成率。为减少过拟合，大多数情境提示与工具定义不公开。
- 参数: 35 scenarios (15 agentic, 20 non-agentic) · preference Elo + task success rate · native and cascaded systems
- 能力维度: 时间响应性, 行为似真性
- 图片: https://cdn.sanity.io/images/6vfeftx9/articles/d0023e187a3cc35d55aa8f6c6763688741f63c18-1254x1254.png?w=1200
- 项目主页: https://artificialanalysis.ai/articles/announcing-the-speech-agent-arena

#### PlayWorld：以智能体玩家评测世界模型的长时目标基准（PlayWorld） — Kaixin Ding, 快手 / 可灵 (2026-08-13)
- 类型: 数据集 / 基准 · 获取方式: 开源权重 / 代码
- 输入: 键盘与手柄动作, 文字提示 → 输出: 交互式帧流
- 核心想法: 以智能体能在世界模型里完成什么来评判它；对于控制方式各异的模型，这比回放固定动作序列更公平。
- 内容: 快手与香港大学推出的基准：让多模态 AI 智能体在 171 个情境中操控世界模型、追求长时程目标，例如原地转一圈检查场景是否一致，或走进水里看是否出现涟漪。在包括 Genie 3、HappyOyster 与 HY-World 2 在内的九个模型上测试后发现，它们在长时程交互上仍不可靠。
- 实现方式: 智能体玩家自行选择动作以达成每个情境的目标；模型从几何一致性、交互保真度以及视野内与视野外的演化等维度评分，并辅以视频质量与可控性等基础指标。
- 参数: 171 scenarios · 4 core dimensions · 9 models
- 能力维度: 持久性, 反应性
- 论文: https://arxiv.org/abs/2608.13552 (arXiv 2026)
- 视频: https://kxding.github.io/project/PlayWorld/hero-mosaic.mp4
- 图片: https://kxding.github.io/project/PlayWorld/og.jpg
- 项目主页: https://kxding.github.io/project/PlayWorld/
- 代码: https://github.com/kxding/PlayWorld

#### GENEA 手势生成挑战赛 2026（GENEA Challenge 2026） — Rajmund Nagy (2026-08-11)
- 类型: 数据集 / 基准 · 获取方式: 仅限研究
- 输入: 语音与音频 → 输出: 动作 / 动画
- 核心想法: 生成的身体还不会“听”：手势模型动作可以很自然，却对谈话对象视而不见，而社交情境检验的恰恰是这一点。
- 内容: 第四届 GENEA Challenge：对语音驱动手势生成的大规模人工评测。五支队伍的系统都在 Meta 的双人对话数据集 Seamless Interaction 上训练，共开展四项用户研究（869 名评审、23,000 多票）。在每项研究中，真实动作捕捉都是上限；在语音对齐上，最好的系统得分 32%，真实动作为 62%；在双人研究中，没有一个系统在回应对方方面明显高于随机水平。
- 实现方式: 通过解耦的众包研究分别评估动作真实感与语音对齐；在双人错配研究中替换对话者以检验“倾听”；并在 Grounded Gestures 子集上新增文本错配研究，检验语义手势。
- 参数: 5 systems · 4 user studies · 23,000+ votes · 869 raters · Seamless Interaction dataset
- 能力维度: 行为似真性, 反应性
- 论文: https://arxiv.org/abs/2608.10839 (arXiv 2026)
- 图片: https://arxiv.org/html/2608.10839v1/seamless-humanlikeness__pairwise_win_fraction.png
- 项目主页: https://genea-workshop.github.io/2026/challenge/

#### CaliBench — Odyssey (2026-08-10)
- 类型: 数据集 / 基准 · 获取方式: 开源权重 / 代码
- 输入: 图像 → 输出: 平面视频
- 核心想法: 一个每次都以同样方式展开的生成情境，并不是对偶然性的模拟；对依赖结果多样性的研究来说，校准与真实感同样重要。
- 内容: Odyssey 推出的基准，问的是视频世界模型能否复现物理结果的正确分布，而不只是生成一段看似合理的视频：从同一起始帧出发，模型对高尔顿板、岔路、骰子、扑克牌或轮盘生成多次推演，再把结果与已知分布比较。在六个图生视频模型（包括 Veo 3.1、Seedance 2.0 与 Runway Gen-4.5）上，Odyssey 报告普遍存在模式坍缩，Veo 3.1 在每个随机种子下都掷出同一个点数。
- 实现方式: 由视觉语言模型（Gemini 3.1 Pro，与人工标注一致率约 93%）从每段生成视频中读出结果，报告“可判读率”（结果清晰可读的比例）与“校准度”（与解析分布之间的归一化总变差距离）；论文发表于 TMLR。
- 参数: 9 scenes · 32 generations per model and scene · 6 image-to-video models · metric: mnTV
- 能力维度: 行为似真性, 情境多样性
- 论文: https://arxiv.org/abs/2608.16829 (TMLR 2026)
- 视频: https://framerusercontent.com/assets/3Qzar3JAlowjShHI2HIZ40khA4.mp4
- 图片: https://framerusercontent.com/assets/uvhuHUqb9mf5tVnGa97Xmjqne58.jpg
- 项目主页: https://odyssey.ml/introducing-calibench
- 代码: https://github.com/odysseyml/CaliBench

#### WorldRoamBench — Ting-Bing Xu (2026-06-30)
- 类型: 数据集 / 基准 · 获取方式: 仅限研究
- 输入: 键盘与手柄动作, 图像 → 输出: 交互式帧流
- 核心想法: 一个模型可以在平均意义上很好地沿路径行进，却仍会漏掉单次按键；而遵守碰撞约束又可能让它偏离预定路线。平均分掩盖了参与者真正会感受到的东西。
- 内容: 由高德地图（阿里巴巴）与南京大学、清华大学、北京大学共同推出的基准，用 1,000 多个第一人称与第三人称测试用例（室内、自然、城市场景）检验交互式世界模型在 10–60 秒推演中的表现。它对逐帧动作跟随、画面漂移、交互物理（碰撞、穿模、重力、反射、阴影）与记忆分别打分，并维护一个包含 Genie 3 在内、覆盖 10 多个开源与闭源模型的排行榜；截至 2026 年 10 月，数据集下载仍标注为“即将推出”。
- 实现方式: 在统一的测试集上运行各模型，由动作、视觉、物理与记忆四个模块打分；记忆通过重建场景点云来衡量，从而把“遗忘”与动作跟随偏差区分开。
- 参数: 1,000+ cases · 10–60 s rollouts · 4 dimensions · 10+ models (open and closed)
- 能力维度: 持久性, 反应性
- 论文: https://arxiv.org/abs/2606.31672 (arXiv 2026)
- 视频: https://worldroam.amap.com/scoring_gallery/memory/case2-Urban-0016/Urban-0016-Good-Genie3.mp4
- 图片: https://worldroam.amap.com/figs/evaluation_framework.png
- 项目主页: https://worldroam.amap.com/

#### WRBench：当前世界模型缺少持久的状态核心（WRBench） — Jinpeng Lu (2026-06-18)
- 类型: 数据集 / 基准 · 获取方式: 开源权重 / 代码
- 输入: 镜头路径 / 位姿, 文字提示, 键盘与手柄动作 → 输出: 交互式帧流, 平面视频
- 核心想法: 把“看起来一致”与“真正是一个世界”区分开：即使无人注视，事件也应继续发展，而当今的模型做不到。
- 内容: 一个诊断性基准，检验相机移开时生成的世界是否仍在继续演化。在来自 23 个模型、四种控制范式的 9600 段视频中，它发现当前系统表现得像跟拍镜头：重新看到的物体停留在被离开时的状态，而不是让原本进行中的事件继续推进。
- 实现方式: 把相机运动视为对“可观测性”的干预，并按经人工校准的链条逐级评分：相机是否执行了要求的动作，场景在视野内是否连续且可辨认，以及重新出现的目标是否与此前启动的事件相符。
- 参数: 9,600 videos · 23 models · 4 control paradigms
- 能力维度: 持久性, 行为似真性
- 论文: https://arxiv.org/abs/2606.20545 (arXiv 2026)
- 视频: https://jinplu.github.io/WRBench/videos/cat_expected_inspatio_yaw_rl60.mp4
- 项目主页: https://jinplu.github.io/WRBench/
- 代码: https://github.com/JinPLu/WRBench

#### MBench — Shengjun Zhang, 腾讯 (2026-05-30)
- 类型: 数据集 / 基准 · 获取方式: 开源权重 / 代码
- 输入: 文字提示, 键盘与手柄动作 → 输出: 平面视频, 交互式帧流
- 核心想法: 把生成世界是否保住了物体、场地与因果规则分开衡量；这正是参与者回到原处时会检查的三件事。
- 内容: 清华大学与腾讯微信视觉团队推出的基准，检验视频世界模型“记不记得住”：它把记忆拆成实体、环境与因果三类一致性，下设十二个子维度，从物体几何、人物身份到对极几何一致性、光照与状态演化，测试素材是精选的真实拍摄长视频。论文评测了八个文本条件续写模型与六个动作条件世界模型（包括 Matrix-Game 3.0、HY-WorldPlay 与 Yume-1.5），发现长期保持状态是它们共同的短板。
- 实现方式: 测试用例取自真实长视频，评分结合基于规则的指标（如对极几何与重投影一致性）和视觉语言模型问答，文本条件与动作条件模型分开评测。
- 参数: 3 dimensions · 12 sub-dimensions · 8 text-conditioned + 6 action-conditioned models · dataset on Hugging Face
- 能力维度: 持久性, 实验控制
- 论文: https://arxiv.org/abs/2606.00793 (arXiv 2026)
- 视频: https://huggingface.co/datasets/PeanutUp/PeanutUpproject-page-videos/resolve/main/assets/geometry_1.mp4
- 图片: https://peanutup.github.io/MBench-project/assets/dimension.jpg
- 项目主页: https://peanutup.github.io/MBench-project/
- 代码: https://github.com/study-overflow/MBench

#### WBench：交互视频世界模型多轮评测基准（WBench） — Kaining Ying, 美团 (2026-05-25)
- 类型: 数据集 / 基准 · 获取方式: 开源权重 / 代码
- 输入: 文字提示, 镜头路径 / 位姿, 键盘与手柄动作 → 输出: 交互式帧流, 平面视频
- 核心想法: 按体验实际展开的方式逐轮测试世界模型，并让文字、位姿与键盘驱动的模型在同一批用例上比较。
- 内容: 复旦大学与美团 LongCat 团队推出的交互世界模型多轮基准：289 个用例、1058 个交互轮次（导航、主体动作、事件编辑、视角切换），从视频质量、设定遵循、交互遵循、一致性与物理合理性五个维度打分。它设有公开排行榜，论文发现受测的 20 个模型没有一个在所有维度上都表现出色。
- 实现方式: 每个用例规定一个世界设定和一段第一或第三人称的多轮交互序列；导航指令在文字、六自由度位姿与离散动作之间统一；22 项自动子指标结合专用视觉模型与多模态大模型，并经过人工评判校验。
- 参数: 289 cases · 1,058 turns · 5 dimensions · 22 sub-metrics · 20 models · public leaderboard
- 能力维度: 实验控制, 持久性
- 论文: https://arxiv.org/abs/2605.25874 (arXiv 2026)
- 视频: https://meituan-longcat.github.io/WBench/video/multi.mp4
- 项目主页: https://meituan-longcat.github.io/WBench/
- 代码: https://github.com/meituan-longcat/WBench

#### iWorld-Bench：交互世界模型基准（iWorld-Bench） — Jianjie Fang, 清华大学 FIB 实验室 (2026-05-05)
- 类型: 数据集 / 基准 · 获取方式: 开源权重 / 代码
- 输入: 键盘与手柄动作, 镜头路径 / 位姿, 文字提示 → 输出: 交互式帧流, 平面视频
- 核心想法: 把同一个测试翻译成各个模型自己的控制方式，使相机、键盘与文字驱动的世界模型能在距离感知与记忆上比较。
- 内容: 清华大学在 ICML 2026 发表的世界模型交互能力基准：收集 33 万段视频，精选 2100 个覆盖不同视角、天气与场景的样本，构造六类任务共 4900 个测试样本，涵盖画面质量、轨迹跟随与记忆。它用一个“动作生成框架”让控制接口不同的模型能被同样测试，公开排行榜上有 14 个模型。
- 实现方式: “动作生成框架”把每个任务转换为模型可接受的输入形式；六类任务用亮度与色温一致性、轨迹对齐、记忆对称性等指标评分。
- 参数: 330K clips · 2.1K curated samples · 4.9K test samples · 6 task types · 14 models
- 能力维度: 实验控制, 持久性
- 论文: https://arxiv.org/abs/2605.03941 (ICML 2026)
- 视频: http://iWorld-Bench.com/static/videos/MemorySymmetry_Good_0.818159_0a0b1ce8a70f8c0c_batch001_mem4.mp4
- 图片: http://iWorld-Bench.com/static/images/overview.png
- 项目主页: http://iWorld-Bench.com
- 代码: https://github.com/EmbodiedCity/iWorld-Bench

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

#### Embody 3D 动作与行为数据集（Embody 3D） — Meta (2025-10-17)
- 类型: 数据集 / 基准 · 获取方式: 开源权重 / 代码
- 输入: 多视角拍摄 / 扫描 → 输出: 动作 / 动画, 语音 / 声音
- 核心想法: 以三维方式记录的多人、带情绪的日常互动，并为每人单独录音：这正是虚拟人学会倾听与回应、而不只是比划手势所需的训练素材。
- 内容: Meta Codec Avatars 实验室发布的动作与行为数据集：在多机位采集棚中记录了 439 名参与者共 500 人·小时的三维动作追踪数据（超过 5,400 万帧）。除了指定动作、手势与行走，它还记录了多人讨论、不同情绪状态下的对话、协作活动以及在类公寓空间中的共同生活，并提供手部追踪、体型、文字标注和每位参与者单独的音轨。
- 实现方式: 多机位同步采集并完成标定，估计每位参与者的体型，进行多人三维姿态追踪，并用麦克风波束成形分离每位说话者的声音。
- 参数: 500 person-hours · 439 participants · 54M+ frames · body + hands + shape · per-person audio · text annotations
- 能力维度: 行为似真性, 情境多样性
- 论文: https://arxiv.org/abs/2510.16258 (arXiv 2025)
- 图片: https://arxiv.org/html/2510.16258v1/imgs/teaser.jpg https://arxiv.org/html/2510.16258v1/imgs/dyadic_conversation.png
- 项目主页: https://www.meta.com/emerging-tech/codec-avatars/embody-3d

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

#### Full-Duplex-Bench — Guan-Ting Lin (2025-03-06)
- 类型: 数据集 / 基准 · 获取方式: 开源权重 / 代码
- 输入: 语音与音频 → 输出: 语音 / 声音
- 核心想法: 把“这像不像一场对话”变成实验室可以复现的数字：模型何时等待、何时附和、何时让出话轮。
- 内容: 台湾大学与加州大学伯克利分校推出的开源全双工口语对话模型评测套件，评估停顿处理、附和回应、顺畅的轮流发言与用户打断（v1，ASRU 2025）。后续版本加入重叠语音（v1.5）、通过 WebRTC 由自动 AI 考官主持的实时多轮会话（v2），以及在真实不流利语音下的工具调用（v3，2026 年）；Artificial Analysis 在其 Speech to Speech Index 中用它的一部分来评“对话动态”。
- 实现方式: 把预先录制的（从 v2 起也包括实时的）用户音频流式输入模型，基于时间对齐转写的自动指标（接管率、延迟、附和频率）为每种行为打分；v2 另加一个与模型对话并评分的大语言模型考官。
- 参数: v1 (2025-03) · v1.5 (2025-07) · v2 (2025-10, WebRTC examiner) · v3 (2026-04, tool use + disfluency)
- 能力维度: 时间响应性, 反应性
- 论文: https://arxiv.org/abs/2503.04721 (ASRU 2025)
- 图片: https://daniellin94144.github.io/FDB-v3-demo/FDBv3.drawio.png
- 项目主页: https://github.com/DanielLin94144/Full-Duplex-Bench
- 代码: https://github.com/DanielLin94144/Full-Duplex-Bench

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

#### Panda-70M 视频字幕数据集（Panda-70M） — Tsai-Shien Chen, Snap Inc. (2024-02-29)
- 类型: 数据集 / 基准 · 获取方式: 开源权重 / 代码
- 输入:  → 输出: 平面视频
- 核心想法: 开源视频模型对场景如何运动的认识，很大一部分来自这类语料：自动加字幕的网络片段，也带着网络内容的偏差。
- 内容: 包含 7,070 万段带字幕视频片段（约 16.7 万小时）的数据集，片段切自 380 万条 YouTube 长视频，由 Snap Research 联合加州大学默塞德分校等在 CVPR 2024 发布。它被广泛用作开源视频生成模型的预训练数据。
- 实现方式: 先把长视频切成语义连贯的片段，再由多个跨模态“教师”模型（输入画面、标题与字幕的图像和视频描述模型）为每段提出候选字幕，最后由微调过的检索模型挑出最合适的一条。
- 参数: 70.7M clips · ~167k hours · from 3.8M videos (HD-VILA-100M) · CVPR 2024
- 能力维度: 情境多样性
- 论文: https://arxiv.org/abs/2402.19479 (CVPR 2024)
- 视频: https://www.youtube.com/watch?v=m2NQ5k1oTcs
- 项目主页: https://snap-research.github.io/Panda-70M
- 代码: https://github.com/snap-research/Panda-70M

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
- **Botao 'Amber' Hu / 胡博涛** — 设计师与研究者，主持现实设计实验室（Reality Design Lab），在中国美术学院教授混合现实设计；开源 HoloKit 头显及本图库的创作者。 代表作: HoloKit (open-source MR headset); EchoVision; Generative Reality Inspire (2026). https://amber.botao.hu/
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
- **Reality Design Lab / 现实设计实验室** — 胡博涛（Botao “Amber” Hu）的设计研究实验室，研究混合现实与生成式沉浸体验，开发开源 HoloKit 工具包；本图库 Generative Reality Inspire 即由其制作。 https://reality.design/
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

- **NVIDIA** (43) — GPU 与人工智能计算公司. GPU 厂商，并推出 ACE：一套面向游戏角色的语音、语言与面部动画模型；其研究团队还开发了 Voyager 与 NitroGen 等游戏智能体。 https://research.nvidia.com
- **Meta** (41) — Meta AI 研究院 / FAIR / Reality Labs 现实实验室. Meta 的 AI 研究（FAIR）与 Reality Labs 团队；在三维资产方面发布了 Meta 3D Gen、SAM 3D Objects 与 Body、ShapeR 以及 Meta Motivo 人形模型。 https://ai.meta.com
- **Google DeepMind** (39) — 谷歌旗下的人工智能研究实验室. 谷歌的人工智能实验室（Gemini、Genie、Veo）。其 SIMA 项目训练能在商业三维游戏中听从语言指令的智能体，SIMA 2 还进入了 Genie 3 生成的世界；它也维护用于生成式社会模拟的 Concordia 库。 https://deepmind.google
- **Google** (28) — 谷歌研究院、Google Labs 与 Google AR. 谷歌在 DeepMind 之外的研究与产品团队；谷歌研究院发表了 DreamFusion，这篇 2022 年的论文开启了借助二维扩散模型的文生三维路线。 https://research.google
- **ByteDance Seed** (21) — 字节跳动的基础模型研究团队. 构建字节跳动基础模型（豆包、Seedance、UI-TARS）的研究团队；2025 年发布游戏智能体 Game-TARS 与 Lumine。 https://seed.bytedance.com
- **Tencent Hunyuan** (19) — 腾讯的基础模型团队. 腾讯混元团队发布覆盖文本、图像、视频、三维（混元3D 1.0 至 3.x、HY 3D Studio）和动作（HY-Motion）的开源与闭源模型。 https://hunyuan.tencent.com
- **Alibaba Tongyi (Qwen)** (17) — 阿里巴巴通义实验室与 Qwen 团队. 阿里巴巴通义实验室开发千问 Qwen 系列、万相 Wan 视频模型以及 Fun-Audio / CosyVoice 语音模型，其中许多以开源权重发布。 https://wan.video
- **Mel Slater** (16) — 虚拟现实研究者，巴塞罗那大学 EventLab 联合主任. 从计算机科学转向临场感研究，提出“地点错觉”与“似真错觉”，主持了虚拟米尔格拉姆、旁观者与身体拥有感等一系列实验。
- **Microsoft** (16) — 微软研究院. 微软研究院发布了 TRELLIS（2024）和 TRELLIS.2（2025），两者都是基于结构化三维潜变量、采用 MIT 许可的三维生成模型。 https://www.microsoft.com/research
- **Kuaishou** (14) — 短视频公司（可灵团队）. 快手开发可灵视频模型并开源了 LivePortrait，其可灵团队还发布了实时自回归数字人模型 MIDAS。 https://www.kuaishou.com
- **OpenAI** (11) — 人工智能研究与产品公司. GPT、Sora 与实时语音模型的开发者；2019 年的多智能体捉迷藏研究展示了智能体在三维物理世界中自发学会使用工具。 https://openai.com
- **Runway** (10) — AI 视频公司. Gen 与 Aleph 视频模型的开发者，也做世界模型研究（GWM-1）；同时提供应用与开发者 API。 https://runwayml.com
- **Tripo AI (VAST)** (10) — 三维生成公司（VAST）. VAST 开发 Tripo 三维生成模型与 Tripo Studio，并发布 TripoSR（与 Stability AI 合作）、TripoSG、UniRig、TripoSplat 等开源研究。 https://www.tripo3d.ai/
- **Snap Inc.** (9) — 相机公司；Snapchat、Lens Studio 与 Spectacles / SPECS AR 眼镜. Snapchat 镜头（每天使用数十亿次）的开发者，也推出独立 AR 眼镜：面向开发者的 Spectacles（2024）与消费级 SPECS（2026）。 https://research.snap.com
- **Stability AI** (9) — 开源生成模型公司. Stable Diffusion 的开发公司，也发布了开源三维模型：TripoSR（与 Tripo AI 合作）、Stable Fast 3D、SPAR3D 和 Stable Video 3D。 https://stability.ai
- **Tencent ARC Lab** (9) — 腾讯 PCG 应用研究中心. 腾讯从事视觉生成与编辑研究的实验室，成果包括 StereoCrafter 与 Rolling Forcing。 https://arc.tencent.com
- **Jeremy Bailenson** (7) — 斯坦福大学虚拟人交互实验室（VHIL）创始主任. 传播学学者，研究化身、虚拟身体与沉浸式媒体如何改变态度与行为，从“普罗透斯效应”到大规模 VR 实地研究。 https://vhil.stanford.edu/
- **Odyssey** (7) — 世界模型 AI 实验室. 由 Oliver Cameron 与 Jeff Hawke 于 2023 年创立的 AI 实验室，致力于通用世界模型，先后发布 Odyssey-1、-2、-3、多智能体 Agora 系列模型及 API。 https://odyssey.ml
- **World Labs** (7) — 空间智能公司. 由李飞飞等人创立，开发 Marble 世界模型与 Spark 泼溅渲染器。 https://www.worldlabs.ai
- **Apple** (6) — 消费科技公司. Apple Vision Pro 会为佩戴者生成 Persona：一个由面部扫描重建、由头显传感器驱动的三维化身。 https://machinelearning.apple.com
- **Decart** (6) — 构建实时生成视频与世界模型的 AI 实验室. 初创公司，推出实时生成的类 Minecraft 世界 Oasis 与实时视频到视频模型 MirageLSD，并通过 API 提供。 https://decart.ai
- **Deemos (Hyper3D Rodin)** (6) — Hyper3D Rodin 背后的三维生成公司. 源自上海科技大学的公司，开发 Rodin 系列三维生成模型（Gen-1 基于 CLAY 研究模型，之后有 Gen-1.5、Gen-2、Gen-2.5）和 ChatAvatar 人脸生成，通过 hyper3d.ai 和 API 提供服务。 https://hyper3d.ai
- **USC Institute for Creative Technologies** (6) — 南加州大学下属的大学附属研究中心. 1999 年在美国陆军资助下成立，把人工智能、图形与叙事结合用于训练和健康；虚拟人工具包、SimSensei 与 Bravemind 均出自这里。 https://ict.usc.edu/
- **Alaya Lab** (5) — AI 游戏与世界模型实验室. 一家研究 AI 游戏创作、世界模型与游戏智能体的实验室，发布了 Yume 交互世界模型（2025）、Sekai 探索数据集以及开源的 AlayaWorld 框架（2026）。 https://alayalab.ai/
- **Jean-Louis van Gelder** (5) — 马克斯·普朗克犯罪、安全与法律研究所所长；莱顿大学教授. 犯罪学家与心理学家，用 VR 研究犯罪决策（虚拟入室盗窃项目）和“未来自我”干预。 https://csl.mpg.de/en
- **Luma AI** (5) — 生成式 AI 公司（三维拍摄、视频）. 以 NeRF 拍摄应用和 Genie 文生三维起家，之后把重心转向视频生成（Dream Machine、Ray 系列模型）。 https://lumalabs.ai
- **Roblox** (5) — 在线游戏平台. 用户在此搭建并游玩各类体验的平台；其基础 AI 团队开发了部分开源的 Cube 三维基础模型，以及在游戏内使用的三维与 4D 生成功能。 https://corp.roblox.com
- **Shengshu Technology (Vidu)** (5) — 源自清华大学的视频生成公司. 由清华大学研究者创立；2024 年 4 月发布 Vidu，此后推出 Q 系列与实时 S 系列模型。 https://www.vidu.com
- **Skywork (Kunlun Tech)** (5) — 昆仑万维旗下人工智能业务. 昆仑万维的人工智能业务，开源 SkyReels 视频模型与 Matrix 世界模型。 https://www.skywork.ai
- **Tavus** (5) — 实时对话视频 AI 公司. Tavus 开发面对面 AI 对话所需的模型：Phoenix（渲染）、Raven（感知）、Sparrow（轮流发言），以及 2026 年 10 月发布的统一全双工视频到视频模型 Griffin。其对话视频接口（CVI）API 和面向个人用户的 PALs 都基于这些模型。 https://www.tavus.io
- **Adobe** (4) — 创意软件公司（Adobe 研究院）. Photoshop 和 Substance 3D 的开发商；Adobe 研究院参与了 LRM，这是首个用于单张图像三维重建的大型重建模型。 https://research.adobe.com
- **ElevenLabs** (4) — AI 音频公司. ElevenLabs 开发语音合成、声音克隆、对话智能体、音效与音乐模型，在媒体制作中被广泛使用。 https://elevenlabs.io
- **Epic Games** (4) — 游戏开发商与引擎厂商（Fortnite、Unreal Engine）. Fortnite 与 Unreal Engine 的开发商；2025 年在 Fortnite 中上线可语音对话的 AI 达斯·维达，随后以 Persona 装置（后更名 Conversations）向创作者开放这项技术。 https://www.unrealengine.com
- **Hong-Xing (Koven) Yu** (4) — 斯坦福大学研究者. 斯坦福大学吴佳俊组的计算机视觉研究者，WonderJourney 与 WonderWorld 的第一作者。 https://kovenyu.com
- **Inworld AI** (4) — 实时 AI 公司，前身是游戏 AI 角色引擎. 2021 年成立，最初为游戏 AI 角色打造引擎，育碧 NEO NPC 与英伟达 Covert Protocol 演示都使用了它。到 2026 年，它主要推广实时语音模型（TTS、STT、语音到语音）以及面向消费级 AI 应用的运行时。 https://inworld.ai/
- **Kyutai** (4) — 非营利开放科学 AI 实验室. Kyutai 是位于巴黎的非营利研究实验室，由 Iliad、CMA CGM 与 Schmidt Sciences 资助，语音模型均公开发布。 https://kyutai.org
- **Meshy** (4) — AI 三维生成公司. Meshy 的开发公司，提供文生三维、图生三维、AI 贴图、自动绑定与动画的网页、应用和 API；模型从 Meshy-1（2023 年）迭代到 Meshy 7.1（2026 年 9 月）。 https://www.meshy.ai/
- **PixVerse** (4) — AI 视频公司（爱诗科技）. 总部位于北京的 PixVerse 视频生成器与应用的开发者，由爱诗科技打造；2026 年推出实时世界模型 R1 与 R2。 https://pixverse.ai
- **Robbyant** (4) — 蚂蚁集团具身智能公司. 蚂蚁集团旗下的具身智能公司，发布面向机器人与空间感知的开源 LingBot 系列模型。 https://technology.robbyant.com
- **Ryo Suzuki** (4) — 科罗拉多大学博尔德分校 ATLAS 研究所与计算机系助理教授，Programmable Reality Lab 负责人. 人机交互研究者，研究 AR/VR、实体界面与 AI 的交叉；实验室的“生成式 AR”方向希望把物理世界变成生成式 AI 的画布。 https://ryosuzuki.org
- **StepFun** (4) — 中国基础模型公司. 阶跃星辰开发 Step 系列语言、多模态与音频模型，并开源了其中多款。 https://www.stepfun.com
- **Wayve** (4) — 具身智能自动驾驶公司. 总部位于伦敦的公司，开发端到端驾驶模型，并自 2023 年起推出 GAIA 系列生成式驾驶世界模型。 https://wayve.ai
- **Alibaba Token Hub (ATH)** (3) — 阿里巴巴集团旗下推出 HappyHorse 与 HappyOyster 的事业群. 阿里巴巴集团旗下事业群，其 AI 创新事业部（前身为淘天集团未来生活实验室）研发通过阿里云百炼提供的 HappyHorse 音视频模型；2026 年还推出了世界模型产品 HappyOyster。 https://www.happyoyster.cn/
- **Artificial Analysis** (3) — 独立 AI 基准评测公司. 跨服务商评测模型的质量、价格与速度，并运营图像与视频盲投竞技场。 https://artificialanalysis.ai
- **Character.AI** (3) — 面向大众的 AI 角色平台. Character.AI 运营一个大型 AI 角色聊天平台，并开发视频模型（AvatarFX、TalkingMachines）为角色配上面孔。 https://character.ai
- **Doron Friedman** (3) — 赖克曼大学先进现实实验室负责人. 研究虚拟人、远程临场与面向心理健康的 VR；其实验室开发由大语言模型驱动的虚拟人和自动化情境生成流程。
- **Hume AI** (3) — 语音 AI、表达测量与评测公司. Hume AI 开发共情语音接口 EVI、Octave 语音合成模型以及开源的 TADA 模型；2026 年其主打表达测量 API（50 多种语言、600 多个表达维度），以及用于评测真实场景语音 AI 的工具与基准，包括 RW-Voice-EQ Bench。 https://www.hume.ai
- **Jiwen Yu** (3) — 香港大学研究者. 香港大学博士研究者，与快手可灵团队合作研究交互式视频生成。 https://yujiwen.github.io
- **Joon Sung Park** (3) — 人机交互研究者，Simile 联合创始人兼 CEO. 斯坦福大学计算机科学博士，2023 年以 Smallville 论文提出生成式智能体，随后用 1,052 名美国人的两小时访谈构建个体智能体。与 Michael Bernstein、Percy Liang 共同创办 Simile。
- **Keiichi Ihara** (3) — Programmable Reality Lab（科罗拉多大学博尔德分校）与筑波大学博士生. 人机交互研究者，构建把电影、教学视频等二维媒介转化为空间内容的混合现实系统。
- **Lightricks** (3) — 创意应用公司，LTX 模型开发者. Facetune 与 LTX Studio 的开发者，发布开源的 LTX-Video、LTX-2 与 LTX-2.5 模型。 https://ltx.io
- **Meituan** (3) — 科技公司（MeiGen / LongCat 团队）. 美团的 MeiGen 团队发布了 MultiTalk 和 InfiniteTalk，这是用于音频驱动说话视频与配音的开源模型。 https://www.meituan.com
- **MiniMax** (3) — 大模型公司（海螺 AI）. 海螺视频模型、MiniMax 语言模型与语音模型的开发者；2026 年 7 月以开源权重发布 H3 视频模型。 https://www.minimax.io
- **Shanghai AI Laboratory** (3) — 位于上海的公共人工智能研究机构. 大型公共科研机构（又称浦江实验室），研究基础模型、具身智能与三维视觉，π³ 重建模型出自这里。 https://www.shlab.org.cn/
- **Stijn Spanhove** (3) — In The Pocket 公司 XR 开发者；Snap Spectacles 创作者. 持续发布把 AR 眼镜、Vision Pro 与生成模型结合起来的短小概念验证。
- **Tencent** (3) — 中国科技与游戏公司. 总部位于深圳的互联网与游戏公司；除混元外，其多个研究团队也发表交互式视频方面的工作。 https://www.tencent.com
- **ZJU3DV** (3) — 浙江大学三维视觉组. 浙江大学 CAD&CG 国家重点实验室周晓巍、彭思达团队，长期研究动态人体与场景捕捉。 https://zju3dv.github.io/
- **Agora** (2) — 实时互动平台. 运营面向音视频 SDK 的全球实时网络，推出对话式 AI 引擎，并支持开源 TEN Framework。 https://www.agora.io
- **Albert "Skip" Rizzo** (2) — 南加州大学创意技术研究所医学虚拟现实部门主任. 临床心理学家，开发了用于 PTSD 暴露疗法的 Virtual Iraq/Afghanistan 与 Bravemind，并主持虚拟病人研究。
- **Amap (Alibaba)** (2) — 阿里巴巴集团旗下的地图与导航服务，其视觉实验室（CV Lab）研发生成式三维地球与世界模型. 高德是阿里巴巴集团的数字地图与导航服务；其视觉实验室于 2026 年发布了生成式三维地球模型 ABot-Earth。 https://abot-earth.amap.com/
- **Bernhard Kerbl** (2) — Inria / 维也纳工业大学研究者. 3D 高斯泼溅（SIGGRAPH 2023）共同第一作者，也是其超大场景层级版本的第一作者。
- **Botao 'Amber' Hu** (2) — 牛津大学研究者；Reality Design Lab 创始人；HoloKit 发明者. 设计师与研究者（清华大学本科、斯坦福大学人工智能硕士），主持 Reality Design Lab 在具身与社交混合现实、思辨设计和生成式未来构想方面的研究；实验室作品曾在 SIGGRAPH、CHI、TEI 与 Ars Electronica 展出。 https://reality.design
- **Chuan Guo** (2) — 人体动作生成研究者. 研究者（阿尔伯塔大学，后进入业界），创建了 HumanML3D 数据集（CVPR 2022）和 MoMask（CVPR 2024）。 https://ericguo5513.github.io/
- **Chuanrui Zhang** (2) — 南洋理工大学博士研究者，字节跳动 Seed 实习生. SIMART（SIGGRAPH 2026）第一作者，该工作在字节跳动 Seed 实习期间与南洋理工大学合作完成。 https://simart-mllm.github.io/
- **Convai** (2) — 面向游戏与 XR 角色的对话式 AI 平台. 为 Unreal Engine、Unity 与网页三维场景提供能说话、感知和行动的角色引擎与插件；2023 年与英伟达用 ACE 合作制作了 Kairos 演示。 https://convai.com/
- **Daniel Freeman** (2) — 牛津大学临床心理学教授. 主持牛津大学针对恐高、偏执以及精神病患者广场回避（gameChange）的自动化 VR 治疗研究。 https://gamechangevr.com/
- **Domna Banakou** (2) — 虚拟具身研究者（巴塞罗那大学 EventLab）. 研究虚拟身体与场景的渐进变化如何改变知觉、态度与焦虑。
- **Duo Wang** (2) — 伊利诺伊大学厄巴纳-香槟分校传媒学院研究者. EmSim 的第一作者：这是一个由大语言模型评分、在警校学员中试用的 VR 冲突降级模拟器。
- **Evonne Ng** (2) — 双人互动行为与手势生成研究者. Evonne Ng（加州大学伯克利分校，后加入 Meta）主导了 Learning to Listen（CVPR 2022）和 Audio2Photoreal（2024），建模对话中倾听者的脸和身体如何回应。 https://evonneng.github.io
- **Haozhe Xie** (2) — 南洋理工大学 S-Lab 研究者. 南洋理工大学刘子纬 S-Lab 的研究者，CityDreamer 与 CityDreamer4D 的第一作者。 https://www.infinitescript.com
- **HeyGen** (2) — AI 视频虚拟人平台. HeyGen 提供 AI 虚拟人视频制作，并通过 LiveAvatar 提供实时虚拟人流式 API。 https://www.heygen.com
- **Huadai Liu** (2) — 音频生成研究者（浙江大学）. Huadai Liu 在浙江大学研究文本、视频与空间音频的生成。
- **InSpatio** (2) — 构建三维与 4D 世界模型的中国空间智能初创公司. 其 INSPATIO-WORLD 论文与浙江大学三维视觉研究者（章国锋、鲍虎军）合著；公司发布了 InSpatio-World、InSpatio-WorldFM、QuerySplat 等开源模型。 https://www.inspatio.com/
- **Inria GraphDeco** (2) — Inria 图形学研究组. 由 George Drettakis 领导的 Inria 蔚蓝海岸大学研究组，3D 高斯泼溅及其层级扩展的出处。 https://team.inria.fr/graphdeco/
- **JD.com** (2) — 中国电商与科技公司. 中国零售与科技集团，其 JoyAI 团队通过 jd-opensource 发布开源模型。 https://www.jd.com
- **Jia-Peng Zhang** (2) — 清华大学研究者. 清华大学研究者，与 VAST 合作的 UniRig（SIGGRAPH 2025）第一作者。 https://zjp-shadow.github.io/
- **Jianyuan Wang** (2) — 牛津 VGG / Meta AI 研究者. VGGT（CVPR 2025 最佳论文）与 VGGT-Ω（CVPR 2026 Oral）第一作者，牛津视觉几何组与 Meta 的合作工作。
- **Jiawei Ren** (2) — 南洋理工大学 S-Lab / NVIDIA 研究者. DreamGaussian4D 与 L4GM（NeurIPS 2024，与 NVIDIA 合作）的第一作者。
- **Jim Blascovich** (2) — 社会心理学家，加州大学圣塔芭芭拉分校. 共同创办加州大学圣塔芭芭拉分校的虚拟环境与行为研究中心，倡导把沉浸式 VR 作为社会心理学的研究方法。
- **Jiraphon Yenphraphai** (2) — 普渡大学博士研究者. 普渡大学博士研究者（导师 Raymond A. Yeh），与 Snap Research 合作完成的 ShapeGen4D（ICLR 2026）第一作者。 https://domejiraphon.github.io/
- **Jonathan T. Barron** (2) — Google DeepMind 研究科学家. Google 研究者，mip-NeRF、mip-NeRF 360、Zip-NeRF 等工作以及多项辐射场质量基准的作者。
- **Jonathon Luiten** (2) — Meta 研究者. Dynamic 3D Gaussians（3DV 2024）第一作者，在 Meta 参与了 BulletGen。
- **Junchao Huang** (2) — 香港中文大学（深圳）研究者，SolarWM 第一作者. SolarWM（2026）的第一作者，该工作为长时视频世界模型提供完全开放的数据与训练技术栈；他也是 WorldCast 的合作者。 https://junchao-cs.github.io/SolarWM-Web/
- **Junxuan Li** (2) — Meta Codec Avatars 实验室研究科学家. Junxuan Li 是 URAvatar（SIGGRAPH Asia 2024）和大规模 Codec Avatars（CVPR 2026）的第一作者。 https://junxuan-li.github.io
- **KRAFTON** (2) — 电子游戏发行商. 韩国游戏公司，发行《绝地求生》与 inZOI；与英伟达 ACE 合作推出运行在本地小语言模型上的“可共玩角色”（CPC）。 https://www.krafton.com/
- **Lei Zhang** (2) — 人机交互研究者（密歇根大学博士，现任职于新泽西理工学院）. 研究沉浸式创作中的人机共创，从 VRCopilot（密歇根大学）到 Capybara（与普林斯顿 HCI 实验室合作）。
- **Mar Gonzalez-Franco** (2) — XR 研究科学家（Google；曾任职于微软研究院）. 从事化身、具身与社交 XR 研究的神经科学家与工程师，主导了米尔格拉姆范式的 VR 复现研究。
- **Matthew Tancik** (2) — 研究者，Nerfstudio 联合创建者. NeRF 合著者，在伯克利主导了 Nerfstudio，后加入 Luma AI。
- **Michael Wiesing** (2) — 巴塞罗那大学 EventLab 研究员. 研究 VR 体验如何延续到物理现实中的信念与行动。
- **Mingyu Ouyang** (2) — 人工智能研究者（新加坡国立大学）. 新加坡国立大学研究者；Player-1（2026）的第一作者，该工作完成于腾讯 ARC 实验室实习期间。
- **NAVER LABS Europe** (2) — NAVER 的欧洲研究院. 韩国 NAVER 公司位于格勒诺布尔的研究中心，DUSt3R / MASt3R 系列三维基础模型的出处。 https://europe.naverlabs.com/
- **Niantic Spatial** (2) — 从 Niantic 独立出来的地理空间 AI 公司. 在 Niantic 于 2025 年出售游戏业务后，专注大型地理空间模型、视觉定位与 AR 地图。 https://www.nianticspatial.com/
- **PlayCanvas** (2) — 网页图形引擎公司（Snap 旗下）. 开发开源 PlayCanvas 引擎与 SuperSplat 高斯泼溅编辑器。 https://playcanvas.com/
- **Qianqian Wang** (2) — 加州大学伯克利分校研究者. 伯克利研究者，Shape of Motion 与 CUT3R 第一作者。
- **Reality Design Lab** (2) — 由 Botao 'Amber' Hu 主持的混合现实独立设计研究实验室. 以“设计新现实”为宗旨，创作混合现实艺术作品，开发开源工具（HoloKit、HoloMask、Unity 版 MultipeerConnectivity），并开展教学项目；作品曾在 SIGGRAPH、CHI、IEEE VR 与 Ars Electronica 展出。 https://reality.design
- **Ruofei Du** (2) — Google XR 交互感知与图形负责人. 研究面向 XR 的交互图形与 AI，主导 XR Blocks，参与 Thing2Reality 与 Sensible Agent。 https://duruofei.com
- **Samsung Electronics** (2) — 电子公司；Galaxy XR 头显制造商. 与谷歌、高通共同开发 Android XR，并于 2025 年 10 月推出 Galaxy XR 头显。 https://www.samsung.com
- **Sesame** (2) — 语音 AI 与硬件公司. Sesame 由 Oculus 联合创始人 Brendan Iribe 参与创立，开发对话式语音智能体与对话语音模型 CSM，并已宣布眼镜产品。 https://www.sesame.com
- **SpAItial** (2) — 三维世界模型初创公司（Echo）. 由慕尼黑工业大学教授 Matthias Niessner 联合创立的初创公司，研发空间基础模型；2025 年获 1300 万美元种子轮融资，先后发布 Echo（2025 年 12 月）和 Echo-2（2026 年 4 月）。 https://www.spaitial.ai
- **Suno** (2) — AI 音乐公司. Suno 打造了被广泛使用的歌曲生成器，能根据提示写出并演唱完整歌曲。 https://suno.com
- **Tabitha Peck** (2) — 戴维森学院计算机科学家. 研究虚拟具身与化身效应，2013 年与 Mel Slater 团队合作的“黑人化身与内隐偏见”研究的第一作者。
- **Tsinghua University FIB Lab** (2) — 清华大学电子工程系研究实验室. 由李勇领导的实验室，研究城市科学与大语言模型智能体；2025 年发布 AgentSociety 模拟器。
- **Ubisoft** (2) — 电子游戏发行商. 《刺客信条》《全境封锁》的法国发行商；其巴黎团队在 2024 年展示 NEO NPC 原型，2025 年推出可游玩的 Teammates 实验。 https://www.ubisoft.com/
- **Unity** (2) — 游戏引擎公司. Unity 引擎的开发者，大量 XR 与移动游戏以及许多 VR 研究实验室都在用它。 https://unity.com
- **Wangbo Yu** (2) — 北京大学博士研究者. ViewCrafter（2024，TPAMI 2025）及其后续视频世界模型 WorldCrafter（2026）的第一作者。
- **Weihao Tan** (2) — 人工智能研究者，游戏智能体方向. Cradle（2024）与 Lumine（2025，字节跳动 Seed）的第一作者：前者通过截图和键鼠输出游玩《荒野大镖客 2》，后者能实时完成数小时的《原神》任务。
- **Zhaoxi Chen** (2) — 南洋理工大学 S-Lab 博士研究者. 前馈式图像到 4D 模型 4DNeX 的第一作者。 https://frozenburning.github.io
- **Zijie Wu** (2) — 华中科技大学博士研究者. AnimateAnyMesh（ICCV 2025，与阿里巴巴达摩院合作）和 R-DMesh（SIGGRAPH 2026，与腾讯混元合作）的第一作者。
- **Ziming Li** (2) — 罗切斯特理工学院研究员. Roshan Peiris 实验室中面向自闭症人士的大语言模型 VR 职场沟通训练研究（CHI EA 2024）的第一作者。
- **Ziqi Huang** (2) — 南洋理工大学 S-Lab 研究者. 在刘子纬课题组研究视频生成及其评测，VBench 与 VBench++ 的第一作者。 https://ziqihuangg.github.io
- **xAI (SpaceXSI)** (2) — Grok 背后的 AI 公司；其 2026 年的页面使用 SpaceXSI 名称. xAI 开发 Grok 系列模型，以及 Grok Voice 语音到语音与语音转写 API。 https://x.ai
- **1X Technologies** (1) — 人形机器人公司. 挪威与美国背景的人形机器人公司，产品包括 EVE 与 NEO。 https://www.1x.tech
- **4DV.ai** (1) — 4D 高斯视频创业公司. 基于高斯泼溅开发 4D 视频拍摄、播放与编辑工具的创业公司，CEO 孙佳明是 FreeTimeGS 的合著者。据 Radiancefields.com 报道，其 Infinite Studio 演示获得 SIGGRAPH 2025 Real-Time Live 最佳展示奖。 https://www.4dv.ai
- **Aashish Rai** (1) — 布朗大学交互式三维视觉与学习实验室博士研究者. PackUV（CVPR 2026）与 UVGS 的第一作者，这两项工作把高斯泼溅映射为 UV 图像，使其能像视频一样存储与传输。
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
- **Amir Mann** (1) — 以色列理工学院研究者. 以色列理工学院研究者（与 Or Litany 合作），VideoMDM 第一作者；该工作用视频中的二维姿态训练三维动作扩散模型。 https://videomdm.github.io/
- **Anam** (1) — 实时交互虚拟人公司. Anam 开发 CARA 系列实时虚拟人扩散模型，并提供面对面 AI 智能体的 API。 https://anam.ai
- **Andreessen Horowitz (a16z)** (1) — 风险投资机构（a16z 基础设施团队）. 风险投资机构，其基础设施团队于 2023 年与 Convex 合作发布 AI Town：一个 MIT 许可、可在浏览器中运行的 LLM 角色小镇起步套件。 https://a16z.com/
- **Andrew Liu** (1) — Google Research 研究者. Infinite Nature（ICCV 2021）的第一作者，与 Noah Snavely、Angjoo Kanazawa 等在 Google Research 合作。
- **Andy Serkis** (1) — 演员、导演，Imaginarium Productions 联合创始人. 以动作捕捉表演闻名的演员与导演（咕噜、凯撒），其伦敦工作室 Imaginarium 从事表演捕捉与沉浸式叙事。 http://www.imaginariumuk.com
- **Ant Group** (1) — 中国金融科技与人工智能公司（支付宝）. 蚂蚁集团是支付宝的运营方，通过 inclusionAI 组织发布开源 AI 模型，其中包括 2026 年的 Realtime-Venus 全双工交互模型；其具身智能业务为 Robbyant。 https://www.antgroup.com/
- **Anuttacon** (1) — AI 游戏工作室. 由米哈游联合创始人蔡浩宇创办的 AI 原生游戏工作室；2025 年发布《Whispers from the Star》。 https://www.anuttacon.com/
- **Anything World** (1) — AI 绑定与动画公司. 为任意三维模型（包括动物和交通工具）提供自动绑定与动画的公司，提供网页应用和游戏引擎插件。 https://anything.world/
- **Applied Intuition** (1) — 车辆软件与自动驾驶仿真公司. 为汽车、卡车和国防客户提供仿真、自动驾驶与车辆软件工具，并以 Applied Intuition Research 名义发表研究。 https://www.appliedintuition.com/
- **AppliedVR** (1) — 数字疗法公司. RelieVRx 的开发商，这是一款经美国 FDA De Novo 途径授权、用于慢性下背痛的居家 VR 项目。 https://www.appliedvr.io/
- **Arcturus** (1) — 体积视频软件公司. HoloSuite 的开发者，这套工具用于编辑、压缩与流式传输体积视频，后来转向基于高斯泼溅的体育回放。 https://arcturus.studio/
- **Arena (formerly LMArena)** (1) — 众包 AI 评测平台. 源自加州大学伯克利分校的 LMSYS Chatbot Arena，运营文本、视觉、图像与视频模型的公开盲投排行榜。 https://arena.ai
- **Ars Electronica Futurelab** (1) — Ars Electronica 的艺术与科技研究实验室. 处于艺术、技术与社会交叉点的跨学科实验室，以 Deep Space 8K 及与产业伙伴的合作闻名。 https://ars.electronica.art/futurelab/en/
- **Art from the Machine** (1) — 独立模组开发者. 以化名活动的开发者，开发了开源模组 Mantella，让《上古卷轴 V：天际》与《辐射 4》中的 NPC 能进行由语言模型驱动的语音对话。
- **Astronex** (1) — 机器人与世界模型团队. 开源实时世界模型基座 Astronex-World 1.0（2026）的发布团队，通过 GitHub 组织 Astronex-Robotics 发布；其他公开信息很少。 https://world.astronex.com.cn/
- **Atlantic Studios** (1) — 由 Anthony Geffen 创立的纪实与沉浸式内容制作公司. 伦敦制作公司（原名 Atlantic Productions），以与 David Attenborough 合作的自然历史影片和 VR、XR 纪录片知名。 https://www.atlanticstudios.co.uk
- **Autodesk Research** (1) — Autodesk 的研究部门. 专注设计、制造与人机交互的产业研究团队，长期在 UIST 和 CHI 发表创作工具方面的研究。 https://www.research.autodesk.com/
- **Avaturn Live** (1) — 实时交互虚拟人公司. Avaturn Live 开发实时交互虚拟人，发布了包含模型权重、渲染器和服务后端的开源方案 AVTR-1。 https://avaturn.live
- **Aviad Dahan** (1) — 特拉维夫大学研究者. Aviad Dahan 是 SepGen（2026）的第一作者。该工作来自特拉维夫大学，合作者包括 Lior Wolf、Raja Giryes 和谷歌的研究者，是一个多音轨音视频生成与分离模型。 https://sepgen.github.io/
- **Axon** (1) — 公共安全科技公司（TASER 电击器、执法记录仪）. TASER 电击武器与警用执法记录仪的制造商，也为警员提供 VR 训练。 https://www.axon.com/products/vr
- **Bangbang Yang** (1) — 字节跳动 PICO 混合现实团队研究者. 研究面向 XR 的神经渲染与场景编辑。 https://ybbbbt.com/
- **Barbara Olasov Rothbaum** (1) — 埃默里大学精神病学教授. 临床心理学家，她 1995 年的试验是最早的虚拟现实暴露疗法对照研究之一。
- **Beijing Academy of Artificial Intelligence (BAAI)** (1) — 非营利人工智能研究机构. 位于北京的非营利研究机构；其智能体团队发布了 Cradle，一个在商业游戏与软件中测试的通用计算机控制框架。 https://www.baai.ac.cn/
- **Ben Mildenhall** (1) — 研究者，World Labs 联合创始人. NeRF（2020）第一作者，后在 Google Research 工作，现为 World Labs 联合创始人。
- **Ben Poole** (1) — 谷歌研究科学家. 谷歌研究员，DreamFusion 第一作者，该论文提出了用于文生三维的分数蒸馏采样（SDS）。
- **Biao Jiang** (1) — 复旦大学研究者. 复旦大学研究者，与腾讯合作的 MotionGPT（NeurIPS 2023）第一作者。
- **Binbin Huang** (1) — 上海科技大学研究者. 2D 高斯泼溅（SIGGRAPH 2024）第一作者。
- **Bing Li** (1) — 山东大学研究者. CyberSelf 的第一作者：在这个 VR 系统中，人们与一个外貌和声音都像自己的大语言模型化身对话。
- **Binyang Han** (1) — 新西兰坎特伯雷大学研究者. IEEE VR 2026 一项研究的第一作者：在 XR 中，一个大语言模型驱动的具身智能体在目标冲突的两人之间进行调解。
- **Blockade Labs** (1) — Skybox AI 的开发者. 开发 Skybox AI 的初创公司：一个生成 360° 等距柱状天空盒与环境的网页工具和 API。 https://www.blockadelabs.com
- **Bodyswaps** (1) — 软技能培训公司. 为学生和员工打造在 VR 与浏览器中进行的 AI 化身角色扮演，并提供自动反馈。 https://bodyswaps.co/
- **Bohong Chen** (1) — 浙江大学 CAD&CG 国家重点实验室研究者. 浙江大学 CAD&CG 国家重点实验室周昆课题组研究者，EchoAvatar（SIGGRAPH 2026）第一作者。 https://github.com/RobinWitch
- **Bowen Xue** (1) — 斯坦福大学研究者. Bowen Xue 是 Ring Forcing（ECCV 2026）的第一作者，该工作在斯坦福大学完成，合作者包括张吕敏（Lvmin Zhang）、Maneesh Agrawala 以及字节跳动的研究者。 https://ringforcing.com
- **Bowen Zhang** (1) — 中国科学技术大学博士研究者. 与微软亚洲研究院合作的视频到 4D 扩散模型 Gaussian Variation Field Diffusion（ICCV 2025）的第一作者。
- **Boyuan Chen** (1) — 麻省理工学院研究者，Diffusion Forcing 第一作者. 麻省理工学院的博士研究者，研究视频世界模型与机器人学习。 https://boyuan.space
- **Brian Nlong Zhao** (1) — 伊利诺伊大学厄巴纳-香槟分校博士研究者. 伊利诺伊大学厄巴纳-香槟分校 James M. Rehg 课题组研究者，与斯坦福大学 Jiajun Wu、剑桥大学 Shangzhe Wu 合作完成的 Kirin（ECCV 2026）共同第一作者。 https://briannlongzhao.github.io/
- **CAMEL-AI** (1) — 开源多智能体研究社区. CAMEL 多智能体框架与 OASIS 背后的开源社区；OASIS 是可容纳一百万个 LLM 智能体的社交媒体模拟器。 https://www.camel-ai.org/
- **Chaoyang Wang** (1) — Snap Research 研究科学家. Snap 4D 视频扩散模型系列 4Real-Video 与 4Real-Video-V2 的第一作者。
- **Chaoyue Song** (1) — 南洋理工大学博士研究者. 南洋理工大学研究者，与字节跳动 Seed 合作的 Puppeteer（NeurIPS 2025 亮点论文）和 MagicArticulate 第一作者。 https://chaoyuesong.github.io/
- **Chen Geng** (1) — 斯坦福大学博士研究者. 斯坦福大学 Jiajun Wu 课题组研究者，NeuROK（CVPR 2026）第一作者。 https://chen-geng.com
- **Chen Tessler** (1) — 英伟达研究科学家. 英伟达研究科学家，研究基于物理的角色控制；MaskedMimic（SIGGRAPH Asia 2024）第一作者，并维护 ProtoMotions。
- **Chen Yang** (1) — 长春理工大学研究者. 与 Chunyi Chen 合作研究协同虚拟环境，《One Word, One World》（Virtual Reality，2026）第一作者。
- **Cheng-Chih Tsai** (1) — 台湾科技大学研究者. 与 Tse-Yu Pan、Ping-Hsuan Han 合作研究生成式 VR 原型工具，DreamCraft（IEEE VR 2026）第一作者。
- **Cheng-Kuang Chang** (1) — 麻省理工学院 CSAIL 研究者. Cheng-Kuang Chang 是 D2（2026）的第一作者。该工作在麻省理工学院 CSAIL 与 MIT-IBM Watson AI Lab 合作完成，把回合制口语语言模型转换为全双工模型。 https://d2-duplex-demo.github.io/
- **Chengqian Ma** (1) — 北京大学研究者. Chengqian Ma 是 Motion-Omni（2026）的第一作者。这是一个开源的语音对话模型，可在生成语音的同时生成面部、手部和全身动作。 https://step-out.github.io/Motion-Omni-Page/
- **Chong Bao** (1) — 浙江大学 CAD&CG 国家重点实验室研究者. Chong Bao 是浙江大学 CAD&CG 国家重点实验室的研究者，Archon（CVPR 2026）的第一作者；该统一多模态数字人模型与 Google 和 Google DeepMind 合作完成。 https://zju3dv.github.io/archon/
- **Chuhan Zhang** (1) — Google DeepMind 研究科学家. D4RT 的第一作者，该论文获 CVPR 2026 最佳论文奖，研究前馈式 4D 重建与追踪。
- **Chuqiao Li** (1) — 图宾根大学博士研究者. 图宾根大学与图宾根 AI 中心 Gerard Pons-Moll 课题组研究者，FrankenMotion（CVPR 2026）第一作者。 https://coral79.github.io/
- **Claire Nee** (1) — 朴次茅斯大学司法心理学教授. 研究入室盗窃者的专业技能与决策，共同领导虚拟入室盗窃项目。
- **Cong Wei** (1) — 滑铁卢大学博士研究者. Cong Wei 是滑铁卢大学的博士研究者，MoCha（2025）的第一作者。该工作与 Meta GenAI 团队合作完成，可根据语音和文本生成电影风格的说话角色，包括两个角色之间的对话。 https://congwei1230.github.io/MoCha/
- **Connor Powelson** (1) — 刑事司法研究者. 2025 年一项关于警察在精神健康协同出警中如何决策的 VR 出声思维研究的第一作者。
- **Cyrus Vachha** (1) — 加州大学伯克利分校电子工程与计算机系研究者. 研究沉浸式三维创作与辐射场（NeRF、高斯泼溅），与 Björn Hartmann 合作。
- **D-ID** (1) — 数字人与可视化 AI 智能体公司. D-ID 能让照片中的人脸动起来，并提供实时的可视化 AI 智能体；2026 年推出面向交互与脚本场景的 V4 Expressive 虚拟人。 https://www.d-id.com
- **Daily** (1) — WebRTC 音视频基础设施公司. 提供实时视频 API，维护开源智能体框架 Pipecat 与 Pipecat Cloud。 https://www.daily.co
- **Dan Pollak** (1) — 赖克曼大学先进现实实验室研究员. Inceptor 的第一作者，该流程可为心理健康训练生成社会 VR 片段。
- **Daniel Duckworth** (1) — Google DeepMind 研究工程师. Google 研究者，SMERF 第一作者，这是一种可在浏览器中流式加载大场景的辐射场。
- **Daniel Watson** (1) — Google DeepMind 研究科学家. 4DiM 及谷歌早期三维新视角扩散工作 3DiM 的共同第一作者。
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
- **Dohui Lee** (1) — 韩国科学技术院（KAIST）元宇宙研究生院研究者. 与 Sang Ho Yoon（KAIST）和 Qi Sun（纽约大学）合作研究 VR 交互设计，HOICraft（CHI 2026）第一作者。
- **Duotun Wang** (1) — 香港科技大学（广州）博士研究者. 与 Zeyu Wang、Mingming Fan 合作研究面向混合现实的生成式 AI，2026 年 IJHCI 视觉生成式 AI 与 MR 综述第一作者。
- **Duowen Chen** (1) — 仿真与图形学研究者（佐治亚理工学院）. Duowen Chen 在佐治亚理工学院 Bo Zhu 课题组研究生成式三维世界中的仿真与声音。
- **Dylan Ebert** (1) — Hugging Face 机器学习工程师. 在 Hugging Face 从事三维机器学习，3D Arena 的创建者。
- **Dynamics Lab** (1) — 生成式游戏引擎初创公司. 推出 Mirage（2025 年 7 月）与 Mirage 2（2025 年 8 月）这两款可在浏览器中游玩的生成式世界引擎的初创公司；2026 年 10 月核查时，其网站与发布帖均已下线。
- **Egon Brunswik** (1) — 心理学家，加州大学伯克利分校（1903–1955）. 出生于匈牙利的心理学家，提出概率功能主义与“透镜模型”，主张实验应像抽样被试一样认真地抽样情境。
- **Eloi Alonso** (1) — 研究者，DIAMOND 第一作者. 日内瓦大学的机器学习研究者，研究用于强化学习的扩散世界模型。
- **Emergence AI** (1) — 带有研究实验室的智能体系统公司. 总部位于纽约的公司，为企业构建自主智能体系统。其研究实验室运营 Emergence World，一个长期运行的大语言模型智能体社会模拟。 https://www.emergence.ai/
- **Enyao Chang** (1) — 北京交通大学软件学院研究者. 2026 年一项关于 VR 演讲练习中大语言模型驱动的“教练评委”的随机研究的第一作者。
- **Erzhen Hu** (1) — 弗吉尼亚大学计算机系博士研究者. 研究 XR 通信，与 Google XR 合作者完成 Thing2Reality 的第一作者。
- **Esen K. Tütüncü** (1) — 巴塞罗那大学神经科学研究所研究者. HCI 与 XR 研究者，PlayWrite 的第一作者，该项目与 Autodesk Research（多伦多、旧金山）合作完成。
- **Etched** (1) — AI 芯片公司. 设计 Transformer 专用推理芯片 Sohu 的初创公司，与 Decart 合作开发了 Oasis。 https://www.etched.com
- **Evercoast** (1) — 4D 体积捕捉公司. 旗下 Mavericks 采集软件与 Cloudbreak 处理软件可把同步多相机画面转换为 4D 空间视频，用于音乐、体育、虚拟制片与机器人数据。 https://evercoast.com/
- **Eyeline Labs (Netflix)** (1) — Netflix 旗下 Eyeline 制作技术团队的研究实验室. 隶属 Netflix 的研究实验室，研究面向影视制作的生成式视频与拍摄技术，成果包括 Vista4D（CVPR 2026 Highlight）。 https://eyeline-labs.github.io/Vista4D/
- **Fangfu Liu** (1) — 研究者，Gamma-World 第一作者（与 NVIDIA 合作）. Gamma-World（2026）的第一作者；该多智能体交互世界模型来自 NVIDIA Research 空间智能实验室。
- **Fernanda De La Torre** (1) — 麻省理工学院脑与认知科学系研究者；与微软合作的 LLMR 第一作者. 主导 LLMR：微软用语言模型创建与修改交互式混合现实世界的框架。
- **Fernanda Herrera** (1) — 斯坦福虚拟人交互实验室研究员. 主导了比较 VR 与传统换位思考的大规模《Becoming Homeless》研究。
- **Figmin XR** (1) — 混合现实创作应用 Figmin XR 背后的独立团队. 开发 Figmin XR：一款跨平台（Quest、Vision Pro、HoloLens）的应用，用于搭建和分享混合现实场景、玩具与可编程物体。 https://figmin.com
- **Fish Audio** (1) — 语音 AI 公司（Hanabi AI Inc.）. Fish Audio 运营语音合成与声音克隆平台，并发布开源权重的语音合成模型，从 Fish Speech 到 Drama 3。 https://fish.audio
- **Floreo** (1) — 为自闭症及神经多样性学习者提供临床设计课程的 VR 平台. 在头显上提供 VR 课程（社交技能、安全、与警察互动），由辅导者跟进并引导学习者；联合创始人兼 CEO 为 Vijay Ravindran。 https://floreovr.com/
- **Franziska Grießenauer** (1) — 萨尔茨堡大学心理学研究者. 在 Thomas Probst 的心理治疗研究组从事放松与意象技术研究；2026 年一项 VR 中 AI 生成个人安全之地随机试验的第一作者。
- **Gale Lucas** (1) — 南加州大学创意技术研究所研究员. 社会心理学家，发现人们在相信虚拟人由计算机控制时会披露更多。
- **Gavriel Habib** (1) — OriginAI 研究者. Gavriel Habib 是 PixReenact（2026）的第一作者。该工作来自 OriginAI，合作者包括英伟达的 Dvir Samuel，是一个流式头像重演模型。 https://gavriel-habib.github.io/pixreenact/
- **General Intuition** (1) — 研究在时空中行动的智能体的 AI 实验室. 从游戏片段平台 Medal 分拆出来的 AI 实验室，利用大规模游戏视频档案训练智能体与世界模型。 https://generalintuition.com
- **Genmo** (1) — 开源视频模型初创公司. 发布了 100 亿参数、Apache 2.0 许可的开源文生视频模型 Mochi 1。 https://www.genmo.ai
- **Georgy Savva** (1) — 纽约大学研究者，Solaris 第一作者. Solaris（2026）的第一作者。Solaris 是纽约大学推出的《我的世界》多人视频世界模型，配套一套自动化的多智能体数据采集系统。 https://solaris-wm.github.io/
- **GoodAI** (1) — 人工智能研究公司与游戏开发商. 总部位于布拉格的人工智能研究公司，由 Marek Rosa（Keen Software House 创始人）创办；开发了由大语言模型驱动 NPC 的沙盒游戏 AI People。 https://www.goodai.com/
- **Gracia** (1) — 体积高斯视频公司. 将 4D 高斯泼溅视频流式传输到 Quest、Pico、Apple Vision Pro、桌面与浏览器的公司，2026 年起把重点表述为面向物理 AI 的世界重建模型。 https://gracia.ai/
- **Gradium** (1) — 由 Kyutai 的 Moshi 研究者创立的语音 AI 公司. Gradium 为语音智能体提供流式语音合成、语音识别、翻译与声音设计；到 2026 年 7 月其种子轮融资达到 1 亿美元。 https://gradium.ai
- **Guan-Ting Lin** (1) — 台湾大学研究者. 李宏毅课题组的语音研究者，Full-Duplex-Bench 的第一作者，该基准与加州大学伯克利分校的合作者共同开发。
- **Guanjun Wu** (1) — 华中科技大学研究者. 《4D Gaussian Splatting for Real-Time Dynamic Scene Rendering》（CVPR 2024）第一作者。
- **Guanzhi Wang** (1) — 人工智能研究者（加州理工学院、英伟达）. 加州理工学院博士研究者，与英伟达合作；Voyager（2023）的第一作者，该智能体通过编写并保存代码技能来探索 Minecraft。
- **Guibao Shen** (1) — 立体转换研究者. 香港科技大学（广州）研究者，StereoPilot 第一作者，该工作在快手可灵团队实习期间完成。
- **Guido Makransky** (1) — 哥本哈根大学教育心理学教授. 研究沉浸式 VR 中的学习，合作提出 CAMIL 模型，解释临场感与能动性何时促进、何时妨碍学习。
- **Gustav Bøg Petersen** (1) — 与斯坦福虚拟人交互实验室合作的研究者. 研究 VR 中的学习与环境态度，OceanSpeak 对话式 AI 研究的第一作者。
- **Guy Tevet** (1) — 特拉维夫大学研究者. 特拉维夫大学研究者（与 Amit Bermano、Daniel Cohen-Or 合作），人体动作扩散模型 MDM（ICLR 2023）第一作者。 https://guytevet.github.io/
- **Habin Lim** (1) — 高丽大学研究者. Habin Lim 是 FacePlex（2026）的共同第一作者。该模型来自高丽大学与 Klleon，可全双工地生成语音与面部动作，并用高斯泼溅渲染。 https://hahminlew.github.io/faceplex
- **Haiyu Zhang** (1) — 研究者，WorldPlay2 第一作者. WorldPlay2（2026）的共同第一作者；该工作是腾讯混元实时世界模型 WorldPlay 的后续研究，作者与 WorldPlay 多有重合。
- **Hal Hershfield** (1) — 加州大学洛杉矶分校安德森管理学院市场营销与行为决策教授. 研究“未来自我”心理学；与斯坦福 VHIL 合作发现，见到自己变老的化身会增加储蓄。
- **Hanlin Wang** (1) — 香港科技大学研究者，WorldDirector 第一作者. WorldDirector（2026）的第一作者。WorldDirector 是香港科技大学与蚂蚁集团合作的可控视频世界模型，能持久记住运动物体。 https://worlddirector.github.io/
- **Hanmo Chen** (1) — 音视频联合生成研究者（西安电子科技大学与 vivo 蓝图影像实验室）. Hanmo Chen 在西安电子科技大学和 vivo 蓝图影像实验室研究音视频联合生成。
- **Hanwen Liang** (1) — 多伦多大学研究者. 多伦多大学的博士研究者，与 Snap Research 合作完成 Wonderland 并任第一作者。
- **Hanxue Liang** (1) — 剑桥大学 / NVIDIA 研究者. NVIDIA 前馈式子弹时间重建模型 BTimer 的第一作者。
- **Hao Zhang** (1) — 伊利诺伊大学厄巴纳-香槟分校博士研究者，Snap 研究实习生. 伊利诺伊大学厄巴纳-香槟分校研究者，与 Snap Research 合作完成的 RigMo 第一作者。 https://haoz19.github.io/
- **Haocheng Xi** (1) — 加州大学伯克利分校博士研究者. Haocheng Xi 是 Video DeltaNet（2026）的第一作者。该工作是 MiniMax H3 的开源混合注意力版本，在加州大学伯克利分校完成，部分工作在 Impossible, Inc. 实习期间进行。 https://openvdn.github.io/
- **Haotong Lin** (1) — 字节跳动 Seed / 浙江大学研究者. Depth Anything 3 第一作者。
- **Haoxuan Che** (1) — 香港科技大学研究者，GameGen-X 第一作者. GameGen-X（2024）的第一作者；该模型是用于生成并交互控制开放世界游戏视频的扩散 Transformer。
- **Haoyi Duan** (1) — 斯坦福大学研究者. 与吴佳俊、李飞飞合作，WorldScore 的第一作者。 https://haoyi-duan.github.io
- **Haoyi Zhu** (1) — 上海人工智能实验室研究者. 上海人工智能实验室开源几何感知世界模型 Aether 的第一作者。
- **Haoyu Wang** (1) — 伦敦帝国理工学院戴森设计工程学院研究者. 研究混合现实中的触觉与生成式 AI，与多伦多大学 Dynamic Graphics Project 合作者共同完成 Prop-Chromeleon。
- **Haoyuan Li** (1) — 研究者，PanoWorld 第一作者. PanoWorld（2026）的第一作者；该具备长程记忆的全景世界模型由 Insta360 研究团队与中国科学院自动化研究所合作完成。
- **Hedra** (1) — 生成式角色视频公司. Hedra 开发音频驱动的角色视频模型（Character-3）和制作会说话角色的工作室。 https://www.hedra.com
- **Heng Yu** (1) — 卡内基梅隆大学博士研究者. 4Real（NeurIPS 2024）第一作者，与 Snap Research 合作完成。
- **Hezhen Hu** (1) — 得克萨斯大学奥斯汀分校研究者. Hezhen Hu是 HumanNOVA（CVPR 2026 Highlight）的第一作者，与得克萨斯大学奥斯汀分校的 Georgios Pavlakos、Zhangyang Wang 合作；HumanNOVA 是一个由单张照片前馈生成三维人体化身的模型。 https://humannova.github.io
- **Ho Kei Cheng** (1) — 计算机视觉研究者（伊利诺伊大学厄巴纳-香槟分校）. Ho Kei（Rex）Cheng 以视频目标分割（XMem、Cutie）以及与 Sony AI 合作开发的 MMAudio 视频配音模型而知名。 https://hkchengrex.com
- **Hongxin Zhang** (1) — 麻省大学阿默斯特分校博士研究者. 麻省大学阿默斯特分校 Chuang Gan 具身智能实验室研究者，同时隶属 Genesis AI，GS-Agent（2026）第一作者。 https://icefoxzhx.github.io/
- **Hongyuan Chen** (1) — 西湖大学研究者. 西湖大学 Anpei Chen 课题组研究者，Motion 3-to-4（CVPR 2026）第一作者。 https://hyuanchen.github.io/
- **Hongzhou Zhu** (1) — 清华大学博士研究者. Hongzhou Zhu是 Causal Forcing（ICML 2026）的第一作者，来自清华大学朱军教授的机器学习组，也是生数科技 Vidu S2 技术报告的作者之一。 https://zhuhz22.github.io/
- **Horizon Robotics** (1) — 中国的车载与机器人 AI 芯片及软件公司. 地平线研发 AI 处理器与智能驾驶软件；其机器人团队开源了 EmbodiedGen 工具包（2025）和 EmbodiedGen V2（2026）。
- **Huan Ling** (1) — 英伟达多伦多 AI 实验室研究科学家. 英伟达基于动态三维高斯的文本到 4D 方法 Align Your Gaussians 的第一作者。 https://www.cs.toronto.edu/~linghuan/
- **Hugues Bruyère** (1) — Dpt.（蒙特利尔）合伙人与创新负责人. 创意技术专家，用实时生成模型制作交互装置与混合现实体验原型。
- **Hunter Hoffman** (1) — 华盛顿大学研究科学家. 与 David Patterson 合作开发 SnowWorld，在烧伤换药时分散患者对疼痛的注意。
- **Insta360** (1) — 拥有 AI 研究团队的全景相机厂商. 消费级全景相机厂商；其研究团队与中国科学院自动化研究所合作，于 2026 年发布全景世界模型 PanoWorld。 https://www.insta360.com/
- **Jacob Barker** (1) — VORTeX（2026）第一作者. 开发用于训练和评估外科团队协作的“虚拟手术室团队体验”（VORTeX）。
- **Jaewook Lee** (1) — 华盛顿大学 Makeability Lab 博士研究者. 研究 AI 驱动的增强现实，与 Niantic Spatial 合作主导 ImaginateAR。
- **Jaeyeon Kim** (1) — 视听学习研究者（首尔大学）. Jaeyeon Kim 在首尔大学视觉与学习实验室研究视听生成。 https://jaeyeonkim99.github.io/visage/
- **Jaeyoung Chung** (1) — 首尔国立大学计算机视觉实验室研究者. 首尔国立大学 Kyoung Mu Lee 实验室的研究者，LucidDreamer 的共同第一作者。
- **Jawset** (1) — Postshot 开发商. 开发 Postshot 的小型软件公司，Postshot 是在本地 GPU 上训练和编辑辐射场与高斯泼溅的桌面应用。 https://www.jawset.com/
- **Ji Xia** (1) — MBZUAI 基础模型研究院研究者，LOCI 第一作者. LOCI（2026）的第一作者。LOCI 是采用混合空间记忆的流式世界模型，出自 MBZUAI 基础模型研究院的同一团队，该团队还发表了 Memorizon。 https://xiaji2021.github.io/LOCI/
- **Jiahao Lu** (1) — 香港科技大学博士研究者. GAE（2026）的共同第一作者；该工作与腾讯 ARC 实验室合作，为世界生成提出了几何原生的潜空间。 https://jiah-cloud.github.io/GAE.github.io/
- **Jianan Jiang** (1) — 宾夕法尼亚州立大学 SNeC 实验室博士研究者. 研究扩展现实中的生成式三维创作，在宾州州立大学与 Bin Li 合作。 https://horizonjohn.github.io/
- **Jianhong Bai** (1) — 镜头可控视频研究者. 浙江大学研究者，与快手可灵团队合作完成 ReCamMaster。 https://jianhongbai.github.io/
- **Jianjie Fang** (1) — 清华大学研究者，iWorld-Bench 第一作者. iWorld-Bench（ICML 2026）的第一作者。该基准与排行榜用于评测世界模型的交互能力，在清华大学 EmbodiedCity 项目下发布。 http://iWorld-Bench.com
- **Jiaxiang Tang** (1) — 北京大学博士研究者. 北京大学研究者，DreamGaussian（ICLR 2024 口头报告）第一作者，是较早把三维高斯泼溅用于生成的工作。 https://me.kiui.moe/
- **Jiaxin Huang** (1) — 浙江大学 X-D Lab（廖依伊课题组）研究者. Gen3R（CVPR 2026）的第一作者，该工作把视频扩散模型与 VGGT 重建模型耦合在一起。 https://xdimlab.github.io/Gen3R/
- **Jiayuan Wen** (1) — 伦敦大学学院虚拟环境与计算机图形组研究者. 与 Anthony Steed、Daniele Giunchi 和 Eyal Ofek 合作研究 VR 中的自适应音频。
- **Jing Tan** (1) — 沉浸式视频生成研究者. 香港中文大学研究者，Imagine360 第一作者。
- **Jingcheng Ni** (1) — 布朗大学博士研究者. 布朗大学 Srinath Sridhar 课题组研究者，与麻省理工学院、耶鲁大学和香港大学合作完成的 Sonic-AMG（2026）第一作者。 https://jingchengni.com/
- **Jingjing Jiang** (1) — 名古屋大学研究者. Jingjing Jiang 是 Moshi-Face（Interspeech 2026）的第一作者，来自名古屋大学信息学研究科东中龙一郎（Ryuichiro Higashinaka）的对话系统团队。 https://arxiv.org/abs/2606.21970
- **Jingwei Ma** (1) — 全景视频合成研究者. 华盛顿大学研究者，与 Google DeepMind 合作的 VidPanos（SIGGRAPH Asia 2024）第一作者。 https://vidpanos.github.io/
- **Jinpeng Lu** (1) — 研究者，WRBench 第一作者. 论文《Current World Models Lack a Persistent State Core》（2026）的第一作者，该文提出诊断性基准 WRBench；项目主页列出的参与机构包括中国科学技术大学、中国科学院自动化研究所、X-Humanoid 与德累斯顿工业大学。 https://jinplu.github.io/WRBench/
- **Jonathan Steuer** (1) — 传播学研究者（1992 年时在斯坦福大学）. 1992 年发表论文，以“远程临场”体验及其两个决定因素——生动性与交互性——来定义虚拟现实。
- **Jonathan Tseng** (1) — 斯坦福大学研究者. 斯坦福大学研究者（与 C. Karen Liu 合作），由音乐生成可编辑舞蹈的 EDGE（CVPR 2023）第一作者。 https://edge-dance.github.io/
- **Joseph P. McCleery** (1) — 费城的自闭症研究者. 临床科学家，自 2018 年起与费城儿童医院自闭症研究中心合作，在自闭症青少年与成人中测试 Floreo 的 VR 警察安全模块。
- **Juming Jiang** (1) — 香港都会大学健康教育研究者. 2026 年 JMIR 一篇关于医疗卫生教育中生成式 AI 虚拟病人的系统综述的第一作者。
- **Junliang Guo** (1) — 微软研究院研究者，MineWorld 第一作者. MineWorld（2025）的第一作者；MineWorld 是微软研究院开源的 Minecraft 实时交互世界模型。
- **Junlong Chen** (1) — 剑桥大学工程系博士研究者. 与 Per Ola Kristensson 合作研究大语言模型辅助的沉浸式场景编辑。
- **Junyi Wu** (1) — 研究者，World-T3 第一作者. World-T3（2026）的第一作者；该实时视频世界模型采用测试时训练记忆，由伊利诺伊大学芝加哥分校与 Meta Reality Labs 合作完成。
- **Junyi Zhang** (1) — 加州大学伯克利分校博士研究者. MonST3R（ICLR 2025）第一作者。
- **Justin Cui** (1) — 长视频生成研究者. 加州大学洛杉矶分校研究者，Self-Forcing++ 第一作者，该工作与字节跳动 Seed 合作完成。
- **K R Prajwal** (1) — 唇形同步与语音驱动视频研究者. K R Prajwal 当时在印度海得拉巴国际信息技术学院（IIIT Hyderabad），是 Wav2Lip（ACM Multimedia 2020）的第一作者。
- **K. Anders Ericsson** (1) — 心理学家，佛罗里达州立大学（1947–2020）. 瑞典心理学家，开创了专家表现研究，并界定了“刻意练习”的概念。
- **Kaifeng Zhao** (1) — 苏黎世联邦理工学院博士研究者. 苏黎世联邦理工学院研究者（与 Siyu Tang 合作），在英伟达完成的 ARDY（SIGGRAPH 2026）第一作者。 https://research.nvidia.com/labs/sil/projects/ardy/
- **Kaining Ying** (1) — 复旦大学研究者，WBench 第一作者. WBench（2026）的第一作者。WBench 是复旦大学与美团 LongCat 团队构建的交互视频世界模型多轮评测基准，并设有公开排行榜。 https://meituan-longcat.github.io/WBench/
- **Kaixin Ding** (1) — 研究者，PlayWorld 第一作者. PlayWorld（2026）的第一作者。PlayWorld 是快手与香港大学推出的基准，让多模态智能体在世界模型中追求长时程目标。 https://kxding.github.io/project/PlayWorld/
- **Kaixin Yao** (1) — 上海科技大学与影眸科技研究者. CAST（SIGGRAPH 2025 最佳论文）的第一作者，该工作由上海科技大学与影眸科技完成。
- **Kamilla Bergsnev** (1) — 2026 年一篇关于 AI 用于 VR 暴露疗法的系统综述的第一作者. 系统梳理了人工智能如何被用来定制 VR 暴露疗法的研究者。
- **Kandinsky Lab** (1) — Kandinsky 图像与视频模型的研发团队. 发布 Kandinsky 图像、视频与世界模型的研究团队，多数模型为开源权重；Kandinsky 6.0 Video（2026）可生成带同步音频的视频。 https://kandinskylab.ai
- **Kartik Teotia** (1) — 马克斯·普朗克信息学研究所研究者. Kartik Teotia 在马克斯·普朗克信息学研究所 Christian Theobalt 团队研究对话式三维头部化身，是 STEER（SIGGRAPH Asia 2026）的第一作者。 https://kartik-teotia.github.io/STEER/
- **Ke Xing** (1) — 立体视频生成研究者. 北京交通大学研究者（与 Dzine AI 合作），StereoWorld（CVPR 2026）第一作者。 https://ke-xing.github.io/StereoWorld/
- **Kevin Xie** (1) — NVIDIA 多伦多 AI 实验室研究者. NVIDIA 多伦多 AI 实验室研究者，VideoPanda 共同第一作者。 https://research.nvidia.com/labs/toronto-ai/VideoPanda/
- **Kim Youwang** (1) — POSTECH 博士研究者. Kim Youwang 是 POSTECH 的博士研究者，FiCA（2026）的第一作者。该工作在 Meta Codec Avatars 实验室实习期间完成，可从一张人像照片生成可驱动的高斯 Codec Avatar。 https://youwangk.github.io/FiCA.html
- **Kiwhan Song** (1) — MIT 研究者，《历史引导视频扩散》第一作者. 《历史引导视频扩散》（ICML 2025）的第一作者；该工作与 Boyuan Chen、Max Simchowitz、Yilun Du、Russ Tedrake、Vincent Sitzmann 合作提出 Diffusion Forcing Transformer。
- **Koji Inoue** (1) — 京都大学研究者. Koji Inoue 在京都大学河原达也（Tatsuya Kawahara）实验室研究对话机器人与虚拟人的语音对话和倾听行为（附和、话轮转换、点头）。
- **Koki Nagano** (1) — 英伟达研究院研究科学家. Koki Nagano 在英伟达研究院从事数字人研究，是 DyaPlex（NeurIPS 2026）的共同第一作者；DyaPlex 是面向双人互动的全双工语音与动作模型。 https://research.nvidia.com/labs/amri/projects/DyaPlex/
- **Kolby Nottingham** (1) — 人工智能研究者. 研究游戏中的语言模型智能体；与 Max Robinson 共同开发 Mindcraft，后者的 YouTube 频道 Emergent Garden 让这个机器人广为人知。 https://kolbynottingham.com/
- **Konstantin W. Kühlem** (1) — 亚琛工业大学视觉计算研究所研究员. VR 中具身对话智能体低延迟大语言模型对话系统（IVA 2025）的第一作者。
- **Krea** (1) — 实时创意 AI 工具公司. 以实时图像生成著称的创意工具公司；2025 年 10 月发布开源的 Krea Realtime 14B 视频模型。 https://www.krea.ai
- **Kunhao Liu** (1) — 流式视频生成研究者. 南洋理工大学研究者，Rolling Forcing（ICLR 2026）第一作者，该工作与腾讯 ARC 实验室合作完成。 https://kunhao-liu.github.io/
- **Kyle Johnsen** (1) — 计算机科学家（佛罗里达大学，后任职于佐治亚大学）. 与 Benjamin Lok 团队合作构建并验证了用于医学问诊训练的真人大小虚拟病人。
- **Leia Inc.** (1) — 3D 显示与空间 AI 公司（Immersity）. 可切换 2D/3D 光场显示屏与 Immersity 平台的开发者，其软件估计普通照片和视频的深度，从而以 3D 方式呈现。 https://www.immersity.ai
- **LemonSlice** (1) — 交互式虚拟人模型公司. LemonSlice 开发用于交互式虚拟人的实时视频扩散模型（2025 年的 LemonSlice-2、2026 年的 Character World Model-1），可从一张图像驱动任意角色。 https://lemonslice.com
- **Li Hu** (1) — 阿里巴巴通义实验室研究者，WanToFight 第一作者. WanToFight（2026）的第一作者。WanToFight 是阿里巴巴通义实验室用视频模型生成的实时双人格斗游戏引擎。 https://humanaigc.github.io/wantofight/
- **Liangyang Ouyang** (1) — 东京大学博士研究者，HelloWorld 第一作者. HelloWorld（2026）的第一作者；该视频世界模型让画面中的角色能对用户做出社交回应，由 Alaya Lab 与东京大学佐藤洋一实验室合作完成。
- **Light in the Head** (1) — Marc Da Costa 与 Matthew Niederhauser 的工作室. 使用机器学习、VR 与装置创作的艺术家二人组，也是 Sensorium 的联合创始人。
- **Lihan Jiang** (1) — 中国科学技术大学 / 上海人工智能实验室研究者. AnySplat（SIGGRAPH Asia 2025）第一作者。
- **Lihe Yang** (1) — 香港大学研究者. 香港大学赵恒爽组的博士研究者，与字节跳动（TikTok）合作的 Depth Anything 与 Depth Anything V2 的第一作者。 https://liheyoung.github.io
- **Lingen Li** (1) — 全景视频生成研究者. 香港中文大学研究者，CubeComposer（CVPR 2026）第一作者，该工作与腾讯 ARC 实验室合作完成。 https://lg-li.github.io/
- **Linxi (Jim) Fan** (1) — 人工智能研究者（英伟达）. 英伟达研究科学家，研究具身智能体与机器人基础模型；MineDojo（2022）的第一作者，也是 Voyager（2023）的合作者。 https://jimfan.me/
- **Linxi Xie** (1) — 斯坦福大学研究者，Generated Reality 第一作者. Generated Reality（CVPR 2026 Findings）的第一作者。该工作是由头部与手部追踪控制的 VR 视频世界模型，出自斯坦福大学 Gordon Wetzstein 团队，合作者来自上海纽约大学与北卡罗来纳大学。 https://codeysun.github.io/generated-reality/
- **Linyi Jin** (1) — 密歇根大学 / Google DeepMind 博士研究者. Stereo4D（CVPR 2025）第一作者，与 Google DeepMind 合作，利用互联网 VR180 视频构建。
- **Linzhan Mou** (1) — 普林斯顿大学博士研究者. 普林斯顿大学图形学研究者（与 Adam Finkelstein、Szymon Rusinkiewicz 合作），UniMate（SIGGRAPH Asia 2026）第一作者。 https://linzhanmou.com/unimate/
- **Liquid City** (1) — 由 Keiichi Matsuda 创立的设计工作室. 由设计师、电影人 Keiichi Matsuda（Hyper-Reality、Merger）领导的工作室，设计 AR、AI 智能体与空间界面。 https://www.liquid.city
- **LiveKit** (1) — 实时音视频基础设施公司. 开发开源 WebRTC 媒体服务器、LiveKit Agents 框架与 LiveKit Cloud。 https://livekit.io
- **Liyuan Zhu** (1) — 斯坦福大学博士研究者. 斯坦福大学博士研究者（与 Iro Armeni、Gordon Wetzstein 合作），与 NVIDIA 合作完成的 World from Motion（NeurIPS 2026）第一作者。 https://www.zhuliyuan.net/
- **Longwen Zhang** (1) — 上海科技大学 / 影眸科技研究者. CLAY（SIGGRAPH 2024）第一作者，该原生三维生成模型后来成为 Rodin Gen-1。
- **Lu Ling** (1) — 普渡大学研究者. DL3DV-10K 的第一作者，这是一个面向三维视觉的大型真实场景视频数据集。 https://dl3dv-10k.github.io/DL3DV-10K/
- **Lukas Höllein** (1) — 慕尼黑工业大学研究者. 慕尼黑工业大学 Matthias Niessner 视觉计算与 AI 实验室的博士研究者，Text2Room 的第一作者。 https://lukashoel.github.io
- **Lvmin Zhang** (1) — 可控生成研究者. 斯坦福博士研究者，ControlNet、IC-Light 与 FramePack 的作者。
- **MBZUAI Institute of Foundation Models** (1) — 穆罕默德·本·扎耶德人工智能大学（MBZUAI）的基础模型研究院. MBZUAI 下属研究院；2026 年 9 月，其世界模型团队发布了 LOCI（空间线性记忆）与 Memorizon（超出上下文窗口的训练）。
- **Manycore Tech** (1) — 杭州公司，运营酷家乐室内设计平台，并开源空间智能模型. 群核科技运营酷家乐室内设计平台，并开源了 SpatialLM（2025）和 SpatialGen（2025）等空间智能模型。 https://manycoretech.com/
- **Marcel Binz** (1) — 认知科学家（慕尼黑亥姆霍兹中心）. 慕尼黑亥姆霍兹中心“以人为本人工智能研究所”的研究者，构建人类认知的机器学习模型；Centaur（《自然》，2025）的第一作者。
- **Martin de La Gorce** (1) — 微软研究者. 微软研究者，VoluMe（2025）第一作者。
- **Math Magic (Hi3D)** (1) — Hi3D 背后的三维生成公司. 深圳公司，开发 Hi3D（原名 Hitem3D）图生三维平台，面向游戏、设计和 3D 打印，提供模型拆分和多色打印准备等功能。 https://www.hi3d.ai
- **Matt Deitke** (1) — AI 研究者（Objaverse、Objaverse-XL）. 在艾伦人工智能研究所主导了 Objaverse 与 Objaverse-XL 三维数据集。 https://mattdeitke.com
- **Matt Gottsacker** (1) — 中佛罗里达大学研究者. 2026 年 VERA 论文的第一作者，该研究让 263 名参与者用自己的头显远程完成晕动症实验。
- **Matt Zhou** (1) — 剑桥大学研究者. Articraft 第一作者；该系统由剑桥大学 Shangzhe Wu 课题组与牛津大学视觉几何组（VGG）合作完成，用智能体生成可活动的三维资产。 https://articraft3d.github.io/
- **Matthew J. Smith** (1) — 社会工作研究者（西北大学，后任职于密歇根大学）. 以虚拟面试官 Molly Porter 为核心的虚拟现实求职面试训练试验的第一作者。
- **Max Kinateder** (1) — 研究火灾与疏散中人类行为的研究者. 用 VR 研究疏散决策的心理学家；2016 年的真实与虚拟环境对比研究是他与 William H. Warren 在布朗大学完成的。
- **Mehdi Moussaïd** (1) — 马克斯·普朗克人类发展研究所研究科学家. 研究人群行为与集体动力学，包括让真实参与者在共享虚拟环境中进行人群疏散实验。
- **Mehrnaz Hosseinzadeh** (1) — 认知与行为科学研究者. 2026 年一篇关于心理学与认知神经科学中沉浸式 VR 实验搭建工具的范围综述的第一作者。
- **Meng-Li Shih** (1) — 研究者（弗吉尼亚理工，后至华盛顿大学）. 《3D Photography using Context-aware Layered Depth Inpainting》（CVPR 2020）的第一作者，合作者包括黄嘉斌与 Johannes Kopf。 https://shihmengli.github.io
- **Mengxu Pan** (1) — 研究社交 VR 中大语言模型智能体的人机交互研究者. CHI 2026 一项研究的第一作者：英语学习者在社交 VR 中与基于大语言模型的具身智能体练习；合作者来自维多利亚大学、不列颠哥伦比亚大学与东北大学。
- **Michal Geyer** (1) — 视频合成研究者. 魏茨曼科学研究所研究者，Eye2Eye 第一作者（工作在 Google DeepMind 完成）。 https://video-eye2eye.github.io/
- **Midjourney** (1) — 独立图像与视频生成实验室. 自筹资金的实验室，以审美导向的图像模型著称；2025 年 6 月发布首个视频模型。 https://www.midjourney.com
- **Mirelo** (1) — 制作视频生成音效模型的音频 AI 公司. Mirelo 开发为视频添加音效、拟音与环境声的生成模型，通过在线工作室、API 和剪辑软件插件提供。 https://mirelo.ai
- **Moonvalley** (1) — 面向影视创作者的视频生成公司. 与工作室 Asteria 一同开发只用授权素材训练的视频模型 Marey。 https://www.moonvalley.com
- **Moreah Zisquit** (1) — 赖克曼大学研究员. 2025 年一项在 VR 自我对话咨询中加入 AI 智能体的形成性研究的第一作者。
- **Moxin** (1) — 基于 NPU 构建世界模型的公司. MoWorld（2026）的开发公司；它称 MoWorld 是首个基于神经网络处理器（NPU）构建的实时交互世界模型，曾在 2026 年世界人工智能大会展出，并于 2026 年 9 月开源。 https://moxin-tech.github.io/moworld/
- **Mursion** (1) — 沉浸式模拟训练公司. 源于“人在回路”教学模拟器的研究；由受过训练的模拟专员实时为化身配音并操控其行为，公司如今主打 AI 驱动的模拟。 https://www.mursion.com/
- **Muyao Niu** (1) — 东京大学博士研究者，与 Alaya Lab 合作. WorldSculpt（2026）的第一作者，该项目由 Alaya Lab 与东京大学合作完成。 https://alaya-lab.github.io/WorldSculpt/
- **Muzhe Wu** (1) — 密歇根大学博士研究者. 与 Anhong Guo、Xu Wang 合作，研究为现实任务生成的 AI 指导。
- **Naisha Agarwal** (1) — 加州大学洛杉矶分校研究者；微软研究院合作者. 与微软研究院的 Judith Amores、Andrew D. Wilson 合作主导 Storycaster。
- **Nathalia Gomez** (1) — 德雷塞尔大学人机交互研究者. 与 Tiffany D. Do 合作研究 VR 中的具身对话智能体；《Listening and Mirroring》（VRST 2026）的第一作者。
- **Nels Numan** (1) — 伦敦大学学院博士研究者；微软研究院合作者. 研究协作式混合现实与远程临场，SpaceBlender 第一作者，也是 XR Blocks 的合作者。
- **NetEase Games** (1) — 电子游戏开发商与发行商. 中国游戏公司，旗下有《逆水寒》《蛋仔派对》《永劫无间》；2023 年在《逆水寒》手游中上线 LLM 驱动的 NPC，2025 年在《永劫无间》手游 PC 版中上线基于英伟达 ACE、本地运行的 AI 队友。 https://www.neteasegames.com/
- **Nick Yee** (1) — 化身与网络游戏研究者（斯坦福 VHIL；后联合创办 Quantic Foundry）. 在斯坦福读博期间与 Jeremy Bailenson 一起提出“普罗透斯效应”，之后大规模研究玩家动机。
- **Nicolas Moenne-Loccoz** (1) — NVIDIA 研究者. NVIDIA 研究者，3D Gaussian Ray Tracing（3DGRT）第一作者。
- **Nicolas von Lützow** (1) — 慕尼黑工业大学视觉计算与人工智能实验室博士研究者. GaussianGPT（ECCV 2026 口头报告）的第一作者，该工作完成于慕尼黑工业大学 Matthias Niessner 的研究组。 https://nicolasvonluetzow.github.io/GaussianGPT/
- **Nikhil Keetha** (1) — 卡内基梅隆大学 / Meta 博士研究者. MapAnything 第一作者，这是 Meta 与卡内基梅隆大学合作的公制三维重建模型。
- **Nima Zargham** (1) — 不来梅大学数字媒体实验室研究者. 人机交互与游戏研究者，任职于 Rainer Malaka 领导的数字媒体实验室，研究游戏中的语音交互与对话智能体。
- **Noiz AI** (1) — 音视频生成式 AI 公司. 与香港科技大学合作发布 HelixWorld（2026）的公司；HelixWorld 是一个同时生成视频与空间立体声的实时世界模型。 https://helixworld.org/
- **Nozomu Iwai** (1) — Preferred Networks 研究者. Preferred Networks 研究者，与 Fabrice Matulic 合作完成 AR 会说话物件研究（CHI 2025 扩展摘要）的第一作者。
- **OpenBMB** (1) — 面壁智能与清华 NLP 实验室的开源模型社区. OpenBMB 是 MiniCPM 系列模型背后的开源项目，由面壁智能与清华大学自然语言处理实验室主导。 https://www.openbmb.cn
- **Ophilus.AI** (1) — AI 公司，多智能体世界模型 Khora 的联合开发方. 与 RhOS.ai 联合开发 Khora：一个从同一份共享世界状态渲染任意数量玩家画面的世界模型（2026 年 8 月发布技术报告）。
- **Overworld** (1) — 开源世界模型初创公司. 发布可在消费级显卡本地运行的开源实时扩散世界模型（Waypoint）及开源客户端 Biome 的初创公司。 https://over.world
- **Pao-Ju Chen** (1) — 亚东科技大学护理教育者. 从事基于模拟的护理教育研究；2026 年一项关于产科共情沟通的 AI 增强 VR 模拟随机研究的第一作者。
- **Patrick Kenny** (1) — 南加州大学创意技术研究所研究员（2000 年代）. 在 USC ICT 主持虚拟人与虚拟病人项目，包括 2007 年 I/ITSEC 上关于构建训练用交互式虚拟人的综述。
- **Patrick McClanahan** (1) — 犯罪学研究者，宾夕法尼亚虚拟入室盗窃项目（马克斯·普朗克犯罪、安全与法律研究所）. 主导虚拟入室盗窃项目的宾夕法尼亚分支，把 VR 盗窃任务带进美国监狱，并以开放获取方式公开了虚拟街区。
- **Patrick Pui Kin Kor** (1) — 香港理工大学护理学研究者. 研究护理教育与老年护理；主持了 2026 年一项比较沉浸式 VR 护理模拟后生成式 AI 复盘与教师复盘的研究。
- **Pau Mora** (1) — 瓦伦西亚理工大学研究者. 在 Mariano Alcañiz 的研究组开发用于心理健康的生成式 VR 工具；Refugio（2026）的第一作者。
- **Paul Engstler** (1) — 牛津大学视觉几何组（VGG）博士研究者. 与 Iro Laina、Christian Rupprecht 和 Andrea Vedaldi 合作研究三维场景生成，SynCity（2025）与 SynCity 3000（2026）作者。 https://research.paulengstler.com/
- **Peiwen Sun** (1) — 空间音频生成研究者（香港科技大学）. Peiwen Sun 在香港科技大学研究语言驱动的音频生成。 https://peiwensun2000.github.io/bewo/
- **Peng Dai** (1) — 立体与空间视频研究者. 香港大学研究者，与 Google 合作的 S²VG 第一作者。 https://daipengwa.github.io/S-2VG_ProjectPage/
- **Pengjun Fang** (1) — 音频生成研究者（香港科技大学与 Noiz AI）. Pengjun Fang 在香港科技大学和初创公司 Noiz AI 研究视频到音频的生成。
- **Philippa Garety** (1) — 伦敦国王学院临床心理学教授. 临床心理学家，主持了针对精神病患者痛苦幻听的数字化身疗法 AVATAR2 试验。
- **Pika** (1) — 面向大众的视频生成初创公司. 2023 年由斯坦福博士生创立，以 Pika 1.0 和趣味化编辑特效著称。 https://pika.art
- **Polycam** (1) — 三维捕捉应用公司. 一款覆盖 LiDAR、摄影测量与高斯泼溅的手机、网页与无人机三维捕捉应用的开发商。 https://poly.cam/
- **Preferred Networks** (1) — 日本人工智能公司. 总部位于东京的 AI 公司，开发深度学习模型与 AI 芯片，并开展包括 AR 与角色交互在内的应用研究。 https://www.preferred.jp/en/
- **Princeton Vision & Learning Lab** (1) — 普林斯顿大学邓嘉的计算机视觉实验室. 由邓嘉领导的高校实验室，开发了 Infinigen 程序化世界生成器。 https://pvl.cs.princeton.edu
- **Proxima** (1) — 独立游戏工作室. 《Suck Up!》背后的小型工作室；在这款喜剧游戏里，玩家要说服由 AI 驱动的镇民让吸血鬼进门。 https://www.playsuckup.com/
- **Qi Wu** (1) — NVIDIA 研究者. NVIDIA 研究者，3DGUT（CVPR 2025）第一作者。
- **Qian Wang** (1) — 全景视频生成研究者. 北京大学深圳研究生院研究者，360DVD 第一作者。
- **Qirui Wu** (1) — 西蒙菲莎大学博士研究者，英伟达实习生. 西蒙菲莎大学研究者（与 Angel X. Chang 合作），与英伟达学习与感知研究组合作完成的 GATOR 第一作者。 https://research.nvidia.com/labs/lpr/gator/
- **Rafail Fridman** (1) — 魏茨曼科学研究所研究者（Tali Dekel 课题组）. SceneScape（NeurIPS 2023）的第一作者，该工作以统一网格实现文本驱动的无限场景生成。 https://scenescape.github.io/
- **Raina Cao** (1) — 不列颠哥伦比亚大学人机交互研究者. 与 Mirjana Prpa、Alexandra Kitson 合作研究社交 VR 中大语言模型智能体的对话时序；《Quantifying Latencies》（CHI 2026）的第一作者。
- **Rajmund Nagy** (1) — 瑞典皇家理工学院博士研究者. 在瑞典皇家理工学院与 Gustav Eje Henter 合作研究手势生成，GENEA Challenge 2026 报告的第一作者。 https://genea-workshop.github.io/2026/challenge/
- **Ramon Oliva** (1) — 巴塞罗那大学 EventLab 研究员. 与 Mel Slater 团队开发 VR 系统并开展社交 VR 研究，包括 2026 年关于会议小组讨论中化身互换与大语言模型驱动的艾伦·图灵的研究。
- **Rashawn Ray** (1) — 马里兰大学社会学家；应用社会科学研究实验室（LASSR）执行主任. 研究种族、警务与不平等；其实验室用 VR 模拟让在职警察参与，研究内隐偏见与冲突降级。
- **Remy Sabathier** (1) — Meta 与伦敦大学学院研究者. ActionMesh（CVPR 2026）的第一作者，这是 Meta 的开源模型，可将视频、图像或文字变成动画三维网格。 https://remysabathier.github.io/
- **Replicate** (1) — 模型托管平台（并入 Cloudflare）. 以带版本号的 HTTP 接口运行开源与闭源模型，Cog 容器格式的创建者。 https://replicate.com
- **RhOS.ai** (1) — AI 公司，多智能体世界模型 Khora 的联合开发方. 与 Ophilus.AI 联合开发多智能体世界模型 Khora，于 2026 年 8 月发布技术报告与在线演示。 https://rhos.ai/research/khora
- **Ritik Vatsal** (1) — 不列颠哥伦比亚大学计算机科学系研究者. 在不列颠哥伦比亚大学与 Robert Xiao 合作研究 VR 交互，Look2React（IEEE TVCG 2026）第一作者。
- **Roberto Coviello** (1) — XR 与 AI 工程师；QuestCameraKit 作者. 维护 QuestCameraKit：基于 Meta Quest 透视摄像头 API 的开源示例集。 https://xrdevrob.com
- **Robin S. Rosenberg** (1) — 临床心理学家；斯坦福虚拟人交互实验室的合作者. 研究“超级英雄心理学”的心理学家，2013 年斯坦福虚拟人交互实验室“在 VR 中像超级英雄一样飞行”研究的第一作者。
- **Ruijie Zhu** (1) — 新加坡南洋理工大学博士研究者（腾讯 ARC Lab 实习）. MotionCrafter（CVPR 2026 Highlight）第一作者，该方法用 4D VAE 从单目视频重建 4D 几何与场景流。
- **Ruili Feng** (1) — 阿里通义实验室研究者，The Matrix 第一作者. The Matrix（2024）的第一作者；该世界模拟器由阿里通义实验室与香港大学、滑铁卢大学和 Vector Institute 合作完成。
- **Ruiqi Gao** (1) — Google DeepMind 研究科学家. Google DeepMind 的生成模型研究者，CAT3D 与 CAT4D 的共同第一作者。
- **Rundi Wu** (1) — 哥伦比亚大学 / Google DeepMind 博士研究者. CAT4D（CVPR 2025）第一作者，在 Google DeepMind 完成。
- **Runjia Li** (1) — 牛津大学 VGG 博士研究者，VMem 第一作者. VMem（ICCV 2025 Highlight）的第一作者；该工作与 Philip Torr、Andrea Vedaldi、Tomas Jakab 合作，提出以面元为索引的视图记忆，使交互式场景视频保持一致。
- **Ruoshi Liu** (1) — 哥伦比亚大学博士研究者. 哥伦比亚大学研究者（Carl Vondrick 实验室，与丰田研究院合作），Zero-1-to-3 第一作者。 https://ruoshiliu.github.io/
- **Ruoyu Wen** (1) — 坎特伯雷大学人机交互研究者. 与 Thammathip Piumsomboon、Mark Billinghurst 合作研究用于情绪支持的生成式 AI 与 VR；OasisMind（IUI 2026）的第一作者。
- **Ryan Po** (1) — 斯坦福大学博士研究者，《长上下文状态空间视频世界模型》第一作者. 《长上下文状态空间视频世界模型》（2025）的第一作者，合作者来自斯坦福大学、普林斯顿大学与 Adobe Research。
- **Ryu Furusawa** (1) — 影像艺术家. Ryu Furusawa 是日本影像艺术家，擅长在时间与空间上重组拍摄的影像。 https://ryufurusawa.com
- **Ryutaro Kurai** (1) — Cluster 公司研究者（Cluster Metaverse Lab）. 日本社交 VR 平台 Cluster 的研究者，为平台用户开发基于大语言模型的创作工具。
- **SHOTPROS** (1) — 欧盟“地平线 2020”VR 警务训练研究项目（2019–2022）. 由警务机构、大学与企业组成的联合体，研究压力下的决策与行动，并构建了一套 VR 训练框架。 https://shotpros.eu/
- **Sand AI** (1) — 视频生成初创公司. 2025 年 4 月开源了 240 亿参数的自回归视频模型 MAGI-1。 https://sand.ai
- **Sandra C. Sandoval** (1) — 马里兰大学研究者. 研究语言、因果推断与警务；2026 年一项分析警察在 VR 模拟中如何与虚拟角色对话的研究的第一作者。
- **Sarah Roßkopf** (1) — 雷根斯堡大学心理学家（临床心理学与心理治疗）. 在 Andreas Mühlberger 的研究组中，研究虚拟版特里尔社会应激测试中的社会应激、临场感与声音真实感。
- **Seedleap.ai** (1) — 推出 Zing 世界模型及其 Loopit 网页应用的 AI 公司. 2026 年 9 月发布开源权重的实时世界模型 Zing-0.5，支持键盘与文字联合控制，并提供基于 SGLang 的服务部署方案以及网页应用 zing.loopit.me。 https://zing.loopit.me/
- **Sensen Gao** (1) — 南洋理工大学研究者. PixWorld（2026）的共同第一作者，该工作由南洋理工大学与 PixVerse 背后的爱诗科技合作完成。 https://sensengao.github.io/PixWorld/
- **Seung Wook Kim** (1) — 英伟达研究员，GameGAN 第一作者. 英伟达多伦多 AI 实验室研究员，研究游戏与驾驶的神经模拟。
- **Shenghai Yuan** (1) — 实时视频生成研究者. 北京大学研究者（袁粒课题组，与字节跳动合作），Helios 第一作者。
- **Shengjun Zhang** (1) — 清华大学研究者. 与张章共同担任 MBench 第一作者，来自清华大学段岳圻课题组，并与腾讯微信视觉团队合作。
- **Shenhan Qian** (1) — 慕尼黑工业大学博士研究者. Shenhan Qian 在慕尼黑工业大学 Matthias Niessner 组，是 GaussianAvatars（CVPR 2024）的第一作者。 https://shenhanqian.github.io
- **Sherry Yang** (1) — 研究者，UniSim 第一作者. 研究者（发表 UniSim 时任职于 Google DeepMind 与加州大学伯克利分校），研究把视频模型用作真实世界模拟器。
- **Sherwin Bahmani** (1) — 多伦多大学博士研究者. 4D-fy 的第一作者，这是 2023—2024 年被引用最多的文本到 4D 方法之一。 https://sherwinbahmani.github.io/
- **Shijie Zhou** (1) — 加州大学洛杉矶分校研究者. 加州大学洛杉矶分校 Achuta Kadambi 实验室的博士研究者，DreamScene360 的第一作者。
- **Shiqian Li** (1) — 北京大学与腾讯混元研究者. Shiqian Li是 4DStreamCtrl（2026）的第一作者。该工作来自北京大学与腾讯混元，是一个可用三维方式控制镜头和物体的流式视频生成器。 https://4dstreamctrl.github.io/
- **Shitao Tang** (1) — 西蒙菲莎大学研究者. 西蒙菲莎大学 Yasutaka Furukawa 组的博士研究者，MVDiffusion 的第一作者。
- **Shuai Yang** (1) — 长视频生成研究者. 就职于 NVIDIA 与香港科技大学（广州）的研究者，LongLive 第一作者。
- **Shuai Yang** (1) — 上海交通大学与上海人工智能实验室研究者. LayerPano3D（SIGGRAPH 2025）的第一作者，合作者来自香港中文大学、斯坦福与南洋理工。
- **Shunsuke Saito** (1) — Meta Codec Avatars 实验室研究科学家. Shunsuke Saito 在 Meta 主导高斯 Codec Avatars 研究，包括可重光照高斯 Codec Avatars（CVPR 2024）和大规模 Codec Avatars（CVPR 2026）。 https://shunsukesaito.github.io
- **Shuzhe Wang** (1) — 阿尔托大学 / NAVER LABS Europe 研究者. DUSt3R（CVPR 2024）第一作者，该工作在 NAVER LABS Europe 完成。
- **Siddharth Ahuja** (1) — BlenderMCP 开发者. 独立开发者，发布了开源的 BlenderMCP：连接语言模型与 Blender 的 Model Context Protocol 桥接工具。
- **Sijie Zhao** (1) — 立体视频生成研究者. 腾讯研究者，StereoCrafter 共同第一作者。
- **Simile** (1) — 人类行为模拟公司. 由 Joon Sung Park、Michael Bernstein 与 Percy Liang 创办，把生成式智能体研究做成对客户与人群的模拟。2026 年 2 月公开亮相。 https://www.simile.com/
- **Sixiao Zheng** (1) — 可控视频世界模型研究者. 复旦大学研究者，与腾讯 ARC 实验室合作的 VerseCrafter（CVPR 2026）第一作者。 https://sixiaozheng.github.io/VerseCrafter_page/
- **Siyin Wang** (1) — 清华大学博士研究者. Siyin Wang 是清华大学张超团队的博士研究者，ELLSA 2（2026）的第一作者。该模型与字节跳动合作，基于 SALMONN-omni 系列构建，是一个同时生成手势和面部表情的全双工对话模型。
- **Sofia Adelaide Osimo** (1) — 虚拟具身研究者（巴塞罗那大学 EventLab）. 2015 年“自我咨询”研究的第一作者：参与者在自己的身体与西格蒙德·弗洛伊德的身体之间切换。
- **Sofia Seinfeld** (1) — 虚拟具身研究者（巴塞罗那大学 EventLab）. 让家暴罪犯“进入”受害者身体的那项研究的第一作者。
- **Solène Neyret** (1) — 巴塞罗那大学 EventLab 研究员. 研究 VR 中的具身换位思考如何改变从众行为与群体中的伤害行为。
- **Sony Group** (1) — 电子与娱乐集团（Sony AI、Creative AI Lab）. 索尼的 Creative AI Lab 研究生成式音频，包括音效生成和 SpecMaskFoley 等视频生成音频模型。 https://www.sony.com
- **Soul AI Lab** (1) — 社交应用 Soul 的 AI 实验室. Soul AI Lab 是社交平台 Soul 的研究部门，开源了 14B 实时流式虚拟人模型 SoulX-FlashTalk。
- **Sruti Srinidhi** (1) — 卡内基梅隆大学 WiSE 实验室博士研究者. 在卡内基梅隆大学与 Anthony Rowe 合作研究 XR 系统，GenAssist（IEEE VR 2026）第一作者。 https://wise.ece.cmu.edu/
- **Stanislaw Szymanowicz** (1) — 牛津大学视觉几何组研究者. 牛津大学视觉几何组的博士研究者（Splatter Image、Flash3D），与 Google 合作完成 Bolt3D 并任第一作者。 https://szymanowiczs.github.io
- **Stanley J. Hamstra** (1) — 医学教育研究者（渥太华大学；美国毕业后医学教育认证委员会）. 研究基于模拟的训练，2014 年重新审视模拟“保真度”一文的第一作者。
- **Strivr** (1) — 沉浸式培训公司. 2015 年从斯坦福 VHIL 衍生，先用 360° VR 训练运动员，后把 VR 培训推广到沃尔玛等企业；截至 2026 年主推基于智能眼镜的 AI 质检。 https://www.strivr.com/
- **Studio Atelico** (1) — 面向游戏的本地端 AI 引擎开发商. 由来自 Uber、Meta、世嘉与 Creative Assembly 的 AI 与游戏从业者创办的工作室，开发让角色在玩家自己的 GPU 上运行的 Atelico AI 引擎。 https://atelico.studio
- **Suibi Che-Chuan Weng** (1) — 科罗拉多大学博尔德分校 ATLAS 研究所人机交互研究者. 研究创意混合现实与生成式 AI，Editing Reality（DIS 2026）第一作者。
- **Sungnyun Kim** (1) — 韩国科学技术院（KAIST）金在哲人工智能研究生院博士研究者. 在 KAIST AI 与 Se-Young Yun 合作研究语音与对话模型，DyaFDB（2026）第一作者。
- **Sylvia Xueni Pan** (1) — 伦敦大学金史密斯学院虚拟社会互动研究者. 研究人与虚拟角色的社会互动，与 Antonia Hamilton 合写了用 VR 研究社会互动的经典综述。
- **Synthesia** (1) — 企业级 AI 视频与虚拟人平台. Synthesia 为企业培训和内部沟通制作 AI 虚拟人视频，2026 年加入实时交互虚拟人和用于角色扮演与访谈的 Sessions 平台。 https://www.synthesia.io
- **Taekyung Ki** (1) — 韩国科学技术院（KAIST）博士研究者. Taekyung Ki 是 Avatar Forcing（CVPR 2026）的第一作者，该模型是能对用户声音与动作作出反应的实时交互头部虚拟人。 https://taekyungki.github.io
- **Talespin** (1) — 沉浸式软技能培训公司，现已并入 Cornerstone. 开发带虚拟人的 VR 软技能模拟和无代码创作工具 CoPilot Designer；talespin.com 现已跳转至 Cornerstone 的沉浸式学习平台。 https://www.cornerstoneondemand.com/platform/immersive-learning/
- **Tareq Alsaleh** (1) — 多伦多都会大学交通创新实验室（LiTrans）研究者. Bilal Farooq 领导的 LiTrans 实验室的交通研究者，该实验室用 VR 与 XR 做出行行为实验。
- **The Khronos Group** (1) — 图形与空间计算标准联盟. 制定 glTF、OpenXR、Vulkan 与 WebGL 的开放行业联盟。 https://www.khronos.org
- **Thomas Müller** (1) — NVIDIA 研究者. NVIDIA 研究者，Instant Neural Graphics Primitives（instant-ngp）第一作者。
- **Tianqi Liu** (1) — 华中科技大学与南洋理工大学 S-Lab 博士研究者. Free4D（ICCV 2025）与 Light-X 的第一作者，研究借助视频模型的 4D 场景生成与渲染。
- **Tianwei Yin** (1) — 快速生成模型研究者. MIT 博士研究者，DMD 蒸馏与 CausVid 的第一作者。
- **Tianye Li** (1) — Meta Reality Labs 研究者. Neural 3D Video Synthesis（DyNeRF，CVPR 2022）第一作者，该工作在 Meta Reality Labs Research 完成。
- **Tianyi Xiao** (1) — 苏黎世联邦理工学院制图与地理信息研究所研究者. 研究空间认知、草图地图与增强现实。
- **Tianyuan Zhang** (1) — 麻省理工学院 CSAIL 博士研究者. PhysDreamer（ECCV 2024 口头报告）的第一作者，该方法让静态三维物体获得从视频模型中学到的物理响应。
- **Ting-Bing Xu** (1) — 高德地图视觉实验室（阿里巴巴）研究者. WorldRoamBench 的第一作者；该基准由高德地图视觉实验室与南京大学、清华大学、北京大学共同构建。
- **Ting-Hsuan Chen** (1) — 360° 视频生成研究者. 南加州大学研究者，与博世研究院、阳明交通大学合作的 Pantheon360（CVPR 2026）共同第一作者。 https://koi953215.github.io/pantheon360_page/
- **Tinghui Zhou** (1) — 计算机视觉研究者（加州大学伯克利分校博士）. Stereo Magnification（SIGGRAPH 2018）的第一作者，该论文提出了多平面图像表示与 RealEstate10K 数据集。 https://tinghuiz.github.io
- **Tom Craig** (1) — 伦敦国王学院社会精神病学教授. 主持 AVATAR 疗法试验：幻听者与由治疗师配音、代表其“迫害者”的化身对话。
- **Tomoki Itamiya** (1) — 爱知工科大学教授. 开发 AR 与 VR 防灾教育工具，例如叠加在真实房间与街道上的洪水和地震模拟。
- **Tong Wu** (1) — 斯坦福大学研究者. 斯坦福大学 Gordon Wetzstein 组的研究者，研究具备三维感知的视频生成。
- **Transitional Forms** (1) — 由 Pietro Gagliano 创立的 AI 娱乐工作室. 围绕实时 AI 智能体创作故事与游戏的工作室，作品从与加拿大国家电影局合作的动态电影 Agence，到多智能体故事模拟。 https://www.transforms.ai
- **Tsai-Shien Chen** (1) — 加州大学默塞德分校 / Snap Research 研究者. Panda-70M 的第一作者，该工作完成于其在 Snap Research 实习期间。
- **Tsehaye Haidemariam** (1) — 挪威 BI 商学院研究者. 研究虚拟现实、元宇宙与社会身份；2026 年“合成具身”框架（关于 AI 生成的身份线索）的第一作者。
- **Tu Anh Nguyen** (1) — 语音研究者（Meta AI / ENS–Inria）. Tu Anh Nguyen 在 Meta AI 与巴黎认知机器学习团队从事无文本口语语言建模研究。
- **Uriel Singer** (1) — Meta AI 研究科学家. Meta 研究者，Make-A-Video 与 MAV3D（文本到 4D，2023）的第一作者。
- **Uthana** (1) — AI 人体动作公司. Uthana 提供文生动作、视频转动作、自动绑定与动作重定向模型，面向游戏动画和人形机器人训练，可通过网页应用、API 以及 Blender、Maya 和 Unity AI 插件使用。 https://uthana.com/
- **Valve** (1) — 游戏公司、Steam 运营方. 运营 Steam，生产 Index、Steam Deck 与 Steam Frame 头显。 https://store.steampowered.com
- **Varjo** (1) — XR 头显与重建公司. 芬兰高分辨率 XR 头显厂商，推出了 Teleport 云服务，把手机或相机素材转换为高斯泼溅场景。 https://varjo.com/
- **Vincent Leroy** (1) — NAVER LABS Europe 研究者. NAVER LABS Europe 研究者，MASt3R（ECCV 2024）第一作者。
- **Visko** (1) — 开发实时“活模型”（Live Model）视频生成的创业公司. Visko Platform Inc. 由 Qing（Will）Yin 于 2025 年创立，发布了 Orbis：一个在用户随时修改提示词时仍持续流式生成视频的模型。公司于 2026 年 9 月 1 日宣布完成 1000 万美元种子前轮融资。 https://www.visko.ai/
- **Volcano Engine (BytePlus)** (1) — 字节跳动旗下云平台. 字节跳动的云服务与模型即服务业务，海外品牌为 BytePlus。 https://www.volcengine.com
- **Volinga** (1) — 面向虚拟制片的高斯泼溅工具公司. 从 Arquimea 研究中心分拆出来的西班牙公司，2023 年 1 月推出 Unreal Engine 的 NeRF 插件，同年转向高斯泼溅，现销售训练套件与 Unreal 渲染器。 https://volinga.ai/
- **W3C Immersive Web Working Group** (1) — 网页标准组织. 万维网联盟（W3C）中负责制定 WebXR 设备 API 及其模块的工作组。 https://www.w3.org/immersive-web/
- **Waymo** (1) — Alphabet 旗下的自动驾驶公司. Alphabet 旗下的自动驾驶公司，在多座美国城市运营无人驾驶网约车。 https://waymo.com
- **Weiwei Jiang** (1) — 南京信息工程大学研究者. 研究人机协同设计与虚拟现实的 HCI 学者，与日本、澳大利亚、丹麦和德国的合作者共同完成 CoGen3D。
- **Weixi Feng** (1) — 加州大学圣巴巴拉分校研究者. 加州大学圣巴巴拉分校王威廉组的博士研究者，LayoutGPT 的第一作者。 https://weixi-feng.github.io
- **Weiyu Li** (1) — 香港科技大学博士研究者，Meta AI 研究实习生. 香港科技大学研究者（与谭平合作），与 Meta AI 合作完成的 MeshFlow（CVPR 2026 Highlight）第一作者。 https://wyysf-98.github.io/
- **Wemade Next** (1) — 游戏开发商（Wemade 子公司）. 韩国游戏开发商，Wemade 旗下子公司，开发《传奇》（Legend of Mir）系列 MMORPG，包括 MIR4 与 MIR5。
- **Wenqiang Sun** (1) — 香港科技大学博士研究者. DimensionX 的共同第一作者，这是香港科技大学与清华大学的开源图像到三维 / 4D 场景方法。
- **XREAL** (1) — AR 眼镜公司. 中国显示眼镜厂商（原名 Nreal），与 Google 合作开发 Android XR 眼镜 XREAL AURA。 https://www.xreal.com
- **Xiangyue Zhang** (1) — 东京大学与通义实验室（阿里巴巴）研究者. StreamTalk（ECCV 2026）以及此前伴随语音手势模型 SemTalk（ICCV 2025）、EchoMask（ACM MM 2025）的第一作者，也是 FloodDiffusion 2 的合著者。 https://www.xiangyuezhang.com/
- **Xianhao Carton Liu** (1) — 明尼苏达大学 HCI 研究者. 研究增强现实中通过代理界面操作现实物体的 HCI 学者，与陈朱天（Zhu-Tian Chen）、Mar Gonzalez-Franco 合作。
- **Xiaofeng Mao** (1) — 研究者，Yume 第一作者. Yume（2025）与 Yume 1.5 的第一作者；这两个开源交互世界生成模型后来以 Alaya Lab 的名义发布。
- **Xiaoran Yang** (1) — 研究 XR 中大语言模型智能体的人机交互研究者. ISMAR 2026 一项研究的第一作者，研究 VR 中的具身对话智能体如何提示不确定性与信息来源。
- **Xindi Wu** (1) — 普林斯顿大学与英伟达研究者. 普林斯顿大学博士研究者，与英伟达合作研究视频世界模型的记忆机制。
- **Xinyang Li** (1) — 厦门大学 MAC 实验室博士研究者. FlashWorld 的第一作者，该工作与腾讯混元合作完成。
- **Xinyu Ning** (1) — 生成式 AI 与 XR 系统综述的第一作者（Lik-Hang Lee 团队）. 梳理了 2023–2025 年生成式 AI 与扩展现实结合研究的研究者。
- **Xinyu Wang** (1) — 流式视频编辑研究者. 清华大学研究者，LiveEdit（ECCV 2026）第一作者。 https://live-edit.github.io/
- **Xuanchi Ren** (1) — NVIDIA 研究科学家. NVIDIA 多伦多 AI 实验室研究者，GEN3C 的第一作者，Lyra 的合作者。 https://xuanchiren.com
- **Xudong Xu** (1) — 视听学习研究者. Xudong Xu 研究视听学习与三维感知生成；Sounding Bodies 与 Meta Reality Labs Research 合作完成。
- **Xueyang Wang** (1) — 清华大学研究者. 研究跨现实创作与空间锚定的生成，Roomify（CHI 2026）第一作者。
- **Xun Huang** (1) — 生成式视频研究者. 研究科学家（Self Forcing 发表时任职于 Adobe Research），以 AdaIN 风格迁移和实时视频扩散研究著称。
- **Yang Gao** (1) — 北京航空航天大学研究者. IEEE VR 2026 一项研究的第一作者，研究 AI 重建外观与克隆声音如何影响人们对虚拟名人智能体的信任。
- **Yang Zhou** (1) — 优酷 Orange 3DV 团队研究者，MoVerse 第一作者. MoVerse（2026）的第一作者。MoVerse 是一个从单张图像构建全景三维高斯骨架的实时世界模型，出自优酷 Moku Lab 的 Orange 3DV 团队（阿里巴巴虎鲸文娱集团）。 https://orange-3dv-team.github.io/MoVerse/
- **Yang-Tian Sun** (1) — 香港大学博士研究者. Yang-Tian Sun是 Stereo World Model（CVPR 2026）的第一作者，该工作由香港大学与 VAST、字节跳动 Pico 合作完成。 https://sunyangtian.github.io/
- **Yanni Mei** (1) — 达姆施塔特工业大学博士研究者. 研究增强现实中感知操控的 HCI 学者，与 Jan Gugenheimer、Florian Müller 合作。
- **Yanqin Jiang** (1) — 中国科学院自动化研究所博士研究者. Consistent4D 与 Animate3D 的第一作者，这两项工作分别是视频到 4D 和为现有三维模型添加动画的早期参照。
- **Yehonathan Litman** (1) — 卡内基梅隆大学博士研究者. Lift4D（SIGGRAPH Asia 2026）的第一作者，该方法把形变物体的单目视频提升为完整的 4D 高斯。
- **Yi-Hua Huang** (1) — 香港大学博士研究者. 香港大学齐晓娟课题组研究者，与 VAST 合作完成的 AniGen（SIGGRAPH 2026）第一作者。 https://yihua7.github.io/website/
- **Yichen Chai** (1) — 香港理工大学研究者. 与 Henry Been-Lirn Duh 合作研究混合现实设计工具，GenerativeSurface（IEEE TVCG 2026）第一作者。
- **Yicong Hong** (1) — Adobe 研究院研究科学家. Adobe 研究院研究员，《LRM：用于单张图像三维重建的大型重建模型》（ICLR 2024）第一作者。
- **Yifan Wang** (1) — 浙江大学研究者. 浙江大学三维视觉组研究者，FreeTimeGS（CVPR 2025）第一作者。
- **Yihang Luo** (1) — 南洋理工大学 S-Lab 博士研究者. 南洋理工大学 S-Lab 吕健勤（Chen Change Loy）课题组研究者，4RC（ICML 2026）第一作者。 https://yihangluo.com/
- **Yiliu Tang** (1) — 伊利诺伊大学厄巴纳-香槟分校信息科学学院研究者. 与 Yun Huang 合作研究 XR 中的生成式 AI，《Empowered XR through Generative AI》（CHI 2026）第一作者。
- **Yiyi Cai** (1) — ShandaAI 东京研究院研究者. FloodDiffusion（CVPR 2026）与 FloodDiffusion 2（2026）的第一作者，两者都是 ShandaAI 东京研究院与东京大学的流式文本生成动作模型；第二版通过 Alaya Lab 的 GitHub 与 Hugging Face 账号发布。
- **Yongzhen Hu** (1) — 浙江大学三维视觉组研究者. InfiniSplat v2（2026）共同第一作者，这是一个可接受任意数量输入视角的前馈式高斯重建模型。
- **Yoojin Han** (1) — 延世大学建筑与环境心理学研究者. 利用沉浸式 360° 刺激研究绿植等室内空间特征如何影响人；主持了 2026 年一项把生成式 AI 全景用作实验刺激的验证研究。
- **You-Zhe Xie** (1) — 阳明交通大学与 Alaya Lab 研究者. OuroWorld（2026）的第一作者，该方法把静态三维高斯世界变成循环播放的三维动态照片。 https://www.youzhexie.me/
- **Yu Han** (1) — Meta Reality Labs 研究者. Yu Han 是 FaceGAN（《No Distillation Needed》，2026）的第一作者。该工作来自 Meta Reality Labs，是一个单次前向的实时说话头像模型，合作者包括 Alexander Richard、Wojciech Zielonka 和 Michael Zollhoefer。 https://wojciechzielonka.com/facegan/
- **Yu Zhang** (1) — 华东师范大学研究者. Yu Zhang 是 EmbodiedHead（ECCV 2026）的第一作者。该工作来自华东师范大学计算机科学与技术学院，为大模型智能体提供可实时倾听和说话的头部虚拟人。 https://vpx-ecnu.github.io/EmbodiedHead-Website/
- **Yudong Jin** (1) — 浙江大学与蚂蚁灵波科技博士研究者. 4DAnyone（SIGGRAPH Asia 2026）的共同第一作者，该方法把一段随手拍的人物视频变成 4D 高斯人体。
- **Yue Yang** (1) — 宾夕法尼亚大学研究者. 宾夕法尼亚大学的博士研究者，与艾伦人工智能研究所合作主导了 Holodeck。 https://yueyang1996.github.io
- **Yupei Duan** (1) — 密苏里大学学习技术研究者. 为护理教育设计沉浸式 VR 环境；2026 年一项关于生成式 AI 虚拟标准化病人的 AIxVR 研究的第一作者。
- **Yuting Wen** (1) — 口腔医学教育研究者. 2026 年一项随机试验的第一作者，比较了 VR 牙科技能训练中 ChatGPT 指导与教师现场指导的效果。
- **Yuwei Guo** (1) — 视频生成研究者. 香港中文大学研究者，AnimateDiff（ICLR 2024）第一作者。
- **Yuxue Yang** (1) — 中国科学院自动化研究所与 CreateAI 博士研究者. NeoVerse（CVPR 2026 Highlight）的第一作者，这是一个在真实单目视频上训练的 4D 世界模型。
- **Yuyang Zhao** (1) — 新加坡国立大学研究者. 新加坡国立大学 Gim Hee Lee 课题组研究者，与微软合作完成的 GenXD（ICLR 2025）第一作者。
- **Yvain Tisserand** (1) — 日内瓦大学瑞士情感科学中心研究者. 为 VR 训练与情感研究构建虚拟人；2026 年一项研究的第一作者，该研究用日内瓦警察测试了一个基于规则的虚拟嫌疑人。
- **Zehao Yu** (1) — 图宾根大学研究者. Andreas Geiger 团队的博士研究者，Mip-Splatting 第一作者。
- **Zehuan Huang** (1) — 北京航空航天大学博士研究者. 北京航空航天大学软件学院 Lu Sheng 课题组研究者，与 VAST 合作完成的 AnimaX（2025）第一作者。
- **Zeqi Xiao** (1) — 研究者，WorldMem 第一作者. 南洋理工大学 S-Lab 研究者，研究一致的视频世界模拟。 https://xizaoqu.github.io
- **Zhan Li** (1) — 波特兰州立大学 / OPPO 美国研究院研究者. Spacetime Gaussian Feature Splatting（CVPR 2024）第一作者。
- **Zhan Xu** (1) — 研究者（马萨诸塞大学阿默斯特分校，后加入 Adobe）. RigNet（SIGGRAPH 2020）第一作者，该工作完成于马萨诸塞大学阿默斯特分校 Evangelos Kalogerakis 团队。 https://zhan-xu.github.io/
- **Zhen Xu** (1) — 浙江大学研究者. 浙江大学三维视觉组研究者，EasyVolcap 的作者，《Representing Long Volumetric Video with Temporal Gaussian Hierarchy》（SIGGRAPH Asia 2024）第一作者。
- **Zhengqi Li** (1) — Google DeepMind 研究科学家. 研究动态场景重建的 Google 研究者，MegaSaM（CVPR 2025）第一作者。
- **Zhibing Li** (1) — 香港中文大学博士研究者. 香港中文大学林达华课题组研究者，与上海人工智能实验室合作完成的 SS4D（SIGGRAPH Asia 2025）共同第一作者。 https://lizb6626.github.io/
- **Zhifei Chen** (1) — 香港科技大学（广州）研究者，ReWorld 第一作者. ReWorld（2026）的第一作者。ReWorld 是香港科技大学（广州）与阿里巴巴 ATH 事业群合作开发的实时交互世界模型，具备长时记忆。 https://zhifeichen097.github.io/ReWorld/
- **Zhipu AI** (1) — 源自清华大学的大模型公司. GLM 语言模型及开源 CogVideoX 视频模型（“清影”产品底座）的开发者。 https://www.zhipuai.cn
- **Zhiyang Deng** (1) — 人工智能研究者（腾讯、新加坡国立大学）. 新加坡国立大学研究者；WorldMind（2026）的共同第一作者，该工作完成于腾讯研究实习期间。
- **Zhiyang Guo** (1) — 中国科学技术大学博士研究者. Make-It-Animatable（CVPR 2025）第一作者，可在一秒内为人形网格和高斯泼溅完成绑定。 https://jasongzy.github.io/
- **Zhuangze Hou** (1) — 香港城市大学创意媒体学院研究者. 研究虚拟现实中由 AI 辅助的空间设计，EchoLadder（UIST 2025）第一作者。
- **Zhuo Ning** (1) — 西蒙弗雷泽大学研究者. Zhuo Ning 是 Soundwich（2026）的第一作者。该工作在西蒙弗雷泽大学完成，合作者包括 Ali Mahdavi-Amiri、Daniel Cohen-Or 以及特拉维夫大学和 CYENS 的研究者。 https://soundwich.avdemo.workers.dev/
- **Ziang Cao** (1) — 南洋理工大学（S-Lab）博士研究者. 南洋理工大学刘子纬课题组研究者，PhysX 系列物理三维生成工作的第一作者，包括 PhysX-Anything（CVPR 2026）和 PhysX-Omni。 https://physx-omni.github.io/
- **Zikai Liao** (1) — 石溪大学研究者. Zikai Liao 是 GLARE（NeurIPS 2026）的第一作者。该工作来自石溪大学与 Atmanity Inc.，提供倾听头像的数据集与模型。
- **Zitong Lan** (1) — 声学与空间音频研究者（宾夕法尼亚大学）. Zitong Lan 在宾夕法尼亚大学 Mingmin Zhao 课题组研究声学仿真与空间音频。
- **Ziyang Ye** (1) — 香港中文大学（深圳）研究者，WorldCast 第一作者. WorldCast（2026）的第一作者。WorldCast 是面向《反恐精英 2》的分布式多人世界模型，合作者来自香港中文大学（深圳）、SLAI、清华大学深圳国际研究生院、滴滴 Voyager Research 与中国科学技术大学。 https://ziyang-ye.github.io/WorldCast-Page/
- **Ziyi Liu** (1) — 普渡大学博士研究者. Ziyi Liu 是普渡大学的博士研究者，AgentHands（CHI 2026）的第一作者。该工作与 Google XR 合作完成，为 XR 对话智能体配上一双与语音同步、指向真实物体的手。 https://research.google/blog/agenthands-generating-interactive-hand-gestures-for-spatially-grounded-agent-conversations-in-xr/
- **Ziyi Wu** (1) — 生成式三维与视频研究者. 多伦多大学博士研究者；360Anything 第一作者，该工作在 Google DeepMind 完成。
- **Zizhang Li** (1) — 斯坦福大学博士研究者. 吴佳俊组 WonderPlay（ICCV 2025 Highlight）的共同第一作者。
- **bilibili** (1) — 中国视频平台（Index 团队）. 哔哩哔哩是中国视频社区，其 Index 团队开发开源的 IndexTTS 语音模型。 https://www.bilibili.com
- **fal** (1) — 生成式媒体推理平台. 通过一个 API 托管 1,000 多个图像、视频、音频与三维模型，并提供 Serverless GPU。 https://fal.ai
