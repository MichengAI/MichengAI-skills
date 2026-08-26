# MichengAI City Reflection Travel Print

[中文](./README.md) · **English** · [Back to repository](../README.en.md)

Creates a collectible contemporary travel art print for a city. Genuine landscape, architecture, and local culture form one coherent environment above gentle mirror-like reflections, with restrained magazine typography.

## Inputs

| Parameter | Required | Behavior |
| --- | --- | --- |
| `city` | Yes | The city is the visual core and top title. The skill asks when it is missing. |
| `size` | No | Supports an aspect ratio or pixel dimensions; defaults to a `3:4` request. When the tool supports pixels, it requests `768×1024`. |
| `country` | No | Inferred from the city when reliable; the skill asks if the city is ambiguous. |
| `slogan` | No | Generated from authentic city character when absent; rendered verbatim when supplied. |

## Visual character

- Builds one continuous environment from authentic terrain, waterfront, neighborhood, and architectural language instead of a landmark collage.
- Uses sophisticated desaturated color, watercolor-and-gouache paper texture, fine architectural linework, and controlled contemporary illustration.
- Places the scene above a calm glass-like surface with soft, gently faded vertical reflections.
- Uses extremely subtle translucent geometric borders for a contemporary gallery-art atmosphere.
- Renders only a small city name, slogan, and `No. 05 — year` at the top; no unrequested readable text appears in the built environment.
- Requests the target ratio or pixels directly from the image-generation tool; it does not depend on Python, scripts, cropping, padding, or resizing to change the composition afterwards.

## Usage

```text
Use $michengai-city-reflection-travel-print to create a city travel art print.
City: Hong Kong
Country: China
Size: 3:4
Slogan: A city of lights, framed by two shores
```

With only the required input:

```text
Use $michengai-city-reflection-travel-print to create a city travel art print.
City: Lisbon
```

## Demos

The tested examples are compressed to **720 × 960 WebP** and displayed in two 320px columns to balance loading, layout rhythm, and typographic legibility.

| Beijing · Ancient and Contemporary | Shanghai · Rivers and Radiance |
| --- | --- |
| <img src="./assets/demo/beijing.webp" alt="Beijing city reflection travel print demo" width="320"> | <img src="./assets/demo/shanghai.webp" alt="Shanghai city reflection travel print demo" width="320"> |
| Guangzhou · Lingnan Tides | Shenzhen · A Young Future |
| <img src="./assets/demo/guangzhou.webp" alt="Guangzhou city reflection travel print demo" width="320"> | <img src="./assets/demo/shenzhen.webp" alt="Shenzhen city reflection travel print demo" width="320"> |
| Guiyang · Green Mountain Air | Macau · Old Bay, Shared Horizons |
| <img src="./assets/demo/guiyang.webp" alt="Guiyang city reflection travel print demo" width="320"> | <img src="./assets/demo/macau.webp" alt="Macau city reflection travel print demo" width="320"> |

## Files

- [`SKILL.md`](./SKILL.md): parameter rules, city selection logic, and visual constraints.
- [`references/prompt-template.md`](./references/prompt-template.md): city-specific image-generation prompt template.
- [`agents/openai.yaml`](./agents/openai.yaml): Codex display metadata and default invocation.
