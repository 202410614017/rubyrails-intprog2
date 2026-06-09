# Liskov Substitution Principle — Solo Leveling — Muhammed Hamza Erhan

from abc import ABC, abstractmethod


class Avci_Kotu:
    def __init__(self, guc: int, zeka: int):
        self.guc = guc
        self.zeka = zeka

    def guc_artir(self, miktar: int):
        self.guc += miktar

    def zeka_artir(self, miktar: int):
        self.zeka += miktar


class YanlisPlayer(Avci_Kotu):
    def guc_artir(self, miktar: int):
        self.guc += miktar
        self.zeka += miktar  # BEKLENMEDIK! LSP IHLALI


def stat_test_et(avci: Avci_Kotu):
    avci.guc_artir(10)
    avci.zeka_artir(5)
    print(f"  Guc: {avci.guc} | Zeka: {avci.zeka}", end="  ")
    if avci.guc == 20 and avci.zeka == 15:
        print("-> GECTI")
    else:
        print("-> KALDI (LSP IHLALI)")


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
            print(f"  {self.isim}: Bu dungeon cok guclu, giremem.")
            return False
        print(f"  {self.isim}: E-rank dungeon temizlendi!")
        return True

    def skill_kullan(self) -> str:
        return f"{self.isim} temel saldiri kullandi."


class SungJinwoo(Hunter):
    def __init__(self):
        super().__init__("Sung Jinwoo", "Ozel", guc=999, zeka=999)
        self.golge_sayisi = 0

    def dungeon_temizle(self, seviye: int) -> bool:
        self.golge_sayisi += 1
        print(f"  {self.isim}: S-rank dungeon saniyede temizlendi. Golge ordusu: {self.golge_sayisi}")
        return True

    def skill_kullan(self) -> str:
        return f"{self.isim} Arise kullandi. Herkes golge oldu."


def baskani_hazirla(hunter: Hunter, dungeon_seviyesi: int):
    sonuc = hunter.dungeon_temizle(dungeon_seviyesi)
    if sonuc:
        print(f"  Skill: {hunter.skill_kullan()}")
