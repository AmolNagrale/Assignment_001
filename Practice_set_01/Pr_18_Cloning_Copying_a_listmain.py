# Cloning or Copying a list Python

'''1.Using slicing technique

This is the easiest and the fastest way to clone a list.
This method is considered when we want to modify a list and
also keep a copy of the original. In this we make a copy of
the list itself, along with the reference. This process is
also called cloning. This technique takes about 0.039 seconds
and is the fastest technique.'''

# Python program to copy or clone a list
# Using the Slice Operator
def Cloning(li1):
    li_copy = li1[:]
    return li_copy
  
# Driver Code
li1 = [4, 8, 2, 10, 15, 18]
li2 = Cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)


'''2.Using the extend() method

The lists can be copied into a new list by using the extend() function.
This appends each element of the iterable object (e.g., anothre list) to
the end of the new list. This takes around 0.053 second to complete.
'''

# Python code to clone or copy a list
# Using the in-built function extend()
def Cloning(li1):
    li_copy = []
    li_copy.extend(li1)
    return li_copy
  
# Driver Code
li1 = [4, 8, 2, 10, 15, 18]
li2 = Cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)

'''3.Using the list() method
This is the simplest method of cloning a list by using the builtin function list().
This takes about 0.075 seconds to complete.
'''
# Python code to clone or copy a list
# Using the in-built function list()
def Cloning(li1):
    li_copy = list(li1)
    return li_copy
  
# Driver Code
li1 = [4, 8, 2, 10, 15, 18]
li2 = Cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)

'''4. Using the method of Shallow Copy
This method of copying using copy.copy is well explained in the article Shallow Copy.
This takes around 0.186 seconds to complete.
Using list comprehension
The method of list comprehension can be used to copy all the elements individually
from one list to another. This takes around 0.217 seconds to complete.
'''
# Python code to clone or copy a list
# Using list comprehension
def Cloning(li1):
    li_copy = [i for i in li1]
    return li_copy
  
# Driver Code
li1 = [4, 8, 2, 10, 15, 18]
li2 = Cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)

'''5.Using the append() method

This can be used for appending and adding elements to list or copying them to a new list.
It is used to add elements to the last position of list. This takes around 0.325 seconds
to complete and is the slowest method of cloning.
'''
# Python code to clone or copy a list
# Using append()
def Cloning(li1):
    li_copy =[]
    for item in li1: li_copy.append(item)
    return li_copy
  
# Driver Code
li1 = [4, 8, 2, 10, 15, 18]
li2 = Cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)

'''6. Using the copy() method
The inbuilt method copy is used to copy all the elements from one list to another.
This takes around 1.488 seconds to complete.
'''

# Python code to clone or copy a list
# Using bilt-in method copy()
def Cloning(li1):
    li_copy =[]
    li_copy = li1.copy()
    return li_copy
  
# Driver Code
li1 = [4, 8, 2, 10, 15, 18]
li2 = Cloning(li1)
print("Original List:", li1)
print("After Cloning:", li2)

'''7.Using the method of Deep Copy
This takes around 10.59 seconds to complete and is the slowest method of cloning.
'''
#By using '='

# list1 = [1,2,3,4,5]
# list2 = list1
# print(list2)
# print(id(list2))
# print(list1)
# print(id(list2))

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

# list1 = [[1,2,3,4],[5,6,7,8]]
# list2 = list1.copy()
# print(list1, list2)
# list2[1][2]=1000
# print(list1, list2)

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


