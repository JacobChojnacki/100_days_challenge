import os

from additional_files.coffee_data_15 import resources, MENU


def calculate_amount_of_money():
    print("Please insert coins.")
    quarters = float(input("How many quarters?: "))
    dimes = float(input("How many dimes?: "))
    nickles = float(input("How many nickles?: "))
    pennies = float(input("How many pennies?: "))
    amount = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
    return amount


def coffee_machine(water=300, coffee=100, milk=200, money=0.0):
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == 'report':
        print(f"Water: {water}ml")
        print(f"Coffee: {coffee}g")
        print(f"Milk: {milk}ml")
        print(f"Money: ${money}")
        return coffee_machine(water, coffee, milk, money)
    else:
        money = calculate_amount_of_money()
        if choice == "espresso":
            espresso_cost = MENU["espresso"]["cost"]
            if money < espresso_cost:
                print("Sorry that's not enough money. Money refunded.")
            else:
                espresso_water = MENU['espresso']['ingredients']['water']
                espresso_coffee = MENU['espresso']['ingredients']['coffee']
                if espresso_water > water:
                    print("Sorry there is not enough of water")
                    return coffee_machine(money=money)
                elif espresso_coffee > coffee:
                    print("Sorry there is not enough of coffee")
                else:
                    print(f"Here is ${round((money - espresso_cost), 3)} in change.")
                    print("Here is your espresso. Enjoy!")
                    return coffee_machine(water - espresso_water, coffee - espresso_coffee)
        elif choice == "latte":
            latte_cost = MENU["latte"]["cost"]
            if money < latte_cost:
                print("Sorry that's not enough money. Money refunded.")
            else:
                latte_water = MENU['latte']['ingredients']['water']
                latte_coffee = MENU['latte']['ingredients']['coffee']
                latte_milk = MENU['latte']['ingredients']['milk']
                if latte_water > water:
                    print("Sorry there is not enough of water")
                    return coffee_machine(money=money)
                elif latte_coffee > coffee:
                    print("Sorry there is not enough of coffee")
                    return coffee_machine(money=money)
                elif latte_milk > milk:
                    print("Sorry there is not enough of water")
                    return coffee_machine(money=money)
                else:
                    print(f"Here is ${round((money - latte_cost), 3)} in change.")
                    print("Here is your latte. Enjoy!")
                    return coffee_machine(water - latte_water, coffee - latte_coffee, milk - latte_milk)
        elif choice == 'cappuccino':
            cappuccino_cost = MENU["cappuccino"]["cost"]
            if money < cappuccino_cost:
                print("Sorry that's not enough money. Money refunded.")
            else:
                cappuccino_water = MENU['cappuccino']['ingredients']['water']
                cappuccino_coffee = MENU['cappuccino']['ingredients']['coffee']
                cappuccino_milk = MENU['cappuccino']['ingredients']['milk']
                if cappuccino_water > water:
                    print("Sorry there is not enough of water")
                    return coffee_machine(money=money)
                elif cappuccino_coffee > coffee:
                    print("Sorry there is not enough of coffee")
                    return coffee_machine(money=money)
                elif cappuccino_milk > milk:
                    print("Sorry there is not enough of water")
                    return coffee_machine(money=money)
                else:
                    print(f"Here is ${round((money - cappuccino_cost), 3)} in change.")
                    print("Here is your latte. Enjoy!")
                    return coffee_machine(water - cappuccino_water, coffee - cappuccino_coffee, milk - cappuccino_milk)


coffee_machine()
