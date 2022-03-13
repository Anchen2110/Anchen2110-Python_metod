# users = [
# {'name': 'Hanna', 'age': 10, 'login':'user56'},
# {'name': 'Mark', 'age': 15, 'login':'usER111'},
# {'name': 'Jane', 'age': 17, 'login':'superGirl'},
# {'name': 'Jack', 'age': 7, 'login':'userJack'}
# ]

# sortedUsersbyName=sorted(users, key=lambda x: x['name'])

# print("Users list sorted by name:")
# for user in sortedUsersbyName:
#     for key,value in user.items():
#         print("{}:{}".format(key,value))





# ilmDict={'originalTitle':'Forever',
#         'creator':'Matthew Miller',
#         'rate':8.3,
#         'description':'A 200-year-old man worksin the New York City Morgue trying to find a key to unlock the curse of his immortality.',
#         'years':[2014,2015]
#         }

# for key,value in filmDict.items():
#     print("{}:{}".format(key,value))

# sortedTuples = sorted(filmDict.items(), key=lambda x: x[0])
# print(sortedTuples)

# filmDictSorted=dict(sortedTuples)
# for key,value in filmDictSorted.items():
#     print("{}:{}".format(key,value))

# keyList=list(filmDict.keys())
# print(keyList)
# sortedKeys=sorted(keyList)
# print(sortedKeys)

# for key in sortedKeys:
#     print("{}:{}".format(key,filmDict[key]))

# bookDict={'author': 'Matthes',
#         'title':'Python',
#         'reading age':'12',
#         'language':'English'
#         }

# print("Unsorted book info:")
# for key,value in bookDict.items():
#     print("{}:{}".format(key,value))

# # sortedTuples = sorted(filmDict.items(), key=lambda x: x[0])
# # print(sortedTuples)

# print("Book info sorted by element value:")
# bookDictSorted=dict(sorted(bookDict.items(), key=lambda x: x[1]))
# for key,value in bookDictSorted.items():
#     print("{}:{}".format(key,value))





# users = [
# {'name': 'Hanna', 'age': 10, 'login':'user56'},
# {'name': 'Mark', 'age': 15, 'login':'usER111'},
# {'name': 'Jane', 'age': 17, 'login':'superGirl'},
# {'name': 'Jack', 'age': 7, 'login':'userJack'}
# ]

# keyName=input("Input info type:")
# keyValue=input("Input info value:")

# keyValue=keyValue if keyName!='age' else int(keyValue)

# fl=False

# for user in users:
#     if user.get(keyName)==keyValue:
#         print("Element is found!")
#         for key,val in user.items():
#             print("{}:{}".format(key,val))
#         fl=True
#         break
# if fl==False:
#     print("Element is not found!")

        




users12=list(filter(lambda user: user['age'] >12, users))

for user in users12:
    for key,val in user.items():
        print("{}:{}".format(key,val))
    






        
