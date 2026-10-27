"""Paisa Science animated long-video editor (16:9).
usage: python3 anim.py <project dir> <out.mp4> [stills]
<project dir> holds lines.py (LINES), audio/lNN.wav + audio/durs.json, and plan.py with:
  IMG   = {"s01": "path.png", ...}         scene stills (any size, 16:9)
  CLIPS = {line_id: ("clip.mp4", "lipsync"|"anim"[, start_offset_s])}  optional video per line
  SMALL = {line_id: "small caption"}       optional assumption line under the headline
  GAP, LONG_GAP_AFTER, END_HOLD, DISCLAIMER
Every line = one or two shots (new shot every <=5 s), camera always moving (push-in, pull-out, pans, drift with tilt),
whip-pan blur into each new shot, headline text pops in with overshoot + glow, music ducked under the voices,
whoosh / pop / coin SFX on cuts and text.
"""
import os, sys, json, math, subprocess, tempfile, wave
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from fontTools.ttLib import TTFont

W, H, FPS, SR = 1920, 1080, 30, 44100
VERT = os.environ.get("ANIM_VERTICAL") == "1"   # 9:16 Shorts mode: 1080x1920, text kept clear of the Shorts UI
if VERT: W, H = 1080, 1920
HEAD_Y, CHIP_XY, SMALL_B, DISC_B = (300, (40, 190), 560, 470) if VERT else (80, (40, 34), 40, 30)
HERE = os.path.dirname(os.path.abspath(__file__))
POP = "/usr/share/fonts/truetype/google-fonts/Poppins-Bold.ttf"
DJV = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
_cmap = {p: set(TTFont(p)["cmap"].getBestCmap()) for p in (POP, DJV)}
COL = {"gold": (255, 200, 40), "white": (255, 255, 255), "red": (255, 80, 70), "teal": (40, 230, 200)}
_fc = {}
def font(p, s):
    if (p, s) not in _fc: _fc[(p, s)] = ImageFont.truetype(p, s)
    return _fc[(p, s)]

def runs(s):
    out = []
    for ch in s:
        p = POP if ord(ch) in _cmap[POP] else DJV
        if out and out[-1][0] == p: out[-1][1] += ch
        else: out.append([p, ch])
    return out

