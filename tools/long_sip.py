"""Paisa Science long video #1: SIP ki poori guide (16:9, 1920x1080).
python3 long_sip.py voice            -> synthesise narration, write timing json
python3 long_sip.py stills out.png   -> preview frames
python3 long_sip.py render out.mp4   -> full video (parallel by chapter)
"""
import json, math, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__))
W, H, FPS = 1920, 1080, 30
FD = "/usr/share/fonts/truetype/google-fonts/"
_fc = {}
def F(w, s):
    if (w, s) not in _fc: _fc[(w, s)] = ImageFont.truetype(FD + f"Poppins-{w}.ttf", s)
    return _fc[(w, s)]
INK, INK2 = (8, 34, 29), (16, 60, 50)
GOLD, GOLD_D, MINT, RED, GREY, WHITE, SOFT = (255, 205, 70), (190, 140, 20), (70, 220, 140), (255, 95, 85), (165, 180, 190), (255, 255, 255), (205, 222, 215)
BLUE = (110, 170, 255)
def clamp(x, a=0, b=1): return max(a, min(b, x))
def ease(x): x = clamp(x); return 1 - (1 - x) ** 3
def lerp(a, b, t): return a + (b - a) * t
def _grad(a, b):
    im = Image.new("RGB", (1, H))
    for y in range(H): im.putpixel((0, y), tuple(int(a[i] + (b[i] - a[i]) * y / H) for i in range(3)))
    return im.resize((W, H)).convert("RGBA")
BG = _grad(INK2, INK)

def ov(img, fn):
    o = Image.new("RGBA", img.size, (0, 0, 0, 0)); fn(ImageDraw.Draw(o)); img.alpha_composite(o)
def T(img, s, x, y, size, col, a=1.0, w="Bold", anchor="la"):
    if a <= 0: return
    ov(img, lambda d: d.text((x, y), s, font=F(w, size), fill=col + (int(255 * clamp(a)),), anchor=anchor))
def frame_chrome(img, chap_no, chap_title):
    def f(d):
        d.rounded_rectangle((60, 44, 60 + d.textlength("PAISA SCIENCE", font=F("Bold", 30)) + 48, 96), 26, fill=(0, 0, 0, 140))
        d.text((84, 52), "PAISA SCIENCE", font=F("Bold", 30), fill=GOLD + (255,))
        if chap_no is not None:
            s = f"{chap_no}. {chap_title}"; d.text((W - 60, 56), s, font=F("Medium", 30), fill=SOFT + (220,), anchor="ra")
        s = "Sirf educational. Investment advice nahi. Returns guaranteed nahi."
        d.text((W / 2, H - 46), s, font=F("Medium", 26), fill=SOFT + (170,), anchor="ma")
    ov(img, f)
def coin(d, cx, cy, r, a=255):
    d.ellipse((cx - r, cy - r * .62, cx + r, cy + r * .62), fill=GOLD + (a,), outline=GOLD_D + (a,), width=5)
    d.text((cx, cy), "₹", font=F("Bold", int(r * .8)), fill=(120, 80, 0, a), anchor="mm")
def lakh(v):
    return f"₹{v/1e7:.2f} cr" if v >= 1e7 else f"₹{v/1e5:.1f} lakh" if v >= 1e5 else f"₹{v:,.0f}"
def rev(k, i, lp=1.0, d=.6):
    """reveal amount for an element that appears on line i (k = current line, lp = seconds into it)"""
    return 1.0 if k > i else ease(lp / d) if k == i else 0.0

# ---------------- finance helpers (numbers verified in the session) ----------------
def fv(p, r, n, step=0.0):
    i = r / 12; v = 0; m = p; out = [0]
    for k in range(n):
        if k and k % 12 == 0: m *= 1 + step
        v = (v + m) * (1 + i); out.append(v)
    return out
def invested(p, n, step=0.0):
    t = 0; m = p; out = [0]
    for k in range(n):
        if k and k % 12 == 0: m *= 1 + step
        t += m; out.append(t)
    return out

