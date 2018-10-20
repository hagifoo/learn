from collections import defaultdict
from currency import Currency
from currency import Yen100Coin
from payment import Payment

class ChangeMachine:

    def __init__(self):
        self._currency_collections = defaultdict(int)

    def input(self, currency: Currency):
        self._currency_collections[currency.__class__] += 1 

    def refund(self, payment: Payment, price: int):
        currencies = payment.get_currencies()
        if len(currencies) != 1:
            raise RuntimeError('payment should be a currency')

        payment_amount = payment.amount()
        if (payment_amount != 100) and (payment_amount != 500):
            raise RuntimeError('payment should be 100 or 500')

        if payment_amount == 500 and self._currency_collections[Yen100Coin] < 4:
            raise RuntimeError('Not enouhg 100 coin for change')

        change = 0
        if payment_amount == 100:
            self._currency_collections[Yen100Coin] += 1
            change = 0

        if payment_amount == 500:
            self._currency_collections[Yen100Coin] -= (payment_amount - 100) / 100
            change += (payment.amount() - price)

        return change
