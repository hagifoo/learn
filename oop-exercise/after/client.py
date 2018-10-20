from vending_machine import VendingMachine
from currency import Yen100Coin
from currency import Yen500Coin
from drink import Coke
from drink import DietCoke
from payment import Payment

if __name__ == '__main__':
    print('# 200円を入れて 0: COKE を購入')

    payment = Payment([Yen100Coin(), Yen100Coin()])
    drink_type = Coke
    vending_machine = VendingMachine()
    my_drink = vending_machine.buy(payment, drink_type)
    change = vending_machine.refund()

    print('Drink: {}'.format(my_drink))
    print('Change: {}'.format(change))
    print('->100円か500円しか受け付けないのでそのまま返ってくる')

    print('# 500円を入れて 1: DIET_COKE を購入')

    payment = Payment([Yen500Coin()])
    drink_type = DietCoke
    vending_machine = VendingMachine()
    my_drink = vending_machine.buy(payment, drink_type)
    change = vending_machine.refund()

    print('Drink: {}'.format(my_drink))
    print('Change: {}'.format(change))
    print('->DIET_COKEが出て400円返ってくる')

    print('# 100円を入れて 1: DIET_COKE を購入 * 6')

    vending_machine = VendingMachine()
    for i in range(6):
        payment = Payment([Yen100Coin()])
        drink_type = DietCoke
        my_drink = vending_machine.buy(payment, drink_type)
        change = vending_machine.refund()

    print('Drink: {}'.format(my_drink))
    print('Change: {}'.format(change))
    print('->DIET_COKEが品切れで100円返ってくる')

    print('# 500円を入れて 1: DIET_COKE を購入 * 3')

    vending_machine = VendingMachine()
    for i in range(3):
        payment = Payment([Yen500Coin()])
        drink_type = DietCoke
        my_drink = vending_machine.buy(payment, drink_type)
        change = vending_machine.refund()

    print('Drink: {}'.format(my_drink))
    print('Change: {}'.format(change))
    print('->釣り銭切れで500円返ってくる')
