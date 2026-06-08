# -*- coding: utf-8 -*-
"""Haftalik kisa video slayt ve anlatim metinleri (PDF ozetleri)."""

WEEK_VIDEOS = [
    {
        "num": 2,
        "sid": "hafta-2-ruby-rails-giris",
        "title": "Hafta 2: Ruby ve Rails Giris",
        "slides": [
            {
                "title": "Hafta 2 — Ruby ve Rails",
                "lines": ["Internet Programciligi II", "Ruby dili + Rails framework"],
                "say": "Hafta ikide Ruby programlama diline ve Rails web frameworkune giris yapiyoruz.",
            },
            {
                "title": "Ruby Temelleri",
                "lines": [
                    "Her sey nesnedir: sayi, metin, dizi",
                    "Symbol tekil, String her seferinde yeni",
                    "Array ve Hash en cok kullanilan yapilar",
                ],
                "say": "Ruby'de her sey nesnedir. Symbol tekil bir degerdir, String ise her seferinde yeni bir nesne olusturur. Array ve Hash veri yapilarini sik kullanacaksin.",
            },
            {
                "title": "OOP — Mutlaka Bil",
                "lines": [
                    "Kapsulleme: @name, attr_accessor",
                    "Kalitim: class Dog < Animal",
                    "Polimorfizm: speak metodunu override",
                ],
                "say": "Nesne yonelimli programlamada uc kavram cok onemli. Kapsulleme ile veriyi gizler, getter ve setter ile erisirsin. Kalitim ile alt sinif ust siniftan turetilir. Polimorfizm ile alt sinif metodu override eder.",
            },
            {
                "title": "Rails MVC",
                "lines": [
                    "Model: veritabani ve is kurallari",
                    "View: kullaniciya gorunen HTML",
                    "Controller: istegi isler, yonlendirir",
                ],
                "say": "Rails MVC mimarisini kullanir. Model veritabani ile calisir. View arayuzu gosterir. Controller gelen istegi isler ve dogru view'a yonlendirir. Akis: routes, controller, model, view.",
            },
            {
                "title": "Kurulum Komutlari",
                "lines": [
                    "rails new blog -d postgresql",
                    "rails db:create",
                    "rails s  → sunucuyu baslat",
                ],
                "say": "Projeyi rails new ile olusturursun. Veritabani icin db create, sunucu icin rails s komutunu kullan. Hafta iki tamamlandi.",
            },
        ],
    },
    {
        "num": 3,
        "sid": "hafta-3-orm-active-record",
        "title": "Hafta 3: ORM ve Active Record",
        "slides": [
            {
                "title": "Hafta 3 — ORM",
                "lines": ["Object Relational Mapping", "Tablo = Ruby sinifi"],
                "say": "Hafta uc ORM yani Object Relational Mapping konusunu isliyor. Veritabani tablosu Ruby sinifine karsilik gelir.",
            },
            {
                "title": "Temel Sorgular",
                "lines": [
                    "Post.all → tum kayitlar",
                    "Post.find(1) → bulamazsa HATA",
                    "Post.find_by(title: 'x') → nil",
                    "Post.where(status: 1) → liste",
                ],
                "say": "Post nokta all tum kayitlari getirir. Find bir numara ile arar, bulamazsa hata verir. Find by bulamazsa nil doner. Where ise filtreleyerek liste dondurur.",
            },
            {
                "title": "CRUD Islemleri",
                "lines": [
                    "create → yeni kayit",
                    "update → guncelle",
                    "destroy → sil",
                ],
                "say": "Create ile yeni kayit olusturursun. Update ile guncellersin. Destroy ile silersin. Hepsi Active Record uzerinden SQL yazmadan yapilir.",
            },
            {
                "title": "Migration",
                "lines": [
                    "rails g migration AddStatusToPost",
                    "db:migrate → uygula",
                    "db:rollback → geri al",
                ],
                "say": "Veritabani semasini migration ile degistirirsin. Migrate komutu bekleyen migrationlari uygular. Rollback son migrationi geri alir.",
            },
        ],
    },
    {
        "num": 4,
        "sid": "hafta-4-enum-routes-controllers",
        "title": "Hafta 4: Routes ve CRUD",
        "slides": [
            {
                "title": "Hafta 4 — Routes",
                "lines": ["URL → Controller aksiyonu", "config/routes.rb"],
                "say": "Hafta dort routes ve controller konusu. Routes dosyasi URL isteklerini dogru controller aksiyonuna yonlendirir.",
            },
            {
                "title": "HTTP Metotlari",
                "lines": [
                    "GET → oku",
                    "POST → olustur",
                    "PATCH/PUT → guncelle",
                    "DELETE → sil",
                ],
                "say": "GET veri okur. POST yeni kayit olusturur. PATCH veya PUT gunceller. DELETE siler. Sinavda bu eslesmeyi bilmen gerekir.",
            },
            {
                "title": "resources :posts",
                "lines": [
                    "7 CRUD route otomatik",
                    "index, show, new, create",
                    "edit, update, destroy",
                ],
                "say": "Resources posts yazarak yedi CRUD route otomatik olusur: index, show, new, create, edit, update ve destroy.",
            },
            {
                "title": "Enum ve ERB",
                "lines": [
                    "enum status: { draft: 0 }",
                    "ERB: <% %> kod, <%= %> cikti",
                    "@post controller'dan view'a",
                ],
                "say": "Enum sayisal degerlere anlamli isim verir, ornegin draft sifir. ERB sablonlarinda yuzde isareti kod, esittir isareti cikti icin kullanilir. Controller degiskenleri view'a at ile gider.",
            },
        ],
    },
    {
        "num": 5,
        "sid": "hafta-5-form-helpers-strong-parameters",
        "title": "Hafta 5: Formlar ve Guvenlik",
        "slides": [
            {
                "title": "Hafta 5 — Formlar",
                "lines": ["form_with model: @post", "Kullanicidan veri alma"],
                "say": "Hafta bes form helpers ve guvenlik. Form with model ile kullanicidan veri alirsin.",
            },
            {
                "title": "Strong Parameters",
                "lines": [
                    "params.require(:post).permit(...)",
                    "Sadece izinli alanlar gecer",
                    "Mass assignment saldirisini onler",
                ],
                "say": "Strong Parameters sadece izin verdigi alanlari kabul eder. Bu mass assignment saldirisini onler. Post params icinde require ve permit kullanilir.",
            },
            {
                "title": "Partial ve DRY",
                "lines": [
                    "_form.html.erb → partial",
                    "before_action → ortak kod",
                    "button_to → DELETE formu",
                ],
                "say": "Partial dosyalar alt cizgi ile baslar ve tekrar eden form kodunu azaltir. Before action ortak controller kodunu tek yerde toplar. Button to DELETE istegi icin form olusturur.",
            },
            {
                "title": "CSRF Korumasi",
                "lines": [
                    "authenticity_token",
                    "Form guvenligi",
                ],
                "say": "Her formda authenticity token vardir. Bu CSRF saldirilarina karsi koruma saglar.",
            },
        ],
    },
    {
        "num": 6,
        "sid": "hafta-6-bootstrap-frontend",
        "title": "Hafta 6: Bootstrap Frontend",
        "slides": [
            {
                "title": "Hafta 6 — Bootstrap",
                "lines": ["Responsive arayuz", "12 sutun grid sistemi"],
                "say": "Hafta alti Bootstrap ile frontend duzenleme. Bootstrap responsive bir CSS frameworkudur.",
            },
            {
                "title": "Grid Sistemi",
                "lines": [
                    "container → ortalanmis",
                    "row + col-md-6 → yarim genislik",
                    "col-md-4 → ucde bir",
                ],
                "say": "Container icerigi ortalar. Row satir, col sutundur. Col md alti ekranin yarisi demektir. On iki sutunluk grid sistemi kullanilir.",
            },
            {
                "title": "Bilesenler",
                "lines": [
                    "navbar → ust menu",
                    "card → icerik kutusu",
                    "btn → buton stilleri",
                ],
                "say": "Navbar ust menu, card icerik kutusu, btn buton siniflaridir. Navbar ve footer genelde partial olarak layouta eklenir.",
            },
        ],
    },
    {
        "num": 7,
        "sid": "hafta-7-model-iliskileri-kategori",
        "title": "Hafta 7: Model Iliskileri",
        "slides": [
            {
                "title": "Hafta 7 — Iliskiler",
                "lines": ["Tablolar arasi baglanti", "Active Record associations"],
                "say": "Hafta yedi model iliskileri. Veritabani tablolari arasinda baglanti kurarsin.",
            },
            {
                "title": "belongs_to ve has_many",
                "lines": [
                    "belongs_to → FK bu tabloda",
                    "has_many → karsi tarafta cok",
                    "Post belongs_to :category",
                ],
                "say": "Belongs to yabanci anahtarin bulundugu taraftir. Has many karsi tarafta birden cok kayit demektir. Ornegin post bir kategoriye aittir.",
            },
            {
                "title": "HABTM ve Scaffold",
                "lines": [
                    "has_and_belongs_to_many",
                    "Ara tablo, id yok",
                    "scaffold → hizli CRUD",
                ],
                "say": "Has and belongs to many coktan coga iliski icin ara tablo kullanir, ara tabloda id olmaz. Scaffold ile model, view ve controller hizlica olusturulur.",
            },
        ],
    },
    {
        "num": 8,
        "sid": "hafta-8-validation-active-storage",
        "title": "Hafta 8: Validation ve Active Storage",
        "slides": [
            {
                "title": "Hafta 8 — Validation",
                "lines": ["Modelde veri kurallari", "Kaydetmeden once kontrol"],
                "say": "Hafta sekiz validation ve dosya yukleme. Modelde veri kurallarini tanimlarsin.",
            },
            {
                "title": "validates Kurallari",
                "lines": [
                    "presence → bos olamaz",
                    "uniqueness → tekil",
                    "length → uzunluk siniri",
                ],
                "say": "Presence alanin bos olamayacagini, uniqueness tekil olmasini, length ise uzunluk sinirini belirler. Gecersiz kayit save ile kaydedilmez.",
            },
            {
                "title": "normalizes ve Active Storage",
                "lines": [
                    "normalizes → kaydetmeden duzenle",
                    "has_one_attached :image",
                    "Resim yukleme",
                ],
                "say": "Normalizes veriyi kaydetmeden once duzenler, ornegin bosluk siler. Active Storage ile has one attached image kullanarak resim yuklersin.",
            },
        ],
    },
    {
        "num": 9,
        "sid": "hafta-9-i18n-friendlyid-action-text",
        "title": "Hafta 9: I18n ve Gems",
        "slides": [
            {
                "title": "Hafta 9 — I18n",
                "lines": ["Coklu dil destegi", "locale/tr.yml, en.yml"],
                "say": "Hafta dokuz yerellestirme ve gem paketleri. I18n ile coklu dil destegi saglanir.",
            },
            {
                "title": "Ceviri ve Locale",
                "lines": [
                    "I18n.t('posts.title')",
                    "?locale=en → dil degistir",
                ],
                "say": "I18n nokta t ile ceviri metni alirsin. Soru isareti locale esittir en ile dili degistirirsin. Metinler YAML dosyalarinda tutulur.",
            },
            {
                "title": "FriendlyId ve Action Text",
                "lines": [
                    "FriendlyId → SEO slug URL",
                    "/posts/baslik-slug",
                    "Action Text → zengin editor",
                ],
                "say": "FriendlyId bir numara yerine okunabilir slug URL olusturur. Action Text ise zengin metin editoru saglar, kalin yazi ve liste ekleyebilirsin.",
            },
        ],
    },
    {
        "num": 10,
        "sid": "hafta-10-devise-authorization",
        "title": "Hafta 10: Devise ve Yetkilendirme",
        "slides": [
            {
                "title": "Hafta 10 — Devise",
                "lines": ["Kullanici girisi", "Kayit, sifre sifirlama"],
                "say": "Hafta on Devise ile kimlik dogrulama ve yetkilendirme. Devise kayit ol, giris yap ve sifre sifirlama islemlerini hazir verir.",
            },
            {
                "title": "Authentication vs Authorization",
                "lines": [
                    "Authentication → kimlik (Devise)",
                    "Authorization → yetki (admin?)",
                    "authenticate_user! → giris zorunlu",
                ],
                "say": "Authentication kim oldugunu sorar, Devise bunu yapar. Authorization ne yapabilecegini belirler. Authenticate user bang giris zorunlu kilar.",
            },
            {
                "title": "current_user",
                "lines": [
                    "current_user.posts.new",
                    "Post kullaniciya atanir",
                    "Rol bazli erisim",
                ],
                "say": "Current user ile oturum acmis kullaniciya erisirsin. Yeni post olustururken current user nokta posts nokta new ile post kullaniciya atanir. Admin ve user rolleri ile yetki kontrol edilir.",
            },
        ],
    },
]
