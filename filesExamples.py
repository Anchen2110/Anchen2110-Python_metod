def removeLine(fileIn, fileOut, lineNumber):
    with open(fileIn) as fr:
        lines = fr.readlines()

        counter=1 # position pointer 

        with open(fileOut, 'w') as fw:
            for line in lines:
                if counter != lineNumber:
                    fw.write(line)
                counter += 1

myFile='../Data/Info.txt'
resultFile='../Data/result.txt'

removeLine(myFile, resultFile, 2)




def readFromFile(fileName):
    with open(fileName) as fileHandler:
        data = fileHandler.read()
        print(data)

def removePunctuation(myStr, marks):
    resultStr=""
    for symbol in myStr:
        if symbol not in marks:
            resultStr+=symbol
    return resultStr
            


def reverseFileWords(fileName):
    with open(fileName) as fileHandler:
        data = fileHandler.read()
        data=removePunctuation(data, punctuationSymbols)
        words=data.split()
        reversedWords=reversed(words)

        for word in reversedWords:
            print(word)

    
punctuationSymbols='''!()-;?@#$%:'"\,./*_'''
myFile='../Data/simpleText.txt'

reverseFileWords(myFile)



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




def replaceTextInFile(fileName,originText,newText):
    with open(fileName) as fileHandler:
        data = fileHandler.read()
        data = data.replace(originText, newText)

    with open(fileName,'w') as fileHandler:
        fileHandler.write(data)

def readFromFile(fileName):
    with open(fileName) as fileHandler:
        data = fileHandler.read()
        print(data)
       
    
myFile='../Data/PythonAbout.txt'

print("Original file content:")
readFromFile(myFile)

replaceTextInFile(myFile,'Python','Java Script')

print("New file content:")
readFromFile(myFile)




