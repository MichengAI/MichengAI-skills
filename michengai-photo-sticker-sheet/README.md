# MichengAI Photo Sticker Sheet

**中文** · [English](./README.en.md) · [返回仓库首页](../README.md)

将上传的参考照片重制为收藏级竖版贴纸板：上方保留写实主图，左下转译为同场景手绘明信片，右下提取原图中的代表性元素制作成规整、不越界的模切贴纸。

## 演示

| <strong>荒野旧车</strong><br><img src="./assets/demo/abandoned-green-car.webp" alt="荒野旧车贴纸板示例" height="480"> | <strong>风暴雪山</strong><br><img src="./assets/demo/storm-mountain-river.webp" alt="风暴雪山贴纸板示例" height="480"> |
| :--- | :--- |
| <strong>雪中神社</strong><br><img src="./assets/demo/snow-forest-shrine.webp" alt="雪中神社贴纸板示例" height="480"> | <strong>林间石刻</strong><br><img src="./assets/demo/moss-prayer-stone.webp" alt="林间石刻贴纸板示例" height="480"> |
| <strong>冬日榻榻米</strong><br><img src="./assets/demo/sunlit-tatami-room.webp" alt="冬日榻榻米贴纸板示例" height="480"> | <strong>高台锈车</strong><br><img src="./assets/demo/rusted-station-wagon.webp" alt="高台锈车贴纸板示例" height="480"> |

## 视觉结构

1. **上方写实主图**：保留参考照片的主体、场景、空间关系、色彩、光线和氛围。
2. **左下手绘明信片**：以水彩、石版画或旅行插画重新表现同一场景，完整保留四条边框。
3. **右下模切贴纸**：从原图提取 4–6 个代表性元素，使用白色刀模边与轻微投影进行规整陈列。

## 特性

- 适用于旅行、建筑、自然、静物、食物、商品和日常场景照片。
- 默认输出 4:5 竖版；明确指定其他比例时可自适应。
- 多张照片逐张处理，每张照片单独输出，禁止合并拼图。
- 所有贴纸必须来自原图，不凭空添加无关元素。
- 采用严格三区布局，禁止贴纸压住明信片、互相重叠、越界或被裁切。
- 默认不生成标题、随机文字、Logo、水印或手机界面。
- 直接调用图片编辑/生成工具产出成品，而不是只返回提示词。

## 使用

```text
使用名为 `michengai-photo-sticker-sheet` 的 Skill，把这张照片制作成收藏级贴纸板。
```

多张照片：

```text
使用名为 `michengai-photo-sticker-sheet` 的 Skill 分别处理我上传的照片，每张单独输出，不要拼图。
```

## 文件

- [`SKILL.md`](./SKILL.md)：输入规则、生成流程、三区版式与验证要求。
- [`references/prompt-template.md`](./references/prompt-template.md)：强调边界稳定性的自适应图片生成模板。
- [`agents/openai.yaml`](./agents/openai.yaml)：可选的 OpenAI/Codex 集成元数据和默认提示；核心 Skill 可独立使用。
- [`assets/demo/`](./assets/demo/)：六张实际生成效果演示。
