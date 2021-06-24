def main():
    batches={"PPA":12500,"LB":11000,"PYTHON":13000,"ANGULAR":10000,"LSP":11000}
    print("enter the batch name")
    name=input()
    print(batches.get(name,"there is no such batch"))

if __name__=="__main__":
    main()