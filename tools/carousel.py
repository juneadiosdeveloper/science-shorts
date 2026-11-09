"""Paisa Science Instagram carousel (1080x1350, 4:5) + Story cards.
usage: python3 carousel.py <name> <outdir>      (slides from DECKS[name])
       python3 carousel.py story <bg.jpg|png> <out.jpg> "<line1>|<line2>"
Every slide: brand chip, big headline, body lines, slide counter, disclaimer. Last slide = save/share/follow.
"""
import os, sys
from PIL import Image, ImageDraw, ImageFilter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from paisa import F, GOLD, MINT, RED, WHITE, SOFT, INK, INK2

CW, CH = 1080, 1350

def grad(a, b, w, h):
    im = Image.new("RGB", (1, h))
    for y in range(h): im.putpixel((0, y), tuple(int(a[i] + (b[i] - a[i]) * y / h) for i in range(3)))
    return im.resize((w, h))

def fit_font(d, s, w, size, weight="Bold"):
    fo = F(weight, size)
    while d.textlength(s, font=fo) > w and fo.size > 26: fo = F(weight, fo.size - 4)
    return fo

def slide(head, body, k, n, head_col=GOLD, foot=None):
    im = grad(INK2, INK, CW, CH); d = ImageDraw.Draw(im)
    s = "PAISA SCIENCE"; fo = F("Bold", 34); tw = d.textlength(s, font=fo)
    d.rounded_rectangle((60, 60, 60 + tw + 50, 118), 29, fill=(0, 0, 0)); d.text((85, 66), s, font=fo, fill=GOLD)
    c = f"{k}/{n}"; fo = F("Bold", 34); d.text((CW - 60 - d.textlength(c, font=fo), 68), c, font=fo, fill=SOFT)
    y = 200
    for ln in head.split("\n"):
        fo = fit_font(d, ln, CW - 140, 104); d.text((70, y), ln, font=fo, fill=head_col, stroke_width=3, stroke_fill=(0, 0, 0)); y += fo.size + 24
    y += 30; d.line((70, y, 300, y), fill=GOLD, width=8); y += 50
    for ln, col in body:
        if ln == "": y += 30; continue
        fo = fit_font(d, ln, CW - 140, 58, "Bold" if col != SOFT else "Medium")
        d.text((70, y), ln, font=fo, fill=col); y += fo.size + 26
    if foot:
        fo = F("Bold", 44); tw = d.textlength(foot, font=fo)
        d.rounded_rectangle(((CW - tw) / 2 - 40, CH - 250, (CW + tw) / 2 + 40, CH - 170), 40, fill=GOLD)
        d.text(((CW - tw) / 2, CH - 240), foot, font=fo, fill=INK)
    s = "Sirf educational. Financial advice nahi."; fo = F("Medium", 30); d.text(((CW - d.textlength(s, font=fo)) / 2, CH - 90), s, font=fo, fill=SOFT)
    return im

