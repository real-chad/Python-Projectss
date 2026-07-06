


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


