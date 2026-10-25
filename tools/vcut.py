"""Vertical 9:16 cut-down of a 16:9 long video (Shorts / Reels).
usage: python3 vcut.py <long.mp4> <start_s> <end_s> <out.mp4> "<top line 1>|<top line 2>" "<small assumption>" "<bottom 1>|<bottom 2>"
Layout (same as instagram/reel_homeloan.mp4): blurred zoomed copy as background, the 16:9 frame full-width in the middle,
big headline above (gold 2nd line), assumption line under the video, CTA below. Hard cut in/out, audio copied from the long video
with a 0.15 s fade so the cut does not click.
"""
import sys, os, subprocess, tempfile
from PIL import Image, ImageDraw
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from anim import text_sprite, small_sprite, COL

src, a, b, out, top, small, bot = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), sys.argv[4], sys.argv[5], sys.argv[6], sys.argv[7]
W, H, VH = 1080, 1920, 608
VY = 640  # top of the 16:9 frame
ov = Image.new("RGBA", (W, H), (0, 0, 0, 0))
def place(spr, cy, maxw=1020):
    if spr.width > maxw: spr = spr.resize((maxw, int(spr.height * maxw / spr.width)), Image.LANCZOS)
    ov.alpha_composite(spr, ((W - spr.width) // 2, int(cy - spr.height / 2)))
t1, t2 = (top.split("|") + [""])[:2]
place(text_sprite(t1, 84, COL["white"]), 380)
if t2: place(text_sprite(t2, 96, COL["gold"]), 500)
if small: place(small_sprite(small, 34), VY + VH + 50)
b1, b2 = (bot.split("|") + [""])[:2]
place(text_sprite(b1, 60, COL["white"]), 1460)
if b2: place(text_sprite(b2, 64, COL["teal"]), 1560)
tmp = tempfile.mkdtemp(); ovp = f"{tmp}/ov.png"; ov.save(ovp)
d = b - a
fc = (f"[0:v]split[a][b];[a]scale=-2:{H},crop={W}:{H},gblur=sigma=40,eq=brightness=-0.18[bg];"
      f"[b]scale={W}:{VH}[fg];[bg][fg]overlay=0:{VY}[v1];[v1][1:v]overlay=0:0,format=yuv420p[v]")
subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-ss", f"{a:.3f}", "-t", f"{d:.3f}", "-i", src, "-loop", "1", "-i", ovp,
                "-filter_complex", fc, "-map", "[v]", "-map", "0:a", "-t", f"{d:.3f}",
                "-af", f"afade=t=in:d=0.05,afade=t=out:st={d - 0.15:.3f}:d=0.15", "-c:v", "libx264", "-preset", "medium", "-crf", "19",
                "-r", "30", "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart", out], check=True)
print(out, round(d, 2), "s")
