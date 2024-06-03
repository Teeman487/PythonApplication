# list1=list() # Create an empty list
# print(list1)

# list2=list[22,31,61]
# print(list2)  # []

# list3=list(["tom", "tom", "Akinade"])
# print(list3)

# list4=list("python")
# print(list4) #['p', 'y', 't', 'h', 'o', 'n']

# list5=list(["Python"])
# print(list5) #['Python']

#Accessing Elements in List
# l=[1,2,3,4,5]
# print(l[1])  #2
# print(l[-1]) #5
# print(l[0]) #1

#List Command Operations
# list1 = [2,3,4,1,32]
# print(2 in list1) #True
# print(33 not in list1) # True
# print(len(list1)) #5
# print(min(list1)) #1
# print(sum(list1)) #42

#List slicing
# list =[11,33,44,66,788,1]
# print(list[0:5]) # [11, 33, 44, 66, 788]
# print(list[:3]) # [11, 33, 44]
# print(list[2:]) #[44, 66, 788, 1]


# list1=[11,33]
# list2=[1,9]
#
# list3=list1+list2 #[11, 33, 1, 9]
# print(list3)
#
# list4=[1,2,3,4]
# list5=list4 *3 # [1, 2, 3, 4, 1, 2, 3, 4, 1, 2, 3, 4]
# print(list5)


# list=[1,2,3,4,5]
# for i in list:
#     print(i, end=" ") # 1 2 3 4 5

# Commonly used list methods with return type
# list1=[2,3,4,1,32,4]
# list1.append(19)
# print(list1) # [2, 3, 4, 1, 32, 4, 19]
#
# print(list1.count(4)) #2
# print(list1.index(4))
#
# list2=[99,54]
# list1.extend(list2)
# print(list1) # [2, 3, 4, 1, 32, 4, 19, 99, 54]
list1 = [2, 3, 4, 1, 32, 4, 19, 99, 54]

print(list1.index(32))
list1.insert(1,'hello') # [2, 'hello', 3, 4, 1, 32, 4, 19, 99, 54]
print(list1)

print(list1.pop(2)) # 3
print(list1) # [2, 'hello', 4, 1, 32, 4, 19, 99, 54]
#
list1.remove(32)
print(list1) # [2, 'hello', 4, 1, 4, 19, 99, 54]
#
list1.reverse()
print(list1) # [54, 99, 19, 4, 1, 4, 'hello', 2]

# list1.sort()
# print(list1)


#List Comprehension

# for x in range(10):
#     print(x) # 0 1 2 3 ...9


# list1=[x for x in range(10)]
# print("Print list..",list1) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


for x in range(10):
    if (x%2 == 0):
        print(x)
list1=[x for x in range(10) if x%2 == 0]
print(list1)
