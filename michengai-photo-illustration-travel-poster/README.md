# MichengAI Photo Abstract Travel Poster

**中文** · [English](./README.en.md) · [返回仓库首页](../README.md)

基于参考照片制作高级写实抽象旅行海报：上部是带柔和胶片感的真实旅行摄影，下部以中式留白与意象提炼转译同一场景，只在角落保留微型地点与日期文字。

## 输入

| 参数 | 是否必填 | 规则 |
| --- | --- | --- |
| `reference_image` | 是 | 每张照片独立编辑并保留主体身份、数量、视角和空间关系；多张照片禁止合并。 |
| `location_text` | 否 | 用于角落地点小字；无法确认真实地点时使用通用场景名，不虚构城市。 |
| `date_text` | 否 | 未提供时使用当前公历年份。 |
| `size` | 否 | 支持比例或图像工具可接收的像素尺寸；默认请求 `3:4`。 |
| `language` | 否 | 控制角落文字语言；默认跟随当前对话语言。 |

## 特征

- 上部为温暖自然日光、轻雾、低反差、略微褪色与细腻胶片颗粒的写实旅行摄影。
- 下部使用暖象牙白纸面，以 1–3 个场景意象和 3–5 组主从形建立节奏；让“空白”成为画面的一部分，不是逐物手绘写生或缩小版照片。
- 上下两部分保持同一场景的主次、动势、疏密、方向与关键节奏；下部仅以无五官姿态、树团、屋顶点、舟形或倒影短线等有限线索传意，不描摹脸、纹理或逐物细节。
- 仅渲染地点和日期两处角落微型文字；禁止标题、口号、Logo 和水印。
- 中文提示词以参考照片为唯一视觉来源；不会把示例中的桥、船、河流或山景强行加入不相干的照片。

## 使用

```text
使用 `michengai-photo-illustration-travel-poster` 处理我上传的一张旅行照片，生成 3:4 写实抽象旅行海报。
地点文字：FIELD STUDY
日期文字：2026
```

```text
使用 `michengai-photo-illustration-travel-poster` 分别处理我上传的旅行照片，每张单独输出。
尺寸：4:5
```

## 演示

| <strong>高原人物</strong><br><img src="./assets/demo/plateau-monastics.webp" alt="高原人物写实手绘旅行海报演示" width="320"> | <strong>雪峰徒步</strong><br><img src="./assets/demo/snow-peak-hikers.webp" alt="雪峰徒步写实手绘旅行海报演示" width="320"> |
| :--- | :--- |
| <strong>山谷寺院</strong><br><img src="./assets/demo/mountain-monastery.webp" alt="山谷寺院写实手绘旅行海报演示" width="320"> | <strong>海岸落日</strong><br><img src="./assets/demo/coastal-sunset.webp" alt="海岸落日写实手绘旅行海报演示" width="320"> |
| <strong>岛屿乐声</strong><br><img src="./assets/demo/island-flutist.webp" alt="岛屿乐声写实手绘旅行海报演示" width="320"> | <strong>旷野花影</strong><br><img src="./assets/demo/flower-framed-dragon-blood-trees.webp" alt="旷野花影写实手绘旅行海报演示" width="320"> |

## 文件

- [`SKILL.md`](./SKILL.md)：输入、生成流程、视觉约束与验证标准。
- [`references/prompt-template.md`](./references/prompt-template.md)：以参考照片为唯一视觉来源、下部使用中式留白意象转译的中文提示词模板。
- [`agents/openai.yaml`](./agents/openai.yaml)：可选的 OpenAI/Codex 展示元数据与默认提示。
- [`assets/demo/`](./assets/demo/)：六张由参考照片生成的 3:4 演示图。\n
