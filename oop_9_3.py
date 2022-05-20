class Person:
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

    def getInfo(self):
        return f"Person first name -  {self.firstName}; last name - {self.lastName}; age - {self.age}."

    def getHi(self, msgText):
        return f"{msgText}! I am {self.firstName}."

class Employee (Person):
    def __init__(self, firstName, lastName, age, jobTitle, salary, seniority):
        super().__init__(firstName, lastName, age)
        self.jobTitle=jobTitle
        self.salary=salary
        self.seniority=seniority

    def getInfo(self):
        return super().getInfo()+f"\njobTitle -  {self.jobTitle}; salary - {self.salary}; seniority - {self.seniority}."

    def getSickLeavePerc(self):
        if self.seniority>5:
            return 1
        elif 3<self.seniority<=5:
            return 0.75
        else:
            return 0.5

employee1=Employee("Kate","Smith",20,"HR",2500,7)
print(employee1.getHi("Hello"))
print(employee1.getInfo())
print("The percentage of salary in case of sick leave will be {}%".format(employee1.getSickLeavePerc()*100))


# class Person:

#     def __init__(self, firstName, lastName, age):
#         self.firstName = firstName
#         self.lastName = lastName
#         self.age = age

#     def getInfo(self):
#         return f"Person first name -  {self.firstName}; last name - {self.lastName}; age - {self.age}."

#     def getHi(self, msgText):
#         return f"{msgText}! I am {self.firstName}."


# # person1=Person("Joe","Black",30)
# # person2=Person("Kate","Smith",20)

# # print(person1.showInfo())
# # print(person2.showInfo())

# # print(person1.sayHi("Hi"))
# # print(person2.sayHi("Hello"))


# class Student(Person):
#     spec="Computer Science"

#     def isSuccessful(self,meanScore):
#         return True if meanScore>=75 else False
    

# student1=Student("Joe","Black",30)

# print(student1.getInfo())
# print(student1.getHi("Morning"))

# print(f"Is {student1.firstName} successful student?.{student1.isSuccessful(85)}")




# # class Student(Person):
# #     spec="Computer Science"

# #     def __init__(self, firstName, lastName, age, score):
# #         super().__init__(firstName, lastName, age)
# #         self.score = score

# #     def isSuccessful(self):
# #         if self.score>=75:
# #             return True
# #         else:
# #             return False

# # student1=Student("Joe","Black",30, 78)

# # print(student1.showInfo())
# # print(student1.sayHi("Morning"))

# # print(f"Is {student1.firstName} successful student?.{student1.isSuccessful()}")


# # class Student(Person):
# #     spec="Computer Science"

# #     def __init__(self, firstName, lastName, age, score):
# #         super().__init__(firstName, lastName, age)
# #         self.score = score

# #     def getInfo(self):
# #         return super().getInfo()+f"score - {self.score}"
    
# #     def isSuccessful(self):
# #         return True if self.score>=75 else False
# #         # if self.score>=75:
# #         #     return True
# #         # else:
# #         #     return False

# # student1=Student("Joe","Black",30, 78)

# # print(student1.getInfo())
# # print(student1.isSuccessful())



# # student2=Student("Jane", 18)

# # print(student1.showInfo())