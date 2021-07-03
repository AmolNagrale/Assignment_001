# fibonacci series 

# def fib():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b
# for f in fib():
#     if f>100:
#         break
#     print(f)
    
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

# generator

# l = (x*x for x in range(10))
# for x in l:
#    # print(x) # generator concept  # This approche is not store a data directly to memory location, hence generator used paranthersis()
#     print(l)
#     
    
# l = [x*x for x in range(10)] 
# for x in l:
#     #print(x) # MemoryError :- dirctly store the data in memory, hence memoryerror will occured.
#     print(l)

#=========================================================================
# Generator vs normal collections wrt performance :

# import random
# import time
# 
# names = ['sunny','bunny','channy','vinny']
# subjects = ['python','java','hadoop']
# 
# def people_list(num_people):
#     results = []
#     for i in range (num_people):
#         person = {'id':i,
#                   'name': random.choice(names),
#                   'subjects':random.choice(subjects)
#                   }
#         results.append(person)
#     return results
# 
# # def people_generator(num_people):
# #     for i in range(num_people):
# #         person = {'id':i,
# #                   'name': random.choice(names),
# #                   'subjects':random.choice(subjects)
# #                   }
# #     yield person
# 
# t1 = time.clock()
# person = people_list(10000000)
# t2 = time.clock()


# t1 = time.clock()
# person = people_generator(10000000)
# t2 = time.clock()


#print('Took {}'.format(t2-t1))
    
#===================================================================================

# Demonstrate Python Generator Function

def fibonacci(xterms):
    # first two terms
    x1 = 0
    x2 = 1
    count = 0

    if xterms <= 0:
        print("Please provide a +ve integer")
    elif xterms == 1:
        print("Fibonacci seq upto",xterms,":")
        print(x1)
    else:
        while count < xterms:
            xth = x1 + x2
            x1 = x2
            x2 = xth
            count += 1
            yield xth

fib = fibonacci(5)

print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
print(next(fib))
#print(next(fib)) # more than 5th time approche will get error (StopIteration)


     
     
