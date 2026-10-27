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
