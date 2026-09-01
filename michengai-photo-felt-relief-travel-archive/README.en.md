# MichengAI Photo Felt Relief Travel Archive

[中文](./README.md) · **English** · [Back to repository](../README.en.md)

Turns each reference photo into a complete `3:4` portrait material-study archive in one image-editing call. A warm ivory sheet stacks an intact source photograph and a mixed-material relief with the same visible dimensions and aspect ratio, followed by restrained English typewriter notes. Landscape inputs use equal landscape panels, `1:1` inputs use two centered equal square panels, and portrait inputs retain their native portrait ratio.

## Inputs

| Parameter | Required | Behavior |
| --- | --- | --- |
| `reference_image` | Yes | Each photo is processed independently and is the sole visual source for its poster. |
| `size` | No | Defaults to portrait `3:4`, with an approximately 46/54 upper/lower split. |
| `title` | No | Optional English title; otherwise derived from visible scene facts. |
| `scene_subtitle` | No | Optional English scene subtitle; unverified locations are never invented. |
| `description` | No | Optional one- or two-sentence English description; otherwise generated only from visible facts. |
| `study_number` | No | Defaults to `01` for one image and increments in input order for multiple images. |

## Characteristics

- Mounts the full upper photo with proportional scaling—no cropping, stretching, outpainting, recomposition, recoloring, or altered light.
- Selects a landscape, square, or portrait layout from the source ratio; the two panels always keep equal width, equal height, and the same aspect ratio, with all copy below the relief.
- Maps a `1:1` source to two centered equal square panels rather than placing it inside a landscape mat or widening the relief.
- Builds the lower view as one complete rectangular material artwork with a subtle rough edge and unified cast shadow, preserving subject count, placement, scale, orientation, perspective, and depth relationships.
- Uses layered hand-cut felt and needle-felted wool as the primary materials, with only scene-justified bark, cork, reclaimed wood, burlap, paper pulp, plaster, or wire.
- Uses wall-mounted low relief: approximately `5–12 mm` maximum projection and `1–3 mm` stacked felt sheets, with visible needle marks, fibers, seams, lifted edges, and natural imperfections.
- Combines warm ivory fiber paper, muted source-derived colors, and matte materials for a museum-archive specimen-photography character.
- Generates only an English title, a scene line with `STUDY NO.`, one or two concise sentences, and a slash-separated materials line in restrained vintage typewriter typography.
- Explicitly excludes knitting, crochet, plush toys, plastic models, smooth 3D, watercolor, cartoons, interfaces, watermarks, and unrelated text.
- Generates the complete poster in one image-editing call without script, web, or post-production assembly.

## Usage

```text
Use `michengai-photo-felt-relief-travel-archive` to turn each uploaded photo into a separate 3:4 felt-relief travel archive poster.
```

```text
Use `michengai-photo-felt-relief-travel-archive` on this photo. Keep the complete original above, build an equally wide rectangular material relief below, and place the archive copy underneath the relief.
```

## Files

- [`SKILL.md`](./SKILL.md): input handling, dual-zone layout, material mapping, English copy, exclusions, and acceptance checks.
- [`references/prompt-template.md`](./references/prompt-template.md): the Chinese image-editing prompt template filled separately for each source photo.
- [`agents/openai.yaml`](./agents/openai.yaml): OpenAI/Codex display metadata and default prompt.
