"""Flag glitches in AI animation clips before they go into a video.
usage: python3 tools/clipcheck.py clip1.mp4 [clip2.mp4 ...] [--sheet out.jpg]
Checks every frame (scaled to 180x320) for:
  - noise bursts: high-frequency energy jumps far above the clip's own median (glitter/static clouds, 'sparkle explosions')
  - flashes: mean brightness jumps between neighbouring frames
  - big sudden changes: frame-to-frame difference spikes (morph pops, cuts inside the clip)
Prints PASS/FLAG per clip with the bad time ranges, and optionally saves a contact sheet (every 0.5 s) to look at.
"""
import sys, subprocess, numpy as np
from PIL import Image
W, H, FPS = 180, 320, 24
def frames(p):
    b = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", p, "-vf", f"fps={FPS},scale={W}:{H}", "-f", "rawvideo", "-pix_fmt", "gray", "-"],
                       capture_output=True).stdout
    return np.frombuffer(b, np.uint8).reshape(-1, H, W).astype(np.float32)
def ranges(idx):
    out = []
    for i in idx:
        if out and i - out[-1][1] <= 3: out[-1][1] = i
        else: out.append([i, i])
    return [(a / FPS, b / FPS) for a, b in out]
def check(p):
    f = frames(p)
    hf = np.array([np.abs(np.diff(x, axis=0)).mean() + np.abs(np.diff(x, axis=1)).mean() for x in f])
    br = f.mean(axis=(1, 2)); df = np.r_[0, np.abs(np.diff(f, axis=0)).mean(axis=(1, 2))]
    med_hf, med_df = np.median(hf), np.median(df) + 0.5
    bad = sorted(set(np.where(hf > med_hf * 1.45)[0]) | set(np.where(np.r_[0, np.abs(np.diff(br))] > 12)[0]) | set(np.where(df > med_df * 6)[0]))
    return len(f) / FPS, ranges(bad)
def sheet(paths, out):
    tiles = []
    for p in paths:
        f = frames(p); idx = list(range(0, len(f), FPS // 2))
        row = Image.new("L", (W * len(idx), H))
        for k, i in enumerate(idx): row.paste(Image.fromarray(f[i].astype(np.uint8)), (k * W, 0))
        tiles.append(row)
    c = Image.new("L", (max(t.width for t in tiles), H * len(tiles)))
    for k, t in enumerate(tiles): c.paste(t, (0, k * H))
    c.save(out)
if __name__ == "__main__":
    a = sys.argv[1:]; out = None
    if "--sheet" in a: i = a.index("--sheet"); out = a[i + 1]; del a[i:i + 2]
    flagged = 0
    for p in a:
        d, r = check(p)
        if r: flagged += 1; print(f"FLAG {p} ({d:.1f}s): " + ", ".join(f"{x:.2f}-{y:.2f}s" for x, y in r))
        else: print(f"PASS {p} ({d:.1f}s)")
    if out: sheet(a, out); print("sheet:", out)
    sys.exit(1 if flagged else 0)
