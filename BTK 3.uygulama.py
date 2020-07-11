# values = 1,2,3,
#
# # print(values)
# # print(type(values))
# x,y,z = values
# print(values)

x , y , z = 2, 5, 10
numbers = 1, 5, 7, 10, 6

# a = int(input("İlk sayıyı girin:"))
# b = int(input("İkinci sayıyı girin:"))
# result = (a * b) - (x + y + z)



# result = (x + y + z) % 3


# result = (y ** x)

# x = int(input("Sayi giriniz:"))
#
# result = ((x > 0) and (x < 100))

# x = int(input("Sayi giriniz: "))
#
# result = (x > 0) and (x % 2 == 0)

email = "yusuf123@gmail.com"
password = "2123"

# x = input("Email giriniz:")
#
# y = input("Password giriniz:")
#
# result = (email == x) and (password == y)

#
# x = float(input("1.sayiyi giriniz:"))
# y = float(input("2.sayiyi giriniz:"))
# z = float(input("3.sayiyi giriniz:"))
#
# result = (x > y > z) or (z > y > x)
#


#EHLİYET ALMA DURUMU

isim = input("İsim Giriniz:")
yas = int(input("Yaş Giriniz:"))
egitim = input("Eğtim Durumu:")

if (yas >= 18):

    if (egitim == "lise") or (egitim == "üniversite"):
        print("{} Ehliyet alabilirsiniz".format(isim))
    else:
        print("{} Ehliyet alamazsıız".format(isim))
else:
    print("Ehliyet alamazsınız")




