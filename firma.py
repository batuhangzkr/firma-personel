from personel import Personel

class Firma:
    def __init__(self):
        self.personel_listesi = []

    def personel_ekle(self,personel):
        self.personel_listesi.append(personel)

    def personel_listele(self):
        for personel in self.personel_listesi:
            print(personel)

    def maas_zammi(self,personel,zam_orani):
        for p in self.personel_listesi:
            if p == personel:
                p.maas += p.maas * zam_orani / 100

    def personel_cikart(self,personel):
        self.personel_listesi.remove(personel)