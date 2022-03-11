# bookDict={'author':'Eric Matthes',
#         'title':'Python Crash Course',
#         'price':14.43,
#         'reading age':'12 years and up',
#         'language':'English'
#         }

# for dictKey, dicVal in bookDict.items():
#         print("{}:{}".format(dictKey,dicVal))


# myDict1= {'key1': 1, 'key2': 20.5, 'key3': True}
# myDict2=myDict1.copy()

# myDict1['key1']=111
# print(myDict1['key1']) #111
# print(myDict2['key1']) #1



# for dictKey in bookDict:
#         print("{}:{}".format(dictKey,bookDict[dictKey]))

# for dictKey in bookDict:
#         print(bookDict[dictKey])

# for dictKey in bookDict:
#         print(dictKey)

# print(bookDict)

# delItem=bookDict.pop("price")
# print("item {} was deleted".format(delItem))
# print(bookDict)

# delItem=bookDict.pop("discount","None")
# print(delItem)






# print(bookDict.keys())
# #dict_keys(['author', 'title', 'price', 'reading age', 'language'])

# keyList=list(bookDict.keys())
# print(keyList) #['author', 'title', 'price', 'reading age', 'language']

# valuesList=list(bookDict.values())
# print(valuesList) 
# #['Eric Matthes', 'Python Crash Course', 14.43, '12 years and up', 'English']

# dictItems=list(bookDict.items())
# print(dictItems)



# # print(bookDict)

# # bookDict.update([('pages', 600), ('discount', True)])
# # print(bookDict)

# # bookDict.update([['pages', 700], ('online', False)])
# # print(bookDict)


# studGr1={'Joe':75,'Bob':92}
# studGr2={'Kate':62,'Joe':90, 'Jack':84}

# print(studGr1) #{'Joe': 75, 'Bob': 92}
# studGr1.update(studGr2)
# print(studGr1) #{'Joe': 90, 'Bob': 92, 'Kate': 62, 'Jack': 84}

# del studGr2['Jack'] 
# print(studGr2) #{'Kate': 62, 'Joe': 90}

# studGr2.clear()
# print(studGr2) #{}







# print(bookDict.get('author')) #Eric Matthes
# print(bookDict.get('page'))   #None
# print(bookDict.get('page',0)) #0

# print(bookDict)

# bookDict['price']=12
# print(bookDict)




# bookDict['pagesN']=350
# print(bookDict)

# infoType=input("What info do you want to know about book?")

# if infoType in bookDict:
#         print(bookDict[infoType])
# else:
#         print("Sorry!")



# newInfo=input("What info about book do you want to add?")
# if newInfo!="":
#         newInfoValue=input("Input value for key '{}':".format(newInfo))
#         if newInfoValue!="":
#                 bookDict[newInfo]=newInfoValue
#         else:
#                 print("No value for for key '{}':".format(newInfo))
# else:
#         print("No key!")





# myDict1= {'key1': 1, 'key2': 20.5, 'key3': True}

# print(myDict1['key1'])  #1

# bookDict={'author':'Eric Matthes',
#         'title':'Python Crash Course',
#         'price':14.43,
#         'reading age':'12 years and up',
#         'language':'English'
#         }

# print(bookDict['author']) #Eric Matthes

# print(bookDict['pages'])



# myEmptyDict1={}
# print(myEmptyDict1)  #{}

# myEmptyDict2=dict()
# print(myEmptyDict2)  #{}


# myDict3 = dict([("a", 111), ("b", 222)])
# myDict4 = dict([["a", 111], ["b", 222]])

# myDict5 = dict(['qw', 'er', 'ty'])
# print(myDict5)  #{'q': 'w', 'e': 'r', 't': 'y'}

# keyList=['a','b']
# valueList=[111,222]

# myDict6=dict(zip(keyList,valueList))

# print(myDict6)  #{'a': 111, 'b': 222}


# myDict7=dict(firstName='Joe', lastName='Smith')
# print(myDict7)  #{'firstName': 'Joe', 'lastName': 'Smith'}







# myDict1= {'key1': 1, 'key2': 20.5, 'key3': True}
# myDict2= {1: 'student', 2: 'admin'}

# print(myDict1)  #{'key1': 1, 'key2': 20.5, 'key3': True}
# print(myDict2)  #{1: 'student', 2: 'admin'}

# bookDict={'author':'Eric Matthes',
#         'title':'Python Crash Course',
#         'price':14.43,
#         'reading age':'12 years and up',
#         'language':'English'
#         }
# print(len(bookDict))  #5

