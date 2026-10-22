# Paisa Science toolkit

- `paisa.py`: video template + the scenes and scripts for each Short (`sip`, `card`, `infl`)
- `music.py`: background music and sound effects (`music.py out.wav <seconds> <cut times>`)
- `voice/make_with_voice.py <video> <recording> <out.mp4>`: cleans Junaid's recording, syncs scenes to his lines, renders the final Short
- `voice/clean_voice.py`: noise removal (spectral gate + RNNoise `sh.rnnn`), EQ, de-ess, compression, -16 LUFS
- `build.py`: AI-voice fallback (needs the Kokoro model files in `kokoro/`)
- `brand.py`: logo and banner

Setup on a fresh machine: `pip install noisereduce soundfile pillow numpy kokoro-onnx` and ffmpeg.
