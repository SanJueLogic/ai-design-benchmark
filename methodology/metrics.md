# Evaluation Metrics | 评测指标定义

[English](#english) | [中文](#中文)

---

## English

> This document corresponds to §5 and Appendix B of the paper.

### Core Metrics

#### 1. Task Understanding & Execution (Objective)

**Definition**: Whether the product correctly generated content matching the task prompt (element completeness, size/spec compliance, style direction).

**Evaluation question**: Q1 — "Looking at the task prompt, which image has the highest completion rate?"

**Calculation**: The product receiving the most votes on this question is considered the winner. Ties are allowed (both products count as winners when vote counts are equal).

#### 2. Basic Professional Quality (Objective)

**Definition**: Whether there are hard quality defects (text distortion / typos / blurry images / broken elements).

**Evaluation question**: Q2 — "Which image has the most accurate graphics/text, with no distortion or typo issues?"

#### 3. Visual Experience (Subjective)

**Definition**: Overall visual quality — style fit, color harmony, compositional balance, creative novelty.

**Evaluation question**: Q3 — "Which image is most memorable, with the strongest creativity and design sense?"

#### 4. Information Communication (Subjective)

**Definition**: Whether core information is communicated clearly and efficiently, with clear information hierarchy.

**Evaluation question**: Q4 — "Which image is most suitable for actual commercial use?"

#### 5. Overall Applicability (Mixed)

**Definition**: Holistic judgment — if you were the client, which image would you approve directly without requesting revisions?

**Evaluation question**: Q5 — "If you were the client, which image would you approve directly without asking for changes?"

### Aggregated Metrics

| Metric | Definition |
|--------|-----------|
| **Task Win Rate** | Products winning the most questions in a task win that task. `Task win rate = tasks won / total tasks in scene` |
| **Scene Win Rate** | Products winning the most tasks in a scene rank first |
| **Overall Win Rate** | Total tasks won across all scenes / total tasks |

### Confidence Metrics

**Ticket Concentration** — gap between 1st and 2nd place scene win rates:

| Gap | Confidence | Meaning |
|:---:|:----------:|---------|
| ≥ 20% | ✅ High | Directly citable |
| 10%–20% | ⚠️ Medium | Cite with caution |
| < 10% | ❌ Low | Limited statistical significance |

**Bootstrap CI** — 10,000 task-resample iterations (seed=42), 95% confidence interval. See `../tools/confidence.py`.

**Random baseline**: 33% (3-way selection). Products with overall win rates significantly above 33% have a statistically meaningful advantage.

---

## 中文

> 本文档对应论文 §5 与附录 B。

### 核心指标

#### 1. 任务理解与执行（客观）

**定义**：被评测产品是否按任务 Prompt 的要求正确生成了对应内容（元素完整性、尺寸/规格、风格方向）。

**评测题目**：Q1 — "对照任务 Prompt，哪张图的完成度最高？"

**计算方式**：该题获得评测员最多投票的产品视为"胜出"；允许并列。

#### 2. 基础专业质量（客观）

**定义**：是否存在图像硬伤（文字畸变 / 错别字 / 图像模糊 / 元素崩坏）。

**评测题目**：Q2 — "哪张图图形/文字最准确，没有崩坏/错别字问题？"

#### 3. 视觉体验效果（主观）

**定义**：视觉呈现的整体质感——风格契合度、配色和谐性、构图平衡感、创意新颖度。

**评测题目**：Q3 — "哪张图最有记忆点，创意和设计感最强？"

#### 4. 信息传达效果（主观）

**定义**：核心信息是否清晰高效传递，信息层级是否分明。

**评测题目**：Q4 — "哪张图最适合实际商用？"

#### 5. 综合应用性（混合）

**定义**：综合考量后，如果你是甲方，你会直接通过哪张（不要求返工）。

**评测题目**：Q5 — "如果你是甲方，你会直接通过哪张，不要求返工？"

### 聚合指标

| 指标 | 定义 |
|------|------|
| **任务胜率** | 5 题中赢得题目数最多的产品赢得该任务。`任务胜率 = 赢得任务数 / 该场景总任务数` |
| **场景胜率** | 赢得任务数最多者排名第一 |
| **总胜率** | 所有场景赢得任务数 ÷ 总任务数 |

### 置信度指标

**票数集中度** — 第一名与第二名场景胜率差值：

| 差距 | 置信度 | 含义 |
|:---:|:-----:|------|
| ≥ 20% | ✅ 高 | 可直接引用 |
| 10%–20% | ⚠️ 中 | 谨慎引用 |
| < 10% | ❌ 低 | 统计意义有限 |

**Bootstrap 置信区间**：10,000 次 task-resample（seed=42），95% CI。见 `../tools/confidence.py`。

**随机基准**：33%（3 选 1）。总胜率显著高于 33% 的产品具备统计优势。
