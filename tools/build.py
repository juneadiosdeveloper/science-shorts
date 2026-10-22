import sys, subprocess, numpy as np, soundfile as sf
from kokoro_onnx import Kokoro
import paisa
name, out = sys.argv[1], sys.argv[2]
k = Kokoro("kokoro/kokoro-v1.0.onnx", "kokoro/voices-v1.0.bin"); V = "hf_alpha"; SR = 24000
buf = np.zeros(int(30 * SR), dtype=np.float32)
for st, en, txt in paisa.VIDEOS[name][1]:
    win = en - st - .2; sp = 1.05
    a, _ = k.create(txt, voice=V, speed=sp, lang="hi")
    if len(a) / SR > win:
        sp = sp * len(a) / SR / win; a, _ = k.create(txt, voice=V, speed=min(sp, 1.45), lang="hi")
    idx = np.where(np.abs(a) > .01)[0]; a = a[max(0, idx[0] - 200): idx[-1] + 2000]
    s = int(st * SR); buf[s:s + len(a)] += a[:len(buf) - s]
    print(f"{name} {st:5.2f}-{st + len(a) / SR:5.2f} (limit {en}) speed {sp:.2f}")
buf /= np.abs(buf).max() / .95; sf.write(f"{name}_vo.wav", buf, SR)
