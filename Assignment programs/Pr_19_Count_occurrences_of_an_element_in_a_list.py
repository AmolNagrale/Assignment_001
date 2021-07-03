# Count occurances of an elements in list

# 1. approche using for loop

# def occurance():
#     count = 0
#     for ele in list1:
#         if ele == x :
#             count +=1
#     return count
# 
# #Driver code
# list1 = [10,20,30,10,10,10,40,10,20,10]
# x = 10
# print("{} has occured by {} times".format(x, occurance()))
#

#=======================================================================

#2. approche by using counte() function
# def counter():
#     return mylist.count(x)
# 
# mylist = [10,5,20,30,40,70,10,10,10]
# x = 10
# print("{} has occured by {} times".format(x, counter()))

#=====================================================================

#3.(Using Counter()) 

# from collections import Counter
#  
# # declaring the list
# l = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
#  
# # driver program
# x = 4
# d = Counter(l)
# print('{} has occurred {} times'.format(x, d[x]))

#====================================================================
from collections import counter

mylist = [10,20,30,40,10,10]
x = 10
dic = counter(mylist)
print("{} has occurred {} times".format(x, dic[x]))


