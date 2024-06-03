#  print even numbers between 1 to 10 numbers
# for i in range(2,10,2): # by default starting value is 2 (start value, max value, inc/dec)
#     print(i) # 2  4 6 8

# for i in range(1, 11, 2):  # by default starting value is 2 (start value, max value, inc/dec)
#     print(i)  # 1 3 5 7 9

# for i in range(10, 1, -1):
#     if i==7:
#         continue   # Skips to next iteration
#
#     print(i, end=" , ")  # 10 , 9 , 8  , 6 , 5 , 4 , 3 , 2   #7is skipped

# While loop
# 1.....10
# i=1
# while i<=10:
#
#     i=i+1
#     print(i, end=' ')   #2 3 4 5 6 7 8 9 10 11

# i=1
# while i<=10:
#     print(i, end=' ')  # 1 2 3 4 5 6 7 8 9 10
#     i=i+1


i=10
while i>=1:
    print(i, end=" ")
    i=i-1