import threading
amount=1000

def atm(func):
    func()

def deposit():
    value=int(input("enter amount to deposit"))
    global amount
    amount=amount+value
    print("deposit sucessful-balance",amount)
def withdraw():
    value=int(input("enter amount to withdraw"))
    global amount
    if value>amount:
        print("there is no sufficient balance")
    else:
        amount=amount-value
        print("withdraw sucessful-balance",amount)

def main():
    print("inside main")
    atm(deposit)
    atm(withdraw)

if __name__=="__main__":
    main()