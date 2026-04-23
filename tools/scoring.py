"""
scoring.py — 四层聚合打分脚本

用法:
    python tools/scoring.py --input results/round-1/raw-votes.csv --output results/round-1/aggregated-repro.csv

输入格式 (raw-votes.csv):
    scene, evaluator, role, question, task, vote

vote 取值:
    1/2/3 = 选择对应产品（产品顺序见 --product-map）
    5 = 差不多（不计入）
    6 = 此题目与任务无关（不计入）
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
    四层聚合：
    L1 - 题目层：统计每道题每个产品的得票数
    L2 - 任务层：5 题中赢得最多题目的产品赢得该任务（允许并列）
    L3 - 场景层：赢得任务数 / 总任务数 = 场景胜率
    L4 - 总榜层：所有场景赢得任务数 / 总任务数
    """
    products = list(product_map.values())

    # L1: 题目层得票
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

    # L2: 任务层胜出判定
    # key: (scene, task) -> {product: questions_won}
    task_wins: dict = defaultdict(lambda: defaultdict(int))
    for (scene, task, question), prod_votes in q_votes.items():
        if not prod_votes:
            continue
        max_votes = max(prod_votes.values())
        winners = [p for p, v in prod_votes.items() if v == max_votes]
        for w in winners:
            task_wins[(scene, task)][w] += 1

    # L2 -> 任务胜出产品（允许并列）
    task_winners: dict = defaultdict(set)
    for (scene, task), prod_q_wins in task_wins.items():
        if not prod_q_wins:
            continue
        max_q = max(prod_q_wins.values())
        for p, w in prod_q_wins.items():
            if w == max_q:
                task_winners[(scene, task)].add(p)

    # L3: 场景层聚合
    scene_tasks: dict = defaultdict(set)
    scene_prod_wins: dict = defaultdict(lambda: defaultdict(int))
    for (scene, task), winners in task_winners.items():
        scene_tasks[scene].add(task)
        for p in winners:
            scene_prod_wins[scene][p] += 1

    # 构建输出行
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

        # 标注第一名
        for r in results:
            if r["scene"] == scene and r["product"] == winner_prod:
                r["first_place"] = "是"

    # 总榜行
    for prod in products:
        wins = overall_wins[prod]
        rate = wins / total_tasks if total_tasks > 0 else 0.0
        results.append({
            "scene": "【总计】",
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
    print(f"结果已写入: {path}")


def main():
    parser = argparse.ArgumentParser(description="AI Design Benchmark 四层聚合打分脚本")
    parser.add_argument("--input", required=True, help="原始投票 CSV 路径")
    parser.add_argument("--output", required=True, help="聚合结果 CSV 输出路径")
    parser.add_argument(
        "--product-map",
        default="1:Lovart,2:Roboneo,3:即梦",
        help="投票值到产品名的映射，格式：1:ProductA,2:ProductB,3:ProductC",
    )
    args = parser.parse_args()

    product_map = {}
    for item in args.product_map.split(","):
        k, v = item.strip().split(":")
        product_map[k.strip()] = v.strip()

    print(f"产品映射: {product_map}")
    rows = load_votes(args.input)
    print(f"加载 {len(rows)} 条投票记录")

    results = aggregate(rows, product_map)
    write_results(results, args.output)


if __name__ == "__main__":
    main()
