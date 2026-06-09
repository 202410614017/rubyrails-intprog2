# Single Responsibility — Gizem Senol
class MakyajStudyosu:
    # KOTU: Bu sinif hem musteri bilgisini tutuyor, hem makyaj yapiyor,
    # hem temizlik islerinden sorumlu hem de fatura kesiyor.
    def __init__(self, musteri_adi, hizmet_turu, ucret):
        self.musteri_adi = musteri_adi
        self.hizmet_turu = hizmet_turu
        self.ucret = ucret

    def makyaj_uygula(self):
        print(f"{self.musteri_adi} isimli musteriye {self.hizmet_turu} makyaji uygulanmaktadir.")

    def fircalari_ve_salonu_temizle(self):
        print("Kullanilan firçalar dezenfekte edilmekte ve salon temizlenmektedir.")

    def fatura_kes(self):
        kdv_dahil = self.ucret * 1.20
        print(f"Fatura Kesildi: {self.musteri_adi} - Toplam Tutar (KDV Dahil): {kdv_dahil} TL")


class MakyajHizmeti:
    def __init__(self, musteri_adi, hizmet_turu):
        self.musteri_adi = musteri_adi
        self.hizmet_turu = hizmet_turu

    def makyaj_uygula(self):
        print(f"{self.musteri_adi} isimli musteriye {self.hizmet_turu} makyaji uygulanmaktadir.")


class HijyenYoneticisi:
    def fircalari_temizle(self):
        print("Kullanilan makyaj firçalari dezenfekte edilmistir.")

    def salonu_temizle(self):
        print("Makyaj masasi bir sonraki musteri icin temizlenmistir.")


class FinansYonetimi:
    @staticmethod
    def fatura_kes(musteri_adi, ucret):
        kdv_dahil = ucret * 1.20
        print(f"Fatura Kesildi: {musteri_adi} - Toplam Tutar (KDV Dahil): {kdv_dahil} TL")
