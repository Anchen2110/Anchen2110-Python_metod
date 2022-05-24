class Person:
    def __init__(self, firstName, lastName, age):
        self.firstName = firstName
        self.lastName = lastName
        self.age = age

    def getInfo(self):
        return f"Person first name -  {self.firstName}; last name - {self.lastName}; age - {self.age}."

    def getHi(self, msgText):
        return f"{msgText}! I am {self.firstName}."

class Developer (Person):
    def __init__(self, firstName, lastName, age, jobTitle):
        super().__init__(firstName, lastName, age)
        self.jobTitle=jobTitle
        self.__salary=0
    
    def setBasicSalary(self):
        if self.__rung=='Junior':
            self.__salary=1000
        elif self.__rung=='Middle':
            self.__salary=3000
        elif self.__rung=='Senior':
            self.__salary=5000
        elif self.__rung=='Lead':
            self.__salary=10000
    
    @classmethod
    def setRung(cls,rungName):
        cls.__rung=rungName

    def calculateSalary(self,perc):
        return  self.__salary+self.__salary*perc    

    def getInfo(self):
        return super().getInfo()+f"\njobTitle -  {self.jobTitle};\nrung - {self.__rung};\nbasic salary - {self.__salary}."

Developer.setRung("Junior")

jun1=Developer("Kate","Smith",22,"UI (user interface) designer")
jun2=Developer("Joe","Smith",25,"Back-end developer")

for jun in zip((jun1, jun2),(0.25,0.3)):
    jun[0].setBasicSalary()
    print(jun[0].getInfo())
    print(f"expexted salary:{jun[0].calculateSalary(jun[1])}")


Developer.setRung("Middle")

midl1=Developer("Bob","Dilan",32,"Web developer")
midl2=Developer("Anna","Morning",35,"Data scientist")
midl3=Developer("Helen","Adams",42,"Systems analyst")

for midl in zip((midl1, midl2, midl3),(0.2,0.37, 0.15)):
    midl[0].setBasicSalary()
    print(midl[0].getInfo())
    print(f"expexted salary:{midl[0].calculateSalary(midl[1])}")


# import re

# class myOperator:
       
#     @staticmethod
#     def incrementer(str):
#         numbers=[float(s) for s in re.findall(r'-?\d+\.?\d*', str)]
#         result=[]
#         for number in numbers:
#             result.append(number+1)
#         return result

#     @staticmethod
#     def decrementer(str):
#         numbers=[float(s) for s in re.findall(r'-?\d+\.?\d*', str)]
#         result=[]
#         for number in numbers:
#             result.append(number-1)
#         return result

# userStr="Extract 500 , 100.45, 23.1 and 1000 from my string"
# print(myOperator.incrementer(userStr))
# print(myOperator.decrementer(userStr))