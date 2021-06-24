def main():
    name=input("enter the file name")
    fobj=open(name,"r") #create new file #w for write
    print("data from file is:")
    print(fobj.readline())
if __name__=="__main__":
    main()
