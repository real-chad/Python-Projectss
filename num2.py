import random
com = random.randint(1,100)
tries = 0
print("You Have Only 5 Tries")
while True:
    
    hum = int(input("Guess the Number if you can:- "))
    tries += 1
    if tries >= 5 and hum != com:
        print(f"You have Lost the Game , Original Number was {com}")
        break
    if hum == com:
        print(f"You have successfully won the game in {tries} tries")
        break
    elif hum > com :
        print("Go Lower Please , you are not climbing Mount Everest")
    elif hum < com :
        print("Go Higher Please ,think you are climbing Mount Everest")
    
    

    