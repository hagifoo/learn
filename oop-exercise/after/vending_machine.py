from typing import Type
from drink import Coke
from drink import DietCoke
from drink import Drink
from drink import Tea
from drink_collection import DrinkCollection


class VendingMachine:

    def __init__(self):
        self._cokes = DrinkCollection([Coke() for i in range(5)])
        self._diet_cokes = DrinkCollection([DietCoke() for i in range(5)])
        self._teas = DrinkCollection([Tea() for i in range(5)])
        self._number_of_100_yen = 10
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
        if (payment != 100) and (payment != 500):
            self._change += payment
            return None

        if payment == 500 and self._number_of_100_yen < 4:
            self._change += payment
            return None

        if payment == 100:
            self._number_of_100_yen += 1

        if payment == 500:
            self._change += (payment - 100)
            self._number_of_100_yen -= (payment - 100) / 100

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
