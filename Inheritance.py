# Single Inheritance
# class A:   # 1 parent
#     def m1(self):
#         print("This is m1 method from class A")
#
# class B(A): # 1 child B gets all the functionalities from A
#     def m2(self):
#         print("This is m2 method from class B")
#
# aobj=A()
# aobj.m1()
#
# bobj=B()
# bobj.m1()
# bobj.m2()


# Single Inheritance
# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A):
#      a,b=100,200
#      def m2(self):
#          print(self.a+self.b)
#
# b=B()
# b.m1()
# b.m2()

# Multilevel Inheritance
# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A):
#      a,b=100,200
#      def m2(self):
#          print(self.a+self.b)
#
#
# class C(B):
#     i,j=1,2
#     def m3(self):
#         print(self.i+self.j)
#
# b=B()
# b.m1() #A
# b.m2() #B
#
# c=C()
# c.m1()  #A
# c.m2()  #B
# c.m3()  #C

# Hierarchical Inheritance
# class A:
#     x,y=10,20
#     def m1(self):
#         print(self.x+self.y)
#
# class B(A):
#      a,b=100,200
#      def m2(self):
#          print(self.a+self.b)
#
#
# class C(A):
#     i,j=1,2
#     def m3(self):
#         print(self.i+self.j)
#
# b=B()
# b.m1() #A
# b.m2() #B
#
# c=C()
# c.m1()  #A
# c.m3()  #C

# Multiple Inheritance
class A:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)

class B:
     a,b=100,200
     def m2(self):
         print(self.a+self.b)


class C(A,B):
    i,j=1,2
    def m3(self):
        print(self.i+self.j)

c=C()
c.m1()  #A
c.m2()
c.m3()  #C


#super
# class A:
#     def m1(self):
#         print("This is method from A")
#
# class B(A):
#      def m2(self):
#         print("This is method from B")
#         super().m1() #calling parent class method using super()
#
# b=B()
# b.m2()


# a,b=15,20
# class A:
#     a,b=10,20
# class B(A):
#     a,b=100,200
#     def m1(self,a,b):
#         print(a+b) # local variables  3
#         print(self.a+self.b)  # child class variables  300
#         print(super().a+super().b)  # Parent class variables  # Child class variables
#         print(globals()['a']+globals()['b'])
#
#
# boj=B()
# boj.m1(1,2)

# invoke parent class constructor
# class A:
#     def __init__(self):
#         print("constructor from A")
#
# class B(A):
#     def __init__(self):
#         print("constructor from B")
#         super().__init__() # Approach1 calls parent class constructor
#         A.__init__(self)  # Approach2 calls aprent class constc
#
#
# bobj=B()

