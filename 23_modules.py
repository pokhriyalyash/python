# Modules 
# Modules are the .py files that contains set of functions you want to include in your programme 

# Inbuilt modules
# Datetime
# random
# math

# import datetime
# x = datetime.datetime.now()
# print(x)

# y = datetime.datetime(2025,11,24)
# print(y.strftime("%A")) #Monday
# print(y.strftime("%a")) #Mon
# print(y.strftime("%B")) #November
# print(y.strftime("%y")) #25



# import random

# x= random.randint(1,10)
# print(x)

# l = ["Heads","Tails"]
# x = random.choice(l)
# print(x)


# import math

# x = max(24,23,28)
# print(x)

# a = pow(2,10)
# print(a)

# b = math.sqrt(64)
# print(b)

# c = abs(-12)
# print(c)

# k = math.ceil(2.44)
# print(k)

# m = math.floor(2.4)
# print(m)


#creation of modules
# import demo01
# a=demo01.add(2,3)
# print(a)

#alias
import demo01 as d
a=d.add(2,3)
print(a)

b = d.employee["Name"]
print(b)