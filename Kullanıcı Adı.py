#Kullanıcı Adı Ve Parola Programı
defkullanıcı="yazılım123"
defparola="asdf"

kullanıcı=input("Kullanıcı Adı:")
parola=input("Parola:")



if ((defkullanıcı==kullanıcı) and (defparola==parola)):
    print("Web Sitesine Hosgeldiniz")

elif ((defkullanıcı!=kullanıcı) and (defparola==parola)):
    print("Kullanıcı Adı Yanlış!!")
elif ((defkullanıcı==kullanıcı) and (defparola!=parola)):
    print("Parola Yanlıs !!")
else:
    print("Tekrar Deneyiniz!!")


