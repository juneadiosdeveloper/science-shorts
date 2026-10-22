from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math, sys
FD = "/usr/share/fonts/truetype/google-fonts/"
def F(w, s): return ImageFont.truetype(FD + f"Poppins-{w}.ttf", s)
INK = (8, 34, 29); INK2 = (16, 60, 50); GOLD = (255, 205, 70); GOLD_D = (190, 140, 20); MINT = (70, 220, 140); WHITE = (255, 255, 255)

def grad(w, h, a, b):
    im = Image.new("RGB", (1, h))
    for y in range(h): im.putpixel((0, y), tuple(int(a[i] + (b[i] - a[i]) * y / h) for i in range(3)))
    return im.resize((w, h))

def mark(d, cx, cy, s):
    """Flask holding stacked gold coins: 'paisa' + 'science'."""
    neck_w, neck_h = .34 * s, .42 * s
    body = [(cx - neck_w / 2, cy - .55 * s), (cx + neck_w / 2, cy - .55 * s), (cx + neck_w / 2, cy - .55 * s + neck_h),
            (cx + .62 * s, cy + .55 * s), (cx - .62 * s, cy + .55 * s), (cx - neck_w / 2, cy - .55 * s + neck_h)]
    d.polygon(body, fill=INK2, outline=MINT, width=max(4, int(s * .06)))
    d.rounded_rectangle((cx - neck_w / 2 - .08 * s, cy - .63 * s, cx + neck_w / 2 + .08 * s, cy - .52 * s), int(.04 * s), fill=MINT)
    r = .2 * s
    for i, (dx, dy) in enumerate([(-.24, .36), (.2, .36), (-.02, .17), (.0, -.02)]):
        x, y = cx + dx * s, cy + dy * s
        d.ellipse((x - r, y - r * .62, x + r, y + r * .62), fill=GOLD, outline=GOLD_D, width=max(2, int(s * .025)))
    f = F("Bold", int(s * .26)); tw = d.textlength("₹", font=f)
    d.text((cx - tw / 2, cy - .02 * s - s * .19), "₹", font=f, fill=(120, 80, 0))

def logo(path):
    S = 800; im = grad(S, S, INK2, INK); d = ImageDraw.Draw(im)
    mark(d, S / 2, S / 2 - 20, 420)
    im.save(path)

def banner(path):
    W, H = 2560, 1440; im = grad(W, H, INK2, INK).convert("RGBA"); d = ImageDraw.Draw(im, "RGBA")
    # faint rising compound curve across whole banner
    ov = Image.new("RGBA", (W, H), (0, 0, 0, 0)); od = ImageDraw.Draw(ov)
    for gx in range(0, W, 160): od.line((gx, 0, gx, H), fill=(255, 255, 255, 12), width=2)
    pts = [(x, 1330 - 1250 * (1.08 ** (x / 64) - 1) / (1.08 ** 40 - 1)) for x in range(0, W + 1, 8)]
    od.line(pts, fill=MINT + (45,), width=12)
    im.alpha_composite(ov); d = ImageDraw.Draw(im, "RGBA")
    # safe area 1546x423 centred
    cx, cy = W // 2, H // 2
    mark(d, cx - 560, cy, 300)
    d.text((cx - 360, cy - 175), "Paisa", font=F("Bold", 150), fill=WHITE)
    d.text((cx - 360 + d.textlength("Paisa ", font=F("Bold", 150)), cy - 175), "Science", font=F("Bold", 150), fill=GOLD)
    d.text((cx - 352, cy + 20), "Paise ka gyaan, 30 second mein", font=F("Medium", 64), fill=MINT)
    d.text((cx - 352, cy + 110), "SIP  •  Budget  •  Tax  •  Credit Card  •  Investing basics", font=F("Regular", 42), fill=(210, 225, 220))
    im.convert("RGB").save(path)

if __name__ == "__main__":
    out = sys.argv[1]
    logo(f"{out}/paisa_science_logo.png"); banner(f"{out}/paisa_science_banner.png")
