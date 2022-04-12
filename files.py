try:
    print("We're opening a file...")
    fileHandler = open("../Data/test.txt")
    
except:
    print("We can't open a file. Sorry!")

print("Program is finished. Bye!")

# with open("../Data/newTest.txt") as f:
#    # perform file operations




# fileHandler = open("../Data/newTest.txt")
# #File Handling
# fileHandler.close()

# fileHandler = open("../Data/newTest.txt","a")
# myStrs=["Appended line 1\n","Appended line 2\n"]
# fileHandler.writelines(myStrs)

# fileHandler = open("../Data/newTest.txt","w")
# for i in range(5):
#     fileHandler.write("This is line %d\n" % (i+1))

# fileHandler = open("../Data/newTest.txt","w+")
# n=fileHandler.write("How to Create a Text File in Python?")
# print("We wrote {} symbols. Let's check it.".format(n))
# print(len("How to Create a Text File in Python?"))

# fileHandler = open("../Data/test.txt")
# for line in fileHandler:
#     print(line)

# fileHandler = open("../Data/test.txt")
# lines=fileHandler.readlines()
# print(lines)
# fileHandler = open("../Data/test.txt")

# str1=fileHandler.readline()
# print(str1)

# str2=fileHandler.readline()
# print(str2)


# fileHandler = open("../Data/test.txt")
# str1=fileHandler.readline()
# print(str1)
# rawStr=repr(str1)
# print(rawStr)
# fileHandler = open("../Data/test.txt")
# rawStr=repr(fileHandler.read())
# print (rawStr)

# print("1st part:")
# print (fileHandler.read(6))
# print("2nd part:")
# print (fileHandler.read()) 


# fileHandler = open("../Data/test.txt")
# print (fileHandler.read())


# fileHandler = open("test.txt") # open file in current directory
# if fileHandler:
#     print("File is open")

# 


# if fileHandler:
#     print("File is open")
