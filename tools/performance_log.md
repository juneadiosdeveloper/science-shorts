# Paisa Science performance log

## 2026-10-22 (Thu)
**Numbers (Metricool, brand 7570802):**
- Subscribers: 0 (gained 0, lost 0)
- Published videos: 0 — first Short (₹10,000 SIP = ₹1 crore) goes live today 16:00 IST
- Views (90 d): 0 · Watch hours (365 d): 0 / 4,000 · Shorts views (90 d): 0 / 10M
- Best time to post (getBestTimeToPostByNetwork, next 7 days): 16:00 IST is the top hour on every day.

**Queue:** 22 Oct SIP · 23 Oct Credit card minimum due · 24 Oct Inflation (all scheduled, not drafts).
Old science-channel drafts (sky blue 22 Oct, lightning 23 Oct, compound interest 24 Oct) still sit in Metricool as drafts — asked Junaid whether to delete.

**What worked:** too early to tell — no data yet.

**Changes applied:**
1. Keep 16:00 IST posting time (data-backed peak hour).
2. No other changes until the first 3 Shorts have 48 h of data (review from 25–26 Oct).

## 2026-10-23 (Fri)
**Numbers (Metricool, brand 7570802, Asia/Kolkata):**
- Subscribers: 0 (gained 0, lost 0)
- Published: 1 Short — "₹10,000 SIP = ₹1 CRORE?" (DxwFJxuw7OA, live 22 Oct 16:00). Views / watch time / avg view duration / likes / comments / shares: not reported yet (YouTube Analytics lags 24–48 h).
- Today 16:00: Credit card minimum-due Short (realistic presenter) is scheduled live (approved yesterday).
- Best time (getBestTimeToPostByNetwork, Sat 24 Oct): 16:00 IST top hour again (5,880), 10:00 next (5,392).

**Improvements applied to the next video (inflation remake, realistic format):**
1. Editor fixed to the style guide: `real.py` now does hard cuts only (old 0.3 s crossfade removed), refuses to slow/freeze a clip (b-roll generated at the needed length and only trimmed), colour-matches every clip to the lip-sync clip and adds light grain; top shading lighter.
2. On-screen numbers appear instantly on the spoken word (no fade-in) and every assumption (6% mehngai, 7% return) is on screen.
3. Voice track played 1.08x (36.6 s → 33.9 s) to keep the Short tight; first comment asks a question to seed comments.
Next review: 25–26 Oct, once SIP + credit-card Shorts have 48 h of data (compare avg view duration and % viewed of 3D vs realistic format).
**Produced today:** inflation remake (realistic) → videos/inflation_chupa_tax_real.mp4, 33.8 s. Metricool draft updated (old id 403408723 → new id 403791817), still DRAFT for Sat 24 Oct 16:00 IST, waiting for Junaid's yes.
Credits: ElevenLabs ~5,818 (TTS 970 + HeyGen lip-sync 2 × 2,424). Runway 318 (4 stills 24, b-roll 267, one market shot regenerated after face drift 27). Runway left: 2,262.
Note: Kling 3.0 Standard (9 cr/s) held the face better than Gen-4.5 (12 cr/s) on the 2 s market shot; use Kling 3 Std for b-roll by default.
- Junaid approved ("yes") → inflation Short switched from draft to scheduled: Sat 24 Oct 16:00 IST (Metricool id 403793829).
- Checked Runway speech (eleven_v4 via Runway, ~5 Runway credits per 1,000 chars): Pyaari voice not available there (voice library search returns nothing on this workspace) and Runway MCP has no lip-sync/avatar tool, so lip-sync stays on ElevenLabs (HeyGen = ~83% of EL spend).
- Junaid updated the YouTube channel branding (name Paisa Science, handle, description, logo, banner, defaults Hindi/Education, phone verification) on 23 Oct. Check the channel name on the credit-card Short in the next run.

## 2026-10-24 (Sat)
**Numbers (Metricool, brand 7570802, Asia/Kolkata):**
- Subscribers: 0 (gained 0, lost 0). Channel videos: 2 published.
- SIP Short (DxwFJxuw7OA, 22 Oct) and Credit-card Short (ofla0hmAlI0, 23 Oct): views / watch minutes / avg view duration / likes / comments / shares all still null in Metricool (YouTube Analytics lag, 48 h+). No performance verdict possible yet.
- Today 16:00 IST: inflation Short (realistic) goes live (approved, Metricool id 403793829).
- Best time Sun 25 Oct: 16:00 IST top hour (5,648), 17:00 next (5,417).

**Improvements applied to the next video (Rule of 72 Short):**
1. HeyGen Avatar 4 nodes default to 16:9 (first outro came back 1920x1080 with her face cropped). Always: estimate → `creative_update_node` aspect_ratio 9:16 → run.
2. HeyGen moderation blocked the spoken hook "aapka paisa kitne saal mein double hoga?" twice ("may violate Terms of Service") — it reads like a money-doubling scam line. Keep spoken talking-head lines free of "paisa double / guaranteed" phrasing; put the topic claim in on-screen text instead (hook re-voiced: "Hisaab ka sabse aasaan formula chahiye? Bas ek number yaad rakho...").
3. Series continuity: the Rule of 72 Short reuses the inflation Short's 6% assumption (prices double in ~12 years) and ends with a quiz-style first comment to seed comments; every exact value (9.0 / 11.9 / 6.1 yrs) is shown next to the 72-rule estimate.

**Produced today:** Rule of 72 Short → videos/rule_of_72_real.mp4 (~29.7 s), Approved by Junaid ("yes") → scheduled Sun 25 Oct 16:00 IST (Metricool id 404767713). Junaid feedback: content too basic, make it trickier (see STYLE_GUIDE 'Content depth'). Backlog still open: long SIP video (draft 403408962, Sun 25 Oct 18:00) not yet remade in realistic format; old science drafts left untouched.
Numbers verified: 72/8 = 9 (exact ln2/ln1.08 = 9.01 yrs), 72/6 = 12 (11.90), 72/12 = 6 (6.12); ₹100 × 1.06^12 = ₹201.
Credits: Runway 250 (4 stills × 4 + b-roll 26 s Kling 3 Std 234); Runway left 2,012.
ElevenLabs: TTS 397 + re-voiced hook 57; HeyGen used clips 2,424 (hook) + 1,818 (outro) = 4,696 for the final Short. Waste: 1,818 (16:9 outro) + 2 blocked hook runs (2 × 2,424 listed; may be refunded since nothing was produced). Fixes above prevent both.
**Produced 24 Oct (evening):** first animated long video (Priya + Gullu), "₹50 Lakh Loan Pe ₹54 Lakh Byaaj? 3 Tareeke Se Bachao" → videos/home_loan_prepayment_long.mp4 (3:30, 16:9, 53 shots, 4 animated clips, 2 lip-sync shots). Metricool DRAFT id 405122119 for Mon 26 Oct 16:00 IST (best hour 9,351), thumbnail A attached; thumbs B/C in long/homeloan/thumbs for Test & Compare. Waiting for Junaid's yes.
Credits: ElevenLabs ~10.8k (voices 2.4k + lip-sync 8.5k). Runway ~380 (46 images + 4 Kling clips); Runway left 1,635.
Editor: tools/anim.py (project long/homeloan: lines.py, plan.py, audio/, clips/). Voice lines split with ElevenLabs Scribe word timestamps (free).
- Junaid approved ("schedule it for tomorrow") → long video scheduled Sun 25 Oct 17:00 IST (Metricool id 405129270), one hour after the Rule of 72 Short (16:00).
- Junaid changed the plan: long video Sun 25 Oct 16:00 IST (id 405132150), Rule of 72 Short moved to Mon 26 Oct 16:00 IST (id 405131995).
- Instagram @paisa_science connected to Metricool (24 Oct night). Scheduled: Sun 25 Oct 16:00 IG Reel = 58 s vertical teaser of the home-loan video (instagram/reel_homeloan.mp4, id 405210760) + Story 16:10 (manual, link sticker; id 405210854); Mon 26 Oct 16:00 IG Reel = Rule of 72 Short (id 405210845) + Story 16:10 (manual; id 405210866). 5 hashtags each. Facebook Page not connected yet.
- Facebook Page (id 1384710478060339) connected. FB Reels scheduled: Sun 25 Oct 16:00 home-loan teaser (id 405215470, first comment = YouTube channel link), Mon 26 Oct 16:00 Rule of 72 (id 405215359). Facebook allows links in comments: always put the YouTube link in the first comment.

## 2026-10-25 (Sun)
**Numbers (vidIQ YouTube Analytics, 20-25 Oct; Metricool video metrics still empty for this channel):**
- Channel: 0 subscribers, 55 lifetime views, 3 public videos (SIP 3D Short, credit-card realistic Short, inflation realistic Short).
- SIP Short (DxwFJxuw7OA, 3D format): 10 views, 4 engaged views, avg view duration 22 s = 72% viewed, 0 likes/comments/shares/subs.
- Credit-card + inflation Shorts: not in YouTube Analytics yet (48 h lag). No viewer comments yet (only our own pinned questions), so no replies to draft.
- Traffic sources: no rows yet. Instagram/Facebook: first posts go live today 16:00, no data.
- Today 16:00 IST: animated long video (home loan) goes live on YouTube + IG/FB teaser Reels (approved).
- Best time Tue 27 Oct: YouTube 16:00 (10,353, top); Instagram 18:00 (4,788) / 10:00 (4,942) beat 16:00 (3,532).

**What we can say:** 72% viewed on the first Short is a healthy retention signal, but 10 views = YouTube has barely tested the channel. Volume of uploads (daily cadence) matters more than tweaks right now.

**Improvements applied:**
1. Analytics source switched to vidIQ channel_analytics (dimension video): Metricool returns empty per-video rows, vidIQ gives views, engaged views, avg duration, % viewed, subs per video. Used for all reviews from now on.
2. First home-loan cut-down built with the new tools/vcut.py and the quiz-first hook: the Short opens directly on "A ya B?" (no intro) and ends on Gullu's "Dugni?!" punchline so the loop replays into the question; on-screen assumption line + "Poori video, neeche link" CTA to push viewers to the long video (watch hours for YPP).
3. Shorts packaging: the vidIQ title scorer preferred a search keyword at the start + concrete ₹ number (76) over a curiosity-only title (69): keep "keyword: hook + ₹ figure" pattern.

**Produced today:** videos/homeloan_quiz_a_ya_b_short.mp4 (40.0 s, 9:16). Numbers re-verified (EMI ₹43,391; +1 EMI/yr → 201 months, saves ₹10.29 lakh; EMI +5%/yr → 147 months, saves ₹19.52 lakh).
Metricool DRAFTS for Tue 27 Oct: YouTube Short 405436391 (16:00), IG Reel 405436398 (16:00), IG Story 405436407 (16:10, manual link sticker), FB Reel 405436416 (16:00). Waiting for Junaid's yes.
vidIQ: keyword "home loan emi" (IN ~4.4k/mo; "home loan prepayment" 7.4k, +90%); titles scored "Home Loan EMI: A ya B? ₹19.5 Lakh Kaise Bache 🤯 #shorts" 76 (chosen) vs "Home Loan Jaldi Khatam: 1 Extra EMI ya EMI +5%? 😱" 69 (Test & Compare alt).
Credits: ElevenLabs 0, Runway 0 (left 1,635), vidIQ 25 (left 105 until 24 Nov).
- Owner request (25 Oct): tomorrow's video from the most-viewed niche idea, cartoon girl + monkey. Research (vidIQ outliers, 6 top channels, all time):
  top replicable idea = Labour Law Advisor "5 STUPID mistakes WEALTHY people never make!" (1.6M). Built our own 72.8 s 9:16 animated Short
  "5 Money Mistakes Jo Ameer Log Kabhi Nahi Karte 💸 #shorts" (vidIQ 81; alt "5 Galtiyan Jo Ameer Log Kabhi Nahi Karte 😱" 54) → videos/5_money_mistakes_short.mp4.
  Numbers verified (12% flat ₹1L 2 yr → 21.57% reducing; ₹2,000 SIP 5 yr 12% → ₹1,64,973; others simple products). Script doc: https://claude.ai/artifact/728DHEpZCkVwxxtnSMCnZp
  Metricool DRAFTS Mon 26 Oct: YT 405505634 (16:00), IG Reel 405505640 (16:00), IG Story 405505646 (16:10 manual), FB Reel 405505654 (16:00).
  Rule of 72 posts moved to Wed 28 Oct (owner approved): YT 405497444, IG 405497451, Story 405497456 (16:10), FB 405497459.
  Credits: ElevenLabs ~4.7k (TTS ~1.07k + HeyGen 9:16 hook 3,636); Runway 140 (monkey sheet 2 + 18 stills; 3 failed tasks retried on Pro), left 1,495; vidIQ 30 (left 75).
