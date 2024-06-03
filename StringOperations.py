#Creating strings

#Approach
name="Toheeb"
print(name)

name1=str("welcome")
print(name1)

#  +  *

# str="welcome"
# print(str+" to programming")
#
# print(str * 3)

# str="welcome"
# print(str[1:3]) #el
# print(str[:6]) #welcom
# print(str[4:]) #ome

# print(ord('Z')) #90
# print(chr(90))
# print(len("hello")) #5
# print(max("abc")) #c
# print(min("abc"))
# print(min(2,3,4))

#Membership Operator - in and not in - check existence of string in another string

# str="welcome"
# print("wel" in str) # true
# print("xyz" in str) # false
#
# print("wel" not in str) # false

 #Comparison Operators
# print("tim" == "tie") #false
# print("free" != "freedom") #True
# print("arrow" > "aron") #True
# print("right" >= "left") #True
# print("yellow" <= "fellow") # False
# print("abc" > "") # True

# s="Python"
# for i in s:
#     print(i)

s= "welcome to python"
print(s.isalnum()) #False
print("Welcome".isalpha()) #True
print("2012".isdigit()) #True
print("first Number".isidentifier()) #false
print(s.islower()) #True
print("WELCOME".isupper()) #True
print(" ".isspace()) #True

# print(s.endswith("thon")) #True
# print(s.startswith("good")) #False
# print(s.find("come")) #3
# print(s.find("become")) #-1
# print(s.rfind("o")) #15
# print(s.count("o")) # 3

s= "String in Python"
s1 = s.capitalize()
print(s1) # String in python

s2 = s.title()
print(s2) # String In Python

s3 = s.lower()
print(s3) # string in python

s4 = s.upper()
print(s4) # STRING IN PYTHON

s5 = s.strip()
print(s5) # String in Python
s6 = s.rstrip()
print(s6) # String in Python
s7 = s.swapcase()
print(s7) #sTRING IN pYTHON
s8 = s.replace("in", "on")
print(s8) #Strong on Python

print(s) #String in Python
