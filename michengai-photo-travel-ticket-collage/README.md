# MichengAI Photo Travel Ticket Collage

**中文** · [English](./README.en.md) · [返回仓库首页](../README.md)

将一张参考照片制作成上下对照的竖版旅行纪念拼贴：上部以固定半幅保留真实原照，下部在轻盈纸张留白中放置一张同场景重绘的横向旅行票卡，并加入结构化票根、圆形旅行邮戳、英文标题与来源配色圆点。

## 输入

| 参数 | 是否必填 | 规则 |
| --- | --- | --- |
| `reference_image` | 是 | 每张照片独立处理，并作为该成品的唯一视觉来源；多张照片不合并。 |
| `size` | 否 | 默认竖版 `3:4`；其他比例仍保留上下结构。 |
| `title_text` | 否 | 票卡主标题；默认使用 `WANDERLUST`，用户明确指定时才替换。 |
| `subtitle_text` | 否 | 标题下方的一行英文短句；默认使用 `Collecting moments along the way.`。 |
| `ticket_text` | 否 | 可提供 `DESTINATION`、`SEASON`、`JOURNEY`、`MEMORY` 四组票据信息；未提供时按照片生成概念化纪念字段。 |

## 特征

- 水平分界锁定在画布高度的 `50%`，上下区域严格 `5:5`；上部照片以等比缩放、重新取景或同源扩景适配固定半幅，不会为了保留完整原图而扩大上半区。
- 下部以米白、浅灰或暖灰纸面留白承托横向票卡；以“主票 + 右侧票根”的完整纸张外轮廓计算，票卡宽度固定为画布宽度的 `83% ±1%`，并在下半区水平、垂直居中。
- 票卡把同一场景提炼为清新水彩、轻彩铅、淡水洗与旅行杂志插图融合的文艺插画，而不是机械描摹或照片滤镜。
- 右侧默认使用约占票卡宽度 20–24% 的可撕票根，包含场景图标、四组标签和值、分隔线、竖排旅行短句及小型符号。
- 票根底部加入场景自适应的圆形旅行纪念邮戳；主票使用默认系列标题、副标题和 5 个来源配色圆点。
- 无法确认真实地点时使用主题表达；编号与字段仅为概念化纪念设计，不冒充真实交通凭证，也不会把示例地标强加到其他照片。

## 使用

```text
使用 `michengai-photo-travel-ticket-collage` 把我上传的旅行照片制作成 3:4 旅行票根对照拼贴。
```

```text
使用 `michengai-photo-travel-ticket-collage` 分别处理我上传的每张照片，每张单独输出。
票根信息：DESTINATION—HIGH COUNTRY；SEASON—GOLDEN HOUR；JOURNEY—ALPINE WALK；MEMORY—NO. 0721
```

## 文件

- [`SKILL.md`](./SKILL.md)：输入、构图、票根结构、插画风格、文字与验收规则。
- [`references/prompt-template.md`](./references/prompt-template.md)：针对单张参考照片填写的中文图像编辑提示词模板。
- [`agents/openai.yaml`](./agents/openai.yaml)：可选的 OpenAI/Codex 展示元数据与默认提示。
