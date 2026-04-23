"""
confidence.py — 置信度与 Bootstrap 置信区间计算

用法:
    python tools/confidence.py --input results/round-1/raw-votes.csv

输出:
    - 各场景票数集中度（第一名与第二名胜率差）
    - 各产品总胜率的 95% Bootstrap 置信区间
"""

import csv
import argparse
import random
from collections import defaultdict
from scoring import load_votes, aggregate


BOOTSTRAP_N = 10_000
BOOTSTRAP_SEED = 42


def compute_scene_confidence(results: list[dict]) -> list[dict]:
    """计算各场景票数集中度（差距）及置信度标签。"""
    scene_rates: dict = defaultdict(dict)
    for r in results:
        if r["scene"] == "【总计】":
            continue
        scene_rates[r["scene"]][r["product"]] = float(r["win_rate"].strip("%")) / 100

    output = []
    for scene, prod_rates in sorted(scene_rates.items()):
        sorted_prods = sorted(prod_rates.items(), key=lambda x: -x[1])
        first_prod, first_rate = sorted_prods[0]
        second_prod, second_rate = sorted_prods[1] if len(sorted_prods) > 1 else ("—", 0.0)
        gap = first_rate - second_rate

        if gap >= 0.20:
            confidence = "✅ 高（≥20%）"
        elif gap >= 0.10:
            confidence = "⚠️ 中（10-20%）"
        else:
            confidence = "❌ 低（<10%）"

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
    Task-resample Bootstrap：
    每次从全部任务中有放回地抽样（与原始任务数相同），
    计算各产品总胜率，重复 n_iter 次，取 alpha/2 和 1-alpha/2 分位数作为 CI。
    """
    # 按 (scene, task) 组织行
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
            if r["scene"] == "【总计】":
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
    parser = argparse.ArgumentParser(description="置信度与 Bootstrap CI 计算")
    parser.add_argument("--input", required=True, help="原始投票 CSV 路径")
    parser.add_argument(
        "--product-map",
        default="1:Lovart,2:Roboneo,3:即梦",
        help="投票值到产品名的映射",
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

    print("\n=== 场景置信度 ===")
    print(f"{'场景':<12} {'第一名':<8} {'胜率':>6} {'第二名':<8} {'胜率':>6} {'差距':>6}  {'置信度'}")
    print("-" * 72)
    for c in compute_scene_confidence(results):
        print(
            f"{c['scene']:<12} {c['first']:<8} {c['first_rate']:>6} "
            f"{c['second']:<8} {c['second_rate']:>6} {c['gap']:>6}  {c['confidence']}"
        )

    print(f"\n=== Bootstrap 95% CI（{args.n_bootstrap:,} 次迭代，seed={args.seed}）===")
    ci = bootstrap_overall_ci(rows, product_map, n_iter=args.n_bootstrap, seed=args.seed)
    print(f"{'产品':<10} {'均值':>8} {'95% CI'}")
    print("-" * 40)
    for prod, vals in sorted(ci.items(), key=lambda x: -x[1]["mean"]):
        print(f"{prod:<10} {vals['mean']:>7.1%}  ({vals['lo']:.1%} – {vals['hi']:.1%})")


if __name__ == "__main__":
    main()
