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
