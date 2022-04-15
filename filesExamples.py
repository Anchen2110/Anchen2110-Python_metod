def readFromFile(fileName):
    with open(fileName) as fileHandler:
        data = fileHandler.read()
        print(data)

def wordCounter(fileName):
    nWords = 0

    with open(fileName) as fileHandler:
        data = fileHandler.read()
        lines = data.split()
        for word in lines:
            if not word.isnumeric():
                nWords+=1
    return nWords

myFile='../Data/Info.txt'

print("File content:")
readFromFile(myFile)

print("Number of words: {}".format(wordCounter(myFile)))




# def replaceTextInFile(fileName,originText,newText):
#     with open(fileName) as fileHandler:
#         data = fileHandler.read()
#         data = data.replace(originText, newText)

#     with open(fileName,'w') as fileHandler:
#         fileHandler.write(data)

# def readFromFile(fileName):
#     with open(fileName) as fileHandler:
#         data = fileHandler.read()
#         print(data)
       
    
# myFile='../Data/PythonAbout.txt'

# print("Original file content:")
# readFromFile(myFile)

# replaceTextInFile(myFile,'Python','Java Script')

# print("New file content:")
# readFromFile(myFile)




