# CHANGELOG

所有版本变更均记录于此文件，格式遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)。

---

## [v1.1] — 2026-04-23

### 新增

- **§9.5 数据污染防护（Contamination Protocol）**：明确声明"星选"为虚构品牌、任务 prompt 原创性、评测对象无关性、时间窗口冻结机制（对标 SWE-bench 做法）
- **§9.2 生成耗时数据**：补充 Round 1 各产品生成耗时分布表（部分缺失，Round 2 完整记录）
- **§10.1 Bootstrap 置信区间**：对 3 款产品胜率进行 10,000 次 task-resample Bootstrap（seed=42），Lovart 56%（95% CI: 47%–64%）/ 即梦 27%（19%–35%）/ Roboneo 19%（12%–27%）；新增 SOTA 基准注释
- **§10.7 典型失败模式分析**：各产品 3 个典型失败模式文字描述，含 L-1 至 R-3 共 9 个模式，图片案例存档于 GitHub `results/round-1/failure-cases/`（阶段二补充）
- **§12 社区生态建设**：新增 BIG-Bench 式社区贡献机制规划（task.json Schema / PR 模板 / Verified 子集 / 对抗性子集）
- **§12 评测维度扩展表**：新增未来计划扩展维度（生成耗时完整版、成本估算、Circular Evaluation、国际化任务集）
- **附录 F 场景标准卡（Scenario Cards）**：7 个场景各一张标准卡，含数据来源、任务数量、评测员配置、胜率摘要、置信度及备注（对标 HELM 做法）

### 修改

- **§7.4 评测员资质披露**：补充评测员代号（E01-E10）、职能工龄区间（设计 3-8 年 / 研发 4-10 年）、专业方向概述；新增"评测偏差调查"机制说明（对标 HELM / ChatBot Arena 评测员披露规范）
- **§11.1 评测员代号匿名化**：`FST、LXD 等` → `E01-E10 等`，避免个人信息泄露风险
- **§11.2 方法局限措辞**：将"Kappa 偏低"替换为"票数集中度偏低（差距 <10%）"，与 §8.3 框架保持一致

---

## [v1.0] — 2026-04-20

### 初版发布

- 完整论文稿首版，约 900 行，含 13 章 + 5 附录
- 脱敏完成：美团 / 美境 / 袋鼠团团 = 0 处
- 数据重算：剔除美境AI后 3 家横评，Lovart 56% / 即梦 27% / Roboneo 19%
- 参考文献：12 条 BibTeX（HELM / SWE-bench / ChatBot Arena / MMLU / MMMU / MMBench / DrawBench / GenEval / GAIA / HumanEval / Fleiss / Landis）
- GitHub 占位符填入：`SanJueLogic/ai-design-benchmark`
- 数据修正：线下推广物料 62% → 63%；线上营销活动差距 50% → 45%；IP形象 / 商品图片美化置信度标记由 ⚠️ 改为 ❌
- §10.4 完整重写：移除 Kappa 值（0.36 / 0.24 / 0.13 / 0.12），替换为票数集中度框架

---

## 版本号策略

- `v1.x`：对现有内容的渐进式改进（新增章节、数据修正、方法论完善）
- `v2.0`：Round 2 完成后，基于扩大评测员规模和新增场景的大版本更新
- 每个版本发布时同步更新 GitHub 库 `paper/` 目录下的 PDF 和 Markdown 文件
