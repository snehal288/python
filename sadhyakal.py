import os
import threading
from time import sleep
def thread1(no):
    print("thread1 is created")
    print("PID of thread1",os.getpid())
    print("PID of parent thread1",os.getppid())
    for i in range(no):
        sleep(1)
        print("thread1 is",i)
def thread2(no):
    print("thread2 is created")
    print("PID of thread2",os.getpid())
    print("PID of parent thread2",os.getppid())
    for i in range(no):
        sleep(1)
        print("thread2 is",i)
def main():
    print("inside main thread ")
    print("PID of main process is",os.getpid())
    print("PID of parent process of main is",os.getppid())
    value=10
    t1=threading.Thread(target=thread1,args=(value,))
    t2=threading.Thread(target=thread2,args=(value,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("end of main")
if __name__=="__main__":
    main()
