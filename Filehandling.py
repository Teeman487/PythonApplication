# file=open("C:\pythonFile.txt", "w") # open file for writing
# file.write('This is my first line\n')
# file.write('This is 2nd line')
# file.close()

#Reading all the data at once
# file=open("C:\pythonFile.txt", "r")
# print(file.read()) #read entire content of file at once
# print(file.read(10)) #read given number of characters from the file
# print(file.readlines()) #read entire content of file at once in array format []
# print(file.readline()) # read the first line
# file.close()

# file=open("C:\pythonFile.txt", "a")
# file.write("This is the Third Line\n")
# file.close()


#Looping
file=open("C:\pythonFile.txt", "r")

for l in file:
    print(l)
file.close()

