#!/usr/bin/env python3
import csv
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TIE_ORDER = ["C1", "C2", "C4", "C6", "C3", "C5"]

with (ROOT / "SCORING_MODEL.csv").open(encoding="utf-8-sig", newline="") as f:
    model_rows = list(csv.DictReader(f))

weights = {
    row["metric_id"]: float(row["weight"])
    for row in model_rows
    if row.get("metric_id") in {"C1", "C2", "C3", "C4", "C5", "C6"}
}
assert round(sum(weights.values()), 10) == 100, "Weights must sum to 100"

with (ROOT / "SCORE_MATRIX.csv").open(encoding="utf-8-sig", newline="") as f:
    rows = list(csv.DictReader(f))

scored = []
for row in rows:
    if row.get("status") == "FINAL_EXCLUSION":
        continue
    total = sum(float(row[cid]) / 5 * weights[cid] for cid in weights)
    recalculated = round(total)
    published = int(float(row["weighted_score"]))
    if recalculated != published:
        raise SystemExit(
            f"Score mismatch for {row['participant']}: published={published}, recalculated={recalculated}"
        )
    row["_score"] = published
    scored.append(row)

def sort_key(row):
    return tuple([-row["_score"]] + [-float(row[cid]) for cid in TIE_ORDER])

ordered = sorted(scored, key=sort_key)
for expected_rank, row in enumerate(ordered, start=1):
    published_rank = int(float(row["rank"]))
    if published_rank != expected_rank:
        raise SystemExit(
            f"Rank mismatch for {row['participant']}: published={published_rank}, expected={expected_rank}"
        )

print("place | participant | score")
for row in ordered:
    print(f"{int(float(row['rank'])):>5} | {row['participant']} | {row['_score']}")
print("\nPASS: weights=100; all 13 totals and frozen tie-break reproduce.")
