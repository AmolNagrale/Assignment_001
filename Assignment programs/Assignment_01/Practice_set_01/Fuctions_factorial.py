# def fact(n):
#     if n==0:
#         result =1
#     else:
#         result = n*fact(n-1)
#     return result
# 
# print("The factorial of given number:",fact(7))


def fact (n):
    if n==0:
        result=1
    else:
        result = (n*fact(n-1))
    return result

print("The recursive value of the giver number:",fact(3))
     