# MichengAI Photo Geometry Poster

[中文](./README.md) · **English** · [Back to repository](../README.en.md)

Transforms an uploaded reference photo into a premium portrait editorial poster. The upper panel remains realistic photography, the lower panel geometrically reinterprets the same composition and perspective, and the footer adds restrained title, subtitle, and year typography.

## Demos

| <strong>Storm over Snow Peaks</strong><br><img src="./assets/demo/snow-peak-storm.webp" alt="Storm over Snow Peaks demo" height="480"> | <strong>Starlight on Water</strong><br><img src="./assets/demo/sparkling-water.webp" alt="Starlight on Water demo" height="480"> |
| :--- | :--- |
| <strong>Mist Beyond the Window</strong><br><img src="./assets/demo/misty-valley-window.webp" alt="Mist Beyond the Window demo" height="480"> | <strong>Wilderness Green Car</strong><br><img src="./assets/demo/wilderness-green-car.webp" alt="Wilderness Green Car demo" height="480"> |
| <strong>Shrine in Snow</strong><br><img src="./assets/demo/snow-shrine.webp" alt="Shrine in Snow demo" height="480"> | <strong>Fog Valley Camp</strong><br><img src="./assets/demo/fog-valley-camp.webp" alt="Fog Valley Camp demo" height="480"> |

## Visual structure

1. **Realistic photography** preserves the reference subject, framing, viewpoint, perspective, horizon, palette, and recognizable silhouettes.
2. **Geometric reinterpretation** rebuilds the same scene with clean rectangular and polygonal forms while retaining spatial relationships and hierarchy.
3. **Editorial typography** presents a title, subtitle, and year in a restrained architecture, travel, or city-culture magazine layout.

## Features

- Works with city, architecture, landscape, and travel photography.
- Supports Chinese and English titles and subtitles.
- Follows the requested language, or the current conversation language when none is specified.
- Uses 4–10 Chinese characters or 2–5 English words for generated titles.
- Does not intentionally add extra copy, logos, watermarks, or unrelated objects.
- Produces the finished image with an image editing/generation tool instead of returning only a prompt.

## Usage

```text
Use the `michengai-photo-geometry-poster` skill to turn my uploaded photo into a premium editorial poster.
```

With specified copy:

```text
Use the `michengai-photo-geometry-poster` skill on this photo.
Render the title "MOUNTAINS IN MIST", the subtitle "Sandstone pillars rise through drifting mist above the forest.", and the year "2026".
```

## Files

- [`SKILL.md`](./SKILL.md): workflow, visual constraints, and copy rules.
- [`references/prompt-template.md`](./references/prompt-template.md): adaptive image-generation template.
- [`agents/openai.yaml`](./agents/openai.yaml): optional OpenAI/Codex integration metadata and default prompt; the core skill works independently.
- [`assets/demo/`](./assets/demo/): generated output demos.
