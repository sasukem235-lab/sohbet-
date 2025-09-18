#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import time
import random
import urllib.parse
import json
import re

try:
    import requests
except Exception:
    requests = None

try:
    from bs4 import BeautifulSoup
except Exception:
    BeautifulSoup = None

ANSI_COLORS = [
    '\033[91m', # red
    '\033[92m', # green
    '\033[94m', # blue
]
ANSI_RESET = '\033[0m'

def colorize(s):
    return f"{random.choice(ANSI_COLORS)}{s}{ANSI_RESET}"

def typewriter(text, cps=19920, jitter=0.04, newline=True):
    delay = 1.0 / max(1, cps)
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(max(0, delay + random.uniform(-jitter, jitter)))
    if newline:
        sys.stdout.write("\n")
        sys.stdout.flush()

def fetch_api(site_value):
    base = "https://free.zirveexec.com/api_public.php"
    params = {'site': site_value}
    url = base + "?" + urllib.parse.urlencode(params, safe='')
    if requests:
        r = requests.get(url, timeout=15)
        r.raise_for_status()
        return r.content, getattr(r, "headers", {}), r
    else:
        from urllib import request
        req = request.Request(url, headers={'User-Agent': 'anim-print/1.0'})
        with request.urlopen(req, timeout=15) as resp:
            content = resp.read()
            headers = dict(resp.getheaders())
            return content, headers, None

def extract_texts_from_json(obj):
    texts = []
    if isinstance(obj, dict):
        for v in obj.values():
            texts.extend(extract_texts_from_json(v))
    elif isinstance(obj, list):
        for v in obj:
            texts.extend(extract_texts_from_json(v))
    elif isinstance(obj, (str,)):
        s = obj.strip()
        if s:
            texts.append(s)
    return texts

def html_to_text(html_bytes, encoding='utf-8'):
    try:
        text = html_bytes.decode(encoding, errors='replace')
    except Exception:
        text = html_bytes.decode('utf-8', errors='replace')
    if BeautifulSoup:
        soup = BeautifulSoup(text, 'html.parser')
        for s in soup(["script", "style", "noscript"]):
            s.decompose()
        visible = soup.get_text(separator="\n")
        lines = [ln.strip() for ln in visible.splitlines()]
        lines = [ln for ln in lines if ln]
        return lines
    else:
        no_tags = re.sub(r'<[^>]+>', '', text)
        lines = [ln.strip() for ln in no_tags.splitlines()]
        lines = [ln for ln in lines if ln]
        return lines

def gather_texts_from_response(content_bytes, headers=None, response_obj=None):
    try:
        decoded = content_bytes.decode('utf-8', errors='strict')
        parsed = json.loads(decoded)
        texts = extract_texts_from_json(parsed)
        if texts:
            return texts
    except Exception:
        pass
    encoding = None
    if headers:
        ct = headers.get('Content-Type', '')
        m = re.search(r'charset=([^\s;]+)', ct, re.I)
        if m:
            encoding = m.group(1)
    lines = html_to_text(content_bytes, encoding or 'utf-8')
    return lines

def present_texts(texts, site_label):
    # - 8 
    texts = texts[8:]
    if not texts:
        print("Metin yoğ cünki free apiğ.")
        return
    for t in texts:
        s = re.sub(r'\s+', ' ', t).strip()
        if not s:
            continue
        typewriter(colorize(s), cps=120, jitter=0.03)

def main():
    if len(sys.argv) >= 2:
        site_value = sys.argv[1]
    else:
        site_value = input("Site adını gir (ör: purna/purna.com): ").strip()
        if not site_value:
            print("Site yok la(yada kod 5satır/free ap diye")
            return
    site_value = site_value.strip()
    try:
        content, headers, raw_resp_obj = fetch_api(site_value)
        texts = gather_texts_from_response(content, headers=headers, response_obj=raw_resp_obj)
    except Exception as e:
        print(f"Hata: {e}")
        return
    present_texts(texts, site_value)

if __name__ == "__main__":
    main()