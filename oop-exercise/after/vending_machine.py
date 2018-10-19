from drink import Drink


class VendingMachine:

    def __init__(self):
        self._quantity_of_coke = 5
        self._quantity_of_diet_coke = 5
        self._quantity_of_tea = 5
        self._number_of_100_yen = 10
        self._change = 0

    # 投入金額. 100円と500円のみ受け付ける.
    # return. ジュース or None
    def buy(self, payment: int, kind_of_drink: int):

        if (payment != 100) and (payment != 500):
            self._change += payment
            return None

        if (kind_of_drink == Drink.COKE) and (self._quantity_of_coke == 0):
            self._change += payment
            return None

        if (kind_of_drink == Drink.DIET_COKE) and \
                (self._quantity_of_diet_coke == 0):
            self._change += payment
            return None

        if (kind_of_drink == Drink.TEA) and (self._quantity_of_tea == 0):
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

        if kind_of_drink == Drink.COKE:
            self._quantity_of_coke -= 1

        if kind_of_drink == Drink.DIET_COKE:
            self._quantity_of_diet_coke -= 1

        if kind_of_drink == Drink.TEA:
            self._quantity_of_tea -= 1

        return Drink(kind_of_drink)

    def refund(self):
        result = self._change
        self._change = 0
        return result
