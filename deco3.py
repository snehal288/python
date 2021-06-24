#swapping decorator
def substraction(no1, no2):
    print("3=inside substraction")
    return no1 - no2
def subdecorator(fun_name):
    print("6:inside subdecorator")
    def updator(a,b):
        print("8:inside updator")
        if a<b:
            a,b=b,a
        return fun_name(a,b)
    return updator
def main():
    print("14=inside main")
    sub=subdecorator(substraction)
    print("enter first no")
    value1=int(input())
    print("enter second no")
    value2=int(input())
    ret = sub(value1,value2)
    print("sub is", ret)
    print("22:end of main")
if __name__ == "__main__":
    print("24=inside starter")
    main()