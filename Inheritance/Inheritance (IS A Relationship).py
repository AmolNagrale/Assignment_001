# class P:
#     a = 10
#     def __init__(self):
#         self.b = 20
#         
# class C(P):
#     c = 30
#     def __init__(self):
#         super().__init__()
#         self.d = 40
#     
# c = C()
# print(c.a,c.b,c.c,c.d)

#=============================================

#Types of Inheritance

# Single inheritance

# class P:
#     def m1(self):
#         print("Parent Method")
#         
# class C(P):
#     def m2(self):
#         print("Child Method")
# 
# c = C()
# c.m1()
# c.m2()

#============================================

# multi level inheritance

# class P:
#     def m1(self):
#         print('Parent Method')
# 
# class C(P):
#     def m2(self):
#         print('Child Method')
#         
# class CC(C):
#     def m3(self):
#         print("Sub child method")
#         
# c = CC()
# c.m1()
# c.m2()
# c.m3()

#=============================================
# hieraechical Inheritance

# class P:
#     def m(self):
#         print("parent Method")
#         
# class C1(P):
#     def m11(self):
#         print("child method")
#         
# class C2(P):
#     def m22(self):
#         print("Second child method")
#         
# c1 = C1()
# c2 = C2()
# c1.m()
# c1.m11()
# c2.m()
# c2.m22()
#

#===============================================

#multiple Inheritance
# class P1:
#     def m1(self):
#         print("P1 Method")
# 
# class P2:
#     def m2(self):
#         print("P2 Method")
#         
# class C(P1,P2):
#     def m3(self):
#         print("Child method")
#         
# c = C()
# c.m1()
# c.m2()
# c.m3()

#============================================
'''If both the parent has same methods in that condition
python will consider order of parent class'''

# class P1:
#     def m1(self):
#         print("P1 method ")
#         
# class P2:
#     def m1(self):
#         print("P2 Method ")
#         
# class C(P2,P1):
#     def m2(self):
#         print("Child Method ")
#         
# c = C()
# c.m1()
# c.m2()

#==============================================

#Hybrid Inheritance

#==============================================

#Cyclic Inheritance

class P1(P2):
    #def m1(self):
        #print("P2 is a parent of P1 child !!! ")
    pass

class P2(P1):
    #def m2(self):
        #print("P1 is a parent of P2 child !!! ")
    pass

p1 = P1()
p2 = P2()
p1.m1()
p1.m2()
p2.m1()
p2.m2()
