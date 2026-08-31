# MichengAI White-Space Memory Sketch

**中文** · [English](./README.en.md) · [返回仓库首页](../README.md)

把真实照片重绘成一页当代中式纸本记忆画：留白参与构图，主画域开放而不封死，少量关键轮廓自然越界，中文题字与英文小注根据每张照片的色彩关系灵活配色。

## 视觉结构

1. **记忆锚点**：只保留 2–4 个最能确认主体、动作和空间关系的锚点，其余摄影微细节主动概括或删除。
2. **紧凑开放画域**：实际着色约占整页 25–32%，同时限制插画整体外包围并保留至少 10–15% 安静纸边；根据照片选择刷痕、卷轴、一角淡彩、斜向或宣纸撕边结构，不套居中矩形模板。
3. **克制越界**：选择 1–3 个塔尖、树枝、人物、绳索、水流、倒影或花簇等锚点轻微越出主画域，打破死板但不变成满版。
4. **局部色彩**：从原图提炼 2–4 个核心色，只在小画内部使用。
5. **中式双层页边注**：默认包含一条中文手写短句和一个更小的英文/日期标签；文字颜色从每张照片的深色与强调色中选择，不固定套用灰蓝。

## 效果对比

左侧原图保留各自的原始画幅比例，右侧重绘统一为 3:4。以下均为 WebP 展示图：原图最长边不超过 1200 px，重绘图为 900 × 1200 px，单张约 58–240 KiB。

| 原图 | 中式纸本记忆画 |
| --- | --- |
| **富士山与樱花**<br><img src="./assets/demo/fuji-cherry-before.webp" alt="富士山与樱花原图" height="320"> | <img src="./assets/demo/fuji-cherry-after.webp" alt="富士山与樱花重绘图" height="320"> |
| **雾中双瀑**<br><img src="./assets/demo/mist-twin-falls-before.webp" alt="雾中双瀑原图" height="320"> | <img src="./assets/demo/mist-twin-falls-after.webp" alt="雾中双瀑重绘图" height="320"> |
| **雪山攀登**<br><img src="./assets/demo/snow-climber-before.webp" alt="雪山攀登原图" height="320"> | <img src="./assets/demo/snow-climber-after.webp" alt="雪山攀登重绘图" height="320"> |
| **雨林瀑布**<br><img src="./assets/demo/rainforest-falls-before.webp" alt="雨林瀑布原图" height="320"> | <img src="./assets/demo/rainforest-falls-after.webp" alt="雨林瀑布重绘图" height="320"> |
| **高山湖**<br><img src="./assets/demo/alpine-lake-before.webp" alt="高山湖原图" height="320"> | <img src="./assets/demo/alpine-lake-after.webp" alt="高山湖重绘图" height="320"> |
| **窗边西瓜**<br><img src="./assets/demo/window-watermelon-before.webp" alt="窗边西瓜原图" height="320"> | <img src="./assets/demo/window-watermelon-after.webp" alt="窗边西瓜重绘图" height="320"> |

## 适用范围

- 日常随手拍、旅行碎片、宠物、食物、器物、窗景、街角、旧店、建筑与自然风景。
- 希望保留真实主体和空间关系，但不需要像素级还原的照片风格转译。
- 想把普通照片变成轻、静、带纸张呼吸感的小型手绘作品。

不适用于写真人像精修、旧照修复、商品广告、满版拼贴、大标题海报和密集信息图。

## 使用

```text
使用 `michengai-photo-white-space-memory-sketch` 把这张照片重绘成中式纸本记忆画页，保留人物姿态、窗框和下午斜光；让窗框或光影轻微越出主画域，题字颜色跟随照片。
```

指定页边注：

```text
使用 `michengai-photo-white-space-memory-sketch` 处理这张照片。中文小字使用“风在旧窗边停了一会儿”，档案标签使用“08.30 / HOME”。
```

多图处理：

```text
分别处理我上传的照片，每张单独输出一张 3:4 中式纸本记忆画页，版式和题字配色按各自照片决定，不要拼图。
```

## 文件

- [`SKILL.md`](./SKILL.md)：核心执行流程、视觉边界和验收标准。
- [`references/prompt-template.md`](./references/prompt-template.md)：完整中文自适应提示词与聚焦修正语句。
- [`agents/openai.yaml`](./agents/openai.yaml)：可选的 OpenAI/Codex 展示元数据和中文默认提示。
- [`assets/demo/`](./assets/demo/)：保留原图比例的压缩对比样张与 3:4 重绘样张。
