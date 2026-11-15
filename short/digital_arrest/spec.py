# Sun 22 Nov 2026 (planned) - Category: Scams & safety (GROWTH PLAN idea #7). FIRST synced motion-graphics Short (HyperFrames),
# owner 15 Nov: "voice and animation not matching". Facts: I4C/MHA advisory (May 2024): CBI, ED, police etc. do not arrest anyone over
# video calls; "digital arrest" has no legal basis (PIB / PM Mann Ki Baat, 27 Oct 2024). MHA/I4C: ~₹120.3 crore lost to digital-arrest
# frauds Jan-Apr 2024. Help: 1930 / cybercrime.gov.in. Lines 6-9 wait for Runway credits (voice).
import os
R = os.path.dirname(os.path.abspath(__file__)) + "/../../fetched/"
TOPIC = "SCAM ALERT"
DISCLAIMER = "Educational only. Source: I4C / MHA advisories."
GAP, END_HOLD = 0.12, 0.3
LINES = [
 dict(id=1, wav="audio/l01.wav", cap="Police video call par \"digital arrest\" kare... aur paise maange?",
      items=[("call", "\"POLICE OFFICER\"", 0), ("head", "DIGITAL ARREST?", "red", 0), ("sub", "PAISE MAANGE = SCAM?", "gold", 8)]),
 dict(id=2, wav="audio/l02.wav", cap="Mere naam par drugs ka parcel?! Mujhe arrest mat karo!",
      items=[("char", R + "sal_s07.png", "shake"), ("head", "DRUGS PARCEL?!", "red", 3), ("sub", "MUJHE ARREST MAT KARO!", "white", 6)]),
 dict(id=3, wav="audio/l03.wav", cap="Sirf chaar mahino mein, logon ne aise ek sau bees crore rupaye ganwaye.",
      items=[("head", "SIRF 4 MAHINE MEIN", "gold", 0), ("counter", "₹", 0, 120, " CRORE", 7, 10), ("sub", "GAYAB!", "red", 12),
             ("chip", "I4C / MHA: digital arrest fraud, Jan-Apr 2024", 0)]),
 dict(id=4, wav="audio/l04.wav", cap="Sach ye hai: kanoon mein digital arrest jaisa kuch hai hi nahi.",
      items=[("call", "\"POLICE OFFICER\"", 0), ("head", "KANOON MEIN", "white", 3), ("sub", "'DIGITAL ARREST' NAHI HOTA", "teal", 5),
             ("stamp", "FAKE!", "red", 11)]),
 dict(id=5, wav="audio/l05.wav", cap="CBI, police ya ED, kabhi video call par arrest nahi karte, aur na paise maangte hain.",
      items=[("badges", ["CBI", "POLICE", "ED"], [0, 1, 3]), ("head", "VIDEO CALL PE ARREST: NAHI", "teal", 4),
             ("sub", "PAISE BHI NAHI MAANGTE", "gold", 12)]),
]
