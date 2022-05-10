class Person:

    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

    def showInfo(self):
        return f"Person first name -  {self.firstName}; last name - {self.lastName}; age - {self.age}."

    def sayHi(self, msgText):
        return f"{msgText}! I am {self.firstName}."


# person1=Person("Joe","Black",30)
# person2=Person("Kate","Smith",20)

# print(person1.showInfo())
# print(person2.showInfo())

# print(person1.sayHi("Hi"))
# print(person2.sayHi("Hello"))


# class Student(Person):
#     spec="Computer Science"

#     def isSuccessful(self,meanScore):
#         if meanScore>=75:
#             return True
#         else:
#             return False

# student1=Student("Joe","Black",30)

# print(student1.showInfo())
# print(student1.sayHi("Morning"))

# print(f"Is {student1.firsNname} successful student?.{student1.isSuccessful(85)}")




# class Student(Person):
#     spec="Computer Science"

#     def __init__(self, firstName, lastName, age, score):
#         super().__init__(firstName, lastName, age)
#         self.score = score

#     def isSuccessful(self):
#         if self.score>=75:
#             return True
#         else:
#             return False

# student1=Student("Joe","Black",30, 78)

# print(student1.showInfo())
# print(student1.sayHi("Morning"))

# print(f"Is {student1.firstName} successful student?.{student1.isSuccessful()}")


class Student(Person):
    spec="Computer Science"

    def __init__(self, firstName, lastName, age, score):
        super().__init__(firstName, lastName, age)
        self.score = score

    def showInfo(self):
        return super().showInfo()+f"score - {self.score}"
    
    def isSuccessful(self):
        if self.score>=75:
            return True
        else:
            return False

student1=Student("Joe","Black",30, 78)

print(student1.showInfo())



# student2=Student("Jane", 18)

# print(student1.showInfo())