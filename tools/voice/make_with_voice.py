"""Build a Paisa Science Short from Junaid's own recording.
usage: python3 make_with_voice.py <video: sip|card|infl> <recording> <out.mp4>
The recording = the script's lines read in order with a short pause (~1 s) between lines.
Steps: clean voice -> find the lines -> fit each scene to its line -> render -> music + mix.
"""
import os, sys, subprocess, tempfile, re
import numpy as np, soundfile as sf
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, ROOT)
import paisa
from PIL import Image

name, rec, out = sys.argv[1], sys.argv[2], sys.argv[3]
tmp = tempfile.mkdtemp(); clean = f"{tmp}/clean.wav"
subprocess.run([sys.executable, f"{HERE}/clean_voice.py", rec, clean], check=True)
y, SR = sf.read(clean)
NL = len(paisa.VIDEOS[name][1])                       # number of script lines = scenes

# --- find spoken lines: frames louder than the noise floor, gaps >= 0.55 s split lines
win = int(.02 * SR); e = np.sqrt(np.convolve(y ** 2, np.ones(win) / win, "same"))
thr = max(np.percentile(e, 20) * 4, 10 ** (-42 / 20)); voiced = e > thr
segs, i = [], 0
while i < len(voiced):
    if voiced[i]:
        j = i
        while j < len(voiced) and voiced[j]: j += 1
        segs.append([i, j]); i = j
    else: i += 1
merged = []
for a, b in segs:
    if merged and a - merged[-1][1] < .55 * SR: merged[-1][1] = b
    else: merged.append([a, b])
merged = [s for s in merged if s[1] - s[0] > .25 * SR]          # drop clicks / breaths
while len(merged) > NL:                                        # too many: join the closest pair
    gaps = [merged[k + 1][0] - merged[k][1] for k in range(len(merged) - 1)]
    k = int(np.argmin(gaps)); merged[k][1] = merged[k + 1][1]; del merged[k + 1]
if len(merged) < NL:
    sys.exit(f"Found {len(merged)} lines but the script has {NL}. Please leave a 1-second pause between lines.")

# --- scene timing: original durations, stretched to fit each spoken line (+ breathing room)
orig = [0] + paisa.CUTS[name] + [30]
lead, tail = .35, .55
new = [0.0]
for k in range(NL):
    od = orig[k + 1] - orig[k]; ln = (merged[k][1] - merged[k][0]) / SR
    new.append(new[-1] + max(od if k else 3.0, lead + ln + tail))
TOTAL = new[-1]
print("scene cuts:", [round(c, 2) for c in new[1:-1]], "total %.1fs" % TOTAL)

# --- voice track placed scene by scene
vo = np.zeros(int(TOTAL * SR) + SR)
for k, (a, b) in enumerate(merged):
    s = int((new[k] + lead) * SR); seg = y[a:b]
    seg = seg * np.minimum(1, np.minimum(np.arange(len(seg)), np.arange(len(seg))[::-1]) / (.01 * SR))  # 10 ms fades
    vo[s:s + len(seg)] += seg
sf.write(f"{tmp}/vo.wav", vo[:int(TOTAL * SR)], SR)

# --- frames: map new time -> original scene time (compress short scenes, hold the end of long ones)
def frame(T):
    k = max(i for i in range(NL) if new[i] <= T); t = T - new[k]
    od, nd = orig[k + 1] - orig[k], new[k + 1] - new[k]
    lt = t if t < od - .25 else min(t, od - .25)
    img = paisa.VIDEOS[name][0](orig[k] + lt)
    f = min(1, t / .2 if k else 1, (nd - t) / .2 if k < NL - 1 else 1)
    if f < 1: img = Image.blend(Image.new("RGBA", img.size, (0, 0, 0, 255)), img, max(f, 0))
    return img.convert("RGB")

vid = f"{tmp}/v.mp4"
ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", "1080x1920", "-r", "30", "-i", "-",
                       "-c:v", "libx264", "-preset", "medium", "-crf", "20", "-pix_fmt", "yuv420p", vid], stdin=subprocess.PIPE)
for i in range(int(TOTAL * 30)): ff.stdin.write(frame(i / 30).tobytes())
ff.stdin.close(); ff.wait()

subprocess.run([sys.executable, f"{ROOT}/music.py", f"{tmp}/m.wav", f"{TOTAL:.3f}", ",".join(f"{c:.2f}" for c in new[1:-1])], check=True)
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", vid, "-i", f"{tmp}/m.wav", "-i", f"{tmp}/vo.wav", "-filter_complex",
    "[2:a]aresample=44100,aformat=channel_layouts=stereo,volume=1.0,asplit=2[v1][v2];[1:a]volume=0.4[m];"
    "[m][v1]sidechaincompress=threshold=0.03:ratio=8:attack=20:release=400[duck];"
    "[duck][v2]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.95[a]",
    "-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out], check=True)
print("done ->", out, "%.1fs" % TOTAL)
