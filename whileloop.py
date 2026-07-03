


# a  = 5678
# while a > 0:
#     print (a%10)
#     a  = a// 10
rev = 0
n = int(input("Enter your NUmber please:- "))

while n>0 :
    rev = rev * 10 + n % 10
    n = n//10
print(rev)


# aik aisa system jo usr sa input le or sare numbers ko add kr de
sum = 0
a = int(input("Enter your Numbere please:- "))
while a>0:
    n = 