import os
R = os.path.dirname(os.path.abspath(__file__)) + "/../../fetched/"
IMG = {f"s{i:02d}": R + f"hl_s{i:02d}.png" for i in range(1, 45)}
C = os.path.dirname(os.path.abspath(__file__)) + "/clips/"
CLIPS = {k: v for k, v in {
    1: (C + "c01.mp4", "anim"), 2: (C + "lip02.mp4", "lipsync"), 7: (C + "c07.mp4", "anim"),
    19: (C + "c19.mp4", "anim"), 25: (C + "c25.mp4", "anim"), 42: (C + "lip42.mp4", "lipsync")}.items() if os.path.exists(v[0])}
SMALL = {4: "Example: ₹50 lakh · 8.5% saalana · 20 saal (8.5% sirf example hai)",
         7: "EMI ₹43,391 me se ₹35,417 byaaj (pehla mahina)",
         16: "Maana gaya: ₹50 lakh, 8.5%, 20 saal",
         25: "Maana gaya: 8.5% byaaj, EMI har saal +5%",
         26: "Approx. Asli bachat aapke loan ke rate aur rules par nirbhar",
         29: "Maana gaya: ₹50 lakh, 8.5%, 20 saal",
         30: "Apne bank ke prepayment rules zaroor check karein"}
GAP, LONG_GAP_AFTER, END_HOLD = 0.25, {5, 13, 22, 31}, 7.0
GAP_OVERRIDE = {2: 0.0, 42: 0.0}
DISCLAIMER = "Educational purpose only. Not financial advice. Invest after your own research."
