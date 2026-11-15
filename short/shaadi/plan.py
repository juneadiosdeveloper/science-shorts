import os
R = os.path.dirname(os.path.abspath(__file__)) + "/../../fetched/"
IMG = {"s01": R+"sh_s01.png", "s02": R+"sh_s02.png", "s03": R+"hlm_s06.png", "s04": R+"hlm_s07.png", "s05": R+"fno_s07.png",
       "s06": R+"hlm_s08.png", "s07": R+"gm_s12.png", "s08": R+"hlm_s03.png", "s09": R+"sal_s08.png"}
CLIPS = {1: (R+"sh_c01.mp4", "anim"), 2: (R+"sh_c02.mp4", "anim"), 3: (R+"hlm_c06b.mp4", "anim"), 4: (R+"hlm_c07a.mp4", "anim"),
         5: (R+"fno_c07.mp4", "anim"), 6: (R+"hlm_c08.mp4", "anim"), 7: (R+"sh_c07.mp4", "anim"), 8: (R+"hlm_c03.mp4", "anim"), 9: (R+"sh_c09.mp4", "anim")}
SMALL = {1: "Sab numbers udaharan · 8% sirf maana, guaranteed nahi",
         3: "Personal loan 14% saalana, 60 EMI (udaharan)",
         4: "Kul chukaya ₹13.96L = ₹10L + ₹3.96L byaaj",
         5: "₹10L savings + ₹13.96L loan = ~₹24L",
         7: "₹20L x (1.08)^10 = ₹43.2L · 8% maana, mehngai alag"}
GAP, LONG_GAP_AFTER, END_HOLD = 0.12, set(), 0.1
DISCLAIMER = "Educational only. Not financial advice. Rates are examples."
