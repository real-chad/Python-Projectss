# default arguments
def additon(a,b,c):
    print(a+b+c)
additon(5,10,15)

# positional arguments
def subtraction (a,b = 10,c = 20):
    print(c-b-a)
subtraction(5)

# keyword arguments
def multiply (a,b,c):
    print(a*b*c)
multiply(a = 8, b = 5, c =6)