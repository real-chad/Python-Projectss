def palindrome(a):
    copy = a
    
    rev = 0
    while a>0:
        rev = rev * 10 + a%10
        a = a//10
    if copy == rev:
            print(f"{copy} is a palindrome")
    else:   
            print(f"{copy} is not a palindrome")
palindrome(131)

def additon (a,b=12):
      print(a+b+b)
    
additon(1)



