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

SCENES = {"card": [s1, s2, s3, s4, s5, s6], "infl": [i1, i2, i3, i4, i5, i6], "r72": [r1, r2, r3, r4, r5, r6, r7]}

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
