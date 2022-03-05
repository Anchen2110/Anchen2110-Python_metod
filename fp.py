def myGreeting1():
    print("Good morning! Have a nice day!")

def myGreeting2():
    print("Good day! Nice to see you!")

def myGreeting3():
    print("Hey! Long-time no see.")

def myGreeting4():
    print("Good night! See you tomorrow.")

myGreetingsList=(myGreeting1,myGreeting2,myGreeting3,myGreeting4)

# def getGreetingRecipient():
#     greetRecipient=input("name?")
#     print("Dear, ", greetRecipient)

# def sayHello(getRecipientFunction):
#     getRecipientFunction()





def greetingRecipient(greetFunction):
    greetRecipient=input("name?")
    print("Dear, ", greetRecipient)

    greetFunction()


def checkTimeOfDay():
    while True:
        timeOfDay=input("Input time of day (M-morning;D-afternoon;E- everning;N-night):")
        if timeOfDay=="M":
            return myGreetingsList[0]
        elif timeOfDay=="D":
            return myGreetingsList[1]
        elif timeOfDay=="E":
            return myGreetingsList[2]
        elif timeOfDay=="N":
            return myGreetingsList[3]
        else:
            print("Wrong input!")


for i in range(3):
    greetingRecipient(checkTimeOfDay())
    


    

# for myGreeting in myGreetingsList:
#     greetingRecipient(myGreeting)




# sayGoodMorning=myGreeting1
# sayGoodMorning()
