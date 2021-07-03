#Python Program to find sum of array

'''Given an array of integers, find the sum of its elements.

Examples :

Input : arr[] = {1, 2, 3}
Output : 6
1 + 2 + 3 = 6

Input : arr[] = {15, 12, 13, 10}
Output : 50'''

Method 1:-

def _sum(arr): 
      
    # initialize a variable
    # to store the sum
    # while iterating through
    # the array later
    sum=0
      
    # iterate through the array
    # and add each element to the sum variable
    # one at a time
    for i in arr:
        sum = sum + i
          
    return(sum) 
  
# driver function 
arr=[] 
# input values to list 
arr = [12, 3, 4, 15] 
  
# calculating length of array 
n = len(arr) 
  
ans = _sum(arr) 
  
# display sum 
print ('Sum of the array is ', ans) 
  
#====================================================================================================

Method 2:

# Python 3 code to find sum 
# of elements in given array
# driver function
arr = []
  
# input values to list
arr = [12, 3, 4, 15]
  
# sum() is an inbuilt function in python that adds 
# all the elements in list,set and tuples and returns
# the value 
ans = sum(arr)
  
# display sum
print ('Sum of the array is ',ans)


