import os
import multiprocessing
from time import sleep
def process1(no):
    print("process1 is created")
    print("PID of process1",os.getpid())
    print("PID of parent process1",os.getppid())
    for i in range(no):
        sleep(1)
        print("process1 is",i)
def process2(no):
    print("process2 is created")
    print("PID of process2",os.getpid())
    print("PID of parent process2",os.getppid())
    for i in range(no):
        sleep(1)
        print("process2 is",i)
def main():
    print("inside main process ")
    print("PID of main process is",os.getpid())
    print("PID of parent process of main is",os.getppid())
    value=10
    p1=multiprocessing.Process(target=process1,args=(value,))
    p2=multiprocessing.Process(target=process2,args=(value,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("end of main")
if __name__=="__main__":
    main()
