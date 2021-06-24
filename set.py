def main():
    arr={10,20.5,"hello",10} #order change hote(unordered)#duplication not allowed
    print(type(arr))
    print(arr)
    print(len(arr))
    for value in arr:
        print(value)
    if "hello" in arr:
        print("hello is there")
    arr.add(20)
    print(arr)
    arr.remove(20)
    print(arr)
    arr.discard(20.5)
    print(arr)
    #arr.pop()#last elements change hota so result is unpredictable
    #print(arr)
    #arr.remove(120)
    #print(arr)
    arr.discard(120)
    print(arr)
if __name__=="__main__":
    main()