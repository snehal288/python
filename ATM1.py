
import threading
amount=1000

def atm(func,kulup):
    func(kulup)

def deposit(kulup):
    kulup.acquire()
    value=int(input("enter amount to deposit"))
    global amount
    amount=amount+value
    print("deposit sucessful-balance:",amount)
    kulup.release()
def withdraw(kulup):
    kulup.acquire()
    value=int(input("enter amount to withdraw:"))
    global amount
    if value>amount:
        print("there is no sufficient balance:")
    else:
        amount=amount-value
        print("withdraw sucessful-balance:",amount)
    kulup.release()

def main():
    print("inside main")
    kulup=threading.Lock()
    t1=threading.Thread(target=atm,args=(deposit,kulup,))
    t2=threading.Thread(target=atm,args=(withdraw,kulup,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("ATM application closed")

if __name__=="__main__":
    main()