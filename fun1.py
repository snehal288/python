#positional argument
def student(name,rno,address,marks):
    print("name is",name)
    print("roll is", rno)
    print("address is", address)
    print("marks is", marks)

#keyword arguments
def computer(RAM,PROCESSOR,HDD):
    print("RAM size is",RAM)
    print("PROCESSOR is", PROCESSOR)
    print("size of HDD", HDD)
#Default argument(should be from right to left order)
def circlearea(radius,PI=3.14):
    print("value of radius",radius)
    print("value of PI", PI)
    return circlearea


#variable number of arguments
def fun(*value):
    print(type(value))
    print("number of arguments are",len(value))


def main():
    student("snehal",11,"nashik",56)

    computer(PROCESSOR="i7",RAM=8,HDD="1TB")
    computer(HDD="5TB",RAM=10,PROCESSOR="i3")

    circlearea(radius=10.25)
    circlearea(radius=13.7,PI=7.12)

    fun(10,20,30)
    fun(11,21,51,101)
    fun()

if __name__=="__main__":
    main()