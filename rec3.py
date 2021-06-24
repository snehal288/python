i=1 #define kel variable mhanje memory dili
def fun():
    global i #keyword use karun declare kela variable
    print(i)
    i=i+1
    fun()
def main():
    fun()
if __name__=="__main__":
    main()