def NotlariHesapla():
    satir = satir[:-1]
    liste = satir.








def NotlariOku():
    with open("sinav_uygulamalari.txt","r",encoding="utf-8") as file:

        for satir in file:
            print(NotlariHesapla(satir))




def NotlariGir():
    name = input("Ad:")
    surname = input("Soyad:")
    not1 = input("Not1:")
    not2 = input("Not2:")
    not3 = input("Not3:")

    with open("sinav_uygulamalari.txt","a",encoding="utf-8") as file :
        file.write(name+" "+ surname + ":" + not1 + "," + not2 + "," + not3 + "\n")





def NotlariKayitEt():
    pass


while True:
    islem = input("1 - Notları Oku\n2 - Notları Gir\n3 - Notları Kayıt Et\n4 - Çıkış\n?")

    if islem == "1":
        NotlariOku()
    elif islem == "2":
        NotlariGir()
    elif islem == "3":
        NotlariKayitEt()
    else:
        break
