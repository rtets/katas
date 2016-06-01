class Prices(object):
    def __init__(self,priceList):
        self._unitPrices = dict()
        self._specialPrices = dict()
        for row in priceList:
            item,unitPrice,specialPrice = row.split('|')
            self._unitPrices[item] = int(unitPrice)
            if specialPrice != '':
                self._specialPrices[item] = tuple(int(str) for str in specialPrice.split(' for '))

    def calculate(self,item,quantity):
        unitPrice = self._unitPrices[item]
        scount,srate = self._specialPrices[item] if item in self._specialPrices else (quantity,unitPrice)
        return (quantity/scount)*srate + (quantity%scount)*unitPrice
