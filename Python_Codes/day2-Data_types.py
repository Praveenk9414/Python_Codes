greeting = "Hello"
for i in range(len(greeting)):
    print(greeting[i])
print("Praveen"[0])

3+5
7-4
3*2
2**3
print(type(5/2)) #-- o/p -> float
print(type(67//45)) #-- o/p -> int

# PEMDAS     --- priority order
#     Parantheses
#     Exponents
#     Multiplication  / Division
#     Addition  /  Subtraction

print(3 * (3 + 3) / 3 - 3)

# # calculating BMI
# height = input()
# weight = input()

# weight_as_int = int(weight)
# height_as_float = float(height)

# # Using the exponent ops--
# bmi = weight_as_int/(height_as_float ** 2)

# # Or using Multiplication and pemdas / bodmas
# bmi = weight_as_int/(height_as_float * height_as_float)

# bmi_as_int = int(bmi)
# print(bmi_as_int)

# Uisng round function...
print(8/3)
print(round(8/3))
print(round(7/2, 2))


score = 0

# incrementing shortcuts
score += 1
score -= 1
score *= 1
score /= 1

points = 10
level = 5
isWinning = True

print("your score point is "+str(points)+", and your level is "+str(level)+", also you are winning "+str(isWinning))

# or Using f-string

print(f"your score point is {points}, and your level is {level}, also you are winning {isWinning}")