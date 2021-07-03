def fact(num):
    result=1
    while num>=1:
        result=result*num
        num=num-1
    return result
for i in range(1,4):
    print("The factorial of",i,"is",fact(i))

# def sum_sub(a,b):
#     sum=a+b
#     sub=a-b
#     return sum,sub
# x,y=sum_sub(150,30)
# print("The sum is :",x)
# print("The sub is :",y)

# def mul_dev(a,b):
#     mul = a*b
#     div = a//b
#     return mul,div
# x,y=mul_dev(10,5)
# print("The multiplication is :",x)
# print("The division is :",y)

