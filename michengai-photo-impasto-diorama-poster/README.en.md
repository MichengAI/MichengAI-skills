# MichengAI Photo Impasto Diorama Poster

[中文](./README.md) · **English** · [Back to repository](../README.en.md)

Turns each reference photograph into a separate `3:4` portrait poster: authentic editorial photography above and a tactile impasto-oil miniature scene on bright textured paper below. The two sections are split exactly at the horizontal center, and multiple source photos are never combined.

## Inputs

| Parameter | Required | Behavior |
| --- | --- | --- |
| `reference_image` | Yes | Each photo is processed independently and is the sole visual source for its poster. |
| `size` | No | Defaults to portrait `3:4`; other ratios still retain an exact 50/50 vertical split. |
| `title` | No | When omitted, a short title is derived from a verified subject, place, mood, or symbol. |
| `subtitle` | No | Optional single line of microcopy. |
| `number` | No | Defaults to `01`, `02`, and so on in input order. |

## Characteristics

- Preserves subject identity, proportions, posture, perspective, real materials, natural light, and the source color atmosphere in the upper photograph, with restrained art-publication grading only.
- Reinterprets the subject silhouette and narrative relationship below as a 3D impasto miniature organized around a centered or slightly offset diagonal axis—not as a literal redraw.
- Supports the subject with a source-derived painted ribbon and only a few relevant reflections, ripples, light marks, shadows, clouds, or mist, leaving most of the warm-white paper open.
- Rebuilds the palette from the clearest, brightest, most lively source colors instead of averaging the whole image into muted gray.
- Keeps visible paint buildup, palette-knife marks, raised edges, and paper fibers while avoiding plastic CG, resin toys, cartoons, and commercial product-render styling.
- Processes and presents multiple photos one at a time, without collages, contact sheets, or cross-photo element borrowing.

## Usage

```text
Use `michengai-photo-impasto-diorama-poster` to process each uploaded photo as a separate 3:4 poster.
```

```text
Use `michengai-photo-impasto-diorama-poster` on this photo.
Title: Stained Moments
Number: 01
```

## Demos

| <strong>Above the snowline</strong><br><img src="./assets/demo/snowline-hiker.png" alt="Snow-peak hiker impasto diorama poster demo" width="320"> | <strong>Storm lakeshore</strong><br><img src="./assets/demo/storm-lakeshore.png" alt="Storm lake impasto diorama poster demo" width="320"> |
| :--- | :--- |
| <strong>Rust-colour pause</strong><br><img src="./assets/demo/rusted-car.png" alt="Rusted car impasto diorama poster demo" width="320"> | <strong>Watermelon by the window</strong><br><img src="./assets/demo/window-watermelon.png" alt="Window watermelon impasto diorama poster demo" width="320"> |
| <strong>Colours of wind</strong><br><img src="./assets/demo/wind-colors.png" alt="Colourful fabric flags impasto diorama poster demo" width="320"> | <strong>White line in mist</strong><br><img src="./assets/demo/mist-white-line.png" alt="Rainforest waterfall impasto diorama poster demo" width="320"> |

## Files

- [`SKILL.md`](./SKILL.md): input rules, composition, style boundaries, typography, and validation criteria.
- [`references/prompt-template.md`](./references/prompt-template.md): the Chinese image-editing prompt template filled separately for each source photo.
- [`agents/openai.yaml`](./agents/openai.yaml): optional OpenAI/Codex display metadata and default prompt.
- [`assets/demo/`](./assets/demo/): six impasto-diorama poster examples generated from reference photographs.
