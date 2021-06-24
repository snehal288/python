import sys
def main ():
    print("recurion limit is",sys.getrecursionlimit())
    sys.setrecursionlimit(1500)
    print("recursion limit",sys.getrecursionlimit())
if __name__=="__main__":
    main()
