def main():
    batches={"PPA":12500,"LB":11000,"PYTHON":13000,"ANGULAR":10000}
    batches["LSP"]=11000
    print("keys of dic")
    for value in batches.keys():
        print(value)
    print("keys and value of dic")
    for value in batches.keys():
        print(value,batches[value])
    print("keys and value are")
    for i,j in batches.items():
        print(i,j)

if __name__=="__main__":
    main()