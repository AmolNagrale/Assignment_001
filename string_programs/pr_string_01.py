#string program using break statement in for loop

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#   if x == "banana":
#     break

#my code

# x = ["red","green","blue","yellow"]
# for i in x:
#     print(i, end=" ")
#     if i == "blue":
#         break

# continue statement

# fruits = ["banana","orange","mango","cherry"]
# for i in fruits:
#     if i == "mango":
#         continue
#     print(i)

# for loop using else condition
# 
# for i in range(11):
#     print(i)
# else:
#     print("iteration was finished !!")

#using break statements

# for x in range(6):
#   if x == 3: break
#   print(x)
# else:
#   print("Finally finished!")

#If the loop breaks, the else block is not executed.

#######################################################################

#Nested Loops

#A nested loop is a loop inside a loop.

#The "inner loop" will be executed one time for each iteration of the "outer loop":  

# adj = ["red :", "big :", "tasty :"]
# fruits = ["apple", "banana", "cherry"]
# 
# for x in adj:
#   for y in fruits:
#     print(x, y)
    
#######################################################################

# a = 200
# b = 33
# c = 500
# # if a > b and c > a:
# #  	print("Both conditions are True")
# if b < a or b > c:
# 	print("only one condition are true")

######################################################################

# #Python - Format - Strings
# 
# ''' Strings & numbers can't directly added,
# 
# But we can combine strings and numbers by using the format() method!
# 
# The format() method takes the passed arguments, formats them,
# 
# and places them in the string where the placeholders {} are:'''
# 
# age = 36
# 
# txt = "My name is John, and I am {}"
# 
# print(txt.format(age))

##########################################################################

#The format() method takes unlimited number of arguments, and are placed into the respective placeholders:

# quantity = 3
# itemno = 567
# price = 49.95
# 
# myorder = "I want {} pieces of item {} for {} dollars."
# 
# print(myorder.format(quantity, itemno, price))

#########################################################################

# subjects = 3
# sclass = 7
# Faculty = 9
# 
# mycls = " I have total{} subjects in this college, there are total {} classes & for managing {} Teachching faculty."
# 
# print(mycls.format(subjects,sclass,Faculty))

#########################################################################

