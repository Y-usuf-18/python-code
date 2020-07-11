ogrenciler = {}

number = input("NO:")
name = input("Öğrenci adı:")
phone = input("Telefon:")

ogrenciler.update({
    number : {
        "ad" : name,
        "telefon" : phone

    }
})
print(ogrenciler)