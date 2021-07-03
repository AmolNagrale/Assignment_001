# Python Program for factorial of a number

'''Factorial of a non-negative integer, is multiplication of all integers smaller than or equal to n.
For example factorial of 6 is 6*5*4*3*2*1 which is 720.'''

# n! = n*(n-1)*(n-2)*(n-3)..........*1

# 1. Recursive :

# WAP program for 5 factorials

# def factorial(n):
#     # single line to find factorial
#     return 1 if (n==1 or n==0) else n * factorial(n - 1) # One line Solution (Using Ternary operator) 
# 
# # Driver Code
# num = 5
# print("Factorial of",num,"is",factorial(num))

#============================================================================================================
#2.Iterative: using while loop

def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1: # or = "if any one value is 1 then output is 1"
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return fact

# Driver Code
num = 100;
print("Factorial of",num,"is",factorial(num))

#====================================================================================
#2.Iterative: using for loop

# def fact(number):
#     # initialize variable to store factorial
#     fact = 1
#     # loop from the number till 1
#     for number in range(5, 1,-1):
#         # multiply current number with the product of previous numbers
#         fact = fact * number
#     return fact
# 
# # read number from keyboard
# number = int(input("Enter a number\n"))
# # find factorial
# factorial = fact(number)
# print("Factorial is "+str(factorial))

#==========================================================================================================
# 3. By using In-built function:


# import math
# 
# def factorial(n):
#     return(math.factorial(n))
# 
# 
# # Driver Code
# num = 5
# print("Factorial of", num, "is",factorial(num))

#=========================================================================================================






 