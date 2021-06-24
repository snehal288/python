import os

def main():
    print("inside main ")
    print("PID of control process is",os.getpid())
    print("PID of parent process is",os.getppid())

if __name__=="__main__":
    main()
