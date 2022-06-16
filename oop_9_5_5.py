class StrDescriptor:
    def __init__(self, minLen, name=""):
        self.name=name
        self.minLen=minLen
  
    def __get__(self, obj, objtype):
        return self.name
  
    def __set__(self, obj, value):
        if not isinstance(value, str):
            print('The value must be a string!')

        elif len(value) == 0:
            print('The value cannot be empty!')

        elif len(value) < self.minLen:
            print('Too short value!')

        else:
            self.name = value

class User:
    firstName=StrDescriptor(3)
    lastName=StrDescriptor(4)

    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName


user1=User("Joe", "Black")
print(f"User1: {user1.firstName} {user1.lastName}")

user1.firstName=""
user1.firstName="AB"

user1.lastName=""
user1.lastName="ABC"

user2=User("AB", "ABC")


# class User:
#     def __init__(self, firstName, lastName):
#         self.__firstName = firstName
#         self.__lastName = lastName

#     @property
#     def firstName(self):
#         return self.__firstName

#     @firstName.setter
#     def firstName(self, value):
#         if not isinstance(value, str):
#             print('The first name must be a string!')

#         elif len(value) == 0:
#             print('The first name cannot be empty!')

#         elif len(value) < 3:
#             print('Too short value for the first name!')

#         self.__firstName = value
    
#     @property
#     def lastName(self):
#         return self.__lastName

#     @lastName.setter
#     def lastName(self, value):
#         if not isinstance(value, str):
#             print('The last name must be a string!')

#         elif len(value) == 0:
#             print('The last name cannot be empty!')

#         elif len(value) < 4:
#             print('Too short value for the last name!')
        
#         else:
#             self.__lastName = value

# user1=User("Joe", "Black")
# print(f"User1: {user1.firstName} {user1.lastName}")

# user1.firstName=""
# user1.firstName="AB"

# user1.lastName=""
# user1.lastName="ABC"



# class MyDescriptor1:  
#     def __init__(self,name=""):
#         print("Descriptor's __init__ was started...")
#         self.name=name
  
#     def __get__(self, obj, objtype):
#         print(f"Descriptor's __get__(instance={obj}, objtype={objtype}) was started...")
#         return "{} was processed".format(self.name)
  
#     def __set__(self, obj, name):
#         print(f"Descriptor's __set__(instance={obj}, name={name}) was started...")
#         if isinstance(name, str):
#             self.name = name
#         else:
#             print("Name should be string")

# class MyDescriptor2:
#     def __init__(self, age = 18):
#         self.age = age

#     def __set__(self, obj, age):
#         if not 18 <= age <= 75:
#             print('Valid age must be in [18, 75]')
#         else:
#             self.age = age

#     def __get__(self, obj, objtype):
#         return self.age


# class User:
#     userName = MyDescriptor1()
#     userAge=MyDescriptor2()

    
# user1 = User()
# user1.userName = "Jack"
# print("User name: {}".format(user1.userName))
# print("User age: {}".format(user1.userAge))

# user1.userAge = 4
# print("User age: {}".format(user1.userAge))
# user1.userAge = 100
# print("User age: {}".format(user1.userAge))
# user1.userAge = 25
# print("User age: {}".format(user1.userAge))






# class MyDescriptor1:  
#     def __init__(self,name=""):
#         print("Descriptor's __init__ was started...")
#         self.name=name
  
#     def __get__(self, obj, objtype):
#         print(f"Descriptor's __get__(instance={obj}, objtype={objtype}) was started...")
#         return "{} was processed".format(self.name)
  
#     def __set__(self, obj, name):
#         print(f"Descriptor's __set__(instance={obj}, name={name}) was started...")
#         if isinstance(name, str):
#             self.name = name
#         else:
#             print("Name should be string")


# class User:
#     userName = MyDescriptor1()
    
# user1 = User()

# user1.userName = "Jack"
# print(user1.userName)

# user1.userName = 111
# print(user1.userName)

# user1.userName = "Jack"
# print(user1.userName)


            