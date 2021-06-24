# accept n numbers from user  and filter out only even numbers  from that n number after that add 2 in every even and the add the al numbers

def checkeven(no):
    if no%2==0:
        return True
    else:
        return False
def marvellousfilter(arr):
    brr=[]
    for i in range(len(arr)):
        if checkeven(arr[i])==True:
            brr.append(arr[i])
    return brr
def marvellousmap(arr):
    for i in range(len(arr)):
        arr[i]=arr[i]+2
    return arr
def marvellousreduce(arr):
    sum=0
    for i in range(len(arr)):
        sum=sum+arr[i]
    return sum
def main():
    arr=[]
    print("enter num ")
    size=int(input())

    for i in range(size):
        print("enter number",i+1)
        no=int(input())
        arr.append(no)
    print("enter data is ",arr)

    newdata=marvellousfilter(arr)
    print("after filter",newdata)

    newdata1=marvellousmap(newdata)
    print("after map",newdata1)

    output=marvellousreduce(newdata1)
    print("after reduce",output)
if __name__=="__main__":
    main()