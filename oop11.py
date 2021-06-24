class base1:
    def __init__(self):

        print("inside base1 contructor")
    def fun(self):
        print("base1 fun")
class base2:
    def __init__(self):

        print("inside base2 constructor")
    def fun(self):
        print("base2 fun")
class derived(base1,base2):
    def __init__(self):
        base2. __init__(self)
        base1. __init__(self)
        print("inside derived2 constructor")

def main():
    dobj=derived()
    dobj.fun()
if __name__=="__main__":
    main()