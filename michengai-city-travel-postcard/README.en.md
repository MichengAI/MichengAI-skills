# MichengAI City Travel Postcard

[中文](./README.md) · **English** · [Back to repository](../README.en.md)

Creates a premium illustrated travel postcard for a specified city. One geographically accurate landmark anchors a coherent local environment, rendered as a refined Japanese tourism-magazine collage with gouache, watercolor, tactile paper, and restrained multilingual editorial typography.

## Inputs

| Parameter | Required | Behavior |
| --- | --- | --- |
| `city` | Yes | Determines the landmark, local name, country/region, environment, and artwork text. The skill asks when facts are ambiguous. |
| `size` | No | Accepts a ratio or pixels supported by the image tool; defaults to a `3:4` request. |
| `country_or_region` | No | Inferred only when reliable; the skill asks when ambiguous. |
| `language` | No | Controls explanatory language; the in-image local name always uses the city’s locally used script. |

## Characteristics

- Builds a factual city profile and selects one geographically accurate focal landmark.
- Keeps architecture, streets, geography, transport, tiny figures, and nature in one believable viewpoint—never a landmark collage.
- Uses a quiet Japanese travel-editorial identity: layered paper collage, gouache, watercolor, matte stock, and subtle handmade cut edges.
- Renders only three text lines: city, local city name plus country/region, and primary landmark.
- Is prompt-only: it requests the ratio or pixels directly and does not depend on Python, scripts, cropping, padding, or resizing after generation.

## Usage

```text
Use $michengai-city-travel-postcard to create an illustrated travel postcard.
City: Shanghai
Size: 3:4
```

```text
Use $michengai-city-travel-postcard to create an illustrated travel postcard.
City: Shenzhen
Size: 1080×1350
```

## Demos

| <strong>Beijing · Temple of Heaven</strong><br><img src="./assets/demo/beijing-temple-of-heaven.webp" alt="Beijing Temple of Heaven travel postcard demo" width="320"> | <strong>Shanghai · Oriental Pearl Tower</strong><br><img src="./assets/demo/shanghai-oriental-pearl.webp" alt="Shanghai Oriental Pearl travel postcard demo" width="320"> |
| :--- | :--- |
| <strong>Shenzhen · Ping An Finance Center</strong><br><img src="./assets/demo/shenzhen-ping-an.webp" alt="Shenzhen Ping An Finance Center travel postcard demo" width="320"> | <strong>Guangzhou · Canton Tower</strong><br><img src="./assets/demo/guangzhou-canton-tower.webp" alt="Guangzhou Canton Tower travel postcard demo" width="320"> |

## Files

- [`SKILL.md`](./SKILL.md): parameters, city-fact rules, visual constraints, and validation criteria.
- [`references/prompt-template.md`](./references/prompt-template.md): city-specific generation prompt template.
- [`agents/openai.yaml`](./agents/openai.yaml): Codex display metadata and default invocation.
