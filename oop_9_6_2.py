class MyMetaClass1(type):
    def __new__(cls, name, bases, dict):
        print("'Hello' from__new__()!")
        print(cls, name, bases, dict)
        return type.__new__(cls, name, bases, dict)
    
    def __init__(self, name, bases, dict):
        print("'Hello' from__init__()!")

    def __call__(self, *args, **kwargs):
        print("'Hello' from__call__()!")

class MyClass1(metaclass=MyMetaClass1):
    pass


obj=MyClass1()

# class MyMetaClass1(type):
#     pass

# class MyClass1(metaclass=MyMetaClass1):
#     pass

# print(type(MyMetaClass1))
# print(type(MyClass1))