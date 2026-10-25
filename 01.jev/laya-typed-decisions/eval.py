# /// script
# requires-python = ">=3.10"
# dependencies = ["laya @ git+https://github.com/NandhaKishorM/laya@432312b36714d8889eba405507b37eda25257d9c"]
# ///
"""Score a Laya checkpoint on a JSONL test file, the same way `laya-train --eval` scores "before".

uv run eval.py data/all-test.jsonl [checkpoint]   # checkpoint: english (default) or a local dir
"""
import json
import sys

from laya.train import (calibration_records, evaluate_records, items_from_rows, load_checkpoint,
                        read_jsonl, resolve_device)

data = sys.argv[1]
ckpt = sys.argv[2] if len(sys.argv) > 2 else "english"
model, tok, cfg = load_checkpoint(ckpt)
dev = resolve_device("auto")
model.to(dev)
max_len, head_max_len = cfg.get("max_len", 512), cfg.get("head_max_len", 192)
items, skipped = items_from_rows(tok, read_jsonl(data), max_len, head_max_len)
print(f"{ckpt} on {data}: {len(items)} decisions, skipped {skipped}, device {dev}", flush=True)
records = calibration_records(model, tok, items, dev, max_len, head_max_len)
print(json.dumps(evaluate_records(records, cfg.get("temperature"), cfg.get("temperature_by_options")), indent=2))
