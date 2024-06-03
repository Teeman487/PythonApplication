#private variables can be accessed only within the method
# class myClass:
#     __a=10  # private variable
#     b=3
#     def disp(self):
#         print(self.__a)
#         print(self.b)
# obj= myClass()
# obj.disp()

#print(myClass.__a) # we cannot access bcoz it private


#private methods can be access only within the method
# a=56
# class myClass:
#     x=78
#     x=x+a
#     def __disp1(self):  #private method
#         print("This is display1 method")
#
#     def disp2(self): #part of same class for above
#         print("This is display2 method")
#         self.__disp1()
#         print(a)
#
# obj=myClass()
# obj.disp2()
# print(myClass.x)


#We can access private variables outside if class indirectly using methods
z=89
class myClass:
    __empid=101
    def getempid(self,eid):
      self.__empid=eid
      return eid

    def dispempid(self):
        print(self.__empid)

obj=myClass()
print(obj.getempid(33))
obj.dispempid()
print(myClass.empid)
