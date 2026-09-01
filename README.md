# MichengAI Skills

**中文** · [English](./README.en.md)

迷城 AI 的风格化照片编辑与旅行视觉 Skills 集合，遵循可被兼容 Agent Skills 的工具发现和调用的目录结构。每个 Skill 都有独立、可辨识的视觉语言，并提供中英文说明。

## Skills

展示名保留每个 Skill 的核心用途，便于理解和日常称呼；安装与调用仍以 `Skill ID` 为准。

| Skill | 展示名 | 功能 | 文档 | Skill ID |
| --- | --- | --- | --- | --- |
| MichengAI Photo Geometry Poster | **写实几何海报** | 将参考照片转化为“写实摄影 + 同构图几何插画 + 编辑排版”的竖版海报 | [中文](./michengai-photo-geometry-poster/README.md) · [English](./michengai-photo-geometry-poster/README.en.md) | `michengai-photo-geometry-poster` |
| MichengAI Photo Impasto Diorama Poster | **厚涂微景观海报** | 将每张照片分别制作成“真实编辑摄影 + 明亮留白中的 3D 厚涂油画微景观”的 3:4 对半海报 | [中文](./michengai-photo-impasto-diorama-poster/README.md) · [English](./michengai-photo-impasto-diorama-poster/README.en.md) | `michengai-photo-impasto-diorama-poster` |
| MichengAI Photo Isometric Impasto Atlas | **轴测厚涂场景图鉴** | 将每张照片制作成“可信现场摄影 + 同源轴测微缩场景 + 不规则颜料地形”的 3:4 等分图鉴海报 | [中文](./michengai-photo-isometric-impasto-atlas/README.md) · [English](./michengai-photo-isometric-impasto-atlas/README.en.md) | `michengai-photo-isometric-impasto-atlas` |
| MichengAI Photo Felt Relief Travel Archive | **羊毛毡浅浮雕旅行档案** | 将每张照片制作成“完整原始摄影 + 同视角手工毛毡与针毡羊毛浅浮雕”的 3:4 旅行档案海报 | [中文](./michengai-photo-felt-relief-travel-archive/README.md) · [English](./michengai-photo-felt-relief-travel-archive/README.en.md) | `michengai-photo-felt-relief-travel-archive` |
| MichengAI Photo Travel Ticket Collage | **照片旅行票根拼贴** | 将每张照片制作成“半幅真实原照 + 同源插画票卡 + 结构化票根与旅行邮戳”的 3:4 对照拼贴 | [中文](./michengai-photo-travel-ticket-collage/README.md) · [English](./michengai-photo-travel-ticket-collage/README.en.md) | `michengai-photo-travel-ticket-collage` |
| MichengAI Photo Sticker Sheet | **照片贴纸收藏卡** | 将参考照片转化为“写实主图 + 同源手绘明信片 + 原图元素模切贴纸”的收藏级竖版贴纸板 | [中文](./michengai-photo-sticker-sheet/README.md) · [English](./michengai-photo-sticker-sheet/README.en.md) | `michengai-photo-sticker-sheet` |
| MichengAI Photo Manga Sticker Fusion | **真人照片漫画贴纸融合** | 将一个人或多人群体转化为黑白手绘漫画贴纸，或在实景中自然加入漫画角色，同时严格保留摄影背景 | [中文](./michengai-photo-manga-sticker-fusion/README.md) · [English](./michengai-photo-manga-sticker-fusion/README.en.md) | `michengai-photo-manga-sticker-fusion` |
| MichengAI White-Space Memory Sketch | **中式留白记忆画页** | 将真实照片重绘为开放画域、少量元素越界、文字随图配色的中式纸本记忆画页 | [中文](./michengai-photo-white-space-memory-sketch/README.md) · [English](./michengai-photo-white-space-memory-sketch/README.en.md) | `michengai-photo-white-space-memory-sketch` |
| MichengAI Rubber Stamp Field Notes | **橡皮章田野笔记** | 将每张旅行照片分别制作成“真实照片 + 旧纸 + 小型多色橡皮章 + 中英文档案文字”的田野笔记 | [中文](./michengai-rubber-stamp-field-notes/README.md) · [English](./michengai-rubber-stamp-field-notes/README.en.md) | `michengai-rubber-stamp-field-notes` |
| MichengAI City Reflection Travel Print | **城市倒影旅行画** | 根据必填城市生成“当代旅行艺术 + 镜面倒影 + 杂志排版”的收藏级城市印刷品，支持尺寸、国家与标语 | [中文](./michengai-city-reflection-travel-print/README.md) · [English](./michengai-city-reflection-travel-print/README.en.md) | `michengai-city-reflection-travel-print` |
| MichengAI City Travel Postcard | **城市插画明信片** | 根据城市生成“日式旅游杂志插画 + 纸张拼贴 + 多语编辑排版”的旅行明信片，支持尺寸 | [中文](./michengai-city-travel-postcard/README.md) · [English](./michengai-city-travel-postcard/README.en.md) | `michengai-city-travel-postcard` |
| MichengAI Photo Abstract Travel Poster | **写实抽象旅行海报** | 基于参考照片制作“上部复古写实旅行摄影 + 下部中式留白意象转译 + 角落微型文字”的高级编辑海报 | [中文](./michengai-photo-illustration-travel-poster/README.md) · [English](./michengai-photo-illustration-travel-poster/README.en.md) | `michengai-photo-illustration-travel-poster` |

