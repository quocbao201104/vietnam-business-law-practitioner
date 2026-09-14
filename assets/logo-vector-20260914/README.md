# Vietnam Business Law Practitioner — Vector logo and README banner

Reconstructed from the user-supplied PNG on 2026-09-14. This task wrote only this new kit and its ZIP archive. No plugin, skill, or repository README files were edited by this task.

## Ready-to-use files

| Purpose | Files | Background |
| --- | --- | --- |
| GitHub README banner, 1600 × 440 | `banner/readme-banner-light.svg`, `banner/readme-banner-light.png` | White |
| Dark README banner, 1600 × 440 | `banner/readme-banner-dark.svg`, `banner/readme-banner-dark.png` | Ink blue |
| Standalone symbol | `svg/symbol-color.svg`, `symbol-black.svg`, `symbol-white.svg` in the same folder | Transparent |
| Symbol with name | `svg/lockup-color.svg`, `lockup-black.svg`, `lockup-white.svg` in the same folder | Transparent |
| Symbol PNG exports | `png/symbol-{color,black,white}-{32,64,128,256,512,1024}.png` | Transparent RGBA; 18 files |
| Name lockup PNG exports | `png/lockup-{color,black,white}-1600.png` | Transparent RGBA; 3 files |
| Favicon | `favicon/favicon.ico`, containing 16/32/48 px | Transparent |
| Favicon vector sources | `favicon/favicon-optical-{color,black,white}.svg` | Transparent |
| Sharing/print PDF | `pdf/vietnam-business-law-practitioner-vector.pdf` | Color and black on paper; white on a vector ink-blue field |

The PDF has six pages: color symbol, color lockup, black symbol, black lockup, white symbol, white lockup. It contains paths only, with no raster images or text drawing operators. It is an RGB vector sharing/print file, not a certified PDF/X or spot-color separation.

All distribution SVG files contain true paths. They do not embed a PNG, font, external resource, or data URI. Only the editable source retains text elements.

## Banner decision

The selected left-symbol/right-text arrangement and three-line hierarchy are retained. The canvas is reframed from the 1672 × 941 reference to **1600 × 440** with source-space bounds (49,245)–(1649,685). This removes unused vertical space without stretching the symbol. Top/bottom artwork clear space is approximately 50 px; left/right clear space is approximately 100/117 px.

At a simulated README content width of 830 px, the banner is approximately 228 px high. The preview is a local size simulation, not a screenshot of the live GitHub page.

## Geometry and optical adjustments

`source/master.json` is the single geometry/layout/color source. The mark has three closed paths: the V, upper bar, and lower bar. The standalone and name-lockup exports use identical path coordinates; only their viewBox differs.

- The V's rounded terminals and bottom corners are reconstructed with cubic Bézier curves.
- The inner notch, asymmetry of the arms, two horizontal bars, and rounded bar ends follow the PNG.
- Raster edge noise and texture are removed; fills are flat.
- The standard master keeps the approximately 13 px vertical gap between the horizontal bars in source coordinates.
- The color is **#0F4352**, derived from the median sampled ink pixels in the supplied image. Black and white variants change only fill.
- Threshold-mask overlap (IoU) with the symbol reference is **0.986715** at 512 × 512. Reference mask: R < 80 and G < 130; vector mask: alpha > 127. This describes silhouette overlap, not a brand-recognition or design-quality score.
- `qa/symbol-overlay.png` shows the intersection in ink blue, reference-only pixels in pink, and vector-only pixels in cyan.
- `qa/reference-comparison.png` compares the source PNG and reconstruction side by side.

## Font provenance

The actual font used inside the AI-generated reference cannot be identified conclusively from the PNG. This reconstruction uses **Inter** as an explicitly documented replacement, not as a claimed exact original.

- Official upstream: https://github.com/rsms/inter
- Distribution source: https://github.com/google/fonts/tree/main/ofl/inter
- Included unmodified variable font: `source/Inter-opsz-wght.ttf`.
- Version: **4.001; git-66647c0bb**.
- Font SHA-256: `29160a80ff49ddcab2c97711247e08b1fab27a484a329ce8b813d820dc559031`.
- License: **SIL Open Font License 1.1**; full copyright and license in `source/OFL.txt`.
- Copyright statement in the included license: Copyright 2020 The Inter Project Authors.

“Vietnam” and “Practitioner” use weight 400; “Business Law” uses weight 900. Optical-size axis is 32. HarfBuzz applies kerning; the script converts each line to glyph paths and then fits its ink bounds to the reference:

| Line | Reference ink bounds | Horizontal scale | Vertical scale |
| --- | --- | --- | --- |
| Vietnam | (634,306)–(1063,392) | 107.6606% | 100.0227% |
| Business Law | (637,408)–(1532,522) | 96.1141% | 104.0419% |
| Practitioner | (638,540)–(1237,627) | 110.6961% | 101.1858% |

These per-line adjustments retain the selected layout and visual hierarchy. They produce a customized wordmark based on Inter; the result is not an untouched font specimen or a claim of identical glyph shapes.

Distribution SVG and PDF lettering is outlined. `source/lockup-editable.svg` retains editable text and the same optical matrices. Load the included font in your editor if editing that file. The font itself has not been modified.

## Favicon treatment and small sizes

The normal 16 px reduction compresses the bar-to-bar gap below half a pixel. The favicon therefore uses a separate 16-unit master that retains the V and both bars, slightly simplifies the terminals, and increases the bar-to-bar gap to 1.2 units. Its upper bar occupies y=4–5.3 and lower bar y=6.5–7.8.

The favicon is not substituted into normal symbol SVG or 32–1024 px PNG exports. All three ICO frames are rendered from the optical favicon SVG, and each decoded frame was compared pixel-for-pixel against its corresponding render.

At 16 px, the V remains the strongest cue; the bars are less distinct than at larger sizes. Prefer the normal symbol at 32 px or above and 64 px or above where the two interior bars should read comfortably. See `qa/small-size-check.png`.

## Verification

- Rendered all SVG distribution files using resvg without system fonts.
- Checked that all distribution SVG files contain no text/image elements or data URI.
- Compared path/transform signatures and alpha channels across color/black/white: identical within each asset family.
- Verified all 18 symbol PNG sizes, RGBA mode, transparent and opaque alpha values, and fully transparent corner pixels.
- Verified that banners are opaque and transparent assets have actual alpha transparency.
- Decoded the ICO and verified its exact frame sizes and pixels.
- Verified all six PDF pages contain no raster image or font-dependent text drawing operators.
- Rendered all PDF pages through Poppler and visually checked the contact sheet.
- Rendered editable SVG with the bundled font and compared it against outlined SVG; mask overlap is recorded in `qa/verification.json`.
- Verified that the user-supplied PNG and its reference copy match byte-for-byte. The four initially observed files under `assets/brand/concepts/` were absent at the final check; no command in this task deleted or moved them. Their original hashes and final status are retained, rather than claiming they remain unchanged. This external-state check is reported separately from export validation.
- Ran the builder's help and export/verification path.

## Editing and rebuilding

Keep `source/master.json` as the source of truth. `source/rebuild.py` reconstructs exports from this file and the bundled font. Dependencies are listed at the top of the script; `--deps` supports an isolated Python dependency directory. Use `python -B` to avoid cache artifacts.

The PNG in `source/reference.png` is for visual comparison only. It is not embedded into any vector deliverable.

A theme-aware README insertion is provided in `readme-snippet.md`. The root repository README has been left unchanged.
