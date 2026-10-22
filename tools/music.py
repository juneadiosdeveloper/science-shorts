import numpy as np, wave, sys
SR = 44100; DUR = float(sys.argv[2]) if len(sys.argv) > 2 else 30.0; N = int(SR * DUR)
CUTS = [float(c) for c in sys.argv[3].split(',')] if len(sys.argv) > 3 else None
t = np.arange(N) / SR
out = np.zeros((N, 2))

def note(f): return 440 * 2 ** ((f - 69) / 12)
def env(n, a, r):
    e = np.ones(n); ai = int(a * SR); ri = int(r * SR)
    if ai: e[:ai] = np.linspace(0, 1, ai)
    if ri: e[-ri:] *= np.linspace(1, 0, ri)
    return e
def add(sig, start, pan=0.0, gain=1.0):
    s = max(0, int(start * SR)); e = min(N, s + len(sig))
    if e <= s: return
    sig = sig[:e - s] * gain
    out[s:e, 0] += sig * (1 - pan) / 2 * 2 ** .5 * .7
    out[s:e, 1] += sig * (1 + pan) / 2 * 2 ** .5 * .7

BPM = 96; beat = 60 / BPM; bar = 4 * beat
# C - G - Am - F, (midi roots)
prog = [[60, 64, 67], [55, 59, 62, 67], [57, 60, 64], [53, 57, 60, 65]]
nb = int(DUR / bar) + 1
for b in range(nb):
    ch = prog[b % 4]; st = b * bar
    # warm pad
    n = int(bar * SR * 1.05); tt = np.arange(n) / SR
    pad = sum(np.sin(2 * np.pi * note(m) * tt + .3 * np.sin(2 * np.pi * .5 * tt)) +
              .3 * np.sin(2 * np.pi * note(m) * 2.003 * tt) for m in ch)
    add(pad * env(n, .6, .6), st, gain=.045)
    # bass
    n = int(bar * SR); tt = np.arange(n) / SR
    bass = np.sin(2 * np.pi * note(ch[0] - 24) * tt) * np.exp(-tt * 1.2)
    add(bass, st, gain=.22)
    # pluck arpeggio (8th notes) from 4s onward
    if st >= 3.9:
        arp = ch + [ch[0] + 12]
        for k in range(8):
            m = arp[[0, 1, 2, 3, 2, 1, 2, 3][k]] + 12
            n = int(.5 * SR); tt = np.arange(n) / SR
            pl = (np.sin(2 * np.pi * note(m) * tt) + .4 * np.sin(4 * np.pi * note(m) * tt)) * np.exp(-tt * 9)
            add(pl, st + k * beat / 2, pan=(-.4 if k % 2 else .4), gain=.08)
    # soft kick + hat from 10s
    if (st >= 9.9 and st < 27) if CUTS is None else (st >= CUTS[1] - .1 and st < CUTS[-1]):
        for k in range(4):
            n = int(.25 * SR); tt = np.arange(n) / SR
            kick = np.sin(2 * np.pi * (50 + 90 * np.exp(-tt * 30)) * tt) * np.exp(-tt * 14)
            add(kick, st + k * beat, gain=.35)
            hat = np.random.default_rng(k).standard_normal(int(.05 * SR)) * np.exp(-np.arange(int(.05 * SR)) / SR * 80)
            add(np.diff(hat, prepend=0), st + k * beat + beat / 2, pan=.3, gain=.05)

# whoosh at scene changes
rng = np.random.default_rng(1)
for ts in ([4, 10, 17, 23, 27] if CUTS is None else CUTS):
    n = int(.7 * SR); tt = np.arange(n) / SR
    noise = rng.standard_normal(n)
    # crude band sweep: smoothed noise with moving average width shrinking
    sm = np.convolve(noise, np.ones(8) / 8, 'same')
    w = np.sin(np.pi * tt / .7) ** 2
    add(sm * w, ts - .35, pan=np.sin(ts), gain=.12)
# pops for text reveals
for ts in ([0.4, 0.9, 1.4, 2.0, 4.6, 5.8, 10.4, 17.1, 17.6, 19.8, 23.5, 27.1, 27.6, 28.3] if CUTS is None else [0.4] + [c + .15 for c in CUTS]):
    n = int(.15 * SR); tt = np.arange(n) / SR
    pop = np.sin(2 * np.pi * (900 - 500 * tt / .15) * tt) * np.exp(-tt * 35)
    add(pop, ts, gain=.18)
# shimmer on prism split & final title
for ts in ([5.3, 27.4] if CUTS is None else [CUTS[-1] + .35]):
    for i, m in enumerate([84, 88, 91, 96, 100]):
        n = int(1.2 * SR); tt = np.arange(n) / SR
        add(np.sin(2 * np.pi * note(m) * tt) * np.exp(-tt * 3), ts + i * .07, pan=-.6 + .3 * i, gain=.05)

# master fade
fade = np.ones(N); fade[:int(.3 * SR)] = np.linspace(0, 1, int(.3 * SR)); fade[-int(1.5 * SR):] *= np.linspace(1, 0, int(1.5 * SR))
out *= fade[:, None]
out = np.tanh(out * 1.2); out /= np.abs(out).max() / .89
pcm = (out * 32767).astype(np.int16)
with wave.open(sys.argv[1], 'wb') as w:
    w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm.tobytes())
