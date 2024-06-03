# __slots__ restricts the attributes that can be added to instances of a class
# allows to explicitly declare which attributes a class can have, potentially saving memory and improving performance
# class MyClass:
#     __slots__= ['x','y']
# obj = MyClass()
# obj.x = 5
# obj.y = 10
#
# x=5
# y=2
# print(x/y)

my_list=[1,2,3,4]
my_list.pop(0)
print(my_list)

f="Hello, Toheeb"
print(f.split(','))