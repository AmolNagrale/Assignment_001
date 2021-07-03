''' important note - *args which is used to help process list of elements in args.
Instate of args we can used other name also.'''

def students(*argsamol):
    
    for item in argsamol:
        print(item)

argsamol = ["Amol","Avi","Amit","Ashish","Mangesh"]

students(*argsamol)