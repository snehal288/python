class demo:
    def __init__(self):
        self.public=10
        self._protected=20
        self.__private=30
    def publicfun(self):
        print("public fun")
        self.__privatefun() #only called by public

    def _protectedfun(self):
        print("protected fun")

    def __privatefun(self):
        print("private fun")

obj=demo()
print(obj.public)
print(obj._protected)
obj.publicfun()
obj._protectedfun()
obj.fun()
#obj.__privatefun()
#print(obj.__private)