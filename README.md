# Sınav Çalışma Merkezi

**Internet Programcılığı II** + **Nesne Yönelimli Programlama** — tek sitede.

## Yayın adresi

`https://202410614017.github.io/rubyrails-intprog2/`

## Bölümler

| Bölüm | İçerik |
|-------|--------|
| **Int Prog II** | Hafta 2–10 Rails arşivi, videolar, quiz, 7 günlük plan |
| **OOP** | Kapsülleme, kalıtım, SOLID, LSP Solo Leveling (PDF gelince genişler) |

## Dosyalar

| Dosya | Açıklama |
|-------|----------|
| `index.html` | Çalışma sitesi |
| `CALISMA_REHBERI.md` | Int Prog PDF arşivi kaynağı |
| `oop_content.py` | OOP ders konuları (PDF gelince genişlet) |
| `solid_principles.py` | SOLID ilkeleri |
| `lsp_solo_leveling.py` | LSP Solo Leveling örneği |
| `build_site.py` | Siteyi yeniden üret |

## Siteyi güncellemek

```bash
py generate_videos.py   # isteğe bağlı — videoları yeniden üret
py build_site.py
git add .
git commit -m "Site guncellendi"
git push
```

## GitHub Pages ayarı

Repo → **Settings** → **Pages** → Branch: **main**, Folder: **/ (root)**
