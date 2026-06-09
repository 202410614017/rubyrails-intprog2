# -*- coding: utf-8 -*-
"""Hafta 9 SOLID alistirmalari — PDF + kullanici ornekleri, cozumlu."""

WEEK9_EXERCISES = [
    {
        "id": "ocp-alan-hesaplayici",
        "principle": "O",
        "title": "Open/Closed — AlanHesaplayici",
        "week": 9,
        "gist": "https://gist.github.com/ecmelkytz/f3290c0269b51c66e79f2dc6529457e9",
        "problem": (
            "Yeni sekil eklendiginde AlanHesaplayici icindeki if/elif blogu degismek zorunda. "
            "Mevcut kod her yeni sekilde kirilganlasir."
        ),
        "bad_code": """class AlanHesaplayici:
    def alan_hesapla(self, sekil_tipi, *args):
        if sekil_tipi == "daire":
            yaricap = args[0]
            return 3.14159 * yaricap * yaricap
        elif sekil_tipi == "kare":
            kenar = args[0]
            return kenar * kenar
        elif sekil_tipi == "dikdortgen":
            return args[0] * args[1]
        elif sekil_tipi == "ucgen":
            return (args[0] * args[1]) / 2
        else:
            raise ValueError(f"Bilinmeyen sekil: {sekil_tipi}")""",
        "bad_why": (
            "Her yeni sekil (elips, yamuk) icin alan_hesapla metoduna elif eklenmeli. "
            "Sinif degisiklige kapali degil, genislemeye kapali — OCP ihlali."
        ),
        "good_code": """from abc import ABC, abstractmethod

class Sekil(ABC):
    @abstractmethod
    def alan(self):
        pass

class Daire(Sekil):
    def __init__(self, yaricap):
        self.yaricap = yaricap
    def alan(self):
        return 3.14159 * self.yaricap ** 2

class Dikdortgen(Sekil):
    def __init__(self, u, g):
        self.u, self.g = u, g
    def alan(self):
        return self.u * self.g

class AlanHesaplayici:
    def alan_hesapla(self, sekil: Sekil):
        return sekil.alan()  # yeni sekil = yeni sinif, bu sinif degismez""",
        "good_why": (
            "AlanHesaplayici artik sekil tipini bilmez; alan() metoduna sahip her nesne calisir. "
            "Elips eklemek icin sadece Elips(Sekil) yazilir — mevcut kod degismez. OCP'ye uygun."
        ),
    },
    {
        "id": "lsp-dosya",
        "principle": "L",
        "title": "Liskov Substitution — Dosya Sistemi",
        "week": 9,
        "gist": "https://gist.github.com/ecmelkytz/49596f9fb8b61d0af0e64155edd2dacba",
        "problem": (
            "SaltOkunurDosya ve GeciciDosya, Dosya yerine konuldugunda yaz/sil cagrisi patlar. "
            "dosya_islemleri(Dosya) guvenle calismiyor."
        ),
        "bad_code": """class Dosya:
    def oku(self):
        return f"{self.ad} okundu"
    def yaz(self, veri):
        return f"{self.ad} yazildi"
    def sil(self):
        return "silindi"

class SaltOkunurDosya(Dosya):
    def yaz(self, veri):
        raise PermissionError("Salt okunur!")
    def sil(self):
        raise PermissionError("Silinemez!")

def dosya_islemleri(dosya: Dosya):
    print(dosya.oku())
    print(dosya.yaz("Merhaba"))  # SaltOkunur'da patlar!
    print(dosya.sil())""",
        "bad_why": (
            "Ust sinif Dosya yaz/sil vaat ediyor ama alt siniflar bozuyor. "
            "Dosya yerine SaltOkunurDosya konunca program kirilir — LSP ihlali."
        ),
        "good_code": """from abc import ABC, abstractmethod

class Okunabilir(ABC):
    @abstractmethod
    def oku(self): pass

class Yazilabilir(ABC):
    @abstractmethod
    def yaz(self, veri): pass

class Silinebilir(ABC):
    @abstractmethod
    def sil(self): pass

class NormalDosya(Okunabilir, Yazilabilir, Silinebilir):
    def oku(self): return "okundu"
    def yaz(self, v): return "yazildi"
    def sil(self): return "silindi"

class SaltOkunurDosya(Okunabilir):
    def oku(self): return "okundu"

def oku_ve_yaz(obj: Yazilabilir, veri):
    if isinstance(obj, Okunabilir):
        print(obj.oku())
    obj.yaz(veri)  # sadece Yazilabilir nesnelerle cagir""",
        "good_why": (
            "Yeteneklere gore kucuk arayuzler: Okunabilir, Yazilabilir, Silinebilir. "
            "SaltOkunur sadece Okunabilir — yaz cagrisi zorlanmaz. LSP'ye uygun."
        ),
    },
    {
        "id": "isp-cihaz",
        "principle": "I",
        "title": "Interface Segregation — Akilli Ev Cihazlari",
        "week": 9,
        "gist": "https://gist.github.com/ecmelkytz/ec49ef94dce542dd661544e3a618dca0",
        "problem": (
            "Tek buyuk Cihaz ABC'si tum metotlari zorunlu kiliyor. Ampul video_kaydet icin "
            "NotImplementedError firlatiyor — kullanilmayan arayuze bagimli."
        ),
        "bad_code": """class Cihaz(ABC):
    @abstractmethod
    def ac(self): pass
    @abstractmethod
    def kapat(self): pass
    @abstractmethod
    def sicaklik_ayarla(self, d): pass
    @abstractmethod
    def video_kaydet(self): pass
    @abstractmethod
    def hareket_algila(self): pass

class Ampul(Cihaz):
    def ac(self): print("Acildi")
    def kapat(self): print("Kapandi")
    def sicaklik_ayarla(self, d):
        raise NotImplementedError("Ampul sicaklik ayarlayamaz")
    def video_kaydet(self):
        raise NotImplementedError()
    def hareket_algila(self):
        raise NotImplementedError()""",
        "bad_why": (
            "Ampul kullanmadigi 3 metodu bos/raise ile implement etmek zorunda. "
            "Buyuk arayuz gereksiz bagimlilik — ISP ihlali."
        ),
        "good_code": """class Acilabilir(ABC):
    @abstractmethod
    def ac(self): pass
    @abstractmethod
    def kapat(self): pass

class SicaklikAyarlanabilir(ABC):
    @abstractmethod
    def sicaklik_ayarla(self, d): pass

class GuvenlikCihazi(ABC):
    @abstractmethod
    def video_kaydet(self): pass
    @abstractmethod
    def hareket_algila(self): pass

class Ampul(Acilabilir):
    def ac(self): print("Ampul acildi")
    def kapat(self): print("Ampul kapandi")

class Termostat(Acilabilir, SicaklikAyarlanabilir):
    def ac(self): pass
    def kapat(self): pass
    def sicaklik_ayarla(self, d): print(f"{d} derece")""",
        "good_why": (
            "Her cihaz sadece ihtiyaci olan arayuzleri implement eder. "
            "Ampul sadece Acilabilir — gereksiz metot yok. ISP'ye uygun."
        ),
    },
    {
        "id": "dip-bildirim",
        "principle": "D",
        "title": "Dependency Inversion — Bildirim Sistemi",
        "week": 9,
        "gist": "https://gist.github.com/ecmelkytz/d12748bb40cb30421978119fabe9eda4",
        "problem": (
            "NotificationManager dogrudan EmailService, SMSService somut siniflarina bagli. "
            "Yeni kanal eklemek veya test icin mock kullanmak zor."
        ),
        "bad_code": """class EmailService:
    def send_email(self, message):
        print(f"Email: {message}")

class NotificationManager:
    def __init__(self):
        self.email = EmailService()
        self.sms = SMSService()

    def send(self, message, channel):
        if channel == "email":
            self.email.send_email(message)
        elif channel == "sms":
            self.sms.send_sms(message)""",
        "bad_why": (
            "Ust seviye NotificationManager alt seviye somut siniflara bagimli. "
            "Email servisi degisince manager degismek zorunda — DIP ihlali."
        ),
        "good_code": """from abc import ABC, abstractmethod

class BildirimKanali(ABC):
    @abstractmethod
    def gonder(self, mesaj: str):
        pass

class EmailKanali(BildirimKanali):
    def gonder(self, mesaj):
        print(f"Email: {mesaj}")

class NotificationManager:
    def __init__(self, kanallar: dict):
        self.kanallar = kanallar  # enjekte edilen soyut bagimlilik

    def send(self, mesaj, channel):
        self.kanallar[channel].gonder(mesaj)""",
        "good_why": (
            "Manager somut siniflari bilmez; BildirimKanali soyutlamasina bagimlidir. "
            "Testte sahte kanal enjekte edilebilir. DIP'ye uygun."
        ),
    },
]
