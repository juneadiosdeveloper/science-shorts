import os
R = os.path.dirname(os.path.abspath(__file__)) + "/../../fetched/"
# reused library stills (our own Chintu/Priya assets); only new Runway asset = hook clip tx_c1 (gen-4-turbo from sal_s07)
IMG = {"s01": R+"sal_s07.png", "s02": R+"sal_s02.png", "s03": R+"gm_s03.png", "s04": R+"gm_s13.png", "s05": R+"hlm_s05.png",
       "s06": R+"hlm_s07.png", "s07": R+"gm_s01.png", "s08": R+"hlm_s03.png", "s09": R+"hlm_s08.png", "s10": R+"sal_s08.png"}
CLIPS = {1: (R+"tx_c1.mp4", "anim"), 3: (R+"hlm_c05.mp4", "anim")}
CLIPS = {k: v for k, v in CLIPS.items() if all(os.path.exists(x[0]) for x in (v if isinstance(v, list) else [v]))}
SMALL = {1: "New regime, tax year 2026-27, salaried, sirf standard deduction maana",
         3: "₹13L − ₹75,000 = ₹12.25L · marginal relief: tax max ₹25,000 + 4% cess",
         4: "₹13,00,000 − ₹26,000 = ₹12,74,000 vs ₹12,75,000",
         8: "Har case alag: NPS, allowances, doosri income se badal sakta hai"}
GAP, LONG_GAP_AFTER, END_HOLD = 0.1, set(), 0.1
GAP_OVERRIDE = {3: 0.05}
DISCLAIMER = "Educational only. Not tax advice. Check your own case."
