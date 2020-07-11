import random
class Dusman:

    def __init__(self,isim = "Dusman",kalan_can = 500,saldiri_gucu = 10,mermi_sayisi = 5):

        self.isim = isim
        self.kalan_can = kalan_can
        self.saldiri_gucu = saldiri_gucu
        self.mermi_sayisi = mermi_sayisi

    def saldir(self):

        print(self.isim + "SALDIRIYOR.")
        harcananmermi = random.randrange(0,10)
        print(str(harcananmermi) + "kadar harcandı")
        self.mermi_sayisi -= harcananmermi

        return(harcananmermi,self.saldiri_gucu)

    def saldırıya_ugra(self,harcananmermi,saldiri_gucu):
        print("Vruldum")
        self.kalan_can -= (harcananmermi * saldiri_gucu)

    def mermi_bittimi(self):
        if (self.mermi_sayisi <= 0 ):
            print("Mermim biti,Cıkıyorum")
            return True
        return False

    def hayatta_mi(self):
        if (self.kalan_can <= 0 ):
            print("Ölüyorumm")

    def print(self):
        print("Basılıyor")
        print("isim:",self.isim,"kalan can:",self.kalan_can,"saldırı gucu:",self.saldiri_gucu,"mermi sayısı:",self.mermi_sayisi)

dusmanlar = []


i = 0
while(i < 10):
    rastgelecan = random.randrange(100,200)
    rastgelesaldırıgucu = random.randrange(10,20)
    ratgelemermi = random.randrange(20,30)
    yenıdusman = Dusman("Dusman" +str(i + 1),rastgelecan,rastgelesaldırıgucu,ratgelemermi)
    dusmanlar.append(yenıdusman)

    i += 1

for dusman in dusmanlar:
    dusman.print()










