"""Paisa Science Shorts: shared template + three videos.
Usage: python3 paisa.py <video: sip|card|infl> stills <out.png>
       python3 paisa.py <video> render <out.mp4>
"""
import math, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

W, H, FPS, DUR = 1080, 1920, 30, 30.0
FD = "/usr/share/fonts/truetype/google-fonts/"
_fc = {}
def F(w, s):
    k = (w, s)
    if k not in _fc: _fc[k] = ImageFont.truetype(FD + f"Poppins-{w}.ttf", s)
    return _fc[k]

INK, INK2 = (8, 34, 29), (16, 60, 50)
GOLD, GOLD_D, MINT, RED, GREY, WHITE = (255, 205, 70), (190, 140, 20), (70, 220, 140), (255, 95, 85), (165, 180, 190), (255, 255, 255)
SOFT = (205, 222, 215)

def clamp(x, a=0, b=1): return max(a, min(b, x))
def ease(x): x = clamp(x); return 1 - (1 - x) ** 3
def lerp(a, b, t): return a + (b - a) * t

def _grad(a, b):
    im = Image.new("RGB", (1, H))
    for y in range(H): im.putpixel((0, y), tuple(int(a[i] + (b[i] - a[i]) * y / H) for i in range(3)))
    return im.resize((W, H)).convert("RGBA")
BG = _grad(INK2, INK)
BG_RED = _grad((70, 20, 22), (24, 8, 10))

def ov(img, fn):
    o = Image.new("RGBA", img.size, (0, 0, 0, 0)); fn(ImageDraw.Draw(o)); img.alpha_composite(o)

def txt(img, s, y, font, fill, a=1.0, x=None):
    if a <= 0: return
    fo = font
    while ImageDraw.Draw(Image.new("L", (1, 1))).textlength(s, font=fo) > (W - 280 if fo.size >= 100 else W - 140) - (0 if x is None else x - 70) and fo.size > 30:
        fo = F("Bold" if "Bold" in fo.path else "Medium", fo.size - 6)
    font = fo
    def f(d):
        tw = d.textlength(s, font=font); xx = (W - tw) / 2 if x is None else x
        d.text((xx + 3, y + 4), s, font=font, fill=(0, 0, 0, int(110 * a)))
        d.text((xx, y), s, font=font, fill=fill + (int(255 * clamp(a)),))
    ov(img, f)

def chip(img, a=1.0):
    def f(d):
        s = "PAISA SCIENCE"; fo = F("Bold", 38); tw = d.textlength(s, font=fo)
        d.rounded_rectangle(((W - tw) / 2 - 30, 92, (W + tw) / 2 + 30, 158), 33, fill=(0, 0, 0, int(150 * a)))
        d.text(((W - tw) / 2, 100), s, font=fo, fill=GOLD + (int(255 * a),))
    ov(img, f)

def disclaimer(img, s="Sirf educational. Investment advice nahi."):
    def f(d):
        fo = F("Medium", 34); tw = d.textlength(s, font=fo); d.text(((W - tw) / 2, 1838), s, font=fo, fill=SOFT + (190,))
    ov(img, f)

def caption(img, lines, a, y0=1450):
    if a <= 0: return
    def f(d):
        lh, fo = 72, F("Medium", 50); h = lh * len(lines) + 56
        d.rounded_rectangle((56, y0, W - 56, y0 + h), 34, fill=(4, 14, 12, int(215 * a)))
        for i, (s, col) in enumerate(lines):
            tw = d.textlength(s, font=fo); d.text(((W - tw) / 2, y0 + 28 + i * lh), s, font=fo, fill=col + (int(255 * a),))
    ov(img, f)

def coin(d, cx, cy, r, a=255):
    d.ellipse((cx - r, cy - r * .62, cx + r, cy + r * .62), fill=GOLD + (a,), outline=GOLD_D + (a,), width=5)
    fo = F("Bold", int(r * .8)); tw = d.textlength("₹", font=fo); d.text((cx - tw / 2, cy - r * .62), "₹", font=fo, fill=(120, 80, 0, a))

