import os
R = os.path.dirname(os.path.abspath(__file__)) + "/../../fetched/"
IMG = {f"s{k:02d}": R + f"hlm_s{k:02d}.png" for k in range(1, 9)}
C = os.path.dirname(os.path.abspath(__file__)) + "/clips/"
def c(n): return (C + f"c{n}.mp4", "anim")
# c06a is played reversed (the model shrank the red stack; reversed it grows, matching "byaaj aur badha").
# every shot is a moving 5 s gen-4-turbo clip; lines 6 and 7 are longer than 5 s, so two clips each (hard cut mid-line)
CLIPS = {1: c("01"), 2: c("02"), 3: c("03"), 4: c("04"), 5: c("05"), 6: [(C + "c06a_rev.mp4", "anim", 1.6), c("06b")], 7: [c("07a"), c("07b")], 8: c("08")}
CLIPS = {k: v for k, v in CLIPS.items() if all(os.path.exists(x[0]) for x in (v if isinstance(v, list) else [v]))}
SMALL = {3: "₹50 lakh, 8.5% maana: 20 saal byaaj ₹54.1L vs 30 saal ₹88.4L",
         5: "Rate 8.5% se 9.5% (1 saal baad), EMI wahi ₹43,391",
         6: "EMI ₹46,498 karte, tenure 20 saal: byaaj ₹61.2L vs ₹78.7L",
         7: "₹50,000 loan mein, 8.5% par 20 saal EMI se chukaya"}
GAP, LONG_GAP_AFTER, END_HOLD = 0.15, set(), 0.2
GAP_OVERRIDE = {4: 0.08}
DISCLAIMER = "Educational only. Not financial advice. Rates are examples."
