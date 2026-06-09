#!/usr/bin/env python3
"""Kaynak dosyalar degisince build_site.py calistirir (Live Server otomatik yeniler)."""

import subprocess
import sys
import time
from pathlib import Path

BASE = Path(__file__).parent
WATCH = [
    "build_site.py",
    "term_glossary.py",
    "web_enrichment.py",
    "ruby_faq_tr.py",
    "quiz_data.py",
    "study_plan.py",
    "solid_principles.py",
    "solid_class_examples.py",
    "lsp_solo_leveling.py",
    "oop_content.py",
    "oop_week9_exercises.py",
    "video_data.py",
    "CALISMA_REHBERI.md",
    "OOP_CALISMA.md",
    "weekly_paths.py",
]


def mtimes() -> dict[str, float]:
    out = {}
    for name in WATCH:
        p = BASE / name
        if p.exists():
            out[name] = p.stat().st_mtime
    return out


def rebuild() -> None:
    print("[dev_watch] build_site.py calistiriliyor...", flush=True)
    subprocess.run([sys.executable, str(BASE / "build_site.py")], cwd=BASE, check=True)
    print("[dev_watch] index.html guncellendi.", flush=True)


def main() -> None:
    print("Dosya izleme acik. Ctrl+C ile dur.", flush=True)
    print("Live Server: index.html -> Open with Live Server", flush=True)
    print("Izlenen:", ", ".join(WATCH[:5]), "...", flush=True)
    prev = mtimes()
    rebuild()
    while True:
        time.sleep(1)
        cur = mtimes()
        if cur != prev:
            prev = cur
            try:
                rebuild()
            except subprocess.CalledProcessError as e:
                print(f"[dev_watch] Hata: {e}", flush=True)


if __name__ == "__main__":
    main()
