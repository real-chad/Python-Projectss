import random
game = ["stone","paper","scissors"]


print ("Welcome to The Stone Paper Scissors Game You Have to choose one of the three options:- 'STONE', 'PAPER', 'SCISSORS'")


while True:
    com = random.choice(game)

    hum = input("Enter your Table Turning Move:- ").lower()
   
    if hum ==com:
        print("Match Draw")
        break
    elif hum == "scissors" and com == "paper" :
        print(f"You Have Successfully won the Game computer chose {com}")
        break
    elif hum == "stone" and com == "scissors":
        print(f"You Have Successfully Won , computer chose {com}")
        break

    elif hum == "paper" and com == "stone":
        print("You Have Successfully Won")
        break
    else:
        print(f"Computer Won! Computer chose: {com}")
        break
