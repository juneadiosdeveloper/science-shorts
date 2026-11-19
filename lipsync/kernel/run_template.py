# Kaggle GPU kernel: LatentSync 1.5 lip-sync. Job values are filled in by lipsync/submit.py.
import os, subprocess, sys, urllib.request, shutil, time
JOB = "__JOB__"
VIDEO_URL = "__VIDEO_URL__"
AUDIO_URL = "__AUDIO_URL__"
STEPS = int("__STEPS__")
GUIDE = float("__GUIDE__")
def sh(c):
    print("+", c, flush=True); r = subprocess.run(c, shell=True)
    if r.returncode: raise SystemExit(f"failed: {c}")
t0 = time.time()
sh("nvidia-smi || true")
sh("git clone -q --depth 1 https://github.com/bytedance/LatentSync /kaggle/temp/LS")
os.chdir("/kaggle/temp/LS")
sh("apt-get -qq install -y ffmpeg >/dev/null 2>&1 || true")
sh("pip install -q uv")
sh("uv python install 3.10 -q && uv venv -q --python 3.10 /kaggle/temp/venv")
PY = "/kaggle/temp/venv/bin/python"
sh(f"uv pip install -q --python {PY} -r requirements.txt --index-strategy unsafe-best-match")
sh(f"{PY} -m pip --version || uv pip install -q --python {PY} pip")
sh(f"/kaggle/temp/venv/bin/huggingface-cli download ByteDance/LatentSync-1.5 whisper/tiny.pt --local-dir checkpoints")
sh(f"/kaggle/temp/venv/bin/huggingface-cli download ByteDance/LatentSync-1.5 latentsync_unet.pt --local-dir checkpoints")
urllib.request.urlretrieve(VIDEO_URL, "in_video.mp4"); urllib.request.urlretrieve(AUDIO_URL, "in_audio.wav")
sh(f"{PY} -m scripts.inference --unet_config_path configs/unet/stage2.yaml --inference_ckpt_path checkpoints/latentsync_unet.pt "
   f"--inference_steps {STEPS} --guidance_scale {GUIDE} --enable_deepcache --video_path in_video.mp4 --audio_path in_audio.wav "
   f"--video_out_path /kaggle/working/{JOB}_out.mp4")
open(f"/kaggle/working/{JOB}_done.txt","w").write(f"ok {time.time()-t0:.0f}s\n")
print("DONE", time.time()-t0)
