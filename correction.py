def askPersonalInfo(): 
    while True: 
        firstName=input("Your first name:") 
        lastName=input("Your last name:") 
        yearBirth=input("Your year of birth:") 
        gender=input("Your gender (M,F):") 
        if firstName=="" or lastName=="" or yearBirth=="" or gender=="" or gender not in ('F','M'): 
            print("Wrong data!") 
        else: 
            return firstName,lastName,yearBirth,gender 

 

def askAdditionalInfo(queryStr): 
    infoInd=1 
    infoList=[] 
    while True: 
        infoName=input("Your {} {} name:".format(queryStr,infoInd)) 
        if infoName=="": 
            print("No info. Stop input") 
            break 
        else: 
            infoList.append(infoName) 
            infoInd+=1 

    if len(infoList)>0: 
        if queryStr=='hobby': 
            print("You have {} hobbies.".format(infoInd-1)) 
        elif queryStr=='programming languages': 
            print("You know {} programming languages.".format(infoInd-1))     
    else: 
        print("You have no info at all") 
    return infoList 

 

userInfo=[] 
userInfo.append(askPersonalInfo()) 
userInfo.append(askAdditionalInfo('hobby')) 
userInfo.append(askAdditionalInfo('programming languages')) 
print(userInfo) 