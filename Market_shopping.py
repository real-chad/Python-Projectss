bill = 0 
cart = []
print ("Welcome to the Ultimate Bachat Bazar your goto place for cheapest groceries")
print("""Items Available in our Shop are : 
- Milk (Rs 100) 
- Bread (Rs 120) 
- Eggs (Rs 150 per dozen) """)

while True:
    item = input("Enter the item you want to order(or type 'checkout' for finishing) :- ").lower()
    if item == "checkout":
        print(f"You bought {cart}")
        print(f"Your total bill is {bill }")
        break
    
    elif item == "milk":
        print("Milk has been added to your cart ")
        cart.append("Milk")
        bill += 100
    elif item == "bread":
        bill += 120
        cart.append("bread")
        print("Bread has been added to your cart") 
    elif item == "eggs":
        bill += 150
        cart.append("eggs")
        print("A dozen eggs have been added to your cart")
    else:
        print("Kotha nahi ha be jo har rang ki mil jaye")
    

        
    

