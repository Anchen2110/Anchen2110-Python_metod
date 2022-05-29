userLogs=['Admin123','superUSER','GOODstudent']
userBYears=[2000, 2010, 2005]

def listMaker1(myList):
    result=[]
    for item in myList:
        result.append(item.lower())
    return result


def listMaker2(myList):
    result=[]
    for item in myList:
        result.append(2022-item)
    return result

newList1=listMaker1(userBYears)
newList2=listMaker2(userLogs)

newList1=listMaker1(userLogs)
newList2=listMaker2(userBYears)

print(newList1)
print(newList2)

# def defineStudSuccess(name,score):
#     if score>=90:
#         print("{} has excellent level".format(name))
#     elif 75<=score<90:
#         print("{} has good level".format(name))
#     elif 60<=score<75:
#         print("{} has average level".format(name))
#     else:
#         print("{} has poor level".format(name))

# def definePupSuccess(name,score):
#     if score>=10:
#         print("{} has excellent level".format(name))
#     elif 7<=score<10:
#         print("{} has good level".format(name))
#     elif 4<=score<7:
#         print("{} has average level".format(name))
#     else:
#         print("{} has poor level".format(name))

# defineStudSuccess("Jane",78)
# defineStudSuccess("Bob",6)







# myVar=1000
# print(type(myVar))

# myVar=[1,2,3,4,5]
# print(type(myVar))

# myVar="Hello"
# print(type(myVar))

# class Student:
#     pass

# class Student:
#     age=20
#     name="Bob"

# student1=Student()
# student2=Student()

# print(student1.name)

# class Student:

#     spec="Computer science"

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def showInfo(self):
#         return f"Student {self.name} is {self.age} years old."

#     def showMsg(self, msgText):
#         return f"Student {self.name} says '{msgText}'."

# student1=Student("Bob",20)
# student2=Student("Jane", 18)

# print(student1.showInfo())
# print(student1.showMsg("Hello!"))

# print(student2.showInfo())
# print(student2.showMsg("Hi!"))

# print("Student's 1 info:")
# print(student1.name)
# print(student1.age)
# print(student1.spec)

# print("Student's 2 info:")
# print(student2.name)
# print(student2.age)
# print(student1.spec)


# student1.sayHello()







