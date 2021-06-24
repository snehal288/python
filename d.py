#defination of addition function
from dd import *
def main():
    print("enter first no")
    value1=int(input())

    print("second no")
    value2=int(input())

    ret=addition(value1,value2)
    print("addition of {} and {} is {}".format(value1,value2,ret))
    ret = substraction(value1,value2)
    print("sub of {} and {} is {}".format(value1, value2, ret))


if __name__=="__main__":
    main()

