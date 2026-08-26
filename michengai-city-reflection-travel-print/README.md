# MichengAI City Reflection Travel Print

**中文** · [English](./README.en.md) · [返回仓库首页](../README.md)

根据城市生成可收藏的当代旅行艺术印刷品：城市真实的景观、建筑与文化环境融为一体，置于柔和的镜面倒影上，并配以克制的杂志排版。

## 输入

| 参数 | 是否必填 | 规则 |
| --- | --- | --- |
| `city` | 是 | 城市是画面核心和顶部标题。未提供时会先询问。 |
| `size` | 否 | 支持比例或像素尺寸；未提供时输出精确 `768×1024`（`3:4`）。 |
| `country` | 否 | 未提供时由城市可靠判断；城市有歧义时会先确认。 |
| `slogan` | 否 | 未提供时根据真实城市特征生成；提供后逐字使用。 |

## 视觉特征

- 以城市真实的地貌、滨水、街区和建筑语言建立一个连续环境，而非地标拼贴。
- 高级低饱和配色、水彩与水粉纸感、细腻建筑线稿和现代数字插画控制。
- 平静的玻璃感反射面，带柔和、略微褪色的垂直倒影。
- 极轻微的半透明几何边缘，营造当代画廊艺术感。
- 顶部只使用城市名、标语和 `No. 05 — 年份` 三项小号杂志文字；建筑与环境中不生成未指定文字。
- 生成后以非语义裁切和缩放交付精确尺寸，而非仅依赖提示词声明比例。

## 使用

```text
使用 $michengai-city-reflection-travel-print 生成城市旅行艺术印刷品。
城市：香港
国家：中国
尺寸：3:4
标语：一城烟火，两岸风华
```

只提供必填参数：

```text
使用 $michengai-city-reflection-travel-print 生成一张城市旅行艺术印刷品。
城市：里斯本
```

## 演示

以下实测结果均压缩为 **720 × 960 WebP**，并以 320px 宽双列展示，兼顾页面加载、版面秩序和文字可读性。

| 北京・一城古今，半卷山河 | 上海・海纳百川，光耀东方 |
| --- | --- |
| <img src="./assets/demo/beijing.webp" alt="北京城市倒影旅行印刷品演示" width="320"> | <img src="./assets/demo/shanghai.webp" alt="上海城市倒影旅行印刷品演示" width="320"> |
| 广州・市井千年，潮起岭南 | 深圳・青春热土，创领未来 |
| <img src="./assets/demo/guangzhou.webp" alt="广州城市倒影旅行印刷品演示" width="320"> | <img src="./assets/demo/shenzhen.webp" alt="深圳城市倒影旅行印刷品演示" width="320"> |
| 贵阳・山城绿意，云上清风 | 澳门・海湾旧梦，中西相映 |
| <img src="./assets/demo/guiyang.webp" alt="贵阳城市倒影旅行印刷品演示" width="320"> | <img src="./assets/demo/macau.webp" alt="澳门城市倒影旅行印刷品演示" width="320"> |

## 文件

- [`SKILL.md`](./SKILL.md)：参数规则、城市选择逻辑与视觉约束。
- [`references/prompt-template.md`](./references/prompt-template.md)：城市专属生成提示词模板。
- [`agents/openai.yaml`](./agents/openai.yaml)：Codex 展示名称和默认调用提示。
- [`scripts/fit_canvas.py`](./scripts/fit_canvas.py)：将生成结果裁切并缩放为精确交付尺寸。
