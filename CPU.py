import os

def main():
    print("inside main")
    print("number of CPU are:",os.cpu_count())
if __name__=="__main__":
    main()