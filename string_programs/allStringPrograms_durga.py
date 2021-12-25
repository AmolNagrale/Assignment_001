# WAP to find out positive & negative index according to the given string

# s = input("Enter the some string:")
# i=0
# for x in s:
#     print("The charecter present at positive index {} and at negative index {} is {}".format(i,i-len(s),x))
#     i=i+1
    
#=======================================================================

# Accessing charecters by using slicing operator

# s='Learning python is very very easy!!!'
# #print(s[::])
# print(s[-1:-10:-1])
#----------------------------------------------------------------------
# concatination & replication

# s = 'python is very easy language'
# s1 = ', But need to study hard'
# print(s+s1)
# print( s *5)

#=======================================================================

# s = 'Amol'
# print(len(s))

#=====================

#WAP to access each charecter of string in forword & backword direction by using while loop

# s = 'Learning python is very easy !!!\n'
# n = len(s)
# i=0
# #print(" Forword Direction")
# while i <n:
#     print(s[i],end="")
#     i+=1
# #print("\n Backword Direction")
# i=-1
# while i>=-n:
#     print(s[i],end="")
#     i-=1

#=============================

# s='python is very easy language !!'
# n= len(s)
# i=0
# while i<n:
#     print(s[i], end="")
#     i=i+1
# i=-1
# while i>=-n:
#     print(s[i],end="")
#     i=i-1

# Alternate method

# s = 'python is very easy language '
# for i in s:
#     print(i, end="")
#     
# print("\nForword Direction")
# for i in s[::]:
#     print(i, end="")
#     
# print("\nBackword Direction")
# for i in s[::-1]:
#     print(i, end="")
#     
#================================

#checking Membership
# 
# s = 'Durga'
# print('D' in s)
# print('d' in s)
# print('z' in s)

#====================================
# comparision program

# s1 = input("Enter the first string :")
# s2 = input("Enter the second string :")
# if s1==s2:
#     print("Both string are equal")
# elif s1>s2:
#     print("S1 is greater than s2")
# else:
#     print("s1 is less than s2")

#===================================

#Remove spaces from the string
# 
# city = input("Enter the city name :")
# scity = city.strip()
# if scity=='Hyadrabad':
#     print("Hello Hyadrabadi.. Adab")
# elif scity=='Chennai':
#     print("Hello Madrasi...Vanakkam")
# elif scity=='Banglore':
#     print("Hello Kannadiga..Shubhodaya")
# else:
#     print("Your entered city is invalid")
    
#============================================
    
# WAP to print giver string forword & Backword direction

# s = 'Django learning is very easy, but you know the basic concept of python '
# print('Forword Direction')
# print(s[::])
# print('\nBackword Direction')
# print(s[::-1])

# s = 'Django learning is very easy, but you know the basic concept of python '
# n = len(s)
# print('Forword Direction')
# i=0
# while i<n:
#     print(s[i], end="")
#     i+=1
# print('\nBackword Direction')
# i=-1
# while i>-n:
#     print(s[i], end="")
#     i-=1

#========================================

# finding substring

# for forword direction
#find() & index()

# for Backword direction
#rfind() & rindex()

# s = 'Learning python is very easy'
# print(s.find("python"))
# print(s.find("java"))
# print(s.find("r"))
# print(s.rfind("r"))

 # we can find out the string by using srart & end limits also

# s = 'durgaravipawanshiva'
# print(s.find('a'))
# print(s.find('a',7,15))
# print(s.find('z',7,15))

#=============================================
# index() method
# s = input('Enter the main string : ')
# subs= input('Enter the sub string : ')
# try:
#     n=s.index(subs)
# except ValueError:
#     print('substring not found')
# else:
#     print('substring found')

#==============================================

# WAP to display all positions of substring in a given main string

# s = input("Enter main string : ")
# subs = input("Enter sub-string :")
# flag=False
# pos=-1
# n=len(s)
# while True:
#     pos=s.find(subs,pos+1,n)
#     if pos==-1:
#         break
#     print('found at position',pos)
#     flag=True
# if flag==False:
#     print("Not Found")

#=============================================
# counting substring in the given string
# s = 'ababccasdasab'
# print(s.count('a'))
# print(s.count('s'))
# print(s.count('a',3,7;))

#==============================================

