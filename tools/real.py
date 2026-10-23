"""Paisa Science realistic presenter Short: talking-head clips + Runway b-roll + one continuous voice track.
usage: python3 real.py <dir> <out.mp4> [stills] [--ovl NAME]
<dir>: vo.mp3 (full narration), plan.txt lines "start end clip.mp4 overlay_index" (seconds on the narration timeline;
       talking clips must start exactly where their audio starts). Overlays come from short3d.SCENES[NAME] (default: card).
Style guide rules enforced here: hard cuts only (no fades), clips are never slowed or frozen (a clip shorter than its
slot is an error: regenerate it longer), every clip is colour-matched to the first talking clip, light film grain on top.
"""
import os, sys, subprocess, tempfile
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import paisa, short3d
from short3d import W, H, FPS, BLACK, chip, clamp

# lighter top shading than the 3D format (owner feedback): just enough for the headline numbers to read
SHADE = Image.new("L", (1, H))
for y in range(H):
    top = clamp((600 - y) / 600) ** 1.4 * 150
    bot = clamp((y - 1350) / 570) ** 1.3 * 190
    SHADE.putpixel((0, y), int(max(top, bot)))
SHADE = SHADE.resize((W, H))
GRAIN = 4.0          # film grain strength (std-dev in 0-255 units)

def dur(p):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p],
                                capture_output=True, text=True).stdout)

VF = f"fps={FPS},scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}"

def frame_at(path, t):
    b = subprocess.run(["ffmpeg", "-loglevel", "error", "-ss", f"{t:.3f}", "-i", path, "-frames:v", "1", "-vf", VF,
                        "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], capture_output=True).stdout
    return np.frombuffer(b[:W * H * 3], np.uint8).reshape(H, W, 3)

def stats(path):
    """Per-channel mean/std over a few frames (centre crop, so overlays/edges do not bias it)."""
    d = dur(path); fr = [frame_at(path, d * f) for f in (.15, .5, .85)]
    px = np.concatenate([f[H // 6:H * 5 // 6, W // 6:W * 5 // 6].reshape(-1, 3) for f in fr]).astype(np.float32)
    return px.mean(0), px.std(0) + 1e-3

def reader(path, need):
    """Frames of a clip at real speed, cut to the slot. Never slowed, never frozen."""
    if dur(path) + .5 / FPS < need:
        sys.exit(f"{os.path.basename(path)} is {dur(path):.2f}s but the slot needs {need:.2f}s: regenerate it longer")
    pr = subprocess.Popen(["ffmpeg", "-loglevel", "error", "-i", path, "-vf", VF, "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                          stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    last = None
    while True:
        b = pr.stdout.read(W * H * 3)
        if len(b) < W * H * 3: break
        last = np.frombuffer(b, np.uint8).reshape(H, W, 3); yield last
    pr.stdout.close(); pr.wait()
    while True: yield last          # only covers the < 1 frame rounding gap checked above

def grade(fr, src, ref, rng):
    """Reinhard colour transfer (half strength, so clips keep their own light) + light luma grain."""
    m, s = src; rm, rs = ref
    x = fr.astype(np.float32)
    y = (x - m) * (1 + .5 * (rs / s - 1)) + (m + .5 * (rm - m))
    y += rng.normal(0, GRAIN, (H, W, 1)).astype(np.float32)
    return Image.fromarray(np.clip(y, 0, 255).astype(np.uint8))

def main(d, out, stills=False, ovl_name="card"):
    plan = []
    for ln in open(f"{d}/plan.txt"):
        if ln.strip() and not ln.startswith("#"):
            a, b, c, k = ln.split(); plan.append((float(a), float(b), f"{d}/{c}", int(k)))
    ovl = short3d.SCENES[ovl_name]
    TOTAL = plan[-1][1]
    st = {c: stats(c) for _, _, c, _ in plan}
    ref = st[next(c for _, _, c, _ in plan if os.path.basename(c).startswith("talk"))]
    rng = np.random.default_rng(7)

    def dress(base, k, t, seg):
        im = Image.composite(BLACK, base, SHADE).convert("RGBA"); chip(im); ovl[k](im, t, seg)
        paisa.disclaimer(im, "Sirf educational. Financial advice nahi.")
        return im.convert("RGB")

    if stills:
        for i, (a, b, c, k) in enumerate(plan):
            t = (b - a) - .3
            base = grade(frame_at(c, min(t, dur(c) - .1)), st[c], ref, rng)
            dress(base, k, t, b - a).save(f"{out[:-4]}_s{i + 1}.jpg", quality=88)
        return
    tmp = tempfile.mkdtemp(); vid = f"{tmp}/v.mp4"
    ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                           "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p", vid], stdin=subprocess.PIPE)
    seg, rd = -1, None
    for i in range(int(round(TOTAL * FPS))):
        T = i / FPS
        j = max(n for n in range(len(plan)) if plan[n][0] <= T + 1e-6)
        a, b, c, k = plan[j]
        if j != seg: seg, rd = j, reader(c, b - a)          # hard cut: the new clip starts on this exact frame
        ff.stdin.write(dress(grade(next(rd), st[c], ref, rng), k, T - a, b - a).tobytes())
    ff.stdin.close(); ff.wait()
    cuts = ",".join(f"{p[0]:.2f}" for p in plan[1:])
    subprocess.run([sys.executable, f"{HERE}/music.py", f"{tmp}/m.wav", f"{TOTAL:.3f}", cuts], check=True)
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", vid, "-i", f"{tmp}/m.wav", "-i", f"{d}/vo.mp3", "-filter_complex",
        "[2:a]aresample=44100,aformat=channel_layouts=stereo,apad,asplit=2[v1][v2];[1:a]volume=0.25[m];"
        "[m][v1]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=400[duck];"
        "[duck][v2]amix=inputs=2:duration=first:normalize=0,loudnorm=I=-14:TP=-1.5:LRA=11[a]",
        "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-ar", "44100", "-movflags", "+faststart", out], check=True)
    print("done", out, f"{TOTAL:.1f}s")

if __name__ == "__main__":
    args = sys.argv[1:]; name = "card"
    if "--ovl" in args: i = args.index("--ovl"); name = args[i + 1]; del args[i:i + 2]
    main(args[0], args[1], len(args) > 2 and args[2] == "stills", name)
