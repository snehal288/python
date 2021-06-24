#chaining
def substraction(no1, no2):
    return no1 - no2

def subdecorator(fun_name):#fun_name is consider as reference
    return fun_name(10,5)

def main():

    ret = subdecorator(substraction)#substraction is function as a object
    print("sub is", ret)


if __name__ == "__main__":
    main()