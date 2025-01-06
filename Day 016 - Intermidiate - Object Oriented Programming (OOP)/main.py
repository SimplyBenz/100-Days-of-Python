from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# CoffeeMenuItem = MenuItem()
CoffeeMenu = Menu()
CoffeeMachine = CoffeeMaker()
CoinMachine = MoneyMachine()

IsOn = True

while IsOn:

    OrderCoffee = input(f"What would you like? ({CoffeeMenu.get_items()}): ")

    if OrderCoffee == "off":
        print("Turning off the coffee machine.")
        IsOn = False
    elif OrderCoffee == "report":
        CoffeeMachine.report()
        CoinMachine.report()
    else:
        drink = CoffeeMenu.find_drink(OrderCoffee)
        if CoffeeMachine.is_resource_sufficient(drink):
            if CoinMachine.make_payment(drink.cost):
                CoffeeMachine.make_coffee(drink)
