"""Produce the branded theme.json from the live OpenCloud theme.

Reads theme-live.json, rewrites the product name and the logo/favicon
references to files we serve ourselves under /brand/, writes theme.json.
"""
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "theme-live.json")
DST = os.path.join(HERE, "theme.json")

PRODUCT_NAME = "Longstraw Carbon Files"
LOGO = "/brand/longstraw-carbon-logo.png"
LOGO_WHITE = "/brand/longstraw-carbon-logo-white.png"
FAVICON = "/brand/favicon.svg"


def main() -> None:
    d = json.load(open(SRC))

    common = d["common"]
    print("was name:", common.get("name"), "| slogan:", common.get("slogan"))
    common["name"] = PRODUCT_NAME
    common["logo"] = LOGO

    web = d["clients"]["web"]
    web["defaults"]["favicon"] = FAVICON
    web["defaults"]["logo"] = LOGO
    web["defaults"]["logoMobile"] = LOGO
    for theme in web.get("themes", []):
        if theme.get("isDark"):
            theme["logo"] = LOGO_WHITE
            theme["logoMobile"] = LOGO_WHITE
        elif "logo" in theme:
            theme["logo"] = LOGO

    with open(DST, "w") as fh:
        json.dump(d, fh, indent=2, ensure_ascii=False)
        fh.write("\n")

    check = json.load(open(DST))
    print("new name:", check["common"]["name"])
    print("new defaults:", check["clients"]["web"]["defaults"])
    print("dark logo:", [t.get("logo") for t in check["clients"]["web"]["themes"] if t.get("isDark")])
    print("wrote", DST, os.path.getsize(DST), "bytes")


if __name__ == "__main__":
    main()
