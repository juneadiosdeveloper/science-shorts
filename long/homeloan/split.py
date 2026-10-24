import subprocess, re, sys, json
def sil(p, db=-38, d=0.12):
    o = subprocess.run(["ffmpeg","-i",p,"-af",f"silencedetect=noise={db}dB:d={d}","-f","null","-"],capture_output=True,text=True).stderr
    s = [float(x) for x in re.findall(r"silence_start: ([\d.]+)", o)]; e = [float(x) for x in re.findall(r"silence_end: ([\d.]+)", o)]
    return list(zip(s, e))
def dur(p): return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",p],capture_output=True,text=True).stdout)
p, n = sys.argv[1], int(sys.argv[2])
S = [x for x in sil(p) if x[0] > 0.05 and x[1] < dur(p) - 0.05]
top = sorted(S, key=lambda x: x[1]-x[0], reverse=True)[:n-1]
top.sort()
print("gap durations (sorted by time):", [round(b-a,2) for a,b in top])
print("smallest chosen", round(min(b-a for a,b in top),3), "largest unchosen", round(max([b-a for a,b in S if (a,b) not in top] or [0]),3))
cuts = [(a+b)/2 for a,b in top]
bounds = [0]+cuts+[dur(p)]
json.dump(bounds, open(sys.argv[3],"w"))
print([round(bounds[i+1]-bounds[i],2) for i in range(len(bounds)-1)])
