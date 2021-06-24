import os
import time
import multiprocessing
def square(no):
    return no*no
def parallelprocessing():
    start = time.time()
    print("parallel processing")
    arr = range(1000)
    pobj=multiprocessing.Pool()
    ret=pobj.map(square,arr)
    end = time.time()
    print("result of parallel processing is:", ret)
def serialprocessing():
    start=time.time()
    print("serial processing")
    arr=range(1000)
    ret=[]
    for i in arr:
        ret.append(square(i))
    end=time.time()
    print("time required for serial execution",end-start)
def main():
    print("inside main")
    serialprocessing()
    parallelprocessing()
if __name__=="__main__":
    main()