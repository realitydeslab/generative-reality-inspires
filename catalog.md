# Generative Reality Inspire — catalog

A catalog of generative immersive technology: the models, products, APIs, research demos, studies and devices with which situations can be generated and entered. Fields: video generation, interactive virtual humans, speech and spatial audio, interactive world models, 3D scene and world generation, 3D assets and motion, capture / reconstruction / 4D, agents and simulated societies, generative XR experiences, immersive behavioral research and training, and platforms / APIs / delivery. Each entry lists its idea, how it works, its input, output, timing (pre-generated, turn-based, real-time, full-duplex, scripted) and access (open weights, API, product, waitlist, research), and links to its video, paper and official page. Compiled by Reality Design Lab as the living survey behind a research agenda on generative immersion for behavioral science. Capabilities are as reported by their developers.

https://generative.reality.design · 2026-10-17 · 318 labs & creators · 508 entries

## How an AI assistant should use this file

- Ground ideas in the specific entries below and name the entry and creator you draw on.
- Cite papers with the DOI / arXiv / URL given here; do not invent references.
- Combine inputs, outputs, timing and access across entries to propose systems and studies.
- Treat capabilities as developer-reported and check the official page; do not invent details not stated here.

## Video Generation

Models that synthesise audiovisual events from text, images and references. The fastest route to scenario material, but a clip is watched, not acted in.

### Frontier text- & image-to-video

Closed flagship models (Sora, Veo, Kling, Runway, Luma, Hailuo, Seedance…), many now with native audio.

#### Kling 4.0 — Kuaishou (2026-09-28)
- Type: Model · Timing: Pre-generated · Access: Product / app
- Input: Text prompt, Image, Video → Output: Flat video, Speech / voice, Sound, music & spatial audio
- Idea: Thirty-second takes can hold a whole short interaction (approach, exchange, reaction) in one continuous shot.
- What it is: Kling 4.0, introduced on 2026-09-28 (a Flash version went first to top-tier subscribers), extends single generations to about 30 seconds with keyframe control and stereo sound; broader rollout was reported for 2026-10-16, and it is live on kling.ai as of mid-October 2026.
- How it works: Next Kling generation; reported to accept up to 10 keyframe images per clip and to output up to 4K; architecture not published.
- Specs: ~30 s per generation · up to 10 keyframes · up to 4K (reported)
- Capability: Persistence, Experimental control, Perceptual realism
- Video: https://www.youtube.com/watch?v=nlM7kL3kv_Y
- Project page: https://kling.ai/

#### Wan 3.0 — Alibaba Tongyi (Qwen) (2026-08-06)
- Type: Model · Timing: Pre-generated · Access: Waitlist / early access, Public API
- Input: Text prompt, Image, Video → Output: Flat video, Speech / voice, Sound, music & spatial audio
- Idea: Even the leading open-weight video lab now keeps its newest flagship closed, so open Wan models trail by a generation.
- What it is: Wan 3.0 entered public beta on Alibaba Cloud on 2026-08-06; unlike the open Wan 2.1 and 2.2 it is closed and API-only, and it takes text, image, video and audio in one prompt. Wan 2.5 (2025-09) and Wan 2.6 (2025-12) had already added native audio and reference casting.
- How it works: Multimodal audio-video generation model served through Alibaba Cloud Model Studio; architecture and weights not published as of October 2026.
- Specs: up to 30 s · 1080p (reported)
- Capability: Persistence, Authoring accessibility, Experimental control
- Video: https://www.youtube.com/watch?v=dC5pu8zL2p8
- Images: https://img.alicdn.com/imgextra/i1/O1CN01WlNesT1EWvfm8mzKw_!!6000000000360-2-tps-600-315.png
- Project page: https://wan.video/
- API docs: https://www.alibabacloud.com/help/en/model-studio/

#### Gemini Omni — Google DeepMind (2026-05-19)
- Type: Model · Timing: Pre-generated · Access: Product / app, Public API
- Input: Text prompt, Image, Video → Output: Flat video, Speech / voice, Sound, music & spatial audio
- Idea: Generation and editing merge into one conversation, so a scenario can be revised shot by shot ('make the bystander turn around') instead of re-rolled.
- What it is: Google's successor to the Veo line, announced at I/O on 2026-05-19. Its first model, Gemini Omni Flash, takes any mix of text, images, audio and video and generates or conversationally edits video with sound in the Gemini app, Flow, YouTube Shorts and Google Vids; in the Gemini API it entered preview on 2026-06-30 and became generally available as gemini-omni-1.1-flash on 2026-08-27.
- How it works: Natively multimodal Gemini-family generator that accepts up to three seconds of reference video plus images and audio; DeepMind reports leading human-rater preference for editing and for text-, image- and reference-to-video.
- Specs: 360p / 720p · 1080p and 4K via upscaling · up to 3 s video reference · API GA 2026-08-27
- Capability: Experimental control, Co-creation & agency, Authoring accessibility
- Video: https://www.youtube.com/watch?v=KUyRq7szZsM
- Project page: https://deepmind.google/models/gemini-omni/
- API docs: https://ai.google.dev/gemini-api/docs/video

#### Seedance 2.0 — ByteDance Seed (2026-02-12)
- Type: Model · Timing: Pre-generated · Access: Product / app, Public API
- Input: Text prompt, Image, Video → Output: Flat video, Speech / voice, Sound, music & spatial audio
- Idea: Audio, motion and camera references in one prompt give director-level control, and also make consent for likeness a design requirement.
- What it is: Seedance 2.0 (public release in ByteDance's Jimeng and Doubao apps on 2026-02-12; global via BytePlus in April) generates audio and video jointly from any mix of text, image, audio and video references. Press reports say ByteDance paused real-person reference uploads soon after launch; Seedance 2.5 (2026-07-30) extends single generations to 30 seconds.
- How it works: Unified multimodal audio-video joint generation architecture accepting text, image, audio and video inputs (per the Seedance 2.0 technical report).
- Specs: 4–15 s · joint audio-video · Seedance 2.5: up to 30 s
- Capability: Perceptual realism, Experimental control, Situational reach
- Paper: https://arxiv.org/abs/2604.14148 (arXiv 2026)
- Video: https://www.youtube.com/watch?v=l89woJ0jidw
- Project page: https://seed.bytedance.com/en/seedance2_0

#### Kling 3.0 — Kuaishou (2026-02-04)
- Type: Model · Timing: Pre-generated · Access: Product / app, Public API
- Input: Text prompt, Image, Video → Output: Flat video, Speech / voice, Sound, music & spatial audio
- Idea: Directing who speaks and when makes short multi-character dialogue scenes feasible as stimulus material.
- What it is: Kling 3.0 (2026-02-04) generates multi-shot sequences of up to 15 seconds with native audio and multilingual, lip-synced dialogue in which users assign who speaks; 'Omni' variants take reference videos and images to keep characters consistent.
- How it works: Successor of the Kling-Omni architecture with joint audio-visual generation and storyboard-style multi-shot planning (per Kuaishou's press release).
- Specs: up to 15 s · multi-shot · speech in EN / ZH / JA / KO / ES
- Capability: Behavioral plausibility, Authoring accessibility, Perceptual realism
- Video: https://www.youtube.com/watch?v=XD_7FNPhZQY
- Project page: https://kling.ai/
- API docs: https://app.klingai.com/global/dev

#### Vidu Q3 — Shengshu Technology (Vidu) (2026-02-02)
- Type: Model · Timing: Pre-generated · Access: Product / app, Public API
- Input: Text prompt, Image → Output: Flat video, Speech / voice, Sound, music & spatial audio
- Idea: Shows how fast Chinese labs iterate: four major Vidu generations in under two years, each adding reference and audio features.
- What it is: Vidu Q3 (early February 2026) is Shengshu Technology's audio-visual model, generating clips with synchronized speech and sound and strong reference-to-video consistency. Shengshu launched the Vidu line with Tsinghua University in April 2024 as China's first Sora-class model; Vidu Q4 was in preview in October 2026.
- How it works: U-ViT diffusion transformer (Tsinghua's architecture) extended to joint audio-visual generation; Q3 details not published.
- Capability: Authoring accessibility, Persistence
- Video: https://www.youtube.com/watch?v=QQloL2IW8kA
- Project page: https://www.vidu.com/
- API docs: https://platform.vidu.com/

#### Gen-4.5 — Runway (2025-12-01)
- Type: Model · Timing: Pre-generated · Access: Product / app, Public API
- Input: Text prompt, Image → Output: Flat video
- Idea: The physical plausibility of bodies and objects, more than resolution, became the axis frontier models compete on.
- What it is: Gen-4.5 (2025-12-01) improves motion quality, physical weight and prompt adherence; Runway reported it ranked first on the Artificial Analysis text-to-video benchmark at launch with 1,247 Elo. Image-to-video followed in early 2026.
- How it works: Runway's next-generation video diffusion model, trained on NVIDIA Hopper and Blackwell GPUs; details not published.
- Specs: #1 Artificial Analysis T2V at launch · 1,247 Elo (Runway claim)
- Capability: Behavioral plausibility, Perceptual realism
- Video: https://www.youtube.com/watch?v=ei2PsDpPbB4
- Images: https://d3phaj0sisr2ct.cloudfront.net/site/images/research/gen/launch-post/card-gen-4.5.png
- Project page: https://runwayml.com/research/introducing-runway-gen-4.5
- API docs: https://docs.dev.runwayml.com/

#### Veo 3.1 — Google DeepMind (2025-10-15)
- Type: Model · Timing: Pre-generated · Access: Public API, Product / app
- Input: Text prompt, Image → Output: Flat video, Speech / voice, Sound, music & spatial audio
- Idea: Reference images and first/last frames let a researcher hold a character and setting fixed across clips, a first step toward controlled stimulus sets.
- What it is: Veo 3.1 (2025-10-15) adds richer native audio and stronger prompt adherence to Veo 3, plus 'ingredients to video' (reference images), first-and-last-frame transitions and scene extension to a minute or more, in Flow and the Gemini API.
- How it works: Veo 3 successor with reference conditioning, first/last-frame interpolation and extension that continues each new clip from the final second of the previous one.
- Specs: 8 s per clip · extend to 60 s+ · 720p / 1080p · native audio
- Capability: Experimental control, Perceptual realism, Authoring accessibility
- Video: https://www.youtube.com/watch?v=I06Ef8alr2Y
- Images: https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Veo3.1_Social_v3.width-1300.png
- Project page: https://blog.google/innovation-and-ai/products/veo-updates-flow/
- API docs: https://ai.google.dev/gemini-api/docs/video

#### Sora 2 — OpenAI (2025-09-30)
- Type: Model · Timing: Pre-generated · Access: Research only
- Input: Text prompt, Image, Video → Output: Flat video, Speech / voice, Sound, music & spatial audio
- Idea: Consented likeness insertion turned a video model into a social medium; its withdrawal within months is a warning for any study that needs a stable model version.
- What it is: OpenAI's second video model, launched on 2025-09-30 with a social iOS app; it generates clips with synchronized dialogue and sound effects and can insert 'cameos' of verified users. The app closed on 2026-04-26 and the API on 2026-09-24.
- How it works: Joint video-and-audio generation; OpenAI reports better physical plausibility (a missed shot rebounds instead of teleporting into the hoop) and multi-shot instruction following; architecture not published.
- Specs: synchronized audio · cameos · app 2025-09-30 → closed 2026-04-26
- Capability: Perceptual realism, Behavioral plausibility, Co-creation & agency
- Video: https://www.youtube.com/watch?v=lEcg6AJ6DVY
- Images: https://images.ctfassets.net/kftzwdyauwt9/1Q8NDmnyavsoPAKDlWpW18/a1f595376097668d1772c9cac40fc8ee/16_x_9____1_.png?w=1600&h=900&fit=fill
- Project page: https://openai.com/index/sora-2/

#### Ray3 — Luma AI (2025-09-18)
- Type: Model · Timing: Pre-generated · Access: Product / app, Public API
- Input: Text prompt, Image, Video → Output: Flat video
- Idea: A model that critiques its own drafts hints at generation loops that check a scene against a specification before anyone sees it.
- What it is: Ray3 (2025-09-18) is Luma's 'reasoning' video model, which judges and revises its own drafts and can export 16-bit HDR for studio pipelines; Ray3.14 (2026-01-26) moved to native 1080p and Ray3.2 (2026-06-09) added up to 16 keyframes per clip.
- How it works: Video diffusion model with a multimodal reasoning stage that plans and evaluates generations, trained for HDR output (per Luma).
- Specs: 16-bit HDR · draft mode · Ray3.2: up to 16 keyframes
- Capability: Perceptual realism, Experimental control
- Video: https://www.youtube.com/watch?v=z2UIcD2xvsA
- Images: https://cdn.sanity.io/images/2ylxvaa2/production/3f83440c074f2a5e161d1975975cafeb73a81a78-1920x1080.png?rect=0,36,1920,1008&w=1200&h=630&fm=jpg
- Project page: https://lumalabs.ai/ray
- API docs: https://docs.lumalabs.ai/

#### Marey — Moonvalley (2025-07-08)
- Type: Model · Timing: Pre-generated · Access: Product / app
- Input: Text prompt, Image, Video → Output: Flat video
- Idea: Licensed-only training data answers the provenance question institutions face before they can use generated footage.
- What it is: Moonvalley's Marey (public launch July 2025) is trained only on licensed footage and built for filmmakers, with camera, motion and pose controls such as camera-path re-direction and pose transfer.
- How it works: Video diffusion model trained on commercially licensed video and co-developed with the animation studio Asteria (per Moonvalley).
- Specs: 1080p · 24 fps
- Capability: Experimental control, Authoring accessibility
- Video: https://www.youtube.com/watch?v=YbhQnzYAIjM
- Project page: https://www.moonvalley.com/

#### Hailuo 02 — MiniMax (2025-06-18)
- Type: Model · Timing: Pre-generated · Access: Product / app, Public API
- Input: Text prompt, Image → Output: Flat video
- Idea: Credible full-body motion is a prerequisite for scenes in which bodily behavior is the stimulus.
- What it is: MiniMax's Hailuo 02 (2025-06-18) generates native 1080p clips and became known for complex full-body motion such as gymnastics and acrobatics.
- How it works: Noise-aware Compute Redistribution (NCR) architecture that MiniMax says makes training and inference about 2.5x more efficient, with 3x the parameters and 4x the data of Hailuo 01.
- Specs: 1080p · 6 s / 768p · 10 s
- Capability: Behavioral plausibility, Perceptual realism
- Video: https://www.youtube.com/watch?v=J18idUz87LA
- Project page: https://www.minimax.io/news/minimax-hailuo-02
- API docs: https://platform.minimax.io/docs

#### Midjourney Video V1 — Midjourney (2025-06-18)
- Type: Model · Timing: Pre-generated · Access: Product / app
- Input: Image, Text prompt → Output: Flat video
- Idea: Midjourney presents it as a step from its aesthetic image model toward real-time open-world simulation.
- What it is: Midjourney's first video model (2025-06-18) animates any Midjourney image into five-second clips, extendable to about 21 seconds, with automatic or prompted motion.
- How it works: Image-to-video model with 'low' and 'high' motion settings; architecture not published.
- Specs: 480p · 5 s, extendable to ~21 s
- Capability: Authoring accessibility, Situation diversity
- Video: https://www.youtube.com/watch?v=E9PvSeIO5NY
- Project page: https://updates.midjourney.com/introducing-our-v1-video-model/

#### Seedance 1.0 — ByteDance Seed (2025-06-11)
- Type: Model · Timing: Pre-generated · Access: Product / app, Public API
- Input: Text prompt, Image → Output: Flat video
- Idea: Native multi-shot storytelling (cut, reverse shot, close-up) in a single generation.
- What it is: ByteDance Seed's Seedance 1.0 (2025-06-11) generates 1080p multi-shot clips that keep subjects consistent across cuts; ByteDance reported it ranked first in the Artificial Analysis text- and image-to-video arenas after release.
- How it works: Diffusion transformer with decoupled spatial and temporal layers, multi-source data curation, RLHF and a distillation stack giving about 10x faster inference (per the technical report).
- Specs: 1080p · 5–10 s · multi-shot
- Capability: Persistence, Perceptual realism, Authoring accessibility
- Paper: https://arxiv.org/abs/2506.09113 (arXiv 2025)
- Video: https://www.youtube.com/watch?v=F7wNbB0_uyk
- Project page: https://seed.bytedance.com/en/seedance

#### Veo 3 — Google DeepMind (2025-05-20)
- Type: Model · Timing: Pre-generated · Access: Public API, Product / app
- Input: Text prompt, Image → Output: Flat video, Speech / voice, Sound, music & spatial audio
- Idea: Sound and lip-synced speech arrive with the picture, so a generated scene can carry a social interaction, not just a view.
- What it is: Veo 3 (Google I/O, 2025-05-20) generates video together with dialogue, sound effects and ambient sound in one pass, which made talking characters in generated scenes common; a September 2025 DeepMind paper reports it solving perception and physics tasks zero-shot.
- How it works: Joint audio-video diffusion model; the paper 'Video models are zero-shot learners and reasoners' probes it on 62 tasks by prompting alone.
- Specs: 8 s · 720p / 1080p · native audio
- Capability: Perceptual realism, Situational reach, Behavioral plausibility
- Paper: https://arxiv.org/abs/2509.20328 (arXiv 2025)
- Video: https://www.youtube.com/watch?v=QYnJ3qJ5qJQ
- Images: https://storage.googleapis.com/gweb-uniblog-publish-prod/images/5.20v2_SS_1920x1080.width-1300.png
- Project page: https://blog.google/innovation-and-ai/products/generative-media-models-io-2025/
- API docs: https://ai.google.dev/gemini-api/docs/video

#### Gen-4 — Runway (2025-03-31)
- Type: Model · Timing: Pre-generated · Access: Product / app, Public API
- Input: Text prompt, Image → Output: Flat video
- Idea: Identity that holds across shots is what turns isolated clips into a scenario with recurring characters.
- What it is: Gen-4 (2025-03-31) keeps characters, objects and locations consistent across shots from a single reference image, so the same person can appear in different lighting and settings.
- How it works: Image-to-video diffusion with visual reference conditioning ('References') for identity and style; architecture not published.
- Specs: 5 / 10 s · 720p
- Capability: Persistence, Experimental control, Authoring accessibility
- Video: https://www.youtube.com/watch?v=uRkfzKYFOxc
- Images: https://d3phaj0sisr2ct.cloudfront.net/site/content/images/card_gen4post.jpg
- Project page: https://runwayml.com/research/introducing-runway-gen-4
- API docs: https://docs.dev.runwayml.com/

#### Veo 2 — Google DeepMind (2024-12-16)
- Type: Model · Timing: Pre-generated · Access: Public API, Product / app
- Input: Text prompt, Image → Output: Flat video
- Idea: Lens type and camera moves became reliable prompt parameters, useful when a scenario needs a specific viewpoint.
- What it is: Second Veo model (2024-12-16) with better physics and camera control and output up to 4K; DeepMind reported it was preferred over Sora Turbo, Kling and Minimax in human comparisons at launch. It became available in the Gemini API, Gemini app and YouTube Shorts.
- How it works: Diffusion-based video model with improved modeling of physics, human motion and cinematography; details not published.
- Specs: up to 4K · 8 s clips (API)
- Capability: Perceptual realism, Experimental control, Behavioral plausibility
- Video: https://www.youtube.com/watch?v=PEUcCF-jVCI
- Images: https://storage.googleapis.com/gweb-uniblog-publish-prod/images/12-16-24_GenMedia_16x9.width-1300.png
- Project page: https://blog.google/innovation-and-ai/models-and-research/google-labs/video-image-generation-update-december-2024/
- API docs: https://ai.google.dev/gemini-api/docs/video

#### Movie Gen — Meta (2024-10-04)
- Type: Research demo · Timing: Pre-generated · Access: Research only
- Input: Text prompt, Image → Output: Flat video, Sound, music & spatial audio
- Idea: Put personalization, editing and sound into one documented system, with one of the most detailed public technical reports of its generation.
- What it is: Meta's Movie Gen (2024-10-04) is a research suite that generates 16-second 1080p video, personalizes it from a photo of a person, edits it by text and adds synchronized sound effects and music; it was not released as a standalone product.
- How it works: 30B-parameter transformer trained with flow matching for video, plus a 13B audio model, described in a 92-page report.
- Specs: 30B video · 13B audio · 16 s · 16 fps · 1080p (upsampled)
- Capability: Perceptual realism, Experimental control, Authoring accessibility
- Paper: https://arxiv.org/abs/2410.13720 (arXiv 2024)
- Video: https://www.youtube.com/watch?v=FHSSx4dUs7E
- Project page: https://ai.meta.com/research/movie-gen/

#### Gen-3 Alpha — Runway (2024-06-17)
- Type: Model · Timing: Pre-generated · Access: Product / app, Public API
- Input: Text prompt, Image, Video → Output: Flat video
- Idea: Framed commercial video generation explicitly as world modeling, a line Runway later carried into its interactive GWM models.
- What it is: Gen-3 Alpha (2024-06-17) was the first model trained on Runway's new large-scale multimodal infrastructure, with expressive human characters and fine-grained temporal control; Runway presented it as a step toward 'General World Models'.
- How it works: Diffusion model trained jointly on videos and images with highly descriptive, temporally dense captions.
- Specs: 10 s · 1280×768
- Capability: Perceptual realism, Experimental control
- Video: https://www.youtube.com/watch?v=nByslCkykj8
- Images: https://d3phaj0sisr2ct.cloudfront.net/site/blog/images/research-001.jpg
- Project page: https://runwayml.com/research/introducing-gen-3-alpha
- API docs: https://docs.dev.runwayml.com/

#### Dream Machine — Luma AI (2024-06-12)
- Type: Product / app · Timing: Pre-generated · Access: Product / app, Public API
- Input: Text prompt, Image → Output: Flat video
- Idea: Free public access in mid-2024 turned video generation into something a student could test the same afternoon.
- What it is: Luma's Dream Machine (2024-06-12) made a high-quality text- and image-to-video model free to try on the web, producing 120-frame clips in about two minutes; it was among the first Sora-class tools open to anyone.
- How it works: Transformer-based video diffusion model (Luma Ray1) trained directly on video.
- Specs: 5 s · 120 frames
- Capability: Authoring accessibility, Situation diversity
- Video: https://www.youtube.com/watch?v=Zb3tffmBPRE
- Images: https://cdn.sanity.io/images/2ylxvaa2/production/b31d99c8312ed2f74080e118e9d58bf6b2b6e953-1200x630.png?w=1200&h=630&fm=jpg
- Project page: https://lumalabs.ai/dream-machine
- API docs: https://docs.lumalabs.ai/

#### Kling — Kuaishou (2024-06-06)
- Type: Model · Timing: Pre-generated · Access: Product / app, Public API
- Input: Text prompt, Image → Output: Flat video
- Idea: Showed that a Chinese short-video platform could put frontier video generation in millions of users' hands months before OpenAI did.
- What it is: Kuaishou's first Kling model (2024-06-06) was the first Sora-class text-to-video model the public could use, with clips of up to two minutes at 1080p and 30 fps claimed; it opened worldwide in July 2024.
- How it works: Diffusion transformer with a 3D VAE and 3D spatiotemporal attention, trained on Kuaishou-scale video data (per Kuaishou).
- Specs: up to 2 min · 1080p · 30 fps (claimed)
- Capability: Perceptual realism, Persistence, Authoring accessibility
- Video: https://www.youtube.com/watch?v=BKNAXS0keoQ
- Project page: https://kling.ai/
- API docs: https://app.klingai.com/global/dev

#### Veo — Google DeepMind (2024-05-14)
- Type: Model · Timing: Pre-generated · Access: Waitlist / early access
- Input: Text prompt, Image, Video → Output: Flat video
- Idea: Treated film vocabulary as the control interface: you direct a shot with the words a cinematographer would use.
- What it is: Google DeepMind's first Veo model, announced at Google I/O on 2024-05-14, generating 1080p clips that can run beyond a minute and follow cinematic terms such as 'timelapse' or 'aerial shot'; it first reached selected creators through VideoFX.
- How it works: Latent diffusion transformer conditioned on text, image or video; DeepMind describes it as building on GQN, Phenaki, WALT, VideoPoet and Lumiere.
- Specs: 1080p · > 60 s (claimed)
- Capability: Perceptual realism, Experimental control
- Video: https://www.youtube.com/watch?v=dKAVFLB75xs
- Images: https://storage.googleapis.com/gweb-uniblog-publish-prod/images/IO24_Gen_Media_Header_1.width-1300.png
- Project page: https://blog.google/innovation-and-ai/products/google-generative-ai-veo-imagen-3/

#### Sora — OpenAI (2024-02-15)
- Type: Model · Timing: Pre-generated · Access: Research only
- Input: Text prompt, Image, Video → Output: Flat video
- Idea: Made 'video model as world simulator' the field's framing: minute-long shots that keep objects and space mostly consistent, but nothing a person can act in.
- What it is: OpenAI's first text-to-video model, previewed in February 2024 with up to one-minute 1080p shots that keep scenes and camera motion consistent; it shipped as a product in December 2024. OpenAI closed the Sora app on 2026-04-26 and the API on 2026-09-24.
- How it works: Diffusion transformer over spacetime patches of a compressed video latent, trained on videos and images of varying duration, resolution and aspect ratio.
- Specs: up to 60 s · up to 1080p (Feb 2024 preview)
- Capability: Perceptual realism, Persistence, Situation diversity
- Paper: https://openai.com/index/video-generation-models-as-world-simulators/ (OpenAI technical report 2024)
- Video: https://www.youtube.com/watch?v=HK6y8DAPN_0
- Images: https://images.ctfassets.net/kftzwdyauwt9/8264d3d7-922c-4343-dde924eae75b/c9f68101050dc2a6caaac2f434c0da5e/paper-airplanes.jpg?w=1600&h=900&fit=fill
- Project page: https://openai.com/index/sora/

#### Lumiere — Google (2024-01-23)
- Type: Research demo · Timing: Pre-generated · Access: Research only
- Input: Text prompt, Image → Output: Flat video
- Idea: Global temporal coherence beats stitched keyframes for motion that has to look physically continuous.
- What it is: Google Research's Lumiere (2024-01-23) generates a clip's whole duration in one pass instead of keyframes plus interpolation, giving more coherent motion; demos included stylized generation, cinemagraphs and video inpainting.
- How it works: Space-Time U-Net (STUNet) that downsamples in both space and time, built on a pretrained text-to-image diffusion model.
- Specs: 80 frames · 16 fps · 5 s
- Capability: Behavioral plausibility, Experimental control
- Paper: https://arxiv.org/abs/2401.12945 (SIGGRAPH Asia 2024)
- Video: https://www.youtube.com/watch?v=f9ThAzZs32M
- Images: https://lumiere-video.github.io/images/lumiere_frame_poster.jpg
- Project page: https://lumiere-video.github.io/

#### Pika 1.0 — Pika (2023-11-28)
- Type: Product / app · Timing: Pre-generated · Access: Product / app
- Input: Text prompt, Image, Video → Output: Flat video
- Idea: An early sign that playful editing features, not raw quality, drive mass adoption of generative video.
- What it is: Pika 1.0 (2023-11-28) turned the Discord-born Pika bot into a web 'idea-to-video' platform with text-to-video, image animation and in-video edits such as region modification and canvas expansion.
- How it works: Proprietary video diffusion model; later Pika 2.x versions added effects such as Pikaffects and scene ingredients.
- Capability: Authoring accessibility, Co-creation & agency
- Video: https://www.youtube.com/watch?v=6b10jGNNbXQ
- Images: https://pika.art/brand/opengraph.png
- Project page: https://pika.art/

#### Gen-2 — Runway (2023-03-20)
- Type: Model · Timing: Pre-generated · Access: Product / app
- Input: Text prompt, Image → Output: Flat video
- Idea: Put prompt-to-clip generation in the hands of non-engineers two years before it became photorealistic.
- What it is: Runway's Gen-2 (2023-03-20) was the first commercially available text-to-video model, turning a prompt or an image into four-second clips inside a web editor used by filmmakers.
- How it works: Latent video diffusion that extends Runway's Gen-1 structure-and-content model with text and image conditioning.
- Specs: 4 s clips (at launch)
- Capability: Authoring accessibility, Situation diversity
- Video: https://www.youtube.com/watch?v=trXPfpV5iRQ
- Images: https://runway-static-assets.s3.amazonaws.com/site/images/news/Researchhub_014.jpg
- Project page: https://runwayml.com/research/gen-2

#### Imagen Video — Google (2022)
- Type: Research demo · Timing: Pre-generated · Access: Research only
- Input: Text prompt → Output: Flat video
- Idea: Cascaded diffusion showed high resolution was reachable, at the cost of chaining seven models.
- What it is: Google Research's Imagen Video (2022-10-05) generated 5.3-second clips at 1280×768 and 24 fps from text, the highest-fidelity text-to-video results of its time; it was never released.
- How it works: Cascade of seven video diffusion models (a base model plus three spatial and three temporal super-resolution stages) conditioned on a T5-XXL text encoder.
- Specs: 1280×768 · 24 fps · 128 frames
- Capability: Perceptual realism
- Paper: https://arxiv.org/abs/2210.02303 (arXiv 2022)
- Video: https://imagen.research.google/video/videos/leaves.mp4
- Images: https://imagen.research.google/video/leaves.png
- Project page: https://imagen.research.google/video/

#### Make-A-Video — Meta (2022)
- Type: Research demo · Timing: Pre-generated · Access: Research only
- Input: Text prompt, Image → Output: Flat video
- Idea: Showed that motion can be learned from unlabeled video and appearance from captioned images, a recipe many later models reused.
- What it is: Meta AI's Make-A-Video (2022-09-29) was one of the first text-to-video systems, producing short, low-resolution clips such as a teddy bear painting a portrait, learned without paired text-video data.
- How it works: Extends a text-to-image diffusion model with spatiotemporal convolution and attention layers, frame interpolation and super-resolution.
- Specs: 16 frames · up to 768×768
- Capability: Situation diversity
- Paper: https://arxiv.org/abs/2209.14792 (ICLR 2023)
- Images: https://makeavideo.studio/assets/A_teddy_bear_painting_a_portrait-sm.gif
- Project page: https://makeavideo.studio/

### Open-weight video models

Wan, HunyuanVideo, LTX, CogVideoX, Mochi, Open-Sora and others that can be run, version-pinned and inspected.

#### MiniMax H3 — MiniMax (2026-07-31)
- Type: Model · Timing: Pre-generated · Access: Open weights / code, Public API, Product / app
- Input: Text prompt, Image, Video → Output: Flat video, Speech / voice, Sound, music & spatial audio
- Idea: A flagship-level audio-video model with downloadable weights lets a lab pin the exact model behind its stimuli.
- What it is: MiniMax H3 (2026-07-31) generates up to 15 seconds of 2K video with native stereo sound from text, image, video and audio context and edits video by instruction; unusually for a flagship, MiniMax published the weights on Hugging Face.
- How it works: Contextual Omni Representation with an H3-VAE, an H3-Omni Transformer and in-context regeneration for editing (per MiniMax).
- Specs: up to 15 s · 2K · native stereo audio
- Capability: Authoring accessibility, Experimental control, Perceptual realism
- Video: https://filecdn.minimax.chat/public/h3-en-v2-video-001-1785473639588.mp4
- Images: https://file.cdn.minimax.io/public/3df321d9-42bd-4be0-ac58-71f22377a11f.png
- Project page: https://www.minimax.io/blog/minimax-h3
- API docs: https://platform.minimax.io/docs
- Code: https://huggingface.co/MiniMaxAI/MiniMax-H3

#### HunyuanVideo 1.5 — Tencent Hunyuan (2025-11-20)
- Type: Model · Timing: Pre-generated · Access: Open weights / code
- Input: Text prompt, Image → Output: Flat video
- Idea: The open-model race shifted to quality per parameter; a lab can run it without a cluster.
- What it is: HunyuanVideo 1.5 (2025-11-20) is a lightweight 8.3-billion-parameter open model that produces 720p video (1080p with its super-resolution stage) and runs on consumer GPUs.
- How it works: DiT with selective and sliding tile attention (SSTA), glyph-aware bilingual text encoding and a video super-resolution network.
- Specs: 8.3B · 720p → 1080p SR
- Capability: Authoring accessibility, Experimental control
- Paper: https://arxiv.org/abs/2511.18870 (arXiv 2025)
- Video: https://github.com/user-attachments/assets/d45ec78e-ea40-47f1-8d4d-f4d9a0682e2d
- Project page: https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5
- Code: https://github.com/Tencent-Hunyuan/HunyuanVideo-1.5

#### LTX-2 — Lightricks (2025-10-23)
- Type: Model · Timing: Pre-generated · Access: Open weights / code, Public API, Product / app
- Input: Text prompt, Image → Output: Flat video, Speech / voice, Sound, music & spatial audio
- Idea: Open, version-pinnable audio-video generation at production resolution, with LoRA hooks for custom control.
- What it is: Lightricks' LTX-2 (announced 2025-10-23, weights released afterwards) generates synchronized audio and video at up to 4K and 50 fps; LTX-2.5 followed in August 2026 as a 22B open model with a family of control LoRAs.
- How it works: Asymmetric dual-stream transformer that generates audio and video jointly through cross-modal attention (per the LTX-2 paper).
- Specs: up to 4K · up to 50 fps · up to 20 s · synchronized audio
- Capability: Perceptual realism, Temporal responsiveness, Authoring accessibility
- Paper: https://arxiv.org/abs/2601.03233 (arXiv 2026)
- Video: https://www.youtube.com/watch?v=KRJW3yXwJdY
- Images: https://cdn.prod.website-files.com/68872d15af29880764eac4aa/695b91d18b612de840f4786e_ltx-2-mode-open-graph.jpg
- Project page: https://ltx.io/model/ltx-2
- Code: https://github.com/Lightricks/LTX-2

#### Ovi — Character.AI (2025-09-30)
- Type: Model · Timing: Pre-generated · Access: Open weights / code
- Input: Text prompt, Image → Output: Flat video, Speech / voice, Sound, music & spatial audio
- Idea: Open joint audio-video generation lets labs study lip-synced speech stimuli without a closed API.
- What it is: Character.AI's Ovi (2025-09-30) is an open model that generates five seconds of 720p video together with its audio (speech, effects, music) in one pass, one of the first open-weight answers to Veo 3-style talking clips.
- How it works: Twin-backbone design: identical audio and video diffusion transformers (the video branch initialized from Wan 2.2) fused block by block with bidirectional cross-attention.
- Specs: 11B · 5 s · 720p · 24 fps
- Capability: Behavioral plausibility, Perceptual realism
- Paper: https://arxiv.org/abs/2510.01284 (arXiv 2025)
- Video: https://aaxwaz.github.io/Ovi/assets/final_ovi_trailer.mp4
- Images: https://aaxwaz.github.io/Ovi/assets/robot_red_eye.png
- Project page: https://aaxwaz.github.io/Ovi/
- Code: https://github.com/character-ai/Ovi

#### Wan 2.2 — Alibaba Tongyi (Qwen) (2025-07-28)
- Type: Model · Timing: Pre-generated · Access: Open weights / code, Public API
- Input: Text prompt, Image → Output: Flat video
- Idea: Aesthetic parameters (light, lens, composition) become explicit, reproducible knobs in an open model.
- What it is: Wan 2.2 (2025-07-28) is the first open mixture-of-experts video model, with cinematic controls for lighting, color and composition and a 5B model that makes 720p video on a single consumer GPU.
- How it works: Two-expert MoE diffusion (a high-noise expert for layout, a low-noise expert for detail; 27B total, 14B active) plus a high-compression TI2V-5B model.
- Specs: A14B MoE · TI2V-5B · 720p · 24 fps
- Capability: Perceptual realism, Experimental control, Authoring accessibility
- Video: https://www.youtube.com/watch?v=ktDogWm7Hac
- Project page: https://wan.video/
- Code: https://github.com/Wan-Video/Wan2.2

#### Wan 2.1 — Alibaba Tongyi (Qwen) (2025-02-25)
- Type: Model · Timing: Pre-generated · Access: Open weights / code, Public API
- Input: Text prompt, Image, Video → Output: Flat video
- Idea: The open base most 2025 real-time and control research was built on, so findings transfer between labs.
- What it is: Alibaba's Wan 2.1 (open-sourced 2025-02-25 under Apache 2.0) provides 14B and 1.3B text- and image-to-video models; the small one needs about 8 GB of VRAM. It became the base of many research and community models, including VACE, Self Forcing and Krea Realtime.
- How it works: Diffusion transformer trained with flow matching and a new causal 3D VAE (Wan-VAE) that encodes 1080p video of unlimited length.
- Specs: 14B / 1.3B · 480p / 720p · 1.3B on 8.19 GB VRAM
- Capability: Authoring accessibility, Experimental control, Situation diversity
- Paper: https://arxiv.org/abs/2503.20314 (arXiv 2025)
- Video: https://www.youtube.com/watch?v=2CObXv_CLyY
- Project page: https://wan.video/
- Code: https://github.com/Wan-Video/Wan2.1

#### Step-Video-T2V — StepFun (2025-02-17)
- Type: Model · Timing: Pre-generated · Access: Open weights / code
- Input: Text prompt → Output: Flat video
- Idea: Pushed open-model scale to 30B and documented the practical limits of scaling video diffusion.
- What it is: StepFun's Step-Video-T2V (2025-02-17) is a 30-billion-parameter open text-to-video model that generates up to 204 frames from Chinese or English prompts.
- How it works: DiT with 3D full attention, a deep-compression video VAE (16x16 spatial, 8x temporal) and Video-DPO preference tuning.
- Specs: 30B · 204 frames · 544×992
- Capability: Persistence, Perceptual realism
- Paper: https://arxiv.org/abs/2502.10248 (arXiv 2025)
- Video: https://github.com/user-attachments/assets/9274b351-595d-41fb-aba3-f58e6e91603a
- Project page: https://github.com/stepfun-ai/Step-Video-T2V
- Code: https://github.com/stepfun-ai/Step-Video-T2V

#### HunyuanVideo — Tencent Hunyuan (2024-12-03)
- Type: Model · Timing: Pre-generated · Access: Open weights / code, Product / app
- Input: Text prompt → Output: Flat video
- Idea: Briefly closed the gap between open and closed video quality and seeded a large ecosystem of LoRAs and control adapters.
- What it is: Tencent's HunyuanVideo (2024-12-03) was the largest open video model at release, at 13 billion parameters; Tencent reported it outperformed Runway Gen-3 and Luma 1.6 in professional human evaluation.
- How it works: Dual-stream-to-single-stream diffusion transformer with a 3D causal VAE and a multimodal LLM as text encoder.
- Specs: 13B · 720p · 129 frames
- Capability: Perceptual realism, Experimental control
- Paper: https://arxiv.org/abs/2412.03603 (arXiv 2024)
- Video: https://github.com/user-attachments/assets/22440764-0d7e-438e-a44d-d0dad1006d3d
- Project page: https://github.com/Tencent-Hunyuan/HunyuanVideo
- Code: https://github.com/Tencent-Hunyuan/HunyuanVideo

#### LTX-Video — Lightricks (2024-11-22)
- Type: Model · Timing: Pre-generated · Access: Open weights / code, Product / app
- Input: Text prompt, Image → Output: Flat video
- Idea: Generation faster than real time is the precondition for any loop in which a scene reacts to a participant.
- What it is: Lightricks' LTX-Video (2024-11-22) was the first open video model fast enough to generate clips faster than they play: about five seconds of 768×512 video in roughly four seconds on an H100. A 13B version followed in May 2025.
- How it works: DiT with a highly compressed VAE (1:192) whose decoder also performs the final denoising step.
- Specs: 2B / 13B · 768×512 · 24 fps · faster than real time on H100
- Capability: Temporal responsiveness, Authoring accessibility
- Paper: https://arxiv.org/abs/2501.00103 (arXiv 2024)
- Video: https://www.youtube.com/watch?v=7ZMxtMyUD_U
- Project page: https://github.com/Lightricks/LTX-Video
- Code: https://github.com/Lightricks/LTX-Video

#### Mochi 1 — Genmo (2024-10-22)
- Type: Model · Timing: Pre-generated · Access: Open weights / code
- Input: Text prompt → Output: Flat video
- Idea: Permissive licensing made it a common base for academic fine-tuning and benchmarking.
- What it is: Genmo's Mochi 1 (2024-10-22) was a 10-billion-parameter open text-to-video model under Apache 2.0, with motion quality and prompt adherence that were strong for its time.
- How it works: Asymmetric Diffusion Transformer (AsymmDiT) with a video VAE that compresses 128x and a single T5-XXL text encoder.
- Specs: 10B · 480p · 30 fps · 5.4 s
- Capability: Behavioral plausibility, Experimental control
- Video: https://cdn.genmo.dev/results/mochi-launch.mp4
- Images: https://www.genmo.ai/media/social/mochi1.png
- Project page: https://www.genmo.ai/blog/mochi-1-a-new-sota-in-open-text-to-video
- Code: https://github.com/genmoai/mochi

#### CogVideoX — Zhipu AI (2024-08-06)
- Type: Model · Timing: Pre-generated · Access: Open weights / code, Product / app
- Input: Text prompt, Image → Output: Flat video
- Idea: Showed an open model could run on a single consumer GPU and be fine-tuned by labs for their own scenarios.
- What it is: Zhipu AI's CogVideoX (open-sourced 2024-08-06) was the first strong open text-to-video model from a Chinese lab, generating 6-second 720×480 clips; it powers Zhipu's Qingying product.
- How it works: Diffusion transformer with a 3D causal VAE and an 'expert transformer' whose expert adaptive LayerNorm fuses text and video tokens.
- Specs: 2B / 5B · 6 s · 720×480 · 8 fps
- Capability: Authoring accessibility, Experimental control
- Paper: https://arxiv.org/abs/2408.06072 (ICLR 2025)
- Video: https://github.com/user-attachments/assets/cf5953ea-96d3-48fd-9907-c4708752c714
- Project page: https://github.com/zai-org/CogVideo
- Code: https://github.com/zai-org/CogVideo

#### Stable Video Diffusion — Stability AI (2023-11-21)
- Type: Model · Timing: Pre-generated · Access: Open weights / code
- Input: Image → Output: Flat video
- Idea: Gave researchers a video prior they could fine-tune; many later 3D and 4D generators start from SVD weights.
- What it is: Stable Video Diffusion (2023-11-21) was the first widely used open-weight image-to-video model, turning a still image into 14- or 25-frame clips; it also served as the base for multi-view 3D generators.
- How it works: Latent video diffusion with temporal layers added to Stable Diffusion 2.1, trained in three stages: image pretraining, curated video pretraining and high-quality fine-tuning.
- Specs: 576×1024 · 14 / 25 frames · 3–30 fps
- Capability: Authoring accessibility, Experimental control
- Paper: https://arxiv.org/abs/2311.15127 (arXiv 2023)
- Images: https://static1.squarespace.com/static/6213c340453c3f502425776e/62f2452bc121595f4d87c713/655c90f932dda45e84c36b21/1728899860281/SVD+blog+cover+image.jpg?format=1500w
- Project page: https://stability.ai/news/stable-video-diffusion-open-ai-video-model
- Code: https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt

### Control, editing & characters

Camera paths, motion transfer, reference characters, video-to-video editing and performance-driven animation.

#### Kling O1 — Kuaishou (2025-12-01)
- Type: Model · Timing: Pre-generated · Access: Product / app, Public API
- Input: Text prompt, Image, Video → Output: Flat video
- Idea: A single model that both shoots and edits means a scene can be iterated by instruction while the characters stay fixed.
- What it is: Kling O1 (2025-12-01), billed as the first unified video model, handles generation, reference-based creation and video editing (swapping subjects, restyling, changing shots) within one multimodal prompt.
- How it works: Multimodal visual-language backbone driving a diffusion video generator, described in the Kling-Omni technical report.
- Capability: Experimental control, Co-creation & agency, Authoring accessibility
- Paper: https://arxiv.org/abs/2512.16776 (arXiv 2025)
- Video: https://www.youtube.com/watch?v=V_oiFFTpxHs
- Project page: https://kling.ai/
- API docs: https://app.klingai.com/global/dev

#### Wan-Animate — Alibaba Tongyi (Qwen) (2025-09-17)
- Type: Open-source tool · Timing: Pre-generated · Access: Open weights / code
- Input: Image, Video → Output: Flat video, Virtual human (face / body)
- Idea: Open-weight performance transfer: any recorded actor can drive any character on a lab's own GPUs.
- What it is: Wan-Animate (2025-09) animates a character image with the body motion and facial expressions of a driving video, or replaces the person in the video with that character while matching the scene's lighting; weights are open as Wan2.2-Animate-14B.
- How it works: Built on Wan 2.2, with skeleton signals for body motion, implicit facial features for expression and a relighting LoRA for character replacement.
- Specs: 14B
- Capability: Behavioral plausibility, Experimental control
- Paper: https://arxiv.org/abs/2509.14055 (arXiv 2025)
- Video: https://humanaigc.github.io/wan-animate/content/aa/rep_shots.mp4
- Images: https://humanaigc.github.io/wan-animate/content/aa/arch.png
- Project page: https://humanaigc.github.io/wan-animate/
- Code: https://huggingface.co/Wan-AI/Wan2.2-Animate-14B

#### Runway Aleph — Runway (2025-07-25)
- Type: Model · Timing: Pre-generated · Access: Product / app, Public API
- Input: Video, Text prompt, Image → Output: Flat video
- Idea: Editing real footage by instruction lets a researcher change one factor (lighting, a prop, the weather) while the rest of a recorded scene stays the same.
- What it is: Aleph (2025-07-25) is Runway's in-context video editing model: given existing footage it adds or removes objects, changes lighting, weather or season, restyles the clip, or renders a new camera angle of the same scene; Aleph 2.0 followed on 2026-05-21.
- How it works: In-context video model conditioned on the input clip plus text or image instructions; architecture not published.
- Capability: Experimental control, Co-creation & agency, Authoring accessibility
- Video: https://www.youtube.com/watch?v=KUHx-2uz_qI
- Images: https://d3phaj0sisr2ct.cloudfront.net/site/content/images/rw-card-aleph.jpg
- Project page: https://runwayml.com/research/introducing-runway-aleph
- API docs: https://docs.dev.runwayml.com/

#### Act-Two — Runway (2025-07-15)
- Type: Model · Timing: Pre-generated · Access: Product / app, Public API
- Input: Video, Image → Output: Flat video, Virtual human (face / body)
- Idea: A recorded human performance becomes the control signal: behavior is scripted by acting it once and re-cast onto many characters.
- What it is: Act-Two (2025-07-15) transfers an actor's recorded performance (face, head, body and hands) onto any character image or video; it succeeds Act-One (2024-10), which animated faces only.
- How it works: Performance-driven video generation from a driving video and a character reference; architecture not published.
- Capability: Experimental control, Behavioral plausibility, Authoring accessibility
- Video: https://www.youtube.com/watch?v=JW8PHlFD7HM
- Project page: https://runwayml.com/research
- API docs: https://docs.dev.runwayml.com/

#### ReCamMaster — Jianhong Bai, Kuaishou (2025-03-14)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code
- Input: Video, Camera path / pose → Output: Flat video
- Idea: Re-shooting a recorded event from a new angle is a step toward free-viewpoint video without 3D capture.
- What it is: ReCamMaster (2025-03-14, Zhejiang University with Kuaishou's Kling team) re-renders an existing video along a new camera trajectory, producing the same dynamic scene from a different viewpoint.
- How it works: Conditions a pretrained text-to-video model on the source video by frame-dimension concatenation, trained on a synchronized multi-camera dataset rendered in Unreal Engine 5.
- Capability: Experimental control, Situational reach
- Paper: https://arxiv.org/abs/2503.11647 (arXiv 2025)
- Video: https://jianhongbai.github.io/ReCamMaster/videos/ReCamMaster/TEASER_compressed.mp4
- Images: https://jianhongbai.github.io/ReCamMaster/pics/fig_pipe.png
- Project page: https://jianhongbai.github.io/ReCamMaster/
- Code: https://github.com/KwaiVGI/ReCamMaster

#### VACE — Alibaba Tongyi (Qwen) (2025-03-10)
- Type: Open-source tool · Timing: Pre-generated · Access: Open weights / code
- Input: Video, Image, Text prompt → Output: Flat video
- Idea: Combining pose, depth, mask and reference conditions in one open model gives labs fine-grained, reproducible control over generated stimuli.
- What it is: VACE (paper 2025-03-10; open weights on Wan 2.1 in May 2025) is Alibaba's all-in-one model for reference-to-video, video-to-video and masked editing: move, swap, expand or animate anything in a clip with one network.
- How it works: A Video Condition Unit packs text, frames and masks into one input that is injected into a diffusion transformer through context adapters.
- Specs: 1.3B / 14B (Wan 2.1-based)
- Capability: Experimental control, Authoring accessibility
- Paper: https://arxiv.org/abs/2503.07598 (ICCV 2025)
- Video: https://ali-vilab.github.io/VACE-Page/assets/videos/SwapAnything_1.mp4
- Project page: https://ali-vilab.github.io/VACE-Page/
- Code: https://github.com/ali-vilab/VACE

### Real-time & long video

Causal, autoregressive and distilled models that stream video live or keep generating for minutes.

#### Vidu S1 — Shengshu Technology (Vidu) (2026-07-03)
- Type: Model · Timing: Real-time streaming · Access: Product / app
- Input: Speech & audio, Text prompt, Image → Output: Interactive frame stream, Speech / voice
- Idea: Conversation-paced video generation moves video models into the turn-taking loop of virtual humans.
- What it is: Vidu S1 (2026-07-03) is Shengshu's real-time interactive video model: a generated character or scene responds within milliseconds as you talk to it, for uses such as talking pets or gaming companions.
- How it works: Real-time video generation conditioned on streaming voice input; architecture not published.
- Capability: Temporal responsiveness, Reactivity, Behavioral plausibility
- Video: https://www.youtube.com/watch?v=jaPLmykNk0I
- Project page: https://www.vidu.com/

#### Helios — Shenghai Yuan (2026-03-04)
- Type: Research demo · Timing: Real-time streaming · Access: Open weights / code
- Input: Text prompt, Image → Output: Interactive frame stream
- Idea: Real-time no longer means 1.3B: quality and responsiveness stop being a trade-off.
- What it is: Helios (Peking University with ByteDance, 2026-03) is an open 14-billion-parameter model that generates minute-scale video in real time on a single H100, showing large real-time models can match small ones in speed.
- How it works: Autoregressive video diffusion with techniques for long-horizon stability and efficient inference (per the Helios paper).
- Specs: 14B · real-time on 1 H100 · minute-scale (reported)
- Capability: Temporal responsiveness, Persistence, Perceptual realism
- Paper: https://arxiv.org/abs/2603.04379 (arXiv 2026)
- Video: https://www.youtube.com/watch?v=vd_AgHtOUFQ
- Images: https://pku-yuangroup.github.io/Helios-Page/figures/highlight_speed_v2.png
- Project page: https://pku-yuangroup.github.io/Helios-Page/
- Code: https://github.com/PKU-YuanGroup/Helios

#### Lucy 2 — Decart (2026-01-26)
- Type: Model · Timing: Real-time streaming · Access: Public API, Product / app
- Input: Video, Text prompt, Image → Output: Interactive frame stream
- Idea: Live, reference-guided transformation of a person's camera view is the building block for generative mixed-reality conditions.
- What it is: Decart's Lucy 2 (2026-01-26) edits a live video stream at 1080p and 30 fps with near-zero latency, from character swaps and clothing changes to product placement and full environment changes driven by text and reference images; Lucy 2.5 (2026-07-16) improved temporal stability.
- How it works: Real-time world-transformation video model building on MirageLSD and Lucy Edit; Decart reports it learns physical consistency without depth maps or 3D.
- Specs: 1080p · 30 fps · near-zero latency (claimed)
- Capability: Temporal responsiveness, Reactivity, Co-creation & agency
- Video: https://www.youtube.com/watch?v=N82RN4dPKaM
- Images: https://cdn.prod.website-files.com/69a974f0b1fffb03644ecf2c/6a4d10c78242cf13741618a1_lucy-og.jpg
- Project page: https://decart.ai/publications/lucy-2-introducing-sota-video-generation-in-realtime

#### Krea Realtime 14B — Krea (2025-10-15)
- Type: Model · Timing: Real-time streaming · Access: Open weights / code, Product / app
- Input: Text prompt, Video → Output: Interactive frame stream
- Idea: Real-time generation at 14B scale shows interactivity no longer requires a small, low-quality model.
- What it is: Krea Realtime 14B (2025-10-15) is an open text-to-video model distilled from Wan 2.1 14B that streams at about 11 fps on one B200 and lets users change prompts or restyle video while it is generating.
- How it works: Self Forcing distillation of a bidirectional 14B model into an autoregressive one, with KV-cache recomputation and attention-bias techniques against error accumulation.
- Specs: 14B · ~11 fps on 1 B200 · ~1 s to first frame
- Capability: Temporal responsiveness, Co-creation & agency
- Video: https://s.krea.ai/krea-rt-video-blog/prompt_003.mp4
- Images: https://s.krea.ai/krea_realtime_14b_cover.webp
- Project page: https://www.krea.ai/blog/krea-realtime-14b
- Code: https://huggingface.co/krea/krea-realtime-video

#### LongLive — Shuai Yang, NVIDIA (2025-09-26)
- Type: Research demo · Timing: Real-time streaming · Access: Open weights / code
- Input: Text prompt → Output: Interactive frame stream
- Idea: A running scene that changes when told to is the core of a directable situation.
- What it is: LongLive (NVIDIA, MIT, HKUST (Guangzhou) and others, 2025-09) generates video in real time for up to four minutes while the user types new prompts mid-stream, with smooth transitions between them.
- How it works: Frame-level autoregressive model with KV re-caching on prompt switches, streaming long tuning and short-window attention with a frame sink.
- Specs: 1.3B · 20.7 fps (H100) · up to 240 s
- Capability: Temporal responsiveness, Adaptation, Persistence
- Paper: https://arxiv.org/abs/2509.22622 (ICLR 2026)
- Video: https://www.youtube.com/watch?v=CO1QC7BNvig
- Images: https://nvlabs.github.io/LongLive/assets/streaming_long.jpg
- Project page: https://nvlabs.github.io/LongLive/
- Code: https://github.com/NVlabs/LongLive

#### MirageLSD — Decart (2025-07-17)
- Type: Model · Timing: Real-time streaming · Access: Product / app, Public API
- Input: Video, Text prompt → Output: Interactive frame stream
- Idea: Live 'reskinning' of the real world is the most direct generative route to mixed-reality situations, as long as the transformation stays stable.
- What it is: Decart's MirageLSD (2025-07-17) transforms any live camera, game or video feed into a prompted style or world in real time (Decart cites under 40 ms latency at 24 fps); it was released as a web demo and mobile apps and later succeeded by Lucy 2.
- How it works: Live-Stream Diffusion: a causal, frame-by-frame video diffusion model that uses diffusion forcing and history augmentation to resist error accumulation, with custom GPU kernels.
- Specs: 24 fps · < 40 ms latency (claimed)
- Capability: Temporal responsiveness, Reactivity, Co-creation & agency
- Video: https://cdn.prod.website-files.com/6874f65b561c843511ee5b85%2F68791e9e65a7de52792e9cdf_mirage-transcode.mp4
- Images: https://cdn.prod.website-files.com/6875c2f7957701899283e82a/68793def662cebbb07fd8940_image.png
- Project page: https://web.archive.org/web/20250801/https://decart.ai/publications/mirage

#### Seaweed APT2 — ByteDance Seed (2025-06-11)
- Type: Research demo · Timing: Real-time streaming · Access: Research only
- Input: Text prompt, Image, Camera path / pose → Output: Interactive frame stream
- Idea: One network evaluation per frame makes video respond to input like a game engine, at least for a minute.
- What it is: ByteDance Seed's Seaweed APT2 (2025-06) streams 736×416 video at 24 fps on one H100 for up to a minute, steered in real time by camera moves or, in its virtual-human demo, by a person's pose.
- How it works: Autoregressive adversarial post-training (AAPT): a pretrained video diffusion model is converted to emit one latent frame per network evaluation, trained adversarially with student forcing on long rollouts.
- Specs: 8B · 24 fps · 736×416 · up to 1,440 frames (1 min)
- Capability: Temporal responsiveness, Reactivity, Persistence
- Paper: https://arxiv.org/abs/2506.09350 (arXiv 2025)
- Video: https://cdn.seaweed-apt.com/apt2/highres/man-helmet.mp4
- Images: https://cdn.seaweed-apt.com/apt2/misc/teaser.jpg
- Project page: https://seaweed-apt.com/2

#### Self Forcing — Xun Huang, Adobe (2025-06-09)
- Type: Research demo · Timing: Real-time streaming · Access: Open weights / code
- Input: Text prompt → Output: Interactive frame stream
- Idea: Became a common training recipe for real-time video models such as LongLive and Krea Realtime.
- What it is: Self Forcing (Adobe Research and UT Austin, 2025-06) trains an autoregressive video model on its own rollouts, closing the train-test gap, and streams video at about 17 fps with sub-second latency on one H100.
- How it works: Autoregressive rollout with KV caching during training, a holistic video-level distribution-matching loss and a rolling KV cache for extrapolation.
- Specs: 1.3B · ~17 fps · < 1 s latency (H100)
- Capability: Temporal responsiveness, Persistence
- Paper: https://arxiv.org/abs/2506.08009 (arXiv 2025)
- Video: https://github.com/user-attachments/assets/7548c2db-fe03-4ba8-8dd3-52d2c6160739
- Images: https://self-forcing.github.io/static/teaser.jpg
- Project page: https://self-forcing.github.io/
- Code: https://github.com/guandeh17/Self-Forcing

#### MAGI-1 — Sand AI (2025-04-21)
- Type: Model · Timing: Pre-generated · Access: Open weights / code
- Input: Text prompt, Image, Video → Output: Flat video
- Idea: Chunk-wise autoregression gives second-by-second control over how a scene unfolds.
- What it is: Sand AI's MAGI-1 (2025-04-21) is an open 24-billion-parameter autoregressive video model that generates video chunk by chunk, enabling streaming output, unlimited extension and prompt changes per chunk.
- How it works: Autoregressive denoising over 24-frame chunks, with later chunks kept noisier while earlier ones are refined, on a transformer-based VAE.
- Specs: 24B (4.5B distilled) · 24-frame chunks
- Capability: Persistence, Experimental control
- Paper: https://arxiv.org/abs/2505.13211 (arXiv 2025)
- Video: https://www.youtube.com/watch?v=RauucR3jmo0
- Images: https://repository-images.githubusercontent.com/970023948/34ab6cc2-a578-4398-8f10-be2bffa59fa4
- Project page: https://github.com/SandAI-org/MAGI-1
- Code: https://github.com/SandAI-org/MAGI-1

#### SkyReels-V2 — Skywork (Kunlun Tech) (2025-04-21)
- Type: Model · Timing: Pre-generated · Access: Open weights / code
- Input: Text prompt, Image → Output: Flat video
- Idea: Diffusion forcing turns a clip model into a continuous storyteller, though drift still accumulates over minutes.
- What it is: Skywork's SkyReels-V2 (2025-04) is an open 'infinite-length film' model that keeps extending a video while holding shots consistent, trained with film-grammar annotations.
- How it works: Diffusion-forcing framework (per-token noise levels) with a multimodal captioner (SkyCaptioner) for shot language and reinforcement learning for motion quality.
- Specs: 1.3B / 14B · 540p / 720p · unlimited length
- Capability: Persistence, Authoring accessibility
- Paper: https://arxiv.org/abs/2504.13074 (arXiv 2025)
- Video: https://github.com/user-attachments/assets/f6f9f9a7-5d5f-433c-9d73-d8d593b7ad25
- Project page: https://github.com/SkyworkAI/SkyReels-V2
- Code: https://github.com/SkyworkAI/SkyReels-V2

#### FramePack — Lvmin Zhang (2025-04-17)
- Type: Open-source tool · Timing: Pre-generated · Access: Open weights / code
- Input: Image, Text prompt → Output: Flat video
- Idea: Constant memory regardless of length makes long takes possible on ordinary hardware.
- What it is: FramePack (Lvmin Zhang and Maneesh Agrawala, Stanford, 2025-04) generates one- to two-minute image-to-video clips on a 6 GB laptop GPU by compressing past frames into a fixed-size context.
- How it works: Next-frame-section prediction with progressive context packing (older frames get fewer tokens) and anti-drifting bidirectional sampling, on a HunyuanVideo backbone.
- Specs: 13B · 30 fps · 60–120 s · 6 GB VRAM
- Capability: Persistence, Authoring accessibility
- Paper: https://arxiv.org/abs/2504.12626 (arXiv 2025)
- Video: https://lllyasviel.github.io/frame_pack_gitpage/long/250415_173937_297_5230_451.mp4
- Images: https://lllyasviel.github.io/frame_pack_gitpage/img/sample.png
- Project page: https://lllyasviel.github.io/frame_pack_gitpage/
- Code: https://github.com/lllyasviel/FramePack

#### CausVid — Tianwei Yin, Adobe (2024-12-10)
- Type: Research demo · Timing: Real-time streaming · Access: Open weights / code
- Input: Text prompt, Image → Output: Interactive frame stream
- Idea: Video that plays the moment you press generate: the hinge between offline clips and live, steerable streams.
- What it is: CausVid (MIT and Adobe, 2024-12) converts a slow bidirectional video diffusion model into a causal one that starts streaming frames after about 1.3 seconds at roughly 9 fps on one GPU.
- How it works: Distribution-matching distillation of a bidirectional teacher into a 4-step autoregressive student with block-causal attention and KV caching.
- Specs: 9.4 fps streaming · ~1.3 s first-frame latency
- Capability: Temporal responsiveness, Persistence
- Paper: https://arxiv.org/abs/2412.07772 (CVPR 2025)
- Video: https://www.youtube.com/watch?v=nXAT18XuEKc
- Project page: https://causvid.github.io/
- Code: https://github.com/tianweiy/CausVid

#### StreamDiffusion — Akio Kodaira (2023-12-19)
- Type: Open-source tool · Timing: Real-time streaming · Access: Open weights / code
- Input: Video, Text prompt → Output: Interactive frame stream
- Idea: Per-frame diffusion on a live camera feed was the first practical way to change what a person sees as it happens.
- What it is: StreamDiffusion (2023-12-19) restyles a live webcam or screen feed with Stable Diffusion at up to about 90 fps on one RTX 4090, and became the engine of many TouchDesigner and live-performance installations; StreamDiffusionV2 (2025-11) extends it to video diffusion models.
- How it works: Pipeline-level optimizations (stream batching of denoising steps, residual classifier-free guidance, a stochastic similarity filter) around few-step models such as SD-Turbo and LCM.
- Specs: up to 91 fps img2img on RTX 4090 (reported)
- Capability: Temporal responsiveness, Reactivity
- Paper: https://arxiv.org/abs/2312.12491 (arXiv 2023)
- Video: https://www.youtube.com/watch?v=I9Eq4LoB7Wk
- Images: https://raw.githubusercontent.com/cumulo-autumn/StreamDiffusion/main/assets/demo_07.gif
- Project page: https://github.com/cumulo-autumn/StreamDiffusion
- Code: https://github.com/cumulo-autumn/StreamDiffusion

#### Phenaki — Google (2022)
- Type: Research demo · Timing: Pre-generated · Access: Research only
- Input: Text prompt → Output: Flat video
- Idea: The first sketch of a story-driven, prompt-switching video stream, an idea later made interactive by real-time models such as LongLive.
- What it is: Phenaki (Google, 2022-10-05) generated videos of variable length, up to minutes, from a sequence of prompts that change over time, for example a story told shot by shot.
- How it works: C-ViViT tokenizer that compresses video into discrete tokens, plus a bidirectional masked transformer conditioned on text that generates autoregressively in time.
- Specs: variable length · minutes (prompt sequences)
- Capability: Persistence, Adaptation
- Paper: https://arxiv.org/abs/2210.02399 (ICLR 2023)
- Video: https://www.youtube.com/watch?v=Uf_xSjL0Bh8
- Project page: https://phenaki.github.io/

### Panoramic, stereo & spatial video

360°, stereo and spatial video generation, and 2D-to-3D conversion for headsets.

#### 360Anything — Ziyi Wu, Google DeepMind (2026-01-22)
- Type: Research demo · Timing: Pre-generated · Access: Research only
- Input: Image, Video → Output: 360° / stereo video, Image / panorama
- Idea: Any generated clip, even a world-model rollout, can be wrapped around the viewer after the fact.
- What it is: 360Anything (Google DeepMind with the University of Toronto, ECCV 2026) lifts any perspective image or video, including footage from the Genie 3 world model, to a seamless 360° panorama without camera calibration.
- How it works: Geometry-free diffusion transformer that learns from data where the perspective input sits inside the panorama, without explicit camera intrinsics or extrinsics.
- Capability: Situational reach, Situation diversity
- Paper: https://arxiv.org/abs/2601.16192 (ECCV 2026)
- Video: https://360anything.github.io/videos/video_360_viewer/genie_3_concat.mp4
- Images: https://360anything.github.io/imgs/image_360_viewer/lighthouse_ours.png
- Project page: https://360anything.github.io/

#### StereoPilot — Guibao Shen, Kuaishou (2025-12-18)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code
- Input: Video → Output: 360° / stereo video
- Idea: Fast, format-aware stereo conversion lets a lab deliver generated scenes to different headsets without re-rendering.
- What it is: StereoPilot (HKUST (Guangzhou) with Kuaishou's Kling team, 2025-12) converts monocular video to stereo for both parallel and converged camera setups in a single efficient pass, using generative video priors.
- How it works: Unified feed-forward stereo conversion on a video-generation backbone, trained on a curated dataset covering parallel and converged stereo.
- Capability: Situational reach, Perceptual realism
- Paper: https://arxiv.org/abs/2512.16915 (arXiv 2025)
- Video: https://hit-perfect.github.io/StereoPilot/Video_Intro/StereoPilot.mp4
- Images: https://hit-perfect.github.io/StereoPilot/Figs/PacificRim.gif
- Project page: https://hit-perfect.github.io/StereoPilot/
- Code: https://github.com/KlingTeam/StereoPilot

#### Imagine360 — Jing Tan (2024-12-04)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code
- Input: Video → Output: 360° / stereo video
- Idea: Turns phone footage of an event into surround material a participant can look around in.
- What it is: Imagine360 (CUHK and Shanghai AI Laboratory, NeurIPS 2025) expands an ordinary perspective video into a full 360° video, inventing the surroundings outside the original frame while keeping its motion.
- How it works: Dual-branch perspective/panorama diffusion with antipodal masking and elevation-aware design, trained on panoramic video.
- Capability: Situational reach, Perceptual realism
- Paper: https://arxiv.org/abs/2412.03552 (NeurIPS 2025)
- Video: https://www.youtube.com/watch?v=gRGo4B41GXY
- Project page: https://ys-imtech.github.io/projects/Imagine360/
- Code: https://github.com/YS-IMTech/Imagine360

#### StereoCrafter — Sijie Zhao, Tencent ARC Lab (2024-09-11)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code
- Input: Video → Output: 360° / stereo video
- Idea: Any existing or generated clip can become stereo, the cheapest path from flat stimuli to headset stimuli.
- What it is: StereoCrafter (Tencent ARC Lab, 2024-09) converts ordinary 2D videos into long, high-fidelity stereoscopic 3D for headsets such as Apple Vision Pro, using a video diffusion model to fill disoccluded regions.
- How it works: Depth-based forward warping to a second view, then a stereo video inpainting diffusion model trained on large stereo video data fills the holes.
- Capability: Situational reach, Perceptual realism
- Paper: https://arxiv.org/abs/2409.07447 (arXiv 2024)
- Video: https://github.com/stereocrafter/stereocrafter.github.io/releases/download/V0.0.1/camel_sbs.mp4
- Project page: https://stereocrafter.github.io/
- Code: https://github.com/TencentARC/StereoCrafter

#### 360DVD — Qian Wang (2024-01-12)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code
- Input: Text prompt → Output: 360° / stereo video
- Idea: One of the first ways to generate surround video a person can look around in, rather than a framed view.
- What it is: 360DVD (Peking University, CVPR 2024) generates 360° equirectangular panorama videos from text, with optional motion conditions, for viewing in a VR headset.
- How it works: Lightweight 360-Adapter with 360°-specific enhancements on a pretrained text-to-video model, trained on the WEB360 panorama-video dataset.
- Specs: equirectangular · 512×1024
- Capability: Situational reach, Situation diversity
- Paper: https://arxiv.org/abs/2401.06578 (CVPR 2024)
- Video: https://akaneqwq.github.io/360DVD/static/videos/01-vr.mp4
- Images: https://akaneqwq.github.io/360DVD/static/images/framework.webp
- Project page: https://akaneqwq.github.io/360DVD/
- Code: https://github.com/akaneqwq/360DVD

## Interactive Virtual Humans

Faces and bodies generated live for conversation: video avatars that listen while they speak, audio-driven portraits, photoreal 3D avatars, and models of nonverbal behaviour.

### Real-time conversational video

Full-duplex audio-visual agents rendered as video: Tavus, HeyGen, D-ID, Character.AI, Anam, Hedra and others.

#### Griffin — Tavus (2026-10-01)
- Type: Model · Timing: Full-duplex · Access: Waitlist / early access
- Input: Video, Speech & audio → Output: Virtual human (face / body), Speech / voice, Dialogue / text
- Idea: The first commercial virtual human that listens while it talks, can be interrupted and nods mid-sentence, so face-to-face timing becomes a generated, studyable variable.
- What it is: Griffin is a full-duplex video-to-video model for live video calls: it watches and hears the person, decides moment by moment whether to speak, hold, back-channel or yield, and generates the speech and every pixel of a 720p person in real time from one reference image. Tavus reports that 48% of people in one-minute calls thought it was a real person; Griffin-Lite is a research preview for selected testers as of October 2026.
- How it works: A continuous conversational model reads incoming audio and video at sub-second intervals and emits text plus control signals; a streaming autoregressive diffusion speech generator (on a 48 kHz continuous codec) and a few-step causal video DiT distilled with DMD2, teacher forcing and Self-Forcing render the reply.
- Specs: 720p · real time · 0.43 s avg audio-to-video latency (H100) · 48% judged human in 1-min calls · VideoFDB generation 3.83 (human 3.92)
- Capability: Temporal responsiveness, Behavioral plausibility, Perceptual realism
- Video: https://www.youtube.com/watch?v=lHw6yoyPkpo
- Images: https://cdn.prod.website-files.com/68c8e57d6e512b9573db146f/6abe6c84125e80a50a54a217_Griffin%20OG%20v3%20%E2%80%94%2003%20Split%20%C2%B7%20Type%20Left.jpg
- Project page: https://www.tavus.io/griffin
- API docs: https://docs.tavus.io

#### Sessions (Interactive Avatars) — Synthesia (2026-10-01)
- Type: Product / app · Timing: Turn-based · Access: Product / app, Public API
- Input: Speech & audio → Output: Virtual human (face / body), Speech / voice, Dialogue / text
- Idea: A mainstream training vendor now sells scored roleplay with a responsive avatar, which is the deliberate-practice loop of simulation training at enterprise scale.
- What it is: Sessions is Synthesia's platform for two-way conversations with real-time avatars: Roleplay Sessions (first released in July 2026) let employees rehearse sales, coaching or support conversations with an avatar that pushes back, followed by AI scoring and feedback, and Survey Sessions turn a form into a spoken interview. An Interactive Avatars API exposes the same avatars to developers.
- How it works: Likely a cascaded stack (speech recognition, an LLM scenario prompt, TTS and Synthesia's real-time avatar renderer) with a separate LLM coach that grades transcripts.
- Capability: Situational reach, Authoring accessibility, Adaptation
- Video: https://www.youtube.com/watch?v=vcYBbtFejmg
- Images: https://cdn.prod.website-files.com/65e89895c5a4b8d764c0d70e/6abd354ed0f78074501e8826_GTM_Sessions_Blog-Header_V1.png
- Project page: https://www.synthesia.io/post/sessions-interactive-avatar-platform
- API docs: https://www.synthesia.io/features/avatars/interactive-avatars

#### Gemini 3.8 Live with Live Avatar — Google DeepMind (2026-09-24)
- Type: Product / app · Timing: Turn-based · Access: Product / app, Public API
- Input: Speech & audio, Video, Image → Output: Virtual human (face / body), Speech / voice, Dialogue / text
- Idea: A frontier-lab virtual human ships with provenance built in: every generated frame and word is watermarked, which matters for studies that must disclose synthetic interlocutors.
- What it is: Live Avatar couples Google's Gemini 3.8 Live dialogue model with near-real-time video generation, so an enterprise agent appears as a talking character that sees and hears the user, lip-syncs across 97 languages (switching mid-conversation) and keeps talking while tools run in the background. It is available in Gemini Enterprise with preset avatars; custom avatars from a reference image are allowlist-only, and all audio and video carry SynthID watermarks.
- How it works: Gemini 3.8 Live native audio dialogue (audio and video in, speech out) natively coupled with a low-latency streaming video generator; turn-taking is handled by the Live model, with interruption support as in the Live API (Google describes 'fluid turn-taking', not overlapping speech).
- Specs: 97 languages · near-real-time streaming video · SynthID in audio and video
- Capability: Temporal responsiveness, Perceptual realism, Experimental control
- Video: https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/GLA-Video_3_compression.mp4
- Images: https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Slide_16_9_-_37.width-1300.png
- Project page: https://deepmind.google/blog/introducing-gemini-38-live-with-live-avatar/
- API docs: https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/live-api

#### Character World Model-1 (CWM-1) — LemonSlice (2026-09-23)
- Type: Model · Timing: Real-time streaming · Access: Product / app, Public API
- Input: Speech & audio, Image, Text prompt → Output: Virtual human (face / body), Interactive frame stream
- Idea: Treats the avatar as a small world model centred on a character, so body language and object interaction are generated rather than rigged.
- What it is: CWM-1 generates an entire live video-call scene from one image of any character (person, anime, animal): face, body, hands, hair and surroundings, with an emotion engine that triggers actions such as shrugging, leaning in or picking up a phone. It follows LemonSlice-2 (December 2025), a 20B causal model that ran at 20 fps on one GPU.
- How it works: A causal, few-step video diffusion transformer conditioned on audio, a prompt and action/emotion states predicted by a separate emotion engine that reads the conversation.
- Specs: LemonSlice-2: 20B params · 20 fps on 1 GPU · 471 ms p99 latency (platform)
- Capability: Behavioral plausibility, Experimental control, Situation diversity
- Video: https://lemonslice.com/cwm-1/header/header-1.webm
- Images: https://lemonslice.com/cwm-1/launch.webp
- Project page: https://lemonslice.com/cwm-1
- API docs: https://lemonslice.com/docs

#### AVTR-1 — Avaturn Live (2026-09-19)
- Type: Open-source tool · Timing: Real-time streaming · Access: Open weights / code
- Input: Speech & audio, Image → Output: Virtual human (face / body), Motion / animation
- Idea: An open, measurable reference for the plumbing of live avatars, including a test (R-DGG) of whether the listener's motion actually depends on the other speaker.
- What it is: AVTR-1 is an open stack for real-time avatar conversations: a small motion generator listens to both the user's and the voice agent's audio, and a renderer and serving backend turn it into a synchronized audio-video stream that handles interruptions. Weights, renderer and backend are released under component-specific licenses.
- How it works: A 153M-parameter autoregressive flow-matching motion generator conditioned on both participants' audio, with a self-distilled streaming audio encoder and analytically bounded user-facing latency.
- Specs: 153M-param motion model · real time on data-center and consumer GPUs
- Capability: Temporal responsiveness, Experimental control
- Paper: https://arxiv.org/abs/2609.22913 (arXiv 2026)
- Video: https://avaturn-live.github.io/avtr-1-projectpage/media/pair_V00_S2019_I00001095.mp4
- Images: https://avtr-1.avaturn.live/media/og-preview.png
- Project page: https://avaturn-live.github.io/avtr-1-projectpage/
- Code: https://github.com/avaturn-live/avtr-1

#### FacePlex — Habin Lim (2026-06-29)
- Type: Research demo · Timing: Full-duplex · Access: Research only
- Input: Speech & audio, Text prompt → Output: Virtual human (face / body), Speech / voice
- Idea: Shows that a full-duplex face needs to anticipate its own speech, not just follow it.
- What it is: FacePlex generates a conversational avatar's speech and facial motion together, token by token, while the user talks, prepares mouth shapes before the matching audio is emitted, and adds non-verbal reactions grounded in the dialogue, rendered with Gaussian splatting.
- How it works: A unified streaming framework that places speech tokens, facial-motion tokens and Gaussian-splatting rendering on one shared timeline, built on a full-duplex spoken dialogue model.
- Specs: 122 ms end-to-end avatar interaction latency
- Capability: Temporal responsiveness, Behavioral plausibility
- Paper: https://arxiv.org/abs/2606.30145 (arXiv 2026)
- Video: https://hahminlew.github.io/faceplex/static/videos/compare_offline/session_1.mp4
- Images: https://hahminlew.github.io/faceplex/static/images/main_figure.png
- Project page: https://hahminlew.github.io/faceplex

#### Wan-Streamer — Alibaba Tongyi (Qwen) (2026-06-24)
- Type: Model · Timing: Full-duplex · Access: Research only
- Input: Video, Speech & audio, Text prompt → Output: Virtual human (face / body), Speech / voice, Dialogue / text
- Idea: Collapses the whole cascade into one streaming model, so timing, turn-taking and expression are learned jointly rather than stitched together.
- What it is: Wan-Streamer is an end-to-end model that listens, sees, thinks, speaks and responds on video at the same time, inside one Transformer, with no separate speech recognition, LLM, TTS or avatar modules. Version 0.3 (July 2026) adds 'world + event stream' video pretraining for free-form behaviour; the demos show real-time full-duplex video conversation.
- How it works: Interleaved visual, audio and text input and output tokens in a single Transformer with block-causal attention, causal encoders and decoders for incremental streaming.
- Specs: 640×368 · 25 fps · ~200 ms model-side latency
- Capability: Temporal responsiveness, Reactivity, Behavioral plausibility
- Paper: https://arxiv.org/abs/2606.25041 (arXiv 2026)
- Video: https://wan-streamer.com/v0.1/assets/video/realtime.mp4
- Images: https://wan-streamer.com/v0.1/assets/img/agent-chat-poster.jpg https://wan-streamer.com/v0.1/assets/img/framework.png
- Project page: https://wan-streamer.com

#### CARA-4 — Anam (2026-05-12)
- Type: Model · Timing: Turn-based · Access: Public API, Product / app
- Input: Speech & audio, Image, Text prompt → Output: Virtual human (face / body)
- Idea: Directable performance (a distressed patient versus a calm coach) turns the avatar's affect into an experimental condition you can write down.
- What it is: CARA-4 is Anam's real-time avatar diffusion model: from a single photo it renders a conversational face at 25 fps in landscape (1152×768) or portrait (768×1152), with Director Notes that let a builder set how the avatar performs (warm, distressed, angry) and let the LLM shift that direction mid-reply.
- How it works: A diffusion model generating every pixel in real time, conditioned on speech audio and text performance cues, inside a conversation engine with sub-second median latency from end of user speech.
- Specs: 1152×768 / 768×1152 · 25 fps · <1 s median response latency
- Capability: Perceptual realism, Experimental control, Behavioral plausibility
- Video: https://framerusercontent.com/assets/89hAkOrdOYdbEcy5VV2WX2NS6uk.mp4
- Images: https://framerusercontent.com/assets/cyASyHEg6g3WK5dCwQoOyyVbFZU.png
- Project page: https://anam.ai/research
- API docs: https://anam.ai/docs/introduction/models

#### LPM 1.0 (Large Performance Model) — Ailing Zeng (2026-04-09)
- Type: Research demo · Timing: Real-time streaming · Access: Research only
- Input: Speech & audio, Image, Text prompt → Output: Virtual human (face / body), Flat video
- Idea: Frames expressiveness, real-time speed and long-horizon identity as one 'performance trilemma' that game NPCs and live characters must solve together.
- What it is: LPM 1.0 is a video model for conversational character performance: given a character image, it generates listening video from the user's audio and speaking video from synthesized speech, with text prompts for motion, in real time and at unbounded length while keeping identity stable. The authors propose LPM-Bench for interactive character performance.
- How it works: A 17B Diffusion Transformer trained on speaking-listening paired human video with identity-aware references, distilled into a causal streaming generator (Online LPM).
- Specs: 17B base · real-time streaming · infinite length
- Capability: Behavioral plausibility, Persistence, Experimental control
- Paper: https://arxiv.org/abs/2604.07823 (arXiv 2026)
- Video: https://pub-4e149c2dec59455a88c79783cc4985c8.r2.dev/videos/hero-demo.mp4
- Project page: https://large-performance-model.github.io

#### V4 Expressive Visual Agents — D-ID (2026-03-16)
- Type: Product / app · Timing: Turn-based · Access: Product / app, Public API
- Input: Speech & audio, Text prompt → Output: Virtual human (face / body), Speech / voice, Dialogue / text
- Idea: Emotion-matched expression became a standard feature of commercial agents, but it follows the agent's own text, not the user's behaviour.
- What it is: D-ID's V4 Expressive Visual Agents are real-time conversational avatars whose expressions follow the emotional tone of what they say, built from a short recording of a person and deployable on websites or via API, with a self-hosting option for enterprises.
- How it works: A cascaded agent (knowledge base, LLM, TTS) drives D-ID's V4 avatar video model, which conditions facial expression on the sentiment of the generated speech.
- Capability: Perceptual realism, Authoring accessibility
- Video: https://www.youtube.com/watch?v=-WhLtR1no0M
- Project page: https://www.d-id.com/introducing-v4-expressive-avatars/
- API docs: https://docs.d-id.com

#### Phoenix-4 — Tavus (2026-02-18)
- Type: Model · Timing: Real-time streaming · Access: Public API, Product / app
- Input: Speech & audio, Text prompt → Output: Virtual human (face / body)
- Idea: Makes the listening face, not just the speaking mouth, a controllable output of a real-time renderer.
- What it is: Phoenix-4 renders a full-face video replica of a real person in real time, with explicit emotion control and active-listening expressions while the user speaks; it is the face of Tavus' Conversational Video Interface. Phoenix-4.5 (2026-09-09) adds upper-body motion, zero-shot identities and about 134 ms audio-to-video latency.
- How it works: An audio feature encoder and behaviour model drive a real-time full-face rendering network trained on conversation video, with emotion and listening states as conditioning; it works alongside Sparrow (turn-taking) and Raven (perception) in a cascaded stack.
- Specs: 1080p · 40 fps (Phoenix-4) · ~134 ms audio-to-video (Phoenix-4.5)
- Capability: Perceptual realism, Behavioral plausibility
- Video: https://www.youtube.com/watch?v=FDxfK2xisoE
- Images: https://cdn.prod.website-files.com/68c8e57d6e512b9573db147f/6993c0e122a8c8cbd131d6ac_Herop44.avif
- Project page: https://www.tavus.io/blog/phoenix-4-real-time-human-rendering-with-emotional-intelligence
- API docs: https://docs.tavus.io

#### LiveAvatar (Interactive Avatar) — HeyGen (2025-11)
- Type: Platform / API · Timing: Turn-based · Access: Public API, Product / app
- Input: Speech & audio, Text prompt → Output: Virtual human (face / body), Speech / voice
- Idea: Real-time avatars became cheap enough to give every voice agent a face, which moves the open question from 'can it render' to 'does it behave'.
- What it is: LiveAvatar is HeyGen's real-time avatar streaming API, the successor to its Interactive Avatar: a half- or full-body 1080p avatar, cloned from an image or two minutes of footage, speaks a voice agent's replies over WebRTC. HeyGen reports under 300 ms median time to first frame and prices from about $0.01 per minute at volume.
- How it works: Avatar-only rendering streamed via LiveKit/WebRTC, driven either by HeyGen's managed ASR-LLM-TTS stack or by the developer's own voice agent.
- Specs: 1080p · <300 ms median time to first frame · unlimited concurrency
- Capability: Authoring accessibility, Temporal responsiveness
- Video: https://www.youtube.com/watch?v=4hVvW4tHFJY
- Images: https://www.liveavatar.com/og-image-fb.jpg
- Project page: https://www.liveavatar.com/
- API docs: https://docs.liveavatar.com
- Code: https://github.com/heygen-com/liveavatar-web-sdk

#### Conversational Video Interface (Phoenix-2) — Tavus (2024-08-15)
- Type: Platform / API · Timing: Turn-based · Access: Public API, Product / app
- Input: Speech & audio, Video → Output: Virtual human (face / body), Speech / voice, Dialogue / text
- Idea: Packaged speech recognition, an LLM, voice and a rendered face into one API, which made a talking video person something a lab could rent by the minute.
- What it is: Tavus' Conversational Video Interface puts a video replica of a real person into a live call that answers spoken questions; it launched in August 2024 with the Phoenix-2 rendering model, which Tavus describes as the step that broke the real-time barrier. As of October 2026 a CVI 'PAL' is configured with a persona, face, voice, objectives, guardrails, knowledge base and memories, and runs on the full Tavus pipeline, in Echo mode, or inside LiveKit, Pipecat or Agora.
- How it works: A cascaded pipeline: speech-to-text, an LLM, text-to-speech and the Phoenix-2 audio-driven face renderer (likely a 3D-prior talking-head model fitted per replica from a short training video), streamed over WebRTC with interruption handling.
- Capability: Temporal responsiveness, Authoring accessibility
- Video: https://www.youtube.com/watch?v=OZthIm5W-yQ
- Project page: https://www.tavus.io/blog/introducing-the-evolution-of-conversational-video-interface-now-with-emotional-intelligence
- API docs: https://docs.tavus.io

### Audio-driven talking heads & bodies

Speech-to-face and speech-to-body generation from a single image: VASA-1, EMO, OmniHuman, Hallo, LivePortrait…

#### SoulX-FlashTalk — Soul AI Lab (2025-12-29)
- Type: Model · Timing: Real-time streaming · Access: Open weights / code
- Input: Image, Speech & audio → Output: Virtual human (face / body), Interactive frame stream
- Idea: An open real-time avatar from a social-app company, used as a baseline by commercial full-duplex systems in 2026.
- What it is: SoulX-FlashTalk streams a high-fidelity audio-driven avatar from a 14B model with sub-second start-up and real-time frame rate, for unbounded durations; weights are on Hugging Face.
- How it works: Self-correcting bidirectional distillation that keeps bidirectional attention within chunks, a multi-step retrospective self-correction mechanism, and hybrid sequence parallelism with parallel VAE decoding.
- Specs: 14B params · 32 fps · 0.87 s start-up latency
- Capability: Temporal responsiveness, Persistence
- Paper: https://arxiv.org/abs/2512.23379 (arXiv 2025)
- Video: https://github.com/Soul-AILab/Soul-AILab.github.io/raw/refs/heads/main/soulx-livetalk/static/videos/teaser_1_n_0129.mp4
- Project page: https://soul-ailab.github.io/soulx-flashtalk/
- Code: https://github.com/Soul-AILab/SoulX-FlashTalk

#### Live Avatar — Alibaba Quark (2025-12-04)
- Type: Model · Timing: Real-time streaming · Access: Open weights / code
- Input: Image, Speech & audio → Output: Virtual human (face / body), Interactive frame stream
- Idea: Shows that frontier-size video models can run as live avatars if the denoising steps are spread across GPUs.
- What it is: Live Avatar streams an audio-driven avatar from a 14B diffusion model in real time and for hours (over 10,000 seconds) without identity drift; its demos show live interaction with a voice agent.
- How it works: Two-stage distillation of a bidirectional model into a causal few-step streamer, long-horizon anti-drift strategies, and Timestep-forcing Pipeline Parallelism (one denoising timestep per GPU).
- Specs: 14B params · 45 fps · 1.21 s time to first frame on 5× H800 · >10,000 s stable
- Capability: Temporal responsiveness, Persistence
- Paper: https://arxiv.org/abs/2512.04677 (arXiv 2025)
- Video: https://www.youtube.com/watch?v=_KwHex65wCU
- Project page: https://liveavatar.github.io/
- Code: https://github.com/Alibaba-Quark/LiveAvatar

#### MIDAS — Kuaishou (2025-08-26)
- Type: Research demo · Timing: Real-time streaming · Access: Research only
- Input: Speech & audio, Text prompt, Image → Output: Virtual human (face / body), Interactive frame stream
- Idea: Uses an LLM backbone as the motion planner of a streaming avatar, so new control signals can be added like new tokens.
- What it is: MIDAS from Kuaishou's Kling team is a real-time, streaming digital human that takes audio, pose and text as control and generates video autoregressively, demonstrated in duplex two-person conversations and multilingual speech.
- How it works: A lightly modified LLM consumes multimodal condition encodings and guides a diffusion head, with a deep-compression autoencoder (up to 64×) and about 20,000 hours of dialogue video for training.
- Specs: ~20,000 h training dialogue · up to 64× latent compression
- Capability: Temporal responsiveness, Experimental control
- Paper: https://arxiv.org/abs/2508.19320 (arXiv 2025)
- Video: https://chenmingthu.github.io/milm/static/videos/dia_duplex.mp4
- Images: https://chenmingthu.github.io/milm/static/images/dialog.png
- Project page: https://chenmingthu.github.io/milm/

#### OmniHuman-1.5 — ByteDance Seed (2025-08-26)
- Type: Model · Timing: Pre-generated · Access: Public API, Product / app
- Input: Image, Speech & audio, Text prompt → Output: Virtual human (face / body), Flat video
- Idea: Adds a 'deliberative' planner so a generated person acts on what is said, a step from lip sync toward behaviour.
- What it is: OmniHuman-1.5 generates minute-long videos of one or several characters whose gestures and expressions follow the meaning and emotion of the speech, not only its rhythm, and can be steered with text prompts; it is available through BytePlus and Dreamina.
- How it works: A dual-system design: a multimodal LLM reasons over audio, image and text to plan high-level actions, and a multimodal DiT with a pseudo last-frame identity design renders the video.
- Capability: Behavioral plausibility, Experimental control
- Paper: https://arxiv.org/abs/2508.19209 (arXiv 2025)
- Video: https://www.youtube.com/watch?v=zjrcDKe2dlI
- Project page: https://omnihuman-lab.github.io/v1_5/

#### InfiniteTalk — Meituan (2025-08-19)
- Type: Model · Timing: Pre-generated · Access: Open weights / code
- Input: Video, Image, Speech & audio → Output: Virtual human (face / body), Flat video
- Idea: Open, long-form audio-driven video that many later real-time systems compare against or build on.
- What it is: InfiniteTalk dubs or animates a person to new speech over unlimited length, moving lips, head, posture and expression together while keeping identity, from a source video or a single image.
- How it works: Sparse-frame video dubbing on a Wan-based video diffusion model, conditioning on selected reference frames so whole-body motion follows audio across chunks.
- Capability: Persistence, Perceptual realism
- Paper: https://arxiv.org/abs/2508.14033 (arXiv 2025)
- Video: https://meigen-ai.github.io/InfiniteTalk/videos/0.mp4
- Images: https://meigen-ai.github.io/InfiniteTalk/images/0.png
- Project page: https://meigen-ai.github.io/InfiniteTalk/
- Code: https://github.com/MeiGen-AI/InfiniteTalk

#### TalkingMachines — Character.AI (2025-06-03)
- Type: Research demo · Timing: Real-time streaming · Access: Research only
- Input: Image, Speech & audio → Output: Virtual human (face / body), Interactive frame stream
- Idea: Showed the recipe most 2026 real-time avatars use: distil a big bidirectional video model into a causal few-step streamer.
- What it is: TalkingMachines turns a pretrained image-to-video model into a real-time, audio-driven character animator for FaceTime-style calls with an audio LLM, streaming video of unbounded length without drift.
- How it works: An 18B audio-conditioned DiT adapted from a SOTA image-to-video model, distilled asymmetrically into a sparse causal autoregressive student, with DiT and VAE decoding split across GPUs.
- Specs: 18B params · real-time streaming
- Capability: Temporal responsiveness, Perceptual realism
- Paper: https://arxiv.org/abs/2506.03099 (arXiv 2025)
- Video: https://aaxwaz.github.io/TalkingMachines/assets/videos/albert_2.mp4
- Project page: https://aaxwaz.github.io/TalkingMachines/

#### HunyuanVideo-Avatar — Tencent Hunyuan (2025-05-26)
- Type: Model · Timing: Pre-generated · Access: Open weights / code
- Input: Image, Speech & audio → Output: Virtual human (face / body), Flat video
- Idea: Open weights for multi-character audio-driven scenes, a step from one talking head to a small generated social situation.
- What it is: HunyuanVideo-Avatar animates one or several characters in a scene from audio, with emotion taken from a reference image and separate audio streams driving different characters, for example a two-person comedy dialogue.
- How it works: A multimodal DiT built on HunyuanVideo with a character image injection module, an audio emotion module and a face-aware audio adapter that masks audio to each character.
- Capability: Situation diversity, Behavioral plausibility
- Paper: https://arxiv.org/abs/2505.20156 (arXiv 2025)
- Video: https://hunyuanvideo-avatar.github.io/static/%E5%8F%8C%E4%BA%BA/%E9%BB%91%E7%99%BD%E7%9B%B8%E5%A3%B0-2.mp4
- Project page: https://hunyuanvideo-avatar.github.io/
- Code: https://github.com/Tencent-Hunyuan/HunyuanVideo-Avatar

#### AvatarFX — Character.AI (2025-04-22)
- Type: Model · Timing: Pre-generated · Access: Product / app
- Input: Image, Text prompt, Speech & audio → Output: Virtual human (face / body), Flat video
- Idea: Brought face video to a mass companion-chat platform, together with the safety questions (minors, impersonation) that follow.
- What it is: AvatarFX lets Character.AI users turn a character image into a video of it speaking, singing or emoting with a chosen voice, for human, animal and stylized characters, inside the Character.AI app.
- How it works: A DiT-based diffusion video model with audio conditioning (per Character.AI's announcement; architecture details unpublished).
- Capability: Authoring accessibility, Situation diversity
- Video: https://www.youtube.com/watch?v=LEPaWVbRJ1E
- Project page: https://character.ai

#### Character-3 — Hedra (2025-03-12)
- Type: Model · Timing: Pre-generated · Access: Product / app, Public API
- Input: Image, Speech & audio, Text prompt → Output: Virtual human (face / body), Flat video
- Idea: Made audio-driven character video a creator tool used at scale, including for non-human and stylized characters.
- What it is: Character-3 animates any character image (photo, illustration, 3D render) into a talking or singing video from audio and a text prompt that sets emotion and body movement, inside the Hedra Studio app.
- How it works: An 'omnimodal' video model that jointly conditions on image, text and audio (architecture not published).
- Capability: Authoring accessibility, Perceptual realism
- Video: https://www.youtube.com/watch?v=2IcwhZZGJUs
- Project page: https://www.hedra.com/
- API docs: https://www.hedra.com/docs

#### OmniHuman-1 — ByteDance Seed (2025-02-03)
- Type: Model · Timing: Pre-generated · Access: Product / app, Research only
- Input: Image, Speech & audio, Video → Output: Virtual human (face / body), Flat video
- Idea: Scaling one model over mixed conditions (text, audio, pose) brought audio-driven video from heads to whole bodies.
- What it is: OmniHuman-1 turns one image (portrait, half body or full body; real or cartoon) plus audio into a video of the person talking, singing or gesturing, including hands and objects; ByteDance later offered it in Dreamina / Jimeng.
- How it works: A DiT video model trained with an 'omni-conditions' strategy that mixes weaker (text, audio) and stronger (pose) conditions so more training data stays usable.
- Capability: Perceptual realism, Situation diversity
- Paper: https://arxiv.org/abs/2502.01061 (ICCV 2025)
- Video: https://www.youtube.com/watch?v=1NU8NzvAxEg
- Project page: https://omnihuman-lab.github.io/

#### Loopy — ByteDance Seed (2024-09-04)
- Type: Research demo · Timing: Pre-generated · Access: Research only
- Input: Image, Speech & audio → Output: Virtual human (face / body), Flat video
- Idea: Long-range temporal context lets non-verbal motion arise from the audio, not from a looped template.
- What it is: Loopy animates a portrait from audio alone, with sighs, eyebrow movement and head motion that follow the speech rhythm and emotion, without spatial motion templates.
- How it works: A video diffusion model with inter- and intra-clip temporal modules and an audio-to-latents module for long-term motion dependency.
- Capability: Perceptual realism, Behavioral plausibility
- Paper: https://arxiv.org/abs/2409.02634 (ICLR 2025 (Oral))
- Video: https://loopyavatar.github.io/video/diverse_1.mp4
- Project page: https://loopyavatar.github.io/

#### LivePortrait — Kuaishou (2024-07-03)
- Type: Open-source tool · Timing: Real-time streaming · Access: Open weights / code
- Input: Image, Video → Output: Virtual human (face / body), Flat video
- Idea: A fast, controllable, open retargeting tool that became the default way to puppeteer a generated face with a real performer.
- What it is: LivePortrait transfers a driving video's expressions and head pose onto a still portrait (people, and in a later release animals) in about 13 ms per frame, with explicit controls for eye and lip opening and stitching back into the original image.
- How it works: An implicit-keypoint (non-diffusion) animation framework scaled to about 69M training frames, with small MLP stitching and eye/lip retargeting modules.
- Specs: 12.8 ms per frame on RTX 4090
- Capability: Experimental control, Authoring accessibility
- Paper: https://arxiv.org/abs/2407.03168 (arXiv 2024)
- Video: https://liveportrait.github.io/src/video/all_cross_opt.mp4
- Images: https://liveportrait.github.io/src/img/live-portrait.png
- Project page: https://liveportrait.github.io/
- Code: https://github.com/KlingAIResearch/LivePortrait

#### VASA-1 — Microsoft (2024-04-16)
- Type: Model · Timing: Real-time streaming · Access: Research only
- Input: Image, Speech & audio → Output: Virtual human (face / body), Flat video
- Idea: Showed that a single photo could become a real-time conversational face, and why its makers withheld it over impersonation risk.
- What it is: VASA-1 turns one portrait photo and a speech clip into a lifelike talking face with synchronized lips, expressive micro-movements and natural head motion, generated online at 512×512 and up to 40 fps. Microsoft did not release it publicly; in 2025 it reported using VASA-1 for the stylized faces of Copilot Portraits in Copilot Labs.
- How it works: A diffusion transformer generates holistic facial dynamics and head motion in a disentangled face latent space learned from video, then a decoder renders frames from the latent codes.
- Specs: 512×512 · up to 40 fps online · negligible starting latency
- Capability: Perceptual realism, Temporal responsiveness
- Paper: https://arxiv.org/abs/2404.10667 (NeurIPS 2024 (Oral))
- Video: https://vasavatar.github.io/VASA-1/video/realtime_demo.mp4
- Project page: https://www.microsoft.com/en-us/research/project/vasa-1/

#### EMO (Emote Portrait Alive) — Alibaba Tongyi (Qwen) (2024-02-27)
- Type: Research demo · Timing: Pre-generated · Access: Research only
- Input: Image, Speech & audio → Output: Virtual human (face / body), Flat video
- Idea: Moved talking heads from mouth-only lip sync to whole-face emotional performance driven directly by audio.
- What it is: EMO makes a single portrait talk or sing along to any audio, with expressive faces and head motion, and no 3D face model or facial landmarks in between.
- How it works: An audio-to-video diffusion model (Stable Diffusion backbone with ReferenceNet identity features, audio cross-attention and speed/face-region controls) trained on 250+ hours of talking video.
- Capability: Perceptual realism, Behavioral plausibility
- Paper: https://arxiv.org/abs/2402.17485 (arXiv 2024)
- Video: https://humanaigc.github.io/emote-portrait-alive/content/video/%E8%B5%AB%E6%9C%AC16_9.mp4
- Images: https://humanaigc.github.io/emote-portrait-alive/content/images/framework/intro.png
- Project page: https://humanaigc.github.io/emote-portrait-alive/

#### Wav2Lip — K R Prajwal (2020-08-23)
- Type: Open-source tool · Timing: Pre-generated · Access: Open weights / code
- Input: Speech & audio, Video → Output: Flat video, Virtual human (face / body)
- Idea: The lineage's precursor: once lips could follow any voice, a face could be paired with a synthetic speaker, and its lip-sync metrics (LSE-C/D) are still used to score avatars in 2026.
- What it is: Wav2Lip re-syncs the lips of any talking face in a video to a new audio track, for arbitrary identities and languages, without per-speaker training.
- How it works: A GAN-based lip generator trained against a frozen, pre-trained lip-sync expert discriminator (SyncNet) that penalises out-of-sync mouth shapes.
- Capability: Perceptual realism, Authoring accessibility
- Paper: https://arxiv.org/abs/2008.10010 (ACM Multimedia 2020)
- Video: https://www.youtube.com/watch?v=0fXaDCZNOJc
- Project page: https://github.com/Rudrabha/Wav2Lip
- Code: https://github.com/Rudrabha/Wav2Lip

### Photoreal 3D avatars

Codec Avatars, Gaussian head and body avatars, MetaHuman, Personas, NVIDIA ACE: drivable 3D people for XR.

#### Large-scale Codec Avatars (LCA) — Junxuan Li, Meta (2026-04-02)
- Type: Research demo · Timing: Real-time streaming · Access: Research only
- Input: Image, Video → Output: Virtual human (face / body), Gaussian splats / radiance field
- Idea: Applies the foundation-model recipe (pretrain on a million in-the-wild videos, post-train on studio data) to 3D avatars, so diversity of people stops being a capture bottleneck.
- What it is: LCA produces a full-body, high-fidelity 3D avatar of almost anyone in a single forward pass, with fine facial expressions and finger-level control, generalizing across hairstyles, clothing and demographics.
- How it works: Pre-training a feed-forward Gaussian avatar model on 1M in-the-wild videos for appearance and geometry priors, then post-training on curated multi-view data for expressivity and fidelity.
- Specs: 1M pretraining videos · full body · feed-forward
- Capability: Situation diversity, Perceptual realism, Experimental control
- Paper: https://arxiv.org/abs/2604.02320 (CVPR 2026)
- Video: https://www.youtube.com/watch?v=eqFz2GFPIkE
- Project page: https://junxuan-li.github.io/lca

#### Audio2Face-3D — NVIDIA (2025-09-24)
- Type: Open-source tool · Timing: Real-time streaming · Access: Open weights / code
- Input: Speech & audio → Output: Motion / animation, Virtual human (face / body)
- Idea: Gives game-engine NPCs and XR agents an open, inspectable speech-to-face layer that can run beside an LLM and TTS.
- What it is: Audio2Face-3D generates lip sync and facial expression for a rigged 3D character from speech audio in real time, and NVIDIA open-sourced the models, SDK and training framework in September 2025, with plug-ins for Unreal Engine and Maya.
- How it works: Neural networks (regression and diffusion variants) map audio features to facial blendshape or vertex animation plus emotion, part of NVIDIA ACE.
- Capability: Temporal responsiveness, Authoring accessibility
- Paper: https://arxiv.org/abs/2508.16401 (arXiv 2025)
- Video: https://www.youtube.com/watch?v=-l8kjQUTfQk
- Images: https://developer-blogs.nvidia.com/wp-content/uploads/2025/09/NVIDIA-Open-Source-Audio2Face-video-500x282.gif
- Project page: https://developer.nvidia.com/blog/nvidia-open-sources-audio2face-animation-model/
- Code: https://github.com/NVIDIA/Audio2Face-3D

#### Personas (visionOS 26) — Apple (2025-06-09)
- Type: Product / app · Timing: Real-time streaming · Access: Product / app
- Input: Multi-view capture / scan, Body, face & gaze tracking → Output: Virtual human (face / body)
- Idea: The first photoreal self-avatar most XR users actually meet, which makes it the realistic baseline for embodied telepresence studies.
- What it is: A Persona is the 3D likeness of an Apple Vision Pro wearer, created from a quick face scan with the headset and animated live by its eye, face and hand tracking in FaceTime and shared spatial apps; visionOS 26 rebuilt Personas with more realistic hair, skin, eyelashes and side profiles.
- How it works: On-device reconstruction from the headset's front cameras (Apple describes 'volumetric rendering' and machine learning in visionOS 26), driven by internal eye and face cameras.
- Capability: Perceptual realism, Temporal responsiveness
- Video: https://www.youtube.com/watch?v=81bsjbTN88g
- Project page: https://www.apple.com/os/visionos/

#### LAM (Large Avatar Model) — Alibaba Tongyi (Qwen) (2025-02-25)
- Type: Model · Timing: Real-time streaming · Access: Open weights / code
- Input: Image, Speech & audio → Output: Virtual human (face / body), Gaussian splats / radiance field
- Idea: One-shot 3D heads cheap enough for a browser make embodied agents deployable without GPU streaming.
- What it is: LAM turns a single photo into an animatable 3D Gaussian head in one forward pass that runs in real time on phones and in WebGL, and Alibaba pairs it with audio-driven animation for chat avatars.
- How it works: A transformer whose FLAME canonical points query multi-scale image features to predict canonical Gaussian attributes, animated by standard linear blend skinning with corrective blendshapes.
- Capability: Authoring accessibility, Temporal responsiveness
- Paper: https://arxiv.org/abs/2502.17796 (arXiv 2025)
- Video: https://www.youtube.com/watch?v=FrfE3RYSKhk
- Project page: https://aigc3d.github.io/projects/LAM/
- Code: https://github.com/aigc3d/LAM

#### URAvatar — Junxuan Li, Meta (2024-10-31)
- Type: Research demo · Timing: Real-time streaming · Access: Research only
- Input: Video, Multi-view capture / scan → Output: Virtual human (face / body), Gaussian splats / radiance field
- Idea: Brings Codec-Avatar quality from the capture studio to a phone, the step that would let a study include participants' own faces.
- What it is: URAvatar creates a relightable, drivable photoreal head avatar from a phone scan, using a universal prior learned from hundreds of studio-captured people, and renders it in real time under new lighting.
- How it works: A universal relightable Gaussian avatar prior trained on multi-view, multi-light captures; a phone scan is fitted by inverse rendering and fine-tuning the prior.
- Capability: Authoring accessibility, Perceptual realism
- Paper: https://arxiv.org/abs/2410.24223 (SIGGRAPH Asia 2024)
- Video: https://junxuan-li.github.io/urgca-website/static/videos/ica-driving-video_crop.mp4
- Images: https://junxuan-li.github.io/urgca-website/static/images/overview.png
- Project page: https://junxuan-li.github.io/urgca-website/

#### Relightable Gaussian Codec Avatars — Shunsuke Saito, Meta (2023-12-06)
- Type: Research demo · Timing: Real-time streaming · Access: Research only
- Input: Multi-view capture / scan, Body, face & gaze tracking → Output: Virtual human (face / body), Gaussian splats / radiance field
- Idea: Lighting consistency is part of believability: a face that ignores the room's light reads as pasted in.
- What it is: Relightable Gaussian Codec Avatars render a drivable 3D head with individual hair strands, skin pores and eye reflections under any lighting, in real time, so the avatar fits the light of the scene it is placed in.
- How it works: 3D Gaussians attached to a deformable head model with learnable radiance transfer (diffuse spherical-harmonics and spherical-Gaussian specular), plus an explicit eye model, trained on light-stage multi-view capture.
- Capability: Perceptual realism
- Paper: https://arxiv.org/abs/2312.03704 (CVPR 2024 (Oral))
- Video: https://shunsukesaito.github.io/rgca/static/videos/full_video.mp4
- Images: https://shunsukesaito.github.io/rgca/static/images/overview.png
- Project page: https://shunsukesaito.github.io/rgca/

#### GaussianAvatars — Shenhan Qian (2023-12-04)
- Type: Research demo · Timing: Real-time streaming · Access: Open weights / code
- Input: Multi-view capture / scan, Body, face & gaze tracking → Output: Virtual human (face / body), Gaussian splats / radiance field
- Idea: Rigging splats to a standard face model made Gaussian avatars drivable by the same parameters games and trackers already use.
- What it is: GaussianAvatars builds a photoreal 3D head from multi-view video by binding 3D Gaussians to a FLAME face mesh, so the head can be re-animated with new expressions and poses and rendered in real time from any viewpoint.
- How it works: 3D Gaussians parented to FLAME mesh triangles, moving with them, with binding inheritance during densification, optimized jointly with FLAME parameters on multi-view video.
- Capability: Perceptual realism, Experimental control
- Paper: https://arxiv.org/abs/2312.02069 (CVPR 2024)
- Video: https://www.youtube.com/watch?v=lVEY78RwU_I
- Project page: https://shenhanqian.github.io/gaussian-avatars
- Code: https://github.com/ShenhanQian/GaussianAvatars

#### MetaHuman Animator — Epic Games (2023-06-15)
- Type: Product / app · Timing: Pre-generated · Access: Product / app
- Input: Video, Body, face & gaze tracking → Output: Motion / animation, Virtual human (face / body)
- Idea: Performance capture for everyone, the authored-but-recorded route to believable virtual-human behaviour.
- What it is: MetaHuman Animator turns an actor's performance filmed on an iPhone or stereo head-mounted camera into high-fidelity facial animation on any MetaHuman within minutes; later versions add animation from a webcam or from audio alone, and Unreal Engine 5.8 (2026) adds markerless body capture of one actor from a single webcam or phone camera.
- How it works: A 4D solver fits a person-specific MetaHuman identity from a few frames, then tracks the captured video and depth to transfer the performance onto the standard facial rig.
- Capability: Perceptual realism, Authoring accessibility
- Video: https://www.youtube.com/watch?v=bIGnx2jvrbg
- Project page: https://www.metahuman.com/

#### MetaHuman Creator — Epic Games (2021-02-10)
- Type: Product / app · Timing: Real-time streaming · Access: Product / app
- Input: Scene spec, code & rules, Multi-view capture / scan → Output: Virtual human (face / body), Mesh / 3D asset
- Idea: The non-generative baseline: authored, rigged, controllable humans whose every parameter can be logged, which generative avatars still struggle to match on control.
- What it is: MetaHuman Creator lets anyone design a realistic, fully rigged digital human in minutes by blending scanned faces and adjusting skin, hair and body, ready to animate in Unreal Engine; since Unreal Engine 5.6 (2025) it runs inside the engine and accepts mesh or scan input.
- How it works: Parametric blending over a database of scanned faces and bodies (from 3Lateral and Cubic Motion), with a standard facial rig and LODs for real-time rendering.
- Capability: Authoring accessibility, Perceptual realism, Experimental control
- Video: https://www.youtube.com/watch?v=OeUBATSJSr0
- Project page: https://www.metahuman.com/

#### Codec Avatars — Meta (2019-03)
- Type: Research demo · Timing: Real-time streaming · Access: Research only
- Input: Body, face & gaze tracking, Multi-view capture / scan → Output: Virtual human (face / body)
- Idea: Set the target that later Gaussian, phone-scan and feed-forward avatars chase: telepresence where a face is encoded, sent and decoded like a codec.
- What it is: Codec Avatars are Meta's photorealistic 3D avatars of real people, captured in multi-camera studios and driven live by cameras inside a VR headset, so two people in headsets see each other's faces in 3D. The best-known public demonstration was the 2023 Lex Fridman interview with Mark Zuckerberg held entirely between Codec Avatars.
- How it works: A deep appearance model (variational autoencoder) learns a person-specific latent code of face geometry and view-dependent texture from studio capture; headset cameras regress the code in real time and a decoder renders it.
- Capability: Perceptual realism, Temporal responsiveness
- Paper: https://doi.org/10.1145/3197517.3201401 (ACM TOG (SIGGRAPH 2018))
- Video: https://www.youtube.com/watch?v=MVYrJJNdrEg
- Project page: https://tech.facebook.com/reality-labs/2019/3/codec-avatars-facebook-reality-labs/

### Listening, gesture & dyadic behaviour

Models of backchannels, gaze, gesture and turn-taking between two people.

#### Sparrow-2 — Tavus (2026-08-27)
- Type: Model · Timing: Turn-based · Access: Public API
- Input: Speech & audio → Output: Agent behaviour & actions
- Idea: Conversational timing is now a measurable model output with its own benchmark, which makes response latency something an experiment can set.
- What it is: Sparrow-2 is Tavus' turn-taking model: it decides every 10 ms whether a voice or video agent should listen, wait or speak, distinguishing a thinking pause from the end of a turn and real interruptions from background noise. Tavus reports it leads the TurnBench benchmark in end-of-turn (92.4% recall) and interruption detection (97.4% recall).
- How it works: A streaming acoustic-semantic model over the whole audio scene (speaker intent, prosody, environment) that replaces silence timers and VAD endpointing; successor to Sparrow-0 (2025) and Sparrow-1 (January 2026).
- Specs: 10 ms decision frame · TurnBench end-of-turn recall 92.4% · interruption recall 97.4%
- Capability: Temporal responsiveness, Behavioral plausibility
- Video: https://www.youtube.com/watch?v=E7MjlfJQkJM
- Images: https://cdn.prod.website-files.com/68c8e57d6e512b9573db147f/6a8ff14fd7938137631903b7_download%20(2).avif
- Project page: https://www.tavus.io/blog/sparrow-2
- API docs: https://docs.tavus.io

#### VideoFDB — NVIDIA (2026-05-28)
- Type: Dataset / benchmark · Timing: Full-duplex · Access: Open weights / code
- Input: Video, Speech & audio → Output: Dialogue / text, Virtual human (face / body)
- Idea: Gives full-duplex virtual humans a shared yardstick with a human reference score, so vendor claims can be compared.
- What it is: VideoFDB is the first benchmark for full-duplex audio-visual-to-audio-visual conversational agents: 237 expert-annotated dyadic clips from real video calls covering 11 nonverbal dynamics, scored separately for perception (does the agent read the moment) and generation (does it respond with fitting speech, gaze and expression), with a public leaderboard.
- How it works: Clips from natural video calls annotated with a taxonomy that separates perception from generation behaviours, scored by a rubric-based LM-as-judge on fluency, affect matching, nonverbal fit and timing.
- Specs: 237 clips · 11 nonverbal dynamics · human reference 3.92
- Capability: Temporal responsiveness, Experimental control
- Paper: https://arxiv.org/abs/2605.30256 (arXiv 2026)
- Images: https://research.nvidia.com/labs/amri/projects/video-fdb/og/videofdb-sunburst.png
- Project page: https://research.nvidia.com/labs/amri/projects/video-fdb/
- Code: https://huggingface.co/datasets/nvidia/video-full-duplex-benchmark

#### Raven-1 — Tavus (2026-02-10)
- Type: Model · Timing: Real-time streaming · Access: Public API
- Input: Video, Speech & audio → Output: Dialogue / text, Agent behaviour & actions
- Idea: Perception of the human becomes a separate, swappable model whose outputs could be logged as a record of what the agent 'saw'.
- What it is: Raven-1 is Tavus' multimodal perception model for live conversation: it fuses the user's tone, facial expression, gaze, posture and hesitation into running natural-language descriptions that the agent's LLM reads, so a flat 'fine' and a cheerful 'fine' lead to different replies.
- How it works: Unified audio-visual fusion producing LLM-readable descriptions rather than emotion labels, with rolling updates so context is never more than about 300 ms stale.
- Specs: audio descriptions <100 ms · context ≤300 ms stale · pipeline <600 ms
- Capability: Reactivity, Temporal responsiveness
- Video: https://www.youtube.com/watch?v=GH9-EmgtABw
- Images: https://cdn.prod.website-files.com/68c8e57d6e512b9573db147f/698ac479d3b6b3e85ef6cb96_processed-image%20(97).avif
- Project page: https://www.tavus.io/blog/raven-1-bringing-emotional-intelligence-to-artificial-intelligence
- API docs: https://docs.tavus.io

#### Avatar Forcing — Taekyung Ki (2026-01-02)
- Type: Research demo · Timing: Real-time streaming · Access: Open weights / code
- Input: Speech & audio, Video, Image → Output: Virtual human (face / body)
- Idea: Conditioning on the user's motion, not only audio, lets a portrait avatar react to what a participant does without speaking.
- What it is: Avatar Forcing animates a head avatar that reacts in real time to the user's voice and visible behaviour (speech, nods, laughter) as well as its own speech, with about 500 ms latency on one GPU.
- How it works: Diffusion forcing over motion latents with causal, real-time multimodal conditioning on user audio and motion, plus preference optimization that uses samples with user conditions dropped as negatives.
- Specs: ~500 ms latency · single H100 (14 GB) · 6.8× faster than baseline
- Capability: Reactivity, Temporal responsiveness
- Paper: https://arxiv.org/abs/2601.00664 (CVPR 2026)
- Video: https://www.youtube.com/watch?v=TARPGnJ8GW4
- Project page: https://taekyungki.github.io/AvatarForcing/
- Code: https://github.com/TaekyungKi/AvatarForcing

#### Seamless Interaction — Meta (2025-06-27)
- Type: Dataset / benchmark · Timing: Pre-generated · Access: Open weights / code
- Input: Speech & audio, Video → Output: Motion / animation, Virtual human (face / body)
- Idea: Open, large-scale dyadic data is what full-duplex avatars train and get evaluated on; the 2026 GENEA gesture challenge is built on it.
- What it is: Seamless Interaction is Meta FAIR's dataset of over 4,000 hours of face-to-face conversation from more than 4,000 participants, released with dyadic motion models that generate a speaker's facial expressions and gestures from both people's audio and the other person's visual behaviour, for 2D video or 3D Codec Avatars.
- How it works: Multi-camera recordings of naturalistic and improvised dyadic sessions; audio-visual dyadic motion models (diffusion-based) with controllable emotion and expressivity, optionally driven by LLM speech.
- Specs: 4,000+ hours · 4,000+ participants
- Capability: Behavioral plausibility, Situation diversity, Experimental control
- Paper: https://arxiv.org/abs/2506.22554 (arXiv 2025)
- Images: https://raw.githubusercontent.com/facebookresearch/seamless_interaction/main/assets/banner.gif
- Project page: https://ai.meta.com/research/seamless-interaction/
- Code: https://github.com/facebookresearch/seamless_interaction

#### INFP — ByteDance Seed (2024-12-05)
- Type: Research demo · Timing: Pre-generated · Access: Research only
- Input: Speech & audio, Image → Output: Virtual human (face / body)
- Idea: Removes the manual 'now speak / now listen' switch that most talking heads need, a precondition for natural turn-taking.
- What it is: INFP animates a single portrait in a two-person conversation from both speakers' audio, switching on its own between speaking and listening, with nods, gaze and expressions while the other person talks.
- How it works: Stage 1 learns a low-dimensional motion latent from real conversation video (head imitation); stage 2 maps dual-track audio to those latents with a denoising model; trained on the new DyConv dyadic dataset.
- Capability: Behavioral plausibility, Temporal responsiveness
- Paper: https://arxiv.org/abs/2412.04037 (CVPR 2025)
- Video: https://www.youtube.com/watch?v=6exuYJ393LI
- Images: https://grisoon.github.io/INFP/static/images/task-v3.png
- Project page: https://grisoon.github.io/INFP/

#### Audio2Photoreal — Evonne Ng, Meta (2024-01-03)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code
- Input: Speech & audio → Output: Virtual human (face / body), Motion / animation
- Idea: Shows that photoreal rendering exposes subtle gesture errors that stick figures hide, so behaviour and appearance must be evaluated together.
- What it is: Audio2Photoreal turns the audio of a two-person conversation into the face, body and hand gestures of a photorealistic 3D avatar, including listening behaviour, and renders it with Meta's Codec Avatars.
- How it works: A VQ-transformer predicts guide poses, a diffusion model fills in body motion, and a separate audio-conditioned diffusion model generates face codes, trained on a new multi-view conversational capture dataset.
- Capability: Behavioral plausibility, Perceptual realism
- Paper: https://arxiv.org/abs/2401.01885 (arXiv 2024)
- Video: https://www.youtube.com/watch?v=Y0GMaMtUynQ
- Project page: https://people.eecs.berkeley.edu/~evonne_ng/projects/audio2photoreal/
- Code: https://github.com/facebookresearch/audio2photoreal

#### Learning to Listen — Evonne Ng (2022-04-18)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code
- Input: Speech & audio, Video → Output: Motion / animation, Virtual human (face / body)
- Idea: Treats listening as a generative, non-deterministic behaviour, the missing half of a conversational virtual human.
- What it is: Learning to Listen generates the facial reactions of a listener (nods, smiles, frowns) from the speaker's words, voice and face, producing several plausible listener responses for the same speaker turn.
- How it works: A VQ-VAE codebook of listener motion and a transformer that autoregressively predicts listener codes from multimodal speaker input, trained on in-the-wild dyadic interview video.
- Capability: Behavioral plausibility, Situation diversity
- Paper: https://arxiv.org/abs/2204.08451 (CVPR 2022)
- Video: https://www.youtube.com/watch?v=3CSlKZ5T6DU
- Project page: https://evonneng.github.io/learning2listen/
- Code: https://github.com/evonneng/learning2listen

## Speech, Sound & Spatial Audio

The audio half of audio-visual immersion: full-duplex speech models that can be interrupted, expressive voices, generated sound effects and music, and spatial audio.

### Full-duplex speech & voice agents

Speech-to-speech models that listen while they talk: Moshi, Sesame, GPT realtime, Gemini Live, Hume EVI…

#### Gemini 3.8 Live — Google DeepMind (2026-09-15)
- Type: Model · Timing: Turn-based · Access: Public API
- Input: Speech & audio, Video, Text prompt → Output: Speech / voice, Dialogue / text
- Idea: Background reasoning during speech closes the gap between a fast voice and a smart one, useful for characters that must stay responsive while working through complex scenario logic.
- What it is: Two audio-to-audio models for the Live API, generally available since 15 September 2026: Gemini 3.8 Live for low-latency dialogue and Gemini 3.8 Live Extended Thinking, which reasons in the background during the conversation. Google highlights asynchronous function calls and proactive audio, where the agent speaks only when relevant.
- How it works: Audio-to-audio Gemini models with interleaved reasoning and default asynchronous function calling, succeeding gemini-3.1-flash-live-preview (March 2026).
- Capability: Temporal responsiveness, Reactivity
- Video: https://storage.googleapis.com/gdm-deepmind-com-prod-public/media/SeC1i4kt5pDKGMWX/gemini-audio__demo__multi-tasking.webm
- Project page: https://deepmind.google/models/gemini-audio/
- API docs: https://ai.google.dev/gemini-api/docs/live

#### SeedRealtime — ByteDance Seed (2026-08-05)
- Type: Model · Timing: Full-duplex · Access: Product / app
- Input: Speech & audio, Video → Output: Speech / voice, Dialogue / text
- Idea: Proactive, interference-robust timing in a deployed product: the system decides when to speak from what it sees and hears, not from silence.
- What it is: ByteDance Seed's native audio-visual full-duplex model, which watches, listens and speaks at once, chimes in or pauses at the right moment, and ignores bystander chatter and background noise. Seed reports that it halves conversational pacing problems compared with cascaded systems in human evaluation, and that it is fully rolled out at scale.
- How it works: A unified architecture that natively fuses continuous audio, video and text streams and models the user's conversational state, replacing an external voice-activity detector.
- Capability: Temporal responsiveness, Reactivity
- Video: https://lf3-static.bytednsdoc.com/obj/eden-cn/lapzild-tss/ljhwZthlaukjlkulzlp/user-upload/4xfa4msff67ew.mp4
- Project page: https://seed.bytedance.com/en/blog/seedrealtime-audio-visual-full-duplex-llm-released-toward-omni-modal-natural-interaction

#### GPT-Live — OpenAI (2026-07-08)
- Type: Model · Timing: Full-duplex · Access: Product / app, Public API
- Input: Speech & audio → Output: Speech / voice, Dialogue / text
- Idea: OpenAI's own break with turn-based voice: the mainstream ChatGPT voice now overlaps and backchannels, so full-duplex timing is no longer a research-only property.
- What it is: A full-duplex voice model that now powers ChatGPT Voice: it listens while it speaks, says 'mhmm' or 'yeah' to show attention and can stay quiet while the user thinks. Harder requests are handed to a frontier model (GPT-5.5 at launch) in the background while the conversation continues. GPT-Live-1 became generally available in the API on 10 September 2026, and GPT-Live-1.1 (15 October 2026) added voices and accents in ChatGPT.
- How it works: Full-duplex architecture that processes input continuously while generating output, with background delegation to a reasoning model; outputs carry SynthID watermarks since 31 July 2026.
- Specs: GPT-Live-1 and GPT-Live-1 mini · ChatGPT · API GA 2026-09-10 (v1/live/sessions)
- Capability: Temporal responsiveness, Behavioral plausibility
- Video: https://www.youtube.com/watch?v=EAN5Cj347PY
- Images: https://images.ctfassets.net/kftzwdyauwt9/54glGpDpS58mKdx6Y3GobW/6ea5121851a36b8cf0505a96be2de994/bidi-art-card_16_9__1_.png?w=1600&h=900&fit=fill
- Project page: https://openai.com/index/introducing-gpt-live/
- API docs: https://developers.openai.com/api/docs/changelog

#### GPT-Realtime-2 — OpenAI (2026-05-07)
- Type: Model · Timing: Turn-based · Access: Public API
- Input: Speech & audio, Text prompt → Output: Speech / voice, Dialogue / text
- Idea: Voice agents that reason and act mid-conversation make multi-step role-play scenarios (a dispatcher, a clerk, a negotiator) feasible over a phone line.
- What it is: OpenAI's first voice model with GPT-5-class reasoning, launched with GPT-Realtime-Translate (live translation from 70+ input into 13 output languages) and GPT-Realtime-Whisper (streaming transcription). It can say short preambles such as 'let me check that', call several tools in parallel and keep the conversation going while it works. GPT-Realtime-2.1 and 2.1 mini (6 July 2026) improved alphanumeric recognition, noise handling and interruption behaviour.
- How it works: Speech-to-speech model with adjustable reasoning effort, preambles and parallel tool calls in the Realtime API; conversation is still segmented into turns.
- Specs: +15.2% Big Bench Audio vs GPT-Realtime-1.5 (OpenAI)
- Capability: Temporal responsiveness, Reactivity
- Video: https://www.youtube.com/watch?v=JOu8v6CBjkE
- Images: https://images.ctfassets.net/kftzwdyauwt9/CtzMayHtxIkcMPAo8BpqJ/966285cf3802995841337122190ec2fd/OAI_GPT-Realtime-2_Art_Card_16x9.png.png?w=1600&h=900&fit=fill
- Project page: https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/
- API docs: https://platform.openai.com/docs/guides/realtime

#### Hibiki-Zero — Kyutai (2026-02-12)
- Type: Model · Timing: Real-time streaming · Access: Open weights / code
- Input: Speech & audio → Output: Speech / voice
- Idea: Live interpretation with voice transfer makes cross-language encounters stageable: a participant hears a foreign-language interlocutor in their own language with a short, natural delay.
- What it is: A simultaneous speech-to-speech translation model that listens to French, Spanish, Portuguese or German and speaks the English translation in the speaker's own voice while they are still talking. It follows Hibiki (February 2025) and no longer needs word-aligned training data.
- How it works: A 3B decoder-only multistream Transformer over Mimi tokens at 12.5 Hz that models source and target speech jointly and adapts its delay to gather just enough context, trained without word-level alignments.
- Specs: 3B · 12.5 Hz · FR/ES/PT/DE → EN · CC BY-NC-SA 4.0
- Capability: Temporal responsiveness, Situational reach
- Paper: https://arxiv.org/abs/2602.11072 (arXiv 2026)
- Video: https://github.com/user-attachments/assets/d533ec45-8d5e-4e41-886a-0b2d198be6f3
- Images: https://opengraph.githubassets.com/645106f5c200b440e2f106671ceaf13e48ac82c921672b8db6c2724e1a6ddc6e/kyutai-labs/hibiki-zero
- Project page: https://kyutai.org/blog/2026-02-12-hibiki-zero/
- Code: https://github.com/kyutai-labs/hibiki-zero

#### MiniCPM-o 4.5 — OpenBMB (2026-02-03)
- Type: Model · Timing: Full-duplex · Access: Open weights / code
- Input: Speech & audio, Video → Output: Speech / voice, Dialogue / text
- Idea: Full-duplex audio-visual conversation small enough for one GPU, so a headset scenario can run its interlocutor offline and version-pinned.
- What it is: A 9B open omni-modal model that watches a live camera stream, listens and speaks at the same time, and can speak up on its own when it notices something. It runs locally through llama.cpp, Ollama and vLLM and clones a voice from a short reference clip.
- How it works: End-to-end assembly of SigLIP2 vision, a Whisper-medium audio encoder, a CosyVoice2 speech decoder and a Qwen3-8B backbone, processing continuous audio-video input and concurrent text-speech output streams without mutual blocking.
- Specs: 9B · full-duplex audio + video · local inference (llama.cpp-omni)
- Capability: Temporal responsiveness, Reactivity
- Paper: https://arxiv.org/abs/2604.27393 (Technical report (arXiv 2026))
- Video: https://www.youtube.com/watch?v=6UzC-O1Q-1U
- Images: https://opengraph.githubassets.com/32a28717382bef321452043efe551d5e3b48d955488f80e319b7355cba3a43eb/OpenBMB/MiniCPM-V
- Project page: https://github.com/OpenBMB/MiniCPM-V
- Code: https://huggingface.co/openbmb/MiniCPM-o-4_5

#### PersonaPlex — NVIDIA (2026-01-15)
- Type: Model · Timing: Full-duplex · Access: Open weights / code
- Input: Speech & audio, Text prompt → Output: Speech / voice, Dialogue / text
- Idea: Removes the trade-off between a configurable persona and full-duplex naturalness, which is what a scripted confederate in a behavioral study needs.
- What it is: An open full-duplex conversational model in which developers pick a voice and define any role in a text prompt (a customer-service agent, an astronaut, a fantasy character) while keeping Moshi-style interruptions, backchannels and conversational rhythm.
- How it works: Moshi's 7B dual-stream architecture with hybrid voice-and-text system prompts, fine-tuned on Fisher conversations relabelled with LLM-written persona descriptions plus synthetic dialogues.
- Specs: 7B · Moshi architecture · open weights
- Capability: Behavioral plausibility, Experimental control
- Paper: https://research.nvidia.com/labs/adlr/files/personaplex/personaplex_preprint.pdf (Preprint 2026)
- Video: https://research.nvidia.com/labs/adlr/files/personaplex/personaplex-intro.mp4
- Images: https://opengraph.githubassets.com/b3ed03a6cecaddba122da6989b7312f8f08ca56a739ca320f413dca7aaff6350/NVIDIA/personaplex
- Project page: https://research.nvidia.com/labs/adlr/personaplex/
- Code: https://github.com/NVIDIA/personaplex

#### Qwen3-Omni — Alibaba Tongyi (Qwen) (2025-09-22)
- Type: Model · Timing: Turn-based · Access: Open weights / code, Public API
- Input: Speech & audio, Video, Image → Output: Speech / voice, Dialogue / text
- Idea: An open model a lab can host that hears and watches the participant and replies in speech: a self-hosted alternative to closed realtime APIs.
- What it is: An open-weight, natively omni-modal model that takes text, images, audio and video and answers in streaming text and natural speech. Alibaba reports open-source state of the art on 32 of 36 audio and audio-visual benchmarks, with 119 text languages, 19 speech-input and 10 speech-output languages.
- How it works: Mixture-of-experts Thinker-Talker design (30B total, 3B active) with an AuT audio encoder and a multi-codebook Talker for streaming speech.
- Specs: 30B-A3B MoE · 234 ms theoretical first-packet latency (Qwen) · 119 / 19 / 10 languages
- Capability: Temporal responsiveness, Situation diversity
- Paper: https://arxiv.org/abs/2509.17765 (Technical report (arXiv 2025))
- Video: https://www.youtube.com/watch?v=_zdOrPju4_g
- Images: https://opengraph.githubassets.com/d43656f30182aae86d2489ca2e28f8912ccf78430f4743f461ca6c3166c2c752/QwenLM/Qwen3-Omni
- Project page: https://github.com/QwenLM/Qwen3-Omni
- Code: https://github.com/QwenLM/Qwen3-Omni

#### gpt-realtime — OpenAI (2025-08-28)
- Type: Model · Timing: Turn-based · Access: Public API
- Input: Speech & audio, Image, Text prompt → Output: Speech / voice, Dialogue / text
- Idea: Made instructible, tool-using voice agents an off-the-shelf API: a scenario author can define a phone-call character in a system prompt.
- What it is: OpenAI's production speech-to-speech model for the Realtime API, released with remote MCP tools, image input and SIP phone calling. It follows spoken style instructions such as 'speak quickly and empathetically', switches languages mid-sentence, and adds the voices Cedar and Marin.
- How it works: One speech-to-speech model served over WebRTC, WebSocket or SIP; turns are segmented by server or semantic voice-activity detection with barge-in.
- Specs: Big Bench Audio 82.8% vs 65.6% for the Dec 2024 model (OpenAI)
- Capability: Temporal responsiveness, Experimental control
- Video: https://www.youtube.com/watch?v=nfBbmtMJhX0
- Images: https://images.ctfassets.net/kftzwdyauwt9/16qATUOZ1GSdE7JHHr0qFG/47b074ae6486a3d8f9ad14adb7812d13/RealtimeAPI_Blog_Open_Graphic_Image__1200x630_.png?w=1600&h=900&fit=fill
- Project page: https://openai.com/index/introducing-gpt-realtime/
- API docs: https://platform.openai.com/docs/guides/realtime

#### Step-Audio 2 — StepFun (2025-07-22)
- Type: Model · Timing: Turn-based · Access: Open weights / code, Public API
- Input: Speech & audio → Output: Speech / voice, Dialogue / text
- Idea: Reads how something is said, not only what is said, which a virtual interlocutor needs to react to a participant's stress or hesitation.
- What it is: StepFun's end-to-end audio language model for spoken conversation that picks up emotion and other paralinguistic cues, switches timbre on spoken request and can search the web mid-conversation. StepFun reports state-of-the-art results on LibriSpeech, MMAU and URO-Bench; the smaller Step-Audio 2 mini is open-weight.
- How it works: Audio encoder plus LLM that generates interleaved text and discrete audio tokens, trained with reasoning-oriented reinforcement learning and retrieval-augmented generation including audio search.
- Capability: Perceptual realism, Adaptation
- Paper: https://arxiv.org/abs/2507.16632 (Technical report (arXiv 2025))
- Video: https://www.youtube.com/watch?v=AAsl0pwbKME
- Images: https://opengraph.githubassets.com/b3e3c4a9bb21755a2be0af80a3424e5bb4422426ffe5ea35b27cd073fdc1bd7e/stepfun-ai/Step-Audio2
- Project page: https://github.com/stepfun-ai/Step-Audio2
- Code: https://github.com/stepfun-ai/Step-Audio2

#### EVI 3 — Hume AI (2025-05-29)
- Type: Model · Timing: Turn-based · Access: Public API, Product / app
- Input: Speech & audio, Text prompt → Output: Speech / voice, Dialogue / text
- Idea: Prompt-designed voices with emotional delivery make it cheap to cast many distinct virtual characters for one study.
- What it is: Hume's third Empathic Voice Interface, a speech-language model that can create a new voice and personality from a text prompt in under a second and then converse in it. In Hume's blind comparison it was rated above GPT-4o on empathy, expressiveness, naturalness, interruption quality and response speed.
- How it works: A single voice-to-voice speech-language model that streams user speech in and produces speech and language together, consulting reasoning models and web search while it talks.
- Capability: Perceptual realism, Adaptation
- Video: https://www.youtube.com/watch?v=SyO7sRtkcRE
- Images: https://cdn.sanity.io/images/xqnc2for/production/282c4a42cdd49007a55031f3e06a2f880373f9bf-2160x2160.png?rect=0,513,2160,1134&w=1200&h=630
- Project page: https://www.hume.ai/blog/introducing-evi-3
- API docs: https://dev.hume.ai/docs/speech-to-speech-evi/overview

#### Unmute — Kyutai (2025-05-22)
- Type: Open-source tool · Timing: Turn-based · Access: Open weights / code, Product / app
- Input: Speech & audio, Text prompt → Output: Speech / voice, Dialogue / text
- Idea: Gives researchers a voice front-end they can put any LLM and persona behind, at the price of turn-taking instead of Moshi-style overlap.
- What it is: A modular voice layer that lets any text LLM listen and speak, combining Kyutai's streaming speech-to-text and text-to-speech with semantic turn detection. At unmute.sh people can talk to it, interrupt it and choose a voice and personality.
- How it works: Cascade of streaming STT with semantic voice-activity detection, any text LLM, and a streaming TTS that starts speaking before the full reply is written; open-sourced in July 2025.
- Capability: Temporal responsiveness, Authoring accessibility
- Video: https://www.youtube.com/watch?v=sRUaYQyX2vw
- Images: https://opengraph.githubassets.com/871275284d27de66853e8b7ea8593ad83e38d94d709d5974ea8ca7996a1291dc/kyutai-labs/unmute
- Project page: https://kyutai.org/blog/2025-05-22-unmute/
- Code: https://github.com/kyutai-labs/unmute

#### Amazon Nova Sonic — Amazon (2025-04-08)
- Type: Model · Timing: Turn-based · Access: Public API
- Input: Speech & audio → Output: Speech / voice, Dialogue / text
- Idea: Brings speech-to-speech agents with tool use into an enterprise cloud, relevant for institutions bound to AWS for data governance.
- What it is: A speech-to-speech foundation model on Amazon Bedrock that streams conversation in both directions, adapts its delivery to the speaker's tone and handles users talking over it. Nova 2 Sonic followed in December 2025.
- How it works: Unified speech understanding and generation model served through Bedrock's bidirectional streaming API with barge-in.
- Capability: Temporal responsiveness, Experimental control
- Video: https://www.youtube.com/watch?v=68HjtdRYkUI
- Images: https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2024/11/20/Bedrock-Nova-feat-img-1260x630.png
- Project page: https://aws.amazon.com/blogs/aws/introducing-amazon-nova-sonic-human-like-voice-conversations-for-generative-ai-applications/
- API docs: https://docs.aws.amazon.com/nova/latest/userguide/speech.html

#### Sesame CSM (Maya & Miles) — Sesame (2025-02-27)
- Type: Model · Timing: Turn-based · Access: Product / app, Open weights / code
- Input: Speech & audio, Text prompt → Output: Speech / voice, Dialogue / text
- Idea: Targets 'voice presence': the conversation so far, not only the text, decides prosody, which is the cue that makes a virtual interlocutor feel present.
- What it is: Sesame's Conversational Speech Model, presented through the voice companions Maya and Miles, which pause, laugh, change tone and correct themselves in ways many listeners found hard to tell from a person. A 1B CSM was released as open weights in March 2025; in 2026 Sesame offers its agents in iOS and Android apps, with eyewear announced.
- How it works: Two autoregressive Transformers over interleaved text and audio tokens (a backbone predicts the first RVQ codebook from conversation history, a small decoder the rest), trained on about one million hours of mostly English audio.
- Specs: Tiny 1B · Small 3B · Medium 8B backbones · CSM-1B open (Apache 2.0)
- Capability: Perceptual realism, Behavioral plausibility
- Video: https://www.youtube.com/watch?v=i1BoLH1r2lU
- Images: https://www.sesame.com/assets/images/og/sesame.jpg
- Project page: https://www.sesame.com/research/crossing_the_uncanny_valley_of_voice
- Code: https://github.com/SesameAILabs/csm

#### Gemini native audio (Live API) — Google DeepMind (2024-12-11)
- Type: Model · Timing: Turn-based · Access: Public API, Product / app
- Input: Speech & audio, Video, Text prompt → Output: Speech / voice, Dialogue / text
- Idea: Lets a voice agent see what the participant's camera sees while it talks: the audio-visual input a headset scenario needs.
- What it is: Gemini 2.0 introduced native audio output and the Multimodal Live API for streaming voice-and-camera conversations; Gemini 2.5 Flash Native Audio (preview from May 2025, updated in September and December 2025) added affective dialogue and proactive audio.
- How it works: Natively multimodal Gemini model that consumes streamed audio and video and emits audio tokens directly, served over a bidirectional WebSocket with voice-activity detection and barge-in.
- Capability: Temporal responsiveness, Reactivity
- Video: https://www.youtube.com/watch?v=qE673AY-WEI
- Images: https://ai.google.dev/static/site-assets/images/share-gemini-api-2026-07.png
- Project page: https://ai.google.dev/gemini-api/docs/live
- API docs: https://ai.google.dev/gemini-api/docs/live

#### Moshi — Kyutai (2024-07-03)
- Type: Model · Timing: Full-duplex · Access: Open weights / code
- Input: Speech & audio → Output: Speech / voice, Dialogue / text
- Idea: The first openly released full-duplex voice model: a lab can run, pin and inspect a conversational partner that overlaps speech like a person instead of waiting for silence.
- What it is: An open speech-text foundation model that listens and speaks at the same time, so it can be interrupted, interject and backchannel in real time. Kyutai demonstrated it live in July 2024 and released weights, code and the paper in September 2024.
- How it works: A 7B Helium text LLM extended with parallel audio streams for the user and the model, tokenised by the streaming Mimi codec at 12.5 Hz, with an 'inner monologue' of time-aligned text tokens.
- Specs: 7B · Mimi codec 12.5 Hz · 160 ms theoretical / ~200 ms practical latency
- Capability: Temporal responsiveness, Behavioral plausibility
- Paper: https://arxiv.org/abs/2410.00037 (Technical report (arXiv 2024))
- Video: https://www.youtube.com/watch?v=hm2IJSKcYvo
- Images: https://opengraph.githubassets.com/c8a1dcee9d391167fc1993e466ce1b5b2a2da00e30da3e390021a0478eea6fbb/kyutai-labs/moshi
- Project page: https://kyutai.org/blog/2024-09-18-moshi-release/
- Code: https://github.com/kyutai-labs/moshi

#### GPT-4o voice (Advanced Voice Mode) — OpenAI (2024-05-13)
- Type: Model · Timing: Turn-based · Access: Product / app, Public API
- Input: Speech & audio, Video → Output: Speech / voice, Dialogue / text
- Idea: Collapsed the speech-to-text, LLM and TTS cascade into one model so that paralinguistic cues survive; OpenAI itself later called it turn-based because it waits for silence.
- What it is: OpenAI's first end-to-end audio model in ChatGPT: it hears tone, answers with emotion, laughter or singing, and stops when interrupted, with OpenAI reporting 320 ms average response time. Shown live in May 2024, it reached ChatGPT as Advanced Voice Mode later that year and developers through the Realtime API beta in October 2024.
- How it works: A single multimodal Transformer trained end-to-end on text, vision and audio; the end of a turn is detected from silence by voice-activity detection.
- Specs: 232 ms min / 320 ms avg audio response (OpenAI)
- Capability: Temporal responsiveness, Perceptual realism
- Video: https://www.youtube.com/watch?v=1uM8jhcqDP0
- Project page: https://openai.com/index/hello-gpt-4o/

#### dGSLM (Generative Spoken Dialogue Language Modeling) — Tu Anh Nguyen, Meta (2022-03-30)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code, Research only
- Input: Speech & audio → Output: Speech / voice
- Idea: Showed that turn-taking, overlap and 'mm-hm' can be learned from raw two-channel audio: the conceptual ancestor of full-duplex voice agents.
- What it is: A textless model that generates two-channel spoken dialogue directly from audio, including overlapping speech, laughter and backchannels between two speakers. Given the start of a real conversation, it continues both sides as audio.
- How it works: Discrete HuBERT units per speaker channel, modelled by a dual-tower Transformer with cross-attention and trained on about 2,000 hours of Fisher telephone conversations.
- Specs: 2 audio channels · ~2,000 h training audio
- Capability: Behavioral plausibility, Temporal responsiveness
- Paper: https://arxiv.org/abs/2203.16502 (TACL 2023)
- Images: https://speechbot.github.io/dgslm/figure.png
- Project page: https://speechbot.github.io/dgslm/
- Code: https://github.com/facebookresearch/fairseq/tree/main/examples/textless_nlp/dgslm

### Expressive voice & cloning

Text-to-speech with emotion, timing and voice design; cloning a voice from seconds of audio.

#### Eleven v4 — ElevenLabs (2026-09-28)
- Type: Model · Timing: Pre-generated · Access: Public API, Product / app
- Input: Text prompt → Output: Speech / voice
- Idea: Acting direction and inline sound cues in one pass blur the line between a voice line and a small sound scene.
- What it is: ElevenLabs' 2026 text-to-speech generation, with a new architecture, a Turbo variant for low-latency agents, one voice across many languages and more consistent voice cloning. ElevenLabs says it follows inline direction such as [laughs], [said angrily in French accent] or sound cues like [light rain] more accurately than v3.
- How it works: New TTS architecture (unpublished) with a separate Turbo model for real-time use; follows audio tags and direction prompts.
- Specs: v4 + v4 Turbo
- Capability: Perceptual realism, Authoring accessibility
- Video: https://www.youtube.com/watch?v=th_tXR2QQ6U
- Images: https://eleven-public-cdn.elevenlabs.io/payloadcms/3o2hqbr4pb7-1920x1080.webp
- Project page: https://elevenlabs.io/blog/eleven-v4
- API docs: https://elevenlabs.io/docs

#### TADA — Hume AI (2026-03-10)
- Type: Model · Timing: Pre-generated · Access: Open weights / code
- Input: Text prompt, Speech & audio → Output: Speech / voice
- Idea: Guaranteed text fidelity matters in experiments: a stimulus voice that never drops or invents a word is a controllable stimulus.
- What it is: An open-source speech-language model from Hume that aligns text and audio one-to-one, so by construction it cannot skip or hallucinate words. Hume reports a real-time factor of 0.09, more than five times faster than comparable LLM-based TTS.
- How it works: Llama-based 1B (English) and 3B (multilingual) models over a tokenizer running at 2-3 audio frames per second with text-acoustic dual alignment.
- Specs: 1B / 3B · RTF 0.09 · 2-3 tokens per second of audio
- Capability: Experimental control, Temporal responsiveness
- Paper: https://arxiv.org/abs/2602.23068 (arXiv 2026)
- Video: https://www.youtube.com/watch?v=eT5c_nsAO_Q
- Images: https://cdn.sanity.io/images/xqnc2for/production/05620681ef774dc41236f42520a269829e11851a-4800x2520.png?w=1200&h=630
- Project page: https://www.hume.ai/blog/opensource-tada
- Code: https://github.com/HumeAI/tada

#### Eleven v3 — ElevenLabs (2025-06)
- Type: Model · Timing: Pre-generated · Access: Public API, Product / app
- Input: Text prompt → Output: Speech / voice
- Idea: Turns a script into an acted scene with interruptions and emotions, lowering the cost of recording varied voiced stimuli.
- What it is: ElevenLabs' most expressive text-to-speech model at its launch, directed with inline audio tags such as [whispers], [sighs] or [excited] and able to render multi-speaker dialogue in 70+ languages. Released as an alpha in June 2025, it became generally available on 2 February 2026.
- How it works: A new TTS architecture (details unpublished) that interprets text context and bracketed audio tags to control emotion, delivery and non-verbal sounds.
- Specs: 70+ languages · multi-speaker dialogue
- Capability: Perceptual realism, Authoring accessibility
- Video: https://www.youtube.com/watch?v=zv_IoWIO5Ek
- Images: https://eleven-public-cdn.elevenlabs.io/payloadcms/xffpzuby3yb-cover.webp
- Project page: https://elevenlabs.io/blog/eleven-v3
- API docs: https://elevenlabs.io/docs

#### IndexTTS2 — bilibili (2025-06-23)
- Type: Model · Timing: Pre-generated · Access: Open weights / code
- Input: Text prompt, Speech & audio → Output: Speech / voice
- Idea: Duration control lets generated speech land on exact timestamps, essential when speech must sync with generated video or a scripted VR event.
- What it is: An open zero-shot TTS model from bilibili's Index team that clones a voice from a short sample, controls emotion separately from timbre and can fix the exact duration of the output, the combination dubbing needs. Its demos re-voice film and animation clips in Chinese and English.
- How it works: Autoregressive text-to-semantic Transformer with explicit token-count duration control and disentangled speaker and emotion prompts, followed by a semantic-to-mel model and vocoder.
- Capability: Experimental control, Perceptual realism
- Paper: https://arxiv.org/abs/2506.21619 (arXiv 2025)
- Video: https://index-tts.github.io/index-tts2.github.io/ex6/Let_the_Bullets_Fly_1.mp4
- Project page: https://index-tts.github.io/index-tts2.github.io/
- Code: https://github.com/index-tts/index-tts

#### Octave — Hume AI (2025-02-26)
- Type: Model · Timing: Pre-generated · Access: Public API, Product / app
- Input: Text prompt → Output: Speech / voice
- Idea: Voice design by description lets an experimenter specify a character ('a nervous young paramedic') instead of searching a stock voice library.
- What it is: Hume's LLM-based text-to-speech, which infers how a line should be delivered from the script (whispering a secret, shouting in triumph) and creates new voices from a text description. Octave 2 later extended it to more languages.
- How it works: A speech-language model trained to understand and synthesise speech, predicting tune, rhythm and timbre from text, acting instructions and context.
- Capability: Perceptual realism, Authoring accessibility
- Video: https://www.youtube.com/watch?v=rKcgsg0HBlY
- Images: https://cdn.sanity.io/images/xqnc2for/production/9b31d5726693ff81fd8347008940845ea7824338-1080x1080.png?rect=0,257,1080,567&w=1200&h=630
- Project page: https://www.hume.ai/blog/octave-the-first-text-to-speech-model-that-understands-what-its-saying
- API docs: https://dev.hume.ai/docs/text-to-speech-tts/overview

### Sound effects, music & video-to-audio

Generated foley, ambience, music and soundtracks matched to video.

#### Seed Audio 1.0 — ByteDance Seed (2026-07-20)
- Type: Model · Timing: Pre-generated · Access: Public API
- Input: Text prompt → Output: Sound, music & spatial audio, Speech / voice
- Idea: Generates the sound scene rather than separate clips, which is closer to how an immersive situation is actually heard.
- What it is: ByteDance Seed's scene-level audio creation model that generates speech, sound effects, ambience and background texture together from one prompt, so a line of dialogue arrives with its room tone, footsteps and alarms already in place. It is available through BytePlus.
- How it works: A unified generative framework that models the speech, effects and ambience of one scene jointly (architecture unpublished).
- Capability: Authoring accessibility, Perceptual realism
- Video: https://lf3-static.bytednsdoc.com/obj/eden-cn/lapzild-tss/ljhwZthlaukjlkulzlp/user-upload/4xfa4mrsklaag.mp4
- Project page: https://seed.bytedance.com/en/blog/from-speech-to-audio-creation-introducing-the-seed-audio-1-0-audio-creation-model

#### Suno v5.5 — Suno (2026-03-26)
- Type: Model · Timing: Pre-generated · Access: Product / app
- Input: Text prompt, Speech & audio → Output: Sound, music & spatial audio
- Idea: Personal voice and style models move music generation from generic tracks toward a person's own sonic identity.
- What it is: The 2026 version of Suno's song generator, which adds Voices (singing in your own recorded voice), custom models tuned to a creator's catalogue and a taste profile. It follows Suno v5 (September 2025).
- How it works: Proprietary song-generation model (likely a Transformer over audio tokens) with voice cloning and per-user model customisation.
- Capability: Authoring accessibility, Co-creation & agency
- Video: https://www.youtube.com/watch?v=eVlFcpX1VGA
- Images: https://suno.com/blog/v5-5/opengraph-image?4a0be6b3238f1ddc
- Project page: https://suno.com/blog/v5-5

#### Lyria 3 — Google DeepMind (2026-02-18)
- Type: Model · Timing: Pre-generated · Access: Product / app, Public API
- Input: Text prompt, Image → Output: Sound, music & spatial audio
- Idea: Image-to-music lets a soundtrack be derived from how a scene looks, keeping score and setting consistent.
- What it is: Google DeepMind's 2026 music model with vocals, launched in the Gemini app on 18 February 2026, followed by Lyria 3 Pro for full-length songs (25 March 2026) and Lyria 3.5 (generally available 3 September 2026). It accepts text and image prompts, and all outputs carry SynthID watermarks.
- How it works: Generative music model with vocals (architecture unpublished), exposed as 30-second clip and full-song variants; outputs are SynthID-watermarked.
- Specs: 48 kHz stereo (Lyria 3 API) · 44.1 kHz stereo (Lyria 3.5)
- Capability: Authoring accessibility, Perceptual realism
- Video: https://www.youtube.com/watch?v=Op8X8RmiE98
- Images: https://storage.googleapis.com/gweb-uniblog-publish-prod/images/0217_KeywordHeaderFinalc.width-1300.png
- Project page: https://blog.google/innovation-and-ai/products/gemini-app/lyria-3
- API docs: https://ai.google.dev/gemini-api/docs/music-generation

#### Stable Audio 2.5 — Stability AI (2025-09-10)
- Type: Model · Timing: Pre-generated · Access: Public API, Product / app
- Input: Text prompt → Output: Sound, music & spatial audio
- Idea: Fast sound design with open siblings makes it a version-pinnable option for reproducible stimulus production.
- What it is: Stability AI's enterprise model for music and sound design, which Stability says generates tracks of up to three minutes in under two seconds on a GPU and supports audio inpainting. The open Stable Audio Open (2024) and the Stable Audio 3 family (May 2026, small and medium music and SFX models on Hugging Face) give labs downloadable alternatives.
- How it works: Latent diffusion Transformer with adversarial relativistic-contrastive (ARC) post-training for few-step sampling, trained on licensed data.
- Specs: up to 3 min of audio in < 2 s (Stability)
- Capability: Authoring accessibility, Experimental control
- Video: https://www.youtube.com/watch?v=zlldXbV72SM
- Images: http://static1.squarespace.com/static/6213c340453c3f502425776e/62f2452bc121595f4d87c713/68af30c1f7616137793f399f/1765490304733/StableAudio2.5_Thumbnail_1x1_v5+%281%29.png?format=1500w
- Project page: https://stability.ai/news/stability-ai-introduces-stable-audio-25-the-first-audio-model-built-for-enterprise-sound-production-at-scale
- Code: https://huggingface.co/stabilityai/stable-audio-3-medium

#### HunyuanVideo-Foley — Tencent Hunyuan (2025-08)
- Type: Model · Timing: Pre-generated · Access: Open weights / code
- Input: Video, Text prompt → Output: Sound, music & spatial audio
- Idea: Balances what the text asks for with what the video shows, so a sound designer can steer a scene's foley with a prompt.
- What it is: Tencent Hunyuan's open text-video-to-audio model that generates high-fidelity foley and ambience matched to the picture. Its demo page compares it side by side with MMAudio, FoleyCrafter and ThinkSound on the same clips.
- How it works: Multimodal diffusion Transformer with joint audio-video attention and text cross-attention, representation alignment to self-supervised audio features, trained on a large automatically curated dataset.
- Capability: Perceptual realism, Experimental control
- Paper: https://arxiv.org/abs/2508.16930 (arXiv 2025)
- Video: https://texttoaudio-train-1258344703.cos.ap-guangzhou.myqcloud.com/hunyuanvideo-foley_demo/demo_show/1-1.mp4
- Images: https://opengraph.githubassets.com/4837e51d5700901b7328e37eca87975e75c4648e45fdbd4bfb31c6d00d89539f/Tencent-Hunyuan/HunyuanVideo-Foley
- Project page: https://szczesnys.github.io/hunyuanvideo-foley/
- Code: https://github.com/Tencent-Hunyuan/HunyuanVideo-Foley

#### Eleven Music — ElevenLabs (2025-08-05)
- Type: Model · Timing: Pre-generated · Access: Public API, Product / app
- Input: Text prompt → Output: Sound, music & spatial audio
- Idea: Licensed, editable music generation reduces rights risk for stimuli that will be published with a study.
- What it is: ElevenLabs' music model that generates studio-grade songs with or without vocals from a prompt, with section-by-section editing and multilingual lyrics; ElevenLabs says it is cleared for commercial use through licensing deals with music rights holders. Music v2 and Music v2.5 (11 September 2026) followed.
- How it works: Text-to-music model with structure-level control over sections, lyrics and style (architecture unpublished).
- Capability: Authoring accessibility, Experimental control
- Video: https://www.youtube.com/watch?v=VDwTSuKbrg8
- Images: https://eleven-public-cdn.elevenlabs.io/payloadcms/qoyke7g9a6g-image%20(44).webp
- Project page: https://elevenlabs.io/blog/eleven-music-is-here
- API docs: https://elevenlabs.io/docs

#### Lyria RealTime — Google DeepMind (2025-05)
- Type: Model · Timing: Real-time streaming · Access: Public API, Product / app
- Input: Text prompt → Output: Sound, music & spatial audio
- Idea: An adaptive score: music that changes with the scene as it unfolds rather than a track picked from a playlist.
- What it is: A music model that produces a continuous stream of music which people steer live by blending and re-weighting text prompts, used in MusicFX DJ and offered in the Gemini API. Its open counterpart, Magenta RealTime, can run locally.
- How it works: Generates music chunk by chunk, conditioned on the preceding audio and on weighted, changeable text prompts (details largely unpublished; Magenta RealTime, the open counterpart, likely uses the same streaming scheme).
- Capability: Temporal responsiveness, Co-creation & agency
- Video: https://storage.googleapis.com/gdm-deepmind-com-prod-public/media/media/lyria_realtime_header.mp4
- Project page: https://deepmind.google/models/lyria/lyria-realtime/
- API docs: https://ai.google.dev/gemini-api/docs/music-generation

#### MMAudio — Ho Kei Cheng (2024-12)
- Type: Model · Timing: Pre-generated · Access: Open weights / code
- Input: Video, Text prompt → Output: Sound, music & spatial audio
- Idea: Fast, open foley lets a pipeline give every generated clip plausible sound, though it does not produce intelligible speech or structured music.
- What it is: An open video-to-audio model that adds synchronised sound effects and ambience to silent video; the authors report about 1.2 seconds to generate audio for an 8-second clip with the smallest model. It became a widely used open baseline for foley generation.
- How it works: Flow-matching multimodal Transformer trained jointly on video-audio and large text-audio data, with a synchronisation module that aligns audio with video frame features.
- Specs: 157M-1.03B parameters · 8 s audio in ~1.2 s (small model, authors)
- Capability: Perceptual realism, Situation diversity
- Paper: https://arxiv.org/abs/2412.15322 (CVPR 2025)
- Video: https://www.youtube.com/watch?v=YElewUT2M4M
- Images: https://opengraph.githubassets.com/9338427bbd0a4344c8597ed9e14235a566d9f7d523bd22ebe5ebc26f20250eaa/hkchengrex/MMAudio
- Project page: https://hkchengrex.github.io/MMAudio
- Code: https://github.com/hkchengrex/MMAudio

#### V2A (video-to-audio) — Google DeepMind (2024-06-17)
- Type: Research demo · Timing: Pre-generated · Access: Research only
- Input: Video, Text prompt → Output: Sound, music & spatial audio, Speech / voice
- Idea: Sound that follows the picture frame by frame turns a silent generated clip into an audiovisual event.
- What it is: Google DeepMind's video-to-audio research that generates soundtracks, sound effects and even dialogue for silent video, steered by optional positive and negative text prompts.
- How it works: Diffusion model that refines audio from noise conditioned on encoded video frames and text, trained with AI-generated sound annotations and dialogue transcripts; output watermarked with SynthID.
- Capability: Perceptual realism, Authoring accessibility
- Video: https://www.youtube.com/watch?v=9Q0-t8D9XFI
- Project page: https://deepmind.google/discover/blog/generating-audio-for-video/

### Spatial & ambisonic audio

Sound placed and rendered in 3D space, generated or upmixed for headsets.

#### ViSAGe — Jaeyeon Kim (2025-06-13)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code, Research only
- Input: Video, Camera path / pose → Output: Sound, music & spatial audio
- Idea: Head-trackable spatial sound for video: the step from a stereo soundtrack to audio that belongs to a 3D scene in a headset.
- What it is: Generates first-order ambisonic sound from a silent field-of-view video and its camera direction, so sound sources stay where they are on screen when the listener turns. The authors also release YT-Ambigen, a dataset of about 102K YouTube clips with ambisonic audio.
- How it works: Codec-based autoregressive generation of ambisonic channels conditioned on CLIP video features, patch-wise energy maps and camera direction, with new spatial-audio evaluation metrics.
- Specs: first-order ambisonics (4 channels)
- Capability: Perceptual realism, Experimental control
- Paper: https://arxiv.org/abs/2506.12199 (ICLR 2025)
- Video: https://www.youtube.com/watch?v=awUvswKbNyQ
- Project page: https://jaeyeonkim99.github.io/visage/

#### OmniAudio — Huadai Liu (2025-04-21)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code, Research only
- Input: Video → Output: Sound, music & spatial audio
- Idea: Pairs naturally with generated 360° video: turns a watched panorama into a place that is also spatially audible.
- What it is: Generates first-order ambisonics from 360° video, so the soundscape of a panoramic clip matches what surrounds the viewer in every direction. The authors built Sphere360, a dataset of over 103,000 real 360° clips with spatial audio.
- How it works: Self-supervised flow-matching pre-training on spatial and non-spatial audio, followed by dual-branch conditioning on panoramic and field-of-view video features.
- Specs: first-order ambisonics · Sphere360 103K clips
- Capability: Perceptual realism, Situational reach
- Paper: https://arxiv.org/abs/2504.14906 (ICML 2025)
- Video: https://www.youtube.com/watch?v=Bg1xqWy0ugs
- Images: https://opengraph.githubassets.com/a2469ea8c177f6d51c3aaafca025bf2971cf0717b6912d3d141e00bc591ac654/liuhuadai/OmniAudio
- Project page: https://github.com/liuhuadai/OmniAudio
- Code: https://github.com/liuhuadai/OmniAudio

#### Both Ears Wide Open (BEWO) — Peiwen Sun (2024-10-14)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code, Research only
- Input: Text prompt, Image → Output: Sound, music & spatial audio
- Idea: Text control over where a sound is and how it moves lets authors script spatial cues for a VR scene without a sound engine.
- What it is: Generates binaural spatial audio from a text description, placing and moving sound sources as written (e.g. a dog barking on the left that runs to the right), and also accepts image prompts. The authors release BEWO-1M, about one million text-spatial audio pairs.
- How it works: SpatialSonic, a one-stage latent diffusion model guided by spatial-aware text and image encoders and azimuth-state conditioning, trained on BEWO-1M.
- Specs: binaural stereo · BEWO-1M dataset
- Capability: Experimental control, Authoring accessibility
- Paper: https://arxiv.org/abs/2410.10676 (ICLR 2025)
- Images: https://peiwensun2000.github.io/bewo/static/I2A_audios/image_001.jpg
- Project page: https://peiwensun2000.github.io/bewo/
- Code: https://github.com/PeiwenSun2000/Both-Ears-Wide-Open

#### Sounding Bodies — Xudong Xu, Meta (2023-11-01)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code, Research only
- Input: Body, face & gaze tracking, Speech & audio → Output: Sound, music & spatial audio
- Idea: Spatially correct body sound is what makes a co-present avatar sound co-present; this model ties it to tracked pose.
- What it is: Renders the full 3D sound field produced by a human body (speech, footsteps, claps, finger snaps) from headset microphone audio and tracked body pose, so a virtual person sounds right from any listening position. Developed with Meta Reality Labs Research.
- How it works: Neural network that maps head-mounted microphone signals and 3D body pose to the sound field around the body, trained on multi-view captures recorded with a large spherical microphone array.
- Capability: Perceptual realism, Behavioral plausibility
- Paper: https://arxiv.org/abs/2311.06285 (NeurIPS 2023)
- Images: https://opengraph.githubassets.com/041b4f76c06e31a7107b494fd5503ebe36ad06f5021380c741bc640d600a9a6c/facebookresearch/SoundingBodies
- Project page: https://github.com/facebookresearch/SoundingBodies
- Code: https://github.com/facebookresearch/SoundingBodies

## Interactive World Models

Action-conditioned models that generate the next moment of a world in response to keyboard, controller or agent input: Genie and its peers. Playable, though persistence, control and headset support are still open problems.

### General world models

Promptable, playable worlds from text or an image: Genie 3, Project Genie, GWM-1, Mirage, Odyssey, Matrix-Game, Hunyuan-GameCraft…

#### Agora-2 — Odyssey (2026-09)
- Type: Model · Timing: Real-time streaming · Access: Waitlist / early access
- Input: Keyboard & controller actions → Output: Interactive frame stream, Agent behaviour & actions
- Idea: A shared generated world is the precondition for social situations; Agora-2 shows it working, but in one game's visual world.
- What it is: A playable research preview of a multi-agent world model in which up to 20 humans and AI agents share one generated world in real time, each participant's actions changing what the others see; it was trained on Diablo II gameplay captures.
- How it works: A world model trained on Diablo II captures that pair observations with actions and game state, predicting a shared state from many participants' simultaneous actions; it extends Agora-1 (May 2026) to 5× more participants and multiple environments.
- Specs: up to 20 participants · real-time (developer-reported)
- Capability: Co-creation & agency, Persistence, Behavioral plausibility
- Video: https://framerusercontent.com/assets/ZfcIM6TLKcPbbzfURMa87Lo6ww.mp4
- Images: https://framerusercontent.com/assets/G8pOTIjyosApbiNbN1y31BVpbM.jpeg
- Project page: https://odyssey.ml/introducing-agora-2
- API docs: https://agora.odyssey.systems

#### PixVerse R2 — PixVerse (2026-09-22)
- Type: Model · Timing: Real-time streaming · Access: Product / app
- Input: Keyboard & controller actions, Text prompt, Speech & audio → Output: Interactive frame stream, Sound, music & spatial audio
- Idea: Consequences that persist inside a running world, plus spoken input, move world models toward interactive scenarios such as interviews.
- What it is: A real-time world model for continuous audiovisual play: users move with WASD, change weather or call in a vehicle by prompt, speak or add references, and the consequences carry forward; PixVerse's own demos include questioning an AI suspect in real time.
- How it works: Movement, prompt, audio and reference inputs at different rates are merged into one continuous generation loop on top of PixVerse's audio-video model.
- Capability: Reactivity, Persistence, Co-creation & agency
- Video: https://www.youtube.com/watch?v=PEGqOLcdVIs
- Images: https://media.pixverse.ai/asset/blog/pixverse-r2-real-time-omni-world-model-cover-v5.webp
- Project page: https://pixverse.ai/en/model/pixverse-r2

#### GWM Worlds 2 — Runway (2026-09-03)
- Type: Model · Timing: Real-time streaming · Access: Waitlist / early access
- Input: Text prompt, Camera path / pose, Image → Output: Interactive frame stream, Sound, music & spatial audio
- Idea: Separates what persists (scene, subjects, rules) from what happens (timestamped events), which is close to how an experimenter would script a situation.
- What it is: A research preview of a playable world model that streams video and sound together; one person can play a character while another 'directs' the scene with text actions addressed to any subject, such as a sword slash, a spoken reply or a room flooding.
- How it works: Built on Runway's audio-video model and driven by 'WorldPrompt': a genesis prompt with scene, subjects and laws, a first frame, a timestamped stream of free-text actions, and per-frame camera input.
- Specs: 720p · 24 fps · 48 kHz audio · no preset session length (developer-reported)
- Capability: Co-creation & agency, Experimental control, Reactivity
- Video: https://www.youtube.com/watch?v=pmjyB-lc4KQ
- Images: https://d3phaj0sisr2ct.cloudfront.net/site/research/gwm-worlds-2/images/gwm-worlds-2-card.webp
- Project page: https://runway.com/research/introducing-gwm-worlds-2

#### LingBot-World 2.0 — Robbyant (2026-07-08)
- Type: Open-source tool · Timing: Real-time streaming · Access: Open weights / code, Product / app
- Input: Text prompt, Keyboard & controller actions, Image → Output: Interactive frame stream, Agent behaviour & actions
- Idea: Pairs a world model with two LLM agents, one acting and one directing, a pattern that maps directly onto confederate and experimenter roles.
- What it is: The second LingBot world model (also called LingBot-World-Infinity), which Robbyant describes as the first hour-long interactive world model: an unbounded interaction horizon, attacks, archery and spell-casting actions, text-driven events, and an agent harness with a 'pilot' agent that plays and a 'director' agent that adds scene elements.
- How it works: Causal pretraining for unbounded rollouts, a distilled real-time variant, and an agentic harness in which a pilot agent plans character behavior and a director agent synthesizes new environmental elements as the scene progresses.
- Specs: 720p · 60 fps real-time variant · hour-long sessions (developer-reported)
- Capability: Persistence, Reactivity, Co-creation & agency
- Paper: https://arxiv.org/abs/2607.07534 (arXiv 2026)
- Video: https://www.youtube.com/watch?v=78l_RW_f12c
- Images: https://raw.githubusercontent.com/Robbyant/lingbot-world-v2/main/assets/teaser.png
- Project page: https://technology.robbyant.com/lingbot-world-v2
- API docs: https://www.reactor.inc/lingbot-world-v2
- Code: https://github.com/Robbyant/lingbot-world-v2

#### Project Genie: Street View grounding — Google DeepMind, Google (2026-05-19)
- Type: Product / app · Timing: Real-time streaming · Access: Product / app, Waitlist / early access
- Input: Image, Text prompt, Keyboard & controller actions → Output: Interactive frame stream
- Idea: Grounds a generated world in a specific real street, which makes place-based scenarios possible, though only as a stylised starting point that drifts as you move.
- What it is: An I/O 2026 update that lets Project Genie start a world from a real place: users drop a Maps pin in the U.S., pick a style such as 'Ocean World' or 'B&W film', describe a character, and Genie builds the world from Street View imagery; access widened the same day to Google AI Ultra subscribers worldwide.
- How it works: Street View imagery retrieved through Google's Maps Imagery Grounding conditions the opening frames, after which Genie 3 continues the world in real time from user actions.
- Specs: U.S. places at launch · global Google AI Ultra rollout (developer-reported)
- Capability: Situational reach, Perceptual realism, Authoring accessibility
- Video: https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/GeoGenie_hero_small_kA4AQO6.mp4
- Images: https://storage.googleapis.com/gweb-uniblog-publish-prod/images/projectgenie-social.width-1300.png
- Project page: https://blog.google/innovation-and-ai/models-and-research/google-deepmind/project-genie-expands/
- API docs: https://labs.google/projectgenie

#### Waypoint-1.5 — Overworld (2026-04-09)
- Type: Open-source tool · Timing: Real-time streaming · Access: Open weights / code, Product / app
- Input: Text prompt, Image, Keyboard & controller actions → Output: Interactive frame stream
- Idea: World models on consumer hardware: a lab can run sessions offline, log them and avoid cloud latency.
- What it is: An open-weight real-time world model that runs locally on gaming PCs or by streaming, turning a prompt or image into an explorable first-person world; it follows Waypoint-1 (January 2026), and a Waypoint 2 beta was inviting builders in October 2026.
- How it works: A real-time diffusion world model with a prompting pipeline that rewrites user input into seed images, synthetic video and aligned controls, released in 720p and 360p tiers for local and streamed play.
- Specs: up to 720p · 60 fps · 1B parameters · consumer GPUs (developer-reported)
- Capability: Temporal responsiveness, Authoring accessibility
- Video: https://www.youtube.com/watch?v=W2vDzB4KvxU
- Images: https://over.world/blog/waypoint-1-5/og.jpg
- Project page: https://over.world/blog/waypoint-1-5
- Code: https://huggingface.co/Overworld/Waypoint-1.5-1B

#### Project Genie — Google DeepMind, Google (2026-01-29)
- Type: Product / app · Timing: Real-time streaming · Access: Product / app, Waitlist / early access
- Input: Text prompt, Image, Keyboard & controller actions → Output: Interactive frame stream
- Idea: Puts a real-time world model in front of paying users for the first time: authoring a world now takes a sentence and a picture, but a session ends after a minute.
- What it is: A Google Labs web prototype, powered by Genie 3, Nano Banana Pro and Gemini, where Google AI Ultra subscribers sketch a world and character from text and images, explore it in first or third person, remix others' worlds and download the result; sessions are capped at 60 seconds.
- How it works: Nano Banana Pro renders a preview image the user can edit ('world sketching'), Gemini likely handles prompt understanding, and Genie 3 then generates the path ahead in real time from the user's movement and camera input.
- Specs: 60 s per generation · U.S. Google AI Ultra, 18+ at launch (developer-reported)
- Capability: Authoring accessibility, Temporal responsiveness, Co-creation & agency
- Video: https://www.youtube.com/watch?v=YxkGdX4WIBE
- Images: https://storage.googleapis.com/gweb-uniblog-publish-prod/images/genie-3__project-genie__hero-film_social-shar.width-1300.jpg
- Project page: https://blog.google/innovation-and-ai/models-and-research/google-deepmind/project-genie/
- API docs: https://labs.google/projectgenie

#### LingBot-World — Robbyant (2026-01-28)
- Type: Open-source tool · Timing: Real-time streaming · Access: Open weights / code
- Input: Image, Text prompt, Keyboard & controller actions → Output: Interactive frame stream
- Idea: An open, minute-horizon world model from a Chinese lab, released the day before Project Genie, which narrowed the gap between open and closed world models.
- What it is: An open-source world simulator from Ant Group's Robbyant that keeps realistic, scientific and cartoon worlds consistent over minute-long interaction and responds in under a second; a hosted demo runs on Reactor.
- How it works: A world model derived from a large video-generation backbone and post-trained for action conditioning, long-term memory and low-latency streaming; later releases added fast and action variants.
- Specs: 16 fps · < 1 s latency · minute-level horizon (developer-reported)
- Capability: Persistence, Temporal responsiveness, Situation diversity
- Paper: https://arxiv.org/abs/2601.20540 (arXiv 2026)
- Video: https://www.youtube.com/watch?v=Hg_giTANYks
- Images: https://raw.githubusercontent.com/Robbyant/lingbot-world/main/assets/teaser.png
- Project page: https://technology.robbyant.com/lingbot-world
- Code: https://github.com/Robbyant/lingbot-world

#### PixVerse R1 — PixVerse (2026-01-12)
- Type: Model · Timing: Real-time streaming · Access: Product / app, Public API
- Input: Text prompt, Image → Output: Interactive frame stream, Sound, music & spatial audio
- Idea: A consumer video app reframed as a live world: the shift from clips to sessions, at the cost of game-level control.
- What it is: PixVerse's first real-time world model, which keeps generating a live audiovisual scene that viewers steer with prompts instead of waiting for a finished clip; later updates added 720p API access for partners, shared worlds and personalised avatars.
- How it works: PixVerse describes three parts: an 'Omni' native multimodal foundation model, autoregressive memory for continuous streaming, and an 'Instantaneous Response Engine' that cuts sampling cost for low latency.
- Specs: 1080p research claim · 720p via partner API (developer-reported)
- Capability: Temporal responsiveness, Persistence
- Video: https://media.pixverse.ai/asset/media/Fig/PixVerse-R1-demo-0.mp4
- Images: https://media.pixverse.ai/asset/media/realtimecover.png
- Project page: https://pixverse.ai/en/blog/pixverse-r1-next-generation-real-time-world-model

#### HY-World 1.5 (WorldPlay) — Tencent Hunyuan (2025-12-17)
- Type: Open-source tool · Timing: Real-time streaming · Access: Open weights / code, Product / app
- Input: Image, Text prompt, Keyboard & controller actions → Output: Interactive frame stream
- Idea: Combines real-time play with long-term geometric memory in an open model, so persistence can be studied rather than taken on trust.
- What it is: An open-source, real-time interactive world model that streams a navigable world from an image or text and keeps its geometry consistent when the user returns to a place; later releases added a lightweight 5B variant, training code and RL post-training (WorldCompass).
- How it works: An autoregressive video model (8B, built on HunyuanVideo) with dual action representation, reconstituted context memory that re-selects past frames by geometry, and context-forcing distillation for real-time speed.
- Specs: 24 fps · 720p · real-time (developer-reported)
- Capability: Persistence, Temporal responsiveness
- Paper: https://arxiv.org/abs/2512.14614 (arXiv 2025)
- Video: https://github.com/user-attachments/assets/9fd12b40-41ab-4201-8667-8b333db1123d
- Images: https://raw.githubusercontent.com/Tencent-Hunyuan/HY-WorldPlay/main/assets/teaser.webp
- Project page: https://3d-models.hunyuan.tencent.com/world/
- Code: https://github.com/Tencent-Hunyuan/HY-WorldPlay

#### GWM-1 — Runway (2025-12-11)
- Type: Model · Timing: Real-time streaming · Access: Waitlist / early access, Public API
- Input: Keyboard & controller actions, Camera path / pose, Speech & audio → Output: Interactive frame stream, Virtual human (face / body)
- Idea: One video backbone serves places, people and robots, which hints at a single model for a whole situation, though the variants are still separate models.
- What it is: Runway's first general world model family, released as three post-trained variants: GWM Worlds for explorable environments, GWM Avatars for conversational characters and GWM Robotics for action-conditioned robot video, with a Robotics SDK.
- How it works: An autoregressive model built on Gen-4.5 that generates frame by frame and is conditioned on camera pose, robot commands or audio.
- Specs: 720p · up to 2 min (developer-reported)
- Capability: Temporal responsiveness, Reactivity, Situational reach
- Video: https://www.youtube.com/watch?v=aevPpq4PIhE
- Images: https://d3phaj0sisr2ct.cloudfront.net/site/images/research/gwm/gwm-card-01.png
- Project page: https://runwayml.com/research/introducing-runway-gwm-1
- API docs: https://docs.dev.runwayml.com/

#### Odyssey-2 — Odyssey (2025-10-27)
- Type: Model · Timing: Real-time streaming · Access: Product / app, Public API
- Input: Text prompt, Image → Output: Interactive frame stream
- Idea: Makes video behave like a chat: you steer it by typing, which lowers the bar for authoring, but text is coarse compared with game controls.
- What it is: A world model that begins streaming video within seconds of a typed prompt and keeps changing it as the viewer types new instructions, for multi-minute sessions in a web app; it follows Odyssey-1 (May 2025) and was later offered through an API as Odyssey-2 Pro.
- How it works: A causal, autoregressive video model that generates each frame from past frames and the current text, producing a new frame every 50 ms.
- Specs: 20 fps · 50 ms per frame · multi-minute streams (developer-reported)
- Capability: Temporal responsiveness, Co-creation & agency, Authoring accessibility
- Video: https://framerusercontent.com/assets/1RxJjsLhuFccE8n3TwpMnC8cNE.mp4
- Images: https://framerusercontent.com/assets/iGnprsv1qq41yOKpOnTDNQNBrRs.jpg
- Project page: https://odyssey.ml/introducing-odyssey-2
- API docs: https://developer.odyssey.ml

#### RTFM — World Labs (2025-10-16)
- Type: Research demo · Timing: Real-time streaming · Access: Waitlist / early access
- Input: Image, Camera path / pose → Output: Interactive frame stream
- Idea: Treats a learned model as a renderer with spatial memory, a route to persistent worlds without building explicit 3D.
- What it is: A 'Real-Time Frame Model' research preview that renders a world generated from a single image as you move through it in the browser, with reflections, gloss and shadows; World Labs reports it runs on one H100 and that the world 'will never be forgotten'.
- How it works: An end-to-end autoregressive diffusion transformer over frames whose stored frames carry 3D poses; it retrieves nearby frames as context ('context juggling') to keep the world consistent.
- Specs: 1× H100 · interactive frame rate (developer-reported)
- Capability: Persistence, Perceptual realism, Temporal responsiveness
- Video: https://wlt-ai-cdn.art/videos/2025-10-15-v3/matchmove-icegleam.mp4
- Images: https://www.worldlabs.ai/api/opengraph-image?imageUrl=/images/rtfm-thumbnail-glass.png&title=RTFM:%20A%20Real-Time%20Frame%20Model
- Project page: https://www.worldlabs.ai/blog/rtfm
- API docs: https://rtfm.worldlabs.ai/

#### Mirage 2 — Dynamics Lab (2025-08-21)
- Type: Model · Timing: Real-time streaming · Access: Waitlist / early access
- Input: Image, Text prompt, Keyboard & controller actions → Output: Interactive frame stream
- Idea: Showed in 2025 that anyone could step into their own picture, while press tests found loose controls and sudden scene changes.
- What it is: A 'generative world engine' that turned any uploaded image, from a photo to a child's drawing, into a world playable in the browser with WASD keys, and let players change it with text mid-session; the online demo was offline when checked in October 2026.
- How it works: Reported as an autoregressive transformer-based diffusion model streaming frames from image and text prompts with live text edits.
- Specs: > 10 min sessions · ~200 ms latency · single GPU (developer-reported, via press)
- Capability: Authoring accessibility, Co-creation & agency, Temporal responsiveness
- Video: https://www.youtube.com/watch?v=Ps55y7NPgTs
- Project page: https://www.gigazine.net/gsc_news/en/20250825-ai-generative-world-mirage-2

#### Hunyuan-GameCraft — Tencent Hunyuan (2025-08-14)
- Type: Open-source tool · Timing: Turn-based · Access: Open weights / code
- Input: Image, Text prompt, Keyboard & controller actions → Output: Interactive frame stream
- Idea: Brings AAA-game visual quality to action-conditioned video, but each action chunk is generated in turn rather than streamed live.
- What it is: An open-weight model that turns an image and a text prompt into high-dynamic, game-like video controlled by keyboard and mouse, keeping the scene consistent across long action sequences; paper June 2025, weights August 2025.
- How it works: Built on HunyuanVideo: keyboard and mouse inputs are unified into a continuous camera-action space, with a hybrid history condition for autoregressive extension and distillation for speed; trained on over a million gameplay clips from 100+ AAA games.
- Capability: Reactivity, Persistence, Perceptual realism
- Paper: https://arxiv.org/abs/2506.17201 (arXiv 2025)
- Video: https://hunyuan-gamecraft.github.io/assets/videos/main.mp4
- Images: https://hunyuan-gamecraft.github.io/assets/images/pipeline.png
- Project page: https://hunyuan-gamecraft.github.io/
- Code: https://github.com/Tencent-Hunyuan/Hunyuan-GameCraft-1.0

#### Matrix-Game 2.0 — Skywork (Kunlun Tech) (2025-08-12)
- Type: Open-source tool · Timing: Real-time streaming · Access: Open weights / code
- Input: Image, Keyboard & controller actions → Output: Interactive frame stream
- Idea: The first widely used open real-time world model: a lab can download it, run it and pin the version.
- What it is: An open-weight world model that streams minute-long interactive video from a single image, controlled by keyboard and mouse, in Minecraft-like, urban-driving and GTA-style scenes.
- How it works: A few-step causal diffusion model distilled for autoregressive streaming, trained on about 1,200 hours of Unreal Engine and GTA5 interaction data with action injection modules.
- Specs: 25 fps · minute-level video (developer-reported)
- Capability: Temporal responsiveness, Reactivity
- Paper: https://arxiv.org/abs/2508.13009 (arXiv 2025)
- Video: https://matrix-game-v2.github.io/static/videos/matrix-game2.mp4
- Images: https://matrix-game-v2.github.io/static/imgs/architecture.png
- Project page: https://matrix-game-v2.github.io/
- Code: https://github.com/SkyworkAI/Matrix-Game

#### Yan — Tencent (2025-08-12)
- Type: Research demo · Timing: Real-time streaming · Access: Research only
- Input: Image, Text prompt, Keyboard & controller actions → Output: Interactive frame stream
- Idea: Splits a world into simulation, generation and live editing, a useful decomposition for anyone who needs to change a situation while it runs.
- What it is: A framework for interactive video with three parts: Yan-Sim simulates a game world at 1080p and 60 fps from player input, Yan-Gen creates new interactive worlds from text and images, and Yan-Edit lets players change structure and style with text while they play.
- How it works: A highly compressed low-latency 3D-VAE with KV-cache shift-window denoising for real-time simulation, plus a multimodal diffusion generator distilled for streaming and a hybrid model that separates mechanics from visual rendering for editing.
- Specs: 1080p · 60 fps (developer-reported)
- Capability: Perceptual realism, Temporal responsiveness, Co-creation & agency
- Paper: https://arxiv.org/abs/2508.08601 (arXiv 2025)
- Video: https://greatx3.github.io/Yan/videos_compressed/teaser.mp4
- Images: https://greatx3.github.io/Yan/images/architecture/yan_sim.png
- Project page: https://greatx3.github.io/Yan/

#### Genie 3 — Google DeepMind (2025-08-05)
- Type: Model · Timing: Real-time streaming · Access: Waitlist / early access, Product / app
- Input: Text prompt, Keyboard & controller actions → Output: Interactive frame stream
- Idea: The first real-time general world model: a situation can be described in words and walked into, but it lasts minutes, not hours, and the person controls only one avatar.
- What it is: A general-purpose world model that generates a navigable world from a text prompt and streams it in real time; DeepMind reports 720p at 24 fps with consistency for a few minutes, plus 'promptable world events' that change weather or add objects mid-session.
- How it works: Autoregressive frame-by-frame generation that attends to the trajectory so far, so revisited places stay consistent without an explicit 3D representation; trained on large-scale video.
- Specs: 720p · 24 fps · consistent for a few minutes · promptable world events (developer-reported)
- Capability: Temporal responsiveness, Persistence, Situational reach
- Video: https://www.youtube.com/watch?v=PDKhUknuQDg
- Images: https://lh3.googleusercontent.com/MZsGi3QroEY4lNLxrQVBVpn_5NZDXMCKwXs8nStlzGvjS7p76pP-FjyyO-hrYuBhERc60C5-KosmVJFfITEYN7wx_cV94Wju48IyYRwQ39_DtRDU=w1200-h630-n-nu-rw
- Project page: https://deepmind.google/blog/genie-3-a-new-frontier-for-world-models/

#### Genie 2 — Google DeepMind (2024-12-04)
- Type: Model · Timing: Turn-based · Access: Research only
- Input: Image, Text prompt, Keyboard & controller actions → Output: Interactive frame stream
- Idea: Moves world models from 2D games to rich 3D-looking scenes, but only for short sessions and not in real time.
- What it is: A foundation world model that turns one prompt image into a 3D-looking world a person or agent can play with keyboard and mouse, with physics, lighting, NPCs and object interactions; DeepMind reports consistent play for up to about a minute.
- How it works: An autoregressive latent diffusion model over video frames, conditioned on keyboard and mouse actions, trained on a large video dataset; prompt images were generated with Imagen 3.
- Specs: 10–20 s typical · up to ~1 min consistency (developer-reported)
- Capability: Situation diversity, Persistence, Situational reach
- Video: https://storage.googleapis.com/gdm-deepmind-com-prod-public/media/media/genie2_zoom_v6.mp4
- Images: https://lh3.googleusercontent.com/NtYWmA3waHr1wi5OrNVdxndoSe4iS7Kui6GU4p8HvpFN_YrsbDcGudAgi4Nl-rN1geHpA4Czl0yXO6TQ73n8Q39oMmhDj_vbQ3rWNYE9EVLJcqm2=w1200-h630-n-nu-rw
- Project page: https://deepmind.google/discover/blog/genie-2-a-large-scale-foundation-world-model/

#### Genie — Google DeepMind (2024-02-23)
- Type: Model · Timing: Turn-based · Access: Research only
- Input: Image, Keyboard & controller actions → Output: Interactive frame stream
- Idea: Shows that controls can be learned from unlabeled video, so any picture can become a world with a small set of discovered actions.
- What it is: An 11-billion-parameter model that turns a single image, sketch or photo into a playable 2D platformer, learned from internet gameplay videos without any action labels.
- How it works: A spatiotemporal video tokenizer, a latent action model that infers 8 discrete actions between frames, and an autoregressive dynamics model, trained on 30,000 hours of 2D platformer videos filtered from about 200,000 hours of internet footage.
- Specs: 11B parameters · 8 latent actions · ~1 fps (developer-reported)
- Capability: Reactivity, Situation diversity
- Recognition: ICML 2024 Best Paper
- Paper: https://arxiv.org/abs/2402.15391 (ICML 2024)
- Video: https://www.youtube.com/watch?v=DSVsnCDTyfc
- Project page: https://sites.google.com/view/genie-2024/home

### Neural game engines

Games rendered frame by frame by a network: GameNGen, DIAMOND, Oasis, Muse / WHAM, WHAMM…

#### Matrix-Game 4.0 — Skywork (Kunlun Tech) (2026-10-15)
- Type: Open-source tool · Timing: Real-time streaming · Access: Open weights / code
- Input: Keyboard & controller actions, Text prompt, Scene spec, code & rules → Output: Interactive frame stream
- Idea: Hands state and rules back to an engine and leaves only appearance to the model, which restores persistence and experimental control.
- What it is: An open release that keeps the game logic, physics and player input in a real game engine and uses a causal video model only to turn the engine's low-poly frames into detailed visuals; it ships three playable games (medieval castle, ancient Egypt, city racing) with weights and source.
- How it works: Streaming neural rendering: a few-step causal video model renders successive chunks conditioned on low-poly RGB frames and text prompts from an executable engine.
- Specs: 864×480 · up to 67 fps on RTX 5080 (developer-reported)
- Capability: Experimental control, Persistence, Perceptual realism
- Video: https://matrix-game-v4-0.github.io/page/assets/prompt/egypt06.mp4
- Images: https://matrix-game-v4-0.github.io/page/assets/fig/overview_en.png
- Project page: https://matrix-game-v4-0.github.io/page/
- Code: https://github.com/SkyworkAI/Matrix-Game

#### MIRA — General Intuition, Kyutai (2026-07-06)
- Type: Open-source tool · Timing: Real-time streaming · Access: Open weights / code, Product / app
- Input: Keyboard & controller actions → Output: Interactive frame stream, Agent behaviour & actions
- Idea: Several people share one generated situation and see each other's actions, with no game engine underneath; the developers report it runs indefinitely without diverging.
- What it is: An open multiplayer world model of Rocket League in which four people play a 2v2 match in a browser, each seeing a consistent generated view at 20 fps, with boost, goals and demolitions tracked by the model alone; an autopilot mode lets the model play for absent players.
- How it works: A 5B-parameter diffusion transformer over a 600M-parameter video representation codec, trained on bot gameplay with action dropout, conditioned on all four players' inputs; developed by General Intuition and Kyutai with Epic Games.
- Specs: 4 players · 20 fps · 576p split across players · 5B + 600M parameters (developer-reported)
- Capability: Co-creation & agency, Persistence, Temporal responsiveness
- Video: https://mira-wm.com/media/hero-v2.mp4
- Project page: https://mira-wm.com/blog-post/
- Code: https://github.com/mira-wm/mira

#### Dreamer 4 — Danijar Hafner, Google DeepMind (2025-09-29)
- Type: Research demo · Timing: Real-time streaming · Access: Research only
- Input: Keyboard & controller actions → Output: Interactive frame stream, Agent behaviour & actions
- Idea: A world model accurate enough to train agents for long tasks, which is the same property needed to trust it as a test bed.
- What it is: An agent that learns to obtain diamonds in Minecraft purely from offline video, by practising inside a learned world model that also runs in real time for human players on a single GPU.
- How it works: A causal tokenizer and an efficient transformer dynamics model trained with a 'shortcut forcing' objective; the agent learns by reinforcement learning on imagined rollouts.
- Specs: real-time on 1 GPU (developer-reported)
- Capability: Reactivity, Behavioral plausibility
- Paper: https://arxiv.org/abs/2509.24527 (arXiv 2025)
- Video: https://www.youtube.com/watch?v=oDlBtTcX0g0
- Project page: https://danijar.com/project/dreamer4/

#### WHAMM — Microsoft (2025-04-04)
- Type: Research demo · Timing: Real-time streaming · Access: Product / app, Research only
- Input: Keyboard & controller actions → Output: Interactive frame stream
- Idea: Shows how little data is needed to clone one level, and how short the memory of such a clone is.
- What it is: A real-time playable AI rendition of a Quake II level in Copilot Labs, generated from controller input at 640×360; Microsoft notes it forgets objects that leave view for about a second and has noticeable latency; the project page now lists it as WHAM-RT.
- How it works: A MaskGIT-style World and Human Action model that generates image tokens in parallel, trained on one week of curated Quake II play with a 0.9-second (9-frame) context.
- Specs: 640×360 · 10+ fps · 0.9 s context (developer-reported)
- Capability: Temporal responsiveness, Reactivity
- Video: https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/vid1_square.mp4
- Images: https://www.microsoft.com/en-us/research/wp-content/uploads/2025/04/whamm_overview.png
- Project page: https://www.microsoft.com/en-us/research/articles/whamm-real-time-world-modelling-of-interactive-environments/

#### Muse (WHAM) — Microsoft (2025-02-19)
- Type: Model · Timing: Turn-based · Access: Open weights / code, Research only
- Input: Image, Keyboard & controller actions → Output: Interactive frame stream, Agent behaviour & actions
- Idea: Models the player's actions as well as the world, so it can predict what a person is likely to do next, not only what they will see.
- What it is: A 'World and Human Action Model' trained on seven years of human play of the Xbox game Bleeding Edge that generates gameplay visuals, controller actions or both, consistent for up to two minutes; weights and the WHAM Demonstrator tool were released for researchers, and on 2026-09-23 Microsoft moved the WHAM team and technology into its Microsoft AI product group.
- How it works: A 1.6B-parameter transformer that predicts interleaved image tokens and controller-action tokens, trained on more than 1 billion images and controller actions (over 7 years of play) at 300×180 resolution, developed with Ninja Theory.
- Specs: 1.6B parameters · 300×180 · up to 2 min consistency (developer-reported)
- Capability: Persistence, Authoring accessibility, Situation diversity
- Paper: https://doi.org/10.1038/s41586-025-08600-3 (Nature 2025)
- Video: https://www.microsoft.com/en-us/research/wp-content/uploads/2025/02/BE-Play-Session-edited.mp4
- Images: https://www.microsoft.com/en-us/research/wp-content/uploads/2025/02/WHAM-TWLIFB-1200x627-1.jpg
- Project page: https://www.microsoft.com/en-us/research/blog/introducing-muse-our-first-generative-ai-model-designed-for-gameplay-ideation/
- Code: https://huggingface.co/microsoft/wham

#### GameFactory — Jiwen Yu, Kuaishou (2025-01-14)
- Type: Research demo · Timing: Turn-based · Access: Open weights / code, Research only
- Input: Text prompt, Keyboard & controller actions → Output: Flat video
- Idea: Separates 'how to move' from 'what the world looks like', which is what lets a lab script new scenarios without new game data.
- What it is: A method for creating new games as interactive video: action control learned from Minecraft is transferred to open-domain scenes generated from text, so a player can walk and look around in worlds that were never in the training data.
- How it works: A pretrained video diffusion model with a style-decoupling LoRA and a separate action-control module trained on the GF-Minecraft dataset, extended autoregressively for long videos.
- Capability: Situation diversity, Authoring accessibility, Experimental control
- Paper: https://arxiv.org/abs/2501.08325 (ICCV 2025 (Highlight))
- Video: https://yujiwen.github.io/gamefactory/videos/gallery/1.mp4
- Images: https://yujiwen.github.io/gamefactory/static/assets/layout.jpg
- Project page: https://yujiwen.github.io/gamefactory/
- Code: https://github.com/KwaiVGI/GameFactory

#### Oasis — Decart, Etched (2024-10-31)
- Type: Model · Timing: Real-time streaming · Access: Open weights / code, Product / app
- Input: Keyboard & controller actions → Output: Interactive frame stream
- Idea: The first real-time AI game world played at scale, which also exposed how quickly an unanchored world forgets what you left behind.
- What it is: A Minecraft-like open world generated frame by frame from keyboard and mouse input and playable in the browser at about 20 fps; the code and a 500M-parameter checkpoint were released openly alongside a live demo of a larger model.
- How it works: A ViT autoencoder and a diffusion transformer generate each frame autoregressively from past frames and actions, trained with Diffusion Forcing; Etched targeted its Sohu chip for higher resolutions.
- Specs: ~20 fps · 500M open weights (developer-reported)
- Capability: Temporal responsiveness, Reactivity
- Video: https://oasis-model.github.io/wide1.mp4
- Images: https://oasis-model.github.io/1.webp
- Project page: https://oasis-model.github.io/
- Code: https://github.com/etched-ai/open-oasis

#### GameNGen — Google, Google DeepMind (2024-08-27)
- Type: Research demo · Timing: Real-time streaming · Access: Research only
- Input: Keyboard & controller actions → Output: Interactive frame stream
- Idea: Proves real-time neural rendering of a full game is possible, for one game whose rules the model has memorised.
- What it is: The first game engine run entirely by a neural model: DOOM played interactively at about 20 fps on a single TPU, with human raters only slightly better than chance at telling short generated clips from the real game (developer-reported).
- How it works: An RL agent records gameplay, then a Stable Diffusion v1.4 model fine-tuned on past frames and actions predicts the next frame, with noise augmentation on the context to prevent drift.
- Specs: ~20 fps · single TPU · PSNR 29.4 (developer-reported)
- Capability: Temporal responsiveness, Perceptual realism
- Paper: https://arxiv.org/abs/2408.14837 (ICLR 2025)
- Video: https://www.youtube.com/watch?v=O3616ZFGpqw
- Images: https://gamengen.github.io/static/images/embed_image.png
- Project page: https://gamengen.github.io/

#### DIAMOND — Eloi Alonso (2024-05-20)
- Type: Open-source tool · Timing: Real-time streaming · Access: Open weights / code
- Input: Keyboard & controller actions → Output: Interactive frame stream, Agent behaviour & actions
- Idea: Visual detail matters for agents, and an open, small diffusion model is enough for a playable 3D game world.
- What it is: A diffusion world model that trains Atari agents in imagination and, as a demo, turns recorded Counter-Strike: Global Offensive gameplay into a Dust II map people can play on a consumer GPU.
- How it works: An EDM-style diffusion model conditioned on past frames and actions, used both as the RL environment and, for CS:GO, as a two-stage generator with an upsampler.
- Specs: Atari 100k mean HNS 1.46 · CS:GO playable at ~10 fps on RTX 3090 (developer-reported)
- Capability: Perceptual realism, Reactivity
- Paper: https://arxiv.org/abs/2405.12399 (NeurIPS 2024 (Spotlight))
- Video: https://x.com/EloiAlonso1/status/1793916382779982120
- Images: https://diamond-wm.github.io/static/gifs/half_diamond.gif
- Project page: https://diamond-wm.github.io/
- Code: https://github.com/eloialonso/diamond

#### GameGAN — Seung Wook Kim, NVIDIA (2020-05-22)
- Type: Research demo · Timing: Real-time streaming · Access: Open weights / code, Research only
- Input: Keyboard & controller actions → Output: Interactive frame stream
- Idea: The first widely shown neural game engine: a game's rules and graphics can both be learned from play data.
- What it is: A generative model that learned to re-create a playable PAC-MAN purely from 50,000 recorded episodes of screen frames and key presses, without access to the game engine; NVIDIA released it for the game's 40th anniversary.
- How it works: A GAN with a dynamics engine, an external memory module that keeps the maze consistent, and a rendering engine that separates static background from moving agents.
- Capability: Reactivity, Persistence
- Paper: https://arxiv.org/abs/2005.12126 (CVPR 2020)
- Video: https://www.youtube.com/watch?v=BYt6r8z6pUY
- Project page: https://nv-tlabs.github.io/gameGAN/
- Code: https://github.com/nv-tlabs/GameGAN_code

#### World Models — David Ha (2018-03-27)
- Type: Research demo · Timing: Real-time streaming · Access: Open weights / code, Research only
- Input: Keyboard & controller actions → Output: Interactive frame stream, Agent behaviour & actions
- Idea: The lineage starts here: a learned simulator can stand in for the real environment, and its flaws can be exploited by whoever acts inside it.
- What it is: An interactive paper in which an agent learns a compressed model of a car-racing game and of VizDoom, then trains entirely inside its own generated 'dream' and transfers the learned policy back to the real game; readers can play inside the dream in the browser.
- How it works: A VAE compresses frames, a mixture-density RNN predicts the next latent state from action, and a small controller is evolved with CMA-ES inside the RNN's rollouts.
- Capability: Reactivity
- Paper: https://arxiv.org/abs/1803.10122 (NeurIPS 2018 (as 'Recurrent World Models Facilitate Policy Evolution'))
- Video: https://www.youtube.com/watch?v=HzA8LRqhujk
- Images: https://worldmodels.github.io/assets/world_models_card_both.png
- Project page: https://worldmodels.github.io/
- Code: https://github.com/hardmaru/WorldModelsExperiments

### World models for robots & driving

Physical-AI simulators that predict how the world responds to an agent: Cosmos, GAIA, V-JEPA 2, UniSim…

#### Odyssey-3 — Odyssey (2026-09-15)
- Type: Model · Timing: Real-time streaming · Access: Product / app, Public API
- Input: Text prompt, Keyboard & controller actions, Video → Output: Interactive frame stream, Agent behaviour & actions
- Idea: One world model as both simulator and controller, which would let the same model play the environment and the agents in it.
- What it is: Odyssey's third foundation world model, which the company says can both generate interactive worlds and, with small action decoders trained on hours of data, control robot arms, humanoids, cars, drones and video-game characters.
- How it works: An autoregressive diffusion transformer trained on a large collection of visual observations; task-specific action decoders translate its internal representations into control signals.
- Specs: few to tens of hours of task data per embodiment (developer-reported)
- Capability: Adaptation, Situational reach, Behavioral plausibility
- Video: https://framerusercontent.com/assets/J2EGlzwE6xA1NPIEdgwQypDfz1A.mp4
- Images: https://framerusercontent.com/assets/JU7BjLegfmzvfZ2iaaZ0CIAWWag.jpg
- Project page: https://odyssey.ml/introducing-odyssey-3
- API docs: https://developer.odyssey.ml

#### GAIA-4 — Wayve (2026-08-03)
- Type: Model · Timing: Turn-based · Access: Research only
- Input: Video, Keyboard & controller actions, Scene spec, code & rules → Output: Flat video
- Idea: Closed-loop and anchored to a real recording: the counterfactual changes only what the agent's decision changes, a clean design for 'what if' tests.
- What it is: The fourth GAIA world model, which puts Wayve's AI Driver in the loop: a recorded drive becomes the starting point of a simulation in which the camera view changes with every braking or steering decision, so engineers can test futures that never happened.
- How it works: A multimodal world model that re-simulates sensor input conditioned on the driving model's actions while keeping the underlying scene tied to the original recording as a deterministic baseline.
- Capability: Reactivity, Experimental control, Situational reach
- Video: https://wayve.ai/wp-content/uploads/2026/07/GAIA-4-Trimmed-1.mp4
- Images: https://wayve.ai/wp-content/uploads/2026/07/GAIA-4-Hero-Image.jpg
- Project page: https://wayve.ai/thinking/gaia-4/

#### Oasis 3 — Decart (2026-06-10)
- Type: Model · Timing: Real-time streaming · Access: Public API
- Input: Text prompt, Keyboard & controller actions → Output: Interactive frame stream
- Idea: Rare long-tail events become something you can request by prompt and drive through, rather than wait for on real roads.
- What it is: Decart's interactive world model for physical AI, starting with autonomous driving: it generates diverse, photorealistic driving environments from a single prompt that respond to the vehicle's actions in real time, and was available by API from launch.
- How it works: A real-time generative world model served on Decart's optimized inference stack (DOS), conditioned on prompts and vehicle controls for closed-loop robot training.
- Capability: Situational reach, Temporal responsiveness, Situation diversity
- Video: https://www.youtube.com/watch?v=yeGmjZ8Nr1A
- Images: https://cdn.prod.website-files.com/69ac78b058a3b8e6de5d1387/6a297d526275636705fa5eb5_oaasis.jpg
- Project page: https://decart.ai/publications/introducing-oasis-3-first-interactive-world-model-for-physical-ai
- API docs: https://platform.decart.ai/

#### Cosmos 3 — NVIDIA (2026-05-31)
- Type: Model · Timing: Pre-generated · Access: Open weights / code, Public API
- Input: Text prompt, Video, Keyboard & controller actions → Output: Flat video, Agent behaviour & actions, Sound, music & spatial audio
- Idea: Reasoning about a situation before simulating it is the step that makes generated outcomes checkable against an explanation.
- What it is: An open 'omni-model' announced at GTC Taipei that reasons about a scene, generates video and ambient sound, and outputs robot action data such as joint angles and gripper positions, so one model can describe, simulate and act.
- How it works: A mixture-of-transformers model in which a reasoning block interprets the scene and a generation block produces physically grounded video, audio and numerical action outputs; it can be post-trained as a world-action model.
- Capability: Situational reach, Behavioral plausibility, Experimental control
- Video: https://www.youtube.com/watch?v=q7Hj3J9SOXw
- Images: https://blogs.nvidia.com/wp-content/uploads/2026/05/Featured-image.png
- Project page: https://blogs.nvidia.com/blog/cosmos-3-physical-ai-open-world-foundation-model/
- Code: https://github.com/nvidia-cosmos

#### Waymo World Model — Waymo, Google DeepMind (2026-02-06)
- Type: Model · Timing: Real-time streaming · Access: Research only
- Input: Text prompt, Keyboard & controller actions, Scene spec, code & rules → Output: Flat video, Dynamic 3D / 4D
- Idea: A general world model's knowledge transfers to a safety-critical domain once post-trained on that domain's sensors, a pattern other high-stakes simulations could follow.
- What it is: A driving simulator built on Genie 3 that generates both camera and lidar data, controllable by language prompts, driving inputs and scene layouts, to rehearse rare events such as a tornado, an elephant on the road or a wrong-way driver.
- How it works: Genie 3 post-trained on Waymo driving data to output multi-sensor 2D video and 3D lidar, with an efficient real-time variant used when a simulation departs from a logged event.
- Specs: camera + lidar output (developer-reported)
- Capability: Situational reach, Experimental control, Perceptual realism
- Video: https://storage.googleapis.com/waymo-prod-cdn/uploads/bd1e232de236794e89f6daa89b594b93-topline_video_close_loop_sim_cropped.webm
- Images: https://lh3.googleusercontent.com/pcL3e60qMHH67WyyOeA1d-8Tjx2B4kwe90bpyvAyWOgf8Clb40mPxyjhpSAaH1ZsJzvtOxhU-eMYvfy5G_YYPYyGvRmRYlLHxOs
- Project page: https://waymo.com/blog/2026/02/the-waymo-world-model-a-new-frontier-for-autonomous-driving-simulation

#### V-JEPA 2 — Meta (2025-06-11)
- Type: Model · Timing: Turn-based · Access: Open weights / code
- Input: Video, Image → Output: Agent behaviour & actions
- Idea: A world model does not have to render pixels to be useful; predicting abstract consequences is enough for planning.
- What it is: A self-supervised video world model that predicts in a learned representation space rather than in pixels; Meta reports that an action-conditioned version lets a robot arm plan pick-and-place tasks zero-shot in labs it has never seen.
- How it works: A joint-embedding predictive architecture pre-trained on over 1 million hours of internet video and images, then post-trained as V-JEPA 2-AC on under 62 hours of unlabeled robot video from the DROID dataset and used for model-predictive control.
- Specs: 1.2B parameters · 1M+ hours of video · < 62 h robot data (developer-reported)
- Capability: Behavioral plausibility, Adaptation
- Paper: https://arxiv.org/abs/2506.09985 (arXiv 2025)
- Video: https://about.fb.com/wp-content/uploads/2025/06/01_VJEPA2.mp4
- Images: https://about.fb.com/wp-content/uploads/2025/06/VJEPA-2-Launch_Header-Cover_Social-Share.png?w=1200
- Project page: https://about.fb.com/news/2025/06/our-new-model-helps-ai-think-before-it-acts/
- Code: https://github.com/facebookresearch/vjepa2

#### GAIA-2 — Wayve (2025-03-26)
- Type: Model · Timing: Pre-generated · Access: Research only
- Input: Scene spec, code & rules, Video, Text prompt → Output: Flat video
- Idea: Rare and dangerous traffic situations can be specified as parameters and generated on demand, a template for scenario-controlled studies.
- What it is: A generative driving world model that produces consistent multi-camera driving video from structured inputs such as ego-vehicle motion, other agents, weather, time of day and road layout, across UK, US and German roads; it followed GAIA-1 (2023).
- How it works: A latent diffusion world model with a dedicated video tokenizer and rich structured conditioning (ego dynamics, agent configurations, environment, road semantics) plus external driving-model embeddings.
- Specs: multi-camera · UK / US / Germany data (developer-reported)
- Capability: Situational reach, Experimental control, Situation diversity
- Paper: https://arxiv.org/abs/2503.20523 (Technical report 2025)
- Video: https://www.youtube.com/watch?v=bwTzVU1ib1I
- Images: https://wayve.ai/wp-content/uploads/2025/03/Wayve-GAIA-2-Hero-Blog-Image.jpg
- Project page: https://wayve.ai/thinking/gaia-2/

#### Cosmos — NVIDIA (2025-01-06)
- Type: Platform / API · Timing: Pre-generated · Access: Open weights / code
- Input: Text prompt, Image, Video → Output: Flat video
- Idea: Open, permissively licensed world models that labs can fine-tune to their own environments, the default base for robot and driving simulation.
- What it is: An open platform of 'world foundation models' for physical AI, announced at CES 2025: video tokenizers, a data-curation pipeline and diffusion and autoregressive models that generate physically plausible video for training robots and autonomous vehicles, later extended with Predict, Transfer and Reason models.
- How it works: Diffusion and autoregressive transformer models pre-trained on about 100M clips curated from 20M hours of video, with guardrails and post-training recipes for camera control, robotics and driving.
- Specs: 4B–14B parameters · 20M hours of source video (developer-reported)
- Capability: Situational reach, Situation diversity
- Paper: https://arxiv.org/abs/2501.03575 (arXiv 2025)
- Video: https://www.youtube.com/watch?v=9Uch931cDx8
- Images: https://www.nvidia.com/content/dam/en-zz/Solutions/ai/cosmos/nvidia-cosmos-og.jpg
- Project page: https://www.nvidia.com/en-us/ai/cosmos/
- Code: https://github.com/nvidia-cosmos

#### Navigation World Models — Amir Bar, Meta (2024-12-04)
- Type: Research demo · Timing: Turn-based · Access: Open weights / code
- Input: Image, Keyboard & controller actions → Output: Flat video, Agent behaviour & actions
- Idea: Uses a world model as an imagination for planning, with constraints that can be added at planning time.
- What it is: A controllable video model that imagines what an agent will see along a candidate path, so a robot can plan a route by simulating trajectories and checking whether they reach the goal, including in unfamiliar places from a single image.
- How it works: A 1B-parameter Conditional Diffusion Transformer (CDiT) trained on egocentric videos of humans and robots, conditioned on past frames and navigation actions.
- Specs: 1B parameters (developer-reported)
- Capability: Experimental control, Reactivity
- Recognition: CVPR 2025 Best Paper Honorable Mention
- Paper: https://arxiv.org/abs/2412.03572 (CVPR 2025)
- Video: https://www.amirbar.net/nwm/assets/known_environments/recon_ours_1_1080p.mp4
- Images: https://www.amirbar.net/nwm/assets/nwm.png
- Project page: https://www.amirbar.net/nwm/
- Code: https://github.com/facebookresearch/nwm

#### 1X World Model — 1X Technologies (2024-09-17)
- Type: Model · Timing: Turn-based · Access: Open weights / code, Research only
- Input: Video, Keyboard & controller actions → Output: Flat video
- Idea: World models as an evaluation tool: comparing policies in imagination before running them on hardware.
- What it is: A learned simulator for 1X's humanoid robots that imagines several futures from the same starting frames under different action proposals, including rigid, deformable and articulated objects such as laundry, doors and drawers; 1X released a dataset and public challenge.
- How it works: An action-conditioned video prediction model trained on 1X's own robot logs, with tokenized video and a public 1xgpt baseline.
- Capability: Experimental control, Reactivity
- Video: https://www.youtube.com/watch?v=xPX6dDRYbV4
- Images: https://cdn.sanity.io/images/qka6yvsc/production/1da42dae7a0f986a38880cd979a570e0fba70ddd-2048x1080.png?fit=max&auto=format
- Project page: https://www.1x.tech/discover/1x-world-model
- Code: https://github.com/1x-technologies/1xgpt

#### UniSim — Sherry Yang, Google DeepMind (2023-10)
- Type: Research demo · Timing: Turn-based · Access: Research only
- Input: Text prompt, Image, Keyboard & controller actions → Output: Flat video
- Idea: Reframes video generation as a simulator of real-world interaction, the conceptual step from 'video model' to 'world model'.
- What it is: A 'universal simulator' that predicts what a camera would see after a person or robot carries out an action described in text, such as 'cut the carrot' or 'open the drawer', so that planners and RL policies can be trained in simulation and then deployed on real robots.
- How it works: A video diffusion model conditioned on past frames and text or low-level actions, trained on an orchestrated mix of image, video, robot and navigation datasets; it is rolled out autoregressively for long-horizon interaction.
- Capability: Situational reach, Reactivity
- Recognition: ICLR 2024 Outstanding Paper Award
- Paper: https://arxiv.org/abs/2310.06114 (ICLR 2024)
- Video: https://universal-simulator.github.io/unisim/materials/cut_carrot-final.mp4
- Images: https://universal-simulator.github.io/unisim/materials/unisim.png
- Project page: https://universal-simulator.github.io/unisim/

### Memory, consistency & control

Research on keeping a generated world coherent: spatial memory, long context, promptable events, state.

#### WorldTrace — Xindi Wu, NVIDIA (2026-08-07)
- Type: Research demo · Timing: Real-time streaming · Access: Research only
- Input: Keyboard & controller actions, Camera path / pose → Output: Interactive frame stream
- Idea: Pinpoints why world models forget (positional encodings drift out of range) and fixes it without retraining, so existing models can run longer sessions.
- What it is: A training-free fix for interactive video world models that forget once a session runs past their training length: it keeps the model's compressed memory addressable so long rollouts stay smooth and previously visited scenes can be recalled.
- How it works: The KV cache is compressed into fixed in-distribution slot positions with canonical-key writers, avoiding averaging across incompatible RoPE phases; two variants target smooth rollouts (Field) and scene recall (Landmark).
- Capability: Persistence, Experimental control
- Paper: https://arxiv.org/abs/2608.07408 (NeurIPS 2026)
- Video: https://research.nvidia.com/labs/sil/projects/WorldTrace/videos/teaser/worldtrace_panel_rotate90.mp4
- Images: https://research.nvidia.com/labs/sil/projects/WorldTrace/figures/og-card.png
- Project page: https://research.nvidia.com/labs/sil/projects/WorldTrace/

#### Matrix-Game 3.0 — Skywork (Kunlun Tech) (2026-03-27)
- Type: Open-source tool · Timing: Real-time streaming · Access: Open weights / code
- Input: Image, Keyboard & controller actions, Camera path / pose → Output: Interactive frame stream
- Idea: Shows memory and real-time speed together in an open model, at a hardware cost (8 GPUs) that still limits lab use.
- What it is: An open-weight, memory-augmented interactive world model that streams 720p video in real time and keeps scenes consistent over long sessions by retrieving relevant past frames by camera position; Skywork followed it with Matrix-Game 3.5 (patch memory) in August 2026.
- How it works: A 5B autoregressive diffusion model building on Matrix-Game 2.0 with GPU-based camera-aware memory retrieval, few-step sampling, INT8 quantization, distillation and a lightweight VAE.
- Specs: 720p · up to 40 fps · 5B parameters · 8 GPUs (developer-reported)
- Capability: Persistence, Temporal responsiveness
- Paper: https://arxiv.org/abs/2604.08995 (arXiv 2026)
- Video: https://matrix-game-v3.github.io/static/videos/teaser.mp4
- Images: https://matrix-game-v3.github.io/static/imgs/mg3_overview.png
- Project page: https://matrix-game-v3.github.io/
- Code: https://github.com/SkyworkAI/Matrix-Game

#### Video World Models with Long-term Spatial Memory — Tong Wu (2025-06-05)
- Type: Research demo · Timing: Turn-based · Access: Research only
- Input: Camera path / pose, Image → Output: Flat video, 3D scene / world
- Idea: Combines an explicit 3D store with a generative model: geometry for what must persist, generation for what can change.
- What it is: A video world model that keeps a 3D point cloud of the static scene as long-term memory alongside recent frames and keyframes, so places revisited after long camera paths look the same.
- How it works: A geometry-grounded memory with three parts: a point-cloud spatial memory of static content, a working memory of recent frames and an episodic memory of keyframes, all conditioning a video diffusion model.
- Capability: Persistence, Experimental control
- Paper: https://arxiv.org/abs/2506.05284 (arXiv 2025)
- Video: https://spmem.github.io/static/videos/wm-demo.mp4
- Images: https://spmem.github.io/static/images/teaser.jpg
- Project page: https://spmem.github.io/

#### Context-as-Memory — Jiwen Yu, Kuaishou (2025-06-03)
- Type: Research demo · Timing: Turn-based · Access: Research only
- Input: Camera path / pose, Image → Output: Flat video
- Idea: Simple retrieval by field of view beats compressing the past, which makes memory inspectable frame by frame.
- What it is: A method that keeps a generated scene consistent over long interactive videos by treating all previously generated frames as memory and retrieving only those whose camera views overlap the next view.
- How it works: Past frames are concatenated as context to a video diffusion model, with a memory-retrieval module that selects frames by camera field-of-view overlap to bound compute.
- Capability: Persistence
- Paper: https://arxiv.org/abs/2506.03141 (SIGGRAPH Asia 2025)
- Video: https://www.youtube.com/watch?v=6Ye6wWupWD4
- Images: https://context-as-memory.github.io/pics/framework.jpg
- Project page: https://context-as-memory.github.io/

#### WorldMem — Zeqi Xiao (2025-04-16)
- Type: Research demo · Timing: Turn-based · Access: Open weights / code
- Input: Keyboard & controller actions, Image → Output: Interactive frame stream
- Idea: Persistence can be engineered: store what was seen with where and when, and look it up instead of hoping the model remembers.
- What it is: A world model with an explicit memory bank: when a player in Minecraft turns back to a place built or seen earlier, the model retrieves stored frames and their poses and regenerates the place consistently, including changes made over time.
- How it works: A memory bank of past frames tagged with camera poses and timestamps, read by a memory-attention module inside a video diffusion model.
- Capability: Persistence
- Paper: https://arxiv.org/abs/2504.12369 (arXiv 2025)
- Video: https://xizaoqu.github.io/worldmem/resources/cover.mp4
- Images: https://xizaoqu.github.io/worldmem/resources/success_044.png
- Project page: https://xizaoqu.github.io/worldmem/
- Code: https://github.com/xizaoqu/WorldMem

#### Diffusion Forcing — Boyuan Chen (2024-07-01)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code
- Input: Keyboard & controller actions, Video → Output: Flat video
- Idea: Long, stable rollouts are a training problem before they are a memory problem; this recipe fixed much of the drift.
- What it is: A training method that gives each frame its own noise level, so a video model can roll out stably far beyond its training length and be guided toward goals; it underlies many later real-time world models.
- How it works: Sequence diffusion in which every token is denoised at an independently sampled noise level, combining next-token prediction with full-sequence diffusion and enabling guidance over future tokens.
- Capability: Persistence, Experimental control
- Paper: https://arxiv.org/abs/2407.01392 (NeurIPS 2024)
- Video: https://www.youtube.com/watch?v=CNgwS8B7UvE
- Images: https://boyuan.space/diffusion-forcing/static/images/teaser.png
- Project page: https://boyuan.space/diffusion-forcing/
- Code: https://github.com/buoyancy99/diffusion-forcing

## 3D Scene & World Generation

Generated environments with explicit geometry (Gaussian splats, meshes, panoramas) that can be walked through in a headset, edited and kept. Persistence comes with the representation.

### Explorable 3D worlds

Text or image to a navigable 3D world: Marble, Atlas, HunyuanWorld, WonderWorld, Lyra, Voyager…

#### Atlas — World Labs (2026-09-01)
- Type: Model · Timing: Pre-generated · Access: Waitlist / early access
- Input: Image, Camera path / pose, Video → Output: Flat video, Gaussian splats / radiance field, Image / panorama
- Idea: One model now spans imagined and real places: the more photos of a site you give it, the less it invents, which makes 'grounded versus imagined' a dial a study can set.
- What it is: World Labs' 'omni' world model, pretrained from scratch on text, images, video and 3D: from one to a few reference images and a hand-designed camera path it generates up to one minute of 1440p video, reconstructs real places from one to over a hundred photos, and outputs point clouds or Gaussian splats. Early access only as of October 2026; World Labs says it will power future versions of Marble.
- How it works: A multimodal autoregressive diffusion transformer encodes every input image at a 3D position in a shared spatial context and generates new frames and depth maps conditioned on it with pixel-exact camera geometry; depth is fused into point clouds and completed into 3D Gaussian splats.
- Specs: up to 60 s video at 1440p · 1–6 reference images for generation · reconstruction from 1 to 100+ images · point cloud / 3DGS output
- Capability: Persistence, Experimental control, Perceptual realism
- Video: https://www.youtube.com/watch?v=hzvXRHBInx0
- Images: https://www.worldlabs.ai/images/atlas-og.jpg
- Project page: https://www.worldlabs.ai/blog/atlas

#### Echo-2 — SpAItial (2026-04)
- Type: Model · Timing: Pre-generated · Access: Product / app
- Input: Image, Text prompt → Output: Gaussian splats / radiance field, 3D scene / world
- Idea: World generation is becoming a tool call: an agent can now request, edit and hand over a 3D place in the middle of a conversation.
- What it is: SpAItial's second world model generates real-time navigable 3D scenes from text or images that run in a browser on any device; in June 2026 the company added a Claude plugin and hosted MCP server for generating and editing worlds from a chat.
- How it works: Generates one spatially persistent 3D scene per prompt instead of a frame sequence; SpAItial claims it outperforms Marble 1.1 on the WorldScore benchmark (company claim, not independently verified).
- Capability: Persistence, Authoring accessibility
- Video: https://www.youtube.com/watch?v=2CIoyGoGHZs
- Images: https://spaitial.ai/og-image-default.png
- Project page: https://www.spaitial.ai/

#### HY-World 2.0 — Tencent Hunyuan (2026-04-16)
- Type: Model · Timing: Pre-generated · Access: Open weights / code, Product / app
- Input: Text prompt, Image, Video → Output: Gaussian splats / radiance field, Mesh / 3D asset, 3D scene / world
- Idea: Tencent frames it explicitly against video world models: build the world once as assets and render it for free, instead of paying per frame for a world that disappears.
- What it is: Tencent's second-generation open world model: text or a single image is expanded into a navigable 3D Gaussian-splat or mesh world, and multi-view photos or video are reconstructed into 3D, with outputs that import into Blender, Unity, Unreal Engine and Isaac Sim. Weights were released in April–May 2026; an HY World 2.1 update, usable in Tencent's web product, followed in July 2026.
- How it works: Four stages: HY-Pano 2.0 (about 80B parameters) generates a panorama, WorldNav plans camera trajectories, WorldStereo 2.0 (about 17B) expands the world with keyframe views and geometric memory, and WorldMirror 2.0, a feed-forward model predicting depth, normals, cameras, points and 3DGS, composes the final world.
- Specs: HY-Pano 2.0 ~80B · WorldStereo 2.0 ~17B · 3DGS / mesh output
- Capability: Persistence, Experimental control, Authoring accessibility
- Paper: https://arxiv.org/abs/2604.14268 (Technical report 2026)
- Video: https://github.com/user-attachments/assets/b56f4750-25c9-48fb-83ff-d58526711463
- Images: https://raw.githubusercontent.com/Tencent-Hunyuan/HY-World-2.0/main/assets/teaser.png
- Project page: https://github.com/Tencent-Hunyuan/HY-World-2.0
- Code: https://github.com/Tencent-Hunyuan/HY-World-2.0

#### Lyra 2.0 — NVIDIA (2026-04-15)
- Type: Model · Timing: Pre-generated · Access: Open weights / code
- Input: Image, Camera path / pose → Output: Gaussian splats / radiance field, Mesh / 3D asset, Flat video
- Idea: It targets the two failures that limit long generated walks, forgetting places that fall out of context and drifting appearance, which are also what break a participant's sense of a stable place.
- What it is: NVIDIA's open successor to Lyra for large environments: it generates long camera-controlled walkthroughs that can turn back and revisit places, and lifts them into a persistent 3D world exportable as splats or meshes, for example as robot training scenes in Isaac Sim. GUI and training code were released in July 2026.
- How it works: Per-frame 3D geometry is kept only to retrieve relevant past frames and build dense correspondences with the target view (against spatial forgetting), the video model is trained on self-augmented histories of its own degraded outputs (against drift), and the long trajectories fine-tune feed-forward reconstruction into 3D Gaussians and meshes.
- Specs: long-horizon walkthroughs with revisits · 3DGS and mesh export
- Capability: Persistence, Situational reach
- Paper: https://arxiv.org/abs/2604.13036 (SIGGRAPH Asia 2026 (accepted))
- Video: https://nv-tlabs.github.io/Project-Lyra/assets/teaser.mp4
- Images: https://nv-tlabs.github.io/Project-Lyra/assets/method_v2.png
- Project page: https://nv-tlabs.github.io/Project-Lyra/
- Code: https://github.com/nv-tlabs/lyra

#### Echo — SpAItial (2025-12)
- Type: Model · Timing: Pre-generated · Access: Waitlist / early access
- Input: Image, Text prompt → Output: Gaussian splats / radiance field, 3D scene / world
- Idea: A second company, from the Munich 3D-vision community, now sells persistent splat worlds, so researchers are not tied to a single vendor's format.
- What it is: SpAItial's first world model: a single image or short text prompt becomes a metric-scale 3D Gaussian-splat environment that can be explored freely in real time in a web browser.
- How it works: SpAItial describes inferring one unified metric-scale scene representation of geometry and appearance from which every frame and depth map is rendered, displayed with 3D Gaussian splatting; the architecture is unpublished.
- Capability: Persistence, Perceptual realism
- Video: https://www.youtube.com/watch?v=mlkRiJfuARw
- Project page: https://www.spaitial.ai/

#### Marble — World Labs (2025-11-12)
- Type: Product / app · Timing: Pre-generated · Access: Product / app, Public API
- Input: Text prompt, Image, Video → Output: Gaussian splats / radiance field, Mesh / 3D asset, 3D scene / world
- Idea: A researcher can author a whole set from a prompt or a few photos and then keep, version and reload exactly the same world for every participant.
- What it is: World Labs' world-generation product: text, one or more photos, a video or a coarse 3D layout become a persistent 3D world that can be edited, expanded, stitched with others and exported as Gaussian splats, meshes or video. Beta from 2025-09-16, generally available from 2025-11-12; Marble 1.1 and 1.1 Plus (larger worlds) followed in 2026, and the World API opened it to developers on 2026-01-21.
- How it works: A proprietary multimodal world model generates a 3D Gaussian-splat world (with optional mesh extraction) from the inputs; a layout editor (Chisel) separates coarse 3D structure from visual style, and worlds render on web, mobile and VR through World Labs' open-source Spark renderer.
- Specs: text / image / multi-image / video / 3D layout in · Gaussian splats, mesh or video out · Marble 1.1 Plus for larger worlds
- Capability: Authoring accessibility, Persistence, Perceptual realism
- Video: https://www.youtube.com/watch?v=UslQB4LUueI
- Images: https://www.worldlabs.ai/images/nov12-thumbnail.jpg
- Project page: https://www.worldlabs.ai/blog/marble-world-model
- API docs: https://docs.worldlabs.ai/api

#### FlashWorld — Xinyang Li, Tencent Hunyuan (2025-10-16)
- Type: Model · Timing: Pre-generated · Access: Open weights / code
- Input: Text prompt, Image → Output: Gaussian splats / radiance field, 3D scene / world
- Idea: When a world takes seconds instead of minutes, scenes can be regenerated between trials or sampled in large numbers for a study.
- What it is: An open model that produces a 3D Gaussian-splat scene from a single image or a text prompt in about 5–10 seconds on one GPU, with a browser demo for viewing the result.
- How it works: A multi-view diffusion model built on a video-diffusion prior is pre-trained in two modes (multi-view images and direct 3D Gaussians) and then distilled so that the fast 3D-oriented mode matches the visual quality of the multi-view mode.
- Specs: 5–10 s per scene on one GPU · authors report 10–100× faster than prior work
- Capability: Temporal responsiveness, Situation diversity, Authoring accessibility
- Paper: https://arxiv.org/abs/2510.13678 (ICLR 2026 (oral))
- Video: https://www.youtube.com/watch?v=nUIiCj8J6B4
- Images: https://imlixinyang.github.io/FlashWorld-Project-Page/static/images/teaser.png
- Project page: https://imlixinyang.github.io/FlashWorld-Project-Page/
- Code: https://github.com/imlixinyang/FlashWorld

#### Lyra — NVIDIA (2025-09-23)
- Type: Model · Timing: Pre-generated · Access: Open weights / code
- Input: Text prompt, Image, Video → Output: Gaussian splats / radiance field, Dynamic 3D / 4D
- Idea: The 3D knowledge already inside a video model can be read out as a scene, without any multi-view training data.
- What it is: NVIDIA's open model that turns a single image (or a video, for dynamic scenes) into an explicit 3D Gaussian-splat scene in one feed-forward pass, ready for real-time rendering and simulation such as Isaac Sim.
- How it works: Self-distillation: a 3DGS decoder is added beside the RGB decoder of a camera-controlled video diffusion model (GEN3C on Cosmos) and trained only on the model's own synthetic outputs to match the decoded video.
- Specs: single image → 3DGS · video → dynamic 3DGS · feed-forward
- Capability: Persistence, Situational reach
- Paper: https://arxiv.org/abs/2509.19296 (ICLR 2026)
- Video: https://research.nvidia.com/labs/toronto-ai/lyra/assets/videos/teaser/teaser.mp4
- Images: https://research.nvidia.com/labs/toronto-ai/lyra/assets/images/isaac/apartment_1.png
- Project page: https://research.nvidia.com/labs/toronto-ai/lyra/
- Code: https://github.com/nv-tlabs/lyra

#### HunyuanWorld-Voyager — Tencent Hunyuan (2025-09-02)
- Type: Model · Timing: Pre-generated · Access: Open weights / code
- Input: Image, Camera path / pose → Output: Flat video, 3D scene / world
- Idea: Generating depth with every frame means the world is rebuilt as you go instead of being recovered afterwards by structure-from-motion.
- What it is: An open video-diffusion model that, from one image and a user-drawn camera path, generates aligned RGB and depth video, so each step of the walk is also a 3D point cloud that can be reconstructed directly into a scene.
- How it works: World-consistent video diffusion jointly denoises RGB and depth conditioned on a world cache of earlier points (with point culling), extended autoregressively with smooth video sampling for long-range exploration; trained on a scalable data engine of real and Unreal Engine video with estimated cameras and depth.
- Specs: RGB-D video along a user camera path · direct point-cloud reconstruction
- Capability: Persistence, Experimental control
- Paper: https://arxiv.org/abs/2506.04225 (ACM TOG (SIGGRAPH Asia 2025))
- Video: https://github.com/user-attachments/assets/2eb844c9-30ba-4770-8066-189c123affee
- Images: https://raw.githubusercontent.com/Tencent-Hunyuan/HunyuanWorld-Voyager/main/assets/teaser.png
- Project page: https://github.com/Tencent-Hunyuan/HunyuanWorld-Voyager
- Code: https://github.com/Tencent-Hunyuan/HunyuanWorld-Voyager

#### Matrix-3D — Skywork (Kunlun Tech) (2025-08-12)
- Type: Model · Timing: Pre-generated · Access: Open weights / code
- Input: Text prompt, Image, Camera path / pose → Output: 360° / stereo video, Gaussian splats / radiance field, 3D scene / world
- Idea: Generating panoramic rather than forward-facing video removes the empty regions behind the viewer that make most single-image worlds feel like stage sets.
- What it is: An open framework that turns a text prompt or image into an omnidirectional, explorable 3D world: it first generates a 360° panoramic video along a chosen trajectory, then reconstructs that video into a 3D Gaussian-splat scene.
- How it works: A trajectory-guided panoramic video diffusion model conditioned on scene-mesh renders generates the walk; it is lifted to 3D either by a feed-forward large panorama reconstruction model or by an optimisation pipeline, trained on the synthetic Matrix-Pano dataset.
- Specs: 360° panoramic video → 3DGS · 5B low-VRAM mode (12 GB)
- Capability: Persistence, Situational reach
- Paper: https://arxiv.org/abs/2508.08086 (Technical report 2025)
- Video: https://www.youtube.com/watch?v=cOmIVyade-c
- Images: https://matrix-3d.github.io/static/images/fig2.png
- Project page: https://matrix-3d.github.io/
- Code: https://github.com/SkyworkAI/Matrix-3D

#### HunyuanWorld 1.0 — Tencent Hunyuan (2025-07-26)
- Type: Model · Timing: Pre-generated · Access: Open weights / code, Product / app
- Input: Text prompt, Image → Output: Mesh / 3D asset, Image / panorama, 3D scene / world
- Idea: Panorama-first generation gives a complete 360° surround in mesh form that ordinary CG pipelines can open, at the cost of limited walking range.
- What it is: Tencent's open-weight world generator: a text prompt or image becomes a 360° panorama that is then decomposed into layered 3D meshes (sky, background, separable objects) for exploration in a browser, headset or game engine. A quantised 'lite' version (August 2025) runs on consumer GPUs such as the RTX 4090.
- How it works: Panorama diffusion models (PanoDiT) generate a 360° world proxy, which is segmented into semantic layers, lifted to 3D with depth estimation and inpainting, and exported as layered meshes with disentangled objects.
- Specs: 360° panorama proxy · layered mesh export · lite version on consumer GPUs
- Capability: Persistence, Authoring accessibility, Situation diversity
- Paper: https://arxiv.org/abs/2507.21809 (Technical report 2025)
- Video: https://github.com/user-attachments/assets/747b3e41-df9c-4cd2-b1d1-c0dce63f63ef
- Images: https://raw.githubusercontent.com/Tencent-Hunyuan/HunyuanWorld-1.0/main/assets/teaser.png
- Project page: https://3d-models.hunyuan.tencent.com/world/
- Code: https://github.com/Tencent-Hunyuan/HunyuanWorld-1.0

#### Large World Model demo (Generating Worlds) — World Labs (2024-12-02)
- Type: Research demo · Timing: Pre-generated · Access: Research only
- Input: Image → Output: 3D scene / world, Gaussian splats / radiance field
- Idea: A generated world becomes a place you can return to rather than a clip that ends, though these first worlds were small and bounded.
- What it is: World Labs' first public result: a single image is turned into a 3D scene that can be explored in the browser in real time, with interactive camera effects such as depth of field and dolly zoom.
- How it works: A generative model (details unpublished) lifts one image into an explicit 3D representation that is rendered client-side in real time; World Labs describes it as a first step toward large world models.
- Specs: single image in · real-time browser rendering
- Capability: Persistence, Perceptual realism
- Video: https://wlt-ai-cdn.art/videos/banner_video.mp4
- Images: https://www.worldlabs.ai/images/generating-worlds-nologo.jpg
- Project page: https://www.worldlabs.ai/blog/generating-worlds

#### WonderWorld — Hong-Xing (Koven) Yu (2024-06-13)
- Type: Research demo · Timing: Turn-based · Access: Open weights / code
- Input: Image, Text prompt, Camera path / pose → Output: Gaussian splats / radiance field, 3D scene / world
- Idea: Generation fast enough to answer a user's request turns the participant into a co-author of the world.
- What it is: From one image, a user moves the camera and types what should appear there; WonderWorld generates each new connected 3D scene in under ten seconds, so a world is built interactively piece by piece.
- How it works: Fast Layered Gaussian Surfels (FLAGS) are initialised directly from estimated geometry in foreground, background and sky layers, avoiding slow per-scene optimisation, with guided depth diffusion to keep new scenes geometrically connected.
- Specs: < 10 s per new scene on one A6000 GPU (authors)
- Capability: Temporal responsiveness, Co-creation & agency, Authoring accessibility
- Paper: https://arxiv.org/abs/2406.09394 (CVPR 2025)
- Video: https://kovenyu.com/wonderworld/interactive_converted_60fps_trimmed_cropped/cathedral_2_interactive_compressed_60fps_trimmed_cropped.mp4
- Images: https://kovenyu.com/wonderworld/complete/venice.jpg
- Project page: https://kovenyu.com/wonderworld/
- Code: https://github.com/KovenYu/WonderWorld

#### WonderJourney — Hong-Xing (Koven) Yu (2023-12-06)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code
- Input: Text prompt, Image → Output: 3D scene / world, Flat video
- Idea: Letting a language model write 'what comes next' turns scene generation into open-ended travel, but each step is only a short, view-dependent 3D patch.
- What it is: Starting from any image or text, WonderJourney generates a long sequence of connected 3D scenes, flying from a painting into a mountain range or a poem's landscape, rendered as a continuous camera journey.
- How it works: An LLM proposes the next scene description, a text-to-image model with depth estimation builds a point-cloud scene, and a vision-language model checks the result before the camera moves on.
- Capability: Situation diversity, Situational reach
- Paper: https://arxiv.org/abs/2312.03884 (CVPR 2024)
- Video: https://www.youtube.com/watch?v=2X8TU3KwZ-c
- Project page: https://kovenyu.com/wonderjourney/
- Code: https://github.com/KovenYu/WonderJourney

#### LucidDreamer — Jaeyoung Chung (2023-11-22)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code
- Input: Text prompt, Image → Output: Gaussian splats / radiance field, 3D scene / world
- Idea: Inpainting plus depth was enough to grow a coherent splat scene from one prompt, the recipe many later world generators refined.
- What it is: Generates a whole 3D Gaussian-splat scene, not a single object, from a text prompt or an image, in any style, by repeatedly imagining new views and stitching them into one point cloud.
- How it works: 'Dreaming' alternates Stable Diffusion inpainting of a moved camera view with monocular depth lifting into a shared point cloud; 'alignment' merges the points, which initialise a 3D Gaussian splatting optimisation.
- Capability: Situation diversity, Perceptual realism
- Recognition: IEEE TVCG 2025 Best Paper Runner-Up
- Paper: https://arxiv.org/abs/2311.13384 (IEEE TVCG 2025)
- Video: https://github.com/user-attachments/assets/35004aaa-dffc-4133-b15a-05224e68b91e
- Project page: https://luciddreamer-cvlab.github.io/
- Code: https://github.com/luciddreamer-cvlab/LucidDreamer

#### CityDreamer — Haozhe Xie (2023-09-01)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code
- Input: Camera path / pose → Output: 3D scene / world, Flat video
- Idea: City scale is where situations like crowds, traffic and getting lost live; CityDreamer shows generated layout and appearance can be separated at that scale.
- What it is: Generates unbounded 3D cities, street layouts, buildings and background, that can be flown through with a consistent camera, learned from Google Earth imagery and OpenStreetMap layouts.
- How it works: An unbounded layout generator produces a semantic and height map; separate neural-field generators render buildings (instance-wise) and background, composed with compact bird's-eye-view scene representations.
- Capability: Situational reach, Situation diversity
- Paper: https://arxiv.org/abs/2309.00610 (CVPR 2024)
- Video: https://www.youtube.com/watch?v=te4zinLTYz0
- Images: https://www.infinitescript.com/projects/CityDreamer/CityDreamer-Thumbnail.webp
- Project page: https://www.infinitescript.com/project/city-dreamer/
- Code: https://github.com/hzxie/CityDreamer

#### Text2Room — Lukas Höllein (2023-03-21)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code
- Input: Text prompt → Output: Mesh / 3D asset, 3D scene / world
- Idea: It was an early proof that a 2D image model plus depth can furnish an entire enterable room.
- What it is: From a text prompt, Text2Room builds a complete, textured 3D room mesh that can be walked around, by painting the room view by view with an image model.
- How it works: Iterative text-conditioned inpainting along a chosen camera trajectory, with monocular depth estimation and depth alignment, fuses each new view into a single mesh; a second pass fills holes from additional viewpoints.
- Capability: Authoring accessibility, Persistence
- Paper: https://arxiv.org/abs/2303.11989 (ICCV 2023 (oral))
- Video: https://www.youtube.com/watch?v=fjRnFL91EZc
- Images: https://lukashoel.github.io/text-to-room/static/images/teaser-min.jpg
- Project page: https://lukashoel.github.io/text-to-room/
- Code: https://github.com/lukasHoel/text2room

#### Infinite Nature — Andrew Liu, Google (2020)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code
- Input: Image, Camera path / pose → Output: Flat video, Image / panorama
- Idea: The lineage anchor for explorable worlds: it showed endless novel terrain from one image, and also how it falls apart without a persistent 3D memory.
- What it is: From a single landscape photo, Infinite Nature generates an arbitrarily long video of a drone-like flight into the scene, inventing new coastline and mountains as the camera advances.
- How it works: Render-refine-repeat: the current frame and its disparity are warped to the next camera pose, and a network inpaints and refines the result, trained on aerial nature videos.
- Capability: Situation diversity, Situational reach
- Paper: https://arxiv.org/abs/2012.09855 (ICCV 2021 (oral))
- Video: https://www.youtube.com/watch?v=oXUf6anNAtc
- Images: https://infinite-nature.github.io/teaser.png
- Project page: https://infinite-nature.github.io/
- Code: https://github.com/google-research/google-research/tree/master/infinite_nature

### 360° panoramas & skyboxes

Equirectangular worlds and skyboxes for VR, often the first layer of a generated scene.

#### LayerPano3D — Shuai Yang (2024-08-23)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code
- Input: Text prompt → Output: Gaussian splats / radiance field, Image / panorama
- Idea: Layering the panorama is a cheap way to add parallax and disocclusion, which is what makes a 360° image feel like a place in a headset.
- What it is: Generates a full-view 360° panorama from text and splits it into depth layers turned into 3D Gaussians, so a viewer can walk a short distance and see occluded content appear behind objects.
- How it works: Text-guided anchor views are synthesised into a high-resolution panorama, decomposed into layered panoramas by depth with inpainting of hidden content, and each layer is optimised as 3D Gaussians.
- Capability: Perceptual realism, Persistence
- Paper: https://arxiv.org/abs/2408.13252 (SIGGRAPH 2025)
- Video: https://www.youtube.com/watch?v=lpNs5JwaJoA
- Project page: https://ys-imtech.github.io/projects/LayerPano3D/
- Code: https://github.com/YS-IMTech/LayerPano3D

#### DreamScene360 — Shijie Zhou (2024-04-10)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code
- Input: Text prompt → Output: Gaussian splats / radiance field, Image / panorama
- Idea: A panorama is a convenient first layer for a VR scene: it fixes the whole surround before any 3D is built.
- What it is: Turns a text prompt into a full 360° 3D scene: a generated panorama is lifted into Gaussian splats that can be viewed from any direction with limited movement.
- How it works: A GPT-4V self-refinement loop improves the prompt, a 2D diffusion model generates the panorama, monocular depth initialises a panoramic 3D Gaussian set, and semantic and geometric regularisation on synthesised virtual views fills unseen regions.
- Capability: Authoring accessibility, Persistence
- Paper: https://arxiv.org/abs/2404.06903 (ECCV 2024)
- Video: https://www.youtube.com/watch?v=6rMIQfe7b24
- Images: https://raw.githubusercontent.com/ShijieZhou-UCLA/DreamScene360/main/assets/teaser_v6.png
- Project page: https://dreamscene360.github.io/
- Code: https://github.com/ShijieZhou-UCLA/DreamScene360

#### Skybox AI — Blockade Labs (2023)
- Type: Product / app · Timing: Pre-generated · Access: Product / app, Public API
- Input: Text prompt, Sketch & gesture, Image → Output: Image / panorama
- Idea: The quickest way to put a participant inside a generated surround, but a skybox stays a backdrop: nothing in it can be reached or moved.
- What it is: A web tool and API that generates 360° equirectangular skyboxes from a prompt or a rough sketch, with style packs, remixing of existing 360° photos, HDRI lighting export and a depth-based 'world mesh' export for game engines and VR.
- How it works: Proprietary diffusion models (Model 3 and later) trained for seamless equirectangular output; depth estimation turns the panorama into a simple enclosing mesh.
- Capability: Authoring accessibility, Situation diversity
- Video: https://www.youtube.com/watch?v=eKO49j-ibaA
- Images: https://static.wixstatic.com/media/8d6639_b2ee76a88e224659804c1ef09c7bc5da~mv2.jpg
- Project page: https://www.blockadelabs.com/
- API docs: https://api-documentation.blockadelabs.com/api/

#### MVDiffusion — Shitao Tang (2023-07-03)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code
- Input: Text prompt, Image → Output: Image / panorama
- Idea: Treating a panorama as many views that must agree, rather than one wide image, removes seams and drift at the wrap-around edge.
- What it is: Generates a seamless 360° panorama from text by producing eight overlapping perspective views at once that agree with each other; the same idea also textures a scanned room mesh consistently.
- How it works: Correspondence-aware attention layers inserted into a pretrained Stable Diffusion model share features between pixel-correspondent locations of the views, which are denoised in parallel.
- Capability: Perceptual realism, Persistence
- Paper: https://arxiv.org/abs/2307.01097 (NeurIPS 2023 (spotlight))
- Video: https://mvdiffusion.github.io/pics/panorama/1_h264.mp4
- Images: https://mvdiffusion.github.io/assets/images/teaser_v2.gif
- Project page: https://mvdiffusion.github.io/
- Code: https://github.com/Tangshitao/MVDiffusion

#### Text2Light — Zhaoxi Chen (2022)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code
- Input: Text prompt → Output: Image / panorama
- Idea: A generated environment can also light the scene, so virtual people and objects look as if they belong in it.
- What it is: Generates high-resolution HDR 360° panoramas from a text description, usable both as an immersive backdrop and as physically based lighting for rendering 3D scenes.
- How it works: Zero-shot two-stage pipeline: a text-driven low-resolution LDR panorama is generated with CLIP guidance and hierarchical codebooks, then upscaled by a structure-aware super-resolution network and lifted to HDR.
- Capability: Perceptual realism, Authoring accessibility
- Paper: https://arxiv.org/abs/2209.09898 (ACM TOG (SIGGRAPH Asia 2022))
- Video: https://www.youtube.com/watch?v=XDx6tOHigPE
- Images: https://frozenburning.github.io/projects/text2light/img/teaser.jpg
- Project page: https://frozenburning.github.io/projects/text2light/
- Code: https://github.com/FrozenBurning/Text2Light

### Layout, procedural & code-built scenes

Scenes assembled by language models, procedural rules or programs: Holodeck, Infinigen, scene graphs.

#### WorldClaw — Tencent Hunyuan (2026-08-07)
- Type: Research demo · Timing: Pre-generated · Access: Research only
- Input: Text prompt → Output: Mesh / 3D asset, 3D scene / world
- Idea: Agents that plan, build and then inspect renders can scale generation from a room to a landscape while keeping every object editable.
- What it is: A Tencent Hunyuan agentic system that turns one open-ended prompt into a large, explorable open-world 3D scene with terrain, regions and editable instance-level assets.
- How it works: Planning agents write a structured specification (regions, terrain, assets, materials, spatial relations); a region-aware height field and semantic layout form the terrain, detailed regions are generated as terrain-conditioned compositions and reconstructed into textured meshes, and render-based agents refine terrain, objects and contacts.
- Capability: Situational reach, Authoring accessibility, Experimental control
- Paper: https://arxiv.org/abs/2608.05248 (arXiv 2026)
- Video: https://tencent-hunyuan.github.io/Hunyuan3D-WorldClaw/media/worldclaw-teaser.mp4
- Images: https://tencent-hunyuan.github.io/Hunyuan3D-WorldClaw/assets/worldclaw-share.jpg
- Project page: https://tencent-hunyuan.github.io/Hunyuan3D-WorldClaw/
- Code: https://github.com/Tencent-Hunyuan/Hunyuan3D-WorldClaw

#### SAGE — NVIDIA (2026-02-10)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code
- Input: Text prompt → Output: 3D scene / world, Mesh / 3D asset
- Idea: Generating the situation from the task description, then checking it with critics, is the same loop a study needs when its scenario must be both varied and valid.
- What it is: Given an embodied task such as 'pick up a bowl and place it on the table', SAGE's agent generates a physically valid, simulation-ready room for it and refines it until it passes its own checks; NVIDIA released code and the SAGE-10k scene dataset.
- How it works: An LLM agent couples layout and object-composition generators (including TRELLIS assets) with critics for semantic plausibility, visual realism and physical stability, iterating until the scene meets intent and loads stably in Isaac Sim.
- Specs: SAGE-10k dataset · Isaac Sim / Isaac Lab
- Capability: Situational reach, Situation diversity, Behavioral plausibility
- Paper: https://arxiv.org/abs/2602.10116 (arXiv 2026)
- Video: https://research.nvidia.com/labs/cosmos-lab/sage/assets/video-sage.mp4
- Images: https://research.nvidia.com/labs/cosmos-lab/sage/assets/images/teaser.png
- Project page: https://research.nvidia.com/labs/cosmos-lab/sage/
- Code: https://github.com/NVlabs/sage

#### WorldGen — Meta (2025-11-20)
- Type: Research demo · Timing: Pre-generated · Access: Research only
- Input: Text prompt → Output: Mesh / 3D asset, 3D scene / world
- Idea: Walkability comes first: the layout and navmesh are planned before appearance, so the world works as a level, not only as a view.
- What it is: Meta Reality Labs' research system that turns a single text prompt into a traversable, fully textured 3D world (reported up to about 50 × 50 m) with a navigation mesh, ready to explore or edit in Unity or Unreal Engine. Research only as of October 2026.
- How it works: LLM-driven layout reasoning and procedural blockout produce a navmesh-aware scene plan, a reference image is generated, image-to-3D reconstruction builds the scene, and object-aware decomposition and per-object enhancement and texturing finish the world.
- Specs: scenes up to ~50 × 50 m (reported) · navmesh · Unity / Unreal export
- Capability: Authoring accessibility, Situational reach, Persistence
- Paper: https://arxiv.org/abs/2511.16825 (CVPR 2026)
- Video: https://www.youtube.com/watch?v=mzuyLODsUTM
- Images: https://arxiv.org/html/2511.16825v1/x1.png
- Project page: https://www.meta.com/blog/worldgen-3d-world-generation-reality-labs-generative-ai-research/

#### BlenderMCP — Siddharth Ahuja (2025-03)
- Type: Open-source tool · Timing: Turn-based · Access: Open weights / code
- Input: Text prompt, Image → Output: 3D scene / world, Mesh / 3D asset
- Idea: Scene building by conversation inside a professional tool: the language model writes the code, the person keeps the file.
- What it is: An open-source add-on and Model Context Protocol server that lets Claude and other language models inspect and edit a live Blender scene: creating and placing objects, applying materials, pulling Poly Haven assets and calling 3D generators.
- How it works: A Blender add-on opens a socket server; an MCP server exposes tools (scene inspection, object creation, Python execution, asset search) that the language model calls turn by turn.
- Capability: Authoring accessibility, Co-creation & agency
- Video: https://www.youtube.com/watch?v=DqgKuLYUv00
- Project page: https://github.com/ahujasid/blender-mcp
- Code: https://github.com/ahujasid/blender-mcp

#### Holodeck — Yue Yang, Allen Institute for AI (Ai2) (2023-12-14)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code
- Input: Text prompt → Output: 3D scene / world, Mesh / 3D asset
- Idea: The language model writes the scene as constraints, so every generated room is an inspectable specification that can be logged, varied and rebuilt.
- What it is: From a prompt such as 'a 1b1b apartment of a researcher who has a cat', Holodeck builds a complete interactive multi-room environment in AI2-THOR, with floor plan, materials, doors, windows and furnished objects that embodied agents can navigate.
- How it works: GPT-4 proposes floor plans, materials and object lists with spatial-relation constraints; assets are retrieved from Objaverse and a constraint solver optimises the layout before the scene is loaded into the AI2-THOR simulator.
- Capability: Authoring accessibility, Situation diversity, Experimental control
- Paper: https://arxiv.org/abs/2312.09067 (CVPR 2024)
- Video: https://www.youtube.com/watch?v=Pk5BcEqqPoU
- Images: https://yueyang1996.github.io/holodeck/static/images/floorplan_customizability.jpg
- Project page: https://yueyang1996.github.io/holodeck/
- Code: https://github.com/allenai/Holodeck

#### Infinigen — Alexander Raistrick, Princeton Vision & Learning Lab (2023-06-15)
- Type: Open-source tool · Timing: Pre-generated · Access: Open weights / code
- Input: Scene spec, code & rules → Output: 3D scene / world, Mesh / 3D asset
- Idea: Procedural generation gives what learned generators cannot: every parameter of a scene is known, seedable and reproducible.
- What it is: An open-source procedural generator that creates unlimited photorealistic natural worlds, terrain, plants, animals, weather, entirely from code in Blender, with exact ground truth for depth, segmentation and geometry. Infinigen Indoors (CVPR 2024) extended it to furnished rooms, followed by articulated simulation-ready assets (2025) and the ProcFunc abstractions (2026).
- How it works: Every asset, from geometry to materials, is generated by randomised mathematical rules (no external assets), composed into scenes by constraint-based arrangement and rendered with Blender's path tracer.
- Specs: fully procedural · no external assets · ground-truth depth, normals, segmentation
- Capability: Situation diversity, Experimental control, Perceptual realism
- Paper: https://arxiv.org/abs/2306.09310 (CVPR 2023)
- Video: https://www.youtube.com/watch?v=6tgspeI-GHY
- Images: https://infinigen.org/img/social_card.png
- Project page: https://infinigen.org/
- Code: https://github.com/princeton-vl/infinigen

#### LayoutGPT — Weixi Feng (2023-05-24)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code
- Input: Text prompt → Output: 3D scene / world
- Idea: Layout written as text is the most controllable layer of a generated scene: it can be read, edited and diffed before anything is rendered.
- What it is: Shows that a text-only language model, prompted with CSS-style examples, can write numeric layouts: bounding boxes for images and object positions and sizes for 3D indoor rooms.
- How it works: In-context learning with retrieved exemplars in a CSS-like format lets GPT-3.5/4 output layouts, which condition a layout-to-image model or place furniture in 3D-FRONT rooms.
- Capability: Experimental control, Authoring accessibility
- Paper: https://arxiv.org/abs/2305.15393 (NeurIPS 2023)
- Video: https://layoutgpt.github.io/static/videos/merged_scenes.mp4
- Images: https://layoutgpt.github.io/static/images/3d_qualitative.png
- Project page: https://layoutgpt.github.io/
- Code: https://github.com/weixi-feng/LayoutGPT

### Photos to spatial scenes

One photo to a 3D scene with depth and parallax: spatial scenes, monocular depth, single-image splats.

#### Hyper3D WorldGen — Deemos (Hyper3D Rodin) (2026-09-09)
- Type: Product / app · Timing: Pre-generated · Access: Product / app
- Input: Image → Output: Mesh / 3D asset, Gaussian splats / radiance field, 3D scene / world
- Idea: Objects arrive with physical properties, so a photographed room can become an interactive scene rather than a backdrop.
- What it is: Hyper3D's scene generator turns a single photo into a 3D scene of independent, editable objects (generated as Rodin meshes with estimated collision geometry, mass and friction) set in a Gaussian-splat background, for robotics simulation, film, games and spatial computing.
- How it works: Building on CAST, objects are detected automatically or by user boxes, completed in 3D, placed via a contact, support and suspension relation graph with estimated pose, scale and physics, while the background is reconstructed as 3D Gaussian splats.
- Capability: Behavioral plausibility, Authoring accessibility, Persistence
- Video: https://www.youtube.com/watch?v=-rhncMVVtGM
- Images: https://storage.deemos.dev/features/worldgen/introBg.webp
- Project page: https://hyper3d.ai/features/worldgen

#### SHARP — Apple (2025-12-11)
- Type: Model · Timing: Pre-generated · Access: Open weights / code
- Input: Image → Output: Gaussian splats / radiance field
- Idea: Sub-second, metric splats from one photo make 'step into this picture' cheap enough to do for every stimulus image, though only for small head movements.
- What it is: Apple's open model that converts a single photo into a metric-scale 3D Gaussian representation in under a second on a standard GPU, which then renders photorealistic nearby views in real time.
- How it works: A single feed-forward network regresses the parameters of 3D Gaussians from one image with absolute scale; the authors report LPIPS 25–34% and DISTS 21–43% lower than the best prior model with three orders of magnitude less synthesis time.
- Specs: < 1 s per image on a standard GPU · metric-scale 3DGS · real-time rendering
- Capability: Temporal responsiveness, Perceptual realism
- Paper: https://arxiv.org/abs/2512.10685 (ICLR 2026)
- Video: https://www.youtube.com/watch?v=pSQSsXqQlcY
- Images: https://apple-aiml-research.github.io/ml-sharp/teaser.jpg
- Project page: https://apple-aiml-research.github.io/ml-sharp/
- Code: https://github.com/apple/ml-sharp

#### Spatial Scenes (visionOS 26) — Apple (2025-06-09)
- Type: Product / app · Timing: Pre-generated · Access: Product / app, Public API
- Input: Image → Output: 3D scene / world, Image / panorama
- Idea: Photo-to-3D now ships by default in a headset OS, so personal photos become a ready source of familiar, real places for immersive studies.
- What it is: A visionOS 26 feature that turns any 2D photo into a spatial scene with depth and multiple perspectives, so the viewer can lean in and look around it on Apple Vision Pro (and as parallax on the iOS 26 Lock Screen), and developers get a Spatial Scene API. With visionOS 27, announced at WWDC on 2026-06-08, Vision Pro users can also turn panoramas into spatial scenes and use them as personal Environments.
- How it works: Apple describes 'a new generative AI algorithm and computational depth' that infers geometry and fills disoccluded regions to create multiple perspectives; the model is not published (Apple's SHARP research addresses the same task).
- Capability: Perceptual realism, Authoring accessibility
- Video: https://www.apple.com/newsroom/videos/2025/autoplay/06/visionos-26-introduces-powerful-new-spatial-experiences-for-apple-vision-pro/apple-wwdc25-visionos-26-spatial-scenes-photos-app/large_2x.mp4
- Images: https://www.apple.com/newsroom/images/2025/06/visionos-26-introduces-powerful-new-spatial-experiences-for-apple-vision-pro/tile/Apple-WWDC25-visionOS-26-hero-250609-lp.jpg.og.jpg
- Project page: https://www.apple.com/newsroom/2025/06/visionos-26-introduces-powerful-new-spatial-experiences-for-apple-vision-pro/

#### Bolt3D — Stanislaw Szymanowicz, Google (2025-03-18)
- Type: Research demo · Timing: Pre-generated · Access: Research only
- Input: Image, Multi-view capture / scan → Output: Gaussian splats / radiance field, 3D scene / world
- Idea: Direct sampling of 3D, rather than of images to be reconstructed later, is what brings scene generation down to seconds.
- What it is: Generates a 3D Gaussian-splat scene from one or a few images in under seven seconds on a single GPU, without per-scene optimisation.
- How it works: A latent diffusion model built on 2D diffusion architectures directly outputs splatter-image-style 3D Gaussians and geometry, trained on a large multi-view dataset whose geometry was densely reconstructed beforehand.
- Specs: < 7 s per scene on one GPU · up to 300× lower inference cost than optimisation-based methods (authors)
- Capability: Temporal responsiveness, Perceptual realism
- Paper: https://arxiv.org/abs/2503.14445 (ICCV 2025)
- Video: https://szymanowiczs.github.io/bolt3d/videos/single_vs_2_view.mp4
- Images: https://szymanowiczs.github.io/bolt3d/img/rep_img.png
- Project page: https://szymanowiczs.github.io/bolt3d

#### Stable Virtual Camera — Stability AI (2025-03-18)
- Type: Model · Timing: Pre-generated · Access: Open weights / code
- Input: Image, Multi-view capture / scan, Camera path / pose → Output: Flat video, Image / panorama
- Idea: A scene can be 'filmed' along an exact camera path from a handful of photos without building 3D at all, useful for standardised stimulus videos.
- What it is: Stability AI's open view-synthesis model: from one or more photos and any target camera path (orbits, spirals, dolly zooms), it generates 3D-consistent novel views and smooth videos up to about half a minute long, with loop closure.
- How it works: A 1.3B-parameter multi-view diffusion model conditioned on input views and target camera rays, with a two-pass procedural sampling strategy for long trajectories, without 3D distillation.
- Specs: 1.3B parameters · 576p · videos up to ~30 s
- Capability: Experimental control, Perceptual realism
- Paper: https://arxiv.org/abs/2503.14489 (arXiv 2025)
- Video: https://stable-virtual-camera.github.io/assets/task_overview.mp4
- Images: https://stable-virtual-camera.github.io/img/seva.png
- Project page: https://stable-virtual-camera.github.io/
- Code: https://github.com/Stability-AI/stable-virtual-camera

#### GEN3C — Xuanchi Ren, NVIDIA (2025-03-05)
- Type: Model · Timing: Pre-generated · Access: Open weights / code
- Input: Image, Video, Camera path / pose → Output: Flat video
- Idea: Keeping an explicit 3D cache under a video generator is a middle road: video-quality pixels, but the world stays where it was when the camera returns.
- What it is: A video model with precise camera control: from one or a few images (or a video) it renders new camera trajectories that stay consistent with the 3D content, with a GUI for drawing camera paths; built on NVIDIA Cosmos and released openly in June 2025.
- How it works: Depth predicted from the inputs is unprojected into a point-cloud 3D cache; renders of the cache along the user's camera path condition a video diffusion model, which fills holes and corrects artifacts.
- Capability: Experimental control, Persistence
- Paper: https://arxiv.org/abs/2503.03751 (CVPR 2025 (highlight))
- Video: https://github.com/nv-tlabs/gen3c_website/raw/main/assets/cosmos/compressed/gui_demo.mp4
- Images: https://research.nvidia.com/labs/toronto-ai/GEN3C/assets/cosmos/composed_single_view/grid_1_thumbnail.png
- Project page: https://research.nvidia.com/labs/toronto-ai/GEN3C/
- Code: https://github.com/nv-tlabs/GEN3C

#### CAST — Kaixin Yao, Deemos (Hyper3D Rodin) (2025-02-18)
- Type: Research demo · Timing: Pre-generated · Access: Research only
- Input: Image → Output: Mesh / 3D asset, 3D scene / world
- Idea: A photo becomes a set of objects that rest on and touch each other correctly, the precondition for anything in the scene to be picked up or pushed.
- What it is: Rebuilds a single RGB photo as a 3D scene of separate, complete object meshes placed with physically consistent contacts and support, so the scene can be edited or simulated object by object.
- How it works: Object-level segmentation and relative depth estimation feed an occlusion-aware generator that produces each object's full geometry; a pose-alignment model places objects, and a physics-aware correction step uses a relation graph to remove interpenetration and floating.
- Capability: Persistence, Behavioral plausibility, Experimental control
- Recognition: SIGGRAPH 2025 Best Paper Award
- Paper: https://arxiv.org/abs/2502.12894 (ACM TOG (SIGGRAPH 2025))
- Video: https://www.youtube.com/watch?v=xKnVOjs5go4
- Project page: https://sites.google.com/view/cast4

#### Wonderland — Hanwen Liang, Snap Inc. (2024-12-16)
- Type: Research demo · Timing: Pre-generated · Access: Research only
- Input: Image, Camera path / pose → Output: Gaussian splats / radiance field, 3D scene / world
- Idea: The compressed latents of a camera-controlled video model already encode a multi-view scene; reading 3D straight from them saves decoding and optimisation.
- What it is: From a single image, Wonderland reconstructs a wide-scope 3D Gaussian-splat scene in a feed-forward pass, including background regions far outside the photo.
- How it works: A camera-guided video diffusion model produces latents along specified trajectories; a large reconstruction model trained progressively on that latent space predicts the 3D Gaussians.
- Capability: Perceptual realism, Situational reach
- Paper: https://arxiv.org/abs/2412.12091 (arXiv 2024)
- Video: https://snap-research.github.io/wonderland/3d_autoregressive/00c5252d5_final.mp4
- Images: https://snap-research.github.io/wonderland/teaser-final.png
- Project page: https://snap-research.github.io/wonderland/

#### MoGe — Microsoft (2024-10-24)
- Type: Model · Timing: Pre-generated · Access: Open weights / code
- Input: Image → Output: Image / panorama, 3D scene / world
- Idea: Predicting a point map rather than a depth map gives a usable 3D layout of a photo, including the camera, in a single step.
- What it is: Microsoft's open models that recover a 3D point map of an open-domain photo (geometry plus camera field of view) in one pass; MoGe-2 (July 2025) added metric scale and sharper detail and MoGe-3 (August 2026) finer point-map geometry.
- How it works: A ViT model predicts affine-invariant point maps trained with a robust, optimal alignment solver and multi-scale local geometry losses; later versions add metric-scale prediction.
- Capability: Perceptual realism, Experimental control
- Paper: https://arxiv.org/abs/2410.19115 (CVPR 2025 (oral))
- Video: https://wangrc.site/MoGePage/static/videos/teaser/teaser_crf28.mp4
- Images: https://raw.githubusercontent.com/microsoft/MoGe/main/assets/overview_simplified.png
- Project page: https://wangrc.site/MoGePage/
- Code: https://github.com/microsoft/MoGe

#### Depth Pro — Apple (2024-10-02)
- Type: Model · Timing: Pre-generated · Access: Open weights / code
- Input: Image → Output: Image / panorama
- Idea: Metric depth from any photo is the cheapest step from a picture to geometry; most photo-to-scene pipelines start here.
- What it is: Apple's open monocular depth model that predicts a sharp, metric-scale depth map from a single photo, without camera intrinsics, in a fraction of a second.
- How it works: A multi-scale vision-transformer encoder with a combined real and synthetic training curriculum predicts metric depth and estimates focal length from the image itself.
- Specs: 2.25-megapixel depth map in 0.3 s on a standard GPU (authors)
- Capability: Perceptual realism, Temporal responsiveness
- Paper: https://arxiv.org/abs/2410.02073 (ICLR 2025)
- Video: https://www.youtube.com/watch?v=no5yJje_mos
- Images: https://raw.githubusercontent.com/apple/ml-depth-pro/main/data/depth-pro-teaser.jpg
- Project page: https://github.com/apple/ml-depth-pro
- Code: https://github.com/apple/ml-depth-pro

#### Depth Anything V2 — Lihe Yang, ByteDance Seed (2024-06-14)
- Type: Model · Timing: Pre-generated · Access: Open weights / code
- Input: Image, Video → Output: Image / panorama
- Idea: Reliable depth for any picture is the hidden layer under many 'generated' 3D scenes: errors in depth become errors in the world.
- What it is: Open monocular depth models (from about 25M to 1.3B parameters) that estimate fine-grained relative depth for any image, widely built into 3D-photo, 2D-to-3D video and scene-generation tools; it follows Depth Anything (January 2024).
- How it works: A teacher trained only on precise synthetic depth labels pseudo-labels about 62 million real images, on which smaller student models are trained (DINOv2 encoder with a DPT head).
- Specs: Small 25M · Base 98M · Large 335M · Giant 1.3B
- Capability: Perceptual realism, Situation diversity
- Paper: https://arxiv.org/abs/2406.09414 (NeurIPS 2024)
- Video: https://www.youtube.com/watch?v=zna5PrtDUFE
- Images: https://depth-anything-v2.github.io/static/images/teaser.png
- Project page: https://depth-anything-v2.github.io/
- Code: https://github.com/DepthAnything/Depth-Anything-V2

#### CAT3D — Ruiqi Gao, Google DeepMind (2024-05-16)
- Type: Research demo · Timing: Pre-generated · Access: Research only
- Input: Image, Multi-view capture / scan, Text prompt → Output: 3D scene / world, Image / panorama
- Idea: Multi-view diffusion fills what the camera never saw, which is why one casual photo can now become a navigable place.
- What it is: Creates a full 3D scene from any number of photos, even a single image or a text-generated picture, by first imagining many consistent novel views and then reconstructing them, in about a minute.
- How it works: A multi-view latent diffusion model conditioned on input views and target camera poses generates large sets of consistent novel views, which are fed to a robust NeRF reconstruction.
- Specs: about 1 min per scene (authors)
- Capability: Perceptual realism, Authoring accessibility
- Paper: https://arxiv.org/abs/2405.10314 (NeurIPS 2024 (oral))
- Video: https://cat3d.github.io/videos/teaser/cat_compress.mp4
- Images: https://cat3d.github.io/img/rep_img.jpeg
- Project page: https://cat3d.github.io/

#### 3D Photography using Context-aware Layered Depth Inpainting — Meng-Li Shih (2020)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code
- Input: Image → Output: Image / panorama, Flat video
- Idea: The lineage anchor for today's spatial scenes: one photo plus inpainted hidden layers already gives a convincing sense of depth.
- What it is: Turns a single RGB-D photo (depth from a phone or a depth estimator) into a '3D photo' with real parallax, synthesising the color and depth hidden behind foreground objects so the camera can move slightly.
- How it works: The photo is converted to a layered depth image; learned color and depth inpainting networks fill the occluded regions locally around depth discontinuities, and the result is rendered as a mesh.
- Capability: Perceptual realism
- Paper: https://arxiv.org/abs/2004.04727 (CVPR 2020)
- Video: https://www.youtube.com/watch?v=D0JObXCfxv0
- Project page: https://shihmengli.github.io/3D-Photo-Inpainting/
- Code: https://github.com/vt-vl-lab/3d-photo-inpainting

## 3D Assets, Characters & Motion

Objects, characters and animation generated on demand: the props and actors of an authored situation.

### Text & image to 3D

Meshes and textures from a prompt or photo: Meshy, Tripo, Rodin, Hunyuan3D, TRELLIS, SAM 3D…

#### Meshy 7 — Meshy (2026-08-12)
- Type: Model · Timing: Pre-generated · Access: Product / app, Public API
- Input: Image, Text prompt → Output: Mesh / 3D asset
- Idea: Once obvious failures are rare, 3D generators compete on faithfulness to a reference and on surface detail, which matters when a generated prop must match a specific real object. Meshy reports that Meshy 7 and 7.1 lead its own benchmarks; these are not independent tests.
- What it is: Meshy's image-to-3D model tuned for geometry alignment, meaning how closely the generated shape matches the input image, launched with Meshy's own alignment benchmark; the Meshy 7.1 update (10 September 2026) adds an Ultra 4K mode that generates geometry at 4096³ with raw meshes of up to 80 million triangles.
- How it works: Proprietary image-to-3D foundation model; for 7.1 Meshy scaled its voxel geometry representation and generation backbone from 2048³ to 4096³ and added high-precision mesh extraction and simplification.
- Specs: 7.1 Ultra 4K: 4096³ geometry · up to 80M raw triangles
- Capability: Perceptual realism, Authoring accessibility
- Video: https://www.youtube.com/watch?v=FYl0ng2haZ8
- Images: https://cdn.meshy.ai/landing-assets/blog/meshy-7/meshy-7-cover.webp https://cdn.meshy.ai/landing-assets/blog/meshy-7.1-launch/meshy-7-1-launch-cover-v2.webp
- Project page: https://www.meshy.ai/blog/meshy-7-image-to-3d-geometry-alignment
- API docs: https://docs.meshy.ai/

#### Meshy 3D Agent — Meshy (2026-05-29)
- Type: Product / app · Timing: Turn-based · Access: Product / app
- Input: Text prompt, Image, Sketch & gesture → Output: Mesh / 3D asset, Dialogue / text
- Idea: Moves asset generation from a single prompt box to a dialogue that plans and iterates, the pattern a researcher could use to author scenario props by talking.
- What it is: A conversational agent inside Meshy: a person describes an idea or uploads a photo or sketch, and the agent brainstorms directions, generates concept images in batches, turns the chosen one into a downloadable 3D model, and can rig and animate characters through chat.
- How it works: An LLM-driven agent that orchestrates Meshy's image generation, image-to-3D, texturing, rigging and animation tools in one chat; Meshy also exposes these tools to outside agents through an MCP server.
- Capability: Authoring accessibility, Co-creation & agency
- Video: https://www.youtube.com/watch?v=YwnwaCpRNGE
- Images: https://cdn.meshy.ai/landing-assets/blog/meshy-3d-agent/meshy-3d-agent-cover-new.webp
- Project page: https://www.meshy.ai/blog/meshy-3d-agent
- API docs: https://www.meshy.ai/mcp

#### Rodin Gen-2.5 — Deemos (Hyper3D Rodin) (2026-05-19)
- Type: Model · Timing: Pre-generated · Access: Product / app, Public API
- Input: Image, Text prompt → Output: Mesh / 3D asset
- Idea: Adds an LLM-style speed–quality dial to 3D generation, useful when a scenario needs many cheap background props and a few detailed focal objects.
- What it is: Rodin Gen-2.5 generates meshes of up to 10 million polygons and lets users set an adaptive 'thinking effort' that trades seconds for detail, from roughly 4-second drafts to slower hero assets, with 3D-native textures, batches of up to 10 results and manual part splitting.
- How it works: Proprietary; Deemos describes adaptive inference-time compute ('thinking effort') for geometry and texture and 3D-native texture generation, building on Gen-2's part-based pipeline.
- Specs: up to 10M polygons · 1M-poly mesh in ~4 s (developer claims)
- Capability: Perceptual realism, Experimental control
- Video: https://www.youtube.com/watch?v=ymTb7eKc9ng
- Images: https://storage.deemos.dev/assets/og-banner.png
- Project page: https://x.com/DeemosTech/status/2056744290689441833
- API docs: https://docs.hyper3d.ai/

#### TripoSplat — Tripo AI (VAST) (2026-05-07)
- Type: Model · Timing: Pre-generated · Access: Open weights / code
- Input: Image → Output: Gaussian splats / radiance field
- Idea: Generated assets in splat form can sit natively inside Gaussian-splat captures of real places, narrowing the gap between captured environments and generated props.
- What it is: VAST's open model that turns a single image into 3D Gaussians rather than a mesh, with the Gaussian density learned so that primitives concentrate where geometry is complex; released with code, weights and a ComfyUI workflow.
- How it works: Density-Sampled Gaussians (DeG): Gaussian centres are sampled from a learnable density over an octree and trained with a differentiable render-contribution gradient, and a latent diffusion model is trained on the DeG representation.
- Specs: MIT licence · variable-resolution decoding
- Capability: Perceptual realism, Authoring accessibility
- Paper: https://arxiv.org/abs/2605.16355 (SIGGRAPH 2026 (Conference Papers))
- Video: https://cdn-blog.holymolly.ai/media/production/triposplat-kv.mp4
- Images: https://cdn-blog.holymolly.ai/media/production/Splat-kv-new.webp
- Project page: https://www.tripo3d.ai/research/triposplat
- Code: https://github.com/VAST-AI-Research/TripoSplat

#### Seed3D 2.0 — ByteDance Seed (2026-04-23)
- Type: Model · Timing: Pre-generated · Access: Public API
- Input: Image, Video, Text prompt → Output: Mesh / 3D asset, 3D scene / world
- Idea: Articulated output, such as drawers that open and doors that swing, turns a generated prop into something a person or a robot can manipulate.
- What it is: Second Seed3D generation focused on geometric precision and material quality; it adds part-level segmentation and completion, articulated assets exported with joint information in URDF for simulators such as Isaac Sim, and scene composition from images, videos or text. It is offered through ByteDance's Volcano Engine Ark platform.
- How it works: Coarse-to-fine two-stage geometry generation and a unified Mixture-of-Experts PBR material model with vision-language priors for material decomposition under unknown lighting (ByteDance Seed blog).
- Capability: Perceptual realism, Behavioral plausibility
- Video: https://lf3-static.bytednsdoc.com/obj/eden-cn/lapzild-tss/ljhwZthlaukjlkulzlp/user-upload/1vx23mnwp9xif.mp4
- Images: https://lf3-static.bytednsdoc.com/obj/eden-cn/lapzild-tss/ljhwZthlaukjlkulzlp/user-upload/4og2ymo6oe71o.jpeg
- Project page: https://seed.bytedance.com/en/seed3d_2_0

#### Cube 4D generation — Roblox (2026-02-04)
- Type: Model · Timing: Turn-based · Access: Waitlist / early access, Product / app
- Input: Text prompt → Output: Mesh / 3D asset, Agent behaviour & actions
- Idea: Generation at play time, by participants, of objects that obey the world's rules: a concrete template for letting people inside a generated situation create things that actually work. Roblox reports 160,000+ objects generated in early access in one game.
- What it is: Beta of '4D generation' on Roblox: inside a game, a player types a prompt and receives a functional object, for example a car they can get into and drive, because Cube generates parts that match a schema and Roblox attaches behaviours to them.
- How it works: Schemas such as Car-5 (body plus four wheels) and Body-1 (any single mesh) define the named mesh parts an object needs; Cube generates those parts and scripted behaviours make them work in the experience.
- Specs: beta schemas: Car-5, Body-1 · 160K+ objects in early access
- Capability: Co-creation & agency, Behavioral plausibility, Reactivity
- Video: https://www.youtube.com/watch?v=8y9k6AsPY6w
- Images: https://cms-media.roblox.com/assets/63a0216d-5e83-1ba0-9156-5cb411951612.webp
- Project page: https://corp.roblox.com/newsroom/2026/02/accelerating-creation-powered-roblox-cube-foundation-model

#### ShapeR — Meta (2026-01-16)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code
- Input: Video, Multi-view capture / scan → Output: Mesh / 3D asset
- Idea: From 'one clean product photo' to 'walk through a real room wearing glasses': object generation that works on the messy captures people actually make in situ.
- What it is: Generates metric 3D shapes of the objects in a casually captured video, for example from Aria glasses, using SLAM points, posed views and machine-generated captions for each detected object; it comes with a benchmark of 178 in-the-wild objects across 7 real scenes.
- How it works: Visual-inertial SLAM, 3D detection and VLM captioning extract per-object conditions; a rectified-flow transformer trained with compositional augmentations and an object-to-scene curriculum generates each shape.
- Specs: benchmark: 178 objects · 7 scenes
- Capability: Situational reach, Perceptual realism
- Paper: https://arxiv.org/abs/2601.11514 (arXiv preprint)
- Video: https://www.youtube.com/watch?v=EbY30KAA55I
- Images: https://facebookresearch.github.io/ShapeR/images/panel1.png
- Project page: https://facebookresearch.github.io/ShapeR/
- Code: https://github.com/facebookresearch/ShapeR

#### TRELLIS.2 — Microsoft (2025-12)
- Type: Model · Timing: Pre-generated · Access: Open weights / code
- Input: Image → Output: Mesh / 3D asset
- Idea: Native handling of thin, open and nested surfaces such as cloth, leaves and interiors removes a common reason generated props look like closed plastic shells.
- What it is: Successor to TRELLIS: a 4-billion-parameter image-to-3D model built on O-Voxel, a sparse voxel structure that encodes arbitrary topology (open, non-manifold and fully enclosed surfaces) together with PBR material attributes.
- How it works: A Sparse Compression VAE over O-Voxels gives a compact latent space; large flow-matching transformers (4B parameters) trained on public 3D datasets generate geometry and materials.
- Specs: 4B parameters · MIT licence
- Capability: Perceptual realism, Authoring accessibility
- Paper: https://arxiv.org/abs/2512.14692 (Technical report)
- Video: https://microsoft.github.io/TRELLIS.2/assets/trellis2.mp4
- Images: https://microsoft.github.io/TRELLIS.2/assets/method/overview.jpg
- Project page: https://microsoft.github.io/TRELLIS.2/
- Code: https://github.com/microsoft/TRELLIS.2

#### SAM 3D (Objects and Body) — Meta (2025-11-19)
- Type: Model · Timing: Pre-generated · Access: Open weights / code
- Input: Image → Output: Mesh / 3D asset, Virtual human (face / body)
- Idea: Grounds asset generation in real photographs: any snapshot of a room or a person becomes a source of 3D props and bodies for rebuilding that situation.
- What it is: Meta's pair of open models that lift things in an ordinary photo into 3D: SAM 3D Objects reconstructs the geometry, texture and layout of selected objects even in clutter or under occlusion, and SAM 3D Body recovers a full-body human mesh including hands and feet, promptable with masks or keypoints.
- How it works: Objects: multi-stage training (synthetic pretraining, then real-world alignment) on data annotated with a human- and model-in-the-loop pipeline; Body: an encoder-decoder over the new Momentum Human Rig (MHR) parametric mesh.
- Specs: ≥5:1 human-preference win rate on real-world objects (Meta)
- Capability: Authoring accessibility, Perceptual realism
- Paper: https://arxiv.org/abs/2511.16624 (Technical report)
- Video: https://www.youtube.com/watch?v=B7PZuM55ayc
- Images: https://raw.githubusercontent.com/facebookresearch/sam-3d-objects/main/doc/intro.png
- Project page: https://ai.meta.com/sam3d/
- Code: https://github.com/facebookresearch/sam-3d-objects

#### Seed3D 1.0 — ByteDance Seed (2025-10-22)
- Type: Model · Timing: Pre-generated · Access: Research only
- Input: Image → Output: Mesh / 3D asset, 3D scene / world
- Idea: Frames generated assets as training environments rather than art: the test is whether an agent can interact with them in a physics simulator.
- What it is: ByteDance Seed's image-to-3D foundation model aimed at simulation: it produces assets with accurate geometry, aligned textures and PBR materials that can be dropped into physics engines for robot manipulation training, and assembled into complete scenes.
- How it works: Diffusion-transformer geometry generation followed by multi-view texture and PBR material synthesis; individual objects are assembled into scenes for simulation.
- Capability: Perceptual realism, Situational reach
- Paper: https://arxiv.org/abs/2510.19944 (Technical report)
- Video: https://lf3-static.bytednsdoc.com/obj/eden-cn/lapzild-tss/ljhwZthlaukjlkulzlp/user-upload/1vx23mh0jdhl0.mp4
- Images: https://lf3-static.bytednsdoc.com/obj/eden-cn/lapzild-tss/ljhwZthlaukjlkulzlp/user-upload/1vx23mh0jdet6.jpg
- Project page: https://seed.bytedance.com/en/seed3d

#### Rodin Gen-2 — Deemos (Hyper3D Rodin) (2025-09-24)
- Type: Model · Timing: Pre-generated · Access: Product / app, Public API
- Input: Image, Text prompt → Output: Mesh / 3D asset
- Idea: Part-aware generation turns one blob of geometry into separable pieces such as doors, wheels and limbs that can later be animated or made interactive.
- What it is: Second-generation Rodin 3D generator from Deemos (Hyper3D), which Deemos says gives four times the mesh quality of Gen-1.5 and builds models recursively from parts ('BANG to Parts'), so a generated object can be split into editable components.
- How it works: Proprietary 3D-native diffusion model continuing the CLAY line, combined with BANG (generative exploded dynamics) for part decomposition.
- Specs: 4× mesh quality vs Gen-1.5 (developer claim)
- Capability: Authoring accessibility, Experimental control
- Video: https://www.youtube.com/watch?v=1VLCf5_lCug
- Project page: https://hyper3d.ai/
- API docs: https://docs.hyper3d.ai/

#### Hunyuan3D 3.0 — Tencent Hunyuan (2025-09-16)
- Type: Model · Timing: Pre-generated · Access: Product / app, Public API
- Input: Image, Text prompt, Sketch & gesture → Output: Mesh / 3D asset
- Idea: Shows the pattern of Chinese labs releasing open weights (2.x) and then a closed flagship (3.x) sold through a cloud API and an end-to-end studio.
- What it is: Tencent's closed flagship for production assets, which Tencent says has three times the precision of earlier versions with 1536³ geometric resolution; it powers the Hunyuan 3D engine, launched globally with a Tencent Cloud API on 26 November 2025, and HY 3D Studio, which chains generation, retopology, UVs, texturing, rigging and animation.
- How it works: Proprietary; Tencent describes a 3.6-billion-voxel high-resolution geometry representation with image, multi-view and sketch conditioning, likely a scaled-up successor of the Hunyuan3D-DiT shape model.
- Specs: 1536³ geometry · 3.6B voxels (Tencent claims)
- Capability: Perceptual realism, Authoring accessibility
- Video: https://x.com/TencentHunyuan/status/1967873084960260470
- Images: https://www.tencent.com/wp-content/uploads/2025/11/f126e13e424fb6903c0891c383ecb495.jpg
- Project page: https://www.tencent.com/en-us/articles/2202235.html

#### Tripo 3.0 — Tripo AI (VAST) (2025-08-20)
- Type: Model · Timing: Pre-generated · Access: Product / app, Public API
- Input: Image, Text prompt → Output: Mesh / 3D asset
- Idea: One of the main commercial image-to-3D services alongside Meshy, Rodin and Hunyuan3D, and the one most tightly linked to open research releases from the same lab.
- What it is: VAST's third-generation Tripo model with sharper geometry and an Ultra mode, available in Tripo Studio and the Tripo API; Tripo followed it with the H3.1 HD model (May 2026) and the P2.0 character model.
- How it works: Proprietary; VAST's published research (the TripoSG rectified-flow shape model) suggests a large rectified-flow transformer over a 3D shape latent, but the 3.0 architecture is unpublished.
- Capability: Perceptual realism, Authoring accessibility
- Video: https://www.youtube.com/watch?v=uRZPf-2VmGs
- Images: https://cdn-blog.holymolly.ai/media/production/Tripo3D_og-1.webp
- Project page: https://www.tripo3d.ai/
- API docs: https://platform.tripo3d.ai/docs

#### Cube 3D — Roblox (2025-03-17)
- Type: Model · Timing: Pre-generated · Access: Open weights / code, Product / app
- Input: Text prompt → Output: Mesh / 3D asset
- Idea: Treats 3D shapes as tokens a language model can read and write, a step toward one model that generates objects, scenes, rigs and scripts for a game platform.
- What it is: The first open-source part of Roblox's Cube 3D foundation model: text-to-shape generation available in Roblox Studio and through an in-game API, so creators and their games can generate meshes from prompts.
- How it works: A 3D shape tokenizer converts meshes into discrete tokens; an autoregressive transformer generates shape tokens from text, which are decoded back into meshes, and the same tokens support shape-to-text and LLM-assisted text-to-scene.
- Capability: Authoring accessibility, Situation diversity
- Paper: https://arxiv.org/abs/2503.15475 (Technical report)
- Video: https://www.youtube.com/watch?v=85PNb99CT68
- Images: https://raw.githubusercontent.com/Roblox/cube/main/resources/teaser.png
- Project page: https://corp.roblox.com/newsroom/2025/03/introducing-roblox-cube
- Code: https://github.com/Roblox/cube

#### Hunyuan3D 2.0 — Tencent Hunyuan (2025-01-21)
- Type: Model · Timing: Pre-generated · Access: Open weights / code, Product / app
- Input: Image, Text prompt → Output: Mesh / 3D asset
- Idea: The open-weight model much of the community and many Chinese apps built on; Tencent reports more than 3 million Hugging Face downloads across its open 3D models by November 2025.
- What it is: Tencent's open-weight two-stage 3D asset system: Hunyuan3D-DiT generates the shape from an image and Hunyuan3D-Paint textures it; it shipped with a Blender add-on and a web studio, and Hunyuan3D 2.1 (June 2025) added open PBR materials.
- How it works: A flow-based diffusion transformer over a shape VAE latent generates geometry aligned to the condition image, then a multi-view diffusion texture model paints generated or hand-made meshes.
- Capability: Authoring accessibility, Perceptual realism
- Paper: https://arxiv.org/abs/2501.12202 (Technical report)
- Video: https://github.com/user-attachments/assets/a2cbc5b8-be22-49d7-b1c3-7aa2b20ba460
- Images: https://raw.githubusercontent.com/Tencent-Hunyuan/Hunyuan3D-2/main/assets/images/teaser.jpg
- Project page: https://3d.hunyuan.tencent.com/
- Code: https://github.com/Tencent-Hunyuan/Hunyuan3D-2

#### TRELLIS — Microsoft (2024-12-02)
- Type: Model · Timing: Pre-generated · Access: Open weights / code
- Input: Image, Text prompt → Output: Mesh / 3D asset, Gaussian splats / radiance field
- Idea: One latent, several output formats: the same generated object can become a game mesh or a splat for a photoreal scene, and parts can be regenerated without starting over.
- What it is: Microsoft's open-source 3D generator built on a Structured LATent (SLAT) representation that decodes to meshes, 3D Gaussians or radiance fields; it generates assets from an image or text and supports local 3D edits.
- How it works: A sparse 3D voxel grid carrying multiview DINOv2 features is encoded into structured latents and generated with rectified-flow transformers of up to 2B parameters trained on 500K assets.
- Specs: up to 2B parameters · 500K training assets · MIT licence
- Capability: Authoring accessibility, Situation diversity
- Paper: https://arxiv.org/abs/2412.01506 (CVPR 2025)
- Video: https://microsoft.github.io/TRELLIS/assets/teaser.mp4
- Images: https://microsoft.github.io/TRELLIS/assets/pipeline.png
- Project page: https://microsoft.github.io/TRELLIS/
- Code: https://github.com/microsoft/TRELLIS

#### Meshy-4 — Meshy (2024-08-22)
- Type: Model · Timing: Pre-generated · Access: Product / app, Public API
- Input: Text prompt, Image → Output: Mesh / 3D asset
- Idea: Marked the shift of commercial 3D generators from 'looks fine from a distance' to geometry detailed enough for game props.
- What it is: Fourth-generation Meshy model that remastered geometry quality for text-to-3D and image-to-3D, with cleaner hard-surface shapes and a two-step text-to-3D workflow: an untextured preview first, then texturing.
- How it works: Proprietary 3D generative model (architecture unpublished); text-to-3D is split into a fast preview mesh stage and a separate PBR texturing stage.
- Capability: Authoring accessibility, Perceptual realism
- Video: https://www.youtube.com/watch?v=AH58ABQbXd8
- Images: https://cdn.meshy.ai/landing-assets/blog/meshy-4-break-grounds/cover.png
- Project page: https://www.meshy.ai/blog/meshy-4-break-grounds
- API docs: https://docs.meshy.ai/

#### Stable Fast 3D (SF3D) — Stability AI (2024-08-01)
- Type: Model · Timing: Pre-generated · Access: Open weights / code, Public API
- Input: Image → Output: Mesh / 3D asset
- Idea: Sub-second, relightable meshes make it plausible to generate props while a session is running rather than in a pre-production step.
- What it is: Stability AI's single-image-to-mesh model that returns a UV-unwrapped, textured mesh with predicted material parameters in about 0.5 seconds, with lighting removed from the texture so the asset can be relit.
- How it works: A large reconstruction transformer trained specifically for mesh output, with fast UV unwrapping, material and normal-map prediction, and a delighting step.
- Specs: ~0.5 s per mesh
- Capability: Temporal responsiveness, Authoring accessibility
- Paper: https://arxiv.org/abs/2408.00653 (Technical report)
- Video: https://www.youtube.com/watch?v=uT96UCBSBko
- Project page: https://stability.ai/news/introducing-stable-fast-3d
- Code: https://github.com/Stability-AI/stable-fast-3d

#### Meta 3D Gen (AssetGen) — Meta (2024-07-02)
- Type: Research demo · Timing: Pre-generated · Access: Research only
- Input: Text prompt → Output: Mesh / 3D asset
- Idea: Physically based materials rather than baked colours are what let a generated asset sit convincingly under a VR scene's own lighting.
- What it is: Meta's text-to-3D pipeline that combines 3D AssetGen (text to mesh with PBR materials) and 3D TextureGen (texturing and retexturing), producing an asset in under a minute according to Meta.
- How it works: AssetGen generates multi-view images with shaded and albedo channels, reconstructs a signed distance field and PBR materials with a large reconstruction model, then refines texture in UV space.
- Specs: <1 min per asset (Meta claim)
- Capability: Perceptual realism, Authoring accessibility
- Paper: https://arxiv.org/abs/2407.02445 (Technical report)
- Video: https://www.youtube.com/watch?v=xY_2jAEcBa0
- Images: https://assetgen.github.io/static/teaser/teaser.jpg
- Project page: https://assetgen.github.io/

#### CLAY (Rodin Gen-1) — Longwen Zhang, Deemos (Hyper3D Rodin) (2024-05-30)
- Type: Research demo · Timing: Pre-generated · Access: Research only
- Input: Text prompt, Image, Multi-view capture / scan → Output: Mesh / 3D asset
- Idea: Argued for training on native 3D data instead of distilling 2D models, which became the dominant recipe (Hunyuan3D, TRELLIS, TripoSG) for production-grade assets.
- What it is: The 3D-native generative model behind Deemos's Rodin Gen-1: a latent diffusion transformer trained directly on 3D geometry that produces meshes and PBR materials from text, images or 3D controls such as voxels, bounding boxes and point clouds.
- How it works: A multi-resolution VAE over neural-field geometry plus a minimal latent Diffusion Transformer, trained progressively on a large curated 3D dataset, with a separate multi-view diffusion model for PBR materials.
- Capability: Authoring accessibility, Experimental control
- Paper: https://arxiv.org/abs/2406.13897 (ACM TOG (SIGGRAPH 2024))
- Video: https://www.youtube.com/watch?v=YcKFp4U2Voo
- Project page: https://sites.google.com/view/clay-3dlm

#### TripoSR — Tripo AI (VAST), Stability AI (2024-03-04)
- Type: Model · Timing: Pre-generated · Access: Open weights / code
- Input: Image → Output: Mesh / 3D asset
- Idea: Fast and permissive (MIT) enough to run inside other tools, it became a building block for inserting props on demand.
- What it is: Open-weight image-to-3D model released by Stability AI and Tripo AI that reconstructs a textured mesh from a single image in under half a second on an NVIDIA A100.
- How it works: LRM-style transformer that maps DINO image features to a triplane NeRF, with changes to data curation, model design and training, followed by marching-cubes mesh extraction.
- Specs: <0.5 s per object on A100 · MIT licence
- Capability: Temporal responsiveness, Authoring accessibility
- Paper: https://arxiv.org/abs/2403.02151 (Technical report)
- Video: https://www.youtube.com/watch?v=il0THDcRaDY
- Images: https://raw.githubusercontent.com/VAST-AI-Research/TripoSR/main/figures/teaser800.gif
- Project page: https://stability.ai/news/triposr-3d-generation
- Code: https://github.com/VAST-AI-Research/TripoSR

#### Genie (Luma) — Luma AI (2024-01-09)
- Type: Product / app · Timing: Pre-generated · Access: Product / app
- Input: Text prompt → Output: Mesh / 3D asset
- Idea: Made text-to-3D a consumer action measured in seconds; Luma has since moved its focus to video models and the standalone Genie page now redirects to its main site.
- What it is: Luma's text-to-3D generator: a prompt returns several candidate 3D models within seconds, and one can be refined into a higher-quality textured mesh for download, in the browser or on Discord.
- How it works: Proprietary feed-forward 3D generative model (architecture unpublished), with a fast draft stage and a separate refinement stage.
- Specs: drafts in <10 s (developer claim)
- Capability: Authoring accessibility, Situation diversity
- Video: https://www.youtube.com/watch?v=5rW98mMdP6I
- Project page: https://lumalabs.ai/genie

#### LRM: Large Reconstruction Model — Yicong Hong, Adobe (2023-11-08)
- Type: Research demo · Timing: Pre-generated · Access: Research only
- Input: Image → Output: Gaussian splats / radiance field, Mesh / 3D asset
- Idea: Replaced per-object optimization with a single feed-forward pass, moving image-to-3D from hours to seconds; TripoSR, InstantMesh and most production pipelines follow this template.
- What it is: A 500-million-parameter transformer that predicts a triplane NeRF of an object from one image in about five seconds, trained on roughly one million objects from Objaverse and MVImgNet.
- How it works: Learnable triplane tokens cross-attend to DINO image features in an image-to-triplane transformer decoder, trained end to end with rendering losses on multi-view data.
- Specs: 500M parameters · ~5 s per object · ~1M training objects
- Capability: Authoring accessibility, Temporal responsiveness
- Paper: https://arxiv.org/abs/2311.04400 (ICLR 2024)
- Video: https://www.youtube.com/watch?v=RD-UhM1kBVY
- Project page: https://research.adobe.com/publication/lrm-large-reconstruction-model-for-single-image-to-3d/

#### DreamGaussian — Jiaxiang Tang (2023-09-28)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code
- Input: Image, Text prompt → Output: Gaussian splats / radiance field, Mesh / 3D asset
- Idea: Brought Gaussian splatting into generation and cut optimization-based image/text-to-3D from hours to minutes, a step toward explicit 3D representations in asset models.
- What it is: Generates a textured mesh from one image (or a text prompt) in about two minutes by optimizing 3D Gaussians with score distillation, then extracting a mesh and refining its UV texture.
- How it works: Progressive densification of 3D Gaussians under SDS guidance (Zero-1-to-3 for images, Stable Diffusion for text), followed by mesh extraction and texture refinement in UV space.
- Specs: ~2 min per image-to-3D asset
- Capability: Authoring accessibility, Temporal responsiveness
- Paper: https://arxiv.org/abs/2309.16653 (ICLR 2024 (Oral))
- Video: https://dreamgaussian.github.io/videos/text-to-image-to-3d.mp4
- Project page: https://dreamgaussian.github.io/
- Code: https://github.com/dreamgaussian/dreamgaussian

#### Zero-1-to-3 — Ruoshi Liu (2023-03-20)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code
- Input: Image, Camera path / pose → Output: Image / panorama, Mesh / 3D asset
- Idea: Turned a 2D image model into a viewpoint-controllable object renderer, which made a single photo the default input for 3D asset generation.
- What it is: Fine-tunes Stable Diffusion to render an object from a new viewpoint given one photo and a relative camera rotation; the generated views can then be lifted into a 3D model with score distillation.
- How it works: A latent diffusion model conditioned on the input image and the relative camera pose, fine-tuned on renderings of Objaverse objects; 3D reconstruction by score distillation into a neural field.
- Capability: Authoring accessibility, Perceptual realism
- Paper: https://arxiv.org/abs/2303.11328 (ICCV 2023)
- Video: https://www.youtube.com/watch?v=H5dVW5yOfPY
- Images: https://zero123.cs.columbia.edu/assets/teaser.png
- Project page: https://zero123.cs.columbia.edu/
- Code: https://github.com/cvlab-columbia/zero123

#### DreamFusion — Ben Poole, Google (2022-09-29)
- Type: Research demo · Timing: Pre-generated · Access: Research only
- Input: Text prompt → Output: Gaussian splats / radiance field, Mesh / 3D asset
- Idea: Showed that 3D objects can be pulled out of a 2D image model with no 3D training data, the starting point of the text-to-3D lineage, at the cost of a slow optimization per object.
- What it is: Text-to-3D method from Google Research that optimizes a NeRF from scratch using a frozen 2D text-to-image diffusion model (Imagen) as its only guide; a prompt yields a relightable 3D object after a long per-object optimization.
- How it works: Score Distillation Sampling: a randomly initialised NeRF is rendered from random viewpoints and updated with gradients from Imagen's denoising loss, with shading terms that encourage real geometry.
- Specs: per-prompt NeRF optimization · Imagen 64×64 prior
- Capability: Authoring accessibility, Situation diversity
- Recognition: ICLR 2023 Outstanding Paper Award
- Paper: https://arxiv.org/abs/2209.14988 (ICLR 2023)
- Video: https://dreamfusion-cdn.ajayj.com/dreamfusion_overview.mp4
- Images: https://dreamfusion3d.github.io/assets/images/dreamfusion_samples.png
- Project page: https://dreamfusion3d.github.io/

### Characters, rigging & animation

Generated characters with skeletons, auto-rigging and animation ready for engines.

#### Tripo P2.0 — Tripo AI (VAST) (2026-09-06)
- Type: Model · Timing: Pre-generated · Access: Product / app, Public API
- Input: Image, Text prompt → Output: Mesh / 3D asset, Motion / animation
- Idea: Quad topology with sensible edge flow is what lets a generated character deform properly when it moves; P2.0 targets the gap between a statue and an actor.
- What it is: Tripo's character model that generates animation-ready characters with clean quad topology from an image or a prompt; it appeared as a preview on 6 September 2026 and was released officially on 1 October 2026.
- How it works: Proprietary; VAST has not published the architecture.
- Capability: Authoring accessibility, Perceptual realism
- Video: https://www.youtube.com/watch?v=g4ozFeSBPfo
- Project page: https://www.tripo3d.ai/
- API docs: https://platform.tripo3d.ai/docs

#### Puppeteer — Chaoyue Song, ByteDance Seed (2025-08-14)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code
- Input:  → Output: Mesh / 3D asset, Motion / animation
- Idea: Closes the step between a static generated model and an animated asset for objects of any category, not only characters with standard skeletons.
- What it is: Rigs and animates arbitrary 3D models: an autoregressive transformer predicts the skeleton, an attention network predicts skinning weights, and an optimization stage produces stable, high-fidelity animation.
- How it works: Joint-based tokenization with hierarchical ordering and stochastic perturbation for skeleton generation, topology-aware joint attention for skinning, and a differentiable optimization-based animation pipeline.
- Capability: Authoring accessibility, Perceptual realism
- Paper: https://arxiv.org/abs/2508.10898 (NeurIPS 2025 (Spotlight))
- Video: https://www.youtube.com/watch?v=DnKx803JHyI
- Images: https://chaoyuesong.github.io/Puppeteer/static/images/method/method.png
- Project page: https://chaoyuesong.github.io/Puppeteer/
- Code: https://github.com/Seed3D/Puppeteer

#### UniRig — Jia-Peng Zhang, Tripo AI (VAST) (2025-04-16)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code
- Input:  → Output: Mesh / 3D asset
- Idea: One model for every kind of creature, which matters once generators produce arbitrary characters rather than only humanoids.
- What it is: Unified auto-rigging model from Tsinghua University and VAST that generates topologically valid skeletons and skinning weights for humans, animals and other characters with very different skeleton structures.
- How it works: An autoregressive transformer with Skeleton Tree Tokenization generates the bone hierarchy and a bone-point cross-attention module predicts skinning weights; trained on Rig-XL, 14,000+ rigged models.
- Specs: Rig-XL: 14K+ rigged models
- Capability: Authoring accessibility, Situation diversity
- Paper: https://arxiv.org/abs/2504.12451 (ACM TOG (SIGGRAPH 2025))
- Video: https://zjp-shadow.github.io/works/UniRig/static/videos/teaser-720p.mp4
- Images: https://zjp-shadow.github.io/works/UniRig/static/images/result.webp
- Project page: https://zjp-shadow.github.io/works/UniRig/
- Code: https://github.com/VAST-AI-Research/UniRig

#### Make-It-Animatable — Zhiyang Guo (2024-11-27)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code
- Input:  → Output: Mesh / 3D asset, Motion / animation
- Idea: Sub-second rigging means a character generated during a session can be animated immediately.
- What it is: Makes any 3D humanoid model, mesh or Gaussian splat, animation-ready in under one second by predicting blend weights, bones and pose transformations, whatever the input pose.
- How it works: A particle-based shape autoencoder with coarse-to-fine, structure-aware prediction of skinning weights, bone positions and pose-to-rest transforms against a standard humanoid skeleton.
- Specs: <1 s per character
- Capability: Authoring accessibility, Temporal responsiveness
- Paper: https://arxiv.org/abs/2411.18197 (CVPR 2025)
- Video: https://www.youtube.com/watch?v=mH6L9r_28LA
- Images: https://jasongzy.github.io/Make-It-Animatable/static/images/teaser.jpg
- Project page: https://jasongzy.github.io/Make-It-Animatable/
- Code: https://github.com/jasongzy/Make-It-Animatable

#### Meshy auto-rigging and animation — Meshy (2024-07-04)
- Type: Product / app · Timing: Pre-generated · Access: Product / app, Public API
- Input:  → Output: Mesh / 3D asset, Motion / animation
- Idea: The commercial default for turning a prop into an actor: a generated character becomes a moving extra with one click, though from a fixed preset library rather than generated motion.
- What it is: Meshy's rigging and animation tools: an uploaded or generated humanoid or quadruped character is auto-rigged in seconds and animated with a library of more than 600 motion presets (walk cycles, idles, jumps, attacks), then exported to game engines.
- How it works: Automatic skeleton fitting and skinning for humanoid and quadruped meshes, followed by retargeting of motion-capture-style presets from Meshy's animation library.
- Specs: 600+ motion presets
- Capability: Authoring accessibility
- Video: https://www.youtube.com/watch?v=DRYu_M76qoM
- Images: https://cdn.meshy.ai/landing-assets/og-images/animation_og.webp
- Project page: https://www.meshy.ai/features/ai-animation-generator
- API docs: https://docs.meshy.ai/

#### Animate Anything — Anything World (2023-09-28)
- Type: Product / app · Timing: Pre-generated · Access: Product / app
- Input:  → Output: Mesh / 3D asset, Motion / animation
- Idea: Extends auto-rigging beyond humanoids, so the animals and machines of a scene can move as well.
- What it is: Anything World's service that automatically rigs and animates uploaded 3D models, including animals, vehicles and other non-humanoid shapes, and returns engine-ready animated assets.
- How it works: Proprietary; the system likely classifies the model's category, places a category-specific skeleton, computes skinning and applies a matching animation set.
- Capability: Authoring accessibility, Situation diversity
- Video: https://www.youtube.com/watch?v=EVKFVvIu3FQ
- Images: https://cdn.prod.website-files.com/6101e033eba551a09cbbe91c/64f342ce3a3dc9a3448a5e91_autoRigg_home_small_2.png
- Project page: https://anything.world/

#### RigNet — Zhan Xu (2020-05-01)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code
- Input:  → Output: Mesh / 3D asset
- Idea: The starting point of the 'generate a character, then make it move' lineage without a rigging artist.
- What it is: Neural network that predicts a skeleton and skinning weights for an arbitrary articulated character mesh, the first learned auto-rigging method for diverse shapes beyond humanoids.
- How it works: Graph neural networks over the mesh predict joint locations, then bone connectivity via a minimum spanning tree over learned edge probabilities, then skinning weights; trained on about 2,700 rigged characters.
- Capability: Authoring accessibility
- Paper: https://arxiv.org/abs/2005.00559 (ACM TOG (SIGGRAPH 2020))
- Video: https://www.youtube.com/watch?v=J90VETgWIDg
- Images: https://zhan-xu.github.io/rig-net/teaser.png
- Project page: https://zhan-xu.github.io/rig-net/
- Code: https://github.com/zhan-xu/RigNet

### Human motion generation

Text- and audio-to-motion models for bodies, hands and interaction.

#### ARDY — Kaifeng Zhao, NVIDIA (2026-07-09)
- Type: Research demo · Timing: Real-time streaming · Access: Open weights / code
- Input: Text prompt, Scene spec, code & rules → Output: Motion / animation
- Idea: Moves text-to-motion from offline clips to a live, steerable body, the property a generated virtual human needs when a participant changes the situation mid-scene.
- What it is: Streaming motion generator from NVIDIA and ETH Zürich that produces 3D human motion in real time while accepting new text prompts and kinematic constraints on the fly: root paths, waypoints, full-body keyframes and sparse joint targets.
- How it works: A two-stage autoregressive transformer denoiser over a hybrid representation (explicit root features plus a latent body embedding), with variable history context and long-horizon constraint conditioning, trained on a large motion-capture corpus.
- Capability: Temporal responsiveness, Experimental control, Reactivity
- Paper: https://arxiv.org/abs/2607.08741 (ACM TOG (SIGGRAPH 2026))
- Video: https://research.nvidia.com/labs/sil/projects/ardy/assets/videos/ardy_siggraph_video_cam_ready.mp4
- Images: https://raw.githubusercontent.com/nv-tlabs/ardy/main/assets/banner.png
- Project page: https://research.nvidia.com/labs/sil/projects/ardy/
- Code: https://github.com/nv-tlabs/ardy

#### HY-Motion 1.0 — Tencent Hunyuan (2025-12-30)
- Type: Model · Timing: Pre-generated · Access: Open weights / code
- Input: Text prompt → Output: Motion / animation
- Idea: Scaling reaches motion generation: much more data and a larger model give markedly better prompt following, narrowing the gap with text-to-video for bodies.
- What it is: Tencent's open-weight, billion-parameter text-to-motion model that generates 3D human motion for character animation from natural-language prompts across more than 200 motion categories, released with a Lite version and a Hugging Face demo.
- How it works: A Diffusion Transformer with flow matching, pretrained on 3,000+ hours of motion, fine-tuned on 400 hours of curated data, then aligned with reinforcement learning from human feedback and reward models.
- Specs: 1B parameters · 3,000+ h pretraining · 200+ motion categories
- Capability: Situation diversity, Experimental control
- Paper: https://arxiv.org/abs/2512.23464 (Technical report)
- Video: https://x.com/TencentHunyuan/status/2005916817987100708
- Images: https://huggingface.co/tencent/HY-Motion-1.0/resolve/main/assets/teaser.jpg
- Project page: https://hunyuan.tencent.com/motion
- Code: https://github.com/Tencent-Hunyuan/HY-Motion-1.0

#### Meta Motivo — Meta (2024-12)
- Type: Model · Timing: Real-time streaming · Access: Open weights / code
- Input: Body, face & gaze tracking, Scene spec, code & rules → Output: Motion / animation, Agent behaviour & actions
- Idea: One pretrained body controller that is prompted with goals instead of retrained per task: a candidate for virtual bodies whose behaviour an experimenter can specify on the fly.
- What it is: Meta FAIR's behavioral foundation model for a physics-simulated humanoid: without further training it can track a motion, reach a goal pose or optimize a reward specified at test time, and it comes with an interactive web demo.
- How it works: Forward-backward representations with conditional policy regularization (FB-CPR): unsupervised reinforcement learning in a shared latent space of states, motions and rewards, regularized toward unlabeled motion-capture data, on an SMPL-based humanoid in MuJoCo.
- Capability: Reactivity, Adaptation
- Paper: https://arxiv.org/abs/2504.11054 (ICLR 2025)
- Video: https://metamotivo.metademolab.com/assets/demo_1080p-ccfbbf9f.mp4
- Images: https://metamotivo.metademolab.com/bg_share.png
- Project page: https://metamotivo.metademolab.com/
- Code: https://github.com/facebookresearch/metamotivo

#### MaskedMimic — Chen Tessler, NVIDIA (2024-09-22)
- Type: Research demo · Timing: Real-time streaming · Access: Open weights / code
- Input: Text prompt, Body, face & gaze tracking → Output: Motion / animation, Agent behaviour & actions
- Idea: Physically simulated characters that react to pushes, terrain and objects, steered by whatever constraints a scenario author sets, are closer to behaving actors than kinematic animation clips.
- What it is: A single physics-based controller for simulated humanoids that fills in full-body motion from any partial description, such as sparse keyframes, VR head and hand tracking, text, or objects to interact with, and runs inside a physics simulator.
- How it works: Motion inpainting: a motion-tracking teacher policy is distilled into a conditional VAE policy that takes masked motion descriptions, trained on large motion-capture datasets in NVIDIA Isaac Gym; code is released in ProtoMotions.
- Capability: Reactivity, Experimental control, Behavioral plausibility
- Paper: https://arxiv.org/abs/2409.14393 (ACM TOG (SIGGRAPH Asia 2024))
- Video: https://www.youtube.com/watch?v=rePVn1xDWlo
- Images: https://research.nvidia.com/labs/par/projects/maskedmimic/assets/teaser.jpg
- Project page: https://research.nvidia.com/labs/par/projects/maskedmimic/
- Code: https://github.com/NVlabs/ProtoMotions

#### SayMotion — DeepMotion (2023-12-08)
- Type: Product / app · Timing: Pre-generated · Access: Product / app
- Input: Text prompt, Video → Output: Motion / animation
- Idea: An early commercial example of animators typing motions instead of capturing them, useful for quickly blocking out what generated characters do.
- What it is: DeepMotion's text-to-3D-animation tool: describe an action in words and get a 3D character animation that can be refined, looped or combined with motion captured from ordinary video, then exported to common 3D formats.
- How it works: Proprietary text-to-motion generation, likely combined with DeepMotion's markerless video motion capture (Animate 3D).
- Capability: Authoring accessibility
- Video: https://www.youtube.com/watch?v=6b2Lk3A_dzI
- Project page: https://www.deepmotion.com/saymotion

#### MoMask — Chuan Guo (2023-11-29)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code
- Input: Text prompt → Output: Motion / animation
- Idea: Discrete, masked generation gave a large jump in motion quality and remains a strong open baseline for text-driven bodies.
- What it is: Text-to-motion model that represents motion as hierarchical residual tokens and generates them with masked transformers, reaching higher fidelity on HumanML3D than diffusion baselines and supporting temporal inpainting.
- How it works: A residual VQ-VAE quantizes motion into a base layer and residual layers; a masked transformer predicts base tokens from text and a residual transformer fills the finer layers.
- Specs: HumanML3D FID 0.045 (authors)
- Capability: Perceptual realism, Experimental control
- Paper: https://arxiv.org/abs/2312.00063 (CVPR 2024)
- Video: https://www.youtube.com/watch?v=T5Wqxs37vg0
- Project page: https://ericguo5513.github.io/momask/
- Code: https://github.com/EricGuo5513/momask-codes

#### MotionGPT — Biao Jiang (2023-06-26)
- Type: Research demo · Timing: Turn-based · Access: Open weights / code
- Input: Text prompt → Output: Motion / animation, Dialogue / text
- Idea: Puts body motion into the same token stream as language, the step that lets later conversational agents speak and move from one model.
- What it is: Treats human motion as a foreign language: motion is tokenized and a language model is trained on mixed text and motion tokens, so one model can generate motion from text, caption motion, and predict or in-between motion.
- How it works: A VQ-VAE motion tokenizer plus a T5 language model pre-trained on a motion–language corpus and instruction-tuned on prompt-based motion tasks.
- Capability: Authoring accessibility, Experimental control
- Paper: https://arxiv.org/abs/2306.14795 (NeurIPS 2023)
- Video: https://www.youtube.com/watch?v=AH_q9P5dQ-c
- Project page: https://motion-gpt.github.io/
- Code: https://github.com/OpenMotionLab/MotionGPT

#### EDGE — Jonathan Tseng (2022-11-19)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code
- Input: Speech & audio → Output: Motion / animation
- Idea: Audio-driven body generation with editable constraints: music (and by extension speech or sound) drives the body while chosen poses stay pinned.
- What it is: Generates dance choreography from music with a diffusion model, with editing controls such as joint-wise constraints, in-betweening and continuation to arbitrary length.
- How it works: A transformer diffusion model conditioned on Jukebox music embeddings, with a contact-consistency loss for foot physics and a new Physical Foot Contact score; trained on AIST++.
- Capability: Perceptual realism, Experimental control
- Paper: https://arxiv.org/abs/2211.10658 (CVPR 2023)
- Video: https://edge-dance.github.io/assets/media/gallery1.mp4
- Images: https://edge-dance.github.io/assets/media/cover.png
- Project page: https://edge-dance.github.io/
- Code: https://github.com/Stanford-TML/EDGE

#### MDM: Human Motion Diffusion Model — Guy Tevet (2022-09-29)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code
- Input: Text prompt → Output: Motion / animation
- Idea: Brought diffusion to motion and made it editable: keyframes or parts of the body can be fixed while the rest is generated, a basic form of experimental control over a generated body.
- What it is: Diffusion model that generates human motion from text or action labels and supports editing such as in-betweening and body-part completion without retraining.
- How it works: A transformer-encoder diffusion model over pose sequences that predicts the clean sample instead of the noise, enabling geometric losses on foot contact and velocity; CLIP text conditioning; trained on HumanML3D and KIT-ML.
- Capability: Situation diversity, Experimental control
- Paper: https://arxiv.org/abs/2209.14916 (ICLR 2023)
- Video: https://www.youtube.com/watch?v=rVkIDj5wgjs
- Images: https://guytevet.github.io/mdm-page/static/figures/mdm_arch.png
- Project page: https://guytevet.github.io/mdm-page/
- Code: https://github.com/GuyTevet/motion-diffusion-model

#### HumanML3D — Chuan Guo (2022-06)
- Type: Dataset / benchmark · Access: Open weights / code
- Input: Text prompt → Output: Motion / animation
- Idea: Nearly every text-to-motion model since 2022 is trained and scored on it, so its coverage (everyday solo actions, little social interaction) shapes what generated bodies can do.
- What it is: Dataset of 14,616 human motion clips paired with 44,970 text descriptions (28.59 hours, drawn from AMASS and HumanAct12), released with a text-to-motion baseline; it is the standard benchmark for text-to-motion.
- How it works: Crowd-sourced text annotations of AMASS and HumanAct12 motion clips, plus a temporal VAE that predicts motion length from text and then generates the motion.
- Specs: 14,616 motions · 44,970 descriptions · 28.59 h
- Capability: Situation diversity, Experimental control
- Paper: https://openaccess.thecvf.com/content/CVPR2022/html/Guo_Generating_Diverse_and_Natural_3D_Human_Motions_From_Text_CVPR_2022_paper.html (CVPR 2022)
- Video: https://www.youtube.com/watch?v=085mBtMeZpg
- Images: https://ericguo5513.github.io/text-to-motion/model.png
- Project page: https://ericguo5513.github.io/text-to-motion/
- Code: https://github.com/EricGuo5513/HumanML3D

## Capture, Reconstruction & 4D

Turning the real world into navigable 3D and 4D (3D plus time): radiance fields and Gaussian splatting, feed-forward reconstruction in seconds, dynamic scenes, generative 4D and volumetric video.

### NeRF & Gaussian splatting

The representations that made photoreal real-time novel views possible.

#### 3DGUT — Qi Wu, NVIDIA (2024-12-17)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code
- Input: Multi-view capture / scan → Output: Gaussian splats / radiance field
- Idea: Removes the requirement that captures come from an ideal pinhole camera, which widens what real footage can become a scene.
- What it is: 3DGUT keeps the speed of splat rasterisation while supporting distorted cameras such as fisheye lenses and rolling shutters, so footage from robots, cars and headsets can be reconstructed directly.
- How it works: The unscented transform projects sigma points of each Gaussian through the exact camera model instead of linearising it, and is shared with 3DGRT for hybrid rendering.
- Capability: Situational reach, Perceptual realism
- Paper: https://arxiv.org/abs/2412.12507 (CVPR 2025)
- Video: https://research.nvidia.com/labs/toronto-ai/3DGUT/res/3DGUT_ready_compressed.mp4
- Images: https://research.nvidia.com/labs/toronto-ai/3DGUT/res/teaser.jpg
- Project page: https://research.nvidia.com/labs/toronto-ai/3DGUT/
- Code: https://github.com/nv-tlabs/3dgrut

#### 3D Gaussian Ray Tracing (3DGRT) — Nicolas Moenne-Loccoz, NVIDIA (2024-07-09)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code
- Input: Multi-view capture / scan → Output: Gaussian splats / radiance field
- Idea: Lets captured places be mixed with inserted objects and lighting effects that rasterised splats cannot show.
- What it is: NVIDIA's 3DGRT ray-traces Gaussian particles instead of rasterising them, enabling reflections, refractions, shadows and fisheye or wide-angle cameras inside captured scenes.
- How it works: Each Gaussian is wrapped in a bounding mesh inside a hardware-accelerated BVH, and hits are processed in depth order in chunks along each ray.
- Capability: Perceptual realism
- Paper: https://arxiv.org/abs/2407.07090 (SIGGRAPH Asia 2024 (ACM TOG))
- Video: https://gaussiantracer.github.io/res/3dgrt_supplementary_video.mp4
- Images: https://gaussiantracer.github.io/res/method_figure.jpg
- Project page: https://gaussiantracer.github.io/
- Code: https://github.com/nv-tlabs/3dgrut

#### Hierarchical 3D Gaussians for Very Large Datasets — Bernhard Kerbl, Inria GraphDeco (2024-06-17)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code
- Input: Multi-view capture / scan → Output: Gaussian splats / radiance field, 3D scene / world
- Idea: Shows that captured places can grow from a room to a neighbourhood without losing real-time viewing.
- What it is: A level-of-detail hierarchy of Gaussians lets city-block captures from tens of thousands of photos be rendered in real time, switching detail smoothly as you move.
- How it works: Scenes are split into chunks trained independently, merged into a tree of Gaussians, and rendered by selecting a cut through the tree per view.
- Specs: tens of thousands of photos · kilometre-scale trajectories · level of detail
- Capability: Situational reach, Persistence
- Paper: https://arxiv.org/abs/2406.12080 (SIGGRAPH 2024 (ACM TOG))
- Video: https://www.youtube.com/watch?v=p-mb2TzVJZk
- Project page: https://repo-sam.inria.fr/fungraph/hierarchical-3d-gaussians/
- Code: https://github.com/graphdeco-inria/hierarchical-3d-gaussians

#### 2D Gaussian Splatting — Binbin Huang (2024-03-26)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code
- Input: Multi-view capture / scan → Output: Gaussian splats / radiance field, Mesh / 3D asset
- Idea: Gives captured scenes geometry you can collide with, which interactive situations need.
- What it is: 2D Gaussian Splatting replaces 3D blobs with flat oriented discs, so a capture yields accurate surfaces and a clean mesh as well as photoreal views.
- How it works: Surfels with ray-splat intersection, depth distortion and normal-consistency losses are optimised per scene; meshes are extracted with TSDF fusion.
- Capability: Persistence, Experimental control
- Paper: https://arxiv.org/abs/2403.17888 (SIGGRAPH 2024)
- Video: https://www.youtube.com/watch?v=oaHCtB6yiKU
- Project page: https://surfsplatting.github.io/
- Code: https://github.com/hbb1/2d-gaussian-splatting

#### SMERF — Daniel Duckworth, Google DeepMind (2023-12-12)
- Type: Research demo · Timing: Pre-generated · Access: Research only
- Input: Multi-view capture / scan → Output: Gaussian splats / radiance field, 3D scene / world
- Idea: Shows that a large captured place can be explored in a browser tab without a dedicated GPU.
- What it is: SMERF streams house-sized radiance fields into a web browser and renders them in real time on laptops and phones, with quality close to the slow Zip-NeRF it is distilled from.
- How it works: The scene is tiled into independent MERF submodels loaded by camera position, trained by distillation from a Zip-NeRF teacher.
- Capability: Situational reach, Temporal responsiveness
- Paper: https://arxiv.org/abs/2312.07541 (SIGGRAPH 2024 (ACM TOG))
- Video: https://www.youtube.com/watch?v=zhO8iUBpnCc
- Images: https://smerf-3d.github.io/assets/img/merf/social.jpg
- Project page: https://smerf-3d.github.io/

#### Mip-Splatting — Zehao Yu (2023-11-27)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code
- Input: Multi-view capture / scan → Output: Gaussian splats / radiance field
- Idea: Matters for headsets, where people lean in and step back far more than a capture camera did.
- What it is: Mip-Splatting removes the shimmering and thin-line artefacts that appear when a Gaussian splat scene is zoomed in or out relative to how it was captured.
- How it works: A 3D smoothing filter bounds Gaussian size by the sampling rate of the training views, and a 2D Mip filter replaces screen-space dilation.
- Capability: Perceptual realism
- Recognition: CVPR 2024 Best Student Paper
- Paper: https://arxiv.org/abs/2311.16493 (CVPR 2024)
- Video: https://www.youtube.com/watch?v=D389imzYO04
- Images: https://niujinshuchong.github.io/mip-splatting/resources/teaser.png
- Project page: https://niujinshuchong.github.io/mip-splatting/
- Code: https://github.com/autonomousvision/mip-splatting

#### 3D Gaussian Splatting — Bernhard Kerbl, Inria GraphDeco (2023-08-08)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code
- Input: Multi-view capture / scan → Output: Gaussian splats / radiance field
- Idea: Made photoreal captured places fast enough for headsets, and its explicit primitives can be edited, streamed, and later animated in time.
- What it is: 3D Gaussian Splatting represents a captured scene as millions of small coloured, semi-transparent 3D Gaussians that are rasterised rather than ray-marched, giving photoreal novel views at real-time frame rates.
- How it works: Gaussians are initialised from structure-from-motion points and optimised with adaptive densification through a differentiable tile-based rasteriser.
- Specs: ≥30 fps at 1080p · per-scene training in tens of minutes (paper)
- Capability: Perceptual realism, Temporal responsiveness, Persistence
- Paper: https://arxiv.org/abs/2308.04079 (SIGGRAPH 2023 (ACM TOG))
- Video: https://www.youtube.com/watch?v=T_kXY43VZnk
- Project page: https://repo-sam.inria.fr/fungraph/3d-gaussian-splatting/
- Code: https://github.com/graphdeco-inria/gaussian-splatting

#### Instant Neural Graphics Primitives (Instant NeRF) — Thomas Müller, NVIDIA (2022)
- Type: Open-source tool · Timing: Pre-generated · Access: Open weights / code
- Input: Multi-view capture / scan → Output: Gaussian splats / radiance field
- Idea: Made capturing a radiance field feel like taking a photo rather than running a batch job.
- What it is: NVIDIA's instant-ngp trains a NeRF from a handful of photos in seconds to minutes and lets you fly through the result in an interactive viewer while it is still training.
- How it works: A multiresolution hash table of trainable feature vectors replaces most of the MLP, and fully fused CUDA kernels train and render on one GPU.
- Specs: NeRF training in seconds; 1920×1080 rendering in tens of milliseconds (paper)
- Capability: Temporal responsiveness, Authoring accessibility
- Recognition: SIGGRAPH 2022 Best Paper Award
- Paper: https://arxiv.org/abs/2201.05989 (SIGGRAPH 2022 (ACM TOG))
- Video: https://www.youtube.com/watch?v=DJ2hcC1orc4
- Images: https://nvlabs.github.io/instant-ngp/assets/twitter.jpg
- Project page: https://nvlabs.github.io/instant-ngp/
- Code: https://github.com/NVlabs/instant-ngp

#### Mip-NeRF 360 — Jonathan T. Barron, Google (2022)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code
- Input: Multi-view capture / scan → Output: Gaussian splats / radiance field
- Idea: Defined what a full walk-around capture of a real place should look like, including the far background.
- What it is: Mip-NeRF 360 extends anti-aliased NeRF to unbounded real scenes captured by walking around an object, with a nine-scene dataset that became the standard test for splatting methods.
- How it works: A non-linear scene contraction maps unbounded space into a bounded ball, an online proposal network distils density for sampling, and a distortion regulariser suppresses floaters.
- Capability: Perceptual realism, Situational reach
- Paper: https://arxiv.org/abs/2111.12077 (CVPR 2022)
- Video: https://www.youtube.com/watch?v=zBSH-k9GbV4
- Images: https://jonbarron.info/mipnerf360/img/gardenvase.jpg
- Project page: https://jonbarron.info/mipnerf360/
- Code: https://github.com/google-research/multinerf

#### NeRF — Ben Mildenhall, Matthew Tancik, Jonathan T. Barron (2020)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code
- Input: Multi-view capture / scan → Output: Gaussian splats / radiance field
- Idea: The point where a set of photos became a place you can look around in, at the cost of a day of training per scene and slow rendering.
- What it is: Neural Radiance Fields represent a scene as a small neural network that returns colour and density for any point and viewing direction, so new photoreal views of a captured object or room can be rendered from about a hundred photos.
- How it works: An MLP with positional encoding maps 5D coordinates to radiance and density, trained per scene by differentiable volume rendering against posed photos.
- Specs: ~100 posed photos · per-scene training about 1–2 days on one V100 (paper)
- Capability: Perceptual realism, Persistence
- Recognition: ECCV 2020 Best Paper Honorable Mention
- Paper: https://arxiv.org/abs/2003.08934 (ECCV 2020)
- Video: https://www.youtube.com/watch?v=JuH79E8rdKc
- Images: https://cdn.prod.website-files.com/51e0d73d83d06baa7a00000f/5e700ef6067b43821ed52768_pipeline_website-01.png
- Project page: https://www.matthewtancik.com/nerf
- Code: https://github.com/bmild/nerf

### Feed-forward reconstruction

One network pass from images to geometry or splats: DUSt3R, VGGT, AnySplat…

#### VGGT-Ω — Jianyuan Wang, Meta (2026-05-14)
- Type: Model · Timing: Pre-generated · Access: Open weights / code
- Input: Image, Video → Output: 3D scene / world, Dynamic 3D / 4D
- Idea: The authors report that reconstruction quality scales predictably with model and data size, which suggests feed-forward 3D will keep improving the way language models did.
- What it is: VGGT-Ω is the 2026 successor to VGGT: a larger feed-forward reconstructor for both static and dynamic scenes, with a text-aligned variant and a public Hugging Face demo.
- How it works: A simplified VGGT with a single multi-task dense head, registers and no high-resolution convolutions, trained at larger scale with a dynamic-scene annotation pipeline and self-supervision.
- Specs: ~1B parameters · 256–512 px checkpoints · gated weights on Hugging Face
- Capability: Temporal responsiveness, Situation diversity
- Paper: https://arxiv.org/abs/2605.15195 (CVPR 2026)
- Video: https://vggt-omega.github.io/assets/demos/transmission_video.mp4
- Project page: https://vggt-omega.github.io/
- Code: https://github.com/facebookresearch/vggt-omega

#### LingBot-Map — Robbyant (2026-04-15)
- Type: Model · Timing: Real-time streaming · Access: Open weights / code
- Input: Video → Output: 3D scene / world
- Idea: Feed-forward reconstruction that keeps up with a walking camera is what live mapping of a person's surroundings needs.
- What it is: LingBot-Map is an open streaming 3D reconstruction model from Ant Group's Robbyant that turns a live video stream into camera poses and a point cloud at about 20 frames per second.
- How it works: A geometric context transformer combines an anchor context, a pose-reference window and a trajectory memory in its attention to limit drift while keeping the streaming state compact.
- Specs: ~20 fps at 518×378 (paper)
- Capability: Temporal responsiveness, Persistence
- Paper: https://arxiv.org/abs/2604.14141 (arXiv 2026)
- Video: https://www.youtube.com/watch?v=dChg10XY4aM
- Images: https://mdn.alipayobjects.com/huamei_u94ywh/afts/img/fkaZRp3UjWwAAAAAgBAAAAgADkxfAQFr/original.png
- Project page: https://technology.robbyant.com/lingbot-map
- Code: https://github.com/Robbyant/lingbot-map

#### Depth Anything 3 — ByteDance Seed, Haotong Lin (2025-11-13)
- Type: Model · Timing: Pre-generated · Access: Open weights / code
- Input: Image, Video → Output: 3D scene / world, Gaussian splats / radiance field
- Idea: Collapses monocular depth, multi-view reconstruction and feed-forward splatting into one open model.
- What it is: Depth Anything 3 from ByteDance Seed predicts consistent depth and camera rays from one image or any number of views, and can output a 3D Gaussian scene for novel views.
- How it works: A plain DINOv2 transformer with cross-view attention predicts a depth-ray representation, trained with a teacher-student scheme on synthetic and real data; a Gaussian head is added for rendering.
- Capability: Authoring accessibility, Situation diversity
- Paper: https://arxiv.org/abs/2511.10647 (arXiv 2025)
- Video: https://depth-anything-3.github.io/assets/teaser_compress.mp4
- Images: https://depth-anything-3.github.io/assets/teaser.png
- Project page: https://depth-anything-3.github.io/
- Code: https://github.com/ByteDance-Seed/Depth-Anything-3

#### MapAnything — Nikhil Keetha, Meta (2025-09-16)
- Type: Model · Timing: Pre-generated · Access: Open weights / code
- Input: Image, Multi-view capture / scan, Camera path / pose → Output: 3D scene / world
- Idea: Metric scale and optional sensor inputs make reconstructions measurable, which matters when a captured room is used as an experimental setting.
- What it is: MapAnything is a single model from Meta and Carnegie Mellon that turns images, optionally with known intrinsics, poses or depth, into metric-scale 3D geometry and cameras.
- How it works: A multi-view transformer with a factored scene representation (per-view ray directions, depth along rays, poses and a global metric scale) is trained across many datasets and input configurations.
- Capability: Experimental control, Authoring accessibility
- Paper: https://arxiv.org/abs/2509.13414 (3DV 2026)
- Video: https://map-anything.github.io/static/MapAnything_Teaser.mp4
- Images: https://map-anything.github.io/static/MapAnything_Geometric_Inp.png
- Project page: https://map-anything.github.io/
- Code: https://github.com/facebookresearch/map-anything

#### AnySplat — Lihan Jiang (2025-05-29)
- Type: Model · Timing: Pre-generated · Access: Open weights / code
- Input: Image → Output: Gaussian splats / radiance field, 3D scene / world
- Idea: Removes the per-scene training step that made splat capture slow, so a walkthrough can become explorable almost immediately.
- What it is: AnySplat turns a set of unposed, uncalibrated photos into a complete 3D Gaussian splat scene, together with the camera poses, in a single forward pass of a few seconds.
- How it works: A geometry transformer (VGGT-style) predicts Gaussians, intrinsics and extrinsics; differentiable voxelisation merges per-pixel Gaussians, trained with rendering and distillation losses.
- Capability: Authoring accessibility, Temporal responsiveness
- Paper: https://arxiv.org/abs/2505.23716 (SIGGRAPH Asia 2025 (ACM TOG))
- Video: https://city-super.github.io/anysplat/static/videos/teaser_video.mp4
- Images: https://city-super.github.io/anysplat/static/images/teaser.png
- Project page: https://city-super.github.io/anysplat/
- Code: https://github.com/InternRobotics/AnySplat

#### VGGT — Jianyuan Wang, Meta (2025-03-14)
- Type: Model · Timing: Pre-generated · Access: Open weights / code
- Input: Image, Video → Output: 3D scene / world
- Idea: Made one network pass the default first step for turning photos or a video into a 3D scene.
- What it is: VGGT (Visual Geometry Grounded Transformer) takes one to hundreds of images and, in a single forward pass of about a second, predicts every camera, depth map, point map and point track.
- How it works: A 1.2B-parameter transformer alternates frame-wise and global attention over DINO patch tokens and decodes camera, depth, point and tracking heads, trained on many 3D datasets.
- Specs: 1.2B parameters · up to hundreds of views · under 1 s per scene (paper)
- Capability: Temporal responsiveness, Authoring accessibility
- Recognition: CVPR 2025 Best Paper Award
- Paper: https://arxiv.org/abs/2503.11651 (CVPR 2025)
- Video: https://vgg-t.github.io/resources/teaser_video_v3_compressed_short.mp4
- Images: https://vgg-t.github.io/resources/architecture_v4.png
- Project page: https://vgg-t.github.io/
- Code: https://github.com/facebookresearch/vggt

#### CUT3R — Qianqian Wang (2025-01-21)
- Type: Model · Timing: Real-time streaming · Access: Open weights / code
- Input: Video, Image → Output: 3D scene / world, Dynamic 3D / 4D
- Idea: A state that accumulates the world as you move is closer to how a headset should perceive a room than batch reconstruction.
- What it is: CUT3R reconstructs a scene online from a stream of images, updating a persistent internal state with each new frame and outputting camera pose and a metric point map per frame, including for moving content.
- How it works: A recurrent transformer reads each image against a learned state token set, writes back to it, and can also query the state from unseen viewpoints.
- Capability: Persistence, Temporal responsiveness
- Paper: https://arxiv.org/abs/2501.12387 (CVPR 2025)
- Video: https://cut3r.github.io/static/videos/cut3r_factory.mp4
- Project page: https://cut3r.github.io/
- Code: https://github.com/CUT3R/CUT3R

#### MASt3R — Vincent Leroy, NAVER LABS Europe (2024-06-14)
- Type: Model · Timing: Pre-generated · Access: Open weights / code
- Input: Image → Output: 3D scene / world
- Idea: Turned pointmap models into the front end of SLAM and structure-from-motion systems.
- What it is: MASt3R adds dense feature matching and metric scale to DUSt3R, so image pairs yield reliable correspondences for mapping, localisation and large reconstructions.
- How it works: A second head predicts local descriptors trained with a matching loss, and a fast reciprocal matcher finds correspondences on top of metric pointmaps.
- Capability: Authoring accessibility, Experimental control
- Paper: https://arxiv.org/abs/2406.09756 (ECCV 2024)
- Video: https://www.youtube.com/watch?v=AWu5z2O9H3s
- Images: https://github.com/naver/mast3r/raw/main/assets/mast3r.jpg
- Project page: https://europe.naverlabs.com/blog/mast3r-matching-and-stereo-3d-reconstruction/
- Code: https://github.com/naver/mast3r

#### DUSt3R — Shuzhe Wang, NAVER LABS Europe (2023-12-21)
- Type: Model · Timing: Pre-generated · Access: Open weights / code
- Input: Image → Output: 3D scene / world
- Idea: Started the move from fragile photogrammetry to models that reconstruct from whatever photos you have.
- What it is: DUSt3R takes two photos with unknown cameras and directly regresses a 3D point for every pixel, so depth, camera poses and a point cloud fall out of one network instead of a structure-from-motion pipeline.
- How it works: A ViT encoder-decoder pretrained with cross-view completion outputs pointmaps for both images in the first camera's frame; a global alignment step merges many views.
- Capability: Authoring accessibility, Temporal responsiveness
- Paper: https://arxiv.org/abs/2312.14132 (CVPR 2024)
- Video: https://www.youtube.com/watch?v=kI7wCEAFFb0
- Images: https://github.com/naver/dust3r/raw/main/assets/dust3r.jpg
- Project page: https://europe.naverlabs.com/research/publications/dust3r-geometric-3d-vision-made-easy/
- Code: https://github.com/naver/dust3r

#### pixelSplat — David Charatan (2023-12-19)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code
- Input: Image → Output: Gaussian splats / radiance field
- Idea: An early sign that splat scenes could come out of a network instead of a training run.
- What it is: pixelSplat predicts a 3D Gaussian scene from just two photos in one network pass, with no per-scene optimisation, and renders new views between them.
- How it works: An epipolar transformer encodes the image pair, and per-pixel depth distributions are sampled differentiably to place Gaussians.
- Capability: Temporal responsiveness, Authoring accessibility
- Paper: https://arxiv.org/abs/2312.12337 (CVPR 2024)
- Video: https://davidcharatan.com/pixelsplat/static/videos/teaser.mp4
- Images: https://pixelsplat.github.io/static/images/banner.png
- Project page: https://davidcharatan.com/pixelsplat/
- Code: https://github.com/dcharatan/pixelsplat

### Dynamic 4D scenes

Moving scenes reconstructed in space and time: 4D Gaussians, spacetime splats, 4D video.

#### FreeTimeGS — Yifan Wang, ZJU3DV (2025-06-05)
- Type: Research demo · Timing: Pre-generated · Access: Research only
- Input: Multi-view capture / scan, Video → Output: Dynamic 3D / 4D, Gaussian splats / radiance field
- Idea: The published method behind 4DV.ai's 4D video, linking a CVPR paper directly to a production medium.
- What it is: FreeTimeGS lets Gaussians appear at any time and place and carry their own motion, reconstructing fast, complex movement from multi-camera rigs for real-time free-viewpoint playback.
- How it works: Each Gaussian has a temporal centre, velocity-based motion function and temporal opacity, with a 4D regularisation that avoids overfitting to individual frames.
- Capability: Perceptual realism, Temporal responsiveness
- Paper: https://arxiv.org/abs/2506.05348 (CVPR 2025)
- Video: https://zju3dv.github.io/freetimegs/demo/demo_f1.mp4
- Images: https://zju3dv.github.io/freetimegs/img/teaser.jpg
- Project page: https://zju3dv.github.io/freetimegs/

#### Stereo4D — Linyi Jin, Google DeepMind (2024-12-12)
- Type: Dataset / benchmark · Timing: Pre-generated · Access: Open weights / code
- Input: Video → Output: Dynamic 3D / 4D
- Idea: Real 3D motion at scale is the missing training signal for 4D generators that should move things plausibly.
- What it is: Stereo4D mines stereoscopic VR180 videos from the internet to produce a large dataset of real-world scenes with dense 3D point tracks of how things actually move.
- How it works: Stereo depth, camera poses and 2D tracks are fused and filtered into world-space 3D trajectories; a DUSt3R variant (DynaDUSt3R) is trained on them to predict motion.
- Capability: Situation diversity, Behavioral plausibility
- Paper: https://arxiv.org/abs/2412.09621 (CVPR 2025)
- Video: https://stereo4d.github.io/static/videos/pipeline/vr180s-v2_compressed.mp4
- Images: https://stereo4d.github.io/stereo4d_teaser.jpg
- Project page: https://stereo4d.github.io/

#### MegaSaM — Zhengqi Li, Google DeepMind (2024-12-05)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code
- Input: Video → Output: Dynamic 3D / 4D, 3D scene / world
- Idea: A dependable camera and depth estimate is the first thing any 4D capture or video-to-world pipeline needs.
- What it is: MegaSaM estimates accurate camera paths and consistent depth from casual, dynamic videos, including handheld footage with little camera motion, where classic SLAM and structure-from-motion fail.
- How it works: A differentiable SLAM system in the style of DROID-SLAM is combined with monocular depth priors and uncertainty-aware optimisation, then refined into consistent video depth.
- Capability: Situational reach, Experimental control
- Recognition: CVPR 2025 Best Paper Honorable Mention
- Paper: https://arxiv.org/abs/2412.04463 (CVPR 2025)
- Video: https://www.youtube.com/watch?v=swigYTCdoiw
- Project page: https://mega-sam.github.io/
- Code: https://github.com/mega-sam/mega-sam

#### BTimer — Hanxue Liang, NVIDIA (2024-12-04)
- Type: Research demo · Timing: Pre-generated · Access: Research only
- Input: Video → Output: Dynamic 3D / 4D, Gaussian splats / radiance field
- Idea: Brings the feed-forward speed of VGGT-style models to moving scenes, and applies directly to generated video.
- What it is: NVIDIA's BTimer reconstructs a full 3D Gaussian snapshot of any moment in a monocular video in a single forward pass, giving a bullet-time view of moving scenes, including clips from video generators.
- How it works: A transformer takes the context frames plus a target timestamp and outputs pixel-aligned Gaussians for that instant, trained on static and dynamic data with a curriculum.
- Capability: Temporal responsiveness, Authoring accessibility
- Paper: https://arxiv.org/abs/2412.03526 (arXiv 2024)
- Video: https://research.nvidia.com/labs/toronto-ai/bullet-timer/davis_results/tennis_demo.mp4
- Images: https://research.nvidia.com/labs/toronto-ai/bullet-timer/figures/teaser.png
- Project page: https://research.nvidia.com/labs/toronto-ai/bullet-timer/

#### MonST3R — Junyi Zhang (2024-10-04)
- Type: Model · Timing: Pre-generated · Access: Open weights / code
- Input: Video → Output: Dynamic 3D / 4D, 3D scene / world
- Idea: Showed that feed-forward geometry need not assume a frozen world.
- What it is: MonST3R extends DUSt3R-style pointmaps to videos with motion, estimating per-frame geometry, camera trajectory and moving-object masks directly from a monocular clip.
- How it works: DUSt3R is fine-tuned on a small mix of synthetic dynamic datasets to predict per-timestep pointmaps, followed by a light global optimisation over windows.
- Capability: Temporal responsiveness, Situational reach
- Paper: https://arxiv.org/abs/2410.03825 (ICLR 2025)
- Video: https://monst3r-project.github.io/files/teaser_vid_v2_lowres.mp4
- Images: https://monst3r-project.github.io/files/teaser_monst3r.png
- Project page: https://monst3r-project.github.io/
- Code: https://github.com/Junyi42/monst3r

#### Shape of Motion — Qianqian Wang (2024-07-18)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code
- Input: Video → Output: Dynamic 3D / 4D, Gaussian splats / radiance field
- Idea: Moves 4D capture from camera rigs to footage anyone already has, with honest limits on unseen regions.
- What it is: Shape of Motion reconstructs a single casual phone video of a moving scene into 4D Gaussians with full-length 3D trajectories, so the event can be replayed from new angles.
- How it works: Scene motion is a small set of shared SE(3) motion bases, fitted with monocular depth and 2D track priors from foundation models.
- Capability: Situational reach, Persistence
- Paper: https://arxiv.org/abs/2407.13764 (ICCV 2025)
- Video: https://shape-of-motion.github.io/static/videos/swing.mp4
- Images: https://shape-of-motion.github.io/static/images/open_graph.png
- Project page: https://shape-of-motion.github.io/
- Code: https://github.com/vye16/shape-of-motion

#### Spacetime Gaussians — Zhan Li (2023-12-28)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code
- Input: Multi-view capture / scan, Video → Output: Dynamic 3D / 4D, Gaussian splats / radiance field
- Idea: Gaussians that appear and disappear over time handle flames, smoke and occlusion better than deforming one fixed set.
- What it is: Spacetime Gaussian Feature Splatting gives each Gaussian its own lifespan, motion and rotation curves, playing back multi-view recordings at very high resolution in real time.
- How it works: Temporal opacity, polynomial motion and rotation per Gaussian are combined with neural splatted features decoded by a small MLP, with guided sampling of new Gaussians in poorly covered regions.
- Specs: 8K at 60 fps on RTX 4090, lite model (paper)
- Capability: Perceptual realism, Temporal responsiveness
- Paper: https://arxiv.org/abs/2312.16812 (CVPR 2024)
- Video: https://www.youtube.com/watch?v=_7deTUDRlns
- Images: https://oppo-us-research.github.io/SpacetimeGaussians-website/static/images/methodv2.png
- Project page: https://oppo-us-research.github.io/SpacetimeGaussians-website/
- Code: https://github.com/oppo-us-research/SpacetimeGaussians

#### 4D Gaussian Splatting (4DGS) — Guanjun Wu (2023-10-12)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code
- Input: Video, Multi-view capture / scan → Output: Dynamic 3D / 4D, Gaussian splats / radiance field
- Idea: The reference point for treating recorded events, not just places, as something a viewer can walk around.
- What it is: 4D Gaussian Splatting represents a moving scene as one set of 3D Gaussians plus a learned deformation field, so recorded dynamic scenes play back from free viewpoints in real time.
- How it works: A HexPlane spatio-temporal encoder feeds a small MLP that predicts per-Gaussian position, rotation and scale offsets at each timestamp.
- Specs: 82 fps at 800×800 on RTX 3090 (paper, synthetic scenes)
- Capability: Perceptual realism, Temporal responsiveness
- Paper: https://arxiv.org/abs/2310.08528 (CVPR 2024)
- Video: https://www.youtube.com/watch?v=_wRbq8KnaVg
- Images: https://guanjunwu.github.io/4dgs/static/images/pipeline_00.jpg
- Project page: https://guanjunwu.github.io/4dgs/
- Code: https://github.com/hustvl/4DGaussians

#### Dynamic 3D Gaussians — Jonathon Luiten (2023-08-18)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code
- Input: Multi-view capture / scan, Video → Output: Dynamic 3D / 4D, Gaussian splats / radiance field
- Idea: Tracking comes for free with the reconstruction, so captured motion can drive or be compared with other content.
- What it is: Dynamic 3D Gaussians reconstructs multi-camera recordings of people juggling or playing sports as Gaussians that move over time, so every point is tracked through the sequence as it is rendered from new views.
- How it works: Gaussians keep fixed colour, size and opacity and only move and rotate per timestep, regularised by local rigidity, rotation-similarity and isometry losses.
- Specs: 27-camera studio captures · dense 6-DoF tracking
- Capability: Persistence, Experimental control
- Paper: https://arxiv.org/abs/2308.09713 (3DV 2024)
- Video: https://dynamic3dgaussians.github.io/vid_assets/0/juggle.mp4
- Project page: https://dynamic3dgaussians.github.io/
- Code: https://github.com/JonathonLuiten/Dynamic3DGaussians

#### Neural 3D Video Synthesis (DyNeRF) — Tianye Li, Meta (2021)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code
- Input: Multi-view capture / scan, Video → Output: Dynamic 3D / 4D
- Idea: Its multi-view kitchen recordings became the shared yardstick for every later 4D Gaussian method.
- What it is: Meta Reality Labs' DyNeRF reconstructs short multi-camera recordings of people cooking, with flames and moving hands, as a radiance field you can replay from new viewpoints and at new moments.
- How it works: A NeRF conditioned on a compact learned latent code per frame is trained with hierarchical keyframe sampling and ray importance sampling over about 20 synchronised cameras.
- Capability: Perceptual realism, Experimental control
- Paper: https://arxiv.org/abs/2103.02597 (CVPR 2022)
- Video: https://neural-3d-video.github.io/resources/video.mp4
- Project page: https://neural-3d-video.github.io/
- Code: https://github.com/facebookresearch/Neural_3D_Video

### Generative 4D

Dynamic 3D content generated or completed with video priors: DreamGaussian4D, CAT4D, BulletGen, SV4D…

#### 4DNeX — Zhaoxi Chen (2025-08-18)
- Type: Model · Timing: Pre-generated · Access: Open weights / code
- Input: Image → Output: Dynamic 3D / 4D, Flat video
- Idea: Image-to-4D without per-scene optimisation, built by repurposing an open video model.
- What it is: 4DNeX generates a dynamic 3D point-cloud scene from a single image in one feed-forward pass, so a still photo becomes a short moving scene that can be viewed from new angles.
- How it works: A pretrained video diffusion model is fine-tuned to jointly output RGB and XYZ point-map sequences, trained on a large curated 4D dataset (4DNeX-10M).
- Capability: Authoring accessibility, Situation diversity
- Paper: https://arxiv.org/abs/2508.13154 (arXiv 2025)
- Video: https://www.youtube.com/watch?v=jaXNU1-0zgk
- Project page: https://4dnex.github.io/
- Code: https://github.com/3DTopia/4DNeX

#### BulletGen — Denis Rozumny, Jonathon Luiten, Meta (2025-06-23)
- Type: Research demo · Timing: Pre-generated · Access: Research only
- Input: Video → Output: Dynamic 3D / 4D, Gaussian splats / radiance field
- Idea: Generation used as a repair tool inside reconstruction, keeping the captured motion while filling the gaps.
- What it is: Meta's BulletGen improves 4D Gaussian reconstructions of casual monocular videos by generating, at frozen bullet-time moments, the views the camera never saw and using them to supervise the reconstruction.
- How it works: A diffusion video model is aligned with the current 4D Gaussian scene at a single frozen time step; generated frames are added as supervision in an iterative optimisation that also improves 2D/3D tracking.
- Capability: Situational reach, Perceptual realism
- Paper: https://arxiv.org/abs/2506.18601 (CVPR 2026 Workshop (4D World Models))
- Images: https://arxiv.org/html/2506.18601v2/imgs/teaser/skating/v1_our.png https://arxiv.org/html/2506.18601v2/x1.png
- Project page: https://arxiv.org/abs/2506.18601

#### SV4D 2.0 — Stability AI (2025-03-20)
- Type: Model · Timing: Pre-generated · Access: Open weights / code
- Input: Video → Output: Dynamic 3D / 4D, Flat video
- Idea: Shows the open-weight object-4D line maturing toward usable animated assets.
- What it is: SV4D 2.0 improves Stability AI's video-to-4D model with sharper, more consistent multi-view videos that hold up better under large motion and can be optimised into 4D assets.
- How it works: Blended 3D and frame attention without reference multi-views, more and cleaner animated training data and progressive 3D-to-4D training improve consistency; outputs are refined in a two-stage 4D optimisation.
- Capability: Perceptual realism, Persistence
- Paper: https://arxiv.org/abs/2503.16396 (arXiv 2025)
- Video: https://www.youtube.com/watch?v=dtqj-s50ynU
- Project page: https://sv4d20.github.io/
- Code: https://github.com/Stability-AI/generative-models

#### CAT4D — Rundi Wu, Google DeepMind (2024-11-27)
- Type: Research demo · Timing: Pre-generated · Access: Research only
- Input: Video → Output: Dynamic 3D / 4D, Gaussian splats / radiance field
- Idea: Generation fills what one camera could not see, which is how a casual clip can become a navigable moment.
- What it is: Google DeepMind's CAT4D turns a single monocular video of a dynamic scene into a 4D Gaussian scene by first generating the missing camera viewpoints with a multi-view video diffusion model.
- How it works: A multi-view video diffusion model, trained on mixed static, dynamic and synthetic data, samples novel views at chosen times; an alternating sampling strategy keeps them consistent before 4D Gaussian fitting.
- Capability: Situational reach, Persistence
- Paper: https://arxiv.org/abs/2411.18613 (CVPR 2025)
- Video: https://cat-4d.github.io/videos/howitworks_cat4d.mp4
- Images: https://cat-4d.github.io/img/rep_img.jpg
- Project page: https://cat-4d.github.io/

#### Stable Video 4D (SV4D) — Stability AI (2024-07-24)
- Type: Model · Timing: Pre-generated · Access: Open weights / code
- Input: Video → Output: Dynamic 3D / 4D, Flat video
- Idea: An open-weight multi-view video model that labs can run and pin for object-level 4D content.
- What it is: Stability AI's SV4D takes a video of an object and generates consistent novel-view videos around it, which are then used to fit a dynamic 3D representation.
- How it works: Stable Video Diffusion is extended with view and frame attention to denoise a grid of views × frames jointly; outputs supervise a dynamic NeRF.
- Capability: Authoring accessibility, Situation diversity
- Paper: https://arxiv.org/abs/2407.17470 (arXiv 2024)
- Video: https://www.youtube.com/watch?v=RBP8vdAWTgk
- Project page: https://sv4d.github.io/
- Code: https://github.com/Stability-AI/generative-models

#### L4GM — Jiawei Ren, NVIDIA (2024-06-14)
- Type: Model · Timing: Pre-generated · Access: Open weights / code
- Input: Video → Output: Dynamic 3D / 4D, Gaussian splats / radiance field
- Idea: Shows 4D object generation as a forward pass, fast enough to sit inside an interactive tool.
- What it is: NVIDIA's L4GM (Large 4D Gaussian Reconstruction Model) turns a single-view video of an object into an animated 3D Gaussian object in about a second.
- How it works: A multi-view LGM backbone is extended with temporal self-attention and trained on renders of animated Objaverse objects, with an interpolation model to raise frame rate.
- Specs: about 1 s per video (paper)
- Capability: Temporal responsiveness, Authoring accessibility
- Paper: https://arxiv.org/abs/2406.10324 (NeurIPS 2024)
- Video: https://research.nvidia.com/labs/toronto-ai/l4gm/assets/4d_scenes/regular_assets/w_interp_000000.mp4
- Images: https://research.nvidia.com/labs/toronto-ai/l4gm/assets/figures/framework_largertext.png
- Project page: https://research.nvidia.com/labs/toronto-ai/l4gm/
- Code: https://github.com/nv-tlabs/L4GM-official

#### 4Real — Heng Yu, Snap Inc. (2024-06-11)
- Type: Research demo · Timing: Pre-generated · Access: Research only
- Input: Text prompt → Output: Dynamic 3D / 4D, Gaussian splats / radiance field
- Idea: Moved text-to-4D from objects on a white background to whole scenes.
- What it is: 4Real, from Snap Research and CMU, generates photorealistic dynamic scenes with backgrounds from a text prompt, viewable from a range of angles, rather than isolated cartoon-like objects.
- How it works: A text-to-video model generates a reference video and a freeze-time orbit video; a canonical 3D Gaussian scene is built from the orbit and deformed to match the reference with score distillation.
- Capability: Perceptual realism, Situation diversity
- Paper: https://arxiv.org/abs/2406.07472 (NeurIPS 2024)
- Video: https://snap-research.github.io/4Real/resources/teaser-1080p.mp4
- Images: https://snap-research.github.io/4Real/resources/racoon_sync.gif
- Project page: https://snap-research.github.io/4Real/

#### DreamGaussian4D — Jiawei Ren (2023-12-28)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code
- Input: Image, Video → Output: Dynamic 3D / 4D, Gaussian splats / radiance field, Mesh / 3D asset
- Idea: Brought 4D object generation down to minutes and to a format game engines can load.
- What it is: DreamGaussian4D animates a 3D Gaussian object generated from a single image, driven by a reference video, and exports it as an animated mesh, in minutes rather than hours.
- How it works: A static Gaussian object from DreamGaussianHD is deformed by a HexPlane deformation network fitted to an image-to-video driving clip, then refined by video-to-video texture optimisation.
- Capability: Authoring accessibility, Temporal responsiveness
- Paper: https://arxiv.org/abs/2312.17142 (arXiv 2023)
- Video: https://jiawei-ren.github.io/projects/dreamgaussian4d/videos/teaser.mp4
- Project page: https://jiawei-ren.github.io/projects/dreamgaussian4d/
- Code: https://github.com/jiawei-ren/dreamgaussian4d

#### MAV3D (Make-A-Video3D) — Uriel Singer, Meta (2023-01-26)
- Type: Research demo · Timing: Pre-generated · Access: Research only
- Input: Text prompt, Image → Output: Dynamic 3D / 4D
- Idea: The first text-to-4D system; it set the template of borrowing motion from video models.
- What it is: Meta's MAV3D generated short dynamic 3D scenes, such as an animated corgi viewable from any angle, from a text prompt alone, by distilling a text-to-video model.
- How it works: A HexPlane dynamic NeRF is optimised with score distillation from Make-A-Video, using a static-to-dynamic schedule and super-resolution fine-tuning.
- Capability: Authoring accessibility, Situation diversity
- Paper: https://arxiv.org/abs/2301.11280 (ICML 2023)
- Video: https://make-a-video3d.github.io/assets/rotating_grid.mp4
- Images: https://make-a-video3d.github.io/assets/images/teaser.png
- Project page: https://make-a-video3d.github.io/

### Volumetric video & telepresence

People captured in 3D and streamed or replayed: Beam, volumetric studios, Gaussian video.

#### Gracia — Gracia (2025)
- Type: Product / app · Timing: Pre-generated · Access: Product / app
- Input: Multi-view capture / scan, Video → Output: Dynamic 3D / 4D, Gaussian splats / radiance field
- Idea: One of the first services to put streamed Gaussian video into consumer headsets (first 4DGS streaming in March 2026 and a free Apple Vision Pro app in June 2026, as reported by Radiancefields.com), so it shows where file size and bandwidth limit what can be shown.
- What it is: Gracia captures performers and scenes as 4D Gaussian splat video and streams it to apps on Quest, Pico, Apple Vision Pro, desktop and the browser, where viewers can walk around the recorded moment.
- How it works: Multi-camera captures are reconstructed into per-frame splat sequences and encoded as keyframes plus motion deltas for streaming (as described by Radiancefields.com); Unity and Unreal plug-ins and WebGPU playback are offered.
- Capability: Perceptual realism, Situational reach
- Video: https://www.youtube.com/watch?v=m3ti-mJu0tI
- Images: https://gracia.ai/images/open-graph/hub.jpg
- Project page: https://gracia.ai/

#### VoluMe — Martin de La Gorce, Microsoft (2025-07-28)
- Type: Research demo · Timing: Real-time streaming · Access: Research only
- Input: Video → Output: Virtual human (face / body), Gaussian splats / radiance field
- Idea: 3D video calls without camera rigs, but with the trade-off that unseen sides are predicted rather than captured.
- What it is: Microsoft Research's VoluMe turns an ordinary single webcam feed into a live 3D Gaussian reconstruction of the person, so a regular video call can be viewed in 3D from slightly different angles.
- How it works: A network predicts per-frame 3D Gaussians conditioned on the input frame, trained so the reconstruction matches the input view exactly and stays temporally stable.
- Capability: Temporal responsiveness, Perceptual realism
- Paper: https://arxiv.org/abs/2507.21311 (ICCV 2025)
- Video: https://www.youtube.com/watch?v=xgh46cf4_fw
- Images: https://www.microsoft.com/en-us/research/wp-content/uploads/2025/07/volume_banner.jpg
- Project page: https://www.microsoft.com/en-us/research/publication/volume/

#### 4DV.ai 4D Gaussian Video — 4DV.ai (2025-06)
- Type: Platform / API · Timing: Pre-generated · Access: Waitlist / early access
- Input: Multi-view capture / scan, Video → Output: Dynamic 3D / 4D, Gaussian splats / radiance field
- Idea: Treats 4D video as a medium of its own: recorded events become places a viewer can stand inside, but only at capture stages for now.
- What it is: 4DV.ai records scenes with multi-camera rigs and turns them into 4D Gaussian splat video that plays in a web, Quest or Vision Pro viewer, where you can pause, orbit and move through the action; it showed the work live at SIGGRAPH 2025 Real-Time Live and in an 11.5-minute all-4DGS film with Dell and Radiancefields.com at SIGGRAPH 2026.
- How it works: Built on the FreeTimeGS line of research: Gaussians are tracked continuously through time rather than rebuilt per frame, which the company says reduces flicker and tolerates unsynchronised cameras.
- Specs: 70-camera 4K PTZ rig shown at NAB 2026 with OBSBOT · 30–60 Mbps finished stream (reported)
- Capability: Perceptual realism, Situational reach
- Recognition: SIGGRAPH 2025 Real-Time Live! Best in Show (as reported by Radiancefields.com); Venice Immersive 2026: three 4DGS projects (per 4DV.ai)
- Paper: https://arxiv.org/abs/2506.05348 (CVPR 2025)
- Video: https://www.youtube.com/watch?v=M01_By5h8lQ
- Images: https://framerusercontent.com/images/1JJc7VhziLkne1hdBiux2vfYo.webp
- Project page: https://www.4dv.ai/viewer/rocket?nowheel

#### Google Beam — Google (2025-05-20)
- Type: Product / app · Timing: Real-time streaming · Access: Product / app
- Input: Multi-view capture / scan, Speech & audio, Body, face & gaze tracking → Output: Virtual human (face / body), Dynamic 3D / 4D
- Idea: Volumetric telepresence is now a product you can buy, but at about $25,000 per unit (reported) and for one-to-one calls only.
- What it is: Google Beam is the commercial successor to Project Starline: an AI model turns several 2D camera streams into a 3D rendering of the remote person on a light-field display, sold built into HP's Dimension screen.
- How it works: Google reports a six-camera array and an AI volumetric video model that renders on a 3D light-field display with millimetre head tracking at 60 fps.
- Specs: 6 cameras · 60 fps · 65-inch light-field display (HP Dimension) · 1:1 calls · ~$25,000 per unit (reported)
- Capability: Perceptual realism, Temporal responsiveness
- Video: https://www.youtube.com/watch?v=NGPyOHKWLFQ
- Images: https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Google_Beam_hero.width-1300.png
- Project page: https://blog.google/innovation-and-ai/technology/research/google-beam-expansion/
- API docs: https://beam.google/

#### Temporal Gaussian Hierarchy (Long Volumetric Video) — Zhen Xu, ZJU3DV (2024-12)
- Type: Research demo · Timing: Pre-generated · Access: Research only
- Input: Multi-view capture / scan, Video → Output: Dynamic 3D / 4D, Gaussian splats / radiance field
- Idea: Length is what separates a clip from a scene someone can spend time in; this work removed the seconds-long limit of earlier 4D Gaussians.
- What it is: This ZJU method stores minutes-long multi-camera recordings of people as one hierarchy of Gaussians shared across time segments, so long volumetric video can be played back in real time without running out of GPU memory.
- How it works: A temporal tree assigns each Gaussian to the segment span where it is needed, so static regions are shared across long spans while dynamic regions get short-lived Gaussians; appearance uses a lightweight Gaussian-based model.
- Capability: Persistence, Perceptual realism
- Paper: https://arxiv.org/abs/2412.09608 (SIGGRAPH Asia 2024 (ACM TOG))
- Video: https://www.youtube.com/watch?v=y7e0YRNNmXw
- Images: https://zju3dv.github.io/longvolcap/img/teaser.jpg
- Project page: https://zju3dv.github.io/longvolcap/

#### Project Starline — Google (2021-05-18)
- Type: Research demo · Timing: Real-time streaming · Access: Research only
- Input: Multi-view capture / scan, Speech & audio, Body, face & gaze tracking → Output: Virtual human (face / body), Dynamic 3D / 4D
- Idea: Eye contact and depth cues at life size, tested with users, make it a reference for what remote social presence can feel like.
- What it is: Google's Project Starline prototype is a booth in which two people talk across a light-field display that shows each other life-size and in 3D, captured and transmitted in real time.
- How it works: Several colour and depth cameras feed a real-time fusion and compression pipeline; a head-tracked autostereoscopic display renders the remote person with spatial audio.
- Capability: Perceptual realism, Temporal responsiveness
- Paper: https://doi.org/10.1145/3478513.3480490 (SIGGRAPH Asia 2021 (ACM TOG))
- Video: https://www.youtube.com/watch?v=Q13CishCKXY
- Images: https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Blog_HERO.width-1300.png
- Project page: https://blog.google/technology/research/project-starline/

#### HoloSuite (HoloEdit / HoloStream) — Arcturus (2020)
- Type: Product / app · Timing: Pre-generated · Access: Product / app
- Input: Multi-view capture / scan, Video → Output: Dynamic 3D / 4D, Virtual human (face / body)
- Idea: The editing and delivery layer volumetric capture needs before it can be dropped into an experience.
- What it is: Arcturus HoloSuite is a production toolset for editing, compressing and streaming volumetric video of people into games, AR and web players; the company has since moved into Gaussian-splat replays of live sports.
- How it works: Captured mesh sequences are cleaned, re-timed, retargeted (e.g. head gaze) and encoded into adaptive streams with plug-ins for Unity and Unreal.
- Capability: Authoring accessibility, Experimental control
- Video: https://www.youtube.com/watch?v=T0CjAilUtbM
- Project page: https://arcturus.studio/

#### High-Quality Streamable Free-Viewpoint Video — Alvaro Collet, Microsoft (2015)
- Type: Research demo · Timing: Pre-generated · Access: Research only
- Input: Multi-view capture / scan → Output: Dynamic 3D / 4D, Virtual human (face / body)
- Idea: The studio volumetric-video pipeline that preceded Gaussian video, and the baseline it is judged against.
- What it is: Microsoft's capture-stage system records performers with a dome of synchronised cameras and turns them into streamable textured 3D meshes that can be placed in AR, VR or film.
- How it works: Multi-view RGB and infrared stereo give point clouds that are meshed, tracked for temporal coherence, texture-mapped and compressed for streaming.
- Capability: Perceptual realism, Persistence
- Paper: https://doi.org/10.1145/2766945 (SIGGRAPH 2015 (ACM TOG))
- Video: https://www.youtube.com/watch?v=_ljYpdGJdoo

### Capture apps & splat tools

Phone and headset capture, training and viewing tools: Luma, Polycam, Scaniverse, Postshot, Hyperscape, SuperSplat…

#### Meta Horizon Hyperscape Capture — Meta (2025-09-17)
- Type: Product / app · Timing: Pre-generated · Access: Product / app, Waitlist / early access
- Input: Passthrough & live surroundings, Multi-view capture / scan → Output: Gaussian splats / radiance field, 3D scene / world
- Idea: Capture by the headset itself turns any room into a revisitable VR setting, but the replica is static, processing is on Meta's servers, and the 2026 removal of sharing shows how quickly a beta platform can change under a study.
- What it is: Hyperscape Capture lets a Meta Quest 3 or 3S owner scan a room by looking around it for a few minutes; Meta's servers then build a photoreal Gaussian-splat replica that can be revisited in the headset. Meta added link sharing for up to eight visitors on 20 November 2025, then removed sharing on 12 May 2026; worlds are now view-only in the Capture (Beta) app.
- How it works: Headset cameras record during a single guided scan session; cloud processing (up to 8 hours per Meta's help page) produces Gaussian splats, now rendered on-device in the Capture app.
- Specs: Quest 3 / 3S · scan in minutes · processing up to 8 h (Meta help page)
- Capability: Situational reach, Authoring accessibility
- Video: https://www.youtube.com/watch?v=zJ4pjwIPiRk
- Project page: https://www.meta.com/help/quest/1088536553019177/

#### Spark — World Labs (2025-06-02)
- Type: Open-source tool · Timing: Real-time streaming · Access: Open weights / code
- Input: Scene spec, code & rules → Output: Gaussian splats / radiance field, 3D scene / world
- Idea: Lets captured or generated splat worlds be wrapped in web interactions, the cheapest route to putting them in front of study participants.
- What it is: Spark is World Labs' open-source Gaussian splat renderer for three.js; Spark 2.0 (April 2026) streams worlds of over 100 million splats into an ordinary web page.
- How it works: A three.js renderer with GPU sorting, level of detail and streaming, plus programmable per-splat effects for editing and animation.
- Specs: 100M+ splats streamed in the browser (Spark 2.0)
- Capability: Authoring accessibility, Situational reach
- Video: https://www.youtube.com/watch?v=BpzKZnV0MQc
- Images: https://sparkjs.dev/static/images/logo-hero.png
- Project page: https://sparkjs.dev/
- Code: https://github.com/sparkjsdev/spark

#### Postshot — Jawset (2024)
- Type: Product / app · Timing: Pre-generated · Access: Product / app
- Input: Video, Multi-view capture / scan → Output: Gaussian splats / radiance field, 3D scene / world
- Idea: Local training gives labs control over data and versions, which cloud capture apps do not.
- What it is: Jawset Postshot is a Windows desktop application that trains Gaussian splats and radiance fields from video or photos on a local NVIDIA GPU, with live preview, editing and plug-ins for After Effects and Unreal.
- How it works: Camera tracking and splat optimisation run locally with a progressive preview; v1.1 (May 2026) is the current release line.
- Capability: Authoring accessibility, Experimental control
- Video: https://www.youtube.com/watch?v=u-EOH3NRFSU
- Project page: https://www.jawset.com/

#### Teleport by Varjo — Varjo (2024-06-18)
- Type: Product / app · Timing: Pre-generated · Access: Product / app
- Input: Video, Multi-view capture / scan → Output: Gaussian splats / radiance field, 3D scene / world
- Idea: Connects capture of real sites to professional XR training and visualisation.
- What it is: Teleport is Varjo's cloud service that turns phone scans or 360° camera footage of real places into Gaussian splat scenes that can be explored on the web, in VR headsets or inside game engines.
- How it works: Uploaded captures are reconstructed in the cloud into splats, with large-area capture and automatic 360° video conversion added in later releases.
- Capability: Situational reach, Authoring accessibility
- Video: https://www.youtube.com/watch?v=15GCm6NlIj4
- Images: https://cdn.prod.website-files.com/6708c29d4750b8ec6dcacff9/674083c9edee9798111729ae_Teleport%20OG.png
- Project page: https://get.teleport.varjo.com/

#### Scaniverse — Niantic Spatial (2024-03-20)
- Type: Product / app · Timing: Pre-generated · Access: Product / app
- Input: Video, Multi-view capture / scan → Output: Gaussian splats / radiance field
- Idea: On-device processing keeps raw footage local, which can matter for ethics review when capturing real spaces.
- What it is: Scaniverse trains Gaussian splats on the phone itself, so a walk around an object or place yields a viewable splat within minutes without uploading; in 2026 it sits inside Niantic Spatial's capture service.
- How it works: Phone video and ARKit/ARCore poses feed an on-device Gaussian optimisation; scans can be shared to Niantic Spatial's map and reconstruction services.
- Capability: Authoring accessibility, Temporal responsiveness
- Video: https://www.youtube.com/watch?v=Arrr6ezwJ_4
- Project page: https://www.nianticspatial.com/products/capture

#### SuperSplat — PlayCanvas (2023-10)
- Type: Open-source tool · Timing: Pre-generated · Access: Open weights / code, Product / app
- Input: Multi-view capture / scan → Output: Gaussian splats / radiance field
- Idea: The common place where captured splats are cleaned and shared, which makes it part of most capture pipelines.
- What it is: SuperSplat is PlayCanvas's free, open-source browser editor for Gaussian splats, plus a hosting site, for cleaning, cropping, combining and publishing splat scenes; version 3.0 (September 2026) was rebuilt on WebGPU.
- How it works: A web app on the PlayCanvas engine edits PLY/SOG splats with selection tools and exports compressed formats for viewers and engines.
- Capability: Authoring accessibility, Experimental control
- Video: https://www.youtube.com/watch?v=7B0KdoJCUK8
- Images: https://superspl.at/header.webp
- Project page: https://superspl.at/
- Code: https://github.com/playcanvas/supersplat

#### Polycam Gaussian Splatting — Polycam (2023-09-28)
- Type: Product / app · Timing: Pre-generated · Access: Product / app
- Input: Multi-view capture / scan, Video → Output: Gaussian splats / radiance field, Mesh / 3D asset
- Idea: Put splat capture in the same app people already used for photogrammetry and LiDAR scans.
- What it is: Polycam, a widely used phone and web 3D scanning app, added Gaussian splat processing so uploaded photos or video become splat scenes viewable at high frame rates in a browser.
- How it works: Photos or video are processed in the cloud into 3D Gaussians alongside mesh and point-cloud outputs, with in-browser editing and export.
- Capability: Authoring accessibility
- Video: https://www.youtube.com/watch?v=m2j8EF6N2G8
- Project page: https://poly.cam/tools/gaussian-splatting

#### Luma 3D Capture — Luma AI (2022)
- Type: Product / app · Timing: Pre-generated · Access: Product / app
- Input: Video, Multi-view capture / scan → Output: Gaussian splats / radiance field, 3D scene / world
- Idea: Brought radiance-field capture to ordinary phones before most people had heard of NeRF.
- What it is: Luma's phone app guided people through filming an object or place and returned a NeRF, later a Gaussian-splat 'interactive scene' that could be embedded on the web or exported to game engines.
- How it works: A guided capture UI collects video around the subject; cloud reconstruction trains a NeRF or 3D Gaussian scene with meshes and exports for Unreal and other tools.
- Capability: Authoring accessibility
- Video: https://www.youtube.com/watch?v=JXb_a3ZIGnI
- Project page: https://lumalabs.ai/

#### Nerfstudio — Matthew Tancik (2022)
- Type: Open-source tool · Timing: Pre-generated · Access: Open weights / code
- Input: Multi-view capture / scan, Video → Output: Gaussian splats / radiance field
- Idea: A shared, versioned codebase makes reconstruction choices reportable and repeatable across labs.
- What it is: Nerfstudio is an open-source framework and web viewer for training and comparing radiance fields and Gaussian splats (via gsplat) from your own captures.
- How it works: Modular PyTorch components (data parsers, samplers, fields, renderers) with the Nerfacto and Splatfacto methods and a browser viewer.
- Capability: Experimental control, Authoring accessibility
- Paper: https://arxiv.org/abs/2302.04264 (SIGGRAPH 2023)
- Video: https://www.youtube.com/watch?v=nSFsugarWzk
- Images: https://assets.nerf.studio/opg.png
- Project page: https://docs.nerf.studio/
- Code: https://github.com/nerfstudio-project/nerfstudio

## Agents & Simulated Societies

Characters and populations driven by language models that remember, plan and act inside worlds: the social side of a generated situation.

### Generative agents & social simulation

Believable agents with memory and reflection, from Smallville to simulations of whole populations.

#### Simile — Simile, Joon Sung Park (2026-02-12)
- Type: Platform / API · Timing: Turn-based · Access: Product / app
- Input: Text prompt → Output: Dialogue / text, Agent behaviour & actions
- Idea: Population simulation has become a product; its accuracy claims are exactly what behavioral researchers would need to check before using such twins as participants.
- What it is: A commercial platform that simulates how real customer groups would respond to a product launch, price change or campaign, using agents built from interviews and survey data in the line of the Stanford 1,000-person study.
- How it works: Likely the generative-agent architecture with interview-grounded personas, validated by comparing simulated and held-out human response distributions; Simile reports enterprise studies (e.g. with CVS Health) but does not publish full model details.
- Capability: Situation diversity, Situational reach, Behavioral plausibility
- Video: https://www.youtube.com/watch?v=_7FuglsjhbM
- Images: https://cdn.sanity.io/images/bz52j8pw/production/2b12507f79346d8ce26c4e362188d12e57e13414-1200x630.png?rect=0,2,1200,627&w=1200&h=627&fit=crop&auto=format
- Project page: https://www.simile.com/

#### AgentSociety — Tsinghua University FIB Lab (2025-02-12)
- Type: Open-source tool · Timing: Pre-generated · Access: Open weights / code
- Input: Scene spec, code & rules, Text prompt → Output: Agent behaviour & actions, Dialogue / text
- Idea: Treats an agent population as a lab where interventions that are unethical or impossible with people can be piloted first.
- What it is: A simulator that gives more than 10,000 LLM agents jobs, homes, mobility and social ties inside a modelled city, then runs social experiments on them: polarization, inflammatory messages, universal basic income and a hurricane shock.
- How it works: LLM agents with needs, emotions and memories act in an urban environment (mobility, economy, social network) on a distributed simulation engine; the authors report about 5 million agent and environment interactions and compare outcomes with findings from human studies.
- Specs: 10,000+ agents · ~5 million interactions
- Capability: Situational reach, Experimental control, Situation diversity
- Paper: https://arxiv.org/abs/2502.08691 (arXiv)
- Video: https://www.youtube.com/watch?v=Oww_rbKvM0U
- Images: https://opengraph.githubassets.com/2adbf7870edfc463bf6e2fc58ee3d5f0698af94621dca4e2ac4df3208861b60b/tsinghua-fib-lab/AgentSociety
- Project page: https://agentsociety.readthedocs.io/
- Code: https://github.com/tsinghua-fib-lab/AgentSociety

#### OASIS — CAMEL-AI (2024-11-18)
- Type: Open-source tool · Timing: Pre-generated · Access: Open weights / code
- Input: Scene spec, code & rules → Output: Agent behaviour & actions, Dialogue / text
- Idea: Lets you test how a feed algorithm or a rumor changes a crowd before trying anything on real users.
- What it is: A social-media simulator in which up to one million LLM agents follow, post, comment and repost on X- and Reddit-like platforms with recommendation feeds, used to replicate information spread, group polarization and herd effects.
- How it works: Agents built on the CAMEL framework act through a shared action space over a dynamic social graph; an environment server and interest- or hot-score-based recommender update what each agent sees, and parallel LLM inference lets it scale to very large populations.
- Specs: up to 1,000,000 agents
- Capability: Situational reach, Situation diversity, Experimental control
- Paper: https://arxiv.org/abs/2411.11581 (arXiv)
- Video: https://www.youtube.com/watch?v=wjLHrdZ1Smk
- Images: https://raw.githubusercontent.com/camel-ai/oasis/main/assets/banner.png
- Project page: https://github.com/camel-ai/oasis
- Code: https://github.com/camel-ai/oasis

#### Generative Agent Simulations of 1,000 People — Joon Sung Park (2024-11-15)
- Type: Research demo · Timing: Turn-based · Access: Research only, Open weights / code
- Input: Speech & audio, Text prompt → Output: Dialogue / text, Agent behaviour & actions
- Idea: Agents grounded in a real person's own words, not demographics, can stand in for that individual on held-out questions; this is the bridge from Smallville to participant 'digital twins' in behavioral research.
- What it is: Stanford researchers interviewed 1,052 Americans for two hours each and turned every transcript into an agent that answers surveys, personality tests and economic games as that person would. The agents were scored against the participants' own answers given two weeks later.
- How it works: An AI interviewer ran semi-structured American Voices Project interviews; full transcripts were placed in an LLM's context to build per-person agents, evaluated on General Social Survey items, Big Five, economic games and replicated experiments, normalised by each participant's two-week test-retest consistency.
- Specs: 1,052 participants · 2-hour interviews · 83–86% of test-retest consistency on GSS
- Capability: Behavioral plausibility, Experimental control, Situation diversity
- Paper: https://arxiv.org/abs/2411.10109 (arXiv)
- Video: https://www.youtube.com/watch?v=6EIkeKruJaI
- Images: https://raw.githubusercontent.com/StanfordHCI/genagents/main/static_dir/cover3.png
- Project page: https://arxiv.org/abs/2411.10109
- Code: https://github.com/StanfordHCI/genagents

#### Project Sid — Altera (Fundamental Research Labs) (2024-10-31)
- Type: Research demo · Timing: Real-time streaming · Access: Research only
- Input:  → Output: Agent behaviour & actions, Dialogue / text
- Idea: Scale changes the questions: with hundreds of agents in one persistent world, you can watch institutions and culture form, or fail to.
- What it is: Up to more than 1,000 LLM agents share a Minecraft server for hours: they take on roles such as farmer or guard, vote to change a tax law, and pass a parody religion from agent to agent.
- How it works: The PIANO architecture runs concurrent modules (memory, action, talking, social awareness, goals) and a cognitive controller that keeps an agent's speech and actions coherent in real time; societies were scored on civilizational benchmarks such as specialization, rule adherence and meme transmission.
- Specs: 10–1,000+ agents · Minecraft
- Capability: Behavioral plausibility, Persistence, Situation diversity
- Paper: https://arxiv.org/abs/2411.00114 (arXiv)
- Video: https://www.youtube.com/watch?v=2tbaCn0Kl90
- Images: https://raw.githubusercontent.com/altera-al/project-sid/main/visual_abstract.png
- Project page: https://github.com/altera-al/project-sid
- Code: https://github.com/altera-al/project-sid

#### Concordia — Google DeepMind (2023-12-06)
- Type: Open-source tool · Timing: Turn-based · Access: Open weights / code
- Input: Text prompt, Scene spec, code & rules → Output: Dialogue / text, Agent behaviour & actions
- Idea: Separates who acts from what the world says happened, which gives social scientists one place to set, log and audit the rules of a simulated situation.
- What it is: An open-source Python library for generative agent-based models: researchers write characters and a scenario, and a 'Game Master' agent narrates what happens when the characters act, much like a tabletop role-playing game.
- How it works: Agents are built from composable LLM components (memory, observation, plans, identity); the Game Master resolves free-text actions into events grounded in physical, social or digital state; v2.0 restructured the components, and the NeurIPS 2024 Concordia Contest used it for cooperation research.
- Capability: Experimental control, Authoring accessibility, Behavioral plausibility
- Paper: https://arxiv.org/abs/2312.03664 (arXiv)
- Video: https://www.youtube.com/watch?v=2FO5g65mu2I
- Images: https://opengraph.githubassets.com/4de00716ff808a0096aa35431807b2a0ef1508212df30727e4812f407badf203/google-deepmind/concordia
- Project page: https://github.com/google-deepmind/concordia
- Code: https://github.com/google-deepmind/concordia

#### AI Town — Andreessen Horowitz (a16z) (2023-08)
- Type: Open-source tool · Timing: Real-time streaming · Access: Open weights / code
- Input: Text prompt → Output: Agent behaviour & actions, Dialogue / text
- Idea: Turned the generative-agents paper into a template people fork for their own simulated communities and games.
- What it is: A deployable, MIT-licensed town in the browser where LLM characters walk around, start conversations and remember them; a visitor can join as a character and chat with the residents.
- How it works: A TypeScript game loop on the Convex reactive database stores world state, agent memories and embeddings, and calls a hosted or local LLM (OpenAI, Together or Ollama) for conversations and memory summaries.
- Capability: Authoring accessibility, Co-creation & agency
- Video: https://www.youtube.com/watch?v=UoJjeyQR66s
- Images: https://opengraph.githubassets.com/475a5f833a271707e21592833533372def75afb692ea2a116bc756cff677f406/a16z-infra/ai-town
- Project page: https://www.convex.dev/ai-town
- Code: https://github.com/a16z-infra/ai-town

#### Generative Agents (Smallville) — Joon Sung Park (2023-04-07)
- Type: Research demo · Timing: Turn-based · Access: Open weights / code, Research only
- Input: Text prompt → Output: Agent behaviour & actions, Dialogue / text
- Idea: Memory, reflection and planning on top of an LLM are enough to make a small society that coordinates over days without a script.
- What it is: Twenty-five LLM-driven characters live in Smallville, a pixel-art town: they wake, work, gossip, form opinions and remember each other. Seeded with one agent's wish to host a Valentine's Day party, the others spread invitations, ask each other on dates and show up at the right time.
- How it works: Each agent keeps a natural-language memory stream; retrieval by recency, importance and relevance feeds GPT-3.5 prompts that write reflections and hierarchical day plans, which a sandbox game engine turns into movement and dialogue; believability was rated by human evaluators against ablations.
- Specs: 25 agents · 2 game days · GPT-3.5-turbo
- Capability: Behavioral plausibility, Persistence, Co-creation & agency
- Paper: https://arxiv.org/abs/2304.03442 (UIST 2023)
- Video: https://www.youtube.com/watch?v=ZdoU9vI2yCg
- Images: https://raw.githubusercontent.com/joonspk-research/generative_agents/main/cover.png
- Project page: https://github.com/joonspk-research/generative_agents
- Code: https://github.com/joonspk-research/generative_agents

### Agents that act in 3D worlds

Agents that perceive and act in games and generated worlds: Voyager, SIMA, game-playing agents.

#### NitroGen — NVIDIA (2026-01-04)
- Type: Model · Timing: Real-time streaming · Access: Open weights / code
- Input: Video → Output: Agent behaviour & actions
- Idea: Internet gameplay video becomes training data for agents, the same way it is for video world models.
- What it is: An open vision-action foundation model for gaming agents, trained on 40,000 hours of public gameplay videos from more than 1,000 games, that plays 3D action games, 2D platformers and procedurally generated worlds from raw frames.
- How it works: Player actions are extracted automatically from on-screen controller overlays in gameplay videos, and a unified vision-action model is trained by large-scale behavior cloning; NVIDIA reports up to 52% relative improvement on unseen games over training from scratch.
- Specs: 40,000 h video · 1,000+ games
- Capability: Situation diversity, Reactivity
- Paper: https://arxiv.org/abs/2601.02427 (arXiv)
- Video: https://nitrogen.minedojo.org/assets/videos/banner.mp4
- Images: https://nitrogen.minedojo.org/assets/images/nitrogen_overview.webp
- Project page: https://nitrogen.minedojo.org/
- Code: https://github.com/MineDojo/NitroGen

#### SIMA 2 — Google DeepMind (2025-11-13)
- Type: Research demo · Timing: Real-time streaming · Access: Waitlist / early access
- Input: Text prompt, Image, Video → Output: Agent behaviour & actions, Dialogue / text
- Idea: The first public pairing of a generalist agent with a world model: Genie 3 makes the world, SIMA 2 acts in it and improves there without new human data.
- What it is: A Gemini-based game companion that reasons about goals, talks with the player, follows instructions given as text in several languages, emoji or images, and carries skills into games it has never seen, including 3D worlds generated on the fly by Genie 3.
- How it works: A Gemini foundation model fine-tuned on human gameplay and Gemini-labelled data maps screen frames and instructions to keyboard-mouse actions; in a self-improvement loop Gemini proposes tasks and estimates rewards, and the agent's own trajectories train its next version.
- Capability: Reactivity, Adaptation, Co-creation & agency
- Paper: https://arxiv.org/abs/2512.04797 (arXiv)
- Video: https://www.youtube.com/watch?v=Zphax4f6Rls
- Images: https://lh3.googleusercontent.com/A5vgACWjzxaEanLkjrZSNlQDjI0SEZ4tKJqE2EtboljSRIkcbEVv4JA2H7a-BEYNoWK097hNdthFdB6h537DUVvFbAUwhWUFSzzA0E0ndr6zMC8tMA=w1200-h630-n-nu-rw
- Project page: https://deepmind.google/blog/sima-2-an-agent-that-plays-reasons-and-learns-with-you-in-virtual-3d-worlds/

#### Lumine — ByteDance Seed, Weihao Tan (2025-11-12)
- Type: Research demo · Timing: Real-time streaming · Access: Research only
- Input: Video, Text prompt → Output: Agent behaviour & actions
- Idea: Real-time, hours-long play in a commercial open world means an agent can now be a long-lived companion or test player inside 3D worlds.
- What it is: A vision-language agent that plays Genshin Impact in real time, finishing the five-hour Mondstadt main storyline at roughly human pace, and without fine-tuning completes 100-minute missions in Wuthering Waves and the first chapter of Honkai: Star Rail.
- How it works: A vision-language model trained on a curriculum of 1,731 hours of human gameplay (action primitives), 200 hours of instruction-following data and 15 hours of reasoning data reads frames at 5 Hz, emits 30 Hz keyboard-mouse action chunks and calls on reasoning only when needed.
- Specs: 5 Hz perception · 30 Hz actions · 5-hour storyline
- Capability: Reactivity, Persistence
- Paper: https://arxiv.org/abs/2511.08892 (arXiv)
- Video: https://www.youtube.com/watch?v=aNmR8PhN-m8
- Images: https://img.alicdn.com/imgextra/i4/2042484851/O1CN01jUnyzn1lhoQ0yKvbC_!!2042484851.jpg
- Project page: https://www.lumine-ai.org/

#### Game-TARS — ByteDance Seed (2025-10-27)
- Type: Model · Timing: Real-time streaming · Access: Research only
- Input: Video, Text prompt → Output: Agent behaviour & actions
- Idea: One action space for every game lets agent training scale like language-model pretraining.
- What it is: A generalist game agent that controls any game through native keyboard and mouse input; ByteDance reports about twice the previous best success rate on open-world Minecraft tasks and near novice-human generality in unseen web 3D games.
- How it works: Continual pretraining on more than 500B tokens of multimodal trajectories across OS, web and game domains, with a decaying continual loss against causal confusion and a sparse-thinking strategy that reasons only at key steps.
- Specs: 500B+ training tokens
- Capability: Reactivity, Situation diversity
- Paper: https://arxiv.org/abs/2510.23691 (arXiv)
- Video: https://lf3-static.bytednsdoc.com/obj/eden-cn/eojfrzeh7vhouloj/seed-tars/game-tars-unseen.mp4
- Images: https://lf3-static.bytednsdoc.com/obj/eden-cn/eojfrzeh7vhouloj/seed-tars/game-tars-hero.png
- Project page: https://seed-tars.com/game-tars/

#### SIMA — Google DeepMind (2024-03-13)
- Type: Research demo · Timing: Real-time streaming · Access: Research only
- Input: Text prompt, Video → Output: Agent behaviour & actions
- Idea: Uses the same pixels-in, keyboard-out interface as a human, so one agent can enter any game, including generated worlds, without an API.
- What it is: A Scalable Instructable Multiworld Agent that watches the screen and presses keys to follow spoken-style instructions such as 'chop down the tree' or 'open the map' across nine commercial games, including No Man's Sky, Valheim and Teardown, and four research environments.
- How it works: Pretrained image and video encoders plus a text encoder feed a transformer policy trained by behavioral cloning on human gameplay annotated with instructions; about 600 basic skills of roughly 10 seconds were evaluated.
- Specs: 9 games + 4 research environments · ~600 skills
- Capability: Reactivity, Situation diversity
- Paper: https://arxiv.org/abs/2404.10179 (arXiv)
- Video: https://storage.googleapis.com/gdm-deepmind-com-prod-public/media/media/Compressed-Fig_2_Sima_1.mp4
- Images: https://lh3.googleusercontent.com/he4kR35RBqPtN9SQ4qMzZjlZJFY9ocs14rJls1ELrNoNoF7MzbF6U-dDBtvNxnI2a6PY_xhHdgQT61BMCpph94Vu4h1mT9fTORPajOwYeS2ypulXSQ=w1200-h630-n-nu-rw
- Project page: https://deepmind.google/blog/sima-generalist-ai-agent-for-3d-virtual-environments/

#### Cradle — Weihao Tan, Beijing Academy of Artificial Intelligence (BAAI) (2024-03-05)
- Type: Research demo · Timing: Turn-based · Access: Open weights / code
- Input: Video, Text prompt → Output: Agent behaviour & actions
- Idea: Showed that a general agent can enter a commercial 3D game through the same screen a player sees, at the price of being far slower than real time.
- What it is: A framework that lets a multimodal LLM play Red Dead Redemption 2's main story missions using only screenshots and keyboard-mouse output, and that transfers to Stardew Valley, Cities: Skylines and everyday software.
- How it works: GPT-4V / GPT-4o models run a loop of information gathering, self-reflection, task inference, skill curation, action planning and memory, writing and reusing skill code that issues keyboard and mouse events.
- Capability: Reactivity, Adaptation
- Paper: https://arxiv.org/abs/2403.03186 (arXiv)
- Video: https://www.youtube.com/watch?v=ay5gBqzPcDE
- Images: https://baai-agents.github.io/Cradle/images/cradle-banner.png
- Project page: https://baai-agents.github.io/Cradle/
- Code: https://github.com/BAAI-Agents/Cradle

#### Voyager — Guanzhi Wang, NVIDIA (2023-05-25)
- Type: Research demo · Timing: Turn-based · Access: Open weights / code
- Input: Text prompt → Output: Agent behaviour & actions
- Idea: An agent that stores what it learns as code can keep growing in an open world, a pattern later NPC and world-agent systems reuse.
- What it is: A GPT-4 agent that plays Minecraft without human input: it proposes its own next goals, writes JavaScript to reach them, and saves working code as reusable skills, going from punching trees to mining diamonds.
- How it works: An automatic curriculum, an iterative prompting loop with environment feedback, execution errors and self-verification, and a vector-indexed skill library drive GPT-4 through the Mineflayer API; the authors report 3.3x more unique items and up to 15.3x faster tech-tree progress than prior methods.
- Capability: Adaptation, Persistence
- Paper: https://arxiv.org/abs/2305.16291 (arXiv)
- Video: https://voyager.minedojo.org/assets/videos/gallery/diamond.mp4
- Images: https://voyager.minedojo.org/assets/images/components.png
- Project page: https://voyager.minedojo.org/
- Code: https://github.com/MineDojo/Voyager

#### XLand: Open-Ended Learning Agents — Google DeepMind (2021)
- Type: Research demo · Timing: Pre-generated · Access: Research only
- Input:  → Output: Agent behaviour & actions
- Idea: A precursor of SIMA and of agents in generated worlds: generality came from training across a generated space of situations rather than one handcrafted task.
- What it is: Agents trained in XLand, a procedurally generated universe of 3D worlds and multiplayer games, learn general behaviors such as experimenting, cooperating and using objects, and then play held-out games like hide-and-seek and capture the flag without further training.
- How it works: Deep reinforcement learning with population-based training and a dynamic curriculum that generates worlds, goals and co-players matched to each agent's current ability, evaluated zero-shot on held-out tasks.
- Capability: Situation diversity, Adaptation
- Paper: https://arxiv.org/abs/2107.12808 (arXiv)
- Video: https://www.youtube.com/watch?v=lTmL7jwFfdw
- Project page: https://deepmind.google/blog/generally-capable-agents-emerge-from-open-ended-play/

#### Multi-Agent Hide and Seek — OpenAI (2019)
- Type: Research demo · Timing: Pre-generated · Access: Open weights / code, Research only
- Input:  → Output: Agent behaviour & actions
- Idea: A precursor of agents in worlds: competition alone produced a sequence of strategies nobody designed.
- What it is: Teams of hiders and seekers trained by reinforcement learning in a 3D physics world discover, over hundreds of millions of games, how to build forts from boxes, use ramps to climb walls and exploit physics glitches.
- How it works: Multi-agent self-play with PPO and entity-centric attention policies in a MuJoCo environment; six phases of emergent strategy were identified and compared with intrinsic-motivation baselines.
- Capability: Behavioral plausibility, Reactivity
- Paper: https://arxiv.org/abs/1909.07528 (ICLR 2020)
- Video: https://www.youtube.com/watch?v=kopoLzvh5jY
- Project page: https://openai.com/index/emergent-tool-use/
- Code: https://github.com/openai/multi-agent-emergence-environments

### NPC & character platforms

Engines for conversational characters in games and XR: Inworld, Convai, ACE, AI NPCs in shipped games.

#### Total War: PHARAOH AI advisor (NVIDIA ACE demo) — NVIDIA (2026-01-05)
- Type: Research demo · Timing: Turn-based · Access: Research only
- Input: Speech & audio, Text prompt → Output: Speech / voice, Dialogue / text
- Idea: An NPC whose job is to coach the player inside the game, a pattern that maps directly onto tutors in training simulations.
- What it is: A CES 2026 tech demo that adds a talking advisor to Creative Assembly's strategy game Total War: PHARAOH: players ask about the game's systems and their current campaign, and the advisor answers in voice.
- How it works: NVIDIA ACE runs speech recognition, a small language model grounded in game data and current game state, and speech synthesis on the local RTX GPU.
- Capability: Adaptation, Temporal responsiveness
- Video: https://www.youtube.com/watch?v=6es-Zvh5bu4
- Images: https://www.nvidia.com/content/dam/en-zz/Solutions/geforce/news/ces-2026-nvidia-geforce-rtx-announcements/ces-2026-nvidia-geforce-rtx-announcements-ogimage.jpg
- Project page: https://www.nvidia.com/en-us/geforce/news/ces-2026-nvidia-geforce-rtx-announcements/

#### Teammates — Ubisoft (2025-11-21)
- Type: Research demo · Timing: Real-time streaming · Access: Waitlist / early access
- Input: Speech & audio → Output: Dialogue / text, Speech / voice, Agent behaviour & actions
- Idea: Moves generative NPCs from conversation to coordinated action: natural speech becomes the controller for teammates in a live combat situation.
- What it is: A playable first-person shooter level in which the player gives spoken orders to two AI squadmates, Pablo and Sofia, and to an in-game assistant, Jaspar, who can highlight enemies, explain lore, change settings or pause the game. It was playtested with a few hundred players.
- How it works: Built on Ubisoft's Snowdrop engine; speech is transcribed and interpreted together with game-state context by an LLM layer (reported as Google Gemini with internal middleware) that selects squad behaviors and generates voiced replies.
- Capability: Reactivity, Temporal responsiveness, Co-creation & agency
- Video: https://www.youtube.com/watch?v=y6uBzRpqT3w
- Images: https://staticctf.ubisoft.com/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/5YY8eeQIZh8QolUZwzJOhF/8a826f0cfcca1a41dda148c808096435/Ubisoft_Teammates_XP_Sofia_and_Pablo.jpg
- Project page: https://news.ubisoft.com/en-us/article/3mWlITIuWuu0MoVuR6o8ps/ubisoft-reveals-teammates--an-ai-experiment-to-change-the-game

#### Whispers from the Star — Anuttacon (2025-08-14)
- Type: Product / app · Timing: Turn-based · Access: Product / app
- Input: Speech & audio, Text prompt → Output: Speech / voice, Dialogue / text, Virtual human (face / body)
- Idea: A whole commercial game built on one LLM character and open voice conversation, which tests whether a single relationship can carry an experience.
- What it is: An interactive science-fiction story in which the player keeps Stella, an astronaut stranded on an alien planet, alive by talking to her through a communicator; there are no dialogue options, and what she does next depends on what the player says.
- How it works: Likely a proprietary LLM pipeline with speech recognition, a persona and story-state model for Stella, synthesized voice and rendered character animation; Anuttacon has not published technical details.
- Capability: Temporal responsiveness, Co-creation & agency, Behavioral plausibility
- Video: https://www.youtube.com/watch?v=3hnIPdVZK1A
- Images: https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/3730100/f4c10b5b4ad08b6e879bb53ffa12f5123cca760e/header.jpg?t=1764897761
- Project page: https://store.steampowered.com/app/3730100/

#### AI Darth Vader in Fortnite — Epic Games (2025-05-16)
- Type: Product / app · Timing: Turn-based · Access: Product / app
- Input: Speech & audio → Output: Speech / voice, Dialogue / text, Agent behaviour & actions
- Idea: The largest public test of a licensed LLM character so far, and a clear lesson that a character's voice and persona need guardrails before release.
- What it is: Fortnite players could recruit Darth Vader to their squad and talk to him over the microphone; he answered in a synthesized James Earl Jones voice. Players got him to swear within hours, which Epic patched. The underlying tech went to creators as the Persona device, renamed Conversations and released as an experimental UEFN feature on 2026-04-16 (publishing not yet enabled).
- How it works: Push-to-talk speech goes to Google's Gemini 2.0 Flash, prompted with Vader's persona, and the text reply is voiced by ElevenLabs Flash v2.5 in a voice modeled on Jones, who had signed the rights over to Disney in 2022; reports say Conversations uses Gemini 3.1 Flash-Lite with ElevenLabs.
- Capability: Temporal responsiveness, Reactivity, Authoring accessibility
- Video: https://www.youtube.com/watch?v=M7spbUI40NQ
- Project page: https://www.fortnite.com/news/bring-npcs-to-life-with-ai-powered-conversations

#### NARAKA: BLADEPOINT AI Teammate — NetEase Games, NVIDIA (2025-01-06)
- Type: Product / app · Timing: Real-time streaming · Access: Product / app
- Input:  → Output: Agent behaviour & actions
- Idea: One of the first shipped LLM teammates in a large Chinese action game, run on the player's GPU rather than a server.
- What it is: Since 27 March 2025, players of NetEase's NARAKA: BLADEPOINT Mobile PC Version (Chinese market) can add an on-device AI teammate to their party in Free Training: it fights alongside them, finds items they need, swaps gear and suggests which skills to unlock.
- How it works: Likely an NVIDIA ACE small language model on the local GeForce RTX GPU that picks high-level actions and suggestions, while the game's own combat AI executes moves; NetEase has not published model details.
- Capability: Reactivity, Adaptation
- Video: https://www.youtube.com/watch?v=I65tiaHQuFk
- Images: https://www.nvidia.com/content/dam/en-zz/Solutions/geforce/news/nvidia-ace-naraka-bladepoint-inzoi-launch-this-month/nvidia-ace-inzoi-naraka-bladepoint-mobile-pc-version-launch-this-month-ogimage.jpg
- Project page: https://www.nvidia.com/en-us/geforce/news/nvidia-ace-naraka-bladepoint-inzoi-launch-this-month/

#### PUBG Ally — KRAFTON, NVIDIA (2025-01-06)
- Type: Product / app · Timing: Real-time streaming · Access: Waitlist / early access
- Input: Speech & audio → Output: Agent behaviour & actions, Dialogue / text, Speech / voice
- Idea: A teammate that both talks and acts in a fast competitive game, running on the player's own GPU rather than in the cloud.
- What it is: An AI teammate for PUBG: Battlegrounds that the player talks to by voice: it calls out enemies in game lingo, shares loot, drives vehicles and fights alongside the player. KRAFTON calls it a Co-Playable Character; after demos at CES 2025 and GDC 2026 it was scheduled to launch in summer 2026 through PUBG's Arcade Mode beta.
- How it works: First shown with the Mistral-NeMo-Minitron-8B small language model through NVIDIA ACE; KRAFTON then moved from a behavior-tree-plus-SLM workflow to an autonomous tool-calling agent loop on a distilled on-device Nemotron model, adding long-term memory (announced at CES 2026).
- Capability: Reactivity, Temporal responsiveness, Adaptation
- Video: https://www.youtube.com/watch?v=ukV-ZUJ1mTo
- Images: https://www.nvidia.com/content/dam/en-zz/Solutions/geforce/news/nvidia-ace-autonomous-ai-companions-pubg-naraka-bladepoint/nvidia-ace-autonomous-ai-companions-ogimage.jpg
- Project page: https://www.krafton.ai/blog/pubg_ally_nemotron/

#### inZOI Smart Zoi — KRAFTON, NVIDIA (2025-01-06)
- Type: Product / app · Timing: Real-time streaming · Access: Product / app
- Input: Text prompt → Output: Agent behaviour & actions, Dialogue / text
- Idea: A whole simulated town of LLM-driven residents in a mass-market game, running locally, which is close to a playable Smallville.
- What it is: In KRAFTON's life simulation inZOI, Smart Zoi lets every resident of a city act on its own life goals, react to events around it and adjust tomorrow's schedule from today's experiences, instead of waiting for player commands; players can read a Smart Zoi's inner thoughts as they happen and nudge them. The experimental setting shipped with the game's Steam early access in March 2025 for GeForce RTX GPUs.
- How it works: A 0.5B-parameter Mistral-NeMo-Minitron small language model running on-device through NVIDIA ACE selects each Zoi's next action from the game's action set, guided by goals, memories and reflections, with the game simulation executing and animating the choice.
- Specs: 0.5B-parameter SLM · on-device · GeForce RTX
- Capability: Behavioral plausibility, Situation diversity, Reactivity
- Video: https://www.youtube.com/watch?v=Pk9z1upOj3U
- Images: https://shared.akamai.steamstatic.com/store_item_assets/steam/apps/2456740/89acee5c3d965af802002617d6c130e5e03bd240/header.jpg?t=1792094410
- Project page: https://www.nvidia.com/en-us/geforce/news/nvidia-ace-naraka-bladepoint-inzoi-launch-this-month/

#### Covert Protocol — NVIDIA, Inworld AI (2024-03-19)
- Type: Research demo · Timing: Turn-based · Access: Research only
- Input: Speech & audio → Output: Dialogue / text, Speech / voice, Virtual human (face / body)
- Idea: Makes conversation itself the game mechanic: social skill, not dialogue-tree choice, decides progress.
- What it is: A GDC 2024 tech demo in which the player is a private detective in a hotel and must talk information out of AI-driven characters; what each character reveals depends on how the conversation goes, so each playthrough differs.
- How it works: Inworld's character engine handles personas, goals and knowledge for each character, while NVIDIA ACE supplies Riva speech recognition and Audio2Face facial animation; the scene is built in Unreal Engine.
- Capability: Reactivity, Behavioral plausibility
- Video: https://www.youtube.com/watch?v=uryeFhnNzEs
- Images: https://www.nvidia.com/content/dam/en-zz/Solutions/geforce/news/nvidia-ace-gdc-gtc-2024-ai-character-game-and-app-demo-videos/nvidia-ace-covert-protocol-ogimage.jpg
- Project page: https://www.nvidia.com/en-us/geforce/news/nvidia-ace-gdc-gtc-2024-ai-character-game-and-app-demo-videos/

#### NEO NPC — Ubisoft, Inworld AI, NVIDIA (2024-03-19)
- Type: Research demo · Timing: Turn-based · Access: Research only
- Input: Speech & audio, Text prompt → Output: Dialogue / text, Speech / voice, Virtual human (face / body)
- Idea: Recasts the game writer's job: instead of writing every line, the writer writes the person and then tests what the model makes of them.
- What it is: A Ubisoft Paris prototype shown at GDC 2024 in which players negotiate and plan with characters such as Bloom and Iron by speaking freely, while the characters stay within backstories written by a narrative director.
- How it works: Inworld's LLM-based character engine generates dialogue from authored backstories and guardrails, NVIDIA Audio2Face animates the faces, and performance capture from actors sets each character's expressive range.
- Capability: Behavioral plausibility, Authoring accessibility
- Video: https://www.youtube.com/watch?v=TxrYI6Aoav0
- Images: https://staticctf.ubisoft.com/J3yJr34U2pZ2Ieem48Dwy9uqj5PNUQTn/3NWrkKkT1Bxy1f7VUsyH2q/30eb696cebe4ff5ce9efffd52ec303b1/UN-Ubisoft-New-Generative-AI-Prototype-960x540.jpg
- Project page: https://news.ubisoft.com/en-us/article/5qXdxhshJBXoanFZApdG3L/how-ubisofts-new-generative-ai-prototype-changes-the-narrative-for-npcs

#### Convai — Convai (2023)
- Type: Platform / API · Timing: Turn-based · Access: Public API, Product / app
- Input: Speech & audio, Text prompt → Output: Dialogue / text, Speech / voice, Agent behaviour & actions
- Idea: A ready-made path from a written character sheet to an embodied NPC in a 3D or XR scene, without building the speech and action pipeline yourself.
- What it is: A platform for building characters that hold voice conversations, perceive their surroundings and carry out actions such as fetching an object or guiding a player, with plugins for Unreal Engine, Unity and web 3D, and use in VR training scenes.
- How it works: Characters are configured in a web dashboard (backstory, knowledge base, voice, actions); the engine streams speech recognition, LLM responses with action selection, speech synthesis and lip-sync to the game client, and supports NPC-to-NPC conversation and live game-state context.
- Capability: Authoring accessibility, Reactivity, Temporal responsiveness
- Video: https://www.youtube.com/watch?v=q3Th60XdhSs
- Images: https://cdn.prod.website-files.com/66f6655083b0f778e338eebf/66fba91c8dc2a2d8413cf159_openGraph.jpg
- Project page: https://convai.com/
- API docs: https://docs.convai.com/

#### Suck Up! — Proxima (2023-12)
- Type: Product / app · Timing: Turn-based · Access: Product / app
- Input: Speech & audio, Text prompt → Output: Dialogue / text, Speech / voice, Agent behaviour & actions
- Idea: Persuasion of LLM characters as the whole mechanic, and a showcase of how players probe and break character prompts.
- What it is: A comedy game in which the player is a vampire who must talk AI-driven townsfolk into opening their doors, using disguises and improvised lies; each resident has a personality and reacts to what the player says. On Steam since October 2025.
- How it works: Likely a cloud LLM per character with persona prompts and game-state context (disguise, time, prior visits), speech recognition for voice input and synthesized replies; the developer has not published details.
- Capability: Reactivity, Co-creation & agency
- Video: https://www.youtube.com/watch?v=JkObwtlXtC4
- Images: https://cdn.prod.website-files.com/6642c397a9d95685228ac4f3/6644f0c6bc2113e41247eb9e_Suck%20Up!.png
- Project page: https://www.playsuckup.com/

#### NVIDIA ACE for Games: Kairos demo — NVIDIA, Convai (2023-05-28)
- Type: Research demo · Timing: Turn-based · Access: Research only
- Input: Speech & audio → Output: Dialogue / text, Speech / voice, Virtual human (face / body)
- Idea: The demo that set the template for voice-in, voice-and-face-out game characters: speech recognition, an LLM with a persona, speech synthesis and audio-driven facial animation in one loop.
- What it is: In a ray-traced Unreal Engine 5 ramen shop, the player speaks to Jin, the owner, and he answers in voice with lip-synced facial animation, staying within his backstory. Shown in the Computex 2023 keynote.
- How it works: Convai's character platform runs on NVIDIA ACE modules: Riva speech recognition and synthesis, a NeMo language model given Jin's backstory with guardrails, and Audio2Face generating facial animation from the synthesized voice.
- Capability: Temporal responsiveness, Perceptual realism, Behavioral plausibility
- Video: https://www.youtube.com/watch?v=5R8xZb6J3r0
- Images: https://iprsoftwaremedia.com/219/files/20234/646ec444b3aed34ea82f0ed7_nvidia-ace-for-games/nvidia-ace-for-games_b71f46a0-fffd-445d-984b-b531c995ecfb-prv.jpg?v=b71f46a0-fffd-445d-984b-b531c995ecfb
- Project page: https://nvidianews.nvidia.com/news/nvidia-ace-for-games-sparks-life-into-virtual-characters-with-generative-ai

## Generative XR Experiences

Generation inside headsets and glasses: in-situ co-creation in mixed reality, reality restyled live, generative cinema and enactment, and the generative features shipping in XR platforms.

### In-situ co-creation in MR / VR

Speaking, sketching or gesturing content into the space around you: Editing Reality, LLMR, Social Conjuring…

#### Editing Reality — Suibi Che-Chuan Weng, Ryo Suzuki (2026-06-12)
- Type: Research demo · Timing: Turn-based · Access: Research only
- Input: Speech & audio, Sketch & gesture, Passthrough & live surroundings → Output: Mesh / 3D asset, 3D scene / world
- Idea: Treats generation as a material you shape in place, round after round, rather than a one-shot command typed on a screen.
- What it is: A mixed-reality system for co-creating with generative AI inside a physical room: by speaking, sketching and grabbing, a person generates, modifies, erases and retextures virtual and reconstructed objects anchored where they stand.
- How it works: Research through design: iterative system development combining speech, sketch and direct manipulation with generative 3D and texture models, a formative workshop and an expert review, distilled into design framings for in-situ co-creation.
- Capability: Co-creation & agency, Authoring accessibility
- Paper: https://doi.org/10.1145/3800645.3813087 (DIS 2026)
- Video: https://www.youtube.com/watch?v=PzxpJLmMLwk
- Project page: https://ryosuzuki.org/editing-reality

#### Prop-Chromeleon — Haoyu Wang (2026-05-01)
- Type: Research demo · Timing: Turn-based · Access: Research only
- Input: Text prompt, Passthrough & live surroundings → Output: Mesh / 3D asset
- Idea: Constraining generation to the shape of a real object turns any household item into a passive haptic prop for generated content.
- What it is: Hold a water bottle, type 'a magic lantern', and a virtual lantern shaped to fit the bottle is generated and anchored onto it in mixed reality, so what you see matches what you feel.
- How it works: A generative pipeline produces 3D assets from text prompts under geometric constraints from the scanned prop and anchors them to it; a generation study scores shape similarity and prompt fidelity, and a user study compares realism and enjoyment with static props.
- Capability: Perceptual realism, Authoring accessibility
- Paper: https://arxiv.org/abs/2605.00804 (DIS 2026)
- Video: https://www.youtube.com/watch?v=IKRM-_YxGpM
- Images: https://arxiv.org/html/2605.00804v2/figures/teaser.png
- Project page: https://arxiv.org/abs/2605.00804

#### Vibe Coding XR — Ruofei Du, Google (2026-03-25)
- Type: Research demo · Timing: Turn-based · Access: Open weights / code, Research only
- Input: Text prompt → Output: Agent behaviour & actions, 3D scene / world
- Idea: Gives language models a compact vocabulary for users, rooms and agents, so a one-line request can produce a runnable XR prototype.
- What it is: A prompt such as 'create a dandelion that reacts to my hand' becomes a working, physics-aware mixed-reality app that can be tested in a simulated room on the desktop and then sent to a headset.
- How it works: Gemini generates code against XR Blocks' semantic 'Reality Model' WebXR API; a desktop simulated-reality loop precedes headset deployment, and the VCXR60 set of 60 prompts with automated evaluation measures one-shot success.
- Specs: VCXR60: 60 prompts
- Capability: Authoring accessibility
- Paper: https://arxiv.org/abs/2603.24591 (arXiv 2026)
- Video: https://www.youtube.com/watch?v=nknCzIxHHzw
- Images: https://arxiv.org/html/2603.24591v2/vcxr_samples.png
- Project page: https://xrblocks.github.io/
- Code: https://github.com/google/xrblocks

#### NeXus Print — Ars Electronica Futurelab (2025-09)
- Type: Experience / artwork · Timing: Turn-based
- Input: Text prompt, Sketch & gesture → Output: Mesh / 3D asset, 3D scene / world
- Idea: A public, festival-scale version of multi-user in-situ generation, framed as a tool for collective brainstorming and rethinking public spaces.
- What it is: Groups wearing Meta Quest 3 enter one shared XR space and, with simple text prompts and hand gestures, generate 3D objects and environments to build or reimagine a world together.
- How it works: A shared Quest 3 session links hand-gesture interaction with text-to-3D generation of objects and environments (developed with Dai Nippon Printing).
- Specs: Meta Quest 3 · multi-user
- Capability: Co-creation & agency, Authoring accessibility
- Recognition: Open Futurelab, Ars Electronica Festival 2025
- Video: https://www.youtube.com/watch?v=HH4xfM-XL2Q
- Images: https://ars.electronica.art/futurelab/files/2025/10/ars-electronica-2025-20cbettinagangl_4932x3288-1-2000x1000.jpg
- Project page: https://ars.electronica.art/futurelab/en/nexus-print/

#### Drawings into playable XR worlds — Stijn Spanhove (2025-08-28)
- Type: Research demo · Timing: Real-time streaming · Access: Research only
- Input: Image, Keyboard & controller actions → Output: Interactive frame stream
- Idea: An early sign of action-conditioned world models streaming into AR glasses, with a drawing as the only authoring step.
- What it is: A child's drawing is fed to the Mirage 2 world model and opens up in front of the viewer on Snap Spectacles as a world they can play in.
- How it works: Proof of concept: the drawing is sent as the starting image to Dynamics Lab's Mirage 2 interactive world model and the generated frame stream is displayed on Spectacles, with inputs passed back to the model.
- Capability: Co-creation & agency, Reactivity
- Video: https://x.com/stspanho/status/1961138591934947462
- Project page: https://x.com/stspanho/status/1961138591934947462

#### Capybara — Lei Zhang (2025-08-11)
- Type: Research demo · Timing: Turn-based · Access: Research only
- Input: Text prompt, Body, face & gaze tracking, Passthrough & live surroundings → Output: Mesh / 3D asset, Motion / animation, Agent behaviour & actions
- Idea: Positions children as authors of AI-driven AR, not only its audience.
- What it is: Children create 3D characters and accessories with text-to-3D AI, animate them with auto-rigging and their own body movements, and program how the characters react to real objects the camera recognizes.
- How it works: An AR visual-programming environment combines text-to-3D generation, automatic rigging, body tracking and vision-based object recognition as programmable triggers; user studies with 20 children in the United States and Argentina.
- Specs: user studies with 20 children (US, Argentina)
- Capability: Authoring accessibility, Co-creation & agency
- Paper: https://arxiv.org/abs/2508.08467 (UIST 2025)
- Video: https://www.youtube.com/watch?v=paJP8B8btVk
- Images: https://arxiv.org/html/2508.08467v2/Figures/Teaser_Figure_V20.png
- Project page: https://arxiv.org/abs/2508.08467

#### EchoLadder — Zhuangze Hou (2025-08-04)
- Type: Research demo · Timing: Turn-based · Access: Research only
- Input: Speech & audio → Output: 3D scene / world
- Idea: Breaking generation into reversible, progressive suggestions keeps people steering the scene instead of accepting one AI output.
- What it is: A VR designer speaks instructions at any level of vagueness ('make it cosier', 'put a lamp by the sofa') and receives concrete scene changes that can be applied, regenerated or retracted with a toggle.
- How it works: A large vision-language model reads the current VR scene and the spoken instruction and proposes concrete edits through a progressive design pipeline; an ablation study and a user study against a no-suggestion baseline.
- Capability: Authoring accessibility, Experimental control
- Paper: https://arxiv.org/abs/2508.02173 (UIST 2025)
- Video: https://www.youtube.com/watch?v=mSZTSsDLjRE
- Images: https://arxiv.org/html/2508.02173v1/Pic_table/Teaser.png
- Project page: https://arxiv.org/abs/2508.02173

#### ImaginateAR — Jaewook Lee, Niantic Spatial (2025-04-30)
- Type: Research demo · Timing: Turn-based · Access: Research only
- Input: Speech & audio, Passthrough & live surroundings → Output: Mesh / 3D asset, 3D scene / world
- Idea: Pairs pre-computed scene understanding of a real place with fast 3D generation so anyone can author AR anywhere by speaking.
- What it is: Outdoors, a person says 'a dragon enjoying a campfire' and a phone AR app generates the 3D assets and arranges them in the real park or street, ready to be adjusted by hand.
- How it works: Offline outdoor scene-graph construction, a fast text-to-3D asset pipeline and LLM-based layout reasoning run in a mobile AR tool; a technical evaluation and a three-part user study (N=20).
- Specs: mobile AR · user study N=20
- Capability: Authoring accessibility, Situational reach
- Paper: https://arxiv.org/abs/2504.21360 (UIST 2025)
- Video: https://www.youtube.com/watch?v=G9mH1HKSPkg
- Images: https://nianticspatial.github.io/imaginatear/resources/social_card.png
- Project page: https://nianticspatial.github.io/imaginatear/

#### AI-Powered Talking Characters on Everyday Objects — Nozomu Iwai, Preferred Networks (2025-04-25)
- Type: Research demo · Timing: Turn-based · Access: Research only
- Input: Speech & audio, Passthrough & live surroundings → Output: Dialogue / text, Speech / voice, Virtual human (face / body)
- Idea: Grounds generated characters in real objects and their surroundings, so conversation refers to what is actually there.
- What it is: Through an AR headset or a phone, a kettle, a plant or a chair gets an animated face and a personality drawn from what it is, chats with you about the room and reacts when things around it change.
- How it works: Language, vision and speech models give each recognized object a personality and dialogue grounded in its function and in scene changes; a preliminary evaluation on HoloLens 2 and an Android phone.
- Capability: Behavioral plausibility, Reactivity
- Paper: https://doi.org/10.1145/3706599.3719978 (CHI 2025 Extended Abstracts)
- Video: https://www.youtube.com/watch?v=RkRc7TRDPDQ
- Project page: https://doi.org/10.1145/3706599.3719978

#### Sketch2Terrain — Tianyi Xiao (2025-04-25)
- Type: Research demo · Timing: Real-time streaming · Access: Research only
- Input: Sketch & gesture → Output: Mesh / 3D asset, 3D scene / world
- Idea: Real-time generation from sketches gives non-experts a way to externalize remembered landscapes, and gives researchers one uniform setup to collect that data.
- What it is: A person draws a few freehand 3D strokes in AR and a generative model turns them into a complete terrain with hills and valleys in real time.
- How it works: Freehand AR strokes condition a generative terrain model that outputs elevation meshes in real time; a between-subjects study (N=36) compared it with conventional sketch mapping.
- Specs: between-subjects study N=36
- Capability: Authoring accessibility, Temporal responsiveness, Experimental control
- Paper: https://doi.org/10.1145/3706598.3713467 (CHI 2025)
- Video: https://www.youtube.com/watch?v=DPvd_EmxzVg
- Project page: https://doi.org/10.1145/3706598.3713467

#### Figmin XR AI creation tools — Figmin XR (2024)
- Type: Product / app · Timing: Turn-based · Access: Product / app
- Input: Text prompt → Output: Mesh / 3D asset, Agent behaviour & actions
- Idea: A consumer headset app where generated assets and generated behaviour land directly in the space you are standing in.
- What it is: Inside the mixed-reality creation app Figmin XR, users generate 3D models from a text prompt (via Luma Genie in the built-in browser) and drop them into their room, and later had language models write scripts that make objects interactive.
- How it works: Text-to-3D results from Luma Genie are imported as scene objects, and LLMs (including GPT-5 in 2025) write code against Figmin XR's scripting API.
- Capability: Authoring accessibility
- Video: https://www.youtube.com/watch?v=PFY1mk4gzjs
- Project page: https://figmin.com

#### Dreamcrafter — Cyrus Vachha (2024-10-13)
- Type: Research demo · Timing: Turn-based · Access: Research only
- Input: Speech & audio, Text prompt → Output: Gaussian splats / radiance field, Mesh / 3D asset
- Idea: Proxies that stand in during high-latency generation keep immersive editing fluid even when the model is slow.
- What it is: A VR editor for captured scenes (NeRFs and Gaussian splats): add or restyle objects by voice or by direct manipulation, and keep working with quick previews while slower generations finish.
- How it works: A modular VR architecture plugs in generative 2D, 3D and radiance-field editing models, mixes natural-language and direct-manipulation control, and shows proxy representations during slow operations.
- Capability: Authoring accessibility, Perceptual realism
- Paper: https://arxiv.org/abs/2512.20129 (CHI 2025)
- Video: https://www.youtube.com/watch?v=47r0uMhrokE
- Project page: https://dream-crafter.github.io/

#### Thing2Reality — Erzhen Hu, Google (2024-10-09)
- Type: Research demo · Timing: Turn-based · Access: Research only
- Input: Image, Video → Output: Gaussian splats / radiance field, Image / panorama
- Idea: Turning shared 2D content into 3D on the spot makes remote discussion spatial: people can reference parts of an object, not just a picture of it.
- What it is: During an XR call, a participant grabs a 2D image or a physical object from the video feed and it materializes as a 3D object between everyone, which they can move, rotate and point at.
- How it works: Segmented 2D content is converted into conditioned multiview renderings and then 3D Gaussians with image-to-3D generation, and shared in a multi-user XR session; a user study measured discussion efficiency.
- Capability: Co-creation & agency, Temporal responsiveness
- Paper: https://arxiv.org/abs/2410.07119 (UIST 2025)
- Video: https://www.youtube.com/watch?v=sKrq77cOtC4
- Images: https://arxiv.org/html/2410.07119v1/teaserfigure.png
- Project page: https://arxiv.org/abs/2410.07119

#### Social Conjuring — Amina Kobenova, Microsoft (2024-09-30)
- Type: Research demo · Timing: Turn-based · Access: Research only
- Input: Text prompt → Output: 3D scene / world, Mesh / 3D asset
- Idea: Shows that prompting a world into existence becomes a social act: what gets generated depends on who else is in the room.
- What it is: Several people stand in the same virtual world and build and change it together at runtime by prompting an AI, which places and modifies objects while they talk and react to each other's requests.
- How it works: The Social Conjurer framework combines LLM-driven 3D scene generation with social, tool-based and spatial-reasoning interactions for multi-user real-time co-creation, evaluated in a preliminary user study (N=12).
- Specs: multi-user · preliminary study N=12
- Capability: Co-creation & agency, Authoring accessibility
- Paper: https://arxiv.org/abs/2410.00274 (arXiv 2024)
- Images: https://arxiv.org/html/2410.00274v2/images/teaser.png https://arxiv.org/html/2410.00274v2/images/scene_examples/zoo-cropped.png
- Project page: https://arxiv.org/abs/2410.00274

#### SpaceBlender — Nels Numan, Microsoft (2024-09-20)
- Type: Research demo · Timing: Pre-generated · Access: Research only
- Input: Image, Text prompt → Output: 3D scene / world
- Idea: Generating a meeting place from everyone's real context helps familiarity, but generated clutter can also pull attention away from the task.
- What it is: Each participant contributes photos of their own room, and SpaceBlender stitches them into one generated VR space where remote collaborators meet amid familiar surroundings.
- How it works: Depth estimation lifts 2D photos to meshes, which are aligned and joined by diffusion-based space completion guided by geometric priors and adaptive prompts; a within-subjects study (N=20, in pairs) compared it with a generic VR room and a scene-generation baseline.
- Specs: within-subjects study N=20
- Capability: Perceptual realism, Authoring accessibility
- Paper: https://arxiv.org/abs/2409.13926 (UIST 2024)
- Video: https://www.youtube.com/watch?v=2rTTyjNl-a0
- Images: https://arxiv.org/html/2409.13926v1/fig1-July24.png
- Project page: https://arxiv.org/abs/2409.13926

#### VRCopilot — Lei Zhang (2024-08-18)
- Type: Research demo · Timing: Turn-based · Access: Research only
- Input: Speech & audio, Sketch & gesture → Output: 3D scene / world, Mesh / 3D asset
- Idea: Finds that scaffolded creation (you draw a wireframe, AI fills it) keeps more sense of agency than fully automatic generation.
- What it is: Inside VR, a person furnishes a room together with generative models: they speak and point to request furniture, sketch wireframes the AI fills in, or let it lay out the whole scene.
- How it works: A mixed-initiative system integrates pre-trained 3D layout and object generators with multimodal speech-and-pointing input and wireframe intermediate representations; user studies compare manual, scaffolded and automatic creation.
- Capability: Authoring accessibility, Co-creation & agency
- Paper: https://arxiv.org/abs/2408.09382 (UIST 2024)
- Video: https://www.youtube.com/watch?v=95xd8oF3Rik
- Images: https://arxiv.org/html/2408.09382v1/Figures/teaser.png
- Project page: https://arxiv.org/abs/2408.09382

#### MagicItem — Ryutaro Kurai (2024-06-19)
- Type: Research demo · Timing: Turn-based · Access: Research only
- Input: Text prompt → Output: Agent behaviour & actions
- Idea: One of the first LLM behaviour-authoring tools tested with ordinary users of a live metaverse rather than lab participants.
- What it is: In the commercial social VR platform Cluster, users with no programming background describe what an object should do and an LLM writes the Cluster Script that makes it behave that way.
- How it works: An LLM is prompted with the Cluster Script API to generate object behaviours from natural language, integrated into the platform and evaluated online with 63 general users.
- Specs: online study with 63 platform users
- Capability: Authoring accessibility, Reactivity
- Paper: https://arxiv.org/abs/2406.13242 (IEEE Access 2025)
- Video: https://www.youtube.com/watch?v=ZKf5RkQkV_g
- Images: https://arxiv.org/html/2406.13242v1/teaser.png
- Project page: https://arxiv.org/abs/2406.13242

#### Video2MR — Keiichi Ihara, Ryo Suzuki (2024-05-28)
- Type: Research demo · Timing: Pre-generated · Access: Research only
- Input: Video → Output: Motion / animation, Virtual human (face / body)
- Idea: Any 2D video becomes an embodied demonstration you can walk around, a cheap source of situated instruction.
- What it is: Turns an online sports or exercise video into a mixed-reality coach: the person in the 2D video becomes a 3D avatar in your room, with highlighted posture differences, motion trails, speed control and repositioning.
- How it works: 3D human motion is extracted from monocular video and retargeted onto an avatar placed in mixed reality, with automatically generated visual augmentations.
- Capability: Situational reach, Authoring accessibility
- Paper: https://arxiv.org/abs/2405.18565 (IUI 2025)
- Video: https://www.youtube.com/watch?v=f1L-2US25PU
- Images: https://arxiv.org/html/2405.18565v1/figures/teaser.jpg
- Project page: https://ryosuzuki.org/video2mr

#### LLMR — Fernanda De La Torre, Microsoft (2023-09-21)
- Type: Research demo · Timing: Turn-based · Access: Research only
- Input: Text prompt, Speech & audio → Output: 3D scene / world, Agent behaviour & actions
- Idea: Makes the behaviour of an immersive world, not just its look, something a person can ask for in plain language.
- What it is: Type or say 'make a timer out of a rotating cube' or 'recolor the scene for a color-blind user' and LLMR writes, checks and runs the Unity code that changes the live mixed-reality world.
- How it works: An orchestration of GPT-4 modules for scene understanding, task planning, code building, self-debugging and memory runs inside Unity; the authors report a 4x lower average error rate than plain GPT-4 and a usability study (N=11).
- Specs: Unity · 4x lower error rate vs GPT-4 (reported) · N=11
- Capability: Authoring accessibility, Reactivity
- Paper: https://arxiv.org/abs/2309.12276 (CHI 2024)
- Video: https://www.youtube.com/watch?v=j44JJtp272k
- Images: https://arxiv.org/html/2309.12276v3/Figures/Final/teaser.png
- Project page: https://arxiv.org/abs/2309.12276

### Restyling reality live

Diffusion and video-to-video models repainting passthrough or camera views as you look.

#### Real-time AI style transfer on Spectacles — Alessio Grancini (2026-07-28)
- Type: Research demo · Timing: Real-time streaming · Access: Research only
- Input: Passthrough & live surroundings → Output: Interactive frame stream
- Idea: On see-through glasses, restyling has to decide what to augment and where, not just filter the whole frame.
- What it is: An experiment connects Snap Spectacles to Decart's real-time video model and projects the transformed camera feed back into the wearer's view at real-world scale, so the street appears restyled live.
- How it works: The Spectacles camera stream is sent over WebRTC to Decart's real-time video-to-video API and the returned frames are rendered at world scale in the lens; the prototype was built in a day with an agentic coding loop.
- Capability: Temporal responsiveness
- Video: https://x.com/alessiograncini/status/2082150582467387856
- Project page: https://x.com/alessiograncini/status/2082150582467387856

#### Body Oracle Translator — Danlin Huang, Botao 'Amber' Hu, Reality Design Lab (2026-03)
- Type: Experience / artwork · Timing: Real-time streaming
- Input: Body, face & gaze tracking → Output: Image / panorama
- Idea: Restyles people rather than rooms: the lens rewrites bodies as an alternative written language, an 'alternative present' to share.
- What it is: Looking through a handheld mixed-reality lens, people see each other's postures and movements translated in real time into speculative AI-generated characters inspired by Chinese oracle-bone script.
- How it works: Pose tracking feeds an image-generation model trained to map body skeletons to oracle-bone-style glyphs (building on Body Oracle), and the glyphs are overlaid on people in the handheld MR view.
- Capability: Reactivity, Co-creation & agency
- Recognition: IEEE VR 2026 XR Gallery
- Video: https://www.youtube.com/watch?v=GXeLSfZnXAQ
- Project page: https://reality.design/project/body-oracle

#### Roomify — Xueyang Wang (2026-03-05)
- Type: Research demo · Timing: Pre-generated · Access: Research only
- Input: Text prompt, Passthrough & live surroundings → Output: 3D scene / world
- Idea: Keeping the room's functional layout while changing its style offers presence without losing spatial awareness.
- What it is: Turns your physical room into a themed virtual environment, such as a forest cabin or a spaceship, in which every sofa, table and wall stays where it really is, and lets designers edit it in MR and preview it in VR.
- How it works: In-situ 3D scene understanding, AI spatial reasoning and style-aware generation replace each furnishing with a themed counterpart of matching geometry and function; studies with 18 VR users and 8 design professionals.
- Specs: presence +63% vs passthrough, +26% vs fully virtual (reported, N=18)
- Capability: Perceptual realism, Situation diversity
- Paper: https://arxiv.org/abs/2603.04917 (CHI 2026)
- Video: https://www.youtube.com/watch?v=zPEOMXafHVA
- Images: https://arxiv.org/html/2603.04917v1/teaser.png
- Project page: https://arxiv.org/abs/2603.04917

#### Real-time AI video restyling an XR room — Stijn Spanhove (2025-10-21)
- Type: Research demo · Timing: Real-time streaming · Access: Research only
- Input: Text prompt, Passthrough & live surroundings → Output: Interactive frame stream
- Idea: Shows a comfort constraint of restyling live: the generated view must change slowly enough not to fight the wearer's motion.
- What it is: A room seen in XR is repainted by a live video model, first as a 'modern, Ikea style room', then as an 'industrial loft', with updates synced slowly to avoid dizziness.
- How it works: Rendered XR views are passed through a real-time video-to-video model and the restyled result is blended back into the scene at a reduced update rate.
- Capability: Temporal responsiveness, Situation diversity
- Video: https://x.com/stspanho/status/1980751025930661934
- Project page: https://x.com/stspanho/status/1980751025930661934

#### Decart XR — Decart, Roberto Coviello (2025-10-04)
- Type: Open-source tool · Timing: Real-time streaming · Access: Open weights / code, Product / app
- Input: Speech & audio, Passthrough & live surroundings → Output: Interactive frame stream
- Idea: Real-time video-to-video turns any room into a prompt-selected world, but what you see stops matching what you touch.
- What it is: On Meta Quest, the wearer speaks a prompt and watches the passthrough view of their own room transformed live by a real-time video model; the app is free on SideQuest and open source.
- How it works: Passthrough camera frames from QuestCameraKit are streamed to Decart's real-time video-to-video model, likely MirageLSD over WebRTC, and the restyled frames are rendered back into the headset.
- Capability: Temporal responsiveness, Situation diversity
- Video: https://x.com/DecartAI/status/1974534910623859128
- Project page: https://github.com/DecartAI/Decart-XR
- API docs: https://decart.ai
- Code: https://github.com/DecartAI/Decart-XR

#### MR + Diffusion passthrough prototype — Hugues Bruyère (2025-03-16)
- Type: Research demo · Timing: Real-time streaming · Access: Research only
- Input: Passthrough & live surroundings, Text prompt → Output: Image / panorama
- Idea: One of the first diffusion-on-passthrough demos after Meta opened the Passthrough Camera API in 2025.
- What it is: A Quest mixed-reality prototype reads the passthrough camera and replaces parts of the room with diffusion-generated imagery that stays in place as the wearer looks around.
- How it works: Frames from Meta's Passthrough Camera API are sent to an image diffusion model and the results are re-projected onto the matching surfaces of the room.
- Capability: Temporal responsiveness, Perceptual realism
- Video: https://x.com/smallfly/status/1901403937321750862
- Project page: https://x.com/smallfly/status/1901403937321750862

#### Real-time on-device generative AR model — Snap Inc. (2024-06-18)
- Type: Model · Timing: Real-time streaming · Access: Waitlist / early access
- Input: Text prompt, Passthrough & live surroundings → Output: Interactive frame stream
- Idea: Moves restyling of the live camera view from the cloud onto the device that the person is holding.
- What it is: Snap previewed an image diffusion model small enough to run on a smartphone and fast enough to re-render the camera view live from a text prompt, meant for AR Lenses, alongside Lens Studio 5.0's generative tools.
- How it works: A compact text-conditioned image diffusion model optimized for on-device inference re-renders camera frames in real time; Snap said Lenses using it would reach users first and creators later.
- Capability: Temporal responsiveness, Authoring accessibility
- Recognition: AWE USA 2024
- Video: https://www.youtube.com/watch?v=zqHNq2ML_5Q
- Project page: https://techcrunch.com/2024/06/18/snap-previews-its-real-time-image-model-that-can-generate-ar-experiences/

#### DreamSpace — Bangbang Yang (2023-10-19)
- Type: Research demo · Timing: Pre-generated · Access: Research only
- Input: Text prompt, Multi-view capture / scan → Output: 3D scene / world, Image / panorama
- Idea: Restyles a real room's geometry instead of replacing it, so the generated world keeps the layout your body already knows.
- What it is: Type a style such as 'Van Gogh' or 'cyberpunk' and a scanned room is re-textured end to end, with coherent textures across walls, floor and furniture that you can walk through in a VR headset.
- How it works: A stylized 360-degree panorama is generated from the room's centre with coarse-to-fine diffusion and dual texture alignment, then propagated to the rest of the mesh by inpainting and an implicit imitation network for occluded parts.
- Capability: Perceptual realism, Situation diversity
- Paper: https://arxiv.org/abs/2310.13119 (IEEE VR 2024)
- Video: https://www.youtube.com/watch?v=Ni5kXdj7cfw
- Project page: https://ybbbbt.com/publication/dreamspace/

### Generative film, theatre & enactment

Stories, films and scenarios that are generated or extended around the viewer.

#### Generative Enactments — Botao 'Amber' Hu, Reality Design Lab (2026)
- Type: Research demo · Timing: Turn-based · Access: Research only
- Input: Text prompt → Output: Flat video
- Idea: Uses fast, cheap video generation to let people rehearse situations that are unsafe, unethical or not yet possible to stage, with a configuration that researchers can specify and compare.
- What it is: Participants act inside a scenario and receive AI-generated first-person video of the consequences, either after a short wait or streamed reactively, so they can watch a situation unfold in response to what they do.
- How it works: A configuration form specifies how researchers, participants and AI systems propose, generate, contest and revise pathways; illustrated with domestic-robot attention (adversarial, turn-based), bystander intervention (choice-based) and trainee-teacher rehearsal (reactive streaming), with implementation and pilot evidence.
- Capability: Situational reach, Reactivity, Experimental control
- Images: https://images.spr.so/cdn-cgi/imagedelivery/j42No7y-dcokJuNgXeA0ig/e24f1e2a-3433-4a17-a6d6-3cdd234543f0/robot-archetype-06-care-or-control/public
- Project page: https://amber.botao.hu/project/generative-enactments

#### CinemaWorld — Keiichi Ihara, Ryo Suzuki (2026-03-09)
- Type: Research demo · Timing: Pre-generated · Access: Research only
- Input: Video, Passthrough & live surroundings → Output: 3D scene / world
- Idea: Extends a fixed film into the viewer's physical space automatically, without hand-authored AR for each scene.
- What it is: While a 2D film plays, the viewer's own room on a Meta Quest 3 fills with generated 3D content synchronized to the scene: particle effects, surrounding objects, textures, character-driven effects and lighting.
- How it works: Films are preprocessed with multimodal LLMs to extract key features, generative AI produces dynamic 3D augmentations that are embedded spatially in the room; evaluated with 100 clips, a user study (N=12) and interviews with film creators (N=8).
- Specs: Meta Quest 3 · 100 clips · N=12 · 8 experts
- Capability: Perceptual realism, Authoring accessibility
- Paper: https://arxiv.org/abs/2603.08060 (UIST 2026)
- Video: https://ryosuzuki.org/static/video/cinemaworld.mp4
- Images: https://arxiv.org/html/2603.08060v1/figures/teaser_ver1.1.jpg
- Project page: https://ryosuzuki.org/cinemaworld

#### Step inside an AI-generated movie scene — Stijn Spanhove (2025-12-29)
- Type: Research demo · Timing: Pre-generated · Access: Research only
- Input: Video, Image → Output: Gaussian splats / radiance field, Motion / animation
- Idea: Assembles a walkable film scene entirely from off-the-shelf generators, hinting at films that become explorable situations.
- What it is: A browser WebXR proof of concept, recorded on Apple Vision Pro, lets the viewer enter the Dojo from The Matrix, teleport around generated characters in motion and ask questions to an AI agent inside the scene.
- How it works: Environment generated as a Gaussian splat from source footage with World Labs, characters converted from images to rigged 3D models with Tripo, motion from AI motion capture, and an embedded AI agent answering questions.
- Capability: Perceptual realism, Authoring accessibility
- Video: https://x.com/stspanho/status/2005626245166313514
- Project page: https://x.com/stspanho/status/2005626245166313514

#### Life Stories × World Labs — Liquid City (2025-11)
- Type: Experience / artwork · Timing: Pre-generated
- Input: Speech & audio → Output: Gaussian splats / radiance field, Image / panorama
- Idea: A spoken memory becomes a place you can walk into, a route from oral history to an immersive situation.
- What it is: A true memory collected by Liquid City's AI interviewer is turned into descriptions, then images, and finally an explorable 3D Gaussian-splat world made with World Labs' Marble, such as 'Night Lake'.
- How it works: Pipeline: AI interview, LLM scene description, image generation, then World Labs Marble image-to-world generation into Gaussian splats.
- Capability: Situational reach, Authoring accessibility
- Video: https://www.youtube.com/watch?v=w5fp-otQhQU
- Images: https://lifestory.liquid.city/img/life-stories-banner.png https://lifestory.liquid.city/img/lifestories-demo.png
- Project page: https://lifestory.liquid.city/

#### Storycaster — Naisha Agarwal, Microsoft (2025-10-26)
- Type: Research demo · Timing: Turn-based · Access: Research only
- Input: Speech & audio, Passthrough & live surroundings → Output: Image / panorama, Sound, music & spatial audio, Dialogue / text
- Idea: A generative CAVE keeps people aware of the real room and of each other while the story around them changes.
- What it is: A projection room becomes a story space: a narrator agent guides participants, and by voice they co-create scenes that are projected on the walls with generated imagery, ambient audio and dialogue, while real objects in the room can turn into their story counterparts.
- How it works: Live camera feeds and cylindrical projection augment the walls; image, audio and dialogue generators, object-level editing of physical items and an LLM narrator respond to voice commands; a study with 13 participants.
- Specs: room-scale projection · study n=13
- Capability: Co-creation & agency, Perceptual realism
- Paper: https://arxiv.org/abs/2510.22857 (CHI 2026)
- Video: https://www.youtube.com/watch?v=ckCtta27LJQ
- Images: https://arxiv.org/html/2510.22857v2/Figure1.png
- Project page: https://arxiv.org/abs/2510.22857

#### Generative-AI earthquake rehearsal overlaid on a real room — Tomoki Itamiya (2025-04-23)
- Type: Research demo · Timing: Pre-generated · Access: Research only
- Input: Image → Output: 360° / stereo video
- Idea: Stages a dangerous event inside the very room where people would have to respond, with adjustable severity and replay.
- What it is: From a single photo of a real room, a generative video model creates an earthquake scenario with falling ceiling panels; it is converted to spatial video and overlaid on the same room in Apple Vision Pro, with rewind and slow motion.
- How it works: Image-to-video generation from a photo of the room, with the degree of ceiling-panel collapse adjusted, then conversion to stereo spatial video aligned with the physical room.
- Capability: Situational reach, Experimental control
- Video: https://x.com/t_itamiya/status/1914896389152133364
- Project page: https://x.com/t_itamiya/status/1914896389152133364

#### Tulpamancer — Light in the Head (2023-08)
- Type: Experience / artwork · Timing: Pre-generated
- Input: Text prompt → Output: 3D scene / world, Dialogue / text
- Idea: A personal VR journey generated from one person's answers, made once and then discarded.
- What it is: Visitors answer questions about their lives at an old computer terminal, then put on a VR headset and are led by their 'tulpa' through uniquely generated scenes about their past and possible futures; each work is deleted after viewing.
- How it works: A machine-learning pipeline, likely language and image generation, turns each participant's answers into a sequence of virtual scenes and narration before the headset session.
- Capability: Adaptation, Situation diversity
- Recognition: Venice Immersive 2023
- Video: https://www.youtube.com/watch?v=nBYuZiTI8gA
- Images: https://static.labiennale.org/files/styles/seo_thumbnail/public/cinema/2023/Schede_film/970x647/Ve_Immersive/dacosta-niederhauser.jpg?itok=FJNGWYE9
- Project page: https://www.labiennale.org/en/cinema/2023/venice-immersive/tulpamancer

#### Agence — Transitional Forms (2020)
- Type: Experience / artwork · Timing: Real-time streaming
- Input: Keyboard & controller actions → Output: Agent behaviour & actions
- Idea: An early precursor: a story whose characters are trained agents rather than animation, so viewer interference has consequences.
- What it is: A short 'dynamic film' about small creatures on a tiny planet whose behaviour is driven by AI agents; viewers can watch, or reach in and change their world, and the story plays out differently each time.
- How it works: Characters run reinforcement-learning policies in real time within a game-engine film, and viewer interactions change their environment (co-produced with the National Film Board of Canada).
- Capability: Behavioral plausibility, Co-creation & agency
- Recognition: BFI London Film Festival 2020
- Video: https://vimeo.com/426287032
- Project page: https://www.transforms.ai/agence

### Generative features in XR platforms

What headsets and glasses ship: spatial scenes, captured spaces, generative lenses, AI world editors.

#### Android XR auto-spatialization — Google, Samsung Electronics (2026-04-07)
- Type: Product / app · Timing: Real-time streaming · Access: Product / app
- Input: Video, Image → Output: 360° / stereo video, Image / panorama
- Idea: System-level 2D-to-3D conversion means every flat source becomes stereoscopic content in a headset, generated rather than captured.
- What it is: An experimental Android XR feature on the Samsung Galaxy XR headset that turns almost any app, game, website, image or video, including YouTube videos and 2D games, into a 3D experience at the push of a button.
- How it works: Likely per-frame monocular depth estimation with stereo view synthesis at the system compositor; enabled from the Labs tab in Settings.
- Capability: Perceptual realism
- Video: https://storage.googleapis.com/gweb-uniblog-publish-prod/original_videos/Auto_Spatialization.mp4
- Images: https://storage.googleapis.com/gweb-uniblog-publish-prod/images/Final_Hero_Image.width-1300.png
- Project page: https://blog.google/products-and-platforms/platforms/android/android-xr-immersive-features-update-april-2026/

#### XR Blocks — Google (2025-09-29)
- Type: Open-source tool · Timing: Turn-based · Access: Open weights / code
- Input: Text prompt, Speech & audio, Passthrough & live surroundings → Output: Agent behaviour & actions
- Idea: Lowers the cost of wiring perception, rendering and generative models together, the step most AI + XR prototypes stall on.
- What it is: An open-source WebXR framework from Google with plug-and-play modules for user, world, peers, interface, context and agents, so AI + XR prototypes (Gemini assistants, scene understanding) run in Chrome and on Android XR headsets.
- How it works: A modular architecture built on WebXR, three.js, TensorFlow and Gemini, with templates, samples and demos; the foundation for Vibe Coding XR.
- Capability: Authoring accessibility, Experimental control
- Paper: https://arxiv.org/abs/2509.25504 (arXiv 2025)
- Video: https://www.youtube.com/watch?v=75QJHTsAoB8
- Images: https://arxiv.org/html/2509.25504v1/teaser.png
- Project page: https://xrblocks.github.io/
- API docs: https://xrblocks.github.io/docs/
- Code: https://github.com/google/xrblocks

#### Meta Horizon Studio generative AI tools — Meta (2025-09-17)
- Type: Platform / API · Timing: Turn-based · Access: Product / app, Waitlist / early access
- Input: Text prompt → Output: Mesh / 3D asset, Image / panorama, Sound, music & spatial audio
- Idea: Puts prompt-to-asset and prompt-to-code generation in the main authoring tool of a large social VR platform.
- What it is: Meta's world-building editor for Horizon lets creators generate meshes, textures, TypeScript, audio and skyboxes from text prompts on top of the new Horizon Engine, with an agentic assistant announced to combine the tools.
- How it works: Text-to-3D, texture, code, audio and skybox generators integrated into the editor, with the Horizon Engine rendering the results; in September 2026 Meta repositioned Horizon Studio as a browser tool for agentic creation of mobile games, in early access.
- Capability: Authoring accessibility
- Video: https://www.youtube.com/watch?v=viXoK-MJRls
- Project page: https://www.meta.com/blog/connect-2025-day-one-keynote-ai-glasses-ray-ban-display-neural-band-metaverse-news/
- API docs: https://developers.meta.com/horizon-worlds/

#### Spectacles AI release with Snap3D — Snap Inc. (2025-06-10)
- Type: Platform / API · Timing: Turn-based · Access: Public API, Product / app
- Input: Text prompt, Speech & audio → Output: Mesh / 3D asset
- Idea: Makes text-to-3D a standard building block of AR glasses apps, so a Lens can create objects the developer never modelled.
- What it is: A Spectacles OS release adds the Snap3D API, which generates 3D objects on demand inside Lenses, together with OpenAI and Gemini integrations and better speech recognition for multimodal AI Lenses.
- How it works: Cloud text-to-3D generation exposed as a Lens Studio API and called at runtime from Spectacles Lenses, alongside hosted LLM and ASR services.
- Capability: Authoring accessibility
- Video: https://www.youtube.com/watch?v=qpi1JTnPwgs
- Project page: https://investor.snap.com/news/news-details/2025/Snap-to-Launch-New-Lightweight-Immersive-Specs-in-2026/default.aspx
- API docs: https://developers.snap.com/spectacles

#### visionOS 2 spatial photos from 2D images — Apple (2024-06-10)
- Type: Product / app · Timing: Turn-based · Access: Product / app
- Input: Image → Output: Image / panorama
- Idea: Made generated depth a default way to revisit personal memories in a headset; visionOS 26 later extended it to Spatial Scenes.
- What it is: In visionOS 2, Apple Vision Pro users can turn any 2D photo in their library into a spatial photo with depth that comes to life in the headset.
- How it works: Apple says visionOS uses advanced machine learning to transform a 2D image into a stereo spatial photo, likely monocular depth estimation plus view synthesis with inpainting.
- Capability: Perceptual realism
- Video: https://www.apple.com/newsroom/videos/videos-2024/autoplay/2024/visionos-2-spatial-photos/large_2x.mp4
- Images: https://www.apple.com/newsroom/images/2024/06/visionos-2-brings-new-spatial-computing-experiences-to-apple-vision-pro/tile/Apple-WWDC24-visionOS-2-spatial-photos-240610-lp.jpg.og.jpg?202608191902
- Project page: https://www.apple.com/newsroom/2024/06/visionos-2-brings-new-spatial-computing-experiences-to-apple-vision-pro/

## Immersive Behavioral Research & Training

Where the situations are used: VR experiments in social psychology and criminology, simulation training with virtual humans and patients, clinical VR, presence theory, and the first studies that bring generative AI into immersive research.

### Presence, plausibility & method

Why people respond to virtual situations, and how to design and validate them: Slater, Steuer, Blascovich, Brunswik…

#### Confusing virtual reality with reality – An experimental study — Michael Wiesing, Mel Slater (2025-05-13)
- Type: Behavioral study · Timing: Scripted / rule-based
- Input: Body, face & gaze tracking, Speech & audio → Output: Authored VR scenario, Virtual human (face / body)
- Idea: When a virtual situation matches physical reality closely, people carry virtual facts into the real world, a safety and ethics issue that grows as generated worlds become photoreal.
- What it is: Forty-nine participants interacted with a virtual experimenter in a virtual copy of a real room. 20% sat on a virtual chair without checking for a real one, and a week later, in the real room, 45% expected a tablet the virtual experimenter had put in a drawer to be there.
- How it works: Experiment with a virtual experimenter, behavioral measures (sitting, object expectations a week later) and implicit-attitude tests, analysed with Bayesian statistics.
- Specs: N=49 · follow-up after 1 week
- Capability: Perceptual realism, Behavioral plausibility
- Paper: https://doi.org/10.1016/j.isci.2025.112655 (iScience (2025))
- Video: https://www.youtube.com/watch?v=pM279hO8n5s

#### The Cognitive Affective Model of Immersive Learning (CAMIL): a Theoretical Research-Based Model of Learning in Immersive Virtual Reality — Guido Makransky (2021)
- Type: Paper / review
- Input: Body, face & gaze tracking, Keyboard & controller actions → Output: Authored VR scenario
- Idea: More presence is not automatically more learning: a generated training scenario helps only when its realism and interactivity serve the learning goal instead of overloading the learner.
- What it is: Model that explains learning in immersive VR through two affordances, presence and agency, which act on learning through six affective and cognitive factors such as interest, self-efficacy, embodiment and cognitive load.
- How it works: Theoretical synthesis by Makransky and Petersen of empirical work on immersive learning into a causal model with testable predictions.
- Capability: Perceptual realism, Co-creation & agency
- Paper: https://doi.org/10.1007/s10648-020-09586-2 (Educational Psychology Review 33 (2021))

#### Why and how to use virtual reality to study human social interaction: The challenges of exploring a new research landscape — Sylvia Xueni Pan (2018)
- Type: Paper / review
- Input: Body, face & gaze tracking, Speech & audio → Output: Authored VR scenario, Virtual human (face / body)
- Idea: Virtual partners buy precise, repeatable social stimuli at the cost of two-way realism, the gap LLM-driven characters now try to close.
- What it is: Review in the British Journal of Psychology on using VR to study face-to-face social interaction: what virtual characters let researchers control, and what is lost when the partner is not a real person.
- How it works: Narrative review with Antonia Hamilton of VR social-interaction paradigms, covering character realism, interaction loops and validity.
- Capability: Experimental control, Behavioral plausibility
- Paper: https://doi.org/10.1111/bjop.12290 (British Journal of Psychology (2018))
- Video: https://www.youtube.com/watch?v=rh6e-mW_y5E

#### Enhancing Our Lives with Immersive Virtual Reality — Mel Slater (2016)
- Type: Paper / review
- Input: Body, face & gaze tracking → Output: Authored VR scenario, Virtual human (face / body)
- Idea: VR's value lies in situations that are impossible, dangerous or unethical in reality, including inhabiting another body, which generation could make much cheaper to build.
- What it is: Long review in Frontiers in Robotics and AI that surveys how immersive VR has been used in neuroscience, psychology, clinical therapy, training, education and entertainment, sets out its distinctive affordances and adds ethical cautions.
- How it works: Narrative review with Maria V. Sanchez-Vives organized around presence, body ownership and application areas.
- Capability: Situational reach, Perceptual realism
- Paper: https://doi.org/10.3389/frobt.2016.00074 (Frontiers in Robotics and AI 3 (2016))

#### Place illusion and plausibility can lead to realistic behaviour in immersive virtual environments — Mel Slater (2009)
- Type: Paper / review
- Input: Body, face & gaze tracking → Output: Authored VR scenario
- Idea: Rendering quality buys place illusion; plausibility comes from credible events that respond to you, which is what generative agents and world models have to supply.
- What it is: Theory paper that splits presence into place illusion (the sense of being there, set by sensorimotor contingencies) and plausibility illusion (the sense that what happens is really happening), and argues that the two together produce realistic behavior.
- How it works: Conceptual analysis drawing on earlier presence experiments, defining immersion as the set of valid sensorimotor actions a system supports.
- Capability: Perceptual realism, Behavioral plausibility
- Paper: https://doi.org/10.1098/rstb.2009.0138 (Philosophical Transactions of the Royal Society B (2009))
- Video: https://www.youtube.com/watch?v=WSLyfBscA9E

#### Immersive Virtual Environment Technology as a Methodological Tool for Social Psychology — Jim Blascovich (2002)
- Type: Paper / review
- Input: Body, face & gaze tracking → Output: Authored VR scenario, Virtual human (face / body)
- Idea: The founding claim of the field: VR eases the trade-off between experimental control and realism, and generated situations keep the method only if they keep that control.
- What it is: Target article in Psychological Inquiry proposing immersive virtual environments as a social-psychology method: experimenters can hold a realistic situation constant across participants, replicate it exactly, and use virtual humans in place of confederates.
- How it works: Conceptual target article reviewing early immersive-VR studies and the method's advantages and limits, followed by peer commentaries in the same issue.
- Capability: Experimental control, Situational reach
- Paper: https://doi.org/10.1207/S15327965PLI1302_01 (Psychological Inquiry 13(2))

#### Defining Virtual Reality: Dimensions Determining Telepresence — Jonathan Steuer (1992)
- Type: Paper / review
- Input:  → Output: Authored VR scenario
- Idea: Vividness and interactivity are still the two axes generative systems are judged on: how rich the generated world is, and how fast and how widely it answers back.
- What it is: Paper in the Journal of Communication that defines virtual reality by the experience of telepresence rather than by hardware, and names two technology variables that determine it: vividness (breadth and depth of sensory information) and interactivity (speed, range and mapping of user control).
- How it works: Conceptual paper that classifies media technologies along the vividness and interactivity dimensions.
- Capability: Perceptual realism, Reactivity
- Paper: https://doi.org/10.1111/j.1460-2466.1992.tb00812.x (Journal of Communication 42(4))

#### Representative design and probabilistic theory in a functional psychology — Egon Brunswik (1955)
- Type: Paper / review
- Input:  → Output: Authored VR scenario
- Idea: Representative design is the methodological case for generative situations: produce many ecologically sampled variants of a scene instead of one hand-built version.
- What it is: Classic Psychological Review paper arguing that psychology should sample stimulus situations from the environments people actually live in, as carefully as it samples participants, instead of isolating single variables in artificial set-ups.
- How it works: Theoretical argument within Brunswik's probabilistic functionalism (the lens model), contrasting systematic and representative experimental designs.
- Capability: Situation diversity, Experimental control
- Paper: https://doi.org/10.1037/h0047470 (Psychological Review 62(3))

### VR experiments in social psychology

Obedience, bystanders, embodiment and social interaction studied in immersive situations.

#### An Embodied Perspective as a Victim of Sexual Harassment in Virtual Reality Reduces Action Conformity in a Later Milgram Obedience Scenario — Solène Neyret, Mel Slater (2020)
- Type: Behavioral study · Timing: Scripted / rule-based
- Input: Body, face & gaze tracking → Output: Authored VR scenario, Virtual human (face / body)
- Idea: Situations can be chained: one embodied experience changes behavior in the next, so a generated sequence of scenes is itself an experimental manipulation.
- What it is: Sixty men saw a group of men sexually harass a woman in a virtual bar, either only as one of the group or also from the woman's body; those who had been embodied as the victim later conformed less with the group in a Milgram-style scenario.
- How it works: Three groups of 20 (group member only, also embodied as the woman, empty-bar control) followed by a virtual Milgram task under group pressure.
- Specs: N=60 (3 × 20)
- Capability: Situational reach, Experimental control
- Paper: https://doi.org/10.1038/s41598-020-62932-w (Scientific Reports 10 (2020))
- Video: https://www.youtube.com/watch?v=D6QcTSB6_t0

#### Building long-term empathy: A large-scale comparison of traditional and virtual reality perspective-taking — Fernanda Herrera, Jeremy Bailenson (2018)
- Type: Behavioral study · Timing: Scripted / rule-based
- Input: Body, face & gaze tracking, Keyboard & controller actions → Output: Authored VR scenario
- Idea: Embodied perspective-taking can outlast the session; long follow-ups, not post-session ratings, are the right test for a generated empathy scenario.
- What it is: Two experiments compared 'Becoming Homeless', a VR experience of losing one's job and home, with traditional perspective-taking; over eight weeks VR participants held more positive, longer-lasting attitudes toward homeless people and were more likely to sign a petition supporting affordable housing.
- How it works: Large-sample experiments comparing VR, narrative perspective-taking and control conditions (and desktop vs. headset in Study 2), with attitude scales and a petition-signing behavioral measure over eight weeks.
- Specs: follow-up over 8 weeks
- Capability: Situational reach, Experimental control
- Paper: https://doi.org/10.1371/journal.pone.0204494 (PLOS ONE 13(10))
- Video: https://www.youtube.com/watch?v=OK2yJIcAhDE

#### Participant concerns for the Learner in a Virtual Reality replication of the Milgram obedience study — Mar Gonzalez-Franco, Mel Slater (2018)
- Type: Behavioral study · Timing: Scripted / rule-based
- Input: Speech & audio, Body, face & gaze tracking → Output: Authored VR scenario, Virtual human (face / body)
- Idea: Logging fine-grained behavior inside a virtual replication can test theories, here the 'agentic state', that the original paradigm could only argue about.
- What it is: Forty participants went through a VR version of the Milgram paradigm; compared with 20 controls, they tried to help the virtual Learner by stressing the correct word when reading the test items, a sign of concern for the victim rather than pure obedience.
- How it works: VR replication with acoustic analysis of how participants read the word pairs, compared with a control group not taken through the simulation.
- Specs: N=40 VR + 20 controls
- Capability: Behavioral plausibility, Experimental control
- Paper: https://doi.org/10.1371/journal.pone.0209704 (PLOS ONE 13(12))
- Video: https://www.youtube.com/watch?v=83zBvG1e7uA

#### Bystander Responses to a Violent Incident in an Immersive Virtual Environment — Mel Slater (2013)
- Type: Behavioral study · Timing: Scripted / rule-based
- Input: Body, face & gaze tracking, Speech & audio → Output: Authored VR scenario, Virtual human (face / body)
- Idea: Violence that cannot be staged becomes a controlled 2x2 experiment, the template for generating many variants of a dangerous social scene.
- What it is: Forty male Arsenal supporters watched an argument in a virtual bar escalate into violence; they intervened more often when the victim was a fellow Arsenal supporter, supporting a social-identity account of bystander behavior.
- How it works: Two-factor between-groups design (victim in-group vs. out-group x victim looks or does not look at the participant) with life-size virtual characters; interventions coded from recordings.
- Specs: N=40 · 2×2 between-groups
- Capability: Situational reach, Behavioral plausibility
- Paper: https://doi.org/10.1371/journal.pone.0052766 (PLoS ONE 8(1): e52766)
- Video: https://www.youtube.com/watch?v=m6kBQk0DCFM

#### Putting yourself in the skin of a black avatar reduces implicit racial bias — Tabitha Peck, Mel Slater (2013)
- Type: Behavioral study · Timing: Scripted / rule-based
- Input: Body, face & gaze tracking → Output: Virtual human (face / body), Authored VR scenario
- Idea: Full-body ownership of a different identity measurably shifts attitudes, a strong and ethically loaded manipulation for any generated-avatar study.
- What it is: Light-skinned participants embodied in a dark-skinned virtual body that moved with them showed lower implicit racial bias afterwards than participants in the other body conditions.
- How it works: Between-groups embodiment experiment with full-body motion capture and a virtual mirror; Implicit Association Test before and after exposure.
- Capability: Experimental control, Situational reach
- Paper: https://doi.org/10.1016/j.concog.2013.04.016 (Consciousness and Cognition 22(3))
- Video: https://www.youtube.com/watch?v=HliN3iOX090

#### Increasing Saving Behavior Through Age-Progressed Renderings of the Future Self — Hal Hershfield, Jeremy Bailenson (2011)
- Type: Behavioral study · Timing: Scripted / rule-based
- Input: Body, face & gaze tracking → Output: Virtual human (face / body), Authored VR scenario
- Idea: A generated self from another point in time can shift a real economic decision, an early case of synthetic faces used as a behavioral intervention.
- What it is: Participants who met an age-progressed avatar of themselves in a virtual mirror, and in later studies on screen, put more money into a hypothetical retirement account than those who saw their current-age avatar.
- How it works: Series of experiments with Stanford VHIL using age-morphed 3D avatars, measuring hypothetical savings allocations.
- Capability: Situational reach, Experimental control
- Paper: https://doi.org/10.1509/jmkr.48.spl.s23 (Journal of Marketing Research 48 (SPL))
- Video: https://www.youtube.com/watch?v=ixwValjzqRg

#### The Proteus Effect: The Effect of Transformed Self-Representation on Behavior — Nick Yee, Jeremy Bailenson (2007)
- Type: Behavioral study · Timing: Scripted / rule-based
- Input: Body, face & gaze tracking → Output: Virtual human (face / body), Authored VR scenario
- Idea: The body you are given is an experimental variable: generated avatars change behavior, not just appearance.
- What it is: Two VR experiments: participants given more attractive avatars walked closer to a confederate and disclosed more, and participants given taller avatars behaved more confidently in a negotiation, independent of how others saw them.
- How it works: Between-subjects head-mounted-display studies manipulating avatar attractiveness (Study 1) and height (Study 2), measuring interpersonal distance, self-disclosure and negotiation outcomes.
- Capability: Experimental control, Perceptual realism
- Paper: https://doi.org/10.1111/j.1468-2958.2007.00299.x (Human Communication Research 33(3))
- Video: https://www.youtube.com/watch?v=nuOphOwjIDM

#### A Virtual Reprise of the Stanley Milgram Obedience Experiments — Mel Slater (2006)
- Type: Behavioral study · Timing: Scripted / rule-based
- Input: Body, face & gaze tracking, Speech & audio → Output: Authored VR scenario, Virtual human (face / body)
- Idea: Proof that people respond to extreme virtual social situations as if they were real, which makes ethically impossible paradigms studiable and means generated situations need ethical review too.
- What it is: Participants gave word-association tests to a female virtual Learner and administered 'shocks' for wrong answers while she protested; those who could see and hear her showed stress responses and some withdrew, although everyone knew she was not real.
- How it works: Between-groups experiment (Learner seen and heard vs. text-only interaction) in a CAVE-like projection system, with skin conductance, heart rate and behavioral measures, following Milgram's procedure.
- Capability: Situational reach, Experimental control
- Paper: https://doi.org/10.1371/journal.pone.0000039 (PLoS ONE 1(1): e39)
- Video: https://www.youtube.com/watch?v=RjUNg3pkEag

#### An Experiment on Public Speaking Anxiety in Response to Three Different Types of Virtual Audience — David-Paul Pertaub, Mel Slater (2002)
- Type: Behavioral study · Timing: Scripted / rule-based
- Input: Speech & audio, Body, face & gaze tracking → Output: Authored VR scenario, Virtual human (face / body)
- Idea: Even low-fidelity virtual characters evoke social threat when their behavior signals judgement, the basis of every virtual-audience trainer since.
- What it is: People gave five-minute talks to an audience of eight virtual men that stayed neutral, behaved warmly, or showed boredom and hostility; the negative audience produced anxiety even though speakers knew the audience was virtual.
- How it works: Between-groups experiment (neutral, positive, negative audience) with self-reported anxiety and speaker-confidence measures, run at University College London.
- Specs: 5-min talk · 8 virtual audience members · 3 conditions
- Capability: Behavioral plausibility, Experimental control
- Paper: https://doi.org/10.1162/105474602317343668 (Presence: Teleoperators and Virtual Environments 11(1))
- Video: https://www.youtube.com/watch?v=rqvdb4gttyU

### Criminology & exceptional situations

Burglary, aggression, threat and emergencies: situations that cannot be staged for real.

#### Using Virtual Reality to Examine Officer Decision-Making in Police Co-Response Interactions — Connor Powelson (2025-07-21)
- Type: Behavioral study · Timing: Scripted / rule-based
- Input: Body, face & gaze tracking, Speech & audio → Output: Authored VR scenario
- Idea: VR plus think-aloud turns a rare, high-risk encounter into inspectable decision data, an easy base for generated variations of the subject's behavior.
- What it is: Police officers worked through VR mental-health crisis calls with a clinician co-responder while thinking aloud, revealing how they decide where the clinician stands, what information to share and who takes which role.
- How it works: Qualitative study combining VR simulations, think-aloud protocols and semi-structured interviews with officers and a co-responder.
- Capability: Situational reach
- Paper: https://doi.org/10.1007/s12103-025-09831-w (American Journal of Criminal Justice (2025))
- Images: https://media.springernature.com/m685/springer-static/image/art%3A10.1007%2Fs12103-025-09831-w/MediaObjects/12103_2025_9831_Fig1_HTML.png

#### Introducing The Virtual Burglary Project – Pennsylvania (VBPP): An Open Access Virtual Reality Environment for Criminology Research — Patrick McClanahan (2025-03-27)
- Type: Open-source tool · Timing: Scripted / rule-based · Access: Open weights / code
- Input: Body, face & gaze tracking, Keyboard & controller actions → Output: Authored VR scenario, 3D scene / world
- Idea: Shared, open virtual stimuli let different labs run the same situation, the replication infrastructure generated scenarios will also need.
- What it is: Paper that releases two open-access virtual neighborhoods from the Pennsylvania arm of the Virtual Burglary Project, built to study burglary-related behavior, emotion and cognition and reusable by other criminologists.
- How it works: Description of two VR neighborhoods, their adjustable features and data logging, with example research questions; the project ran VR burglary tasks in US prisons.
- Capability: Experimental control, Authoring accessibility
- Paper: https://doi.org/10.21428/cb6ab371.f1f780ee (CrimRxiv (2025))
- Video: https://www.youtube.com/watch?v=2BST0F-Nq_8

#### Virtual Reality for Criminologists: A Road Map — Jean-Louis van Gelder (2023-08-08)
- Type: Paper / review
- Input:  → Output: Authored VR scenario
- Idea: Criminology's case for VR rests on observing behavior in situations that are illegal or unsafe to create, the class of situation generative tools could make cheaper to vary.
- What it is: Essay in Crime and Justice that reviews VR studies in criminogenic contexts and related fields, explains the technology's features, limits and ethical challenges, and argues that VR may become 'the criminological equivalent of the petri dish'.
- How it works: Review and research agenda covering ecological validity, theory testing, ethics and practical design choices for VR criminology.
- Capability: Situational reach, Experimental control
- Paper: https://doi.org/10.1086/726691 (Crime and Justice 52 (2023))

#### Learning on the job: Studying expertise in residential burglars using virtual environments — Claire Nee, Jean-Louis van Gelder (2019)
- Type: Behavioral study · Timing: Scripted / rule-based
- Input: Body, face & gaze tracking, Keyboard & controller actions → Output: Authored VR scenario
- Idea: A virtual scene validated by expert behavior (burglars act like burglars) sets the bar any generated crime scenario should meet.
- What it is: Fifty-six incarcerated burglars, 50 other offenders and 55 non-offenders each carried out a mock burglary in a virtual neighborhood; the burglars scoped the area and searched houses in ways that showed domain expertise.
- How it works: Quasi-experiment comparing the three groups on routes, time allocation and target selection during a virtual burglary, interpreted through cognitive expertise theory.
- Specs: N=161 (56 burglars · 50 other offenders · 55 non-offenders)
- Capability: Situational reach, Experimental control
- Paper: https://doi.org/10.1111/1745-9125.12210 (Criminology 57(3))
- Video: https://www.youtube.com/watch?v=82XkiXi7uQE

#### Offenders become the victim in virtual reality: impact of changing perspective in domestic violence — Sofia Seinfeld, Mel Slater (2018)
- Type: Behavioral study · Timing: Scripted / rule-based
- Input: Body, face & gaze tracking → Output: Virtual human (face / body), Authored VR scenario
- Idea: Swapping an offender into the victim's body is an intervention only VR can stage; generation could tailor the abuser, setting and script to each case.
- What it is: Male domestic-violence offenders and non-violent controls were embodied in a woman's virtual body while a virtual man verbally abused her; afterwards the offenders recognized fear in female faces better than before.
- How it works: Full-body ownership illusion through a head-mounted display and motion capture, with emotion-recognition tests before and after the virtual abuse scene.
- Capability: Situational reach, Experimental control
- Paper: https://doi.org/10.1038/s41598-018-19987-7 (Scientific Reports 8 (2018))
- Video: https://www.youtube.com/watch?v=l4R9aJIKzRI

#### Virtual Burglary: Exploring the Potential of Virtual Reality to Study Burglary in Action — Jean-Louis van Gelder (2017)
- Type: Behavioral study · Timing: Scripted / rule-based
- Input: Body, face & gaze tracking, Keyboard & controller actions → Output: Authored VR scenario
- Idea: Crime becomes an observable, logged behavior instead of a self-report, the kind of situational reach generated environments could extend to many more offences and settings.
- What it is: Seventy-seven male undergraduates walked a virtual neighborhood in a headset and were asked to burgle one house; the system logged their route, the items they stole and their heart rate, while an alarm and beliefs about the chance of being caught were varied.
- How it works: Free-roaming VR burglary task with experimentally varied alarm and perceived-risk conditions, behavioral logs, heart rate and dispositional measures (self-control, sensation seeking).
- Specs: N=77
- Capability: Situational reach, Experimental control
- Paper: https://doi.org/10.1177/0022427816663997 (Journal of Research in Crime and Delinquency 54(1))
- Video: https://www.youtube.com/watch?v=uAiuTmkKejY
- Project page: https://csl.mpg.de/en/projects/virtual-burglary-project

#### Crowd behaviour during high-stress evacuations in an immersive virtual environment — Mehdi Moussaïd (2016)
- Type: Behavioral study · Timing: Scripted / rule-based
- Input: Keyboard & controller actions → Output: Authored VR scenario, Agent behaviour & actions
- Idea: Multi-user virtual environments make crowd emergencies experimentally reachable; generated layouts and hazards could extend such tests far beyond one building.
- What it is: Groups of real participants, each controlling an avatar in a shared 3D virtual building, reproduced known crowd patterns during normal egress, and a high-stress evacuation condition showed how crowd movement changes under pressure.
- How it works: Networked multi-participant experiments comparing virtual crowd patterns with real-world observations, plus a high-stress evacuation condition.
- Capability: Situational reach, Experimental control
- Paper: https://doi.org/10.1098/rsif.2016.0414 (Journal of the Royal Society Interface 13(122))
- Video: https://www.youtube.com/watch?v=pqH7pPmM28c

### Simulation training & virtual humans

Virtual patients, interviewers and teammates for practising communication and judgement.

#### Talespin CoPilot Designer — Talespin (2021)
- Type: Product / app · Timing: Pre-generated · Access: Product / app
- Input: Text prompt → Output: Virtual human (face / body), Dialogue / text, Authored VR scenario
- Idea: Generative AI entered VR training first as an authoring aid, drafting branches that humans review, before it ran characters live.
- What it is: No-code tool for building VR soft-skills simulations with virtual humans, branching dialogue and feedback; by 2023 it had added generative AI for drafting content. Talespin's site now redirects to Cornerstone's immersive-learning platform, which advertises role play with AI-powered virtual humans.
- How it works: Flow editor for branching dialogue with animated virtual humans, extended with generative content tools, delivered on headsets and desktop.
- Capability: Authoring accessibility, Behavioral plausibility
- Video: https://www.youtube.com/watch?v=qOFuXWC67-c
- Project page: https://www.cornerstoneondemand.com/platform/immersive-learning/

#### Bodyswaps — Bodyswaps (2019)
- Type: Product / app · Timing: Turn-based · Access: Product / app
- Input: Speech & audio, Body, face & gaze tracking → Output: Virtual human (face / body), Dialogue / text, Speech / voice
- Idea: Commercial training has moved from branching scripts to open AI role-play with automated scoring; whether that scoring is valid is the open research question.
- What it is: Soft-skills training in VR and the browser in which learners hold role-play conversations with AI avatars, for example a nurse talking with a patient, then get a transcript and feedback from an AI coach on what they said and how they said it.
- How it works: AI avatar dialogue with speech input (likely LLM-based) on VR headsets, desktop and mobile, with automated analysis of speech content and nonverbal cues such as eye contact.
- Capability: Reactivity, Adaptation
- Video: https://www.youtube.com/watch?v=XtsHXFwbbCU
- Project page: https://bodyswaps.co/

#### SHOTPROS: VR training for police decision-making under stress — SHOTPROS (2019)
- Type: Research demo · Timing: Scripted / rule-based · Access: Research only
- Input: Body, face & gaze tracking, Keyboard & controller actions, Speech & audio → Output: Authored VR scenario
- Idea: Stress becomes a controllable training parameter that trainers dial up or down, a natural slot for adaptive generation.
- What it is: EU Horizon 2020 project in which police organizations, psychologists and VR developers built and field-tested VR scenarios for training decision-making and acting under stress, with physiological monitoring and trainer controls.
- How it works: Requirements from police trainers, human-factors studies and multi-country field trials over three years, summarized as tools and guidelines by Zechner et al. (2023).
- Capability: Situational reach, Experimental control
- Paper: https://doi.org/10.3390/mti7020014 (Multimodal Technologies and Interaction 7(2))
- Video: https://www.youtube.com/watch?v=MXJHzBUbdgU
- Project page: https://shotpros.eu/

#### Axon VR Training — Axon (2018)
- Type: Product / app · Timing: Scripted / rule-based · Access: Product / app
- Input: Body, face & gaze tracking, Keyboard & controller actions → Output: Authored VR scenario, 360° / stereo video
- Idea: De-escalation is now trained in headsets at police-department scale; Axon says some scenarios adapt in real time, a claim worth testing against scripted branching.
- What it is: VR training for police from the maker of TASER and body cameras. It began in October 2018 with a 360-degree empathy scenario about schizophrenia, followed in 2019 by autism and suicide scenarios; today officers progress from empathy and crisis-response modules to de-escalation, tactical decision-making and simulator drills with replica TASERs and handguns.
- How it works: Authored live-action and CG scenarios on standalone headsets with tracked weapon replicas and instructor controls; adaptivity is developer-reported.
- Capability: Situational reach, Adaptation
- Video: https://www.youtube.com/watch?v=PA8DoNYwCz4
- Project page: https://www.axon.com/products/vr

#### Strivr — Strivr (2015)
- Type: Product / app · Timing: Scripted / rule-based · Access: Product / app
- Input: Body, face & gaze tracking → Output: 360° / stereo video, Authored VR scenario
- Idea: Filmed 360-degree situations took VR rehearsal to a large retail workforce; the company's next step was AI that watches real work through glasses.
- What it is: Enterprise VR training that grew out of Stanford's VHIL: 360-degree video and interactive modules let workers rehearse situations such as store rushes or difficult customers, and Walmart deployed it in its training academies. In 2026 its site leads with AI quality assurance on smart glasses while still offering the VR platform.
- How it works: Captured 360-degree video and authored interactive scenarios delivered on standalone headsets, with analytics on trainee responses.
- Capability: Perceptual realism, Situational reach
- Video: https://www.youtube.com/watch?v=0s4OBHV0WH4
- Project page: https://www.strivr.com/

#### Mursion — Mursion (2014)
- Type: Product / app · Timing: Real-time streaming · Access: Product / app
- Input: Speech & audio, Body, face & gaze tracking → Output: Virtual human (face / body), Dialogue / text, Speech / voice
- Idea: A human-in-the-loop virtual human shows what full reactivity looks like at scale; LLM agents are measured against this Wizard-of-Oz baseline.
- What it is: Simulation platform where employees and teachers rehearse difficult conversations with avatars; trained simulation specialists voice and steer the avatars live, and by 2026 Mursion presents itself as an AI-powered upskilling platform.
- How it works: Avatars puppeteered in real time by a trained human operator (voice, expression, behavior) following scenario guides and coaching; the company now also advertises AI-powered simulations.
- Capability: Reactivity, Adaptation
- Video: https://www.youtube.com/watch?v=yRD4Hbn3EUM
- Project page: https://www.mursion.com/

#### Reconsidering Fidelity in Simulation-Based Training — Stanley J. Hamstra (2014)
- Type: Paper / review
- Input:  → Output: Authored VR scenario
- Idea: Generated realism is not the goal: a training scenario needs the cues that matter for the task, which is cheaper and more testable than photorealism.
- What it is: Commentary in Academic Medicine arguing that 'fidelity' should be replaced by physical resemblance and functional task alignment, and that learning is driven by engagement and correspondence with the task rather than surface realism.
- How it works: Conceptual analysis of the simulation-training literature by Hamstra, Brydges, Hatala, Zendejas and Cook.
- Capability: Perceptual realism, Behavioral plausibility
- Paper: https://doi.org/10.1097/ACM.0000000000000130 (Academic Medicine 89(3))

#### Virtual Reality Job Interview Training in Adults with Autism Spectrum Disorder — Matthew J. Smith (2014)
- Type: Behavioral study · Timing: Scripted / rule-based
- Input: Speech & audio → Output: Virtual human (face / body), Dialogue / text, Speech / voice
- Idea: Graded difficulty and endless repetition with a virtual interviewer already worked with branching scripts; generation removes the authoring ceiling, not the need for trials.
- What it is: Randomized trial of Virtual Reality Job Interview Training, in which adults with autism repeatedly interview with a virtual hiring manager ('Molly Porter') whose difficulty can be raised and who gives feedback; trainees improved their role-play interview performance compared with controls.
- How it works: Randomized controlled efficacy trial of SIMmersion's branching-dialogue simulator, assessed with role-play interviews before and after training.
- Capability: Adaptation, Reactivity
- Paper: https://doi.org/10.1007/s10803-014-2113-y (Journal of Autism and Developmental Disorders 44)
- Video: https://www.youtube.com/watch?v=Uz-hfR1Hulo

#### Building Interactive Virtual Humans for Training Environments — Patrick Kenny, USC Institute for Creative Technologies (2007)
- Type: Paper / review · Timing: Scripted / rule-based
- Input: Speech & audio, Body, face & gaze tracking → Output: Virtual human (face / body), Dialogue / text, Agent behaviour & actions
- Idea: The pre-LLM blueprint: every module of a training virtual human was hand-built and authored, the cost that generative models now remove and the control they put at risk.
- What it is: I/ITSEC paper from USC ICT describing the architecture of interactive virtual humans for training: speech recognition, language understanding, dialogue management, emotion modeling, nonverbal behavior generation and rendering, with examples from ICT's negotiation and virtual-patient trainers.
- How it works: System overview of ICT's integrated virtual human architecture and the authoring work behind its training applications.
- Capability: Behavioral plausibility, Authoring accessibility
- Paper: https://openalex.org/W2151904280 (I/ITSEC 2007)

#### The validity of a virtual human experience for interpersonal skills education — Kyle Johnsen (2007)
- Type: Behavioral study · Timing: Scripted / rule-based
- Input: Speech & audio, Body, face & gaze tracking → Output: Virtual human (face / body), Dialogue / text
- Idea: Validation against the real-world exam is the step most LLM virtual-patient papers still skip.
- What it is: Thirty-three second-year medical students interviewed a life-size virtual patient in a Virtual Objective Structured Clinical Examination (VOSCE) and were graded on interview skills; their scores were compared with an exam using a human standardized patient.
- How it works: Comparison of interview performance with a projected life-size virtual human (speech-recognition dialogue) and with a human standardized patient, as part of a medical-school course requirement.
- Specs: N=33 medical students
- Capability: Behavioral plausibility, Experimental control
- Paper: https://doi.org/10.1145/1240624.1240784 (CHI 2007)

#### Virtual Standardized Patients (Justin, Justina) — USC Institute for Creative Technologies, Albert "Skip" Rizzo (2007)
- Type: Research demo · Timing: Scripted / rule-based · Access: Research only
- Input: Speech & audio → Output: Virtual human (face / body), Dialogue / text
- Idea: Standardized patients that never tire and never drift: the consistency LLM-driven patients trade for breadth.
- What it is: Life-size virtual patients from USC ICT, such as an adolescent with conduct disorder and a young woman with PTSD after sexual assault, that clinicians in training interview by speaking; the patient answers with authored lines chosen by a language-understanding module.
- How it works: Statistical classification of trainee questions into authored response sets, animated with ICT's virtual human technology and evaluated with psychiatry residents and social-work students.
- Capability: Behavioral plausibility, Reactivity
- Paper: https://doi.org/10.20385/1860-2037/8.2011.3 (Journal of Virtual Reality and Broadcasting 8 (2011))
- Video: https://www.youtube.com/watch?v=PPbcl8Z-8Ec

#### The role of deliberate practice in the acquisition of expert performance — K. Anders Ericsson (1993)
- Type: Paper / review
- Input:  → Output: Authored VR scenario
- Idea: Training value comes from many targeted repetitions with feedback at the edge of ability, which adaptive generated scenarios can offer at scale.
- What it is: Psychological Review paper showing that expert musicians differ from less accomplished peers mainly in accumulated hours of deliberate practice: effortful, goal-directed practice with immediate feedback and repetition, designed to improve performance.
- How it works: Theoretical framework plus retrospective diary and interview studies of violinists and pianists at a Berlin music academy.
- Capability: Adaptation, Situation diversity
- Paper: https://doi.org/10.1037/0033-295X.100.3.363 (Psychological Review 100(3))

### Clinical & therapeutic VR

Exposure, coaching and therapy delivered in virtual situations.

#### Desensitizing Anxiety Through Imperceptible Change: Feasibility Study on a Paradigm for Single-Session Exposure Therapy for Fear of Public Speaking — Domna Banakou, Mel Slater (2024-07-22)
- Type: Behavioral study · Timing: Scripted / rule-based
- Input: Speech & audio, Body, face & gaze tracking → Output: Authored VR scenario, Virtual human (face / body)
- Idea: A situation that morphs continuously and below awareness compresses a whole exposure ladder into one session, a kind of control only generated or procedural scenes allow.
- What it is: People afraid of public speaking talked with a virtual therapist who, over a single session, turned into an entire audience through almost imperceptible changes; a week later this single session reduced anxiety about speaking on a virtual stage at least as much as five conventional exposure sessions.
- How it works: Feasibility study with three arms (single-session imperceptible change n=16, five-session exposure n=14, control conversation n=15) and a VR speaking test a week later, analysed with Bayesian models.
- Specs: N=45 · 3 arms · test after 1 week
- Capability: Adaptation, Experimental control
- Paper: https://doi.org/10.2196/52212 (JMIR Formative Research 8 (2024))
- Video: https://www.youtube.com/watch?v=QFvJMPmdsDE

#### Automated virtual reality therapy to treat agoraphobic avoidance and distress in patients with psychosis (gameChange): a multicentre, parallel-group, single-blind, randomised, controlled trial in England with mediation and moderation analyses — Daniel Freeman (2022)
- Type: Behavioral study · Timing: Scripted / rule-based
- Input: Body, face & gaze tracking → Output: Authored VR scenario, Virtual human (face / body), Speech / voice
- Idea: Therapy can run without a therapist in the room once the situation and the coach are automated; this trial standard is what generated therapies will have to match.
- What it is: Multicentre randomized trial across nine NHS trusts of gameChange, automated VR therapy in which a virtual coach guides people with psychosis through everyday situations they avoid, such as a café, a bus or a shop, at graded difficulty; it reduced avoidance and distress, most clearly for people with severe agoraphobia.
- How it works: Single-blind RCT (gameChange plus usual care vs. usual care alone) with graded VR exposure led by a pre-recorded virtual coach, plus mediation and moderation analyses.
- Specs: 9 NHS trusts · single-blind RCT
- Capability: Situational reach, Adaptation
- Paper: https://doi.org/10.1016/S2215-0366(22)00060-8 (The Lancet Psychiatry 9(5))
- Video: https://www.youtube.com/watch?v=AdMLfdPBb60
- Project page: https://gamechangevr.com/

#### RelieVRx — AppliedVR (2021)
- Type: Product / app · Timing: Scripted / rule-based · Access: Product / app
- Input: Body, face & gaze tracking → Output: Authored VR scenario, Sound, music & spatial audio
- Idea: Scripted VR became a regulated medical device; any generative or adaptive successor will have to clear the same evidence bar.
- What it is: Prescription home VR program for chronic low back pain that teaches pain-management skills such as breathing, relaxation and attention shifting through short daily sessions; it received FDA De Novo authorization in 2021.
- How it works: Pre-built modules grounded in cognitive behavioral therapy and mindfulness, delivered on a standalone headset at home and evaluated in randomized trials against sham VR.
- Capability: Adaptation, Situational reach
- Video: https://www.youtube.com/watch?v=iDM1vHLlH9Q
- Project page: https://www.relievrx.com/

#### AVATAR therapy for auditory verbal hallucinations in people with psychosis: a single-blind, randomised controlled trial — Tom Craig (2018)
- Type: Behavioral study · Timing: Real-time streaming
- Input: Speech & audio → Output: Virtual human (face / body), Speech / voice
- Idea: A personalized, human-voiced avatar of a patient's tormentor is a clinical use of virtual humans that LLMs could scale but must not let drift.
- What it is: People who hear persecutory voices created a digital face and voice for their main voice, then held dialogues with it while a therapist spoke as the avatar through a voice transformer and gradually made it less hostile; voices became less severe than with supportive counselling.
- How it works: Single-blind RCT of AVATAR therapy (invented by Julian Leff in 2008) vs. supportive counselling, with avatars built from patients' descriptions and voiced live by the therapist; the larger AVATAR2 trial followed in 2024.
- Capability: Reactivity, Adaptation
- Paper: https://doi.org/10.1016/S2215-0366(17)30427-3 (The Lancet Psychiatry 5(1))
- Video: https://www.youtube.com/watch?v=4Gmp9IILUx4

#### Automated psychological therapy using immersive virtual reality for treatment of fear of heights: a single-blind, parallel-group, randomised controlled trial — Daniel Freeman (2018)
- Type: Behavioral study · Timing: Scripted / rule-based
- Input: Body, face & gaze tracking → Output: Authored VR scenario, Virtual human (face / body), Speech / voice
- Idea: Early rigorous evidence that a fully automated virtual coach can deliver psychological therapy, the precedent for LLM-guided therapy in VR.
- What it is: Randomized trial in which adults with fear of heights received about six 30-minute VR sessions over two weeks guided by an animated virtual coach, with no therapist present; fear of heights fell substantially compared with usual care.
- How it works: Single-blind RCT of automated cognitive VR therapy (virtual coach animated from an actor's motion and voice capture) on consumer headsets vs. usual care, with the Heights Interpretation Questionnaire as outcome.
- Specs: ~6 × 30-min sessions over 2 weeks
- Capability: Adaptation, Situational reach
- Paper: https://doi.org/10.1016/S2215-0366(18)30226-8 (The Lancet Psychiatry 5(8))
- Video: https://www.youtube.com/watch?v=yDJArJ40FGc

#### Conversations between self and self as Sigmund Freud—A virtual body ownership paradigm for self counselling — Sofia Adelaide Osimo, Mel Slater (2015)
- Type: Behavioral study · Timing: Scripted / rule-based
- Input: Speech & audio, Body, face & gaze tracking → Output: Virtual human (face / body), Authored VR scenario, Speech / voice
- Idea: The counsellor can be the participant in another body, a design that later work extends with AI agents nudging the self-dialogue.
- What it is: Participants explained a personal problem to a virtual counsellor, then swapped into the counsellor's body and answered themselves, hearing their own voice transformed; being embodied as Sigmund Freud when giving the advice improved mood more than counselling from a copy of their own body.
- How it works: Embodiment experiment with full-body tracking, alternating first-person perspective between participant and counsellor avatars with voice transformation, comparing a Freud body with a self-copy body.
- Capability: Co-creation & agency, Situational reach
- Paper: https://doi.org/10.1038/srep13899 (Scientific Reports 5 (2015))
- Video: https://www.youtube.com/watch?v=sn-UNGcbi2Q

#### It's only a computer: Virtual humans increase willingness to disclose — Gale Lucas, USC Institute for Creative Technologies (2014)
- Type: Behavioral study · Timing: Scripted / rule-based
- Input: Speech & audio, Body, face & gaze tracking → Output: Virtual human (face / body), Dialogue / text
- Idea: Believing no human is watching makes people more open, so what participants are told about an AI interlocutor is itself a variable to control.
- What it is: People interviewed by the SimSensei virtual human reported less fear of self-disclosure, managed their impressions less and showed sadness more openly when they believed it was fully automated than when they believed a human was operating it.
- How it works: 2x2 design crossing framing (computer vs. human operator) with actual control (automated vs. Wizard-of-Oz), measuring fear of disclosure, impression management and coded emotional expression.
- Capability: Behavioral plausibility, Experimental control
- Paper: https://doi.org/10.1016/j.chb.2014.04.043 (Computers in Human Behavior 37)

#### SimSensei Kiosk: a virtual human interviewer for healthcare decision support — David DeVault, USC Institute for Creative Technologies (2014)
- Type: Research demo · Timing: Scripted / rule-based · Access: Research only
- Input: Speech & audio, Video, Body, face & gaze tracking → Output: Virtual human (face / body), Dialogue / text, Speech / voice
- Idea: Built in three cycles, from face-to-face data to Wizard-of-Oz to full automation, the method a generative interviewer would still need to follow.
- What it is: Virtual human interviewer 'Ellie' who asks people about their lives and wellbeing while the MultiSense module tracks face, gaze, posture and voice; she gives listening feedback and follow-up questions, and the system extracts indicators of depression, anxiety and PTSD.
- How it works: Analysis of human interviews, a Wizard-of-Oz prototype with two operators choosing speech and gestures, then an automated system with multimodal perception, rule-based dialogue policies and authored utterances.
- Capability: Temporal responsiveness, Reactivity
- Paper: https://doi.org/10.65109/mxiv3169 (AAMAS 2014)
- Video: https://www.youtube.com/watch?v=ejczMs6b1Q4

#### Virtual Reality as an Adjunctive Non-pharmacologic Analgesic for Acute Burn Pain During Medical Procedures — Hunter Hoffman (2011)
- Type: Paper / review · Timing: Scripted / rule-based
- Input: Body, face & gaze tracking, Keyboard & controller actions → Output: Authored VR scenario
- Idea: Immersion itself works like a dose: attention drawn into a virtual world is attention taken from pain, so stronger immersion can mean stronger effect.
- What it is: Review of SnowWorld, the University of Washington VR world in which burn patients throw snowballs at snowmen and penguins during wound care; patients report 35-50% less procedural pain while immersed, and fMRI shows lower pain-related brain activity.
- How it works: Review of clinical and laboratory studies by Hoffman's group, including water-friendly and robot-arm-mounted headsets for hydrotank wound care.
- Specs: 35-50% less procedural pain (patient reports)
- Capability: Perceptual realism, Situational reach
- Paper: https://doi.org/10.1007/s12160-010-9248-7 (Annals of Behavioral Medicine 41(2))
- Video: https://www.youtube.com/watch?v=Nh4K_dZ7LvQ

#### Bravemind — Albert "Skip" Rizzo, USC Institute for Creative Technologies (2005)
- Type: Research demo · Timing: Scripted / rule-based · Access: Research only
- Input: Body, face & gaze tracking, Keyboard & controller actions → Output: Authored VR scenario, Sound, music & spatial audio
- Idea: A clinician who adjusts stimuli in real time is the original adaptive immersive situation; generation would widen the scene library each clinician can draw on.
- What it is: VR exposure therapy for combat-related PTSD that grew out of 'Virtual Iraq': a clinician places the patient in customizable Iraq and Afghanistan scenes and adds sounds, smells, explosions and vibration step by step as the patient recounts the trauma.
- How it works: Prolonged exposure therapy delivered with a head-mounted display, a clinician control panel for stimulus onset and multisensory add-ons, evaluated in open trials and randomized trials.
- Capability: Situational reach, Adaptation
- Paper: https://doi.org/10.1080/20008198.2017.1414560 (European Journal of Psychotraumatology 8 (2017))
- Video: https://www.youtube.com/watch?v=LRL0TzrNtVc
- Project page: https://ict.usc.edu/research/projects/bravemind-virtual-reality-exposure-therapy/

#### Effectiveness of computer-generated (virtual reality) graded exposure in the treatment of acrophobia — Barbara Olasov Rothbaum (1995)
- Type: Behavioral study · Timing: Scripted / rule-based
- Input: Body, face & gaze tracking → Output: Authored VR scenario
- Idea: Graded exposure needs only a believable ladder of situations, which is why VR therapy worked with 1995 graphics and why generation's contribution is breadth and personalization.
- What it is: Early controlled study of VR exposure therapy: students with fear of heights rode a virtual glass elevator, crossed bridges and stood on balconies at increasing heights in a head-mounted display, and showed less anxiety and avoidance than a waiting-list group.
- How it works: Controlled comparison of graded VR exposure with a waiting-list control, with anxiety, avoidance and attitude measures, by Rothbaum, Hodges and colleagues at Emory University and Georgia Tech.
- Capability: Situational reach, Adaptation
- Paper: https://doi.org/10.1176/ajp.152.4.626 (American Journal of Psychiatry 152(4))

### Generative AI in immersive studies

Studies and reviews that put LLM agents, generated scenarios or world models into research and training.

#### When Generative Artificial Intelligence Meets Extended Reality: A Systematic Review — Xinyu Ning (2026)
- Type: Paper / review
- Input: Text prompt, Speech & audio → Output: 3D scene / world, Virtual human (face / body), Dialogue / text
- Idea: The field is young and small: three years of work fit in 26 papers, so methods for generative immersive research are still open territory.
- What it is: PRISMA systematic review of 26 articles from 2023 to 2025 that combine generative AI with XR, summarizing the application areas and key technical implementations and pointing out research gaps.
- How it works: Systematic review following PRISMA with database search, screening and thematic analysis of the included articles.
- Capability: Authoring accessibility, Situation diversity
- Paper: https://doi.org/10.1080/10447318.2025.2565392 (International Journal of Human-Computer Interaction (2026; online 2025-09-30))

#### VR scuba diving with harbor seals increases ocean connectedness, and the effect of conversational AI on pro-environmental engagement depends on prior experience with seals — Gustav Bøg Petersen, Jeremy Bailenson (2026-09-07)
- Type: Behavioral study · Timing: Turn-based
- Input: Speech & audio → Output: Authored VR scenario, Virtual human (face / body), Dialogue / text
- Idea: Yoked controls address the core problem of studying generative conversation: each control sees exactly what a treated participant got, which isolates the effect of interacting.
- What it is: In OceanSpeak, participants scuba-dive in VR and talk with an AI-powered harbor seal about ocean acidification and overfishing. A preregistered study (N=106) used a yoked control: control participants saw identical content, including another participant's AI conversation, but could not talk themselves.
- How it works: Preregistered between-subjects experiment with Stanford's Virtual Human Interaction Lab using yoked replay of AI conversations; outcomes were ocean connectedness, empathy with seals, pro-ocean behaviors and knowledge.
- Specs: N=106 (53 + 53 yoked controls)
- Capability: Experimental control, Reactivity
- Paper: https://doi.org/10.1016/j.cexr.2026.100181 (Computers & Education: X Reality (2026))

#### CoEmpaTeam: Enhancing Cognitive Empathy using LLM-based Avatars and Dynamic Role Play in Virtual Reality — Dehui Kong (2026-04-13)
- Type: Research demo · Timing: Turn-based · Access: Research only
- Input: Speech & audio, Body, face & gaze tracking → Output: Virtual human (face / body), Dialogue / text, Speech / voice
- Idea: Personality becomes a controllable, pre-validated parameter of LLM characters, a step toward treating generated people as calibrated stimuli.
- What it is: VR system for training cognitive empathy in which users work with three LLM-driven avatars of clearly different personalities and switch roles to see situations through another person's eyes; the personalities were validated in an online experiment (n=90) and the system was tested in a lab study (n=32).
- How it works: LLM-driven avatars with prompted personalities, technical and online validation of perceived personality, then a lab experiment on cognitive-empathy outcomes.
- Specs: online N=90 · lab N=32
- Capability: Behavioral plausibility, Situation diversity
- Paper: https://doi.org/10.1145/3772318.3790389 (CHI 2026)
- Video: https://www.youtube.com/watch?v=ODzQGc8KNZI

#### Where extended reality and AI may take us: Ethical issues of impersonation and AI fakes in social virtual reality — Ramon Oliva, Mel Slater (2026-04-02)
- Type: Behavioral study · Timing: Turn-based
- Input: Speech & audio, Body, face & gaze tracking → Output: Virtual human (face / body), Dialogue / text, Speech / voice
- Idea: Look-alike avatars plus LLM agents make identity itself manipulable, so studies with generated people need disclosure and consent rules of their own.
- What it is: At IEEE VR 2025 a panel was held in social VR with each panellist in a look-alike avatar; midway two panellists swapped avatars and impersonated each other, and an LLM-controlled Alan Turing avatar took part. About 40 of the 100 audience members who answered a survey did not notice the swap.
- How it works: Field study during a live conference panel projected to the audience, with a post-panel survey on detecting the swap and perceiving the AI panellist.
- Specs: ~100 audience survey responses
- Capability: Perceptual realism, Behavioral plausibility
- Paper: https://doi.org/10.1371/journal.pone.0340829 (PLOS ONE (2026))
- Images: https://journals.plos.org/plosone/article/figure/image?id=10.1371/journal.pone.0340829.g001&size=large

#### Artificial intelligence (AI) for virtual reality exposure therapy (VRET): A systematic review — Kamilla Bergsnev (2026-03-26)
- Type: Paper / review
- Input: Body, face & gaze tracking, Speech & audio → Output: Authored VR scenario
- Idea: Adaptive exposure, adjusting the feared situation to the patient in the moment, is the clinical use case closest to real-time generation, and its evidence base is still small.
- What it is: PRISMA systematic review of 23 peer-reviewed articles, published up to November 2025, on using artificial intelligence to tailor VR exposure therapy to the needs of patients and therapists.
- How it works: Systematic review following PRISMA across PsycINFO, Web of Science, Google Scholar, EMBASE, CINAHL and MEDLINE; 23 of 377 screened records included.
- Specs: 23 of 377 records
- Capability: Adaptation, Experimental control
- Paper: https://doi.org/10.1038/s41398-026-03936-4 (Translational Psychiatry (2026))

#### Integrating Virtual Reality and Large Language Models for Team-Based Non-Technical Skills Training and Evaluation in the Operating Room — Jacob Barker (2026-01-19)
- Type: Research demo · Timing: Pre-generated · Access: Research only
- Input: Speech & audio, Body, face & gaze tracking → Output: Authored VR scenario, Dialogue / text
- Idea: Here the LLM is the measurement instrument, not the scenario: automated, structured coding of team behavior adds experimental control instead of removing it.
- What it is: VORTeX is a multi-user VR operating room in which surgical teams handle laparoscopic emergencies (pneumothorax, intra-abdominal bleeding); an LLM then classifies the team's dialogue against the NOTSS framework and draws networks of who leads and who integrates.
- How it works: Multi-user VR simulation with recorded team speech; structured prompts derived from NOTSS classify behaviors and build directed communication graphs; pilot with 12 surgical professionals at SAGES 2024.
- Specs: pilot N=12 · 2 emergency scenarios
- Capability: Experimental control, Behavioral plausibility
- Paper: https://doi.org/10.1038/s44484-026-00009-3 (npj Digital Surgery (2026))
- Images: https://media.springernature.com/lw685/springer-static/image/art%3A10.1038%2Fs44484-026-00009-3/MediaObjects/44484_2026_9_Fig1_HTML.png

#### CLiVR: Conversational Learning System in Virtual Reality with AI-Powered Patients — Akilan Amithasagaran (2025-10-21)
- Type: Research demo · Timing: Turn-based · Access: Research only
- Input: Speech & audio → Output: Virtual human (face / body), Dialogue / text, Speech / voice
- Idea: Sampling cases from a structured database gives LLM patients variety with a handle on what varies, a practical answer to the control problem.
- What it is: Meta Quest 3 system in which medical trainees hold spoken conversations with LLM-driven virtual patients; each case is generated from a syndrome-symptom database, and sentiment analysis gives feedback on the trainee's tone. Thirteen medical-school faculty rated it usable and realistic.
- How it works: Unity application combining speech processing, an LLM conditioned on a generated case and 3D avatars; expert user study (n=13) on usability, realism and educational value.
- Specs: Meta Quest 3 · expert study N=13
- Capability: Situation diversity, Reactivity
- Paper: https://arxiv.org/abs/2510.19031 (arXiv (2025))
- Images: https://arxiv.org/html/2510.19031v1/Images/vr-combined.png

#### A Latency-Optimized LLM-based Multimodal Dialogue System for Embodied Conversational Agents in VR — Konstantin W. Kühlem (2025-09-16)
- Type: Research demo · Timing: Turn-based · Access: Research only
- Input: Speech & audio → Output: Virtual human (face / body), Dialogue / text, Speech / voice
- Idea: Turn-taking delay is the first thing that breaks plausibility with LLM characters, so engineering for latency is part of the experimental apparatus.
- What it is: Dialogue system that shortens response latency for an LLM-driven embodied guide in a VR museum, who helps visitors explore artworks and artists with spoken replies and gestures.
- How it works: Multimodal agent pipeline (speech recognition, LLM, speech synthesis, gesture) optimized for end-to-end latency, likely by overlapping stages; a follow-up study on engagement appeared at IEEE AIxVR 2026.
- Capability: Temporal responsiveness
- Paper: https://doi.org/10.1145/3717511.3749287 (IVA 2025)
- Video: https://www.youtube.com/watch?v=kfjh-9yDeQQ

#### Inceptor: Automated Generation of Social Scenarios in Virtual Reality — Dan Pollak, Doron Friedman (2025-09-16)
- Type: Research demo · Timing: Pre-generated · Access: Research only
- Input: Text prompt, Scene spec, code & rules → Output: Authored VR scenario, Virtual human (face / body), Motion / animation
- Idea: Generating many short social scenes of authored quality is where generation already pays off for training, before any live LLM conversation.
- What it is: Pipeline that turns written scenario descriptions into social VR episodes with animated virtual characters; for a mental-health resilience training project it produced 32 episodes, more than two hours of content, in a short time, and the authors tested an LLM for choosing character animations.
- How it works: Automated authoring pipeline from scripts to multi-character VR scenes, used in a deployed resilience-training program; the authors report that it will be released as open source.
- Specs: 32 episodes · >2 h of content
- Capability: Authoring accessibility, Situation diversity
- Paper: https://doi.org/10.1145/3717511.3747061 (IVA 2025)
- Video: https://www.youtube.com/watch?v=uUfgWLcIdaY

#### Milo: an LLM-based virtual human open-source platform for extended reality — Alon Shoa, Doron Friedman (2025-06-05)
- Type: Open-source tool · Timing: Turn-based · Access: Open weights / code
- Input: Speech & audio, Body, face & gaze tracking → Output: Virtual human (face / body), Dialogue / text, Speech / voice
- Idea: Open, lab-owned virtual-human stacks matter for research: a study can pin the prompt, model and behavior pipeline it actually ran.
- What it is: Open-source system for putting LLM-driven virtual humans into VR and AR applications, demonstrated as a single conversational agent, an attendee of a multi-user VR meeting, a helper in a VR self-talk session and a participant in an AR live event.
- How it works: Architecture that integrates speech recognition, an LLM, speech synthesis and avatar animation into XR platforms, with lessons from several deployments.
- Capability: Authoring accessibility, Reactivity
- Paper: https://doi.org/10.3389/frvir.2025.1555173 (Frontiers in Virtual Reality 6 (2025))
- Images: https://www.frontiersin.org/files/Articles/1555173/frvir-06-1555173-HTML/image_m/frvir-06-1555173-g001.jpg
- Code: https://github.com/Advanced-Reality-Lab/Milo

#### AI-Enhanced Virtual Reality Self-Talk for Psychological Counseling: Formative Qualitative Study — Moreah Zisquit, Doron Friedman, Mel Slater (2025-02-10)
- Type: Behavioral study · Timing: Turn-based
- Input: Speech & audio, Body, face & gaze tracking → Output: Virtual human (face / body), Dialogue / text, Speech / voice
- Idea: Instead of replacing the therapist, the LLM nudges a person's own reasoning, a lower-risk role for generative agents in clinical VR.
- What it is: Adds an AI agent to embodied VR self-talk, where people alternate between their own avatar and a counsellor avatar; the agent steps in with guidance when participants get stuck, and a formative qualitative study explored how people experienced its help.
- How it works: Formative qualitative study with interviews after AI-supported VR self-talk sessions, by Reichman University's Advanced Reality Lab with Mel Slater.
- Capability: Co-creation & agency, Reactivity
- Paper: https://doi.org/10.2196/67782 (JMIR Formative Research 9 (2025))

#### Exploring the Use of Large Language Model-Driven Chatbots in Virtual Reality to Train Autistic Individuals in Job Communication Skills — Ziming Li (2024-05-11)
- Type: Research demo · Timing: Turn-based · Access: Research only
- Input: Speech & audio, Text prompt → Output: Virtual human (face / body), Dialogue / text, Speech / voice
- Idea: Prompting replaces branching scripts, so the coach rather than a developer authors the scenario: the VR-JIT idea with the authoring bottleneck removed.
- What it is: VR application in which autistic trainees practise customer conversations by speaking with avatars driven by GPT-3.5 Turbo, while job coaches create the training scenarios by writing text prompts; a preliminary study involved three trainees and two job coaches.
- How it works: Speech-to-text, LLM response generation and text-to-speech for VR avatars, evaluated in a preliminary usability study; the RIT lab has since extended the line to environment-grounded role play.
- Specs: 3 trainees · 2 job coaches
- Capability: Authoring accessibility, Reactivity
- Paper: https://doi.org/10.1145/3613905.3651996 (CHI EA 2024)
- Video: https://www.youtube.com/watch?v=p5zcxrxM8BQ

## Platforms, APIs & Delivery

What it takes to build and deliver: model APIs and inference hosts, real-time agent stacks, engines and splat runtimes, headsets and displays, and the datasets and benchmarks the field measures itself by.

### Model APIs & inference hosts

Where developers call video, 3D, world and avatar models: first-party APIs and hosts such as fal and Replicate.

#### World API — World Labs (2026-01-21)
- Type: Platform / API · Timing: Pre-generated · Access: Public API
- Input: Text prompt, Image, Video → Output: Gaussian splats / radiance field, 3D scene / world
- Idea: Turns 'build the room' into an API call that returns an explicit 3D world, so a lab can generate many variants of a setting and then keep each one fixed for every participant.
- What it is: World Labs' public API for its Marble world model: send text, one image, several images, a 360° panorama or a video, and get back a navigable 3D world that renders in the browser or exports to other tools. World Labs reports uses such as turning 2D films into explorable spaces (Escape.ai) and generating environments for robot simulators like Isaac Sim and MuJoCo.
- How it works: Asynchronous world-generation requests run Marble, which lifts the inputs into a 3D Gaussian-splat scene with optional mesh export.
- Specs: inputs: text, image, multi-image, 360° panorama, video · output: Gaussian splats + mesh · launched 2026-01-21
- Capability: Authoring accessibility, Persistence, Situational reach
- Video: https://wlt-ai-cdn.art/videos/marble_labs/world-api.mp4
- Images: https://www.worldlabs.ai/api/opengraph-image?imageUrl=/images/world-api.jpg&title=Announcing%20the%20World%20API
- Project page: https://www.worldlabs.ai/blog/announcing-the-world-api
- API docs: https://docs.worldlabs.ai

#### Decart API Platform — Decart (2025)
- Type: Platform / API · Timing: Real-time streaming · Access: Public API
- Input: Video, Text prompt, Keyboard & controller actions → Output: Interactive frame stream, Flat video
- Idea: Real-time generation sold by the second makes a live, generatively altered surrounding something a lab can rent rather than train.
- What it is: Decart's API streams real-time generative video: Lucy 2.5 edits or restyles a live camera feed (swapping characters, objects or backgrounds) over WebRTC, and the Oasis 3 Preview world model returns camera frames in response to driving actions over gRPC. Billing is per second of active generation, $0.01–0.04 per second at 720p as of October 2026.
- How it works: WebRTC (Lucy) and gRPC (Oasis) sessions to Decart-hosted autoregressive video models, with JavaScript and Python SDKs; Decart reports serving them on AWS Trainium 3.
- Specs: Lucy 2.5: 720p, $0.02/s ($0.04/s fast mode) · Lucy Restyle 2: $0.01/s · Oasis 3 Preview: $0.02/s
- Capability: Temporal responsiveness, Reactivity
- Video: https://www.youtube.com/watch?v=GXTOeJlDS9o
- Images: https://cdn.prod.website-files.com/69a974f0b1fffb03644ecf2c/69b94eac7c2b44111d02c52d_og.jpg
- Project page: https://platform.decart.ai
- API docs: https://docs.platform.decart.ai

#### OpenAI Videos API (Sora 2) — OpenAI (2025-10-06)
- Type: Platform / API · Timing: Pre-generated · Access: Public API
- Input: Text prompt, Image, Video → Output: Flat video, Sound, music & spatial audio
- Idea: A frontier video model you could call and pin by snapshot until the vendor withdrew it: a study built on a hosted generator can lose its stimulus source on a fixed date.
- What it is: OpenAI's v1/videos endpoint put Sora 2 and Sora 2 Pro behind a public API, so developers could generate, remix, extend and edit clips with synchronized sound. OpenAI removed the Videos API and every Sora 2 snapshot from the API on 2026-09-24, with no replacement.
- How it works: Asynchronous REST jobs (POST /v1/videos) rendered by OpenAI's Sora 2 models (architecture undisclosed; likely diffusion transformers like the first Sora), with character references, extensions, edits and Batch API support added in March 2026.
- Specs: sora-2 / sora-2-pro · up to 20 s · 1080p on sora-2-pro ($0.70/s) · launched 2025-10-06 · removed 2026-09-24
- Capability: Authoring accessibility, Experimental control
- Video: https://www.youtube.com/watch?v=hS1YqcewH0c
- Project page: https://developers.openai.com/api/docs/deprecations
- API docs: https://developers.openai.com/api/docs/guides/video-generation

#### Gemini API video generation (Veo, Omni) — Google, Google DeepMind (2025-04-09)
- Type: Platform / API · Timing: Pre-generated · Access: Public API
- Input: Text prompt, Image, Video → Output: Flat video, Sound, music & spatial audio
- Idea: The most complete hosted video stack for labs: model ids you can pin, preview-to-GA lifecycles you can track, and shutdown notices that tell you when a stimulus model will go away.
- What it is: Google's Gemini API and Vertex AI (documented in 2026 as the Gemini Enterprise Agent Platform) serve DeepMind's video models as versioned endpoints: Veo 2 from April 2025, Veo 3 and 3.1 with native audio, 4K output from January 2026 and Veo 3.1 Lite from March 2026. In 2026 Google added Gemini Omni Flash, a conversational video generation and editing model (preview 2026-06-30, GA 2026-08-27).
- How it works: Long-running prediction operations on model ids such as veo-3.1-generate-preview and gemini-omni-1.1-flash; Google marks Veo output with SynthID watermarks.
- Specs: Veo 3.1: 4 / 6 / 8 s · 720p–4K · native audio · Omni Flash: 360p–4K, extend, first + last frame
- Capability: Authoring accessibility, Experimental control
- Video: https://www.youtube.com/watch?v=Co-97Ht5vAY
- Images: https://ai.google.dev/static/site-assets/images/share-gemini-api-2026-07.png
- Project page: https://ai.google.dev/gemini-api/docs/changelog
- API docs: https://ai.google.dev/gemini-api/docs/video

#### Kling AI API (KlingAI Open Platform) — Kuaishou (2024)
- Type: Platform / API · Timing: Pre-generated · Access: Public API
- Input: Text prompt, Image, Video → Output: Flat video, Image / panorama
- Idea: Puts a Chinese frontier video model behind the same kind of versioned API as Veo or Ray, so cross-lab stimulus comparisons do not have to go through a consumer app.
- What it is: Kuaishou's KlingAI Open Platform gives developers API access to the Kling video and image models, with per-model references and unit pricing. Along with resellers such as fal, it is one of the main routes by which a Chinese frontier video model reaches third-party apps worldwide.
- How it works: Asynchronous REST tasks (text-to-video, image-to-video, extension) signed with access and secret keys; results return as hosted video URLs.
- Specs: API since 2024 · v1.5 1080p professional mode and video extension added 2024-11
- Capability: Authoring accessibility, Perceptual realism
- Video: https://www.youtube.com/watch?v=mT5aHJxnqx0
- Project page: https://app.klingai.com/global/dev/document-api/quickStart/productIntroduction/overview
- API docs: https://app.klingai.com/global/dev/document-api/quickStart/productIntroduction/overview

#### Luma API (Ray) — Luma AI (2024)
- Type: Platform / API · Timing: Pre-generated · Access: Public API
- Input: Text prompt, Image, Video → Output: Flat video, Image / panorama
- Idea: Keyframe-level control through an API is what turns a video model into something an experimenter can script shot by shot.
- What it is: Luma's API serves its Ray video models and Photon image models to developers. The Ray3.2 API (2026-06-09) exposes the model's full control surface: up to 16 keyframes per clip, performance tracking, HDR generation and EXR export.
- How it works: Asynchronous generation jobs on Luma's Ray video models with multi-keyframe conditioning, video-to-video and reframing endpoints.
- Specs: Ray3.2 API (2026-06-09) · up to 16 keyframes per clip · HDR · EXR export
- Capability: Experimental control, Authoring accessibility
- Video: https://www.youtube.com/watch?v=YawXSpOlzgw
- Images: https://cdn.sanity.io/images/2ylxvaa2/production/ff7469d468f6f7e447ccb4a50276f1cb03c6664d-1200x630.jpg?w=1200&h=630&fm=jpg
- Project page: https://lumalabs.ai/api
- API docs: https://docs.lumalabs.ai

#### Runway API (Runway Dev) — Runway (2024-09)
- Type: Platform / API · Timing: Pre-generated · Access: Public API
- Input: Text prompt, Image, Video → Output: Flat video, Virtual human (face / body), Sound, music & spatial audio
- Idea: One integration covers pre-rendered clips and live conversational characters, so a study can move between offline and real-time stimuli without changing vendor.
- What it is: Runway's developer platform serves its own video, image and audio models and models from other labs through one API, with a model router, reusable workflows and real-time conversational 'Characters'. Runway ran its first online API hackathon in May 2026 around real-time video agents.
- How it works: REST task API with SDKs; a router picks a model per request from a cost, latency or quality preference, and Characters stream in real time (likely over WebRTC).
- Specs: launched 2024-09 · credit-based billing · model router · real-time Characters
- Capability: Authoring accessibility, Temporal responsiveness
- Video: https://www.youtube.com/watch?v=rV81E4TntkI
- Images: https://d3phaj0sisr2ct.cloudfront.net/devportal/og-image-v4.jpg
- Project page: https://runwayml.com/api
- API docs: https://docs.dev.runwayml.com/

#### fal — fal (2023)
- Type: Platform / API · Timing: Pre-generated · Access: Public API
- Input: Text prompt, Image, Video → Output: Flat video, Mesh / 3D asset, Sound, music & spatial audio
- Idea: Lets a lab swap the generator behind a stimulus pipeline by changing one parameter, which makes model comparisons cheap but ties reproducibility to a third party's catalogue.
- What it is: A generative-media inference host: one API and SDK for more than 1,000 image, video, audio and 3D models from many labs (Kling, Seedance, MiniMax, FLUX and open-weight models), plus serverless GPUs to deploy your own. fal reports more than 1.5 million developers as of October 2026.
- How it works: Queued and streaming HTTP / WebSocket endpoints in front of optimized inference on H100, H200 and B200 clusters; custom models deploy as serverless apps.
- Specs: 1,000+ models · billed per output · serverless and dedicated GPUs
- Capability: Authoring accessibility, Temporal responsiveness
- Video: https://www.youtube.com/watch?v=fcBfGnpUKjI
- Images: https://fal.ai/og-thumbnail.webp
- Project page: https://fal.ai
- API docs: https://docs.fal.ai
- Code: https://github.com/fal-ai/fal

#### Volcano Engine Ark / BytePlus ModelArk — Volcano Engine (BytePlus) (2023-06-28)
- Type: Platform / API · Timing: Pre-generated · Access: Public API
- Input: Text prompt, Image → Output: Flat video, Dialogue / text
- Idea: The official route to ByteDance's Seedance models, with enterprise terms that matter when a study needs a stable endpoint it can contract for.
- What it is: ByteDance's model-as-a-service platform (Volcano Engine Ark in China, BytePlus ModelArk internationally) serves the Doubao language models and the Seedance video models through an API. BytePlus added first- and last-frame control for Seedance 1.0 Pro on ModelArk in 2025 and lists Seedance 2.0 and 2.5 in 2026.
- How it works: Managed inference endpoints with REST APIs, model versions and quotas; video jobs run asynchronously and return hosted MP4 files.
- Specs: launched 2023-06-28 (China) · Seedance 1.0 Pro first/last-frame control (2025) · Seedance 2.0 / 2.5 (2026)
- Capability: Authoring accessibility, Experimental control
- Video: https://www.youtube.com/watch?v=pBUvj5USz1Y
- Project page: https://www.volcengine.com/product/ark
- API docs: https://docs.byteplus.com/en/docs/ModelArk

#### Replicate — Replicate (2021)
- Type: Platform / API · Timing: Pre-generated · Access: Public API, Open weights / code
- Input: Text prompt, Image, Video → Output: Flat video, Mesh / 3D asset, Image / panorama
- Idea: Version ids per model make it one of the easier hosts on which to pin the exact generator a study used.
- What it is: Runs thousands of open and proprietary models behind one API, each addressed by a version id, and lets developers publish their own models packaged with the open-source Cog container format. Replicate announced on 2025-11-17 that it is joining Cloudflare; it keeps its brand and its API.
- How it works: Models packaged as Cog containers run on Replicate's GPU fleet; each prediction is an HTTP job addressed by a model version.
- Specs: thousands of models · per-second GPU or per-output billing · joining Cloudflare (announced 2025-11-17)
- Capability: Experimental control, Authoring accessibility
- Video: https://www.youtube.com/watch?v=VmYYcGtbF8E
- Images: https://replicate.com/blog/replicate-cloudflare.png
- Project page: https://replicate.com/blog/replicate-cloudflare
- API docs: https://replicate.com/docs
- Code: https://github.com/replicate/cog

### Real-time media & agent stacks

WebRTC, voice-agent and streaming frameworks that carry full-duplex interaction.

#### Agora Conversational AI Engine — Agora (2025-04)
- Type: Platform / API · Timing: Full-duplex · Access: Public API
- Input: Speech & audio, Text prompt → Output: Speech / voice, Dialogue / text, Virtual human (face / body)
- Idea: Network-level robustness (packet loss, noisy rooms) matters as much as model latency once virtual humans run outside the lab.
- What it is: A hosted service that drops a voice agent into an Agora real-time channel: developers bring any LLM and text-to-speech, and Agora handles audio transport over its global network, noise suppression, interruption and turn-taking. The same channel can carry a digital-human avatar from partner vendors.
- How it works: REST calls start an agent that joins an Agora SD-RTN channel, runs speech recognition, an LLM and text-to-speech (or a speech-to-speech model) in a managed pipeline, and streams speech back into the channel.
- Specs: launched 2025 · bring-your-own LLM and TTS · Agora SD-RTN global network
- Capability: Temporal responsiveness, Reactivity
- Video: https://www.youtube.com/watch?v=B0nacrYT5bU
- Images: https://cdn.prod.website-files.com/661e75fc70756be16764754b/6a5f42861fc82c4cd5e27a2f_Products%20_%20Conversational%20AI%20Engine.png
- Project page: https://www.agora.io/en/products/conversational-ai-engine/
- API docs: https://docs.agora.io/en/conversational-ai/overview/product-overview

#### Gemini Live API — Google, Google DeepMind (2024-12-11)
- Type: Platform / API · Timing: Full-duplex · Access: Public API
- Input: Speech & audio, Video, Text prompt → Output: Speech / voice, Dialogue / text
- Idea: Because it watches video while it talks, it can react to what a participant does in front of the camera, not only to what they say.
- What it is: Google's bidirectional streaming API for voice-and-vision agents: an app streams microphone audio and camera or screen video to Gemini over a WebSocket and gets spoken replies the user can interrupt. It launched as the Multimodal Live API with Gemini 2.0 in December 2024; since 2026-09-15 the default models are Gemini 3.8 Live and Gemini 3.8 Live Extended Thinking, with asynchronous function calling and proactive audio.
- How it works: Stateful WebSocket sessions to native audio-to-audio Gemini models with voice-activity detection, session resumption, context compression and tool calls; ephemeral tokens let browsers connect directly.
- Specs: audio + video in · audio out · GA models gemini-3.8-live and gemini-3.8-live-extended-thinking (2026-09-15)
- Capability: Temporal responsiveness, Reactivity
- Video: https://www.youtube.com/watch?v=3CyW24Pkz4o
- Project page: https://ai.google.dev/gemini-api/docs/live-api
- API docs: https://ai.google.dev/gemini-api/docs/live-api

#### OpenAI Realtime API and GPT-Live — OpenAI (2024-10-01)
- Type: Platform / API · Timing: Full-duplex · Access: Public API
- Input: Speech & audio, Text prompt, Image → Output: Speech / voice, Dialogue / text
- Idea: Separates the voice that keeps a conversation going from the reasoning that decides what a character does, the architecture a responsive virtual confederate needs.
- What it is: OpenAI's low-latency speech-to-speech interface over WebRTC, WebSocket or SIP: beta at DevDay 2024, generally available on 2025-08-28 with gpt-realtime, then gpt-realtime-2 (2026-05-07) and 2.1 (2026-07-06). On 2026-09-10 OpenAI made GPT-Live 1 generally available, a full-duplex voice layer that keeps talking while a separate backend model or agent runs tools ('delegation').
- How it works: Persistent sessions stream audio in and out of a native audio model; server-side voice-activity detection handles turn-taking and interruption, and function calls or delegated backend tasks run while audio continues.
- Specs: WebRTC / WebSocket / SIP · beta 2024-10-01 · GA 2025-08-28 · beta interface removed 2026-05-12 · GPT-Live 1 GA 2026-09-10
- Capability: Temporal responsiveness, Reactivity
- Video: https://www.youtube.com/watch?v=qGS9Ghnq1RU
- Project page: https://developers.openai.com/api/docs/guides/realtime
- API docs: https://developers.openai.com/api/docs/guides/live

#### TEN Framework — Agora (2024-06)
- Type: Open-source tool · Timing: Full-duplex · Access: Open weights / code
- Input: Speech & audio, Video, Text prompt → Output: Speech / voice, Dialogue / text, Virtual human (face / body)
- Idea: Open turn-detection and VAD models matter because when a virtual human decides to speak is itself an experimental variable.
- What it is: An open-source framework, supported by Agora and its community, for real-time multimodal conversational agents. It ships TEN Agent demos, its own voice-activity-detection and turn-detection models, and connectors for RTC and WebSocket transport; the latest release is 0.11.73 (2026-09-22).
- How it works: A graph of extensions written in C++, Go, Python or Node.js runs inside one runtime and exchanges audio, video and data messages with low overhead.
- Specs: ~11.2k GitHub stars (Oct 2026) · TEN VAD and TEN Turn Detection models · RTC and WebSocket
- Capability: Temporal responsiveness, Experimental control
- Video: https://www.youtube.com/watch?v=yYg07CbPZfg
- Images: https://opengraph.githubassets.com/1/TEN-framework/ten-framework
- Project page: https://theten.ai/
- Code: https://github.com/TEN-framework/ten-framework

#### Pipecat — Daily (2024-05)
- Type: Open-source tool · Timing: Full-duplex · Access: Open weights / code, Public API
- Input: Speech & audio, Video, Text prompt → Output: Speech / voice, Dialogue / text, Virtual human (face / body)
- Idea: A frame-level pipeline makes every stage of a conversational stimulus explicit and swappable, which helps when a study must report which models produced what.
- What it is: An open-source Python framework, maintained by Daily, for voice and multimodal agents built as pipelines of frames passing through speech, LLM, video and avatar services; Pipecat Flows adds structured conversation graphs and Pipecat Cloud hosts agents. Pipecat 1.0 shipped on 2026-04-14 and 1.12 on 2026-09-26.
- How it works: Asynchronous pipelines of processors exchange audio, video, text and control frames over transports such as Daily WebRTC, WebSocket or telephony; Flows encode dialogue states and transitions.
- Specs: ~16.6k GitHub stars (Oct 2026) · v1.0.0 on 2026-04-14 · v1.12.0 on 2026-09-26
- Capability: Temporal responsiveness, Experimental control
- Video: https://www.youtube.com/watch?v=tAQW319_h-s
- Images: https://opengraph.githubassets.com/1/pipecat-ai/pipecat
- Project page: https://docs.pipecat.ai/getting-started/introduction
- API docs: https://docs.pipecat.ai
- Code: https://github.com/pipecat-ai/pipecat

#### LiveKit Agents — LiveKit (2023-11)
- Type: Open-source tool · Timing: Full-duplex · Access: Open weights / code, Public API
- Input: Speech & audio, Video, Text prompt → Output: Speech / voice, Dialogue / text, Virtual human (face / body)
- Idea: The plumbing that lets a researcher swap the voice, model or avatar of a virtual human while keeping the same room, logging and timing behavior.
- What it is: An open-source framework for real-time voice, video and physical-AI agents that join LiveKit WebRTC rooms as participants. It wires speech-to-text, LLM and text-to-speech (or speech-to-speech) models and avatar providers into one session, with turn detection, interruption handling, telephony and evaluation tools; 1.0 shipped on 2025-04-10 and 1.8.8 on 2026-10-15, and LiveKit Cloud hosts deployments.
- How it works: Python and Node.js workers connect to a LiveKit media server over WebRTC; a pipeline of plugins (STT, LLM, TTS, VAD and a transformer turn-detection model) or a realtime model handles each conversation.
- Specs: ~14.8k GitHub stars (Oct 2026) · 1.0 on 2025-04-10 · 1.8.8 on 2026-10-15
- Capability: Temporal responsiveness, Experimental control
- Video: https://www.youtube.com/watch?v=OZG0oZKctgw
- Images: https://livekit.com/opengraph-image.png?opengraph-image.10qgazecccxaz.png
- Project page: https://docs.livekit.io/agents/
- API docs: https://docs.livekit.io/agents/
- Code: https://github.com/livekit/agents

### Engines, runtimes & viewers

Game engines, WebXR and splat renderers that put generated content in front of people.

#### Roblox Build and AI creation tools — Roblox (2026-09-11)
- Type: Platform / API · Timing: Turn-based · Access: Product / app, Waitlist / early access
- Input: Text prompt, Image → Output: 3D scene / world, Mesh / 3D asset, Agent behaviour & actions
- Idea: Prompt-to-game on a platform with 29 billion play-hours a quarter means generated situations reach players at scale, a recruitment and ecological-validity channel as much as a tool.
- What it is: At RDC 2026 (2026-09-11) Roblox described an 'AI creation layer' on its engine: Build, a tab in the Roblox app where anyone makes a game from prompts (about 9,000 games published in its New Zealand alpha, now expanding to Serbia and Singapore), and Scene Generator, due later in 2026, which turns a text prompt plus a reference image into a functional layout editable in Studio. These sit alongside Studio's Assistant and the open Cube 3D model.
- How it works: LLM agents and generative 3D models (Cube) likely produce Luau scripts, assets and layouts inside Roblox's engine and cloud services; games publish instantly to Roblox's multiplayer infrastructure.
- Specs: Build alpha: ~9,000 games by 2026-09-01; 71% of Build creators had never used Studio · Scene Generator: later 2026
- Capability: Authoring accessibility, Co-creation & agency
- Video: https://www.youtube.com/watch?v=AD3I2Vw7l5M
- Images: https://cms-media.roblox.com/assets/ced9560d-5aa5-42d3-b5d8-8e70abeac00c.png
- Project page: https://corp.roblox.com/newsroom/2026/09/rdc-2026-the-world-needs-more-play

#### glTF Gaussian Splatting extension (KHR_gaussian_splatting) — The Khronos Group (2026-02-03)
- Type: Platform / API · Timing: Pre-generated · Access: Open weights / code
- Input:  → Output: Gaussian splats / radiance field
- Idea: A shared file format is what lets a generated world move unchanged from the model that made it to whichever engine runs the study.
- What it is: A Khronos extension that stores 3D Gaussian splats (position, rotation, scale, opacity and spherical-harmonic color) as glTF 2.0 mesh primitives, giving engines and viewers a common baseline format. Khronos released it as a release candidate for industry feedback on 2026-02-03; as of October 2026 the spec is marked complete and ratified, with compression left to future extensions.
- How it works: Extends glTF mesh primitives with per-point attributes for Gaussian parameters and a defined rendering model, so splat scenes travel with standard glTF tooling.
- Specs: release candidate 2026-02-03 · ratified (status as of Oct 2026) · glTF 2.0 · uncompressed baseline
- Capability: Experimental control, Authoring accessibility
- Video: https://www.youtube.com/watch?v=EEFIxtBRRBo
- Images: https://www.khronos.org/assets/uploads/apis/gltf-Square.png
- Project page: https://www.khronos.org/news/press/gltf-gaussian-splatting-press-release
- Code: https://github.com/KhronosGroup/glTF/tree/main/extensions/2.0/Khronos/KHR_gaussian_splatting

#### Immersive Web SDK (IWSDK) — Meta (2025)
- Type: Open-source tool · Timing: Real-time streaming · Access: Open weights / code
- Input: Scene spec, code & rules, Body, face & gaze tracking → Output: 3D scene / world
- Idea: Agent-operable XR scenes mean an LLM can build and test a study environment end to end, not only write the code for it.
- What it is: Meta's open-source framework for WebXR apps built on Three.js: an entity-component runtime with grab interactions, locomotion, spatial audio, physics, scene understanding and HTML-like spatial UI, plus a Spatial Editor. As of October 2026 its site calls it 'AI-native': coding agents can take screenshots, send controller input and inspect the running XR scene to debug it.
- How it works: Three.js renderer under an entity-component architecture, with UIKitML for spatial UI and an agent tool interface for scene inspection and simulated input.
- Specs: v1.0.1 · Three.js-based · Spatial Editor
- Capability: Authoring accessibility
- Video: https://www.youtube.com/watch?v=d1PwLkvgP7A
- Images: https://opengraph.githubassets.com/1/facebook/immersive-web-sdk
- Project page: https://iwsdk.dev/
- Code: https://github.com/facebook/immersive-web-sdk

#### Unity AI tools (Unity AI) — Unity (2025-08)
- Type: Platform / API · Timing: Turn-based · Access: Product / app, Waitlist / early access
- Input: Text prompt, Image, Scene spec, code & rules → Output: 3D scene / world, Mesh / 3D asset
- Idea: When an agent can edit the scene graph directly, a scenario script and its 3D implementation can be revised in the same conversation.
- What it is: Unity's AI tooling for its engine: an agentic in-editor assistant that reads the open scene and performs editor actions, an AI gateway, an MCP server and CLI, and official plugins for Claude Code, Codex and Grok. The Unity AI open beta opened to all Unity 6+ developers on 2026-05-04; Unity has since retired the 'Unity AI' brand name, and on 2026-10-07 Unity announced Unity Spark, a no-code, prompt-driven game maker, as a closed beta.
- How it works: An LLM agent with Unity-specific tools and project context (scene hierarchy, components, assets) issues Editor commands; external agents connect through MCP via the Unity CLI.
- Specs: Unity 6+ · CLI, MCP server and plugins free · in-editor assistant in Pro / Enterprise / Industry, $10/month for Personal after trial · open beta 2026-05-04
- Capability: Authoring accessibility
- Video: https://www.youtube.com/watch?v=pHRZm2BwNQc
- Images: https://cdn.sanity.io/images/fuvbjjlp/production/b55d23a7301a66deab7adb111442c13cb6510919-3840x2160.png
- Project page: https://unity.com/products/ai

#### NVIDIA Omniverse NuRec — NVIDIA (2025-06)
- Type: Platform / API · Timing: Pre-generated · Access: Product / app
- Input: Multi-view capture / scan, Video → Output: Gaussian splats / radiance field, 3D scene / world
- Idea: A route from a real place to a controllable simulation: reconstruct a site once, then let generative models vary conditions while the geometry stays fixed.
- What it is: NVIDIA's neural-reconstruction libraries for Omniverse: they turn camera and lidar captures into 3D Gaussian-splat scenes packaged as OpenUSD and render them inside simulators (Isaac Sim, CARLA, AlpaSim). NVIDIA pairs NuRec with its Cosmos world models to generate variations of the reconstructed scenes.
- How it works: Gaussian-splat reconstruction from multi-sensor logs (built on open-source gsplat, per NVIDIA), exported to OpenUSD with trajectories through the NCore data standard.
- Specs: OpenUSD output · camera + lidar input · integrations: Isaac Sim, CARLA, AlpaSim
- Capability: Perceptual realism, Situational reach, Experimental control
- Video: https://www.youtube.com/watch?v=e3dfXj6ATA0
- Project page: https://developer.nvidia.com/omniverse/nurec

#### Android XR SDK (Jetpack XR) — Google (2024-12-12)
- Type: Platform / API · Timing: Real-time streaming · Access: Waitlist / early access
- Input: Body, face & gaze tracking, Passthrough & live surroundings, Speech & audio → Output: 3D scene / world
- Idea: One Android toolchain spans headsets and glasses, so a study app can follow participants from full immersion to heads-up overlays.
- What it is: Google's SDK for Android XR apps on headsets (Galaxy XR), wired XR glasses (XREAL AURA) and AI glasses: Jetpack Compose for XR, SceneCore, ARCore for Jetpack XR (plane and object tracking with semantic labels), and Unity, OpenXR and WebXR paths. As of October 2026 it is at Developer Preview 4.
- How it works: Kotlin Jetpack libraries over an OpenXR-based perception stack, with Gemini APIs available to apps on the device.
- Specs: Developer Preview 4 (2026) · targets Galaxy XR, XREAL AURA, AI glasses · Unity / OpenXR / WebXR
- Capability: Authoring accessibility, Situational reach
- Video: https://www.youtube.com/watch?v=otzSN5pSNZk
- Project page: https://developer.android.com/develop/xr
- API docs: https://developer.android.com/develop/xr/jetpack-xr-sdk

#### Meta Spatial SDK — Meta (2024-09-25)
- Type: Platform / API · Timing: Real-time streaming · Access: Product / app
- Input: Body, face & gaze tracking, Passthrough & live surroundings, Scene spec, code & rules → Output: 3D scene / world
- Idea: Lowers the cost of a mixed-reality study app to that of an Android app, including access to the headset camera for AI that reads the participant's surroundings.
- What it is: Meta's Kotlin / Android framework for building Horizon OS apps on Quest without a game engine: 2D Android panels, 3D glTF content, mixed-reality scene understanding and passthrough camera access in one entity-component runtime, with a desktop Spatial Editor. It lets mobile developers add mixed-reality features, including AI that reads the passthrough camera feed, to existing apps.
- How it works: Entity-component-system scene graph with a physically based renderer, the Android activity lifecycle, and Horizon OS mixed-reality APIs (scene, anchors, passthrough camera).
- Specs: Kotlin / Android · Quest 3 and 3S · Spatial Editor · announced 2024-09-25
- Capability: Authoring accessibility, Situational reach
- Video: https://www.youtube.com/watch?v=6aKbrPp09jo
- Images: https://opengraph.githubassets.com/1/meta-quest/Meta-Spatial-SDK-Samples
- Project page: https://github.com/meta-quest/Meta-Spatial-SDK-Samples
- Code: https://github.com/meta-quest/Meta-Spatial-SDK-Samples

#### Unreal Engine 5 — Epic Games (2022-04-05)
- Type: Platform / API · Timing: Real-time streaming · Access: Product / app
- Input: Scene spec, code & rules, Video → Output: 3D scene / world, Virtual human (face / body), Motion / animation
- Idea: Gives generated content a photoreal, deterministic runtime: the generative layer can sit in MetaHumans and scripts while the engine keeps timing and logging exact.
- What it is: Epic's real-time engine behind many high-fidelity VR studies and virtual-production stages, with Nanite geometry, Lumen lighting and MetaHuman digital humans. Unreal Engine 5.8 (2026-06-23) added MetaHuman Collections for crowds of hundreds, full-body markerless MetaHuman capture from a webcam, open-source OpenRigLogic (MIT) and an experimental MCP plugin that lets any LLM inspect and drive the editor.
- How it works: C++ engine with Blueprint visual scripting; Nanite virtualized geometry and Lumen global illumination render in real time, and MetaHuman tools rig and animate scanned or generated characters.
- Specs: UE 5.0 released 2022-04-05 · UE 5.8 released 2026-06-23 · free, 5% royalty above $1M gross for games
- Capability: Perceptual realism, Authoring accessibility, Experimental control
- Video: https://www.youtube.com/watch?v=ExFF5gXVhDU
- Images: https://cms-assets.unrealengine.com/AiKUh5PQCTaOFnmJDZJBfz/resize=width:1200/cmqhyducc6qq007n7n99x5sjf
- Project page: https://www.unrealengine.com/en-US/news/unreal-engine-5-8-is-now-available

#### WebXR Device API — W3C Immersive Web Working Group (2019)
- Type: Platform / API · Timing: Real-time streaming · Access: Open weights / code
- Input: Body, face & gaze tracking, Passthrough & live surroundings, Keyboard & controller actions → Output: 3D scene / world, 360° / stereo video
- Idea: The lowest-friction delivery path for a generated scene: a URL that opens in a headset, which also makes remote and large-sample XR studies feasible.
- What it is: The W3C web standard that lets a page open immersive VR and AR sessions on headsets and phones, with pose tracking, controller and hand input, and AR modules for hit testing, anchors and depth. Chromium browsers (including Meta Quest Browser and Chrome on Android XR) and Safari on visionOS implement it; the core spec is a W3C Candidate Recommendation Draft, latest dated 2026-06-09.
- How it works: A JavaScript API that supplies per-frame viewer and input poses and an XR-compatible WebGL / WebGPU layer to render into; feature modules add AR capabilities.
- Specs: W3C Candidate Recommendation Draft (2026-06-09) · editors from Google and Meta
- Capability: Situational reach, Authoring accessibility
- Video: https://www.youtube.com/watch?v=C3XDHjam-eI
- Images: https://opengraph.githubassets.com/1/immersive-web/webxr
- Project page: https://www.w3.org/TR/webxr/
- API docs: https://www.w3.org/TR/webxr/
- Code: https://github.com/immersive-web/webxr

#### PlayCanvas Engine — PlayCanvas (2014)
- Type: Open-source tool · Timing: Real-time streaming · Access: Open weights / code
- Input: Scene spec, code & rules → Output: Gaussian splats / radiance field, 3D scene / world
- Idea: Generated worlds can ship as a link: a participant opens a splat scene in a desktop or headset browser with nothing to install.
- What it is: An MIT-licensed web graphics runtime (WebGL, WebGPU, WebXR, glTF) that has become one of the main browser renderers for Gaussian splats; PlayCanvas, owned by Snap, also builds the SuperSplat editor. Engine 2.20 (June 2026) added splat relighting, soft shadows and depth of field, streaming of scenes with billions of splats, and WebXR on WebGPU.
- How it works: JavaScript / TypeScript engine with an entity-component system, a GPU splat renderer that sorts and rasterizes Gaussians, and WebXR session support.
- Specs: MIT · ~17k GitHub stars (Oct 2026) · v2.20 (2026-06) · billions of splats via streaming (PlayCanvas claim)
- Capability: Perceptual realism, Authoring accessibility
- Video: https://www.youtube.com/watch?v=gsLkNo-PBF4
- Images: https://playcanvas.com/assets/images/og/playcanvas.png
- Project page: https://playcanvas.com
- Code: https://github.com/playcanvas/engine

#### Babylon.js — Microsoft (2013)
- Type: Open-source tool · Timing: Real-time streaming · Access: Open weights / code
- Input: Scene spec, code & rules → Output: 3D scene / world, Gaussian splats / radiance field
- Idea: A second mature open web engine for splat and WebXR delivery, useful when a study needs browser-based 3D without lock-in to one vendor.
- What it is: Microsoft's open-source (Apache-2.0) JavaScript rendering and game engine for the web, with WebXR, WebGPU and Gaussian-splat support. Babylon.js 9.0 shipped on 2026-03-26.
- How it works: TypeScript engine with a node-based material editor, physics, WebXR experience helpers and a splat renderer, running on WebGL2 or WebGPU.
- Specs: Apache-2.0 · ~26k GitHub stars (Oct 2026) · v9.0 (2026-03-26)
- Capability: Authoring accessibility, Perceptual realism
- Video: https://www.youtube.com/watch?v=Th9mD_D5DrQ
- Images: https://www.babylonjs.com/assets/videos/newGaussianSplat.jpg
- Project page: https://www.babylonjs.com
- API docs: https://doc.babylonjs.com
- Code: https://github.com/BabylonJS/Babylon.js

### Headsets, glasses & displays

The hardware generated worlds are delivered on.

#### Steam Frame — Valve (2025-11-12)
- Type: Device · Access: Product / app
- Input: Body, face & gaze tracking, Keyboard & controller actions → Output: 3D scene / world, Authored VR scenario
- Idea: Wireless PC streaming lets a headset show worlds generated on a desktop GPU, which matters while real-time world models still need workstation or datacenter hardware.
- What it is: Valve's standalone, streaming-first VR headset, announced on 2025-11-12 and sold from September 2026 ($1,059 for 256 GB, $1,299 for 1 TB). It runs SteamOS on a Snapdragon 8 Gen 3 and streams PC VR wirelessly with eye-tracked foveated streaming; it ships no generative features of its own but brings PC-rendered worlds to a wireless headset.
- How it works: Snapdragon 8 Gen 3 with 16 GB LPDDR5X, 2160×2160 LCD per eye, inside-out tracking, eye tracking, and a dedicated wireless adapter for PC streaming.
- Specs: 2160×2160 LCD per eye · 72–144 Hz · Snapdragon 8 Gen 3 · 16 GB · $1,059 / $1,299
- Capability: Perceptual realism
- Video: https://www.youtube.com/watch?v=OmKrKTwtukE
- Images: https://clan.fastly.steamstatic.com/images/45479024/41ac1feaa13a1396844a31be91beb068eb2e509f.jpg
- Project page: https://store.steampowered.com/sale/steamframe

#### Samsung Galaxy XR — Samsung Electronics, Google (2025-10-21)
- Type: Device · Access: Product / app
- Input: Speech & audio, Body, face & gaze tracking, Passthrough & live surroundings → Output: 3D scene / world, 360° / stereo video
- Idea: The first mass-market headset whose operating system generates spatial content from flat media by default.
- What it is: The first Android XR headset, made by Samsung with Google and Qualcomm and launched on 2025-10-21 at $1,799.99. It ships Gemini as a multimodal assistant that sees what the wearer sees, Media Auto-Spatialization that turns 2D photos and videos into 3D, and immersive Google Maps.
- How it works: Snapdragon XR2+ Gen 2 with micro-OLED displays, eye and hand tracking, and an external battery pack.
- Specs: Snapdragon XR2+ Gen 2 · micro-OLED, 3,552×3,840 per eye · $1,799.99 · launched 2025-10-21 (US, Korea)
- Capability: Perceptual realism, Situational reach
- Video: https://www.youtube.com/watch?v=MPwZscUoly4
- Project page: https://www.samsung.com/us/xr/galaxy-xr/galaxy-xr/
- API docs: https://developer.android.com/develop/xr

#### Apple Vision Pro (M5) — Apple (2025-10-15)
- Type: Device · Access: Product / app
- Input: Body, face & gaze tracking, Speech & audio, Passthrough & live surroundings → Output: 360° / stereo video, 3D scene / world, Virtual human (face / body)
- Idea: The highest-fidelity mainstream display for generated scenes and video, with eye and hand tracking built in, at a price that limits lab fleets.
- What it is: Apple's mixed-reality headset, upgraded on 2025-10-15 with the M5 chip, refresh rates up to 120 Hz and the Dual Knit Band, at $3,499. For generated content it ships visionOS 26 Spatial Scenes (generative depth that makes a 2D photo explorable), Personas for video calls, 180° / 360° and wide-FOV video playback, and Apple Immersive video.
- How it works: Dual micro-OLED displays (23 million pixels in total) driven by M5 together with the R1 sensor chip, with eye, hand and room tracking.
- Specs: M5 + R1 · micro-OLED, 23M pixels total · up to 120 Hz · $3,499 · on sale 2025-10-22
- Capability: Perceptual realism, Situational reach
- Video: https://www.apple.com/newsroom/videos/2025/autoplay/10/apple-vision-pro-immersive-experience/large_2x.mp4
- Images: https://www.apple.com/newsroom/images/2025/10/apple-vision-pro-upgraded-with-the-m5-chip-and-dual-knit-band/tile/Apple-Vision-Pro-hero-251015-lp.jpg.og.jpg?202608191813
- Project page: https://www.apple.com/newsroom/2025/10/apple-vision-pro-upgraded-with-the-m5-chip-and-dual-knit-band/
- API docs: https://developer.apple.com/visionos/

#### Meta Ray-Ban Display — Meta (2025-09-17)
- Type: Device · Access: Product / app
- Input: Speech & audio, Body, face & gaze tracking, Passthrough & live surroundings → Output: Dialogue / text, Image / panorama
- Idea: A heads-up channel for generated text and images during everyday activity; not an immersive display, but an always-available one.
- What it is: Meta's first consumer glasses with a built-in display: a monocular full-color in-lens display in Ray-Ban frames, controlled by the Meta Neural Band EMG wristband, for $799. For generated content it shows Meta AI answers with visuals, live captions and translation, and navigation in the wearer's view.
- How it works: A projector and waveguide in the right lens, camera and microphones on the frame, and surface-EMG decoding of finger gestures at the wrist.
- Specs: monocular in-lens display, 600×600 px · $799 incl. Neural Band · US launch 2025-09-30
- Capability: Situational reach, Temporal responsiveness
- Video: https://www.youtube.com/watch?v=hrj4NQuE93M
- Images: https://about.fb.com/wp-content/uploads/2025/09/Meta-Ray-Ban-Display_Social-Share.jpg?w=1200
- Project page: https://about.fb.com/news/2025/09/meta-ray-ban-display-ai-glasses-emg-wristband/

#### SPECS (Snap consumer AR glasses) — Snap Inc. (2025-06-10)
- Type: Device · Access: Waitlist / early access
- Input: Speech & audio, Body, face & gaze tracking, Passthrough & live surroundings → Output: 3D scene / world, Dialogue / text
- Idea: Untethered AR glasses that place generated content in the wearer's real surroundings, from a company that already runs generative Lenses at phone scale.
- What it is: Snap's standalone see-through AR glasses for consumers, announced on 2025-06-10 for 2026 and launched at the SPECS event on 2026-09-16: pre-orders at $2,195 ($2,395 with a cellular case), shipping later in fall 2026 in the US, UK and France. They run SPECS OS with Lens Studio apps, including generative AI Lenses, and SPECS Intelligence, an anticipatory AI service across iPhone, Mac and the glasses.
- How it works: On-glasses compute with no puck, see-through waveguide displays, hand and voice input, with Lens Studio as the authoring tool and cloud AI services.
- Specs: pre-order $2,195 (from 2026-09-16) · ships fall 2026 (US, UK, France) · standalone, no puck
- Capability: Situational reach, Reactivity
- Video: https://www.youtube.com/watch?v=_RHEDU7neds
- Project page: https://investor.snap.com/news/news-details/2026/SPECS-Make-Computing-More-Human-with-New-Experiences-Partnerships-and-SPECS-Intelligence/default.aspx
- API docs: https://developers.snap.com/spectacles/home

#### XREAL AURA — XREAL, Google (2025-05-20)
- Type: Device · Access: Waitlist / early access
- Input: Body, face & gaze tracking, Passthrough & live surroundings, Speech & audio → Output: 3D scene / world, 360° / stereo video
- Idea: Brings full Android XR apps to glasses-weight hardware, so mixed-reality stimuli can leave the lab in a form people will wear in public.
- What it is: Optical see-through Android XR glasses (formerly Project Aura) co-developed with Google, with a compute puck on Snapdragon and Gemini assistance. As of October 2026 they are in reservation, with launch expected in fall 2026 in the US, Canada, Japan and South Korea, listed at $1,279 (12 GB / 256 GB) or $1,499 (16 GB / 512 GB).
- How it works: A Snapdragon (Reality Elite) compute puck plus an X1S spatial coprocessor in the glasses, driving 70° optical see-through displays.
- Specs: 70° FOV · Sony micro-OLED 1920×1200 per eye · 95 g · 3 ms motion-to-photon · listed $1,279 / $1,499
- Capability: Situational reach
- Video: https://www.youtube.com/watch?v=qIQ7Qga61QI
- Images: https://resource.xreal.com/www-xreal-com/images/aura/AuraPic_Mobile.webp
- Project page: https://www.xreal.com/aura
- API docs: https://developer.android.com/develop/xr

#### Meta Quest 3 / Quest 3S — Meta (2023-06-01)
- Type: Device · Access: Product / app
- Input: Body, face & gaze tracking, Passthrough & live surroundings, Keyboard & controller actions → Output: 3D scene / world, Authored VR scenario
- Idea: The default delivery device for VR studies: cheap enough to deploy in numbers, with camera access that lets generated content respond to the participant's real room.
- What it is: Meta's standalone mixed-reality headsets: Quest 3 (announced 2023-06-01, launched 2023-10-10 at $499) and the cheaper Quest 3S (2024-09-25, from $299.99), both on Snapdragon XR2 Gen 2 with color passthrough. They are widely used in VR research labs, and Horizon OS gives apps passthrough-camera access for AI and runs Meta's Hyperscape photoreal captures.
- How it works: Snapdragon XR2 Gen 2 with inside-out tracking, hand tracking and color passthrough; pancake lenses and a depth sensor on Quest 3, Fresnel lenses on Quest 3S.
- Specs: Quest 3: 2064×2208 per eye, $499 at launch · Quest 3S: 1832×1920 per eye, from $299.99
- Capability: Situational reach
- Video: https://www.youtube.com/watch?v=Exu7r2vZpcw
- Project page: https://about.fb.com/news/2023/09/meet-meta-quest-3-mixed-reality-headset/

### Datasets & benchmarks

The data these models learn from and the tests they are compared on.

#### Arena Video Arena (LMArena) — Arena (formerly LMArena) (2026-01-21)
- Type: Dataset / benchmark · Access: Product / app
- Input: Text prompt, Image → Output: Flat video
- Idea: Human pairwise preference is the closest public proxy for perceived realism, but it rewards impressive short clips, not consistency over a long interactive session.
- What it is: Arena's crowdsourced leaderboard for video generation: visitors enter a prompt, watch clips from two anonymous models side by side and vote, and the votes become ratings for text-to-video and image-to-video. It was introduced on lmarena.ai in January 2026; the company has since rebranded from LMArena to Arena (arena.ai).
- How it works: Blind pairwise comparisons from public users, aggregated with a Bradley-Terry model into ratings with confidence intervals.
- Specs: text-to-video and image-to-video leaderboards · blind pairwise votes
- Capability: Perceptual realism, Experimental control
- Video: https://www.youtube.com/watch?v=6Z1z6ztfx60
- Project page: https://arena.ai

#### WorldScore — Haoyi Duan (2025-04-01)
- Type: Dataset / benchmark · Access: Open weights / code
- Input: Text prompt, Image, Camera path / pose → Output: 3D scene / world, Flat video, Dynamic 3D / 4D
- Idea: Puts video models and explicit 3D generators on one scale for camera control and consistency, the comparison that matters when choosing a route to an explorable world.
- What it is: A unified benchmark for world generation from Stanford that evaluates 3D scene generators, 4D generators and video models on the same task: generate a sequence of scenes that follows layout and camera-trajectory instructions. It scores controllability, quality and dynamics on 3,000 test examples and keeps a public leaderboard; the paper evaluates 19 models.
- How it works: World generation decomposed into next-scene tasks with explicit camera-trajectory layouts, scored by automatic metrics for camera and object control, content alignment, 3D and photometric consistency, style, subjective quality and motion.
- Specs: 3,000 test examples · 19 models evaluated · ICCV 2025
- Capability: Persistence, Experimental control
- Paper: https://arxiv.org/abs/2504.00983 (ICCV 2025)
- Video: https://haoyi-duan.github.io/WorldScore/assets/videos/overview.mp4
- Images: https://haoyi-duan.github.io/WorldScore/assets/images/overview/dataset_overview.jpg
- Project page: https://haoyi-duan.github.io/WorldScore/
- Code: https://github.com/haoyi-duan/WorldScore

#### VBench-2.0 — Dian Zheng, Ziqi Huang (2025-03-27)
- Type: Dataset / benchmark · Access: Open weights / code
- Input: Text prompt → Output: Flat video
- Idea: Asks whether generated events obey physics and common sense, the properties that decide whether a generated situation is behaviorally plausible.
- What it is: A follow-up benchmark that tests 'intrinsic faithfulness' rather than surface quality: 18 dimensions grouped into human fidelity, controllability, creativity, physics and commonsense, scored with vision-language models, LLMs and anomaly detectors.
- How it works: Dimension-specific prompt sets evaluated by VLM / LLM judges and specialist detectors, with agreement checked against human annotations.
- Specs: 18 dimensions in 5 categories · arXiv 2025-03
- Capability: Behavioral plausibility, Experimental control
- Paper: https://arxiv.org/abs/2503.21755 (arXiv 2025)
- Video: https://www.youtube.com/watch?v=kJrzKy9tgAc
- Images: https://vchitect.github.io/VBench-2.0-project/assets/vbench/images/figures/fig_paper_teaser.jpg
- Project page: https://vchitect.github.io/VBench-2.0-project/
- Code: https://github.com/Vchitect/VBench

#### Artificial Analysis Video Arena — Artificial Analysis (2024)
- Type: Dataset / benchmark · Access: Product / app
- Input: Text prompt, Image, Video → Output: Flat video
- Idea: Puts quality ratings next to price and latency per provider, the three numbers a lab weighs when it chooses a hosted generator.
- What it is: Independent benchmarking firm Artificial Analysis runs a blind-vote arena for video models with separate text-to-video, image-to-video and video-editing leaderboards, next to price and speed comparisons across API providers. Video labs routinely cite its rankings in launch posts.
- How it works: Pairwise human preference votes on clips from shared prompts, aggregated into Elo-style ratings, alongside measured generation time and listed price per provider.
- Specs: text-to-video · image-to-video · video editing · online since at least 2024-10
- Capability: Perceptual realism, Experimental control
- Images: https://artificialanalysis.ai/opengraph-image.png?ab13fbb533329573
- Project page: https://artificialanalysis.ai/text-to-video/arena

#### 3D Arena — Dylan Ebert (2024-06)
- Type: Dataset / benchmark · Access: Open weights / code
- Input: Image → Output: Mesh / 3D asset, Gaussian splats / radiance field
- Idea: The largest public human judgement of generated 3D assets, useful for choosing which generator to trust for scene props.
- What it is: An open Hugging Face Space where people compare two anonymous image-to-3D results (meshes or Gaussian splats) generated from the same input image and vote. The 2025 paper reports 123,243 votes from 8,096 users across 19 models since its June 2024 launch, and finds preferences for Gaussian-splat and textured outputs.
- How it works: Pairwise preference voting in a web 3D viewer on the 100-prompt iso3d set, with statistical fraud detection, aggregated into Elo ratings.
- Specs: 123,243 votes · 8,096 users · 19 models · iso3d: 100 prompts
- Capability: Perceptual realism, Experimental control
- Paper: https://arxiv.org/abs/2506.18787 (arXiv 2025)
- Images: https://cdn-thumbnails.huggingface.co/social-thumbnails/spaces/3d-arena/3d-arena.png
- Project page: https://huggingface.co/spaces/dylanebert/3d-arena

#### DL3DV-10K — Lu Ling (2023-12-26)
- Type: Dataset / benchmark · Access: Open weights / code
- Input: Multi-view capture / scan, Video → Output: 3D scene / world
- Idea: Real-world scene diversity at this scale is what lets reconstruction and world models generalize beyond a handful of benchmark rooms.
- What it is: A dataset of 10,510 videos (51.2 million frames) of real indoor and outdoor scenes from 65 types of locations, with varied reflection, transparency and lighting, built to train and benchmark novel-view synthesis and 3D reconstruction. It has become a standard training source for feed-forward reconstruction and camera-controlled video models.
- How it works: Phone and drone video captures with camera poses estimated by structure-from-motion, labeled by scene complexity, plus a benchmark split for novel-view synthesis.
- Specs: 10,510 videos · 51.2M frames · 65 location types · CVPR 2024
- Capability: Situation diversity, Perceptual realism
- Paper: https://arxiv.org/abs/2312.16256 (CVPR 2024)
- Video: https://dl3dv-10k.github.io/DL3DV-10K/assets/img/teaser1080-2x.mp4
- Images: https://dl3dv-10k.github.io/DL3DV-10K/assets/img/Scene_Category_by_secondary_POI.png
- Project page: https://dl3dv-10k.github.io/DL3DV-10K/
- Code: https://github.com/DL3DV-10K/Dataset

#### VBench — Ziqi Huang (2023-11-29)
- Type: Dataset / benchmark · Access: Open weights / code
- Input: Text prompt, Image → Output: Flat video
- Idea: Breaks 'video quality' into separately measurable dimensions, though high temporal-smoothness scores can reward videos that barely move.
- What it is: A benchmark suite that scores text-to-video models on 16 dimensions such as subject consistency, motion smoothness, temporal flickering, dynamic degree and spatial relationship, each with its own prompt set and automatic evaluator checked against human preference. Its public leaderboard is cited by many video-model releases, and VBench++ (2024) adds image-to-video and trustworthiness tests.
- How it works: Per-dimension prompt suites scored by automatic metrics built on pretrained vision models (feature similarity, optical flow, detectors, aesthetic predictors), validated with human preference annotations per dimension.
- Specs: 16 dimensions · CVPR 2024 Highlight · VBench++ arXiv 2411.13503
- Capability: Experimental control, Perceptual realism
- Paper: https://arxiv.org/abs/2311.17982 (CVPR 2024)
- Video: https://www.youtube.com/watch?v=7IhCC8Qqn8Y
- Images: https://vchitect.github.io/VBench-project/assets/vbench/images/dim_results/fig_teaser_new.jpg
- Project page: https://vchitect.github.io/VBench-project/
- Code: https://github.com/Vchitect/VBench

#### Objaverse-XL — Matt Deitke (2023-07-11)
- Type: Dataset / benchmark · Access: Open weights / code
- Input:  → Output: Mesh / 3D asset
- Idea: The asset generators that furnish generated worlds learned their sense of objects largely from this corpus, including its biases and uneven licenses.
- What it is: An open dataset of more than 10 million deduplicated 3D objects (hand-modeled objects, photogrammetry scans and professional scans of historic artifacts) gathered from public sources by the Allen Institute for AI. It is a main pretraining corpus for image-to-3D and multi-view diffusion models; the paper trains Zero123-XL on more than 100 million renders from it.
- How it works: Crawling and deduplicating public 3D repositories, with metadata and rendering scripts; licenses vary per object.
- Specs: 10M+ objects · NeurIPS 2023 Datasets and Benchmarks
- Capability: Situation diversity
- Paper: https://arxiv.org/abs/2307.05663 (NeurIPS 2023 Datasets and Benchmarks)
- Video: https://objaverse.allenai.org/objaverse-xl/image-to-3d.mp4
- Images: https://objaverse.allenai.org/objaverse-xl/objaverse-xl.jpg
- Project page: https://objaverse.allenai.org/
- Code: https://github.com/allenai/objaverse-xl

#### RealEstate10K — Tinghui Zhou (2018)
- Type: Dataset / benchmark · Access: Open weights / code
- Input: Camera path / pose, Video → Output: 3D scene / world, Flat video
- Idea: Ordinary walkthrough footage with recovered camera paths is what taught view-synthesis and camera-controlled video models how indoor space unfolds as you move.
- What it is: A dataset of camera trajectories for about 10 million frames from some 80,000 clips of YouTube real-estate walkthrough videos, released by Google with the Stereo Magnification paper. It became the standard testbed for novel-view synthesis and, later, camera-controlled video generation.
- How it works: SLAM and bundle adjustment on walkthrough footage recover per-frame camera intrinsics and poses; the dataset ships poses and video ids, not the videos.
- Specs: ~10M frames · ~80K clips · SIGGRAPH 2018
- Capability: Situation diversity, Experimental control
- Paper: https://arxiv.org/abs/1805.09817 (SIGGRAPH 2018 (ACM TOG))
- Images: https://tinghuiz.github.io/projects/mpi/images/teaser.png
- Project page: https://google.github.io/realestate10k/

## Resources & links: people, institutions and websites

### Researchers

- **Albert "Skip" Rizzo** (Los Angeles, US) — Director for Medical Virtual Reality at the USC Institute for Creative Technologies, behind the Bravemind VR exposure therapy for PTSD and virtual standardized patients for clinical training. Known for: Bravemind / Virtual Iraq (2005–); SimCoach (2011); Virtual standardized patients. https://ict.usc.edu/about-us/leadership/research-leadership/albert-skip-rizzo/
- **Aleksander Holynski** (New York, US) — Professor at Columbia University who also leads a Google DeepMind team on generative 3D and world models; co-author of InstructPix2Pix, CAT3D and CAT4D, which turn a few images into 3D and 4D scenes with multi-view diffusion. Known for: CAT3D (NeurIPS 2024); CAT4D (CVPR 2025); InstructPix2Pix (CVPR 2023). https://holynski.org/
- **Alexandre Défossez** (Paris, FR) — Founding member and Chief Exploration Officer of Kyutai; lead author of Moshi and, earlier at Meta, of the EnCodec audio codec, the Demucs source separator and MusicGen. Known for: Moshi (2024); EnCodec (2022); MusicGen (NeurIPS 2023); Demucs (2019). https://ai.honu.io/
- **Angjoo Kanazawa** (Berkeley, US) — Associate professor at UC Berkeley who leads the Kanazawa AI Research (KAIR) lab; her group builds the open tools many splatting projects run on (Nerfstudio, gsplat) and methods for 4D reconstruction of people and scenes from casual video. She has advised Luma AI and Wonder Dynamics. Known for: Nerfstudio (SIGGRAPH 2023); gsplat (2024); Shape of Motion (2024); Plenoxels (CVPR 2022). https://people.eecs.berkeley.edu/~kanazawa/
- **Antonia Hamilton** (London, UK) — Professor of social neuroscience at UCL's Institute of Cognitive Neuroscience who studies imitation, gaze and nonverbal coordination in face-to-face interaction, using motion capture and virtual characters. Known for: Why and how to use virtual reality to study human social interaction (with Pan, 2018); Social neuroscience of mimicry. https://antoniahamilton.com/
- **Ashley Edwards** — Senior research scientist at Google DeepMind working on reinforcement learning and foundation world models. Her earlier work on learning latent actions from observation alone underlies Genie's latent action model, which lets a world model be trained on unlabelled video. Known for: Imitating Latent Policies from Observation (ICML 2019); Genie (ICML 2024, co-first author). https://ashedwards.github.io/
- **Ben Mildenhall** (San Francisco, US) — Co-founder of World Labs and first author of NeRF, the 2020 paper that started the neural radiance field era of view synthesis. He was a research scientist at Google Research from 2021 to 2023. Known for: NeRF (ECCV 2020); Mip-NeRF 360 (CVPR 2022); DreamFusion (ICLR 2023). https://bmild.github.io/
- **Bernhard Kerbl** (Copenhagen, DK) — First author of 3D Gaussian Splatting, which made photoreal radiance fields render in real time and set off the splatting boom. He is now a tenure-track assistant professor at the University of Copenhagen and a principal investigator associated with TU Wien. Known for: 3D Gaussian Splatting for Real-Time Radiance Field Rendering (SIGGRAPH 2023 Best Paper); A Hierarchical 3D Gaussian Representation for Real-Time Rendering of Very Large Datasets (SIGGRAPH 2024). https://snosixtyboo.github.io/
- **Bill Peebles** (San Francisco, US) — Research scientist and Head of Sora at OpenAI and co-author of the Diffusion Transformer (DiT), the architecture behind most current video models. OpenAI closed the Sora app in April 2026 and its API in September 2026, keeping Sora as a world-simulation research effort. Known for: Scalable Diffusion Models with Transformers (DiT, ICCV 2023); Sora (2024); Sora 2 (2025). https://www.wpeebles.com/
- **Botao 'Amber' Hu / 胡博涛** — Designer and researcher who directs Reality Design Lab and teaches mixed reality design at the China Academy of Art; maker of the open HoloKit headset and of this gallery. Known for: HoloKit (open-source MR headset); EchoVision; Generative Reality Inspire (2026). https://amber.botao.hu/
- **Christoph Lassner** (San Francisco, US) — Co-founder of World Labs who previously led research teams at Epic Games and Meta Reality Labs Research on interactive radiance-field reconstruction and rendering, and on 3D body models. Known for: Keep it SMPL / SMPLify (ECCV 2016); Pulsar: Efficient Sphere-based Neural Rendering (CVPR 2021). https://christophlassner.de/
- **Daniel Freeman** (Oxford, UK) — Professor of clinical psychology at the University of Oxford who uses VR to study and treat paranoia; his gameChange trial tested automated VR therapy with a virtual coach for people with psychosis. Known for: gameChange automated VR therapy trial (Lancet Psychiatry, 2022); Automated VR treatment for fear of heights (Lancet Psychiatry, 2018). https://en.wikipedia.org/wiki/Daniel_Freeman_(psychologist)
- **Eloi Alonso** — Co-founder of General Intuition and first author of DIAMOND, an open diffusion world model trained an Atari agent entirely in imagination and then generated a playable Counter-Strike map. He did his PhD with François Fleuret at the University of Geneva. Known for: DIAMOND: Diffusion for World Modeling (NeurIPS 2024 Spotlight); IRIS: Transformers are Sample-Efficient World Models (ICLR 2023). https://eloialonso.github.io/
- **Fei-Fei Li / 李飞飞** (Stanford / San Francisco, US, 1976–) — Stanford professor who created ImageNet and is co-founder and CEO of World Labs, the spatial-intelligence company behind Marble; she argues that the next step after language models is models that generate and reason about 3D worlds. Known for: ImageNet (CVPR 2009); World Labs Marble (2025); From Words to Worlds: Spatial Intelligence (essay, 2025). https://profiles.stanford.edu/fei-fei-li
- **George Drettakis** (Sophia Antipolis, FR) — Senior researcher who leads the GraphDeco group at Inria Sophia Antipolis and senior author of 3D Gaussian Splatting; decades of work on image-based rendering made the method possible. Known for: 3D Gaussian Splatting (SIGGRAPH 2023); Deep Blending for Free-Viewpoint Image-Based Rendering (SIGGRAPH Asia 2018). https://www-sop.inria.fr/members/George.Drettakis/
- **Gordon Wetzstein** (Stanford, US) — Professor at Stanford who leads the Computational Imaging Lab, working across 3D-aware generative models, neural rendering and holographic near-eye displays for AR and VR. Known for: EG3D (CVPR 2022); Holographic glasses for virtual reality (SIGGRAPH 2022); SIREN (NeurIPS 2020). https://stanford.edu/~gordonwz/
- **Guido Makransky** (Copenhagen, DK) — Professor of educational psychology at the University of Copenhagen whose CAMIL model explains when immersive VR helps learning, and whose experiments found that more presence can mean less learning. Known for: CAMIL: Cognitive Affective Model of Immersive Learning (Educational Psychology Review, 2021); Adding immersive VR to a science lab simulation causes more presence but less learning (2019). https://researchprofiles.ku.dk/en/persons/guido-makransky/
- **Hao Li / 黎顥** (Abu Dhabi, AE / Los Angeles, US, 1981–) — Co-founder and CEO of Pinscreen and professor of computer vision at MBZUAI, where he directs the Metaverse Center; he builds instant photoreal avatars and speaks often on deepfakes. Known for: paGAN (SIGGRAPH Asia 2018); Pinscreen avatars; Realistic Dynamic Facial Textures from a Single Image using GANs (ICCV 2017). https://en.wikipedia.org/wiki/Hao_Li
- **Ioannis Patras** (London, UK) — Professor of Computer Vision and Human Sensing at Queen Mary University of London and Head of Research at Tavus, where he co-authored Griffin (2026), a real-time 'human interaction model' that Tavus reports 48% of study participants took for a real person. Known for: Griffin human interaction model (Tavus, 2026); Facial expression and affect analysis. https://www.qmul.ac.uk/eecs/people/profiles/patrasioannis.html
- **Jack Parker-Holder** (London, UK) — Research Director at Google DeepMind who scales world models; he co-led Genie, Genie 2 and Genie 3, models that turn a prompt into an environment you can act in. He is also an honorary lecturer at UCL DARK. Known for: Genie: Generative Interactive Environments (ICML 2024); Genie 2 (2024); Genie 3 (2025). https://jparkerholder.github.io/
- **Jake Bruce** (London, UK) — Research scientist at Google DeepMind in London and first author of Genie, the 11B-parameter model that learned playable 2D worlds from internet gameplay videos without action labels; he also contributed to Genie 3. Known for: Genie: Generative Interactive Environments (ICML 2024 Best Paper); Genie 3 (2025). https://jakebruce.ca/
- **Jaron Lanier** (Berkeley, US, 1960–) — VR pioneer who founded VPL Research in 1985, the first company to sell VR goggles and data gloves, and who works at Microsoft; his books argue for data dignity and against using people as fuel for AI. Known for: VPL Research DataGlove and EyePhone (1980s); Dawn of the New Everything (2017); Who Owns the Future? (2013). https://www.jaronlanier.com/
- **Jean-Louis van Gelder** (Freiburg, DE) — Director at the Max Planck Institute for the Study of Crime, Security and Law in Freiburg who brought VR into criminology, most famously by having burglars walk through a virtual neighbourhood. Known for: Virtual Burglary (Journal of Research in Crime and Delinquency, 2017); Virtual Reality for Criminologists (Crime and Justice, 2023). https://csl.mpg.de/en/jean-louis-van-gelder
- **Jeremy Bailenson** (Stanford, US) — Founding director of Stanford's Virtual Human Interaction Lab; his Proteus effect and transformed social interaction studies showed how avatars change the people who wear them. Known for: The Proteus Effect (Human Communication Research, 2007); Transformed Social Interaction (2004); Experience on Demand (2018). https://vhil.stanford.edu/people/jeremy-bailenson
- **Jim Blascovich** (Santa Barbara, US) — Distinguished Professor Emeritus of psychology at UC Santa Barbara whose 2002 paper made immersive virtual environments a methodological tool for social psychology, trading off experimental control against mundane realism. Known for: Immersive virtual environment technology as a methodological tool for social psychology (Psychological Inquiry, 2002); Infinite Reality (with Bailenson, 2011). https://psych.ucsb.edu/people/emeriti/jim-blascovich
- **Jon Barron** (San Francisco, US) — Principal research scientist at Google DeepMind in San Francisco who leads a small team working mostly on NeRF; co-author of NeRF and of the Mip-NeRF and Zip-NeRF line, and of generative 3D work such as DreamFusion and CAT3D. Known for: Mip-NeRF (ICCV 2021); Zip-NeRF (ICCV 2023); CAT3D (NeurIPS 2024). https://jonbarron.info/
- **Jonathan Gratch** (Los Angeles, US) — Professor at the USC Institute for Creative Technologies who directs its Affective Computing Group; he builds computational models of emotion for virtual humans and studies why people disclose more to them. Known for: EMA: a process model of appraisal dynamics (2009); It's only a computer: virtual humans increase willingness to disclose (2014); SimSensei Kiosk (AAMAS 2014). https://people.ict.usc.edu/~gratch/
- **Joon Sung Park** (Palo Alto, US) — Computer scientist who introduced generative agents (the Smallville town of 25 LLM characters) and later simulated 1,052 real people from interviews; he now runs Simile, a Palo Alto company that sells population-scale behavioral simulations. Known for: Generative Agents (UIST 2023 Best Paper); Generative Agent Simulations of 1,000 People (2024); Social Simulacra (UIST 2022). https://www.joonsungpark.com/
- **Justin Johnson** (San Francisco, US) — Co-founder of World Labs and faculty member at the University of Michigan; known for perceptual losses for style transfer, the CLEVR reasoning benchmark and image generation from scene graphs. Known for: Perceptual Losses for Real-Time Style Transfer (ECCV 2016); CLEVR (CVPR 2017); Image Generation from Scene Graphs (CVPR 2018). https://www.worldlabs.ai/about
- **Linxi "Jim" Fan / 范麟熙** (Santa Clara, US) — Senior research scientist and lead of AI agents at NVIDIA (GEAR lab); his Minecraft agents MineDojo and Voyager showed LLM-driven agents learning open-ended skills in a game world. Known for: Voyager (2023); MineDojo (NeurIPS 2022 Outstanding Paper); Eureka (ICLR 2024). https://jimfan.me/
- **Louis-Philippe Morency** (Pittsburgh, US) — Leonardo Associate Professor at Carnegie Mellon who directs the MultiComp Lab; he co-built SimSensei, the virtual interviewer that read nonverbal cues to screen for distress, and works on multimodal models of social behavior. Known for: SimSensei Kiosk (AAMAS 2014); Multimodal Machine Learning: A Survey and Taxonomy (TPAMI 2019). https://www.cs.cmu.edu/~morency/
- **Mar Gonzalez-Franco** — Neuroscientist and computer scientist who manages a Google organization on human-AI interaction and intelligent eyewear that shaped input and interaction for Android XR; at Microsoft Research she led avatar embodiment work and the open Rocketbox avatar library. Known for: The Rocketbox Library (Frontiers in VR 2020); Avatar Embodiment questionnaire (Frontiers 2018); Android XR input and interaction. https://margonzalezfranco.github.io/
- **Maria V. Sanchez-Vives** (Barcelona, ES) — ICREA research professor at IDIBAPS in Barcelona who leads its Systems Neuroscience group and is a long-time collaborator of Mel Slater at the Event Lab; she studies presence, body ownership and how virtual bodies change behavior. Known for: From presence to consciousness through virtual reality (Nat. Rev. Neurosci., 2005); Enhancing Our Lives with Immersive Virtual Reality (Frontiers in Robotics and AI, 2016). https://ca.wikipedia.org/wiki/Mavi_S%C3%A1nchez-Vives
- **Matthias Nießner** (Munich, DE, 1986–) — Professor at TU Munich who leads the Visual Computing & AI lab and co-founded Synthesia; his group's face reenactment and Gaussian avatar work feeds both deepfake detection and drivable 3D heads. Known for: Face2Face (CVPR 2016); ScanNet (CVPR 2017); GaussianAvatars (CVPR 2024). https://niessnerlab.org/
- **Mel Slater** (Barcelona, ES) — Virtual reality researcher who leads the Event Lab at the University of Barcelona; his place illusion and plausibility account defines presence, and his virtual Milgram and bystander studies show that people respond realistically to virtual others. Known for: Place illusion and plausibility (Phil. Trans. R. Soc. B, 2009); A Virtual Reprise of the Stanley Milgram Obedience Experiments (PLoS ONE, 2006); Bystander responses to a violent incident in an immersive virtual environment (PLoS ONE, 2013). https://www.ub.edu/eventlab/EventLab/
- **Michael Bernstein** (Stanford, US) — Professor of computer science at Stanford (HCI group) and senior author of Generative Agents and Social Simulacra; he studies how simulated people can be used, and misused, to prototype social systems. Known for: Generative Agents (UIST 2023); Social Simulacra (UIST 2022); Generative Agent Simulations of 1,000 People (2024). https://hci.stanford.edu/msb/
- **Michael J. Black** (Tübingen, DE) — Founding director of the Perceiving Systems department at the Max Planck Institute for Intelligent Systems and co-founder of Meshcapade; his SMPL body model is the common skeleton of most 3D human generation and motion research. Known for: SMPL (SIGGRAPH Asia 2015); SMPL-X (CVPR 2019); AMASS (ICCV 2019). https://en.wikipedia.org/wiki/Michael_J._Black
- **Neil Zeghidour** (Paris, FR) — Co-founder of the Paris lab Kyutai and CEO of its voice spin-off Gradium (December 2025); co-author of SoundStream, AudioLM and Moshi, the first open full-duplex speech model that listens while it talks. Known for: SoundStream (2021); AudioLM (2022); Moshi (2024). https://scholar.google.com/citations?user=fiJamZ0AAAAJ
- **Noah Snavely** (New York, US) — Professor at Cornell Tech and researcher at Google DeepMind whose work runs from Photo Tourism (2006) to the RealEstate10K camera-path dataset and 4D reconstruction of casual videos, data that most camera-controlled video and scene models now train on. Known for: Photo Tourism (SIGGRAPH 2006); Stereo Magnification / RealEstate10K (SIGGRAPH 2018); MegaSaM (CVPR 2025). https://www.cs.cornell.edu/~snavely/
- **Percy Liang** (Stanford, US) — Stanford professor and director of the Center for Research on Foundation Models (CRFM); co-author of Generative Agents and the 1,000-people simulation, and of the HELM evaluation framework. Known for: HELM (2022); Generative Agents (UIST 2023); On the Opportunities and Risks of Foundation Models (2021). https://cs.stanford.edu/~pliang/
- **Ruiqi Gao** — Research scientist at Google DeepMind working on generative models; first author of CAT3D, which creates a 3D scene from one or a few images in about a minute. Known for: CAT3D: Create Anything in 3D with Multi-View Diffusion Models (NeurIPS 2024); Understanding Diffusion Objectives as the ELBO (NeurIPS 2023). https://ruiqigao.github.io/
- **Ryo Suzuki** (Boulder, US) — Assistant professor at the University of Colorado Boulder (ATLAS Institute), formerly at the University of Calgary, who runs the Programmable Reality Lab; his group builds AR systems that generate interactive content from the physical world with AI. Known for: RealitySketch (UIST 2020); Augmented Physics (UIST 2024); RealityCanvas (UIST 2023). https://ryosuzuki.org/
- **Shlomi Fruchter** — Research Director at Google DeepMind who helped lead Veo and Imagen 3 and co-authored GameNGen, the diffusion model that ran DOOM in real time with no game engine. Known for: GameNGen: Diffusion Models Are Real-Time Game Engines (ICLR 2025); Veo (2024); Imagen 3 (2024). https://shlomifruchter.github.io/
- **Sylvia Xueni Pan** (London, UK) — Professor of Virtual Reality at Goldsmiths, University of London, who co-leads its MA/MSc in Virtual and Augmented Reality; she uses virtual characters to study social interaction and to train doctors' responses to difficult patients. Known for: Why and how to use virtual reality to study human social interaction (British Journal of Psychology, 2018); GPs' responses to patient demand for antibiotics in VR (2016). https://www.panxueni.com/
- **Thomas Müller** — Creator of instant-ngp, whose multiresolution hash encoding cut NeRF training from hours to seconds, and of tiny-cuda-nn. Formerly principal research scientist at NVIDIA, he now works as an independent researcher. Known for: Instant Neural Graphics Primitives (SIGGRAPH 2022 Best Paper); tiny-cuda-nn (2021). https://tom94.net/
- **Tim Brooks** (San Francisco, US) — Leads media generation at Meta Superintelligence Labs (the Muse Image and Muse Video models). Before that he led an omnimodel team at Google DeepMind and co-led Sora at OpenAI; his PhD work at Berkeley produced InstructPix2Pix. Known for: Sora: Video generation models as world simulators (2024); InstructPix2Pix (CVPR 2023); Generating Long Videos of Dynamic Scenes (NeurIPS 2022). https://timothybrooks.com/
- **Tim Rocktäschel** (London, UK) — Professor of AI at UCL and co-founder and Chief Scientist of Recursive; he previously led the Open-Endedness team at Google DeepMind, which produced Genie. His work argues that open-ended environments, not fixed datasets, are what agents need to keep learning. Known for: Genie (ICML 2024); Open-Endedness is Essential for Artificial Superhuman Intelligence (ICML 2024); The NetHack Learning Environment (NeurIPS 2020). https://rockt.ai/
- **Vincent Sitzmann** (Cambridge, MA, US) — Associate professor at MIT CSAIL who leads the Scene Representation Group, working on neural scene representations and video world models that keep 3D structure and memory over time. Known for: SIREN (NeurIPS 2020); Scene Representation Networks (NeurIPS 2019); Diffusion Forcing (NeurIPS 2024). https://www.vincentsitzmann.com/
- **Yann LeCun** (New York / Paris, 1960–) — Turing Award laureate and NYU professor who left his post as Meta's Chief AI Scientist to co-found Advanced Machine Intelligence (AMI) Labs in December 2025. He argues that agents need predictive world models (JEPA) rather than pixel-by-pixel generation. Known for: A Path Towards Autonomous Machine Intelligence (2022); I-JEPA (2023); V-JEPA 2 (2025). https://en.wikipedia.org/wiki/Yann_LeCun
- **Yaser Sheikh** (Pittsburgh, US) — Founded Meta's Reality Labs lab in Pittsburgh and, as a Meta vice president from 2015 to 2025, led the invention of Codec Avatars, real-time photoreal telepresence avatars. He is now a consulting professor at Carnegie Mellon and founder of a stealth AI venture. Known for: Codec Avatars (2019–2025); OpenPose (CVPR 2017); Panoptic Studio (ICCV 2015). https://www.cs.cmu.edu/~yaser/
- **Zhu Jun / 朱军** (Beijing, CN) — Professor of computer science at Tsinghua University and chief scientist of Shengshu Technology. His group's U-ViT architecture underlies Vidu, launched in April 2024, which the team describes as the first Sora-like video generator after Sora. Known for: U-ViT: All are Worth Words (CVPR 2023); Vidu (2024); ProlificDreamer (NeurIPS 2023). https://ml.cs.tsinghua.edu.cn/~jun/index.shtml
- **Ziwei Liu / 刘子纬** (Singapore) — Associate professor at Nanyang Technological University (MMLab@NTU, S-Lab) whose group built VBench, a widely used video-generation benchmark, along with open 3D and avatar generators. Known for: VBench (CVPR 2024); LGM: Large Multi-View Gaussian Model (ECCV 2024); DeepFashion (CVPR 2016). https://liuziwei7.github.io/

### Founders & builders

- **Amit Jain** (San Francisco, US) — Co-founder and CEO of Luma AI, which moved from NeRF capture apps to the Dream Machine and Ray video models and now describes its mission as general physical AI. Known for: Luma NeRF capture app (2022); Dream Machine (2024); Ray3 (2025). https://x.com/gravicle
- **Brendan Iribe** (San Francisco, US, 1979–) — Oculus co-founder who co-founded Sesame, the voice-companion company whose Conversational Speech Model (2025) made AI voices pause, laugh and interrupt like people; Sesame is also building smart glasses. Known for: Oculus Rift (2012–2016); Sesame CSM / Maya and Miles (2025). https://en.wikipedia.org/wiki/Brendan_Iribe
- **Cristóbal Valenzuela** (New York, US, 1989–) — Co-founder and CEO of Runway, which took video generation from research to filmmaking tools (Gen-1 to Gen-4.5) and in 2025 moved into general world models. Known for: Runway Gen-2 (2023); Gen-4 (2025); GWM-1 world model (2025). https://en.wikipedia.org/wiki/Crist%C3%B3bal_Valenzuela
- **Dean Leitersdorf** (San Francisco, US / Tel Aviv, IL) — Co-founder and CEO of Decart, which builds real-time generative video: Oasis, a playable Minecraft-like world model (with Etched), and MirageLSD, live video-to-video restyling. Known for: Oasis (2024); MirageLSD (2025). https://x.com/dleitersdorf
- **Ethan (Yuanming) Hu / 胡渊鸣** — Founder and CEO of Meshy, the text- and image-to-3D asset generator; before that he created the Taichi programming language for graphics during his MIT PhD. Known for: Taichi (SIGGRAPH Asia 2019); Meshy (2023–); DiffTaichi (ICLR 2020). https://yuanming.taichi.graphics/
- **Hassaan Raza** (San Francisco, US) — Co-founder and CEO of Tavus, whose conversational video interface pairs perception, turn-taking and face models; in October 2026 Tavus launched Griffin, which it calls a human interaction model. Known for: Tavus CVI (2024); Phoenix / Raven / Sparrow models; Griffin (2026). https://www.tavus.io/griffin
- **Joshua Xu** (Los Angeles, US) — Co-founder and CEO of HeyGen, the avatar video platform whose interactive avatars bring talking-head generation into real-time conversation. Known for: HeyGen avatar video (2020–); HeyGen Interactive Avatar / LiveAvatar. https://x.com/joshua_xu_
- **Mati Staniszewski** (London, UK, 1995–) — Co-founder and CEO of ElevenLabs, whose expressive text-to-speech, voice cloning and agent platform became the default voice layer for many generated characters. Known for: ElevenLabs TTS (2023); Eleven v3 (2025); ElevenLabs Agents platform. https://en.wikipedia.org/wiki/Mati_Staniszewski
- **Oliver Cameron** (San Francisco, US) — Co-founder and CEO of Odyssey, which builds foundation world models that stream interactive video; previously he worked on self-driving cars at Voyage and Cruise. Known for: Odyssey interactive video (2025); Voyage self-driving (2017–2021). https://x.com/olivercameron
- **Victor Riparbelli** (London, UK) — Co-founder and CEO of Synthesia, the AI avatar video company he started with researchers Lourdes Agapito and Matthias Nießner; it has been an early voice for consent rules on synthetic people. Known for: Synthesia avatars (2017–); Synthesia Expressive Avatars (2024). https://x.com/vriparbelli
- **Yan Junjie / 闫俊杰** (Shanghai, CN, 1989–) — Co-founder and CEO of MiniMax, the Shanghai company behind the Hailuo video models and the Speech series of TTS models. Known for: Hailuo Video-01 (2024); Hailuo 02 (2025); MiniMax Speech-02 (2025). https://en.wikipedia.org/wiki/Yan_Junjie

### Artists & directors

- **Hsin-Chien Huang / 黄心健** (Taipei, TW, 1966–) — Taiwanese new-media artist whose VR works, including To the Moon with Laurie Anderson and Bodyless, are landmarks of immersive storytelling at Venice and other festivals. Known for: La Camera Insabbiata / Chalkroom (with Laurie Anderson, Venice 2017); To the Moon (2018); Bodyless (2019). https://hsinchienhuang.com/
- **Ian Cheng** (New York, US, 1984–) — Artist who makes live simulations: open-ended virtual ecosystems whose agents keep acting and changing without a script, the art-world counterpart of generative agent worlds. Known for: Emissaries trilogy (2015–2017); BOB (Bag of Beliefs) (2018–2019); Life After BOB (2021). https://iancheng.com/
- **Keiichi Matsuda** (London, UK) — Designer and filmmaker whose short film Hyper-Reality pictured a city saturated with augmented-reality ads and assistant agents; his later work designs AI agents for everyday mixed reality. Known for: Hyper-Reality (2016); Merger (2018). http://km.cx/
- **Nonny de la Peña** (Los Angeles, US) — Journalist and filmmaker credited with creating immersive journalism; founder of Emblematic Group, whose VR pieces such as Hunger in Los Angeles put viewers bodily inside reconstructed real events. Known for: Hunger in Los Angeles (Sundance 2012); Project Syria (2014); Immersive Journalism (Presence, 2010). https://en.wikipedia.org/wiki/Nonny_de_la_Pe%C3%B1a
- **Paul Trillo** (Los Angeles, US) — Writer-director who made some of the first commissioned films with Sora, including the 2024 music video for Washed Out's The Hardest Part, built from a single endless zoom through generated scenes. Known for: The Hardest Part (Washed Out, made with Sora, 2024). https://paultrillo.com/
- **Refik Anadol** (Los Angeles, US, 1985–) — Media artist whose studio turns large datasets into immersive, room-scale generative works; its Large Nature Model and the Dataland museum in Los Angeles make AI-generated nature into an environment people walk into. Known for: Unsupervised (MoMA, 2022); Large Nature Model (2024); Dataland (Los Angeles). https://refikanadol.com/

### AI labs & companies

- **AI at Meta (FAIR & Superintelligence Labs)** (Menlo Park, US) — Meta's AI research groups, which released V-JEPA 2 world models, the Seamless Interaction dataset and models of two-person face-to-face behavior, and SAM 3D; the research page now leads with its 2026 Muse models. https://ai.meta.com/research/
- **Alibaba Tongyi Wan / 阿里通义万相** (Hangzhou, CN) — Alibaba's Tongyi Lab video family; Wan 2.1 and 2.2 were released as open weights and became a common base for open video research and fine-tunes. https://wan.video/
- **ByteDance Seed / 字节跳动 Seed** (Beijing, CN) — ByteDance's foundation-model team, formed in 2023, behind the Seedance video models, OmniHuman audio-driven human animation and Seed3D. https://seed.bytedance.com/en/
- **Decart** (San Francisco, US / Tel Aviv, IL) — Real-time generative video lab: Oasis (2024) was a playable world model of a Minecraft-like game, and MirageLSD (2025) restyles live camera video in real time. https://decart.ai/
- **ElevenLabs** (London, UK / New York, US) — Voice AI company whose text-to-speech, voice cloning, sound effects, music and conversational agent platform supply the voices of many generated characters and virtual humans. https://elevenlabs.io/
- **General Intuition** — World-model lab co-founded by DIAMOND author Eloi Alonso that trains agents and world models on large archives of game play, describing itself as 'the frontier lab for acting in space and time'. https://www.generalintuition.com/
- **Google DeepMind** (London, UK) — Google's AI lab and the single largest source of landmarks in this gallery: the Genie world models (Genie 1 to 3), the Veo video models with native audio, CAT3D and the SIMA game agents. https://deepmind.google/
- **Gradium** (Paris, FR) — Paris voice-AI company spun out of Kyutai in December 2025 and led by Neil Zeghidour; it turns the Moshi line of research into a real-time voice API for agents (low-latency speech synthesis, transcription, live translation and voice cloning). https://gradium.ai/
- **Hume AI** (New York, US) — Voice AI company grounded in emotion science, maker of the EVI empathic voice interface and Octave TTS; it now also sells expression measurement (600+ dimensions) for evaluating voice agents, which is useful for coding affect in studies. https://www.hume.ai/
- **Kling AI (Kuaishou) / 可灵 AI（快手）** (Beijing, CN) — Kuaishou's video-generation product, launched in June 2024 and updated through a fast series of Kling versions that have often ranked at or near the top of public video arenas. https://kling.ai/
- **Kyutai** (Paris, FR) — Non-profit open-science AI lab in Paris that released Moshi, the first open full-duplex speech model, plus Hibiki live speech translation and the Unmute voice stack; its voice work was spun out as Gradium in 2025. https://kyutai.org/
- **Luma AI** (San Francisco, US) — Started with NeRF and splat capture on phones, then released the Dream Machine and Ray video models; its site now presents AI agents for creative work. https://lumalabs.ai/
- **Meta Reality Labs Research** (Redmond / Pittsburgh, US) — Meta's research arm for AR and VR, home of Codec Avatars (photoreal telepresence), Hyperscape room capture with Gaussian splatting, and the Aria research glasses. https://tech.facebook.com/reality-labs/
- **Microsoft Research** (Redmond, US) — Microsoft's research organization, which produced VASA-1 lifelike talking faces from one photo, the Muse (WHAM) game world model with Xbox, and the open Rocketbox avatar library used across VR studies. https://www.microsoft.com/en-us/research/
- **MiniMax / MiniMax（稀宇科技）** (Shanghai, CN) — Shanghai AI company whose Hailuo video models and Speech text-to-speech models have ranked near the top of public video and speech arenas. https://www.minimax.io/
- **Mursion** (San Francisco, US) — Immersive simulation company where employees practice difficult conversations with avatars that push back; it began with human simulation specialists voicing the avatars and now markets an AI-powered upskilling platform. https://www.mursion.com/
- **NVIDIA Spatial Intelligence Lab** (Toronto, CA) — NVIDIA's research lab for AI that perceives, models and interacts with the physical world (the former Toronto AI Lab), behind 3D-consistent video and world generation such as GEN3C and Lyra and the 3DGUT renderer. https://research.nvidia.com/labs/sil/
- **OpenAI** (San Francisco, US) — Released Sora (2024), which framed video models as world simulators, and Sora 2 with synchronized sound (2025), plus the gpt-realtime speech-to-speech API. It closed the Sora app in April 2026 and the Sora API in September 2026, moving the team to world simulation research. https://openai.com/
- **Runway** (New York, US) — New York company that turned video generation into filmmaking tools (Gen-1 through Gen-4.5, Act-Two, Aleph) and in December 2025 launched GWM-1, a general world model; it also runs the AI Festival (AIF). https://runway.com/
- **Shanghai AI Laboratory / 上海人工智能实验室** (Shanghai, CN) — State-backed research institute founded in 2020 that publishes open models and benchmarks, including the Vchitect video-generation project behind the VBench leaderboard (with NTU S-Lab). https://www.shlab.org.cn/
- **Shengshu Technology (Vidu) / 生数科技** (Beijing, CN) — Beijing company spun out of Tsinghua University, maker of the Vidu video models (first released April 2024) with reference-to-video for consistent characters. https://www.vidu.com/
- **Simile** (Palo Alto, US) — Palo Alto company founded by generative-agents author Joon Sung Park that sells simulations of how customers, employees or populations respond to change; it announced a $200M Series B at a $2B valuation in 2026. https://www.simile.com/
- **Tencent Hunyuan / 腾讯混元** (Shenzhen, CN) — Tencent's foundation-model team, one of the most prolific open-weight sources in the field: HunyuanVideo, Hunyuan3D, HunyuanWorld and the GameCraft game-video model. https://hunyuan.tencent.com/
- **World Labs** (San Francisco, US) — The spatial-intelligence company founded by Fei-Fei Li, Justin Johnson, Ben Mildenhall and Christoph Lassner; its Marble product generates persistent, editable 3D worlds from text, images, video and 3D layouts. https://www.worldlabs.ai/

### Academic labs

- **Event Lab (Universitat de Barcelona)** (Barcelona, ES) — Mel Slater's Barcelona lab for virtual environments in neuroscience and technology, known for studies of body ownership, embodiment and people's responses to virtual others. https://www.ub.edu/eventlab/EventLab/
- **Inria GraphDeco** (Sophia Antipolis, FR) — George Drettakis's graphics group at Inria Sophia Antipolis, where 3D Gaussian Splatting was invented (SIGGRAPH 2023 best paper) and released with open code. https://team.inria.fr/graphdeco/
- **Max Planck Institute for the Study of Crime, Security and Law / 马克斯·普朗克犯罪、安全与法律研究所** (Freiburg, DE) — Freiburg institute whose criminology department, led by Jean-Louis van Gelder, uses virtual reality to study offending, victimization and decision-making under realistic conditions. https://csl.mpg.de/en
- **MMLab@NTU / S-Lab** (Singapore) — Nanyang Technological University's multimedia lab (Chen Change Loy, Ziwei Liu), a major source of open video, 3D and avatar generators and of the VBench benchmark. https://www.mmlab-ntu.com/
- **Reality Design Lab / 现实设计实验室** — Botao 'Amber' Hu's design research lab working on mixed reality and generative immersive experiences, maker of the open HoloKit toolkit; it makes this gallery, Generative Reality Inspire. https://reality.design/
- **Stanford Virtual Human Interaction Lab (VHIL)** (Stanford, US) — Jeremy Bailenson's lab studying what VR and avatars do to people, from the Proteus effect to Zoom fatigue and large-scale VR classes. https://vhil.stanford.edu/
- **Stanford Vision and Learning Lab (SVL)** (Stanford, US) — Stanford lab of Fei-Fei Li, Jiajun Wu and colleagues that builds simulation environments and benchmarks for embodied agents (BEHAVIOR, OmniGibson) and evaluations of world generation such as WorldScore. https://svl.stanford.edu/
- **UCL Virtual Environments and Computer Graphics (VECG)** (London, UK) — UCL Computer Science group where much of presence research took shape in the 1990s–2000s, including Slater's virtual Milgram (2006) and Arsenal-fan bystander (2013) studies; it continues to work on VR, collaborative virtual environments and graphics. http://vecg.cs.ucl.ac.uk/
- **USC Institute for Creative Technologies** (Los Angeles, US) — Army-sponsored USC research center that has built interactive virtual humans for training and therapy for two decades, including Bravemind VR exposure therapy and the SimSensei virtual interviewer. https://ict.usc.edu/

### Conferences & workshops

- **ACM CHI** — The ACM Conference on Human Factors in Computing Systems, the largest HCI venue, where generative XR systems, LLM agent studies and VR user studies are published. https://chi2027.acm.org/
- **ACM IVA (Intelligent Virtual Agents)** — ACM conference on intelligent virtual agents: embodied conversational characters, nonverbal behavior generation and their use in training, health and research. https://iva.acm.org/
- **ACM SIGGRAPH & SIGGRAPH Asia** — The main computer graphics conferences, where NeRF-era rendering, 3D Gaussian Splatting, avatar and motion-generation papers appear, along with an Immersive Pavilion and Real-Time Live demos. https://s2026.siggraph.org/
- **ACM UIST** — ACM Symposium on User Interface Software and Technology, where Generative Agents won a best paper in 2023 and many AR authoring and AI-in-the-loop systems debut. https://uist.acm.org/
- **AIF (Runway AI Festival)** — Runway's annual festival, started in 2023 as the AI Film Festival, that screens short films made with generative video tools. https://aif.runwayml.com/
- **CVPR** — IEEE/CVF Conference on Computer Vision and Pattern Recognition, the largest vision venue and the usual home of video generation, 3D/4D reconstruction and world-generation papers and workshops. https://cvpr.thecvf.com/
- **I/ITSEC** (Orlando, US) — The Interservice/Industry Training, Simulation and Education Conference in Orlando, the largest venue for military and industrial simulation training, where ICT's virtual-human trainers were presented. https://www.iitsec.org/
- **ICCV & ECCV** — The International and European Conferences on Computer Vision, held in alternate years (ICCV odd, ECCV even); NeRF appeared at ECCV 2020 and DiT at ICCV 2023. https://iccv.thecvf.com/
- **ICLR** — International Conference on Learning Representations, with open review on OpenReview; GameNGen and many video and world-model papers appeared here. https://iclr.cc/
- **IEEE ISMAR** — IEEE International Symposium on Mixed and Augmented Reality, the main AR/MR research venue, increasingly with generative and LLM-driven XR papers. https://ismar.net/
- **IEEE VR** — IEEE Conference on Virtual Reality and 3D User Interfaces, the main venue for VR systems, presence and embodiment studies; its papers are published in IEEE TVCG. https://ieeevr.org/
- **NeurIPS** — Conference on Neural Information Processing Systems, where much world-model, diffusion and agent research is published, along with datasets and benchmarks tracks. https://neurips.cc/
- **Venice Immersive** (Venice, IT) — The immersive section of the Venice International Film Festival, the leading showcase and competition for VR, MR and immersive works since 2017. https://www.labiennale.org/en/cinema/2026/venice-immersive

### Journals

- **ACM Transactions on Graphics (TOG)** — The leading graphics journal, which publishes SIGGRAPH and SIGGRAPH Asia technical papers, among them 3D Gaussian Splatting and instant-ngp. https://en.wikipedia.org/wiki/ACM_Transactions_on_Graphics
- **Computers in Human Behavior** — Elsevier journal on the psychology of computer use, a frequent outlet for studies of virtual humans, avatars and VR effects on behavior. https://en.wikipedia.org/wiki/Computers_in_Human_Behavior
- **Frontiers in Virtual Reality** — Open-access journal founded in 2020 covering VR/AR technology and its use in psychology, health and training. https://www.frontiersin.org/journals/virtual-reality
- **IEEE Transactions on Visualization and Computer Graphics (TVCG)** — IEEE journal that publishes the IEEE VR and ISMAR journal papers, the main archival outlet for VR systems and perception research. https://www.computer.org/csdl/journal/tg
- **PRESENCE: Virtual and Augmented Reality** — MIT Press journal founded in 1992 as Presence: Teleoperators and Virtual Environments, where presence theory, immersive journalism and much early VR behavior research were published. https://en.wikipedia.org/wiki/Presence:_Teleoperators_%26_Virtual_Environments

### Newsletters, podcasts & media

- **80 Level** — Industry site for game and 3D artists that tracks generative 3D, splatting and real-time tools as they enter production. https://80.lv/
- **Bilawal Sidhu** — Creator and former Google Maps / AR product manager whose YouTube and social channels demo and explain 3D capture, splatting and generative video. https://www.youtube.com/@bilawalsidhu
- **Radiance Fields** — News site and newsletter dedicated to radiance fields: Gaussian splatting, NeRF and the capture tools and platforms built on them. https://radiancefields.com/
- **Road to VR** — Long-running XR news site covering headsets, platforms and immersive software, including generative features on Quest, Vision Pro and Android XR. https://roadtovr.com/
- **Two Minute Papers** — Károly Zsolnai-Fehér's YouTube channel that explains new graphics and AI papers in short videos; a quick way to see new video, splatting and simulation results in motion. https://www.youtube.com/@TwoMinutePapers
- **UploadVR** — XR news site that reports on VR and AR hardware, apps and platform changes, often with hands-on tests of new immersive features. https://www.uploadvr.com/
- **Voices of VR Podcast** — Kent Bye's podcast, an oral history of XR with more than a thousand episodes of interviews with immersive artists, researchers and developers, including on XR ethics and AI. https://voicesofvr.com/

### Communities & directories

- **Awesome 3D Gaussian Splatting** — MrNeRF's curated, regularly updated list of Gaussian splatting papers, code and tools, sorted by topic from compression to avatars and 4D. https://github.com/MrNeRF/awesome-3D-gaussian-splatting
- **Awesome Talking Head Generation** — Curated GitHub list of talking-head and audio-driven portrait generation papers, datasets and code. https://github.com/harlanhong/awesome-talking-head-generation
- **Awesome Video Diffusion** — Show Lab (NUS)'s curated list of video diffusion papers and code, from text-to-video to editing, control and long video. https://github.com/showlab/Awesome-Video-Diffusion
- **Awesome World Models** — Curated GitHub list of world-model papers across games, embodied AI, autonomous driving and video generation. https://github.com/knightnemo/Awesome-World-Models
- **C2PA (Content Credentials)** — The Coalition for Content Provenance and Authenticity, which maintains the open Content Credentials standard that several video and image generators attach to their output to mark it as AI-made. https://c2pa.org/
- **Hugging Face Daily Papers** — Daily, upvoted feed of new arXiv papers on Hugging Face, started by AK (@_akhaliq), with linked models, datasets and demo Spaces; the fastest way to catch new generative video, 3D and world-model releases. https://huggingface.co/papers
- **Hugging Face Spaces** — Hosted demos for open models, where many video, 3D, avatar and speech models can be tried in the browser on release day. https://huggingface.co/spaces

### Leaderboards & arenas

- **3D Arena** — Hugging Face arena where people vote between pairs of generated 3D models to rank image-to-3D generators. https://huggingface.co/spaces/3d-arena/3d-arena
- **Arena (formerly LMArena)** — The crowd-voted model ranking site that grew out of Chatbot Arena and LMArena; besides text it ranks text-to-video, image-to-video and image models. https://arena.ai/
- **Artificial Analysis Speech Arena** — Blind human-preference arena ranking text-to-speech models and voices, with price and latency comparisons. https://artificialanalysis.ai/text-to-speech/arena
- **Artificial Analysis Video Arena** — Blind pairwise human-preference arena with Elo rankings for text-to-video and image-to-video models, with and without audio, alongside price and speed data. https://artificialanalysis.ai/video/arena
- **TTS Arena** — Community Hugging Face arena where listeners vote between text-to-speech outputs, covering both open and commercial voices. https://huggingface.co/spaces/TTS-AGI/TTS-Arena-V2
- **VBench Leaderboard** — Leaderboard for VBench, which scores video generators on 16 dimensions such as subject consistency, motion smoothness and physical plausibility. https://huggingface.co/spaces/Vchitect/VBench_Leaderboard
- **WorldScore** — Unified benchmark and leaderboard for world generation from Stanford that compares 3D scene generators, 4D generators and video models on controllability, quality and dynamics. https://haoyi-duan.github.io/WorldScore/

## Labs & creators

- **Google DeepMind** (32) — AI research lab of Google. Google's AI lab (Gemini, Genie, Veo). Its SIMA project trains agents that follow language instructions in commercial 3D games and, with SIMA 2, in worlds generated by Genie 3; it also maintains the Concordia library for generative social simulation. https://deepmind.google
- **Meta** (29) — Meta AI / FAIR / Reality Labs. Meta's AI research (FAIR) and Reality Labs groups; in 3D assets they released Meta 3D Gen, SAM 3D Objects and Body, ShapeR and the Meta Motivo humanoid model. https://ai.meta.com
- **NVIDIA** (29) — GPU and AI computing company. Maker of GPUs and of ACE, a stack of speech, language and facial-animation models for game characters; its research groups also built the Voyager and NitroGen game agents. https://research.nvidia.com
- **Google** (21) — Google Research, Google Labs and Google AR. Google's research and product groups outside DeepMind; Google Research authored DreamFusion, the 2022 paper that started text-to-3D via 2D diffusion. https://research.google
- **ByteDance Seed** (16) — ByteDance's foundation-model research team. Research team building ByteDance's foundation models (Doubao, Seedance, UI-TARS); in 2025 it released the game agents Game-TARS and Lumine. https://seed.bytedance.com
- **Mel Slater** (14) — VR researcher, co-director of the EventLab, University of Barcelona. Computer scientist turned presence researcher who formulated place illusion and plausibility and ran the virtual Milgram, bystander and body-ownership experiments.
- **Tencent Hunyuan** (14) — Tencent's foundation-model team. Tencent's Hunyuan team releases open and closed models across text, image, video, 3D (Hunyuan3D 1.0 to 3.x, HY 3D Studio) and motion (HY-Motion). https://hunyuan.tencent.com
- **Microsoft** (13) — Microsoft Research. Microsoft Research released TRELLIS (2024) and TRELLIS.2 (2025), MIT-licensed 3D generators built on structured 3D latents. https://www.microsoft.com/research
- **Kuaishou** (11) — Short-video company (Kling team). Kuaishou develops the Kling video models and open-sourced LivePortrait; its Kling team also published MIDAS, a real-time autoregressive digital human. https://www.kuaishou.com
- **Alibaba Tongyi (Qwen)** (9) — Alibaba's Tongyi Lab and Qwen team. Alibaba's Tongyi Lab develops the Qwen model family, the Wan video models and the Fun-Audio / CosyVoice speech models, many released as open weights. https://wan.video
- **OpenAI** (9) — AI research and deployment company. Developer of GPT, Sora and the realtime voice models; in 2019 its multi-agent hide-and-seek study showed agents inventing tool use in a 3D physics world. https://openai.com
- **Runway** (9) — AI video company. Maker of the Gen and Aleph video models and of world-model research (GWM-1); sells an app and a developer API. https://runwayml.com
- **Stability AI** (7) — Open generative-model company. Company behind Stable Diffusion that also released open 3D models: TripoSR (with Tripo AI), Stable Fast 3D, SPAR3D and Stable Video 3D. https://stability.ai
- **Apple** (6) — Consumer technology company. Apple's Vision Pro creates a Persona, a 3D avatar of the wearer reconstructed from a face scan and driven by the headset's sensors. https://machinelearning.apple.com
- **Decart** (6) — AI lab building real-time generative video and world models. Start-up behind Oasis (a real-time generated Minecraft-like world) and the MirageLSD live video-to-video model, offered through an API. https://decart.ai
- **World Labs** (6) — Spatial-intelligence company. Founded by Fei-Fei Li and colleagues; makes the Marble world model and the Spark splat renderer. https://www.worldlabs.ai
- **Deemos (Hyper3D Rodin)** (5) — 3D generation company behind Hyper3D Rodin. ShanghaiTech-rooted company that builds the Rodin 3D generators (Gen-1 based on the CLAY research model, Gen-1.5, Gen-2, Gen-2.5) and the ChatAvatar face generator, sold through hyper3d.ai and an API. https://hyper3d.ai
- **Luma AI** (5) — Generative AI company (3D capture, video). Started with NeRF capture apps and the Genie text-to-3D generator, then moved its focus to video generation (Dream Machine, Ray models). https://lumalabs.ai
- **Skywork (Kunlun Tech)** (5) — AI unit of Kunlun Tech. Kunlun Tech's AI unit, which open-sources the SkyReels video models and the Matrix world models. https://www.skywork.ai
- **Snap Inc.** (5) — Camera company; Snapchat, Lens Studio and Spectacles / SPECS AR glasses. Maker of Snapchat Lenses, used billions of times a day, and of standalone AR glasses: Spectacles for developers (2024) and the consumer SPECS (2026). https://research.snap.com
- **Tavus** (5) — Real-time conversational video AI company. Tavus builds models for face-to-face AI conversation: Phoenix (rendering), Raven (perception), Sparrow (turn-taking) and, since October 2026, Griffin, a unified full-duplex video-to-video model. Its Conversational Video Interface API and consumer PALs run on these models. https://www.tavus.io
- **Tripo AI (VAST)** (5) — 3D generation company (VAST). VAST builds the Tripo 3D generation models and Tripo Studio, and publishes open research such as TripoSR (with Stability AI), TripoSG, UniRig and TripoSplat. https://www.tripo3d.ai/
- **USC Institute for Creative Technologies** (5) — University-affiliated research center of the University of Southern California. Research institute founded in 1999 with US Army funding to combine AI, graphics and storytelling for training and health; home of the Virtual Human Toolkit, SimSensei and Bravemind. https://ict.usc.edu/
- **Epic Games** (4) — Game developer and engine maker (Fortnite, Unreal Engine). Developer of Fortnite and Unreal Engine; launched a voice-chat AI Darth Vader in Fortnite in 2025 and opened the technology to creators as the Persona device, later called Conversations. https://www.unrealengine.com
- **Jeremy Bailenson** (4) — Founding director of the Virtual Human Interaction Lab (VHIL), Stanford University. Communication scholar who studies how avatars, virtual bodies and immersive media change attitudes and behavior, from the Proteus effect to large VR field studies. https://vhil.stanford.edu/
- **Kyutai** (4) — Non-profit open-science AI lab. Kyutai is a Paris non-profit research lab funded by Iliad, CMA CGM and Schmidt Sciences that releases its speech models openly. https://kyutai.org
- **Meshy** (4) — AI 3D generation company. Startup behind Meshy, a web, app and API product for text-to-3D, image-to-3D, AI texturing, auto-rigging and animation; it shipped model generations from Meshy-1 (2023) to Meshy 7.1 (September 2026). https://www.meshy.ai/
- **Adobe** (3) — Creative-software company (Adobe Research). Maker of Photoshop and Substance 3D; Adobe Research co-authored LRM, the first large reconstruction model for single-image 3D. https://research.adobe.com
- **Character.AI** (3) — Consumer AI character platform. Character.AI runs a large consumer platform for chatting with AI characters and develops video models (AvatarFX, TalkingMachines) to give them faces. https://character.ai
- **Doron Friedman** (3) — Head of the Advanced Reality Lab, Reichman University. Studies virtual humans, telepresence and VR for mental health; his lab builds LLM-driven virtual humans and automated scenario pipelines.
- **ElevenLabs** (3) — AI audio company. ElevenLabs builds text-to-speech, voice cloning, conversational agents, sound effects and music models used widely in media production. https://elevenlabs.io
- **Hume AI** (3) — Voice AI, expression-measurement and evaluation company. Hume AI builds the Empathic Voice Interface (EVI), the Octave text-to-speech models and the open-source TADA model; in 2026 it leads with Expression APIs (600+ dimensions of expression in 50+ languages) and tools and benchmarks for evaluating real-world voice AI, including RW-Voice-EQ Bench. https://www.hume.ai
- **Jean-Louis van Gelder** (3) — Director at the Max Planck Institute for the Study of Crime, Security and Law; professor at Leiden University. Criminologist and psychologist who uses VR to study criminal decision-making (Virtual Burglary Project) and future-self interventions. https://csl.mpg.de/en
- **Joon Sung Park** (3) — HCI researcher; co-founder and CEO of Simile. Stanford computer science PhD who introduced generative agents in the 2023 Smallville paper and then built agents grounded in two-hour interviews with 1,052 Americans. Co-founded Simile with Michael Bernstein and Percy Liang.
- **Odyssey** (3) — World-model AI lab. AI lab founded in 2023 by Oliver Cameron and Jeff Hawke to build general-purpose world models; it released Odyssey-1, -2 and -3, the multi-agent Agora models and an API. https://odyssey.ml
- **Robbyant** (3) — Embodied AI unit of Ant Group. Ant Group's embodied-intelligence company, which publishes the open LingBot family of models for robots and spatial perception. https://technology.robbyant.com
- **Roblox** (3) — Online game platform. Platform where users build and play experiences; its Foundation AI team develops the Cube 3D foundation model, open-sourced in part, and in-experience 3D and 4D generation. https://corp.roblox.com
- **Ryo Suzuki** (3) — Assistant Professor, ATLAS Institute and Computer Science, University of Colorado Boulder; director of the Programmable Reality Lab. HCI researcher working at the intersection of AR/VR, tangible interfaces and AI; the lab's 'Generative AR' theme aims to make the physical world a canvas for generative AI. https://ryosuzuki.org
- **Stijn Spanhove** (3) — XR developer, In The Pocket; Snap Spectacles creator. Developer who publishes short proofs of concept that combine AR glasses, Vision Pro and generative models.
- **Agora** (2) — Real-time engagement platform. Runs a global real-time network for voice and video SDKs, the Conversational AI Engine, and backs the open-source TEN Framework. https://www.agora.io
- **Albert "Skip" Rizzo** (2) — Director of Medical Virtual Reality, USC Institute for Creative Technologies. Clinical psychologist who built Virtual Iraq/Afghanistan and Bravemind for PTSD exposure therapy and led virtual-patient research.
- **Bernhard Kerbl** (2) — Researcher, Inria / TU Wien. Co-first author of 3D Gaussian Splatting (SIGGRAPH 2023) and first author of its hierarchical version for very large scenes.
- **Botao 'Amber' Hu** (2) — Researcher, University of Oxford; founder of Reality Design Lab; inventor of HoloKit. Designer and researcher (Tsinghua BS, Stanford MS in AI) who leads Reality Design Lab's work on embodied, social mixed reality, speculative design and generative futuring; the lab's works have been shown at SIGGRAPH, CHI, TEI and Ars Electronica. https://reality.design
- **Chuan Guo** (2) — Researcher in human motion generation. Researcher (University of Alberta, later industry) who created the HumanML3D dataset (CVPR 2022) and MoMask (CVPR 2024). https://ericguo5513.github.io/
- **Convai** (2) — Conversational AI platform for game and XR characters. Startup that provides an engine and plugins for characters that talk, perceive and act in Unreal Engine, Unity and web 3D; it built NVIDIA's 2023 Kairos demo with ACE. https://convai.com/
- **Daniel Freeman** (2) — Professor of clinical psychology, University of Oxford. Leads Oxford's automated VR therapy research for fear of heights, paranoia and agoraphobic avoidance in psychosis (gameChange). https://gamechangevr.com/
- **Evonne Ng** (2) — Researcher in dyadic behaviour and gesture generation. Evonne Ng (UC Berkeley, later Meta) led Learning to Listen (CVPR 2022) and Audio2Photoreal (2024), models of how a listener's face and body respond in conversation. https://evonneng.github.io
- **Hong-Xing (Koven) Yu** (2) — Researcher, Stanford University. Computer-vision researcher in Jiajun Wu's group at Stanford, first author of WonderJourney and WonderWorld. https://kovenyu.com
- **Inria GraphDeco** (2) — Graphics research group at Inria. Research group led by George Drettakis at Inria Université Côte d'Azur, origin of 3D Gaussian Splatting and its hierarchical extension. https://team.inria.fr/graphdeco/
- **Inworld AI** (2) — Real-time AI company, formerly an AI character engine for games. Founded in 2021 to build an engine for AI game characters, used in Ubisoft's NEO NPC and NVIDIA's Covert Protocol demos. By 2026 it mainly markets real-time voice models (TTS, STT, speech-to-speech) and a runtime for consumer AI apps. https://inworld.ai/
- **Jianyuan Wang** (2) — Researcher, Oxford VGG / Meta AI. First author of VGGT (CVPR 2025 Best Paper) and VGGT-Ω (CVPR 2026 Oral), joint work of Oxford's Visual Geometry Group and Meta.
- **Jiawei Ren** (2) — Researcher, NTU S-Lab / NVIDIA. First author of DreamGaussian4D and of L4GM (NeurIPS 2024, with NVIDIA).
- **Jiwen Yu** (2) — Researcher at the University of Hong Kong. PhD researcher at the University of Hong Kong working with Kuaishou's Kling team on interactive video generation. https://yujiwen.github.io
- **Jonathan T. Barron** (2) — Research scientist, Google DeepMind. Google researcher behind mip-NeRF, mip-NeRF 360, Zip-NeRF and many radiance-field quality benchmarks.
- **Jonathon Luiten** (2) — Researcher, Meta. First author of Dynamic 3D Gaussians (3DV 2024) and co-author of BulletGen at Meta.
- **Junxuan Li** (2) — Research scientist, Meta Codec Avatars Lab. Junxuan Li is first author of URAvatar (SIGGRAPH Asia 2024) and Large-scale Codec Avatars (CVPR 2026). https://junxuan-li.github.io
- **KRAFTON** (2) — Video game publisher. South Korean publisher of PUBG: Battlegrounds and inZOI; with NVIDIA ACE it introduced 'Co-Playable Characters' that run on small on-device language models. https://www.krafton.com/
- **Keiichi Ihara** (2) — PhD student, Programmable Reality Lab (University of Colorado Boulder) and University of Tsukuba. HCI researcher building mixed-reality systems that turn 2D media such as films and tutorial videos into spatial content.
- **Lei Zhang** (2) — HCI researcher (University of Michigan PhD; now New Jersey Institute of Technology). Researcher on human-AI co-creation in immersive authoring, from VRCopilot (University of Michigan) to Capybara (with the Princeton HCI Lab).
- **Lightricks** (2) — Creative-app company and maker of LTX. Maker of Facetune and LTX Studio; releases the open LTX-Video, LTX-2 and LTX-2.5 models. https://ltx.io
- **Matthew Tancik** (2) — Researcher, co-creator of Nerfstudio. Co-author of NeRF and lead author of Nerfstudio at UC Berkeley; later joined Luma AI.
- **MiniMax** (2) — Foundation-model company (Hailuo). Chinese AI company behind the Hailuo video models, the MiniMax language models and speech models; it released the H3 video model with open weights in July 2026. https://www.minimax.io
- **NAVER LABS Europe** (2) — Research lab of NAVER. Grenoble research centre of the Korean company NAVER, home of the DUSt3R / MASt3R family of 3D foundation models. https://europe.naverlabs.com/
- **Niantic Spatial** (2) — Geospatial AI company spun out of Niantic. Builds large geospatial models, visual positioning and mapping for AR, after Niantic sold its games business in 2025. https://www.nianticspatial.com/
- **PixVerse** (2) — AI video company (AIsphere). Beijing-based maker of the PixVerse video generator and app, developed by AIsphere; in 2026 it added the real-time R1 and R2 world models. https://pixverse.ai
- **PlayCanvas** (2) — Web graphics engine company (part of Snap). Develops the open-source PlayCanvas engine and the SuperSplat Gaussian-splat editor. https://playcanvas.com/
- **Qianqian Wang** (2) — Researcher, UC Berkeley. Berkeley researcher, first author of Shape of Motion and CUT3R.
- **Reality Design Lab** (2) — Independent design research lab for mixed reality, directed by Botao 'Amber' Hu. Makes mixed-reality artworks, open-source toolkits (HoloKit, HoloMask, MultipeerConnectivity for Unity) and teaching programmes under the motto 'design new realities'; its works have been shown at SIGGRAPH, CHI, IEEE VR and Ars Electronica. https://reality.design
- **Samsung Electronics** (2) — Electronics company; maker of the Galaxy XR headset. Consumer-electronics company that co-developed Android XR with Google and Qualcomm and launched the Galaxy XR headset in October 2025. https://www.samsung.com
- **Shengshu Technology (Vidu)** (2) — Video-generation company spun out of Tsinghua University. Founded by Tsinghua researchers; launched Vidu in April 2024 and later the Q-series and real-time S-series models. https://www.vidu.com
- **SpAItial** (2) — 3D world-model startup (Echo). Startup co-founded by TUM professor Matthias Niessner that builds spatial foundation models; it raised a $13 million seed round in 2025 and released Echo (Dec 2025) and Echo-2 (Apr 2026). https://www.spaitial.ai
- **StepFun** (2) — Chinese foundation-model company. StepFun develops the Step series of language, multimodal and audio models and open-sources several of them. https://www.stepfun.com
- **Ubisoft** (2) — Video game publisher. French publisher of Assassin's Creed and The Division; its Paris teams showed the NEO NPC prototype in 2024 and the playable Teammates experiment in 2025. https://www.ubisoft.com/
- **Wayve** (2) — Embodied-AI driving company. London company building end-to-end driving models, and the GAIA line of generative driving world models since 2023. https://wayve.ai
- **Weihao Tan** (2) — AI researcher, game agents. First author of Cradle (2024), which played Red Dead Redemption 2 from screenshots and keyboard-mouse output, and of Lumine (2025, ByteDance Seed), which completes hours-long Genshin Impact missions in real time.
- **ZJU3DV** (2) — 3D vision group at Zhejiang University. Computer vision group of Xiaowei Zhou and Sida Peng at Zhejiang University's State Key Lab of CAD&CG, active in dynamic human and scene capture. https://zju3dv.github.io/
- **Zhaoxi Chen** (2) — PhD researcher, NTU S-Lab. First author of 4DNeX, a feed-forward image-to-4D model. https://frozenburning.github.io
- **Ziqi Huang** (2) — Researcher, S-Lab, Nanyang Technological University. Works on video generation and its evaluation with Ziwei Liu's group; first author of VBench and VBench++. https://ziqihuangg.github.io
- **1X Technologies** (1) — Humanoid-robot company. Norwegian-American maker of the EVE and NEO humanoid robots. https://www.1x.tech
- **4DV.ai** (1) — 4D Gaussian video startup. Startup building capture, playback and editing tools for 4D video based on Gaussian splatting; its CEO Jiaming Sun co-authored FreeTimeGS. Its Infinite Studio demo won Best in Show at SIGGRAPH 2025 Real-Time Live, as reported by Radiancefields.com. https://www.4dv.ai
- **Ailing Zeng** (1) — Researcher in human motion and character generation. Ailing Zeng is first author and co-lead of LPM 1.0 (2026), a 17B video-based character performance model for real-time conversation. https://large-performance-model.github.io
- **Akilan Amithasagaran** (1) — First author of CLiVR (2025). Developed CLiVR, an LLM-driven virtual patient system for Meta Quest 3, with collaborators in medical education.
- **Akio Kodaira** (1) — Developer of real-time diffusion pipelines. Lead author of StreamDiffusion, developed with collaborators including UC Berkeley researchers.
- **Alessio Grancini** (1) — AR engineer; Snap Spectacles developer relations. AR engineer (formerly at Magic Leap) who builds and teaches Spectacles experiments. https://www.alessiograncini.com
- **Alexander Raistrick** (1) — Researcher, Princeton Vision & Learning Lab. PhD researcher with Jia Deng at Princeton, first author of Infinigen, Infinigen Indoors and ProcFunc. https://infinigen.org
- **Alibaba Quark** (1) — Alibaba's Quark / Qwen Applications research team. The Quark team in Alibaba's Qwen Applications Business Group released Live Avatar, a streaming 14B avatar model, with USTC.
- **Allen Institute for AI (Ai2)** (1) — Non-profit AI research institute. Non-profit research institute behind AI2-THOR, ProcTHOR, Objaverse and Holodeck. https://allenai.org
- **Alon Shoa** (1) — Researcher, Advanced Reality Lab, Reichman University. Developer of Milo, an open-source LLM-based virtual human platform for XR.
- **Altera (Fundamental Research Labs)** (1) — AI agent startup. Startup building autonomous digital humans; in 2024 it ran Project Sid, simulations of 10 to more than 1,000 LLM agents in Minecraft. Its YouTube channel now carries the name Fundamental Research Labs.
- **Alvaro Collet** (1) — Researcher, Microsoft (2015). First author of High-Quality Streamable Free-Viewpoint Video (SIGGRAPH 2015), the system behind Microsoft's Mixed Reality Capture Studios.
- **Amazon** (1) — Amazon (AWS and Amazon AGI). Amazon develops the Nova foundation models, served on AWS Bedrock. https://aws.amazon.com/ai/generative-ai/nova/
- **Amina Kobenova** (1) — HCI researcher; first author of Social Conjuring with Microsoft collaborators. Researcher on social, multi-user creation with generative AI in virtual worlds; co-authors include Judith Amores and Jaron Lanier.
- **Amir Bar** (1) — Researcher at Meta FAIR, first author of Navigation World Models. Computer-vision researcher (Meta FAIR, Tel Aviv University) working on visual prediction and world models. https://www.amirbar.net
- **Anam** (1) — Real-time interactive avatar company. Anam builds the CARA family of real-time avatar diffusion models and an API for face-to-face AI agents. https://anam.ai
- **Andreessen Horowitz (a16z)** (1) — Venture capital firm (a16z infra team). Venture firm whose infrastructure team released AI Town with Convex in 2023: an MIT-licensed starter kit for a browser town of chatting LLM characters. https://a16z.com/
- **Andrew Liu** (1) — Researcher, Google Research. First author of Infinite Nature (ICCV 2021) with Noah Snavely and Angjoo Kanazawa at Google Research.
- **Anuttacon** (1) — AI game studio. Studio founded by miHoYo co-founder Cai Haoyu to make AI-native games; released Whispers from the Star in 2025. https://www.anuttacon.com/
- **Anything World** (1) — AI rigging and animation company. Company offering automatic rigging and animation for arbitrary 3D models, including animals and vehicles, through a web app and game-engine plugins. https://anything.world/
- **AppliedVR** (1) — Digital therapeutics company. Maker of RelieVRx, a home VR program for chronic low back pain authorized by the FDA through the De Novo pathway. https://www.appliedvr.io/
- **Arcturus** (1) — Volumetric video software company. Maker of HoloSuite, a toolset for editing, compressing and streaming volumetric video, which has since moved into Gaussian-splat sports replays. https://arcturus.studio/
- **Arena (formerly LMArena)** (1) — Crowdsourced AI evaluation platform. Grew out of the LMSYS Chatbot Arena at UC Berkeley; runs public blind-vote leaderboards for text, vision, image and video models. https://arena.ai
- **Ars Electronica Futurelab** (1) — Art and technology research lab of Ars Electronica. Interdisciplinary lab at the intersection of art, technology and society, known for Deep Space 8K and collaborations with industry partners. https://ars.electronica.art/futurelab/en/
- **Artificial Analysis** (1) — Independent AI benchmarking company. Benchmarks model quality, price and speed across providers, including blind-vote image and video arenas. https://artificialanalysis.ai
- **Avaturn Live** (1) — Real-time interactive avatar company. Avaturn Live builds real-time interactive avatars and released AVTR-1, an open stack with model weights, renderer and serving backend. https://avaturn.live
- **Axon** (1) — Public-safety technology company (TASER, body cameras). Maker of TASER energy weapons and police body cameras that also sells VR training for officers. https://www.axon.com/products/vr
- **Bangbang Yang** (1) — Researcher, ByteDance PICO mixed-reality group. Researcher in neural rendering and scene editing for XR. https://ybbbbt.com/
- **Barbara Olasov Rothbaum** (1) — Professor of psychiatry, Emory University. Clinical psychologist whose 1995 trial was one of the first controlled studies of virtual reality exposure therapy.
- **Beijing Academy of Artificial Intelligence (BAAI)** (1) — Non-profit AI research institute. Non-profit research institute in Beijing; its agents team released Cradle, a framework for general computer control tested in commercial games and software. https://www.baai.ac.cn/
- **Ben Mildenhall** (1) — Researcher, co-founder of World Labs. First author of NeRF (2020), later at Google Research, now a co-founder of World Labs.
- **Ben Poole** (1) — Research scientist, Google. Google researcher and first author of DreamFusion, which introduced Score Distillation Sampling for text-to-3D.
- **Biao Jiang** (1) — Researcher, Fudan University. Fudan University researcher and first author of MotionGPT (NeurIPS 2023), developed with Tencent.
- **Binbin Huang** (1) — Researcher, ShanghaiTech University. First author of 2D Gaussian Splatting (SIGGRAPH 2024).
- **Blockade Labs** (1) — Maker of Skybox AI. Startup that makes Skybox AI, a web tool and API for generating 360° equirectangular skyboxes and environments. https://www.blockadelabs.com
- **Bodyswaps** (1) — Soft-skills training company. Builds VR and browser role-plays with AI avatars and automated feedback for students and employees. https://bodyswaps.co/
- **Boyuan Chen** (1) — Researcher at MIT, first author of Diffusion Forcing. PhD researcher at MIT working on video world models and robot learning. https://boyuan.space
- **CAMEL-AI** (1) — Open-source multi-agent research community. Open-source community behind the CAMEL multi-agent framework and OASIS, a social-media simulator for up to one million LLM agents. https://www.camel-ai.org/
- **Chaoyue Song** (1) — PhD researcher, Nanyang Technological University. NTU researcher and first author of Puppeteer (NeurIPS 2025 spotlight) and MagicArticulate, developed with ByteDance Seed. https://chaoyuesong.github.io/
- **Chen Tessler** (1) — Research scientist, NVIDIA. NVIDIA research scientist working on physics-based character control; first author of MaskedMimic (SIGGRAPH Asia 2024) and maintainer of ProtoMotions.
- **Claire Nee** (1) — Professor of forensic psychology, University of Portsmouth. Studies burglars' expertise and decision-making; co-heads the Virtual Burglary Project.
- **Connor Powelson** (1) — Criminal justice researcher. First author of a 2025 VR think-aloud study of police decisions in mental-health co-response calls.
- **Cyrus Vachha** (1) — Researcher, EECS, University of California, Berkeley. Researcher in immersive 3D authoring and radiance fields (NeRF, Gaussian splatting), working with Björn Hartmann.
- **D-ID** (1) — Digital human and visual AI agent company. D-ID animates faces from photos and offers real-time Visual AI Agents; its V4 Expressive avatars (2026) target interactive and scripted use. https://www.d-id.com
- **Daily** (1) — WebRTC video and voice infrastructure company. Provides real-time video APIs and maintains the open-source Pipecat agent framework and Pipecat Cloud. https://www.daily.co
- **Dan Pollak** (1) — Researcher, Advanced Reality Lab, Reichman University. First author of Inceptor, a pipeline that generates social VR episodes for mental-health training.
- **Daniel Duckworth** (1) — Research engineer, Google DeepMind. Google researcher, first author of SMERF, a streamable radiance field for large scenes in a web browser.
- **Danijar Hafner** (1) — Research scientist, author of the Dreamer agents. Research scientist at Google DeepMind known for the Dreamer line of world-model agents. https://danijar.com
- **Danlin Huang** (1) — Designer-researcher, School of Design Innovation, China Academy of Art. Designer and researcher who works with Reality Design Lab on speculative, body-centred mixed-reality works such as Body Oracle and FungiSync.
- **David Charatan** (1) — PhD researcher, MIT. MIT researcher, first author of pixelSplat (CVPR 2024).
- **David DeVault** (1) — Researcher in natural-language dialogue, USC Institute for Creative Technologies. Led the SimSensei Kiosk virtual human interviewer project.
- **David Ha** (1) — Researcher, first author of World Models (2018). Machine-learning researcher, then at Google Brain, later co-founder of Sakana AI; co-wrote World Models with Jürgen Schmidhuber. https://worldmodels.github.io
- **David-Paul Pertaub** (1) — Researcher, University College London (2002). First author of the 2002 virtual-audience public speaking experiment with Mel Slater and Chris Barker.
- **DeepMotion** (1) — AI motion-capture and animation company. Company known for markerless motion capture from video (Animate 3D) and SayMotion, a text-to-3D-animation tool. https://www.deepmotion.com/
- **Dehui Kong** (1) — Researcher, Karlsruhe Institute of Technology. First author of CoEmpaTeam (CHI 2026), a VR system for training cognitive empathy with LLM-driven avatars.
- **Denis Rozumny** (1) — Researcher, Meta. Meta researcher, first author of BulletGen.
- **Dian Zheng** (1) — Researcher, Shanghai AI Laboratory and Sun Yat-sen University. First author of VBench-2.0, which tests the physical and commonsense faithfulness of generated video.
- **Domna Banakou** (1) — Researcher in virtual embodiment (EventLab, University of Barcelona). Studies how virtual bodies and gradual scene changes alter perception, attitudes and anxiety.
- **Dylan Ebert** (1) — Machine learning engineer, Hugging Face. Works on 3D machine learning at Hugging Face; created 3D Arena.
- **Dynamics Lab** (1) — Generative game-engine startup. Startup that released Mirage (July 2025) and Mirage 2 (August 2025), browser-playable generative world engines; its website and launch posts were offline when checked in October 2026.
- **Egon Brunswik** (1) — Psychologist, University of California, Berkeley (1903-1955). Hungarian-born psychologist whose probabilistic functionalism and lens model asked experiments to sample situations as carefully as participants.
- **Eloi Alonso** (1) — Researcher, first author of DIAMOND. Machine-learning researcher (University of Geneva) working on diffusion world models for reinforcement learning.
- **Erzhen Hu** (1) — PhD researcher, Department of Computer Science, University of Virginia. HCI researcher on XR communication; first author of Thing2Reality with Google XR collaborators.
- **Etched** (1) — AI chip company. Startup designing Sohu, a transformer-specific inference chip; co-developed Oasis with Decart. https://www.etched.com
- **Fernanda De La Torre** (1) — Researcher, MIT Brain and Cognitive Sciences; LLMR lead author with Microsoft. Researcher who led LLMR, a Microsoft framework for creating and editing interactive mixed-reality worlds with language models.
- **Fernanda Herrera** (1) — Researcher, Stanford Virtual Human Interaction Lab. Led the large-scale Becoming Homeless studies comparing VR and traditional perspective-taking.
- **Figmin XR** (1) — Independent team behind the mixed-reality creation app Figmin XR. Makes Figmin XR, a cross-platform app (Quest, Vision Pro, HoloLens) for building and sharing mixed-reality scenes, toys and scripted objects. https://figmin.com
- **Gale Lucas** (1) — Researcher, USC Institute for Creative Technologies. Social psychologist who showed that people disclose more to a virtual human they believe is computer-controlled.
- **General Intuition** (1) — AI lab for agents acting in space and time. AI lab spun out of the game-clip platform Medal that trains agents and world models on large archives of gameplay video. https://generalintuition.com
- **Genmo** (1) — Open video-model startup. Startup that released Mochi 1, a 10B-parameter open text-to-video model under Apache 2.0. https://www.genmo.ai
- **Gracia** (1) — Volumetric Gaussian video company. Company that streams 4D Gaussian splat video to Quest, Pico, Apple Vision Pro, desktop and the browser, and in 2026 describes its focus as world reconstruction models for physical AI. https://gracia.ai/
- **Guanjun Wu** (1) — Researcher, Huazhong University of Science and Technology. First author of 4D Gaussian Splatting for Real-Time Dynamic Scene Rendering (CVPR 2024).
- **Guanzhi Wang** (1) — AI researcher (Caltech, NVIDIA). Caltech PhD researcher working with NVIDIA; first author of Voyager (2023), an LLM agent that explores Minecraft by writing and storing code skills.
- **Guibao Shen** (1) — Researcher in stereo conversion. HKUST (Guangzhou) researcher, first author of StereoPilot, developed during an internship with Kuaishou's Kling team.
- **Guido Makransky** (1) — Professor of educational psychology, University of Copenhagen. Studies learning in immersive VR; co-authored CAMIL, which explains when presence and agency help or hurt learning.
- **Gustav Bøg Petersen** (1) — Researcher working with Stanford's Virtual Human Interaction Lab. Studies learning and environmental attitudes in VR; first author of the OceanSpeak conversational-AI study.
- **Guy Tevet** (1) — Researcher, Tel Aviv University. Tel Aviv University researcher (with Amit Bermano and Daniel Cohen-Or) and first author of the Human Motion Diffusion Model (MDM, ICLR 2023). https://guytevet.github.io/
- **Habin Lim** (1) — Researcher, Korea University. Habin Lim is co-first author of FacePlex (2026), a full-duplex speech and facial-motion model with Gaussian-splatting rendering, from Korea University and Klleon. https://hahminlew.github.io/faceplex
- **Hal Hershfield** (1) — Professor of marketing and behavioral decision making, UCLA Anderson School of Management. Studies the psychology of the future self; with Stanford VHIL he showed that meeting an aged avatar of oneself increases saving.
- **Hanwen Liang** (1) — Researcher, University of Toronto. PhD researcher at the University of Toronto and first author of Wonderland, done with Snap Research.
- **Hanxue Liang** (1) — Researcher, University of Cambridge / NVIDIA. First author of BTimer, NVIDIA's feed-forward bullet-time reconstruction model.
- **Haotong Lin** (1) — Researcher, ByteDance Seed / Zhejiang University. First author of Depth Anything 3.
- **Haoyi Duan** (1) — Researcher, Stanford University. Works with Jiajun Wu and Fei-Fei Li; first author of WorldScore. https://haoyi-duan.github.io
- **Haoyu Wang** (1) — Researcher, Dyson School of Design Engineering, Imperial College London. HCI researcher on haptics and generative AI in mixed reality; led Prop-Chromeleon with collaborators at the University of Toronto's Dynamic Graphics Project.
- **Haozhe Xie** (1) — Researcher, S-Lab, Nanyang Technological University. Researcher in Ziwei Liu's S-Lab at NTU, first author of CityDreamer and CityDreamer4D. https://www.infinitescript.com
- **Hedra** (1) — Generative character video company. Hedra makes audio-driven character video models (Character-3) and a studio for talking characters. https://www.hedra.com
- **Heng Yu** (1) — PhD researcher, Carnegie Mellon University. First author of 4Real (NeurIPS 2024), done with Snap Research.
- **HeyGen** (1) — AI video avatar platform. HeyGen offers AI avatar video creation and, through LiveAvatar, a real-time avatar streaming API. https://www.heygen.com
- **Ho Kei Cheng** (1) — Computer-vision researcher (UIUC). Ho Kei (Rex) Cheng is a researcher known for video object segmentation (XMem, Cutie) and the MMAudio video-to-audio model, developed with Sony AI. https://hkchengrex.com
- **Huadai Liu** (1) — Audio generation researcher (Zhejiang University). Huadai Liu researches text-, video- and spatial-audio generation at Zhejiang University.
- **Hugues Bruyère** (1) — Partner and innovation lead, Dpt. (Montreal). Creative technologist who prototypes interactive installations and mixed-reality experiences with real-time generative models.
- **Hunter Hoffman** (1) — Research scientist, University of Washington. Developed SnowWorld with David Patterson to distract burn patients from pain during wound care.
- **Jacob Barker** (1) — First author of VORTeX (2026). Develops the Virtual Operating Room Team Experience for training and evaluating surgical teamwork.
- **Jaewook Lee** (1) — PhD researcher, Makeability Lab, University of Washington. HCI researcher on AI-powered augmented reality; led ImaginateAR with Niantic Spatial.
- **Jaeyeon Kim** (1) — Audio-visual learning researcher (Seoul National University). Jaeyeon Kim researches audio-visual generation at Seoul National University's Vision and Learning Lab. https://jaeyeonkim99.github.io/visage/
- **Jaeyoung Chung** (1) — Researcher, Computer Vision Lab, Seoul National University. Co-first author of LucidDreamer in Kyoung Mu Lee's lab at Seoul National University.
- **Jawset** (1) — Developer of Postshot. Small software company that makes Postshot, a desktop application for training and editing radiance fields and Gaussian splats on a local GPU. https://www.jawset.com/
- **Jia-Peng Zhang** (1) — Researcher, Tsinghua University. Tsinghua University researcher and first author of UniRig (SIGGRAPH 2025), developed with VAST. https://zjp-shadow.github.io/
- **Jianhong Bai** (1) — Researcher in camera-controlled video. Zhejiang University researcher who developed ReCamMaster with Kuaishou's Kling team. https://jianhongbai.github.io/
- **Jiaxiang Tang** (1) — PhD researcher, Peking University. Peking University researcher and first author of DreamGaussian (ICLR 2024 oral), an early generative use of 3D Gaussian splatting. https://me.kiui.moe/
- **Jim Blascovich** (1) — Social psychologist, University of California, Santa Barbara. Co-founded UCSB's Research Center for Virtual Environments and Behavior and argued for immersive VR as a method for social psychology.
- **Jing Tan** (1) — Researcher in immersive video generation. CUHK researcher, first author of Imagine360.
- **Jonathan Steuer** (1) — Communication researcher (Stanford University, 1992). Wrote the 1992 paper that defined virtual reality by the experience of telepresence and its two determinants, vividness and interactivity.
- **Jonathan Tseng** (1) — Researcher, Stanford University. Stanford researcher (with C. Karen Liu) and first author of EDGE, editable dance generation from music (CVPR 2023). https://edge-dance.github.io/
- **Junyi Zhang** (1) — PhD researcher, UC Berkeley. First author of MonST3R (ICLR 2025).
- **K R Prajwal** (1) — Researcher in lip sync and speech-driven video. K R Prajwal, then at IIIT Hyderabad, is first author of Wav2Lip (ACM Multimedia 2020).
- **K. Anders Ericsson** (1) — Psychologist, Florida State University (1947-2020). Swedish psychologist who founded the study of expert performance and defined deliberate practice.
- **Kaifeng Zhao** (1) — PhD researcher, ETH Zürich. ETH Zürich researcher (with Siyu Tang) and first author of ARDY (SIGGRAPH 2026), developed at NVIDIA. https://research.nvidia.com/labs/sil/projects/ardy/
- **Kaixin Yao** (1) — Researcher, ShanghaiTech University and Deemos. First author of CAST (SIGGRAPH 2025 Best Paper), developed at ShanghaiTech University and Deemos.
- **Kamilla Bergsnev** (1) — First author of a 2026 systematic review on AI for VR exposure therapy. Researcher who reviewed how artificial intelligence is used to tailor VR exposure therapy.
- **Konstantin W. Kühlem** (1) — Researcher, Visual Computing Institute, RWTH Aachen University. First author of a latency-optimized LLM dialogue system for embodied conversational agents in VR (IVA 2025).
- **Krea** (1) — Real-time creative AI tools. Creative-tool company known for real-time image generation; released the open Krea Realtime 14B video model in October 2025. https://www.krea.ai
- **Kyle Johnsen** (1) — Computer scientist (University of Florida, later University of Georgia). Built and validated life-size virtual patients for medical interview training with Benjamin Lok's group.
- **LemonSlice** (1) — Interactive avatar model company. LemonSlice builds real-time video diffusion models for interactive avatars (LemonSlice-2, 2025; Character World Model-1, 2026) that animate any character from one image. https://lemonslice.com
- **Light in the Head** (1) — Studio of Marc Da Costa and Matthew Niederhauser. Artist duo working with machine learning, VR and installations; also co-founders of Sensorium.
- **Lihan Jiang** (1) — Researcher, USTC / Shanghai AI Lab. First author of AnySplat (SIGGRAPH Asia 2025).
- **Lihe Yang** (1) — Researcher, The University of Hong Kong. PhD researcher with Hengshuang Zhao at HKU, first author of Depth Anything and Depth Anything V2 (with ByteDance/TikTok). https://liheyoung.github.io
- **Linyi Jin** (1) — PhD researcher, University of Michigan / Google DeepMind. First author of Stereo4D (CVPR 2025), built with Google DeepMind from internet VR180 videos.
- **Liquid City** (1) — Design studio founded by Keiichi Matsuda. Studio led by the designer and filmmaker Keiichi Matsuda (Hyper-Reality, Merger) that designs AR, AI agents and spatial interfaces. https://www.liquid.city
- **LiveKit** (1) — Real-time media infrastructure company. Builds an open-source WebRTC media server, the LiveKit Agents framework and LiveKit Cloud. https://livekit.io
- **Longwen Zhang** (1) — Researcher, ShanghaiTech University / Deemos. First author of CLAY (SIGGRAPH 2024), the 3D-native generative model that became Rodin Gen-1.
- **Lu Ling** (1) — Researcher, Purdue University. First author of DL3DV-10K, a large real-scene video dataset for 3D vision. https://dl3dv-10k.github.io/DL3DV-10K/
- **Lukas Höllein** (1) — Researcher, Technical University of Munich. PhD researcher in Matthias Niessner's Visual Computing & AI lab at TUM, first author of Text2Room. https://lukashoel.github.io
- **Lvmin Zhang** (1) — Researcher in controllable generation. Stanford PhD researcher, author of ControlNet, IC-Light and FramePack.
- **Mar Gonzalez-Franco** (1) — XR research scientist (Google; formerly Microsoft Research). Neuroscientist and engineer working on avatars, embodiment and social XR; led a VR replication of the Milgram paradigm.
- **Martin de La Gorce** (1) — Researcher, Microsoft. Microsoft researcher, first author of VoluMe (2025).
- **Matt Deitke** (1) — AI researcher (Objaverse, Objaverse-XL). Led the Objaverse and Objaverse-XL 3D datasets at the Allen Institute for AI. https://mattdeitke.com
- **Matthew J. Smith** (1) — Social work researcher (Northwestern University, later University of Michigan). Lead author of trials of Virtual Reality Job Interview Training with the virtual interviewer Molly Porter.
- **Mehdi Moussaïd** (1) — Research scientist, Max Planck Institute for Human Development. Studies crowd behavior and collective dynamics, including crowd evacuations with real participants in shared virtual environments.
- **Meituan** (1) — Technology company (MeiGen / LongCat teams). Meituan's MeiGen team released MultiTalk and InfiniteTalk, open models for audio-driven talking video and dubbing. https://www.meituan.com
- **Meng-Li Shih** (1) — Researcher (Virginia Tech, then University of Washington). First author of 3D Photography using Context-aware Layered Depth Inpainting (CVPR 2020), with Jia-Bin Huang and Johannes Kopf. https://shihmengli.github.io
- **Michael Wiesing** (1) — Researcher at the EventLab, University of Barcelona. Studies how VR experiences carry over into beliefs and actions in physical reality.
- **Midjourney** (1) — Independent image and video generation lab. Self-funded lab known for its aesthetic image models; released its first video model in June 2025. https://www.midjourney.com
- **Moonvalley** (1) — Video-generation company for filmmakers. Builds Marey, a video model trained only on licensed footage, together with the studio Asteria. https://www.moonvalley.com
- **Moreah Zisquit** (1) — Researcher, Reichman University. First author of a 2025 formative study that adds an AI agent to VR self-talk counselling.
- **Mursion** (1) — Immersive simulation training company. Grew out of research on human-in-the-loop teaching simulators; trained simulation specialists voice and steer avatars live, and the company now markets AI-powered simulations. https://www.mursion.com/
- **Naisha Agarwal** (1) — Researcher, University of California, Los Angeles; Microsoft Research collaborator. HCI researcher who led Storycaster with Judith Amores and Andrew D. Wilson at Microsoft Research.
- **Nels Numan** (1) — PhD researcher, University College London; Microsoft Research collaborator. Researcher in collaborative mixed reality and telepresence; first author of SpaceBlender and co-author of XR Blocks.
- **NetEase Games** (1) — Video game developer and publisher. Chinese game company behind Justice Online, Eggy Party and NARAKA: BLADEPOINT; it shipped LLM-driven NPCs in Justice Online Mobile in 2023 and an on-device NVIDIA ACE AI teammate in NARAKA: BLADEPOINT Mobile PC Version in 2025. https://www.neteasegames.com/
- **Nick Yee** (1) — Researcher on avatars and online games (Stanford VHIL; later co-founder of Quantic Foundry). Named the Proteus effect with Jeremy Bailenson as a PhD student at Stanford, then studied player motivation at scale.
- **Nicolas Moenne-Loccoz** (1) — Researcher, NVIDIA. NVIDIA researcher, first author of 3D Gaussian Ray Tracing (3DGRT).
- **Nikhil Keetha** (1) — PhD researcher, CMU / Meta. First author of MapAnything, a Meta and Carnegie Mellon model for metric 3D reconstruction.
- **Nozomu Iwai** (1) — Researcher, Preferred Networks. Researcher at Preferred Networks; first author, with Fabrice Matulic, of the AR talking-objects study (CHI 2025 Extended Abstracts).
- **OpenBMB** (1) — Open-source model community of ModelBest and Tsinghua NLP. OpenBMB is the open-source effort behind the MiniCPM models, led by ModelBest with Tsinghua University's NLP lab. https://www.openbmb.cn
- **Overworld** (1) — Open-weight world-model startup. Startup releasing open-weight, real-time diffusion world models (Waypoint) that run locally on consumer GPUs, plus the open-source Biome client. https://over.world
- **Patrick Kenny** (1) — Researcher, USC Institute for Creative Technologies (2000s). Led virtual human and virtual patient projects at USC ICT, including the 2007 I/ITSEC overview of building interactive virtual humans for training.
- **Patrick McClanahan** (1) — Criminologist, Pennsylvania Virtual Burglary Project (Max Planck Institute for the Study of Crime, Security and Law). Led the Pennsylvania arm of the Virtual Burglary Project, which brought VR burglary tasks into US prisons and released its virtual neighborhoods as open access.
- **Peiwen Sun** (1) — Spatial audio generation researcher (HKUST). Peiwen Sun researches language-driven audio generation at the Hong Kong University of Science and Technology. https://peiwensun2000.github.io/bewo/
- **Pika** (1) — Consumer video-generation startup. Founded in 2023 by Stanford PhD students; known for Pika 1.0 and playful editing effects. https://pika.art
- **Polycam** (1) — 3D capture app company. Maker of a phone, web and drone 3D capture app covering LiDAR, photogrammetry and Gaussian splats. https://poly.cam/
- **Preferred Networks** (1) — Japanese AI company. Tokyo-based AI company that develops deep-learning models, AI chips and applied research, including AR and character interaction. https://www.preferred.jp/en/
- **Princeton Vision & Learning Lab** (1) — Jia Deng's computer-vision lab at Princeton University. Academic lab led by Jia Deng that develops the Infinigen procedural world generator. https://pvl.cs.princeton.edu
- **Proxima** (1) — Indie game studio. Small studio behind Suck Up!, a comedy game in which players talk AI-driven townsfolk into letting a vampire in. https://www.playsuckup.com/
- **Qi Wu** (1) — Researcher, NVIDIA. NVIDIA researcher, first author of 3DGUT (CVPR 2025).
- **Qian Wang** (1) — Researcher in panoramic video generation. Peking University (Shenzhen Graduate School) researcher, first author of 360DVD.
- **Ramon Oliva** (1) — Researcher, EventLab, University of Barcelona. Develops VR systems and social VR studies with Mel Slater's group, including a 2026 study of an avatar swap and an LLM-driven Alan Turing on a conference panel.
- **Replicate** (1) — Model hosting platform (joining Cloudflare). Runs open and proprietary models behind versioned HTTP endpoints; creator of the Cog container format. https://replicate.com
- **Roberto Coviello** (1) — XR and AI engineer; author of QuestCameraKit. Engineer who maintains QuestCameraKit, open-source samples for Meta Quest's Passthrough Camera API. https://xrdevrob.com
- **Ruiqi Gao** (1) — Research scientist, Google DeepMind. Generative-model researcher at Google DeepMind and co-first author of CAT3D and CAT4D.
- **Rundi Wu** (1) — PhD researcher, Columbia University / Google DeepMind. First author of CAT4D (CVPR 2025), built at Google DeepMind.
- **Ruofei Du** (1) — Interactive perception and graphics lead, Google XR. Researcher in interactive graphics and AI for XR; leads XR Blocks and co-authored Thing2Reality and Sensible Agent. https://duruofei.com
- **Ruoshi Liu** (1) — PhD researcher, Columbia University. Columbia University researcher (with Carl Vondrick's lab and Toyota Research Institute) and first author of Zero-1-to-3. https://ruoshiliu.github.io/
- **Ryutaro Kurai** (1) — Researcher, Cluster, Inc. (Cluster Metaverse Lab). Researcher at the Japanese social VR platform Cluster, working on LLM-based creation tools for its users.
- **SHOTPROS** (1) — EU Horizon 2020 research project on VR police training (2019-2022). Consortium of police organizations, universities and companies that studied decision-making and acting under stress and built a VR training framework. https://shotpros.eu/
- **Sand AI** (1) — Video-generation startup. Startup that open-sourced MAGI-1, a 24B-parameter autoregressive video model, in April 2025. https://sand.ai
- **Sesame** (1) — Voice AI and hardware company. Sesame, co-founded by Oculus co-founder Brendan Iribe, builds conversational voice agents and the Conversational Speech Model (CSM), with eyewear announced. https://www.sesame.com
- **Seung Wook Kim** (1) — Researcher at NVIDIA, first author of GameGAN. Researcher at NVIDIA's Toronto AI lab working on neural simulation of games and driving.
- **Shenghai Yuan** (1) — Researcher in real-time video generation. Peking University researcher (Li Yuan's group, with ByteDance), first author of Helios.
- **Shenhan Qian** (1) — PhD researcher, Technical University of Munich. Shenhan Qian, in Matthias Niessner's group at TUM, is first author of GaussianAvatars (CVPR 2024). https://shenhanqian.github.io
- **Sherry Yang** (1) — Researcher, first author of UniSim. Researcher (Google DeepMind and UC Berkeley at the time of UniSim) working on video models as real-world simulators.
- **Shijie Zhou** (1) — Researcher, University of California, Los Angeles. PhD researcher in Achuta Kadambi's lab at UCLA, first author of DreamScene360.
- **Shitao Tang** (1) — Researcher, Simon Fraser University. PhD researcher in Yasutaka Furukawa's group at Simon Fraser University, first author of MVDiffusion.
- **Shuai Yang** (1) — Researcher in long video generation. Researcher affiliated with NVIDIA and HKUST (Guangzhou), first author of LongLive.
- **Shuai Yang** (1) — Researcher, Shanghai Jiao Tong University and Shanghai AI Laboratory. First author of LayerPano3D (SIGGRAPH 2025), written with CUHK, Stanford and NTU collaborators.
- **Shunsuke Saito** (1) — Research scientist, Meta Codec Avatars Lab. Shunsuke Saito leads research on Gaussian Codec Avatars at Meta, including Relightable Gaussian Codec Avatars (CVPR 2024) and Large-scale Codec Avatars (CVPR 2026). https://shunsukesaito.github.io
- **Shuzhe Wang** (1) — Researcher, Aalto University / NAVER LABS Europe. First author of DUSt3R (CVPR 2024), developed at NAVER LABS Europe.
- **Siddharth Ahuja** (1) — Developer of BlenderMCP. Independent developer who released BlenderMCP, an open-source Model Context Protocol bridge between language models and Blender.
- **Sijie Zhao** (1) — Researcher in stereo video generation. Tencent researcher, co-first author of StereoCrafter.
- **Simile** (1) — Human-behavior simulation company. Company founded by Joon Sung Park, Michael Bernstein and Percy Liang that turns generative-agent research into simulations of customers and populations. It came out of stealth in February 2026. https://www.simile.com/
- **Sofia Adelaide Osimo** (1) — Researcher on virtual embodiment (EventLab, University of Barcelona). Lead author of the 2015 self-counselling study in which participants alternate between their own body and Sigmund Freud's.
- **Sofia Seinfeld** (1) — Researcher in virtual embodiment (EventLab, University of Barcelona). Lead author of the study that embodied domestic-violence offenders in the body of a victim.
- **Solène Neyret** (1) — Researcher at the EventLab, University of Barcelona. Studies how embodied perspective-taking in VR changes conformity and harmful group behavior.
- **Soul AI Lab** (1) — AI lab of the Soul social app. Soul AI Lab, the research arm of the Soul social platform, open-sourced SoulX-FlashTalk, a 14B real-time streaming avatar model.
- **Stanislaw Szymanowicz** (1) — Researcher, University of Oxford (VGG). PhD researcher in Oxford's Visual Geometry Group (Splatter Image, Flash3D) and first author of Bolt3D, done with Google. https://szymanowiczs.github.io
- **Stanley J. Hamstra** (1) — Medical education researcher (University of Ottawa; ACGME). Studies simulation-based training; first author of the 2014 reappraisal of fidelity in simulation.
- **Strivr** (1) — Immersive training company. Spun out of Stanford's VHIL in 2015 to train athletes with 360-degree VR, then scaled VR training to employers such as Walmart; by 2026 it markets AI quality assurance on smart glasses. https://www.strivr.com/
- **Suibi Che-Chuan Weng** (1) — HCI researcher, ATLAS Institute, University of Colorado Boulder. Researcher in creative mixed reality and generative AI; first author of Editing Reality (DIS 2026).
- **Suno** (1) — AI music company. Suno makes a widely used song generator that writes and sings complete tracks from a prompt. https://suno.com
- **Sylvia Xueni Pan** (1) — Researcher in virtual social interaction, Goldsmiths, University of London. Studies social interaction with virtual characters and co-wrote, with Antonia Hamilton, the standard review on using VR to study social interaction.
- **Synthesia** (1) — Enterprise AI video and avatar platform. Synthesia makes AI avatar videos for corporate training and communication, and in 2026 added real-time Interactive Avatars and the Sessions platform for roleplay and interviews. https://www.synthesia.io
- **Tabitha Peck** (1) — Computer scientist, Davidson College. Studies virtual embodiment and avatar effects; lead author of the 2013 black-avatar implicit-bias study with Mel Slater's group.
- **Taekyung Ki** (1) — PhD researcher, KAIST. Taekyung Ki is first author of Avatar Forcing (CVPR 2026), a real-time interactive head avatar that reacts to the user's voice and motion. https://taekyungki.github.io
- **Talespin** (1) — Immersive soft-skills training company, now part of Cornerstone. Built VR soft-skills simulations with virtual humans and the no-code authoring tool CoPilot Designer; talespin.com now redirects to Cornerstone's immersive-learning platform. https://www.cornerstoneondemand.com/platform/immersive-learning/
- **Tencent** (1) — Chinese technology and games company. Shenzhen-based internet and games company; several of its research teams, besides Hunyuan, publish interactive video work. https://www.tencent.com
- **Tencent ARC Lab** (1) — Applied research center of Tencent PCG. Tencent research lab working on visual generation and editing, including StereoCrafter and Rolling Forcing. https://arc.tencent.com
- **The Khronos Group** (1) — Graphics and spatial-computing standards consortium. Open industry consortium behind glTF, OpenXR, Vulkan and WebGL. https://www.khronos.org
- **Thomas Müller** (1) — Researcher, NVIDIA. NVIDIA researcher, first author of Instant Neural Graphics Primitives (instant-ngp).
- **Tianwei Yin** (1) — Researcher in fast generative models. MIT PhD researcher, first author of DMD distillation and CausVid.
- **Tianye Li** (1) — Researcher, Meta Reality Labs. First author of Neural 3D Video Synthesis (DyNeRF, CVPR 2022), done at Meta Reality Labs Research.
- **Tianyi Xiao** (1) — Researcher, Institute of Cartography and Geoinformation, ETH Zurich. Researcher on spatial cognition, sketch mapping and augmented reality.
- **Tinghui Zhou** (1) — Computer vision researcher (UC Berkeley PhD). First author of Stereo Magnification (SIGGRAPH 2018), which introduced multiplane images and the RealEstate10K dataset. https://tinghuiz.github.io
- **Tom Craig** (1) — Professor of social psychiatry, King's College London. Led the AVATAR therapy trial in which people who hear voices talk with a therapist-voiced avatar of their persecutor.
- **Tomoki Itamiya** (1) — Professor, Aichi University of Technology. Researcher who builds AR and VR disaster-education tools, such as flood and earthquake simulations overlaid on real rooms and streets.
- **Tong Wu** (1) — Researcher at Stanford University. Researcher in Gordon Wetzstein's group at Stanford working on 3D-aware video generation.
- **Transitional Forms** (1) — AI entertainment studio founded by Pietro Gagliano. Studio that builds stories and games around live AI agents, from the dynamic film Agence (with the National Film Board of Canada) to multi-agent story simulations. https://www.transforms.ai
- **Tsinghua University FIB Lab** (1) — Research lab, Department of Electronic Engineering, Tsinghua University. Lab led by Yong Li working on urban science and LLM agents; released the AgentSociety simulator in 2025.
- **Tu Anh Nguyen** (1) — Speech researcher (Meta AI / ENS–Inria). Tu Anh Nguyen worked on textless spoken language modelling at Meta AI and the Cognitive Machine Learning team in Paris.
- **Unity** (1) — Game engine company. Maker of the Unity engine, used by a large share of XR and mobile games and many VR research labs. https://unity.com
- **Uriel Singer** (1) — Research scientist, Meta AI. Meta researcher, first author of Make-A-Video and of MAV3D (text-to-4D, 2023).
- **Valve** (1) — Game company and maker of Steam. Runs Steam and makes Index, Steam Deck and the Steam Frame headset. https://store.steampowered.com
- **Varjo** (1) — XR headset and reconstruction company. Finnish maker of high-resolution XR headsets that launched Teleport, a cloud service that turns phone or camera footage into Gaussian splat scenes. https://varjo.com/
- **Vincent Leroy** (1) — Researcher, NAVER LABS Europe. NAVER LABS Europe researcher, first author of MASt3R (ECCV 2024).
- **Volcano Engine (BytePlus)** (1) — ByteDance's cloud platform. ByteDance's cloud and model-as-a-service business, branded BytePlus outside China. https://www.volcengine.com
- **W3C Immersive Web Working Group** (1) — Web standards body. The World Wide Web Consortium group that writes the WebXR Device API and its modules. https://www.w3.org/immersive-web/
- **Waymo** (1) — Autonomous-driving company of Alphabet. Alphabet's self-driving company, operating driverless ride-hailing in several U.S. cities. https://waymo.com
- **Weixi Feng** (1) — Researcher, UC Santa Barbara. PhD researcher in William Wang's group at UCSB, first author of LayoutGPT. https://weixi-feng.github.io
- **XREAL** (1) — AR glasses company. Chinese maker of display glasses (formerly Nreal) and of XREAL AURA, Android XR glasses co-developed with Google. https://www.xreal.com
- **Xindi Wu** (1) — Researcher at Princeton and NVIDIA. PhD researcher at Princeton University who worked with NVIDIA on memory for video world models.
- **Xinyang Li** (1) — PhD researcher, MAC Lab, Xiamen University. First author of FlashWorld, developed with Tencent Hunyuan.
- **Xinyu Ning** (1) — First author of a systematic review of generative AI in XR (Lik-Hang Lee's group). Researcher who mapped the 2023-2025 literature combining generative AI with extended reality.
- **Xuanchi Ren** (1) — Research scientist, NVIDIA. Researcher at NVIDIA's Toronto AI Lab, first author of GEN3C and co-author of Lyra. https://xuanchiren.com
- **Xudong Xu** (1) — Researcher in audio-visual learning. Xudong Xu works on audio-visual learning and 3D-aware generation; Sounding Bodies was developed with Meta Reality Labs Research.
- **Xueyang Wang** (1) — Researcher, Tsinghua University. HCI researcher on cross-reality authoring and spatially grounded generation; first author of Roomify (CHI 2026).
- **Xun Huang** (1) — Researcher in generative video. Research scientist (Adobe Research at the time of Self Forcing), known for AdaIN style transfer and real-time video diffusion.
- **Yicong Hong** (1) — Research scientist, Adobe Research. Researcher at Adobe Research and first author of LRM: Large Reconstruction Model for Single Image to 3D (ICLR 2024).
- **Yifan Wang** (1) — Researcher, Zhejiang University. First author of FreeTimeGS (CVPR 2025) in the ZJU3DV group.
- **Yue Yang** (1) — Researcher, University of Pennsylvania. PhD researcher at the University of Pennsylvania who led Holodeck with the Allen Institute for AI. https://yueyang1996.github.io
- **Zehao Yu** (1) — Researcher, University of Tübingen. PhD researcher in Andreas Geiger's group, first author of Mip-Splatting.
- **Zeqi Xiao** (1) — Researcher, first author of WorldMem. Researcher at Nanyang Technological University (S-Lab) working on consistent video world simulation. https://xizaoqu.github.io
- **Zhan Li** (1) — Researcher, Portland State University / OPPO US Research. First author of Spacetime Gaussian Feature Splatting (CVPR 2024).
- **Zhan Xu** (1) — Researcher (UMass Amherst, later Adobe). First author of RigNet (SIGGRAPH 2020), done at UMass Amherst with Evangelos Kalogerakis. https://zhan-xu.github.io/
- **Zhen Xu** (1) — Researcher, Zhejiang University. ZJU3DV researcher behind EasyVolcap and first author of Representing Long Volumetric Video with Temporal Gaussian Hierarchy (SIGGRAPH Asia 2024).
- **Zhengqi Li** (1) — Research scientist, Google DeepMind. Google researcher working on dynamic scene reconstruction, first author of MegaSaM (CVPR 2025).
- **Zhipu AI** (1) — Foundation-model company spun out of Tsinghua University. Maker of the GLM language models and the open CogVideoX video models behind its Qingying product. https://www.zhipuai.cn
- **Zhiyang Guo** (1) — PhD researcher, University of Science and Technology of China. First author of Make-It-Animatable (CVPR 2025), which rigs humanoid meshes and Gaussian splats in under a second. https://jasongzy.github.io/
- **Zhuangze Hou** (1) — Researcher, School of Creative Media, City University of Hong Kong. HCI researcher on AI-assisted spatial design in virtual reality; first author of EchoLadder (UIST 2025).
- **Ziming Li** (1) — Researcher, Rochester Institute of Technology. First author of an LLM-driven VR job-communication trainer for autistic individuals (CHI EA 2024) in Roshan Peiris's lab.
- **Ziyi Wu** (1) — Researcher in generative 3D and video. University of Toronto PhD researcher; first author of 360Anything, done at Google DeepMind.
- **bilibili** (1) — Chinese video platform (Index team). bilibili is a Chinese video community whose Index team develops the open IndexTTS speech models. https://www.bilibili.com
- **fal** (1) — Generative-media inference platform. Hosts more than 1,000 image, video, audio and 3D models behind one API and offers serverless GPUs. https://fal.ai
