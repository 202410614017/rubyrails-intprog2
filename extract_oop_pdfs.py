#!/usr/bin/env python3
"""NYP II PDF slaytlarini metne cikarir."""

from pathlib import Path

try:
    from pypdf import PdfReader
except ImportError:
    import subprocess
    import sys

    subprocess.check_call([sys.executable, "-m", "pip", "install", "pypdf", "-q"])
    from pypdf import PdfReader

BASE = Path(__file__).parent
OUT = BASE / "_oop_pdf_extract.txt"

PDFS = [
    Path(r"c:\Users\mehme\Downloads\NYP II - 1. Hafta (1).pdf"),
    Path(r"c:\Users\mehme\Downloads\NYP II - 2. Hafta (1).pdf"),
    Path(r"c:\Users\mehme\Downloads\NYP II - 3. Hafta (1).pdf"),
    Path(r"c:\Users\mehme\Downloads\NYP II - 4. Hafta (1).pdf"),
    Path(r"c:\Users\mehme\Downloads\NYP II - 5. Hafta (1).pdf"),
    Path(r"c:\Users\mehme\Downloads\NYP II - 6. Hafta  (1).pdf"),
    Path(r"c:\Users\mehme\Downloads\NYP II - 7. Hafta (1).pdf"),
    Path(r"c:\Users\mehme\Downloads\NYP II - 8. Hafta (1).pdf"),
    Path(r"c:\Users\mehme\Downloads\NYP II - 9. Hafta.pdf"),
]


def main():
    parts = []
    for pdf in PDFS:
        if not pdf.exists():
            print(f"UYARI: bulunamadi: {pdf}")
            continue
        reader = PdfReader(str(pdf))
        text = "\n".join(page.extract_text() or "" for page in reader.pages)
        parts.append(f"===== {pdf.name} =====\n{text}")
    OUT.write_text("\n\n".join(parts), encoding="utf-8")
    print(f"OK {OUT} ({OUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
