# f = open("abc.txt",'w')
# f.write("Durga\n")
# f.write("Software\n")
# f.write("Solutions\n")
# print("Data write to the file successfully")
# f.close()

#==================================================

# #properties of writting a file
# 
# f = open("abcd.txt",'w')
# print("File Name:",f.name)
# print("File mode",f.mode)
# print("Is file readable ",f.readable())
# print("Is file writable ",f.writable())
# print("Is file closed ",f.closed)
# f.close()
# print("Is file closed ",f.closed)
# #

#properties of reading a file

# f = open("abcdefg.txt",'r')
# print("File Name:",f.name)
# print("File mode",f.mode)
# print("Is file readable ",f.readable())
# print("Is file writable ",f.writable())
# print("Is file closed ",f.closed)
# f.close()
# print("Is file closed ",f.closed)


# #properties of append a file
# 
# f = open("abcdefgh.txt",'a')
# print("File Name:",f.name)
# print("File mode",f.mode)
# print("Is file readable ",f.readable())
# print("Is file writable ",f.writable())
# print("Is file closed ",f.closed)
# f.close()
# print("Is file closed ",f.closed)

#properties of Exclusive 'x' a file

# f = open("abcdefghi.txt",'x')
# print("File Name:",f.name)
# print("File mode",f.mode)
# print("Is file readable ",f.readable())
# print("Is file writable ",f.writable())
# print("Is file closed ",f.closed)
# f.close()
# print("Is file closed ",f.closed)

#=========================================

#Writing data to text files

# f=open("abcd.txt",'w')
# f.write("Durga\n")
# f.write("software\n")
# f.write("solutions\n")
# print("Data written into file successfully")
# f.close()

#==============================================

# f=open("abcde.txt",'w')
# f.write("Durga\n")
# f.write("software\n")
# f.write("solutions\n")
# print("Data written into file successfully")
# f.close()

#==================================================

# # Reading charecter data from the file:
# 
# # 1. read() -->To read total data from file
# 
# f = open("abc.txt",'r')
# data = f.read()
# print(data)
# f.close()
# 
# # 2. read(n) -->To read 'n' charecters data from the file..
# 
# f = open("abc.txt",'r')
# data = f.read(9)
# print(data)
# f.close()
# 
# # 3. readline() -->To read only single line from the file..
# 
# f = open("abc.txt",'r')
# line1 = f.readline()
# print(line1,end="")
# line2 = f.readline()
# print(line2,end="")
# line3 = f.readline()
# print(line3,end="")
# f.close()
# 
# # 4. readlines() -->To read all lines into the file..
# 
# f = open("abc.txt",'r')
# data = f.readlines()
# for line in data:
#     print(data,end='')
# f.close()

#==========================================================

# The with statement

# with open("abc.txt","w") as f:
#     f.write("Durga\n")
#     f.write("Software\n")
#     f.write("Solutions\n")
#     print("is file closed?",f.closed)
# 
# print("is file closed?",f.closed)

#=====================================================

# import os
# fname = input("Enter file name:")
# if os.path.isname(fname):
#     print("File Exists:",fname)
#     f = open(fname,'r')
#     print("The Content of file is :")
#     text = f.read()
#     print(text)
# else:
#     print("File Not Exists:",fname)

#===================================================
# tell()

# f = open("abc.txt",'r')
# print(f.tell())
# print(f.read(4))
# print(f.tell())
# print(f.read(5))
# print(f.tell())

#====================================================
#seek()

# data ="All students are STUPIDS"
# f = open('abc.txt','w')
# f.write(data)
# with open('abc.txt','r+') as f:
#     text = f.read()
#     print(text)
#     print("The current cursor Position :",f.tell())
#     f.seek(17)
#     print("The current cursor position",f.tell())
#     f.write("GEMS!!!") # cursor jump to the 17 position & override STUPID to JEMS!!!
#     f.seek(0)
#     text = f.read()
#     print("Data After Modification :")
#     print(text)
#     f.close()
#======================================================

# WAP to check whether the given file exists or not. if it is available then print it's content

# import os,sys
# fname = input("Enter file name :")
# if os.path.isfile(fname):
#     print("File Exists:",fname)
#     f = open(fname,'r')
#     
# else:
#     print("file not Exists:",fname)
#     sys.exit(0)
# print("The Content of file is :")
# data = f.read()
# print(data)

# After modifying code

# import os,sys
# fname = input("Enter file name :")
# if os.path.isfile(fname):
#     print("File Exists:",fname)
#     f = open(fname,'r')
#     print("The Content of file is :")
#     data = f.read()
#     print(data)
# 
# else:
#     print("file not Exists:",fname)
#     sys.exit(0)


# Here we do not need to use sys.exit(0) module

# import os
# fname = input("Enter file name :")
# if os.path.isfile(fname):
#     print("File Exists:",fname)
#     f = open(fname,'r')
#     print("The Content of file is :")
#     data = f.read()
#     print(data)
#     f.close()

# else:
#     print("file not Exists:",fname)

#===============================================

# WAP the numbers of lines,words and charecter present in the given file?

# import os,sys
# fname = input("Enter file name :")
# if os.path.isfile(fname):
#     print("File Exists:",fname)
#     f = open(fname,'r')
#     
# else:
#     print("file not Exists:",fname)
#     sys.exit(0)
# lcount=wcount=ccount=0
# for line in f:
#     lcount = lcount+1
#     ccount=ccount+1
#     ccount=ccount+len(line)
#     words=line.split()
#     wcount=wcount+len(words)
# print("The number of lines:",lcount)
# print("The number of words:",wcount)
# print("The number of charecters:",ccount)

#================================================

# Handling Byte data

f1 = open("Photo.jpg",'rb')
f2 = open("newpic.jpg",'wb')
bytes = f1.read()
f2.write(bytes)
print("New Image is available with the new name newpic.jpg")