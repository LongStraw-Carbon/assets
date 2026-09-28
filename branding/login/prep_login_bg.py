"""Prepare the login background files.

- login-bg.jpg: the wide photo (used live), copied as-is
- login-bg-alt.jpg: centre-cropped 16:9 from the tall Pexels photo,
  resized to 1920 wide, so there is a second option to switch to
"""
import os

from PIL import Image

REPO = "/tmp/assets-repo"
OUT = "/opt/data/tmp/lsbrand"

wide = os.path.join(REPO, "WhatsApp Image 2026-09-27 at 20.03.47.jpeg")
tall = os.path.join(REPO, "pexels-fi-u-59232535-32576972.jpg")

# chosen background: wide photo, no processing
im = Image.open(wide).convert("RGB")
im.save(os.path.join(OUT, "login-bg.jpg"), quality=88, optimize=True)
print("login-bg.jpg", im.size, os.path.getsize(os.path.join(OUT, "login-bg.jpg")), "bytes")

# alternative: centre crop of the tall photo to 16:9, 1920 wide
im2 = Image.open(tall).convert("RGB")
w, h = im2.size
target_ratio = 16 / 9
crop_h = int(w / target_ratio)
if crop_h > h:
    crop_w = int(h * target_ratio)
    left = (w - crop_w) // 2
    box = (left, 0, left + crop_w, h)
else:
    top = (h - crop_h) // 2
    box = (0, top, w, top + crop_h)
alt = im2.crop(box)
alt = alt.resize((1920, int(1920 * alt.height / alt.width)), Image.LANCZOS)
alt.save(os.path.join(OUT, "login-bg-alt.jpg"), quality=84, optimize=True)
print("login-bg-alt.jpg", alt.size, os.path.getsize(os.path.join(OUT, "login-bg-alt.jpg")), "bytes")
