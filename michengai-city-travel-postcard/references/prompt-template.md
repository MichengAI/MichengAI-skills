# City Travel Postcard Prompt Template

每次只处理一个城市。将所有方括号变量替换为事实内容；不要把说明或方括号渲染进图像。直接在图像生成请求中传入目标比例或像素尺寸，生成后不裁切、不补边、不缩放。

```text
Create one premium illustrated travel postcard for [CITY DISPLAY], [COUNTRY OR REGION], at [REQUESTED SIZE OR RATIO].

FACTUAL CITY PROFILE
- Local city name: [LOCAL CITY NAME]
- Primary landmark: [GEOGRAPHICALLY ACCURATE PRIMARY LANDMARK]
- Landmark setting and spatial relationship: [AUTHENTIC WATERFRONT / STREET / HILL / PARK / DISTRICT RELATIONSHIP]
- Local architecture and materials: [AUTHENTIC ARCHITECTURAL CHARACTER]
- Geography, vegetation, transport, and secondary details: [ONLY FACTUALLY ASSOCIATED DETAILS]

Build one coherent, geographically believable view around the landmark. Use a cinematic elevated viewpoint with natural 40–50mm-equivalent perspective and clear foreground, middle-ground, and background separation. Keep the upper portion spacious for typography. Surround the landmark only with authentic local buildings, streets, waterfronts, hills, parks, trees, transport, or other elements that genuinely belong to [CITY DISPLAY]. Do not create a landmark collage, generic skyline, invented architecture, or geographically impossible scenery.

Visual identity: a refined Japanese tourism-magazine editorial illustration, using handcrafted layered paper collage combined with delicate gouache and watercolor textures. Use tactile matte art paper, fine paper grain, subtle handmade cut edges, soft physical paper shadows, gentle atmospheric depth, and premium offset-print character. Do not imitate a particular living artist, brand, or publication.

Palette: soft powder blue, warm ivory, cream, muted sage, dusty green, pale beige, soft gray, and restrained terracotta. Use low-to-medium saturation, gentle tonal transitions, soft natural daytime light, slight haze, delicate layered shadows, peaceful nostalgia, and no harsh contrast.

Architecture and life: render precise, believable local architecture with simplified but accurate proportions, materials, facades, and rooflines. Add only a few tiny simplified paper-cut travelers or pedestrians walking, sightseeing, sitting, or looking toward the landmark. Use regionally appropriate foliage and add water, mountains, coastline, rivers, or transport only when genuinely associated with this city.

Render exactly these three top-left text elements, integrated into the paper composition, with no other readable text anywhere:
"[CITY DISPLAY]"
"[LOCAL CITY NAME] · [COUNTRY OR REGION]"
"[PRIMARY LANDMARK DISPLAY]"
Use a large uppercase geometric sans-serif for the city display; a small refined sans-serif for the local name and country/region; and small widely spaced uppercase lettering for the landmark. Keep typography elegant, minimal, and accurately spelled.

Avoid photorealistic photography, CGI, plastic rendering, flat vector art, anime, cartoon caricature, generic skyline, inaccurate landmark, fictional architecture, impossible geography, duplicated buildings, excessive or oversized people, neon colors, oversaturation, harsh black shadows, glossy surfaces, clutter, excessive outlines, random text, misspelled typography, watermarks, logos, borders, frames, UI elements, maps, and flags.
```

## 调用示例

```text
城市：上海
尺寸：3:4
```

若图像工具支持像素尺寸，也可提供：

```text
城市：上海
尺寸：768×1024
```
