

def displayif(no):
    for i in range(no): #iteration
        print("hello")

def displayiw(no):
    while no!=0:
        print("hello")
        no=no-1
def displayr(no):
    if no !=0:
        no=no-1
        print("hello") #recursive
        displayr(no)
def main():
    print("enter number of iteration")
    value=int(input())
    print("calling iterative for loop functions")
    displayif(value)
    print("calling iterative while loop functions")
    displayiw(value)
    print("calling recursive function")
    displayr(value)

if __name__=="__main__":
    main()
