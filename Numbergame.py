import random
com = random.randint(1,100)
 
tries = 0



while True:
    tries += 1
    hum  = int(input("Guess the Number if you have one Father:- "))
    if hum == com:
        print(f"Congrats You are son of a single father but your mother tried it {tries} times")
        break
    elif hum > com:
        print("Go a little bit lower to prove your Mother innocence")
    elif hum < com:
        print("Go a bit higher ah") 