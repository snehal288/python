#defination of addition function
def addition(no1,no2):
    ans=no1+no2
    return ans
#defination of substraction function
def substraction(no1,no2):
    ans=no1+no2
    return ans

#entry point function
def main():
    print("enter first number:")
    value1=int(input())

    print("enter second number:")
    value2=int(input())

    ret1=addition(value1,value2)
    ret2=substraction(value1,value2)

    print("addition is:",ret1)
    print("substraction is:",ret2)


#code starter
if __name__=="_main_":
    main()



