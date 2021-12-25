# '='/copy/deepcopy

'''Important Points:
The difference between shallow and deep copying is only relevant for compound objects
(objects that contain other objects, like lists or class instances):

A shallow copy constructs a new compound object and then (to the extent possible) inserts
references into it to the objects found in the original.
A deep copy constructs a new compound object and then, recursively, inserts copies into
it of the objects found in the original.'''

#By using '='

# list1 = [1,2,3,4,5]
# list2 = list1
# print(list2)
# print(id(list2))
# print(list1)
# print(id(list1))

# By using copy()/shallow copy

# list1 = [1,2,3,4]
# list2 = list1.copy() # syntax of shallow copy
# print(list1)
# print(list2)
# list2[2] = 100
# print(list2)    # only changes done at list2 
# print(list1)    # print as it is
# 
# print(list1,list2)

#shallow copy by using nested list

list1 = [[1,2,3,4],[5,6,7,8]]
list2 = list1.copy()
print(list1, list2)
list2[1][2]=1000
print(list1, list2)

''' Whenever i have used nested list that time it has to be changed both
lists but same senario i have used with single list it has changed on perticular list(list2)'''

#shallow copy by using nested list for append operation

# list1 = [[1,2,3,4],[5,6,7,8]]
# list2 = list1.copy()
# list2.append([9,8,7,6])
# print(list2)
# print(list1)

'''whenever append operation is performing on perticular list that time
changes has been shown in only this list  '''

# Deepcopy opration

# import copy  # In deep copy operation we must be need to import copy
# list1 = [1,2,3,4,5]
# list2 = copy.deepcopy(list1)
# list2[1] = 100
# print(list2, list1) # In this senario same operation has been performed as per shallow copy(shallow copy == Deep copy)

# Deepcopy is using nested lists

# list1 = [[1,2,3,4],[5,6,7,8]]
# list2 = copy.deepcopy(list1)
# list2[1][2] = 100
# print(list1, list2)

'''In this senario shallow copy != deepcopy ---- changes has done only in perticular list of items'''









