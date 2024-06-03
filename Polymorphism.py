#Overriding a variable
# class Parent:
#     name="scott"
#
# class Child(Parent):
#      name = "David"
#
# obj=Child()
# print(obj.name)   # David


# class Bank:
#      def rateofinterest(self):
#       return 67
# class ICICI(Bank):   # reoccur in childs class
#
#
#       def rateofinterest(self):
#         return 10.5
#
# obj=ICICI()
# print(obj.rateofinterest())
#
# obj1=Bank()
# print(obj1.rateofinterest())



#Overloading Methods

# class Human:
#     def sayHello(self,name=None):
#         if name is not None:
#             print("Hello "+name)
#         else:
#             print("Hello")
#
# obj=Human()
# obj.sayHello("Toheeb")
# obj.sayHello()

class Bird:
    def fly(self,name):
        if name=="parot":
            print("can fly")
        if name=="penguine":
            print("cannot fly")
        if name is None:
            print("No input")

    def fly(self, name,food):
        if name == "parot":
            print("can fly")
        if name == "penguine":
            print("cannot fly")
        if name is None:
            print("No input")
        if food =="Rice":
            print("Eat rice")

obj=Bird()
obj.fly("parot","Rice")