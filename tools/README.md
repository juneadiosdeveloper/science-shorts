# Paisa Science toolkit

- `paisa.py`: video template + the scenes and scripts for each Short (`sip`, `card`, `infl`)
- `music.py`: background music and sound effects (`music.py out.wav <seconds> <cut times>`)
- `voice/make_with_voice.py <video> <recording> <out.mp4>`: cleans Junaid's recording, syncs scenes to his lines, renders the final Short
- `voice/clean_voice.py`: noise removal (spectral gate + RNNoise `sh.rnnn`), EQ, de-ess, compression, -16 LUFS
- `build.py`: AI-voice fallback (needs the Kokoro model files in `kokoro/`)
- `brand.py`: logo and banner

Setup on a fresh machine: `pip install noisereduce soundfile pillow numpy kokoro-onnx` and ffmpeg.
- `long_sip.py`: 16:9 long-video template (chapters, narration-synced reveals, title cards). `python3 long_sip.py voice | stills out.png | chapter <i> out.mp4`. Expects `kokoro/` next to it. Render chapters 2 at a time (2 CPU cores), concat, then run music.py.
- Junaid's voice for long videos: put his chapter recordings in a folder as ch0.<ext> ... ch9.<ext>, then `python3 long_sip.py voice_rec <folder>` (cleans each file, splits it into lines at the pauses, writes long_vo.wav + long_timing.json), then render chapters as usual.
- `recording_script.md`: the scripts Junaid reads (one numbered line per narration line, 1-second pause between lines).
