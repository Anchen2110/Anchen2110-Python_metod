from random import randint


def printList(myList):
    for index, elem in enumerate(myList):
        print("element {}: {}".format(index+1, elem))


def generateNum(n):
    nList=[]
    for i in range(n):
        nList.append(randint(11,100))
    return nList



# def myBubbleSort(myList):
#     global C
#     global E
#     print("C={}, E={}".format(C,E))

#     for i in range(len(myList)-1):
#         sortedFlag=True
#         for j in range(len(myList)-i-1):
#             C+=1
#             if myList[j]<myList[j+1]:
#                 E+=1
#                 temp=myList[j]
#                 myList[j]=myList[j+1]
#                 myList[j+1]=temp
#                 sortedFlag=False
#         if sortedFlag:
#             break
#     print("C={}, E={}".format(C,E))

# C=0
# E=0
# numbers1=generateNum(20)

# print("Original list1:")
# printList(numbers1)
# myBubbleSort(numbers1)
# print("Sorted list1:")
# printList(numbers1)

# C=0
# E=0

# numbers2=sorted(numbers1)
# print("Original list2:")
# printList(numbers2)
# myBubbleSort(numbers2)
# print("Sorted list2:")
# printList(numbers2)

# C=0
# E=0

# numbers3=generateNum(10)+[10,9,8,7,6,5,4,3,2,1]

# print("Original list3:")
# printList(numbers3)
# myBubbleSort(numbers3)
# print("Sorted list3:")
# printList(numbers3)





# def InsertionSort(myList,startInd,gapValue):

#     global C
#     global E

#     for i in range(startInd+gapValue,len(myList),gapValue):

#         currentElem = myList[i]
#         currentInd = i

#         C+=1      
#         while currentInd>=gapValue and myList[currentInd-gapValue]>currentElem:
#             myList[currentInd]=myList[currentInd-gapValue]
#             currentInd = currentInd-gapValue
#             E+=1

#         myList[currentInd]=currentElem
#         E+=1

# def ShellSort(myList):
#     global C
#     global E
#     print("C={}, E={}".format(C,E))

    
#     subListN = len(myList)//2
#     step=1
#     while subListN > 0:

#       for startInd in range(subListN):
#         InsertionSort(myList,startInd,subListN)

#       #print("Interval={}. After step {}: {}".format(subListN,step,myList))

#       subListN = subListN // 2
#     print("C={}, E={}".format(C,E))

# C=0
# E=0
# numbers1=generateNum(20)

# print("Original list1:")
# printList(numbers1)
# ShellSort(numbers1)
# print("Sorted list1:")
# printList(numbers1)

# C=0
# E=0

# numbers2=sorted(numbers1,reverse=True)
# print("Original list2:")
# printList(numbers2)
# ShellSort(numbers2)
# print("Sorted list2:")
# printList(numbers2)

# C=0
# E=0

# numbers3=[1,2,3,4,5,6,7,8,9,10]+generateNum(10)

# print("Original list3:")
# printList(numbers3)
# ShellSort(numbers3)
# print("Sorted list3:")
# printList(numbers3)


# def MergeSort(myList):
#     global C
#     global E
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
#             C+=1
#             if leftPart[i] < rightPart[j]:
#                 myList[k] = leftPart[i]
#                 i += 1
#                 E+=1
#             else:
#                 myList[k] = rightPart[j]
#                 j += 1
#                 E+=1

#             k += 1
  
#         # Checking if any element was left in leftPart-list
#         while i < len(leftPart):
#             myList[k] = leftPart[i]
#             i += 1
#             k += 1
#             E+=1

#         # Checking if any element was left in rightPart-list
#         while j < len(rightPart):
#             myList[k] = rightPart[j]
#             j += 1
#             k += 1
#             E+=1
#         #print("temp merge: {}".format(myList))
#         print("C={}, E={}".format(C,E))

# C=0
# E=0
# numbers1=generateNum(20)

# print("Original list1:")
# printList(numbers1)
# MergeSort(numbers1)
# print("Sorted list1:")
# printList(numbers1)

# C=0
# E=0

# numbers2=sorted(numbers1,reverse=True)
# print("Original list2:")
# printList(numbers2)
# MergeSort(numbers2)
# print("Sorted list2:")
# printList(numbers2)

# C=0
# E=0

# numbers3=[1,2,3,4,5,6,7,8,9,10]+generateNum(10)

# print("Original list3:")
# printList(numbers3)
# MergeSort(numbers3)
# print("Sorted list3:")
# printList(numbers3)

def quickSort(myList, start, end):
    if start < end:
        pivot = partition(myList, start, end)
        quickSort(myList, start, pivot-1)
        quickSort(myList, pivot+1, end)
    return myList

