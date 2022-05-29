import random

# class Book:
#     def __init__(self, title, author, pages,feedbacksN):
#         self.title = title
#         self.author = author
#         self.pages = pages
#         self.feedbacksN=feedbacksN

#     def __str__(self):
#         return f"Title: {self.title}, author: {self.author}, pages: {self.pages}, feedbacksN:{self.feedbacksN}"

#     def __eq__(self, otherObj):
#         if self.author==otherObj.author and self.title==otherObj.title:
#             return True
#         else:
#             return False
    
#     def __gt__(self, otherObj):
#         if self.pages>otherObj.pages:
#             return True
#         else:
#             return False
#     def __getitem__(self,ind):
#         if 0<=ind<=11:
#             return self.feedbacksN[ind]
#         else:
#             return -1
    
# PythonFeedbacks=[random.randint(50,300) for i in range(12)]
# book1=Book("Python Crash Course","Eric Matthes", 624,PythonFeedbacks)
# print(book1[2]) #265

# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def __str__(self):
#         return f"Title: {self.title}, author: {self.author}, pages: {self.pages}"

#     def __eq__(self, otherObj):
#         if self.author==otherObj.author and self.title==otherObj.title:
#             return True
#         else:
#             return False
    
#     def __gt__(self, otherObj):
#         if self.pages>otherObj.pages:
#             return True
#         else:
#             return False

    
    
# book1=Book("Python Crash Course","Eric Matthes", 624)
# book2=Book("JavaScript: The Good Parts","Douglas Crockford", 170)
# book3=Book("Python Crash Course","Eric Matthes", 700)

# print(book1==book3)
# print(book1>book2)

# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def __str__(self):
#         return f"Title: {self.title}, author: {self.author}, pages: {self.pages}"
    
    
# book1=Book("Python Crash Course","Eric Matthes", 624)
# book2=Book("JavaScript: The Good Parts","Douglas Crockford", 170)

# print(book1==book2) #False
# print(book1)

# class Class1:
#     def __new__(cls):
#         print("Hi! I am __new__ magic method.") 
#         return super(Class1, cls).__new__(cls)
    
#     def __init__(self):
#         print("Hi! I am __init__ magic method.")
        

# obj1=Class1()


# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def showInfo(self):
#         print("Title: {}".format(self.title))
#         print("Author: {}".format(self.author))
#         print("Pages: {}".format(self.pages))

# book1=Book("Python Crash Course","Eric Matthes", 624)
# book2=Book("JavaScript: The Good Parts","Douglas Crockford", 170)

# print(book1+book2)

# number1=2
# number2=5.7
# print(number1+number2) #7.7

# str1="Hello!"
# str2="Python"
# print(str1+str2) #Hello!Python

# print(len("Student")) #7
# print(len(["Python", "C#", "JavaScript"])) #3
# print(len({"firstName": "Jane", "lastName": "Smith"})) #2

# class Film:
#     def __init__(self, originalTitle, director, genre):
#         self.originalTitle = originalTitle
#         self.director = director
#         self.genre = genre

#     def showInfo(self):
#         print("Original title: {}".format(self.originalTitle))
#         print("Director: {}".format(self.director))
#         print("Genre: {}".format(self.genre))

# class Book:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def showInfo(self):
#         print("Title: {}".format(self.title))
#         print("Author: {}".format(self.author))
#         print("Pages: {}".format(self.pages))

# film1=Film("The Godfather","Francis Ford Coppola","Crime, drama")
# book1=Book("Python Crash Course","Eric Matthes", 624)

# for item in (film1, book1):
#     item.showInfo()
   
