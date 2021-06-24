
# 1 : Function accepts nothing and return nothing
def fun():
    print("Function fun")


# 2 : Function which accerpts parameter and returns nothing
def gun(no):
    print("Function gun with parameter :", no)


# 3 : Function which accepts parameter and return the value
def sun(no):
    print("Function sun with parameter :", no)
    return no + 1

# 4 : Function accepts nultple values and return multiple values
def outer():
    print("inside outer")
    def inner():
        print("inside inner")
    inner()
def mun():
    pass


def main():
    fun()
    gun(11)
    ret = sun(10)
    print("Return value of sun is : ", ret)
    outer()
    mun()


if __name__ == "__main__":
    main()


