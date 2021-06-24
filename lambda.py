#name=lambda parameters:body
def addition(no1,no2):
    return no1+no2
sum=lambda no1,no2: no1+no2
def  fun(name):
     ret=name(10,20)
     print("fun",ret)

def main():
    print("enter no")
    value1=int(input())
    print("enter no")
    value2= int(input())
    ret=addition(value1,value2)
    print("add is",ret)

    ret=sum(value1,value2)
    print("addition due to lambda is:",ret)
    fun(sum)

if __name__=="__main__":
    main()