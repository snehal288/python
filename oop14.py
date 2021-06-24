class base:
    def __init__(self):
        self.i=10
        self.j=20
    def fun(self):
        print("base fun")
class derived(base):
    def __init__(self):
        base.__init__(self)
        #self.__init__() recursive call
        #super().__init__()
        self.i=30
        self.j=40
    def gun(self):
        print("derived gun")
        base.fun(self)
        self.fun() #fun(self)
        super().fun()
        #print(i) not
        print(self.i)
        print(super().i)
dobj=derived()
dobj.gun()