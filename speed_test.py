# Speed test example on Decorators

from time import time

def SpeedTest(func):
    def wrapper():
        start = time()
        func()
        end = time()
        print(f"Function running time is: {end - start}")
    return wrapper

@SpeedTest
def BigLoop():
    for number in range(1, 20000):
        print(number)

BigLoop()