"""Paisa Science 3D Short compositor.
usage: python3 short3d.py <video: card> <dir> <out.mp4> [stills]
<dir> holds s1.png..sN.png (9:16 scene art) and vo1.mp3..voN.mp3 (one narration line each).
Each scene lasts lead + line + tail. Scene art gets a slow Ken Burns move; overlays come from SCENES below.
"""
import os, sys, subprocess, tempfile, math
import numpy as np, soundfile as sf
from PIL import Image, ImageDraw, ImageFilter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import paisa
from paisa import W, H, F, txt, chip, ov, ease, clamp, GOLD, RED, WHITE, MINT, SOFT

FPS, LEAD, TAIL, XF = 30, .25, .45, .30
SR = 44100

def load_vo(p):
    w = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", p, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                       capture_output=True, check=True).stdout
    return np.frombuffer(w, np.float32).astype(np.float64)

def fit(img):
    """Cover-fit to 1.12x the frame so the Ken Burns move never shows an edge."""
    s = max(W * 1.12 / img.width, H * 1.12 / img.height)
    return img.convert("RGB").resize((round(img.width * s), round(img.height * s)), Image.LANCZOS)

SHADE = Image.new("L", (1, H))
for y in range(H):
    top = clamp((620 - y) / 620) ** 1.3 * 200          # dark band behind headline numbers
    bot = clamp((y - 1300) / 620) ** 1.3 * 210          # dark band behind captions
    SHADE.putpixel((0, y), int(max(top, bot)))
SHADE = SHADE.resize((W, H))
BLACK = Image.new("RGB", (W, H), (0, 0, 0))

def kb(big, t, d, k):
    """Ken Burns: alternate zoom-in / zoom-out with a small drift."""
    p = ease(t / d) if d else 0
    z = 1.0 + .07 * (p if k % 2 == 0 else 1 - p)          # 1.00 .. 1.07 of the 1.12 canvas
    cw, ch = W * 1.06 / z, H * 1.06 / z                     # canvas is >= 1.12x frame, so this always fits
    dx = (big.width - cw) * (.5 + .18 * math.sin(k * 1.7) * (p - .5))
    dy = (big.height - ch) * (.5 + .12 * math.cos(k * 1.3) * (p - .5))
    return big.transform((W, H), Image.EXTENT, (dx, dy, dx + cw, dy + ch), Image.BILINEAR)

def caption_box(img, lines, a, y0=1500):
    if a <= 0: return
    def f(d):
        fo = F("Bold", 54); lh = 74; h = lh * len(lines) + 44
        d.rounded_rectangle((60, y0, W - 60, y0 + h), 30, fill=(0, 0, 0, int(170 * a)))
        for i, (s, col) in enumerate(lines):
            f2 = fo
            while d.textlength(s, font=f2) > W - 170 and f2.size > 30: f2 = F("Bold", f2.size - 4)
            tw = d.textlength(s, font=f2); d.text(((W - tw) / 2, y0 + 20 + i * lh + (fo.size - f2.size) * .6), s, font=f2, fill=col + (int(255 * a),),
                                                  stroke_width=3, stroke_fill=(0, 0, 0, int(255 * a)))
    ov(img, f)

