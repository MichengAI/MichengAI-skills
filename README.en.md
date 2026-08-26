# MichengAI Skills

[中文](./README.md) · **English**

A collection of style-specific photo-editing skills for Codex. Each skill has a distinct visual language and separate Chinese and English documentation.

## Skills

| Skill | What it does | Documentation | Invoke with |
| --- | --- | --- | --- |
| MichengAI Photo Geometry Poster | Turns a reference photo into a portrait poster combining realistic photography, an aligned geometric reinterpretation, and editorial typography | [中文](./michengai-photo-geometry-poster/README.md) · [English](./michengai-photo-geometry-poster/README.en.md) | `$michengai-photo-geometry-poster` |
| MichengAI Rubber Stamp Field Notes | Turns each travel photo into a separate 4:3 field-note poster combining an authentic photograph, aged paper, a small multi-color rubber stamp, and localized Chinese or English archival text | [中文](./michengai-rubber-stamp-field-notes/README.md) · [English](./michengai-rubber-stamp-field-notes/README.en.md) | `$michengai-rubber-stamp-field-notes` |
| MichengAI City Reflection Travel Print | Creates a collectible city print with contemporary travel art, mirror-like reflections, and magazine typography; accepts city, size, country, and slogan inputs | [中文](./michengai-city-reflection-travel-print/README.md) · [English](./michengai-city-reflection-travel-print/README.en.md) | `$michengai-city-reflection-travel-print` |
| MichengAI City Travel Postcard | Creates a Japanese tourism-editorial illustrated postcard with paper collage and multilingual typography; accepts city and size inputs | [中文](./michengai-city-travel-postcard/README.md) · [English](./michengai-city-travel-postcard/README.en.md) | `$michengai-city-travel-postcard` |

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

Copy-Item -Recurse `
  .\MichengAI-skills\michengai-city-reflection-travel-print `
  "$HOME\.codex\skills\michengai-city-reflection-travel-print"

Copy-Item -Recurse `
  .\MichengAI-skills\michengai-city-travel-postcard `
  "$HOME\.codex\skills\michengai-city-travel-postcard"
```

macOS or Linux:

```bash
cp -R ./MichengAI-skills/michengai-photo-geometry-poster \
  ~/.codex/skills/michengai-photo-geometry-poster

cp -R ./MichengAI-skills/michengai-rubber-stamp-field-notes \
  ~/.codex/skills/michengai-rubber-stamp-field-notes

cp -R ./MichengAI-skills/michengai-city-reflection-travel-print \
  ~/.codex/skills/michengai-city-reflection-travel-print

cp -R ./MichengAI-skills/michengai-city-travel-postcard \
  ~/.codex/skills/michengai-city-travel-postcard
```

## Usage examples

```text
Use $michengai-photo-geometry-poster to turn my uploaded photo into a premium editorial poster.
```

```text
Use $michengai-rubber-stamp-field-notes to process each uploaded travel photo as a separate field-note poster.
```

```text
Use $michengai-city-reflection-travel-print to create a city travel art print. City: Hong Kong; Size: 3:4.
```

```text
Use $michengai-city-travel-postcard to create an illustrated travel postcard. City: Shanghai; Size: 3:4.
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
├── michengai-rubber-stamp-field-notes/
│   ├── README.md
│   ├── README.en.md
│   ├── SKILL.md
│   ├── agents/
│   ├── assets/demo/
│   └── references/
├── michengai-city-reflection-travel-print/
    ├── README.md
    ├── README.en.md
    ├── SKILL.md
    ├── agents/
    ├── assets/demo/
    └── references/
└── michengai-city-travel-postcard/
    ├── README.md
    ├── README.en.md
    ├── SKILL.md
    ├── agents/
    └── references/
```

See the README files inside each child skill for detailed behavior, prompts, and demos.
