# num1=int(input("Enter First Number:")) #10 treated as string
# num2=int(input("Enter second Number:"))  #20 treated as string
#
# print(int(num1)+int(num2))

# num1=float(input("Enter First Decimal Number:")) #10 treated as string
# num2=float(input("Enter second Decimal Number:"))  #20 treated as string
#
# print(num1+num2)

# num1=input("Enter First Decimal Number:") #10 treated as string
# num2=input("Enter second Integer Number:")  #20 treated as string
#
# print(float(num1)+int(num2))  # ValueError: invalid literal for int() with base 10: '22.4'
# float variable can hold integer value
# Integer value can not hold float var

# num1=int(input("Enter First Decimal Number:")) # Accept only Int, int cant absorb float
# print()
# num2=int(input("Enter second Integer Number:")) # cant accept float
# print((num1)+(num2))

# num1=float(input("Enter First Decimal Number:")) # Accept float & Int
# print()
# num2=float(input("Enter second Integer Number:"))
# print((num1)+(num2))


num1=input("Enter First Decimal Number:") # Accept float & Int
print()
num2=input("Enter second Integer Number:")
print(int(num1)+int(num2))
