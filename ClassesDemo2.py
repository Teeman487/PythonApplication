#Constructor
# class MyClass:
#     def m1(self):
#         print("good morning")
#     def __init__(self):
#         print("this is constructor")
# c=MyClass()
# c.m1()

# Converting local variables into class variables
class MyClass:
    def values(self,val1,val2): # val1 & val2 are local variable
        print(val1)   #here local variable
        print(val2)     #here local variable
        self.val1=val1       #self.val1 is a class variable
        self.val2=val2
    def add(self):
        print(self.val1+self.val2)  # 30

mc=MyClass()
mc.values(10,20)
mc.add()

#or

# class MyClass:
#     def __init__(self,val1,val2): # val1 & val2 are local variable
#         print(val1)   #here local variable
#         print(val2)     #here local variable
#         self.val1=val1       #self.val1 is a class variable
#         self.val2=val2
#     def add(self):
#         print(self.val1+self.val2)  # 30
#
# mc=MyClass(10,20)
# mc.add()

#How to call current class method in another method
# class MyClass:
#     def m1(self):
#         print("this is m1 method")
#         self.m2(100)
#
#     def m2(self,a):
#         print("this is m2 method",a)
#
# mc=MyClass()
# mc.m1()

# Constructor with arguments
# class MyClass:
#      name="kumar"     # class variable
#      def __init__(self,name):
#          print(name)    # constructor argument  local
#          print(self.name)  # self rep class variable
#
# mc=MyClass("Toheeb")

class Emp:
    def __init__(self,eid,ename,sal):
        self.eid=eid        # storing local var in now class var
        self.ename=ename
        self.sal=sal

    def display(self):
        print("EmpId:{} EmpName:{} EmpSal{}".format(self.eid,self.ename,self.sal))
        print("EmpId:%d EmpName:%s EmpSal:%g" %(self.eid,self.ename,self.sal))

el=Emp(101,'smith',10000)
el.display()



# __str__  automatically invoke at the time of printing the reference vriable
           # It will retuern string
# a="Toheeb"
# class MyClass:
#     a="Rofia"
#     def marriage(self):
#         return "Married couples"
#
#     def __str__(self):   # self access class variable
#         name=self.a
#         return (a+" loves "+name+" Both "+self.marriage())   # must return a string
#
# c=MyClass()  # c is the reference variable
# print(c.marriage()) #  Explicit                <__main__.MyClass object at 0x000001F5DE7A75C0>
# print(c)            # Implicit



# class Emp:
#     def __init__(self,eid,ename,sal):
#         self.eid=eid        # storing local var in now class var
#         self.ename=ename
#         self.sal=sal
#
#     def __str__(self):   # returns string value
#         return ("EmpId:{} EmpName:{} EmpSal{}".format(self.eid,self.ename,self.sal))
#
# el=Emp(101,'smith',10000)
# # el.display()
# print(el)   # whenever we print the reference var auto str function will be execited


#
# class MyClass:
#     def __del__(self): # del function auto execute when we try to destroy objects
#         print("Destroyed")
#
# c1=MyClass()
# c2=MyClass()
# del c1
# del c2
