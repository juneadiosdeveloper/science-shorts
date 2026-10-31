# Paisa Science: video style guide (realistic presenter format)

## STANDING RULE #1 (owner, 25 Oct 2026): every new video = the idea of a most-viewed video in the niche
- Never pick a topic on our own. Before every new video (long, animated Short or realistic Short), find the most-viewed videos in
  Indian personal finance (vidIQ outliers sorted by viewCount, allTime + recent, top channels: warikoo, Labour Law Advisor,
  Finance With Sharan, Pranjal Kamra, CA Rachana Ranade, Sagar Sinha; plus Hindi keyword searches) and build the video on the
  highest-viewed idea we have not used yet that can be made in our format (skip interviews, house tours, news, stock tips).
- Log the source video (title, channel, views) in tools/performance_log.md and in the script doc. Cut-downs of a long video inherit
  its source idea.
- What we take: the idea, structure, list of points and hook/title pattern (title adapted in Hindi with our keywords). What stays
  ours: script, numbers, characters, visuals, description. SEBI/education rules and number checks still apply; skip any point that
  would be a buy/sell call, a product/fund name or a sponsorship.
- Ideas used so far: warikoo "SIP KYA HAI? SIP vs LUMPSUM" (~4.5M) → long video #2 script (26 Oct, awaiting OK); warikoo "Loans jaldi repay kariye!" (~5.0M) → home-loan long video + cut-downs; Labour Law Advisor
  "5 STUPID mistakes WEALTHY people never make!" (1.6M) → 5 money mistakes Short; warikoo "40 CRORES from a 10,000 INR SALARY?" (5.07M) → 40 crore Short;
  warikoo "30,000 vs 3,00,000 vs 3,00,00,000 INR Per Month" (~1.2M) → ₹30k vs ₹3 lakh salary Short (27 Oct);
  Sharan "The Ugly Truth Behind ₹15Cr Trading" → F&O 93% Short (27 Oct); warikoo "Home Loan Mistakes That Cost You LAKHS" (~1.2M) → home loan 3 galtiyan Short (28 Oct).

Approved format (23 Oct 2026): realistic AI Indian woman presenter (same face every video, from
Runway portrait task ed8090cd-8324-47c0-803c-fae8673e2b3a), sweet Hindi female voice "Pyaari"
(ElevenLabs voice_id EHeVIpHOvJGuhp2QcMZZ, eleven_v4), she talks on camera for the hook and the
closing line, realistic Runway shots in between, number overlays on top.

## Owner feedback to fix in every new video
"Transitions disappear/fade and you can tell it is AI."

1. No fade/dissolve between shots. Use hard cuts on the beat of the voice (cut exactly where a
   sentence starts). At most a 3-4 frame quick cut, never a slow blend.
2. Never slow down or freeze a clip. Generate every shot at the length it is needed
   (use a model that respects duration, e.g. gen-4.5 / kling), or cover one line with two shots.
3. Avoid AI tells: no close-ups of hands typing, phone screens, money or text; prefer medium shots
   with small natural motion (breathing, head turn, smile, blink, slow handheld push-in).
   Check every clip frame-by-frame (start, middle, end) for face/hand morphing and regenerate bad ones.
4. Same look in every shot: same kurta, same hair, same warm home light; colour-match all clips
   and add light film grain so AI clips and lip-sync clips blend.
5. Lip-sync clips: feed the full-resolution portrait (not a thumbnail) and keep her framing identical
   to the b-roll so the cut feels like one shoot.
6. Text overlays: appear instantly on the spoken word (no slow fade-in), lighter top shading,
   creator-style captions.

## Always
- Education only (SEBI rules): no buy/sell calls, no fund names, no guaranteed returns, assumptions on screen.
- YouTube: isAiGeneratedContent = true; description line: presenter & voice are AI-generated.
- Never publish or schedule without the owner's explicit "yes".

## Content depth (owner feedback 24 Oct 2026)
"Very basic knowledge. Give something more tricky / harder so people get more interested."
- No more textbook basics (what is SIP / inflation / Rule of 72). Every Short needs a counter-intuitive twist:
  a number that surprises, a common belief proved wrong, or a hidden cost most people miss.
