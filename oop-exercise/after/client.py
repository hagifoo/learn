from vending_machine import VendingMachine
from drink import Coke
from drink import DietCoke

if __name__ == '__main__':
    print('# 200円を入れて 0: COKE を購入')

    money = 200
    drink_type = Coke
    vending_machine = VendingMachine()
    my_drink = vending_machine.buy(money, drink_type)
    change = vending_machine.refund()

    print('Drink: {}'.format(my_drink))
    print('Change: {}'.format(change))
    print('->100円か500円しか受け付けないのでそのまま返ってくる')

    print('# 500円を入れて 1: DIET_COKE を購入')

    money = 500
    drink_type = DietCoke
    vending_machine = VendingMachine()
    my_drink = vending_machine.buy(money, drink_type)
    change = vending_machine.refund()

    print('Drink: {}'.format(my_drink))
    print('Change: {}'.format(change))
    print('->DIET_COKEが出て400円返ってくる')

    print('# 100円を入れて 1: DIET_COKE を購入 * 6')

    vending_machine = VendingMachine()
    for i in range(6):
        money = 100
        drink_type = DietCoke
        my_drink = vending_machine.buy(money, drink_type)
        change = vending_machine.refund()

    print('Drink: {}'.format(my_drink))
    print('Change: {}'.format(change))
    print('->DIET_COKEが品切れで100円返ってくる')
