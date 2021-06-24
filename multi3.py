import os
import multiprocessing
def process1():
    print("process1 is created")
    print("PID of process1",os.getpid())
    print("PID of parent process1",os.getppid())
def process2():
    print("process2 is created")
    print("PID of process2",os.getpid())
    print("PID of parent process2",os.getppid())
def main():
    print("inside main process ")
    print("PID of main process is",os.getpid())
    print("PID of parent process of main is",os.getppid())
    p1=multiprocessing.Process(target=process1,args=())
    p2=multiprocessing.Process(target=process2,args=())
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print("end of main process")

if __name__=="__main__":
    main()
