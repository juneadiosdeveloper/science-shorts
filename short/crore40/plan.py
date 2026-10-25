import os
R = os.path.dirname(os.path.abspath(__file__)) + "/../../fetched/"
IMG = {f"s{i:02d}": R + f"cr_s{i:02d}.png" for i in range(1, 12)}
IMG["s12"] = R + "gm_s15.png"
C = os.path.dirname(os.path.abspath(__file__)) + "/clips/"
CLIPS = {k: v for k, v in {1: (C + "lip01.mp4", "lipsync")}.items() if os.path.exists(v[0])}
SMALL = {3: "Maana: ₹2,000/mahina, 12% saalana, umar 22 → 60 (guaranteed nahi)",
         5: "Maana: SIP har saal +10%, 12% saalana",
         7: "Maana: ₹5,000 se shuru, +15%/saal, 14% saalana (bahut optimistic)",
         9: "Maana: 6% saalana mehngai · ₹43 cr ÷ 9.15",
         11: "Sirf educational. Returns market par nirbhar, guaranteed nahi"}
GAP, LONG_GAP_AFTER, END_HOLD = 0.18, set(), 1.2
GAP_OVERRIDE = {1: 0.0}
DISCLAIMER = "Educational only. Not financial advice. Returns are assumptions."