def cover(img, l1, big, l2, big_col=GOLD, t=1.0):
    """Cover / hook frame. Text kept inside the centre band (y 640-1240) so a 3:2 crop still reads."""
    chip(img)
    txt(img, l1, 660, F("Bold", 84), WHITE, 1 if t >= 1 else ease(t / .3))
    txt(img, big, 780, F("Bold", 150), big_col, 1 if t >= 1 else ease((t - .15) / .3))
    txt(img, l2, 980, F("Bold", 84), WHITE, 1 if t >= 1 else ease((t - .3) / .3))

def lakh(v):
    return f"₹{v/1e7:.2f} cr" if v >= 1e7 else f"₹{v/1e5:.1f} lakh" if v >= 1e5 else f"₹{v:,.0f}"

def axes(img, L, R, T, B, ylabels, xlabels):
    def f(d):
        fo = F("Medium", 34)
        for v, s in ylabels:
            y = B - (B - T) * v; d.line((L, y, R, y), fill=(255, 255, 255, 30), width=2); d.text((L - 20 - d.textlength(s, font=fo), y - 22), s, font=fo, fill=SOFT + (255,))
        for v, s in xlabels:
            x = L + (R - L) * v; d.text((x - d.textlength(s, font=fo) / 2, B + 14), s, font=fo, fill=SOFT + (255,))
    ov(img, f)

# ======================= VIDEO 1: SIP ======================
def sip_fv(p, r, n):
    i = r / 12; return p * ((1 + i) ** n - 1) / i * (1 + i) if n else 0

