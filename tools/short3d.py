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
SCENES = {"card": [s1, s2, s3, s4, s5, s6]}

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

    def scene_img(k, t):
        im = kb(arts[k], t, durs[k], k)
        im = Image.composite(BLACK, im, SHADE).convert("RGBA")
        chip(im); ovl[k](im, t, durs[k])
        paisa.disclaimer(im, "Sirf educational. Financial advice nahi.")
        return im.convert("RGB")

    def frame(T):
        k = int(np.searchsorted(starts, T, side="right") - 1); k = min(k, n - 1); t = T - starts[k]
        im = scene_img(k, t)
        if k > 0 and t < XF:                                  # crossfade from the previous scene's end
            prev = scene_img(k - 1, durs[k - 1]); im = Image.blend(prev, im, ease(t / XF))
        return im

    if len(sys.argv) > 4 and sys.argv[4] == "stills":
        for k in range(n): frame(starts[k] + durs[k] - .5).save(f"{out[:-4]}_s{k + 1}.jpg", quality=88)
        print("stills", [round(x, 2) for x in durs]); return
    vid = f"{tmp}/v.mp4"
    ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                           "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p", vid], stdin=subprocess.PIPE)
    for i in range(int(TOTAL * FPS)): ff.stdin.write(frame(i / FPS).tobytes())
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
