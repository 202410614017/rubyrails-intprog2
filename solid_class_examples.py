# -*- coding: utf-8 -*-
"""Sinif arkadaslarinin SOLID odev ornekleri — site gosterimi icin."""

CLASS_EXAMPLES_BY_LETTER = {
    "S": {
        "title": "Makyaj Studyosu — Tek Sorumluluk (SRP)",
        "filename": "solid_examples/single_responsibility.py",
        "author": "Gizem Senol",
        "theme": "Makyaj salonu islemleri",
        "bad_code": """class MakyajStudyosu:
    def __init__(self, musteri_adi, hizmet_turu, ucret):
        self.musteri_adi = musteri_adi
        self.hizmet_turu = hizmet_turu
        self.ucret = ucret

    def makyaj_uygula(self):
        print(f"{self.musteri_adi} — {self.hizmet_turu} makyaji")

    def fircalari_ve_salonu_temizle(self):
        print("Firçalar dezenfekte, salon temizleniyor")

    def fatura_kes(self):
        kdv_dahil = self.ucret * 1.20
        print(f"Fatura: {kdv_dahil} TL")""",
        "bad_why": (
            "Sinifin degismesi icin 3 farkli neden var: makyaj, hijyen, finans. "
            "KDV orani degisirse makyaj koduna dokunmak gerekir — SRP ihlali."
        ),
        "good_code": """class MakyajHizmeti:
    def makyaj_uygula(self): ...

class HijyenYoneticisi:
    def fircalari_temizle(self): ...
    def salonu_temizle(self): ...

class FinansYonetimi:
    @staticmethod
    def fatura_kes(musteri_adi, ucret):
        kdv_dahil = ucret * 1.20
        ...""",
        "good_why": (
            "Her sinif tek is yapar: makyaj, hijyen veya fatura. "
            "Vergi kurali degisince yalnizca FinansYonetimi guncellenir."
        ),
    },
    "O": {
        "title": "Para Transferi — Acik/Kapali (OCP)",
        "filename": "solid_examples/open_closed.py",
        "author": "Salih KOZA",
        "theme": "Banka transfer yontemleri",
        "bad_code": """class ParaTransferi:
    def transfer_yap(self, miktar, yontem):
        if yontem == "havale":
            print(f"{miktar} TL Havale. Komisyon: 0")
        elif yontem == "eft":
            print(f"{miktar} TL EFT. Komisyon: 5")
        else:
            raise ValueError("Bilinmeyen yontem!")""",
        "bad_why": (
            "SWIFT veya kripto eklemek icin sinifi acip yeni elif yazmak gerekir. "
            "Calisan havale/EFT kodu risk altinda — OCP ihlali, if/elif spagetti."
        ),
        "good_code": """class TransferYontemi(ABC):
    @abstractmethod
    def islem_yap(self, miktar): pass

class Havale(TransferYontemi):
    def islem_yap(self, miktar): ...

class EFT(TransferYontemi):
    def islem_yap(self, miktar): ...

class TransferMerkezi:
    def transferi_baslat(self, miktar, yontem: TransferYontemi):
        yontem.islem_yap(miktar)  # if/elif yok!""",
        "good_why": (
            "TransferMerkezi degismez; yeni yontem icin sadece yeni sinif eklenir "
            "(ornegin class SwiftTransfer). Mevcut kod kapali, genisleme acik — OCP uygun."
        ),
    },
    "L": {
        "title": "Solo Leveling Avci — Liskov (LSP)",
        "filename": "solid_examples/liskov.py",
        "author": "Muhammed Hamza Erhan",
        "theme": "Solo Leveling / Hunter hiyerarsisi",
        "bad_code": """class Avci_Kotu:
    def guc_artir(self, miktar):
        self.guc += miktar
    def zeka_artir(self, miktar):
        self.zeka += miktar

class YanlisPlayer(Avci_Kotu):
    def guc_artir(self, miktar):
        self.guc += miktar
        self.zeka += miktar  # beklenmeyen!

def stat_test_et(avci):
    avci.guc_artir(10); avci.zeka_artir(5)
    # Beklenen: guc=20, zeka=15
    # YanlisPlayer → zeka=20 → KALDI""",
        "bad_why": (
            "Avci'da guc ve zeka bagimsiz artar. YanlisPlayer guc artirinca zeka da artar; "
            "stat_test_et patlar. Alt sinif ust sinifin yerine konulamaz — LSP ihlali."
        ),
        "good_code": """class Hunter(ABC):
    @abstractmethod
    def dungeon_temizle(self, seviye: int) -> bool: pass
    @abstractmethod
    def skill_kullan(self) -> str: pass

class ERankHunter(Hunter): ...
class SungJinwoo(Hunter): ...

def baskani_hazirla(hunter: Hunter, seviye: int):
    if hunter.dungeon_temizle(seviye):
        print(hunter.skill_kullan())
# Hangi hunter gelirse gelsin calisir""",
        "good_why": (
            "Her Hunter bool/str sozlesmesine uyar. SungJinwoo ekstra ozellik ekler "
            "ama sozlesmeyi bozmaz. Detay: asagidaki LSP Solo Leveling paneli."
        ),
        "extra_link": "#lsp-solo-leveling",
    },
    "I": {
        "title": "Hayvan Arayuzleri — Arayuz Ayirimi (ISP)",
        "filename": "solid_examples/Interface_segration.py",
        "author": "Hilmi Arda Dagci",
        "theme": "Kartal, kopek, kedi davranislari",
        "bad_code": """class Animal(ABC):
    @abstractmethod
    def eat(self): pass
    @abstractmethod
    def fly(self): pass
    @abstractmethod
    def swim(self): pass

class Eagle(Animal):
    def eat(self): ...
    def fly(self): ...
    def swim(self): pass  # Kartal yuzmez!

class Dog(Animal):
    def eat(self): ...
    def fly(self): pass   # Kopek ucamaz!
    def swim(self): ...""",
        "bad_why": (
            "Eagle, Dog ve Cat kullanmadigi fly/swim metotlarini bos implement etmek zorunda. "
            "Siskin arayuz gereksiz kod ve hata riski — ISP ihlali."
        ),
        "good_code": """class Eatable(ABC):
    @abstractmethod
    def eat(self): pass

class Flyable(ABC):
    @abstractmethod
    def fly(self): pass

class Swimmable(ABC):
    @abstractmethod
    def swim(self): pass

class Eagle(Eatable, Flyable): ...
class Dog(Eatable, Swimmable): ...
class Cat(Eatable): ...""",
        "good_why": (
            "Her sinif yalnizca ihtiyaci olan kucuk arayuzu alir. "
            "Kedi yuzme/uçma metodu yazmak zorunda kalmaz — ISP uygun."
        ),
    },
    "D": {
        "title": "Leon & Silah — Bagimlilik Tersine Cevirme (DIP)",
        "filename": "solid_examples/Dependency_inversion.py",
        "author": "Emir Can BICEN",
        "theme": "Resident Evil — Leon silah secimi",
        "bad_code": """class Tabanca:
    def ates_et(self):
        print("BANG!")

class Leon:
    def __init__(self):
        self.silah = Tabanca()  # somut sinifa bagimli

    def saldir(self):
        self.silah.ates_et()""",
        "bad_why": (
            "Leon yalnizca Tabanca kullanabilir. Shotgun veya Requiem eklemek icin "
            "Leon sinifini degistirmek gerekir — ust seviye alt seviyeye bagimli, DIP ihlali."
        ),
        "good_code": """class Silah(ABC):
    @abstractmethod
    def ates_et(self): pass

class Tabanca(Silah): ...
class Shotgun(Silah): ...
class Requiem(Silah): ...

class Leon:
    def __init__(self, silah: Silah):
        self.silah = silah  # disaridan enjekte

leon_boss = Leon(Requiem())
leon_boss.saldir()""",
        "good_why": (
            "Leon somut silahi bilmez; Silah soyutlamasina bagimlidir. "
            "Yeni silah = yeni sinif, Leon degismez — Dependency Injection ile DIP uygun."
        ),
    },
}
