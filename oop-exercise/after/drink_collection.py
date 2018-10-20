from typing import List
from drink import Drink

class DrinkCollection:

    def __init__(self, drinks: List[Drink]):
        self._drinks = list()
        self._drinks.extend(drinks)

    def add(self, drink):
        self._drinks.append(drink)

        return drink

    def pop(self):
        if(len(self._drinks) == 0):
            raise RuntimeError('No drink!')

        return self._drinks.pop()
