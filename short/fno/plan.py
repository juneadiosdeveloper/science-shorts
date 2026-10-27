import os
R = os.path.dirname(os.path.abspath(__file__)) + "/../../fetched/"
IMG = {"s01": R+"fno_s01.png", "s02": R+"fno_s02.png", "s03": R+"fno_s03.png", "s05": R+"fno_s05.png",
       "s07": R+"fno_s07.png", "s08": R+"fno_s08.png", "s09": R+"sal_s07.png", "s11": R+"gm_s14.png"}
C = os.path.dirname(os.path.abspath(__file__)) + "/clips/"
# every line gets its own animated clip (gen-4-turbo, 5 s / 10 s) except line 10 (short Priya line, still + camera move)
CLIPS = {k: (C + f"c{k:02d}.mp4", "anim") for k in (1,2,3,4,5,6,7,8,9,11) if os.path.exists(C + f"c{k:02d}.mp4")}
if 4 in CLIPS: CLIPS[4] = (C + "c04.mp4", "anim", 1.9)   # skip the sparkle burst at the start of the dance clip
SMALL = {3: "Kahani kaalpanik hai; asli numbers SEBI study se",
         8: "Source: SEBI study, 23 Sep 2024 · individual F&O traders, FY22-FY24",
         10: "SEBI: avg loss ~₹2 lakh per trader, transaction cost milakar"}
GAP, LONG_GAP_AFTER, END_HOLD = 0.15, set(), 0.2
DISCLAIMER = "Educational only. Not financial advice. No buy/sell recommendation."
