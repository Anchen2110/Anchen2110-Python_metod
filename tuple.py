def askPersonalInfo():
    while True:
        firstName=input("Input your first name:")
        lastName=input("Input your last name:")
        yearBirth=input("Input your year of birth:")
        gender=input("Input your gender (M,F):")
        if firstName=="" or lastName=="" or yearBirth=="" or gender=="" or gender not in ('F','M'):
            print("Wrong data!")
        else:
            return firstName,lastName,yearBirth,gender

def askAdditionalInfo(queryStr):
    infoInd=1
    infoList=[]
    while True:
        infoName=input("Name of the {} #{}:".format(queryStr,infoInd))
        if infoName=="":
            print("No info. Input stopped.")
            break
        else:
            infoList.append(infoName)
            infoInd+=1
    if len(infoList)>0:
        if queryStr=='hobby':
            print("You have {} hobbies.".format(infoInd-1))
        elif queryStr=='programming languages':
            print("You know {} programming languages.".format(infoInd-1))
    
    else:
        print("You have no info at all")

    return infoList


userInfo=[]
userInfo.append(askPersonalInfo())
userInfo.append(askAdditionalInfo('hobby'))
userInfo.append(askAdditionalInfo('programming languages'))

print(userInfo)

#print(personalInfo)


# userTypes=('admin','student','teacher','moderator', 'admin')
# if 'student' in userTypes:
#     print('student is correct login' )
#333




# myEmptyTuple1=()
# myEmptyTuple2= tuple()

# print(myEmptyTuple1)
# print(type(myEmptyTuple1))

# print(myEmptyTuple1)
# print(type(myEmptyTuple2))

# myTuple1=('element1', 12, 35.6, False)
# myTuple2=('item1')
# userTypes='admin','student','teacher'
# userName='Jane',

# print("myTuple1:", myTuple1,"type: ", type(myTuple1))
# print("myTuple2:", myTuple2,"type: ", type(myTuple2))
# print("userTypes:", userTypes,"type: ", type(userTypes))
# print("userName:", userName,"type: ", type(userName))

# itemTuple=('item1','item2','item1','item3')
# print(itemTuple) #('item1', 'item2', 'item1', 'item3')

# namesTuple = tuple(('Alex', 'Helen'))
# print(namesTuple) #('Alex', 'Helen')

# userTypes1=('admin','student','teacher','moderator')
# userTypes2=('user1','user2')

# allUsers=userTypes1+userTypes2
# for user in allUsers:
#     print(user)

# userTypes=('admin','student','teacher','moderator', 'admin')
# print(userTypes.count('admin'))  #2

# userTypes=('admin','student','teacher','moderator', 'admin')
# print(userTypes.index('admin')) #0


# userTypes=('admin','student','teacher','moderator')
# for user in userTypes*2:
#     print(user)

# userTypes=('admin','student','teacher','moderator')
# for i in range(len(userTypes)):
#     print(userTypes[i])


# userTypes=('admin','student','teacher','moderator')
# for user in userTypes:
#     print(user)
# userTypes=('admin','student','teacher','moderator')

# user1, *users =userTypes
# print(user1) #admin
# print(users) #['student', 'teacher', 'moderator']


# userTypes=('admin','student','teacher','moderator')

# firstUser, *users, lastUser =userTypes
# print(firstUser) #admin
# print(users) #['student', 'teacher']
# print(lastUser) #moderator
# print(user1) #admin
# print(users) #['student', 'teacher', 'moderator']
# userTypes=('admin','student','teacher','moderator')
# user1, user2,user3,user4 =userTypes
# print(user1)  #admin 
# print(user2)  #student 
# print(user3)  #teacher 
# print(user4)  #moderator 


# userTypes=('admin','student','teacher','moderator')
# userTypes[0]='user'


# print("1st user:", userTypes[0])
# print("last user:", userTypes[len(userTypes)-1])
# print("last user once again:", userTypes[-1])
# print("1st two users:", userTypes[:2])
# print("2nd and 3rd users:", userTypes[1:3])


