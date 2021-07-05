import cal

# print("Cal Module's Variable : ",cal.a)
# 
# cal.name()
# 
# print("The addition of cal module is :",cal.add(20,40))
# 
# print("The substraction of cal module is :",cal.sub(40,20))
# 
# add = cal.add # aliasing with add
# a = add(20,40)
# print(a)
# 
# sub = cal.sub # aliasing with sub
# b = sub(40,20)
# print(b)


# from cal import a, name, add, sub
# 
# print(a)
# name()
# a = add(10,20)
# print(a)
# 
# b = sub(40,20)
# print(b)

# from cal import add as s
# 
# a = s(10,20)
# print(a)



from cal import a as x, name as y, add as z, sub as u

print(x)
y()
a = z(10,20)
print(a)

b = u(40,20)
print(b)