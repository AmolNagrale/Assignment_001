s= lambda n:n*n
print(s(4))

s= lambda a,b:a+b
print("The sum of value is:", s(5,6))

# find the greater number by using lambda fuction

s= lambda a,b: a if a>b else b

print("The greater number is:",s(10,20))

# find the greater number of 3 variable by using lambda function

s= lambda a,b,c : a if (a>b) and (a>c) else b if (b>a) and (b>c) else c

print("The greater value of three numbers :", s(10,20,30))

