# fibonacci series 

def fib():
    a,b=0,1
    while True:
        yield a
        a,b=b,a+b
for f in fib():
    if f>100:
        break
    print(f)
    
# To generate first n numbers:

# def firstn(num):
#     n=1
#     while n>=1:
#         yield n
#         n=n+1
#         
# values=firstn(5)
# for x in values:
#     print(x)
#     break

###########################################################################
# using generator function 
# i = (x*x for x in range(100000000000000))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

# Using normal function

# i = [x*x for x in range (10000000000)]
# print(i[0])

##########################################################################





     
     
