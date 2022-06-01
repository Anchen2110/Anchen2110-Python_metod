class Product:
    def __init__(self, name, price, discountPercentage=25):
        self.name = name
        self.price = price
        self._discountPercentage = discountPercentage
    
    def getDiscount(self):
        return self._discountPercentage/100

    def setDiscount(self,value):
        self._discountPercentage=value*100    
    
    def showInfo(self):
        print (f"name:{self.name}, price with discount:{self.price*(1-self.getDiscount())} grn.")
    
    def toUSD(self,usdExchRate):
        return self.price*(1-self.getDiscount())/usdExchRate


item1=Product("Lipton Peach Iced", 42, 0.3)
item2=Product("Pure Apple Juice", 28)

item1.showInfo()
print(f"Price in USD$:{item1.toUSD(30)}")
item2.showInfo()
print(f"Price in USD$:{item2.toUSD(30)}")

item1.setDiscount(0.5)
print(f"New discount for {item1.name} - {item1.getDiscount()*100}%.")

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