def big(img, s, y, size, col, a):
    """Headline text with a thick outline so it reads on any art."""
    if a <= 0: return
    fo = F("Bold", size)
    while ImageDraw.Draw(Image.new("L", (1, 1))).textlength(s, font=fo) > W - 120 and fo.size > 40: fo = F("Bold", fo.size - 6)
    def f(d):
        tw = d.textlength(s, font=fo); sc = 1 + .12 * (1 - ease(a))       # small pop-in
        d.text(((W - tw) / 2, y + 6), s, font=fo, fill=(0, 0, 0, int(150 * a)))
        d.text(((W - tw) / 2, y), s, font=fo, fill=col + (int(255 * a),), stroke_width=max(4, fo.size // 18), stroke_fill=(20, 10, 10, int(255 * a)))
    ov(img, f)

def pop(t, at, d=.35): return ease((t - at) / d)

# ---------- credit-card minimum-due Short ----------
BAL, INT = paisa.CARD_BAL, paisa.CARD_INT
def s1(img, t, d):
    big(img, "Sirf MINIMUM DUE", 230, 96, WHITE, 1.0)          # visible on frame 0 (hook + thumbnail)
    big(img, "bharte ho? RUKO!", 350, 120, RED, 1.0)
    caption_box(img, [("Credit card ka sabse bada trap", GOLD)], pop(t, 1.4))
def s2(img, t, d):
    big(img, "Bill ₹50,000", 190, 84, WHITE, pop(t, .2))
    big(img, "Minimum due ₹2,500", 315, 80, GOLD, pop(t, 1.6))
    big(img, "~3.5% mahina byaaj", 445, 84, RED, pop(t, 3.6))
    caption_box(img, [("Baaki ₹47,500 par byaaj lagta hai", WHITE), ("≈ 42% saalana!", RED)], pop(t, 4.6))
def s3(img, t, d):
    p = clamp((t - .3) / (d - .8)); m = int(round(p * 36))          # first 3 years tick by
    big(img, f"Mahina {m}", 210, 84, WHITE, pop(t, .1))
    big(img, f"Baaki: ₹{BAL[m]:,.0f}", 320, 96, RED, pop(t, .1))
    caption_box(img, [("3 saal baad bhi udhaar", WHITE), (f"₹{BAL[36]:,.0f} baaki!", GOLD)], pop(t, d - 2.2))
def s4(img, t, d):
    big(img, "15+ SAAL", 200, 150, RED, pop(t, .2))
    big(img, f"Byaaj ~₹{INT/1e3:.0f},000", 380, 100, GOLD, pop(t, 2.4))
    caption_box(img, [("₹50,000 ke bill par!", WHITE), ("GST alag. Bank ke rate alag ho sakte hain", SOFT)], pop(t, 3.2))
def s5(img, t, d):
    big(img, "Hamesha", 200, 84, WHITE, pop(t, .2))
    big(img, "POORA BILL bharo", 320, 116, MINT, pop(t, .6))
    caption_box(img, [("Utna hi kharcho, jitna", WHITE), ("agle mahine bhar sako", WHITE)], pop(t, 2.6))
def s6(img, t, d):
    big(img, "Minimum due =", 210, 96, WHITE, pop(t, .1))
    big(img, "MAXIMUM BYAAJ", 340, 124, RED, pop(t, .9))
    caption_box(img, [("Follow karo: Paisa Science", GOLD)], pop(t, 1.8))
# ---------- inflation Short (realistic format: text appears instantly on the spoken word) ----------
def on(t, at): return 1.0 if t >= at else 0.0
def i1(img, t, d):                      # talk hook
    big(img, "Aapke ₹1,00,000", 210, 100, WHITE, 1.0)
    big(img, "har saal CHHOTE!", 335, 116, RED, 1.0)
    caption_box(img, [("Mehngai ka chupa tax", GOLD)], on(t, 1.9))
def i2(img, t, d):
    big(img, "MEHNGAI", 230, 150, GOLD, 1.0)
    big(img, "= INFLATION", 400, 96, WHITE, on(t, .75))
def i3(img, t, d):
    big(img, "Maan lo: 6% saalana", 190, 84, WHITE, 1.0)
    big(img, "Aaj ₹100 ka saamaan", 315, 88, GOLD, on(t, 2.7))
    big(img, "12 saal baad ≈ ₹201", 440, 96, RED, on(t, 4.9))
    caption_box(img, [("6% sirf udaharan hai.", WHITE), ("Asli mehngai har saal badalti hai", SOFT)], on(t, 1.2))
def i4(img, t, d):
    big(img, "₹1 lakh ki khareedne ki taakat", 190, 70, WHITE, 1.0)
    big(img, "10 saal: ~₹55,800", 310, 96, GOLD, on(t, 2.9))
    big(img, "20 saal: ~₹31,200", 440, 96, RED, on(t, 5.3))
    caption_box(img, [("Maana gaya: 6% saalana mehngai", SOFT)], on(t, 1.0))
def i5(img, t, d):
    big(img, "REAL RETURN", 190, 120, GOLD, 1.0)
    big(img, "= Return − Mehngai", 335, 84, WHITE, on(t, 2.0))
    big(img, "7% − 6% ≈ 1%", 450, 110, RED, on(t, 3.8))
    caption_box(img, [("Asli badhat sirf ~1% (0.94%)", MINT), ("7% aur 6% sirf udaharan", SOFT)], on(t, 6.8))
def i6(img, t, d):                      # talk outro
    big(img, "Mehngai =", 210, 96, WHITE, on(t, .7))
    big(img, "CHUPA TAX", 340, 140, RED, on(t, .7))
    caption_box(img, [("Follow karo: Paisa Science", GOLD)], on(t, 1.4))

# ---------- Rule of 72 Short (realistic format) ----------
def r1(img, t, d):                      # talk hook
    big(img, "Paisa DOUBLE", 210, 116, GOLD, 1.0)
    big(img, "kitne saal mein?", 345, 100, WHITE, 1.0)
    caption_box(img, [("Bas ek number yaad rakho", WHITE)], on(t, 2.39))
def r2(img, t, d):
    big(img, "72", 170, 260, GOLD, on(t, .13))
    big(img, "RULE OF 72", 450, 104, WHITE, on(t, 1.24))
def r3(img, t, d):
    big(img, "72 ÷ saalana return", 190, 88, WHITE, 1.0)
    big(img, "= double hone ke saal", 310, 80, GOLD, on(t, .9))
    big(img, "Maan lo: 8% saalana", 440, 88, MINT, on(t, 2.46))
    caption_box(img, [("8% sirf udaharan hai.", WHITE), ("Returns guaranteed nahi hote", SOFT)], on(t, 2.46))
def r4(img, t, d):
    big(img, "72 ÷ 8 = 9", 200, 130, WHITE, 1.0)
    big(img, "~9 SAAL mein DOUBLE", 380, 92, GOLD, on(t, 1.53))
    caption_box(img, [("Exact (8% compound): ~9.0 saal", MINT), ("Rule of 72 sirf andaaza hai", SOFT)], on(t, 2.3))
def r5(img, t, d):
    big(img, "6% par ~12 saal", 200, 110, WHITE, 1.0)
    big(img, "12% par ~6 saal", 350, 110, MINT, on(t, 2.33))
    caption_box(img, [("Exact: 11.9 saal aur 6.1 saal", WHITE), ("Sab returns sirf udaharan", SOFT)], on(t, 2.9))
def r6(img, t, d):
    big(img, "ULTA bhi!", 190, 120, RED, 1.0)
    big(img, "Mehngai 6% maan lo", 340, 88, WHITE, on(t, 1.63))
    big(img, "~12 saal: DAAM DOUBLE", 460, 88, RED, on(t, 4.0))
    caption_box(img, [("₹100 ka saamaan ~12 saal baad ~₹200", GOLD), ("6% sirf udaharan, asli mehngai badalti hai", SOFT)], on(t, 4.0))
def r7(img, t, d):                      # talk outro
    big(img, "Agli baar:", 210, 96, WHITE, 1.0)
    big(img, "72 ÷ RETURN", 340, 130, GOLD, on(t, 1.05))
    caption_box(img, [("Follow karo: Paisa Science", GOLD)], on(t, 1.3))

# ---------- credit-card kamai Short (realistic format, 3 Nov; idea: warikoo "CREDIT CARDS se PAISE AISE KAMATE HAIN!" 4.4M) ----------
def c0(img, t, d):                      # talk hook: Rs figure on frame 1
    big(img, "₹1 LAKH PE", 200, 110, WHITE, 1.0)
    big(img, "₹60,000+ BYAAJ?", 335, 116, RED, 1.0)
    caption_box(img, [("Credit card se bank ki 3 kamai", GOLD)], on(t, 1.6))
def c1(img, t, d):
    big(img, "#1 SWIPE FEE", 200, 116, GOLD, 1.0)
    big(img, "Dukaandaar bank ko deta hai", 345, 72, WHITE, on(t, 1.0))
    big(img, "~2%", 440, 130, RED, on(t, 2.9))
def c2(img, t, d):
    big(img, "Yeh kharcha", 200, 96, WHITE, 1.0)
    big(img, "DAAMON MEIN?", 330, 120, RED, on(t, 2.0))
    caption_box(img, [("Fee card aur dukaan ke hisaab se alag hoti hai", SOFT)], on(t, .4))
def c3(img, t, d):
    big(img, "#2 BYAAJ", 200, 130, GOLD, 1.0)
    big(img, "Poora bill nahi bhara?", 350, 80, WHITE, on(t, .7))
    big(img, "~3.5% MAHINA", 460, 110, RED, on(t, 2.78))
def c4(img, t, d):
    big(img, "3.5% × 12 =", 200, 100, WHITE, 1.0)
    big(img, "42%+ SAALANA", 330, 124, RED, on(t, 1.76))
    caption_box(img, [("Compounding ke saath ~51%", MINT), ("Rate card ke hisaab se alag ho sakta hai", SOFT)], on(t, 2.3))
def c5(img, t, d):
    big(img, "₹1 lakh baaki, 1 saal", 200, 84, WHITE, 1.0)
    big(img, "BYAAJ + 18% GST", 320, 96, GOLD, on(t, 2.2))
    big(img, "₹60,000+", 440, 140, RED, on(t, 3.78))
    caption_box(img, [("Maana: 3.5%/mahina, koi payment nahi", WHITE), ("Late fee alag. Hisaab: ₹60,306-₹62,521", SOFT)], on(t, .5))
def c6(img, t, d):
    big(img, "#3 'NO COST' EMI", 200, 100, GOLD, on(t, .28))
    big(img, "+ Processing fee", 330, 92, RED, on(t, 2.34))
    big(img, "+ GST", 440, 110, RED, on(t, 3.32))
    caption_box(img, [("EMI lene se pehle total cost check karo", WHITE)], on(t, 3.5))
def c7(img, t, d):                      # talk outro
    big(img, "POORA BILL", 200, 120, MINT, 1.0)
    big(img, "ya MINIMUM?", 340, 120, RED, on(t, 1.45))
    caption_box(img, [("Comment karo!", GOLD)], on(t, 2.0))

def k0(img, t, d):                      # talk hook: Rs figure on frame 1
    big(img, "₹5,000 KE KHARCHE", 200, 100, WHITE, 1.0)
    big(img, "= ₹50 LAKH?", 330, 130, RED, 1.0)
    caption_box(img, [("20 saal ka hisaab", GOLD)], on(t, 2.8))
def k1(img, t, d):
    big(img, "SALARY: 1 TAREEKH", 200, 96, WHITE, 1.0)
    big(img, "15 TAK GAYAB!", 330, 120, RED, on(t, 2.0))
def k2(img, t, d):
    big(img, "KAHAN GAYI?", 200, 110, GOLD, 1.0)
    big(img, "Food apps ₹2,200", 330, 90, WHITE, on(t, 1.3))
    big(img, "OTT ₹700", 440, 90, WHITE, on(t, 3.3))
def k3(img, t, d):
    big(img, "Food apps ₹2,200", 200, 80, WHITE, 1.0)
    big(img, "OTT ₹700", 300, 80, WHITE, 1.0)
    big(img, "Shopping ₹2,100", 400, 90, RED, on(t, 1.0))
def k4(img, t, d):
    big(img, "= ₹5,000", 200, 140, RED, 1.0)
    big(img, "HAR MAHINA", 345, 100, WHITE, 1.0)
    caption_box(img, [("Bina pata chale!", GOLD)], on(t, 1.5))
def k5(img, t, d):
    big(img, "YAHI ₹5,000", 200, 110, GOLD, 1.0)
    big(img, "HAR MAHINA NIVESH", 330, 84, WHITE, on(t, 1.2))
    big(img, "12% SAALANA (maana)", 430, 76, MINT, on(t, 2.3))
def k6(img, t, d):
    big(img, "20 SAAL BAAD", 200, 100, WHITE, 1.0)
    big(img, "~₹50 LAKH", 320, 140, MINT, on(t, 1.3))
    big(img, "Jeb se: sirf ₹12 lakh", 460, 76, GOLD, on(t, 2.35))
    caption_box(img, [("Maana: ₹5,000 SIP, 12%/saal, 20 saal", WHITE), ("Hisaab: ₹49.96 lakh. Return guaranteed nahi", SOFT)], on(t, .3))
def k7(img, t, d):
    big(img, "RULE:", 200, 110, GOLD, 1.0)
    big(img, "PEHLE BACHAT", 320, 120, MINT, on(t, 2.1))
    big(img, "PHIR KHARCHA", 450, 110, WHITE, on(t, 2.95))
def k8(img, t, d):                      # talk outro
    big(img, "FOOD, SHOPPING", 200, 100, WHITE, 1.0)
    big(img, "ya OTT?", 330, 130, RED, on(t, 2.5))
    caption_box(img, [("Comment karo!", GOLD)], on(t, 4.3))

# ---------- FD real-return Short (realistic, Fri 6 Nov; idea: warikoo "Make regular income from your investments" 4.6M -> what your FD income really earns) ----------
def f0(img, t, d):                      # talk hook: Rs figure on frame 1
    big(img, "PAPA KI 7% FD", 200, 118, WHITE, 1.0)
    big(img, "PAISA GHATA RAHI?", 335, 104, RED, 1.0)
    caption_box(img, [("Socho: HAAN ya NAA?", GOLD)], on(t, 3.6))
def f1(img, t, d):
    big(img, "₹10 LAKH FD", 200, 124, WHITE, 1.0)
    big(img, "7% BYAAJ", 340, 120, GOLD, on(t, 1.1))
def f2(img, t, d):
    big(img, "SAAL KA BYAAJ", 200, 100, WHITE, 1.0)
    big(img, "₹70,000", 330, 140, MINT, on(t, .35))
def f3(img, t, d):
    big(img, "PAR 30% TAX SLAB", 200, 100, RED, on(t, .2))
    caption_box(img, [("Maana: 30% slab (cess alag)", SOFT)], on(t, .6))
def f4(img, t, d):
    big(img, "HAATH MEIN SIRF", 200, 96, WHITE, 1.0)
    big(img, "₹49,000", 330, 140, GOLD, on(t, 1.05))
    caption_box(img, [("₹70,000 − 30% tax = ₹49,000 (4.9%)", WHITE)], on(t, 1.2))
def f5(img, t, d):
    big(img, "MEHNGAI 6%", 200, 124, RED, on(t, .25))
    caption_box(img, [("6% sirf maana gaya, asli mehngai badalti hai", SOFT)], on(t, .6))
def f6(img, t, d):
    big(img, "TAAKAT BACHANE KO", 200, 92, WHITE, 1.0)
    big(img, "₹60,000 CHAHIYE", 320, 108, RED, on(t, 1.3))
    caption_box(img, [("₹10 lakh × 6% = ₹60,000", WHITE)], on(t, 1.4))
def f7(img, t, d):
    big(img, "₹49,000 − ₹60,000", 200, 96, WHITE, 1.0)
    big(img, "= −₹11,000", 320, 140, RED, on(t, .9))
def f8(img, t, d):
    big(img, "HAR SAAL TAAKAT", 200, 96, WHITE, 1.0)
    big(img, "CHUPCHAAP KAM!", 320, 116, RED, on(t, .5))
    caption_box(img, [("Asli return: lagbhag −1% saalana", GOLD)], on(t, .8))
def f9(img, t, d):
    big(img, "10 SAAL BAAD", 200, 110, WHITE, 1.0)
    big(img, "FD: ~₹16 LAKH", 330, 120, MINT, on(t, 1.5))
def f10(img, t, d):
    big(img, "KHAREEDNE KI TAAKAT", 200, 86, WHITE, 1.0)
    big(img, "~₹9 LAKH", 320, 150, RED, on(t, 1.75))
    caption_box(img, [("Tax + mehngai ke BAAD ka return dekho", GOLD), ("₹16.1L ÷ 1.06^10 = ~₹9.0L (aaj ke daam)", SOFT)], on(t, .4))
def f11(img, t, d):                     # talk outro
    big(img, "BHEJO US DOST KO", 200, 98, WHITE, 1.0)
    big(img, "JISKE PAPA SIRF FD", 320, 92, GOLD, on(t, 1.0))
    caption_box(img, [("Ghar mein FD hai? HAAN ya NAA", WHITE), ("Comment karo + Follow karo", GOLD)], on(t, 3.6))

# ---------- Riya vs Aman: 5 saal vs 25 saal (realistic, Sat 7 Nov; idea: warikoo "AAPKE 20s ke liye COMPLETE FINANCIAL PLANNING" 3.8M -> start in your 20s) ----------
def ra0(img, t, d):                     # talk hook: Rs figure on frame 1
    big(img, "₹3 LAKH > ₹15 LAKH?", 200, 112, WHITE, 1.0)
    big(img, "KAISE?", 330, 120, GOLD, 1.0)
    caption_box(img, [("Socho: HAAN ya NAA?", GOLD)], on(t, 3.0))
def ra1(img, t, d):
    big(img, "RIYA, UMAR 25", 200, 116, WHITE, 1.0)
    big(img, "₹5,000 / MAHINA", 330, 112, MINT, on(t, 1.4))
def ra2(img, t, d):
    big(img, "SIRF 5 SAAL", 200, 120, WHITE, 1.0)
    big(img, "KUL ₹3 LAKH", 330, 124, GOLD, on(t, .6))
    caption_box(img, [("Phir band. Ek rupaya aur nahi.", SOFT)], on(t, 1.6))
def ra3(img, t, d):
    big(img, "AMAN:", 200, 110, WHITE, 1.0)
    big(img, "\"ABHI TOH UMAR HAI\"", 320, 96, RED, on(t, .5))
def ra4(img, t, d):
    big(img, "SHURU KIYA", 200, 110, WHITE, 1.0)
    big(img, "UMAR 35 MEIN", 330, 116, RED, on(t, .4))
def ra5(img, t, d):
    big(img, "25 SAAL × ₹5,000", 200, 104, WHITE, 1.0)
    big(img, "KUL ₹15 LAKH", 330, 124, GOLD, on(t, 1.7))
def ra6(img, t, d):
    big(img, "12% SAALANA", 200, 116, WHITE, 1.0)
    caption_box(img, [("Maana: 12% saalana (1%/mahina), guaranteed nahi", SOFT)], on(t, .3))
def ra7(img, t, d):
    big(img, "AMAN @ 60", 200, 116, WHITE, 1.0)
    big(img, "~₹95 LAKH", 330, 140, MINT, on(t, 1.2))
    caption_box(img, [("₹15 lakh lagaye (35 se 60)", SOFT)], on(t, .2))
def ra8(img, t, d):
    big(img, "RIYA KE ₹3 LAKH?", 200, 104, WHITE, 1.0)
    caption_box(img, [("25-30 lagaye, phir 60 tak chhod diye", SOFT)], on(t, .2))
def ra9(img, t, d):
    big(img, "RIYA @ 60", 200, 116, WHITE, 1.0)
    big(img, "~₹1.48 CRORE!", 320, 128, GOLD, 1.0)
    caption_box(img, [("Byaaj pe byaaj ko paisa nahi, SAMAY chahiye", GOLD), ("Mehngai 6% maano to aaj ke ~₹19 lakh", SOFT)], on(t, .3))
def ra10(img, t, d):                    # talk outro
    big(img, "BHEJO US DOST KO", 200, 98, WHITE, 1.0)
    big(img, "JO \"BAAD MEIN\" BOLTA HAI", 320, 84, GOLD, on(t, 1.0))
    caption_box(img, [("Aap RIYA ho ya AMAN? Comment karo", WHITE), ("Follow karo: roz ek tricky paisa fact", GOLD)], on(t, 3.6))

# ---------- Bonus: bike loan ya card? (realistic, LIP-SYNC TEST, Sun 8 Nov; idea: warikoo "How To Pay Off Your Loans FAST? Leave the EMI TRAP" 3.8M -> costliest debt first) ----------
def bk0(img, t, d):                     # talk hook a: Rs figure on frame 1
    big(img, "₹1 LAKH BONUS", 200, 116, WHITE, 1.0)
    big(img, "KAHAN LAGAOGE?", 330, 104, GOLD, 1.0)
def bk1(img, t, d):                     # talk hook b (punch-in)
    big(img, "A) BIKE LOAN", 200, 104, WHITE, 1.0)
    big(img, "B) CREDIT CARD", 320, 104, GOLD, 1.0)
    caption_box(img, [("Socho: A ya B? Comment mein likho", GOLD)], on(t, 1.4))
def bk2(img, t, d):
    big(img, "AMAN NE A CHUNA", 200, 104, WHITE, 1.0)
    big(img, "BIKE LOAN KHATAM", 320, 100, MINT, on(t, .4))
def bk3(img, t, d):
    big(img, "EK EMI KAM", 200, 116, WHITE, 1.0)
    big(img, "DIL KHUSH :)", 330, 110, MINT, on(t, .6))
def bk4(img, t, d):
    big(img, "BIKE LOAN", 200, 116, WHITE, 1.0)
    big(img, "10% SAALANA", 330, 116, GOLD, on(t, .3))
def bk5(img, t, d):
    big(img, "SAAL KA BYAAJ", 200, 104, WHITE, 1.0)
    big(img, "~₹10,000", 320, 140, GOLD, on(t, .5))
    caption_box(img, [("₹1 lakh baaki, 10% saalana, 1 saal (sirf tulna)", SOFT)], on(t, .2))
def bk6(img, t, d):                     # talk 4a
    big(img, "PAR CARD PE?", 200, 112, WHITE, 1.0)
    big(img, "3.5% / MAHINA", 330, 112, RED, on(t, 1.0))
def bk7(img, t, d):                     # talk 4b (punch-in)
    big(img, "YAANI SAAL KA", 200, 104, WHITE, 1.0)
    big(img, "42%!", 320, 150, RED, on(t, .6))
def bk8(img, t, d):
    big(img, "₹1 LAKH CARD PE", 200, 104, WHITE, 1.0)
    big(img, "1 SAAL", 330, 116, RED, on(t, .6))
    caption_box(img, [("Maana: beech mein koi payment nahi", SOFT)], on(t, .3))
def bk9(img, t, d):
    big(img, "BYAAJ + GST", 200, 110, WHITE, 1.0)
    big(img, "₹60,306!", 320, 140, RED, on(t, .9))
    caption_box(img, [("₹1L × (1.035^12 − 1) = ₹51,107 + 18% GST", SOFT)], on(t, .3))
def bk10(img, t, d):                    # talk 6a
    big(img, "EK GALAT CHOICE", 200, 104, WHITE, 1.0)
    big(img, "= ?", 320, 130, GOLD, 1.0)
def bk11(img, t, d):                    # talk 6b (punch-in)
    big(img, "~₹50,000", 200, 140, RED, 1.0)
    big(img, "KA NUKSAAN", 340, 104, WHITE, 1.0)
    caption_box(img, [("RULE: sabse mehenga byaaj, sabse PEHLE", GOLD), ("₹60,306 − ₹10,471 = ₹49,835", SOFT)], on(t, .3))
def bk12(img, t, d):                    # talk outro a
    big(img, "BHEJO US DOST KO", 200, 98, WHITE, 1.0)
    big(img, "JO SIRF MINIMUM BHARTA HAI", 320, 74, GOLD, on(t, .9))
def bk13(img, t, d):                    # talk outro b (punch-in)
    big(img, "AAP A HO YA B?", 200, 110, GOLD, 1.0)
    caption_box(img, [("Comment karo + Follow karo", WHITE), ("Roz ek tricky paisa fact", GOLD)], on(t, .4))

# ---------- Ghar ka asli kharcha (realistic, saree look, Mon 9 Nov; idea: warikoo "BUYING a 50L HOUSE Without a LOAN" ~2.0M) ----------
def gh0(img, t, d):                     # talk hook a: Rs figure on frame 1
    big(img, "₹50 LAKH KA GHAR", 200, 104, WHITE, 1.0)
    big(img, "= ₹97 LAKH?", 330, 128, GOLD, 1.0)
def gh1(img, t, d):                     # talk hook b (punch-in)
    big(img, "HAAN YA NAA?", 200, 120, GOLD, 1.0)
    caption_box(img, [("Comment mein likho: HAAN ya NAA", WHITE)], on(t, .5))
def gh2(img, t, d):
    big(img, "KHARCHA #1", 200, 104, WHITE, 1.0)
    big(img, "20% DOWN PAYMENT", 320, 96, GOLD, on(t, .4))
def gh3(img, t, d):
    big(img, "= ₹10 LAKH", 200, 128, GOLD, 1.0)
    big(img, "APNI JEB SE", 340, 96, WHITE, on(t, .5))
    caption_box(img, [("Bank aam taur pe ~80% tak hi loan deta hai", SOFT)], on(t, .2))
def gh4(img, t, d):
    big(img, "KHARCHA #2", 200, 104, WHITE, 1.0)
    big(img, "STAMP DUTY + REGISTRATION", 320, 70, GOLD, on(t, .4))
def gh5(img, t, d):
    big(img, "~₹3.5 LAKH", 200, 128, RED, 1.0)
    big(img, "AUR!", 340, 104, WHITE, on(t, .6))
    caption_box(img, [("Udaharan: ~7% (har state mein alag)", SOFT)], on(t, .2))
def gh6(img, t, d):
    big(img, "KHARCHA #3", 200, 104, WHITE, 1.0)
    big(img, "₹40 LAKH LOAN", 320, 110, GOLD, on(t, .4))
def gh7(img, t, d):
    big(img, "20 SAAL", 200, 116, WHITE, 1.0)
    big(img, "8.5% BYAAJ", 330, 110, GOLD, on(t, .3))
    caption_box(img, [("Rate sirf udaharan, aapka alag ho sakta hai", SOFT)], on(t, .2))
def gh8(img, t, d):
    big(img, "EMI ₹34,713", 200, 116, WHITE, 1.0)
    big(img, "KUL BYAAJ?", 330, 110, GOLD, on(t, 1.0))
def gh9(img, t, d):
    big(img, "₹43.3 LAKH!", 200, 136, RED, 1.0)
    big(img, "SIRF BYAAJ", 340, 96, WHITE, on(t, .4))
    caption_box(img, [("₹34,713 × 240 = ₹83.3 lakh − ₹40 lakh loan", SOFT)], on(t, .2))
def gh10(img, t, d):
    big(img, "SAB JODO", 200, 120, WHITE, 1.0)
    caption_box(img, [("₹10L + ₹3.5L + ₹83.3L (240 EMI)", GOLD)], on(t, .3))
def gh11(img, t, d):
    big(img, "~₹97 LAKH!", 200, 140, RED, 1.0)
    big(img, "₹50 LAKH KA GHAR", 340, 90, WHITE, 1.0)
    caption_box(img, [("Maintenance, interiors alag", SOFT)], on(t, .3))
def gh12(img, t, d):
    big(img, "BHEJO US DOST KO", 200, 98, WHITE, 1.0)
    big(img, "JO GHAR LENE WALA HAI", 320, 80, GOLD, on(t, .9))
def gh13(img, t, d):
    big(img, "GHAR LOGE", 200, 110, GOLD, 1.0)
    big(img, "YA KIRAYA?", 320, 110, WHITE, 1.0)
    caption_box(img, [("Comment karo + Follow karo", WHITE), ("Roz ek tricky paisa fact", GOLD)], on(t, .3))

# ---------- Gehne ka asli kharcha (realistic, saree look, Tue 10 Nov; idea: warikoo "How To INVEST in GOLD and SILVER" ~1.4M) ----------
def gd0(img, t, d):                     # talk hook a: Rs figure on frame 1
    big(img, "₹5.92 LAKH KA GEHNA", 200, 88, WHITE, 1.0)
    big(img, "BECHO = ₹5 LAKH?", 320, 108, GOLD, 1.0)
def gd1(img, t, d):                     # talk hook b (punch-in)
    big(img, "HAAN YA NAA?", 200, 120, GOLD, 1.0)
    caption_box(img, [("Comment mein likho: HAAN ya NAA", WHITE)], on(t, .5))
def gd2(img, t, d):
    big(img, "CHUPA KHARCHA #1", 200, 96, WHITE, 1.0)
    big(img, "MAKING CHARGE", 320, 104, GOLD, on(t, .5))
def gd3(img, t, d):
    big(img, "15% = ₹75,000", 200, 120, GOLD, 1.0)
    caption_box(img, [("Udaharan: sona ₹5 lakh, making 15%", SOFT), ("(aam taur pe ~8-25%, dukaan ke hisaab se)", SOFT)], on(t, .2))
def gd4(img, t, d):
    big(img, "CHUPA KHARCHA #2", 200, 96, WHITE, 1.0)
    big(img, "GST 3%", 320, 120, GOLD, on(t, .4))
def gd5(img, t, d):
    big(img, "+₹17,250", 200, 136, RED, 1.0)
    caption_box(img, [("3% × (₹5,00,000 + ₹75,000)", SOFT)], on(t, .2))
def gd6(img, t, d):
    big(img, "BILL", 200, 104, WHITE, 1.0)
    big(img, "₹5,92,250", 320, 136, GOLD, on(t, .2))
def gd7(img, t, d):
    big(img, "ANDAR SONA?", 200, 110, WHITE, 1.0)
    big(img, "SIRF ₹5 LAKH", 330, 120, GOLD, on(t, .5))
def gd8(img, t, d):
    big(img, "BECHNE JAO...", 200, 112, WHITE, 1.0)
def gd9(img, t, d):
    big(img, "MAKING + GST", 200, 110, RED, 1.0)
    big(img, "WAPAS NAHI", 330, 110, WHITE, on(t, .3))
    caption_box(img, [("Maana: sirf sone ki keemat milti hai", SOFT), ("(kai dukaan aur katauti bhi karti hain)", SOFT)], on(t, .2))
def gd10(img, t, d):
    big(img, "DIN 1", 200, 110, WHITE, 1.0)
    big(img, "−₹92,250", 330, 140, RED, on(t, .3))
def gd11(img, t, d):
    big(img, "SONA +18.5% BADHE", 200, 88, GOLD, 1.0)
    big(img, "TAB JAAKE BARABAR", 320, 80, WHITE, on(t, .5))
    caption_box(img, [("₹5,92,250 ÷ ₹5,00,000 = 1.1845", SOFT)], on(t, .2))
def gd12(img, t, d):
    big(img, "BHEJO US DOST KO", 200, 98, WHITE, 1.0)
    big(img, "JISKI SHAADI HAI", 320, 96, GOLD, on(t, .9))
def gd13(img, t, d):
    big(img, "GEHNA: NIVESH", 200, 104, GOLD, 1.0)
    big(img, "YA SHAUK?", 320, 116, WHITE, 1.0)
    caption_box(img, [("Comment karo + Follow karo", WHITE), ("Roz ek tricky paisa fact", GOLD)], on(t, .3))

# ---------- ₹15,000 salary se ₹1 crore (realistic, saree look, Wed 11 Nov; idea: warikoo "15,000 SALARY to 1 CRORE" ~3.0M) ----------
def sl0(img, t, d):                     # talk hook a: Rs figure on frame 1
    big(img, "₹15,000 SALARY", 200, 100, WHITE, 1.0)
    big(img, "₹1 CRORE?", 330, 136, GOLD, 1.0)
def sl1(img, t, d):                     # talk hook b (punch-in)
    big(img, "HAAN YA NAA?", 200, 120, GOLD, 1.0)
    caption_box(img, [("Comment mein likho: HAAN ya NAA", WHITE)], on(t, .5))
def sl2(img, t, d):
    big(img, "STEP #1", 200, 110, WHITE, 1.0)
    big(img, "PEHLE BACHAO 20%", 320, 92, GOLD, on(t, .5))
def sl3(img, t, d):
    big(img, "₹3,000 / MAHINA", 200, 110, GOLD, 1.0)
    caption_box(img, [("₹15,000 ka 20%, salary aate hi alag", SOFT)], on(t, .2))
def sl4(img, t, d):
    big(img, "12% SAALANA", 200, 110, WHITE, 1.0)
    big(img, "(MAANA GAYA)", 320, 80, SOFT, 1.0)
    caption_box(img, [("Sirf udaharan. Return guaranteed nahi.", SOFT)], on(t, .2))
def sl5(img, t, d):
    big(img, "₹1 CRORE =", 200, 104, WHITE, 1.0)
    big(img, "~29.5 SAAL", 320, 128, RED, on(t, .2))
    caption_box(img, [("₹3,000 har mahina, kabhi nahi badhaya", SOFT)], on(t, .2))
def sl6(img, t, d):
    big(img, "STEP #2", 200, 110, WHITE, 1.0)
    big(img, "HAR HIKE PE BACHAT +10%", 320, 76, GOLD, on(t, .4))
def sl7(img, t, d):
    big(img, "₹3,000 → ₹3,300", 200, 100, GOLD, 1.0)
    big(img, "→ ₹3,630 ...", 320, 96, WHITE, on(t, .6))
    caption_box(img, [("Salary +10% / saal, bachat bhi +10%", SOFT), ("(bachat wahi 20% rehti hai)", SOFT)], on(t, .2))
def sl8(img, t, d):
    big(img, "₹1 CRORE", 200, 136, GOLD, 1.0)
    big(img, "SIRF ~23.5 SAAL", 330, 100, WHITE, on(t, .5))
def sl9(img, t, d):
    big(img, "6 SAAL PEHLE!", 200, 116, MINT, 1.0)
    caption_box(img, [("355 mahine vs 281 mahine (12% maana)", SOFT)], on(t, .2))
def sl10(img, t, d):
    big(img, "BADI SALARY NAHI", 200, 96, WHITE, 1.0)
    big(img, "BADHTI BACHAT", 320, 110, GOLD, on(t, .4))
def sl11(img, t, d):
    big(img, "AMEER BANATI HAI", 200, 100, GOLD, 1.0)
    caption_box(img, [("Dhyan: 23 saal baad ₹1 crore ki", SOFT), ("keemat mehngai se aaj se kam hogi", SOFT)], on(t, .2))
def sl12(img, t, d):
    big(img, "BHEJO US DOST KO", 200, 98, WHITE, 1.0)
    big(img, "JISKI SALARY ₹15K HAI", 320, 84, GOLD, on(t, .7))
def sl13(img, t, d):
    big(img, "STEP 1 YA STEP 2?", 200, 100, GOLD, 1.0)
    caption_box(img, [("Comment karo + Follow karo", WHITE), ("Roz ek tricky paisa fact", GOLD)], on(t, .3))

SCENES = {"card": [s1, s2, s3, s4, s5, s6], "infl": [i1, i2, i3, i4, i5, i6], "r72": [r1, r2, r3, r4, r5, r6, r7], "cc": [c0, c1, c2, c3, c4, c5, c6, c7], "kh": [k0, k1, k2, k3, k4, k5, k6, k7, k8], "fd": [f0, f1, f2, f3, f4, f5, f6, f7, f8, f9, f10, f11], "ra": [ra0, ra1, ra2, ra3, ra4, ra5, ra6, ra7, ra8, ra9, ra10], "bk": [bk0, bk1, bk2, bk3, bk4, bk5, bk6, bk7, bk8, bk9, bk10, bk11, bk12, bk13], "gh": [gh0, gh1, gh2, gh3, gh4, gh5, gh6, gh7, gh8, gh9, gh10, gh11, gh12, gh13], "sl": [sl0, sl1, sl2, sl3, sl4, sl5, sl6, sl7, sl8, sl9, sl10, sl11, sl12, sl13], "gd": [gd0, gd1, gd2, gd3, gd4, gd5, gd6, gd7, gd8, gd9, gd10, gd11, gd12, gd13]}

def main(name, d, out):
    ovl = SCENES[name]; n = len(ovl)
    arts = [fit(Image.open(f"{d}/s{k + 1}.png")) for k in range(n)]
    vos = [load_vo(f"{d}/vo{k + 1}.mp3") for k in range(n)]
    durs = [LEAD + len(v) / SR + TAIL for v in vos]
    starts = np.concatenate([[0], np.cumsum(durs)]); TOTAL = starts[-1]
    tmp = tempfile.mkdtemp()
    vo = np.zeros(int(TOTAL * SR) + SR)
    for k, v in enumerate(vos):
        s = int((starts[k] + LEAD) * SR); vo[s:s + len(v)] += v
    pk = np.max(np.abs(vo)); vo = vo / pk * .89 if pk > 0 else vo
    sf.write(f"{tmp}/vo.wav", vo[:int(TOTAL * SR)], SR)

    clips = [f"{d}/a{k + 1}.mp4" if os.path.exists(f"{d}/a{k + 1}.mp4") else None for k in range(n)]

    def clip_dur(p):
        return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p],
                                    capture_output=True, text=True).stdout)

    trim = {}                                                 # scene index -> seconds of usable clip (ping-pong loops it)
    if os.path.exists(f"{d}/trim.txt"):
        for ln in open(f"{d}/trim.txt"):
            if ln.strip(): a, b = ln.split(); trim[int(a) - 1] = float(b)

    def clip_vf(k):
        # slow the clip down only if it is shorter than the scene; otherwise play at real speed and cut
        st = 1.0 if k in trim else max(1.0, durs[k] / clip_dur(clips[k]))
        return (f"setpts={st:.4f}*PTS,fps={FPS},scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}")

    def clip_reader(k):
        """Yield the scene's frames in order (holds the last frame if the clip runs out)."""
        if k in trim:                                         # usable part only, played forward/backward
            pr = subprocess.Popen(["ffmpeg", "-loglevel", "error", "-t", str(trim[k]), "-i", clips[k], "-vf", clip_vf(k), "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                                  stdout=subprocess.PIPE)
            fr = []
            while True:
                b = pr.stdout.read(W * H * 3)
                if len(b) < W * H * 3: break
                fr.append(Image.frombytes("RGB", (W, H), b))
            pr.wait(); seq = fr + fr[-2:0:-1]
            i = 0
            while True: yield seq[i % len(seq)]; i += 1
        pr = subprocess.Popen(["ffmpeg", "-loglevel", "error", "-i", clips[k], "-vf", clip_vf(k), "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                              stdout=subprocess.PIPE)
        last = None
        while True:
            b = pr.stdout.read(W * H * 3)
            if len(b) < W * H * 3: break
            last = Image.frombytes("RGB", (W, H), b); yield last
        pr.wait()
        while True: yield last

    def clip_frame_at(k, t):
        b = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", clips[k], "-vf", clip_vf(k) + f",trim=start={t:.3f}", "-frames:v", "1",
                            "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True).stdout
        return Image.frombytes("RGB", (W, H), b[:W * H * 3])

    def dress(k, t, base):
        im = Image.composite(BLACK, base, SHADE).convert("RGBA")
        chip(im); ovl[k](im, t, durs[k])
        paisa.disclaimer(im, "Sirf educational. Financial advice nahi.")
        return im.convert("RGB")

    if len(sys.argv) > 4 and sys.argv[4] == "stills":
        for k in range(n):
            t = durs[k] - .5
            base = clip_frame_at(k, min(t, trim.get(k, 99) - .1)) if clips[k] else kb(arts[k], t, durs[k], k)
            dress(k, t, base).save(f"{out[:-4]}_s{k + 1}.jpg", quality=88)
        print("stills", [round(x, 2) for x in durs], "clips:", [bool(c) for c in clips]); return
    vid = f"{tmp}/v.mp4"
    ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                           "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p", vid], stdin=subprocess.PIPE)
    prev_last, k, rd = None, -1, None
    for i in range(int(TOTAL * FPS)):
        T = i / FPS; kk = min(int(np.searchsorted(starts, T, side="right") - 1), n - 1)
        if kk != k:
            k = kk; rd = clip_reader(k) if clips[k] else None
        t = T - starts[k]
        base = next(rd) if rd else kb(arts[k], t, durs[k], k)
        im = dress(k, t, base)
        if k > 0 and t < XF and prev_last is not None: im = Image.blend(prev_last, im, ease(t / XF))
        ff.stdin.write(im.tobytes())
        if T + 1.5 / FPS >= starts[k + 1]: prev_last = im           # last frame of this scene, for the next crossfade
    ff.stdin.close(); ff.wait()
    subprocess.run([sys.executable, f"{HERE}/music.py", f"{tmp}/m.wav", f"{TOTAL:.3f}", ",".join(f"{c:.2f}" for c in starts[1:-1])], check=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", vid, "-i", f"{tmp}/m.wav", "-i", f"{tmp}/vo.wav", "-filter_complex",
        "[2:a]aresample=44100,aformat=channel_layouts=stereo,asplit=2[v1][v2];[1:a]volume=0.35[m];"
        "[m][v1]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=400[duck];"
        "[duck][v2]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]",
        "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "44100", "-movflags", "+faststart", out], check=True)
    print("done", out, f"{TOTAL:.1f}s")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
