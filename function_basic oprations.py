def calc(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b
    return sum,sub,mul,div
t=calc(10,5)
print("The result are :",t)
print(type(t))
#for i in t:
#     print(i)