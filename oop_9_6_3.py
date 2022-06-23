from typing import Protocol, List, runtime_checkable

@runtime_checkable
class Item(Protocol):
    price:float
    discount:int

class Product:
    def __init__(self, name, price, disc, producer):
        self.name = name
        self.price = price
        self.disc=disc
        self.producer=producer


class Book:
    def __init__(self, title, author, price, discount):
        self.title = title
        self.author = author
        self.price=price
        self.discount=discount

# def calculateTotalPrice(objs):
#     sum=0
#     for obj in objs:
#         sum+=obj.price*(1-obj.discount/100)
#     return sum

# book1=Book("Python Crash Course","Eric Matthes", 150, 25)
# book2=Book("JavaScript: The Good Parts","Douglas Crockford", 178, 30)

# print (calculateTotalPrice([book1,book2])) #237.1


# def calculateTotalPrice(objs:List[Item]):
#     sum=0
#     for obj in objs:
#         sum+=obj.price*(1-obj.discount/100)
#     return sum

# purchase1 = calculateTotalPrice([
# Book("JavaScript: The Good Parts","Douglas Crockford", 178, 30),
# Book("Python Crash Course","Eric Matthes", 150, 25)
# ])

# print(purchase1) #237.1


# purchase2 = calculateTotalPrice([
# Product('Tea', 100, 15,'Lipton'),
# Book("Python Crash Course","Eric Matthes", 150, 25)
# ])

# print(purchase2)

def calculateTotalPrice(objs:List[Item]):
    sum=0
    for obj in objs:
        if isinstance(obj, Item):
            sum+=obj.price*(1-obj.discount/100)
        else:
            print("Incompatible type")
    return sum

purchase3 = calculateTotalPrice([
Book("JavaScript: The Good Parts","Douglas Crockford", 178, 30),
Product('Tea', 100, 15,'Lipton'),
Book("Python Crash Course","Eric Matthes", 150, 25)
])

print(purchase3) #237.1


# number1=2 
# number2=5.7 
# print(number1+number2) #7.7   

# str1="Hello!" 
# str2="Python" 
# print(str1+str2) #Hello!Python 

# print(len("Student")) #7 
# print(len(["Python", "C#", "JavaScript"])) #3 
# print(len({"firstName": "Jane", "lastName": "Smith"})) #2 

# class MyClass:
#     def __len__(self):
#         return 1000

# obj=MyClass()
# print(len(obj)) #1000

# number=1000
# print(len(number))