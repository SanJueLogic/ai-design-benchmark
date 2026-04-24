"""
confidence.py — Confidence and Bootstrap confidence interval calculator

Usage:
    python tools/confidence.py --input results/round-1/raw-votes.csv

Output:
    - Scene-level ticket concentration (gap between 1st and 2nd place win rates)
    - 95% Bootstrap confidence intervals for each product's overall win rate
"""

import csv
import argparse
import random
from collections import defaultdict
from scoring import load_votes, aggregate


BOOTSTRAP_N = 10_000
BOOTSTRAP_SEED = 42


def compute_scene_confidence(results: list[dict]) -> list[dict]:
    """Compute per-scene ticket concentration (gap) and confidence label."""
    scene_rates: dict = defaultdict(dict)
    for r in results:
        if r["scene"] == "[Total]":
            continue
        scene_rates[r["scene"]][r["product"]] = float(r["win_rate"].strip("%")) / 100

    output = []
    for scene, prod_rates in sorted(scene_rates.items()):
        sorted_prods = sorted(prod_rates.items(), key=lambda x: -x[1])
        first_prod, first_rate = sorted_prods[0]
        second_prod, second_rate = sorted_prods[1] if len(sorted_prods) > 1 else ("—", 0.0)
        gap = first_rate - second_rate

        if gap >= 0.20:
            confidence = "✅ High (≥20%)"
        elif gap >= 0.10:
            confidence = "⚠️ Medium (10-20%)"
        else:
            confidence = "❌ Low (<10%)"

        output.append({
            "scene": scene,
            "first": first_prod,
            "first_rate": f"{first_rate:.1%}",
            "second": second_prod,
            "second_rate": f"{second_rate:.1%}",
            "gap": f"{gap:.1%}",
            "confidence": confidence,
        })
    return output


def bootstrap_overall_ci(
    rows: list[dict],
    product_map: dict[str, str],
    n_iter: int = BOOTSTRAP_N,
    seed: int = BOOTSTRAP_SEED,
    alpha: float = 0.05,
) -> dict[str, dict]:
    """
    Task-resample Bootstrap:
    Each iteration samples (with replacement) the same number of tasks as the original,
    computes each product's overall win rate, repeats n_iter times,
    and takes the alpha/2 and 1-alpha/2 quantiles as the CI bounds.
    """
    task_rows: dict = defaultdict(list)
    for row in rows:
        task_rows[(row["scene"], row["task"])].append(row)

    all_tasks = list(task_rows.keys())

    rng = random.Random(seed)
    win_counts: dict = defaultdict(list)

    for _ in range(n_iter):
        sample_tasks = [rng.choice(all_tasks) for _ in all_tasks]
        sample_rows = []
        for t in sample_tasks:
            sample_rows.extend(task_rows[t])
        results = aggregate(sample_rows, product_map)
        for r in results:
            if r["scene"] == "[Total]":
                rate = float(r["win_rate"].strip("%")) / 100
                win_counts[r["product"]].append(rate)

    ci_results = {}
    for prod, rates in win_counts.items():
        rates_sorted = sorted(rates)
        lo = rates_sorted[int(alpha / 2 * n_iter)]
        hi = rates_sorted[int((1 - alpha / 2) * n_iter)]
        mean = sum(rates) / len(rates)
        ci_results[prod] = {"mean": mean, "lo": lo, "hi": hi}

    return ci_results


def main():
    parser = argparse.ArgumentParser(description="AI Design Benchmark — confidence and Bootstrap CI calculator")
    parser.add_argument("--input", required=True, help="Path to raw-votes CSV file")
    parser.add_argument(
        "--product-map",
        default="1:Lovart,2:Roboneo,3:即梦",
        help="Mapping from vote value to product name, e.g. 1:ProductA,2:ProductB,3:ProductC",
    )
    parser.add_argument("--n-bootstrap", type=int, default=BOOTSTRAP_N)
    parser.add_argument("--seed", type=int, default=BOOTSTRAP_SEED)
    args = parser.parse_args()

    product_map = {}
    for item in args.product_map.split(","):
        k, v = item.strip().split(":")
        product_map[k.strip()] = v.strip()

    rows = load_votes(args.input)
    results = aggregate(rows, product_map)

    print("\n=== Scene Confidence ===")
    print(f"{'Scene':<30} {'1st':<10} {'Rate':>6} {'2nd':<10} {'Rate':>6} {'Gap':>6}  {'Confidence'}")
    print("-" * 85)
    for c in compute_scene_confidence(results):
        print(
            f"{c['scene']:<30} {c['first']:<10} {c['first_rate']:>6} "
            f"{c['second']:<10} {c['second_rate']:>6} {c['gap']:>6}  {c['confidence']}"
        )

    print(f"\n=== Bootstrap 95% CI ({args.n_bootstrap:,} iterations, seed={args.seed}) ===")
    ci = bootstrap_overall_ci(rows, product_map, n_iter=args.n_bootstrap, seed=args.seed)
    print(f"{'Product':<12} {'Mean':>8} {'95% CI'}")
    print("-" * 40)
    for prod, vals in sorted(ci.items(), key=lambda x: -x[1]["mean"]):
        print(f"{prod:<12} {vals['mean']:>7.1%}  ({vals['lo']:.1%} – {vals['hi']:.1%})")


if __name__ == "__main__":
    main()
