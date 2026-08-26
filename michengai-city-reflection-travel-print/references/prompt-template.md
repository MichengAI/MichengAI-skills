# City Reflection Travel Print Prompt Template

每次只处理一个城市。将全部方括号变量替换为实际内容；不要把本模板的说明文字渲染到成品中。生成阶段预留安全构图区，之后使用 `scripts/fit_canvas.py` 输出精确目标尺寸。

```text
Use case: stylized-concept
Asset type: collectible contemporary city travel art print
Primary request: create one premium [REQUESTED RATIO] travel artwork for [CITY], [COUNTRY]. Compose all essential details inside the central 84% of the canvas: reserve at least 8% crop-safe space on every edge because the image will be non-semantically cropped to the exact requested final size after generation.

CITY PROFILE
- Geographic setting: [AUTHENTIC GEOGRAPHIC SETTING]
- Cultural anchor and spatial relationship: [ONE AUTHENTIC CULTURAL ANCHOR] [TRUE RELATIONSHIP TO RIVER/BRIDGE/SLOPE/STREET/WATERFRONT]
- Urban character and density: [ACCURATE CITY SCALE; e.g. continuous dense high-rise skyline, moderate urban fabric, or low-rise historic town]
- Supporting vegetation or water context: [CITY-SPECIFIC CONTEXT]

Build the composition around this authentic profile. Create one serene, sophisticated, cohesive destination environment rather than a collage of disconnected landmarks. Let the cultural anchor, natural setting, city fabric, and water or reflective surface belong to the same believable view. If the city is high-density, render a continuous, varied-height modern urban band in the appropriate background plane; do not reduce it to isolated low-rise blocks. If the city is not high-density, portray its real scale instead.

Style and materials: sophisticated modern editorial illustration with fine architectural linework, tactile paper grain, restrained watercolor-and-gouache textures, and polished contemporary digital illustration. Use a harmonious, slightly desaturated palette of warm ivory, soft beige, muted earth tones, gentle local architectural colors, and subtle environmental blues or greens. Add diffused natural light, delicate shadows, generous negative space, and a few extremely subtle translucent geometric forms only at the outer border area.

Reflection: place the complete landscape above a calm glass-like reflective surface. Render delicate vertical reflections of the principal architecture, terrain, and major elements. Keep reflections soft, atmospheric, and slightly faded.

Text (render exactly these three top-aligned text elements and no other readable text anywhere in the image):
"[CITY]"
"[SLOGAN]"
"No. 05 — [YEAR]"
Use refined small magazine typography with wide letter spacing, minimal weight, and precise alignment. Render the supplied city name and slogan character-for-character in their intended language. Do not render lettering, plaques, store signs, logos, labels, or watermarks on buildings, streets, boats, or backgrounds.

Constraints: make [CITY] unmistakable through the authentic profile; do not force elements that do not belong. Preserve one cohesive landscape instead of a landmark collage. Keep every essential element inside the crop-safe area and respect the requested [REQUESTED RATIO].

Avoid: anime aesthetics, photorealistic collages, generic stock imagery, oversized landmarks, excessive cultural symbols, clutter, excessive decoration, oversized typography, logos, watermarks, brand marks, map graphics, flags, borders, unrelated text, invented signage, and overly saturated tourist-poster colors.
```

## 完成后尺寸交付

生成完成后运行：

```bash
python scripts/fit_canvas.py generated.png final.png --size 768x1024
```

若用户指定明确像素，替换 `--size`；脚本以居中、非语义裁切和高质量缩放交付精确尺寸。

## 示例

```text
size: 3:4
city: 香港
country: 中国
slogan: 一城烟火，两岸风华
```
