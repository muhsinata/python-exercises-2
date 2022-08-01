from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

get_order = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

keep_ordering = True
while keep_ordering:
    order = input(f"What would you like? {get_order.get_items()}: ")
    drink = get_order.find_drink(order)
    if order == "report":
        coffee_maker.report()
        money_machine.report()
    elif order == "off":
        keep_ordering = False
    elif coffee_maker.is_resource_sufficient(drink):
        if money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
