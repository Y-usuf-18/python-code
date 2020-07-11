defkullanıcıadı="root"
defparola="root"
while(True):

    kullanıcı=input("Kullanıcı Adı:")
    parola=input("Parola:")

   if
       
        ((kullanıcı==defkullanıcıadı) and (defparola==parola)):

        break



    elif
        ((kullanıcı!=defkullanıcıadı) and (defparola==parola)):
        print("Kullanıcı Adını Yanlış Girdiniz")

    elif
        ((kullanıcı==defkullanıcıadı) and (defparola!=parola)):

        print("Şifrenizi Yanlış Girdiniz")
        print("Şifrenizi Değiştirmek İster misiniz?(E/H)")
        cevap=input()

        if
            (cevap=="E")

        yeniparola=input("Yeni Parola:")
        print("BİRAZ BEKLE")
        defparola=yeniparola
        print("Şifreniz Değiştirildi")

        else
            print("Tekrar Deneyin")



