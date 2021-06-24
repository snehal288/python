import functools
def checkeven(no):
    if no%2==0:
        return True
    else:
        return False
def increment(no):
    return no+2
def add(no1,no2):
    return no1+no2
def main():
    arr=[]
    print("enter num ")
    size=int(input())

    for i in range(size):
        print("enter number",i+1)
        no=int(input())
        arr.append(no)
    print("enter data is ",arr)
    # namedata=filter(function_name,data)
    newdata=list(filter(checkeven,arr))   #newdata=marvellousfilter(arr)
    print("after filter",newdata)

    newdata1=list(map(increment,newdata)) #newdata1=marvellousmap(newdata)
    print("after map",newdata1) #print("after map",newdata1)

    output=functools.reduce(add,newdata1)#output=marvellousreduce(newdata1)
    print("after reduce ",output)#print("after reduce",output)
if __name__=="__main__":
    main()