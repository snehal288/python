
def startDynamic(no):
    iCnt=0
    while iCnt<no:
        print("jay ganesh")
        iCnt=iCnt+1

def main():
    print("ENTER NUMBER OF TIMES YOU WANT TO DISPLAY MSG ON SCREEN")
    value=int(input())
    startDynamic(value)

if __name__=="__main__":
    main()