class Engine:
    a = 10
    def __init__(self):
        self.b = 20
        
    def m1(self):
        print("Engine Specific functionality")
        
class Car:
    def __init__(self):
        self.e=Engine()
        
        
    def m2(self):
        print("Class Car using Engine class function")
        print(Engine.a)
        print(self.e.b)
        self.e.m1()

c = Car()
c.m2()