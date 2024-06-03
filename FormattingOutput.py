name='john'
age=25
# sal = input("Enter Salary: ")
sal=10000.25

#Approach1
print(name,age,sal)

#Approach2
print("Name is:",name)
print("Age is:",age)
print("Sal is age")

#Approach3: using % operator Here type is imp
# print("Name: %s, Age:%d, salary: %g" %(name,age,sal))
print("Name: %s, Age: %d, salary: %g"%(name,age,sal))
print("Name:{}, Age:{}, Salary:{}".format(name,age,sal))  # most preferred
print("Name:{2}, Age:{2}, Salary:{2}".format(name,age,sal))

# #Approach4: using {} Here value is imp
# print("Name:{} Age:{} Salary:{}".format(name,age,sal))
#
# #Approach 5 using {} Here index & value imp
# print("Name:{0} Age:{2} Salary:{2}".format(name,age,sal)) # index starts from 0


