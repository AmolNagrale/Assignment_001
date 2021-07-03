
# Comprehensions in Python

#list comprehension
# 1 normal method

# ls = []
# for i in range (100):
#     if i%3 == 0:
#         ls.append(i)
# 
# print(ls)
# 
# # using comprehension method
# ls =[i for i in range(100) if i%3 ==0]
# print(ls)
# 
# ls =[i for i in range(1, 100) if i%3 ==0]
# print(ls)

########################################################################

# Dictinary comprehensions

# dict1 = {i: f"item {i}" for i in range(5)} # original key:value pair
# 
# dict2 = {value:key for key,value in dict1.items()} # reverse Value:key
# 
# print(dict1, "\n", dict2)
#print(dict2)

########################################################################

# # Set comprehensions
# 
# # note :: set not repeat items
# 
# dresses = {dress for dress in {"dress1","dress2","dress2","dress3","dress1"}}
# print(dresses)
# print(type(dresses))
#########################################################################

# #Generator comprehensions 
# 
# evens = (i for i in range(100) if i%2 ==0)
# print(evens)
# print(evens.__next__()) # Generator has iterate once 
# print(evens.__next__())
# print(evens.__next__())
# print(evens.__next__())
# print(evens.__next__())
# 
# # generator don't allocate memory location to whole list

##########################################################################

# # Set datatypes
# 
# s = {"Amol",100,0,40, True,1.5}
# 
# s.add(60)
# 
# print(s)
# 
# s.remove(100)
# 
# print(s)
# 
# s.discard(1.5)
# 
# print(s)

###########################################################################

# # frozenset datatype
# 
# s = {10,20,30,40}
# s = frozenset(s)
# print(type(s))
# 
# fs = frozenset({10,20,30,40})
# for i in fs:
#     print(i)

# we haven't done any index/slice/append operation in it bcz, it's immutable.

###########################################################################

#dict datatype

# d = {"Amol":101, "Amit":102,"Ashish":103}
# print(d)

# print(d)
# print(d["Amol"])
# print(d[101])
# d.add("Amita"=104)
# print(d)

############################################################################

import keyword
str_list = ['for', 'TP', 'python', 'del', 'Mango', 'assert', 'yield','if','Lion', 'as','Snake', 'box', 'return', 'try', 'loop', 'eye', 'global', 'while', 'update', 'is']
keyword_list = []
non_keyword_list = [] 
for item in str_list:
   if keyword.iskeyword(item):
      keyword_list.append(item)
   else:
      non_keyword_list.append(item)
print("Keywords: " + "\n",str(keyword_list))
print("\nNon Keywords: " +"\n", str(non_keyword_list))
      


