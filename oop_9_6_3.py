number1=2 
number2=5.7 
print(number1+number2) #7.7   

str1="Hello!" 
str2="Python" 
print(str1+str2) #Hello!Python 

print(len("Student")) #7 
print(len(["Python", "C#", "JavaScript"])) #3 
print(len({"firstName": "Jane", "lastName": "Smith"})) #2 

class MyClass:
    def __len__(self):
        return 1000

obj=MyClass()
print(len(obj)) #1000

number=1000
print(len(number))