word1=input("1st word:")
word2=input("2nd word:")

if set(word1)==set(word2):
    print("Yes")
else:
    print("No")

# usersApp1=['user134','admin56','superBob','student','spider34']
# usersApp2=['fifa56','user134','studGood','admin56','spider34']

# print("App1+App2 users:")
# print(set(usersApp1)&set(usersApp2))

# print("App1 users only:")
# print(set(usersApp1)-set(usersApp2))

# print("App2 users only:")
# print(set(usersApp2)-set(usersApp1))

# print("All users:")
# print(set(usersApp1)|set(usersApp2))



# allPizzaTypes=['Veggie','Pepperoni','Meat','Margherita','Meat','BBQ Chicken','Hawaiian','Veggie']

# uniquePizzaTypes=list(set(allPizzaTypes))
# print(uniquePizzaTypes) 
#['BBQ Chicken', 'Veggie', 'Meat', 'Margherita', 'Hawaiian', 'Pepperoni']

# frozenA = frozenset(['Hanna','Joe','Kate'])
# frozenB = frozenset(['Bob','Joe','Jane','Kate','Jack'])

# print("frozenA:",frozenA)
# print("frozenB:",frozenB)

# print("Intersection of frozensets:")
# print(frozenA&frozenB) 
# print(frozenA.intersection(frozenB))

# print("Union of frozensets:")
# print(frozenA|frozenB) 
# print(frozenA.union(frozenB))

# print("Difference of two frozensets:")
# print(frozenB-frozenA) 
# print(frozenB.difference(frozenA))
# frozenA.add('user')

# frozenB.remove('Bob')



# scores={1,2,3,4,5,6,7,8,9,10,11,12}

# print("Min score is", min(scores))
# print("Max score is", max(scores))
# print("Sum of scores:", sum(scores))



# studSet={'Bob','Joe','Jane','Kate','Jack'}

# print("We have {} students in our group.".format(len(studSet)))
# for ind,item in enumerate(studSet):
#     print(ind,item)



# studGroup1={'Hanna','Joe','Kate'}
# studGroup2={'Bob','Joe','Jane','Kate','Jack'}
# print("studGroup1:",studGroup1)
# print("studGroup2:",studGroup2)

# print("Intersection of sets:")
# print(studGroup1&studGroup2) #
# print(studGroup1.intersection(studGroup2))

# print("Union of sets:")
# print(studGroup1|studGroup2) #
# print(studGroup1.union(studGroup2))

# print("Difference of two sets:")
# print(studGroup2-studGroup1) #
# print(studGroup2.difference(studGroup1))


# mySet = {1, 2, 3, 4, 5}
# print(mySet)

# mySet.discard(4)
# print(mySet)

# mySet.remove(5)
# print(mySet)

# mySet.discard(10)
# print(mySet)


# mySet.remove(10)
# print(mySet)







# mySet = {1, 2, 3}
# print(mySet)

# mySet.add(4)
# print(mySet)

# mySet.update([3, 4, 5])
# print(mySet)

# mySet.update([5, 6, 7], {8, 9})
# print(mySet)


# userNames= {'Joe','Bob','Kate'}
# name=input("Your name:")
# if name in userNames:
#     print("Welcome, ", name)


# userNames= {'Joe','Bob','Kate'}
# for name in userNames:
#     print(name)

# word=input("Your word:")
# for letter in set(word):
#     print(letter)

# mySet1 = {1, 2, 3}
# mySet2= {'Joe','Bob','Kate'}
# mySet3= {23,'Bob',False,(45.6, 12)}

# print("mySet1 - set of numbers:",mySet1)
# print("mySet2 - set of strings:",mySet2)
# print("mySet3 - of mixed datatypes:",mySet3)

# mySet4=set((10,20,30))
# print("mySet4:",mySet4) #{10, 20, 30}

# uniqueUsersName= {'Joe','Bob','Kate','Bob'}
# print(uniqueUsersName) #{'Kate', 'Joe', 'Bob'}

# allUsersName= ['Joe','Bob','Kate','Bob']
# uniqueUsersName=set(allUsersName)
# print(uniqueUsersName) #{'Kate', 'Joe', 'Bob'}

# #passwordsSet={'111',['222','333']}

# myEmptySet=set()
# print(myEmptySet) #set()

# mySetA = {1, 2, 3}
# mySetB = {3, 2, 1}
# print(mySetA==mySetA) #True








