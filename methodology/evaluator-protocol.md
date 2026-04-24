# Evaluator Protocol | 评测员协议

[English](#english) | [中文](#中文)

---

## English

> This document corresponds to §7.4 of the paper.

### Evaluator Composition

#### Round 1 Configuration

| Role | Count | Experience | Notes |
|------|:-----:|-----------|-------|
| Design | 5 | 3–8 years | Brand design, marketing design, or UI/UX experience |
| Engineering | 4 | 4–10 years | Software engineering background with basic aesthetic sense |
| ML/Algorithm | 1 | 3+ years | Participated in select scenes only; results are reference-only |

#### Recommended Configuration (Round 2+)

- At least **15 evaluators per scene**
- Add "target user" role (enterprise business stakeholders, brand managers)
- Role distribution: Design ≥ 40% / Engineering ≤ 40% / End users ≥ 20%

### Informed Consent

Before participating, each evaluator must understand and agree to:

1. **Purpose**: Cross-product comparison of AI design tool outputs across design scenarios
2. **Data use**: Voting data will be used to calculate product win rates and may be published as research data
3. **Anonymization**: All personal identifiers (names, abbreviation codes) will be replaced with anonymous codes (E01–E10) before public release
4. **Blind testing**: Product sources are not revealed during evaluation to ensure objectivity

### Blind Testing Protocol

**Administrator steps**:
1. For each task, arrange product outputs in random order (record the random seed for reproducibility)
2. Name images A/B/C (or anonymous numbers) — no product identifiers
3. Package the task prompt and corresponding images and distribute to evaluators

**Evaluator steps**:
1. View images independently — no discussion with other evaluators
2. Vote question-by-question following `scoring-guide.md`
3. Suggested time per scene: 30–60 minutes (~16–20 tasks × 5 questions)

### Bias Survey (Optional)

**After** evaluation (not before), ask evaluators:
- Did you guess the source product on any questions? (If yes, which type?)
- Which dimension was hardest to distinguish? (Completion / Quality / Visual / Commercial / Overall)
- What aesthetic style do you personally prefer? (International minimalist / Traditional Chinese / Trendy)

Bias survey results do not affect scoring but help explain inter-role divergence and improve future rounds.

### Data Management

- Raw votes stored in CSV format: `scene / evaluator / role / question / task / vote`
- `evaluator` column uses anonymous codes (E01–E10); real names are never stored
- Raw data: `results/round-{N}/raw-votes.csv`
- Aggregated results: `results/round-{N}/aggregated.csv`

---

## 中文

> 本文档对应论文 §7.4。

### 评测员构成要求

#### Round 1 配置

| 职能 | 人数 | 工龄要求 | 说明 |
|------|:---:|---------|------|
| 设计 | 5 人 | 3-8 年 | 具备品牌设计、营销设计或 UI/UX 工作经验 |
| 研发 | 4 人 | 4-10 年 | 软件工程背景，具备一定审美基础 |
| 算法 | 1 人 | 3 年以上 | 仅参与部分场景，结论供参考 |

#### 推荐配置（Round 2+）

- 每场景不少于 **15 人**
- 建议加入"目标用户"职能（企业业务方、品牌经理等）
- 各职能占比：设计 ≥ 40% / 研发 ≤ 40% / 用户 ≥ 20%

### 评测员知情与同意

参与前，每位评测员需了解并同意以下事项：

1. **评测目的**：横向对比 AI 设计工具在各设计场景中的表现
2. **数据用途**：投票数据将用于计算产品胜率，并可能作为研究数据公开发布
3. **匿名处理**：对外发布时，所有个人身份信息将替换为匿名代号（E01-E10）
4. **盲测说明**：评测过程中不会告知图片来源产品，确保结论客观性

### 盲测执行规范

**管理员操作**：
1. 对每道任务，将各产品生成结果图按随机顺序排列（使用随机数种子记录，便于复现）
2. 将图片命名为 A/B/C（或匿名数字），不包含任何产品标识
3. 将任务 Prompt 和对应图片打包发给评测员

**评测员执行**：
1. 独立查看图片，不与其他评测员讨论
2. 按 `scoring-guide.md` 的指引逐题投票
3. 每场景建议完成时间：30-60 分钟（约 16-20 任务 × 5 题）

### 偏差调查（可选）

**评测结束后**（不是之前），向评测员提出以下问题，用于识别系统性偏差：

- 你是否在某些题目上猜测出了图片来源？（如果是，请说明是哪类题目）
- 你在哪个维度上最难以区分？（完成度 / 质量 / 视觉 / 商用 / 综合）
- 你的审美倾向偏向哪类风格？（国际化简约 / 中式传统 / 流行潮流）

偏差调查结果不影响本轮计分，但用于解释职能间分歧及改进下一轮评测设计。

### 数据管理

- 原始投票记录以 CSV 格式存储，列包含：`scene / evaluator / role / question / task / vote`
- `evaluator` 列使用匿名代号（E01-E10），不存储真实姓名
- 原始数据文件存于 `results/round-{N}/raw-votes.csv`
- 聚合结果存于 `results/round-{N}/aggregated.csv`
