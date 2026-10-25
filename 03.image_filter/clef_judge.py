# /// script
# requires-python = ">=3.11"
# ///
"""llama-server(/v1/systemone)에 올린 Clef-Flash로 이미지 검열 판정.

uv run clef_judge.py IMG [IMG ...]
"""
import base64
import json
import mimetypes
import sys
import time
import urllib.request

URL = "http://localhost:8080/v1/systemone"
QUESTIONS = {
    "rating": {
        "type": "choice",
        "instructions": "How sexually explicit is this image?",
        "criteria": {
            "safe": "No nudity or sexual content.",
            "suggestive": "Revealing clothing or sexually suggestive pose, no exposed genitals or nipples.",
            "explicit": "Nudity with exposed genitals or nipples, or sexual activity.",
        },
    },
    "drawn": {"type": "noul", "instructions": "Is this a drawing, anime or illustration rather than a photo?"},
}


def judge(path: str) -> dict:
    mime = mimetypes.guess_type(path)[0] or "image/jpeg"
    data = base64.b64encode(open(path, "rb").read()).decode()
    body = {"state": "Review the attached image for content moderation.",
            "images": [f"data:{mime};base64,{data}"], "questions": QUESTIONS}
    req = urllib.request.Request(URL, json.dumps(body).encode(), {"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=120) as r:
        return json.load(r)


if __name__ == "__main__":
    for p in sys.argv[1:]:
        t = time.time()
        res = judge(p)
        a = res["answers"]
        print(f"{p}\t{a['rating']['choice']}\t{json.dumps(a['rating']['probabilities'])}"
              f"\tdrawn={a['drawn']['noul']:.2f}\ttokens={res['usage']['input_tokens']}\t{time.time() - t:.2f}s")