DECKS = {
 # Tue 3 Nov 11:00, companion of the credit-card kamai Short (numbers verified 29 Oct, re-run 1 Nov)
 "cc": [
  ("Credit card\n'FREE' hai?", [("Phir bank har saal hazaaron", WHITE), ("kaise kamata hai?", WHITE), ("", None), ("3 chupi kamai, swipe karke dekho", MINT)], GOLD, "Swipe karo  >>"),
  ("#1 Swipe fee", [("Har swipe pe dukaandaar", WHITE), ("bank ko lagbhag 2% tak deta hai", WHITE), ("", None), ("Yeh kharcha aksar daamon mein", RED), ("jud jaata hai", RED), ("", None), ("Fee card aur dukaan ke hisaab se alag", SOFT)], GOLD, None),
  ("#2 Byaaj", [("Poora bill nahi bhara?", WHITE), ("~3.5% mahina = 42%+ saalana", RED), ("Compounding ke saath ~51%", RED), ("", None), ("3.5% sirf udaharan; asli rate", SOFT), ("aapke card par nirbhar", SOFT)], GOLD, None),
  ("₹1 lakh baaki,\n1 saal", [("Byaaj: ₹51,107", WHITE), ("+18% GST: ₹9,199", WHITE), ("= ₹60,306 se zyada!", RED), ("", None), ("Hisaab: 1,00,000 × (1.035^12 − 1)", SOFT), ("Maana: koi payment nahi. Late fee alag", SOFT)], RED, None),
  ("#3 'No cost' EMI", [("Byaaj zero dikh sakta hai, par", WHITE), ("+ processing fee", RED), ("+ us par 18% GST", RED), ("", None), ("EMI lene se pehle", MINT), ("TOTAL cost check karo", MINT)], GOLD, None),
  ("Seekh", [("1. Bill hamesha POORA bharo", MINT), ("2. Due date se pehle", MINT), ("3. EMI = total cost dekho", MINT), ("", None), ("Minimum due = byaaj ka jaal", RED)], GOLD, None),
  ("Save karo", [("Bhejo us dost ko jo", WHITE), ("har cheez card pe leta hai", GOLD), ("", None), ("Comment: aap bill kaise bharte ho?", WHITE), ("1) Poora  2) Minimum  3) Card nahi", SOFT)], MINT, "Follow @paisa_science"),
 ],
 # Sat 7 Nov 11:00, companion of the Riya vs Aman Short (numbers verified 2 Nov: ₹5,000 at start of month, 1%/month, until age 60)
 "late": [
  ("5 saal late =\n₹1.48 crore kam?", [("₹5,000 mahina, 60 ki umar tak", WHITE), ("Shuru kab kiya, bas itna farak", WHITE), ("", None), ("Apni umar dhoondo, swipe karo", MINT)], GOLD, "Swipe karo  >>"),
  ("Shuru @ 25", [("35 saal × ₹5,000 = ₹21 lakh lagaye", WHITE), ("60 pe: ~₹3.25 crore", MINT), ("", None), ("Maana: 12% saalana (1%/mahina)", SOFT), ("Guaranteed nahi, sirf udaharan", SOFT)], GOLD, None),
  ("Shuru @ 30", [("30 saal = ₹18 lakh lagaye", WHITE), ("60 pe: ~₹1.76 crore", GOLD), ("", None), ("Sirf 5 saal late:", WHITE), ("~₹1.48 crore kam!", RED)], GOLD, None),
  ("Shuru @ 35", [("25 saal = ₹15 lakh lagaye", WHITE), ("60 pe: ~₹95 lakh", GOLD), ("", None), ("25 wale se ~₹2.3 crore kam", RED)], GOLD, None),
  ("Shuru @ 40 / 45", [("40: ₹12 lakh lagaye = ~₹50 lakh", WHITE), ("45: ₹9 lakh lagaye = ~₹25 lakh", WHITE), ("", None), ("Har 5 saal ki deri:", WHITE), ("corpus lagbhag AADHA", RED)], RED, None),
  ("Twist", [("Ye sab 35 saal baad ke rupaye hain", WHITE), ("6% mehngai maano to ₹1.48 crore", WHITE), ("= aaj ke ~₹19 lakh", GOLD), ("", None), ("Aur ye farak sirf 25-30 ke", MINT), ("₹3 lakh ka kamaal hai", MINT)], GOLD, None),
  ("Save karo", [("Bhejo us dost ko jo kehta hai", WHITE), ("\"abhi toh umar hai\"", GOLD), ("", None), ("Comment: aapne kis umar mein", WHITE), ("shuru kiya? 25 / 30 / 35 / abhi nahi", SOFT)], MINT, "Follow @paisa_science"),
 ],
 # Tue 10 Nov 11:00, companion of the gehna (gold jewellery) Short (numbers verified 5 Nov: sona ₹5,00,000; bill = sona × (1+making) × 1.03)
 "gehna": [
  ("₹5 lakh ka sona,\nbill ₹5.92 lakh?", [("Gehne ke 2 chupe kharche", WHITE), ("jo bechte waqt wapas nahi milte", WHITE), ("", None), ("Apna making % dhoondo, swipe karo", MINT)], GOLD, "Swipe karo  >>"),
  ("#1 Making charge", [("Sone ki keemat ke upar % mein", WHITE), ("Aam taur pe ~8% se 25% tak", WHITE), ("Design jitna bareek, % utna zyada", WHITE), ("", None), ("Bechne par wapas nahi milta", RED)], GOLD, None),
  ("#2 GST 3%", [("Sone + making, dono par 3%", WHITE), ("₹5,75,000 × 3% = ₹17,250", WHITE), ("", None), ("Ye bhi wapas nahi milta", RED)], GOLD, None),
  ("Making % vs bill", [("Sona ₹5 lakh ka maano:", SOFT), ("8%: bill ₹5,56,200 (−₹56,200)", WHITE), ("15%: bill ₹5,92,250 (−₹92,250)", GOLD), ("25%: bill ₹6,43,750 (−₹1,43,750)", RED), ("", None), ("Barabari ke liye sona badhe:", WHITE), ("11.2% / 18.5% / 28.8%", MINT)], GOLD, None),
  ("Bechne jao to?", [("Aam taur pe sirf sone ki keemat", WHITE), ("(weight × purity × us din ka rate)", SOFT), ("", None), ("Kai dukaanein katauti bhi", RED), ("karti hain: pehle poochho", RED)], GOLD, None),
  ("Kharidne se pehle", [("1. Making charge kitna %?", MINT), ("2. Bill mein sona, making, GST", MINT), ("    alag-alag likha hai?", MINT), ("3. Wapas/exchange pe katauti?", MINT), ("4. Hallmark hai?", MINT)], GOLD, None),
  ("Save karo", [("Bhejo us dost ko", WHITE), ("jiski shaadi hone wali hai", GOLD), ("", None), ("Comment: ghar mein gehna", WHITE), ("1) Nivesh  2) Shauk  3) Dono", SOFT)], MINT, "Follow @paisa_science"),
 ],
 # Sat 14 Nov 11:00, companion of the "dost ki car" Short (numbers verified 9 Nov: ₹12L car, ₹2L down, ₹10L loan 9% 5 yr, EMI ₹20,758; value -20% yr1, -15%/yr after)
 "car": [
  ("₹12 lakh ki car,\nasli daulat ₹1.6 lakh?", [("Dost ki nayi car ka", WHITE), ("2 saal baad ka hisaab", WHITE), ("", None), ("Swipe karo, khud check karo", MINT)], GOLD, "Swipe karo  >>"),
  ("Udaharan", [("Car ₹12,00,000", WHITE), ("Down payment ₹2,00,000", WHITE), ("Loan ₹10,00,000, 9%, 5 saal", WHITE), ("EMI ₹20,758 har mahina", GOLD), ("", None), ("Sab numbers sirf udaharan", SOFT)], GOLD, None),
  ("Car ki keemat", [("Naye din: ₹12.00 lakh", WHITE), ("1 saal baad (−20%): ₹9.60 lakh", WHITE), ("2 saal (−15%): ₹8.16 lakh", GOLD), ("3 saal: ₹6.94 lakh", WHITE), ("5 saal: ₹5.01 lakh", RED), ("", None), ("Asli girawat model/shehar pe nirbhar", SOFT)], GOLD, None),
  ("2 saal baad", [("Diye: ₹2L + ₹20,758 × 24", WHITE), ("= ₹6,98,200", RED), ("Loan baaki: ₹6,52,784", RED), ("Car ki keemat: ₹8,16,000", WHITE), ("", None), ("Car mein asli hissa: ₹1,63,216", GOLD)], GOLD, None),
  ("Poore 5 saal", [("Kul diye: ₹14,45,501", WHITE), ("Sirf byaaj: ₹2,45,501", RED), ("Car ki keemat: ~₹5.01 lakh", WHITE), ("", None), ("Car zaroorat hai? Theek.", MINT), ("Bas dikhawe ke liye nahi.", MINT)], GOLD, None),
  ("Car lene se pehle", [("1. EMI salary ka kitna %?", MINT), ("2. Down payment zyada, loan kam", MINT), ("3. Tenure chhota = byaaj kam", MINT), ("4. Insurance + petrol + service", MINT), ("    bhi budget mein jodo", MINT)], GOLD, None),
  ("Save karo", [("Bhejo us dost ko", WHITE), ("jo sochta hai sab usse ameer hain", GOLD), ("", None), ("Comment: aap", WHITE), ("1) Car wale  2) Bachat wale", SOFT)], MINT, "Follow @paisa_science"),
 ],
}

