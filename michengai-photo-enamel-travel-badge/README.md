# MichengAI 珐琅旅行纪念徽章

**中文** · [English](./README.en.md) · [返回仓库首页](../README.md)

从上传照片中提取最有识别度的单一视觉主体，将核心轮廓适度简化为金色金属边、微浮雕和珐琅填色的实体旅行纪念徽章，再与原照片组成上下对照的 `3:4` 竖版画页。

## 演示

| <strong>秋林越野车</strong><br><img src="./assets/demo/autumn-offroad-badge.webp" alt="秋林越野车珐琅旅行纪念徽章示例" height="480"> | <strong>露营猫咪</strong><br><img src="./assets/demo/camping-cat-badge.webp" alt="露营猫咪珐琅旅行纪念徽章示例" height="480"> |
| :--- | :--- |
| <strong>富士樱花</strong><br><img src="./assets/demo/fuji-sakura-badge.webp" alt="富士樱花珐琅旅行纪念徽章示例" height="480"> | <strong>山间四人合影</strong><br><img src="./assets/demo/mountain-four-person-badge.webp" alt="山间四人合影珐琅旅行纪念徽章示例" height="480"> |
| <strong>荒野锈车</strong><br><img src="./assets/demo/rusted-car-badge.webp" alt="荒野锈车珐琅旅行纪念徽章示例" height="480"> | <strong>席地吹笛人</strong><br><img src="./assets/demo/seated-flutist-badge.webp" alt="席地吹笛人珐琅旅行纪念徽章示例" height="480"> |
| <strong>雪地越野车</strong><br><img src="./assets/demo/snow-offroad-badge.webp" alt="雪地越野车珐琅旅行纪念徽章示例" height="480"> | <strong>窗边西瓜</strong><br><img src="./assets/demo/window-watermelon-badge.webp" alt="窗边西瓜珐琅旅行纪念徽章示例" height="480"> |

## 视觉结构

1. **上方原照片**：`3:2` 横向照片面板，保留主体、构图、光影、颜色和真实摄影质感。
2. **下方徽章陈列**：`3:2` 横向深色粗麻布面板，一枚徽章居中偏上，整体视觉体量约占画面 `25%–30%`；根据主体自然轮廓灵活缩放，四周保持大留白。
3. **整体画布**：两个等高 `3:2` 面板上下组合，形成严格的 `3:4` 竖版成品。

## 徽章工艺

- 外形跟随照片核心主体，不默认套用圆章或盾牌底板。
- 保留外轮廓、关键负形和最有辨识度的局部，舍弃细碎纹理与完整背景。
- 使用连续金色金属边、克制微浮雕和少量同源珐琅色。
- 采用左上主高光、右下柔和补光和自然接触投影，呈现可信实体厚度。
- 背景从原图提取和谐深色，并转为低反光的粗麻布质感。

## 边界

- 多张照片逐张处理，每张单独输出，不合并拼图。
- 下方只放一枚完整徽章，不添加文字、地图、飞机、指南针或其他通用旅行符号。
- 禁止扁平贴纸、白色刀模边、2D 矢量、满版场景、卡通、塑料滴胶、树脂玩具和写实环境道具。
- 原图不是 `3:2` 时，优先安全裁切；会损伤主体时使用同源边缘延展，禁止拉伸。
- 直接调用图片编辑或生成工具产出完整成品，不只返回提示词。

## 使用

```text
使用名为 `michengai-photo-enamel-travel-badge` 的 Skill，把这张照片制作成 3:4 珐琅旅行纪念徽章画页。
```

多张照片：

```text
使用名为 `michengai-photo-enamel-travel-badge` 的 Skill 分别处理我上传的照片，每张单独输出，不要拼图。
```

## 文件

- [`SKILL.md`](./SKILL.md)：输入规则、主体提炼、固定版式、徽章工艺和验收要求。
- [`references/prompt-template.md`](./references/prompt-template.md)：根据每张照片填写的中文图片生成模板。
- [`agents/openai.yaml`](./agents/openai.yaml)：可选的 OpenAI/Codex 展示元数据和默认提示；核心 Skill 可独立使用。
- [`assets/demo/`](./assets/demo/)：八张 `720×960` WebP 实际生成效果演示。
