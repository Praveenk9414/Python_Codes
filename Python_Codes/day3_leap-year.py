# year = int(input("Enter the year you want to check "))

# if(year % 100 == 0 and year % 400 != 0):
#     print("Not leap year")
# elif(year % 4 == 0):
#     print("Leap year")
# else:
#     print("Not leap year")

# if year % 4 == 0:
#       if year % 100 == 0:
#           if year % 400 == 0:
#               print("Leap year")
#           else:
#               print("Not leap year")
#       else:
#           print("Leap year")
# else:
#      print("Not leap year")




x = int(input("Enter the year you want to check leap year"))
if(x%4==0 | x%400==0):
    print("leap year")
else:
    print("Not Leap year")