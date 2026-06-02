# -*- coding: utf-8 -*-
"""build_cover.py - assemble the publishing PDF: prepend the cover image as a first page
to the typeset essay PDF. Reproducible (cover image + essay PDF -> with-cover PDF), so the
publishing edition is a build output, not a hand-assembled input.

Inputs:  build/covers/the-shifting-weight-of-nations-cover.png  (the canonical cover, source asset)
         OUTDIR/the-shifting-weight-of-nations.pdf               (the typeset essay, from build_pdf.py)
Output:  OUTDIR/the-shifting-weight-of-nations-with-cover.pdf

The cover page takes the essay's page width; its height is proportional to the cover image, so the
full cover shows uncropped. OUTDIR defaults to ../outputs (override with WON_OUTPUT_DIR).
"""
import io, os
from PIL import Image
from pypdf import PdfReader, PdfWriter

HERE = os.path.dirname(os.path.abspath(__file__))
OUTDIR = os.environ.get("WON_OUTPUT_DIR", os.path.join(HERE, "..", "outputs"))
COVER = os.path.join(HERE, "covers", "the-shifting-weight-of-nations-cover.png")
ESSAY = os.path.join(OUTDIR, "the-shifting-weight-of-nations.pdf")
OUT = os.path.join(OUTDIR, "the-shifting-weight-of-nations-with-cover.pdf")


def build():
    essay = PdfReader(ESSAY)
    page_w = float(essay.pages[0].mediabox.width)          # essay trim width (A4 = 595.28 pt)
    img = Image.open(COVER)
    dpi = img.width * 72.0 / page_w                        # map image width -> essay page width
    buf = io.BytesIO()
    img.convert("RGB").save(buf, format="PDF", resolution=dpi)
    cover = PdfReader(io.BytesIO(buf.getvalue()))
    writer = PdfWriter()
    writer.add_page(cover.pages[0])
    for p in essay.pages:
        writer.add_page(p)
    with open(OUT, "wb") as f:
        writer.write(f)
    return OUT, len(writer.pages)


if __name__ == "__main__":
    out, n = build()
    print("wrote", out, f"({n} pages)")
