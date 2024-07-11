import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


def isWinner(usr,comp):
    if (usr - comp == 2) or (comp - usr == 1) :
        print("You Lose")
    else:
        print("You Win")



print("Let's play Rock Paper &scissors")
print("0-rock, 1-paper, 2-scissors")
print("provide me a sequence in which you want to keep the list_of_choice ")
print("e.g for for lst_choice = [rock,paper,scissors] you should type --> 012")

list_seq_input = input()

sample_list = ["rock", "paper", "scissors"]

a = int(list_seq_input[0])
b = int(list_seq_input[1])
c = int(list_seq_input[2])
print("sequence of list is --> ",sample_list[a], sample_list[b], sample_list[c])

user_input = int(input())
computer_input = random.randint(0, 2)

lst = [rock,paper,scissors]
lst_choice = [lst[a], lst[b], lst[c]]

print("User:")
print(lst_choice[user_input])

print("Computer:")
print(lst_choice[computer_input])

if user_input - computer_input == 0:
    print("It's a tie")
elif list_seq_input == '012' or list_seq_input == '201' or list_seq_input == '120':
    isWinner(user_input,computer_input)
else:
    isWinner(computer_input,user_input)
