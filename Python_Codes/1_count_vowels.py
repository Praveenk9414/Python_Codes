string = "Hello World"
count = sum(1 for char in string.lower() if char in 'aeiou')
print(count)
# count = 0
# for char in string:
#     if char in 'aeiou':
#         count += 1