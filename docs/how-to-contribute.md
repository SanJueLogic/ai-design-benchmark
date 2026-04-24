# How to Contribute | 如何贡献新任务

[English](#english) | [中文](#中文)

---

## English

Contributions of new evaluation tasks or design scenes via Pull Request are welcome.

### Contribution Types

| Type | Description |
|------|-------------|
| New tasks | Add task entries to existing 7 scenes |
| New scenes | Add a brand-new design scene (e.g., cultural T-shirts, product packaging, motion graphics) |
| Evaluation results | Submit your own evaluation data collected using this framework |
| Tool improvements | Improve `scoring.py`, `confidence.py`, or the SbS template |

### Contributing New Tasks

**Requirements**

- [ ] **Original prompts**: Not from other benchmarks or public datasets — written by you
- [ ] **No brand specificity**: No real brand names; use the fictional brand "StarSelect" or other fictional names
- [ ] **Clear task type**: One of four types — ambiguous / explicit / edit / compound
- [ ] **Directly executable**: Description is clear enough to paste directly into an AI design tool
- [ ] **Edit-type tasks include reference image**: Place in `dataset/v1.0/reference-images/` and explain in your PR

**JSON format (tasks.json entry)**

```json
{
  "id": "SP-021",
  "scene": "Product Poster Design",
  "scene_id": "product_poster_design",
  "type": "explicit",
  "prompt": "Design an e-commerce hero image for StarSelect nut gift box...",
  "has_reference_image": false
}
```

`type` values: `ambiguous` / `explicit` / `edit` / `compound`

**Submission steps**

1. Fork this repository
2. Add your entry to `dataset/v1.0/tasks.json` (keep IDs sequential)
3. If applicable, add reference images to `dataset/v1.0/reference-images/`
4. Submit a PR with description explaining:
   - Design intent of the task (what capability does it test?)
   - Why this task type was chosen
   - Whether you've tested it on any product (optional)

### Review Criteria

| Criterion | Description |
|-----------|-------------|
| Originality | Prompt not found in other public datasets |
| No brand specificity | No real brands, products, or individuals |
| Executability | Can be directly submitted to an AI design tool |
| Type distribution | New tasks should not over-concentrate in one type |

---

## 中文

欢迎通过 Pull Request 向本 benchmark 贡献新的评测任务或新的设计场景。

### 贡献类型

| 类型 | 说明 |
|------|------|
| 新任务 | 在现有 7 个场景中补充新的任务条目 |
| 新场景 | 增加全新的设计场景（如文化 T 恤、商品包装、营销动效） |
| 评测结果 | 提交你用本框架跑出的产品评测数据 |
| 工具改进 | 改进 scoring.py / confidence.py 或 SbS 模板 |

### 贡献新任务

**格式要求**

- [ ] **原创提示词**：不来自其他 benchmark 或公开数据集，由你本人原创
- [ ] **无品牌特异性**：提示词中不包含真实品牌名，使用虚构品牌"星选"或其他虚构名称
- [ ] **题型明确**：属于四种题型之一（模糊 / 明确 / 编辑型 / 复合型）
- [ ] **可直接执行**：任务描述清晰，可直接将 Prompt 粘贴到 AI 设计工具执行
- [ ] **编辑型任务需附参考图**：将参考图放入 `dataset/v1.0/reference-images/` 并在 PR 中说明

**JSON 格式（tasks.json 条目）**

```json
{
  "id": "SP-021",
  "scene": "商品海报设计",
  "scene_id": "product_poster_design",
  "type": "explicit",
  "prompt": "设计一张'星选'坚果礼盒的电商主图...",
  "has_reference_image": false
}
```

`type` 取值：`ambiguous` / `explicit` / `edit` / `compound`

**提交步骤**

1. Fork 本仓库
2. 在 `dataset/v1.0/tasks.json` 中新增条目（保持 id 连续）
3. 如有参考图，放入 `dataset/v1.0/reference-images/`
4. 提交 PR，PR 描述中说明：任务设计意图、题型选择理由、是否已在某款产品上测试过（非必须）

### 审核标准

| 标准 | 说明 |
|------|------|
| 原创性 | Prompt 未在其他公开数据集出现 |
| 无品牌特异性 | 不包含真实品牌、产品或人物 |
| 可执行性 | 可直接用于 AI 设计工具 |
| 题型分布 | 新任务不过度集中于某一题型 |

如有任何问题，请在 Issues 中提出。