#replacing string
# s = 'learning python is very difficult'
# s1 = s.replace('difficult','easy')
# print(s)
# print(id(s))
# print(id(s1))
# print(id(s))
#======================================

# s = 'learning python is very easy'
# l=s.split()
# print(l)

# txt = "welcome to the jungle"

# x = txt.split()

# print(x)

#======================================
# WAP to reverse internal content of each word

#1. using for loop

# s = 'durga software solution'
# n = s.split()
# for i in n:
#     print(i[::-1], end=" ")

# # alternate using for loop
# s = 'durga software solutions'
# n = s.split()
# l=[]
# for i in n:
#     l.append(i[::-1])
# output=' '.join(l)
# print(output)

# # using while loop

# s = 'durga software solution'
# l = s.split()
# l1 = []
# i = 0
# while i<len(l):
#     l1.append(l[i][::-1])
#     i=i+1
# output=' '.join(l1)
# print(output)

#======================================

# # changing the case of strings

# s = 'learning python is very easy || LEARNING PYTHON IS VERY EASY'
# print(s.lower())
# print(s.upper())
# print(s.title())
# print(s.swapcase())
# print(s.capitalize())

#==========================================

# checking the start & end part of string 

# s = 'python is very easy language'
# print(s.startswith('python'))
# print(s.startswith('is'))
# print(s.endswith('e'))

# get the output in True & False only

#==========================================

# to check the types of charecter in strings

# print('Amol12334'.isalnum())
# print('Amol12334@#!&*'.isalnum())
# print('Amol'.isalpha())
# print('Amol12'.isalpha())
# print('amol'.islower ())
# print('amolN'.islower ())
# print('AMOL'.isupper())
# print('AMOLn'.isupper())
# print('Amol Is Good Employee'.istitle())
# print('Amol Is good Employee'.istitle())
# print(' Amol is good Employee  at TBW'.isspace())
# print('    '.isspace())

#==============================================================

# formating of strings
# name='Amol'
# salary=1000
# age=31
# print("{}'s salary is {} and his age is {} ".format(name,salary,age))
# print("{0}'s salary is {1} and his age is {2} ".format(name,salary,age))
# print("{x}'s salary is {y} and his age is {z} ".format(z=age,y=salary,x=name))

#==============================================================

# WAP to reverse the given strings

# s = 'Learning python is very easy'
# print(s[::-1])

# s = 'Learning python is very easy'
# print(''.join(reversed(s)))

# s ='Learning python is very easy'
# l=len(s)-1
# target=''
# i=0
# while i>0:
#     target=target+s[i]
#     i=i+1
# output=''.join(target)
# print(output)

#=============================================================

# s ='one two three four five six'
# l = s.split()
# i = 0 
# l1 =[]
# while i < len(l):
#     if i%2==0:
#         l1.append(l[i])
#     else:
#         l1.append(l[i][::-1])
#     i = i+1
# output =' '.join(l1)
# print(output)


#=============================================================
# WAP to print odd position & even position charecters

# s = input("Enter sone string : ")
# i = 0
# print("Charecter at Even position : ")
# while i < len(s):
#     print(s[i],end=",")
#     i=i+2
# print()
# print("Charecter at odd position : ")
# i=1
# while i < len(s):
#     print(s[i], end=",")
#     i=i+2
# print()

# Alternate way

# s = input("Enter some string : ")
# print('Charecters at Even position', s[0::2])
# print('Charecters at odd position', s[1::2])

#============================================================

# WAP to sort the charecters of the string and first alphabet symbols followed by numeric value
#s = input('Enter the some string :')
# s = 'B4A1D3@#$'
# s1=s2=output=""
# for x in s:
#     if x.isalpha():
#         s1=s1+x
#     else:
#         s2=s2+x
# for x in sorted(s1):
#      output=output+x
# for x in sorted(s2):
#     output=output+x
# print(output)
        
#=========================================================

# s = 'a4k3b2w24'
# output=''
# for x in s:
#     if x.isalpha():
#         output=output+x
#         previous=x
#     else:
#         output=output+chr(ord(previous)+int(x))
# print(output)

#========================================================

s = 'ABGHHYTFGHFDSAA'
d={}
for x in s:
    if x not in l:
        l.append(x)
output= "".join(l)
print(output)
