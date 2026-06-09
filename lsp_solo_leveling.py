# -*- coding: utf-8 -*-
"""
Liskov Yerine Gecme Prensibi (LSP) — Solo Leveling ornekleri.
Kaynak calisma: Muhammed Hamza Erha (sinif arkadas ornegi, siteye uyarlandi).
"""

CREDIT = "Ornek calisma: Muhammed Hamza Erha — Solo Leveling temasiyla LSP aciklamasi"

LSP_INTRO = {
    "title": "Liskov Yerine Gecme Prensibi (LSP)",
    "subtitle": "Solo Leveling Ornekleriyle",
    "what": (
        "Alt sinif, ust sinifin YERINE GECEBILMELI. Gecince program BOZULMAMALI."
    ),
    "short": (
        "Sung Jinwoo da bir Avci. Jinwoo'yu Avci yerine koyunca program calisiyor mu? "
        "Calisiyorsa LSP tamam, bozulduysa LSP ihlali."
    ),
}

BAD_CODE = """class Avci_Kotu:
    def __init__(self, guc: int, zeka: int):
        self.guc = guc
        self.zeka = zeka

    def guc_artir(self, miktar: int):
        self.guc += miktar       # sadece gucu arttirir

    def zeka_artir(self, miktar: int):
        self.zeka += miktar      # sadece zekayi arttirir


class YanlisPlayer(Avci_Kotu):
    def guc_artir(self, miktar: int):
        self.guc += miktar
        self.zeka += miktar      # BEKLENMEDIK! Avci bunu yapmiyor


def stat_test_et(avci: Avci_Kotu):
    avci.guc_artir(10)
    avci.zeka_artir(5)
    # Beklenen: guc=20, zeka=15
    if avci.guc == 20 and avci.zeka == 15:
        print("GECTI")
    else:
        print("KALDI (LSP IHLALI)")

stat_test_et(Avci_Kotu(10, 10))      # GECTI
stat_test_et(YanlisPlayer(10, 10))  # zeka=20 → KALDI"""

BAD_WHY = (
    "Avci sinifinda guc_artir ve zeka_artir bagimsizdir. YanlisPlayer guc artirinca "
    "zeka da artiyor — ust sinifi bekleyen stat_test_et patlar (guc=20, zeka=20 olur). "
    "Alt sinif ust sinifin yerine konuldugunda program bozuluyor → LSP ihlali."
)

GOOD_CODE = """from abc import ABC, abstractmethod

class Hunter(ABC):
    def __init__(self, isim: str, rank: str, guc: int, zeka: int):
        self.isim = isim
        self.rank = rank
        self.guc = guc
        self.zeka = zeka

    @abstractmethod
    def dungeon_temizle(self, seviye: int) -> bool:
        pass

    @abstractmethod
    def skill_kullan(self) -> str:
        pass


class ERankHunter(Hunter):
    def dungeon_temizle(self, seviye: int) -> bool:
        if seviye > 2:
            return False
        return True

    def skill_kullan(self) -> str:
        return f"{self.isim} temel saldiri kullandi."


class SungJinwoo(Hunter):
    def __init__(self):
        super().__init__("Sung Jinwoo", "Ozel", guc=999, zeka=999)
        self.golge_sayisi = 0

    def dungeon_temizle(self, seviye: int) -> bool:
        self.golge_sayisi += 1
        return True  # sozlesme bozulmadi: bool donuyor

    def skill_kullan(self) -> str:
        return f"{self.isim} Arise kullandi."


def baskani_hazirla(hunter: Hunter, dungeon_seviyesi: int):
    if hunter.dungeon_temizle(dungeon_seviyesi):
        print(hunter.skill_kullan())

# Hangi hunter gelirse gelsin calisir — LSP TAMAM
baskani_hazirla(ERankHunter("Jinwoo", "E", 10, 10), 1)
baskani_hazirla(SungJinwoo(), 10)"""

GOOD_WHY = (
    "Her Hunter tipi soyut siniftan kalitim alir ve dungeon_temizle → bool, "
    "skill_kullan → str sozlesmesine uyar. SungJinwoo ekstra ozellik (golge_sayisi) "
    "ekler ama sozlesmeyi bozmaz. baskani_hazirla(hunter) hangi alt sinif gelirse gelsin calisir."
)

LSP_FIVE_RULES = [
    {
        "num": 1,
        "name": "On Kosul",
        "rule": "Alt sinif daha kati sart koyamaz.",
        "example": (
            "Normal Avci her seviye dungeona girebilir beklenir. ERankAvci seviye 2'den "
            "yuksek dungeon'i reddederse, ust sinifi kullanan kod seviye 5 verdiginde program patlar."
        ),
    },
    {
        "num": 2,
        "name": "Son Kosul",
        "rule": "Alt sinif daha az garanti veremez.",
        "example": (
            "Dungeon temizlenince en az 1 item dusmeli. Jinwoo 'item dusmedi, sadece golge aldim' "
            "derse loot bekleyen sistem patlar."
        ),
    },
    {
        "num": 3,
        "name": "Degismez (Invariant)",
        "rule": "Ust sinifin ic kurallari alt sinifta bozulmamali.",
        "example": (
            "toplam_stat = guc + zeka + dayaniklilik kurali varsa Jinwoo guc artirinca "
            "toplam_stat guncellenmezse sistem yanlis deger gosterir."
        ),
    },
    {
        "num": 4,
        "name": "Istisna",
        "rule": "Alt sinif yeni beklenmedik hata firlatamaz.",
        "example": (
            "Gate kapaninca GateKapandiHatasi firlatilir. Jinwoo MonarkUyandiHatasi firlatirsa "
            "kimse yakalamaz, sistem coker."
        ),
    },
    {
        "num": 5,
        "name": "Donus Tipi",
        "rule": "Alt sinif farkli tip donduremez.",
        "example": (
            "skill_kullan() her zaman str dondurmeli. None veya int dondururse .upper() cagrisi patlar."
        ),
    },
]
