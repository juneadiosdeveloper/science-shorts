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
