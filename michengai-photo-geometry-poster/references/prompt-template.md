# Editorial Photo Poster Prompt Template

生成前先根据参考照片填写方括号变量。删除所有方括号说明，不要把变量提示渲染进画面。

```text
Recreate the uploaded reference image as a premium editorial poster while faithfully preserving its overall composition, framing, camera perspective, dominant colors, lighting direction, recognizable subjects, and visual hierarchy.

Create a tall portrait-format poster on a warm ivory/off-white background with generous, carefully balanced margins. Divide the main visual into two aligned sections that depict the same scene from the same viewpoint.

UPPER SECTION — REALISTIC EDITORIAL PHOTOGRAPHY
Reconstruct the reference as a highly realistic [time of day / lighting] photograph of [scene summary]. Preserve these visual anchors: [anchor 1], [anchor 2], [anchor 3], [anchor 4], [anchor 5]. Keep [main subject] in [position], retain the original horizon and vanishing point, and preserve the recognizable silhouettes of [distinctive objects]. Use realistic materials, natural shadows, detailed environmental textures, subtle atmospheric depth, cinematic but restrained color grading, and fine film grain. The result should feel photographed rather than illustrated, with no fantasy additions and no unrelated objects.

LOWER SECTION — GEOMETRIC REINTERPRETATION
Directly below, recreate exactly the same scene, composition, perspective, and visual hierarchy as an elegant geometric block illustration. Translate [subjects and environmental elements] into large clean rectangular and polygonal forms while preserving their positions, scale relationships, movement, and recognizable silhouettes. Use crisp edges, layered blocks, and subtle tonal variation. The style must feel intentionally designed for a contemporary art book, not like crude low-resolution pixel art. Use a sophisticated muted palette derived from the reference, favoring forest green, olive, teal, dusty blue, cream, ochre, terracotta, warm orange, muted pink, and pale sky blue where appropriate.

TYPOGRAPHY SECTION
At the bottom, create a refined editorial typography area using a clean modern sans-serif in dark navy/charcoal. Render exactly these three text elements and no other text:
- Large title on the left: "[TITLE]"
- Subtitle on the right: "[SUBTITLE]"
- Year below the title on the left: "[YEAR]"
Use careful spacing, alignment, and a clear typographic hierarchy. Do not repeat, paraphrase, abbreviate, or misspell any text.

The final image must have a premium architecture, travel, or culture magazine aesthetic; a cohesive relationship between the realistic photograph and its geometric reinterpretation; polished high-resolution detail; and a balanced portrait-poster composition. Do not add extra text, logos, watermarks, borders, captions, signatures, or unrelated objects.
```

## 文案语言

标题和副标题同时支持中文与英文：

- 用户指定语言时严格遵循。
- 未指定语言时跟随当前对话语言；中文请求默认生成中文文案。
- 中文标题：4–10 个汉字；英文标题：2–5 个单词。采用“核心场景 + 氛围或状态”的编辑标题逻辑。
- 副标题：一句与标题同语言的自然短句，具体描述主体、空间关系、运动或光线。
- 年份：当前年份，继续使用阿拉伯数字。

中文排版使用清晰的现代中文无衬线字体，并要求逐字准确渲染。不要在中文请求中默认套用 `CITY IN MOTION` 等英文文案。
