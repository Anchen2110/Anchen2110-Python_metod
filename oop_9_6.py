from typing import List, Protocol, runtime_checkable

@runtime_checkable
class Item(Protocol):
    price:float
    discount:int

class Book:
    def __init__(self, title, author, price, discount):
        self.title = title
        self.author = author
        self.price=price
        self.discount=discount

# def calculateTotalPrice(objs:Item):
#     sum=0
#     for obj in objs:
#         sum+=obj.price*(1-obj.discount/100)
#     return sum


book1=Book("Python Crash Course","Eric Matthes", 150, 25)
book2=Book("JavaScript: The Good Parts","Douglas Crockford", 178, 30)

#print (calculateTotalPrice([book1,book2]))  #237.1

class Product:
    def __init__(self, name, price, disc, producer):
        self.name = name
        self.price = price
        self.disc=disc
        self.producer=producer

def calculatePriceWithDisc(obj:Item):
    return obj.price*(1-obj.discount/100)

product1= Product('Tea', 100, 15,'Lipton')

#print(calculatePriceWithDisc(product1))


# def calculateTotalPrice(objs:List[Item]):
#     sum=0
#     for obj in objs:
#         sum+=obj.price*(1-obj.discount/100)
#     return sum

def calculateTotalPrice(objs:List[Item]):
    sum=0
    for obj in objs:
        if isinstance(obj, Item):
            sum+=obj.price*(1-obj.discount/100)
        else:
            print("Incompatible type")
    return sum

purchase1 = calculateTotalPrice([
    Book("JavaScript: The Good Parts","Douglas Crockford", 178, 30),
    Book("Python Crash Course","Eric Matthes", 150, 25)
])

print(purchase1) #237.1

# purchase2 = calculateTotalPrice([
#     Product('Tea', 100, 15,'Lipton'),
#     Book("Python Crash Course","Eric Matthes", 150, 25)
# ])

purchase2 = calculateTotalPrice([
    Book("JavaScript: The Good Parts","Douglas Crockford", 178, 30),
    Product('Tea', 100, 15,'Lipton'),
    Book("Python Crash Course","Eric Matthes", 150, 25)
])

print(purchase2) #237.1



# calculate total a product list
# purchase = calculateTotalPrice([
#     Product('Tea', 100, 15,'Lipton'),
#     Book("Python Crash Course","Eric Matthes", 150, 25)
# ])

# print(purchase)       

# def method1(self):
#     print(self.prop1)

# MyClass2=type("MyClass2",(),{"prop1":"Hello","method1":method1})

# myObj2 = MyClass2()
# print(myObj2.prop1)
# myObj2.method1()

# MyClass2.prop2=100

# myObj3 = MyClass2()
# print(myObj2.prop2) #100




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