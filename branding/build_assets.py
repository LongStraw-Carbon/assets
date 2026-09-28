"""Build Longstraw Carbon branding assets from the source logo.

Reads logo-no-background.png, writes:
  longstraw-carbon-logo.png       clean copy of the source logo
  longstraw-carbon-logo-white.png white silhouette for the dark theme
  ls-favicon-{512,256,128,64,32}.png  square padded favicon bitmaps
  favicon.svg                     SVG wrapper embedding the 128px bitmap
"""
import base64
import os

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
# Default source is the repo logo; override with LOGO_SRC (e.g. the vector
# PDF rendered at 300dpi) to rebuild from a higher resolution original.
SRC = os.environ.get("LOGO_SRC") or os.path.join(HERE, "logo-no-background.png")


def main() -> None:
    im = Image.open(SRC).convert("RGBA")
    w, h = im.size
    print("source logo:", im.size, "mode RGBA")

    im.save(os.path.join(HERE, "longstraw-carbon-logo.png"))

    r, g, b, a = im.split()
    white = Image.merge(
        "RGBA",
        (a.point(lambda v: 255), a.point(lambda v: 255), a.point(lambda v: 255), a),
    )
    white.save(os.path.join(HERE, "longstraw-carbon-logo-white.png"))
    print("white silhouette written")

    pad = int(0.08 * max(w, h))
    side = max(w, h) + 2 * pad
    canvas = Image.new("RGBA", (side, side), (0, 0, 0, 0))
    canvas.paste(im, ((side - w) // 2, (side - h) // 2), im)
    for px in (512, 256, 128, 64, 32):
        path = os.path.join(HERE, f"ls-favicon-{px}.png")
        canvas.resize((px, px), Image.LANCZOS).save(path)

    with open(os.path.join(HERE, "ls-favicon-128.png"), "rb") as fh:
        b64 = base64.b64encode(fh.read()).decode()
    svg = (
        '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" '
        'width="128" height="128">'
        '<image width="128" height="128" href="data:image/png;base64,'
        + b64
        + '"/></svg>\n'
    )
    with open(os.path.join(HERE, "favicon.svg"), "w") as fh:
        fh.write(svg)
    print("favicon.svg bytes:", len(svg))

    for name in sorted(os.listdir(HERE)):
        print(" ", name, os.path.getsize(os.path.join(HERE, name)))


if __name__ == "__main__":
    main()
