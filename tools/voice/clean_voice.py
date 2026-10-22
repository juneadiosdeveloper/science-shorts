"""Clean a phone voice recording for narration.
usage: python3 clean_voice.py <input audio (m4a/ogg/opus/mp3/wav)> <output.wav>
Chain: 48 kHz mono -> spectral-gate denoise -> RNNoise -> EQ (rumble cut, mud cut,
presence + air lift) -> de-ess -> compress -> loudness normalise (-16 LUFS, -1.5 dBTP).
"""
import subprocess, sys, os, tempfile
import numpy as np, soundfile as sf, noisereduce as nr

HERE = os.path.dirname(os.path.abspath(__file__))
src, out = sys.argv[1], sys.argv[2]
tmp = tempfile.mkdtemp()
raw, gated = f"{tmp}/raw.wav", f"{tmp}/gated.wav"

subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", src, "-ac", "1", "-ar", "48000", raw], check=True)
y, sr = sf.read(raw)
# 1. spectral gating: learns the noise floor from the quietest 10% of frames
y = nr.reduce_noise(y=y, sr=sr, stationary=True, prop_decrease=0.85, n_fft=2048)
sf.write(gated, y, sr)

# 2-6. neural denoise + broadcast voice chain
chain = ",".join([
    f"arnndn=m={HERE}/sh.rnnn:mix=0.85",
    "highpass=f=80", "lowpass=f=15000",
    "equalizer=f=250:t=q:w=1.2:g=-2.5",    # less boxy / muddy
    "equalizer=f=3500:t=q:w=1.0:g=3",      # presence: clearer words
    "equalizer=f=10000:t=q:w=1.0:g=2",     # air
    "deesser=i=0.4",
    "acompressor=threshold=-20dB:ratio=3:attack=10:release=150:makeup=2",
    "loudnorm=I=-16:TP=-1.5:LRA=7",
])
subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", gated, "-af", chain, "-ar", "48000", out], check=True)
print("cleaned ->", out)
