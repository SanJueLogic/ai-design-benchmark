# Product Image Enhancement — Evaluation Task Set

[English](#english) | [中文](#中文)

---

## English

> **Note**: This document is the generic cross-product evaluation version. Brand-specific content has been replaced with the fictional brand 'StarSelect / 星选'. Reference images for edit-type tasks are available in `../reference-images/` and can be used directly for evaluation.

| ID | Task Type | Prompt | Reference Image |
| :--- | :--- | :--- | :--- |
| B-001 | Ambiguous[^1] | Touch it up | ![B001.jpg](../reference-images/B001.jpg) |
| B-002 | Ambiguous[^1] | Make it cleaner | ![B002.jpg](../reference-images/B002.jpg) |
| B-003 | Ambiguous[^1] | Without changing the product packaging information, help me enhance this product image to make it more appealing | ![B003.png](../reference-images/B003.png) |
| B-004 | Ambiguous[^1] | Without changing the product packaging information, help me enhance this product image to make it more appealing | ![B004.png](../reference-images/B004.png) |
| B-005 | Explicit[^2] | Make this suitable as a main product image — without changing the product packaging information, enhance this product image: remove reflections, straighten edges, correct alignment, improve color contrast; size requirement 1600×1600px, product centered at 0.9 proportion, white background | ![B005.png](../reference-images/B005.png) |
| B-006 | Explicit[^2] | Take the strawberries out of this box, arrange them on a wooden tray for an e-commerce white-background image; strawberries should be slightly larger, must look realistic, retain dried leaves and white parts, approximately 14 pieces, casually placed on a wooden tray | ![B006.png](../reference-images/B006.png) |
| B-007 | Explicit[^2] | Remove the small part of the person in this poster that overlaps with the border | ![B007.jpg](../reference-images/B007.jpg) |
| B-008 | Explicit[^2] | Increase brightness and clarity; make the bed sheets look smoother | ![B008.jpg](../reference-images/B008.jpg) |
| B-009 | Explicit[^2] | Make this image clearer so it doesn't look blurry on a mobile phone | ![B009.png](../reference-images/B009.png) |
| B-010 | Explicit[^2] | Enhance the image — size 3333×2500, strong sense of space, bright and cozy scene, clean and tidy, bed sheets flat without wrinkles, without changing the original items | ![B010.jpg](../reference-images/B010.jpg) |
| B-011 | Explicit[^2] | Open the curtains and increase clarity | ![B011.jpg](../reference-images/B011.jpg) |
| B-012 | Explicit[^2] | Keep only the product, place the product in the center of the image, remove everything else | ![B012.jpg](../reference-images/B012.jpg) |
| B-013 | Explicit[^2] | Increase brightness; make the cup look smoother | ![B013.jpg](../reference-images/B013.jpg) |
| B-014 | Explicit[^2] | Make this suitable as a main product image — without changing the product packaging information, enhance this product image: remove reflections, straighten edges, correct alignment, improve color contrast; size requirement 1600×1600px, product centered at 0.9 proportion, white background; keep only this product | ![B014.jpg](../reference-images/B014.jpg) |
| B-015 | Edit-type[^3] | Based on this product photo, help me create an e-commerce white-background image — pastry only, no plastic packaging | ![B015.png](../reference-images/B015.png) |
| B-016 | Edit-type[^3] | Add a moon and starry sky to the background | ![B016.png](../reference-images/B016.png) |
| B-017 | Compound[^4] | Based on these two floor plan images, design a complete home interior design solution in modern minimalist style for a multi-generational family; bright and cozy main color tones with a premium feel | ![B017.png](../reference-images/B017.png) |
| B-018 | Compound[^4] | Image style: 'realistic photography' — adjust to high-definition quality, and complete the laptop and chair in front of the puppy | ![B018.png](../reference-images/B018.png) |
| B-019 | Compound[^4] | Design an animation of a glowing Easter egg rolling; the year number is on the egg, the rolling path forms a 'circle', symbolizing 'trapping good luck, circling happiness'; the dynamic version shows the egg rolling and growing larger, then bursting into fireworks made of brand elements | / |
| B-020 | Compound[^4] | A transparent takeout cup of iced Americano coffee — transparent plastic cup, flat lid, clearly visible ice cubes and dark coffee inside; white background directly behind; light shining from the left side of the cup, passing through the coffee and ice to create a translucent internal glow casting on the white background; high realism, premium commercial lighting | / |

[^1]: **Ambiguous task**: the prompt is imprecise and vague, testing the model's ability to understand and creatively interpret design requirements
[^2]: **Explicit task**: the prompt is precise, including specific brand name, style, color scheme, and composition requirements; tests the model's precise execution ability
[^3]: **Edit-type task**: based on editing an existing image; tests the model's image understanding and local editing ability
[^4]: **Compound task**: requires completing a primary design task plus scene extension or multiple proposals in one conversation; tests comprehensive ability

---

## 中文

# 商品图片美化设计场景评测任务集（通用竞品版）

> **说明**：本文档为通用竞品评测版本，已移除品牌特异性内容，适用于对各 AI 设计工具的横向评测。所有编辑型及明确型任务所需参考图已内置于 `images/` 目录，可直接执行评测，无需手动准备图片。

| 序号 | 题目类型 | 任务提示词 | 需要上传的图片 |
| :--- | :--- | :--- | :--- |
| B-001 | 模糊任务[^1] | 美化一下 | ![B001.jpg](../reference-images/B001.jpg) |
| B-002 | 模糊任务[^1] | 干净点 | ![B002.jpg](../reference-images/B002.jpg) |
| B-003 | 模糊任务[^1] | 不改变商品包装信息，帮我优化这张商品图片，使它更美观 | ![B003.png](../reference-images/B003.png) |
| B-004 | 模糊任务[^1] | 不改变商品包装信息，帮我优化这张商品图片，使它更美观 | ![B004.png](../reference-images/B004.png) |
| B-005 | 明确任务[^2] | 把这个图做成可以作为产品主图，不改变商品包装信息，帮我优化这张商品图片使它更美观，去掉反光，边缘变整齐，变正，颜色对比度好看，要求图片尺寸 1600\*1600，商品主体居中占比 0.9，白底图 | ![B005.png](../reference-images/B005.png) |
| B-006 | 明确任务[^2] | 把这盒草莓里面的草莓拿出来，放在木盘子里做一张电商白底图，要求草莓稍微大一点，一定要真实，保留枯叶和白色部分，数量大概14个，随意放在一个木盘子里 | ![B006.png](../reference-images/B006.png) |
| B-007 | 明确任务[^2] | 消除这张海报中人物图像遮住边框的一小部分 | ![B007.jpg](../reference-images/B007.jpg) |
| B-008 | 明确任务[^2] | 提高亮度和清晰度，床单平整一些 | ![B008.jpg](../reference-images/B008.jpg) |
| B-009 | 明确任务[^2] | 让这个图片更清晰，在手机上看的时候不要太糊 | ![B009.png](../reference-images/B009.png) |
| B-010 | 明确任务[^2] | 美化图片，尺寸为 3333x2500，空间感大，画面明亮温馨，干净整洁，床单平整无褶皱，未改变原有物品样子 | ![B010.jpg](../reference-images/B010.jpg) |
| B-011 | 明确任务[^2] | 打开窗帘，提高清晰度 | ![B011.jpg](../reference-images/B011.jpg) |
| B-012 | 明确任务[^2] | 仅保留产品，将产品放在图片中间，其余全部消除 | ![B012.jpg](../reference-images/B012.jpg) |
| B-013 | 明确任务[^2] | 提高亮度，杯子平整一些 | ![B013.jpg](../reference-images/B013.jpg) |
| B-014 | 明确任务[^2] | 把这个图做成可以作为产品主图，不改变商品包装信息，帮我优化这张商品图片使它更美观，去掉反光，边缘变整齐，变正，颜色对比度好看，要求图片尺寸 1600\*1600，商品主体居中占比 0.9，白底图，只要这个商品 | ![B014.jpg](../reference-images/B014.jpg) |
| B-015 | 编辑型需求[^3] | 根据这个图片的实物图，帮我制作它的电商白底图，只有糕点不要带塑料包装 | ![B015.png](../reference-images/B015.png) |
| B-016 | 编辑型需求[^3] | 背景加上月亮星空 | ![B016.png](../reference-images/B016.png) |
| B-017 | 复合型需求[^4] | 请根据这两张家装平面图，设计完整的家装设计方案，三代同堂现代简约风格，主要色调明亮温馨，带有高级质感 | ![B017.png](../reference-images/B017.png) |
| B-018 | 复合型需求[^4] | 图片风格："写实摄影"，把图片调整成高清画质，并且补全小狗面前的电脑和坐着的椅子 | ![B018.png](../reference-images/B018.png) |
| B-019 | 复合型需求[^4] | 设计正在滚一个发光的彩蛋，彩蛋上写有年份数字，滚动轨迹形成一个"圆圈"，寓意"圈住好运、圈出快乐"。动态版本可以让彩蛋越滚越大，最后炸开变成品牌元素组成的烟花 | — |
| B-020 | 复合型需求[^4] | 一杯透明外卖杯装的冰美式咖啡，透明塑料杯，平盖，杯内清晰可见冰块和深色咖啡，紧贴背后的白色背景，光线从杯子正左侧照射，穿过咖啡和冰块，形成通透的内部发光感，投射在紧贴着咖啡杯白色背景上，高真实度，高级商业光影 | — |

[^1]: **模糊任务**：用户的任务请求相对模糊，需要考验模型工具的理解能力
[^2]: **明确任务**：用户的任务请求非常具体，对处理效果有明确要求
[^3]: **编辑型需求**：基于已有图片进行编辑修改，考验模型的图像理解与局部编辑能力
[^4]: **复合型需求**：在一个需求中隐含多个任务请求
