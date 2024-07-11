files = ['apple.txt','yahoo.pdf','gmail.pdf','google.txt','amazon.pdf','facebook.txt','flipkart.pdf']

lst1 =[]
lst2 = []

for extension in files:
    if(extension[-3:] == "txt"):
        lst1.append(extension)
    else:
        lst2.append(extension)

new_file = lst1 + lst2
print(new_file)