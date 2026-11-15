"""Paisa Science synced motion-graphics Short (9:16) built with HyperFrames.
Owner feedback 15 Nov 2026: "animation is not good, voice and animation not matching" -> every visual lands on the word
that says it. usage:  python3 tools/hf_short.py <project dir> <out.mp4> [--preview]
<project dir>/spec.py defines:
  LINES = [dict(id=1, wav="audio/l01.wav", cap="Police video call pe 'digital arrest'...", items=[...]), ...]
     cap  = Roman (Hinglish) caption, SAME number of words as spoken (timings are spread over the spoken audio by length)
     items = visuals of that line, each anchored to a caption word index `at` (0-based) and optional `until` (word idx or "end"):
       ("char", img, mood)            mood: pop | shake | sad | float ; shows the character card for the whole line
       ("head", text, color, at)      big headline pops on word `at`
       ("sub", text, color, at)       second headline line
       ("counter", prefix, n0, n1, suffix, at, until)  number counts n0->n1 between two words
       ("call", caller, at)           incoming video-call card
       ("stamp", text, color, at)     rubber stamp slam
       ("badges", [texts], [ats])     badges popping one per word, each struck with a red cross
       ("dial", "1930", [ats])        dial pad, digits typed on words
       ("buttons", ["HAAN","NAA"], at)
       ("chip", text, at)             small source/assumption chip
  TOPIC = "SCAM ALERT"; GAP = 0.12; END_HOLD = 0.3; DISCLAIMER = "..."
"""
import os, sys, json, shutil, subprocess, wave, html
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
SR = 44100
W, H = 1080, 1920
GOLD, TEAL, RED, WHITE = "#FFC828", "#28E6C8", "#FF5046", "#FFFFFF"
COLORS = {"gold": GOLD, "teal": TEAL, "red": RED, "white": WHITE}


def read_wav(p):
    a = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", p, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True).stdout
    return np.frombuffer(a, np.float32)


def word_times(sig, words):
    """Spread words over the voiced parts of the line, weighted by length (no ASR available in the sandbox)."""
    hop = int(.01 * SR)
    rms = np.array([np.sqrt(np.mean(sig[i:i + hop] ** 2)) for i in range(0, len(sig) - hop, hop)])
    voiced = rms > max(rms.max() * .06, 1e-4)
    # close tiny gaps (< 80 ms) so syllable dips do not count as pauses
    idx = np.where(voiced)[0]
    for a, b in zip(idx[:-1], idx[1:]):
        if 1 < b - a <= 8: voiced[a:b] = True
    vt = np.where(voiced)[0] * .01                       # voiced time stamps (10 ms grid)
    if len(vt) == 0: vt = np.arange(0, len(sig) / SR, .01)
    wts = np.array([max(2, len(w.strip(".,?!:'\""))) + 1.5 for w in words], float)
    cum = np.concatenate([[0], np.cumsum(wts)]) / wts.sum()
    pos = (cum * (len(vt) - 1)).round().astype(int)
    out = []
    for k in range(len(words)):
        s = vt[pos[k]]; e = vt[max(pos[k], pos[k + 1] - 1)] + .01
        out.append((round(float(s), 3), round(float(e), 3)))
    return out


def esc(s): return html.escape(s, quote=True)


