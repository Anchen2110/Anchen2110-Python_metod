class WalletFunctor:
    def __init__(self, startCoins=100): 
        self.__startCoins = startCoins
    
    def __call__(self, coins=0):
        return self.__startCoins+coins

# userWallet=WalletFunctor()
# print(f"Start state of user wallet: {userWallet()} coins")
# print(f"State of user wallet after updating to 50 coins: {userWallet(50)} coins")



# botWallet=WalletFunctor(50)
# print(f"Start state of bot wallet: {botWallet()} coins")
# print(f"State of user bot after updating to 20 coins: {botWallet(20)} coins")


class UserPlayer:
    def __init__(self, name):
        self.name=name
        self.__walletSetter=WalletFunctor()
        self.__wallet=self.__walletSetter()
    
    def updateWallet(self,coins=0):
        self.__wallet=self.__walletSetter(coins)
        #self.__wallet(coins)

    def showWallet(self):
        print(f"{self.name}! You have {self.__wallet} coins now.")


# user1=UserPlayer("Joe")
# user1.showWallet()
# user1.updateWallet(50)
# user1.showWallet()

import random


class BotPlayer:
    def __init__(self):
        self.__name=random.choice(["SuperBot","MegaBot","Bot-player"])
        self.__walletSetter=WalletFunctor(50)
        self.__wallet=self.__walletSetter()
    
    def updateWallet(self,coins=0):
        self.__wallet=self.__walletSetter(coins)
        #self.__wallet(coins)

    def showWallet(self):
        print(f"{self.__name}! You have {self.__wallet} coins now.")


bot1=BotPlayer()
bot1.showWallet() 
bot1.updateWallet(20)
bot1.showWallet()  


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