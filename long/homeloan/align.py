import subprocess, re, sys, json
exec(open('lines.py').read())
def sil(p, db=-38, d=0.10):
    o = subprocess.run(["ffmpeg","-i",p,"-af",f"silencedetect=noise={db}dB:d={d}","-f","null","-"],capture_output=True,text=True).stderr
    s = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", o)]; e = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", o)]
    return list(zip(s, e))
def dur(p): return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",p],capture_output=True,text=True).stdout)
p, spk, out = sys.argv[1], sys.argv[2], sys.argv[3]
L = [l for l in LINES if l[1] in spk]
ch = [len(l[2]) for l in L]
D = dur(p); S = [x for x in sil(p) if 0.05 < x[0] and x[1] < D - 0.05]
a = (D - 0.35*(len(L)-1)) / sum(ch)
cand = [(x[0]+x[1])/2 for x in S]; gl = [x[1]-x[0] for x in S]
pts = [0.0] + cand + [D]; g = [9] + gl + [9]
n, m = len(L), len(pts)
INF = 1e18
best = [[INF]*m for _ in range(n+1)]; prev = [[-1]*m for _ in range(n+1)]
best[0][0] = 0
for i in range(1, n+1):
    pred = a*ch[i-1]
    for j in range(1, m):
        if i == n and j != m-1: continue
        for k in range(j):
            if best[i-1][k] >= INF: continue
            seg = pts[j]-pts[k]
            c = best[i-1][k] + ((seg-pred)/max(pred,0.8))**2 - (3*g[j] if j < m-1 else 0)
            if c < best[i][j]: best[i][j] = c; prev[i][j] = k
j = m-1; b = [D]
for i in range(n, 0, -1):
    j = prev[i][j]; b.append(pts[j])
b = b[::-1]
json.dump({"ids":[l[0] for l in L],"bounds":b}, open(out,"w"))
for i,l in enumerate(L):
    print(l[0], round(b[i+1]-b[i],2), round(a*ch[i],2), l[2][:30])
