#!/usr/bin/env python3
"""CALISMA_REHBERI.md -> sade anlatim sitesi + PDF"""

import html
import re
import subprocess
import sys
from pathlib import Path

try:
    import markdown
    from markdown.extensions.tables import TableExtension
    from markdown.extensions.fenced_code import FencedCodeExtension
    from markdown.extensions.toc import TocExtension
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "markdown", "-q"])
    import markdown
    from markdown.extensions.tables import TableExtension
    from markdown.extensions.fenced_code import FencedCodeExtension
    from markdown.extensions.toc import TocExtension

from quiz_data import QUIZ
from study_plan import STUDY_PLAN, MUST_KNOW
from web_enrichment import TOPICS, match_panel_topics, topics_for_week
from solid_principles import SOLID, STUDENT_HEADER
from solid_class_examples import CLASS_EXAMPLES_BY_LETTER
from lsp_solo_leveling import (
    LSP_INTRO, BAD_CODE, BAD_WHY, GOOD_CODE, GOOD_WHY, LSP_FIVE_RULES, CREDIT,
)
from oop_content import OOP_META, OOP_MUST_KNOW, OOP_TOPICS, OOP_PDF_PLACEHOLDER
from oop_week9_exercises import WEEK9_EXERCISES
from term_glossary import ALL_GLOSSARY, INTPROG_GLOSSARY, OOP_GLOSSARY

BASE = Path(__file__).parent
MD_FILE = BASE / "CALISMA_REHBERI.md"
OOP_MD_FILE = BASE / "OOP_CALISMA.md"
HTML_FILE = BASE / "index.html"
PDF_FILE = BASE / "CALISMA_REHBERI.pdf"

RUBY_ICON_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" class="course-icon-svg" aria-hidden="true"><path fill="#CC342D" d="M64 10 118 36v56L64 118 10 92V36z"/><path fill="#9B111E" d="M64 10v108L10 92V36z" opacity=".45"/><path fill="#fff" d="M64 10l54 26-54 26L10 36z" opacity=".22"/><path fill="#fff" d="M64 62 118 36v28L64 92 10 64V36z" opacity=".12"/></svg>"""

PYTHON_ICON_SVG = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 128 128" class="course-icon-svg" aria-hidden="true"><path fill="#3776AB" d="M63.9 10.5c-30.5 0-28.6 13.2-28.6 13.2v13.6h29.1v2H18.3S10 37.8 10 63.9c0 26.1 7.9 25.2 7.9 25.2h9.4v-12.2s-.4-7.9 7.8-7.9h29.1s7.6.1 7.6-7.3V23.7s1.2-13.2-28.6-13.2zM47.9 18.1a4.9 4.9 0 1 1 0 9.8 4.9 4.9 0 0 1 0-9.8z"/><path fill="#FFD43B" d="M64.1 117.5c30.5 0 28.6-13.2 28.6-13.2V90.7H63.6v-2h46.1s8.3 1.5 8.3-24.6c0-26.1-7.9-25.2-7.9-25.2h-9.4v12.2s.4 7.9-7.8 7.9H63.6s-7.6-.1-7.6 7.3v19.4s-1.2 13.2 28.5 13.2zm16.2-7.6a4.9 4.9 0 1 1 0-9.8 4.9 4.9 0 0 1 0 9.8z"/></svg>"""

RUBY_ICON_SM = RUBY_ICON_SVG.replace('class="course-icon-svg"', 'class="course-icon-svg course-icon-sm"')
PYTHON_ICON_SM = PYTHON_ICON_SVG.replace('class="course-icon-svg"', 'class="course-icon-svg course-icon-sm"')

WEEK_META = {
    "hafta-2-ruby-rails-giris": {
        "num": 2, "tag": "Ruby & Rails",
        "summary": "Ruby dilini ogrenir, Rails projesini kurar ve MVC yapisini anlarsin.",
        "simple": [
            "Ruby'de sayi, metin, dizi — hepsi nesnedir.",
            "Rails = Model (veri) + View (arayuz) + Controller (mantik).",
            "routes.rb istegi yonlendirir, controller isler, view gosterir.",
            "rails new, db:create, rails s ile proje calistirilir.",
        ],
        "focus": ["Her sey nesne", "MVC akisi", "rails s"],
    },
    "hafta-3-orm-active-record": {
        "num": 3, "tag": "Veritabani",
        "summary": "SQL yazmadan veritabani islemleri yaparsin. Tablo = Model sinifi.",
        "simple": [
            "ORM: veritabani tablosu = Ruby sinifi.",
            "Post.create ile kayit ekle, Post.all ile listele.",
            "find id arar (hata verir), find_by arar (nil doner), where filtreler.",
            "Migration ile tablo/kolon ekle; rails db:migrate calistir.",
        ],
        "focus": ["ORM", "find vs where", "migration"],
    },
    "hafta-4-enum-routes-controllers": {
        "num": 4, "tag": "Routes & CRUD",
        "summary": "URL'leri controller'a baglarsin. 7 CRUD islemi resources ile gelir.",
        "simple": [
            "GET okur, POST olusturur, PUT/PATCH gunceller, DELETE siler.",
            "resources :posts otomatik 7 route olusturur.",
            "Enum: sayisal degerlere anlamli isim verir (draft: 0).",
            "@degisken controller'dan view'a veri tasir.",
        ],
        "focus": ["HTTP metotlari", "resources :posts", "Enum"],
    },
    "hafta-5-form-helpers-strong-parameters": {
        "num": 5, "tag": "Form & Guvenlik",
        "summary": "Form ile veri alir, Strong Parameters ile guvenli kaydedersin.",
        "simple": [
            "form_with model: @post ile form olusturulur.",
            "post_params sadece izin verilen alanlari gecirir.",
            "Partial (_form) ile tekrar eden kod azaltilir.",
            "before_action ile ortak kod tek yerde toplanir.",
        ],
        "focus": ["form_with", "Strong Params", "partial"],
    },
    "hafta-6-bootstrap-frontend": {
        "num": 6, "tag": "Bootstrap",
        "summary": "Blog arayuzunu Bootstrap ile duzenlersin.",
        "simple": [
            "Grid 12 sutun: col-md-6 = yarim genislik.",
            "container ortalar, container-fluid tam genislik.",
            "Navbar ve footer partial olarak layout'a eklenir.",
            "card, btn siniflari ile modern gorunum.",
        ],
        "focus": ["12 sutun grid", "navbar/footer", "card"],
    },
    "hafta-7-model-iliskileri-kategori": {
        "num": 7, "tag": "Iliskiler",
        "summary": "Tablolar arasi baglanti kurarsin. Post-Category coktan coga.",
        "simple": [
            "belongs_to: FK bu tabloda. has_many: karsi taraf cok kayit.",
            "HABTM: ara tablo, id yok, iki FK var.",
            "scaffold ile model+view+controller hizli olusur.",
            "category_ids: [] ile coklu kategori secilir.",
        ],
        "focus": ["belongs_to/has_many", "HABTM", "scaffold"],
    },
    "hafta-8-validation-active-storage": {
        "num": 8, "tag": "Dogrulama",
        "summary": "Veri kurallarini modelde tanimlarsin. Resim yuklemek icin Active Storage.",
        "simple": [
            "validates: veriyi kontrol eder, gecersizse kaydetmez.",
            "normalizes: kaydetmeden once duzenler (bosluk sil, buyuk harf).",
            "presence, uniqueness, length en sik kullanilan kurallar.",
            "has_one_attached :image ile dosya yukleme.",
        ],
        "focus": ["validates", "normalizes", "Active Storage"],
    },
    "hafta-9-i18n-friendlyid-action-text": {
        "num": 9, "tag": "I18n & Gems",
        "summary": "Coklu dil, SEO URL ve zengin metin editoru.",
        "simple": [
            "I18n.t ile metin cevirirsin (tr.yml, en.yml).",
            "?locale=en ile dil degistirilir.",
            "FriendlyId: /posts/1 yerine /posts/baslik-slug.",
            "Action Text: zengin metin editoru (kalin, liste, resim).",
        ],
        "focus": ["I18n.t", "FriendlyId", "Action Text"],
    },
    "hafta-10-devise-authorization": {
        "num": 10, "tag": "Devise",
        "summary": "Kullanici girisi ve rol bazli yetkilendirme.",
        "simple": [
            "Devise: kayit ol, giris yap, sifre sifirla.",
            "Authentication = kimlik, Authorization = yetki.",
            "authenticate_user! giris zorunlu kilar.",
            "current_user.posts.new ile post kullaniciya atanir.",
        ],
        "focus": ["Devise", "authenticate_user!", "roller"],
    },
}

OOP_WEEK_META = {
    "hafta-1-oop-giris-prosedurel-programlama": {
        "num": 1, "tag": "Giris",
        "summary": "Prosedurel vs OOP, ders kurallari, OOP tarihi ve temel prensipler.",
        "simple": ["Prosedurel = fonksiyon + global veri", "OOP = nesne (veri + davranis)", "Python'da class ile baslariz"],
    },
    "hafta-2-siniflar-nesneler": {
        "num": 2, "tag": "Sinif & Nesne",
        "summary": "class, __init__, self, instance variable ve instance metotlar.",
        "simple": ["class = kalip, nesne = ornek", "self = bu nesne", "__init__ otomatik calisir"],
    },
    "hafta-3-kapsulleme": {
        "num": 3, "tag": "Kapsulleme",
        "summary": "Veriyi gizleme, getter/setter, @property, private convention.",
        "simple": ["_ veya __ ile gizle", "@property ile kontrollu erisim", "Encapsulation = guvenli veri"],
    },
    "hafta-4-kalitim-miras": {
        "num": 4, "tag": "Kalitim",
        "summary": "class Child(Parent), method overriding, isinstance.",
        "simple": ["Kalitim = kod tekrarini azaltir", "Override = ust metodu yeniden yaz", "super() ile ust cagir"],
    },
    "hafta-5-super-coklu-miras-statik-metot": {
        "num": 5, "tag": "super & MRO",
        "summary": "super(), coklu miras, MRO sirasi, @staticmethod.",
        "simple": ["super().__init__() ust constructor", "MRO = metot arama sirasi", "@staticmethod nesne gerektirmez"],
    },
    "hafta-6-polimorfizm-soyut-sinif": {
        "num": 6, "tag": "Polimorfizm",
        "summary": "Polimorfizm, duck typing, ABC ve @abstractmethod.",
        "simple": ["Ayni metod farkli davranis", "ABC'den dogrudan nesne yok", "Duck typing = ne yaptigina bak"],
    },
    "hafta-7-tasarim-desenleri-giris": {
        "num": 7, "tag": "Design Patterns",
        "summary": "Tasarim desenleri giris: Singleton, Factory vb.",
        "simple": ["Desen = tekrar eden cozum sablonu", "Singleton tek nesne", "Factory nesne uretimi"],
    },
    "hafta-8-tasarim-desenleri-devam": {
        "num": 8, "tag": "Patterns Devam",
        "summary": "Observer, Decorator ve diger desenler.",
        "simple": ["Observer olay dinler", "Decorator davranis ekler", "Desenler SOLID ile uyumlu olmali"],
    },
    "hafta-9-solid-prensipleri": {
        "num": 9, "tag": "SOLID (PDF)",
        "summary": "PDF 9. hafta slaytlari: SOLID tanimlari, SRP/OCP/LSP/ISP/DIP anlatimi.",
        "simple": ["SRP tek is", "OCP genislet", "LSP yerine koy", "ISP kucuk arayuz", "DIP soyut bagimlilik"],
    },
    "hafta-10-solid-calisma-odev-cozumleri": {
        "num": 10, "tag": "SOLID Calisma",
        "summary": "Odev formatinda 5 SOLID ilkesi, PDF alistirmalari (OCP/LSP/ISP/DIP) cozumlu, LSP Solo Leveling.",
        "simple": [
            "Her ilke: tanim, amac, kotu/iyi kod, neden?",
            "Sinif arkadas ornekleri: SRP, OCP, LSP, ISP, DIP (Python)",
            "AlanHesaplayici, Dosya, Cihaz, Bildirim odevleri",
            "Solo Leveling LSP ornegi — sinav icin",
        ],
    },
}

