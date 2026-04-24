"""
scoring.py — 4-layer aggregation scoring script

Usage:
    python tools/scoring.py --input results/round-1/raw-votes.csv --output results/round-1/aggregated-repro.csv

Input format (raw-votes.csv):
    scene, evaluator, role, question, task, vote

vote values:
    1/2/3 = vote for corresponding product (see --product-map)
    5     = about the same (excluded from scoring)
    6     = not relevant to this task (excluded from scoring)
"""

import csv
import argparse
from collections import defaultdict


SKIP_VOTES = {"5", "6"}


def load_votes(path: str) -> list[dict]:
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def aggregate(rows: list[dict], product_map: dict[str, str]) -> list[dict]:
    """
    4-layer aggregation:
    L1 - Question level: count votes per product per question
    L2 - Task level: product that wins the most questions wins the task (ties allowed)
    L3 - Scene level: tasks_won / total_tasks = scene win rate
    L4 - Overall: total tasks_won / total tasks across all scenes
    """
    products = list(product_map.values())

    # L1: question-level vote counts
    # key: (scene, task, question) -> {product: vote_count}
    q_votes: dict = defaultdict(lambda: defaultdict(int))
    for row in rows:
        if row["vote"] in SKIP_VOTES:
            continue
        prod = product_map.get(row["vote"])
        if prod is None:
            continue
        key = (row["scene"], row["task"], row["question"])
        q_votes[key][prod] += 1

    # L2: task-level winner determination
    # key: (scene, task) -> {product: questions_won}
    task_wins: dict = defaultdict(lambda: defaultdict(int))
    for (scene, task, question), prod_votes in q_votes.items():
        if not prod_votes:
            continue
        max_votes = max(prod_votes.values())
        winners = [p for p, v in prod_votes.items() if v == max_votes]
        for w in winners:
            task_wins[(scene, task)][w] += 1

    # L2 -> task winners (ties allowed)
    task_winners: dict = defaultdict(set)
    for (scene, task), prod_q_wins in task_wins.items():
        if not prod_q_wins:
            continue
        max_q = max(prod_q_wins.values())
        for p, w in prod_q_wins.items():
            if w == max_q:
                task_winners[(scene, task)].add(p)

    # L3: scene-level aggregation
    scene_tasks: dict = defaultdict(set)
    scene_prod_wins: dict = defaultdict(lambda: defaultdict(int))
    for (scene, task), winners in task_winners.items():
        scene_tasks[scene].add(task)
        for p in winners:
            scene_prod_wins[scene][p] += 1

    results = []
    total_tasks = sum(len(tasks) for tasks in scene_tasks.values())
    overall_wins: dict = defaultdict(int)

    for scene in sorted(scene_tasks.keys()):
        n_tasks = len(scene_tasks[scene])
        winner_prod = None
        winner_rate = 0.0
        for prod in products:
            wins = scene_prod_wins[scene].get(prod, 0)
            rate = wins / n_tasks if n_tasks > 0 else 0.0
            overall_wins[prod] += wins
            results.append({
                "scene": scene,
                "product": prod,
                "tasks_won": wins,
                "total_tasks": n_tasks,
                "win_rate": f"{rate:.1%}",
                "first_place": "",
            })
            if rate > winner_rate:
                winner_rate = rate
                winner_prod = prod

        for r in results:
            if r["scene"] == scene and r["product"] == winner_prod:
                r["first_place"] = "Yes"

    # L4: overall row
    for prod in products:
        wins = overall_wins[prod]
        rate = wins / total_tasks if total_tasks > 0 else 0.0
        results.append({
            "scene": "[Total]",
            "product": prod,
            "tasks_won": wins,
            "total_tasks": total_tasks,
            "win_rate": f"{rate:.1%}",
            "first_place": "",
        })

    return results


def write_results(results: list[dict], path: str):
    fieldnames = ["scene", "product", "tasks_won", "total_tasks", "win_rate", "first_place"]
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)
    print(f"Results written to: {path}")


def main():
    parser = argparse.ArgumentParser(description="AI Design Benchmark — 4-layer aggregation scoring")
    parser.add_argument("--input", required=True, help="Path to raw-votes CSV file")
    parser.add_argument("--output", required=True, help="Output path for aggregated results CSV")
    parser.add_argument(
        "--product-map",
        default="1:Lovart,2:Roboneo,3:即梦",
        help="Mapping from vote value to product name, e.g. 1:ProductA,2:ProductB,3:ProductC",
    )
    args = parser.parse_args()

    product_map = {}
    for item in args.product_map.split(","):
        k, v = item.strip().split(":")
        product_map[k.strip()] = v.strip()

    print(f"Product map: {product_map}")
    rows = load_votes(args.input)
    print(f"Loaded {len(rows)} vote records")

    results = aggregate(rows, product_map)
    write_results(results, args.output)


if __name__ == "__main__":
    main()
