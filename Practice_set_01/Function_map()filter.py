
# without lambda fuction

# def double(x):
#     return x*2
# l=[1,2,3,4]
# l1=list(map(double,l))
# print(l1)
# print(type(l1))

# def add(x):
#     return x+x
# l=[1,2,3,4,5]
# l1=list(map(add,l))
# print(l1)

##########################################################################

#with lambda function

# l=[1,2,3,4,5]
# l1=list(map(lambda x:x*2,l))
# print(l1)

# l=[10,20,30,40,50]
# l1=list(map(lambda x:x+x,l))
# print(l1)

#########################################################################

# python code to demonstrate working of reduce()

# # importing functools for reduce()
# import functools
# 
# # initializing list
# lis = [1, 3, 5, 6, 2, ]
# 
# # using reduce to compute sum of list
# # print("The sum of the list elements is : ", end="")
# # print(functools.reduce(lambda a, b: a+b, lis))
# 
# # using reduce to compute maximum element from list
# print("The maximum element of the list is : ", end="")
# print(functools.reduce(lambda a, b: a if a > b else b, lis))

###########################################################################

#my code

# import functools
# list = [1,5,7,3,7,9,]
# print("The maximum elements of list is: ",end="")
# print(functools.reduce(lambda a,b: a if (a>b) else b,list))

###########################################################################

# python code to demonstrate working of reduce()
# using operator functions

# importing functools for reduce()
# import functools
# 
# # importing operator for operator functions
# import operator
# 
# # initializing list
# lis = [1, 3, 5, 6, 2, ]
# 
# # using reduce to compute sum of list
# # using operator functions
# print("The sum of the list elements is : ", end="")
# print(functools.reduce(operator.add, lis))
# 
# # using reduce to compute product
# # using operator functions
# print("The product of list elements is : ", end="")
# print(functools.reduce(operator.mul, lis))
# 
# # using reduce to concatenate string
# print("The concatenated product is : ", end="")
# print(functools.reduce(operator.add, ["geeks", "for", "geeks"]))
# 
# ###########################################################################

# #my code :: multiplication & adition by using filter function - without lambda

# import functools
# import operator
# list = [1,3,6,7,9,2]
# 
# print("The multiplication of the given list is :",end="")
# print(functools.reduce(operator.mul, list))
# 
# print("The addition of given list is :",end="")
# print(functools.reduce(operator.add, list))
# 
# print("The concatenated product is : ", end="")
# print(functools.reduce(operator.add,["geeks","for","geeks"]))

################################################################################

# python code to demonstrate summation
# using reduce() and accumulate() ------------- sequence

# # importing itertools for accumulate()
# import itertools
# 
# # importing functools for reduce()
# import functools
# 
# # initializing list
# lis = [1, 3, 4, 10, 4]
# 
# # printing summation using accumulate()
# print("The summation of list using accumulate is :", end="")
# print(list(itertools.accumulate(lis, lambda x, y: x+y)))
# 
# # printing summation using reduce()
# print("The summation of list using reduce is :", end="")
# print(functools.reduce(lambda x, y: x+y, lis))

############################################################################

# lis = [1, 3, 4, 10, 4]
# import functools
# import itertools
# 
# print("The summation of list using accumulate is :",end="")
# print(list(itertools.accumulate(lis,lambda x,y:x+y)))
# 
# print("The addition of list using filter function :",end="")
# print(functools.reduce(lambda x,y:x+y ,lis))

#############################################################################




