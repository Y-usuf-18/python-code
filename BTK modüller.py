# YÖNTEM 1
# import math
# import math as islem
# value = dir(math)
# value = help(math)
# value = help(math.factorial)
# value = islem.sqrt(49)

# YÖNTEM 2
# from math import *

# value = factorial(4)
# print(value)


import random

# result = random.random() * 100

# result = random.uniform(10,100)

# names = ["ali","ayse","cenk","barıs"]

# result = names[random.randint(0,len(names) - 1)]

# result = random.choice(names)

# liste = list(range(10))
# random.shuffle(liste)


liste = list(range(100))
result = random.sample(liste,3)



print(result)