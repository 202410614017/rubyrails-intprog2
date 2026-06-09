# -*- coding: utf-8 -*-
"""Nesne Yonelimli Programlama — ders konulari (PDF gelince genisletilecek)."""

OOP_META = {
    "title": "Nesne Yonelimli Programlama",
    "subtitle": "OOP Sinavi — SOLID, kalitim, polimorfizm, kapsulleme",
    "description": (
        "Bu bolum Nesne Yonelimli Programlama dersin icin. SOLID ilkeleri, "
        "LSP Solo Leveling ornegi ve temel OOP kavramlari burada. "
        "PDF slaytlarini attiginda otomatik olarak genisletilecek."
    ),
}

OOP_MUST_KNOW = [
    ("Kapsulleme", "@private veri + getter/setter veya attr_accessor ile kontrollu erisim"),
    ("Kalitim", "class Child < Parent — alt sinif ust siniftan ozellik alir"),
    ("Polimorfizm", "Ayni metod adi, farkli siniflarda farkli davranis (override)"),
    ("Soyutlama", "Gereksiz detayi gizle; abstract class / interface ile sozlesme"),
    ("LSP", "Alt sinif ust sinifin yerine konulunca program bozulmamali"),
    ("SRP", "Bir sinif tek sorumluluk — tek degisim nedeni"),
    ("OCP", "Genislemeye acik, degisiklige kapali"),
    ("ISP", "Kullanilmayan arayuze bagimli olma"),
    ("DIP", "Somut sinif yerine soyutlamaya bagimli ol"),
]

OOP_TOPICS = [
    {
        "id": "oop-nedir",
        "title": "OOP Nedir?",
        "summary": "Programi nesneler (veri + davranis) etrafinda organize eder.",
        "body": """**Nesne Yonelimli Programlama (OOP)** yazilimi **nesneler** etrafinda kurar.
Her nesne **veri (attribute)** ve **davranis (method)** icerir.

**4 temel kavram:**
1. **Kapsulleme** — veriyi gizle, kontrollu erisim
2. **Kalitim** — ust siniftan turetme
3. **Polimorfizm** — ayni arayuz, farkli davranis
4. **Soyutlama** — detayi gizle, onemli olani goster

**Sinav ipucu:** OOP'nin amaci kod tekrarini azaltmak, bakimi kolaylastirmak ve gercek dunya modellerini kodlamaktir.""",
        "code": """# Python
class Ogrenci:
    def __init__(self, ad, no):
        self.ad = ad      # attribute
        self.no = no

    def bilgi(self):      # method
        return f"{self.ad} - {self.no}"

# Ruby
class Ogrenci
  def initialize(ad, no)
    @ad = ad
    @no = no
  end
  def bilgi
    "#{@ad} - #{@no}"
  end
end""",
    },
    {
        "id": "kapsulleme",
        "title": "Kapsulleme (Encapsulation)",
        "summary": "Veriyi disaridan dogrudan erisilemez yap; getter/setter ile kontrol et.",
        "body": """**Kapsulleme** nesnenin ic verisini korur. Disaridan `@balance` veya `self.balance`
dogrudan degistirilmemeli.

**Ruby:** `@name` + `attr_reader` / `attr_writer` / `attr_accessor`
**Python:** `_name` (convention) veya `@property`

**Sinav ipucu:** Kapsulleme = veri gizleme + kontrollu erisim. Banka hesabinda bakiye
dogrudan degistirilemez, `yatir()` / `cek()` metotlari kullanilir.""",
        "code": """class BankaHesabi:
    def __init__(self):
        self.__bakiye = 0  # private

    def yatir(self, miktar):
        if miktar > 0:
            self.__bakiye += miktar

    def bakiye(self):
        return self.__bakiye""",
    },
    {
        "id": "kalitim",
        "title": "Kalitim / Miras (Inheritance)",
        "summary": "Alt sinif ust sinifin ozelliklerini alir; super ile ust metot cagrilir.",
        "body": """**Kalitim** kod tekrarini azaltir. Ortak ozellikler ust sinifta, ozel olanlar alt sinifta.

**Ruby:** `class Dog < Animal`
**Python:** `class Dog(Animal):`

**super** ust sinifin metodunu cagirir.

**Sinav ipucu:** IS-A iliskisi (Dog IS-A Animal). Kalitim ≠ composition (has-a).""",
        "code": """class Animal:
    def speak(self):
        return "Ses"

class Dog(Animal):
    def speak(self):
        return super().speak() + " — Hav hav!""",
    },
    {
        "id": "polimorfizm",
        "title": "Polimorfizm",
        "summary": "Ayni metod farkli siniflarda farkli sonuc uretir.",
        "body": """**Polimorfizm** ayni arayuzun farkli implementasyonlarini kullanmayi saglar.
Ust sinif referansi ile alt sinif nesneleri ayni sekilde islenebilir.

**Sinav ipucu:** Override = alt sinif ust metodu yeniden yazar.
Ornek: `speak()` — Kopek "hav", Kedi "miyav" der.""",
        "code": """def ses_cikar(hayvan):
    print(hayvan.speak())  # hangi sinif olursa olsun calisir

ses_cikar(Dog())
ses_cikar(Cat())""",
    },
    {
        "id": "soyutlama",
        "title": "Soyutlama (Abstraction)",
        "summary": "Gereksiz detayi gizle; abstract class/interface ile sozlesme tanimla.",
        "body": """**Soyutlama** kullanicinin sadece gerekli arayuzu gormesini saglar.
Ic implementasyon gizlenir.

**Python:** `ABC` + `@abstractmethod`
**Ruby:** abstract class pattern veya Module

**Sinav ipucu:** Soyut siniftan dogrudan nesne olusturulamaz (genelde).
Alt siniflar tum abstract metotlari implement etmeli.""",
        "code": """from abc import ABC, abstractmethod

class Sekil(ABC):
    @abstractmethod
    def alan(self):
        pass

class Daire(Sekil):
    def __init__(self, r):
        self.r = r
    def alan(self):
        return 3.14 * self.r ** 2""",
    },
    {
        "id": "solid-ozet",
        "title": "SOLID Ilkeleri Ozet",
        "summary": "S-O-L-I-D — iyi OOP tasariminin 5 temel ilkesi.",
        "body": """| Harf | Ilke | Tek cumle |
|------|------|-----------|
| **S** | Single Responsibility | Tek sorumluluk |
| **O** | Open/Closed | Genislemeye acik, degisiklige kapali |
| **L** | Liskov Substitution | Alt sinif yerine konulabilir |
| **I** | Interface Segregation | Kucuk arayuzler |
| **D** | Dependency Inversion | Soyutlamaya bagimli ol |

Asagida her ilke detayli orneklerle aciklandi. LSP icin Solo Leveling ornegine bak.""",
        "code": None,
    },
]

# PDF gelince doldurulacak bolumler
OOP_PDF_PLACEHOLDER = {
    "ready": True,
    "message": "Hafta 1-9 PDF arsivi yuklendi.",
}
