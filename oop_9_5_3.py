class Product:
    def __init__(self, name, price, discountPercentage=25):
        self.name = name
        self.price = price
        self.__discountPercentage =discountPercentage*100 if 0<discountPercentage<1 else discountPercentage
       
    @property 
    def discountPercentage(self):
        return self.__discountPercentage

    @discountPercentage.setter
    def discountPercentage(self,value):
        if 0.1<=value<=0.75:
            self.__discountPercentage=value*100
        elif 10<=value<=75:
             self.__discountPercentage=value
        else:
            print(f"Discoun value less than 10% or greater than 75% is not possible!")

    @discountPercentage.deleter
    def discountPercentage(self):
        print("It is impossible to delete this property!")

    def showInfo(self):
        print (f"name:{self.name}, price with discount:{self.price*(1-self.getDiscount()/100)} grn.")
    
    def toUSD(self,usdExchRate):
        return self.price*(1-self.getDiscount())/usdExchRate


 
item1=Product("Lipton Peach Iced", 42, 30)
del item1.discountPercentage


# class Product:
#     def __init__(self, name, price, discountPercentage=25):
#         self.name = name
#         self.price = price
#         self.__discountPercentage =discountPercentage*100 if 0<discountPercentage<1 else discountPercentage
       
        
#     def getDiscount(self):
#         return self.__discountPercentage

#     def setDiscount(self,value):
#         if 0.1<=value<=0.75:
#             self.__discountPercentage=value*100
#         elif 10<=value<=75:
#              self.__discountPercentage=value
#         else:
#             print(f"Discoun value less than 10% or greater than 75% is not possible!")
    
#     def delDiscount(self):
#         print("It is impossible to delete this property!")

   
#     def showInfo(self):
#         print (f"name:{self.name}, price with discount:{self.price*(1-self.getDiscount()/100)} grn.")
    
#     def toUSD(self,usdExchRate):
#         return self.price*(1-self.getDiscount())/usdExchRate

    

#     discountPercentage = property(
#         fget=getDiscount,
#         fset=setDiscount,
#         fdel=delDiscount, 
#         doc="Product discount property."

#     ) 


 
# item1=Product("Lipton Peach Iced", 42, "Super iced tea!",30)
# del item1.discountPercentage
# help(Product.discountPercentage)

# print(item1.desc)
# del item1.desc




# class Product:
#     def __init__(self, name, price, discountPercentage=25):
#         self.name = name
#         self.price = price
#         self.__discountPercentage =discountPercentage*100 if 0<discountPercentage<1 else discountPercentage

#         # self.__discountPercentage = discountPercentage
    
#     def getDiscount(self):
#         return self.__discountPercentage

#     def setDiscount(self,value):
#         if 0.1<=value<=0.75:
#             self.__discountPercentage=value*100
#         elif 10<=value<=75:
#              self.__discountPercentage=value
#         else:
#             print(f"Discoun value less than 10% or greater than 75% is not possible!")
    
#     def showInfo(self):
#         print (f"name:{self.name}, price with discount:{self.price*(1-self.getDiscount()/100)} grn.")
    
#     def toUSD(self,usdExchRate):
#         return self.price*(1-self.getDiscount())/usdExchRate

#     discountPercentage = property(
#         fget=getDiscount,
#         fset=setDiscount
#     )   
 
# item1=Product("Lipton Peach Iced", 42, 30)
# item1.showInfo()

# print(item1.discountPercentage)

# item1.discountPercentage=0.25
# print(item1.discountPercentage)

# item1.discountPercentage=60
# print(item1.discountPercentage)

# item1.discountPercentage=85
# print(item1.discountPercentage)

# item2=Product("Pure Apple Juice", 28, 0.5)
# item2.showInfo()
# print(item2.discountPercentage)








# # item1.setDiscount(0.8)

# class Product:
#     def __init__(self, name, price, discountPercentage=25):
#         self.name = name
#         self.price = price
#         self._discountPercentage = discountPercentage
    
#     def getDiscount(self):
#         return self._discountPercentage/100

#     def setDiscount(self,value):
#         if 0.1<=value<=0.75:
#             self._discountPercentage=value*100
#         else:
#             print(f"Discoun value less than 10% or greater than 75% is not possible!")

    
#     def showInfo(self):
#         print (f"name:{self.name}, price with discount:{self.price*(1-self.getDiscount())} grn.")
    
#     def toUSD(self,usdExchRate):
#         return self.price*(1-self.getDiscount())/usdExchRate


# item1=Product("Lipton Peach Iced", 42, 30)
# item1.showInfo()

# # item1.setDiscount(0.8)

# item1._discountPercentage=90
# item1.showInfo()

# item2=Product("Pure Apple Juice", 28, 0.8)
# item2.showInfo()



# class Product:
#     def __init__(self, name, price, discountPercentage=25):
#         self.name = name
#         self.price = price
#         self._discountPercentage = discountPercentage
    
#     def getDiscount(self):
#         return self._discountPercentage/100

#     def setDiscount(self,value):
#         self._discountPercentage=value*100    
    
#     def showInfo(self):
#         print (f"name:{self.name}, price with discount:{self.price*(1-self.getDiscount())} grn.")
    
#     def toUSD(self,usdExchRate):
#         return self.price*(1-self.getDiscount())/usdExchRate


# item1=Product("Lipton Peach Iced", 42, 30)
# item2=Product("Pure Apple Juice", 28)

# item1.showInfo()
# print(f"Price in USD$:{item1.toUSD(30)}")
# item2.showInfo()
# print(f"Price in USD$:{item2.toUSD(30)}")

# item1.setDiscount(0.5)
# print(f"New discount for {item1.name} - {item1.getDiscount()*100}%.")

# class Product:
#     def __init__(self, name, price, discount=0.25):
#         self.name = name
#         self.price = price
#         self._discount = discount
    
#     def getDiscount(self):
#         return self._discount

#     def setDiscount(self,value):
#         self._discount=value    
    
#     def showInfo(self):
#         print (f"name:{self.name}, price with discount:{self.price*(1-self.getDiscount())} grn.")
    
#     def toUSD(self,usdExchRate):
#         return self.price*(1-self.getDiscount())/usdExchRate


# item1=Product("Lipton Peach Iced", 42, 0.3)
# item2=Product("Pure Apple Juice", 28)

# item1.showInfo()
# print(f"Price in USD$:{item1.toUSD(30)}")
# item2.showInfo()
# print(f"Price in USD$:{item2.toUSD(30)}")

# item1.setDiscount(0.5)
# print(f"New discount for {item1.name} - {item1.getDiscount()*100}%.")





# class Product:
#     def __init__(self, name, price, discount=0.25):
#         self.name = name
#         self.price = price
#         self.discount = discount
    
#     def showInfo(self):
#         print (f"name:{self.name}, price with discount:{self.price*(1-self.discount)} grn.")
    
#     def toUSD(self,usdExchRate):
#         return self.price*(1-self.discount)/usdExchRate


# item1=Product("Lipton Peach Iced", 42, 0.3)
# item2=Product("Pure Apple Juice", 28)

# item1.showInfo()
# print(f"Price in USD$:{item1.toUSD(30)}")
# item2.showInfo()
# print(f"Price in USD$:{item2.toUSD(30)}")

# item1.discount=0.5
# print(f"New discount for {item1.name} - {item1.discount*100}%.")

