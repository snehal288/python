import sys
def addition(no1,no2):
    return no1+no2
def main():
    ret=addition(int(sys.argv[1]),int(sys.argv[2]))
    print("addition is:",ret)


if __name__ == "__main__":
    main()


