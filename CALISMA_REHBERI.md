# İnternet Programcılığı II — Eksiksiz Ders Notu Arşivi

> **Kaynak:** Hafta 2–10 ders slaytları (Öğr. Gör. Ecmel Albayrak)  
> Bu arşiv PDF slaytlarındaki **tüm konuları** içerir. Hiçbir hafta atlanmamıştır.  
> Sınav hazırlığı için **Konu İndeksi**, haftalık notlar ve test sorularını kullanın.

## Konu İndeksi — Alfabetik

| Konu | Hafta | Açıklama |
|------|-------|----------|
| Active Record | 3 | ORM kütüphanesi, model katmanı |
| Active Storage | 8 | Dosya/resim yükleme |
| Array (Dizi) | 2 | Ruby veri türü, metotları |
| attr_accessor / reader / writer | 2 | **Kapsülleme** — getter/setter |
| Authentication | 10 | Kimlik doğrulama (Devise) |
| Authorization | 10 | Yetkilendirme (admin?, roller) |
| before_action | 5 | Controller callback (DRY) |
| belongs_to | 7 | Model ilişkisi, FK bu tabloda |
| Bloklar (each, map, yield) | 2 | Ruby blok yapısı |
| Bootstrap Grid | 6 | 12 sütun responsive layout |
| button_to | 5 | DELETE form butonu |
| Constants (Sabitler) | 2 | PI = 3.14, büyük harf |
| CRUD | 4 | Create Read Update Delete |
| CSRF / authenticity_token | 5 | Form güvenlik tokeni |
| Enum | 4 | Sayısal sabitlere isim (draft: 0) |
| ERB | 4 | Embedded Ruby, <% %> <%= %> |
| FriendlyId | 9 | SEO slug URL |
| Global değişken ($) | 2 | $monday — her yerden erişim |
| Hash | 2 | Key-value Ruby yapısı |
| has_many | 7 | Model ilişkisi |
| has_many :through | 7 | Ara tablo ile ilişki |
| has_one | 7 | Bire-bir ilişki |
| HABTM | 7 | Çoktan çoğa, join table |
| HTTP Metotları | 4 | GET POST PUT PATCH DELETE |
| I18n | 9 | Çoklu dil (t, l, locale) |
| Instance variable (@) | 2 | Nesneye ait değişken |
| **Kalıtım (Miras)** | 2 | class Dog < Animal, super |
| **Kapsülleme** | 2 | @name, getter/setter, attr_* |
| Lambda vs Proc | 2 | Argüman toleransı farkı |
| Migration | 3 | Veritabanı şema değişikliği |
| Modül (Module) | 2 | include, namespacing |
| MVC | 2 | Model View Controller |
| Normalization | 8 | Veriyi kaydetmeden düzenleme |
| ORM | 3 | Tablo ↔ Sınıf eşlemesi |
| Partial | 5 | _form.html.erb yeniden kullanım |
| Polimorfizm | 2 | speak metodunu override etme |
| private / protected / public | 2 | Erişim kontrolü |
| Strong Parameters | 5 | params.require.permit |
| Symbol | 2 | :user tekil nesne |
| Validation | 8 | validates kuralları |
| Class variable (@@) | 2 | Sınıfa ait değişken |

### OOP Kavramları (Hafta 2 — Mutlaka Bil)

| Kavram | Ruby'de Nasıl? | Örnek |
|--------|----------------|-------|
| **Kapsülleme** | Instance variable @ ile gizle, getter/setter ile eriş | `@name`, `attr_accessor :name` |
| **Kalıtım (Miras)** | Alt sınıf üst sınıftan türetilir | `class Dog < Animal` |
| **Polimorfizm** | Alt sınıf metodu override eder | `def speak; "I'm a dog"; end` |
| **super** | Üst sınıf metodunu çağırır | `super + " from Cat class"` |
| **Abstraction** | Modül/sınıf ile arayüz tanımlama | `module Movable` |

## Hafta 2 — Ruby & Rails Giriş

### 2. Hafta Ders İçeriği

- Ruby Programlama Diline Giriş

- Rails Blog Projesinin İlklenmesi

- Rails Dizin Yapısı

- MVC Mimarisi

### Ruby

1995 yılında Yukuhiro "Matz" Matsumoto tarafından geliştirilen

Ruby, açık kaynaklı ve nesne yönelimli bir programlama dilidir.

En son kararlı sürüm 4.0.1 sürümüdür.

Ruby’de her şey nesnedir.

### Ruby Veri Türleri - Integer

Integer, tam sayıları ifade eder. Pek çok programlama dilinde sayılar, stringler

primitive (ilkel/basit) tiplerdir, nesne değildirler. Ruby'de sayılar dahil her şey

nesnedir.

```ruby
3.class # => Integer
3.class.superclass # => Numeric
3.class.superclass.superclass # => Object
3.class.superclass.superclass.superclass # => BasicObject
Demek ki hiyerarşi şu şekilde:
Integer < Numeric < Object < BasicObject
```

### Ruby Veri Türleri - Integer

Integer için kullanılabilir metotlara herhangi bir sayı değerinde methods

metodu ile ulaşabilirsiniz. (ör: 3.methods)

```ruby
# Sayısal değeri String'e çevirir
5.to_s # => "5"
# Sıfır mı?
5.zero? # => false
# Çift sayı mı?
5.even? # => false
# Tek sayı mı?
5.odd? # => true
```

### Ruby Veri Türleri - Float

Float, ondalıklı sayıları ifade eder. Float için kullanılabilir metotlara herhangi

bir float değerinde methods metodu ile ulaşabilirsiniz. (ör: 3.6.methods)

```ruby
# Float’ı Integer'a çevirir
3.6.to_i # => 3
# Negatif sayı mı?
3.6.negative? # => false
# Kendisinden küçük veya ona eşit en büyük sayıyı döndürür.
3.6.floor # => 3
# Kendisinden büyük veya ona eşit en küçük sayıyı döndürür.
3.2.ceil # => 4
```

### Ruby Veri Türleri - String

```ruby
mesaj = "Merhaba"
mesaj.class # => String
mesaj.class.superclass # => Object
mesaj.class.superclass.superclass # => BasicObject
mesaj.class.superclass.superclass.superclass # => nil
Demek ki hiyerarşi şu şekilde:
String < Object < BasicObject
```

### Ruby Veri Türleri - String

```ruby
"MERHABA".downcase    # => "merhaba"
"merhaba".upcase      # => "MERHABA"
"Merhaba".swapcase    # => "mERHABA"
"merhaba".capitalize  # => "Merhaba"
"   merhaba  ".strip  # => "merhaba"
"  merhaba".lstrip    # => "merhaba"
"merhaba  ".rstrip    # => "merhaba"
"merhaba".reverse     # => "abahrem"
"dünya".prepend("Merhaba ") # => "Merhaba dünya"
String.new.methods ile kullanılabilecek tüm string metotlarını öğrenebiliriz.
```

### Ruby Veri Türleri - String

```ruby
%w{foo bar baz}       # => ["foo", "bar", "baz"]
%w{foo bar baz}.class # => Array
%w Array üretir.
%i{foo bar baz} # => [:foo, :bar, :baz]
%i içinde Symbol olan Array üretir.
String içinde değişken kullanmak için #{} interpolation kullanılır.
yas = 18
puts "Siz #{yas} yaşındasınız."
Siz 18 yaşındasınız.
```

### Ruby Veri Türleri - Array

```ruby
a = []
b = Array.new
c = Array.new(5) # => [nil, nil, nil, nil, nil]
d = [2, "foo", 1.8, :bar] # => [2, "foo", 1.8, :bar]
years = Array(2022..2025) # => [2022, 2023, 2024, 2025]
years[0] # => 2022
years[-1] # => 2025
İçinde her tür Ruby objesini taşıyabilen bir nesnedir.
```

### Ruby Veri Türleri - Array

```ruby
[1, 2, 3, 4].length # => 4
[1, 2, 3, 4].count # => 4
[1, 2, 3, 4].include?(3) # => true
[1, 2, 3, 4].first # => 1
[1, 2, 3, 4].first(2) # => [1, 2]
[1, 2, 3, 4].last # => 4
[2, 8, 1, 9].sort # => [1, 2, 8, 9]
["a", 1, nil, 2, 1, "a"].compact # => ["a", 1, 2, 1, "a"]
["a", nil, 2, nil, "b", 1, "a"].uniq # => ["a", nil, 2, "b"]
[1, 2, ["a", "b", :c]].flatten # => [1, 2, "a", "b", :c]
```

### Ruby Veri Türleri - Array

```ruby
# Dizileri birleştirme
a, b = [2, 3, 5], [5]
a + b # => [2, 3, 5, 5]
# İki diziyi uniq olarak birleştirme
a | b # => [2, 3, 5]
# İki diziyi birleştirme
a.concat([4, 6, 7]) # => [2, 3, 5, 4, 6, 7]
# Diziler arası fark
a - b # => [2, 3, 4, 6, 7]
```

### Ruby Veri Türleri - Array

```ruby
a = [2, 3, 5]
# Dizi sonuna eleman ekleme
a << 7 # => [2, 3, 5, 7]
a.push(8) # => [2, 3, 5, 7, 8]
# Dizi başına eleman ekleme
a.unshift(1) # => [1, 2, 3, 5, 7, 8]
# Dizi elemanını sondan ve baştan silme
a.pop # => 8  a # => [1, 2, 3, 5, 7]
a.shift # => 1  a # => [2, 3, 5, 7]
# Belirtilen dizi elemanını silme
a.delete(2) # => 2 a # => [3, 5, 7]
```

### Ruby Veri Türleri - Hash

```ruby
h = Hash.new() # => {}
h[:name] = "Kerim"
h[:last_name] = "Bayrak"
h # => {:name=>"Kerim", :last_name=>"Bayrak"}
h.keys # => [:name, :last_name]
h[:name] # => "Kerim"
h.values # => ["Kerim", "Bayrak"]
h.value?("Kerim") # => true
h.key?(:name) # true
Key-Value çifti barındıran yine Array’e benzeyen başka bir nesnedir.
```

### Ruby Veri Türleri - Symbol

```ruby
"user".to_sym # => :user
Symbol (sembol) Ruby’e ait özel bir nesnedir. Bir tür yer tutucu görevindedir.
: işareti ile başlayan her şey semboldür. Sembolün, değişkenden en önemli
farkı tekil olmasıdır. Yani sembole atanan değişkenden hafızada 1 adet
bulunur.
"hello".object_id  # => 322080
"hello".object_id  # => 323700  Her seferinde yeni bir nesne oluşturuluyor.
:hello.object_id   # => 3040348
:hello.object_id   # => 3040348
```

### Fonksiyonlar (Methods)

```ruby
def hello
"Merhaba"
end
hello
=> "Merhaba"
Ruby’de eğer return ile bir değer
döndürülmezse çalıştırılan en son satırın
değeri döndürülür.
def hello(name)
"Merhaba #{name}"
end
hello("Merve")
=> "Merhaba Merve"
Fonksiyonlar parametre alır. Default bir
değer de atanabilir.
def hello(name="Duygu")
"Merhaba #{name}"
end
hello
=> "Merhaba Duygu"
```

### Metot Yazma Kuralları

? ile biten method mutlaka true ya da false döner.

```ruby
a = "ebru"
b = "ebru"
a.eql? b  # => true
! ile biten method tehlikeli bir iş yaptığını anlatır.
a = "deneme"
a.upcase   # => "DENEME"
a          # => "deneme"
a.upcase!  # => "DENEME"
a          # => "DENEME"
```

### Değişken Sayıda Argümanlar

Fonksiyonlara değişken sayıda parametre geçmek gerekebilir. Bu

durumda argümanın başına * işareti gelir.

```ruby
def merhaba(*isimler)
"Merhaba #{isimler.join(' ve ')}"
end
merhaba("merve", "hasan")
# => "Merhaba merve ve hasan"
```

### Local Değişkenler

```ruby
out_text = "aslı"
def greet_user(user_name)
out_text = "Merhaba #{user_name}"
end
puts greet_user("poyraz")  # Merhaba poyraz
puts out_text              # aslı
Küçük harfle [a-z] veya _ ile başlayabilir.
Fonksiyon içindeki out_text ile dışındaki değişkenin kapsamları farklı.
```

### Global Değişkenler ve Sabitler (Constants)

$monday = "Pazartesi"

$ işaretiyle başlayan tüm değişkenler Global değişkenlerdir. Kodun

herhangi bir yerinde kullanılabilir ve erişilebilir.

Sabitler büyük harfle başlar ve genelde tüm harfleri büyük yazılırlar.

Değeri değiştirilmesi beklenmeyen değişkenlerdir.

PI = 3.14

### Sınıflar (Classes)

Sınıflar birbiri ile ilişkili birden fazla metodun

bir arada durmasını sağlar.

```ruby
class Animal
def speak
"Hello!"
end
end
class Dog < Animal
def speak
"I’m a dog"
end
end
class Cat < Animal
def speak
super + " from Cat
class"
end
end
animal = Animal.new
animal.speak # => Hello!
kopek = Dog.new
kopek.speak # => I’m a dog
kedi = Cat.new
kedi.speak # => Hello! from Cat class
class Animal
def initialize(name)
@name = name
end
def name=(name)
@name = name
end
def name
"#{@name}"
end
end
Instance variable, bir nesneye ait olan ve o
nesnenin state’ini temsil eden
değişkendir ve @ ile başlarlar.
Eğer bir method = ile bitiyorsa bu, o
method’un bir setter metodu olduğu
anlamına gelir.
a = Animal.new("Wolf")
a.name   # Wolf
a.name = "Haski"
a.name   # Haski
getter ve setter metodları kapsüllenmiş nesne özelliklerine erişmek ve
değiştirmek için kullanılan metodlardır.
class Animal
attr_accessor :name
def initialize(name)
@name = name
end
def hello
"Hello #{name}"
end
end
attr_accessor @name örnek değişkeni için
hem setter hem de getter metodu oluşturur.
Sadece getter metodu oluşturmak için
attr_reader, sadece setter metodu
oluşturmak için attr_writer kullanılabilir.
a = Animal.new("Wolf")
a.hello       # Hello Wolf
a.name       # Wolf
a.name = "Haski"
a.name         # Haski
```

### Sınıf Değişkeni

```ruby
class CoffeeMachine
attr_accessor :name
@@coffee_number = 0
def initialize(name)
@name = name
@@coffee_number += 1
end
def self.sold_coffee_count
@@coffee_number
end
end
@@ işareti ile başlarlar.
Sınıfa ait değişkenlerdir.
Kullanmadan önce
değişken tanımlanmalıdır.
coffee1 = CoffeeMachine.new("Latte")
coffee2 = CoffeeMachine.new("Americano")
puts "Kaç defa Coffee instance'ı oluştu? #{CoffeeMachine.sold_coffee_count}"
Kaç defa Coffee instance'ı oluştu? 2
```

### Erişim Metotları Public, Private ve Protected

Sınıf içerisindeki metotlar erişilebilirlik

açısından kısıtlanabilir. public olanlar

her yerden erişilebilirken, private

olana sadece dolaylı (implicit) olarak

erişilebilir, protected olana ise hem

dolaylı hem de alt sınıftan erişilebilir.

```ruby
class User
def public_message
private_message
protected_message
end
private
def private_message
puts "Bu private metot."
end
protected
def protected_message
puts "Bu protected metot."
end
end
u = User.new
u.private_message # Error
u.protected_message # Error
u.public_message
"Bu private metot."
"Bu protected metot."
```

### Modül (Module)

Bir modül, metotlar ve sabitlerin bir koleksiyonudur. Sınıflar gibi

türetilemezler. Sınıflara modüller include edilerek modül metotları sınıf

