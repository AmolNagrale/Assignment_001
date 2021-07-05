# # x = int(input("Enter some number"))
# # print(x)
# 
# try:
#     print(10/0)
# except ZeroDivisionError as msg:
#     print("Esception raised and its is discription :",msg)

#====================================================================

# try:
#     x = int(input("Enter first number"))
#     y = int(input("Enter second number"))
#     print(x/y)
# except ZeroDivisionError:
#     print(" ZeroDivisionError ")
# except ValueError:
#     print("ValueError")

#====================================================
# PVM alway work on top to bottom
# # parent error
# try:
#     x = int(input("Enter first number"))
#     y = int(input("Enter second number"))
#     print(x/y)
# except ArithmaticError:
#     print(" ArithmaticError ")
# except ZeroDivisionError:
#     print("ZeroDivisionError")

# First child error

# try:
#     x = int(input("Enter first number"))
#     y = int(input("Enter second number"))
#     print(x/y)
# 
# except ZeroDivisionError:
#     print("ZeroDivisionError")
#     
# except ArithmaticError:
#     print(" ArithmaticError ")
#     
#===============================================
    
# #single except block tht can handle multiple exception
#     
# try:
#     x = int(input("Enter first number"))
#     y = int(input("Enter second number"))
#     print(x/y)
# 
# except (ZeroDivisionError,ValueError) as msg:
#     print("Please provide valid number only & problem is ",msg)
#     
#==================================================================

#Default except block

# try:
#     x = int(input("Enter first number"))
#     y = int(input("Enter second number"))
#     print(x/y)
# 
# except ZeroDivisionError as msg:
#     print("ZeroDivisionError : Can't divide with zero ")
# except:
#     print("Default Except: Please provide valid input")
#     

# first use default block
# try:
#     x = int(input("Enter first number"))
#     y = int(input("Enter second number"))
#     print(x/y)
# 
# except:
#     print("Default Except: Please provide valid input")
#     
# except ZeroDivisionError as msg:
#     print("ZeroDivisionError : Can't divide with zero ")

#=============================================================

# try:
#     print("Try1")
#     
# except:
#     print("except1")
# print("except2")
# 
# try:
#     print("Try1")
#     
# except:
#     print("except1")
# print("except2")

# try:
#     print("Try1")
#     
# except:
#     print("except1")
#     print("except2")
# 
# try:
#     print("Try1")
#     
# finally:
#     print("finally1")
#     


# try:
#     print("Try1")
#     
# except:
#     print("except1")
# if 10>20:    
#     print("if")
# else:
#     print("else")
#     

try:
    print("Try1")
    try:
        print("Try1")
    except:
        print("except1")
    finally:
        print("inner finally block")
    
except:
    print("outer except")
   
    

    

