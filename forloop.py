
def displayF(no):
    print("for loop")
    icnt=0
    for icnt in range (0,no):
        print("jay ganesh")

def displayW(no):
    print("while loop")
    iCnt=0
    while iCnt<no:
        print("jay ganesh")
        iCnt=iCnt+1

def main():
    print("ENTER NUMBER OF iteration")
    value=int(input())
    displayW(value)
    displayF(value)

if __name__=="__main__":
    main()