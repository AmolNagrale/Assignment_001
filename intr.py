# def fact(n):
#     if n==0:
#         result=1
#     else:
#         result = n*fact(n-1)
#     return result
# 
# print("The factorial of given number is :", fact(1))

l = [1,2,3,4,5,6,7,8,9,10]
l1 = list(filter(lambda x:x%2==0,l))
print(l1)