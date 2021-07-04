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

# def fibonacci(xterms):
#     # first two terms
#     x1 = 0
#     x2 = 1
#     count = 0
# 
#     if xterms <= 0:
#         print("Please provide a +ve integer")
#     elif xterms == 1:
#         print("Fibonacci seq upto",xterms,":")
#         print(x1)
#     else:
#         while count < xterms:
#             xth = x1 + x2
#             x1 = x2
#             x2 = xth
#             count += 1
#             yield xth
# 
# fib = fibonacci(5)
# 
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# print(next(fib))
# #print(next(fib)) # more than 5th time approche will get error (StopIteration)

#===================================================================================

# Demonstrate Python Generator Expression

# Define the list
# alist = [4, 16, 64, 256]
# 
# # Find square root using the list comprehension
# out = [a**(1/2) for a in alist]
# print(out)
# 
# # Use generator expression to calculate the square root
# out = (a**(1/2) for a in alist)
# print(out)
# print(next(out))
# print(next(out))
# print(next(out))
# print(next(out))
# #print(next(out))
#      
#===================================================================================

# Generator next() Method Demo
#
# alist = ['Python', 'Java', 'C', 'C++', 'CSharp']
# def list_items():
#     for item in alist:
#         yield item
# 
# gen = list_items()
# 
# iter = 0
# 
# while iter < len(alist):  
#     print(next(gen))
#     iter += 1
#     
    
#==================================================================================

# Generator For Loop Demo
#
# alist = ['Python', 'Java', 'C', 'C++', 'CSharp']
# def list_items():
#     for item in alist:
#         yield item
# 
# gen = list_items()
# 
# for item in gen:
#     print(item)

#==================================================================================

# Python Generator Function with Multiple Yield

# def testGen():
#     x = 2
#     print('First yield')
#     # Generator function has many yield statements
#     yield x
# 
#     x *= 1
#     print('Second yield')
#     yield x
# 
#     x *= 1
#     print('Last yield')
#     yield x
# 
# # Call the generator
# iter = testGen()
# 
# # Invoke the first yield
# next(iter)
# 
# # Invoke the second yield
# next(iter)
# 
# # Invoke the last yield
# next(iter)

#==================================================================

# Generate Arithmetic Progression Using Iterator Class
# 
# class AP:
#     def __init__(self, a1, d, size):
#         self.ele = a1
#         self.diff = d
#         self.len = size
#         self.count = 0
# 
#     def __iter__(self):
#         return self
# 
#     def __next__(self): 
#         if self.count >= self.len:
#             raise StopIteration
#         elif self.count == 0:
#             self.count += 1
#             return self.ele
#         else:
#             self.count += 1
#             self.ele += self.diff
#             return self.ele
# 
# for ele in AP(1, 2, 10):
#     print(ele)


# Generate Arithmetic Progression Using Generator Function
 
# def AP(a1, d, size):
#     count = 1
#     while count <= size:
#         yield a1
#         a1 += d
#         count += 1
# 
# for ele in AP(1, 2, 10):
#     print(ele)

#===========================================================================
 # Find All Prime Numbers Using Generator
# 
# def find_prime():
#     num = 1
#     while True:
#         if num > 1:
#             for i in range(2, num):
#                 if (num % i) == 0:
#                     break
#             else:
#                 yield num
#         num += 1
#          # continously generate prime numbers, need to break iteration use 'ctrl+c'
# for ele in find_prime():
#     print(ele)
    
#==========================================================================
    
#Chain Multiple Operations Using Generator Pipeline

def find_prime():
    num = 1
    while num < 100:
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                yield num
        num += 1

def find_odd_prime(seq):
    for num in seq:
        if (num % 2) != 0:
            yield num

a_pipeline = find_odd_prime(find_prime())

for a_ele in a_pipeline:
    print(a_ele)

'''
Generators can produce a sequence on the fly and allow us to access one of its
items whenever we need it. While doing so, it doesn’t consume a lot of memory
and still gives us the ability to work with infinite streams of data. All in all,
it is a trickier programming concept and worth trying in projects.

'''






