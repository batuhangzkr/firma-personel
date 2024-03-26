from personel import Personel
from firma import Firma

personel1 = Personel("Ahmet Yılmaz","Muhasebe",5,5000)
personel2 = Personel("Elif Kaya","IT",3,7000)


firma = Firma()

firma.personel_ekle(personel1)
firma.personel_ekle(personel2)

firma.personel_listele()

firma.maas_zammi(personel1,10)

firma.personel_listele()

firma.personel_cikart(personel1)

firma.personel_listele()
