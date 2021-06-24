#swapping decorator
def substraction(no1, no2):
    return no1 - no2
def subdecorator(fun_name):#fun_name is consider as reference
    def updator(a,b):  #nested function
        if a<b:        #first parameter is small
            a,b=b,a    #swapping
        return fun_name(a,b)
    return updator
def main():
    sub=subdecorator(substraction)
    print("enter first no")
    value1=int(input())
    print("enter second no")
    value2=int(input())
    ret = sub(value1,value2)
    print("sub is", ret)
if __name__ == "__main__":
    main()