def chart(img, L, R, Tp, B, ymax, yticks, xticks, series, prog, xlab=None):
    """series: list of (values list, colour, label, label_pos)"""
    def f(d):
        fo = F("Medium", 28)
        for v, s in yticks:
            y = B - (B - Tp) * v / ymax; d.line((L, y, R, y), fill=(255, 255, 255, 28), width=2)
            d.text((L - 18, y), s, font=fo, fill=SOFT + (255,), anchor="rm")
        for x, s in xticks:
            d.text((L + (R - L) * x, B + 16), s, font=fo, fill=SOFT + (255,), anchor="ma")
        if xlab: d.text(((L + R) / 2, B + 58), xlab, font=fo, fill=SOFT + (200,), anchor="ma")
        for vals, col, lab, lp, p in series:
            n = len(vals) - 1; N = max(1, int(n * p))
            pts = [(L + (R - L) * j / n, B - (B - Tp) * vals[j] / ymax) for j in range(0, N + 1, max(1, n // 300))]
            if len(pts) > 1: d.line(pts, fill=col + (255,), width=9, joint="curve")
            x, y = pts[-1]; d.ellipse((x - 11, y - 11, x + 11, y + 11), fill=col + (255,))
            if lab and p >= .999: d.text(lp, lab, font=F("Bold", 40), fill=col + (255,), anchor="rm")
    ov(img, f)

# ============================ CHAPTERS ============================
def ch_hook(img, k, lp, t):
    def f(d):
        for i in range(9):
            y = lerp(-80, 760 - i * 46, ease((t - i * .1) / .7)); coin(d, 1500 + (i % 2) * 14, y, 92)
    ov(img, f)
    T(img, "₹10,000 × 240 mahine", 120, 300, 72, WHITE, ease(t / .5))
    T(img, "= ₹1 CRORE?", 120, 400, 150, GOLD, ease((t - .4) / .5))
    items = ["SIP kya hai", "Rupee cost averaging", "Compounding", "SIP vs RD", "Waqt ki taakat", "Step-up SIP", "Shuru kaise karein", "5 badi galtiyan"]
    for i, s in enumerate(items):
        a = rev(k, 3, lp + .15 * (-i), .5)
        T(img, f"{i+1}. {s}", 130 + (i // 4) * 560, 620 + (i % 4) * 66, 38, SOFT if i % 2 else WHITE, a, "Medium")

def ch_what(img, k, lp, t):
    boxes = [("Har mahine", "₹ tay rakam", GOLD, 1), ("Mutual fund", "shares + bonds ki tokri", MINT, 3), ("Units milti hain", "NAV ke bhaav par", BLUE, 4)]
    def f(d):
        for i, (a1, a2, col, line) in enumerate(boxes):
            a = rev(k, line, lp)
            if a <= 0: continue
            x = 160 + i * 560; y = 330
            d.rounded_rectangle((x, y, x + 440, y + 300), 30, fill=(4, 14, 12, int(200 * a)), outline=col + (int(255 * a),), width=5)
            d.text((x + 220, y + 105), a1, font=F("Bold", 50), fill=col + (int(255 * a),), anchor="mm")
            d.text((x + 220, y + 190), a2, font=F("Medium", 34), fill=WHITE + (int(255 * a),), anchor="mm")
            if i and a > .5:
                d.line((x - 110, y + 150, x - 18, y + 150), fill=SOFT + (int(255 * a),), width=6)
                d.polygon([(x - 18, y + 136), (x - 18, y + 164), (x, y + 150)], fill=SOFT + (int(255 * a),))
        a = rev(k, 1, lp)
        if a: d.text((W / 2, 210), "SIP = Systematic Investment Plan", font=F("Bold", 60), fill=WHITE + (int(255 * a),), anchor="ma")
        a = rev(k, 5, lp)
        if a: d.text((W / 2, 720), "NAV = ek unit ki us din ki keemat (Net Asset Value)", font=F("Medium", 40), fill=SOFT + (int(255 * a),), anchor="ma")
        a = rev(k, 6, lp)
        if a: d.text((W / 2, 820), "Market ka time pakadne ki zaroorat nahi. Aadat kaam karti hai.", font=F("Bold", 44), fill=GOLD + (int(255 * a),), anchor="ma")
    ov(img, f)

def ch_rca(img, k, lp, t):
    navs = [10, 8, 12.5, 10]
    T(img, "Har mahine ₹1,000", 120, 160, 56, WHITE, rev(k, 1, lp))
    def f(d):
        base = 760
        for i, nv in enumerate(navs):
            a = rev(k, 2 + i, lp)
            if a <= 0: continue
            x = 160 + i * 300; h = nv / 12.5 * 380 * ease(a * 1.3)
            d.rounded_rectangle((x, base - h, x + 180, base), 16, fill=(BLUE if nv != 8 else MINT) + (int(255 * a),))
            d.text((x + 90, base - h - 52), f"NAV ₹{nv:g}", font=F("Bold", 36), fill=WHITE + (int(255 * a),), anchor="ma")
            d.text((x + 90, base + 18), f"Mahina {i+1}", font=F("Medium", 30), fill=SOFT + (int(255 * a),), anchor="ma")
            d.text((x + 90, base + 62), f"{1000/nv:g} units", font=F("Bold", 38), fill=GOLD + (int(255 * a),), anchor="ma")
        a = rev(k, 6, lp)
        if a:
            d.rounded_rectangle((1380, 300, 1820, 760), 30, fill=(4, 14, 12, int(210 * a)))
            for j, (lab, val, col) in enumerate([("Lagaye", "₹4,000", WHITE), ("Units", "405", GOLD), ("Aapki avg keemat", "₹9.88", MINT), ("NAV ka avg", "₹10.13", GREY)]):
                aa = a if j < 2 else rev(k, 7, lp)
                d.text((1420, 330 + j * 105), lab, font=F("Medium", 32), fill=SOFT + (int(255 * aa),))
                d.text((1780, 370 + j * 105), val, font=F("Bold", 44), fill=col + (int(255 * aa),), anchor="ra")
    ov(img, f)
    T(img, "Girawat = zyada units = SALE!", W / 2, 900, 52, MINT, rev(k, 8, lp), anchor="ma")
    T(img, "Nuksaan se bachne ki guarantee nahi", W / 2, 972, 36, SOFT, rev(k, 9, lp), "Medium", anchor="ma")

SIP12, INV = fv(1e4, .12, 240), invested(1e4, 240)
def ch_comp(img, k, lp, t):
    T(img, "₹10,000 / mahina • 20 saal • 12% saalana (maan kar)", 120, 150, 44, WHITE, rev(k, 2, lp), "Medium")
    if k < 8:
        p_inv = rev(k, 3, lp, 2.5); p_val = rev(k, 4, lp, 4.0)
        chart(img, 260, 1340, 260, 900, 1e7, [(v * 1e6 * 2.5, f"{int(v*25)}L") for v in range(5)] + [(1e7, "1 cr")],
              [(y / 20, str(y)) for y in (0, 5, 10, 15, 20)],
              [(INV, GREY, "₹24 lakh", (1330, 820), p_inv), (SIP12, MINT, "₹99.9 lakh*", (1300, 250), p_val)], 1, "saal")
        T(img, "Aapka paisa", 1400, 720, 38, GREY, rev(k, 3, lp))
        T(img, "Value", 1400, 280, 38, MINT, rev(k, 4, lp))
        T(img, "Kamaai ~₹76 lakh", 1400, 420, 44, GOLD, rev(k, 5, lp))
    else:
        def f(d):
            for i, (r, v) in enumerate([("8%", 59.3e5), ("10%", 76.6e5), ("12%", 99.9e5)]):
                a = rev(k, 8, lp - i * .3); y = 320 + i * 190
                d.text((180, y + 40), r, font=F("Bold", 64), fill=GOLD + (int(255 * a),))
                d.rounded_rectangle((420, y, 420 + 1200 * v / 1e7 * a, y + 130), 24, fill=MINT + (int(255 * a),))
                if a > .9: d.text((450, y + 65), lakh(v), font=F("Bold", 56), fill=INK + (255,), anchor="lm")
        ov(img, f)
        T(img, "Return kabhi pakka nahi hota", W / 2, 900, 52, RED, rev(k, 9, lp), anchor="ma")


def ch_rd(img, k, lp, t):
    T(img, "₹10,000 / mahina • 20 saal", 120, 150, 52, WHITE, rev(k, 1, lp))
    def f(d):
        rows = [("RD (7% maan kar)", 52.4e5, BLUE, 2), ("SIP (12% maan kar)", 99.9e5, MINT, 3)]
        for j, (lab, v, col, line) in enumerate(rows):
            a = rev(k, line, lp, 1.0); y = 330 + j * 220
            d.text((140, y - 56), lab, font=F("Bold", 42), fill=col + (int(255 * a),))
            d.rounded_rectangle((140, y, 140 + 1300 * v / 1e7 * a, y + 130), 24, fill=col + (int(255 * a),))
            if a > .9: d.text((170, y + 65), lakh(v), font=F("Bold", 56), fill=INK + (255,), anchor="lm")
        rows2 = [("RD", "Fixed byaaj, kam risk", BLUE), ("SIP (equity fund)", "Market se juda, upar-neeche", MINT)]
        for j, (a1, a2, col) in enumerate(rows2):
            a = rev(k, 4 + j, lp); y = 800 + j * 70
            d.text((140, y), a1, font=F("Bold", 40), fill=col + (int(255 * a),))
            d.text((620, y), a2, font=F("Medium", 40), fill=WHITE + (int(255 * a),))
    ov(img, f)
    T(img, "Lakshya + samay + risk dekh kar chuno", 1840, 960, 40, GOLD, rev(k, 6, lp), anchor="ra")

def ch_start(img, k, lp, t):
    steps = [(1, "PAN + KYC poora karo"), (2, "Lakshya aur samay tay karo"), (3, "Goal ke hisaab se fund type"), (4, "Salary ke baad ki tareekh chuno"), (5, "Auto-debit lagao, bhool jao"), (6, "Saal mein ek baar review karo")]
    for i, (line, s) in enumerate(steps):
        x = 140 + (i % 2) * 860; y = 220 + (i // 2) * 200; a = rev(k, line, lp)
        if a <= 0: continue
        def f(d, x=x, y=y, a=a, i=i, s=s):
            d.rounded_rectangle((x, y, x + 780, y + 150), 28, fill=(4, 14, 12, int(200 * a)), outline=MINT + (int(200 * a),), width=3)
            d.ellipse((x + 30, y + 40, x + 100, y + 110), fill=GOLD + (int(255 * a),))
            d.text((x + 65, y + 75), str(i + 1), font=F("Bold", 40), fill=INK + (int(255 * a),), anchor="mm")
            d.text((x + 130, y + 75), s, font=F("Bold", 38), fill=WHITE + (int(255 * a),), anchor="lm")
        ov(img, f)
    T(img, "Hum kisi fund ka naam nahi lete: yeh aapka faisla hai", W / 2, 900, 38, SOFT, rev(k, 7, lp), "Medium", anchor="ma")

AMIT, RAVI = fv(1e4, .12, 420), [0] * 120 + fv(1e4, .12, 300)
def ch_time(img, k, lp, t):
    T(img, "Dono: ₹10,000 / mahina, 60 saal ki umar tak, 12% maan kar", 120, 150, 40, WHITE, rev(k, 1, lp), "Medium")
    chart(img, 260, 1420, 260, 860, 7e7, [(v * 1e7, f"{v} cr") for v in range(0, 8)],
          [((a - 25) / 35, str(a)) for a in (25, 35, 45, 55, 60)],
          [(AMIT, MINT, "₹6.50 cr", (1395, 262), rev(k, 5, lp, 3.5) if k >= 5 else rev(k, 2, lp, 1.0) * .0001),
           (RAVI, BLUE, "₹1.90 cr", (1395, 650), rev(k, 4, lp, 3.5))], 1, "umar")
    T(img, "Amit (25 se)", 1500, 280, 42, MINT, rev(k, 2, lp))
    T(img, "lagaye ₹42 lakh", 1500, 340, 34, SOFT, rev(k, 3, lp), "Medium")
    T(img, "Ravi (35 se)", 1500, 700, 42, BLUE, rev(k, 2, lp))
    T(img, "lagaye ₹30 lakh", 1500, 760, 34, SOFT, rev(k, 3, lp), "Medium")
    T(img, "Sirf ₹12 lakh zyada, rakam ~3.4 guna", W / 2, 975, 46, GOLD, rev(k, 6, lp), anchor="ma")

STEP = fv(1e4, .12, 240, .10)
def ch_step(img, k, lp, t):
    T(img, "Har saal SIP 10% badhao", 120, 150, 60, WHITE, rev(k, 1, lp))
    def f(d):
        m = 1e4; base = 780
        for y in range(20):
            a = rev(k, 2, lp - y * .08, .4)
            if a <= 0: continue
            x = 140 + y * 52; hf = 1e4 / 61159 * 400; hs = m / 61159 * 400 * a
            d.rectangle((x, base - hs, x + 22, base), fill=MINT + (int(255 * a),))
            d.rectangle((x + 24, base - hf, x + 44, base), fill=GREY + (int(255 * a),))
            m *= 1.1
        d.text((140, base + 18), "Saal 1", font=F("Medium", 28), fill=SOFT + (255,))
        d.text((140 + 19 * 52 + 44, base + 18), "Saal 20", font=F("Medium", 28), fill=SOFT + (255,), anchor="ra")
        a = rev(k, 2, lp)
        if a:
            d.text((140, 330), "Mahine ki SIP: ₹10,000 se ₹61,159 (saal 20 tak)", font=F("Medium", 34), fill=MINT + (int(255 * a),))
            d.text((140, 380), "Normal SIP: hamesha ₹10,000", font=F("Medium", 34), fill=GREY + (int(255 * a),))
        a = rev(k, 3, lp)
        if a:
            d.rounded_rectangle((1250, 330, 1810, 780), 30, fill=(4, 14, 12, int(210 * a)))
            rows = [("", "Normal", "Step-up"), ("Lagaye", "₹24 L", "₹68.7 L"), ("Value*", "₹99.9 L", "₹1.99 cr")]
            for j, (a1, a2, a3) in enumerate(rows):
                aa = a if j < 2 else rev(k, 4, lp)
                y = 370 + j * 120
                d.text((1280, y), a1, font=F("Medium", 34), fill=SOFT + (int(255 * aa),))
                d.text((1560, y), a2, font=F("Bold", 40), fill=GREY + (int(255 * aa),), anchor="ra")
                d.text((1780, y), a3, font=F("Bold", 40), fill=MINT + (int(255 * aa),), anchor="ra")
            d.text((1280, 720), "*12% maan kar", font=F("Medium", 28), fill=SOFT + (int(255 * a),))
    ov(img, f)
    T(img, "Lagbhag DOGUNI rakam", W / 2, 900, 60, GOLD, rev(k, 5, lp), anchor="ma")

def ch_mist(img, k, lp, t):
    items = [(1, "Market girte hi SIP band karna"), (5, "Roz portfolio check karna"), (6, "Bahut saare funds"), (7, "Kharche (expense ratio) ko ignore karna"), (9, "Bina lakshya (goal) ke SIP")]
    def f(d):
        for i, (line, s) in enumerate(items):
            a = rev(k, line, lp)
            if a <= 0: continue
            y = 200 + i * 112; cur = (k >= line) and (i == len(items) - 1 or k < items[i + 1][0])
            d.rounded_rectangle((100, y, 900, y + 92), 22, fill=(RED if cur else (4, 14, 12)) + (int((235 if cur else 170) * a),))
            d.text((140, y + 46), f"{i+1}. {s}", font=F("Bold", 36), fill=WHITE + (int(255 * a),), anchor="lm")
        if 2 <= k <= 4:
            a = rev(k, 2, lp)
            d.text((1000, 220), "20 saal SIP, 5ve saal 1 saal ruke", font=F("Bold", 40), fill=WHITE + (int(255 * a),))
            for j, (lab, v, col) in enumerate([("Bina ruke", 99.9e5, MINT), ("1 saal ruke", 92.2e5, RED)]):
                aa = rev(k, 3, lp - j * .3); y = 320 + j * 170
                d.rounded_rectangle((1000, y, 1000 + 760 * v / 1e7 * aa, y + 110), 20, fill=col + (int(255 * aa),))
                if aa > .9: d.text((1030, y + 55), f"{lab}: {lakh(v)}", font=F("Bold", 40), fill=INK + (255,), anchor="lm")
            a = rev(k, 3, lp)
            if a: d.text((1000, 680), "₹1.2 lakh kam lagaye, ~₹7.7 lakh kam mile", font=F("Bold", 38), fill=GOLD + (int(255 * a),))
        if k >= 7 and k < 9:
            a = rev(k, 8, lp)
            d.text((1000, 220), "Kharche ke baad return: 11% vs 10%", font=F("Bold", 40), fill=WHITE + (int(255 * a),))
            for j, (lab, v, col) in enumerate([("11%", 87.4e5, MINT), ("10%", 76.6e5, RED)]):
                aa = rev(k, 8, lp - j * .3); y = 320 + j * 170
                d.rounded_rectangle((1000, y, 1000 + 760 * v / 1e7 * aa, y + 110), 20, fill=col + (int(255 * aa),))
                if aa > .9: d.text((1030, y + 55), f"{lab}: {lakh(v)}", font=F("Bold", 40), fill=INK + (255,), anchor="lm")
            if a: d.text((1000, 680), "1% ka fark = ~₹10.8 lakh (20 saal)", font=F("Bold", 38), fill=GOLD + (int(255 * a),))
    ov(img, f)

def ch_recap(img, k, lp, t):
    pts = [(1, "SIP = har mahine anushasan"), (2, "Girawat mein zyada units"), (3, "Jaldi shuruaat = sabse bada fayda"), (4, "Step-up se chhoti shuruaat badi"), (5, "Girawat mein SIP band mat karo")]
    for i, (line, s) in enumerate(pts):
        a = rev(k, line, lp)
        if a > 0:
            ov(img, lambda d, i=i, a=a: d.line([(165, 238 + i * 105), (185, 258 + i * 105), (215, 218 + i * 105)], fill=MINT + (int(255 * a),), width=9, joint="curve"))
        T(img, s, 240, 205 + i * 105, 50, WHITE, rev(k, line, lp))
    T(img, "Like • Subscribe • Comment: aapne SIP kis umar mein shuru ki?", W / 2, 820, 44, GOLD, rev(k, 7, lp), anchor="ma")
    T(img, "Research karein ya SEBI-registered advisor se salah lein", W / 2, 900, 36, SOFT, rev(k, 6, lp), "Medium", anchor="ma")

CHAPTERS = [
 dict(key="hook", title="Shuruaat", draw=ch_hook, lines=[
  "हर महीने दस हज़ार रुपये। बीस साल। और आखिर में, लगभग एक करोड़?",
  "सुनने में जादू लगता है। लेकिन यह जादू नहीं, गणित है।",
  "आज इस वीडियो में हम SIP का पूरा हिसाब समझेंगे।",
  "SIP क्या है, यह काम कैसे करती है, कंपाउंडिंग का असली खेल, SIP और RD का फ़र्क, समय की ताकत, स्टेप-अप SIP, शुरू कैसे करें, और वो पाँच गलतियाँ जो लोगों का लाखों का नुकसान करवाती हैं।",
  "हर नंबर हम कैलकुलेटर से निकालेंगे, ताकि आप खुद चेक कर सको।",
  "एक ज़रूरी बात: यह वीडियो सिर्फ़ समझाने के लिए है। हम किसी फंड या स्टॉक की सलाह नहीं देते।"]),
 dict(key="what", title="SIP kya hai", draw=ch_what, lines=[
  "चलो शुरू करते हैं। SIP आखिर है क्या?",
  "SIP का मतलब है, सिस्टेमैटिक इन्वेस्टमेंट प्लान।",
  "यानी हर महीने, एक तय तारीख को, एक तय रकम, अपने आप निवेश होती रहे। जैसे रिकरिंग डिपॉज़िट, बस पैसा बाज़ार से जुड़े फंड में जाता है।",
  "म्यूचुअल फंड को एक टोकरी समझो। उसमें बहुत सारी कंपनियों के शेयर या बॉन्ड होते हैं।",
  "आप जब पैसा डालते हो, तो आपको उस टोकरी की यूनिट्स मिलती हैं।",
  "एक यूनिट की उस दिन की कीमत को NAV कहते हैं, यानी नेट एसेट वैल्यू।",
  "SIP की सबसे अच्छी बात: आपको बाज़ार का सही समय पकड़ने की ज़रूरत नहीं। आदत अपना काम करती है।"]),
 dict(key="rca", title="Rupee cost averaging", draw=ch_rca, lines=[
  "अब SIP की पहली ताकत समझते हैं: रुपी कॉस्ट एवरेजिंग।",
  "मान लो आप हर महीने एक हज़ार रुपये डालते हो।",
  "पहले महीने NAV दस रुपये है, तो आपको सौ यूनिट्स मिलती हैं।",
  "दूसरे महीने बाज़ार गिरा, NAV आठ रुपये। अब उतने ही पैसों में एक सौ पच्चीस यूनिट्स।",
  "तीसरे महीने बाज़ार चढ़ा, NAV साढ़े बारह रुपये। अब सिर्फ़ अस्सी यूनिट्स।",
  "चौथे महीने फिर दस रुपये, यानी सौ यूनिट्स।",
  "कुल चार हज़ार रुपये, और चार सौ पाँच यूनिट्स।",
  "आपकी औसत कीमत पड़ी लगभग नौ रुपये अठासी पैसे, जबकि NAV का औसत था दस रुपये तेरह पैसे।",
  "मतलब, जब बाज़ार गिरता है, SIP अपने आप ज़्यादा यूनिट्स खरीद लेती है। गिरावट आपके लिए सेल बन जाती है।",
  "लेकिन ध्यान रहे, यह नुकसान से बचने की गारंटी नहीं है। यह बस खरीदने की कीमत को औसत कर देता है।"]),
 dict(key="comp", title="Compounding ka hisaab", draw=ch_comp, lines=[
  "अब SIP की सबसे बड़ी ताकत: कंपाउंडिंग।",
  "कंपाउंडिंग का मतलब है, आपकी कमाई पर भी कमाई।",
  "मान लो हर महीने दस हज़ार, बीस साल तक, और सालाना रिटर्न बारह प्रतिशत मान लेते हैं।",
  "आपकी जेब से गए कुल चौबीस लाख रुपये।",
  "और बीस साल बाद, कैलकुलेटर के हिसाब से, यह बन सकता है लगभग निन्यानवे लाख नब्बे हज़ार।",
  "यानी लगभग छिहत्तर लाख रुपये, सिर्फ़ कंपाउंडिंग की कमाई।",
  "ग्राफ़ देखो। पहले दस साल लाइन धीरे चलती है, फिर तेज़ी से ऊपर भागती है। यही कंपाउंडिंग का कर्व है।",
  "पर याद रखो, बारह प्रतिशत सिर्फ़ एक मान लिया गया नंबर है।",
  "अगर रिटर्न दस प्रतिशत हो, तो रकम लगभग छिहत्तर लाख साठ हज़ार। और आठ प्रतिशत हो, तो लगभग उनसठ लाख।",
  "म्यूचुअल फंड के रिटर्न बाज़ार पर निर्भर करते हैं, और कोई भी रिटर्न पक्का नहीं होता।"]),

 dict(key="rd", title="SIP vs RD", draw=ch_rd, lines=[
  "अक्सर लोग पूछते हैं, SIP बेहतर है या रिकरिंग डिपॉज़िट?",
  "चलो वही दस हज़ार महीना, बीस साल का हिसाब लगाते हैं।",
  "अगर RD पर सात प्रतिशत ब्याज मान लें, तो रकम बनती है लगभग बावन लाख चालीस हज़ार।",
  "और SIP में बारह प्रतिशत मान कर, लगभग निन्यानवे लाख नब्बे हज़ार।",
  "लेकिन यह तुलना पूरी कहानी नहीं है। RD में ब्याज तय होता है और जोखिम कम।",
  "इक्विटी फंड की SIP बाज़ार से जुड़ी है। कुछ साल अच्छे होंगे, कुछ साल नुकसान भी दिखेगा।",
  "इसलिए सही चुनाव आपके लक्ष्य, समय और जोखिम उठाने की क्षमता पर निर्भर करता है। कम समय के लक्ष्य के लिए स्थिर विकल्प, लंबे लक्ष्य के लिए लोग अक्सर SIP चुनते हैं।"]),
 dict(key="time", title="Waqt ki taakat", draw=ch_time, lines=[
  "अब सबसे ज़रूरी चीज़: समय।",
  "दो दोस्त हैं, अमित और रवि। दोनों हर महीने दस हज़ार की SIP करते हैं, दोनों साठ साल की उम्र तक।",
  "अमित पच्चीस साल की उम्र में शुरू करता है। रवि दस साल बाद, पैंतीस में।",
  "अमित ने कुल लगाए बयालीस लाख। रवि ने तीस लाख।",
  "बारह प्रतिशत मान कर, साठ की उम्र में रवि के पास लगभग एक करोड़ नब्बे लाख।",
  "और अमित के पास? लगभग छह करोड़ पचास लाख!",
  "सिर्फ़ बारह लाख ज़्यादा लगाए, लेकिन लगभग साढ़े तीन गुना रकम। फ़र्क पैसे का नहीं, समय का है।"]),
 dict(key="step", title="Step-up SIP", draw=ch_step, lines=[
  "अब एक स्मार्ट तरीका: स्टेप-अप SIP।",
  "हर साल सैलरी बढ़ती है, तो SIP भी थोड़ी बढ़ा दो। जैसे हर साल दस प्रतिशत।",
  "पहले साल दस हज़ार, दूसरे साल ग्यारह हज़ार, तीसरे साल बारह हज़ार एक सौ, और ऐसे ही। बीसवें साल तक यह लगभग इकसठ हज़ार महीना हो जाती है।",
  "बीस साल में आपकी जेब से जाएँगे लगभग अड़सठ लाख सत्तर हज़ार।",
  "और बारह प्रतिशत मान कर, रकम बन सकती है लगभग एक करोड़ निन्यानवे लाख।",
  "यानी सामान्य SIP से लगभग दोगुनी। शुरुआत छोटी रखो, बस हर साल थोड़ा बढ़ाते रहो।"]),

 dict(key="start", title="SIP kaise shuru karein", draw=ch_start, lines=[
  "अब समझते हैं, SIP शुरू करने के आम कदम क्या होते हैं।",
  "पहला, आपका PAN और KYC पूरा होना चाहिए। यह एक बार का काम है।",
  "दूसरा, लक्ष्य और समय तय करो। पैसा कितने साल बाद और किसलिए चाहिए।",
  "तीसरा, लक्ष्य और जोखिम के हिसाब से फंड की कैटेगरी चुनो। लंबे लक्ष्य और छोटे लक्ष्य के लिए अलग सोच होती है।",
  "चौथा, SIP की तारीख सैलरी आने के कुछ दिन बाद रखो, ताकि पैसा हमेशा खाते में हो।",
  "पाँचवाँ, ऑटो-डेबिट लगाओ, और रोज़ की चिंता छोड़ दो।",
  "छठा, साल में एक बार रिव्यू करो, और सैलरी बढ़े तो SIP भी बढ़ाओ।",
  "ध्यान रहे, हम किसी फंड का नाम नहीं सुझाते। फंड चुनने से पहले उसकी जानकारी पढ़ें, या रजिस्टर्ड सलाहकार से बात करें।"]),
 dict(key="mist", title="5 badi galtiyan", draw=ch_mist, lines=[
  "अब वो पाँच गलतियाँ, जो SIP का फ़ायदा खा जाती हैं।",
  "पहली गलती: बाज़ार गिरते ही SIP बंद कर देना।",
  "मान लो बीस साल की SIP में, पाँचवें साल बाज़ार गिरा, और आपने एक साल SIP रोक दी।",
  "आपने सिर्फ़ एक लाख बीस हज़ार कम लगाए, लेकिन आखिर में लगभग सात लाख सत्तर हज़ार कम मिले।",
  "और गिरावट में रुकने का मतलब है, सस्ती यूनिट्स खरीदने का मौका छोड़ना।",
  "दूसरी गलती: रोज़-रोज़ पोर्टफ़ोलियो चेक करना। लंबी दौड़ में रोज़ का उतार-चढ़ाव बस शोर है।",
  "तीसरी गलती: बहुत सारे फंड। दस फंड रखने से डाइवर्सिफ़िकेशन नहीं, बस उलझन बढ़ती है।",
  "चौथी गलती: खर्च को नज़रअंदाज़ करना। हर फंड एक सालाना फ़ीस लेता है, जिसे एक्सपेंस रेशियो कहते हैं।",
  "अगर खर्च की वजह से आपका रिटर्न ग्यारह की जगह दस प्रतिशत रह जाए, तो बीस साल में लगभग दस लाख अस्सी हज़ार का फ़र्क पड़ सकता है।",
  "पाँचवीं गलती: बिना लक्ष्य के SIP। पहले तय करो, पैसा किसलिए है और कब चाहिए। घर, बच्चों की पढ़ाई, या रिटायरमेंट।"]),
 dict(key="recap", title="Saar", draw=ch_recap, lines=[
  "तो आज का सार।",
  "SIP यानी हर महीने अनुशासन से निवेश।",
  "रुपी कॉस्ट एवरेजिंग गिरावट में ज़्यादा यूनिट्स दिलाती है।",
  "कंपाउंडिंग को समय चाहिए, इसलिए जल्दी शुरुआत सबसे बड़ा फ़ायदा है।",
  "स्टेप-अप SIP से छोटी शुरुआत भी बड़ी बन सकती है।",
  "और गिरावट में घबराकर SIP बंद मत करो।",
  "यह वीडियो सिर्फ़ जानकारी के लिए है। निवेश से पहले अपनी रिसर्च करें, या SEBI रजिस्टर्ड सलाहकार से बात करें।",
  "अगर वीडियो काम का लगा, तो लाइक करो, चैनल को सब्सक्राइब करो, और कमेंट में बताओ, आपने SIP किस उम्र में शुरू की। मिलते हैं अगले वीडियो में।"]),
]
TITLE_CARD, GAP, TAIL = 2.4, 0.5, 1.0

def title_card(img, i, title, t):
    a = clamp(min(t / .4, (TITLE_CARD - t) / .4))
    T(img, f"CHAPTER {i}", W / 2, 400, 44, GOLD, a, anchor="ma")
    T(img, title, W / 2, 470, 110, WHITE, a, anchor="ma")

def render_frame(ci, t, timing):
    ch = CHAPTERS[ci]; tm = timing[ci]
    img = BG.copy()
    start = TITLE_CARD if ci else 0.0
    if ci and t < TITLE_CARD:
        title_card(img, ci, ch["title"], t); frame_chrome(img, None, ""); return img
    k, lp = -1, 0.0
    for j, (s, d) in enumerate(tm["lines"]):
        if t >= s: k, lp = j, t - s
    ch["draw"](img, k, lp, t - start)
    frame_chrome(img, ci if ci else None, ch["title"])
    D = tm["dur"]
    f = min(1, (D - t) / .35) if ci < len(CHAPTERS) - 1 else min(1, (D - t) / 1.0)
    if f < 1: img = Image.blend(Image.new("RGBA", img.size, (0, 0, 0, 255)), img, max(0, f))
    return img

def voice():
    import numpy as np, soundfile as sf
    from kokoro_onnx import Kokoro
    k = Kokoro(f"{HERE}/kokoro/kokoro-v1.0.onnx", f"{HERE}/kokoro/voices-v1.0.bin"); SR = 24000
    timing = []; tracks = []
    for ci, ch in enumerate(CHAPTERS):
        pos = TITLE_CARD if ci else 0.6; buf = [np.zeros(int(pos * SR))]; lines = []
        for s in ch["lines"]:
            a, _ = k.create(s, voice="hf_alpha", speed=0.95, lang="hi")
            idx = np.where(np.abs(a) > .01)[0]; a = a[max(0, idx[0] - 200): idx[-1] + 1500]
            lines.append((pos, len(a) / SR)); buf += [a, np.zeros(int(GAP * SR))]; pos += len(a) / SR + GAP
        dur = pos + TAIL; buf.append(np.zeros(int(TAIL * SR)))
        y = np.concatenate(buf)[:int(dur * SR)]; tracks.append(y)
        timing.append(dict(lines=lines, dur=len(y) / SR))
        print(ch["key"], "%.1fs" % (len(y) / SR))
    full = np.concatenate(tracks); full /= np.abs(full).max() / .95
    sf.write(f"{HERE}/long_vo.wav", full, SR)
    json.dump(timing, open(f"{HERE}/long_timing.json", "w"))
    print("total %.1f s = %.1f min" % (len(full) / SR, len(full) / SR / 60))

def render_chapter(ci, out):
    timing = json.load(open(f"{HERE}/long_timing.json"))
    D = timing[ci]["dur"]
    ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                           "-c:v", "libx264", "-preset", "veryfast", "-crf", "21", "-pix_fmt", "yuv420p", out], stdin=subprocess.PIPE)
    for i in range(int(round(D * FPS))): ff.stdin.write(render_frame(ci, i / FPS, timing).convert("RGB").tobytes())
    ff.stdin.close(); ff.wait()

if __name__ == "__main__":
    mode = sys.argv[1]
    if mode == "voice": voice()
    elif mode == "stills":
        timing = json.load(open(f"{HERE}/long_timing.json")); ims = []
        for ci, tm in enumerate(timing):
            ls = tm["lines"]
            for j in ([len(ls) // 2, len(ls) - 1] if ci else [len(ls) - 1]):
                s, d = ls[j]; ims.append(render_frame(ci, s + d * .9, timing).convert("RGB").resize((640, 360)))
        cols = 3; rows = math.ceil(len(ims) / cols); sheet = Image.new("RGB", (640 * cols, 360 * rows))
        for i, im in enumerate(ims): sheet.paste(im, ((i % cols) * 640, (i // cols) * 360))
        sheet.save(sys.argv[2])
    elif mode == "chapter": render_chapter(int(sys.argv[2]), sys.argv[3])
