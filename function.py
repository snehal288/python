
# 1 : Function accepts nothing and return nothing
def fun():
    print("Function fun")


# 2 : Function which accepts parameter and returns nothing
def gun(no):
    print("Function gun with parameter :", no)


# 3 : Function which accepts parameter and return the value
def sun(no):
    print("Function sun with parameter :", no)
    return no + 1


# 4 : Function accepts nultple values and return multiple values
def addsub(no1, no2):
    add = no1 + no2
    sub = no1 - no2
    return add, sub


def main():
    fun()
    gun(11)
    ret = sun(10)
    print("Return value of sun is : ", ret)

    ret1, ret2 = addsub(12, 10)
    print("Addition is : ", ret1)
    print("Substrin is : ", ret2)


if __name__ == "__main__":
    main()


