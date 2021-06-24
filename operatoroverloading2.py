class demo:
    def __init__(self,x,y):
        self.i=x
        self.j=y
    def __add__(self, other):  #special methood
        return demo(self.i+other.i,self.j+other.j)
def main():
    obj1=demo(10,20)
    obj2=demo(30,40)
    ret=obj1+obj2     #obj1.__add__(obj2) #__add__(obj1,obj2)
    print(ret.i,ret.j)
if __name__=="__main__":
    main()