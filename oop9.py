#multi level inareturn
class base:
    def __init__(self):
        self.i=10
        self.j=20
        print("inside base contructor")

class derived1(base):
    def __init__(self):
        base. __init__(self) #implisite calling
        self.x=30
        self.y=40
        print("inside derived1 constructor")
class derived2(derived1):
    def __init__(self):
        derived1. __init__(self)
        self.a=50
        self.b=60
        print("inside derived2 constructor")
def main():
    dobj=derived2()
    print(dobj.i)
    print(dobj.j)
    print(dobj.x)
    print(dobj.y)
    print(dobj.a)
    print(dobj.b)

if __name__=="__main__":
    main()