# Decorator chaining fuction

# def decor(func):
#     def inner(name):
#         print("Decor function Exicution")
#         func(name)
#     return inner
# 
# def decor2(func):
#     def inner(name):
#         print("Second decor function exicution")
#         func(name)
#     return inner
# 
# @decor2 # for join the main function with decor2
# @decor  # for join the main function with decor
# 
# def wish(name):
#     print("Hello",name,"Good Morning")
# 
# wish("Durga")

# according to calling sequence of decorator function will exicuted  

#===========================================================================

# generator

# l = (x*x for x in range(10))
# for x in l:
#    # print(x) # generator concept  # This approche is not store a data directly to memory location, hence generator used paranthersis()
#     print(l)
#     
    
l = [x*x for x in range(10)] 
for x in l:
    #print(x) # MemoryError :- dirctly store the data in memory, hence memoryerror will occured.
    print(l)

#====================================================================

# Advance level of decorator use

# Class MyDecorator():
#     def __init__(self, arg1, arg2):
#          print("Inside __init__()")
#          self.arg1 = arg1
#          self.arg2 = arg2
#                
#     def __call__(self, f):
#          print("Inside __call__()")      
#         def wrapped_f(*args, **kwargs):
#              print("Inside wrapped_f()")
#              print("arg1", self.arg1)
#              f(*args, **kwargs)
#              print("After decorated f()")
#         return wrapped_f
#                
# @MyDecorator("test", 1, 2)
# def func1(a,b):
#      print("inside func1()")
#      return a+b

