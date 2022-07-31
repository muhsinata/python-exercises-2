# Coffee Machine

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}


def ingredient_checker(which_drink, which_resources):
    for ingredient in MENU[which_drink]["ingredients"]:
        if MENU[which_drink]["ingredients"][ingredient] > which_resources[ingredient]:
            print(f"Sorry there is no enough {ingredient}.")
            return 1
        else:
            return 0


def how_much_money_given():
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many quarters?: "))
    nickles = int(input("how many quarters?: "))
    pennies = int(input("how many quarters?: "))
    total = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return total


def money_earned(consumer_money, consumer_order):
    drink_cost = MENU[consumer_order]["cost"]
    if consumer_money >= drink_cost:
        change_amount = consumer_money - drink_cost
        print(f"Here is {round(change_amount, 2)} in change.")
        return drink_cost
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def report(resource_remain, total_revenue):
    print(f"Water: {resource_remain['water']}ml")
    print(f"Milk: {resource_remain['milk']}ml")
    print(f"Coffee: {resource_remain['coffee']}g")
    print(f"Money: ${total_revenue}")


def start_machine():
    keep_ordering = True
    revenue = 0
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }
    while keep_ordering:
        drink = input("What would you like? (espresso/latte/cappuccino): ")
        if drink == "report":
            report(resources, revenue)
        elif drink == "off":
            keep_ordering = False
        else:
            ingredient_adequacy = ingredient_checker(drink, resources)
            if ingredient_adequacy == 0:
                given_money = how_much_money_given()
                is_money_enough = money_earned(given_money, drink)
                if is_money_enough:
                    revenue += is_money_enough
                    for ingredient in MENU[drink]["ingredients"]:
                        resources[ingredient] -= MENU[drink]["ingredients"][ingredient]
                    print(f"Here is your {drink} ☕. Enjoy!")


start_machine()

