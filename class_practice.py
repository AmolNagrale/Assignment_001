# inside constructor by using self keyword

#class Test:
#     def __init__(self):
#         self.ename = 'Amol'
#         self.eno = 100
#         self.addr = 'aaaaaaa'
# 
# t = Test()
# print(t.__dict__)
    
#=====================================================

#2 . Inside instance method by using self variable

# class Test:
#     def __init__(self):
#         self.a = 10
#         self.b = 20
#         self.c = 30
#         
#     def m1(self):
#         self.d = 40
#         self.e = 50
# 
# t = Test()
# t.m1()
# print(t.__dict__)

#====================================================

#3. outside of the class by using object refrance
# 
# class Test2:
#     def __init__(self):
#         self.a = 10
#         self.b = 20
#         self.c = 30
#         
#     def m2(self):
#         self.d = 40
#         self.e = 50
#         
# t = Test2()
# t.m2()
# t.f = 50
# t.g = 60
# print(t.__dict__)

#======================================================

# How to access instance variable

# class Test:
#     def __init__(self):
#         self.a = 10
#         self.b = 20
#         self.c = 30
#         
#     def display(self):
#         print(self.a)
#         print(self.b)
#         print(self.c)
#         
# t = Test()
# t.display()
# print(t.a,t.b,t.c) # we have access veriable by using instance veriable

#=============================================================

# How to delete instance veriable from the class

# class Test1:
#     def __init__(self):
#         self.a = 10
#         self.b = 20
#         self.c = 30
#         
#     def std(self):
#         print(self.a)
#         print(self.b)
#        
#         
# t = Test1()
# t.std()
# del t.a
# print(t.__dict__)
#         
#=================================================================

# practice on static veriable

# class Test:
#     x = 10
#     def __init__(self):
#         self.y = 20
#         
# 
# t1 = Test()
# t2 = Test()
# print('t1 =',t1.x,t1.y)
# print('t2 =',t2.x,t2.y)
# t2.x = 888
# t1.y = 777
# print('t1 =',t1.x,t1.y)
# print('t2 =',t2.x,t2.y)

#=================================================================

# Various places to declare static variable
# dirctly inside class
# inside constructor by using class name
# inside the method by using class name
# inside class method by using class name/veriable name'cls'
# inside static method by using class name



# class Test:
#     a = 10      # directly inside class
#     def __init__(self):
#         Test.b = 20 # inside constructor by using class name
#         Test.c = 30
#         self.d = 40 
#     def m1(self):
#         Test.e = 50 # inside method by using class name
#     @classmethod   
#     def m2(cls):
#         Test.f = 60 #inside class method by using class name
#         cls.g = 70  #inside class method by using 'cls' veriable name
#     @staticmethod
#     def m3():   
#         Test.h = 80 # inside static method by using class name
# 
# print(Test.__dict__)
# t = Test()
# print(Test.__dict__)
# t.m1()
# print(Test.__dict__)
# Test.m2()
# print(Test.__dict__)
# Test.m3()
# print(Test.__dict__)
# Test.i = 90
# print(Test.__dict__)


#==========================================================================

# how to access static veriables
# inside constructor : by using either self or classname 
# inside instance method : by using either self or classname
# inside class method : by using either cls variable or classname
# inside static method : by using class name        
# From outside of class : by using classname      
# From outside of class : by using either object refrance or class name        
   
   
# class Test:
#     a = 10
#     def __init__(self):
#         print(self.a)
#         print(Test.a)
#     def m1(self):
#         print(self.a)
#         print(Test.a)
#     @classmethod
#     def m2(cls):
#         print(cls.a)
#         print(Test.a)
#     @staticmethod
#     def m3():
#         print(Test.a)
# print(Test.__dict__)
# t = Test()
# print(t.a)
# t.m1()
# t.m2()
# t.m3()

#====================================================================

# Where we can modify the value of static variable

# class Test:
#     a = 10
#     
#     @classmethod
#     def m3(cls):
#         cls.a = 1010
#         
#     @staticmethod
#     def m2():
#         Test.a = 999
#         
# print(Test.a)
# Test.m3()
# print(Test.a)
# Test.m2()
# print(Test.a)

#==============================================================================

# Bank application:

import sys

class Customer:
    '''Customer class with bank operations'''
    bankname = 'Janata Sahakari Bank'
    def __init__(self,name,balence= 0.0):
        self.name = name
        self.balence = balence
        
    def deposit(self,amt):
        self.balence = self.balence+amt
        print("Balence after deposit :",self.balence)
        
    def withdrow(self,amt):
        if amt>self.balence:
            print("Insufficient amount can't perform this operation")
            sys.exit()
        self.balence = self.balence-amt
        print("Balence after withdrow amount",self.balence)
print("Welcome to ",Customer.bankname)
name = input(" Enter your Name :")
c = Customer(name)
while True:
    print("d-Deposit \n w-Withdrow \ne-exit")
    option = input("choose your option :")
    if option == 'd' or option == 'D':
        amt = float(input('Enter amount :'))
        c.deposit(amt)
    elif option == 'w' or option == 'W':
        amt = float(input("Enter amount :"))
        c.withdrow(amt)
    elif option == 'e' or option == 'E':
        print("Thanks for Banking !!!!! ")
        sys.exit()
    else:
        print('Invalid option ......please choose valid option')
    
    

        



















