# import random
# from datetime import date
# class Person:

#     hobby="Cooking"

#     def __init__(self, firstName, lastName, age):
#         # public properties
#         self.firstName = firstName
#         self.lastName = lastName

#         #protecte properties
#         self._age = age

#         #private properties
#         self.__personID=random.randint(1,100)        

#     #private methods
#     def __showID(self):
#         print (self.__personID)
    
#     # public methods
#     def getInfo(self):
#         self.__showID()
#         return f"Person first name -  {self.firstName}; last name - {self.lastName}; age - {self._age}."

#     def sayHi(self, msgText):
#         print(self.getInfo())
#         return f"{msgText}! I am {self.firstName}."

#     #static methods
#     @staticmethod
#     def sayGreetings():
#         print("Nice to meet you!")

#     #class methods
#     @classmethod
#     def setDefaultHobby(cls):
#         cls.hobby="Drawing"
   
#     @classmethod
#     def basedOnBYear(cls,firstName, lastName, bYear):
#         personAge=date.today().year - bYear
#         return cls(firstName, lastName, personAge)

#     @classmethod
#     def basedOnStr(cls,strInf):
#         firstName, lastName,age = strInf.split(' ')
#         return cls(firstName, lastName,age)






# person1=Person("Joe","Black",30)
# print(person1.getInfo())

# person2=Person.basedOnBYear("Kate","Smith",2000)
# print(person2.getInfo())

# person3=Person.basedOnStr("Kate Smith 25")
# print(person3.getInfo())




# import random
# from datetime import date
# class Person:

#     hobby="Cooking"

#     def __init__(self, firstName, lastName, age):
#         # public properties
#         self.firstName = firstName
#         self.lastName = lastName

#         #protecte properties
#         self._age = age

#         #private properties
#         self.__personID=random.randint(1,100)        

#     #private methods
#     def __showID(self):
#         print (self.__personID)
    
#     # public methods
#     def getInfo(self):
#         self.__showID()
#         return f"Person first name -  {self.firstName}; last name - {self.lastName}; age - {self._age}."

#     def sayHi(self, msgText):
#         print(self.getInfo())
#         return f"{msgText}! I am {self.firstName}."

#     #static methods
#     @staticmethod
#     def sayGreetings():
#         print("Nice to meet you!")

#     #class methods
#     @classmethod
#     def setDefaultHobby(cls):
#         cls.hobby="Drawing"
   
#     @classmethod
#     def basedOnBYear(cls,firstName, lastName, bYear):
#         personAge=date.today().year - bYear
#         return cls(firstName, lastName, personAge)





# person1=Person("Joe","Black",30)
# print(person1.getInfo())

# person2=Person.basedOnBYear("Kate","Smith",2000)
# print(person2.getInfo())


# import random
# class Person:

#     hobby="Cooking"

#     def __init__(self, firstName, lastName, age):
#         # public properties
#         self.firstName = firstName
#         self.lastName = lastName

#         #protecte properties
#         self._age = age

#         #private properties
#         self.__personID=random.randint(1,100)        

#     #private methods
#     def __showID(self):
#         print (self.__personID)
    
#     # public methods
#     def showInfo(self):
#         self.__showID()
#         return f"Person first name -  {self.firstName}; last name - {self.lastName}; age - {self._age}."

#     def sayHi(self, msgText):
#         print(self.showInfo())
#         return f"{msgText}! I am {self.firstName}."

#     #static methods
#     @staticmethod
#     def sayGreetings():
#         print("Nice to meet you!")

#     #class methods
#     @classmethod
#     def setDefaultHobby(cls):
#         cls.hobby="Drawing"



# person1=Person("Joe","Black",30)
# print(person1.hobby)

# Person.setDefaultHobby()

# person2=Person("Kate","Smith",20)
# print(person2.hobby)

# person3=Person("Bob","Gordon",40)
# print(person3.hobby)


# import random
# class Person:

#     def __init__(self, firstName, lastName, age):
#         # public properties
#         self.firstName = firstName
#         self.lastName = lastName

#         #protecte properties
#         self._age = age

#         #private properties
#         self.__personID=random.randint(1,100)        

#     #private methods
#     def __showID(self):
#         print (self.__personID)
    
#     # public methods
#     def showInfo(self):
#         self.__showID()
#         return f"Person first name -  {self.firstName}; last name - {self.lastName}; age - {self._age}."

#     def sayHi(self, msgText):
#         print(self.showInfo())
#         return f"{msgText}! I am {self.firstName}."

