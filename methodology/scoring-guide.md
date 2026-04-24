# Scoring Guide | 打分操作规范

[English](#english) | [中文](#中文)

---

## English

> This document corresponds to §8 of the paper. Use it as a reference when conducting SbS voting.

### Evaluation Flow

1. The administrator collects outputs for the same task from all products, shuffles the order, and removes product labels
2. Each evaluator independently opens the evaluation sheet and selects the "best" image for each question
3. After all evaluators complete voting, the administrator aggregates votes using the 4-layer algorithm

### Voting Options

| Option | Meaning | Counts toward win rate? |
|--------|---------|:-----------------------:|
| A / B / C | This product is best on this question | ✅ Yes |
| About the same | Products perform similarly on this question | ❌ No |
| Not relevant to task | The question has a design flaw, or the images can't answer it | ❌ No |

> **Note**: Only one option per question. If you genuinely can't distinguish, choose "About the same" — don't force a pick.

### Question-by-Question Guide

**Q1 — Completion Rate (Objective)**
> "Looking at the task prompt, which image has the highest completion rate?"

Look at: Are all required elements present? Does the size/ratio meet requirements? Does the style direction match?
Don't look at: Whether it looks good — only whether it was executed correctly.

**Q2 — Basic Quality (Objective)**
> "Which image has the most accurate graphics/text, with no distortion or typo issues?"

Look at: Text correctness, element integrity, image clarity.
Tip: First eliminate images with hard defects, then pick the best from the rest.

**Q3 — Visual Experience (Subjective)**
> "Which image is most memorable, with the strongest creativity and design sense?"

Look at: Overall visual impact, color harmony, compositional balance, creative novelty.
Note: This is subjective — different evaluators giving different answers is normal.

**Q4 — Commercial Fit (Subjective)**
> "Which image is most suitable for actual commercial use?"

Look at: Clear information hierarchy, prominent key selling points, overall readiness for deployment.

**Q5 — Overall Judgment (Mixed)**
> "If you were the client, which image would you approve directly without asking for changes?"

Look at: Synthesize all dimensions above from a real client perspective.

### Calibration

Before each round, the administrator provides 2–3 calibration questions (with known answers). All evaluators complete these first to align their understanding before beginning the actual evaluation.

---

## 中文

> 本文档对应论文 §8，供评测员在执行 SbS 投票时参照使用。

### 评测流程概览

1. 管理员将同一任务的各产品输出图汇总，打乱排列顺序，不标注产品名称
2. 评测员独立打开评测表格，对每道题选出"最好的一张"
3. 所有评测员完成后，管理员汇总投票，按四层聚合算法计算胜率

### 投票选项说明

| 选项 | 含义 | 是否计入胜率 |
|------|------|:----------:|
| A / B / C | 该产品在此题最好 | ✅ 计入 |
| 差不多 | 几款产品在此题表现相近，无明显差异 | ❌ 不计入 |
| 此题目与任务无关 | 题目本身有缺陷，或图片无法回答该问题 | ❌ 不计入 |

> **注意**：每题只能选一个选项。如果真的难以区分，选"差不多"，不要强行选出一个。

### 逐题打分指引

**Q1 — 完成度（客观）**
> "对照任务 Prompt，哪张图的完成度最高？"

看什么：要求的元素是否都在图里？尺寸/比例是否符合？风格方向是否有所体现？
不看什么：不考虑"好不好看"，只看"做没做到"。

**Q2 — 基础质量（客观）**
> "哪张图图形/文字最准确，没有崩坏/错别字问题？"

看什么：文字是否正确、图形是否完整、图像是否清晰。
技巧：先用排除法剔除有硬伤的，再从剩余中选最好的。

**Q3 — 视觉体验（主观）**
> "哪张图最有记忆点，创意和设计感最强？"

看什么：整体视觉冲击力、配色和谐度、构图平衡感、创意新颖度。
注意：这是主观题，不同评测员给出不同答案是正常的。

**Q4 — 商用适配（主观）**
> "哪张图最适合实际商用？"

看什么：信息层级是否清晰、核心卖点是否突出、整体完成度能否直接投放使用。

**Q5 — 综合判断（混合）**
> "如果你是甲方，你会直接通过哪张，不要求返工？"

看什么：综合以上所有维度，模拟真实甲方视角给出最终判断。

### 校准机制

每轮评测开始前，管理员提供 2-3 道"校准题"（已知答案的示例），所有评测员先完成校准题并对齐理解后，再开始正式评测。