içerisinde kullanılabilir.

module Movable

```ruby
def move
"I’m moving"
end
end
class Animal
include Movable
end
Animal.new.move # => "I’m moving"
```

### Modül (Module) Namespacing

Modül içerisinde modül tanımlanabilir.

module Framework

VERSION = 5

module HttpFunctions

```ruby
def self.fetch_url
"This is url fetcher"
end
end
end
Framework::VERSION  # => 5
Framework::HttpFunctions.fetch_url
# => "This is url fetcher"
```

### Bloklar

### Bloklar do/end ile ya da { } ile sarmalanmışlardır. Bloklar için each, map,

select, and find metotları sıklıkla kullanılır.

```ruby
numbers = [2, 5, 8]
numbers.each { |number| puts number }
# 2
# 5
# 8
[1, 2, 3, 4, 5].map do |num|
num * 2
end
#=> [2, 4, 6, 8, 10]
```

### Bloklar

```ruby
def test_function
yield
end
test_function {
puts "Merhaba"
}
test_function do
puts "Ben block içinden geliyorum"
end
test_function do
[1, 2, 3, 4].each do |n|
puts "Sayı #{n}"
end
end
```

### Bloklar

```ruby
def test_function
yield
end
test_function metoduna herhangi bir blok girdisi vermezsek no block given
(yield) hatası alırız. Bunu önlemek için:
def test_function
if block_given?
yield
else
puts "Lütfen blok giriniz!"
end
end
```

### Proc (Procedures) ve Lambda

İkisi de bir değişkende saklanabilen ve yeniden kullanılabilen bir kod bloğu

içerir.

```ruby
# Creating a Proc
my_proc = Proc.new { |name| puts "Hello, #{name}!" }
# Calling the Proc
my_proc.call("Alice")  # Hello, Alice!
# Creating a Lambda
my_lambda = lambda { |name| puts "Hello, #{name}!" }
# Alternative syntax using ->
# my_lambda = ->(name) { puts "Hello, #{name}!" }
# Calling the Lambda
my_lambda.call("Bob")  # Hello, Bob!
```

### Proc (Procedures) ve Lambda Farkları

Proc’ta yanlış sayıda argüman verilirse, fazlalıkları yok sayar veya eksik olanları

sıfıra ayarlar. Lamda’da yanlış sayıda argüman verilirse hata oluşturur.

```ruby
my_proc = Proc.new { |x, y| puts "Sum: #{x + y}" }
# Pass fewer arguments
my_proc.call(3)  # Output: Sum: 3
# Pass more arguments
my_proc.call(3, 4, 5)  # Output: Sum: 7
my_lambda = lambda { |x, y| puts "Sum: #{x + y}" }
my_lambda.call(3) # Output: ArgumentError: wrong number of
arguments (given 1, expected 2)
my_lambda.call(3, 4, 5)  # Output: ArgumentError: wrong number of
arguments (given 3, expected 2)
```

### Koşullar

a, b = 5, 9

if a == b

puts "a, b'ye eşit"

elsif a < b

puts "a, b'den küçük"

else

puts "a, b'den büyük"

```ruby
end
unless a == b
puts "a, b’ye eşit değil"
end
```

### for Döngüsü

for i in 1..3

puts "i = #{i}"

```ruby
end
# i = 1
# i = 2
# i = 3
```

### ternary Operatörü

Kısaltılmış if yapısıdır.

```ruby
amount = 2
result = amount == 1 ? "apple" : "apples"
puts "#{amount} #{result}."
```

### Github Classroom Proje Depo Oluşturma Linki

Aşağıda belirtilen linke tıklayın ve ödevi kabul edin. Github hesabınızda

sizin öğrenci numaranızla (kullanıcı adınız) biten bir repo oluşacaktır.

### Rails blog uygulamasında yapacağımız bütün geliştirmeler için artık bu

repo kullanılacaktır.

A Sınıfı: https://classroom.github.com/a/6IGCNVNj

B Sınıfı: https://classroom.github.com/a/JkQ9HsoV

### Son Kontroller

node ve npm kurulum kontrolü:

node -v

npm –v

yarn -v

Yoksa kur:

sudo apt update

sudo apt install nodejs npm

Yarn kurulumu:

npm install -g yarn

### Rails Blog Uygulamasının Oluşturulması

```ruby
rails new blogger-a-ogrencino -d postgresql --css bootstrap
```

### Rails blog uygulaması, postgresql veritabanı ve bootstrap kütüphanesi

kullanılarak aşağıdaki gibi oluşturulur. blogger-a-ogrencino Github’da

oluşturulan repo ismiyle aynı olduğuna dikkat edin. Dikkat! ogrencino kısmı

kendi öğrenci numaranız olacak.

Yukarıdaki kodu çalıştırdığınızda blogger-a-ogrencino adında bir rails projesini

ilklendirmiş (başlatmış) olacaksınız.

### Blog Uygulamasının Github’a Gönderilmesi

Oluşturulan proje dizinine girebilmek için wsl terminalden:

cd blogger-a-ogrencino

Ardından yerelimizde oluşturduğumuz projeyi Github’da oluşturulan repoya

bağlamak için şu kodlar sırasıyla çalıştırılır:

```ruby
git init
git remote add origin https://…
Github arayüzünden erişebileceğiniz repo url’ini kopyalayın ve uzak makine ismi
(origin) olarak ekleyin.
```

### Blog Uygulamasının Github’a Gönderilmesi

Kodları çalıştırırken proje dizininde olmanız gerektiğini unutmayın!

Proje dosyalarını git’e eklemek için:

```ruby
git add .
Ne yaptığımıza dair açıklayıcı bir mesaj eklemek için:
git commit -m "First commit"
Artık Github’daki repoya yereldeki dosyaları gönderebiliriz.
git push –u origin main
Gönderme işleminden sonra Github arayüzünden bu dosyaları görebilmeniz gerekir.
```

### Blog Uygulamasının Veritabanı Ayarı

code .

Proje dizinindeyken vscode ile projeyi açmak için aşağıdaki kod çalıştırılır.

Dilerseniz vscode’u açtıktan sonrada Open Folder diyerek de rails projenizi

seçebilirsiniz.

Uygulamanın çalışabilmesi için veritabanının oluşturulması gerekmektedir.

config dizini altında database.yml dosyası içerisinde development altında pg

### veritabanı username ve password bilgileri eklenmesi gerekmektedir.

Bu bilgilerin postgresql kurarken oluşturduğunuz

username ve password olduğunu unutmayın. Şahsi

bilgisayarlarda bu değerleri farklı oluşturmuş

olabilirsiniz.

Blog Uygulamasında Veritabanı Oluşturma

### Veritabanı username ve password belirttikten sonra artık veritabanları

oluşturulabilir. Bunun için de rails db:create kodu çalıştırılır. Bu kod hem

development ortamı hem de test ortamı için veritabanlarını oluşturur. Dikkat

ettiyseniz herhangi bir SQL kodu yazmamıza gerek kalmadı.

```ruby
rails db:create
Created database 'blogger_development'
Created database 'blogger_test'
```

### Rails Uygulamasının Çalıştırılması

Artık uygulama çalışmaya hazır

durumda. Aşağıdaki kod

çalıştırıldığında localhost:3000’de

uygulamanız çalışacaktır.

```ruby
rails s
Farklı bir portta çalıştırmak için:
rails s -p 3001
```

### Rails Dizin Yapısı

### Rails uygulamasının

yapısını oluşturan bir dizi

otomatik oluşturulmuş

dosya ve klasör mevcuttur.

### Rails Dizin Yapısı

README.md: Uygulama hakkında bilgiler, nasıl kullanılacağının

belirtilmesi gibi bilgiler bu dosyaya kaydedilir.

.gitignore: git’in gözardı etmesini istediğimiz dosyalar belirtilir.

