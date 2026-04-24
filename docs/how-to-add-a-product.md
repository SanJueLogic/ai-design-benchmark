# How to Add a New Product | 如何新增被评测产品

[English](#english) | [中文](#中文)

---

## English

### Pre-checks

Before adding a new product, confirm:

- [ ] The product has a publicly accessible interface (web app / API)
- [ ] You have a legitimate account and usage rights
- [ ] The product's Terms of Service do not prohibit screenshots or publishing evaluation data

### Step 1 — Assign a Vote Number

Assign a numeric ID to the new product (must not conflict with existing products):

```
# Example: 4 products
--product-map "1:Lovart,2:Jimeng,3:Roboneo,4:NewProduct"
```

Note: Adding a product changes the random baseline from 33% to 25%. Confidence thresholds should be adjusted accordingly.

### Step 2 — Execute Tasks and Save Outputs

For each task:
1. Submit the same prompt (edit-type tasks: also upload the same reference image)
2. Save output images: `{scene_prefix}-{id}_result_{product}.jpg`
3. Record generation time (seconds)

### Step 3 — Include in Blind Test

Mix the new product's outputs with other products in the blind test sheet (evaluators cannot see product names).

### Step 4 — Update Vote Data

In `raw-votes.csv`, use your assigned numeric ID for the new product (e.g., `4`). Format is otherwise identical.

### Step 5 — Re-aggregate Results

Re-run scoring.py with the updated `--product-map`:

```bash
python tools/scoring.py \
  --input results/round-{N}/raw-votes.csv \
  --output results/round-{N}/aggregated.csv \
  --product-map "1:Lovart,2:Jimeng,3:Roboneo,4:NewProduct"
```

### Notes

- **Never modify published historical data**: Historical round conclusions only represent the products that participated in that round
- **Document product version**: Specify the version number and test date in your analysis report
- **Adjust confidence thresholds**: With 4 products, the random baseline is 25%; recommended thresholds: ≥15% = ✅, 8–15% = ⚠️, <8% = ❌

---

## 中文

### 前置检查

在新增产品前，请确认：

- [ ] 该产品有可访问的公开入口（网页版 / API）
- [ ] 你有合法的账号和使用权限
- [ ] 该产品的使用条款（ToS）不禁止截图和评测数据发布

### 第一步：分配投票编号

在你的评测轮次中，为新产品分配一个数字编号（不与现有产品冲突）：

```
# 示例：4 款产品
--product-map "1:Lovart,2:即梦,3:Roboneo,4:NewProduct"
```

注意：新增产品会改变随机基准（从 33% 变为 25%），置信度阈值需相应调整。

### 第二步：执行任务并保存结果

对每条任务：
1. 提交相同的 Prompt（编辑型任务上传相同的参考图）
2. 保存生成结果图，命名格式：`{场景前缀}-{序号}_result_{产品名}.jpg`
3. 记录生成耗时（秒）

### 第三步：纳入盲测

将新产品的结果图与其他产品一起打乱排列，制作盲测卷（评测员看不到产品名称）。

### 第四步：更新投票数据

在 `raw-votes.csv` 中，新产品的投票值使用你分配的编号（如 `4`），其余格式不变。

### 第五步：更新聚合结果

用新的 `--product-map` 重新运行 scoring.py：

```bash
python tools/scoring.py \
  --input results/round-{N}/raw-votes.csv \
  --output results/round-{N}/aggregated.csv \
  --product-map "1:Lovart,2:即梦,3:Roboneo,4:NewProduct"
```

### 注意事项

- **不要修改已发布的历史轮次数据**：历史轮次结论只代表当时参与的产品范围
- **注明产品版本**：在分析报告中说明新产品的版本号和测试时间
- **置信度阈值调整**：4 款产品时随机基准为 25%，建议阈值：≥15% = ✅，8-15% = ⚠️，<8% = ❌
