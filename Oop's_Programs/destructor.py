import time
class Test:
    def __init__(self):
        print("Object initialization")
    def __del__(self):
        print("Fulfill last wish & performing clean up activities ")

t1 = Test()
t1 = None
time.sleep(5)
print("End of Application ")