#     #static methods
#     @staticmethod
#     def sayGreetings():
#         print("Nice to meet you!")

# person1=Person("Joe","Black",30)
# person1.sayGreetings()



import random
class Person:

    def __init__(self, firstName, lastName, age):
        # public properties
        self.firstName = firstName
        self.lastName = lastName

        #protected properties
        self._age = age

        #private properties
        self.__personID=random.randint(1,100)        

    #protected methods
    def _getFullName(self):
        return f"Person full name:{self.firstName} {self.lastName}"

        
    #private methods
    def __showID(self):
        print (self.__personID)
    
    # public methods
    def getInfo(self):
        self.__showID()
        return f"Person first name -  {self.firstName}; last name - {self.lastName}; age - {self._age}."

    def getHi(self, msgText):
        print(self.showInfo())
        return f"{msgText}! I am {self.firstName}."

    def sayGreetings():
        print("Nice to meet you!")

person1=Person("Joe","Black",30)
print(person1._getFullName())
# person1.sayGreetings()
# print(person1.showInfo())



class Employee(Person):
    def __init__(self, firstName, lastName, age, salary):
        super().__init__(firstName, lastName, age)
        self.salary = salary

    def isRetiree(self):
        print(self.getInfo())
        if self._age>60:
            print(f"{self.firstName} is retiree")
        else:
            print(f"{self.firstName} is not retiree")

    def changeAge(self, newAge):
        self._age=newAge

    def showEmployeeID(self):
        print(self.__personID)
        #self.__showID()


# employee1=Employee("Joe","Black",30, 3000)
# employee1.isRetiree()

# employee1.showEmployeeID()

# employee1.changeAge(65)
# employee1.isRetiree()


# employee1._age=20
# print(employee1.showInfo())

# class Person:

#     def __init__(self, firstName, lastName, age):
#         # public properties
#         self.firstName = firstName
#         self.lastName = lastName

#         #protected properties
#         self._age = age

#     # public methods
#     def showInfo(self):
#         return f"Person first name -  {self.firstName}; last name - {self.lastName}; age - {self._age}."

#     def sayHi(self, msgText):
#         print(self.showInfo())
#         return f"{msgText}! I am {self.firstName}."



# class Employee(Person):
#     def __init__(self, firstName, lastName, age, salary):
#         super().__init__(firstName, lastName, age)
#         self.salary = salary

#     def isRetiree(self):
#         print(self.showInfo())
#         if self._age>60:
#             print(f"{self.firstName} is retiree")
#         else:
#             print(f"{self.firstName} is not retiree")

#     def changeAge(self, newAge):
#         self._age=newAge

# employee1=Employee("Joe","Black",30, 3000)
# employee1.isRetiree()

# employee1.changeAge(65)
# employee1.isRetiree()


# employee1._age=20
# print(employee1.showInfo())


# person1=Person("Joe","Black",30)
# print(person1.sayHi("Hi"))

# print(person1._spec)
# person1._spec="SE"
# print(person1._spec)


# class Person:

#     def __init__(self, firstName, lastName, age):
#         # public properties
#         self.firstName = firstName
#         self.lastName = lastName
#         self.age = age

#     # public methods
#     def showInfo(self):
#         return f"Person first name -  {self.firstName}; last name - {self.lastName}; age - {self.age}."

#     def sayHi(self, msgText):
#         print(self.showInfo())
#         return f"{msgText}! I am {self.firstName}."

# person1=Person("Joe","Black",30)
# print(person1.sayHi("Hi"))

# class Employee(Person):
#     def __init__(self, firstName, lastName, age, salary):
#         super().__init__(firstName, lastName, age)
#         self.salary = salary

#     def isRetiree(self):
#         print(self.showInfo())
#         if self.age>60:
#             print(f"{self.firstName} is retiree")
#         else:
#             print(f"{self.firstName} is not retiree")

# employee1=Employee("Joe","Black",30, 3000)
# employee1.isRetiree()


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




# class Person:

#     def __init__(self, firstName, lastName, age):
#         # public properties
#         self.firstName = firstName
#         self.lastName = lastName
#         self.age = age

#     # public methods
#     def showInfo(self):
#         return f"Person first name -  {self.firstName}; last name - {self.lastName}; age - {self.age}."

#     def sayHi(self, msgText):
#         return f"{msgText}! I am {self.firstName}."

# person1=Person("Joe","Black",30)
# print(person1.showInfo())
# person1.age=35
# print(person1.showInfo())


# print(person1.sayHi("Hi"))