# fruits = ['mango','cherry','banana']
# x,y,z = fruits
# print(x)
# print(y)
# print(z)
# 
# fruits = ('mango','cherry','banana')
# x,y,z = fruits
# print(x)
# print(y)
# print(z)

# print(bin(15))

# complex data types
# 
# a +bj

# b = True
# print(type(b))

# a = 10
# b = 2
# 
# 10>20>30

# x = 0
# while True:
#     x+=1
#     print("The programmer",x)
#    

# for i in range(4):
#     for j in range(4):
#         print("i=",i,"j=",j)

# n = int(input("Enter the number of rows: "))
# for i in range(1, n+1):
#     print("  *  "*i)
#

# n = int(input("Enter number of rows :"))
# for i in range(1, n+1):
#     for j in range(1, i+1):
#         print(" *",end=" ")
#     print()

# n = int(input("Enter number of rows:"))
# for i in range(1,n+1):
#     print(" "* (n-i),end="")
#     print("* "*i)

# cart = [10,20,600,70,60]
# for item in cart:
#         if item>500:
#             print("To place this order insurance must required")
#             break
#         print(item)

# for i in range(10):
#     if i%2==0:
#         continue
#     print(i)

# to print numbers from 1 to 10

# n = 1
# while n<=10:
#     print(n)
#     n+=1

#==========================================================

# s = input("Enter some string :")
# i = 0
# for x in s:
#     print("Charecter present at poaitive index :{} and at negative index :{} is {}".format(i,i-len(s),x))
#     i = i+1

#===========================================================

# l = list(range(0,10,2))
# print(l)
# print(type(l))

# l = 'Amol'
# s = list(l)
# print(s)

#============================================================

# s = 'Learning python is very easy'
# l = s.split()
# print(l)
# print(type(l))

#============================================================

# n = [1,2,3,4,5,6,7,8,9,0]
# print(n[2:7:2])
# print(n[4::2])

#============================================================

def fact(n):
    if n == 0:
        result = 1
    else:
        result = n*fact(n-1)
    return result


print("The factorial of given number is :",fact(5))
        












