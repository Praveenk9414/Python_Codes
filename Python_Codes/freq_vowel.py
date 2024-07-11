str1 = "Hello WorOld"
count = 0
for i in str1.lower():
    if(i == 'a' or i=='e' or i=='i' or i=='o' or i=='u'):
        count +=1
print(count)