#accept n number from user and return addition of that n numbers

def Addition(list):
    sum=0
    for i in range(len(list)):
        sum=sum+list [i]
    return sum

def main():
    arr = []
    print("enter the number of element")
    size=int(input())

    for i in range(size):
        print("enter element no",i+1)
        value=int(input())
        arr.append(value)
    print("accept data",arr)

    ret=Addition(arr)
    print("addition of element:",ret)


if __name__=="__main__":
    main()
