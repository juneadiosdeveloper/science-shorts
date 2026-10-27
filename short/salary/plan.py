import os
R = os.path.dirname(os.path.abspath(__file__)) + "/../../fetched/"
IMG = {f"s{i:02d}": R + f"sal_s{i:02d}.png" for i in range(1, 9)}
C = os.path.dirname(os.path.abspath(__file__)) + "/clips/"
CLIPS = {k: v for k, v in {1: (C + "lip01.mp4", "lipsync")}.items() if os.path.exists(v[0])}
SMALL = {3: "Maana: SIP har saal +10% (salary ke saath)",
         4: "Maana: ₹15,000/mahina, 25 saal tak same",
         5: "Maana: 12% saalana, 25 saal, maasik SIP (guaranteed nahi)",
         6: "Dost ne kul ₹88.5 lakh lagaye, Chintu ne ₹45 lakh"}
GAP, LONG_GAP_AFTER, END_HOLD = 0.15, set(), 0.9
GAP_OVERRIDE = {1: 0.0}
DISCLAIMER = "Educational only. Not financial advice. Returns are assumptions."
