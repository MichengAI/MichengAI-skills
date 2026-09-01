# MichengAI Photo Isometric Impasto Atlas

[中文](./README.md) · **English** · [Back to repository](../README.en.md)

Turn every reference photo into a separate `3:4` portrait scene-atlas poster. The upper half preserves a credible editorial photograph; the lower half reconstructs the same subject and environment in an isometric or axonometric miniature space resting on an irregular, palette-knife impasto terrain derived from the source colors. The horizontal split is strictly 50/50, and multiple photos are never combined.

## Inputs

| Input | Required | Behavior |
| --- | --- | --- |
| `reference_image` | Yes | Processed independently and treated as the only visual source of truth for its poster. |
| `size` | No | Defaults to a `3:4` portrait canvas; other ratios retain equal upper and lower regions. |
| `title` | No | May use a verified place, the subject, or a narrative name; uncertain places are never invented. |
| `caption` | No | One concrete line, or omitted. |
| `number` | No | Optional atlas numbering such as `01` or `001`. |

## Visual language

- The photographic region preserves structure, camera perspective, natural materials, lighting direction, and the source atmosphere with restrained publication-grade grading.
- The lower region uses an elevated isometric view, consistent parallel relationships, and clear depth layers instead of a flat illustration, isolated icon, or exaggerated wide-angle model.
- Essential relationships among the subject, paths, water, courtyards, vegetation, terrain, or people remain legible while secondary distance is simplified.
- The scene stands on an irregular painted terrain rather than a standard plinth. Source-derived colors form palette-knife spreads, overlaps, breaks, and raised edges.
- Fine miniature construction and physical paint coexist without becoming glossy CG, resin décor, blocks, clay toys, or a generic oil-paint filter.
- Titles, captions, verified locations, and numbers remain restrained within the paper space of the lower half.
- Multiple inputs are edited and presented one by one.

## Usage

```text
Use `michengai-photo-isometric-impasto-atlas` to process each uploaded photo as a separate 3:4 isometric impasto scene-atlas poster.
```

```text
Use `michengai-photo-isometric-impasto-atlas` on this architecture photo. Preserve the spatial relationship between the courtyard and water; title: Waterside Echo; number: 01.
```

## Files

- [`SKILL.md`](./SKILL.md): input boundaries, equal split, axonometric reconstruction, paint terrain, typography, and acceptance criteria.
- [`references/prompt-template.md`](./references/prompt-template.md): Chinese prompt template completed for one source photo at a time.
- [`agents/openai.yaml`](./agents/openai.yaml): OpenAI/Codex interface metadata and default prompt.
