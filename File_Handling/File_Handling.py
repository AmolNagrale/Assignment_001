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

# Handling Byte data ==>Image 

# f1 = open("Photo.jpg",'rb')
# f2 = open("newpic.jpg",'wb')
# bytes = f1.read()
# f2.write(bytes)
# print("New Image is available with the new name newpic.jpg")

#================================================
# Handling byte data ==>video

# f1 = open("Video.mp4",'rb')
# f2 = open("newvideo.mp4",'wb')
# bytes = f1.read()
# f2.write(bytes)
# print("New Image is available with the new name newpic.jpg")
# 
# f1 = open("audio.mp3",'rb')
# f2 = open("newaudio.mp3",'wb')
# bytes = f1.read()
# f2.write(bytes)
# print("New Image is available with the new name newpic.jpg")

#======================================================
# Handling csv files

# writting data to csv file

# import csv
# with open("emp.csv",'w',newline='')as f: # newline ='' use to remove extra spaces in xl
#     w = csv.writer(f)
#     w.writerow(["ENO","ENAME","ESAL","EADDR"])
#     n = int(input("Enter number of emplyee :"))
#     for i in range(n):
#         eno = int(input("Enter employee Number :"))
#         ename = input("Enter Employee Name :")
#         esal = float(input("Enter Employee Sal :"))
#         eaddr = input("Enter employee address :")
#         w.writerow([eno,ename,esal,eaddr])
#     print("Total Employees data written to csv file successfully !!!!!")

#=============================================================
# Reading data from csv file

# import csv
# f = open("emp.csv",'r')
# r = csv.reader(f)
# data =list(r)
# #print(data) # we have get a output in list form
# #print(type(r))
# for line in data:
#     for word in line:
#         print(word,"\t",end='')
#     print() # after reading first row will move on next line..
#     
#=================================================
# zipping & unzipping files

# Zipping files

# from zipfile import*
# f = ZipFile("file2.zip",'w',ZIP_DEFLATED)
# f.write("cricketers.txt")
# f.write("heroes.txt")
# f.write("Friends.txt")
# f.close()
# print("files1.zip file created successfully")

# unzipping files

# from zipfile import*
# f = ZipFile("file2.zip",'r',ZIP_STORED)
# names = f.namelist()
# for name in names:
#     print("File Name :",name)
#     print("The Content of this file :")
#     f1=open(name,'r')
#     print(f1.read())
#     print()
# print("files2.unzip files successfully")

#===========================================

# Working with directories :

# 1.current working directories

# import os
# cwd = os.getcwd
# print("Current working directory :",cwd)

# 2. create sub directory in current working directories
# import os
# os.mkdir("mysub")
# print("My sub directory create in cwd ")

#3. to create sub/Amol dirctory in mysub

# import os
# os.mkdir("mysub/Amol")
# print("mysub2 created inside mysub")

# #4. to create sub/Amol/pythonclass dirctory in mysub
# 
# import os
# os.mkdir("mysub/Amol/pythonclass")
# print("mysub2 created inside mysub")
# 
# #5. to create multiple directories in sub directories 

# import os
# os.makedirs("sub1/sub2/sub3")
# print("mysub2 created inside mysub")
#
# import os
# os.removedirs("mysub/Amol/pythonclass")
# print("mysub2 created inside mysub")
# 

# import os
# for dirpath,filenames in os.walk("Downloads"):
#     print("Current working directory path :",dirpath)
#     print("Directories :",dirnames)
#     print("File Names:",filenames)
# print()
#

# import os
# os.system("dir *.py")
# os.system("py demo.py")

# import os
# stat = os.stat("abc.txt")
# print(stat)

# import os
# from datetime import*
# stats=os.stat("abc.txt")
# print("File size in bytes :",stats.st_size)
# print("File Last access Time :",datetime.fromtimestamp(stats.st_atime))
# print("File Last Modified Time :",datetime.fromtimestamp(stats.st_mtime))


#==========================================================================

# Writing & reading state of objectby using pickle module :

import pickle
class Employee:
    def __init__(self,eno,ename,eaddr):
        self.eno = eno
        self.ename = ename
        self.eaddr = eaddr
    def display(self):
        print(self.eno,"\t",self.ename,"\t",self.eaddr)

with open("emp.dat","wb") as f:
    e = Employee(100,'Durga','Hyd')
    pickle.dump(e,f)
    print("Pickling of Employee object completed")
      
    
with open("emp.dat","rb") as f:
    obj=pickle.load(f)
    print("Employee Information after unpickling")
    obj.display()
