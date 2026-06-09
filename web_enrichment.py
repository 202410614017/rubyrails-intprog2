# -*- coding: utf-8 -*-
"""
PDF konu basliklari icin internet kaynakli derinlestirme icerigi.
Kaynaklar: ruby-lang.org, guides.rubyonrails.org, api.rubyonrails.org
"""

TOPICS = [
    {
        "id": "kapsulleme",
        "title": "Kapsulleme (Encapsulation)",
        "week": 2,
        "keywords": ["kapsul", "attr_accessor", "attr_reader", "attr_writer", "erisim"],
        "summary": "Instance variable (@) disaridan dogrudan okunamaz; getter/setter ile kontrollu erisim saglanir.",
        "explain": (
            "Ruby'de @ ile baslayan instance variable'lar nesnenin icindedir ve disaridan "
            "dogrudan erisilemez — bu iyi kapsullemeyi destekler. attr_reader sadece okuma, "
            "attr_writer sadece yazma, attr_accessor ikisini birden otomatik uretir. "
            "Resmi Ruby FAQ: instance variable'lara erisim icin bu accessor'lar tercih edilir."
        ),
        "code": """class Person
  attr_reader :name
  attr_accessor :age

  def initialize(name, age)
    @name = name
    @age = age
  end
end

p = Person.new("Ali", 20)
p.name      # => "Ali"  (okuma)
p.age = 21  # => 21     (yazma)""",
        "exam_tip": "Sinavda: @name gizli kalir, dis erisim attr_* ile yapilir. attr_reader = sadece oku.",
        "sources": [
            {"name": "Ruby Resmi FAQ — Accessors", "url": "https://www.ruby-lang.org/en/documentation/faq/7/"},
            {"name": "Ruby Module#attr_accessor API", "url": "https://docs.ruby-lang.org/en/master/Module.html#method-i-attr_accessor"},
        ],
    },
    {
        "id": "kalitim",
        "title": "Kalitim / Miras (Inheritance)",
        "week": 2,
        "keywords": ["kalitim", "miras", "inherit", "super", "class dog"],
        "summary": "Alt sinif ust siniftan ozellikleri alir; super ile ust sinif metodu cagrilir.",
        "explain": (
            "Ruby'de class Child < Parent ile kalitim kurulur. Alt sinif ust sinifin metotlarini "
            "kullanabilir veya override edebilir. super kelimesi ust siniftaki ayni metodu cagirir. "
            "Tek kalitim vardir (coklu kalitim yok); modul ile mixin kullanilir."
        ),
        "code": """class Animal
  def speak
    "Ses cikarir"
  end
end

class Dog < Animal
  def speak
    super + " — hav hav!"
  end
end

Dog.new.speak  # => "Ses cikarir — hav hav!""",
        "exam_tip": "class X < Y = X, Y'den turetilir. super = ust metod. Polimorfizm = ayni metod farkli davranis.",
        "sources": [
            {"name": "Ruby Classes Tutorial", "url": "https://www.ruby-lang.org/en/documentation/quickstart/3/"},
            {"name": "Ruby Inheritance (Learn Ruby)", "url": "https://rubylearning.com/satishtalim/ruby_inheritance.html"},
        ],
    },
    {
        "id": "polimorfizm",
        "title": "Polimorfizm",
        "week": 2,
        "keywords": ["polimorf", "override", "speak"],
        "summary": "Ayni metod adi farkli siniflarda farkli davranis gosterir.",
        "explain": (
            "Polimorfizm, ayni arayuzun (metod adinin) alt siniflarda farkli implementasyon "
            "sunmasidir. Ornegin speak metodu Animal'da genel, Dog'da 'hav', Cat'te 'miyav' doner. "
            "Ruby'de duck typing sayesinde 'ne olduguna degil, ne yapabildigine bakilir'."
        ),
        "code": """class Cat < Animal
  def speak
    "Miyav!"
  end
end

[Dog.new, Cat.new].each { |a| puts a.speak }""",
        "exam_tip": "Override = alt sinif ust metodu yeniden yazar. Polimorfizm sinavda genelde speak ornegiyle gelir.",
        "sources": [
            {"name": "Ruby OOP — Polymorphism", "url": "https://www.ruby-lang.org/en/documentation/"},
        ],
    },
    {
        "id": "mvc",
        "title": "MVC Mimarisi",
        "week": 2,
        "keywords": ["mvc", "model", "view", "controller", "routes"],
        "summary": "Model=veri, View=arayuz, Controller=istek isleme. Rails'in temel yapisi.",
        "explain": (
            "Rails MVC mimarisini kullanir. Tarayici istegi routes.rb uzerinden Controller'a gelir. "
            "Controller Model ile veritabanina erisir, sonucu View'a (@degisken) aktarir. "
            "View ERB sablonu HTML uretir. Resmi Rails rehberi bu akisi 'Getting Started' bolumunde anlatir."
        ),
        "code": """# config/routes.rb
resources :posts

# app/controllers/posts_controller.rb
def show
  @post = Post.find(params[:id])  # Model
end
# app/views/posts/show.html.erb  → View render""",
        "exam_tip": "Akis: Browser → Routes → Controller → Model → View. @post instance variable view'a gider.",
        "sources": [
            {"name": "Rails Guides — MVC", "url": "https://guides.rubyonrails.org/getting_started.html#mvc-architecture"},
            {"name": "Rails Routing", "url": "https://guides.rubyonrails.org/routing.html"},
        ],
    },
    {
        "id": "symbol",
        "title": "Symbol vs String",
        "week": 2,
        "keywords": ["symbol", "string", ":user"],
        "summary": "Symbol tekil ve degismez; String her seferinde yeni nesne. Hash key'lerde Symbol tercih edilir.",
        "explain": (
            "Symbol (:name) bellekte tektir, ayni sembol tekrar kullanildiginda ayni nesneye isaret eder. "
            "String her literal yeni nesne olusturur. Rails'de status: :published gibi enum ve hash key'lerde "
            "Symbol yaygindir. object_id ile fark gorulebilir."
        ),
        "code": """:a.object_id == :a.object_id  # => true
"a".object_id == "a".object_id  # => false (genelde)

user = { name: "Ali", role: :admin }
user[:name]  # => "Ali\"""",
        "exam_tip": "Symbol tekil, String cogaltilir. Rails enum ve params key'lerinde :draft gibi symbol kullanilir.",
        "sources": [
            {"name": "Ruby Symbol Documentation", "url": "https://docs.ruby-lang.org/en/master/Symbol.html"},
        ],
    },
    {
        "id": "orm",
        "title": "ORM (Object Relational Mapping)",
        "week": 3,
        "keywords": ["orm", "object relational", "tablo", "sinif"],
        "summary": "Veritabani tablosu = Ruby sinifi. SQL yazmadan CRUD yapilir.",
        "explain": (
            "ORM, iliskisel veritabani tablolarini nesne yonelimli siniflara esler. "
            "posts tablosu Post modeline karsilik gelir. Active Record Rails'in ORM katmanidir. "
            "Migration ile sema, model ile veri islemleri yonetilir."
        ),
        "code": """# db/migrate/xxx_create_posts.rb → posts tablosu
# app/models/post.rb
class Post < ApplicationRecord
end

Post.create(title: "Merhaba")
Post.all""",
        "exam_tip": "ORM = tablo ↔ sinif. Active Record = Rails ORM. SQL yazmadan Post.create, Post.all kullanilir.",
        "sources": [
            {"name": "Rails Active Record Basics", "url": "https://guides.rubyonrails.org/active_record_basics.html"},
        ],
    },
    {
        "id": "migration",
        "title": "Migration",
        "week": 3,
        "keywords": ["migration", "migrate", "rollback", "schema", "add_column"],
        "summary": "Veritabani semasini versiyonlu Ruby dosyalariyla degistirir.",
        "explain": (
            "Migration dosyalari db/migrate/ altindadir. up/down veya change metodu ile tablo "
            "olusturma, kolon ekleme yapilir. rails db:migrate bekleyen migrationlari uygular. "
            "db:rollback son migrationi geri alir. schema.rb guncel semayi tutar."
        ),
        "code": """# rails g migration AddStatusToPosts status:integer
class AddStatusToPosts < ActiveRecord::Migration[7.0]
  def change
    add_column :posts, :status, :integer, default: 0
  end
end

# Terminal: rails db:migrate""",
        "exam_tip": "db:migrate uygula, db:rollback geri al, db:reset sil+yeniden kur+seed. Migration dosyasi db/migrate/.",
        "sources": [
            {"name": "Rails Migration Guide", "url": "https://guides.rubyonrails.org/active_record_migrations.html"},
            {"name": "Rails db:migrate API", "url": "https://api.rubyonrails.org/classes/ActiveRecord/Migration.html"},
        ],
    },
    {
        "id": "find-where",
        "title": "find / find_by / where",
        "week": 3,
        "keywords": ["find", "find_by", "where", "first", "last"],
        "summary": "find id ile arar (hata), find_by kosul (nil), where filtre (liste/Relation).",
        "explain": (
            "Post.find(1) primary key ile arar; kayit yoksa ActiveRecord::RecordNotFound hatasi. "
            "Post.find_by(title: 'x') ilk esleseni doner, yoksa nil. "
            "Post.where(status: 1) ActiveRecord::Relation doner (lazy, zincirlenebilir)."
        ),
        "code": """Post.find(1)                    # hata verebilir
Post.find_by(title: "Rails")    # nil veya kayit
Post.where(status: :published)  # Relation
Post.where(status: 1).order(created_at: :desc).limit(5)""",
        "exam_tip": "find → exception, find_by → nil, where → koleksiyon. where sonucu uzerinde order/limit zincirlenir.",
        "sources": [
            {"name": "Active Record Query Interface", "url": "https://guides.rubyonrails.org/active_record_querying.html"},
        ],
    },
    {
        "id": "enum",
        "title": "Active Record Enum",
        "week": 4,
        "keywords": ["enum", "draft", "published", "status"],
        "summary": "Integer kolona anlamli isim verir; DB'de sayi, kodda symbol.",
        "explain": (
            "enum status: { draft: 0, published: 1 } ile status kolonuna isimler baglanir. "
            "post.draft? ve post.published! gibi yardimci metotlar otomatik olusur. "
            "Veritabaninda integer saklanir, Ruby tarafinda okunabilir."
        ),
        "code": """class Post < ApplicationRecord
  enum :status, { draft: 0, published: 1, archived: 2 }
end

post = Post.new
post.draft!
post.draft?       # => true
post.status       # => "draft\"""",
        "exam_tip": "enum status: { draft: 0 } — DB'de 0, kodda :draft. draft?, published! otomatik metotlar.",
        "sources": [
            {"name": "Rails Enum API", "url": "https://api.rubyonrails.org/classes/ActiveRecord/Enum.html"},
        ],
    },
    {
        "id": "http-crud",
        "title": "HTTP Metotlari ve CRUD",
        "week": 4,
        "keywords": ["http", "get", "post", "patch", "delete", "crud", "resources"],
        "summary": "GET okur, POST olusturur, PATCH gunceller, DELETE siler. resources 7 route uretir.",
        "explain": (
            "RESTful Rails uygulamalarinda HTTP metodu islemi belirler. "
            "resources :posts tek satirda index, show, new, create, edit, update, destroy "
            "route'larini olusturur. rails routes komutu ile listelenir."
        ),
        "code": """# config/routes.rb
resources :posts

# GET    /posts          → index
# GET    /posts/:id      → show
# POST   /posts          → create
# PATCH  /posts/:id      → update
# DELETE /posts/:id      → destroy""",
        "exam_tip": "GET=oku, POST=olustur, PATCH/PUT=guncelle, DELETE=sil. resources :posts = 7 CRUD route.",
        "sources": [
            {"name": "Rails Routing — REST", "url": "https://guides.rubyonrails.org/routing.html#restful-routing-the-rails-default"},
        ],
    },
    {
        "id": "erb",
        "title": "ERB Sablonlari",
        "week": 4,
        "keywords": ["erb", "<%", "<%=", "embedded"],
        "summary": "<% %> Ruby kodu calistirir, <%= %> ciktiyi HTML'e yazar.",
        "explain": (
            "ERB (Embedded Ruby) view dosyalarinda Ruby kodu calistirir. "
            "<% if @post %> sadece calistirir, <%= @post.title %> HTML'e escape edilmis cikti yazar. "
            "<%- -%> bosluk kirpma icin kullanilabilir."
        ),
        "code": """<%# yorum %>
<h1><%= @post.title %></h1>
<% @posts.each do |post| %>
  <p><%= link_to post.title, post %></p>
<% end %>""",
        "exam_tip": "<% %> kod, <%= %> cikti. @degisken controller'dan view'a gelir.",
        "sources": [
            {"name": "Rails Action View Overview", "url": "https://guides.rubyonrails.org/action_view_overview.html"},
        ],
    },
    {
        "id": "strong-parameters",
        "title": "Strong Parameters",
        "week": 5,
        "keywords": ["strong", "parameter", "permit", "require", "mass assignment"],
        "summary": "params icinden sadece izin verilen alanlar gecirilir; guvenlik icin zorunlu.",
        "explain": (
            "Strong Parameters mass assignment saldirisini onler. "
            "params.require(:post).permit(:title, :body) sadece title ve body'yi kabul eder. "
            "admin gibi ek alanlar permit edilmezse atanamaz."
        ),
        "code": """class PostsController < ApplicationController
  def create
    @post = Post.new(post_params)
    @post.save
  end

  private

  def post_params
    params.require(:post).permit(:title, :body, :status)
  end
end""",
        "exam_tip": "require(:post).permit(...) — izinli alanlar. CSRF icin authenticity_token formda otomatik.",
        "sources": [
            {"name": "Rails Strong Parameters Guide", "url": "https://guides.rubyonrails.org/action_controller_overview.html#strong-parameters"},
        ],
    },
    {
        "id": "form-with",
        "title": "form_with ve Partials",
        "week": 5,
        "keywords": ["form_with", "partial", "_form", "before_action"],
        "summary": "form_with model ile form olusturur; partial (_form) tekrari azaltir.",
        "explain": (
            "form_with model: @post otomatik action/method belirler (new→create, edit→update). "
            "Partial dosyalar _ ile baslar: render 'form'. before_action :set_post gibi "
            "callback'ler tekrar eden kodu controller'da toplar."
        ),
        "code": """<%# app/views/posts/_form.html.erb %>
<%= form_with model: @post do |f| %>
  <%= f.text_field :title %>
  <%= f.submit %>
<% end %>

<%# controller %>
before_action :set_post, only: [:show, :edit, :update, :destroy]""",
        "exam_tip": "Partial _ ile baslar. before_action DRY. button_to DELETE formu olusturur.",
        "sources": [
            {"name": "Rails Form Helpers", "url": "https://guides.rubyonrails.org/form_helpers.html"},
        ],
    },
    {
        "id": "bootstrap-grid",
        "title": "Bootstrap Grid",
        "week": 6,
        "keywords": ["bootstrap", "grid", "col-md", "container", "row"],
        "summary": "12 sutunluk responsive grid; container, row, col-* siniflari.",
        "explain": (
            "Bootstrap 5 grid sistemi 12 sutun uzerinden calisir. container icerigi ortalar, "
            "row satir, col-md-6 medium ekranda yarim genislik demektir. "
            "Rails 7+ ile rails new --css bootstrap veya importmap ile eklenir."
        ),
        "code": """<div class="container">
  <div class="row">
    <div class="col-md-8">Ana icerik</div>
    <div class="col-md-4">Sidebar</div>
  </div>
</div>""",
        "exam_tip": "12 sutun grid. col-md-6 = yarim. container ortalar, container-fluid tam genislik.",
        "sources": [
            {"name": "Bootstrap Grid Docs", "url": "https://getbootstrap.com/docs/5.3/layout/grid/"},
        ],
    },
    {
        "id": "associations",
        "title": "Model Iliskileri (belongs_to / has_many)",
        "week": 7,
        "keywords": ["belongs_to", "has_many", "has_one", "foreign", "association"],
        "summary": "belongs_to FK bu tabloda; has_many karsi tarafta cok kayit.",
        "explain": (
            "Post belongs_to :category — posts tablosunda category_id vardir. "
            "Category has_many :posts — bir kategorinin cok postu olabilir. "
            "has_many :through ara model ile iliski kurar. dependent: :destroy silme davranisini belirler."
        ),
        "code": """class Post < ApplicationRecord
  belongs_to :category
  belongs_to :user
end

class Category < ApplicationRecord
  has_many :posts
end

post.category.name
category.posts""",
        "exam_tip": "belongs_to = FK burada. has_many = karsi tarafta cok. HABTM = ara tablo, id yok.",
        "sources": [
            {"name": "Rails Associations Guide", "url": "https://guides.rubyonrails.org/association_basics.html"},
        ],
    },
    {
        "id": "habtm",
        "title": "HABTM (has_and_belongs_to_many)",
        "week": 7,
        "keywords": ["habtm", "has_and_belongs", "join", "categories_posts"],
        "summary": "Coktan coga iliski; ara join tablosu, genelde id kolonu yok.",
        "explain": (
            "has_and_belongs_to_many iki model arasinda coktan coga baglanti kurar. "
            "posts_categories gibi ara tablo sadece iki foreign key icerir. "
            "Ek ozellik (tarih vb.) gerekiyorsa has_many :through tercih edilir."
        ),
        "code": """class Post < ApplicationRecord
  has_and_belongs_to_many :categories
end

class Category < ApplicationRecord
  has_and_belongs_to_many :posts
end

# join table: categories_posts (post_id, category_id)""",
        "exam_tip": "HABTM ara tablo, id yok. category_ids = [] ile coklu secim. Scaffold hizli CRUD uretir.",
        "sources": [
            {"name": "Rails HABTM", "url": "https://guides.rubyonrails.org/association_basics.html#the-has-and-belongs-to-many-association"},
        ],
    },
    {
        "id": "validation",
        "title": "Validation (validates)",
        "week": 8,
        "keywords": ["validat", "presence", "uniqueness", "length"],
        "summary": "Model kaydetmeden once veri kurallarini kontrol eder.",
        "explain": (
            "validates :title, presence: true bos birakilamaz der. "
            "uniqueness tekil olmayi, length uzunluk sinirini kontrol eder. "
            "Gecersiz kayit save → false doner, errors mesajlari dolar."
        ),
        "code": """class Post < ApplicationRecord
  validates :title, presence: true, length: { minimum: 3 }
  validates :slug, uniqueness: true
end

post = Post.new
post.valid?   # => false
post.errors.full_messages""",
        "exam_tip": "presence, uniqueness, length en sik. Gecersizse save false. errors.full_messages hata listesi.",
        "sources": [
            {"name": "Rails Validations Guide", "url": "https://guides.rubyonrails.org/active_record_validations.html"},
        ],
    },
    {
        "id": "normalizes",
        "title": "Normalization (normalizes)",
        "week": 8,
        "keywords": ["normaliz", "strip", "downcase"],
        "summary": "Kaydetmeden once veriyi otomatik duzenler.",
        "explain": (
            "Rails 7.1+ normalizes ile attribute kaydedilmeden once transform edilir. "
            "Ornegin email downcase, title strip ile bosluk temizlenir. "
            "Validation'dan once calisir, tutarli veri saglar."
        ),
        "code": """class User < ApplicationRecord
  normalizes :email, with: ->(e) { e.strip.downcase }
end

User.create(email: "  ALI@Mail.COM  ")
# email => "ali@mail.com\"""",
        "exam_tip": "normalizes = kaydetmeden duzenle. validates = kural kontrol. Ikisi birlikte kullanilir.",
        "sources": [
            {"name": "Rails normalizes API", "url": "https://api.rubyonrails.org/classes/ActiveRecord/Normalization/ClassMethods.html"},
        ],
    },
    {
        "id": "active-storage",
        "title": "Active Storage",
        "week": 8,
        "keywords": ["active storage", "attached", "upload", "image"],
        "summary": "Dosya/resim yukleme; has_one_attached / has_many_attached.",
        "explain": (
            "Active Storage Cloud veya disk uzerinde dosya yonetir. "
            "has_one_attached :avatar model ile dosyayi iliskilendirir. "
            "Formda file_field :avatar kullanilir; variant ile thumbnail uretilebilir."
        ),
        "code": """class Post < ApplicationRecord
  has_one_attached :image
end

# form
<%= f.file_field :image %>

# view
<%= image_tag @post.image if @post.image.attached? %>""",
        "exam_tip": "has_one_attached :image. file_field ile yukle. attached? dosya var mi kontrol.",
        "sources": [
            {"name": "Rails Active Storage Overview", "url": "https://guides.rubyonrails.org/active_storage_overview.html"},
        ],
    },
    {
        "id": "i18n",
        "title": "I18n (Yerellestirme)",
        "week": 9,
        "keywords": ["i18n", "locale", "translate", "t(", "tr.yml"],
        "summary": "Coklu dil destegi; I18n.t ve config/locales/*.yml dosyalari.",
        "explain": (
            "I18n modulu metinleri YAML dosyalarinda tutar. I18n.t('posts.title') ceviri doner. "
            "URL'de ?locale=en veya session ile dil degistirilir. "
            "Rails varsayilan locale config/application.rb'de ayarlanir."
        ),
        "code": """# config/locales/tr.yml
tr:
  posts:
    title: "Basliklar"

# view
<%= t('posts.title') %>
<%= link_to 'EN', url_for(locale: :en) %>""",
        "exam_tip": "I18n.t veya t() helper. locale= en/tr. YAML dosyalari config/locales/.",
        "sources": [
            {"name": "Rails I18n Guide", "url": "https://guides.rubyonrails.org/i18n.html"},
        ],
    },
    {
        "id": "friendly-id",
        "title": "FriendlyId (Slug URL)",
        "week": 9,
        "keywords": ["friendly", "slug", "friendlyid"],
        "summary": "/posts/1 yerine /posts/rails-rehberi gibi okunabilir URL.",
        "explain": (
            "FriendlyId gem'i basliktan slug uretir ve URL'de id yerine slug kullanir. "
            "extend FriendlyId; friendly_id :title, use: :slugged ile model yapilandirilir. "
            "SEO ve kullanici deneyimi icin faydalidir."
        ),
        "code": """class Post < ApplicationRecord
  extend FriendlyId
  friendly_id :title, use: :slugged
end

# /posts/ruby-on-rails-rehberi
Post.friendly.find(params[:id])""",
        "exam_tip": "FriendlyId = slug URL. friendly_id :title. find yerine friendly.find kullanilir.",
        "sources": [
            {"name": "FriendlyId GitHub", "url": "https://github.com/norman/friendly_id"},
        ],
    },
    {
        "id": "action-text",
        "title": "Action Text",
        "week": 9,
        "keywords": ["action text", "rich text", "trix", "has_rich_text"],
        "summary": "Zengin metin editoru (Trix); kalin, liste, resim embed.",
        "explain": (
            "Action Text Rails'e dahil zengin metin cozumudur. has_rich_text :content ile "
            "model iliskilendirilir. Formda rich_text_area :content kullanilir. "
            "Trix editor arayuzu saglar, icerik HTML olarak saklanir."
        ),
        "code": """class Post < ApplicationRecord
  has_rich_text :content
end

<%= form_with model: @post do |f| %>
  <%= f.rich_text_area :content %>
<% end %>""",
        "exam_tip": "has_rich_text :content. rich_text_area form helper. Trix editor kullanilir.",
        "sources": [
            {"name": "Rails Action Text Overview", "url": "https://guides.rubyonrails.org/action_text_overview.html"},
        ],
    },
    {
        "id": "devise",
        "title": "Devise (Authentication)",
        "week": 10,
        "keywords": ["devise", "authentication", "sign_in", "current_user"],
        "summary": "Hazir kullanici girisi: kayit, giris, sifre sifirlama.",
        "explain": (
            "Devise gem'i User modeline moduller ekler (:database_authenticatable, :registerable vb.). "
            "authenticate_user! giris zorunlu kilar. current_user oturum acmis kullaniciyi doner. "
            "devise_for :users routes.rb'ye login/register yollarini ekler."
        ),
        "code": """class ApplicationController < ActionController::Base
  before_action :authenticate_user!
end

class PostsController < ApplicationController
  def create
    @post = current_user.posts.new(post_params)
  end
end""",
        "exam_tip": "Devise = authentication. authenticate_user! giris zorunlu. current_user aktif kullanici.",
        "sources": [
            {"name": "Devise GitHub Wiki", "url": "https://github.com/heartcombo/devise"},
            {"name": "Devise Getting Started", "url": "https://github.com/heartcombo/devise#getting-started"},
        ],
    },
    {
        "id": "authorization",
        "title": "Authorization (Yetkilendirme)",
        "week": 10,
        "keywords": ["authorization", "admin", "rol", "yetki", "can?"],
        "summary": "Kim oldugunu degil, ne yapabilecegini kontrol eder.",
        "explain": (
            "Authentication kimlik dogrulama (Devise), Authorization yetkilendirme (admin mi?). "
            "user.admin? gibi metotlar veya Pundit/Cancancan gem'leri ile erisim kontrol edilir. "
            "Controller'da unless current_user.admin? redirect yapilir."
        ),
        "code": """def destroy
  unless current_user.admin?
    redirect_to root_path, alert: "Yetkiniz yok"
    return
  end
  @post.destroy
end""",
        "exam_tip": "Authentication=kimlik, Authorization=yetki. admin? rol kontrolu. Devise auth, rol ayri.",
        "sources": [
            {"name": "Rails Security Guide", "url": "https://guides.rubyonrails.org/security.html"},
        ],
    },
    {
        "id": "bloklar",
        "title": "Bloklar, Proc ve Lambda",
        "week": 2,
        "keywords": ["blok", "proc", "lambda", "each", "yield", "map"],
        "summary": "Blok do/end veya {}; Proc/Lambda farkli arguman kurallari.",
        "explain": (
            "Bloklar Ruby'nin guclu yonudur: [1,2,3].each { |n| puts n }. "
            "Proc arguman sayisina toleransli, Lambda katidir (arity kontrol). "
            "yield metot icinden blogu cagirir."
        ),
        "code": """[1, 2, 3].map { |x| x * 2 }  # => [2, 4, 6]

my_proc = Proc.new { |a, b| a + b }
my_proc.call(1)      # => 1 (eksik arg OK)

my_lambda = ->(a, b) { a + b }
# my_lambda.call(1)  # ArgumentError""",
        "exam_tip": "each/map blok alir. Lambda -> veya lambda{}. Proc toleransli, Lambda katı arguman.",
        "sources": [
            {"name": "Ruby Proc vs Lambda", "url": "https://docs.ruby-lang.org/en/master/Proc.html"},
        ],
    },
]


def topics_for_week(week: int):
    return [t for t in TOPICS if t["week"] == week]


def topic_by_id(topic_id: str):
    for t in TOPICS:
        if t["id"] == topic_id:
            return t
    return None


def match_panel_topics(panel_title: str, week: int):
    """Panel basligina gore eslesen zenginlestirme konularini dondur."""
    title = panel_title.lower()
    for tr_src, tr_dst in {"ı": "i", "ğ": "g", "ü": "u", "ş": "s", "ö": "o", "ç": "c"}.items():
        title = title.replace(tr_src, tr_dst)
    matched = []
    for topic in TOPICS:
        if topic["week"] != week:
            continue
        for kw in topic["keywords"]:
            if kw in title:
                matched.append(topic)
                break
    return matched


from ruby_faq_tr import attach_ruby_faq_to_topics

attach_ruby_faq_to_topics(TOPICS)
