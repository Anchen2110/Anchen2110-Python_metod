import os
mainpath = os.path.normpath("D:/Dir")

for path, dirnames, filenames in os.walk(mainpath):
    i=path.rfind("\\")
    dir=path[i+1:]
    print(dir)
    for file in filenames:
        print(" "*len(dir)+file)
      
    
 

        
    
 #print(f"path – {path}")

#  for dir in dirnames:
#      print(dir)
#  print(f"dirnames – {dirnames}")
#  print(f"filenames – {filenames}")

# myStr=input("Введите строку:")
# mySymb=input("Введите символ")
# myW=input("Введите ширину")

# def corrector(userStr,w,mySymb):

#     txt = "{:"+mySymb+"^"+myW+"}"
#     print(txt.format(userStr))
    

# corrector(myStr,myW,mySymb)
# print(result)

# import random

# myStr=input("Введите строку:")
# mySymbols=["a","b","c","d","e","f"]
# randSymb=random.choice(mySymbols)
# print("Случайно вытянули символ - {}".format(randSymb))
# randInd=random.randint(0,len(myStr))
# print("Случайная позиция в предложении будет - {}".format(randInd))





# v=int(input("v=?"))
# N=int(input("N=?"))

# if v<50:
#     x=5
# elif v<100:
#     x=15
# elif v<150:
#     x=25
# else:
#     x=35
# c=x*N
# print("c=",c)