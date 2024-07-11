def swap(a,b):
    return b,a
a = int(input("enter the value of a"))
b = int(input("enter the value of b"))
a,b = swap(a,b)
print("a : ",a," b : ",b)