## 安装

推荐使用通用的 [Skills CLI](https://github.com/vercel-labs/skills)。它会从 GitHub 仓库识别包含 `SKILL.md` 的目录，并按当前 Agent 的规则安装。

查看可用 Skills：

```bash
npx skills add MichengAI/MichengAI-skills --list
```

安装单个 Skill：

```bash
npx skills add MichengAI/MichengAI-skills \
  --skill michengai-rubber-stamp-field-notes
```

安装仓库中的全部 Skills：

```bash
npx skills add MichengAI/MichengAI-skills \
  --skill "*"
```

如需固定安装到某个 Agent 的全局目录，请显式指定 Agent。以 Codex 为例：

```bash
npx skills add MichengAI/MichengAI-skills \
  --global --agent codex \
  --skill michengai-rubber-stamp-field-notes
```

也可以手动复制任一含 `SKILL.md` 的子目录到所用 Agent 的 Skills 目录。具体路径与调用语法请遵循该 Agent 的官方说明。

## 使用

在支持 Agent Skills 的客户端中，以该平台自己的调用语法引用上表中的 Skill ID。例如：

```text
使用 `michengai-photo-geometry-poster` 把这张照片处理成中文编辑海报。
```

```text
使用 `michengai-photo-sticker-sheet` 把这张照片制作成收藏级贴纸板。
```

```text
使用 `michengai-photo-manga-sticker-fusion` 把照片里的主角转化为黑白漫画贴纸，背景完全保持真实。
```

```text
使用 `michengai-photo-white-space-memory-sketch` 把这张照片重绘成中式纸本记忆画页，使用开放画域和少量越界元素，并让中英文页边注根据照片配色。
```

```text
使用 `michengai-photo-impasto-diorama-poster` 分别处理我上传的照片，每张单独输出一张 3:4 厚涂微景观海报。
```

```text
使用 `michengai-photo-isometric-impasto-atlas` 分别处理我上传的照片，每张单独输出一张 3:4 轴测厚涂场景图鉴。
```

```text
使用 `michengai-photo-felt-relief-travel-archive` 将我上传的每张照片分别制作成一张 3:4 羊毛毡浅浮雕旅行档案海报。
```

```text
使用 `michengai-photo-travel-ticket-collage` 把我上传的旅行照片制作成上部原照、下部旅行票根纪念卡的 3:4 对照拼贴。
```

```text
使用 `michengai-rubber-stamp-field-notes` 分别处理我上传的旅行照片，每张照片单独输出。
```

```text
使用 `michengai-city-reflection-travel-print` 生成城市旅行艺术印刷品。城市：香港；尺寸：3:4。
```

```text
使用 `michengai-city-travel-postcard` 生成城市插画明信片。城市：上海；尺寸：3:4。
```

```text
使用 `michengai-photo-illustration-travel-poster` 处理我上传的旅行照片，生成写实抽象旅行海报；尺寸：3:4。
```

在 Codex 中可使用其 `$skill-id` 语法；其他 Agent 则使用各自的 Skills 调用方式。

## 平台适配

每个子目录中的 `SKILL.md` 是跨 Agent 的核心指令与唯一事实来源。`agents/openai.yaml` 仅是可选的 OpenAI/Codex 展示元数据和默认提示，其他兼容客户端可忽略该文件。

## 仓库结构

```text
MichengAI-skills/
├── README.md
├── README.en.md
├── michengai-photo-geometry-poster/
│   ├── README.md
│   ├── README.en.md
│   ├── SKILL.md
│   ├── agents/              # 可选平台适配
│   ├── assets/demo/
│   └── references/
├── michengai-photo-sticker-sheet/
├── michengai-photo-manga-sticker-fusion/
├── michengai-photo-white-space-memory-sketch/
├── michengai-photo-impasto-diorama-poster/
├── michengai-photo-isometric-impasto-atlas/
├── michengai-photo-felt-relief-travel-archive/
├── michengai-photo-travel-ticket-collage/
├── michengai-rubber-stamp-field-notes/
├── michengai-city-reflection-travel-print/
├── michengai-city-travel-postcard/
└── michengai-photo-illustration-travel-poster/
```

各子 Skill 的详细能力、提示示例和演示图请查看对应目录中的 README。\n
