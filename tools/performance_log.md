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
