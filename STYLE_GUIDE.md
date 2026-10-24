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
