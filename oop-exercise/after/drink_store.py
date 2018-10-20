from typing import Type
from drink import Drink
from drink_collection import DrinkCollection

class DrinkStore:

    def __init__(self):
        self._collections = {}

    def _get_collection(self, drink_type: Type[Drink]):
        if drink_type not in self._collections:
            self._collections[drink_type] = DrinkCollection([])

        return self._collections[drink_type]

    def store(self, drink: Drink):
       	self._get_collection(drink.__class__).add(drink)

    def pull(self, drink_type: Type[Drink]):
        return self._get_collection(drink_type).pop()
