# MichengAI Skills

**中文** · [English](./README.en.md)

面向 Codex 的迷城 AI 风格化照片编辑 Skills 集合。每个 Skill 使用独立、可辨识的视觉语言，并提供中英文说明。

## Skills

| Skill | 功能 | 文档 | 调用方式 |
| --- | --- | --- | --- |
| MichengAI Photo Geometry Poster | 将参考照片转化为“写实摄影 + 同构图几何插画 + 编辑排版”的竖版海报 | [中文](./michengai-photo-geometry-poster/README.md) · [English](./michengai-photo-geometry-poster/README.en.md) | `$michengai-photo-geometry-poster` |
| MichengAI Rubber Stamp Field Notes | 将每张旅行照片分别制作成“真实照片 + 旧纸 + 小型多色橡皮章 + 中英文档案文字”的 4:3 横版田野笔记 | [中文](./michengai-rubber-stamp-field-notes/README.md) · [English](./michengai-rubber-stamp-field-notes/README.en.md) | `$michengai-rubber-stamp-field-notes` |
| MichengAI City Reflection Travel Print | 根据必填城市生成“当代旅行艺术 + 镜面倒影 + 杂志排版”的收藏级城市印刷品，支持尺寸、国家与标语 | [中文](./michengai-city-reflection-travel-print/README.md) · [English](./michengai-city-reflection-travel-print/README.en.md) | `$michengai-city-reflection-travel-print` |

## 安装

克隆仓库：

```bash
git clone https://github.com/MichengAI/MichengAI-skills.git
```

将需要的子 Skill 文件夹复制到 Codex Skills 目录：

```text
~/.codex/skills/
```

Windows PowerShell 示例：

```powershell
Copy-Item -Recurse `
  .\MichengAI-skills\michengai-photo-geometry-poster `
  "$HOME\.codex\skills\michengai-photo-geometry-poster"

Copy-Item -Recurse `
  .\MichengAI-skills\michengai-rubber-stamp-field-notes `
  "$HOME\.codex\skills\michengai-rubber-stamp-field-notes"

Copy-Item -Recurse `
  .\MichengAI-skills\michengai-city-reflection-travel-print `
  "$HOME\.codex\skills\michengai-city-reflection-travel-print"
```

macOS 或 Linux 示例：

```bash
cp -R ./MichengAI-skills/michengai-photo-geometry-poster \
  ~/.codex/skills/michengai-photo-geometry-poster

cp -R ./MichengAI-skills/michengai-rubber-stamp-field-notes \
  ~/.codex/skills/michengai-rubber-stamp-field-notes

cp -R ./MichengAI-skills/michengai-city-reflection-travel-print \
  ~/.codex/skills/michengai-city-reflection-travel-print
```

## 使用示例

```text
使用 $michengai-photo-geometry-poster 把这张照片处理成中文编辑海报。
```

```text
使用 $michengai-rubber-stamp-field-notes 分别处理我上传的旅行照片，每张照片单独输出。
```

```text
使用 $michengai-city-reflection-travel-print 生成城市旅行艺术印刷品。城市：香港；尺寸：3:4。
```

## 仓库结构

```text
MichengAI-skills/
├── README.md
├── README.en.md
├── michengai-photo-geometry-poster/
│   ├── README.md
│   ├── README.en.md
│   ├── SKILL.md
│   ├── agents/
│   ├── assets/demo/
│   └── references/
├── michengai-rubber-stamp-field-notes/
│   ├── README.md
│   ├── README.en.md
│   ├── SKILL.md
│   ├── agents/
│   ├── assets/demo/
│   └── references/
└── michengai-city-reflection-travel-print/
    ├── README.md
    ├── README.en.md
    ├── SKILL.md
    ├── agents/
    ├── assets/demo/
    └── references/
```

各子 Skill 的详细能力、提示示例和演示图请查看对应目录中的 README。
