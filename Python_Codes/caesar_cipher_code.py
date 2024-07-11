# list_letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# # def encode(shift_num, message):
# #     lst = []
# #     for letter in message:
# #         letter_num = list_letter.index(letter)
# #         index = letter_num + shift
# #         if index > len(list_letter)-1:
# #             val = len(list_letter) - letter_num
# #             index = -len(list_letter) + shift - val
# #         lst.extend(list_letter[index])
# #     return ''.join(lst)

# # def decode(shift_num, message):
# #     lst = []
# #     for letter in message:
# #         letter_num = list_letter.index(letter)
# #         index = letter_num - shift
# #         lst.extend(list_letter[index])
# #     return ''.join(lst)

# def encode(shift_num, message):
#     lst = []
#     for letter in message:
#         letter_num = list_letter.index(letter)
#         index = letter_num + shift
#         if index > len(list_letter)-1:

#             list_letter.extend()
#         lst.extend(list_letter[index])
#     return ''.join(lst)

# def decode(shift_num, message):
#     lst = []
#     for letter in message:
#         letter_num = list_letter.index(letter)
#         index = letter_num - shift
#         lst.extend(list_letter[index])
#     return ''.join(lst)

# ek_aur_bar = 'y'
# while ek_aur_bar == 'y':
#     x = input("Type 'encode' to encrypt and 'decode' to decrypt -> ")
#     if x == 'encode':
#         message = input("Type your message -> ")
#         shift = int(input("Type the shift number -> "))
#         print("Here the encoded message ->", encode(shift, message))
#     elif x == 'decode':
#         message = input("Type your message -> ")
#         shift = int(input("Type the shift number -> "))
#         print("Here the decoded message -> ", decode(shift, message))
#     ek_aur_bar = input("Do you want to continue Y/n ").lower()

list_letter = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

x = ['d','f','a','e']
for letter in x:
    max = 0
    prev = 0
    if letter in list_letter and max >= prev:
        max = list_letter.index(letter)
        prev = max
print(list_letter[max])