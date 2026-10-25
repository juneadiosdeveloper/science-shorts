# Paisa Science: video style guide (realistic presenter format)

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
- Home-loan cut-downs: #1 quiz A-or-B (83.1-123.15 s) done 25 Oct; next: Byaaj Monster 82% (YouTube only, IG already has the teaser),
  then step-up ₹19.5 lakh reveal.
