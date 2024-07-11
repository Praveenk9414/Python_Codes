# calculating BMI
height = input("Enter the height (in metres .. 1.75 , 1.89)")
weight = input("Enter the weight (in kg)")

weight_as_int = int(weight)
height_as_float = float(height)

# Using the exponent ops--
bmi = weight_as_int/(height_as_float ** 2)

# Or using Multiplication and pemdas / bodmas
bmi = weight_as_int/(height_as_float * height_as_float)

bmi_as_int = int(bmi)

# if(bmi_as_int < 18.5 ):
#     print(f"Your BMI is {bmi_as_int}, you are underweight.")
# elif(bmi_as_int >= 18.5 and bmi_as_int < 25):
#     print(f"Your BMI is {bmi_as_int}, you have a normal weight.")
# elif(bmi_as_int >= 25 and bmi_as_int < 30):
#     print(f"Your BMI is {bmi_as_int}, you are slightly overweight.")
# elif(bmi_as_int >= 30 and bmi_as_int < 35):
#     print(f"Your BMI is {bmi_as_int}, you are obese.")
# else:
#     print(f"Your BMI is {bmi_as_int}, you are clinically obese.")

# Or you could directly did this

if bmi_as_int < 18.5:
  print(f"Your BMI is {bmi_as_int}, you are underweight.")
elif bmi_as_int < 25:
  print(f"Your BMI is {bmi_as_int}, you have a normal weight.")
elif bmi_as_int < 30:
  print(f"Your BMI is {bmi_as_int}, you are slightly overweight.")
elif bmi_as_int < 35:
  print(f"Your BMI is {bmi_as_int}, you are obese.")
else:
  print(f"Your BMI is {bmi_as_int}, you are clinically obese.")