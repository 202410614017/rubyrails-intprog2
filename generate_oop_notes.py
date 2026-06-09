#!/usr/bin/env python3
"""NYP II PDF cikarimindan OOP_CALISMA.md uretir."""

import re
from pathlib import Path

BASE = Path(__file__).parent
EXTRACT = BASE / "_oop_pdf_extract.txt"
OUTPUT = BASE / "OOP_CALISMA.md"

WEEK_TITLES = {
    "1. Hafta": ("Hafta 1 — OOP Giriş & Prosedürel Programlama", 1),
    "2. Hafta": ("Hafta 2 — Sınıflar & Nesneler", 2),
    "3. Hafta": ("Hafta 3 — Kapsülleme", 3),
    "4. Hafta": ("Hafta 4 — Kalıtım (Miras)", 4),
    "5. Hafta": ("Hafta 5 — super, Çoklu Miras, Statik Metot", 5),
    "6. Hafta": ("Hafta 6 — Polimorfizm & Soyut Sınıf", 6),
    "7. Hafta": ("Hafta 7 — Tasarım Desenleri Giriş", 7),
    "8. Hafta": ("Hafta 8 — Tasarım Desenleri Devam", 8),
    "9. Hafta": ("Hafta 9 — SOLID Prensipleri", 9),
}

SKIP_LINE = re.compile(
    r"^(Nesne Yönelimli|Programlama|Öğr\. Gör\.|ecmel\.|\d+/\d+/\d+ \d+$)$",
    re.I,
)

OOP_HEADERS = [
    r"^\d+\. Hafta$",
    r"^Dersin ",
    r"^Prosedürel",
    r"^Nesne Yönelimli",
    r"^OOP",
    r"^Sınıf",
    r"^Nesne ",
    r"^__init__",
    r"^Instance",
    r"^self ",
    r"^Miras",
    r"^Kalıt",
    r"^Kapsül",
    r"^Polimorf",
    r"^Soyut",
    r"^Abstract",
    r"^@staticmethod",
    r"^super",
    r"^Çoklu Miras",
    r"^MRO",
    r"^SOLID",
    r"^Single Responsibility",
    r"^Tek Sorumluluk",
    r"^Open/Closed",
    r"^Açık/Kapalı",
    r"^Liskov",
    r"^Interface Segregation",
    r"^Arayüz Ayrım",
    r"^Dependency Inversion",
    r"^Bağımlılık",
    r"Alıştırma",
    r"Presibi",
    r"Prensibi",
    r"^Design Pattern",
    r"^Tasarım",
    r"^Singleton",
    r"^Factory",
    r"^Observer",
    r"^Decorator",
    r"^Encapsulation",
    r"^Inheritance",
    r"^Abstraction",
    r"^Getter",
    r"^Property",
    r"^@property",
    r"^Metot",
    r"^Constructor",
    r"^Destructor",
    r"^Overriding",
    r"^Overloading",
    r"^Duck Typing",
    r"^Magic Method",
    r"^__str__",
    r"^__repr__",
    r"^Class ",
    r"^Static",
    r"^Classmethod",
    r"^Teams",
    r"^Geliştirme Ortam",
    r"^Beklentiler",
    r"^Ders Kaynak",
    r"^Global ",
    r"^Fonksiyon",
    r"^Encapsulated",
]

HEADER_PATTERNS = [re.compile(p, re.I) for p in OOP_HEADERS]

TOPIC_INDEX = """
## Konu İndeksi — NYP II

| Konu | Hafta | Açıklama |
|------|-------|----------|
| Prosedürel vs OOP | 1 | Fonksiyon merkezli vs nesne merkezli |
| Sınıf & Nesne | 2 | class, __init__, self, instance variable |
| Kapsülleme | 3 | private, getter/setter, @property |
| Kalıtım | 4 | class Child(Parent), override |
| super() | 5 | Üst sınıf constructor/metot çağrısı |
| Çoklu miras & MRO | 5 | Birden fazla üst sınıf |
| @staticmethod | 5 | Nesneye bağlı olmayan metot |
| Polimorfizm | 6 | Aynı arayüz, farklı davranış |
| Soyut sınıf (ABC) | 6 | @abstractmethod |
| Tasarım desenleri | 7–8 | Singleton, Factory, Observer vb. |
| **SOLID** | 9 | S, O, L, I, D ilkeleri |
| SRP | 9 | Tek sorumluluk |
| OCP | 9 | Açık/kapalı — AlanHesaplayici alıştırması |
| LSP | 9 | Dosya sistemi alıştırması |
| ISP | 9 | Akıllı ev cihazları alıştırması |
| DIP | 9 | Bildirim sistemi alıştırması |
"""

