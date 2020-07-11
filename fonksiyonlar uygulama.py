# def sayHELLO(name):
    # print("Hello "+ name)

# sayHELLO("Çınar")

#
# def yashesapla(dogumyili):
#     return 2020 - dogumyili

# a = yashesapla(2010)
# print(a)
#
# def emeklilikyasi(dogumyili,isim):
#     yas = yashesapla(dogumyili)
#     emeklilik = 65 - yas
#
#     if (emeklilik > 0):
#         print(f"emekliliğinize {emeklilik} yıl kaldı")
#
#     else:
#         print("Zaten emeklisiniz")
#
# emeklilikyasi(1970,"Ali")

# def add(*params):
#     return sum((params))
# print(add(10,20))
# print(add(10,20,30))

# def displayuser(**paramss):
#     for key,value in paramss.items():
#         print("{} is {}".format(key,value))




# displayuser(name = "Çınar",age = 15,phone = "1241324")
# displayuser(name = "Taner",age = 32,city = "İstanbul")
# displayuser(name = "Ada",age = 44,city = "Miami")

#
# def repeatword(kelime,adet):
#     print(kelime * adet)
# repeatword("Merhaba\n",10)


# def parame(*params):
#     lise = []
#     for param in params:
#         lise.append(param)
#         print(lise)

# parame(12,3,45,67,89)




# def asalsayi(sayi1,sayi2):
#
#     for sayi in range(sayi1,sayi2 + 1):
#         if (sayi > 1):
#             for i in range(2,sayi):
#                 if (sayi % i == 0 ):
#                     break
#                 else:
#                     print(sayi)
# asalsayi(5,17)


#
# def tambolenleriBul(sayi):
#     tambolenler = []
#     for i in range(2,sayi):
#         if (sayi % i == 0 ):
#             tambolenler.append(i)
#             print(tambolenler)
#
# tambolenleriBul(
#     20
# )

# def square(num):
#     return num ** 2

 # numbers = [1,2,4,6,8]
# square = lambda num : num ** 2
#
# result =list(map(square,numbers))
#
# print(result)

# def check_even(num):
#     return num % 2 == 0
#
# result = list(filter(lambda num : num % 2 == 0,numbers)

# Bankamatik Uygulama




SadikHesap = {
    "ad": "Sadık",
    "hesapno": 131321,
    "bakiye": 3000,
    "ekhesap": 2000

}

AliHesap = {
    "ad": "Ali",
    "hesapno": 121421,
    "bakiye": 2000,
    "ekhesap": 1000

}

def paracek(hesap,miktar):
    print(f"Merhaba {hesap['ad']} Bey")

    if hesap["bakiye"] > miktar:
        print("Paranızı Alabilirsiniz")

    else:
        toplam = hesap["bakiye"] + hesap["ekhesap"]

        if (toplam > miktar):
            ekhesapkullanimi= input("Ek Hesap kullanmak ister misniz? e/h ")
            if (ekhesapkullanimi == "e"):
                print("Paranınzı alabilrisiniz")
            else:
                print(f"{hesap['hesapno']} nolu hesabınızda {hesap['bakiye']} TL vardır.")

        else:
            print("Bakiye yetersiz")

paracek(AliHesap,2300)


