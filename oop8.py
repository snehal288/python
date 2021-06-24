class base:
    def __init__(self):
        self.i=10
        self.j=20
        print("inside base contructor")
    def fun(self):
        print("inside base fun")
    def gun(self):
        print("inside base gun")
class derived(base):
    def __init__(self):
        base. __init__(self) #implisite calling
        self.x=30
        self.y=40
        print("inside derived constructor")
    def sun(self):
        print("inside derived sun")
    def gun(self): #overridding
        print("inside derived gun")
def main():
    bobj=base()
    print(bobj.i)
    print(bobj.j)
    bobj.fun()
    bobj.gun()

    dobj=derived()
    print(dobj.i)
    print(dobj.j)
    print(dobj.x)
    print(dobj.y)
    dobj.sun()
    dobj.gun()
    dobj.fun()

if __name__=="__main__":
    main()