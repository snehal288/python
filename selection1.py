#taking no from user check even or
def checkEven(no):
    if no% 2==0:
        return True
    else:
        return False
def main():
    print("enter one number")
    value=int(input())
    bret=checkEven(value)

    if bret==True:
        print("{}is even number".format(value))
    else:
        print("{} is odd number".format(value))

if __name__=="__main__":
   main()