/log/*

/tmp/*

!/log/.keep

!/tmp/.keep

/tmp/pids/*

!/tmp/pids/

!/tmp/pids/.keep

/config/master.key

.gitignore

### Rails Dizin Yapısı

app: Geliştirme süreci çoğunlukla bu dizin altında gerçekleşmektedir.

controllers Kullanıcıdan gelen istekleri alır,

model ve view ile etkileşimde

bulunarak uygun yanıtları üretir.

models Uygulamanın veri yapısını ve iş

mantığını temsil eder. Veritabanı

ile etkileşimde bulunur.

views

posts_controller.rb

post.rb

posts

index.html.erb

edit.html.erb

new.html.erb

Projenin arayüzlerinin oluşturulduğu

bölümdür. Kullanıcılardan alınan

istekleri controller’a iletir.

### Rails Dizin Yapısı - config

config: Uygulama ayarlarının ve yapılandırmalarının yer aldığı dizindir.

database.yml Veritabanı konfigürasyonu

Sistemin çoklu dil desteğinin sağlandığı dizin

routes.rb Uygulama yolları (urls)

importmap.rb JS paketlerinin eklendiği dosya

locals

tr.yml

en.yml

### Rails Dizin Yapısı - config

environments

RAILS_ENV değiştirilmezse geliştirme ortamı

default olarak “development” olacaktır.

development.rb

production.rb

test.rb

➜ rails c

Loading development environment (Rails

8.0.1)

```ruby
blogger(dev)> Rails.env
=> "development"
blogger(dev)> Rails.env.production?
=> false
config
```

### Rails Dizin Yapısı - config

master.key

▤ credentials.yml.enc

### Veritabanı şifreleri, API anahtarları vs. gizli

tutulması gereken bilgiler

credentials.yml.enc dosyasında şifreli bir

şekilde tutulur.

Bu dosyanın şifresi master.key

kullanılarak çözülür ve içerik bilgilerine

ulaşılır. Bu dosya .gitignore dosyasının

içerisine eklenmelidir

EDITOR="code --wait" rails credentials:edit

config

### Rails Veritabanı Kullanıcı Adı ve Parolayı Credentials’a Kaydetme

Rails.application.credentials.dig(:pg, :username)

Rails.application.credentials.pg[:username]

Rails c giriş yaptıktan sonra yukarıdaki postgresql bilgilerine aşağıdaki gibi

erişilebilir.

myo

database.yml Dosyasındaki Veritabanı Bilgilerini Güncelle

```ruby
<%= Rails.application.credentials.dig(:pg, :username) %>
<%= Rails.application.credentials.dig(:pg, :password) %>
<% %> bu aralıkta ruby kodu çalıştırılır. Çıktı elde etmek için <%= %>
kullanılmalı.
```

### Rails Dizin Yapısı

db: Veritabanı ile ilgili dosyaların bulunduğu dizindir.

schema.rb

seed.rb

migrations

20241020111632_create_units.rb

### Veritabanı şeması

### Veritabanı için ön tanımlı verilerin oluşturulduğu dosya

### Veritabanı şemasını nasıl değiştirileceğini tanımlayan

Ruby sınıfları.

Bu dosya 20/10/2024 tarihinde 11:16:32’de oluşturulmuştur.

### Rails Dizin Yapısı

public: Uygulamanın kullanıcılar tarafından erişilebilir olan dosyalarının

bulunduğu dizindir.

log: Uygulama log dosyalarını içerir.

development.log Geliştirici ortamı logları

test.log Test ortamı logları

production.log Production ortamı logları

### Rails Dizin Yapısı

test: Uygulama için yazılmış test dosyalarının bulunduğu dizindir.

controllers Controller sınıfları için uygulanan testler

models Model validation testleri

fixtures Testler için kullanılan veri örnekleri

helpers Helper sınıfları için uygulanan testler

### Rails Dizin Yapısı

vendor: Tüm üçüncü party kütüphane dosyalarının bulunduğu dizin.

package.json: Uygulama için hangi npm bağımlılıklarının gerekli

olduğunu belirtmemizi sağlar.

### Rails Dizin Yapısı

Gemfile: Uygulamanın gem bağımlılıklarının belirtildiği dosyadır.

Gemfile.lock: Yüklenen kütüphanelerin tam versiyon ve bağımlılıklarının

belirtildiği dosyadır. Bundler bu dosyayı otomatik günceller.

### Rubygems

Ruby geniş bir üçüncü parti kütüphanesine sahiptir.

### RubyGems, kütüphanelerin oluşturulması, paylaşılması ve kurulumu için tasarlanmış

bir Ruby paketleme sistemidir.

Kütüphanelerin barındırıldığı ana mekan RubyGems.org‘dur. Bu depoda gemleri

bulup makinenize kurabilirsiniz. RubyGems web sitesini kullanarak ya da gem

komutu ile gemleri arayabilirsiniz.

gem search -r rails

gem search -r paginate

Bir gem kurmak için gem install gem_name komutunu kullanın. Kurulu gemleri

taramak için gem list komutunu kullanabilirsiniz.

### Rails MVC

routes.rb

```ruby
get "/users", to: "users/index"
```

### Rails Anasayfa Güncelleme

Anasayfaya Merhaba Rails yazdıralım.

Bunun için view, controller sayfalarının ve routes dosyasında bu sayfanın

yolunun oluşturulması gerekmektedir.

```ruby
class HomeController < ApplicationController
def index; end
end
app/controllers/home_controller.rb
root "home#index"
config/routes.rb
<h1>Merhaba Rails</h1>
app/views/home/index.html.erb
```

### Kaynaklar

- https://www.rubyguides.com/ruby -tutorial/

- https://docs.ruby-lang.org/en/master/index.html

- https://guides.rubyonrails.org/

- https://www.ruby-lang.org/tr/

- https://rubymonk.com/

---

## Hafta 3 — ORM & Active Record

Ecmel Albayrak

### 3. Hafta Ders İçeriği

- ORM (Object Relational Mapping) nedir?

- Active Record nedir?

- Rails console işlemleri

- Rails migration yapısı

### ORM (Object Relational Mapping) Nedir?

Nesneleri ilişkisel olarak eşleştirme olarak adlandırılır. Veritabanında oluşturulan

her bir tabloya karşılık uygulama tarafında bir sınıf/model oluşturulur. ORM

tekniği belli bir programlama diline bağlı değildir ve her nesneye yönelik dillerde

yazılabilir/kullanılabilir.

### ORM ile SQL sorgusu yazmadan veritabanına DDL (Data Definition Language)

ve DML (Data Manipulation Language) sorguları yapılabilir.

DMLDDL

Create: Yeni bir db nesnesi oluştur

Alter: Var olan db nesnesini günceller

Drop: Var olan db nesnesini siler

Select: Db’deki verileri sorgular

Insert: Db’ye yeni veri ekler

Update: Var olan verileri günceller

Delete: Db’deki verileri siler

Customer

first_name

last_name

customer_no

string

string

integer

ORM

customers

PK id bigint not null

first_name varchar(50) not null

last_name varchar(50) not null

customer_no int not nullMapping

Model/Sınıf Tablo

İlişkisel VeritabanıNesne Yönelimli Programlama

ORM, veritabanı tabloları ile nesne yönelimli programlama dilindeki sınıflar

arasında bir haritalama (mapping) sağlar.

### ORM (Object Relational Mapping) Nedir?

Nesne Yönelimli Programlama

Nesneler

İlişkisel Veritabanı

Satırlar

persons

### ORM (Object Relational Mapping) Nedir?

Nesne Yönelimli Programlama

Attribute

İlişkisel Veritabanı

Column

personsclass Person:

```ruby
first_name = “John”
last_name = “Connor”
phone = “+16105551234”
```

### ORM (Object Relational Mapping) Nedir?

Nesne Yönelimli Programlama

İlişkiler

İlişkisel Veritabanı

Foreign Keys

Customer

has_many :orders

id

first_name

last_name

customer_no

integer

string

string

integer

Order

belongs_to :customer

id

product

date

customer_id

integer

string

string

integer

customers

PK id bigint not null

first_name varchar(50) not null

last_name varchar(50) not null

customer_no integer not null

orders

PK id bigint not null

product varchar(255) not null

date date not null

customer_id bigint not null

### ORM Kullanmanın Avantajları

- Daha az SQL sorgusu yazmayı sağlar.

- Nesneye yönelik bir programlama imkanı sağlar.

- Veritabanı platformu bağımlılığı yoktur. Postgresql kullanıyorken

Mysql geçişini sorunsuzca gerçekleştirebiliriz.

- Veritabanı modellemesi uygulama tarafında yapılabilir.

- Geliştirme ve bakım maliyeti düşüktür.

Dillere Göre ORM Araçları

- Ruby: ActiveRecord, DataMapper

- Java: JPA, Hibernate, EJB, Ebean

- C#: Entity Framework, Dapper, ECO, XPO

- Php: CakePHP, Codelgniter, RedBean, Doctrine,

- Python: Django, South, Storm

- Go: Gorm

### ActiveRecord Nedir?

MVC mimarisinde model katmanını oluşturan ORM (Object Relational

Mapping) kütüphanesidir. Model, veri ve business logic’ten sorumlu sistem

katmanıdır.

### Active Record, kalıcı depolama gerektiren Ruby nesnelerini bir veritabanına

kaydetmenize ve kullanmanıza yardımcı olur.

Business Logic nedir?

Verilerin nasıl oluşturulacağını, depolanacağını ve değiştirileceğini

belirleyen iş kurallarını kodlayan programın bir parçasıdır.

### ActiveRecord Nedir?

### Veritabanındaki her bir tablo bir sınıfa karşılık gelmektedir.

Model/Sınıf Tablo/Şema

Article articles

CourseAssessment course_assessments

Deer deers

Mouse mice

Person people

### Tür Açıklama

string Metin değerlerini depolamak için kullanılır. Varsayılan olarak

dizelerin maksimum uzunluğu 255 karakterdir.

text string'den daha uzun metin değerlerini depolamak için kullanılır.

(65.535 karaktere kadar)

### Active Record’un Desteklediği Veri Türleri

### Tür Açıklama

integer Tam sayıları depolamak için kullanılır. Tam sayılar -2147483648

ile 2147483647 arasındaki değerleri tutabilir.

float Ondalıklı sayıları depolamak için kullanılır. Varsayılan olarak,

kayan noktalı sayılar 8 bayt bellek kullanılarak depolanır.

boolean true/false değerlerini depolamak için kullanılır.

### Active Record’un Desteklediği Veri Türleri

### Tür Açıklama

decimal

float'a benzerdir, ancak ondalık değerlerin hassasiyetini (yani

ondalık noktadan sonraki basamak sayısını) belirtmenize olanak

tanır. Yüksek hassasiyet düzeyinde depolamanız gereken

finansal veriler için kullanılır.

precision burada 10

scale burada 4

Precision 4, scale 2: 99.99

Precision 8, scale 3: 99999.999

### Active Record’un Desteklediği Veri Türleri

### Tür Açıklama

date Sadece yıl, ay, gün depolamak için kullanılır.

datetime Tarih ve saat değerlerini depolamak için kullanılır.

timestamps

datetime'a benzerdir, ancak hem kaydın ne zaman

oluşturulduğunu (created_at) hem de ne zaman güncellendiğini

(updated_at) depolar.

### Active Record’un Desteklediği Veri Türleri

### Rails Model Oluşturma

Blog uygulamasında oluşturulacak içerikler için bir model oluşturulması

gerekmektedir. Model ismi Post olsun. İçerik başlığı için title, içerik metni için

article alanlarını oluşturalım.

```ruby
rails g model Post title article:text
veri türü belirtilmezse default string olur.
```

### Veri Tabanı Tablosu Oluşturma

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
db/migrates/20241216100235_create_posts.rb dosya içeriği
CREATE TABLE posts (
id int(11) NOT NULL auto_increment,
title varchar(255),
article text(65536),
PRIMARY KEY  (id)
);
SQL kodu yazmaya gerek yok
created_at updated_a
t
db/migrates/20241216100235_create_posts.rb dosyasını işleme alarak veri
tabanında posts tablosu oluşması için aşağıdaki kod çalıştırılır.
rails db:migrate
psql -U myo -d blogger_development
blogger_development=# \dt
```

### Veri Tabanı Tablosu Oluşturma

### Veri tabanına bağlanıp tabloları görüntüleyin:

Dikkat! Sizin veritabanı

adınız farklı olabilir.

Dikkat! Sizin kullanıcı adınız farklı olabilir.

### Veritabanındaki posts tablosunun kolonlarını görüntüleyelim.

psql -U myo -d blogger_development

blogger_development=# \d posts;

Pg Veritabanı Kolonları Görüntüleme

### Post modelini oluşturduktan sonra uygun bir mesaj ile yapılanları Github’a

göndermek için şu adımlar sırasıyla gerçekleştirilir.

```ruby
git status # Hangi dosyalarda değişiklik yapılmış görün.
git add .  # Yapılan değişiklikleri ekleyin.
git commit -m "Create post model" # Uygun bir mesaj ekleyin.
git push origin main # main branch’ine yapılan değişikleri gönderin
Yapılan Değişiklikleri Github’a Gönderelim
```

### Konsolda Rails Modeliyle Etkileşim

```ruby
rails c # konsola giriş
Post.column_names
=> ["id", "title", "article", "created_at", "updated_at"]
Yeni bir post kaydı oluşturalım.
post = Post.new(title:"Git Commit Komutu", article:"Lorem
ipsum …")
```

### Konsolda Rails Modeliyle Etkileşim

```ruby
post = Post.new(title:"Git Commit Komutu", article:"Lorem
ipsum …")
post değişkeni bir Post sınıf örneğidir (instance). Veri tabanına henüz
kaydedilmediği için id, created_at ve updated_at zaman damgaları nil’dir.
```

### Konsolda Rails Modeliyle Etkileşim

### Veri tabanına kaydetmek için save etmeliyiz.

### Veri tabanına kaydedildikten sonra post içeriği:

### Konsolda Rails Modeliyle Etkileşim

save metoduna benzer şekilde tek bir çağrıda active record nesnesini oluşturup

kaydetmek için create kullanılabilir.

Post.create(title:"Git Status Komutu", article:"")

### Veritabanındaki Kayıtlara Model Üzerinden Ulaşmak

Post.all

```ruby
Post.count # => 2
```

### Veritabanındaki Kayıtlara Model Üzerinden Ulaşmak

```ruby
# İlk oluşturulan blog kayıt verisine ulaşmak için:
Post.first
# İlk 10 blog kaydını getirmek için:
Post.first(10)
# İkinci oluşturulan blog kayıt verisine ulaşmak için:
Post.second
# Son oluşturulan blog kayıt verisine ulaşmak için:
Post.last
# Son oluşturulan 10 blog kaydını getirmek için:
Post.last(10)
```

### Veritabanındaki Kayıtlara Model Üzerinden Ulaşmak

Post.take

Post Load (0.8ms)  SELECT `posts`.* FROM `posts` LIMIT 1

Sıralamaya bakmadan bir kayıt bulmak için:

Post.take(2)

Post Load (0.7ms)  SELECT `posts`.* FROM `posts` LIMIT 2

Sıralamaya bakmadan herhangi iki kaydı bulmak için:

### Veritabanından Verilere Ulaşılması

psql -U myo -d blogger_development

```ruby
# Veritabanına giriş yaptıktan sonra aşağıdaki kod çalıştırılır.
select * from posts;
```

### Veritabanındaki Verileri Filtreleme

Post.where(title:"Git Commit Komutu")

Post.where('title LIKE ?',"%Commit%")

İçerisinde commit yazısı geçen kayıtları bulmak için:

Filtreleme işlemi where ile yapılabilir.

### Where not ve Where or Kullanımı

Post.where.not(title: nil)

Blog girdi başlığı nil olmayanları bul.

Blog girdi başlığı boş olmayan veya blog metni (article) boş olanları bul.

Post.where.not(title: nil).or(Post.where(article: nil))

### Where and Kullanımı

Post.where.not(title: nil).where(article: nil)

İç içe where ve and kullanılabilir.

Title ve article bilgisi boş olmayan post girdilerini bul.

Post.where(id: [1, 2]).and(Post.where.not(title: nil))

Id değeri 1 veya 2 olan ve title bilgisi boş olmayan post girdilerini bul.

### Veritabanındaki Verileri İstenen Sırada Getirme

Varsayılan olarak sıralama artan (ascending) şekilde yapılır.

Post.order(:created_at)

Azalan (descending) şekilde sıralamak için:

Post.order(created_at: :desc)

### Spesifik Bir Kayıt Bulma

Post.find(1)

Tek bir id’ye göre arama yapmak için find metodu kullanılır.

Select sorgusunda id’si 1 olan kaydı bulmak için WHERE, tek bir kayıt

bulmak için LIMIT kullanılır.

### Spesifik Bir Kayıt Bulma

İstenen alana göre veri bulmak için find_by kullanılır.

Post.find_by(title:"Git Commit Komutu")

find_by

Tek bir kayıt veya

nil döner

find

id’ye göre tek kayıt bulur

bulamazsa hata/istisna

(exception) oluşur.

where

### ActiveRecord::Relation

nesnesi döner

Tek bir kayıt bulmak için find_by, birden fazla kayıt bulmak için where

kullanılmalı.

### Spesifik Bir Kayıt Bulma

Post.find([1, 3])

Array olarak birden fazla değer de aranabilir.

Aşağıdaki kodları, kaydı bulunmayan id değerleri bulmak için kullanın

(örneğin 3 id değerine sahip bir post kaydı olmasın) ve çıkan sonuçları

karşılaştırın.

Post.find_by(id: [1, 3])

### Kayıtları Güncelleme

### Kayıtları güncellemenin 2 yolu var. Biri update kullanmak bir diğeri nesneye

yeni değerleri atadıktan sonra save etmek.

```ruby
post = Post.find(1)
post.update(title:"Başlık Güncelleme")
```

### Kayıtları Güncelleme

Yeni değer atadıktan sonra save etmek.

```ruby
post = Post.find(1)
post.title = "Başlık Güncelleme 2"
post.save
```

### Kayıtları Silmek

### Veritabanından bir kayıt silmek için destroy kullanılır.

Post.first.destroy

Tablodaki tüm verileri silmek için destroy_all kullanılır.

Post.destroy_all

Post.count

### Rails Migration Yapısı

### Migration bir veritabanı şemasının (schema) nasıl değiştirileceğini tanımlayan

bir Ruby sınıfıdır. Migration’lar, genellikle veritabanına yeni bir tablo/sütun

ekleneceği zaman, sütundaki tür değişiklikleri veya tablo ilişkilerindeki

güncellemeler dolayısıyla kullanılır.

### Migration sınıfları ActiveRecord::Migration sınıfını miras alır ve change adında

bir metoda sahiptir.

```ruby
class CreatePosts < ActiveRecord::Migration[8.0]
def change
end
end
```

### Rails Migration Yapısı

Yeni tablo oluşturmak için:

```ruby
rails generate migration CreateUser first_name last_name
```

### Rails Migration Yapısı

Var olan bir tabloya kolon eklemek için:

```ruby
rails g migration AddIdNumberToUser id_number:integer
```

### Rails Migration Yapısı

Var olan bir tablodan kolon silmek için:

```ruby
rails g migration RemoveIdNumberFromUser id_number:integer
```

### Rails Migration Yapısı

Var olan bir tabloyu silmek için:

```ruby
rails g migration DropUser
```

### Rails Migration Yapısı

### Migration dosyası ile yapılan değişiklikleri geri almak için rollback yapılır.

Örneğin posts tablosu oluşturulduktan sonra tabloyu silmek için şu kod

çalıştırılır:

```ruby
rails db:rollback
rails db:migrate:status
down
```

### Rails Migration Status

Rollback STEP parametresi ile istenilen sayı kadar geri gidilebilir.

### Rails Migration Status

Sadece belirli bir migration dosyası versiyon numarası belirtilerek geri

alınabilir.

### Veritabanı Üzerinde Yapılabilecek İşlemler

db:create O andaki ortam için db oluşturur.

db:create:all Tüm ortamlarda db oluşturur.

db:drop Sadece o andaki ortam için db siler.

db:drop:all Tüm ortamlarda db siler.

db:migrate O anki ortamda çalıştırılmamış migration dosyalarını

çalıştırır.

db:migrate:up Tek bir migration çalıştırır.

db:migrate:down Bir migration geri alır.

### Veritabanı Üzerinde Yapılabilecek İşlemler

db:migrate:status Migration durumunu gösterir.

db:rollback Son migration’ı geri alır.

db:seed db/seed.rb dosyasındaki verileri db’ye ekler.

db:schema:load Güncel şemayı veritabanına uygular.

db:setup db:schema:load ve db:seed işlemlerini yapar.

db:reset db:drop ve db:setup işlemlerini yapar.

---

## Hafta 4 — Enum, Routes, Controllers

### 4. Hafta Ders İçeriği

- Post modeline yeni sütun ekleme

- ActiveRecord Enum ve Scopes kullanımı

- Rails routes

- Rails controllers & actions

- Veritabanına seed verisi ekleme

### Post modeline status alanı ekleme

Blog post kaydı için yayına alma (active), yayından kaldırma (passive) ve

düzenlenmesi gerektiğine (must_be_update) dair bilgileri belirtmek için

status alanı ekleyelim.

```ruby
rails g migration AddStatusToPost status:integer
class AddStatusToPost < ActiveRecord::Migration[8.0]
def change
add_column :posts, :status, :integer, default:0
end
end
```

### Post Modeli Sütun Bilgileri

Post

id

title

article

status

created_at

updated_at

integer

string

text

integer

datetime

datetime

### Post modeline status ekledikten sonra kolon bilgileri aşağıdaki gibi

olacaktır.

```ruby
rails db:migrate komutunu çalıştırarak son oluşturulan migration
dosyasıyla veritabanındaki posts tablosuna status alanının eklenmesini
sağlayın.
```

### Active Record Enum

```ruby
class Post < ApplicationRecord
enum :status, {
draft: 0,
published: 1,
inactive: 2
}
end
Yeni post oluşturulduğunda veritabanında default değer 0 olduğu için
status durumu draft olarak oluşturulacaktır.
Enum, sabit değerleri sayısal olarak saklayan ve bize anlamlı isimler
kullanmamızı sağlayan yapı. app/models/post.rb
```

### Active Record Scope

Scope metodu, Rails modellerinin içinde tanımlanan özel sorgulardır.

```ruby
class Post < ApplicationRecord
scope :published, -> { where(status: :published) }
end
Enum olarak tanımlanan değerlerin scope’ları otomatik oluşturduğu için
yukarıdaki gibi scope oluşturmaya gerek yoktur. Eğer enum’la birlikte
scope’ların oluşması istenmiyorsa aşağıdaki gibi belirtilmeli.
class Post < ApplicationRecord
enum :status, {draft: 0, published: 1, inactive: 2},
scopes: false
end
```

### Active Record Scope

Post.published # Status durumu published olan tüm postlar

Post.draft # Status durumu draft olan tüm postlar

Post.inactive # Status durumu inactive olan tüm postlar

```ruby
post = Post.first
post.published?
=> true
post.draft?
=> false
rails c komutunu çalıştırdıktan sonra aşağıdakileri deneyelim.
```

### Active Record Scope

```ruby
post = Post.first
post.status
=> "draft"
post.update(status: :published)
post.published?
=> true
Post.statuses
=> {"draft"=>0, "published"=>1, "inactive"=>2}
Post.statuses.keys
=> ["draft", "published", "inactive"]
Scope’lar birleştirilerek kullanılabilir.
```

### Active Record Scopes

Post.draft.or(Post.inactive) # Status durumu draft ve inactive

olan tüm postlar

Post.published.draft # Status durumu published ve draft olan tüm

postlar

```ruby
class Post < ApplicationRecord
scope :not_published, -> { where(status: [:published, :draft]) }
end
Post.draft.or(Post.inactive) # Status durumu draft ve inactive
olan tüm postlar
```

### Active Record Enum - Prefix

```ruby
class Post < ApplicationRecord
enum status: {draft: 0, published: 1, inactive: 2},
prefix: true
end
Post.status_draft # Status durumu draft olan tüm postlar
Post.status_published # Status durumu published olan tüm postlar
Post.inactive # Status durumu inactive olan tüm postlar
```

### Active Record Enum - Suffix

```ruby
class Post < ApplicationRecord
enum status: {draft: 0, published: 1, inactive: 2},
suffix: true
end
Post.draft_status # Status durumu draft olan tüm postlar
Post.published_status # Status durumu published olan tüm postlar
Post.inactive_status # Status durumu inactive olan tüm postlar
```

### Rails Router

Gelen HTTP isteklerini URL yoluna göre Rails uygulamanızdaki belirli

denetleyici (controller) eylemleriyle (actions) eşleştirir. Ayrıca URL'leri dinamik

olarak da üretebilir.

Rails.application.routes.draw do

```ruby
get "/posts", to: "posts/index"
end
routes.rb
http://example.org/posts?query=rails&sort=asc
```

### URL Parçaları

### http Protokol (Hyper-Text Transfer Protocol)

https Güvenli http, ssl (secure socket layer)

sertifikalı

example.org Host

/posts Path

?query=rails&sort=asc Parametreler

Parametre

başlangıcı

Anahtar

(Key)

Değer

(Value)

### HTTP (Hyper Text Transfer Protocol)

Bir istemci (client) ile bir web sunucusu (server) arasındaki iletişimi sağlar.

Request (İstek): Client tarafından

sunucudan belirli bir kaynağı (örneğin

bir web sayfası görüntüleme) talep

eden bir mesajdır. Bu mesaj, isteğin

türünü (GET, POST vs.) ve talep

edilen kaynağın adresini içerir.

```ruby
Processing(İşleme): Sunucu, isteği aldıktan sonra talep edilen kaynağı bulur ve veri
tabanı sorguları, dosya okuma/yazma işlemleri vb. çeşitli işlemleri gerçekleştirir.
Response(Yanıt): Sunucunun yaptığı işlemlerin sonucunu içerir.
```

### HTTP Metot ve Amaçları

GET Belirli bir kaynaktan veri istemek için kullanılır.

- GET istekleri yalnızca veri istemek için kullanır.

- Hassas istekler GET ile gönderilmemeli.

POST Yeni bir kayıt oluşturmak adına sunucuya veri

göndermek için kullanılır.

### HTTP Metot ve Amaçları

PUT Belirtilen URL’de var olan bir veriyi güncellemek için

kullanılır. Hangi kaynak güncellenecekse o kaynağın

id’sinin gönderilmesi zorunludur.

PATCH Belirtilen URL’de var olan bir veriyi güncellemek için

kullanılır.  PUT ile tüm kaynak verileri güncellenirken,

PATCH ile kaynaktaki bazı veriler güncellenir.

DELETE Belirtilen kaynağı siler.

### HTTP Metotlar ve Yollar (Routes)

### Veritabanındaki bütün postları listeler.

Id’si belirtilen post silinir.

Yeni post oluşturulur.

Id’si belirtilen post güncellenir.

Id’si belirtilen post getirilir.

/posts

/posts

/posts/post_id

/posts/post_id

/posts/post_id

/posts

Bir kaynak için ihtiyaç duyulan 4 ortak eylem; Create, Read, Update,

Delete (CRUD) için oluşturulabilecek rotalar şu şekildedir:

### Rails Routes

### Index - Bütün post kayıtlarını gösterir.

```ruby
get "/posts", to: "posts#index"
Show - Belirli bir post kaydının görüntülenmesini sağlar.
get "/posts/:id", to: "posts#show"
```

### Rails Routes

/posts/1 -> id’si 1 olan post bilgilerini gösterir.

URL’de post id’si kullanmak ne kadar doğru?

Bunun yerine /posts/post-title tarzı istenen bir kurala göre belirlenen

ifade (slug) kullanılması SEO (Arama Motoru Optimizasyonu)

anlamında da daha güzel olur.

Not: Rails’de bunun için friendly_id gem’i kullanacağız.

```ruby
get "/posts/:id", to: "posts#show"
```

### Rails Routes

New - Yeni bir post kaydı oluşturmak için form render eder.

```ruby
get "/posts/new", to: "posts#new"
Create - Hata kontrolünden sonra yeni bir post kaydı oluşturur.
post "/posts", to: "posts#create"
```

### Rails Routes

Edit - Belirli bir kaydı güncellemek için form render eder.

```ruby
get "/posts/:id/edit", to: "posts#edit"
put "/posts/:id", to: "posts/update"
Update - Hata kontrolünden sonra belirtilen post kaydının
güncellenmesini sağlar.
patch "/posts/:id", to: "posts/update"
```

### Rails Routes

Destroy - Belirtilen post kaydının silinmesini sağlar.

delete "/posts/:id", to: "posts#destroy"

### Rails Routes - Resources

Bu yolları teker teker oluşturmak yerine Rails otomatik bir şekilde

oluşturabilmeniz için bir kolaylık sağlar. config/routes.rb dosya

içerisine aşağıdaki satırı ekleyin.

resources :posts

```ruby
rails s çalıştırıp localhost:3000/routes adresine giderseniz Rails’in
sizin için otomatik olarak oluşturduğu yolları görüntüleyebilirsiniz.
Ayrıca terminalde rails routes çalıştırdığınızda uygulama yollarının
çıktısını elde edebilirsiniz.
localhost:3000/routes
```

### Arayüzden Blog Girdisi Oluşturma

Arayüz üzerinden blog girdisi oluşturabilmek için Post modeli için Views (kullanıcı

sayfaları) ve Controller oluşturulması gerekmektedir. Aşağıdaki kod

PostsController sınıfını ve içerisinde index metodunu oluşturur. Ayrıca views

altında posts dizini ve onun altında index.html.erb dosyasını oluşturur.

```ruby
rails g controller Posts index --skip-routes
```

Rails Controllers & Actions

```ruby
class PostsController < ApplicationController
def index
end
end
controllers/posts_controller.rb
<h1>Posts#index</h1>
<p>Find me in app/views/posts/index.html.erb</p>
views/posts/index.html.erb
Rails Controllers & Actions
Server’ı çalıştırıp (rails s) tarayıcıya localhost:3000/posts yazarsanız
views/posts/index.html.erb sayfa içerisindekiler görüntülenmesi gerekir.
Eğer root yolunu değiştirirseniz direk post girdilerinin olduğu sayfa açılır.
root "posts#index"
config/routes.rb
Bu değişiklikten sonra tarayıcı url kısmına sadece localhost:3000
yazmanız yeterli.
Örnek Değişkenler (Instance Variables)
```

### Veritabanındaki verileri html sayfasında gösterelim.

```ruby
class PostsController < ApplicationController
def index
@posts = Post.all
end
end
controllers/posts_controller.rb
Rails verileri views ile paylaşmak için örnek değişkenleri kullanır. Örnek
değişkenler @ ile başlar.
```

### ERB (Embedded Ruby) Nedir?

İçeriğimizin gösterileceği html dosyası views/posts/index.html.erb erb

uzantılıdır.

ERB, ruby kodunu çalıştırarak Rails ile dinamik olarak HTML

üretmemize olanak tanır.

```ruby
<%= %> etiketi, ERB'ye içerideki Ruby kodunu çalıştırmasını ve dönüş
değerini çıktı olarak vermesini söyler.
<h1>Posts</h1>
<% @posts.each do |post| %>
<%= post.title %><br/>
<%= post.article %><br/>
<%= post.status %><br/>
<% end %>
views/posts/index.html.erb
```

### Index Sayfa İçeriği

### Belirli Bir Kaydın Görüntülenmesi

```ruby
class PostsController < ApplicationController
def show
@post = Post.find(params[:id])
end
end
controllers/posts_controller.rb
params, request ile gelen tüm verilerin tutulduğu hash benzeri yapıdır.
Tarayıcıdan /posts/1 ziyaret edildiğinde params = {id: 1} değerini alır
ve Post.find(1) post girdisi @post örnek değişkenine yüklenir.
```

### Belirli Bir Kaydın Görüntülenmesi

<h1><%= @post.title %></h1>

<p><%= @post.article %></p>

<p><%= @post.status %></p>

```ruby
<%= link_to "Geri", posts_path %>
views/posts/show.html.erb
```

### Link Helpers

- posts_path generates "/posts"

- posts_url generates "http://localhost:3000/posts"

- post_path(1) generates "/posts/1"

- post_url(1) generates "http://localhost:3000/posts/1"

_url, protokol, host ve port’u kapsayacak şekilde tam bir URL oluşturur.

_path, tarayıcının anladığı mevcut domainle ilişkili bir yol oluşturur.

<h1>Posts</h1>

```ruby
<% @posts.each do |post| %>
<%= post.title %><br/>
<%= post.article %><br/>
<%= post.status %><br/>
<%= link_to "Görüntüle", post_path(post) %>
<% end %>
views/posts/index.html.erbIndex Sayfasına Link Ekleme
```

### Veritabanına Seed Verisi Eklemek

Ön tanımlı blog kayıtları oluşturabilmek için seed verisi olarak db/seed.rb

dosyasına eklenmesi gerekmektedir.

Json veya yml formatında veri dosyası hazırlayarak seed verisi oluşturulabilir.

https://gist.github.com/ecmelkytz/340c55edca9258c8eb9dbee191450183

adresindeki json formatında kaydedilen post verilerini kopyalayın ve db/data

altında posts.json adında bir dosya oluşturarak içerisine kaydedin.

```ruby
posts = YAML.load_file(Rails.root.join("db/data/posts.json"), symbolize_names:
true)
posts.each do |post|
Post.find_or_create_by(title: post[:title], article: post[:article], status:
post[:status])
end
db/seeds.rb
rails db:seed
Post.count => 6
```

### Veritabanına Seed Verisi Eklemek

### Index sayfasında sadece status durumu published postlar gösterilmesi için:

```ruby
class PostsController < ApplicationController
def index
@posts = Post.published
end
end
controllers/posts_controller.rb
```

---

## Hafta 5 — Form Helpers & Strong Parameters

### 5. Hafta Ders İçeriği

- Active View Yardımcı Metotlar (Helpers)

- Strong Parameters

- Partials

### Arayüzden Post Oluşturmak

Create işlemi için iki action’a ihtiyacımız var.

- Yeni post oluşturmak için post formunu render eden new action

- Post’u kaydetmek için create action

```ruby
class PostsController < ApplicationController
def new
@post = Post.new
end
end
controllers/posts_controller.rb
Ardından views/posts/ new.html.erb dosyasını oluşturun.
```

### Action View

- MVC’de View’e karşılık gelir.

- Web isteklerini karşılamak için Action Controller ile birlikte

çalışırlar.

- Action Controller, model katmanıyla iletişim kurmak ve veri

almakla ilgilenir.

- Action View bu verileri kullanarak web isteğine bir yanıt gövdesi

oluşturmaktan sorumludur.

- Action View, formlar, tarihler ve stringler için HTML etiketlerini

dinamik olarak oluşturan bir çok yardımcı metot (helper) sağlar.

### Action View Form Helpers

Ana form yardımcı metodu form_with’dir.

```ruby
<%= form_with do |form| %>
Form contents
<% end %>
<form action="/posts/new" accept-charset="UTF-8" method="post">
<input type="hidden" name="authenticity_token"
value="Lz6ILqUEs2CGdDa-oz38TqcqQORavGnbGkG0CQA8zc8peOps-
K7sHgFSTPSkBx89pQxh3p5zPIkjoOTiA_UWbQ" autocomplete="off">
Form contents
</form>
views/posts/new.html.erb
```

### Action View Form Helpers

<form action="/posts/new" accept-charset="UTF-8" method="post">

<input type="hidden" name="authenticity_token"

value="Lz6ILqUEs2CGdDa-oz38TqcqQORavGnbGkG0CQA8zc8peOps-

K7sHgFSTPSkBx89pQxh3p5zPIkjoOTiA_UWbQ" autocomplete="off">

</form>

Parametre belirtilmediği zaman method post ve action niteliğinin

değeri geçerli sayfa olarak ayarlanır.

Formda authenticity_token oluşturulur ve bu hidden field olarak tutulur.

Kullanıcı formu gönderdiğinde, Rails authenticity_token'a bakar, oturumda

depolananla karşılaştırır ve eğer eşleşirse isteğin devam etmesine izin

verir. Dışarıdan gelen sahte istekleri engeller.

Model Nesneleriyle Form Oluşturma

form_with model nesnelerini forma bağlamak için :model parametresine

sahiptir.

Form elemanlarının ilk parametresi her zaman input’un adıdır. Form submit

edildiğinde bu input’lar controller’da params değişkeninde kullanılacaklar.

```ruby
<%= form_with model: @post do |form| %>
<%= form.label :title, "Başlık" %>
<%= form.text_field :title %>
<% end %>
views/posts/new.html.erb
Bu input değerine controller içinde params[:title] şeklinde ulaşılabilir.
Form Elemanları İçin Yardımcı Metotlar (Bunları Eklemeyin!)
<%= form_with do |form| %>
<%= form.text_field :title %><br/>
<%= form.text_area :article, size: "70x5" %><br/>
<%= form.hidden_field :user_id, value: "123456" %>
<% end %>
<input type="text" name:"title" id="title" ></input>
<textarea name="article" id="article" cols="70" rows="5"></textarea>
<input value="foo" autocomplete="off" type="hidden" name="user_id"
id="user_id">
Html Çıktıları:
Form Elemanları İçin Yardımcı Metotlar (Bunları Eklemeyin!)
<%= form_with do |form| %>
<%= form.number_field :price, min:0, max:20, step: 2 %><br/>
<%= form.range_field :discount, in: 1..100 %><br/>
<%= form.password_field :password %>
<% end %>
<input type="number" name="price" id="price" min="0" max="20" step="2">
<input type="range" name="discount" id="discount" min="1" max="100">
<input type="password" name="password" id="password">
Html Çıktıları:
Form Elemanları İçin Yardımcı Metotlar (Bunları Eklemeyin!)
<%= form_with do |form| %>
<%= form.date_field :birth %><br/>
<%= form.time_field :started_at %><br/>
<%= form.month_field :birthday_month %>
<% end %>
<input type="date" name="birth" id="birth">
<input type="time" name="started_at" id="started_at">
<input type="month" name="birthday_month" id="birthday_month">
Html Çıktıları:
select
<%= form_with model: @post do |form| %>
<%= form.select(:status, Post.statuses.keys) %>
<% end %>
Seçilebilecek her seçenek için option oluştururlar.
```

Radio Buttons: collection_radio_buttons

```ruby
<%= form_with model: @post do |form| %>
<%= form.collection_radio_buttons :status, Post.statuses, :first, :first %>
<% end %>
⃝ draft          ⃝ published        ⃝ inactive
Kullanıcı seçenekler yalnızca birini seçebilir.
collection_radio_buttons(method, collection, value_method, text_method)
Post.statuses -> { "draft" => 0, "published" => 1, inactive: 2 }
form’da gönderilen değer
kullanıcıya görünen yazı
Model Nesneleriyle Form Oluşturma (Bu kodları ekleyin)
new.html.erb içeriği aşağıdaki gibi oluşturulabilir.
<%= form_with model: @post do |form| %>
<%= form.label :title, "Post Başlığı" %>
<%= form.text_field :title %><br/>
<%= form.label :article, "Post Metni" %>
<%= form.text_area :article %><br/>
<%= form.label :status, "Post Durumu" %>
<%= form.select(:status, Post.statuses.keys) %><br/>
<%= form.submit %>
<% end %>
app/views/posts/new.html.erb
Model Nesneleriyle Form Oluşturma
Browser’dan html çıktılarını inceleyelim.
```

```ruby
class PostsController < ApplicationController
def create
@post = Post.new(post_params)
if @post.save
redirect_to posts_path
else
render :new
end
end
private
def post_params
params.require(:post).permit(:title, :article, :status)
end
end
controllers/posts_controller.rbArayüzden Post Oluşturmak
```

### Strong Parameter Nedir?

Create eylemi, form tarafından gönderilen verileri işler, ancak güvenlik için

filtrelenmesi gerekir. post_params burada devreye giriyor.

Rails’e, :title, :article ve :status parametre dizisine sahip :post adlı bir

anahtar olduğundan emin olmasını söyleriz.

Rails bunlar haricindeki tüm parametreleri yok sayar.

```ruby
def post_params
params.require(:post).permit(:title, :article, :status)
end
```

### Index Sayfasına Yeni Post Ekleme Linki Ekle

<h1>Posts</h1>

```ruby
<%= link_to "Yeni Post Oluştur", new_post_path %>
<% @posts.each do |post| %>
<%= post.title %><br/>
<%= post.article %><br/>
<%= post.status %><br/>
<%= link_to "Görüntüle", post_path(post) %>
<% end %>
views/posts/index.html.erb
```

link_to  Kullanımı

link_to, Action View’in sağladığı bir helper. Parametre olarak verilen model

nesneleri için link oluşturur.

@post = Post.find(1)

link_to "Post", @post

```ruby
# <a href="/posts/1">Post</a>
link_to "Posts", posts_path
# <a href="/posts">Posts</a>
link_to(name = nil, options = nil, html_options = nil, &block)
Post
Posts
link_to Kullanımı
link_to nil, "https://google.com"
# <a href="https://google.com">https://google.com</a>
link_to "Posts", posts_path, id: "posts", class: "btn btn-
primary"
# <a href="/posts" id="posts" class="btn btn-primary">Posts</a>
https://google.com
```

link_to Kullanımı

```ruby
<%= link_to(@post) do %>
<strong><%= @post.title %></strong> - Görüntüle
<% end %>
# <a href="/posts/1">
<strong>Post 1 Başlık</strong> - Görüntüle
</a>
Post 1 Başlık - Görüntüle
```

### Arayüzden Post Güncellemek

Güncelleme işlemi oluşturma işlemine benzer şekilde iki eylemi içerir.

Bunlar edit ve update eylemleridir.

```ruby
def edit
@post = Post.find(params[:id])
end
def update
@post = Post.find(params[:id])
if @post.update(post_params)
redirect_to @post
else
render :edit
end
end
controllers/posts_controller.rb
Edit Sayfası Ekle
views/posts/edit.html.erb
new.html.erb sayfa içeriği ile ne farkı var?
<%= form_with model: @post do |form| %>
<%= form.label :title, "Post Başlığı" %>
<%= form.text_field :title %><br/>
<%= form.label :article, "Post Metni" %>
<%= form.text_area :article %><br/>
<%= form.label :status, "Post Durumu" %>
<%= form.select(:status, Post.statuses.keys) %><br/>
<%= form.submit %>
<% end %>
Show ve Index Sayfalarına Güncelleme Linki Ekle
<%= link_to "Post Güncelle", edit_post_path(@post) %>
views/posts/show.html.erb
<% @posts.each do |post| %>
<%= post.title %><br/>
<%= post.article %><br/>
<%= post.status %><br/>
<%= link_to "Görüntüle", post_path(post) %> |
<%= link_to "Güncelle", edit_post_path(post) %>
<% end %>
views/posts/index.html.erb
```

### Partials

new ve edit sayfa içerikleri aynı. Bu durumu, bir görünümü birden fazla

yerde yeniden kullanmanıza olanak veren partials özelliği ile ortadan

kaldırabiliriz.

Formu app/views/posts/_form.html.erb adlı bir dosyaya taşıyabiliriz.

Ardından bu form new ve edit sayfalarında render edilir.

Dikkat: Partials olarak oluşturulan dosya adının önünde _ olmalıdır.

views/posts/new.html.erb

```ruby
<%= render "form", post: @post, form_title: "Yeni Post Ekle" %>
<%= link_to "Geri", posts_path %>
```

### Partials

views/posts/edit.html.erb

```ruby
<%= render "form", post: @post, form_title: "Postu Güncelle" %>
<%= link_to "Geri", post_path(@post) %>
_form.html.erb Son Hali
<h1><%= form_title %></h1>
<%= form_with model: post do |form| %>
<%= form.label :title, "Post Başlığı" %>
<%= form.text_field :title %><br/>
<%= form.label :article, "Post Metni" %>
<%= form.text_area :article %><br/>
<%= form.label :status, "Post Durumu" %>
<%= form.select(:status, Post.statuses.keys) %><br/>
<%= form.submit %>
<% end %>
views/posts/_form.html.erb
```

### Before Action Callback

show, edit ve update action’larında @post = Post.find(params[:id]) satırı tekrar

edilmektedir. Bu durum DRY’ye uygun olmadığı için action’lar tetiklenmeden

önce bir fonksiyon içerisinde bu değişken ataması yapılabilir.

```ruby
class PostsController < ApplicationController
before_action :set_post, only: %i[show edit update]
private
def set_post
@post = Post.find(params[:id])
end
end
```

### Before Action Callback

Güncelleme sonrası show, edit ve update içerikleri:

```ruby
def show; end
def edit; end
def update
if @post.update(post_params)
redirect_to @post
else
render :edit
end
end
```

### button_to Kullanımı

```ruby
<%= button_to "Sil", @post, method: :delete %>
● Kendi başına mini bir form oluşturur
● Genelde tek işlem için kullanılır (delete gibi)
● Link gibi görünen buton üretir
<form class="button_to" method="post" action="/posts/1">
<input type="hidden" name="_method" value="delete"
autocomplete="off">
<input type="hidden" name="authenticity_token"
value="RANDOM_TOKEN_HERE" autocomplete="off">
<button type="submit">Sil</button>
</form>
```

### Arayüzden Post Kaydını Silmek

Silme işlemi için destroy action controller’a eklenmesi gerekir.

before_action :set_post, only: %i[show edit update destroy]

```ruby
def destroy
@post.destroy
redirect_to posts_path
end
controllers/posts_controller.rb
<%= button_to "Sil", @post, method: :delete, data: {
turbo_confirm: "Emin misin?" } %>
views/posts/show.html.erb
Show ve Index'e Silme Butonlarını Ekleyin
<%= button_to "Sil", @post, method: :delete, data: {
turbo_confirm: "Emin misin?" } %>
views/posts/show.html.erb
<% @posts.each do |post| %>
<%= post.title %><br/>
<%= post.article %><br/>
<%= post.status %><br/>
<%= link_to "Görüntüle", post_path(post) %> |
<%= link_to "Güncelle", edit_post_path(post) %> |
<%= button_to "Sil", post, method: :delete, data: { turbo_confirm: "Emin misin?" } %>
<% end %>
views/posts/index.html.erb
```

### MVC İçeriklerinin Son Hali

Post için model, views ve controller içeriklerine aşağıdaki linkten

ulaşabilirsiniz.

https://gist.github.com/ecmelkytz/600437c7c8fa4d7d731639a862224796

### Kaynaklar

https://guides.rubyonrails.org/form_helpers.html

---

## Hafta 6 — Bootstrap Frontend

### 6. Hafta Ders İçeriği

- Bootstrap ile Frontend düzenleme

### Bootstrap

Hızlı ve kolay bir şekilde web uygulaması geliştirebilmek için kullanılan ücretsiz

bir frontend çerçevesidir. Formlar, butonlar, tablolar, navigation, modals gibi html

ve css templateleri mevcuttur ve isteğe bağlı bazı JS eklentileri de mevcuttur.

### Bootstrap 5 mobil cihazlara duyarlı olacak şekilde tasarlanmıştır.

<meta name="viewport" content="width=device-width, initial-scale=1">

Viewport: Kullanıcıların bir web sayfasında görüntüleyebildiği alanların tamamına

denir.

width=device-width: Viewport genişliğini cihazın ekran genişliğine ayarlar ve

doğru ölçeklendirmeyi sağlar.

initial-scale=1: Zoom seviyesini 1’e (%100) ayarlar ve gereksiz zoomlamayı

önler.

### Bootstrap Breakpoints (Kırılma Noktaları)

Responsive tasarımın çeşitli cihazlarda ve görüntüleme alanı boyutlarında

(viewport) nasıl görüntülendiğini belirlememize yardımcı olur. Ekran genişliğine

göre tasarımın değiştiği noktalardır.

Breakpoint Class Infix Boyut

Extra small None <576px             <

6 Inch

Small sm ≥576px           >=

6 Inch

Medium md ≥768px           >=

8 Inch

Large lg ≥992px      >=

10,3 Inch

Extra large xl ≥1200px    >=

12,5 Inch

Extra extra large xxl ≥1400px    >=

14,5 Inch

### Bootstrap Container

Container, sayfadaki içeriği ortalayan ve genişliğini kontrol eden ana kapsayıcıdır.

.container (Her breakpoint’de max-width değişir)

.container-{breakpoint} (belirtilen breakpoint’e kadar width: 100%).

.container-fluid (width: Bütün breakpoint’lerde %100).

Extra small

<576px

Small

≥576px

Medium

≥768px

Large

≥992px

X-Large

≥1200px

XX-Large

≥1400px

.container 100% 540px 720px 960px 1140px 1320px

.container-md 100% 100% 720px 960px 1140px 1320px

.container-fluid 100% 100% 100% 100% 100% 100%

- https://getbootstrap.com/docs/5.3/layout/containers/

- https://getbootstrap.com/docs/5.3/examples/grid/#containers

### Bootstrap Grid

Grid sistem, içeriği hizalamak için bir dizi container, satır (row) ve sütun (col)

kullanır.

<div class="container">

<div class="row">

<div class="col">

First column

</div>

<div class="col">

Second column

</div>

</div>

</div>

### Bootstrap Grid

Her satırda 12 sütun eklenebilir. 12

sütun uzunluğunu aşmayacak

şekilde farklı uzunluklarda sütun

yan yana eklenebilir. Örneğin col-4

ile yan yana 3 sütun eklenebilir.

<div class="container text-center">

<div class="row">

<div class="col">col</div>

<div class="col">col</div>

<div class="col">col</div>

<div class="col">col</div>

</div>

<div class="row">

<div class="col-8">col-8</div>

<div class="col-4">col-4</div>

</div>

</div>

### Bootstrap Grid

Mobil telefonlarda veya 768px’den

daha dar ekranlarda sütunlar

otomatik olarak üst üste yığılır.

Extra small

<576px

Small

≥576px

Medium

≥768px

Large

≥992px

X-Large

≥1200px

XX-Large

≥1400px

Container

max-width

None

(auto)

540px 720px 960px 1140px 1320px

Class preﬁx .col- .col-sm- .col-md- .col-lg- .col-xl- .col-xxl-

col-md-3 col-md-3 col-md-3 col-md-3

<div class="row">

<div class="col-md-3">.col-sm-3</div>

<div class="col-md-3">.col-sm-3</div>

<div class="col-md-3">.col-sm-3</div>

<div class="col-md-3">.col-sm-3</div>

</div>

### Bootstrap İnceleyin

- https://getbootstrap.com/docs/5.3/getting-started/introduction/

### Bootstrap JS

### Bootstrap JS işlemleri düzgün çalışması için popper.js kütüphanesi

eklenmesi gerekiyor.

pin "@popperjs/core", to:

"https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/po

pper.min.js"

conﬁg/importmap.rb

import "@popperjs/core"

javascript/application.js

Ardından rails assets:precompile çalıştırın.

### Bootstrap ile Navbar Ekleyelim

app/views dizini altında shared adında bir klasör oluşturalım ve içinde

_navbar.html.erb adında partial dosyası oluşturalım.

https://getbootstrap.com/docs/5.3/components/navbar/ adresinden veya

https://getbootstrap.com/docs/5.3/examples/navbars/ istediğiniz navbarı seçin

kodlarını _navbar.html.erb dosyasına kaydedin.

views/layouts/application.html.erb dosyası içerisine render edelim.

<body>

```ruby
<%= render "shared/navbar" %>
<div class="container">
<%= yield %>
</div>
</body>
```

### Navbar’daki Blogger yazısına (başka bir isim de verebilirsiniz) basınca

anasayfaya giden bir link ekleyin.

```ruby
<%= link_to "Blogger", root_path, class:"navbar-brand" %>
```

### Navbar’da görünmesini istediğiniz başka alanlar varsa link olarak

ekleyebilirsiniz. Ör: Hakkımda, Projelerim vs.

### Hakkımda

### Bootstrap ile Footer Ekleyelim

### Footer için views/shared klasörü altında _footer.html.erb adında partial

dosyası oluşturalım.

https://getbootstrap.com/docs/5.3/examples/footers/ adresinden

istediğiniz footer’ı seçin ve kodlarını _footer.html.erb dosyasına kaydedin.

views/layouts/application.html.erb dosyası içerisine render edelim.

<body class="d-flex flex-column min-vh-100">

```ruby
<%= render "shared/navbar" %>
<div class="container">
<%= yield %>
</div>
<%= render "shared/footer" %>
</body>
```

### Index Sayfasını Güncelleyelim

<div class="row">

```ruby
<% @posts.each do |post| %>
<div class="col-md-8 mx-auto mt-4">
<div class="card">
<div class="card-header"><%= link_to post.title, post_path(post)
%></div>
<div class="card-body"><%= post.article %></div>
<div class="card-footer">
<%= link_to "Güncelle", edit_post_path(post), class:"btn
btn-outline-warning btn-sm" %>
</div>
</div>
</div>
<% end %>
app/views/posts/index.html.erb
Sayfalarınızı istediğiniz şekilde tasarlayabilirsiniz.
Bu kod bir örnektir.
```

### Index Sayfasını Güncelleyelim

### Show Sayfasını Güncelleyelim

### Form Sayfasını Güncelleyelim

https://getbootstrap.com/docs/5.3/forms/overview/

### Hakkımda Sayfası

### Hakkımda sayfası için path, view ve controller’da ilgili action’ı oluşturun.

```ruby
get "about", to: "home#about"
conﬁg/routes.rb
class HomeController < ApplicationController
def about; end
end
app/controllers/home_controller.rb
views/home/about.html.erb dosyasını oluşturun ve içerisini bootstrap
sınıflarını ve html etiketlerini kullanarak kendinizle alakalı bilgileri ekleyin.
Uygulamanın Diğer Sayfalarını Oluşturalım
● Sayfada profil resmi bulunsun ve iletişim için sosyal medya adres iconları
linklensin.
● Footer ve Navbar’a linkleyin, linke basınca ilgili sayfa açılsın.
Gizem Bulut
```

### Hakkımda

### image_tag Kullanımı

```ruby
image_tag("profile.png")
# <img src="/assets/profile.png" />
```

### image_tag HTML resim etiketi oluşturur. Resimler app/assets/images altına

yerleştirilir. Yeni eklenen resimlerin gözükmesi için rails assets:precompile çalıştırılır.

```ruby
image_tag(source, options = {})
image_tag("profile.png", size: "150x150", alt: "Profile Image")
# <img src="/assets/profile.png" width="150" height="150" alt="Profile
Image />
image_tag("/icons/icon.gif", class: "menu_icon")
# <img src="/icons/icon.gif" class="menu_icon" />
```

### Hakkımda Sayfası

Sayfada resim gösterebilmek için app/assets/images altına resmi ekleyin.

Ardından rails assets:precompile kodunu çalıştırın ve sayfa içerisinde

### image_tag metodu ile kullanın.

```ruby
<%= image_tag("profile.jpg", width:"200x200") %>
Iconlar için https://icons.getbootstrap.com/ adresine bakabilirsiniz.
Icon’a link vermek için:
<%= link_to "https://github.com/yourusername" do %>
<i class="bi bi-github link-dark"></i>
<% end %>
```

### Projelerim Sayfası

### Projelerim sayfası için path, view ve controller’da ilgili action’ı oluşturun.

```ruby
get "projects", to: "home#projects"
conﬁg/routes.rb
class HomeController < ApplicationController
def projects; end
end
app/controllers/home_controller.rb
views/home/projects.html.erb dosyasını oluşturun ve içerisini bootstrap
sınıflarını ve html etiketlerini kullanarak kendinizle alakalı bilgileri ekleyin.
```

### Projelerim Sayfası

### Footer veya Navbar’a linkleyin. Linke basınca ilgili sayfa açılsın.

https://getbootstrap.com/docs/5.3/components/list-group/

### Not

Slayt içerisinde verilen tasarımlar örnektir. Aynı sayfalar olmak kaydıyla, Bootstrap

kütüphanesini kullanarak istediğiniz sayfa tasarımlarını yapabilirsiniz.

---

## Hafta 7 — Model İlişkileri & Kategori

### 7. Hafta Ders İçeriği

- Rails model ilişkileri

- Blog uygulamasına kategori tablosu ekleme ve bağlantı sağlama

### Rails Model İlişkileri

Rails’de 6 çeşit model ilişkisi mevcuttur.

- belongs_to

- has_one

- has_many

- has_many :through

- has_one :through

- has_and_belongs_to_many

### Rails Model İlişkileri - belongs_to

```ruby
class Book < ApplicationRecord
belongs_to :author
end
```

### Rails Model İlişkileri - has_many

```ruby
class Author < ApplicationRecord
has_many :books, dependent: :destroy
end
```

### Rails Model İlişkileri - has_many ve belongs_to

```ruby
class CreateAuthors < ActiveRecord::Migration[8.0]
def change
create_table :authors do |t|
t.string :name
t.timestamps
end
end
end
class CreateBooks < ActiveRecord::Migration[8.0]
def change
create_table :books do |t|
t.belongs_to :author
t.datetime :published_at
t.timestamps
end
end
end
rails g model Author name
rails g model Book author:references published_at:datetime
Aşağıdaki komutlar ile migrationlar oluşur
```

### Rails Model İlişkileri - has_many :through

### Rails Model İlişkileri - has_many :through

```ruby
class Physician < ApplicationRecord
has_many :appointments, dependent: :destroy
has_many :patients, through: :appointments
end
class Patient < ApplicationRecord
has_many :appointments, dependent: :destroy
has_many :physicians, through: :appointments
end
class Appointment < ApplicationRecord
belongs_to :physician
belongs_to :patient
end
```

has_many :through migration dosya örneği

```ruby
class CreatePhysicians < ActiveRecord::Migration[8.0]
def change
create_table :physicians do |t|
t.string :name
end
end
class CreatePatients < ActiveRecord::Migration[8.0]
create_table :patients do |t|
t.string :name
end
end
class CreateAppointments < ActiveRecord::Migration[8.0]
create_table :appointments do |t|
t.belongs_to :physician
t.belongs_to :patient
t.datetime :appointment_date
end
end
rails g model Physician name
rails g model Patient name
rails g model Appointmet physician:references
patient:references appontment_date:datetime
```

### Rails Model İlişkileri - has_one

```ruby
class User < ApplicationRecord
has_one :proﬁle
end
profiles
Model: Profile
belongs_to :user
id integer
user_id integer
bio text
users
Model: User
has_one :profile
id integer
full_name string
```

### Rails Model İlişkileri - has_one ve belongs_to

```ruby
class CreateUsers < ActiveRecord::Migration[8.0]
def change
create_table :users do |t|
t.string :full_name
t.timestamps
end
end
end
class CreateProfiles < ActiveRecord::Migration[8.0]
def change
create_table :profiles do |t|
t.belongs_to :user
t.text :bio
t.timestamps
end
end
end
rails g model User full_name:string
rails g model Proﬁle user:references bio:text
Aşağıdaki komutlar ile migration oluşur
profiles
Model: Profile
belongs_to :user
id integer
user_id integer
bio text
users
Model: User
has_one :profile
id integer
full_name string
```

### Rails Model İlişkileri - has_one :through

profiles

Model: Profile

belongs_to :user

has_one :account

id integer

user_id integer

bio string

users

Model: User

has_one :profile

has_one :account, through: :profile

id integer

full_name string

accounts

Model: Account

belongs_to :profile

id integer

profile_id integer

account_no string

### Rails Model İlişkileri - has_one :through

```ruby
class User < ApplicationRecord
has_one :proﬁle
has_one :account, through:  :proﬁle
end
class Proﬁle < ApplicationRecord
belongs_to :user
has_one :account
end
class Account < ApplicationRecord
belongs_to :proﬁle
end
```

### Rails Model İlişkileri - has_one :through

```ruby
class CreateUser < ActiveRecord::Migration[8.0]
def change
create_table :users do |t|
t.string :full_name
end
end
class CreateProﬁle < ActiveRecord::Migration[8.0]
create_table :proﬁles do |t|
t.belongs_to :user
t.text :bio
end
end
class CreateAccounts < ActiveRecord::Migration[8.0]
create_table :accounts do |t|
t.belongs_to :proﬁle
t.string :account_no
end
end
rails g model User full_name
rails g model Proﬁle user:references bio:text
rails g model Account proﬁle:references account_no
has_and_belongs_to_many  -  HABTM
users
id integer
first_name string
id_number string
roles
id integer
name string
usersroles
user_id integer
role_id integer
```

### Rails Model İlişkileri - has_and_belongs_to_many

```ruby
class User < ApplicationRecord
has_and_belongs_to_many :roles
end
class Role < ApplicationRecord
has_and_belongs_to_many :users
end
```

### Rails Model İlişkileri - has_and_belongs_to_many

```ruby
class CreateUsersAndRoles < ActiveRecord::Migration[8.0]
def change
create_table :users do |t|
t.string :ﬁrst_name
t.string :id_number
end
create_table :roles do |t|
t.string :name
end
create_table :users_roles, id: false do |t|
t.belongs_to :role
t.belongs_to :user
end
end
end
Projeye Y eni Tablo Ekleme
rails g scaffold Category name code
scaﬀold ile controller, model,
views, yollar (routes) ve diğer
sayfalar (test, helper vs.)
otomatik olarak oluşturulur.
Ardından rails db:migrate
çalıştırın
```

### Tablolar Arası Bağlantı Sağlayalım

```ruby
rails g migration CreateJoinTablePostsCategories posts
categories
posts
has_and_belongs_to_many
:categories
id integer
title string
article text
status integer
categories
has_and_belongs_to_many :posts
id integer
name string
code string
categories_posts
category_id integer
post_id integer
```

### Tablolar Arası Bağlantı Sağlayalım

```ruby
class CreateJoinTablePostsCategories <
```

### ActiveRecord::Migration[8.0]

```ruby
def change
create_join_table :posts, :categories do |t|
t.index [:post_id, :category_id]
t.index [:category_id, :post_id]
end
end
end
db/migrate/create_join_table_posts_categories
```

### Tablolar Arası Bağlantı Sağlayalım

```ruby
class Category < ApplicationRecord
has_and_belongs_to_many :posts
end
app/models/category.rb
app/models/post.rb
class Post < ApplicationRecord
has_and_belongs_to_many :categories
end
Konsol İşlemleri
Category.create(name: "Java Programming", code:"java")
Category.create(name: "Python Programming", code:"python")
Post.create(title:"Java’ya Giriş", article: "Java programlama …")
Post.last.categories << Category.ﬁnd_by(name: "Java Programming")
Post.last.categories << Category.last
Post.last.categories
Konsol İşlemleri
Post.last.categories.count   # Son postun kategori sayısı
Category.last.posts  # Son kategoriye ait tüm postlar
Category.ﬁrst.posts  # İlk kategoriye ait tüm postlar
Category.last.posts <<  Post.ﬁrst   # Son kategoriye ilk postu dahil et
<%= form_with model: post do |form| %>
<%= form.label :category, class:"form-label" %>
<%= form.select :category_ids,
Category.all.collect { |c| [c.name, c.id] },
{},
{ class:"form-select", multiple: true } %>
<% end %>
app/views/posts/_form.html.erb
```

### Form Sayfasına Kategori Select Box Ekleme

### Post Girdisinin Kategorisini Belirleme

Form üzerinden formun kategorilerini seçip kaydetmeye çalışın, post’un

### kategorileri seçilebildi mi? (Strong Parameter 🌟

)

```ruby
def post_params
params.require(:post).permit(:title, :article, :status,
category_ids: [])
end
controllers/posts_controller.rb
def post_params
params.require(:post).permit(:title, :article, :status,
category_ids: [])
end
controllers/posts_controller.rb
```

### Controller Güncelleme

Hata ayıklamak için ilgili action içine binding.irb yazabilirsiniz

### Post Show Sayfasına Kategoriler İçin Badge Ekleme

### Kategori Sayfaları

Oluşturulan kategori sayfalarını bootstrap bileşenleri ile düzenleyiniz.

Örnek kodlar için bakınız:

https://gist.github.com/ecmelkytz/cb3764fc07c13ed8f465e5059486dd06

### Kategoriler Sayfasında İlgili Postları Listelemek

### Kategori görüntüleme sayfası örnek url: localhost:3000/categories/1

Coding kategorisine ait tüm postlar

### Navbar’a İşlemler için dropdown menü ekleyelim. Yeni post ve kategori ekleme linkleri

burada olsun.

<ul class="dropdown-menu">

<li>

```ruby
<%= link_to "Yeni Post Oluştur", new_post_path, class: "dropdown-item" %>
</li>
<li>
<%= link_to "Yeni Kategori Oluştur", new_category_path, class: "dropdown-item" %>
</li>
<li><hr class="dropdown-divider"></li>
<li><a class="dropdown-item" href="#">Çıkış</a></li>
</ul>
```

### Footer’a Kategoriler linki ekleyin.

```ruby
<%= link_to "Kategoriler", categories_path, class: "nav-link px-2
text-body-secondary" %>
Sizin kullandığınız footer nav link sınıfı farklı
olabilir.
```

---

## Hafta 8 — Validation & Active Storage

### 8. Hafta Ders İçeriği

- Rails validations (doğrulama) ve normalization (normalleştirme)

- Active Storage

- Blog postuna resim yüklemek için yeni kolon ekleme

### Rails Validation

### Active Record validasyonları veritabanına eklenecek verilerin belirli kurallara

uymasını sağlamanıza olanak sağlar. Örneğin, modeldeki bir değerin boş (nil)

olduğu, benzersiz (unique) olduğu, veritabanında zaten bulunmadığı, belirli bir

formatta (regex) olduğu ve daha fazlası doğrulanabilir.

Validation Seviyeleri

- Veritabanı kısıtları

- Client-side

- Controller level (keep skinny)

- Model level

### Rails Validation

### Tetikleyici (Trigger) Validasyonlar

- create

- create!

- save

- save!

- update

- update!

Aşağıdaki metotlar validasyonları tetikler ve sadece doğrulama yapılırsa

### veritabanına eklenir.

Veri doğrulanamadıysa metot sonlarındaki ! işareti bir

istisna mesaj (exception) verilmesini sağlar. !

olmayanlarda save ve update false döner, create’de

ise  nesnenin kendisi döndürülür.

```ruby
save(validate: false) ile doğrulama yapılmadan veri
```

### veritabanına kaydedilebilir.

### Validasyonları Atlayan Metotlar

- decrement!

- increment!

- toggle!

- touch

- update_all

- update_attribute

Aşağıdaki yöntemler validasyonları atlar ve nesneyi geçerliliğinden bağımsız

olarak veritabanına kaydeder. Dikkatli kullanılmalılar.

Sayısal bir niteliği 1 (varsayılan) veya belirtilen miktarda azaltır.

Sayısal bir niteliği 1 (varsayılan) veya belirtilen miktarda artırır.

Bir boolean niteliğini true ve false arasında değiştirir.

Bir kaydın özniteliklerini değiştirmeden zaman damgasını

(updated_at) günceller.

update_all metodu toplu (bulk) güncellemeler için kullanılır.

User.where(active:true).update_all(last_login_at:Time.current)

update_attribute metodu mevcut bir kaydın tek bir niteliği güncellenir.

user.update_attribute(email: "new@example.com")

### Rails Normalization

Validasyonlardaki gibi verileri reddetmek yerine belirtilen biçimde değiştirir.

Validasyonlardan (before_validation) önce çalıştırılırlar.

Validation

Veriyi kontrol eder

Doğrulama başarısız olabilir

Doğrulama her save işleminde

yapılır

Normalization

Veriyi değiştirir

Her zaman işletilir

Doğrulamadan önce çalışır

### Rails Normalization

```ruby
class Post < ApplicationRecord
normalizes :title, with: -> title { title.squish.titlecase }
end
```

### Post modelinin title alanı için oluşturulan normalizasyon ile title bilgi

### veritabanına kaydedilmeden önce string’in başında, sonunda veya ortasında

fazla boşluk varsa siler (squish) ve her kelimenin ilk harfini büyük harfe

çevirir (titlecase) ondan sonra veritabanına kaydedilir.

### Validation Helpers

- presence

- uniqueness

- inclusion

- exclusion

- length

- numericality

- format

### Validation Helpers - presence

Değerin boş olmadığını doğrular.

```ruby
class Post < ApplicationRecord
validates :title, presence: true
validates :article, presence: true
end
Post.new(title: "a", article: "b").valid?
=> true
Post.create(title: "", article: "b").valid?
=> false
Post.create!(title: "", article: "b").valid?
=> Validation failed: Title can't be blank
```

### Validation Helpers - uniqueness

Nesne kaydedilmeden hemen önce değerin benzersiz olduğunu

doğrular.

```ruby
class Post < ApplicationRecord
validates :title, presence: true, uniqueness: true
validates :article, presence: true
end
Post.create(title: "a", article: "b").valid?
=> true
Post.create!(title: "a", article: "b")
=> Validation failed: Title has already been taken
```

### Validation Helpers - uniqueness

Başka bir örnek:

```ruby
class Account < ApplicationRecord
validates :email, uniqueness: true
validates :account_name, uniqueness: { case_sensitive: true }
end
email ve account_name alanının tekil ve ayrıca account_name alanının
büyük küçük harfe duyarlı olması gerektiği belirtilir.
```

### Validation Helpers - inclusion

Değerin verilen bir kümeye dahil edildiğini doğrular.

```ruby
class Post < ApplicationRecord
validates :status, inclusion: { in: statuses.keys }
end
Status alanı için Post modelde enum olarak belirtilen draft, published
ve inactive türlerinden başka değer seçilmemesini garanti eder.
```

### Validation Helpers - exclusion

inclusion’ın tam tersidir. Değerin verilen bir kümeye dahil olmadığını

doğrular.

```ruby
class Account < ApplicationRecord
validates :subdomain, exclusion: { in: %w(www us ca),
message: "%{value} is reserved." }
end
Account modelindeki subdomain alanı için www, us ve ca
değerlerinden başka herhangi bir değer girilebilmesini garanti eder.
```

### Validation Helpers - length

Değerlerin, uzunluğu belirtilen kısıtlara göre olmasını garanti eder.

```ruby
class Post < ApplicationRecord
validates :title, presence: true, uniqueness: true, length: {
maximum: 255 }
validates :article, presence: true, length: {maximum: 65_535}
end
```

### Post modelindeki title alanı hem benzersiz, hem boş geçilemez hem de

uzunluğu max. 255 karakterden oluşmak zorundadır.

Article alanı ise boş geçilemez ve uzunluğu max. 65_535 karakterden

oluşmak zorundadır.

### Validation Helpers - length

Başka bir örnek:

```ruby
class User < ApplicationRecord
validates :bio, length: { maximum: 500 }
validates :password, length: { in: 6..20 }
validates :id_number, length: { is: 11 }
end
User modeli için bio alanı maksimum 500 karakter uzunluğunda,
password alanı 6 ile 20 karakter uzunluğunda, id_number ise sadece
11 karakter uzunluğunda olabileceğini belirtir.
```

### Validation Helpers - numericality

Değerlerin yalnızca sayısal değerlere sahip olduğunu doğrular. Default

olarak integer ya da float kabul eder.

```ruby
class Book < ApplicationRecord
validates :year, numericality: { only_integer: true,
greater_than_or_equal_to: 1950, less_than_or_equal_to: 2025 }
validates :number_of_pages, numericality: { only_integer:
true, greater_than: 0 }
end
Book modeli için year alanı 1950 - 2025 arasında sayısal bir değer
olmalı. number_of_pages alanı 0’dan büyük bir sayısal değer olmalı.
```

### Validation Helpers - format

Belirtilen belirli bir düzenli ifadeyle eşleşip eşleşmediğini doğrular.

```ruby
class Contact < ApplicationRecord
validates :phone_number, format: { with: /\A\d+\z/,
message: "only allows numbers" }
end
Contact modelindeki phone_number alanı için sadece belirtilen
formatta bir değer girilebilir.
\A ve \z  düzenli ifadenin tüm dizeyle eşleştiğinden emin olmak için
kullanılır.
\d+ bir veya daha fazla sayısal karakteri ifade etmektedir.
```

### Validation Options

allow_nil: nil  # Değer nil geçilebilir.

allow_blank: nil & whitespace # Değer nil veya boş geçilebilir.

message: # Default error mesajları değiştirilebilir.

on:

if: ve unless: # Doğrulamanın hangi koşulda gerçekleşeceğini veya

gerçekleşmeyeceğini belirtir.

save

create

update

```ruby
# Doğrulamanın ne zaman gerçekleşeceğini belirtir.
```

### Validation Options - allow_nil

Doğrulanan değer nil olduğunda doğrulamayı atlar.

```ruby
class Post < ApplicationRecord
validates :status, inclusion: { in: statuses.keys },
allow_nil: true
end
Post.new(title: "a", article: "b", status: nil).valid?
=> true
Post.new(title: "a", article: "b", status: :removed).valid?
=> false
```

### Validation Options - allow_blank

Özniteliğin değeri boşsa (örneğin nil veya boş bir dize) doğrulamanın

geçmesini sağlar.

```ruby
class Contact < ApplicationRecord
validates :phone_number, numericality: { only_integer: true
}, allow_blank: true
end
User.create(id_number: "").valid?
=> true
User.create(id_number: nil).valid?
=> true
```

### Validation Options - on

Doğrulamanın ne zaman gerçekleşeceğini belirtmenize olanak tanır.

Validasyonlar varsayılan olarak kaydetme (save) sırasında çalışır.

```ruby
class User < ApplicationRecord
# Default olarak update ve create eylemlerinde çalışır.
validates :first_name, presence: true
# Burada oluşabilecek sıkıntı ne?
validates :email, uniqueness: true, on: :create
# Burada oluşabilecek sıkıntı ne?
validates :age, numericality: true, on: :update
end
```

### Validation Options - if ve unless

Koşullu doğrulama yapılmasına imkan sağlar.

```ruby
class Order < ApplicationRecord
validates :card_number, presence: true, if: :paid_with_card?
def paid_with_card?
payment_type == "card"
end
end
```

### Validation Options - message

### Active Record, her validation helper için varsayılan hata mesajını

kullanır. Ancak :message seçeneği ile doğrulama başarısız olduğunda

hatalar koleksiyonuna eklenecek mesajı kendimiz belirleyebiliriz.

```ruby
class Post < ApplicationRecord
validates :title, presence: { message: "Post başlığı boş
bırakılamaz."}
end
```

### Hata Mesajları

- errors

- errors.messages

```ruby
class Post < ApplicationRecord
validates :title, presence: { message: "Post başlığı boş
bırakılamaz." }
end
Post.new.errors.any?
=> false
Post.create.errors.messages
=> {:title=>["Post başlığı boş bırakılamaz."]
```

### Hata Mesajları

- errors.messages.values

- errors[:attr]

Post.create.errors.messages.values

```ruby
=> ["Post başlığı boş bırakılamaz."]
Post.create.errors[:title]
=> ["Post başlığı boş bırakılamaz."]
class Post < ApplicationRecord
validates :title, presence: { message: "Post başlığı boş
bırakılamaz." }
end
```

### Hata Mesajları

- errors.count

- errors.clear

Post.create.errors.size

```ruby
=> 1
Post.create.errors.clear
=> [ ]
class Post < ApplicationRecord
validates :title, presence: { message: "Post başlığı boş
bırakılamaz." }
end
```

### Post Modeli Validation ve Normalizasyon Son Hali

```ruby
class Post < ApplicationRecord
normalizes :title, with: -> title { title.squish.titlecase }
validates :title, presence: true, uniqueness: true, length: {
maximum: 255 }
validates :article, presence: true, length: {maximum: 65_535}
validates :status, inclusion: { in: statuses.keys }
end
```

### Kategori Validation ve Normalizasyon

```ruby
class Category < ApplicationRecord
normalizes :name, with: ->(name) { name.squish.titleize }
validates :name, presence: true
end
```

### Kategori modelindeki name alanının boş geçilmemesini ve normalizasyon

ile titleize edilmesini sağlayın.

### Sayfalarda Hata Mesajlarının Gösterimi

Post formunda hata gösteriminin yapılabilmesi için _form.html.erb dosyasına

şunları ekleyin:

```ruby
<% if post.errors.any? %>
<div class="alert alert-danger">
<h5><%= post.errors.count %> hata bulundu:</h5>
<ul class="mb-0">
<% post.errors.full_messages.each do |message| %>
<li><%= message %></li>
<% end %>
</ul>
</div>
<% end %>
```

### Sayfalarda Hata Mesajlarının Gösterimi

PostController içindeki düzenlemeler:

```ruby
def create
@post = Post.new(post_params)
if @post.save
redirect_to posts_path
else
render :new, status: :unprocessable_entity
end
end
def update
if @post.update(post_params)
redirect_to post_path(@post)
else
render :edit, status: :unprocessable_entity
end
end
422: Validasyon hatalarından
dolayı sunucu veriyi işleyemiyor.
```

### Sayfalarda Hata Mesajlarının Gösterimi

### Active Storage

```ruby
rails active_storage:install
rails db:migrate
Blog postuna resim alanı ekleyebilmek için dosya upload edebilmemiz
gerekiyor. Burada Active Storage devreye giriyor.
```

### Active Storage, dosyaları Amazon S3, Google Cloud Storage veya Microsoft

Azure Storage gibi bir bulut depolama hizmetleri gibi upload etmeyi ve bu

dosyaları Active Record nesnelerine eklemeyi kolaylaştırır.

### Active Storage - Dosya Attach Etme

Bir dosya attach etmek için has_one_attached kullanılır.

```ruby
class Post < ApplicationRecord
has_one_attached :image
end
def post_params
params.require(:post).permit(:title, :article, :status,
:image, category_ids: [])
end
controllers/posts_controller.rb
models/post.rb
```

### Active Storage - Dosya Attach Etme

```ruby
<%= form.label :image, "Resim", class: "form-label" %>
<%= form.file_field :image, class: "form-control" %>
views/posts/_form.html.erb
<% if @post.image.present? %>
<%= image_tag(@post.image) %>
<% end %>
views/posts/show.html.erb
Eklenen Resmin Blog Sayfasında Gösterilmesi
```

---

## Hafta 9 — I18n, FriendlyId, Action Text

### 9. Hafta Ders İçeriği

- Yerelleştirme - Internationalization (I18n)

- Url Düzenleme (friendly_id)

- Zengin İçerik Üretimi - Action Text

### Internationalization (I18n) - Y erelleştirme

I18n (Internationalization), uygulamanızı Türkçe dışındaki bir dile çevirmek

veya uygulamanızda çoklu dil desteği sağlamak için kullanımı kolay ve

genişletilebilir bir çerçeve sağlar.

I18n API’nin en önemli metotları şunlardır:

translate # Metin çevirilerinde kullanılır.

localize  # Tarih ve saat nesnelerini belirtilen biçimlere göre

yerelleştirir.

Şu şekilde de kullanılabilirler:

I18n.t "store.title"

I18n.l Time.now

### Internationalization (I18n) - Y erelleştirme

### Yerelleştirme ayarlarının yapılması gerekmektedir. locale.rb dosyasını

oluşturun.

I18n.load_path +=

Dir[Rails.root.join("config/locales/**/*.yml").to_s]

