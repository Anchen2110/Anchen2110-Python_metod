class MyDescriptor1:  
    def __init__(self,name=""):
        print("Descriptor's __init__ was started...")
        self.name=name
  
    def __get__(self, obj, objtype):
        print(f"Descriptor's __get__(instance={obj}, objtype={objtype}) was started...")
        return "{} was processed".format(self.name)
  
    def __set__(self, obj, name):
        print(f"Descriptor's __set__(instance={obj}, name={name}) was started...")
        if isinstance(name, str):
            self.name = name
        else:
            print("Name should be string")

class MyDescriptor2:
    def __init__(self, age = 18):
        self.age = age

    def __set__(self, obj, age):
        if not 18 <= age <= 75:
            print('Valid age must be in [18, 75]')
        else:
            self.age = age

    def __get__(self, obj, objtype):
        return self.age


class User:
    userName = MyDescriptor1()
    userAge=MyDescriptor2()

    
user1 = User()
user1.userName = "Jack"
print("User name: {}".format(user1.userName))
print("User age: {}".format(user1.userAge))

user1.userAge = 4
print("User age: {}".format(user1.userAge))
user1.userAge = 100
print("User age: {}".format(user1.userAge))
user1.userAge = 25
print("User age: {}".format(user1.userAge))




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


            