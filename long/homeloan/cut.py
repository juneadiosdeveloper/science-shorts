import json, subprocess
exec(open('lines.py').read())
def words(f):
    d = json.load(open(f)); w = d["words"] if isinstance(d, dict) else d
    return [x for x in w if x.get("type", "word") == "word"]
out = {}
for spk, raw, wf in (("PL", "audio/p_raw.mp3", "audio/p_words.json"), ("G", "audio/g_raw.mp3", "audio/g_words.json")):
    W = words(wf); i = 0
    L = [l for l in LINES if l[1] in spk]
    for k, l in enumerate(L):
        n = len(l[2].split())
        seg = W[i:i+n]; i += n
        assert seg[0]["text"] == l[2].split()[0] and seg[-1]["text"] == l[2].split()[-1], (l[0], seg[0]["text"], seg[-1]["text"])
        a = max(0, seg[0]["start"] - 0.04); b = seg[-1]["end"] + 0.10
        if k + 1 < len(L): b = min(b, W[i]["start"] - 0.02)
        subprocess.run(["ffmpeg","-loglevel","error","-y","-ss",f"{a:.3f}","-to",f"{b:.3f}","-i",raw,"-ar","44100","-ac","1",f"audio/l{l[0]:02d}.wav"],check=True)
        out[l[0]] = round(b - a, 3)
    assert i == len(W), (spk, i, len(W))
json.dump(out, open("audio/durs.json","w"), indent=0)
print(out, sum(out.values()))
