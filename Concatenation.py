print(10+10)  # valid

print(10.5+10.5) # valid
print("welcome"+" python")

print(10+10.5) # valid both belongs to Number

print(True+5) #6 valid
# True 1
# False 0
print(True+True) #2 valid
print(False+10) #10 valid


print(10+"welcome") #TypeError: unsupported operand type(s)
print(10.5+"welcome") #TypeError: unsupported operand type(s)

print(True+"welcome") #TypeError: unsupported operand type(s)
