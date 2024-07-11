import random
print("Welcome to the PyPassword Generator")
letter_count = int(input("How many letters would you like in your password? "))
special_char_count = int(input("How many special characters would you like in your password? "))
number_count = int(input("How many numbers would you like in your password? "))
lst_special_char = ['@', '#', '$', '&', '%', '!', '/']
p1 = ''
p2 = ''
p3 = ''
for _ in range(letter_count):
    p1 = p1 +str(chr(random.randint(97,122)))
for _ in range(special_char_count):
    p2 = p2 +str(lst_special_char[random.randint(0, len(lst_special_char)-1)])
for _ in range(number_count):
    p3 = p3 +str(random.randint(0, 9))

passwd = p1 + p2 + p3
passwd_list = list(passwd)

random.shuffle(passwd_list)

passwd = ''.join(passwd_list)
print("Password Genarated -> ",passwd)