# class Durgamath:
#     
#     @staticmethod
#     def add(x,y):
#         print("The sum :",x+y)
#         
#     @staticmethod    
#     def product(x,y):
#         print("The product :",x*y)
#         
#     @staticmethod   
#     def average(x,y):
#         print("The average :",(x+y)/2)
#         
# Durgamath.add(10,20)
# Durgamath.product(10,20)
# Durgamath.average(10,20)
# 
#===================================================

# class Employee:
#     def __init__(self,eno,ename,esal):
#         self.eno = eno
#         self.ename = ename
#         self.esal = esal
#     
#     def display(self):
#         print("Employee number",self.eno)
#         print("Employee Name ",self.ename)
#         print("Employee salary ",self.esal)
#         
# class Test:
#     def modify(emp):
#         emp.esal = emp.esal+10000
#         emp.display()
#         
#         
# e = Employee(100,'Amol',10000)
# Test.modify(e)

#===============================================================================

# Inner classes

# class Outer:
#     def __init__(self):
#         print("Outer class object creation ")
#         
#     class Inner:
#         def __init__(self):
#             print("Inner class object creation..")
#             
#         def m1(self):
#             print("Inner class method ")
#     
#     o = Outer() #outer class object
#     i = o.Inner # using outer class inner class object creation
#     i.m1() # using outer & inner class object call m1 method

#Note - We can define this way also i = Outer().Inner()
#       We can define this way also i = Outer().Inner().m1()

#====================================================================

# class Outer:
#     def __init__(self):
#         print("Outer class object creation ")
#         
#     class Inner:
#         def __init__(self):
#             print("Inner class object creation..")
#         
#         class InnerInner:
#             def __init__(self):
#                 print("InnerInner class object creation..")
#                 
#             def m1(self):
#                 print("Inner class method ")
# 
# Outer().Inner().InnerInner().m1()

#========================================================================

# class Human:
#     def __init__(self):
#         self.name = 'Amol'
#         self.head = self.Head()
#         self.brain = self.head.Brain()
#         
#     def display(self):
#         print('Hello',self.name)
#         self.head.talk()
#         self.brain.think()
#         
#     class Head:
#         def talk(self):
#             print("Talking....")
#             
#         class Brain:
#             def think(self):
#                 print("Thinking.....")
#         
#         
# h = Human()
# h.display()

#=========================================================================

# class Person:
#     
#     def __init__(self,name,dd,mm,yyyy):
#         self.name = name
#         self.Dob = self.Dob(dd,mm,yyyy)
#         
#     def display(self):
#         print("Name", self.name)
#         self.Dob.display()
#     
#     class Dob:
#         def __init__(self,dd,mm,yyyy):
#             self.dd = dd
#             self.mm = mm
#             self.yyyy = yyyy
#          
#         def display(self):
#             print('{}/{}/{}'.format (self.dd,self.mm,self.yyyy))
#         
# p=Person('Amol',30,8,1948)
# p.display()

#=================================================
# Nested method :- we can define method inside method
# To define method specific repeatedly required functionality..

# class Test:
#     def m1(self):
#         def calc(a,b):
#             print("The Sum :",a+b)
#             print("The product :",a*b)
#             print("The division :",a/b)
#             print("The differance :",a-b)
#             print()
#         
#         calc(10,20)
#         calc(100,200)
#         calc(1000,2000)
#         calc(10000,20000)
# t = Test()
# t.m1()
#             
#====================================================




        
        