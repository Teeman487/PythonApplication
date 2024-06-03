#Creating basic class and object which include methods
# class MyClass:
#     def myFunc(self):
#         pass
#
#     def display(self,name):
#         print("Name is:", name)
#
# mc=MyClass()
# mc.myFunc()
# mc.display('toheeb')

#Instance and static methods
# class MyClass:
#     def m1(self):   # Instance method called using object
#         print("instance method")
#
#     @staticmethod
#     def m2(self): # self here is treated as argument
#         print("static method")
#
# mc=MyClass()
# mc.m1()
#
# MyClass.m2(10)  #By default static method doesnt take a parameter

#static method: those methods can easily be called using class name

#In python we only have static methods not variable
# In java we have both static variables and methods


#Declaring variables inside the class
# class Myclass:
#     a,b=100,200  # class variables
#     def add(self): # self rep class variables
#         print(self.a+self.b)
#     def mul(self):
#         print(self.a*self.b)
# mc=Myclass()
# mc.add()
# mc.mul()

# Local variables. class variables & Global Variables

# i,j=15,25         #Global variables
# class MyClass:
#     a,b=10,20   # class variables
#
#     def add(self,x,y):      #local variables
#         print(x+y)   # accessing local variables
#         print(self.a+self.b)  # accessing class variables
#         print(i+j)    # directly access
#
# mc=MyClass()
# mc.add(100,200)


#Local Variables, class variables &Global variables with same name

# a,b=15,25         #Global variables
# class MyClass:
#     a,b=10,20     # class variables
#
#     def add(self,a,b):
#         print(a+b)     # access local variables
#         print(self.a+self.b)      # class variables
#         print(globals() ['a']+globals()['b'])  # access global variables
#
# mc=MyClass()
# mc.add(100,200)

# Creating multiple objects for one class

# class MyClass:
#     def display(self):
#         print("Good morning")
#
# obj1=MyClass()    #Named object
# obj1.display()
#
# MyClass().display()    #Nameless object
#
# obj2=MyClass()
# obj2.display()

# every object has different memory location, independent



#Named Object & Nameless object


#How to check memory locations of Objects
class MyClass:
    def m1(self):
        pass
c1=MyClass()
c2=MyClass()
c3=c1

print(id(c1))  #id is a function that returns memory location
print(id(c2))
print(id(c3))

print(c1 is not c2)  #True
print(c1 is c3)  #True