def partition(myList, start, end):
    pivot = myList[start]
    left = start+1
    right = end
    done = False
    while not done:
        while left <= right and myList[left] <= pivot:
            left = left + 1
        while myList[right] >= pivot and right >=left:
            right = right -1
        if right < left:
            done= True
        else:
            temp=myList[left]
            myList[left]=myList[right]
            myList[right]=temp
    temp=myList[start]
    myList[start]=myList[right]
    myList[right]=temp
    return right


def quickSort(a,l,r):
    if(l<r):
        p = partition(a,l,r)
        quickSort(a,l,p-1)
        quickSort(a,p+1,r)

def partition(a,l,r):
    i = l-1
    p = a[(l+(r-l))//2]
    for j in range(l,r):
        if a[j] <= p:
            i += 1
            a[i],a[j] = a[j],a[i]
            
    a[i+1],a[r] = a[r],a[i+1]
    return (i+1)


def QuickSort(myList, firstInd, lastInd):

    global C
    global E

    i = firstInd
    j = lastInd
    pivotElem = myList[firstInd + (lastInd - firstInd) // 2] # pivot element in the middle
    while i <= j:
        while myList[i] < pivotElem:
            i += 1
            C+=1
        while myList[j] > pivotElem:
            j -= 1
            C+=1
        C+=1
        if i <= j: # swap 
            E+=1
            myList[i], myList[j] = myList[j], myList[i]
            i += 1
            j -= 1
    if firstInd < j: # sort left part
        QuickSort(myList, firstInd, j)
    if i < lastInd: # sort right part
        QuickSort(myList, i, lastInd)
    
    print("C={}, E={}".format(C,E))
    
    return myList

    # if (firstInd<lastInd):
    #     i=firstInd-1
    #     midInd  = (firstInd+(lastInd-firstInd))//2

    #     for j in range(firstInd,lastInd):
    #         C+=1
    #         if myList[j] <= myList[midInd]:
    #             i += 1
    #             myList[i],myList[j] = myList[j],myList[i]
    #             E+=1
        
    #     myList[i+1],myList[lastInd] = myList[lastInd],myList[i+1]
    #     E+=1

    #     QuickSort(myList,firstInd,i)
    #     QuickSort(myList,i+2,lastInd)




        



    # if len(myList) == 1:
    #     return myList
    # elif len(myList) > 1:
    #     firstInd =0
    #     lastInd=len(myList)-1

    #     midInd  = (firstInd+lastInd)//2
    #     print("midInd : {}, mid elem={}".format(midInd,myList[midInd]))


    #     leftPart = myList[:midInd]
    #     rightPart = myList[midInd+1:]
    #     print("current list before: {}".format(myList))
    #     print("left before: {}".format(leftPart))
    #     print("right before: {}".format(rightPart))

    #     while True:
    #         while myList[firstInd]<=myList[midInd] and firstInd<lastInd:
    #             firstInd+=1
    #         while myList[lastInd]>=myList[midInd] and lastInd>firstInd:
    #             lastInd-=1
    #         # if firstInd<lastInd:
    #         #     temp=myList[firstInd]
    #         #     myList[firstInd]=myList[lastInd]
    #         #     myList[lastInd]=temp

    #         #     firstInd+=1
    #         #     lastInd-=1
    #         if lastInd<=firstInd:
    #             break
    #         else:
    #             temp=myList[firstInd]
    #             myList[firstInd]=myList[lastInd]
    #             myList[lastInd]=temp
        
    #     # temp=myList[firstInd]
    #     # myList[firstInd]=myList[lastInd]
    #     # myList[lastInd]=temp

    #     print("current list after: {}".format(myList))
    #     leftPart = myList[:midInd]
    #     rightPart = myList[midInd+1:]
    #     print("left after: {}".format(leftPart))
    #     print("right after: {}".format(rightPart))

    #     leftPart=QuickSort (leftPart)
    #     rightPart=QuickSort (rightPart)

    #     leftPart=QuickSort (leftPart)
    #     leftPart.append(myList[midInd])

    #     myList=leftPart+rightPart
    #     print(myList)

    #     print("C={}, E={}".format(C,E))
        
    #     return myList

C=0
E=0
numbers1=generateNum(20)

print("Original list1:")
printList(numbers1)
QuickSort(numbers1,0,len(numbers1)-1)
print("Sorted list1:")
printList(numbers1)

C=0
E=0

numbers2=sorted(numbers1,reverse=True)
print("Original list2:")
printList(numbers2)
QuickSort(numbers2,0,len(numbers1)-1)
print("Sorted list2:")
printList(numbers2)

C=0
E=0

numbers3=[1,2,3,4,5,6,7,8,9,10]+generateNum(10)

print("Original list3:")
printList(numbers3)
QuickSort(numbers3,0,len(numbers1)-1)
print("Sorted list3:")
printList(numbers3)







