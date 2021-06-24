class student:
    def __init__(self,str,a,b,c):
        self.name=str
        self.m1=a
        self.m2=b
        self.m3=c
    def __eq__(self, other):
        return ((self.m1==other.m1) and (self.m2==other.m2) and (self.m3==other.m3))

    def __gt__(self, other):
        return ((self.m1>=other.m1) and (self.m2>=other.m2) and (self.m3>=other.m3))
def main():
    obj1=student("piyush",99,99,99)
    obj2=student("snehal",90,99,45)

    if obj1==obj2:
        print("both student equal")
    else:
        print("both student different")
    if obj1>obj2:
        print("first object is greater")
    else:
        print("second object is greater")

if __name__=="__main__":
    main()