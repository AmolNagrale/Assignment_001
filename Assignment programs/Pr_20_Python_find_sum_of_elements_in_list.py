# Python program to find sum of elements in list

# list = [10,20,30,40,50]
# 
# total = 0
# 
# for i in range(0,len(list)):
#     
#     total +=list[i]
#     
# print("The sum of list elements is :",total)

#========================================================
# by using functions

# def sums():
#     total = 0
#     for i in range (0, len(list)):
#         total +=list[i]
#     return total
# 
# list = [10,20,30,40,50]
# print(sums())

#=======================================================

#by using sum() method

# list = [10,20,30,30,40,50,70]
# #summation = sum(list)
# #print(summation)
# print(" Sum of total elements are ",sum(list))

#=========================================================

# Python program to find sum of all
# elements in list using recursion
 
# creating a list
list1 = [11, 5, 17, 18, 23]
 
# creating sum_list function
def sumOfList(list, size):
   if (size == 0):
     return 0
   else:
     return list[size - 1] + sumOfList(list, size - 1)
  
# Driver code    
total = sumOfList(list1, len(list1))
 
print("Sum of all elements in given list: ", total)

