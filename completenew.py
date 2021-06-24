from arithmatic import *


#entry point function
def main():
    print("enter first number:")
    value1=int(input())

    print("enter second number:")
    value2=int(input())

    ret1=addition(value1,value2)
    ret2=substraction(value1,value2)

    print("addition is:",ret1)
    print("substraction is:",ret2)

if __name__=="__main__":
 main()