I18n.available_locales = [ :tr, :en]

I18n.default_locale = :tr

conﬁg/initializers/locale.rb

### Internationalization (I18n) - Switch

Uygulamada diller arası geçiş nasıl yapılacak?

around_action :switch_locale

private

```ruby
def switch_locale(&action)
locale = params[:locale] || I18n.default_locale
I18n.with_locale(locale, &action)
end
application_controller.rb
application_controller dosyasına yukarıdaki kodları ekleyelim.
Y erelleştirme Dosya Yapısı
conﬁg
locales
|-defaults
|---tr.yml
|---en.yml
|-models
|---post
|-----tr.yml
|-----en.yml
|-views
|---defaults
|-----tr.yml
|-----en.yml
|---posts
|-----tr.yml
|-----en.yml
Y erelleştirmede Default Değerler
config/locales/defaults/tr.yml dosyası oluşturalım ve
https://github.com/svenfuchs/rails-i18n/blob/master/rails/locale/tr.yml
adresindeki içeriği kopyalayıp dosya içerisine kaydedelim.
config/locales/defaults/en.yml dosyası oluşturalım ve
https://github.com/svenfuchs/rails-i18n/blob/master/rails/locale/en.yml
adresindeki içeriği kopyalayıp dosya içerisine kaydedelim.
config/locales/defaults/tr.yml dosyasının en üstüne eylemler (actions)
için şunları ekleyin:
tr:
actions:
name: İşlemler
back: Geri
destroy: Sil
edit: Düzenle
new: Ekle
reset: Sıfırla
search: Ara
show: Görüntüle
update: Güncelle
Y erelleştirmede Default Değerler
config/locales/defaults/en.yml dosyasının içine eylemler (actions) için
şunları ekleyin:
en:
actions:
name: Actions
back: Back
destroy: Destroy
edit: Edit
new: New
reset: Reset
search: Search
show: Show
update: Update
Y erelleştirmede Default Değerler
Y erelleştirmelerin Sayfalarda Kullanımı
Bütün görüntüleme linklerini güncelleyelim. Örnek Post index sayfasındaki
show linki.
<%= link_to t("actions.show"), post_path(post), class:"btn btn-info
btn-sm" %>
```

