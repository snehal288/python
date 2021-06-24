class base1:
    def __init__(self):
        self.i=10
        self.j=20
        print("inside base1 contructor")

class base2:
    def __init__(self):
        self.x=10
        self.y=20
        print("inside base2 constructor")
class derived(base1,base2):
    def __init__(self):
        base1. __init__(self)
        base2. __init__(self)
        self.a=50
        self.b=60
        print("inside derived2 constructor")
def main():
    dobj=derived()
    print(dobj.i)
    print(dobj.j)
    print(dobj.x)
    print(dobj.y)
    print(dobj.a)
    print(dobj.b)

if __name__=="__main__":
    main()