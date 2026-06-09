# Open Closed SOLID "O" harfi — Salih KOZA

class ParaTransferi:
    def transfer_yap(self, miktar, yontem):
        if yontem == "havale":
            print(f"{miktar} TL Havale ile ayni bankaya gonderiliyor. Komisyon: 0 TL")
        elif yontem == "eft":
            print(f"{miktar} TL EFT ile farkli bankaya gonderiliyor. Komisyon: 5 TL")
        else:
            raise ValueError("Bilinmeyen transfer yontemi!")


from abc import ABC, abstractmethod


class TransferYontemi(ABC):
    @abstractmethod
    def islem_yap(self, miktar):
        pass


class Havale(TransferYontemi):
    def islem_yap(self, miktar):
        print(f"{miktar} TL Havale ile gonderildi. Komisyon: 0")


class EFT(TransferYontemi):
    def islem_yap(self, miktar):
        print(f"{miktar} TL EFT ile gonderildi. Komisyon: 5 TL")


class TransferMerkezi:
    def transferi_baslat(self, miktar, yontem: TransferYontemi):
        yontem.islem_yap(miktar)
