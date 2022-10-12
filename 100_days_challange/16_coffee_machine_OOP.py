from additional_files.coffee_maker_16 import CoffeeMaker
from additional_files.menu_16 import Menu
from additional_files.money_machine_16 import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
money_machine = MoneyMachine()

while True:
    options = menu.get_items()
    guess = input(f"What would you like? ({options}): ")
    if guess == 'off':
        break
    elif guess == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(guess)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
