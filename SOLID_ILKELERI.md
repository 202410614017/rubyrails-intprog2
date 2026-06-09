# SOLID İlkeleri

**İnternet Programcılığı II — Nesne Yönelimli Tasarım**

Ad Soyad: ___________________________  
Öğrenci No: _________________________  
Tarih: ______________________________

---

## S — Single Responsibility Principle (Tek Sorumluluk İlkesi)

| | |
|---|---|
| **İlke tanımı** | Bir sınıf yalnızca tek bir sorumluluğa sahip olmalıdır; yani sınıfı değiştirmek için yalnızca tek bir nedeni olmalıdır. |
| **Amacı / çözmeye çalıştığı problem** | Büyüyen sınıflarda kodun karışmasını, bakım zorluğunu ve hata riskini azaltmak. Bir sınıf hem iş mantığı hem dosya kaydı hem e-posta gönderimi yaparsa her yeni gereksinimde tüm sınıf kırılganlaşır. |

### İlkeye aykırı (kötü) kod örneği

```ruby
class Post
  def publish
    save_to_database
    send_email_to_subscribers
    write_to_log_file
  end
  # ... veritabanı, e-posta, log metotları aynı sınıfta
end
```

**Neden kötü?** Post sınıfı veritabanı, e-posta ve loglama sorumluluklarını aynı anda taşır. E-posta servisi değişirse Post değişmek zorunda kalır. Tek değişiklik birden fazla nedenden sınıfı etkiler — SRP ihlali.

### İlkeye uygun (iyi) kod örneği

```ruby
class Post
  def publish(publisher:, notifier:, logger:)
    publisher.save(self)
    notifier.notify_subscribers(self)
    logger.info("Post yayınlandı")
  end
end
# PostPublisher, EmailNotifier, FileLogger ayrı sınıflar
```

**Neden iyi?** Her sınıfın tek görevi var. E-posta mantığı değişince yalnızca EmailNotifier güncellenir — SRP'ye uygun.

---

## O — Open/Closed Principle (Açık/Kapalı İlke)

| | |
|---|---|
| **İlke tanımı** | Yazılım varlıkları genişlemeye açık, değişikliğe kapalı olmalıdır. Mevcut kodu değiştirmeden yeni davranış eklenebilmelidir. |
| **Amacı / çözmeye çalıştığı problem** | Çalışan kodu bozmadan yeni özellik eklemek. Her yeni ödeme tipi için if/elsif eklenmesi regression riskini artırır. |

### İlkeye aykırı (kötü) kod örneği

```ruby
class PaymentProcessor
  def pay(method, amount)
    if method == :credit_card
      # ...
    elsif method == :paypal
      # ...
    # her yeni tip için buraya ekleme
    end
  end
end
```

**Neden kötü?** Yeni ödeme yöntemi eklendiğinde `pay` metodu değiştirilmek zorunda — OCP ihlali.

### İlkeye uygun (iyi) kod örneği

```ruby
class PaymentProcessor
  def pay(gateway, amount)
    gateway.charge(amount)
  end
end
# CreditCardGateway, PaypalGateway, CryptoGateway — charge metodu
```

**Neden iyi?** Yeni gateway eklemek için PaymentProcessor'a dokunulmaz — OCP'ye uygun.

---

## L — Liskov Substitution Principle (Liskov Yerine Koyma İlkesi)

| | |
|---|---|
| **İlke tanımı** | Alt sınıf nesneleri, üst sınıf nesnelerinin yerine kullanılabilmeli; programın davranışı bozulmamalı. |
| **Amacı / çözmeye çalıştığı problem** | Kalıtımda alt sınıfın üst sınıfın sözleşmesini bozmamasını sağlamak. Polimorfizm güvenli çalışsın. |

### İlkeye aykırı (kötü) kod örneği

```ruby
class Bird
  def fly; "Uçuyor"; end
end
class Penguin < Bird
  def fly
    raise "Penguen uçamaz!"
  end
end
```

**Neden kötü?** Penguin, Bird yerine konulduğunda `fly` çağrısı programı kırar — LSP ihlali.

### İlkeye uygun (iyi) kod örneği

```ruby
class Bird
  def move; raise NotImplementedError; end
end
class Sparrow < Bird; def move; "Uçuyor"; end; end
class Penguin < Bird; def move; "Yüzüyor"; end; end
```

**Neden iyi?** Ortak sözleşme `move`; her alt sınıf kendi gerçeğini uygular — LSP'ye uygun.

---

## I — Interface Segregation Principle (Arayüz Ayırımı İlkesi)

| | |
|---|---|
| **İlke tanımı** | İstemciler kullanmadıkları arayüzlere bağımlı olmamalı. Büyük arayüzler yerine küçük, özelleştirilmiş arayüzler tercih edilmeli. |
| **Amacı / çözmeye çalıştığı problem** | Sınıfları zorunlu ama boş/kullanılmayan metot implementasyonlarından kurtarmak. |

### İlkeye aykırı (kötü) kod örneği

```ruby
module Worker
  def work; end
  def eat; end
  def sleep; end
end
class Robot
  include Worker
  def work; "Çalışıyor"; end
  def eat; end   # anlamsız
  def sleep; end # anlamsız
end
```

**Neden kötü?** Robot kullanmadığı `eat`/`sleep` metotlarını da implement etmek zorunda — ISP ihlali.

### İlkeye uygun (iyi) kod örneği

```ruby
module Workable; def work; end; end
module Eatable; def eat; end; end
class Robot
  include Workable
  def work; "Çalışıyor"; end
end
```

**Neden iyi?** Robot yalnızca ihtiyacı olan modülü alır — ISP'ye uygun.

---

## D — Dependency Inversion Principle (Bağımlılık Tersine Çevirme İlkesi)

| | |
|---|---|
| **İlke tanımı** | Üst seviye modüller alt seviye modüllere bağımlı olmamalı; her ikisi de soyutlamalara bağımlı olmalıdır. |
| **Amacı / çözmeye çalıştığı problem** | Sıkı bağımlılıkları gevşetmek; test ve değiştirmeyi kolaylaştırmak. Controller doğrudan PostgreSQL'e bağlıysa veritabanı değişince controller da değişir. |

### İlkeye aykırı (kötü) kod örneği

```ruby
class PostsController
  def create
    db = PostgreSQLConnection.new
    db.insert(params[:post])
  end
end
```

**Neden kötü?** Controller somut PostgreSQL sınıfına bağımlı — DIP ihlali.

### İlkeye uygun (iyi) kod örneği

```ruby
class PostsController
  def initialize(repository:)
    @repository = repository
  end
  def create(params)
    @repository.insert(params)
  end
end
```

**Neden iyi?** Controller soyut repository'ye bağımlı; testte mock enjekte edilebilir — DIP'ye uygun.

---

*Kaynak: SOLID — Robert C. Martin (Uncle Bob). Örnekler Ruby ile hazırlanmıştır.*
