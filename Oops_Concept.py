# class Student:
#     '''This is the students class need to required data'''
#     def __init__(self):
#         self.name = 'Amol'
#         self.age = 30
#         self.marks = 80
#         
#     def talk(self):
#         print("Hello I am",self.name)
#         print("My age is",self.age)
#         print("My marks are:",self.marks)


# class Student:
#     '''This is the students class need to required data'''
#     def __init__(self,name,age,marks):
#         self.name = name
#         self.age = age
#         self.marks = marks
#         
#     def talk(self):
#         print("Hello I am",self.name)
#         print("My age is",self.age)
#         print("My marks are:",self.marks)
#         
#s1 = Student('Amol',40,100)
#s1.talk()

#

# Example on normal constructor/method declaration

class Student:
    def __init__(self,eno,ename,esal,eaddr):
        self.eno = eno
        self.ename = ename
        self.esal = esal
        self.eaddr = eaddr
         
    def display(self):
        print("Employee number:",self.eno)
        print("Employee Name :",self.ename)
        print("Employee salary :",self.esal)
        print("Employee Address :",self.eaddr)
        print()
        
e1 = Student(100,'A',1000,'aaaa')
e2 = Student(200,'B',2000,'bbbb')
e3 = Student(300,'c',3000,'cccc')
e4 = Student(400,'D',4000,'dddd')
e5 = Student(500,'E',5000,'eeee')
e1.display()
e2.display()
e3.display()
e4.display()
e5.display()

#===========================================================

# if we are declare two constructor in that case we are trying to check which construxtor will exicute

# class Test:
#     def __init__(self):
#         print("No argument constructor ...")
#         
#     def __init__(self,x):
#         print(" One argument constructor ...")
#         
#     def __init__(self,x,y):
#         print("Two argument constructor...")
#         
# #t = Test()
# #t = Test(10)
# t = Test(10,20)

#===============================================================

# class Movie:
#     def __init__(self,name,hero,heroine,rating):
#         self.name = name
#         self.hero = hero
#         self.heroine = heroine
#         self.rating = rating
#         
#     def info(self):
#         print('movie name :',self.name)
#         print('hero name :',self.hero)
#         print('heroine name :',self.heroine)
#         print('movie rating :',self.rating)
#         print()
#         
# Movies = [Movie('Bahubali','Prabhas','Anushka', 99),
#           Movie('Spider','Mahesh','Rakul',98),
#           Movie('Rayees','Shahrukh','Sunny',97),
#           Movie('Sultan','Salman','Anukshka',96)]
#           
# 
# for Movie in Movies:
#     Movie.info()
#     
#=======================================================
    
# Types of veriables
'''
1. instance variable
2. static variable
3. local veriable'''

# 1. instance veriable

# class Employee:
#     def __init__(self):
#         self.eno = 100
#         self.ename = 'Amol'
#         self.esal = 10000
#         
# e = Employee()
# print(e.__dict__) # By using this this method we will get dictionary output
# print(e.eno)
# print(e.ename)

# inside instance method by using self variable

# class Test:
#     def __init__(self):
#         self.a = 10
#         self.b = 20
#         
#     def m1(self):
#         self.c = 30 # we are able to declare instance veriable outside of constructor
#     
# t = Test()
# t.m1()
# print(t.__dict__)
#===============================================================

 #outside of the class by using refrance veriable

# class Test:
#     def __init__(self):
#         self.a = 10
#         
#     def m1(self):
#         self.b = 20
# 
# t1 = Test()    # t1 instance/object created
# t2 = Test()    # t2 instance/object created 
# t1.m1()        # Added constructor method & normal method
# t2.x = 777     # declare new x veriable in t2 having a value of 777
# print(t1.__dict__)
# print(t2.__dict__)

#==================================================================
# How to access instance veriable

# class Test:
#     def __init__(self):
#         self.a = 10
#         self.b = 20
#         
#     def m1(self):
#         print(self.a)
#         print(self.b)
#         
# t = Test()
# t.m1()
# print(t.a)
# print(t.b)
# print(t.a, t.b)

#====================================================
# How to delete instance veriable

# class Test:
#     def __init__(self):
#         self.a = 10
#         self.b = 20
#         self.c = 30
#         self.d = 40
#         self.e = 50
#         
#         
#     def m1(self):
#         del self.b
#         
# t = Test()
# print(t.__dict__)
# t.m1()
# print(t.__dict__)
# del t.c
# print(t.__dict__)

#==============================================

# class Test:
#     def __init__(self):
#         self.a=10
#         
#     def m1(self):
#         self.a = 777 # override the a value instate of 10
#         self.b = 888
# t = Test()
# t.m1()
# print(t.__dict__)
# t.b = 999 # override the value of b
# t.c = 666
# print(t.__dict__) # {'a': 10, 'b': 999, 'c': 666}

#==================================================

#in that example we are confirm when object is created constructor instance veriable exicute once

# class Test:
#     def __init__(self):
#         self.a = 10
#         self.b = 20
#         
# t1 = Test()
# t1.a = 777
# t2 = Test()
# t2.b = 888
# print(t1.a, t1.b)
# print(t2.a, t2.b)

#=======================================================
# Static variable

# class Test:
#     a = 10
#     def __init__(self):
#         self.b = 20
#     
# t1 = Test()
# t1.b = 777
# Test.a = 888
# t2 = Test()
# print(t1.a, t1.b)
# print(t2.a, t2.b)

#================================================

