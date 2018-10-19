from collections import defaultdict
from currency import Currency
from currency import Yen100Coin

class ChangeMachine:

    def __init__(self):
        self._currency_collections = defaultdict(int)

    def input(self, currency: Currency):
        self._currency_collections[currency.__class__] += 1 

    def refund(self, payment: int, price: int):
        if (payment != 100) and (payment != 500):
            raise RuntimeError('payment should be 100 or 500')

        if payment == 500 and self._currency_collections[Yen100Coin] < 4:
            raise RuntimeError('payment should be 100 or 500')

        change = 0
        if payment == 100:
            self._currency_collections[Yen100Coin] += 1
            change = 0

        if payment == 500:
            self._currency_collections[Yen100Coin] -= (payment - 100) / 100
            change += (payment - price)

        return change

