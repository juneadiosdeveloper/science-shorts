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
sh("pip install -q diffusers==0.32.2 transformers==4.48.0 decord==0.6.0 accelerate==0.26.1 einops==0.7.0 omegaconf==2.3.0 "
   "mediapipe==0.10.11 python_speech_features==0.6 scenedetect==0.6.1 ffmpeg-python==0.2.0 face-alignment==1.4.1 "
   "kornia==0.8.0 insightface==0.7.3 onnxruntime-gpu DeepCache==0.1.1 lpips==0.1.4 'huggingface-hub==0.30.2' 'numpy<2'")
sh("huggingface-cli download ByteDance/LatentSync-1.5 whisper/tiny.pt --local-dir checkpoints")
sh("huggingface-cli download ByteDance/LatentSync-1.5 latentsync_unet.pt --local-dir checkpoints")
urllib.request.urlretrieve(VIDEO_URL, "in_video.mp4"); urllib.request.urlretrieve(AUDIO_URL, "in_audio.wav")
sh(f"python -m scripts.inference --unet_config_path configs/unet/stage2.yaml --inference_ckpt_path checkpoints/latentsync_unet.pt "
   f"--inference_steps {STEPS} --guidance_scale {GUIDE} --enable_deepcache --video_path in_video.mp4 --audio_path in_audio.wav "
   f"--video_out_path /kaggle/working/{JOB}_out.mp4")
open(f"/kaggle/working/{JOB}_done.txt","w").write(f"ok {time.time()-t0:.0f}s\n")
print("DONE", time.time()-t0)
