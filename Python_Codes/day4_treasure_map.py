line1 = ["⬜️","️⬜️","️⬜️"]
line2 = ["⬜️","⬜️","️⬜️"]
line3 = ["⬜️️","⬜️️","⬜️️"]
map = [line1, line2, line3]
print("Hiding your treasure! X marks the spot.")
position = input() # Where do you want to put the treasure?

# letter = position[0]
# num = int(position[1])

# if (position[0] == 'A'):
#     pos = 0
# elif position[0] == 'B':
#     pos = 1
# else :
#     pos = 2

# if num == 3:
#     line3[pos] = 'X'
# elif num == 2:
#     line2[pos] = 'X'
# else:
#     line1[pos] = 'X'

letter = position[0].lower()

abc = ["a","b","c"]
letter_index = abc.index(letter)
num_index = int(position[1])-1

map[num_index][letter_index] = 'X'

print(f"{line1}\n{line2}\n{line3}")