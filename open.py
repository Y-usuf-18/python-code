with open("yazılım.txt","r+") as dosya:
    data = dosya.readlines()
    data.insert(1,"787656\n")
    dosya.seek(0)
    dosya.writelines(data)

