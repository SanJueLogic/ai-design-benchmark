# How to Run an Evaluation Round | 如何跑一轮评测

[English](#english) | [中文](#中文)

---

## English

### Prerequisites

- Python >= 3.9
- Accounts for at least 2 AI design tools to be evaluated
- 6+ evaluators (recommend a mix of design and engineering roles; see `methodology/evaluator-protocol.md`)

### Step 1 — Select Tasks

Choose the scenes and tasks for this round from `dataset/v1.0/tasks.json`:

```bash
python -c "
import json
data = json.load(open('dataset/v1.0/tasks.json'))
from collections import Counter
print(Counter(t['scene'] for t in data['tasks']))
"
```

Recommend 15–20 tasks per scene, covering all four task types: ambiguous / explicit / edit / compound.

### Step 2 — Collect Outputs

For each task, submit the same prompt to each product (edit-type tasks also require uploading the reference image). Save the output images.

Recommended naming: `{scene_prefix}-{id}_result_{product}.jpg`

### Step 3 — Prepare Blind Test Sheet

Gather all product outputs for the same task, arrange them in random order (no product labels), and create an evaluation sheet.

Use the HTML template in `tools/sbs-template/` to quickly generate an online voting sheet.

### Step 4 — Collect Votes

Evaluators vote question-by-question following `methodology/scoring-guide.md`. Record votes in CSV format:

```
scene, evaluator, role, question, task, vote
Logo Design, E01, Design, Q1, L-001, 1
```

`vote` values: `1/2/3` = product choice, `5` = about the same, `6` = not relevant

### Step 5 — Aggregate Win Rates

```bash
python tools/scoring.py \
  --input results/round-{N}/raw-votes.csv \
  --output results/round-{N}/aggregated.csv \
  --product-map "1:ProductA,2:ProductB,3:ProductC"
```

### Step 6 — Calculate Confidence

```bash
python tools/confidence.py \
  --input results/round-{N}/raw-votes.csv \
  --product-map "1:ProductA,2:ProductB,3:ProductC"
```

### Step 7 — Publish Results

Organize the following files under `results/round-{N}/`:
- `raw-votes.csv` (evaluator codes anonymized)
- `aggregated.csv`
- `analysis-reports/` (scene-level analysis reports in Markdown)

Submit via Pull Request or post the results link in Issues.

---

## 中文

### 前置准备

- Python >= 3.9
- 至少 2 款被评测的 AI 设计工具账号
- 6 名以上评测员（建议设计 + 研发职能混合，详见 `methodology/evaluator-protocol.md`）

### 第一步：选定任务集

从 `dataset/v1.0/tasks.json` 选择本轮要评测的场景和任务：

```bash
python -c "
import json
data = json.load(open('dataset/v1.0/tasks.json'))
from collections import Counter
print(Counter(t['scene'] for t in data['tasks']))
"
```

建议每场景选 15-20 条任务，覆盖模糊 / 明确 / 编辑型 / 复合型四种题型。

### 第二步：执行评测，采集生成结果

对每条任务，在各产品中分别提交 Prompt（编辑型任务同时上传参考图），保存生成结果图。

建议命名规范：`{场景前缀}-{序号}_result_{产品}.jpg`

### 第三步：制作盲测卷

将同一任务的各产品结果图汇总，用随机顺序排列（不标注产品名），制作成评测表格。

可使用 `tools/sbs-template/` 下的 HTML 模板快速生成在线评测表格。

### 第四步：评测员投票

评测员按 `methodology/scoring-guide.md` 的规范逐题投票，将投票结果记录为以下格式：

```
scene, evaluator, role, question, task, vote
Logo 设计, E01, 设计, Q1, L-001, 1
```

`vote` 取值：`1/2/3` = 对应产品，`5` = 差不多，`6` = 无关

### 第五步：聚合计算胜率

```bash
python tools/scoring.py \
  --input results/round-{N}/raw-votes.csv \
  --output results/round-{N}/aggregated.csv \
  --product-map "1:ProductA,2:ProductB,3:ProductC"
```

### 第六步：计算置信度

```bash
python tools/confidence.py \
  --input results/round-{N}/raw-votes.csv \
  --product-map "1:ProductA,2:ProductB,3:ProductC"
```

### 第七步：发布结果

在 `results/round-{N}/` 下整理以下文件：
- `raw-votes.csv`（评测员代码匿名化后）
- `aggregated.csv`
- `analysis-reports/`（各场景分析报告 Markdown）

通过 Pull Request 提交到本仓库，或在 Issues 中公布结果链接。
