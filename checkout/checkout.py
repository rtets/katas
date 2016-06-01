class Checkout(object):
    def __init__(self,prices):
        self._prices = prices
        self._basket = dict()

    def scan(self,item):
        self._basket[item] = self._basket[item]+1 if item in self._basket else 1

    def total(self):
        return sum(self._prices.calculate(item,quantity) for item,quantity in self._basket.items())