### Post show sayfasındaki edit, back ve destroy linklerini güncelleyelim.

```ruby
<%= link_to t("actions.back"), posts_path, class: "btn btn-secondary
me-1" %>
<%= link_to t("actions.edit"), edit_post_path(@post), class: "btn
btn-warning" %>
<%= button_to t("actions.destroy"), @post, method: :delete, data: {
turbo_confirm: "Emin misin?" }, class: "btn btn-danger" %>
Url’ye localhost:3000/posts/?locale=en yazınca ne oluyor gözlemleyin.
Post Model Y erelleştirme
config/locales/models/post/tr.yml dosyası oluşturalım.
tr:
```

### activerecord:

models:

post:

one: Blog Girdisi

other:  Blog Girdileri

attributes:

post:

article: Post Metni

category: Kategori

image: Post Resmi

status: Post Yayın Durumu

title:  Post Başlığı

enums:

post:

statuses:

draft: Taslak

published:  Yayınlandı

inactive: Yayından kaldırıldı

Post Model Y erelleştirme

config/locales/models/post/en.yml dosyası oluşturalım.

en:

### activerecord:

models:

post:

one: Post

other:  Posts

attributes:

post:

article: Post Article

category: Post Category

image: Post Image

status: Post Status

title: Post Title

enums:

