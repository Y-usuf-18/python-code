# import datetime
# simdi = datetime.datetime.now()
# result = simdi + datetime.timedelta(days=10)
#
# print(result)
import os
# result = os.name
# os.chdir(".. / ..")

# klasör yeri öğrenme
# result = os.getcwd()

# klasör oluşturma
# os.mkdir("New directory")
# os.rename("New directory","yeniklasör")

# listeleme
# result = os.listdir()
# for dosya in os.listdir():
#     if dosya.endswitch(".py"):
#         print(dosya)
# import datetime
# result = os.stat("Alan.py")
# result = datetime.datetime.fromtimestamp(1588628544)
# os.system("notepad.exe")
# # path
# result = os.path.abspath("Alan.py")
# result = os.path.exists("Alan.py")

import re
# result = dir(re)
# re module
str = "Python kursu için Python kursu izleyin"
# re.findall
# result = re.findall("Python",str)
# result = len(result)

# re.split
# result = re.split(" ",str)
# result = re.split("P",str)

# re.sub
# result = re.sub(" ","-",str)

# re.search

# result = re.search("Python",str)
# result = result.span()
# result = result.string
# result = result.start()
# result = result.end()




# regular expression



import json

# person_string = '{"name":"Ayaz","languages":["python","C#"]}'

# result = json.loads(person_string)
# result = result["name"]
# result = person_string["languages"]
#
# with open("person") as p:
#     data = json.load(p)
#
#
#
# print(data["languages"])

# person_dictionary = {
#     "name":"Ali",
#     "languages":["Pythn","C#"]
#
# }
# data = json.dumps(person_dictionary)
# # print(data)
# # print(type(data))
#
# with open("person","w") as f:
#     json.dump(person_dictionary,f
#               )
# UYGULAMA DEMO JSON

# class User:
#     def __init__(self,username,password,email):
#         self.username = username
#         self.password = password
#         self.email = email
#
#
# class UserRepository:
#     def register(self):
#         pass
#     def login(self):
#         pass
#     def SaveToFile(self):
#         pass
#
# while True:
#     print("Menü".center(50,"*"))
#     secim = input("1-Register\n2-Login\n3-Logout\n4-Identity\n5-Exit\nseciminiz:")
#     if secim == "5":
#         break
#
#     else:
#         if secim == "1":
#             pass
#         elif secim == "2":
#             pass
#         elif secim == "3":
#             pass
#         elif secim == "4":
#             pass
#         else:
#             print("Yanlış Seçim")





# Request
import requests
import json
# result = requests.get("https://pypi.org/project/requests/")
# result = result.text
#
# print(type(result))

# api_url = "https://api.exchangeratesapi.io/latest?base="
#
# bozulan_tur = input("Hangi tür para bozdurmak istersiniz?: ")
# cevrilcek_tur = input("Alınan para tür?: ")
# miktar = int(input("Miktar yazın: "))
#
# result = requests.get(api_url+bozulan_tur)
# result = json.loads(result.text)
#
#
# print("1 {0} = {1} {2} ".format(bozulan_tur,result["rates"][cevrilcek_tur],cevrilcek_tur) )
# print("{0} {1} = {2} {3}".format(miktar,bozulan_tur,miktar * result["rates"][cevrilcek_tur],cevrilcek_tur))
#
# html_doc = """

# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Ana Sayfa</title>
# </head>
# <body>
#     <div class = group 1>
#
#         <h1>
#             Title
#         </h1>
#         <ul>
#             <li>Menü 1</li>
#             <li>Menü 2</li>
#             <li>Menü 3</li>
#         </ul>
#     </div>
#
#
#
#
# </body>
# </html>
# """
#
# from bs4 import BeautifulSoup
#
# soup = BeautifulSoup(html_doc,"html.parser")
# result = soup.prettify()
# result = soup.title
# result = soup.head
# result = soup.body
# result = soup.title.string
# result = soup.h1
# result = soup.h2
# result = soup.find_all("h1")
# result = soup.div
#
# print(result)

import requests
from bs4 import BeautifulSoup
url = "https://m.imdb.com/chart/top"

html = requests.get(url).content
soup = BeautifulSoup(html,"html parser")
list = soup.find("div",{"class":"lister - list"})



print(list)


