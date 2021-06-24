def addition(*arr):
    sum=0

    for no in arr:
      sum=sum+no
    return sum
def main():
    ret=addition(10,20,30,40)
    print("addition is",ret)
    ret=addition(10,20)
    print("addition is",ret)

if __name__=="__main__":
    main()
