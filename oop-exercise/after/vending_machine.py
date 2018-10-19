from typing import Type
from currency import Yen100Coin
from drink import Coke
from drink import DietCoke
from drink import Drink
from drink import Tea
from drink_collection import DrinkCollection
from change_machine import ChangeMachine


class VendingMachine:

    def __init__(self):
        self._cokes = DrinkCollection([Coke() for i in range(5)])
        self._diet_cokes = DrinkCollection([DietCoke() for i in range(5)])
        self._teas = DrinkCollection([Tea() for i in range(5)])
        self._change_machine = ChangeMachine()
        for i in range(10):
            self._change_machine.input(Yen100Coin())
        self._change = 0

    # 投入金額. 100円と500円のみ受け付ける.
    # return. ジュース or None
    def buy(self, payment: int, kind_of_drink: Type[Drink]):
        try:
            return self._buy(payment, kind_of_drink)
        except:
            self._change += payment
            return None

    def _buy(self, payment: int, kind_of_drink: Type[Drink]):
        self._change = self._change_machine.refund(payment, 100)

        if kind_of_drink == Coke:
            return self._cokes.pull()

        if kind_of_drink == DietCoke:
            return self._diet_cokes.pull()

        if kind_of_drink == Tea:
            return self._teas.pull()

    def refund(self):
        result = self._change
        self._change = 0
        return result
