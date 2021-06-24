class ageinvalid(Exception):
    def __init__(self,data):
        self.data=data

def main():
    try:
        age=int(input("enter yourage for pan card"))
        if age<18:
            raise ageinvalid("your age is less that 18")
    except ageinvalid as obj:
        print(obj)
    else:
        print("you will get the pan")


if __name__=="__main__":
    main()