def story(bg, out, lines):
    W, H = 1080, 1920
    im = Image.open(bg).convert("RGB"); s = max(W / im.width, H / im.height)
    im = im.resize((round(im.width * s), round(im.height * s))); x = (im.width - W) // 2; y = (im.height - H) // 2
    im = im.crop((x, y, x + W, y + H))
    sh = Image.new("L", (1, H))
    for yy in range(H): sh.putpixel((0, yy), int(max(0, (700 - yy) / 700) * 170 + max(0, (yy - 1300) / 620) * 220))
    im = Image.composite(Image.new("RGB", (W, H)), im, sh.resize((W, H))); d = ImageDraw.Draw(im)
    s = "PAISA SCIENCE"; fo = F("Bold", 40); tw = d.textlength(s, font=fo)
    d.rounded_rectangle((40, 190, 40 + tw + 50, 252), 31, fill=(20, 15, 10)); d.text((65, 196), s, font=fo, fill=GOLD)
    a, b = lines.split("|"); y = 360
    for t, col in ((a, WHITE), (b, GOLD)):
        fo = fit_font(d, t, W - 100, 110); tw = d.textlength(t, font=fo)
        d.text(((W - tw) / 2, y), t, font=fo, fill=col, stroke_width=6, stroke_fill=(15, 10, 10)); y += fo.size + 60
    for t, col, sz in (("Full video: YouTube", WHITE, 64), ("Paisa Science", GOLD, 84), ("(link bio mein)", WHITE, 56)):
        fo = F("Bold", sz); tw = d.textlength(t, font=fo); d.text(((W - tw) / 2, {64: 1500, 84: 1585, 56: 1700}[sz]), t, font=fo, fill=col, stroke_width=4, stroke_fill=(0, 0, 0))
    im.save(out, quality=90)

if __name__ == "__main__":
    if sys.argv[1] == "story":
        story(sys.argv[2], sys.argv[3], sys.argv[4])
    else:
        deck = DECKS[sys.argv[1]]; os.makedirs(sys.argv[2], exist_ok=True)
        for i, (h, b, col, foot) in enumerate(deck, 1):
            slide(h, b, i, len(deck), col, foot).save(f"{sys.argv[2]}/{sys.argv[1]}_{i}.jpg", quality=92)
