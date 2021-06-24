#design oop app which accept n numbers and perform operations display even number,summation of all and display all perfect number
class Numbers:
    def __init__(self,no=10):
        self.size=no
        self.arr=[]
    def __del__(self):
        print("dealocating memory")
        del self.arr
    def accept(self):
        print("please enter the elements:")
        for i in range(self.size):
            print("enter number:",i+1)
            self.arr.append(int(input()))
    def display(self):
        print("element of list:")
        for i in range(self.size):
            print(self.arr[i])
    def summation(self):
        sum=0
        for i in range(self.size):
            sum=sum+self.arr[i]
        return sum
    def evendisplay(self):
        print("even elements from list")
        for i in range(self.size):
            if(self.arr[i]%2)==0:
                print(self.arr[i])
    def perfectdisplay(self):
        sum=0
        for i in range(self.size):
            for j in range(1,int(self.arr[i]/2)+1):
                if (self.arr[i]%j)==0:
                    sum=sum+j
            if sum==self.arr[i]:
                print(self.arr[i])
            sum=0
    def primedisplay(self):
        flag=False
        for i in range(self.size):
            for j in range(2,int(self.arr[i]/2)+1):
                if(self.arr[i]%j)==0:
                    flag=True
                    break
            if flag==False:
                print(self.arr[i])
            flag=False
def main():
    print("enter number of elements")
    value=int(input())
    obj1=Numbers(value)
    obj1.accept()
    obj1.display()
    ret=obj1.summation()
    print("summation of element",ret)
    obj1.evendisplay()
    print("perfect numbers are")
    obj1.perfectdisplay()
    print("prime numbers are")
    obj1.primedisplay()
    del obj1
if __name__=="__main__":
    main()
