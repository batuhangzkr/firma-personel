class Personel:
    def __init__(self,ad,departman,calisma_yili,maas):
        self.ad = ad
        self.departman = departman
        self.calisma_yili = calisma_yili
        self.maas = maas

    def __str__(self):
        return f"Adı:{self.ad},Departmanı:{self.departman},Çalışma Yılı:{self.calisma_yili},Maaşı:{self.maas}"
