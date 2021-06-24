def main():
    no1=int(input("enter first number"))
    no2 = int(input("enter second number"))
    try:   #RUN by PVM
        ans=no1/no2              #10/0 he exception ahe
    except ZeroDivisionError as obj:
        print("divide by zero",obj)
    except Exception as eobj: #CATCH karto msdhoni will catch
        print("exception occur",eobj)
    else:
        print("ans is",ans)

if __name__=="__main__":
    main()