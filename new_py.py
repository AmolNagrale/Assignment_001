# def decor(func):
#     def inner(name):
#         print("Decorator1 exicuting...")
#         func(name)
#     return inner
# 
# def decor1(func):
#     def inner(name):
#         print("Decorator2 executing...")
#         func(name)
#     return inner
# 
# @decor1 # input is return value of decor, means first exicute & print value
# @decor  # input is return value from main function (wish). Exicutating & print final value

# def wish(name):
#     print("Hello",name,"Good Morning")
# wish("Durga") # finally wish function will exicuted

#==============================================
def doubledecor(func):
    def inner():
        x = func()
        return 2*x
    return inner

def squaredecor(func):
    def inner():
        x = func()
        return x*x
    return inner

@doubledecor # input is return value of sqauredecor & final 2*100 = 200 
@squaredecor # input from main function (num), 10*10 = 100
 
def num():
    return 10
print(num()) # 200 is final o/p.
