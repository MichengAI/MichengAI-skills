# MichengAI Skills

面向 Codex 的迷城 AI 个人创作 Skills 集合。

当前仓库收录了一套照片编辑 Skill：将参考照片重制为“写实摄影 + 同构图几何插画 + 编辑排版”的竖版海报。

[English](#english)

## Skills

| Skill | 功能 | 调用方式 |
| --- | --- | --- |
| [MichengAI Photo Geometry Poster](./michengai-photo-geometry-poster/) | 保留参考照片的构图、透视和主体，上半部生成写实摄影，下半部生成几何块面转译，并加入编辑杂志式排版 | `$michengai-photo-geometry-poster` |

## MichengAI Photo Geometry Poster

### 视觉结构

1. **写实摄影区**：保留参考照片的主体、取景、视角、透视、地平线、主色和标志性轮廓。
2. **几何转译区**：用干净的矩形与多边形重构同一场景，保持对应的视角、比例和视觉层级。
3. **编辑排版区**：生成标题、副标题和年份，形成建筑、旅行或城市文化杂志式海报。

### 特性

- 支持城市、建筑、自然风景与旅行照片。
- 支持中文和英文标题、副标题。
- 未指定语言时跟随当前对话语言；中文请求默认生成中文文案。
- 中文标题使用 4–10 个汉字，英文标题使用 2–5 个单词。
- 使用现代无衬线字体和克制的深色排版。
- 不主动添加额外文字、Logo、水印或无关物体。
- 直接调用图片编辑/生成工具产出成品，而不只是返回提示词。

## 安装

克隆仓库：

```bash
git clone https://github.com/MichengAI/MichengAI-skills.git
```

将 Skill 文件夹复制到 Codex Skills 目录：

```text
~/.codex/skills/michengai-photo-geometry-poster/
```

Windows PowerShell 示例：

```powershell
Copy-Item -Recurse `
  .\MichengAI-skills\michengai-photo-geometry-poster `
  "$HOME\.codex\skills\michengai-photo-geometry-poster"
```

macOS 或 Linux 示例：

```bash
cp -R ./MichengAI-skills/michengai-photo-geometry-poster \
  ~/.codex/skills/michengai-photo-geometry-poster
```

## 使用

上传一张参考照片，然后调用：

```text
使用 $michengai-photo-geometry-poster 把这张照片处理成中文编辑海报。
```

也可以指定文案：

```text
使用 $michengai-photo-geometry-poster 处理这张照片。
标题使用“湖畔金晖”，副标题使用“宫阁依山而立，在澄澈秋光中俯瞰湖面。”，年份使用 2026。
```

## 目录结构

```text
MichengAI-skills/
├── README.md
└── michengai-photo-geometry-poster/
    ├── SKILL.md
    ├── agents/
    │   └── openai.yaml
    └── references/
        └── prompt-template.md
```

---

## English

**MichengAI Skills** is a collection of personal creative skills for Codex.

The current skill, **MichengAI Photo Geometry Poster**, transforms an uploaded reference photo into a premium portrait editorial poster with three coordinated layers:

1. A realistic photographic reconstruction that preserves the original composition and perspective.
2. A geometric reinterpretation of the same scene using clean rectangular and polygonal forms.
3. A restrained typography section with a title, subtitle, and year.

It supports both Chinese and English copy, follows the user's requested language, and works with city, architecture, landscape, and travel photography.

Invoke it with:

```text
Use $michengai-photo-geometry-poster to turn my uploaded photo into a premium editorial poster.
```
