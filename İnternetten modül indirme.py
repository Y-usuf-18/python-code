sayı1 = input("SAYI1:")
sayı2 = input("SAYI2:")

try:
    sayı1 = int(sayı1)
    sayı2 = int(sayı2)

    print(sayı1/sayı2)
except ValueError:
    print("Lütfen sayı giriniz")
except ZeroDivisionError:
 print("Lüfen 0 dan baska bir sayı giriniz")

