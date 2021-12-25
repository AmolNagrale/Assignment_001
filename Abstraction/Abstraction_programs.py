#Examples from Geeky show

# from abc import ABC, abstractmethod
# 
# class Father(ABC):
#     @abstractmethod
#     def disp(self):
#         pass
#     
#     def show(self):
#         print('Concreate Method')
#     
# class Child(Father):
#     def disp(self):
#         print('Child class')
#         print('Defining Abstract class')
#         
# 
# c = Child()
# c.disp()
# c.show()

#=================================================================================
#Examples from Geeky show

# from abc import ABC, abstractmethod
# 
# class Defenceforce:
#     @abstractmethod
#     def area(self):
#         pass
#     
#     def gun(self):
#         print("Gun = AK-47")
#         
# class Army(Defenceforce):
#     def area(self):
#         print("Army area = Land")
#         
# class Airforce(Defenceforce):
#     def area(self):
#         print("Airforce area = Sky ")
#         
# class Navy(Defenceforce):
#     def area(self):
#         print("Navy area = Sea ")
#         
# a = Army()
# ar = Airforce()
# n = Navy()
# 
# a.area()
# a.gun()
# print()
# ar.area()
# ar.gun()
# print()
# n.area()
# n.gun()

#=========================================================================

# from abc import ABC, abstractmethod
# 
# class Defenceforce:
#     @abstractmethod
#     def __init__(self,batch):
#         self.batch = batch # for individual asign the value 
#         self.id = 1857 # common id use for all child class
#         
#     def area(self):
#         pass
#     
#     def gun(self):
#         print("Gun = AK-47",self.id)
#         
# class Army(Defenceforce):
#     def area(self):
#         print("Army area = Land",self.batch)
#         
# class Airforce(Defenceforce):
#     def area(self):
#         print("Airforce area = Sky ",self.batch)
#         
# class Navy(Defenceforce):
#     def area(self):
#         print("Navy area = Sea ",self.batch)
#         
# a = Army('A')
# ar = Airforce('B')
# n = Navy('C')
# 
# a.area()
# a.gun()
# print()
# ar.area()
# ar.gun()
# print()
# n.area()
# n.gun()
# 
# # I have used constructor in this example for initiatizing the batch no's as per defence sections

#===========================================================================================

# Interface
#We use interface when all the features need to be implimented differently for different objects.

# from abc import ABC, abstractmethod
# 
# class Defenceforce:
#     @abstractmethod
#     def area(self):
#         pass
#     @abstractmethod
#     def gun(self):
#         pass
#         
# class Army(Defenceforce):
#     def area(self):
#         print("Army area = Land")
#     def gun(self):
#         print('Gun = AK-41')
#         
# class Airforce(Defenceforce):
#     def area(self):
#         print("Airforce area = Sky ")
#     def gun(self):
#         print('Gun = AK-42')
#         
# class Navy(Defenceforce):
#     def area(self):
#         print("Navy area = Sea ")
#     def gun(self):
#         print('Gun = AK-43')
#         
# a = Army()
# ar = Airforce()
# n = Navy()
# 
# a.area()
# a.gun()
# print()
# ar.area()
# ar.gun()
# print()
# n.area()
# n.gun()

#=====================================================

class Account:
    def __init__(self,name,balence,min_balence):
        self.name=name
        self.balence = balence
        self.min_balence = min_balence
        
def deposit(self,amount):
    self.balence = self.balence+amount
    
def withdrow(self,amount):
    if self.balence-amount>= self.min_balence:
        self.balence=self.balence-amount
    else:
        print('Sorry, InSufficient-Funds')
        
    def print_statement(self):
        print('Account Balence:',self.balence)
        
    def print_statement(self):
        print('Account Balence:',self.balence)

class CurrentAccount(Account):
    def __init__(self,name,balence):
        super().__init__(name,balence,min_balence=-1000)
        
    def __str__(self):
        return "{}'s Saving Account Balence:{}".format(self.name,self.balence)
    
c = CurrentAccount('Durga',10000)
print(c)
#c.deposit(10000)
print(c)
c.withdrow(20900)
print(c)
