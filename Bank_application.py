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
    print("d-Deposit \n w-Withdrow \n e-exit")
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
    
    