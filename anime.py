current_time = int(input("Enter the Time in 24 hrs Format:- "))
tomorrow_task = input("Kal subha Github account setup krna ha (True or False):- ")
if current_time >= 23 and tomorrow_task == "True":
    print("Tere Maa Baap na tujhe is lye paida kya ha kyaaa??? Mobile band kr or jaldi so")
elif current_time < 23:
    print("Chal Aik adh or episode dekh le koi ni mera bacha")
else:
    print("Yr bus sukoon sa rest kr le koi na bare bare hain teri gf ka")