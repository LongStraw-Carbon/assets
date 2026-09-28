"""Finalise the branding assets after switching to the vector PDF source.

- keeps a high resolution original for print use
- writes a web sized logo (1200px wide) so the UI does not load a 360KB PNG
- rebuilds the white silhouette at the same web size
"""
import os

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
HIRES_SRC = os.path.join(HERE, "pdf_page0_render.png")
HIRES = os.path.join(HERE, "longstraw-carbon-logo-hires.png")
WEB = os.path.join(HERE, "longstraw-carbon-logo.png")
WEB_WHITE = os.path.join(HERE, "longstraw-carbon-logo-white.png")

WEB_WIDTH = 1200


def main() -> None:
    hires = Image.open(HIRES_SRC).convert("RGBA")
    hires.save(HIRES, optimize=True)
    print("hires:", hires.size, os.path.getsize(HIRES), "bytes")

    w = WEB_WIDTH
    h = round(hires.height * w / hires.width)
    web = hires.resize((w, h), Image.LANCZOS)
    web.save(WEB, optimize=True)
    print("web logo:", web.size, os.path.getsize(WEB), "bytes")

    a = web.split()[-1]
    white = Image.merge("RGBA", tuple(a.point(lambda v: 255) for _ in range(3)) + (a,))
    white.save(WEB_WHITE, optimize=True)
    print("white:", white.size, os.path.getsize(WEB_WHITE), "bytes")


if __name__ == "__main__":
    main()
