# class Duck:
#     def talk(self):
#         print('Quack Quack...')
#         
# class Dog:
#     def talk(self):
#         print('Bow Bow...')
#         
# class Cat:
#     def talk(self):
#         print('Meow Meow..')
#         
# class Goat:
#     def talk(self):
#         print('Myaah Myaah...')
#         
# def f1(obj):
#     obj.talk()
#     
# l = [Duck(),Dog(),Cat(),Goat()]
# for obj in l:
#     f1(obj)
#     
#==============================================

class Duck:
    def talk(self):
        print('Quack Quack...')
        
class Dog:
    def bark(self):
        print('Bow Bow...')
        
      
def f1(obj):
    obj.talk()

d1 = Dog()
d1.talk() # AttributeError: 'Dog' object has no attribute 'talk'

'''To overcome this issue we need to hasattr(obj,'attributename')'''

class Duck:
    def talk(self):
        print('Quack Quack...')
        
class Dog:
    def bark(self):
        print('Bow Bow...')
        
      
def f1(obj):
    
    if hasattr(obj,'talk'):
        obj.talk()
    elif hasattr(obj,'bark'):
        obj.bark()
        
d = Duck()
f1(d)


