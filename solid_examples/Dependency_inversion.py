# Dependency Inversion — Emir Can BICEN

class Tabanca:
    def ates_et(self):
        print("Tabanca ile ates edildi: BANG!")


class LeonKotu:
    def __init__(self):
        self.silah = Tabanca()

    def saldir(self):
        self.silah.ates_et()


from abc import ABC, abstractmethod


class Silah(ABC):
    @abstractmethod
    def ates_et(self):
        pass


class TabancaGood(Silah):
    def ates_et(self):
        print("Tabanca ile ates edildi: BANG!")


class Shotgun(Silah):
    def ates_et(self):
        print("Shotgun ile ates edildi: BOOM!")


class Requiem(Silah):
    def ates_et(self):
        print("Requiem ile ates edildi: KABOOM!")


class Leon:
    def __init__(self, silah: Silah):
        self.silah = silah

    def saldir(self):
        self.silah.ates_et()
