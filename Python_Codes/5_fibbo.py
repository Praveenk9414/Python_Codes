def fibbo(n):
    if(n<=1):
        return 1
    else:
        return fibbo(n-1)+fibbo(n-2)

numofterm = int(input("Enter the no of terms"))
for i in range(numofterm):
    print(fibbo(i))