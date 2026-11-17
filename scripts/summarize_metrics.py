"""Read the original saved training CSV, without rerunning training."""

import csv
from pathlib import Path

path = Path(__file__).resolve().parent.parent / "results" / "results.csv"
with path.open(newline="", encoding="utf-8") as file:
    rows = list(csv.DictReader(file))
if not rows:
    raise SystemExit("No training log rows")

best = max(rows, key=lambda row: float(row["metrics/mAP50-95(B)"]))
print(f"Logged epochs: {len(rows)}")
for key in ("epoch", "metrics/precision(B)", "metrics/recall(B)", "metrics/mAP50(B)", "metrics/mAP50-95(B)"):
    print(f"{key}: {best[key]}")
print("These numbers come from the archived log, not a new validation run.")
