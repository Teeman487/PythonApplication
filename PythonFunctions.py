
# def sum(start,end):
#     result=10
#     for i in range(start,end+1): #5 6 7
#         result=result+i
#     return result
#
#
# s=sum(5,7)
# print(s)

# def sum(start, end):
#     if(start < end):
#         print("start should be less than end")
#         # return    #None
#
#     result=0
#     for i in range(start,end+1):  # 1 2 3 4 5
#         result = result + i       # 0+1+2+3+4+5
#     return result                 # 15
#
# s=sum(1,5)
# print(s)

# def test():
#     i=100
#     return
#
# print(test())

# global_var=12 # global variable
#
# def fun():
#     local_var=100 # local variable
#     print(global_var) # you can access global variables in side function
#
# fun()
#
# print(local_var) #NameError: not defined

# xy=100
#
# def cool():
#     xy=200
#     print(xy) # 200
# cool()
# print(xy)  #100


# t=1
# def increment():
#     # t=10
#     global t  #global variable in the function based on global key
#     t=100
#     print(t)   #100
#
# increment()   #100

# Passing Arguments with default values(positional)
# def fun(i, j=100):
#     print(i,j)
#
# fun(50,250)

# def named_args(name, greeting):
#     print(greeting + " "+name)
#
# named_args("Toheeb", "Hi")  #Positional Arguments
# named_args(name='Toheeb', greeting='hi')  #Keyword Argument

# def my_func(a,b,c):
#     print(a,b,c)
#
# my_func(10,20,30)  #10 20 30   Positional Arguments
# my_func(10,b=20,c=30)  #Positional arguments Keyword arguments
# my_func(10,c=30,b=20)
# my_func(12,b=20,30) #incorrect

def bigger(a,b):
    if a>b:
        return a,b
    else:
        return b,a

s=bigger(100,200)
print(s)
print(type(s)) #<class 'tuple'>