# CHANGELOG

[English](#english) | [中文](#中文)

All notable changes are documented here, following [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

---

## English

## [v1.1] — 2026-04-23

### Added

- **§9.5 Contamination Protocol**: explicit declaration that "StarSelect (星选)" is a fictional brand, all task prompts are original, and a time-window freeze mechanism (modeled after SWE-bench)
- **§9.2 Generation latency data**: Round 1 per-product latency distribution table (partial; complete recording planned for Round 2)
- **§10.1 Bootstrap confidence intervals**: 10,000-iteration task-resample Bootstrap (seed=42) — Lovart 56% (95% CI: 47%–64%) / Jimeng 27% (19%–35%) / Roboneo 19% (12%–27%); added SOTA reference annotation
- **§10.7 Typical failure pattern analysis**: 3 failure patterns per product, 9 patterns total (L-1 to R-3); image case archive in `results/round-1/failure-cases/` (to be added in Phase 2)
- **§12 Community ecosystem**: BIG-Bench-style community contribution mechanism (task.json schema / PR template / Verified subset / adversarial subset)
- **§12 Evaluation dimension expansion table**: planned future dimensions (full latency, cost estimation, Circular Evaluation, internationalized task set)
- **Appendix F Scenario Cards**: one standard card per scene (7 total), including data source, task count, evaluator configuration, win-rate summary, confidence, and notes (modeled after HELM)

### Changed

- **§7.4 Evaluator qualification disclosure**: added evaluator codes (E01–E10), role seniority ranges (Design 3–8 yrs / Engineering 4–10 yrs), and specialization overview; added "evaluator bias survey" mechanism (modeled after HELM / Chatbot Arena disclosure standards)
- **§11.1 Evaluator anonymization**: `FST, LXD, ...` → `E01–E10`, reducing personal identification risk
- **§11.2 Limitations wording**: replaced "low Kappa" with "low ticket concentration (gap <10%)", consistent with the §8.3 framework

## [v1.0] — 2026-04-20

### Initial Release

- Complete paper first version, ~900 lines, 13 chapters + 5 appendices
- Desensitization complete: 0 occurrences of internal company/product names
- Data recalculation: 3-product cross-comparison after excluding 4th product — Lovart 56% / Jimeng 27% / Roboneo 19%
- References: 12 BibTeX entries (HELM / SWE-bench / Chatbot Arena / MMLU / MMMU / MMBench / DrawBench / GenEval / GAIA / HumanEval / Fleiss / Landis)
- Data corrections: Offline Promotion 62% → 63%; Online Marketing gap 50% → 45%; IP Character / Image Enhancement confidence ⚠️ → ❌

## Versioning Policy

- `v1.x`: incremental improvements to existing content (new sections, data corrections, methodology refinements)
- `v2.0`: major update after Round 2, based on expanded evaluator pool and new scenes
- Each release updates both PDF and Markdown in the `paper/` directory

---

## 中文

所有版本变更均记录于此文件，格式遵循 [Keep a Changelog](https://keepachangelog.com/zh-CN/1.0.0/)。

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

## [v1.0] — 2026-04-20

### 初版发布

- 完整论文稿首版，约 900 行，含 13 章 + 5 附录
- 脱敏完成：内部公司/产品名称 = 0 处
- 数据重算：剔除第四家产品后 3 家横评，Lovart 56% / 即梦 27% / Roboneo 19%
- 参考文献：12 条 BibTeX（HELM / SWE-bench / ChatBot Arena / MMLU / MMMU / MMBench / DrawBench / GenEval / GAIA / HumanEval / Fleiss / Landis）
- GitHub 占位符填入：`SanJueLogic/ai-design-benchmark`
- 数据修正：线下推广物料 62% → 63%；线上营销活动差距 50% → 45%；IP形象 / 商品图片美化置信度标记由 ⚠️ 改为 ❌

## 版本号策略

- `v1.x`：对现有内容的渐进式改进（新增章节、数据修正、方法论完善）
- `v2.0`：Round 2 完成后，基于扩大评测员规模和新增场景的大版本更新
- 每个版本发布时同步更新 GitHub 库 `paper/` 目录下的 PDF 和 Markdown 文件
