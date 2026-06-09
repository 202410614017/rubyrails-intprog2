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

## L — Liskov Substitution Principle (Liskov Yerine Geçme İlkesi)

| | |
|---|---|
| **İlke tanımı** | Alt sınıf, üst sınıfın yerine geçebilmeli; geçince program bozulmamalı. |
| **Amacı / çözmeye çalıştığı problem** | Polimorfizmde alt sınıfın sözleşmeyi bozmaması. Sung Jinwoo da bir Avcı — yerine konunca program çalışıyor mu? |

### İlkeye aykırı (kötü) kod — YanlisPlayer

```python
class Avci_Kotu:
    def guc_artir(self, miktar):
        self.guc += miktar
    def zeka_artir(self, miktar):
        self.zeka += miktar

class YanlisPlayer(Avci_Kotu):
    def guc_artir(self, miktar):
        self.guc += miktar
        self.zeka += miktar  # BEKLENMEDİK!

# stat_test_et: guc+10, zeka+5 → guc=20, zeka=15 beklenir
# YanlisPlayer → zeka=20 → KALDI (LSP İHLALİ)
```

**Neden kötü?** Güç artınca zeka da artıyor; üst sınıfı bekleyen test patlar.

### İlkeye uygun (iyi) kod — Hunter / SungJinwoo

```python
class Hunter(ABC):
    @abstractmethod
    def dungeon_temizle(self, seviye: int) -> bool: ...
    @abstractmethod
    def skill_kullan(self) -> str: ...

class SungJinwoo(Hunter):
    def dungeon_temizle(self, seviye):
        return True  # sözleşme: bool döner
    def skill_kullan(self):
        return "Arise kullandi"  # sözleşme: str döner

def baskani_hazirla(hunter: Hunter, seviye):
    if hunter.dungeon_temizle(seviye):
        print(hunter.skill_kullan())
# Hangi hunter gelirse gelsin çalışır — LSP TAMAM
```

**Neden iyi?** Her alt sınıf aynı sözleşmeye uyar; SungJinwoo ekstra özellik ekler ama bozmaz.

### LSP'nin 5 Kuralı (Solo Leveling)

1. **Ön koşul** — Alt sınıf daha katı şart koyamaz (E-rank avcı seviye 5 dungeon reddedemez).
2. **Son koşul** — Alt sınıf daha az garanti veremez (item düşmeli).
3. **Değişmez** — İç kurallar bozulmamalı (toplam_stat = guc + zeka).
4. **İstisna** — Yeni beklenmedik hata fırlatılamaz.
5. **Dönüş tipi** — skill_kullan() her zaman str dönmeli.

*Detaylı Python kodu: site #lsp-solo-leveling | Örnek çalışma: Muhammed Hamza Erha*

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
