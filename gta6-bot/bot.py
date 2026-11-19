#!/usr/bin/env python3
"""GTA 6 Moments bot.

Each run: pick the most-viewed fresh GTA 6 Twitch clip that is not posted yet,
turn it into a vertical 1080x1920 Short (blurred background, hook text,
word-timed captions, streamer credit) and upload it to YouTube.

Credentials come from secrets.enc (decrypted with the BOT_KEY GitHub secret);
the YouTube refresh token comes from state/yt_token.enc.
"""
import datetime as dt
import json
import os
import re
import subprocess
import sys
import tempfile
from pathlib import Path

import requests
import yaml

HERE = Path(__file__).resolve().parent
STATE = HERE / "state"
POSTED = STATE / "posted.json"
CFG = yaml.safe_load((HERE / "config.yml").read_text())
UA = {"User-Agent": "gta6-moments-bot/1.0"}


# ---------------------------------------------------------------- secrets
def decrypt(path: Path) -> str:
    key = os.environ["BOT_KEY"]
    out = subprocess.run(
        ["openssl", "enc", "-d", "-aes-256-cbc", "-pbkdf2", "-iter", "200000",
         "-base64", "-A", "-pass", "env:BOT_KEY", "-in", str(path)],
        check=True, capture_output=True, env={**os.environ, "BOT_KEY": key})
    return out.stdout.decode()


def load_secrets() -> dict:
    return json.loads(decrypt(HERE / "secrets.enc"))


# ---------------------------------------------------------------- state
def load_posted() -> list:
    return json.loads(POSTED.read_text()) if POSTED.exists() else []


def save_posted(items: list) -> None:
    STATE.mkdir(exist_ok=True)
    POSTED.write_text(json.dumps(items, indent=1, ensure_ascii=False) + "\n")


# ---------------------------------------------------------------- twitch
def twitch_token(s: dict) -> str:
    r = requests.post("https://id.twitch.tv/oauth2/token", data={
        "client_id": s["twitch_client_id"],
        "client_secret": s["twitch_client_secret"],
        "grant_type": "client_credentials"}, timeout=30)
    r.raise_for_status()
    return r.json()["access_token"]


def helix(s, tok, path, params):
    r = requests.get("https://api.twitch.tv/helix/" + path, params=params, timeout=30,
                     headers={"Client-Id": s["twitch_client_id"],
                              "Authorization": "Bearer " + tok})
    r.raise_for_status()
    return r.json()


def game_id(s, tok) -> str:
    for name in CFG["twitch_game_names"]:
        data = helix(s, tok, "games", {"name": name})["data"]
        if data:
            return data[0]["id"]
    data = helix(s, tok, "search/categories", {"query": "Grand Theft Auto VI"})["data"]
    if not data:
        sys.exit("GTA 6 category not found on Twitch")
    return data[0]["id"]


def candidate_clips(s, tok, gid, posted_ids, posted_streamers_today):
    since = dt.datetime.now(dt.timezone.utc) - dt.timedelta(hours=CFG["clip_max_age_hours"])
    params = {"game_id": gid, "first": 100,
              "started_at": since.strftime("%Y-%m-%dT%H:%M:%SZ")}
    clips, cursor = [], None
    for _ in range(3):  # up to 300 clips
        if cursor:
            params["after"] = cursor
        js = helix(s, tok, "clips", params)
        clips += js["data"]
        cursor = js.get("pagination", {}).get("cursor")
        if not cursor:
            break
    allow = {x.lower() for x in CFG.get("allowlist") or []}
    block = {x.lower() for x in CFG.get("blocklist") or []}
    out = []
    for c in clips:
        who = c["broadcaster_name"].lower()
        if c["id"] in posted_ids or who in block:
            continue
        if CFG["require_allowlist"] and who not in allow:
            continue
        if c["view_count"] < CFG["min_clip_views"]:
            continue
        if c["duration"] < CFG["min_clip_seconds"]:
            continue
        if CFG.get("languages") and c.get("language") not in CFG["languages"]:
            continue
        if posted_streamers_today.get(who, 0) >= CFG["max_per_streamer_per_day"]:
            continue
        out.append(c)
    out.sort(key=lambda c: c["view_count"], reverse=True)
    return out


# ---------------------------------------------------------------- text
EMOJI_RE = re.compile(r"[\U00010000-\U0010ffff☀-➿]")


def clean_title(t: str) -> str:
    t = EMOJI_RE.sub("", t)
    t = re.sub(r"\s+", " ", t).strip(" -|.")
    return t or "This GTA 6 moment is insane"