post:

statuses:

draft: Draft

published: Published

inactive: Inactive

Post Model Y erelleştirme

Model yerelleştirmeleri yaptıktan sonra post form’da kullanılan label’lar silinebilir.

<div class="mb-2">

```ruby
<%= form.label :title, "Post Başlığı", class: "form-label" %>
<%= form.text_field :title, class: "form-control" %><br/>
</div>
<div class="mb-2">
<%= form.label :article, "Post Metni", class: "form-label" %>
<%= form.text_area :article, class: "form-control" %><br/>
</div>
X
X
Post View Y erelleştirme
config/locales/views/post/tr.yml dosyasını oluşturup form başlıklarını ekleyelim
tr:
posts:
edit:
title:  Post Güncelle
new:
title:  Yeni Post
<%= render "form", post: @post, form_title: t(".title") %>
views/posts/new.html.erb
<%= render "form", post: @post, form_title: t(".title") %>
views/posts/edit.html.erb
Post View Y erelleştirme
config/locales/views/post/en.yml dosyasını oluşturup form başlıklarını ekleyelim
en:
posts:
edit:
title:  Edit Post
new:
title:  New Post
```

### Footer’da gösterilen linkleri yerelleştirelim.

tr:

shared:

### footer:

about: Hakkımda

categories: Kategoriler

