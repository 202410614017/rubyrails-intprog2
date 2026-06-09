# -*- coding: utf-8 -*-
"""SOLID ilkeleri — sinav/odev formatinda (Ruby ornekleri)."""

STUDENT_HEADER = {
    "title": "SOLID Ilkeleri",
    "subtitle": "Internet Programciligi II — Nesne Yonelimli Tasarim",
    "fields": ["Ad Soyad: ___________________________", "Ogrenci No: _________________________", "Tarih: ______________________________"],
}

SOLID = [
    {
        "letter": "S",
        "name": "Single Responsibility Principle (SRP)",
        "name_tr": "Tek Sorumluluk Ilkesi",
        "definition": (
            "Bir sinif yalnizca tek bir sorumluluga sahip olmalidir; yani sinifi degistirmek icin "
            "yalnizca tek bir nedeni olmalidir."
        ),
        "purpose": (
            "Buyuyen siniflarda kodun karismasini, bakim zorlugunu ve hata riskini azaltmak. "
            "Her modul tek bir isi yapsin; degisiklikler izole kalsin."
        ),
        "problem": "Bir sinif hem is mantigi hem dosya kaydi hem e-posta gonderimi yaparsa her yeni gereksinimde tum sinif kirilganlasir.",
        "bad_code": """class Post
  def publish
    save_to_database
    send_email_to_subscribers
    write_to_log_file
  end

  def save_to_database
    # veritabani islemi
  end

  def send_email_to_subscribers
    # e-posta gonderimi
  end

  def write_to_log_file
    # log yazma
  end
end""",
        "bad_why": (
            "Post sinifi ayni anda veritabani, e-posta ve loglama sorumluluklarini tasiyor. "
            "E-posta servisi degisirse Post sinifi degismek zorunda kalir. Test etmek zorlasir; "
            "tek bir degisiklik birden fazla nedenden dolayi sinifi etkiler — SRP ihlali."
        ),
        "good_code": """class Post
  def publish(publisher:, notifier:, logger:)
    publisher.save(self)
    notifier.notify_subscribers(self)
    logger.info("Post yayinlandi: #{title}")
  end
end

class PostPublisher
  def save(post)
    # sadece veritabani
  end
end

class EmailNotifier
  def notify_subscribers(post)
    # sadece e-posta
  end
end

class FileLogger
  def info(message)
    # sadece log
  end
end""",
        "good_why": (
            "Her sinifin tek gorevi var: Post yayinlama kararini verir, diger isleri uzman siniflara devreder. "
            "E-posta mantigi degistiginde yalnizca EmailNotifier guncellenir. Siniflar kucuk, test edilebilir "
            "ve bakimi kolay — SRP'ye uygun."
        ),
    },
    {
        "letter": "O",
        "name": "Open/Closed Principle (OCP)",
        "name_tr": "Acik/Kapali Ilke",
        "definition": (
            "Yazilim varliklari (siniflar, moduller) genislemeye acik, degisiklige kapali olmalidir. "
            "Mevcut kodu degistirmeden yeni davranis eklenebilmelidir."
        ),
        "purpose": (
            "Calisan kodu bozmadan yeni ozellik eklemek. if/elsif zincirleri yerine genisleme "
            "(kalitim, modul, polymorphism) ile yeni davranislar eklenir."
        ),
        "problem": "Her yeni odeme tipi icin mevcut sinifa if/elsif eklenirse kod surekli degisir ve regression riski artar.",
        "bad_code": """class PaymentProcessor
  def pay(method, amount)
    if method == :credit_card
      # kredi karti odeme
    elsif method == :paypal
      # paypal odeme
    elsif method == :bank_transfer
      # havale — her yeni tip icin buraya ekleme yapilir
    end
  end
end""",
        "bad_why": (
            "Yeni bir odeme yontemi (ornegin :crypto) eklendiginde PaymentProcessor sinifinin "
            "icindeki pay metodu degistirilmek zorunda. Acik/kapali ilkeye gore sinif "
            "genislemeye kapali degil, her ekleme mevcut kodu kirar — OCP ihlali."
        ),
        "good_code": """class PaymentProcessor
  def pay(gateway, amount)
    gateway.charge(amount)
  end
end

class CreditCardGateway
  def charge(amount)
    # kredi karti
  end
end

class PaypalGateway
  def charge(amount)
    # paypal
  end
end

# Yeni tip: mevcut kodu degistirmeden ekle
class CryptoGateway
  def charge(amount)
    # kripto odeme
  end
end""",
        "good_why": (
            "PaymentProcessor artik hangi odeme tipi oldugunu bilmez; charge metoduna sahip "
            "her gateway calisir. CryptoGateway eklemek icin PaymentProcessor'a dokunulmaz. "
            "Mevcut kod kapali (degismez), yeni davranis genislemeyle acik — OCP'ye uygun."
        ),
    },
    {
        "letter": "L",
        "name": "Liskov Substitution Principle (LSP)",
        "name_tr": "Liskov Yerine Koyma Ilkesi",
        "definition": (
            "Alt sinif nesneleri, ust sinif nesnelerinin yerine kullanilabilmeli; "
            "programin davranisi bozulmamali."
        ),
        "purpose": (
            "Kalitim hiyerarsisinde alt sinifin ust sinifin sozlesmesini (contract) bozmamasini saglamak. "
            "Polimorfizm guvenli calissin."
        ),
        "problem": "Alt sinif ust sinifin bekledigi davranisi degistirirse (ornegin fly metodu hata firlatirsa) polimorfizm kirilir.",
        "bad_code": """class Bird
  def fly
    "Ucuyor"
  end
end

class Penguin < Bird
  def fly
    raise "Penguen ucamaz!"  # ust sinifin sozlesmesini bozar
  end
end

birds = [Bird.new, Penguin.new]
birds.each { |b| b.fly }  # Penguin'de patlar""",
        "bad_why": (
            "Penguin, Bird'in yerine konuldugunda fly cagrisi programi kirar. "
            "Ust sinif 'her kus ucabilir' beklentisi vardir; alt sinif bunu ihlal eder. "
            "LSP: alt sinif ust sinifin yerine guvenle kullanilamiyor."
        ),
        "good_code": """class Bird
  def move
    raise NotImplementedError
  end
end

class Sparrow < Bird
  def move
    "Ucuyor"
  end
end

class Penguin < Bird
  def move
    "Yuzuyor"
  end
end

birds = [Sparrow.new, Penguin.new]
birds.each { |b| puts b.move }  # ikisi de calisir""",
        "good_why": (
            "Ortak sozlesme move metodudur; her alt sinif kendi gercegini uygular. "
            "Penguin Bird yerine konuldugunda program bozulmaz. "
            "Alt sinif ust sinifin bekledigi arayuzu korur — LSP'ye uygun."
        ),
    },
    {
        "letter": "I",
        "name": "Interface Segregation Principle (ISP)",
        "name_tr": "Arayuz Ayirimi Ilkesi",
        "definition": (
            "Istemciler kullanmadiklari arayuzlere bagimli olmamali. "
            "Buyuk, siskin arayuzler yerine kucuk, ozellestirilmis arayuzler tercih edilmeli."
        ),
        "purpose": (
            "Siniflari zorunlu ama bos/kullanilmayan metot implementasyonlarindan kurtarmak. "
            "Modul ve mixin'lerde sadece gereken davranislar sunulur."
        ),
        "problem": "Tek dev modul hem yazdir hem taray hem faks metotlari icerirse bazı siniflar bos metot birakmak zorunda kalir.",
        "bad_code": """module Worker
  def work; end
  def eat; end
  def sleep; end
  def attend_meeting; end  # her worker icin gerekli degil
end

class Robot
  include Worker

  def work
    "Calisiyor"
  end

  def eat
    # robot yemek yemez — bos veya anlamsiz
  end

  def sleep
    # robot uyumaz
  end

  def attend_meeting
    # anlamsiz
  end
end""",
        "bad_why": (
            "Robot, kullanmadigi eat/sleep/attend_meeting metotlarini da implement etmek zorunda. "
            "Buyuk arayuz istemciyi gereksiz bagimliliklara zorlar. "
            "ISP: kullanilmayan metotlar arayuze dahil edilmemeli."
        ),
        "good_code": """module Workable
  def work; end
end

module Eatable
  def eat; end
end

class Human
  include Workable
  include Eatable

  def work; "Calisiyor"; end
  def eat; "Yemek yiyor"; end
end

class Robot
  include Workable

  def work; "Calisiyor"; end
  # sadece ihtiyaci olan modul
end""",
        "good_why": (
            "Arayuzler role gore ayrildi: Workable, Eatable. Robot yalnizca Workable alir; "
            "bos eat/sleep yazmak zorunda kalmaz. Her sinif sadece ihtiyaci olan davranisa bagimli — ISP'ye uygun."
        ),
    },
    {
        "letter": "D",
        "name": "Dependency Inversion Principle (DIP)",
        "name_tr": "Bagimlilik Tersine Cevirme Ilkesi",
        "definition": (
            "Ust seviye moduller alt seviye modullere bagimli olmamali; "
            "her ikisi de soyutlamalara (abstraction) bagimli olmalidir."
        ),
        "purpose": (
            "Siki bagimliliklari (concrete class) gevsetmek; test, degistirme ve genisletmeyi kolaylastirmak. "
            "Dependency Injection ile somut sinif yerine arayuz/soyut bagimlilik kullanilir."
        ),
        "problem": "Controller dogrudan PostgreSQL sinifina bagliysa MySQL'e gecis tum controller'i degistirir.",
        "bad_code": """class PostsController
  def create
    db = PostgreSQLConnection.new  # somut sinifa dogrudan bagimli
    db.insert(params[:post])
  end
end""",
        "bad_why": (
            "PostsController dogrudan PostgreSQLConnection somut sinifina bagimli. "
            "Veritabani degisirse controller degismek zorunda. "
            "Ust seviye (controller) alt seviyeye (PostgreSQL) bagimli — DIP ihlali."
        ),
        "good_code": """class PostsController
  def initialize(repository:)
    @repository = repository  # soyut bagimlilik enjekte edilir
  end

  def create(params)
    @repository.insert(params)
  end
end

class PostRepository
  def insert(data)
    # PostgreSQL veya baska implementasyon
  end
end

# Rails'de benzeri:
# @post = Post.new(post_params)  → ActiveRecord soyutlamasi
PostsController.new(repository: PostRepository.new)""",
        "good_why": (
            "Controller somut veritabani sinifini bilmez; repository arayuzune bagimlidir. "
            "Testte sahte (mock) repository enjekte edilebilir. "
            "Ust ve alt seviye soyutlamaya bagimli — DIP'ye uygun. Rails'de ActiveRecord da bu soyutlamadir."
        ),
    },
]