def hook_text(clip) -> str:
    t = clean_title(clip["title"])
    if len(t) > CFG["hook_max_chars"]:
        t = t[: CFG["hook_max_chars"]].rsplit(" ", 1)[0] + "..."
    return t.upper()


def ass_escape(t: str) -> str:
    return t.replace("\\", "").replace("{", "(").replace("}", ")").replace("\n", " ")


def ts(sec: float) -> str:
    sec = max(0.0, sec)
    h, rem = divmod(sec, 3600)
    m, s = divmod(rem, 60)
    return f"{int(h)}:{int(m):02d}:{s:05.2f}"


def build_ass(hook: str, credit: str, words: list, duration: float) -> str:
    head = f"""[Script Info]
ScriptType: v4.00+
PlayResX: 1080
PlayResY: 1920
WrapStyle: 0

[V4+ Styles]
Format: Name, Fontname, Fontsize, PrimaryColour, SecondaryColour, OutlineColour, BackColour, Bold, Italic, Underline, StrikeOut, ScaleX, ScaleY, Spacing, Angle, BorderStyle, Outline, Shadow, Alignment, MarginL, MarginR, MarginV, Encoding
Style: Hook,DejaVu Sans,64,&H00FFFFFF,&H00FFFFFF,&H00000000,&H00000000,-1,0,0,0,100,100,0,0,3,18,0,8,70,70,190,1
Style: Cap,DejaVu Sans,78,&H0000F0FF,&H00FFFFFF,&H00000000,&H64000000,-1,0,0,0,100,100,0,0,1,7,3,2,60,60,430,1
Style: Credit,DejaVu Sans,40,&H00FFFFFF,&H00FFFFFF,&H00000000,&H96000000,-1,0,0,0,100,100,0,0,3,10,0,2,60,60,150,1

[Events]
Format: Layer, Start, End, Style, Name, MarginL, MarginR, MarginV, Effect, Text
"""
    ev = [f"Dialogue: 2,{ts(0)},{ts(duration)},Hook,,0,0,0,,{ass_escape(hook)}",
          f"Dialogue: 2,{ts(0)},{ts(duration)},Credit,,0,0,0,,{ass_escape(credit)}"]
    # captions: chunks of up to 3 words, each shown while it is spoken
    chunk = []
    for w in words + [None]:
        if w is not None:
            chunk.append(w)
        if chunk and (w is None or len(chunk) == 3 or w["word"].rstrip().endswith((".", "?", "!", ","))):
            start, end = chunk[0]["start"], chunk[-1]["end"]
            txt = " ".join(x["word"].strip() for x in chunk).upper()
            ev.append(f"Dialogue: 1,{ts(start)},{ts(max(end, start + 0.25))},Cap,,0,0,0,,{ass_escape(txt)}")
            chunk = []
    return head + "\n".join(ev) + "\n"


# ---------------------------------------------------------------- media
def download(clip, work: Path) -> Path:
    out = work / "clip.mp4"
    subprocess.run(["yt-dlp", "-q", "--no-warnings", "-f", "best[ext=mp4]/best",
                    "-o", str(out), clip["url"]], check=True)
    return out


def probe_duration(p: Path) -> float:
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", str(p)], capture_output=True, text=True, check=True)
    return float(r.stdout.strip())


def transcribe(p: Path) -> list:
    if not CFG["captions"]:
        return []
    try:
        from faster_whisper import WhisperModel
        model = WhisperModel(CFG["whisper_model"], device="cpu", compute_type="int8")
        segs, _ = model.transcribe(str(p), word_timestamps=True, vad_filter=True)
        return [{"word": w.word, "start": w.start, "end": w.end}
                for s in segs for w in (s.words or []) if w.word.strip()]
    except Exception as e:  # captions are a bonus, never block a post
        print("captions skipped:", e)
        return []


def render(src: Path, ass: Path, out: Path) -> None:
    vf = ("[0:v]scale=1080:1920:force_original_aspect_ratio=increase,crop=1080:1920,"
          "boxblur=24:4,eq=brightness=-0.12[bg];"
          "[0:v]scale=1080:-2[fg];"
          f"[bg][fg]overlay=(W-w)/2:(H-h)/2,subtitles={ass}[v]")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", str(src),
                    "-filter_complex", vf, "-map", "[v]", "-map", "0:a?",
                    "-c:v", "libx264", "-preset", "veryfast", "-crf", "20",
                    "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "160k",
                    "-movflags", "+faststart", str(out)], check=True)


