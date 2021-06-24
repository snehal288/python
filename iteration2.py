
def startDynamic(no,msg):
    iCnt=0
    while iCnt<no:
        print(msg)
        iCnt=iCnt+1

def main():
    print("ENTER NUMBER OF TIMES YOU WANT TO DISPLAY MSG ON SCREEN")
    value=int(input())
    print("enter msg")
    name=input()
    startDynamic(value,name)

if __name__=="__main__":
    main()