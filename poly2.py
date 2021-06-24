class c:
    def learnandcode(self):
        print("learning c programming")
class cpp:
    def learnandcode(self):
        print("learn cpp")
class golang:
    def learnandcode(self):
        print("golang")
class developer:
    def coding(self,lang):
        lang.learnandcode()

cobj=c()
cppobj=cpp()
golangobj=golang()
obj=developer()
obj.coding(cobj)
obj.coding(cppobj)
obj.coding(golangobj)
