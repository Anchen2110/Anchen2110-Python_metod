class WalletFunctor:
    def __init__(self, startCoins=100): 
        self.__startCoins = startCoins
    
    def __call__(self, coins):
        return self.__startCoins+coins

# userWallet=WalletFunctor()
# print(userWallet(50))

# botWallet=WalletFunctor(50)
# print(botWallet(20))

class UserPlayer:
    def __init__(self, name):
        self.name=name
        self.__wallet=WalletFunctor()
    
    def updateWallet(self,coins):
        return self.__wallet(coins)

    def showWallet(self):
        print(f"You have {self.__wallet} coins now.")


# user1=UserPlayer("Joe")
# user1.updateWallet(50)
# user1.showWallet()
    


# class UserPlayer:
#     def __init__(self, name):
#         self.name=name
#         self.__wallet=100

#     def updateWallet(self,coins):
#         self.__wallet+=coins
    
#     def showWallet(self):
#         print(f"You have {self.__wallet} coins now.")


# user1=UserPlayer("Joe")
# user1.updateWallet(50)
# user1.showWallet()