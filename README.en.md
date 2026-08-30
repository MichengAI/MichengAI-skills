# MichengAI Skills

[中文](./README.md) · **English**

A collection of MichengAI style-specific photo-editing and travel-visual skills. The repository follows a directory structure discoverable by compatible Agent Skills clients. Every skill has its own visual language and bilingual documentation.

## Skills

Display names retain each Skill's core purpose for clarity and everyday reference; installation and invocation still use the `Skill ID`.

| Skill | Display name | What it does | Documentation | Skill ID |
| --- | --- | --- | --- | --- |
| MichengAI Photo Geometry Poster | **Realistic Geometry Poster** | Turns a reference photo into a portrait poster combining realistic photography, an aligned geometric reinterpretation, and editorial typography | [中文](./michengai-photo-geometry-poster/README.md) · [English](./michengai-photo-geometry-poster/README.en.md) | `michengai-photo-geometry-poster` |
| MichengAI Photo Sticker Sheet | **Photo Sticker Card** | Turns a reference photo into a collectible portrait sheet combining a realistic hero photo, a matching hand-painted postcard, and source-derived die-cut stickers | [中文](./michengai-photo-sticker-sheet/README.md) · [English](./michengai-photo-sticker-sheet/README.en.md) | `michengai-photo-sticker-sheet` |
| MichengAI Rubber Stamp Field Notes | **Rubber Stamp Field Notes** | Turns each travel photo into a separate field-note poster combining an authentic photograph, aged paper, a small multi-color rubber stamp, and localized Chinese or English archival text | [中文](./michengai-rubber-stamp-field-notes/README.md) · [English](./michengai-rubber-stamp-field-notes/README.en.md) | `michengai-rubber-stamp-field-notes` |
| MichengAI City Reflection Travel Print | **City Reflection Travel Art** | Creates a collectible city print with contemporary travel art, mirror-like reflections, and magazine typography; accepts city, size, country, and slogan inputs | [中文](./michengai-city-reflection-travel-print/README.md) · [English](./michengai-city-reflection-travel-print/README.en.md) | `michengai-city-reflection-travel-print` |
| MichengAI City Travel Postcard | **Illustrated City Postcard** | Creates a Japanese tourism-editorial illustrated postcard with paper collage and multilingual typography; accepts city and size inputs | [中文](./michengai-city-travel-postcard/README.md) · [English](./michengai-city-travel-postcard/README.en.md) | `michengai-city-travel-postcard` |
| MichengAI Photo Illustration Travel Poster | **Photo-Illustration Travel Poster** | Creates from a scene or reference photo a premium editorial poster with nostalgic travel photography above, an aligned minimalist hand-drawn interpretation below, and tiny corner text | [中文](./michengai-photo-illustration-travel-poster/README.md) · [English](./michengai-photo-illustration-travel-poster/README.en.md) | `michengai-photo-illustration-travel-poster` |

## Installation

The recommended path is the cross-agent [Skills CLI](https://github.com/vercel-labs/skills). It discovers directories containing `SKILL.md` in this GitHub repository and installs them according to the active Agent's conventions.

List the available skills:

```bash
npx skills add MichengAI/MichengAI-skills --list
```

Install one skill:

```bash
npx skills add MichengAI/MichengAI-skills \
  --skill michengai-rubber-stamp-field-notes
```

Install every skill in this repository:

```bash
npx skills add MichengAI/MichengAI-skills \
  --skill "*"
```

To target one Agent's global skills directory, state the Agent explicitly. For example, for Codex:

```bash
npx skills add MichengAI/MichengAI-skills \
  --global --agent codex \
  --skill michengai-rubber-stamp-field-notes
```

As a manual fallback, copy any child directory containing `SKILL.md` into your Agent's skills directory. Use that Agent's documentation for its directory path and invocation syntax.

## Usage

In a compatible Agent Skills client, refer to a Skill ID using that client's own invocation convention. For example:

```text
Use the `michengai-photo-geometry-poster` skill to turn my uploaded photo into a premium editorial poster.
```

```text
Use the `michengai-photo-sticker-sheet` skill to turn my uploaded photo into a collectible sticker sheet.
```

```text
Use the `michengai-rubber-stamp-field-notes` skill to process each uploaded travel photo as a separate field-note poster.
```

```text
Use the `michengai-city-reflection-travel-print` skill to create a city travel art print. City: Hong Kong; Size: 3:4.
```

```text
Use the `michengai-city-travel-postcard` skill to create an illustrated travel postcard. City: Shanghai; Size: 3:4.
```

```text
Use the `michengai-photo-illustration-travel-poster` skill to create a photo-and-illustration travel poster. Scene: a historic riverside town; Size: 3:4.
```

Codex uses its `$skill-id` convention; other Agent clients use their own Skills invocation syntax.

## Platform adapters

`SKILL.md` in each child directory is the cross-agent core instruction and source of truth. `agents/openai.yaml` is optional OpenAI/Codex display metadata and a default prompt; compatible clients that do not use it can ignore it.

## Repository structure

```text
MichengAI-skills/
├── README.md
├── README.en.md
├── michengai-photo-geometry-poster/
│   ├── README.md
│   ├── README.en.md
│   ├── SKILL.md
│   ├── agents/              # optional platform adapters
│   ├── assets/demo/
│   └── references/
├── michengai-photo-sticker-sheet/
├── michengai-rubber-stamp-field-notes/
├── michengai-city-reflection-travel-print/
├── michengai-city-travel-postcard/
└── michengai-photo-illustration-travel-poster/
```

See each child skill's README for detailed behavior, prompt examples, and demos.
