# AI Design Benchmark

**一套面向 AI 设计工具的系统性评测框架** | A reproducible benchmark framework for evaluating AI design tools

[![License: CC BY 4.0](https://img.shields.io/badge/Data%20License-CC%20BY%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)
[![License: MIT](https://img.shields.io/badge/Code%20License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Paper](https://img.shields.io/badge/Paper-v1.1-blue.svg)](paper/AI-Design-Benchmark-v1.1.md)

---

## 简介

本项目提供一套可复现的 AI 设计工具横向评测方法论，包含：

- **7 大设计场景、115 条评测任务**（Logo / IP 形象 / 徽章奖杯 / 商品海报 / 商品图片美化 / 线上营销活动 / 线下推广物料）
- **双盲 SbS（Side-by-Side）投票机制**：评测员在不知道图片来源的情况下逐题选出最优结果
- **四层聚合算法**：投票 → 题目 → 任务 → 场景，保证结论可复现
- **两步置信度量化**：票数集中度（≥20%/10-20%/<10%）+ Bootstrap 95% CI
- **Round 1 实证结果**：3 款公开 AI 设计工具（Lovart / 即梦 / Roboneo）横向对比数据

> 论文全文见 [`paper/`](paper/) | 方法论文档见 [`methodology/`](methodology/) | 任务集见 [`dataset/`](dataset/)

---

## 快速开始

### 环境要求

```bash
Python >= 3.9
pip install -r tools/requirements.txt
```

### 复现 Round 1 结果

```bash
git clone https://github.com/SanJueLogic/ai-design-benchmark
cd ai-design-benchmark
python tools/scoring.py --input results/round-1/raw-votes.csv --output results/round-1/aggregated-repro.csv
python tools/confidence.py --input results/round-1/aggregated-repro.csv
```

### 运行你自己的一轮评测

详见 [`docs/how-to-run-a-round.md`](docs/how-to-run-a-round.md)

---

## 目录结构

```
ai-design-benchmark/
├── paper/                        # 论文正文（中文 Markdown + PDF）
├── methodology/                  # 方法论文档（指标定义 / 打分规范 / 评测员协议）
├── dataset/
│   └── v1.0/
│       ├── tasks.json            # 结构化任务集（115 条）
│       ├── scenes/               # 按场景组织的任务书（Markdown）
│       └── reference-images/     # 编辑型任务参考图
├── results/
│   └── round-1/
│       ├── raw-votes.csv         # 原始投票数据（评测员已匿名）
│       ├── aggregated.csv        # 聚合胜率结果
│       └── analysis-reports/     # 场景级分析报告
├── tools/
│   ├── scoring.py                # 四层聚合打分脚本
│   ├── confidence.py             # 置信度与 Bootstrap CI 计算
│   └── sbs-template/             # SbS 投票网页模板
└── docs/
    ├── how-to-run-a-round.md     # 如何跑一轮评测
    ├── how-to-add-a-product.md   # 如何新增被评测产品
    └── how-to-contribute.md      # 如何贡献新任务
```

---

## Round 1 结果摘要

> 数据采集时间：2026 年 3-4 月 | 评测方式：双盲 SbS 图片排序 | 评测员：10 人（设计 5 / 研发 4 / 算法 1）

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

> 完整结果与置信度说明见 [`results/round-1/`](results/round-1/)

---

## 引用

如果本框架对你的研究有帮助，请引用：

```bibtex
@techreport{liu2026aidesignbenchmark,
  title     = {AI 设计工具评测 Benchmark v1.0：面向企业级设计场景的系统性横向评测框架},
  author    = {刘三觉},
  year      = {2026},
  institution = {独立评测研究},
  url       = {https://github.com/SanJueLogic/ai-design-benchmark}
}
```

---

## 贡献

欢迎通过 Pull Request 提交新任务或新场景，详见 [`docs/how-to-contribute.md`](docs/how-to-contribute.md)

---

## License

- **数据与文档**（论文、任务集、评测结果）：[CC BY 4.0](LICENSE-DATA) — 可自由使用，需注明来源
- **代码**（tools/ 下的脚本）：[MIT](LICENSE-CODE)
