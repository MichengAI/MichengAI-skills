# City Reflection Travel Print Prompt Template

每次只处理一个城市。将全部方括号变量替换为实际内容；不要把本模板的说明文字渲染到成品中。直接在图像生成请求中要求目标比例或像素尺寸，不进行任何后期裁切、补边或缩放。

```text
Use case: stylized-concept
Asset type: collectible contemporary city travel art print
Primary request: create one premium [REQUESTED RATIO] travel artwork for [CITY], [COUNTRY]. Generate directly at the requested ratio [AND TARGET PIXEL SIZE IF THE TOOL SUPPORTS IT]. Preserve the full intended composition: do not rely on later cropping, padding, or resizing.

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

Constraints: make [CITY] unmistakable through the authentic profile; do not force elements that do not belong. Preserve one cohesive landscape instead of a landmark collage. Respect the requested [REQUESTED RATIO] directly in the generated image; do not crop, pad, or resize the result after generation.

Avoid: anime aesthetics, photorealistic collages, generic stock imagery, oversized landmarks, excessive cultural symbols, clutter, excessive decoration, oversized typography, logos, watermarks, brand marks, map graphics, flags, borders, unrelated text, invented signage, and overly saturated tourist-poster colors.
```

## 尺寸交付

- 在生成请求中直接传入用户指定比例；未指定时为 `3:4`。
- 工具支持明确像素尺寸时，一并传入目标像素；未支持时不伪造“精确像素”承诺。
- 若首次结果比例不符，做一次针对比例的重新生成；不得用后期裁切、补边或缩放改变构图。

## 示例

```text
size: 3:4
city: 香港
country: 中国
slogan: 一城烟火，两岸风华
```
