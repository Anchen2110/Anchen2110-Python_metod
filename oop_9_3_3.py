class myBook:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def showBookInfo(self):
        print("Title: {}".format(self.title))
        print("Author: {}".format(self.author))
        print("Pages: {}".format(self.pages))

class myFile:
    def __init__(self, fileSize, src):
        self.fileSize = fileSize
        self.src = src
        

    def showFileProps(self):
        print("File size: {}".format(self.fileSize))
        print("File source: {}".format(self.src))

class myEBook(myBook,myFile):
    def __init__(self,title, author, pages,fileSize, src):
        myBook.__init__(self,title, author, pages)
        myFile.__init__(self,fileSize, src)
        


eBook1=myEBook("Python Crash Course","Eric Matthes", 624, 1024,"https://www.amazon.co.uk/dp/1593276036/?tag=adnruk-21")
eBook1.showBookInfo()
eBook1.showFileProps()


# class myBook:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def showBookInfo(self):
#         print("Title: {}".format(self.title))
#         print("Author: {}".format(self.author))
#         print("Pages: {}".format(self.pages))

# class myFile:
#     def __init__(self, fileSize, src):
#         self.fileSize = fileSize
#         self.src = src
        

#     def showFileProps(self):
#         print("File size: {}".format(self.fileSize))
#         print("File source: {}".format(self.src))

# class myEBook(myBook,myFile):
#     def __init__(self,title, author, pages,fileSize, src):
#         myBook.__init__(self,title, author, pages)
#         myFile.__init__(self,fileSize, src)


# eBook1=myEBook("Python Crash Course","Eric Matthes", 624, 1024,"https://www.amazon.co.uk/dp/1593276036/?tag=adnruk-21")
# eBook1.showBookInfo()
# eBook1.showFileProps()
# eBook1=myEBook("Python Crash Course","Eric Matthes", 624)
# eBook1.showBookInfo()
# eBook1.showFileProps()


# class myBook:
#     def __init__(self, title, author, pages):
#         self.title = title
#         self.author = author
#         self.pages = pages

#     def showBookInfo(self):
#         print("Title: {}".format(self.title))
#         print("Author: {}".format(self.author))
#         print("Pages: {}".format(self.pages))

# class myFile:
#     def __init__(self, fileSize, src):
#         self.fileSize = fileSize
#         self.src = src
        

#     def showFileProps(self):
#         print("File size: {}".format(self.fileSize))
#         print("File source: {}".format(self.src))

# class myEBook(myBook,myFile):
#     pass


# eBook1=myEBook("Python Crash Course","Eric Matthes", 624, 1024,"https://www.amazon.co.uk/dp/1593276036/?tag=adnruk-21")
# eBook1.showBookInfo()
# eBook1.showFileProps()
# # eBook1=myEBook("Python Crash Course","Eric Matthes", 624)
# # eBook1.showBookInfo()
# # eBook1.showFileProps()

        
