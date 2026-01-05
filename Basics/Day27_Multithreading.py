from time import sleep
from threading import *

class Hello(Thread):
    def run(self):
        for i in range(5):
            print("hello")
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("Hi")
            sleep(1)

t1 = Hello()
t2 = Hi()

t1.start()
sleep(0.1)
t2.start()

t1.join() # join is used to join or to complete the execution of that 2 threads and then , it will print the other statements
t2.join()
print("Bye")
#collision - it happens when two threads are comming at the same time to the cpu . so we need to write sleep method between the object calling . so no colision between the threads