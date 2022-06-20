class MyMetaClass3(type):
    def __new__(cls, name, bases, dict, **kwargs):
        resultCls=super().__new__(cls, name, bases,dict)
        if kwargs:
            for key, value in kwargs.items():
                setattr(resultCls, key, value)
        return resultCls
    
    

class User(metaclass=MyMetaClass3, firstName='Joe', age=15):
    attr=100

class Book(metaclass=MyMetaClass3, title='Python', price=15.78):
    attr=100

obj1=User()
print(obj1.firstName)
print(obj1.age)

obj2=Book()
print(obj2.title)
print(obj2.price)





# class MyMetaClass2(type):
#     def __new__(cls, name, bases, dict):
#         resultCls=super().__new__(cls, name, bases, dict)
#         if 'id' not in dict.keys():
#             print(f"No 'id' attr. in the class '{name}'! Let's add it.")
#             resultCls.id=0       
#         return resultCls

    
    

# class User(metaclass=MyMetaClass2):
#     attr=100

# obj=User()
# print(obj.id)


# class MyMetaClass1(type):
#     def __new__(cls, name, bases, dict):
#         if 'id' not in dict.keys(): 
#             print(f"No 'id' attr. in the class '{name}'! ")
#         else:
#             nMethods = {key: value for key, value in dict.items() if callable(value)}
#             if len(nMethods)>3:
#                 print(f"More than 3 methods in the class '{name}'! ")
#             else:
#                 print(f"Class '{name}' is creating...")            
#                 return super().__new__(cls, name, bases, dict)
    
 
# class MyClass1(metaclass=MyMetaClass1):
#     attr=100

# class MyClass2(metaclass=MyMetaClass1):
#     attr=100
#     id=1

#     def method1(self):
#         pass

#     def method2(self):
#         pass

#     def method3(self):
#         pass

# class MyClass3(metaclass=MyMetaClass1):
#     id=2

#     def method1(self):
#         pass

#     def method2(self):
#         pass

#     def method3(self):
#         pass

#     def method4(self):
#         pass
    




# class MyMetaClass1(type):
#     def __new__(cls, name, bases, dict):
#         if 'id' not in dict.keys(): 
#             print(f"No 'id' attr. in the class '{name}'! ")
#         else:
#             print(f"Class '{name}' is creating...")            
#             return super().__new__(cls, name, bases, dict)
    
 
# class MyClass1(metaclass=MyMetaClass1):
#     attr=100

# class MyClass2(metaclass=MyMetaClass1):
#     attr=100
#     id=1
# class MyMetaClass1(type):
#     def __new__(cls, name, bases, dict):
#         print("'Hello' from__new__()!")
#         print("Type of the class being created ", cls)
#         print("Name of the class being created:", name)
#         print("Tuple of base classes: ", bases)
#         print("Dictionary of attr.: ", dict)
       
#         return super().__new__(cls, name, bases, dict)
    
 
# class MyClass1(metaclass=MyMetaClass1):
#     attr=100

# class MyMetaClass1(type):
#     def __new__(cls, name, bases, dict):
#         print("'Hello' from__new__()!")
#         print("Type of the class being created ", cls)
#         print("Name of the class being created:", name)
#         print("Tuple of base classes: ", bases)
#         print("Dictionary of attr.: ", dict)
       
#         return type.__new__(cls, name, bases, dict)
    
 
# class MyClass1(metaclass=MyMetaClass1):
#     attr=100


#obj=MyClass1()

   # def __init__(self, name, bases, dict):
    #     print("'Hello' from__init__()!")

    # def __call__(self, *args, **kwargs):
    #     print("'Hello' from__call__()!")


class MyMetaClass1(type):
    pass

class MyClass1(metaclass=MyMetaClass1):
    pass

print(type(MyMetaClass1))
print(type(MyClass1))