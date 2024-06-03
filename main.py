# #Approach1
# import Operations
# Operations.add(10,20)
# Operations.mu1(10,20)
#
# #Approach2
#
# from Operations import add,mu1
# add(10,20)
# mu1(10,20)
#
# #Approach3
# from Operations import *
# add(10,20)
# mu1(10,20)




#Approach1
# import animal
# import bird
#
# animal.fly()
# animal.color()
#
# bird.fly()
# bird.color()


#Approach2
# from bird import *
# from animal import *
#
# fly()
# color()

#Approach1
# import aModule
# import bModule
#
# obj=aModule.Animal()
# obj.display()
#
# obj2=bModule.Bird()
# obj2.display()

#Approach2
# from aModule import Animal
# from bModule import Bird
#
# obj=Animal()
# obj.display()
#
# obj2=Bird()
# obj2.display()



import mModule
print(dir(mModule.B))