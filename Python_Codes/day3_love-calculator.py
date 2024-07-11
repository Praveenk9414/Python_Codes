print("The Love Calculator is calculating your score...")
name1 = input("What is your name? ").upper()
name2 = input("What is their name? ").upper()

comb_name = name1 + name2
lower_name = comb_name.lower()
t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")

count_True = t + r + u + e

l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")

count_Love = l + o + v + e

score = int(str(count_True)+str(count_Love))
if(10 > score > 90):
    print(f"Your score is *{score}*, you go together like coke and mentos.")
elif(40 < score < 50):
    print(f"Your score is *{score}*, you are alright together.")
else:
    print(f"Your score is *{score}*.")


# count_True = sum(1 for char in name1 if char in 'TRUEFALSE')
# count_Love = sum(1 for char in name2 if char in 'LOVEFALSE')


# for i in range(len(name1)):
#     if(name1[i] == 'T' or name1[i] == 'R' or name1[i] == 'U' or name1[i] == 'E'):
#         count_True += 1
#     if(name1[i] == 'L' or name1[i] == 'O' or name1[i] == 'V' or name1[i] == 'E'):
#         count_Love += 1
# for i in range(len(name2)):
#     if(name2[i] == 'T' or name2[i] == 'R' or name2[i] == 'U' or name2[i] == 'E'):
#         count_True += 1
#     if(name2[i] == 'L' or name2[i] == 'O' or name2[i] == 'V' or name2[i] == 'E'):
#         count_Love += 1

# Love_score = count_True*10 + count_Love
# Love_score_as_int = int(Love_score)
# if(Love_score_as_int < 10 or Love_score_as_int > 90):
#     print(f"Your score is *{Love_score_as_int}*, you go together like coke and mentos.")
# elif(Love_score_as_int > 40 and Love_score_as_int < 50):
#     print(f"Your score is *{Love_score_as_int}*, you are alright together.")
# else:
#     print(f"Your score is *{Love_score_as_int}*.")


