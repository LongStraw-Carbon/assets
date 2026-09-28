# Longstraw Carbon brand assets

Source of truth for the Longstraw Carbon logo and favicons. Anything that
needs the brand - the OpenCloud instance at `assets.longstraw.earth`, docs,
decks, web pages - takes its files from this folder.

## Files

| File | What it is |
|---|---|
| `logo-no-background.png` | Original logo, 1500x541, transparent background |
| `longstraw-carbon-logo.png` | Same logo, clean name, for general use |
| `longstraw-carbon-logo-white.png` | White silhouette of the mark, for dark backgrounds |
| `favicon.svg` | Favicon in SVG form, embeds the 128px bitmap (use this on websites) |
| `ls-favicon-{512,256,128,64,32}.png` | Square padded favicon bitmaps with transparent margins |
| `theme.json` | OpenCloud theme consumed by `assets.longstraw.earth` |
| `build_assets.py` | Regenerates the favicons and white variant from the source logo |
| `build_theme.py` | Regenerates `theme.json` (name, logo and favicon references) |

Other images in the repository root (`Untitled.jpeg`, the screenshot, the
UUID-named jpeg) are raw uploads kept for reference.

## How the OpenCloud instance uses these

- `theme.json` is served at `/themes/opencloud/theme.json` by an nginx
  override, so the product name reads **Longstraw Carbon Files**.
- Logos and the favicon are served from `/brand/` on the same host.
- The browser tab title (`Longstraw Carbon`) is rewritten by an nginx
  `sub_filter` rule, because the OpenCloud web frontend ships its HTML as
  embedded assets that cannot be overridden from disk.
- Deployment details live in the `work-server` repository runbook.

## Regenerating

```bash
pip install pillow
python3 build_assets.py     # favicons + white variant
python3 build_theme.py      # theme.json (edit the constants at the top first)
```