- Junaid approved Monday ("monday yes") → 5 money mistakes Short scheduled Mon 26 Oct 16:00: YT 405511843, IG Reel 405511882, FB Reel 405511948, IG Story 16:10 405511900 (manual). Tuesday quiz Short still a draft (no yes yet).
- Owner standing rule (25 Oct): every next video must be the idea of a most-viewed niche video, never our own topic choice (STYLE_GUIDE 'STANDING RULE #1').
- Junaid approved Tuesday ("tuesday yes") → quiz Short scheduled Tue 27 Oct 16:00: YT 405513595, IG 405513639, FB 405513723, IG Story 16:10 405513663 (manual).
- Wed Rule of 72 removed per Junaid: all 4 posts switched back to DRAFT (YT 405513832, IG 405513862, Story 405513873, FB 405513890) so they cannot publish; the Metricool MCP has no delete, Junaid can delete them in the planner.
- Wed replacement (STANDING RULE #1): source = warikoo "40 CRORES from a 10,000 INR SALARY?" (5.07M views, highest unused idea). Our 63.8 s Priya + Chintu Short "10K Salary Se 40 Crore Possible? SIP Ka Sach 🤯 #shorts" (vidIQ 81; alt "₹10,000 Salary Se ₹40 Crore? 😱 Asli Hisaab" 77) → videos/10k_salary_40_crore_short.mp4.
  Numbers (Python, monthly SIP at start of month, r/12, step-up yearly): ₹2,000 × 38 yr @12% = ₹1.87 cr; +10%/yr = ₹5.35 cr; ₹5,000 +15%/yr @14% = ₹42.9 cr; ÷1.06^38 (9.15) = ₹4.69 cr real.
  Metricool DRAFTS Wed 28 Oct 16:00: YT 405523572, IG 405523620, FB 405523669, IG Story 16:10 405523628.
- Fix: Poppins has no "→" glyph, small captions showed a box. 5 mistakes Short re-rendered and the 3 Monday posts re-uploaded (YT 405523408, IG 405523430, FB 405523461; same text/time). Rule: no arrows in SMALL captions (headlines are fine, they fall back to DejaVu).
- Long-video frequency rule written (STYLE_GUIDE): review at 72 h; ≥35% avg view % and views ≥ week's Shorts median → 2 long/week (Sun + Thu). First review Wed 28 Oct.
- Credits (second Short): ElevenLabs ~5.0k (TTS ~0.84k + HeyGen 4,242); Runway ~80 (11 stills + 1 Pro retry), left ~1,415; vidIQ 15 (left 55).
- Junaid approved Wednesday ("yes") → 40 crore Short scheduled Wed 28 Oct 16:00: YT 405534537, IG 405534579, FB 405534650, IG Story 16:10 405534596 (manual).

## 25 Oct — Islamic channel Episode 1 (Hindi, family) rendered
- videos/islamic_ep01_pehla_insaan.mp4 (16:9, 3:44, no music). Packaging + thumbnail in islamic/ep01/. NOT uploaded: owner will say where.
- Spend: 2 HeyGen Avatar 4 lip-syncs (~2,424 EL credits each), 2 Kling 3.0 Standard motion clips on Runway (credits left 1,144).

## 2026-10-26 (Mon)
**Numbers (vidIQ YouTube Analytics 20-26 Oct; long video + Shorts from 24-25 Oct not in Analytics yet, 48 h lag):**
- Credit-card Short (ofla0hmAlI0, realistic): 37 views, 16 engaged, avg 15 s = 51% viewed, 0 likes/comments/subs.
- SIP Short (DxwFJxuw7OA, 3D): 15 views, 4 engaged, avg 22 s = 72% viewed.
- Subscribers: 0. Traffic sources: no rows yet.
- Instagram (Metricool): home-loan teaser Reel (58 s, 25 Oct): reach 118, 133 views, 3 likes, 1 comment, 0 saves/shares, avg watch 10.2 s (~18% of 58 s), 57% view rate (>3 s).
- Today 16:00: 5 money mistakes Short live on YT/IG/FB (approved). Tue quiz + Wed 40-crore approved and scheduled.

**What it says:** retention falls with length: 22-30 s Shorts hold 51-72%, the 58 s IG teaser held ~18%. The 3 s hook works on IG (57% stay past 3 s), the middle loses people.

**Improvements applied:**
1. Cut-downs kept under 30 s and opened on the shock line: Byaaj Monster 28.1 s (starts on Gullu's "sirf 43 hazaar ki EMI", ends on "monster kha gaya"), lump-sum 22.4 s. Rule: cut-downs ≤ 30 s unless a quiz needs the answer.
2. Titles: exact ₹ figures beat a curiosity phrase in vidIQ: "Home Loan EMI: ₹43,391 Mein ₹35,417 Sirf Byaaj? 😱" 75 vs "Home Loan EMI Ka 82% Sirf Byaaj? 😱 Pehli EMI Ka Sach" 63; "Home Loan Prepayment: ₹1 Lakh Se ₹4.2 Lakh Bachat? 🤯" 81.
3. vidIQ budget: only 40 credits left until 24 Nov (8 calls). From now: 1 analytics call every 2-3 days, 1 title score per upload (keyword research only for new topics), comments check Wed 28 + Sat 31 Oct.
- Planned "step-up ₹19.5 lakh" cut-down dropped: the quiz Short (Tue) already reveals it. Replaced with the lump-sum + "tenure kam, EMI nahi" cut.
- Emoji in vcut.py captions renders as a box (Poppins); keep vcut text emoji-free.

**Produced today (0 ElevenLabs, 0 Runway):** videos/homeloan_byaaj_monster_short.mp4 (28.1 s), videos/homeloan_lumpsum_short.mp4 (22.4 s); numbers re-run (int month 1 ₹35,417 = 81.6%; ₹1 lakh lump sum → 228 months, saves ₹4.23 lakh).
Metricool DRAFTS: Thu 29 Oct 16:00 YT 406211262, FB 406211288, IG Story 16:10 406211298 (no IG Reel: IG already had the 82% teaser). Fri 30 Oct 16:00 YT 406211409, IG Reel 406211430, FB 406211466, IG Story 16:10 406211477.
- Long video #2 script for approval (STANDING RULE #1 source: warikoo "SIP KYA HAI? SIP vs LUMPSUM", ~4.5M): "SIP vs Lump Sum: same market, ₹2.8 lakh ka farak" — https://claude.ai/artifact/A4HcuVet2biH6z8XmMumY3
  Numbers (Python, ₹6 lakh, 5 yr, monthly compounding of yearly example returns): steady 12% → LS ₹10.57L / SIP ₹8.11L; −30% first → ₹9.78L / ₹9.45L; −30% last → ₹9.78L / ₹6.67L; avg 13% vs CAGR 10.27%.
- vidIQ used 15 (analytics 5, title scores 10); left 40.
- Junaid approved ("yes") → scheduled: Thu 29 Oct 16:00 YT 406668596, FB 406668740, IG Story 16:10 406668794 (manual); Fri 30 Oct 16:00 YT 406668993, IG Reel 406669132, FB 406669258, IG Story 16:10 406669304 (manual).

## 2026-10-27 (Tue)
**Numbers (Metricool, brand 7570802; vidIQ analytics skipped today to save credits, next call Wed 28 for the 72 h long-video review):**
- YouTube: first subscriber (+1 on 25 Oct, 0 lost). Daily channel views 22-23 Oct: 10 / 42; 24-26 Oct rows not filled yet (Analytics lag). Per-video YouTube rows still empty in Metricool.
- Instagram 5 money mistakes Reel (72.8 s, 26 Oct): reach 151, 165 views, avg watch 14.2 s (~20%), 54.5% past 3 s, 2 likes, 1 comment, 0 saves/shares.
- Instagram home-loan teaser (58 s, 25 Oct): reach 118, 133 views, avg watch 10.2 s (~18%), 57.1% past 3 s, 3 likes, 1 comment.
- Today 16:00: quiz A-ya-B Short live on YT/IG/FB (approved). Wed 40-crore, Thu Byaaj Monster, Fri lump sum approved. Sat 31 Oct + Sun 1 Nov were empty.
- Long video #2 (SIP vs lump sum) script: no reply/comment from Junaid yet, so not produced.

**What it says:** on IG both long Reels lose ~80% of watch time; the 3 s hook holds (55-57%), the length kills completion. Our Shorts at 60-73 s are too long for a channel this new.

**Improvements applied:**
1. New Shorts capped at ~45 s: 8 lines, no "subscribe" tail line (the comment CTA is the last line so the loop replays into the hook), voice atempo 1.18 instead of 1.12. Sat Short = 43.2 s (vs 63.8 / 72.8 s for the last two animated Shorts).
2. Title pattern "₹X vs ₹Y: Kaun ...?" (contrast + question) scored 85 in vidIQ, our best yet (₹-figure titles 75-81). Use contrast-vs titles for comparison topics.
3. Every assumption that changes the verdict goes on screen: the dost invests more in total (₹88.5 lakh vs ₹45 lakh), shown as a caption so the twist is honest.

**Produced today:** Sat 31 Oct Short "₹30,000 vs ₹3 Lakh Salary: Kaun Zyada Ameer?" → videos/salary_30k_vs_3lakh_short.mp4 (43.2 s, 9:16, Priya + Chintu + new tortoise "dost", Priya lip-sync hook). Project short/salary.
  STANDING RULE #1 source: warikoo "30,000 vs 3,00,000 vs 3,00,00,000 INR Per Month" (~1.2M views). Our angle: savings habit beats salary.
  Numbers (Python, SIP at start of month, 12%/12 monthly, 25 yr): dost ₹7,500 +10%/yr → ₹3,20,66,596 (invested ₹88.5 lakh); Chintu ₹15,000 flat → ₹2,84,64,526 (invested ₹45 lakh).
  vidIQ: "₹30,000 vs ₹3 Lakh Salary: Kaun Zyada Ameer? 🤯 #shorts" 85 (alt for Test & Compare, not scored: "Salary 10x, Paisa Kam? ₹2.85 Cr vs ₹3.21 Cr 😱 #shorts").
  Metricool DRAFTS Sat 31 Oct: YT 407420125 (16:00), IG Reel 407420205 (16:00), IG Story 407420233 (16:10, manual link sticker), FB Reel 407420285 (16:00). Waiting for Junaid's yes.
  Best time Sat 31: YouTube 16:00 (5,880, top); Instagram 10:00 (3,409) beats 16:00 (2,091), kept 16:00 per same-time rule.
  Credits: ElevenLabs ~3.6k (TTS ~535 + HeyGen 9:16 hook 3,030); Runway 102 (8 stills + 4 retries: two 2.1 failures, s02 letterbox bands, s04 showed a real brand name on a storefront), left 1,042; vidIQ 5 (left 35).
- Still checks: reject stills with letterbox/blur bands and with any readable brand name or logo (add "plain unbranded storefronts, no signs" to mall/shop prompts).
- Junaid approved Saturday ("this is yes") → salary Short scheduled Sat 31 Oct 16:00: YT 407872437, IG Reel 407872453, FB 407872497, IG Story 16:10 407872479 (manual link sticker).
- Owner feedback (27 Oct): our videos feel like slides after the first 1-2 s; wants every scene animated like reference Reel instagram.com/reel/De9yemvP2Me (vidIQ watch, 10 credits, left 25):
  37 s, 13 shots, avg shot ~2.8 s, hard cuts, 70-90% of the frame moving all the time (character blinks/breathes/acts, objects move, camera push-ins),
  no lip-sync (Hindi voiceover story), SFX under every action, one static top banner headline, hook = shocking visual action in second 1.
  Cost check: ElevenLabs Seedance mini 5 s 720p = ~4.6k EL credits (too expensive); Krea has 0 credits (free plan); Runway Kling 3 Std ~9 cr/s → ~350-400 Runway credits per fully animated 40 s Short.
- NEW FORMAT TEST (owner, 27 Oct): fully animated Short, every line = its own moving clip, no lip-sync. Sun 1 Nov "F&O Trading: 100 Mein Se 93 Ka Nuksaan? 😱 SEBI Report #shorts" (vidIQ 78) → videos/fno_93_percent_short.mp4 (41.1 s, 11 shots, 10 animated). Project short/fno.
  Source idea (STANDING RULE #1): Finance With Sharan "The Ugly Truth Behind ₹15Cr Trading". Facts: SEBI study 23 Sep 2024: ~93% of 1 cr+ individual equity F&O traders lost money FY22-FY24, avg loss ~₹2 lakh incl. costs (source on screen + description).
  Model test (same still, Runway): Seedance 2 Mini 4 s = 60 cr (15/s, big motion but face drift), Kling 3 Turbo 3 s = 42 cr (14/s), Gen-4 Turbo 5 s = 25 cr (5/s, character stays the same, motion subtler). → Gen-4 Turbo for all clips; clips come only in 5 s / 10 s, so keep each line <= ~4.8 s.
  Cost of this Short: Runway ~300 (8 stills ~48 + 8×5 s + 1×10 s clips 250; the test clip reused as shot 9), ElevenLabs ~570 (TTS only, no HeyGen; old format ~3.6k). Runway left 629 (the 3 model tests cost ~127).
  Metricool DRAFTS Sun 1 Nov: YT 407902759 (16:00), IG Reel 407902780 (16:00), IG Story 407902798 (16:10, manual), FB 407902824 (16:00). Best time Sun: YT 16:00 (5,648). Waiting for Junaid's yes.
  Compare on 3-4 Nov: avg % viewed / IG avg watch time vs Sat salary Short (still + lip-sync format, 43 s).
- vidIQ used today: 5 (salary title) + 10 (watch reference reel) + 5 (F&O title) = 20; left 20 until 24 Nov.
- Junaid approved Sunday ("yes") → F&O Short scheduled Sun 1 Nov 16:00: YT 407950082, IG Reel 407950100, FB 407950135, IG Story 16:10 407950117 (manual).
  Owner: the animation issue (glitter cloud in the dance shot) must not happen again → tools/clipcheck.py + automatic glitch gate in anim.py (it flags exactly c04 1.46-2.79 s, all other clips pass) + prompt rules in STYLE_GUIDE.

## 2026-10-28 (Wed)
**Numbers (vidIQ YouTube Analytics 20-28 Oct, lagged ~48 h; Metricool IG):**
- Inflation Short (tBzBvitEwXs, realistic): 85 views, 37 engaged, avg 18 s = 53% viewed, 3 likes. Credit-card Short (ofla0hmAlI0): 60 views, 24 engaged, 60% viewed, 2 likes. SIP 3D Short: 22 views, 43%.
- **Long-video 72 h review (home loan, 2h9IU8kJfXQ):** 9 views, 8 engaged, avg view duration 10 s = 5.2% of 3:30, 0 subs. Bar (>= 35% / 1:15 and >= Shorts median) NOT met → stay at 1 long video/week, fix the opening first.
- 5 money mistakes / quiz / 40-crore Shorts not in YouTube Analytics yet. Subscribers: 1. Comments: no viewer comments yet (only our pinned questions) → nothing to reply to.
- Instagram: 5 money mistakes Reel (26 Oct) took off: reach 709, 773 views, avg watch 16.2 s, 60% past 3 s, 18 likes, 7 saves, 10 shares (6x the reach of any other Reel). Quiz A-ya-B Reel (27 Oct, 40 s): reach 115, avg watch 6.3 s, 44% past 3 s. Home-loan teaser: reach 120. IG followers: 2. Account reach 26-27 Oct: 373 / 443.

**What it says:** (1) a numbered "galtiyan" list is what people save and send to a friend on IG; (2) a question-card opening without a ₹ figure loses half the viewers in 3 s; (3) the long video loses viewers in its first ~10 s: the opening (logo/intro + slow setup) is the problem, not the topic.

**Improvements applied:**
1. Next Short is a numbered mistakes list again ("Home loan ki 3 galtiyan"), with the save/share CTA aimed at a specific friend ("jo ghar lene wala hai") and a "1, 2 ya 3?" number-comment question.
2. Hook rule: the ₹ figure must be on screen from frame 1 (first headline = "₹34 LAKH KA NUKSAAN?"), the topic line second.
3. Long videos: cold open = the most shocking ₹ result + the visual in the first 3 s, no logo/intro, promise of the answer by second 8, new shot every 2-3 s in the first 30 s. Applies to long video #2 (SIP vs lump sum) before it is produced.

**Produced today:** Mon 2 Nov Short "Home Loan Mistakes: EMI Kam, Byaaj ₹34 Lakh Zyada? 😱 #shorts" (vidIQ 83) → videos/home_loan_3_galtiyan_short.mp4 (37.4 s, 9:16, fully animated: 10 gen-4-turbo clips, every shot moving, no lip-sync). Project short/hlmistakes.
  STANDING RULE #1 source: warikoo "Home Loan Mistakes That Cost You LAKHS" (~1.2M views). Our 3 mistakes + numbers.
  Numbers (Python, reducing balance, r/12, ₹50 lakh): 20 yr @8.5% EMI ₹43,391, interest ₹54.14L; 30 yr EMI ₹38,446 (−₹4,945), interest ₹88.40L (+₹34.3L). Rate 8.5→9.5% after 12 months, EMI kept: ~297 months total, interest ₹78.75L (+₹24.6L); EMI raised to ₹46,498 instead: interest ₹61.22L (~₹17.5L less). ₹50,000 premium financed 20 yr @8.5% → ₹1,04,139 repaid.
  Clip check: clipcheck passed all 10 clips; c06a showed the red coin stack SHRINKING while the line says interest grows → played reversed (from 1.6 s) so it grows.
  Metricool DRAFTS Mon 2 Nov: YT 408552508 (16:00), IG Reel 408552514 (16:00), FB Reel 408552524 (16:00), IG Story 408551621 (16:10, manual link sticker). Best time Mon: YT 16:00 (9,351, top).
  Alt title for Test & Compare (not scored, no vidIQ credits left): "Home Loan Ki 3 Galtiyan: ₹34 Lakh Ka Nuksaan? 😱 #shorts".
  Credits: ElevenLabs ~525 (TTS only); Runway ~312 (8 stills incl. 1 Pro retry ~56 + 10 clips 250), left 317; vidIQ 15 (analytics 5, comments 5, title 5) → 0 left until 24 Nov.
- Tool: anim.py CLIPS entry may now be a list of clips → the line is split into equal shots, one moving clip each (lines > 5 s no longer need a 10 s clip).

## 2026-10-29 (Thu)
**YouTube scorecard (vidIQ user_videos = live public view counts, 5 credits; Metricool YouTube per-video rows still empty, daily views lag after 25 Oct):**
| Video | Format | Age | Views | Likes |
|---|---|---|---|---|
| Inflation (tBzBvitEwXs) | realistic presenter, 34 s | 5 d | 88 | 3 |
| Credit card minimum due (ofla0hmAlI0) | realistic presenter, 31 s | 6 d | 62 | 2 |
| SIP 1 crore (DxwFJxuw7OA) | 3D, 31 s | 7 d | 23 | 2 |
| Home-loan long video (2h9IU8kJfXQ) | animated 16:9, 3:30 | 4 d | 11 | 3 |
| 5 money mistakes (FI-72VzBB6g) | animated Priya + Chintu, 73 s | 3 d | 7 | 1 |
| 40 crore (oH6X_i7R7C8) | animated, 64 s | 1 d | 2 | 1 |
| Home loan A ya B quiz (Onb2KAFUjQU) | animated cut-down, 41 s | 2 d | 1 | 1 |
Subscribers: 3 (Metricool). Instagram (same days): 40 crore Reel reach 838 / 990 views / avg 17.9 s / 61.9% past 3 s / 19 likes / 9 saves; 5 mistakes reach 710, 7 saves, 10 shares; quiz reach 119; home-loan teaser 120.

**What it says:** the animated cartoon Shorts are getting almost no YouTube distribution (1-7 views in 1-3 days) while the realistic presenter Shorts got 62-88 at the same age, and the SAME animated videos do well on Instagram (reach 700-840). So the content/hooks are not the problem on YouTube; YouTube is either not testing these Shorts at all or has classified them differently (cartoon = possible auto "made for kids" / low-trust signal for finance). Junaid asked (push, 09:40) to check Studio > Audience on the animated Shorts.

**Improvements applied:**
1. YouTube format switch: next new Short (Tue 3 Nov) is back in the realistic presenter format (the YouTube winner). Animated stays an Instagram format (it wins there). Already-queued animated posts (Thu-Mon) stay as a fair test; decision on 3-4 Nov with 48 h numbers for both.
2. Retention rules kept from the data: ₹ figure + spoken question on frame 1 ("₹1 LAKH PE ₹60,000+ BYAAJ?"), 30.6 s, numbered 3-point list (IG saves/shares), new shot every ~3.5 s (8 shots in 30 s instead of 6 in the old realistic Shorts), loop ending on a 1/2 comment question.
3. Cheaper realistic b-roll: gen-4-turbo 5 s clips from presenter stills (25 credits each) instead of Kling 3 Std at exact length (~9/s): 6 clips = 150 Runway credits vs ~270 for the inflation Short.

**Produced today:** Tue 3 Nov Short "Credit Card Se Bank Kaise Kamata Hai? ₹60,000+ 😱 #shorts" → videos/credit_card_kamai_real.mp4 (30.6 s, 9:16, realistic presenter, HeyGen hook + outro). Project assets/real/cc (plan.txt, overlays short3d "cc").
  STANDING RULE #1 source: warikoo "CREDIT CARDS se PAISE AISE KAMATE HAIN!" (4.4M views, highest unused replicable idea on OutlierKit's warikoo list; #3 "Make regular income from your investments" 4.6M is next).
  Numbers (Python): ₹1,00,000 × (1.035^12 − 1) = ₹51,107; +18% GST = ₹60,306; GST added to balance monthly = ₹62,521; 3.5% × 12 = 42%, compounded 51.1%. Swipe fee "lagbhag 2% tak" (on screen: varies by card and shop).
  Alt title for Test & Compare: "Credit Card Free Hai? Bank Ki 3 Chupi Kamai 🤯 #shorts" (no vidIQ score: 0 credits left until 24 Nov).
  Metricool DRAFTS Tue 3 Nov: YT 409676727 (16:00), IG Reel 409676889 (16:00), FB Reel 409676903 (16:00), IG Story 409676909 (16:10, manual link sticker). Best time Tue: YT 16:00 (10,353, top). Waiting for Junaid's yes.
  Credits: ElevenLabs ~5.3k (TTS 452 + HeyGen 3,030 + 1,818; Scribe 0); Runway 168 (3 stills 18 + 6 gen-4-turbo clips 150), left 149; vidIQ 5 (left 0).
- Mon 2 Nov home-loan 3 galtiyan posts are still DRAFTS (no yes yet).
- Long video #2 (SIP vs lump sum) script still waiting for Junaid's OK; not produced.
- Runway is nearly empty (149 credits, plan 0): one more realistic Short at most. Needs a top-up or plan for next week's production.
- Owner approved (29 Oct evening, "yes"): every video on all 3 platforms; IG Reel moves to 18:00 (Story 18:10), YT + FB stay 16:00.
  Moved: Sat IG Reel → 410329514, Sun → 410329524, Mon draft → 410329538, Tue draft → 410329554 (all 18:00); Stories Sat 410329829, Sun 410329839, Mon draft 410329849, Tue draft 410329856 (18:10).
  Fri 30 Oct IG Reel 406669132 NOT moved (update blocked by a permission check) → still 16:00. Byaaj Monster IG repost not created yet.

## 2026-10-30 (Fri)
**Numbers (Metricool; YouTube per-video + traffic-source rows still empty, vidIQ 0 credits until 24 Nov → no YouTube per-video check today):**
- YouTube subscribers: 3 (+2 since 26 Oct, 0 lost). Daily views 22-26 Oct: 10 / 42 / 68 / 56 / 5; 27-29 Oct not filled yet.
- Instagram Reels (lifetime): 40 crore (28 Oct, 64 s) reach 1,099 (+31% in 1 day), 1,230 views, avg 17.6 s, 62.2% past 3 s, 29 likes, 9 saves, 7 shares.
  5 money mistakes reach 710, 7 saves, 10 shares (plateaued). Quiz A-ya-B reach 119, 46% past 3 s. Home-loan teaser reach 120.
- Today: lump-sum Short YT + FB 16:00, IG Reel still 16:00 (move to 18:00 blocked again by a permission check → Junaid can move it by hand). Sat-Sun scheduled; Mon 2 + Tue 3 Nov still DRAFTS (no yes yet).

**What it says:** the two Reels that broke out (40 crore, 5 mistakes) are both "big ₹ promise / numbered list" stories with Priya + Chintu that keep growing for 2-3 days; the home-loan quiz/teaser posts stall at ~120 reach. IG audience wants salary/SIP/mistakes topics more than home-loan maths.

**Improvements applied:**
1. Wed 4 Nov gap filled at 0 credits: Byaaj Monster cut-down as IG Reel DRAFT 410801443 (18:00), caption leads with the exact ₹ figure ("₹43,391 mein se ₹35,417 sirf byaaj?") and a 1/2/3 number-comment question; it already went to YT/FB on 29 Oct.
2. Topic priority for the next new Short (week of 9 Nov): salary / first-salary / money-mistakes angle over home loan (IG reach 700-1,100 vs ~120). Home-loan topics stay in the long video + its cut-downs only.
3. No new production today: queue full to Wed 4 Nov, Runway 149 credits (one realistic Short max), vidIQ 0. Long video #2 (SIP vs lump sum) still waits for Junaid's OK on the script.
- Numbers re-run: EMI ₹43,391, month-1 interest ₹35,417, principal ₹7,974, total interest ₹54.14 lakh.
- Credits today: ElevenLabs 0, Runway 0 (149 left), vidIQ 0 (0 left).
- Owner (30 Oct, chat): liked prompts 2-4 from a creator Reel (pain → hooks, write Reel, improve hook) → STYLE_GUIDE "Script pipeline"; owner: "I leave it to you, make the channel monetized" → produced it today.
  New Short Thu 5 Nov "Paise Kaise Bachaye: ₹5,000 Kharche = ₹50 Lakh? 😱 #shorts" → videos/kharche_50_lakh_real.mp4 (34.5 s, realistic presenter, 9 shots, HeyGen hook + outro). Project assets/real/kh, overlays short3d "kh".
  STANDING RULE #1 source: warikoo "15,000 SALARY to 1 CRORE" (3.0M): small monthly amount → big corpus; our angle = everyday small spends.
  Hook pipeline: chosen "₹5,000 ke kharche = ₹50 lakh?" (₹ figure + contrast); runners-up "Salary 15 tareekh tak khatam?", "Chai-sutta aur Swiggy ne ₹50 lakh kha liye?" (brand name → dropped).
  Numbers (Python): ₹5,000 SIP at start of month, 1%/month (12%/12), 240 months → ₹49,95,740; invested ₹12,00,000. Split ₹2,200 + ₹700 + ₹2,100 = ₹5,000 (example).
  Reused 2 shots from the credit-card Short (bill shock, hand on face), mirrored; 5 new gen-4-turbo clips + 2 new stills.
  Credits: Runway 137 (2 stills 12 + 5 clips 125) → 12 left; ElevenLabs ~7.3k (TTS 487 + Scribe 190 + HeyGen 3,030 + 3,636). Note: Scribe is NOT free (190 credits for 34 s).
  Metricool DRAFTS Thu 5 Nov: YT 411669972 (16:00), FB Reel 411669992 (16:00), IG Reel 411670031 (18:00), IG Story 411670049 (18:10, manual link sticker). Best time Thu: YT 16:00 (11,979, top). Alt title (Test & Compare, unscored, vidIQ 0): "Salary 15 Tareekh Tak Khatam? ₹50 Lakh Ka Hisaab 🤯 #shorts".

## 2026-10-31 (Sat)
**ALERT: Fri 30 Oct posts all FAILED in Metricool ("You have reached your Metricool account limit")**: lump-sum Short YT 406668993, IG Reel 406669132,
FB 406669258, IG Story 406669304. The Short never went live anywhere. Today's Sat 16:00/18:00 salary posts (YT 407872437, FB 407872497, IG 410329514,
Story 410329829) are still PENDING and will most likely fail the same way. Cause: free-plan monthly post limit (we schedule 4 posts per video:
YT + FB + IG Reel + IG Story). Assumed to reset with the new month on 1 Nov (to confirm in Metricool > Billing).
**Numbers (Metricool):**
- YouTube: subs 3 (no change since 28 Oct); daily views 22-27 Oct 10 / 42 / 68 / 56 / 5 / 11, 28-30 Oct not filled yet. vidIQ 0 credits (resets 24 Nov) → no per-video check.
- Instagram Reels lifetime: 40 crore (28 Oct) reach 1,101 (flat vs yesterday 1,099), 1,232 views, avg 17.6 s, 62% past 3 s, 29 likes, 9 saves, 7 shares.
  5 mistakes reach 710 / 10 shares; quiz 119; home-loan teaser 120. IG followers 4. Account reach 26-29 Oct: 373 / 445 / 1,088 / 15 (no new Reel 29-30 Oct → reach collapses).
**What it says:** (1) a day without a new Reel drops IG account reach from ~1,000 to ~15, so a missed post costs a whole day of distribution; (2) the post limit,
not the content, is now the bottleneck: 4 posts/video × 1 video/day ≈ 120 posts/month.
**Improvements (applied / proposed to Junaid):**
1. Post budget: from now 3 Metricool posts per video (YT + IG Reel + FB Reel); the IG Story is done by hand by sharing the live Reel to Story + YouTube link
   sticker (10 s, he had to touch every Story anyway for the sticker). Saves 25% of the limit. Asked Junaid: upgrade Metricool OR keep this rule.
2. YouTube first: when the limit is close, YT post is created before IG/FB (views on YouTube = main goal). Wed 4 Nov Byaaj Monster IG repost (draft 410801443,
   home-loan repeat, expected ~120 reach) is the first slot to drop if the limit stays.
3. Re-queue the failed lump-sum Short: no free day until Fri 6 Nov (queue Sat-Thu full) → propose Fri 6 Nov 16:00 YT/FB, 18:00 IG, once Junaid says yes.
- No production today: Runway 12 credits (plan 0), vidIQ 0. Next new Short (week of 9 Nov) needs a Runway top-up (~150 credits per realistic Short).
- Still waiting for Junaid's yes: Mon 2 Nov home-loan galtiyan, Tue 3 Nov credit card, Wed 4 Nov Byaaj Monster IG, Thu 5 Nov kharche ₹50 lakh; long video #2 (SIP vs lump sum) script.
- Credits today: ElevenLabs 0, Runway 0 (12 left), vidIQ 0 (0 left).
- 31 Oct 11:20: Junaid upgraded Metricool (to be confirmed by today's 16:00 posts) and bought Runway credits → Runway 3,012 (purchased, plan 0). Enough for ~20 realistic Shorts (~150 each).
- 31 Oct 12:20: Junaid: "upload on all platforms at your time" → scheduled (new posts; updateScheduledPost blocked, so old drafts stay as unused drafts):
  Mon 2 Nov home-loan galtiyan YT 411957213 / FB 411957441 (16:00), IG 411957450 (18:00), Story 411957456 (18:10);
  Tue 3 Nov credit card YT 411957711 / FB 411957717, IG 411957722, Story 411957730;
  Wed 4 Nov failed lump-sum Short re-queued: YT 411957985 / FB 411957992, IG 411958000, Story 411958008;
  Thu 5 Nov kharche: FB 411958321, IG 411958331, Story 411958342 — YT create blocked by a permission check → Junaid schedules draft 411669972 by hand;
  Fri 6 Nov 18:00 Byaaj Monster IG Reel 411958348 (moved from Wed). All IG captions now carry a follow line.
- Owner feedback: target = followers; realistic girl instead of cartoon; more interactive; Seedance allowed → STYLE_GUIDE "Owner direction (31 Oct)".
- 31 Oct 16:10: Metricool upgrade confirmed: salary Short PUBLISHED on YouTube (kyEt26giIuM) and Facebook (reel 1120207264065150).
- 31 Oct 18:30: Sat Story did not go live (autoPublish false = only a phone reminder). Re-posted as auto Story 412136002 (18:36); auto Stories 1-5 Nov: 412136010/018/033/042/049 (18:10).

## 2026-11-01 (Sun)
**Checks:** Sat 31 Oct salary Short PUBLISHED on YT (kyEt26giIuM), FB, IG Reel (DfKKXPGALTn) and auto Story 412136002. No ERROR posts; no YouTube/Instagram/Metricool alert mails.
Fixed: Thu 5 Nov kharche Short had NO scheduled YouTube post (only draft 411669972; create had been blocked on 31 Oct) → created YT 412650878 (16:00) myself today.
**Plans:** Runway 3,012 → ~2,794 after today (purchased credits, plan 0; fine for ~12 more Shorts). vidIQ 0 (resets 24 Nov). ElevenLabs est. ~60k used since the Oct cycle (today ~9.7k) → still > 15k left. Metricool upgraded (no cap). No alert needed.
**Numbers (Metricool):** YouTube subs 3 (no change); daily views 25-28 Oct 56 / 5 / 11 / 2, 29-31 Oct not filled yet (vidIQ 0 → no per-video check).
Instagram Reels lifetime: 40 crore 1,102 reach / 1,232 views / 9 saves / 7 shares (flat); 5 mistakes 710 / 10 shares; salary Reel (31 Oct, animated) 209 reach in ~15 h, 240 views, avg 14.0 s, 64.5% past 3 s, 3 likes, 0 saves, 0 shares. IG followers 4. Account reach 31 Oct 211 (vs 0-15 on the two no-Reel days).
**What it says:** (1) the salary Reel holds well past 3 s (64.5%) but earned zero saves/shares: a comparison story without a "send this to X" trigger does not spread; the two breakout Reels both had a numbered list + a specific person to send it to. (2) Days without a new Reel still drop IG reach to ~0, so the daily Reel + Story chain must never break. (3) YouTube daily views fell to 2-11/day from 56-68 when the cartoon Shorts were running; realistic Shorts resume Mon-Fri.
**Improvements applied:**
1. Share trigger in the script itself, not only the caption: new FD Short's spoken outro = "ye video us dost ko bhejo jiske papa sirf FD pe bharosa karte hain" + HAAN/NAA comment question; IG caption numbered 1-4.
2. First Instagram CAROUSEL (save-bait): Tue 3 Nov 11:00 "Credit card 'free' hai? 3 chupi kamai" (7 slides, our own tools/carousel.py renderer so every ₹ figure is exact; Canva not needed for text slides) → IG 412659168.
3. Fri 6 Nov IG slot given to the NEW FD Reel (best hour 18:00); the Byaaj Monster home-loan repost moved to Sat 7 Nov 18:00 (412658798) so the IG chain has a Reel on Saturday too.

**Produced today:** Fri 6 Nov Short "FD Ka Sach: 7% FD Mein Paisa Ghat Raha Hai? 😱 #shorts" → videos/fd_asli_return_real.mp4 (36.6 s, realistic presenter, 12 shots ~2-3 s each, HeyGen 9:16 hook + outro, papa character added). Project assets/real/fd, overlays short3d "fd".
  STANDING RULE #1 source: warikoo "Make regular income from your investments" (4.6M, next unused idea in the list): what your FD income really earns after tax + inflation. Our script/numbers.
  SHARE TEST: relatable 5 (papa's FD), not common knowledge 4, surprising ₹ number 5 (₹16 lakh looks like ₹9 lakh), send-to trigger 5 ("jiske papa sirf FD pe bharosa karte hain") = 19/20.
  Hooks: chosen "Papa ki 7% FD paisa ghata rahi? Haan ya naa?"; runners-up "₹10 lakh FD = asli mein ₹9 lakh?", "FD ka byaaj ₹70,000, haath mein ₹49,000?".
  Numbers (Python): 7% × 0.70 = 4.9% → ₹49,000/yr on ₹10 lakh; 6% inflation needs ₹60,000 → ~₹11,000/yr buying power lost; real return (1.049/1.06 − 1) = −1.04%; 10 yr: ₹10L × 1.049^10 = ₹16.13L, ÷ 1.06^10 = ₹9.01L in today's prices. (With 4% cess: 4.816%, ₹8.94L.)
  Line 7 ("tax aur mehngai ke baad ka return dekho") cut from the voice to keep 36.6 s; it is on screen as a caption instead. Voice atempo 1.2 (was 1.12) + internal pauses capped at 0.22 s.
  Metricool (scheduled, not drafts) Fri 6 Nov: YT 412659089 (16:00), FB Reel 412659098 (16:00), IG Reel 412659109 (18:00), IG Story 412659116 (18:10, auto, story_fd.jpg).
  Alt title (Test & Compare, unscored, vidIQ 0): "FD Interest Ka Sach: ₹10 Lakh Asli Mein ₹9 Lakh? 🤯 #shorts".
  Credits: ElevenLabs ~9.7k (TTS ~613 + HeyGen 3,636 + 5,453); Runway ~218 (3 stills 18 + 8 gen-4-turbo clips 200), left ~2,794; vidIQ 0. Reused 2 older shots (kh b_write, cc c3a mirrored).
- Tool: tools/carousel.py (4:5 carousel decks + Story cards with the "Full video: YouTube Paisa Science (link bio mein)" line).
- Queue now: Sun 1 F&O, Mon 2 home-loan galtiyan, Tue 3 credit card (+ carousel 11:00), Wed 4 lump sum, Thu 5 kharche, Fri 6 FD (all 3 platforms + Story), Sat 7 IG repost only → next run produces Sat 7 Nov (YT/FB/IG) + Sat carousel.

## 2026-11-02 (Mon)
**Checks:** Sun 1 Nov F&O Short PUBLISHED on YT (407950082), FB (407950135), IG Reel (410329524) + auto Story 412136010. No ERROR posts; no YouTube/Instagram/Metricool/Runway/ElevenLabs alert mails (Gmail, last 2 days). Old 2-5 Nov DRAFTS (4085525xx, 4096767xx, 4103295xx, 4116699xx/4116700xx) stay unused; the scheduled copies (4119572xx-4119583xx, 412650878, 4121360xx) are PENDING.
**Plans:** Runway 2,794 → 2,515 after today (purchased, fine for ~9 more Shorts). vidIQ 0 (resets 24 Nov). Metricool upgraded. ElevenLabs est. ~68.5k used this cycle (today ~8.5k: TTS 582 + HeyGen hook 3,030 + outro 4,848) → ~31k left = ~3-4 realistic Shorts at the current recipe → ALERT sent to Junaid (top-up/upgrade link) because the daily production will hit it around 5-6 Nov unless the cycle resets first.
**Numbers (Metricool):** YouTube subs 3 (no change); daily views 26-29 Oct 5 / 11 / 2 / 15, 30 Oct-1 Nov not filled yet; vidIQ 0 → no per-video check.
Instagram Reels lifetime: salary (31 Oct) reach 430 (was 209 at 15 h) / 486 views / avg 13.5 s / 63% past 3 s / 8 likes / 0 saves / 0 shares; F&O (1 Nov, ~21 h) reach 118 / 145 views / avg 10.4 s / 57.5% past 3 s / 1 like / 0 saves / 0 shares; 40 crore 1,102 (flat); quiz 119.
**What it says:** (1) the last two animated Reels (salary, F&O) got 0 saves and 0 shares, the 40 crore + 5 mistakes Reels got 7-10 shares each: the difference is a numbered ₹ list + a named friend to send it to; (2) 3-s hold 57-63% is fine, so the weak point is the share trigger and the end of the video, not the hook; (3) realistic Shorts start on YouTube today (Mon-Sat), first 48 h data on 4 Nov.
**Improvements applied:**
1. New Sat Short is a 2-character story (Riya vs Aman) with the "send to" person inside the story itself ("jo kehta hai abhi toh umar hai") and an A-or-B identity question ("Aap Riya ho ya Aman?") as the comment CTA: identity questions are easier to answer than number questions.
2. Sat carousel = companion table of the Reel (start @25/30/35/40/45) so the Reel viewer has a save-bait follow-up on the profile the same day.
3. ElevenLabs saving: from the next Short the lip-sync outro stays <= 5 s (send line + question only; follow line moves to on-screen text). Today's 7.9 s outro cost 4.8k vs 3.0k for the hook.
- Metricool: Sat 7 Nov IG repost (Byaaj Monster) moved to Sun 8 Nov 10:00 (updateScheduledPost worked, new id 413537375) to free Sat 18:00 for the new Reel.

**Produced today:** Sat 7 Nov Short "SIP Kab Shuru Kare? ₹3 Lakh vs ₹15 Lakh Ka Sach 😱 #shorts" → videos/riya_aman_5_saal_real.mp4 (35.8 s, realistic presenter, 11 shots ~2-3 s, HeyGen hook + outro). Project assets/real/ra, overlays short3d "ra".
  STANDING RULE #1 source: warikoo "AAPKE 20s ke liye COMPLETE FINANCIAL PLANNING" (3.8M, next unused): start investing in your 20s; our angle = 5 early years beat 25 late years.
  SHARE TEST: relatable 5, not common knowledge 4 (₹3L beats ₹15L is surprising even for people who know "start early"), surprising ₹ number 5, send-to trigger 5 ("jo kehta hai abhi toh umar hai") = 19/20.
  Hooks: chosen "₹3 lakh, ₹15 lakh se zyada kaise? Haan ya naa?"; runners-up "5 saal late = ₹1.48 crore kam?", "Har din ki deri = ₹8,000 ka nuksaan?" (per-day figure sounded too much like hype → dropped).
  Numbers (Python): ₹5,000 at start of month, 1%/month. Riya 25-30: 60 months → ₹4,12,432, then 360 months → ₹1,48,26,776. Aman 35-60: 300 months → ₹94,88,175. In today's prices (6%, 35 yr) Riya ≈ ₹19.29 lakh. Carousel: start @25 ₹3.25 Cr, @30 ₹1.76 Cr, @35 ₹94.9 L, @40 ₹49.96 L, @45 ₹25.2 L.
  Line 7 ("byaaj pe byaaj ko paisa nahi, samay chahiye") cut from the voice for length; on screen instead. Voice atempo 1.25.
  Metricool (scheduled): YT 413537643 (16:00), FB Reel 413537650 (16:00), IG Reel 413537660 (18:00), IG Story 413537666 (18:10, auto, story_riya_aman.jpg), IG carousel 413537673 (11:00, 7 slides).
  Alt title (Test & Compare, unscored, vidIQ 0): "25 vs 35 Mein Investing: ₹1.48 Crore vs ₹95 Lakh 🤯 #shorts".
  Credits: ElevenLabs ~8.5k; Runway 279 (9 stills 54 + 9 gen-4-turbo clips 225), left 2,515; vidIQ 0. clipcheck: all 9 clips PASS, contact sheet clean.
- Queue now: Mon 2 home-loan galtiyan, Tue 3 credit card (+ carousel 11:00), Wed 4 lump sum, Thu 5 kharche, Fri 6 FD, Sat 7 Riya vs Aman (+ carousel 11:00), Sun 8 IG repost 10:00 → next run produces Sun 8 Nov (YT/FB/IG 18:00).

## 2026-11-03 (Tue)
**Checks:** Mon 2 Nov home-loan galtiyan PUBLISHED on YT (p9ESCG_aVsw), FB (reel 1627535656052731), IG Reel (DfPT9-ikWYM) + auto Story 412136018. No ERROR posts; no YouTube/Instagram/Metricool/Runway/ElevenLabs mails (Gmail, 2 days). Today's posts (credit card YT 411957711 / FB 411957717 16:00, IG 411957722 18:00, Story 412136033, carousel 412659168 11:00) PENDING. Old drafts 4085525xx/4096767xx/4103295xx stay unused.
**Plans:** Runway 2,459 (purchased; fine for ~9 Shorts). vidIQ 0 (resets 24 Nov). Metricool upgraded. ElevenLabs est. ~31k → ~17.8k after today's lip-sync test (13.2k). Already alerted on 2 Nov; top-up decision after the test on 10 Nov. Next Shorts use hook-only lip-sync (~3k) → re-alert only if the estimate falls under ~5k.
**Numbers (Metricool):** YouTube subs 3 (no change). Per-video lifetime (all videos connector, data to 31 Oct): realistic Shorts 22-24 Oct 24 / 64 / 88 views; animated Shorts 26-31 Oct 2-8 views; long video 12. Daily views 28-30 Oct 2 / 15 / 1, 31 Oct-2 Nov not filled yet. First realistic Short of the new run (credit card) goes live today 16:00.
Instagram Reels lifetime: home-loan galtiyan (2 Nov, <1 day) reach 866 / 997 views / avg 14.6 s / 68% past 3 s / 15 likes / 4 saves / 0 shares / 1 comment (2nd best Reel ever, best 3-s hold); F&O 337 / 62%; salary 431 / 63%; 40 crore 1,102. IG followers 5 (+1). Account reach 31 Oct 309, 1 Nov 310, 2 Nov 1,005.
**What it says:** (1) numbered "galtiyan" list Reels keep winning on IG (5 mistakes 710, home-loan galtiyan 866 in a day, 68% hold) vs story/comparison Reels (~330-430); (2) shares are still ~0 on every Reel since 28 Oct: the named "send to" person is in the caption but not yet felt in the video; (3) YouTube: cartoon Shorts got 2-8 views, realistic 24-88: the realistic run (3-8 Nov) is the real test.
**Improvements applied:**
1. LIP-SYNC TEST Short built for Sun 8 Nov (owner test): she talks to camera ~59% of the video (hook, 2 mid lines, outro), every talk clip split into normal + 1.15x punch-in so the shot changes every ~2-2.5 s (14 shots in 31.9 s).
2. Interactive A/B quiz from frame 1 ("₹1 LAKH BONUS: A) bike loan B) credit card") + the "send to" person spoken in the video ("us dost ko bhejo jo card ka sirf minimum bharta hai") + identity question ("Aap A ho ya B?") to push comments and shares.
3. HeyGen pricing learned: Avatar 4 bills in steps (≤5 s = 3,030 credits, ≤6 s = 3,636). Keep every talk clip ≤ 5.0 s incl. padding (today's 5.9 s hook cost 606 extra).

**Produced today:** Sun 8 Nov Short "Kaunsa Loan Pehle Chukaye? ₹50,000 Ka Farak 😱 #shorts" → videos/bonus_bike_ya_card_real.mp4 (31.9 s, realistic presenter, LIP-SYNC TEST: 4 HeyGen 9:16 expressive clips). Project assets/real/bk, overlays short3d "bk".
  STANDING RULE #1 source: warikoo "How To Pay Off Your Loans FAST? | Leave the EMI TRAP Forever!" (3.8M, highest unused replicable idea on OutlierKit's warikoo list): pay the costliest debt first. Our story/numbers.
  SHARE TEST: relatable 5 (bonus + EMIs + card), not common knowledge 4 (most close the "loan" because an EMI disappears), surprising ₹ number 4 (~₹50,000), send-to trigger 4 ("jo card ka sirf minimum bharta hai") = 17/20.
  Hooks: chosen "₹1 lakh bonus: bike loan ya credit card? A ya B?"; runners-up "Ek EMI kam = ₹50,000 ka nuksaan?", "Bonus aaya? Pehle ye loan chukao".
  Numbers (Python): card ₹1,00,000 × (1.035^12 − 1) = ₹51,107 + 18% GST ₹9,199 = ₹60,306; bike ₹1,00,000 × ((1+0.10/12)^12 − 1) = ₹10,471; difference ₹49,835. Assumption on screen: no payment for 1 year (comparison only).
  Line 7 ("rule: sabse mehenga byaaj, sabse pehle") cut from the voice for length, on screen in shot 12. Voice atempo 1.25.
  Reused 4 older shots (ra Aman sofa + stressed, fd calculator, cc bill shock); 1 new Aman-with-bike still + 2 gen-4-turbo clips (clipcheck PASS, contact sheet clean).
  Metricool (scheduled): YT 414827242 (16:00, best Sun hour 5,648), FB Reel 414827273 (16:00), IG Reel 414827303 (18:00), IG Story 414827316 (18:10, auto, story_bonus_bike_card.jpg).
  Alt title (Test & Compare, unscored, vidIQ 0): "₹1 Lakh Bonus: Bike Loan Ya Credit Card? 🤯 #shorts".
  Credits: ElevenLabs ~13.2k (TTS 492 + HeyGen 3,636 + 3 × 3,030); Runway 56 (1 still 6 + 2 clips 50), left 2,459; vidIQ 0.
- Compare on Tue 10 Nov (48 h): this LIP-SYNC TEST vs realistic Shorts of 3-7 Nov (YT views, engaged/views, avg % viewed, subs; IG reach, 3-s hold, shares, follows).
- Queue now: Tue 3 credit card (+ carousel 11:00), Wed 4 lump sum, Thu 5 kharche, Fri 6 FD, Sat 7 Riya vs Aman (+ carousel 11:00), Sun 8 bonus A/B (lip-sync test) + IG repost 10:00 → next run produces Mon 9 Nov (hook-only lip-sync).

## 2026-11-04 (Wed)
**Checks:** Tue 3 Nov credit card Short PUBLISHED on YT (Ch6TtsbrHI0), FB (reel 3375155402873142), IG Reel (DfR42Y6CYKO), auto Story 412136033 and carousel 412659168 (DfRIxmZioMr). No ERROR posts; no YouTube/Instagram/Metricool/Runway/ElevenLabs mails (Gmail, 2 days). Today's lump-sum posts (YT 411957985 / FB 411957992 16:00, IG 411958000 18:00, Story 412136042) PENDING; old drafts (409676xxx, 410329xxx, 410801443) stay unused.
**Plans:** Runway 2,419 → 2,158 after today (purchased; ~10 more Shorts). vidIQ 0 (resets 24 Nov). Metricool upgraded. ElevenLabs est. ~17.8k → ~15.0k after today (TTS 398 + HeyGen 2,424) = ~5 more hook-only Shorts → runs out around the 9-10 Nov production run → alert re-sent (top-up link) since the 10 Nov test decision is the same day.
**Numbers (Metricool):** YouTube subs 3 (no change). Per-video (data to 1 Nov): F&O 15 views (avg 14 s), salary 4, home-loan EMI 7, 40 crore 8; realistic Shorts 22-24 Oct still the best (24 / 64 / 88). Daily views 28-31 Oct 2 / 15 / 1 / 7; 1-3 Nov not filled yet.
Instagram Reels lifetime: credit card (3 Nov, first realistic Reel, ~16 h) reach 61 / 81 views / avg 7.2 s / 40% past 3 s / 0 likes / 0 saves / 0 shares / 1 comment; home-loan galtiyan (animated list) 921 / 68%; F&O 338 / 62%; salary 431 / 63%; 40 crore 1,102 (flat). IG account: 5 followers.
**What it says:** (1) the first realistic Reel is far weaker on IG than the animated list Reels at the same age (61 vs 866 reach, 40% vs 68% hold) while realistic wins on YouTube (24-88 vs 2-15 views); one data point, re-check 5-6 Nov after the FD + lump-sum Reels. (2) "numbered list + ₹ in frame 1" is what won on IG (5 mistakes, galtiyan) → put that structure inside the realistic format. (3) YouTube Studio data for 2-3 Nov not in yet; the realistic run's 48 h check stays on Thu-Fri.
**Improvements applied:**
1. Mon 9 Nov Short = realistic presenter + numbered list ("KHARCHA #1 / #2 / #3") with the ₹ claim on screen from frame 1 and spoken at 0.0 s ("₹50 lakh ka ghar, asal mein ₹97 lakh ka? Haan ya naa?"): combines what wins on YouTube (presenter) with what wins on IG (list + ₹ figure).
2. HeyGen tier learned: a talk clip ≤ 4.0 s (audio incl. padding) costs 2,424 credits vs 3,030 for ≤ 5.0 s → keep the hook line ≤ 3.75 s spoken. Today's Short used 2.8k ElevenLabs in total (was 3.6-13.2k).
3. First video in the new saree look (owner, 4 Nov): HeyGen image + all b-roll of her from saree portrait b43b0c4f; no old kurta shots of her (dropped r_calc), only a kurta-free Aman shot reused.

**Produced today:** Mon 9 Nov Short "Ghar Ka Asli Kharcha: ₹50 Lakh = ₹97 Lakh? 😱 #shorts" → videos/ghar_97_lakh_real.mp4 (30.6 s, realistic presenter, saree look, 14 shots ~2.2 s, hook-only lip-sync split a/b, outro voice-over on b-roll). Project assets/real/gh, overlays short3d "gh".
  STANDING RULE #1 source: warikoo "BUYING a 50L HOUSE Without a LOAN" (~2.0M, next unused on the list): the true cost of a ₹50 lakh house. Our script/numbers.
  SHARE TEST: relatable 5 (ghar lena), not common knowledge 4 (most people never add down payment + stamp duty + total EMIs), surprising ₹ number 5 (₹50L → ~₹97L), send-to trigger 5 ("us dost ko jo ghar lene wala hai") = 19/20.
  Hooks: chosen "₹50 lakh ka ghar, asal mein ₹97 lakh ka? Haan ya naa?"; runners-up "Ghar ki price tag jhooth bolti hai?", "₹43 lakh sirf byaaj, ghar ₹50 lakh ka?".
  Numbers (Python): 20% down ₹10,00,000; loan ₹40,00,000 @8.5%, 240 months → EMI ₹34,713, total EMIs ₹83,31,103, interest ₹43,31,103; stamp duty + registration ~7% example ₹3,50,000; all-in ₹96,81,103.
  Metricool (scheduled): YT 416079268 (16:00), FB Reel 416079285 (16:00), IG Reel 416079299 (18:00), IG Story 416079311 (18:10, auto, story_ghar_97_lakh.jpg).
  Alt title (Test & Compare, unscored, vidIQ 0): "₹50 Lakh Ka Ghar Asli Mein ₹97 Lakh Ka? 🤯 #shorts".
  Credits: ElevenLabs ~2.8k (TTS 398 + HeyGen 2,424); Runway 261 (6 stills 36 + 9 gen-4-turbo clips 225), left 2,158; vidIQ 0. clipcheck: 10/10 PASS; contact sheet: c6 (odd arm raise) not used.
- Queue now: Wed 4 lump sum, Thu 5 kharche, Fri 6 FD, Sat 7 Riya vs Aman (+ carousel 11:00), Sun 8 bonus A/B (lip-sync test) + IG repost 10:00, Mon 9 ghar ₹97 lakh → next run produces Tue 10 Nov (+ Tue carousel 11:00).

## 2026-11-05 (Thu)
**Checks:** Wed 4 Nov lump-sum Short PUBLISHED on YT (411957985), FB (411957992), IG Reel (411958000) + Stories 411958008 and 412136042 (two Stories went up: the 31 Oct auto copy and the old one; harmless). No ERROR posts; no YouTube/Instagram/Metricool/Runway/ElevenLabs mails (Gmail, 2 days). Today's kharche posts (YT 412650878 / FB 411958321 16:00, IG 411958331 18:00, Stories 411958342 + 412136049) PENDING; old drafts (4116699xx/4116700xx, 410801443) stay unused.
**Plans:** Runway 2,158 → 1,897 after today (purchased; ~7 more Shorts). vidIQ 0 (resets 24 Nov). Metricool upgraded. ElevenLabs est. ~15.0k → ~12.1k after today (TTS 453 + HeyGen 2,424) = ~4 more hook-only Shorts (covers production through ~9 Nov runs → Wed 11-Sat 14 Nov uploads). Already alerted 2 + 4 Nov; re-alert only under ~5k (rule from 3 Nov). No alert today.
**Numbers (Metricool):** YouTube subs 3 (no change); per-video data still only to 1 Nov (F&O 15, salary 4, home-loan EMI 7, 40 crore 8; realistic 22-24 Oct 24 / 64 / 88). Daily views 29-31 Oct 15 / 1 / 7; 1-4 Nov not filled yet → realistic-run 48 h check moves to Fri.
Instagram Reels lifetime: credit card (realistic, 3 Nov, ~2 days) reach 99 / 129 views / avg 8.2 s / 42% past 3 s / 0 saves / 0 shares; lump sum (animated cut-down, 4 Nov, <1 day) 103 / 63%; home-loan galtiyan 923 / 68% / 4 saves; F&O 340; salary 432; 40 crore 1,102 / 9 saves / 7 shares.
**What it says:** (1) the realistic credit-card Reel is still the weakest on IG (99 reach, 42% hold) while animated Reels hold 62-68%: one data point, the FD (Fri) and Riya/Aman (Sat) realistic Reels decide; if both stay < 50% hold → IG-only TRIAL_REEL variant with list headline + bigger ₹ in the first 0.5 s (rule from 4 Nov). (2) Saves/shares only come from numbered-list Reels (40 crore, 5 mistakes, galtiyan) → every new Short keeps a numbered "CHUPA KHARCHA #1/#2" structure. (3) All topics since 28 Oct were loans/SIP/FD; a fresh life-event topic (wedding gold, Nov-Dec shaadi season) widens the "send to" audience.
**Improvements applied:**
1. Tue 10 Nov Short = new topic family (gold jewellery / shaadi) with the strongest send-to trigger so far ("us dost ko jiski shaadi hone wali hai") spoken + on screen + in every caption.
2. IG hook fix inside the video: ₹ figure + question on frame 1 ("₹5.92 LAKH KA GEHNA / BECHO = ₹5 LAKH?"), list headers "CHUPA KHARCHA #1/#2", identity A/B CTA ("Gehna: nivesh ya shauk?").
3. Carousel Tue 10 Nov 11:00 built as a companion "find your making %" table (8% / 15% / 25%) + pre-purchase checklist, so the Reel and carousel cross-feed saves on the same day.

**Produced today:** Tue 10 Nov Short "Gold Making Charge Ka Sach: ₹92,000 Gaayab? 😱 #shorts" → videos/gehna_asli_kharcha_real.mp4 (30.3 s, realistic presenter, saree look, 14 shots ~2.2 s, hook-only lip-sync split a/b, outro voice-over on b-roll). Project assets/real/gd, overlays short3d "gd".
  STANDING RULE #1 source: warikoo "How To INVEST in GOLD and SILVER" (~1.4M, next unused on the list after Gen Z saving, which overlaps the Thu kharche Short): what gold jewellery really costs vs what it is worth. Education only, no products/brands.
  SHARE TEST: relatable 5 (shaadi/tyohaar gehna), not common knowledge 4 (most never add making + GST vs resale), surprising ₹ number 5 (~₹92,000 on day 1, +18.5% just to break even), send-to trigger 5 ("jiski shaadi hone wali hai") = 19/20.
  Hooks: chosen "Chhah lakh ka gehna, becho toh sirf paanch lakh? Haan ya naa?"; runners-up "Making charge: ₹75,000 jo kabhi wapas nahi aata?", "Sona 18% badhe tab jaake barabar?".
  Numbers (Python): sona ₹5,00,000; making 15% (example, ~8-25%) ₹75,000; GST 3% × ₹5,75,000 = ₹17,250; bill ₹5,92,250; sell-back assumed = gold value only, no deduction → gap ₹92,250; break-even 18.45%. Carousel: 8% → ₹5,56,200 (11.24%), 25% → ₹6,43,750 (28.75%).
  Metricool (scheduled): YT 417316638 (16:00), FB Reel 417316654 (16:00), IG Reel 417316671 (18:00), IG Story 417316693 (18:10, auto, story_gehna.jpg), IG carousel 417316707 (11:00, 7 slides, instagram/carousel_gehna).
  Alt title (Test & Compare, unscored, vidIQ 0): "₹5.92 Lakh Ka Gehna, Wapas ₹5 Lakh? 🤯 #shorts".
  Credits: ElevenLabs ~2.9k (TTS 453 + HeyGen 2,424); Runway 261 (6 stills 36 + 9 gen-4-turbo clips 225), left 1,897; vidIQ 0. clipcheck 9/9 PASS; contact sheet clean (c3 ends in a smile → only its first 2.3 s + punch-in used).
- Queue now: Thu 5 kharche, Fri 6 FD, Sat 7 Riya vs Aman (+ carousel 11:00), Sun 8 bonus A/B (lip-sync test) + IG repost 10:00, Mon 9 ghar ₹97 lakh, Tue 10 gehna (+ carousel 11:00) → next run produces Wed 11 Nov.

## 2026-11-06 (Fri)
**Checks:** Thu 5 Nov kharche Short PUBLISHED on YT (412650878), FB (411958321), IG Reel (411958331) + Stories 411958342 / 412136049. No ERROR posts; no YouTube/Instagram/Metricool/Runway/ElevenLabs mails (Gmail, 2 days). Today's FD posts (YT 412659089 / FB 412659098 16:00, IG 412659109 18:00, Story 412659116) PENDING. Old drafts (4116699xx/4116700xx) stay unused.
**Plans:** Runway 1,897 → 1,617 after today (purchased; ~6 more Shorts). vidIQ 0 (resets 24 Nov). Metricool upgraded. ElevenLabs est. ~12.1k → ~9.2k after today (TTS 463 + HeyGen 2,424) = ~3 more hook-only Shorts → runs out at the ~9 Nov production run (Sat 14 Nov upload) → alert sent with the top-up link (inside the 7-day window). If it runs out: switch to voice-over-only Shorts (no lip-sync, ~0.5k each) until topped up.
**Numbers (Metricool):** YouTube subs 3 (no change). Per-video (data to 2 Nov): F&O 22 views, home-loan galtiyan 12, 40 crore 10, home-loan EMI 7, salary 4; realistic 22-24 Oct still best (24 / 64 / 88). Daily views 29 Oct-2 Nov 15 / 1 / 7 / 15 / 21; 3-5 Nov (first realistic run days) not filled yet.
Instagram Reels lifetime: kharche (realistic, 5 Nov, <1 day) reach 115 / 133 views / avg 6.5 s / 46.7% past 3 s / 2 likes / 0 saves / 0 shares; credit card (realistic, 3 Nov) 99 / 42%; lump sum (animated cut-down) 126 / 63%; home-loan galtiyan (animated list) 923 / 68% / 4 saves; F&O 340 / 62%; salary 432 / 63%; 40 crore 1,102 / 62% / 9 saves / 7 shares.
**What it says:** (1) realistic Reels on IG: 42% and 47% past 3 s vs 57-68% for animated Reels; FD tonight is the 3rd data point. (2) Avg watch on realistic Reels is 6.5-8 s vs 13-17 s for animated ones, so the drop is not only the hook: viewers leave mid-video. (3) YouTube per-video data is still 4 days behind, so the realistic-run YT verdict moves to Sun 8 Nov.
**Improvements applied:**
1. Topic = realistic remake of our best-ever IG idea (40 crore family, 1,102 reach): if this Reel also stays < 50% hold, the format (not the topic) is the IG problem → from 8 Nov the IG Reel gets an IG-only variant (bigger ₹ headline + motion in frame 1) or the animated style for IG while YT keeps the realistic girl.
2. Numbered "STEP #1 / STEP #2" structure with a mid-video reveal ("6 SAAL PEHLE!" at ~17 s) to give viewers a reason to stay past 10 s; identity CTA "Step 1 ya step 2?" + named send-to ("jiski pehli salary ₹15,000 hai").
3. QA rule: gen-4-turbo turned "steam rises from the mug" into a cloud over her face (c1b, dropped) → added steam/smoke/fog to the banned prompt words in STYLE_GUIDE; reused the clean clip's tail with a 1.15x punch-in instead (no extra credits).

**Produced today:** Wed 11 Nov Short "₹15,000 Salary Se ₹1 Crore? 6 Saal Pehle Kaise 😱 #shorts" → videos/salary_15k_1crore_real.mp4 (30.8 s, realistic presenter, saree look, 14 shots ~2.2 s, hook-only lip-sync split a/b, outro voice-over on b-roll + "send to" friend shot). Project assets/real/sl, overlays short3d "sl".
  STANDING RULE #1 source: warikoo "15,000 SALARY to 1 CRORE" (~3.0M, next unused on the list). Our script/numbers.
  SHARE TEST: relatable 5 (first salary), not common knowledge 4 (most think ₹15k can't reach ₹1 crore, and nobody counts the years saved by step-up), surprising ₹ number 4 (~29.5 → ~23.5 saal), send-to trigger 5 ("jiski pehli salary ₹15,000 hai") = 18/20.
  Hooks: chosen "₹15,000 ki salary se ₹1 crore? Haan ya naa?"; runners-up "₹3,000 mahina = ₹1 crore, kitne saal?", "Har hike pe ye karo, ₹1 crore 6 saal pehle".
  Numbers (Python): ₹3,000 at start of month, 1%/month. Flat: 355 months (29.6 yr) → ₹1,00,61,070. +10% every 12 months: 281 months (23.4 yr) → ₹1,01,21,270. Difference 74 months (~6.2 yr). Inflation caveat on screen.
  Metricool (scheduled): YT 418519884 (16:00), FB Reel 418519899 (16:00), IG Reel 418519913 (18:00), IG Story 418519922 (18:10, auto, story_salary_1crore.jpg).
  Alt title (Test & Compare, unscored, vidIQ 0): "15000 Salary Mein 1 Crore Kaise Banaye? 🤯 #shorts".
  Credits: ElevenLabs ~2.9k (TTS 463 + HeyGen 2,424); Runway 280 (5 stills 30 + 10 gen-4-turbo clips 250), left 1,617; vidIQ 0. clipcheck 11/11 PASS; contact sheet: c1b steam cloud → dropped.
- Queue now: Fri 6 FD, Sat 7 Riya vs Aman (+ carousel 11:00), Sun 8 bonus A/B (lip-sync test) + IG repost 10:00, Mon 9 ghar ₹97 lakh, Tue 10 gehna (+ carousel 11:00), Wed 11 ₹15k → ₹1 crore → next run produces Thu 12 Nov.

## 2026-11-07 (Sat)
**Checks:** Fri 6 Nov FD Short PUBLISHED on YT (eDIEbzVKm6o), FB (reel 28962072900113554), IG Reel (DfZnKMvGaUu) + auto Story 412659116. No ERROR posts; no YouTube/Instagram/Metricool/Runway/ElevenLabs/Facebook mails (Gmail, 2 days). Today's posts (Riya/Aman YT 413537643 / FB 413537650 16:00, IG 413537660 18:00, Story 413537666 18:10, carousel 413537673 11:00) PENDING.
**Plans:** Runway 1,617 → 1,356 after today (purchased; ~5 more Shorts). vidIQ 0 (resets 24 Nov). Metricool upgraded. ElevenLabs est. ~9.2k → ~6.3k after today (TTS 480 + HeyGen 2,424) = ~2 more hook-only Shorts. Alerted 2/4/6 Nov with the link; no new alert today. Next run: if the estimate drops under ~5k, the Short after that is voice-over only (no lip-sync, ~0.5k) and Junaid gets one more push.
**Numbers (Metricool):** YouTube subs 3 (no change). Daily views 1-3 Nov 15 / 21 / 89 (3 Nov = first realistic run day, best day since 25 Oct). Per-video (data to 3 Nov): credit card (realistic) 78 views at ~1 day vs animated Shorts of 26 Oct-2 Nov 2-26 → realistic girl confirmed for YouTube.
Instagram Reels lifetime: FD (realistic, 6 Nov, <1 day) reach 104 / 128 views / avg 8.1 s / 35.4% past 3 s / 1 like / 0 saves / 0 shares; kharche (realistic) 117 / 46.4%; credit card (realistic) 99 / 42.1%; lump sum (animated cut-down) 128 / 62.6%; home-loan galtiyan (animated list) 923 / 68.1% / 4 saves; F&O 340 / 62.3%; salary 432 / 62.7%; 40 crore 1,102 / 62.1% / 9 saves / 7 shares. IG followers ~5.
**What it says:** (1) 3 realistic Reels in a row hold only 35-46% past 3 s vs 62-68% for every animated Reel: on IG the first second of the talking-head hook loses people, on YT the same format wins (78 vs 2-26 views). (2) Avg watch on realistic Reels 6-8 s vs 13-17 s animated: they also leave mid-video. (3) Reach for all recent Reels is ~100-130 (incl. the animated lump-sum cut-down), so account-level reach is low; hold rate is the lever we control.
**Improvements applied:**
1. IG-only COLD-OPEN variant (test, Thu 12 Nov): the IG Reel starts with the 1.35 s reveal moment (her facepalm-to-shock shot + "KUL ~₹3,700!" + her line "kul kareeb saintees sau!") and then plays the normal video from the hook. YT/FB keep the normal cut. Compare its 3-s hold with the 35-46% of realistic Reels; if > 55%, every IG Reel gets a cold open from 13 Nov.
2. New topic family for the Gen Z / first-job audience (no cost EMI, shopping habits) with a strong send-to ("jo har cheez EMI pe leta hai") and identity A/B CTA ("EMI wale ho ya cash wale?").
3. QA: gen-4-turbo morphed a held phone box into a dark object after ~2 s (c1b) → dropped; reused c1's tail with a 1.15x punch-in. Rule: hand-held props only for clips we use ≤ 2 s, or keep the prop on a table.

**Produced today:** Thu 12 Nov Short "No Cost EMI Ka Sach: ₹3,700 Extra? 😱 #shorts" → videos/no_cost_emi_real.mp4 (31.1 s, realistic presenter, saree look, 14 shots ~2.2 s, hook-only lip-sync split a/b, outro voice-over on b-roll + friend shot) and videos/no_cost_emi_real_ig.mp4 (32.6 s, IG cold-open variant). Project assets/real/nc, overlays short3d "nc".
  STANDING RULE #1 source: warikoo "Why Gen Z STOPPED Saving" (~2.4M, next unused on the list; angle = "no cost" EMI habit, idea also covered by Zero1 "No Cost EMIs (EXPOSED)"). Our script/numbers.
  SHARE TEST: relatable 5 (phone on EMI), not common knowledge 4 (most think "no cost" = ₹0 extra), surprising ₹ number 4 (~₹3,700 / 6%), send-to trigger 5 ("jo har cheez EMI pe leta hai") = 18/20.
  Hooks: chosen "No cost EMI pe ₹3,700 zyada? Haan ya naa?"; runners-up "No Cost EMI: byaaj kahan chhupa hai?", "₹60,000 ka phone, asal mein ₹63,700?".
  Numbers (Python): 6 × ₹10,000, 15%/12 per month → PV ₹57,460, byaaj ₹2,540 (= dukaan ka discount); GST 18% ₹457; fee ₹199 × 1.18 = ₹235; lost cash discount ₹3,000 (udaharan); total ₹3,692 = 6.2%. All rates/fees/discount on screen as examples.
  Metricool (scheduled): YT 419660048 (16:00), FB Reel 419660057 (16:00), IG Reel 419659868 (18:00, cold-open variant), IG Story 419659876 (18:10, auto, story_no_cost_emi.jpg).
  Note: Metricool now rejects instagramData on a post whose providers list has no instagram (YT/FB-only posts must omit it).
  Alt title (Test & Compare, unscored, vidIQ 0): "No Cost EMI Sach Mein Free Hai? ₹3,700 Ka Sach 🤯 #shorts".
  Credits: ElevenLabs ~2.9k (TTS 480 + HeyGen 2,424); Runway 261 (6 stills 36 + 9 gen-4-turbo clips 225), left 1,356; vidIQ 0. clipcheck 9/9 PASS; contact sheet: c1b prop morph → dropped.
- Queue now: Sat 7 Riya vs Aman (+ carousel 11:00), Sun 8 bonus A/B (lip-sync test) + IG repost 10:00, Mon 9 ghar ₹97 lakh, Tue 10 gehna (+ carousel 11:00), Wed 11 ₹15k → ₹1 crore, Thu 12 no cost EMI (IG cold-open test) → next run produces Fri 13 Nov.

## 2026-11-08 (Sun)
**Checks:** Sat 7 Nov Riya/Aman Short PUBLISHED on YT (-hRsoAwvl0w), FB (reel 1459135419478311), IG Reel (DfcL_KeEcb8), auto Story 413537666 and carousel 413537673 (Dfbb5sBDR1I). No ERROR posts; no YouTube/Instagram/Metricool/Facebook/Runway/ElevenLabs mails (Gmail, 2 days). Today's posts (IG repost 413537375 10:00, bonus A/B lip-sync test YT 414827242 / FB 414827273 16:00, IG 414827303 18:00, Story 414827316 18:10) PENDING.
**Plans:** Runway 1,356 → 1,039 after today (purchased credits, ~265/Short → ~4 Shorts = runs out at the ~12 Nov production run) → push alert with the top-up link today. vidIQ 0 (resets 24 Nov). Metricool upgraded. ElevenLabs est. ~6.3k → ~5.8k (today voice-over only, TTS 537, no HeyGen).
**Numbers (Metricool):** YouTube subs 3 (no change). Daily views 1-4 Nov 15 / 21 / 89 / 32; 5-7 Nov not filled yet. Per-video still only to 3 Nov (credit card 78, F&O 26, galtiyan 19).
Instagram Reels lifetime: Riya/Aman (realistic, 7 Nov, <1 day) reach 29 / 39 views / avg 3.7 s / 30.6% past 3 s / 0 saves; FD (realistic) 147 / 39.8%; kharche 117 / 46.8%; lump sum (animated) 128 / 62.9%; credit card 99 / 42.6%; galtiyan (animated list) 923 / 68.1%.
**What it says:** (1) 4 realistic Reels in a row hold 31-47% past 3 s on IG (animated 57-68%); Riya/Aman is the weakest (comparison story, no list). (2) The talking-head lip-sync hook is common to all weak IG Reels, so the next test removes it: Fri 13 Nov is VOICE-OVER ONLY (her shocked reaction shot with motion + big ₹ headline in frame 1, voice starts at 0.0 s). (3) YT per-video data lags 5 days; realistic Shorts still win on YT (78 vs 2-26 views).
**Improvements applied:**
1. VO-only realistic Short (no HeyGen): tests whether the lip-sync opener is what loses IG viewers, and cuts ElevenLabs use from ~2.9k to ~0.5k per Short (ElevenLabs runway now ~10 Shorts instead of 2). Compare Fri 13 IG 3-s hold vs Thu 12 cold-open and the 31-47% realistic average.
2. Numbered list structure on screen (UPGRADE #1-#4) + named send-to person ("us couple ko jo dono kamate hain") + identity CTA ("upgrade wale ya bachat wale?") + 14 shots (~2.5 s).
3. New topic family (household budget / lifestyle inflation) to widen the send-to audience beyond loans/EMI; tools/real.py now accepts a plan with no talk clip (colour ref = first clip).

**Produced today:** Fri 13 Nov Short "Do Salary, Phir Bhi Bachat Nahi? ₹54 Lakh Ka Sach 😱 #shorts" → videos/do_salary_bachat_real.mp4 (35.3 s, realistic presenter, saree look, 14 shots, VOICE-OVER ONLY TEST). Project assets/real/dk, overlays short3d "dk", story instagram/story_do_salary.jpg.
  STANDING RULE #1 source: warikoo "Why Two Incomes Are Making Indian Families Poorer" (~829K, OutlierKit warikoo outlier list, fetched today; higher unused ideas were interviews/product-heavy: "2026 Mutual Fund Strategy According to Salary" 1.1M (fund picks), "₹63 LAKH Debt" 1.0M (interview), "₹18,000 Salary to Crorepati" 1.0M (overlaps ₹15k Short)). Our script/numbers, gender-neutral ("doosri salary", not whose).
  Remaining unused on the warikoo list: "DEBT MUTUAL FUNDS Explained" 998K (needs care: no product), "WHY you think YOUR FRIENDS are RICHER than YOU?" 828K (next), "Managing Responsibilities at 18" 1.0M (interview).
  SHARE TEST: relatable 5 (two-income households), not common knowledge 4 (people feel it but never add up the upgrades), surprising ₹ number 4 (₹5,000 left of ₹50,000; ₹54 lakh in 10 yr), send-to trigger 5 ("us couple ko jo dono kamate hain") = 18/20.
  Hooks: chosen "Do salary, phir bhi bachat sirf ₹5,000? Haan ya naa?"; runners-up "Doosri salary ka 90% kahan gaya?", "₹50,000 extra, bachat sirf ₹5,000?".
  Numbers (Python): upgrades ₹15,000 + ₹12,000 + ₹8,000 + ₹10,000 = ₹45,000; ₹50,000 − ₹45,000 = ₹5,000; ₹45,000 × 120 = ₹54,00,000; half-first ₹25,000 × 120 = ₹30,00,000 (no return assumed). All amounts on screen as examples.
  Metricool (scheduled): YT 420466553 (16:00), FB Reel 420466573 (16:00), IG Reel 420466585 (18:00), IG Story 420466593 (18:10, auto).
  Alt title (Test & Compare, unscored, vidIQ 0): "Double Income, Phir Bhi Saving Zero? ₹54 Lakh 🤯 #shorts".
  Credits: ElevenLabs ~0.54k (TTS only); Runway 317 (7 stills 42 + 11 gen-4-turbo clips 275), left 1,039; vidIQ 0. clipcheck 11/11 PASS; contact sheet clean (c3 she turns her back after ~2 s, acceptable for the flat shot).
- Queue now: Sun 8 bonus A/B (lip-sync test), Mon 9 ghar ₹97 lakh, Tue 10 gehna (+ carousel 11:00), Wed 11 ₹15k → ₹1 crore, Thu 12 no cost EMI (IG cold-open test), Fri 13 do salary (VO-only test) → next run produces Sat 14 Nov (+ Sat carousel 11:00). Tue 10: 48 h lip-sync test review.

## 2026-11-09 (Mon)
**Checks:** Sun 8 Nov posts all PUBLISHED: IG repost 413537375 (Dfd5v0kDBh6, 10:00), bonus A/B lip-sync test YT (Kbf9AHJ1akg), FB (reel 1111799174995133), IG Reel (DfewyKNgSwR), auto Story 414827316. No ERROR posts; no YouTube/Instagram/Metricool/Facebook/Runway/ElevenLabs mails (Gmail, 2 days). Today's ghar ₹97 lakh posts (YT 416079268 / FB 416079285 16:00, IG 416079299 18:00, Story 416079311) PENDING.
**Plans:** Runway 1,039 → 890 after today (4 stills 24 + 5 clips 125; reused 6 older saree clips) → ~5 more Shorts at this mix, covers uploads to ~19-20 Nov; already alerted 8 Nov, no new alert. vidIQ 0 (resets 24 Nov). Metricool upgraded. ElevenLabs est. ~5.8k → ~5.2k (TTS only, 581) = ~9 more voice-over-only Shorts; no lip-sync planned (see below), so no alert.
**Numbers (Metricool):** YouTube subs 3 (no change). Daily views 1-5 Nov 15 / 21 / 89 / 32 / 7; 6-8 Nov not filled yet.
Instagram Reels lifetime: bonus A/B LIP-SYNC TEST (8 Nov, <1 day) reach 100 / 122 views / avg 3.0 s / **15.2% past 3 s** / 0 saves / 0 shares; home-loan EMI animated repost (8 Nov 10:00) 126 / 175 views / avg 13.4 s / 56.2%; Riya/Aman (realistic) 100 / 33.3%; FD 148 / 39.5%; kharche 117 / 46.8%; lump sum (animated) 128 / 62.9%; credit card 99 / 42.6%; galtiyan (animated list) 923 / 68.1%.
**What it says:** (1) LIP-SYNC TEST lost clearly on IG: the most-talking-head Reel ever held only 15% past 3 s, the same-day animated repost 56%. Talking to camera is what makes IG viewers swipe. Verdict: no extra lip-sync, no ElevenLabs top-up for lip-sync; YT side of the test still to read on Tue 10 (48 h). (2) Every Reel with a talking-head opener is < 47%, every animated/b-roll opener 56-68% → voice-over-only realistic Shorts (Fri 13 + Sat 14) are now the default unless Tue's YT data says lip-sync wins big on YouTube. (3) Reach is flat at ~100-150 for every new Reel, so hold rate stays the lever.
**Improvements applied:**
1. Sat 14 Nov Short is voice-over only (2nd in a row) with a story opener (her shocked reaction + ₹ headline at 0.0 s), and the story character (Rohan) carries the middle, so no talking head at all.
2. Cheaper production: reused 6 clean saree clips from older Shorts for generic reactions and generated only the 5 story-specific clips → 149 Runway credits instead of ~260-317 (Runway lasts ~2x longer).
3. Topic widened to social comparison (friends' cars / Insta lifestyle) with the strongest send-to so far ("us dost ko jo sochta hai sab usse ameer hain") + identity CTA ("car wale ya bachat wale?") + Sat carousel as a companion 5-year table.

**Produced today:** Sat 14 Nov Short "Dost Tumse Ameer Hai? ₹12 Lakh Car Ka Sach 😱 #shorts" → videos/dost_car_daulat_real.mp4 (35.9 s, realistic presenter (saree) + friend character, 14 shots, VOICE-OVER ONLY). Project assets/real/cr, overlays short3d "cr", story instagram/story_dost_car.jpg, carousel instagram/carousel_car (7 slides).
  STANDING RULE #1 source: warikoo "WHY you think YOUR FRIENDS are RICHER than YOU?" (~828K, next unused on the OutlierKit warikoo list). Our story/script/numbers.
  SHARE TEST: relatable 5 (friend's new car / Insta lifestyle), not common knowledge 4 (nobody subtracts the loan from the car's value), surprising ₹ number 4 (₹12 lakh car → ~₹1.63 lakh equity after 2 yr), send-to trigger 5 ("jo sochta hai sab usse ameer hain") = 18/20.
  Hooks: chosen "₹12 lakh ki car, par dost ki asli daulat sirf ₹1.6 lakh? Haan ya naa?"; runners-up "Dost tumse ameer kyun lagta hai?", "₹7 lakh diye, car mein hissa sirf ₹1.6 lakh?".
  Numbers (Python): ₹10,00,000 @9%, 60 months → EMI ₹20,758; balance after 24 EMI ₹6,52,784; paid ₹2,00,000 + 24 × ₹20,758 = ₹6,98,200; value ₹12,00,000 × 0.8 × 0.85 = ₹8,16,000 (example depreciation) → equity ₹1,63,216. Carousel: 5 yr total ₹14,45,501, interest ₹2,45,501, value ~₹5,01,126.
  QA: clipcheck 5/5 PASS; contact sheet: c2b (pats roof) has a flying yellow cloth after ~2 s → dropped, slot uses a 1.15x punch-in of c2's tail; c1 hand blur after 4.8 s → punch-in taken from 3.7-4.53 s.
  Metricool (scheduled): carousel 421353334 (11:00), YT 421353145 (16:00), FB Reel 421353304 (16:00), IG Reel 421353317 (18:00), IG Story 421353326 (18:10, auto).
  Alt title (Test & Compare, unscored, vidIQ 0): "Car Loan Ka Sach: ₹12 Lakh Car, Daulat ₹1.6 Lakh? 🤯 #shorts".
  Credits: ElevenLabs ~0.58k (TTS only, atempo 1.4); Runway 149, left 890; vidIQ 0.
- Queue now: Mon 9 ghar ₹97 lakh, Tue 10 gehna (+ carousel 11:00), Wed 11 ₹15k → ₹1 crore, Thu 12 no cost EMI (IG cold-open test), Fri 13 do salary (VO-only test), Sat 14 dost ki car (VO-only + carousel 11:00) → next run produces Sun 15 Nov. Tue 10: YT side of the lip-sync test; Sun 15: VO-only verdict (Fri 13 IG hold).
- Owner feedback (9 Nov, later): content feels repetitive (12 Shorts in a row on loans/EMI/salary with the same hook, list and ending). Decision: keep 9-14 Nov queue; from Sun 15 Nov follow the VARIETY RULE in STYLE_GUIDE (8 rotating topic areas, rotating formats, hooks and endings; first up: UPI fraud / PIN myth, myth-vs-fact format).

## 2026-11-10 (Tue)
**Checks:** Mon 9 Nov ghar ₹97 lakh posts all PUBLISHED: YT (ZkupEWbPvFM), FB (reel 1642020690700009), IG Reel (DfhVi-aldJX), auto Story 416079311. No ERROR posts; no YouTube/Instagram/Metricool/Facebook/Runway/ElevenLabs mails (Gmail, 2 days). Today's gehna posts (carousel 417316707 11:00, YT 417316638 / FB 417316654 16:00, IG 417316671 18:00, Story 417316693 18:10) PENDING.
**Plans:** Runway 890 → 735 after today (5 stills 30 + 5 gen-4-turbo clips 125; 8 reused saree clips) → ~4-5 Shorts left = runs out around the 14-15 Nov production runs (inside 7 days) → push alert with top-up link. ElevenLabs est. ~5.2k → ~4.6k (TTS only, 571) = under the 5k line → push alert (rule 3 Nov); ~8 VO-only Shorts left. vidIQ 0 (resets 24 Nov). Metricool upgraded.
**Numbers (Metricool):** YouTube subs 3 (no change). Daily views 1-6 Nov 15 / 21 / 89 / 32 / 7 / 45; 7-9 Nov not filled yet. Per-video still only to 3 Nov (credit card 78, F&O 26, galtiyan 19) → YT side of the LIP-SYNC TEST cannot be read yet (Metricool lags ~5 days, vidIQ 0 credits); re-check Thu 12.
Instagram Reels lifetime: ghar ₹97 lakh (realistic, hook-only lip-sync + numbered list, 9 Nov, <1 day) reach 100 / 125 views / avg 6.6 s / **52.3% past 3 s** (best realistic Reel so far); bonus A/B lip-sync test 100 / 15.2%; animated repost (8 Nov) 126 / 56.2%; Riya/Aman 100 / 33.3%; FD 148 / 39.5%; kharche 117 / 46.8%; lump sum 128 / 62.9%; credit card 99 / 42.6%. Saves/shares 0 on all new Reels; IG followers ~5.
**What it says:** (1) The best realistic Reel (ghar, 52%) opened on a big ₹ contrast headline ("₹50 lakh = ₹97 lakh?") with a short hook lip-sync, the worst (15%) was mostly talking head: the first-frame headline matters more than whether she talks. (2) Reach is still stuck at ~100 per Reel and shares at 0: content has been 12 loan/salary Shorts in a row (owner's repetition feedback) → variety rule starts with Sun 15. (3) YT daily views still 7-89; YT per-video data lags, no new conclusion.
**Improvements applied:**
1. VARIETY RULE first Short (Sun 15): area A fraud & scams, format MYTH vs FACT (3 numbered myths), hook type = myth statement ("Paise LENE ke liye UPI PIN? Sabse bada jhooth!"), ending = send to mummy-papa + "1, 2 ya 3?" quiz + 1930 helpline (save-worthy). New story character: papa (Runway task 9ac52836-4f34-4107-b3ce-3103ec7cf4a1) for family-safety topics.
2. Shares: send-to target is now parents (family WhatsApp groups are the biggest share channel for fraud-safety content), spoken AND on screen with a second shot of her explaining to papa.
3. Metricool now rejects twitterData when twitter is not a provider ("networkData contains data for network 'twitter'"): omit twitterData on every post.

**Produced today:** Sun 15 Nov Short "UPI PIN Daalne Se Paise Milte Hain? 3 Fraud Myth 😱 #shorts" → videos/upi_pin_myth_real.mp4 (36.3 s, realistic presenter (saree) + papa, 14 shots ~2.6 s, VOICE-OVER ONLY). Project assets/real/up, overlays short3d "up", story instagram/story_upi_pin.jpg.
  Idea source (VARIETY RULE 4): RBI public-awareness film "Scam through QR code scan" (RBI Kehta Hai) + common UPI-fraud explainers; facts from NPCI/bank safety guidance (PIN only to pay/check balance, never to receive) and MHA's National Cyber Crime Helpline 1930 / cybercrime.gov.in (checked today). No calc; ₹5,000 example only.
  Area A / format myth-vs-fact / hook myth statement / ending send-to-parents + quiz (log for rotation: next E credit score myth, quiz format).
  SHARE TEST: relatable 5 (every family uses UPI), not common knowledge 3 (young viewers know, parents often don't), surprising 3 (₹5,000 "aaye nahi, chale gaye"), send-to trigger 5 ("mummy-papa jo naye naye UPI chala rahe hain") = 16/20.
  Hooks: chosen "Paise lene ke liye UPI PIN daalna padta hai? Ye sabse bada jhooth hai!"; runners-up "₹5,000 lene gaye, ₹5,000 chale gaye?", "UPI ke 3 jhooth jo papa maante hain".
  QA: clipcheck 5/5 PASS; contact sheet: c1 turns into a laugh after ~2 s → used 0-2.0 s only; c2 papa gestures after ~3 s (fine, slot 3.25 s); c3/c4/c5 clean.
  Metricool (scheduled): YT 422713408 (16:00), FB Reel 422713432 (16:00), IG Reel 422713458 (18:00), IG Story 422713472 (18:10, auto).
  Alt title (Test & Compare, unscored, vidIQ 0): "UPI Fraud Se Kaise Bache? PIN Ka Sabse Bada Jhooth 🤯 #shorts".
  Credits: ElevenLabs ~0.57k (TTS only, atempo 1.4); Runway 155, left 735; vidIQ 0.
- Queue now: Tue 10 gehna (+ carousel 11:00), Wed 11 ₹15k → ₹1 crore, Thu 12 no cost EMI (IG cold-open test), Fri 13 do salary (VO-only test), Sat 14 dost ki car (+ carousel 11:00), Sun 15 UPI PIN myth → next run produces Mon 16 Nov (VARIETY: E credit score myth, 3-second quiz format). Thu 12: YT side of the lip-sync test; Sun 15: VO-only verdict. Sat 14 carousel exists; Tue 17 carousel = UPI safety checklist (to make on 12-13 Nov).

## 2026-11-11 (Wed)
**Checks:** Tue 10 Nov gehna posts all PUBLISHED: carousel 417316707 (DfjKX7WiAOb, 11:00), YT (C8SxMJY8tuk), FB (reel 1110582158447470), IG Reel (Dfj6V6tmes8), auto Story 417316693. No ERROR posts; no YouTube/Instagram/Metricool/Facebook/Runway/ElevenLabs/vidIQ mails (Gmail, 2 days). Today's ₹15k → ₹1 crore posts (YT 418519884 / FB 418519899 16:00, IG 418519913 18:00, Story 418519922) PENDING; queue to Sun 15 intact.
**Plans:** Runway 725 at start → 632 after today (3 stills 18 + 3 gen-4-turbo clips 75; 12 reused saree clips) → ~5-6 Shorts at this mix ≈ uploads to ~21-22 Nov; alerted 8 + 10 Nov, no new alert. ElevenLabs est. ~4.6k → ~4.0k (TTS 643) = ~6 VO-only Shorts; alerted 10 Nov, no new alert. vidIQ 0 (resets 24 Nov). Metricool upgraded.
**Numbers (Metricool):** YouTube subs 3 (no change since Oct). Daily views 1-7 Nov 15 / 21 / 89 / 32 / 7 / 45 / 28; 8-10 Nov not filled yet.
Instagram Reels lifetime: gehna (realistic, hook-only lip-sync + list, 10 Nov, <1 day) reach 96 / 115 views / avg 7.1 s / 42.3% past 3 s / 0 saves / 0 shares; ghar ₹97 lakh 105 / 53.1%; bonus A/B lip-sync test 100 / 15.2%; animated repost (8 Nov) 126 / 56.2%; Riya/Aman 100 / 33.3%; FD 148 / 39.5%; kharche 117 / 46.8%; lump sum 128 / 62.9%; credit card 99 / 42.6%.
**What it says:** (1) Reach is flat at ~100 per Reel for 9 Reels and saves/shares are 0 on all realistic Reels: nothing we post is being sent on, so the algorithm never widens the test. (2) Best realistic hold (ghar 53%) and best ever (animated lists 62-68%) both put the question + number on frame 1 AND give a reason to keep watching (numbered list). (3) YT subs flat at 3 for 3 weeks: viewers get no "series" reason to subscribe.
**Improvements applied:**
1. VARIETY RULE #2: area E (credit score myths), format = 3-SECOND QUIZ (new: on-screen "SAWAL #1/#2/#3" + 3-2-1 countdown, viewer answers HAAN/NAA in their head), hook type = question/challenge. Quiz = self-test viewers want to share ("check karo tumhara score kitna sahi").
2. Comment trigger is now a self-score ("kitne sahi? 0, 1, 2 ya 3"), easiest possible comment (one digit) → comments are what YT/IG need to widen distribution.
3. Send-to person is a fear, not a situation ("us dost ko jo darr ke maare kabhi score check nahi karta"), shown as a story character on screen (new friend character, task 16720bc7-4720-419c-8796-148ccde6a2b1).

**Produced today:** Mon 16 Nov Short "CIBIL Score Check Karne Se Girta Hai? 3 Sawal Quiz 😱 #shorts" → videos/credit_score_quiz_real.mp4 (38.2 s, realistic presenter (saree) + friend, 18 shots ~2.1 s, VOICE-OVER ONLY, atempo 1.45). Project assets/real/cs, overlays short3d "cs", story instagram/story_credit_score.jpg.
  Idea source (VARIETY RULE 4): common CIBIL/credit score myth explainers (Zee Business "Credit Score ko lekar 5 galatfahmiyan", bank/NBFC myth-buster pages); facts checked today: own score check = soft enquiry, no impact; many applications in a short time = hard enquiries; utilisation = balance / total limit. Our script.
  Area E / format 3-second quiz / hook question-challenge / ending self-score comment + send-to fearful friend (rotation next: B failed UPI/ATM refund rule, explainer).
  SHARE TEST: relatable 5 (everyone with a card/loan app sees "check your score"), not common knowledge 4 (most believe checking lowers it, and that closing a card helps), surprising 3 (25% → 50% utilisation, ~₹2,065 interest a month on minimum due), send-to trigger 5 ("jo darr ke maare score check nahi karta") = 17/20.
  Hooks: chosen "Apna CIBIL score check karne se score girta hai? 3 second mein socho!"; runners-up "Purana card band kiya, score gira?", "Minimum due bhara, phir bhi ₹2,000 byaaj?".
  Numbers (Python): 2 × ₹1,00,000 limit, ₹50,000 used = 25%; one closed → ₹50,000 / ₹1,00,000 = 50%; minimum due example: ₹50,000 × 3.5% = ₹1,750 + 18% GST ₹315 = ₹2,065 (rate = example, on screen).
  QA: clipcheck 3/3 PASS; contact sheet: c1 clean (small card on table with print → blurred), c2 clean, c3 friend laughs after ~2.5 s → used 0-1.8 s only. Overlay arrow "→" rendered as a box → replaced with "SE".
  Credits: ElevenLabs ~0.64k (TTS only); Runway 93, left 632; vidIQ 0.
  Metricool (scheduled): YT 423998502 (16:00), FB Reel 423998520 (16:00), IG Reel 423998560 (18:00), IG Story 423998575 (18:10, auto, story_credit_score.jpg).
  Alt title (Test & Compare, unscored, vidIQ 0): "Credit Score Ke 3 Myth: Aapke Kitne Sahi? 🤯 #shorts".
- Queue now: Wed 11 ₹15k → ₹1 crore, Thu 12 no cost EMI (IG cold-open test), Fri 13 do salary (VO-only test), Sat 14 dost ki car (+ carousel 11:00), Sun 15 UPI PIN myth, Mon 16 credit score quiz → next run produces Tue 17 Nov (VARIETY: B failed UPI/ATM refund rule, explainer) + Tue 17 carousel 11:00 (UPI safety checklist). Thu 12: YT side of the lip-sync test; Sun 15: VO-only verdict (Fri 13 IG hold).

## 2026-11-12 (Thu)
**Checks:** Wed 11 Nov ₹15k → ₹1 crore posts all PUBLISHED: YT (-vMgqVEqGfg), FB (reel 2387361401995036), IG Reel (DfmfPO7HwVp), auto Story 418519922. No ERROR posts; Gmail (2 days) has no YouTube/Instagram/Metricool/Facebook/Runway/ElevenLabs/vidIQ mails. Today's no cost EMI posts (YT 419660048 / FB 419660057 16:00, IG 419659868 18:00 cold-open, Story 419659876) PENDING; queue to Mon 16 intact.
**Plans:** Runway 632 at start → 514 after today (3 stills 18 + 4 gen-4-turbo clips 100; 13 reused saree clips) → ~4 Shorts at this mix ≈ production to ~16 Nov (uploads to ~21 Nov). ElevenLabs est. ~4.0k → ~3.4k (TTS 613) ≈ 5 VO-only Shorts → runs out around the 17 Nov run. Both inside 7 days, alerted 8 + 10 Nov, not topped up yet → one more push today with both links. vidIQ 0 (resets 24 Nov). Metricool upgraded.
**Numbers (Metricool):** YouTube subs 3 (flat). Daily views 1-8 Nov 15 / 21 / 89 / 32 / 7 / 45 / 28 / 16; 9-11 Nov not filled yet.
Instagram Reels lifetime: gehna (10 Nov, realistic, hook-only lip-sync + numbered list) now **reach 213 / 283 views / avg 9.9 s / 51.7% past 3 s / 1 save** = best realistic Reel on reach and first save; ₹15k → ₹1 crore (11 Nov, lip-sync hook, made 6 Nov before the VO-only switch, <1 day) reach 19 / avg 3.0 s / **15.8%**; ghar ₹97 lakh 105 / 53.1%; lip-sync test 100 / 15.2%; animated repost 126 / 56.2%; Riya/Aman 100 / 33.3%; FD 148 / 39.5%.
**What it says:** (1) Second Reel opening on a talking head at ~15% hold → confirms the 9 Nov verdict; every Short from 13 Nov is voice-over only (no more lip-sync openers in the queue after today's no cost EMI). (2) Gehna kept growing on day 2 (96 → 213 reach): a concrete everyday object + hidden cost + numbered list earns the first save; reach for realistic Reels can grow after day 1, so judge at 48 h. (3) YT subs still 3: no series reason to subscribe yet.
**Improvements applied:**
1. VARIETY RULE #3: area B (bank/RBI rules), format = "RULE YOUR BANK WON'T TELL YOU" explainer (NIYAM #1 / #2 on screen), hook type = shocking fact ("ATM se paisa nahi nikla, par kat gaya? Bank dega ₹100 roz!"), ending = send-to friend at the ATM + Haan/Naa comment.
2. Authority for saves: official source named in caption + description (RBI TAT circular, 20 Sep 2019) and the complaint path (bank → 30 days → cms.rbi.org.in) as a save-worthy action step.
3. Tue carousel = UPI safety checklist (7 niyam, family WhatsApp send-to) that also carries the failed-UPI refund rule, so the 11:00 carousel and 18:00 Reel feed each other on the same day.

**Produced today:** Tue 17 Nov Short "ATM Se Paisa Nahi Nikla? Bank Dega ₹100 Roz 😱 #shorts" → videos/atm_refund_rule_real.mp4 (34.0 s, realistic presenter (saree) + friend at ATM, 17 shots ~2.0 s, VOICE-OVER ONLY, atempo 1.45). Project assets/real/rf, overlays short3d "rf", story instagram/story_atm_refund.jpg, carousel instagram/carousel_upi (7 slides, DECKS "upi").
  Idea source (VARIETY RULE 4): popular "ATM se paisa nahi nikla / failed transaction refund" explainers; facts from RBI circular DPSS.CO.PD No.629/02.01.014/2019-20 (20 Sep 2019, TAT harmonisation): ATM cash not dispensed → auto-reversal T+5, ₹100/day after; UPI/IMPS debited but beneficiary not credited → T+1, ₹100/day after; RBI Integrated Ombudsman via CMS if the bank does not resolve in 30 days. Our script.
  Area B / format explainer / hook shocking fact / ending send-to + Haan/Naa (rotation next: D money-back policy real return, calculation format).
  SHARE TEST: relatable 5 (almost everyone has had a failed ATM/UPI debit), not common knowledge 4 (few know the ₹100/day compensation), surprising ₹ 4 (₹10,000 back on day 12 = ₹700), send-to 4 ("jiska paisa kabhi ATM mein atka tha") = 17/20.
  Hooks: chosen "ATM se paisa nahi nikla, par account se kat gaya? Bank aapko roz ₹100 dega!"; runners-up "Bank aapko ₹700 dene wala tha, aapko pata tha?", "UPI atka? Ye RBI niyam bank nahi batata".
  Numbers (Python check): delay = 12 − 5 = 7 days × ₹100 = ₹700. ₹10,000 and 12 days are examples (on screen).
  QA: clipcheck 4/4 PASS; contact sheet: c1 used from 0.6 s (already turning to camera), c1b from 0.9 s (points at ATM), c3 head-scratch 0-1.85 s + 1.15x punch-in from 2.9 s; no morphing.
  Metricool (scheduled): carousel 425251481 (11:00), YT 425251418 (16:00), FB Reel 425251434 (16:00), IG Reel 425251455 (18:00), IG Story 425251467 (18:10, auto).
  Alt title (Test & Compare, unscored, vidIQ 0): "Failed Transaction Refund: RBI Ka ₹100 Roz Niyam 🤯 #shorts".
  Credits: ElevenLabs ~0.61k (TTS only); Runway 118, left 514; vidIQ 0.
- Queue now: Thu 12 no cost EMI (IG cold-open test), Fri 13 do salary (VO-only), Sat 14 dost ki car (+ carousel), Sun 15 UPI PIN myth, Mon 16 credit score quiz, Tue 17 ATM/UPI refund rule (+ UPI carousel 11:00) → next run produces Wed 18 Nov (VARIETY: D money-back/endowment policy real return, calculation format). Sun 15: VO-only verdict (Fri 13 IG hold). Sat 21 carousel to make by 16 Nov.

## 2026-11-13 (Fri)
**Checks:** Thu 12 Nov no cost EMI posts all PUBLISHED: YT (J_TFw2EbWIo), FB (reel 1456141445963408), IG Reel cold-open variant (DfpD_NUknpa), auto Story 419659876. No ERROR posts; Gmail (2 days) has no YouTube/Instagram/Metricool/Facebook/Runway/ElevenLabs/vidIQ mails. Today's do salary posts (YT 420466553 / FB 420466573 16:00, IG 420466585 18:00, Story 420466593) PENDING; queue to Tue 17 intact.
**Plans:** Runway 514 at start → 321 after today (3 stills 18 + 7 gen-4-turbo clips 175; daily-wardrobe rule = no reused presenter clips) → ONE more Short at this cost; runs out at the 14-15 Nov production run. ElevenLabs est. ~3.4k → ~2.8k (TTS 561) ≈ 4-5 VO-only Shorts → out around 17-18 Nov. Both inside 7 days, alerted 8/10/12 Nov, still not topped up → push again today with both links. vidIQ 0 (resets 24 Nov). Metricool upgraded.
**Numbers (Metricool):** YouTube subs 3 (flat). Daily views 1-9 Nov 15 / 21 / 89 / 32 / 7 / 45 / 28 / 16 / 41; 10-12 Nov not filled yet.
Instagram Reels lifetime: no cost EMI (12 Nov, IG cold-open variant: 1.35 s reveal before a lip-sync hook, <1 day) reach 37 / 39 views / avg 2.7 s / **18.9% past 3 s**; ₹15k → ₹1 crore (11 Nov) 103 / 33.6% / 1 save (up from 15.8% at <1 day); gehna 214 / 285 views / 51.9% / 1 save; ghar 105 / 53.1%; lip-sync test 100 / 15.2%; animated repost 126 / 56.2%; Riya/Aman 100 / 33.3%; FD 148 / 39.5%; kharche 117 / 46.8%. Shares still 0 on every Reel.
**What it says:** (1) The cold-open trick did not rescue a Reel that still goes into a talking head (18.9% at <1 day); the fix is no lip-sync at all, which the whole queue from 13 Nov already follows. (2) Day-1 hold under-reads: ₹15k Reel went 15.8% → 33.6% by day 2, so verdicts on Fri 13 (VO-only) wait until Sun 15 (48 h). (3) Zero shares in 13 Reels: send-to must name a family member who would actually forward it (papa/mummy), which also suits the family-WhatsApp channel.
**Improvements applied:**
1. VARIETY RULE #4: area D (insurance), format = CALCULATION REVEAL (story: agent sells papa a "bachat wali" policy → IRR 4.3% → inflation-adjusted ₹5 lakh → cover ~₹10 lakh), hook type = too-good-to-be-true offer as a question ("₹10 lakh bharo, ₹16 lakh pao? fayda ya nuksaan?"), ending = 2-question save checklist + send to papa + Haan/Naa.
2. Daily wardrobe rule started: outfit #2 white shirt + navy blazer (portrait task e07d291f-0bee-4b8b-9975-ee13f5418894, used as face ref for all her stills). Reused only a papa clip (up_c3), no saree clips.
3. Responsible-finance line added on screen + caption ("chalti policy jaldi band mat karo, pehle surrender ka nuksaan samjho"): keeps the video educational (no "surrender your policy" call) and gives a save-worthy second takeaway.

**Produced today:** Wed 18 Nov Short "Money Back Policy Ka Sach: Return Sirf 4.3%? 😱 #shorts" → videos/policy_return_real.mp4 (33.5 s, realistic presenter (blazer) + papa + agent, 18 shots ~1.9 s, VOICE-OVER ONLY, atempo 1.45). Project assets/real/mb, overlays short3d "mb", story instagram/story_policy_return.jpg.
  Idea source (VARIETY RULE 4): popular "endowment / money-back policy real return" explainers in Indian personal finance (idea only; no insurer or plan named). Our script and numbers.
  Area D / format calculation reveal / hook too-good offer question / ending checklist + send-to papa + Haan/Naa (rotation next: G salary gone by the 20th, story format).
  SHARE TEST: relatable 5 (most families hold such a policy), not common knowledge 4 (people see ₹16 lakh vs ₹10 lakh, never the IRR), surprising ₹ 4 (₹16 lakh = ~₹5 lakh today, 4.3%), send-to 5 ("papa jinhone 'bachat wali' policy li hai") = 18/20.
  Hooks: chosen "Dus lakh bharo, solah lakh pao? Ye policy fayda hai ya nuksaan?"; runners-up "₹6 lakh ka fayda, ya 4.3% ka sach?", "Papa ki bachat wali policy ka asli return".
  Numbers (Python, numpy_financial): cash flows −₹50,000 at t=0..19, +₹16,00,000 at t=20 → IRR 4.288%; ₹16,00,000 / 1.06^20 = ₹4,98,888. Premium, maturity, cover ~₹10 lakh and 6% inflation are examples (on screen + caption).
  QA: clipcheck 6/7 PASS; c1 flagged single frames at 1.17 s and 4.50 s → hook uses 1.35-3.15 s, c1t uses 2.4-4.1 s (both outside). Contact sheet: no face/hand morphing; papers on table have unreadable fine print only.
  Metricool (scheduled): YT 426533433 (16:00), FB Reel 426533457 (16:00), IG Reel 426533474 (18:00), IG Story 426533486 (18:10, auto).
  Alt title (Test & Compare, unscored, vidIQ 0): "Bachat Wali Policy: ₹16 Lakh Ka Asli Sach 🤯 #shorts".
  Credits: ElevenLabs ~0.56k (TTS only); Runway 193, left 321; vidIQ 0.
- Queue now: Fri 13 do salary (VO-only), Sat 14 dost ki car (+ carousel 11:00), Sun 15 UPI PIN myth, Mon 16 credit score quiz, Tue 17 ATM/UPI refund (+ UPI carousel 11:00), Wed 18 money-back policy → next run produces Thu 19 Nov (VARIETY: G salary gone by the 20th, story format) + Sat 21 carousel (to make by 16 Nov). Sun 15: VO-only verdict (Fri 13 IG hold at 48 h). If Runway is not topped up by the next run, Thu 19 uses the cheapest mix (1 portrait + 3 clips, rest stills with push-in) to stay under ~120 credits.
