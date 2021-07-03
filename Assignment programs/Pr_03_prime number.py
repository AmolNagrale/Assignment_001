# Python program to print all Prime numbers in an Interval

'''A prime number is a natural number greater than 1 that has
no positive divisors other than 1 and itself.
The first few prime numbers are {2, 3, 5, 7, 11, ….}.'''

# Python program to print all

# number should be greater than 1

start = 11
end = 25

for i in range(start, end+1): #------------printing 11 to 25 numbers
   # print(i)
    if i>1:
        for j in range(2,i): #-------------printing 2 to end value numbers
            print(j)
             
            
            if(i % j==0): # ---------------checking remaider will be 0
                break
        else:
            print(i)


            