def sip(T):
    img = BG.copy()
    if T < 4:
        cover(img, "₹10,000 ki SIP", "= ₹1 CRORE?", "20 saal ka hisaab", t=1.0)
        caption(img, [("Calculator se samjho 👇".replace(" 👇", ""), GOLD)], ease((T - 1.6) / .5))
    elif T < 11:
        t = T - 4; chip(img)
        txt(img, "Har mahine ₹10,000", 330, F("Bold", 72), WHITE, ease(t / .4))
        txt(img, "20 saal = 240 kisht", 430, F("Medium", 56), SOFT, ease((t - .4) / .4))
        n = int(240 * ease((t - .8) / 3.2))
        def f(d):
            for k in range(min(n // 12, 20)):
                coin(d, 540 + (k % 2) * 12 - 6, 1240 - k * 30, 120)
        ov(img, f)
        txt(img, f"Lagaye: {lakh(n * 1e4)}", 1300, F("Bold", 76), GOLD, ease((t - .8) / .4))
        caption(img, [("Aapki jeb se kul ₹24 lakh", WHITE)], ease((t - 4.2) / .4), 1480)
    elif T < 19:
        t = T - 11; chip(img)
        txt(img, "Aapka paisa vs Uski value", 250, F("Bold", 60), WHITE, ease(t / .4))
        L, R, Tp, B = 200, 990, 420, 1260
        axes(img, L, R, Tp, B, [(v / 100, f"{v}L") for v in (0, 25, 50, 75, 100)], [(y / 20, f"{y}") for y in (0, 5, 10, 15, 20)])
        p = ease((t - .4) / 3.6); N = max(2, int(240 * p))
        def f(d):
            for fn, col in [(lambda m: 1e4 * m, GREY), (lambda m: sip_fv(1e4, .12, m), MINT)]:
                pts = [(L + (R - L) * m / 240, B - (B - Tp) * fn(m) / 1e7) for m in range(0, N + 1, 2)]
                d.line(pts, fill=col + (255,), width=12, joint="curve"); x, y = pts[-1]; d.ellipse((x - 14, y - 14, x + 14, y + 14), fill=col + (255,))
            if t > 4.2:
                a = int(255 * ease((t - 4.2) / .4)); fo = F("Bold", 58)
                d.text((L + 330, Tp + 10), "₹99.9 lakh*", font=fo, fill=MINT + (a,))
                d.text((R - 250, B - 80), "₹24 lakh", font=fo, fill=GREY + (a,))
        ov(img, f)
        txt(img, "saal", B + 64, F("Medium", 34), SOFT)
        caption(img, [("*12% saalana maan kar.", GOLD), ("Market return guaranteed nahi.", WHITE)], ease((t - 4.6) / .4))
    elif T < 25:
        t = T - 19; chip(img)
        txt(img, "Asli jaadu: COMPOUNDING", 300, F("Bold", 64), GOLD, ease(t / .4))
        def f(d):
            base, x0, bw = 1250, 230, 240
            for i, (lab, v, col) in enumerate([("Aapka paisa", 24e5, GREY), ("Kamaai*", 75.9e5, MINT)]):
                p = ease((t - .5 - i * .5) / .8); h = 700 * v / 76e5 * p; x = x0 + i * 380
                d.rounded_rectangle((x, base - h, x + bw, base), 20, fill=col + (255,))
                fo = F("Bold", 52); s = lakh(v)
                if p > .9: d.text((x + bw / 2 - d.textlength(s, font=fo) / 2, base - h - 70), s, font=fo, fill=WHITE + (255,))
                fo2 = F("Medium", 40); d.text((x + bw / 2 - d.textlength(lab, font=fo2) / 2, base + 16), lab, font=fo2, fill=SOFT + (255,))
        ov(img, f)
        caption(img, [("Kamaai par bhi kamaai =", WHITE), ("paisa ~3 guna se zyada!", MINT)], ease((t - 2.2) / .4))
    elif T < 28:
        t = T - 25; chip(img)
        txt(img, "Return badla, result badla", 300, F("Bold", 58), WHITE, ease(t / .3))
        def f(d):
            for i, (r, v) in enumerate([("8%", 59.3e5), ("10%", 76.6e5), ("12%", 99.9e5)]):
                p = ease((t - .2 - i * .25) / .6); y = 480 + i * 250
                d.text((90, y + 22), r, font=F("Bold", 60), fill=GOLD + (255,))
                d.rounded_rectangle((260, y, 260 + 640 * v / 1e7 * p, y + 120), 22, fill=MINT + (255,))
                if p > .9: d.text((290, y + 28), lakh(v), font=F("Bold", 52), fill=INK + (255,))
        ov(img, f)
        caption(img, [("Return kabhi pakka nahi hota", GOLD)], ease((t - 1.2) / .3))
    else:
        t = T - 28; chip(img)
        txt(img, "Jaldi shuru karo,", 720, F("Bold", 84), WHITE, ease(t / .3))
        txt(img, "WAQT do!", 850, F("Bold", 150), GOLD, ease((t - .3) / .3))
        caption(img, [("Follow karo: roz ek Paisa Science", GOLD)], ease((t - .6) / .3), 1400)
    disclaimer(img); return img

SIP_VO = [
    (0.35, 4, "दस हज़ार की SIP, एक करोड़?"),
    (4.4, 11, "हर महीने दस हज़ार, बीस साल तक। यानी आपने कुल चौबीस लाख लगाए।"),
    (11.4, 19, "अगर बारह प्रतिशत सालाना रिटर्न मानें, तो यह लगभग एक करोड़ बन सकता है। पर रिटर्न की गारंटी नहीं होती।"),
    (19.4, 25, "चौबीस लाख आपके, और छिहत्तर लाख कमाई। यही है कंपाउंडिंग!"),
    (25.3, 28, "रिटर्न कम, तो रकम भी कम।"),
    (28.2, 30, "जल्दी शुरू करो!"),
]

# ======================= VIDEO 2: CREDIT CARD ======================
def card_sim():
    b, out = 5e4, [5e4]; ti = 0
    while b > .5:
        b -= min(b, max(.05 * b, 200)); i = b * .035; b += i; ti += i; out.append(b)
    return out, ti
CARD_BAL, CARD_INT = card_sim()

def card(T):
    img = (BG_RED if T < 4 else BG).copy()
    if T < 4:
        cover(img, "Sirf MINIMUM DUE", "TRAP! 🚨".replace(" 🚨", ""), "bharte ho? Ruko!", big_col=RED, t=1.0)
        caption(img, [("₹50,000 ke bill ka sach", GOLD)], ease((T - 1.6) / .5))
    elif T < 10:
        t = T - 4; chip(img)
        def f(d):
            d.rounded_rectangle((140, 300, 940, 860), 40, fill=(245, 248, 246, 255))
            fo, fb = F("Medium", 46), F("Bold", 60)
            rows = [("Total due", "₹50,000", INK), ("Minimum due (5%)", "₹2,500", (200, 60, 50))]
            for i, (k, v, c) in enumerate(rows):
                a = int(255 * ease((t - .3 - i * .5) / .4)); y = 380 + i * 180
                d.text((200, y), k, font=fo, fill=(60, 80, 75, a)); d.text((880 - d.textlength(v, font=fb), y + 50), v, font=fb, fill=c + (a,))
            a = int(255 * ease((t - 1.6) / .4))
            d.text((200, 740), "Baaki ₹47,500 par byaaj", font=F("Bold", 44), fill=(200, 60, 50, a))
        ov(img, f)
        txt(img, "~3.5% mahina", 960, F("Bold", 110), RED, ease((t - 2.2) / .4))
        txt(img, "= lagbhag 42% saalana!", 1110, F("Bold", 64), WHITE, ease((t - 2.6) / .4))
        caption(img, [("Aur naye kharch par bhi", WHITE), ("interest-free din khatam", GOLD)], ease((t - 3.4) / .4))
    elif T < 18:
        t = T - 10; chip(img)
        txt(img, "Sirf minimum bharte raho to...", 260, F("Bold", 56), WHITE, ease(t / .4))
        L, R, Tp, B = 220, 990, 420, 1240
        axes(img, L, R, Tp, B, [(v / 50, f"{v}k") for v in (0, 10, 20, 30, 40, 50)], [(y / 16, f"{y}") for y in (0, 4, 8, 12, 16)])
        n = len(CARD_BAL); p = ease((t - .4) / 4.0); N = max(2, int(n * p))
        def f(d):
            pts = [(L + (R - L) * m / 192, B - (B - Tp) * CARD_BAL[m] / 5e4) for m in range(0, N)]
            d.line(pts, fill=RED + (255,), width=12, joint="curve"); x, y = pts[-1]; d.ellipse((x - 14, y - 14, x + 14, y + 14), fill=RED + (255,))
        ov(img, f)
        txt(img, "saal", B + 64, F("Medium", 34), SOFT)
        txt(img, f"Mahina {N - 1}", 1362, F("Bold", 60), GOLD, ease((t - .4) / .3))
        caption(img, [("Udhaar dheere-dheere ghatta hai", WHITE)], ease((t - 4.6) / .4))
    elif T < 24:
        t = T - 18; chip(img)
        txt(img, "Khatam hone mein", 330, F("Bold", 64), WHITE, ease(t / .4))
        txt(img, "15+ SAAL", 440, F("Bold", 150), RED, ease((t - .4) / .4))
        txt(img, "Sirf byaaj diya", 720, F("Bold", 64), WHITE, ease((t - 1.2) / .4))
        txt(img, f"~₹{CARD_INT/1e3:.0f},000", 830, F("Bold", 150), GOLD, ease((t - 1.6) / .4))
        txt(img, "₹50,000 ke bill par!", 1030, F("Bold", 64), WHITE, ease((t - 2.0) / .4))
        caption(img, [("GST alag. Bank ke rate alag ho", SOFT), ("sakte hain, apna MITC dekho", SOFT)], ease((t - 2.8) / .4))
    elif T < 28:
        t = T - 24; chip(img)
        txt(img, "Bachne ka tareeka", 380, F("Bold", 72), GOLD, ease(t / .3))
        for i, s in enumerate(["✔ Hamesha TOTAL due bharo".replace("✔ ", "1. "), "2. Utna hi kharcho jitna", "    agle mahine bhar sako"]):
            txt(img, s, 560 + i * 110, F("Bold", 60), WHITE, ease((t - .4 - i * .3) / .3), x=110)
        caption(img, [("Credit card = suvidha, udhaar nahi", MINT)], ease((t - 1.6) / .3))
    else:
        t = T - 28; chip(img)
        txt(img, "Minimum due", 720, F("Bold", 84), WHITE, ease(t / .3))
        txt(img, "= MAXIMUM", 850, F("Bold", 150), RED, ease((t - .3) / .3))
        txt(img, "byaaj", 1030, F("Bold", 84), WHITE, ease((t - .4) / .3))
        caption(img, [("Follow karo: roz ek Paisa Science", GOLD)], ease((t - .6) / .3), 1400)
    disclaimer(img, "Sirf educational. Financial advice nahi."); return img

CARD_VO = [
    (0.35, 4, "क्रेडिट कार्ड का सिर्फ़ मिनिमम ड्यू भरते हो? रुको!"),
    (4.4, 10, "मिनिमम ड्यू बस ढाई हज़ार, पर बाकी पर साढ़े तीन प्रतिशत महीना ब्याज!"),
    (10.4, 18, "अगर हर बार सिर्फ़ मिनिमम भरते रहे, तो उधार बहुत धीरे-धीरे घटता है।"),
    (18.4, 24, "खत्म होने में पंद्रह साल से ज़्यादा, और ब्याज लगभग चौरानवे हज़ार!"),
    (24.3, 28, "इसलिए हमेशा पूरा बिल भरो।"),
    (28.05, 30, "मिनिमम ड्यू, मैक्सिमम ब्याज!"),
]

# ======================= VIDEO 3: INFLATION ======================
def infl(T):
    img = BG.copy()
    if T < 4:
        cover(img, "₹1 lakh, 20 saal baad", "₹31,000?", "Mehngai ka sach", big_col=RED, t=1.0)
        caption(img, [("Paise ki TAAKAT ghatti hai", GOLD)], ease((T - 1.6) / .5))
    elif T < 10:
        t = T - 4; chip(img)
        txt(img, "Mehngai (Inflation) kya hai?", 300, F("Bold", 60), WHITE, ease(t / .4))
        def f(d):
            for i, (yr, price) in enumerate([("Aaj", 100), ("1 saal baad", 106), ("12 saal baad", 201)]):
                a = int(255 * ease((t - .6 - i * .7) / .4)); y = 480 + i * 230
                d.rounded_rectangle((110, y, 970, y + 180), 30, fill=(4, 14, 12, int(.8 * a)))
                d.text((150, y + 55), yr, font=F("Medium", 52), fill=SOFT + (a,))
                s = f"₹{price}"; d.text((930 - d.textlength(s, font=F("Bold", 80)), y + 40), s, font=F("Bold", 80), fill=GOLD + (a,))
        ov(img, f)
        caption(img, [("Wahi saamaan, har saal mehnga", WHITE), ("(6% mehngai maan kar)", GOLD)], ease((t - 2.8) / .4))
    elif T < 18:
        t = T - 10; chip(img)
        txt(img, "₹1 lakh ki khareedne ki taakat", 260, F("Bold", 54), WHITE, ease(t / .4))
        L, R, Tp, B = 220, 990, 420, 1240
        axes(img, L, R, Tp, B, [(v / 100, f"{v}k") for v in (0, 25, 50, 75, 100)], [(y / 20, f"{y}") for y in (0, 5, 10, 15, 20)])
        p = ease((t - .4) / 3.6); N = max(2, int(200 * p))
        def f(d):
            pts = [(L + (R - L) * k / 200, B - (B - Tp) / 1.06 ** (k / 10)) for k in range(0, N + 1)]
            d.line(pts, fill=RED + (255,), width=12, joint="curve"); x, y = pts[-1]; d.ellipse((x - 14, y - 14, x + 14, y + 14), fill=RED + (255,))
            if t > 4.2:
                a = int(255 * ease((t - 4.2) / .4))
                d.text((L + (R - L) * .5 + 30, B - (B - Tp) * .558 - 110), "10 saal: ₹55,800", font=F("Bold", 46), fill=WHITE + (a,))
                d.text((R - 230, B - (B - Tp) * .312 + 30), "₹31,200", font=F("Bold", 56), fill=GOLD + (a,))
        ov(img, f)
        txt(img, "saal", B + 64, F("Medium", 34), SOFT)
        caption(img, [("20 saal mein taakat 1/3 se bhi kam", WHITE)], ease((t - 4.6) / .4))
    elif T < 24:
        t = T - 18; chip(img)
        txt(img, "REAL RETURN", 340, F("Bold", 120), GOLD, ease(t / .4))
        txt(img, "= Return − Mehngai", 510, F("Bold", 72), WHITE, ease((t - .5) / .4))
        def f(d):
            a = int(255 * ease((t - 1.2) / .4))
            rows = [("Return (maan lo)", "7%", MINT), ("Mehngai (maan lo)", "6%", RED), ("Asli kamaai", "~1%", GOLD)]
            for i, (k, v, c) in enumerate(rows):
                y = 700 + i * 150
                if i == 2: d.line((140, y - 20, 940, y - 20), fill=SOFT + (a,), width=4)
                d.text((140, y), k, font=F("Medium", 54), fill=SOFT + (a,)); d.text((940 - d.textlength(v, font=F("Bold", 72)), y - 8), v, font=F("Bold", 72), fill=c + (a,))
        ov(img, f)
        caption(img, [("Return mehngai se kam = ", WHITE), ("asal mein nuksaan", RED)], ease((t - 2.6) / .4))
    elif T < 28:
        t = T - 24; chip(img)
        txt(img, "Yaad rakho", 420, F("Bold", 80), GOLD, ease(t / .3))
        for i, s in enumerate(["Paisa sirf jodo mat,", "mehngai se TEZ", "badhana seekho"]):
            txt(img, s, 600 + i * 120, F("Bold", 76), WHITE if i != 1 else MINT, ease((t - .3 - i * .3) / .3))
        caption(img, [("Pehle samjho, phir nivesh karo", WHITE)], ease((t - 1.4) / .3))
    else:
        t = T - 28; chip(img)
        txt(img, "Mehngai", 720, F("Bold", 84), WHITE, ease(t / .3))
        txt(img, "CHUPA TAX", 850, F("Bold", 150), RED, ease((t - .3) / .3))
        txt(img, "hai!", 1030, F("Bold", 84), WHITE, ease((t - .4) / .3))
        caption(img, [("Follow karo: roz ek Paisa Science", GOLD)], ease((t - .6) / .3), 1400)
    disclaimer(img, "Sirf educational. 6% mehngai ek udaharan hai."); return img

INFL_VO = [
    (0.35, 4, "एक लाख, बीस साल बाद सिर्फ़ इकतीस हज़ार?"),
    (4.4, 10, "वही सामान हर साल महंगा। छह प्रतिशत पर, सौ का सामान बारह साल में दो सौ का।"),
    (10.4, 18, "एक लाख की ताकत, दस साल में छप्पन हज़ार, बीस साल में इकतीस हज़ार।"),
    (18.4, 24, "असली कमाई, रिटर्न माइनस महंगाई। सात में से छह गया, बचा बस एक प्रतिशत।"),
    (24.3, 28, "पैसा सिर्फ़ जोड़ो मत, महंगाई से तेज़ बढ़ाना सीखो।"),
    (28.05, 30, "महंगाई, एक छुपा टैक्स!"),
]

VIDEOS = {"sip": (sip, SIP_VO), "card": (card, CARD_VO), "infl": (infl, INFL_VO)}
CUTS = {"sip": [4, 11, 19, 25, 28], "card": [4, 10, 18, 24, 28], "infl": [4, 10, 18, 24, 28]}

def frame(name, T):
    fn = VIDEOS[name][0]; img = fn(T)
    for c in CUTS[name]:
        d = abs(T - c)
        if d < .2: img = Image.blend(Image.new("RGBA", img.size, (0, 0, 0, 255)), img, d / .2)
    return img.convert("RGB")

if __name__ == "__main__":
    name, mode, out = sys.argv[1], sys.argv[2], sys.argv[3]
    if mode == "stills":
        c = CUTS[name]; ts = [0.0, 3.5, c[0] + 4.5, c[1] + 6.5, c[2] + 5.0, c[3] + 3.5, 29.6]
        ims = [frame(name, t).resize((300, 533)) for t in ts]
        s = Image.new("RGB", (300 * len(ims), 533)); [s.paste(im, (i * 300, 0)) for i, im in enumerate(ims)]; s.save(out); sys.exit()
    ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                           "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", out], stdin=subprocess.PIPE)
    for i in range(int(DUR * FPS)): ff.stdin.write(frame(name, i / FPS).tobytes())
    ff.stdin.close(); ff.wait()
