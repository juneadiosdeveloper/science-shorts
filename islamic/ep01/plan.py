import os
D = os.path.dirname(os.path.abspath(__file__))
R = D + "/../../fetched/"
KEYS = [f"f{i}" for i in range(1, 10)] + ["g_aisha", "g_fatima", "g_maryam", "g_giggle", "g_amazed", "g_mfatima", "g_mmaryam",
        "g_maisha", "g_wave", "e_sky", "e_soil", "e_clay", "e_spirit", "e_flame", "e_fireclay", "e_lights", "e_names", "e_gather"]
IMG = {k: R + f"is_{k}.png" for k in KEYS}
C = D + "/clips/"
CLIPS = {k: v for k, v in {3: (C + "lip03.mp4", "lipsync"), 31: (C + "lip31.mp4", "lipsync"),
                           10: (C + "soil.mp4", "anim"), 15: (C + "lights.mp4", "anim")}.items() if os.path.exists(v[0])}
SMALL = {}
GAP, LONG_GAP_AFTER, END_HOLD = 0.3, {5, 30}, 2.0
GAP_OVERRIDE = {3: 0.0, 31: 0.0}
DISCLAIMER = "Qur'an aur sahih hadith par aadharit. Characters AI se banaye gaye hain. Anbiya ki tasveer nahi dikhayi jaati."
CHIP_TEXT = ""
MUSIC = False
