# def even_odd(x):
#     if x%2 == 0:
#         print("{} number is even ".format(x))
#     else:
#         print("{} number is odd ".format(x))
#     
# even_odd(5)
# even_odd(6)

#================================================================

# def f1(num):
#     result=1 # initialise result for output storing element
#     while num>=1:  
#         result = result*num 
#         num = num-1
#     return result
# 
# for i in range(1,6):
#     print(" The factorial of",i,"is :",f1(i))
#     
#=================================================================
    
#Returning multiple values in function
    
# def sum_sub(a,b):
#     sum = a+b
#     sub = a-b
#     return sum,sub
# 
# print(sum_sub(100,20))

#================================================================
# 
# def calc(x,y):
#     sum = x+y
#     sub = x-y
#     mul = x*y
#     div = x/y
#     fdiv = x//y
#     mod = x%y
#     return sum,sub,mul,div,fdiv,mod
# 
# print(calc(100,20))

#=================================================================
def sub (b,a):
    print(b-a)
    
sub(200,100)