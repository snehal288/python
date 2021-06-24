#words in exception
def main():
    no1=int(input("enter first number"))
    no2 = int(input("enter second number"))
    try:   #RUN by PVM
        ans=no1/no2              #10/0 he exception ahe
    except Exception as eobj: #CATCH karto
        print("exception occur",eobj)
    else:
        print("ans is",ans)

if __name__=="__main__":
    main()