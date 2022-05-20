class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def showInfo(self):
        print("Title: {}".format(self.title))
        print("Author: {}".format(self.author))
        print("Pages: {}".format(self.pages))

book1=Book("Python Crash Course","Eric Matthes", 624)
book2=Book("JavaScript: The Good Parts","Douglas Crockford", 170)

print(book1+book2)

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
   