# ---------------------------------------------------------------- youtube
def yt_access_token(s: dict) -> str:
    refresh = decrypt(STATE / "yt_token.enc").strip()
    r = requests.post("https://oauth2.googleapis.com/token", data={
        "client_id": s["google_client_id"], "client_secret": s["google_client_secret"],
        "refresh_token": refresh, "grant_type": "refresh_token"}, timeout=30)
    r.raise_for_status()
    return r.json()["access_token"]


def yt_upload(tok: str, path: Path, title: str, desc: str, tags: list) -> str:
    meta = {"snippet": {"title": title, "description": desc, "tags": tags,
                        "categoryId": "20", "defaultLanguage": "en"},
            "status": {"privacyStatus": CFG["privacy"], "selfDeclaredMadeForKids": False}}
    size = path.stat().st_size
    r = requests.post(
        "https://www.googleapis.com/upload/youtube/v3/videos?uploadType=resumable&part=snippet,status",
        headers={"Authorization": "Bearer " + tok, "Content-Type": "application/json",
                 "X-Upload-Content-Type": "video/mp4", "X-Upload-Content-Length": str(size)},
        data=json.dumps(meta), timeout=60)
    r.raise_for_status()
    with open(path, "rb") as f:
        up = requests.put(r.headers["Location"], data=f, timeout=600,
                          headers={"Authorization": "Bearer " + tok, "Content-Type": "video/mp4"})
    up.raise_for_status()
    return up.json()["id"]


def make_title(clip, hook: str) -> str:
    base = clean_title(clip["title"])
    t = f"{base} | {clip['broadcaster_name']} GTA 6 #shorts"
    if len(t) > 100:
        t = f"{base[:100 - 12]} | GTA 6 #shorts"
    return t[:100]


def make_desc(clip) -> str:
    who = clip["broadcaster_name"]
    return (f"{clean_title(clip['title'])}\n\n"
            f"Credit: {who} - watch them live: https://twitch.tv/{clip['broadcaster_name'].lower()}\n"
            f"Original clip: {clip['url']}\n\n"
            "Daily best GTA 6 moments from your favourite streamers. Subscribe for more!\n\n"
            "#GTA6 #GTAVI #GrandTheftAuto6 #Gaming #Shorts #ViceCity\n\n"
            "All gameplay belongs to Rockstar Games. Clip and commentary belong to the streamer credited above.")


# ---------------------------------------------------------------- main
def main() -> None:
    dry = "--dry-run" in sys.argv
    s = load_secrets()
    posted = load_posted()
    today = dt.datetime.now(dt.timezone.utc).date().isoformat()
    todays = [p for p in posted if p["posted_at"].startswith(today)]
    if len(todays) >= CFG["max_per_day"]:
        print(f"daily cap reached ({len(todays)}/{CFG['max_per_day']})")
        return
    per_streamer = {}
    for p in todays:
        per_streamer[p["streamer"].lower()] = per_streamer.get(p["streamer"].lower(), 0) + 1

    tok = twitch_token(s)
    gid = game_id(s, tok)
    clips = candidate_clips(s, tok, gid, {p["clip_id"] for p in posted}, per_streamer)
    print(f"GTA 6 game id {gid}; {len(clips)} usable clips")
    if not clips:
        return

    yt = None if dry else yt_access_token(s)
    for clip in clips[:3]:  # try the top 3 in case a download fails
        try:
            with tempfile.TemporaryDirectory() as td:
                work = Path(td)
                src = download(clip, work)
                dur = probe_duration(src)
                hook = hook_text(clip)
                credit = f"twitch.tv/{clip['broadcaster_name'].lower()}"
                ass = work / "subs.ass"
                ass.write_text(build_ass(hook, credit, transcribe(src), dur), encoding="utf-8")
                out = work / "short.mp4"
                render(src, ass, out)
                title, desc = make_title(clip, hook), make_desc(clip)
                print("rendered:", title, f"({dur:.0f}s, {clip['view_count']} views)")
                if dry:
                    Path(HERE / "last_dry_run.mp4").write_bytes(out.read_bytes())
                    return
                vid = yt_upload(yt, out, title, desc, CFG["tags"])
        except Exception as e:
            print(f"clip {clip['id']} failed: {e}")
            continue
        posted.append({"clip_id": clip["id"], "video_id": vid, "streamer": clip["broadcaster_name"],
                       "views_at_pick": clip["view_count"], "title": title,
                       "posted_at": dt.datetime.now(dt.timezone.utc).isoformat(timespec="seconds")})
        save_posted(posted)
        print(f"uploaded https://youtube.com/shorts/{vid}")
        return
    sys.exit("all candidate clips failed")


if __name__ == "__main__":
    main()
