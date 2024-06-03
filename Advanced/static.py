class Math:

    c_var=100

    @staticmethod  # defines a static method of a class
    def add(x,y):
        return x+y
    def sub(k,z):
        return k-z

print(Math.add(3,5))
print(Math.sub(7,2))
print(Math.c_var)





# class MyClass:
#     def values(self,val1,val2): # val1 & val2 are local variable
#         print(val1)   #here local variable
#         print(val2)     #here local variable
#         self.val1=val1       #self.val1 is a class variable
#         self.val2=val2
#     def add(self):
#         print(self.val1+self.val2)  # 30
#
# mc=MyClass()
# mc.values(10,20)
# MyClass.add()
# # mc.add()