class demo:
    x=10
    y=20
    def __init__(self):
        print("inside contructor")
        self.i=30
        self.j=40
    def __del__(self):
        print("inside destructor")
    def fun(self):
        print("inside fun")
def main():
    obj1=demo()
    obj2=demo()
    obj1.fun()    #fun(obj1)
    obj2.fun()
    del obj1
    del obj2
if __name__=="__main__":
    main()