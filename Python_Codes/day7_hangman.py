import os
import random

from hangman_tools import word_list, hangman_stages, logo # made a module named hangman_word it contain the word_list and the hangman_stages

print(logo)

# def get_random_words(words):
#     return list(words[random.randint(0,len(words)-1)])

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def check(guess, word, current_guess):
    for letter in range(0, len(word)):
        if guess == word[letter]:
            current_guess[letter] = guess
    

def display_status(guess, prev_guess, word, current_guess, attempt):
    if guess in prev_guess:     # check wether repetition of letter is done
        print(f"You have already guessed {guess}")
    else:
        check(guess, word, current_guess)
        if current_guess == prev_guess:
            print(f"You guessed '{guess}' which is not in the word .... so you lose a life")
    print(hangman_stages[attempt])
    print(' '.join(current_guess))
    print()

def hint_call(word, prev_guess, attempt, current_guess):
    possible_choices = [item for item in list(word) if item not in prev_guess]       # here lst1 = list(word) and lst2 = prev_guess
    let = random.choice(possible_choices)   # choosing a random letter for hint
    check(let, word, current_guess)
    return let
def play_hangman():

    word = random.choice(word_list)

    current_guess = ['_']*len(word)
    guess = ''
    attempt = 0  #attempts for the hangman list
    # display_status(guess, prev_guess, word, current_guess, attempt)
    hinted_list = []
    while attempt < len(hangman_stages)-1 and '_' in current_guess :
        
        prev_guess = current_guess.copy()
        hint = input("Do you need a hint (Y/n)").lower()
        if hint == 'y':
            hint_letter = hint_call(word, prev_guess, attempt, current_guess)
            hinted_list.append(hint_letter)
        else:
            guess = input("Please enter a single letter at a time ").lower()
            if current_guess == prev_guess and guess not in hinted_list:
                attempt += 1
                print(f"You guessed '{guess}' which is not in the word .... so you lose a life")

        clear_screen()  # Clear the screen first
        print(logo)  # Display the logo again after clearing the screen
        display_status(guess, prev_guess, word, current_guess, attempt)  # Then display the status

    if '_' not in current_guess:
        print("You Win")
    else:
        print("You Lose","......the word was ->",''.join(word))

play_hangman()
