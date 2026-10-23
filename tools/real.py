"""Paisa Science realistic presenter Short: talking-head clips + Runway b-roll + one continuous voice track.
usage: python3 real.py <dir> <out.mp4> [stills]
<dir>: vo.mp3 (full narration), plan.txt lines "start end clip.mp4 overlay_index" (seconds on the narration timeline;
       talking clips must start exactly where their audio starts). Overlays reuse the scene cards from short3d.py.
"""
import os, sys, subprocess, tempfile
import numpy as np
from PIL import Image
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import paisa, short3d
from short3d import W, H, FPS, SHADE, BLACK, chip, ease, XF

def dur(p):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p],
                                capture_output=True, text=True).stdout)

def reader(path, need):
    """Frames of a clip, cover-cropped to 1080x1920, slowed only if shorter than needed; holds the last frame."""
    st = 1.0 if os.path.basename(path).startswith("talk") else max(1.0, need / dur(path))   # never retime lip-synced clips
    vf = f"setpts={st:.4f}*PTS,fps={FPS},scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}"
    pr = subprocess.Popen(["ffmpeg", "-loglevel", "error", "-i", path, "-vf", vf, "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                          stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    last = None
    while True:
        b = pr.stdout.read(W * H * 3)
        if len(b) < W * H * 3: break
        last = Image.frombytes("RGB", (W, H), b); yield last
    pr.stdout.close(); pr.wait()
    while True: yield last

def main(d, out, stills=False):
    plan = []
    for ln in open(f"{d}/plan.txt"):
        if ln.strip() and not ln.startswith("#"):
            a, b, c, k = ln.split(); plan.append((float(a), float(b), f"{d}/{c}", int(k)))
    ovl = short3d.SCENES["card"]
    TOTAL = plan[-1][1]
    if stills:
        for i, (a, b, c, k) in enumerate(plan):
            t = (b - a) - .5
            fr = subprocess.run(["ffmpeg", "-loglevel", "error", "-ss", f"{min(t, dur(c) - .1):.2f}", "-i", c, "-frames:v", "1", "-vf",
                                 f"scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H}", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                                capture_output=True).stdout
            base = Image.frombytes("RGB", (W, H), fr[:W * H * 3])
            im = Image.composite(BLACK, base, SHADE).convert("RGBA"); chip(im); ovl[k](im, t, b - a)
            paisa.disclaimer(im, "Sirf educational. Financial advice nahi.")
            im.convert("RGB").save(f"{out[:-4]}_s{i + 1}.jpg", quality=88)
        return
    tmp = tempfile.mkdtemp(); vid = f"{tmp}/v.mp4"
    ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", str(FPS), "-i", "-",
                           "-c:v", "libx264", "-preset", "medium", "-crf", "19", "-pix_fmt", "yuv420p", vid], stdin=subprocess.PIPE)
    seg, rd, prev_last = -1, None, None
    for i in range(int(TOTAL * FPS)):
        T = i / FPS
        j = max(n for n in range(len(plan)) if plan[n][0] <= T + 1e-6)
        a, b, c, k = plan[j]
        if j != seg: seg, rd = j, reader(c, b - a)
        t = T - a
        im = Image.composite(BLACK, next(rd), SHADE).convert("RGBA")
        chip(im); ovl[k](im, t, b - a); paisa.disclaimer(im, "Sirf educational. Financial advice nahi.")
        im = im.convert("RGB")
        if j > 0 and t < XF and prev_last is not None: im = Image.blend(prev_last, im, ease(t / XF))
        ff.stdin.write(im.tobytes())
        if T + 1.5 / FPS >= b: prev_last = im
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
    main(sys.argv[1], sys.argv[2], len(sys.argv) > 3 and sys.argv[3] == "stills")
