# print a password generater
import random
chars = [ 'a' , 'b' , 'c','d','0','8','1','x','-','=','$','#']
password = ""
user = int(input("Enter length for your password:- "))
for i in range(user):
   
    password += (random.choice(chars))
print(password)