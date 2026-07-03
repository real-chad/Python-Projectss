# a = 34
# a = 76
# a = "Hadi"
# print(type(a))
# b = "2"
# a = int(b)
# print(a)
# a = 'dd'
# print(a)

import secrets
import string
chars = "ajkfnjksnfjsnfnsn23jn4j35i34i093i49;[];[;;]"
us = int(input("Enxter the length fro your password:- "))
password = ""
for i in range(us):
    password += secrets.choice(chars)
print(password)