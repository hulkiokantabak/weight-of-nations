# -*- coding: utf-8 -*-
"""win_fonts.py - Windows-only helper for a faithful PDF body font.

The @fontsource per-weight IBM Plex Sans woff2 name each weight as a separate family
("IBM Plex Sans" / "IBM Plex Sans Medium" / "IBM Plex Sans SemiBold"), which the MSYS2
Pango/fontconfig stack mishandles when WeasyPrint loads them via @font-face - the body
text falls back to a system font. This rebuilds them as ONE family ("IBM Plex Sans",
weights 400/500/600 via the OS/2 table) and drops them into a fontconfig-scanned dir, so
the `'IBM Plex Sans'` fallback in build_pdf.py's CSS resolves to the real font.

Run once on Windows before build_pdf.py:  python win_fonts.py
Not needed on Linux/CI, where the woff2 @font-face load directly. Override the destination
with WON_WIN_FONTS_DIR (default: the MSYS2 mingw64 fonts dir).
"""
import io, os, glob
from fontTools.ttLib import TTFont

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "fonts", "@fontsource", "ibm-plex-sans", "files")
DST = os.environ.get("WON_WIN_FONTS_DIR", r"C:\msys64\mingw64\share\fonts\won")


def build():
    os.makedirs(DST, exist_ok=True)
    for f in glob.glob(os.path.join(DST, "IBMPlexSans-*.ttf")):
        os.remove(f)
    for w in (400, 500, 600):
        font = TTFont(os.path.join(SRC, f"ibm-plex-sans-latin-{w}-normal.woff2"))
        nm = font["name"]
        for rec in list(nm.names):
            if rec.nameID in (1, 4, 16):
                nm.setName("IBM Plex Sans", rec.nameID, rec.platformID, rec.platEncID, rec.langID)
            elif rec.nameID in (2, 17):
                nm.setName("Regular", rec.nameID, rec.platformID, rec.platEncID, rec.langID)
            elif rec.nameID == 6:
                nm.setName(f"IBMPlexSans-{w}", rec.nameID, rec.platformID, rec.platEncID, rec.langID)
        font["OS/2"].usWeightClass = w
        font.flavor = None
        font.save(os.path.join(DST, f"IBMPlexSans-{w}.ttf"))
        print("wrote", os.path.join(DST, f"IBMPlexSans-{w}.ttf"))
    print("done - now run: build_pdf.py  (set WEASYPRINT_DLL_DIRECTORIES=C:\\msys64\\mingw64\\bin)")


if __name__ == "__main__":
    build()
