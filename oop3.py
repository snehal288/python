class arithematic:#class defination
    value=111       #class variable
    def __init__(self,i,j):       #class constructor
        print("inside constructor")
        self.no1=i               #no1 &no2 are characteristic ahe
        self.no2=j               #instance variable

    def add(self):               #instance method
        print(arithematic.value)
        return self.no1+self.no2
    def sub(self):
        return self.no1-self.no2

def main():
    print("value is:",arithematic.value)
    obj1=arithematic(21,11)      #__init__(obj1,21,11)
    obj2=arithematic(101,51)     #__init__(obj2,101,51)
    print("value is:",obj1.value)

    ret=obj1.add()
    print("addition is",ret)
    ret=obj1.sub()
    print("substraction is",ret)

    ret = obj2.add()
    print("addition is", ret)
    ret = obj2.sub()
    print("substraction is", ret)
if __name__=="__main__":
    main()