home: Anasayfa

projects: Projelerim

Y erelleştirmede Default Değerler

conﬁg/locales/views/shared/tr.yml

en:

shared:

### footer:

about: About

categories: Categories

home: Home

projects: Projects

conﬁg/locales/views/shared/en.yml

Y erelleştirmelerin Sayfalarda Kullanımı

### Footer için eklenen yerelleştirmeleri kullanalım.

<li class="nav-item">

```ruby
<%= link_to t(".home"), root_path, class:"nav-link px-2
text-body-secondary" %>
</li>
<li class="nav-item">
<%= link_to t(".projects"), projects_path, class: "nav-link px-2
text-body-secondary" %>
</li>
<li class="nav-item">
<%= link_to t(".categories"), categories_path, class: "nav-link px-2
text-body-secondary" %>
</li>
<li class="nav-item">
<%= link_to t(".about"), about_path, class: "nav-link px-2
text-body-secondary" %>
</li>
views/shared/_footer.html.erb
```

### Kategori Sayfalarının Y erelleştirilmesi

### Kategori sayfalarının post modelinde olduğu gibi bütün

### yerelleştirmelerini yapın.

### Category Model Y erelleştirme

config/locales/models/category/tr.yml dosyası oluşturalım.

tr:

### activerecord:

models:

category:

one: Kategori

other: Kategoriler

attributes:

category:

name: Kategori Adı

code:  Kategori Kodu

### Category Model Y erelleştirme

config/locales/models/category/en.yml dosyası oluşturalım.

en:

### activerecord:

models:

category:

one: Category

other: Categories

attributes:

category:

name: Category Name

code:  Category Code

### Kategori View Y erelleştirme

config/locales/views/category/tr.yml dosyasını oluşturup form başlıklarını ekleyelim.

