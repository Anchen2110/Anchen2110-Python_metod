# myVar=1000
# print(type(myVar))

# myVar=[1,2,3,4,5]
# print(type(myVar))

# myVar="Hello"
# print(type(myVar))

# class Student:
#     pass

class Student:

    spec="Computer science"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showInfo(self):
        return f"Student {self.name} is {self.age} years old."

    def showMsg(self, msgText):
        return f"Student {self.name} says '{msgText}'."

student1=Student("Bob",20)
student2=Student("Jane", 18)

print(student1.showInfo())
print(student1.showMsg("Hello!"))

print(student2.showInfo())
print(student2.showMsg("Hi!"))

print("Student's 1 info:")
print(student1.name)
print(student1.age)
print(student1.spec)

print("Student's 2 info:")
print(student2.name)
print(student2.age)
print(student1.spec)


# student1.sayHello()







