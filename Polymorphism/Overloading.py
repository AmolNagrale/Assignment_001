# class Book:
#     def __init__(self,pages):
#         self.pages = pages
#         
#     def __add__(self,other):
#         return self.pages + other.pages 
#     
# b1 = Book(100)
# b2 = Book(200)
# 
# 
# 
# print("The total numbers of pages:",b1+b2)

#====================================================
# Example on how to add more than two object contents..
# class Book:
#     def __init__(self,pages):
#         self.pages = pages
#         
#     def __add__(self,other):
#         print('add method calling...')
#         total = self.pages+other.pages
#         return Book(total)
#     
# #     def __str__(self):
# #         print('str method calling...')
# #         return str(self.pages)
# #         
# b1 = Book(100)
# b2 = Book(200)
# b3 = Book(300)
# b4 = Book(50)
# bx = b1+b2+b3+b4
# print(bx.pages)
# print('Total numbers of pages :',b1)
# print('Total numbers of pages :',b1+b2)
# print('Total numbers of pages :',b1+b2+b3)
# print('Total numbers of pages :',b1+b2+b3+b4)

#=============================================================

# class Students:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#         
#     def __str__(self):
#         return 'This is student with name {} and marks {} '.format(self.name, self.marks)
#     
# s1 = Students('Durga',100)
# s2 = Students('Sunny',200)
# print(s1)
# print(s2)

#================================================================

class Employee:
    def __init__(self,name,days):
        self.name = name
        self.days = days
    
    def __mul__(self,other):
        return self.days*other.salary
    
class TimeSheet:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        
t = Employee('Durga',25)
e = TimeSheet('Durga',500)
print('This month salary',t*e)

#===============================================
