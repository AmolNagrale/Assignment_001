
# Ways to find length of list

List being an integral part of Python day-day programming has to be learned
by all the python users and having a knowledge of its utility and operations
is essential and always a plus. So this article discusses one such utility
of finding the no. of elements in a list.


Method 1 : Naive Method

In this method one just runs a loop and increases the counter till the last
element of the list to know its count. This is the most basic strategy that
can be possibly employed in the absence of other present techniques.

Code #1 : Demonstrating finding length of list using Naive Method


# Python code to demonstrate
# length of list
# using naive method
  
# Initializing list 
test_list = [ 1, 4, 5, 7, 8 ]
  
# Printing test_list
print ("The list is : " + str(test_list))
  
# Finding length of list 
# using loop
# Initializing counter
counter = 0
for i in test_list:
      
    # incrementing counter
    counter = counter + 1
  
# Printing length of list 
print ("Length of list using naive method is : " + str(counter))
Output :

The list is : [1, 4, 5, 7, 8]
Length of list using naive method is : 5

#===========================================================================================================

Method 2 : Using len()




The len() method offers the most used and easy way to find length of any list.
This is the most conventional technique adopted by all the programmers today.


# Python program to demonstrate working
# of len()
a = []
a.append("Hello")
a.append("Geeks")
a.append("For")
a.append("Geeks")
print("The length of list is: ", len(a))
Output:
The length of list is:  4

# Python program to demonstrate working
# of len()
n = len([10, 20, 30])
print("The length of list is: ", n)
Output:
The length of list is:  3
Method 3 : Using length_hint()

This technique is lesser known technique of finding list length. This particular method is defined in operator class and it can also tell the no. of elements present in the list.

Code #2 : Demonstrating finding length of list using len() and length_hint()


# Python code to demonstrate
# length of list
# using len() and length_hint
from operator import length_hint
  
# Initializing list 
test_list = [ 1, 4, 5, 7, 8 ]
  
# Printing test_list
print ("The list is : " + str(test_list))
  
# Finding length of list 
# using len()
list_len = len(test_list)
  
# Finding length of list 
# using length_hint()
list_len_hint = length_hint(test_list)
  
# Printing length of list 
print ("Length of list using len() is : " + str(list_len))
print ("Length of list using length_hint() is : " + str(list_len_hint))
Output :

The list is : [1, 4, 5, 7, 8]
Length of list using len() is : 5
Length of list using length_hint() is : 5
Performance Analysis – Naive vs len() vs length_hint()

When while choosing amongst alternatives its always necessary to have a valid
reason why to chose one over another. This section does a time analysis of
how much time it takes to execute all of them to offer a better choice to use.

Code #3 : Performance Analysis


# Python code to demonstrate
# length of list
# Performance Analysis
from operator import length_hint
import time
  
# Initializing list 
test_list = [ 1, 4, 5, 7, 8 ]
  
# Printing test_list
print ("The list is : " + str(test_list))
  
# Finding length of list 
# using loop
# Initializing counter
start_time_naive = time.time()
counter = 0
for i in test_list:
      
    # incrementing counter
    counter = counter + 1
end_time_naive = str(time.time() - start_time_naive)
  
# Finding length of list 
# using len()
start_time_len = time.time()
list_len = len(test_list)
end_time_len = str(time.time() - start_time_len)
  
# Finding length of list 
# using length_hint()
start_time_hint = time.time()
list_len_hint = length_hint(test_list)
end_time_hint = str(time.time() - start_time_hint)
  
# Printing Times of each 
print ("Time taken using naive method is : " + end_time_naive)
print ("Time taken using len() is : " + end_time_len)
print ("Time taken using length_hint() is : " + end_time_hint)