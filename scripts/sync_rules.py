#!/usr/bin/env python3
import pathlib, urllib.request, time
SELECTED = ['AdvertisingLite', 'Lan', 'OpenAI', 'Claude', 'Anthropic', 'Gemini', 'Telegram', 'Google', 'YouTube', 'GitHub', 'Twitter', 'Facebook', 'Instagram', 'GlobalMedia', 'Netflix', 'Disney', 'Spotify', 'TikTok', 'PayPal', 'Apple', 'AppStore', 'AppleID', 'AppleMedia', 'Microsoft', 'OneDrive', 'ChinaMedia', 'BiliBili', 'Direct', 'ChinaMax', 'Proxy', 'Global']
UPSTREAM = "https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/QuantumultX"
ROOT = pathlib.Path(__file__).resolve().parents[1]
for name in SELECTED:
    outdir = ROOT / "rules" / "QuantumultX" / name
    outdir.mkdir(parents=True, exist_ok=True)
    url = f"{UPSTREAM}/{name}/{name}.list"
    req = urllib.request.Request(url, headers={"User-Agent":"qx-rules-sync"})
    data = urllib.request.urlopen(req, timeout=60).read()
    (outdir / f"{name}.list").write_bytes(data)
    time.sleep(0.2)
print(f"synced {len(SELECTED)} rule files")
