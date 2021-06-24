def addf(data):
    sum=0
    for i in range(len(data)): sum=sum+data[i]
    return sum
def addw(data):
    sum=0
    i=0
    while i <(len(data)):
        sum=sum+data[i]
        i=i+1
    return sum
sum=0
i=0
def additionR(data):
    global sum
    global i
    if i<len(data):
        sum=sum+data[i]
        i=i+1
        additionR(data)
    return sum
def main():
    arr=[]
    size=int(input("enter size of array"))

    for i in range(size):arr.append(int(input()))
    print("data is",arr)
    print("add is",addf(arr))
    print("add is", addw(arr))
    print("add is", additionR(arr))



if __name__=="__main__":
    main()