from coffe_recipe import MENU

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money" : 0,
}

#TODO Prompt user by asking “What would you like? (espresso/latte/cappuccino):"
def start_order():
    
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ")

    #TODO Turn off the Coffee Machine by entering “off” to the prompt. coffee machine should have secret code that is required to turn off.
    if coffee_type == "off":
        secret_code = input("Enter the secret code: ")
        if secret_code == "123":
            print("Turning off the coffee machine.")
            exit()
        else:
            print("Invalid secret code! Try again.")

    #TODO Print report. eg. Water: 100ml Milk: 50ml Coffee: 76g Money: $2.5
    if coffee_type == "report":
        print(f"Water: {resources["water"]}ml\nMilk: {resources["milk"]}ml\nCoffee: {resources["coffee"]}g\nMoney: ${resources["money"]}")

    if coffee_type not in MENU:
        print("Invalid coffee type! Try again.")
        exit()

    if coffee_type == "espresso":
        WaterUSE = 50
        CoffeeUSE = 18
        MoneyUSE = 1.5
    elif coffee_type == "latte":
        WaterUSE = 200
        MilkUSE = 150
        CoffeeUSE = 24
        MoneyUSE = 2.5
    elif coffee_type == "cappuccino":
        WaterUSE = 250
        MilkUSE = 100
        CoffeeUSE = 24
        MoneyUSE = 3.0

#TODO Check resources sufficient?
def check_resources():
    if resources["water"] < WaterUSE:
        print("Sorry there is not enough water.")
    elif resources["milk"] < MilkUSE:
        print("Sorry there is not enough milk.")
    elif resources["coffee"] < CoffeeUSE:
        print("Sorry there is not enough coffee.")


#TODO Process coins.
'''
Quarters: $0.25
Dimes: $0.10
Nickles: $0.05
Pennies: $0.01
'''
def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return total


#TODO Check transaction successful?
def check_transaction():
    if total >= MoneyUSE:
        change = total - MoneyUSE
        print(f"Here is ${change} in change.")
        print(f"Here is your {coffee_type} ☕️. Enjoy!")
    else:
        print("Sorry that's not enough money. Money refunded.")


#TODO Make Coffee.



start_order()