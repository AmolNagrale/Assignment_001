class A:
    def m1(self):
        print("A class Method")
class B(A):
     #def m1(self):
        #print("B class Method")
    pass
class C(A):
     #def m1(self):
        #print("C class Method")
    pass
class D(B,C):
    #def m1(self):
        #print("D class Method")
    pass
d = D()
d.m1()
