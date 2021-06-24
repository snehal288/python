class marvellous:
     value1=11

     def __init__(self,no1,no2):
        self.i=no1
        self.j=no2
        print("inside con")
     def __del__(self):
        print("inside des")
     def fun(self):
        print("inside fun")
        print("value of j",self.j)

def main():
     obj1 = marvellous(11, 21)
     obj2 = marvellous(51, 101)
     print("value of i", obj1.i)
     print("value of i", obj2.i)
     print("value class", marvellous.value1)
     obj1.fun()
     obj2.fun()
     del obj1
     del obj2
if __name__ == "__main__":
     main()