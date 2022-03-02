def QuickSort (myList):
    if len(myList) == 1:
        return myList
    elif len(myList) > 1:
        # midInd  = len(myList)//2
        # print("midInd : {}, mid elem={}".format(midInd,myList[midInd]))

        firstInd =0
        lastInd=len(myList)-1

        midInd  = (firstInd+lastInd)//2
        print("midInd : {}, mid elem={}".format(midInd,myList[midInd]))


        leftPart = myList[:midInd+1]
        rightPart = myList[midInd+1:]
        print("current list before: {}".format(myList))
        print("left before: {}".format(leftPart))
        print("right before: {}".format(rightPart))

        while True:
            while myList[firstInd]<myList[midInd]:
                firstInd+=1
            while myList[lastInd]>myList[midInd]:
                lastInd-=1
            if firstInd<lastInd:
                temp=myList[firstInd]
                myList[firstInd]=myList[lastInd]
                myList[lastInd]=temp

                firstInd+=1
                lastInd-=1
            if firstInd>=lastInd:
                break
        print("current list after: {}".format(myList))
        leftPart = myList[:midInd+1]
        rightPart = myList[midInd+1:]
        print("left after: {}".format(leftPart))
        print("right after: {}".format(rightPart))

        QuickSort (leftPart)
        QuickSort (rightPart)

        myList=leftPart+rightPart
        
        return myList



numbers=[12,8,25,17,33,31,40,42]
print("Original list: {}".format(numbers))


print("Sorted list: {}".format(QuickSort(numbers)))



        


# def MergeSort(myList):
#     if len(myList) > 1:
  
#          # Finding the middle of the list
#         m = len(myList)//2
#         print("m: {}".format(m))
        
  

#         # Splitting a list into left and right parts
#         leftPart = myList[:m]
#         rightPart = myList[m:]
#         print("left: {}".format(leftPart))
#         print("right: {}".format(rightPart))
  
#         # Sorting the left part
#         MergeSort(leftPart)
  
#         # Sorting the right part
#         MergeSort(rightPart)
  
#         #merge steps
#         i = j = k = 0
  
#         # Copy data to sorted list from leftPart-list and rightPart-list
#         while i < len(leftPart) and j < len(rightPart):
#             if leftPart[i] < rightPart[j]:
#                 myList[k] = leftPart[i]
#                 i += 1
#             else:
#                 myList[k] = rightPart[j]
#                 j += 1
#             k += 1
  
#         # Checking if any element was left in leftPart-list
#         while i < len(leftPart):
#             myList[k] = leftPart[i]
#             i += 1
#             k += 1
#         # Checking if any element was left in rightPart-list
#         while j < len(rightPart):
#             myList[k] = rightPart[j]
#             j += 1
#             k += 1
#         print("temp merge: {}".format(myList))





# ShellSort(numbers)


# def ShellSort(myList):
#     subListN = len(myList)//2
#     step=1
#     while subListN > 0:

#       for startInd in range(subListN):
#         InsertionSort(myList,startInd,subListN)

#       print("Interval={}. After step {}: {}".format(subListN,step,myList))

#       subListN = subListN // 2

# def InsertionSort(myList,startInd,gapValue):
#     for i in range(startInd+gapValue,len(myList),gapValue):

#         currentElem = myList[i]
#         currentInd = i

#         while currentInd>=gapValue and myList[currentInd-gapValue]>currentElem:
#             myList[currentInd]=myList[currentInd-gapValue]
#             currentInd = currentInd-gapValue

#         myList[currentInd]=currentElem

# numbers=[33,31,40,8,12,17,25,42]
# print("Original list: {}".format(numbers))

# ShellSort(numbers)
# print("Sorted list: {}".format(numbers))

# def myBubbleSort_v1(myList):
#     for i in range(len(myList)-1):
#         sortedFlag=True
#         for j in range(len(myList)-i-1):
#             if myList[j]<myList[j+1]:
#                 temp=myList[j]
#                 myList[j]=myList[j+1]
#                 myList[j+1]=temp
#                 sortedFlag=False
#         if sortedFlag:
#             break

# def printList(myList):
#     for index, elem in enumerate(myList):
#         print("elemen {}: {}".format(index+1, elem))

# print("Original list:")
# printList(numbers)
# myBubbleSort(numbers)
# print("Sorted list:")
# printList(numbers)


# """ def myBubbleSort(myList):
#     for i in range(len(myList)-1):
#         for j in range(len(myList)-i-1):
#             if myList[j]<myList[j+1]:
#                 temp=myList[j]
#                 myList[j]=myList[j+1]
#                 myList[j+1]=temp """
