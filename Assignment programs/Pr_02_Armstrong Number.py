# Python Program to check Armstrong Number

'''A positive integer of n digits is called an Armstrong number of order n (order is number of digits) if.'''

# for eg :-
# 
# Input : 153
# Output : Yes
# 153 is an Armstrong number.
# 1*1*1 + 5*5*5 + 3*3*3 = 153


# Python program to check Armstrong number using functions Example:-

num = int(input(" Enter the number :"))
sum = 0
temp = num
order = len(str(num)) #----------to find a length of input for order purpose

while temp>0:
    digit = temp % 10 # ---------we get remainder of input. It is last digit i/p. 
    #print("digit",digit)
    sum += digit**order  #-------expontial operation  
    #print("digit",digit)
    #print("sum",sum)
    temp//=10     # ---------------quatient value(point value skip)
    #print("temp",temp)
if num==sum:
    print("This is an Armstrong number: ", num)
else:
    print("This is not an Armstrong number: ", num)


'''Note :: The Armstrong numbers

1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407, 1634, 8208, 9474, 54748,
92727, 93084, 548834, 1741725, 4210818, 9800817, 9926315, 24678050, 24678051,
88593477, 146511208, 472335975, 534494836, 912985153, and 4679307774.'''
