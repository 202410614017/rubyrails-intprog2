# -*- coding: utf-8 -*-
"""
Ruby resmi SSS (ruby-lang.org/documentation/faq) iceriginin Turkce ozetleri.
Kaynak: https://www.ruby-lang.org/en/documentation/faq/
Her konu icin ilgili FAQ bolumu ve Turkce aciklama.
"""

FAQ_BASE = "https://www.ruby-lang.org/en/documentation/faq"

RUBY_FAQ_BY_ID = {
    "kapsulleme": {
        "section": 7,
        "section_title": "Metotlar",
        "question": "Nesnenin instance variable'larina erisebilir miyim?",
        "answer": (
            "@ ile baslayan instance variable'lar nesnenin icindedir ve disaridan dogrudan "
            "okunamaz — bu iyi kapsullemeyi destekler. Ruby, bu degiskenlere kontrollu erisim "
            "icin attr_reader (sadece okuma), attr_writer (sadece yazma) ve attr_accessor "
            "(ikisi birden) tanimlamayi kolaylastirir. Kendi getter/setter metotlarinizi da "
            "yazabilirsiniz (ornegin dogrulama icin). attr_reader :name ile p.name cagrisi "
            "bir metot cagrisidir; @name dogrudan disaridan erisilemez."
        ),
        "url": f"{FAQ_BASE}/7/",
    },
    "kalitim": {
        "section": 7,
        "section_title": "Metotlar",
        "question": "Ruby hangi metodu cagirmaya karar verir? (Kalitim / miras)",
        "answer": (
            "Ruby tum mesajlari metotlara dinamik olarak baglar. Once alicinin singleton "
            "metotlarina, sonra kendi sinifindaki metotlara, en son ust siniflara ve karistirilan "
            "(include) modullere bakar. ClassName.ancestors bu arama sirasini gosterir. "
            "Ust siniftaki ayni isimli metodu cagirmak icin super kullanilir. Modul eklemek "
            "icin include arama zincirinin sonuna ekler; ust siniftaki metodu ezmek icin "
            "prepend onune ekler."
        ),
        "url": f"{FAQ_BASE}/7/",
    },
    "polimorfizm": {
        "section": 2,
        "section_title": "Karsilastirmalar",
        "question": "Ruby saf nesne yonelimli bir dil mi?",
        "answer": (
            "Ruby, prosedurel gibi gorunen ama aslinda tamamen nesne yonelimli bir dildir. "
            "Fonksiyon yoktur, yalnizca metot cagrilari vardir. class disinda yazilan def "
            "aslında Object sinifina ait bir metot tanimlar. Her sey nesnedir; ayni metot adi "
            "farkli siniflarda farkli davranis gosterdiginde (override) polimorfizm ortaya cikar."
        ),
        "url": f"{FAQ_BASE}/2/",
    },
    "mvc": {
        "section": 1,
        "section_title": "Genel Sorular",
        "question": "Ruby nedir ve hangi ozelliklere sahiptir?",
        "answer": (
            "Ruby, Yukihiro Matsumoto (Matz) tarafindan yazilmis guclu bir nesne yonelimli "
            "dildir. Siniflar, metotlar, nesneler, mixin'ler, singleton metotlar, istisna "
            "yakalama, iterator'lar ve closure'lar icerir. Rails MVC yapisi Ruby'nin bu OOP "
            "temeli uzerine kurulur: Controller ve Model siniflari, View ise ERB ile Ruby kodu "
            "calistirir."
        ),
        "url": f"{FAQ_BASE}/1/",
    },
    "symbol": {
        "section": 6,
        "section_title": "Sozdizimi",
        "question": ":name ne anlama gelir?",
        "answer": (
            "Isimden once gelen iki nokta (:name) bir Symbol nesnesi uretir. Program calisirken "
            "ayni isim icin hep ayni Symbol nesnesi kullanilir. Symbol'ler metot, degisken ve "
            "benzeri tanimlayicilari temsil eder. Hash anahtarlari icin sik kullanilir cunku "
            "String her seferinde yeni nesne olustururken Symbol tektir — bellek tasarrufu saglar. "
            "Rails enum ve params key'lerinde :draft gibi symbol'ler bu yuzden tercih edilir."
        ),
        "url": f"{FAQ_BASE}/6/",
    },
    "orm": {
        "section": 1,
        "section_title": "Genel Sorular",
        "question": "Ruby'de her sey nesne midir?",
        "answer": (
            "Ruby tam entegre bir nesne yonelimli dildir. Active Record ORM'de posts tablosu "
            "Post sinifine karsilik gelir; Post.create ve Post.all gibi cagrilar aslinda Post "
            "sinifina gonderilen mesajlardir (metot cagrisi). Veritabani satiri Ruby nesnesi "
            "olarak temsil edilir — SQL yerine nesne uzerinden islem yapilir."
        ),
        "url": f"{FAQ_BASE}/1/",
    },
    "migration": {
        "section": 7,
        "section_title": "Metotlar",
        "question": "Ruby'de sinif tanimi ve metotlar nasil calisir?",
        "answer": (
            "Migration dosyalari Ruby sinifidir: class AddStatusToPosts < ActiveRecord::Migration "
            "kalitim kullanir. change, up, down metotlari Ruby metotlaridir. Rails db:migrate "
            "komutu bu siniflari yukler ve change metodunu cagirir. Ruby FAQ'ye gore metot "
            "secimi kalitim zincirinde (ancestors) yapilir; Migration sinifi ust siniftan "
            "add_column gibi metotlari miras alir."
        ),
        "url": f"{FAQ_BASE}/7/",
    },
    "find-where": {
        "section": 7,
        "section_title": "Metotlar",
        "question": "Ruby hangi metodu cagirir?",
        "answer": (
            "Post.find(1), Post.find_by(title: 'x') ve Post.where(status: 1) cagrilarinin "
            "hepsi Ruby'nin dinamik metot baglama kurallarina tabidir. find bulunamazsa "
            "exception firlatir; find_by nil doner — bunlar Active Record'un metot tanimlaridir. "
            "where ise Relation nesnesi dondurur; sonuc uzerinde order, limit gibi metotlar "
            "zincirlenebilir (her biri yeni mesaj / metot cagrisi)."
        ),
        "url": f"{FAQ_BASE}/7/",
    },
    "enum": {
        "section": 6,
        "section_title": "Sozdizimi",
        "question": "Symbol hash anahtari olarak nasil kullanilir?",
        "answer": (
            "Ruby FAQ: Symbol'ler hash anahtari icin idealdir — { name: 'Jane', age: 24 } "
            "sozdizimi symbol key kullanir. Rails enum status: { draft: 0, published: 1 } "
            "tanimi veritabaninda integer saklar, Ruby tarafinda :draft gibi symbol isimleri "
            "kullanir. draft? ve published! yardimci metotlari otomatik uretilir."
        ),
        "url": f"{FAQ_BASE}/6/",
    },
    "http-crud": {
        "section": 7,
        "section_title": "Metotlar",
        "question": "+, -, * ... operator mu metot mu?",
        "answer": (
            "Ruby FAQ: +, - ve benzeri operator degil, metot cagrisidir; yeniden tanimlanabilir. "
            "Rails routes da HTTP istegini Controller'daki index, show, create gibi metotlara "
            "yönlendirir. resources :posts tek satirda yedi CRUD metodu icin yol olusturur — "
            "GET okuma, POST olusturma, PATCH guncelleme, DELETE silme."
        ),
        "url": f"{FAQ_BASE}/7/",
    },
    "erb": {
        "section": 5,
        "section_title": "Iterator'lar",
        "question": "Blok nedir ve ERB ile iliskisi?",
        "answer": (
            "Iterator, blok veya Proc kabul eden metottur; blok metot cagrisindan hemen sonra "
            "yazilir. ERB sablonlari da gomulu Ruby kodu calistirir: <% %> kod calistirir, "
            "<%= %> sonucu yazar. View'daki each donguleri FAQ'deki data.each { |i| puts i } "
            "ornegiyle ayni blok mantigini kullanir."
        ),
        "url": f"{FAQ_BASE}/5/",
    },
    "strong-parameters": {
        "section": 4,
        "section_title": "Degiskenler ve Argumanlar",
        "question": "Argumanlar nasil gecirilir?",
        "answer": (
            "Ruby'de gercek arguman formal argumana atanir; nesne referansi kopyalanir, "
            "nesnenin kendisi degil. params.require(:post).permit(:title, :body) yalnizca "
            "izin verilen alanlari yeni Post nesnesine gecirir — kotu niyetli ek alanlar "
            "(admin: true gibi) atanamaz. Bu, Ruby'nin arguman gecirme modeli uzerine "
            "Rails guvenlik katmanidir."
        ),
        "url": f"{FAQ_BASE}/4/",
    },
    "form-with": {
        "section": 5,
        "section_title": "Iterator'lar",
        "question": "Blok iterator'a nasil gecirilir?",
        "answer": (
            "Blok, iterator cagrisindan hemen sonra yazilir. form_with model: @post do |f| ... "
            "end yapisinda |f| blogu form builder nesnesini alir — FAQ'deki each { |i| ... } "
            "ornegiyle ayni mantik. before_action gibi callback'ler de Ruby metotlaridir."
        ),
        "url": f"{FAQ_BASE}/5/",
    },
    "bootstrap-grid": {
        "section": 1,
        "section_title": "Genel Sorular",
        "question": "Ruby ile sunucu ve arayuz nasil birlikte calisir?",
        "answer": (
            "Bootstrap CSS/HTML katmanidir; Ruby FAQ dogrudan Bootstrap anlatmaz. Ancak Rails "
            "view'larinda ERB ile Ruby kodu calistirilirken HTML sinifleri (container, row, col) "
            "statik icerik olarak yazilir. Ruby'nin gorevi veriyi hazirlamak (@posts), Bootstrap "
            "in gorunumu duzenlemektir."
        ),
        "url": f"{FAQ_BASE}/1/",
    },
    "associations": {
        "section": 7,
        "section_title": "Metotlar",
        "question": "Modul include / prepend ve kalitim zinciri",
        "answer": (
            "belongs_to ve has_many Rails iliskileridir; altta yatan Ruby kavrami kalitim ve "
            "modul karistirmadir. FAQ: include modulu ancestors zincirine ekler; prepend onune "
            "koyarak ust sinif metodunu ezebilirsiniz. post.category.name cagrisi once Post'ta, "
            "gerekirse ust siniflarda category metodunu arar."
        ),
        "url": f"{FAQ_BASE}/7/",
    },
    "habtm": {
        "section": 2,
        "section_title": "Karsilastirmalar",
        "question": "Mixin (modul karistirma) nedir?",
        "answer": (
            "Ruby tek kalitim destekler ama guclu mixin kavramina sahiptir: sinif tanimina modul "
            "dahil edilince o modulun metotlari sinifa eklenir. has_and_belongs_to_many iki model "
            "arasinda coktan coga baglanti kurar; join tablosu ara nesne gibi davranir. "
            "Ek ozellik gerekiyorsa has_many :through tercih edilir."
        ),
        "url": f"{FAQ_BASE}/2/",
    },
    "validation": {
        "section": 7,
        "section_title": "Metotlar",
        "question": "Yikici (destructive) metot nedir?",
        "answer": (
            "Yikici metot nesnenin durumunu degistirir. String'de str ve str! farki gibi: "
            "validates kurallari gecmezse save false doner ve errors dolar — nesne durumu "
            "kaydedilmez. downcase! gibi ! ile biten metotlar aliciyi yerinde degistirir; "
            "validation gecersiz kaydi veritabanina yazmaz."
        ),
        "url": f"{FAQ_BASE}/7/",
    },
    "normalizes": {
        "section": 4,
        "section_title": "Degiskenler ve Argumanlar",
        "question": "Atama nesnenin kopyasini mi uretir?",
        "answer": (
            "Ruby FAQ: Atama tek basina yeni nesne kopyasi olusturmaz; degiskenler nesneye "
            "referans tutar. normalizes email'i kaydetmeden once strip.downcase ile donusturur — "
            "validation'dan once calisir. Ayni referans mantigi: b.concat('d') cagrisi a ve A "
            "degiskenlerinin de gosterdigi nesneyi degistirebilir."
        ),
        "url": f"{FAQ_BASE}/4/",
    },
    "active-storage": {
        "section": 4,
        "section_title": "Degiskenler ve Argumanlar",
        "question": "Nesnem beklenmedik sekilde neden degisti?",
        "answer": (
            "Degiskenler nesneye referans tutar; a = b = 'abc' sonrasinda b.concat('d') hem "
            "a'yi hem b'yi etkiler. has_one_attached :image dosyayi modele baglar; "
            "attached? ile kontrol edilir. Parametre gecirme de referans oldugu icin "
            "formdan gelen dosya nesnesi uzerinde islem yapilir."
        ),
        "url": f"{FAQ_BASE}/4/",
    },
    "i18n": {
        "section": 6,
        "section_title": "Sozdizimi",
        "question": "Symbol sabit veya enum degeri olarak",
        "answer": (
            "FAQ: status = :open veya NORTH = :NORTH gibi Symbol'ler sabit veya enum degeri "
            "olarak kullanilabilir. I18n.t('posts.title') ceviri anahtarini string olarak alir; "
            "locale=:en gibi symbol parametreler dil seciminde kullanilir."
        ),
        "url": f"{FAQ_BASE}/6/",
    },
    "friendly-id": {
        "section": 6,
        "section_title": "Sozdizimi",
        "question": "Symbol ile metot cagrisi (send)",
        "answer": (
            "Symbol bir metoda karsilik geliyorsa demo.send(:hello) ile cagrilabilir. "
            "FriendlyId slug uretir; Post.friendly.find(params[:id]) find metodunun slug "
            "versiyonunu kullanir. Symbol'ler metot adlarini temsil etmek icin idealdir."
        ),
        "url": f"{FAQ_BASE}/6/",
    },
    "action-text": {
        "section": 4,
        "section_title": "Degiskenler ve Argumanlar",
        "question": "Formal arguman uzerinden metot cagirma",
        "answer": (
            "Ruby'de tum degiskenler nesneye referanstir; has_rich_text :content iliskisi "
            "kurulunca content uzerinden metot cagrilari yapilir. rich_text_area form helper'i "
            "Trix editor ile HTML icerigi nesneye baglar."
        ),
        "url": f"{FAQ_BASE}/4/",
    },
    "devise": {
        "section": 7,
        "section_title": "Metotlar",
        "question": "Bu basit fonksiyon benzeri metotlar nereden geliyor?",
        "answer": (
            "class disinda yazilan def aslinda Object sinifina ait metottur; self gizli alicidir. "
            "Devise User modeline modul ekleyerek sign_in, current_user gibi metotlari "
            "Controller'a getirir. authenticate_user! cagrilmazsa yonlendirme yapilir — "
            "Ruby'de her sey metot mesajidir."
        ),
        "url": f"{FAQ_BASE}/7/",
    },
    "authorization": {
        "section": 7,
        "section_title": "Metotlar",
        "question": "private ve protected arasindaki fark nedir?",
        "answer": (
            "private: metot yalnizca fonksiyon formunda (alici yazilmadan) cagrilabilir; "
            "other.foo seklinde baska nesnede cagrilamaz. protected: kendi sinifi ve alt "
            "siniflar icinden alici ile cagrilabilir (ornegin age <=> other.age). "
            "Authorization: current_user.admin? ile yetki kontrolu — authentication (Devise) "
            "kim oldugunu, authorization ne yapabilecegini belirler."
        ),
        "url": f"{FAQ_BASE}/7/",
    },
    "bloklar": {
        "section": 5,
        "section_title": "Iterator'lar",
        "question": "Iterator nedir?",
        "answer": (
            "Iterator, blok veya Proc kabul eden metottur. [1,2,3].each { |n| puts n } "
            "orneginde each iterator'dur. Blok do/end veya { } ile yazilir. yield metot "
            "icinden blogu cagirir; & parametresi blogu Proc'a cevirir. Proc arguman sayisina "
            "toleransli, lambda katidir."
        ),
        "url": f"{FAQ_BASE}/5/",
    },
}


def attach_ruby_faq_to_topics(topics: list) -> None:
    """TOPICS listesindeki her ogeye ruby_faq alanini ekler."""
    for topic in topics:
        faq = RUBY_FAQ_BY_ID.get(topic["id"])
        if faq:
            topic["ruby_faq"] = faq
            faq_source = {
                "name": f"Ruby Resmi SSS — Bolum {faq['section']} ({faq['section_title']})",
                "url": faq["url"],
            }
            sources = topic.get("sources", [])
            if not any(s.get("url") == faq["url"] for s in sources):
                topic["sources"] = [faq_source] + sources
