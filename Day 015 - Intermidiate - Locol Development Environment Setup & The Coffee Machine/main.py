from coffe_recipe import MENU

resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 1000,
    "money" : 0,
}

coffee_type = ""

#TODO Prompt user by asking “What would you like? (espresso/latte/cappuccino):"
def start_order():
    
    global coffee_type
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ")

    #TODO Turn off the Coffee Machine by entering “off” to the prompt. coffee machine should have secret code that is required to turn off.
    if coffee_type == "off":
        print("Turning off the coffee machine.")
        exit()

    #TODO Print report. eg. Water: 100ml Milk: 50ml Coffee: 76g Money: $2.5
    elif coffee_type == "report":
        print(f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${resources["money"]}")
        start_order()

    elif coffee_type in MENU:
        print("In the menu.")
        if coffee_type == "espresso":
            WaterUSE = MENU["espresso"]["ingredients"].get("water")
            MilkUSE = MENU["espresso"]["ingredients"].get("milk",0)
            CoffeeUSE = MENU["espresso"]["ingredients"].get("coffee")
            MoneyUSE = MENU["espresso"]["cost"]
        elif coffee_type == "latte":
            WaterUSE = MENU["latte"]["ingredients"].get("water")
            MilkUSE = MENU["latte"]["ingredients"].get("water")
            CoffeeUSE = MENU["latte"]["ingredients"].get("water")
            MoneyUSE = MENU["latte"]["cost"]
        elif coffee_type == "cappuccino":
            WaterUSE = MENU["cappuccino"]["ingredients"].get("water")
            MilkUSE = MENU["cappuccino"]["ingredients"].get("milk")
            CoffeeUSE = MENU["cappuccino"]["ingredients"].get("coffee")
            MoneyUSE = MENU["cappuccino"]["cost"]
        else:
            print("Invalid coffee type! Try again.")
            exit()

        check_resources(WaterUSE, MilkUSE, CoffeeUSE, MoneyUSE)

#TODO Check resources sufficient?
def check_resources(Water, Milk, Coffee, Money):
    if resources["water"] < Water:
        print("Sorry there is not enough water.")
        exit()
    elif resources["milk"] < Milk:
        print("Sorry there is not enough milk.")
        exit()
    elif resources["coffee"] < Coffee:
        print("Sorry there is not enough coffee.")
        exit()
    else:
        resources["water"] -= Water 
        resources["milk"] -= Milk 
        resources["coffee"] -= Coffee
        process_coins(total=Money)

#TODO Process coins.
'''
Quarters: $0.25
Dimes: $0.10
Nickles: $0.05
Pennies: $0.01
'''
def process_coins(total):
    global coffee_type
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    recived_money = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    #TODO Check transaction successful?
    if recived_money >= total:
        resources["money"] += total
        change = recived_money - total
        print(f"Here is ${change} in change.")
        print(resources)
        #TODO Fix the how to refer to coffee_type in function start_order
        print(f"Here is your {coffee_type}. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")

    start_order()

#TODO Make Coffee.

start_order()