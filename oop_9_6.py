def method1(self):
    print(self.prop1)

MyClass2=type("MyClass2",(),{"prop1":"Hello","method1":method1})

myObj2 = MyClass2()
print(myObj2.prop1)
myObj2.method1()

MyClass2.prop2=100

myObj3 = MyClass2()
print(myObj2.prop2)




# class MyClass1():
#     pass

# MyClass1=type("MyClass1",(),{})

# myObj1 = MyClass1()
# print(myObj1)
# print(type(myObj1))



# MyClass = type('MyClass', (BaseClass), clsDict)

# class MyClass1():
#     pass

# myObj1 = MyClass1()
# print(myObj1)
# print(type(myObj1))

# print(type(type(myObj1)))

# myNumber=10
# myStr="Admin"
# myList=[1,2,3]

# print(type(myNumber))
# print(type(type(myNumber)))

# print(type(myStr))
# print(type(type(myStr)))

# print(type(myList))
# print(type(type(myList)))