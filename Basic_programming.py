
# Global veriable basic program practice

# a = 10
# def f1():
#     a = 777
#     print(a)
# 
# def f2():
# 	print(a)
#     
#     
# f1()
# f2()

##########################################################################

# a = 10
# def f1():
#     global a
#     a=777
#     print(a)
#     
# def f2():
#     print(a)
#     
# print(a)        
# 
# f1()
# f2()

##########################################################################
''' Use same variable name inside/outside of the function,
1. we are able to call global veriable inside & outside of function.
2. But for local veriable we are not able accss outside the function'''

# x = "awesome"
# 
# def myfunc():
#   x = "fantastic"
#   print("Python is " + x)
# 
# myfunc()
# 
# print("Python is " + x)

##########################################################################

'''The global Keyword

Normally, when you create a variable inside a function, that variable is local,

and can only be used inside that function.

To create a global variable inside a function, you can use the global keyword.

#Example##

If you use the global keyword, the variable belongs to the global scope:'''

# def myfunc():
#   global x
#   x = "fantastic"
# 
# myfunc()
# 
# print("Python is " + x)



# 2. Example

# x = "awesome"
# 
# def myfunc():
#   global x
#   x = "fantastic"
# 
# myfunc()
# 
# print("Python is " + x)


###########################################################################


# x = "Fantastic"
# 
# def f1():
#     
#     global x
#     
#     x = " eazy "
#     
#     # print( "Python is " + x)
# f1()
# 
# print("python is " + x)

##########################################################################

# Bool data types
# 
# b = True
# print(type(b))


# a = 10
# b = 20
# c = a<b
# print(c)

# a = True + True # Value of True = 1 
# print(a)
# b = True +False # Value of False = 0
# print(b)

###########################################################################

# str = "Teambrainwork"
# print(len(str))
# print(str[:8:-2])
# a = int("b1111")
# print(a)

##########################################################################
# y = "TeamBrainworks"
# x = [10,20,30,255]
# b = bytearray(x)
# print(type(b))
# print(x[-2])
# print(x[::-2])
# for i in b:
#     print(i)

# usnig range datatypes print the positive & negative values.

# for i in range(5,50,5):
#     print(i,end =" ")
# for j in range(50,0,-5):
#     print(j, end =" ")

# for i in range(10,20,2):
#     print(i, end =" ")

i = list[list(range(10))]
print(i)
