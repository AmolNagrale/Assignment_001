# Clear a list using different ways.

'''1. clear()
2. initialise a list with no values
3. *=0
4. del()'''

mylist = [1,2,3,4,5,6]

print("list before clear ",mylist)

mylist.clear()

print("list after clear",mylist)

#=======================================================================

#2. initialise a list with no values

mylist = [1,2,3,4,5,6,7]

print("list before clear ",mylist)

mylist = []

print("list after clear",mylist)

#======================================================================

#3. *=0

mylist = [1,2,3,4,5,6,7]

print("list before clear ",mylist)

mylist *=0

print("list after clear",mylist)

#======================================================================

# 4. using del()

mylist = [1,2,3,4,5,6,7]

print("list before clear ",mylist)

del mylist[:]

print("list after clear",mylist)

#=====================================================================




