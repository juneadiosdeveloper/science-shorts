import os
R = os.path.dirname(os.path.abspath(__file__)) + "/../../fetched/"
IMG = {f"s{i:02d}": R + f"gm_s{i:02d}.png" for i in range(1, 16)}
C = os.path.dirname(os.path.abspath(__file__)) + "/clips/"
CLIPS = {k: v for k, v in {1: (C + "lip01.mp4", "lipsync")}.items() if os.path.exists(v[0])}
SMALL = {2: "Example: ₹1 lakh, 2 saal, '12% flat', EMI ₹5,167",
         3: "Flat: byaaj poore ₹1 lakh par · asli = reducing-balance rate",
         5: "Example: ₹30,000 ki 3 cheezein, 3 kisht har ek",
         7: "Example: kharcha ₹30,000/mahina × 6",
         9: "Example: ₹8,000/mahina bachat × 5 saal = ₹4.8 lakh",
         11: "₹2,000/mahina, 12% saalana maana (guaranteed nahi)",
         12: "Example. Pehle skill, phir SIP: dono zaroori"}
GAP, LONG_GAP_AFTER, END_HOLD = 0.18, set(), 1.2
GAP_OVERRIDE = {1: 0.0}
DISCLAIMER = "Educational only. Not financial advice. Numbers are examples."
