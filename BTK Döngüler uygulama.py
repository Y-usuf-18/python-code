# numbers = [1,2,3,4,5]
# for i in numbers:
#     print(i)

# names = ["çınar","can","sena"]

# for i in names:
    # print(f"my name is {i}")

# sayilar =  [1,3,5,7,9,12,19,21]

# toplam = 0
# for sayi in sayilar:
#     toplam += sayi
#     print("toplam:",toplam)

# for i in sayilar:
#
#     if (i % 2 == 1):
#
#         a = i ** 2
#         print(a)

# x = 0
#
# while x < 100 :
#     x += 1
#     print(x)

# sayilar = [1,3,5,7,9,12,15,17,20]

# i = 0
# while (i < len(sayilar)):

    # print(sayilar[i])

    # i += 1

# i = 100
# while (i > 0):
#     print(i)
#     i -= 1

# numbers = []
# i = 0
# while (i < 5):
#     sayi = int(input("Sayı Girin:"))
#     numbers.append(sayi)
#     i += 1
# numbers.sort()
# print(numbers)

#
# a = "Hello"
#
# for letter in enumerate(a):
#     print(letter)

# for x in range(10):
#     print(x**2)
#
# numbers = [x**2 for x in range(10)]
# print(numbers)

# results = [x if x%2==0 else "TEK" for x in range(1,10)]
# print(results)



# import random
#
# sayi = random.randint(1,100)
# hak = 5
# sayac = 0
#
# while (hak > 0 ):
#     hak -= 1
#     tahmin = int(input("Tahmin edin:"))
#     sayac += 1
#     if (tahmin == sayi):
#         print(f"Tebrikler {sayac}.defada bildiniz.Toplam puanınız {100 - (20) * (sayac)}")
#         break
#     elif (tahmin < sayi):
#         print("Yukarı")
#     elif (tahmin > sayi):
#         print("Aşağı")
#
#     if hak == 0 :
#         print(f"Hakkınız bitti.Tutulan sayi: {sayi}.Puanınız {100 -(20) * (sayac)} ")


sayi = int(input("Sayı Giriniz:"))
asalmi= True

if (sayi == 1):
    print("Asal değil")

for i in range(2,sayi):
    if (sayi % i == 0):
        asalmi = False
        break

if asalmi:
        print("sayı asaldır")

else:
        print("sayı asal değildir")
