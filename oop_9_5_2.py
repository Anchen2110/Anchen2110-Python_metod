pricesUSD=[100.34,35,67.99,25.5]
print(pricesUSD)

def changePriceDecorator_v1(myFunction):
    print("Hello! Let's change your prices...")
    def simpleWrapper(argList):
        print("I've got list of prices with {} elements. Function starts working...".format(len(argList)))
        resutl=myFunction(argList)
        resutlwithDisc=list(map(lambda x: x*(1-0.15), resutl))
        print("Let's set a discount..")
        return resutlwithDisc
    return simpleWrapper

#pricesToGRN = changePriceDecorator_v1(toPriceNew)
@changePriceDecorator_v1
def toPriceNew(priceList):
    return list(map(lambda x: x*27.5, priceList))

print(toPriceNew(pricesUSD))
