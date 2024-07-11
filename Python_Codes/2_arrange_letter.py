str1 = 'PyNaTive'
a=[]
b=[]
for i in range(len(str1)):
    if(str1[i].islower()):
        a.append(str1[i])
    else:
        b.append(str1[i])
str1_arr = ''.join(a+b)
print(str1_arr)