- Hook = the surprising claim as a question (on-screen text), answer revealed with a real calculation by ~20 s.
- Still education only: generic examples, every assumption on screen, verify every number by running it.
- Spoken lip-sync lines must avoid scam-sounding phrases ("paisa double", "guaranteed") - HeyGen blocks them.

### Topic bank (numbers verified 24 Oct 2026, assumptions are examples)
1. "9% flat" loan = ~15.7% real rate: ₹10 lakh, 5 yr, 9% flat → EMI ₹24,167, interest ₹4.5 lakh; same EMI on reducing balance = ~15.7% p.a.
2. 7% FD = losing money: 30% tax slab → 4.9% post-tax; 6% inflation → real return ≈ −1.0%/yr.
3. One extra home-loan EMI per year: ₹50 lakh, 8.5%, 20 yr (EMI ₹43,391) → loan ends in 201 months instead of 240 (~3 yr 3 mo early), interest ₹54.1 lakh → ₹43.8 lakh (~₹10.3 lakh saved).
4. Average return lie: +50% then −50% = "0% average" but ₹100 → ₹75 (−25%).

## What the biggest Indian finance channels do (research 24 Oct 2026)
Sources: OutlierKit channel analyses (warikoo 7.1M subs / 2.5B views, 88% of views from Shorts; Finance With Sharan 3.7M / 1.4B, 59% Shorts), ytubeinfluencers India finance list.
Top performers: warikoo "Loans jaldi repay kariye!" 5.0M, "40 CRORES from a 10,000 INR SALARY?" 5.0M, "SIP KYA HAI? SIP vs LUMPSUM" 4.5M,
"30,000 vs 3,00,000 vs 3,00,00,000 INR Per Month" 1.2M, "Home Loan Mistakes That Cost You LAKHS" 1.2M; Sharan: "The Ugly Truth Behind ₹15Cr Trading", "₹62 Crore Without Gold or Real Estate".
Patterns to copy (without copying their content):
1. A specific, big ₹ number in the title + first frame (lakh/crore), ideally a contrast (small input → huge cost/result).
2. "Is this POSSIBLE?" / impossible-constraint question as the hook.
3. Name a trap or mistake people make every day ("... jo aapko LAKHS ka nuksaan karata hai").
4. Contrarian "asli sach" framing: what the bank/dealer/agent does not tell you.
5. Relatable mini-story: one person (generic name, e.g. "Rahul, ₹50 lakh home loan") instead of abstract theory.
6. Loans, home loans, salary levels and tax are the highest-pull topics; basics still work only when wrapped in a shocking number.
Next order: (1) one extra home-loan EMI saves ~₹10.3 lakh, (2) "9% flat" = ~15.7%, (3) 7% FD = −1% real, (4) +50% −50% = −25%.

## Owner instruction (24 Oct 2026): next video copies the IDEA of the niche's most-viewed Short
- Most-viewed finance Short found: warikoo "Loans jaldi repay kariye! | Pay off debt faster!" (~5.0M views).
- Next Short = same idea (pay the loan off faster), our own script, numbers, presenter and visuals:
  ₹50 lakh home loan, 8.5%, 20 yr, EMI ₹43,391 → 1 extra EMI per year → loan ends after 201 months instead of 240, interest ₹54.1 lakh → ₹43.8 lakh (~₹10.3 lakh saved).
- Copy ideas/topics and hook patterns only. Never reuse anyone's script, wording, footage, thumbnails or title verbatim:
  YouTube treats copied/reused content as ineligible for YPP monetization, and it is a copyright risk.

