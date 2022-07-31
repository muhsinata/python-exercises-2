from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
order = input(f"What would you like? ({menu.get_items()}): ")
drink = menu.find_drink(order)

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

menu_item = MenuItem()

if order == "report":
    coffee_maker.report()
    money_machine.report()
else:
    if coffee_maker.is_resource_sufficient(order):
        money_machine.make_payment(menu_item.cost)
    else:
        print("Sorry, ingredients are insufficient.")
