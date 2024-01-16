from ingredients import MENU

should_continue = False
stock = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
            "money": 0,
        }


def flavor_cost(coffee_flavor):
    print("Please insert the designated coins.")

    quarters = int(input("How many quarters you will insert?"))
    dimes = int(input("How many dimes you will insert?"))
    nickles = int(input("How many nickles you will insert?"))
    pennies = int(input("How many pennies you will insert?"))

    money = (0.25 * quarters) + (0.10 * dimes) + (0.05 * nickles) + (0.01 * pennies)

    cost = MENU[coffee_flavor]["cost"]

    if cost > money:
        print("Sorry that's not enough money. Money Refunded.")
        return -1
    else:
        change = money - cost
        stock["money"] += money

        print(f"{money}$ received, {change}$ returned.")
        return 1


def flavor_creator(flavor):
    water = MENU[flavor]["ingredients"]["water"]
    coffee = MENU[flavor]["ingredients"]["coffee"]
    milk = MENU[flavor]["ingredients"]["milk"]

    if water < stock["water"] and coffee < stock["coffee"] and milk < stock["milk"]:
        stock["water"] -= water
        stock["coffee"] -= coffee
        stock["milk"] -= milk
        print(f"Here it is your {flavor} coffee, please enjoy!")
    else:
        print("There are not enough resources. Money refunded")


while not should_continue:
    selection = input("What would you like? ").lower()

    if selection == "off":
        break

    if selection == "report":
        print(f"Water:{stock['water']}ml\nMilk:{stock['milk']}ml\nCoffee:{stock['coffee']}g ")

    if (selection != "report" and "off") and flavor_cost(selection) >= 0:
        flavor_creator(selection)
