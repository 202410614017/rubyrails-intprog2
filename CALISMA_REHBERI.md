# İnternet Programcılığı II — Sınav Çalışma Rehberi

> **Kaynak:** Hafta 2–10 ders slaytları (Ecmel Albayrak)  
> Bu rehber PDF'lerdeki **tüm konuları** kapsar; hiçbir hafta atlanmamıştır.

---

## İçindekiler

1. [Hafta 2 — Ruby & Rails Giriş](#hafta-2--ruby--rails-giriş)
2. [Hafta 3 — ORM & Active Record](#hafta-3--orm--active-record)
3. [Hafta 4 — Enum, Routes, Controllers](#hafta-4--enum-routes-controllers)
4. [Hafta 5 — Form Helpers & Strong Parameters](#hafta-5--form-helpers--strong-parameters)
5. [Hafta 6 — Bootstrap Frontend](#hafta-6--bootstrap-frontend)
6. [Hafta 7 — Model İlişkileri & Kategori](#hafta-7--model-i̇lişkileri--kategori)
7. [Hafta 8 — Validation & Active Storage](#hafta-8--validation--active-storage)
8. [Hafta 8 — I18n, FriendlyId, Action Text](#hafta-9--i18n-friendlyid-action-text)
9. [Hafta 10 — Devise & Authorization](#hafta-10--devise--authorization)
10. [Komut Hızlı Referans](#komut-hızlı-referans)
11. [Sınav Soruları (Kendini Test Et)](#sınav-soruları-kendini-test-et)

---

## Hafta 2 — Ruby & Rails Giriş

### Ruby Temelleri

| Konu | Önemli Nokta |
|------|--------------|
| Ruby | 1995, Matz Matsumoto, açık kaynak, OOP, **her şey nesnedir** |
| Integer | `3.class` → Integer → Numeric → Object → BasicObject |
| Float | `to_i`, `negative?`, `floor`, `ceil` |
| String | `downcase`, `upcase`, `capitalize`, `strip`, `%w{}`, `%i{}`, `#{}` interpolation |
| Array | `length`, `count`, `include?`, `first`, `last`, `sort`, `compact`, `uniq`, `flatten`, `+`, `\|`, `-`, `<<`, `push`, `unshift`, `pop`, `shift`, `delete` |
| Hash | Key-value, `:symbol` key, `keys`, `values`, `key?`, `value?` |
| Symbol | `:user` — tekil, `object_id` sabit kalır (String'den fark) |

### Metot Kuralları

- `?` ile biten → `true`/`false` döner (`even?`, `odd?`, `zero?`)
- `!` ile biten → tehlikeli/destructive (`upcase!` orijinali değiştirir)
- `return` yoksa **son satırın değeri** döner
- `*isimler` → değişken sayıda argüman

### Değişken Türleri

| Tür | Sözdizimi | Kapsam |
|-----|-----------|--------|
| Local | `out_text` (küçük harf/`_`) | Fonksiyon içi |
| Global | `$monday` | Her yerden erişim |
| Instance | `@name` | Nesneye ait |
| Class | `@@coffee_number` | Sınıfa ait, `@@` ile |
| Constant | `PI = 3.14` | Büyük harf, değiştirilmez |

### Sınıflar & OOP

```ruby
class Dog < Animal          # Kalıtım
  def speak; super; end     # super → üst sınıf metodu
end

attr_accessor :name        # getter + setter
attr_reader :name          # sadece getter
attr_writer :name          # sadece setter
```

**Erişim:** `public` (her yerden) | `private` (sadece dolaylı) | `protected` (dolaylı + alt sınıf)

### Modül

- Metot/sabit koleksiyonu, **türetilemez**
- `include Movable` → sınıfa karıştırılır
- Namespacing: `Framework::VERSION`, `Framework::HttpFunctions.fetch_url`

### Bloklar, Proc, Lambda

```ruby
[1,2,3].each { |n| puts n }
[1,2,3].map { |n| n * 2 }

def test_function
  yield if block_given?
end

my_proc = Proc.new { |x,y| puts x+y }   # fazla/eksik argüman tolere eder
my_lambda = ->(x,y) { puts x+y }      # yanlış argüman → ArgumentError
```

### Koşullar

```ruby
if / elsif / else / end
unless a == b
amount == 1 ? "apple" : "apples"   # ternary
for i in 1..3
```

---

### Rails Blog Projesi Kurulumu

```bash
rails new blogger-a-ogrencino -d postgresql --css bootstrap
cd blogger-a-ogrencino
git init
git remote add origin https://...
git add .
git commit -m "First commit"
git push -u origin main
rails db:create
rails s                    # localhost:3000
rails s -p 3001            # farklı port
```

### Rails Dizin Yapısı (EZBERLE!)

| Dizin/Dosya | Görevi |
|-------------|--------|
| `app/controllers` | İstekleri alır, model+view ile etkileşir |
| `app/models` | Veri yapısı, iş mantığı, DB etkileşimi |
| `app/views` | Arayüz (`.html.erb`) |
| `config/database.yml` | DB ayarları |
| `config/routes.rb` | URL yolları |
| `config/importmap.rb` | JS paketleri |
| `config/locales/` | Çoklu dil (tr.yml, en.yml) |
| `config/environments/` | development, production, test |
| `config/master.key` + `credentials.yml.enc` | Gizli bilgiler (şifreli) |
| `db/migrate/` | Migration dosyaları |
| `db/schema.rb` | Güncel DB şeması |
| `db/seeds.rb` | Ön tanımlı veri |
| `public/` | Statik dosyalar |
| `log/` | Log dosyaları |
| `test/` | Test dosyaları |
| `vendor/` | 3. parti kütüphaneler |
| `Gemfile` / `Gemfile.lock` | Gem bağımlılıkları |
| `package.json` | npm bağımlılıkları |

### Credentials

```bash
EDITOR="code --wait" rails credentials:edit
```

```yaml
# database.yml içinde:
<%= Rails.application.credentials.dig(:pg, :username) %>
<%= Rails.application.credentials.dig(:pg, :password) %>
```

`<% %>` → Ruby çalıştır | `<%= %>` → çıktı ver

### MVC Akışı

```
routes.rb → Controller → Model → View → HTML yanıt
get "/users", to: "users#index"
```

### Anasayfa

```ruby
# config/routes.rb
root "home#index"

# app/controllers/home_controller.rb
class HomeController < ApplicationController
  def index; end
end

# app/views/home/index.html.erb
<h1>Merhaba Rails</h1>
```

### RubyGems

```bash
gem search -r rails
gem install gem_name
gem list
```

---

## Hafta 3 — ORM & Active Record

### ORM Nedir?

- **Object Relational Mapping** — tablo ↔ sınıf, satır ↔ nesne, sütun ↔ attribute, FK ↔ ilişki
- SQL yazmadan DDL ve DML işlemleri

| DDL | DML |
|-----|-----|
| Create, Alter, Drop | Select, Insert, Update, Delete |

**Avantajlar:** Az SQL, OOP, platform bağımsızlığı, uygulama tarafında modelleme, düşük maliyet

**Dillere göre ORM:** Ruby→ActiveRecord, Java→Hibernate, C#→Entity Framework, Python→Django, Go→Gorm

### Active Record

- MVC'de **Model** katmanı
- Tablo adı → çoğul snake_case (`Post` → `posts`, `Person` → `people`)

### Veri Türleri

| Tür | Açıklama |
|-----|----------|
| `string` | Max 255 karakter |
| `text` | Max 65.535 karakter |
| `integer` | -2147483648 – 2147483647 |
| `float` | 8 byte ondalık |
| `boolean` | true/false |
| `decimal` | Hassas finansal veri (precision, scale) |
| `date` | Yıl-ay-gün |
| `datetime` | Tarih + saat |
| `timestamps` | `created_at`, `updated_at` otomatik |

### Model Oluşturma

```bash
rails g model Post title article:text
rails db:migrate
```

```ruby
class CreatePosts < ActiveRecord::Migration[8.0]
  def change
    create_table :posts do |t|
      t.string :title
      t.text :article
      t.timestamps
    end
  end
end
```

### Rails Console Komutları

```ruby
rails c
Post.column_names
post = Post.new(title: "...", article: "...")  # henüz kaydedilmedi, id nil
post.save
Post.create(title: "...", article: "...")       # oluştur + kaydet

Post.all
Post.count
Post.first / Post.second / Post.last
Post.first(10) / Post.last(10)
Post.take / Post.take(2)   # sıralama yok, LIMIT

Post.where(title: "Git Commit Komutu")
Post.where('title LIKE ?', "%Commit%")
Post.where.not(title: nil)
Post.where.not(title: nil).or(Post.where(article: nil))
Post.where.not(title: nil).where(article: nil)
Post.where(id: [1,2]).and(Post.where.not(title: nil))

Post.order(:created_at)              # ASC (varsayılan)
Post.order(created_at: :desc)        # DESC

Post.find(1)                         # id ile, bulamazsa exception
Post.find_by(title: "...")           # tek kayıt veya nil
Post.find([1, 3])                    # çoklu id
Post.where(...)                      # ActiveRecord::Relation döner

post.update(title: "...")
post.title = "..."; post.save

Post.first.destroy
Post.destroy_all
```

### find vs find_by vs where

| Metot | Döner | Bulamazsa |
|-------|-------|-----------|
| `find(id)` | Tek kayıt | Exception |
| `find_by(...)` | Tek kayıt veya nil | nil |
| `where(...)` | Relation (çoklu) | Boş relation |

### Migration

```bash
rails g migration CreateUser first_name last_name
rails g migration AddIdNumberToUser id_number:integer
rails g migration RemoveIdNumberFromUser id_number:integer
rails g migration DropUser
rails db:migrate
rails db:rollback
rails db:migrate:status
```

### DB Komutları

| Komut | İşlev |
|-------|-------|
| `db:create` | Mevcut ortam için DB oluştur |
| `db:create:all` | Tüm ortamlar |
| `db:drop` | Mevcut ortam DB sil |
| `db:drop:all` | Tüm ortamlar |
| `db:migrate` | Bekleyen migration'ları çalıştır |
| `db:migrate:up` | Tek migration çalıştır |
| `db:migrate:down` | Tek migration geri al |
| `db:migrate:status` | Durum |
| `db:rollback` | Son migration geri al |
| `db:seed` | seeds.rb çalıştır |
| `db:schema:load` | Şemayı yükle |
| `db:setup` | schema:load + seed |
| `db:reset` | drop + setup |

---

## Hafta 4 — Enum, Routes, Controllers

### Status Alanı Ekleme

```bash
rails g migration AddStatusToPost status:integer
```

```ruby
add_column :posts, :status, :integer, default: 0
```

### Enum

```ruby
class Post < ApplicationRecord
  enum :status, { draft: 0, published: 1, inactive: 2 }
end
```

- Default 0 → `draft`
- Otomatik scope: `Post.published`, `Post.draft`, `Post.inactive`
- Soru metodları: `post.published?`, `post.draft?`
- `Post.statuses` → `{"draft"=>0, "published"=>1, "inactive"=>2}`
- `scopes: false` → otomatik scope kapatılır
- `prefix: true` → `Post.status_draft`
- `suffix: true` → `Post.draft_status`

### Scope

```ruby
scope :published, -> { where(status: :published) }
Post.published.or(Post.inactive)
```

### HTTP & URL

```
http://example.org/posts?query=rails&sort=asc
  ↑protokol  ↑host        ↑path  ↑parametreler (? ile başlar)
```

| Metot | Amaç |
|-------|------|
| GET | Veri iste (hassas veri gönderme!) |
| POST | Yeni kayıt oluştur |
| PUT | Tüm kaynağı güncelle (id zorunlu) |
| PATCH | Kısmi güncelleme |
| DELETE | Kaynak sil |

### CRUD Routes

| Action | HTTP | Route | Açıklama |
|--------|------|-------|----------|
| index | GET | `/posts` | Tümünü listele |
| show | GET | `/posts/:id` | Tek kayıt |
| new | GET | `/posts/new` | Form göster |
| create | POST | `/posts` | Kaydet |
| edit | GET | `/posts/:id/edit` | Düzenleme formu |
| update | PUT/PATCH | `/posts/:id` | Güncelle |
| destroy | DELETE | `/posts/:id` | Sil |

```ruby
resources :posts          # 7 CRUD route otomatik
root "posts#index"
rails routes             # terminalde route listesi
# localhost:3000/rails/info/routes
```

### Controller & ERB

```bash
rails g controller Posts index --skip-routes
```

```ruby
class PostsController < ApplicationController
  def index
    @posts = Post.published   # @ ile instance variable → view'a gider
  end
  def show
    @post = Post.find(params[:id])
  end
end
```

**ERB:**
- `<% %>` → kod çalıştır, çıktı yok
- `<%= %>` → kod çalıştır, çıktı ver

```erb
<% @posts.each do |post| %>
  <%= post.title %>
  <%= link_to "Görüntüle", post_path(post) %>
<% end %>
```

### Path Helpers

| Helper | Üretir |
|--------|--------|
| `posts_path` | `/posts` |
| `posts_url` | `http://localhost:3000/posts` |
| `post_path(1)` | `/posts/1` |
| `post_url(1)` | Tam URL |
| `new_post_path` | `/posts/new` |
| `edit_post_path(post)` | `/posts/1/edit` |

`_path` → göreceli yol | `_url` → tam URL (protokol+host+port)

### Seed Verisi

```ruby
# db/seeds.rb
posts = YAML.load_file(Rails.root.join("db/data/posts.json"), symbolize_names: true)
posts.each do |post|
  Post.find_or_create_by(title: post[:title], article: post[:article], status: post[:status])
end
```

```bash
rails db:seed
```

---

## Hafta 5 — Form Helpers & Strong Parameters

### Action View

- MVC'de **View** katmanı
- Controller veriyi alır → View HTML yanıt üretir
- `form_with` ana form helper

### form_with

```erb
<%= form_with model: @post do |form| %>
  <%= form.label :title, "Başlık" %>
  <%= form.text_field :title %>
  <%= form.text_area :article, size: "70x5" %>
  <%= form.select(:status, Post.statuses.keys) %>
  <%= form.collection_radio_buttons :status, Post.statuses, :first, :first %>
  <%= form.submit %>
<% end %>
```

- `authenticity_token` → CSRF koruması (hidden field)
- Model bağlı form → `params[:post][:title]` şeklinde gelir

### Form Elemanları

| Helper | HTML |
|--------|------|
| `text_field` | `<input type="text">` |
| `text_area` | `<textarea>` |
| `hidden_field` | `<input type="hidden">` |
| `number_field` | `<input type="number">` |
| `password_field` | `<input type="password">` |
| `date_field` | `<input type="date">` |
| `file_field` | Dosya yükleme |
| `select` | `<select>` dropdown |
| `collection_radio_buttons` | Radio butonlar |

### CRUD Controller (Tam)

```ruby
class PostsController < ApplicationController
  before_action :set_post, only: %i[show edit update destroy]

  def index
    @posts = Post.published
  end

  def show; end

  def new
    @post = Post.new
  end

  def create
    @post = Post.new(post_params)
    if @post.save
      redirect_to posts_path
    else
      render :new
    end
  end

  def edit; end

  def update
    if @post.update(post_params)
      redirect_to @post
    else
      render :edit
    end
  end

  def destroy
    @post.destroy
    redirect_to posts_path
  end

  private

  def set_post
    @post = Post.find(params[:id])
  end

  def post_params
    params.require(:post).permit(:title, :article, :status)
  end
end
```

### Strong Parameters

```ruby
params.require(:post).permit(:title, :article, :status)
```

- `:post` anahtarının varlığını zorunlu kılar
- Sadece izin verilen alanları geçirir → **Mass Assignment** saldırısını önler

### link_to

```erb
<%= link_to "Post", @post %>
<%= link_to "Posts", posts_path, class: "btn btn-primary" %>
<%= link_to(@post) do %>
  <strong><%= @post.title %></strong>
<% end %>
```

### button_to (DELETE için)

```erb
<%= button_to "Sil", @post, method: :delete, data: { turbo_confirm: "Emin misin?" } %>
```

- Kendi mini formunu oluşturur
- `_method=delete` hidden field ekler

### Partials

- Dosya adı `_` ile başlar: `_form.html.erb`
- `render "form", post: @post, form_title: "Yeni Post Ekle"`

### before_action (DRY)

```ruby
before_action :set_post, only: %i[show edit update destroy]
```

---

## Hafta 6 — Bootstrap Frontend

### Bootstrap 5

- Ücretsiz frontend framework
- Responsive (mobil uyumlu)
- Viewport meta: `<meta name="viewport" content="width=device-width, initial-scale=1">`

### Breakpoints

| Breakpoint | Class | Boyut |
|------------|-------|-------|
| Extra small | (none) | <576px |
| Small | `sm` | ≥576px |
| Medium | `md` | ≥768px |
| Large | `lg` | ≥992px |
| X-Large | `xl` | ≥1200px |
| XX-Large | `xxl` | ≥1400px |

### Container

| Sınıf | Davranış |
|-------|-----------|
| `.container` | Her breakpoint'te max-width değişir |
| `.container-md` | Belirtilene kadar %100 |
| `.container-fluid` | Her zaman %100 |

### Grid (12 sütun)

```html
<div class="container">
  <div class="row">
    <div class="col-md-8">...</div>
    <div class="col-md-4">...</div>
  </div>
</div>
```

- `<768px` → sütunlar üst üste yığılır
- Prefix: `.col-`, `.col-sm-`, `.col-md-`, `.col-lg-`, `.col-xl-`, `.col-xxl-`

### Popper.js (Bootstrap JS için)

```ruby
# config/importmap.rb
pin "@popperjs/core", to: "https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js"
```

```javascript
// app/javascript/application.js
import "@popperjs/core"
```

```bash
rails assets:precompile
```

### Layout Yapısı

```erb
<body class="d-flex flex-column min-vh-100">
  <%= render "shared/navbar" %>
  <div class="container">
    <%= yield %>
  </div>
  <%= render "shared/footer" %>
</body>
```

### Navbar & Footer

- `app/views/shared/_navbar.html.erb`
- `app/views/shared/_footer.html.erb`
- `link_to "Blogger", root_path, class: "navbar-brand"`

### Card Örneği (Index)

```erb
<div class="row">
  <% @posts.each do |post| %>
    <div class="col-md-8 mx-auto mt-4">
      <div class="card">
        <div class="card-header"><%= link_to post.title, post_path(post) %></div>
        <div class="card-body"><%= post.article %></div>
        <div class="card-footer">
          <%= link_to "Güncelle", edit_post_path(post), class: "btn btn-outline-warning btn-sm" %>
        </div>
      </div>
    </div>
  <% end %>
</div>
```

### Ek Sayfalar

```ruby
# routes.rb
get "about", to: "home#about"
get "projects", to: "home#projects"
```

### image_tag

```erb
<%= image_tag("profile.jpg", width: "200", alt: "Profile") %>
```

- Resimler: `app/assets/images/`
- Yeni resim sonrası: `rails assets:precompile`

### Bootstrap Icons

```erb
<%= link_to "https://github.com/username" do %>
  <i class="bi bi-github link-dark"></i>
<% end %>
```

---

## Hafta 7 — Model İlişkileri & Kategori

### 6 İlişki Türü

| İlişki | Örnek |
|--------|-------|
| `belongs_to` | Book → Author (FK book'ta) |
| `has_one` | User → Profile |
| `has_many` | Author → Books |
| `has_many :through` | Physician → Patients (Appointment üzerinden) |
| `has_one :through` | User → Account (Profile üzerinden) |
| `has_and_belongs_to_many` (HABTM) | User ↔ Role (join table) |

### belongs_to + has_many

```ruby
class Book < ApplicationRecord
  belongs_to :author
end

class Author < ApplicationRecord
  has_many :books, dependent: :destroy
end
```

```bash
rails g model Author name
rails g model Book author:references published_at:datetime
```

### has_many :through

```ruby
class Physician < ApplicationRecord
  has_many :appointments, dependent: :destroy
  has_many :patients, through: :appointments
end

class Appointment < ApplicationRecord
  belongs_to :physician
  belongs_to :patient
end
```

### has_one

```ruby
class User < ApplicationRecord
  has_one :profile
end

class Profile < ApplicationRecord
  belongs_to :user
end
```

### HABTM

```ruby
class User < ApplicationRecord
  has_and_belongs_to_many :roles
end

class Role < ApplicationRecord
  has_and_belongs_to_many :users
end
```

Join table: `users_roles` (`id: false`)

### Scaffold & Kategori

```bash
rails g scaffold Category name code
rails db:migrate
```

### Post ↔ Category (HABTM)

```bash
rails g migration CreateJoinTablePostsCategories posts categories
```

```ruby
class Post < ApplicationRecord
  has_and_belongs_to_many :categories
end

class Category < ApplicationRecord
  has_and_belongs_to_many :posts
end
```

### Konsol

```ruby
Category.create(name: "Java Programming", code: "java")
Post.last.categories << Category.find_by(name: "Java Programming")
Post.last.categories.count
Category.last.posts
```

### Form — Çoklu Kategori

```erb
<%= form.select :category_ids,
  Category.all.collect { |c| [c.name, c.id] },
  {}, { class: "form-select", multiple: true } %>
```

```ruby
def post_params
  params.require(:post).permit(:title, :article, :status, category_ids: [])
end
```

---

## Hafta 8 — Validation & Active Storage

### Validation Seviyeleri

1. Veritabanı kısıtları
2. Client-side
3. Controller level
4. **Model level** (en çok kullanılan)

### Tetikleyen Metotlar

`create`, `create!`, `save`, `save!`, `update`, `update!`

- `!` → hata olursa **exception**
- `!` yok → `save`/`update` **false** döner
- `save(validate: false)` → doğrulama atlanır

### Validasyon Atlayan Metotlar (DİKKAT!)

`decrement!`, `increment!`, `toggle!`, `touch`, `update_all`, `update_attribute`

### Normalization

- Validasyondan **önce** çalışır (`before_validation`)
- Veriyi reddetmez, **değiştirir**

```ruby
normalizes :title, with: -> title { title.squish.titlecase }
```

| | Validation | Normalization |
|---|-----------|---------------|
| Ne yapar | Kontrol eder | Değiştirir |
| Başarısız olabilir mi | Evet | Hayır |
| Ne zaman | save sırasında | doğrulamadan önce |

### Validation Helpers

| Helper | Açıklama | Örnek |
|--------|----------|-------|
| `presence` | Boş olamaz | `validates :title, presence: true` |
| `uniqueness` | Benzersiz | `validates :title, uniqueness: true` |
| `inclusion` | Kümede olmalı | `inclusion: { in: statuses.keys }` |
| `exclusion` | Kümede olmamalı | `exclusion: { in: %w(www us ca) }` |
| `length` | Uzunluk | `maximum: 255`, `in: 6..20`, `is: 11` |
| `numericality` | Sayısal | `only_integer: true, greater_than: 0` |
| `format` | Regex | `with: /\A\d+\z/` |

### Validation Options

| Seçenek | Açıklama |
|---------|----------|
| `allow_nil: true` | nil ise doğrulama atlanır |
| `allow_blank: true` | nil veya boş string geçer |
| `on: :create` / `:update` | Ne zaman çalışır |
| `if:` / `unless:` | Koşullu doğrulama |
| `message:` | Özel hata mesajı |

### Hata Mesajları

```ruby
post.errors.any?
post.errors.messages          # {:title=>["..."]}
post.errors.full_messages     # ["Title ..."]
post.errors[:title]
post.errors.count / .size
post.errors.clear
```

### Post Model Son Hali

```ruby
class Post < ApplicationRecord
  normalizes :title, with: -> title { title.squish.titlecase }
  validates :title, presence: true, uniqueness: true, length: { maximum: 255 }
  validates :article, presence: true, length: { maximum: 65_535 }
  validates :status, inclusion: { in: statuses.keys }
end
```

### Form Hata Gösterimi

```erb
<% if post.errors.any? %>
  <div class="alert alert-danger">
    <h5><%= post.errors.count %> hata bulundu:</h5>
    <ul>
      <% post.errors.full_messages.each do |message| %>
        <li><%= message %></li>
      <% end %>
    </ul>
  </div>
<% end %>
```

```ruby
render :new, status: :unprocessable_entity   # HTTP 422
```

### Active Storage

```bash
rails active_storage:install
rails db:migrate
```

```ruby
class Post < ApplicationRecord
  has_one_attached :image
end

def post_params
  params.require(:post).permit(:title, :article, :status, :image, category_ids: [])
end
```

```erb
<%= form.file_field :image, class: "form-control" %>
<% if @post.image.present? %>
  <%= image_tag(@post.image) %>
<% end %>
```

---

## Hafta 9 — I18n, FriendlyId, Action Text

### I18n (Internationalization)

```ruby
I18n.t "store.title"    # translate
I18n.l Time.now         # localize
```

### locale.rb

```ruby
# config/initializers/locale.rb
I18n.load_path += Dir[Rails.root.join("config/locales/**/*.yml").to_s]
I18n.available_locales = [:tr, :en]
I18n.default_locale = :tr
```

### Dil Değiştirme

```ruby
# application_controller.rb
around_action :switch_locale

private
def switch_locale(&action)
  locale = params[:locale] || I18n.default_locale
  I18n.with_locale(locale, &action)
end
```

URL: `localhost:3000/posts?locale=en`

### Dosya Yapısı

```
config/locales/
  defaults/tr.yml, en.yml
  models/post/tr.yml, en.yml
  views/posts/tr.yml, en.yml
  views/shared/tr.yml, en.yml
```

### Kullanım

```erb
<%= link_to t("actions.show"), post_path(post) %>
<%= render "form", post: @post, form_title: t(".title") %>
<%= link_to t(".home"), root_path %>
```

`t(".title")` → mevcut view dosyasının yoluna göre çeviri arar

### Model Yerelleştirme (tr.yml)

```yaml
tr:
  activerecord:
    models:
      post:
        one: Blog Girdisi
        other: Blog Girdileri
    attributes:
      post:
        title: Post Başlığı
    enums:
      post:
        statuses:
          draft: Taslak
          published: Yayınlandı
```

### Dil Bayrağı

```erb
<%= link_to url_for(locale: :tr) %>
<%= link_to url_for(locale: :en) %>
```

### FriendlyId

```ruby
# Gemfile
gem 'friendly_id', '~> 5.7'

# Model
extend FriendlyId
friendly_id :title, use: :slugged

# Controller
@post = Post.friendly.find(params[:id])
```

```bash
bundle install
rails generate friendly_id
rails g migration AddSlugToPosts slug:uniq
rails db:migrate
Post.find_each(&:save)   # mevcut kayıtlara slug oluştur
```

URL: `/posts/1` → `/posts/java-ya-giris`

### Action Text (Zengin İçerik)

```bash
bin/rails action_text:install
rails db:migrate
rails assets:precompile
sudo apt-get install libvips   # resimler için
```

```ruby
class Post < ApplicationRecord
  has_rich_text :article
end
```

```erb
<%= form.rich_textarea :article %>
```

---

## Hafta 10 — Devise & Authorization

### Authentication vs Authorization

| | Authentication | Authorization |
|---|----------------|---------------|
| Ne | Kim olduğunu doğrular | Ne yapabileceğini belirler |
| Ne zaman | Login | Login sonrası |
| Nasıl | Şifre, 2FA | Roller, izinler |
| Örnek | Email+şifre giriş | Sadece kendi dosyalarına erişim |

Devise → Authentication | Pundit/CanCanCan → Authorization

### Devise Modülleri

| Modül | Özellik |
|-------|---------|
| Database Authenticatable | Email+şifre giriş |
| Registerable | Kayıt ol |
| Recoverable | Şifre sıfırlama |
| Rememberable | Beni hatırla |
| Trackable | Oturum takibi |
| Confirmable | Email onayı |
| Lockable | Hesap kilitleme |
| Timeoutable | İşlem yoksa oturum düşer |
| Omniauthable | OAuth (Google, Facebook) |

### Kurulum

```bash
bundle add devise
rails generate devise:install
rails generate devise User firstname lastname gender:integer username slug active:boolean
rails db:migrate
rails g devise:views
```

```ruby
class User < ApplicationRecord
  devise :database_authenticatable, :registerable,
         :recoverable, :rememberable, :validatable,
         :timeoutable

  extend FriendlyId
  friendly_id :username, use: :slugged

  enum :gender, { secret: 0, male: 1, female: 2 }
  enum :role, { editor: 1, admin: 2 }

  normalizes :firstname, with: -> firstname { firstname.squish.titlecase }
  validates :firstname, presence: true, length: { maximum: 255 }
  validates :username, presence: true, uniqueness: true
  validates :email, presence: true, uniqueness: true

  has_many :posts, dependent: :destroy

  def fullname
    "#{firstname} #{lastname}"
  end
end
```

### Strong Parameter (Devise)

```ruby
class ApplicationController < ActionController::Base
  before_action :configure_permitted_parameters, if: :devise_controller?

  protected

  def configure_permitted_parameters
    devise_parameter_sanitizer.permit(:sign_up, keys: [:firstname, :lastname, :email, :username, :gender])
    devise_parameter_sanitizer.permit(:sign_in, keys: [:email, :password])
  end
end
```

### Navbar — Oturum Kontrolü

```ruby
current_user           # giriş yapmış kullanıcı
user_signed_in?        # giriş yapılmış mı?
destroy_user_session_path, method: :delete
```

### Giriş Zorunluluğu

```ruby
before_action :authenticate_user!
```

### Rol Sistemi

```bash
rails g migration AddRoleToUser role:integer
# default: 1 (editor)
```

### Admin Namespace

```ruby
# routes.rb
namespace :admin do
  resources :users, only: [:index, :show, :edit, :update]
end
```

```ruby
module Admin
  class UsersController < ApplicationController
    before_action :authenticate_user!
    before_action :authorize_admin

    def index
      @users = User.all
    end

    private

    def authorize_admin
      redirect_to root_path, alert: "Permissions denied" unless current_user.admin?
    end

    def set_user
      @user = User.friendly.find(params[:id])
    end
  end
end
```

### Post ↔ User İlişkisi

```bash
Post.destroy_all
rails g migration AddUserToPost user:references
rails db:migrate
```

```ruby
class Post < ApplicationRecord
  belongs_to :user
end

class User < ApplicationRecord
  has_many :posts, dependent: :destroy
end
```

```ruby
def create
  @post = current_user.posts.new(post_params)
  if @post.save
    redirect_to posts_path, notice: "Post başarılı bir şekilde oluşturuldu."
  else
    render :new, status: :unprocessable_entity
  end
end
```

---

## Komut Hızlı Referans

```bash
# Proje
rails new app -d postgresql --css bootstrap
rails s / rails c

# Model & Migration
rails g model Post title:text
rails g migration AddStatusToPost status:integer
rails g controller Posts index --skip-routes
rails g scaffold Category name code

# Veritabanı
rails db:create / db:migrate / db:rollback / db:seed / db:reset
rails db:migrate:status

# Diğer
rails routes
rails assets:precompile
rails active_storage:install
bin/rails action_text:install
bundle add devise
rails generate devise:install
rails g devise:views

# Git
git status / git add . / git commit -m "..." / git push origin main
```

---

## Sınav Soruları (Kendini Test Et)

### Ruby (Hafta 2)

1. Ruby'de `3.class.superclass.superclass` ne döner?
2. Symbol ile String arasındaki temel fark nedir?
3. `attr_accessor`, `attr_reader`, `attr_writer` farkları?
4. Proc ile Lambda arasındaki argüman farkı?
5. `?` ve `!` ile biten metotların anlamı?

### ORM & Active Record (Hafta 3)

6. ORM'in avantajları nelerdir?
7. `find`, `find_by` ve `where` arasındaki fark?
8. `save` ile `create` arasındaki fark?
9. `db:setup` ile `db:reset` ne yapar?
10. Migration rollback nasıl yapılır?

### Routes & HTTP (Hafta 4)

11. GET ve POST ne zaman kullanılır?
12. PUT ile PATCH farkı?
13. `resources :posts` kaç route oluşturur? İsimlerini yaz.
14. `posts_path` ile `posts_url` farkı?
15. Enum'da `draft: 0` ne anlama gelir?

### Forms & Security (Hafta 5)

16. Strong Parameters neden gerekli?
17. `authenticity_token` ne işe yarar?
18. Partial dosya adlandırma kuralı?
19. `button_to` ile `link_to` farkı (DELETE için)?
20. `before_action` ne sağlar?

### Bootstrap (Hafta 6)

21. Bootstrap grid kaç sütunludur?
22. `.container` ile `.container-fluid` farkı?
23. `col-md-8` ne zaman yan yana, ne zaman alt alta?

### İlişkiler (Hafta 7)

24. `belongs_to` FK hangi tabloda?
25. `has_many :through` ne zaman kullanılır?
26. HABTM join table özelliği?
27. `dependent: :destroy` ne yapar?

### Validation (Hafta 8)

28. Validation ile Normalization farkı?
29. `create!` ile `create` farkı?
30. `validates :title, presence: true, uniqueness: true, length: { maximum: 255 }` ne kontrol eder?
31. HTTP 422 ne anlama gelir?

### I18n & Gems (Hafta 9)

32. `I18n.t` ve `I18n.l` farkı?
33. FriendlyId ne sağlar?
34. Action Text ne için kullanılır?

### Devise (Hafta 10)

35. Authentication ile Authorization farkı?
36. `current_user` ve `user_signed_in?` ne döner?
37. `authenticate_user!` ne yapar?
38. Admin namespace'te yetki kontrolü nasıl yapılır?
39. `current_user.posts.new` neden kullanılır?

---

## Cevap Anahtarı (Kısa)

<details>
<summary>Tıkla — cevapları gör</summary>

1. Object | 2. Symbol tekil (aynı object_id), String her seferinde yeni nesne | 3. accessor=get+set, reader=get, writer=set | 4. Proc toleranslı, Lambda strict | 5. ?→boolean, !→destructive

6. Az SQL, OOP, platform bağımsız, düşük maliyet | 7. find→exception, find_by→nil, where→Relation | 8. save mevcut nesne, create yeni+save | 9. setup=schema+seed, reset=drop+setup | 10. rails db:rollback

11. GET=okuma, POST=oluşturma | 12. PUT=tüm kaynak, PATCH=kısmi | 13. index,show,new,create,edit,update,destroy (7) | 14. path=göreceli, url=tam | 15. DB'de 0, draft anlamında

16. Mass assignment koruması | 17. CSRF koruması | 18. `_` ile başlar | 19. button_to form+_method=delete | 20. Tekrarlayan kodu merkezileştirir

21. 12 | 22. container=max-width, fluid=%100 | 23. ≥768px yan yana, altında üst üste

24. belongs_to olan tabloda | 25. Ara tablo üzerinden çok-çok | 26. id:false, iki FK | 27. Parent silinince child'ları da siler

28. Validation reddeder, normalization değiştirir | 29. !→exception | 30. Boş olamaz, tekil, max 255 | 31. Validasyon hatası

32. t=metin, l=tarih/saat | 33. SEO dostu slug URL | 34. WYSIWYG zengin metin editörü

35. Auth=kimlik, Authz=yetki | 36. current_user=User objesi, signed_in?=boolean | 37. Giriş yoksa yönlendirir | 38. current_user.admin? kontrolü | 39. Post otomatik o kullanıcıya atanır

</details>

---

**İyi çalışmalar!** Sorularını veya belirli bir haftayı daha detaylı açıklamamı istersen yaz.
