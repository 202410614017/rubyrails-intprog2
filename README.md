# İnternet Programcılığı II — Sınav Çalışma Rehberi

Hafta 2–10 ders notlarının anlatımlı özeti. Site GitHub Pages üzerinde yayınlanır.

## Yayın adresi

Site yayına alındıktan sonra:

`https://202410614017.github.io/rubyrails-intprog2/`

## Dosyalar

| Dosya | Açıklama |
|-------|----------|
| `index.html` | Çalışma sitesi (GitHub Pages bunu gösterir) |
| `CALISMA_REHBERI.pdf` | PDF sürüm |
| `CALISMA_REHBERI.md` | Kaynak metin |
| `videos/hafta-2.mp4` … `hafta-10.mp4` | Haftalık kısa özet videolar (~30–70 sn) |
| `generate_videos.py` | Videoları yeniden üretmek için (TTS + slayt) |
| `web_enrichment.py` | PDF konulari icin internet kaynakli aciklama ve ornek kodlar |
| `build_site.py` | Siteyi yeniden üretmek için |

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
