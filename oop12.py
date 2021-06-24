#public no1
#protected _no2
#private   __no2
class base:
    def __init__(self):
        self.no1=11;     #public member
        self._no2=21     #protected member
        self.__no3=51    #private member
    def fun(self):       #public method
        print(self.no1,self._no2,self.__no3)
    def _fun(self):       #protected method
        print(self.no1,self._no2,self.__no3)
    def __fun(self):       #private method
        print(self.no1,self._no2,self.__no3)
class derived(base):
    def __init__(self):
        base.__init__(self)
    def gun(self):
        print(self.no1)
        print(self._no2)
        #print(self.__no3)  not allowed
        self.fun()
        self._fun()
        #self.__fun()    not allowed

def main():
    bobj=base()
    print(bobj.no1)
    print(bobj._no2)
    #print(bobj.__no3) not allowed
    bobj.fun()
    bobj._fun()
    #bobj.__fun() not allowed
    dobj=derived()
    dobj.gun()

if __name__=="__main__":
    main()