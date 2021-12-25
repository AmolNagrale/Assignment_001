# Multi threading

# there are three way to create thread class
#1. without using any class
#2. with using extended thread class
#3. without using extended thread class

# 1. Creating thread without using any class

# from threading import*
# def display():
#     for i in range(1,11):
#         print("Child Tread")
# t = Thread(target = display)
# t.start()
# for i in range(1,11):
#     print("Main Thread")    # by default
    
#2. with using extended thread class
    
# from threading import*
# class mythread(Thread):
#     def run(self):
#         for i in range(10):
#             print("Child Thread-1")
            
# t=mythread()
# t.start()
# for i in range(10):
#     print("Main Thread-1")
    
#3. creating thread without using extended thread class
 
from threading import*
class Test:
    def display(self):
        print(current_thread().getName())
        #for i in range(10):
            #print("child Thread-2")

obj=Test()
t1=Thread(target=obj.display)
t2=Thread(target=obj.display)
t2.start()
print(current_thread().getName())
t1.start()

for i in range(5):
   print("Main Thread-2")
    
    
# 3 without Multi-threading

# from threading import*
# import time
# def doubles(numbers):
#     for n in numbers:
#         time.sleep(1)
#         print("Double:",2*n)
#         
# def squares(numbers):
#     for n in numbers:
#         time.sleep(1)
#         print("Square:",n*n)
# numbers=[1,2,3,4,5,6]
# begintime=time.time()
# t1=Thread(target=doubles,args=(numbers,))
# t2=Thread(target=squares,args=(numbers,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print("The total time taken:",time.time()-begintime)

#=======================================================================

#setting & getting name of thread

# from threading import*
# print(current_thread().getName())
# current_thread().setName("Pawan Kalyan")
# print(current_thread().getName())
# print(current_thread().name)


#===================================================================

# Thread identification number(ident)

# from threading import*
# def test():
#     print("Child Thread")
#     
# t=Thread(target=test)
# t.start()
# print("Main Thread identification Number:",current_thread().ident)
# print("Child thread identification Number:",t.ident)

#========================================================================
# Active.count()

# from threading import*
# import time
# def display():
#     print(current_thread().getName(),"....Started")
#     time.sleep(3)
#     print(current_thread().getName(),"...End")
# print("The Number of active threads:",active_count())
# t1=Thread(target=display,name="ChildThread-1")
# t2=Thread(target=display,name="ChildThread-2")
# t3=Thread(target=display,name="ChildThread-3")
# 
# t1.start()
# t2.start()
# t3.start()
# 
# print("The number of active threads",active_count())
# print("The numbers of active threads",active_count())

#====================================================================

# Active Thread()

# from threading import*
# import time
# def display():
#     print(current_thread().getName(),"....Started")
#     time.sleep(3)
#     print(current_thread().getName(),"...End")
#     print("The Number of active threads:",active_count())
# t1=Thread(target=display,name="ChildThread-1")
# t2=Thread(target=display,name="ChildThread-2")
# t3=Thread(target=display,name="ChildThread-3")
# 
# t1.start()
# t2.start()
# t3.start()
# 
# I=enumerate()
# for t in I:
#     print("Thread Name:",t.name)
# time.sleep(5)
# I=enumerate()
# for t in I:
#     print("Thread Name:",t.name)
# print("The numbers of active threads",active_count())
# print("The numbers of active threads",active_count())

#===========================================================
# IsAlive

# from threading import*
# import time
# def display():
#     print(current_thread().getName(),"....Started")
#     time.sleep(3)
#     print(current_thread().getName(),"...End")
#     print("The Number of active threads:",active_count())
# t1=Thread(target=display,name="ChildThread-1")
# t2=Thread(target=display,name="ChildThread-2")
# t3=Thread(target=display,name="ChildThread-3")
# 
# t1.start()
# t2.start()
# t3.start()
# 
# print(t1.name,"is Alive:",t1.isAlive())
# print(t2.name,"is Alive:",t2.isAlive())
# time.sleep(5)
# print(t1.name,"is Alive:",t1.isAlive())
# print(t2.name,"is Alive:",t2.isAlive())

#=================================================================

# join() method

# from threading import*
# import time
# def display():
#     for i in range(10):
#         print("Seetha thread")
#         time.sleep(2)
#         
# t=Thread(target=display)
# t.start()
# t.join()
# for i in range(10):
#     print("Rama Thread")
#     
#=================================================================

#Daemon Thread

# from threading import*
# print(current_thread().isDaemon())
# current_thread().setDaemon(True)
# t.setDaemon(True)

#==================================================================

# Default Nature

# from threading import*
# def job():
#     print("Child Thread")
# t=Thread(target=job)
# print(t.isDaemon())
# t.setDaemon(True)
# print(t.isDaemon())

#==================================================================

# from threading import*
# import time
# def job():
#     for i in range(10):
#         print("Lazy Thread")
#         time.sleep(2)
#         
# t=Thread(target=job)
# #t.setDaemon(True)
# t.start()
# time.sleep(5)
# print("End Of Main Thread")

#=================================================================
# Synchronization:

# from threading import*
# import time
# def wish(name):
#     for i in range(10):
#         print("Good Evening:",end="")
#         time.sleep(2)
#         print(name)
# t1=Thread(target=wish,args=("Dhoni",))
# t2=Thread(target=wish,args=("Yuvraj",))
# t1.start()
# t2.start()

#===================================================================
#synchronization by using lock concept

# from threading import*
# import time
# l=lock()
# def wish(name):
#     l.acquire()
#     for i in range(10):
#         print("Good Evening:",end="")
#         time.sleep(10)
#         print(name)
#     l.release()
#         
# t1=Thread(target=wish,args=("Dhoni",))
# t2=Thread(target=wish,args=("Kohli",))
# t1.start()
# t2.start()

#========================================================================
# RLock

# from threading import*
# import time
# l=RLock()
# def factorial(n):
#     l.acquire()
#     if n==0:
#         result=1
#     else:
#         result=n*factorial(n-1)
#     l.release()
#     return result
# 
# def results(n):
#     print("The factorial of",n,"is:",factorial(n))
#     
# t1=Thread(target=results,args=(5,))
# t2=Thread(target=results,args=(9,))
# t1.start()
# t2.start()
#     
#=====================================================================



