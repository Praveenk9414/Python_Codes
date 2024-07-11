import random #random module generate a random number

random_integer = random.randint(1,10)

print(random_integer)

random_float = random.random()  # only limited to random number generation of num b/w 0 and 1
print(random_float)

random_float2 = random.random() * 5  # this will now generate random number b/w 0 and 5
print(random_float2)
# this module are just another python code or .py file which are imported using import function

# For example let's make a module for value of pie
import day4_pie_Module

print(day4_pie_Module.pie)

love_score = random.randint(1,100)
print(f"Your love score is {love_score}")