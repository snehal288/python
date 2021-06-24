class student:
    school="adarsh"              #class variable
    def __init__(self,no1,no2,no3):
        self.m1=no1              #instance variable
        self.m2=no2
        self.m3=no3

    def instance_total(self):    #instance method
        print("inside instance method")
        return self.m1+self.m2+self.m3
    @classmethod                 #decorator
    def class_displayschool(cls):#class method
        print("school name",cls.school)
    @staticmethod
    def static_info():
        print("this class contain the information of school")

def main():
    student.class_displayschool() #calling class method
    obj1=student(50,80,70)        #object creation
    obj2=student(65,80,75)
    ret=obj1.instance_total() #calling instance method
    print("total",ret)
    student.static_info()     #calling static method

if __name__=="__main__":
    main()
