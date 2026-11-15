# Vendored skills (installed 14 Nov 2026, owner request)
Copies of 5 public skill repos so every scheduled run (which clones this repo) can read them. Each folder keeps its LICENSE.
- instagram-agent-skill/ (github.com/Jakeschincariol/instagram-agent-skill, MIT): ig-reel, ig-caption, ig-carousel, ig-story, ig-viral, ig-plan, ig-audit, ig-profile, ig-comment, ig-reply, ig-dm, ig-repurpose, ig-human
- marketingskills/ (github.com/coreyhaines31/marketingskills, MIT): social, copywriting, copy-editing, marketing-psychology, ai-seo, ab-testing, marketing-ideas, reverse-engineer-marketing, ...
- remotion/ (github.com/remotion-dev/skills): remotion-best-practices (router), remotion-create, remotion-render, remotion-captions, ...
- remocn/ (github.com/Remocn/remocn, MIT): remocn, add, video, studio, changelog (ready-made Remotion animations/transitions)
- skill-creator/ (github.com/anthropics/skills, Apache-2.0)
Use: read the SKILL.md (and the references it points to) with the Read tool before the step it covers. See STYLE_GUIDE "SKILLS TO USE".
Update: git clone --depth 1 the repo and re-copy its skills folder.

## Added 15 Nov 2026 (owner: "whatever skills is mentioned install it and if useful use it in creation of all videos")
Source: the "5 free Claude skills" reel Junaid sent. Copied skill folders only (not the full repos); upstream commit in brackets.
| Folder | Upstream | What we use it for |
|---|---|---|
| hyperframes/ | heygen-com/hyperframes (e426ce4) | HTML+GSAP video rendered frame-exact with `npx hyperframes` (CLI 0.9.52 works in the sandbox, Chrome + ffmpeg found). Motion-graphics scenes, animated ₹ numbers/charts, word-synced captions, transitions. Read hyperframes/hyperframes/SKILL.md first. |
| ffmpeg-skill/ | kajisho5/ffmpeg-skill (3605d0e) | 42 stdlib ffmpeg tools: probe/check per platform, loudness (-14 LUFS), silence trim, captions, `look.py` contact sheets. Use for every final export check. |
| clipify/ | louisedesadeleer/clipify (5f6b75e) | Opus-style word-by-word captions (build_ass.py), cutting clips from long videos, 16:9 → 9:16 reframes. |
| explainroo/ | vincentsch/explainroo (733b194) | Explainer videos where every drawing appears on the spoken word (script.md + scenes.js); supports Hindi (hi). |
| openmontage/ | OpenMontageInc/OpenMontage (fecb9a1) | Collection of production skills (remotion, lottie, manim, threejs, sound-effects, video-understand, visual-style...). Many need API keys we do not have (HeyGen API, BFL, Azure); use the keyless ones. |
Third-party code: read a script before running it; never give it our keys. Sandbox limits found: HuggingFace and openaipublic are blocked by the proxy (no local Whisper model download), GitHub releases blocked for curl.
