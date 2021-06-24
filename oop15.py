class base:
    def __init__(self):
        self.i =10
    def fun(self):
        print("base fun")
class derived(base):
    def __init__(self):
        base.__init__(self)
        self.i=20

    def fun(self):
        print("derived fun")
    def gun(self):
        print("derived gun")
        self.fun()
        super().fun()
        print(base().i)
        print(self.i)

dobj=derived()
dobj.gun()