# minzhou@bu.edu


class Stock:

    def __init__(self, symbol, name):
        self.__symbol = symbol
        self.__name = name
        self.__previousClosingPrice = 0
        self.__currentPrice = 0

    # getter
    def getName(self):
        return self.__name

    def getSymbol(self):
        return self.__symbol

    def getPreviousPrice(self):
        return self.__previousClosingPrice

    def getCurrentPrice(self):
        return self.__currentPrice

    def getChangePercent(self):
        return str(round((self.__currentPrice - self.__previousClosingPrice) / self.__previousClosingPrice, 4) * 100) + '%'

    # setter
    def setPreviousPrice(self, price):
        self.__previousClosingPrice = price

    def setCurrentPrice(self, price):
        self.__previousClosingPrice = self.__currentPrice
        self.__currentPrice = price


def main():
    stock = Stock('INTC', 'IntelCorporation')
    stock.setCurrentPrice(20.5)
    stock.setCurrentPrice(20.35)
    print('Stock name: {}  symbol: {}'.format(stock.getName(), stock.getSymbol()))
    print('Previous Price: {}'.format(stock.getPreviousPrice()))
    print('Current Price: {}'.format(stock.getCurrentPrice()))
    print('The price-change percentage is:', stock.getChangePercent())

if __name__ == '__main__':
    main()