tr:

categories:

edit:

title:  Kategori Güncelle

new:

title:  Yeni Kategori

config/locales/views/category/en.yml dosyasını oluşturup form başlıklarını ekleyelim.

en:

categories:

edit:

title: Update Category

new:

title: New Category

### Kategori View Y erelleştirme

```ruby
<% content_for :title, t(".title") %>
<%= render "form", category: @category %>
<% content_for :title, t(".title") %>
<%= render "form", category: @category %>
app/views/categories/edit.html.erb
app/views/categories/new.html.erb
⭐
```

### Footer’a Türkiye ve ABD bayrak iconu kullanarak bunlara

basıldığında ilgili yerelleştirilmiş sayfaların gösterilmesini sağlayın.

link_to url_for(locale: :tr) link_to url_for(locale: :en)

Friendly_id Gem Ekle

https://github.com/norman/friendly_id  Gemfile’a friendly_id ekleyelim.

gem 'friendly_id', '~> 5.7'

$ bundle install

$ rails generate friendly_id

$ rails g migration AddSlugToPosts slug:uniq

$ rails db:migrate

### Modele Ekleyelim

```ruby
class Post < ApplicationRecord
extend FriendlyId
friendly_id :title, use: :slugged
end
Post.find_each(&:save)
Rails console çalıştırıp tüm var olan kayıtları güncelleyelim. Amaç yeni
oluşturulan slug alanını doldurmak ve artık url’de post id’si yerine post
başlığının gösterilmesini sağlamak.
app/models/post.rb
```

### Controller Düzenleme

```ruby
class PostsController < ApplicationController
def set_post
@post = Post.friendly.find(params[:id])
end
end
Server çalıştırıp post show sayfasına gidin ve url’i kontrol edin.
app/controllers/posts_controller.rb
```

### Blog Girdilerinde Zengin İçerik Üretimi

bin/rails action_text:install

bin/rails action_text:install

```ruby
rails db:migrate
rails assets:precompile
İçerik oluştururken aşağıdaki gibi bir menü kullanmak için rails Action Text projeye
eklenir.
```

### Blog Girdilerinde Zengin İçerik Üretimi

```ruby
# app/models/post.rb
class Post < ApplicationRecord
has_rich_text :article
end
<%# app/views/posts/_form.html.erb %>
<%= form_with model: post do |form| %>
<%= form.label :article %>
<%= form.rich_textarea :article %>
<% end %>
Post model ve form içeriğine ekleme yapalım.
```

### Blog Girdilerinde Zengin İçerik Üretimi

sudo apt-get install libvips

Post içerisindeki resimlerin gözükmesi için libvips kütüphanesi kurulması

gerekiyor.

---

## Hafta 10 — Devise & Authorization

10.Hafta Ders İçeriği

- Devise ile User Modeli Oluşturma

- Kullanıcılara Rol Ekleme

- User ve Post Model İlişkilendirme

### Devise Kütüphanesi

### Devise, Rails uygulamaları için tam özellikli bir kimlik doğrulama (Authentication) çözümüdür.

İçerisinde aşağıdaki gibi birçok hazır özellik bulunur:

Database Authenticatable Kullanıcı adı/e-posta + şifre ile giriş

Registerable Kayıt olma, hesap oluşturma

Recoverable Şifre sıfırlama

Rememberable Beni hatırla özelliği

Trackable Oturum takibi (son giriş zamanı, IP vs.)

Confirmable E-posta onayı

Lockable Belirli sayıda yanlış girişte hesap kilitleme

Timeoutable Belirli süre işlem yapılmazsa oturumun düşmesi

Omniauthable Google, Facebook gibi OAuth sağlayıcıları ile giriş

### Authentication ve Authorization Farkları

### Authentication

(Kimlik Doğrulama)

Authorization

(Yetkilendirme)

Ne yapar? Bir kullanıcının gerçekten o kişi olup

olmadığını doğrular.

Doğrulanmış bir kullanıcının hangi

### kaynaklara veya işlemlere erişim hakkı

olduğunu belirler.

Ne zaman? Sisteme giriş yaparken (login

aşamasında)

Kimlik doğrulandıktan sonra (oturum

açıldıktan sonra)

Nasıl

çalışır?

Genellikle kullanıcı adı ve şifre, bazen

de biyometrik veriler, SMS kodları

veya iki faktörlü kimlik doğrulama ile.

Genellikle roller, izinler ya da yetki

politikaları (policies) ile.

Örnek Kullanıcının e-posta ve şifre ile

sisteme giriş yapması.

Sisteme giriş yapmış bir kullanıcının

sadece kendi dosyalarına erişebilmesi,

başkasının dosyalarına erişememesi.

Rails’de yetkilendirme işlemleri için genellikle Pundit, CanCanCan gibi başka kütüphaneler kullanılır.

### Devise Gem Ekle

### Devise gem’ini Gemfile’e ekleyelim: https://github.com/heartcombo/devise

```ruby
bundle add devise
rails generate devise:install
rails generate devise User firstname lastname
gender:integer username slug active:boolean
User modelini oluşturalım.
```

### Devise Gem Ekle

### Migration dosya içerisinde eklediğimiz bazı alanların düzenlenmesi:

create_table :users do |t|

t.string :firstname

t.string :lastname

t.integer :gender

t.string :username

t.string :slug

t.boolean :active, default: true

```ruby
end
add_index :users, :username,             unique: true
add_index :users, :slug,                 unique: true
rails db:migrate
Kullanıcılar sisteme giriş yaptığında 30 dakika boyunca herhangi bir aktivite
gerçekleştirmezse sistemden çıkışının yapılması ve tekrar giriş yapmasını
sağlamak için timeoutable modülünün aktifleştirilmesi gerekmektedir.
class User < ApplicationRecord
```

### devise :database_authenticatable, :registerable,

:recoverable, :rememberable, :validatable,

:timeoutable

```ruby
end
app/models/user.rb
User modeline gender (cinsiyet) için parametreleri enum olarak ekleyelim ve
```

### URL düzenlemesi için friendly_id kütüphanesini kullanalım.

```ruby
class User < ApplicationRecord
```

### devise :database_authenticatable, :registerable,

:recoverable, :rememberable, :validatable, :timeoutable

extend FriendlyId

friendly_id :username, use: :slugged

enum :gender, {

secret: 0,

male: 1,

female: 2

}

```ruby
end
User modeline validasyonları ve normalizasyonları ekleyelim.
class User < ApplicationRecord
normalizes :firstname, with: -> firstname {
firstname.squish.titlecase }
normalizes :lastname, with: -> lastname { lastname.squish.titlecase}
validates :firstname, presence: true, length: { maximum: 255 }
validates :lastname, presence: true, length: { maximum: 255 }
validates :username, presence: true, length: { maximum: 32 },
uniqueness: true
validates :email, presence: true, uniqueness: true
validates :gender, inclusion: { in: genders.keys }
end
```

### Devise Sayfalarını Düzenle

### Devise view sayfalarını oluşturun.

```ruby
rails g devise:views
Registration (sign-up) ve session (sign-in) sayfalarını bootstrap ile düzenleyin.
```

### Devise Sayfalarını Düzenle

Kayıt ve giriş sayfalarını düzenlemek için

https://gist.github.com/ecmelkytz/4d0f9fad17f9462312bfe67e8a59e583

linkindeki örnek kodları kullanabilirsiniz.

- Registration (sign-up) kodunu views/devise/registrations/new.html.erb

dosya içerisine ekleyin.

- Session (sign-in) kodunu views/devise/sessions/new.html.erb dosya

içerisine ekleyin.

### Devise Strong Parameter

Giriş ve kayıt ol sayfalarındaki veri alanlarının kontrolü için (strong parameter)

application_controller’a aşağıdaki eklemeler yapılmalı.

```ruby
class ApplicationController < ActionController::Base
before_action :configure_permitted_parameters, if:
:devise_controller?
protected
def configure_permitted_parameters
```

### devise_parameter_sanitizer.permit(:sign_up, keys: [:firstname,

:lastname, :email, :username, :gender])

### devise_parameter_sanitizer.permit(:sign_in, keys: [:email,

:password])

```ruby
end
end
app/controllers/application_controller.rb
Y erelleştirme
Model alanlarının çevirileri için locales/models/user altında tr.yml ve en.yml
dosyalarını oluşturun.
tr:
```

### activerecord:

models:

user:

one: Kullanıcı

other: Kullanıcılar

attributes:

user:

email: E-posta

gender: Cinsiyet

firstname: Ad

lastname: Soyad

active: Aktiflik Durumu

password: Parola

password_confirmation: Parola Teyit

created_at: Oluşturulma Tarihi

updated_at: Güncellenme Tarihi

username: Kullanıcı Adı

remember_me: Beni Hatırla

en:

### activerecord:

models:

user:

one: User

other: Users

attributes:

user:

email: E-mail

gender: Gender

firstname: First Name

lastname: Last Name

active: Active

password: Password

password_confirmation: Password

Confirmation

created_at: Created at

updated_at: Updated at

username: Username

remember_me: Remember Me

Y erelleştirme

### Devise için default çeviriler:

Türkçe için: https://github.com/tigrish/devise-i18n/blob/master/rails/locales/tr.yml

locales/defaults/devise/tr.yml dosyasına kaydedin.

İngilizce için: https://github.com/tigrish/devise-i18n/blob/master/rails/locales/en.yml

locales/defaults/devise/en.yml dosyasına kaydedin.

### Kullanıcı Kaydı Gerçekleştirin

Kayıt sayfasını kullanarak kullanıcı kaydı gerçekleştirin.

```ruby
rails c ile konsola giriş yapın ve oluşturulan kullanıcıyı görüntüleyin.
User.last
#<User id: 1, firstname: "Aslıhan", lastname: "Kartal", gender:
"female", active: true, email: [FILTERED], created_at: "2024-01-07
15:12:33.550750000 +0000", updated_at: "2024-01-07
15:12:33.550750000 +0000">
User modeline fullname adında bir custom metot ekleyin.
def fullname
"#{firstname} #{lastname}"
end
User.last.fullname
=> "Aslıhan Kartal"
app/models/user.rb
```

### Navbar Güncelle

Sisteme giriş yapıldığında navbar’da kullanıcı ismi gözüksün ve dropdown menü

kullanarak sistemden çıkış yapılması sağlansın.

- Sisteme giriş yapıldıktan sonra current_user ile kullanıcı bilgilerine ulaşılabilir.

```ruby
Ör: current_user.fullname  # => Ecmel Albayrak
- Sisteme giriş yapmış mı sorgusu için:  user_signed_in?
- Sistemden çıkış yapmak için:
link_to destroy_user_session_path, method: :delete, data: { turbo_method:
:delete }
```

### Navbar Güncelle

- Kullanıcı sisteme giriş yaptıysa navbar’da kullanıcı adı - soyadı gözükecek

ve dropdown menüde “Çıkış Yap” butonuna basınca çıkış yapacak.

- Kullanıcı sisteme giriş yapmadıysa “Giriş Yap” ve “Kayıt Ol “butonları

### navbar’da gözükecek.

### Navbar’ın güncel halini aşağıdaki linkteki koddan yardım alarak

oluşturabilirsiniz.

https://gist.github.com/ecmelkytz/bd19ef014acef75e47450a433f827b68

Giriş Y etkisi

Giriş yapılmadan görüntülenmesini istemediğiniz sayfanın controller’ına

before_action :authenticate_user! eklemeniz gerekmektedir.

application_controller dosyasına veya sadece posts_controller dosyasına

eklerseniz ne olur gözlemleyin.

### Rol Ekleme

User modeline role alanı ekleyelim ve enum olarak oluşturalım. Kullanıcı rolü

default olarak editor olsun.

```ruby
rails g migration AddRoleToUser role:integer
enum :role, { editor: 1, admin: 2 }
class AddRoleToUser < ActiveRecord::Migration[8.0]
def change
add_column :users, :role, :integer, default: 1
end
end
app/models/user.rb
Ardından rails db:migrate komutunu çalıştıralım.
```

### Admin Altında Kullanıcı Bilgileri

namespace :admin do

resources :users, only: [:index, :show, :edit, :update]

```ruby
end
conﬁg/routes.rb
Admin dizi altında kullanıcı işlemlerini yapabilmek için ilgili yolları ekleyelim.
```

### Admin Altında Kullanıcı Bilgileri

İlgili kullanıcı sayfalarını görüntülemek için controllers/admin dizini altında

users_controller.rb dosyası içerisinde index, show, edit ve update action’larını

oluşturun.

module Admin

```ruby
class UsersController < ApplicationController
before_action :authenticate_user!
def index
@users = User.all
end
end
end
controllers/admin/users_controller.rb
```

### Admin Altında Kullanıcı Bilgileri

module Admin

```ruby
class UsersController < ApplicationController
before_action :set_user, only: %i[show edit update]
def  show; end
def edit; end
private
def set_user
@user = User.friendly.find(params[:id])
end
end
end
```

### Admin Altında Kullanıcı Bilgileri

module Admin

```ruby
class UsersController < ApplicationController
before_action :set_user, only: %i[show edit update]
def update
if @user.update(user_params)
redirect_to admin_user_path(@user)
else
render :edit, status: :unprocessable_entity
end
end
end
end
Sadece admin rolüne sahip olanlar admin altındaki sayfalara ulaşabilsin.
module Admin
class UsersController < ApplicationController
before_action :authorize_admin
private
def  authorize_admin
redirect_to root_path, alert: "Permissions denied"
unless current_user.admin?
end
end
controllers/admin/users_controller.rb
```

### Admin Altında Kullanıcı Sayfaları

Kullanıcılar için controllers/admin/users_controller.rb, views/admin/users/

altında index.html.erb, show.html.erb ve edit.html.erb dosya içerikleri için

örnek kod içeriği:

https://gist.github.com/ecmelkytz/3475e7ded52321c7726f5e601ac71156

### Post Modeline Kullanıcı Bilgisi Ekleme

```ruby
rails c çalıştırıp veritabanındaki bütün post kayıtlarını silelim.
Post.destroy_all
Proje dizininde Post modeline user_id eklemek için aşağıdaki kodu yazalım:
rails g migration AddUserToPost user:references
rails db:migrate
class AddUserToPost < ActiveRecord::Migration[8.0]
def change
add_reference :posts, :user, null: false, foreign_key: true
end
end
```

### Post ile User Arasında İlişkileri Ekleyelim

```ruby
class Post < ApplicationRecord
belongs_to :user
end
class User < ApplicationRecord
has_many :posts, dependent: :destroy
end
```

### Post için Strong Parameter

```ruby
def post_params
params.require(:post).permit(:title, :article,
:status, :image, :user_id, category_ids: [])
end
```

### Post modeline eklenen user_id bilgisini controllers/posts_controller.rb içindeki

post_params metoduna ekleyelim.

### Post Controller Düzenleme

Sisteme giriş yapan kullanıcı (current_user) adına post girdisinin oluşturulması için:

```ruby
def create
@post = current_user.posts.new(post_params)
if @post.save
redirect_to posts_path, notice: "Post başarılı bir
şekilde oluşturuldu."
else
render :new, status: :unprocessable_entity
end
end
controllers/posts_controller.rb
```

---

---

## Sınav Soruları (Kendini Test Et)

Site test bolumunde 39 soru ve detayli cevaplar interaktif olarak yer alir.

---

## Komut Hızlı Referans

```bash
rails new app -d postgresql --css bootstrap
rails s / rails c
rails g model Post title:text
rails g migration AddStatusToPost status:integer
rails db:create / db:migrate / db:rollback / db:seed / db:reset
rails routes
rails active_storage:install
bin/rails action_text:install
bundle add devise
rails generate devise:install
git add . && git commit -m "mesaj" && git push
```