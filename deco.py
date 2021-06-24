#inbuild fun from module
def substraction(no1,no2):
    return no1-no2

def main():
    print("enter first number")
    value1=int(input())
    print("enter second number")
    value2=int(input())
    ret=substraction(value1,value2)
    print("sub is",ret)

if __name__=="__main__":
 main()