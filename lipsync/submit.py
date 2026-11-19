"""Run pending lip-sync jobs on Kaggle's free GPU and save the results in the repo.
A job is lipsync/jobs/<id>/ with video.mp4 + audio.wav (+ optional job.json {"steps":20,"guidance":1.5}).
Result: lipsync/jobs/<id>/out.mp4 and log.txt."""
import json, os, re, subprocess, sys, time, pathlib
ROOT = pathlib.Path(__file__).resolve().parent
REPO = os.environ.get("GITHUB_REPOSITORY", "juneadiosdeveloper/science-shorts")
BRANCH = os.environ.get("GITHUB_REF_NAME", "main")
def run(c, check=True):
    print("+", " ".join(c) if isinstance(c, list) else c, flush=True)
    r = subprocess.run(c, shell=isinstance(c, str), capture_output=True, text=True)
    print(r.stdout[-3000:], r.stderr[-3000:], flush=True)
    if check and r.returncode: raise SystemExit(f"failed ({r.returncode})")
    return r
def username():
    r = run("kaggle config view", check=False)
    m = re.search(r"username:\s*(\S+)", r.stdout)
    if m and m.group(1) not in ("None", ""): return m.group(1)
    r = run("kaggle kernels list --mine --csv --page-size 5", check=False)
    for line in r.stdout.splitlines()[1:]:
        if "/" in line: return line.split("/")[0]
    u = os.environ.get("KAGGLE_USERNAME")
    if u: return u
    raise SystemExit("could not find Kaggle username; set KAGGLE_USERNAME in secrets")
def main():
    jobs = [d for d in sorted((ROOT / "jobs").iterdir()) if d.is_dir() and (d / "video.mp4").exists()
            and (d / "audio.wav").exists() and not (d / "out.mp4").exists() and not (d / "failed.txt").exists()]
    if not jobs: print("no pending jobs"); return
    user = username(); print("kaggle user:", user)
    tpl = (ROOT / "kernel" / "run_template.py").read_text()
    for d in jobs:
        jid = re.sub(r"[^a-z0-9-]", "-", d.name.lower())
        cfg = json.loads((d / "job.json").read_text()) if (d / "job.json").exists() else {}
        raw = f"https://raw.githubusercontent.com/{REPO}/{BRANCH}/lipsync/jobs/{d.name}"
        code = (tpl.replace("__JOB__", jid).replace("__VIDEO_URL__", raw + "/video.mp4").replace("__AUDIO_URL__", raw + "/audio.wav")
                   .replace("__STEPS__", str(cfg.get("steps", 20))).replace("__GUIDE__", str(cfg.get("guidance", 1.5))))
        kd = pathlib.Path("/tmp/kern") / jid; kd.mkdir(parents=True, exist_ok=True)
        (kd / "run.py").write_text(code)
        slug = f"lipsync-{jid}"[:50]
        (kd / "kernel-metadata.json").write_text(json.dumps({"id": f"{user}/{slug}", "title": slug, "code_file": "run.py",
            "language": "python", "kernel_type": "script", "is_private": True, "enable_gpu": True, "enable_internet": True,
            "machine_shape": "NvidiaTeslaT4", "dataset_sources": [], "competition_sources": [], "kernel_sources": []}))
        run(["kaggle", "kernels", "push", "-p", str(kd)])
        status = ""
        for _ in range(110):  # up to ~55 min
            time.sleep(30)
            st = run(["kaggle", "kernels", "status", f"{user}/{slug}"], check=False).stdout
            status = st.strip().split()[-1].strip('"').lower() if st.strip() else ""
            if any(k in st.lower() for k in ("complete", "error", "cancel")): break
        out = pathlib.Path("/tmp/out") / jid; out.mkdir(parents=True, exist_ok=True)
        run(["kaggle", "kernels", "output", f"{user}/{slug}", "-p", str(out)], check=False)
        log = "\n".join(p.read_text(errors="ignore")[-20000:] for p in out.glob("*.log"))
        (d / "log.txt").write_text(f"status: {status}\n{log}")
        res = list(out.glob("*_out.mp4"))
        if res: res[0].rename(d / "out.mp4")
        else: (d / "failed.txt").write_text(f"status: {status}\n")
if __name__ == "__main__": main()
