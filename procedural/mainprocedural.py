import os


def clear():
    os.system('clear')



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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

coins = {
    "quarters": 0.25,
    "dimes": 0.1,
    "nickles": 0.05,
    "pennies": 0.01,
}


def report():
  water = resources["water"]
  milk = resources["milk"]
  coffee = resources["coffee"]
  money = resources["money"]
  print(f"Water: {water}ml, \nMilk: {milk}ml \nCoffee: {coffee}g")
  print(f'Money: {money}')



def enough_resources(order, resources):
    if MENU[order]["ingredients"]["water"] > resources["water"]:
        print(f"There is not enough water")
        return False

    elif MENU[order]["ingredients"]["coffee"] > resources["coffee"]:
        print(f"There is not enough coffee")
        return False

    elif "milk" in MENU[order]["ingredients"] and MENU[order]["ingredients"]["milk"] > resources["milk"]:
        print(f"There is not enough milk")
        return False

    else:
        pricing = MENU[order]['cost']
        print(f"Total order price: {pricing} ")
        return True

def process_coins(order):
  quarters = int(input("How many quarters you want to insert? "))
  dimes = int(input("How many dimes do you want to insert? "))
  nickles = int(input("How many nickles do you want to insert? "))
  pennies = int(input("How many pennies do you want to insert? "))

  total_price = coins["quarters"] * quarters + coins["dimes"] * dimes +  coins["nickles"] * nickles + coins["pennies"] * pennies
  return total_price

def transaction_successful(order, user_payment):
  change = 0
  if MENU[order]["cost"] > user_payment:
    print("Sorry, that's not enough money. Money refunded.")
    return change
  elif MENU[order]["cost"] < user_payment:
    change = user_payment - MENU[order]["cost"]
    change = round(change, 2)
    print(f"Here is your change: {change}.")
    return change
  elif MENU[order]["cost"] == user_payment:
    print("Your coffee is almost ready")
    return change

def order_maker(order):
    resources["water"] = resources["water"] - MENU[order]["ingredients"]["water"]
    resources["coffee"] = resources["coffee"] - MENU[order]["ingredients"]["coffee"]
    if "milk" in MENU[order]["ingredients"]:
      resources["milk"] = resources["milk"] - MENU[order]["ingredients"]["milk"]
    resources["money"] = resources["money"] + MENU[order]["cost"]


print("Hello, I'm the coffee machine")
turned_on = True
while turned_on:
  order = input("What would you like? (espresso/latte/cappuccino): ")

  if order == "off":
      turned_on = False
      print("Turning off the coffee machine. Goodbye!")
      break

  if order == "report":
      report()
      continue

  if order in MENU:
    if not enough_resources(order, resources):
      continue

    user_payment = process_coins(order)

    change = transaction_successful(order, user_payment)

    if change == 0 and MENU[order]["cost"] > user_payment:
      continue

    order_maker(order)
    print(f"Here is your {order}. Enjoy!")
  else:
    print("Invalid selection. Please choose espresso, latte, or cappuccino.")