def build(pdir, out, preview=False):
    ns = {"__file__": os.path.abspath(f"{pdir}/spec.py")}
    exec(open(f"{pdir}/spec.py").read(), ns)
    LINES, TOPIC = ns["LINES"], ns.get("TOPIC", "PAISA SCIENCE")
    GAP, END_HOLD = ns.get("GAP", .12), ns.get("END_HOLD", .3)
    hf = f"{pdir}/hf"; os.makedirs(f"{hf}/assets", exist_ok=True)
    shutil.copy(f"{HERE}/hf_assets/gsap.min.js", f"{hf}/assets/gsap.min.js")
    els, js, sfx, voice = [], [], [], []
    t = 0.0; uid = 0
    caps_all = []
    for L in LINES:
        sig = read_wav(f"{pdir}/{L['wav']}"); d = len(sig) / SR
        words = L["cap"].split()
        wt = [(t + a, t + b) for a, b in word_times(sig, words)]
        L["_t"], L["_d"], L["_wt"] = t, d, wt
        voice.append((t, f"{pdir}/{L['wav']}"))
        end = t + d + GAP + (END_HOLD if L is LINES[-1] else 0)
        L["_end"] = end
        caps_all.append((words, wt, L.get("hi", [])))
        def at(i): return wt[min(i, len(wt) - 1)][0] if isinstance(i, int) else t
        for it in L.get("items", []):
            uid += 1; k = it[0]; eid = f"e{uid}"
            if k == "char":
                img, mood = it[1], it[2]
                name = os.path.basename(img); shutil.copy(img, f"{hf}/assets/{name}")
                s0 = t
                els.append(f'<div id="{eid}" class="clip card" data-start="{s0:.3f}" data-duration="{end - s0:.3f}"><img src="assets/{name}"/></div>')
                js.append(f'tl.fromTo("#{eid}",{{scale:.82,y:60,opacity:0,rotation:-2}},{{scale:1,y:0,opacity:1,rotation:0,duration:.32,ease:"back.out(2.2)"}},{s0:.3f});')
                js.append(f'tl.fromTo("#{eid} img",{{scale:1.04}},{{scale:1.16,duration:{end - s0:.3f},ease:"none"}},{s0:.3f});')
                if mood == "shake":
                    for j in range(6):
                        js.append(f'tl.to("#{eid}",{{x:{(-18 if j % 2 else 18)},rotation:{(-2 if j % 2 else 2)},duration:.05}},{s0 + .35 + j * .05:.3f});')
                    js.append(f'tl.to("#{eid}",{{x:0,rotation:0,duration:.08}},{s0 + .66:.3f});')
                elif mood == "sad":
                    js.append(f'tl.to("#{eid}",{{y:30,scale:.97,duration:.6,ease:"power2.out"}},{s0 + .4:.3f});')
                elif mood == "pop":
                    js.append(f'tl.to("#{eid}",{{scale:1.04,duration:.18,yoyo:true,repeat:1,ease:"sine.inOut"}},{s0 + .5:.3f});')
                sfx.append(("whoosh", s0))
            elif k in ("head", "sub"):
                txt, col, a = it[1], COLORS[it[2]], it[3]; s0 = max(t, at(a) - .05)
                y = 330 if k == "head" else 450
                size = 92 if k == "head" else 70
                size = int(min(size, 1000 / (0.66 * max(1, len(txt)))))
                els.append(f'<div id="{eid}" class="clip head" style="top:{y}px;font-size:{size}px;color:{col}" data-start="{s0:.3f}" data-duration="{end - s0:.3f}">{esc(txt)}</div>')
                js.append(f'tl.fromTo("#{eid}",{{scale:.4,opacity:0}},{{scale:1,opacity:1,duration:.34,ease:"back.out(2.6)"}},{s0:.3f});')
                sfx.append(("pop", s0))
            elif k == "counter":
                pre, n0, n1, suf, a, b = it[1:7]; s0 = at(a); s1 = wt[min(b, len(wt) - 1)][1] if b != "end" else t + d
                els.append(f'<div id="{eid}" class="clip counter" data-start="{s0:.3f}" data-duration="{end - s0:.3f}">{esc(pre)}<span id="{eid}n">{n0}</span>{esc(suf)}</div>')
                js.append(f'tl.fromTo("#{eid}",{{scale:.5,opacity:0}},{{scale:1,opacity:1,duration:.3,ease:"back.out(2)"}},{s0:.3f});')
                js.append(f'(function(){{var o={{v:{n0}}};tl.to(o,{{v:{n1},duration:{max(.3, s1 - s0):.3f},ease:"power1.out",onUpdate:function(){{document.getElementById("{eid}n").textContent=Math.round(o.v).toLocaleString("en-IN")}}}},{s0:.3f});}})();')
                js.append(f'tl.to("#{eid}",{{scale:1.12,duration:.12,yoyo:true,repeat:1}},{s1:.3f});')
                sfx.append(("pop", s0)); sfx.append(("hit", s1))
            elif k == "call":
                caller, a = it[1], it[2]; s0 = max(t, at(a) - .1)
                els.append(f'<div id="{eid}" class="clip call" data-start="{s0:.3f}" data-duration="{end - s0:.3f}">'
                           f'<div class="ctop">INCOMING VIDEO CALL</div><div class="avatar" id="{eid}a">?</div><div class="cname">{esc(caller)}</div>'
                           f'<div class="cbtns"><span class="b red">&#x2715;</span><span class="b green">&#x2713;</span></div></div>')
                js.append(f'tl.fromTo("#{eid}",{{y:200,opacity:0}},{{y:0,opacity:1,duration:.35,ease:"power3.out"}},{s0:.3f});')
                n = int((end - s0) / .6)
                for j in range(n):
                    js.append(f'tl.fromTo("#{eid}a",{{boxShadow:"0 0 0 0 rgba(255,80,70,.8)"}},{{boxShadow:"0 0 0 46px rgba(255,80,70,0)",duration:.55}},{s0 + .3 + j * .6:.3f});')
                sfx.append(("whoosh", s0))
            elif k == "stamp":
                txt, col, a = it[1], COLORS[it[2]], it[3]; s0 = at(a)
                els.append(f'<div id="{eid}" class="clip stamp" style="color:{col};border-color:{col}" data-start="{s0:.3f}" data-duration="{end - s0:.3f}">{esc(txt)}</div>')
                js.append(f'tl.fromTo("#{eid}",{{scale:3,opacity:0,rotation:-25}},{{scale:1,opacity:1,rotation:-12,duration:.22,ease:"power4.in"}},{s0:.3f});')
                sfx.append(("hit", s0 + .2))
            elif k == "badges":
                texts, ats = it[1], it[2]
                for j, (tx, a) in enumerate(zip(texts, ats)):
                    uid += 1; bid = f"e{uid}"; s0 = at(a); y = 590 + j * 170
                    els.append(f'<div id="{bid}" class="clip badge" style="top:{y}px" data-start="{s0:.3f}" data-duration="{end - s0:.3f}">{esc(tx)}<span class="x" id="{bid}x">&#x2715; VIDEO CALL ARREST</span></div>')
                    js.append(f'tl.fromTo("#{bid}",{{x:-700,opacity:0}},{{x:0,opacity:1,duration:.3,ease:"power3.out"}},{s0:.3f});')
                    js.append(f'tl.fromTo("#{bid}x",{{scale:0,opacity:0}},{{scale:1,opacity:1,duration:.22,ease:"back.out(3)"}},{s0 + .35:.3f});')
                    sfx.append(("pop", s0))
            elif k == "dial":
                digits, ats = it[1], it[2]; s0 = max(t, at(ats[0]) - .3)
                els.append(f'<div id="{eid}" class="clip dial" data-start="{s0:.3f}" data-duration="{end - s0:.3f}"><div class="screen">' +
                           "".join(f'<span id="{eid}d{j}">{esc(c)}</span>' for j, c in enumerate(digits)) + '</div><div class="callbtn">CALL</div></div>')
                js.append(f'tl.fromTo("#{eid}",{{scale:.7,opacity:0}},{{scale:1,opacity:1,duration:.3,ease:"back.out(2)"}},{s0:.3f});')
                for j, a in enumerate(ats):
                    js.append(f'tl.fromTo("#{eid}d{j}",{{opacity:0,y:30}},{{opacity:1,y:0,duration:.12}},{at(a):.3f});')
                    sfx.append(("tick", at(a)))
            elif k == "buttons":
                labels, a = it[1], it[2]; s0 = at(a)
                els.append(f'<div id="{eid}" class="clip btns" data-start="{s0:.3f}" data-duration="{end - s0:.3f}">' +
                           "".join(f'<span class="bt" id="{eid}b{j}">{esc(x)}</span>' for j, x in enumerate(labels)) + '</div>')
                for j in range(len(labels)):
                    js.append(f'tl.fromTo("#{eid}b{j}",{{scale:0}},{{scale:1,duration:.3,ease:"back.out(3)"}},{s0 + j * .15:.3f});')
                sfx.append(("pop", s0))
            elif k == "chip":
                txt, a = it[1], it[2]; s0 = at(a)
                els.append(f'<div id="{eid}" class="clip chip" data-start="{s0:.3f}" data-duration="{end - s0:.3f}">{esc(txt)}</div>')
                js.append(f'tl.fromTo("#{eid}",{{opacity:0,y:20}},{{opacity:1,y:0,duration:.25}},{s0:.3f});')
        t = end
    TOTAL = t
    # ---- captions: groups of <=3 words, active word gold ----
    gid = 0
    for words, wt, hi in caps_all:
        groups, cur = [], []
        for i, w in enumerate(words):
            cur.append(i)
            pause = i + 1 < len(words) and wt[i + 1][0] - wt[i][1] > .15
            if len(cur) == 3 or pause or w[-1] in ".?!," or i == len(words) - 1:
                groups.append(cur); cur = []
        for gi, g in enumerate(groups):
            gid += 1; s0 = wt[g[0]][0] - .05; e0 = wt[g[-1]][1] + .08
            if gi + 1 < len(groups): e0 = min(e0, wt[groups[gi + 1][0]][0] - .06)
            if g is groups[-1]: e0 = max(e0, wt[g[-1]][1] + .15)
            spans = "".join(f'<span id="c{gid}w{j}">{esc(words[i])}</span>' for j, i in enumerate(g))
            els.append(f'<div id="c{gid}" class="clip cap" data-start="{s0:.3f}" data-duration="{e0 - s0:.3f}">{spans}</div>')
            js.append(f'tl.fromTo("#c{gid}",{{y:24,opacity:0}},{{y:0,opacity:1,duration:.1}},{s0:.3f});')
            js.append(f'tl.set("#c{gid}",{{opacity:0,visibility:"hidden"}},{e0 - .01:.3f});')
            for j, i in enumerate(g):
                js.append(f'tl.to("#c{gid}w{j}",{{color:"{GOLD}",scale:1.12,duration:.06}},{wt[i][0]:.3f});')
                js.append(f'tl.to("#c{gid}w{j}",{{color:"#FFFFFF",scale:1,duration:.06}},{wt[i][1]:.3f});')
    # ---- loop frame: last 0.3 s shows frame-0 headline again is handled by END_HOLD + first items ----
    disc = esc(ns.get("DISCLAIMER", "Educational only. Not financial advice."))
    page = f"""<!doctype html>
<html lang="en"><head><meta charset="UTF-8"/><meta name="viewport" content="width={W}, height={H}"/>
<script src="assets/gsap.min.js"></script>
<style>
:root{{--ground:#1a0f33;--ink:#fff;--font-display:"Poppins";}}
*{{margin:0;padding:0;box-sizing:border-box}}
html,body{{width:{W}px;height:{H}px;overflow:hidden;background:var(--ground)}}
#root{{position:relative;width:100%;height:100%;font-family:"Poppins";font-weight:700;color:#fff;
  background:radial-gradient(1200px 900px at 50% 38%,#3b1f7a 0%,#1a0f33 60%,#0d0820 100%)}}
.grid{{position:absolute;inset:0;background-image:linear-gradient(rgba(255,255,255,.05) 2px,transparent 2px),linear-gradient(90deg,rgba(255,255,255,.05) 2px,transparent 2px);background-size:90px 90px}}
.topic{{position:absolute;top:190px;left:0;right:0;text-align:center}}
.topic span{{background:{RED};color:#fff;font-size:36px;padding:8px 24px;border-radius:14px;letter-spacing:2px}}
.brand{{position:absolute;top:196px;left:48px;font-size:26px;color:{GOLD};opacity:.9}}
.head{{position:absolute;left:0;right:0;text-align:center;line-height:1.1;text-shadow:0 6px 0 #0d0820,0 0 30px rgba(0,0,0,.6);padding:0 40px;z-index:5}}
.card{{position:absolute;left:140px;top:540px;width:800px;height:560px;border-radius:36px;overflow:hidden;border:6px solid {GOLD};box-shadow:0 30px 80px rgba(0,0,0,.6);z-index:2}}
.card img{{width:100%;height:100%;object-fit:cover;object-position:50% 35%}}
.counter{{position:absolute;left:0;right:0;top:640px;text-align:center;font-size:150px;color:{RED};text-shadow:0 8px 0 #0d0820;z-index:6}}
.call{{position:absolute;left:210px;top:540px;width:660px;height:560px;border-radius:48px;background:linear-gradient(#2b2b38,#121218);border:4px solid #444;z-index:3;text-align:center;padding-top:40px}}
.ctop{{font-size:30px;color:#bbb;letter-spacing:3px}}
.avatar{{width:190px;height:190px;border-radius:50%;background:#555;margin:36px auto 24px;font-size:120px;line-height:200px;color:#ddd}}
.cname{{font-size:52px}}
.cbtns{{margin-top:44px;display:flex;justify-content:space-around}}
.cbtns .b{{width:120px;height:120px;border-radius:50%;font-size:64px;line-height:120px}}
.red{{background:{RED}}} .green{{background:#2ecc71}}
.stamp{{position:absolute;left:0;right:0;margin:auto;top:800px;width:640px;text-align:center;font-size:120px;border:12px solid;border-radius:20px;z-index:8;background:rgba(13,8,32,.55)}}
.badge{{position:absolute;left:120px;width:840px;height:140px;border-radius:30px;background:#2a1b55;border:4px solid {TEAL};font-size:64px;line-height:142px;padding-left:40px;z-index:4}}
.badge .x{{position:absolute;right:30px;top:0;font-size:30px;color:{RED}}}
.dial{{position:absolute;left:240px;top:540px;width:600px;height:560px;border-radius:48px;background:#121218;border:4px solid {TEAL};z-index:4;text-align:center}}
.dial .screen{{font-size:170px;color:#fff;margin-top:90px;letter-spacing:12px;height:220px}}
.dial .callbtn{{margin:60px auto 0;width:360px;height:120px;border-radius:60px;background:#2ecc71;font-size:56px;line-height:120px}}
.btns{{position:absolute;left:0;right:0;top:820px;display:flex;justify-content:center;gap:60px;z-index:6}}
.bt{{display:inline-block;width:340px;height:170px;border-radius:40px;font-size:90px;line-height:170px;background:{GOLD};color:#1a0f33}}
.bt+.bt{{background:{TEAL}}}
.chip{{position:absolute;left:0;right:0;top:1230px;margin:auto;width:fit-content;max-width:960px;text-align:center;font-size:30px;font-weight:600;background:rgba(0,0,0,.55);padding:10px 22px;border-radius:14px;color:#eee;z-index:7}}
.cap{{position:absolute;left:0;right:0;top:1135px;text-align:center;font-size:66px;line-height:1.2;text-shadow:0 5px 0 #000,0 0 18px #000;z-index:9;padding:0 50px}}
.cap span{{display:inline-block;margin:0 12px}}
.disc{{position:absolute;left:0;right:0;top:1305px;text-align:center;font-size:24px;font-weight:600;color:rgba(255,255,255,.75)}}
</style></head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="{TOTAL:.3f}" data-width="{W}" data-height="{H}">
<div class="grid"></div>
<div class="brand">PAISA SCIENCE</div>
<div class="topic"><span>{esc(TOPIC)}</span></div>
{chr(10).join(els)}
<div class="disc">{disc}</div>
<audio id="mix" class="clip" src="assets/mix.wav" data-start="0" data-duration="{TOTAL:.3f}" data-volume="1"></audio>
</div>
<script>
const tl = gsap.timeline({{paused:true}});
{chr(10).join(js)}
tl.fromTo(".grid",{{backgroundPosition:"0px 0px"}},{{backgroundPosition:"0px 540px",duration:{TOTAL:.3f},ease:"none"}},0);
tl.set({{}},{{}},{TOTAL:.3f});
window.__timelines["main"] = tl;
tl.seek(0);
</script></body></html>"""
    open(f"{hf}/index.html", "w").write(page)
    # ---- audio mix: voice + music bed (ducked) + sfx ----
    N = int(TOTAL * SR) + SR
    vo = np.zeros(N)
    for t0, p in voice:
        a = read_wav(p); s = int(t0 * SR); vo[s:s + len(a)] += a[:N - s]
    def tone(f, d, dec, g):
        tt = np.arange(int(d * SR)) / SR; return np.sin(2 * np.pi * f * tt) * np.exp(-tt * dec) * g
    rng = np.random.default_rng(5)
    def noise(d, dec, g, lp=1):
        n = rng.standard_normal(int(d * SR)); n = np.convolve(n, np.ones(lp) / lp, "same"); tt = np.arange(len(n)) / SR
        return n * np.exp(-tt * dec) * g
    fx = np.zeros(N)
    for kind, t0 in sfx:
        s = int(t0 * SR)
        if kind == "pop": sig = tone(1320, .15, 30, .09) + tone(2640, .15, 45, .04)
        elif kind == "hit":
            sig = tone(90, .35, 9, .35); nz = noise(.12, 30, .08, 4); sig[:len(nz)] += nz
        elif kind == "tick": sig = tone(2200, .05, 80, .07)
        else: sig = noise(.35, 7, .05, 30) * np.sin(np.linspace(0, np.pi, int(.35 * SR)))
        e = min(N, s + len(sig)); fx[s:e] += sig[:e - s]
    tmp = f"{pdir}/_tmp"; os.makedirs(tmp, exist_ok=True)
    cuts = ",".join(f"{L['_t']:.2f}" for L in LINES[1:])
    subprocess.run([sys.executable, f"{HERE}/music.py", f"{tmp}/m.wav", f"{TOTAL:.3f}", cuts], check=True)
    sf = wave.open(f"{tmp}/m.wav"); m = np.frombuffer(sf.readframes(sf.getnframes()), np.int16).reshape(-1, 2).astype(np.float32) / 32767
    music = np.zeros((N, 2)); music[:min(N, len(m))] = m[:N]
    env = np.convolve(np.abs(vo), np.ones(int(.25 * SR)) / int(.25 * SR), "same")
    duck = np.convolve(np.where(env > .01, .22, .55), np.ones(int(.3 * SR)) / int(.3 * SR), "same")
    mix = music * duck[:, None] * .5 + (vo + fx)[:, None]
    mix /= max(1e-6, np.abs(mix).max()) / .9
    with wave.open(f"{tmp}/raw.wav", "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes((mix * 32767).astype(np.int16).tobytes())
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", f"{tmp}/raw.wav", "-af", "loudnorm=I=-14:TP=-1.5:LRA=11", "-ar", str(SR), f"{hf}/assets/mix.wav"], check=True)
    json.dump({str(L["id"]): dict(t=round(L["_t"], 3), d=round(L["_d"], 3), words=list(zip(L["cap"].split(), [w[0] for w in L["_wt"]]))) for L in LINES},
              open(f"{pdir}/timing.json", "w"), ensure_ascii=False, indent=0)
    print(f"total {TOTAL:.2f}s; html {hf}/index.html")
    q = "draft" if preview else "delivery"
    r = subprocess.run(["npx", "--yes", "hyperframes@0.9.52", "render", ".", "-o", os.path.abspath(out), "-q", q, "--quiet"], cwd=hf)
    if r.returncode: sys.exit("render failed")
    print("done", out)


if __name__ == "__main__":
    build(sys.argv[1], sys.argv[2], "--preview" in sys.argv)
