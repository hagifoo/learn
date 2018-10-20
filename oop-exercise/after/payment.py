from functools import reduce
from typing import List
from currency import Currency

class Payment:

    def __init__(self, currencies: List[Currency]):
        self._currencies = currencies

    def get_currencies(self):
        return self._currencies

    def amount(self):
        return reduce(lambda x, y: x + y.amount(), self._currencies, 0)
