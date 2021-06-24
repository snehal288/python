def substraction(no1, no2): #100
    return no1 - no2
def subdecorator(fun_name): #200 fun_name=100
    def updator(a,b):       #300
        if a<b:
            a,b=b,a
        return fun_name(a,b) #return call 100(6,3)->3
    return updator          #return 300
def main():                 #400
    sub=subdecorator(substraction) #call 200(100) sub=300
    print("enter first no")       #6
    value1=int(input())
    print("enter second no")     #3
    value2=int(input())
    ret = sub(value1,value2)     #call 300(6,3)->3
    print("sub is", ret)
if __name__ == "__main__":
    main()                  #call 400