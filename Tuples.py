# t1=()
# t2=(11,25,46)
# t3=([1,2,3,4,5,6,8])
# t4=tuple("abc")
#
# print(t1)
# print(t2)
# print(t3)
# print(t4)
#
# print(min(t2)) # 11
# print(max(t2)) #46
#
# print(sum(t2)) # 82
#
# for i in t3:
#     print(i, end=" , ")
# print()
#

#Slicing Tuples
# z1=(1,15,60,100,20)
z1=('Toheeb', 'Azeez', 'Rafiu', 'Aisha')
print(z1[0:4]) #(1, 15, 60, 100)
print(z1[0:])

print(100 in z1) #True

print(200 in z1) #False
print(200 not in z1) #True