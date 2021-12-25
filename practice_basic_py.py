# s= input("Enter the some string : ")
# l=[]
# for x in s:
#     if x not in l:
#         l.append(x)
#         print(l)
# output =''.join(l)
# #print(output)

#WAP to reverse the given string

# s = input("Enter the some string ")
# print(s[::-1])

# s= input("Enter some string :")
# # print(''.join(reversed(s)))
# i=len(s)-1
# target=''
# while i>0:
#     target=target+s[i]
#     i=i-1
# print(target)

# s = "Geeksforgeeks"
# str = ""
# for i in s:
#     str = i + str
#     str1 =''.join(str)
# print(str1)
#   

  
# print ("The original string  is : ",end="")
# print (s)
#   
# print ("The reversed string(using loops) is : ",end="")
# print (reverse(s))

# s = input("Enter the string :")
# l=s.split()
# l1=[]
# i=len(l)-1
# while i>0:
#     l1.append(l[i])
#     i-=1
# output=''.join(l1)
# print(output)

# s = input("Enter some string :")
# l = s.split()
# l1=[]
# i=0
# while i<lwn(l):
#     l1.append(l(i)[::-1])
#     i=i+1
# output=''.join(l1)
# print(output)

# n = int(input("Enter the number of students :"))
# d = {}
# for i in range(n):
#     name=input("Enter Student Name:")
#     marks=input("Enter Student marks:")
#     d[name]=marks
# while True:
#     name=input("Enter student name to get marks:")
#     marks=d.get(name,-1)
#     if marks==-1:
#         print("Student not found")
#     else:
#         print("The Marks of",name,"are",marks)
#     option=input("Do you want find anather student marks[Yes|No]")
#     if option=="No":
#         break
# print("Thanks for using our application !!")

# color = input("Enter the favorate color :")
# if (color=="Blue"):
#     print("This is my favorate color")
# elif(color=="Yellow"):
#     print("This not my favrate color")
# else:
#     print("This is the common color, which can be like anyone !!")

# n1 = int(input("Enter the first number:"))
# n2 = int(input("Enter the second number:"))
# if (n1>n2):
#     print("First number is larger than second number !!")
# elif(n1<n2):
#     print("Second number is larger than First number !!")
# else:
#     print("Both the numbers are same !!")

# n1 = int(input("Enter any number :"))
# if n1%2==0:
#     print("Given number is even !!")
# else:
#     print("Given  number is odd number !!")


# n = int(input("Enter any number :"))
# if n>=1 and n<=100:
#     print("The number",n,"is between 1 to 100 ")
# else:
#     print("The number",n," is out of range !!")
#

# n = int(input("Enter a digit from 0 to 9 :"))
# if n==0:
#     print("Zero")
# elif n==1:
#     print("One")
# elif n==2:
#     print("Two")
# elif n==3:
#     print("Three")
# elif n==4:
#     print("Four")
#     
# else:
#     print("Please enter a number between 1 to 9 !!!")

# x = 1
# while x<=10:
#     print(x)
#     x = x+1
# 
# for x in range(1,11):
#     print(x)

# n = int(input("Enter Number :"))
# sum=0
# i=1
# while i<=n:
#     sum=sum+i
# print("The sum of first",n,"number is :",sum)
# 
# name = ""
# while name!="durga":
#     name=input("Enter Name :")
# print("Thanks for confirmation !!")
 
# 
# i=0
# while True:
#     i=i+1
#     print("Hello")
    
    
# for i in range(10):
#     for j in range(10):
#         print("i=",i,"j=",j)
#         

# n = int(input("Enter the number of rows"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

# n = int(input("Enter number of rows :"))
# for i in range(1, n+1):
#     print(" "*(n-i),end="")
#     print("*"*i)
    
# for i in range(10):
#     if i==4:
#         print("The procesing is enough ..please break")
#         break
#     print(i)
#     
# cart = [10,20,30,40,600,70,80]
# for item in cart:
#     if item>80:
#         print("To please this order insurance must be required !!")
#         break
#     print(item)

# for i in range(11):
#     if i%2==0:
#         continue
#     print(i)

# cart=[10,20,30,600,40,50]
# for item in cart:
#     if item>=500:
#         print("We cannot process this order")
#         break
#     print(item)
# else:
#     print("Congrats ....all items processed successfully ")

# factorial number :
# def factorial(n):
#     if n==0:
#         result=1
#     else:
#         result=n*factorial(n-1)
#     return result
# print("Factorial of 4 is", factorial(4))
# print("Factorial of 4 is", factorial(5))

#fabonacci series

# def fib():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b
# for f in fib():
#     if f>100:
#         break
#     print(f)


# range of numbers

# for i in range(0,20,5):
#     print(i, end=" ")
# for j in range(25,0,-5):
#     print(j, end=" ")

# n=0
# while True:
#     n=n+1
#     print(n)

# s = input("Enter the string :")
# i = 0
# for x in s:
#     
#     print("The charecter present in the positive index {} and at negative index {} is {}".format(i,i-len(s),x))
#     i=i+1
#     
# s = "Amol is very itelligent employee !!"
# print(s[0:50:3])


# i = input("Enter the string :")
# print(i*5)

# s = "Learning python is very easy !!"
# n =len(s)
# i=0
# print("Forword direction !!")
# while i<n:
#     print(s[i],end="")
#     i+=1
#     
# print("Backword direction !!")
# i=-1
# while i>=-n:
#     print(s[i],end="")
#     i-=1

# s = "Learning python is very easy "
# print("Forword Direction")
# for i in s[::-1]:
#     print(i,end="")
    
# print("Forword direction")
# for i in s[::]:
#     print(i, end="")
#     
# print("Backword direction")
# for i in s[::-1]:
#     print(i, end="")

# s = "abbbbbbaaaabbaaa"
# subs = s.replace("b","a")
# print(subs)

# s = "durga software solutions"
# l=s.split("-")
# for x in l:
#     print(x)

# t = ["sunnychinny"]
# i = len(t)
# print(i)

# list = []
# list.append("A")
# list.append("B")
# list.append("C")
# list.append(10.5)
# list.append(True)

l = [6,1,2,3,4,5]
#a=l[::-1]
#l.insert(6,444)
l.sort()
print(l)
