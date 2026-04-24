# Evaluation Results | 评测结果说明

[English](#english) | [中文](#中文)

---

## English

### Directory Structure

```
results/
├── round-1/                    # Round 1 (March–April 2026)
│   ├── raw-votes.csv           # Raw votes (evaluators anonymized as E01–E10)
│   ├── aggregated.csv          # Aggregated win-rate results per scene
│   ├── analysis-reports/       # Scene-level analysis reports (Markdown)
│   └── failure-cases/          # Typical failure case images (to be added in Phase 2)
└── README.md
```

### Round 1 Overview

| Field | Value |
|-------|-------|
| Data collection | March–April 2026 |
| Products evaluated | Lovart / Jimeng (即梦) / Roboneo |
| Scenes | 7 (Logo / IP Character / Badge & Trophy / Product Poster / Image Enhancement / Online Marketing / Offline Promotion) |
| Total tasks | 115 |
| Evaluators | 10 (5 design / 4 engineering / 1 ML) |
| Method | Double-blind SbS ranking |
| Random baseline | 33% (3-way) |

### Reproducing Results

```bash
python tools/scoring.py \
  --input results/round-1/raw-votes.csv \
  --output results/round-1/aggregated-repro.csv \
  --product-map "1:Lovart,2:Roboneo,3:即梦"

python tools/confidence.py \
  --input results/round-1/raw-votes.csv \
  --product-map "1:Lovart,2:Roboneo,3:即梦"
```

### Data Format

**raw-votes.csv**

| Column | Description |
|--------|-------------|
| scene | Design scene name |
| evaluator | Anonymous code (E01–E10) |
| role | Role (Design / Engineering / Algorithm) |
| question | Evaluation question (Q1–Q5) |
| task | Task ID (e.g., L-001) |
| vote | Vote value (1–3 = product, 5 = about the same, 6 = not relevant) |

**aggregated.csv**

| Column | Description |
|--------|-------------|
| scene | Design scene |
| product | Product name |
| tasks_won | Number of tasks won |
| total_tasks | Total tasks in scene |
| win_rate | Scene win rate |
| first_place | Whether ranked first |

---

## 中文

### 目录结构

```
results/
├── round-1/                    # Round 1（2026 年 3-4 月）
│   ├── raw-votes.csv           # 原始投票记录（评测员已匿名为 E01-E10）
│   ├── aggregated.csv          # 各场景 × 产品胜率聚合结果
│   ├── analysis-reports/       # 场景级分析报告（Markdown）
│   └── failure-cases/          # 典型失败案例图片（待阶段二补充）
└── README.md
```

### Round 1 基本信息

| 字段 | 内容 |
|------|------|
| 数据采集时间 | 2026 年 3-4 月 |
| 参评产品 | Lovart / 即梦 / Roboneo |
| 评测场景 | 7 个（Logo / IP 形象 / 徽章奖杯 / 商品海报 / 商品图片美化 / 线上营销 / 线下推广）|
| 总任务数 | 115 条 |
| 评测员人数 | 10 人（设计 5 / 研发 4 / 算法 1）|
| 评测方式 | 双盲 SbS 图片排序投票 |
| 随机基准 | 33%（3 选 1）|

### 复现说明

```bash
python tools/scoring.py \
  --input results/round-1/raw-votes.csv \
  --output results/round-1/aggregated-repro.csv \
  --product-map "1:Lovart,2:Roboneo,3:即梦"

python tools/confidence.py \
  --input results/round-1/raw-votes.csv \
  --product-map "1:Lovart,2:Roboneo,3:即梦"
```

### 数据格式

**raw-votes.csv**

| 列名 | 说明 |
|------|------|
| scene | 设计场景名称 |
| evaluator | 评测员匿名代号（E01-E10）|
| role | 职能（设计 / 研发 / 算法）|
| question | 评测题目（Q1-Q5）|
| task | 任务编号（如 L-001）|
| vote | 投票值（1-3 = 产品，5 = 差不多，6 = 无关）|

**aggregated.csv**

| 列名 | 说明 |
|------|------|
| scene | 设计场景 |
| product | 产品名称 |
| tasks_won | 赢得任务数 |
| total_tasks | 总任务数 |
| win_rate | 场景胜率 |
| first_place | 是否排名第一 |
