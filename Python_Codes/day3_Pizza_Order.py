print("Thank you for choosing Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L :")
add_pepperoni = input("Do you want pepperoni? Y or N :")
extra_cheese = input("Do you want extra cheese? Y or N :") 

bill = 0

if(size == 'S'):
    bill += 15
elif(size == 'M'):
    bill += 20
elif(size == 'L'):
    bill += 25
else:
    print("Invalid size")

if(size == 'S' and add_pepperoni == 'Y'):
    bill += 2
elif((size == 'M' or 'L') and add_pepperoni == 'Y'):
    bill += 3

if(extra_cheese == 'Y'):
    bill += 1
    
print(f"Your final bill is: ${bill}.")    