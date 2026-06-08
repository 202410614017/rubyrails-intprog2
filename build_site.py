#!/usr/bin/env python3
"""CALISMA_REHBERI.md -> profesyonel anlatim sitesi + PDF"""

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

BASE = Path(__file__).parent
MD_FILE = BASE / "CALISMA_REHBERI.md"
HTML_FILE = BASE / "index.html"
PDF_FILE = BASE / "CALISMA_REHBERI.pdf"

WEEK_META = {
    "hafta-2-ruby-rails-giris": {
        "num": 2,
        "tag": "Ruby & Rails Temelleri",
        "summary": "Ruby dilinin temel yapı taşlarını ve Rails projesinin nasıl kurulup çalıştığını öğrenirsin. MVC mimarisi bu haftanın omurgasıdır.",
        "focus": ["Ruby'de her sey nesnedir", "MVC: routes -> controller -> model -> view", "rails new, db:create, rails s"],
    },
    "hafta-3-orm-active-record": {
        "num": 3,
        "tag": "Veritabani & ORM",
        "summary": "SQL yazmadan veritabani islemleri yapmayi ogrenirsin. Active Record, tablolari Ruby siniflarina cevirir.",
        "focus": ["ORM = tablo <-> sinif eslestirmesi", "find / find_by / where farki", "Migration ile sema yonetimi"],
    },
    "hafta-4-enum-routes-controllers": {
        "num": 4,
        "tag": "Routes & CRUD",
        "summary": "HTTP isteklerini controller action'larina baglarsin. Enum, scope ve CRUD rotalarini kullanirsin.",
        "focus": ["resources :posts = 7 CRUD route", "GET/POST/PUT/PATCH/DELETE", "Enum ile status yonetimi"],
    },
    "hafta-5-form-helpers-strong-parameters": {
        "num": 5,
        "tag": "Formlar & Guvenlik",
        "summary": "Kullanicidan veri almak icin form helper'lari ve guvenli parametre filtreleme (Strong Parameters) kullanilir.",
        "focus": ["form_with model: @post", "post_params ile mass assignment korumasi", "Partials ve before_action"],
    },
    "hafta-6-bootstrap-frontend": {
        "num": 6,
        "tag": "Bootstrap UI",
        "summary": "Blog arayuzunu Bootstrap ile duzenlersin. Grid, navbar, footer ve card yapilari kullanilir.",
        "focus": ["12 sutunlu grid sistemi", "container vs container-fluid", "Partial: _navbar, _footer"],
    },
    "hafta-7-model-iliskileri-kategori": {
        "num": 7,
        "tag": "Model Iliskileri",
        "summary": "Tablolar arasi iliskileri kurarsin. Post ve Category coktan coga (HABTM) baglanir.",
        "focus": ["belongs_to / has_many / HABTM", "scaffold ile hizli CRUD", "category_ids: [] strong param"],
    },
    "hafta-8-validation-active-storage": {
        "num": 8,
        "tag": "Dogrulama & Dosya",
        "summary": "Veri kalitesini model seviyesinde kontrol edersin. Active Storage ile resim yuklersin.",
        "focus": ["validates vs normalizes farki", "presence, uniqueness, length", "has_one_attached :image"],
    },
    "hafta-9-i18n-friendlyid-action-text": {
        "num": 9,
        "tag": "I18n & Zengin Icerik",
        "summary": "Uygulamayi coklu dile cevirirsin. FriendlyId ile SEO dostu URL, Action Text ile zengin metin.",
        "focus": ["I18n.t ve locale dosyalari", "friendly_id :title, use: :slugged", "has_rich_text :article"],
    },
    "hafta-10-devise-authorization": {
        "num": 10,
        "tag": "Kimlik & Yetki",
        "summary": "Devise ile kullanici girisi yapilir. Roller (editor/admin) ve yetkilendirme eklenir.",
        "focus": ["Authentication vs Authorization", "authenticate_user!", "current_user", "belongs_to :user"],
    },
}

HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Internet Programciligi II | Calisma Rehberi</title>
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

    /* Sidebar */
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

    /* Main */
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

    /* Week blocks */
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

    /* Accordion panels */
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
    .panel[open] summary::after {{ content: '−'; }}
    .panel-inner {{ padding: .85rem 1rem 1rem; background: white; }}

    /* Content typography */
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

    /* Special sections (quiz, commands) */
    .special-block {{ background: var(--paper); border: 1px solid var(--line); border-radius: var(--radius); margin-bottom: 1.5rem; box-shadow: var(--shadow); overflow: hidden; scroll-margin-top: 1rem; }}
    .special-head {{ padding: 1.1rem 1.5rem; border-bottom: 1px solid var(--line); background: #fafbfc; }}
    .special-head h2 {{ font-size: 1.1rem; font-weight: 700; border: none; margin: 0; padding: 0; }}
    .special-body {{ padding: .5rem 1.5rem 1.25rem; }}

    .quiz-grid {{ display: grid; gap: .5rem; }}
    .quiz-item {{
      border: 1px solid var(--line); border-radius: 8px; padding: .7rem .85rem; background: #fafbfc;
    }}
    .quiz-item summary {{ cursor: pointer; font-weight: 500; font-size: .88rem; list-style: none; }}
    .quiz-item summary::-webkit-details-marker {{ display: none; }}
    .quiz-item .q-num {{ color: var(--accent); font-weight: 700; margin-right: .25rem; }}
    .quiz-item .ans {{ margin-top: .5rem; padding-top: .5rem; border-top: 1px dashed var(--line); font-size: .84rem; color: var(--green-text); }}

    .callout {{
      border-radius: 8px; padding: .75rem 1rem; margin: .65rem 0; font-size: .86rem;
    }}
    .callout-exam {{ background: var(--amber-soft); border: 1px solid var(--amber-border); color: #78350f; }}
    .callout-tip {{ background: var(--green-soft); border: 1px solid var(--green-border); color: #14532d; }}

    .mobile-toggle {{
      display: none; position: fixed; bottom: 1.25rem; right: 1.25rem; z-index: 200;
      background: var(--accent); color: white; border: none; border-radius: 50%;
      width: 48px; height: 48px; font-size: 1.2rem; cursor: pointer; box-shadow: var(--shadow-lg);
    }}

    @media (max-width: 768px) {{
      .sidebar {{ transform: translateX(-100%); transition: transform .25s; }}
      .sidebar.open {{ transform: translateX(0); box-shadow: var(--shadow-lg); }}
      .main {{ margin-left: 0; padding: 1rem; }}
      .mobile-toggle {{ display: flex; align-items: center; justify-content: center; }}
    }}

    @media print {{
      .sidebar, .mobile-toggle, .topbar-actions {{ display: none !important; }}
      .main {{ margin-left: 0; max-width: 100%; padding: .5rem; }}
      .week-block, .special-block {{ break-inside: avoid; box-shadow: none; }}
      .panel {{ break-inside: avoid; }}
      .panel[open] summary {{ border-bottom: 1px solid #ddd; }}
    }}
  </style>
</head>
<body>
  <div class="layout">
    <aside class="sidebar" id="sidebar">
      <div class="brand">
        <div class="brand-kicker">Sinav Rehberi</div>
        <h1>Internet Programciligi II</h1>
        <p>Hafta 2-10 | Ruby on Rails</p>
      </div>
      <nav>{toc}</nav>
    </aside>
    <main class="main">
      <div class="topbar">
        <h2>Ders Notlari — Anlatimli Ozet</h2>
        <p>Tum konular korundu; her hafta acilir-kapanir bolumler halinde sadelestirildi. Soldan hafta sec veya asagidan incele.</p>
        <div class="topbar-actions">
          <button class="btn btn-red" onclick="window.print()">PDF Olarak Indir</button>
          <a class="btn btn-ghost" href="#sinav-sorulari-kendini-test-et">Test Sorulari</a>
        </div>
      </div>
      {content}
    </main>
  </div>
  <button class="mobile-toggle" id="menuBtn" aria-label="Menu">&#9776;</button>
  <script>
    const links = document.querySelectorAll('.sidebar nav a');
    const sections = [...document.querySelectorAll('.week-block, .special-block')];
    window.addEventListener('scroll', () => {{
      let cur = '';
      sections.forEach(s => {{ if (window.scrollY >= s.offsetTop - 100) cur = s.id; }});
      links.forEach(a => a.classList.toggle('active', a.getAttribute('href') === '#' + cur));
    }});
    document.getElementById('menuBtn').onclick = () => document.getElementById('sidebar').classList.toggle('open');
    links.forEach(a => a.onclick = () => document.getElementById('sidebar').classList.remove('open'));
    document.querySelectorAll('.week-block .panel').forEach((p, i) => {{ if (i === 0) p.open = true; }});
  </script>
</body>
</html>"""


def slugify(text: str) -> str:
    text = text.lower().strip()
    for k, v in {'ı':'i','ğ':'g','ü':'u','ş':'s','ö':'o','ç':'c','İ':'i','Ğ':'g','Ü':'u','Ş':'s','Ö':'o','Ç':'c','—':'-','–':'-'}.items():
        text = text.replace(k, v)
    text = re.sub(r'[^a-z0-9\s-]', '', text)
    return re.sub(r'[\s-]+', '-', text).strip('-')


def md_to_html_fragment(md: str) -> str:
    def md_slugify(v, sep='-'):
        return slugify(v)
    md_engine = markdown.Markdown(extensions=[TableExtension(), FencedCodeExtension(), TocExtension(slugify=md_slugify, permalink=False)])
    return md_engine.convert(md)


def split_sections(md_text: str):
    md_text = re.sub(r'^# .+\n\n', '', md_text)
    md_text = re.sub(r'> .+\n\n', '', md_text)
    md_text = re.sub(r'## İçindekiler\n\n.*?(?=\n---\n)', '', md_text, flags=re.DOTALL)
    parts = re.split(r'\n---\n\n## ', md_text)
    sections = []
    for i, part in enumerate(parts):
        if i == 0:
            if part.startswith('## '):
                part = part[3:]
            else:
                continue
        else:
            part = '## ' + part
        m = re.match(r'## (.+?)\n', part)
        if not m:
            continue
        title = m.group(1).strip()
        body = part[m.end():].strip()
        sections.append((title, slugify(title), body))
    return sections


def split_h3_sections(body: str):
    chunks = re.split(r'\n### ', body)
    result = []
    for i, chunk in enumerate(chunks):
        if i == 0 and not chunk.strip():
            continue
        if i > 0:
            chunk = '### ' + chunk
        m = re.match(r'### (.+?)\n', chunk)
        if m:
            result.append((m.group(1).strip(), chunk[m.end():].strip()))
        elif chunk.strip():
            result.append(('Genel', chunk.strip()))
    return result


def enhance_inner_html(html: str) -> str:
    html = re.sub(
        r'<pre><code(?: class="language-(\w+)")?>(.*?)</code></pre>',
        lambda m: f'<div class="code-block"><div class="code-label">{m.group(1) or "kod"}</div><pre><code>{m.group(2)}</code></pre></div>',
        html, flags=re.DOTALL
    )
    html = re.sub(r'<hr\s*/?>', '', html)
    return html


def build_week_block(title: str, sid: str, body: str) -> str:
    meta = WEEK_META.get(sid, {})
    num = meta.get('num', '')
    tag = meta.get('tag', '')
    summary = meta.get('summary', '')
    focus = meta.get('focus', [])

    chips = ''.join(f'<span class="chip">{f}</span>' for f in focus)
    head = f'''
    <section class="week-block" id="{sid}">
      <div class="week-head">
        <div class="week-head-top">
          {"<span class='week-badge'>Hafta " + str(num) + "</span>" if num else ""}
          {"<span class='week-tag'>" + tag + "</span>" if tag else ""}
        </div>
        <h2>{title}</h2>
        {"<div class='week-summary'><strong>Bu haftada ne ogreniyorsun?</strong> " + summary + "</div>" if summary else ""}
        {"<div class='focus-chips'>" + chips + "</div>" if chips else ""}
      </div>
      <div class="week-body">
    '''

    panels = []
    for h3_title, h3_body in split_h3_sections(body):
        inner = enhance_inner_html(md_to_html_fragment(h3_body))
        open_attr = ''
        panels.append(f'''
        <details class="panel"{open_attr}>
          <summary>{h3_title}</summary>
          <div class="panel-inner">{inner}</div>
        </details>
        ''')

    return head + ''.join(panels) + '</div></section>'


def build_quiz_section(body: str) -> str:
    html = md_to_html_fragment(body)
    questions = re.findall(r'<h3[^>]*>([^<]+)</h3>\s*<ol>(.*?)</ol>', html, re.DOTALL)
    if not questions:
        return f'<section class="special-block" id="sinav-sorulari-kendini-test-et"><div class="special-head"><h2>Sinav Sorulari</h2></div><div class="special-body">{enhance_inner_html(html)}</div></section>'

    items = []
    answers_html = ''
    ans_match = re.search(r'<details>.*?<summary>.*?</summary>\s*(.*?)\s*</details>', html, re.DOTALL)
    if ans_match:
        answers_html = re.sub(r'<[^>]+>', ' ', ans_match.group(1))
        answers_html = re.sub(r'\s+', ' ', answers_html).strip()

    ans_parts = [a.strip() for a in answers_html.split('|')] if answers_html else []

    q_num = 0
    for cat, ol in questions:
        for li in re.findall(r'<li>(.*?)</li>', ol, re.DOTALL):
            q_text = re.sub(r'<[^>]+>', '', li).strip()
            ans = ans_parts[q_num] if q_num < len(ans_parts) else 'Cevap icin slaytlara bak.'
            q_num += 1
            items.append(f'''
            <details class="quiz-item">
              <summary><span class="q-num">{q_num}.</span> {q_text}</summary>
              <div class="ans">{ans}</div>
            </details>
            ''')

    return f'''
    <section class="special-block" id="sinav-sorulari-kendini-test-et">
      <div class="special-head"><h2>Kendini Test Et — {q_num} Soru</h2></div>
      <div class="special-body">
        <div class="callout callout-exam">Soruya tikla, cevabi gor. Sinav oncesi tum sorulari en az bir kez coz.</div>
        <div class="quiz-grid">{"".join(items)}</div>
      </div>
    </section>
    '''


def build_commands_section(body: str) -> str:
    inner = enhance_inner_html(md_to_html_fragment(body))
    return f'''
    <section class="special-block" id="komut-hizli-referans">
      <div class="special-head"><h2>Komut Hizli Referans</h2></div>
      <div class="special-body">
        <div class="callout callout-tip">Terminalde en cok kullanacagin Rails komutlari. Ezber listesi olarak kullan.</div>
        {inner}
      </div>
    </section>
    '''


def build_toc(sections) -> str:
    lines = ['<div class="nav-label">Haftalar</div>']
    for title, sid, _ in sections:
        if 'sinav' in sid or 'komut' in sid or 'cevap' in sid:
            continue
        meta = WEEK_META.get(sid, {})
        num = meta.get('num', '?')
        short = title.split('—')[-1].strip() if '—' in title else title
        lines.append(f'<a href="#{sid}"><span class="w-num">{num}</span>{short}</a>')
    lines.append('<div class="nav-label">Sinav</div>')
    lines.append('<a href="#komut-hizli-referans"><span class="w-num">#</span>Komutlar</a>')
    lines.append('<a href="#sinav-sorulari-kendini-test-et"><span class="w-num">?</span>Test Sorulari</a>')
    return '\n'.join(lines)


def build_content(sections) -> str:
    blocks = []
    for title, sid, body in sections:
        if 'cevap' in sid.lower():
            continue
        if 'sinav-sorular' in sid:
            blocks.append(build_quiz_section(body))
        elif 'komut-hizli' in sid:
            blocks.append(build_commands_section(body))
        else:
            blocks.append(build_week_block(title, sid, body))
    return '\n'.join(blocks)


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
            subprocess.run([
                str(exe), "--headless", "--disable-gpu", "--no-pdf-header-footer",
                f"--print-to-pdf={pdf_path}", url
            ], capture_output=True, timeout=30)
            if pdf_path.exists() and pdf_path.stat().st_size > 10000:
                return True
    return False


def main():
    md_text = MD_FILE.read_text(encoding='utf-8')
    sections = split_sections(md_text)
    toc = build_toc(sections)
    content = build_content(sections)
    html = HTML_TEMPLATE.format(toc=toc, content=content)
    HTML_FILE.write_text(html, encoding='utf-8')
    print(f"OK Website: {HTML_FILE}")
    if generate_pdf():
        print(f"OK PDF: {PDF_FILE}")
    else:
        print("PDF: Siteyi acip 'PDF Olarak Indir' butonunu kullan")


if __name__ == '__main__':
    main()
