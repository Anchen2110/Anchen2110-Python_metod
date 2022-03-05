# def BinarySearch(myList, keyItem):
#     L=0
#     R=len(myList)-1
#     keyFound=False

#     while (L<=R) and (keyFound==False):
#         m=(L+R)//2
        
#         if myList[m]==keyItem:
#             keyFound=True
#         elif myList[m]>keyItem:
#             R=m-1
#         else:
#             L=m+1
        
#     if keyFound:
#         return m
#     else:
#         return -1


# numbers=[2,5,9,12,17,18,21,32]
# key1=17
# key2=29
# indKey1=BinarySearch(numbers, key1)
# indKey2=BinarySearch(numbers, key2)

# for indKey in (indKey1,indKey2):
#     if indKey!=-1:
#         print(indKey)
#     else:
#         print("Item is not found")



# def new_func():
#     def LinearSearchAllKeys(myList, keyItem):
#         indList=[]
#         for i in range(len(myList)):
#           if myList[i] == keyItem:
#              indList.append(i)
    
#         return indList

#     numbers=[40,17,62,90,10,17,11,80,25,17]
#     key1=17
#     key2=29
#     indKey1=LinearSearchAllKeys(numbers, key1)
#     indKey2=LinearSearchAllKeys(numbers, key2)

#     for indKey in (indKey1,indKey2):
#         if len (indKey)!=0:
#             print(indKey)
#         else:
#             print("Search failed")




# def LinearSearch(myList, keyItem):
#    for i in range(len(myList)):
#       if myList[i] == keyItem:
#          return i
#    return -1

# numbers=[40,62,90,10,17,11,80,25]
# print("Original list: {}".format(numbers))

# key1=17
# print("Key element {} is in List in {} position".format(key1,LinearSearch(numbers, key1)))

# key2=29
# print("Key element {} is in List in {} position".format(key2,LinearSearch(numbers, key2)))


# def QuickSort (myList):
#     if len(myList) == 1:
#         return myList
#     elif len(myList) > 1:
#         firstInd =0
#         lastInd=len(myList)-1

#         midInd  = (firstInd+lastInd)//2
#         print("midInd : {}, mid elem={}".format(midInd,myList[midInd]))


#         leftPart = myList[:midInd+1]
#         rightPart = myList[midInd+1:]
#         print("current list before: {}".format(myList))
#         print("left before: {}".format(leftPart))
#         print("right before: {}".format(rightPart))

#         while True:
#             while myList[firstInd]<myList[midInd]:
#                 firstInd+=1
#             while myList[lastInd]>myList[midInd]:
#                 lastInd-=1
#             if firstInd<lastInd:
#                 temp=myList[firstInd]
#                 myList[firstInd]=myList[lastInd]
#                 myList[lastInd]=temp

#                 firstInd+=1
#                 lastInd-=1
#             if firstInd>=lastInd:
#                 break
#         print("current list after: {}".format(myList))
#         leftPart = myList[:midInd+1]
#         rightPart = myList[midInd+1:]
#         print("left after: {}".format(leftPart))
#         print("right after: {}".format(rightPart))

#         QuickSort (leftPart)
#         QuickSort (rightPart)

#         myList=leftPart+rightPart
        
#         return myList



# numbers=[12,8,25,17,33,31,40,42]
# print("Original list: {}".format(numbers))


# print("Sorted list: {}".format(QuickSort(numbers)))



        


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

numbers=[5,2,4,7,6]

def myBubbleSort(myList):
    for i in range(len(myList)-1):
        for j in range(len(myList)-i-1):
            if myList[j]<myList[j+1]:
                temp=myList[j]
                myList[j]=myList[j+1]
                myList[j+1]=temp


def printList(myList):
    for index, elem in enumerate(myList):
        print("element {}: {}".format(index+1, elem))

print("Original list:")
printList(numbers)
myBubbleSort(numbers)
print("Sorted list:")
printList(numbers)





