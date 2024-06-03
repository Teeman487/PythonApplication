# print("Program is started")
#
# try:
#     print(10/5) # ZeroDivisionError
# except Exception:
#     print("Entered in to except block - Handled exception")
# except ZeroDivisionError:
#     print("Entered in to except block - Handled ZeroDivision")
# else:
#     print("Entered in to else block...")
# finally:
#     print("Program is completed")
#Case1: Exception occured-->except-->finally
#Case2: Exception occured-->Not handled-->finally
#Case3: Exception Not occured -->No except-->else-->finally



#case1 Thrown exception --> except
#case2  Not thrown exception -> else(executed only if the statement not throw an exception)



# def enterage(age):
#     if age<0:
#         raise ValueError("Only positive integers are allowed")
#     if age %2 == 0:
#         print("age is even")
#     else:
#         print("age is odd")
#
# try:
#    num=-5
#    enterage(num)
# except ValueError:
#     print("only positive integers are allowed")
# except:
#      print("something is wrong")



try:
    number=""
    print("The number is ",number)
except Exception as ex:
    print("Exception:", ex)