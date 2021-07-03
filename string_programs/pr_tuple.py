# a = (10,20,30)
# print(a)
# print(type(a))

# indexing & slice

#t = (10,20,30,40,50,60)
# print(t[2:5])
# print(t[0:6])
# print(t[2:100])
# print(t[::1])
# print(t[0:-1])
# print(t[::-2])
#print(t[5])

# WAP to take tuple numbers from keyboard & print it sum & average

t = eval (input("Enter the tuple numbers :"))
l = len(t)
sum = 0
for x in t:
    sum = sum+x
print("The sum is :",sum)
print("The avarage is :",sum/l)
          