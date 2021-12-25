# class Student:
#     def __init__(self):
#         self.name='Amol'
#         self.age=30
#         self.marks=100


#     def talk(self):
#         print("The name of the student is :", self.name)
#         print("The age of the student is: ", self .age)
#         print("The marks of the student is :",self.marks)

# a=Student()
# print(a.talk())

#===================================================================

class Student:
    def __init__(self, name, rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks

    def disp(self):
        print("The name of the student is :",self.name)
        print("The rollno of the student is :",self.rollno)
        print("The marks of the student is :",self.marks)

st=Student('Amol',10,100)
st.disp()

#====================================================================

# class Student:
#     '''This is the student class with required data'''
#     def __init__(self,x,y,z):
#         self.x=x
#         self.y=y
#         self.z=z

#     def display(self):
#         print('Student Name:{}\nRollno\nMarks:{}'.format(self.x,self.y,self.z))

# s1=Student('Amol',10,20)
# s1.display()
# s2=Student('Amit',30,40)
# s2.display()

#====================================================================

# class Employee:
#     def __init__(self):
#         self.eno=100
#         self.ename='Amol'
#         self.esal=1000
# e=Employee()
# print(e.__dict__)

#===================================================================

