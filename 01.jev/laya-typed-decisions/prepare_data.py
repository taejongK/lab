# /// script
# requires-python = ">=3.10"
# dependencies = ["datasets"]
# ///
"""typed-decisions train/test -> Laya JSONL rows ({state, questions, gold}) under data/.

uv run prepare_data.py [config]   # config: all (default), customer_service, ...
"""
import json
import sys
from pathlib import Path

from datasets import load_dataset

config = sys.argv[1] if len(sys.argv) > 1 else "all"
out = Path(__file__).parent / "data"
out.mkdir(exist_ok=True)
for split in ("train", "test"):
    ds = load_dataset("LocalLLaMA/typed-decisions", config, split=split)
    path = out / f"{config}-{split}.jsonl"
    with open(path, "w", encoding="utf-8") as f:
        for r in ds:
            f.write(json.dumps({k: json.loads(r[k]) for k in ("state", "questions", "gold")}, ensure_ascii=False) + "\n")
    print(f"{path}: {len(ds)} cases")