def text_sprite(s, size, col, stroke=None):
    """RGBA sprite of a headline: coloured text, dark outline, soft glow."""
    stroke = stroke or max(4, size // 14)
    rs = runs(s); d0 = ImageDraw.Draw(Image.new("L", (1, 1)))
    wsum = sum(d0.textlength(t, font=font(p, size)) for p, t in rs)
    pad = size // 2; w, h = int(wsum) + 2 * pad, int(size * 1.45) + 2 * pad
    txt = Image.new("RGBA", (w, h), (0, 0, 0, 0)); d = ImageDraw.Draw(txt); x = pad
    for p, t in rs:
        f = font(p, size); d.text((x, pad), t, font=f, fill=col + (255,), stroke_width=stroke, stroke_fill=(15, 8, 25, 255))
        x += d.textlength(t, font=f)
    glow = Image.new("RGBA", (w, h), col + (0,)); glow.putalpha(txt.getchannel("A").filter(ImageFilter.GaussianBlur(size // 5)).point(lambda a: int(a * .55)))
    out = Image.alpha_composite(glow, txt)
    return out

def ease(x): x = min(max(x, 0), 1); return x * x * (3 - 2 * x)
def pop_scale(t, d=.38):
    """0 before the pop, then a bouncy ease-out-back from 0.4x to 1.0x (overshoots to ~1.1x)."""
    if t <= 0: return 0
    if t >= d: return 1
    x = t / d - 1; c1 = 2.2; return .4 + .6 * (1 + (c1 + 1) * x ** 3 + c1 * x ** 2)
def appear_times(n, line_d):
    if n <= 1: return [.12] * n
    return [min(.12 + q * (line_d * .55 / (n - 1)), line_d - 1.4) for q in range(n)]

MOVES = ["push", "pan_r", "pull", "pan_l", "drift_up", "push_tilt", "pan_r_tilt", "pull_down"]
def camera(img, t, d, move, seed):
    """Crop+resize a big still for time t of a d-second shot; camera never static."""
    p = ease(t / d) * .85 + (t / d) * .15
    bw, bh = img.size; base = min(bw / W, bh / H)
    z0, z1, x0, x1, y0, y1, r0, r1 = 1.0, 1.0, .5, .5, .5, .5, 0, 0
    if move == "push": z0, z1 = 1.0, 1.22
    elif move == "pull": z0, z1 = 1.25, 1.03
    elif move == "pan_r": z0 = z1 = 1.18; x0, x1 = .38, .62
    elif move == "pan_l": z0 = z1 = 1.18; x0, x1 = .62, .38
    elif move == "drift_up": z0, z1 = 1.12, 1.2; y0, y1 = .62, .42
    elif move == "pull_down": z0, z1 = 1.25, 1.08; y0, y1 = .38, .55
    elif move == "push_tilt": z0, z1, r0, r1 = 1.05, 1.25, -1.5, 1.5
    elif move == "pan_r_tilt": z0 = z1 = 1.2; x0, x1, r0, r1 = .4, .6, 1.2, -1.2
    rnd = np.random.default_rng(seed); jx, jy = rnd.uniform(-.04, .04, 2)
    z = z0 + (z1 - z0) * p; cx = x0 + (x1 - x0) * p + jx * (1 - p); cy = y0 + (y1 - y0) * p + jy * (1 - p)
    cw, ch = W * base / z, H * base / z
    left = min(max(cx * bw - cw / 2, 0), bw - cw); top = min(max(cy * bh - ch / 2, 0), bh - ch)
    rot = r0 + (r1 - r0) * p
    if abs(rot) > .05:
        m = 1.06; cw2, ch2 = cw * m, ch * m
        l2 = min(max(left - (cw2 - cw) / 2, 0), bw - cw2); t2 = min(max(top - (ch2 - ch) / 2, 0), bh - ch2)
        fr = img.crop((int(l2), int(t2), int(l2 + cw2), int(t2 + ch2))).resize((int(W * m), int(H * m)), Image.BILINEAR)
        fr = fr.rotate(rot, Image.BILINEAR)
        ox, oy = (fr.width - W) // 2, (fr.height - H) // 2
        return fr.crop((ox, oy, ox + W, oy + H))
    return img.crop((int(left), int(top), int(left + cw), int(top + ch))).resize((W, H), Image.BILINEAR)

def whip(arr, k, n=6):
    """Directional motion blur + slide for the first n frames of a new shot (whip-pan)."""
    if k >= n: return arr
    s = (1 - k / n) ** 2; shift = int(260 * s); taps = 7
    acc = np.zeros_like(arr, dtype=np.float32)
    for i in range(taps):
        acc += np.roll(arr, -shift + int(shift * 2 * i / (taps - 1) * .5), axis=1)
    return (acc / taps).astype(np.uint8)

TOPBAND = Image.new("L", (1, H))
TB = 820 if VERT else 430
for y in range(H): TOPBAND.putpixel((0, y), int(max(0, (TB - y) / TB) ** 1.5 * 165))
TOPBAND = TOPBAND.resize((W, H)); BLACK = Image.new("RGB", (W, H), (0, 0, 0))
BOTBAND = Image.new("L", (1, H))
B0, B1 = (1300, 300) if VERT else (900, 180)
for y in range(H): BOTBAND.putpixel((0, y), int(max(0, min(1, (y - B0) / B1)) ** 1.4 * 150))
BOTBAND = BOTBAND.resize((W, H))

def chip(s="PAISA SCIENCE"):
    f = font(POP, 30); d0 = ImageDraw.Draw(Image.new("L", (1, 1))); tw = d0.textlength(s, font=f)
    im = Image.new("RGBA", (int(tw) + 44, 54), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, im.width - 1, 53), 27, fill=(0, 0, 0, 140)); d.text((22, 7), s, font=f, fill=(255, 200, 40, 255))
    return im
CHIP = chip()

def small_sprite(s, size=36, col=(235, 235, 235)):
    f = font(POP, size); d0 = ImageDraw.Draw(Image.new("L", (1, 1))); tw = d0.textlength(s, font=f)
    im = Image.new("RGBA", (int(tw) + 50, size + 34), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, im.width - 1, im.height - 1), 20, fill=(0, 0, 0, 150)); d.text((25, 10), s, font=f, fill=col + (255,))
    return im

def video_frames(path, n, ss=0.0):
    pr = subprocess.Popen(["ffmpeg", "-loglevel", "error", "-ss", f"{ss:.3f}", "-i", path, "-vf", f"fps={FPS},scale={int(W*1.12)}:{int(H*1.12)}:force_original_aspect_ratio=increase,crop={int(W*1.12)}:{int(H*1.12)}",
                           "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    fs = []; sz = int(W * 1.12) * int(H * 1.12) * 3
    while len(fs) < n:
        b = pr.stdout.read(sz)
        if len(b) < sz: break
        fs.append(Image.frombuffer("RGB", (int(W * 1.12), int(H * 1.12)), b))
    pr.stdout.close(); pr.wait()
    if len(fs) < n - 1: sys.exit(f"{path}: {len(fs)} frames < {n} needed: regenerate it longer")
    while len(fs) < n: fs.append(fs[-1])   # < 1 frame rounding only
    return fs

def tone(f, d, decay, gain=1.0):
    t = np.arange(int(d * SR)) / SR; return np.sin(2 * np.pi * f * t) * np.exp(-t * decay) * gain

def main(pdir, out, stills=False):
    ns = {"__file__": os.path.abspath(f"{pdir}/plan.py")}; exec(open(f"{pdir}/lines.py").read(), ns); exec(open(f"{pdir}/plan.py").read(), ns)
    LINES, IMG, CLIPS, SMALL = ns["LINES"], ns["IMG"], ns.get("CLIPS", {}), ns.get("SMALL", {})
    GAP, LONG, END_HOLD, DISC = ns["GAP"], .5, ns["END_HOLD"], ns["DISCLAIMER"]
    durs = {int(k): v for k, v in json.load(open(f"{pdir}/audio/durs.json")).items()}
    # ---- timeline ----
    shots, t, voice, sfx = [], 0.0, [], []
    mi = 0
    for (lid, spk, txt, heads, sk) in LINES:
        d = durs[lid]; slot = d + ns.get("GAP_OVERRIDE", {}).get(lid, LONG if lid in ns["LONG_GAP_AFTER"] else GAP)
        if lid == LINES[-1][0]: slot += END_HOLD
        voice.append((t, f"{pdir}/audio/l{lid:02d}.wav"))
        clip = CLIPS.get(lid)
        parts = [slot] if (clip or slot <= 5.2) else [slot / 2, slot / 2]
        tt = t
        for k, pd in enumerate(parts):
            shots.append(dict(t=tt, d=pd, img=sk, move=MOVES[mi % len(MOVES)], clip=clip if k == 0 else None, lid=lid,
                              heads=heads, small=SMALL.get(lid), line_t=t, line_d=slot))
            mi += 1; tt += pd
        for at in appear_times(len(heads), slot): sfx.append(("pop", t + at))
        t += slot
    TOTAL = t
    print(f"total {TOTAL:.1f}s, {len(shots)} shots")
    # ---- glitch gate: no AI clip may show a flagged glitch (noise burst / flash / morph pop) inside the part we use ----
    import clipcheck
    bad = []
    for sh in shots:
        c = sh["clip"]
        if not c or c[1] != "anim": continue
        off = c[2] if len(c) > 2 else 0.0
        _, rr = clipcheck.check(c[0])
        hit = [(a, b) for a, b in rr if b >= off and a <= off + sh["d"]]
        if hit: bad.append(f"line {sh['lid']}: {os.path.basename(c[0])} glitch at " + ", ".join(f"{a:.2f}-{b:.2f}s" for a, b in hit) + f" (used {off:.2f}-{off + sh['d']:.2f}s)")
    if bad and os.environ.get("ALLOW_GLITCH") != "1":
        sys.exit("GLITCH GATE FAILED (regenerate the clip or move its start offset):\n  " + "\n  ".join(bad))
    # ---- sprites ----
    imgs = {}
    def getimg(k):
        if k not in imgs:
            im = Image.open(IMG[k]).convert("RGB"); s = max(W * 1.3 / im.width, H * 1.3 / im.height)
            imgs[k] = im.resize((int(im.width * s), int(im.height * s)), Image.LANCZOS)
        return imgs[k]
    spr = {}
    def heads_for(sh):
        key = sh["lid"]
        if key not in spr:
            L = []
            for i, (s, c) in enumerate(sh["heads"]):
                size = 112 if len(s) <= 18 else (92 if len(s) <= 26 else 74)
                sp = text_sprite(s, size, COL[c])
                if sp.width > W - 20: sp = sp.resize((W - 20, int(sp.height * (W - 20) / sp.width)), Image.LANCZOS)
                L.append(sp)
            sm = small_sprite(sh["small"], 30 if VERT else 36) if sh["small"] else None
            if sm is not None and sm.width > W - 30: sm = sm.resize((W - 30, int(sm.height * (W - 30) / sm.width)), Image.LANCZOS)
            spr[key] = (L, sm)
        return spr[key]
    chip_spr = chip(ns["CHIP_TEXT"]) if ns.get("CHIP_TEXT") else (None if "CHIP_TEXT" in ns else CHIP)
    disc = small_sprite(DISC, 30)
    if disc.width > W - 30: disc = disc.resize((W - 30, int(disc.height * (W - 30) / disc.width)), Image.LANCZOS)
    # ---- render ----
    tmp = tempfile.mkdtemp(); vid = f"{tmp}/v.mp4"
    reuse = os.environ.get("REUSE_VID")
    if reuse: vid = reuse
    if not stills and not reuse:
        ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                               "-c:v", "libx264", "-preset", "veryfast", "-crf", "20", "-pix_fmt", "yuv420p", vid], stdin=subprocess.PIPE)
    cur, frames, cache_clip = -1, 0, None
    NF = int(round(TOTAL * FPS))
    stills_at = [sh["t"] + sh["d"] * .7 for sh in shots] if stills else None
    for i in range(0 if not reuse else NF, NF):
        T = i / FPS
        if stills and not any(abs(T - s) < .5 / FPS for s in stills_at): continue
        j = max(n for n in range(len(shots)) if shots[n]["t"] <= T + 1e-6); sh = shots[j]
        if j != cur:
            cur, k0 = j, i
            cache_clip = video_frames(sh["clip"][0], int(math.ceil(sh["d"] * FPS)) + 1, sh["clip"][2] if len(sh["clip"]) > 2 else 0.0) if (sh["clip"] and not stills) else None
        lt = T - sh["t"]
        if cache_clip is not None:
            src = cache_clip[min(i - k0, len(cache_clip) - 1)]
            fr = camera(src, lt, sh["d"], "push" if sh["clip"][1] == "lipsync" else "drift_up", j)
        elif sh["clip"] and stills:
            fr = camera(getimg(sh["img"]), lt, sh["d"], sh["move"], j)
        else:
            fr = camera(getimg(sh["img"]), lt, sh["d"], sh["move"], j)
        arr = whip(np.asarray(fr), i - k0) if (j > 0 and not stills) else np.asarray(fr)
        fr = Image.fromarray(arr)
        L, sm = heads_for(sh)
        ht = T - sh["line_t"]
        if L or sm:
            fr = Image.composite(BLACK, fr, TOPBAND)
        fr = fr.convert("RGBA")
        if chip_spr is not None: fr.alpha_composite(chip_spr, CHIP_XY)
        n = len(L); y = HEAD_Y
        ats = appear_times(n, sh["line_d"])
        for q, sp in enumerate(L):
            sc = pop_scale(ht - ats[q])
            if sc > 0:
                w2, h2 = max(1, int(sp.width * sc)), max(1, int(sp.height * sc))
                s2 = sp.resize((w2, h2), Image.BILINEAR) if sc != 1 else sp
                fr.alpha_composite(s2, ((W - w2) // 2, y + (sp.height - h2) // 2))
            y += int(sp.height * .78)
        if sm and ht > .5:
            fr.alpha_composite(sm, ((W - sm.width) // 2, H - sm.height - SMALL_B))
        if sh["lid"] == LINES[-1][0] or (T > TOTAL - 9):
            fr = Image.composite(Image.new("RGBA", (W, H), (0, 0, 0, 255)), fr, BOTBAND)
            fr.alpha_composite(disc, ((W - disc.width) // 2, H - disc.height - DISC_B))
        fr = fr.convert("RGB")
        if stills:
            fr.save(f"{out[:-4]}_s{j + 1:02d}.jpg", quality=85); continue
        ff.stdin.write(fr.tobytes())
    if stills: return
    if not reuse: ff.stdin.close(); ff.wait()
    # ---- audio: voices + music (ducked) + sfx ----
    N = int(TOTAL * SR) + SR
    vo = np.zeros(N)
    for t0, p in voice:
        w = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", p, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True).stdout
        a = np.frombuffer(w, np.float32); s = int(t0 * SR); vo[s:s + len(a)] += a[:N - s]
    fx = np.zeros(N); rng = np.random.default_rng(3)
    seen = set()
    for kind, t0 in sfx:
        key = (kind, round(t0, 2))
        if key in seen: continue
        seen.add(key); s = int(t0 * SR)
        if True:
            sig = tone(1320, .18, 28, .10) + tone(2640, .18, 40, .05) + tone(3960, .18, 55, .03)
        e = min(N, s + len(sig)); fx[s:e] += sig[:e - s]
    cuts = ",".join(f"{x['t']:.2f}" for x in shots[1:])
    music = np.zeros((N, 2))
    if ns.get("MUSIC", True):   # plan.py MUSIC = False -> voices + light SFX only (e.g. Islamic channel, no instruments)
        subprocess.run([sys.executable, f"{HERE}/music.py", f"{tmp}/m.wav", f"{TOTAL:.3f}", cuts], check=True)
        sf = wave.open(f"{tmp}/m.wav"); m = np.frombuffer(sf.readframes(sf.getnframes()), np.int16).reshape(-1, 2).astype(np.float32) / 32767
        music[:min(N, len(m))] = m[:N]
    env = np.convolve(np.abs(vo), np.ones(int(.25 * SR)) / int(.25 * SR), "same")
    duck = np.where(env > .01, .22, .55)
    duck = np.convolve(duck, np.ones(int(.3 * SR)) / int(.3 * SR), "same")
    mix = music * duck[:, None] * .5 + (vo + fx)[:, None]
    mix /= max(1e-6, np.abs(mix).max()) / .9
    with wave.open(f"{tmp}/a.wav", "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((mix * 32767).astype(np.int16).tobytes())
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", vid, "-i", f"{tmp}/a.wav", "-filter_complex", "[1:a]loudnorm=I=-14:TP=-1.5:LRA=11[a]",
                    "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-shortest", "-movflags", "+faststart", out], check=True)
    json.dump([dict(t=round(s["t"], 2), d=round(s["d"], 2), lid=s["lid"], img=s["img"]) for s in shots], open(f"{out[:-4]}_shots.json", "w"))
    print("done", out, f"{TOTAL:.1f}s")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], len(sys.argv) > 3 and sys.argv[3] == "stills")
