import functools
def main():
    arr=[]
    print("enter num ")
    size=int(input())

    for i in range(size):
        print("enter number",i+1)
        no=int(input())
        arr.append(no)
    print("enter data is ",arr)

    newdata=list(filter(lambda no:(no%2==0),arr))
    print("after filter",newdata)

    newdata1=list(map(lambda no:no+2,newdata))
    print("after map",newdata1)

    output=functools.reduce( lambda no1,no2:no1+no2,newdata1)
    print("after reduce ",output)
if __name__=="__main__":
    main()