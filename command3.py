import sys
def addition(no1,no2):
    return no1+no2
def main():
    if len(sys.argv)<3 or len(sys.argv)>3:
        print("invalid number of arguments")
        return
    ret=addition(int(sys.argv[1]),int(sys.argv[2]))
    print("addition is:",ret)

if __name__ == "__main__":
    main()


