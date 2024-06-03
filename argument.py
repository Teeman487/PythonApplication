# def sum(*args):
#     s=0
#     for i in args:
#         s+=i  # s=s+i
#     print("sum is ",s)
#
# sum(10,20,30,40)

# def mu_three(a,b,c):
#     print(a,b,c)
# args=[1,2,3]   #List
#
# mu_three(*args)


#Ex1
def my_three(a,b,c):
    print(a,b,c)

a={'a':"one", 'b':"two", 'c':"three"}
my_three(**a)


#Ex2

# def my_fumc(**kargs):
#     for i,j in kargs.items():
#         print(i,j)
#
# my_fumc(name='tom',spot='football',roll=10, heigh=5)