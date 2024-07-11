print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12 or 15? "))


split = int(input("How many people to split the bill? "))

# net_amount = total_bill + total_bill * (tip/100)..... or ......net_bill_with_tip = (total_bill*(1 + (tip/100)))/split
# net_bill_no_tip = total_bill / split
# net_tip_per_person = (total_bill * (tip/100)) / split
# print(f"Each person should pay: ${round(net_bill_with_tip, 2)}, of which the actual bill per person is ${round(net_bill_no_tip, 2)} and tip per person is ${round(net_tip_per_person, 2)}")

net_bill_with_tip = "{:.2f}".format((total_bill*(1 + (tip/100)))/split)
net_bill_no_tip = "{:.2f}".format(total_bill / split)
net_tip_per_person = "{:.2f}".format((total_bill * (tip/100)) / split)

print(f"Each person should pay: ${net_bill_with_tip}, of which the actual bill per person is ${net_bill_no_tip} and tip per person is ${net_tip_per_person}")