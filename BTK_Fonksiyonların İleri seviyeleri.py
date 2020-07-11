#
# name = input("name?")
# def names(name):
#     print("Hello "+ name)
#
# names(name)

# def factoriel(number):
    #
    # def inner_factoriel(number):
    #     if number == 1:
    #         return 1
    #     return number * inner_factoriel(number-1)
    # return inner_factoriel(number)

# print(factoriel(5))


# def rol_sorgula(page):
#
#     def inner(rol):
#         if rol == "Admin":
#             return "{0} rolü {1} sayfasına ulasabilir".format(rol, page)
#
#         else:
#             return "{0} rolü {1} sayfasına ulasamaz".format(rol, page)
#     return inner
#
# user1 = rol_sorgula("Produc Edit")
# print(user1("Admin"))

import math
import time


def calculate_time(func):
    def inner(*args,**kwargs):
        start = time.time()
        time.sleep(1)
        func(*args,**kwargs)
        finish = time.time()
        print("fonksiyon " + str(finish-start)+" saniye sürdü")
    return inner




@calculate_time
def usalma(a,b):
    print(math.pow(a,b))
@calculate_time
def factoriel(num):
    print(math.factorial(num))
usalma(2,3)
factoriel(5)







