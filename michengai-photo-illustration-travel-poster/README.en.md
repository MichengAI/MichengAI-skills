# MichengAI Photo Illustration Travel Poster

[中文](./README.md) · **English** · [Back to repository](../README.en.md)

Creates a premium travel poster from either a reference photograph or a scene description, with soft film-like photography above and a sparse hand-drawn reinterpretation of the same scene below. Only tiny location and date text appears near the corners.

## Inputs

| Parameter | Required | Behavior |
| --- | --- | --- |
| `reference_image` | No | When supplied, each photo is edited independently while preserving subject identity, count, viewpoint, and spatial relationships. Multiple photos are never combined. |
| `scene` | No | Defaults to a historic riverside town with wooden boats, a stone arch bridge, mature trees, and misty karst mountains. |
| `location_text` | No | Used as tiny corner text. When a real place cannot be confirmed, the skill uses a generic scene label instead of inventing a city. |
| `date_text` | No | Defaults to the current calendar year. |
| `size` | No | Accepts a ratio or pixels supported by the image tool; defaults to a `3:4` request. |
| `language` | No | Controls the corner text language; defaults to the current conversation language. |

## Characteristics

- Uses warm daylight, gentle haze, soft contrast, slightly faded film color, and subtle analog grain in the upper photograph.
- Uses warm ivory paper, sparse lines, imperfect brush texture, muted earth colors, and generous negative space below.
- Keeps both sections aligned to the same scene, viewpoint, subject positions, and spatial relationships.
- Renders only two tiny text elements: location and date. No title, slogan, logo, or watermark.
- Supports both reference-photo editing and scene generation; when a photo is supplied, source fidelity takes priority.

## Usage

```text
Use `michengai-photo-illustration-travel-poster` to create a 3:4 photo-and-illustration travel poster.
Scene: a historic riverside town
Location text: River Town
Date text: 2026
```

```text
Use `michengai-photo-illustration-travel-poster` to create a travel poster.
Scene: a quiet coastal fishing village with distant mountains
Size: 4:5
```

## Demos

| <strong>Plateau figures</strong><br><img src="./assets/demo/plateau-monastics.webp" alt="Plateau figures photo-illustration travel poster demo" width="320"> | <strong>Snow-peak hikers</strong><br><img src="./assets/demo/snow-peak-hikers.webp" alt="Snow-peak hikers photo-illustration travel poster demo" width="320"> |
| :--- | :--- |
| <strong>Mountain monastery</strong><br><img src="./assets/demo/mountain-monastery.webp" alt="Mountain monastery photo-illustration travel poster demo" width="320"> | <strong>Coastal sunset</strong><br><img src="./assets/demo/coastal-sunset.webp" alt="Coastal sunset photo-illustration travel poster demo" width="320"> |
| <strong>Island flutist</strong><br><img src="./assets/demo/island-flutist.webp" alt="Island flutist photo-illustration travel poster demo" width="320"> | <strong>Flower-framed dragon blood trees</strong><br><img src="./assets/demo/flower-framed-dragon-blood-trees.webp" alt="Flower-framed dragon blood trees photo-illustration travel poster demo" width="320"> |

## Files

- [`SKILL.md`](./SKILL.md): inputs, workflow, visual constraints, and validation criteria.
- [`references/prompt-template.md`](./references/prompt-template.md): the original English prompt translated and structured as a reusable Chinese generation template.
- [`agents/openai.yaml`](./agents/openai.yaml): optional OpenAI/Codex UI metadata and default prompt.
- [`assets/demo/`](./assets/demo/): six 3:4 examples created from reference photographs.
