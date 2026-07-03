# Print a KBC game
score = 0
print("Welcome to tHE KBC kaun banega crorepati You have to answer three questions correctly each question is worth 35 Lac rupees")
Question_1 = print("Which is A Surface phenomena:     "
"A) Boiling "
"B) Evaporation "
"C) Melting "
"D) Sublimation ")
ans1 = input("Enter your Answer for the first Question:- ").upper()
if ans1 == "B":
    print("You answered the first question correctly")
    score += 1
else:
    print("Wrong Answer the correct answer was 'B' (Evaporation) ")

print("Now its time for Question 2")
Queston_2 = print("How many Fathers do you Have:- " 
"A. Single " 
"B. Two " 
"C. Unknown " 
"D. Both A and B ")
ans2 = input("Enter your answer for second question:- ").upper()
if ans2 == "C":
    print("So you know the innocence of your Mother congrats")
    score += 1
else:
    print(" WRONG , You should investigate your mother's past")
print("Now its time for the last question")
Question_3 = print("What is your Body Count" 
"A. One " 
"B. Two " 
"C. Three " 
"D. NONE ")
ans3 = input("Enter your answer for last question:- ").upper()
if ans3 == "D":
    print("Correct but remember Your exams have fed you up many times")
    score += 1
else:
    print("Wrong , Everybody will reject you based on your face ")

if score == 3:
    print(f"You won Your score is {score}")
    print("105 Lacs have been transferred to your bank account")
else:
    print(f"Sorry you lost you only scored {score} points")
