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

BASE = Path(__file__).parent
MD_FILE = BASE / "CALISMA_REHBERI.md"
HTML_FILE = BASE / "index.html"
PDF_FILE = BASE / "CALISMA_REHBERI.pdf"

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
  <title>Internet Programciligi II | Ders Notu Arsivi</title>
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
      --sidebar-w: 260px;
      --radius: 12px;
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
    .layout {{ display: flex; min-height: 100vh; }}

    .sidebar {{
      width: var(--sidebar-w);
      background: var(--sidebar);
      border-right: 1px solid var(--line);
      position: fixed; inset: 0 auto 0 0;
      overflow-y: auto; z-index: 100;
      padding: 1.25rem 0 2rem;
    }}
    .brand {{ padding: 0 1.25rem 1.25rem; border-bottom: 1px solid var(--line); margin-bottom: .75rem; }}
    .brand-kicker {{ font-size: .68rem; font-weight: 600; letter-spacing: .08em; text-transform: uppercase; color: var(--accent); }}
    .brand h1 {{ font-size: 1rem; font-weight: 700; margin-top: .35rem; line-height: 1.35; }}
    .brand p {{ font-size: .78rem; color: var(--text-soft); margin-top: .35rem; }}
    .nav-label {{ padding: .85rem 1.25rem .35rem; font-size: .68rem; font-weight: 600; text-transform: uppercase; letter-spacing: .07em; color: #9ca3af; }}
    .sidebar nav a {{
      display: flex; align-items: center; gap: .55rem;
      padding: .5rem 1.25rem; color: var(--text-soft); text-decoration: none;
      font-size: .84rem; border-left: 3px solid transparent; transition: .15s;
    }}
    .sidebar nav a .w-num {{
      width: 1.35rem; height: 1.35rem; border-radius: 6px; background: var(--bg);
      display: inline-flex; align-items: center; justify-content: center;
      font-size: .68rem; font-weight: 700; color: var(--text-soft); flex-shrink: 0;
    }}
    .sidebar nav a:hover, .sidebar nav a.active {{
      color: var(--text); background: var(--accent-soft); border-left-color: var(--accent);
    }}
    .sidebar nav a.active .w-num {{ background: var(--accent); color: white; }}

    .main {{ margin-left: var(--sidebar-w); flex: 1; padding: 2rem 2.5rem 4rem; max-width: 820px; }}

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

    .mobile-toggle {{
      display: none; position: fixed; bottom: 1.25rem; right: 1.25rem; z-index: 200;
      background: var(--accent); color: white; border: none; border-radius: 50%;
      width: 48px; height: 48px; font-size: 1.2rem; cursor: pointer; box-shadow: var(--shadow-lg);
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

    @media (max-width: 768px) {{
      .sidebar {{ transform: translateX(-100%); transition: transform .25s; }}
      .sidebar.open {{ transform: translateX(0); box-shadow: var(--shadow-lg); }}
      .main {{ margin-left: 0; padding: 1rem; }}
      .mobile-toggle {{ display: flex; align-items: center; justify-content: center; }}
      .quiz-toolbar {{ flex-direction: column; align-items: stretch; }}
    }}

    @media print {{
      .sidebar, .mobile-toggle, .topbar-actions, .quiz-toolbar, .quiz-btn {{ display: none !important; }}
      .main {{ margin-left: 0; max-width: 100%; padding: .5rem; }}
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
    <aside class="sidebar" id="sidebar">
      <div class="brand">
        <div class="brand-kicker">Ders Notu Arsivi</div>
        <h1>Internet Programciligi II</h1>
        <p>Hafta 2-10 | Tum PDF icerigi</p>
      </div>
      <nav>{toc}</nav>
    </aside>
    <main class="main">
      <div class="topbar">
        <h2>Eksiksiz Ders Notu Arsivi</h2>
        <p>Tum PDF slaytlarindan cikarilmis haftalik notlar — kapsulleme, kalitim, migration, Devise dahil hicbir konu atlanmadi. 7 gunluk plan ve ezber listesi ile sinava hazirlan.</p>
        <div class="topbar-actions">
          <a class="btn btn-red" href="#7-gunluk-plan">7 Gunluk Plan</a>
          <a class="btn btn-ghost" href="#konu-indeksi">Konu Indeksi</a>
          <a class="btn btn-ghost" href="#sinav-ezber-listesi">Ezber Listesi</a>
          <button class="btn btn-ghost" onclick="window.print()">PDF Indir</button>
        </div>
        <div class="archive-toolbar">
          <input type="search" class="archive-search" id="panelSearch" placeholder="Konu ara: kapsulleme, kalitim, migration, devise...">
          <button type="button" class="btn btn-ghost" id="expandAll">Tum panelleri ac</button>
          <button type="button" class="btn btn-ghost" id="collapseAll">Tum panelleri kapat</button>
        </div>
      </div>
      {content}
    </main>
  </div>
  <button class="mobile-toggle" id="menuBtn" aria-label="Menu">&#9776;</button>
  <script>
    const links = document.querySelectorAll('.sidebar nav a');
    const sections = [...document.querySelectorAll('.week-block, .special-block, .plan-hero')];
    window.addEventListener('scroll', () => {{
      let cur = '';
      sections.forEach(s => {{ if (window.scrollY >= s.offsetTop - 100) cur = s.id; }});
      links.forEach(a => a.classList.toggle('active', a.getAttribute('href') === '#' + cur));
    }});
    document.getElementById('menuBtn').onclick = () => document.getElementById('sidebar').classList.toggle('open');
    links.forEach(a => a.onclick = () => document.getElementById('sidebar').classList.remove('open'));
    document.querySelectorAll('.week-block').forEach(week => {{
      const first = week.querySelector('.panel');
      if (first) first.open = true;
    }});

    document.getElementById('expandAll')?.addEventListener('click', () => {{
      document.querySelectorAll('.week-block .panel').forEach(p => {{ p.open = true; }});
    }});
    document.getElementById('collapseAll')?.addEventListener('click', () => {{
      document.querySelectorAll('.week-block .panel').forEach(p => {{ p.open = false; }});
    }});
    document.getElementById('panelSearch')?.addEventListener('input', e => {{
      const q = e.target.value.trim().toLowerCase();
      document.querySelectorAll('.week-block').forEach(week => {{
        let any = !q;
        week.querySelectorAll('.panel').forEach(panel => {{
          const match = !q || panel.textContent.toLowerCase().includes(q);
          panel.style.display = match ? '' : 'none';
          if (match) any = true;
        }});
        week.style.display = any ? '' : 'none';
      }});
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
      if (first) {{ first.classList.add('open'); first.scrollIntoView({{ behavior: 'smooth', block: 'start' }}); }}
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


def enhance_inner_html(fragment: str) -> str:
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
    h3_sections = sorted(split_h3_sections(body), key=lambda x: panel_sort_key(x[0]))
    for h3_title, h3_body in h3_sections:
        inner = enhance_inner_html(md_to_html_fragment(h3_body))
        panels.append(f"""
        <details class="panel">
          <summary>{html.escape(h3_title)}</summary>
          <div class="panel-inner">{inner}</div>
        </details>
        """)

    return head + simple_html + "".join(panels) + "</div></section>"


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
    inner = enhance_inner_html(md_to_html_fragment(body))
    return f"""
    <section class="special-block" id="konu-indeksi">
      <div class="special-head"><h2>Konu Indeksi — Alfabetik</h2></div>
      <div class="special-body">
        <div class="callout callout-tip">Tum PDF slaytlarindan cikarilmis konu listesi. <strong>Kapsulleme</strong>, <strong>kalitim (miras)</strong>, <strong>polimorfizm</strong> ve diger OOP kavramlari asagida tabloda vurgulanmistir.</div>
        {inner}
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


def build_toc(sections) -> str:
    lines = [
        '<div class="nav-label">Basla</div>',
        '<a href="#7-gunluk-plan"><span class="w-num">7</span>7 Gunluk Plan</a>',
        '<a href="#konu-indeksi"><span class="w-num">A</span>Konu Indeksi</a>',
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


def build_content(sections) -> str:
    blocks = [build_study_plan_section()]
    for title, sid, body in sections:
        if "konu-indeksi" in sid:
            blocks.append(build_topic_index_section(body))
            break
    blocks.append(build_must_know_section())
    for title, sid, body in sections:
        if "cevap" in sid.lower() or "konu-indeksi" in sid:
            continue
        if "sinav-sorular" in sid:
            blocks.append(build_quiz_section())
        elif "komut-hizli" in sid:
            blocks.append(build_commands_section(body))
        elif title.lower().startswith("hafta"):
            blocks.append(build_week_block(title, sid, body))
    return "\n".join(blocks)


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
    toc = build_toc(sections)
    content = build_content(sections)
    page = HTML_TEMPLATE.format(toc=toc, content=content)
    HTML_FILE.write_text(page, encoding="utf-8")
    print(f"OK Website: {HTML_FILE}")
    if generate_pdf():
        print(f"OK PDF: {PDF_FILE}")
    else:
        print("PDF: Siteyi acip 'PDF Olarak Indir' butonunu kullan")


if __name__ == "__main__":
    main()