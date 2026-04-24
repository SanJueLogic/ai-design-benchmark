# AI Design Benchmark

[English](#english) | [中文](#中文)

---

## English

**A reproducible benchmark framework for evaluating AI design tools across 7 design scenarios**

[![License: CC BY 4.0](https://img.shields.io/badge/Data%20License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![License: MIT](https://img.shields.io/badge/Code%20License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Paper](https://img.shields.io/badge/Paper-v1.1-blue.svg)](https://github.com/SanJueLogic/ai-design-benchmark/releases/download/v1.1/AI-Design-Benchmark-v1.1.pdf)
[![Tests](https://github.com/SanJueLogic/ai-design-benchmark/actions/workflows/test.yml/badge.svg)](https://github.com/SanJueLogic/ai-design-benchmark/actions/workflows/test.yml)

### News

- **2026-04**: v1.1 released — added reference images (53 files), bilingual tasks, CI pipeline, and 9 scoring tests; paper PDF published as [Release asset](https://github.com/SanJueLogic/ai-design-benchmark/releases/tag/v1.1)
- **2026-04**: Round 1 results published — Lovart 56% (95% CI: 47%–64%), Jimeng 27%, Roboneo 19% across 7 scenes

### Overview

This project provides a reproducible framework for cross-product evaluation of AI design tools, including:

- **7 design scenarios, 140 tasks in dataset** — 115 tasks evaluated in Round 1 (Logo Design / IP Character Design / Badge & Trophy / Product Poster / Product Image Enhancement / Online Marketing / Offline Promotion)
- **Double-blind SbS (Side-by-Side) voting**: evaluators pick the best output without knowing which product generated it
- **4-layer aggregation algorithm**: Vote → Question → Task → Scene, ensuring full reproducibility
- **Two-step confidence quantification**: Ticket concentration (≥20% / 10–20% / <10%) + Bootstrap 95% CI
- **Round 1 empirical results**: cross-product comparison data for 3 publicly available AI design tools (Lovart / Jimeng / Roboneo)

> Full paper → [`paper/`](paper/) | Methodology → [`methodology/`](methodology/) | Task dataset → [`dataset/`](dataset/)

### Quick Start

**Requirements**

```bash
Python >= 3.9
pip install -r tools/requirements.txt
```

**Reproduce Round 1 results**

```bash
git clone https://github.com/SanJueLogic/ai-design-benchmark
cd ai-design-benchmark
python tools/scoring.py --input results/round-1/raw-votes.csv --output results/round-1/aggregated-repro.csv
python tools/confidence.py --input results/round-1/raw-votes.csv
```

**Run your own evaluation round** → [`docs/how-to-run-a-round.md`](docs/how-to-run-a-round.md)

### Repository Structure

```
ai-design-benchmark/
├── paper/                        # Full paper (Chinese Markdown + PDF)
├── methodology/                  # Methodology docs (metrics / scoring / evaluator protocol)
├── dataset/
│   └── v1.0/
│       ├── tasks.json            # Structured task dataset (140 tasks; 115 evaluated in Round 1)
│       ├── scenes/               # Per-scene task books (Markdown)
│       └── reference-images/     # Reference images for edit-type tasks
├── results/
│   └── round-1/
│       ├── raw-votes.csv         # Raw votes (evaluators anonymized)
│       ├── aggregated.csv        # Aggregated win-rate results
│       └── analysis-reports/     # Scene-level analysis reports
├── tools/
│   ├── scoring.py                # 4-layer aggregation scoring script
│   ├── confidence.py             # Confidence & Bootstrap CI calculator
│   └── sbs-template/             # SbS voting web template
└── docs/
    ├── how-to-run-a-round.md     # How to run an evaluation round
    ├── how-to-add-a-product.md   # How to add a new product
    └── how-to-contribute.md      # How to contribute new tasks
```

### Round 1 Results Summary

> Data collected: March–April 2026 | Method: double-blind SbS ranking | Evaluators: 10 (5 design / 4 engineering / 1 ML)

| Rank | Product | Win Rate | 95% CI | Scenes Won |
|:---:|---------|:-------:|:------:|:---------:|
| 🥇 1 | **Lovart** | 56% | 47%–64% | 6 |
| 🥈 2 | **Jimeng (即梦)** | 27% | 19%–35% | 1 |
| 🥉 3 | **Roboneo** | 19% | 12%–27% | 0 |

| Scene | Winner | Win Rate | Confidence |
|-------|:------:|:--------:|:---------:|
| Logo Design | Lovart | 71% | ✅ High |
| IP Character Design | Lovart | 44% | ❌ Low |
| Badge & Trophy Design | Lovart | 63% | ✅ High |
| Product Poster Design | Jimeng | 50% | ⚠️ Medium |
| Product Image Enhancement | Lovart | 46% | ❌ Low |
| Online Marketing Design | Lovart | 67% | ✅ High |
| Offline Promotion Design | Lovart | 63% | ✅ High |

> Full results and confidence explanations → [`results/round-1/`](results/round-1/)

### Citation

If this framework is helpful to your research, please cite:

```bibtex
@techreport{liu2026aidesignbenchmark,
  title     = {AI Design Tool Evaluation Benchmark v1.0: A Systematic Cross-Product Evaluation Framework for Enterprise Design Scenarios},
  author    = {Liu, Sanjue},
  year      = {2026},
  institution = {Independent Research},
  url       = {https://github.com/SanJueLogic/ai-design-benchmark}
}
```

### Contributing

Contributions of new tasks or scenes via Pull Request are welcome. See [`docs/how-to-contribute.md`](docs/how-to-contribute.md)

### Contact

For questions, collaboration, or citation inquiries:

📧 842559943@qq.com

### License

- **Data & documentation** (paper, task dataset, results): [CC BY 4.0](LICENSE-DATA) — free to use with attribution
- **Code** (scripts under `tools/`): [MIT](LICENSE-CODE)

---

## 中文

**一套面向 AI 设计工具的系统性评测框架**

### 简介

本项目提供一套可复现的 AI 设计工具横向评测方法论，包含：

- **7 大设计场景、140 条任务（数据集总量）**，Round 1 实评 115 条（Logo 设计 / IP 形象设计 / 徽章奖杯设计 / 商品海报设计 / 商品图片美化 / 线上营销活动 / 线下推广物料）
- **双盲 SbS（Side-by-Side）投票机制**：评测员在不知道图片来源的情况下逐题选出最优结果
- **四层聚合算法**：投票 → 题目 → 任务 → 场景，保证结论可复现
- **两步置信度量化**：票数集中度（≥20% / 10–20% / <10%）+ Bootstrap 95% CI
- **Round 1 实证结果**：3 款公开 AI 设计工具（Lovart / 即梦 / Roboneo）横向对比数据

> 论文全文 → [`paper/`](paper/) | 方法论文档 → [`methodology/`](methodology/) | 任务集 → [`dataset/`](dataset/)

### 快速开始

**环境要求**

```bash
Python >= 3.9
pip install -r tools/requirements.txt
```

**复现 Round 1 结果**

```bash
git clone https://github.com/SanJueLogic/ai-design-benchmark
cd ai-design-benchmark
python tools/scoring.py --input results/round-1/raw-votes.csv --output results/round-1/aggregated-repro.csv
python tools/confidence.py --input results/round-1/raw-votes.csv
```

**运行你自己的评测** → [`docs/how-to-run-a-round.md`](docs/how-to-run-a-round.md)

### Round 1 结果摘要

> 数据采集时间：2026 年 3-4 月 | 评测方式：双盲 SbS | 评测员：10 人（设计 5 / 研发 4 / 算法 1）

| 排名 | 产品 | 总胜率 | 95% CI | 第一场景数 |
|:---:|------|:------:|:------:|:--------:|
| 🥇 1 | **Lovart** | 56% | 47%–64% | 6 |
| 🥈 2 | **即梦** | 27% | 19%–35% | 1 |
| 🥉 3 | **Roboneo** | 19% | 12%–27% | 0 |

| 场景 | 第一名 | 胜率 | 置信度 |
|------|:-----:|:----:|:-----:|
| Logo 设计 | Lovart | 71% | ✅ 高 |
| IP 形象设计 | Lovart | 44% | ❌ 低 |
| 徽章奖杯设计 | Lovart | 63% | ✅ 高 |
| 商品海报设计 | 即梦 | 50% | ⚠️ 中 |
| 商品图片美化 | Lovart | 46% | ❌ 低 |
| 线上营销活动 | Lovart | 67% | ✅ 高 |
| 线下推广物料 | Lovart | 63% | ✅ 高 |

### 引用

```bibtex
@techreport{liu2026aidesignbenchmark,
  title     = {AI 设计工具评测 Benchmark v1.0：面向企业级设计场景的系统性横向评测框架},
  author    = {刘三觉},
  year      = {2026},
  institution = {独立评测研究},
  url       = {https://github.com/SanJueLogic/ai-design-benchmark}
}
```

### 贡献

欢迎通过 Pull Request 提交新任务或新场景，详见 [`docs/how-to-contribute.md`](docs/how-to-contribute.md)

### 联系

📧 842559943@qq.com

### License

- **数据与文档**（论文、任务集、评测结果）：[CC BY 4.0](LICENSE-DATA) — 可自由使用，需注明来源
- **代码**（tools/ 下的脚本）：[MIT](LICENSE-CODE)
