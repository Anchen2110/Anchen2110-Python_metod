# fileHandler = open("test.txt") # open file in current directory
# if fileHandler:
#     print("File is open")

fileHandler = open("../Data/test.txt") # specifying relative path
if fileHandler:
    print("File is open")
    