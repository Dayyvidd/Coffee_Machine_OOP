from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

Menu = Menu()
Coffee = CoffeeMaker()
Money = MoneyMachine()

while True:
    user_Beverage = input("What would you like? (espresso/latte/cappuccino) ")

    if user_Beverage in Menu.get_items():

        if Coffee.is_resource_sufficient(Menu.find_drink(user_Beverage)):

            cost = Menu.find_drink(user_Beverage).cost

            payment = Money.make_payment(cost)

            if payment:
                brew = Coffee.make_coffee(Menu.find_drink(user_Beverage))

    elif user_Beverage == "report":

        Coffee.report()
        Money.report()

    else:

        print(f"Sorry we do not have {user_Beverage}")


