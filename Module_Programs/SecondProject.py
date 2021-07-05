# Second Project # list/second

# import first
# import Second
# 
# print(first.a)
# first.name()
# 
# print(Second.a)
# Second.name()

#=====================================================

# from first import name, a
# print(a)
# name()
# 
# 
# from Second import name, a
# print(a)
# name()

#=====================================================

# use class
# 
# import first
# import Second

# from first import Myclass as Myc, Myschool as Mys
# from Second import Mycollege as Mycl

from first import*
from Second import*

#c = first.Myclass()
c = Myclass()
# c = Myc()
c.name()

#s = first.Myschool()
s = Myschool()
# s = Mys()
s.show()

#s = first.Mycollege()
s = Mycollege()
# s = Mycl()
s.disp()

