from pathlib import Path
def createfile():
    try:
        name = input("Enter the name for your File:- ")
        path = Path(name)
        if not path.exists():
            with open(path,"w") as fs:
                data = input("What do you want to enter in your file:-")
                fs.write(data)
            print("File Created Successfully")
        else:
            print("Error, File Name already exists")
    except Exception as err:
        print(f"An error has occured as {err}")

def readfile():
    try:
        name = input("Please tell the name of your File:- ")
        path = Path(name)
        if path.exists():
            with open(path,'r') as fs:
                content = fs.read()
                print(f"The content of your file is :- \n{content} ")
        else:
            print("Invalid Name, File doesnot Exist")
    except Exception as err:
        print(f"An error has Occured as {err}")

def updatefile():
    try:
        name = input("Enter the name of your file:- ")
        path = Path(name)
        
        if path.exists():
            print("ENTER 1 TO RENAME YOUR FILE")
            print("ENTER 2 TO APPEND CONTENT")
            print("ENTER 3 TO OVERWRITE YOUR FILE")
            choice = int(input("Enter your option:- "))
            
            if choice == 1:
                new_name = input("Enter the new name of your file:- ")
                new_path = Path(new_name)
                if not new_path.exists():
                    path.rename(new_path)
                    print("File has been Successfully Renamed")
                else:
                    print("File already Exists")
                    
            elif choice == 2:
                with open(path, 'a') as fs:
                    data = input("What do you want to append:- ")
                    fs.write("\n" + data)
                print("Successfully appended")
                
            elif choice == 3:
                with open(path, 'w') as fs:
                    data = input("What do you want to overwrite:- ")
                    fs.write("\n" + data)
                print("Successfully overwritten")
        else:
            print("No such file exists!")
            
    except Exception as err:
        print(f"An error has occurred as {err}")


def deletefile():
    try:
        name = input("Enter the name of your File:- ")
        path = Path(name)
        if path.exists():
            path.unlink()
            print("File deleted Successfully")
        else:
            print("No such File exists")
    except Exception as err:
        print(f"An error has occured as {err}")


    


while True:
    print("\nPress 1 To Create a File")
    print("Press 2 To Read a File")
    print("Press 3 To Update a File")
    print("Press 4 To Delete a File")
    print("Press 5 To Exit") 
    
    try:
        a = int(input("\nTell your Response:- "))
        
        if a == 1:
            createfile()
        elif a == 2:
            readfile()
        elif a == 3:
            updatefile()
        elif a == 4:
            deletefile()
        elif a == 5:
            print("System has closed")
            break
        else:
            print("Invalid Option! Please enter a number between 1 and 5.")
            
    except ValueError:
        print(" Please enter a valid number, text characters are not allowed ")
