str = input("Enter your string:")
isBinary = 0
for i in str:
    if i.isdigit():
        if i == "1" or i == "0":
            isBinary = 1
        else:
            isBinary = 0
            break
    else:
        isBinary = 0
        break

if isBinary:
    print("Yes")
else:
    print("No")