# MichengAI Rubber Stamp Field Notes

[中文](./README.md) · **English** · [Back to repository](../README.en.md)

Turns each travel photo into a separate, quiet, collectible 4:3 field-note poster. The authentic photograph remains on the left, while an aged-paper area on the right contains generous whitespace, a small handmade multi-color rubber stamp, and minimal English archival text.

## Core rules

- Generate one independent result per photo. Never create a collage, combined-location design, or contact sheet.
- The photograph occupies roughly 58% of the frame and preserves the original subject, perspective, light, texture, and atmosphere.
- The aged-paper area occupies roughly 42% and uses subtle paper fibers, faint handling marks, and large unprinted areas.
- The rubber stamp sits in the lower-middle paper area and occupies roughly 30–38% of the right section's height.
- The stamp keeps only a few location-defining silhouettes and uses 2–4 muted spot colors sampled from the photograph.
- The impression retains believable uneven pressure, broken contours, dry ink, grain, and slight color-layer misregistration without looking digitally distressed.

## Archival text

The right side contains only:

- the correct English location name;
- a number;
- exactly three short English keywords;
- the Gregorian calendar year.

When the location cannot be identified reliably, the skill asks the user instead of guessing.

## Usage

```text
Use $michengai-rubber-stamp-field-notes to process each uploaded travel photo separately.
Use the correct English location name, start numbering at 01, use the year 2026, and never create a collage.
```

## Files

- [`SKILL.md`](./SKILL.md): per-photo workflow, layout ratios, and rubber-stamp constraints.
- [`references/prompt-template.md`](./references/prompt-template.md): adaptive image-generation template.
- [`agents/openai.yaml`](./agents/openai.yaml): Codex display metadata and default invocation.

> This style does not have a demo image yet. Future tested outputs can be stored under `assets/demo/` in this child skill.