WEEK9_EXERCISES_MD = """
## Hafta 9 — SOLID Alıştırmaları (Çözümlü)

Site bolumu **Hafta 10 — SOLID Calisma & Odev Cozumleri** (#hafta-10-solid-calisma-odev-cozumleri) altinda 4 alistirmanin kotu/iyi kodu ve aciklamasi yer alir.

| Ilke | Konu | Gist |
|------|------|------|
| OCP | AlanHesaplayici | Sekil soyut sinifi ile genislet |
| LSP | Dosya sistemi | Okunabilir/Yazilabilir arayuzleri ayir |
| ISP | Akilli ev cihazlari | Kucuk arayuzler (Acilabilir, Sicaklik...) |
| DIP | Bildirim sistemi | BildirimKanali soyutlamasi |
"""


def is_code_line(line: str) -> bool:
    s = line.strip()
    if not s:
        return False
    if s.startswith("class ") or s.startswith("def ") or s.startswith("import "):
        return True
    if s.startswith("from ") or s.startswith("@") or s.startswith("self."):
        return True
    if s.startswith("print(") or s.startswith("return ") or s.startswith("pass"):
        return True
    if s.startswith("elif ") or s.startswith("else:") or s.startswith("if "):
        return True
    if re.match(r"^\w+\(", s):
        return True
    return False


def should_skip(line: str) -> bool:
    s = line.strip()
    if not s:
        return True
    if SKIP_LINE.search(s):
        return True
    if re.match(r"^\d+/\d+/\d+", s):
        return True
    if s in {"I", "Programlama"}:
        return True
    if re.match(r"^\d+\. Hafta$", s) and len(s) < 15:
        return False  # keep as potential header context
    return False


def is_header(line: str) -> bool:
    s = line.strip()
    if len(s) > 90 or len(s) < 3:
        return False
    if s.startswith("•") or s.startswith("http"):
        return False
    if is_code_line(s):
        return False
    return any(p.search(s) for p in HEADER_PATTERNS)


def format_week_body(raw: str) -> str:
    lines = raw.splitlines()
    out = []
    in_code = False
    code_buf = []
    code_lang = "python"

    def flush_code():
        nonlocal in_code, code_buf
        if code_buf:
            out.append(f"```{code_lang}")
            out.extend(code_buf)
            out.append("```")
            out.append("")
            code_buf = []
        in_code = False

    for line in lines:
        stripped = line.strip()
        if should_skip(stripped):
            if in_code:
                flush_code()
            continue

        if is_header(stripped):
            flush_code()
            out.append(f"### {stripped}")
            out.append("")
            continue

        if is_code_line(stripped) or (in_code and stripped):
            in_code = True
            code_buf.append(stripped)
            continue

        flush_code()
        if stripped.startswith("•"):
            out.append(f"- {stripped[1:].strip()}")
        else:
            out.append(stripped)
        out.append("")

    flush_code()
    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def split_pdfs(text: str):
    parts = re.split(r"===== (.+?) =====\n", text)
    chunks = []
    for i in range(1, len(parts), 2):
        chunks.append((parts[i], parts[i + 1] if i + 1 < len(parts) else ""))
    return chunks


def match_week(fname: str):
    for key, val in WEEK_TITLES.items():
        if key.replace(" ", "") in fname.replace(" ", ""):
            return val
    m = re.search(r"(\d+)\.\s*Hafta", fname)
    if m:
        n = int(m.group(1))
        key = f"{n}. Hafta"
        return WEEK_TITLES.get(key, (f"Hafta {n}", n))
    return None, None


def main():
    if not EXTRACT.exists():
        raise SystemExit("Once: py extract_oop_pdfs.py")

    raw = EXTRACT.read_text(encoding="utf-8")
    sections = [TOPIC_INDEX.strip(), ""]

    for fname, body in split_pdfs(raw):
        title, num = match_week(fname)
        if not title:
            continue
        sections.append(f"## {title}")
        sections.append("")
        sections.append(format_week_body(body))
        sections.append("")
        sections.append("---")
        sections.append("")

    sections.append(WEEK9_EXERCISES_MD.strip())

    header = """# Nesne Yönelimli Programlama II — Eksiksiz Ders Notu Arşivi

> **Kaynak:** NYP II Hafta 1–9 slaytları (Öğr. Gör. Ecmel Albayrak)  
> Python OOP + SOLID prensipleri. Hafta 9 alıştırmaları site üzerinde çözümlü.

"""
    OUTPUT.write_text(header + "\n".join(sections), encoding="utf-8")
    print(f"OK {OUTPUT} ({OUTPUT.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
