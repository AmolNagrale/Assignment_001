# n = [10,20,30,40]
# print(n)
# n[1] = 777
# print(n)

# s = " python is very easy language !!"
# l = s.split()
# print(l)

# s = "durga"
# l = list(s)
# print(l)
# 
# i = list(range(0,10,2))
# print(i)

# transversal

# n = [0,1,2,3,4,5,6,7,8,9]
# i = 0
# while i<len(n):
#     print(n[i])
#     i = i+1
     
# #by using loop
#     
# n = [0,1,2,3,4,5,6,7,8,9]
# for n1 in n:
#     print(n1)


#display element indexwise

# l = ["A","B","C","D"]
# x = len(l)
# for i in range(x):
#     print(l(i)," is available at positive index :" ,i,"and at negative index :",i+x)
# 

# important function of list

# n = [1,2,2,3,3,3,4,4,4,4,2,1,5,6,4,8,9,0,7,6,5,5,2,]
# print(n.count(1))
# print(n.count(2))
# print(n.count(3))
# print(n.count(4))
# print(n.count(5))
# print(n.count(6))

#list manipulation
#1. append

# list = []
# 
# list.append("A")
# list.append("B")
# list.append("C")
# list.append("D")
# list.append("E")
# 
# print(list)

# insert
# list = [1,2,3,4,5]
# list.insert(1, 444)
# 
# print(list)

# extend

# order1 = ["chicken","mutton","eges","fish"]
# order2 = ["dal","rice","panner","sabji","mutter"]
# order1.extend(order2)
# print(order1)
# order1.extend("tambda")
# print(order1)


# remove

# list = [5,2,5,4,5]
# list.remove(5)
# print(list)
# list.remove(5)
# print(list)

#pop

# n = [10,20,30,10]
# print(n.pop())
# print(n)


# list = [1,2,3,4,5]
# print(list.pop(1))
# print(list)

# list = [1,2,3,4,5]
# list.reverse()
# print(list)

# list = ["f","b","c","d","e","a"]
# list.sort(reverse=True)
# print(list)
# list.sort(reverse=False)
# print(list)

# x = [10,20,30,40]
# y = x
# print(id(x))
# print(id(y))
# y[1] = 101
# print(y)
# del.x
# a = [10,20,30,[10,30,50]]
# #c = (a + [40])*4
# print(a[2][2])
# c.clear()
# print(c)


# n = [10,20,30,[40,60,50]]
# 
# print(n)
# 
# print(n[2][0])

# programs on matrix by using nested list method

# n = [[10,20,30],[40,50,60],[70,80,90]]
# print (n)
# print("Elements in row wise :")
# for r in n:
#     print(r)
# print("Element in matrix wise :")
# for i in range(len(n)):
#     #print(i)
#     for j in range(len(n[i])):
#      #print(j)
#          print(n[i][j], end="  ") # this statement use for printing matrix
#          
#     print()

# words = ["Balaiah","Nag","Venktesh","Chiranjeevi"]
# l = [w[0] for w in words]
# print(l)

# words = "the quick brown fox jumps over the lezy dog".split()
# print(words)
# l = [[w.upper(),len(w)] for w in words]
# print(l)

# WAP to display the unique vowels present in the giver word

vowels = ['a','e','i','o','u']
word = input("Enter the words to serach for vowels :")
found = []
for letter in word:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
print(found)
print("The numbers of different vowels present in",word,"is",len(found))

    




