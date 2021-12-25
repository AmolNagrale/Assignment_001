# Python program to find largest
# number in a list
  
# # creating empty list
# list1 = []
#   
# # asking number of elements to put in list
# num = int(input("Enter number of elements in list: "))
#   
# # iterating till num to append elements in list
# for i in range(1, num + 1):
#     ele = int(input("Enter elements: "))
#     list1.append(ele)
#       
# # print maximum element
# print("Largest element is:", max(list1))


# class Test:
#     a = 10
#     def __init__(self):
#         self.b = 20
# 
# t1 = Test()
# print(t1.__dict__)
# t2 = Test()
# t1.c = 30
# t2.d = 40
# print(t1.__dict__)
# print(t2.__dict__)

# class Test:
#     a = 10
#     def __init__(self):
#         self.b=20
#         
# print(Test.a)


class Test:
    a = 10
    b = 20
    def __init__(self):
        self.a = 30
        self.b = 40

t1 = Test()
t2 = Test()
t1.c = 50
t2.d = 60
print(t1.__dict__)
print(t2.__dict__)

