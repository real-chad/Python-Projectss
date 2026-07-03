print("Welcome to the Ultimate Tracker for your Daily Habits")
coding = int(input("Enter the hours you did coding (in Hours) :- "))
walk =  int(input("Enter the Time you Walked (In minutes) :- "))
scrolling = int(input("Enter the time you did endless scrolling (in minutes) :- "))
if coding >= 2 and walk >= 30 and scrolling < 30: 
    print("Absolute Beast Mode, keep it up dude")
elif scrolling >= 30:
    print("Kamal Shahzade, bus scrolling kam kr de")
else:
    print("Ghatiya BAAP KI ghatiya aulad")