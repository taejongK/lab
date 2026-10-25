# /// script
# requires-python = ">=3.11"
# ///
"""GantMan(nsfw_data_scraper) URL 목록에서 클래스별 N장을 받는다.

uv run fetch_gantman.py --per-class 200 [--classes hentai drawings ...]
URL 목록은 data/urls/{class}.txt, 이미지는 data/gantman/{class}/ 에 저장.
"""
import argparse
import hashlib
import random
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).parent / "data"
CLASSES = ["drawings", "hentai", "neutral", "porn", "sexy"]


def fetch(url: str, out_dir: Path) -> bool:
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=15) as r:
            # imgur는 지운 이미지를 removed.png(200)로 돌려준다
            if "removed" in r.url or not r.headers.get("Content-Type", "").startswith("image/"):
                return False
            body = r.read()
    except Exception:
        return False
    ext = Path(url.split("?")[0]).suffix or ".jpg"
    (out_dir / f"{hashlib.md5(body).hexdigest()}{ext}").write_bytes(body)
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--per-class", type=int, default=200)
    ap.add_argument("--classes", nargs="+", default=CLASSES)
    args = ap.parse_args()
    for c in args.classes:
        urls = (ROOT / "urls" / f"{c}.txt").read_text().split()
        random.Random(0).shuffle(urls)
        out_dir = ROOT / "gantman" / c
        out_dir.mkdir(parents=True, exist_ok=True)
        i = 0
        with ThreadPoolExecutor(16) as ex:
            # 같은 이미지(md5)는 덮어쓰므로 성공 수가 아니라 폴더 안 파일 수로 센다
            while (got := len(list(out_dir.iterdir()))) < args.per_class and i < len(urls):
                batch = urls[i : i + min(args.per_class - got, 64)]
                i += len(batch)
                list(ex.map(lambda u: fetch(u, out_dir), batch))
        print(f"{c}: {len(list(out_dir.iterdir()))}장 ({i}개 URL 시도)")


if __name__ == "__main__":
    main()
