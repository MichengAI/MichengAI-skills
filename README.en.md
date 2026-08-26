# MichengAI Skills

[中文](./README.md) · **English**

A collection of style-specific photo-editing skills for Codex. Each skill has a distinct visual language and separate Chinese and English documentation.

## Skills

| Skill | What it does | Documentation | Invoke with |
| --- | --- | --- | --- |
| MichengAI Photo Geometry Poster | Turns a reference photo into a portrait poster combining realistic photography, an aligned geometric reinterpretation, and editorial typography | [中文](./michengai-photo-geometry-poster/README.md) · [English](./michengai-photo-geometry-poster/README.en.md) | `$michengai-photo-geometry-poster` |
| MichengAI Rubber Stamp Field Notes | Turns each travel photo into a separate 4:3 field-note poster combining an authentic photograph, aged paper, a small multi-color rubber stamp, and archival English text | [中文](./michengai-rubber-stamp-field-notes/README.md) · [English](./michengai-rubber-stamp-field-notes/README.en.md) | `$michengai-rubber-stamp-field-notes` |

## Installation

Clone the repository:

```bash
git clone https://github.com/MichengAI/MichengAI-skills.git
```

Copy the skill folders you need into the Codex skills directory:

```text
~/.codex/skills/
```

Windows PowerShell:

```powershell
Copy-Item -Recurse `
  .\MichengAI-skills\michengai-photo-geometry-poster `
  "$HOME\.codex\skills\michengai-photo-geometry-poster"

Copy-Item -Recurse `
  .\MichengAI-skills\michengai-rubber-stamp-field-notes `
  "$HOME\.codex\skills\michengai-rubber-stamp-field-notes"
```

macOS or Linux:

```bash
cp -R ./MichengAI-skills/michengai-photo-geometry-poster \
  ~/.codex/skills/michengai-photo-geometry-poster

cp -R ./MichengAI-skills/michengai-rubber-stamp-field-notes \
  ~/.codex/skills/michengai-rubber-stamp-field-notes
```

## Usage examples

```text
Use $michengai-photo-geometry-poster to turn my uploaded photo into a premium editorial poster.
```

```text
Use $michengai-rubber-stamp-field-notes to process each uploaded travel photo as a separate field-note poster.
```

## Repository structure

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
└── michengai-rubber-stamp-field-notes/
    ├── README.md
    ├── README.en.md
    ├── SKILL.md
    ├── agents/
    └── references/
```

See the README files inside each child skill for detailed behavior, prompts, and demos.
