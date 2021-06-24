def main():
    no1=int(input("enter first number"))
    no2 = int(input("enter second number"))
    try:                          #RUN by PVM
        print("inside try")
        ans=no1/no2              #10/0 he exception ahe
    except ZeroDivisionError as obj:
        print("divide by zero",obj)
    else:
        print("inside else")
        print("ans is",ans)
    finally:                    #resource free karych logic ast
        print("deallocation all resource")

if __name__=="__main__":
    main()