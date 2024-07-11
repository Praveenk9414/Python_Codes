import random

input_str = input()
names = input_str.split(',')

print(names[random.randint(0,len(names)-1)],"is going to buy the meal today!")
    