## Owner decision (24 Oct 2026): next video is a 3–5 min LONG video (16:9), not a Short
Topic: home-loan prepayment (idea from warikoo's top video, our own script and numbers).
- Format: 16:9, 3–5 min, Hindi, Pyaari voice. Presenter on camera (HeyGen Avatar 4, aspect_ratio 16:9 set on the node) only for the
  intro (~5 s) and outro (~4 s). The rest: number/chart scenes from tools/long_sip.py template (chapters, narration-synced reveals)
  mixed with 6–8 realistic Runway shots of her (16:9, Kling 3 Std, generated at exact length).
- Budget per long video: ElevenLabs ≤ ~11k (TTS ~4.5k + lip-sync ~5.5k), Runway ≤ ~450.
- Outline: hook (Rahul, ₹50 lakh, 8.5%, 20 yr: "₹10 lakh bachane ka tareeka jo koi nahi batata") → EMI ₹43,391, total interest ₹54.1 lakh
  → why early EMIs are mostly interest (month 1: ₹35,417 of ₹43,391) → 1 extra EMI/yr: 201 months, ~₹10.3 lakh saved → other routes
  (raise EMI 5%/yr, lump-sum prepayment) → when prepaying may NOT be the best use of money (emergency fund first, compare with
  post-tax return, tax deduction on interest, check prepayment charges in the loan agreement) → summary + question for comments.
- Chapters in the description, custom thumbnail (big ₹ figure), Metricool type "video", isAiGeneratedContent true, draft first.
- Verify every number by running it; all rates are examples, not advice.
- Character decision (24 Oct 2026, owner: "take the character which can generate more views"): keep the SAME realistic AI presenter
  (not a 3D cartoon). Reason: every top Indian finance channel (warikoo, Sharan, Pranjal Kamra, CA Rachana) is led by a real-looking
  human face, which builds trust in money topics, and one face across Shorts + long videos helps viewers recognise the channel.
  To keep cost low in long videos: lip-sync only intro/outro, and use still images of her (~4 Runway credits each, slow camera move
  in our editor) plus charts for the middle, with only 2-3 short Runway video shots.

## Standing role (owner, 24 Oct 2026)
Claude acts as the channel's experienced social media / SEO manager, without being told each step:
views, likes, comments, subscribers and monetization (YPP) are the goal of every decision.
Every upload ships with: search-first title < 60 chars (2 options for Test & Compare), 2–3 thumbnails (max 3 words, big ₹ figure,
shocked face, never the title repeated), keyword-rich Hindi/Hinglish description with chapters, tags, pinned first comment that asks a
question, end screen + Related Video links, best posting time from Metricool. Every daily run reviews performance and changes
something concrete. Comments: reply to every comment within 24 h when a tool can read/reply YouTube comments (Metricool MCP cannot
today); until then draft replies for Junaid and ask him to connect a comments-capable tool.

## Formats (24 Oct 2026)
- Long videos (16:9, ~4:30): animated 3D, Priya (cartoon character A, Runway task 286104ef-e448-41e5-b1e4-c3e4debc6957) + Gullu
  (golden piggy-bank sidekick). Approved script: https://claude.ai/artifact/CMJg2PfPQgyAyRvqwh1Rgw (home loan prepayment).
  Each long video also gives 3 Shorts (9:16) linked to it with Related Video.
- Daily-feed Shorts: realistic presenter format (above) for new topics.
- Cadence to fit ~100k ElevenLabs/month: 1 long video/week (~11.5k) + its 3 cut-down Shorts (no new lip-sync) + ~2 new realistic
  Shorts/week (~5k each).

## vidIQ (connected 24 Oct 2026)
- Budget alert 26 Oct: 40 credits left until 24 Nov: 1 title score per upload, analytics every 2-3 days, comments Wed + Sat only.
- Account knowledgekaadda496@gmail.com, free plan: 150 credits/month (most calls cost 5, resets on the 24th). Budget ~25 calls/month:
  1 keyword research + 2 title scores per upload, 1 channel-comments check every 2-3 days, outliers once a week for topics.
- Paisa Science channel (UCGSINJTgGLSXZ4e_cIqQnYQ) IS connected to vidIQ (confirmed 25 Oct 2026). Per-video analytics: vidiq_channel_analytics
  dimensions=[video] (Metricool's YouTube video metrics come back empty for this channel). Comments: vidiq_video_comments channelId, every 2-3 days.
- Comment replies: vidIQ publishes immediately, so each reply text needs Junaid's explicit OK in chat before posting (draft with
  vidiq_generate_comment_replies / by hand, show him, then post).
- First results: "home loan mistakes" ~20.5k/mo, "home loan tips" ~11.5k (+33%), "home loan prepayment" ~7.4k (+90%),
  "home loan prepayment reduce emi or tenure" ~4.5k. Title scores (long): "₹50 Lakh Loan Pe ₹54 Lakh Byaaj? 3 Tareeke Se Bachao" 76,
  "Home Loan Jaldi Kaise Khatam Kare? ₹19 Lakh Bachao 😱" 72.

## Instagram cross-posting (owner, 24 Oct 2026)
Owner rule (29 Oct 2026, "yes"): EVERY video goes to all 3 platforms, no exceptions (a repeat clip gets a new hook line + caption on IG). YouTube + Facebook at 16:00, Instagram Reel at 18:00 and its Story at 18:10 (Metricool: IG best hours 18:00 / 10:00, 16:00 weaker).
Every YouTube upload also goes to Instagram AND the Facebook Page (separate Metricool posts, facebookData type REEL, YouTube channel link https://www.youtube.com/channel/UCGSINJTgGLSXZ4e_cIqQnYQ in the FB first comment) at the same time (same Metricool post, provider instagram added, own caption).
Status: Instagram NOT yet connected to Metricool brand 7570802 (only YouTube) — Junaid must connect a Professional
(Creator/Business) Instagram account in Metricool first.
Rules (checked Oct 2026):
- Max 5 hashtags per Reel/post (Instagram limit since Dec 2025). Use 5 specific ones, not #reels/#explore:
  1 broad niche (#PersonalFinance or #FinanceInHindi), 2-3 topic (#HomeLoan #EMI ...), 1 brand (#PaisaScience).
- Search on Instagram works on keywords in the caption and on-screen text more than hashtags: first line = hook +
  main search phrase in Hinglish ("Home loan jaldi kaise khatam karein?"), then 2-4 short lines of value, a question CTA,
  "Save karo" + "Share karo us dost ko jiska loan hai", then disclaimer + AI line, then the 5 hashtags.
- Format: Shorts → Reel (9:16) with instagramData.type REEL, showReelOnFeed true, isAiGenerated true, first comment = question.
  Long 16:9 videos → post the 9:16 cut-down Reel (Byaaj Monster / quiz / step-up) with "Full video YouTube pe — link bio mein",
  not the 16:9 file.
- Story with YouTube link: the Instagram API cannot add link stickers, so schedule the Story with autoPublish false
  (Metricool sends Junaid a phone notification; he adds the link sticker and posts, ~10 s). Keep the channel link in bio.
- Collab/trending audio cannot be added via API reliably; keep our own music.

## Long-video cut-downs (25 Oct 2026)
- tools/vcut.py <long.mp4> <start> <end> <out> "<top1>|<top2>" "<assumption>" "<cta1>|<cta2>": 1080x1920, blurred background,
  16:9 frame in the middle, headline above, assumption under the video, CTA below (same look as the Instagram teaser).
- Start the cut ON the question/hook line (no intro), end on the punchline so the loop replays into the question.
- Line start times: rebuild the anim.py timeline (durs.json + GAP/LONG_GAP_AFTER/GAP_OVERRIDE) instead of guessing.
- Home-loan cut-downs: #1 quiz A-or-B (83.1-123.15 s, Tue 27), #2 Byaaj Monster 82% (12.61-40.67 s, Thu 29, YT+FB only), #3 lump sum
  + "tenure kam, EMI nahi" (123.15-145.56 s, Fri 30). Step-up cut dropped (the quiz already reveals it).
- New animated Shorts (27 Oct): ~45 s max, 8 lines, last line = comment CTA (no subscribe tail), atempo 1.18. IG Reels of 58-73 s held only 18-20%.
- Keep cut-downs <= 30 s (IG 58 s teaser held only ~18%; 22-30 s Shorts hold 51-72%). No emoji in vcut.py text (renders as a box).

## Animated Shorts: Priya + Chintu (owner, 25 Oct 2026)
- Owner asked for a cartoon girl + monkey built on the idea of the niche's most-viewed video. New sidekick **Chintu** (cheeky cartoon
  monkey, yellow t-shirt, backwards red cap; Runway ref task cb8d524b-eb2a-4b41-a044-4b1b3dea8c81), voice "Yatin – Fun & Playful
  Character" 7M0JpWdLkoBBL8M1moPi (eleven_v4). Priya stays the same (task 286104ef..., Pyaari). Gullu stays in the long videos.
- Format: Chintu makes the money mistake, Priya fixes it with the number. Hook = Priya lip-sync to camera (HeyGen 9:16, expressive).
- Build: `ANIM_VERTICAL=1 python3 tools/anim.py <project> <out.mp4>` (1080x1920, text clear of the Shorts UI). Project = short/mistakes.
  One TTS call per line (generations_count 1), trimmed + atempo 1.12; durs.json from the trimmed files; lip clip slot GAP 0.
- Scene stills: nano-banana-2.1 2K 9:16 (6 cr); if a task fails, retry once with nano-banana-pro; check every still for blank bands.
- Copying from top videos: idea/structure/topic list yes; titles and descriptions are rewritten in Hindi with our own keywords
  (an exact copy competes head-on with the big channel in search and adds reused-content risk for YPP).

## Long-video frequency rule (owner delegated, 25 Oct 2026)
Why long videos matter: YPP needs 4,000 public watch hours (Shorts views do NOT count toward them) or 10M Shorts views in 90 days.
For a new channel the watch-hour path is the realistic one, so long videos get priority whenever they hold viewers.
- Review each long video 72 h after it goes live (vidIQ channel_analytics, dimension video + report audience_retention):
  - KEEP GOING FASTER (2 long videos/week, Sun + Thu, 16:00) when: average view percentage >= 35% (or avg view duration >= 1:15)
    AND it got at least as many views as the median of our Shorts from the same week, or brought subscribers.
  - STAY at 1/week when below that, and fix the weakest part first (retention dip in the first 30 s = hook; low views = title/thumbnail).
  - Go to 3/week only after two long videos in a row clear the bar and ElevenLabs credits allow it.
- Credit plan for 2 long/week (~100k ElevenLabs/month): long videos use one lip-sync shot only (intro, ~3.6k) instead of two,
  so ~8k each; the 3 cut-down Shorts per long video stay free; new animated Shorts drop to ~1/week (~4.7k).
- Every long video still follows STANDING RULE #1 (idea of a most-viewed niche video).
- First review: home-loan long video (live 25 Oct 16:00) on Wed 28 Oct.

## Fully animated Shorts (owner, 27 Oct 2026, TEST until the 3-4 Nov comparison)
Owner: "my videos animate 1-2 s and then look like slides". Reference Reel (instagram.com/reel/De9yemvP2Me): 13 shots in 37 s (~2.8 s each),
70-90% of the frame always moving, no lip-sync, story voiceover, SFX on every action, one big top headline, shocking visual in second 1.
- Every line gets its own image-to-video clip: Runway gen-4-turbo, 9:16, 5 s (25 credits) or 10 s (50) from a nano-banana-2.1 2K still (6).
  Prompt = one clear body action + one environment motion + camera move ("jumps and dances", "coins crumble into red dust", "slow push-in").
- Lines <= ~4.8 s so a 5 s clip covers line + gap; last line END_HOLD small enough to fit. Reuse a still for 2 clips with different actions.
- anim.py CLIPS entry ("clip.mp4", "anim", start_offset) skips a bad start (e.g. a glitch in the first second).
- No HeyGen lip-sync in this format (saves ~3k ElevenLabs credits per Short); Priya narrates, Chintu reacts.
- Story arc beats a list: character wants something → action → twist with the real number (with source) → lesson + comment question.
- Budget: ~280-300 Runway credits per Short. Runway plan 570/month: 2 animated Shorts/week need ~2,400/month (upgrade or mix with still Shorts).
- Check every clip at 3 points for morphing/glitches before building.

### Animation quality gate (owner, 27 Oct 2026: "the animation issue must not happen in the next video")
Issue in the F&O Short: shot 4 (dance) had a glitter/static cloud covering the frame for ~1.3 s (prompt asked for "gold sparkles burst").
- tools/clipcheck.py scans every frame of every clip for noise bursts, flashes and morph pops; anim.py now runs it automatically and
  REFUSES to build if a flagged range falls inside the part of a clip we use (ALLOW_GLITCH=1 only with the owner's OK).
- Regenerate any flagged clip (25 credits) instead of shipping it; also look at a contact sheet (clipcheck --sheet) for face/hand morphing.
- Prompt rules for gen-4-turbo: no "sparkles/particles/glitter burst", "explosion", "magic", "dust cloud" (they render as static noise);
  keep the action in place and small-to-medium (wave, nod, dance on the spot, slump, point); no "jumps up from the chair" or spins;
  one character action + one gentle environment motion (screen glow pulses, papers drift) + "slow camera push-in".

## Data rules from 28 Oct 2026 review
- IG: numbered mistakes/galtiyan lists get saved and shared (5 mistakes Reel: 6x reach, 7 saves, 10 shares). Prefer list Shorts; captions = numbered list +
  "Save karo" + "share karo us dost ko jo <specific situation>" + a number-answer question ("1, 2 ya 3?").
- First frame carries the ₹ figure (first headline), the topic line second. A question card without a number held only 44% past 3 s.
- Long videos: cold open on the shocking ₹ result in the first 3 s, no logo/intro, answer promised by second 8, new shot every 2-3 s for the first 30 s
  (first long video averaged 10 s viewed = 5%).
- Lines longer than ~4.8 s: give the line two 5 s clips (CLIPS entry = list) instead of a 10 s clip; reversing a clip is fine when the model
  animated the motion backwards (check the direction of growth/shrink against the line).

## YOUTUBE VIEWS = THE MAIN GOAL (owner, 28 Oct 2026: "views are not coming on YouTube, that is our main aim")
State 28 Oct: channel views per day 10 / 42 / 68 / 56 (22-25 Oct), best Short 85 views, 3 subs. Instagram numbers are a side metric, never the headline.
Daily review now starts with a YouTube scorecard (Metricool YTEV02 daily views + subs: free; vidIQ per-video when credits allow):
views per Short at 48 h, engaged views / views (proxy for "viewed vs swiped away"), avg % viewed, subs gained. A Short is a hit at >= 70% engaged/views.
Why views are low (diagnosis 28 Oct): only 30-56% of people who see our Shorts keep watching past the first moment (engaged/views 37/85, 24/60, 9/22),
so YouTube stops pushing them to new viewers after the first small test. Plus: new channel, and format kept changing (3D, realistic, animated, cut-downs).
Rules from now:
1. First 1 second decides everything: frame 1 = movement + the ₹ number on screen + the spoken question starts at 0.0 s (no logo, no setup line).
2. Shorts 20-35 s (our 30 s Shorts hold 53-72%; 60-73 s ones held far less). Loop: last line flows back into the first.
3. One format for 2 weeks (fully animated Priya + Chintu) so the channel has one identity and results are comparable.
4. Topics only from proven high-view ideas (STANDING RULE #1), title = search phrase first.
5. Any Short under 50% engaged/views: the next Short changes the hook style (not the topic).

### 29 Oct 2026 data: YouTube does not distribute the cartoon Shorts
Live view counts: animated Priya + Chintu Shorts 1-7 views after 1-3 days; realistic presenter Shorts 62-88. Same animated videos reach 700-840 on Instagram.
- Rule 3 above is changed: YouTube Shorts = realistic presenter format; animated = Instagram-first (and long videos until the 72 h data says otherwise).
- Realistic Short recipe (cc, 3 Nov): one TTS (Pyaari eleven_v4, atempo 1.12), Scribe word times, HeyGen 9:16 expressive hook + outro from the full-res portrait,
  3 nano-banana-2.1 2K stills of her (ref = portrait task), 6 gen-4-turbo 5 s clips (one action each) = ~150 Runway, new shot every ~3.5 s, tools/real.py --ovl <name>.
- Lip-sync audio must be uploaded via a raw.githubusercontent.com URL (creative_attach_reference_file); the googleapis upload URL is blocked from the sandbox.
- Ideas used: warikoo "CREDIT CARDS se PAISE AISE KAMATE HAIN!" (4.4M) → credit card kamai Short (3 Nov). Next unused: warikoo "Make regular income from your investments" (4.6M), "AAPKE 20s ke liye COMPLETE FINANCIAL PLANNING" (3.8M), "15,000 SALARY to 1 CRORE" (3.0M).

## Script pipeline (owner, 30 Oct 2026): run these 3 steps for every new Short/Reel
1. Pain to hooks: list 10 frustrations our audience (22-35, salaried, Hindi/Hinglish) has about the topic and turn each into a
   curiosity hook under 10 words. Keep the 2-3 that are specific and carry a ₹ figure.
2. Write the Reel: strong hook, relatable problem (Chintu's situation), one useful takeaway, natural CTA (number-comment question
   + save/share to a named friend). Simple sentences, no filler; every line must earn its 3-4 s.
3. Improve the hook: write 10 hook options that make the idea clear in 2 seconds. Specific, curious, no clickbait, nothing
   scam-sounding ("paisa double", "guaranteed"). Pick the best, keep runner-up for the title/Test & Compare.
Log the chosen hook + 2 runners-up in performance_log so we learn which hook types win.

## Metricool post budget (31 Oct 2026)
Fri 30 Oct posts failed with "You have reached your Metricool account limit" (free-plan monthly post cap). Until Junaid upgrades:
- 3 Metricool posts per video (YT Short + IG Reel + FB Reel). IG Story = Junaid shares the live Reel to Story by hand + YouTube link sticker.
- Create the YouTube post first; repost-only IG posts (old cut-downs) are the first to drop when the cap is near.
- Every daily run checks the previous day's posts with getScheduledPosts (status ERROR / detailedStatus) and alerts Junaid at once.

## Plan & credit watch (owner, 31 Oct 2026: "give me the link BEFORE it runs out")
Every daily run checks every plan and alerts Junaid (push notification, with the upgrade/top-up link) when any one will run out
within ~7 days or before the next queued upload, never after it has failed.
| Service | Plan (31 Oct) | How to check | Warn when | Link |
|---|---|---|---|---|
| Metricool | Free: 20 PUBLISHED posts/month, each network counts once, resets 1st of month | count PUBLISHED + queued providers this month (getScheduledPosts) | queued posts this month > 16 | https://metricool.com/pricing/ (Starter $25/mo monthly, unlimited posts) |
| Runway | Pro, 2,250 credits/month + top-ups | whoami credits.total | < 300 (2 Shorts) | https://app.runwayml.com/settings/billing (top-up from 1,000 cr = $10) |
| ElevenLabs | ~100k credits/month | not readable via MCP: sum usage from performance_log | est. < 15k left | https://elevenlabs.io/app/subscription |
| vidIQ | Free, 150 credits/month, resets 24th | vidiq_balance | < 20 | https://vidiq.com/pricing |
| OpusClip | 10 min balance | opusclip_get_usage | not used in pipeline | https://www.opus.pro/pricing |
Metricool free cap in practice: 4 posts/video → only 5 videos/month. Oct: 21 published by 29 Oct → all 30 Oct posts failed.

## Owner direction (31 Oct 2026): followers first, realistic girl, Seedance allowed
- Goal of every video = more FOLLOWERS/SUBSCRIBERS (then views). Every caption gets a follow line ("➕ Follow karo @paisa_science: roz ek paise ki
  tricky baat"); every Short ends on a reason to follow (next part / series promise) plus the comment question.
- All new Shorts/Reels use the realistic presenter girl (Runway portrait task ed8090cd...), not the cartoon. Cartoon Priya + Chintu: no new videos
  (already-made ones still go out).
- Make videos more interactive: she talks to camera more (question to viewer, "comment mein likho 1 ya 2"), on-screen polls/quiz moments,
  a new shot every ~2-3 s. Seedance (seedance-2 / 2.5 on Runway) is allowed for the key moving shots (hook, reveal) when gen-4-turbo looks static;
  check face drift on every Seedance clip.
- Ideas: STANDING RULE #1 still applies (copy the idea of a famous high-view video, never its script/footage).
- Owner said (31 Oct): upload on all platforms at our best times (YT + FB 16:00, IG Reel 18:00, Story 18:10) without asking each time for queued
  videos he already saw; brand-new videos are still sent to him first.
- Metricool and Runway upgraded 31 Oct (Runway 3,012 credits). Metricool post cap no longer the bottleneck.

## FULL CONTROL (owner, 31 Oct 2026) — supersedes every "wait for Junaid's yes" rule above
- Junaid: "You have 100% control. You don't need my review, input or decision." Claude decides and publishes everything itself
  (topics, format, style, characters, scheduling, publishing, comment replies). Main goal: followers + YPP monetization.
- Contact Junaid only for (a) something only he can do, (b) a plan/credit about to run out (with link, BEFORE it runs out), (c) a big result.
- Every task for him gets a one-time reminder (send_later) at the exact time it is needed, which pushes a phone notification.
- Content rules (SEBI/education, platform rules, AI disclosure, no copied scripts/footage) still apply in full.

## SHARE TEST (owner, 31 Oct 2026) — every topic and hook must pass before production
Owner: "Viewer should feel 'yaar ye naya hai, mere dost ko pata nahi hoga, ise bhejta hoon'."
A topic passes only if ALL four are yes:
1. Relatable: it happens in a normal salaried Indian's life (salary, EMI, credit card, rent, insurance, bank, UPI, tax, gold, parents' FD).
2. Not common knowledge: most viewers do NOT already know it (no "SIP kya hai", "save money", "emergency fund rakho").
3. Surprising + checkable: a hidden cost, a rule people don't know, or a common belief proved wrong, with a ₹ number we calculate on screen.
4. Send-to-a-friend trigger: there is a specific person to tag ("jiska home loan chal raha hai", "jo har cheez card pe leta hai",
   "papa jo FD mein hi paisa rakhte hain"). Caption + last line name that person: "Ye video us dost ko bhejo jo ...".
Hook formula: "<everyday thing> ka <hidden ₹ cost / rule> jo 90% log nahi jaante?" spoken + on screen in second 1, answer by ~15 s.
Score every idea 1-5 on each point; produce only ideas with 16+/20. Log the score and the chosen "send to" person.

## Extra connectors to use (reviewed 31 Oct 2026)
- Canva: (1) Instagram CAROUSELS 2x/week (Tue + Sat 11:00, separate from the daily Reel): 6-8 slides turning a video's hidden-₹ fact into
  "save this" steps, last slide = "Follow @paisa_science" + "bhejo us dost ko jo ...". Carousels get the most saves/shares → followers.
  (2) Thumbnails for long videos (3 options). Use the Paisa Science colours; no real logos/brands.
- Descript (Agent Underlord): optional for burned-in word-by-word captions / filler removal on long videos; check output before posting.
- OpusClip: auto-pick Shorts from long videos (only 10 min balance → long videos only).
- vidIQ instagram_tiktok_outlier_search / ig_profile_reels: find which Reels are viral in Indian finance (topic ideas), when credits allow.
- Gmail: read YouTube/Instagram/Metricool emails (errors, policy notices, comment alerts) in the daily check.
- Do NOT use: TEXT_TO_QUANT (trading backtests: off-topic and against our no-trading-advice rule), Supabase/Granola/Figma (no need), Krea (0 credits).
- Bird (WhatsApp/SMS): later, a WhatsApp channel/broadcast for followers needs an opt-in list and costs per message; skip until 1k followers.

## Instagram Stories: auto-publish (31 Oct 2026)
Stories with autoPublish false never went up (Metricool only marks them "Published" after sending a phone reminder; Junaid did not get/see it).
From now every Story is autoPublish TRUE at 18:10. No link sticker via API: the Story image itself says "Full video: YouTube Paisa Science
(link bio mein)". Old manual Story posts (410329839, 411957456, 411957730, 411958008, 411958342, drafts 4103298xx) may still send phone
reminders: Junaid ignores them.