PANEL_PRIORITY = {
    "ruby": 1, "temel": 1, "metot": 2, "degisken": 3, "sinif": 4, "modul": 5,
    "blok": 6, "kosul": 7, "rails blog": 8, "kurulum": 8, "dizin": 9, "mvc": 10,
    "credentials": 11, "anasayfa": 12, "rubygems": 13,
    "orm": 1, "active record": 2, "veri tur": 3, "model olustur": 4, "tablo": 5,
    "konsol": 6, "find": 7, "where": 8, "order": 9, "guncelle": 10, "sil": 11,
    "migration": 12, "db komut": 13,
    "status": 1, "enum": 2, "scope": 3, "http": 4, "crud": 5, "route": 6,
    "controller": 7, "erb": 8, "path": 9, "seed": 10,
    "action view": 1, "form": 2, "strong": 3, "link": 4, "partial": 5,
    "before": 6, "button": 7, "destroy": 8,
    "bootstrap": 1, "breakpoint": 2, "container": 3, "grid": 4, "navbar": 5,
    "footer": 6, "card": 7, "image": 8,
    "ilisk": 1, "belongs": 2, "has_many": 3, "has_one": 4, "habtm": 5,
    "scaffold": 6, "kategori": 7, "join": 8,
    "validation": 1, "normaliz": 2, "helper": 3, "hata": 4, "active storage": 5,
    "i18n": 1, "locale": 2, "yerellestir": 3, "friendly": 4, "action text": 5,
    "devise": 1, "authentication": 2, "kurulum": 3, "rol": 4, "admin": 5, "user": 6,
}

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Sinav Calisma Merkezi | Int Prog II + OOP</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=DM+Sans:ital,opsz,wght@0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&family=IBM+Plex+Mono:wght@400;500&display=swap" rel="stylesheet">
  <style>
    :root {{
      --bg: #f8f9fb;
      --paper: #ffffff;
      --sidebar: #ffffff;
      --text: #1a1d26;
      --text-soft: #5c6370;
      --line: #e8ebf0;
      --accent: #b91c1c;
      --accent-soft: #fef2f2;
      --accent-border: #fecaca;
      --blue-soft: #eff6ff;
      --blue-border: #bfdbfe;
      --blue-text: #1d4ed8;
      --green-soft: #f0fdf4;
      --green-border: #bbf7d0;
      --green-text: #15803d;
      --amber-soft: #fffbeb;
      --amber-border: #fde68a;
      --amber-text: #b45309;
      --code-bg: #f4f6f8;
      --shadow: 0 1px 3px rgba(16,24,40,.06), 0 1px 2px rgba(16,24,40,.04);
      --shadow-lg: 0 8px 24px rgba(16,24,40,.08);
      --sidebar-w: 520px;
      --nav-strip-h: min(38vh, 320px);
      --pane-divider: #e2e8f0;
      --oop-accent: #6d28d9;
      --oop-soft: #f5f3ff;
      --oop-border: #ddd6fe;
      --oop-text: #5b21b6;
    }}
    * {{ box-sizing: border-box; margin: 0; padding: 0; }}
    html {{ scroll-behavior: smooth; }}
    body {{
      font-family: 'DM Sans', system-ui, sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.65;
      font-size: 15px;
    }}
    .layout {{ display: flex; flex-direction: column; height: 100vh; overflow: hidden; }}

    .site-nav {{
      flex-shrink: 0; background: var(--paper);
      border-bottom: 2px solid var(--line); box-shadow: var(--shadow);
      z-index: 200;
    }}
    .site-nav-brand {{
      display: flex; align-items: center; justify-content: space-between; gap: 1rem;
      padding: .65rem 1.25rem; border-bottom: 1px solid var(--line);
    }}
    .site-nav-brand .brand {{ padding: 0; border: none; margin: 0; flex: 1; }}
    .brand-kicker {{ font-size: .65rem; font-weight: 600; letter-spacing: .08em; text-transform: uppercase; color: var(--accent); }}
    .site-nav-brand .brand h1 {{ font-size: .95rem; font-weight: 700; margin-top: .2rem; line-height: 1.3; }}
    .site-nav-brand .brand p {{ font-size: .72rem; color: var(--text-soft); margin-top: .2rem; }}
    .site-nav-dual {{
      display: grid; grid-template-columns: 1fr 1fr;
      max-height: var(--nav-strip-h);
    }}
    .nav-col {{
      overflow-y: auto; padding-bottom: .75rem; min-width: 0;
    }}
    .nav-col-intprog {{
      border-right: 2px solid var(--accent-border);
      background: linear-gradient(180deg, #fffbfb 0%, #fff 100%);
    }}
    .nav-col-oop {{
      background: linear-gradient(180deg, #fdfcff 0%, #fff 100%);
    }}
    .nav-col-title {{
      padding: .55rem 1rem .4rem; font-size: .68rem; font-weight: 700;
      text-transform: uppercase; letter-spacing: .06em; position: sticky; top: 0; z-index: 2;
    }}
    .nav-col-title-intprog {{ background: #fef2f2; color: var(--accent); border-bottom: 1px solid var(--accent-border); }}
    .nav-col-title-oop {{ background: var(--oop-soft); color: var(--oop-text); border-bottom: 1px solid var(--oop-border); }}
    .nav-col a {{
      display: flex; align-items: center; gap: .5rem;
      padding: .42rem 1rem; color: var(--text-soft); text-decoration: none;
      font-size: .8rem; border-left: 3px solid transparent; transition: .12s;
    }}
    .nav-col a .w-num {{
      width: 1.25rem; height: 1.25rem; border-radius: 5px; background: var(--bg);
      display: inline-flex; align-items: center; justify-content: center;
      font-size: .65rem; font-weight: 700; color: var(--text-soft); flex-shrink: 0;
    }}
    .nav-col-intprog a:hover, .nav-col-intprog a.active {{
      color: var(--text); background: var(--accent-soft); border-left-color: var(--accent);
    }}
    .nav-col-intprog a.active .w-num {{ background: var(--accent); color: white; }}
    .nav-col-oop a:hover, .nav-col-oop a.active {{
      color: var(--text); background: var(--oop-soft); border-left-color: var(--oop-accent);
    }}
    .nav-col-oop a.active .w-num {{ background: var(--oop-accent); color: white; }}
    .nav-label {{ padding: .65rem 1rem .25rem; font-size: .65rem; font-weight: 600; text-transform: uppercase; letter-spacing: .06em; color: #9ca3af; }}

    .main {{
      flex: 1; min-height: 0; padding: 0; max-width: none; overflow: hidden;
      display: flex; flex-direction: column;
    }}
    .course-picker {{
      flex-shrink: 0; display: grid; grid-template-columns: 1fr 1fr; gap: .75rem;
      padding: .75rem 1rem; background: var(--paper);
      border-bottom: 1px solid var(--line); box-shadow: var(--shadow);
    }}
    .course-picker-label {{
      grid-column: 1 / -1; font-size: .72rem; font-weight: 700; text-transform: uppercase;
      letter-spacing: .07em; color: var(--text-soft); margin-bottom: -.25rem;
    }}
    .courses-split {{
      display: grid; grid-template-columns: 1fr 1fr; flex: 1; min-height: 0;
    }}
    .course-pane {{
      overflow-y: auto; height: 100%; scroll-behavior: smooth;
      padding: 1rem 1rem 2.5rem; min-width: 0;
      border-right: 1px solid var(--pane-divider);
    }}
    .course-pane:last-child {{ border-right: none; }}
    .course-pane-intprog {{ background: #ffffff; }}
    .course-pane-oop {{ background: #fafafa; }}

    .term-tip {{ position: relative; display: inline-flex; align-items: center; vertical-align: middle; }}
    .term-tip-btn {{
      width: 1.15rem; height: 1.15rem; margin-left: .25rem; padding: 0;
      border-radius: 50%; border: 1px solid var(--blue-border); background: var(--blue-soft);
      color: var(--blue-text); font-size: .62rem; font-weight: 800; font-family: inherit;
      cursor: pointer; line-height: 1; flex-shrink: 0;
    }}
    .term-tip-btn:hover {{ background: #dbeafe; }}
    .term-tip-pop {{
      display: none; position: absolute; left: 0; top: calc(100% + 6px); z-index: 500;
      width: min(280px, 85vw); padding: .65rem .75rem; border-radius: 10px;
      background: #1e293b; color: #f1f5f9; font-size: .78rem; line-height: 1.5;
      box-shadow: 0 12px 28px rgba(0,0,0,.25); text-align: left;
    }}
    .term-tip-pop.open {{ display: block; }}
    .term-tip-pop strong {{ display: block; color: #fff; font-size: .82rem; margin-bottom: .35rem; }}
    .term-tip-pop p {{ margin: .3rem 0; color: #cbd5e1; }}
    .term-tip-pop em {{ color: #94a3b8; font-style: normal; font-weight: 600; }}
    .term-tip-code {{
      margin: .45rem 0 0; padding: .45rem .55rem; background: #0f172a; border-radius: 6px;
      font-size: .68rem; line-height: 1.45; overflow-x: auto; white-space: pre-wrap;
    }}
    .panel-inner td {{ position: relative; vertical-align: top; }}
    .nav-col-oop a.active .w-num {{ background: var(--oop-accent); color: white; }}

    .course-hub {{
      display: contents;
    }}
    @media (min-width: 640px) {{ .course-hub {{ display: contents; }} }}

    .course-card {{
      display: flex; align-items: center; gap: .85rem;
      border: 1px solid var(--line); border-radius: var(--radius); padding: 1rem 1.15rem;
      background: var(--paper); box-shadow: var(--shadow); text-decoration: none; color: inherit;
      transition: .15s;
    }}
    .course-card:hover {{ box-shadow: var(--shadow-lg); transform: translateY(-1px); }}
    .course-card.intprog {{ border-top: 4px solid var(--accent); background: linear-gradient(180deg, #fffbfb 0%, #fff 100%); }}
    .course-card.oop {{ border-top: 4px solid var(--oop-accent); background: linear-gradient(180deg, #fdfcff 0%, #fff 100%); }}
    .course-icon-svg {{ width: 52px; height: 52px; flex-shrink: 0; display: block; }}
    .course-icon-sm {{ width: 18px; height: 18px; }}
    .course-card-body {{ flex: 1; min-width: 0; }}
    .course-card-kicker {{ font-size: .68rem; font-weight: 700; text-transform: uppercase; letter-spacing: .06em; }}
    .course-card.intprog .course-card-kicker {{ color: var(--accent); }}
    .course-card.oop .course-card-kicker {{ color: var(--oop-accent); }}
    .course-card h3 {{ font-size: 1.02rem; margin: .25rem 0; }}
    .course-card p {{ font-size: .82rem; color: var(--text-soft); line-height: 1.45; margin: 0; }}
    .nav-col-title {{ display: flex; align-items: center; gap: .45rem; }}

    .topbar {{
      background: var(--paper); border: 1px solid var(--line); border-radius: var(--radius);
      padding: 1.75rem 2rem; margin-bottom: 1.75rem; box-shadow: var(--shadow);
    }}
    .topbar h2 {{ font-size: 1.55rem; font-weight: 700; letter-spacing: -.02em; }}
    .topbar > p {{ color: var(--text-soft); margin-top: .5rem; max-width: 540px; }}
    .topbar-actions {{ display: flex; gap: .6rem; margin-top: 1.1rem; flex-wrap: wrap; }}
    .btn {{
      display: inline-flex; align-items: center; gap: .35rem;
      padding: .5rem .95rem; border-radius: 8px; font-size: .84rem; font-weight: 600;
      text-decoration: none; cursor: pointer; border: none; font-family: inherit;
    }}
    .btn-red {{ background: var(--accent); color: white; }}
    .btn-red:hover {{ background: #991b1b; }}
    .btn-ghost {{ background: white; color: var(--text); border: 1px solid var(--line); }}
    .btn-ghost:hover {{ border-color: #cbd5e1; }}

    .week-block {{
      background: var(--paper); border: 1px solid var(--line); border-radius: var(--radius);
      margin-bottom: 1.5rem; box-shadow: var(--shadow); overflow: hidden;
      scroll-margin-top: 1rem;
    }}
    .week-head {{
      padding: 1.35rem 1.5rem 1.1rem;
      border-bottom: 1px solid var(--line);
      background: linear-gradient(180deg, #fff 0%, #fafbfc 100%);
    }}
    .week-head-top {{ display: flex; align-items: center; gap: .75rem; flex-wrap: wrap; margin-bottom: .65rem; }}
    .week-badge {{
      background: var(--accent); color: white; font-size: .72rem; font-weight: 700;
      padding: .25rem .6rem; border-radius: 6px;
    }}
    .week-tag {{ font-size: .78rem; color: var(--text-soft); font-weight: 500; }}
    .week-head h2 {{ font-size: 1.2rem; font-weight: 700; letter-spacing: -.01em; border: none; margin: 0; padding: 0; }}
    .week-summary {{
      background: var(--blue-soft); border: 1px solid var(--blue-border);
      border-radius: 8px; padding: .85rem 1rem; margin-top: .85rem;
      font-size: .88rem; color: #1e3a5f; line-height: 1.55;
    }}
    .week-summary strong {{ color: var(--blue-text); font-weight: 600; }}
    .focus-chips {{ display: flex; flex-wrap: wrap; gap: .4rem; margin-top: .75rem; }}
    .chip {{
      font-size: .72rem; font-weight: 500; padding: .25rem .55rem; border-radius: 999px;
      background: var(--green-soft); color: var(--green-text); border: 1px solid var(--green-border);
    }}

    .week-body {{ padding: .25rem 1.5rem 1.25rem; }}

    .week-video {{
      margin: .85rem 0 1rem; border: 1px solid var(--line); border-radius: 10px;
      overflow: hidden; background: #0f172a;
    }}
    .week-video-label {{
      padding: .55rem .85rem; font-size: .78rem; font-weight: 600;
      background: #1e293b; color: #e2e8f0; border-bottom: 1px solid #334155;
    }}
    .week-video video {{
      width: 100%; display: block; max-height: 360px; background: #000;
    }}

    .simple-box {{
      background: var(--amber-soft); border: 1px solid var(--amber-border);
      border-radius: 10px; padding: 1rem 1.15rem; margin: .85rem 0 1rem;
    }}
    .simple-box h3 {{
      font-size: .88rem; font-weight: 700; color: var(--amber-text); margin-bottom: .55rem;
    }}
    .simple-box ul {{ margin: 0 0 0 1.15rem; font-size: .88rem; color: #78350f; }}
    .simple-box li {{ margin: .3rem 0; }}

    .panel {{
      border: 1px solid var(--line); border-radius: 10px; margin: .65rem 0;
      background: #fafbfc; overflow: hidden;
    }}
    .panel summary {{
      padding: .85rem 1rem; cursor: pointer; font-weight: 600; font-size: .92rem;
      list-style: none; display: flex; align-items: center; justify-content: space-between;
      user-select: none;
    }}
    .panel summary::-webkit-details-marker {{ display: none; }}
    .panel summary::after {{ content: '+'; font-size: 1.1rem; color: var(--text-soft); font-weight: 400; }}
    .panel[open] summary {{ border-bottom: 1px solid var(--line); background: white; }}
    .panel[open] summary::after {{ content: '\\2212'; }}
    .panel-inner {{ padding: .85rem 1rem 1rem; background: white; }}

    .panel-inner h3, .panel-inner h4 {{ display: none; }}
    .panel-inner p {{ margin: .5rem 0; color: var(--text-soft); font-size: .9rem; }}
    .panel-inner ul, .panel-inner ol {{ margin: .5rem 0 .5rem 1.25rem; color: var(--text-soft); font-size: .9rem; }}
    .panel-inner li {{ margin: .25rem 0; }}
    .panel-inner li::marker {{ color: var(--accent); }}
    .panel-inner strong {{ color: var(--text); }}

    .panel-inner table {{
      width: 100%; border-collapse: collapse; font-size: .82rem;
      margin: .65rem 0; border: 1px solid var(--line); border-radius: 8px; overflow: hidden;
    }}
    .panel-inner th {{
      background: #f1f5f9; padding: .55rem .7rem; text-align: left;
      font-weight: 600; color: var(--text); font-size: .78rem;
    }}
    .panel-inner td {{ padding: .5rem .7rem; border-top: 1px solid var(--line); color: var(--text-soft); vertical-align: top; }}
    .panel-inner tr:nth-child(even) td {{ background: #fafbfc; }}

    .code-block {{
      background: var(--code-bg); border: 1px solid var(--line); border-radius: 8px;
      margin: .65rem 0; overflow: hidden;
    }}
    .code-label {{
      font-size: .68rem; font-weight: 600; text-transform: uppercase; letter-spacing: .06em;
      color: var(--text-soft); padding: .4rem .75rem; background: #eef1f5; border-bottom: 1px solid var(--line);
    }}
    .panel-inner pre {{
      margin: 0; padding: .75rem .85rem; overflow-x: auto; background: transparent; border: none;
    }}
    .panel-inner pre code {{
      font-family: 'IBM Plex Mono', monospace; font-size: .78rem; line-height: 1.55;
      color: #334155; background: none; border: none; padding: 0;
    }}
    .panel-inner code {{
      font-family: 'IBM Plex Mono', monospace; font-size: .8em;
      background: #eef1f5; padding: .1em .35em; border-radius: 4px; color: #be123c;
    }}

    .special-block {{
      background: var(--paper); border: 1px solid var(--line); border-radius: var(--radius);
      margin-bottom: 1.5rem; box-shadow: var(--shadow); overflow: hidden; scroll-margin-top: 1rem;
    }}
    .special-head {{ padding: 1.1rem 1.5rem; border-bottom: 1px solid var(--line); background: #fafbfc; }}
    .special-head h2 {{ font-size: 1.1rem; font-weight: 700; border: none; margin: 0; padding: 0; }}
    .special-body {{ padding: .5rem 1.5rem 1.25rem; }}
    .special-body h3 {{ font-size: .95rem; font-weight: 700; margin: 1rem 0 .55rem; color: var(--text); }}
    .special-body p {{ margin: .5rem 0; color: var(--text-soft); font-size: .9rem; }}
    .special-body table {{
      width: 100%; border-collapse: collapse; font-size: .82rem;
      margin: .65rem 0 1rem; border: 1px solid var(--line); border-radius: 8px; overflow: hidden;
    }}
    .special-body th {{
      background: #f1f5f9; padding: .55rem .7rem; text-align: left;
      font-weight: 600; color: var(--text); font-size: .78rem;
    }}
    .special-body td {{ padding: .5rem .7rem; border-top: 1px solid var(--line); color: var(--text-soft); vertical-align: top; }}
    .special-body tr:nth-child(even) td {{ background: #fafbfc; }}
    .special-body strong {{ color: var(--text); }}

    .archive-toolbar {{
      display: flex; flex-wrap: wrap; gap: .6rem; align-items: center; margin-top: 1rem;
    }}
    .archive-search {{
      flex: 1; min-width: 200px; padding: .55rem .85rem; border-radius: 8px;
      border: 1px solid var(--line); font-family: inherit; font-size: .86rem;
    }}
    .archive-search:focus {{ outline: none; border-color: var(--accent-border); box-shadow: 0 0 0 3px var(--accent-soft); }}

    .callout {{
      border-radius: 8px; padding: .75rem 1rem; margin: .65rem 0; font-size: .86rem;
    }}
    .callout-exam {{ background: var(--amber-soft); border: 1px solid var(--amber-border); color: #78350f; }}
    .callout-tip {{ background: var(--green-soft); border: 1px solid var(--green-border); color: #14532d; }}
    .callout-web {{ background: var(--blue-soft); border: 1px solid var(--blue-border); color: #1e3a5f; }}

    .enrich-toolbar {{ display: flex; flex-wrap: wrap; gap: .5rem; margin: .75rem 0 1rem; }}
    .enrich-tab {{
      padding: .35rem .7rem; border-radius: 999px; font-size: .78rem; font-weight: 600;
      border: 1px solid var(--line); background: white; color: var(--text-soft);
      cursor: pointer; font-family: inherit;
    }}
    .enrich-tab.active {{ background: var(--blue-soft); border-color: var(--blue-border); color: var(--blue-text); }}
    .enrich-grid {{ display: grid; gap: .65rem; }}
    .enrich-card {{
      border: 1px solid var(--blue-border); border-radius: 10px; background: white; overflow: hidden;
    }}
    .enrich-card.hidden {{ display: none; }}
    .enrich-card-head {{
      padding: .85rem 1rem; cursor: pointer; display: flex; align-items: center; gap: .6rem;
      background: linear-gradient(180deg, #fff 0%, var(--blue-soft) 100%);
    }}
    .enrich-card-head h3 {{ font-size: .92rem; font-weight: 700; margin: 0; flex: 1; color: var(--text); }}
    .enrich-week-badge {{
      font-size: .68rem; font-weight: 700; padding: .2rem .5rem; border-radius: 6px;
      background: var(--blue-text); color: white; flex-shrink: 0;
    }}
    .enrich-card-body {{ display: none; padding: .85rem 1rem 1rem; border-top: 1px solid var(--line); }}
    .enrich-card.open .enrich-card-body {{ display: block; }}
    .enrich-card-body p {{ font-size: .88rem; color: var(--text-soft); margin: .45rem 0; line-height: 1.55; }}
    .enrich-exam {{
      margin-top: .65rem; padding: .6rem .75rem; background: var(--amber-soft);
      border: 1px solid var(--amber-border); border-radius: 8px; font-size: .82rem; color: #78350f;
    }}
    .enrich-sources {{ margin-top: .65rem; display: flex; flex-wrap: wrap; gap: .4rem; }}
    .enrich-sources a {{
      font-size: .76rem; padding: .3rem .55rem; border-radius: 6px;
      background: var(--blue-soft); color: var(--blue-text); text-decoration: none; border: 1px solid var(--blue-border);
    }}
    .enrich-sources a:hover {{ background: #dbeafe; }}

    .panel-enrich {{
      margin: .5rem 0 .75rem; border-left: 3px solid var(--blue-text);
      background: var(--blue-soft); border-radius: 0 8px 8px 0; padding: .75rem .9rem;
    }}
    .panel-enrich-label {{
      font-size: .72rem; font-weight: 700; text-transform: uppercase; letter-spacing: .05em;
      color: var(--blue-text); margin-bottom: .4rem;
    }}
    .panel-enrich p {{ font-size: .84rem; color: #1e3a5f; margin: .35rem 0; }}
    .panel-enrich .enrich-sources {{ margin-top: .45rem; }}
    .panel-enrich pre {{
      margin: .5rem 0 0; padding: .6rem .7rem; background: white; border-radius: 6px;
      border: 1px solid var(--blue-border); overflow-x: auto; font-size: .76rem;
    }}

    .ruby-faq-box {{
      margin: .65rem 0 0; padding: .75rem .9rem; border-radius: 8px;
      border: 1px solid #fca5a5; background: linear-gradient(180deg, #fff5f5 0%, #fff 100%);
    }}
    .ruby-faq-label {{
      font-size: .7rem; font-weight: 700; text-transform: uppercase; letter-spacing: .04em;
      color: #991b1b; margin-bottom: .45rem;
    }}
    .ruby-faq-q {{ font-size: .86rem; color: #7f1d1d; margin: .25rem 0 .35rem; }}
    .ruby-faq-a {{ font-size: .84rem; color: #450a0a; line-height: 1.55; margin: 0 0 .5rem; }}
    .ruby-faq-link {{
      font-size: .78rem; font-weight: 600; color: #b91c1c; text-decoration: none;
    }}
    .ruby-faq-link:hover {{ text-decoration: underline; }}
    .panel-enrich .ruby-faq-box {{ margin-top: .55rem; }}

    .solid-class-example {{
      margin-top: 1rem; padding: .85rem 1rem; border-radius: 8px;
      border: 1px dashed #c4b5fd; background: #faf5ff;
    }}
    .solid-class-example .solid-row-label {{ color: #6d28d9; }}
    .solid-example-meta {{
      font-size: .78rem; color: #6b7280; margin: .2rem 0 .65rem;
    }}
    .solid-example-meta code {{
      font-size: .74rem; background: #ede9fe; padding: .1rem .35rem; border-radius: 4px;
    }}

    .solid-header {{
      border: 2px dashed var(--line); border-radius: var(--radius); padding: 1.25rem 1.5rem;
      margin-bottom: 1.25rem; background: #fafbfc;
    }}
    .solid-header h3 {{ font-size: 1.1rem; margin-bottom: .75rem; }}
    .solid-header .field {{ font-size: .9rem; margin: .45rem 0; color: var(--text-soft); border-bottom: 1px dotted #cbd5e1; padding-bottom: .25rem; }}
    .solid-principle {{
      border: 1px solid var(--line); border-radius: var(--radius); margin-bottom: 1.25rem;
      overflow: hidden; background: white; box-shadow: var(--shadow);
    }}
    .solid-principle-head {{
      padding: 1rem 1.25rem; background: linear-gradient(180deg, #fff 0%, #fafbfc 100%);
      border-bottom: 1px solid var(--line); display: flex; align-items: center; gap: .75rem;
    }}
    .solid-letter {{
      width: 2.5rem; height: 2.5rem; border-radius: 10px; background: var(--accent); color: white;
      display: flex; align-items: center; justify-content: center; font-weight: 800; font-size: 1.1rem; flex-shrink: 0;
    }}
    .solid-principle-head h3 {{ font-size: 1rem; margin: 0; }}
    .solid-principle-head span {{ font-size: .78rem; color: var(--text-soft); display: block; margin-top: .15rem; }}
    .solid-body {{ padding: 1rem 1.25rem 1.25rem; }}
    .solid-row {{ margin-bottom: .85rem; }}
    .solid-row-label {{
      font-size: .72rem; font-weight: 700; text-transform: uppercase; letter-spacing: .05em;
      color: var(--accent); margin-bottom: .3rem;
    }}
    .solid-row p {{ font-size: .88rem; color: var(--text-soft); line-height: 1.55; margin: 0; }}
    .solid-code-grid {{ display: grid; gap: .75rem; margin-top: .75rem; }}
    @media (min-width: 768px) {{ .solid-code-grid {{ grid-template-columns: 1fr 1fr; }} }}
    .solid-code-box {{ border-radius: 8px; overflow: hidden; border: 1px solid var(--line); }}
    .solid-code-box.bad {{ border-color: #fecaca; }}
    .solid-code-box.good {{ border-color: #bbf7d0; }}
    .solid-code-box-head {{
      padding: .45rem .75rem; font-size: .72rem; font-weight: 700; text-transform: uppercase;
    }}
    .solid-code-box.bad .solid-code-box-head {{ background: var(--accent-soft); color: var(--accent); }}
    .solid-code-box.good .solid-code-box-head {{ background: var(--green-soft); color: var(--green-text); }}
    .solid-code-box pre {{
      margin: 0; padding: .65rem .75rem; font-size: .74rem; line-height: 1.5;
      background: var(--code-bg); overflow-x: auto;
    }}
    .solid-why {{ padding: .55rem .75rem; font-size: .82rem; line-height: 1.5; border-top: 1px solid var(--line); }}
    .solid-code-box.bad .solid-why {{ background: #fff5f5; color: #991b1b; }}
    .solid-code-box.good .solid-why {{ background: #f0fdf4; color: #14532d; }}

    .lsp-hero {{
      background: linear-gradient(135deg, #1e3a5f 0%, #312e81 50%, #4c1d95 100%);
      color: white; border-radius: var(--radius); padding: 1.35rem 1.5rem; margin-bottom: 1rem;
    }}
    .lsp-hero h3 {{ font-size: 1.15rem; margin-bottom: .35rem; }}
    .lsp-hero p {{ font-size: .88rem; opacity: .92; line-height: 1.55; }}
    .lsp-rules {{ display: grid; gap: .65rem; margin-top: 1rem; }}
    .lsp-rule {{
      border: 1px solid var(--line); border-radius: 8px; padding: .85rem 1rem; background: #fafbfc;
    }}
    .lsp-rule-num {{
      display: inline-flex; width: 1.5rem; height: 1.5rem; border-radius: 6px;
      background: #312e81; color: white; align-items: center; justify-content: center;
      font-size: .72rem; font-weight: 700; margin-right: .4rem;
    }}
    .lsp-rule h4 {{ font-size: .88rem; display: inline; }}
    .lsp-rule p {{ font-size: .84rem; color: var(--text-soft); margin: .4rem 0 0 1.9rem; line-height: 1.5; }}
    .lsp-credit {{ font-size: .78rem; color: var(--text-soft); margin-top: 1rem; font-style: italic; }}
    .solid-extra-link {{
      display: inline-block; margin-top: .75rem; font-size: .82rem; font-weight: 600;
      color: #312e81; text-decoration: none; padding: .4rem .75rem;
      background: #ede9fe; border-radius: 8px; border: 1px solid #c4b5fd;
    }}
    .solid-extra-link:hover {{ background: #ddd6fe; }}

    .course-banner {{
      border-radius: var(--radius); padding: 1.25rem 1.35rem; margin-bottom: 1.25rem;
      color: white; box-shadow: var(--shadow-lg);
      display: flex; gap: 1rem; align-items: flex-start;
    }}
    .course-banner-icon .course-icon-svg {{ width: 56px; height: 56px; filter: drop-shadow(0 2px 4px rgba(0,0,0,.2)); }}
    .course-banner-text {{ flex: 1; min-width: 0; }}
    .course-banner-intprog {{ background: linear-gradient(135deg, #991b1b, #dc2626); }}
    .course-banner-oop {{ background: linear-gradient(135deg, #5b21b6, #7c3aed); }}
    .course-banner h2 {{ font-size: 1.35rem; margin-bottom: .35rem; }}
    .course-banner p {{ font-size: .88rem; opacity: .92; max-width: 620px; }}
    .course-banner-actions {{ display: flex; flex-wrap: wrap; gap: .5rem; margin-top: .85rem; }}
    .course-banner .btn {{ background: rgba(255,255,255,.15); color: white; border-color: rgba(255,255,255,.35); }}
    .course-banner .btn:hover {{ background: rgba(255,255,255,.25); }}

    .nav-oop .w-num {{ background: var(--oop-soft); color: var(--oop-text); }}

    .oop-panel .panel {{ border-color: var(--oop-border); }}
    .oop-panel .panel[open] summary {{ background: var(--oop-soft); }}
    .week-block.oop-week .week-badge {{ background: var(--oop-accent); }}
    .week-block.oop-week {{ border-color: var(--oop-border); }}
    .week-block.oop-week .week-summary {{ background: var(--oop-soft); border-color: var(--oop-border); color: #4c1d95; }}
    .week-block.oop-week .chip {{ background: var(--oop-soft); color: var(--oop-text); border-color: var(--oop-border); }}

    .quiz-toolbar {{
      display: flex; flex-wrap: wrap; gap: .5rem; align-items: center;
      margin: .75rem 0 1rem;
    }}
    .quiz-tabs {{ display: flex; flex-wrap: wrap; gap: .35rem; flex: 1; }}
    .quiz-tab {{
      padding: .35rem .7rem; border-radius: 999px; font-size: .78rem; font-weight: 600;
      border: 1px solid var(--line); background: white; color: var(--text-soft);
      cursor: pointer; font-family: inherit;
    }}
    .quiz-tab:hover {{ border-color: #cbd5e1; color: var(--text); }}
    .quiz-tab.active {{
      background: var(--accent-soft); border-color: var(--accent-border);
      color: var(--accent);
    }}
    .quiz-actions {{ display: flex; gap: .4rem; flex-wrap: wrap; }}
    .quiz-actions .btn {{ font-size: .78rem; padding: .4rem .75rem; }}

    .quiz-grid {{ display: grid; gap: .55rem; }}
    .quiz-card {{
      border: 1px solid var(--line); border-radius: 8px; padding: .75rem .9rem;
      background: #fafbfc;
    }}
    .quiz-card.hidden {{ display: none; }}
    .quiz-q {{ font-weight: 500; font-size: .88rem; margin-bottom: .55rem; line-height: 1.5; }}
    .quiz-q .q-n {{
      display: inline-flex; align-items: center; justify-content: center;
      min-width: 1.4rem; height: 1.4rem; border-radius: 6px;
      background: var(--accent-soft); color: var(--accent);
      font-size: .72rem; font-weight: 700; margin-right: .4rem;
    }}
    .quiz-btn {{
      font-size: .78rem; font-weight: 600; padding: .35rem .7rem;
      border-radius: 6px; border: 1px solid var(--line); background: white;
      color: var(--text); cursor: pointer; font-family: inherit;
    }}
    .quiz-btn:hover {{ border-color: var(--accent-border); background: var(--accent-soft); }}
    .quiz-a {{
      display: none; margin-top: .6rem; padding-top: .6rem;
      border-top: 1px dashed var(--line); font-size: .84rem;
      color: var(--green-text); line-height: 1.55;
    }}
    .quiz-a.visible {{ display: block; }}

    .site-nav-brand .mobile-toggle {{
      display: none; flex-shrink: 0;
      background: var(--accent); color: white; border: none; border-radius: 8px;
      width: 40px; height: 40px; font-size: 1.1rem; cursor: pointer;
    }}

    .mobile-toggle {{
      display: none;
    }}

    /* 7-day plan */
    .plan-hero {{
      background: linear-gradient(135deg, #991b1b 0%, #b91c1c 50%, #dc2626 100%);
      color: white; border-radius: var(--radius); padding: 1.5rem 1.75rem;
      margin-bottom: 1.5rem; box-shadow: var(--shadow-lg);
    }}
    .plan-hero h2 {{ font-size: 1.35rem; font-weight: 700; margin-bottom: .4rem; }}
    .plan-hero p {{ opacity: .92; font-size: .9rem; max-width: 560px; }}
    .plan-progress {{
      margin-top: 1rem; background: rgba(255,255,255,.2); border-radius: 999px; height: 8px; overflow: hidden;
    }}
    .plan-progress-bar {{ height: 100%; background: white; border-radius: 999px; width: 0%; transition: width .3s; }}
    .plan-progress-text {{ font-size: .78rem; margin-top: .45rem; opacity: .9; }}

    .plan-day {{
      border: 1px solid var(--line); border-radius: var(--radius); margin-bottom: .85rem;
      background: var(--paper); overflow: hidden; box-shadow: var(--shadow);
    }}
    .plan-day-head {{
      padding: 1rem 1.15rem; cursor: pointer; display: flex; align-items: flex-start; gap: .85rem;
      background: #fafbfc; border-bottom: 1px solid transparent;
    }}
    .plan-day.open .plan-day-head {{ border-bottom-color: var(--line); }}
    .plan-day-num {{
      width: 2.2rem; height: 2.2rem; border-radius: 10px; background: var(--accent); color: white;
      display: flex; align-items: center; justify-content: center; font-weight: 700; font-size: .95rem; flex-shrink: 0;
    }}
    .plan-day.done .plan-day-num {{ background: var(--green-text); }}
    .plan-day-title {{ font-weight: 700; font-size: .95rem; }}
    .plan-day-meta {{ font-size: .78rem; color: var(--text-soft); margin-top: .2rem; }}
    .plan-day-goal {{ font-size: .84rem; color: var(--text-soft); margin-top: .35rem; }}
    .plan-day-toggle {{ margin-left: auto; color: var(--text-soft); font-size: 1.1rem; flex-shrink: 0; }}

    .plan-day-body {{ display: none; padding: 1rem 1.15rem 1.15rem; }}
    .plan-day.open .plan-day-body {{ display: block; }}
    .plan-tasks {{ list-style: none; margin: 0; padding: 0; }}
    .plan-tasks li {{
      display: flex; align-items: flex-start; gap: .6rem; padding: .55rem 0;
      border-bottom: 1px solid var(--line); font-size: .88rem;
    }}
    .plan-tasks li:last-child {{ border-bottom: none; }}
    .plan-tasks input[type=checkbox] {{ margin-top: .25rem; width: 16px; height: 16px; accent-color: var(--accent); cursor: pointer; flex-shrink: 0; }}
    .plan-tasks label {{ cursor: pointer; flex: 1; }}
    .plan-tasks label.done {{ text-decoration: line-through; color: var(--text-soft); opacity: .7; }}
    .plan-tasks a {{ color: var(--blue-text); text-decoration: none; font-size: .78rem; display: block; margin-top: .2rem; }}
    .plan-tasks a:hover {{ text-decoration: underline; }}
    .plan-remember {{
      margin-top: .85rem; padding: .75rem .9rem; background: var(--amber-soft);
      border: 1px solid var(--amber-border); border-radius: 8px; font-size: .82rem;
    }}
    .plan-remember strong {{ color: var(--amber-text); display: block; margin-bottom: .35rem; }}
    .plan-remember ul {{ margin: 0 0 0 1rem; color: #78350f; }}

    .must-know-grid {{ display: grid; gap: .5rem; }}
    .must-know-item {{
      display: grid; grid-template-columns: 1fr 1.2fr; gap: .75rem;
      padding: .65rem .85rem; background: #fafbfc; border: 1px solid var(--line); border-radius: 8px; font-size: .84rem;
    }}
    .must-know-item strong {{ color: var(--accent); }}
    .must-know-item span {{ color: var(--text-soft); }}
    @media (max-width: 600px) {{ .must-know-item {{ grid-template-columns: 1fr; }} }}

    @media (max-width: 1100px) {{
      :root {{ --nav-strip-h: min(32vh, 260px); }}
      .site-nav-dual {{ grid-template-columns: 1fr; max-height: none; }}
      .nav-col-intprog {{ border-right: none; border-bottom: 2px solid var(--accent-border); max-height: 28vh; }}
      .nav-col-oop {{ max-height: 28vh; }}
      .course-picker {{ grid-template-columns: 1fr; }}
      .courses-split {{ grid-template-columns: 1fr; }}
      .course-pane {{ height: auto; min-height: 45vh; border-right: none; border-bottom: 1px solid var(--pane-divider); }}
      .main {{ overflow: visible; }}
      .layout {{ height: auto; overflow: visible; }}
    }}

    @media (max-width: 768px) {{
      .site-nav {{ position: relative; }}
      .site-nav-dual {{ display: none; }}
      .site-nav.nav-open .site-nav-dual {{ display: grid; }}
      .site-nav-brand .mobile-toggle {{ display: flex; align-items: center; justify-content: center; }}
      .quiz-toolbar {{ flex-direction: column; align-items: stretch; }}
    }}

    @media print {{
      .site-nav, .mobile-toggle, .topbar-actions, .quiz-toolbar, .quiz-btn, .term-tip-btn {{ display: none !important; }}
      .main {{ max-width: 100%; padding: .5rem; height: auto; overflow: visible; }}
      .layout {{ height: auto; }}
      .courses-split {{ grid-template-columns: 1fr; height: auto; }}
      .course-pane {{ height: auto; overflow: visible; page-break-before: auto; }}
      .week-block, .special-block {{ break-inside: avoid; box-shadow: none; }}
      .panel {{ break-inside: avoid; }}
      .panel[open] summary {{ border-bottom: 1px solid #ddd; }}
      .quiz-a {{ display: block !important; }}
      .quiz-card.hidden {{ display: block !important; }}
    }}
  </style>
</head>
<body>
  <div class="layout">
    <header class="site-nav" id="siteNav">
      <div class="site-nav-brand">
        <div class="brand">
          <div class="brand-kicker">Sinav Calisma Merkezi</div>
          <h1>Internet Prog II + Nesne Yonelimli Prog</h1>
          <p>Ustte iki ders menusu — altta yan yana icerik</p>
        </div>
        <button class="mobile-toggle" id="menuBtn" aria-label="Menu">&#9776;</button>
      </div>
      <div class="site-nav-dual">
        <nav class="nav-col nav-col-intprog nav-intprog" aria-label="Internet Programciligi II">
          <div class="nav-col-title nav-col-title-intprog">{ruby_icon_sm} Internet Programciligi II</div>
          {toc_intprog}
        </nav>
        <nav class="nav-col nav-col-oop nav-oop" aria-label="Nesne Yonelimli Programlama">
          <div class="nav-col-title nav-col-title-oop">{python_icon_sm} Nesne Yonelimli Programlama</div>
          {toc_oop}
        </nav>
      </div>
    </header>
    <main class="main">
      {course_picker}
      <div class="courses-split">
        <div class="course-pane course-pane-intprog" id="pane-intprog">
          {content_intprog}
        </div>
        <div class="course-pane course-pane-oop" id="pane-oop">
          {content_oop}
        </div>
      </div>
    </main>
  </div>
  <script>
    function scrollPaneToId(pane, id) {{
      const el = document.getElementById(id);
      if (!el || !pane) return;
      const top = el.getBoundingClientRect().top - pane.getBoundingClientRect().top + pane.scrollTop - 12;
      pane.scrollTo({{ top: Math.max(0, top), behavior: 'smooth' }});
    }}

    document.querySelectorAll('.site-nav a[href^="#"], .course-picker a[href^="#"]').forEach(a => {{
      a.addEventListener('click', e => {{
        const id = a.getAttribute('href').slice(1);
        const el = document.getElementById(id);
        if (!el) return;
        const pane = el.closest('.course-pane');
        if (pane) {{
          e.preventDefault();
          scrollPaneToId(pane, id);
          document.getElementById('siteNav').classList.remove('nav-open');
        }}
      }});
    }});

    function setupPaneSpy(paneId, navSelector) {{
      const pane = document.getElementById(paneId);
      if (!pane) return;
      const links = document.querySelectorAll(navSelector + ' a[href^="#"]');
      const sections = [...pane.querySelectorAll('.week-block, .special-block, .plan-hero, .course-banner')];
      pane.addEventListener('scroll', () => {{
        const paneTop = pane.getBoundingClientRect().top;
        let cur = '';
        sections.forEach(s => {{
          const rect = s.getBoundingClientRect();
          if (rect.top - paneTop <= 90) cur = s.id;
        }});
        links.forEach(a => a.classList.toggle('active', a.getAttribute('href') === '#' + cur));
      }}, {{ passive: true }});
    }}
    setupPaneSpy('pane-intprog', '.nav-intprog');
    setupPaneSpy('pane-oop', '.nav-oop');

    document.getElementById('menuBtn').onclick = () => document.getElementById('siteNav').classList.toggle('nav-open');

    document.querySelectorAll('.term-tip-btn').forEach(btn => {{
      btn.addEventListener('click', e => {{
        e.stopPropagation();
        const pop = btn.nextElementSibling;
        const wasOpen = pop.classList.contains('open');
        document.querySelectorAll('.term-tip-pop.open').forEach(p => p.classList.remove('open'));
        if (!wasOpen) pop.classList.add('open');
      }});
    }});
    document.addEventListener('click', () => {{
      document.querySelectorAll('.term-tip-pop.open').forEach(p => p.classList.remove('open'));
    }});
    document.querySelectorAll('.term-tip-pop').forEach(pop => {{
      pop.addEventListener('click', e => e.stopPropagation());
    }});

    document.querySelectorAll('.course-pane .week-block').forEach(week => {{
      const first = week.querySelector('.panel');
      if (first) first.open = true;
    }});

    function filterPanelsInPane(pane, q) {{
      if (!pane) return;
      pane.querySelectorAll('.week-block').forEach(week => {{
        let any = !q;
        week.querySelectorAll('.panel').forEach(panel => {{
          const match = !q || panel.textContent.toLowerCase().includes(q);
          panel.style.display = match ? '' : 'none';
          if (match) any = true;
        }});
        week.style.display = any ? '' : 'none';
      }});
      if (pane.id === 'pane-intprog') {{
        pane.querySelectorAll('.enrich-card').forEach(card => {{
          if (!q) {{ card.classList.remove('hidden'); return; }}
          card.classList.toggle('hidden', !card.textContent.toLowerCase().includes(q));
        }});
      }}
      if (pane.id === 'pane-oop') {{
        pane.querySelectorAll('.panel').forEach(panel => {{
          if (!q) {{ panel.style.display = ''; return; }}
          panel.style.display = panel.textContent.toLowerCase().includes(q) ? '' : 'none';
        }});
      }}
    }}

    document.getElementById('expandAll')?.addEventListener('click', () => {{
      document.querySelectorAll('#pane-intprog .week-block .panel').forEach(p => {{ p.open = true; }});
    }});
    document.getElementById('collapseAll')?.addEventListener('click', () => {{
      document.querySelectorAll('#pane-intprog .week-block .panel').forEach(p => {{ p.open = false; }});
    }});
    document.getElementById('panelSearch')?.addEventListener('input', e => {{
      filterPanelsInPane(document.getElementById('pane-intprog'), e.target.value.trim().toLowerCase());
    }});
    document.getElementById('oopPanelSearch')?.addEventListener('input', e => {{
      filterPanelsInPane(document.getElementById('pane-oop'), e.target.value.trim().toLowerCase());
    }});

    document.querySelectorAll('.enrich-tab').forEach(tab => {{
      tab.addEventListener('click', () => {{
        const week = tab.dataset.week;
        document.querySelectorAll('.enrich-tab').forEach(t => t.classList.toggle('active', t === tab));
        document.querySelectorAll('.enrich-card').forEach(card => {{
          if (week === 'all') card.classList.remove('hidden');
          else card.classList.toggle('hidden', card.dataset.week !== week);
        }});
      }});
    }});
    document.querySelectorAll('.enrich-card-head').forEach(head => {{
      head.addEventListener('click', () => head.closest('.enrich-card').classList.toggle('open'));
    }});

    function setQuizAnswer(card, show) {{
      const ans = card.querySelector('.quiz-a');
      const btn = card.querySelector('.quiz-btn');
      if (!ans || !btn) return;
      ans.classList.toggle('visible', show);
      btn.textContent = show ? 'Cevabi Gizle' : 'Cevabi Goster';
    }}

    document.querySelectorAll('.quiz-btn').forEach(btn => {{
      btn.addEventListener('click', () => {{
        const card = btn.closest('.quiz-card');
        const ans = card.querySelector('.quiz-a');
        setQuizAnswer(card, !ans.classList.contains('visible'));
      }});
    }});

    document.getElementById('quizShowAll')?.addEventListener('click', () => {{
      document.querySelectorAll('.quiz-card:not(.hidden)').forEach(card => setQuizAnswer(card, true));
    }});

    document.getElementById('quizHideAll')?.addEventListener('click', () => {{
      document.querySelectorAll('.quiz-card').forEach(card => setQuizAnswer(card, false));
    }});

    document.querySelectorAll('.quiz-tab').forEach(tab => {{
      tab.addEventListener('click', () => {{
        const week = tab.dataset.week;
        document.querySelectorAll('.quiz-tab').forEach(t => t.classList.toggle('active', t === tab));
        document.querySelectorAll('.quiz-card').forEach(card => {{
          if (week === 'all') card.classList.remove('hidden');
          else card.classList.toggle('hidden', card.dataset.week !== week);
        }});
      }});
    }});

    // 7-day plan checkboxes
    const PLAN_KEY = 'intprog2-plan-v1';
    function loadPlan() {{
      try {{ return JSON.parse(localStorage.getItem(PLAN_KEY) || '{{}}'); }} catch(e) {{ return {{}}; }}
    }}
    function savePlan(data) {{ localStorage.setItem(PLAN_KEY, JSON.stringify(data)); }}
    function updateProgress() {{
      const boxes = document.querySelectorAll('.plan-tasks input[type=checkbox]');
      const done = [...boxes].filter(b => b.checked).length;
      const total = boxes.length;
      const pct = total ? Math.round(done / total * 100) : 0;
      const bar = document.getElementById('planProgressBar');
      const txt = document.getElementById('planProgressText');
      if (bar) bar.style.width = pct + '%';
      if (txt) txt.textContent = done + ' / ' + total + ' gorev tamamlandi (' + pct + '%)';
      document.querySelectorAll('.plan-day').forEach(day => {{
        const dboxes = day.querySelectorAll('.plan-tasks input[type=checkbox]');
        const ddone = [...dboxes].filter(b => b.checked).length;
        day.classList.toggle('done', dboxes.length > 0 && ddone === dboxes.length);
      }});
    }}
    const saved = loadPlan();
    document.querySelectorAll('.plan-tasks input[type=checkbox]').forEach(box => {{
      const id = box.dataset.taskId;
      if (saved[id]) box.checked = true;
      const label = box.closest('li')?.querySelector('label');
      if (label && box.checked) label.classList.add('done');
      box.addEventListener('change', () => {{
        saved[id] = box.checked;
        savePlan(saved);
        if (label) label.classList.toggle('done', box.checked);
        updateProgress();
      }});
    }});
    document.querySelectorAll('.plan-day-head').forEach(head => {{
      head.addEventListener('click', e => {{
        if (e.target.tagName === 'INPUT' || e.target.tagName === 'A' || e.target.tagName === 'LABEL') return;
        head.closest('.plan-day').classList.toggle('open');
      }});
    }});
    document.getElementById('openToday')?.addEventListener('click', () => {{
      document.querySelectorAll('.plan-day').forEach(d => d.classList.remove('open'));
      const first = document.querySelector('.plan-day:not(.done)');
      if (first) {{
        first.classList.add('open');
        const pane = document.getElementById('pane-intprog');
        if (pane && first.id) scrollPaneToId(pane, first.id);
        else first.scrollIntoView({{ behavior: 'smooth', block: 'start' }});
      }}
    }});
    updateProgress();
    document.querySelector('.plan-day')?.classList.add('open');
  </script>
</body>
</html>"""


def slugify(text: str) -> str:
    text = text.lower().strip()
    tr_map = {
        "ı": "i", "ğ": "g", "ü": "u", "ş": "s", "ö": "o", "ç": "c",
        "İ": "i", "Ğ": "g", "Ü": "u", "Ş": "s", "Ö": "o", "Ç": "c",
        "—": "-", "–": "-",
    }
    for src, dst in tr_map.items():
        text = text.replace(src, dst)
    text = re.sub(r"[^a-z0-9\s-]", "", text)
    return re.sub(r"[\s-]+", "-", text).strip("-")


def md_to_html_fragment(md: str) -> str:
    def md_slugify(value, separator="-"):
        return slugify(value)

    md_engine = markdown.Markdown(
        extensions=[
            TableExtension(),
            FencedCodeExtension(),
            TocExtension(slugify=md_slugify, permalink=False),
        ]
    )
    return md_engine.convert(md)


def split_sections(md_text: str):
    md_text = re.sub(r"^# .+\n\n", "", md_text)
    md_text = re.sub(r"(?:^> .+\n)+\n?", "", md_text, flags=re.MULTILINE)
    md_text = re.sub(r"## İçindekiler\n\n.*?(?=\n## )", "", md_text, flags=re.DOTALL)
    matches = list(re.finditer(r"^## (.+?)$", md_text, re.MULTILINE))
    sections = []
    for i, match in enumerate(matches):
        title = match.group(1).strip()
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(md_text)
        body = md_text[start:end].strip()
        body = re.sub(r"\n---+\s*$", "", body)
        sections.append((title, slugify(title), body))
    return sections


def split_h3_sections(body: str):
    chunks = re.split(r"\n### ", body)
    result = []
    for i, chunk in enumerate(chunks):
        if i == 0 and not chunk.strip():
            continue
        if i > 0:
            chunk = "### " + chunk
        m = re.match(r"### (.+?)\n", chunk)
        if m:
            result.append((m.group(1).strip(), chunk[m.end() :].strip()))
        elif chunk.strip():
            result.append(("Genel", chunk.strip()))
    return result


def inject_term_tips(fragment: str, glossary: dict) -> str:
    if not glossary or "<table" not in fragment:
        return fragment
    keys = sorted(glossary.keys(), key=len, reverse=True)

    def tip_markup(key: str) -> str:
        g = glossary[key]
        code = ""
        if g.get("code"):
            code = f'<pre class="term-tip-code">{html.escape(g["code"])}</pre>'
        return (
            f'<span class="term-tip">'
            f'<button type="button" class="term-tip-btn" aria-label="{html.escape(g["title"])} — nasil kullanilir?">i</button>'
            f'<span class="term-tip-pop" role="tooltip">'
            f'<strong>{html.escape(g["title"])}</strong>'
            f'<p><em>Ne?</em> {html.escape(g["what"])}</p>'
            f'<p><em>Nasil?</em> {html.escape(g["how"])}</p>'
            f"{code}"
            f"</span></span>"
        )

    def inject_in_text(text: str) -> str:
        result = text
        plain = re.sub(r"<[^>]+>", "", text)
        for key in keys:
            if key.lower() not in plain.lower():
                continue
            pattern = re.compile(re.escape(key), re.IGNORECASE)
            parts: list[str] = []
            last = 0
            changed = False
            for match in pattern.finditer(result):
                if "term-tip" in result[max(0, match.start() - 30) : match.end() + 30]:
                    parts.append(result[last : match.end()])
                    last = match.end()
                    continue
                parts.append(result[last : match.end()])
                parts.append(tip_markup(key))
                last = match.end()
                changed = True
            if changed:
                parts.append(result[last:])
                result = "".join(parts)
        return result

    def process_row(match: re.Match) -> str:
        row = match.group(0)
        if "<th>" in row:
            return row
        cell_pattern = re.compile(r"(<td>)(.*?)(</td>)", re.DOTALL)
        cells = list(cell_pattern.finditer(row))
        if not cells:
            return row
        out: list[str] = []
        pos = 0
        for i, cm in enumerate(cells):
            out.append(row[pos : cm.start()])
            content = cm.group(2)
            if i == 0 or i == len(cells) - 1:
                content = inject_in_text(content)
            out.append(cm.group(1) + content + cm.group(3))
            pos = cm.end()
        out.append(row[pos:])
        return "".join(out)

    return re.sub(r"<tr>.*?</tr>", process_row, fragment, flags=re.DOTALL)


def enhance_inner_html(fragment: str, glossary: dict | None = None) -> str:
    fragment = re.sub(
        r'<pre><code(?: class="language-(\w+)")?>(.*?)</code></pre>',
        lambda m: (
            f'<div class="code-block"><div class="code-label">{m.group(1) or "kod"}</div>'
            f"<pre><code>{m.group(2)}</code></pre></div>"
        ),
        fragment,
        flags=re.DOTALL,
    )
    fragment = re.sub(r"<hr\s*/?>", "", fragment)
    if glossary:
        fragment = inject_term_tips(fragment, glossary)
    return fragment


def panel_sort_key(title: str):
    t = title.lower()
    for tr_src, tr_dst in {"ı": "i", "ğ": "g", "ü": "u", "ş": "s", "ö": "o", "ç": "c"}.items():
        t = t.replace(tr_src, tr_dst)
    priority = 999
    for keyword, order in PANEL_PRIORITY.items():
        if keyword in t:
            priority = min(priority, order)
    return (priority, t)


def week_video_path(num: int) -> Path | None:
    path = BASE / "videos" / f"hafta-{num}.mp4"
    return path if path.exists() else None


def build_week_video_html(num: int) -> str:
    if not week_video_path(num):
        return ""
    return f"""
        <div class="week-video">
          <div class="week-video-label">Kisa Video Ozeti (~1 dk) — Hafta {num}</div>
          <video controls preload="metadata" playsinline poster="">
            <source src="videos/hafta-{num}.mp4" type="video/mp4">
            Tarayiciniz video oynatmayi desteklemiyor.
          </video>
        </div>
        """


def build_week_block(title: str, sid: str, body: str) -> str:
    meta = WEEK_META.get(sid, {})
    num = meta.get("num", "")
    tag = meta.get("tag", "")
    summary = meta.get("summary", "")
    focus = meta.get("focus", [])
    simple = meta.get("simple", [])

    chips = "".join(f'<span class="chip">{html.escape(f)}</span>' for f in focus)
    head = f"""
    <section class="week-block" id="{sid}">
      <div class="week-head">
        <div class="week-head-top">
          {"<span class='week-badge'>Hafta " + str(num) + "</span>" if num else ""}
          {"<span class='week-tag'>" + html.escape(tag) + "</span>" if tag else ""}
        </div>
        <h2>{html.escape(title)}</h2>
        {"<div class='week-summary'><strong>Bu haftada ne ogreniyorsun?</strong> " + html.escape(summary) + "</div>" if summary else ""}
        {"<div class='focus-chips'>" + chips + "</div>" if chips else ""}
      </div>
      <div class="week-body">
    """

    video_html = build_week_video_html(num) if num else ""

    week_enrich_html = ""
    if num:
        week_topics = topics_for_week(num)
        if week_topics:
            links = "".join(
                f'<a href="#enrich-{html.escape(t["id"])}">{html.escape(t["title"])}</a>'
                for t in week_topics
            )
            week_enrich_html = f"""
        <div class="callout callout-web" style="margin:.85rem 0 0">
          <strong>Bu hafta — Ruby resmi SSS + internet aciklamalari (Turkce):</strong>
          <div class="enrich-sources" style="margin-top:.45rem">{links}</div>
        </div>
        """

    simple_html = ""
    if simple:
        items = "".join(f"<li>{html.escape(s)}</li>" for s in simple)
        simple_html = f"""
        <div class="simple-box">
          <h3>Basit Anlatim</h3>
          <ul>{items}</ul>
        </div>
        """

    panels = []
    seen_enrich = set()
    h3_sections = sorted(split_h3_sections(body), key=lambda x: panel_sort_key(x[0]))
    for h3_title, h3_body in h3_sections:
        inner = enhance_inner_html(md_to_html_fragment(h3_body))
        enrich_html = ""
        if num:
            for topic in match_panel_topics(h3_title, num):
                if topic["id"] in seen_enrich:
                    continue
                seen_enrich.add(topic["id"])
                enrich_html += build_inline_enrichment_html(topic, compact=True)
        panels.append(f"""
        <details class="panel">
          <summary>{html.escape(h3_title)}</summary>
          <div class="panel-inner">{inner}{enrich_html}</div>
        </details>
        """)

    return head + video_html + week_enrich_html + simple_html + "".join(panels) + "</div></section>"


def build_oop_week_block(title: str, sid: str, body: str) -> str:
    meta = OOP_WEEK_META.get(sid, {})
    num = meta.get("num", "")
    tag = meta.get("tag", "")
    summary = meta.get("summary", "")
    simple = meta.get("simple", [])

    chips = "".join(f'<span class="chip">{html.escape(s)}</span>' for s in simple) if simple else ""
    head = f"""
    <section class="week-block oop-week" id="{sid}">
      <div class="week-head">
        <div class="week-head-top">
          {"<span class='week-badge'>Hafta " + str(num) + "</span>" if num else ""}
          {"<span class='week-tag'>" + html.escape(tag) + "</span>" if tag else ""}
        </div>
        <h2>{html.escape(title)}</h2>
        {"<div class='week-summary'><strong>Bu haftada ne ogreniyorsun?</strong> " + html.escape(summary) + "</div>" if summary else ""}
        {"<div class='focus-chips'>" + chips + "</div>" if chips else ""}
      </div>
      <div class="week-body">
    """

    simple_html = ""
    if simple:
        items = "".join(f"<li>{html.escape(s)}</li>" for s in simple)
        simple_html = f"""
        <div class="simple-box">
          <h3>Basit Anlatim</h3>
          <ul>{items}</ul>
        </div>
        """

    panels = []
    for h3_title, h3_body in split_h3_sections(body):
        inner = enhance_inner_html(md_to_html_fragment(h3_body))
        panels.append(f"""
        <details class="panel">
          <summary>{html.escape(h3_title)}</summary>
          <div class="panel-inner">{inner}</div>
        </details>
        """)

    return head + simple_html + "".join(panels) + "</div></section>"


def build_course_picker() -> str:
    return f"""
    <div class="course-picker" id="course-hub">
      <div class="course-picker-label">Ders sec — hangi derse calisacaksin?</div>
      <section class="course-hub">
        <a class="course-card intprog" href="#intprog-course">
          {RUBY_ICON_SVG}
          <div class="course-card-body">
            <div class="course-card-kicker">Ders 1 · Ruby</div>
            <h3>Internet Programciligi II</h3>
            <p>Rails, migration, Devise — Hafta 2-10, quiz ve 7 gunluk plan.</p>
          </div>
        </a>
        <a class="course-card oop" href="#oop-course">
          {PYTHON_ICON_SVG}
          <div class="course-card-body">
            <div class="course-card-kicker">Ders 2 · Python</div>
            <h3>Nesne Yonelimli Programlama</h3>
            <p>OOP, SOLID, kalitim — Hafta 1-10 PDF ve cozumlu alistirmalar.</p>
          </div>
        </a>
      </section>
    </div>
    """


def build_intprog_banner() -> str:
    return f"""
    <div class="course-banner course-banner-intprog" id="intprog-course">
      <div class="course-banner-icon">{RUBY_ICON_SVG}</div>
      <div class="course-banner-text">
      <h2>Internet Programciligi II</h2>
      <p>Ruby on Rails — Hafta 2-10 PDF arsivi, kapsulleme, migration, Devise. 7 gunluk sinav plani ve interaktif quiz.</p>
      <div class="course-banner-actions">
        <a class="btn" href="#7-gunluk-plan">7 Gunluk Plan</a>
        <a class="btn" href="#konu-indeksi">Konu Indeksi</a>
        <a class="btn" href="#internet-kaynaklari">Internet Kaynaklari</a>
        <a class="btn" href="#sinav-sorulari-kendini-test-et">Quiz</a>
        <button class="btn" onclick="window.print()">PDF Indir</button>
      </div>
      <div class="archive-toolbar" style="margin-top:.85rem">
        <input type="search" class="archive-search" id="panelSearch" placeholder="Int Prog ara: migration, devise, enum...">
        <button type="button" class="btn" id="expandAll">Panelleri ac</button>
        <button type="button" class="btn" id="collapseAll">Panelleri kapat</button>
      </div>
      </div>
    </div>
    """


def build_oop_banner() -> str:
    return f"""
    <div class="course-banner course-banner-oop" id="oop-course">
      <div class="course-banner-icon">{PYTHON_ICON_SVG}</div>
      <div class="course-banner-text">
      <h2>{html.escape(OOP_META['title'])}</h2>
      <p>NYP II — Hafta 1-9 PDF arsivi. Hafta 10: SOLID calismalari ve cozumlu alistirmalar.</p>
      <div class="course-banner-actions">
        <a class="btn" href="#oop-konu-indeksi">Konu Indeksi</a>
        <a class="btn" href="#hafta-10-solid-calisma-odev-cozumleri">Hafta 10 SOLID</a>
        <a class="btn" href="#oop-ezber">OOP Ezber</a>
      </div>
      <div class="archive-toolbar" style="margin-top:.85rem">
        <input type="search" class="archive-search" id="oopPanelSearch" placeholder="OOP ara: solid, kalitim, kapsulleme...">
      </div>
      </div>
    </div>
    """


def build_oop_must_know_section() -> str:
    items = "".join(
        f'<div class="must-know-item"><strong>{html.escape(k)}</strong><span>{html.escape(v)}</span></div>'
        for k, v in OOP_MUST_KNOW
    )
    return f"""
    <section class="special-block oop-must-know" id="oop-ezber">
      <div class="special-head"><h2>OOP Sinav Ezber Listesi</h2></div>
      <div class="special-body">
        <div class="callout callout-web">Nesne Yonelimli Programlama sinavindan once bu 9 maddeyi iki kez oku.</div>
        <div class="must-know-grid">{items}</div>
      </div>
    </section>
    """


def build_solid_class_example_html(letter: str) -> str:
    ex = CLASS_EXAMPLES_BY_LETTER.get(letter)
    if not ex:
        return ""
    extra = ""
    if ex.get("extra_link"):
        extra = f'<a class="solid-extra-link" href="{html.escape(ex["extra_link"])}">Detayli LSP ornegi ve 5 kural →</a>'
    return f"""
            <div class="solid-class-example" id="solid-ornek-{letter.lower()}">
              <div class="solid-row-label">Sinif arkadas ornegi (Python)</div>
              <p style="font-size:.9rem;font-weight:600;margin:.25rem 0">{html.escape(ex['title'])}</p>
              <p class="solid-example-meta">
                Tema: {html.escape(ex['theme'])} · Hazirlayan: {html.escape(ex['author'])} ·
                Dosya: <code>{html.escape(ex['filename'])}</code>
              </p>
              <div class="solid-code-grid">
                <div class="solid-code-box bad">
                  <div class="solid-code-box-head">Kotu kod</div>
                  <pre><code>{html.escape(ex['bad_code'])}</code></pre>
                  <div class="solid-why"><strong>Neden kotu?</strong> {html.escape(ex['bad_why'])}</div>
                </div>
                <div class="solid-code-box good">
                  <div class="solid-code-box-head">Iyi kod</div>
                  <pre><code>{html.escape(ex['good_code'])}</code></pre>
                  <div class="solid-why"><strong>Neden iyi?</strong> {html.escape(ex['good_why'])}</div>
                </div>
              </div>
              {extra}
            </div>
            """


def build_solid_principles_inner() -> str:
    fields = "".join(f'<div class="field">{html.escape(f)}</div>' for f in STUDENT_HEADER["fields"])
    principles = []
    for p in SOLID:
        principles.append(f"""
        <article class="solid-principle" id="solid-{p['letter'].lower()}">
          <div class="solid-principle-head">
            <div class="solid-letter">{html.escape(p['letter'])}</div>
            <div>
              <h3>{html.escape(p['name'])}</h3>
              <span>{html.escape(p['name_tr'])}</span>
            </div>
          </div>
          <div class="solid-body">
            <div class="solid-row">
              <div class="solid-row-label">Ilke tanimi</div>
              <p>{html.escape(p['definition'])}</p>
            </div>
            <div class="solid-row">
              <div class="solid-row-label">Amaci / cozmeye calistigi problem</div>
              <p>{html.escape(p['purpose'])}</p>
              <p style="margin-top:.35rem"><em>Problem:</em> {html.escape(p['problem'])}</p>
            </div>
            <div class="solid-code-grid">
              <div class="solid-code-box bad">
                <div class="solid-code-box-head">Ilkeye aykiri (kotu) kod</div>
                <pre><code>{html.escape(p['bad_code'])}</code></pre>
                <div class="solid-why"><strong>Neden kotu?</strong> {html.escape(p['bad_why'])}</div>
              </div>
              <div class="solid-code-box good">
                <div class="solid-code-box-head">Ilkeye uygun (iyi) kod</div>
                <pre><code>{html.escape(p['good_code'])}</code></pre>
                <div class="solid-why"><strong>Neden iyi?</strong> {html.escape(p['good_why'])}</div>
              </div>
            </div>
            {build_solid_class_example_html(p['letter'])}
            {f'<a class="solid-extra-link" href="#lsp-solo-leveling">Detayli Solo Leveling LSP ornegi (Python) →</a>' if p.get("extra_section") and not CLASS_EXAMPLES_BY_LETTER.get(p['letter']) else ""}
          </div>
        </article>
        """)
    return f"""
        <div id="solid-ilkeleri">
        <div class="solid-header">
          <h3>{html.escape(STUDENT_HEADER['title'])}</h3>
          <p style="font-size:.85rem;color:var(--text-soft);margin-bottom:.75rem">{html.escape(STUDENT_HEADER['subtitle'])}</p>
          {fields}
        </div>
        <div class="callout callout-exam">
          Her SOLID ilkesi: <strong>ilke adi, tanimi, amaci, kotu/iyi kod</strong> ve aciklama.
          Altinda sinif arkadaslarinin Python ornekleri (Makyaj Studyosu, Leon, Solo Leveling vb.) yer alir.
        </div>
        {"".join(principles)}
        </div>
        """


def build_solid_exercises_inner() -> str:
    cards = []
    for ex in WEEK9_EXERCISES:
        gist = ""
        if ex.get("gist"):
            gist = f'<div class="enrich-sources"><a href="{html.escape(ex["gist"])}" target="_blank" rel="noopener">PDF Gist cozumu</a></div>'
        cards.append(f"""
        <article class="solid-principle" id="oop-ex-{html.escape(ex['id'])}">
          <div class="solid-principle-head">
            <div class="solid-letter">{html.escape(ex['principle'])}</div>
            <div>
              <h3>{html.escape(ex['title'])}</h3>
              <span>PDF 9. Hafta Alistirma — Cozumlu</span>
            </div>
          </div>
          <div class="solid-body">
            <div class="solid-row">
              <div class="solid-row-label">Problem</div>
              <p>{html.escape(ex['problem'])}</p>
            </div>
            <div class="solid-code-grid">
              <div class="solid-code-box bad">
                <div class="solid-code-box-head">Ilkeye aykiri (kotu) kod</div>
                <pre><code>{html.escape(ex['bad_code'])}</code></pre>
                <div class="solid-why"><strong>Neden kotu?</strong> {html.escape(ex['bad_why'])}</div>
              </div>
              <div class="solid-code-box good">
                <div class="solid-code-box-head">Ilkeye uygun (iyi) kod</div>
                <pre><code>{html.escape(ex['good_code'])}</code></pre>
                <div class="solid-why"><strong>Neden iyi?</strong> {html.escape(ex['good_why'])}</div>
              </div>
            </div>
            {gist}
          </div>
        </article>
        """)
    return f"""
        <div id="oop-solid-alistirmalar">
        <div class="callout callout-exam">
          PDF 9. hafta odevleri: AlanHesaplayici (OCP), Dosya (LSP), Cihaz (ISP), Bildirim (DIP).
        </div>
        {"".join(cards)}
        </div>
        """


def build_lsp_detail_inner() -> str:
    rules = "".join(
        f"""
        <div class="lsp-rule">
          <span class="lsp-rule-num">{r['num']}</span>
          <h4>{html.escape(r['name'])} — {html.escape(r['rule'])}</h4>
          <p>{html.escape(r['example'])}</p>
        </div>
        """
        for r in LSP_FIVE_RULES
    )
    return f"""
        <div id="lsp-solo-leveling">
        <div class="lsp-hero">
          <h3>{html.escape(LSP_INTRO['title'])}</h3>
          <p><strong>Ne demek?</strong> {html.escape(LSP_INTRO['what'])}</p>
          <p style="margin-top:.5rem">{html.escape(LSP_INTRO['short'])}</p>
        </div>
        <div class="callout callout-web">
          Sinif arkadas calismasindan uyarlandi (Muhammed Hamza Erha). Python kodu.
        </div>
        <div class="solid-code-grid">
          <div class="solid-code-box bad">
            <div class="solid-code-box-head">Kotu kod — LSP ihlali (YanlisPlayer)</div>
            <pre><code>{html.escape(BAD_CODE)}</code></pre>
            <div class="solid-why"><strong>Neden kotu?</strong> {html.escape(BAD_WHY)}</div>
          </div>
          <div class="solid-code-box good">
            <div class="solid-code-box-head">Iyi kod — LSP dogru (Hunter / SungJinwoo)</div>
            <pre><code>{html.escape(GOOD_CODE)}</code></pre>
            <div class="solid-why"><strong>Neden iyi?</strong> {html.escape(GOOD_WHY)}</div>
          </div>
        </div>
        <h3 style="margin:1.25rem 0 .65rem;font-size:.95rem">LSP'nin 5 Kurali</h3>
        <div class="lsp-rules">{rules}</div>
        <p class="lsp-credit">{html.escape(CREDIT)}</p>
        </div>
        """


def build_oop_week10_block() -> str:
    sid = "hafta-10-solid-calisma-odev-cozumleri"
    meta = OOP_WEEK_META[sid]
    num, tag, summary, simple = meta["num"], meta["tag"], meta["summary"], meta["simple"]
    chips = "".join(f'<span class="chip">{html.escape(s)}</span>' for s in simple)
    items = "".join(f"<li>{html.escape(s)}</li>" for s in simple)
    panels = f"""
        <details class="panel" open>
          <summary>1. SOLID Ilkeleri — Odev / Sinav Formati (S-O-L-I-D)</summary>
          <div class="panel-inner">{build_solid_principles_inner()}</div>
        </details>
        <details class="panel">
          <summary>2. PDF Alistirmalari — OCP, LSP, ISP, DIP (Cozumlu)</summary>
          <div class="panel-inner">{build_solid_exercises_inner()}</div>
        </details>
        <details class="panel">
          <summary>3. LSP Solo Leveling Detay Ornegi</summary>
          <div class="panel-inner">{build_lsp_detail_inner()}</div>
        </details>
        """
    return f"""
    <section class="week-block oop-week" id="{sid}">
      <div class="week-head">
        <div class="week-head-top">
          <span class="week-badge">Hafta {num}</span>
          <span class="week-tag">{html.escape(tag)}</span>
        </div>
        <h2>Hafta 10 — SOLID Calisma & Odev Cozumleri</h2>
        <div class="week-summary"><strong>Bu haftada ne var?</strong> {html.escape(summary)}</div>
        <div class="focus-chips">{chips}</div>
      </div>
      <div class="week-body">
        <div class="simple-box">
          <h3>Hafta 10 Ozeti</h3>
          <ul>{items}</ul>
        </div>
        {panels}
      </div>
    </section>
    """


def build_oop_course(oop_sections) -> str:
    blocks = [build_oop_banner(), build_oop_must_know_section()]
    for title, sid, body in oop_sections:
        if "konu-indeksi" in sid:
            inner = enhance_inner_html(md_to_html_fragment(body), OOP_GLOSSARY)
            blocks.append(f"""
            <section class="special-block" id="oop-konu-indeksi">
              <div class="special-head"><h2>OOP Konu Indeksi</h2></div>
              <div class="special-body">
                <div class="callout callout-tip">Tablodaki <strong>i</strong> butonuna tikla: terimin ne oldugu, nasil kullanildigi ve ornek kod acilir.</div>
                {inner}
              </div>
            </section>
            """)
            break
    for title, sid, body in oop_sections:
        if "konu-indeksi" in sid or "solid-alistirma" in sid:
            continue
        if title.lower().startswith("hafta"):
            blocks.append(build_oop_week_block(title, sid, body))
    blocks.append(build_oop_week10_block())
    return "".join(blocks)


def build_study_plan_section() -> str:
    days_html = []
    task_id = 0
    for day in STUDY_PLAN:
        tasks_li = []
        for task in day["tasks"]:
            task_id += 1
            tid = f"d{day['day']}-t{task_id}"
            link = f'<a href="{html.escape(task["link"])}">Konuya git →</a>' if task.get("link") else ""
            tasks_li.append(f"""
            <li>
              <input type="checkbox" id="{tid}" data-task-id="{tid}">
              <label for="{tid}">{html.escape(task["text"])}{link}</label>
            </li>
            """)
        remember_li = "".join(f"<li>{html.escape(r)}</li>" for r in day["remember"])
        days_html.append(f"""
        <div class="plan-day" data-day="{day['day']}">
          <div class="plan-day-head">
            <div class="plan-day-num">{day['day']}</div>
            <div>
              <div class="plan-day-title">Gun {day['day']}: {html.escape(day['title'])}</div>
              <div class="plan-day-meta">{html.escape(day['time'])}</div>
              <div class="plan-day-goal">{html.escape(day['goal'])}</div>
            </div>
            <span class="plan-day-toggle">+</span>
          </div>
          <div class="plan-day-body">
            <ul class="plan-tasks">{"".join(tasks_li)}</ul>
            <div class="plan-remember"><strong>Bu gunun sonunda bilmen gerekenler:</strong><ul>{remember_li}</ul></div>
          </div>
        </div>
        """)

    return f"""
    <section class="special-block" id="7-gunluk-plan">
      <div class="plan-hero">
        <h2>7 Gun Kala — Sifirdan Gecer Not Plani</h2>
        <p>Ruby/Rails bilgin yoksa bu plani takip et. Her gun 2-3 saat yeterli. Gorevleri tiklayarak ilerlemeni kaydet.</p>
        <div class="plan-progress"><div class="plan-progress-bar" id="planProgressBar"></div></div>
        <div class="plan-progress-text" id="planProgressText">0 / 0 gorev tamamlandi</div>
        <div style="margin-top:.85rem"><button type="button" class="btn btn-ghost" id="openToday" style="background:rgba(255,255,255,.15);color:white;border-color:rgba(255,255,255,.3)">Bugunun gorevine git</button></div>
      </div>
      <div class="special-body" style="padding-top:0">
        {"".join(days_html)}
      </div>
    </section>
    """


def build_topic_index_section(body: str) -> str:
    inner = enhance_inner_html(md_to_html_fragment(body), INTPROG_GLOSSARY)
    return f"""
    <section class="special-block" id="konu-indeksi">
      <div class="special-head"><h2>Konu Indeksi — Alfabetik</h2></div>
      <div class="special-body">
        <div class="callout callout-tip">Tablodaki <strong>i</strong> butonuna tikla: terimin mantigi ve kullanimi acilir. <strong>Kapsulleme</strong>, <strong>kalitim</strong>, <strong>polimorfizm</strong> vurgulanmistir.</div>
        {inner}
      </div>
    </section>
    """


def build_enrich_sources_html(sources: list) -> str:
    links = "".join(
        f'<a href="{html.escape(s["url"])}" target="_blank" rel="noopener">{html.escape(s["name"])}</a>'
        for s in sources
    )
    return f'<div class="enrich-sources">{links}</div>' if links else ""


def build_enrich_code_html(code: str) -> str:
    if not code:
        return ""
    return f'<div class="code-block"><div class="code-label">ornek kod</div><pre><code>{html.escape(code)}</code></pre></div>'


def build_ruby_faq_html(topic: dict, compact: bool = False) -> str:
    faq = topic.get("ruby_faq")
    if not faq:
        return ""
    section = faq.get("section_title", "")
    section_num = faq.get("section", "")
    label = "Ruby Resmi SSS (Turkce)"
    if section:
        label += f" — Bolum {section_num}: {section}"
    answer = faq["answer"]
    if compact and len(answer) > 320:
        answer = answer[:320].rsplit(" ", 1)[0] + "..."
    return f"""
        <div class="ruby-faq-box">
          <div class="ruby-faq-label">{html.escape(label)}</div>
          <p class="ruby-faq-q"><strong>S:</strong> {html.escape(faq['question'])}</p>
          <p class="ruby-faq-a"><strong>C:</strong> {html.escape(answer)}</p>
          <a class="ruby-faq-link" href="{html.escape(faq['url'])}" target="_blank" rel="noopener">
            ruby-lang.org resmi FAQ →
          </a>
        </div>
        """


def build_inline_enrichment_html(topic: dict, compact: bool = False) -> str:
    code = build_enrich_code_html(topic["code"]) if not compact else ""
    exam = (
        f'<div class="enrich-exam"><strong>Sinav ipucu:</strong> {html.escape(topic["exam_tip"])}</div>'
        if topic.get("exam_tip") and not compact
        else ""
    )
    if compact:
        return f"""
        <div class="panel-enrich" id="enrich-{html.escape(topic['id'])}">
          <div class="panel-enrich-label">Internet kaynagi + Ruby resmi SSS (Turkce)</div>
          <p><strong>{html.escape(topic['title'])}</strong> — {html.escape(topic['summary'])}</p>
          <p>{html.escape(topic['explain'][:280])}{'...' if len(topic['explain']) > 280 else ''}</p>
          {build_ruby_faq_html(topic, compact=True)}
          {build_enrich_code_html(topic['code'])}
          {build_enrich_sources_html(topic['sources'])}
        </div>
        """
    return ""


def build_enrich_card_html(topic: dict) -> str:
    return f"""
    <div class="enrich-card" id="enrich-{html.escape(topic['id'])}" data-week="{topic['week']}">
      <div class="enrich-card-head">
        <span class="enrich-week-badge">H{topic['week']}</span>
        <h3>{html.escape(topic['title'])}</h3>
      </div>
      <div class="enrich-card-body">
        <p>{html.escape(topic['summary'])}</p>
        <p>{html.escape(topic['explain'])}</p>
        {build_ruby_faq_html(topic)}
        {build_enrich_code_html(topic['code'])}
        {f'<div class="enrich-exam"><strong>Sinav ipucu:</strong> {html.escape(topic["exam_tip"])}</div>' if topic.get("exam_tip") else ""}
        {build_enrich_sources_html(topic['sources'])}
      </div>
    </div>
    """


def build_web_enrichment_section() -> str:
    tabs = ['<button type="button" class="enrich-tab active" data-week="all">Tumu</button>']
    for w in range(2, 11):
        tabs.append(f'<button type="button" class="enrich-tab" data-week="{w}">Hafta {w}</button>')
    cards = "".join(build_enrich_card_html(t) for t in TOPICS)
    return f"""
    <section class="special-block" id="internet-kaynaklari">
      <div class="special-head"><h2>Internet Kaynaklari ile Derinlestirilmis Konular</h2></div>
      <div class="special-body">
        <div class="callout callout-web">
          PDF slayt basliklari (kapsulleme, migration, kalitim vb.) resmi Ruby SSS
          (<a href="https://www.ruby-lang.org/en/documentation/faq/7/" target="_blank" rel="noopener">ruby-lang.org</a>)
          ve Rails dokumantasyonundan Turkce aciklamalarla desteklendi.
        </div>
        <div class="enrich-toolbar">{"".join(tabs)}</div>
        <div class="enrich-grid">{cards}</div>
      </div>
    </section>
    """


def build_must_know_section() -> str:
    items = "".join(
        f'<div class="must-know-item"><strong>{html.escape(k)}</strong><span>{html.escape(v)}</span></div>'
        for k, v in MUST_KNOW
    )
    return f"""
    <section class="special-block" id="sinav-ezber-listesi">
      <div class="special-head"><h2>Sinav Ezber Listesi — 15 Kritik Madde</h2></div>
      <div class="special-body">
        <div class="callout callout-exam">7. gun ve sinav sabahi bu listeyi 2 kez oku. Cogu sinav sorusu bu maddelerden turetilir.</div>
        <div class="must-know-grid">{items}</div>
      </div>
    </section>
    """


def build_quiz_section() -> str:
    total = sum(len(block["items"]) for block in QUIZ)
    tabs = ['<button type="button" class="quiz-tab active" data-week="all">Tumu</button>']
    for block in QUIZ:
        week = block["week"]
        label = html.escape(block["title"])
        tabs.append(
            f'<button type="button" class="quiz-tab" data-week="{week}">H{week}: {label}</button>'
        )

    cards = []
    q_num = 0
    for block in QUIZ:
        week = block["week"]
        for item in block["items"]:
            q_num += 1
            q_text = html.escape(item["q"])
            a_text = html.escape(item["a"])
            cards.append(f"""
            <div class="quiz-card" data-week="{week}">
              <div class="quiz-q"><span class="q-n">{q_num}</span> {q_text}</div>
              <button type="button" class="quiz-btn">Cevabi Goster</button>
              <div class="quiz-a">{a_text}</div>
            </div>
            """)

    return f"""
    <section class="special-block" id="sinav-sorulari-kendini-test-et">
      <div class="special-head"><h2>Kendini Test Et — {total} Soru</h2></div>
      <div class="special-body">
        <div class="callout callout-exam">Soruya tikla, cevabi gor. Sinav oncesi tum sorulari en az bir kez coz.</div>
        <div class="quiz-toolbar">
          <div class="quiz-tabs">{"".join(tabs)}</div>
          <div class="quiz-actions">
            <button type="button" class="btn btn-ghost" id="quizShowAll">Tum cevaplari ac</button>
            <button type="button" class="btn btn-ghost" id="quizHideAll">Tum cevaplari kapat</button>
          </div>
        </div>
        <div class="quiz-grid">{"".join(cards)}</div>
      </div>
    </section>
    """


def build_commands_section(body: str) -> str:
    inner = enhance_inner_html(md_to_html_fragment(body))
    return f"""
    <section class="special-block" id="komut-hizli-referans">
      <div class="special-head"><h2>Komut Hizli Referans</h2></div>
      <div class="special-body">
        <div class="callout callout-tip">Terminalde en cok kullanacagin Rails komutlari. Ezber listesi olarak kullan.</div>
        {inner}
      </div>
    </section>
    """


def build_toc_intprog(sections) -> str:
    lines = [
        '<a href="#course-hub"><span class="w-num">*</span>Ders Secimi</a>',
        '<a href="#intprog-course"><span class="w-num">IP</span>Giris</a>',
        '<a href="#7-gunluk-plan"><span class="w-num">7</span>7 Gunluk Plan</a>',
        '<a href="#konu-indeksi"><span class="w-num">A</span>Konu Indeksi</a>',
        '<a href="#internet-kaynaklari"><span class="w-num">W</span>Internet Kaynaklari</a>',
        '<a href="#sinav-ezber-listesi"><span class="w-num">!</span>Ezber Listesi</a>',
        '<div class="nav-label">Haftalar</div>',
    ]
    for title, sid, _ in sections:
        if "konu-indeksi" in sid or "sinav" in sid or "komut" in sid or "cevap" in sid:
            continue
        meta = WEEK_META.get(sid, {})
        num = meta.get("num", "?")
        short = title.split("—")[-1].strip() if "—" in title else title
        lines.append(
            f'<a href="#{sid}"><span class="w-num">{num}</span>{html.escape(short)}</a>'
        )
    lines.append('<div class="nav-label">Sinav</div>')
    lines.append('<a href="#komut-hizli-referans"><span class="w-num">#</span>Komutlar</a>')
    lines.append(
        '<a href="#sinav-sorulari-kendini-test-et"><span class="w-num">?</span>Test Sorulari</a>'
    )
    return "\n".join(lines)


def build_toc_oop(oop_sections=None) -> str:
    lines = [
        '<a href="#course-hub"><span class="w-num">*</span>Ders Secimi</a>',
        '<a href="#oop-course"><span class="w-num">O</span>Giris</a>',
        '<a href="#oop-konu-indeksi"><span class="w-num">A</span>Konu Indeksi</a>',
        '<a href="#oop-ezber"><span class="w-num">!</span>OOP Ezber</a>',
        '<div class="nav-label">Haftalar</div>',
    ]
    if oop_sections:
        for title, sid, _ in oop_sections:
            if "konu-indeksi" in sid or "solid-alistirma" in sid:
                continue
            if not title.lower().startswith("hafta"):
                continue
            meta = OOP_WEEK_META.get(sid, {})
            num = meta.get("num", "?")
            short = title.split("—")[-1].strip() if "—" in title else title
            lines.append(
                f'<a href="#{sid}"><span class="w-num">{num}</span>{html.escape(short)}</a>'
            )
        h10 = OOP_WEEK_META["hafta-10-solid-calisma-odev-cozumleri"]
        if not any(sid == "hafta-10-solid-calisma-odev-cozumleri" for _, sid, _ in oop_sections):
            lines.append(
                f'<a href="#hafta-10-solid-calisma-odev-cozumleri">'
                f'<span class="w-num">{h10["num"]}</span>SOLID Calisma</a>'
            )
    return "\n".join(lines)


def build_intprog_content(sections) -> str:
    intprog_blocks = [build_intprog_banner(), build_study_plan_section()]
    for title, sid, body in sections:
        if "konu-indeksi" in sid:
            intprog_blocks.append(build_topic_index_section(body))
            break
    intprog_blocks.append(build_must_know_section())
    intprog_blocks.append(build_web_enrichment_section())
    for title, sid, body in sections:
        if "cevap" in sid.lower() or "konu-indeksi" in sid:
            continue
        if "sinav-sorular" in sid:
            intprog_blocks.append(build_quiz_section())
        elif "komut-hizli" in sid:
            intprog_blocks.append(build_commands_section(body))
        elif title.lower().startswith("hafta"):
            intprog_blocks.append(build_week_block(title, sid, body))

    return "".join(intprog_blocks)


def generate_pdf():
    html_path = HTML_FILE.resolve()
    pdf_path = PDF_FILE.resolve()
    browsers = [
        Path(r"C:\Program Files\Google\Chrome\Application\chrome.exe"),
        Path(r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"),
        Path(r"C:\Program Files\Microsoft\Edge\Application\msedge.exe"),
    ]
    url = "file:///" + str(html_path).replace("\\", "/")
    for exe in browsers:
        if exe.exists():
            subprocess.run(
                [
                    str(exe),
                    "--headless",
                    "--disable-gpu",
                    "--no-pdf-header-footer",
                    f"--print-to-pdf={pdf_path}",
                    url,
                ],
                capture_output=True,
                timeout=30,
            )
            if pdf_path.exists() and pdf_path.stat().st_size > 10000:
                return True
    return False


def main():
    md_text = MD_FILE.read_text(encoding="utf-8")
    sections = split_sections(md_text)
    oop_sections = []
    if OOP_MD_FILE.exists():
        oop_sections = split_sections(OOP_MD_FILE.read_text(encoding="utf-8"))
    toc_intprog = build_toc_intprog(sections)
    toc_oop = build_toc_oop(oop_sections)
    content_intprog = build_intprog_content(sections)
    content_oop = build_oop_course(oop_sections)
    page = HTML_TEMPLATE.format(
        toc_intprog=toc_intprog,
        toc_oop=toc_oop,
        course_picker=build_course_picker(),
        ruby_icon_sm=RUBY_ICON_SM,
        python_icon_sm=PYTHON_ICON_SM,
        content_intprog=content_intprog,
        content_oop=content_oop,
    )
    HTML_FILE.write_text(page, encoding="utf-8")
    print(f"OK Website: {HTML_FILE}")
    if generate_pdf():
        print(f"OK PDF: {PDF_FILE}")
    else:
        print("PDF: Siteyi acip 'PDF Olarak Indir' butonunu kullan")


if __name__ == "__main__":
    main()