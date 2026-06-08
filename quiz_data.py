# -*- coding: utf-8 -*-
"""Sinav test sorulari ve detayli cevaplar."""

QUIZ = [
    {
        "week": 2,
        "title": "Ruby Temelleri",
        "items": [
            {
                "q": "Ruby'de 3.class.superclass.superclass ne doner?",
                "a": "Object doner. Hiyerarsi: Integer → Numeric → Object → BasicObject. Yani 3 bir Integer nesnesidir ve ust sinifi Numeric, onun ust sinifi Object'tir.",
            },
            {
                "q": "Symbol ile String arasindaki temel fark nedir?",
                "a": "Symbol (:user) tekil bir nesnedir; ayni sembol her zaman ayni object_id'ye sahiptir. String her olusturuldugunda yeni bir nesne yaratir. Semboller genelde hash key ve sabit isimler icin kullanilir.",
            },
            {
                "q": "attr_accessor, attr_reader, attr_writer farklari?",
                "a": "attr_reader: sadece okuma (getter). attr_writer: sadece yazma (setter). attr_accessor: hem getter hem setter olusturur. Ornek: attr_accessor :name ile hem name hem name= kullanilabilir.",
            },
            {
                "q": "Proc ile Lambda arasindaki arguman farki?",
                "a": "Proc fazla veya eksik argumanda hata vermez (eksigi nil sayar, fazlasini yok sayar). Lambda arguman sayisina katidir; yanlis sayida arguman verilirse ArgumentError olusur.",
            },
            {
                "q": "? ve ! ile biten metotlarin anlami?",
                "a": "? ile biten metotlar boolean doner (even?, zero?). ! ile biten metotlar destructive/tehlikeli islem yapar; orijinal veriyi degistirir (upcase! gibi).",
            },
        ],
    },
    {
        "week": 3,
        "title": "ORM & Active Record",
        "items": [
            {
                "q": "ORM'in avantajlari nelerdir?",
                "a": "Daha az SQL yazilir, nesne yonelimli calisilir, veritabani platformundan bagimsizlik saglanir (PostgreSQL'den MySQL'e gecis kolay), modelleme uygulama tarafinda yapilir, bakim maliyeti dusuktur.",
            },
            {
                "q": "find, find_by ve where arasindaki fark?",
                "a": "find(id): id ile arar, bulamazsa exception firlatir. find_by(...): tek kayit veya nil doner. where(...): sifir veya cok kayit donen ActiveRecord::Relation nesnesi doner.",
            },
            {
                "q": "save ile create arasindaki fark?",
                "a": "Post.new ile once nesne olusturulur, save ile kaydedilir (iki adim). Post.create ile nesne olusturulur ve aninda veritabanina yazilir (tek adim).",
            },
            {
                "q": "db:setup ile db:reset ne yapar?",
                "a": "db:setup = schema:load + seed (sema yuklenir, seed verisi eklenir). db:reset = db:drop + setup (veritabani silinir, sifirdan olusturulur ve seed eklenir).",
            },
            {
                "q": "Migration rollback nasil yapilir?",
                "a": "rails db:rollback komutu son migration'i geri alir. rails db:migrate:status ile durum kontrol edilir. STEP parametresi ile birden fazla migration geri alinabilir.",
            },
        ],
    },
    {
        "week": 4,
        "title": "Routes & HTTP",
        "items": [
            {
                "q": "GET ve POST ne zaman kullanilir?",
                "a": "GET: veri okumak icin (sayfa gosterme, listeleme). POST: yeni kayit olusturmak icin (form gonderme). GET ile hassas veri gonderilmemeli.",
            },
            {
                "q": "PUT ile PATCH farki?",
                "a": "PUT kaynagin tum alanlarini gunceller. PATCH sadece degisen alanlari gunceller (kismi guncelleme). Ikisi de mevcut kaydi guncellemek icin kullanilir.",
            },
            {
                "q": "resources :posts kac route olusturur? Isimleri?",
                "a": "7 CRUD route: index, show, new, create, edit, update, destroy. Ornek: GET /posts (index), GET /posts/:id (show), POST /posts (create), DELETE /posts/:id (destroy).",
            },
            {
                "q": "posts_path ile posts_url farki?",
                "a": "posts_path sadece yol doner: /posts. posts_url tam URL doner: http://localhost:3000/posts (protokol + host + port dahil).",
            },
            {
                "q": "Enum'da draft: 0 ne anlama gelir?",
                "a": "Veritabaninda status alani 0 olarak saklanir, Ruby tarafinda draft anlamina gelir. Yeni kayit default 0 ise otomatik draft olur. post.draft? ve Post.draft scope kullanilabilir.",
            },
        ],
    },
    {
        "week": 5,
        "title": "Formlar & Guvenlik",
        "items": [
            {
                "q": "Strong Parameters neden gerekli?",
                "a": "Mass assignment saldirisini onler. Sadece izin verilen alanlar (permit) modele aktarilir. Ornek: params.require(:post).permit(:title, :article) — baska alanlar yok sayilir.",
            },
            {
                "q": "authenticity_token ne ise yarar?",
                "a": "CSRF (Cross-Site Request Forgery) korumasi saglar. Formda hidden field olarak gonderilir, Rails oturumdaki token ile karsilastirir. Eslesmezse istek reddedilir.",
            },
            {
                "q": "Partial dosya adlandirma kurali?",
                "a": "Partial dosya adi _ ile baslar: _form.html.erb. render 'form' veya render partial: 'form' ile cagrilir. Ayni formu new ve edit sayfalarinda tekrar kullanmak icin idealdir.",
            },
            {
                "q": "button_to ile link_to farki (DELETE icin)?",
                "a": "link_to sadece link olusturur; DELETE icin ek ayar gerekir. button_to kendi mini formunu olusturur, _method=delete hidden field ekler — silme islemi icin daha guvenli ve standart.",
            },
            {
                "q": "before_action ne saglar?",
                "a": "DRY prensibi: tekrarlayan kodu action'lardan once calistirir. Ornek: before_action :set_post, only: [:show, :edit, :update] — @post her action'da otomatik yuklenir.",
            },
        ],
    },
    {
        "week": 6,
        "title": "Bootstrap",
        "items": [
            {
                "q": "Bootstrap grid kac sutundur?",
                "a": "12 sutunludur. Ornek: col-4 + col-4 + col-4 = 12, yan yana 3 esit sutun. col-8 + col-4 = 12, genis + dar sutun.",
            },
            {
                "q": ".container ile .container-fluid farki?",
                "a": "container: ekran genisligine gore max-width sinirli (ortalanmis). container-fluid: her zaman %100 genislik, sinir yok.",
            },
            {
                "q": "col-md-8 ne zaman yan yana, ne zaman alt alta?",
                "a": "768px ve uzeri ekranlarda yan yana durur. 768px altinda (mobil) sutunlar otomatik ust uste yigilir (responsive).",
            },
        ],
    },
    {
        "week": 7,
        "title": "Model Iliskileri",
        "items": [
            {
                "q": "belongs_to FK hangi tabloda?",
                "a": "Foreign key, belongs_to tanimlanan modelin tablosundadir. Ornek: Book belongs_to :author → books tablosunda author_id sutunu vardir.",
            },
            {
                "q": "has_many :through ne zaman kullanilir?",
                "a": "Iki model arasinda ara (join) tablo oldugunda. Ornek: Physician has_many :patients, through: :appointments — randevu tablosu uzerinden doktor-hasta iliskisi.",
            },
            {
                "q": "HABTM join table ozelligi?",
                "a": "id sutunu yoktur (id: false). Sadece iki foreign key icerir (post_id, category_id). Post ve Category coktan coga baglanir. Ornek: categories_posts tablosu.",
            },
            {
                "q": "dependent: :destroy ne yapar?",
                "a": "Ust kayit silindiginde bagli alt kayitlari da otomatik siler. Ornek: Author silinince has_many :books, dependent: :destroy ile kitaplari da silinir.",
            },
        ],
    },
    {
        "week": 8,
        "title": "Validation & Storage",
        "items": [
            {
                "q": "Validation ile Normalization farki?",
                "a": "Validation veriyi kontrol eder, gecersizse reddeder (save basarisiz). Normalization veriyi kaydetmeden once degistirir (squish, titlecase) — reddetmez, duzenler.",
            },
            {
                "q": "create! ile create farki?",
                "a": "create basarisiz olursa false doner veya hatali nesne doner. create! basarisiz olursa exception firlatir (ActiveRecord::RecordInvalid). ! isareti exception garantisi verir.",
            },
            {
                "q": "validates :title, presence: true, uniqueness: true, length: { maximum: 255 } ne kontrol eder?",
                "a": "Baslik bos olamaz, benzersiz olmali (ayni baslikla ikinci kayit olamaz) ve en fazla 255 karakter olabilir.",
            },
            {
                "q": "HTTP 422 ne anlama gelir?",
                "a": "Unprocessable Entity — sunucu istegi anladi ama validasyon hatalari nedeniyle isleyemedi. render :new, status: :unprocessable_entity ile form hatalari gosterilir.",
            },
        ],
    },
    {
        "week": 9,
        "title": "I18n & Gems",
        "items": [
            {
                "q": "I18n.t ve I18n.l farki?",
                "a": "I18n.t (translate): metin cevirir — buton, label, mesaj. I18n.l (localize): tarih ve saat nesnelerini yerel formata cevirir. Ornek: t('actions.show'), l(Time.now).",
            },
            {
                "q": "FriendlyId ne saglar?",
                "a": "URL'de id yerine okunabilir slug kullanir. /posts/1 yerine /posts/ruby-programlamaya-giris. SEO icin faydalidir. friendly_id :title, use: :slugged",
            },
            {
                "q": "Action Text ne icin kullanilir?",
                "a": "Zengin metin editoru (WYSIWYG) saglar — kalin, italik, liste, resim ekleme. has_rich_text :article ve form.rich_textarea :article ile kullanilir.",
            },
        ],
    },
    {
        "week": 10,
        "title": "Devise & Yetki",
        "items": [
            {
                "q": "Authentication ile Authorization farki?",
                "a": "Authentication (kimlik dogrulama): Kullanici kim? — giris yapma. Authorization (yetkilendirme): Ne yapabilir? — giris sonrasi erisim hakki. Devise authentication, Pundit/CanCanCan authorization icin.",
            },
            {
                "q": "current_user ve user_signed_in? ne doner?",
                "a": "current_user: giris yapmis User nesnesini doner (yoksa nil). user_signed_in?: boolean — true ise oturum acik, false ise acik degil.",
            },
            {
                "q": "authenticate_user! ne yapar?",
                "a": "Giris yapilmamissa kullaniciyi login sayfasina yonlendirir. before_action :authenticate_user! ile korumali sayfalar olusturulur.",
            },
            {
                "q": "Admin namespace'te yetki kontrolu nasil yapilir?",
                "a": "before_action :authorize_admin tanimlanir. unless current_user.admin? ise root_path'e redirect edilir. Sadece admin rolundekiler admin/users sayfalarina erisebilir.",
            },
            {
                "q": "current_user.posts.new neden kullanilir?",
                "a": "Post otomatik olarak giris yapan kullaniciya atanir. user_id elle gondermek yerine iliski uzerinden olusturma guvenli ve dogru yontemdir.",
            },
        ],
    },
]
