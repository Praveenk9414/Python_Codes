lst = ["x","y","z"]

# lst.append("b","j") --> this is wrong --> append takes exactly 1 argument 
lst.append("b")         # list.append(x)  -- (Add an item to the end of the list) equivalent to a[len(a):] = [x]
print(lst)


lst1 = ["f", "e", "d"]   # Output :['x', 'y', 'z', 'a', 'b', 'f', 'e', 'd']

# lst.extend(["f","e","d"])   
# print(lst)

lst.extend(lst1)
print(lst)

# The append method adds a single element to the end of the list.
# That single element can be any type of object, including iterables like lists, tuples, sets, or dictionaries.
# However, the entire iterable is treated as a single element and added as-is.





# Using list slicing to append and extend elements

lst6 = ["a","b","c"]

add = [1,2,3]       # here it can be tuple or dict or a set it works the same 

lst6[len(lst):] = [add]  # what append does
print(lst)

lst6[len(lst):] = add    # what extend does
print(lst)





lst2 = [1, 2, 3]
lst3 = [4, 5, 6]

lst2.append(lst3)
print(lst2)  # Output: [1, 2, 3, [4, 5, 6]]

tup3 = (4, 5, 6)
lst2.append(tup3)  # The tuple is added as a single element.
print(lst2)  # Output: [1, 2, 3, [4, 5, 6], (4, 5, 6)]

# Accessing the first element of the nested list
print(lst2[3][0])  # Output: 4



lst6.insert(2,"imposter")  # list.insert(i, x)  (i-->index of the position you want ti insert it ) (x--> the element)
print(lst6)          # the 'x' can be a single element or a iterable


lst6.remove(2)     # this removes just that element which = 'x'  and also it's first occurence ....
print(lst6)           # if no value in the list is ='x' --> ValueError 

#(it doesn't remove as per index) 
# want something that remove as per index -->
lst6.pop(2)
print(lst6)

lst6.pop()   # removes the last element from the list
print(lst6)



lst6.clear()   # clear everthing in the list, Equivalent to del a[:]
print(lst6)

# del lst6[:]
# print(lst6)






# to search for an element index   <syntax>  list.index(x[, start[, end]]) everthing within [] are optional parameters and x-> necessary (parameter) therefore outside []

list1 = ["a","123",1,2,3,1,(1,2,3)]

x = list1.index(1)   #searches for the element 1 in the list and returns it starting the search from 0
print(x)

x = list1.index(1,4)  #searches for the element from index-> 4 to the end and return the index
print(x)

#count the occurenect

y =list1.count(1)  #Return the number of times x appears in the list.
print(y)

# list.sort(*, key=None, reverse=False)  

list2 = [1,2,3,6,2,3,9,1,2,4]

list2.sort()
print(list2)
