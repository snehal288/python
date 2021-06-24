def main():
    name=input("enter the file name we want to create")
    fobj=open(name,"w") #create new file #w for write
    str=input("enter the data that you want to write")
    fobj.write(str)
if __name__=="__main__":
    main()