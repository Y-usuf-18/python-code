faktöriyel=1

while True:
    sayi=int(input("Lütfen bir sayı giriniz:"))
    if sayi <= 0:
        print("pozitif giriniz")
    else:
        for i in range(1,sayi+1):
            faktöriyel*=i
            print("Faktöriyel:",faktöriyel)
            break


