#positional arguments

# def sub(a,b):
#     print(a-b)
#     
# sub(200,100)
# sub(5,10)

# Keyword arguments

# def wish(name,massage):
#     print("Hello",name,massage)
# wish(name="amol",massage="Good morning")
# wish(massage="Good morning",name="amol")

#Everytime first use keyword argument & then positional argument

# def wish(name,msg):
#     print("Hello",name,msg)
# wish("Amol","good morning")
# wish("Amol",msg="good morning")
# wish(name = "Amol","good morning")

#default argument
# 
# def wish(name ="guest"):
#     print("hello",name,"good morning")
# 
# wish("Amol")
# wish()

#variable length arguments

# def sum(*n):
#     total =0
#     for n1 in n:
#         total =total +n1
#     print("The sum=", total)
#     
# sum()
# sum(10)
# sum(10,20)
# sum(10,20,30,40)

#mix positional arguments & variable arguments

# def f1(n1,*s):
#     print(n1)
#     for s1 in s:
#         print(s1)
# 
# f1(10)
# f1(10,20,30,40)
# f1(10,'a',20,'b')

def display(**kwargs):
    for k,v in kwargs.items():
        print(k,"=",v)
display(n1=10,n2=20,n3=30)
display(rno=100,name="Amol",marks=70,subject="python")




