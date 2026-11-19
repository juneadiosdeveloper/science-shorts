#!/usr/bin/env python3
"""One-time: swap the Google sign-in code (auth/code.enc) for a refresh token,
store it encrypted in state/yt_token.enc and write the outcome to auth/status.txt."""
import json, os, subprocess
from pathlib import Path
import requests

HERE = Path(__file__).resolve().parent

def dec(p):
    return subprocess.run(["openssl", "enc", "-d", "-aes-256-cbc", "-pbkdf2", "-iter", "200000",
                           "-base64", "-A", "-pass", "env:BOT_KEY", "-in", str(p)],
                          check=True, capture_output=True).stdout.decode().strip()

def enc(text, p):
    subprocess.run(["openssl", "enc", "-aes-256-cbc", "-pbkdf2", "-iter", "200000", "-salt",
                    "-base64", "-A", "-pass", "env:BOT_KEY", "-out", str(p)],
                   input=text.encode(), check=True)

s = json.loads(dec(HERE / "secrets.enc"))
code = dec(HERE / "auth" / "code.enc")
r = requests.post("https://oauth2.googleapis.com/token", data={
    "code": code, "client_id": s["google_client_id"], "client_secret": s["google_client_secret"],
    "redirect_uri": "http://localhost", "grant_type": "authorization_code"}, timeout=30)
js = r.json()
if r.ok and js.get("refresh_token"):
    enc(js["refresh_token"], HERE / "state" / "yt_token.enc")
    ch = requests.get("https://www.googleapis.com/youtube/v3/channels?part=snippet&mine=true",
                      headers={"Authorization": "Bearer " + js["access_token"]}, timeout=30).json()
    names = [i["snippet"]["title"] for i in ch.get("items", [])]
    msg = f"OK - connected to channel: {', '.join(names) or 'unknown (upload-only scope)'}"
else:
    msg = f"FAILED - {js.get('error')}: {js.get('error_description')}"
(HERE / "auth" / "status.txt").write_text(msg + "\n")
(HERE / "auth" / "code.enc").unlink()
print(msg)
