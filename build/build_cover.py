# -*- coding: utf-8 -*-
"""build_cover.py - assemble the publishing PDF: prepend the cover image as a first page
to the typeset essay PDF. Reproducible (cover image + essay PDF -> with-cover PDF), so the
publishing edition is a build output, not a hand-assembled input.

Inputs:  build/covers/the-shifting-weight-of-nations-cover.png  (the canonical cover, source asset)
         OUTDIR/the-shifting-weight-of-nations.pdf               (the typeset essay, from build_pdf.py)
Output:  OUTDIR/the-shifting-weight-of-nations-with-cover.pdf

The cover page takes the essay's page width; its height is proportional to the cover image, so the
full cover shows uncropped. The cover is embedded LOSSLESSLY when img2pdf is available (preferred,
preserves the PNG for print); otherwise it falls back to Pillow's JPEG embedding. OUTDIR defaults
to ../outputs (override with WON_OUTPUT_DIR).
"""
import io, os
from PIL import Image
from pypdf import PdfReader, PdfWriter

HERE = os.path.dirname(os.path.abspath(__file__))
OUTDIR = os.environ.get("WON_OUTPUT_DIR", os.path.join(HERE, "..", "outputs"))
COVER = os.path.join(HERE, "covers", "the-shifting-weight-of-nations-cover.png")
ESSAY = os.path.join(OUTDIR, "the-shifting-weight-of-nations.pdf")
OUT = os.path.join(OUTDIR, "the-shifting-weight-of-nations-with-cover.pdf")


def _cover_page_pdf(page_w):
    """A single-page PDF of the cover at page_w (pt) wide, height proportional to the image."""
    iw, ih = Image.open(COVER).size
    page_h = page_w * ih / iw
    try:
        import img2pdf  # lossless: embeds the PNG as-is
        return img2pdf.convert(COVER, layout_fun=img2pdf.get_layout_fun((page_w, page_h)))
    except ImportError:
        buf = io.BytesIO()
        Image.open(COVER).convert("RGB").save(buf, format="PDF", resolution=iw * 72.0 / page_w)
        return buf.getvalue()


def build():
    essay = PdfReader(ESSAY)
    page_w = float(essay.pages[0].mediabox.width)          # essay trim width (A4 = 595.28 pt)
    cover = PdfReader(io.BytesIO(_cover_page_pdf(page_w)))
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
