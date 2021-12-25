# class P:
#     a = 10
#     def __init__(self):
#         self.b = 20
#         print(" P class Method ")
#         
# class C(P):
#     a = 777
#     def m1(self):
#         print(super().a)
#         print(self.b)
#         
# c = C()
# c.m1()

#=============================================

class P:
    a = 10
    d = 333
    def __init__(self):
        self.b = 20
           
class C(P):
    a = 777
    def m1(self):
        print(super().a)
        print(super().d)
        print(self.b)
        self.b = 888
        print(self.b)
        super().__init__()
        print(self.b)
                
c = C()
c.m1()

