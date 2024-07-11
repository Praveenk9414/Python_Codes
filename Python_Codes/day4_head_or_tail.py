import random
coin = random.randint(0,1)
print("do you wanna toss a coin Y/N \n")
toss = input()
if(toss == 'Y'):
    if(coin == 1):
        print("Head")
    else:
        print("Tail")
else:
    print("Ok")